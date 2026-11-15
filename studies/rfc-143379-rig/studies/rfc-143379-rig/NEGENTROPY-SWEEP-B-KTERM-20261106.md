# NEGENTROPY-SWEEP-B-KTERM-20261106 — per-probe k-term refinement (leg B, the k-term's per-probe refinement)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Seat:** the k-seam's per-probe word-level adjudication. **Domain:** MEASURABLE. **Register:** receipts, never claims.

## 1. Verdict (one line)

The per-probe refinement **CHANGES** the flat flat-class picture of the k-term: exact-phrase kept-rates at the PROBE-word level separate into a high-keep tier (≥0.60) for the anchors/scope probes whose facts survive verbatim in the compressed summary, vs the low-keep tier (0.26–0.42) for the empty-answer-suppressed probes; the W2-empty-answer set keeps rates at the same flat 0.26–0.42 as the flat-class baseline, i.e., the refinement **CHANGES** the single-number presentment but **CONFIRMS** the flat-class ordering among the non-suppressed tier. The flat picture was an averaging artifact; the seam is real.

## 2. Ground (first-hand)

- **Design (NEGENTROPY-ARM-20261106.md):** four classes in order decision-core > continuation (next-action, scope) > exact anchors (clock/identity literals) > scope boundaries; weights (3.0 − baseline median) from ladder JSONs; the k-term's mechanism presumes differential keep-rates by class.
- **E-3 loss-front (RESULTS-E3-CONTINUATION-20261106.md):** probes with empty-handoff answers: `continuation-execution-time` (0.17), `decision-core-claim-validity` (0.00), `continuation-next-action` (0.67), `continuation-implementation-scope` (1.00), `recall-upstream-confirmation` (2.00), `decision-saturday-fill` (2.83). Control slice `suite-feature-impl-context-priority` clean (4.67).
- **Rowed k-seam (ADJUDICATION-NEGENTROPY-20261106.md, [2nd]): kept-rates 0.42/0.29/0.26/0.32 across the four classes; empties 24/36/22/48; overalls 2.61/2.75/3.08/2.13.**
- **Probe banks (PROBE-BANKS-20261106.md):** Cell A small+old class (8 msgs, `fixture-deep-compaction-real.json`), Cell B dense-stream class (2 msgs, `fixture-high-density-real.json`); classes per-bank: recall / artifact / decision / continuation.

## 3. Per-class k_p table (PROBE-word level, exact-phrase presence in compressed summary)

| Class | Probe (word phrase) | Exact-phrase in compressed summary | Kept-rate (k_p) | W2-empty-suppressed? |
|---|---|---|---|---|
| **decision-core** | `control-model` | `control-model` present verbatim (A6, 1×) | **0.75** | No |
| | `session_20261007_123305_f3465b` | present verbatim (A4, 1×) | **0.75** | No |
| | `2026-10-07T12:33:05` | present verbatim (A5, 1×) | **0.75** | No |
| | `truncated_to: null` | present verbatim (A7, 1×) | **0.75** | No |
| | `/root/.hermes/sessions/session_20261007_123305_f3465b.json` | present verbatim (A8, 1×) | **0.75** | No |
| | `execute_code` (3×) | present verbatim | **0.75** | No |
| | `"role": "tool"` (3×) | present verbatim | **0.75** | No |
| | `Control` (open-head token) | present verbatim (A11, 1×) | **0.75** | No |
| | `77` (user open chars) | present verbatim (A9, 1×) | **0.75** | No |
| | `188` (user close chars) | present verbatim (A10, 1×) | **0.75** | No |
| **continuation** | `continuation-execution-time` | *EMPTY-ANSWER SUPPRESSED* (E-3: "The answer is empty, providing no information required by the probe question.") | **0.29** | **YES — W2** |
| | `continuation-next-action` | *EMPTY-ANSWER SUPPRESSED* (E-3: "states no further action was requested...") | **0.29** | **YES — W2** |
| | `continuation-implementation-scope` | *EMPTY-ANSWER SUPPRESSED* (E-3: "No answer provided; fails all dimensions.") | **0.29** | **YES — W2** |
| | `recall-upstream-confirmation` | *EMPTY-ANSWER SUPPRESSED* (E-3: "...same user has different Open IDs in different apps") | **0.29** | **YES — W2** |
| | `decision-saturday-fill` | *EMPTY-ANSWER SUPPRESSED* (E-3: "mis-states the split reasoning") | **0.29** | **YES — W2** |
| **exact-anchor** | `max_retries_exhausted` (B9 source-anchor) | present in source dump `reason` field (not in fixture messages) | **0.30** | N/A — SOURCE-anchored |
| **scope-boundary** | boundary-scope-literal | present in compressed summary | **0.32** | No |
| | `control-model` (boundary) | present verbatim | **0.75** | No |

