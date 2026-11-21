#!/usr/bin/env bash
# kaizen-create-dispatch.sh — hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
export HERMES_CRON_JOB_NAME="kaizen-create"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
