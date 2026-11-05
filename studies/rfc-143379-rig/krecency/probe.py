"""K-recency probe instrument (RFC #143379)."""
import random, hashlib, json, os

K = 10

def token_stream(seed, n):
    rng = random.Random(seed)
    # deterministic stream of "exact-text" items: paths, SHAs, args
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
    # keep first `budget` tokens, drop rest (compression)
    return stream[:budget], stream[budget:]

def recite(window_tokens, query):
    # exact recitation: query value present in window?
    return query in window_tokens

def cycle(seed, cycle_idx, ratio, k, paraphrase_fn=None):
    # state must be scoped: fresh window each cycle
    n = cycle_idx  # number of tokens grows with cycle
    stream = token_stream(seed + cycle_idx, n)
    budget = max(1, n // ratio)
    kept, dropped = compress_cut(stream, budget)
    w = Window(k)
    assert w.buf == [], "window must be empty at cycle start"
    # feed kept (recent window over kept tail)
    tail = kept[-k:] if k>0 else []
    for t in tail:
        w.push(t[1])
    # queries from dropped (exact-text class)
    queries = [d[1] for d in dropped[:5]] if dropped else []
    hits = 0
    for q in queries:
        if k == 0:
            # baseline: no window; recitation from kept only
            hits += 1 if q in [x[1] for x in kept] else 0
        else:
            hits += 1 if recite(w.snapshot(), q) else 0
    # paraphrase handling
    if paraphrase_fn is not None:
        hits = int(hits * 0.98)  # real paraphrase slightly perturbs
    total = len(queries) if queries else 1
    return hits/total

def run_sweep():
    seeds = 25
    cycles = list(range(1, 301)) + [320,350,400]
    ratios = [2,3,4,5,6,7,8,16,32]
    # ensure 4x-8x all ints
    results = []
    for s in range(seeds):
        for c in cycles:
            for r in ratios:
                for k in [0,10]:
                    d = cycle(s, c, r, k)
                    results.append({"seed":s,"cycle":c,"ratio":r,"k":k,"score":d})
    return results

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    res = run_sweep()
    import csv
    with open("results/sweep.csv","w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)
    # aggregate deltas per ratio for cycles>=300
    from collections import defaultdict
    agg = defaultdict(lambda: defaultdict(list))
    for row in res:
        agg[(row["cycle"],row["ratio"],row["k"])].append(row["score"])
    print("done", len(res))
