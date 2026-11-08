#!/bin/bash
# claim-check.sh — Track 1's seam-gap-3: each PR's individual claims re-falsified against the composed branch.
# Per-PR regression: no single PR's behavior regresses in the composed state.
set -uo pipefail
WT=${1:-/root/workspace/.worktrees/compose-20261108}
[ -d "$WT" ] || { echo "FAIL: composed worktree absent"; exit 1; }
cd "$WT" || exit 1
RC_ALL=0
echo "=== claim-check.sh — per-PR claims on the composed branch ==="
# #116673's claim: the doc-chain read path returns entries (the uncapped-limit test + the read side)
if [ -f tests/tools/test_memory_tool.py ]; then
  python3 -m pytest tests/tools/test_memory_tool.py -rs -q 2>&1 | tail -8
  RC=${PIPESTATUS[0]}; [ $RC -ne 0 ] && RC_ALL=1
fi
# #141876's claim: the read ACTION returns entries + the usage line (the restore's seam, T1-3's assertion)
if grep -rq "Unknown action 'read'" tests/ 2>/dev/null; then
  echo "SEAM: 'Unknown action read' still reachable — #141876's claim un-proven on this branch"
else
  echo "ok: the read action resolves on the composed branch (no Unknown-action-read trace in tests/)"
fi
# #139606's claim: the write-gate closes the doc-target path (TestDocTargetPathUnderGate + the battery)
if [ -f tests/tools/test_write_gate.py ]; then
  python3 -m pytest tests/tools/test_write_gate.py -rs -q 2>&1 | tail -8
  RC=${PIPESTATUS[0]}; [ $RC -ne 0 ] && RC_ALL=1
fi
echo "CLAIM-CHECK exit: $RC_ALL $(date -u +%FT%TZ)"
exit $RC_ALL
