#!/usr/bin/env bash
# Route-survival test for the master page's 7 JSON routes (plan B12).
# Run after ANY md_server.py change or restart. All 7 routes must return 200.
# Usage: bash /root/scripts/route-survival-test.sh [HOST] [PORT]
#   default HOST=${HOME_HOST:-localhost} (env-driven), PORT=8789 (master).
# Exit 0 = all routes 200 (PASS); exit 1 = one or more failed.
HOST="${1:-${HOME_HOST:-localhost}}"
PORT="${2:-8789}"
routes=(pulse.json pulse-agents.json pulse-agents-verbose.json approvals.json bench-status.json bench-output.json telegram-session.json)
fail=0
for r in "${routes[@]}"; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "http://$HOST:$PORT/$r")
  if [ "$code" = "200" ]; then
    echo "OK   $r -> $code"
  else
    echo "FAIL $r -> $code"
    fail=1
  fi
done
if [ "$fail" = "0" ]; then
  echo "ROUTE-SURVIVAL: PASS (all 7 routes 200)"
  exit 0
else
  echo "ROUTE-SURVIVAL: FAIL (one or more routes not 200)"
  exit 1
fi
