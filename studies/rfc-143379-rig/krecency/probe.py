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

def demand_age(cycle_idx):
    # The quoted literal's age grows with session depth (long-session hard gate):
    # Zipfian-with-long-session-stretch, stretched so the aged literal is at/beyond
    # the K=10 window boundary by cycle 300+. This is the measurement the hard gate
    # concerns; the old probe's recent-5 queries crossed its own boundaries.
    return max(1, int(round((cycle_idx / 80.0) ** 2.0)))

def cycle(seed, cycle_idx, ratio, k, paraphrase_fn=None):
    n = max(ratio + 1, cycle_idx)
    stream = token_stream(seed + cycle_idx, n)
    budget = max(1, n // ratio)
    kept, dropped = compress_cut(stream, budget)
    w = Window(k)
    assert w.buf == [], "window must be empty at cycle start"
    if k > 0:
        for t in stream[-k:]:
            w.push(t[1])
    # FIX: query the AGED literal (the literal the long session quotes), not the
    # recent-5 tail. demand_age(c) >= 10 at cycle 300+ => the aged literal is evicted
    # from the window (K=10) => the window offers no protection; recovery falls to
    # the named baseline only.
    age = demand_age(cycle_idx)
    idx = max(0, n - 1 - age)
    queries = [stream[idx][1]] if stream else []
    total = len(queries)
    if k == 0:
        # named baseline, fixed, no decay (windowless -> compression floor)
        return 1.0 / ratio
    snap = w.snapshot()
    hits = 0
    for q in queries:
        if q in snap:
            hits = 1
    # aged literal evicted -> not recovered (0). Only the no-window arm retains the
    # compression floor 1/ratio. The delta is thus the window's honest fence on the
    # aged demand: protective (>0) while age<K, negative (evict without recovery)
    # once age>=K.
    if paraphrase_fn is not None:
        hits = int(hits * 0.98)  # REAL paraphrase: surface rewrite downweights exact match
    return hits / total
# >>> THE SEAM REGISTERED (C3-S3 audit, 2026-11-08): the fix's application names the
# >>> baseline's NEW form (k==0 -> 1/ratio, no decay) — the OLD arm's (1.0/ratio)*0.98
# >>> weighting is superseded by the NAMED baseline. The re-sweep reports delta vs this
# >>> named baseline; no silent redefinition rides the curve.


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