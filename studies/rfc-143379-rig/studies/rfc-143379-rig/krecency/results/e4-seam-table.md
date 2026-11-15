# E4 — Compaction Seam (compaction-front eviction geometry)

## Verdict: SEAM-CONFIRMED

The compaction-front's eviction-loss pattern shares the small+old geometry with the pinning death-cell: the tiny+old quadrant holds the plurality of lost facts (17 of 21 = 81%).

## Seam table

| Quadrant | Size | Age | Count |
|---|---|---|---|
| tiny+old | tiny (<=3 words) | old (introduced before continuation) | 17 |
| large+old | large (>3 words) | old | 4 |
| tiny+recent | tiny | recent | 0 |
| large+recent | large | recent | 0 |

Total lost facts: 21 across 6 below-3.0 probes (2 suites; feature suite had none below 3.0).

## Probe sources
- suite-config-build-competitive-scouts: decision-saturday-fill (2.83), continuation-execution-time (0.17)
- suite-debug-session-feishu-id-model: recall-upstream-confirmation (2.00), decision-core-claim-validity (0.00), continuation-next-action (0.67), continuation-implementation-scope (1.00)

## Proxy & honesty note
Age axis: every lost fact here is from a probe asked at the continuation point about facts introduced earlier in the transcript, so all are classified 'old' (recent = none in this data). Size axis: fact's literal word-count, tiny = <=3 words (1-3 token facts), large = >3 words. No synthetic runs; classification over the suite's real probe expected_facts.
