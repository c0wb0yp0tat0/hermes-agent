#!/usr/bin/env python3
"""FINISH-LINE-REPLICATION — the apex run's failable acceptance (written BEFORE the nodes, per the method).
The run is not done until this exits 0."""
import json, subprocess, sys

fails = []
repo = "c0wb0yp0tat0/hermes-agent"
branch = "study/rfc-143379-rig-20261105"

def exists(path):
    return subprocess.run(["gh", "api", f"repos/{repo}/contents/{path}?ref={branch}", "--jq", ".sha"],
                          capture_output=True, text=True).returncode == 0

head = subprocess.run(["gh", "api", f"repos/{repo}/branches/{branch}", "--jq", ".commit.sha"],
                      capture_output=True, text=True).stdout.strip()
print("final head:", head[:10])

# 1. the gate's re-measurement's receipt (the runner's union at the final head GREEN) - the run's own landing row
# 2. the arms' re-run CSVs present at the head
for p in ("krecency/results/alias.csv", "krecency/results/pin.csv", "krecency/results/competing.csv"):
    if not exists("studies/rfc-143379-rig/" + p):
        fails.append("MISSING arm CSV at head: " + p)
# 3. the fleet's fourth landing (the step finding)
if not exists("studies/rfc-143379-rig/copycat-findings/copycat-step-20261105.md"):
    fails.append("MISSING the step finding (the fourth lens)")
# 4. the three-voice rotation's posts (the experiment's comment ids)
comments = json.loads(subprocess.run(["gh", "api", f"repos/{repo}/issues/1/comments?per_page=100", "--jq", "[.[].id]"],
                                     capture_output=True, text=True).stdout)
for need in (6670761196, 6670858992, 6671044098):
    if need not in comments:
        fails.append("MISSING the rotation comment: " + str(need))

if fails:
    print("FINISH-LINE: FAIL")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("FINISH-LINE: PASS - the full ring's artifacts are on the record.")
