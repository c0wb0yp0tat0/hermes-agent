# EVAL-LADDER-BATTERY-20261106 — the ladder-battery's per-rung recovery table and the depth-vs-density verdict

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Gate:** RUNGS-BUILD landed (`697cd49de7`, verified 2/2). **Seat:** curriculum-ladder battery. **Status:** PARTIAL — wall clause (provider window closed); no live run executed in this battery.

## [Executive Summary]

The five-rung ladder is now in place by construction, but it is **not yet separated by measurement**. Rungs 1-3 carry recorded recovery medians and miss counts (`CURRICULUM-LADDER.md`: 4.333 / 4.000 / 4.667; misses 2 / 4 / 0) that reproduce the non-monotonic depth-vs-density pattern; rungs 4-5 (`fixture-deep-compaction.json`, `fixture-high-density.json`) are schema-verified at build but unprobed because the provider window is closed. Verdict: **LADDER-PARTIAL** — structural coverage improved, measurement did not run, and depth vs. density remain unseparated on evidence. The seam-arc's corrected honest-blind standard (3.33, three-block composition, 0/5 below 3.0) stands as the bar rungs are read against. The gate holds; the row posts as partial.

## [Analysis Brief]

### (a) Per-rung recovery table — rungs 1-3 (records-grounded, CURRICULUM-LADDER.md §(a)-(b))

| Rung | Fixture | pre_tokens | pre_msgs | compaction ratio (depth) | recovery median | misses (density proxy) |
|------|---------|-----------:|---------:|------------------------:|----------------:|-----------------------:|
| 1 | config-build-competitive-scouts | 25813 | 61 | 0.171 | 4.333 | 2 |
| 2 | debug-session-feishu-id-model | 27977 | 59 | 0.625 | 4.000 | 4 |
| 3 | feature-impl-context-priority | 44794 | 75 | 0.687 | 4.667 | 0 |

Recorded pattern (honest, from the records): feishu 4.000 is the worst recovery (4 misses, incl. 2 zero-answer continuations) -> config 4.333 (2 misses) -> feature 4.667 (0 misses). The gradient is non-monotonic by compaction depth: the deepest compaction (feature, 0.687) recovers best, while the mid-depth rung (feishu, 0.625) recovers worst. Interpretation carried from the record: recovery tracks fact-density / context-crossings, not compaction depth alone.

### (b) Per-rung status — rungs 4-5 (RUNGS-BUILT.md; schema-verified at build)

| Rung | Fixture | class | axis intent (by construction) | recovery median | misses | retention-reward scalar | status |
|------|---------|-------|-------------------------------|----------------:|-------:|------------------------:|--------|
| 4 | rungs/fixture-deep-compaction.json | eval schema, config-JSON class | deep-compaction stress (high ratio) | NOT RUN | NOT RUN | NOT RUN | schema-verified at build; smoke blocked by provider (no credentials) |
| 5 | rungs/fixture-high-density.json | eval schema, config-JSON class | high fact-density stress | NOT RUN | NOT RUN | NOT RUN | schema-verified at build; smoke blocked by provider (no credentials) |

No measured pre_tokens / pre_msgs / ratio / miss counts are claimed for rungs 4-5 here; their measured axis positions are pending a provider-credentialed run.

### (c) Retention-reward scalar

Definition carried from the retention arm: the measured survival weighted into per-rung scores (retention r = 1.0 full retention drops deep-minima prevalence 1.00 -> 0.00; r in {0.0, 0.25, 0.5} stay at 1.00; cost line 3 tiny-aged literals, <= 3 tokens, age >= threshold; token budget 3 tokens; `RESULTS-RETENTION.md`).

- Rungs 1-3: no single retention-reward scalar is recorded in the ladder records. Recovery medians (4.333 / 4.000 / 4.667) and miss counts (2 / 4 / 0) are the recorded proxies; the scalar is not re-derived in this battery.
- Rungs 4-5: NOT MEASURED (provider wall).

Scalar status for this battery: UNMEASURED.

### (d) Standard of comparison (seam-arc, corrected honest-blind)

The honest-blind reproduction (`RESULTS-AUDIT.md`) corrected the seam-cleared median to **3.33** (three-block composition: derivations + time-anchors + forward-intents; 0/5 below 3.0; probes 3.33 / 3.00 / 3.00 / 3.00 / 3.33). That 3.33 is the standard rungs are read against. All three recorded rungs sit above it (4.333, 4.000, 4.667); feishu (4.000) is the closest to the floor among rungs 1-3.

### (e) Depth-vs-density verdict (the LADDER-GAPS named need)

Question: does the complete ladder now separate compaction-depth from fact-density?

Answer: **NOT YET, BY MEASUREMENT.** Structurally, the ladder now has all five rungs in place by construction, and rungs 4-5 add the two stress cells the ladder named as missing (deep-compaction stress and high fact-density stress; `RUNGS-BUILT.md`). But no recovery, miss count, or retention-reward scalar exists for rungs 4-5, and rungs 1-3 were not re-measured in a single comparable battery here. Therefore the read-side alone cannot yet say whether the composition-fix helps depth, density, or their interaction. The original non-monotonic pattern (deepest compaction recovering best) is reproduced by the recorded rungs 1-3, but the inverse cells needed to isolate the axes are unmeasured.

Verdict: **LADDER-PARTIAL**. Structural coverage improved; measurement did not run; depth and density are not yet separated on evidence.

### (f) Wall clause (recorded state)

- Provider window closed: no credentials; the new rungs' smoke was already blocked at build (`RUNGS-BUILT.md`: "Smoke blocked by provider (no credentials)").
- This battery executed no live run. Rungs 1-3 values are carried from `CURRICULUM-LADDER.md`, not re-measured here. Rungs 4-5 have no values and no NOT-RUN marker is removed.
- Partial landed per the wall clause; the gate holds; the row posts.

## [Recommendation/Action Plan]

- Re-run the 5-rung battery once provider credentials are available; execute rungs 4-5 first probes (recovery + retention-reward scalar) and re-measure rungs 1-3 in the same battery for comparability.
- Populate the rungs 4-5 axis table (pre_tokens, pre_msgs, ratio, misses, context-crossings) from the run, not from construction.
- Read the resulting per-rung medians against the 3.33 honest-blind standard before declaring LADDER-SEALED or LADDER-GAPS-2.

## [Next Steps]

- Provider-credentialed run of the complete 5-rung battery, then depth-vs-density adjudication.
- Until then, LADDER-PARTIAL stands; no NOT-RUN marker is cleared by this artifact.

## [Artifact]

- File: `studies/rfc-143379-rig/EVAL-LADDER-BATTERY-20261106.md`
- Branch: `study/rfc-143379-rig-20261105`
- Grounding: `CURRICULUM-LADDER.md` (rungs 1-3 medians 4.333 / 4.000 / 4.667, misses 2 / 4 / 0); `RUNGS-BUILT.md` (rungs 4-5 schema-verified, smoke blocked by provider); `RESULTS-AUDIT.md` (corrected honest-blind standard 3.33); `RESULTS-RETENTION.md` (retention-reward scalar definition).
- Commit: this commit.
