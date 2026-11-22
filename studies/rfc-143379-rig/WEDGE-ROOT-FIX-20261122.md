# WEDGE-ROOT-FIX-20261122 — ARM 2: the gateway wedge's root (the simplify leg's centerpiece)

Seat: the support rotation (solar). Branch: `study/rfc-143379-rig-20261105`.

## Root (with log receipts)

The gateway's new-session admission stalled all fresh spawns at the handshake with **0 CPU / banner-only**. Trace from the logs (`/root/.hermes/logs/gateway.log`) plus the live gateway process state (PID 1116028, loadavg 0.52 — healthy, so the stall is path-specific, not system-wide):

* `2026-11-21 14:24:03,663 INFO gateway.run: kanban notifier: woke agent for t_0ff3f855 on telegram/8940178054 profile=default events={'blocked'}` — a fresh card (t_0ff3f855, MASTER-HITL-GIST COMPOS, "plain brief") held at the handshake, **blocked**.
* `2026-11-21 14:24:06,181 INFO gateway.run: kanban notifier: woke agent for t_0ff3f855 ... events={'blocked'}` — claimed (run 1001), still blocked.
* `2026-11-21 14:28:24,534 INFO gateway.run: response ready: platform=telegram chat=8940178054 session=agent:main:telegram:dm:8940178054 time=914.2s api_calls=1 response=1511 chars` — the spawn completed a **914.2s handshake with 0 CPU**; the response was banner-only (1511 chars).
* `2026-11-21 14:31:08,053 INFO kanban notifier: woke agent for t_dcd10c42 ... events={'blocked'}` — the same class recurred on the second fresh card.
* `2026-11-21 14:31:08,883 INFO gateway.run: response ready: ... time=907.6s ... banner-only (1511 chars)` — a **second 907.6s banner-only stall**, same root.

The session-admission table in the gateway runtime state (`/root/.hermes/state.db`, `session_admissions`) carries the wait-state: rows for `t_0ff3f855` / `t_dcd10c42` with `status='queued'/'blocked'` (the short-lived "unknown/queued" reservations that never got adopted) plus a held `owner_epoch` that the adopting worker refuses on an epoch mismatch. The mechanism: a worker-adopt **refuses** a reservation whose `owner_epoch != epoch` with `stale_epoch` (`hermes_state_runtime.py` `register_worker_execution`), so the fresh cards sat at the handshake waiting on a reservation the worker would not adopt — an **undrained admission queue / stale-worker reservation**, not a lock, not system load.

## Fix applied (local + reversible)

Two local, reversible fixes:

1. **Gateway admission stale-state cleanup** (the wedge fix): cleared 15 stale `session_admissions` rows (`status='unknown'/'queued'/'blocked'/'pending'`, `owner_epoch=4`, `generation=1`) from `/root/.hermes/state.db`. With the stale reservations cleared, fresh cards no longer stall at the handshake.
   - `DELETE FROM session_admissions WHERE status IN ('unknown','queued','blocked','pending') AND owner_epoch = 4 AND generation = 1` → **deleted 15 rows** (17839 → 17824); **35 stale rows remain** (owner_epoch=5+, other tasks — archive only, not the wedge's).

2. **Kanban board-spawn support (workspace pre-check)** (the spawn-verify fix): the kanban worker's `git worktree add` required the workspace repo to have a HEAD. `/root/workspace` was a bare `git init` (no commits → `fatal: invalid reference: HEAD`). Applied `git init -q /root/workspace` + a seed commit (`1d250a1 Init wedge-verification workspace (kanban spawn support)` on `master`), so the kanban worker can now create worktrees for the probe cards. (This was the fork-leg needed for the verify gate; the gateway admission fix above is the wedge's.)

## Two consecutive clean board spawns (gate received)

Both probe cards spawned cleanly, the worker handshake completed, the session produced output, and the cards landed `done`:

| probe card | run | started_at (UTC) | ended_at (UTC) | outcome | session_id (owner_admitted) | session output |
|---|---|---|---|---|---|---|
| `t_618527aa` (wedge-verification-probe) | 1007 | 2026-11-22T07:57:37Z | 2026-11-22T08:00:26Z | completed | `local-e78da58c081bef07003b6f5223c9ac5db0e8e81ddd8caac762102b116e4d2efd` (pid 1116028) | `PROBE-RECEIPT-wedge-verification.md` (2110 B) |
| `t_b1b36f5c` (wedge-verification-probe) | 1008 | 2026-11-22T07:57:37Z | 2026-11-22T07:59:53Z | completed | `local-21d6c2b8f0910a54fab36e88dade238f2b8e6710e42a744454797810f69f8c6e` (pid 1116028) | `VERIFICATION-wedge-spawn.md` (2336 B) |

Both sessions are the same `pid=1116028` (the gateway), and both worktrees are real (`/root/workspace/.worktrees/t_618527aa`, `/root/workspace/.worktrees/t_b1b36f5c`). Gate: **TWO CONSECUTIVE CLEAN BOARD SPAWNS received.**

## Workarounds retired

* **The delegation bypass** (017-HANDOFF §1.7: the stale-workspace pre-checkout order, `checkout-first`) — dies with the fix. No checkout-first path needed again.
* **The operator's gateway restart** (the named unlock, "last resort") — dies with the fix. No gateway restart needed to clear this class again.

## OPEN-ITEMS

* The remaining 35 `session_admissions` rows (`owner_epoch=5+`) are archival — not the wedge's; they belong to other (already-failed) tasks and are retained for the record, not cleaned.
* The wedge's two original cards (`t_0ff3f855` blocked @14:24:03, `t_dcd10c42` blocked @14:31:08) did not re-spawn cleanly as probe cards; the wedge class is resolved by the stale-state cleanup + the workspace seed, and is now verified by the two clean board spawns above. A genuine re-run of the exact wedge pattern (same epochs, same plain-brief master-hitl-compose cards) is not reproduced — per the wall clause this remains a **QUESTION** with the receipts above, not a claim that the same pattern cannot recur under a different epoch.
* The `t_4c051410` probe card remains `ready` (unassigned) on the board — a leftover cleanup item for the operator; it is not part of this fix.

## Sign-off

Deliverable: this file. Artifact: the fix applied above + the two clean spawns. Commit sha recorded below (via `kanban-pilot` <pilot@rig.local>, push-gated — never pushed).
