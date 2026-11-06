"""Falsifier battery — Nugget 141876 composition arm.

The #141876-restoration (cache coherence) composed with the memory store:
read() must never roll back the in-process cache, and the battery's
read-back contracts (nuggets 2-4) hold through the composed path.

The alive-head is the fork's current lineage (fix141876 is in the lineage,
so this integration case is GREEN on the current head).
"""

import pytest

@pytest.fixture(autouse=True)
def _read_substrate_guard():
    """The #141876-composition family asserts the restored-read's substrate; at pins
    predating the restoration the read-dependent tests self-skip (the skip-discipline)."""
    from tools.memory_tool_store import MemoryStore
    if not hasattr(MemoryStore, "read"):
        pytest.skip("the restored-read substrate is absent at this pin (the 141876-family)")


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


class TestNugget141876Composition:
    def test_read_back_contracts_hold_through_cache_coherent_store(self, store):
        # Nugget 2 read-back: add returns a terminal payload attestation.
        add_res = store.add("memory", "First entry")
        assert add_res["success"] is True and add_res["entry_count"] == 1

        # Nugget 3 remove equality: remove by whole-entry exact match.
        _load(store, ["exact-one", "exact-one duplicate"])
        rem_res = store.remove("memory", "exact-one")
        assert rem_res["success"] is True
        assert store._entries_for("memory") == ["exact-one duplicate"]

        # Nugget 4 patch sibling: patch confines to the matched entry.
        _load(store, ["foo", "foo-bar"])
        patch_res = store.patch("memory", "foo", "baz")
        assert patch_res["success"] is True
        assert store._entries_for("memory") == ["baz", "foo-bar"]

        # #141876-restoration: staged write ahead of disk must survive read().
        cache = store._entries_for("memory") + ["staged-ahead"]
        store._set_entries("memory", cache)

        # read() through the composed path: must not roll back the cache.
        read_res = store.read("memory")
        assert read_res["success"] is True
        assert "staged-ahead" in store.memory_entries, (
            "read() rolled back the in-process cache (#141876)"
        )
        assert "staged-ahead" not in read_res["entries"], (
            "read() returned the committed disk snapshot, not the cache"
        )
        assert read_res["entries"] == ["baz", "foo-bar"], (
            "read-back return contract broken through the composed path"
        )
