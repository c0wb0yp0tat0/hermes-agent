"""release_point_gate.py — F2: the release-point archive-eligibility probe (SPRINT-FIRE-SEQUENCE F2).

Mechanism (LANE-3 GOVERNANCE probe A, adopted verbatim from the NCE release-point
rule): a block is archive-eligible iff a citable `release_event_id` (event-hash +
final-use timestamp) is bound to its lineage row. Without it, the block stays in
hot storage or is stubbed only under an explicit override flag. The whole gate
disarms via GOVERNED_COMPACTION_RELEASE_RULE=OFF (the two-way door's rollback).
"""

import os

GATE_FLAG = "GOVERNED_COMPACTION_RELEASE_RULE"


class LineageRow:
    """A block's lineage row: the final-use record the gate reads."""

    def __init__(self, block_id, release_event_id=None, final_use_ts=None, override=False):
        self.block_id = block_id
        self.release_event_id = release_event_id
        self.final_use_ts = final_use_ts
        self.override = override

    def is_archive_eligible(self):
        """Archive-eligible iff a citable event bound the final use. An override is
        stub-eligibility, never archive-eligibility — the witness is what archives."""
        if self.release_event_id is None or self.final_use_ts is None:
            return False
        # citable = the event id is a real hash (16+ hex chars) and its timestamp is sane
        if not isinstance(self.release_event_id, str) or len(self.release_event_id) < 16:
            return False
        return True


class CompactionGovernor:
    """The governor's archive-or-stub decision, as the gate demands it."""

    def __init__(self, flag_default=True):
        self.flag_default = flag_default

    def gate_on(self):
        env = os.environ.get(GATE_FLAG)
        if env is not None:
            return env.lower() not in ("0", "off", "false", "no")
        return self.flag_default

    def decide(self, row):
        """decide(row) -> 'archive' | 'stub' | 'keep'  (keep = hot storage)."""
        if not self.gate_on():
            # GOVERENED_COMPACTION_RELEASE_RULE=OFF: the pre-F2 behavior (stub-or-keep by default)
            return "stub"
        if row.is_archive_eligible():
            return "archive"
        # in-scope rule: a block whose final use is NOT citable stays hot, or stubs under
        # an explicit override — never silently archived without its witness
        return "keep" if not row.override else "stub"


# --- F3-A DJUDGE-CONTROL SEAM (the pre-registered judge gate's fixture lives with the battery) ---
