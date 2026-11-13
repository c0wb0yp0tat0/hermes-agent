# RESULTS-CROSSINGS — crossings arm (E3)

Verdict: CELL-DEPENDENT. The small+old cell (tiny window x aged demand) sits at
1.00 deep-minima prevalence for every pinning variant (none / literal / literal+membership);
pinning never reaches the 0.15 bar there (delta +0.85 vs 0.15). All other quadrants
(large+recent, large+old, small+recent) sit at 0.00 for every variant.

## Quadrant table (recurrence-rich ground)
| quadrant | none | literal | literal+membership |
|---|---|---|---|
| large+recent | 0.00 | 0.00 | 0.00 |
| small+old | 1.00 | 1.00 | 1.00 |
| large+old | 0.00 | 0.00 | 0.00 |
| small+recent | 0.00 | 0.00 | 0.00 |

## Recurrence-free secondary sweep
Same shape: small+old stays 1.00 across variants; all other cells 0.00. The
portability gap does not introduce new cell-dependence.

## E4-candidacy note
The compaction-front (compression-eval continuation/decision-losses) likely shares
the small+old shape: aged demand beyond a tiny window is unrecoverable regardless of
pinning. One line; no new probes.

CSV: results/crossings.csv
EOF