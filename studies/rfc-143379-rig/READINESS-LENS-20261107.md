# READINESS-LENS-20261107 — the readiness-gap sheet

**Seat:** readiness lens (fan). **Branch:** `study/rfc-143379-rig-20261105`. **Plain register.** What must close before 3oltan-seo's pilot can start.

## Gaps (each with gate + blocker)

1. **R2 — Harness write-deadline (IMP-8).** Named, unbuilt, split between thread row-id and branch-byte artifact. Gate: one settle-condition picked and receipted (thread row-id *or* branch-byte). Blocker: no PR-UPDATE ack in branch bytes since `5e0774420b`; thread UNMEASURED.
2. **R4 — unbuilt instrument.** Gate: instrument built + receipted. Blocker: draft R4 still OPEN, unnamed.
3. **R5 — W2-isolation eval.** SEPARATION-UNMEASURED; guard-preamble + empty-answer receipts banked, isolate re-run pending. Gate: verdict-line flips from SEPARATION-UNMEASURED. Blocker: eval-runtime cannot execute the isolate re-run.
4. **R6 — Fabric conclusions.** 30 `queued` + 1 `in_progress`, no conclusions column. Gate: conclusions column in FABRIC-RECEIPTS with per-fork quotes, audit-verified. Blocker: unaudited breadth claim.
5. **R7 — NOT-RUN census.** 3 of 40 markers under-specified (class-level settle-conditions). Gate: census tightened to experiment-level. Blocker: pilot register would freeze gaps as complete-as-NOT-RUN.
6. **R8 — Machinery-vs-science ratio.** Label fronts honestly (prep + machinery, not proven science). Gate: framing repair receipted. Blocker: one measured negative (K-recency FAIL) + one unmeasured separation + one self-referential loop.
7. **S1 — Settle-condition ambiguity on write-deadline.** Must be picked, not carried as "or". Blocker: same as R2.
8. **S2 — Eval's external provider-window dependency.** Schedule, not control. Blocker: no degraded-proxy run; window return not a kit instrument.
9. **S3 — Same-account-fork breadth caveat.** Hosted-window independence ≠ org independence. Blocker: eligibility threshold (quorum vs all 31) undefined.
10. **S4 — Self-audited termination proof.** Decorrelation within family, not cross-family. Blocker: audit seat is same-family-ish.
11. **S5 — One-case reservation theorem.** Hypothesis, not theorem (unbuilt retrieval check). Blocker: unbuilt experiment.
12. **S6 — Read-restore PR #116673 gate.** Open, unmerged, 11 days stale. Gate: PR passes. Blocker: pilot's start-line unread; thread surface UNMEASURED.

## R-list items' honest state
- R1 carried; R2 OPEN (non-negotiable); R3 carried; R4 OPEN; R5 OPEN (non-negotiable); R6 OPEN (dispatched, not concluded); R7 OPEN (census repair); R8 OPEN (framing repair). None closed.

## Read-restore #116673's position
- Open, unmerged, updated 2026-10-27; 11 days stale at 2026-11-07. Binding dependency; pilot wait quantified.

## W2-isolation's measure
- SEPARATION-UNMEASURED. Guard-preamble + empty-answer receipts banked; isolate re-run not executed. Lift (below-3.0 hold 5/5→1/5, median 0.67→3.00) has unseparated cause; instrument diverged +0.33.

## Harness read-budget seam
- Read-gap cost: ~64 MB compensation (12 MB spillover + 52 MB sessions), 5 drift-events (3 READ-path-mechanic), twice-read overhead EST. The harness write-deadline's read-phase budget cap is the remaining seam (enforcement exists; cap unbuilt).

## Fabric's conclusions
- Dispatched, not concluded: 30 `queued`, 1 `in_progress`, no conclusions column. 31 distinct run-ids, identical pin (universal-pin design, not a failure). Per-fork workflow presence UNMEASURED (git-only lane). 30/30 GREEN is a later wave, unaudited.

## Biggest blocker
Read-restore PR #116673 — open, unmerged, 11 days stale; pilot's start-line; thread surface UNMEASURED in the git-only lane.
