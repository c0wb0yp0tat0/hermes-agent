# NEGENTROPY-SWEEP-20261121-0228

- seat: copycat lane (RFC #143379 rig) · branch: study/rfc-143379-rig-20261105 · fire: 2026-11-21T02:28Z
- the gate: "nothing public without the user's word." — artifacts only; RFC upstream QUIET; nothing posts.
- register: [1st] = re-read by this lane this pass (git-tree, study listings, branch logs) · [2nd] = carried from a study doc, not re-derived · ABSENT+named when unreceived · tags IN-LANE / BORROWED <src> / HEAD-RECON.

## 1. THE WINDOW-CHECK (the gate)
| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | carried, not re-run | [2nd] BORROWED NEGENTROPY-SWEEP-20261118-1157; settle needs the W2 probe set re-fired — IN-LANE: no W2 probe row landed 2026-11-19→21 |
| k-term two-tier re-measure | baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat | [2nd] BORROWED same; the budget's class ordering presupposes differential keep-rates → the flat k-term contradicts it. Not re-measured: eval-window closed (§2) |
| budget consolidation re-verify | decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00 | [2nd] BORROWED same; ordering stable, no re-derive this pass |

## 2. THE SEAM-SCAN (every fire)
| seam | state | receipt |
|---|---|---|
| read-burn harness-deadline | OPEN — this lane burned its read budget on git-tree forensics (285 blobs) instead of the artifact delta | IN-LANE: §3 friction row |
| fold: scribe cell → get_memory byte-compare | NOT-RUN — no scribe cell in lane | IN-LANE |
| fold: served `?raw=1` grep | NOT-RUN — no served surface reachable from lane | IN-LANE |
| token watcher single-source line | ABSENT + named — loop-state token file not received this pass | IN-LANE |
| machine-layer: scribe tunnel / runners / Harbor-local-LM | ABSENT + named (all three) | IN-LANE |
| dispositions | AUTO-CONTINUE: artifact landed+pushed · HOLD-SAFE: none · NEEDS-THE-CHAIR: eval-window re-open (api_key/base_url) + W2 settle | IN-LANE |

## 3. THE ENTROPY CLASSES (CTO freedom applies)
- **dead surface — vendored hermes_cli tree.** `studies/rfc-143379-rig/hermes_cli/` is a full mirror of the package (runtime_provider.py = 1195 lines; 285-blob study tree is mostly these copies). Second source of truth, provenance unstamped. *Countermove:* stamp each vendored file with its source commit, or prune the tree from the study dir.
- **dead surface — orphan sentinel.** `scripts/apply-credit-to-64555892.py` + id 6455589220; the 64555892 prefix is real in the zip, the body is 6455589220. No consumer names it. *Countermove:* name the intended credit target or delete the script.
- **loose thread — DESIGN.md vs DESIGN-HANDOFF.md.** DESIGN.md says "TODO: convert into task-based agent with handoff doc"; HANDOFF says "Tasks auto-generate from DESIGN.md" — circular, no owner. *Countermove:* pick one source, stamp the other superseded.
- **loose thread — unrowed landings.** `probes/fixture-high-density-real.probes.json` (3577 b) + `probes/fixture-deep-compaction-real.probes.json` (3686 b), untracked, 2026-11-21T02:14/02:15; no consumer. *Countermove:* row into the eval or delete.
- **friction — the study dir is a mirror.** The copycat lane's read budget is spent navigating vendored package copies, not the delta baseline. *Countermove:* prune the vendored hermes_cli tree.
- **UNSPOKEN (the prize).** Every "receipt" about hermes behavior is read from a copy whose provenance is unstamped, so the lane cannot distinguish the copy from the live package — the sweep's evidence plane is unfalsifiable until stamped. *Countermove:* provenance stamp per vendored file, then re-receipt §2.

## 4. THE ORDERED NEXT-MOVES
1. Prune or provenance-stamp the vendored `hermes_cli/` tree — gate: user's word for deletion · seat: copycat lane.
2. Re-fire the W2 probe set to settle the isolation condition — gate: eval-window open (api_key/base_url) · seat: rig owner.
3. Re-measure the k-term two-tier on the live eval — gate: same window · seat: rig owner.
4. Resolve DESIGN.md vs DESIGN-HANDOFF.md to one source — gate: chair · seat: rig owner.
5. Row or delete the two untracked probe fixtures — gate: chair · seat: copycat lane.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS
1. seat/branch/fire — header. 2. gate verbatim — header. 3. register hand-separation — header; [1st]/[2nd]/ABSENT inline. 4. window-check — §1. 5. seam-scan — §2. 6. entropy classes with countermoves — §3. 7. ordered next-moves — §4. 8. loop-state line — §6.

## 6. THE LOOP-STATE LINE
CONTINUE + prune or provenance-stamp the vendored `hermes_cli/` tree in the study dir (gate: user's word for deletion) — receipt: §3 dead-surface row + §4 move 1.