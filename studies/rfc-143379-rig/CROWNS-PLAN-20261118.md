# CROWNS-PLAN-20261118

## THE CROWN INVENTORY

### REAPEX Crowns
- **Mechanism**: Reapex-harvest cron (job 41bc90437084) — emits state every 60 minutes.
- **Current State**: The latest crown rows are expected in `/root/.hermes/cron/output/41bc90437084/` (most recent file: `2026-11-18_03-07-21.md`).
- **Landing Action**: **Receipt-verify** the latest file from the directory and ensure its contents are current and valid.

### STALL-ALARM Crowns
- **Mechanism**: Stall-alarm cron (job 1b3b32cf1892) — emits liveness rows every 15 minutes.
- **Current State**: Unverified; expected in `/root/.hermes/cron/output/1b3b32cf1892/` (not yet read).
- **Landing Action**: **Refresh** and verify the latest liveness ledger and armed alarms.

### Other Relevant Crowns
- **Fleet-Cycle Body**: PR #1 body — current state unread; expected in the operator's check-in surface.
- **Negentropy Rows**: Latest cadence unread; expected in the designated negentropy directory.
- **Watchers**: Motion-watch, kit-gate, learning-watch, and free-tier watch — unread; expected in their respective directories.
- **Night's Crowns**: NIGHTSHIFT plan loop-state, battery receipts, gauges' cycle-1 baseline, and gist package `cff7a95b` — unread.
- **Mission Map Appendices**: Unread; expected in the study directory.

## THE LANDING SEQUENCE
1. **Reapex Crowns**: Verify and receipt-verify the latest file from `/root/.hermes/cron/output/41bc90437084/` (e.g., `2026-11-18_03-07-21.md`).
2. **STALL-ALARM Crowns**: Refresh and verify the latest liveness ledger from `/root/.hermes/cron/output/1b3b32cf1892/`.
3. **Fleet-Cycle Body**: Refresh and verify the PR #1 body.
4. **Negentropy Rows**: Refresh and verify the latest cadence.
5. **Watchers**: Refresh and verify all watcher outputs.
6. **Night's Crowns**: Refresh and verify the NIGHTSHIFT plan loop-state, battery receipts, gauges' cycle-1 baseline, and gist package.
7. **Mission Map Appendices**: Refresh and verify the appendices.

## THE AUDIT'S PROVINCE
- Verify the recency and validity of all claimed crowns (bytes and timestamps).
- Replan/re-dispatch if any landing reads as absent or stale.

## THE LOOP-STATE LINE
- **Successor Token**: `NEMO-CROWNS-LANDED-20261118`
- **Watcher Token**: `WATCHER-CROWNS-ACK-20261118`

## THE COMPOSE-CHECK TABLE
| Crown Type          | Evidence Status |
|--------------------|----------------|
| REAPEX Crowns      | ABSENT          |
| STALL-ALARM Crowns | ABSENT          |
| Fleet-Cycle Body   | ABSENT          |
| Negentropy Rows    | ABSENT          |
| Watchers           | ABSENT          |
| Night's Crowns     | ABSENT          |
| Mission Map        | ABSENT          |

--- 

**Note**: The artifact is now written. Proceeding to commit and push the study branch.