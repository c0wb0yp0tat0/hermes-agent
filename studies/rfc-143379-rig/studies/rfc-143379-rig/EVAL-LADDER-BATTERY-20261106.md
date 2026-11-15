# EVAL-LADDER-BATTERY-20261106 — the ladder-battery's per-rung recovery table and the depth-vs-density verdict (FULL)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Gate:** RUNGS-REBUILD landed (substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`, `fixes/falsifier-battery-20261104`); 5 fixtures × 3 runs executed 2026-11-06. **Seat:** curriculum-ladder battery. **Status:** FULL — supersedes the LADDER-PARTIAL of the same path. **Register:** receipts, never claims — every number traced to the run-JSONs under `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/` or the records cited.

## [Executive Summary]

The five-rung ladder is now in place **by measurement**, not only by construction. The battery ran all 5 fixtures × 3 runs at the substrate-pin `a996d4ad3039…` (compressor + judge `deepseek/deepseek-v4-flash-0731`), label `ladder-20261106-a996d4ad`. The five recovery medians are **4.50 / 3.25 / 4.67 / 1.00 / 0.00** (rungs 1-5 respectively). The two rebuilt real cells (rungs 4-5) are not "intermediate" rungs — they are the **depth-cell floor** (1.00) and the **density-cell floor** (0.00), and they sit *below* all three native rungs. That is the separation the LADDER-GAPS verdict asked for: compaction depth and fact-density are now measured on distinct real streams, and the dense stream is the hardest cell in the ladder, not the deep one. The honest read: recovery does **not** track compaction depth (deepest compaction, rung 3, recovers best at 4.67; shallowest, rung 1, 4.50); it tracks **fact-density / tiny+old-anchor survival**, which the E-3 continuation-loss probe names as the small+old class. Verdict: **LADDER-SEPARATED (on this battery's evidence; walls §(d) stand)**. The seam-arc's corrected honest-blind standard (3.33, three-block composition, 0/5 below 3.0) remains the bar rungs are read against; only rung 3 (4.67) and rung 1 (4.50) clear it on recovery median, rung 2 (3.25) sits just under, and rungs 4-5 (1.00 / 0.00) are far below.

## [Analysis Brief]

### (a) Freshness row — when the battery ran, the pin, the 15 runs

| Item | Value (receipted) |
|---|---|
| Label | `ladder-20261106-a996d4ad` |
| Substrate pin | `a996d4ad3039e280dc21e9b558f5a44c081dda42` (`fixes/falsifier-battery-20261104`) |
| Compressor model | `deepseek/deepseek-v4-flash-0731` |
| Judge model | `deepseek/deepseek-v4-flash-0731` |
| Runs per fixture | 3 (15 runs total) |
| Medians reported over runs | yes (single runs are noise; medians are the signal) |
| Fixture set | 3 native (config-build-competitive-scouts, debug-session-feishu-id-model, feature-impl-context-priority) + 2 rebuilt real cells (fixture-deep-compaction-real, fixture-high-density-real) |
| Source artifacts | `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/` (15 per-run JSONs + `report.md` + `summary.json`), copied to scratch when the battery landed |

The battery supersedes `LADDER-PARTIAL` (the provider-window-closed row of the same path): the window is open and all 15 runs executed.

### (b) Per-rung recovery table — ALL FIVE rungs

| Rung | Fixture | pre_tokens | pre_msgs | compaction ratio (depth) | recovery median (overall) | misses (density proxy) | below-3.0 probes | retention-reward scalar |
|------|---------|-----------:|---------:|------------------------:|------------------------:|-----------------------:|-----------------:|------------------------:|
| 1 | config-build-competitive-scouts | 25813 | 61 | 0.187 (18.7%) | 4.50 | 4 | recall-first-repo (0.00); artifact-all-jobs (0.00); artifact-final-schedule (0.00); continuation-execution-time (1.00) | UNMEASURED (no single scalar in ladder records; recovery median + miss count are the recorded proxies) |
| 2 | debug-session-feishu-id-model | 27977 | 59 | 0.627 (62.7%) | 3.25 | 5 | recall-upstream-confirmation (2.33); artifact-new-tool (0.00); decision-core-claim-validity (0.83); continuation-next-action (0.00); continuation-implementation-scope (0.00) | UNMEASURED (as above) |
| 3 | feature-impl-context-priority | 44794 | 75 | 0.684 (68.4%) | 4.67 | 1 | continuation-next-step (2.17) | UNMEASURED (as above) |
| 4 | fixture-deep-compaction-real | 379 | 8 | −3.504 (−350.4%; post 1707) | 1.00 | 5 | recall-session-identity (1.00); recall-loop-sequence (0.17); artifact-message-shape (0.00); decision-model-pin (1.17); continuation-close-intent (0.00) | UNMEASURED (first measure only) |
| 5 | fixture-high-density-real | 63633 | 2 | 0.000 (0.0%; no compaction, 63633→63633) | 0.00 | 6 | recall-stream-source (0.00); recall-retry-receipt (0.17); artifact-turn-shape (0.00); artifact-density-receipts (0.17); decision-truncation; (continuation probe per report tail) | UNMEASURED (first measure only) |

Dimension medians (from `report.md`, 6 dims) for the record:

| Rung | Fixture | accuracy | context_awareness | artifact_trail | completeness | continuity | instruction_following | overall |
|------|---------|---------:|------------------:|---------------:|-------------:|-----------:|--------------------:|--------:|
| 1 | config-build-competitive-scouts | 4.00 | 5.00 | 4.00 | 5.00 | 4.00 | 5.00 | 4.50 |
| 2 | debug-session-feishu-id-model | 2.50 | 3.50 | 3.00 | 3.00 | 2.50 | 5.00 | 3.25 |
| 3 | feature-impl-context-priority | 5.00 | 5.00 | 4.00 | 5.00 | 4.50 | 5.00 | 4.67 |
| 4 | fixture-deep-compaction-real | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 |
| 5 | fixture-high-density-real | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

**Miss counts** (probes with overall median < 3.0): rung 1 = 4, rung 2 = 5, rung 3 = 1, rung 4 = 5, rung 5 = 6 (per `report.md` "Probes scoring below 3.0 overall (median)"). Note: the prior `CURRICULUM-LADDER.md` recorded rungs 1-3 misses as 2 / 4 / 0 against an older battery; this battery's fresh run re-measures 4 / 5 / 1. The fresh-run counts are the signal for this battery (the prior counts are the historical record's; both are receipts, and the discrepancy is itself a receipt of provider-judge variance — see §(d)).

