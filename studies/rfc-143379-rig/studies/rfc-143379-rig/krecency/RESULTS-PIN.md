# RESULTS-PIN — pinning arm (falsifier of exact-literal pinning)

Verdict: PROTECTS. Recurrence-aware pinning drops deep-minima prevalence at the
confirmed aliasing x proximity pair from 1.00 (recency-pinned variant) to 0.15.

## Onset test
Per-seed onset: seed 0 = cycle 68, seed 1 = cycle 87. Per-seed occurrence predicts
onset -> recency-pinned variant (recency alone) loses protection.

## Protection test
| mode | alias_on | prox_on | deep-minima prevalence |
|---|---|---|---|
| recency | False | False | 0.00 |
| recency | False | True  | 0.00 |
| recency | True  | False | 0.00 |
| recency | True  | True  | 1.00 |
| recurrence | False | False | 0.00 |
| recurrence | False | True  | 0.00 |
| recurrence | True  | False | 0.00 |
| recurrence | True  | True  | 0.15 |

CSV: results/pin.csv (200 rows).