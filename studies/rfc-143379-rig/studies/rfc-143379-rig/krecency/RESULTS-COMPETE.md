# RESULTS-COMPETE.md

## Verdict: NOT-CONFIRMED

The re-labeling of the deep sub-zero excursions as the field's COMPETITION class is **not** confirmed by this instrument arm under the implemented rival-collision model. At rival-rate 0% the deep-low prevalence does not vanish (0.447), so the "noise floor" is not solely the conflict class; the floor term (latent survival) itself produces the lows. At 10%/30% prevalence scales (0.469 / 0.677) — partial scaling, but the baseline does not vanish. The a*-proxy R2 vs per-trial score is ~0 (0.00-0.002), not the field's 0.35-0.58 shape; the softmax-over-pool proxy as implemented does not track per-trial failure. Honest NOT-CONFIRMED is a finding: the excursion class may be a mixture, or the proxy/mechanism needs revision.

## Rate table (deep-low fraction, score<0.15)

| rival_rate | deep-low frac | R2(a*,score) |
|------------|---------------|--------------|
| 0%         | 0.4467        | 0.000        |
| 10%        | 0.4687        | 0.002        |
| 30%        | 0.6766        | 0.000        |

## Artifacts

- probe_compete.py
- sweep_compete.py
- results/compete.csv
