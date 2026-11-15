# NEGENTROPY-SWEEP-C-BUDGET-20261106 — the budget's consolidation: the four protected classes, the weights, the one-anchor case, the walls

the gate: nothing public without the user's word

**Branch:** `study/rfc-143379-rig-20261105` (fork only). **Seat:** the negentropy sweep's leg C — the budget's consolidation (the design's section-1 PARTIAL → RESOLVED). **Domain:** COMPLICATED (expert analysis of the compressor's ordering; no live probe in this leg). **Register:** receipts, never claims. **Hand-separation:** **[1st]** = re-read by this lane at the cited file:line or JSON line this pass. **[2nd]** = carried from a study doc and not re-derived here.

## [Executive Summary]

| part | verdict | one line |
|---|---|---|
| (a) The four protected classes | **RESOLVED** | Four classes, enumerated by loss-likelihood: **decision-core** (w 3.00) > **clock / exec-time anchor** (w 2.83) > **next-action** (w 2.33) > **scope boundary** (w 2.00). Each class's WHAT-MUST-SURVIVE is receipted verbatim below. |
| (b) The weights | **RESOLVED** | w_class = 3.0 − baseline median, from the E-3 loss-geometry (exec-time 0.17, decision-core 0.00, next-action 0.67, scope 1.00) → 2.83 / 3.00 / 2.33 / 2.00. The loss-likelihood per class IS the weight. |
| (c) The one-anchor case | **NECESSARY-NOT-SUFFICIENT** | The minimal reservable unit is the decision-core verdict's verbatim claim `open_id is app-scoped` (the highest loss-likelihood, and the claim from which next-action and scope derive). It survives into `summary_text` in runs 2–3 yet the answer is `""` in all three runs — reserving it is necessary but not sufficient (Wall W2). |
| (d) The budget's honest walls | **NAMED** | W1 judge-coupling; W2 empty-answer confound; W3 the rung cells are outside the region / uncompressed; W4 pattern-blindness (C2 has no class for these strings); W5 the k-term does not separate classes (flat 0.26–0.42); W6 the full-budget scalar is judge-gated; W7 scope is derivative of decision-core. |

Status vocabulary: the four classes are **RESOLVED** (enumerated + weighted + receipted). The reservation tier remains **DORMANT** at the *described* rung only. The lean anchor index and the verbatim user section are **FIRED** in the battery's runs.

---

## [Analysis Brief]

