# Curriculum Ladder — the composition-fix's graduated test-scale (wildcard-seat first seam)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Seat:** curriculum-arm (wildcard first-seam adoption, per RL-CROSS-LENS SEAMS-NAMED #1). **Receipts, not claims.**

## [Executive Summary]

Designs the graduated-depth ladder for testing the composition-fix across the compression-eval fixture-families. Three rungs exist today (config-build, debug-feishu, feature-impl). Verdict: **LADDER-GAPS** — the gradient is non-monotonic (hardest compaction recovers best), and two intermediate rungs are missing before the ladder can honestly certify the composition-fix. Public gate: lands on branch only.

## [Analysis Brief]

### (a) The ladder's design — complexity axes & rung positions

Axes: session length (pre_tokens / pre_message_count), compaction depth (compression_ratio), fact-density (misses / probe count), context-crossings (multi-topic turns).

| Rung | Fixture | pre_tokens | pre_msgs | ratio | overall_median | misses |
|------|---------|-----------|----------|-------|----------------|--------|
| 1 | config-build-competitive-scouts | 25813 | 61 | 0.171 | 4.333 | 2 |
| 2 | debug-session-feishu-id-model | 27977 | 59 | 0.625 | 4.000 | 4 |
| 3 | feature-impl-context-priority | 44794 | 75 | 0.687 | 4.667 | 0 |

Easy->hard by compaction depth: config (0.171) -> feishu (0.625) -> feature (0.687).

### (b) Calibration data (honest, from records)

Per-rung recovery: feishu 4.00 (worst, 4 misses incl. 2 zero-answer continuations) -> config 4.33 (2 misses) -> feature 4.67 (0 misses). The gradient is non-monotonic: the deepest compaction (feature) recovers best, while the mid-depth rung (feishu) recovers worst. Interpretation: recovery tracks fact-density / context-crossings, not compaction depth alone.

### (c) Verdict: LADDER-GAPS

Missing rungs needed before the composition-fix can be certified:
1. A shallow-compaction + high-fact-density fixture (config-like depth, feishu-like density) to isolate depth vs density.
2. A deep-compaction + low-fact-density fixture (feature-like depth, config-like density) to test the inverse.

Without these, the ladder cannot distinguish whether the composition-fix helps depth, density, or their interaction.

## [Recommendation/Action Plan]

- Add the two missing fixture-rungs to hermes-compression-eval before re-running the composition-fix battery.
- Re-run with curriculum ladder ordering once rungs exist; track retention-reward scalar per rung.
- Keep all findings on fork branch.

## [Next Steps]

- Spec the two missing fixtures against the existing fixture schema.
- Re-run falsifier battery with the complete ladder.

## [Artifact]

- File: `studies/rfc-143379-rig/CURRICULUM-LADDER.md`
- Commit on branch `study/rfc-143379-rig-20261105`, pushed; `git ls-tree HEAD --name-only studies/rfc-143379-rig/ | grep -ci CURRICULUM` = 1.
- SHA: recorded at commit time.
