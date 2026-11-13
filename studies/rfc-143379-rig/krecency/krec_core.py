"""krec_core.py — the krecency family-tree's shared machinery (E5, the simplify-arm).

The deterministic stream-generation, the K-window, the demand-age distribution, the
cycle-simulation, and the csv/json emitters — extracted ONCE so the arms carry only
their parameters, their experiments, and their verdicts. Derived-never-injected:
every knob is a parameter; the refactor changes NOTHING numerate.

Pre-baseline (2026-11-06, the sameness-gate's rows): sweep_age 8251, pin 201,
membership 201, compete 24751, competing 19801, sweep 14851, archive 14851,
scaling 78201, recite 801, alias 801, constraints 401, constraints.json 17.
Headline bars: pinning 0.15-vs-1.00, membership 0.15-vs-1.00, aliasing R2 0.65.
"""

import csv
import hashlib
import json
import os
import random
from collections import defaultdict

FLOOR = {2: 0.3, 3: 0.24, 4: 0.204, 5: 0.18, 6: 0.17, 7: 0.16, 8: 0.156, 16: 0.151, 32: 0.14}


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
    total = len(queries)
    floor = FLOOR.get(ratio, 1.0 / ratio)
    if k == 0:
        # all-compressed: latent floor
        return floor
    snap = w.snapshot()
    hits = 0
    for q in queries:
        if q in snap:
            hits += 1
        elif rng.random() < float(floor):
            hits += 1
    return hits / total


def write_csv(path, rows, fieldnames=None):
    """The shared csv-emitter (the family-tree's canonical output-shape)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames or list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def write_json(path, obj):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f)
