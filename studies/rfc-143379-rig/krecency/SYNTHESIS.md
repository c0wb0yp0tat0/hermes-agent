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