#!/bin/bash
# c39-dispatch.sh — wrapper that hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
# Fixes the cron-system env gap (cron does not set HERMES_CRON_JOB_NAME, causing watchdog-dispatch.sh
# to default JOB_NAME=watchdog and read next-leg-spec-watchdog.txt instead of next-leg-spec-c39-fire.txt)
# Pattern follows c34-audit-2-dispatch.sh (proven 09-30).
export HERMES_CRON_JOB_NAME="c39-fire"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
