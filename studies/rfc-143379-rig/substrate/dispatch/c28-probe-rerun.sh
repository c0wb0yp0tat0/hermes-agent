#!/bin/bash
# C28 Phase 3 probe restart — first-line fail-safe for crashed probe
# Original probe (PID 2543691/2647811/2647817) died during Cell D4 after completing 3/8 cells
# No deliverables produced. Script intact (SYNTAX-OK), engine :44831 UP, 25 segments present.
# Results JSON: /root/.hermes/cache/scratch/c28-generation-results.json
# Verdict:       /root/.hermes/cache/scratch/c28-generation-verdict.txt
python3 /root/.hermes/cache/scratch/c28_generation_probe.py 2>&1 | tee /root/.hermes/cache/scratch/c28-generation-probe.log
echo "C28_PROBE_RERUN_DONE_EXIT=$?"
