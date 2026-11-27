# THE READ GAP — a safety defect in the memory store

Parent: #143379 · Cross-link: "narrow spin-off: the read gap, not the doc-chain substrate" · Lane: the regular lane, open source first — the same lane any contributor would use.

@3oltan-seo, @kvnloo, and the room: the read gap as its own ticket — separated from the doc-chain substrate, receipted like the thread's own work.

## The defect

The memory store cannot read its own record. On current main, asking the memory path for its own entries answers "Unknown action 'read'" (jfugalde's execution, comment 6386263138; kvnloo's probe, comment 7087999804). The read action was removed in 56ee8a5cc6 — the 14-line deletion, 2026-02-19 — and the compensations grew in its place: the code that exists only to hand entries back because the store cannot be read (four sites, ~30 lines: the over-budget echo, the nearest-entry hint, the replaced-entry fields, the batch echo — measured at comment 6386263138).

The safety consequence, from the field and the record:

- **The fabrication factory** (3oltan-seo's contour, comment 7192744535): a packed anchor → compaction rewrites history into a summary → a cold topic with no read tool → the answer comes from the summary — formally confident, byte-accurate, the premise possibly wrong, the miss invisible because there was no read attempt.
- **The fabrication pump, reproduced**: without the read path, an agent fabricates responses 6 of 6, twice; the same prompts with one non-punitive abstention sentence restored refuse cleanly 12 of 12 (comment 6815556328).
- **The read-suite**: 4 of 4 failures on main at the predicted call-shape errors, green at the restore (comment 7122051629).
- **The recorded session**: answered from its summary of the record instead of reading it back — the repair was one line, read the original ask verbatim before building anything (comment 7154275288).
- **The users' symptom**: "you're not listening." The read's absence is a fabrication pump. That is a safety issue, not an innovation gap.

## The fix — the smallest diff

The store's read path only:

- `MemoryStore.read` restored — the 12-line method per #141876, as hardened by jfugalde's review (comment 6399028865): the snapshot under the store's own `_file_lock` (main's two-writer rule, tested as shipped at comment 7155449141); stateless — it never writes the live list, so a stale snapshot cannot roll a writer's commit back; sanitized — blocked text is withheld, and `closest_entries` stops handing the BLOCKED text back on both paths (jfugalde's measured seam, comment 6399028865).
- A failed read attempt logs a miss — a signal, not a silent absence (3oltan-seo's discriminator, comments 6369077436, 6376772075).
- One regression test with real fcntl: the correctness envelope below; the test fails when the lock is removed.

One small diff — not a new mechanism. The write-gate's read-back seams (the batch-path bypass, the single-op blind spots, comments 6630249660) stay with the write-gate's own review, as jfugalde advised: "let the maintainers answer the inventory question instead of settling it in a patch" (comment 6399028865).

## Separated — out of this ticket (named, parked)

- **The doc-chain substrate**: the bounded read's chain semantics (#116673), the chain-doc write path (`_add_doc` — the locked re-read → append → write, the replace retirement, kvnloo's prescriptions at comments 7181202866 and 7186196454, the FB-2 class with its hold-back clause, the condition at 7181202866) — park in the RFC's thread and the substrate's own future home. Nothing here depends on them.
- **Compaction governance**: the K-recency window, the provenance work, the gate (≥0pp at 300+ cycles, 4×–8×, whole run — open, unticked, and belonging to the compaction work's home; comment 7155126154).
- **The pins and the frame** (34/34 at the pinned commit — the substrate's practice, not this ticket's).
- The drift-class extrapolations from the RFC body.

The thread's registered arms and promises — the moved-gate arm, the team-up on the `_add_doc` diff, the hold-back clause — stay live on the RFC's own thread, in the substrate's home. This ticket is the read alone.

## The correctness envelope (the read's bar)

The restored read's concurrency envelope: the reader holds the store's lock across the snapshot and never writes the live list; the harness's waits are gone, so only the lock can order the writer. kvnloo's arm (comment 7187597182), adopted as probe revision 5 (`eff109fb2ba313c9713b7fc13fa585f65c9ccd79221a80e34febbefc5dd935d7`): three hundred fresh runs per row — rows one to three 0/300, the fourth (both protections removed) 300/300, receipt `fbefb4ac…e16`, prediction `08103259…` committed before the first run, one wording difference on the record (the receipt's bar line carries a phrase from the design document; the results match the prediction exactly). The phase-1 kit receipt: `3ff6aee4…fba9`, three cold confirmations (comments 7183339657, 7186196454, 7186351716). The envelope ran on the combined store (`a9c65dc4`); the re-run against #141876 alone is part of the landing, pre-registered in the same envelope.

## The pre-registration

- **Falsifier** (@3oltan-seo, comments 6362735198, 6369077436, 6376772075): cold-detail survival at 90%+ memory — a turn touching a referenced topic gets the detail in-context, no add being refused.
- **Discriminator** (@3oltan-seo, comments 6369077436, 6376772075): the miss-rate trend — misses rise when read is absent, fall when read is restored, on the record, in the open. Not the absolute zero: a single cold-pointer miss is a logged signal, not a failure.
- **The pilot's field check** (comment 7192744535): the full envelope ships cold, one command, a predicted receipt and sha256, run and hash-compared — at the pilot's cadence. Every shipped instrument carries one line stating its own perturbation: what it touches, what it costs, and that nothing outside its sandbox moves. The contour is production with real stakes — nothing lab-shaped is asked of it; its own numbers (occupancy, falsifier, discriminator) are the field instrument, reported as they occur.

## The record

- Pins: 0f602c5f (MAIN read-less baseline), ec649ad9 (#141876 composition, 443 pass, dispatch contract 64/64), a9c65dc4 (the combined hardening, the envelope's home) — 60a2e156 (#116673) and 268bb091 (round2-gate) park with the substrate.
- Thread: the RFC thread's full 64 comments, verbatim — 64/64, including 7192744535, 7186196454, 7187597182, 7186351716, 7185328530.
- Starting child sha256: the audited draft was 867cf9ef2b0a47245f2d5cbe84863e6c7a1e32cef4298c66772e9a9fdbfbcf3f; the pre-separation revision was 3481a398a340f09725f9a6e3f542b89cf62b7bcd0ac6591de9b82f5476f48cef; this revision's pre-record content hash was f247715ce9c434ee7b972b357d15b7acb344d5aa199d1eaba17503bafa82b4be, and its final content hash is in the staging notes (both logged 2026-11-26).

## Open questions

- Merged-first experiment or a narrower first slice — one ask, decided by triage.
- The child's naming and its lane placement.
- The triage ask — what moves the read-gap fix; what causes a session to answer from its summary instead of the record (the thread's question, answered in the field at comment 7192744535, instrumented here).

## The close

"One ask, in one breath: what would move the read-gap fix at triage? If the shape is wrong — a merged-first experiment, a narrower first slice, more evidence — name it, and it is our next job. Thank you for the room, and for the patience this thread has shown it."

*Pilot receipt: ENVELOPE GREEN·GREEN·GREEN·RED CONFIRMED; RECEIPT_SHA256 3ff6aee45b16d45b6d8db1084381c6447f549fd01ab72da11c4aedcb5071fba9 (three cold confirmations, unmoved).*

*Prepared with Hermes and reviewed by @c0wb0yp0tat0 before posting.*
