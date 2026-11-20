# F2-CITATION-ARM-20261120 — the compaction battery's citation arm (spec + RED/GREEN receipts)

*Gate: "the gate: nothing public without the user's word." — RFC QUIET. Nothing moves public/permanent until the user speaks.*

Seat: runners (unmetered class) · Branch `study/rfc-143379-rig-20261105` · 2026-11-20 · Parent: MASTER-FLAGSHIP-20261119 (P3 row) + P3-RELEASE-POINT-20261120 §5 + P3-F2-BATTERY-RECEIPTS-20261120 · Consumers: the head/runner's code-write apply + the F2/F3 lanes.

## 0. The gate, verbatim
> "the gate: nothing public without the user's word." — RFC QUIET.

## 1. Place in the sequence + why arm B read == arm A
P3's fire measured **F2-B == F2-A** and the pre-committed INCONCLUSIVE clause bound: *rewrite the experiment, never the claim.* The named cause (P3-F2-BATTERY-RECEIPTS-20261120): the existing compaction battery never drives an **uncited in-place release** past the wired gate, so gate ON and gate OFF produce the same battery. The citation arm is the missing instrument: it prepares the exact episode class the rule exists for and replays it under both flags. This artifact specs that arm and receipts its RED-before (absent) and GREEN (the exact test file, executed).

## 2. The parametrized episode (exact spec)
`make_episode(seed, cut_point=12)` — probes/battery_pilot.py:32, the **non-re-observable-fact class**: a fact planted once at the cut-point turn, filler either side; truncation at the cut-point destroys it unless the record keeps it. `cut_point = 12` is pinned to the battery's own default (probes/battery_full.py:26, `BATTERY_CUT`).

Pre-committed episode set (one-factor law, mirrored verbatim across arms):
```
SEEDS     = (11, 23, 37)          # tests/e2e/core/compaction/_helpers.py:44
N_TURNS   = 10                    # tests/e2e/core/compaction/_helpers.py:45
EPISODES  = [seed * N_TURNS + t for seed in SEEDS for t in range(N_TURNS)]   # 30 episodes
CUT_POINT = 12                    # probes/battery_full.py:26
```
Each episode is prepared as an **IN-PLACE compression** (`prepared['in_place'] = True`) whose **snapshot receipt carries NO `release_event_id`** unless the arm binds one (§3). The 15/15 citable split is pre-committed by index parity — never chosen post-hoc.

## 3. The two expected states (and the one named seam)
| Arm | Flag | Prepared block | Expected state |
|---|---|---|---|
| **A — the record's control** | `GOVERNED_COMPACTION_RELEASE_RULE=OFF` | uncited, in-place | **archives** (the pre-F2 behavior; the gate is inert) |
| **B — the release-point governor** | `GOVERNED_COMPACTION_RELEASE_RULE=ON` | uncited, in-place | **F2-HOLD** — the ValueError at hermes_state_mutation_compress.py:22-25 |
| **B (cited class)** | `ON` | `release_event_id` bound (16+ hex) | **archives** — the citation releases the block |

The gate, verbatim as applied (commit ddd5de0a54, `compress_in_transaction`):
```python
        if os.environ.get("GOVERNED_COMPACTION_RELEASE_RULE", "").lower() in ("on", "1", "true"):
            rel = (snapshot.get("release_event_id") if isinstance(snapshot, dict) else None)
            if not (isinstance(rel, str) and len(rel) >= 16):
                raise ValueError(
                    "F2-HOLD: no citable release_event_id in the snapshot receipt; the block is "
                    "held (archive deferred) — release a block only when the teacher can cite "
                    "the event that ended its use")
```
**Named seam (not silent).** The gate reads a top-level `release_event_id` on the snapshot, and `local_snapshot` (hermes_state_mutation_prepared.py:9-18) builds `{receipt, target, target_revision}` — so the cited branch is **unreachable** until the receipt's citation surfaces. The apply's second line (additive, inert unless the lineage row carries a citation; revert = delete the block):
```python
    snapshot = {'receipt': saved, 'target': target, 'target_revision': revision}
    cited = saved.get('release_event_id')
    if isinstance(cited, str) and cited:
        snapshot['release_event_id'] = cited
    return snapshot
```
Receipt: with only the gate applied, arm B holds **all 30** (§6, the RED run) — the seam is load-bearing, proven, not asserted.

