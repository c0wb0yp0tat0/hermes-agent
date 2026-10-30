"""Fix 1 — cache-coherence contract (#141876): read must never mutate the shared cache.

A stale disk snapshot must never roll back newer in-process entries. ``read()``
refreshes from disk but treats the in-memory cache as append-only-authoritative:
it parses disk entries and returns them WITHOUT overwriting ``memory_entries``
/ ``user_entries`` via ``_set_entries``.

Red (before fix): read() calls self._set_entries(), rolling the cache back to the
disk snapshot — a concurrent add()'s cache update is silently lost.
Green (after fix): read() is cache-transparent; the shared cache is untouched.
"""

import json

import pytest

from tools.memory_tool import MemoryStore, _memory_tool


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=500, user_char_limit=300)
    s.load_from_disk()
    return s


class TestFix1CacheCoherence:

    def test_concurrent_read_does_not_roll_back_cache(self, store):
        """The core contract: a cache state set ahead of disk survives a read().

        Simulates a concurrent add() that has already updated the in-process
        cache but not yet committed to disk. read() reads the (stale) disk,
        but must NOT overwrite the cache — otherwise the concurrent write is
        silently lost (#141876).
        """
        store.add("memory", "persist this to disk")
        # Simulate a concurrent add that updated cache but not yet flushed to disk:
        cache = store._entries_for("memory")
        cache.append("concurrent write not yet on disk")
        store._set_entries("memory", cache)

        result = store.read("memory")
        assert result["success"] is True
        # The key assertion: "concurrent write not yet on disk" must survive.
        assert "concurrent write not yet on disk" in store.memory_entries, (
            "read() rolled back the in-process cache — concurrent write was lost (#141876)"
        )

    def test_read_does_not_call_set_entries(self, store):
        """read() must not touch _set_entries — the cache is owned by _mutate."""
        store.add("memory", "disk entry")
        called = []
        original = store._set_entries
        store._set_entries = lambda target, entries: (
            called.append((target, list(entries))),
            original(target, entries),
        )[1]

        store.read("memory")
        assert called == [], (
            f"read() invoked _set_entries with {called!r} — cache mutation is forbidden (#141876)"
        )

    def test_read_returns_disk_content_but_preserves_cache(self, store):
        """read() returns the current disk content AND leaves the cache intact."""
        store.add("memory", "disk-only entry")
        # Add a second entry to the cache that isn't yet on disk.
        store._set_entries("memory", store._entries_for("memory") + ["cache-only entry"])

        result = store.read("memory")
        assert result["success"] is True
        assert "disk-only entry" in result["entries"]
        # Cache retains BOTH entries.
        assert "disk-only entry" in store.memory_entries
        assert "cache-only entry" in store.memory_entries

    def test_concurrent_add_read_no_cache_loss(self, store):
        """Interleaved add()/read() cycles must never drop entries from the cache."""
        store.add("memory", "seed")

        for i in range(15):
            new_entry = f"concurrent-{i:02d}"
            store.add("memory", new_entry)  # updates cache via _mutate
            store.read("memory")            # must not roll cache back

            assert new_entry in store.memory_entries, (
                f"cache lost entry {new_entry} after read() (#141876)"
            )

        # Final cache has all entries.
        assert len(store.memory_entries) == 16  # seed + 15

    def test_read_dispatch_path_does_not_mutate_cache(self, store):
        """The dispatch layer's read action must also be cache-transparent."""
        store.add("memory", "dispatch entry")
        # Simulate a concurrent write that updated cache but not yet flushed to disk.
        store._set_entries("memory", store._entries_for("memory") + ["cache-only dispatch entry"])
        cache_before = list(store.memory_entries)

        outcome, _ = _memory_tool("read", "memory", None, None, None, None, store)
        assert outcome == "success"

        assert store.memory_entries == cache_before, (
            "dispatch read() mutated the shared cache (#141876)"
        )
        assert "cache-only dispatch entry" in store.memory_entries, (
            "dispatch read() rolled back the concurrent cache write (#141876)"
        )
