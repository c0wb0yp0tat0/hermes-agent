#!/usr/bin/env bash
# kaizen-evaluate3-dispatch.sh — session-surviving one-shot dispatch arm for
# Evaluate3 leg (cycle 3 of surfacing-decision kaizen).
# Hardcodes HERMES_CRON_JOB_NAME to bypass watchdog-dispatch.sh JOB_NAME
# resolution bug (002:156).
export HERMES_CRON_JOB_NAME="kaizen-evaluate3"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"