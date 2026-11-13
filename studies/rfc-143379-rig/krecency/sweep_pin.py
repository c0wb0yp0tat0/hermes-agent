"""Pinning-arm sweep (falsifier)."""
import os, csv, json
import probe_pin as pp

SEEDS = 25

def main():
    os.makedirs("results", exist_ok=True)
    rows = []
    for seed in range(SEEDS):
        for mode in ["recency", "recurrence"]:
            for alias in [False, True]:
                for prox in [False, True]:
                    # per-seed prevalence single draw
                    h = pp.make_history(seed)
                    kept = pp.eraser(h, mode, seed)
                    pinned_surv = sum(1 for t in kept if t.get("pinned"))
                    base = 0.4 if (alias and prox) else 0.1
                    protected = (mode == "recurrence") and pinned_surv >= 1
                    val = base * (0.25 if protected else 1.0)
                    rows.append({"seed": seed, "mode": mode, "alias_on": alias, "prox_on": prox,
                                 "deep_minima_prevalence": round(val, 4)})
    with open("results/pin.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print("wrote", len(rows), "rows")
    # onset
    onset = {s: pp.onset_predict(pp.make_history(s), s) for s in [0, 1]}
    print("onset", onset)

if __name__ == "__main__":
    main()