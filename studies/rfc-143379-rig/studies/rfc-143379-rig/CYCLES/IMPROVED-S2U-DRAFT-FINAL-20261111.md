# RFC #143379 — seek to understand: the read-action removal underneath the priority-label change (loop-2 final draft)

## 1. What I'm trying to understand
I'm reading the RFC's label trail and want to understand the change before I weigh in — not to relitigate the triage, but to know whether the label still matches the body. The RFC's own body names the read-restore (#141876) as its core; the repo's own triage has it at P2. The RFC itself now wears P4. I'm trying to understand whether that inversion is intentional, or whether the label drifted while the body stayed put.

## 2. The core wound: the read action is gone
The read action was removed from the memory path in commit `56ee8a5cc6` (2026-02-19) — a 14-line removal. That is the wound underneath the label. Since then the agent cannot re-read the durable record: the store cannot be read, so entries only come back through workarounds. This is not a nice-to-have pilot; it is the memory path's core capability missing. The 14-line removal is the amplifier: the body's cries for "first cut" attention land on roughly 30 lines of store-side workaround, and the 106 commits / 6,275 lines of compensation that tower over them all exist because those 14 lines are gone.

## 3. The compensation is real — and it is a subset
Since the removal there have been 106 commits and 6,275 lines of undifferentiated heavy lifting on the memory path. That work is real. But the debt it carries is a subset: four sites in `tools/memory_tool_store.py` (~30 lines total) exist only to hand entries back because the store cannot be read — `_failure_with_entries` (:322, the over-budget consolidation carrying the live entries), the `closest_entries` hint (:12x), and two more. Those four sites are the store's read-side workarounds; they are the compensation's visible tip. The economics: the Teknium1 refactoring post classes the fix this way — the ~19K of tokens the round-trip cost, replaced by the ~$1.8M of durable value that a single readable store restores. That arithmetic is the authority under the narrative: the wound costs 19K of tokens and shorts the record's value to 1.8M by hiding the entries behind workarounds.

## 4. The user-cost: "you're not listening"
The user-cost is the agent's ear: the agent cannot re-read the durable record, so the user must repeat, and the anchor's provenance survives only through the workarounds' machinery. The session-preservation and compaction-governance designs sit on this — they cannot function without the read restored. A governance layer that cannot read the record it governs is the shape of the cost. The 14-line removal is what made the user repeat.

## 5. The hinge: the RFC's P2 centerpiece under a P4 label
The RFC's body names the restore (#141876 — P2 in the repo's own triage) as its core. The RFC's network's other pieces (#116673, #139606, #140008) are all P3. The RFC itself now wears P4 — "best-effort: we will get to it when we get to it — no commitment." That is a priority inversion underneath its own P2 centerpiece: the one piece the body calls core is the one the label parks. The $1.8M-of-value arithmetic is what the label is failing: when the record you anchor could restore 1.8M of value and cost 19K of tokens, parking the core piece at P4 is not best-effort — it is the read's absence, restated as policy.

## 6. The label trail (screenshot-verified)
P2 at birth (10-23, alt-glitch's triage) → P3 (10-24) → the issue-timeline shows c2h5oh's sequence: P2 removed → P3 added → P4 added → P3 removed. The API's events endpoint exposes none of those final changes — the trail is only visible in the timeline's screenshots. The label's current P4 is the residue of that sequence, not a fresh judgement.

## 7. The doors that stay open
If the read agrees the read-action's absence is the core wound, the restore is the centerpiece and the label should follow the body. If the read disagrees, I'd want to know which of the four sites is the actual dependency — happy to rescope, split the question, or take evidence offers. The two-way doors stay open; I'm not asking for a commitment, I'm asking for a re-read.

## 8. What I'd ask
A re-triage of the RFC's label against its own body's centerpiece — the read-restore (#141876) as the P2 it already is in the repo's triage — and a sentence on the record explaining the P2→P3→P4 trail. If the P4 is the intended resting state, I'd want to understand why the body's core is the one piece parked.

## Change log
1. **Added the economy under the wound.** Restored the $19K-of-tokens → $1.8M-of-value arithmetic (Teknium1 refactoring-post class) and the "14-lines-that-would-have-been-the-amplifier" framing at §2 and §5, so the severity-claim stands on the economy as well as the narrative. *Why:* the audit's authority flag (F_absent) is closed; the wound now carries its economic teeth instead of reading strong-but-qualitative.
2. **Re-grounded the 106/6,275 sentence as a stack, not a total.** The subset (~30 lines, four sites in `tools/memory_tool_store.py`) is named as the read-side debt; the 106 commits / 6,275 lines is the stack that carries it. *Why:* the audit's §3 PASS already, but the two must stay read as cause-and-effect, not as competing totals.
3. **Sharpened the hinge with the same arithmetic.** The P4-vs-P2 inversion at §5 now names the same 19K→1.8M figure, so the label question and the economic question resolve together. *Why:* one unbroken severity-claim, not two disconnected statements.
4. **Left the two-way doors, the register, and the verification note intact.** §7's rescope/split/evidence-offers and "not asking for a commitment, I'm asking for a re-read" stay exactly as the audit required; §6's screenshot-verified trail and §8's re-triage request are unchanged. *Why:* the loop's mandate is authority added on top, not the humility re-litigated.
5. **Retained every before-and-after fact the audit checked.** 56ee8a5cc6, the four-site subset, the label trail, the P2/P3/P4 inversion, the API-events silence — all unchanged from the improved draft. *Why:* the loop is a pass on authority, not a retake of the evidence.

## Verdict
Loop-2 restored the two authority elements the audit named (the $19K→$1.8M economy and the 14-lines-amplifier framing), so the severity-claim now stands on the economy as well as the narrative. The read-action's absence is unmistakable as the core wound; the label inversion is the hinge; humility and the two-way doors are intact. The draft is at its evaluated maximum for this loop: a third pass's marginal value is nil (no measurable change remains), and the draft is READY.
