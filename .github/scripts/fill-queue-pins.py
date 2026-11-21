#!/usr/bin/env python3
"""fill-queue-pins.py — the fill-queue's rotation: the next receipted green pin.
The queue = the RECEIPTS ledger's certified pins; the state's a local index;
the rotation advances on selection so a failed leg never sticks the queue."""
import json, sys

QUEUE = [
    "d1bdb4582cd5d16be6a6b486f696f8240c222b96",  # #139606 merge head (11-05 GREEN)
    "ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a",  # #141876 (82 GREEN, re-verified 11-11)
    "490527023765ffd901e72d85fc43e60560e5aabd",  # avrea-parallel runner-env head (89 GREEN)
    "a996d4ad3039e280dc21e9b558f5a44c081dda42",  # whole-anchor resolution head (98 GREEN)
    "60a2e1563802368b46018bba2a70f11de31a6b0a",  # #116673 (66 GREEN)
    "ffb85c2c5880672237e1a48bea383f634df70985",  # #140008 (64 GREEN)
    "c39d8ce722d4c5d43a3aa2ea3e71f698f500d870",  # round2-combined-substrate (70 GREEN)
]
STATE = "/root/scripts/fill-queue-state.json"


def load_index():
    try:
        return json.load(open(STATE)).get("index", 0)
    except Exception:
        return 0


def save_index(i):
    json.dump({"index": i}, open(STATE, "w"))


if __name__ == "__main__":
    i = load_index()
    pin = QUEUE[i % len(QUEUE)]
    save_index(i + 1)
    if len(sys.argv) > 1 and sys.argv[1] == "next":
        sys.stdout.write(pin)
    else:
        print(pin)
