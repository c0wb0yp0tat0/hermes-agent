# COPYCAT FINDING — lane `krecency` — the apex adjudication + the next mechanism

**Lane:** copycat (krecency base). **Artifact:** `studies/rfc-143379-rig/copycat-findings/copycat-krecency-20261105.md`.
**Register:** receipts, never claims. No instrument re-run; every number below is read from the rig's files (the files are named at each citation). A red verdict is a finding, never smoothed.

---

## 0. The one-line verdicts (the short form; the body is the proof)

- **The gate FAIL is a FINDING.** The demand-age instrument is *derived* (no hand-injected decay term): `probe_age.py` returns the latent floor for K=0 and the literal's own presence in the K=10 snapshot otherwise; the per-cell min is `-floor` whenever the quoted literal is out-of-window and its survival coin misses. The instrument's own record confirms this ("the noise floor's excursions, not a long-session-only collapse" — `RESULTS-AGE.md` UPDATE).
- **The competition arm's NOT-CONFIRMED is a genuine instrument-limit verdict** — the model built rivals that touch *only* the K=0 floor path and never the K=10 hit path (`probe_compete.py`), so a* is degenerate and the rival sweep cannot move the letter.
- **The archive arm's FAIL is a constructional instrument-limit** — the budget knob admits the demanded literal's ID and never a competing one (`probe_archive.py`), so the budget is toothless by construction (the "constructional-knob check" in `krecency-instrument/SKILL.md`).
- **The constraint arm is a FINDING** — recency-truncate is the worst strategy (violation 1.00) and pinning restores 0.00; this is the mechanism that names the K-recency window's eviction class.
- **The one next mechanism: EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency.** The regime it names is already in the data — `seed 0` carries sub-zero deltas from cycle 60, `seed 1` from cycle 80 — and no existing arm pins. Falsifier: if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection.

---

## 1. The adjudication — for each red verdict, FINDING or INSTRUMENT-LIMIT

### 1.1 The demand-age gate (RESULTS-AGE.md) — FINDING (the letter's worst-case genuinely fails)

**Verdict: FINDING.** The RFC's gate letter (worst-case min ≥ 0pp over all cycles ≥ 300 at every 4x–8x ratio; one sub-zero = FAIL) fails, and the mechanism that produces it is the instrument's own, not an injected one.

**Byte-level, from `probe_age.py` (the probe is derived, never injected):**
- K=0 returns the constant floor: `if k == 0: return floor`, with `FLOOR = {2: 0.30, 3: 0.24, 4: 0.204, 5: 0.18, 6: 0.17, 7: 0.16, 8: 0.156, 16: 0.151, 32: 0.14}`.
- K=10 scores a hit iff `q in snap` (the literal is among the last K of the stream); otherwise it survives with probability `floor` (`if rng.random() < float(floor): hits += 1`).
- The query is `idx = max(0, n - 1 - age)` with `age = 1 + int((cycle/10)**1.3)`, and `n = max(ratio+1, cycle)`. The window is the *tail* `stream[-k:]`.

So the per-cell score is one of three values: `1.0` (in-window), `floor` (survived), or `0.0` (missed). The per-cell delta is therefore **either `1-floor` (positive), `0` (survived), or `-floor` (missed)**. A `-floor` cell is exactly a literal older than K positions whose survival coin missed. There is no aggregation trick that can hide it, and no hand-written decay curve multiplying hits (contrast `probe.py`, where `hits = int(round(hits * decay))` — the injected class the instrument parks as NOT EVIDENCE). `probe_age.py` has no such term.

**Why the failure is a finding, not an artifact:**
- The worst-case min at 300c+ is `-floor` per ratio (e.g., -0.204pp at ratio 4, -0.156pp at ratio 8) — these are the *latent survival* misses, and `RESULTS-AGE.md`'s UPDATE confirms: "at 4x/300c+ ALL 25 seeds carry sub-zero deltas (2-4 of their 4 sampled cycles each); the excursions exist at BOTH horizons (the 150c minima are equally deep), so the min-letter as written fails independent of session length — the noise floor's excursions, not a long-session-only collapse."
- The means' erosion (+23.9 → +0.6pp at 4x) is a **real, separate finding**: the mean delta goes from strongly positive at 150c to ~0 at 300c+ at ratio 4. The direction is the RFC's qualitative shape (positive protection through the session body; long-session reversal). But the *letter* fails on the min, and the min is the floor's escape, not the window's collapse.
- **Distinction enforced:** the means' erosion is a true finding (the window's protective margin compresses as demand age shifts older); the min failure is partly an instrument artifact of the gate letter (worst-case over a floor that is *by construction* the K=0 baseline). Both are reported, not reconciled — the means' erosion is the finding; the min failure is evidence the letter is crushing the floor.

### 1.2 The competition arm (RESULTS-COMPETE.md) — INSTRUMENT-LIMIT (the rival mechanism never reaches the decisive path)

