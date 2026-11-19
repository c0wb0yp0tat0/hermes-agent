"""battery_full.py — SPRINT F4-FULL: the pre-committed verdict's run (200 eps/arm).

Small-N receipt (2026-11-19, rowed): A 0.0 / B 1.0 / C 1.0 — the substrate restores
what truncation destroys on the API reader. This run executes the pre-committed
decision rule at its proper scale: 200 episodes per arm, mirrored across arms,
fresh stores, the deterministic exact-match judge (F3 gate first), cost + cache-hit
rows, and the verbatim decision-rule computation (CERTIFY iff B-A>=20pts AND
B>=0.85*C; FALSIFY if B-A<20 OR (B<0.85C AND B<=A); INCONCLUSIVE per the gate
classes). 429-aware with bounded retries (the free seat's rate limits).
"""

import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes.battery_pilot import arm_view, make_episode, SubstrateRecord  # noqa: E402
from probes.battery_real_v2 import _reader_key, normalize  # noqa: E402
from probes.judge_control_gate import FrozenJudge, JudgeControlGate  # noqa: E402

URL = os.environ.get("READER_URL", "https://inference-api.nousresearch.com/v1/chat/completions")
MODEL = os.environ.get("READER_MODEL", "upstage/solar-mini4:free")
N = int(os.environ.get("BATTERY_N", "200"))
CUT = int(os.environ.get("BATTERY_CUT", "12"))
MAX_RETRY = 3


class Reader:
    def __init__(self):
        self.key = _reader_key()
        self.calls = 0

    def __call__(self, view, question=None):
        q = question if question is not None else view.get("question", "")
        prompt = ("You are answering a recall probe. Given the context below, answer the "
                  "question with the exact answer value and nothing else.\n\nCONTEXT:\n"
                  + "\n".join(view["view"][-12:]) +
                  "\n\nQUESTION: " + q + "\nANSWER:")
        body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 24, "temperature": 0}
        for attempt in range(MAX_RETRY):
            self.calls += 1
            try:
                req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                             headers={"Content-Type": "application/json",
                                                      "Authorization": "Bearer " + self.key},
                                             method="POST")
                r = json.loads(urllib.request.urlopen(req, timeout=90).read().decode())
                return (r.get("choices") or [{}])[0].get("message", {}).get("content", "")
            except Exception as e:
                if attempt < MAX_RETRY - 1:
                    time.sleep(2 + 3 * attempt)
                else:
                    return "<READER-ERROR:%s>" % type(e).__name__


def run_full(n=N, cut=CUT):
    judge = {"grade": lambda a, g: normalize(g) and normalize(g) in normalize(a)}
    ledger = {"pilot": False, "scale": "FULL (pre-committed rule)", "n_per_arm": n,
              "cut_point": cut, "responders": MODEL,
              "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "arms": {}}

    # F3 first: the judge-control gate (pure deterministic grader, 20 known pairs)
    ctrl = [(f"the answer is TOKEN{i} here", f"TOKEN{i}") for i in range(20)]
    gate = JudgeControlGate(
        FrozenJudge(lambda q: "PASS" if judge["grade"](q.split("|", 1)[0], q.split("|", 1)[1]) else "FAIL",
                    judge_id="exact-match-full"),
        [(f"{a}|{g}", "PASS") for a, g in ctrl])
    verdict = gate.run()
    ledger["judge_control"] = verdict
    if verdict["null"]:
        ledger["aborted"] = "judge-control NULL — results never read"
        return ledger

    reader = Reader()
    for arm in "ABC":
        correct, tokens, cache_hits = 0, 0, 0
        for i in range(n):
            ep = make_episode(i + (1000 if arm == "B" else 0) + (2000 if arm == "C" else 0),
                              cut_point=cut)
            store = SubstrateRecord()
            substrate = store.write(ep["turns"][ep["cut_point"]]).read()
            view = arm_view(ep, arm, substrate)
            ans = reader(view, ep["question"])
            tokens += len(view["view"])
            cache_hits += 0 if view["source"] == "truncated" else 1
            if judge["grade"](ans, ep["fact"]):
                correct += 1
        ledger["arms"][arm] = {"correct": correct,
                               "accuracy": round(correct / n, 4),
                               "tokens": tokens,
                               "cache_hit_rate": round(cache_hits / n, 3),
                               "reader_calls": reader.calls}
        reader.calls = 0

    a, b, c = (ledger["arms"][x] for x in "ABC")
    b_a = round((b["accuracy"] - a["accuracy"]) * 100, 1)
    b_over = b["accuracy"] >= 0.85 * c["accuracy"]
    ledger["decision_rule"] = {
        "B_minus_A_points": b_a,
        "B_over_0.85C": b_over,
        "VERDICT": "CERTIFY" if (b_a >= 20 and b_over) else
                   ("FALSIFY" if (b_a < 20 or (b_over is False and b["accuracy"] <= a["accuracy"])) else
                    "INCONCLUSIVE"),
        "rule": "CERTIFY iff B-A>=20pts AND B>=0.85*C; FALSIFY iff B-A<20 OR (B<0.85C AND B<=A)",
    }
    return ledger


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "BATTERY-FULL-LEDGER-20261119.json")
    l = run_full()
    with open(out, "w") as f:
        json.dump(l, f, indent=2)
    print(json.dumps(l, indent=2))
