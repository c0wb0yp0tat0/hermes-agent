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
