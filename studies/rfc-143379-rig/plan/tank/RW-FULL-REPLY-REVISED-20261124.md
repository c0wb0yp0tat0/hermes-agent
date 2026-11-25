@kvnloo and lab —

The reply promised within the hour (row 7147011435) took longer to land; that overrun is ours, and it goes on the record unsoftened. This is the reply it owes, complete at last, and it starts where you left us: your stall arm, answered directly.

Yes — the arm we pre-register is the one you wrote: the reader's pause at snapshot-then-block in `store.read("doc:…")`, held across the writer's commit in the gap. Your fresh ten-run sweep at both pins (row 7143199711) matches it exactly: green, green, green, red only on no-lock plus cache-write at 0/10. The boundary is yours; the register is ours to hold.

**the stall arm**

We register the pause at snapshot-then-block, not inside the writer's commit. The race lives at that boundary: the reader takes its disk snapshot, then blocks on the Event before its return, while the writer commits `store.add("doc:…", "latest")` in the gap. Your fresh run of ten iterations per variant at both `a9c65dc4` and `60a2e156` (row 7143199711) matches the arm exactly, green, green, green, and red only on no-lock plus cache-write at 0/10 with `['initial'] == ['initial', 'latest']`. That is the boundary your stall defines, and we register it as written. Pausing inside the writer's commit tests that commit's own atomic write, a separate hazard, and we do not fold it into this row. If you want the second arm, we will pre-register it beside this one and leave this bar untouched.

**the bars, unchanged**

Nothing in the four classes below moves the pre-registration at row 7135900146. The failing case stays FB-2, a second chain-doc `add` overwriting the first because `_add_doc` writes the note's `content` as the whole file rather than appending a record, with the ungated signature `FIRST_SURVIVED_SECOND_ADD = False` and the fix signature `FIRST_SURVIVED_SECOND_ADD = True`. The three pins stand: the read-less MAIN baseline `0f602c5f6f18615632535251d62a2db74ce93b69`, the class's home `268bb09147eaf948ece6a1beecd92a2268a5fc95`, and the combined GREEN reference `a9c65dc43db9000e8b6e238b50916aa6fa32ff08`, equivalently composed `ec649ad9`. The single-add removal control stays green on the two pins that accept the chain target (`268bb091` and `a9c65dc4`), and refused-by-pin on `0f602c5f`, a refused arm, not a pass or a fail (row 7141681989). A RED there invalidates the probe, never the finding. Divergences are receipt entries, never renegotiated bars.

**the record, straight**

One correction to the record before anything else. Our confirm-run reply is row 7141681989, posted 2026-11-24 19:09Z, where we logged the byte-count and control-refusal divergences. Row 7140129275 is your confirm run, not ours, and the earlier beat that attributed it to us was wrong. The channel finding from the same week, 0/40 then 26/40 then 31/40 then 29/40 at about 70%, and the battery's INCONCLUSIVE verdict, sit on the substrate thread at row 7141681989 and are noted here only as that same-week finding, never as the center of this reply. Your test, your name, your sha, your receipts — credited as yours.

**the open threads**

You accepted all three framings at row 7122500729: the control surface over the method, the second witness the summary does not author, and the cap as a refusal boundary rather than an eviction rule. You accepted the fourth, the contradiction flag, at row 7122688366, with the check running on the pins and never a vote across summaries. We pre-registered four conditions at row 7135900146. C1 is 100% survival across four compactions byte-verbatim, RED on MAIN, GREEN on the branch, and the removal control RED. C2 is the stated cap with plain refusal and no eviction. C3 is no second store, one entry in decision ledger #113309 byte-compared to its own schema. C4 is the contradiction-flagged row, accepted as written.

On the #113309 rebase, you take it as-is onto a branch with KoNit-K's commits and authorship kept, and you stack /pin as a separate commit, all at row 7122500729. We confirm the ledgers move with your rebase and /pin rides atop them as its own commit.

The redaction pass is a general pass built for reuse, scoped to compaction events and session-arc headers only, with stripping rules as in the test corpus. The curve paper sits on top of it as secondary, as you framed at rows 7122500729 and 7122688366.

The scheduled-wake question is ours to answer, and the read of the branch goes beside the question, per row 7122051629. Here is that read. It is PARTIAL at `8ba4b344766e50c2e3eeaba84f4349276a1be021` (row 7135900146). Scheduled wake reads `state.db` and `state.py`, writes its own session rows, and hits zero on every memory-store anchor, with the memory-store write path untouched, so the wake cannot disturb it.

The sibling seam, async-delegation completion picked as "User asked", stays held until our local row lands, per row 7122051629. If no local row lands, the phrase drops from the record.

On your second-pair-of-eyes questions at row 7087999804, #137650 salvage on MAIN and #116788 unattended add, we do not yet hold a stance we can put on the record, so we name the follow-up: a staged read at named pins for each, reported in the next round.

**the hold-back class**

One class remains held by clause. The pre-registration at row 7135900146 withheld it deliberately, its signature not written where a runner can read it. Your confirm at row 7140129275 did not report tripping it, and we record it as not tripped. It stays withheld until the conditions its clause names are met, and we refer to it only as the hold-back class.

**the ask back**

Your run confirms base-red, combined-green at the fix, the removal control green on the two pins that accept the chain target and refused-by-pin on `0f602c5f` (row 7141681989), and now the stall arm at the snapshot boundary. Divergences are data, so log them in the receipt and leave the bars as written. The door stays open for the second stall arm and for the two follow-ups above.

A finding from the same night, no blame, and audited since. It took twenty minutes for the fresh session that inherited this reply to listen enough to properly skill: to read the standing instructions back, verbatim, rather than work from commentary about them. Same root as the stall above, the read holding a stale view while the writes land, and solar's log-level audit of the failure confirms it on the record: four of five claims CONFIRMED, the fifth confirmed on the read-path defect with one note (the banked read-gap workaround stayed active; the fix was available and unapplied, which is its own finding). The cure is the same one this arm names: the read returns the live list, not the snapshot. It is on the record, and the next loop starts there.

If the pause point should move once you look at it, I'm glad to hear it; a question back is welcome, but the answer above is the decision, not a shrug.

For the thread's wider shape: this arm is the read-path's own nerve, the seam the network here has been restoring since the #116673 read landed — the wall's side of this same week sits on the earlier row (7141681989), and your receipts and ours now rest on the same boundary. The seam's full set, the acceptance rows, and the ledger all move with the reply above; nothing in this row retires FB-2 or the redaction pass. The thread's next turn is yours.

*Prepared with Hermes and reviewed by c0wb0yp0tat0 before posting.*
