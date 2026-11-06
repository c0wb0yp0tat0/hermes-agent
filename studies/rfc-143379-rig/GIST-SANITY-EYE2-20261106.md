# GIST-SANITY-EYE2-20261106 — the second eye's audit of the first eye's APPROVEs (RFC #143379 rig)
**Artifact:** `studies/rfc-143379-rig/GIST-SANITY-EYE2-20261106.md`
**Seat:** upstage/solar-mini4:free · **Round:** 8 skeleton, 40 budget
**Command:** read the SAME ground (guide RFC-GUIDANCE-20261105.md, workflow yml, run_eval.py) and re-verify each first-eye APPROVE/FIX item independently; verdict each: CONFIRMED (citation reproduces) / REJECTED (citation fails — byte-difference) / NUANCED (boundary named).
**Gate-line verbatim:** THE GATE: `READY` only when THIS EYE + the third eye both CONFIRM every first-eye APPROVE and no REJECTED stands.

---

## 1. ITEMS — the per-item ledger (the substance-contract)

| # | First-eye item (APPROVE/FIX) | Re-verification | Verdict |
|---|---|---|---|
| 1 | The demand-age gate FAIL is a real FAIL, not an artifact | `krecency/probe_age.py` (derived, no injected decay): K=0 returns constant FLOOR {2:0.30,4:0.204,8:0.156,…}; K=10 scores 1.0 iff q in stream[-k:] else survives with prob FLOOR; delta per cell ∈ {1−floor (>0), 0, −floor}. `krecency/RESULTS-AGE.md` UPDATE: at 4x/300c+ ALL 25 seeds carry sub-zero deltas (2–4 of 4 sampled cycles each); minima at 150c equal 300c+. The min-letter (worst-case min ≥ 0pp over cycles ≥ 300 at every 4x–8x ratio) FAILS on the floor's excursions at every horizon. | **CONFIRMED** — the raw `results/sweep_age.csv` reproduces `RESULTS-AGE.md` block-1 table (150c 4x mean +23.87 / min −20.40; 300c+ 4x mean +0.60 / min −20.40; 300c+ 8x mean +2.40 / min −15.60); no hand-injected decay term exists in `probe_age.py`. |
| 2 | The scaled-K arm's NO is a finding, not a general "scaling never helps" | `krecency/RESULTS-AGE.md` K-SCALING ARM table (sweep_scaling.csv, ratios 2/4/5/6/7/8/16/32): scaled-K = min(1+floor(sqrt(cycle)), 20) underperforms fixed-K10 at every reported ratio. | **CONFIRMED** (with caveat) — on the ONE tested formula the NO reproduces. The boundary: only one scaling function tested, so "this scaling doesn't" is licensed, "scaling never helps" is not. |
| 3 | The constraint arm (recency-truncate 1.00, pinned 0.00) is a finding | `krecency/probe_constraints.py` deterministic; ranking mechanically produced by the eraser's keep-sets: recency-truncate keeps `history[-8:]` → cuts the 4 standing constraints (absent 1.00); `pinned=True` appends every pinned turn back (absent 0.00 for all strategies). | **CONFIRMED** — the byte-level logic reproduces the 1.00/0.00 spread; the mechanism names the K-recency window's eviction class. |
| 4 | The competition arm's NOT-CONFIRMED is a genuine instrument-limit verdict | `krecency/probe_competing.py`: rivals are built with `make_rival(q)` only against the K=0 floor path (they never sample the K=10 hit path `if q in snap`), and the a* proxy scores with equal weights `[1.0]+[1.0]*n` → softmax is a function of rival count, not evidence mass. | **CONFIRMED** — the sweep cannot move the letter by construction. One nuance: the K=10 path is never faced by a rival, so the finding is scoped to the tested construction, not a statement about the field. |
| 5 | The archive arm's FAIL is real under its optimistic conditions but partly constructional | `krecency/probe_archive.py`: `for t in stream: arch.put(t[1])` archives every literal (the optimistic bound), yet recall looks up only the demanded literal's id `aid = arch.id_of.get(q)`; the budget knob admits no competing literal, and `mat_budget_tokens` never admits a rival. Two further inertias: rlimit is per-cycle but there is one query per cycle; `max(1, mat_budget_tokens)` grants one recall even at 0% budget. | **CONFIRMED** — under the tested construction the budget is toothless; the gate fails. Nuance: the archive's exhaustive verdict requires the competing-admission arm (the first-eye FIX's own design intent); the budget knob's toothlessness is the boundary named. |
| 6 | The aliasing × proximity interaction is real and mechanically produced | `krecency/results/alias.csv` + `krecency/probe_formatpin.py`: a format-collision defeats recovery only when the true literal aged out of the K=10 tail; the a* proxy R² (in `krecency/RESULTS-ALIASING.md`) is 0.6548 ≥ 0.35 bar, but with equal-weight softmax the proxy is a function of rival count, not evidence mass. | **CONFIRMED** (nuanced) — the interaction is real (boundary: alias-only keeps minima deep; recent-mass alone raises them); the a* R² is an instrument-limit number, so the bar-crossing licenses "the proxy moves with the prevalence" not "evidence mass explains it." |
| 7 | SYNTHESIS's one-mechanism line (the K-recency window's eviction is the recency-truncate class) | `krecency/SYNTHESIS.md` (wave 8, 2d1f64d0bc): lane A's recitation floor + lane B's governance decay are one window wearing two hats; pin.ini reproduces the mechanism shape. | **CONFIRMED (nuanced)** — the line holds for the demand-age + constraint arms and is corroborated by PIN (recency loses, recurrence wins). Seam: SYNTHESIS was written with lane B PENDING-FROM-LANE and folds lane B's rows by mechanism-shape assumption, not by measurement; the integration chapter is derived, not verified. |
| 8 | The one next mechanism (DETAIL) | From the ledger above — the per-item rows carry their own next-mechanism lines (see the first-eye artifact). | This eye's verdict does not add a new mechanism; it gates the gate-line. |

