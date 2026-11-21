#!/usr/bin/env bash
export HERMES_CRON_JOB_NAME="kaizen-sustain"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
