#!/usr/bin/env bash
# DISPATCH-LABEL-PROBE (the label-slug's crown-adoption, 2026-11-09)
# Before ANY workflow-dispatch: verify the workflow's runs-on labels resolve to a
# REGISTERED runner. Fail fast, name the mismatch — never let an unmatchable job
# enter the queue (the ~6h queued-forever was precisely this hole).
set -uo pipefail
REPO="${1:-c0wb0yp0tat0/hermes-agent}"
WORKFLOW="${2:-}"
LABEL="${3:-}"

if [ -z "$WORKFLOW" ] || [ -z "$LABEL" ]; then
  echo "usage: dispatch-label-probe <repo> <workflow-file> <runs-on-label>"
  exit 2
fi

# the registered runners' labels (the platform's own registration — the truth)
REGISTERED=$(gh api "repos/$REPO/actions/runners" --jq '.runners[].labels[].name' 2>/dev/null | sort -u)
if [ -z "$REGISTERED" ]; then
  echo "PROBE-FAIL: cannot read the runner registration (gh api failed) — ABORT the dispatch"
  exit 1
fi

if echo "$REGISTERED" | grep -qx "$LABEL"; then
  echo "PROBE-PASS: label '$LABEL' is registered — dispatch may fire ($(echo "$REGISTERED" | grep -c .) labels on the pool)"
  exit 0
else
  echo "PROBE-FAIL: label '$LABEL' matches NO registered runner."
  echo "registered labels: $(echo "$REGISTERED" | tr '\n' ' ')"
  echo "the dispatch MUST NOT FIRE — fix the runs-on to a registered label first."
  exit 1
fi
