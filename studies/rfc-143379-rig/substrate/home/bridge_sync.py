#!/usr/bin/env python3
"""bridge_sync.py — mirror the living-home working copies up to the private repo.

The private repo `c0wb0yp0tat0/mechanism-of-mechanisms` is the canonical store
for the living-home documentation; the home keeps its local working copies as
the source of truth (generator + recall path intact). This script mirrors those
working copies up on the same 5-min cron tick as home-update.py.

Push model = PR-on-change (A3): bridge_sync commits to a `bridge/<date>` branch
and pushes; a validator-gated workflow (.github/workflows/bridge-sync.yml) opens
a PR, merged on green. Direct-push-to-main is dropped.

Hard rules:
- NEVER moves a local file — it only copies working copies into the checkout.
- A push failure NEVER blocks local appends: log + continue (exit 0).
- Operates on the canonical checkout (A2), `git pull --rebase` first.
- Generator sources (ACTIVITY/STATUS/OPEN-ITEMS/DOC-INDEX/MECHANISM-STATUS/
  PROJECTS) stay local as source of truth and are NOT pushed here.
Stdlib only.
"""
from __future__ import annotations

import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = "c0wb0yp0tat0/mechanism-of-mechanisms"
CHECKOUT = Path("/root/workspace/repos/mechanism-of-mechanisms-bridge")
MASTER = Path("/root/workspace/master-page")

# Generator sources stay local (source of truth) — never pushed by bridge_sync.
GENERATOR_SOURCES = {
    "ACTIVITY.md", "STATUS.md", "OPEN-ITEMS.md",
    "DOC-INDEX.md", "MECHANISM-STATUS.md", "PROJECTS.md",
}
# Large reference dumps with broken internal links — not migrated to the repo.
# NAVIGATION.md is a ROOT-level doc (its links are root-relative); copying it
# into docs/ breaks every link and fails validate_bridged_docs.py in CI
# (2026-09-28: sync PRs stalled on this). Root-only docs stay at root.
EXCLUDED_TOP_LEVEL = {"README-ALL.md", "README-ALL-FULL.md", "NAVIGATION.md"}

# Sync mapping: (local source, repo destination dir)
SYNC_DIRS = [
    (MASTER / "memory-chain", CHECKOUT / "docs" / "memory-chain"),
    (MASTER / "deepdive-mission-flow", CHECKOUT / "docs" / "mission-flow"),
]


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)


def sync_tree(src: Path, dst: Path, only_md: bool = False) -> int:
    """Copy src tree into dst (containers only). Returns number of files copied.

    MIRROR semantics: files present in dst but absent in src are DELETED
    (the checkout is a mirror of the home, not a working branch). This keeps
    the repo coherent when local files move or are archived (e.g. the
    watcher's staging -> archive move).
    """
    copied = 0
    for dirpath, dirnames, filenames in os.walk(src):
        # skip python caches
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        rel = os.path.relpath(dirpath, src)
        target_dir = dst if rel == "." else dst / rel
        target_dir.mkdir(parents=True, exist_ok=True)
        for fname in filenames:
            if only_md and not fname.endswith(".md"):
                continue
            if fname.endswith(".pyc"):
                continue
            src_file = Path(dirpath) / fname
            dst_file = target_dir / fname
            if not dst_file.exists() or src_file.read_bytes() != dst_file.read_bytes():
                shutil.copy2(src_file, dst_file)
                copied += 1
    # Mirror deletions: remove dst files that no longer exist in src.
    for dirpath, dirnames, filenames in os.walk(dst):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        rel = os.path.relpath(dirpath, dst)
        src_dir = src if rel == "." else src / rel
        for fname in filenames:
            if only_md and not fname.endswith(".md"):
                continue
            if not (src_dir / fname).exists():
                os.remove(Path(dirpath) / fname)
    return copied


