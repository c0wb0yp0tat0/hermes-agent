#!/usr/bin/env bash
# NEGENTROPY-SWEEP-ARM — the recurring sweep's cron arm (the super-regular cadence)
# The no_agent cron launches the harness lane and exits; the lane's landing rows at the head's cadence.
set -uo pipefail
TS=$(date -u +%Y%m%d-%H%M)
SEAT="${NEGENTROPY_SEAT:-meituan/longcat-2.5:free}"  # roster-registered 2026-11-19: solar 403-walled at dispatch probe; longcat live
BRIEF="/root/.hermes/cache/scratch/pr1-rotation/briefs/negentropy-sweep-recurring-brief.md"
ART="/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEGENTROPY-SWEEP-${TS}.md"
LOG="/root/.hermes/cache/scratch/copycat-mission/negentropy-sweep-${TS}-run.log"
# The seat probe (the reply-text contract) — a dead seat = NO arm (the fair-share rest rule's enforcement at the source)
PROBE=$(timeout 60 hermes chat -q "Reply with exactly: OK" -m "$SEAT" 2>&1)
if ! echo "$PROBE" | grep -qE '^\s*OK\s*$'; then
  echo "NEGENTROPY-SWEEP SKIPPED: the alpha's seat did not answer (the fair-share rest rule) — the next fire re-checks."
  exit 0
fi
TEMPLATE="/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEGENTROPY-SWEEP-RECURRING-brief.md"
if [ ! -s "$BRIEF" ] && [ -s "$TEMPLATE" ]; then
  mkdir -p "$(dirname "$BRIEF")"
  cp "$TEMPLATE" "$BRIEF"
  echo "NEGENTROPY-SWEEP SELF-HEALED: brief restored from the repo template (head 2026-11-19); the lane rides the template's reconstruction receipt"
fi
[ -s "$BRIEF" ] || { echo "NEGENTROPY-SWEEP FAILED: the brief absent at $BRIEF (the silent-skip class — a missing brief must be a visible failure, never a healthy skip)"; exit 1; }
[ -e "$ART" ] && { echo "NEGENTROPY-SWEEP SKIPPED: the artifact already exists (a duplicate fire)"; exit 0; }
mkdir -p "$(dirname "$LOG")"  # THE LOGDIR-MISS FIX (2026-11-14): the nohup redirect died silently when the logdir never existed — the arm creates its own
nohup python3 /root/scripts/copycat-harness.py --model "$SEAT" --brief "$BRIEF" --artifact "$ART" --rounds 40 --logfile "$LOG" >/dev/null 2>&1 &
echo "NEGENTROPY-SWEEP ARMED: pid=$! ts=$TS (the lane's landing rows at the head's cadence)"