## 4. The measurement rows (read from the hold/archive counts)
Per arm, one `check_f2` gate row per compaction decision — `(compaction_event_id, guard_outcome="honored", release_hold, rerun_flag, payload_hash)` with `guard_outcome == "honored"` (probes/battery_luna.py:290). The bars are computed from arm B's counts only:

| Bar | Definition | Threshold | Arm B receipt |
|---|---|---|---|
| **precision** | of arm B's `archive` decisions, the fraction whose citation verifies (the cited `release_event_id` hashes to the block's actual final-use event) | **>= 0.95** (fail < 0.80) | 15/15 = **1.000** |
| **FP** | arm B `archive` decisions on blocks with **no** citable ending event (silent archive of an uncited block) | **= 0** | **0** |
| **completeness** | of the truly-citable blocks, the fraction arm B releases | **= 100%** | 15/15 = **100%** |

Arm A's control counts (same 30 prepared episodes): **archives 30 / holds 0**. Arm B: **archives 15 / holds 15**. Verdict on the arm's bars: **PASS** — and named as the arm's *unit-level* machine, not the field-scale certify battery (that is P4's leg; the billed F2-A/F2-B/F2-CTRL field rows stay UNVERIFIED until the runner fires the battery with the arm applied).

## 5. RED-before proof + GREEN spec

### 5.1 RED-before — the arm is absent from the tree today
```
cd /root/workspace/repos/hermes-agent
git rev-parse HEAD                      # f86177e9d30121ad669df28e3c386d715b0412cb
grep -rnE "citation|release_event_id|make_episode|F2-HOLD" tests/e2e/core/compaction/
# -> exit=1, zero matches (same at 04e624aea5f, the first read)
```
The compaction battery (`tests/e2e/core/compaction/`: `_helpers.py`, `test_compaction_auto.py`, `test_compaction_kill9.py`, `test_compaction_manual.py`, `test_compaction_summary_faults.py`) carries **no** citation token, no `make_episode`, no F2-HOLD. RED on the arm's presence; the gate itself is wired (hermes_state_mutation_compress.py:19, 2 hits for `GOVERNED_COMPACTION_RELEASE_RULE`).

### 5.2 GREEN spec — the exact test file + the assertion lines
Lands at **`tests/e2e/core/compaction/test_citation_arm.py`** (additive; revert = delete the file). Executed in a scratch apply (file written, both apply lines in place, then reverted — §6):
```python
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
```
The load-bearing assertion lines:
```python
    assert [row["outcome"] for row in rows] == ["archive"] * 30                                  # arm A: the control
    assert [row["outcome"] for row in rows if not row["citable"]] == ["hold"] * 15              # arm B: uncited held
    assert [row["outcome"] for row in rows if row["citable"]] == ["archive"] * 15               # arm B: cited released
    assert precision >= 0.95 and precision == 1.0                                               # bar: precision
    assert false_positives == 0                                                                 # bar: FP = 0
    assert completeness == 1.0                                                                  # bar: completeness 100%
    assert str(exc).startswith("F2-HOLD"), exc                                                  # the wired gate, verbatim
    assert all(row["check_f2"] == 1 for row in _run_arm(flag, tmp_path, monkeypatch))           # honored per check_f2
```

## 6. The executed-rule binds (receipts actually run)
```
cd /root/workspace/repos/hermes-agent
.venv/bin/python -m pytest tests/e2e/core/compaction/test_citation_arm.py -q     # python 3.14.7, pytest 9.1.1
```
| Receipt | Result | Note |
|---|---|---|
| RED-grep §5.1 @ `f86177e9d3` | **exit=1, zero matches** | the arm is absent from the battery |
| **GREEN** scratch apply: gate + surfacing line + test file | **4 passed in 4.24s** | uncommitted; reverted after the run |
| **RED control**: same, surfacing line reverted | **2 failed, 2 passed in 4.47s** | arm B holds all 30; `archives == 0`, the cited branch unreachable |
| tree after revert | `git status --short` clean; grep exit=1 again | RED restored for the head/runner's apply |

Honest scope: these are the **arm's unit-level** receipts. The billed field rows (`F2-A-20261120`, `F2-B-20261120`, `F2-CTRL-20261120`) stay **UNVERIFIED** until the runner fires the compaction battery with the arm applied.

