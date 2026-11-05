"""Sweep runner for competition arm."""
import probe_compete, csv, json, os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    res = probe_compete.run_sweep()
    os.makedirs("results", exist_ok=True)
    with open("results/compete.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader()
        w.writerows(res)
    print("done", len(res))

if __name__ == "__main__":
    main()
