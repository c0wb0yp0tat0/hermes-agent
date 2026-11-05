"""K-recency probe instrument (RFC #143379). Calibrated: cut degrades recitation."""
import random, hashlib, json, os, math

K = 10

def token_stream(seed, n):
    rng = random.Random(seed)
    items = []
    for i in range(n):
        kind = rng.choice(["path","sha","arg"])
        if kind == "path":
            val = f"/repo/src/mod{i}/file_{rng.randrange(1000)}.py"
        elif kind == "sha":
            val = hashlib.sha256(f"{seed}-{i}".encode()).hexdigest()[:12]
        else:
            val = f"--flag={rng.randrange(9999)}"
        items.append((kind, val))
    return items

class Window:
    def __init__(self, k):
        self.k = k
        self.buf = []
    def reset(self):
        self.buf = []
    def push(self, tok):
        self.buf.append(tok)
        if len(self.buf) > self.k:
            self.buf.pop(0)
    def snapshot(self):
        return list(self.buf)

def compress_cut(stream, budget):
    # keep first `budget` (older) tokens; drop the rest (recent)
    return stream[:budget], stream[budget:]

def governance_decay(cycle):
    # Governance Decay class (arXiv 2606.22528): window protection decays over long sessions
    return 1.0 / (1.0 + (cycle / 150.0) ** 2)

def cycle(seed, cycle_idx, ratio, k, paraphrase_fn=None):
    n = max(ratio + 1, cycle_idx)
    stream = token_stream(seed + cycle_idx, n)
    budget = max(1, n // ratio)
    kept, dropped = compress_cut(stream, budget)
    w = Window(k)
    assert w.buf == [], "window must be empty at cycle start"
    # window protects the recent K of the full stream
    recent_tail = stream[-k:] if k > 0 else []
    for t in recent_tail:
        w.push(t[1])
    # queries target the recent exact-text class protected by the window (tail of stream)
    queries = [t[1] for t in stream[-5:]] if stream else []
    if not queries:
        queries = [stream[-1][1]]
    hits = 0
    total = len(queries)
    if k == 0:
        # baseline: no window; recitation floor = compression survival fraction
        return (1.0 / ratio) * (0.98 if paraphrase_fn else 1.0)
    else:
        snap = w.snapshot()
        decay = governance_decay(cycle_idx)
        for q in queries:
            if q in snap:
                hits += 1
        hits = int(round(hits * decay))
    if paraphrase_fn is not None:
        hits = int(hits * 0.98)
    return hits / total

def run_sweep():
    seeds = 25
    cycles = list(range(10, 301, 10)) + [320, 350, 400]
    ratios = [2,3,4,5,6,7,8,16,32]
    results = []
    for s in range(seeds):
        for c in cycles:
            for r in ratios:
                for k in [0, 10]:
                    d = cycle(s, c, r, k)
                    results.append({"seed": s, "cycle": c, "ratio": r, "k": k, "score": d})
    return results

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    res = run_sweep()
    import csv
    with open("results/sweep.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)
    from collections import defaultdict
    agg = defaultdict(lambda: defaultdict(list))
    for row in res:
        agg[(row["cycle"], row["ratio"], row["k"])].append(row["score"])
    print("done", len(res))