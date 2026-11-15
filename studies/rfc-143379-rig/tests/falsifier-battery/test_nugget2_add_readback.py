"""Falsifier battery — Nugget 2: add read-back blind spot.

Delta: `add` returns a complete terminal success dict, never None.
"""
import pytest

from tools.memory_tool_store import MemoryStore


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=2000, user_char_limit=1000)
    s.load_from_disk()
    return s


class TestNugget2AddReadback:
    def test_add_returns_result_dict_not_none(self, store):
        r = store.add("memory", "First entry")
        assert isinstance(r, dict) and r.get("success") is True

    def test_add_second_entry_terminal_payload(self, store):
        store.add("memory", "First entry")
        r = store.add("memory", "Second entry")
        assert isinstance(r, dict)
        assert r["success"] is True
        assert r["done"] is True
        assert r["entry_count"] == 2
        assert "target" in r and "usage" in r and "message" in r and "note" in r
