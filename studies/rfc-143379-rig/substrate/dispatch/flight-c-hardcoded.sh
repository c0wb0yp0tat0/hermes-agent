#!/bin/bash
# Flight C Dispatch: Programmable Doc Chain Pondering
# Hardcoded spec - no JOB_NAME resolution (cron doesn't pass it)

set -euo pipefail

nohup /root/.local/bin/hermes chat --query-file /root/.hermes/cache/scratch/task-flight-c.md -m poolside/laguna-s-2.1:free > /tmp/flight-c.log 2>&1 &

echo "Flight C dispatched: pid=$!"
echo "Log: /tmp/flight-c.log"