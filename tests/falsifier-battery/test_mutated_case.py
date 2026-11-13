"""Falsifier battery — Nugget 6 (mutated case): the substring-orphan seam.

RED-before (current head): on the un-fixed path the mutation's behavior is
the reachable seam — after the orphan 'foo' is transformed, a substring
'remove('foo')' must NOT silently hit '@doc:foobar'.

GREEN-after (delta's fix lands): the manifest-index resolution makes the
whole-anchor token match hold even in the mutated state; the test passes.

The existing xfail test in test_nugget6_substring_orphan.py is the receipt
(the seam is real and reachable); this hard assertion is the seam-mutation
(the primary shape).
"""

import pytest

@pytest.fixture(autouse=True)
def _read_substrate_guard():
    """The mutated-case's refusal-assertion rides the restored-read's substrate;
    at pins predating the restoration it self-skips (the skip-discipline)."""
    from tools.memory_tool_store import MemoryStore
    if not hasattr(MemoryStore, "read"):
        pytest.skip("the restored-read substrate is absent at this pin (the mutated-case)")


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


class TestMutatedCase:
    def test_mutated_orphan_case_refuses_wrong_target(self, store):
        # RED-before: the orphan 'foo' has been transformed (patch), and a
        # substring 'foo' is still matched against '@doc:foobar' (index 0),
        # silently eradicating the whole anchor.
        _load(store, ["@doc:foobar", "foo"])
        store.patch("memory", "foo", "BAR")
        res = store.remove("memory", "foo")
        # Fixed-contract: the remove must refuse the wrong target.
        assert not res.get("success", False) or "@doc:foobar" in store._entries_for("memory")
