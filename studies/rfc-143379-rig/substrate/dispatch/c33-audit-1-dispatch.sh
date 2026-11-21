#!/bin/bash
# c33-audit-1-dispatch.sh — wrapper that hardcodes HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
# Fixes the cron-system env gap (cron does not set HERMES_CRON_JOB_NAME, causing watchdog-dispatch.sh
# to default JOB_NAME=watchdog and read the shared spec instead of next-leg-spec-c33-audit-1.txt)
export HERMES_CRON_JOB_NAME="c33-audit-1"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
