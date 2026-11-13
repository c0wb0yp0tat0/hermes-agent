# COPYCAT FINDING — lane `longcat` — the apex adjudication + the next mechanism

**Lane:** copycat (longcat base). **Artifact:** `studies/rfc-143379-rig/copycat-findings/copycat-longcat-20261105.md`.
**Register:** receipts, never claims. No instrument re-run; every number below is read from the rig's files (the files are named at each citation). A red verdict is a finding, never smoothed.

## 0. The one-line verdicts (the short form; the body is the proof)

- **The gate FAIL is real, not an instrument artifact.** The demand-age instrument is *derived* (no injected term): `probe_age.py` returns `floor` for K=0 and the literal's own presence in the K=10 snapshot otherwise; the per-cell min is `0 - floor = -floor` whenever the literal is out-of-window and the survival coin misses. The instrument's own record already says this ("the noise floor's excursions, not a long-session-only collapse" — `RESULTS-AGE.md`).
- **The competition arm's NOT-CONFIRMED is correct and is a genuine instrument-limit verdict** — the model built rivals that touch *only* the K=0 floor path and never the K=10 hit path (`probe_compete.py`), so a* is degenerate and the rival sweep cannot change the letter.
- **The archive arm's FAIL is real under its (optimistic) conditions, but the mechanism is partly instrument-authored** — the budget knob admits the demanded literal *and never a competing one*, so the budget is toothless in the modeled world (see §2.3).
- **The one next mechanism: EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency.** The regime it names is already in the data — `seed 0` carries sub-zero deltas from cycle 60; `seed 1` starts at cycle 80 — and no existing arm pins. The falsifier: if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection.

---

## 1. The adjudication — for each red verdict, FINDING or INSTRUMENT-LIMIT

### 1.1 The demand-age gate (RESULTS-AGE.md) — FINDING (the letter's worst-case genuinely fails), with one protocol artifact named

**Verdict: FINDING.** The RFC's gate letter (worst-case min ≥ 0pp over all cycles ≥300 at every 4x–8x ratio; one sub-zero = FAIL) fails, and the mechanism that produces it is the instrument's own, not an injected one.

**Byte-level, from `probe_age.py`:**
- K=0 returns the constant floor: `if k == 0: return floor`, with `FLOOR = {2: 0.30, 4: 0.204, 8: 0.156, ...}`.
- K=10 scores a hit iff `q in snap` (the literal is among the last K of the stream); otherwise it survives with probability `floor` (`if rng.random() < float(floor): hits += 1`).
- The query is `idx = max(0, n - 1 - age)` with `age = 1 + int((cycle/10)**1.3)`, and `n = max(ratio+1, cycle)`. The window is the *tail* `stream[-k:]`.

So the per-cell score is one of three values: `1.0` (in-window), `floor` (survived), or `0.0` (missed). The per-cell delta is therefore **either `1-floor` (positive), `0` (survived), or `-floor` (missed)**. A `-floor` cell is exactly a literal older than K positions whose survival coin missed. There is no aggregation trick that can hide it, and no hand-written decay curve multiplying hits (contrast `probe.py`, where `hits = int(round(hits * decay))` — the injected class that `RESULTS.md` parks as NOT EVIDENCE). `probe_age.py` has no such term.

