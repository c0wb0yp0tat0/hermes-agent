# HY4-CRITIQUE-20261118 — cold-critique delta log

Seat: stepfun/step-3.7-flash:free · scribe-cell: rig-hy4-loop-critique
Draft under critique: HY4-REGROUP-MEMO-20261118.md
Receipt spine: HY4-LOOP-SPINE-20261118.md
Comparator: NEMO-MOMENTUM-REGROUP-20261116.md

---

## Delta 1 — RECEIPT: fold-standard citation does not resolve cleanly

**Draft line (§4):** "Fold standard: NEMO-MOMENTUM-REGROUP-20261116, section 1(a) and section 2 item 1."

**Receipt check:** The comparator's §1(a) (Apex v5 Progress) does carry the fold+verify+row countermove in its prose, so the §1(a) half resolves. However, the comparator's §2 is a four-item next-launch block; "section 2 item 1" points to the "Apex v5 Fold+Verification+Row" launch item, which names seat, artifact, gate, and action — not a fold standard per se. The citation conflates a launch-block entry with a doctrinal source. The closest clean receipt for a fold standard is the comparator §1(a) countermove alone.

**Verdict:** Partial receipt. The §1(a) half holds; the "section 2 item 1" half is a category confusion.

---

## Delta 2 — COUNT: 24-vs-32 handling is correct

**Draft line (verdict line):** "the day-one spine holds twenty-four receipted rows, all COMPLETE; the first ride's thirty-two is a comment volume at one landing, not a row count."

**Spine check:** The spine's "The count, by rule" section states exactly this: 24 = receipted rows with `issuecomment-<digits>` ids in `## 2026-11-05`; 32 = the `count` column value on `issuecomment-6663943572` (RUN-RFC143379-RIG-20261105), which is quantified comment volume at one landing, not a row count. The spine explicitly warns: "Do not substitute one for the other." The draft follows that injunction precisely.

**Spine row confirmed:** `issuecomment-6663943572 | RUN-RFC143379-RIG-20261105 | 32 | COMPLETE` — count column = 32, event = single landing run.

**Verdict:** Correct. No substitution flagged.

---

## Delta 3 — REGISTER: risks header drops into sentence-case mid-section

**Draft line (§1 opening):** "## §1 THE RISKS — named first, each with status and countermove" followed by "### (a) The read-gate defect" (sentence case, no all-caps) and "### (b) The fold-doctrine gap" (same).

**Comparator check:** The comparator's risks block uses full all-caps for each risk heading: "**(a) Apex v5 Progress**", "**(b) Runner Battery Dispatch Race**", etc. The draft opens the section header in all-caps but the four individual risk sub-headings are in title/sentence case. The verdict line and loop-state line are correctly all-caps, so this is an internal register slip within the risks block rather than a wholesale failure.

**Also flagged:** The comparator's loop-state line is a single verdict phrase in all-caps with no leading prose. The draft's loop-state line ("WRITE-FIRST-THEN-COMMIT + fold-verify-row-on-landing. The stage-2 draft is delivered; stage-3 critique is queued behind this gate.") adds explanatory prose after the verdict phrase, slightly relaxing the register.

**Verdict:** Minor register slip; risks sub-headings should be all-caps to match comparator's established pattern.

---

## Delta 4 — OPPORTUNITY: both entries carry no substance — MUST-FIX for stage 4

**Draft lines (§5, two entries):**

*Pilot question:*
> Who: the operator; the memo closes on the operator's word.
> Where: the study's regroup memo, Part 5, "The two opportunities."
> When: not confirmed. The opportunity's recommendation and timing are not confirmed for the reason in section 4: Part 5 read truncated, then content-reads were gated.

*Daily digest:*
> Who: the operator.
> Where: the study's regroup memo, Part 5, "The two opportunities."
> When: not confirmed. Same reason as the pilot question.

**Comparator check:** The comparator's next-launch block (§2) gives each item four named fields — seat, artifact, gate, action — with concrete values in every field. The draft's two opportunity entries carry only who/where metadata. Neither entry contains a verbatim question, a recommendation, or a digest instruction. The "when" field is the only substantive field present and it reads "not confirmed," which means both entries are structurally empty.

**What stage 4 revision must contain:**

1. **Pilot question** — the verbatim question text as it appears in the study's regroup memo, Part 5, "The two opportunities" (the HITL-MEMO-20261116 Part 5 text that was truncated in this lane's read); a concrete recommendation on how the operator's response shapes the next launch gate.

2. **Daily digest** — a concrete digest recommendation: what the digest covers (scope, cadence, distribution), who compiles it, and the earliest confirmed "when" the digest can first ship.

Without these two additions the opportunities block is a labelled gap, not a substantive opportunity statement.

**Verdict:** MUST-FIX. Both entries are structurally empty.

---

## Delta 5 — SHAPE: S5/S6 refusal is honest — the brief names the stages but supplies nothing to receipt

**Draft lines (§2, items 3–4):**
> 3. Stage S5 — Seat: not confirmed. Artifact: not confirmed. Gate: not confirmed. Action: not confirmed. Reason: the brief names stages through S6 but supplies no seat, artifact, gate, or action for S5.
> 4. Stage S6 — [identical not-confirmed pattern]

**Brief check:** The HY4-LOOP-S3 brief's next-launch block names stages S3 through S6 but provides seat, artifact, gate, and action only for S3 (critique) and S4 (revision). S5 and S6 are named but carry no operational detail. The draft correctly marks all four fields as not confirmed and supplies the reason — the brief's own omission.

**Verdict:** Honest refusal. The draft did not invent S5/S6 detail; it flagged the gap. The "not confirmed" stamp is the correct response to an unresourced stage.

---

## Delta 6 — REGISTER: opportunity section drops the all-caps block-heading pattern used elsewhere

**Draft line (§5 opening):** "## THE TWO OPPORTUNITIES (for the operator's word)" — all-caps, matches comparator's "THE REGROUP VERDICT LINE" pattern. However, the two opportunity items are presented as prose paragraphs with bullet metadata rather than as structured launch-block items with named fields (seat/artifact/gate/action), which is the shape the comparator uses for every named forward item in §2.

**Verdict:** Secondary register/shape note; subsumed under Delta 4 (the structural fix also restores the launch-block shape).

---

## The verdict

The draft **partial-passes**.

Three strongest deltas:

1. **Delta 4 (OPPORTUNITY — MUST-FIX):** Both opportunity entries carry no verbatim question and no concrete recommendation; stage 4 must add the verbatim pilot question from HITL-MEMO-20261116 Part 5 and a concrete digest recommendation with an earliest confirmed "when."
2. **Delta 1 (RECEIPT):** The fold-standard citation in §4 conflates a comparator launch-block entry (§2 item 1) with a doctrinal source; the clean receipt is the comparator §1(a) countermove alone.
3. **Delta 3 (REGISTER):** The four risk sub-headings in §1 are sentence-case where the comparator's pattern is all-caps; the loop-state line adds explanatory prose where the comparator uses a bare verdict phrase.

The count handling (Delta 2) is correct and the S5/S6 refusal (Delta 5) is honest; neither is a failure.
