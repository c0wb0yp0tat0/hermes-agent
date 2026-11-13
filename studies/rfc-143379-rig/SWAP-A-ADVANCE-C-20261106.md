# SWAP-A-ADVANCE-C-20261106 — the budget's MINIMUM-RESERVE rule (the one-anchor case, advanced)

**Branch:** `study/rfc-143379-rig-20261105` (fork only). **Lane:** copycat (swap-leg, seat `meituan/longcat-2.5:free`). **Seat:** the negentropy sweep's leg C — the budget's consolidation, advanced one step past `NEGENTROPY-SWEEP-C-BUDGET-20261106.md`. **Domain:** COMPLICATED (expert analysis of the compressor's ordering; no live probe in this leg). **Register:** receipts, never claims. **Hand-separation:** **[1st]** = re-read by this lane at the cited file this pass. **[2nd]** = carried from a study doc and not re-derived here. **Gate:** nothing public without the user's word. **Round-budget:** 40. **Skeleton-by-round-12:** honored (this file is the skeleton, filled in one pass).

---

## 0. The one line

**MINIMUM-RESERVE = the decision-core class, and within it the verdict's verbatim claim `open_id is app-scoped` — the highest loss-likelihood (baseline median 0.00 → weight 3.00) and the generative root from which next-action and scope derive (Wall W7).** The priority-order from the loss-geometry is **decision-core (3.00) > clock / exec-time anchor (2.83) > next-action (2.33) > scope boundary (2.00)**; the one-anchor's failure-profile makes the rule **necessary-but-not-sufficient** — the claim survives into `summary_text` in runs 2–3 yet the answer is `""` in all three runs (Wall W2) — so the rule carries its sufficiency complement: **the next-action / forward-intents block**, the class the anchor-tier alone leaves below 3.0 (anchor.csv 2.67 → intent.csv 3.00).

---

## 1. The MINIMUM-RESERVE rule (the deliverable)

**Rule (the one-anchor case).** When only one anchor can survive the compressor's ordering, the surviving anchor MUST be the **decision-core** class — specifically the decision-core verdict's verbatim claim (`open_id is app-scoped`), the minimal reservable unit named in `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` §(c).

**Priority-order (the four classes, by weight).**

| rank | class | weight | baseline median (loss-likelihood) | source |
|---|---|---:|---:|---|
| 1 | **decision-core** | **3.00** | 0.00 | `krecency/results/anchor.csv` baseline row [1st] |
| 2 | clock / exec-time anchor | 2.83 | 0.17 | same |
| 3 | next-action | 2.33 | 0.67 | same |
| 4 | scope boundary | 2.00 | 1.00 | same |

The weight is `w_class = 3.0 − baseline median` (the design's descriptive weighting, receipted in `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` §(b) [1st]). The loss-likelihood per class IS the weight.

**The rule's two tiers (the honest form).**

- **MINIMUM-RESERVE (1 anchor):** decision-core. Necessary — it is the claim from which next-action and scope derive, and the one whose survival into `summary_text` was observed (runs 2–3).
- **MINIMUM-SUFFICIENT reserve (2 anchors):** decision-core **+ the next-action / forward-intents block.** The one-anchor reservation alone does not lift the answer (Wall W2); the next-action class is the complement that clears the last below-3.0 cell (anchor.csv 2.67 → intent.csv 3.00).

**The rule's mechanism-caveat (the k-seam, named).** The priority-order is **descriptive** (loss-geometry), not mechanistic: the k-term does NOT separate the classes — kept-rates are flat 0.26–0.42 across the four classes, with no k≈1 / k≈0 split (`ADJUDICATION-NEGENTROPY-20261106.md` §k-seam [1st]). The budget's class ordering presupposes differential keep-rates by class; the flat k-term contradicts that mechanism (Wall W5). The rule therefore rests on the loss-likelihood + the generative-root argument (W7) + the one-anchor's failure-profile — **not** on a keep-rate separation that the receipts do not show.

---

## 2. The rationale — why decision-core wins the one-anchor case

### 2.1 The loss-geometry (the priority-order's source)

The measured loss-front (E-3, receipted): the compactors evict the tiny+old anchors while the same machinery at the same depth leaves a structurally similar stream clean (control slice `suite-feature-impl-context-priority` overall median 4.67, misses=[]). The per-class baseline medians are the loss-likelihood: **decision-core 0.00 < exec-time 0.17 < next-action 0.67 < scope 1.00** (`krecency/results/anchor.csv` baseline row [1st]; corroborated by `RESULTS-E3-CONTINUATION-20261106.md` §A [1st]). The decision-core class is the most fragile — its baseline median is the floor (0.00), so its loss costs the most and its reservation buys the most.

### 2.2 The generative root (why the highest-weight class is also the causal root)

The decision-core verdict's claim (`open_id is app-scoped`) is the claim from which the next-action ("close the PR and implement ourselves") and the scope boundary derive (Wall W7, `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` §(d) [1st]). A reservation that holds the root holds the derivation; a reservation that holds only a derivative (next-action, scope) leaves the root unanchored. This is why the priority-order is not merely a loss-likelihood sort — it is a **causal ordering**: decision-core first, then the clock anchor (which the residual pair's shared class confirms — `RESULTS-ANCHOR.md`: the time-anchor block lifts exec-time 1.33 → 3.33 and decision-core 1.67 → 3.00 [1st]), then next-action, then scope (the derivative).

### 2.3 The one-anchor's failure-profile (why the rule is necessary-but-not-sufficient)

The one-anchor case is the budget's hard test: reserve the minimal unit and see whether the answer lifts. The receipt (`NEGENTROPY-SWEEP-C-BUDGET-20261106.md` §(c) [1st]): the decision-core claim **survives into `summary_text` in runs 2–3** yet the answer is `""` in all three runs. So:

- **Necessary:** the claim is the minimal reservable unit — without it the root is unanchored.
- **Not sufficient:** its survival does not lift the answer. The confound is Wall W2 (the empty-answer / handoff-guard confound), which the W2-isolation run-design (`W2-ISOLATION-RUN-DESIGN-20261107.md` [1st]) names as the settle-condition: the guard, not retention, may be nulling the answers.

The sufficiency complement is receipted by the A/B ladder: the anchored condition (time-anchor block) lifts decision-core 0.00 → 3.00 and exec-time 0.17 → 3.33 but leaves **next-action at 2.67 < 3.0** (`krecency/results/anchor.csv` anchored row [1st]); adding the forward-intents block lifts next-action 2.67 → 3.00 and clears all five probes (`krecency/results/intent.csv` intent row [1st]). So the one-anchor decision-core reservation is the minimum NECESSARY reserve, and the **decision-core + forward-intents pair is the minimum SUFFICIENT reserve** on this battery's evidence.

### 2.4 The cost-line (the reserve's price)

The lean anchor index and the verbatim user section are **FIRED** in the battery's runs (`NEGENTROPY-SWEEP-C-BUDGET-20261106.md` status vocabulary [1st]). The cost-lines receipted: time-anchor block ~60 tokens (~0.6% of a 10K context); composed blocks ~180 tokens (~1.8%); cumulative with forward-intents ~240 tokens (~2.4%) (`RESULTS-ANCHOR.md` / `RESULTS-COMPOSE.md` / `RESULTS-INTENT.md` cost-lines [1st]). The one-anchor minimum-reserve's cost is the decision-core claim's verbatim bytes (single-occurrence literal, ≤6 chars class — `RESULTS-SEAMINT.md`: reserved-set size 26 tiny+old literals at real loads [1st]).

---

## 3. The numbers (the receipt table)

| quantity | value | source |
|---|---:|---|
| baseline medians (exec / decision / next / scope) | 0.17 / 0.00 / 0.67 / 1.00 | `krecency/results/anchor.csv` baseline [1st] |
| weights (3.0 − median) | 2.83 / 3.00 / 2.33 / 2.00 | `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` §(b) [1st] |
| anchored: below-3.0 / median / exec / decision / next / scope / recall | 1 / 3.00 / 3.33 / 3.00 / 2.67 / 3.00 / 3.33 | `krecency/results/anchor.csv` anchored [1st] |
| composed: below-3.0 / median | 1 / 3.00 | `krecency/results/compose.csv` composed [1st] |
| intent: below-3.0 / median / next | 0 / 3.33 / 3.00 | `krecency/results/intent.csv` intent [1st] |
| one-anchor claim's survival | into `summary_text` runs 2–3; answer `""` ×3 | `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` §(c) [1st] |
| seam-integration: none / literal-pin / pin+latch (prevalence) | 0.80 / 0.00 / 0.00 (reserved-set 26) | `krecency/RESULTS-SEAMINT.md` [1st] |
| retention: r=1.0 vs r∈{0,0.25,0.5} (deep-minima) | 0.00 vs 1.00 | `krecency/RESULTS-RETENTION.md` [1st] |
| E-3 loss-front | 0.17 / 0.00 / 0.67 / 1.00 / 2.00 / 2.83; control 4.67 clean | `RESULTS-E3-CONTINUATION-20261106.md` §A [1st] |
| tiny+old loss | 17/21 (81%); large+old 4; tiny+recent 0 | `RESULTS-SEAMMECH.md` [1st] |
| k-term kept-rates (flat) | 0.26–0.42 across the four classes | `ADJUDICATION-NEGENTROPY-20261106.md` §k-seam [1st] |
| battery medians (rungs 1–5) | 4.50 / 3.25 / 4.67 / 1.00 / 0.00 | `EVAL-LADDER-BATTERY-20261106.md` [1st] |

---

## 4. The walls (the rule's honest bounds)

- **W1 judge-coupling** — the probe scores ride the judge; the lift is judge-gated.
- **W2 empty-answer confound** — the one-anchor claim survives into `summary_text` yet the answer is `""`; the guard may be the driver (the W2-isolation's settle-condition).
- **W3 the rung cells are outside the region / uncompressed** — the battery's rungs are not the real compaction path.
- **W4 pattern-blindness** — C2's `_ANCHOR_PATTERNS` has no class for the Cell A literals (timestamps, session-ids, model-names, null-literals).
- **W5 the k-term does not separate classes** — flat 0.26–0.42; the priority-order is descriptive, not mechanistic.
- **W6 the full-budget scalar is judge-gated** — the one-anchor scalar reproduces; the full-budget scalar remains a QUESTION.
- **W7 scope is derivative of decision-core** — the generative-root argument; the scope class is not an independent reservation target.

---

## 5. The falsifier (stated in advance)

**The one-anchor A/B.** On the same fixture, same depth, same judge: reserve **ONLY** the decision-core claim vs **ONLY** the clock-anchor vs **ONLY** the next-action block, one anchor each. The rule is **REFUTED** if:

1. the decision-core-only arm does **not** clear the decision-core probe at ≥3.0, **or**
2. another single-class arm clears the decision-core probe at ≥3.0 (i.e., a lower-weight class substitutes for the root), **or**
3. the decision-core-only arm's next-action stays <3.0 **and** the decision-core + forward-intents pair does **not** exceed it on the same fixture (i.e., the pair is not the sufficiency complement).

**Standing receipts that already bound the falsifier:** anchor.csv shows the clock-anchor block leaves next-action at 2.67 < 3.0 (so the clock-anchor alone is not sufficient for next-action); intent.csv shows the pair clears it (3.00). The falsifier's settle-condition is the pair's next-action lift **exceeding** the decision-core-only arm's on the same fixture, and the lift **surviving the W2-isolation (no-guard) variant** — if the pair clears next-action only under the guard, the lift is an answering-artifact, not a retention lift.

---

## 6. The path (the verdict + the numbers + the next mechanism)

**Verdict:** the MINIMUM-RESERVE rule is **DESIGNED** — decision-core wins the one-anchor case (weight 3.00, the generative root, the necessary anchor), with the next-action / forward-intents block as the sufficiency complement (the minimum-sufficient pair). The rule is **necessary-but-not-sufficient** at the one-anchor tier (Wall W2), and its mechanistic underpinning is the generative-root argument, not the k-term (which is flat — Wall W5).

**The numbers:** baseline medians 0.17 / 0.00 / 0.67 / 1.00 → weights 2.83 / 3.00 / 2.33 / 2.00; anchored 1/5 below-3.0 (next-action 2.67); intent 0/5 below-3.0 (next-action 3.00); one-anchor claim survives into `summary_text` runs 2–3, answer `""` ×3.

**The next mechanism: MINIMUM-SUFFICIENT-PAIR RESERVE** — reserve the decision-core claim **and** the forward-intents block as the 2-anchor minimum, and A/B the pair against the decision-core-only arm on the same fixture; the pair's next-action lift (2.67 → 3.00) must exceed the one-anchor arm's and survive the W2-isolation (no-guard) variant. **Falsifier:** if the pair's lift is not greater than the decision-core-only arm's on the same fixture, or if the lift is a guard-artifact (clears only under the guard), the sufficiency complement is refuted and the one-anchor rule stands alone as necessary-but-never-sufficient.

---

## 7. Hand-separation + boundaries

- **[1st]** (re-read this pass): `NEGENTROPY-SWEEP-C-BUDGET-20261106.md`, `RESULTS-E3-CONTINUATION-20261106.md`, `ADJUDICATION-NEGENTROPY-20261106.md`, `SEAM-INTEGRATION-20261106.md`, `PROBE-BANKS-20261106.md`, `EVAL-LADDER-BATTERY-20261106.md`, `krecency/RESULTS-{RETENTION,SEAMMECH,ANCHOR,COMPOSE,INTENT,SEAMFIX,SEAMINT}.md`, `krecency/results/{anchor,intent}.csv`, `W2-ISOLATION-RUN-DESIGN-20261107.md`, `NEXT-SHIFT-PLAN-20261107.md` + its audit/AoA, `NIGHTSHIFT-HANDOFF-20261107-PART1/PART2.md`, the copycat-findings lane files.
- **[2nd]** (carried, not re-derived): the field receipts cited as counterfactuals (memory-anchor 10/10 verbatim-survival; Sleeping-Agent protected-anchor +0.314); the ladder run-JSONs' rowed numbers; the exact run-ids. **Boundary:** this lane's terminal is git-only; no live probe re-run; no instrument re-run. The W2-isolation's empties (2/5/4) are carried from the run-design's re-derivation, not re-grepped here.
- **The gate:** nothing public without the user's word. The public-gates hold until the word.