"""Falsifier battery — Nugget 6: substring-orphan edge (@doc:foobar).

Divergence resolution (see lane report):
  * Shape A (design-delta probe): `_find_unique_match(['@doc:foobar','foo'], 'foo')`
    -> (index=1, ambiguous=False)  HOLDS on the current head (exact-first arm).
  * Shape B (seam-probe, mutated): after the orphan 'foo' is transformed,
    a substring 'foo' still resolves into '@doc:foobar' and removes it.
    FALSIFIED on the current head — the surviving seam.

The delta's falsifier must assert the class is provably gone. The
specified (weaker) assertion is Shape A. The strengthened assertion
(mutated case) is recorded as a surviving seam (xfail) until the
manifest-index resolution lands.
"""
import pytest

@pytest.fixture(autouse=True)
def _nugget6_substrate_guard():
    """The nugget-6 substrate (MemoryStore.orphan_doc_names) lands at the whole-anchor;
    at pins without it the nugget self-skips with the reason recorded (the skip-discipline)."""
    from tools.memory_tool_store import MemoryStore
    if not hasattr(MemoryStore, "orphan_doc_names"):
        pytest.skip("the nugget-6 substrate (orphan_doc_names) is absent at this pin")


from tools.memory_tool_store import (
    MemoryStore,
    ENTRY_DELIMITER,
    _find_unique_match,
)


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


class TestNugget6SubstringOrphan:
    def test_find_unique_match_orphan_is_unique_exact(self):
        # The design-delta's specified falsifier (Shape A): HOLDS on head.
        idx, ambiguous = _find_unique_match(["@doc:foobar", "foo"], "foo")
        assert idx == 1
        assert ambiguous is False

    def test_substring_matches_inside_doc_anchor(self):
        # Documents the surviving class: substring search matches 'foo'
        # inside '@doc:foobar' (index 0) as well as the orphan (index 1).
        from tools.memory_tool_store import _substring_matches
        assert _substring_matches(["@doc:foobar", "foo"], "foo") == [0, 1]

    @pytest.mark.xfail(
        strict=False,
        reason="surviving seam: mutated orphan case still removes @doc:foobar "
               "(substring-orphan class not yet dissolved by manifest-index resolution)",
    )
    def test_mutated_orphan_case_refuses_wrong_target(self, store):
        # Strengthened falsifier: after the orphan 'foo' is transformed, a
        # substring 'foo' must NOT silently eradicate '@doc:foobar'.
        _load(store, ["@doc:foobar", "foo"])
        store.patch("memory", "foo", "BAR")
        res = store.remove("memory", "foo")
        assert not res.get("success", False) or "@doc:foobar" in store._entries_for("memory")

    def test_orphan_doc_names_whole_anchor(self, tmp_path, monkeypatch):
        # patch-b: orphan_doc_names uses whole-anchor token match (fixed class).
        import os
        from pathlib import Path
        docs = tmp_path / "docs"
        docs.mkdir(exist_ok=True)
        (docs / "foobar.md").write_text("x", encoding="utf-8")
        (docs / "foo.md").write_text("y", encoding="utf-8")
        (tmp_path / "MEMORY.md").write_text("@doc:foobar\n", encoding="utf-8")
        monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
        s = MemoryStore()
        # 'foobar' anchor present -> not orphan; 'foo' anchor absent -> orphan
        assert "foo" in s.orphan_doc_names()
        assert "foobar" not in s.orphan_doc_names()
