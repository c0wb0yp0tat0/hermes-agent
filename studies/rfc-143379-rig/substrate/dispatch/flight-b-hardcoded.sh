#!/bin/bash
# Flight B Dispatch: 140+ Lessons Field Evidence
# Hardcoded spec - no JOB_NAME resolution (cron doesn't pass it)

set -euo pipefail

nohup /root/.local/bin/hermes chat --query-file /root/.hermes/cache/scratch/task-flight-b.md -m poolside/laguna-xs-2.1:free > /tmp/flight-b.log 2>&1 &

echo "Flight B dispatched: pid=$!"
echo "Log: /tmp/flight-b.log"