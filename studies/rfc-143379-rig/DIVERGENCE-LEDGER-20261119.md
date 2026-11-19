# DIVERGENCE-LEDGER-20261119.md — the RELOAD compose's adjudication list (every entry receipt-bound)

*The swap-and-enrich wave's named divergences, assembled for the RELOAD compose. Rule: adjudicate by evidence, never silently pick. Each entry: the claim pair, the evidence, the divergence. The compose adds its verdict per entry.*

## L-1 DIVERGENCES (from L-1-PROBE-DESIGN-ENRICHED-20261119.md, E4/hy4, §6 — `21839b2740`)

- **L1-D1 — EHQ cardinality (3-cell vs 4-cell).** APPENDIX-A.1's EHQ field cells are 3 (ABSTAIN / HEDGE / CONFIDENT); the probe's base abstention axis is 4 (R/H/E/A). Evidence: E is split out in the probe, folded into ABSTAIN in EHQ. Standing proposal: keep the probe's 4-cell partition as the instrument; show EHQ as its 3-cell projection. RELOAD verdict: pending.
- **L1-D2 — axis semantics (certainty vs content-present).** EHQ CONFIDENT encodes *certainty*; the probe's A encodes *content-present*. Evidence: the base §1 stale-confident failure class 5 — confident-but-wrong scores A (lowers the abstention rate, looks like a win) yet is a documented failure. Standing proposal: keep both axes; the abstention-cell × correctness cross-tab is the reconciliation-by-evidence. RELOAD verdict: pending.
- **L1-D3 — F3's two faces (judge-control vs write-time assert).** The base probe design §1 calls F3 the inherited judge mis-scoring gate (run-level, ≥90% on 20); the L-4 instrumentation calls F3 the per-episode write-time assert. Evidence: base failure classes 4 (mis-scoring) vs 5 (stale-confident). Standing proposal: F3a = judge control (run-level) + F3b = write-time assert (per-episode), both retained under one label decision. RELOAD verdict: pending (the canonical label).

## L-2 DIVERGENCES (from L-2-ECONOMICS-ENRICHED-20261119.md, E1/solar, §4 — `c714269929`)

- **L2-D1 — n semantics (per-cell vs per-arm).** L-1's abstention axis requires n=40 *per cell* (the ±15pp binomial bound is per-cell); L-2's contract states "40/arm" which reads as a per-arm total. Evidence: 4 cells × 40 = 160 nominal probes minimum; pooling silently drops the ±15pp claim. Standing proposal: L-1 governs the claim — the economics rows relabel `n_cell = 40`; any deviating n is a priced sensitivity row. RELOAD verdict: pending.
- **L2-D2 — pooling.** Pooling R/H/E/A before a CI re-run silently drops the per-cell ±15pp bound. Standing proposal: pooling is opt-in only with a re-run ledger (two-way door). RELOAD verdict: pending.
- **L2-D3 — cap bindingness ($100 vs 160 probes).** The pre-committed $100 cap is a ceiling on new spend; the probe structure requires ≥160 nominal probes plus the governor's per-episode adds plus the oracle free-surface reconciliation. If probe-gate > $100, the cap is violated before CERTIFY can fire. Standing proposal: split the cap into probe-gate (fixed, ≤$100, pre-committed) and post-CERTIFY runtime budget (uncapped by the gate); CERTIFY unreachable while probe-gate > $100. RELOAD verdict: pending.

## L-3 DIVERGENCES (from L-3-REPORTBACK-FRAMING-ENRICHED-20261119.md, E2/longcat, §3.4.4 — `333c100808`)