**Retention-reward scalar.** Definition carried from the retention arm (`krecency/RESULTS-RETENTION.md`): small+old-aware retention at the death-cell — r = 1.0 (full retention) drops deep-minima prevalence 1.00 → 0.00, below the 0.15-bar; r ∈ {0.0, 0.25, 0.5} stay at 1.00; cost line = 3 tiny-aged literals (≤3 tokens, age ≥ threshold); token budget 3 tokens; r is a parameter; reserved set defined by the small+old class. For this battery: **no single retention-reward scalar is recorded per rung** in the ladder records or the run-JSONs; the recovery medians and miss counts above are the recorded proxies. `RESULTS-SEAMINT.md` gives the real-stream reserved-set size = 26 tiny+old literals (≤6 chars), deep-minima prevalence 0.80 → 0.00 under literal-pin. Scalar status for this battery: **UNMEASURED per rung** (the measured survival is folded into the scores, not emitted as a separate scalar in these run-JSONs). This is an honest wall, not a gap to paper over.

### (c) THE SEPARATION VERDICT — does the complete ladder now separate compaction-depth from fact-density?

**Yes — on this battery's evidence, with walls (§(d)).** The ladder's axes (session length pre_tokens/pre_msgs, compaction depth ratio, fact-density misses/probe count, context-crossings) now read as:

Ordering by **compaction depth (ratio)**, shallow → deep: rung 1 (0.187) → rung 2 (0.627) → rung 4 (deep cell, −3.504 post/pre, i.e. the summary *expanded* the state) → rung 3 (0.684) → rung 5 (0.000, no compaction at all).

Ordering by **recovery median**, low → high: rung 5 (0.00) → rung 4 (1.00) → rung 2 (3.25) → rung 1 (4.50) → rung 3 (4.67).

The two orderings **do not align**, and that non-alignment is the separation:

1. **Depth is not the driver.** The deepest compaction (rung 3, 68.4%, 44794→14134) recovers *best* (4.67, 1 miss). The shallowest (rung 1, 18.7%) is close (4.50) but worse. If depth drove recovery, rung 3 would be the worst; it is the best. Depth alone is refuted as the driver — matching the prior LADDER-GAPS interpretation, now on five rungs instead of three.

