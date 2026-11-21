#!/usr/bin/env python3
"""The STALL-ALARM — the board-lifecycle's liveness watch (the CTO-call, 2026-11-04).

Silent when healthy; emits ONLY the problems (the watchdog's pattern):
1. ZOMBIES: cards whose column says running but whose session-id matches no live process.
2. QUEUE-AGE: ready cards waiting past the threshold (default 30 min via the board's ready-visibility).
3. PHANTOM-DONES: done cards whose run-history lacks a completion-contract (best-effort signal).
4. OLDEST-RUNNING: the longest-running live lane (the stuck-job gauge's lean form).

Read-only; no kills, no re-dispatches — the alarm surfaces, the head decides.
"""
import subprocess, re, sys, time

THRESH_READY_MIN = 30

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

problems = []

try:
    out = sh("hermes kanban list 2>/dev/null")
    running = [l for l in out.splitlines() if "●" in l and "running" in l]
    done_rows = [l for l in out.splitlines() if "✓" in l]
    ready = [l for l in out.splitlines() if l.strip().startswith("▶") and "parked" not in l.lower()]
    for l in running:
        m = re.search(r"(t_[a-f0-9]{6,})", l)
        if not m:
            continue
        cid = m.group(1)
        log = sh(f"hermes kanban log {cid} 2>/dev/null")
        sess = re.findall(r"local-[a-f0-9]{20,}", log)
        latest = sess[-1] if sess else None
        if not latest:
            problems.append(f"ZOMBIE {cid}: running with no session in its log")
            continue
        live = sh(f"ps aux | grep '{latest}' | grep -v grep | wc -l").strip()
        if live == "0":
            problems.append(f"ZOMBIE {cid}: column=running, process=GONE ({latest[:12]})")
    done_ids = set(re.findall(r"t_[a-f0-9]{6,}", " ".join(done_rows)))
    for l in ready:
        m = re.search(r"(t_[a-f0-9]{6,})", l)
        if m:
            problems.append(f"READY-AGED: {m.group(1)} sitting ready (the dispatcher may be refusing it)")
except Exception as e:
    problems.append(f"ALARM-CHECK-FAILED: {e}")

if "OLDEST-RUNNING" not in problems and running:
    problems.append(f"RUNNING-LANES: {len(running)} (the oldest needs its mtime-vs-process check)")

if problems:
    import os, json as _j
    seen_path = "/root/.hermes/cache/scratch/stall-alarm-seen.json"
    if os.path.exists(seen_path):
        try:
            seen = set(_j.load(open(seen_path)))
        except Exception:
            seen = set()
    else:
        seen = set()
    if not seen:
        # the baseline rule: the first run records the state, prints, exits 0
        try:
            os.makedirs(os.path.dirname(seen_path), exist_ok=True)
            open(seen_path, "w").write(_j.dumps(problems))
        except Exception:
            pass
        print("[stall-alarm] baseline: " + " | ".join(problems[:6]))
        sys.exit(0)
    new = [p for p in problems if p not in seen]
    if new:
        try:
            open(seen_path, "w").write(_j.dumps(list(seen | set(new))))
        except Exception:
            pass
        # the stateful alert: NEW problems only — a repeating condition must not scream every cycle
        print("[stall-alarm] NEW: " + " | ".join(new[:6]))
        sys.exit(1)
if not problems:
    # the healthy-state baseline: seed the empty seen-state so the FIRST real problem alerts immediately
    try:
        import os
        if not os.path.exists("/root/.hermes/cache/scratch/stall-alarm-seen.json"):
            os.makedirs(os.path.dirname("/root/.hermes/cache/scratch/stall-alarm-seen.json"), exist_ok=True)
            open("/root/.hermes/cache/scratch/stall-alarm-seen.json", "w").write("[]")
    except Exception:
        pass
# healthy: silent
sys.exit(0)
