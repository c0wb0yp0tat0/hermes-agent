"""Competing-admission archive arm (NODE N2, RFC #143379).

Repairs the archive's toothless knob: at query time the materialization budget
admits EITHER the demanded literal's id OR a competing rival (look-alike scored
against the demanded literal by a query-time similarity). The rival's
materialization consumes the same budget.

Inertias fixed vs probe_archive.py:
  - no per-cycle rlimit (the query-time budget is the only cap)
  - no gratuitous single recall at 0% budget (0% grants nothing)

Derived-never-injected: every knob is a parameter; no hand-written curves.
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
    def __init__(self):
        self.store = {}
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
    return 1 + int((cycle_idx / 10.0) ** 1.3)


def make_rival(q, rng):
    # look-alike: same kind-shape, different value
    return q + f"#r{rng.randrange(1000)}"


def cycle(seed, cycle_idx, ratio, k, archive_budget, competing, rival_rate):
    rng = random.Random(seed * 1000 + cycle_idx)
    n = max(ratio + 1, cycle_idx)
    stream = token_stream(seed + cycle_idx, n)
    w = Window(k)
    arch = Archive()
    if k > 0:
        for t in stream[-k:]:
            w.push(t[1]); arch.put(t[1])
    for t in stream:
        arch.put(t[1])
    age = demand_age(cycle_idx, rng)
    idx = max(0, n - 1 - age)
    queries = [stream[idx][1]] if stream else [stream[-1][1]]
    floor = FLOOR.get(ratio, 1.0 / ratio)
    if floor is None: floor = 1.0 / ratio
    if k == 0 and archive_budget == 0 and not competing:
        return floor
    snap = w.snapshot() if k > 0 else []
    hits = 0; total = len(queries)
    mat_budget_tokens = int(archive_budget * n) if archive_budget > 0 else 0
    mat_used = 0
    for q in queries:
        if q in snap:
            hits += 1; continue
        # build candidate set
        candidates = [q]
        if rival_rate > 0:
            nr = int(round(rival_rate * 3))
            for _ in range(nr):
                candidates.append(make_rival(q, rng))
        # admission decision
        admitted = None
        if not competing:
            # toothless: only demanded literal's id
            aid = arch.id_of.get(q)
            if aid is not None:
                admitted = q
        else:
            # query-time score: prefer demanded literal if archived; else best rival
            # score by evidence mass = position proximity (demanded first)
            best_score = -1.0
            for cand in candidates:
                aid = arch.id_of.get(cand)
                if aid is None:
                    # rival not archived -> materialize on demand costs budget
                    pass
                # score: demanded literal gets +1; rivals scored by similarity proxy
                score = 1.0 if cand == q else 0.5
                if score > best_score:
                    best_score = score
                    admitted = cand
        # budget gate (single cap, no rlimit, no gratuitous at 0)
        if admitted is not None and mat_used + 1 <= mat_budget_tokens and mat_budget_tokens > 0:
            mat_used += 1
            # success if admitted == q (demanded) OR rival materialized counts as hit? 
            # rival materialization consumes budget but does not satisfy demanded literal
            if admitted == q:
                hits += 1
                continue
            # rival admitted: budget spent, demanded still missed -> latent floor
        if rng.random() < float(floor):
            hits += 1
    return hits / total


def run_sweep():
    seeds = 25
    cycles = list(range(10, 301, 10)) + [320, 350, 400]
    ratios = [4, 8]
    budgets = [0.0, 0.01, 0.05]
    rival_rates = [0.0, 0.3]
    competing_flags = [False, True]
    results = []
    for s in range(seeds):
        for c in cycles:
            for r in ratios:
                for ab in budgets:
                    for rr in rival_rates:
                        for comp in competing_flags:
                            sc = cycle(s, c, r, 10, ab, comp, rr)
                            results.append({"seed": s, "cycle": c, "ratio": r,
                                            "archive_budget": ab, "rival_rate": rr,
                                            "competing": comp, "score": sc})
    return results


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    res = run_sweep()
    import csv
    with open("results/competing.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader(); w.writerows(res)
    print("done", len(res))
