# READ-PATH-TESTS-20261119-brief.md — the bench door's missing reception: the read-path regression tests (lane)

*You are the lane executing the plan's smallest fireable two-way door — the reception packet the bench-read cut: `tests/tools/test_memory_read.py` asserting the dispatch arm + store read + usage line, RED-before-GREEN. The gate: "the gate: nothing public without the user's word." RFC QUIET. Terminal is git-only for YOU (except the git verbs); the tool code is readable. Commit before exit.*

write-window: 12

## THE GROUND (read first, once)
- `tools/memory_tool_store.py` — the store's implementation (the `read` action: the installed build carries the 14-line reversal, commit `af16e3ab16`; `memory(action="read", target=...)` returns the anchor entries read-only WITH the usage percentage — the dispatch arm + store read + usage line the test asserts).
- `tools/memory_tool.py` — the tool's action schema (the operations list).
- An existing `tests/tools/*.py` test (e.g., `test_accretion_caps.py`) — the suite's conventions.

## YOUR DELIVERABLE
`tests/tools/test_memory_read.py` (~30 lines, the suite's conventions):
1. **The dispatch arm** — a read call routes to the store's read path and returns the entries (assert against a REAL store instance on a temp HOME — follow the suite's fixture conventions).
2. **The store read** — the returned entries equal the on-disk anchors; read-only (no write side effects: assert the files' mtimes/hashes are unchanged after the read).
3. **The usage line** — the read returns the usage percentage (the `usage` key, populated, bounded 0–100).
4. **RED-before-GREEN, proven:** the test must FAIL on a store WITHOUT the read action — demonstrate the RED by (a) running the suite's read-test against a mutated store (the read action removed — a temporary patch in a scratch copy, NOT a commit) and showing the test fails, then (b) GREEN against the real store on the current head. Receipt the RED's output and the GREEN's pass — the doctrine: RED-before, GREEN-after, named reasons.

## THE CONTRACT
One tool call per round · real assertions only (no placeholder tests — a test that cannot fail is not a test) · ≤6,000 chars per write · commit before exit (add → commit → push; pull --rebase on rejection; do not exit until the commit succeeded).
