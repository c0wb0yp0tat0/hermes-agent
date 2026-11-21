#!/usr/bin/env python3
"""Fair-share envelope probe: staircase concurrency on the free-tier lagunas.

Measures how many concurrent `hermes chat` launches each model id sustains
before 429s, the retry-after cadence, and whether the two ids share a pool.
Bounded: ~14 trivial launches total, gentle staircase, gaps between batches.
"""
import subprocess, sys, time, json, re

MODELS = ["poolside/laguna-xs-2.1:free", "poolside/laguna-s-2.1:free"]
STEPS = [1, 2, 3, 4]          # concurrent launches per batch
GAP = 45                      # seconds between batches (let limits reset)
OUT = "/root/.hermes/cache/scratch/fair-share-probe.json"

def launch(model: str) -> dict:
    t0 = time.time()
    try:
        r = subprocess.run(
            ["hermes", "chat", "-q", "Reply with exactly: OK", "-m", model, "--reasoning", "low"],
            capture_output=True, text=True, timeout=90,
        )
        out = (r.stdout or "") + (r.stderr or "")
        dt = round(time.time() - t0, 1)
        if "429" in out:
            m = re.search(r"resets at (\d+:\d+)", out)
            return {"ok": False, "kind": "429", "retry_after": m.group(1) if m else None, "dt": dt}
        if "404" in out:
            return {"ok": False, "kind": "404", "dt": dt}
        if "OK" in out:
            return {"ok": True, "kind": "ok", "dt": dt}
        return {"ok": False, "kind": "other", "dt": dt, "snippet": out[-120:]}
    except subprocess.TimeoutExpired:
        return {"ok": False, "kind": "timeout", "dt": 90}

results = []
for model in MODELS:
    for n in STEPS:
        batch = []
        procs = []
        for _ in range(n):
            p = subprocess.Popen(
                ["hermes", "chat", "-q", "Reply with exactly: OK", "-m", model, "--reasoning", "low"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            procs.append(p)
        for p in procs:
            try:
                out, _ = p.communicate(timeout=90)
                dt = round(time.time() - p._start if hasattr(p, "_start") else 0, 1)
            except subprocess.TimeoutExpired:
                p.kill(); out = "timeout"; dt = 90
            if "429" in out:
                m = re.search(r"resets at (\d+:\d+)", out)
                batch.append({"ok": False, "kind": "429", "retry_after": m.group(1) if m else None, "dt": dt})
            elif "404" in out:
                batch.append({"ok": False, "kind": "404", "dt": dt})
            elif "OK" in out:
                batch.append({"ok": True, "kind": "ok", "dt": dt})
            else:
                batch.append({"ok": False, "kind": "other", "dt": dt, "snippet": out[-100:]})
        results.append({"model": model, "concurrency": n, "batch": batch})
        print(f"{model} x{n}: " + ", ".join(f"{b['kind']}({b.get('retry_after','-')},{b['dt']}s)" for b in batch), flush=True)
        time.sleep(GAP)

with open(OUT, "w") as f:
    json.dump(results, f, indent=2)
print("probe written:", OUT)
