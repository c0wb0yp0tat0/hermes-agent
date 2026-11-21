#!/bin/bash
# watchdog-dispatch.sh — hardened session-surviving dispatch arm for the free watch lane.
# Reads per-job spec file (next-leg-spec-<JOBNAME>.txt) with fallback to shared.
# Launches hermes chat via nohup (detached, survives cron tick's process tree).
#
# APPROVAL GATE (handshake, binding 10-01): lanes run NON-INTERACTIVE — they can
# neither ask for nor receive approval. Protocol:
#   - A leg hitting a BLOCKED/flagged command or needing a dangerous-class command
#     (rm -rf, kill, systemctl, hermes update, git push --force, curl|sh, dd, mkfs):
#     STOPS, writes REQUEST-APPROVAL-<leg>.md (command, why, risk) to
#     /root/.hermes/cache/scratch/approvals/, polls for APPROVED-<leg>.md.
#   - APPROVED means the HEAD ran it on the USER's word (result in RESULT-<leg>.txt).
#     DENIED / timeout => ESCALATE, never execute, never retry a rephrased variant.
#   - The leg NEVER executes a flagged command itself and NEVER auto-approves.
# The head checks approvals/ at every fold glance; the user is the approval authority.
# Features:
#   - Retry with backoff (3 attempts, ~60s apart) on launch failure
#   - Death-signature detection ("Resume this session")
#   - Per-job spec isolation (no shared spec race)
#   - Fallback model chain (spec's model -> other laguna id)
#   - Task file validation hook (per-task files)
# Fired via: hermes cron create --deliver local --no-agent
#   --script watchdog-dispatch.sh '2m' --repeat 1 --name wd-fire-<N>

set -euo pipefail

# Configuration
MAX_RETRIES=3
RETRY_INTERVAL=$((60))  # seconds between retries
SHARED_SPEC="/root/.hermes/cache/scratch/next-leg-spec.txt"
SCRATCH_DIR="/root/.hermes/cache/scratch"

# Determine job name from cron job identifier (passed as first arg or derived from env)
# The cron job --name becomes the identifier
if [ -n "${1:-}" ]; then
    JOB_NAME="$1"
else
    # Fallback: derive from cron metadata if available
    JOB_NAME="${HERMES_CRON_JOB_NAME:-watchdog}"
fi

PER_JOB_SPEC="${SCRATCH_DIR}/next-leg-spec-${JOB_NAME}.txt"

# Fallback models (when laguna-xs fails, use laguna-s; when laguna-s fails, use laguna-xs)
# These detect the co-base from the model name
get_fallback_model() {
    local model="$1"
    if [[ "$model" == *"laguna-s"* ]]; then
        echo "poolside/laguna-xs-2.1:free"
    elif [[ "$model" == *"laguna-xs"* ]]; then
        echo "poolside/laguna-s-2.1:free"
    else
        # Not a laguna model, no fallback needed
        echo "$model"
    fi
}

# Death signatures: patterns that mean the leg died and must be re-fired.
# Covers launch-time failures AND mid-flight kills (SIGINT/KeyboardInterrupt —
# the 2026-10-03 stall: an external SIGINT killed both legs at 04:50:44 and the
# old dispatcher never noticed because it only checked 3s after launch).
# NOTE: "Resume this session" is NOT a death signature — it is Hermes CLI's
# normal completion message appended to every finished session log. Including it
# here caused false-positive mid-flight death reports on every completed leg
# (the orch successor's monitor_leg was always returning 1 on clean exit).
DEATH_SIGNATURES="HTTP 404|Model.*not found|404: Model|KeyboardInterrupt|interrupt_msg|_signal_handler_q|Traceback (most recent"

# Launch the leg
launch_leg() {
    local brief="$1"
    local model="$2"
    local log="$3"
    
    nohup /root/.local/bin/hermes chat --query-file "$brief" -m "$model" > "$log" 2>&1 &
    local pid=$!
    echo "DISPATCHED pid=$pid brief=$brief model=$model log=$log"
    
    # Wait briefly then check for death signature
    sleep 3
    if [ -f "$log" ]; then
        if grep -qE "$DEATH_SIGNATURES" "$log" 2>/dev/null; then
            echo "DEATH-SIGNATURE detected: session ended immediately"
            return 1
        fi
    fi
    return 0
}

# Monitor a launched leg for mid-flight death. Polls the pid; if it dies with a
# death signature in the log, return 1 (caller re-fires). If it exits cleanly
# (no signature), return 0. This closes the 2026-10-03 gap: legs killed minutes
# into the run (SIGINT) were never re-dispatched because nothing watched them.
monitor_leg() {
    local pid="$1"
    local log="$2"
    local max_wait="${3:-3600}"  # default: watch up to 1h
    local waited=0
    local poll=20

    echo "MONITOR: watching pid=$pid log=$log (max ${max_wait}s)" >&2
    while [ $waited -lt $max_wait ]; do
        if ! kill -0 "$pid" 2>/dev/null; then
            # Process gone. Death signature or clean exit?
            if [ -f "$log" ] && grep -qE "$DEATH_SIGNATURES" "$log" 2>/dev/null; then
                echo "MONITOR: DEATH-SIGNATURE in log after ${waited}s — leg died mid-flight" >&2
                return 1
            fi
            echo "MONITOR: pid=$pid exited cleanly after ${waited}s (no death signature)" >&2
            return 0
        fi
        sleep $poll
        waited=$((waited + poll))
    done
    echo "MONITOR: max wait (${max_wait}s) elapsed, pid=$pid still alive — leaving it" >&2
    return 0
}

