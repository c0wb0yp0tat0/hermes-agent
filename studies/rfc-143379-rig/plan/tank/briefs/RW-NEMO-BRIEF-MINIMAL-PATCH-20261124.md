# FLEET-BRIEF NEMO — MINIMAL PATCH (run the exact command, nothing else)

*Seat (pin): `mistralai/mistral-nemo`. The operator's standing: Nemo does the patching. The prior succession fires failed to EXECUTE — they emitted tool-call syntax as text. THIS fire has ONE job: run the verbatim command below, then verify. Nothing to compose, nothing to decide beyond the verification rule.*

## THE ONE COMMAND (run it exactly; the file is the committed note with Nemo's footer, ce07011bfa7)

```
gh api --method PATCH repos/NousResearch/hermes-agent/issues/comments/7147011435 -f body="$(cat /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-20261124.md)"
```

Run it via the `terminal` tool — NOT inside a JSON code block, NOT as a quoted string in prose. The tool call's arguments dict must contain exactly `{"command": "<the command above>"}`.

## THE ONE VERIFICATION (run after the patch)

```
gh api repos/NousResearch/hermes-agent/issues/comments/7147011435 --jq '.body'
```

The fetched body must contain real `—` em-dashes and real line breaks, and the footer must read `*Prepared with Hermes and Nemo, reviewed by c0wb0yp0tat0 before posting.*`. If the fetch shows literal `\u2014` or `\n` text, the patch did NOT apply right — re-run the patch command, then re-fetch.

## THE ARTIFACT (after the verification)

Write a SHORT receipt to `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-INTERIM-NOTE-FORMAT-20261124.md`:
1. The patch command's exit/output (the comment id).
2. The fetched body's first line + the footer line (quote them exactly).
3. One line: PATCHED-CLEAN or PATCHED-AGAIN-NEEDED.
4. The git add + git commit of the receipt (local, no push).

## Write-window

`write-window: 8` — patch first, verify, receipt by round 7. NO stub markers.

## Hard lines

- PATCH ONLY comment 7147011435. Nothing else.
- No installs. Local commits only, NEVER push/pull. Never checkout/stash/rm.
- THE WITNESS RULE: the fetched bytes decide — an escaped-fetch comparison is the failure class.

## Emission

Exit 0 = the receipt EXISTS on disk, re-read, committed; report names the sha. No tool-call syntax in final words.
