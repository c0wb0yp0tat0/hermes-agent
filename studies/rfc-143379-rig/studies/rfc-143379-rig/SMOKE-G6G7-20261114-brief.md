# SMOKE RIDE — G6/G7/G13 certifying run (2026-11-14)

You are the certification lane of the hardened copycat harness (G6 byte-budget breaker, G7 single-call trim, G13 exit-code truth). This is a SMOKE TEST, not a mission.

## Task (do exactly this, in order, then stop)
1. Read this brief once.
2. Write the artifact with ONE write_file call (single call, per the harness's own new contract): a 3-line file with the text: "SMOKE-G6G7-20261114: certified by a real ride on the hardened harness." plus the current date line.
3. Commit + push exactly per the harness's emission contract (git add the artifact; git -c user.name='c0wb0yp0tat0' -c user.email='c0wb0yp0tat0@users.noreply.github.com' commit -q -m "SMOKE: G6/G7/G13 certifying ride"; git push origin study/rfc-143379-rig-20261105; on rejection: git pull --rebase origin study/rfc-143379-rig-20261105 then push).
4. Final message: "SMOKE-CERTIFIED" + the commit sha.

## Contract
- ONE tool call per round (the harness enforces the trim; do not batch).
- No reads beyond this brief; no archaeology; no drop/ paths.
- kenari READ-ONLY; nothing public; RFC quiet.
