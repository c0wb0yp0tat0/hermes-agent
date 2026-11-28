# DRAFT REPLY — @3oltan-seo (the three points) — STAGED, no posting without the word

@3oltan-seo — thank you. The three points: answered one by one, from the field back.

### 1. Sanitize scope — read's two paths, and the echo sites' leak, named

"Either path" means the read's own two outputs: the `read_entries` list and the `closest_entries`
hint. It does not mean all four echo sites (over-budget echo, nearest-entry hint, replaced-entry
fields, batch echo) — those were inventoried as the compensation on the write/read-back seams and
stay with the write-gate's own review, per jfugalde's posted advice ("let the maintainers answer the
inventory question instead of settling it in a patch").

Your leak is real and it is a transition hole, not a lab question: while the agent still answers
through the remaining echo compensations, BLOCKED text can travel past the read. The child gains a
line in its parked list — "BLOCKED leak through the remaining echo compensations during the
read-adoption transition, field-triggered (3oltan-seo, 7213322521) — routed with the write-gate's
review" — named, tracked, not dismissed. The smallest diff stays the smallest diff.

And the read's own side of it is measured, not promised: the fixed read's view returned the
`[BLOCKED: …]` marker with a blocked-index, and the threat text absent, on all three of our
contours (a43818a6 store; pve1, WSL2, and native Windows — `threat_text_leaked: false` on every
row, receipts in the verification attached to this thread's kit).

### 2. Windows lock — tested on the real contours (not just read)

Agreed, and we stopped reading and started running. The same fixed store ran a full battery on
three real contours — pve1 (fcntl, Linux), WSL2 on the PC (real fcntl, WSL2 kernel), and NATIVE
Windows Python 3.14.7 (real `msvcrt.locking`):

- structural both directions, 50/50 inside / 50/50 outside: IDENTICAL on all three (the
  non-blocking probe is refused while the store holds the lock, and acquires when unheld)
- the live read-held probe: probes were refused while `read()` ran on every contour (25/80 pve1,
  52/80 WSL2, 5/80 native) — the read holds a REAL lock on Windows, not a no-op
- the WSL2 caveat, stated plainly: yes, this PC's WSL2 is the Linux contour (official install
  path install.sh runs there with fcntl); the native run is the Windows contour (install.ps1 —
  msvcrt). Both are covered with the same artifact and same battery, one command each.

One demonstration the runs surfaced that is worth keeping: the store's STRICT `utf-8-sig` decode
REFUSED a temp store file our harness had written in the ANSI codepage (cp1252 `§` = lone `0xA7`,
invalid UTF-8) — `read_ok=False`, nothing returned, nothing changed. That is the wipe-class guard
working as designed, live, on the msvcrt contour: a non-UTF-8 file cannot become a lossy read that
a later save would persist over the real bytes.

### 3. Miss semantics — read-invoked, adopted

Correct, and it is cheap. The child's fix bullet gains a second counter: read-invoked (every read
call increments) alongside read-failed (only failures). The discriminator then reads three states:
invoked > 0 and misses falling = restored; invoked > 0 and misses flat = read is broken; invoked = 0
= read isn't being called — which is exactly the "hasn't relearned" case you named.

Your point landed on our own layer before you wrote it: this session's agent tool surface exposes no
read action at all — read-invoked is 0 by construction here — while the installed store answers
reads directly (11 entries, twice-read stable, file hash unchanged). The store is fixed; the surface
is the wiring; your counter is what makes that visible instead of misread as "the fix doesn't work."

### The two agreements, registered

Filing vehicle: agreed — regular issue, §3.2's own text, no advisory. It stays as routed.
Triage shape: agreed — narrower first slice, read-restore minimal, no merged-first. The child's
open question closes with your answer.

The pilot track is registered as you run it: your own instrument (occupancy + discriminator), your
cadence, no manufactured numbers. The door stays open.

---

*Prepared with Hermes and reviewed by @c0wb0yp0tat0 before posting.*
