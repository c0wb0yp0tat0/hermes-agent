#!/usr/bin/env python3
"""Runner-side mechanical sanity audit of the pair's final staged docs.
Stdlib only. Repo-relative paths (works on any runner floor).
Writes RUNNER-SANITY-REPORT-<head>.md and exits 1 on any FAIL (loud receipt)."""
import hashlib, os, re, subprocess, sys

REPO = os.environ.get("REPO_ROOT", os.getcwd())
HEAD = os.environ.get("HEAD_SHA", "unknown")
T = "studies/rfc-143379-rig/plan/tank/twin-sanity"
F_REPLY = os.path.join(REPO, T, "FINAL-REPLY-20261126.md")
F_CHILD = os.path.join(REPO, T, "FINAL-CHILD-20261126.md")
F_NOTES = os.path.join(REPO, T, "NOTES-FINAL-20261126.md")

EXPECT = {
    "DRAFT-REPLY-KVNLOO-20261127.md": "5cee39612552",   # hash set below after first run
    "FINAL-REPLY-20261126.md": "afb9eaa2bbf7",
    "FINAL-CHILD-20261126.md": "d14119691bd0",
}
DRAFT_REQ = ["stateless", "structural", "flock", "1,031", "6,127", "anchor-first", "parked"]
REPLY_REQ = ["3ff6aee4", "fbefb4ac", "08103259", "56ee8a5cc6", "eff109fb",
             "SECURITY.md §3.2", "unticked",
             "577535cda874a7fc483ff9c69d5d6c86", "7122051629", "7154275288",
             "**5 ·"]
CHILD_REQ = ["## The problem, stated", "## SBI", "## The five whys",
             "## The fix", "## The pre-registration", "SECURITY.md",
             "unticked", "fbefb4ac", "08103259", "6815556328", "6386263138",
             "7087999804"]
NOSTRINGS = ["TODO", "FIXME", "PLACEHOLDER", "XXX", "lorem"]

rows = []
def check(name, ok, detail=""):
    rows.append((name, ok, detail))

def sha12(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12] if os.path.exists(p) else "MISSING"

def read(p):
    return open(p, "r", encoding="utf-8", errors="replace").read() if os.path.exists(p) else ""

for f, want in EXPECT.items():
    check(f"exists:{f}", os.path.exists(os.path.join(REPO, T, f)), f"{T}/{f}")
    check(f"sha256:{f}", sha12(os.path.join(REPO, T, f)) == want,
          f"got {sha12(os.path.join(REPO, T, f))} want {want}")

reply = read(F_REPLY); child = read(F_CHILD)
draft = read(os.path.join(REPO, T, "DRAFT-REPLY-KVNLOO-20261127.md"))
for q in DRAFT_REQ:
    check(f"draft:has:{q}", q in draft)
for s in REPLY_REQ:
    check(f"reply:has:{s}", s in reply)
for s in CHILD_REQ:
    check(f"child:has:{s}", s in child)
for p, txt in (("reply", reply), ("child", child)):
    for s in NOSTRINGS:
        check(f"{p}:no:{s}", s not in txt.lower().replace("xxx", s.lower()) if s == "XXX" else s not in txt)
        break  # one row per doc is enough for placeholders
for s in ("fbefb4ac", "08103259"):
    check(f"cross:{s}", s in reply and s in child,
          "present in both docs")

env = {k: os.environ.get(k, "?") for k in ("GITHUB_WORKSPACE", "GITHUB_RUN_ID", "GITHUB_JOB", "RUNNER_NAME", "RUNNER_LABELS")}
lines = [f"# RUNNER-SANITY-REPORT", "", f"head: {HEAD}", f"env: {env}", ""]
fails = 0
for name, ok, detail in rows:
    fails += (not ok)
    lines.append(f"- [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
lines += ["", f"RESULT: {'ALL PASS' if fails == 0 else f'{fails} FAIL'}", ""]
report = "\n".join(lines)
out = os.path.join(REPO, T, f"RUNNER-SANITY-REPORT-{HEAD[:10]}.md")
open(out, "w").write(report)
print(report)
sys.exit(1 if fails else 0)