def sync_top_level_docs() -> int:
    """Copy the moved top-level docs into docs/. Returns number copied.

    COPY-ONLY, never deletes: docs/ also holds repo-native files the sync
    does not own (ideas-digest.md, evidence-plan.md, etc.) — a delete pass
    would nuke them and fail validate_bridged_docs.py in CI (2026-09-28).
    Stale copies of now-excluded files (e.g. NAVIGATION.md) are removed
    manually once, not by the sync.
    """
    copied = 0
    dst = CHECKOUT / "docs"
    dst.mkdir(parents=True, exist_ok=True)
    for fname in sorted(os.listdir(MASTER)):
        if not fname.endswith(".md"):
            continue
        if fname in GENERATOR_SOURCES or fname in EXCLUDED_TOP_LEVEL:
            continue
        src_file = MASTER / fname
        dst_file = dst / fname
        if not dst_file.exists() or src_file.read_bytes() != dst_file.read_bytes():
            shutil.copy2(src_file, dst_file)
            copied += 1
    return copied


def gh_json(args: list[str]) -> list:
    """gh CLI returning JSON array (empty on failure). Uses the user's token."""
    import json

    r = run(["gh", *args], CHECKOUT)
    if r.returncode:
        print(f"bridge_sync: gh {' '.join(args[:2])} failed: {r.stderr.strip()}", file=sys.stderr)
        return []
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return []


MACHINE_BRANCH_PREFIXES = ("bridge/", "automation/")


def open_machine_prs() -> list:
    """Any open PR whose head branch is a machine family (bridge/*, automation/*)
    — the refresh workflows push automation/* (nousresearch responsibility,
    ideas digest); the bridge sync pushes bridge/*. At most one open PR per
    family should ever exist; consume covers both so machine PRs never sit."""
    return [
        p
        for p in gh_json(
            ["pr", "list", "--repo", REPO, "--state", "open",
             "--json", "number,headRefName,mergeable,statusCheckRollup", "--limit", "20"]
        )
        if str(p.get("headRefName", "")).startswith(MACHINE_BRANCH_PREFIXES)
    ]


def checks_failed(pr: dict) -> bool:
    rollup = pr.get("statusCheckRollup") or []
    return any(
        c.get("status") == "COMPLETED" and c.get("conclusion") not in (None, "SUCCESS", "SKIPPED")
        for c in rollup
    )


def checks_green(pr: dict) -> bool:
    rollup = pr.get("statusCheckRollup") or []
    if not rollup:
        return pr.get("mergeable") == "MERGEABLE"
    return all(
        c.get("status") == "COMPLETED" and c.get("conclusion") in ("SUCCESS", "SKIPPED")
        for c in rollup
    )


def consume_open_pr() -> int:
    """Merge the open bridge PR on green; refuse on failed checks; wait when pending.

    Returns 0 = merged/none open, 1 = failing (human review), 2 = still pending.
    This is the self-consumption guard: never spawn a sibling PR while one is
    open, so the pile cannot grow (the 09-25 branch-spam defect).
    """
    prs = open_machine_prs()
    if not prs:
        return 0
    pr = prs[0]
    n, ref = pr["number"], pr["headRefName"]
    if checks_failed(pr):
        print(f"bridge_sync: PR #{n} ({ref}) checks FAILED — human review, not merging", file=sys.stderr)
        return 1
    if not checks_green(pr):
        # A conflicting PR can never go green: GitHub reports the merge state
        # DIRTY while checks may show as pending forever. Reconcile the PR
        # branch to current main first (same reconcile-before-act principle
        # as the fold) so the checks can actually complete.
        st = gh_json(["pr", "view", str(n), "--repo", REPO,
                      "--json", "mergeStateStatus"])
        if st and isinstance(st, list) and st and st[0].get("mergeStateStatus") in ("DIRTY", "CONFLICTING"):
            run(["git", "fetch", "origin", "main"], CHECKOUT)
            run(["git", "fetch", "origin", ref], CHECKOUT)
            run(["git", "checkout", "-B", ref, f"origin/{ref}"], CHECKOUT)
            mb = run(["git", "merge", "origin/main", "-m",
                      "chore: sync living-home docs (rebase onto main)"], CHECKOUT)
            if mb.returncode:
                print(f"bridge_sync: PR #{n} merge-update failed: {mb.stderr.strip()}", file=sys.stderr)
                run(["git", "checkout", "main"], CHECKOUT)
                return 2
            run(["git", "push", "origin", ref], CHECKOUT)
            run(["git", "checkout", "main"], CHECKOUT)
            print(f"bridge_sync: PR #{n} ({ref}) reconciled to main — checks will re-run")
            return 2
        print(f"bridge_sync: PR #{n} ({ref}) checks pending — waiting, no new branch")
        return 2
    m = run(["gh", "pr", "merge", str(n), "--repo", REPO, "--squash", "--delete-branch"], CHECKOUT)
    if m.returncode:
        print(f"bridge_sync: PR #{n} merge failed: {m.stderr.strip()}", file=sys.stderr)
        return 1
    # get back to a clean main so the next tick starts from remote HEAD
    run(["git", "checkout", "main"], CHECKOUT)
    run(["git", "pull", "--rebase", "origin", "main"], CHECKOUT)
    print(f"bridge_sync: PR #{n} merged on green ({ref}); checkout reset to main")
    return 0


