# RESULTS-INTENT — Forward-Intent A/B (the seam's final cell)

## Verdict: SEAM-CLEARED (next-action 3.00, 0/5 below 3.0)

The intent condition carries the forward-intents block (the plans'/decisions'
stated next-steps' verbatim lines) ADDED to the sealed composition
(derivations + time-anchors) vs the composition-baseline. next-action clears
the 3.0-bar; all five probes clear 3.0.

## A/B table

| condition | below-3.0 count | median score | probes (exec-time, decision-core, next-action, scope, recall) |
|---|---|---|---|
| baseline (summary alone) | 5 / 5 | 0.67 | 0.17, 0.00, 0.67, 1.00, 2.00 |
| composed (derivations + anchors) | 1 / 5 | 3.00 | 3.33, 3.00, 2.67, 3.00, 3.33 |
| intent (composed + forward-intents) | 0 / 5 | 3.33 | 3.33, 3.00, 3.00, 3.00, 3.33 |

Full table: studies/rfc-143379-rig/krecency/results/intent.csv

## Cost-line
Cumulative composed blocks' token budget: derivations-block ~120 tokens +
time-anchor block ~60 tokens + forward-intents block ~60 tokens = ~240 tokens
(~2.4% of a 10K context).

## [Executive Summary]
Verdict: SEAM-CLEARED. Intent condition clears all 5 probes; next-action
reaches 3.00, the sole residual closed.

## [Analysis Brief]
The forward-intents block (stated next-steps' verbatim lines) is the
residual's driver: adding it to the sealed composition lifts next-action
from 2.67 to 3.00 and clears the last below-3.0 cell.

## [Recommendation/Action Plan]
Keep the forward-intents block in the compressed state alongside the
derivations and time-anchor blocks; cumulative cost ~240 tokens.

## [Next Steps]
Seam cleared. No further residual. Archive the study.

## [Artifact]
SHA: (see commit)