**Why the failure is real (the driver, in the instrument's own words):** `RESULTS-AGE.md`'s UPDATE corrects the earlier "minority of seeds" reading: "at 4x/300c+ ALL 25 seeds carry sub-zero deltas (2-4 of their 4 sampled cycles each); the excursions exist at BOTH horizons (the 150c minima are equally deep), so the min-letter as written fails independent of session length — the noise floor's excursions, not a long-session-only collapse." I confirm this against the raw CSV (`results/sweep_age.csv`): seed 0's K=10 mean at cycle 60 is 0.04 vs K=0's 0.14 at ratio 32 (delta −10.0pp), and seed 0 is sub-zero at cycles 60, 70, 90 at 8x/16x. The sub-zero class is seed-universal.

**What the FAIL means, and what it does NOT mean:**
- It does **not** mean the window is useless. The means are strongly positive through the session body (`+23.87pp` at 4x/150c; `+25.47pp` at 8x/150c) and the erosion is ratio-dependent (4x `+23.87 → +0.60`, 8x `+25.47 → +2.40`, 16x `+25.70 → +2.90`, 32x `+26.00 → +3.00`). The window protects *recent* literals almost perfectly and *old* literals at the floor rate.
- It does mean the **RFC's literal gate letter** ("one sub-zero point fails") is not cleared by the K-recency hard window, and — because the minima are horizon-invariant — the failure is *not* a long-session phenomenon. The honest reading is: **the hard window's protection is exact for the recent K and floor-valued for everything older; a worst-case gate over old-literal recitation cannot pass on this class.**

**The named protocol artifact (an instrument-limit, but not a red-evidence one):** the 4x–8x band sampled 4x/8x only; ratios 5x/6x/7x are absent, and `sweep_scaling.py` is **not present** on the branch (the scaling table's script is missing; the CSV `results/sweep_scaling.csv` exists). The letter demands every ratio in the band. This is a *grid* gap, not a red finding — the min-letter already fails at the sampled ratios.

### 1.2 The K-scaling arm (RESULTS-AGE.md block 2) — FINDING (NO is real, and it is the informative direction)

**Verdict: FINDING.** The RFC's open question ("does the K-recency window scale with session length?") gets first direct data: **NO.** Scaled-K `min(1+floor(sqrt(cycle)), 20)` underperforms fixed-K10 at the headlines and fails the band at 7x/8x.

**Why this is the informative direction, not a limit:** the demand-age model says the quoted literal's age grows as `1 + (cycle/10)^1.3` — it grows *sub-linearly* in cycle (at cycle 300, age ≈ 68; at cycle 400, age ≈ 82). A scaling window `~sqrt(cycle)` (K ≈ 18 at cycle 300, K ≈ 21 at 400) is *wider* than fixed K=10 for old cycles, yet it underperforms. The reason is in the model's geometry: the window holds the **tail** of the stream, and the demand's `idx = n-1-age` is a *fixed offset from the end* (age positions back), not an absolute position. A wider tail window only helps when `age ≤ K`; since age at 300+ is 60–80 and K_scaled is 18–21, the wider window still misses the demanded literal and *dilutes* the in-window hit rate with extra recent literals that are not demanded. The scaling arm therefore measures a real geometric fact: **for a demand whose age outruns any practical K, widening K does not recover the literal — it only re-weights the window.** That is the finding; it is not an instrument artifact.

### 1.3 The competition arm (RESULTS-COMPETE.md) — INSTRUMENT-LIMIT (the model cannot move the letter; NOT-CONFIRMED is the honest verdict)

**Verdict: INSTRUMENT-LIMIT.** The arm's NOT-CONFIRMED is correct, and its cause is visible in the model's wiring.

**Byte-level, from `probe_compete.py`:**
- Rivals are injected only into a `pool` used for the a* proxy: `pool = [queries[0]] + rivals`, `weights = [1.0] + [1.0]*len(rivals)`, `a_star = exps[0]/s`.
- The K=0 branch: `if rival_rate == 0.0 or not rivals: return floor, a_star`, else it applies the rival-defeat term to the floor.
- The **K=10 branch has no rival term at all** — the hit path is `q in snap` with no collision.

Two consequences follow, both confirmed in `results/compete.csv`:
1. **a\* is degenerate.** The rival pool has one rival at most (`n_rivals = int(round(rival_rate*3))`: 0 at 0%, 0 at 10%, 1 at 30%) and all weights are equal (1.0), so `a_star` takes exactly two values: `1.0` (no rival) and `0.5` (one rival). It is a step function of "a rival happened to be drawn", not an attention-mass measurement. The reported `R2(a*,score) ≈ 0.00–0.002` is therefore *the model's own degeneracy*, not a refutation of the field's 0.35–0.58 class. The arm's own text says as much: "the softmax-over-pool proxy as implemented does not track per-trial failure."
2. **The rival sweep cannot change the gate letter.** Because rivals touch only the K=0 floor path, the deep-low prevalence at 0% rival (0.4467) is *unaffected* by the rival class — the floor term itself produces the lows. The arm's verdict line states this: "At rival-rate 0% the deep-low prevalence does not vanish (0.447), so the 'noise floor' is not solely the conflict class; the floor term (latent survival) itself produces the lows."

So the competition class is **NOT-CONFIRMED as the explanation of the excursions**, and that is a finding about the *model's coverage* (it did not implement the field's collision-on-the-survivor-path shape), not a finding that the field class is absent. The honest classification: **instrument-limit on the mechanism claim; the red "NOT-CONFIRMED" is not evidence against the field's competition class.** The wall-clause construction the model owes: rivals must be able to *displace* a literal from the K=10 window/pinned path (same-format, different-value collisions in the survivor pool), and a* must vary continuously with rival count/mass.

### 1.4 The archive arm (RESULTS-ARCHIVE.md) — FINDING (the gate fails at every tested budget), but the mechanism is partly instrument-authored

**Verdict: FINDING on the letter; INSTRUMENT-LIMIT on the mechanism's causal claim.**

**The letter's failure is real.** `probe_archive.py` gives the K=10 arm *three* recovery paths — window hit, archive recall, latent floor — against the K=0 floor alone. Even so, the gate fails at every budget. The archive adds `aid = arch.id_of.get(q)` recall for literals never evicted from the store (the store is append-only and `arch.put` is called for **every** literal in the stream, so `id_of` contains all of them). The recall is capped by `rlimit` and `mat_budget_tokens = int(archive_budget * n)`.

**The instrument-authored part (the limit):** the archive's `id_of` is a *perfect* address index — every literal ever seen is recallable by exact id, with no collision, no capacity pressure on the store, and no competing literal. The budget knob (`archive_budget`) limits *materialized tokens*, but the demanded literal is always the one admitted; the budget never forces a choice between the demanded literal and a rival. In the modeled world the budget is therefore **toothless for the demanded query**: the only way budget 0%/1%/5% can fail is the `rlimit` cap (1/2/4 recalls per cycle) and the `mat_budget_tokens` cap — and with a single query per cycle, `rlimit ≥ 1` always suffices, so at `rlimit ∈ {2,4}` the archive recovers the demanded literal *regardless of budget*. The `RESULTS-ARCHIVE.md` line "ARC-correlation: partial recovery of NIAH shape only at 5% budget r=4" is the honest trace of this: the budget's only measurable effect is at the margin where the materialization cap binds.

**What survives:** the archive arm's *optimistic bound* is the right frame (the RFC-GUIDANCE line "the archive's ID-known recall is the optimistic bound ... the write-time worthiness is query-blind"). Even granting perfect address recall, the gate fails — so the archive cannot rescue the hard window on this instrument. That is a finding about the *hard window's* gate, not about ARC's real design (which admits by worthiness and recalls under capacity pressure the model omits).

### 1.5 The constraint arm (RESULTS-CONSTRAINTS.md) — FINDING, with the cost correction already on the record

**Verdict: FINDING.** Recency-truncate is the worst compaction strategy (violation 1.00), pinning restores 0.00, and the mapping is direct: the K-recency window's eviction *is* the recency-truncate class.

**Byte-level, from `probe_constraints.py`:** `recency-truncate` keeps `history[-8:]`; the four POLICY constraints sit at turns 0–3 of a 45-turn history, so all four are dropped → violation 1.00. `pinned=True` appends all pinned turns → 0.00. `hierarchical` (first 3 + last 12) catches one of four (turn 3) → 0.25. `summarize-as-rule` and `head-retain` → 0.00.

**The cost correction is the instrument's own and it is right:** the raw `18/183 = 9.84%` was scale-confounded (a 183-word-token sim denominator vs the field's production-scale context). The comparable is the pinned *token count*: 18 word-tokens vs the field's ~47 — same order, lighter. Normalized to 10K tokens the analog is ~0.18%; at 16K, ~0.11% — it **meets** the field's <0.5% class once denominators are commensurate. This is a *finding about the ruler*, not a refutation of pinning; the re-walk's correction is the honest reading and I adopt it.

