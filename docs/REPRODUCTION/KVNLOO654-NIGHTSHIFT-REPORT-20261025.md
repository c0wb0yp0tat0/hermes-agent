# KVNLOO654 NIGHT-SHIFT REPORT — the exact-head reproduction on our idealized substrate (2026-10-25)

**Window:** ~02:15 → ~03:00. **Board:** the full ACES rotation ran end-to-end, self-perpetuating: producer → develop → audit → AoA (t_9cab8dad → t_7bf04175 → t_a637173a → t_3d62ab5b), all done. **Anchor:** diff-check UNCHANGED.

## The headline

The homework fork's exact-head reproduction ran on our idealized substrate (the read-restore live at `af16e3ab16`) — Kevin's tests as written, the stress-test round — and produced gold: the read restores and passes dispatch, but the **stale-cache read-back rollback reproduces live**, and the **consent no-save gate is unmet on every gate tested** (12/12 violations). The findings are corrected, AoA-verified, and postable to the user's review.

## What landed (all evidence-attached)

1. **The reproduction chain completed end-to-end** — the producer's receipts, the develop's findings, the audit's CONFIRMED-WITH-NOTES, the AoA's all-clear with six corrections, all folded to the chain (009-wins, served).
2. **The isolated suites pass by design** — the memory lab 17/17, the consent lab 116/116, the checkout suite 153/153 (per-file counts corrected: 6+19+64+64), the coverage benchmark byte-identical to Kevin's committed artifacts (SHA256 `4f6d26ff…51fe05a8` — the develop's published hash was a 38-char fabrication, corrected).
3. **The exact-head gold:**
   - **The stale-cache read-back rollback REPRODUCES LIVE** — `store.read()` captures an old disk snapshot and overwrites in-memory entries after a concurrent add (the cache holds `['original']` while disk holds `original + newer`). Kevin's question #2 — should read mutate the shared cache? — is the live defect.
   - **#116673** reproduces all three surface findings (read rollback, anchor TOCTOU, 131 KiB uncapped doc response).
   - **#139606** lacks a read action entirely; the read-mismatch DISSOLVES on our substrate (the read is live, the dispatch contract passes).
   - **The write-gate is present as a file but non-functional on `af16e3ab`** — `acceptance_pipeline` crashes on the missing `_doc` primitive (our runtime lacks the chain-doc primitives #116673 would provide), and it's not wired in (zero imports from `memory_tool.py`). Kevin's question #7, answered by execution.
   - **The consent no-save gate is unmet on every variant** — 12/12 applied on our substrate, 0 staged; the #116834 and #116846 gates stage 6/12 and 4/12 but never refuse; our write-gate (Stage 2.c) does NOT shift the picture (it refuses imperative non-user writes, consent content is declarative). The consent retention needs a different layer — a source-level deny on `SYNTHETIC-CONSENT-CODE-*` — Kevin's open question §6.
   - **The dream-cycle (#140008) passes 9/9.**
4. **The six AoA corrections applied and verified** — the SHA256, the test counts, the union row (4 applied / 8 staged — un-swapped), the `_scan_memory_content` file (`memory_tool_store.py` line 28, not `threat_patterns.py`), the write_gate size (25,133 bytes), the audit's fabricated line citations (develop.md has 307 lines, not 388+).

## The doors' state

- **The heads-up to Kevin is LIVE** (kvnloo#654, comment 6394373162, edited to include the idealized-substrate call-out, verified byte-identical) — he knows the follow-up is coming.
- **The full follow-up with Kevin** — the source-backed evidence, the findings — **waits on the user's word** (the only gate).
- **The RFC thread stays clean** — nothing posted there tonight.

## The next moves (the morning's pickups)

1. The user's review of the findings package (`/tmp/kvnloo654-reproduction/` — producer.md, develop.md (corrected), audit.md (corrected), aoa.md).
2. On the user's word: the follow-up comment on kvnloo#654 with the source-backed evidence.
3. The banked findings re-enter the RFC conversation on the user's word — the cache-coherence contract (Kevin's Q2), the consent deny-before-write (Kevin's Q6), the write-gate's non-functional state on our substrate (Kevin's Q7).

## The honest ledger

- The workspace defect (the dispatch's worktree path) — found, patched at the mechanism level (`aces-dispatch.sh` pins the pilot worktree), the chain re-dispatched clean.
- The develop's SHA256 fabrication was the audit→AoA layer's catch — the layers worked as designed.
- The fold's duplicate bullet — my error, removed mechanically, the served count verified.

*One file. The chain ran, the gold is banked, the doors are gated on the user's word.*