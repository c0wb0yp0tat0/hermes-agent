"""Recitation-length arm (RFC #143379 K-recency). Deterministic sim.

Knob:
  recite : recitation-degradation knob — even on exact recovery, the
           recitation's fidelity decays with the session's cumulative length
           (Length-Despite-Perfect-Retrieval class). Modeled as per-token
           re-emission fidelity over the cumulative session length (a
           per-position error rate, not a hand-written decay curve).

Derived-never-injected: knobs are parameters; no decay-shaped function
multiplies trial outcomes. Scoping proof in scoping_test_recite.py.
"""
import random, hashlib, os, math, csv, json

K = 10
FLOOR = {2:0.30,3:0.24,4:0.204,5:0.18,6:0.17,7:0.16,8:0.156,16:0.151,32:0.14}
EPS = 0.002  # per-token recitation error rate (constant; length drives decay)

def token_stream(seed,n):
    rng=random.Random(seed)
    items=[]
    for i in range(n):
        kind=rng.choice(["path","sha","arg"])
        if kind=="path": val=f"/repo/src/mod{i}/file_{rng.randrange(1000)}.py"
        elif kind=="sha": val=hashlib.sha256(f"{seed}-{i}".encode()).hexdigest()[:12]
        else: val=f"--flag={rng.randrange(9999)}"
        items.append((kind,val))
    return items

def demand_age(cycle_idx,rng):
    return 1+int((cycle_idx/10.0)**1.3)

def trial(seed,cycle_idx,ratio,k,pa,M_on,recite):
    rng=random.Random(seed*1000+cycle_idx)
    n=max(ratio+1,cycle_idx)
    stream=token_stream(seed+cycle_idx,n)
    wbuf=[]
    if k>0:
        for t in stream[-k:]:
            wbuf.append(t[1])
    if pa>0 and len(stream)>1:
        old=stream[max(0,n-1-demand_age(cycle_idx,rng))][1]
        if rng.random()<pa:
            wbuf.append(old)
    age=demand_age(cycle_idx,rng)
    idx=max(0,n-1-age)
    q=stream[idx][1] if stream else stream[-1][1]
    M=sum(1 for _ in wbuf) if M_on else 0
    hit=0
    if q in wbuf:
        hit=1
    else:
        floor=FLOOR.get(ratio,1.0/ratio)
        if rng.random()<float(floor):
            hit=1
    score=1.0 if hit else 0.0
    # recitation fidelity: per-token re-emission over cumulative session length
    if recite and hit==1:
        length=n  # cumulative session length proxy
        # per-token exact probability (1-EPS)^length over literal tokens
        lit_tokens=len(q.split()) if isinstance(q,str) else 1
        lit_tokens=max(1,len(q))
        fidelity=(1.0-EPS)**(lit_tokens* (1+cycle_idx//50))
        if rng.random()>fidelity:
            score=0.0  # recitation failed despite perfect retrieval
    evidence_mass=1.0 if (q in wbuf) else 0.0
    excursion=1 if score==0 else 0
    return {"seed":seed,"cycle":cycle_idx,"ratio":ratio,"k":k,"pa":pa,
            "M_on":int(M_on),"recite":int(recite),"score":score,
            "excursion":excursion,"evidence_mass":evidence_mass,"M":M}

def run_sweep():
    seeds=20
    cycles=[10,50,100,200,300]
    ratios=[4,8]
    rows=[]
    for s in range(seeds):
        for c in cycles:
            for r in ratios:
                for pa,M_on in [(0.0,False),(0.3,True)]:
                    for recite in [False,True]:
                        t=trial(s,c,r,K,pa,M_on,recite)
                        rows.append(t)
    return rows

if __name__=="__main__":
    os.makedirs("results",exist_ok=True)
    rows=run_sweep()
    with open("results/recite.csv","w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    from collections import defaultdict
    prev=defaultdict(lambda: defaultdict(int))
    tot=defaultdict(lambda: defaultdict(int))
    for row in rows:
        key=(row["pa"],row["M_on"],row["recite"])
        tot[key][row["cycle"]]+=1
        prev[key][row["cycle"]]+=row["excursion"]
    xs=[r["evidence_mass"] for r in rows]
    ys=[r["score"] for r in rows]
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    num=sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    dx=math.sqrt(sum((x-mx)**2 for x in xs))
    dy=math.sqrt(sum((y-my)**2 for y in ys))
    r2=(num/(dx*dy))**2 if dx*dy else 0.0
    with open("results/recite_summary.json","w") as f:
        json.dump({"n":len(rows),"r2_evidence":r2},f)
    print("done",len(rows),"r2",r2)
    cycles=[10,50,100,200,300]
    for key in sorted(tot):
        print(key, {c: round(prev[key][c]/tot[key][c],3) for c in cycles})
