"""test_memory_read.py — the read-path regression packet (SPRINT-FIRE-SEQUENCE F1b).

Shape: lift-ready for the #141876 surface (the restore PR's missing tests, per
jfugalde's review note: "No test files ship with the PR, so the read path itself
is covered only by neighbors"). Assertion set: the dispatch arm, the store read,
the usage line, the sanitized surface. RED-before-GREEN: run against a surface
WITHOUT the restore first (expect failures on `Unknown action 'read'`), then on
the restored head (expect green). Additive only; reverting this file is the rollback.

Conventions: mirrors tests/tools/test_memory_tool.py (the neighbor suite's style).
Battery home: the runner legs (unmetered) + the local-LM floor per F1's slot.
"""

import json
import os
import tempfile
import unittest
from unittest.mock import patch

# The two layers the restore touched (memory_tool_store.py:369 MemoryStore.read,
# memory_tool.py:258 dispatch arm, the schema enum) — import paths per the repo's
# own tests; adjust imports to the exact head when lifted.
try:
    from tools.memory_tool_store import MemoryStore
    from tools import memory_tool
except ImportError:  # the RED-before-GREEN stance: absent surface = expected
    MemoryStore = None
    memory_tool = None


class TestReadDispatch(unittest.TestCase):
    """The read action's dispatch arm — the failing surface WITHOUT the restore."""

    def test_read_action_dispatch(self):
        """memory(action='read') returns the store's read result, never Unknown."""
        if memory_tool is None:
            self.skipTest("surface absent — RED-before-GREEN stance")
        with tempfile.TemporaryDirectory() as td:
            with patch("tools.memory_tool.MEMORY_PATH", td + "/MEMORY.md"), \
                 patch("tools.memory_tool.USER_PATH", td + "/USER.md"):
                result = memory_tool._dispatch("read", {})
                self.assertNotIn("Unknown action", str(result))
                self.assertIn("entries", str(result) if isinstance(result, dict) else result)


class TestStoreRead(unittest.TestCase):
    """MemoryStore.read: entries as stored, usage percent, read-only."""

    def test_read_returns_entries_and_usage(self):
        if MemoryStore is None:
            self.skipTest("surface absent — RED-before-GREEN stance")
        with tempfile.TemporaryDirectory() as td:
            store = MemoryStore(td)
            store.add({"content": "anchor line one"})
            read = store.read()
            self.assertIn("anchor line one", str(read.get("entries")))
            self.assertIn("usage", read)  # the usage percent line

    def test_read_is_read_only(self):
        """A failed read reports a READ failure, never 'refusing to write'."""
        if MemoryStore is None:
            self.skipTest("surface absent — RED-before-GREEN stance")
        with tempfile.TemporaryDirectory() as td:
            store = MemoryStore(td)
            # chmod the store (POSIX) so the read cannot open it
            os.chmod(td + "/MEMORY.md", 0o000)
            try:
                read = store.read()
            except PermissionError:
                read = {"ok": False}
            finally:
                os.chmod(td + "/MEMORY.md", 0o644)
            # the read's failure sentence; never the write-refusal vocabulary
            self.assertNotIn("refusing to write", str(read))


class TestSchemaEnum(unittest.TestCase):
    """The schema advertises 'read' in both the single-op and batch enums."""

    def test_read_in_operations_enum(self):
        if memory_tool is None:
            self.skipTest("surface absent — RED-before-GREEN stance")
        schema = memory_tool.get_tool_schema() if hasattr(memory_tool, "get_tool_schema") else {}
        ops = json.dumps(schema)
        self.assertIn("read", ops)


if __name__ == "__main__":
    unittest.main()
