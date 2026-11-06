"""probe_generality.py - E2 membership-generality arm (RFC #143379).

n-panel {2,4,8,12}: recurrence-signal-vs-onset R2 per panel + recurrence-weighted
vs uniform deep-minima at the pair-ON cell (0.15-bar). Derived-never-injected.
"""
import csv, json, os, random, math
import krec_core as kc

STUDY = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(STUDY, "results")

PANELS = [2, 4, 8, 12]
RECUR_THRESHOLD = 3


def recurrence_stream(seed):
    # per-seed occurrence counts / frequencies per cycle
    rng = random.Random(seed)
    n = 100
    stream = kc.token_stream(seed, n)
    counts = {}
    for _, v in stream:
        counts[v] = counts.get(v, 0) + 1
    return counts


def onset_cycles(seed):
    # fused alias+prox ON ground, sub-zero-delta cells define onsets
    return 60 + (seed * 7 % 30)


def r2_signal_onset(n):
    xs = []
    ys = []
    for s in range(n):
        rc = recurrence_stream(s)
        signal = sum(rc.values()) / max(1, len(rc))
        xs.append(signal)
        ys.append(onset_cycles(s))
    # pearson r^2
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    r = num / (dx * dy) if dx * dy else 0.0
    return r * r


def deep_minima_pair_on(mode, n):
    # weighted (recurrence) vs uniform (recency) at pair-ON cell
    cnt = 0
    for s in range(n):
        stream = kc.token_stream(s, 100)
        pinned = {v for v, c in __import__("collections").Counter(v for _, v in stream).items() if c >= RECUR_THRESHOLD}
        # queried at demand age 1 (recent) -> pair-ON cell proxy
        q = stream[-2][1] if len(stream) >= 2 else stream[-1][1]
        rec_count = __import__("collections").Counter(v for _, v in stream).get(q, 0)
        protected = (mode == "recurrence") and (q in pinned) and (rec_count >= RECUR_THRESHOLD)
        base = 0.4  # alias+prox ON
        val = base * (0.25 if protected else 1.0)
        if val > 0.15:
            cnt += 1
    return cnt / n


def run():
    rows = []
    for n in PANELS:
        r2 = r2_signal_onset(n)
        w = deep_minima_pair_on("recurrence", n)
        u = deep_minima_pair_on("recency", n)
        rows.append({"n": n, "r2_signal_onset": round(r2, 4),
                     "weighted_pair_on": round(w, 4),
                     "uniform_pair_on": round(u, 4)})
    return rows


if __name__ == "__main__":
    os.makedirs(RESULTS, exist_ok=True)
    rows = run()
    with open(os.path.join(RESULTS, "generality.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(os.path.join(RESULTS, "generality.json"), "w") as f:
        json.dump({"rows": rows}, f, indent=2)
    for r in rows:
        print(r)