#!/usr/bin/env bash
# kaizen-assess-dispatch.sh — wrapper that hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
# Fixes the cron-system env gap (cron does not set HERMES_CRON_JOB_NAME, causing watchdog-dispatch.sh
# to default JOB_NAME=watchdog and read next-leg-spec-watchdog.txt instead of the per-job spec).
# Pattern follows c39-dispatch.sh / c34-audit-2-dispatch.sh (proven 09-30).
export HERMES_CRON_JOB_NAME="kaizen-assess"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
