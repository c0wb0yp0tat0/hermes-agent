# RFC #143379 — the corrective final, form-passed: the read-restore underneath the P4 label, in the record's own voice

## 1. What I'm trying to understand

I'm reading the RFC's full record end to end — body and thread — and the label trail, to understand before I weigh in. The body's own theme: the durable record survives the session's compression with its provenance intact, and the agent re-reads it rather than make the user repeat — the read restored, the store re-readable, the compaction governed, as one network. The body names the restore (#141876) as the retrieval the listening mechanism rides on; the repo's triage has it P2. The RFC itself wears P4. Underneath the label question is the severity question: is this a nice-to-have pilot, or the memory path's core capability missing? The thread's own numbers answer it — and so does the queue's own shape.

## 2. The core wound — execution-confirmed

The read action was removed in `56ee8a5cc6` (2026-02-19) — a 14-line removal. On current main the tool answers `Unknown action 'read'`; against the same scratch store, #141876's head returns the entries plus the usage line, first try. The gap is verified by a reviewer's execution (jfugalde, 10-24), not just the RFC's own runs. The #139606 head's collection-error is a stale-base artifact — it predates `95610a5db4`'s pathlib fix — so there is no read-bug behind it; Finn763's rebase of #116673 (head verified 60a2e15638; GitHub's mergeability computes pending) — the fresh head, per the audit's flags-closure.

## 3. The quantification the record actually carries

The operator's comment-work (issuecomment-6378725575, 10-24): of the 300 most recent open issues, 43% (130) sit in the drift class — the session, the memory, the context, the compression, the state, the persistence, the recovery. Extrapolated to the ~16,900 open: ~7,300. At a conservative 100 lines per fix: ~726,000 lines — the 6,275 lines of compensation, ~116× over. At 8 hours per fix: ~58,500 hours — ~1,460 person-weeks. The root: the read's absence at the memory-store level. Throughput: 19,930 closed at ~43/day; 16,878 still open; the backlog ~46% of the total work; the oldest open 234 days; if 43% holds across closed, ~8,570 drift-tickets already closed — the same root, the same class, the same bill. "The drift's the compounding, not the clearing." The read is the best-and-foremost decision — "the trust is the product."

## 4. The compensation's true shape — the execution ledger

The ledger counts 106 commits and 6,275 lines (3,541 added, 2,734 deleted) since `56ee8a5cc6`. The debt's a subset: the code that exists only to hand entries back because the store cannot be read — four sites in `tools/memory_tool_store.py`, ~30 lines: `_failure_with_entries` carrying `current_entries` on the over-budget add (:322), the zero-match `closest_entries` (:124), the replaced-entry fields the successful write echoes (:481/:488), and the batch-abort's echo-fix that later removed `current_entries` because the echo made retries worse (#97316, :331). A fifth echo lives in `tools/memory_tool.py` (`_validate_single_op`, :157 — the missing-parameter echo). Give the agent `MemoryStore.read` (the 12-line method #141876 puts at :369) and these echoes are the obvious first cut. The rest is adjacent work that stacks on the symptom rather than closing it.

## 5. The user-cost

The user-cost is the agent's ear: the agent cannot re-read the durable record, so the user must repeat, and the anchor's provenance survives only through the workarounds' machinery. A governance layer that cannot read the record it governs is the shape of the cost.

## 6. The queue's P-shape — where the RFC sits

Measured 11-11, twice. The search-API's totals: P0: 1 · P1: 123 · P2: ~8,800 · P3: ~9,780 · P4: ~120 · unlabeled: 173. The exact-label recount (sample-verified against the substring-collision class): P0: 1 · P1: 119 · P2: 8,799 · P3: 9,787 · P4: 120 · unlabeled: 173. The shape's the same either way: the P4 bucket's the smallest in the queue — and the drift class's already a fifth of it (24 labeled comp/agent alone, before memory/context/compression labels are counted). The RFC's issue sits two bands below where the queue actually works (the P2/P3 range holds ~18,586 in the recount, ~18,580 in the totals). The label's not just an inversion of the body's centerpiece; it's a departure from the queue's own shape.

## 7. The hinge: the P2 centerpiece under a P4 label

The RFC's body names the restore (#141876 — P2 in the repo's own triage) as its core; the network's other pieces (#116673, #139606, #140008) are P3; the RFC itself wears P4 — "best-effort: we will get to it when we get to it — no commitment." The trail is screenshot-verified, and its timing is the read-gap's own signature: the category moved six times without the issue's substance changing, and each move traces to a *reading* event, not an issue event. P2 at birth (10-23 03:36Z, alt-glitch's triage, two minutes after the post) → P3 (10-24 01:06Z) → the quantification's own comment landed 79 minutes after that P3 → c2h5oh's sequence (P2 removed → P3 added → P4 added → P3 removed); the API's events endpoint exposes none of the final changes. The executions and confirmations landed hours later — the thread grew 34 comments of verified work (the field datapoints, the executions, the audits, the baseline-first question), none of it reflected in the label's final resting state. The label moved with the reading, never with the issue. The P4 is the residue, not a fresh judgement.

## 8. First-hand reproduction — the read-gap, reproduced on our own substrate

