#!/bin/bash
# flight-sensor.sh — the head's automatic fail-safe sensor (2026-10-03)
# Detects stalled orchestration (dark loops) WITHOUT the user having to say so.
# Runs via cron every ~12 min, free (no LLM), quiet on healthy checks, loud on action.
#
# Stall definition (ALL of):
#   1. No in-flight `hermes chat` process (probe/search lanes)
#   2. No orchestrator arms in cron list (kaizen-orch-fire / aces-orch-fire)
#   3. A team marker exists with STATUS: CONTINUE (work owed)
# => dark loop: the chain owes work but nothing is armed or running.
#
# Actions (autonomous-overcoming loop, 001 09-30):
#   - Re-arm the stalled orchestrator(s) via the session-surviving cron arm
#     (cheap, reversible — the band-aid that keeps the loop moving)
#   - Log the miss + re-arm handle to watchdog-log.md
#   - Escalate (hermes send + escalation file) ONLY if the re-arm fails
#     (script cannot execute the re-arm = true fail-safe failure)
#
# Quiet on clean checks: prints nothing (deliver origin = alerts only).

set -uo pipefail
SCRATCH="/root/.hermes/cache/scratch"
LOG="${SCRATCH}/watchdog-log.md"
ESCALATION="${SCRATCH}/WATCHDOG-ESCALATION.md"
NOW=$(date -Iseconds)
ACTED=0

# --- helper: is a cron arm present? ---
# NOTE (2026-10-03): never use `cron list | grep -q` under `pipefail` — grep -q
# exits on the first match, SIGPIPEs the producer, and pipefail turns that into
# a false "not present". Count instead (grep -c reads all input).
arm_present() {
    local name="$1"
    local count
    count=$(hermes cron list 2>/dev/null | grep -c "Name:      ${name}")
    [ "${count}" -gt 0 ]
}

# --- helper: re-arm one orchestrator (returns handle proof) ---
rearm_orch() {
    local job="$1"   # kaizen-orch-fire | aces-orch-fire
    local wrapper="$2"
    local spec_ok=1
    [ -f "${SCRATCH}/next-leg-spec-${job%-fire}.txt" ] || spec_ok=0
    # Keep the spec pointing at the orchestrator's task file; if missing, fall
    # back to the canonical orchestrator brief if present.
    hermes cron create --deliver local --no-agent --script "${wrapper}" '2m' --repeat 1 --name "${job}" >/dev/null 2>&1
    if arm_present "${job}"; then
        echo "REARMED ${job} @ ${NOW} (spec_ok=${spec_ok})"
    else
        echo "REARM-FAIL ${job} @ ${NOW}"
    fi
}

# --- 1. in-flight check ---
IN_FLIGHT=$(pgrep -f "hermes chat" | wc -l)

# --- 2. orchestrator arms present? ---
KAIZEN_ARM=0; ACES_ARM=0
arm_present "kaizen-orch-fire" && KAIZEN_ARM=1
arm_present "aces-orch-fire" && ACES_ARM=1

# --- 3. team markers: do teams owe work? ---
KAIZEN_OWES=0; ACES_OWES=0
if [ -f "${SCRATCH}/kaizen-next-leg-ready" ]; then
    grep -q "STATUS: CONTINUE" "${SCRATCH}/kaizen-next-leg-ready" && KAIZEN_OWES=1
fi
if [ -f "${SCRATCH}/NEXT-LEG-READY" ]; then
    grep -q "STATUS: CONTINUE" "${SCRATCH}/NEXT-LEG-READY" && ACES_OWES=1
fi

# --- detect + act ---
# Kaizen: owes work, no process, no arm => dark loop
if [ "${IN_FLIGHT}" -eq 0 ] && [ "${KAIZEN_OWES}" -eq 1 ] && [ "${KAIZEN_ARM}" -eq 0 ]; then
    LINE="MISS ${NOW}: kaizen owes work (marker CONTINUE) but no process + no kaizen-orch arm. $(rearm_orch kaizen-orch-fire kaizen-orch-dispatch.sh)"
    echo "${LINE}" >> "${LOG}"
    ACTED=1
fi

# ACES: owes work, no process, no arm => dark loop
if [ "${IN_FLIGHT}" -eq 0 ] && [ "${ACES_OWES}" -eq 1 ] && [ "${ACES_ARM}" -eq 0 ]; then
    LINE="MISS ${NOW}: aces owes work (marker CONTINUE) but no process + no aces-orch arm. $(rearm_orch aces-orch-fire aces-orch-dispatch.sh)"
    echo "${LINE}" >> "${LOG}"
    ACTED=1
fi

# --- escalation: re-arm failed (both teams owed work and are dark) ---
if [ "${ACTED}" -eq 1 ]; then
    # check whether the re-arms actually landed
    KAIZEN_ARM=0; ACES_ARM=0
    arm_present "kaizen-orch-fire" && KAIZEN_ARM=1
    arm_present "aces-orch-fire" && ACES_ARM=1
    if [ "${KAIZEN_OWES}" -eq 1 ] && [ "${KAIZEN_ARM}" -eq 0 ]; then
        printf '# ESCALATION %s\nkaizen re-arm FAILED by flight-sensor.\nEvidence: %s\n' "${NOW}" "${LOG}" > "${ESCALATION}"
        hermes send "ESCALATION: flight-sensor could not re-arm kaizen orch. See WATCHDOG-ESCALATION.md" -t telegram >/dev/null 2>&1
    fi
    if [ "${ACES_OWES}" -eq 1 ] && [ "${ACES_ARM}" -eq 0 ]; then
        printf '# ESCALATION %s\naces re-arm FAILED by flight-sensor.\nEvidence: %s\n' "${NOW}" "${LOG}" > "${ESCALATION}"
        hermes send "ESCALATION: flight-sensor could not re-arm aces orch. See WATCHDOG-ESCALATION.md" -t telegram >/dev/null 2>&1
    fi
fi

# Quiet on healthy: no output.
exit 0
