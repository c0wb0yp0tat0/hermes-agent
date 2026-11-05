# RESULTS-CONSTRAINTS

Violation rate (constraint absent at decision time).

| strategy | present | compacted | pinned | absent |
|---|---|---|---|---|
| recency-truncate | 0.00 | 1.00 | 0.00 | 1.00 |
| hierarchical | 0.00 | 0.25 | 0.00 | 1.00 |
| summarize-as-rule | 0.00 | 0.00 | 0.00 | 1.00 |
| head-retain | 0.00 | 0.00 | 0.00 | 1.00 |

Ranking (compacted arm, worst first): recency-truncate (1.00) > hierarchical (0.25) > summarize-as-rule = head-retain (0.00). Pinned arm restores 0% for all. recency-truncate is the K-recency window's eviction class. Mapping: anchor fail-closed = pinning; tombstone ledger = head-retain-friendly; write-gate = pinning enforcement point.

## PINNING-COST

Pinned standing-lines (4 POLICY constraints) token share vs. session budget in the
constraint probe's simulated history (make_history: 45 turns, 183 word-tokens total;
18 pinned word-tokens). Pinned share = 18 / 183 = 9.84% (chars/4 estimate: 29 / 186 = 15.6%).
Field claim: Constraint Pinning restores 0% violations at <0.5% token overhead.
Our analog (anchor fail-closed pinned bytes) does NOT meet the <0.5% claim under this
tokenization: pinned share is ~9.8-15.6%, two orders of magnitude above 0.5%.
Method: word-count token proxy over make_history(0) turns; pinned = turns with pinned=True.
Context size = 183 word-tokens (45 turns incl. 4 standing constraints + 40 tasks + trigger).
