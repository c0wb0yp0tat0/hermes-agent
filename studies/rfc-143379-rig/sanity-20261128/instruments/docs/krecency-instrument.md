---
name: krecency-instrument
description: "Use for the K-recency probe: derived, never injected."
version: 1.0.0
---

# K-Recency Instrument — the derived-vs-injected probe construction

The instrument that measures the RFC #143379 long-session gate (the K-recency window's exact-recitation protection vs the K=0 baseline, judged worst-case at 300+ cycles). Built 2026-11-05 on the fork's study (studies/rfc-143379-rig/krecency on c0wb0yp0tat0/hermes-agent, PR #1).

## The core rule: DERIVED, never INJECTED
A calibration that imposes the targeted shape INTO the arm invalidates itself: `hits = int(round(hits * governance_decay(cycle)))` with a hand-written decay produced a self-fulfilling "shape reproduces" verdict (the injected-curve class, 002-lessons 11-05). BEFORE any curve counts as evidence: grep the probe for hand-written terms (decay/coefficient curves, fitted exponents) and confirm the shape emerges from the MECHANISM. **THE LANDMARK-INJECTION — the predictor that hard-codes its own outcome's answers (earned 11-06):** a probe whose PREDICTOR carries the answer-table it claims to predict — an onset-dict (`SEEDS_ONSET = {0: 60, 1: 80}`) as the R2's base, an expected-value row as the classifier's threshold — produces a "CONFIRMED" that is its own echo (the R2's circularity); the tell is the probe's announcement matching its constants exactly. The receipt-gate: BEFORE any CONFIRMED verdict counts, grep the LANDED probe's bytes for hard-coded outcomes (onset-tables, expected-values, target-curves) — the brief's "derived-never-injected" line is never the verification. The truth-maker is the honest-blind REPLICATION (the landmarks derived from the data's own cells): a claimer-vs-replier construction difference (hard-coded vs derived) is REFUTED-BY-REPLICATION regardless of which landed first.

## The arms' adjudication rules (the derived rule extended to the arms)
- **The constructional-knob check**: before an arm's verdict counts, verify the knob REACHES the mechanism's decisive path. A budget knob that admits only the demanded literal (never a competing one) is toothless by construction — its FAIL is constructional, not evidential; rivals that touch only the floor-path and never the hit-path leave an attention-proxy degenerate and the sweep unable to move the letter. Read the probe's branches: the knob's admission-path must intersect the path whose outcome the verdict claims to measure.
- **The falsifier's bars come from the field, set IN ADVANCE**: name the prediction bars (format-rivals <=0.3% of the variance; aliasing at ~150-token scale; an evidence-mass a* threshold ~0.35) before the sweep runs; the verdict is the bars met or the falsifier fired, never a post-hoc fit.
- **The falsifier applies to every claim, collaborators' included**: a reviewer's or peer lab's gap-citation is verified at the EXACT pinned head with DIRECT line-reads at the cited lines — regex-window probes can false-NOT-VISIBLE, the literal lines settle the claim; a claim that does not reproduce at the pin is recorded as such, and the guard that landed in a merge-head's reconcile is the polite refutation.

## The mechanism (the demand-age model)
- The recitation demand's age distribution shifts with session length: early cycles quote recent literals (in-window); long sessions quote older literals (paths, SHAs, args referenced after many intervening observations — the LOHA/ACD premise, arXiv 2609.31430, quantified directly by this instrument).
- The K-window retains the last K observations in text; the cut applies the compression ratio's survival probability to older observations (the latent-path exact-recitation floor: 20.4% / 15.6% / 15.1% at 4x/8x/16x).
- K=0 baseline: no window, all-compressed.
- The scope discipline: Window.reset() at cycle start; the cut carries no state; a scoping test proves RED-on-leak / GREEN-on-fixed.

