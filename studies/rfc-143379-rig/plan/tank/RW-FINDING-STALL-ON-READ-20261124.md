# RW FINDING — the read-straddles-write arm reproduced under our own execution (2026-11-24)

## The finding, one line

**kvnloo's 11-23 receipts are reproduced byte-faithfully under our own execution: the rollback (RED) exists ONLY when both the lock and the no-cache-write are removed — the read's stale snapshot loads back into the live list, rolling the writer's commit.** The other three variants stay green because either arm alone prevents the rollback (the lock serializes reader-writer; the no-cache-write keeps the stale snapshot out of the live list).

## The executed receipts (probe: rw-stall-probe-20261124.py, at a9c65dc4, verbatim store)

| variant | rollback_observed | live list after |
|---|---|---|
| as-at-pin | False | ['initial', 'latest'] |
| lock-removed | False | ['initial', 'latest'] |
| cache-write-restored | False | ['initial', 'latest'] |
| both-removed | **True** | **['initial']** |

This is the LOAD-BEARING finding: it confirms the arm's mechanism AND the exact variant that makes it red — the pre-registration's predicted signatures (green, green, green, red) stand on executed bytes, not on kvnloo's table alone.

## The mechanism, from the pin's own bytes

- The FIXED `read()` at `a9c65dc4` (`tools/memory_tool_store.py:551-567`): reads the chain-doc under `_file_lock`, parses entries, returns the sanitized view — and NEVER mutates the live store (`memory_entries`/`_doc_entries` untouched). No cache write, no stale load.
- The ORIGINAL #116673 reader: after taking its disk snapshot, its read() loads that snapshot *back into the live cache* via the cache write. Under the lock, a concurrent writer must wait (serialized) — the writer's commit lands after the read, so the cache write never goes stale. Remove the lock and the writer commits mid-read; the resumed read's snapshot is now stale; the cache write rolls the live list back (drops the writer's entry). The disk file keeps both entries — the LIVE list is the rollback surface, which is why a sequential two-add probe stays green while the concurrent reader-writer arm goes red.

## What the reply's pre-registration should carry

- The arm is separate from FB-2 and complementary: FB-2 is the writer-writer race (the lock's role there); this arm is the reader-writer race (the lock's role here). Together they cover both.
- Pre-registered predicted signatures at the pins: as-at-pin GREEN · lock-removed GREEN · cache-write-restored GREEN · both-removed RED.
- The four-step stall test (seed initial; reader snapshots then stalls; writer commits; reader resumes — assert the live list holds the writer's commit, and the tool-level read returns both entries), adapted to the pre-registration's cold-runnable form.
- kvnloo's own test (`test_doc_reader_and_writer_keep_latest_live_state`, `tests/tools/test_memory_chain_docs.py:198-244` at a9c65dc4) is the named reference — our probe reproduces its prediction, and the reply should carry that lineage honestly.

## The honed honesty surfaces (for the compose)

- The claim's provenance: "removing both turns red" originated in kvnloo's own 11-23 matrix (row 7087999804), entered our spec §3 with that citation, and he has now traced it back himself and corrected it to the reader-writer arm — both sides of the trail get credited.
- Our probe run is the independent confirmation; his test is the named reference; the divergence data (byte count, control refusal) has already been logged in the confirm-run reply.
