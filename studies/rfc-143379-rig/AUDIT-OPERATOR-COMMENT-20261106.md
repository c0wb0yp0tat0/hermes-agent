# AUDIT-OPERATOR-COMMENT-20261106 — second-eye forensic audit of the operator-comment vet

**Target:** `ONESHOT-OPERATOR-COMMENT-20261106.md` (draft, HEAD `fe80424b82`) + vet `VETT-OPERATOR-COMMENT-20261106.md` (HEAD `8ff8b234c5`)
**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond the fork)
**Domain:** COMPLICATED
**Register:** receipts, never claims

---

## 1. Executive Summary

The vet's verdict (FIXED-READY) is **directionally correct**: the draft's structure is sound, the skew-guard is substantively honest, and the substance is fork-only + potential + labeled. No defect-class hunt lands. The substance is safe as a potential comment.

However, this second eye finds **two citation defects in the vet's own fix**, which the vet missed:

1. **The vet's F-1 fix retains the wrong "0.00" for the W2-empty set.** The vet correctly identified that the draft's "k-term two-tier (decision-core 0.75 vs W2-empty 0.00)" inverts the tier's class-membership (0.75 belongs to the anchor-literal tier, not to "decision-core" as a k-term value). But the vet's fix still says "W2-empty-answer set 0.00 kept-rates" — while the NEGENTROPY-SWEEP-B-KTERM-20261106 §3 shows the W2-empty suppressed probes (continuation-execution-time, continuation-next-action, continuation-implementation-scope) have **0.29** kept-rate, not 0.00. The 0.00 belongs to `decision-core-claim-validity` from the E-3 loss-geometry — a different measurement entirely. The vet's fix is incomplete: it re-labels the defect but re-states the wrong number.

2. **The draft's "LAQ local-survival 0.42/0.29/0.26/0.32" is a misattribution.** The draft's Purpose says "LAQ local-survival 0.42/0.29/0.26/0.32 with global-zero". The "0.42/0.29/0.26/0.32" figures are the k-term's kept-rates across the four classes (from NEGENTROPY-SWEEP-B-KTERM §3), not the LAQ-FIDELITY-PROBE's recovery medians (which are 4.50 / 3.25 / 4.67 / 1.00 / 0.00). The draft conflates the k-term's per-class kept-rates with the LAQ's recovery medians. The vet's I-1 Item does not catch this because it frames the pain point as "named as purpose, not asserted as measured prevalence" — a correct epistemic grade — but the specific numbers in the same sentence are misattributed.

The vet's I-2 (E-3 loss-geometry: exec-time 0.17, decision-core 0.00, next-action 0.67, scope 1.00) is **byte-matched and correct** against RESULTS-E3-CONTINUATION-20261106.md §A. The vet's I-8 (field handle "fluent hallucination") is correct. The vet's I-9 (method card) is correct. The vet's I-10 ("certifies nothing… promises no citation-test outcomes") is correct.

---

## 2. Per-Item Ledger (the audit's re-verification)

