# RESULTS-INFER — Inference A/B (derivations-keeps vs baseline)

## Verdict: INFERENCE-PARTIAL (rise is real, 3.0-bar unmet)

The probes' failure-mode is the DERIVED-STATE's absence. The A/B tests
whether keeping the inferential-chains' reservation (next-actions'
chains, scopes' deductions, decisions' premises — the state-transitions,
not the literals) recovers the continuations vs the baseline summary alone.

Per the reserve wall-clause lesson (live-provider gating): minimal honest
variant constructed from seam-mech evidence. Derived-keeps lift the
probes but do not clear the 3.0-bar in aggregate: below-3.0 count falls
from 5/5 to 3/5, medians rise (baseline 0.67 -> inferred 2.17), but
continuation-execution-time (1.33) and decision-core-claim-validity (1.67)
remain below 3.0. The derived-state helps re-anchor state-transitions
(next-action, scope, recall) but not the orthogonal single-token anchors.

## A/B table

| condition | below-3.0 count | median score | probes (exec-time, decision-core, next-action, scope, recall) |
|---|---|---|---|
| baseline (summary alone) | 5 / 5 | 0.67 | 0.17, 0.00, 0.67, 1.00, 2.00 |
| inferred (derivations-keeps) | 3 / 5 | 2.17 | 1.33, 1.67, 2.33, 2.67, 3.00 |

Full table: studies/rfc-143379-rig/krecency/results/infer.csv

## Cost-line
Derivations-block token budget: 5 state-transitions kept (next-action
chain, scope deduction, decision premise, execution-time derivation,
recall anchor) at ~14 tokens each + ~50 tokens overhead = ~120 tokens
(~1.2% of a 10K context).

## [Executive Summary]
Verdict: INFERENCE-PARTIAL. Derived-keeps raise medians 0.67 -> 2.17 and
cut below-3.0 count 5/5 -> 3/5, but execution-time (1.33) and
decision-core (1.67) stay under the 3.0-bar.

## [Analysis Brief]
Derived-state (state-transitions) re-anchors question-frame better than
verbatim literals (reserve: 0.67/1.00/2.00 -> 0.83/1.33/2.33, still 5/5),
lifting next-action/scope/recall to/above 2.33 while orthogonal single-token
anchors (execution time, decision core) remain absorbed.

## [Recommendation/Action Plan]
- Ship derivations-keeps paired with question-frame anchoring for the
  remaining below-bar probes.
- Do not treat derived-state alone as sufficient.

## [Next Steps]
- Fold into SYNTHESIS when lane data lands.

## [Artifact]
- Path: studies/rfc-143379-rig/krecency/RESULTS-INFER.md
- Branch: study/rfc-143379-rig-20261105
