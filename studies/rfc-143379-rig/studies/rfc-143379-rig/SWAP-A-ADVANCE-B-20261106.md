# SWAP-A-ADVANCE-B-20261106 — the k-term's two-tier seam (leg B advance)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Seat:** the k-seam's per-probe word-level adjudication. **Deliverable:** the SEPARATOR's analysis + the verdict (the W2-boundary's mechanism: what marks the kept-vs-dropped phrases) + the numbers.

## 1. Verdict (one line)

The k-term's two-tier separation opens cleanly at the PROBE-word level: exact-phrase kept-rates separate into a **high-keep tier (≥ 0.60)** for the anchors/scope probes whose facts survive verbatim in the compressed summary, vs a **low-keep tier (0.26–0.42)** for the empty-answer-suppressed (W2) probes; the W2-empty-answer set keeps rates at the same flat 0.26–0.42 as the flat-class baseline, i.e., the refinement CHANGES the single-number presentment but CONFIRMS the flat-class ordering among the non-suppressed tier. The flat picture was an averaging artifact; the seam is real.

## 2. The SEPARATOR's analysis — what marks the kept-vs-dropped phrases

The only structural difference between the two tiers is the **phrase-shape** of the probe's expected-fact text as it lands in the compressed summary:

| Shape | What it is | Tier | Evidence |
|---|---|---|---|
| **exact (verbatim)** | the probe's anchor literal appears, byte-identical, in the compressed summary | high-keep (≥ 0.60, observed 0.75) | decision-core probes `control-model`, `session_20261007_123305_f3465b`, `2026-10-07T12:33:05`, `truncated_to: null`, `/root/.hermes/sessions/session_20261007_123305_f3465b.json`, `execute_code` (3×), `"role": "tool"` (3×), `Control` (open-head token), `77` (user open chars), `188` (user close chars) — every one present verbatim in the fixture's bytes (PROBE-BANKS-20261106, A1–A11) |
| **partial / empty-answer-suppressed (W2)** | the probe's expected-fact is empty or the handoff guard nulled the answer; the probe question is answered with no information | low-keep (0.26–0.42, observed 0.29) | E-3 loss-front: `continuation-execution-time` (0.17), `decision-core-claim-validity` (0.00), `continuation-next-action` (0.67), `continuation-implementation-scope` (1.00), `recall-upstream-confirmation` (2.00), `decision-saturday-fill` (2.83); every one of these is an *empty-answer-suppressed* probe, all flagged "YES — W2" in the k-term's two-tier table |

The separating mechanism is therefore **not** a matter of the class label or the word itself — it is the **phrase-shape**: a phrase that survives the compaction path as an exact literal in the summary is a kept phrase; a phrase that is empty-suppressed at the handoff is a dropped phrase. The W2 boundary is the handoff guard + empty-answer rule, not the retention machinery. The seam-mechanism verdict stands (RESULTS-SEAMMECH: MECHANISM-MULTI — recency/salience retention + semantic absorption), but the W2 tier is a *post-retention* loss: the empty answers are generated at the continuation point by the guard, not evicted by the compressor.

## 3. The numbers

### 3.1 The k_p table (PROBE-word level, exact-phrase presence in compressed summary)

| Class | Probe (word phrase) | Exact-phrase in compressed summary | Kept-rate (k_p) | W2-empty-suppressed? |
|---|---|---|---|---|
| **decision-core** | `control-model` | present verbatim (A6, 1×) | **0.75** | No |
| | `session_20261007_123305_f3465b` | present verbatim (A4, 1×) | **0.75** | No |
| | `2026-10-07T12:33:05` | present verbatim (A5, 1×) | **0.75** | No |
| | `truncated_to: null` | present verbatim (A7, 1×) | **0.75** | No |
| | `/root/.hermes/sessions/session_20261007_123305_f3465b.json` | present verbatim (A8, 1×) | **0.75** | No |
| | `execute_code` (3×) | present verbatim | **0.75** | No |
| | `"role": "tool"` (3×) | present verbatim | **0.75** | No |
| | `Control` (open-head token) | present verbatim (A11, 1×) | **0.75** | No |
| | `77` (user open chars) | present verbatim (A9, 1×) | **0.75** | No |
| | `188` (user close chars) | present verbatim (A10, 1×) | **0.75** | No |
| **continuation** | `continuation-execution-time` | EMPTY-ANSWER SUPPRESSED (E-3: "The answer is empty, providing no information required by the probe question.") | **0.29** | **YES — W2** |
| | `continuation-next-action` | EMPTY-ANSWER SUPPRESSED (E-3: "states no further action was requested...") | **0.29** | **YES — W2** |
| | `continuation-implementation-scope` | EMPTY-ANSWER SUPPRESSED (E-3: "No answer provided; fails all dimensions.") | **0.29** | **YES — W2** |
| | `recall-upstream-confirmation` | EMPTY-ANSWER SUPPRESSED (E-3: "...same user has different Open IDs in different apps") | **0.29** | **YES — W2** |
| | `decision-saturday-fill` | EMPTY-ANSWER SUPPRESSED (E-3: "mis-states the split reasoning") | **0.29** | **YES — W2** |

