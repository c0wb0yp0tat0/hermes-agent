#!/usr/bin/env bash
# kaizen-evaluate-dispatch.sh — hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
export HERMES_CRON_JOB_NAME="kaizen-evaluate"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
