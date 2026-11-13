#!/bin/bash
# compose.sh — Track 1's seam-gap-1: the composed-state apply (the merge-composition falsification).
# Order: the T1-1 decision row's decided order (recorded in RECEIPT-LEDGER-20261108.md).
# Abort (exit 2) on conflict — a conflict is DATA (seam-gap-1's honest state), never a silent skip.
set -uo pipefail
REPO=/root/workspace/repos/hermes-agent
WT=/root/workspace/.worktrees/compose-20261108
ORDER_FILE=$1   # the decided order, one PR-name per line: 141876 / 116673 / 139606
[ -s "$ORDER_FILE" ] || { echo "FAIL: order file required (T1-1's decision row)"; exit 1; }
echo "=== compose.sh — the order from the T1-1 decision row ==="
cat "$ORDER_FILE"
# fresh worktree off the pinned base
rm -rf "$WT"; git -C "$REPO" worktree prune >/dev/null 2>&1
git -C "$REPO" worktree add "$WT" --detach origin/main >/dev/null 2>&1 || { echo "FAIL worktree"; exit 1; }
echo "base: $(git -C "$WT" rev-parse HEAD)"
for PR in $(cat "$ORDER_FILE"); do
  case "$PR" in
    141876) TIP=pr-141876; DESC="#141876 restore-read-action" ;;
    116673) TIP=pr-116673; DESC="#116673 the doc-chain read side" ;;
    139606) TIP=pr-139606; DESC="#139606 the write-gate" ;;
    *) echo "FAIL unknown PR in order file: $PR"; exit 1 ;;
  esac
  echo "--- applying $DESC ($(git -C "$REPO" rev-parse --short $TIP)) ---"
  git -C "$WT" merge --no-edit --no-ff "$TIP" >/tmp/compose-merge-$PR.log 2>&1
  RC=$?
  if [ $RC -ne 0 ]; then
    echo "CONFLICT on $PR (exit $RC) — seam-gap-1 OPEN for $PR; hunks:"
    git -C "$WT" diff --name-only --diff-filter=U | sed 's/^/  conflicted: /'
    echo "CONFLICT-DATA: $PR $(date -u +%FT%TZ)" >> /tmp/compose-conflicts.log
    git -C "$WT" merge --abort >/dev/null 2>&1
    echo "resolve-required: $PR" >> /tmp/compose-conflicts.log
    exit 2
  fi
  echo "applied clean: $DESC -> $(git -C "$WT" rev-parse --short HEAD)"
done
echo "=== COMPOSED HEAD ==="
git -C "$WT" log --oneline -5
echo "COMPOSED-OK $(date -u +%FT%TZ)"
