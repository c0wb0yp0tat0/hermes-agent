#!/bin/bash
# audit-gate-launch.sh — prestaged orchestration gate (2026-10-03)
# Waits for the sensor-repair CROSS-AUDIT verdict to land, then immediately
# launches BOTH ACES teams with the fixes. Session-surviving (cron arm).
#
# Contract:
#   - Polls for /root/.hermes/cache/scratch/sensor-repair-audit-verdict.txt
#     (bounded: up to 45 min; the audit lane is in flight now)
#   - On PASS: fire both teams (kaizen chain + gemba re-audit) via
#     session-surviving cron arms, verify each arm, log handles.
#   - On HAND-BACK: do NOT launch — escalate to the head (the audit found a
#     defect; launching on a failed audit would compound it).
#   - On timeout: escalate (audit overdue — head checks the lane).
#   - Quiet on healthy wait: prints nothing until it acts.

set -uo pipefail
SCRATCH="/root/.hermes/cache/scratch"
LOG="${SCRATCH}/watchdog-log.md"
ESCALATION="${SCRATCH}/WATCHDOG-ESCALATION.md"
AUDIT_VERDICT="${SCRATCH}/sensor-repair-audit-verdict.txt"
NOW=$(date -Iseconds)
MAX_WAIT=2700   # 45 min
POLL=20

# --- helper: arm present? (grep -c form — NEVER grep -q in a pipeline under
# pipefail; the SIGPIPE class, 2026-10-03) ---
arm_present() {
    local name="$1"
    local count
    count=$(hermes cron list 2>/dev/null | grep -c "Name:      ${name}")
    [ "${count}" -gt 0 ]
}

# --- helper: fire one team's launch via session-surviving cron arm ---
fire_team() {
    local job="$1"      # e.g. kaizen-orch-fire | aces-reaudit-fire
    local wrapper="$2"  # e.g. kaizen-orch-dispatch.sh | aces-reaudit-dispatch.sh
    local delay="$3"    # e.g. 2m
    if arm_present "${job}"; then
        echo "ALREADY-ARMED ${job}"
        return 0
    fi
    hermes cron create --deliver local --no-agent --script "${wrapper}" "${delay}" --repeat 1 --name "${job}" >/dev/null 2>&1
    if arm_present "${job}"; then
        echo "FIRED ${job} @ ${NOW}"
    else
        echo "FIRE-FAIL ${job} @ ${NOW}"
    fi
}

# --- wait for the audit verdict (bounded) ---
waited=0
while [ $waited -lt $MAX_WAIT ]; do
    if [ -f "${AUDIT_VERDICT}" ]; then
        break
    fi
    sleep $POLL
    waited=$((waited + POLL))
done

if [ ! -f "${AUDIT_VERDICT}" ]; then
    echo "GATE-TIMEOUT ${NOW}: audit verdict not found after ${MAX_WAIT}s" >> "${LOG}"
    printf '# ESCALATION %s\naudit-gate timed out waiting for sensor-repair-audit-verdict.txt.\n' "${NOW}" > "${ESCALATION}"
    hermes send "ESCALATION: audit-gate timed out waiting for the cross-audit verdict. See WATCHDOG-ESCALATION.md" -t telegram >/dev/null 2>&1
    exit 1
fi

# --- read the verdict disposition ---
if grep -q "HAND-BACK" "${AUDIT_VERDICT}"; then
    echo "GATE-HOLD ${NOW}: audit returned HAND-BACK — teams NOT launched. Head must review." >> "${LOG}"
    printf '# ESCALATION %s\nCross-audit returned HAND-BACK. Teams not launched per gate contract.\nEvidence: %s\n' "${NOW}" "${AUDIT_VERDICT}" > "${ESCALATION}"
    hermes send "ESCALATION: cross-audit HAND-BACK — teams held. See WATCHDOG-ESCALATION.md" -t telegram >/dev/null 2>&1
    exit 1
fi

# --- PASS: launch both teams with the fixes ---
echo "GATE-PASS ${NOW}: audit PASS — launching both teams." >> "${LOG}"

# Team 1: kaizen — ensure the orchestrator chain is armed (it self-perpetuates;
# the gate only re-arms if it went dark).
K1=$(fire_team "kaizen-orch-fire" "kaizen-orch-dispatch.sh" "2m")
echo "KAIZEN ${K1}" >> "${LOG}"

# Team 2: gemba — fire the re-audit leg (the ACES track plateaued at C42d;
# the re-audit steer is due per user sequencing: re-audit once the track
# shows no measurable improvement).
# THERMAL HOLD (user steer 2026-10-03): if Whisper is running (the X-video
# transcription), the gemba re-audit must THINK + PLAN but NOT run local
# engine probes until Whisper completes — one CPU-heavy job at a time on
# pve-1 (91°C thermal trip; Whisper alone ≈ 71-77°C). Write the hold marker;
# the re-audit brief checks it and defers probes.
if pgrep -f "faster_whisper|WhisperModel|transcribe" > /dev/null 2>&1; then
    printf 'HOLD-LOCAL-TESTS (2026-10-03): Whisper transcription in progress.\nGemba re-audit: think + plan + sweep (read-only), but DO NOT run local engine probes until this marker is cleared.\nCleared by: the head when the whisper task completes.\n' > "${SCRATCH}/HOLD-LOCAL-TESTS-whisper.md"
    echo "THERMAL-HOLD ${NOW}: whisper running — gemba probes deferred (marker written)" >> "${LOG}"
fi
G1=$(fire_team "aces-reaudit-fire" "aces-reaudit-dispatch.sh" "2m")
echo "GEMBA ${G1}" >> "${LOG}"

# --- verify both arms landed (the proof) ---
KAIZEN_OK=0; GEMBA_OK=0
arm_present "kaizen-orch-fire" && KAIZEN_OK=1
arm_present "aces-reaudit-fire" && GEMBA_OK=1

if [ "${KAIZEN_OK}" -eq 1 ] && [ "${GEMBA_OK}" -eq 1 ]; then
    echo "GATE-COMPLETE ${NOW}: kaizen + gemba both armed. Handles in watchdog-log." >> "${LOG}"
    exit 0
fi

# --- partial failure: escalate (one team not armed) ---
printf '# ESCALATION %s\nGate PASS but launch incomplete: kaizen_ok=%s gemba_ok=%s\nEvidence: %s\n' "${NOW}" "${KAIZEN_OK}" "${GEMBA_OK}" "${LOG}" > "${ESCALATION}"
hermes send "ESCALATION: audit PASS but team launch incomplete (kaizen=${KAIZEN_OK} gemba=${GEMBA_OK}). See WATCHDOG-ESCALATION.md" -t telegram >/dev/null 2>&1
exit 1
