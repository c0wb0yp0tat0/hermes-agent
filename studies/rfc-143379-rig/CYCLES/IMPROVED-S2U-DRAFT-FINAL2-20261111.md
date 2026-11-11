# RFC #143379 — the corrective final: the read-restore, quantified by the record's own thread

## 1. What I'm trying to understand

I'm reading the RFC's full record end to end — body and all 36 thread comments — and the label trail. The body names the read-restore (#141876) as its core; the repo's triage has it P2. The RFC itself wears P4. Underneath the label question is the severity question: is this a nice-to-have pilot, or the memory path's core capability missing? The thread's own numbers answer it. Reading the whole record, the pilot framing collapses — the read is the centerpiece, the compensation, and the evidence.

## 2. The core wound — execution-confirmed

The read action was removed in `56ee8a5cc6` (2026-02-19) — a 14-line removal. On current main the tool answers `Unknown action 'read'`; against the same scratch store, #141876's head returns the entries plus the usage line, first try. The gap is verified by a reviewer's execution (jfugalde, 10-24), not just the RFC's own runs. The #139606 head's collection-error is a stale-base artifact — it predates `95610a5db4`'s pathlib fix — so there is no read-bug behind it; Finn763's rebase of #116673 (head `ffc651bd11`) is clean and mergeable.

## 3. The quantification the record actually carries

The operator's comment-work (issuecomment-6378725575, 10-24): of the 300 most recent open issues, 43% (130) sit in the drift class — the session, the memory, the context, the compression, the state, the persistence, the recovery. Extrapolated to the ~16,900 open: ~7,300. At a conservative 100 lines per fix: ~726,000 lines — the 6,275 lines of compensation, ~116× over. At 8 hours per fix: ~58,500 hours — ~1,460 person-weeks. The root: the read's absence at the memory-store level. Throughput: 19,930 closed at ~43/day; 16,878 still open; the backlog ~46% of the total work; the oldest open 234 days; if 43% holds across closed, ~8,570 drift-tickets already closed — the same root, the same class, the same bill. "The drift's the compounding, not the clearing." The read is the best-and-foremost decision — "the trust is the product."

## 4. The compensation's true shape — the execution ledger

The ledger counts 106 commits and 6,275 lines (3,541 added, 2,734 deleted) since `56ee8a5cc6`. The debt's a subset: the code that exists only to hand entries back because the store cannot be read — four sites in `tools/memory_tool_store.py`, ~30 lines: `_failure_with_entries` carrying `current_entries` on the over-budget add (:322), the zero-match `closest_entries` (:124), the replaced-entry fields the successful write echoes (:481/:488), and the batch-abort's echo-fix that later removed `current_entries` because the echo made retries worse (#97316, :331). Give the agent `MemoryStore.read` (the 12-line method #141876 puts at :369) and these echoes are the obvious first cut. The rest is adjacent work that stacks on the symptom rather than closing it.

## 5. The user-cost

The user-cost is the agent's ear: the agent cannot re-read the durable record, so the user must repeat, and the anchor's provenance survives only through the workarounds' machinery. A governance layer that cannot read the record it governs is the shape of the cost.

## 6. The hinge: the P2 centerpiece under a P4 label

The RFC's body names the restore (#141876 — P2 in the repo's own triage) as its core; the network's other pieces are P3; the RFC itself wears P4 — "best-effort: we will get to it when we get to it — no commitment." The trail is screenshot-verified: P2 at birth (10-23, alt-glitch's triage) → P3 (10-24) → c2h5oh's sequence (P2 removed → P3 added → P4 added → P3 removed); the API's events endpoint exposes none of the final changes. The P4 is the residue, not a fresh judgement.

## 7. The doors that stay open

If the read agrees the read-action's absence is the core wound, the restore is the centerpiece and the label should follow the body. If the read disagrees, I'd want to know which of the four sites is the actual dependency — happy to rescope, split the question, or take evidence offers. The two-way doors stay open; the one-way door's flagged (archive-before-stub's ordering). I'm not asking for a commitment; I'm asking for a re-read.

## 8. What I'd ask

A re-triage of the RFC's label against its own body's centerpiece — the read-restore (#141876) as the P2 it already is in the repo's triage — and a sentence on the record explaining the P2→P3→P4 trail. If the P4 is the intended resting state, I'd want to understand why the body's core is the one piece parked.

## Change log

1. **Re-read the full record end to end** — body, all 36 thread comments, every section, every comment, from the first line to the last. The prior final read the body-extracts only; this final reads the whole record, so every number below is traceable to the thread, not to the body-note's paraphrase.
2. **Re-placed the quantification around the record's true numbers.** The prior final carried the body-note's generic framing and the thread's numbers without the record's full context. This final carries the operator's drift-class arithmetic: 43% (130) of the 300 most recent open issues; ~7,300 of ~16,900; ~726,000 lines at 100 lines/fix; ~116× the compensation; ~58,500 hours at 8h/fix; ~1,460 person-weeks. *Why:* the real quantification lives in the thread (issuecomment-6378725575), and the record's end-to-end read confirms each figure's source.
3. **Added the backlog's full shape.** 19,930 closed at ~43/day; 16,878 open; ~46% of the total work; the oldest open 234 days; ~8,570 drift-tickets already closed if 43% holds. *Why:* "the drift's the compounding, not the clearing" — the closed queue is the same root and the same bill, and the backlog's 46% share is the concrete reason the read is not a nice-to-have.
4. **Replaced the compensation's rough subset description with the execution ledger's four hand-back sites and their receipts.** `_failure_with_entries` (:322), the zero-match `closest_entries` (:124), the replaced-entry fields (:481/:488), and the batch-abort echo-fix (#97316, :331); the ledger's 6,275 = 3,541 added + 2,734 deleted. *Why:* the ledger is the record's own count, with file:line receipts, so the debt is no longer a vague "30 lines" but a precise, auditable subset.
5. **Reinforced the execution-confirmed restore gap.** Current main: `Unknown action 'read'`; #141876's head: entries + usage on the single-op path; #139606's collection-error is a stale-base artifact predating `95610a5db4`'s pathlib fix. *Why:* the gap is verified by a reviewer's execution, not asserted — this is the single strongest evidence point in the thread.
6. **Kept the humility, the two-way doors, and the lean length.** *Why:* the evidence's servant; the ask is a re-read, not a demand.
7. **Kept the register.** Comment IDs, commit SHAs, file:line, the screenshot-verified trail. *Why:* the draft holds the repo's own voice.
8. **Skills default, named-refused.** No skills tool is loadable at this lane's dispatch; the all-skills default is named-refused with that why. The calibration-clause applies: my judgment decides.

## Verdict

This corrective pass read the RFC's complete record end to end — body and all 36 thread comments — and re-placed the draft's quantification around the thread's true numbers: the 43%-drift class, the ~726,000-line / ~58,500-hour / ~1,460-person-week arithmetic, the ~116× over the compensation, the 46%/234-day/8,570-closed backlog, the execution-confirmed `Unknown action 'read'` vs #141876's return, and the four hand-back sites. The prior final carried the thread's headline numbers but the record's end-to-end read — and the verdict's explicit replacement of the prior final's body-note quantification — was the missing leg. The draft is now impossible to mistake for a nice-to-have pilot; the read-restore is the centerpiece and the label must follow the body.
