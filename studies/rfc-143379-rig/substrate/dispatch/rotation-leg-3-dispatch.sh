#!/usr/bin/env bash
export HERMES_CRON_JOB_NAME="rotation-leg-3"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"