#!/usr/bin/env python3
"""tasklist_view.py — read-only unified task-list VIEW generator (ASSEMBLY CG-4).

Renders ONE read-only view aggregating the task surfaces so the task-list state
is visible at a glance:

  - KANBAN BOARD (kanban.db, read only via SQLite URI mode=ro): task counts by
    status, assignee, priority; live/running tasks; blocked tasks (with kind);
    recently completed.
  - LANDING LEDGER (landing-ledger.md, read only): live (IN-FLIGHT/QUEUED) and
    folded track rows.
  - MOTION sensor (motion_watch_state.json, read only): tracked-ticket counts by
    state and the most-recently-moved ticket.
  - AB-01 surface (AB01-SERIES.jsonl, read only): latest observation pulse.

This is a VIEW, not a state store: it reads every input, writes only the output
Markdown file. Inputs are opened in read-only mode or parsed from text; no DB
writes, no status mutation, no plugin-data writes. The generated artifact is a
derivative that rides drop_sync / bridge_sync because it lands under the
master-page source tree (--out under master-page/...).

Usage:
  python3 tasklist_view.py                      # real run -> view file
  python3 tasklist_view.py --db FIXTURE.db --out /tmp/scratch/view.md
  python3 tasklist_view.py --now 2026-01-01T00:00:00Z   # deterministic timestamp
  python3 tasklist_view.py --dry-run            # build in memory, print, no write

Exit: 0 success; non-zero on input/hash failure.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Defaults (all read-only inputs)
# ---------------------------------------------------------------------------
DEFAULT_DB = Path("/root/.hermes/kanban.db")
DEFAULT_LEDGER = Path("/root/workspace/master-page/memory-chain/landing-ledger.md")
DEFAULT_MOTION = Path("/root/.hermes/scripts/var/motion_watch_state.json")
DEFAULT_AB01 = Path("/root/workspace/master-page/deepdive-mission-flow/AB01-SERIES.jsonl")
DEFAULT_OUT = Path("/root/workspace/master-page/deepdive-mission-flow/SUSTAINABILITY/TASKLIST-VIEW.md")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def now_iso(now_override: Optional[str]) -> str:
    if now_override:
        return now_override
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fmt_ts_unix(v: Optional[int]) -> str:
    if not v:
        return "—"
    try:
        return datetime.fromtimestamp(int(v), tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, OSError, OverflowError):
        return str(v)


# ---------------------------------------------------------------------------
# READ-ONLY source collectors
# ---------------------------------------------------------------------------
def read_board(db_path: Path) -> Dict[str, Any]:
    """Open the board strictly read-only and gather the view data."""
    if not db_path.exists():
        raise FileNotFoundError(f"board db not found: {db_path}")
    uri = db_path.resolve().as_uri() + "?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    try:
        statuses = conn.execute(
            "SELECT status, COUNT(*) AS n FROM tasks GROUP BY status ORDER BY status"
        ).fetchall()
        status_counts = {r["status"]: r["n"] for r in statuses}

        assignees = conn.execute(
            "SELECT assignee, status, COUNT(*) AS n FROM tasks GROUP BY assignee, status ORDER BY assignee, status"
        ).fetchall()
        assignee_counts: Dict[str, Dict[str, int]] = {}
        for r in assignees:
            a = r["assignee"] or "(none)"
            assignee_counts.setdefault(a, {})[r["status"]] = r["n"]

        priorities = conn.execute(
            "SELECT priority, COUNT(*) AS n FROM tasks GROUP BY priority ORDER BY priority"
        ).fetchall()
        priority_counts = {r["priority"]: r["n"] for r in priorities}

        running = conn.execute(
            "SELECT id, title, assignee, priority, created_at, started_at, "
            "last_heartbeat_at, worker_pid, current_run_id FROM tasks "
            "WHERE status='running' ORDER BY id"
        ).fetchall()

        blocked = conn.execute(
            "SELECT id, title, assignee, priority, block_kind, last_failure_error, "
            "created_at, started_at FROM tasks WHERE status='blocked' ORDER BY id"
        ).fetchall()

        # recently completed (newest first)
        recent_done = conn.execute(
            "SELECT id, title, assignee, completed_at FROM tasks "
            "WHERE status='done' ORDER BY completed_at DESC LIMIT 15"
        ).fetchall()

        # comments count per task for blocked (signal)
        blocked_comments: Dict[str, int] = {}
        for r in blocked:
            c = conn.execute(
                "SELECT COUNT(*) FROM task_comments WHERE task_id=?", (r["id"],)
            ).fetchone()[0]
            blocked_comments[r["id"]] = c

        task_count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        link_count = conn.execute("SELECT COUNT(*) FROM task_links").fetchone()[0]
        comment_count = conn.execute("SELECT COUNT(*) FROM task_comments").fetchone()[0]
    finally:
        conn.close()

    return {
        "task_count": task_count,
        "status_counts": status_counts,
        "assignee_counts": assignee_counts,
        "priority_counts": priority_counts,
        "running": [dict(r) for r in running],
        "blocked": [dict(r) for r in blocked],
        "blocked_comments": blocked_comments,
        "recent_done": [dict(r) for r in recent_done],
        "link_count": link_count,
        "comment_count": comment_count,
    }


def parse_ledger(path: Path) -> Dict[str, Any]:
    rows = []
    if not path.exists():
        return {"path": str(path), "exists": False, "rows": [], "live": [], "folded": [], "error": "missing"}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        return {"path": str(path), "exists": True, "rows": [], "live": [], "folded": [], "error": str(e)}
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 9:
            continue
        ts, track, mission, base, exitc, artifact, fresh, status, verdict = cells[:9]
        if track in ("ts", "---", "track") or not track:
            continue
        if not ts or ts.startswith("---"):
            continue
        rows.append({
            "ts": ts, "track": track, "mission": mission, "base": base,
            "exit": exitc, "artifact": artifact, "fresh": fresh,
            "status": status, "verdict": verdict,
        })
    live = [r for r in rows if r["status"] in ("IN-FLIGHT", "QUEUED")]
    folded = [r for r in rows if r["status"] in ("FOLDED", "SUPERSEDED")]
    return {"path": str(path), "exists": True, "rows": rows, "live": live, "folded": folded, "error": None}


def read_motion(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "exists": False, "tracked": [], "state_counts": {}, "latest": None, "error": "missing"}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return {"path": str(path), "exists": True, "tracked": [], "state_counts": {}, "latest": None, "error": str(e)}
    snap = data.get("snap") or {}
    tracked_list = data.get("tracked") or list(snap.keys())
    # normalize tracked ids (may contain strings)
    tracked_ids = [str(x) for x in tracked_list]
    state_counts: Dict[str, int] = {}
    latest_entry = None
    latest_ts = None
    for tid, info in snap.items():
        st = (info or {}).get("state") or "unknown"
        state_counts[st] = state_counts.get(st, 0) + 1
        ts = (info or {}).get("updated_at")
        if ts and (latest_ts is None or ts > latest_ts):
            latest_ts = ts
            latest_entry = {"id": tid, **(info or {})}
    return {
        "path": str(path),
        "exists": True,
        "tracked_ids": tracked_ids,
        "tracked_count": len(tracked_ids),
        "snapshot_count": len(snap),
        "state_counts": state_counts,
        "latest": latest_entry,
        "latest_ts": latest_ts,
        "error": None,
    }


def read_ab01(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "exists": False, "error": "missing", "latest": None}
    lines = path.read_text(encoding="utf-8").splitlines()
    last = None
    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue
        try:
            last = json.loads(line)
            break
        except json.JSONDecodeError:
            continue
    if last is None:
        return {"path": str(path), "exists": True, "error": "no observations", "latest": None, "lines": len(lines)}
    return {"path": str(path), "exists": True, "error": None, "latest": last, "lines": len(lines)}


# ---------------------------------------------------------------------------
# RENDER
# ---------------------------------------------------------------------------
def render_view(board, ledger, motion, ab01, generated_at: str) -> str:
    out: List[str] = []
    out.append("# UNIFIED TASK-LIST VIEW (read-only, CG-4)")
    out.append("")
    out.append(f"Generated: {generated_at}")
    out.append("Source: read-only aggregation — board (kanban.db), landing ledger, motion sensor, AB-01 pulse.")
    out.append("Invariant: this view STORES nothing; it is derived on demand. No write surface beyond this file.")
    out.append("")

    # ---- Board at a glance ----
    out.append("## Board at a glance")
    out.append("")
    out.append(f"- Tasks total: {board['task_count']}")
    out.append(f"- Task links (parent->child): {board['link_count']}")
    out.append(f"- Task comments: {board['comment_count']}")
    out.append("")
    out.append("### Status counts")
    out.append("")
    if board["status_counts"]:
        for st in sorted(board["status_counts"]):
            out.append(f"- {st}: {board['status_counts'][st]}")
    else:
        out.append("- (none)")
    out.append("")
    out.append("### Assignees (status breakdown)")
    out.append("")
    if board["assignee_counts"]:
        for a in sorted(board["assignee_counts"]):
            parts = ", ".join(f"{k}={v}" for k, v in sorted(board["assignee_counts"][a].items()))
            out.append(f"- {a}: {parts}")
    else:
        out.append("- (none)")
    out.append("")
    out.append("### Priorities")
    out.append("")
    if board["priority_counts"]:
        for p, n in sorted(board["priority_counts"].items()):
            out.append(f"- priority {p}: {n}")
    else:
        out.append("- (none)")
    out.append("")

    # ---- Running (live) ----
    out.append("## Running (live) tasks")
    out.append("")
    if board["running"]:
        out.append("| ID | Title | Assignee | Prio | Started | Heartbeat |")
        out.append("|----|-------|----------|------|---------|-----------|")
        for r in board["running"]:
            title = (r["title"] or "").replace("|", "/")[:60]
            out.append("| {id} | {title} | {assignee} | {prio} | {started} | {hb} |".format(
                id=r["id"], title=title, assignee=r.get("assignee") or "—",
                prio=r.get("priority", 0),
                started=fmt_ts_unix(r.get("started_at")),
                hb=fmt_ts_unix(r.get("last_heartbeat_at")),
            ))
    else:
        out.append("- none — all terminal.")
    out.append("")

    # ---- Blocked ----
    out.append("## Blocked tasks")
    out.append("")
    if board["blocked"]:
        for r in board["blocked"]:
            title = (r["title"] or "").replace("|", "/")[:80]
            kind = r.get("block_kind") or "untyped"
            err = (r.get("last_failure_error") or "").strip().replace("\n", " ")[:120]
            c = board["blocked_comments"].get(r["id"], 0)
            out.append(f"- **{r['id']}** ({kind}) prio {r.get('priority',0)} — {title}")
            out.append(f"  comments={c}  started={fmt_ts_unix(r.get('started_at'))}")
            if err:
                out.append(f"  last_failure: {err}")
    else:
        out.append("- none.")
    out.append("")

    # ---- Recent completions ----
    out.append("## Recently completed (latest 15)")
    out.append("")
    if board["recent_done"]:
        for r in board["recent_done"]:
            title = (r["title"] or "").replace("|", "/")[:70]
            out.append(f"- {r['id']}  {fmt_ts_unix(r.get('completed_at'))}  {title}")
    else:
        out.append("- none.")
    out.append("")

    # ---- Ledger ----
    out.append("## Landing ledger (tracks)")
    out.append("")
    out.append(f"- Source: {ledger['path']} (exists={ledger['exists']})")
    if ledger.get("error"):
        out.append(f"- Error: {ledger['error']}")
    out.append(f"- Rows total: {len(ledger['rows'])}")
    out.append("")
    out.append("### Live tracks (IN-FLIGHT / QUEUED)")
    out.append("")
    if ledger["live"]:
        for r in ledger["live"]:
            out.append(f"- **{r['track']}** ({r['status']}) — {r['mission']} [{r['base']}]")
    else:
        out.append("- none — all terminal.")
    out.append("")
    out.append("### Folded tracks (newest first)")
    out.append("")
    if ledger["folded"]:
        for r in reversed(ledger["folded"]):
            out.append(f"- **{r['track']}** — {r['verdict']}")
    else:
        out.append("- none.")
    out.append("")

    # ---- Motion sensor ----
    out.append("## Motion sensor (external tracker)")
    out.append("")
    out.append(f"- Source: {motion['path']} (exists={motion['exists']})")
    if motion.get("error"):
        out.append(f"- Error: {motion['error']}")
    out.append(f"- Tracked tickets: {motion.get('tracked_count', 0)}")
    out.append(f"- Snapshot entries: {motion.get('snapshot_count', 0)}")
    if motion.get("state_counts"):
        parts = ", ".join(f"{k}={v}" for k, v in sorted(motion["state_counts"].items()))
        out.append(f"- State counts: {parts}")
    latest = motion.get("latest")
    if latest:
        preview = (latest.get("last_comment_preview") or "").strip().replace("\n", " ")[:120]
        out.append(f"- Most-recently-moved: #{latest.get('number')} ({latest.get('state')}) updated {latest.get('updated_at')}")
        if preview:
            out.append(f"  preview: {preview}")
    out.append("")

    # ---- AB-01 pulse ----
    out.append("## AB-01 achievement surface (latest pulse)")
    out.append("")
    out.append(f"- Source: {ab01['path']} (exists={ab01['exists']}, lines={ab01.get('lines',0)})")
    if ab01.get("error"):
        out.append(f"- Error: {ab01['error']}")
    obs = ab01.get("latest")
    if obs:
        td = obs.get("tier_distribution") or {}
        out.append("- Tier distribution (unlocked): " +
                   ", ".join(f"{k}={v}" for k, v in td.items()))
        dc = (obs.get("defect_classes") or {})
        out.append(f"- Defect classes covered: {dc.get('covered')}/{dc.get('total')} "
                   f"(coverage {dc.get('coverage')})")
        under = dc.get("undercovered") or []
        if under:
            out.append(f"  undercovered: {', '.join(under)}")
        handles = obs.get("handles") or {}
        out.append(f"- Handles: {handles.get('handle_count')} total, "
                   f"olympian_handle_coverage={handles.get('olympian_handle_coverage')}")
        ns = (obs.get("negative_space") or {})
        out.append(f"- Negative space entries: {ns.get('count')}")
    else:
        out.append("- no observation yet.")
    out.append("")

    out.append("---")
    out.append("End of view. Re-run the generator to refresh (read-only on all inputs).")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Read-only unified task-list VIEW generator (CG-4).")
    ap.add_argument("--db", type=Path, default=DEFAULT_DB, help="kanban board sqlite db (read only)")
    ap.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER, help="landing ledger path")
    ap.add_argument("--motion-state", type=Path, default=DEFAULT_MOTION, dest="motion", help="motion watch state json")
    ap.add_argument("--ab01-series", type=Path, default=DEFAULT_AB01, dest="ab01", help="AB-01 series jsonl")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output view markdown path")
    ap.add_argument("--dry-run", action="store_true", help="build view in memory, print to stdout, no write")
    ap.add_argument("--now", default=None, help="override generated timestamp (ISO)")
    args = ap.parse_args(argv)

    # Hash inputs before to prove non-mutation.
    input_hashes_before = {}
    for p in (args.db, args.ledger, args.motion, args.ab01):
        if p.exists():
            input_hashes_before[str(p)] = sha256_file(p)

    generated_at = now_iso(args.now)
    board = read_board(args.db)
    ledger = parse_ledger(args.ledger)
    motion = read_motion(args.motion)
    ab01 = read_ab01(args.ab01)

    view = render_view(board, ledger, motion, ab01, generated_at)

    # Verify inputs unchanged after computation.
    for p, h in input_hashes_before.items():
        if sha256_file(Path(p)) != h:
            print(f"FAIL: input mutated during run: {p}", file=sys.stderr)
            return 2

    if args.dry_run:
        print(view)
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write: temp then replace.
    tmp = args.out.with_suffix(args.out.suffix + ".tmp")
    tmp.write_text(view, encoding="utf-8")
    os.replace(tmp, args.out)
    print(f"view written: {args.out} ({len(view)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
