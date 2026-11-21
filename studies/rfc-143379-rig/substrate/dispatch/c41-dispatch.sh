#!/usr/bin/env bash
# c41-dispatch.sh — hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
export HERMES_CRON_JOB_NAME="c41"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
