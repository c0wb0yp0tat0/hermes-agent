#!/bin/bash
# receipt-emit.sh — Track 1's seam-gap-4: the need-id -> task -> evidence rows, append-only.
set -uo pipefail
LEDGER="/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/RECEIPT-LEDGER-20261108.md"
mkdir -p "$(dirname "$LEDGER")"
[ -f "$LEDGER" ] || printf '# RECEIPT LEDGER — 2026-11-08 (Track 1, the merge-composition falsification)\n\nAppend-only rows: need-id -> task -> evidence (exit codes + artifact paths).\n\n' > "$LEDGER"
now=$(date -u +%FT%TZ)
grep -E "^## " /tmp/compose-rows-*.md 2>/dev/null >/dev/null || true
if [ -s /tmp/compose-rows-latest.md ]; then
  while IFS= read -r row; do
    printf '| %s | %s | %s |\n' "$now" "$row" "compose-worktree" >> "$LEDGER"
  done < /tmp/compose-rows-latest.md
else
  echo ":: warning: no /tmp/compose-rows-latest.md (the rows are written by the fold)" >&2
fi
echo "RECEIPTS at: $LEDGER ($(wc -l < "$LEDGER") lines) $(date -u +%FT%TZ)"
