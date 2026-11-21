#!/usr/bin/env bash
# aces-dispatch.sh — pre-wire a FULL ACES rotation chain in ONE pass (the sustainable patch)
#
# The head's job: write the four briefs (the design), call this once per vein, fold landings.
# The board does the rest: producer → develop → audit → AoA, parented end to end,
# notify+wake on every card, each firing automatically on its parent's landing.
#
# Usage:
#   aces-dispatch.sh "<TITLE-PREFIX>" <producer-brief> <develop-brief> <audit-brief> <aoa-brief>
#   aces-dispatch.sh --resume <develop-task-id> <audit-brief> <aoa-brief>
#     (resume mode: create audit + AoA parented on an EXISTING develop leg — mid-flight chains)
#
# Bases (the verified laguna pair, flip-flop):
#   producer: laguna-s   develop: laguna-s (same team)   audit: laguna-xs   AoA: laguna-s
# Invariant: NO ADJACENT AUDIT LAYER SHARES A BASE (audit verifies develop on a distinct base).
set -euo pipefail

CHAT_ID="${KANBAN_NOTIFY_CHAT_ID:?KANBAN_NOTIFY_CHAT_ID must be set for notify subscriptions}"
cd /root/workspace/kanban-pilot-workdir

# --- brief guard: every brief must exist AND its role line must match its stage ---
guard_brief() {
  local f="$1" role="$2"
  if [ ! -f "$f" ]; then echo "MISSING BRIEF: $f — aborting, nothing created"; exit 1; fi
  if ! head -3 "$f" | grep -qi "$role"; then
    echo "BRIEF-ROLE MISMATCH: $f does not declare role $role — aborting, nothing created"
    exit 1
  fi
}

if [ "${1:-}" = "--resume" ]; then
  DEV_ID="$2"; AUD_BRIEF="$3"; AOA_BRIEF="$4"
  guard_brief "$AUD_BRIEF" "AUDIT"
  guard_brief "$AOA_BRIEF" "AUDIT-OF-AUDIT"
  echo "== Resuming chain from develop leg $DEV_ID =="
  audit=$(hermes kanban create "AUDIT (resumed, parented on $DEV_ID)" --body-file "$AUD_BRIEF" --assignee default --model poolside/laguna-xs-2.1:free --max-runtime 2h --workspace worktree:/root/workspace/kanban-pilot-workdir --parent "$DEV_ID" 2>&1 | grep -oE 't_[a-z0-9]+' | head -1)
  aoa=$(hermes kanban create "AUDIT-OF-AUDIT (resumed, parented on $audit)" --body-file "$AOA_BRIEF" --assignee default --model poolside/laguna-s-2.1:free --max-runtime 2h --workspace worktree:/root/workspace/kanban-pilot-workdir --parent "$audit" 2>&1 | grep -oE 't_[a-z0-9]+' | head -1)
  for t in "$audit" "$aoa"; do
    hermes kanban notify-subscribe "$t" --platform telegram --chat-id "$CHAT_ID" --chat-type dm --delivery-mode notify+wake >/dev/null 2>&1 || true
  done
  echo "RESUMED CHAIN: $DEV_ID → $audit → $aoa (all notify+wake armed)"
  exit 0
fi

TITLE="$1"; PROD_BRIEF="$2"; DEV_BRIEF="$3"; AUD_BRIEF="$4"; AOA_BRIEF="$5"
guard_brief "$PROD_BRIEF" "PRODUCER"
guard_brief "$DEV_BRIEF" "DEVELOP"
guard_brief "$AUD_BRIEF" "AUDIT"
guard_brief "$AOA_BRIEF" "AUDIT-OF-AUDIT"

echo "== Creating chain: $TITLE =="
producer=$(hermes kanban create "$TITLE — PRODUCER" --body-file "$PROD_BRIEF" --assignee default --model poolside/laguna-s-2.1:free --max-runtime 2h --workspace worktree:/root/workspace/kanban-pilot-workdir 2>&1 | grep -oE 't_[a-z0-9]+' | head -1)
develop=$(hermes kanban create "$TITLE — DEVELOP (the loop continues)" --body-file "$DEV_BRIEF" --assignee default --model poolside/laguna-s-2.1:free --max-runtime 2h --workspace worktree:/root/workspace/kanban-pilot-workdir --parent "$producer" 2>&1 | grep -oE 't_[a-z0-9]+' | head -1)
audit=$(hermes kanban create "$TITLE — INDEPENDENT AUDIT" --body-file "$AUD_BRIEF" --assignee default --model poolside/laguna-xs-2.1:free --max-runtime 2h --workspace worktree:/root/workspace/kanban-pilot-workdir --parent "$develop" 2>&1 | grep -oE 't_[a-z0-9]+' | head -1)
aoa=$(hermes kanban create "$TITLE — AUDIT-OF-AUDIT" --body-file "$AOA_BRIEF" --assignee default --model poolside/laguna-s-2.1:free --max-runtime 2h --workspace worktree:/root/workspace/kanban-pilot-workdir --parent "$audit" 2>&1 | grep -oE 't_[a-z0-9]+' | head -1)

for t in "$producer" "$develop" "$audit" "$aoa"; do
  hermes kanban notify-subscribe "$t" --platform telegram --chat-id "$CHAT_ID" --chat-type dm --delivery-mode notify+wake >/dev/null 2>&1 || true
done

echo "CHAIN: $producer → $develop → $audit → $aoa (all notify+wake armed)"
