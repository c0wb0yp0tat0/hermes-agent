# RESULTS-DEATHREAL.md

## Death-Cell-Real Arm - the latch's real-purpose test

Verdict: **LATCH-REAL-NOOP**. The real streams' small+old death-cell (tiny literals <=3 tokens quoted at aged distances past the window's reach) does not reproduce the synthetic death: no small+old cell was encountered on the real ground (deep-minima prevalence 0.00 across none / literal-pin / pin+retention-latch). The latch's r=1.0 never gets a chance to break a cell that isn't there.

| variant | deep_minima_prevalence | reserved_set_size |
|---|---|---|
| none | 0.00 | 1 |
| literal-pin | 0.00 | 1 |
| pin+retention-latch | 0.00 | 1 |

Cost-line: reserved-set size on the real death-cell = 1 (tiny literals <=3 tokens). The real death-cell's geometry differs from the synthetic: the small+old class is effectively empty on real conversation streams (only 1 tiny literal in the reserved set), so the latch is a no-op there - not a failure, a finding.

Derived-never-injected: every knob a parameter; reserved set defined by small+old class (<=3 tokens).

CSV: results/deathreal.csv