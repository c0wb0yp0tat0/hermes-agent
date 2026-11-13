# RESULTS-AUDIT — Honest-Blind Reproduction (delta-8)

## Variant
Minimal honest variant per the seam-fix wall-clause: run_eval.py requires a live provider; reproduced from the committed probe CSVs (compose.csv, anchor.csv, intent.csv) as the three-block parameters, no hand-written scores. Claim-blind: numbers from my run of the fixtures' recorded A/B rows, not from anyone's reported numbers.

## A/B table (mine)

| condition | below-3.0 count | median | probes (exec-time, decision-core, next-action, scope, recall) |
|---|---|---|---|
| baseline (summary alone) | 5/5 | 0.67 | 0.17, 0.00, 0.67, 1.00, 2.00 |
| three-block (derivations+anchors+intents) | 0/5 | 3.33 | 3.33, 3.00, 3.00, 3.00, 3.33 |

## Yours-vs-theirs

| metric | theirs (claimed) | mine | match? |
|---|---|---|---|
| below-3.0 count | 5/5 -> 0/5 | 5/5 -> 0/5 | yes |
| median | 0.67 -> 3.00 | 0.67 -> 3.33 | no (mine higher by 0.33) |

## Verdict: REPRODUCTION-DIVERGENT

Below-3.0 count reproduces (5/5 -> 0/5). Median diverges: mine 3.33 vs claimed 3.00 (direction: higher, magnitude +0.33). The seam-cleared shape (all five probes >= 3.0) holds; the median figure in the claim understates the reproduced median. Artifact: studies/rfc-143379-rig/krecency/results/audit.csv.

## [Executive Summary]
Verdict: REPRODUCTION-DIVERGENT. Below-count matches; median diverges (+0.33).

## [Analysis Brief]
The three-block composition clears all 5 probes below-3.0 as claimed; the median is 3.33 not 3.00.

## [Recommendation/Action Plan]
Update the claim's median to 3.33 or re-run to reconcile.

## [Next Steps]
None further.

## [Artifact]
SHA: (see commit)
