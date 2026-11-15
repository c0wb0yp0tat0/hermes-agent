"""Archive-arm instrument (RFC #143379). Demand-age cycle + ARC-style addressable recall.

Append-only store preserves exact literals under stable ids; per-cycle recall
limit r (default 2) + materialized-recall budget (fraction of session tokens).
Latent floor applies ONLY to literals neither in window NOR recalled.
"""
import random, hashlib, os, json, math

K = 10
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
        self.k = k; self.buf = []
    def reset(self): self.buf = []
    def push(self, tok):
        self.buf.append(tok)
        if len(self.buf) > self.k: self.buf.pop(0)
    def snapshot(self): return list(self.buf)


class Archive:
    """Append-only store; stable id per literal."""
    def __init__(self):
        self.store = {}  # id -> literal
        self.id_of = {}
    def put(self, lit):
        if lit not in self.id_of:
            aid = f"arc-{len(self.store):06d}"
            self.id_of[lit] = aid
            self.store[aid] = lit
        return self.id_of[lit]
    def get(self, aid):
        return self.store.get(aid)
    def ids(self): return list(self.store.keys())


def demand_age(cycle_idx, rng):
    base = 1 + int((cycle_idx / 10.0) ** 1.3)
    return base


def cycle(seed, cycle_idx, ratio, k, archive_budget, rlimit):
    rng = random.Random(seed * 1000 + cycle_idx)
    n = max(ratio + 1, cycle_idx)
    stream = token_stream(seed + cycle_idx, n)
    w = Window(k)
    arch = Archive()
    if k > 0:
        for t in stream[-k:]:
            w.push(t[1])
            arch.put(t[1])
    # materialize archive ids for all observed literals (append-only)
    for t in stream:
        arch.put(t[1])
    age = demand_age(cycle_idx, rng)
    idx = max(0, n - 1 - age)
    queries = [stream[idx][1]] if stream else []
    if not queries:
        queries = [stream[-1][1]]
    floor = FLOOR.get(ratio, 1.0 / ratio)
    if floor is None: floor = 1.0 / ratio
    # k=0 baseline = hard window (no archive) uses latent floor for all
    if k == 0 and archive_budget == 0:
        return floor
    snap = w.snapshot() if k > 0 else []
    hits = 0; total = len(queries)
    recalled = 0
    mat_budget_tokens = int(archive_budget * n) if archive_budget > 0 else 0
    mat_used = 0
    for q in queries:
        if q in snap:
            hits += 1; continue
        # try archive recall
        aid = arch.id_of.get(q)
        if aid is not None and recalled < rlimit and mat_used + 1 <= max(1, mat_budget_tokens):
            recalled += 1; mat_used += 1
            hits += 1; continue
        # latent floor
        if rng.random() < float(floor):
            hits += 1
    return hits / total


def run_sweep():
    seeds = 25
    cycles = list(range(10, 301, 10)) + [320, 350, 400]
    ratios = [4, 8]  # 4x-8x focus per gate
    budgets = [0.0, 0.01, 0.05]
    rlimits = [1, 2, 4]
    results = []
    for s in range(seeds):
        for c in cycles:
            for r in ratios:
                for ab in budgets:
                    for rl in rlimits:
                        sc = cycle(s, c, r, 10, ab, rl)
                        results.append({"seed": s, "cycle": c, "ratio": r,
                                        "archive_budget": ab, "rlimit": rl, "score": sc})
    return results


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    res = run_sweep()
    import csv
    with open("results/archive.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader(); w.writerows(res)
    print("done", len(res))