| # | Item | Vet verdict | Audit verdict | Byte-why |
|---|---|---|---|---|
| **I-1** | User-facing pain point ("believable but empty") named as purpose, not measured prevalence | APPROVE | **CONFIRMED** (framing correct; but the embedded numbers "LAQ local-survival 0.42/0.29/0.26/0.32" are misattributed — these are k-term kept-rates, not LAQ recovery medians) | The draft's Purpose frames the pain point as "Users sometimes receive model output that reads as plausible and well-formed but carries no actionable intent" — the operator's observed experience, correct epistemic grade. However, the same Purpose sentence cites "LAQ local-survival 0.42/0.29/0.26/0.32 with global-zero". The LAQ-FIDELITY file §1 table shows recovery medians (4.50/3.25/4.67/1.00/0.00), not "0.42/0.29/0.26/0.32". Those figures are the k-term kept-rates across the four classes from NEGENTROPY-SWEEP-B-KTERM §3. The draft conflates the two tables. |
| **I-2** | E-3 loss-geometry cite: exec-time 0.17, decision-core 0.00, next-action 0.67, scope 1.00 | APPROVE | **CONFIRMED** | Byte-matched against RESULTS-E3-CONTINUATION-20261106.md §A. The table shows: continuation-execution-time 0.17 (config-build-competitive-scouts), decision-core-claim-validity 0.00 (debug-session-feishu-id-model), continuation-next-action 0.67, continuation-implementation-scope 1.00. All four numbers re-derive from the same table. |
| **I-3** | k-term two-tier: "decision-core 0.75 vs W2-empty 0.00" | FIX (citations defect) | **REJECTED as stated by vet** — the vet's F-1 fix retains the "0.00" error | The NEGENTROPY-SWEEP-B-KTERM §3 shows the W2-empty suppressed probes (continuation class) have 0.29 kept-rate, not 0.00. The 0.00 belongs to `decision-core-claim-validity` from E-3 loss-geometry. The vet's F-1 fix says "W2-empty-answer set 0.00 kept-rates" — this repeats the wrong number. The correct fix should be "W2-empty-answer set 0.29 kept-rates vs the non-suppressed anchors' 0.75". |
| **I-4** | The E-3 loss-geometry numbers cited in the draft's Purpose | APPROVE (per vet, but see I-3) | **PARTIALLY-CONFIRMED** | The four numbers (0.17/0.00/0.67/1.00) are correct. The "LAQ local-survival 0.42/0.29/0.26/0.32" is a misattribution (k-term kept-rates, not LAQ). |
| **I-5** | k-term two-tier: "decision-core 0.75 vs W2-empty 0.00" — the receipt inversion | FIX (label placement) | **CONFIRMED** (the defect is real; the fix is incomplete) | The vet correctly identified that 0.75 belongs to the anchor-literal tier, not to "decision-core" as a k-term value. The defect is real. But the vet's fix retains the "0.00" for the W2-empty set — the wrong number. |
| **I-6** | Compaction-link: "offers one labeled, unmeasured hypothesis" (label trails the offer-verb) | FIX (announcement-vs-label skew) | **CONFIRMED** | The draft's Purpose says "offers one labeled, unmeasured hypothesis for why compaction might preferentially preserve form over intent". The label "labeled, unmeasured" follows the offer-verb "offers", reading as a finding-shaped offer. The vet's F-2 fix ("and states, as the operator's own hypothesis (unmeasured), one candidate link") corrects the adjective order so the label leads. |
| **I-7** | Would-settle-test: "fluent-noise rate vs. depth-vs-density curves" presented as virgin ground | FIX (unflattened surface) | **CONFIRMED** | The EVAL-LADDER-BATTERY-20261106 §(a) states "recovery does NOT track compaction depth (deepest compaction, rung 3, recovers best at 4.67; shallowest, rung 1, 4.50); it tracks fact-density / tiny+old-anchor survival". A "depth-vs-density" curve is exactly the surface the battery already walked. The vet's F-3 fix appends the prior "(the ladder's own measured non-tracking stands: recovery does not track compaction depth — EVAL-LADDER-BATTERY-20261106 §[Executive Summary])". Correct. |
| **I-8** | Field handle: "fluent hallucination" / "local-survival ≠ global-meaning decoupling" / confabulation / sycophantic padding | APPROVE | **CONFIRMED** | These are citations of the field's handles, not new claims. The draft says "what the hallucination-taxonomy literature names 'fluent hallucination'" — explicitly a citation of the field's vocabulary. The adjacent-handle list is hedged ("Adjacent handles"). |
| **I-9** | Method card (Trigger/Essence/Failure-risk/Rollback/Success-signal) | APPROVE | **CONFIRMED** | The card's Essence line binds the wall to the measured figures (0.17/0.00); the Rollback line names the measured surface (decision-core / next-action / scope) and keeps the citation-tests "armed, not landed"; the Success-signal line is a test condition, not a promised outcome. The vet's analysis is byte-accurate. |
| **I-10** | "certifies nothing the record hasn't measured and promises no citation-test outcomes" | APPROVE | **CONFIRMED** | The draft says this explicitly; the citation-tests are never given an outcome; the only forward-looking sentences are test-conditions and the explicit "if the hypothesis survives". True of the draft. |

---

## 3. The Vet's Own Defect Hunt (the vet's claim-checking)

The vet's Executive Summary says: "the 'k-term two-tier 0.75 vs 0.00' — a receipt inversion + a conflated handle". The vet's defect-class hunt ledger says:

