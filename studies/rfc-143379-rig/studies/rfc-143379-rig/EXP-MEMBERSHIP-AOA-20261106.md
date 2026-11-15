# EXP-MEMBERSHIP-AOA-20261106 — the V1-arc's audit-of-audit (the recurrence-carrying pinning-membership's corrected state, 2026-11-06)

**Lane:** copycat (membership-arc). **Artifact:** `studies/rfc-143379-rig/EXP-MEMBERSHIP-AOA-20261106.md`.
**Register:** receipts, never claims. Every verdict rides the bytes read; a number the files don't carry is UNVERIFIED.

---

## 0. The verdict (top of the artifact)

**ADJUST.** The membership-arc's *mechanism* (base exact-literal pinning protects on recurrence-bearing real ground) survives the byte-check; the arc's *record* does not — `RESULTS-MEMBERSHIP.md` still stands under the stale `MEMBERSHIP-CONFIRMED` label and a results table that does not match its own CSV, and the probe's predictor rides a hard-coded onset table. The corrected record (wave 15 replication-refutation + wave 18 real-ground redundancy) contradicts the file's standing label. Corrective notes only; no new mechanism invented.

---

## 1. The byte-checks (quote what was read, name the line/row)

### 1.1 Does `probe_membership.py` hard-code the onsets into its own predictor? — YES (verified)

File: `studies/rfc-143379-rig/krecency/probe_membership.py`.

- Line 6: `SEEDS_ONSET = {0: 60, 1: 80}  # per-seed onset cycles (sub-zero deltas)`
- Lines 19-23:
```
def onset_predict(history, seed):
    # per-seed occurrence predicts onset cycle
    base = SEEDS_ONSET.get(seed, 70)
    occ = sum(t.get("occurrence", 0) for t in history if t.get("membershipned"))
    return base + (occ % 10)
```
The predictor's base-line is the hard-coded onset (`SEEDS_ONSET.get(seed, 70)`); the "recurrence signal" is only `occ % 10` added on top. The recurrence input `occ` is itself drawn from `make_history`, where `occurrence = rng.randint(1, 5)` for the two membershipned literals — i.e. the onset is announced by the constant table, not derived from a blind stream. This is the circularity wave 15 named: the R2 rode the known-onsets' echo. **PASS (as a finding of hard-coding) — the file literally does what wave 15 alleges.**

### 1.2 Do the CSV cells match the `RESULTS-MEMBERSHIP.md` tables? — NO (verified mismatch)

`RESULTS-MEMBERSHIP.md` header table:
```
| uniform | True | True | 1.00 |
| weighted | True | True | 0.15 |
```
and "Per-seed onset: seed 0 = cycle 68, seed 1 = cycle 87" and "CSV: results/membership.csv (200 rows)."

`results/membership.csv` (read in full, 160 data rows + header):
- Header: `seed,mode,alias_on,prox_on,deep_minima_prevalence` — there is **no onset column** in the CSV; the onset cycles are not carried by the CSV at all.
- Mode labels are `recency` / `recurrence`, not `uniform` / `weighted`.
- At `alias_on=True, prox_on=True`: `recency` rows read `0.4` (e.g. seed 0: `0,recency,True,True,0.4`), and `recurrence` rows read `0.1` (e.g. seed 0: `0,recurrence,True,True,0.1`). Not 1.00 / 0.15.
- Row count: 20 seeds × 8 cells = **160 data rows**, not 200. (`RESULTS-MEMBERSHIP.md` says 200.)

The 0.15 / 1.00 figures are not prevalence values in the CSV; 0.15 is the `cnt` cutoff threshold inside `deep_minima_prevalence` (`if val > 0.15: cnt += 1`), and 1.00 is the unprotected multiplier (`base * (0.25 if protected else 1.0)` → 0.4 at the pair-ON cell when unprotected). So the RESULTS table re-labels derived quantities as prevalence. **FAIL (table does not match CSV bytes).**

`results/pin.csv`: same header and same first rows as `membership.csv` as read (head). Full byte-identity not verified under this audit's read window — **UNVERIFIED** (head only).

### 1.3 Does an E2-artifact carry R2 = 0.0000 (n-panel) and weighted = uniform = 1.0000? — NOT FOUND (stated honestly)

Hunt performed over the study tree for `R2`, `n-panel`, `onset`, `sub-zero`: the readable surfaces (`krecency/SYNTHESIS.md`, `RECEIPTS.md`, `CONVERGENCE-VOI-SORT.md`, `copycat-findings/copycat-krecency-20261105.md`, `probe_membership.py`, `RESULTS-MEMBERSHIP.md`, `membership.csv`, `pin.csv`) carry no E2-artifact with those rows. No file named `E2*` / `*membership*replic*` was located in the read window. **Conclusion: the study carries no E2-artifact readable by this audit; the R2 = 0.0000 (n-panel) and weighted = uniform = 1.0000 figures arrive only via the brief's restatement of the wave-15 summary. Those two numbers are UNVERIFIED against bytes by this audit.** (The hard-coding finding in 1.1 is verified and is the mechanism wave 15 names, which makes the refutation's *shape* credible, but its *numbers* are not byte-checked here.)

---

## 2. The label-accuracy (ADJUST-class item)

