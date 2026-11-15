# NEGENTROPY-SWEEP-20261108-1000 — the scheduled sweep's receipt (cadence 2h, the negentropy arm's next-probe fire)

the gate: nothing public without the user's word

**Seat:** `stealth/crouton-alpha` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Fire:** 2026-11-08 10:00 · **Register:** receipts, never claims · **Hand-separation:** [1st] = re-read by this lane this pass (git trees, commit bytes, harness tree); [2nd] = carried from a study doc, not re-derived. **Lane constraint:** git-only lane — shell greps, `gh api` probes and `read_file` outside the allowed roots are rejected; window values and per-fork live statuses are UNMEASURED, not invented. **Prior sweep artifact:** `NEGENTROPY-SWEEP-20261108-0759.md` (commit `916ff594d0`) — the delta baseline; HEAD at sweep-open `916ff594d0` (zero new commits since the prior fire).

## (a) THE WINDOW-CHECK (the gate) — code-receipted, values-unmeasured → SEPARATION-UNMEASURED

| Check | Receipt (this lane's own bytes) |
|---|---|
| `grep -n "api_key\|base_url" /root/workspace/repos/hermes-compression-eval/run_eval.py \| head -5` | Executed as committed-tree read [1st]: `git -C /root/workspace/repos/hermes-compression-eval show HEAD:run_eval.py \| sed -n '70,92p'`; harness HEAD `b65773b401874863b3dab94d6b0bd3d19fd95688` [1st]. |
| Gate code | `_resolve_runtime` (lines 70–90 [1st]): `if not runtime.get("api_key") and not runtime.get("base_url"): raise RuntimeError("No provider configured. Run \`hermes setup\` or set provider credentials in the environment before running the eval.")` — either-or gate, line 81 the receipted wall. Identical to the 0759 fire. |
| Runtime config presence (api_key/base_url values set?) | **UNMEASURED** [1st] — `resolve_runtime_provider` cannot be executed in this git-only lane; no values quoted, none invented. |
| W2-isolation settle-condition (`W2-ISOLATION-RUN-DESIGN-20261107.md`) | SPEC ON-BRANCH [1st]: blob `6677abc234bb7f4a2e51abd25c008143a0e7f334` + status `482b2714287362c701388dc7e5378209b87dfe68`, byte-identical to 0759. Cannot run: window values unmeasured. |
| k-term two-tier re-measure | NOT RUN. Baseline [2nd] (ADJUDICATION-NEGENTROPY-20261106): kept-rates 0.42/0.29/0.26/0.32, flat 0.26–0.42, no class separation. |
| Budget consolidation re-verify | NOT RUN. Baseline [2nd] (NEGENTROPY-SWEEP-C-BUDGET-20261106): decision-core 3.00 > clock/exec-time 2.83 > next-action 2.33 > scope 2.00; descriptive weights only. |

**Verdict: SEPARATION-UNMEASURED.** W2 confound live [2nd]: "It survives into `summary_text` in runs 2–3 yet the answer is `\"\"` in all three runs — reserving it is necessary but not sufficient (Wall W2)."
**Settle-condition re-armed:** the next fire re-attempts the values check (`resolve_runtime_provider` output / eval-start evidence past line 81); on OPEN, the W2-isolation re-run executes per its spec.

## (b) THE SEAM-SCAN — every fire, window or no

| Seam | Status this pass |
|---|---|
| Read-burn / harness-deadline | Correction `9836333f5a` stands [1st, carried via 0759 lineage]; no new harness commit since the prior fires (harness HEAD still `b65773b` [1st]). Read-burn 5-why countermeasure remains undelivered. |
| Alpha fair-share posture | Code receipts exist on-branch (commits `3bb910af78` fair-share 429 handling; `0c7c60acf6` fair-share review; `d5bbdbe3eb` free-tier 429 cooldown) [1st, git log, carried via 0759]. Live fair-share state UNMEASURED in this lane. |
| Fabric latest conclusions | `FABRIC-CONCLUSIONS-20261108.md` [1st]: "Fabric 1.0 (universal pin): **30/31 RED on the checkout-class**"; "31/31 forks receipted with a run-id, 0 fabricated" (30/30 GREEN @ per-fork pins + the study fork's own GREEN). Per-fork `gh api …/fabric-battery.yml/runs` reads remain UNMEASURED (git-only lane). FABRIC-RECEIPTS file unchanged: 60 queued + 1 in_progress + 0 concluded [1st, grep counts this pass]. |
| Roster free-list | Catalog-scan quick probe [1st, `git grep ":free"`]: roster-pin rows unchanged from the APEX-OF-APEXES pin (flagship `reflection/beam-1.0-501b-a23b:free`, free quartet, alpha #6); **0 new `:free` additions** quoted since 0759. |
| Re-apex floor (`/root/.hermes/plans/2026-11-07_0135-reapex-shift.md`) | UNREADABLE in this lane [1st, `read_file` → `{"error": "path outside the allowed roots"}`]; carried [2nd] unchanged. |

## (c) THE SWEEP'S RECEIPT — counts + delta

**Counts:** window: code-RECEIPTED (harness `b65773b`, lines 70–90) / values-UNMEASURED (0 credential values quoted) → SEPARATION-UNMEASURED · seams scanned: 5 (read-burn, alpha, fabric, roster, re-apex floor) · fabric cells this pass: receipts-file 60 queued + 1 in_progress + 0 concluded (unchanged); conclusions artifact: 30/31 RED @ universal pin, 30/30 GREEN @ per-fork pins + study-fork GREEN · `:free` additions: 0 quoted · new branch commits since prior sweep: **0**.

**Delta vs prior sweep (NEGENTROPY-SWEEP-20261108-0759, commit `916ff594d0`):** NOTHING MOVED, WINDOW DID NOT. Changed since 0759 — no commits (`git rev-list --count 916ff594d0..HEAD` → `0` [1st]). Unchanged, therefore: window code receipt identical (harness `b65773b`, line-81 either-or gate); W2 spec/status blobs byte-identical (`6677abc2…` / `482b2714…`); FABRIC-RECEIPTS still 60 queued + 1 in_progress + 0 concluded; FABRIC-CONCLUSIONS still 30/31 RED @ universal pin with 31/31 run-ids; harness-deadline correction unmodified; roster free-list unmodified; arm verdicts stand exactly as the 20261106 baselines left them (k-term flat 0.26–0.42, budget descriptive-only, W2 confound live, SEPARATION-UNMEASURED). The prior sweep's PAPER MOVED / WINDOW DID NOT headline now reads as STILL — the first completely quiet inter-fire interval in this sweep series.
**The one honest new fact this fire adds is the empty one:** an interval with zero commits and zero drift — the sweep's receipt confirms the fleet's state is frozen, not merely slow, while the LLM window that gates the W2 settle-condition remains, as always, unmeasured in this lane.

**Finding one line:** NEGENTROPY-SWEEP-20261108-1000 — window code-receipted (harness b65773b, line-81 either-or gate) but runtime values UNMEASURED → SEPARATION-UNMEASURED; 0 new commits since 0759 (first quiet interval; fabric conclusions unchanged: 30/31 RED @ universal pin, 30/30 GREEN @ per-fork pins, receipts-file still 60 queued + 1 in_progress + 0 concluded), settle-condition re-armed.

**Next mechanism's one line:** the 12:00 fire re-attempts the window's *values* check (resolve_runtime_provider output or eval-start evidence past line 81) and, on OPEN, runs the W2-isolation settle-condition with its spec on-branch — until then the arm holds SEPARATION-UNMEASURED, receipts only, and the quiet interval is receipted as exactly that.