def main() -> int:
    if not CHECKOUT.is_dir() or not (CHECKOUT / ".git").is_dir():
        print(f"bridge_sync: canonical checkout missing at {CHECKOUT}", file=sys.stderr)
        return 0  # never block local appends

    # A2: reconcile to remote HEAD before touching anything.
    pull = run(["git", "pull", "--rebase", "origin", "main"], CHECKOUT)
    if pull.returncode:
        print(f"bridge_sync: git pull --rebase failed (will retry next tick): {pull.stderr.strip()}", file=sys.stderr)
        return 0  # never block local appends

    # Self-consumption + containment: work the open PR (if any) BEFORE making
    # new changes. A pending PR ABSORBS new changes on its own branch (one PR
    # per update family); a failing PR blocks everything for human review.
    pending = consume_open_pr()
    if pending == 1:
        return 0

    # Mirror working copies up (copy, never move).
    total = 0
    for src, dst in SYNC_DIRS:
        only_md = src.name == "deepdive-mission-flow"
        total += sync_tree(src, dst, only_md=only_md)
    total += sync_top_level_docs()

    # Stage and check for changes.
    # NEVER sweep .worktrees/ into the branch — lane worktrees contain .git
    # files, so gitadd stages them as gitlinks and GitHub Actions checkout dies
    # ("No url found for submodule path ... in .gitmodules"), stalling every
    # sync PR (2026-10-04: bridge dead since 09-30, ~170 branches piled up).
    run(["git", "add", "-A", "--", ".", ":(exclude).worktrees"], CHECKOUT)
    status = run(["git", "status", "--porcelain"], CHECKOUT)
    if not status.stdout.strip():
        print("bridge_sync: no changes to push")
        return 0

    if pending == 2:
        # Containment: append to the open PR's branch instead of a new PR.
        prs = open_machine_prs()
        if prs:
            branch = prs[0]["headRefName"]
            run(["git", "fetch", "origin", branch], CHECKOUT)
            run(["git", "checkout", "-B", branch, f"origin/{branch}"], CHECKOUT)
            commit = run(["git", "commit", "-m", "chore: sync living-home docs (amended)"], CHECKOUT)
            if commit.returncode:
                print(f"bridge_sync: amend commit failed: {commit.stderr.strip()}", file=sys.stderr)
                return 0
            push = run(["git", "push", "origin", branch], CHECKOUT)
            if push.returncode:
                print(f"bridge_sync: amend push failed: {push.stderr.strip()}", file=sys.stderr)
                return 0
            print(f"bridge_sync: amended {branch} ({total} files synced) — contained in the open PR")
            return 0
        # no PR found (raced the workflow) — fall through to a fresh branch
        pending = 0

    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    branch = f"bridge/{date}"
    run(["git", "checkout", "-b", branch], CHECKOUT)
    commit = run(
        ["git", "commit", "-m", f"chore: sync living-home docs {date}"],
        CHECKOUT,
    )
    if commit.returncode:
        print(f"bridge_sync: commit failed: {commit.stderr.strip()}", file=sys.stderr)
        return 0

    push = run(["git", "push", "-u", "origin", branch], CHECKOUT)
    if push.returncode:
        print(f"bridge_sync: push failed (local copy intact; retry next tick): {push.stderr.strip()}", file=sys.stderr)
        return 0

    print(f"bridge_sync: pushed {branch} ({total} files synced); PR workflow will open a PR — consumed on green")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
