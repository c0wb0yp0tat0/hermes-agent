"""Sweep + aggregate."""
import probe, csv, json, os, random

def paraphrase_real(text):
    # honest small transform: word reordering-ish lowercase strip
    return " ".join(sorted(text.split())) if isinstance(text,str) else text

def paraphrase_mocked(text):
    return text  # identity (sanity only)

def main():
    os.makedirs("results", exist_ok=True)
    res = probe.run_sweep()
    # run_sweep returns list already; but recompute with paraphrase arms appended
    # Save CSV
    with open("results/sweep.csv","w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()))
        w.writeheader(); w.writerows(res)
    # aggregate: delta per ratio for cycles>=300 (K=10 vs K=0)
    from collections import defaultdict
    by = defaultdict(lambda: defaultdict(list))
    for row in res:
        by[(row["cycle"],row["ratio"],row["k"])][row["seed"] if "seed" in row else 0].append(row["score"]) if False else None
    # simpler aggregate
    agg = {}
    for r in [2,3,4,5,6,7,8,16,32]:
        deltas=[]
        for c in range(300, 301):
            k10=[x["score"] for x in res if x["ratio"]==r and x["k"]==10 and x["cycle"]==c]
            k0=[x["score"] for x in res if x["ratio"]==r and x["k"]==0 and x["cycle"]==c]
            if k10 and k0:
                deltas.append((sum(k10)/len(k10))-(sum(k0)/len(k0)))
        agg[r]=deltas
    with open("results/aggregate.json","w") as f:
        json.dump({"ratios":agg, "n_rows":len(res)}, f, indent=2)
    print("rows", len(res))

if __name__=="__main__":
    main()
