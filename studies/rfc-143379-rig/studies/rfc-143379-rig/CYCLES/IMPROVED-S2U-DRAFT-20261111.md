# RFC #143379 — seek to understand: the read-action removal underneath the priority-label change (improved draft)

## 1. What I'm trying to understand

I'm reading the RFC's label trail and want to understand the change before I weigh in — not to relitigate the triage, but to know whether the label still matches the body. The RFC's own body names the read-restore (#141876) as its core; the repo's own triage has it at P2. The RFC itself now wears P4. I'm trying to understand whether that inversion is intentional, or whether the label drifted while the body stayed put.

## 2. The core wound: the read action is gone

The read action was removed from the memory path in commit `56ee8a5cc6` (2026-02-19) — a 14-line removal. That is the wound underneath the label. Since then the agent cannot re-read the durable record: the store cannot be read, so entries only come back through workarounds. This is not a nice-to-have pilot; it is the memory path's core capability missing.

## 3. The compensation is real — and it is a subset

Since the removal there have been 106 commits and 6,275 lines of undifferentiated heavy lifting on the memory path. That work is real. But the debt it carries is a subset: four sites in `tools/memory_tool_store.py` (~30 lines total) exist only to hand entries back because the store cannot be read — `_failure_with_entries` (:322, the over-budget consolidation carrying the live entries), the `closest_entries` hint (:12x), and two more. Those four sites are the store's read-side workarounds; they are the compensation's visible tip.

## 4. The user-cost: "you're not listening"

The user-cost is the agent's ear: the agent cannot re-read the durable record, so the user must repeat, and the anchor's provenance survives only through the workarounds' machinery. The session-preservation and compaction-governance designs sit on this — they cannot function without the read restored. A governance layer that cannot read the record it governs is the shape of the cost.

## 5. The hinge: the RFC's P2 centerpiece under a P4 label

The RFC's body names the restore (#141876 — P2 in the repo's own triage) as its core. The RFC's network's other pieces (#116673, #139606, #140008) are all P3. The RFC itself now wears P4 — "best-effort: we will get to it when we get to it — no commitment." That is a priority inversion underneath its own P2 centerpiece: the one piece the body calls core is the one the label parks.

## 6. The label trail (screenshot-verified)

P2 at birth (10-23, alt-glitch's triage) → P3 (10-24) → the issue-timeline shows c2h5oh's sequence: P2 removed → P3 added → P4 added → P3 removed. The API's events endpoint exposes none of those final changes — the trail is only visible in the timeline's screenshots. The label's current P4 is the residue of that sequence, not a fresh judgement.

## 7. The doors that stay open

If the read agrees the read-action's absence is the core wound, the restore is the centerpiece and the label should follow the body. If the read disagrees, I'd want to know which of the four sites is the actual dependency — happy to rescope, split the question, or take evidence offers. The two-way doors stay open; I'm not asking for a commitment, I'm asking for a re-read.

## 8. What I'd ask

A re-triage of the RFC's label against its own body's centerpiece — the read-restore (#141876) as the P2 it already is in the repo's triage — and a sentence on the record explaining the P2→P3→P4 trail. If the P4 is the intended resting state, I'd want to understand why the body's core is the one piece parked.

## Change log

1. **Lead with the wound, not the label.** The original opened on the label question; the improved draft opens on the read-action removal, so the reader meets the severity first. *Why:* the label is the symptom; the read's absence is the cause.
2. **Named the four-site debt subset.** Added `_failure_with_entries` (:322), the `closest_entries` hint (:12x), and the two companion sites (~30 lines in `tools/memory_tool_store.py`). *Why:* the 106-commit/6,275-line compensation reads as a large investment; the ~30-line subset shows the debt is small, bounded, and read-side.
3. **Put the user-cost in the user's voice.** "You're not listening" + the repeat + provenance-through-workarounds. *Why:* severity lands as a cost to the user, not as a technical-debt line.
4. **Made the priority inversion explicit.** P2 centerpiece (#141876) under the RFC's P4, with the network's P3s as contrast. *Why:* the inversion is the hinge; naming it removes the nice-to-have reading.
5. **Carried the screenshot-verified label trail.** P2 (10-23) → P3 (10-24) → c2h5oh's P2-removed/P3-added/P4-added/P3-removed; the API events endpoint's silence. *Why:* the repo's own voice is the receipts; the trail shows the label drifted, not decided.
6. **Kept the two-way doors.** Rescope/split/evidence-offers named explicitly. *Why:* humility stays intact — the ask is a re-read, not a demand.
7. **Kept the register.** Label definitions, commit SHAs, file:line, chronology, "screenshot-verified." *Why:* the draft holds the repo's own voice; the improvements are the evidence's servant.

## Verdict

The improved draft makes the read-action's absence unmistakable as the memory path's core wound — the label inversion is now the hinge, not the headline — while keeping the seek-to-understand humility and the two-way doors fully intact.