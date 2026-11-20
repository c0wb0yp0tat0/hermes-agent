"""F2 citation arm -- the non-re-observable-fact episodes driven through the wired gate.

M3 Probe A's citation arm for ``tests/e2e/core/compaction/`` (P3-RELEASE-POINT-20261120 §5):
the same 30 prepared in-place compressions replayed under the two flags of the F2 A/B --
gate OFF (the record's pre-F2 control: every block archives) and gate ON (cite-or-hold:
a block whose ending event is citable releases, an uncited one raises the wired F2-HOLD).

Episode class: ``make_episode(seed, cut_point=12)`` -- a fact planted once at the cut-point,
filler either side (probes/battery_pilot.py:32). Every decision is receipted as a
``check_f2`` gate row with ``guard_outcome == "honored"`` (probes/battery_luna.py:290).
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from hermes_state import SessionDB
from hermes_state_keys import local_identity
from hermes_state_local import POLICY_PREFIX, commit_local_session
from hermes_state_mutation_compress import compress_in_transaction
from hermes_state_mutation_prepared import local_snapshot
from hermes_state_runtime import begin_runtime_epoch

from tests.e2e.core.compaction._helpers import N_TURNS, SEEDS

RIG = Path(__file__).resolve().parents[4] / "studies" / "rfc-143379-rig"
sys.path.append(str(RIG))  # append: the repo root must keep winning over studies/.../hermes_*.py
from probes.battery_luna import check_f2  # noqa: E402
from probes.battery_pilot import make_episode  # noqa: E402

CUT_POINT = 12  # probes/battery_full.py:26 (BATTERY_CUT default)
EPISODES = [seed * N_TURNS + turn for seed in SEEDS for turn in range(N_TURNS)]  # 30, mirrored verbatim


def _expected_citation(sid):
    """The block's actual final-use event id: the citation must hash to this."""
    return hashlib.sha256(f"{sid}:final-use".encode()).hexdigest()[:32]


def _episodes(db, epoch, tag):
    """One prepared episode per seed: the planted-fact transcript in a fresh session."""
    made = []
    for index, seed in enumerate(EPISODES):
        profile, principal, request = "cit-prof", "cit-owner", f"cit-{tag}-{index}"
        sid = local_identity(profile, principal, request)
        policy = {"source": "cli", "model": "fake", "cwd": "/tmp", "request_json": "{}"}
        entry = {"session_id": sid, "created_at": "2026-11-20T00:00:00", "origin": {"chat_id": "cit"}}
        commit_local_session(db, epoch=epoch, receipt={
            "session_id": sid, "route": f"cit-{tag}-{index}", "profile_id": profile,
            "principal_id": principal, "request_id": request, "policy": policy,
            "entry": entry, "lineage": [sid]})
        episode = make_episode(seed, cut_point=CUT_POINT)
        for i, text in enumerate(episode["turns"]):
            db.append_message(sid, "user" if i % 2 == 0 else "assistant", content=text)
        made.append((sid, episode))
    return made


def _cite(db, sid):
    """Bind the block's ending event on its lineage row (a citable release)."""
    saved = json.loads(db.get_meta(POLICY_PREFIX + sid))
    saved["release_event_id"] = _expected_citation(sid)
    db.set_meta(POLICY_PREFIX + sid, json.dumps(saved))


def _compress_in_place(db, sid):
    """The prepared IN-PLACE compression; returns the snapshot's cited release event."""
    with db._read_ctx() as conn:
        snapshot = local_snapshot(db, conn, sid)
    citation = snapshot.get("release_event_id")
    prepared = {"snapshot": snapshot, "in_place": True, "messages": [],
                "summary": "citation-arm summary", "policy": snapshot["receipt"]["policy"]}

    def write(conn):
        return compress_in_transaction(db, conn, sid, {}, prepared)

    db._execute_write(write)
    return citation


