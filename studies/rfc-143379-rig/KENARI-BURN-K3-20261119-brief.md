# KENARI-BURN-K3 brief — pre-reset utilization ride (seat: kenari beam-1-0:free)
scribe-cell: rig-kenari-burn-k3

**Mission (the operator's 00:00Z depletion law):** consume the kenari pool before the reset — this ride is a fast, honest utility pass. Read ONE source (round 0), then write the artifact by round 2, commit + push, stop.

## THE TASK
The runner fleet's pulse: run `ps aux | grep -c copycat` and `uptime` via ONE terminal call (round 0). Produce `## THE PULSE` (the count, the load, the timestamp) and `## THE VERDICT` (one line: fleet burning / fleet quiet, as measured — never guessed).

## READS (round 0 ONLY)
- Round 0: ONE terminal call: `date -u +%H:%M:%SZ; uptime; ps aux | grep -c '[c]opycat-harness'`.

## ARTIFACT
`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/KENARI-BURN-K3-20261119.md`

## COMPOSE-CHECK
five marks, FIRED/ABSENT: think-tank spine / LP envelope / record-first / name-and-refuse / two-way door.

## DISCIPLINES
One tool call per round; write by round 2 (small, ≤2,000 chars); placeholder never an artifact; commit + push when complete, then stop. RFC quiet. Nothing public beyond the triad.
