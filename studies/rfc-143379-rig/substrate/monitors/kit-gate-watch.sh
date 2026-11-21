#!/bin/bash
# kit-gate-watch: the read-restore fix's gate-watch. Quiet while the gate's open;
# emits the moment the read-restore PR merges (the pilot's start-line).
# The read-restore PR: upstream NousResearch/hermes-agent #116673 (the memory-read restore).
PR_NUM=116673
STATE=$(gh api repos/NousResearch/hermes-agent/pulls/$PR_NUM --jq '{state:.state, merged:.merged}' 2>/dev/null)
echo "$STATE" | grep -q '"merged":true' && echo "KIT-GATE: the read-restore fix (#116673) has MERGED — the pilot's start-line is open. The operator's word gates the start; the kit's readiness-list is the prep."
# the quiet path: NO OUTPUT — the stateful contract's silence is real, never a reported quiet
# THE EXIT-CODE FIX (earned 2026-11-08): the quiet path must exit 0 — grep -q's no-match
# exit 1 flagged every tick as a cron ERROR, killing the gate-watch's health signal.
exit 0
