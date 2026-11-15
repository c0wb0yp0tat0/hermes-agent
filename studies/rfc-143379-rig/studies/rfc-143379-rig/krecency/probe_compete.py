"""Competition arm of the demand-age instrument (RFC #143379).

Extends the demand-age cycle so the survivors' pool can contain RIVAL-COLLISIONS:
when an older literal is quoted from the latent/survivor path, a survivor that
shares the literal's format with a DIFFERENT value (a look-alike rival) competes
for the recitation; exact-recovery succeeds only if no rival is present or the
window/pinned copy carries the true literal.

Knobs: rival_rate in {0.0, 0.1, 0.3}, ratios + demand-age, k in {0,10}.
Attention-mass proxy a*: softmax weight of the true literal vs rivals in the
survivor pool, recorded per trial.
"""
import random, hashlib, json, os, math

K = 10
FLOOR = {2: 0.30, 3: 0.24, 4: 0.204, 5: 0.18, 6: 0.17, 7: 0.16, 8: 0.156,
         16: 0.151, 32: 0.14}

RIVAL_RATES = [0.0, 0.1, 0.3]


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
    base = 1 + int((cycle_idx / 10.0) ** 1.3)
    return base


def rival_value(kind, rng):
    # look-alike rival: same shape, different content
    if kind == "path":
        return f"/repo/src/mod{rng.randrange(9999)}/file_{rng.randrange(1000)}.py"
    elif kind == "sha":
        return hashlib.sha256(f"rival-{rng.randrange(10**9)}".encode()).hexdigest()[:12]
    else:
        return f"--flag={rng.randrange(9999)}"


def cycle(seed, cycle_idx, ratio, k, rival_rate=0.0):
    rng = random.Random(seed * 1000 + cycle_idx)
    n = max(ratio + 1, cycle_idx)
    stream = token_stream(seed + cycle_idx, n)
    w = Window(k)
    assert w.buf == [], "window must be empty at cycle start"
    if k > 0:
        for t in stream[-k:]:
            w.push(t[1])
    age = demand_age(cycle_idx, rng)
    idx = max(0, n - 1 - age)
    queries = [stream[idx][1]] if stream else []
    if not queries:
        queries = [stream[-1][1]]
    # determine kind of quoted literal
    qkind = stream[idx][0] if stream else "arg"
    floor = FLOOR.get(ratio, 1.0 / ratio)
    if floor is None:
        floor = 1.0 / ratio

    # rival injection into survivor pool
    rivals = []
    if rng.random() < rival_rate:
        rivals.append(rival_value(qkind, rng))
    # additional rivals scaled by rate (allow multiple)
    n_rivals = 0
    if rival_rate > 0:
        # expected rival count ~ rival_rate * 3
        n_rivals = int(round(rival_rate * 3))
        for _ in range(n_rivals):
            rivals.append(rival_value(qkind, rng))
    rivals = list(dict.fromkeys(rivals))

    # attention-mass proxy a*: softmax over survivor pool {true} + rivals
    # weight true literal vs rivals
    pool = [queries[0]] + rivals
    # assign base weights: true gets 1.0, rivals get 1.0 each (equal mass)
    weights = [1.0] + [1.0] * len(rivals)
    # apply softmax
    import math as _m
    mx = max(weights)
    exps = [_m.exp(wt - mx) for wt in weights]
    s = sum(exps)
    a_star = exps[0] / s if s > 0 else 1.0

    hits = 0
    total = len(queries)
    if k == 0:
        # all-compressed: latent floor, but rival collision can defeat recovery
        if rival_rate == 0.0 or not rivals:
            return floor, a_star
        # with rivals present, recovery probability reduced
        prob = floor * (1.0 - 0.5 * rival_rate)
        return prob, a_star
    snap = w.snapshot()
    for q in queries:
        if q in snap:
            hits += 1
        else:
            # latent path survival, defeated if rival present and not pinned
            p_surv = float(floor)
            if rivals:
                p_surv = p_surv * (1.0 - 0.3 * rival_rate)
            if rng.random() < p_surv:
                hits += 1
    # if rival present and true literal not in window, recovery fails outright sometimes
    if rivals and queries[0] not in snap:
        if rng.random() < rival_rate:
            hits = max(0, hits - 1)
    score = hits / total if total else 0.0
    return score, a_star


def run_sweep():
    seeds = 25
    cycles = list(range(10, 301, 10)) + [320, 350, 400]
    ratios = [2, 4, 8, 16, 32]
    results = []
    for s in range(seeds):
        for c in cycles:
            for r in ratios:
                for k in [0, 10]:
                    for rr in RIVAL_RATES:
                        sc, a = cycle(s, c, r, k, rr)
                        results.append({"seed": s, "cycle": c, "ratio": r, "k": k,
                                        "rival_rate": rr, "score": sc, "a_star": a})
    return results


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    res = run_sweep()
    import csv
    with open("results/compete.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)
    print("done", len(res))
