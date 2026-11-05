"""Demand-age instrument (RFC #143379 INVENT lane). Deterministic sim.

The recitation demand's age distribution shifts with session length: early
cycles quote recent literals (in-window); long sessions quote older literals
(paths, SHAs, args referenced after many intervening observations). The
K-window retains the last K observations in text; the cut applies the
compression ratio's survival probability (latent floor: 20.4/15.6/15.1% at
4x/8x/16x) to older observations. K=0 baseline: no window, all-compressed.
"""
import random, hashlib, json, os, math

K = 10
# latent-path exact-recitation floor by ratio (LOHA/ACD, arXiv 2609.31430)
FLOOR = {2: 0.30, 3: 0.24, 4: 0.204, 5: 0.18, 6: 0.17, 7: 0.16, 8: 0.156,
         16: 0.151, 32: 0.14}


def token_stream(seed, n):
    rng = random.Random(seed)
    items = []
    for i in range(n):
        kind = rng.choice(["path", "sha", "arg"])
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


def demand_age(cycle_idx, rng):
    # Zipfian-with-long-session-stretch: quoted literal age grows with cycle.
    base = 1 + int((cycle_idx / 10.0) ** 1.3)
    return base


def cycle(seed, cycle_idx, ratio, k):
    rng = random.Random(seed * 1000 + cycle_idx)
    n = max(ratio + 1, cycle_idx)
    stream = token_stream(seed + cycle_idx, n)
    w = Window(k)
    assert w.buf == [], "window must be empty at cycle start"
    if k > 0:
        for t in stream[-k:]:
            w.push(t[1])
    # demand: quote literals whose age = demand_age (may exceed window)
    age = demand_age(cycle_idx, rng)
    idx = max(0, n - 1 - age)
    queries = [stream[idx][1]] if stream else []
    if not queries:
        queries = [stream[-1][1]]
    hits = 0
    total = len(queries)
    floor = FLOOR.get(ratio, 1.0 / ratio)
    if floor is None:
        floor = 1.0 / ratio
    if k == 0:
        # all-compressed: latent floor
        return floor
    snap = w.snapshot()
    for q in queries:
        if q in snap:
            hits += 1
        else:
            # latent path survival
            if rng.random() < float(floor):
                hits += 1
    return hits / total


def run_sweep():
    seeds = 25
    cycles = list(range(10, 301, 10)) + [320, 350, 400]
    ratios = [2, 4, 8, 16, 32]
    results = []
    for s in range(seeds):
        for c in cycles:
            for r in ratios:
                for k in [0, 10]:
                    sc = cycle(s, c, r, k)
                    results.append({"seed": s, "cycle": c, "ratio": r, "k": k, "score": sc})
    return results


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    res = run_sweep()
    import csv
    with open("results/sweep_age.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)
    from collections import defaultdict
    agg = defaultdict(lambda: defaultdict(list))
    for row in res:
        agg[(row["cycle"], row["ratio"], row["k"])].append(row["score"])
    out = {}
    for key, v in agg.items():
        for k, scores in v.items():
            out[f"{key[0]}_{key[1]}_k{key[2] if False else k}"] = sum(scores) / len(scores)
    with open("results/agg_age.json", "w") as f:
        json.dump({"n": len(res)}, f)
    print("done", len(res))
