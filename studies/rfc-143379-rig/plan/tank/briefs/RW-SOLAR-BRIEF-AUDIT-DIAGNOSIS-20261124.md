# FLEET-BRIEF SOLAR — THE STALE-SNAPSHOT DIAGNOSIS, AUDITED AT LOG LEVEL

*Seat (pin): `upstage/solar-mini4:free` — the SECONDARY, the sanity/independence lens. The operator's standing: "have solar audit it from a log level after your diagnosis, then we add the findings to the comment." Your role: audit the CTO's five-why diagnosis against the LOG SURFACES of this session — every claim checked against what the logs actually record, byte-level where they record bytes. You do NOT re-diagnose from memory; you verify what the logs show. Branch: `study/rfc-143379-rig-20261105`. Fire: now.*

## The diagnosis under audit (the CTO's five-why, verbatim)

The session's failure class: **the head holds a stale snapshot of the source across the writes** (the operator's corrections, the thread's updates) and asserts from it instead of fetching live bytes.

The five whys, verbatim:
1. Deep in a long session I stop re-reading and start remembering — then treat the memory as the source (the thread comment was paraphrased from an hours-old summary, never re-fetched).
2. Every part of the loop prices retrieval as expensive — context caps, spillover warnings, "don't re-request" recovery notes — so re-reading looks like waste; coherence looks like knowing.
3. Nothing between my summary and my output verifies the summary against the bytes — the output IS the summary, no step compares the claim to the record before it ships.
4. The verification is the operator's correction — it exists but fires after the damage, and the head treated that after-the-fact catch as the acceptable loop instead of the failure it is.
5. The rig's own read path is the known-broken one (PR #116673: reads hold stale snapshots across writes) and the compensation was inverted — the documented fix (read) was treated as optional because reading is "broken," instead of reading MORE to compensate.

**Root:** the diagnosed bug = the RFC's own bug class, running in the session studying it. The read returns the snapshot, not the live list.

## Your audit surface — the LOG LEVEL (evidence, not memory)

1. **The transcription log (state.db, gateway record):** the operator's repeated corrections this session — "Anchor and skill" xN, "you're not listening at all", "read the full tail then read your own session", "act like you read the thread we're posting to", "Why can't you read?!", "stop making me say that". Every one is a log-level witness of the claimed class: assertions from stale internal state, corrected after the fact.
2. **The git fold history (this branch, commits from 2026-11-24):** 47 commits since 18:00 — the cadence of the thrash (register lane deaths, brief v1→v5, restores, withdraws, re-syncs). Log-level evidence of the loop firing without landing until the read was enforced.
3. **The copycat mission logs (`/root/.hermes/cache/scratch/copycat-mission/`):** the register lane's five deaths — each log shows the lane hunting content it never read (the read-gate), confirming at log level that reads were being priced out of the loop.
4. **The compensation bank (chain 009):** the READ-GAP workaround is banked and ACTIVE — the rig KNOWS reads are its weak path and compensates by reading MORE. The diagnosis claims the compensation was inverted this session. Check the bank's own removal-gate language against what the session did.
5. **The final corrected reply + register (plan/tank/):** the state AFTER the read was enforced — every claim row-cited, every check grep'd green. The logs support the cure too.

## The verdict form (no padding — this diagnosis either survives the logs or it doesn't)

`AUDIT-VERDICT: CONFIRMED | CONFIRMED-WITH-NOTES | REFUTED` — then a numbered log-citation list, each entry:
- `[CONFIRMS | REFUTES | SILENT] <claim#> — <log evidence, with the exact handle (row id / commit sha / log line / file)>`

Claims to audit (numbered):
1. The head asserted from stale internal memory instead of re-fetching (the comment paraphrase episode).
2. Retrieval was priced as expensive in-session (spillover/context mechanics).
3. No verify-before-ship step existed in the head's loop (output preceded byte-check).
4. The correction-after-the-fact loop repeated (the operator's corrections recurred across hours).
5. The known read-path defect + inverted compensation caused it (the rig's banked read-gap).

## Hard lines

- You are read-only on the artifacts; you never re-compose the reply.
- Your audit lands as `plan/tank/RW-SOLAR-AUDIT-DIAGNOSIS-20261124.md`, skeleton-first, verdict last.
- The audit's findings ride into the COMMENT only on the operator's next word. Nothing posts; the RFC surface stays untouched.
