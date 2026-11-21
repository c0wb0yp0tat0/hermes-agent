#!/usr/bin/env bash
# Headroom-sweep: proactive cleanup of transient working sets (re-creatable only).
# Safe automation: git clones + sandboxes older than 48h in lane workspaces are
# disposable (re-cloneable); valuable artifacts (verdict .md files) are never touched.
# Wired 2026-10-18 per the disk-deadlock lesson (watch-alone was too late).
set -u

THRESHOLD=6  # GB: root free below this = aggressive sweep
AGE_HOURS=48 # clones/sandboxes older than this are swept

FREE_GB=$(df -BG / | awk 'NR==2 {gsub("G","",$4); print $4}')
FOUND=0

# Always sweep stale transient sets (re-creatable, safe any time)
while IFS= read -r d; do
  [ -z "$d" ] && continue
  if [ "$(find "$d" -maxdepth 0 -mmin +$((AGE_HOURS*60)) 2>/dev/null)" ]; then
    sz=$(du -sh "$d" 2>/dev/null | cut -f1)
    rm -rf "$d" && echo "HEADROOM-SWEEP: removed $d ($sz)"
    FOUND=$((FOUND+1))
  fi
done < <(find /root/.hermes/kanban/workspaces -maxdepth 3 -type d \( -name '*clone*' -o -name 'sandbox-*' -o -name 'final-verify' -o -name 'verify-clone' -o -name 'fresh-clone' \) 2>/dev/null)

# Aggressive sweep when headroom is thin
if [ "$FREE_GB" -lt "$THRESHOLD" ]; then
  echo "HEADROOM-ALERT: root free ${FREE_GB}G (< ${THRESHOLD}G) — sweep above done; consider the deeper offload (old DONE lanes -> private repo + manifest)."
fi

[ "$FOUND" -gt 0 ] && echo "HEADROOM-SWEEP: done ($FOUND sets swept)" || true
exit 0
