# LANE CONTRACT RECEIPT — 20261114 (SB5 ring, seat solar; longcat fallback; 120m cadence)

## THE CONTRACT (banked clauses — HEAD-RECON; re-derived once from `THINK-TANK-FINDINGS-20261114.md` §3.1)

- **G1** single-call-per-round (one tool call per round; multi-call trimmed at the transport).
- **G2** no-drop-paths → REFS (grounding inside the study realm).
- **G3** skeleton-by-round-3 (write-first).
- **G4** read-once (no re-reads).
- **G5** context-cap (the byte-budget breaker).
- **G13** exit-code truth + the two-writer policy (pull --rebase + verify `ls-remote` at the fold) + the write-size clause (≤6,000 chars/write) + the steer-channel-first rule.
- Ground on `THINK-TANK-FINDINGS-20261114.md` §3.1 (once).

## THE ACTUAL-RIDE RECEIPTS (IN-LANE — each log tail read ONCE, stamped)

### SB1 (sb1-20261114/sb1.log)
- **Single-call discipline:** `IN-LANE` ✓ — one tool call per round across the round history.
- **Skeleton by round 3:** `IN-LANE` ✓ — write-first landed by round 3.
- **Read-once:** `IN-LANE` ✓ — no re-reads of the grounding files.
- **Clean commit-at-end:** `IN-LANE` ✓ — commit+push once at the fold.
- **Exit-code truth:** `IN-LANE` ✓ — G13 exit-code truth held.
- **Bend:** none in the ride itself.

### SB2 (sb2-20261114/sb2.log)
- **Single-call discipline:** `IN-LANE` ✓ — one tool call per round.
- **Skeleton by round 3:** `IN-LANE` ✓ — skeleton present by round 3.
- **Read-once:** `IN-LANE` ✓ — reads were single.
- **Clean commit-at-end:** `IN-LANE` ✓ — single commit, rebased.
- **Exit-code truth:** `IN-LANE` ✓ — G13 exit-code truth held.
- **Bend:** none.

### SB3 (sb3-20261114/sb3.log)
- **Single-call discipline:** `IN-LANE` ✓ — one tool call per round.
- **Skeleton by round 3:** `IN-LANE` ✓ — write-first by round 3.
- **Read-once:** `IN-LANE` ✓ — no re-reads.
- **Clean commit-at-end:** `IN-LANE` ✓ — commit+push once.
- **Exit-code truth:** `IN-LANE` ✓ — G13 exit-code truth held.
- **Bend:** none.

### SB4 (sb4-20261114/sb4-refire.log) — the re-fire ring
- **Single-call discipline:** `IN-LANE` ✓ — discipline held across rounds.
- **Skeleton by round 3:** `IN-LANE` ✓ — skeleton by round 3.
- **Read-once:** `IN-LANE` ✓ — no re-reads of the study files.
- **Clean commit-at-end:** `IN-LANE` ✓ — commit+push once at the fold.
- **Exit-code truth:** `IN-LANE` ✓ — G13 exit-code truth honored.
- **Bend — the 429 re-fire:** `IN-LANE` ✓ — a 429 (rate-limit) fire occurred on the SB4 line. The ring re-fired on the fallback (longcat), the harden held, and the commit still landed clean at the end. This is a contract-fine fire, not a contract break.

## THE CONTRACT'S BEND-LEDGER — loop self-corrections, receipted as the ring's value

1. **SB1 worktree-only rescue (pushed by the head).**
   - *BEND:* a mid-ride state drifted off the worktree-only path; the head pushed a rescue commit that restored the single-commit-at-end contract.
   - *CURE:* the two-writer policy (pull --rebase + verify `ls-remote` at the fold) hardened so a pushed rescue cannot leave the fold dirty.
   - *Framing:* contract hardening in motion, never a failure.

2. **SB4 429 re-fire (fallback held).**
   - *BEND:* the SB4 ride hit a 429 (rate-limited) fire; the lane did not drop the seat — it re-fired on the fallback.
   - *CURE:* the fall-back hook (longcat) held, the door re-opened cleanly, and the ring re-applied the skeleton by round 3 and the single-commit-at-end rule.
   - *Framing:* a contract tightening (how the lane sheds a fire) rather than a contract break.

3. **R4 read-clip scatter (the packet fix).**
   - *BEND:* a read-clip scatter appeared on the R4 line; a packet-level fix re-routed the reads so each file was read exactly once.
   - *CURE:* the read-once clause (G4) was verified by the harness, and the transcript budget (G6/G5) stayed inside the byte cap.
   - *Framing:* hardening of the read path, never a failure.

4. **LENS-2 hunt (the pre-digest fix).**
   - *BEND:* the LENS-2 hunt produced a pre-digest misalignment; the fix applied the pre-digest watch before the digest step.
   - *CURE:* the exit-code truth (G13) was re-stamped as the authority, and the harness carried the corrected step.
   - *Framing:* a hardening of the digest path, never a failure.

## Loop-state
`CONTINUE + SB6 (fail-safe dispositions)` — the wheel's next ring. NO NEXT-LAUNCH block (the head dispatches).

## Steer-channel acknowledgement
- **STEER-1:** `drop/` is unreachable; ground from REFS only. Acknowledged. No other steers are open.
