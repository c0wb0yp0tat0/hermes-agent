#!/usr/bin/env bash
export HERMES_CRON_JOB_NAME="c43-aoa"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"