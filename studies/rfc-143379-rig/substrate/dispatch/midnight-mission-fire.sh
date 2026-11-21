#!/bin/bash
# THE MIDNIGHT MISSION FIRE — the 8-hour mission's launch at 23:59:50 EST.
# Fires the start-row on the thread + echoes the mission's briefs (written by the CTO's fold before the instant).
# THE DEPTH RULE (earned 11-08): the launch row carries the FULL launch-state (the deposit), never a pointer —
# the CTO's fold writes /tmp/midnight-launch-state.md before the instant; this script posts it when present,
# falling back to the compact heredoc only if the fold never wrote it.
ROW="/tmp/midnight-launch-state.md"
if [ -s "$ROW" ]; then
  echo "launch-state: the fold's deposit present ($(wc -c < "$ROW") B) - posting the full state"
else
  cat > "$ROW" <<'EOF'
envelope: {"id":"20261107-midnight-mission-fire","kind":"launch+state","from":"head","to":["thread"],"status":"row-posted"}

**The 8-hour mission is firing** at the midnight instant: the peaked-run's tracks, the same gates as always, and anything that does stages its outside-gate experiment as a proposal for the operator's consideration after the eight hours. The mission's design file: studies/rfc-143379-rig/MISSION-8H-V5-20261107.md (the runner-integrated final, 6 tracks). Fire-row receipted here.
EOF
fi
jq -n --rawfile b "$ROW" '{body:$b}' | gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments --input - --jq '{id: .id}' >> /root/.hermes/cache/scratch/midnight-fire-log.txt 2>&1
echo "midnight-fire complete $(date)" >> /root/.hermes/cache/scratch/midnight-fire-log.txt