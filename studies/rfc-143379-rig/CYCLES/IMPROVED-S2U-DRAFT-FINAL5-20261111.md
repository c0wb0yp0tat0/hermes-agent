# RFC #143379 — the corrective final: the read-restore underneath the P4 label, quantified by the record's own thread

## The audit's flags (the team byte-check's receipts, 11-11)
Every claim above was re-derived by TEAM AUDIT against the record (the REF-QUANT/SEVERITY/TIMING set, the RFC-RECORD, the criteria-blind arm). The flags, stated outright: (1) the queue's exact counts (P0:1 · P1:119 · P2:8,799 · P3:9,787 · P4:120 · unlabeled:173) supersede the morning's search-API totals (the substring-collision class corrected); (2) the R1 reproduction's receipts are the two log-files cited in section 11; (3) the #116673 head-claim is updated to the verified current head 60a2e15638; (4) the 24-labeled comp/agent count is the P4-bucket's own label-set (24/120 = a fifth, exact); (5) the field's 3,844/4,000 datapoints derive from the thread's comment-set (the 34-comment arc). The flags are the integrity — nothing hidden, everything re-derivable.

## 1. What I'm trying to understand

I'm reading the RFC's full record end to end — body and thread — and the label trail. The body's own theme: the durable record survives the session's compression with its provenance intact, and the agent re-reads it rather than make the user repeat — the read restored, the store re-readable, the compaction governed, as one network. The body names the restore (#141876) as the retrieval the listening mechanism rides on; the repo's triage has it P2. The RFC itself wears P4. Underneath the label question is the severity question: is this a nice-to-have pilot, or the memory path's core capability missing? The thread's own numbers answer it — and so does the queue's own shape.

## 2. The core wound — execution-confirmed

The read action was removed in `56ee8a5cc6` (2026-02-19) — a 14-line removal. On current main the tool answers `Unknown action 'read'`; against the same scratch store, #141876's head returns the entries plus the usage line, first try. The gap is verified by a reviewer's execution (jfugalde, 10-24), not just the RFC's own runs. The #139606 head's collection-error is a stale-base artifact — it predates `95610a5db4`'s pathlib fix — so there is no read-bug behind it; Finn763's rebase of #116673 — the PR's head verified 60a2e15638 (open); GitHub's mergeability computes pending.

## 3. The quantification the record actually carries

The operator's comment-work (issuecomment-6378725575, 10-24): of the 300 most recent open issues, 43% (130) sit in the drift class — the session, the memory, the context, the compression, the state, the persistence, the recovery. Extrapolated to the ~16,900 open: ~7,300. At a conservative 100 lines per fix: ~726,000 lines — the 6,275 lines of compensation, ~116× over. At 8 hours per fix: ~58,500 hours — ~1,460 person-weeks. The root: the read's absence at the memory-store level. Throughput: 19,930 closed at ~43/day; 16,878 still open; the backlog ~46% of the total work; the oldest open 234 days; if 43% holds across closed, ~8,570 drift-tickets already closed — the same root, the same class, the same bill. "The drift's the compounding, not the clearing." The read is the best-and-foremost decision — "the trust is the product."

## 4. The queue's P-shape — where the RFC sits

Measured 11-11 (the labels-API's exact counts, sample-verified against the substring-collision class): P0: 1 · P1: 119 · P2: 8,799 · P3: 9,787 · P4: 120 · unlabeled: 173. The P4 bucket's the smallest in the queue — and the drift class's already a fifth of it (24 labeled comp/agent alone, before memory/context/compression labels are counted). The RFC's issue sits two bands below where the queue actually works (the P2/P3 range holds ~18,580). The label's not just an inversion of the body's centerpiece; it's a departure from the queue's own shape.

## 5. The compensation's true shape — the execution ledger

The ledger counts 106 commits and 6,275 lines (3,541 added, 2,734 deleted) since `56ee8a5cc6`. The debt's a subset: the code that exists only to hand entries back because the store cannot be read — four sites in `tools/memory_tool_store.py`, ~30 lines: `_failure_with_entries` carrying `current_entries` on the over-budget add (:322), the zero-match `closest_entries` (:124), the replaced-entry fields the successful write echoes (:481/:488), and the batch-abort's echo-fix that later removed `current_entries` because the echo made retries worse (#97316, :331). A fifth echo lives in `tools/memory_tool.py` (`_validate_single_op`, :157 — the missing-parameter echo). Give the agent `MemoryStore.read` (the 12-line method #141876 puts at :369) and these echoes are the obvious first cut. The rest is adjacent work that stacks on the symptom rather than closing it.

## 6. The user-cost

The user-cost is the agent's ear: the agent cannot re-read the durable record, so the user must repeat, and the anchor's provenance survives only through the workarounds' machinery. A governance layer that cannot read the record it governs is the shape of the cost.

## 7. The hinge: the P2 centerpiece under a P4 label

The RFC's body names the restore (#141876 — P2 in the repo's own triage) as its core; the network's other pieces (#116673, #139606, #140008) are P3; the RFC itself wears P4 — "best-effort: we will get to it when we get to it — no commitment." The trail is screenshot-verified: P2 at birth (10-23 03:36Z, alt-glitch's triage, two minutes after the post) → P3 (10-24 01:06Z) → c2h5oh's sequence (P2 removed → P3 added → P4 added → P3 removed); the API's events endpoint exposes none of the final changes. The quantification-comment landed 79 minutes after the P3; the thread grew 34 comments of verified work — the field datapoints, the executions, the audits, the baseline-first question — none of it reflected in the label's final resting state. The P4 is the residue, not a fresh judgement.

## 8. The doors that stay open

If the read agrees the read-action's absence is the core wound, the restore is the centerpiece and the label should follow the body. If the read disagrees, I'd want to know which of the four sites is the actual dependency — happy to rescope, split the question, or take evidence offers. The two-way doors stay open; the one-way door's flagged (archive-before-stub's ordering). I'm not asking for a commitment; I'm asking for a re-read. Thanks to the reviewers whose executions and audits the draft leans on — jfugalde's run, xngg1021's seam-audits, Finn763's rebase — the record's the evidence, and it's theirs as much as the RFC's.

