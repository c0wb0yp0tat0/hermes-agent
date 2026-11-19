"""judge_control_gate.py — F3: the judge-control gate (SPRINT-FIRE-SEQUENCE F3).

Pre-registered rule (LANE-1 §3 + NOTE-5 mis-scoring class): before the battery's
results are read, the frozen judge is checked on a 20-episode control set with
known answers. Control accuracy < 90% → the run is NULL and the judge is refrozen
before re-running. Re-scoring is a pre-registered gate, never an afterthought.
Rollback: the gate is a read-only check; the refreeze is its only write.
"""

import hashlib
import json
import os
import time

CONTROL_MIN_ACCURACY = float(os.environ.get("JUDGE_CONTROL_MIN_ACCURACY", "0.90"))


class FrozenJudge:
    """The judge: a frozen responder (a model seat or a deterministic stub in the
    battery's pilot). The pilot uses a STUB judge so the gate itself is testable;
    the battery swaps in the frozen model seat."""

    def __init__(self, responder, judge_id=None):
        self.responder = responder  # callable(q) -> answer
        self.fingerprint = hashlib.sha256(
            (judge_id or repr(responder)).encode()).hexdigest()[:16]
        self.frozen = False

    def freeze(self):
        self.frozen = True
        return self.fingerprint

    def answer(self, question):
        if not self.frozen:
            raise RuntimeError("judge not frozen — the gate refuses unfrozen answers")
        return self.responder(question)

    def fingerprint_of(self):
        return self.fingerprint


class JudgeControlGate:
    """The pre-registered gate: a 20-episode control set, frozen judge, >=90% or NULL."""

    def __init__(self, judge, control_set, min_accuracy=CONTROL_MIN_ACCURACY):
        self.judge = judge
        self.control_set = control_set  # [(question, gold_answer), ...]
        self.min_accuracy = min_accuracy
        self.result = None  # {"ok": bool, "accuracy": float, "null": bool, "ts": str}

    def run(self):
        """Run the control check; returns the verdict row. NULL when accuracy < min."""
        judge_id = self.judge.freeze()
        correct = 0
        total = len(self.control_set)
        for q, gold in self.control_set:
            try:
                if self.judge.answer(q) == gold:
                    correct += 1
            except Exception:
                pass
        accuracy = correct / total if total else 0.0
        ok = accuracy >= self.min_accuracy
        self.result = {
            "ok": ok,
            "accuracy": round(accuracy, 4),
            "null": not ok,  # NULL = the run is void, judge must be refrozen
            "judge_fingerprint": judge_id,
            "control_n": total,
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        return self.result

    def refreeze(self, new_responder):
        """The only write the gate allows: a refrozen judge on the same control set."""
        self.judge = FrozenJudge(new_responder)
        return self.run()
