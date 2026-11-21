#!/bin/bash
# c42b-dispatch.sh — wrapper that hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
# Fixes the cron-system env gap (cron does not set HERMES_CRON_JOB_NAME, causing watchdog-dispatch.sh
# to default JOB_NAME=watchdog and read next-leg-spec-watchdog.txt instead of next-leg-spec-c42b-fire.txt)
# Pattern follows c39-dispatch.sh (proven pattern).
export HERMES_CRON_JOB_NAME="c42b-fire"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
