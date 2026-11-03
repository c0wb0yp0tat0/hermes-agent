@kvnloo — one commit on this head, with the receipt.

**`ffb85c2c58` — the preserve→dream seam is closed.** `preserve_session` emitted items with `kind="message"`, which Light Sleep's `LOAD_BEARING_KINDS` filter silently drops — everything the SPA preserved was discarded at the seam. The items also carried no `provenance`, so all scored as "agent" and user-origin content lost the PROMOTE floor. Now each preserved message is classified into the dream cycle's kind taxonomy (falsifier / decision / steer / measured on first marker match, else receipt) and carries provenance from the role (`user` → "user").

- *Executed:* new `test_spa_integration.py` (6 seam tests wiring `preserve_session` into `DreamCycle` end-to-end) + `test_dream_cycle.py` — **15✓ / 0✗** via the canonical runner. Seam tests **RED on `e543544aca`** (2✓ / 4✗), **GREEN** with the fix.
- *In flight:* the full suite runs next locally, queued behind the write-gate branch's — tally to follow. Upstream CI is queued on the maintainer-approval gate.
- *Not run yet:* a live compressor/dream-cycle run — the SPA→compressor hookup isn't part of this PR by design, so that door belongs to the integration that wires it. Open whenever wanted.

<sub>Finding credit: kvnloo's downstream RFC-143379 study (P1, source-confirmed). Co-drafted and verified with GitHub Copilot (Kimi K3), shared work with @c0wb0yp0tat0.</sub>
