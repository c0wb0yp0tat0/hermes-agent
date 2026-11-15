# REF-SEVERITY — the severity's receipts (the wound's verified shape)

## The removal
The read action was removed 2026-02-19 (56ee8a5cc6 — the 14-line removal).

## The compensation (verified by execution, issuecomment-6386263138 — jfugalde's run)
- 106 commits, 6,275 lines (3,541 added, 2,734 deleted) on the memory path since the removal — the ledger EXACT, execution-verified.
- The attribution's honest split: 63 fix, 17 refactor, 8 feat, 3 ci, 3 chore, 1 test, 1 docs, 10 no-prefix — the fixes mostly belong to separate classes (drift guard, tolerant old_text, patch-vs-replace semantics, telemetry, lint sweeps).
- **The read's absence shows where code exists only to hand entries back — four sites, ~30 lines:**
  1. `_failure_with_entries` carries `current_entries` on an over-budget add (`memory_tool_store.py:322`).
  2. A zero match returns `closest_entries` (`:124`).
  3. A successful write returns the replaced-entry fields.
  4. A later fix removed `current_entries` from batch aborts because the echo made retries worse (#97316, `:331`).
- jfugalde's line: "That subset is real and it pays for the restore. Counting it, rather than the total, is the version of the argument that survives someone running the numbers."
- Also named: a 5th hand-back site, `_validate_single_op` (`memory_tool.py:157`) — the missing-parameter echo (the operator's own 6392976776).

## The gap (execution-confirmed)
- On current main: the tool answers **`Unknown action 'read'`**.
- Against the same scratch store, #141876's head returns **the entries plus the usage line, first try**.
- The same reviewer's run corrected the RFC's crash-claim: the collection error was a stale base (the `Path` NameError predating 95610a5db4), not a read bug — the record's correction stands on that honesty.

## The field
3oltan-seo's anchor-full wall: 3,844/4,000 (96%), the probe's byte-check 0 (read missing on the released build); the re-triage's relief lived entirely on the doc-chain's traversal because the read isn't there.
