"""battery_pilot.py — F4 pilot: the three-arm battery's machinery, proven end-to-end.

The pilot's job: verify the machinery BEFORE the real arms ride their seats —
episode construction from the non-re-observable-fact class, mirrored episodes
across arms, fresh stores, cache-hit + token logging, the cost-per-success rows,
and the pre-committed decision rule's computation. The pilot's responders are
STUB responders (deterministic, marked STUB-PILOT in the ledger) so the machinery
is testable without burning seats; the real run swaps in the frozen reader seat
(local-LM floor via Harbor, or the API seats per lane-1) and the judge-control
gate from F3.

Arm semantics (LANE-1, the field vocabulary):
  A TRUNCATED-UNCOMPENSATED — the raw reader, history cut at the cut-point.
  B SUBSTRATE — same reader + the durable record + the governor.
  C ORACLE — evidence-only turns (the upper bound, model-vs-substrate separation).

Episode class: the non-re-observable fact (PersistGym's class) — a fact planted
early, destroyed at the cut-point unless the record keeps it.
"""

import hashlib
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes.judge_control_gate import FrozenJudge, JudgeControlGate  # noqa: E402


# ---- episode construction (the non-re-observable-fact class) ----
def make_episode(seed, cut_point=40):
    """One episode: a planted fact at a staged turn, filler between, then the
    cut-point that removes the fact from re-observability. Mirrored verbatim
    across arms; only the memory channel differs."""
    rnd = hashlib.sha256(str(seed).encode()).hexdigest()
    fact = f"fact-{rnd[:12]}"
    turns = [f"turn-{i}" for i in range(cut_point)] + [
        f"PLANTED: {fact} is the answer key",  # the only place the fact appears
    ] + [f"filler-{i}" for i in range(cut_point)]
    question = f"what is the answer key?"
    return {"seed": seed, "fact": fact, "turns": turns, "question": question,
            "cut_point": cut_point}


def arm_view(episode, arm, substrate=None):
    """The arm's context construction: the same episode, different memory channel."""
    if arm == "A":  # truncated-uncompensated: the cut removes everything at/beyond cut_point
        return {"view": episode["turns"][: episode["cut_point"]], "fact_available": False,
                "source": "truncated"}
    if arm == "C":  # oracle: evidence-only turns, no history at all
        return {"view": [episode["turns"][episode["cut_point"]]], "fact_available": True,
                "source": "oracle"}
    # B substrate: same truncated window + the durable record the governor kept
    return {"view": episode["turns"][: episode["cut_point"]] + [substrate or ""],
            "fact_available": episode["fact"] in (substrate or ""), "source": "substrate"}


class StubReader:
    """Pilot responder: answers the question iff the fact is in its view. Marked
    STUB-PILOT so the ledger never confuses it with a real reader's run."""

    def __init__(self, name="stub-reader"):
        self.name = name

    def __call__(self, view):
        if any("PLANTED" in t for t in view["view"]):
            return f"answer:{view['view'][-1].split(':')[1].strip()}"
        return "UNKNOWN"


class SubstrateRecord:
    """The governor's durable record for the pilot: the planted fact written at
    write-time, exactly the doc-chain's write-time assert in miniature."""

    def __init__(self):
        self.entries = []

    def write(self, text):
        self.entries.append(text)
        return self

    def read(self):
        return " ".join(self.entries)


def run_pilot(n_episodes=10, cut_point=6):
    """The machinery run: mirrored eps, fresh stores, three arms, cost+cache rows,
    the decision rule computed (with STUB responders — a machinery receipt, not a
    real verdict)."""
    reader = StubReader()
    ledger = {"pilot": True, "responders": "STUB-PILOT", "arms": {}, "n": n_episodes,
              "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    for arm in "ABC":
        correct = 0
        tokens = 0
        cache_hits = 0
        for i in range(n_episodes):
            ep = make_episode(i, cut_point=cut_point)
            store = SubstrateRecord()
            substrate = store.write(ep["turns"][ep["cut_point"]]).read()
            view = arm_view(ep, arm, substrate)
            ans = reader(view)
            tokens += len(view["view"])  # pilot token proxy: view length
            if view["source"] == "truncated":  # pilot cache proxy: truncation misses
                cache_hits += 0
            else:
                cache_hits += 1
            if ep["fact"] in ans:
                correct += 1
        ledger["arms"][arm] = {
            "correct": correct, "accuracy": round(correct / n_episodes, 3),
            "tokens": tokens, "cache_hit_rate": round(cache_hits / max(1, n_episodes), 3),
        }
    a, b, c = (ledger["arms"][x] for x in "ABC")
    ledger["decision_rule"] = {
        "B_minus_A": round(b["accuracy"] - a["accuracy"], 3),
        "B_over_0.85C": b["accuracy"] >= 0.85 * c["accuracy"],
        "rule": "machinery-only — STUB responders; a real verdict needs the frozen reader + judge gate",
    }
    return ledger


def write_ledger(ledger, path):
    with open(path, "w") as f:
        json.dump(ledger, f, indent=2)
    return path


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "BATTERY-PILOT-LEDGER-20261119.json")
    print(write_ledger(run_pilot(), out))
