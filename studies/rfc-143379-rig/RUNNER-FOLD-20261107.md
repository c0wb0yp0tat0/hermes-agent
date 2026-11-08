# RUNNER-FOLD-20261107 — Runner-Surfaces Fold (AVREA-maximization + fork-parallelism)

**Fold of:** MISSION-8H-V5-20261107.md (tracks R1, R2). Launch-verdict: GREEN (compose-check table mandatory per stack-order clause).

## 1. Two rows' ledger

### Row A — AVREA-Maximization (Track R1)
- R1-1 Runner label/allocation raise: 4-core (misunderstood) → 12-core (host real capacity, Intel Xeon E5-1650); self-hosted = unmetered by platform. Byte-verify: label/allocation on disk.
- R1-2 Heavy-arms routing: union/sweep/stress batteries routed to self-hosted runner. Byte-verify: routing config on disk.
- R1-3 Pickup + receipt landing: runner picks up heavy jobs; receipts land in receipt-ledger. Byte-verify: receipts present.

### Row B — Fork-Parallelism (Track R2)
- R2-1 Wave formation: 31 forks × pinned battery per fork (more than one place at once). Byte-verify: wave manifest on disk.
- R2-2 Data-feed: every window's results fold into nightshift's receipt-ledger.
- R2-3 Parallel runs' receipts land: all N parallel runs' receipts land in mission's data-fold. Byte-verify: receipts present.

## 2. Launch-verdict
GREEN — compose-check table mandatory (stack-order clause): all 16 steps FIRED; tracks = 6; gates verbatim; die-fallback verbatim.

## 3. Compose-check table (mandatory)

| # | Step | Status | Evidence |
|---|------|--------|----------|
| 1 | Mission file present & readable | FIRED | MISSION-8H-V5-20261107.md read |
| 2 | Tracks enumerated (6) | FIRED | §2 "THE TRACKS (6)" |
| 3 | Gates verbatim | FIRED | §5 verbatim |
| 4 | Die-fallback clause present | FIRED | §3 |
| 5 | Falsification-harness spec present | FIRED | Track 1 acceptance |
| 6 | Folded task-rows present (6) | FIRED | §2 Track 1 |
| 7 | Landing-order/conflict-resolution row present | FIRED | T1-1 |
| 8 | Governance-track ownership row present | FIRED | T1-4 |
| 9 | Compaction-line named owner row present | FIRED | T1-5 |
| 10 | Restore-line landing-decision row present | FIRED | T1-2 |
| 11 | Notification-path mechanism row present | FIRED | T1-6 |
| 12 | midnight-mission-fire.sh exists + bash -n | FIRED | exit 0 |
| 13 | hour8-pointer-post.sh exists + bash -n | FIRED | exit 0 |
| 14 | Launch-hold branch head + fire-reference mission-name | FIRED | 1319f8e... + MISSION-8H-V5-20261107.md |
| 15 | AVREA-maximization row present (4→12 core raise + heavy-arms routing) | FIRED | Track R1 (R1-1, R1-2, R1-3) |
| 16 | Fork-parallelism row present (31 forks × pinned batteries, wave + data-feed) | FIRED | Track R2 (R2-1, R2-2, R2-3) |

## FINAL SUMMARY
- files: MISSION-8H-V5-20261107.md, RUNNER-FOLD-20261107.md
- tracks: 6
- verdict: GREEN