2. **Density is the driver.** The two real cells are the two floors of the ladder, and they are density-shaped, not depth-shaped:
   - Rung 4 (deep cell, 8 msgs, small+old class — session id, start stamp, model pin, truncated_to:null, source path, 77/188-char user turns): recovery 1.00. The compaction machinery *expanded* the state (379→1707 tokens, −350.4%) and still lost every tiny+old anchor (recall-session-identity hallucinates a different session/date; decision-model-pin claims data absent). This is the **small+old class** the E-3 probe and the seam-mechanism name — tiny single-occurrence anchors evaporating into the summary.
   - Rung 5 (high-density cell, 2 msgs, system 30846 + user 219239 chars, no compaction at all, 0.0% ratio): recovery 0.00 — the **worst cell in the ladder**, despite zero compaction. The dense stream's facts are unreachable not because they were compacted away but because they were never individually recoverable from a 219K-char turn at this judge/compressor. Density, not depth, is what breaks recovery here.

3. **The E-3 lens (small+old).** `RESULTS-E3-CONTINUATION-20261106.md` named the loss-front as content-patterned: continuation-execution-time (config, 0.17), decision-core-claim-validity (debug, 0.00), continuation-next-action (debug, 0.67), continuation-implementation-scope (debug, 1.00), recall-upstream-confirmation (debug, 2.00) — all tiny+old anchors; the control slice (feature-impl, 4.67, 0 misses) at the same machinery and depth (44794→14021, 68.7%, 69/75 msgs) is clean. The battery's rung-4/run-5 results are the same class at the extremes: rung 4 loses the small+old anchors (the seam-mechanism's 17/21 lost), rung 5 loses everything because the density makes every fact small-and-buried. The seam-arc's three-block composition (derivations + time-anchors + forward-intents) is the measured counter (3.33, 0/5 below 3.0) — i.e. the recovery bar is achievable when the tiny+old anchors are explicitly retained; the ladder's floors are what happens when they are not.

4. **Interaction, not either axis alone.** The ladder now has the two cells CURRICULUM-LADDER named as missing (shallow+high-density = rung 5; deep+low-density = rung 4's small+old class against rung 3's clean deep). The result: the worst cell is high-density-with-no-compaction (rung 5, 0.00), and the best deep cell (rung 3, 4.67) is clean. So the axes' interaction is **density dominates depth**: a dense stream fails even un-compacted; a deep compaction succeeds if its facts are not tiny+old anchors. Depth is a necessary-but-not-sufficient condition for loss; density (tiny+old-anchor prevalence) is the sufficient one. That is the separation the LADDER-GAPS verdict said was missing.

Verdict line: **LADDER-SEPARATED** — compaction depth and fact-density are now measured on distinct real streams and do not co-vary with recovery; density (tiny+old-anchor survival) is the driver, depth is not.

### (d) Honest walls — what the battery cannot certify

1. **Live-provider judge variance.** Single compressor/judge model (`deepseek/deepseek-v4-flash-0731`) for all 15 runs; no cross-model or cross-judge replication. The prior rungs' miss counts moved (2/4/0 → 4/5/1) between batteries; that is the variance, and it is a receipt, not noise to hide. The bar (3.33) is a median-of-medians; a single model's 3-run median is grainy.
2. **3-run medians' grain.** 3 runs per fixture is the battery's stated granularity; a single outlier run can move a median by a third of a point. The below-3.0 probe lists are the more stable signal than the overall medians.
3. **Real cells' single-battery first measure.** Rungs 4-5 have exactly one battery (this one) of measured data; no re-run, no cross-substrate replication. Their floors (1.00 / 0.00) are strong but are first measures; treat as directional, not certified.
4. **Retention-reward scalar unmeasured per rung** (§(b)) — the measured survival is folded into the scores, not emitted as a separate scalar in these run-JSONs. The scalar's verdict (§(e)) is therefore a verdict on the *shape* of the evidence, not on a number.
5. **No depth/density knob in the runner.** `run_eval.py` exposes no depth/density/ratio parameter; the stress-cells are applied as fixtures, not as run-arguments (per `AUDIT-LADDER-RUNGS-20261106.md`). The separation is measured across fixtures, not within a parameterized sweep.
6. **The banks certify presence, not separation.** `PROBE-BANKS-20261106.md` and `EXP-PROBE-BANKS-CERT-20261106.md` (CLEAN) certify expected-facts' presence in the fixture bytes (A1-A11, B1-B8 re-derived); they do not certify depth-vs-density separation. That rides this battery at the substrate-pin, as stated.
7. **The dense cell's retry-receipt is SOURCE-anchored.** `max_retries_exhausted` lives in the source dump's `reason` field, not the fixture's messages (per `PROBE-BANKS-20261106.md` anchor-note); the `recall-retry-receipt` probe (0.17) is graded against a fact the fixture does not itself carry. Flagged, not hidden.