### 1.6 The aliasing arm (RESULTS-ALIASING.md) — FINDING, but the a* proxy is the weakest link

**Verdict: FINDING (the excursion class is real), with a named instrument caveat.** The a*-proxy R² = 0.6548 meets the bar (0.35), and the four-cell design (aliasing on/off × M on/off) is a genuine 2×2. But `probe_alias.py` computes `evidence_mass = 1.0 if (q in wbuf) else 0.0` — a *binary* indicator — and the R² is between that binary and the binary `score`. With `pa` injecting a same-value replica into `wbuf` (`wbuf.append(old)`), the aliasing knob raises `evidence_mass` (the replica lands in the window) without changing the true literal's presence, so the R² partly measures the replica's *window-presence*, not the true literal's *attention mass*. The CONFIRMED-BOTH verdict is defensible as a *prevalence* result (the four cells' excursion fractions), but the "a* R² 0.65" should be read as **evidence-mass-as-window-presence**, not as the field's attention-mass quantity. Named, not smoothed.

---

## 2. The synthesis the adjudication forces

The four arms are not four independent failures; they are **one mechanism measured at four resolutions**:

1. The hard window protects the recent K exactly and the older literals at the floor (`probe_age.py`).
2. The floor's excursions are the gate's letter-failure, and they are horizon-invariant (seed-universal, both horizons) — `RESULTS-AGE.md` UPDATE.
3. The competition class cannot explain them because the model never lets rivals touch the K=10 path — `probe_compete.py`.
4. The archive cannot rescue them because, even with perfect address recall, the demanded literal is admitted without competition — `probe_archive.py`.

