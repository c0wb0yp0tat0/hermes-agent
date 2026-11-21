#!/bin/bash
# c33-dispatch.sh — explicit dispatch for C33 audit-1 (fold-gap audit).
# FIX: watchdog-dispatch.sh's JOB_NAME resolution defaults to "watchdog" when
# the hermes cron system does not pass the job name as $1 or via
# HERMES_CRON_JOB_NAME env var. The reorg leg fired C33 via a DIRECT cron
# (hermes cron create --script watchdog-dispatch.sh --name c33-audit-1) and
# the JOB_NAME bug (002:156) ate the dispatch — watchdog-dispatch.sh read
# next-leg-spec-watchdog.txt instead of next-leg-spec-c33-audit-1.txt, launching
# the watchdog-brief (PID 336832) instead of C33. This wrapper hardcodes the
# spec values, bypassing the faulty resolution. Mirrors c32-dispatch.sh pattern.
set -euo pipefail

SCRATCH_DIR="/root/.hermes/cache/scratch"
BRIEF="/root/.hermes/cache/scratch/tasks/task-20261001-2030-aces-audit-1-brief.md"
MODEL="poolside/laguna-xs-2.1:free"
LOG="/root/.hermes/cache/scratch/c33-audit-1-verdict.txt"
FALLBACK_MODEL="poolside/laguna-s-2.1:free"

echo "=== c33-dispatch.sh: $(date -Iseconds) ===" >&2
echo "Job: c33-audit-1 | brief=$BRIEF model=$MODEL log=$LOG" >&2

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

# Attempt 1 (laguna-xs — launch-tested OK 23:10 EDT)
if launch_leg "$BRIEF" "$MODEL" "$LOG"; then
    echo "SUCCESS: C33 leg launched with model=$MODEL" >&2
    exit 0
fi

echo "ATTEMPT 1 FAILED, retrying with fallback model=$FALLBACK_MODEL" >&2
sleep 2

# Attempt 2 (fallback co-base: laguna-s)
if launch_leg "$BRIEF" "$FALLBACK_MODEL" "$LOG"; then
    echo "SUCCESS: C33 leg launched with fallback model=$FALLBACK_MODEL" >&2
    exit 0
fi

echo "FAILED: All attempts exhausted" >&2
exit 1
