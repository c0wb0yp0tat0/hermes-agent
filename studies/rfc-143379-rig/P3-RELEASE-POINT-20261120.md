# P3-RELEASE-POINT-20261120 — the F2 release-point A/B + F3 judge gate (the plan's P3 arm)

*Gate: "the gate: nothing public without the user's word." — RFC QUIET. Nothing moves public/permanent until the user speaks.*

Seat: runners (unmetered class) · Branch `study/rfc-143379-rig-20261105` · 2026-11-20 · Parent: MASTER-FLAGSHIP-20261119 (P3 row) · Consumers: P4 (PERSISTGYM certify battery) + the F2/F3 lanes.

## 0. The gate, verbatim
> "the gate: nothing public without the user's word." — RFC QUIET.

## 1. Place in the sequence + the baseline story
P3 = the fire's **F2** (release-point A/B) + **F3** (judge gate). F2 rides the compaction episodes M1's battery measures; F3 gates every battery's results before they are read (LANE-1 §3). Baseline: CONFIRMATION-CYCLE-20261118 — **F2 3/3 crown rides + 1 goal-status ghost** (one-flat), **F3 28/31 forks alight** (two-flat). The fronts are plateaued, so a regression is a regression, not noise.

## 2. RED-grep-proof — the gate is ABSENT from the rig's compaction path today
```
cd /root/workspace/repos/hermes-agent
grep -nE "release_event_id|ending_event|GOVERNED_COMPACTION_RELEASE_RULE|citation" \
  hermes_state_compression.py hermes_state_mutation_compress.py hermes_bootstrap.py \
  tests/e2e/core/compaction/*.py
# -> exit=1, zero matches
grep -rln "release_point_gate|GOVERNED_COMPACTION_RELEASE_RULE" --include=*.py . \
  | grep -v studies/rfc-143379-rig/probes
# -> exit=1, zero matches outside the study probe
```
Receipt (2026-11-20, tree @ 680ce1d367): the three wiring points named by M3 Probe A (`hermes_state_compression.py` candidate selection, `hermes_state_mutation_compress.py` mutation write, `hermes_bootstrap.py` archive read-back) and the compaction battery `tests/e2e/core/compaction/*` carry **no** citation / release-event token. The gate exists only as the study probe `probes/release_point_gate.py` (59 lines) + `probes/test_release_point_gate.py` (51 lines) — **unwired**. RED on the wiring; the probe's own unit tests are GREEN (10/10, §6).

## 3. F2 — the release-point A/B (exact spec)

### 3.1 The rule, verbatim
> "release a block only when the teacher can cite the event that ended its use."

Citation = a named event id (`release_event_id`, 16+ hex chars) + `final_use_ts` bound to the block's lineage row. No citation ⇒ held + logged with reason.

### 3.2 The arms
| Arm | Mechanism | Decision per block |
|---|---|---|
| **A — the record's control** | gate OFF (`GOVERNED_COMPACTION_RELEASE_RULE=OFF`; `CompactionGovernor.flag_default=False`) | `stub` — released without a witness (the pre-F2 behavior) |
| **B — the release-point governor** | gate ON (`CompactionGovernor()`); M3 Probe A wired | citable → `archive`; uncited → `keep` (held hot); `override` → `stub` |

### 3.3 The pre-committed episodes (the non-re-observable-fact class)
`make_episode(seed, cut_point)` (probes/battery_pilot.py:32): a fact planted at the cut-point turn — the **only** place it appears — filler either side; truncation at the cut-point destroys it unless the record keeps it. Pre-committed: seeds **(11, 23, 37)** × `N_TURNS = 10` (tests/e2e/core/compaction/_helpers.py:45) = **30** episodes at `cut_point = 12` (probes/battery_full.py:26, `BATTERY_CUT` default), mirrored verbatim across arms (one-factor law). The class is PersistGym's (M1): full history 200/200 vs truncated-with-one-non-re-observable-fact 7.5%.

### 3.4 The measurement bars
| Bar | Definition | Threshold |
|---|---|---|
| **precision** | of arm B's `archive` decisions, the fraction whose citation verifies (the cited `release_event_id` hashes to the block's actual final-use event) | **>= 0.95** (fail < 0.80) |
| **FP** | arm B `archive` decisions on blocks with **no** citable ending event (silent archive of an uncited block) | **= 0** |
| **completeness** | of the truly-citable blocks, the fraction arm B releases | **= 100%** |

Note (honest): FP = 0 makes precision 1.0 on the same set; the >= 0.95 bar is the pre-committed slack for citation-format noise, FP = 0 is the hard zero on the class the rule exists to stop.

