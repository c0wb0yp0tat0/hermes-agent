"""Falsifier battery — Nugget 3: remove whole-entry equality.

Delta: remove selects by whole-entry EXACT match first; a substring
old_text that matches multiple distinct entries is ambiguous/refused.
"""
import pytest

from tools.memory_tool_store import MemoryStore, ENTRY_DELIMITER


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=5000, user_char_limit=1000)
    return s


def _load(store, entries):
    (store._path_for("memory").parent / "MEMORY.md").write_text(
        ENTRY_DELIMITER.join(entries), encoding="utf-8"
    )
    store.load_from_disk()


class TestNugget3RemoveEquality:
    def test_remove_exact_entry_only(self, store):
        _load(store, ["Prefers tea", "Prefers tea with milk"])
        res = store.remove("memory", "Prefers tea")
        assert res["success"] is True
        assert store._entries_for("memory") == ["Prefers tea with milk"]

    def test_remove_substring_refuses_ambiguous(self, store):
        _load(store, ["Prefers tea", "Prefers tea with milk"])
        res = store.remove("memory", "tea")
        assert res["success"] is False
        # nothing removed
        assert store._entries_for("memory") == ["Prefers tea", "Prefers tea with milk"]

    def test_remove_substring_no_match(self, store):
        _load(store, ["alpha", "alpha beta", "beta gamma"])
        res = store.remove("memory", "alpha")
        # 'alpha' is an exact entry, so it removes only that one
        assert res["success"] is True
        assert store._entries_for("memory") == ["alpha beta", "beta gamma"]
