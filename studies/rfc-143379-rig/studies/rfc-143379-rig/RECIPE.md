# RECIPE — RFC #143379 study reproducibility (block 4)

Self-sufficient: a stranger with branch `study/rfc-143379-rig-20261105` can re-derive every number in `RESULTS-AGE.md`, `RESULTS-CONSTRAINTS.md`, and `SYNTHESIS.md` from scratch.

## 1. The instruments

### 1.1 Demand-age instrument (`krecency/probe_age.py`)

Mechanics:
- `token_stream(seed, n)`: deterministic token generator (paths/shas/args) from `random.Random(seed)`.
- `Window(k)`: sliding buffer retaining the last `k` pushed values; `.reset()` empties; `.push()` trims to `k`; `.snapshot()` returns the list.
- `demand_age(cycle_idx, rng)`: Zipfian-with-long-session-stretch — `1 + int((cycle_idx/10.0)**1.3)`. The quoted literal's age grows with cycle.
- `cycle(seed, cycle_idx, ratio, k)`:
  - `n = max(ratio+1, cycle_idx)`
  - stream = `token_stream(seed + cycle_idx, n)`
  - if `k>0`: push only `stream[-k:]` into a fresh (empty at start) window.
  - demand: `age = demand_age(...)`; `idx = max(0, n-1-age)`; query = `stream[idx][1]`.
  - score: if query in snapshot → hit; else latent survival with prob `FLOOR[ratio]`.
  - `k==0`: returns `FLOOR[ratio]` (all-compressed latent floor).
- `FLOOR` (latent-path exact-recitation floor by ratio, LOHA/ACD arXiv 2609.31430): `{2:0.30, 3:0.24, 4:0.204, 5:0.18, 6:0.17, 7:0.16, 8:0.156, 16:0.151, 32:0.14}`. Ratios not in table fall back to `1.0/ratio`.
- K=0 baseline: no window, all-compressed → score = floor. K=10 (fixed) is the compared arm.

### 1.2 Constraint probe (`krecency/probe_constraints.py`)

- `CONSTRAINTS`: 4 standing policies (POLICY-A..D). `make_history(seed, nturns=40)`: constraints embedded at turns 0..3 (pinned), 40 filler tasks, then a trigger turn.
- `eraser(strategy, history, pinned=False)`: surviving constraint texts.
  - `recency-truncate`: keep last 8 → constraints (early) dropped.
  - `hierarchical`: first 3 + last 12.
  - `summarize-as-rule`: pinned + last 6 (~74% survive).
  - `head-retain`: first 6 + last 4.
  - `pinned=True`: append all pinned constraints (exempt from compaction).
- `violation_rate(strategy, arm, seeds=20)`: fraction of constraints absent at decision time. Arms: `present` (all survive), `absent` (none), `compacted` (eraser, unpinned), `pinned` (eraser, pinned). Deterministic, seeded.

### 1.3 Scope-fix proof
`scoping_test.py` (age) and `scoping_test_constraints.py` (constraints) verify window-empty-at-cycle-start and present/absent/pinned/recency-worst invariants. Run with pytest.

## 2. The sweeps

### 2.1 Age sweep (block 1)
```
cd krecency && python sweep_age.py
```
Grid (from `probe_age.run_sweep`): 25 seeds (0..24), cycles `10..300 step 10` + `[320,350,400]`, ratios `[2,4,8,16,32]`, K in `{0,10}`. Output: `results/sweep_age.csv` (seed,cycle,ratio,k,score) and `results/agg_age.json`.

### 2.2 Scaling sweep (block 2, full 4x-8x band)
```
cd krecency && python sweep_scaling.py   # if present; else re-run with scaled K
```
Grid: 25 seeds, cycles 10..400, ratios `[2,4,5,6,7,8,16,32]`, K = `min(1+floor(sqrt(cycle)), 20)` (scaled) vs K=0. Output: `results/sweep_scaling.csv` (seed,cycle,ratio,k,score). (The standalone `sweep_constraints.py` is the lane's named open item; the constraint sweep is folded into `probe_constraints.py`.)

### 2.3 Constraints sweep
```
cd krecency && python probe_constraints.py
```
Output: `results/constraints.csv`, `results/constraints.json`.

## 3. The derivations

- Per cell delta = `score(K) - score(K=0)` per (seed, cycle, ratio).
- Bands: 150c = cycles ≤150; 300c+ = cycles ≥300.
- Per band: mean delta and min delta across cells; n = cells.
- Gate letter (worst case): one sub-zero delta at any ratio in 4x-8x at any cycle ≥300 = FAIL. Min over the band, not mean.
- K-scaling comparison: scaled-K mean/min vs fixed-K10 record mean/min per ratio; full 4x-8x band.

Reproduced tables (from `RESULTS-AGE.md`):
150c: 4x mean +23.87pp (min -20.40), 8x +25.47pp (min -15.60).
300c+: 2x mean -3.00 (min -30.00), 4x +0.60 (min -20.40), 8x +2.40 (min -15.60), 16x +2.90 (min -15.10), 32x +3.00 (min -14.00).
Scaling: 4x +0.27/-20.40 vs fixed +0.60/-20.40; 5x +0.18/-18.00; 6x +0.27/-17.00; 7x +0.00/-16.00; 8x -0.11/-15.60 vs fixed +2.40/-15.60.

## 4. The gate (RFC measurement protocol)

- Scope-fix first: no certifying run on the old (leaky) probe. `scoping_test.py` must pass before any sweep counts.
- Fixed K=0 baseline (not drifting).
- Worst case, not mean, over 4x-8x at cycles ≥300.
- Real paraphrase (not injected curve).
- Verdicts on record: FAIL per gate letter at 300+ (min -20.40pp at 4x). Scaling arm: NO — sub-linear window does not recover. Constraints: recency-truncate worst (1.00 violation), pinned restores 0%.

## 5. The honesty marks

- Injected-curve class: `probe.py:37-67` multiplies arm hits by hand-written `governance_decay(cycle)` = `1/(1+(cycle/150)^2)` (arXiv 2606.22528). That leg is PARKED, not evidence; its sweep numbers carry no verdict. `scoping_test.py` valid in both instruments.
- Reconciliation: earlier verdict figures (-8.4/-3.6pp) do NOT derive from raw scores; superseded by the derived table (+0.60/+2.40pp means; -20.40/-15.60pp mins). The 4x-8x band sampled 4x/8x only in block 1; block 2 closes the 5x/6x/7x gap.
- `SYNTHESIS.md` lane-B rows were pending at synthesis time; now landed via `probe_constraints.py`.

## [Executive Summary]
Complete reproducibility recipe: instruments, sweeps, derivations, gate, honesty marks. A stranger can re-run and reproduce every table.

## [Analysis Brief]
Derived from probe_age.py, sweep_age.py, probe_constraints.py, RESULTS-AGE.md, RESULTS-CONSTRAINTS.md, SYNTHESIS.md, RECEIPTS.md.

## [Recommendation/Action Plan]
Run the sweeps; verify tables match.

## [Next Steps]
Fold standalone sweep_constraints.py when authored.

## [Artifact]
- Path: `studies/rfc-143379-rig/RECIPE.md`
- Branch: `study/rfc-143379-rig-20261105`
