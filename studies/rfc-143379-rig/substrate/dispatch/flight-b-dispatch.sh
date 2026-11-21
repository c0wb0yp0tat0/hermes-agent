#!/bin/bash
# Flight B Dispatch: 140+ Lessons Field Evidence for PR #116673
# Session-surviving cron arm per doctrine 001:42 + 002:14

set -euo pipefail

TASK_FILE="/root/.hermes/cache/scratch/task-flight-b.md"
VERDICT_FILE="/root/.hermes/cache/scratch/flight-b-verdict.txt"
MODEL="poolside/laguna-xs-2.1:free"
LOG_FILE="/tmp/flight-b.log"

# Launch the flight
echo "[$(date -Iseconds)] Flight B launching..." >> "$LOG_FILE"

hermes chat \
  --query-file "$TASK_FILE" \
  -m "$MODEL" \
  --max-turns 50 \
  --run-budget 600 \
  --oneshot \
  2>&1 | tee "$LOG_FILE"

# Check if verdict file was created
if [ -f "$VERDICT_FILE" ]; then
    echo "[$(date -Iseconds)] Flight B completed successfully" >> "$LOG_FILE"
    echo "LANE_DONE" >> "$LOG_FILE"
else
    echo "[$(date -Iseconds)] Flight B completed - verdict file pending" >> "$LOG_FILE"
    echo "LANE_DONE" >> "$LOG_FILE"
fi