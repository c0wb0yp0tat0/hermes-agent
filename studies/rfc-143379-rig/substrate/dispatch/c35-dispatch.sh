#!/bin/bash
# c35-dispatch.sh — explicit dispatch for C35 verification leg (C32 fix integration).
# FIX: watchdog-dispatch.sh's JOB_NAME resolution defaults to "watchdog" when the
# hermes cron system does not pass the job name as $1 or via HERMES_CRON_JOB_NAME.
# The c35-verification cron fired but read next-leg-spec-watchdog.txt (wrong brief).
# This wrapper hardcodes the spec values, bypassing faulty JOB_NAME resolution.
# Pattern: mirrors c32-dispatch.sh (verified +x, launched C32 successfully).
set -euo pipefail

SCRATCH_DIR="/root/.hermes/cache/scratch"
BRIEF="/root/.hermes/cache/scratch/c35-verification-brief.md"
MODEL="poolside/laguna-xs-2.1:free"
LOG="/tmp/c35-verification1.txt"
FALLBACK_MODEL="poolside/laguna-s-2.1:free"

echo "=== c35-dispatch.sh: $(date -Iseconds) ===" >&2
echo "Job: c35-verification | brief=$BRIEF model=$MODEL log=$LOG" >&2

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

# Attempt 1: laguna-xs-2.1:free (co-base per C35 brief: C34 used laguna-s, C35 uses laguna-xs)
if launch_leg "$BRIEF" "$MODEL" "$LOG"; then
    echo "SUCCESS: C35 leg launched with model=$MODEL" >&2
    exit 0
fi

echo "ATTEMPT 1 FAILED, retrying with fallback model=$FALLBACK_MODEL" >&2
sleep 2

# Attempt 2: fallback to laguna-s-2.1:free (co-base fallback)
if launch_leg "$BRIEF" "$FALLBACK_MODEL" "$LOG"; then
    echo "SUCCESS: C35 leg launched with fallback model=$FALLBACK_MODEL" >&2
    exit 0
fi

echo "FAILED: All attempts exhausted" >&2
exit 1