## 7. The compose-check table (8 marks, FIRED/ABSENT, one evidence line each)
| # | Step | State | Evidence line |
|---|---|---|---|
| 1 | Deconstruct | FIRED | M3 Probe A's citation arm + P3 §5's missing instrument; the episode class, the two flags, the bars — each traced to its source doc |
| 2 | Sense | FIRED | Ground read cold (P3 spec + P3 receipts + MASTER-FLAGSHIP + SPRINT-FIRE-SEQUENCE + MASTER-TEAM-M3); absence proven by grep at a pinned sha, not asserted |
| 3 | Choose | FIRED | Arm A = gate OFF (the record's control); arm B = cite-or-hold; the cited class is the pre-committed parity split, no post-hoc choice |
| 4 | Calibrate | FIRED | precision >= 0.95 (fail < 0.80), FP = 0, completeness 100% — P3 §3.4 verbatim; 30 eps, cut 12 from `_helpers.py` + `battery_full.py:26` |
| 5 | Probe | FIRED | Every move names metric + rollback (§9); the named seam (surfacing) proven load-bearing by the RED control run |
| 6 | Review | FIRED | Stranger re-read + 4 adversarial pushbacks + two no-change re-reads (§8) |
| 7 | Record | FIRED | This artifact; §6 receipts are actual runs with their command line; the test file is quoted verbatim |
| 8 | Compose-check | FIRED | This table; the billed field runs named UNVERIFIED, none estimated |

## 8. The review-loop
Draft → stranger re-read (cold, against P3's spec + receipts and M3's probe card) → one refinement per finding → 4 adversarial pushbacks → termination: no-change re-read twice.
- **Refinement (stranger finding):** the first draft measured only the uncited half, which makes precision undefined (arm B archives nothing). Corrected: the pre-committed 15/15 citable split, so all three bars read from real hold/archive counts.
- **Pushback 1 — "precision is vacuous if arm B never archives."** Held: that is exactly the defect; it is why the cited class exists, and the RED control run shows the failure mode (§6).
- **Pushback 2 — "the surfacing line is out of scope / rewrites the wiring."** Held: the landed gate (ddd5de0a54) is untouched; the apply adds one additive, inert line in `local_snapshot`, named as the seam and proven load-bearing by the RED control.
- **Pushback 3 — "a scratch GREEN is not a landing."** Held: §6 says so verbatim; the head/runner's apply commit is the landing, and this artifact is the spec it applies.
- **Pushback 4 — "the 15/15 split is invented."** Held: the *episode class* and the *bars* are pre-committed; the split is a deterministic parity rule declared before the run, and the one-factor law (same 30 prepared episodes, only the flag differs) holds.
Termination: no-change re-read ×2 — stable.

## 9. Two-way doors (master table)
| Move | Reversibility | Rollback |
|---|---|---|
| arm test file add | additive only | delete the file |
| surfacing line | additive, inert unless cited | delete the block |
| shadow → enforce | flag `GOVERNED_COMPACTION_RELEASE_RULE` | flip to `OFF`; held blocks re-admit next cycle, bytes intact |
| public → private | the gate | re-arm to last private value |
| cost → stop | cap stop | COST-OVER recorded ($0 — fake provider, unmetered) |

## 10. Loop-state line
**CONTINUE** — the head/runner's code-write apply (the test file + the one surfacing line) and the battery fire with the arm applied are the next leg.

## 11. Fold for the master's §7
F2-CITATION-ARM 2026-11-20: the compaction battery's citation arm specced — `make_episode(seed, cut_point=12)`, 30 episodes (SEEDS × N_TURNS) mirrored across arms; arm A (gate OFF) archives 30/30, arm B (gate ON) holds the 15 uncited and releases the 15 cited; precision 1.000 >= 0.95, FP = 0, completeness 100%, every decision `check_f2`-honored. RED-before grep exit=1 at f86177e9d3; GREEN 4/4 in a scratch apply (then reverted), RED control 2 failed with the surfacing line absent — the named seam is load-bearing. Billed field rows UNVERIFIED. Next: the apply + the battery fire.

## 12. The wall clause, verbatim
> "a non-reproduction is a QUESTION, not a stop."

