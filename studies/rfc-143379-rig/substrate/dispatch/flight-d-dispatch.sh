#!/bin/bash
# Flight D: SCADA/PLC Abstraction Dispatch
# Session-surviving arm for anchored free lane

BRIEF="/root/.hermes/cache/scratch/flight-d-scada-brief.md"
MODEL="poolside/laguna-xs-2.1:free"
LOG="/tmp/flight-d-output.txt"

# Launch the flight
hermes chat --query-file "$BRIEF" -m $MODEL --oneshot --max-turns 50 > "$LOG" 2>&1

# Exit code
echo "LANE_DONE"
exit 0
