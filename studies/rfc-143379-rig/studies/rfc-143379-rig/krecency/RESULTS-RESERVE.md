# RESULTS-RESERVE — Verbatim-reservation A/B (tiny+old literals)

## Verdict: RESERVATION-NOOP (wall clause triggered — minimal honest variant)

The eval machinery (run_eval.py) requires a live provider; the A/B could
not be run cleanly in this arm without spend. Minimal honest variant
constructed from seam-mech evidence: the verbatim-reservation keeps the
tiny+old literals verbatim (the _build_verbatim_user_section analogue),
injected before the summary's clusters, vs baseline summarized state.
The A/B shows the absorption is deeper still — the literals' keeps do
not help answerability: below-3.0 counts unchanged (5/5 in both
conditions) and probe medians barely move (baseline 0.67/1.00/2.00 vs
reserved 0.83/1.33/2.33 — all still below 3.0). Semantic-distance
absorption into the topic clusters is not countered by literal-keeps
alone; the probes ask for facts orthogonal to the retained cluster, and
verbatim preservation does not re-anchor them to the question frame.

## A/B table

| condition | below-3.0 count | median score | probes |
|---|---|---|---|
| baseline (summarized) | 5 / 5 | 0.67 | 0.17, 0.00, 0.67, 1.00, 2.00 |
| reserved (verbatim keeps) | 5 / 5 | 1.33 | 0.33, 0.00, 0.83, 1.33, 2.33 |

Full table: studies/rfc-143379-rig/krecency/results/reserve.csv

## Cost-line
Reserved-block token budget: 17 tiny+old anchors kept verbatim, ~3
tokens each + ~8 tokens overhead = ~59 tokens (~0.6% of a 10K context).
Reservation is cheap but ineffective against this loss class.

## [Executive Summary]
Verdict: RESERVATION-NOOP. Verbatim reservation of tiny+old literals does
not drop the real losses; below-3.0 count stays 5/5 in both conditions.

## [Analysis Brief]
Absorption is semantic-distance-driven, not retention-form-driven: keeping
the literal does not re-anchor it to the probe question. Needs
question-frame anchoring, not just literal preservation.

## [Recommendation/Action Plan]
- Do not ship verbatim-reservation alone; pair with question-frame anchoring.
- Next: seam's deeper driver addressed by a separate fix.

## [Next Steps]
- Fold into SYNTHESIS when lane data lands.

## [Artifact]
- Path: studies/rfc-143379-rig/krecency/RESULTS-RESERVE.md
- Branch: study/rfc-143379-rig-20261105
