"""Fix 3 — schema dispatch contract (#139606): never advertise an action the store can't perform.

The schema's action enum must only include "read" when the store actually
implements ``read()``. At dispatch time, a store without ``read`` must be
refused cleanly (not crashed with AttributeError).

Red (before fix): a store lacking read() caused AttributeError at dispatch;
the schema advertised "read" unconditionally.
Green (after fix): dispatch fails closed with read_unavailable; schema
narrowly includes "read" only when hasattr(store, "read").
"""

import json

import pytest

from tools.memory_tool import (
    MemoryStore,
    _memory_tool,
    _build_memory_schema_overrides,
)


@pytest.fixture()
def store(tmp_path, monkeypatch):
    monkeypatch.setattr("tools.memory_tool.get_memory_dir", lambda: tmp_path)
    s = MemoryStore(memory_char_limit=500, user_char_limit=300)
    s.load_from_disk()
    return s


class TestFix3SchemaContract:

    def test_dispatch_works_when_store_has_read(self, store):
        """Happy path: a store with read() dispatches the read action."""
        store.add("memory", "readable entry")
        outcome, result_json = _memory_tool("read", "memory", None, None, None, None, store)
        result = json.loads(result_json)
        assert outcome == "success"
        assert result["success"] is True
        assert "readable entry" in result["entries"]

    def test_dispatch_fails_closed_without_read(self):
        """A store lacking read() must be refused cleanly, not AttributeError (#139606)."""

        class StoreWithoutRead:
            """Minimal store stand-in missing the read() primitive (#139606)."""
            memory_entries = []
            user_entries = []
            memory_char_limit = 500
            user_char_limit = 300
            memory_enabled = True
            user_profile_enabled = True

            def target_enabled(self, target):
                return True

        store_no_read = StoreWithoutRead()
        assert not hasattr(store_no_read, "read"), "precondition: store must NOT have read"

        # Must not raise AttributeError.
        outcome, result_json = _memory_tool("read", "memory", None, None, None, None, store_no_read)
        result = json.loads(result_json)

        assert outcome == "rejected"
        assert result["success"] is False
        assert "not available" in result["error"]

    def test_dispatch_without_read_does_not_raise(self):
        """The dispatch path must not raise any exception for a read-less store."""

        class MinimalStore:
            def target_enabled(self, target):
                return True
            def _entries_for(self, target):
                return []

        store_no_read = MinimalStore()
        # Must not raise AttributeError or anything else.
        outcome, result_json = _memory_tool("read", "memory", None, None, None, None, store_no_read)
        assert outcome == "rejected"
        json.loads(result_json)  # parses cleanly

    def test_schema_advertises_read_when_present(self):
        """When MemoryStore has read(), the schema includes it in the enum."""
        if hasattr(MemoryStore, "read"):
            overrides = _build_memory_schema_overrides()
            actions = overrides["parameters"]["properties"]["action"]["enum"]
            assert "read" in actions, (
                "schema must advertise 'read' when the store implements it"
            )

    def test_schema_enum_narrows_without_read(self):
        """When MemoryStore.read is removed, the schema drops 'read' from the enum."""
        original = MemoryStore.read
        try:
            delattr(MemoryStore, "read")
            overrides = _build_memory_schema_overrides()
            actions = overrides["parameters"]["properties"]["action"]["enum"]
            assert "read" not in actions, (
                "schema must NOT advertise 'read' when the store lacks it (#139606)"
            )
        finally:
            MemoryStore.read = original  # restore — never mutate the class permanently

    def test_read_result_shape(self, store):
        """The read response carries the expected fields."""
        store.add("memory", "first")
        store.add("memory", "second")
        outcome, result_json = _memory_tool("read", "memory", None, None, None, None, store)
        result = json.loads(result_json)
        assert outcome == "success"
        assert result["success"] is True
        assert result["target"] == "memory"
        assert "entries" in result
        assert "usage" in result
        assert set(result["entries"]) >= {"first", "second"}
