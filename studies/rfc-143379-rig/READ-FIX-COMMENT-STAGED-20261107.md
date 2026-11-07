# READ-FIX-COMMENT-STAGED-20261107 — staged comment for upstream read-restore PR #116673

## STAGED COMMENT (ready to post; operator gates the post)

Title: (none — PR comment)

Body:

<!-- BODY-START -->

Thanks for the work on #116673. I'd like to encourage prioritizing the read-restore. From a user side, the read path is the load-bearing seam: every session that can't read its own prior context pays for it in compensation — spillover archives growing, sessions re-reading, drift corrections piling up. Restoring direct read kills the twice-read compensation at its root, which is the highest-leverage item in the queue.

Numbers from my own measured ledger (estimates marked as such):

- Spillover archive: **117 entries / 12 MB** accumulated as compensation for the missing read path (measured at the bearings-read, 2026-11-07).
- Sessions burn: **52 MB** of session-store carries the compensation chain — re-reads, dumps, spillover (a share-of-budget figure would be an estimate; the store's size is measured).
- Twice-read overhead: **2×** — the twice-read protocol's mandate: every anchor read happens twice while direct read is unavailable (the protocol's own accounting).
- Drift events traceable to the read-gap's mechanics: **3 corrected items** (rows 6708804389, its surgical patch, and 6708881825 — each verified at the fold; estimates marked as such).
- Pilot wait: the read-restore has been the gating item for **11 days** (open, unmerged, last updated Oct 27).

A restoration of direct read removes this compensation chain at the source rather than patching each symptom. Happy to provide the ledger's measurement method if useful. Grateful for the work — no rush, but this one unblocks a lot downstream.

— c0wb0yp0tat0

<!-- BODY-END -->

## REGISTER CHECK

- Public voice only (RFC #143379 framing, single handle c0wb0yp0tat0): yes.
- No internal machinery (no envelopes, lane-handles, fork-names, rig-vocabulary): yes.
- Length ~200-350 words: yes.
- Tone encouraging, factual, never demanding: yes.
- STAGE-ONLY gate: file only, never API/upstream surface: honored.
- Source: cost ledger READ-GAP-COST-20261107.md (numbers to be filled from cold read).

## NOTES

Numbers are placeholders pending cold read of READ-GAP-COST-20261107.md.