- **L3-D1 — "Receipted, not estimated" vs the pre-committed cap.** The tone contract forbids estimates; the cap is a plan number until the spend lands. Resolution by evidence: label the cap *reported-plan* (a third label beside reported/verified); never called a result.
- **L3-D2 — "Nothing is a result until the rerun holds" vs the economics' need to state the cap now.** Resolution by evidence: the cap is stated as *spend*, never as *finding*; the two vocabularies stay in separate clauses.
- **L3-D3 — "agnostic by demonstration" vs single-seat, single-scale.** Resolution by evidence: the demonstration is scoped to the seat and the n actually run; the unqualified word "agnostic" is not used in the draft register.
- **L3-D4 — free-surface $0 cash vs the "$56.04 spent" sentence.** Resolution by evidence: "paid-equivalent $56.04 shadow, $0 cash on the free seat" — the economics denominate the cap in the shadow class.
- **L3-D5 — the class finding reaches beyond the run vs small-scale honesty.** Resolution by evidence: the class finding is labeled a design assumption under test; APPENDIX-A.3 corroborates the pattern; the leg's n=40 does not close it.

## L-4 — E3's seam (from E3-BRIEF-20261119.md; RESOLVED at 13:4xZ UTC, 2026-11-19)

- **L4-S1 — the seat wall (transport, not artifact).** E3 (stepfun) aborted 403 ×3 at ~08:10Z (`enrich-e3-20261119.log`, deterministic abort, wrote nothing); re-fire #1 (solar) also 403 ×3 at ~13:28Z (`enrich-e3-refire-20261119.log`); re-fire #2 (longcat) LANDED `481f4eaf15` (~13:4xZ), sentinel true, scribe byte-identical, placeholder-scan clean, 19.0 KB, rowed on PR #1 (`#7010649298`).
- **L4-S2 — the seam (delivered):** (a) the tone contract translated rule-by-rule into the classifier's guards (the EHQ cell = two-axis join; the hedge-vs-refusal boundary with a deterministic proxy); (b) the governance compliance rate wired as NULL component 1's governance axis (components 2–4 = framing, never flags); (c) the DRAFT-NOT-POSTABLE register met in flags — every flag/label row carries an `audience` field (internal | staged | public; public never emitted by the probe).
- **L4-D1 — C5 merges an epistemic act with a harness event.** Empty output can be truncation/crash/gate-hold, not the seat's restraint. Resolution by evidence in the landed artifact: C5a `NO_OUTPUT` (with `empty_reason = harness|seat|unknown`, re-fire signal when clustered) + C5b `REFUSED` (counts toward hard abstention); numerator composition visible.
- **L4-D2 — "first-match-wins" vs "credit where true."** Hedge+refusal answers: C1 wins by precedence though the hedge is real. Resolution by evidence: determinism kept; the all-matches log carries the tie (the "receipted" discipline).
- **L4-D3 — C6 "substantive content" is a vibe-risk.** Resolution by evidence: the direct-answer-span proxy (§2.2); the substantive judgment moves to the judge's axis.
- **L4-D4 — "gate" overloaded (F2 vs the public report gate).** Resolution by evidence: GATE-INTERNAL vs GATE-PUBLIC; F2's compliance says nothing about the public gate.

## THE ROSTER FACT (DEEP-STORM-SEAM-4, fired at dispatch, 2026-11-19 ~13:35Z — measured, not assumed)

- **200 (live):** `deepseek/deepseek-v4-flash-0731` (main), `meituan/longcat-2.5:free`.
- **403 (exists, this key denied):** `qwen/qwen4-max:free` (the deck's planned RELOAD seat — WALLED at dispatch), `tencent/hy4-flash:free`, `upstage/solar-mini4:free`, `stepfun/step-3.7-flash:free`.
- **404 / free-period ended:** `stepfun/step-5-preview:free`, `reflection/beam-1.0-501b-a23b:free`, `meituan/aura-2.5:free`, `hy4-flash:free` (bad alias).
- **Consequence for the RELOAD:** the compose rides `meituan/longcat-2.5:free` (fallback, two-way door: if qwen4-max reopens, re-run the compose there). The leg's later arms re-survey at their dispatch.
