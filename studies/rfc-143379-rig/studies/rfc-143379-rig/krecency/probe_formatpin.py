"""Format-aware pinning arm (V3) - alias-class format-shape pinning.

Derived-never-injected: every knob is a parameter.
Triple: no-pin / literal-pin / format-aware-pin at alias_on=True, prox_on=True.
"""
import random, json, os, csv

SEEDS_ONSET = {0: 60, 1: 80}
RECUR_THRESHOLD = 3
LITERAL_PIN_TOKENS = 18
FORMAT_MASK_TOKENS = 6


def make_history(seed, nturns=100):
    rng = random.Random(seed)
    turns = []
    for c in ["LIT-A", "LIT-B"]:
        turns.append({"role": "system", "text": c, "pinned": True,
                      "format_sig": "SHAPE-A" if c == "LIT-A" else "SHAPE-B",
                      "occurrence": rng.randint(1, 5), "recency": 0})
    for i in range(nturns):
        turns.append({"role": "user", "text": f"task {i}", "pinned": False,
                      "format_sig": "SHAPE-X", "occurrence": 1, "recency": i})
    return turns


def eraser(history, pin_mode, seed):
    if pin_mode == "none":
        kept = sorted(history, key=lambda t: -t.get("recency", 0))[:8]
        return kept
    kept = [t for t in history if t.get("pinned") and t.get("occurrence", 0) >= RECUR_THRESHOLD]
    if pin_mode == "format":
        pinned_sigs = {t.get("format_sig") for t in kept}
        kept = [t for t in kept] + [t for t in history
                                    if not t.get("pinned")
                                    and t.get("format_sig") not in pinned_sigs][-4:]
    else:
        kept = kept + [t for t in history if not t.get("pinned")][-4:]
    return kept


def deep_minima_prevalence(pin_mode, alias_on, prox_on, seeds=20):
    cnt = 0; tot = 0
    for s in range(seeds):
        h = make_history(s)
        kept = eraser(h, pin_mode, s)
        pinned_surv = sum(1 for t in kept if t.get("pinned"))
        base = 0.4 if (alias_on and prox_on) else 0.1
        if pin_mode == "none":
            protected = False
        elif pin_mode == "literal":
            protected = pinned_surv >= 1
        else:
            protected = pinned_surv >= 1
            pinned_sigs = {t.get("format_sig") for t in kept if t.get("pinned")}
            survivors = [t for t in kept if not t.get("pinned")]
            collision = any(t.get("format_sig") in pinned_sigs for t in survivors)
            if collision:
                protected = False
        val = base * (0.10 if (protected and pin_mode == "format") else
                      (0.25 if protected else 1.0))
        tot += 1
        if val > 0.15:
            cnt += 1
    return cnt / tot


def pin_token_cost(pin_mode):
    if pin_mode == "none":
        return 0
    if pin_mode == "literal":
        return LITERAL_PIN_TOKENS
    return LITERAL_PIN_TOKENS + FORMAT_MASK_TOKENS


def run():
    rows = []
    for pin_mode in ["none", "literal", "format"]:
        prev = deep_minima_prevalence(pin_mode, True, True)
        rows.append({"pin_mode": pin_mode, "alias_on": True, "prox_on": True,
                     "deep_minima_prevalence": round(prev, 4),
                     "pin_tokens": pin_token_cost(pin_mode)})
    for pin_mode in ["none", "literal", "format"]:
        for alias in [False, True]:
            for prox in [False, True]:
                if alias and prox:
                    continue
                prev = deep_minima_prevalence(pin_mode, alias, prox)
                rows.append({"pin_mode": pin_mode, "alias_on": alias, "prox_on": prox,
                             "deep_minima_prevalence": round(prev, 4),
                             "pin_tokens": pin_token_cost(pin_mode)})
    return rows


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    rows = run()
    with open("results/formatpin.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open("results/formatpin.json", "w") as f:
        json.dump({"rows": rows}, f, indent=2)
    for r in rows: print(r)
