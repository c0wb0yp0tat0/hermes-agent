# ACES-AUDIT-20261107 — the AUDIT-PASS on the IMPROVE-pass ledger (2026-11-07)

Seat: stealth/crouton-alpha. Lane: copycat leg 2, AUDIT-PASS. Branch study/rfc-143379-rig-20261105, fork-only. Method: each IMP receipt re-derived via git show <hash>:<path> from plan 3ba8998840, audit 9285c866af, AoA c54c1bc614, run-design d760fcae90, ADVANCE-D 173540a7b9, ADVANCE-B 0f0d7f1183, ADVANCE-C 7b994549d9, APEX 5fdf311069. Thread rows via gh api were not re-derivable in this lane (no gh tool); IMP-8 marked NUANCED accordingly.

## CLASS-COUNTS: 14 IMPs audited. CONFIRMED 9 (IMP-2,4,5,9,10,11,12,13,14). NUANCED 2 (IMP-3, IMP-8). REFUTED 3 (IMP-1, IMP-6, IMP-7). Seams: SEAM-2,3,5,7 stand; SEAM-1,4 fall with IMP-1/7; SEAM-6 stands bounded.

## PER-ROW LEDGER

IMP-1 REFUTED. Claim: plan section 1 carries rows 1-5; 6th arm missing. Source: git show 3ba8998840 plan section 1, re-read cold, carries SIX rows incl. | 6 | The 3-of-7 sessions messages-timestamps re-check (the PARTIAL's close) | The three durations are re-derived | The re-check's result row + the sessions-verification's PARTIAL-line closed. The 5-row premise is AoA c54c1bc614 section 2A (6 arms named in the handoff; 5 rows in the plan's), contradicted by the plan's own bytes. No restoration owed.

IMP-2 CONFIRMED. Pinned head without hex. Audit 9285c866af section 1 row 3: The gate shape is right; the seam is the pin-ambiguity. Fix: carry the exact pinned HEAD into the feed-back row. Plus row R4: The plan names "pinned head" but not the hex; the handoff's lesson 10 binds the landing-gate to the remote | GAP (the seam). Plan rows 3 and 2.1 confirm hex-absence.

IMP-3 NUANCED. Seat meituan/longcat-2.5:free vs apex-role flagship. Audit 9285c866af section 3 already resolves: PLAN-AUTHOR meituan/longcat-2.5:free = CONFIRMED, The plan's own header carries the seat. No conflict. And every apex-role carries the flagship's designation unless the brief says otherwise. Distinction exists in bytes; risk hypothetical. Downgrade to note.

IMP-4 CONFIRMED. Name which D-verdict fires the ledger. Audit section 1 row 2 verbatim: the brief says "the trigger = D's landing". The plan must pin which landed verdict fires the ledger - SEPARATION-MEASURED vs SEPARATION-REFUTED yields different rotation columns.

IMP-5 CONFIRMED. W2 confound either/or. Audit commit msg: one sharpening (W2 confound either/or); row 1: the W2-empty-answer confound is either lifted from V or named as the standing wall. Wall-id pin unmade in plan bytes.

