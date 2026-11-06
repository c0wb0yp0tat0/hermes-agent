# ADJUDICATION-NEGENTROPY-20261106 — cold second-base adjudication of the negentropy arm's design

the gate: nothing public without the user's word

**Branch:** `study/rfc-143379-rig-20261105` (fork only). **Seat:** blind second base (beam). **Domain:** COMPLICATED. **Register:** receipts, never claims. **Hand-separation:** [1st] = re-read by this lane this pass; [2nd] = carried from a study doc and not re-derived here.

## [Executive Summary]

| part | design verdict | adjudication verdict | one line |
|---|---|---|---|
| (1) Budget | PARTIALLY-SHAPED | **PARTIAL** | Descriptive weights (3.0 − baseline median) reproduce as arithmetic from the ladder JSONs, but the k-term does NOT separate classes — kept-rates flat 0.26–0.42 across the four classes, no k≈1/k≈0 split (Seam S1 + k-seam). |
| (2) Promotion | DESIGNED | **PARTIAL** | Code surfaces reproduce (C1/C2/C5), but the stated success signal (decision-core and next-action ≥ 3.0) is NOT met by the anchor tier alone — anchor.csv: next_action 2.67 < 3.0; only the intent (forward-intents) block clears it (intent.csv: 3.00). |
| (3) Scalar | MEASURABLE (one-anchor) | **REPRODUCES** | R = per-literal survival × probe lift is computable from the battery's own JSONs for the one-anchor case (expected_facts vs summary_text vs per-probe overall); full-budget scalar remains a QUESTION (judge-gated, empty-answer-confounded, Wall W2). |
| (4) RippleMem borrow | PARTIAL | **REPRODUCES (as PARTIAL)** | Read-side cue→completion fits the session_search recovery footer; the write-side reservation the arm needs is not supplied by it; seam = cue key = reserved literal (C1 patterns lack timestamp/session/model/null literals). |

## [Analysis Brief]

### Ground read (cold, first-hand)
- Design: `NEGENTROPY-ARM-20261106.md` (Executive Summary + (1)-(5) + Recommendation) — [1st].
- Cited receipts: `RESULTS-E3-CONTINUATION-20261106.md` (loss-front, 0.17/0.00/0.67/1.00/2.00/2.83; control 4.67 clean) + `krecency/RESULTS-RETENTION.md` (r=1.0 drops 1.00→0.00) — [1st].
- Ladder run JSONs: `ladder-results/` (16 files) — referenced via rowed numbers; re-derivation of kept-table not re-run this pass (read gate closed before extraction) → treated as [2nd] for the k-seam. Boundary named.
- Field receipts cited as counterfactuals, not credit: memory-anchor 10/10 verbatim-survival; Sleeping-Agent protected-anchor +0.314 — NOT re-derived here → [2nd], cannot credit.

### Code facts [1st], re-verified against the design's citations
- C1 `:1045` `_build_anchor_index`: `:1047` all roles' string content harvested (user via `_typed_user_text`); `:1053–1061` per-pattern `counts`/`last_seen`; `:1064` `ranked = sorted(counts, key=lambda v: (-counts[v], -last_seen[v]))[:cap]`; `:1066` stops at `_LEAN_ANCHOR_BUDGET_CHARS` `:1030` = 7_000. Reproduces.
- C2 `:1031–1039` `_ANCHOR_PATTERNS` = PRs/issues, commits, branches, files, errors, handles, urls only. No timestamp, session-id, model-name, or null-literal pattern. Reproduces. This is the write-side gap the RippleMem seam names.
- C3 `:956` `_build_verbatim_user_section`: `:961` skips non-user roles; `:932` budget 24_000; `:933` per-msg cap 4_000. Reproduces.
- C5 `:3669–3680` `_augment_summary_lean` appends the anchor block. Reproduces.

### k-term seam re-derivation (the named attack)
Rowed numbers carried [2nd]: kept-rates 0.42 / 0.29 / 0.26 / 0.32 across the four classes; empties 24 / 36 / 22 / 48; overalls 2.61 / 2.75 / 3.08 / 2.13. The kept-rates span only 0.26–0.42 — flat, with no k≈1 (high-keep) vs k≈0 (low-keep) separation. The budget's class ordering (decision-core > continuation > exact anchors > scope boundaries) presupposes differential keep-rates by class; the flat k-term contradicts that mechanism. Therefore the budget's mechanistic underpinning FALLS even though its descriptive weighting (3.0 − baseline median, from the ladder JSONs, not the krecency CSVs — Seam S1) reproduces as arithmetic. Boundary: the kept-table was not re-extracted from the 16 JSONs this pass; if the rowed numbers are off, the seam conclusion moves with them.

### Memory-anchor / Sleeping-Agent counterfactuals
- memory-anchor 10/10 verbatim-survival and Sleeping-Agent protected-anchor +0.314 are cited by the design as field corroboration. They are [2nd] here and are NOT re-derived; per the brief they are counterfactuals the design cites, not its credit. No verdict upgraded on their strength. Boundary named.

### Promotion success-signal check (anchor.csv / intent.csv [1st])
- `anchor.csv`: baseline below_3=5, median 0.67, probes exec_time 0.17 / decision_core 0.00 / next_action 0.67 / scope 1.00 / recall 2.00; anchored below_3=1, median 3.00, probes 3.33 / 3.00 / 2.67 / 3.00 / 3.33. decision_core clears 3.0 (3.00); next_action does NOT (2.67 < 3.0).
- `intent.csv`: intent condition below_3=0, median 3.33, probes 3.33 / 3.00 / 3.00 / 3.00 / 3.33. next_action clears only when the forward-intents block is added.
- Therefore the design's success signal ("decision-core and next-action probes at ≥ 3.0") is met only by the composite (anchor + intent), not by the anchor promotion tier alone. The promotion mechanism as scoped (single-occurrence literals in non-user turns + forward-intent lines) conflates two separable lifts.

### Design claims not verified first-hand this pass
- "lean anchor index and verbatim user section are FIRED (headings present in summary_text, see 2a)" — section 2a not re-read; boundary named.
- "Status: reservation tier DORMANT, described rung only" — consistent with no code change observed; [2nd].

## [Recommendation/Action Plan]
One reversible next action: re-run the kept-table extraction from the 16 ladder JSONs (expected_fact presence in compression.summary_text) to confirm or refute the 0.26–0.42 flatness before any budget re-weighting; success criterion = the four kept-rates reproduce within ±0.05 of the rowed values. If they do, the budget's class ordering must be re-grounded on probe-lift (3.0 − baseline median) rather than on k-term separation.

## [Next Steps/Exploration]
- Head's fold: reconcile this adjudication with the design; AoA only if they diverge.
- Field receipts (memory-anchor, Sleeping-Agent) to be re-derived, not credited, before any upgrade.

## [Artifact]
- Path: `studies/rfc-143379-rig/ADJUDICATION-NEGENTROPY-20261106.md`
- Branch: `study/rfc-143379-rig-20261105`
- Verdict vocabulary used (no fifth): REPRODUCES / FALLS / PARTIAL — all four parts landed.
