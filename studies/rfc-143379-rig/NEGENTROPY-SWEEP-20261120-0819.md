# NEGENTROPY-SWEEP-20261120-0819 — the recurring sweep

**seat:** negentropy-sweep lane (cadence 2h, no_agent arm) · **branch:** `study/rfc-143379-rig` · **fire time:** 2026-11-20 08:19
**the gate: nothing public without the user's word.**

## THE REGISTER (binding)
Receipts, never claims. **[1st]** = re-derived by this lane this pass (committed bytes via `git rev-parse`/`status`/`ls-remote`, `read_file` of HEAD files). **[2nd]** = carried from a study doc, not re-derived here. **ABSENT + named** = could not be received this pass. Claims tagged `IN-LANE` / `BORROWED <source>` / `HEAD-RECON`.
- Local HEAD `a152708eb7` [1st]. Origin ref `study/rfc-143379-rig` = `982e1eaaeab` [1st]. Local checkout name is `study/rfc-143379-rig-20261105` [1st] — note the name split from the push target.

## 1. THE WINDOW-CHECK (the gate)
| # | standing item | state this fire | receipt |
|---|---|---|---|
| W1 | **W2-isolation settle-condition** | **CHECKED, unchanged.** Verdict `SEPARATION-UNMEASURED`: the eval-runtime LLM-window is CLOSED (`run_eval.py:81` keys on absent `api_key`/`base_url`), so the one re-run isolating probe-answering from the handoff guard stays ARMED-NOT-LANDED. | [1st] `studies/rfc-143379-rig/W2-ISOLATION-STATUS-20261106.md` (read this pass) |
| W2 | **k-term two-tier re-measure** | **CARRIED, not re-run.** Baseline kept-rates 0.42 / 0.29 / 0.26 / 0.26 (span 0.26–0.42) = FLAT; the budget's class ordering presupposes differential keep-rates, so the flat k-term contradicts it. Needs the two-tier harness (machine-side). | [2nd] BORROWED recurring-brief §1; [2nd] 0618 carry |
| W3 | **budget consolidation re-verify** | **CARRIED, not re-run.** `decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00`; no fresh re-measure inputs exist in-lane. | [2nd] BORROWED recurring-brief §1; [2nd] 0618 carry |

## 2. THE SEAM-SCAN (every fire)
| seam | current state | receipt |
|---|---|---|
| **read-burn harness-deadline** | **FELT LIVE.** Two content-reads refused mid-analysis (`READ-GATED … write-window is open`). The transport gates reads once the artifact is near-due; analysis must be front-loaded. | [1st] `git grep` + `git cat-file` refusals this fire |
| **fold checks** (scribe cell → `get_memory` byte-compare; served `?raw=1` grep) | DESIGNED, not runnable in-lane (byte-compare needs `get_memory`, machine-side). **Named defect:** the tracked nested dup `studies/rfc-143379-rig/studies/**` double-counts any `?raw=1` grep → fold verification must de-dup its roots. | [1st] `git ls-files` nested-dup listing |
| **token watcher's single-source line** | **NOT CONVERGED + UNFED.** Origin `982e1eaaeab` ≠ local HEAD `a152708eb7` at fire start; and the line the arming declared the single source (`NEGENTROPY-ARM-EXECUTE-20261119.md`) still reads the placeholder `~21:xx` — never written. | [1st] `ls-remote`, `rev-parse`, `read_file` |
| **machine-layer wire-checks** (scribe tunnel, runners, Harbor/local-LM) | ARMED-NOT-VERIFIED. In-lane runs are forbidden; these stay head-executed rows. | [2nd] BORROWED arm-execute §4 |
| **dispositions** | Three classes held: AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR (+ chair-packets). Membership detail not re-readable this fire (read-gate) — carried at class level only. | [2nd] BORROWED arm-execute §5–§6 |

## 3. THE ENTROPY CLASSES
- **Dead surface.** `NEGENTROPY-SWEEP-20261117-0417.md` is ABSENT from HEAD's tree (ENOENT) though commit `ed3e4cf027` sits in the branch log and is itself not resolvable in this clone (`git show` → unknown revision). *Countermove:* head confirms renamed-vs-deleted; restore or mark dead.
- **Loose threads.** (a) `SCRIBE-WITNESS-REGISTRY.log` dirty — ` M` in `git status -sb` [1st], uncommitted live bookkeeping. (b) The arm-execute loop-state placeholder `~21:xx` never advanced — the token's owner never wrote the file it designated. (c) The nested dup is still tracked. (d) The flat k-term vs budget ordering contradiction is unreconciled.
- **Friction points.** The branch-name split (local `-20261105` vs remote `rfc-143379-rig`) plus remote-ahead forces the pull-rebase dance every fire; the read-gate truncates late analysis.
- **UNSPOKEN (the prize).** The watcher is **armed-but-unfed**: the arming made a file the single source, and that file's line is still a placeholder, so the sentinel watches a value nobody updates — the wiring is ceremonial, not live. *Countermove:* head writes the line (`UPDATED <ts> · <stage> · <owner>`) and re-points the watchers, or re-declares the token's home.
- **Second unspoken.** The delta baseline ("last sweep artifact") skips non-sweep landings: remote advanced to `982e1eaaeab` with no new sweep artifact between 0618 and this fire. *Countermove:* baseline = HEAD's last `NEGENTROPY-SWEEP-*` file, not wall-clock cadence.

## 4. THE ORDERED NEXT-MOVES
1. **Head writes/feeds the arm-execute loop-state line** (kills the ceremonial sentinel). Gate: the gate. Seat: head.
2. **Head converges the branch**: fetch `982e1eaaeab`, reconcile local `-20261105` vs remote `rfc-143379-rig`. Gate: the gate. Seat: head.
3. **Row the nested dup** (archive or delete; stops grep double-count). Gate: the gate. Seat: head/chair.
4. **Commit or revert the dirty registry log.** Gate: the gate. Seat: head.
5. **Land the W2 settle-condition** when the eval-window opens. Gate: the gate. Seat: head.
6. **Re-measure the k-term two-tier** (flat result vs budget ordering). Gate: the gate. Seat: head (machine).

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS
1. Header (seat/branch/fire-time/gate/register) — present above [1st].
2. Window-check table, three rows receipted — W1 [1st], W2/W3 [2nd].
3. Seam-scan rows with receipts — five rows above [1st]/[2nd].
4. Entropy classes, each WITH its countermove — four classes + two unspoken.
5. Ordered next-moves, each with gate + seat — six rows.
6. Compose-check + stamps — this section.
7. Loop-state line — §6 below.
8. Commit + push receipt — landed `f825303314` on `origin/study/rfc-143379-rig` (fast-forward `982e1eaaea..f825303314`) [1st]; `ls-remote` re-read confirms `f825303314`.

## 6. THE LOOP-STATE LINE
**CONTINUE + head feeds the arm-execute loop-state line (kills the armed-but-unfed sentinel) and converges `982e1eaaeab` with local `-20261105`.**
Receipts: HEAD `a152708eb7`→pushed `f825303314`, origin pre-push `982e1eaaeab`, registry `M SCRIBE-WITNESS-REGISTRY.log` [1st]; W2 `SEPARATION-UNMEASURED`, k-term flat, budget 3.00/2.83/2.33/2.00 [2nd].