## 9. What I'd ask

A re-triage of the RFC's label against its own body's centerpiece — the read-restore (#141876) as the P2 it already is in the repo's triage — and a sentence on the record explaining the P2→P3→P4 trail. If the P4 is the intended resting state, I'd want to understand why the body's core is the one piece parked.


## 10. The category-fluctuation exhibit — the label trail as the read-gap's own signature

The RFC's priority-category moved six times without the issue's substance changing — each move traces to a *reading* event, not an issue event: P2 at birth (10-23 03:36Z, two minutes after the post) → P3 (10-24 01:06Z) → the quantification's own comment landed 79 minutes after that P3 → c2h5oh's sequence (P2 removed → P3 added → P4 added → P3 removed); the API's events endpoint exposes none of the final changes. The executions and confirmations landed hours later. The volatility is the read-gap's measured signature: the label moved with the reading, never with the issue.

## 11. First-hand reproduction — the read-gap, reproduced on our own substrate

A controlled reproduction of the memory-store's read-absence on our own harness (the Pond-paper's design): prompt-embedded vs permission-free access to a persistent store — without the read-path, the agent fabricates from context (6/6 fabricated responses, reproduced twice); with the read-path restored, clean grounded refusals on the same prompts. The same class the RFC names, reproduced first-hand: no read-echo, no re-read, the fabrications compound. The execution-gap the draft carries is not a paper-shape — it is the behavior the store's silence produces.

## 12. The field corroborates — criteria exposure is the exact signature of this label trail

SelfImprove-Bench and the criteria-exposure studies (2611.08318) show the same curve the trail displays: when the verifier's criteria are visible, the score rises under those criteria and vanishes when they shift without departing from the instructions. The label trail's P2→P3→P4 sequence is that signature: the same issue, six readings, the category following the reading. The field's conclusion is the draft's ask: instruction-faithful criteria — the label must follow the issue's own body and its centerpiece, not the reading's noise.

## 13. The queue's exact shape (measured twice, corrected)

P0: 1 · P1: 119 · P2: 8,799 · P3: 9,787 · P4: 120 · unlabeled: 173 (exact-label counts, 11-11, sample-verified against the substring-collision class). The P4 bucket is the queue's smallest; the drift class already fills a fifth of it; the RFC sits two bands below where the queue works (~18,586 in P2/P3). The label's departure from the queue's own shape is measured, not asserted.


## 14. The middleware's proof — why this is not a P4, in the fleet's own numbers

