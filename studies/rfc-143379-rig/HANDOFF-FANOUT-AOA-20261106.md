# HANDOFF-FANOUT — eye 3 (the AoA lens) — adjudication of NIGHTSHIFT-HANDOFF-20261106.md

**Lane:** copycat (beam base). **Artifact:** `studies/rfc-143379-rig/HANDOFF-FANOUT-AOA-20261106.md`.
**Register:** receipts, never claims. Every number below is read from the named source file; no predecessor's words taken as fact.

## 0. The one line

The handoff-doc carries the verified state, the nexts, and the doors; three spot-checks from the sources hold; the successor-facing prose needs an em-dash pass before it leaves the building; vote READY-FOR-THE-NEXT with the 0.15 residual seam logged, not blocking.

## 1. Three independent spot-checks (from the sources, never the predecessors')

### Spot-check 1 — the demand-age gate's FAIL is a finding, not an instrument artifact
Source: `probe_age.py` + `RESULTS-AGE.md`.
- `K=0` returns the constant floor (`if k == 0: return floor`, `FLOOR = {2: 0.30, 4: 0.204, 8: 0.156, 16: 0.151, 32: 0.14}`).
- `K=10` scores `1.0` only when `q in snap` (the literal is still inside the tail window `stream[-k:]`); a miss survives with probability `floor`.
- Query index `idx = max(0, n - 1 - age)` with `age = 1 + int((cycle_idx / 10.0) ** 1.3)`; `n = max(ratio + 1, cycle_idx)`.
- Per-cell delta is therefore one of `{1 - floor, 0, -floor}`; a `-floor` cell is a real missed literal.
- `RESULTS-AGE.md` records them as seed-universal at every horizon: all 25 seeds at 4x/300c+.
- Worst-case min -20.40pp at 4x (mean +0.60); -30.00 at 2x; means' erosion 4x +23.87 -> +0.60.
Verdict: the doc's "FAIL at every horizon >=300" and the exact-literals hold against the source. **CONFIRMED.**

### Spot-check 2 — recurrence-aware exact-literal pinning PROTECTS (0.15)
Source: `probe_pinning.py` / handoff A1 pinning row; onset test.
- At the confirmed aliasing x proximity pair-ON cell, deep-minima prevalence drops from 1.00 (recency-pinned variant) to 0.15 under recurrence-aware exact-literal pinning.
- The onset-test explains why: per-seed onsets differ (seed 0: cycle 68; seed 1: cycle 87); per-seed occurrence predicts the onset, a recency-only pin lags it.
- Cost: 18 tokens vs the field's ~47, ~0.18% at production scale (the raw 9.84% was the sim's 183-token denominator, superseded).
Verdict: the doc's "PROTECTS ... to 0.15" and the onset explanation hold. The 0.15 residual is a real seam, not a rounding artifact. **CONFIRMED.**

### Spot-check 3 — the archive arm is REFUTED under its stated (optimistic) conditions
Source: `probe_archive.py` + repair commit `9c3e89566d` (19,800 rows).
- Archive puts every literal (`for t in stream: arch.put(t[1])`) — the optimistic bound (ID-known recall).
- Recall looks up only the demanded literal's id (`aid = arch.id_of.get(q)`), so the budget knob never admits a competing literal: the budget is toothless in the modeled world.
- Two further inertias: `rlimit` is per-cycle but there is one query per cycle; `max(1, mat_budget_tokens)` grants one recall even at 0% budget.
- The competing-admission repair (`9c3e89566d`, 19,800 rows) does not clear the gate: deep minima persist at the taxed budgets.
Verdict: the doc's "FAIL -> REFUTED under the tested construction" and "archive class closed" hold. The toothless-knob mechanism is the constructional part; the repair's non-clearance is the real part. **CONFIRMED.**

## 2. The completeness-check (CTO perspective: does the successor have the state + the nexts + the doors?)

- **State:** present. Part A of the handoff is the complete state-inventory — the verdicts' map (8 instruments with exact-literals), the pinning counter's protected number, and the superseded 9.84% -> 0.18% cost correction. Traceable to the thread, the ledger, or a live read.
- **Nexts:** present, but split. The ranked fire-order and the exact first-turn sequence live in `SHIFT-LAUNCH-PACK-20261106.md` (floor, `452e479e18`), which the handoff names as the midnight-operable floor and points to via the binding reading order. The handoff itself carries the sustain-conditions and the next-shift's fire-order reference. A successor reading only this doc gets the state and the pointer; the executable nexts require the launch-pack step. That is by design (floor vs. house), but it is a seam worth naming.
- **Doors:** present. Binding reading order is stated: this design -> the launch-pack (the floor) -> the thread end-to-end -> the seed. The two-part grounding contract's part one (thread end-to-end) is named.

Completeness verdict: **COMPLETE**, with one seam — the executable fire-order is one document away (launch-pack). Not a blocker; the pointer is explicit and binding.

## 3. The voice-note (successor-facing prose: human, handles-only)

- The handoff's successor-facing lines (the one-line, the reading order, the floor/house framing) are direct and declarative. Good.
- The doc body uses em dashes and bold headers/tables heavily. That is acceptable for an internal design document, but it is not the user's posted register (voice profile: no em dashes; no bold headers/bullet runs where plain paragraphs; no "delve", "it's worth noting", rule-of-three padding).
- Recommendation: before any successor-facing message is drafted from this doc, run a humanize pass that strips em dashes to commas/periods and flattens the bold-header runs. The substance (numbers, pointers, verdicts) carries; only the scaffolding changes.
- No invented flourishes; stay closest to the doc's actual phrasing. The Amazon upstream/downstream origin-style story elements, where present, stay.

## 4. The final vote

**READY-FOR-THE-NEXT.**

The seam is logged, not blocking: the pinning counter protects at 0.15 (not zero) at the confirmed pair-ON cell; the competition arm remains an instrument-limit with the K=10 window-hit path unmeasured; the archive class is closed under the tested construction. None of these invalidate the handoff's state, nexts, or doors. The successor can fire from the first turn on this record. HOLD would only be warranted if a spot-check had failed or a door were missing; neither occurred.
