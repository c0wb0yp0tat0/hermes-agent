# COPYCAT FINDING — lane `beam` — the apex adjudication + the next mechanism

**Lane:** copycat (beam base). **Artifact:** `studies/rfc-143379-rig/copycat-findings/copycat-beam-20261105.md`.
**Register:** receipts, never claims. No instrument re-run; every number below is read from the rig's files (named at each citation). A red verdict is a finding, never smoothed.

## 0. The one-line verdicts (the short form; the body is the proof)

- **The demand-age gate FAIL is a FINDING, not an instrument artifact.** `probe_age.py` is derived (no injected term): K=0 returns the constant `FLOOR`, K=10 scores `1.0` only when the quoted literal is still inside the tail window; a miss returns `0.0` whenever the survival coin fails. The per-cell delta is therefore one of `{1-floor, 0, -floor}`; a `-floor` cell is a real missed literal, and `RESULTS-AGE.md` records them as seed-universal at every horizon (25/25 seeds at 4x/300c+). The gate's letter (worst-case min ≥ 0pp) fails on the floor's excursions, and the means' erosion (4x +23.87 → +0.60pp) is the session-length face of the same mechanism.
- **The scaled-K arm's NO is a FINDING on the tested formula, with a protocol caveat.** `scaled-K = min(1+floor(sqrt(cycle)), 20)` underperforms fixed-K10 at every reported ratio (`RESULTS-AGE.md` K-SCALING ARM table); the sqrt scaling is too slow for the demand age's `1 + (cycle/10)^1.3` growth. The caveat: only one scaling function was tested, so "scaling never helps" is not yet licensed — only "this scaling doesn't."
- **The constraint arm (recency-truncate 1.00, pinned 0.00) is a FINDING.** `probe_constraints.py` is deterministic and the ranking is mechanically produced by the eraser's keep-sets; recency-truncate drops the early standing constraints by construction, and `pinned=True` appends them back. The mechanism is the window's eviction class, confirmed.
- **The competition arm's NOT-CONFIRMED is an INSTRUMENT-LIMIT, not a finding about the field.** `probe_compete.py` injects rivals only into the *survivor pool* of the K=0 floor path; the K=10 hit path (`if q in snap`) never faces a rival, and the a* proxy uses equal weights `[1.0] + [1.0]*n` so its softmax is a function of rival count, not of evidence mass. The sweep cannot move the letter by construction.
- **The archive arm's FAIL is REAL under its stated (optimistic) conditions, but partly CONSTRUCTIONAL.** `probe_archive.py` archives every literal (`for t in stream: arch.put(t[1])`) — the optimistic bound — yet recall looks up only the demanded literal's id (`aid = arch.id_of.get(q)`), so the budget knob never admits a competing literal; the budget is toothless in the modeled world. Two further inertias: `rlimit` is per-cycle but there is one query per cycle, and `max(1, mat_budget_tokens)` grants one recall even at 0% budget.
- **The one next mechanism: COMPETING-ADMISSION ARCHIVE (demand-age level).** Fix the toothless knob so the budget admits the demanded literal *or* a rival by a query-time score, and re-measure whether the archive clears the gate. Falsifier below.

## 1. The adjudication — for each red verdict, FINDING or INSTRUMENT-LIMIT

### 1.1 Demand-age gate (RESULTS-AGE.md) — FINDING

**Verdict: FINDING.** The RFC's gate letter (worst-case min ≥ 0pp over all cycles ≥ 300 at every 4x–8x ratio; one sub-zero = FAIL) fails, and the mechanism is the instrument's own, not an injected term.

**Byte-level, from `probe_age.py`:**
- K=0 returns the constant floor: `if k == 0: return floor`, with `FLOOR = {2: 0.30, 4: 0.204, 8: 0.156, 16: 0.151, 32: 0.14}`.
- K=10 scores `1.0` only when `q in snap` (the literal is among `stream[-k:]` pushed into the window); otherwise it survives with probability `floor` (`if rng.random() < float(floor): hits += 1`).
- The query is `idx = max(0, n - 1 - age)` with `age = 1 + int((cycle_idx / 10.0) ** 1.3)` and `n = max(ratio + 1, cycle_idx)`. The window is the tail `stream[-k:]`.

