# THE READ GAP — a safety defect in the memory store

Parent: #143379 · Cross-link: "narrow spin-off — the read-restore path only" · Lane: the regular lane, open source first — the same lane any contributor would use. Routing note: per [SECURITY.md §3.2](https://github.com/NousResearch/hermes-agent/security), the incorrect-output/hallucination class is not a vulnerability under this policy; the policy welcomes it as a regular issue — filed here, not as an advisory.

@3oltan-seo, @kvnloo, and the room: the read gap as its own ticket — separated from the doc-chain substrate, receipted like the thread's own work.

*Revised 2026-11-28: read-invoked; msvcrt; anchor-first; narrower slice; 6609dac rows; #12831; remove-echo.*

## The problem, stated

Expected: an agent reads the memory store for its own record, misses are visible, and the user never has to repeat themselves. Actual: on current main, asking the store for its entries answers "Unknown action 'read'" (jfugalde's execution, comment 6386263138; @kvnloo's probe, comment 7087999804); without the read path, an agent fabricates responses 6 of 6, twice, and one non-punitive abstention sentence restored refuses cleanly 12 of 12 (comment 6815556328); and a miss leaves no trace, because there was no read attempt (comment 7192744535). The gap in one line: the read path was removed in 56ee8a5cc6 (the 14-line deletion, 2026-02-19) and compensated for ever since — four sites, ~30 lines, that hand entries back without ever reading the store (measured at comment 6386263138).

## SBI — situation, behavior, impact

- **Situation.** The compaction era removed the read action and rewrote history into a summary. Anchors run packed — 96% at the wall, then 73, then 84 as the contour walked (comment 7192744535).
- **Behavior.** A topic goes cold; there is no read tool to check the record; the agent answers from the summary — formally confident, byte-accurate, the premise possibly wrong. The recorded session did exactly this: it answered from its summary of the record instead of reading it back, and the repair was one line, read the original ask verbatim before building anything (comment 7154275288).
- **Impact.** The read-suite reproduces 4 of 4 failures on main at the predicted call-shape errors, green at the restore (comment 7122051629). Users hear "you're not listening." The read's absence is a fabrication pump — a hazard, not an innovation gap.

## The five whys

1. **Why do users get confident wrong answers about their own record?** Because the agent answers from the summary, not from the memory store.
2. **Why does it answer from the summary?** Because there is no read action it can call — the store answers "Unknown action 'read'" on main.
3. **Why is there no read action?** Because it was removed in 56ee8a5cc6 and the echo-sites grew in its place — the over-budget echo, the nearest-entry hint, the replaced-entry fields, the batch echo (comment 6386263138).
4. **Why was the compensation accepted instead of the restore?** Because the removal looked like a design choice — the summary replaced the record — and nothing inside the system signaled that a read was missing.
5. **Why did nothing signal it?** Because a miss without a read attempt leaves no trace: no log, no counter, no echo. Only the fabrication broke the surface — "you're not listening." **Root: the read's absence was compensated instead of restored, and the absence was silent by construction — so the fix must restore the read, make the miss audible, and make the absence audible too.**

## The fix — the smallest diff

The store's read path only:

- `MemoryStore.read` restored — the 12-line method per #141876, as hardened by jfugalde's review (comment 6399028865): the snapshot under the store's own `_file_lock` (main's two-writer rule); stateless — it never writes the live list, so a stale view cannot roll a writer's commit back; sanitized — BLOCKED text is withheld, and `closest_entries` stops echoing it on either path (jfugalde's measured seam, comment 6399028865).
- A failed read attempt logs a miss — a signal, not a silent absence (@3oltan-seo's discriminator, comments 6369077436, 6376772075). A second counter, read-invoked, makes the absence audible: every call increments; restored (invoked > 0, misses falling), broken (invoked > 0, misses flat), not called (invoked = 0) (@3oltan-seo, comment 7213322521; prototype 6/0).
- One regression test with real fcntl — the **structural flock check**: a non-blocking flock on `MEMORY.md.lock`, taken while the read holds it, must fail (contention errnos: EACCES, EAGAIN, EWOULDBLOCK — per the lock-fidelity harvest, 2026-11-27). The guarded property is **stateless**: the live list unchanged after a read that races a writer. The same check runs under `msvcrt.locking` (native Windows 3.14.7), so both backends are covered (@3oltan-seo, comment 7213322521).
- The remove-success confirmation is the one live echo: it quotes the matched raw entry (reproduced 2026-11-28); it now quotes the sanitized marker or omits the text. The batch echo's dispatch import is an installed-runtime boundary.

**Why not rely on the prompt (#12831).** The prompt is a frozen snapshot; a cold topic's detail is exactly what compaction or the budget pushes out by the turn. The read is the on-demand path back to the record when the snapshot no longer carries it (PR #12831, teknium1, 2026-04-20; comment 7192744535).

One small diff — not a new mechanism. The write-gate's read-back seams (the batch-path bypass, the single-op blind spots, comments 6630249660) stay with the write-gate's own review, per jfugalde's advice: "let the maintainers answer the inventory question instead of settling it in a patch" (comment 6399028865).

## Separated — out of this ticket (named, parked)

- **The doc-chain substrate**: the bounded read's chain semantics (#116673), the chain-doc write path (`_add_doc` — the locked re-read → append → write, the replace retirement, @kvnloo's prescriptions at comments 7181202866 and 7186196454, the FB-2 class with its hold-back clause, the moved-gate arm) — stay in the RFC's thread and the substrate's own future home. Nothing here depends on them.
- **Compaction governance**: the K-recency window, the provenance work, the gate (≥0pp at 300+ cycles, 4×–8×, whole run — open, unticked, and belonging to the compaction work's home; comment 7155126154).
- **The pins and the frame** (34/34 at the pinned commit — the substrate's practice, kept in the substrate's home).
- **The anchor-first read rule** (@kvnloo, comment 7210367328): on the combined store the anchor's lock covers everything the response derives from the anchor (bar: real fcntl 50/50, nulled 50/50, whole body 0/50). #141876 has no `chain_docs`; it ships with the combined read.

The thread's registered promises — the team-up on the `_add_doc` diff, the hold-back clause — stay where they were registered, on the RFC's thread. This ticket is the read alone.

## The correctness envelope (the read's bar)

The restored read's concurrency envelope: the reader holds the store's lock across the snapshot and never writes the live list; the harness's waits are gone, so contention is the lock's own signature — the structural check (above), not an output-level red. @kvnloo's arm (comment 7187597182), adopted as probe revision 5: three hundred fresh runs per row — rows one to three 0/300, the fourth (both protections removed) 300/300, receipt `fbefb4ac…e16`, prediction `08103259…` committed before the first run, one wording difference on the record (the receipt's bar line carries a phrase from the design document; the results match the prediction exactly). The phase-1 kit receipt: `3ff6aee4…fba9`, three cold confirmations. The run happened on the combined store (`a9c65dc4`); the re-run against #141876 alone is part of the landing, pre-registered in the same envelope. @kvnloo's re-run on #141876's own file at `6609dac` (file sha `a43818a6…1586a`, py3.15.2, macOS, 50 trials): 0/1,028 + 0/6,566 non-prefix; 50/50 + 50/50 complete; refused 50/50 vs acquired 50/50 — unregistered until the prediction commits and the cold re-run posts its hash (comments 7211318206, 7210367328).

**The kit — one command.** The same phase-1 kit @3oltan-seo ran is here: [THE READ KIT](https://gist.github.com/c0wb0yp0tat0/28594f78bd9662013eb586d26cffc77e) — clone it, `sh RUN.sh`, and the receipt is the output (the reference receipt `3ff6aee4…fba9`; the revision-5 envelope `fbefb4ac…e16`). It states its own perturbation — what it touches, what it costs, nothing outside its sandbox — and it is runnable on any contour; the README says what the check requires. Participants can test themselves; the kit is the test.

## The pre-registration

- **Falsifier** (@3oltan-seo, comments 6362735198, 6369077436, 6376772075): cold-detail survival at 90%+ memory — a turn touching a referenced topic gets the detail in-context.
- **Discriminator** (@3oltan-seo, comments 6369077436, 6376772075): the miss-rate trend — misses rise when read is absent, fall when read is restored; a single cold-pointer miss is a logged signal, not a failure. The three-state read-invoked carries the absence axis: invoked zero means the read is not being called, not that it is broken.
- **The Read-Restore Eigenvector Bookkeeper — a special-use-case instrument** (P3-EIGEN, candidate 4; allowed here for the pilot's tracking, not part of the fix): pins as explicit eigen-axes, the affected set as rows, projection error per class through the sanitize seam. Candidate, class-checked, not adopted; the pilot's tracking instrument, its own sheet if preferred.
- **The pilot's field check** (comment 7192744535): the full envelope ships cold, one command, a predicted receipt and sha256, run and hash-compared — at the pilot's cadence. Every shipped instrument carries one line stating its own perturbation: what it touches, what it costs, nothing outside its sandbox. The contour is production with real stakes — nothing lab-shaped is asked of it; its own numbers (occupancy, falsifier, discriminator) are the field instrument, reported as they occur.

## Open questions

- Merged-first experiment or a narrower first slice — answered from the field: narrower first slice, read-restore as the minimal diff, no merged-first (@3oltan-seo, comment 7213322521). The child's naming and lane placement remain.

## The close

"One ask, in one breath: what would move the read-gap fix at triage? If the shape is wrong — a merged-first experiment, a narrower first slice, more evidence — name it, and it is our next job."
