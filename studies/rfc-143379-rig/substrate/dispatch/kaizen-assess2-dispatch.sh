#!/usr/bin/env bash
export HERMES_CRON_JOB_NAME="kaizen-assess2"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
