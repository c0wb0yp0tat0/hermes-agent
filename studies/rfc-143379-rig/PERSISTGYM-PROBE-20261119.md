# PERSISTGYM-PROBE-20261119 — the PersistGym two-arm certify probe: the protocol + the dispatch receipt

*Gate (verbatim): "the gate: nothing public without the user's word." RFC QUIET.*
*Lane: P4 (fires on P3's receipt) · Branch: study/rfc-143379-rig-20261105 · Seat: longcat (lane) + the floor (runner leg).*

## 1 · THE GROUND (read once, cited)
- **The field's protocol:** arXiv 2610.26632 (Lencevicius, Microsoft, 19 Oct 2026); code + pre-registration + cost ledger at `github.com/raimondasl/persistgym`. PersistGym-lite = a generated ~20–32-turn task; at one turn the agent picks 1 of 10 options (chance 10%); the value was shown (observed) or derived, may/may not be `lookup`-recoverable, sits near or beyond the window W. H1 (luna, observed-far, window-no-notes vs full): not-recoverable drops >=25 pts; recoverable stays within 5 pts. Measured: full history **200/200** vs truncated-with-one-non-re-observable-fact **7.5%**; the **difference = 92.5 pts, 90% CI [89.5, 95.5]** (the interval is on the difference). Once lost, the model chose no answer over guessing.
- **The rig's machinery (committed; no new battery invented):** `probes/battery_pilot.py` — `make_episode` (the non-re-observable-fact class: a fact planted once at the cut-point, filler either side), `arm_view`, `SubstrateRecord`; the F3 judge gate `probes/judge_control_gate.py`. The field's arms ARE the battery.
- **The executed rule (LANE-1 §3, verbatim):** CERTIFY iff B−A>=20 pts AND B>=0.85×C; FALSIFY iff B−A<20 OR (B<0.85C AND B<=A); INCONCLUSIVE iff judge<90% OR cache-log missing OR C−A<5. **D1: the executed rule binds probe verdicts (record-first); the >=90% is the head's ratification bar. Both kept.**

## 2 · THE PROTOCOL (pre-committed before the run)
**Task class.** The field's observed-far / not-recoverable cell — the non-re-observable-fact class. The rig's miniature: `make_episode(seed, cut_point=12)`; the fact appears once, at the cut-point; the question is the 10-option choice (chance floor 10%).

**The two arms (the field's) + the executed rule's arm mapping (explicit).**

| Probe arm | The reader sees | Maps to |
|---|---|---|
| **FULL** | the complete episode history (the fact observable in-context) | the field's baseline (the 200/200 arm) |
| **TRUNC** | the history cut at the cut-point; the fact removed; no record | **the executed rule's A** (truncated-uncompensated) |

The executed rule's **B** (substrate = truncated + the durable record) is the treatment, and **C** (oracle = evidence-only turns) is the ceiling; both ride the SAME mirrored episodes as the named extension seam (the LANE-1 battery's arms), so the rule's A/B/C and the field's FULL/TRUNC are one episode set, never two.

**n = 100 episodes per arm (200 total)**, mirrored seeds (identical episodes across arms), fresh store per episode, deterministic seed. Sized to the pennies budget: the floor's seat is self-hosted (no API meter), so the binding constraint is the floor's wall-clock/CPU — measured: 4-core Intel Pentium Silver N5030, 3 GB, no AVX2 (run 44745081209's hardware header). The field's own cell size is ~100 templates/cell (PREREG), so 100/arm matches the ruler's scale.

**Resolution clause (pre-committed, not post-hoc).** At n=100/arm the SE of an arm-difference at p~0.5 is ~7 pts, so the executed rule's 5-pt INCONCLUSIVE band (C−A<5) is **sub-resolution**. The rule is kept verbatim (it is the executed rule); the scale-up is pre-committed: **if the first run's measured arm-difference SE exceeds 5 pts, the run doubles to 200/arm (the field's own 200/200 scale) before the verdict is read.** The limitation is named, not hidden.

**Chance guard (pre-registered secondary).** The TRUNC arm's accuracy is tested against the 10% chance floor (binomial). If TRUNC sits at/above chance, the ruler's contrast is void -> UNKNOWN (settling evidence: the chance test's numbers).

**Judge.** The frozen exact-match judge + the F3 20-episode control gate (>=90% or NULL-with-named-seam); the control runs before the results are read (P3's gate, specced machine-side). A control-gate failure **short-circuits** the battery to NULL/INCONCLUSIVE — the gate is the operational form, the rule's `judge<90%` branch is its formal expression.

**Logging (mandatory; the field's definition of done).** Input-logging ON for the run log; the probe's output; the seed + prompt template in the run log (so the field can rerun it); cache-hit rate + tokens in/out per arm; cost-per-success per arm. No row that is not actually billed (M1 §2).

**Pre-committed verdict (M1 §3's vocabulary, stated before the run).**

| Verdict | Meaning | Settling evidence |
|---|---|---|
| **COVERED** | the substrate's reader reproduces the field's class (FULL high, TRUNC at chance) and the record arm (B) recovers it per the executed rule | both arms + B, recorded, no GAP |
| **PARTIALLY-COVERED** | one holds, the other not | the seam named |
| **GAP** | the door closed (floor/seat unavailable) | the settling evidence named |
| **UNKNOWN** | the ruler in question (judge-control NULL; chance guard fired; C−A<5) | the settling evidence named |

**The executed rule binds** (D1): the substrate's certify verdict rides LANE-1 §3 verbatim on the same episodes. The two-arm PersistGym probe is the ruler's reproduction on our seat; the record arm (B) is the treatment. The local-LM floor as oracle is **VOID** (pre-registered dead-end) — if the floor is the only seat, the oracle line is void and the verdict reverts to the two-arm read.

## 3 · THE TWO-WAY DOORS (every move)
- **Run -> abort:** the probe aborts mid-run; the run log is preserved; the last good state is the record. No probe is committed by default.
- **Floor -> API seat:** the floor's seat is primary (self-hosted, unmetered); the free-tier API seat is the fallback; the local-LM oracle is void.
- **Cost -> no-cost:** a leg over its class cap stops and records COST-OVER; no re-plan without the user's word.
- **Public -> private:** nothing public without the user's word; the record re-arms to the last private value.
- The probe is **read-only vs the substrate**.

## 4 · THE FAILURE CLASSES PRE-ARMED
NOTE-5's five (compaction cliff; attribution failure; regime reversal; mis-scoring -> the judge gate; stale-confident) + the floor's measured class: the runner's communication loss at build (run 44619039714). **The floor's wall-clock seam:** the per-episode time is measured on the first run; if the floor's window binds, the probe shrinks to the largest feasible cell (pre-committed) rather than silently over-running. The wall clause (verbatim): "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised."

## 5 · THE DISPATCH FORM (machine-side) + THE RESULTS-RECEIPT SHAPE
**Dispatch (the runner leg):** `gh workflow run local-lm-test.yml --ref study/rfc-143379-rig-20261105 -f study_ref=study/rfc-143379-rig-20261105 -f run_id=PERSISTGYM-PROBE-<ts> -f model_profile=qwen2.5-0.5b-q4km -f engine_profile=llama-cpp-cpu`.
**Named seam:** the workflow's "run probe battery" step is the floor's feasibility read (the recite-anchor smoke; run 44745081209's battery-verdict = EXECUTED / PENDING-REVIEW); the two-arm PersistGym battery's execution is the head-machine's fire (the P3 pattern) — the probe script + the workflow step are the cut-path.
**Results-receipt shape:** `probes/PERSISTGYM-PROBE-LEDGER-<run_id>.json` (>=12,000 B) carrying the run row (run id/seed/episode set/cut_point/ts/cost), the arm rows (FULL/TRUNC: correct/accuracy/tokens/cache_hit_rate), the judge-control row, the chance-guard row, the verdict row; its sha256 recorded here on landing.

## 6 · THE DISPATCH RECEIPT (the runner leg's actual state, read first-hand)
- **First dispatch — RED, with its class.** run_id `PERSISTGYM-PROBE-20261119-2127` -> run **44619039714** -> **FAILURE**. Steps: checkout study ref ✓ · runner header ✓ · **build engine (minimal, CPU) ✗ — cancelled; the self-hosted runner lost communication** · fetch model / probe battery / run-receipt / upload — all skipped. 21:28:03Z -> 21:54:07Z (26m04s). **No artifact uploaded; no results file.** Evidence: `gh run view 44619039714 --json` (conclusion=failure, job 135895416639) + the log's own `RUN_ID: PERSISTGYM-PROBE-20261119-2127` line.
- **The floor's health, re-verified first-hand.** run **44745081209** (`ELEMENT-VERIFY-K2-20261120-1345`) -> **SUCCESS**, hostname `c0wb0yp0tat0`, 13:45:58Z: the engine built, the model fetched, the battery executed, the artifacts uploaded. run-receipt sha256 `0129701b4f6677a70ea930bb482110b97f3aaa50a1919e10f2603f3a88e261fb`. So 44619039714's RED is a transient communication loss, not a dead floor.
- **Re-dispatch (P2's form, in motion).** run_id `PERSISTGYM-PROBE-20261120-1352` -> run **44750545821**, created 14:08:06Z, **in_progress at receipt**; `study_ref = study/rfc-143379-rig-20261105` @ `9861d47dc1` (the tip at fire). Results file + sha: **pending its completion** (the shape in §5).
- **The machinery's own receipt (this lane).** `probes/test_battery_pilot.py` **6/6 GREEN** (.venv pytest); a deterministic-stub two-arm run, n=100/arm, cut_point 12, mirrored seeds 0–99: **FULL 1.000 / TRUNC 0.000** (gap 100.0 pts) — the machinery is sound; a real verdict needs the frozen reader + the judge gate. Stub ledger: `~/.hermes/cache/scratch/persistgym-twoarm-stub-20261120.json`.

## 7 · COMPOSE-CHECK (the stack-order clause — eight marks)
| mark | state | one evidence line |
|---|---|---|
| deconstruct | FIRED | the field's protocol (arXiv 2610.26632 + its PREREG) + the rig's committed machinery + the executed rule, each cited |
| sense | FIRED | the floor's measured hardware (4-core / 3 GB / no AVX2) + the 44619039714 RED class + the stub run's 1.000/0.000 + the stranger's six findings |
| choose | FIRED | the field's two arms; the floor's seat primary, the free-tier API fallback; the local-LM oracle void; the arm mapping explicit |
| calibrate | FIRED | n=100/arm (200 total) = the field's ~100 templates/cell; the F3 20-ep >=90% gate; the 92.5-pt ruler (CI on the difference); the resolution clause |
| probe | FIRED | the verdict vocabulary + the executed rule + the chance guard pre-committed; the receipt shape spec'd before the run |
| review | FIRED | the stranger re-read -> one refinement pass -> 4 adversarial pushbacks -> no-change re-read x2 |
| record | FIRED | this artifact; the dispatch receipt carries the run's own bytes; the fold line below |
| compose-check | FIRED | this table |

## 8 · REVIEW-LOOP (the record)
**Stranger re-read** (solar-mini4:free, no stake, cold): six findings. **One refinement pass** (each finding dispositioned): (1) the CI's scale — restated on the difference; (2) the 5-pt band's resolution — the SE clause + the pre-committed 200/arm scale-up; (3) the arm mapping — explicit (TRUNC = the rule's A; B/C the named seam); (4) the floor's capability — the wall-clock seam + the shrink clause; (5) the control gate vs INCONCLUSIVE — the short-circuit stated; (6) the chance floor — the pre-registered chance guard. **Four adversarial pushbacks** (kept in substance): the gate/INCONCLUSIVE overlap was unreconciled; the power argument cuts both ways (the 20-pt margins resolve, the 5-pt band does not); the arm mapping had turned the rule into an open question; the only executability evidence was a RED run. **Termination:** no-change re-read x2 of the refined draft against the ground — stable.

## 9 · FOLD (master §7)
**2026-11-20 — P4 (the PersistGym certify battery) LANDED:** `PERSISTGYM-PROBE-20261119.md` — the field's two-arm protocol (FULL/TRUNC; n=100/arm = the field's ~100/cell; the executed rule's A/B/C mapping explicit; the chance guard; the resolution clause) + the dispatch receipt: run 44619039714 (run_id PERSISTGYM-PROBE-20261119-2127) RED at build engine (the runner lost communication; no artifact), the floor re-verified GREEN (44745081209, run-receipt sha `0129701b…`), the re-dispatch in motion. The machinery 6/6 GREEN + a stub two-arm run (FULL 1.000 / TRUNC 0.000). Loop-state **CONTINUE** — the probe's machine-side fire is the head-machine's (the P3 pattern); the results ledger + its sha land on its completion.
