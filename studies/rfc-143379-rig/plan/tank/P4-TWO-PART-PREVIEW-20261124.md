# P4 — THE TWO-PART CHECK-IN + REPLY (preview, NOT posted)

*Staged artifact for the pair's eyes only. The RFC #143379 surface stays QUIET — nothing in this file posts without the operator's word. The only other public surface allowed is PR #1 (the machine cadence's home). Fire date 2026-11-24, after Pass 3's verdicts folded and the Part-2 receipt probe ran.*

---

## PART 1 — THE PILOT CHECK-IN (to @3oltan-seo, lift this part)

@3oltan-seo — your anchor-full wall on a live production contour (row 6360811382), the one you offered as the first field case study (row 6411683234), is why this note exists. Thank you for the field reads (rows 6360811382, 6362735198, 6369077436) and for running the probe on the live contour (row 6515564390).

Here is what moved since your 10-30 probe, held to your own numbers.

Your byte-check, "byte-check: 0 — read missing on this build" (row 6515564390), named the root we have to fix. You put the requirement plainly: "Restore the read action — yes, unconditionally" (row 6360811382). The restore in #141876 is the trajectory that answer points at, and the read-restore ask still leads because of it.

The 96 to 73 to 84 arc is your occupancy, never a score we assigned. You logged 3 844 / 4 000 (96%) before the 29.10 consolidation, 2 930 / 4 000 (73%) after, and 3 376 / 4 000 (84%) at the probe with two standing entries back (row 6515564390). I repeat them as your measure of the wall — the numbers this check-in stands on.

The record's named failing case — a second chain-doc `add` clobbering the first — is now pre-registered as FB-2 at the pinned SHAs (the matrix row 7087999804; our reply row 7135900146), with the removal control (row 7122051629). The scheduled-wake read moved from an open question (same row) to a reported answer in our reply (row 7135900146).

I am not ticking your gate. You wrote, "at 300+ cycles the window must be ≥ 0pp vs baseline (never below), measured at the compression ratios my sessions actually hit (4×–8×) across the whole run, not the headline ratio" (row 6362735198), and, "The K-recency reversal (−3.5pp @300 turns) is not an open question for me — it's a fail condition" (row 6360811382). You called it a survival criterion, not a preference: "«Not worse than baseline» is therefore a survival criterion for me, not a preference" (row 6362735198). We carry it as your hard gate and leave it open. Our own −3.5pp and +1.1pp are disqualified as certificates until the scope bug in our probe is repaired (row 7122051629), so nothing here clears the gate on our word.

The asks come back to you, and the restore-read ask leads. You said it best: "Restore the read action — yes, unconditionally" (row 6360811382). Then run your falsifier and discriminator on the restored read: "falsifier = cold-detail resolution at 90%+" and "Discriminator = miss-rate trend, not the absolute zero" (row 6369077436). Then your contour's next read, when it comes. The boundary you set stands: sanitized evidence, and tell you what to strip (row 6411683234).

Your gate is open, your words are the standard, and our arms are ready when you call it.

---

## PART 2 — THE REPLY TO @kvnloo'S CONFIRM RUN (lift this part)

@kvnloo — thank you. The confirm run at all three pins plus current main (row 7140129275) is exactly the discipline the pre-registration was written for, and your table is honest in both directions. Three corrections land on our side, and one question gets its answer.

**The byte count is yours.** You read the combined file at `a9c65dc4` as 132 bytes and flagged that our 131 was the character count — verified: the `§` delimiter is 2 bytes in UTF-8, so `64 + 1 + 2 + 1 + 64 = 132` bytes / 131 chars. Our execution receipts printed the character count; the record is corrected (fold 2026-11-24).

**The `0f602c5f` control refusal is accepted as a refused arm, not a pass or a fail.** The pin rejects the chain target before action dispatch, so no chain file exists to recover; by the pre-registration's own rule, a control that cannot produce a recovery observation invalidates that arm — recorded as a divergence, not as evidence of an overwrite. Base red at `268bb091` and combined green at `a9c65dc4` stand confirmed; the baseline arm on `0f602c5f` is refused-by-pin.

**Your "both removed" question gets the interleaving, with the runs that show it.** Our "removing both turns red" claim came from your own matrix row 7087999804; the spec §3 borrowed it. Your sequential run at `a9c65dc4` (no lock green, no cache-write green, both removed green) is consistent: the sequential two-add never overlaps a read with a write, so nothing races. The interleaving that turns it red is two adds in flight: both read the current entries, both write, last-writer-wins can drop the first. We ran that arm on our side today at the same pin with the lock removed (barrier-synced concurrent adds, the verbatim `_mutate` path) — and the outcome is timing-dependent, exactly as a race should be: one run clobbered (the surviving file held only SECOND's 64 bytes, `FIRST_SURVIVED_SECOND_ADD=False`); a second run landed green (both entries, 132 bytes) because the second thread's read happened after the first's write. Both receipts are in the record (`fb2-race-probe-out.json`). The deterministic fact is the one you cannot see sequentially: remove the lock and the result stops being guaranteed — the lock serializes that read-before-write overlap, which is precisely why it is one of the fix's three arms. The harness is yours — one commit, no model calls, `PYTHONPATH` to the extracted pin, the same way you shared `evals/fb2/`, whenever it helps the next arm.

The pre-registration's bars stand as written; the divergences (the refused baseline arm, the byte count) are logged as data beside them. Thank you again — your catch of the two-add class, and now your confirm of it, is the reason this falsifier exists.

---

## THE STANDING PROTOCOL (what the pair must know)

- Both parts are PREVIEW — nothing posts without the operator's word. The RFC surface stays QUIET; PR #1 is the only other public surface allowed.
- Part 1's receipts: the P1 digests (contour/field/delta/eye), the 13/13 head-side byte-check, the Pass-1 adjudication (occupancy-not-scores). Part 2's receipts: kvnloo's row 7140129275, our byte-count correction (probed: 132 B / 131 chars), the refused-arm acceptance, the concurrent-race probe result (the file's OWN bytes: `fb2-race-probe-20261124.py` run, FIRST_SURVIVED=False at 64 B).
- One open voice-call from Pass 3 (stepfun's eye): Part 1's close line ("the pilot moves at your pace") read as polite abdication by the small seat, with an honestly-labeled guess confidence. Flagged for the pair; the operator decides whether it stays or gets the joint-ownership fix.

*Prepared with Hermes and reviewed by c0wb0yp0tat0 before posting.*