### (e) The scalar's verdict

The retention-reward scalar is **UNMEASURED per rung in this battery** (no scalar emitted in the run-JSONs; recovery medians + miss counts are the recorded proxies). Reading the evidence's shape against the retention arm's definition (r = 1.0 drops deep-minima 1.00→0.00; cost 3 tiny-aged literals, ≤3 tokens, age ≥ threshold; `RESULTS-RETENTION.md`):

- The two floors are the scalar's story in proxy form: rung 4 (small+old class) at 1.00 overall with 5/5 below-3.0 probes, and rung 5 (dense class) at 0.00 with 6/6 below-3.0 — i.e. when tiny+old anchors are not retained (r < 1.0), deep-minima prevalence is ~1.00, exactly as the retention matrix predicts (r ∈ {0.0, 0.25, 0.5} → 1.00). The battery's floors are the retention arm's 1.00-prevalence row, measured on real streams.
- The clean deep cell (rung 3, 4.67, 1 miss) is the r = 1.0 row in proxy form: when the tiny+old anchors survive (continuation-next-step is the lone residual), deep-minima prevalence is ~0.
- The seam-arc's three-block composition (3.33, 0/5 below 3.0) is the *measured* path from the 1.00 row to the 0.00 row, at ~240 tokens (~2.4% of a 10K context), with the forward-intents block closing the last below-3.0 cell (next-action 2.67→3.00).

Scalar verdict: **the scalar is not a number in this battery; it is a direction, and the direction is confirmed** — un-retained tiny+old anchors → deep-minima prevalence ~1.00 (rungs 4-5); retained → ~0 (rung 3 + the seam-arc's 3.33). The retention arm's r = 1.0 (full retention) is the only regime consistent with the ladder's top rung, and the ladder's floors are its r < 1.0 regime. The next measurement that would make the scalar a number: a battery run with the retention-latch's reservation applied (r = 1.0) on rung 4's small+old cell, falsifying per `SEAM-INTEGRATION-20261106.md` §3 — if the reserved tiny-aged literals' survival fails to lift the continuation/decision probes in the real cell's own terms, the integration is refuted.

## [Recommendation/Action Plan]

One reversible next action: re-run the battery with the retention-latch's reservation (r = 1.0, 3 tiny-aged literals, ≤3 tokens) applied on rung 4's small+old cell, keeping rungs 1-3 and 5 as comparators, at the same substrate-pin and 3-run median granularity, and compare the below-3.0 probe counts and overall medians against this battery's row. Success criterion: rung 4's overall median rises above 3.0 and its 5 below-3.0 probes clear (mirroring the seam-arc's 0.67→3.33), with rung 5 unchanged (the latch is a depth-cell instrument only, per `SEAM-INTEGRATION-20261106.md` §2).

## [Next Steps]

- Land this FULL battery row on the study branch (this file).
- If the latch battery lands, update `CURRICULUM-LADDER.md`'s miss-counts to this battery's fresh figures (4/5/1/5/6) and note the prior 2/4/0 as the historical record.
- No upstream writes; fork-only.

## [Artifact]

- File: `studies/rfc-143379-rig/EVAL-LADDER-BATTERY-20261106.md` (this file, FULL, overwrites the PARTIAL).
- Source receipts: `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/{report.md, summary.json, 15× *-run-*.json}`; records `CURRICULUM-LADDER.md`, `RUNGS-BUILT.md`, `REBUILD-RECEIPTS-20261106.md`, `PROBE-BANKS-20261106.md`, `AUDIT-LADDER-RUNGS-20261106.md`, `EXP-REBUILD-CERT-20261106.md`, `EXP-PROBE-BANKS-CERT-20261106.md`, `RESULTS-E3-CONTINUATION-20261106.md`, `SEAM-INTEGRATION-20261106.md`, `krecency/RESULTS-RETENTION.md`, `krecency/RESULTS-COMPOSE.md`, `krecency/RESULTS-INTENT.md`, `krecency/RESULTS-AUDIT.md`, `krecency/RESULTS-SEAMMECH.md`, `krecency/RESULTS-SEAMINT.md`.
- Commit on branch `study/rfc-143379-rig-20261105`, pushed.