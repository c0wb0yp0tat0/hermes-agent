#!/bin/bash
# test-suite.sh — Track 1's seam-gap-2: the composed state's unit + integration tests.
# The pinned battery (the workflow's own selection): write-gate + memory-tool + falsifier-battery.
set -uo pipefail
WT=${1:-/root/workspace/.worktrees/compose-20261108}
[ -d "$WT" ] || { echo "FAIL: composed worktree absent (run compose.sh first)"; exit 1; }
BASE="tests/tools/test_write_gate.py tests/tools/test_memory_tool.py"
[ -d "$WT/tests/falsifier-battery" ] && BASE="$BASE tests/falsifier-battery/"
cd "$WT" || exit 1
echo "=== test-suite.sh — the composed battery ==="
python3 -m pytest $BASE -rs -q 2>&1 | tail -25
RC=${PIPESTATUS[0]}
echo "TEST-SUITE exit: $RC $(date -u +%FT%TZ)"
exit $RC
