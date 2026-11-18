# NEMO-AUTOTHROW-PLAN-20261118 — the pre-throw anchor: recon receipts, design, and the sandbox boundary

Status: PLAN (head-side, after five Nemo plan-stage ghost-receipts closed the recon's lane route). Ships as documentation of the option; the successor implements only on the operator's word. THE TWO-WAY-DOOR FRAME binds: flag + off value + rollback named below.

## THE VERDICT
Feasible cleanly — no gateway refactor required. The runtime already exposes a reset hook surface; the anchor banks at the existing reset boundary.

## The hook candidates (receipted from the runtime's own code this session)
1. `gateway/run_shutdown_session_end.py` — the plugin `on_session_reset` hook (`invoke_hook("on_session_reset", **kwargs)`), invoked off-loop under the profile owning the session key. The pre-throw bank lands HERE: the hook fires before the reset commits, bounded and non-raising (the file's own pattern: failures are logged, never raised).
2. `gateway/run_turn.py` — `_reset_notice_session_info` (the auto-reset notice path, resolved inside the profile) — the notice point where "the user is being thrown" is already detected; the bank can ride the same detection.
3. `gateway/session_lifecycle.py` — `_route_reset_reason` (the reset-reason routing: which reset reason → which path) — the classifier that distinguishes auto-throw from manual lever.

## The design (the pre-throw anchor, 8 lines)
1. A hook on the `on_session_reset` boundary (candidate 1) runs a bounded bank-before-lever: write the fresh `NNN-handoff-<date>` deck (the 013/014 pattern: live state, in-flight lanes, queued steps, steers) into the profile's chain dir + the study repo, byte-verified.
2. The bank is append-only: it writes a NEW deck, never touches an existing one; a deck already written in the same hour is skipped (no double-bank).
3. The bank is non-raising: any failure logs `[anchor] bank FAILED: ...` and proceeds — a missed bank is NAMED, never silent (and the post-side cold-start path remains the fallback).
4. FLAG: `auxiliary.pre_throw_anchor.enabled` (bool, default false — off until switched on). OFF VALUE: `false`. ROLLBACK: `hermes config set auxiliary.pre_throw_anchor.enabled false` (or delete the key) — restores the exact prior behavior.
5. The deck's content contract: the same fields as 014-handoff-20261118 (live machinery, queued steps, steers, gates, standing items), generated from the runtime's own state (sessions table, in-flight lane pids, the branch head) — mechanical, not narrated.
6. Sandbox-first: the hook + the deck generator are tested in the sandbox/idealized world (the doc-chain store's test harness) before the flag is ever set true on a live profile. The successor's gate: sandbox test green, THEN the operator's word, THEN live on.

## The patch spec (for the successor)
- New module `gateway/pre_throw_anchor.py`: the deck generator (state probe → deck write → byte-verify → log), called from `run_shutdown_session_end.py`'s reset path behind the flag.
- Tests: the deck generator unit tests (state probe fixtures, double-bank skip, failure logging) + one e2e: a session reset with the flag true writes a deck whose pointer line resolves.
- The toggle pair (the OTHER lever, documented-only): `auxiliary.background_review.enabled` — verified present in the runtime's doctor checks and metrics origin tags (receipted from the build's tests); NO change to it, sandbox-only curiosity, per the operator's gate.

## The risks (each with its counter)
- Missed bank (the throw beats the write) → the post-side cold-start fallback + the named `[anchor] bank FAILED` log; the deck generator runs in microseconds, bounded.
- Double bank (two resets, one hour) → the same-hour skip rule.
- Hook race (a reset during a compression event) → the hook is off-loop and non-raising, both paths independent.
- Flag-off drift (the flag never turns on anywhere) → default false is the SAFE default; the option exists, the obligation doesn't.

## THE LOOP-STATE LINE
`AUTOTHROW-PLAN-ON-SHELF - successor implements in the fork behind the flag, sandbox-tests, and applies live ONLY on the operator's word; the background-review lever stays documented-only; the gist chain runs ungated.`
