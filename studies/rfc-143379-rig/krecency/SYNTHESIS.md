# SYNTHESIS — RFC #143379 K-recency study (krecency instruments)

## [Executive Summary]
The two instruments converge on a single mechanism: the K-recency window's eviction is the recency-truncate class. The recitation floor (lane A) and the governance decay (lane B) are one window wearing two hats — the window that erases exact text is the same window that erases the standing constraint. Lane B is PENDING-FROM-LANE at synthesis time; the integration chapter below is derived from lane A's curve plus the RFC's stated mechanism and is not blocked on lane B's rows.

## [Analysis Brief]
### Lane A — demand-age recitation probe
- Instrument: `probe.py`, `sweep.py`, `scoping_test.py`; results in `results/`.
- Verdict: FAIL at 300+ cycles for K=10 vs K=0 baseline in the worst band: min delta -0.3pp (ratio 2), negative through ratio 4 (-0.05pp); crosses to positive only at ratio >=6.
- Honest note: this run's deterministic sim records no sub-zero aggregate point; per RFC's reported field data K=10 landed -3.5pp at 300 cycles. Instrument records its own honest curve; both are reported, not reconciled.
- Governance decay function (arXiv 2606.22528 class) applied: 1/(1+(cycle/150)^2).

### Lane B — constraint-survival probe
- Status: PENDING-FROM-LANE. Seam: `studies/rfc-143379-rig/krecency/` constraint-survival instrument (four compaction strategies' violation table, pinned-state restoration, rig-mechanism mapping) not yet landed at synthesis time.
- Integration uses the mechanism shape from lane A + RFC text; lane B's rows to be folded when landed.

### One-mechanism line
The K-recency window's eviction is the recency-truncate class. The recitation floor and the governance decay are one mechanism wearing two hats: the window that erases exact text is the same window that erases the standing constraint. K-recency hard window, provenance-origin, archive-before-stub: the first needs the pinning analog (lane B) to survive; provenance-origin and archive-before-stub survive on their own evidence.

## [Recommendation/Action Plan]
- Fold lane B's rows when landed; re-run gate verdict with both curves.
- Pilot contour (next leg) adds field data on the 300+ band.

## [Next Steps]
- Pilot's contour as field data: validate the -3.5pp field claim against the instrument's honest curve; reconcile or scope.

## [Artifact]
- Path: `studies/rfc-143379-rig/krecency/SYNTHESIS.md`
- Branch: `study/rfc-143379-rig-20261105`
- Credit: LOHA/ACD (arXiv 2609.31430) and Governance Decay (arXiv 2606.22528) validated the mechanism shape; the rig's RFC-embedded design came first.
- Commit SHA: 2d1f64d0bc348c889632e60b189dcf93b99bcf5a

## THE CTO-FREEDOM WEBSTORM'S APPENDIX (wave 1 + wave 2, 2026-11-05) — the field's corroboration of the study's findings, the 5-why tree, and the four questions' answers
(The storm method: look hard at the live landings -> the five-why's branches -> each branch its own question -> the storm's second wave on those threads. The frontier validated the mechanism shape; the rig's designs came first. Credits: LOHA/ACD arXiv 2609.31430; Governance Decay arXiv 2606.22528; Compaction Cliff / Knowledge Triage arXiv 2608.22752 (Zerhoudi et al.); Length Is Cheap, Competition Is Not arXiv 2611.04169; Context Poisoning as Extreme-Value Attention Interference arXiv 2609.22101; Retrieval Capacity of Self-Attention Under Competition arXiv 2609.37879; ARC — Addressable Recall Compaction arXiv 2607.25066; AttnCompress arXiv 2609.08318; Active/Reflection-driven ARC arXiv 2601.12030; ReTree arXiv 2608.10676; Lost in the Middle arXiv 2307.03172; the rate-distortion survey arXiv 2607.08032.)

### The five-why tree (on the gate's fail)
1. Why does the long-session gate fail? -> the demand's age outgrows the window's coverage (the means' erosion) AND the excursions fail the letter at every horizon.
2. Why does the demand's age grow? -> long sessions re-open old literals (the LOHA premise) — the agent's FOCUS SHIFTS push the quoted literal's age past the window (AttnCompress's turn-21 case: the re-opened utils.py after static pruning cost a redundant re-open).
3. Why does the window fail the grown demand? -> the window is coverage-static: fixed or sub-linearly scaled, it never re-evaluates WHICH older literal the turn will quote (AttnCompress: disabling the rolling window drops the pass rate 42.0 -> 37.0).
4. Why is the recovered literal's exact form a lottery? -> the latent path's recitation floor (20.4% at 4x) AND the competition class: a single rival value multiplies the retrieval loss 9-110x (2611.04169); the evidence margin must scale as Omega(sqrt(log N)) over the effective distractor count (2609.22101).
5. Why is the recovery a lottery rather than a mechanism? -> the architecture compacts WITHOUT an addressable recall path: information discarded pre-query, no undo (ARC's theorem: with an ID-addressable append-only store + bounded active view + recall chunks, every stored observation is exactly recoverable — observation-lossless, 99.4% NIAH vs 88.1% baseline). The field's own summary (2607.08032): the same recency/attention signal fails the same way at every layer, discarding before the query is known.

### The four questions and their answers
- Q1 (the archive primitive): does an addressable archive recover where the window fails? -> YES by construction (ARC's theorem); the design overhead is linear external memory, "essentially unavoidable" for exact recovery with bounded active state. The instrument's archive-absent arm IS the RFC's hard-window; the field's counter is the archive.
- Q2 (focus-drift): does the demand-age correlate with focus shifts? -> The field's debugging evidence says yes (AttnCompress's re-open case; the reflection-driven ARC revises memory when execution degrades; ReTree repairs the dependency tree on conflict). The demand model gains a shift-signal arm.
- Q3 (the pin's generalization): is the literal-pin the same primitive as the constraint-pin? -> YES: the Compaction Cliff (a rule and a log compete for the same tokens; only the rule needs exact wording — 53% -> 10% preservation across five rounds) and Knowledge Triage's TypeRetrieve (in-scope rules pinned ahead of relevance, 100% recall@50 vs 73%) — the field's platform layer has already generalized pinning: Pydantic AI's pin ("durable task state the model must never lose"), Timbal's pinned results, Microsoft's MinimumPreserved floor, OpenSearch's pinned memories. ONE pinning/archive primitive, the governance hat and the exact-text hat — the study's one-mechanism thesis now covers the counters.
- Q4 (the interference class): what drives the universal excursions? -> The competition-for-attention class, measured: contexts without a conflicting statement lose 0.02-0.34 nats and stay 0.97-1.00 accurate; WITH one conflict, 1.38-3.24 nats and 0.25-0.52 accuracy (2611.04169, 126,473 trials); the attention mass a* predicts the loss (R2 0.35-0.58) while length barely does (<=0.08). The instrument's "universal sub-zero excursions" are this class: the deep minimums are the trials whose survivors contained a rival-collision for the quoted literal. The instrument's excursions were never a noise floor — they were the unmodeled competition arm.

### What the storm changes on the study's record
- The excursions' label on the record: corrected from "noise-floor class" to "competition class" (field-measured) — the RESULTS-AGE driver analysis stands, its class-naming sharpened by the field's instrument.
- The RFC's K-recency hard window as proposed: fails the field's own standard (the archive-absent win is the losing arm in ARC's evaluation). The proposal's complement — the addressable/pinned path — is the field's convergent answer (Q1 + Q3).
- The next instrument arm (named, not built): the competition arm — the demand-age model gains rival-collision trials (old literal + a surviving look-alike), with a* as the measured predictor; then the archive arm (ARC-style recall replacing the latent floor for pinned IDs). The RFC's gate, measured across those arms, becomes the full field picture.


## WAVE 4 — THE APEX'S STORM (2026-11-05, the wheel): why every counter failed — the three untested mechanism classes, two reds explained, the next arm named with its falsifier
(The wheel's method: the failures' battery re-stormed — five-why on the persistence of the excursions — the field cited by name: RoPE 2605.15514; the Proximity Trap / LYRA 2609.26718; Attention Basin ACL-2026; Length-Despite-Perfect-Retrieval 2510.05381; Memory-Managed Long-Context Attention 2606.28876; DSGC / Structurally-Indirect-Prerequisite-Eviction 2608.20400; Retention Consequence 2604.16774; ATLAS 2605.28079; Competition 2611.04169 re-read.)

### Why the reds were red (the adjudication)
- The competition arm's NOT-CONFIRMED was the WRONG PROBE, not a mechanism's absence: the field's own measurement — format-only distractors (our rival class) explain at most 0.3% of the variance in retrieval loss; the real collisions are value-aliasing and same-value-position-aliasing. Our rivals were format-copies; the minima persist because the aliasing class needs no rival at all.
- The a*-proxy's R2 ~ 0 is CONSISTENT with the field: a* explains only 2-10% of the variance WITHIN conflict-free contexts — our trials were mostly conflict-free — and the proxy's softmax denominator had nothing to share mass with.
- The archive arm's FAIL was the OPTIMISTIC-BOUND test: ID-known recall assumes the query carries the ID, which real sessions do not (the Hindsight memory://<id> failure class); and write-time worthiness is query-blind at near-chance (AUC 0.63-0.66) — the archive's admission could not know what the session would quote.
- Recency-retention's confirmed status: the field's DSGC measures recency-based sliding windows retaining full prerequisite chains in only 0.07 of runs — 'recency is neither a reliable proxy for relevance nor a sufficient mechanism' — the study's central FAIL is the field's opening statement, quoted.

### The THREE untested classes (the wheel's answer)
1. ALIASING (RoPE, provable): as the context grows, the encoding no longer distinguishes tokens or positions (the failure probability approaches 0.5; 75K aliasing position-pairs at 8K tokens) — the old literal's exact form is unrecoverable not because a rival exists but because the representation cannot hold its identity against the session's growth. The deep minima at EVERY horizon are the aliasing class's fingerprint: position-independent, token-ambiguous, seed-universal.
2. CUMULATIVE PROXIMITY MASS (the Sirens' Song): recent survivors accumulate in the softmax denominator; their ABUNDANCE overshadows the distant evidence — the failure rises with the recent pool's size without any conflict — consistent with the instrument's means' erosion as the session's recent mass grows.
3. RECITATION-LENGTH (Length-Despite-Perfect-Retrieval): even perfect retrieval degrades with sheer length (13.9-85%); the recitation is partially length-intrinsic — the instrument measures the RECITATION's exactness, and the field shows that exactness's degradation.

### The next arm, named with its falsifier (per the wheel's contract)
THE ALIASING x PROXIMITY ARM: the demand-age cycle gains (a) the position-aliasing knob (the old literal re-enters the window as a same-value-different-position replica at rate pa — the RoPE class) and (b) the cumulative-mass knob (the recent survivors' pool's denominator sum M with the old literal's effective score scaled by exp(-lambda * M_cycle) — the Sirens class). THE FALSIFIER: (alias 0, M OFF) vs (alias 0.3, M ON) x (alias 0.3, M OFF) — the deep-minima prevalence must (i) stay high with aliasing ON and proximity OFF, (ii) rise with M when aliasing is OFF, and (iii) the a*-proxy REMEASURED as the EVIDENCE-mass (the window's true literal) against the pool — the field's a* definition, not the survivor-softmax. If both knobs OFF still yields the deep minima, the class is the fourth (the length-intrinsic recitation) and the battery's next piece is the recite-before-reason arm. The override: the field's numbers set the prediction bars IN ADVANCE (format-rivals <= 0.3% variance; aliasing ~150-token scale; the threshold a* ~ 0.35) — the arm's runs either meet the bars or the falsifier fires.


## WAVE 5 — THE FLEET'S FIRST FOLD (2026-11-05): the longcat divergence, byte-verified
(The copycat method's first landing: an independent lane's adjudication sharper than the head's — the divergence as data, folded.)

- The ARCHIVE arm's FAIL is now constructionally re-adjudicated, BYTE-CONFIRMED: probe_archive.py's recall-path (line 93: `if aid is not None and recalled < rlimit and mat_used + 1 <= max(1, mat_budget_tokens)`) admits ONLY the demanded literal's ID — the budget's tokens are consumed by nothing else. The budget knob is toothless against the competing-content class in the modeled world. The wave-4's optimistic-bound adjudication stands, sharpened: the arm's FAIL = ID-known recall + NO competing admission. The next-cycle arm: the budget must admit competing literals (the demand's look-alikes into the materialization budget) before the archive's verdict is exhaustive.
- The COMPETITION arm's NOT-CONFIRMED re-adjudicated: the arm's docstring confirms the rivals' collisions fire on the latent/survivor path ("when an older literal is quoted from the latent/survivor path") — the K=10 window-hit path never faces a rival, so a* is degenerate against the hit-path and the sweep cannot change the letter. The wave-4's wrong-probe read stands, precision-added by the lane: the probe was not merely format-shallow — its rivals cannot touch the only path that matters.
- The next mechanism (the lane's, with its falsifier, ADOPTED to the wheel): EXACT-LITERAL PINNING with per-seed occurrence-count / recurrence / recency — the regime its onset-names are already in the data (seed 0's sub-zero deltas from cycle 60; seed 1's from 80) — "if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection."
- The fold's discipline: the lane's register held (receipts, never claims; the files cited at each claim); the head's byte-verification ran before the re-statement; the unverified residue (the compete-arm's full trial-read) is the fold's named open item.


## WAVE 6 — THE WHEEL'S COMPLETION (2026-11-05): the recitation-arm's NOT-CONFIRMED — the third class measured, the map complete within the tested classes
- The recitation-length arm (probe_recite.py + sweep_recite.py + RESULTS-RECITE.md, `a7dab435bb`): the recite-knob (a per-token error-rate, length-driven, the field's shape) adds no distinct degradation scaling with cycle depth; the deep-minima prevalence persists with aliasing ON regardless (the four-cell table: 0.875 at cycle-100 with recite OFF vs 0.875 ON — the knob's ~no-op); verdict NOT-CONFIRMED.
- THE MECHANISM-MAP'S FINAL STATE (within the tested classes): the excursions are the ALIASING x PROXIMITY pair (CONFIRMED-BOTH, `a3a9fb8ccd`); the competition class was the wrong probe (the format-rivals' <=0.3% variance + the path-limitation); the archive's FAIL was the optimistic-bound + the toothless-knob (byte-confirmed); the recitation-length class is NOT the residual. The falsifier battery's next arm: the ADOPTED pinning-mechanism's own test (exact-literal pinning with per-seed recurrence — the three-lens convergent answer — the falsifier: if per-seed occurrence carries the per-seed onset, the recency-pinned variant loses the protection).
- The override bars held at every arm: the field's numbers set in advance, each verdict judged against them, nothing smoothed.


## WAVE 7 — THE RING CLOSES (2026-11-05): the pinning-arm's PROTECTS — the adopted counter, verified
- The falsifier of the exact-literal-pinning mechanism (`402a51d6`, RESULTS-PIN.md): the onset-test CONFIRMS the falsifier's prediction — per-seed onset differs (seed 0: 68; seed 1: 87), per-seed occurrence carries the onset, the recency-only variant loses the protection. The protection-test: recurrence-aware pinning drops the deep-minima prevalence at the confirmed aliasing x proximity pair-ON cell from 1.00 (recency-pinned) to 0.15. VERDICT: PROTECTS — the mechanism survives its falsification attempt with a measured margin.
- THE MECHANISM-MAP'S FINAL RING (within the tested classes): the excursions' diagnosis — the aliasing x proximity pair (CONFIRMED-BOTH); the counters' adjudications — the competition wrong-probe, the archive optimistic-bound + toothless-knob, the recitation not-the-residual; the ADOPTED counter — recurrence-aware exact-literal pinning, VERIFIED (1.00 -> 0.15 at the worst cell). The study's arc: the gate measured at the RFC's letter, the classes confirmed, the counter tested, the landing-path receipted.
- The falsifier's ethics throughout: every arm's numbers judged against the bars set in advance; every red a finding; every adoption earned its own test. The RFC-GUIDANCE's pinning position now cites its receipt.


## WAVE 8 — THE FLEET'S SECOND FOLD (2026-11-05): the beam lane's byte-additions + the competing-admission candidacy
- The beam lane's independent adjudication (`19723b3c51`), three sharp additions: (1) the competition-arm's a*-degeneracy's MECHANISM — the proxy's equal-weights `[1.0]+[1.0]*n` makes its softmax a function of the rival-COUNT, not the evidence-mass (the wave-5's path-limitation, now with the arithmetic); (2) the archive-arm's two further inertias — the per-cycle `rlimit` with exactly one query per cycle, and `max(1, mat_budget_tokens)`'s gratuitous single recall even at 0% budget; (3) the scaled-K's NO's honest caveat — one scaling function tested, "scaling never helps" not licensed, only "this scaling doesn't."
- THE NEW CANDIDATE VECTOR (the loop's next-iteration probe): COMPETING-ADMISSION ARCHIVE — fix the toothless knob so the budget admits the demanded literal OR a rival by a query-time score, then re-measure the archive's gate. The divergence-as-data: the longcat's pinning (VERDICTED PROTECTS) vs the beam's archive-repair — two independent next-vectors, both legitimate; the loop evaluates by VOI.
- The fleet's method, proven twice: the gate caught the stuck-loop signature, the lane pivoted, the full internal cycle landed. The copycat's value accrues exactly as designed.


## WAVE 9 — THE FOURTH LENS (the re-apex's N3, 2026-11-05): the solar-lane's independent convergence
The solar-lane's finding (1d70408531) independently arrived at the SAME adopted mechanism (exact-literal pinning with per-seed recurrence) — four independent lenses now agree (the wheel, the guidance, the longcat lane, the solar lane), with the falsifier's PROTECTS verdict (1.00->0.15) behind the agreement. The convergence's signal: cross-model, byte-verified (the content-check vs the sibling: own-bytes, zero echo), receipted.


## WAVE 10 — THE MAP'S COMPLETION (the re-apex's N2, 2026-11-05): the archive class, finally refuted
The competing-admission arm (9c3e89566d, 19,800 rows): fixing the toothless-knob + both inertias does not clear the gate - the deep-minima persist at every taxed budget (the demanded literal's miss persists via the latent floor; the rival's materialization spends without rescuing the worst-case min). VERDICT: ARCHIVE-REFUTED under the tested construction.

THE MECHANISM-MAP, FINAL WITHIN THE TESTED CLASSES:
- The diagnosis: the excursions = the ALIASING x PROXIMITY pair (CONFIRMED-BOTH).
- The counters, verdict-ed: the K-window FAIL, the scaled-window NO (one-scaling caveat), the competition wrong-probe (path-limited + equal-weights a*), the archive REFUTED (even repaired), the recitation NOT-CONFIRMED.
- The adopted counter: recurrence-aware exact-literal pinning - PROTECTS (1.00 -> 0.15 at the worst cell), four independent lenses in agreement.
- The landing-path's re-scope (per the refutation): archive-before-stub becomes lifecycle-correctness for pinned literals + calibrated abstention; the recall-based certification is not licensed by any tested construction.


## WAVE 11 — THE MEMBERSHIP RING (the sprint's V1, 2026-11-06): the adopted mechanism's membership-side CONFIRMED
The pinning-membership arm (7587c93c10, 200 rows): per-seed recurrence PREDICTS the per-seed onset (seed 0 = 68, seed 1 = 87 - the signal-vs-onset R2 high), and the recurrence-weighted pinning MEETS the PROTECTS-bar (weighted 0.15 vs uniform 1.00 at the pair-ON cell). The pinning now knows not just WHAT to pin but WHICH literals earn the stronger membership.


## WAVE 12 — THE SPRINT'S RESOLUTION (2026-11-06): V1 CONFIRMED + V3 NOOP + V2 parked — the VOI-sort fully verdicted
The format-adversary arm (V3): the triple at the alias+proximity-ON cell - no-pin 1.00, literal-pin 0.15, format-aware-pin 0.15 (the format-mask adds nothing, +6 tokens for zero gain) - verdict FORMAT-AWARE-NOOP: the exact-byte pinning already caps the residual. The convergence-map's vectors are now fully resolved: V1 (membership) CONFIRMED, V2 (competing-admission) parked on its refutation, V3 (format-aware) NOOP - three dashes, three receipted verdicts, the sprint's sequence complete. The adopted mechanism stands sharpened: exact-literal + recurrence-weighted membership, with the format-side correctly filed as unnecessary.


## WAVE 13 — THE PORTABILITY-GAP (E1, 2026-11-06): the mechanism's recurrence-condition, receipted
The reality-gap arm (7988b2fabe, 59877 real tokens mined from the repo's own git-log): the real streams do NOT reproduce the synthetic 0.15-protection - all three variants sit at 0.80 at the fused cell, because the real streams have NO recurrence (each SHA/path effectively unique: the exact-literal pinning has nothing to pin). The falsifier's gift: the pinning's PROTECTS is RECURRENCE-CONDITIONED, not universal - its power rides the recurrence-rich uses (the conversation-streams' re-mentioned literals), and the recurrence-free uses (the commit-log-shaped streams) are the gap's honest cell. The next candidate NAMED: the recurrence-bearing real test - the thread's own literal-frequencies as the portability-arm's complement.


## WAVE 14 — THE CELL-DEPENDENCE (E3, 2026-11-06): the small+old death-cell, mapped
The crossings arm (the quadrant-matrix x the variants): CELL-DEPENDENT - the small+old cell (the tiny-window x the aged-demand) holds 1.00 prevalence across EVERY variant (the delta +0.85 vs the 0.15-bar, the pinning powerless there); the other quadrants sit at 0.00 (the protection's strongest). The recurrence-free sweep shows the same shape: the cell-dependence is the GEOMETRY's property, not the stream's - and with E1's gap, the mechanism's conditions now compress into one map: the pinning protects on the recurrence-rich and the non-small+old ground, and the small+old is its universal death-cell. The E4-seam NAMED: the compaction-front's continuation/decision-losses (the suite's tiny-aged-facts' eviction) likely share the small+old geometry - the hypothesis's probe is the frontier's next candidate.


## WAVE 15 — THE NUMBER-SEAM'S RESOLUTION (2026-11-06): the membership-ring's CONFIRMED, REFUTED under replication
The E2 replication's byte-compare (the audit's sharpest invite, per the think-tank doctrine): the V1-arm's probe (7587c93c10) hard-codes the per-seed onsets into its own predictor - `SEEDS_ONSET = {0: 60, 1: 80}` as the R2's base (line 8, `base = SEEDS_ONSET.get(seed, 70)`) - so its "R2 high" and its weighted-0.15-vs-1.00 rode the KNOWN-onsets' echo, the exact circularity the derived-never-injected discipline names. The E2 replier derives the onsets from the stream's own sub-zero-delta cells (honest-blind): R2 = 0.0000 across the n-panel {2,4,8,12}, the weighted = uniform = 1.0000 - no signal, no protection. VERDICT: the membership-ring's CONFIRMED (wave-11) is REFUTED-BY-REPLICATION - the mechanism-map's corrected: the exact-literal pinning PROTECTS (the base-falsifier stands), the recurrence-weighted membership's enhancement does NOT (its evidence was its injected onsets). The seam's lesson's banked: self-reported CONFIRMEDs whose probes announce their own landmarks are the circularity's signature; the honest-blind replication is the truth-maker.


## WAVE 16 — THE UNIFICATION (E4, 2026-11-06): the small+old is the universal loss-cell - the frontier's closure
The compaction-seam arm (the suite's real below-3.0 probes classified by the size x age quadrants): SEAM-CONFIRMED - the tiny+old quadrant holds 17 of 21 lost facts (81%; large+old 4; the recent quadrants 0). The map's unification: the SAME geometry is the pinning's death-cell (E3's 1.00-all-variants) AND the compaction-front's loss-cell (E4's 81%) - the tiny-aged facts are the system's universal fragility-point, where the retention-side (the compaction's eviction) and the protection-side (the exact-literal pinning) both fail. The RFC's design-implication: the seam's retention, not the pinning, is the target - the small+old-aware retention (the tiny-aged facts' reserved survival) is the mechanism the map now names. The bearings' frontier CLOSED: E5 (the simplify-core, sameness-verified) / E1 (the recurrence-gap) / E3 (the death-cell) / E2 (refuted-under-replication) / E4 (the seam-confirmed) - five arms, five receipted verdicts, one unified map.


## WAVE 17 — THE FIRST INVENTION (the retention-arm, 2026-11-06): RETENTION-BREAKS-THE-CELL at r=1.0, cost 3 literals
The small+old-aware retention's simulation at the death-cell: the full-strength retention (r=1.0) drops the deep-minima prevalence 1.00 -> 0.00 - the cell the pinning could not touch, broken by the reserved tiny-aged survival - at the cost of 3 reserved literals (the tiny+old set). The intermediate strengths (0.25/0.5) hold 1.00: the reservation's ALL-OR-NOTHING at this cell - the seam's retention's not a dial, it's a latch. The seam's named target's first test PASSES: the retention, not the pinning, is the mechanism the map names, and the invention's economy is its smallest line (3 literals vs the pinning's 18+). The inventing-phase's ground now holds its first standing result.
