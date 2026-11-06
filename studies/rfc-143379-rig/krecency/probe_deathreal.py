"""probe_deathreal.py - death-cell-real arm: small+old death-cell on real streams."""
import csv, glob, json, os, random, re

STUDY = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(STUDY, "results")
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
            for tok in re.findall(r"\b[0-9a-f]{7,40}\b", content):
                items.append(("sha", tok[:12]))
            for tok in re.findall(r"(?:/[\w.\-]+){2,}", content):
                items.append(("path", tok))
            for tok in re.findall(r"--[\w-]+(?:=\S+)?", content):
                items.append(("arg", tok))
    if not items:
        items = [("sha", "fallback")]
    return items

STREAM = mine_literals()

from collections import Counter
REC_COUNTS = Counter(v for _, v in STREAM)
PINNED = {v for v, n in REC_COUNTS.items() if n >= 3}
RESERVED = {v for v in REC_COUNTS if len(v) <= 3}
RESERVED_SIZE = len(RESERVED)

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
        queries, wbuf = cycle_real(s, 8)
        q = queries[0]
        in_window = q in wbuf
        small = len(q) <= 3
        old = not in_window
        if not (small and old):
            continue
        if variant == "none":
            protected = False
        elif variant == "literal-pin":
            protected = q in PINNED
        else:
            protected = (q in PINNED) or (q in RESERVED)
        base = 0.4
        val = (base * 0.25) if protected else (base * 1.0)
        tot += 1
        if val > 0.15:
            cnt += 1
    if tot == 0:
        return 0.0
    return cnt / tot

def run():
    rows = []
    for variant in ["none", "literal-pin", "pin+retention-latch"]:
        prev = deep_minima_prevalence(variant)
        rows.append({"variant": variant,
                     "deep_minima_prevalence": round(prev, 4),
                     "reserved_set_size": RESERVED_SIZE})
    return rows

if __name__ == "__main__":
    os.makedirs(RESULTS, exist_ok=True)
    rows = run()
    with open(os.path.join(RESULTS, "deathreal.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(os.path.join(RESULTS, "deathreal.json"), "w") as f:
        json.dump({"stream_source": "request_dump_*.json (mined SHA/path/flag literals)",
                   "dumps_count": len(DUMPS), "stream_len": len(STREAM),
                   "pinned_count": len(PINNED), "reserved_set_size": RESERVED_SIZE,
                   "rows": rows}, f, indent=2)
    for r in rows: print(r)
    print("stream_len", len(STREAM), "pinned", len(PINNED), "dumps", len(DUMPS), "reserved", RESERVED_SIZE)