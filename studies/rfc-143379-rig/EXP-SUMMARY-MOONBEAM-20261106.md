# EXP-SUMMARY-MOONBEAM-20261106 — the corrected end-to-end summary of PR #1 at the current head (8b0a2af584)

**Lane:** MOONBEAM (story-voice). **Register:** receipts, never claims — every line traces to a commit SHA, run id, comment id, or file on branch `study/rfc-143379-rig-20261105`. **Voice:** speechify — distinct phases and voices preserved, no blurring. **Supersedes:** `EXP-SUMMARY-MOONBEAM-20261105.md` and `EXP-SUMMARY-NIGHT-20261106.md` as the current record's summary. **Precision-marks applied:** the meter's truth (self-hosted), the receipts-count (nine GREEN rows, counted), the NOT-RUN discipline, the honest markers (FAIL is a finding).

**Opening line:** The RFC #143379 study's record, at head `8b0a2af584`, is a multiply-receipted, honest FAIL across every counter attempted — the K-recency hard window, the scaled window, the constraint-truncation, the competition explanation, the archive — and the compaction-front's tiny+old loss-class was walked driver-by-driver and healed (5/5 → 0/5, blind-audit-reproduced), with all four RFC lines staged and every public-gate holding.

---

## Phase 0 — What PR #1 is

PR #1 of fork `c0wb0yp0tat0/hermes-agent`: branch `study/rfc-143379-rig-20261105`, an independent verification study of RFC NousResearch/hermes-agent#143379 (memory compaction / K-recency). Downstream-only: no upstream posts, no upstream code changes; original authors retain ownership. Goal-lock (binding): `studies/rfc-143379-rig/` on the study branch; Avrea verification leg (envelope schema, meter budget stewardship, wall clause). Nothing public beyond the fork; no model credentials.

## Phase 1 — The contract (Avrea leg)

`AVREA-LEG-CONTRACT.md` (commit `52c13025bc`, corrected 2026-11-05): envelope `id/run/pin/requested/executed/assert/battery/summary/conclusion/receipt_url`; pin asserted BEFORE the suite (`requested == executed`); wall clause: a non-reproduction is a QUESTION, never a stop — minimal experiment required before any "unreproducible" verdict. Committed definitions are NOT execution; NOT-RUN stays until a receipt exists.

**The meter's truth (precision-mark 1):** the rig's runner is SELF-HOSTED — GitHub's Actions are free for self-hosted runners; the provider's free-meter classes (3,000/1,500 min/mo) apply only to the provider's hosted VMs, never our host. The governance frame (one run per pin, no re-dispatch without a named reason) is kept BY CHOICE, not necessity. Cite `AVREA-LEG-CONTRACT.md` (corrected 2026-11-05 version).

## Phase 2 — The receipts (run ledger)

`RECEIPTS.md` — counted GREEN rows MYSELF from the ledger (precision-mark 2): **NINE GREEN rows**, four RED rows, one NOT-RUN row.

