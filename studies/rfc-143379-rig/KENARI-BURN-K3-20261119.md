# KENARI-BURN-K3 — pre-reset utilization ride

scribe-cell: rig-kenari-burn-k3
artifact: KENARI-BURN-K3-20261119

## THE PULSE
Round-0 call (blocked): `date -u +%H:%M:%SZ; uptime; ps aux | grep -c '[c]opycat-harness'`
Lane policy: terminal is git-only for lanes, so the process-count/load/timestamp could not be captured by this lane. No numbers fabricated.
Measured proxy signal: write-window OPEN, read-gate ENGAGED (system-reported) => active burn in progress.

- copycat-harness count: not captured (terminal git-only)
- load: not captured (terminal git-only)
- timestamp: not captured (terminal git-only)

## THE VERDICT
fleet burning (as measured by open write-window + engaged read-gate; ps/uptime blocked by lane policy).

## COMPOSE-CHECK (five marks)
- think-tank spine: ABSENT
- LP envelope: ABSENT
- record-first: FIRED
- name-and-refuse: ABSENT
- two-way door: FIRED