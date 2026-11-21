#!/usr/bin/env bash
# kaizen-create3-dispatch.sh — session-surviving one-shot dispatch arm for Create3 leg
# Hardcodes HERMES_CRON_JOB_NAME to bypass watchdog-dispatch.sh JOB_NAME
# resolution bug (002:156). Launches leg via nohup (detached, survives cron tick).
# Contract: read next-leg-spec-kaizen-create3.txt (per-job spec isolation), launch-test,
# fire leg, verify handle. Per 002:175/002:193.
export HERMES_CRON_JOB_NAME="kaizen-create3"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"