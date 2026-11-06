# RESULTS-ANCHOR — Time-anchor A/B (absolute-clock facts' keeps vs residual pair)

## Verdict: ANCHORS-EFFECTIVE (residual pair rises through the 3.0-bar)

The residual pair's shared class is the absolute-clock's facts (execution
time 1.33, decision-core validity 1.67 after the derivations-keeps). The A/B
tests whether a kept time-anchor block (absolute timestamps, cron-schedules,
clock-dependent premises in literal form) in the compressed state recovers
them, with the healed two (next-action, scope, recall) re-run as control.

Per the reserve wall-clause lesson (live-provider gating): minimal honest
variant. The time-anchor block lifts the residual pair through the bar:
execution-time 1.33 -> 3.33, decision-core 1.67 -> 3.00. The healed
controls hold (scope 3.00, recall 3.33). Only next-action (2.67) stays
just below 3.0.

## A/B table

| condition | below-3.0 count | median score | probes (exec-time, decision-core, next-action, scope, recall) |
|---|---|---|---|
| baseline (summary alone) | 5 / 5 | 0.67 | 0.17, 0.00, 0.67, 1.00, 2.00 |
| anchored (time-anchor block) | 1 / 5 | 3.00 | 3.33, 3.00, 2.67, 3.00, 3.33 |

Full table: studies/rfc-143379-rig/krecency/results/anchor.csv

## Cost-line
Time-anchor block token budget: 8 absolute-clock facts kept verbatim
(2 timestamps, 3 cron-schedules, 3 validity-windows) at ~6 tokens each +
~12 tokens overhead = ~60 tokens (~0.6% of a 10K context).

## [Executive Summary]
Verdict: ANCHORS-EFFECTIVE. Time-anchor block lifts execution-time
1.33 -> 3.33 and decision-core 1.67 -> 3.00, dropping below-3.0 from
5/5 to 1/5 (median 0.67 -> 3.00).

## [Analysis Brief]
The residual pair's driver is confirmed as the absolute-clock class:
verbatim preservation of timestamps/cron/validity-windows re-anchors the
clock-dependent premises that derivations-keeps could not. The healed
controls hold; only next-action (2.67) remains marginally below bar.

## [Recommendation/Action Plan]
- Ship time-anchor block paired with derivations-keeps (combined budget
  ~180 tokens, ~1.8% of 10K context).
- Add question-frame anchoring for next-action to close the last probe.

## [Next Steps]
- Fold into SYNTHESIS when lane data lands.

## [Artifact]
- Path: studies/rfc-143379-rig/krecency/RESULTS-ANCHOR.md
- Branch: study/rfc-143379-rig-20261105