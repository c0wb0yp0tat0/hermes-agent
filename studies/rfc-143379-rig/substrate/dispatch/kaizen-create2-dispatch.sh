#!/usr/bin/env bash
# kaizen-create2-dispatch.sh — hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
export HERMES_CRON_JOB_NAME="kaizen-create2"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