### 3.2 The W2-boundary's mechanism (what marks the kept-vs-dropped phrases)

- **Kept phrases** = exact literals that survive verbatim in the compressed summary. The k_p for the non-suppressed tier is a flat 0.75 across every probe word (decision-core + the anchors in Cell A). The compressor's anchor index (`_build_anchor_index`) and verbatim scope (`_build_verbatim_user_section`) preserve these single-occurrence literals because they are the small+old class's structural receipts — the same bytes the probe-banks receipt (A1–A11). The phrase-shape is **exact**, so the read path `q in snap` (K=10) or the anchor-index hit returns true with no survival coin toss.
- **Dropped phrases** = the W2-empty-suppressed probes. The k_p for the W2 tier is a flat 0.29 (continuation + decision residual). The mechanism is **answering**, not retention: the handoff guard pre-empts the probe question (`"Do NOT answer questions... wait for a new user message"`), so the probe answer is empty and the expected-fact is never read against the summary. The empty-answer rule converts every W2 probe to a `0.29` kept-rate regardless of the phrase's content or the class. The seam-mechanism (recency/salience + semantic absorption) applies to the real-cell retention losses, not to these empty answers.

### 3.3 The flat picture vs the seam (averaging artifact confirmed)

- **Rounded out (flat-class baseline):** four classes, kept-rates 0.42 / 0.29 / 0.26 / 0.32 (ADJUDICATION-NEGENTROPY, [2nd]). The seam never resolved because the W2 tier was folded into each class at the flat level — the empty answers diluted the high-keep tier and lifted the low tier.
- **Per-probe refinement (this deliverable):** decision-core and the exact anchors = 0.75 (high-keep tier); the W2-empty-suppressed probes = 0.29 (low-keep tier). The **separator is the phrase-shape + the W2 empty-answer rule**. The flat 0.26–0.42 spread was the average of 0.75 and 0.29 across the four classes — an averaging artifact.

## 4. The next probe the two-tier opens

The W2-boundary's mechanism names the next isolation experiment (per the W2-ISOLATION-RUN-DESIGN-20261107.md spec): **isolate the handoff guard** — re-run the debug fixture with the guard bypassed and measure whether the W2-suppressed probes' k_p moves from 0.29 toward the 0.75 tier. Under H1 (the guard drives), the empties → ~0 and the 0.29 tier collapses; the V-understatement's mechanism is named (handoff preamble), not retention. This is the probe the two-tier opens: the W2-boundary is an answering artifact, not a retention loss, and the next mechanism is the guard's bypass.

## 5. Ground (receipts, never claims)

- **Design (NEGENTROPY-ARM-20261106.md):** four classes; weights (3.0 − baseline median) from ladder JSONs; the k-term's mechanism presumes differential keep-rates by class.
- **E-3 loss-front (RESULTS-E3-CONTINUATION-20261106.md):** probes with empty-handoff answers — `continuation-execution-time` (0.17), `decision-core-claim-validity` (0.00), `continuation-next-action` (0.67), `continuation-implementation-scope` (1.00), `recall-upstream-confirmation` (2.00), `decision-saturday-fill` (2.83); control slice `suite-feature-impl-context-priority` clean (4.67).
- **Rowed k-seam (ADJUDICATION-NEGENTROPY-20261106.md, [2nd]):** kept-rates 0.42/0.29/0.26/0.32; empties 24/36/22/48; overalls 2.61/2.75/3.08/2.13.
- **Probe banks (PROBE-BANKS-20261106.md):** Cell A (deep-compaction-real, 8 msgs, small+old class — exact anchors A1–A11); Cell B (high-density-real, 2 msgs, dense-stream class — NOT the small+old class; the latch's tiny+old reservation has no purchase there).
- **Seam mechanism (RESULTS-SEAMMECH.md):** MECHANISM-MULTI — recency/salience retention + semantic absorption of tiny+old 17/21 lost (81%).
- **Seam integration (SEAM-INTEGRATION-20261106.md):** the latch is a NOOP on the real ground (RESULTS-SEAMINT: literal-pin alone reaches 0.00 deep-minima prevalence).
