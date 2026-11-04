"""Falsifier battery — Nugget 1: Stage-7 batch-path bypass.

Delta: the batch path collapses into a single authoritative gateway
(`store.apply_batch`). Falsifier: an empty operations batch is rejected
up-front with ``{'success': False, 'error': 'operations list is empty.', ...}``
and zero mutation; a batch that contains a failing op is all-or-nothing.
"""
import os

import pytest

from tools.memory_tool_store import MemoryStore, ENTRY_DELIMITER


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=2000, user_char_limit=1000)
    s.load_from_disk()
    return s


class TestNugget1BatchGateway:
    def test_empty_operations_rejected(self, store):
        res = store.apply_batch("memory", [])
        assert res["success"] is False
        assert res["error"] == "operations list is empty."
        assert store._entries_for("memory") == []

    def test_empty_batch_does_not_mutate(self, store):
        (store._path_for("memory").parent / "MEMORY.md").write_text(
            "first entry", encoding="utf-8"
        )
        # reload to populate
        store.load_from_disk()
        before = list(store._entries_for("memory"))
        res = store.apply_batch("memory", [])
        assert res["success"] is False
        assert store._entries_for("memory") == before

    def test_batch_all_or_nothing_on_bad_op(self, store):
        store.add("memory", "keep me")
        before = list(store._entries_for("memory"))
        res = store.apply_batch("memory", [
            {"action": "remove", "old_text": "keep me"},
            {"action": "remove", "old_text": "does not exist"},
        ])
        assert res["success"] is False
        # nothing applied
        assert store._entries_for("memory") == before

    def test_apply_memory_pending_empty_batch_rejected(self, tmp_path, monkeypatch):
        monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
        from tools.memory_tool import apply_memory_pending
        store = MemoryStore(memory_char_limit=2000, user_char_limit=1000)
        store.load_from_disk()
        payload = {"action": "batch", "target": "memory", "operations": []}
        res = apply_memory_pending(payload, store)
        assert isinstance(res, dict) and res.get("success") is False
