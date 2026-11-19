"""test_battery_pilot.py — F4's machinery tests: the battery's arms behave as designed."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes.battery_pilot import arm_view, make_episode, run_pilot, StubReader  # noqa: E402


class TestEpisodeClass(unittest.TestCase):
    def test_fact_planted_once_after_cut_point(self):
        ep = make_episode(1, cut_point=6)
        self.assertIn("PLANTED:", ep["turns"][ep["cut_point"]])
        self.assertNotIn("PLANTED:", " ".join(ep["turns"][: ep["cut_point"]]))

    def test_mirrored_across_arms(self):
        """The same episode seed gives the same fact everywhere; only the channel differs."""
        ep = make_episode(7, cut_point=6)
        a, c, b = arm_view(ep, "A"), arm_view(ep, "C"), arm_view(ep, "B", "fact-a1b2c3d4e5f6")
        self.assertFalse(a["fact_available"])
        self.assertTrue(c["fact_available"])
        self.assertEqual(c["source"], "oracle")
        self.assertEqual(b["source"], "substrate")


class TestArmSemantics(unittest.TestCase):
    def test_truncated_cannot_answer(self):
        reader = StubReader()
        ep = make_episode(3, cut_point=6)
        view = arm_view(ep, "A")
        self.assertEqual(reader(view), "UNKNOWN")

    def test_oracle_answers(self):
        reader = StubReader()
        ep = make_episode(3, cut_point=6)
        view = arm_view(ep, "C")
        self.assertIn(ep["fact"], reader(view))

    def test_substrate_answers_when_record_holds_the_fact(self):
        reader = StubReader()
        ep = make_episode(3, cut_point=6)
        substrate = " ".join([ep["turns"][ep["cut_point"]]])
        view = arm_view(ep, "B", substrate)
        self.assertIn(ep["fact"], reader(view))


class TestPilotLedger(unittest.TestCase):
    def test_pilot_runs_and_logs_all_arms(self):
        ledger = run_pilot(n_episodes=5, cut_point=6)
        self.assertTrue(ledger["pilot"])
        self.assertIn("A", ledger["arms"])
        self.assertIn("B", ledger["arms"])
        self.assertIn("C", ledger["arms"])
        # machinery shapes: accuracy, tokens, cache-hit rows all present
        for arm in "ABC":
            row = ledger["arms"][arm]
            self.assertIn("accuracy", row)
            self.assertIn("tokens", row)
            self.assertIn("cache_hit_rate", row)
        self.assertIn("B_minus_A", ledger["decision_rule"])
        self.assertIn("stub", ledger["decision_rule"]["rule"].lower())


if __name__ == "__main__":
    unittest.main()
