#!/usr/bin/env bash
# THE 11-07 SHIFT'S LAUNCH — fires at 23:59:50 ET (2026-11-06). One command, receipts, no re-asks.
set -uo pipefail
SEAT="reflection/beam-1.0-501b-a23b:free"
BRIEF="/root/.hermes/cache/scratch/pr1-rotation/briefs/legd-run-design-refire-20261107.md"
ART="/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/W2-ISOLATION-RUN-DESIGN-20261107.md"
LOG="/root/.hermes/cache/scratch/copycat-mission/legd-run-design-20261107-run.log"
REPO="/root/workspace/repos/hermes-agent"

echo "[LAUNCH 2026-11-06 23:59:50 ET] pre-checks:"
# 1. The brief present
[ -s "$BRIEF" ] && echo "  ok brief: $(stat -c %s "$BRIEF")B" || { echo "  FAIL brief absent"; exit 1; }
# 2. The artifact path clear
[ -e "$ART" ] && { echo "  FAIL artifact already exists"; exit 1; } || echo "  ok artifact path clear"
# 3. The seat live (the reply-text contract, never the session header)
PROBE=$(timeout 60 hermes chat -q "Reply with exactly: OK" -m "$SEAT" 2>&1)
echo "$PROBE" | grep -qE '^\s*OK\s*$' && echo "  ok seat live ($SEAT)" || { echo "  FAIL seat probe: $(echo "$PROBE" | tail -c 200)"; exit 1; }
# 4. The branch state (two-writer: remote read before the lane's flight)
REMOTE=$(git -C "$REPO" ls-remote origin refs/heads/study/rfc-143379-rig-20261105 | awk '{print $1}')
LOCAL=$(git -C "$REPO" rev-parse HEAD)
[ "$REMOTE" = "$LOCAL" ] && echo "  ok branch local==remote $LOCAL" || { echo "  NOTE branch drift local=$LOCAL remote=$REMOTE (flag, not a stop)"; }
# 5. The dispatch (the harness lane — session-surviving, the machine's own log)
echo "  dispatch: $SEAT <- $BRIEF -> $ART (40 rounds)"
nohup python3 /root/scripts/copycat-harness.py --model "$SEAT" --brief "$BRIEF" --artifact "$ART" --rounds 40 --logfile "$LOG" >/dev/null 2>&1 &
PID=$!
echo "  armed pid=$PID"
echo "$(date -u +%FT%TZ) LAUNCH-ARMED pid=$PID seat=$SEAT brief=$BRIEF art=$ART" >> /root/.hermes/cache/scratch/pr1-rotation/midnight-launch-receipt.txt
echo "[LAUNCH ARMED] pid=$PID — the RING-0 row posts on the sweep."
