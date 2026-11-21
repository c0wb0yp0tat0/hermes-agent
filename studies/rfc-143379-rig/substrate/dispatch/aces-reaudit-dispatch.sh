#!/usr/bin/env bash
export HERMES_CRON_JOB_NAME="aces-reaudit"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
