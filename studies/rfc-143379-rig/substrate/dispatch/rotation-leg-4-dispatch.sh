#!/usr/bin/env bash
export HERMES_CRON_JOB_NAME="rotation-leg-4"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"

# Wrapper for Leg 4 AOA dispatch
# Self-firing lane per ACES rotation contract
# This script wraps the watchdog pattern for AoA execution

set -uo pipefail

cd /root

# Dispatch via hermes chat (session-surviving)
hermes chat --query-file /root/.hermes/cache/scratch/rotation-leg-4-brief.md \
    -m poolside/laguna-xs-2.1:free \
    --max-turns 20 \
    --reasoning-effort low \
    --oneshot \
    > /root/.hermes/cache/scratch/aoa-output.txt 2>&1

# Capture exit code
EXIT=$?

# Log result
echo "[$(date -Iseconds)] Job $JOB_NAME exit=$EXIT" >> /root/.hermes/cache/scratch/aoa-log.txt

exit $EXIT