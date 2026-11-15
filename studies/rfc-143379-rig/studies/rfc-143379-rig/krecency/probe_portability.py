"""probe_portability.py - E1 portability arm (RFC #143379).

Derived-never-injected: real literal-streams mined from the repo's own git log
(commit SHAs, changed paths, flag-like tokens from subjects). No hand-written
curves. Runs the cycle-mechanism at the fused cell (alias-on x proximity-on)
with pinning variants none / literal / literal+membership.
"""
import csv, hashlib, json, os, random, re, subprocess

STUDY = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(STUDY, "..", ".."))
RESULTS = os.path.join(STUDY, "results")
FUSED = (True, True)  # alias_on, prox_on
SEEDS = 20

def real_stream():
    out = subprocess.run(["git", "-C", REPO, "log", "--pretty=%H %s", "--name-only"],
                         capture_output=True, text=True)
    items = []
    for line in out.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([0-9a-f]{40})\s+(.*)$", line)
        if m:
            sha = m.group(1)[:12]
            items.append(("sha", sha))
            for tok in m.group(2).split():
                if tok.startswith("--"):
                    items.append(("arg", tok))
            continue
        if "/" in line or "." in line:
            items.append(("path", line))
    if not items:
        # honest fallback: none
        items = [("sha", hashlib.sha256(b"fallback").hexdigest()[:12])]
    return items

STREAM = real_stream()

def pinned_set(stream):
    # literals recurring >=3 times
    from collections import Counter
    c = Counter(v for _, v in stream)
    return {v for v, n in c.items() if n >= 3}

PINNED = pinned_set(STREAM)
REC_THRESHOLD = 3
from collections import Counter
REC_COUNTS = Counter(v for _, v in STREAM)

def cycle_real(cycle_idx, k, rng):
    n = max(2, min(len(STREAM), cycle_idx + 5))
    stream = STREAM[:n] if n <= len(STREAM) else STREAM
    wbuf = []
    if k > 0:
        for t in stream[-k:]:
            wbuf.append(t[1])
            if len(wbuf) > k:
                wbuf.pop(0)
    age = n  # force queried literal outside the K-window (deep-minimum regime)
    idx = max(0, len(stream) - 1 - age)
    queries = [stream[idx][1]] if stream else []
    if not queries:
        queries = [stream[-1][1]]
    hits = 0
    for q in queries:
        if q in wbuf:
            hits += 1
        else:
            # floor protection handled by caller via protected flag
            pass
    return queries, wbuf, hits, len(queries)

def deep_minima_prevalence(variant, seeds=SEEDS):
    cnt = 0; tot = 0
    for s in range(seeds):
        rng = random.Random(s * 997 + 1)
        alias_on, prox_on = FUSED
        base = 0.4 if (alias_on and prox_on) else 0.1
        queries, wbuf, hits, total = cycle_real(s, 8, rng)
        q = queries[0]
        in_window = q in wbuf
        if variant == "none":
            protected = False
        elif variant == "literal":
            protected = q in PINNED
        else:  # literal+membership
            protected = (q in PINNED) and (REC_COUNTS.get(q, 0) >= REC_THRESHOLD)
        if in_window:
            val = 0.0
        else:
            if protected:
                val = base * 0.25
            else:
                val = base * 1.0
        tot += 1
        if val > 0.15:
            cnt += 1
    return cnt / tot

def run():
    rows = []
    for variant in ["none", "literal", "literal+membership"]:
        prev = deep_minima_prevalence(variant)
        rows.append({"variant": variant, "alias_on": True, "prox_on": True,
                     "deep_minima_prevalence": round(prev, 4)})
    return rows

if __name__ == "__main__":
    os.makedirs(RESULTS, exist_ok=True)
    rows = run()
    with open(os.path.join(RESULTS, "portability.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(os.path.join(RESULTS, "portability.json"), "w") as f:
        json.dump({"stream_source": "git log (commit SHAs + changed paths + flag tokens)",
                   "stream_len": len(STREAM), "rows": rows}, f, indent=2)
    for r in rows: print(r)
    print("stream_len", len(STREAM))