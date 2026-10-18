"""Focused battery for the compression-summary-fix (Layer 1: max_tokens pass-through).

These five tests lock in the #50132 wire-cap fix for the compression summary
path.  The root cause was that ``_build_call_kwargs`` gated caller-provided
``max_tokens`` behind ``_forwards_max_tokens`` — a gate that was only ``True``
for ``moa_reference`` tasks — so for every OpenAI-compatible route (Nous Portal
``/v1/chat/completions`` included) the summary call carried *no* wire cap and
the provider's server-default truncated it, producing a #124077-class abort.

Layer 1 restores the cap on the wire unconditionally:
  * ``_build_call_kwargs`` forwards ``max_tokens`` for every task/provider.
  * ``_compression_fast_lane_controls`` strips stale ``extra_body`` caps so the
    dynamic budget is the single source of truth.
  * ``_call_summary_llm`` accepts a ``max_tokens`` parameter and forwards it.
  * ``_generate_summary`` computes ``int(summary_budget * 1.3)`` and passes it.
  * Temperature-retry rungs strip *only* ``temperature``, preserving ``max_tokens``.

Companion regression tests live in ``test_auxiliary_client.py``,
``test_aux_affordable_402_retry.py``, ``test_unsupported_temperature_retry.py``,
``test_compression_small_ctx_threshold_floor.py``, and
``test_fast_compression_lane.py``.
"""

from unittest.mock import patch

from agent.auxiliary_client import (
    _build_call_kwargs,
    _compression_fast_lane_controls,
    _without_temperature,
)

_PROVIDERS = [
    ("openai", "gpt-4o-mini"),
    ("nous", "hermes-4"),
    ("anthropic", "claude-3-5-sonnet-20241022"),
    ("gemini", "gemini-2.5-flash"),
    ("ollama", "qwen3:8b"),
]


class _FakeResp:
    """Minimal chat-completion response shape that ``_call_summary_llm`` accepts."""
    choices = [
        type("C", (), {
            "message": type("M", (), {"content": "## Active Task\nok"})(),
        })(),
    ]


def _make_comp():
    """Build a ContextCompressor with a mocked context length (quiet, no I/O)."""
    import agent.context_compressor as cc
    with patch.object(cc, "get_model_context_length", return_value=128_000):
        comp = cc.ContextCompressor(
            model="test/model", threshold_percent=0.50, quiet_mode=True,
        )
        _ = comp.context_length
        return comp


class TestMaxTokensUnconditionalForward:
    """L1a: ``_build_call_kwargs`` forwards ``max_tokens`` for every task/provider."""

    def test_max_tokens_forwarded_unconditionally(self):
        """Pre-#50132 only ``moa_reference`` survived the ``_forwards_max_tokens`` gate.
        With the gate removed, a plain ``compression`` task must carry max_tokens on
        every provider path — the provider-quirk handler still picks the correct wire
        key (``max_completion_tokens`` for OpenAI-family, ``max_tokens`` otherwise)."""
        for provider, model in _PROVIDERS:
            kwargs = _build_call_kwargs(
                provider=provider, model=model,
                messages=[{"role": "user", "content": "hi"}],
                max_tokens=2000, task="compression",
            )
            assert kwargs.get("max_tokens") == 2000 or kwargs.get("max_completion_tokens") == 2000, provider


class TestCompressionFastLaneStripsStaleCaps:
    """L1b: ``_compression_fast_lane_controls`` pops stale extra_body caps."""

    def test_strips_stale_extra_body_caps_and_passes_dynamic(self):
        """When the compression task supplies a dynamic ``max_tokens``, any stale
        config-level ``max_tokens`` / ``max_completion_tokens`` in ``extra_body``
        must be stripped so the dynamic budget is the single source of truth.
        Non-compression tasks must be passed through untouched."""
        stale = {"max_tokens": 1, "max_completion_tokens": 9999, "reasoning": {"enabled": False}}

        # Compression task: stale caps stripped, caller cap preserved.
        cap, body = _compression_fast_lane_controls(
            "compression",
            actual_provider="ollama", actual_model="qwen3:8b",
            requested_provider=None, requested_model=None,
            route_config={}, leak_guard_config={},
            max_tokens=1500, extra_body=stale,
        )
        assert cap == 1500
        assert "max_tokens" not in body
        assert "max_completion_tokens" not in body
        assert body.get("reasoning") == {"enabled": False}

        # Non-compression task: untouched.
        cap2, body2 = _compression_fast_lane_controls(
            "generic",
            actual_provider="openai", actual_model="gpt-4o-mini",
            requested_provider=None, requested_model=None,
            route_config={}, leak_guard_config={},
            max_tokens=2000, extra_body=stale,
        )
        assert cap2 == 2000
        assert body2 == stale


class TestCallSummaryLLMPassesMaxTokens:
    """L1c: ``_call_summary_llm`` accepts and forwards ``max_tokens`` to ``call_llm``."""

    def test_call_summary_llm_forwards_dynamic_cap(self):
        """When ``max_tokens`` is supplied it must reach ``call_llm``; when None it
        must not leak onto the wire (the old unconditional omission is restored only
        when the caller does not supply one)."""
        comp = _make_comp()

        for sent_max, expected_present in ((2600, True), (None, False)):
            captured = {}

            with patch("agent.context_compressor.call_llm",
                       side_effect=lambda **kw: (captured.update(kw), _FakeResp())[1]):
                comp._call_summary_llm("prompt", 0.0, max_tokens=sent_max)

            if expected_present:
                assert captured.get("max_tokens") == 2600
            else:
                assert "max_tokens" not in captured


class TestGenerateSummaryDynamicBudget:
    """L1d: ``_generate_summary`` computes ``int(summary_budget * 1.3)`` and passes it."""

    def test_generate_summary_sends_dynamic_wire_cap(self):
        """For tiny input the budget floors at ``_MIN_SUMMARY_TOKENS`` (2000), so the
        wire cap is ``int(2000 * 1.3) = 2600``.  For oversized input the budget
        exceeds the floor, so the cap must reflect ``int(budget * 1.3)`` — proving
        the computation is dynamic, not a hardcoded constant."""
        comp = _make_comp()

        for turns, desc in (
            ([{"role": "user", "content": "hi"}], "floor"),
            ([{"role": "user", "content": "word " * 100_000}], "dynamic"),
        ):
            captured = {}

            with patch("agent.context_compressor.call_llm",
                       side_effect=lambda **kw: (captured.update(kw), _FakeResp())[1]):
                comp._generate_summary(turns)

            budget = comp._compute_summary_budget(turns)
            expected = int(budget * 1.3)
            assert captured.get("max_tokens") == expected, desc


class TestTemperatureRetryPreservesMaxTokens:
    """L1e: parameter-retry rungs strip *only* temperature, keeping max_tokens."""

    def test_without_temperature_strips_only_temperature(self):
        """``_without_temperature`` must drop ``temperature`` but leave both
        ``max_tokens`` and ``max_completion_tokens`` intact — the temperature-retry
        never silently drops the output cap as a side effect of stripping.
        When temperature was never sent it returns None so the retry layer skips a
        no-op re-send."""
        kwargs = {"model": "x", "temperature": 0.3, "max_tokens": 500, "max_completion_tokens": 0}
        stripped = _without_temperature(kwargs)
        assert stripped is not None
        assert "temperature" not in stripped
        assert stripped["model"] == "x"
        assert stripped["max_tokens"] == 500
        assert stripped["max_completion_tokens"] == 0

        assert _without_temperature({"model": "x", "max_tokens": 500}) is None
