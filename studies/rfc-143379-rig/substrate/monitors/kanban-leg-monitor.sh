#!/bin/bash
# kanban-leg-monitor.sh — death-signature monitor for kanban workers (2026-10-03)
# BAND-AID (two-way mechanism) for the known-unfixed kanban gap: the dispatcher
# detects PID death but NOT mid-flight log death-signatures (HTTP 404,
# Traceback, KeyboardInterrupt, model-not-found) while the process is alive
# but wedged. A wedged worker survives until the 4h stale timeout (enrichment
# verdict Risk 1 / R&D plan Risk 1). This monitor closes that window.
#
# Mechanism (mirrors flight-sensor.sh):
#   - Every N minutes (cron), list RUNNING kanban tasks
#   - For each, read its run log and grep for death signatures
#   - On a signature: block the task (kanban block) so the dispatcher's
#     circuit breaker + retry can re-spawn it cleanly — the block is the
#     two-way door (unblock re-arms it)
#   - Log every action to watchdog-log.md; escalate only if block fails
#
# Quiet on healthy: prints nothing (deliver origin = alerts only).

set -uo pipefail
SCRATCH="/root/.hermes/cache/scratch"
LOG="${SCRATCH}/watchdog-log.md"
ESCALATION="${SCRATCH}/WATCHDOG-ESCALATION.md"
NOW=$(date -Iseconds)
BOARD="kaizen-pilot"

# Death signatures: same family as watchdog-dispatch.sh (the 2026-10-03 class)
DEATH_SIGS="KeyboardInterrupt|interrupt_msg|_signal_handler_q|HTTP 404|Model.*not found|404: Model|Traceback|Resume this session"

# --- find running tasks on the board ---
RUNNING=$(hermes kanban list --board "${BOARD}" 2>/dev/null | grep -E "running" | awk '{print $2}' | tr -d '●' | tr -d ' ')

if [ -z "${RUNNING}" ]; then
    exit 0  # nothing running — quiet
fi

ACTED=0
for TASK in ${RUNNING}; do
    # find the task's run log (workspace dir)
    WS="/root/workspace/kanban-pilot-workdir/.worktrees/${TASK}"
    LOGFILE=""
    if [ -d "${WS}" ]; then
        LOGFILE=$(ls -t "${WS}"/.hermes/*.log "${WS}"/logs/*.log 2>/dev/null | head -1)
    fi
    # fallback: the board's workspaces dir
    [ -z "${LOGFILE}" ] && LOGFILE=$(ls -t /root/.hermes/kanban/boards/${BOARD}/workspaces/${TASK}/*.log 2>/dev/null | head -1)

    if [ -n "${LOGFILE}" ] && [ -f "${LOGFILE}" ]; then
        if grep -qE "${DEATH_SIGS}" "${LOGFILE}" 2>/dev/null; then
            # death signature found — block the task (two-way door: unblock re-arms)
            if hermes kanban block "${TASK}" --reason "death-signature detected by kanban-leg-monitor" >/dev/null 2>&1; then
                echo "KANBAN-MONITOR ${NOW}: blocked ${TASK} (death signature in ${LOGFILE})" >> "${LOG}"
                ACTED=1
            else
                echo "KANBAN-MONITOR-FAIL ${NOW}: could not block ${TASK}" >> "${LOG}"
                printf '# ESCALATION %s\nkanban-leg-monitor could not block wedged task %s.\nEvidence: %s\n' "${NOW}" "${TASK}" "${LOGFILE}" > "${ESCALATION}"
                hermes send "ESCALATION: kanban-leg-monitor could not block wedged task ${TASK}. See WATCHDOG-ESCALATION.md" -t telegram >/dev/null 2>&1
            fi
        fi
    fi
done

exit 0
