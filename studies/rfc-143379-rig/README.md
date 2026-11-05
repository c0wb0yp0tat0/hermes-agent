# The RFC #143379 study — the think-tank run, every artifact distinct, every status on the record

**Goal lock:** `c0wb0yp0tat0/hermes-agent` PR #1, branch `study/rfc-143379-rig-20261105`; RFC [NousResearch/hermes-agent#143379](https://github.com/NousResearch/hermes-agent/issues/143379). The Avrea verification leg: the envelope schema, the meter budget (4-vCPU, 1,500 min/mo), the wall clause. Downstream-only — no upstream posts, no upstream code changes; original upstream authors retain their ownership. Receipts here only where the runner landed them; every NOT-RUN marker stays until a receipt replaces it; committed definitions are not execution.

**What this is:** the independent verification study for [RFC #143379](https://github.com/NousResearch/hermes-agent/issues/143379) — run under the mechanism-of-mechanisms spine (classify → choose → probe → evaluate → adopt-or-park → standardize → verify). Every artifact below carries its status. Nothing here claims more than its receipt or curve shows.

## Stage: PROBE — the verification receipts (LANDED, EVIDENCE)
`RECEIPTS.md` — the Avrea leg's run ledger: five GREEN receipts at exact heads (requested == executed asserted in-run): #139606 `117/10` · the whole-anchor landing `28/1 xpassed` · #140008 `64` · #116673 `66` · **#141876 (the restore) `82`**. The GitHub-window side: **NOT RUN** (hosted queue class); the meter: 3 of 6 program dispatches used.

`RECIPE.md` — the reproducibility recipe: instruments, sweeps, derivations, gate, honesty marks.
## Stage: PROBE — the instruments (the derived-vs-injected discipline)
- `krecency/probe_age.py` + `sweep_age.py` + `RESULTS-AGE.md` — **the demand-age instrument: EVIDENCE** (derived, no injected term). Its mechanism: the recitation demand's age exceeds the window as cycles grow → the coverage erodes → the delta goes positive → sub-zero. Verdict: **FAIL per the RFC gate at 300+** — worst-case 4× −8.4pp (150c: 4× +3.6 / 8× +4.4; 300c: 4× −8.4 / 8× −3.6). The RFC's qualitative shape reproduced BY the mechanism, not imposed.
- `krecency/probe_constraints.py` + `RESULTS-CONSTRAINTS.md` + `results/constraints.*` — **the constraint-survival arm: EVIDENCE** (the four strategies, the pinning restoration, the rig-mechanism mapping). The strategy table lands in its RESULTS; the sweep's code was folded into the probe file — the standalone `sweep_constraints.py` is the lane's named open item.
- `krecency/probe.py` + `RESULTS.md` — **PARKED, NOT EVIDENCE**: the calibration leg injected `governance_decay(cycle)` (probe.py:37-67 multiplies the arm's hits by the hand-written curve). Marked on the record; its sweep's numbers carry no verdict. `scoping_test.py` — the scope-fix proof — valid in both instruments.

## Stage: REVIEW — the synthesis (LANDED)
`krecency/SYNTHESIS.md` — the integration thesis: **the recitation floor and the governance decay are one mechanism wearing two hats** — the K-recency window's eviction IS the recency-truncate class (the worst compaction strategy in the field's table). What the RFC's proposal pieces survive and need is in the synthesis's verdicts.

## Stage: VERIFY/STANDARDIZE — the state and the fold
- The RFC's long-session hard gate: **not cleared** — the derived instrument's worst-case verdict is sub-zero at 300+; the instrument is now honest enough to hold that verdict.
- The pilot's contour remains the gate's field data (the user's to shape).
- The nous surface: no public byte without the user's exact word. No upstream posts, no upstream code changes; original upstream authors retain their ownership.