IMP-6 REFUTED. Audit missed arm-count. Audit section 1 carries SIX rows incl. | 6 | The 3-of-7 sessions messages-timestamps re-check | "the PARTIAL's close" | CONFIRMED | No seam. And Section-2 verdict: READY-FOR-THE-NEXT with the swap-rotations trigger bound to the D-verdict-line (the seam), plus the matrix pin written to a hex. AoA section 2A claim (The audit's section 1 table also carries only five rows and does not flag the omission) is byte-contradicted. Method-fix void.

IMP-7 REFUTED. READY conditional on row-6. AoA vote READY-FOR-THE-NEXT with the seams logged, not blocking; COMPLETE-WITH-SEAMS. But IMP-1 premise refuted: row 6 exists with settle-condition and closing receipt. No unmeasurable arm; no conditional READY owed. SEAM-4 falls.

IMP-8 NUANCED. PR-UPDATE posting loop. AoA: the PR-UPDATE envelope text is delivered below for the head to post. Delivery bytes exist; ack (thread row-id) absent from branch. Thread verification briefed (gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments) but unavailable in this lane (git/read/write only). Neither confirmed nor refuted from branch bytes; keep as open receipt-gap.

IMP-9 CONFIRMED. Fire-time pin refresh. Run-design d760fcae90 section 2: Pin: head c54c1bc614f20bd5e603a4826dc5c80a670a654a (study branch study/rfc-143379-rig-20261105, ls-remote-verified at 00:15 ET). ADVANCE-D 173540a7b9 lands 01:28 ET after the pin, no refresh step. SEAM-5 stands.

IMP-10 CONFIRMED. REFUTED follow-up pre-registration. Run-design section 4: the design names the next isolation candidate: the probe-judge's empty-answer scoring path (probe answer extraction / overall aggregation) in run_eval.py, isolated next by re-running with the judge's empty-answer rule relaxed. Named in one line; no runnable spec ships.

IMP-11 CONFIRMED (bounded). Quoted diff + missing config. ADVANCE-D section 3: --config run_eval_config_no-guard.json --label "W2-NoGuard-run1"; run_eval_config_no-guard.json carries the "handoff_guard": false. Commit stat (173540a7b9) lists only SWAP-A-ADVANCE-D-20261106.md, 65 insertions - no config landed. Section 2 Exact quoted probe-loop shape is a quoted snippet (if runtime.get("api_key") and runtime.get("base_url"): system_preamble = load_handoff_preamble()), not a git diff against run_eval.py. SEAM-6 stands.

IMP-12 CONFIRMED. Tier-number reconciliation. ADVANCE-B section 3.1/3.3: high-keep tier 0.75 (verbatim phrases table), W2 tier flat 0.29 (five continuation/decision probes YES - W2), flat baseline kept-rates 0.42/0.29/0.26/0.32. Run-design W2 0.29 carried by ADVANCE-D. Numbers match across legs; no shared canonical table on branch.

IMP-13 CONFIRMED. Falsifier as priced experiment. ADVANCE-C section 1: The priority-order is descriptive (loss-geometry), not mechanistic: the k-term does NOT separate the classes - kept-rates are flat 0.26-0.42 across the four classes. Section 5: ## 5. The falsifier (stated in advance); The falsifier's settle-condition is the pair's next-action lift exceeding the decision-core-only arm's on the same fixture, and the lift surviving the W2-isolation (no-guard) variant. Falsifier exists but distributed across sections 1-5, not one priced line. SEAM-7 stands.

IMP-14 CONFIRMED. Leg-D stale pending + read-burn unpriced. APEX 5fdf311069 ground-read: SWAP-A-ADVANCE-B/C/D artifacts (advances 173540a7b9/0f0d7f1183/7b994549d9: leg B = k-term two-tier seam, leg C = MINIMUM-RESERVE rule, leg D = pending on the same rotation) - written at APEX head 01:38 ET while ADVANCE-D landed 01:28 ET. Read-burn: the read-burn is the seam the inheritance hides; Until that pass lands, the read-burn seam is logged here as the score's standing seam. Named, unsettled, unpriced.

## CORRECTIONS-LEDGER (for the review-pass)
C-1 IMP-1 REFUTED: strike IMP-1/SEAM-1 as stated; plan has 6 rows. C-2 IMP-6 REFUTED: strike; the audit receipted row 6 CONFIRMED, the AoA miscount is the error. C-3 IMP-7 REFUTED: strike; READY stands unconditioned. C-4 IMP-3 NUANCED: downgrade to note; already resolved in audit section 3. C-5 IMP-8 NUANCED: fetch thread row via gh api outside this lane or carry as explicitly open gap; do not confirm from branch bytes. IMP-2,4,5,9,10,11,12,13,14 CONFIRMED, proceed as-is. Thread-row gap: no gh tool in copycat lane; branch-receipted rows fully re-derived, thread-only receipts unverifiable here.

## OVERALL: REVISIONS-NEEDED
Three of fourteen IMP receipts fail outright (IMP-1, IMP-6, IMP-7, all resting on the one byte-error: the 5 goal rows count, contradicted by the plan's section 1 and the audit's 6-row table), two bounded (IMP-3, IMP-8). The headline seam SEAM-1 does not exist in source bytes, so the review cannot compose from this ledger unrevised. Strike C-1..C-3, downgrade C-4..C-5; the remaining 9 CONFIRMED improvements with SEAM-2,3,5,6,7 standing are ready to compose.

NEXT-LAUNCH: stealth/crouton-alpha || /root/.hermes/cache/scratch/pr1-rotation/briefs/aces-review-brief-20261107.md || /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/ACES-REVIEW-20261107.md || 40 || /root/.hermes/cache/scratch/copycat-mission/aces-review-20261107-run.log
