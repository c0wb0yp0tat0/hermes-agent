# P2 — The Check-In (preview, NOT posted)

Status: staged artifact for the pair and the operator's eyes only. The RFC surface stays QUIET. Nothing in this file posts without the operator's word. Fire date 2026-11-24, after all four Pass-1 recon landings folded.

---

## THE CHECK-IN (lift this block as Pass 3's subject)

@3oltan-seo — your anchor-full wall on a live production contour (row 6360811382), the one you offered as the first field case study (row 6411683234), is why this note exists. Thank you for the field reads (rows 6360811382, 6362735198, 6369077436) and for running the probe on the live contour (row 6515564390).

Here is what moved since your 10-30 probe, held to your own numbers.

Your byte-check, "byte-check: 0 — read missing on this build" (row 6515564390), named the root we have to fix. You put the requirement plainly: "Restore the read action — yes, unconditionally" (row 6360811382). The restore in #141876 is the trajectory that answer points at, and the read-restore ask still leads because of it.

The 96 to 73 to 84 arc is your occupancy, never a score we assigned. You logged 3 844 / 4 000 (96%) before the 29.10 consolidation, 2 930 / 4 000 (73%) after, and 3 376 / 4 000 (84%) at the probe with two standing entries back (row 6515564390). I repeat them as your measure of the wall, nothing more.

Your two-add catch, the second add clobbering the first, is now the named failing case with a removal control (row 7122051629), pinned at the SHAs on the record (rows 6630249660, 6651356150) and pre-registered as FB-2. The scheduled-wake read moved from an open question (row 7122051629) to a reported answer in our reply (row 7135900146; P1-DELTA).

I am not ticking your gate. You wrote, "at 300+ cycles the window must be ≥ 0pp vs baseline (never below), measured at the compression ratios my sessions actually hit (4×–8×) across the whole run, not the headline ratio" (row 6362735198), and, "The K-recency reversal (−3.5pp @300 turns) is not an open question for me — it's a fail condition" (row 6360811382). You called it a survival criterion, not a preference: "«Not worse than baseline» is therefore a survival criterion for me, not a preference" (row 6362735198). We carry it as your hard gate and leave it open. Our own −3.5pp and +1.1pp are disqualified as certificates until the scope bug in our probe is repaired (row 7122051629), so nothing here clears the gate on our word.

The asks come back to you, and the restore-read ask leads. You said it best: "Restore the read action — yes, unconditionally" (row 6360811382). Then run your falsifier and discriminator on the restored read: "falsifier = cold-detail resolution at 90%+" and "Discriminator = miss-rate trend, not the absolute zero" (row 6369077436). Then your contour's next read, when it comes. The boundary you set stands: sanitized evidence, and tell you what to strip (row 6411683234).

Your gate is open, your words are the standard, and the pilot moves at your pace.

---

## RECEIPTS (row id + file)

- Open, field identity, production contour: rows 6360811382, 6411683234 — P1-FIELD-PILOT-20261124, P1-CONTOUR-PILOT-20261124.
- Gratitude, field reads: rows 6360811382, 6362735198, 6369077436 — P1-CONTOUR-PILOT-20261124.
- Restore-read ask leads, byte-check honored: rows 6360811382, 6515564390 — P1-EYE-PILOT-20261124, P1-DELTA-PILOT-20261124.
- Occupancy 96 / 73 / 84 (his numbers, never a score): row 6515564390 — P1-CONTOUR-PILOT-20261124, ORCHESTRATION-3OLTAN-CHECKIN-20261124.
- FB-2 two-add class at pinned SHAs: rows 7122051629, 6630249660, 6651356150 — P1-DELTA-PILOT-20261124.
- Wake read and reply posting: rows 7122051629, 7135900146 — P1-DELTA-PILOT-20261124.
- Hard gate open, −3.5pp fail condition, ≥0pp bar: rows 6362735198, 6360811382, 7122051629 — P1-CONTOUR-PILOT-20261124, P1-EYE-PILOT-20261124.
- Falsifier / discriminator / sanitized boundary: rows 6369077436, 6411683234 — P1-CONTOUR-PILOT-20261124, P1-FIELD-PILOT-20261124.

## WITNESS NOTES (falsifiers, gaps, register)

- Every quoted phrase of the pilot in the check-in was byte-verified this pass against the raw pull at /root/.hermes/cache/scratch/rfc-143379-comments.txt, with its row id: 6360811382, 6362735198, 6369077436, 6411683234, 6515564390. No phrase rides without a receipt. No phantom knowingly admitted.
- Named gap (wall clause): row 7135900146, the reply's posting, rides on the P1-DELTA receipt only. The read gate closed at line 655 of the raw pull before that row, so its raw bytes were not re-read this pass. Minimal move: re-read the raw pull at row 7135900146 before any phrase from it rides as a quote. No pilot quote in the check-in is drawn from that row, so the prose carries no unverified quote.
- The ≥0pp bar and the −3.5pp reversal are carried as the pilot's gate and fail condition, open and un-ticked, per the Pass-1 binding adjudication. The −3.5pp and +1.1pp named as our own measurements are explicitly disqualified as certificates (row 7122051629), not dressed as a pass.
- 96 → 73 → 84 framed as occupancy throughout, never as a score arc.
- The restore-read ask leads the ask-back; the hard gate reads as a gate, not a preference.
- Register checked: pre-registration's honest voice, em-dash cadence at one per composed sentence, pair-metadata absent (no "the fleet", no "the loops", no "kaizen"), pilot-facing second person throughout. Quotes retain the pilot's own byte cadence.
- Preview only. No posting, no public surface touched, no installs, no remote reads or writes.