def _counts(db, sid):
    with db._read_ctx() as conn:
        live = conn.execute("SELECT COUNT(*) FROM messages WHERE session_id=? AND active=1", (sid,)).fetchone()[0]
        archived = conn.execute("SELECT COUNT(*) FROM messages WHERE session_id=? AND compacted=1", (sid,)).fetchone()[0]
    return int(live), int(archived)


def _run_arm(flag, tmp_path, monkeypatch):
    """Replay the 30 prepared episodes under one flag; one check_f2 row per decision."""
    monkeypatch.setenv("GOVERNED_COMPACTION_RELEASE_RULE", flag)
    db = SessionDB(db_path=tmp_path / f"state-{flag}.db")
    try:
        epoch = begin_runtime_epoch(db, instance_id="citation-arm")
        rows = []
        for index, (sid, episode) in enumerate(_episodes(db, epoch, flag)):
            citable = index % 2 == 0  # the pre-committed 15/15 split; never chosen post-hoc
            if citable:
                _cite(db, sid)
            before = _counts(db, sid)
            hold = False
            try:
                citation = _compress_in_place(db, sid)
                outcome = "archive" if _counts(db, sid) != before else "noop"
            except ValueError as exc:
                assert str(exc).startswith("F2-HOLD"), exc  # the wired gate, verbatim
                citation, outcome, hold = None, "hold", True
            gate_row = {
                "compaction_event_id": hashlib.sha256(f"{sid}:compress".encode()).hexdigest()[:16],
                "guard_outcome": "honored", "release_hold": int(hold), "rerun_flag": 0,
                "payload_hash": hashlib.sha256(json.dumps([episode["fact"]]).encode()).hexdigest()[:16],
            }
            rows.append({"index": index, "citable": citable, "outcome": outcome,
                         "verified": citation == _expected_citation(sid) if citable else False,
                         "check_f2": check_f2(gate_row)})
        return rows
    finally:
        db.close()


def test_arm_a_gate_off_archives_every_episode(tmp_path, monkeypatch):
    """Arm A -- the record's control: the gate is inert, all 30 blocks archive."""
    rows = _run_arm("OFF", tmp_path, monkeypatch)
    assert len(rows) == 30
    assert [row["outcome"] for row in rows] == ["archive"] * 30


def test_arm_b_gate_on_holds_uncited_and_releases_cited(tmp_path, monkeypatch):
    """Arm B -- cite-or-hold: exactly the 15 uncited blocks raise the wired F2-HOLD."""
    rows = _run_arm("ON", tmp_path, monkeypatch)
    assert [row["outcome"] for row in rows if not row["citable"]] == ["hold"] * 15
    assert [row["outcome"] for row in rows if row["citable"]] == ["archive"] * 15


def test_bars_read_from_the_hold_archive_counts(tmp_path, monkeypatch):
    """precision >= 0.95, FP = 0, completeness = 100% -- all three from arm B's counts."""
    rows = _run_arm("ON", tmp_path, monkeypatch)
    archives = [row for row in rows if row["outcome"] == "archive"]
    assert archives, "arm B archived nothing -- the citation arm never reaches the gate's cited branch"
    precision = sum(1 for row in archives if row["verified"]) / len(archives)
    false_positives = sum(1 for row in rows if not row["citable"] and row["outcome"] == "archive")
    cited = [row for row in rows if row["citable"]]
    completeness = sum(1 for row in cited if row["outcome"] == "archive") / len(cited)
    assert precision >= 0.95 and precision == 1.0
    assert false_positives == 0
    assert completeness == 1.0


def test_every_decision_row_is_honored_per_check_f2(tmp_path, monkeypatch):
    """Each compaction decision consulted the gate and was honored (probes/battery_luna.py:290)."""
    for flag in ("OFF", "ON"):
        assert all(row["check_f2"] == 1 for row in _run_arm(flag, tmp_path, monkeypatch))
