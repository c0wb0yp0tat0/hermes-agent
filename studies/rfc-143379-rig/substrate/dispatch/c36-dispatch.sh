#!/bin/bash
# c36-dispatch.sh — wrapper that sets HERMES_CRON_JOB_NAME for watchdog-dispatch.sh
# Fixes the JOB_NAME bug (002:156): cron does not pass the job name as $1 or via
# HERMES_CRON_JOB_NAME, causing watchdog-dispatch.sh to default to "watchdog" and
# read the shared next-leg-spec.txt instead of the per-job spec.
# This wrapper sets HERMES_CRON_JOB_NAME="c36-verification" so watchdog-dispatch.sh
# reads next-leg-spec-c36-verification.txt (per-job spec isolation, 002:175).
export HERMES_CRON_JOB_NAME="c36-verification"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
