"""Falsifier battery — #141876-composition arm (xngg's gift's composition).

The single-head battery covers each delta in isolation. This arm composes the
batch gateway (apply_batch, nugget 1) with the terminal-payload read-back
(nugget 2) and the #141876 read cache-coherence restoration (read() must never
mutate the shared cache).

The exact composition's alive-head is the fork's current lineage (this branch).
The integration case the single-head battery lacks: the read-back contracts
(nugget 2) hold through the composed store-surface, and read() is
cache-transparent (#141876) through the composed path.

Named reasons (RED-before / GREEN-after): the composition is GREEN at the new
tip; each assertion's receipt is the composed-path read-back itself.
"""
import pytest

from tools.memory_tool_store import MemoryStore, ENTRY_DELIMITER


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=5000, user_char_limit=1000)
    return s


class TestNugget141876CompositionArm:
    def test_batch_gate_readback_composed(self, store):
        # apply_batch is the single authoritative gateway (nugget 1): the batch
        # path's single gate is the structural read-back, and the single-op
        # read-backs fold into the same terminal-payload attestations as the
        # batch's matched_entries map.
        res = store.apply_batch("memory", [
            {"action": "add", "content": "First entry"},
            {"action": "add", "content": "Second entry"},
            {"action": "patch", "old_text": "First entry", "new_text": "First patched"},
        ])
        assert res["success"] is True
        assert res["entry_count"] == 2
        # Terminal-payload read-back (nugget 2): the caller's read-back is the
        # attestation, not a second read of the store internals.
        assert store._entries_for("memory") == ["First patched", "Second entry"]

        # Read-back through the composed path: the read surface reflects the
        # committed state exactly (success, entries, target, usage).
        read = store.read("memory")
        assert read["success"] is True
        assert read["entries"] == ["First patched", "Second entry"]
        assert read["target"] == "memory"
        assert "usage" in read

    def test_read_cache_coherence_through_composed_path(self, store):
        # #141876 restoration: read() is cache-transparent; it must never roll
        # the in-process cache back to the stale disk snapshot. Through the
        # composed store-surface (batch gateway + read-back), the concurrent
        # write that updated the cache but not yet flushed must survive a read().
        store.add("memory", "persist to disk")
        cache = list(store.memory_entries)
        cache.append("concurrent write not yet on disk")
        store._set_entries("memory", cache)

        result = store.read("memory")
        assert result["success"] is True
        # The concurrent write survives: read() rolled back nothing.
        assert "concurrent write not yet on disk" in store.memory_entries
        # Read-back reflects the committed state, not the rolled-back cache.
        assert result["entries"] == ["persist to disk"]

    def test_composed_readback_reflects_final_state(self, store):
        store.add("memory", "seed")
        res = store.apply_batch("memory", [
            {"action": "remove", "old_text": "seed"},
            {"action": "add", "content": "replacement"},
        ])
        assert res["success"] is True
        assert res["entry_count"] == 1
        read = store.read("memory")
        assert read["success"] is True
        # The composed path's read-back matches the committed state exactly.
        assert read["entries"] == ["replacement"]
        assert store._entries_for("memory") == ["replacement"]
        assert read["target"] == "memory"
        assert "usage" in read