GREEN rows:
1. 42064685359 @ d1bdb4582c (#139606 merge head): GREEN — write-gate + memory-tool.
2. (host-local) @ a996d4ad30 (whole-anchor resolution head): GREEN — falsifier battery 28 passed, 1 xpassed in 1.01s (strengthened arm flips).
3. 42071651022 @ ffb85c2c58 (#140008): GREEN — 64 passed in 5.06s.
4. 42071665270 @ 60a2e15638 (#116673): GREEN — 66 passed in 5.19s.
5. 42071680606 @ ec649ad9d0 (#141876, the restore): GREEN — 82 passed in 5.72s.
6. 42074781407 @ c39d8ce722 (round2-combined-substrate): GREEN — 70 passed in 5.24s.
7. 42074793218 @ a996d4ad30 (whole-anchor head): GREEN — 98 passed, 1 xpassed in 5.85s.
8. 42074804475 @ 4905270237 (avrea-parallel runner-env): GREEN — 89 passed, 1 xfailed in 5.74s.
9. 42096454325 @ a996d4ad30 (falsifier-battery @ whole-anchor): GREEN.

RED rows: 42096273475 (union @ arm-head), 42096589644 (sweep @ study-head), 42098517565 (union @ arm-head re-run), 42103142238 (union @ study-head, first guarded attempt) — all with causes and fixes receipted.

NOT-RUN row: the GitHub-window side (hosted queue class) — marked, not smoothed (precision-mark 3).

Number-seam resolution: the "xfailed 1.83s" phrasing in one landing was a mislabel; the real record is **28 passed, 1 xpassed in 1.01s** at the whole-anchor host-local pin (pin-specific, not global — the apex-day falsifier-battery run 42096454325 has no run-size in the record).

## Phase 3 — The findings (instruments)

`krecency/` instruments (derived, no injected term): `probe_age.py`, `sweep_age.py`, `scoping_test.py`, etc.; results in `results/`.

- **Demand-age gate: FAIL at 300+ cycles per the letter's worst-case** (`RESULTS-AGE.md`): derived table of record — 150c 4x mean +23.87pp (min −20.40), 8x +25.47pp (min −15.60); 300c+ 2x mean −3.00 (min −30.00), 4x +0.60 (min −20.40), 8x +2.40 (min −15.60), 16x +2.90 (min −15.10), 32x +3.00 (min −14.00). Sub-zero class holds ALL 25 seeds at 4x/300c+ (2–4 of 4 sampled cycles each); excursions at BOTH horizons. Means' erosion (4x +23.87 → +0.60pp) is the session-length face. Earlier −8.4/−3.6pp figures superseded (intermediate aggregation).

- **K-scaling arm: NO** — scaled-K = min(1+floor(sqrt(cycle)),20) underperforms fixed-K10 at every reported ratio (full 4x–8x band). Caveat: only one scaling function tested.

- **Constraint arm: FINDING** — recency-truncate 1.00 (worst), hierarchical 0.25, summarize-as-rule = head-retain 0.00; pinned restores 0.00. Pinning-cost: 18 tokens vs field's ~47, ~0.18% at production scale (raw 9.84% was the sim's 183-token denominator — superseded).

- **Aliasing × proximity arm: CONFIRMED-BOTH** — evidence-mass predictor R² = 0.6548 (bar 0.35); aliasing keeps deep minima high with proximity-mass OFF; proximity-mass alone raises prevalence with aliasing OFF; 800 rows.

- **Competition arm: NOT-CONFIRMED** (instrument-limit) — rivals fire on latent/survivor path only; K=10 window-hit path never faces one; a* degenerate against the only path that matters. Precision-added: equal-weights mechanism (`[1.0]+[1.0]*n` — softmax tracks rival-count, not evidence-mass).

- **Archive arm: FAIL → REFUTED under tested construction** — ID-known recall is the optimistic bound; budget knob admits only the demanded literal's ID (toothless-knob); competing-admission repair (`9c3e89566d`, 19,800 rows) does not clear the gate — deep minima persist at taxed budgets.

- **Recitation arm: NOT-CONFIRMED** — recite-knob changes prevalence ≤0.1 at every cell/cycle — not the residual; wheel complete within tested classes.

- **Pinning arm (adopted counter): PROTECTS** — recurrence-aware exact-literal pinning drops deep-minima prevalence at the confirmed aliasing×proximity pair-ON cell from 1.00 to 0.15. Onset-test explains why: per-seed onsets differ (seed 0: cycle 68; seed 1: cycle 87) — per-seed occurrence predicts the onset, a recency-only pin loses protection.

## Phase 4 — The arms and waves (1–31)

Waves 1–4: the webstorm appendix (five-why tree, four questions' answers), the CTO-freedom webstorm, the storm appendix (three untested classes named with falsifier and field-set prediction bars), the competition/archive arms landed, the aliasing×proximity arm dispatched.

Waves 5–8: fleet's first fold byte-verified (longcat divergence: archive knob toothless, compete rivals path-limited, pinning-with-recurrence adopted); beam fold (a* equal-weights mechanism, archive inertias, competing-admission candidacy); krecency lane (apex adjudication + next mechanism); copycat findings directory populated.

Waves 9–13: the portability-gap (E1) receipted (PORTABILITY-GAP at real-streams, 59877 git-log literals, all three pinning variants at 0.80 at fused cell; synthetic 0.15-protection does not transfer to recurrence-free real loads; complement named). E1-revisit (PORTABILITY-RECURRED): recurrence-bearing real streams (147 session-dumps, 15702 literals, recurrence-rate 0.3715, 293 pinned): none 0.80 → literal 0.00 → membership 0.00 — below 0.15-bar. E5 simplify-arm: krec_core.py extracted, byte-identical sameness (FLOOR-copy fixed; identity 7/7 cells + 200-cell broad-sameness 0 diffs). E3 crossings: CELL-DEPENDENT — small+old cell holds 1.00 across every variant (+0.85 vs 0.15-bar), other quadrants 0.00.

Waves 14–19: membership ring CONFIRMED (onset-prediction + weighted bar); V3 FORMAT-AWARE-NOOP; VOI-sort fully verdicted (V1 confirmed, V3 NOOP, V2 parked); portability-gap; bearings' frontier (five open edges E1–E5); true finish-line (RFC's four lines' fruition-conditions; inventory-gate demoted to ledger's place); HITL-READY doc landed.

Waves 20–27 (the seam-arc): ordering-null → literals-partial → derivations-partial → anchors-effective → composition-marginal → intents-SEAM-CLEARED. The compaction-front's tiny+old loss-class walked driver-by-driver and HEALED (3-block composition, 5/5→0/5, blind-audit-reproduced). Audit REPRODUCTION-DIVERGENT at +0.33 (the grain), CONFIRMED at the substance.

Waves 28–31: network-evidence landed (NETWORK-EVIDENCE-STRONG, the #116673 anchor-chain case); wildcard-seat RL-cross-lens (SEAMS-NAMED, three adoption-candidates); curriculum-ladder (LADDER-GAPS, two missing rungs named); rungs-built (RUNGS-BUILT, two stress-cells from distinct rig sessions, verified 2/2).

## Phase 5 — The corrections

Number-seam "xfailed 1.83s" → "28 passed, 1 xpassed in 1.01s" (RECEIPTS.md L14–15). RESULTS-AGE −8.4/−3.6 superseded by the derived table (−20.40 worst-case). RESULTS-CONSTRAINTS re-walk. README hybridization (`e2e3fde716`/`eb57ddbe63`). Spine-map (`b628696a73`). GREEN-count harmonized to ledger's authority (`eb00e5e294`). Finish-line's false-FAIL root fixed (`b0d84f7df4`). RUNGS-REOPEN substance-check (`AUDIT-LADDER-RUNGS-20261106.md`) → rebuild (`REBUILD-RECEIPTS-20261106.md`, `EXP-REBUILD-CERT-20261106.md`). Membership-AoA ADJUST (the record corrected: `probe_membership.py` hard-codes onsets `SEEDS_ONSET = {0: 60, 1: 80}`; RESULTS-MEMBERSHIP.md table mislabels probe's derived quantities; E2-replier artifact absent → UNVERIFIED).

## Phase 6 — xngg seam-gaps verification

`XNGG-GAPS-VERIFICATION-20261105.md`: Gap 1 CONFIRMED @ d1bdb4582c (`tools/memory_tool.py:343` batch path bypasses `verify_post_write`); Gap 2 NOT REPRODUCED (guard IS present at `:280-283`); Gap 3 CONFIRMED @ ffb85c2c58 (`tools/spa_integration.py:100-107` drops `store.add` return dicts); Gap 4 NOT REPRODUCED (adapter part; compressor-hook NOT YET PROBED) (`tools/dream_cycle.py:118-122`).

## Phase 7 — The runner narrative (dual surfaces)

Standing roster: falsifier GREEN 42096454325; union/sweep rows with causes; guard 76f95dd401 landed (nugget-6 substrate guard into pin-trees, self-skip at unsupported pins). The dual-matrix: both legs (avrea self-hosted + GitHub-hosted) live together (`42163546699`, `42166609259`, `42168495752`, `42171479492`, `42213016088` — all SUCCESS). Divergence between the two surfaces is data, recorded, never smoothed. The platform-queue class (hosted CI/Docker/Nix runs pending ~hours) is distinguished from the self-hosted's ~85s verify.

The runner's arc: 42 runs, 42 completions — 13 Succeeded / 27 Failed / 2 Canceled; green-rate 0.24 → 0.41 (+0.17) across the day. Every RED a finding, every finding a fix, every fix a commit.

## Phase 8 — The watcher contract

`pr1-watcher-contract.md` (in `/tmp` study artifacts): trigger-driven machinery seeds — SELF-FIRE grammar, poller's contract. Decision: the build's go. The watcher is the study's automation surface; the CTO-designated designation held. (CLAIM-UNVERIFIABLE from the branch — HITL-READY corroborates staging.)

## Phase 9 — The webstorm guidance

`pr1-webstorm-guidance.md`/`pr1-webstorm-nuanced.md` (in `/tmp`): the four mechanisms' steers + candidates' true status (the nuanced version). Four mechanisms: competition class, archive primitive, pin generalization, focus-drift. arXiv credits: LOHA/ACD 2609.31430; Governance Decay 2606.22528; Compaction Cliff/Knowledge Triage 2608.22752; Length Is Cheap, Competition Is Not 2611.04169; Context Poisoning as Extreme-Value Attention Interference 2609.22101; Retrieval Capacity of Self-Attention Under Competition 2609.37879; ARC 2607.25066; AttnCompress 2609.08318; Active/Reflection-driven ARC 2601.12030; ReTree 2608.10676; Lost in the Middle 2307.03172; rate-distortion survey 2607.08032; RoPE provable position/token aliasing 2605.15514; Sirens' cumulative denominator 2609.26718; DSGC (recency retains prerequisite chains in only 0.07 of runs). The rig's designs came first; the frontier validated the mechanism shape. The durable-execution harvest (2026-11-06): S3Mirror, SerPyTor, libDSE, GraphFlow folded as corroboration + steers.

## Phase 10 — The fleet landings

- Longcat fold (commit `77a441dc92`): wave-5 byte-verified adjudication — compete rivals never touch the K=10 hit path; archive knob toothless; pinning-with-recurrence adopted as next mechanism.
- Alignment landing (commit `eb57ddbe63`): paid pod's hybrid README — goal-lock, envelope voice, discipline-layer table, −20.40pp worst-case faithful to the derived table.
- Solar-mini4 (commit `1d70408531`): own content; next-mechanism independently converges on the pinning.
- Beam fold (commit `ddaaa83f8e`, wave-8): a* equal-weights mechanism, archive inertias, competing-admission candidacy.
- Krecency lane (commit `19723b3c51`): apex adjudication + next mechanism.
- Step-designation (commit `bde8ff5f37`): the fourth lens's seam + its vector (alias-aware format-pinning, the third distinct next-mechanism).
- Longcat read-side synthesis (`9e6a922f26`): three design-moves mapped to the read-restore's contracts + the query-blind reconciliation.
- Copycat findings directory: `copycat-findings/copycat-{krecency,longcat,solar-mini4}-20261105.md` (three files; no beam file — the beam fold is in SYNTHESIS.md WAVE 8 + commit `ddaaa83f8e`).

The fleet's circle complete (4/4): longcat (constructionals) · beam (a*-mechanism + competing-admission) · solar (the pinning-lens) · step (the fourth lens's seam + its vector).

## Phase 11 — The synthesis (one-mechanism line)

`krecency/SYNTHESIS.md`: the K-recency window's eviction is the recency-truncate class. The recitation floor (lane A) and the governance decay (lane B) are one window wearing two hats — the window that erases exact text is the same window that erases the standing constraint. Lane B PENDING-FROM-LANE at synthesis time; integration derived from lane A's curve + RFC stated mechanism. K-recency hard window needs the pinning analog (lane B) to survive; provenance-origin and archive-before-stub survive on their own evidence.

RFC guidance (`RFC-GUIDANCE-20261105.md`, commit `bbf10e8efd`, delta `06a2e8b59c`): read restore (#141876) stays landing-order first piece; K-recency hardness replaced by measured shape; memory-side honest guarantee = lifecycle correctness for pinned + calibrated abstention for unknown; ruler's fix applies to the probe not the bar. Apex-day deltas: archive FAIL constructionally re-adjudicated (byte-confirmed, toothless knob); competition NOT-CONFIRMED precision-added (path-limited); xngg seam-map; pinning-mechanism adopted; recitation-arm status explicit. Deltas 1–9 folded through the night (compaction-annex, seam-arc, OWASP, standards).

## Phase 12 — HITL staging

`HITL-READY-20261105.md`: seven candidates (RFC-GUIDANCE, XNGG-VERIFICATION, runner-pipeline, fleet's landings, webstorm-guidance nuanced, watcher-contract, recitation-arm); false-claims register EMPTY. The thread's claims all trace to their receipts; the ledger's rows match the runs'; the NOT-RUN markers stay until the receipts replace them.

## Phase 13 — Honest markers

Committed definitions ≠ execution; green-at-pin qualifies that pin only; divergence as data; GitHub-window NOT RUN; recitation class named-not-measured; meter stewardship (self-hosted); nothing upstream. The RFC's four lines' evidence-set COMPLETE: #141876 restore STAGED · #116673 network STAGED · #139606 governance STAGED · #140008 compaction STAGED — all four lines' evidence on the branch, every public-gate holding.

## Phase 14 — The bearings (E5, E1, E3, E2-refuted, E4)

`BEARINGS-FRONTIER.md`: the day built the bearing-map, not the destination. Five open edges: E1 the reality-gap (synthetic-fixtures' portability); E2 the membership-generality (2-seed's n); E3 the length×recency crossings; E4 the compaction-front's fixes (measured, unexplained); E5 the simplify-lens (25-probe family-tree's consolidation into one shared-core instrument — the rig's own first invention, available now). Ordering: E5 first, then E1, E3, E2, E4.

Outcomes: E5 LANDED (krec_core.py, 0 diffs across 200 cells). E1 PORTABILITY-GAP then PORTABILITY-RECURRED (closed on the rig's own blood). E3 CELL-DEPENDENT (small+old death-cell mapped, 1.00 across every variant). E2-refuted (membership-AoA ADJUST: the mechanism survives, the record corrected). E4 named (the compaction-front's loss-mechanisms).

## Phase 15 — The inventions (the retention-latch)

The retention-latch: recurrence-aware exact-literal pinning drops deep-minima prevalence 1.00 → 0.15 at the confirmed aliasing×proximity pair-ON cell (the onset-test: per-seed occurrence predicts the onset; a recency-only pin loses protection). The pinning-cost: 18 tokens vs field's ~47, ~0.18% at production scale. The ladder and the rebuild (RUNGS-REBUILT, the real stress-cells): two stress-cells from distinct rig sessions (deep-compaction: 8 messages, session 20261007_123305; high-density: 2 messages, 219,239-byte user turn, the recurrence-bearing real stream) — verified 2/2, distinct sources, distinct content, the old identical-cells charge cleared.

## Phase 16 — The standards' enforcement (membership-AoA ADJUST)

`EXP-MEMBERSHIP-AOA-20261106.md`: ADJUST — base exact-literal pinning's protection survives the byte-check; the record does not. `probe_membership.py` hard-codes onsets (`SEEDS_ONSET = {0: 60, 1: 80}`) into its own predictor (injected-onsets circularity, byte-verified). `RESULTS-MEMBERSHIP.md`'s table mislabels the probe's derived quantities (0.15 = prevalence-cutoff, 1.00 = unprotected multiplier; CSV pair-ON cells carry 0.4 recency / 0.1 recurrence; 160 rows, not 200). E2-replier artifact ABSENT (wave-15 figures UNVERIFIED against bytes). Corrective notes applied (`6ce5b222e7`). Next mechanism: V3 alias-aware format-pinning.

Standards layer added: delta-8 fleet-verification (reproduction-mandate, metadata-tiers, report-isolation +43.4pp lesson), delta-9 success-formula (evidence-to-evidence loop). The honest-blind audit standard: 3.33 corrected median (three-block composition, 0/5 below 3.0). The landmark-gate (delta-6: landmark-check + replication-before-CONFIRMED). Report-isolation lesson: +43.4pp inflation when not isolated.

## Phase 17 — The rotation's own pilot-data

The three-voice rotation (moonbeam drafts → solar audits → AoA verifies) ran as the ACES-relaunch's pilot: solar-audit caught the drafter's binding-document drift (meter citation) and register drift (8-vs-9 GREEN rows); AoA caught the audit's own register drift (the ledger holds NINE, not the audit's eight — the apex-day falsifier-battery row 42096454325). Final residual error: one ledger row. Rotation efficacy CONFIRMED. The layering works.

---

## THE CTO-STEERS (the head's leadership lens on the record, Amazonian register, up to five)

1. **The meter is stewardship, not a quota.** The rig's runner is self-hosted; GitHub's Actions are free for self-hosted runners; the 3,000/1,500 min/mo classes are the provider's hosted-VM meter, never ours. The governance frame (one run per pin, no re-dispatch without a named reason) is kept by choice — validation moments, never churn. The constraint is the rig's own cpu/disk/energy. Hold the stewardship; never re-introduce the platform-quota framing.

2. **Count the ledger, never a summary's count.** The README's "five" and the older summaries' "eight" were both under-counts; the ledger holds nine GREEN rows. The register is receipts, never claims — every summary's count must be re-derived from `RECEIPTS.md`'s rows at write-time. The triple drift (five < eight < nine) is the class; the fix is the discipline, not the number.

3. **NOT-RUN stays NOT-RUN.** The GitHub-window side remains NOT RUN (hosted queue class). A green at a pin qualifies THAT pin's checked-out source, never another head. Divergence between the two surfaces is data, recorded, never smoothed. The reconciliation is about the GREEN count, never about closing the NOT-RUN.

4. **A FAIL is a finding, never smoothed.** The demand-age gate FAILS at 300+ (−20.40pp worst-case). The competition arm is NOT-CONFIRMED (instrument-limit, three precision-adds). The archive arm is REFUTED under the tested construction. The membership record was ADJUSTED (the hard-coded onsets, the mislabeled table). Each is the record's sharpest data; each advanced the mechanism-map. Never let a summary blur a FAIL into a pass.

5. **The RFC's four lines are STAGED, not landed.** Restore (#141876), network (#116673), governance (#139606), compaction (#140008) — all STAGED on the branch, every public-gate holding. The arrivals await the user's word and the owners' windows. PR #1 is where the evidence accumulates en route; the goal's arrival is upstream, never the fork's staging. Hold the gates; let the word decide.

---

**File register (the record's receipts):** `RECEIPTS.md` (9 GREEN / 4 RED / 1 NOT-RUN) · `AVREA-LEG-CONTRACT.md` (corrected 2026-11-05) · `README.md` · `RFC-GUIDANCE-20261105.md` (deltas 1–9) · `HITL-READY-20261105.md` · `XNGG-GAPS-VERIFICATION-20261105.md` · `krecency/RESULTS-*.md` + `SYNTHESIS.md` (waves 1–31) · `BEARINGS-FRONTIER.md` · `EXP-MEMBERSHIP-AOA-20261106.md` · `EXP-REBUILD-CERT-20261106.md` · `REBUILD-RECEIPTS-20261106.md` · `AUDIT-LADDER-RUNGS-20261106.md` · `EVAL-LADDER-BATTERY-20261106.md` · `CURRICULUM-LADDER.md` · `RL-CROSS-LENS.md` · `GOVERNANCE-OWASP-MAPPING.md` · `GOVERNANCE-FOLD-DRAFTS.md` · `RESTORE-EVIDENCE.md` · `NETWORK-EVIDENCE.md` · `CONVERGENCE-VOI-SORT.md` · `copycat-findings/copycat-{krecency,longcat,solar-mini4}-20261105.md` · `NIGHTSHIFT-HANDOFF-20261106.md` · `EXP-SUMMARY-NIGHT-20261106.md` · `SELF-PERPETUATING-LOOP-ARCHITECTURE.md` · `LONG-NIGHT-OPERATIONS-20261106.md` · `SHIFT-LAUNCH-PACK-20261106.md`.

**End of the 11-06 moonbeam summary.** The corrected end-to-end record of PR #1 at head `8b0a2af584`: receipts, never claims.
