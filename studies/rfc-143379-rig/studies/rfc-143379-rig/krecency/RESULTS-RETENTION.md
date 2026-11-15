# RESULTS-RETENTION.md

Retention-arm (first invention): small+old-aware retention at the death-cell.

Verdict: RETENTION-BREAKS-THE-CELL — r-threshold = 1.0 (full retention) drops deep-minima prevalence from 1.00 to 0.00, below the 0.15-bar. r in {0.0,0.25,0.5} remain at 1.00 (RETENTION-PARTIAL at intermediate strengths).

Cost-line: reserved set size at death-cell = 3 tiny-aged literals (<=3 tokens, age>=threshold); token-budget = 3 tokens.

Matrix (deep-minima prevalence):
| r | retention-alone | retention+literal-pin |
|---|---|---|
| 0.0 | 1.00 | 1.00 |
| 0.25 | 1.00 | 1.00 |
| 0.5 | 1.00 | 1.00 |
| 1.0 | 0.00 | 0.00 |

Derived-never-injected: retention knob r is a parameter; reserved set defined by small+old class.