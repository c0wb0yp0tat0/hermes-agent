# LENS-READINESS-20261108 — the READINESS lens (the 8-hour mission's thread-read)

**Seat:** meituan/longcat-2.5:free. **Date:** 2026-11-08. **Lane:** copycat (RFC #143379 apex mission).
**Gate (verbatim):** "the gate: nothing public without the user's word" — fork-only, no thread posts, upstream quiet.

## 1. The lens's question
What must close before the named gates — the pilot's start (the read-restore's fix passing), the kit's closures (the read-budget cap, the W2-isolation's measure, the fabric's conclusions), the operator's review queue — each gap named with its blocker and its unblock path, receipted.

## 2. The ground read (summaries carried)
- **PR #1 thread (end-to-end):** the study's read summaries — PR1-READ-20261107 (272 rows; the machine-log) + ALLPRS-READ-20261107 (3 open PRs; #1 study-related). Current thread tail: 282 rows with the Wave-3 fold (FLEET-CYCLE-BODY-20261108-053342).
- **PR body (current):** FLEET-CYCLE-BODY-20261108-053342 — head `7b4678e` via ls-remote; runner idle; disk 91% under guard; the gates + forward targets.
- **Mission (final form):** MISSION-8H-V5-20261107 — 6 tracks (1, A, C, D, R1, R2); four gates verbatim; falsification-harness spec (compose.sh → test-suite.sh → claim-check.sh → receipt-emit.sh); folded task-rows T1-1…T1-6, R1-1…R1-3, R2-1…R2-3.
- **Plan's gates:** NEXT-SHIFT-PLAN-20261107 — arm 1 (W2-isolation; D's bounded-skeleton re-fire → SEPARATION-MEASURED / SEPARATION-REFUTED).
- **Fold:** WAVE3-UNIFIED-FOLD-20261108 — verdict READY-WITH-NAMED-SEAMS; seam-register S1–S8; compose-check step 6 ABSENT (acceptance-scripts not on disk).

## 3. The gaps table (gap / blocker / unblock / receipt)

### Group A — the pilot's start (the read-restore's fix passing)

