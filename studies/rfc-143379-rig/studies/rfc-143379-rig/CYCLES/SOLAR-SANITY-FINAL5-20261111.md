# NEMO SANITY-CHECK — FINAL5 (improved-S2U-draft)
## Verdict: SANE-WITH-NOTES
*artifact path:* /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/CYCLES/SOLAR-SANITY-FINAL5-20261111.md

---

## (a) End-to-end coherence
Overall the draft coheres well: it reads as a single narrated argument — the read-action's absence is the core wound, the restore (#141876) is the centerpiece sitting P2 in the repo's triage, the label P4 is the residue of a reading-driven category trail, and the ask is to let the label follow the body. Section 1 frames it, section 2 establishes the wound as execution-confirmed, sections 3–4 quantify and place it in the queue, section 5 details the compensation shape, sections 6–7 carry the user-cost and the hinge, sections 8–9 state the ask with open doors, and sections 10–17 supply the category-fluctuation exhibit, the first-hand reproduction, field corroboration, the exact queue shape (measured twice, corrected), the middleware proof, the quantified frame, the self-reinforcing root, and the minimized ask. The architecture is sound and the register holds throughout.

## (b) Internal contradictions — top issues
1. **Section 4 vs. section 13 — identical claims, conflicting totals.** Section 4 says "the P2/P3 range holds ~18,580" while section 13 says "~18,586 in P2/P3". These are the same reported quantity, stated both as 18,580 and 18,586 (a 6-issue discrepancy that is unexplainable and breaks the register). Both sections otherwise repeat the same exact queue counts (P0:1 · P1:119 · P2:8,799 · P3:9,787 · P4:120 · unlabeled:173), so the two versions of the same number stand in direct conflict.
2. **Section 3's "the 6,275 lines of compensation, ~116× over" vs. section 5's "6,275 lines (3,541 added, 2,734 deleted)."** 3,541 + 2,734 = 6,275, so the totals reconcile — but section 3 introduces the 6,275 figure as "*the* compensation" while section 5 is careful to call it "The ledger counts" and frames 6,275 as the total across 106 commits. Section 3's phrasing ("the 6,275 lines of compensation, ~116× over") works as a ratio against the ~726,000 extrapolated drift lines, but the draft never states that the 6,275 is the *ledger total*, not the compensation itself — section 5 explicitly says "The debt's a subset," implying the 6,275 is larger than the debt. This is a framing ambiguity rather than a clean arithmetic contradiction.
3. **Section 10 repeats section 7 almost verbatim** (the P2→P3→P4 trail is stated identically in both), and section 15 claims "This RFC's thread carries 37 comments of verified work" while the audit's flag says the field datapoints derive from "the 34-comment arc" and section 7 says "the thread grew 34 comments." 37 comments vs. 34 comments is a 3-issue discrepancy in the very thread the draft is measuring. Similarly, section 15 says "the read-lightest zone (170 issues)" while section 4 says "unlabeled: 173." 170 vs. 173.
4. **Section 15's "~40,094" complete-issue-history vs. section 3's "~16,900 open" / "~19,930 closed"** — 16,900 + 19,930 = 36,830, which does not equal 40,094, and 40,094 is not 16,900+19,930. These three figures are mutually inconsistent (open + closed ≠ total history). Also section 15's "190 issues arrive every day against ~43 closing" gives a net growth of 147/day; over ~234 days (oldest open) that yields ~34,300 net, which exceeds the claimed 40,094 history and dwarfs the "17,240 drift at total scale" figure. The scale arithmetic is loose and the draft does not reconcile its own totals.

## (c) Sections that read flat / break the register
- **Section 17 is truncated mid-sentence** ("a re-read that costs seconds, and th") — the ask, minimized, does not complete. This is the single most material register-break because it leaves the deliverable of the whole document unfinished.
- **Section 12's citation "(2611.08318)"** reads as a garbled/imprecise arXiv-style identifier and does not clearly resolve; it sits in a supporting footnote of the ask without further context. Not a contradiction, but a completeness gap.
- **Sections 7 and 10** are near-duplicates; section 10's "The executions and confirmations landed hours later" adds a vague temporal claim with no anchor, but this is a minor redundancy rather than a break.

## (d) Does the ask land?
Yes, with the note above. The ask (sections 9, 17) is concrete and single: re-triage the RFC's label against its own body's centerpiece (#141876 read-restore as P2) and put a sentence on the record explaining the P2→P3→P4 trail. It is actionable, it is proportionate (a re-triage "costs seconds"), and it is the correct target for this document. The truncated ending of section 17 and the uncited "(2611.08318)" are the only deltas.

---

## Top 3 notes
1. **Section 4–13 conflict:** "the P2/P3 range holds ~18,580" (§4) vs. "~18,586 in P2/P3" (§13) — same quantity stated with a 6-issue discrepancy and never reconciled.
2. **Section 15 comment-count and label-count drift:** 37 comments in §15 vs. 34 in §7; "unlabeled: 170" in §15 vs. "unlabeled: 173" in §4. Two small inconsistencies that settle on one figure if the draft re-reads the thread.
3. **Section 17 truncation:** the document's ask, minimized, is cut off mid-sentence at the end ("a re-read that costs seconds, and th"). The artifact must be completed before it can close. (Soft issue; not a soundness failure.)
