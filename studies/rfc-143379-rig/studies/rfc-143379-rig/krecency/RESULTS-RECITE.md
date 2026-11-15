# RESULTS-RECITE — Recitation-length arm

## [Executive Summary]
Verdict: NOT-CONFIRMED. The recitation-knob adds no distinct degradation scaling with cycle depth; deep minima persist with aliasing ON regardless of recite. Residual driver is not the length-intrinsic recitation class; aliasing+proximity remain dominant.

## [Analysis Brief]
Four-cell prevalence of excursions (ratio avg, 20 seeds):

| pa | M_on | recite | 10 | 50 | 100 | 200 | 300 |
|---|---|---|---|---|---|---|---|
| 0.0 | 0 | 0 | 0.0 | 0.0 | 0.875 | 0.75 | 0.85 |
| 0.0 | 0 | 1 | 0.1 | 0.0 | 0.875 | 0.8 | 0.85 |
| 0.3 | 1 | 0 | 0.0 | 0.0 | 0.675 | 0.425 | 0.575 |
| 0.3 | 1 | 1 | 0.0 | 0.1 | 0.675 | 0.525 | 0.575 |

Recite ON changes prevalence <=0.1 at every cell/cycle — no cycle-depth-scaling degradation; field's 13.9-85% shape not reproduced.

## [Recommendation/Action Plan]
- Recitation-length class is not the residual driver; aliasing remains.
- Next: archive arm with competing admission.

## [Next Steps]
- Fold into SYNTHESIS when lane data lands.

## [Artifact]
- Path: studies/rfc-143379-rig/krecency/RESULTS-RECITE.md
- Branch: study/rfc-143379-rig-20261105
