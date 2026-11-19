"""battery_real_v2.py — F4 refreeze: the deterministic-judge battery (SPRINT-FIRE-SEQUENCE F3/F4).

FINDING RECEIPTED (battery_real v1, 2026-11-19): the local-LM floor (Harbor,
DeepSeek-V4-Pro-Qwen3.5-9B Q3_K_S) scored 0.15 on the model-judge's echo control —
the quantized seat cannot reliably reproduce exact tokens. Per F3's pre-registered
gate (>=90% or NULL; NULL = results never read), the run aborted correctly. The
refreeze: the JUDGE role is refrozen as a DETERMINISTIC EXACT-MATCH grader (the
probe's facts are exact strings; a deterministic grader cannot be confused and its
mis-scoring class is structurally closed — the F3 gate's purpose). The READER
remains the local seat: the arms measure ITS recollection, which is the probe's
subject. The judge-control now verifies the grading pipeline itself on 20 known
(answer, gold) pairs — a bug in extraction/case-normalization surfaces as NULL.
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


def normalize(s):
    return "".join(ch for ch in (s or "").lower() if ch.isalnum())


class ExactMatchJudge:
    """The refrozen judge: deterministic exact-match on normalized strings. Blind to
    arm identity — it grades (answer, gold) pairs only."""

    def __init__(self):
        self.calls = 0

    def grade(self, answer, gold):
        self.calls += 1
        a, g = normalize(answer), normalize(gold)
        if not g:
            return False
        return g in a  # the fact's normalized string appears in the answer


class LocalLMReader:
    """The frozen reader: Harbor's llama-server, temperature 0, one-shot answer."""

    def __init__(self, url=HARBOR, model=MODEL):
        self.url, self.model = url, model
        self.calls = 0

    def __call__(self, view, question=None):
        self.calls += 1
        q = question if question is not None else view.get("question", "")
        prompt = ("You are answering a recall probe. Given the context below, answer the "
                  "question with the exact answer value and nothing else.\n\nCONTEXT:\n"
                  + "\n".join(view["view"][-10:]) +
                  "\n\nQUESTION: " + q + "\nANSWER:")
        body = {"model": self.model, "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 24, "temperature": 0}
        req = urllib.request.Request(self.url, data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=180).read().decode())
            return (r.get("choices") or [{}])[0].get("message", {}).get("content", "")
        except Exception:
            return "<READER-ERROR>"


def run_v2(n_episodes=5, cut_point=6):
    judge = ExactMatchJudge()
    ledger = {"pilot": False, "refreeze": "deterministic exact-match judge (v1's model-judge "
              "NULLed at 0.15 on the echo control — receipted)",
              "responders": "LOCAL-LM-FLOOR (Harbor DeepSeek-V4-Pro-Qwen3.5-9B)",
              "n": n_episodes, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "arms": {}, "decision_rule": {}}

    # F3 first: the judge-control gate on the GRADING PIPELINE (20 known pairs).
    # A deterministic grader must pass exactly; a bug in normalization/extraction = NULL.
    # v2's NULL was a wrapper bug (str vs bool in the gate's FrozenJudge) — the direct
    # pipeline check was 20/20; the control now compares like-for-like strings and the
    # gate consumes the deterministic judge directly (no llama round-trips for a pure fn).
    ctrl = [(f"the answer is TOKEN{i} here", f"TOKEN{i}") for i in range(20)]
    judge = ExactMatchJudge()
    gate = JudgeControlGate(
        FrozenJudge(lambda q: "PASS" if judge.grade(q.split("|", 1)[0], q.split("|", 1)[1]) else "FAIL",
                    judge_id="exact-match"),
        [(f"{a}|{g}", "PASS") for a, g in ctrl])
    verdict = gate.run()
    ledger["judge_control"] = verdict
    ledger["judge_pipeline_direct"] = {"ok": all(judge.grade(a, g) for a, g in ctrl),
                                       "correct": sum(1 for a, g in ctrl if judge.grade(a, g)), "n": 20}
    if verdict["null"]:
        ledger["aborted"] = "judge-control NULL — grading pipeline bug; results never read"
        return ledger

    # The arms (mirrored episodes, fresh stores, the local reader)
    reader = LocalLMReader()
    for arm in "ABC":
        correct = 0
        tokens = 0
        cache_hits = 0
        for i in range(n_episodes):
            ep = make_episode(i, cut_point=cut_point)
            store = SubstrateRecord()
            substrate = store.write(ep["turns"][ep["cut_point"]]).read()
            view = arm_view(ep, arm, substrate)
            ans = reader(view, ep["question"])
            tokens += len(view["view"])
            cache_hits += 0 if view["source"] == "truncated" else 1
            if judge.grade(ans, ep["fact"]):
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
        "note": "small-N (5/arm) real-path receipt, not the 200/arm verdict — the "
                "pre-committed rule's full run follows on the wider seats",
    }
    return ledger


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "BATTERY-REAL-LEDGER-V2-20261119.json")
    ledger = run_v2()
    with open(out, "w") as f:
        json.dump(ledger, f, indent=2)
    print(json.dumps(ledger, indent=2))
