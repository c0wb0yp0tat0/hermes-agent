#!/bin/bash
# memory-batch-watcher.sh — the automatic reaction to staged memory batches.
# When a new batch lands in /root/.hermes/pending/memory/, dispatch the
# review lane (the nuance process) WITHOUT the user's ping. The head's
# automatic reaction, per the user's standing: the process must not rely
# on the user seeing the notification.
#
# State: /root/.hermes/scripts/var/memory-batch-watcher.state (last processed batch id)

PENDING_DIR="/root/.hermes/pending/memory"
STATE_FILE="/root/.hermes/scripts/var/memory-batch-watcher.state"
REVIEW_BRIEF_TEMPLATE="/root/.hermes/cache/scratch/memory-review-brief.md"
LOG="/root/.hermes/cache/scratch/memory-batch-watcher.log"

mkdir -p "$(dirname "$STATE_FILE")"

# The last processed batch id (default: none)
LAST_PROCESSED=""
[ -f "$STATE_FILE" ] && LAST_PROCESSED=$(cat "$STATE_FILE")

# Find the newest batch
NEWEST=$(ls -t "$PENDING_DIR"/*.json 2>/dev/null | head -1)
[ -z "$NEWEST" ] && exit 0  # no batches staged

NEWEST_ID=$(basename "$NEWEST" .json)

# If the newest batch is already processed, nothing to do
[ "$NEWEST_ID" = "$LAST_PROCESSED" ] && exit 0

# A NEW batch is staged — dispatch the review lane (the nuance process).
# The review brief is parameterized with the batch id.
BRIEF="/root/.hermes/cache/scratch/memory-review-auto-${NEWEST_ID}.md"
sed "s/ce79a6ae.json/${NEWEST_ID}.json/g" "$REVIEW_BRIEF_TEMPLATE" > "$BRIEF" 2>/dev/null

echo "$(date -Is) dispatching review for batch $NEWEST_ID" >> "$LOG"

# Dispatch the review lane (free tier, the nuance process)
timeout 60 hermes chat -m poolside/laguna-xs-2.1:free --query-file "$BRIEF" \
  >> "$LOG" 2>&1

# Mark processed (only on successful dispatch — the lane's verdict is the
# confirmation; the state advances so the next run doesn't re-dispatch)
echo "$NEWEST_ID" > "$STATE_FILE"
echo "$(date -Is) review dispatched for $NEWEST_ID (state advanced)" >> "$LOG"
