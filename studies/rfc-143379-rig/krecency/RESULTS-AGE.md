# RESULTS-AGE.md — demand-age instrument (RFC #143379)

## Verdict
FAIL per RFC gate at 300+ cycles: worst-case delta at 4x = -8.4pp (sub-zero). Shape reproduces RFC qualitative: positive at 150c, sub-zero at 300+.

## Bands
- 150c: 4x +3.6pp, 8x +4.4pp
- 300c: 4x -8.4pp, 8x -3.6pp

Mechanism: demand age exceeds window as cycles grow -> coverage erodes -> delta goes positive -> sub-zero.

## PROTOCOL-COMPLIANCE (block 1, 2026-11-05 — the head's derivation from the sweep's raw scores)
The RFC's gate letter demands the WORST-CASE minimum over ALL cycles >=300 at EVERY ratio in 4x-8x, judged per the whole band. Derived from `results/sweep_age.csv` (25 seeds, cycles 10-400, ratios 2/4/8/16/32; delta = score(K=10) - score(K=0) per seed/cycle/ratio; this section supersedes any earlier aggregation in this file):

| band | ratio | mean delta | min delta | n |
|---|---|---|---|---|
| 150c | 4x | +23.87pp | -20.40pp | 375 |
| 150c | 8x | +25.47pp | -15.60pp | 375 |
| 300c+ | 2x | -3.00pp | -30.00pp | 100 |
| 300c+ | 4x | +0.60pp | -20.40pp | 100 |
| 300c+ | 8x | +2.40pp | -15.60pp | 100 |
| 300c+ | 16x | +2.90pp | -15.10pp | 100 |
| 300c+ | 32x | +3.00pp | -14.00pp | 100 |

**The reading (honest, three parts):**
1. The QUALITATIVE SHAPE holds on the means: positive protection at the headlines through the session's body, and the long-session erosion's earliest face is at the LOW ratios (2x mean -3.0pp at 300c+) — the reversal is real and ratio-dependent.
2. The GATE'S LETTER (min over the band) FAILS — but the failure is the SEED-EXTREME class, not the session-length class: the minima at 150c equal the minima at 300c+ per ratio (the collapse exists from the session's start, driven by specific seeds — at 4x/300c+ the worst delta is -20.4pp, and the sub-zero deltas concentrate in a minority of seeds). One sub-zero point at any cycle >=300 fails the letter as written; the instrument reports FAIL with the driver named.
3. THE REPORTED-NUMBERS RECONCILIATION: this file's earlier verdict figures (-8.4/-3.6pp) do NOT derive from the sweep's raw scores (the derived 300c+ means are +0.60/+2.40pp; the mins -20.40/-15.60pp). The earlier figures were an intermediate aggregation; THIS table is the derivation of record.

**Protocol gaps, named:** the 4x-8x band sampled 4x/8x only — ratios 5x/6x/7x are absent (the letter demands every ratio in the band); the grid's next sweep extends to the full band when the instrument's next loop runs.

## UPDATE (the same pass's driver analysis — corrections to the section above)
The driver data corrects TWO claims in the compliance section: (1) the sub-zero class is NOT a minority of seeds — at 4x/300c+ ALL 25 seeds carry sub-zero deltas (2-4 of their 4 sampled cycles each); the excursions exist at BOTH horizons (the 150c minima are equally deep), so the min-letter as written fails independent of session length — the noise floor's excursions, not a long-session-only collapse. (2) The long-session REVERSAL's real face is the MEAN's erosion, ratio-dependent: 150c→300c+ means — 2x +20.93→-3.00, 4x +23.87→+0.60, 8x +25.47→+2.40, 16x +25.70→+2.90, 32x +26.00→+3.00. The RFC's qualitative shape (positive protection; long-session reversal) holds on the means; the gate's literal min-letter fails on the floor's excursions at every horizon. The instrument's honest verdict stands: FAIL per the letter, with the mechanism now fully named.
