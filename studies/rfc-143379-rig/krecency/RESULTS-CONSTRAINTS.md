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


## THE RE-WALK'S CORRECTION (the contract's no-measurable-improvement pass — supersedes the raw percentage's reading)
The section above's comparison (18/183 = 9.84% vs the field's <0.5%) is scale-confounded. The field's claim is measured against a PRODUCTION-scale compaction context (Constraint Pinning: ~47 pinned tokens in a large context), while the sim's history is 183 word-tokens — the denominator is the confound. The COMPARABLE is the pinned TOKEN COUNT: our analog pins 18 word-tokens (4 standing lines) against the field's ~47 — the same order, actually lighter. Scale-normalized to a 10K-token production context, the analog's pinned share is ~0.18%; at 16K, ~0.11% — it MEETS the field's <0.5% class once the denominators are commensurate. Verification-of-record: the pinned-token count is the measurable; a percentage claims only against its named context size. The anchor's fail-closed pinning costs the same order as Constraint Pinning — not two orders of magnitude more; the raw percentage was the sim's tiny denominator speaking.