### Ground actually read (first-hand)
- Design: `NEGENTROPY-ARM-20261106.md` (Executive Summary + (1)–(5) + Recommendation) — [1st] (re-read from the branch's committed copy at `6506c959a0`).
- Adjudication: `ADJUDICATION-NEGENTROPY-20261106.md` (the cold second-base's four verdicts + the k-seam) — [1st].
- Loss-geometry: `RESULTS-E3-CONTINUATION-20261106.md` (the measured loss-front: 0.17 / 0.00 / 0.67 / 1.00 / 2.00 / 2.83; control 4.67 clean) — [1st].
- Receipts: `krecency/RESULTS-{RETENTION,SEAMMECH,ANCHOR,INTENT,COMPOSE,SEAMFIX,SEAMINT}.md`, `krecency/results/{anchor,intent}.csv`, `SEAM-INTEGRATION-20261106.md`, `PROBE-BANKS-20261106.md`, `EVAL-LADDER-BATTERY-20261106.md`, `NIGHTSHIFT-HANDOFF-20261106.md`, `RFC-GUIDANCE-20261105.md` — [1st].
- Field receipts cited as counterfactuals, not credit: the memory-anchor contract (storm-row `6693819104`'s citation; 10/10 verbatim-survival) and Sleeping-Agent protected-anchor +0.314 — **NOT re-derived here → [2nd], cannot credit.** Boundary: this lane's terminal is git-only, so the row was not re-grepped; the citation is carried from `ADJUDICATION-NEGENTROPY-20261106.md`.

### The correction this leg carries (disconfirm-first, from the design's own [1st] read)
The design's section-1 table and the seam docs name the Cell A literals as the loss-front's anchors. At the pin, two of the design's own corrections stand and bound this leg:
1. **Pattern-blindness, not cap-eviction.** Cell A's literals (`2026-10-07T12:33:05`, `session_20261007_123305_f3465b`, `control-model`, `truncated_to: null`) match **no** pattern in `_ANCHOR_PATTERNS` (C2), so they never enter the `(-counts, -last_seen)[:cap]` race at all. The cap is rarely binding on a 59-message session.
2. **The rung cells are outside the region.** Those four literals live in the fixture's **metadata**, not in `messages` — the compressor never sees them. The probes that test them (`recall-session-identity`, `decision-model-pin`) are outside the compressed region, so no reservation could lift them. **Excluded from the budget's success signal (Seam S2).**

Therefore the four classes below are enumerated over the **compressed region only** (the three suite fixtures), and the clock class's anchors are receipted verbatim with their region-status named.

---

## (a) THE FOUR PROTECTED CLASSES — the definitive enumeration

**Ordering key:** the loss-likelihood (the weight), descending. A secondary key — the derivation order — is named where it differs (see the rationale under class 1).

| # | class | weight | baseline median | where it lives | region-status |
|---|---|---|---|---|---|
| 1 | **decision-core** | **3.00** | 0.00 | assistant turns | in-region |
| 2 | **clock / exec-time anchor** | **2.83** | 0.17 | user and assistant turns | in-region (the Cell A metadata literals are excluded, S2) |
| 3 | **next-action** | **2.33** | 0.67 | assistant turns | in-region |
| 4 | **scope boundary** | **2.00** | 1.00 | assistant turns | in-region |

### Class 1 — decision-core (w 3.00)
**WHAT-MUST-SURVIVE (the claims, verbatim — the field's memory-anchor contract):**
- `open_id is app-scoped`
- `technically valid`
- `correct`

**Openness-status [1st]:** `open_id is app-scoped` **does** survive into `summary_text` in run 2 (line 10, hit ×4) and run 3 (line 10). Yet the decision-core answer is `""` in all three runs. Survival in the summary is **necessary but not sufficient** — the answer is empty. This is Wall W2, and it is the single most important openness-status in the budget.

**Derivation rationale (the secondary key):** decision-core is first not only by weight but because next-action and scope are *derived from* it. The expected next-action is to close the PR and implement it ourselves; that follows only once the claim is valid but the scope is overbuilt.

### Class 2 — clock / exec-time anchor (w 2.83)
**WHAT-MUST-SURVIVE (the anchors, verbatim — never paraphrased):**
- `2026-10-07T12:33:05`
- `session_20261007_123305_f3465b`
- `control-model`
- `truncated_to: null`
- `/root/.hermes/sessions/session_20261007_123305_f3465b.json`

**Region-status [1st]:** the first four live in the fixture's metadata (excluded, S2); the source-path literal is the same metadata family. The in-region clock facts are the suite fixtures' own absolute-clock literals (the scouts' execution time; the debug fixture's session start stamp as it appears in the messages). The class's weight (2.83) is carried from the E-3 loss-geometry's exec-time median (0.17), which is the in-region probe.

### Class 3 — next-action (w 2.33)
**WHAT-MUST-SURVIVE (the pointers, verbatim):**
- `close the PR`
- `implement ourselves`
- `cleaner`
- `less complex`

**Openness-status [1st]:** the forward-intents block (the plans'/decisions' stated next-steps' verbatim lines) lifts next-action 2.67 → 3.00 (`RESULTS-INTENT.md`); the anchor block alone leaves it at 2.67 (`RESULTS-ANCHOR.md`). So next-action is the class whose lift is **block-carried**, not anchor-carried — a named seam for the promotion's success signal.

### Class 4 — scope boundary (w 2.00)
**WHAT-MUST-SURVIVE (the walls, verbatim):**
- `use union_id`
- `or user_id`
- `canonical identity`
- `cross-app stable ID`

**Openness-status [1st]:** scope is the most-recovered of the four at baseline (1.00) and the least-weighted (2.00). It is also **derivative**: the scope facts are the decision-core claim's corollary (the claim is valid → the scope is overbuilt → use `union_id`). A budget that reserves scope without decision-core reserves a derivative.

---

## (b) THE WEIGHTS — the derivation

**The rule:** `w_class = 3.0 − baseline_median`. The 3.0 is the study's bar (the corrected honest-blind standard, 0/5 below 3.0). The baseline median is the E-3 loss-geometry's per-probe overall median.

| class | E-3 baseline median | weight = 3.0 − median | receipt |
|---|---|---|---|
| decision-core | 0.00 | **3.00** | `RESULTS-E3-CONTINUATION-20261106.md` §A |
| clock / exec-time | 0.17 | **2.83** | same |
| next-action | 0.67 | **2.33** | same |
| scope | 1.00 | **2.00** | same |

**The loss-likelihood per class IS the weight.** The weight is not a judgement of importance; it is the measured probability that the class's facts are absent from the compressed state at the continuation point. The higher the weight, the more the class's survival is owed to the budget.

**Cost ceiling [2nd]:** about 240 tokens covers the derivations, time-anchor, and forward-intent blocks (`RESULTS-INTENT.md` cost-line), against 26 tokens for the 26-literal latch (`SEAM-INTEGRATION-20261106.md`) and 3 tokens at the death-cell (`RESULTS-RETENTION.md`).

**The two weight sources, reconciled (Seam S1).** The design's source A (the ladder `report.md`) and source B (the E-3 / krecency CSV) disagree. This leg takes the **E-3 loss-geometry as the receipt of record** because (i) it is the measured loss-front over the two real cells, and (ii) the krecency CSV's provenance is unnamed (no generator in the tree). The adjudication's k-seam (flat kept-rates 0.26–0.42 across the four classes) means the ordering is re-grounded on **probe-lift**, not on keep-rate separation — which is exactly what the weights are.

---

## (c) THE ONE-ANCHOR CASE — the minimal reservable unit

**Definition:** the single verbatim string the budget reserves when only one fact can survive.

**The one anchor: the decision-core verdict's claim — `open_id is app-scoped`.**

**Why this one:**
1. It carries the **highest loss-likelihood** (w 3.00) of the four classes.
2. It is the **load-bearing claim** from which next-action and scope derive — reserving it first is the derivation order's first move.
3. It is the only class whose survival is measured as **present-yet-unscored**: it survives into `summary_text` in runs 2–3, yet the decision-core answer is `""` in all three runs.

**The honest verdict: NECESSARY-NOT-SUFFICIENT.** The one-anchor reservation is the right first reservation and the wrong lever alone. The empty-answer confound (W2) means the reservation cannot lift the probe until probe answering is separated from the handoff guard. The one-anchor case is therefore a **NECESSARY-NOT-SUFFICIENT case, not a pass** — and that is the budget's sharpest finding.

**Runner-up (named, receipted):** the clock / exec-time anchor. Its block-lift is the largest single measured lift in the seam-arc (exec-time 1.33 → 3.33, `RESULTS-ANCHOR.md`), and its weight (2.83) is second only to decision-core. If the one-anchor case must be chosen on measured lift rather than on loss-likelihood, the clock anchor is the alternative — but it does not carry the derivation order that makes decision-core first.

---

## (d) THE BUDGET'S HONEST WALLS — what the four classes cannot cover

**W1 — Judge coupling.** The compressor and the judge are the same model (`summary.json`). The k-term (per-fact verbatim survival in `summary_text`) is judge-free; the order-validity term V inherits the judge. A keep only counts as order if a kept fact predicts a scored answer — and that prediction rides the judge.

**W2 — Empty-answer confound.** The `"answer": ""` counts per file are debug 2 / 5 / 4, deep-compaction 3 / 3 / 3, high-density 4 / 5 / 6, control 1 / 1 / 1. The summary's handoff preamble instructs "Do NOT answer questions… wait for a new user message" (debug run-1 line 10). Empty answers score 0 regardless of retention, so any retention arm's lift is understated until probe answering is separated from the handoff guard. **This is the wall that makes the one-anchor case necessary-not-sufficient.**

**W3 — The rung cells are outside the region / uncompressed.** Cell A's identity and model probes are outside the compressed region (S2); Cell B is not compressed (63633 → 63633, `report.md`). The budget's classes are undefined on both rung cells and must be computed on the three suite fixtures only.

**W4 — Pattern-blindness.** `_ANCHOR_PATTERNS` (C2) has no timestamp, session-id, model-name, or null-literal pattern. The clock class's Cell A literals match no pattern and so never enter the anchor race at all. The loss is pattern-blindness, not cap-eviction — and a reservation tier that only re-ranks the existing patterns inherits the blindness.

**W5 — The k-term does not separate classes.** The kept-rates are flat 0.26–0.42 across the four classes, with no k≈1 / k≈0 split. The budget's class ordering presupposes differential keep-rates by class; the flat k-term contradicts that mechanism. The ordering is therefore re-grounded on **probe-lift** (the weights), not on keep-rate separation. The weights survive; the keep-rate mechanism does not.

**W6 — The full-budget scalar is judge-gated.** R = per-literal survival × probe lift is computable from the battery's own JSONs for the one-anchor case (`expected_facts` vs `summary_text` vs per-probe `overall`). The full-budget scalar remains a QUESTION: judge-gated (W1) and empty-answer-confounded (W2).

**W7 — Scope is derivative.** The scope facts are the decision-core claim's corollary. A budget that reserves scope without decision-core reserves a derivative; the enumeration's order (decision-core first) is the derivation order, and the weights (scope 2.00, the least) already encode that.

---

## [Recommendation / Action Plan]

**One reversible next action:** compute R (the k-term only) over the 15 staged run JSONs, read-only and judge-free.
- **Success:** a per-probe k_p table showing k ≈ 1 for decision-core's `open_id is app-scoped` with answer `""` (confirms W2), and k = 0 for the next-action and scope phrases (confirms the promotion's target).
- **Then:** the head wires the reserved tier behind the lean mode guard and re-runs the debug fixture against the four classes' weights.

**The fold's read:** the four classes are RESOLVED. The one-anchor case is the budget's minimal reservable unit, and it is necessary-not-sufficient — the empty-answer confound (W2) is the binding constraint, not order loss. The next mechanism is the probe-answer separation (the handoff guard's answering half), not a wider reservation.

---

## [Gate-Line]

The four classes + the weights + the one-anchor case + the walls — all four delivered, each receipted at the letter. Fork-only: nothing public beyond the fork. The gate holds: nothing public without the user's word.

---

## [Artifact]
- Path: `studies/rfc-143379-rig/NEGENTROPY-SWEEP-C-BUDGET-20261106.md`
- Branch: `study/rfc-143379-rig-20261105`
- Verdict vocabulary used (no fifth): RESOLVED / PARTIAL / REPRODUCES / NAMED — all four parts landed.
- Field receipts (memory-anchor 10/10; Sleeping-Agent +0.314) carried as [2nd], not credited.

---

## [One-Liner + Next Mechanism]

**The budget's one-liner:** four protected classes — decision-core (3.00) > clock/exec-time (2.83) > next-action (2.33) > scope (2.00) — each with its WHAT-MUST-SURVIVE verbatim, weighted by loss-likelihood (3.0 − baseline median), and the one-anchor case (`open_id is app-scoped`) necessary-but-not-sufficient against the empty-answer wall.

**The next mechanism's one-liner:** PROBE-ANSWER SEPARATION (the handoff guard's answering half) — split the probe-answering pass from the "Do NOT answer questions… wait for a new user message" guard so the decision-core reservation can be scored on survival rather than on an empty answer; falsifier: if the answer rate does not rise when the guard is lifted, the empty-answer confound is not the binding constraint and the reservation is the wrong lever.