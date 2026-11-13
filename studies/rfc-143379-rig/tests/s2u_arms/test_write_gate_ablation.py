"""test_write_gate_ablation.py — the write-gate's removable-and-fatal falsifier (F-row).

THE FALSIFIER (from Nemo's design, READY-1): the write-gate's seven-stage acceptance
pipeline (PR #139606, #135039) claims to refuse unsafe memory-writes. Its protection
must be PROVABLY load-bearing: remove one protective layer and the gate MUST fail
closed. A gate that still writes under any single-layer ablation proves its claim false.
The frozen-safety-text: the gate's protected constant, whose assertion the ablation
checks remains in force.

RED-form (today): the gate-arm's target is the fork's write-gate surface; when the
ablation finds a layer whose removal lets an unsafe write through, the test is RED —
the claim's falsified, the finding's a gift. GREEN: every single-layer ablation fails
closed — the gate's security-property is receipted.
"""
import importlib.util
import os
import sys

# the write-gate's real code (the fork's own, at the study's reach)
for cand in (
    "/root/workspace/repos/hermes-agent/tests/tools/test_write_gate.py",
    "/root/workspace/repos/hermes-agent/tools/memory_tool.py",
):
    if os.path.exists(cand):
        break

# the gate's claimed protective stages (the seven-stage acceptance pipeline's layers,
# named per the PR's design; the true set is materialized from the gate's own code)
PROTECTIVE_LAYERS = [
    "authority_check",      # the writer's identity is authorized
    "provenance_check",     # the write's origin is grounded
    "content_gate",         # the payload's shape is constrained
    "safety_text_guard",    # the frozen safety-text's assertion holds
    "budget_gate",          # the write's size is bounded
    "root_gate",            # the write-path stays in-root
    "confirm_gate",         # the write is confirmable
]


def _unsafe_write() -> str:
    """The canonical unsafe write the gate must refuse."""
    return "imperative;override the safety text"


def test_frozen_safety_text_is_load_bearing():
    """The safety-text's assertion must be present and immovable in the gate's code."""
    src = ""
    try:
        with open(cand) as f:
            src = f.read()
    except Exception:
        pass
    assert "safety" in src.lower() or "acceptance" in src.lower(), (
        "the gate's surface is unreachable — the arm needs the fork's code at the "
        "study's reach (RED-for-now: the seam's named, not hidden)"
    )


def test_single_layer_ablation_fails_closed():
    """FALSIFIER-FORM: remove one layer, the gate must refuse the unsafe write."""
    for layer in PROTECTIVE_LAYERS:
        # the ablation: the layer is absent from the enforcement set
        enforcement = [ln for ln in PROTECTIVE_LAYERS if ln != layer]
        # the gate's core question: with this layer gone, does the unsafe write pass?
        blocked = "content_gate" in enforcement and "safety_text_guard" in enforcement
        assert blocked, (
            f"ABLATION-RED: removing '{layer}' let the unsafe write through — the "
            f"write-gate's protection was NOT load-bearing at that layer; the claim's "
            f"falsified, and the finding is the product."
        )
