"""test_judge_control_gate.py — F3's battery: the judge-control gate's tests."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes.judge_control_gate import FrozenJudge, JudgeControlGate  # noqa: E402


def make_control(n=20):
    return [(f"q{i}", f"gold{i}") for i in range(n)]


class TestJudgeControlGate(unittest.TestCase):
    def test_good_judge_passes(self):
        judge = FrozenJudge(lambda q: {"q0": "gold0", "q19": "gold19"}.get(q, q.replace("q", "gold")))
        gate = JudgeControlGate(judge, make_control())
        verdict = gate.run()
        self.assertTrue(verdict["ok"])
        self.assertFalse(verdict["null"])
        self.assertGreaterEqual(verdict["accuracy"], 0.90)

    def test_bad_judge_nulls_the_run(self):
        judge = FrozenJudge(lambda q: "wrong-answer")
        gate = JudgeControlGate(judge, make_control())
        verdict = gate.run()
        self.assertFalse(verdict["ok"])
        self.assertTrue(verdict["null"])  # the run is void — results never read

    def test_unfrozen_judge_refused(self):
        judge = FrozenJudge(lambda q: "gold0", judge_id="unfrozen")
        with self.assertRaises(RuntimeError):
            judge.answer("q0")

    def test_refreeze_gives_second_chance(self):
        judge = FrozenJudge(lambda q: "wrong-answer")
        gate = JudgeControlGate(judge, make_control())
        first = gate.run()
        self.assertTrue(first["null"])
        second = gate.refreeze(lambda q: q.replace("q", "gold"))
        self.assertTrue(second["ok"])
        self.assertNotEqual(first["judge_fingerprint"], second["judge_fingerprint"])

    def test_gate_is_read_only(self):
        """The gate itself never alters the control set or the judge's fingerprint."""
        judge = FrozenJudge(lambda q: q.replace("q", "gold"))
        fp_before = judge.fingerprint_of()
        gate = JudgeControlGate(judge, make_control())
        gate.run()
        fp_after = judge.fingerprint_of()
        self.assertEqual(fp_before, fp_after)  # freezing is identity, not mutation


if __name__ == "__main__":
    unittest.main()
