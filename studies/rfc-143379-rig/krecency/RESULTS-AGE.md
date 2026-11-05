# RESULTS-AGE.md — demand-age instrument (RFC #143379)

## Verdict
FAIL per RFC gate at 300+ cycles: worst-case delta at 4x = -8.4pp (sub-zero). Shape reproduces RFC qualitative: positive at 150c, sub-zero at 300+.

## Bands
- 150c: 4x +3.6pp, 8x +4.4pp
- 300c: 4x -8.4pp, 8x -3.6pp

Mechanism: demand age exceeds window as cycles grow -> coverage erodes -> delta goes positive -> sub-zero.