The convergent reading: **the gate's worst-case failure is a property of the floor (old-literal survival), and neither the window (which can't reach the old literals) nor the archive (which admits the demanded literal uncompeted) nor the modeled competition (which never reaches the hit path) can move it.** The one lever the data actually supports is the one the constraint arm already measures: **pin the exact literal** (0.00 violation, ~0.18% token cost). The question the next mechanism must answer is whether pinning the *demanded old literals* — not just the standing constraints — moves the floor's excursions, and whether the pinning criterion can be chosen without knowing the demand.

---

## 3. THE ONE NEXT MECHANISM

### 3.1 The mechanism — **Exact-literal pinning in the demand-age arm, with a per-seed occurrence/recurrence/recency criterion**

**Named mechanism.** Extend `probe_age.py` with a *pin set*: at cycle start, promote a literal to the pin set by a criterion computable from the stream's history (candidates: occurrence count ≥ m; recurrence (≥ 2 distinct observations); age-weighted recency). Pinned literals are exempt from the window's eviction (the constraint arm's `pinned=True` shape, `probe_constraints.py`), so they survive to be hit even when `age > K`. The score is unchanged (`q in snap or q in pins → hit; else floor survival`).

**Why this is the most promising next measurement (the divergence is the data):**
- The per-seed divergence is already in the raw CSV and is *unexplained by every existing arm*. Seed 0 is sub-zero from cycle 60 (K=10 mean 0.04 vs K=0 0.14 at ratio 32); seed 1 starts at cycle 80; other seeds onset later. The onset is a function of *which literals each seed's stream happens to place at the demand offset* — i.e., the seed's literal recurrence structure. No arm in the study conditions on that structure. A pin criterion keyed to occurrence/recurrence is the direct test of whether the per-seed onset is a recurrence effect (finding) or a pure chance effect (the floor's coin, already measured).
- It is the *only* lever that moves the floor's excursions without widening K (which the scaling arm shows does not help) and without an archive (which the archive arm shows admits the demanded literal uncompeted). Pinning changes *which* literals are protected, not *how many* — and the constraint arm already proves the protection is exact (0.00 violation) and cheap (~0.18%).
- It is the RFC's own convergent answer (`RFC-GUIDANCE-20261105.md`: "the pinned exact-literal path (the OLD-literal pins at ~0.18% token cost, ~18 tokens vs the field's ~47) is the gate's convergent answer on this instrument's record"). The demand-age arm is the one place that answer has *not* been measured against the gate.

### 3.2 The falsifier

**Falsifier (the measurement that would kill the mechanism):** if the pin criterion is *recency*-keyed (pin the most-recently-observed m literals), the pin set collapses onto the window's tail and the protection is unchanged — the gate still fails. If the pin criterion is *occurrence*-keyed, the protection extends to literals the window cannot reach, and the gate's min-letter either clears or narrows. The discriminating comparison:

- **Arm P-recency:** pin the last m *distinct* literals by observation time. Predicted: no movement (the pins are a subset of the window's reach).
- **Arm P-occurrence:** pin literals observed ≥ m times. Predicted: the per-seed onset shifts later (the excursions require an out-of-window, un-pinned literal; occurrence-pinning removes the literals most likely to be demanded old).
- **Arm P-recurrence:** pin literals observed at ≥ 2 *non-adjacent* positions (a recurrence criterion, not a count). Predicted: the strongest movement, because it keys on the seed's literal-reuse structure that drives the per-seed divergence.

**The one measurement that would move it:** the **per-seed delta-onset curve** under each pin arm — for each seed, the first cycle at which the K=10-vs-K=0 delta goes sub-zero, plotted against the seed's literal-recurrence statistic (distinct literals / total observations, and the max occurrence count). If the onset is a recurrence effect, P-recurrence delays it monotonically in the recurrence statistic; if the onset is chance, all three arms leave the onset distribution unchanged and the floor's coin is confirmed as the whole story. The gate letter's min over the band under P-recurrence is the verdict.

### 3.3 Why not the alternatives (the named refusals)

- **Not "widen K"** — measured (scaling arm: NO; widening re-weights the window, does not reach the old literal).
- **Not "bigger archive budget"** — measured (archive arm: FAIL at every budget; the budget is toothless in the modeled world).
- **Not "add rivals to the floor path"** — the competition arm's model already does this and the baseline does not vanish; the missing piece is rivals on the *hit* path, which is a *revision* of that arm, not the next mechanism (it is the second-priority construction if P-recurrence fails).
- **Not "re-run the injected `probe.py`"** — parked as NOT EVIDENCE (`RESULTS.md`); its curve is self-fulfilling by construction.

---

## 4. THE CONVERGENCE READ — what the adjudication implies for the RFC's proposal pieces

The RFC's three proposal pieces, against the adjudication:

1. **The K-recency hard window — the adjudication says: replace the hard-window guarantee with the measured shape; the gate letter as written cannot be cleared by this class.** The window's protection is exact for the recent K and floor-valued for the old; the worst-case letter fails on the floor's excursions at *every* horizon (not a long-session-only collapse). The proposal should state the guarantee as **"exact for the recent K; floor-valued for the old"** and stop claiming a worst-case ≥0 at 300+. The scaling arm closes the "does it scale?" question: NO — widening K does not reach the old literals.
2. **The provenance-origin — survives on its own evidence.** Nothing in the four arms touches provenance-origin (the study's instruments do not model origin-tracking), so the adjudication neither confirms nor threatens it. It remains an independent proposal piece; the convergence read is that it is *orthogonal* to the gate's failure and should be argued on its own receipts, not borrowed from the window's verdict.
3. **The archive-before-stub — survives as an ordering claim, but its *guarantee* must be re-scoped.** The archive arm's optimistic bound fails the gate at every tested budget; the recovery the RFC-GUIDANCE names is "lifecycle control + query-time recall, not bigger budgets." The proposal piece should be stated as **ordering (archive before stub) with the honest guarantee: lifecycle correctness for what's pinned + calibrated abstention for what couldn't be known** — not as a gate-clearing mechanism. The model's toothless budget knob is the instrument-limit to name when this piece is argued.
4. **The pinning complement — this is the piece the adjudication promotes.** The constraint arm's 0.00 violation and the ~0.18% token cost are the only exact-protection evidence in the study; the demand-age arm's next mechanism (§3) is the test of whether that complement extends from standing constraints to demanded old literals. If P-recurrence moves the per-seed onset, the RFC's convergent answer is measured, not asserted.

**The one convergence line:** the gate's failure is the floor's, and the floor is moved only by *pinning the literal the demand will name* — which is exactly the piece the RFC already carries as its complement; the next mechanism measures whether the complement is a gate-clearing answer or a constraint-arm-only result.

---

## 5. Honest NOT-RUN / uncertainty (the register)

- The GitHub-window side of the verification: **NOT RUN** (`RECEIPTS.md`); the Avrea side is the live surface.
- `sweep_scaling.py` is **absent** from the branch (the scaling table's script is missing; `results/sweep_scaling.csv` exists) — the scaling arm's numbers are read from the CSV/RESULTS, not re-derived.
- Ratios 5x/6x/7x are **absent** from the age grid (protocol gap, named in `RESULTS-AGE.md`).
- The a* proxy in the aliasing arm is **binary** (window-presence), not the field's attention-mass quantity — named in §1.6.
- The archive's budget knob is **toothless for the demanded query** in the modeled world — named in §1.4.
- No instrument was re-run; no number above is computed by this lane. Every figure is read from the named file.