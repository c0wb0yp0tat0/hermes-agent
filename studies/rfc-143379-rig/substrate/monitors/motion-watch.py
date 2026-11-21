#!/usr/bin/env python3
"""Motion watchdog for the touched hermes-agent surfaces.

Silent-when-idle: diffs a JSON state file against live gh api snapshots;
prints ONLY changes. Empty stdout = silence (no_agent cron contract).
Fetch through the AUTHENTICATED gh CLI (user token, 5,000/hr) — never
unauthenticated urllib (shared-IP 60/hr pool, 403s under load).
"""
import json
import os
import subprocess
import sys

STATE_FILE = os.path.expanduser("~/.hermes/scripts/motion-watch-state.json")
TRACKED = [135039, 110126, 11548, 116673, 128990, 116788, 93263, 54572, 139606]
GISTS = ["e2506fef149ccdc54d48de43fffc1646", "9a1b05cdb207104c112e658554868c38", "a5f39d8e403a3941a38842c916353e2a"]


def snapshot(n):
    """Return the tracked fields for issue/PR n via gh api."""
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/NousResearch/hermes-agent/issues/{n}",
             "--jq", "{state, comments, updated_at, title}"],
            capture_output=True, text=True, timeout=30, check=True)
        return json.loads(out.stdout)
    except Exception as e:
        # transient errors are not motion — write to stderr, return None
        print(f"ERROR #{n}: {e}", file=sys.stderr)
        return None


def gist_snapshot(g):
    """Return the tracked fields for gist g via gh api (comments + updated_at)."""
    try:
        out = subprocess.run(
            ["gh", "api", f"gists/{g}",
             "--jq", "{comments, updated_at, description}"],
            capture_output=True, text=True, timeout=30, check=True)
        return json.loads(out.stdout)
    except Exception as e:
        print(f"ERROR gist {g[:8]}: {e}", file=sys.stderr)
        return None


def main():
    cur = {}
    for n in TRACKED:
        s = snapshot(n)
        if s is not None:
            cur[str(n)] = s
    for g in GISTS:
        s = gist_snapshot(g)
        if s is not None:
            cur[f"gist:{g[:8]}"] = s

    if not os.path.exists(STATE_FILE):
        # first run: store baseline, announce watcher live
        with open(STATE_FILE, "w") as f:
            json.dump(cur, f, indent=1)
        print(f"Watcher live — baseline stored for {len(cur)} surfaces.")
        return

    with open(STATE_FILE) as f:
        prev = json.load(f)

    changed = False
    for k, v in cur.items():
        p = prev.get(k)
        if p is None:
            print(f"#{k}: NEW to watch — {v.get('state')} | {v.get('title', '')[:60]}")
            changed = True
            continue
        if p.get("updated_at") != v.get("updated_at") or p.get("comments") != v.get("comments") or p.get("state") != v.get("state"):
            print(f"#{k}: MOVED — {p.get('state')}@{p.get('updated_at')} -> {v.get('state')}@{v.get('updated_at')} (comments {p.get('comments')}->{v.get('comments')}) | {v.get('title', '')[:60]}")
            changed = True

    # atomic write (temp + rename) so a kill mid-write never corrupts the state
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(cur, f, indent=1)
    os.replace(tmp, STATE_FILE)

    if not changed:
        return  # silence — nothing to report


if __name__ == "__main__":
    main()
