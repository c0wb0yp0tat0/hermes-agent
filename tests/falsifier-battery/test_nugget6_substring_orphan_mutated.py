"""Falsifier battery — Nugget 6: mutated substring-orphan case.

The divergence's lesson (nugget 6): after the exact orphan entry is removed,
a substring-matching remove('foo') must NOT silently hit and erase the
structural anchor '@doc:foobar'.

Red-before (un-fixed head e366d9f8): the mutation is the reachable seam —
after the orphan 'foo' is removed, remove('foo') selects the anchor by
substring and erases it (ANCHOR_ERASED). The pre-fix xfail test
'test_mutated_orphan_case_refuses_wrong_target' (strict=False) encoded this
surviving seam; that xfail is the receipt of the seam.

Green-after (fixed head, new tip): manifest-index resolution makes '@doc:'
anchors structural — not addressable entries — so remove('foo') now refuses
with no_match instead of silently erasing the anchor.

The strengthened assertion (strict tightening) is the fixed-contract
falsifier; the pre-fix xfail is the seam's receipt, now closed.
"""
import pytest

@pytest.fixture(autouse=True)
def _nugget6_substrate_guard():
    """The nugget-6 substrate (MemoryStore.orphan_doc_names) lands at the whole-anchor;
    at pins without it the nugget self-skips with the reason recorded (the skip-discipline)."""
    from tools.memory_tool_store import MemoryStore
    if not hasattr(MemoryStore, "orphan_doc_names"):
        pytest.skip("the nugget-6 substrate (orphan_doc_names) is absent at this pin")


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


class TestNugget6SubstringOrphanMutated:
    def test_mutated_orphan_case_refuses_wrong_target(self, store):
        # Construct the mutation FIRST: the orphan 'foo' is removed, leaving
        # only the structural anchor '@doc:foobar'. The exact-anchor's been
        # removed (the orphan is already gone) — that construction is the
        # divergence's lesson, not the xfail fallback.
        _load(store, ["@doc:foobar", "foo"])
        res_orphan = store.remove("memory", "foo")
        assert res_orphan["success"] is True, res_orphan
        assert store._entries_for("memory") == ["@doc:foobar"], (
            "the anchor must survive the orphan's removal"
        )

        # Mutable case (the seam on the un-fixed head): substring 'foo' now
        # selects the anchor and erases it. The fixed-contract falsifier —
        # the strengthened assertion (strict tightening) — must refuse:
        # remove('foo') must NOT silently hit '@doc:foobar'.
        res = store.remove("memory", "foo")
        assert res["success"] is False, res
        assert "@doc:foobar" in store._entries_for("memory"), (
            "the anchor must survive the substring remove"
        )
