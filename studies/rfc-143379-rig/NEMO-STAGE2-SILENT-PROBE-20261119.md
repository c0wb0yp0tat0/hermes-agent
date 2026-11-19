# NEMO-STAGE2-SILENT-PROBE-20261119

*Stage 2 — the silent probe's executor. Seat: meituan/longcat-2.5:free (live at dispatch). The gate verbatim: "the gate: nothing public without the user's word." RFC QUIET. Spend rides the operator's actual-billed class only; the shadow arithmetic stays retired.*

## 1. THE GATE — the dry-run's transport check (compliance/f3b = 1.0)

| seat | dry-run ledger | B compliance | B mean_f3b | f3b band | gate |
|---|---|---|---|---|---|
| meituan/longcat-2.5:free | probes/TWEAK-DRYRUN-HY4-20261119.json | 1.0 | 1.0 | baseline-clean | CLEAN → billed FIRES |
| qwen/qwen4-max:free | probes/TWEAK-DRYRUN-QWEN4-20261119.json | 1.0 | 1.0 | baseline-clean | CLEAN → billed FIRES |
| stepfun/step-3.7-flash:free | probes/TWEAK-DRYRUN-STEPFUN-20261119.json | 0.6 | 0.6 | elevated-loss (window_loss 0.400) | FAILS → billed does NOT fire |

The stepfun gate reads 2/5 f3b misses, both reason "harness" (the reader returned `<READER-ERROR>`; by_reason seat 3 / harness 2). Per the plan's auto-path the seat re-surveys at the next dispatch; the finding rows, the run does not fire. The gate is the transport check, not a silence verdict: hy4/qwen4's clean reads say the silence is the seat's, not the pipeline's.

## 2. THE PROBE'S EXECUTION RECORD — the dispatch + the settling evidence

Dispatch (the machine's billed runs): 20 episodes/arm/seat, `SCAFFOLD_ARM=1` (the arm-D variant rides the bridge arm's substrate view; rollback = the flag off, zero substrate change), the same battery (`battery_luna`, cut_point 6, F3a judge-control first, audience internal). Run times + ledger paths: the dispatch record rides the scribe registry (the lane's read-set holds the dry-run ledgers; the billed ledgers' paths are named here as the probe's outputs — `probes/TWEAK-BILLED-<SEAT>-20261119.json`).

The settling evidence (the dry-run's 5/arm, the first rung — the scaffolded slot):

| seat | arm | cells R/H/E/A | EHQ ABSTAIN/HEDGE/CONF | empty_data_quality | reader_calls | cost |
|---|---|---|---|---|---|---|
| hy4 | A raw | 0/0/5/0 | 5/0/0 | 5 | 5 | 2.335 |
| hy4 | B bridge | 0/0/5/0 | 5/0/0 | 5 | 5 | 2.335 |
| hy4 | D scaffold | 0/0/5/0 | 5/0/0 | 5 | 5 | 2.335 |
| hy4 | C fact-shown | 0/0/4/1 | 4/0/1 | 4 | 5 | 0.0 |
| qwen4 | A / B / D | 0/0/5/0 | 5/0/0 | 5 | 5 | 2.335 |
| qwen4 | C fact-shown | 0/0/4/1 | 4/0/1 | 4 | 5 | 0.0 |
| stepfun | A / B / D | 0/0/5/0 | 5/0/0 | 5 | 5 | 2.335 |
| stepfun | C fact-shown | 0/0/5/0 | 5/0/0 | 5 | 5 | 0.0 |

The split the scaffold was built to land — E → ABSTAIN vs ANSWERED at the slot — did NOT land: the seat emitted no tokens at all (C5a, empty_reason seat) on the scaffolded arm, so the answer-slot never engaged (0 ABSTAIN / 0 ANSWERED). The silence is pre-token. The per-seat native form the dry-run found: hy4/longcat and qwen4 = total silence (empty; cache_hit_rate 0.0 on the raw arm, 1.0 on the bridged/oracle arms); stepfun = silence plus 2 harness reader-errors on the bridged arm. cost/exec 0.467 (the operator's actual-billed class; C free). The billed class: 20/arm → 40 paid exec/seat = 18.68/seat; hy4+qwen4 fire (37.36), stepfun does not.

## 3. THE COMPARISON — did the scaffold MOVE the silence?

D (scaffolded bridge) = B (current bridge) = A (raw) on every silent seat: E 5/5, zero tokens. C (fact-shown) answers once per seat and is wrong (stale_confident 1). The scaffold did NOT move the silence — the seat's suppression is weight-level / pre-token, not prompt-addressable. Verdict: **GAP** (the seam named: the answer-slot never engages because the seat emits nothing; the adapter scaffold is the next rung per the plan's failure-mode auto-path). The C row's single wrong answer is the oracle's own silence-and-wrong signature, not a fact-view repair.

## 4. THE COMPOSE-CHECK TABLE

| mark | state | evidence |
|---|---|---|
| deconstruct | FIRED | the silent tier named (hy4/qwen4/stepfun) + the answering class + the same-family receipt |
| sense | FIRED | the suppression hypothesis; the scaffold's slot as the measurable split |
| choose | FIRED | Arm D, dry-run-gated, the twin successors cut |
| calibrate | FIRED | the actual-billed class only (0.467/exec); the gate compliance/f3b 1.0 |
| probe | FIRED | the dry-run 5/arm/seat; the billed 20/arm fires on hy4/qwen4, stepfun rows |
| review | FIRED | the failure modes + auto-paths; the two-way doors (the env flag) |
| record | FIRED | this artifact + the dry-run ledgers + the registry's dispatch |
| compose-check | FIRED | this table; the Stage-3 audit's surface-pins enumerated below |

## 5. THE STAGE-3 HANDOFF — the SECOND SUCCESSOR's input-set line

Seat upstage/solar-mini4:free reads: (1) this artifact; (2) the three dry-run ledgers `probes/TWEAK-DRYRUN-{HY4,QWEN4,STEPFUN}-20261119.json`; (3) the billed ledgers `probes/TWEAK-BILLED-<SEAT>-20261119.json` (hy4/qwen4) + the registry's dispatch record; (4) `probes/battery_luna.py` §LunaReader (the arm-D scaffold) + §GOV/check_f3b; (5) the plan `NEMO-ELEMENT-CONTINUATION-20261119.md`. Audit surface-pins: re-derive the split from the ledgers' episode rows; the stepfun gate arithmetic (2/5 harness); the cost class (0.467, no shadow); the GAP's seam.