**Verdict: NOT-CONFIRMED, correctly classified as an instrument-limit**, not a finding that rivals don't cause excursions.

**Byte-level, from `probe_compete.py`:** the rival injection is gated behind `if k == 0` for the floor path, and the a* proxy is computed over the survivor pool `{true} + rivals` regardless of k. Look at the structure:

- `rival_rate` affects `rivals` and `n_rivals` computed at the top of `cycle()` — but the *hits* logic for k=10 is in the `else` branch (window-hit path), which never consults `rivals`. The window either contains the literal (`hits += 1` via `q in snap`) or the latent floor kicks in. Rivals are only consulted in the `k == 0` branch (`if rival_rate == 0.0 or not rivals: return floor, a_star` then rival-collision logic).
- The a* proxy: `a_star = exps[0] / s` where `exps` is softmax over `[1.0] + [1.0]*len(rivals)` — with `rival_rate` at 0, there are no rivals, `a_star = 1.0` for all trials. The R² vs per-trial score is ~0 precisely because the window-hit path (k=10) is never pathologically competed, and the floor path (k=0) is all latent survival (all `a_star ≈ 1.0`, no discrimination).

**The finding:** the model's design limits the rival mechanism from reaching the decisive path. The K=10 window hit path doesn't face a rival because the window contains the literal verbatim. The a* proxy is degenerate because it only varies against itself (the true literal vs rivals of the *same shape* that a K=0 latent path would also miss). NOT-CONFIRMED is the correct verdict — the instrument can't measure what the design won't let it touch.

### 1.3 The archive arm (RESULTS-ARCHIVE.md) — INSTRUMENT-LIMIT (constructional, toothless knob)

**Verdict: FAIL is real, but the mechanism is partly instrument-authored** — the budget knob admits only the demanded literal's ID and never a competing one.

**Byte-level, from `probe_archive.py`:** the archive recall path is:

```python
aid = arch.id_of.get(q)
if aid is not None and recalled < rlimit and mat_used + 1 <= max(1, mat_budget_tokens):
    recalled += 1; mat_used += 1
    hits += 1; continue
```

The budget knob (`archive_budget` → `mat_budget_tokens = int(archive_budget * n)`) limits *how many* tokens can be materialized, not *which* literals can be recalled. The `arch.id_of.get(q)` lookup succeeds for the demanded literal regardless of whether a rival had the same format. The probe never constructs a rival literal that shares a format with the demanded one and checks whether the archive admits it. Per the krecency-instrument skill's "constructional-knob check": a budget knob that admits only the demanded literal (never a competing one) is toothless by construction — its FAIL is constructional, not evidential.

**The finding:** the archive's exhaustive verdict requires a competing-admission arm (a rival that shares the demanded literal's format and checks whether the recall budget admits the *rival* or the *true*). Under the current instrument, the FAIL is partly authored by the probe's own admission path, not purely by the mechanism.

### 1.4 The constraint arm (RESULTS-CONSTRAINTS.md) — FINDING (the mechanism that names the K-recency window's eviction class)

**Verdict: FINDING.** The probe is derived (no injected terms), and the result is unambiguous:

- `RESULTS-CONSTRAINTS.md` table: `recency-truncate` = violation 1.00 (worst), `hierarchical` = 0.25, `summarize-as-rule` = 0.00, `head-retain` = 0.00. Pinned arm restores 0.00 for all strategies.
- `probe_constraints.py` scoping test (`test_recency_worst`) asserts `vals["recency-truncate"] >= max(v for k,v in vals.items() if k != "recency-truncate")` — the scoping proof shows RED-on-leak (recency-truncate fails) vs GREEN-on-fixed (pinned restores 0.00).

**The finding:** recency-truncation is the K-recency window's eviction class. The K-window that erases exact text is the same window that erases standing constraints. This is the mechanism that names *why* the demand-age gate fails: the K-recency window's eviction is the recency-truncate class, and the constraint-pinning arm proves the same class behaves the same way under a different label. The field's DSGC corroborates (recency retains prerequisite chains in only 0.07 of runs).

### 1.5 The aliasing arm (RESULTS-ALIASING.md) — FINDING (CONFIRMED-BOTH)

**Verdict: CONFIRMED-BOTH.** The instrument is derived (no injected decay), and the four-cell sweep names the classes:

- `pa` (position-aliasing rate) × `M_on` (cumulative-mass knob). Alias-only (pa=0.3, M_off) keeps deep minima high; M alone (pa=0.0, M_on) raises prevalence. Combined (pa=0.3, M_on=True) is the dominant cell.
- `a*` evidence-mass proxy: R² = 0.6548 against per-trial score (meets the pre-set bar of 0.35).

**The finding:** the deep sub-zero excursions are the *aliasing × cumulative-proximity* classes working together, not noise and not single-rivals. The aliasing arm is the instrument that names the mechanism; the competition arm is the one that failed to reach it (1.2). The two arms are complementary: the aliasing arm confirns the mechanism's existence; the competition arm's constructional limit explains why it couldn't measure the same mechanism in a rival-collision setting.

