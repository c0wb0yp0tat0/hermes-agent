@kvnloo — two commits on this head, with the receipts.

**`9ba7c030d3` — the read-back now attests disk, not the cache.** Stage 7's `verify_post_write` resolved the target's entries through the store's in-memory lists, so a write lost or reverted on disk after the store reported success would have been attested as landed. It now re-reads the target file under the store's own lock via the store's own primitives (`_path_for` / `_file_lock` / `_read_raw_checked` / `_parse_entries`), following the store's doc-awareness wherever the composition takes it.
- *Executed:* `test_write_gate.py` 51✓ / 0✗ / 10 skipped (canonical `scripts/run_tests.sh`). The new regression `test_readback_detects_lost_disk_write` (external rollback: the file reverts on disk while the cache keeps the landed write) is **RED on `5b31ccb7d5`, GREEN** with the fix.

**`7c69692640` — the doc-variant skip condition never flipped.** The skipif probed `getattr(memory_tool, "DOC_TARGET_PREFIX")` where the test file's `memory_tool` is the entry-point *function*, not the module — None on every head — so the 10 doc-chain tests had never executed. The probe now checks the module. Standalone head: the 10 still skip, now for a true reason (the doc store is absent). On a local diagnostic composition (this PR + #116673 @ `60a2e15638`): **61 passed / 0 failed / 0 skipped** — the doc arms execute green for the first time, the doc-target read-back included. The composition stays local; #116673 keeps its own home.

**In flight:** the full suite is running locally — interim 9,671✓ / 8✗, both failing files verified pre-existing on `5b31ccb7d5` (one environment-bound: container mirroring). Final tally + receipt link when it lands. Upstream CI is queued on the maintainer-approval gate.

**Not run yet, both doors open:** the full suite on the composition, and the live-model paths downstream of this PR.

<sub>Findings credit: kvnloo's downstream RFC-143379 study (source-confirmed). Co-drafted and verified with GitHub Copilot (Kimi K3), shared work with @c0wb0yp0tat0.</sub>