### 3.5 The metric rows
| run id | seed | episode set | cost | receipt |
|---|---|---|---|---|
| `F2-A-20261120` | 11,23,37 | 30 eps, non-re-observable class | $0 (fake provider, unmetered) | **UNVERIFIED** — fires runner-side |
| `F2-B-20261120` | 11,23,37 | same 30 eps, mirrored | $0 | **UNVERIFIED** — fires runner-side |
| `F2-CTRL-20261120` | 11,23,37 | 20-ep control subset (F3) | $0 | **UNVERIFIED** — fires runner-side |

### 3.6 The decision rule + the INCONCLUSIVE clause
Pre-committed, no post-hoc swaps:
- **PASS** iff precision >= 0.95 AND FP = 0 AND completeness = 100%.
- **FAIL** iff FP > 0 OR precision < 0.80 OR completeness < 100%.
- **INCONCLUSIVE** iff the run's own pre-conditions fail (cache/log missing, episode set not mirrored, judge gate NULL). **The clause: rewrite the experiment, never the claim.**

### 3.7 The two-way doors
| Move | Reversibility | Rollback |
|---|---|---|
| shadow → enforce | flag `GOVERNED_COMPACTION_RELEASE_RULE` | flip to `OFF`; held blocks re-admit next cycle, bytes intact |
| wire → unwire | additive patch on the three compaction files | `git revert <wire/test commit>`; the probe module stays |
| test commit | additive only | revert the test commit |

## 4. F3 — the judge gate (exact spec)
20 episodes, >= 90% agreement or NULL. Control set = `[(f"the answer is TOKEN{i} here", f"TOKEN{i}") for i in range(20)]` (probes/battery_full.py:66), frozen judge (`FrozenJudge.freeze()`), run **before** the battery's results are read.
| Verdict | Meaning |
|---|---|
| **PASS** | control accuracy >= 0.90 — the run's results may be read |
| **FAIL** | the judge answered, accuracy < 0.90 — the run is void |
| **NULL-with-named-seam** | the gate could not run (judge unfrozen / control set absent / responder error) — the seam is named in the row |

Verdict vocabulary verbatim: **PASS / FAIL / NULL-with-named-seam**. The refreeze is the gate's only write (`JudgeControlGate.refreeze`); the gate is read-only otherwise (test_judge_control_gate.py::test_gate_is_read_only).

## 5. The machine-side dispatch form
Runner leg executes, from the repo root:
```
cd /root/workspace/repos/hermes-agent
# 0. RED-grep re-proof (gate absent) — the §2 command
# 1. F3 first: the judge gate on the 20-ep control set (read-only; refreeze = its only write)
.venv/bin/python -m pytest studies/rfc-143379-rig/probes/test_judge_control_gate.py -q
# 2. F2 arm A — the record's control: the compaction battery with the gate OFF
GOVERNED_COMPACTION_RELEASE_RULE=OFF .venv/bin/python -m pytest tests/e2e/core/compaction/ -q
# 3. F2 arm B — the governor: same battery, gate ON (the runner wires the probe into the three compaction files first)
GOVERNED_COMPACTION_RELEASE_RULE=ON  .venv/bin/python -m pytest tests/e2e/core/compaction/ -q
# 4. the probe's own battery
.venv/bin/python -m pytest studies/rfc-143379-rig/probes/test_release_point_gate.py -q
```
Notes: the compaction battery is pytest-parametrized over `SEEDS = (11, 23, 37)` (no CLI arm selector). `battery_full.py` is the **F4** three-arm certify battery and takes **env** vars (`BATTERY_N`, `BATTERY_CUT`, `READER_URL`, `READER_MODEL`), not flags — the F2 A/B's citation arm is the new arm M3 Probe A adds to `tests/e2e/core/compaction/`. The runner writes the run ledger below.

**Receipt shape.** Each arm's run ledger JSON **>= 12,000 bytes** (the harness read-cap floor — a ledger under it is a stub, not a run) and carries:
- the run row: `run id`, `seed`, `episode set`, `cut_point`, `ts`, `cost_per_exec`;
- the **12,000-token threshold row** (`THRESHOLD_TOKENS = 12_000`, tests/e2e/core/compaction/_helpers.py:39) verbatim;
- the **F2 gate row** per compaction decision: `(compaction_event_id, guard_outcome, release_hold, rerun_flag, payload_hash)` with `guard_outcome == "honored"` (probes/battery_luna.py:289 `check_f2`);
- the F3 verdict row: `PASS / FAIL / NULL-with-named-seam` + judge fingerprint + control accuracy.

## 6. The executed-rule binds (receipts actually run)
| Receipt | Result | Note |
|---|---|---|
| `probes/test_release_point_gate.py` + `probes/test_judge_control_gate.py` | **10/10 GREEN** (0.19s) | .venv python 3.14, pytest 9.1.1, 2026-11-20 |
| RED-grep (§2) | **exit=1, zero matches** | tree @ 680ce1d367 |
| `tests/e2e/core/compaction/test_compaction_auto.py` | **6/7 GREEN**; `test_provider_overflow_terminates[good]` **FLAKY** (FAIL then PASS on re-run) | under `/usr/bin/python3` 7 failed (missing `snowballstemmer`); under `.venv` 6 passed / 1 flaky |