So the per-cell score is one of three values — `1.0` (in-window), `floor` (survived), or `0.0` (missed) — and the per-cell delta is therefore one of `{1-floor, 0, -floor}`. A `-floor` cell is exactly a literal older than K positions whose survival coin missed. There is no aggregation trick hiding it, and no hand-written decay multiplying hits (contrast the earlier `probe.py`, where `hits = int(round(hits * governance_decay(cycle)))` — the injected class that `RESULTS.md` parks as NOT EVIDENCE). `probe_age.py` has no such term; `grep` for decay/coefficient/fitted terms returns nothing.

**Why the failure is real (the driver, in the instrument's own words):** `RESULTS-AGE.md`'s UPDATE corrects the earlier "minority of seeds" reading: "at 4x/300c+ ALL 25 seeds carry sub-zero deltas (2-4 of their 4 sampled cycles each); the excursions exist at BOTH horizons (the 150c minima are equally deep), so the min-letter as written fails independent of session length — the noise floor's excursions, not a long-session-only collapse." I confirm against the raw CSV (`results/sweep_age.csv`): at 4x, seed 0's K=10 score at cycle 60 is 0.00 while K=0's is 0.204, a delta of −20.4pp; the same seed repeats the miss at cycles 80, 100, 120. At cycle 300 the miss is still there (−20.4pp at 4x). The means' erosion is the session-length face: 2x +20.93 → −3.00, 4x +23.87 → +0.60, 8x +25.47 → +2.40, 16x +25.70 → +2.90, 32x +26.00 → +3.00pp. The reversal is real and ratio-dependent, and the protocol's protocol gaps are named in the file itself (4x/8x only sampled in block 1; ratios 5x/6x/7x absent). The gate stands as the RFC's standard; the probe's fixes apply to the probe, not the bar.

**Instrument-limit nuance (one, named):** the min-letter as written is pathologically strict — a single missed survival coin at any horizon fails it, and the instrument's own record says the minima are horizon-independent. The honest reading is therefore two-part: (a) the means' erosion is a genuine session-length effect that the hard window fails to arrest (FINDING), and (b) the min-letter's failure is driven by the latent floor's coin misses, which is the noise-floor class. Both are reported; neither is smoothed.

### 1.2 Scaled-K arm (RESULTS-AGE.md, K-SCALING ARM) — FINDING on the tested formula, with a named caveat

**Verdict: FINDING (scoped).** The RFC's open question "does the K-recency window scale with session length?" is answered NO for the tested scaling function.

**Byte-level:** `scaled-K = min(1+floor(sqrt(cycle)), 20)` (per `RECIPE.md` §2.2 and `RESULTS-AGE.md` block 2). The table in `RESULTS-AGE.md` shows scaled-K mean below fixed-K10 at every ratio, e.g. the 4x–8x band's scaled-K min is deeper than fixed-K10's. The demand age grows as `(cycle/10)^1.3`, i.e. faster than `sqrt(cycle)`; the window's growth rate is below the demand's growth rate, so the scaled window loses the literal even sooner than the fixed one at long horizons.

**Caveat (instrument-limit):** only one scaling function was tested. "Scaling never helps" is not licensed by this arm; "sqrt scaling loses" is. A linear-in-cycle or demand-age-proportional scaling is unmeasured and would be a cheap, high-value follow-up. I do not re-label this as a general NO.

### 1.3 Constraint arm (RESULTS-CONSTRAINTS.md) — FINDING

**Verdict: FINDING.** The mechanism is the window's eviction class, confirmed by a deterministic probe.

**Byte-level, from `probe_constraints.py`:**
- `recency-truncate` keeps `history[-8:]` (`K = 8; kept = history[-K:]`); standing constraints sit at turns 0..3, so they are dropped → violation 1.00.
- `hierarchical` keeps `history[:3] + history[-12:]` → 0.25 violation.
- `summarize-as-rule` keeps pinned + last 6 → ~0.00 violation (the rule survives).
- `head-retain` keeps `history[:6] + history[-4:]` → 0.00 violation.
- `pinned=True` does `kept = kept + [t for t in history if t.get("pinned")]` → 0.00 violation for all strategies.

The ranking (recency-truncate 1.00 > hierarchical 0.25 > summarize-as-rule = head-retain 0.00) is mechanically produced by the keep-sets, not fitted. The mapping in the file (anchor fail-closed = pinning; tombstone ledger = head-retain-friendly; write-gate = pinning enforcement point) is consistent with the probe's branches.

**Instrument-limit nuance (one, named):** the pinning-cost percentage was initially reported as 9.84–15.6% vs the field's <0.5% claim, which the file's own RE-WALK corrects as scale-confounded (183-token sim denominator vs production-scale context). The comparable measurable is the pinned *token count*: ~18 word-tokens (4 standing lines) vs the field's ~47. Scale-normalized to 10K tokens the analog is ~0.18% — it meets the <0.5% class. The raw percentage was the sim's tiny denominator speaking, not a real cost. I accept the re-walk's correction; the pinning cost is of the same order as Constraint Pinning.

### 1.4 Competition arm (RESULTS-COMPETE.md) — INSTRUMENT-LIMIT

**Verdict: INSTRUMENT-LIMIT (the NOT-CONFIRMED verdict stands, but as a constructional finding, not a field finding).**

**Byte-level, from `probe_compete.py`:**
- Rivals are injected only into the *survivor pool* of the K=0 path: `if rng.random() < rival_rate: rivals.append(...)` plus `n_rivals = int(round(rival_rate * 3))`. At `rival_rate = 0.0`, both branches yield zero rivals (`int(round(0.0*3)) == 0`), so the 0% row has no rivals at all.
- The K=10 hit path never sees a rival: the window is `for t in stream[-k:]: w.push(t[1])`, and rivals are never pushed into `w`. The hit test is `if q in snap` where `snap = w.snapshot()` — rivals cannot collide with the true literal on the hit path.
- The K=0 (all-compressed) path returns `floor` when there are no rivals and a rival-defeated floor when there are; rivals only ever touch the floor path.
- The a* proxy: `weights = [1.0] + [1.0] * len(rivals)`, softmax over them. With equal weights, a* is `1/(1+n_rivals)` whenever rivals exist and `1.0` when they don't — a function of rival count, not of evidence mass. Hence R²(a*, score) ≈ 0.000–0.002, nowhere near the field's 0.35–0.58.

**What the table actually shows:** deep-low prevalence 0.447 at 0% rival, 0.469 at 10%, 0.677 at 30%. The baseline does not vanish when rivals are removed, so the "noise floor" is not solely the conflict class — the latent survival term itself produces the lows. That part is a real observation. But the arm cannot test the field's competition class because the rivals never compete on the path whose outcome the verdict claims to measure (the K=10 hit path). The NOT-CONFIRMED verdict is therefore correct in its conclusion ("the re-labeling is not confirmed") but the reason is constructional: the arm as built cannot confirm or refute the field's claim. The honest next step is to rebuild rivals so they compete on the hit path too (a look-alike rival present in the window's tail), and to give a* a weight that varies with the true literal's actual evidence mass (its position/proximity in the window), not a constant 1.0.

### 1.5 Archive arm (RESULTS-ARCHIVE.md) — REAL FAIL under optimistic conditions, partly CONSTRUCTIONAL

**Verdict: FAIL is real under the stated (optimistic) conditions, but the construction must be fixed before the FAIL is treated as exhaustive.**

**Byte-level, from `probe_archive.py`:**
- Optimistic bound: `for t in stream: arch.put(t[1])` archives every observed literal; `class Archive` is append-only with stable ids. So the archive contains the answer by construction — this is the "ID-known recall" optimistic bound the file calls it.
- Recall gate: `aid = arch.id_of.get(q)` — only the demanded literal's id is looked up. A competing literal in the pool is never a candidate for recall; the budget admits the demanded literal or nothing. So `archive_budget` (0/1/5%) only changes how many *tokens* of materialized recall are allowed for that single lookup, not which literal is recalled. The budget is toothless in the modeled world — it cannot fail to find the demanded literal when it is archived, and it cannot be asked to find a different one.
- Inertias: `rlimit` in {1,2,4} is per-cycle but there is exactly one query per cycle (`queries = [stream[idx][1]]`), so rlimit > 1 is inert; and `mat_budget_tokens = int(archive_budget * n)` with `max(1, mat_budget_tokens)` grants one recall even at 0% budget, so the 0% row is not a true "no archive" control.

**What the verdict (FAIL at every budget at cycles ≥ 300) actually establishes:** under ID-known, append-only, everything-archived conditions, the gate still fails at every tested budget and recall limit. That is a real, strong result — the archive does not rescue the gate even when it has the answer in hand. But because the budget knob never admits a competing literal, the arm cannot measure the thing the RFC's "archive-before-stub" piece actually needs to survive: admission under competition (which literal to recall when several look alike). The file's own delta in `RFC-GUIDANCE-20261105.md` names this: "the exhaustive verdict requires the competing-admission arm." The field corroborates the direction: write-time worthiness AUC 0.63–0.66 (query-blind by nature), so recovery lies in lifecycle control + query-time recall, not bigger budgets. I agree with that landing.

## 2. The one next mechanism

**Mechanism: COMPETING-ADMISSION ARCHIVE (demand-age level).**

- **Named mechanism:** an archive whose recall budget is spent by a *query-time admission decision* among {the demanded literal, its look-alike rivals in the survivor pool}, not by a single ID lookup of the demanded literal. The budget knob must intersect the path whose outcome the verdict measures: which literal gets recalled.
- **Why this one:** two of the three red verdicts that touch RFC proposal pieces (competition, archive) are constructional; the archive is the one whose constructional fix directly tests a proposal piece ("archive-before-stub"). Fixing the competition arm's a* proxy is also valuable but secondary — it re-tests a field claim about attention mass, while the competing-admission archive tests whether the RFC's archive piece can ever clear the gate. The divergence between the current (toothless) FAIL and a competing-admission re-measurement is the data.
- **Falsifier:** rebuild `probe_archive.cycle` so that, when the demanded literal is not in the window, the archive recalls among a candidate set of `{demanded} ∪ {rivals}` (rivals generated as in `probe_compete.py`, admitted at rates 0/10/30%), scored by a query-time weight (position-in-window recency + evidence mass), with the budget spent on the admitted candidate. Re-run the full grid (seeds 25, cycles 10..400, ratios 4x/8x, budgets 0/1/5%, rlimits 1/2/4). **The mechanism is falsified (archive-before-stub drops) if the worst-case min stays sub-zero at every budget with rivals present** — the gate cannot be cleared by archive admission under competition, and the piece must be re-scoped to lifecycle + query-time recall only. **It is supported (archive survives) if at least one (budget, rlimit, rival-rate) cell clears the letter's worst-case min ≥ 0pp** — the prior FAIL was constructional, and the piece is certifiable with a competing-admission recall. The one measurement that moves it: the worst-case min delta per (budget, rlimit, rival-rate) cell, reported alongside the current toothless-knob table for direct comparison.

## 3. The convergence read — what this adjudication implies for the RFC's proposal pieces

- **K-recency hard window (as proposed): DROP as the primary mechanism.** It fails the gate where it matters — the means erode 4x +23.87 → +0.60pp and the floor's excursions are seed-universal at every horizon. Sqrt scaling does not help; linear/demand-age-proportional scaling is unmeasured and unlikely to outrun a `(cycle/10)^1.3` demand growth, but that is a measurement, not a proof. The hard window is, on this record, the recency-truncate eviction class wearing a window's hat.
- **Pinned exact-literal path: KEEP — it is the convergent answer.** Constraint pinning gives 0.00 violation; recurrence-aware pinning drops deep-minima prevalence from 1.00 to 0.15; the cost is ~18 pinned tokens (~0.18% at 10K scale, same order as the field's ~47). The pinning analog is the gate's positive result on this instrument's record. The remaining work is to lift pinning from the constraint arm to the demand-age arm (measure whether recurrence-aware pinning clears the gate's worst-case min) — that is the longcat lane's named next mechanism, and I concur it is the right second measurement; it is complementary to, not competing with, the competing-admission archive above.
- **Provenance-origin: KEEP.** It survives on its own evidence — the constraint arm's pinned constraints retain their POLICY-A..D identity through compaction, and head-retain (tombstone-ledger-friendly) gives 0.00 violation. No red verdict touches it. The write-gate = pinning enforcement point mapping holds.
- **Archive-before-stub: HOLD, pending the competing-admission re-measurement.** Under the optimistic ID-known bound it fails at every tested budget, and the field's query-blind admission AUC (0.63–0.66) says bigger budgets will not help. But the constructional caveat (toothless knob) means the current FAIL is not yet exhaustive. The piece should be re-scoped now to "lifecycle correctness for what is pinned + calibrated abstention for what could not be known at write time" (the StageMem/DSGC shape, measured here at 0.00 on the constraint arm), and the competing-admission re-measurement either certifies a recall-based version or closes it. It is not certifiable as proposed today.

## 4. Refused skills / named limits

- `think-tank` §2 (envelope) and `head-supervisor-think-tank` loaded as base doctrine; `krecency-instrument` loaded for the derived-vs-injected standard and the gate protocol. `memory-chain` consulted for conventions.
- Refused: re-running or re-computing the instruments' data — `RESULTS-*.md` already carries the tables and verdicts; the calibration brief forbids it and my value is the independent judgment on that evidence. Refused: posting anything upstream or touching credentials — fork-only, no meter, no model credentials, per the hard lines.

## 5. Receipts cited

- `studies/rfc-143379-rig/krecency/RESULTS-AGE.md` (gate FAIL; derived table; K-scaling NO; seed-universal excursions)
- `studies/rfc-143379-rig/krecency/RESULTS-COMPETE.md` (NOT-CONFIRMED; rate table; a* R²)
- `studies/rfc-143379-rig/krecency/RESULTS-ARCHIVE.md` (FAIL at every budget)
- `studies/rfc-143379-rig/krecency/RESULTS-CONSTRAINTS.md` (violation table; pinning cost + re-walk)
- `studies/rfc-143379-rig/krecency/RESULTS-PIN.md` (recurrence protects 0.15 vs 1.00)
- `studies/rfc-143379-rig/krecency/RESULTS-ALIASING.md` (CONFIRMED-BOTH; a* R² 0.6548)
- `studies/rfc-143379-rig/krecency/RESULTS-RECITE.md` (NOT-CONFIRMED)
- `studies/rfc-143379-rig/krecency/probe_age.py`, `probe_compete.py`, `probe_archive.py`, `probe_constraints.py`
- `studies/rfc-143379-rig/RFC-GUIDANCE-20261105.md` (landing-path + delta)
- `studies/rfc-143379-rig/copycat-findings/copycat-longcat-20261105.md` (peer lane, consulted for the constructional reads)

---

**Artifact path:** `studies/rfc-143379-rig/copycat-findings/copycat-beam-20261105.md`
**Branch:** `study/rfc-143379-rig-20261105`
**Register:** receipts, never claims. A red verdict is a finding, never smoothed.
