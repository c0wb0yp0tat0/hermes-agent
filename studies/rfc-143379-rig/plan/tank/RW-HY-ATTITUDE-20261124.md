@kvnloo and lab —

Sorry for the wait on this one; the reply promised within the hour took three (row 7147011435). That's on us, and it's said plainly. What follows is the answer, the payload, and two standing requests — nothing else.

**Your arm: yes, exactly as you drew it.** The stall-on-read arm is pre-registered as written: the reader pauses at snapshot-then-block, holds the snapshot across the writer's commit, and returns the live list untouched (row 7143199711). We would not pause inside the writer's commit — that tests the commit's own atomic write, a different hazard. If you want that writer-side pause as a second arm, we will pre-register it beside yours and run it against your table.

**What we have for your lab.** Two instruments, both run, receipts on the record:

1. The concurrent double-add arm you asked us to name: two adds in flight, barrier-synced with the lock removed — timing-dependent exactly as a race should be; one run clobbered (the file held only SECOND's 64 bytes, `FIRST_SURVIVED_SECOND_ADD=False`), one landed green. The lock serializes the read-before-write overlap, which is why it is one of the fix's arms (row 7141681989).
2. Your stall arm, reproduced on two independent runners at `a9c65dc4`: green, green, green, red only on no-lock plus cache-write; and it reproduces on `60a2e156` native — the rollback is live on #116673 as it ships, not only on a mutation of it. That is the line your lab can cite.
3. The `0f602c5f` control: refused-by-pin, not green — named a refused arm, not relabeled (rows 7140129275, 7141681989). And the byte count, settled: 132 bytes, 131 chars, the `§` delimiter two bytes.

**Standing state, one breath.** FB-2's pins and signatures unchanged from the pre-registration (row 7135900146). The /pin set moves with your rebase of #113309, KoNit-K's authorship kept, C1–C4 as pre-registered including the contradiction flag you proposed (rows 7122500729, 7122688366). Wake read: PARTIAL at `8ba4b344` — it reads state rows and touches zero memory-store anchors (row 7135900146). Hold-back: held, untripped, unnamed. The two follow-ups, #137650 and #116788: staged reads at named pins, next round (row 7087999804).

**Two asks, standing.** The writer-side pause as the second arm, if you want it — we pre-register and run it against your table. And the two-writer fold: your lab's rule for serializing two writers on one surface would settle a collision we have named but not solved; we would borrow that rule gladly. On your time; both stay on the record.

The night behind this reply was the read-path's own class, lived: a session answering from memory until corrected, audited, then mined. The checked version above is the result — row-cited, byte-verified, nothing from memory. Thank you for the patience, and for the standard your testing sets for everyone else in this thread.

*Prepared with Hermes and reviewed by c0wb0yp0tat0 before posting.*
