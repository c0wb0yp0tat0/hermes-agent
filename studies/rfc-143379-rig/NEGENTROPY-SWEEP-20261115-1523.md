# NEGENTROPY SWEEP — 2026-11-15 15:23 — RIG STATE (sweep lane)

**Date:** 2026-11-15 15:23
**Lane:** negentropy sweep / rig ledger
**Artifacts landed since last sweep:** R1-STALL-ROW-20261115-body.md, SUBSTRATE-READ-RECEIPT-20261114.md.sentinel, R1-READ-RESTORE-DECISION-PREP-20261114-brief.md, R4-APEX-RESIDUE-RECONCILIATION-20261114-brief.md, NEXT-SHIFT-PLAN-AUDIT-20261107.md, RESULTS-E3-CONTINUATION-20261106.md

## Landings (2–3 lines)
- `R1-STALL-ROW-20261115-body.md` is the day's head-side landing: the reader's restore-decision prep is staged and the decision-read is on the cook. The rest of the day's docs are sibling briefs that extend the same read path rather than competing claims.
- `SUBSTRATE-READ-RECEIPT-20261114.md.sentinel`, `R1-READ-RESTORE-DECISION-PREP-20261114-brief.md`, and `R4-APEX-RESIDUE-RECONCILIATION-20261114-brief.md` are the receipt/advance lane: they carry the read path forward without re-issuing the original brief tables.
- `NEXT-SHIFT-PLAN-AUDIT-20261107.md` and `RESULTS-E3-CONTINUATION-20261106.md` are the downstream continuation cards: they hold the next audit rows and the E3 continuation, both untangled from any one claim.

## Stale / die list (2–3 lines)
- The old sweep rows (`NEGENTROPY-SWEEP-20261107-1551.md`, `NEGENTROPY-SWEEP-20261107-1752.md`) are superseded reads: the rig has already folded the underlying state into the 14–15 November set, and there is no disk-backed need to re-read them.
- `NEGENTROPY-SWEEP-20261115-0518.md.sentinel` is not a landing: it is a checkpoint mark left by the earlier gate cycle. It records the same state as the 15:23 row and must not be treated as a new artifact.
- `R4-APEX-RESIDUE-RECONCILIATION-20261114-brief.md` is a resolved sibling: its content is carried forward in the decision-prep branch, so it needs no independent row of its own.

## Chain carry
- The chain must carry at most one dated bullet: the read-ahead is now staged at `R1-STALL-ROW-20261115-body.md`, with the decision-read moving through `R1-READ-RESTORE-DECISION-PREP-20261114-brief.md`. No other durable claim is needed here.

## Rig state (one line)
- The rig is in a decision-ahead state: the restore decision is prepared, the substrate receipt is stamped, and the next audit/continuation rows are queued. The sweep lane is idle until the next stamped return.
