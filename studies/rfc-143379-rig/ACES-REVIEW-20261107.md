# ACES-REVIEW-20261107 — the REVIEW-PASS on the ACES loop (2026-11-07)

**Seat:** `stealth/crouton-alpha` (the alpha; the common denominator on every leg). **Lane:** copycat leg 3 — THE REVIEW-PASS, the chain's end. **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Ground (cold-read):** `ACES-IMPROVE-20261107.md` (`e640efb7a3`) + `ACES-AUDIT-20261107.md` (`9769ab931d`) + the RE-APEX floor cited in both (`5fdf311069` APEX-OF-APEXES; plan file `/root/.hermes/plans/2026-11-07_0135-reapex-shift.md` was outside this lane's read roots — its bytes are receipted here only as cited by IMPROVE/AUDIT, flagged wherever that matters). **Register:** receipts, never claims. **Round-budget:** 40.

---

## (a) CORRECTIONS-LEDGER — every correction applied, dated 2026-11-07, nothing smoothed

| # | Date | The claim (as landed) | The correction | Receipt |
|---|---|---|---|---|
| C-1 | 2026-11-07 | IMP-1 / SEAM-1: the plan's §1 carries 5 goal rows; the 6th arm (3-of-7 sessions messages-timestamps re-check, PARTIAL close) has no goal row, no settle-condition, no closing receipt — restore row 6. | **STRUCK.** The plan has 6 rows. The 5-vs-6 premise is AoA `c54c1bc614` §2A's miscount, byte-contradicted by the plan's own §1 and by the audit's six-row table (row 6: re-check, settle-condition, closing receipt all present). No restoration owed. | AUDIT §CORRECTIONS-LEDGER C-1 + per-row IMP-1: "row 6 … sessions messages-timestamps re-check (the PARTIAL's close) … The 5-row premise is AoA c54c1bc614 section 2A …, contradicted by the plan's own bytes." IMPROVE receipt for IMP-1 itself quotes only the AoA spot-check, never the plan's §1. |
| C-2 | 2026-11-07 | IMP-6: the audit missed the 6th arm (audit §1 table carries only five rows and does not flag the omission) — method-fix owed. | **STRUCK.** The audit's §1 table carries SIX rows including row 6, receipted CONFIRMED with no seam. The AoA's claim about the audit is the byte-error. Method-fix void. | AUDIT per-row IMP-6: "Audit section 1 carries SIX rows incl. \| 6 \| The 3-of-7 sessions messages-timestamps re-check \| 'the PARTIAL's close' \| CONFIRMED \| No seam." |
| C-3 | 2026-11-07 | IMP-7 / SEAM-4: the READY vote is conditional on a measurable goal for the 6th arm; no unmeasurable arm, no unconditional READY. | **STRUCK.** Row 6 exists with settle-condition and closing receipt; the READY stands unconditioned. SEAM-4 falls with IMP-1. | AUDIT per-row IMP-7: "IMP-1 premise refuted: row 6 exists with settle-condition and closing receipt. No unmeasurable arm; no conditional READY owed. SEAM-4 falls." AoA `c54c1bc614` §0: "COMPLETE-WITH-SEAMS … vote READY-FOR-THE-NEXT with the seams logged, not blocking." |
| C-4 | 2026-11-07 | IMP-3: seat `meituan/longcat-2.5:free` vs apex-role flagship `reflection/beam-1.0-501b-a23b:free` is an unresolved seat/role conflation the audit may misread. | **DOWNGRADED to a note.** Already resolved in audit `9285c866af` §3: PLAN-AUTHOR seat CONFIRMED from the plan's own header; every apex-role carries the flagship designation unless the brief says otherwise. Distinction exists in bytes; the misread risk is hypothetical. | AUDIT per-row IMP-3 + §CORRECTIONS-LEDGER C-4: "Audit 9285c866af section 3 already resolves… Distinction exists in bytes; risk hypothetical. Downgrade to note." |
| C-5 | 2026-11-07 | IMP-8: the PR-UPDATE envelope text is an unlanded potential until the head posts it (thread row-id). | **KEPT NUANCED — explicitly open, not confirmed, not refuted.** The delivery bytes exist on branch; the ack (thread row-id) is absent from branch bytes, and thread verification via `gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments` is unavailable in this lane (git/read/write only). Do not confirm from branch bytes. | AUDIT per-row IMP-8: "Neither confirmed nor refuted from branch bytes; keep as open receipt-gap." IMPROVE header concedes the same gap for the whole ledger. |
| R-1 (review's own) | 2026-11-07 | IMP-13's receipt places ADVANCE-C's falsifier "distributed across §1–§2" and the falsifier's settle-condition unspecified in the receipt. | **LOCATOR CORRECTED.** The falsifier lives at ADVANCE-C §5 ("## 5. The falsifier (stated in advance)"), with the settle-condition stated there: the pair's next-action lift exceeding the decision-core-only arm's on the same fixture, surviving the W2-isolation (no-guard) variant. The improvement (one priced line) stands; its receipt's section cite was wrong. | AUDIT per-row IMP-13: "Section 5: ## 5. The falsifier (stated in advance); The falsifier's settle-condition is the pair's next-action lift exceeding the decision-core-only arm's…" vs IMPROVE IMP-13: "not distributed across §1–§2." |
| R-2 (review's own) | 2026-11-07 | IMP-14: APEX's "leg D = pending on the same rotation" is stale at its own head. | **SHARPENED with the timing.** APEX `5fdf311069` was written at 01:38 ET; ADVANCE-D `173540a7b9` landed at 01:28 ET — the "pending" line is 10 minutes stale at APEX's own head, not merely stale in hindsight. Re-designation (D = landed-awaiting-window) owed regardless. | AUDIT per-row IMP-14: "written at APEX head 01:38 ET while ADVANCE-D landed 01:28 ET." |
| R-3 (review's own) | 2026-11-07 | IMP-5's receipt cites the audit's *commit message* ("one sharpening (W2 confound either/or)") as a byte-receipt. | **RECEIPT WEAKENED, SUBSTANCE CONFIRMED.** A commit message is not artifact bytes. The substance stands on audit `9285c866af` §1 row 1 (the W2-empty-answer confound either lifted from V or named as the standing wall; no wall-id pin in plan bytes) — the next loop must re-receipt IMP-5 to §1 row 1, not to the commit message. | AUDIT per-row IMP-5: "Audit commit msg: one sharpening (W2 confound either/or); row 1: the W2-empty-answer confound is either lifted from V or named as the standing wall." |

**Unchanged by this review:** IMP-2, IMP-4, IMP-9, IMP-10, IMP-11, IMP-12, IMP-13 (as corrected by R-1), IMP-14 (as sharpened by R-2) — CONFIRMED, proceed as-is. Nothing was smoothed: C-1–C-3 strike IMP-1, IMP-6, IMP-7 outright; C-4/C-5 downgrade, never delete.

---

## (b) THE MAP'S UPDATE — the night's state-line (re-apex floor, fresh read)

**Landings counted:** 10 on the study branch since `ebd83ba508` — the 8 IMPROVE cold-read (`3ba8998840` PLAN · `9285c866af` AUDIT · `c54c1bc614` AOA · `d760fcae90` W2-RUN-DESIGN · `173540a7b9` ADVANCE-D · `0f0d7f1183` ADVANCE-B · `7b994549d9` ADVANCE-C · `5fdf311069` APEX-OF-APEXES) + 2 ACES-loop landings (`e640efb7a3` IMPROVE · `9769ab931d` AUDIT). IMPROVE's census (8) is correct for its window; it does not count the ACES loop itself — review adds the 2, no contradiction.

**Gates' states:**
- Plan goal-gate: **READY-FOR-THE-NEXT, unconditioned** (C-3 struck the conditional). Two standing seams bind the rotation trigger (SEAM-3) and the head pin (SEAM-2), neither blocking.
- W2-isolation gate: design pinned at `c54c1bc614…` but **pin stale** (SEAM-5) — ADVANCE-D landed after the pin with no refresh step. Fire-time pin-refresh is the gate's first-commit requirement.
- Runnable-spec gate: **NOT YET MET** (SEAM-6) — ADVANCE-D's quoted probe-loop shape is presentational code (`load_handoff_preamble()`), not a `git diff` against the committed `run_eval.py`; the required `run_eval_config_no-guard.json` does not exist on branch. The re-fire must ship both bytes.
- Mechanism gate: MINIMUM-RESERVE is **descriptive-only** (SEAM-7 stands, corrected by R-1) — weight 3.00 > 2.83 > 2.33 > 2.00 rests on loss-geometry/generative-root while the k-term stays flat 0.26–0.42. The falsifier's settle-condition is now receipted (pair lift > decision-core-only, surviving W2-no-guard) but not yet run.
- Tier-numbers gate: **open** (IMP-12 CONFIRMED) — high-keep 0.75 vs W2 0.29 vs flat 0.42/0.29/0.26/0.32 match across B/C/run-design, but no canonical shared table (per-probe k_p, n, presence-bytes) exists on branch.
- Posting gate: **open** (IMP-8, C-5) — PR-UPDATE envelope delivered, thread-row ack unverifiable from this lane.

**Next-arms (as named by the seams, never invented):** D-verdict-named rotation trigger (SEAM-3) · exact HEAD hex in the feed-back row (SEAM-2) · fire-time pin-refresh (SEAM-5) · byte-verified diff + landed config (SEAM-6) · canonical tier table (IMP-12) · falsifier-as-priced-experiment (SEAM-7) · REFUTED-follow-up spec for the judge's empty-answer path (IMP-10) · leg-D re-designation + a priced read-budget per leg (IMP-14) · thread-row ack for the PR-UPDATE envelope (IMP-8, open).

**The seams — the read-burn problem, the alpha's pin:** The APEX floor names the read-burn as its standing seam ("the read-burn is the seam the inheritance hides") and IMP-14 prices the demand: a read-budget per leg, or the seam is decorative. The alpha's pin is the night's through-line and the through-line stands after audit: every surviving seam is a *pinning* failure — a trigger without a verdict-name, a head without a hex, a diff without bytes, a weight without a mechanism. The alpha (`stealth/crouton-alpha`) held as the common denominator on every leg (IMPROVE, AUDIT, REVIEW), which is precisely why the pin failures are comparable across legs: same seat, same bytes, seams visible in the same units.

---

## (c) THE LOOP'S VERDICT — the ACES loop's night-score

| Measure | Count | Receipt |
|---|---|---|
| Improvements named (IMPROVE leg) | **14** (IMP-1…IMP-14) | IMPROVE §CLASS-COUNTS: 14 named, 7 seams, 8 landings cold-read |
| Audit CONFIRMED | **9** (IMP-2, 4, 5, 9, 10, 11, 12, 13, 14) | AUDIT §CLASS-COUNTS + §OVERALL |
| Audit NUANCED | **2** (IMP-3, IMP-8) — C-4 downgrade, C-5 open gap | AUDIT §CORRECTIONS-LEDGER C-4, C-5 |
| Audit REFUTED | **3** (IMP-1, IMP-6, IMP-7) — all on one byte-error | AUDIT §OVERALL: "all resting on the one byte-error: the 5 goal rows count" |
| Overall audit verdict | **REVISIONS-NEEDED** (as landed) — discharged by this review's C-1…C-5 | AUDIT §OVERALL: "Strike C-1..C-3, downgrade C-4..C-5" — done in §(a) above |
| Review's own additions | **3** (R-1 falsifier-locator correction · R-2 APEX 10-minute staleness · R-3 IMP-5 weak-receipt flag) | §(a) rows R-1…R-3, each receipted |
| Review's own corrections applied | **5** (C-1…C-5, exactly as the audit directed) + 3 (R-1…R-3) | §(a) |

**Night-score, in one line:** 14 named → 9 confirmed + 2 nuanced + 3 refuted; the 3 refutations collapse to a single byte-error (AoA §2A's 5-row miscount, uncorrected into IMP-1/6/7), and the loop's prose outran its receipts at exactly the joints the audit pinned. The improvements that survived are the ones that named a pin; the ones that fell are the ones that named a count. The loop improved the night by making that distinction auditable — its net product is 9 confirmed improvements, 5 standing seams, and 1 open receipt-gap (IMP-8), all receipted.

---

## (d) THE NEXT-LOOP'S SEED — the seams ARE the seed (never invented)

The next loop's arms are the standing seams and the open gates, named in fire-order:

1. **SEAM-2 arm (IMP-2):** pin the exact HEAD hex in the feed-back row — settle-condition: the hex written to the row; liveness edge (local ≠ remote) classed as lesson-10. Seat: alpha.
2. **SEAM-3 arm (IMP-4):** name which D-verdict (SEPARATION-MEASURED vs SEPARATION-REFUTED) fires the rotation ledger — settle-condition: the verdict-name bound to the trigger in the plan's sequencing row.
3. **SEAM-5 arm (IMP-9):** fire-time pin-refresh as the re-fire's first commit (head-hex re-verified at fire-time, not design-time). This arm opens the window; arms 4–5 are blocked on it.
4. **SEAM-6 arm (IMP-11):** byte-verify the quoted probe-loop shape against the committed `run_eval.py` (land a real `git diff`) and land `run_eval_config_no-guard.json` — settle-condition: both bytes on branch before the 3-run re-fire improvises them.
5. **IMP-12 arm:** one canonical tier table (per-probe k_p, n, presence-bytes) shared by B, C, and the run-design — settle-condition: the ITERATE arm and the MECHANISM arm read identical rows.
6. **SEAM-7 arm (IMP-13, R-1):** run the falsifier as a priced experiment — pair next-action lift vs decision-core-only, surviving the W2-no-guard variant — with the §5 settle-condition (now receipted) as the verdict line. Seat: alpha.
7. **IMP-10 arm:** pre-register the REFUTED follow-up (the probe-judge's empty-answer rule relaxed) as its own runnable spec, so a REFUTED verdict strands nothing.
8. **IMP-14 arm:** re-designate leg D as landed-awaiting-window (R-2: 10 minutes stale at APEX's head) and price the read-burn seam — a read-budget per leg, or the seam stays decorative.
9. **IMP-5 arm (R-3):** re-receipt the W2-confound improvement to audit `9285c866af` §1 row 1 (bytes), not to the audit commit message; wall-id pin or lift-from-V, stated either/or.
10. **IMP-8 arm (C-5, open):** close the posting loop from a lane with thread access — the head posts the PR-UPDATE envelope and the thread row-id is receipted; until then the gap stays explicitly open. Seat authority outside this lane.

Every arm above is a standing seam, a confirmed improvement, or the audit's own named corrections — no arm invented. The chain's end folds the landing and rows it (no NEXT-LAUNCH block, per brief).
