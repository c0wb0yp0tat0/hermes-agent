#!/usr/bin/env python3
"""DREAM-RUN — the daily quiet-hours consolidation (the rhythm's night half).

Scans the preserved sessions (sessions/), scores the load-bearing content,
promotes winners to the chain (the banking), and prunes fail-closed (verify
the bank BEFORE releasing — two-phase commit, tombstone on prune).

The daily rhythm: day = sessions work + SPA preserves at compression edges;
quiet hours = this run consolidates, banks, prunes. The loop feeds every day.
"""
import os, re, sys, datetime, hashlib, shutil

CHAIN = "/root/workspace/master-page/memory-chain"
DOCS = os.path.join(CHAIN, "sessions")
TOMB = os.path.join(DOCS, ".tombstoned")
WINS = os.path.join(CHAIN, "009-wins.md")

LOAD_BEARING_MARKERS = (
    "verified", "passed", "defect", "falsifier", "decision", "steer",
    "banked", "measured", "converged", "capstone", "doctrine", "fan-out",
)

def band_score(text):
    """The provenance-aware band (calibrated): structural evidence scoring."""
    s = 0.0
    nums = re.findall(r"\d+(?:\.\d+)?", text)
    if len(nums) >= 2:
        s += 0.4
    elif len(nums) == 1:
        s += 0.2
    if re.search(r"[\w/]+\.py:\d+", text) or re.search(r"/[\w/]+/", text):
        s += 0.3
    if re.search(r"\b(verified|passed|refused|measured|banked|converged|confirmed)\b", text.lower()):
        s += 0.2
    if re.search(r"\b(scripts/check|pytest|gh |hermes |battery|chars|threshold)\b", text.lower()):
        s += 0.2
    if len(text) >= 40:
        s += 0.1
    return min(s, 1.0)

def band(s):
    if s >= 0.5:
        return "PROMOTE"
    if s >= 0.2:
        return "HOLD"
    return "REJECT"

def main():
    if not os.path.isdir(DOCS):
        print("DREAM-RUN: no sessions dir yet — nothing to consolidate")
        return
    os.makedirs(TOMB, exist_ok=True)
    sessions = [d for d in sorted(os.listdir(DOCS)) if d != ".tombstoned" and d.endswith(".md")]
    if not sessions:
        print("DREAM-RUN: no preserved sessions — the day was quiet")
        return

    today = datetime.date.today().isoformat()
    print("LIGHT SLEEP: {} preserved session(s) scanned".format(len(sessions)))
    promoted = []
    ledger = []

    for sname in sessions:
        path = os.path.join(DOCS, sname)
        body = open(path).read()
        # Extract the load-bearing lines (skip the front-matter)
        lines = [l for l in body.splitlines() if l.strip().startswith("- ")]
        entries = [l[2:] for l in lines]
        winners = [e for e in entries if band(band_score(e)) in ("PROMOTE", "HOLD")]

        # PHASE 1: bank the winners (append to the wins chain)
        if winners:
            with open(WINS, "a") as f:
                f.write("- {} — DREAM-RUN banked from {}: {}\n".format(
                    today, sname.replace(".md", ""), "; ".join(w[:60] for w in winners)))
            ledger.append((sname, len(winners)))

        # PHASE 2 (fail-closed): verify the bank BEFORE pruning
        with open(WINS) as f:
            wins_text = f.read()
        banked_ok = all(("DREAM-RUN banked from {}".format(sname.replace(".md", ""))) in wins_text for w in winners) if winners else True

        if banked_ok:
            if winners:
                tomb = os.path.join(TOMB, sname)
                shutil.move(path, tomb)
                with open(tomb, "a") as f:
                    f.write("\n---\nPRUNED by DREAM-RUN {} — banked + verified\n".format(datetime.datetime.now().isoformat(timespec="seconds")))
                print("  {}: {} entry(ies) banked -> pruned (tombstoned, verified)".format(sname, len(winners)))
            else:
                # No load-bearing winners: hold without pruning (retention, not loss)
                print("  {}: no load-bearing winners — held (not pruned)".format(sname))
        else:
            print("  {}: BANK VERIFICATION FAILED — attachment persists (fail-closed)".format(sname))

    print("\nDREAM-RUN {}: {} session(s) consolidated, {} banked, loop fed".format(
        today, len(sessions), len(ledger)))

if __name__ == "__main__":
    main()
