"""Sweep wrapper for formatpin arm."""
import os, csv, json
base = os.path.dirname(os.path.abspath(__file__))
os.chdir(base)
ns = {}
exec(open("probe_formatpin.py").read().split('if __name__')[0], ns)
rows = ns["run"]()
os.makedirs("results", exist_ok=True)
with open("results/formatpin.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
with open("results/formatpin.json", "w") as f:
    json.dump({"rows": rows}, f, indent=2)
for r in rows:
    print(r)
