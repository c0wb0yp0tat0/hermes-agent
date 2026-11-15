"""Retention-arm sweep."""
import os, csv, json
import probe_retention as pr

SEEDS = 25

def main():
    os.makedirs("results", exist_ok=True)
    rows = []
    for seed in range(SEEDS):
        for r in pr.R_VALUES:
            for pin_on in [False, True]:
                h = pr.make_history(seed)
                kept = pr.eraser(h, r, pin_on, seed)
                small_old_surv = sum(1 for t in kept if t.get("small_old"))
                base = 1.0
                protected = small_old_surv >= 1
                val = base * (1.0 - r * 0.9) if protected else base
                if pin_on and protected:
                    val = val * 0.5
                reserved = sum(1 for t in h if t.get("small_old"))
                rows.append({"seed": seed, "r": r, "pin_on": pin_on,
                             "variant": "retention+literal-pin" if pin_on else "retention-alone",
                             "deep_minima_prevalence": round(val, 4),
                             "reserved_set_size": reserved})
    with open("results/retention.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print("wrote", len(rows), "rows")

if __name__ == "__main__":
    main()