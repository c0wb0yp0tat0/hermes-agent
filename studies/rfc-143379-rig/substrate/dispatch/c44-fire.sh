#!/usr/bin/env bash
# C44 Citation-Fidelity Gate Validation
# Triggered: 2026-10-04T15:08:38
# Parent: C43 adversarial confabulation stress test

export HERMES_CRON_JOB_NAME="c44"
export C44_MODEL="poolside/laguna-xs-2.1:free"
export C44_BRIEF="/root/.hermes/cache/scratch/c44-brief.md"
export C44_LOG="/root/.hermes/cache/scratch/c44.log"

echo "C44 Citation-Fidelity Gate Implementation @ $(date -Iseconds)"
echo "Job: $HERMES_CRON_JOB_NAME"
echo "Model: $C44_MODEL"

# Arm the successor via session-surviving cron
/opt/hermes/bin/hermes cron create --deliver local --no-agent --script /root/.hermes/scripts/c44-fire.sh '2m' --repeat 1 --name "$HERMES_CRON_JOB_NAME-fire"

echo "Armed: $HERMES_CRON_JOB_NAME-fire"