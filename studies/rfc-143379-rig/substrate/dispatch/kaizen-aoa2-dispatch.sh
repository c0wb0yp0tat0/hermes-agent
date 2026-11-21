#!/bin/bash
# kaizen-aoa2-dispatch.sh — session-surviving one-shot dispatch arm for AoA2 leg
# Fired by the gateway cron daemon (NOT a leg's bg child)
# Reads NEXT-LEG-READY marker, launch-tests model, fires leg, verifies handles
# Contract per kaizen-flight-plan.md Section 5 + 002:149/156/164 (self-fire mechanism)
# Wrapper: export HERMES_CRON_JOB_NAME=kaizen-aoa2; exec watchdog-dispatch.sh

set -euo pipefail

# Hardcode job name as per 002:156 (cron does not pass job name as $1 or via HERMES_CRON_JOB_NAME env)
export HERMES_CRON_JOB_NAME="kaizen-aoa2"

# Execute watchdog-dispatch.sh with the delay argument
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"