- "The 0.75 belongs to the anchor-literal tier, not to 'decision-core' as a k-term value" → **CORRECT** (per NEGENTROPY-SWEEP-B-KTERM §3, the 0.75 is the decision-core anchors' kept-rate, a high-keep tier).
- "the 0.00 belongs to the W2-empty set, not to a 'two-tier' contrast with 0.75" → **INCORRECT**. The NEGENTROPY-SWEEP-B-KTERM §3 shows the W2-empty suppressed probes (continuation-execution-time, continuation-next-action, continuation-implementation-scope) have 0.29 kept-rate, not 0.00. The 0.00 belongs to `decision-core-claim-validity` from the E-3 loss-geometry — a different measurement entirely.

So the vet's defect analysis is half-correct: the receipt-inversion class is MET (0.75 is mis-scoped from the anchor-literal tier to "decision-core"), but the vet mis-identifies what the "0.00" refers to. The 0.00 is the decision-core-claim-validity probe's score, not the W2-empty set's kept-rate.

The vet's F-1 fix ("W2-empty-answer set 0.00 kept-rates vs the non-suppressed anchors' 0.75") retains the wrong number. This is a second citation error in the vet's own output — the vet, which was supposed to catch citation defects, made the same error.

---

## 4. The Vet's F-1 Fix — Byte-Level Verification

| Vet F-1 | Actual NEGENTROPY-SWEEP-B-KTERM §3 |
|---|---|
| "W2-empty-answer set 0.00 kept-rates" | W2-empty suppressed probes (continuation class): **0.29** kept-rate (continuation-execution-time, continuation-next-action, continuation-implementation-scope all 0.29) |
| "non-suppressed anchors' 0.75" | **0.75** — correct (decision-core anchors, high-keep tier) |
| "(NEGENTROPY-SWEEP-B-KTERM-20261106 §3/§4)" | §3 contains the per-class k_p table with the correct numbers. §4 (not read in full here) was not needed for this verification. |

**Oracle verdict on F-1:** INCOMPLETE — the "0.00" must be "0.29". The vet's defect analysis correctly identified the tier inversion but mis-stated the W2-empty set's kept-rate.

---

## 5. The Vet's F-2, F-3 Fixes — Verification

| Fix | Byte-why | Verdict |
|---|---|---|
| **F-2** (compaction-link label) | The draft's Purpose says "offers one labeled, unmeasured hypothesis…". The label trails the offer-verb. The vet's fix "and states, as the operator's own hypothesis (unmeasured), one candidate link" places the label first. | **CONFIRMED CORRECT** |
| **F-3** (would-settle-test prior) | The ladder's measured non-tracking (recovery does not track depth; tracks fact-density) is the prior the would-settle-test must carry. The vet's fix appends the EVAL-LADDER-BATTERY citation. | **CONFIRMED CORRECT** |

---

## 6. The Vet's I-1 Analysis — The Misattribution Leaf

The vet's I-1 says: "The draft frames it as the operator's observed experience ('Users sometimes receive…'), and the Analysis Brief marks the mapping 'plausible, not proven' with 'prevalence rate unmeasured'. That is the correct epistemic grade."

The vet's I-1 is correct about the **framing** of the pain point. But the vet's I-1 ledger does not separately verify the draft's embedded numbers. The draft's Purpose sentence reads:

"LAQ local-survival 0.42/0.29/0.26/0.32 with global-zero"

The "0.42/0.29/0.26/0.32" figures are the **k-term's kept-rates across the four classes** (NEGENTROPY-SWEEP-B-KTERM §3: decision-core 0.75 high-keep? No — actually those are the flat-class baseline rates: 0.42/0.29/0.26/0.32). Wait, let me re-check: the NEGENTROPY-SWEEP-B-KTERM §3 shows:

- decision-core: 0.75 (high-keep tier)
- continuation: 0.29 (low-keep tier, W2-empty suppressed)
- W2-empty suppressed: 0.29

The "0.42/0.29/0.26/0.32" figures appear in the NEGENTROPY-SWEEP-B-KTERM §2 Ground: "Rowed k-seam (ADJUDICATION-NEGENTROPY-20261106.md, [2nd]): kept-rates 0.42/0.29/0.26/0.32 across the four classes; empties 24/36/22/48; overalls 2.61/2.75/3.08/2.13."

So the draft's "LAQ local-survival 0.42/0.29/0.26/0.32" misattributes the k-term's per-class kept-rates to "LAQ local-survival". The LAQ-FIDELITY file's recovery medians are 4.50/3.25/4.67/1.00/0.00 (rungs 1-5), not "0.42/0.29/0.26/0.32".

**Verdict on this misattribution:** The numbers are real (they exist in the record), but they are misattributed to "LAQ local-survival". The draft should say "k-term per-class kept-rates 0.42/0.29/0.26/0.32 with global-zero (decision-core 0.00)".

---

## 7. Gate-Vote

**THE GATE: nothing public without the user's word** (verbatim, from the vet and the record)

**Arithmetic of the audit:**

- I-1: CONFIRMED (framing) + citation misattribution (unnumbered defect)
- I-2: CONFIRMED (byte-matched)
- I-3: REJECTED as stated by vet (vet's F-1 retains wrong number)
- I-4: PARTIALLY-CONFIRMED (numbers correct but misattributed to LAQ)
- I-5: CONFIRMED (defect real; fix incomplete)
- I-6: CONFIRMED (fix correct)
- I-7: CONFIRMED (fix correct)
- I-8: CONFIRMED (correct)
- I-9: CONFIRMED (correct)
- I-10: CONFIRMED (correct)

**Audit gate-vote: APPROVE (post-fix).** The vet's distributed judgment (6 APPROVE · 3 FIX · 0 REJECT) is correct as a disposition: no defect-class hunt lands, and the substance is safe as a potential comment. However, the vet's F-1 fix contains a citation error (the "0.00" for the W2-empty set should be 0.29), and the draft contains a number misattribution ("LAQ local-survival 0.42/0.29/0.26/0.32" should cite the k-term's kept-rates, not LAQ recovery medians). Both are fixable and cheap. The vet's conclusion (FIXED-READY) holds, but the vet's F-1 edit text must be corrected before the head posts.

**The vet's own arithmetic:** 9 APPROVE · 3 FIX · 0 REJECT. The vet's per-item verdicts (I-1, I-2, I-8, I-9, I-10 = APPROVE; I-3/I-5 = FIX; I-6/I-7 = FIX; with the defect-class hunt correctly finding no REJECT) are directionally correct. The two citation errors in the vet's own output (F-1's "0.00 for W2-empty", and the I-1 papering-over of the "LAQ local-survival" misattribution) are the audit's findings.

---

## 8. The Vet's Three Edits (F-1, F-2, F-3) — Status

| Edit | Vet's edit text | Audit status |
|---|---|---|
| **F-1** | Replace: `k-term two-tier (decision-core 0.75 vs W2-empty 0.00)`<br>With: `W2-empty-answer set 0.00 kept-rates vs the non-suppressed anchors' 0.75 (NEGENTROPY-SWEEP-B-KTERM-20261106 §3/§4)` | **INCOMPLETE** — the "0.00" must be "0.29". The W2-empty set's kept-rates are 0.29, not 0.00. The 0.00 belongs to decision-core-claim-validity (E-3 loss-geometry). |
| **F-2** | Replace: `and offers one labeled, unmeasured hypothesis for why compaction might preferentially preserve form over intent`<br>With: `and states, as the operator's own hypothesis (unmeasured), one candidate link — compaction preserving form over intent` | **CORRECT** — label now leads. |
| **F-3** | Append: `(the ladder's own measured non-tracking stands: recovery does not track compaction depth — EVAL-LADDER-BATTERY-20261106 §[Executive Summary])` | **CORRECT** — prior carried. |

---

## 9. Artifact

- File: `AUDIT-OPERATOR-COMMENT-20261106.md` (this file)
- Branch: `study/rfc-143379-rig-20261105` (fork-only)
- Gate-line (verbatim): **the gate: nothing public without the user's word**
- Vet post-state: the head's register + the post at the user's word, after F-1/F-2/F-3 are applied with the F-1 number corrected to 0.29.

---

## 10. Next Mechanism (the record's own, gated on this landing)

The quoted numbers' accuracy is the discipline: "the edited comment's every number re-derives from the receipt named at its cite, and no sentence asserts more than the cited receipt."

After this audit closes, the next mechanism the record dictates is the **fluent-noise rate vs. depth-vs-density curve family** (the citation-test family pointed at the operator), gated on the ladder's measured non-tracking (F-3's prior). Citation-tests remain armed, not landed.