`RESULTS-MEMBERSHIP.md` still reads, at its top: "Verdict: MEMBERSHIP-CONFIRMED. Per-seed recurrence carries per-seed onset (R2 high); recurrence-weighted pinning meets the PROTECTS-bar (weighted 0.15 vs uniform 1.00)."

The corrected record contradicts this standing label:
- Wave 15 (per the brief's claimed chain, and consistent with 1.1): REFUTED-BY-REPLICATION — the onsets are hard-coded, the honest-blind derivation yields R2 = 0.0000 (UNVERIFIED number) and weighted = uniform = 1.0000 (UNVERIFIED number).
- Wave 18 (per the brief): on recurrence-bearing real streams, no-pin 0.80 → literal-pin 0.00 → membership-pin 0.00 — the base pinning PROTECTS; the membership-weighting adds nothing beyond the literal there.

So the file's header label (`MEMBERSHIP-CONFIRMED`) is stale relative to the corrected record. **ADJUST: re-label to REFUTED-BY-REPLICATION / REDUNDANT-ON-REAL-GROUND, and correct the table to the CSV's actual cells (0.4 / 0.1) or remove it.** This is a documentation/label correction, not a mechanism change.

---

## 3. The open value's answered-ness (VOI-sort V1)

V1 asks: "why seed 0 at cycle 68, seed 1 at 87 — the membership's weighting."

- **Answered?** Yes, by wave 15: the onsets are not predicted, they are hard-coded (`SEEDS_ONSET = {0: 60, 1: 80}` plus `occ % 10`), so the membership-weighting carries no predictive signal — the honest-blind R2 = 0.0000 (UNVERIFIED number). The "why" is: there is no learned why; the base-line is injected.
- **Residual (stated honestly):** on recurrence-bearing real ground (wave 18) membership-pin = literal-pin = 0.00 → the weighting is redundant there; the base pinning alone protects. **What the read-side alone cannot certify:** whether there exists a real stream cell where literal-pin leaves a residual that membership-weighting then closes — i.e. a case where the weighting separates from the literal. No such cell is in the record (wave 18 shows equality, not separation). That separation, if it exists, is UNVERIFIED and would require a real-ground run that holds the literal-pin fixed and varies only the weighting.

---

## 4. Per-claim table

| Claim | Byte-evidence | Verdict |
|---|---|---|
| "Per-seed recurrence predicts per-seed onset" (wave 11) | `SEEDS_ONSET = {0: 60, 1: 80}` hard-coded; `onset_predict` uses `base = SEEDS_ONSET.get(seed, 70)` | FAIL (circularity; not derived) |
| "R2 high" | No regression/R2 code in `probe_membership.py`; no E2-artifact located | UNVERIFIED |
| "weighted 0.15 vs uniform 1.00 at pair-ON" | CSV pair-ON cells: recency 0.4, recurrence 0.1; 0.15 is the `cnt` cutoff, 1.00 is the unprotected multiplier | FAIL (table mislabels derived quantities) |
| "CSV has 200 rows" | 160 data rows (20 seeds × 8 cells) | FAIL |
| "seed 0 = cycle 68, seed 1 = cycle 87" | `onset_predict`: 60 + occ%10, 80 + occ%10; occ from `rng.randint(1,5)`; plausible but onset not in CSV | UNVERIFIED (no onset column in CSV) |
| Stale label `MEMBERSHIP-CONFIRMED` | Corrected record (wave 15/18) contradicts | ADJUST (label) |
| Base pinning PROTECTS on real ground (wave 18) | Not in files read (deathreal.csv / probe_deathreal.py not read this audit) | UNVERIFIED (claimed, not byte-checked here) |
| Weighting redundant on real ground (wave 18) | Same as above | UNVERIFIED (claimed, not byte-checked here) |
| LATCH-REAL-NOOP (wave 19) | Not in files read | UNVERIFIED (claimed, not byte-checked here) |

---

## 5. Corrective-only notes

1. Re-label `RESULTS-MEMBERSHIP.md` from `MEMBERSHIP-CONFIRMED` to the corrected state (REFUTED-BY-REPLICATION on the onset claim; REDUNDANT-ON-REAL-GROUND on the weighting claim). ADJUST-class, documentation only.
2. Fix the results table to match `membership.csv` bytes (pair-ON: recency 0.4, recurrence 0.1) or delete it; fix "200 rows" → 160.
3. Remove or fence the hard-coded `SEEDS_ONSET` table; if a blind onset prediction is wanted, derive the base from the stream, not from a constant. (This is the wave-15 corrective, restated — not a new mechanism.)
4. Do not cite the R2 = 0.0000 / weighted = uniform = 1.0000 figures as byte-verified until an E2-artifact lands; they are currently carried only by the wave-15 summary and the brief.

---

## 6. The one next-mechanism line

Alias-aware format-pinning (V3) — the confirmed alias×proximity pair's format-side counter, the record's own next-named vector (per `CONVERGENCE-VOI-SORT.md`) after V1's membership-weighting proved redundant on real ground. (Evidence-to-evidence: base pinning protects on real ground and weighting adds nothing there, so the remaining untested protection surface is the format/aliasing class, not the weighting.)

---

**Artifact path:** `studies/rfc-143379-rig/EXP-MEMBERSHIP-AOA-20261106.md`
**Branch:** `study/rfc-143379-rig-20261105`
**Credit:** receipts, never claims — every number above is either quoted from a named file or marked UNVERIFIED.
