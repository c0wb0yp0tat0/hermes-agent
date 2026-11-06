**[WEB-STORM GUIDANCE 2026-11-05] — the harvest's four mechanisms + the steers, for every leg that references PR #1**

**[Executive Summary]** — The automated nuanced web-storm's batch (the 11-02→11-04 harvest, four mechanisms) lands as guidance at homebase: each mechanism's mapping to the study's surfaces + the steering that follows. Design stays ours; the field additive — corroborations and new steers, no architecture change.

**[Analysis Brief — the four mechanisms, byte-cited]**

1. **FlyHash (arXiv 2611.05791)** — retrieval quality-per-bit robustly beats SimHash (all 20 comparisons, genuine non-circular labels), but HNSW dominates both on quality+latency at ordinary scale. **Mapping:** the memory-economy ρ retrieval term + the `@doc:` resolution. **Steer: default to HNSW/ANN; hashing is a niche under severe per-record storage budgets, not a default** (the honest-narrowing corrects a "hashing is competitive" assumption).

2. **Kernel interpolatory compression (arXiv 2610.40943)** — GAIM/Q-DAIM empirical-interpolation KV-cache compression. **Mapping:** the compression-delivery fidelity ladder gains a mathematical selection method (interpolation-based, not learned). **Steer: additive, no mechanism change.**

3. **AC3 (arXiv 2611.00518)** — context pollution in multi-turn: a separate analyzer rebuilding the task spec from USER messages only; pollution is contagious (an analyzer seeing assistant reasoning degrades performance; prompting does not close the gap) → **structural exclusion required**. **Mapping:** context-management + read-side admission + the analyzer/shielding pattern. **Steer: shield spec extractors from assistant reasoning structurally, not via instructions** — the same rule as the write-gate's L0, confirmed from the conversation side.

4. **LegoSR (arXiv 2610.33465)** — self-improving agent with an experience library of lessons from graded tasks; +29pp over a generic agent with the same model/tools/budget; lessons describe choices+conditions and transfer across families. **Mapping:** the chain as the experience library; corroborates the append-only spine.

**[Recommendation/Action Plan — the enrichment proposals' statuses (staged, per the surface-gates)]**
- **READY:** the PR #135039-staged comment (the read-side provenance section's AC3-insert); the live-gist's retrieval subsection's honest-scope (HNSW-default, hash-only-under-budget).
- **NOT-READY (the user's read-gate):** the #116673 check-in's LegoSR-lesson-bank fold (placement + the gate before any posting).

**[Next Steps]** — The steers ride with the legs referencing this PR: the retrieval-default's correction, the structural-exclusion rule, the additive ladder, the spine's corroboration. The enrichments stay staged until their gates open.

**[Artifact]** — This thread; the rig's own 009-wins.md (the harvest's persist, grep-verified); the four papers by identifier.
