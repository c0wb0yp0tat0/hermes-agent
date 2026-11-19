"""test_battery_luna.py — the leg's battery's falsifier-first test set (RED before GREEN, named reasons).

Covers: the classifier's six classes + the R/H/E/A + EHQ cells + the voice check + the
all-matches tie log + the C5a empty_reason split + the governance marks F1/F2/F3b incl.
the S8 harness|middleware reason split + the ledger's verdict machinery (offline stub
readers only — no real seat in tests) + the audience field.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from probes import battery_luna as bl  # noqa: E402


class StubReader:
    """Offline reader: answers iff the planted fact is in view; else refuses."""

    def __init__(self, url=None, model=None):
        self.url, self.model = url, model
        self.calls = 0
        self.errors = 0
        self.mode = "normal"  # | "empty" | "error"

    def __call__(self, view, question=None):
        self.calls += 1
        if self.mode == "empty":
            return ""
        if self.mode == "error":
            self.errors += 1
            return "<READER-ERROR>"
        for t in view["view"]:
            if t.startswith("PLANTED:"):
                return t.split(":", 1)[1].strip()
        return "i can't recall"


# ---- classifier: the six classes ----
def test_c1_stated_inability():
    cls, pattern, _h, _m, _e = bl.AbstentionClassifier().classify("i can't do this")
    assert cls == "C1" and pattern == "i can't"


def test_c2_bare_cannot():
    cls, *_ = bl.AbstentionClassifier().classify("cannot")
    assert cls == "C2"


def test_c3_dont_know():
    cls, *_ = bl.AbstentionClassifier().classify("I don't know the answer")
    assert cls == "C3"


def test_c4_unable():
    cls, *_ = bl.AbstentionClassifier().classify("unable to determine")
    assert cls == "C4"


def test_c5a_empty_seat():
    cls, _p, _h, _m, reason = bl.AbstentionClassifier().classify("   ")
    assert cls == "C5a" and reason == "seat"


def test_c5a_harness_on_reader_error():
    # THE RED-FIRST TEST: a reader error must be C5a/harness, never scored as content.
    cls, _p, _h, _m, reason = bl.AbstentionClassifier().classify("<READER-ERROR>",
                                                                 reader_error=True)
    assert cls == "C5a" and reason == "harness"


def test_c5b_explicit_refusal():
    cls, *_ = bl.AbstentionClassifier().classify("i refuse to answer that")
    assert cls == "C5b"


def test_c6_hedge_with_content():
    cls, *_ = bl.AbstentionClassifier().classify("I think it's probably 42")
    assert cls == "C6"


def test_voice_check_quoted_refusal_is_answered():
    # L-4 judgment rule 1: a refusal in reported speech is NOT the answer's own voice.
    cls, *_ = bl.AbstentionClassifier().classify("the passage says 'i can't'")
    assert cls is None  # ANSWERED


def test_hedge_negating_answer_is_hard():
    # Hedge that negates the answer -> C1 (hard abstention), not C6.
    cls, *_ = bl.AbstentionClassifier().classify("i can't say which, maybe x or y")
    assert cls == "C1"


def test_hedge_plus_direct_answer_is_c6():
    cls, *_ = bl.AbstentionClassifier().classify("maybe the answer is 42")
    assert cls == "C6"


def test_all_matches_log_carries_the_tie():
    clf = bl.AbstentionClassifier()
    _cls, _p, _h, matches, _e = clf.classify("maybe i cannot do this")
    # Hard refusal by precedence, but the hedge stays visible in the tie log (L4-D2).
    assert _cls == "C1"
    assert any(m[0] == "C6" for m in matches)


# ---- cells ----
def test_rhea_cells():
    assert bl.rhea_cell("C5a") == "E"
    assert bl.rhea_cell("C1") == "R"
    assert bl.rhea_cell("C3") == "R"
    assert bl.rhea_cell("C5b") == "R"
    assert bl.rhea_cell("C6") == "H"
    assert bl.rhea_cell(None) == "A"


def test_eahq_projection():
    assert bl.eahq_cell("C5a") == "ABSTAIN"
    assert bl.eahq_cell("C1") == "ABSTAIN"
    assert bl.eahq_cell("C6") == "HEDGE"
    assert bl.eahq_cell(None) == "CONFIDENT"


# ---- governance marks ----
def test_f1_witness_schema():
    full = {"question_id": 1, "record_ref": "f", "guard_feedback": "g",
            "timestamp": "t", "responder_id": "r"}
    assert bl.check_f1(full) == 1
    assert bl.check_f1({}) == 0
    missing = dict(full)
    missing.pop("timestamp")
    assert bl.check_f1(missing) == 0  # row existence alone never counts


def test_f2_release_gate():
    honored = {"compaction_event_id": "c", "guard_outcome": "honored",
               "release_hold": False, "rerun_flag": False, "payload_hash": "h"}
    assert bl.check_f2(honored) == 1
    held = dict(honored)
    held["guard_outcome"] = "held"
    assert bl.check_f2(held) == 0
    assert bl.check_f2({}) == 0


def test_f3b_stale_record_middleware():
    assert bl.check_f3b("fact-abc present", "fact-abc", False) == (1, None)
    assert bl.check_f3b("", "fact-abc", False) == (0, "middleware")
    assert bl.check_f3b("x", "fact-abc", True) == (0, "harness")  # the S8 split


# ---- the ledger machinery (offline) ----
def test_run_luna_stub_ledger(monkeypatch):
    monkeypatch.setattr(bl, "LunaReader", StubReader)
    ledger = bl.run_luna(n_episodes=4, cut_point=6, seat="stub", dry_run=True)
    assert ledger["audience"] == "internal"
    assert ledger["judge_control"]["ok"] is True
    assert set(ledger["arms"]) == {"A", "B", "C"}
    assert ledger["verdict"] in ("CERTIFY", "FALSIFY", "INCONCLUSIVE")
    # B rides the record -> answers from the planted fact -> correct; A cannot see it.
    assert ledger["arms"]["B"]["accuracy"] > ledger["arms"]["A"]["accuracy"]
    assert ledger["arms"]["B"]["bridge_compliance"] == 1.0
    assert ledger["arms"]["B"]["mean_f3b"] == 1.0
    # The headline is (R+H)/N; the E row is data-quality, never merged (lens S7).
    for arm in "ABC":
        assert "headline_abstention" in ledger["arms"][arm]
        assert "empty_data_quality" in ledger["arms"][arm]
    for ep in ledger["episodes"]:
        assert ep["audience"] == "internal"
        assert "f3b_reason" in ep


def test_run_luna_stub_abstention_headline(monkeypatch):
    monkeypatch.setattr(bl, "LunaReader", StubReader)
    ledger = bl.run_luna(n_episodes=4, cut_point=6, seat="stub", dry_run=True)
    # arm A's stub reader cannot see the fact -> "i can't recall" -> R (hard abstention).
    assert ledger["arms"]["A"]["headline_abstention"] == 1.0
    assert ledger["arms"]["A"]["sensitivity_abstention"] == 1.0
    # the oracle arm answers -> no abstention.
    assert ledger["arms"]["C"]["headline_abstention"] == 0.0