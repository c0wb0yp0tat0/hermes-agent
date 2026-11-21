#!/usr/bin/env bash
# kaizen-evaluate2-dispatch.sh — session-surviving one-shot dispatch arm for
# Evaluate2 leg (cycle 2 of surfacing-decision kaizen).
# Hardcodes HERMES_CRON_JOB_NAME to bypass watchdog-dispatch.sh JOB_NAME
# resolution bug (002:156): cron does not pass job name as $1 or via
# HERMES_CRON_JOB_NAME env var — without this wrapper, the dispatch defaults
# to "watchdog" and reads next-leg-spec-watchdog.txt instead of the per-job spec.
# Mirrors c30-dispatch.sh pattern (Flight 36, 2026-10-01).
export HERMES_CRON_JOB_NAME="kaizen-evaluate2"
exec /root/.hermes/scripts/watchdog-dispatch.sh "$@"
