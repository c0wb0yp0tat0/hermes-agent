#!/usr/bin/env bash
# The disk-guard (runner-workspace class) — the SINGLE disk owner.
# v2 (2026-11-05): NEVER drains while a runner job is live — the Runner.Worker
# process owns its workspace; wiping it mid-run kills the job the host exists
# to serve (the 13:45:25Z Avrea run died exactly at the guard tick).
# Stateful alert contract: exit-1 ALERT on the first trip and on each real
# regression (free space dropped >500MB since the last alert); SILENT
# otherwise. When the drain is exhausted, the alert carries the top
# consumers so the signal is actionable, not a repeating sentence.
set -uo pipefail

THRESHOLD_PCT=92
RUNNER_WORK="/opt/actions-runner/_work"
STATEDIR="/root/.hermes/state"
STATE="$STATEDIR/runner-guard.state"
REG_KB=500000
mkdir -p "$STATEDIR"

pct=$(df / | tail -1 | awk '{gsub(/%/,"",$5); print $5}')
free_kb=$(df / | tail -1 | awk '{print $4}')
pct=${pct:-100}

if [ "$pct" -lt "$THRESHOLD_PCT" ]; then
  rm -f "$STATE"
  exit 0
fi

# alive job? defer the drain — the workspace is the job's, not scratch
if pgrep -f "Runner.Worker" >/dev/null 2>&1; then
  prev_free=$(cat "$STATE" 2>/dev/null || echo "")
  free_after="$free_kb"
  regressed=0
  if [ -n "$prev_free" ] && [ "$free_after" -lt "$((prev_free - REG_KB))" ]; then regressed=1; fi
  if [ -z "$prev_free" ] || [ "$regressed" = "1" ]; then
    echo "$free_after" > "$STATE"
    echo "[runner-guard] disk ${pct}% (${free_after} KB free); runner job ACTIVE — drain deferred. Top consumers:"
    du -sh /root/workspace/.worktrees /root/workspace/master-page /root/workspace/drop /root/workspace/repos /root/actions-runner /root/.hermes/cron/output /root/.hermes/cache/scratch 2>/dev/null | sort -rh | head -7
    exit 1
  fi
  exit 0
fi

# idle: drain the regenerable runner-scratch (checkouts re-fetch; nothing unique)
rm -rf "$RUNNER_WORK"/* 2>/dev/null
rm -f /tmp/battery-receipt.txt /tmp/avrea-* /tmp/gh-cli-cache/* 2>/dev/null
free_after=$(df / | tail -1 | awk '{print $4}')

prev_free=$(cat "$STATE" 2>/dev/null || echo "")
regressed=0
if [ -n "$prev_free" ] && [ "$free_after" -lt "$((prev_free - REG_KB))" ]; then regressed=1; fi

if [ -z "$prev_free" ] || [ "$regressed" = "1" ]; then
  echo "$free_after" > "$STATE"
  echo "[runner-guard] disk ${pct}% (${free_after} KB free), drained runner-scratch (was ${free_kb} KB). Top consumers:"
  du -sh /root/workspace/.worktrees /root/workspace/master-page /root/workspace/drop /root/workspace/repos /root/actions-runner 2>/dev/null | sort -rh | head -5
  exit 1
fi
# same condition, no regression: stay silent
exit 0
