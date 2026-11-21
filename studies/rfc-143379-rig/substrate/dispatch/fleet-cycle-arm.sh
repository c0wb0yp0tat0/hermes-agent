#!/usr/bin/env bash
# FLEET-CYCLE-ARM — the PR #1 body-update arm (the ≥2x-per-shift cadence)
# The no_agent cron launches the harness lane and exits; the lane composes + PATCHes the body + archives + verifies.
set -uo pipefail
TS=$(date -u +%H%M)
SEAT="stealth/crouton-alpha"
BRIEF="/root/.hermes/cache/scratch/pr1-rotation/briefs/fleet-cycle-body-brief.md"
ART="/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/FLEET-CYCLE-BODY-20261107-${TS}.md"
LOG="/root/.hermes/cache/scratch/copycat-mission/fleet-cycle-body-${TS}-run.log"
PROBE=$(timeout 60 hermes chat -q "Reply with exactly: OK" -m "$SEAT" 2>&1)
if ! echo "$PROBE" | grep -qE '^\s*OK\s*$'; then
  echo "FLEET-CYCLE SKIPPED: the alpha's seat did not answer (the fair-share rest rule) — the next fire re-checks."
  exit 0
fi
[ -s "$BRIEF" ] || { echo "FLEET-CYCLE SKIPPED: the brief absent"; exit 0; }
[ -e "$ART" ] && { echo "FLEET-CYCLE SKIPPED: the archive already exists (a duplicate fire)"; exit 0; }
nohup python3 /root/scripts/copycat-harness.py --model "$SEAT" --brief "$BRIEF" --artifact "$ART" --rounds 40 --logfile "$LOG" >/dev/null 2>&1 &
echo "FLEET-CYCLE ARMED: pid=$! ts=$TS (the body's update + the archive land on the lane's completion)"
