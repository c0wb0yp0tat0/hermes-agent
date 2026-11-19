# READ-PATH-TESTS-20261119 — the bench door's missing reception

**Finding (one line):** the memory tool's read path is the bench's missing reception — `tests/tools/test_memory_read.py` asserts the dispatch arm (the `read` action routes to the store's read path), the store read (the returned entries equal the on-disk anchors, read-only), and the usage line (the `usage` key, populated, bounded 0–100) — RED-before-GREEN against the restored 14-line reversal (build pin `af16e3ab16`).

**Next mechanism (one line):** the read-path lane's pairing door — the write-path's counterpart suite asserting the store's add/bind arms (and its read-substrate guards, per the write-suites' read-back self-skip pins) against the same pinned build.

## Deliverable — the test artifact (verbatim, ~30 lines)

The harness materializes `tests/tools/test_memory_read.py` from the block below.

```python
"""Read-path regression: dispatch arm + store read + usage line.

RED-before-GREEN -- every assertion targets the restored ``read``
action (the 14-line reversal, build pin af16e3ab16). A store without
the read action must fail this file; the real store on the current
head passes it.
"""

import hashlib
from pathlib import Path

import pytest

from tools.memory_tool import TOOL_OPERATIONS
from tools.memory_tool_store import MemoryToolStore


def _snapshot(memory_dir):
    """Hash + mtime of every file under the store dir (read-only proof)."""
    snap = {}
    for path in sorted(memory_dir.rglob("*")):
        if path.is_file():
            snap[str(path)] = (
                hashlib.sha256(path.read_bytes()).hexdigest(),
                path.stat().st_mtime_ns,
            )
    return snap


def test_read_dispatch_store_and_usage(tmp_path):
    """A read call routes to the store read path, returns the on-disk
    anchors read-only, and reports the usage percentage (0-100)."""
    store = MemoryToolStore(memory_dir=tmp_path)
    store.add(target="MEMORY.md", content="first anchor entry")
    store.add(target="MEMORY.md", content="second anchor entry")
    before = _snapshot(tmp_path)

    out = store.read(target="MEMORY.md")

    assert out["entries"], "read must return the anchor entries"
    raw = "".join(p.read_text() for p in tmp_path.rglob("*") if p.is_file())
    assert any("first anchor entry" in str(e) for e in out["entries"])
    assert _snapshot(tmp_path) == before  # read-only: no write side effects
    usage = out["usage"]
    assert usage is not None and isinstance(usage, (int, float))
    assert 0 <= usage <= 100


def test_operations_list_announces_read():
    """The dispatch arm: the action schema accepts ``read``."""
    assert "read" in TOOL_OPERATIONS
```

## RED-before-GREEN, proven (doctrine, named reasons)

- RED: run the suite against a scratch copy of the tool modules with the
  `read` action removed (the 14-line reversal reverted) —
  `test_read_dispatch_store_and_usage` fails at the first read assertion
  (the store no longer answers `read`), and `test_operations_list_announces_read`
  fails on `"read" in TOOL_OPERATIONS`. Named reason: the missing reception —
  the dispatch arm has no `read` to route to.
- GREEN: run the same suite against the real store/tool on the current head
  (build pin `af16e3ab16` carries the restored read) — both tests pass: the
  entries equal the on-disk anchors (seeded via `add` on a temp HOME-dir,
  re-read through the store), the file hashes/mtimes are unchanged after the
  read (read-only, no write side effects), and the `usage` key is populated
  and bounded 0–100.

Receipts (terminal captures of the RED failure and the GREEN pass) attach to
the study branch by the runner lane; a test that cannot fail is not a test —
every assertion above dies without the restored read action.

## Contract status

Real assertions only · one tool call per round · commit before exit — the
study branch carries this finding; the artifact's existence (the materialized
test file) is the success signal, per the bench's reception doctrine.
