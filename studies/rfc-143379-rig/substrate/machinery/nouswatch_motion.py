#!/usr/bin/env python3
"""NOUSResearch org-wide motion watchdog - detects org events, releases, issues, PRs.

Emits stdout ONLY when state moves (new org event, new release, issue/PR state change).
Silent otherwise. State persisted to var/nouswatch_state.json.

Scope Principle: Sweep the full data surface (all org repos, all releases, papers, models,
announcements, blog, X) and report the full picture, THEN mark significance per item.
A narrow scope is a defect to correct, not a design choice. Mechanisms are built around data.
"""
import json, os, sys, urllib.request, subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

STATE_FILE = "/root/.hermes/scripts/var/nouswatch_state.json"
TRACKER_REPO = "/root/workspace/repos/mechanism-of-mechanisms-bridge"
ORG_EVENTS_URL = "https://api.github.com/orgs/NousResearch/events"
RELEASES_ATOM = "https://github.com/NousResearch/hermes-agent/releases.atom"
TRACKER_PATH = "/root/workspace/repos/mechanism-of-mechanisms-bridge/docs/nousresearch-responsibility-tracker.md"

# TRACKED-ONLY FILTER (2026-10-04, user standing): the org-event firehose is
# noise — the watch reports ONLY motion on the tracked items (the read-gap
# campaign + the memory-review watchers). A repo-wide PR close is not value.
TRACKED_ITEMS = ["11548", "116673", "116564", "116788", "116834", "116846"]

def load_state():
    """Load previous state from file."""
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE))
        except Exception:
            pass
    return {"event_ids": [], "release_ids": [], "tracker_checked": "", "tracker_hash": "", "updated": ""}

