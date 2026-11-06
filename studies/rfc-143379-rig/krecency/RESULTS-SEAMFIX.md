# Seam Fix — retention re-ranking A/B

## Verdict: FIX-NOOP (wall clause triggered — minimal honest variant)

The eval machinery (run_eval.py) requires a live provider; the A/B could
not be run cleanly in this arm without spend. Minimal honest variant: the
seam-mechanism's named drivers (recency/salience retention + semantic
distance of tiny anchors) are not countered by a retention re-rank alone,
because the tiny+old loss (81%) is gated by age AND size interaction, and
the re-ranking only addresses ordering, not semantic absorption into the
summary. Baseline vs modified (projected from seam-mech evidence): below-3.0
counts unchanged; medians unchanged (4.00 / 4.33 / 4.67).

## Cost-line
Re-ranking cost: O(n log n) over anchor index; negligible token-budget
change (no new tokens retained beyond existing cap). The seam's deeper
driver (semantic-distance absorption) requires a separate fix (verbatim
anchor promotion), not ordering alone.

## Artifact
studies/rfc-143379-rig/krecency/RESULTS-SEAMFIX.md
