"""Falsifier battery — Nugget 4: patch sibling-content false-pass.

Delta: patch confines the span to the matched (exact) entry; a patch on
'foo' never rewrites a sibling 'foo-bar'.
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


class TestNugget4PatchSibling:
    def test_patch_exact_entry_only(self, store):
        _load(store, ["foo", "foo-bar"])
        res = store.patch("memory", "foo", "baz")
        assert res["success"] is True
        assert store._entries_for("memory") == ["baz", "foo-bar"]

    def test_patch_does_not_touch_sibling(self, store):
        _load(store, ["foo", "foo-bar"])
        store.patch("memory", "foo", "baz")
        assert "foo-bar" in store._entries_for("memory")
