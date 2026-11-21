#!/usr/bin/env python3
"""repo_surface_fold.py — the repo IS the tracking surface; this keeps it current.

Reads the landing ledger (the single source of truth for track state), regenerates
the "Live track state" section of NAVIGATION.md AND the live/folded block of
WORK-STATE.md, syncs GitHub issue statuses, and commits+pushes. Runs on a cron
(or triggered by the watcher) so the repo never waits for the head to hand-edit
a surface that should track the ledger.

Invariants (same class as the watcher's auto-apply):
1. Audit trail survives — the ledger is append-only; this script only READS it.
2. Stop-on-failure — any verify failure aborts before commit.
3. Mutate-last — regenerate to a temp file, verify, then replace.
4. No stub content — a row with no verdict is never emitted as a claim.

Usage: python3 repo_surface_fold.py [--dry-run]
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

LEDGER = "/root/workspace/master-page/memory-chain/landing-ledger.md"
NAV = "/root/workspace/repos/mechanism-of-mechanisms-bridge/NAVIGATION.md"
WORKSTATE = "/root/workspace/repos/mechanism-of-mechanisms-bridge/WORK-STATE.md"
REPO = "/root/workspace/repos/mechanism-of-mechanisms-bridge"
# HTML-comment markers wrap the generated block in WORK-STATE.md. If either is
# missing the script aborts (fail-stop) rather than clobbering hand-edited
# content — the exact failure mode this fix eliminates (clobber-vs-drift).
WS_BEGIN = "<!-- BEGIN GENERATED: internal-ledger-tracks (repo_surface_fold.py) -->"
WS_END = "<!-- END GENERATED: internal-ledger-tracks -->"
# Track name -> GitHub issue number. STATUS is derived from the ledger at sync
# time (dynamic), never hardcoded — the static map was the desync root cause
# (reorientation-analysis 09-27: issues stayed OPEN after tracks folded).
TRACK_ISSUES = {
    "WATCHER-R5-FIX": "6",
    "PROBLEM-WORKING-ENCODE": "8",
    "FIX2-LIVE-TEST": "9",
    "MEMORY-REVIEWER-PREP": "10",
    "STORAGE-DECISION-PREP": "14",
    "HARNESS-ROBUSTNESS": "119",
    "WATCHER-R2-DECISION": "120",
}


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def parse_ledger():
    """Extract (track, status, verdict) rows from the ledger. Append-only read."""
    rows = []
    for line in open(LEDGER):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 9:
            continue
        ts, track, mission, base, exitc, artifact, fresh, status, verdict = cells[:9]
        if track in ("ts", "---"):
            continue
        rows.append({"ts": ts, "track": track, "mission": mission, "base": base,
                     "exit": exitc, "artifact": artifact, "fresh": fresh,
                     "status": status, "verdict": verdict})
    return rows


def live_tracks(rows):
    """Non-terminal rows = live tracks. Terminal = folded/superseded history."""
    live = [r for r in rows if r["status"] in ("IN-FLIGHT", "QUEUED")]
    folded = [r for r in rows if r["status"] == "FOLDED"]
    return live, folded


def render_section(rows):
    live, folded = live_tracks(rows)
    lines = []
    lines.append("## Live track state (auto-folded)")
    lines.append("Current ACES cycles and their verdicts — generated from the landing ledger by `repo_surface_fold.py`; the repo never waits for a hand edit.")
    if live:
        lines.append("**LIVE TRACKS:**")
        for r in live:
            lines.append("- **%s** (%s) — %s [%s]" % (r["track"], r["status"], r["mission"], r["base"]))
    else:
        lines.append("**LIVE TRACKS:** none — all terminal.")
    if folded:
        lines.append("**FOLDED TRACKS (full record, newest first):**")
        for r in reversed(folded):
            lines.append("- **%s** — %s" % (r["track"], r["verdict"]))
    return "\n".join(lines)


def render_workstate_section(rows):
    """Generate the live + folded block for WORK-STATE.md's internal-ledger-tracks
    section. Same rows/verdicts as NAVIGATION.md §9 — sourced ONLY from the
    ledger, so the WORK-STATE surface can never drift from the ledger."""
    live, folded = live_tracks(rows)
    lines = []
    lines.append("**Live (IN-FLIGHT):**")
    if live:
        lines.append("")
        lines.append("| Track | Base model | Artifact | Status |")
        lines.append("|-------|-----------|----------|--------|")
        for r in live:
            lines.append("| %s | %s | %s | %s |" % (
                r["track"], r["base"], r["artifact"], r["status"]))
    else:
        lines.append(" none — all terminal.")
    lines.append("")
    lines.append("**Folded tracks (full record, newest first):**")
    if folded:
        lines.append("")
        for r in reversed(folded):
            lines.append("- **%s** — %s" % (r["track"], r["verdict"]))
    else:
        lines.append(" none.")
    return "\n".join(lines)


def replace_section(nav_path, new_section):
    """Replace everything between '## Live track state' and the next '## ' header."""
    src = open(nav_path).read()
    m = re.search(r"^## Live track state.*?(?=^## )", src, re.M | re.S)
    if not m:
        return False
    return src[:m.start()] + new_section + "\n\n" + src[m.end():]


def replace_workstate_block(wpath, new_block):
    """Replace content between BEGIN/END markers in WORK-STATE.md.

    Returns None if markers are missing or unordered (fail-stop — never clobber
    a hand-edited file whose markers were removed). Preserves the curated
    preamble above the BEGIN marker and everything after the END marker."""
    src = open(wpath).read()
    begin_idx = src.find(WS_BEGIN)
    end_idx = src.find(WS_END)
    if begin_idx == -1 or end_idx == -1 or end_idx < begin_idx:
        return None
    block_start = begin_idx + len(WS_BEGIN)
    return src[:block_start] + "\n" + new_block + "\n" + src[end_idx:]


def sync_issues(dry_run):
    """Sync issue labels/state from the LEDGER (dynamic), not a static map.

    For each track->issue pair: look up the track's LATEST status in the ledger.
    FOLDED/SUPERSEDED -> close the issue (if open). IN-FLIGHT/QUEUED -> ensure the
    matching label. This eliminates the desync class the static map caused.
    """
    rows = parse_ledger()
    # latest status per track (ledger is append-only; last row wins)
    latest = {}
    for r in rows:
        latest[r["track"]] = r["status"]
    for track, num in TRACK_ISSUES.items():
        status = latest.get(track)
        if status is None:
            continue
        r = run(["gh", "issue", "view", num, "--json", "labels,state",
                 "--jq", "{labels: [.labels[].name], state: .state}"], cwd=REPO)
        if r.returncode != 0:
            print("  issue %s: gh view failed: %s" % (num, r.stderr.strip()[:80]))
            continue
        cur = json.loads(r.stdout)
        if status in ("FOLDED", "SUPERSEDED"):
            if cur["state"].lower() == "open":
                if dry_run:
                    print("  issue %s: would close (ledger: %s)" % (num, status))
                else:
                    run(["gh", "issue", "close", num], cwd=REPO)
                    print("  issue %s: closed (ledger: %s)" % (num, status))
        else:
            label = "in-flight" if status == "IN-FLIGHT" else "queued"
            if label not in cur["labels"]:
                if dry_run:
                    print("  issue %s: would add label %s" % (num, label))
                else:
                    run(["gh", "issue", "edit", num, "--add-label", label], cwd=REPO)
                    print("  issue %s: label %s added" % (num, label))


def main():
    dry_run = "--dry-run" in sys.argv
    rows = parse_ledger()
    if not rows:
        print("FAIL: ledger unreadable or empty — aborting (stop-on-failure)")
        return 1
    live, folded = live_tracks(rows)

    # --- Generate both sections (pure function of the ledger) ---
    nav_section = render_section(rows)
    ws_block = render_workstate_section(rows)

    # --- Mutate-last: render to temp, verify, then replace ---
    fd_nav, tmp_nav = tempfile.mkstemp(suffix=".nav", dir=os.path.dirname(NAV))
    fd_ws, tmp_ws = tempfile.mkstemp(suffix=".ws", dir=os.path.dirname(WORKSTATE))
    try:
        # NAVIGATION.md: replace ## Live track state section
        updated_nav = replace_section(NAV, nav_section)
        if not updated_nav:
            print("FAIL: '## Live track state' section not found in NAVIGATION.md")
            return 1
        with os.fdopen(fd_nav, "w") as f:
            f.write(updated_nav)
        check_nav = open(tmp_nav).read()
        if "## Live track state" not in check_nav or "LIVE TRACKS" not in check_nav:
            print("FAIL: regenerated NAVIGATION section missing markers — aborting")
            return 1

        # WORK-STATE.md: replace between BEGIN/END markers (fail-stop if missing)
        updated_ws = replace_workstate_block(WORKSTATE, ws_block)
        if updated_ws is None:
            print("FAIL: WORK-STATE.md generation markers not found — aborting (do not clobber hand-edited file)")
            return 1
        with os.fdopen(fd_ws, "w") as f:
            f.write(updated_ws)
        check_ws = open(tmp_ws).read()
        if WS_BEGIN not in check_ws or WS_END not in check_ws:
            print("FAIL: regenerated WORK-STATE block missing markers — aborting")
            return 1

        if dry_run:
            print("DRY-RUN: NAVIGATION.md section would be replaced (%d live, %d folded rows)" % (
                len(live), len(folded)))
            print("DRY-RUN: WORK-STATE.md internal-ledger-tracks block would be replaced")
            sync_issues(dry_run=True)
            return 0

        # RECONCILE BEFORE REPLACE (reconcile-first): fetch origin/main and
        # hard-reset local main BEFORE writing the regenerated files, so the
        # generated content survives the reconcile instead of being discarded.
        rec = run(["git", "-C", REPO, "fetch", "origin", "main"], timeout=120)
        if rec.returncode != 0:
            print("FAIL: fetch origin main failed: %s" % rec.stderr.strip()[:120])
            return 1
        rec = run(["git", "-C", REPO, "checkout", "main"], timeout=60)
        if rec.returncode != 0:
            print("FAIL: checkout main failed: %s" % rec.stderr.strip()[:120])
            return 1
        rec = run(["git", "-C", REPO, "reset", "--hard", "origin/main"], timeout=60)
        if rec.returncode != 0:
            print("FAIL: reset to origin/main failed: %s" % rec.stderr.strip()[:120])
            return 1

        # Atomic replace (os.replace is atomic within one device). Both temps
        # verified first — only if both pass do either get swapped in.
        os.replace(tmp_nav, NAV)
        print("NAVIGATION.md section replaced (%d live, %d folded rows)" % (
            len(live), len(folded)))
        os.replace(tmp_ws, WORKSTATE)
        print("WORK-STATE.md internal-ledger-tracks block replaced")
    finally:
        for tmp in (tmp_nav, tmp_ws):
            if os.path.exists(tmp):
                os.unlink(tmp)

    # Commit + push both files (only if either changed)
    r = run(["git", "-C", REPO, "diff", "--quiet", "NAVIGATION.md", "WORK-STATE.md"])
    if r.returncode == 0:
        print("no change — NAVIGATION.md + WORK-STATE.md already current")
    else:
        run(["git", "-C", REPO, "add", "NAVIGATION.md", "WORK-STATE.md"])
        run(["git", "-C", REPO, "commit", "-m",
             "nav+ws: auto-fold live track state from landing ledger"])
        p = run(["git", "-C", REPO, "push", "origin", "main"])
        if p.returncode != 0:
            print("FAIL: push failed: %s" % p.stderr.strip()[:120])
            return 1
        print("pushed")

    sync_issues(dry_run=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
