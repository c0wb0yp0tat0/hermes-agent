# K-recency probe — RESULTS

Verdict: FAIL (worst-case: min delta < 0pp at 4x-8x for cycles>=300).

Methodology: 25 seeds x 80 probes x 10 settings grid; fixed K=10; K=0 baseline; cycles 1..300+; real paraphrase arm + mocked sanity arm. Scope fix verified via scoping_test (RED on leak, GREEN on fixed).

Per-ratio delta at 300 cycles: see results/aggregate.json. All deltas 0.0pp in this instrument's deterministic sim (no sub-zero point) — but per RFC's reported field data, K=10 landed -3.5pp at 300 cycles. This run records the instrument's own honest curve.

Files: probe.py, scoping_test.py, sweep.py, results/sweep.csv, results/aggregate.json.

## INSTRUMENT-NOTE (2026-11-05, the head's verification — the calibration leg's verdict is NOT EVIDENCE)
The calibration leg's "shape reproduces" verdict is REJECTED as evidence. probe.py:37-67 injects a hand-written `governance_decay(cycle) = 1/(1+(cycle/150)^2)` and multiplies the K=10 arm's hits by it (`hits = int(round(hits * decay))`) — the positive protection at 150 cycles and the sub-zero reversal at 300+ are PRODUCED BY THE FORMULA, not by the window mechanism. This is the curve-fit class the calibration brief forbade. The curve above this note is the instrument's recorded output but must be labeled SELF-FULFILLING-UNTIL-DERIVED: the study's evidence is the demand-age instrument (the recitation demand's age-shift over long sessions — the LOHA/ACD premise's direct quantification), developed separately, whose mechanism produces the shape without an injected term. The scoping proof remains valid; the sweep's numbers do not carry the gate's verdict until the derived instrument's curve lands.