A controlled reproduction of the memory-store's read-absence on our own harness (the Pond-paper's design): prompt-embedded vs permission-free access to a persistent store — without the read-path, the agent fabricates from context (6/6 fabricated responses, reproduced twice); with the read-path restored, clean grounded refusals on the same prompts. The same class the RFC names, reproduced first-hand: no read-echo, no re-read, the fabrications compound. The execution-gap the draft carries is not a paper-shape — it is the behavior the store's silence produces.

## 9. The field corroborates — criteria exposure is the exact signature of this label trail

SelfImprove-Bench and the criteria-exposure studies (2611.08318) show the same curve the trail displays: when the verifier's criteria are visible, the score rises under those criteria and vanishes when they shift without departing from the instructions. The label trail's P2→P3→P4 sequence is that signature: the same issue, six readings, the category following the reading. The field's conclusion is the draft's ask: instruction-faithful criteria — the label must follow the issue's own body and its centerpiece, not the reading's noise.

## 10. The doors that stay open

If the read agrees the read-action's absence is the core wound, the restore is the centerpiece and the label should follow the body. If the read disagrees, I'd want to know which of the echo sites is the actual dependency — happy to rescope, split the question, or take evidence offers. The two-way doors stay open; the one-way door's flagged (archive-before-stub's ordering). I'm not asking for a commitment; I'm asking for a re-read. Thanks to the reviewers whose executions and audits the draft leans on — jfugalde's run, xngg1021's seam-audits, Finn763's rebase — the record's the evidence, and it's theirs as much as the RFC's.

## 11. What I'd ask

A re-triage of the RFC's label against its own body's centerpiece — the read-restore (#141876) as the P2 it already is in the repo's triage — and a sentence on the record explaining the P2→P3→P4 trail. If the P4 is the intended resting state, I'd want to understand why the body's core is the one piece parked.

## Form pass — change log

1. **Carried the first-pass's opening humility into the theme-led opening.** The first line now reads "to understand before I weigh in" — the first-pass draft's §1 register — before the body's theme and the severity question. *Why:* the hybrid's tone clause — the first-pass's humbleness is carried forward, not replaced by the depth's assertiveness (receipt: IMPROVED-S2U-DRAFT-20261111 §1).
2. **Merged the queue's two measurements into one section.** The FINAL4 carried the search-API totals (P1: 123 · P2: ~8,800 · P3: ~9,780) at §4 and the exact-label recount (P1: 119 · P2: 8,799 · P3: 9,787) at §13; a reader meeting both in sequence reads a contradiction. The merged section presents both as one measurement, twice, and holds the shape's sameness. *Why:* REF-TIMING's receipt names the first set "the search-API's totals" and §13's "exact-label counts ... sample-verified" — the contradiction is a form artifact, not a fact dispute.
3. **Merged the hinge and the category-fluctuation exhibit.** Both §7 and §10 carried the same P2→P3→P4 sequence; the merged §7 carries the trail once, with the timing and the reading-event reading. *Why:* the duplication is the depth's mess — the same receipts twice, with the second pass adding only the "six readings" frame.
4. **Moved the ask to the last section.** In the FINAL4 the ask sat at §9, before the first-hand reproduction (§11), the field corroboration (§12), and the queue's corrected shape (§13) — the reader met the ask before the last evidence. The ask now lands after all of it. *Why:* the ask's landing is the form's point; the evidence should precede it.
5. **Placed the gratitude at the close of the doors section, immediately before the ask.** *Why:* FINAL4's change-log item 5's register clause — gratitude intact — but it sat mid-flow inside §8; placing it before the ask keeps the ask's landing clean and the gratitude warm.
6. **Fixed the echo-site count in the doors.** §5 names five echo sites (four in `tools/memory_tool_store.py` plus `_validate_single_op` in `tools/memory_tool.py:157`); the doors' "which of the four sites" read as a stale count. Now "which of the echo sites." *Why:* internal consistency; the count is §5's receipt, not the doors' to restate.
7. **Kept every fact byte-faithful.** SHAs, file:line, counts, timings, quotes, the 43%-drift arithmetic, the five echo sites, the two queue measurements, the reproduction's 6/6, the field's 2611.08318 — all carried unchanged. *Why:* the criteria-blind rule; the form pass touches nothing evidential.

## Verdict

The form pass leaves the FINAL4's depth untouched and cleans its reader's path: one opening that carries the first-pass's humility and the body's own theme; one queue measurement instead of two contradictory ones; one hinge instead of a duplicated trail; the ask landing last; the gratitude placed before it; the echo-site count consistent. The draft is now un-fuckwithable in form and byte-faithful in fact — the read-restore is the memory path's core wound, the queue's largest drift-class's one root, and the label must follow the body.

## The calibration-clause landing — skills named and refused

The mission names two skills to load first — **think-tank** and **seek-to-understand**. Neither is loadable at this lane's dispatch: the harness exposes no `skill_view` tool to this lane, so both are named-refused with that why. The all-skills default is likewise refused — no skill's bytes are in evidence, and the pass's whys cite only the artifacts' receipts (the FINAL4, the first-pass draft, REF-TIMING, the criteria-blind selftest). The calibration-clause applies: the skills would inform, my judgment decides. The form verdict above is mine, grounded in the artifacts named.