"""Sweep runner for demand-age instrument."""
import probe_age, csv, json, os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    res = probe_age.run_sweep()
    os.makedirs("results", exist_ok=True)
    with open("results/sweep_age.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)
    agg = defaultdict(lambda: defaultdict(list))
    for row in res:
        agg[(row["cycle"], row["ratio"])][row["k"]].append(row["score"])  # type: ignore[attr-defined]
    summary = {}
    for (c, r), ks in agg.items():
        k0 = sum(ks[0]) / len(ks[0])
        k10 = sum(ks[10]) / len(ks[10])
        summary[f"{c}_{r}"] = {"k0": k0, "k10": k10, "delta_pp": (k10 - k0) * 100}
    with open("results/agg_age.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("done", len(res))

if __name__ == "__main__":
    main()