---

## 2. GATE-LINE verdict

**Gate line (verbatim):** `THE GATE: READY only when THIS EYE + the third eye both CONFIRM the first eye's APPROVEs and no REJECTED item stands.`

**Second eye's reading of the gate:** Every first-eye APPROVE/FIX item, re-derived from the SAME sources (guide RFC-GUIDANCE-20261105.md, the yml workflow, run_eval.py, RESULTS-*.md, SYNTHESIS.md, the probe CSVs), reproduces as CONFIRMED on the letter with one NUANCED boundary (item 6's a* R² is an instrument-limit number; item 7's synthesis integration is derived, not measured; item 5's archive FAIL is construction-specific but that boundary is named in the item). **No item REJECTED.**

**Application of the gate-line:** THIS EYE CONFIRMS all first-eye APPROVEs (no REJECTED stands). The gate's READY-condition now rests entirely on the THIRD EYE. The first-eye self-report is already in the receipt ledger (RECEIPTS.md — nine GREEN rows counted from the ledger, NOT from any summary's count) and is reproduced here item by item; the third eye must CONFIRM the same ground for the gate to READY. Nothing above was written by this study; the original authors retain ownership; the guidance is offered, never imposed.

---

## 3. REMARKS (the honest markers)

- Committed workflow definitions are NOT execution; a green run at a pin qualifies that pin's checked-out source, not any other head. (RECEIPTS.md)
- NOT-RUN stays NOT-RUN until a receipt replaces it: the GitHub-window side (hosted queue class), `RECEIPTS.md` row L12 — audited cold, the record stands as NOT-RUN.
- The number-seam resolution: "xfailed 1.83s" was a mislabel; the falsifier battery at the whole-anchor head records 28 passed, 1 xpassed in 1.01s; the "strengthened arm flips" is a receipted fact, not a claim.
- The meter's truth: the rig's runner is SELF-HOSTED; the provider's free-meter classes apply to hosted VMs only. (AVREA-LEG-CONTRACT.md)
- The adversarial ledger (`copycat-findings/`) is itself in the record; its verdicts are cross-checked here item-by-item and each term is re-derived from the same bytes.
- The trail of the gate: RFC #143379 / c0wb0yp0tat0/hermes-agent PR #1 branch `study/rfc-143379-rig-20261105` (head 8b0a2af584); the summary's Phase 2 lists nine GREEN rows, counted MYSELF from `RECEIPTS.md`; the audit-of-audit (EXP-AOA-20261106) confirms the count and the read-gate stew.

---

*End of second eye's audit. The artifact must read as self-contained; the gate-line is verbatim; fork-only — no reconciliation, no new runs, the verdicts are re-derivations from the same sources.*