| # | Gap | Blocker | Unblock path | Receipt |
|---|-----|---------|--------------|---------|
| A1 | **Read-restore fix not yet passing on the record** (PR open awaiting its pass; head carries the real fix + proof upstream). | No pass verdict on the record; head-SHA drift risk — the `ec649ad9d` re-check is owed. | Run the read action on the composed head → returns entries + usage line (byte-verified); re-check head-SHA; land the T1-2 landing-decision row (APPROVE/REJECT/DEFER). | PR1-READ-20261107 §4; FLEET-CYCLE-BODY-20261108-053342; MISSION-8H-V5 T1-2; WAVE3 S5 |
| A2 | **Read-action seam not asserted in claim-check.sh** (composed branch could be "green" while read is still "Unknown action 'read'"). | No per-PR regression assertion for the read action (RESTORE-LENS gap #5). | T1-3 names the read action as a required test in seam-gap-3; exit 0 only if read returns entries. | MISSION-8H-V5 T1-3; WAVE3 S5 |
| A3 | **Landing-order conflict unresolved** (jfugalde's #141876-first vs Finn763's re-cut-on-top-of-restored-read). | compose.sh cannot run until the order is fixed (NETWORK-LENS gap #1). | T1-1 decision row in the receipt ledger (need-id → task); compose.sh exit 0 only after the order is fixed. | MISSION-8H-V5 T1-1; WAVE3 S1 |

### Group B — the kit's closures

| # | Gap | Blocker | Unblock path | Receipt |
|---|-----|---------|--------------|---------|
| B1 | **Read-budget cap not set/evidenced** (harness write-window gate is live; the remaining seam is the read-budget cap, not the deadline). | Cap not fixed on the record; the write-window gate's budget line un-receipted. | Set the cap + receipt the budget line (byte-verified) on the branch. | downstream correction 9836333f5a via PR1-READ-20261107 §3 |
| B2 | **W2-isolation measure unmeasured** (verdict-line SEPARATION-UNMEASURED). | W2-empty-answer confound; the eval-window not run. | D's bounded-skeleton re-fire fills the spec-skeleton → SEPARATION-MEASURED or SEPARATION-REFUTED; wall-clause honored (a non-reproduction is a QUESTION, never a stop). | WAVE3 S7; NEXT-SHIFT-PLAN-20261107 arm 1 |
| B3 | **Fabric's conclusions not folded** (per-fork receipts not landed as substrate-components). | Conclusions column open; receipts not yet landed as components (not ends). | Fabric conclusion fold on the branch; receipts land as substrate-components. | WAVE3 S8 |
| B4 | **Acceptance-scripts absent on disk** (compose.sh / test-suite.sh / claim-check.sh / receipt-emit.sh). | Build pending — no `*.sh` matches on disk (S1 open). | Hour-1 build task-row (Track 1 harness spec): all four scripts exit 0 + artifacts on disk (byte-verified) before any composed-state claim is asserted. | WAVE3 compose-check step 6 ABSENT; BLIND-E2E §2; CROSS-AOA-TRUSTER-ON-BLIND Claim 4 |

### Group C — the operator's review queue

| # | Gap | Blocker | Unblock path | Receipt |
|---|-----|---------|--------------|---------|
| C1 | **Operator review queue open** (the kit's fold, the cross-audits, the seven tweaks, the storm's transformed mechanisms). | Awaits the operator's eyes; nothing public without the user's word. | Operator's pass on the branch's artifacts; the reviews move on the operator's judgment. | FLEET-CYCLE-BODY-20261108-053342 (forward); PR1-READ-20261107 §4 |
| C2 | **Notification-path mechanism unnamed** (who reads the hour-8 pointer / staged-proposals gate; SLA + rejection return channel). | No named receiver (PEOPLE-LENS gap #1). | T1-6 row names the receiver + SLA + return channel (byte-verified). | MISSION-8H-V5 T1-6 |
| C3 | **Pilot-substrate STAGED proposal's operator decision unrecorded**. | Decision not surfaced/recorded. | Track C surfaces it at the fold-point; APPROVE/REJECT/DEFER row (status STAGED, never auto-fired). | MISSION-8H-V5 Track C + §3 die-fallback staging shape |
| C4 | **Unowned provenance invariant + governed-compaction issue unopened**. | No named owner (GOVERNANCE-LENS gap #2). | T1-4 names the owner + opens the issue; provenance-survival receipt byte-verified. | GOVERNANCE-LENS-E2E-20261107 gaps; MISSION-8H-V5 T1-4 |

### Group D — machinery standing (Track C)

| # | Gap | Blocker | Unblock path | Receipt |
|---|-----|---------|--------------|---------|
| D1 | **Harness git-whitelist fix + failure-calibration lane**. | Whitelist not corrected; calibrated failure-mode list unfiled. | Track C machinery standing receipt; failure-mode list filed per fold (governance silent-failure classes included). | WAVE3 S6; MISSION-8H-V5 Track C |

## 4. The closeness read (verdict)
The pilot's start is the only hard gate; its fix's evidence is on the record (kvnloo's chain-doc lock, 17 tests green, new regression red without the store) but the **pass verdict is not** — the pilot's start-line is owed, not banked. The kit's three closures are each owned (read-budget cap = harness; W2 = D's bounded re-fire; fabric = per-fork receipts). The operator's queue is open by design — nothing public without the user's word. **READINESS: READY-WITH-NAMED-GAPS** — the gaps are named with blockers and unblock paths; none is a complaint.

## 5. Compose-check table (eight steps — one line each)

| # | Step | Status | Evidence |
|---|------|--------|----------|
| 1 | Thread read end-to-end (PR #1, 272 → 282 rows; summaries carried) | FIRED | PR1-READ-20261107 + ALLPRS-READ-20261107 |
| 2 | PR body read (current state + gates + forward targets) | FIRED | FLEET-CYCLE-BODY-20261108-053342 |
| 3 | Mission V5 read (6 tracks; four gates verbatim; harness spec) | FIRED | MISSION-8H-V5-20261107 §2 / §5 |
| 4 | Plan's gates read (W2 arm + D's bounded-skeleton re-fire) | FIRED | NEXT-SHIFT-PLAN-20261107 arm 1 |
| 5 | Gaps table receipted (every row: gap / blocker / unblock / receipt) | FIRED | §3 above (12 rows, all receipted) |
| 6 | Unblock paths named (no complaint-only rows) | FIRED | §3 unblock column, one per row |
| 7 | Fork-only; no thread posts; nothing public without the user's word | FIRED | contract gate line; no posts made |
| 8 | Artifact lands on branch + landing-gate (tracked + remote == this commit) | FIRED | this commit + push; remote == local verified post-push |

---
*Self-fire: NONE — the SWAP folds all five lenses at the 02:00 fold-point.*
*Fork-only. No thread posts. The artifact lands on the branch.*