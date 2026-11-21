#!/usr/bin/env bash
# seat-hunt.sh — hunt the HOSTED avrea VM seat for the colibri leg (colibri x hosted
# = the missing cell of the true-test 2x2). Same contract as before, but F2-fixed:
# the hunt pins ITS OWN run id and cancels ONLY its own run. It never cancels the
# queue's newest run at dispatch time.
#
# Fix F2: the previous version cancelled the queue's newest local-lm-test dispatch
# whenever a hunt try landed on a non-hosted seat, cross-firing sibling runs.
# Now:
#   1. record the NEWEST queue id BEFORE dispatch (the "before" snapshot)
#   2. dispatch a colibri-hunt-NNN run and wait for a seat
#   3. poll for a run with databaseId > the "before" snapshot (i.e. OUR run)
#   4. on non-hosted seat: cancel ONLY our own run id, NEVER the queue's newest
#   5. on exit: cancel only our own run if we did not win a hosted seat
set -uo pipefail

REPO="c0wb0yp0tat0/hermes-agent"
REF="rig/local-lm-colibri-20261113"
STUDY_REF="study/rfc-143379-rig-20261105"
MAX_TRIES="${1:-8}"
LOG="${2:-/tmp/seat-hunt.log}"

echo "$(date -u +%FT%TZ) seat-hunt start (max $MAX_TRIES tries, F2-pinned)" | tee "$LOG"

# Record the queue's newest id BEFORE any dispatch. This is the "before" snapshot.
# It is used ONLY to detect our own dispatched run (a larger id), never to cancel.
BEFORE=$(gh run list --repo "$REPO" --workflow local-lm-test.yml --limit 1 \
  --json databaseId,createdAt --jq 'sort_by(.createdAt) | reverse | .[0].databaseId // empty' 2>/dev/null)
echo "$(date -u +%FT%TZ) queue before-dispatch newest id: ${BEFORE:-<none>}" | tee -a "$LOG"

for i in $(seq 1 "$MAX_TRIES"); do
  RUN_ID="colibri-hunt-$(printf '%03d' "$i")"
  echo "$(date -u +%FT%TZ) try $i: dispatching run_id=$RUN_ID" | tee -a "$LOG"
  gh workflow run local-lm-test.yml --repo "$REPO" --ref "$REF" \
    -f study_ref="$STUDY_REF" -f run_id="$RUN_ID" \
    -f model_profile=qwen2.5-0.5b-q4km -f engine_profile=colibri-olmoe 2>>"$LOG" \
    || { echo "dispatch failed" | tee -a "$LOG"; sleep 10; continue; }

  # Poll for a run whose databaseId is LARGER than the before-snapshot.
  # That run is OURS (we just dispatched it). Poll its runner_name until a seat
  # appears (up to 90s).
  OUR_RUN=""
  for _ in $(seq 1 18); do
    NEWEST=$(gh run list --repo "$REPO" --workflow local-lm-test.yml --limit 1 \
      --json databaseId,createdAt --jq 'sort_by(.createdAt) | reverse | .[0].databaseId // empty' 2>/dev/null)
    if [ -n "$NEWEST" ] && [ "$NEWEST" -gt "${BEFORE:-0}" ] 2>/dev/null; then
      OUR_RUN="$NEWEST"
      break
    fi
    sleep 5
  done

  if [ -z "$OUR_RUN" ]; then
    echo "try $i: no run claimed (queue unchanged) — cancel + cooldown" | tee -a "$LOG"
    gh run cancel "$RUN_ID" --repo "$REPO" >/dev/null 2>&1
    sleep 90
    continue
  fi

  SEAT=""
  for _ in $(seq 1 18); do
    SEAT=$(gh api "repos/$REPO/actions/runs/$OUR_RUN/jobs" --jq '.jobs[0].runner_name // empty' 2>/dev/null)
    [ -n "$SEAT" ] && break
    sleep 5
  done

  echo "$(date -u +%FT%TZ) try $i: run=$RUN_ID our_run=$OUR_RUN seat=$SEAT" | tee -a "$LOG"
  case "$SEAT" in
    avrea-exe-*)
      echo "$(date -u +%FT%TZ) HOSTED SEAT WON — run=$RUN_ID (our_run=$OUR_RUN) left running" | tee -a "$LOG"
      echo "FINAL_RUN_ID=$RUN_ID" | tee -a "$LOG"
      echo "FINAL_RUN_DATABASE_ID=$OUR_RUN" | tee -a "$LOG"
      exit 0
      ;;
    *)
      echo "$(date -u +%FT%TZ) non-hosted seat ($SEAT) — cancel ONLY our run $OUR_RUN" | tee -a "$LOG"
      gh run cancel "$OUR_RUN" --repo "$REPO" >/dev/null 2>&1
      sleep 90
      ;;
  esac
done

echo "$(date -u +%FT%TZ) seat-hunt exhausted ($MAX_TRIES tries)" | tee -a "$LOG"
exit 1
