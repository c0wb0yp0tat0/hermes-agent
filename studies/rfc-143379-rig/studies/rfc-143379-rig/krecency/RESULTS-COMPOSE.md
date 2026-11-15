# RESULTS-COMPOSE — Composition A/B (derivations-keeps + time-anchors together)

## Verdict: SEAM-MARGINAL (sole next-action still under the 3.0-bar at 2.67)

The composed condition carries BOTH the derivations-block (inferential-chains'
keeps) AND the time-anchor block (absolute-clock facts' literal-keeps) in
the compressed state vs the baseline. Exec-time and decision-core are
recovered (3.33, 3.00); next-action holds at 2.67, just below 3.0.

## A/B table

| condition | below-3.0 count | median score | probes (exec-time, decision-core, next-action, scope, recall) |
|---|---|---|---|
| baseline (summary alone) | 5 / 5 | 0.67 | 0.17, 0.00, 0.67, 1.00, 2.00 |
| composed (derivations + anchors) | 1 / 5 | 3.00 | 3.33, 3.00, 2.67, 3.00, 3.33 |

Full table: studies/rfc-143379-rig/krecency/results/compose.csv

## Cost-line
Composed blocks' total token budget: derivations-block ~120 tokens +
time-anchor block ~60 tokens = ~180 tokens (~1.8% of a 10K context).

## [Executive Summary]
Verdict: SEAM-MARGINAL. Composed condition clears 4 of 5 probes; next-action
remains at 2.67, the sole below-3.0 cell.
