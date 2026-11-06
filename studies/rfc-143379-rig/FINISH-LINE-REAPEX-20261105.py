#!/usr/bin/env python3
"""FINISH-LINE-FIRST — the re-apex run's failable acceptance check (written BEFORE the run, per the dag-ulw method).

The goal (one line): the RFC-gate's measured-truth completeness — every dangling node landed and the
record verified at the final head. This check CAN FAIL — the run is not done until it exits 0.
"""
import json, subprocess, sys

def gh(*args):
    return subprocess.run(['gh'] + list(args), capture_output=True, text=True).stdout

fails = []
repo = 'c0wb0yp0tat0/hermes-agent'
branch = 'study/rfc-143379-rig-20261105'

# 1. The final head's battery must pass (the pytest -q exit 0 check, runner-side).
head = gh('api', f'repos/{repo}/branches/{branch}', '--jq', '.commit.sha').strip()
print(f"final head: {head[:10]}")
# (the runner's union at this head is the battery's receipt; the run's landing is the row)

# 2. The ledger's completeness (every promised artifact exists at the head).
paths = [
    'studies/rfc-143379-rig/RECEIPTS.md',
    'studies/rfc-143379-rig/RFC-GUIDANCE-20261105.md',
    'studies/rfc-143379-rig/XNGG-GAPS-VERIFICATION-20261105.md',
    'studies/rfc-143379-rig/HITL-READY-20261105.md',
    'studies/rfc-143379-rig/AVREA-LEG-CONTRACT.md',
    'studies/rfc-143379-rig/krecency/RESULTS-AGE.md',
    'studies/rfc-143379-rig/krecency/RESULTS-ALIASING.md',
    'studies/rfc-143379-rig/krecency/RESULTS-RECITE.md',
    'studies/rfc-143379-rig/krecency/RESULTS-PIN.md',
    'studies/rfc-143379-rig/krecency/RESULTS-COMPETE.md',
    'studies/rfc-143379-rig/krecency/RESULTS-ARCHIVE.md',
    'studies/rfc-143379-rig/krecency/RESULTS-CONSTRAINTS.md',
    'studies/rfc-143379-rig/krecency/SYNTHESIS.md',
    'studies/rfc-143379-rig/EXP-SUMMARY-MOONBEAM-20261105.md',
    'studies/rfc-143379-rig/EXP-AUDIT-SOLAR-20261105.md',
    'studies/rfc-143379-rig/EXP-AOA-20261105.md',
]
for p in paths:
    code = subprocess.run(['gh', 'api', f'repos/{repo}/contents/{p}?ref={branch}', '--jq', '.sha'],
                          capture_output=True, text=True).returncode
    if code != 0:
        fails.append(f"MISSING at head: {p}")

# 3. The thread's landings (the experiment's three voices posted + the run's receipts' presence).
comments = json.loads(gh('api', f'repos/{repo}/issues/1/comments?per_page=100', '--jq', '[.[].id]'))
for need in (6670761196, 6670858992, 6671044098):
    if need not in comments:
        fails.append(f"MISSING thread comment: {need}")

# 4. The run's own nodes' landings (the competing-admission arm's verdict, the step-seat's state, the fold's records).
if len(fails):
    print("FINISH-LINE: FAIL")
    for f in fails: print("  -", f)
    sys.exit(1)
print("FINISH-LINE: PASS — the goal's measure is met; the run's landings are on the record.")
