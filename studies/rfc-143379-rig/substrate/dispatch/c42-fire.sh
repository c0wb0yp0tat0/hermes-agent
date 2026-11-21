#!/bin/bash
# C42 self-fire: post-generation citation-fidelity gate probe.
# Runs the C42 battery (5 queries at 0.60) through the harness,
# checks if model answers cite segments that actually contain the claimed facts.
# Session-surviving: fires once via cron, persists across session cleanup.
set -euo pipefail
export HARNESS_DEBUG=1
export METRIC_WINDOW_POS=1
export HARNESS_CACHE_THRESHOLD=0.60
export HARNESS_TEMPERATURE=0.0
python3 /root/.hermes/cache/scratch/c42-citation-fidelity-probe.py 2>&1
echo "C42 probe complete. Results: /root/.hermes/cache/scratch/c42-citation-fidelity-results.json"
