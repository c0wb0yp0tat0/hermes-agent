#!/usr/bin/env python3
"""kindness-patrol — the runner's idle-floor duty.

When no verification/creative ride fills the runner, this patrol watches the
surfaces a supporting lab is backing and STAGES kind support previews — never
posts. Auth: public REST only (urllib; no gh on the runner). Drafts land in
the study tree (committed by the workflow) for head curation + the operator's
word. The posting gate is absolute: drafts are drafts.
"""
import json, os, time, urllib.request, urllib.error, sys

API = "https://api.github.com"
TARGET_REPOS = [
    "NousResearch/hermes-agent",   # the upstream he supports with verdicts
    "kvnloo/hermes-agent",         # his own fork (lab-habit watch's scope)
    "kvnloo/fleet-runner",         # his active projects (the watch's map)
    "kvnloo/glide",
    "kvnloo/autokernel",
    "kvnloo/newton",
]
HOME_REPO = "c0wb0yp0tat0/hermes-agent"
DRAFTS_DIR = "studies/rfc-143379-rig/kindness-patrol"
MAX_THREADS = 5           # drafts per run — bounded, never spammy
SINCE_H = float(os.environ.get("KINDNESS_SINCE_H", "6"))

UA = {"User-Agent": "kindness-patrol (rig)", "Accept": "application/vnd.github+json"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def main():
    ts = time.strftime("%Y%m%d-%H%M%S")
    os.makedirs(DRAFTS_DIR, exist_ok=True)
    try:
        events = get(f"{API}/users/kvnloo/events/public?per_page=50")
    except Exception as e:
        print(f"KINDNESS-PATROL: events fetch failed ({e}) — leaving the runner idle-honest")
        return 0
    threads, seen = [], set()
    for e in events:
        if e.get("type") != "IssueCommentEvent":
            continue
        repo = e.get("repo", {}).get("name", "")
        if repo not in TARGET_REPOS:
            continue
        url = (e.get("payload", {}).get("comment", {}) or {}).get("html_url", "")
        rel = url.replace(f"https://github.com/{repo}/", "")
        if not url or rel in seen:
            continue
        seen.add(rel)
        threads.append((e.get("created_at", ""), url, rel, repo))
    threads.sort(reverse=True)
    threads = threads[:MAX_THREADS]
    if not threads:
        print("KINDNESS-PATROL: no fresh supported surfaces in window — nothing staged, runner stays honest-idle")
        return 0
    drafts = []
    for i, (created, url, rel, repo) in enumerate(threads, 1):
        # fetch the thread + the supporting comment's body-head (public reads)
        try:
            if "/pull/" in rel:
                t = get(f"{API}/repos/{repo}/pulls/{rel.split('/')[2]}")
                title, typ = t.get("title", rel), "PR"
            else:
                t = get(f"{API}/repos/{repo}/issues/{rel.split('/')[1]}")
                title, typ = t.get("title", rel), "issue"
        except Exception:
            title, typ = rel, "thread"
        body = (
            f"# STAGED SUPPORT PREVIEW (kindness-patrol) — {typ} #{rel.split('/')[1] if '/' in rel else rel}\n\n"
            f"**Thread:** [{rel}](https://github.com/{repo}/{rel})\n"
            f"**Title:** {title}\n"
            f"**Supporting comment:** {created[:16]}Z on the thread — the lab's verdict/review motion.\n\n"
            f"---\n\n"
            f"@kvnloo — genuinely, thank you for the eyes on this one. The thread's catching real things,\n"
            f"and the support doesn't go unnoticed.\n\n"
            f"Standing offer, on the record: our lab's verification battery is unmetered and warm — if any\n"
            f"claim in this thread would benefit from an independent run (a failing case, a predicted\n"
            f"result, a guard's behavior), name it and it's a dispatch away. One word on the thread, and\n"
            f"the receipt lands back here.\n\n"
            f"*— staged by the rigor's kindness-patrol; posting gated on the operator's word.*\n"
        )
        fpath = f"{DRAFTS_DIR}/STAGED-{ts}-{i}.md"
        with open(fpath, "w") as f:
            f.write(body)
        drafts.append(fpath)
    print(f"KINDNESS-PATROL: STAGED {len(drafts)} preview(s):")
    for d in drafts:
        print(f"  {d}")
    print("  (drafts only — nothing posted; the operator's word is the only gate)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