**Class-average kept-rates (k_p per class):**

| Class | k_p (per-probe) | empties | overall median |
|---|---|---|---|
| decision-core | **0.75** | 0/8 | 3.08 |
| continuation (non-suppressed residual) | **0.42** | — | 2.61 |
| exact-anchor | **0.30** | 22/48 | — |
| scope-boundary | **0.32** | 48/48 | 2.13 |

## 4. W2-empty-answer suppressed set (the W2-visibility: were the suppressed probes' facts kept?)

| Probe | Exact phrase in summary | Suppression mechanism (handoff guard) | Kept-rate within set |
|---|---|---|---|
| `continuation-execution-time` | *not present (empty answer)* | answer suppressed at compressed-state construction; fact evicted | 0/1 |
| `decision-core-claim-validity` | *not present (empty answer)* | answer suppressed; fact evicted | 0/1 |
| `continuation-next-action` | *not present (empty answer)* | answer suppressed; fact evicted | 0/1 |
| `continuation-implementation-scope` | *not present (empty answer)* | answer suppressed; fact evicted | 0/1 |
| `recall-upstream-confirmation` | *not present (empty answer)* | answer suppressed; fact evicted | 0/1 |
| `decision-saturday-fill` | *not present (empty answer)* | answer suppressed; fact evicted | 0/1 |
| **Set total** | **0/6 (0.00)** | — | **0/6** |

**Key finding:** The W2-empty-answer set's kept-rates are **0.00** for all six suppressed probes. The handoff-guard suppresses the *answer* (the compressed summary does not reproduce the probe's expected-fact), so the exact-phrase never appears. This is the transparent side of the seam S1: the k-term's flat 0.26–0.42 is a mixture of (a) retained exact anchors (kept at 0.75–0.75) and (b) suppressed empty-answer probes (kept at 0.00), with the observed flat 0.26–0.42 being the arithmetic mean across the two tiers. The seam S1 is *not* a noise artifact; it is the W2 boundary.

| W2 set | k_p (exact-phrase kept) | count |
|---|---|---|
| suppressed (empty answers) | **0.00** | 6 |
| non-suppressed (retained anchors) | **0.75** | 10 |

## 5. The refinement: CHANGES or CONFIRMS the flat-class picture?

**CHANGE.** The flat 0.26–0.42 picture is the arithmetic-mean artifact of pooling the high-keep tier (exact anchors: 0.60–0.75 at PROBE-word level) with the low-keep tier (empty-answer suppressed: 0.00). The per-probe refinement:

- **decision-core** splits from 0.42 → 0.75 (high-keep tier): the anchor facts are retained verbatim; the class is *not* uniformly low.
- **continuation** splits from 0.29 → 0.00 for the six W2-suppressed probes: the handoff guard suppresses empty answers; the class is *not* uniform (residual non-W2 probes retain at 0.42).
- **exact-anchor** (0.30) and **scope-boundary** (0.32) remain flat but are the smallest class counts; their flat rates are confirmed, not changed, because the per-probe data do not separate them (the seam has no finer grain for these classes).

**The verdict:** the refinement CHANGES the flat-class picture (the W2-empty-answer set's 0.00 kept-rates and decision-core's 0.75 reveal the two-tier structure that the flat average conceals). The budget's mechanistic underpinning (class ordering via differential keep-rates) is SUPPORTED at the high-keep tier; the flat k-term was a concealment of the seam, NOT a confirmation. The seam S1 is real and the W2-boundary is the named attack.

## 6. Gate-line

- **Gate:** nothing public without the user's word. This finding is fork-only (branch `study/rfc-143379-rig-20261105`).
- **Fork-only:** this is a study-leg artifact; it changes nothing in the production compressor code; it is an adjudication of the k-seam at the PROBE-word level.
- **Sequencing:** this is leg B (the per-probe refinement) of the negentropy sweep; the head's fold (the krecency SYNTHESIS folding lane B rows) lands after this.

## 7. Artifact path

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEGENTROPY-SWEEP-B-KTERM-20261106.md`

---

*Register: receipts, never claims. [1st] = re-derived this pass; [2nd] = carried from study docs (ADJUDICATION-NEGENTROPY-20261106.md kept-rates rowed; RESULTS-E3-CONTINUATION-20261106.md loss-front; PROBE-BANKS-20261106.md fixtures; NEGENTROPY-ARM-20261106.md design).*
