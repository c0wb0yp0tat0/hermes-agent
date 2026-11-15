# RESULTS-FORMATPIN — format-aware pinning arm (V3)

Verdict: FORMAT-AWARE-NOOP (format-pin adds nothing beyond exact-literal pinning at the alias+proximity-ON cell).

## Triple cell (alias_on=True, prox_on=True)
| pin_mode | deep_minima_prevalence | pin_tokens |
|---|---|---|
| none | 1.00 | 0 |
| literal | 0.15 | 18 |
| format | 0.15 | 24 |

## Cost line
- literal pin: 18 tokens (~0.18% at 10K context).
- format-aware pin: 24 tokens (18 + 6 mask) (~0.24% at 10K context).
- Delta: +6 tokens for zero prevalence gain.

## Verdict
FORMAT-AWARE-NOOP. Exact-byte pinning already caps the alias+proximity residual at 0.15; adding a format-signature mask (24 vs 18 tokens) does not move prevalence below 0.15. The aliasing arm's residual is byte-level, not format-class. Cost side breaks too: +6 tokens buys nothing. Receipts: probe_formatpin.py, sweep_formatpin.py, results/formatpin.csv.