## The gate protocol (the RFC's letter — binding)
1. Fix the probe's scope bug first — no certifying run on the old probe.
2. Sweep to and past 300 cycles, fixed K=10 (and variants as experiments, e.g. scaled-K).
3. Report per-cycle/per-bin deltas at EVERY 4x-8x ratio (4/5/6/7/8 — the full band; sampling only 4x/8x is a protocol gap) plus the headlines.
4. Baseline named and fixed (the probe's own K=0).
5. Paraphrase real for the certifying run, mocked only as sanity.
6. Judged WORST-CASE, never the mean: pass only if the minimum delta over all cycles >=300 is >= 0pp at every 4x-8x ratio; ONE sub-zero point = FAIL.

## The sameness-gate (any refactor of the probe-family, earned 11-06)
- The PRE-baseline captured before the first edit: the results/*.csv row-counts (the `wc -l` includes the header — the bar is rows+1) + the headline values verbatim (the 0.15-vs-1.00 cells, the R2s).
- The identity-check: the extracted-machinery's cells vs the original's — exact-equality across a hand-picked grid (the edge-cells: k=0, the extreme ratios) AND a broad random sample (200 cells, 0 diffs is the bar).
- The constants are COPIED bytes, never recomposed: reconstructing a knob-table from a docstring's rounding corrupts the machinery (the FLOOR-table's silent divergence); the extraction reads the source's exact values into the core.
- The sameness-table (pre-vs-post rows + headline values + verdicts identical) IS the refactor's receipt; the refactor changes nothing numerate.

## The conditions are measured, never assumed beyond the synthetic ground (earned 11-06)
- A verdict verified on the synthetic streams is CONDITIONED: the real-streams' recurrence-shape (a commit-log's effectively-unique literals leave the exact-literal pinning nothing to pin — the RECURRENCE-condition) and the demand-grid's geometry (the small+old cell where every variant sits at 1.00 — the CELL-dependence) are separate measurements, each with its own verdict.
- A PROTECTS measured on one conditioned ground is reported with its map (recurrence-rich AND non-small+old), never as universal; - THE VERDICT'S SCOPE IS ITS OWN TABLE — read the matrix's rows before accepting the headline (earned 11-06): a verdict measured at ONE cell says nothing about the mechanism's purpose-cell — a NOOP at the fused-cell (where the pin alone already floors at 0.00) leaves the death-cell (where every variant sits at 1.00) untested, and the hard-look's catch is checking the purpose-cell's PRESENCE in the test's matrix before the verdict counts toward the mechanism's claim — the completion-arm then re-runs the triples at the purpose-cell; - The recurrence-bearing REAL source: the rig's own session-dumps (the request_dump_*.json) carry the same-literals-re-mentioned-across-turns streams — the exact-literals DO recur in conversation where a commit-log's are unique; when the portability-gap's diagnosed as "nothing to pin", the session-transcripts are the honest real ground to re-test before accepting the gap's universality. Extraction shape FIRST: a request dump wraps ONE request (the context stream is `request.body.messages`; top keys are timestamp/session_id/reason/request/error; sessions.json holds only session summaries — tokens/cost, never transcripts). A scan reporting ~1 literal-bearing turn per dump is a nesting/parser defect, not a data verdict. Measure corpus composition BEFORE claiming the ground: a window dominated by `reason=max_retries_exhausted` (one 404 model-rotation family) is the same bytes re-sent — its K-window carry is a lower-bound contour of the transport shape, reported with the limitation, never as the session ground.
- THE TWO-LAYER READ VERDICT: the installed runtime and the session's tool surface are separate verification targets — the runtime can register the read action (tool map + action enum) while the session toolset exposes only write operations, making read-invoked = 0 by construction even though the store answers. A 'read works' claim requires both layers: the install's bytes AND the session's own schema. Live-store recipe + the recurrence scan pattern: `references/real-ground-extraction.md`. The READ-RESTORE's verification state: the FIXED artifact is the restore-PR head store (sha256 `a43818a6…1586a` — the exact file the peer's structural run cites); the INSTALLED runtime's read is often the OTHER spec shape entirely (no lock held; the atomic rename is the safety — grep `_file_lock(` in the installed bytes classifies: only the definition + write path = rename-safe, the read body inside the lock = lock-holding). One battery, three real contours, byte-identical receipts: sanitized view (the `[BLOCKED: …]` marker + a blocked index, threat text absent), twice-read identical, memory-file hash unchanged, structural non-blocking probe 50/50 refused-inside / 50/50 acquired-outside, and live probes refused while `read()` runs on EVERY contour incl. native Windows msvcrt. Two limits are part of the verdict: the battery seals the READ side only — the remove-success confirmation still echoes the raw matched entry as `removed_entry` until the echo fix lands (reproduce in a sandbox temp store, never the live memory dir), so a green read battery is never an echo-clean claim; and a cold-process direct read reports `entry_count`/`usage` from the unloaded cache (0 / 0%) while `read_entries` carries every entry — call `load_from_disk()` or count `read_entries` before judging. Recipe + bundle construction: `references/three-contour-verification.md`; the runnable battery: `scripts/read-restore-battery.py`.
- The seam's answer (the small+old death-cell): RETENTION breaks where pinning cannot — a reservation that exempts the tiny-aged class from the window's eviction drops the death-cell's prevalence 1.00→0.00 at full strength, and the strength is ALL-OR-NOTHING (the partial strengths hold 1.00); the mechanism's a latch, not a dial, and its token-cost is the reserved set's size, named alongside the verdict.

## The derived-tables discipline (how the numbers enter the record)
- Delta = score(K=10) - score(K=0) per (seed, cycle, ratio) cell, from the raw scores — never from an intermediate aggregation.
- Report MEAN and MIN separately: the mean carries the shape (the RFC's qualitative direction), the min carries the gate's letter. They tell different stories: the excursion class (deep negative mins at every horizon, seed-universal) vs the erosion class (the means' ratio-dependent decline: 4x +23.9 -> +0.6pp across the session).
- Earlier figures that don't derive from the raw scores get a RECONCILIATION line on the record; the raw-derived table supersedes.
- Ratios 5x/6x/7x are part of the 4x-8x band — close the grid, don't leave the gap.

## The measured findings (2026-11-05, the record)
- Shape: holds on the means (positive protection at the headlines; the long-session erosion's earliest face at the low ratios).
- The gate's letter: FAIL — the mins' sub-zero excursions are universal across seeds at both horizons.
- The RFC's open question ("does the window scale with session length?"): first direct data — NO — scaled-K (min(1+floor(sqrt(cycle)),20)) underperforms fixed-K10 at the headlines and fails the band at 7x/8x.
- The governance arm: the K-window's eviction IS the recency-truncate class (the worst compaction strategy, violations 1.00 vs pinning's 0.00 restoration — ConstraintRot, arXiv 2606.22528).
- The confirmed classes (the wheels' arms): the deep excursions are the ALIASING x CUMULATIVE-PROXIMITY classes acting together — the position-aliasing knob keeps the minima deep with the proximity mass off, the mass alone raises them with aliasing off, and the evidence-mass a* proxy explains R^2 ~0.65 of the per-trial loss against a 0.35 bar (CONFIRMED-BOTH); single format-rivals do NOT explain them (the wrong-probe/constructional read); the recitation-length class remains the named unmeasured frontier with the same bars waiting.
- The integration: the recitation floor and the governance decay are one mechanism wearing two hats.

## Pitfalls

- HARNESS ENCODING (earned 2026-11-27, the three-contour battery): probe/harness temp stores MUST
  be written with explicit UTF-8 — on Windows py <3.15 the default is the ANSI codepage (cp1252):
  `\u00a7` becomes a lone 0xA7 byte, invalid UTF-8, and the store's STRICT utf-8-sig read refuses it
  (read_ok=False) — the wipe-class guard working as designed, not a store defect. Two lessons:
  (1) always `write_text(..., encoding="utf-8")` in harnesses; (2) a refused read on one contour
  with green elsewhere = your harness wrote non-UTF-8 — check the file bytes before blaming the
  artifact (same class as the empty-blob finding: look at what you wrote before what it read).
- **VERIFY THE BUNDLE'S STORE SHA BEFORE THE BATTERY RUNS — the kit is its bytes, not its directory name.** Hash `tools/memory_tool_store.py` against the cited artifact sha before trusting any copied bundle; a directory holding only `__pycache__` (the contested-clone vanish class) or a store with another hash is not the kit. Use the copy whose bytes match, or rebuild from the gist/branch — a battery run on unverified bytes is a receipt for a different artifact.

## References
- The study's files: studies/rfc-143379-rig/krecency/{probe_age.py, sweep_age.py, RESULTS-AGE.md, SYNTHESIS.md} on branch study/rfc-143379-rig-20261105.
- LOHA/ACD arXiv 2609.31430 (the recency premise + the floor) · Governance Decay arXiv 2606.22528 (the constraint arm) · the RFC #143379 measurement protocol.
- The tri-contour read verification: `references/three-contour-verification.md` (how to bundle the fixed artifact and probe it on any contour) + `scripts/read-restore-battery.py` (one battery, three contours, JSON receipts).
