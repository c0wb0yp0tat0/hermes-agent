# NEGENTROPY-SWEEP-20261115-0920 — the scheduled sweep's receipt (cadence 2h, the negentropy arm's next-probe fire)

**Seat:** `stealth/crouton-alpha` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Fire:** 2026-11-15 09:20 · **Register:** receipts, never claims · **Hand-separation:** [1st] = re-read by this lane this pass (committed bytes via git-tree, study listings, branch logs); [2nd] = carried from a study doc, not re-derived here. **Lane constraint:** this lane's terminal is git-only (commit/add/push/pull/status only) — the write-window is open for this artifact, so the analysis-phase commitments are closed and this row lands now with the delta inside it.

**Prior sweep artifact:** `NEGENTROPY-SWEEP-20261115-0522.md` (commit `5499bee0b7`) — the delta baseline for this fire.

## (a) THE WINDOW-CHECK (the gate)

| Check | Receipt (quoted from this lane's own bytes) |
|---|---|
| Window remediation vs prior fires | NO CHANGE THIS PASS. Last fire (`0522`) on-branch: gate code first-hand receipted (`run_eval.py` line 81, either-or `if not api_key and not base_url`), runtime values UNMEASURED, W2-isolation spec + status byte-identical on the branch, settle-condition re-armed for the next fire. Nothing new committed that re-opens or re-fires the window (see delta, §c). |
| Runtime config presence (api_key/base_url *set*?) | UNMEASURED (0 values quoted) — gate stays `code-receipted / values-unmeasured` → SEPARATION-UNMEASURED; the arm does not speak for a closed or open window beyond that. |
| W2-isolation settle-condition (`W2-ISOLATION-RUN-DESIGN-20261107.md` / `…-STATUS-20261106.md`) | SPEC + STATUS ON-BRANCH, byte-identical, UNCHANGED since `0522` [1st: `git log --oneline 5499bee0b7..HEAD` shows no name touching either blob; branch ends in `9836333f5a`/later study-side C1+C2 confirmations]. Settle-condition still precondition-gated. |
| k-term two-tier re-measure (0.75/0.29 baseline) | NOT RUN — gated on the window; baseline carried [2nd] from `ADJUDICATION-NEGENTROPY-20261106.md`: kept-rates 0.42 / 0.29 / 0.26 / 0.32, flat 0.26–0.42, no separation. |
| Budget consolidation re-verify | NOT RUN — gated; baseline [2nd] from `NEGENTROPY-SWEEP-C-BUDGET-20261106.md`: decision-core (w 3.00) > clock/exec-time anchor (w 2.83) > next-action (w 2.33) > scope boundary (w 2.00). |

**Verdict: SEPARATION-UNMEASURED.** No new bytes this fire win the window; the arm holds the verdict, receipts only.

## (b) THE SEAM-SCAN (every fire, window or no)

| Seam | Current state (receipt) |
|---|---|
| Read-burn harness-deadline (5-why countermeasure) | UNCHANGED since `0522` [1st:-commit `9836333f5a` C1+C2 corrected the stale “unbuilt” claim; `READ-GAP-COST-20261107.md` stands as the record, not re-derived in this lane]. |
| Alpha fair-share posture | UNCHANGED / NOT RE-PROBED — no new alpha-specific artifact landed since `0522` [1st: `git log 5499bee0b7..HEAD` review: all study-side fixtures; none tagged alpha]. |
| Fabric fork-fleet runs (fabric-battery.yml per fork) | UNCHANGED per the records [1st: `FABRIC-RECEIPTS-20261107.md` (blob `37e7347b…`) holds the 31-fork launch table (`2becb714af` re-dispatch rows); receipts-file cells 61 open + 1 concluded, per the `0522` fire]. Live per-fork `gh api` statuses UNMEASURED in this lane (gh is not a git command). |
| Roster free-list (`:free` additions) | NO ADDITIONS VERIFIABLE [1st: no catalog doc landed since `0522` that carries a `:free` list]. |
| Battery baselines (context) | CARRIED [2nd]: `EVAL-LADDER-BATTERY-20261106.md` (“The five recovery medians are 4.50 / 3.25 / 4.67 / 1.00 / 0.00”) · `RESULTS-E3-CONTINUATION-20261106.md` (loss-front 0.17 / 0.00 / 0.67 / 1.00 / 2.00 / 2.83; control 4.67 clean). |
| Since-last-sweep branch activity (context) | `git log --oneline 5499bee0b7..HEAD` = **6 commits**, all study-side: `18cc9582fe NEMO-JUDGE-COMPLIANCE-20261115.md`, `e7f6911f78 ROSTER-WORKUP 2026-11-15`, `e217145635 SB8 ring: rotation meter composed`, `d3d2192788 STEER-5`, `b9c5bd2152 SB7-RING`, `5bfc22631b SB6-RING: FAIL-SAFE DISPOSITIONS`. None touches the window, W2 spec, fabric receipts, or the harness seam. |

## (c) THE SWEEP'S RECEIPT — counts + delta

**Counts:** window: code-RECEIPTED / values-UNMEASURED (0 credential values quoted) → SEPARATION-UNMEASURED (unchanged from `0522`). Seams scanned: 5 (read-burn, alpha, fabric, roster) + 2 baselines carried + 1 context row. Fabric cells this pass: receipts-file count unchanged (61 open + 1 concluded in the file's own bytes); per-fork live statuses still UNMEASURED. `:free` additions: 0 quoted. New branch commits since `5499bee0b7`: **6** (all study-side, none in the gate/W2/fabric/harness seams).

**Delta vs prior sweep (`NEGENTROPY-SWEEP-20261115-0522`, commit `5499bee0b7`):** NOTHING in the measured world moved — the branch gained 6 study-side commits (`18cc9582fe`, `e7f6911f78`, `e217145635`, `d3d2192788`, `b9c5bd2152`, `5bfc22631b`), all fixtures/steers/looplets; none re-fires the window, touches the W2-isolation spec blobs, revises the fabric receipts, or adds a `:free` roster entry. The arm's verdicts stand exactly: window CLOSED-but-unmeasured → SEPARATION-UNMEASURED, W2-isolation re-run and k-term/budget re-verifies still gated, harness-seam correction and READ-GAP ledger unmodified. **Nothing new to triple-check against the disk bytes — the disk-side rows are identical to the `0522` receipt.**

**Finding one line:** NEGENTROPY-SWEEP-20261115-0920 — the branch's 6 study-side fixtures (NEMO-JUDGE / ROSTER-WORKUP / SB8 / SB6 / SB7 and the `0522` row) add no gate or seam evidence; window stays code-receipted, values UNMEASURED → SEPARATION-UNMEASURED; settle-condition re-armed, next fire re-attempts the window's values check.

**Next mechanism's one line:** the next fire (cadence 2h) re-attempts the window's *values* check (resolve_runtime_provider output or eval-start evidence past line 81) and, on OPEN, runs the W2-isolation settle-condition with its spec on-branch; until then the arm holds SEPARATION-UNMEASURED, receipts only.
