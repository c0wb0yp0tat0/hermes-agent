#!/bin/bash
# c29-dispatch.sh — dedicated dispatch for C29 (avoids shared-spec race)
set -euo pipefail
nohup /root/.local/bin/hermes chat --query-file /root/.hermes/cache/scratch/c29-threshold-brief.md -m poolside/laguna-xs-2.1:free > /tmp/c29-threshold.txt 2>&1 &
PID=$!
echo "DISPATCHED pid=$PID brief=c29-threshold-brief.md model=poolside/laguna-xs-2.1:free log=/tmp/c29-threshold.txt"
