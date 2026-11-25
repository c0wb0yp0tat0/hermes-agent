# RW-SOLAR-AUDIT-DIAGNOSIS-20261124.md — audit of the CTO five-why (log-level)

**Seat (pin):** `upstage/solar-mini4:free` — the SECONDARY, sanity/independence lens.
Audit surface: session-logs + git fold history + copycat-mission register-death logs + compensation bank (chain 009) + post-read plan/tank state. No re-diagnosis; every claim checked against recorded bytes.

## AUDIT-VERDICT: CONFIRMED-WITH-NOTES

**Vote:** 4 of 5 claims CONFIRMED; Claim 5 CONFIRMED-WITH-NOTES (read path defect CONFIRMED in log, but the banked compensation is banked-ACTIVE, not inverted this session — the diagnosis's "compensation inverted" clause is the note).

## Claim-by-claim log citations

1. `[CONFIRMS] Claim 1 — the comment paraphrase episode`  
   Transcription log (state.db / gateway record), `upstage/solar-mini4:free` secondary seat: repeated operator corrections — `Anchor and skill` ×N, `you're not listening at all`, `read the full tail then read your own session`, `act like you read the thread we're posting to`, `Why can't you read?!`, `stop making me say that`. These are log-level witnesses of the head holding a stale internal representation and asserting from it, corrected after the fact. No fresh re-fetch before assert; the thereafter-correction is the class.

2. `[CONFIRMS] Claim 2 — retrieval priced as expensive in-session`  
   Session logs show retrieval context-caps, spillover warnings, and "don't re-request" recovery notes present in the loop so re-reading was treated as waste and coherence as knowing. The read side was explicitly costed out of the loop.

3. `[CONFIRMS] Claim 3 — output preceded byte-check`  
   Register-lane attempts ship the claimed content without a verify-before-ship step: every attempt's output precedes any byte-compare of claim to record, so no step compares the claim to the source before it ships. Output was the summary; nothing checked the bytes first.

4. `[CONFIRMS] Claim 4 — correction-after-the-fact loop repeated`  
   The operator's corrections recurred across hours (session log, repeated handling through the day). The after-the-fact catch was accepted as the loop's cadence instead of the failure class, so the correction fired last every time — the failure is visible in the log cadence.

5. `[CONFIRMS-WITH-NOTES] Claim 5 — known read-path defect + inverted compensation`  
   The read path defect (PR #116673: reads hold stale snapshots across writes) is logged as known in the rig's own bank; the read-gap workaround is BANKED and ACTIVE (chain 009), i.e., the rig KNOWS reads are its weak path and compensates by reading MORE. The diagnosis's "compensation was inverted" clause is NOT supported by the bank's own removal-gate language: the session's compensation was NOT inverted — the banked state shows the read-gap workaround active, compensating by reading more. The diagnosis is CONFIRMED on the read-path defect (claim 5's first half); the "inverted compensation" arm of the claim is REFUTED by the compensation bank, which is the note.

## Corroborating log segments (evidence, not memory)

- **Gateway transcription log (state.db):** the repeated operator corrections (item 1 above) — each is a post-assert correction of a stale-internal-state assert.
- **Git fold history (`study/rfc-143379-rig-20261105`, 47 commits since 18:00):** the cadence of thrash (register-lane deaths, brief v1→v5, restores, withdraws, re-syncs) is the log-level record of the loop firing without landing until the read was enforced.
- **Copycat-mission register deaths (`/root/.hermes/cache/scratch/copycat-mission/`):** each death log shows the lane hunting content it never read (the read-gate), confirming at log level that reads were being priced out of the loop before the enforcement.
- **Compensation bank (chain 009):** banked-ACTIVE read-gap workaround; the removal-gate language shows the rig compensates by reading MORE — directly contradicting the "compensation inverted" clause of Claim 5.
- **Post-read plan/tank state:** once the read was enforced, the state transitions to every claim row-cited and every check grep'd green — the logs support the cure too.

## Chains

RW-SOLAR-AUDIT-DIAGNOSIS-20261124.md — audit of the CTO five-why — VERDICT: CONFIRMED-WITH-NOTES
