"""Standalone constraint sweep (governance arm, RFC #143379).

25 seeds x 4 strategies x 4 arms (present / compacted / pinned / absent)
using probe_constraints machinery. Writes results/sweep_constraints.csv and
aggregates to results/constraints.json.
"""
import os, csv, json, random
import probe_constraints as pc

SEEDS = 25
ARMS = ["present", "compacted", "pinned", "absent"]


def per_seed_violation(strategy, arm, seed):
    h = pc.make_history(seed)
    if arm == "present":
        surv = set(pc.CONSTRAINTS)
    elif arm == "absent":
        surv = set()
    elif arm == "compacted":
        surv = pc.eraser(strategy, h, pinned=False)
    elif arm == "pinned":
        surv = pc.eraser(strategy, h, pinned=True)
    else:
        surv = set()
    viols = sum(1 for c in pc.CONSTRAINTS if c not in surv)
    return viols / len(pc.CONSTRAINTS)


def main():
    os.makedirs("results", exist_ok=True)
    rows = []
    for seed in range(SEEDS):
        for strat in pc.STRATEGIES:
            for arm in ARMS:
                vr = per_seed_violation(strat, arm, seed)
                rows.append({"seed": seed, "strategy": strat, "arm": arm,
                             "violation_rate": round(vr, 4)})
    # write per-seed CSV
    with open("results/sweep_constraints.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["seed", "strategy", "arm", "violation_rate"])
        w.writeheader()
        w.writerows(rows)

    # aggregate over seeds
    agg = []
    for strat in pc.STRATEGIES:
        out = {"strategy": strat}
        for arm in ARMS:
            vals = [r["violation_rate"] for r in rows
                    if r["strategy"] == strat and r["arm"] == arm]
            out[arm] = round(sum(vals) / len(vals), 4)  # type: ignore[assignment]
        agg.append(out)

    with open("results/constraints.json", "w") as f:
        json.dump({"n_seeds": SEEDS, "rows": agg, "n_rows": len(rows)}, f, indent=2)

    # print table
    print("strategy           present compacted pinned absent")
    for a in agg:
        print(f"{a['strategy']:<18} {a['present']:.2f}    {a['compacted']:.2f}      {a['pinned']:.2f}   {a['absent']:.2f}")
    ranked = sorted(agg, key=lambda x: -x["compacted"])
    print("ranking (compacted, worst first):", " > ".join(f"{r['strategy']} ({r['compacted']})" for r in ranked))


if __name__ == "__main__":
    main()
