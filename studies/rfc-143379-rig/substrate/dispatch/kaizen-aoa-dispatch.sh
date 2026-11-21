#!/bin/bash
# kaizen-aoa-dispatch.sh — session-surviving one-shot dispatch arm for AoA leg
# Fired by the gateway cron daemon (NOT a leg's bg child)
# Reads NEXT-LEG-READY marker, launch-tests model, fires leg, verifies handles
# Contract per kaizen-flight-plan.md §2 + §5 (AOA co-base rotation)

set -euo pipefail

MARKER="/root/.hermes/cache/scratch/kaizen-next-leg-ready"
LOG="/root/.hermes/cache/scratch/kaizen-aoa-run.txt"

# Check for PARK
s=$(cat "$MARKER" 2>/dev/null || echo "")
if [[ "$s" == *"PARK"* ]]; then
    echo "$(date -u +%FT%TZ) PARK — no arm, no dispatch." >> "$LOG"
    exit 0
fi

# Parse from marker (format: NEXT LEG: aoa / STATUS: CONTINUE / BRIEF: path / MODEL: id / SPEC: path / ...)
BRIEF=$(grep '^BRIEF:' "$MARKER" | cut -d' ' -f2-)
MODEL=$(grep '^MODEL:' "$MARKER" | cut -d' ' -f2-)
VERDICT=$(grep '^VERDICT:' "$MARKER" | cut -d' ' -f2-)
JOB_NAME=$(grep '^CRON_NAME:' "$MARKER" | cut -d' ' -f2-)

if [[ -z "$BRIEF" ]] || [[ -z "$MODEL" ]]; then
    echo "$(date -u +%FT%TZ) ERROR: Missing BRIEF or MODEL from marker" >> "$LOG"
    exit 1
fi

# Per-job spec isolation (002:175)
SPEC_FILE="${MARKER%/*}/next-leg-spec-${JOB_NAME}.txt"
echo "$BRIEF $MODEL $VERDICT" > "$SPEC_FILE"

# Launch-test the free id — GREP the reply token, never exit code (002:158)
LAUNCH_OUTPUT=$(hermes chat -q "Reply with exactly: OK" -m "$MODEL" --oneshot --max-turns 3 2>&1) || true
if ! echo "$LAUNCH_OUTPUT" | grep -q "^OK$"; then
    echo "$(date -u +%FT%TZ) LAUNCH-FAIL $MODEL — catalog-drift class" >> "$LOG"
    # Fallback: laguna-s (rotate the other way)
    FALLBACK_MODEL="poolside/laguna-s-2.1:free"
    LAUNCH_OUTPUT=$(hermes chat -q "Reply with exactly: OK" -m "$FALLBACK_MODEL" --oneshot --max-turns 3 2>&1) || true
    if ! echo "$LAUNCH_OUTPUT" | grep -q "^OK$"; then
        echo "$(date -u +%FT%TZ) FALLBACK-FAIL — escalating to watch lane" >> "$LOG"
        exit 1
    fi
    MODEL="$FALLBACK_MODEL"
    echo "$(date -u +%FT%TZ) FALLBACK-SUCCEEDED $MODEL" >> "$LOG"
fi

# Fire with SESSION SURVIVAL (setsid detaches, 002:149)
setsid nohup hermes chat --query-file "$BRIEF" -m "$MODEL" > "$LOG" 2>&1 &
PID=$!

sleep 3
if kill -0 "$PID" 2>/dev/null && [[ -f "$BRIEF" ]]; then
    echo "$(date -u +%FT%TZ) DISPATCH-VERIFIED AOA pid=$PID model=$MODEL brief=$BRIEF verdict=$VERDICT" >> "$LOG"
    exit 0
else
    echo "$(date -u +%FT%TZ) DISPATCH-FAIL — process or brief missing" >> "$LOG"
    exit 1
fi