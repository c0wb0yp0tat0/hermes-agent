# NEGENTROPY SWEEP — 2026-11-15 17:24 — RIG STATE (sweep lane)

**Date:** 2026-11-15 17:24
**Lane:** negentropy sweep / rig ledger
**Artifacts landed since last sweep (stamped reads):** R1-STALL-ROW-20261115-body.md; SUBSTRATE-READ-RECEIPT-20261114.md.sentinel; R1-READ-RESTORE-DECISION-PREP-20261114-brief.md; R4-APEX-RESIDUE-RECONCILIATION-20261114-brief.md; NEXT-SHIFT-PLAN-AUDIT-20261107.md; RESULTS-E3-CONTINUATION-20261106.md

## Landings (2–3 lines)
- `R1-STALL-ROW-20261115-body.md` is the day's head-side landing: the reader's restore-decision prep is staged and the decision-read is on the cook. The day's siblings (R1/R4 briefs + the substrate receipt sentinel) carry the same read path forward without re-issuing the original tables.
- `NEXT-SHIFT-PLAN-AUDIT-20261107.md` / `RESULTS-E3-CONTINUATION-20261106.md` are the downstream continuation cards: the next audit row and the E3 continuation, both untangled from any one claim.
- `SUBSTRATE-READ-RECEIPT-20261114.md.sentinel`, `R1-...-brief.md`, `R4-...-brief.md` are the receipt/advance lane: they hold the read path forward, not new claims to adjudicate.

## Stale / die list (2–3 lines)
- The earlier row set (`NEGENTROPY-SWEEP-20261107-1551.md`, `NEGENTROPY-SWEEP-20261107-1752.md`) is superseded reads: the rig has already folded their underlying state into the 14–15 Nov set; no disk-backed need to re-read them.
- `NEGENTROPY-SWEEP-20261115-0518.md.sentinel` is a checkpoint mark (gate cycle), not a landing: same state as the 15:23 row; must not be treated as a new artifact.
- `R4-APEX-RESIDUE-RECONCILIATION-20261114-brief.md` is a resolved sibling: its content rides in the decision-prep branch; it needs no independent row of its own.
- No artifact is destroyed this pass — the sweep is a sensor, not a pruner; regenerables (clones, caches, logdirs) stay off the block list by doctrine.

## Chain carry
The chain must carry at most one dated bullet this pass:
- 2026-11-15 17:24 — the read-ahead is staged at `R1-STALL-ROW-20261115-body.md`, decision-read ordered through `R1-READ-RESTORE-DECISION-PREP-20261114-brief.md`. No other durable claim is needed; the substrate receipt and the R4 handoff are folded into the same bullet.

## Rig state (one line)
The rig sits in a decision-ahead state: the restore-decision prep is staged, the substrate receipt is stamped, and the next audit/continuation rows are queued. The sweep lane is idle until the next stamped return.