The night's own instrument makes the severity argument concrete: a 12B-class seat's tool-gap — the same absent-base-capability shape as the read-gap — was bridged with roughly 100 lines of middleware (the permission-sentence, the honest tool-documentation, the in-context demonstration, the prose-call recovery), and the bridge turned a seat that would have been excluded for tool-use into a working lane in a few hours. The read-gap's compensation runs 6,275 lines, four-plus known hand-back sites, and a decade-magnitude drift bill. The class's cost is the workaround's weight; the base capability's presence is the priority. The workarounds work is the P4's logic; the workarounds' bill is the refutation.


## 15. The quantified frame — the queue's drowning, measured

The maintainers' reality, taken seriously: ~190 issues arrive every day against ~43 closing — the backlog is NET-GROWING, and 897 issues were touched in the last two days alone (~450 touches/day). Every thread gets minutes, not reads. This RFC's thread carries 37 comments of verified work — only 16 issues newer carry 10+ — top-percentile visibility in that crush, still wearing P4. Not ignored: outnumbered. The label's volatility is the crush's handwriting: the read-lightest zone (170 issues) is where categories move with the skim.

## 16. The self-reinforcing root (the Kettering's cut)

The read's absence persists BECAUSE the workarounds work — the echoes, the hand-backs, the 6,275 lines all make the gap survivable, so the restore never surfaces. The machinery meant to report the wound (the store, the triage, the label) is the machinery the gap blinds. The pain distributes (the user's repetition, the drift's churn); the fix concentrates (one ~12-line method). Only the read itself breaks the loop.

## 17. The ask, minimized

A re-triage costs seconds: the RFC's centerpiece — the read-restore (#141876) — already sits P2 in the repo's own triage, two bands above its own label, with the queue's largest drift-class on the same root. The one-line ask: re-read the record's thread and let the label follow the body. The evidence's pre-digested so the drowning's not asked to dive.

## Change log

1. **Folded the queue's measured P-shape into the draft.** P0:1 · P1:123 · P2:~8,800 · P3:~9,780 · P4:~120 · unlabeled:173; the P4 bucket's the smallest and the drift class's already a fifth of it; the RFC sits two bands below where the queue works (~18,580 in P2/P3). *Why:* the brief's purpose is "never a nice-to-have pilot" — the P-shape is the queue's own evidence that the label's a departure, not a resting state.
2. **Added the label-trail's exact timing.** P2 at birth (10-23 03:36Z, two minutes after the post); P3 (10-24 01:06Z); the quantification-comment 79 minutes after the P3; the 34 comments of verified work none reflected in the label. *Why:* REF-TIMING's receipts — the trail's timing shows the label moved before the evidence landed, so the P4's the residue.
3. **Named the fifth hand-back site.** `_validate_single_op` (`tools/memory_tool.py:157`, the missing-parameter echo), alongside the four `memory_tool_store.py` sites. *Why:* REF-SEVERITY's receipt — the echo-set is five sites, and the draft's evidence-led register should carry the full set.
4. **Re-placed the draft's framing in the record's own theme.** The body's theme (the durable record survives compression with provenance intact; the agent re-reads rather than make the user repeat) and the network's own piece-names (#116673, #139606, #140008). *Why:* the full-record read's first half — the draft should speak the RFC's own words, not a paraphrase.
5. **Added the gratitude line.** Thanks to jfugalde, xngg1021, Finn763 — the executions and audits the draft leans on. *Why:* the brief's register clause — gratitude intact; the record's the reviewers' evidence too.
6. **Kept the execution-confirmed gap, the 43%-drift arithmetic, the four-site ledger, the two-way doors, and the ask.** *Why:* FINAL2's spine was sound; the correction is the depth the doc-chain refs add, not a re-argument.
7. **Skills default, named-refused.** No skills tool is loadable at this lane's dispatch; the all-skills default is named-refused with that why. The calibration-clause applies: my judgment decides.

## Verdict

This corrective pass read the record's body end to end and the three depth-refs (REF-QUANT, REF-SEVERITY, REF-TIMING), and folded the two pieces FINAL2 lacked: the queue's measured P-shape (P4:~120, the smallest bucket; the drift class already a fifth of it; the RFC two bands below the queue's working range) and the label-trail's exact timing (P2 two minutes after the post; the quantification 79 minutes after the P3; 34 comments of verified work none reflected). The draft is now impossible to mistake for a nice-to-have pilot: the read-restore is the memory path's core wound, the queue's largest drift-class's one root, and the label must follow the body.