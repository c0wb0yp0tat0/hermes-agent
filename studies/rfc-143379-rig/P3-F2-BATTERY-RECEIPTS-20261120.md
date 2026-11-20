# P3-F2-BATTERY-RECEIPTS-20261120 — the F2/F3 machine-side battery's first run (the pve1 floor, machine 'pve')

*Run ledger — F2 A/B + F3 judge gate per P3-RELEASE-POINT-20261120.md §5. Host: this seat = the pve1-avrea-parallel floor (machine 'pve', the same floor that ran 44742897319). Commits: wiring 93f8f0fc81-era → the shadow patch (this ledger's commit).*

## The receipts (actual runs, 2026-11-20)
| Step | Command (repo root) | Result | Evidence |
|---|---|---|---|
| 0. wire-proof | `grep -c GOVERNED_COMPACTION_RELEASE_RULE hermes_state_mutation_compress.py` | **2 hits — WIRED** (was exit=1 RED at tree 680ce1d367, the P3 landing's §2) | the shadow check at `compress_in_transaction`'s archive release |
| 1. F3 gate | `.venv/bin/python -m pytest studies/rfc-143379-rig/probes/test_judge_control_gate.py -q` | **5 passed** (0.14s) — the 20-ep control gate PASS | the gate ran BEFORE the battery's results were read |
| 2. F2-A (gate OFF) | `GOVERNED_COMPACTION_RELEASE_RULE=OFF .venv/bin/python -m pytest tests/e2e/core/compaction/ -q` | **33 passed, 1 failed** (110.55s): `test_provider_overflow_terminates[good]` — the SAME named flaky (P3 §6: FAIL-then-PASS on re-run), never a regression | the record control = the pre-F2 baseline |
| 3. F2-B (gate ON) | `GOVERNED_COMPACTION_RELEASE_RULE=ON .venv/bin/python -m pytest tests/e2e/core/compaction/ -q` | **33 passed, 1 failed** (104.96s): the same named flaky | ENFORCEMENT READ: the gate-ON run = the gate-OFF run |
| 4. probe battery | `.venv/bin/python -m pytest studies/rfc-143379-rig/probes/test_release_point_gate.py -q` | **5 passed** (0.14s) | the gate's unit logic holds (5+5 = the P3 §6's 10/10) |

## The instrument read (the honest verdict)
F3: **PASS**. F2's arm-A baseline: reproduced at the battery's full size (33+1 with the named flaky). F2's arm-B enforcement: **INCONCLUSIVE by the pre-committed clause** — the gate-ON run changed nothing because the existing compaction battery never drives an uncited in-place release past the wired gate (its flows publish rather than in-place-archive); the citation-arm episodes (M3 Probe A's new arm for `tests/e2e/core/compaction/`) are NOT yet in the tree. The clause binds: rewrite the experiment, never the claim. The next instrument-add (the citation arm):
- a parametrized episode: `make_episode(seed, cut)` (the non-re-observable-fact class), an in-place compression whose prepared snapshot carries NO `release_event_id`;
- flag OFF → archives (the control); flag ON → **F2-HOLD** (the ValueError, receipted as guard_outcome `honored` per check_f2);
- the bars read from the hold/archive counts: precision >= 0.95, FP = 0, completeness 100%.

## Cost
$0 — fake-provider battery (the unmetered class), nothing billed.
