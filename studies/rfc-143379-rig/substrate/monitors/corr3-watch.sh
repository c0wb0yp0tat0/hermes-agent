#!/bin/bash
# The CORR3 card's status — deterministic output for the monitor gate
hermes kanban list --json 2>/dev/null | python3 -c '
import json, sys
cards = json.load(sys.stdin)
for c in cards:
    if c.get("id") == "t_97e2f429":
        print("STATUS:" + c.get("status", "?"))
        break
'
