#!/bin/bash
# c30-dispatch.sh — explicit dispatch for C30 embedder co-design.
# FIX: watchdog-dispatch.sh's JOB_NAME resolution defaults to "watchdog" when
# the hermes cron system does not pass the job name as $1 or via
# HERMES_CRON_JOB_NAME env var. This wrapper hardcodes the spec values,
# bypassing the faulty resolution.
set -euo pipefail

SCRATCH_DIR="/root/.hermes/cache/scratch"
BRIEF="/root/.hermes/cache/scratch/c30-embedder-co-design-brief.md"
MODEL="poolside/laguna-xs-2.1:free"
LOG="/tmp/c30-embedder-co-design.txt"
FALLBACK_MODEL="poolside/laguna-s-2.1:free"

echo "=== c30-dispatch.sh: $(date -Iseconds) ===" >&2
echo "Job: c30-embedder-co-design | brief=$BRIEF model=$MODEL log=$LOG" >&2

if [ ! -f "$BRIEF" ]; then
    echo "ERROR: Brief not found: $BRIEF" >&2
    exit 1
fi

launch_leg() {
    local brief="$1"
    local model="$2"
    local log="$3"

    nohup /root/.local/bin/hermes chat --query-file "$brief" -m "$model" > "$log" 2>&1 &
    local pid=$!
    echo "DISPATCHED pid=$pid brief=$brief model=$model log=$log" >&2

    sleep 3
    if [ -f "$log" ]; then
        if grep -q "Resume this session" "$log" 2>/dev/null; then
            echo "DEATH-SIGNATURE detected with model=$model" >&2
            return 1
        fi
        if grep -q "HTTP 404\|Model.*not found\|404: Model" "$log" 2>/dev/null; then
            echo "LAUNCH-FAILURE: model $model not found" >&2
            return 1
        fi
    fi
    return 0
}

# Attempt 1
if launch_leg "$BRIEF" "$MODEL" "$LOG"; then
    echo "SUCCESS: C30 leg launched with model=$MODEL" >&2
    exit 0
fi

echo "ATTEMPT 1 FAILED, retrying with fallback model=$FALLBACK_MODEL" >&2
sleep 2

# Attempt 2 (fallback model — co-base diversity: P3/P4 used laguna-s, try laguna-s as fallback)
if launch_leg "$BRIEF" "$FALLBACK_MODEL" "$LOG"; then
    echo "SUCCESS: C30 leg launched with fallback model=$FALLBACK_MODEL" >&2
    exit 0
fi

echo "FAILED: All attempts exhausted" >&2
exit 1
