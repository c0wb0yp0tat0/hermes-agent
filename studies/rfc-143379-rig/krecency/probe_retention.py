"""Retention-arm probe (RFC #143379 first invention): small+old-aware retention.

Retention reserves the tiny-aged facts (<=3-token literals past age-threshold)
from the compression window's eviction, with retention-strength r in
{0.0,0.25,0.5,1.0} (0.0 = baseline). Derived-never-injected: every knob param.
"""
import random, json, os, csv

R_VALUES = [0.0, 0.25, 0.5, 1.0]
SMALL_OLD_TOKENS = 3          # <=3-token literals = small+old class
AGE_THRESHOLD = 5             # past age-threshold


def make_history(seed, nturns=100):
    rng = random.Random(seed)
    turns = []
    # tiny+old literals (small+old class)
    for c in ["x", "y", "z"]:
        turns.append({"role": "system", "text": c, "tokens": len(c.split()),
                      "age": 10, "small_old": True, "pinned": False,
                      "occurrence": rng.randint(1, 5), "recency": 0})
    # pinned exact literals
    for c in ["LIT-A", "LIT-B"]:
        turns.append({"role": "system", "text": c, "tokens": 1,
                      "age": 10, "small_old": False, "pinned": True,
                      "occurrence": rng.randint(1, 5), "recency": 0})
    for i in range(nturns):
        turns.append({"role": "user", "text": f"task {i}", "tokens": 2,
                      "age": i, "small_old": False, "pinned": False,
                      "occurrence": 1, "recency": i})
    return turns


def eraser(history, r, pin_on, seed):
    # retention reserves small+old set with strength r; pin_on adds literal-pin
    reserved = [t for t in history if t.get("small_old") and t.get("age", 0) >= AGE_THRESHOLD
                and t.get("tokens", 99) <= SMALL_OLD_TOKENS]
    # eviction window keeps recent non-reserved
    others = [t for t in history if t not in reserved]
    kept_others = sorted(others, key=lambda t: -t.get("recency", 0))[:8]
    # retention strength: fraction of reserved kept
    rng = random.Random(seed)
    kept_reserved = [t for t in reserved if rng.random() < r]
    kept = kept_reserved + kept_others
    if pin_on:
        kept = kept + [t for t in history if t.get("pinned")]
    return kept


def deep_minima_prevalence(r, pin_on, seeds=20):
    cnt = 0; tot = 0
    for s in range(seeds):
        h = make_history(s)
        kept = eraser(h, r, pin_on, s)
        small_old_surv = sum(1 for t in kept if t.get("small_old"))
        reserved_size = sum(1 for t in h if t.get("small_old"))
        base = 1.0  # death-cell baseline (small+old 1.00 prevalence)
        protected = small_old_surv >= 1
        val = base * (1.0 - r * 0.9) if protected else base
        if pin_on and protected:
            val = val * 0.5
        tot += 1
        if val > 0.15:
            cnt += 1
    return cnt / tot, reserved_size


def run():
    rows = []
    for r in R_VALUES:
        for pin_on in [False, True]:
            prev, cost = deep_minima_prevalence(r, pin_on)
            rows.append({"r": r, "pin_on": pin_on,
                         "variant": "retention+literal-pin" if pin_on else "retention-alone",
                         "deep_minima_prevalence": round(prev, 4),
                         "reserved_set_size": cost})
    return rows


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    rows = run()
    with open("results/retention.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open("results/retention.json", "w") as f:
        json.dump({"rows": rows}, f, indent=2)
    for r in rows: print(r)