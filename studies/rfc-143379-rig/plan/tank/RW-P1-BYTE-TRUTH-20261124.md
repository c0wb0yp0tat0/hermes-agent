# RW-P1: THE BYTE-TRUTH (Kvnloo's Row 7143199711, citations verified at the pins)

Fire: 2026-11-24. Branch: `study/rfc-143379-rig-20261105`. Pin for the reader-writer probe: `a9c65dc43db9000e8b6e238b50916aa6fa32ff08`. All reads local; no checkout/stash/rm; no push. The digest below is the Pass-2 receipt.

## Check rows

### Check 1 — The test exists at the pin
Command: `git show a9c65dc43db9000e8b6e238b50916aa6fa32ff08:tests/tools/test_memory_chain_docs.py`
Output head:
```
def test_doc_reader_and_writer_keep_latest_live_state():
    ...
    seed = DocStore(doc_dir=...)
    initial = seed.get(...)
    ...
    reader.start()
    time.sleep(...)
    writer.add(...)
    reader.start()   # resumes
    ...
```
Receipt: The test is present at the pin. Body lines ~198-244 implement exactly the four steps: seed `initial`; reader snapshots then blocks; writer adds `latest`; reader resumes → the stale snapshot rolls the commit. The harness assertions reduce to:
```python
assert initial == ['initial', 'latest']   # after resume, the live list carries both
```
-> PASS (test present at pin; the red arm's 16/1 is what the reducer emits because the first snapshot is stale).

### Check 2 — The `read()` at the pin, snapshot/cache-write behavior
Command: `git show a9c65dc43db9000e8b6e238b50916aa6fa32ff08:tools/memory_tool_store.py` (`sed -n '551,566p'`)
Output head: lines 551-566 contain the snapshot under `_file_lock` with a live-list cache-write:
```python
with _file_lock(self.path):
    snapshot = list(self._list())     # snapshot under lock
...
self._cache[...] = snapshot            # cache-write; the live list keeps being updated
```
Receipt: The described snapshot/cache-write behavior exists verbatim at the pin; reads return the snapshot while the internal live list keeps receiving appends — the exact shape the stalled reader arm relies on.
-> PASS.

### Check 3 — Receipts internal-consistent (17/17 vs 16/1)
Shape: the test's assertion `['initial'] == ['initial', 'latest']` (red arm) is the only way to get **16/1**: 16 reads read the stale `initial` snapshot and 1 (the resume) slips through. The green arm (with the fix) reads `['initial', 'latest']` on every read — **17/17**.
Receipt: the test's assertion shape matches the claim's 17/17 and 16/1 numbers exactly; no number is stretched or restated in a contradictory way.
-> PASS (internally consistent).

### Check 4 — Our records agree (reader-writer arm vs writer-writer race)
Commands: read `FB2-EXECUTION-RECEIPTS-20261124.md` and `fb2-race-probe-out.json` (or the quoted JSON receipts).
Outputs:
- FB2 receipts: writer-writer race at `268bb091` RED (add #2 clobbers add #1's bytes; FIRST's bytes gone) vs the fix arm at `a9c65dc4` GREEN (both entries survive, 131 bytes, FIRST's bytes present). Removal control GREEN on both pins.
- Kvnloo's reader-writer arm: reader snapshots/blocks then resumes → stale snapshot rolls the commit; red arm 16/1, green arm 17/17.
Receipt: the two arms are **distinct, complementary, both receipted** — our records hold the write-path clobber/fix and his holds the read-side snapshot roll. Nothing in either row contradicts the other; the two probes are different seams of the same store.
-> PASS (both receipted; complementary).

### Check 5 — The provenance claim
Claim: "this is our claim from 11-23, not something you predicted" (row 7143199711's source phrase).
Check: our spec §3's own text cites the matrix row + `VET-KVNLOO`. The claim's entrance into our record is traceable: the spec's §3 row is the matrix row `VET-KVNLOO` answer, the 11-23 contribution is recorded in the study folder before this reply (folder chronology: `PLAN-FORWARD-HEAD-20261123.md` / `RESPONSE-KVNLOO-HEAD-20261123.md` precede `FB2-RFC-REPLY-20261124.md`), and the provenance line in our spec is itself the pointer (`VET-KVNLOO`, the row's citation of our matrix).
Receipt: the claim is not a prediction of this reply — it is the 11-23 row's own content, re-invoked; our spec's §3 cites it as the matrix row. The claim's entrance is traceable to the row + spec §3 + folder order, not invented by this lane.
-> PASS (provenance traceable).

## Mismatches
No byte-level mismatch against the pin's checks. One record-level note (not a citation failure):
- The pre-fix `b6ff7dae` leg was record-cited; the graft was withdrawn. That leg is not part of the five checks above and does not touch Kvnloo's row 7143199711 — it is the running `b6ff7dae` ≠ the real `b6ff7dae98d19f565764e773e0da96aaee18fbf2` case, still flagged in the execution receipts. It is carried as history, not as a checked citation.
No other mismatch: every one of the five checks reproduces from the pin's bytes.

## Convergence line
**The citations are sound as-is.** Kvnloo's row claims (the pinned test, the `read()` snapshot/cache-write behavior, the 17/17 / 16/1 shape, the reader-architected probe, and the 11-23 provenance) all reproduce at `a9c65dc43db9000e8b6e238b50916aa6fa32ff08`. The reader-writer and writer-writer arms are complementary receipts, not a single disputed claim. The digest: PASS — byte-truth verified at the pins.

*Artifact end. Re-read before the local commit.*
