"""Fix 4 — source-level consent deny (#116834, #116846): deny before gate or disk.

The SYNTHETIC-CONSENT-CODE- marker triggers a refusal in ``_memory_tool``
BEFORE the write gate, before stage_write(), before any disk serializer
(Kevin's §6). Denied batch members are filtered (clean ops proceed); if all
members are denied the entire batch is refused.

Red (before fix): consent content flowed through to store.add() and was
persisted to MEMORY.md/USER.md on disk.
Green (after fix): consent content is refused before touching disk.
"""

import json
import os

import pytest

from tools.memory_tool import MemoryStore, _memory_tool

# The marker is defined locally so this test file can be collected even
# before Fix 4 adds the symbol to the module (red-to-green demonstration).
TEST_CONSENT_MARKER = "SYNTHETIC-CONSENT-CODE-"

# These helpers exist only after Fix 4 is applied to memory_tool.py.
try:
    from tools.memory_tool import (
        _SOURCE_CONSENT_MARKER,
        _contains_consent_deny,
        _op_consent_denied,
    )
except ImportError:
    _SOURCE_CONSENT_MARKER = TEST_CONSENT_MARKER
    _contains_consent_deny = None
    _op_consent_denied = None


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=500, user_char_limit=300)
    s.load_from_disk()
    return s


@pytest.fixture()
def large_store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=100_000, user_char_limit=100_000)
    s.load_from_disk()
    return s


def _load_scenarios():
    path = os.path.join(os.path.dirname(__file__), "checkout", "consent_scenarios.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _scan_disk_for_marker(search_root):
    """Walk every file under search_root looking for the consent marker."""
    found = []
    for dirpath, _dirs, filenames in os.walk(search_root):
        for fname in filenames:
            if fname.endswith(".lock"):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                if _SOURCE_CONSENT_MARKER in text:
                    found.append(fpath)
            except (OSError, UnicodeDecodeError):
                continue
    return found


class TestFix4ConsentDeny:

    def test_consent_marker_is_detectable(self):
        """Sanity: the marker detection helper works."""
        assert _contains_consent_deny("SYNTHETIC-CONSENT-CODE-PX7412: do not save")
        assert not _contains_consent_deny("ordinary memory content")
        assert not _contains_consent_deny("")
        assert not _contains_consent_deny(None)

    def test_op_consent_denied_detects_batch_members(self):
        """The batch-level detector keys on content / new_text."""
        assert _op_consent_denied({"action": "add",
                                   "content": "SYNTHETIC-CONSENT-CODE-PX7412: nope"})
        assert not _op_consent_denied({"action": "add", "content": "routine note"})
        assert not _op_consent_denied({"action": "remove", "old_text": "delete me"})

    def test_no_save_never_lands_single(self, large_store, tmp_path):
        """All 8 single-op scenarios: consent content is refused, never written to disk."""
        scenarios = [s for s in _load_scenarios() if s["kind"] == "single"]
        assert len(scenarios) == 8

        for sc in scenarios:
            content = sc["content"]
            target = sc["target"]
            assert _SOURCE_CONSENT_MARKER in content

            outcome, result_json = _memory_tool(
                "add", target, content, None, None, None, large_store
            )
            result = json.loads(result_json)
            assert outcome == "rejected", (
                f"scenario {sc['id']}: expected rejection, got {outcome}"
            )
            assert result["success"] is False
            assert _SOURCE_CONSENT_MARKER in result["error"]

        # After all single-op attempts, no marker on disk anywhere.
        leaked = _scan_disk_for_marker(str(tmp_path))
        assert leaked == [], f"consent marker leaked to: {leaked}"

    def test_no_save_never_lands_batch(self, large_store, tmp_path):
        """All 4 batch scenarios: consent ops filtered or entire batch refused."""
        scenarios = [s for s in _load_scenarios() if s["kind"] == "batch"]
        assert len(scenarios) == 4

        for sc in scenarios:
            ops = sc["operations"]
            target = sc["target"]
            markers = [op for op in ops if _SOURCE_CONSENT_MARKER in (op.get("content") or "")]
            clean = [op for op in ops if _SOURCE_CONSENT_MARKER not in (op.get("content") or "")]

            outcome, result_json = _memory_tool(
                None, target, None, None, None, ops, large_store
            )

            if not clean:
                # All ops carry the marker → entire batch refused.
                assert outcome == "rejected", f"scenario {sc['id']}: expected rejection"
                result = json.loads(result_json)
                assert result["success"] is False
            else:
                # Mixed batch: clean ops proceed, marker ops dropped.
                assert outcome == "success", (
                    f"scenario {sc['id']}: clean ops should proceed, got {outcome}"
                )

            # No marker on disk regardless of accept/reject.
            leaked = _scan_disk_for_marker(str(tmp_path))
            assert leaked == [], f"scenario {sc['id']}: marker leaked to: {leaked}"

    def test_no_save_denies_before_disk(self, large_store, tmp_path):
        """The deny fires before any disk write: the file is never created."""
        content = "SYNTHETIC-CONSENT-CODE-PX7412: test deny-before-disk"
        memory_path = tmp_path / "MEMORY.md"
        assert not memory_path.exists()

        outcome, result_json = _memory_tool(
            "add", "memory", content, None, None, None, large_store
        )
        assert outcome == "rejected"
        # No file created — the deny short-circuited before serialization.
        assert not memory_path.exists()

    def test_no_save_denies_before_gate_stage(self, large_store, tmp_path):
        """The deny fires before the write gate / stage_write path (Kevin's §6)."""
        content = "SYNTHETIC-CONSENT-CODE-PX7412: bypass gate"
        outcome, result_json = _memory_tool(
            "add", "memory", content, None, None, None, large_store
        )
        assert outcome == "rejected"
        result = json.loads(result_json)
        assert result["success"] is False
        assert _SOURCE_CONSENT_MARKER in result["error"]
        # Disk untouched.
        memory_path = tmp_path / "MEMORY.md"
        if memory_path.exists():
            assert _SOURCE_CONSENT_MARKER not in memory_path.read_text(encoding="utf-8")

    def test_batch_clean_ops_proceed_when_marker_present(self, large_store, tmp_path):
        """In a mixed batch, the clean op is saved while the marker op is dropped."""
        ops = [
            {"action": "add", "content": "routine: lab fixtures are disposable"},
            {"action": "add", "content": "SYNTHETIC-CONSENT-CODE-PX7412: user asked NOT to save this"},
        ]
        outcome, result_json = _memory_tool(None, "memory", None, None, None, ops, large_store)
        assert outcome == "success"
        result = json.loads(result_json)
        assert result["success"] is True

        # The clean entry was saved to disk.
        memory_path = tmp_path / "MEMORY.md"
        assert memory_path.exists()
        disk_text = memory_path.read_text(encoding="utf-8")
        assert "routine: lab fixtures are disposable" in disk_text
        assert _SOURCE_CONSENT_MARKER not in disk_text

    def test_all_twelve_scenarios_no_marker_on_disk(self, large_store, tmp_path):
        """The 12-scenario battery: zero markers leak to disk."""
        scenarios = _load_scenarios()
        assert len(scenarios) == 12

        for sc in scenarios:
            if sc["kind"] == "single":
                _memory_tool(
                    "add", sc["target"], sc["content"], None, None, None, large_store,
                )
            else:
                _memory_tool(
                    None, sc["target"], None, None, None, sc["operations"], large_store,
                )

        leaked = _scan_disk_for_marker(str(tmp_path))
        assert leaked == [], f"markers leaked to: {leaked}"