The battery's billed runs fire machine-side on the runners (unmetered class). **This lane's artifact is written from the ACTUAL receipts above, never expected values.** Runs this lane could not execute (the F2-A/F2-B/F2-CTRL rows) are left **UNVERIFIED**, named in §3.5. The flaky compaction case is a named seam, not a silent pass.

## 7. The compose-check table (8 marks, FIRED/ABSENT, one evidence line each)
| # | Step | State | Evidence line |
|---|---|---|---|
| 1 | Deconstruct | FIRED | M3 Probe A's rule + wiring points; the A/B arms; the bars — each traced to its source doc |
| 2 | Sense | FIRED | Ground read cold (master P3 row, M3, FIRE-SEQUENCE, CONFIRMATION-CYCLE); the gate's absence proven by grep, not asserted |
| 3 | Choose | FIRED | Arm A = the record's control (gate OFF); arm B = cite-or-hold; F3 gates F2's results first |
| 4 | Calibrate | FIRED | precision >= 0.95 (fail < 0.80), FP = 0, completeness 100%; 20-ep control >= 90% — all from M3's apex row + LANE-1 §3 |
| 5 | Probe | FIRED | Every move names metric + rollback (§3.7); the INCONCLUSIVE clause pre-committed |
| 6 | Review | FIRED | Stranger re-read + 4 adversarial pushbacks + two no-change re-reads (§8) |
| 7 | Record | FIRED | This artifact; receipts in §6 are actual runs with their command lines |
| 8 | Compose-check | FIRED | This table; ABSENTs (the billed F2 runs) named UNVERIFIED, none estimated |

## 8. The review-loop
Draft → stranger re-read (the draft re-read cold against the four ground docs) → one refinement per finding → 4 adversarial pushbacks → termination: no-change re-read twice.
- **Refinement (stranger re-read finding):** the first draft's dispatch form invented CLI flags (`--n/--arms/--cut-point/--out`) on `battery_full.py`, which takes **env** vars and is the **F4** battery. Corrected: the F2 A/B rides the pytest-parametrized compaction battery (`SEEDS`), and `battery_full.py`'s env-var shape is named as the F4 leg's, not the F2's (§5). The run-id and cut-point placeholders were also pinned to concrete ids (`F2-A-20261120`) and `cut_point = 12`.
- **Pushback 1 — "FP = 0 and precision >= 0.95 are redundant."** Held: redundant on one set; kept both because FP = 0 is the hard zero on the rule's target class and >= 0.95 is the pre-committed slack. Named in §3.4.
- **Pushback 2 — "The gate exists; calling it absent is false."** Held: the *wiring* is absent (grep exit=1 on the three compaction files + the battery); the probe module exists. RED is scoped to the wiring, stated in §2.
- **Pushback 3 — "Arm A stubs, so it is not a release."** Held: arm A is the record's pre-F2 control — the behavior the rule replaces; `stub` is the release-without-witness the rule exists to stop. Named in §3.2.
- **Pushback 4 — "The 12K receipt floor is invented."** Held: 12,000 is the harness's read-cap (DEEP-LOOKS-NETWORK-20261006) and `THRESHOLD_TOKENS` (_helpers.py:39); the floor is the read-cap, the threshold row is the token constant. Both cited in §5.
Termination: no-change re-read ×2 — stable.

## 9. Two-way doors (master table)
| Move | Reversibility | Rollback |
|---|---|---|
| shadow → enforce | flag | `OFF`; held blocks re-admit, bytes intact |
| wire → unwire | additive patch | `git revert` the wire/test commit |
| F3 PASS → refreeze | read-only gate | refreeze = the gate's only write |
| public → private | the gate | re-arm to last private value |
| cost → stop | cap stop | COST-OVER recorded |

## 10. Loop-state line
**CONTINUE** — P4's card fires on this landing (t_ae2f547c).

## 11. Fold for the master's §7
P3 2026-11-20: the F2 release-point A/B + F3 judge gate specced machine-side — RED-grep proves the gate unwired (exit=1 on the three compaction files + the battery); the probe's own tests 10/10 GREEN; the compaction battery 6/7 with one flaky case (named). Arms A (gate OFF, the record's control) / B (cite-or-hold); bars precision >= 0.95, FP = 0, completeness 100%; F3 = 20-ep, >= 90% or NULL-with-named-seam. Billed runs UNVERIFIED, named. Next: P4.

## 12. The wall clause, verbatim
> "a non-reproduction is a QUESTION, not a stop."
