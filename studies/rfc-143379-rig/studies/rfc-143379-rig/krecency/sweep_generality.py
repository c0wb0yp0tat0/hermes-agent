"""sweep_generality.py - E2 sweep."""
import os, csv, json
import probe_generality as pg

def main():
    os.makedirs("results", exist_ok=True)
    rows = pg.run()
    with open("results/generality.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print("wrote", len(rows), "rows")
    for r in rows: print(r)

if __name__ == "__main__":
    main()