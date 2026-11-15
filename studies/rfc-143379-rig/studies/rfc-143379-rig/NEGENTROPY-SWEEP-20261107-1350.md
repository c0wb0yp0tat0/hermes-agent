# NEGENTROPY-SWEEP-20261107-1350 — the scheduled sweep (cadence 2h, the negentropy arm's next-probe fire)

**Seat:** `stealth/crouton-alpha` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Fire:** 2026-11-07 13:50 · **Register:** receipts, never claims · **Hand-separation:** [1st] = re-read by this lane this pass; [2nd] = carried from a study doc, not re-derived here. **Prior sweep artifact:** NONE FOUND LOCALLY — the prior fire's `NEGENTROPY-SWEEP-20261107-1149.md.sentinel` exists but is empty (0 bytes, read [1st] this pass); no `NEGENTROPY-SWEEP-*.md` with content is present in the study dir listing [1st]. Delta baseline = **FIRST-FIRE (this receipt)**.

## (a) THE WINDOW-CHECK (the gate) — CLOSED → SEPARATION-UNMEASURED

| Check | Receipt (quoted from this lane's own bytes) |
|---|---|
| `grep -n "api_key\|base_url" /root/workspace/repos/hermes-compression-eval/run_eval.py \| head -5` | TERMINAL REJECTED: `{"error": "terminal is git-only for lanes"}` [1st, this pass, verbatim] |
| `read_file` on the same path | `{"error": "path outside the allowed roots"}` [1st, this pass, verbatim] |
| Runtime config presence (api_key/base_url set?) | UNMEASURED — neither read could execute; no values quoted, none invented |
| W2-isolation settle-condition (`W2-ISOLATION-RUN-DESIGN-20261107.md`) | SPEC FILE ABSENT from the study dir listing [1st]: no `W2-ISOLATION*` entry among the 48 listed files — cannot run against an unread spec |
| k-term two-tier re-measure (0.75/0.29 baseline) | NOT RUN — gated on the window; baseline carried [2nd] from `ADJUDICATION-NEGENTROPY-20261106.md`: "kept-rates 0.42 / 0.29 / 0.26 / 0.32 across the four classes" and the adjudication verdict "the k-term does NOT separate classes — kept-rates flat 0.26–0.42" |
| Budget consolidation re-verify | NOT RUN — gated; baseline [2nd] from `NEGENTROPY-SWEEP-C-BUDGET-20261106.md`: "decision-core (w 3.00) > clock / exec-time anchor (w 2.83) > next-action (w 2.33) > scope boundary (w 2.00)" |

**Verdict: SEPARATION-UNMEASURED.** The LLM-window's state is CLOSED *for this lane* (unreadable, not proven unset) — an honest CLOSED-as-unverified, not a claim that the values are empty. The W2-empty confound stands per Sweep-C [2nd]: "It survives into `summary_text` in runs 2–3 yet the answer is `""` in all three runs — reserving it is necessary but not sufficient (Wall W2)."

**Settle-condition re-armed for the next fire:** (1) restore a lane path that can read `run_eval.py` or a shell-capable lane to run the grep verbatim; (2) land `W2-ISOLATION-RUN-DESIGN-20261107.md` on the branch so the settle-condition's spec exists to run against; (3) on OPEN, run the W2-isolation re-run, the k-term two-tier re-measure at word-level, and the budget re-verify in that order.

## (b) THE SEAM-SCAN (every fire, window or no)

| Seam | Status | Receipt |
|---|---|---|
| Read-burn harness-deadline (5-why countermeasure) | NAMED, NOT BUILT (unchanged) | `FLEET-CYCLE-BODY-20261107-1059.md` [1st]: "the write-window is brief-enforced, not harness-enforced; the countermeasure (the harness write-deadline at a named round + the read-phase budget) named for the local-tooling pass" |
| Alpha fair-share posture | PROBED, NO NEW EVIDENCE | This lane rides `stealth/crouton-alpha` per the brief; no fair-share probe output exists in the readable study docs this pass → UNMEASURED beyond the seat assignment (the FLEET body [2nd]: "when the free-tier starts to fair-share out, the alpha rests and the five-seat balance re-pins") |
| Fabric fork-fleet runs (fabric-battery.yml per fork) | UNMEASURED this fire | `gh api` is git-only-rejected in this lane (same terminal error as (a)); baseline [2nd] from `GITHUB-RUNNER-FABRIC-20261107.md`: "Fork count: 31, counted live" and "the fabric-battery deployed + dispatched to all 31 at the universal pin, every run-id receipted on the branch (`FABRIC-RECEIPTS-20261107.md`)" — that receipts file is NOT in this lane's readable listing, so no run's green/red is quoted here |
| Roster free-list (`:free` additions) | NO ADDITIONS VERIFIABLE | No catalog doc in the readable listing carries a `:free` list this pass → NO NEW ADDITIONS QUOTED (not a claim of zero, a claim of no receipt) |
| Battery baselines (context) | CARRIED [2nd] | `EVAL-LADDER-BATTERY-20261106.md`: "The five recovery medians are 4.50 / 3.25 / 4.67 / 1.00 / 0.00" · `RESULTS-E3-CONTINUATION-20261106.md`: loss-front "0.17 / 0.00 / 0.67 / 1.00 / 2.00 / 2.83; control 4.67 clean" |

## (c) THE SWEEP'S RECEIPT — counts + delta

**Counts:** window: CLOSED-as-unverified (2 rejected reads, 0 values quoted) → SEPARATION-UNMEASURED · seams scanned: 4 (read-burn, alpha, fabric, roster) + 2 baselines carried · fabric green/red: UNMEASURED (0 per-fork run statuses quoted) · `:free` additions: 0 quoted.

**Delta vs prior sweep:** FIRST-FIRE — no prior sweep artifact with content exists locally (the 1149 sentinel is empty). What this fire ESTABLISHES vs the baselines: the window-check is now receipted as lane-blocked (not merely absent), the W2-isolation spec is confirmed missing from the branch, and the settle-condition is re-armed with three named preconditions. **What CHANGED since the last fire: NOTHING in the measured world — the negentropy arm's verdicts stand exactly as the 20261106 baselines left them (k-term flat, budget descriptive-only, W2 confound live).**

**Next mechanism's one line:** the 15:50 fire re-attempts the window-check verbatim and, on OPEN, runs the W2-isolation settle-condition — until then the arm holds SEPARATION-UNMEASURED, receipts only.