---

## 2. The one next mechanism — EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency

**Why this mechanism:** The regime it names is already in the data, and no existing arm pins. `RESULTS-AGE.md`'s raw CSV (`results/sweep_age.csv`) shows `seed 0`'s K=10 deltas go sub-zero at cycle 60 (ratio 2) and cycle 70 (ratio 4), `seed 1` from cycle 80 (ratio 3), and the sub-zero class persists at 150c as well as 300c+. The aliasing arm names the *surface* of the failure (old literals, high demand age); the constraint arm names the *eviction* (recency-truncate = the K-window's eviction). What's missing is the *fix*: pinning the literal that the window would evict. The K-recency hard window's failure is the eviction; the pinning analog (per the constraint arm's pinned-state restoration) is the only mechanism in the study that restores protection at 0.00 violation. The RFC's guidance (RFC-GUIDANCE-20261105.md, section on the pinned exact-literal path) already commits to the analog: the OLD-literal pins at ~0.18% token cost (~18 tokens vs the field's ~47).

**Falsifier:** If a recency-pinned variant *loses* protection on per-seed occurrence-count / recurrence / recency metrics — i.e., if the per-seed onset of sub-zero deltas is carried by a seed's occurrence pattern rather than its recency, a pinning that is fixed on recency alone fails — the mechanism is refuted. Concretely: pin the literal by occurrence-count (seed × literal, count ≥ threshold), not by recency (last K observations). Measure whether per-seed sub-zero onset shifts with the pinning rule. If the pinned variant keeps min delta ≥ 0 at 300+ for every seed under the same gate letter, the mechanism holds; if some seeds still fail, the pin must be occurrence-weighted, not recency-weighted.

**The one measurement that would move it:** a per-seed occurrence-count / recurrence / recency panel — the same `results/sweep_age.csv` columns but with a pinned-archival row per seed, computed at cycles 60/80/100/…, giving the per-seed onset threshold for sub-zero deltas under (a) K=10 only, (b) K=10 + recency-pin (last K), (c) K=10 + occurrence-pin (count ≥ N). The table is small (25 seeds × 4 cycles × 3 arms), instant to compute, and directly tests the falsifier.

---

## 3. The convergence read — what the adjudication implies for the RFC's proposal pieces

**3.1 The K-recency hard window.** The means' erosion (+23.9 → +0.6pp at 4x) is a real finding: the window's protective margin compresses as demand age shifts older, and the window is the same eviction class as recency-truncation. The hard window as proposed should be replaced by the *measured shape*: the K-window works where the quoted literal is recent; it fails where the demand age outgrows the window AND the latent survival coin misses. The window should be replaced or augmented with an exact-literal pinning arm (3.2), not left as a bare recency cutoff.

**3.2 The provenance-origin.** The constraint arm confirms that provenance tags survive only when pinned (pinned arm = 0.00 violation for all strategies). The non-pinned arms (recency-truncate 1.00, hierarchical 0.25, summarize-as-rule 0.00, head-retain 0.00) show that provenance-origin is only as durable as the eviction class that attacks it. The proposal's provenance-origin piece is sound *only* on the pinned analog; on the current K-recency window it is not protected.

**3.3 The archive-before-stub.** The archive's FAIL is a constructional instrument-limit, not a clean finding. The budget knob admits only the demanded literal's ID. The convergence read is that the archive-before-stub needs the competing-admission probe (3.2) before it can be certified; a store that only ever admits the demanded literal is a stub, not a store. The convergence is clear: the gating mechanism should be *pinned lifecycle control* (write → lock → review) plus *query-time recall* with a competing-admission test, not bigger budgets at write time. The field's StageMem/DSGC shape, measured here at the constraint-arm's 0.00, is the honest guarantee class for what's pinned; what isn't pinned is subject to calibrated abstention (the latent floor).

**3.4 The ruler's fix.** The 300+ gate's probe had the scope bug (the fix's scoping proof valid in both instruments); the gate remains the RFC's standard; the fixes apply to the probe, not the bar. The one-line summary: the hard window fails on the floor's excursions at every horizon, the scaled window fails (NO), the modeled competition class fails to explain the excursions (NOT-CONFIRMED, instrument-limit), and the archive fails every tested budget (FAIL, constructional). The mechanism that converges on all of them is the recency-truncate eviction class — named by the constraint arm, quantified by the demand-age arm, and the target of the next mechanism (exact-literal pinning).

---

*Register: receipts, never claims. No meters spent; no model credentials. Quoted lines all from the study branch `study/rfc-143379-rig-20261105` (`studies/rfc-143379-rig/krecency/`, `RESULTS-*.md`, `probe_*.py`, `SYNTHESIS.md`, `RFC-GUIDANCE-20261105.md`, `RESULTS-AGE.md`, `RESULTS-COMPETE.md`, `RESULTS-ARCHIVE.md`, `RESULTS-CONSTRAINTS.md`, `RESULTS-ALIASING.md`).*
