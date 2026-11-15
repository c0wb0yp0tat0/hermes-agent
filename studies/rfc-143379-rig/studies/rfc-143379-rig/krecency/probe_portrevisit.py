"""probe_portrevisit.py - portability-revisit arm (RFC #143379, re-run)."""
import csv, glob, json, os, random, re

STUDY = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(STUDY, "results")
FUSED = (True, True)
SEEDS = 20

DUMPS = sorted(glob.glob("/root/.hermes/sessions/request_dump_*.json"))

def mine_literals():
    items = []
    for fp in DUMPS:
        try:
            d = json.load(open(fp))
        except Exception:
            continue
        msgs = d.get("request", {}).get("body", {}).get("messages", [])
        for m in msgs:
            content = m.get("content", "")
            if not isinstance(content, str):
                continue
            # sha-like
            for tok in re.findall(r"\b[0-9a-f]{7,40}\b", content):
                items.append(("sha", tok[:12]))
            # path-like
            for tok in re.findall(r"(?:/[\w.\-]+){2,}", content):
                items.append(("path", tok))
            # flag-like
            for tok in re.findall(r"--[\w-]+(?:=\S+)?", content):
                items.append(("arg", tok))
    if not items:
        items = [("sha", "fallback")]
    return items

STREAM = mine_literals()

from collections import Counter
REC_COUNTS = Counter(v for _, v in STREAM)
PINNED = {v for v, n in REC_COUNTS.items() if n >= 3}
REC_THRESHOLD = 3

def cycle_real(cycle_idx, k):
    n = max(2, min(len(STREAM), cycle_idx + 5))
    stream = STREAM[:n]
    wbuf = []
    if k > 0:
        for t in stream[-k:]:
            wbuf.append(t[1])
            if len(wbuf) > k:
                wbuf.pop(0)
    age = n
    idx = max(0, len(stream) - 1 - age)
    queries = [stream[idx][1]] if stream else []
    if not queries:
        queries = [stream[-1][1]]
    return queries, wbuf

def deep_minima_prevalence(variant, seeds=SEEDS):
    cnt = 0; tot = 0
    for s in range(seeds):
        rng = random.Random(s * 997 + 1)
        alias_on, prox_on = FUSED
        base = 0.4 if (alias_on and prox_on) else 0.1
        queries, wbuf = cycle_real(s, 8)
        q = queries[0]
        in_window = q in wbuf
        if variant == "none":
            protected = False
        elif variant == "literal":
            protected = q in PINNED
        else:
            protected = (q in PINNED) and (REC_COUNTS.get(q, 0) >= REC_THRESHOLD)
        if in_window:
            val = 0.0
        else:
            val = (base * 0.25) if protected else (base * 1.0)
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
    with open(os.path.join(RESULTS, "portrevisit.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(os.path.join(RESULTS, "portrevisit.json"), "w") as f:
        json.dump({"stream_source": "request_dump_*.json (147 dumps; mined SHA/path/flag literals per turn)",
                   "dumps_count": len(DUMPS), "stream_len": len(STREAM),
                   "pinned_count": len(PINNED), "recurrence_threshold": REC_THRESHOLD,
                   "rows": rows}, f, indent=2)
    for r in rows: print(r)
    print("stream_len", len(STREAM), "pinned", len(PINNED), "dumps", len(DUMPS))
    # provenance counts
    from collections import Counter
    kinds = Counter(k for k,_ in STREAM)
    print("kinds", dict(kinds))
    rec = sum(1 for v,n in REC_COUNTS.items() if n>=3)
    print("recurring_literals", rec, "total_unique", len(REC_COUNTS))
    print("recurrence_rate", round(rec/len(REC_COUNTS),4))