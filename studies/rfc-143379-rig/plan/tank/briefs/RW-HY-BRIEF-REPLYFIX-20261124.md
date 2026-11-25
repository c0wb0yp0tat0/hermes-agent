# FLEET-BRIEF HY — THE THREAD-COMPLETE REPLY FIX (the four named classes)

*Seat (pin): `tencent/hy4-flash:free` — THE COMPOSER. The CTO's end-to-end read of RFC #143379 (all 50 comments) found four named classes the current max-value reply fails. The operator's standing (2026-11-24): "have hy and beam with think tank fix this." DARKHORSE IS DELETED (the operator's word — redownload later): NO darkhorse session content, NO floor's-record beat, NO telemetry rows, NO transcript references in the reply. Branch: `study/rfc-143379-rig-20261105`. Fire: now.*

## The mission

Compose the REVISED max-value reply to @kvnloo on RFC #143379 — the thread-complete form that closes all four classes. The artifact: `plan/tank/RW-FULL-REPLY-REVISED-20261124.md`. Every number above a row citation must resolve in the thread; cite rows as `(row NNNNNNNNNN)`.

## The thread's live state (the load-bearing rows, verbatim facts)

The exchange to answer is rows 7143199711 (kvnloo's stall-on-read arm) + 7147011435 (our "within the hour" promise). The obligation set from the thread:

1. **The stall-on-read arm** (kvnloo, row 7143199711): the test `test_doc_reader_and_writer_keep_latest_live_state`, `tests/tools/test_memory_chain_docs.py#L198-L244`, at `a9c65dc4`. The four steps: seed `initial`; reader calls `store.read("doc:…")`, takes disk snapshot, blocks on `Event` before returning; writer commits `store.add("doc:…", "latest")`; release reader, assert read returned `["initial"]` while live list and tool-level `read` both say `["initial", "latest"]`. His fresh run 11-24, 10× per variant at both `a9c65dc4` and `60a2e156`: green, green, green, **red** only on no-lock+cache-write (0/10, `['initial'] == ['initial', 'latest']`). He asked directly: does that match the arm we'd pre-register, or would we pause the reader elsewhere (e.g. inside the writer's commit)?
   - OUR ANSWER (already drafted, keep): we register the pause at snapshot-then-block, not inside the writer's commit; the race lives at that boundary; pausing inside the commit tests the commit's own atomic write, a separate hazard. Offer the second arm if he wants it.

2. **The row misattribution (class 1 — MUST FIX):** the draft's "record, straight" beat cites `(row 7140129275)` as "our confirm-run reply." WRONG. 7140129275 is KV NLOO's confirm run. OUR reply that logged the byte-count and control-refusal divergences is **7141681989** (posted 2026-11-24 19:09Z). Correct the citation.

3. **The open threads (class 2 — MUST ADD):** the reply must carry, on the record:
   - The /pin acceptance: kvnloo agreed to all three framings (control surface over the method, second witness the summary does not author, cap as refusal boundary never eviction) at row 7122500729; the fourth acceptance row (the contradiction flag, pin vs summary, check runs on pins never a vote) accepted at 7122688366; the acceptance rows C1–C4 pre-registered at 7135900146 (C1: 100% survival 4 compactions verbatim, RED on MAIN/GREEN on branch, removal control RED; C2: stated cap, plain refusal, no eviction; C3: no second store, one entry in decision ledger #113309, byte-compared to its own schema; C4: the contradiction-flagged row, accepted as written).
   - The #113309 rebase: kvnloo rebases it as-is on a branch first, KoNit-K's commits and authorship kept, /pin stacked as a separate commit (row 7122500729). Our reply confirms the ledgers move with his rebase and /pin rides atop it as its own commit.
   - The redaction pass: a general pass built for reuse, scope = compaction events + session-arc headers only, stripping rules as the test corpus; the curve paper sits on top as secondary (rows 7122500729, 7122688366).
   - The salvage read: the scheduled-wake question — ours to answer, the read of the branch reported beside the question (row 7122051629). The wake read PARTIAL at `8ba4b344766e50c2e3eeaba84f4349276a1be021` (row 7135900146): scheduled wake reads state.db/state.py, writes its own session rows, hits zero on every memory-store anchor; the memory-store write path untouched.
   - The sibling seam (async-delegation completion picked as "User asked"): held until our local row lands; the phrase drops if no local row (row 7122051629).
   - The second-pair-of-eyes questions (kvnloo row 7087999804): #137650 salvage on MAIN and #116788 unattended add — our side's stance belongs on the record if we hold one; if not, name the follow-up.

4. **The hold-back class (class 3 — MUST CLOSE):** the pre-registration (row 7135900146) withheld ONE class by clause — signature deliberately not written where a runner can read it. kvnloo's confirm (7140129275) did not report tripping it. The reply must state the hold-back's status plainly: held, not tripped by his confirm; it stays withheld until the conditions its clause names are met. Name the class's name only as "the hold-back class," never its content.

5. **The star (class 4 — REMOVED BY OPERATOR):** DARKHORSE IS DELETED (the operator, 2026-11-24: "Then delete darkhorse for now... We will redownload later"). The "floor's own record" beat, the channel/seat paragraphs' darkhorse-dependent claims, the telemetry rows, the transcript references — ALL GONE from the reply. The channel finding (0/40 → 26/40 → 31/40 → 29/40, ~70%) and the battery INCONCLUSIVE verdict may stay ONLY as the substrate-thread finding already posted at row 7141681989 — they belong to the study's substrate thread, not the reply's core; if they appear, they appear as one modest beat crediting the same-week finding, never as the reply's center. The "twenty minutes to listen" finding (the operator's add) STAYS: "A finding from the same night, no blame. It took twenty minutes for the fresh session that inherited this reply to listen enough to properly skill — to read the standing instructions back, verbatim, rather than work from commentary about them. Same root as the stall above: the read holding a stale view while the writes land. The fix was cheap and it is on the record: the original ask is the anchor." Keep it near the close, no em-dash doubling.

## The register (the pair's formatting law)

- One em-dash per sentence, never two; lines with two em-dashes are violations.
- `@kvnloo` unbackticked; footers exact: "*Prepared with Hermes and reviewed by c0wb0yp0tat0 before posting.*"
- No staging metadata, no "PREVIEW", no rig-internal headers in body text.
- Row citations as `(row NNNNNNNNNN)` inline; numbers byte-true to the rows above.
- The tone: flat neutral with warmth, receipts not adjectives, the answer is a decision not a shrug.

## Check before you finish

- [ ] All four classes closed: row 7141681989 corrected, /pin set + redaction + salvage + sibling seam on the record, hold-back status named, no darkhorse anywhere.
- [ ] The stall-arm answer present: snapshot-then-block, not inside the commit; second arm offered if he wants one.
- [ ] Register sweep: one em-dash per sentence, @kvnloo unbackticked, footer exact, zero darkhorse strings (`darkhorse`, `floor's own record`, `telemetry rows`, `Sword`, `Song`).
- [ ] The reply is thread-complete: anyone reading it alone sees the whole obligation set answered.

The gist sync rides the fold; the public post waits the operator's word. Fire: now.