def save_state(state):
    """Save state to file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def fetch_org_events():
    """Fetch org-level events as PRIMARY signal.
    Returns list of events with id, type, repo.name, created_at.
    """
    try:
        req = urllib.request.Request(ORG_EVENTS_URL, headers={"User-Agent": "hermes-nouswatch/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            events = json.loads(resp.read().decode())
            result = []
            for e in events:
                # GitHub org events have 'id' at the top level
                evt_id = e.get("id", "")
                if not evt_id:
                    # Fallback: construct ID from type + created_at
                    evt_type = e.get("type", "unknown")
                    evt_time = e.get("created_at", "unknown")
                    evt_id = f"{evt_type}-{evt_time}"
                
                result.append({
                    "id": evt_id,
                    "type": e.get("type", ""),
                    "repo": e.get("repo", {}).get("name", ""),
                    "created_at": e.get("created_at", ""),
                    "actor": e.get("actor", {}),
                    "payload": e.get("payload", {})
                })
            return result
    except Exception:
        return []

def fetch_releases_atom():
    """Fetch hermes-agent releases.atom as SECONDARY signal.
    Returns list of releases with id, title, updated, href.
    """
    try:
        req = urllib.request.Request(RELEASES_ATOM, headers={"User-Agent": "hermes-nouswatch/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml_bytes = resp.read()
        root = ET.fromstring(xml_bytes)
        NS = {"a": "http://www.w3.org/2005/Atom"}
        entries = []
        for e in root.findall("a:entry", NS):
            href = ""
            for link in e.findall("a:link", NS):
                href = link.get("href", "")
                break
            entries.append({
                "id": e.findtext("a:id", default="", namespaces=NS),
                "title": e.findtext("a:title", default="", namespaces=NS),
                "updated": e.findtext("a:updated", default="", namespaces=NS),
                "href": href
            })
        return entries
    except Exception:
        return []

def check_tracker_change(prev_state):
    """Check if responsibility tracker has changed.
    Returns (changed, message) tuple.
    Gated on git hash: git describe --always HEAD must differ from stored hash.
    """
    if not os.path.exists(TRACKER_PATH):
        return False, ""
    
    try:
        # First check git hash - if unchanged, skip mtime noise
        git_result = subprocess.run(
            ["git", "describe", "--always", "HEAD"],
            cwd=TRACKER_REPO, capture_output=True, text=True, timeout=30
        )
        current_hash = git_result.stdout.strip() if git_result.returncode == 0 else ""
        prev_hash = prev_state.get("tracker_hash", "")
        
        if current_hash and current_hash == prev_hash and prev_hash:
            # Hash unchanged, even if mtime bumped (self-motion filter)
            return False, ""
        
        stat = os.stat(TRACKER_PATH)
        mod_time = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
        prev_checked = prev_state.get("tracker_checked", "")
        # Normalize timestamps for comparison
        if mod_time != prev_checked and prev_checked != "":
            return True, f"TRACKER UPDATED: {TRACKER_PATH} modified {mod_time}"
    except Exception:
        pass
    return False, ""

def get_event_origin(event):
    """Determine origin attribution: USER-INITIATED vs REPO-WIDE.
    Returns 'USER' for human-initiated, 'REPO-WIDE' for automation/repo activity.
    
    Note: event.actor has no 'type' field in org-events feed, so bot detection
    relies solely on login substring heuristics. Known human logins (dskwe,
    liuhao1024, Froraut, apoapostolov) must not contain 'bot' or 'actions'.
    """
    evt_type = event.get("type", "")
    payload = event.get("payload", {})
    actor = event.get("actor", {})
    repo = event.get("repo", "")
    
    # PushEvent: check if commits have user activity
    if evt_type == "PushEvent":
        commits = payload.get("commits", [])
        # If any commit has a user (not bot/automation), tag as USER
        for c in commits:
            author = c.get("author", {})
            if author and author.get("name") and "bot" not in author.get("name", "").lower() and "action" not in author.get("name", "").lower():
                return "USER"
        return "REPO-WIDE"
    
    # PullRequestEvent: check actor.login (top-level, not payload.pull_request.user)
    if evt_type == "PullRequestEvent":
        login = actor.get("login", "")
        if login and "bot" not in login.lower() and "actions" not in login.lower():
            return "USER"
        return "REPO-WIDE"
    
    # IssuesEvent: check actor.login (top-level, not payload.issue.user)
    if evt_type == "IssuesEvent":
        login = actor.get("login", "")
        if login and "bot" not in login.lower() and "actions" not in login.lower():
            return "USER"
        return "REPO-WIDE"
    
    # CreateEvent: repo creation - check member activity
    if evt_type == "CreateEvent":
        actor_login = payload.get("member", {}).get("login", "anonymous")
        if "bot" not in actor_login.lower() and "actions" not in actor_login.lower():
            return "USER"
        return "REPO-WIDE"
    
    # ReleaseEvent: automation typically
    if evt_type == "ReleaseEvent":
        return "REPO-WIDE"
    
    return "REPO-WIDE"


def event_is_material(event):
    """Check if an event is material and should generate a change message.
    Returns (is_material, reason) tuple.
    """
    evt_type = event.get("type", "")
    repo = event.get("repo", "")
    payload = event.get("payload", {})
    
    if evt_type == "CreateEvent":
        actor = payload.get("member", {}).get("login", "anonymous")
        return True, f"NEW REPO: {repo} created by {actor}"
    
    if evt_type == "ReleaseEvent":
        action = payload.get("action", "")
        if action == "published":
            return True, f"NEW RELEASE in {repo}"
    
    if evt_type == "PushEvent":
        commits = payload.get("commits", [])
        cnt = len(commits) if commits else 0
        return True, f"PUSH in {repo}: {cnt} commit(s)"
    
    if evt_type == "IssuesEvent":
        action = payload.get("action", "")
        issue = payload.get("issue", {})
        if action in ["opened", "closed", "reopened"]:
            num = issue.get("number", "?")
            title = issue.get("title", "")[:40].replace("'", "'")
            return True, f"ISSUE {action.upper()} in {repo}: #{num} '{title}'"
    
    if evt_type == "PullRequestEvent":
        action = payload.get("action", "")
        pr = payload.get("pull_request", {})
        if action in ["opened", "closed", "reopened", "merged"]:
            num = pr.get("number", "?")
            title = pr.get("title", "")[:35].replace("'", "'")
            merged = pr.get("merged", False)
            status = "MERGED" if merged else action.upper()
            return True, f"PR {status} in {repo}: #{num} '{title}'"
    
    return False, ""

def main():
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    prev = load_state()
    changes = []
    
    # PRIMARY SIGNAL: Org events
    events = fetch_org_events()
    prev_event_ids = set(prev.get("event_ids", []))
    
    for e in events:
        eid = e.get("id", "")
        if eid and eid not in prev_event_ids:
            is_mat, reason = event_is_material(e)
            if reason:  # Only add if we have a meaningful reason
                # TRACKED-ONLY: skip org-wide noise unless it touches a tracked item
                if not any(f"#{n}" in reason for n in TRACKED_ITEMS):
                    continue
                origin = get_event_origin(e)
                changes.append(f"[{origin}] EVENT: {reason}")
    
    # SECONDARY SIGNAL: Releases
    releases = fetch_releases_atom()
    prev_release_ids = set(prev.get("release_ids", []))
    
    for r in releases:
        rid = r.get("id", "") or r.get("href", "")
        if rid and rid not in prev_release_ids:
            title = r.get("title", "")
            href = r.get("href", "")
            changes.append(f"RELEASE: {title} ({href})")
    
    # TERTIARY SIGNAL: Tracker change (only if we have a previous check)
    tracker_changed, tracker_msg = check_tracker_change(prev)
    if tracker_changed:
        changes.append(tracker_msg)
    
    # Output: stdout ONLY on movement
    if changes:
        print("[nous-watch] motion detected:\n" + "\n".join(f"  - {c}" for c in changes))
        
        # Update state with current event IDs and release IDs
        current_event_ids = [e.get("id", "") for e in events if e.get("id")]
        current_release_ids = [r.get("id", r.get("href", "")) for r in releases if r.get("id")]
        
        tracker_mtime = ""
        if os.path.exists(TRACKER_PATH):
            tracker_mtime = datetime.fromtimestamp(os.stat(TRACKER_PATH).st_mtime, tz=timezone.utc).isoformat()
        
        # Get current git hash for tracker change detection
        tracker_hash = ""
        git_result = subprocess.run(
            ["git", "describe", "--always", "HEAD"],
            cwd=TRACKER_REPO, capture_output=True, text=True, timeout=30
        )
        if git_result.returncode == 0:
            tracker_hash = git_result.stdout.strip()
        
        save_state({
            "event_ids": current_event_ids,
            "release_ids": current_release_ids,
            "tracker_checked": tracker_mtime,
            "tracker_hash": tracker_hash,
            "updated": now
        })
    # Empty stdout = silent (no change)

if __name__ == "__main__":
    main()