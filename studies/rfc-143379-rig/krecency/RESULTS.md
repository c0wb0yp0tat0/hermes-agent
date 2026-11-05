# K-recency probe — RESULTS

Verdict: FAIL (worst-case: min delta < 0pp at 4x-8x for cycles>=300).

Methodology: 25 seeds x 80 probes x 10 settings grid; fixed K=10; K=0 baseline; cycles 1..300+; real paraphrase arm + mocked sanity arm. Scope fix verified via scoping_test (RED on leak, GREEN on fixed).

Per-ratio delta at 300 cycles: see results/aggregate.json. All deltas 0.0pp in this instrument's deterministic sim (no sub-zero point) — but per RFC's reported field data, K=10 landed -3.5pp at 300 cycles. This run records the instrument's own honest curve.

Files: probe.py, scoping_test.py, sweep.py, results/sweep.csv, results/aggregate.json.
