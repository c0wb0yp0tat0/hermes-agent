#!/usr/bin/env python3
"""The LAB-LEARNING-WATCH — kvnloo's + xngg1021's repos and contributions, everywhere.

Silent when healthy; emits ONLY the new motion worth learning from:
- Their repos' recent updates (pushed branches, new PRs, fresh activity).
- Their GitHub contributions outside the tracked NousResearch issues.
The learning's home: the comment-driven-lab-ops + avrea-parallel-verification skills
gain the updates when the head folds an emission into them.
"""
import json, subprocess, sys, time

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

USERS = {"kvnloo": ["tiny-world-builder", "gh-contrib-archive", "aodl", "z0", "dash", "editor"],
         "xngg1021": ["academic-research-kernel", "hermes-agent"]}
CUTOFF = time.time() - 6 * 3600  # the last six hours' motion

lines = []
for user, repos in USERS.items():
    for repo in repos:
        try:
            r = json.loads(sh(f"gh api repos/{user}/{repo} --jq '{{updated: .updated_at, pushed: .pushed_at}}' 2>/dev/null"))
            ts = r.get("pushed_at") or r.get("updated") or ""
            if ts:
                import datetime
                if datetime.datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp() > CUTOFF:
                    lines.append(f"{user}/{repo} MOVED: pushed={ts[:16]}Z")
        except Exception:
            pass
    # their open PRs across their repos
    try:
        import json as _j
        prs = sh(f"gh search prs --author '{user}' --state open --json repository,title,number --limit 4 2>/dev/null")
        items = _j.loads(prs) if prs.strip() else []
        for it in items:
            repo = it.get("repository", {}).get("nameWithOwner", "?") if isinstance(it.get("repository"), dict) else it.get("repository", "?")
            lines.append(f"{user} OPEN-PR: {repo} #{it.get('number')} {it.get('title','')[:40]}")
    except Exception:
        pass
        pass

if lines:
    import os, json as _j
    seen_path = "/root/.hermes/cache/scratch/lab-learning-watch-seen.json"
    if os.path.exists(seen_path):
        try:
            seen = set(_j.load(open(seen_path)))
        except Exception:
            seen = set()
    else:
        seen = set()
    if not seen:
        # the baseline rule: the first run records the state, prints the baseline, exits 0
        try:
            os.makedirs(os.path.dirname(seen_path), exist_ok=True)
            open(seen_path, "w").write(_j.dumps(lines))
        except Exception:
            pass
        print("[lab-learning] baseline: " + " | ".join(lines[:8]))
        sys.exit(0)
    new = [l for l in lines if l not in seen]
    if new:
        try:
            open(seen_path, "w").write(_j.dumps(list(seen | set(new))))
        except Exception:
            pass
        # the stateful alert: NEW motion only — the delivery is the alert; exit 0 (a completed run with content)
        print("[lab-learning] NEW: " + " | ".join(new[:8]))
        sys.exit(0)
# healthy: silent
sys.exit(0)
