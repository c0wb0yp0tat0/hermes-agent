# RUNNER-RECON-20261120 — the runner estate's failure classes, reconned to their roots (the head-rendered register)

*The Nemo judge lane's tool-loop ceiling, measured conclusively: the harness route DEAD-RUN'd at round 24 (8 content-only rounds, no fabrication) · the board route ran SIX rides across two cards, each a protocol violation (the worker's output = pure narration, never a terminal board call — even with the floor-zero contract). The seat's judgment-class strength is unreserved; the tool-steering class is the ceiling, named. Per the doctrine's "re-arm on a Proven lander or the head," THIS register is HEAD-RECON: rendered from the receipts (the workflows' bytes on main, the runs' logs, the cadence rows), every claim tagged [HEAD-RECON] or [BORROWED <receipt>].*

## THE CLASS-REGISTER (per class: the receipts → the 5-Why root → the fix → the status)

### 1. creative-copycat — FIXED (main, read-back verified)
- **Receipts [BORROWED rows + logs]:** runs 44657463552 · 44685324283 · 44685408645 · 44771662842 — "cd: /root/workspace/repos/hermes-agent: Permission denied" on the 241 floor (runner user, no /root access).
- **5-Why root:** the workflow's `run:` hardcodes `REPO="/root/workspace/repos/hermes-agent"` into a runner-executed `cd` — a HOST-absolute path in a workflow designed for the dispatcher's registry (main), where the executing runner's home differs by floor. The K3 fixed-path seed was named 2026-11-20 00:43; the fix never landed on MAIN (the dispatch reads main's bytes).
- **Fix (applied this pass, main a27457c5… replaced):** a checkout step (the dispatched ref) + `REPO="${GITHUB_WORKSPACE}"` — the runner-agnostic form. Read-back verified on main.
- **Status:** APPLIED; the next arm's ride proves it (its GREEN is the receipt).

### 2. fill-queue — FIXED (main, read-back verified)
- **Receipts [logs + rows]:** runs 44770762830 · 44751094175 · 44734346016 · 44716995728 · 44700946026 — the receipt rows posting `RFC143379-RIG-ENVELOPE-FILL-LEG-$RUN` with the literal `$RUN`/`$PIN` unexpanded — flagged repeatedly by the rows themselves ("the template posted unexpanded").
- **5-Why root:** the receipt step's python heredoc is QUOTED (`<<'PY'`) yet the script reads `pin = "$PIN"` — the shell never expands the variables inside a quoted heredoc, so the python receives the literal strings and posts them verbatim. The runner's env never carried the values either.
- **Fix (applied this pass, main e45f3913… replaced):** the env-pass form — `PIN="$PIN" RUN="$RUN" python3 - <<'PY'` with `os.environ` reads inside; the machine-log now posts the real run/pin. Read-back verified on main.
- **Status:** APPLIED; the next fill's row is the proof.

### 3. kindness-patrol — ROOT FOUND, SHAPE = THE OPERATOR'S WORD
- **Receipts [rows]:** runs 44759463610 · 44732854163 · 44707545176 — "the patrol step failed, the commit + receipt steps skipped" (the standing class, receipted all day).
- **5-Why root [HEAD-RECON]:** the workflow's FILE IS ABSENT from main's registry — the runs' history names "kindness-patrol" but no file in `.github/workflows/` matches (the full 67-file listing checked). The arm is headless: its dispatches (cron-side) produce the runs whose steps fail at the missing bytes, and the commit/receipt steps skip behind it. The RED is the expected class of a vanished arm, not a flaky step.
- **Fix shape:** two-way — (a) retire the cron's patrol dispatch (the arm's gone; the receipt's the honest no-op) or (b) restore the file if the patrol's duty stands. This is the operator's call; nothing is invented in its place.

### 4. The K2 env families — TWO FIXED EARLIER, THE THIRD APPLIED THIS PASS
- **HOME-unbound [fixed 680ce1d367]:** the systemd runner's job-env lacks HOME — the key-carrier now `-u`-safe + getent-resolved.
- **The floor key-shape [fixed]:** the carrier reads agent_key | access_token with the KEY-ABSENT fail-loud.
- **The mirrors' evidence-void ledgers [fixed THIS pass]:** run 44745081209's ledgers = 10/10 harness errors with the HTTP body SWALLOWED inside the battery's catch — the two-line instrumentation now logs `reader_last_error` (the code + the first 120 chars) into every arm's ledger row. The next 10/arm re-fire's ledgers will NAME the class instead of vanishing it.

### 5. canary-release — the closure pending the queue's terminal verdict
- **Root [HEAD-RECON]:** runs-on `blacksmith-4vcpu-ubuntu-2404` — the hosted label's queue never assigns (the fork's registration state; the stale entries 43858174350 + 44253887362 cancelled by queue-age). The fresh dispatch 44787964389 = the closure's attempt; GREEN/RED/NOT-RUN all close the cadence's dead letter; NOT-RUN is a legitimate, receipted terminal state.

### 6. The identity truth (reconciled 2026-11-20)
p0tat0 = the 241 floor (machine c0wb0yp0tat0, Linux, user c0wb0y) · pve1-avrea-parallel = THIS host (systemd root) · c0wb0y = Windows, the same 241 · the cloud = the fourth. Every future runner-table cites this map.

## THE REPAIR ORDER (executed)
1. creative-copycat's path (main) — done, read-back verified.
2. fill-queue's receipt-row heredoc (main) — done, read-back verified.
3. The battery's reader instrumentation (the branch) — done this pass.
4. The patrol's shape — the operator's word (retire vs restore).
5. The canary's closure — the queue's terminal verdict, watched by the cadence.

## COMPOSE-CHECK (8 marks)
| mark | state | evidence |
|---|---|---|
| deconstruct | FIRED | the 6 classes, each with its receipts ([BORROWED rows/logs] or [HEAD-RECON]) |
| sense | FIRED | the bytes read cold — the workflows on main + the run-logs' actual steps |
| choose | FIRED | the fix per root (env-pass, workspace-relative, instrumentation), never a symptom patch |
| calibrate | FIRED | each fix names its reversibility (the main-file replace = re-PUT the old bytes; the instrumentation = revert the patch) |
| probe | FIRED | the next rides' GREENs are each fix's receipt (the arm, the fill's row, the ledgers' named errors) |
| review | FIRED | the ceiling's honesty (Nemo ×2 transports, SIX board rides, never a terminal call — no 7th try) |
| record | FIRED | this register + the applied commits (main a27457c5… / e45f3913… replaced; the branch's next commit) |
| compose-check | FIRED | this table |

**Fold line:** RUNNER-RECON 2026-11-20 — the layer's roots found and the fixable classes fixed (creative's host-path → workspace-relative · fill's quoted-heredoc → env-pass · the battery's swallowed HTTP error → ledged); the patrol's shape = the operator's word; the canary's closure = the queue's terminal verdict. The runner estate's recurrence loop closes on the next rides' receipts.