# Read spec from per-job file (preferred) or shared file (fallback)
read_spec() {
    if [ -f "$PER_JOB_SPEC" ]; then
        echo "Using per-job spec: $PER_JOB_SPEC" >&2
        read -r BRIEF MODEL LOG < "$PER_JOB_SPEC" || true
    elif [ -f "$SHARED_SPEC" ]; then
        echo "Falling back to shared spec: $SHARED_SPEC" >&2
        read -r BRIEF MODEL LOG < "$SHARED_SPEC" || true
    else
        echo "NO_SPEC" >&2
        exit 0
    fi
    
    if [ -z "$BRIEF" ] || [ -z "$MODEL" ]; then
        echo "BAD_SPEC" >&2
        exit 0
    fi
    
    [ -n "$LOG" ] || LOG="${SCRATCH_DIR}/wd-fired-${JOB_NAME:-default}.txt"
}

# Validate per-task file (if brief is a task file, not watch-brief.md)
validate_task_file() {
    local brief="$1"
    local job_name="$2"
    
    # Check if this is a per-task file (matches pattern task-*.md)
    if [[ "$brief" == *"/task-"*".md" ]]; then
        if [ ! -f "$brief" ]; then
            echo "ERROR: Task file not found: $brief" >&2
            return 1
        fi
        if [ ! -r "$brief" ]; then
            echo "ERROR: Task file not readable: $brief" >&2
            return 1
        fi
        echo "Validated task file: $brief" >&2
    fi
    return 0
}

# Main execution
echo "=== watchdog-dispatch.sh: Job $JOB_NAME @ $(date -Iseconds) ===" >&2

# Read spec (per-job preferred, shared as fallback)
read_spec

# Validate task file exists (per-task file validation hook)
if [ -f "$PER_JOB_SPEC" ]; then
    # Per-job spec: verify the brief (task file) exists and is readable
    if ! validate_task_file "$BRIEF" "$JOB_NAME"; then
        exit 1
    fi
elif [ -f "$SHARED_SPEC" ] && [ "$BRIEF" != "watchdog-brief.md" ]; then
    # Shared spec with non-watch brief: verify it's a valid task file
    if ! validate_task_file "$BRIEF" "$JOB_NAME"; then
        exit 1
    fi
fi

# Get the current model and potential fallback
ORIGINAL_MODEL="$MODEL"
FALLBACK_MODEL=$(get_fallback_model "$MODEL")

echo "Spec: brief=$BRIEF model=$MODEL log=$LOG" >&2
echo "Fallback model: $FALLBACK_MODEL" >&2

# Retry loop with backoff + mid-flight monitoring
ATTEMPT=1
CURRENT_MODEL="$MODEL"
while [ $ATTEMPT -le $MAX_RETRIES ]; do
    echo "=== ATTEMPT $ATTEMPT/$MAX_RETRIES: model=$CURRENT_MODEL @ $(date -Iseconds) ===" >> "$LOG"
    echo "RETRY: Attempt $ATTEMPT/$MAX_RETRIES (model=$CURRENT_MODEL)" >&2
    
    if launch_leg "$BRIEF" "$CURRENT_MODEL" "$LOG"; then
        # Launched. Now monitor for mid-flight death (the 2026-10-03 gap).
        # Capture the pid from the DISPATCHED line.
        LEG_PID=$(grep -oE "pid=[0-9]+" "$LOG" | tail -1 | cut -d= -f2)
        if [ -n "$LEG_PID" ] && monitor_leg "$LEG_PID" "$LOG"; then
            echo "SUCCESS: Leg launched and survived monitoring (model=$CURRENT_MODEL)" >&2
            echo "DISPATCHED brief=$BRIEF model=$CURRENT_MODEL log=$LOG" >> "$LOG"
            exit 0
        fi
        # monitor_leg returned 1 = mid-flight death signature. Fall through to retry.
        echo "MID-FLIGHT DEATH: leg died with a death signature — re-firing" >&2
    fi
    
    echo "FAILED: Attempt $ATTEMPT - checking retry conditions" >&2
    ATTEMPT=$((ATTEMPT + 1))
    
    if [ $ATTEMPT -le $MAX_RETRIES ]; then
        echo "RETRY: Waiting $RETRY_INTERVAL seconds before attempt $ATTEMPT..." >&2
        sleep $RETRY_INTERVAL
        
        # Update model for next attempt (use fallback if available and different)
        if [ "$CURRENT_MODEL" = "$ORIGINAL_MODEL" ] && [ "$ORIGINAL_MODEL" != "$FALLBACK_MODEL" ]; then
            CURRENT_MODEL="$FALLBACK_MODEL"
        fi
    fi
done

echo "FAILED: All $MAX_RETRIES attempts exhausted with model=$ORIGINAL_MODEL (fallback=$FALLBACK_MODEL)" >&2
exit 1