"""test_release_point_gate.py — F2's probe battery: the release-point rule's tests.

RED-before-GREEN expected states: the assertions fail if the gate is not
implemented (module absent = RED); GREEN when this fixture rides the gate.
The gate's rollback (GOVERNED_COMPACTION_RELEASE_RULE=OFF) is tested below.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes.release_point_gate import LineageRow, CompactionGovernor  # noqa: E402


class TestReleasePointEligibility(unittest.TestCase):
    def setUp(self):
        os.environ.pop("GOVERNED_COMPACTION_RELEASE_RULE", None)

    def test_no_release_event_not_eligible(self):
        row = LineageRow("block-1")  # no release_event_id, no final_use_ts
        self.assertFalse(row.is_archive_eligible())
        gov = CompactionGovernor()
        self.assertEqual(gov.decide(row), "keep")  # stays hot — never silently archived

    def test_bound_event_is_eligible(self):
        row = LineageRow("block-2", release_event_id="deadbeefdeadbeef00", final_use_ts=1700000000)
        self.assertTrue(row.is_archive_eligible())
        gov = CompactionGovernor()
        self.assertEqual(gov.decide(row), "archive")

    def test_short_event_id_not_citable(self):
        row = LineageRow("block-3", release_event_id="tiny", final_use_ts=1700000000)
        self.assertFalse(row.is_archive_eligible())

    def test_override_stubs_without_witness(self):
        row = LineageRow("block-4", override=True)
        self.assertFalse(row.is_archive_eligible())  # override ≠ witness
        gov = CompactionGovernor()
        self.assertEqual(gov.decide(row), "stub")  # stubs, never archives without the witness

    def test_gate_off_restores_pre_f2_behavior(self):
        os.environ["GOVERNED_COMPACTION_RELEASE_RULE"] = "OFF"
        gov = CompactionGovernor()
        row = LineageRow("block-5", release_event_id="deadbeefdeadbeef00", final_use_ts=1700000000)
        # flag off = the two-way door's rollback: the gate does not block
        self.assertEqual(gov.decide(row), "stub")


if __name__ == "__main__":
    unittest.main()
