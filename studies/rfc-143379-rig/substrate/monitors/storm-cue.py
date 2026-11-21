#!/usr/bin/env python3
"""STORM-CUE — the web storm trigger, scheduled.

The storm-in-the-protocol doctrine, mechanized: the storm is a standing tool,
and a cron cues when a storm is appropriate. This script watches the surfaces
(new pre-prints from the arxiv-watch, new chain entries) and produces a STORM
CUE — the topics worth storming, the mechanisms underneath, the nuance that
changed. The cue is the trigger for the next web storm.
"""
import os, json, datetime

ARXIV_STATE = "/root/.hermes/cache/scratch/arxiv-watch/state.json"
CHAIN = "/root/workspace/master-page/memory-chain"

def recent_chain_entries(hours=24):
    """The chain's new entries (the doctrine/lessons/wins that landed)."""
    entries = []
    cutoff = datetime.datetime.now() - datetime.timedelta(hours=hours)
    for seg in ("001-conventions", "002-lessons", "009-wins"):
        p = os.path.join(CHAIN, seg + ".md")
        if not os.path.exists(p):
            continue
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(p))
        if mtime > cutoff:
            entries.append("{} (modified {})".format(seg, mtime.strftime("%H:%M")))
    return entries

def new_preprints(hours=24):
    """The pre-prints that landed since the last cue."""
    if not os.path.exists(ARXIV_STATE):
        return []
    state = json.load(open(ARXIV_STATE))
    cutoff = datetime.datetime.now() - datetime.timedelta(hours=hours)
    fresh = []
    for eid, rec in state.items():
        try:
            pub = datetime.datetime.strptime(rec.get("published", ""), "%Y-%m-%d")
            if pub.date() > cutoff.date():
                fresh.append("{} — {}".format(rec.get("title", "?")[:60], eid))
        except ValueError:
            pass
    return fresh

def main():
    print("=== STORM CUE {} ===".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    chain = recent_chain_entries()
    preprints = new_preprints()

    if not chain and not preprints:
        print("NO CUE: no new chain entries, no new pre-prints — the surfaces are quiet")
        print("(the storm fires when the nuance changes, not on a schedule)")
        return

    if chain:
        print("CHAIN MOVEMENT (the doctrine layer):")
        for e in chain:
            print("  - {}".format(e))
    if preprints:
        print("NEW PRE-PRINTS (the scholarly stream):")
        for p in preprints[:5]:
            print("  - {}".format(p))

    print("\nSTORM CUE: the nuance changed — the mechanisms underneath these new")
    print("entries/pre-prints are the storm's targets. Dissect, don't adopt at face")
    print("value; the storm informs, the design stays ours.")

if __name__ == "__main__":
    main()
