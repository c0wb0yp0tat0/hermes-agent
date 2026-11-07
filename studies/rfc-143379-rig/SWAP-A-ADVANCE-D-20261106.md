# SWAP-A-ADVANCE-D-20261106 — the W2-isolation run-design's last mile into a runnable spec

**Branch:** `study/rfc-143379-rig-20261105` | **Seat:** `reflection/beam-1.0-501b-a23b:free` (probed LIVE 00:14 ET, "Beam") | **Lane:** copycat (SPEC lane — runnable spec is the deliverable; the experiment is NOT executed here).

## 1. The seam you were handed (ground)
The run-sitting is the blank on the "is the W2 handoff-preamble the driver of empty answers" seam. The guard-separation's exact shape is in `run_eval.py`'s probe-loop, quoted; the design doc is `NEGENTROPY-SWEEP-D-W2DESIGN-20261106.md` + `W2-ISOLATION-RUN-DESIGN-20261107.md` (§3's bypass mechanics; pin `c54c1bc614f20bd5e603a4826dc5c80a670a654a`; 0.29→~0.75 tier expectation).

## 2. The exact diff-patch of the probe-phase's guard-separation (handoff-preamble removal) in run_eval.py
The probe-phase in `run_eval.py` gates the system-preamble off `runtime.get("api_key") and runtime.get("base_url")` (line 81 — the receipted wall). The one-axis diff, single controlled change:

- **added (run config):** `"handoff_guard": false` in the run's config JSON — the probe's system-preamble is removed so probe-answering is isolated from the guard.
- **removed (probe-loop, run_eval.py):** the guard-branch of the preamble pull — the `runtime.get("api_key") and runtime.get("base_url")` gate is bypassed; the probe-loop no longer reads the handoff block, so the probe sees a system-preamble = empty (compaction summary's other content intact).

Exact quoted probe-loop shape (from the committed `run_eval.py` probe-loop):

```python
# probe-loop (run_eval.py) — guard-separation diff
if runtime.get("api_key") and runtime.get("base_url"):
    system_preamble = load_handoff_preamble()   # removes the "Do NOT answer questions / wait for a new user message" block
else:
    system_preamble = ""                        # guard bypassed → probe-answering unguarded, retention unchanged
```

That is the whole handoff-preamble removal: no other axis moves — model, fixture, JSON shape, probe bank, judge all held constant.

## 3. The 3-run command-line
The design's ONE variant, three runs across the debug fixture with the guard bypassed. From the shell (receipted as the command-line):

```bash
PYTHONDONTWRITEBYTECODE=1 python run_eval.py \
  --fixture /root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-1.json \
  --config  run_eval_config_no-guard.json --label "W2-NoGuard-run1" --count "${EMPTY_TARGET:-10}"

PYTHONDONTWRITEBYTECODE=1 python run_eval.py \
  --fixture /root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-2.json \
  --config  run_eval_config_no-guard.json --label "W2-NoGuard-run2" --count "${EMPTY_TARGET:-10}"

PYTHONDONTWRITEBYTECODE=1 python run_eval.py \
  --fixture /root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-3.json \
  --config  run_eval_config_no-guard.json --label "W2-NoGuard-run3" --count "${EMPTY_TARGET:-10}"
```

`run_eval_config_no-guard.json` carries the `"handoff_guard": false` (preamble source removed) and the same model/fixture/JSON-shape/probe-bank/judge as the guard-on debug runs. Each run emits `'"answer": ""'` per probe; in-lab target is empty-answer count → ~0 under H1, and the W2 probes' k-term kept-rate moves 0.29 → ~0.75 tier.

## 4. The label (handoff-preamble / guard-separation / W2-isolate)
`W2-NoGuard-run1|run2|run3` — label the run class: **no-guard run** (probe-answering isolated from the handoff preamble). Read-back: `grep -c '"answer": ""' <result.json>` per run + W2 tier kept-rate. Vote on the designed seam: CONFIRMED / REFUTED / SEPARATION-UNMEASURED.

## 5. The risks and their mitigations (runnable spec)
| Risk | Mitigation |
|---|---|
| `runtime.get("api_key") and runtime.get("base_url")` gate never opens on the free seat — the bench reports a live seat but the wall is closed | Receipted as the bench's truth; the in-lab run is a SPEC, not an execution; the bench records "SEPARATION-UNMEASURED" until the eval-runtime LLM-window opens |
| H0 (refute) → the empty answers survive no-guard | The design names the next isolation candidate (probe-judge's empty-answer scoring path in `run_eval.py`), listed in the verdict matrix, carried as the next-leg fire-order |
| Wall / grounding drift | Seats rotate probe-before-pin; the pin `c54c1bc614f20bd5e603a4826dc5c80a670a654a` is fixed in §2; receipted receipts only, no claims before receipt |

## 6. The last-mile verdict + the numbers + the path
**Verdict:** the seat is live (00:14 ET, "Beam"), the design is receipted (guard-separation quoted, pin fixed), the command-line is ready. The run is **NOT executed here** (spec lane); the verdict is **UNMEASURED / SPEC-ONLY** until the eval-runtime LLM-window opens and the 3 no-guard runs fire. The numbers (2/5/4 on the debug-class runs) are the guard-on baseline; the in-lab targets (→~0 empties, 0.29→~0.75 tier) are the designed measures.

**Path to a runnable run:** (a) open the eval-runtime LLM-window → (b) run the three `run_eval.py` commands above → (c) `grep -c '"answer": ""'` per run → (d) re-derive the W2 tier kept-rate vs the 0.75 tier → (e) fold into the head's next-shift fire-order (the refuted-radical is already named: the probe-judge's empty-answer scoring path).

## 7. The receipted record
- Design spec (receipted): `NEGENTROPY-SWEEP-D-W2DESIGN-20261106.md` + `W2-ISOLATION-RUN-DESIGN-20261107.md` (pin `c54c1bc614f20bd5e603a4826dc5c80a670a654a`, 0.29→~0.75 expectation).
- Guard-separation quote: `run_eval.py`'s probe-loop, `runtime.get("api_key") and runtime.get("base_url")` (line 81) — the wall.
- Debug-class empties (re-derived by the head at 00:15 ET): run-1 2/10, run-2 5/10, run-3 4/10.
- The 3-run command-line (§3) — this doc's last-mile into a runnable spec.
- No execution is claimed; the verdict is **UNMEASURED / SPEC-ONLY**.