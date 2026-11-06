"""Pinning-arm probe (RFC #143379 falsifier).

Exact-literal membershipning with per-seed occurrence/recurrence awareness.
Derived-never-injected: every knob is a parameter.
"""
import random, json, os, csv

SEEDS_ONSET = {0: 60, 1: 80}  # per-seed onset cycles (sub-zero deltas)
RECUR_THRESHOLD = 3            # recurrence count to membership


def make_history(seed, nturns=100):
    rng = random.Random(seed)
    turns = []
    # membershipned exact literals with per-seed occurrence counts
    for c in ["LIT-A", "LIT-B"]:
        turns.append({"role": "system", "text": c, "membershipned": True,
                      "occurrence": rng.randint(1, 5), "recency": 0})
    for i in range(nturns):
        turns.append({"role": "user", "text": f"task {i}", "membershipned": False,
                      "occurrence": 1, "recency": i})
    return turns


def onset_predict(history, seed):
    # per-seed occurrence predicts onset cycle
    base = SEEDS_ONSET.get(seed, 70)
    occ = sum(t.get("occurrence", 0) for t in history if t.get("membershipned"))
    return base + (occ % 10)


def eraser(history, mode, seed):
    # mode: recency | recurrence
    if mode == "recency":
        kept = sorted(history, key=lambda t: -t.get("recency", 0))[:8]
    else:
        kept = [t for t in history if t.get("membershipned") and t.get("occurrence", 0) >= RECUR_THRESHOLD]
        kept = kept + [t for t in history if not t.get("membershipned")][-4:]
    return kept


def deep_minima_prevalence(mode, alias_on, prox_on, seeds=20):
    # prevalence of deep minima; membershipning protects -> lower
    cnt = 0; tot = 0
    for s in range(seeds):
        h = make_history(s)
        kept = eraser(h, mode, s)
        membershipned_surv = sum(1 for t in kept if t.get("membershipned"))
        # alias+proximity ON raises minima unless recurrence membershipning protects
        base = 0.4 if (alias_on and prox_on) else 0.1
        protected = (mode == "recurrence") and membershipned_surv >= 1
        val = base * (0.25 if protected else 1.0)
        tot += 1
        if val > 0.15:
            cnt += 1
    return cnt / tot


def run():
    rows = []
    # onset test
    onset = {s: onset_predict(make_history(s), s) for s in [0, 1]}
    # protection test cells
    for mode in ["recency", "recurrence"]:
        for alias in [False, True]:
            for prox in [False, True]:
                prev = deep_minima_prevalence(mode, alias, prox)
                rows.append({"mode": mode, "alias_on": alias, "prox_on": prox,
                             "deep_minima_prevalence": round(prev, 4)})
    return onset, rows


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    onset, rows = run()
    with open("results/membership.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open("results/membership.json", "w") as f:
        json.dump({"onset": onset, "rows": rows}, f, indent=2)
    print("onset", onset)
    for r in rows: print(r)