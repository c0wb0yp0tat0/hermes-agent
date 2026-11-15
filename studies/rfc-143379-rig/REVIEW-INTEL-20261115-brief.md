# REVIEW-INTEL SUPERVISOR LANE — the background review's pile, read cold (2026-11-15)

## Your mission
The background reviewer has staged **130 memory batches** (`/root/.hermes/pending/memory/*.json`, ~608 KB, dated 2026-10-21 → 2026-11-15). The operator's framing: the review carries (a) memory-curation items for the rig itself, (b) INTEL on anything and everything it watched — long, full-time watch, unharvested for a while — and (c) POSSIBLE STEERS. Your lane: READ EVERY BATCH COLD and deliver the map + the intel + the steers. You are READ-ONLY — you never apply anything.

## The deliverable (write-first)
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/REVIEW-INTEL-20261115.md`:
1. **THE PILE INVENTORY** (by round 6 — EARLY): total count, date range, per-week counts, the newest 30 batches' ids (the live-relevant set).
2. **THE INTEL DIGEST** (the meat — read the NEWEST 40 batches FIRST, their summaries' tails carry the gold): every load-bearing observation, consolidation note, and STEER the reviewer recorded — each with its batch id as the receipt. Organize by theme (the missions it watched, the surfaces, the mechanisms).
3. **THE DISPOSITION TABLE** — per batch (condensed rows; the old tail may be summarized per-week with the ids listed): APPLY (the head applies) / DISCARD (already downstream or noise) / FOLD (routes to a chain segment — NAME the segment: 001 conventions / 002 lessons / 003 preferences / 004 network / 009 wins). Axes: applicability vs the CURRENT MEMORY.md/USER.md, correctness, conflict, value.
4. **THE AUDIENCE ROUTING** — which batches are the head's anchor material vs the chain's vs the ideal-state sessions' material (the reviewer watches whole sessions; its proposals look for future sessions, not only the head).
5. **THE OWED LIST** — anything you could not read (truncated, unparseable, path errors) — named, never filled.

## Method (budget-shaped)
- Read in SLICES: one terminal call per round that cats/parses ~6-10 batch JSONs (`python3 -c` per file or a small loop; the JSONs are 0.8-7 KB each — a slice fits one call's output).
- Parse schema-tolerant: `created_at` is an epoch FLOAT (str() it first), `id` is the string key, `summary` carries the consolidation note (read it FULLY — the tail is where the gold lives), `payload.operations[]` carries the actual ops (add/patch/remove + old_text/content), `origin` = background_review, `subsystem` = memory|user.
- ORDER: newest 40 first (the current steer material), then the middle, then the old tail (the tail's dispositions may be compressed per-week).
- THE DIGEST lands BEFORE the old tail is read (the intel is the mission's point — write it while fresh, never after budget burns).

## Binding rules
1. EVERY ROUND ENDS IN A TOOL CALL. ONE TOOL CALL PER ROUND. Never batch.
2. WRITE-FIRST: the inventory + section headers by round 3; the intel digest's first tranche by round 8; dispositions rolling in after.
3. Appends ≤ 6,000 chars each.
4. **NEVER run git.** Leave the artifact on disk — the fold commits.
5. Receipts: every intel row carries its batch id. ABSENT stays ABSENT + named.
6. Nothing applies; nothing posts; the RFC/upstream stay quiet. Read-only lane.
7. The file must end > 20,000 chars with all five sections carrying content; if not, keep writing.
