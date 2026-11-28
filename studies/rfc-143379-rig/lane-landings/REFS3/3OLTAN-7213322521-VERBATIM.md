# 3OLTAN-7213322521-VERBATIM.md — VERBATIM thread comment (3oltan-seo, 2026-11-27T08:15:15Z)

Source: RFN 143379 comment 7213322521. This is the ask-set the lane mines. Quoting the body whole below (quoting = the lane quotes/refers, never rewrites).

----

On the child (child-RFC, read-restore) — the form is right, and thanks for the separation: the read defect as its own ticket, the substrate apart, nothing dragged along. That's exactly what survives triage instead of drowning in doc-chain.

On "where the diff could trip" — three points, all from the field, not the lab:

**1. Sanitize asymmetry across echo sites.**
The RFC says "BLOCKED withheld, `closest_entries` stops echoing it on either path." My question: is "either path" all four echo sites (over-budget echo, nearest-entry hint, replaced-entry fields, batch echo), or just `closest_entries`? Read is restored — but while the agent still answers through the remaining echo compensations during the transition, BLOCKED text can leak the same way it did before, just past the read. If sanitize covers only read, and the echo sites aren't passed through the same filter, the hole is half-closed.

**2. Windows lock, not just fcntl.**
The regression test on real fcntl is POSIX-only. Hermes is cross-platform (I run a live Windows instance in my contour — my brother's). On Windows there's no flock/fcntl in the same form — `msvcrt.locking` / another path. If the test only checks the POSIX lock, the fix goes green on Linux/macOS but on Windows the read may not hold a real lock — and that goes unnoticed. The diff must cover the Windows lock variant too, otherwise a contour where the store is read on Windows stays unverified.

**3. Miss semantics: "failed read" ≠ "read not attempted."**
"A failed read attempt logs a miss" covers the case where read is called and doesn't find the record. But the discriminator runs on the other axis: "misses rise when read is absent, fall when restored." If read is restored but the agent — by habit/compatibility — doesn't call it, the miss rate doesn't fall, and it looks like "the fix doesn't work" when in fact "the agent hasn't relearned." A second counter is needed — read-invoked, not just read-failed. Otherwise you can't measure the restoration itself: without it, you can't tell "read is broken" from "read isn't being called."

This isn't a critique of the form — the form is right. It's three places where the fix in production gives "green test, live hole."

On filing — I agree with the regular issue. §3.2: incorrect output isn't a vulnerability, it's an ordinary output defect. An advisory isn't needed; it only slows it down.

On the final "what would move the fix at triage" — narrower first slice. Read-restore as the minimal diff (as already done), without doc-chain, without `_add_doc`, without the gate. Merged-first — no: it mixes read-restore with the substrate and stalls exactly the thing that should merge first.

The pilot isn't abandoned — I have my own instrument (occupancy + discriminator); I report numbers as they occur, at my cadence.


