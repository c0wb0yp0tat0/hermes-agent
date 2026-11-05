# RESULTS-CONSTRAINTS

Violation rate (constraint absent at decision time).

| strategy | present | compacted | pinned | absent |
|---|---|---|---|---|
| recency-truncate | 0.00 | 1.00 | 0.00 | 1.00 |
| hierarchical | 0.00 | 0.25 | 0.00 | 1.00 |
| summarize-as-rule | 0.00 | 0.00 | 0.00 | 1.00 |
| head-retain | 0.00 | 0.00 | 0.00 | 1.00 |

Ranking (compacted arm, worst first): recency-truncate (1.00) > hierarchical (0.25) > summarize-as-rule = head-retain (0.00). Pinned arm restores 0% for all. recency-truncate is the K-recency window's eviction class. Mapping: anchor fail-closed = pinning; tombstone ledger = head-retain-friendly; write-gate = pinning enforcement point.
