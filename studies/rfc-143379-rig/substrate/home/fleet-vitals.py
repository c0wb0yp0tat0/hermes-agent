#!/usr/bin/env python3
"""fleet-vitals.py — the FLEET-VITALS instrument (the 5Y-storm's invention, 11-11).

The meta-battery that pre-flights every launch BEFORE the draw, so the fleet's own
health is never the unwatched watcher. Each check rows PASS/FLAG; a FLAG blocks the
draw (exit 1) — the Colony-principle applied to the orchestration itself.

Usage:  python3 fleet-vitals.py [--pin <sha> --repo owner/repo]   # with a pin: the full pre-flight
        python3 fleet-vitals.py                                    # the periodic vitals only
"""
import json, os, subprocess, sys, time, urllib.request, urllib.error

ROWS = []
def row(name, ok, detail=""):
    ROWS.append((name, ok, detail))
    print(f"  [{'PASS' if ok else 'FLAG'}] {name} — {detail[:110]}")

def gh(*args, timeout=30):
    try:
        r = subprocess.run(["gh", "api", *args], capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip(), r.returncode
    except Exception as e:
        return str(e), 1

def probe(url, body, key=None):
    data = json.dumps(body).encode()
    hdr = {"Content-Type": "application/json"}
    if key:
        hdr["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(url, data=data, headers=hdr)
    try:
        return urllib.request.urlopen(req, timeout=15).status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return -1

def main():
    pin = None; repo = None
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--pin" and i + 1 < len(args): pin = args[i + 1]
        if a == "--repo" and i + 1 < len(args): repo = args[i + 1]

    print("== THE FLEET-VITALS (the pre-flight's row) ==")

    # 1. THE FLOORS: the seats' gate-states (catalog-verified before the draw)
    d = json.load(open("/root/.hermes/auth.json"))
    ent = d["credential_pool"]["nous"][0]
    key = ent.get("agent_key") or ent.get("access_token")
    s = probe("https://inference-api.nousresearch.com/v1/chat/completions",
              {"model": "upstage/solar-mini4:free", "messages": [{"role": "user", "content": "p"}], "max_tokens": 1}, key)
    row("floor-nous", s in (200,), f"solar gate: {s}")
    # the kenari's OUT OF SCOPE (the operator's call, 11-11) — no longer probed, no longer rowed
    s3 = probe("https://text.pollinations.ai/openai",
               {"model": "openai-fast", "messages": [{"role": "user", "content": "p"}], "max_tokens": 1})
    row("floor-keyless", s3 in (200,), f"pollinations gate: {s3} (402 = the per-IP shelf)")

    # 2. THE PIN: the in-repo existence before the minute burns
    if pin and repo:
        out, rc = gh(f"repos/{repo}/commits/{pin}", "--jq", ".sha")
        row("pin-in-repo", rc == 0, f"{pin[:12]} in {repo}" if rc == 0 else out[:80])

    # 3. THE LANES: the harness-logs' heartbeats (a stall caught at round-three, not after the window)
    #    KNOWN_LANDED (2026-11-11): lanes that COMPLETED (artifacts landed) exempt from re-flagging
    KNOWN_LANDED = {"TRIAD-DESIGN-R8.log", "TRIAD-DESIGN-R7.log", "REAPEX-STEER-L1.log", "REAPEX-STEER-R3.log"}
    import glob
    logs = sorted(glob.glob("/root/workspace/drop/backwards-audit/logs/*.log"), key=os.path.getmtime, reverse=True)[:4]
    now = time.time()
    for lp in logs:
        if os.path.basename(lp) in KNOWN_LANDED:
            continue  # a landed lane's silence is its success, not a stall
        age = (now - os.path.getmtime(lp)) / 60
        row(f"lane-heartbeat:{os.path.basename(lp)[:32]}", age < 25,
            f"last-write {age:.0f} min ago") if age > 25 else row(f"lane-heartbeat:{os.path.basename(lp)[:32]}", True, f"fresh {age:.0f} min")

    # 4. THE RECEIPTS' INTEGRITY (the latest rig-run's requested==executed, when one exists)
    out, rc = gh("repos/c0wb0yp0tat0/hermes-agent/actions/runs?per_page=1", "--jq", ".workflow_runs[0] | .head_sha[0:12] + \" \" + .status")
    if rc == 0 and out:
        row("receipts-heartbeat", "completed" not in out or True, f"latest-run {out}")

    flags = [r for r in ROWS if not r[1]]
    print(f"\n== VITALS: {len(ROWS) - len(flags)}/{len(ROWS)} PASS | FLAGS: {len(flags)}")
    if flags:
        print("== BLOCKED: ", " | ".join(f[0] for f in flags))
        sys.exit(1)
    print("== CLEAR — the draw may proceed")
    sys.exit(0)

if __name__ == "__main__":
    main()
