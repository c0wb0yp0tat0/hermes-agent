#!/usr/bin/env bash
# c40-dispatch.sh — hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
export HERMES_CRON_JOB_NAME="c40"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
