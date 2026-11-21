#!/usr/bin/env bash
export HERMES_CRON_JOB_NAME="c42c-fork"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
