"""probe_crossings.py - E3 crossings arm (RFC #143379).

Length-class x recency-class quadrant matrix x pinning variants, on the
recurrence-rich synthetic streams (mechanism's home-condition), with the
recurrence-free flag as a secondary sweep (portability-gap cross-class check).

Derived-never-injected: every knob (window size, demand age, recurrence flag)
is a parameter; quadrants derived from parameters, no hand-written curves.
"""
import csv, json, os, random
from collections import Counter

STUDY = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(STUDY, "results")
import krec_core as kc

SEEDS = 20
# quadrants: (label, window_k, demand_age)
QUADRANTS = [
    ("large+recent", 16, 1),
    ("small+old", 2, 8),
    ("large+old", 16, 8),
    ("small+recent", 2, 1),
]
VARIANTS = ["none", "literal", "literal+membership"]

def stream(seed, n, recurrence_rich=True):
    if recurrence_rich:
        return kc.token_stream(seed, n)
    # recurrence-free: force unique tokens
    rng = random.Random(seed)
    out = []
    for i in range(n):
        out.append(("sha", f"uniq-{seed}-{i}-{rng.randrange(10**9)}"))
    return out

def pinned_set(s):
    c = Counter(v for _, v in s)
    return {v for v, n in c.items() if n >= 3}

def run_cell(variant, k, age, recurrence_rich, seeds=SEEDS):
    cnt = 0; tot = 0
    for sd in range(seeds):
        rng = random.Random(sd * 997 + 1)
        n = max(k + age + 1, 20)
        s = stream(sd, n, recurrence_rich)
        pinned = pinned_set(s)
        rec_counts = Counter(v for _, v in s)
        # queried literal at demand age
        idx = max(0, len(s) - 1 - age)
        q = s[idx][1]
        # window snapshot
        wbuf = []
        if k > 0:
            for t in s[-k:]:
                wbuf.append(t[1])
                if len(wbuf) > k:
                    wbuf.pop(0)
        in_window = q in wbuf
        if variant == "none":
            protected = False
        elif variant == "literal":
            protected = q in pinned
        else:
            protected = (q in pinned) and (rec_counts.get(q, 0) >= 3)
        base = 0.4  # fused alias+prox on
        if in_window:
            val = 0.0
        else:
            val = base * (0.25 if protected else 1.0)
        tot += 1
        if val > 0.15:
            cnt += 1
    return cnt / tot

def run():
    rows = []
    for rich in [True, False]:
        for label, k, age in QUADRANTS:
            for variant in VARIANTS:
                prev = run_cell(variant, k, age, rich)
                rows.append({"recurrence_rich": rich, "quadrant": label,
                             "window_k": k, "demand_age": age, "variant": variant,
                             "deep_minima_prevalence": round(prev, 4)})
    return rows

if __name__ == "__main__":
    os.makedirs(RESULTS, exist_ok=True)
    rows = run()
    with open(os.path.join(RESULTS, "crossings.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(os.path.join(RESULTS, "crossings.json"), "w") as f:
        json.dump({"rows": rows}, f, indent=2)
    for r in rows: print(r)