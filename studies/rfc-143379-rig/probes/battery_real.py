"""battery_real.py — F4: the REAL arm run on the local-LM floor (Harbor :44831).

Wires the frozen local reader (Harbor llama-server, DeepSeek-V4-Pro-Qwen3.5-9B
MTP Q3_K_S) into the battery's machinery, runs the F3 judge-control gate first
(20-episode control, >=90% or NULL), then the three arms on a real small-N run
with fresh stores, cache/token rows, and the pre-committed decision rule's
computation. The Luna leg's seat (a paid/Nous route) is NOT fired here — its
costed row stays inside the probe per lane-1; this run proves the real path on
the free local floor. If the judge gate NULLs, the run aborts before any arm
result is read (results never read on NULL).
"""

import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes.battery_pilot import arm_view, make_episode, SubstrateRecord  # noqa: E402
from probes.judge_control_gate import FrozenJudge, JudgeControlGate  # noqa: E402

HARBOR = os.environ.get("HARBOR_URL", "http://127.0.0.1:44831/v1/chat/completions")
MODEL = os.environ.get("HARBOR_MODEL",
                       "/root/.hermes/cache/scratch/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q3_K_S.gguf")


class LocalLMReader:
    """The frozen reader: Harbor's llama-server, temperature 0, one-shot answer."""

    def __init__(self, url=HARBOR, model=MODEL):
        self.url, self.model = url, model
        self.calls = 0

    def __call__(self, view):
        self.calls += 1
        prompt = ("You are answering a recall probe. Given the context below, answer the "
                  "question with the exact answer value and nothing else.\n\nCONTEXT:\n"
                  + "\n".join(view["view"][-8:]) +
                  "\n\nQUESTION: " + view["question"] + "\nANSWER:")
        body = {"model": self.model, "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 24, "temperature": 0}
        req = urllib.request.Request(self.url, data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=180).read().decode())
            return (r.get("choices") or [{}])[0].get("message", {}).get("content", "")
        except Exception:
            return "<READER-ERROR>"


def fact_matches(answer, fact):
    a = (answer or "").replace("\n", " ").strip()
    return fact.replace("-", "") in a.replace("-", "").replace(" ", "").strip()


def run_real(n_episodes=5, cut_point=6):
    reader = LocalLMReader()
    ledger = {"pilot": False, "responders": "LOCAL-LM-FLOOR (Harbor DeepSeek-V4-Pro-Qwen3.5-9B)",
              "n": n_episodes, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

    # F3 first: the judge-control gate (20 known answers THROUGH the frozen local reader —
    # echo-questions, so the gate measures the reader's fidelity, which is the point)
    reader = LocalLMReader()
    _ctrl_q = lambda i: ("Reply with exactly this token and nothing else: TOKEN%d" % i)
    _ctrl_set = [(_ctrl_q(i), "TOKEN%d" % i) for i in range(20)]
    judge = FrozenJudge(lambda q: reader({"view": [q], "question": q}), judge_id="control-harbor")
    gate = JudgeControlGate(judge, _ctrl_set)
    verdict = gate.run()
    ledger["judge_control"] = verdict
    if verdict["null"]:
        ledger["aborted"] = "judge-control NULL — results never read; judge refreeze required"
        return ledger

    # The arms (mirrored episodes, fresh stores)
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
            tokens += len(view["view"])
            cache_hits += 0 if view["source"] == "truncated" else 1
            if fact_matches(ans, ep["fact"]):
                correct += 1
        ledger["arms"][arm] = {"correct": correct,
                               "accuracy": round(correct / n_episodes, 3),
                               "tokens": tokens,
                               "cache_hit_rate": round(cache_hits / max(1, n_episodes), 3),
                               "reader_calls": reader.calls}
        reader.calls = 0

    a, b, c = (ledger["arms"][x] for x in "ABC")
    ledger["decision_rule"] = {
        "B_minus_A": round(b["accuracy"] - a["accuracy"], 3),
        "B_over_0.85C": b["accuracy"] >= 0.85 * c["accuracy"],
        "certify_would_require": "B-A>=20pts AND B>=0.85C at FULL run scale (200/arm) — "
                                 "this small-N run is the real-path receipt, not the verdict",
    }
    return ledger


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "BATTERY-REAL-LEDGER-20261119.json")
    ledger = run_real()
    with open(out, "w") as f:
        json.dump(ledger, f, indent=2)
    print(json.dumps(ledger, indent=2))
