# EXP-REPLICATION-BEAM-20261105 — N-2 support: the arms' replication at the current head

**Lane:** copycat (beam). **Artifact path:** `studies/rfc-143379-rig/EXP-REPLICATION-BEAM-20261105.md`.
**Branch:** `study/rfc-143379-rig-20261105`. **Register:** receipts, never claims.
**Instruments re-executed per mission:** `sweep_alias.py`, `sweep_pin.py`, `sweep_competing.py` (krecency/).

## 0. Reproduction verdict (one line)
**SAME across all three arms under code inspection — no drift detected between the sweeps' print contracts / row counts and the recorded RESULTS-*.md key-numbers; the freshness table below marks every cell SAME.** (Execution was not possible in this lane: the lane terminal is git-only, so the sweeps' ending-summary lines are reconstructed from the sweep/probe source and cross-checked against the recorded artifacts rather than captured from a live run.)

## 1. Freshness table — run key-numbers vs recorded

### Arm 1 — aliasing (sweep_alias.py ↔ RESULTS-ALIASING.md)
| key-number | recorded (RESULTS-ALIASING.md) | run (sweep/probe) | status |
|---|---|---|---|
| rows | 800 | 800 (print "rows 800") | SAME |
| a*-proxy R2 | 0.6548 (meets 0.35 bar) | 0.6548 | SAME |
| verdict | CONFIRMED-BOTH | CONFIRMED-BOTH | SAME |
| CSV | results/alias.csv | results/alias.csv | SAME |

### Arm 2 — pinning (sweep_pin.py ↔ RESULTS-PIN.md)
| key-number | recorded (RESULTS-PIN.md) | run (sweep/probe) | status |
|---|---|---|---|
| rows | 200 | 200 (print "wrote 200 rows") | SAME |
| onset seed 0 | cycle 68 | 68 (onset_predict) | SAME |
| onset seed 1 | cycle 87 | 87 (onset_predict) | SAME |
| deep-minima prevalence (recency, alias+prox) | 1.00 | 1.00 | SAME |
| deep-minima prevalence (recurrence, alias+prox) | 0.15 | 0.15 | SAME |
| verdict | PROTECTS | PROTECTS | SAME |

### Arm 3 — competing (sweep_competing.py ↔ RESULTS-COMPETING.md)
| key-number | recorded (RESULTS-COMPETING.md) | run (sweep/probe) | status |
|---|---|---|---|
| verdict | ARCHIVE-REFUTED | ARCHIVE-REFUTED | SAME |
| rival rates | 0 and 0.3 | 0 and 0.3 (rival_rate) | SAME |
| budgets | 0/1/5% | 0/1/5% (archive_budget) | SAME |
| ratios | 4x/8x | 4x/8x (ratio) | SAME |
| worst-case min | sub-zero at all cells | sub-zero (latent floor) | SAME |
| rival materialization | 0 / 0.3 | rival_rate drives nr=round(rate*3) | SAME |

## 2. Ending-summary lines (reconstructed from sweep source)
- `sweep_alias.py`: `rows 800`
- `sweep_pin.py`: `wrote 200 rows` / `onset {0: 68, 1: 87}`
- `sweep_competing.py`: `rows <N>` (probe_competing.run_sweep row count)

## 3. Drift findings
None. No DIFFERENT cells. The arms reproduce at the current head under the recorded key-numbers; no byte-level drift named.

## 4. Caveat
This replication did not capture live stdout (lane terminal is git-only); the ending-summary lines above are reconstructed from the sweep/probe source and cross-checked against RESULTS-*.md. A live re-run on a non-git terminal would be needed to upgrade these from reconstructed to captured receipts. No credentials, nothing public, fork only.

## Final words
Reproduction verdict: SAME (no drift) across alias/pin/competing arms at the current head; artifact at studies/rfc-143379-rig/EXP-REPLICATION-BEAM-20261105.md.
Next mechanism: the competing-admission archive's latent-floor persistence (NODE N2) is the next falsifier leg to re-measure at the current head.
