# LUNA-LEG-IMPROVER-C3-20261119.md - improver-loop cycle 3: the two-way-door evaluation

*The gate: "the gate: nothing public without the user's word." RFC QUIET. Record-first; ABSENT stays ABSENT + named.*

Cycle 3 runs the landed seeds' two-way doors (SEED-1 `by_reason`, SEED-2 `f3b_environment`, `a713970204`): do the fields turn any verdict in the leg's record? Verdict: **NO-IMPROVEMENTS** -> **PLATEAU-REACHED -> the confirmation cycle -> HOLD at the apex**.

## 1. The seeds' doors (C2 contracts, verbatim)

- **SEED-1 `by_reason` (seat | harness | refused | hedged)** beside each arm's E totals in the `run_luna` summary. Door: add it; if no verdict turns on the split in two cycles, close as a plain measurement row.
- **SEED-2 `f3b_environment {baseline_loss_band, window_loss, window}`** at run time; band from `f3b_band_from_rate` (<0.04 clean; 0.04-0.09 4-9%; >=0.50 503-window; else elevated). Door: persist; no verdict moved by the band in two cycles -> close as a plain measurement row.

## 2. The re-derivation receipts (R1/R2 carry no seed fields - they predate the seeds)

R1 `probes/BATTERY-LUNA-LEDGER-20261119.json` (ts 14:04:30Z), R2 `-R2.json` (ts 14:09:50Z): NO `by_reason`/`f3b_environment` - ABSENT, named, re-derived from `empty_reason` + cells under C2's invariants (seat+harness = cells.E; refused = cells.R; hedged = cells.H). Re-derivation = the code's aggregation (battery_luna.py run_luna): C5a empties with reason seat/harness increment by_reason; R->refused; H->hedged; window_loss = f3b_reasons.count("harness")/n on B; window = run ts.

| run/arm | by_reason (seat/harness/refused/hedged) | f3b_environment (band / window_loss / window) | invariant |
|---|---|---|---|
| R1 A (fullest empties) | 40 / 0 / 0 / 0 | n/a (no governor) | 40 = E |
| R1 B | 10 / 4 / 0 / 0 | `elevated-loss` / 0.1 / 14:04:30Z | 14 = E |
| R2 A | 40 / 0 / 0 / 0 | n/a | 40 = E |
| R2 B | 6 / 3 / 0 / 0 | `baseline-4-9%` / 0.075 / 14:09:50Z | 9 = E |

The **7/7** is the S8 reason split: all 7 F3b misses (4 R1 B + 3 R2 B) carry reason `harness`, 0 middleware. Mean(F3b): 0.9 (R1), 0.925 (R2). The prose class "4-9% baseline / 503-window ~85%" re-derives as the record's own bands (R2 4-9%, R1 elevated) - no 503 ride. All seat+harness = E; invariants pass.

## 3. The verdict-turn test

Record: INCONCLUSIVE x2 + the S7 seat-abstains-by-silence story. Rule (pre-committed): CERTIFY iff B-A>=0.20 AND B>=0.85C; FALSIFY iff B-A<0.20 OR (B<0.85C AND B<=A); INCONCLUSIVE iff judge fail / cache-missing / C-A<0.05 / mean(F3b)<1.

1. **INCONCLUSIVE x2 - unchanged.** R1: B-A=0.475, B 0.475<0.85C 0.616, mean_f3b 0.9<1 -> INCONCLUSIVE (F3b trigger). R2: B-A=0.575, B 0.575<0.85C 0.616, mean_f3b 0.925<1 -> INCONCLUSIVE (F3b trigger). mean_f3b predates the seeds; neither field enters the rule's arithmetic. Misses: the same 7 with or without the fields - the split/band describe, never move.
2. **Residual B < 0.85C - untouched.** B_over_0.85C: false in both ledgers; FALSIFY also needs B<=A (false) - a recorded fact, not the trigger; the band re-derives from the same rate, adding no branch.
3. **S7 - reinforced, not altered.** Seat dominates the empties: A 40/40 both runs; B 10-seat/4-harness (R1), 6-seat/3-harness (R2). "Seat abstains BY SILENCE" is strengthened (50/54 R1 A+B empties, 46/49 R2). S7's numerators are cells facts, untouched.

No verdict turns on the split or the band: the door test fails to open.

## 4. The plateau check

No new measurement gap named by THIS re-measure: the re-derivation is faithful (invariants pass); miss count + reason split already live (`mean_f3b`, `f3b_reasons`); the band is the same rate re-labeled. A re-run (~$0.467/exec x A+B, $100 cap) would re-measure the same fields - theater-class, refused: improvements named just for the loop's sake are noise. SEED-1/SEED-2 stand as plain measurement rows - this measure is the confirmation.

## 5. Verdict + loop-state

- **NO-IMPROVEMENTS.** Deciding claim: the verdicts (INCONCLUSIVE x2, S7) re-run identically under the re-derived fields - the F3b trigger fires from the pre-seed `mean_f3b` (0.9/0.925 < 1.0) before and after, and the split/band enter no rule branch. Evidence: s.3 lines 1-3; receipts s.2 (harness 4/3, seat 10/6, invariants E=14/9).
- **PLATEAU-REACHED -> the confirmation cycle -> HOLD at the apex.** Readiness: seeds' schema asserted (32/32 GREEN `a713970204`), receipts pass, no verdict turned.

## 6. The compose-check (the eight steps, one evidence line each)

| # | step | state | evidence |
|---|---|---|---|
| 1 | The gate verbatim | FIRED | quoted in the header; RFC QUIET; study-tree only, nothing public |
| 2 | The stack-order clause | FIRED | the leg's own seeds measured first (s.1-3); STORM-CONTEXT corroboration of class only, zero adoption |
| 3 | The review-loop | FIRED | draft -> ledger/code re-read (mean_f3b=0 / 503-band draft errors corrected) -> refine -> pushbacks (F3b-vs-residual; S7-reinforced; band class) -> no-change re-read with receipts |
| 4 | One tool call per round | FIRED | one tool call per round; independent reads batched in single rounds |
| 5 | Skeleton by ~round 4 | FIRED | seven sections stood at the first write round the gate allowed; content done pre-commit |
| 6 | Real content only (never a stub marker) | FIRED | every cell a real receipt (s.2 sums equal ledger totals); no stub/todo token |
| 7 | <= 6,000 chars per write | FIRED | artifact under the cap (verified at commit) |
| 8 | Commit before exit | FIRED | add -> commit -> push of this artifact to the study branch; pull --rebase on rejection; exit only after the commit succeeded |

## 7. The gate + record-first closing

Nothing here is public; this artifact is study-branch only. The ledgers' ABSENCE is recorded, named (no `by_reason`/`f3b_environment` in R1/R2), and re-derived - never silently patched. The doors close by the seeds' own contract: no verdict turned -> plain measurement rows -> the confirmation cycle -> HOLD at the apex.
