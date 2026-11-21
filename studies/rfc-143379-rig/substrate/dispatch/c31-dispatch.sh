#!/bin/bash
# C31 Generation Verification Dispatch Wrapper
# Bypasses watchdog-dispatch.sh JOB_NAME bug (cron doesn't pass job name as $1)

BRIEF="/root/.hermes/cache/scratch/c31-generation-verification.md"
MODEL="poolside/laguna-xs-2.1:free"
LOG="/tmp/c31-generation-results.json"

cd /root
nohup hermes chat --query-file "$BRIEF" -m "$MODEL" > "$LOG" 2>&1 &
echo "C31 dispatch launched: PID $!"