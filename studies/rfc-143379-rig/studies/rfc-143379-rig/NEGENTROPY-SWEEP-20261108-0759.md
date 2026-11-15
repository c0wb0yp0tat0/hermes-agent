# NEGENTROPY-SWEEP-20261108-0759 — the scheduled sweep's receipt (cadence 2h, the negentropy arm's next-probe fire)

the gate: nothing public without the user's word

**Seat:** `stealth/crouton-alpha` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Fire:** 2026-11-08 07:59 · **Register:** receipts, never claims · **Hand-separation:** [1st] = re-read by this lane this pass (git trees, commit bytes); [2nd] = carried from a study doc, not re-derived. **Lane constraint:** git-only lane — shell greps and `gh api` probes rejected; window values and per-fork live statuses are UNMEASURED, not invented. **Prior sweep artifact:** `NEGENTROPY-SWEEP-20261108-0558.md` (commit `c544d3ad55`) — the delta baseline; HEAD at sweep-open `677319b8df`.

## (a) THE WINDOW-CHECK (the gate) — code-receipted, values-unmeasured → SEPARATION-UNMEASURED

| Check | Receipt (this lane's own bytes) |
|---|---|
| `grep -n "api_key\|base_url" /root/workspace/repos/hermes-compression-eval/run_eval.py \| head -5` | Executed as committed-tree read [1st]: `git -C /root/workspace/repos/hermes-compression-eval show HEAD:run_eval.py \| sed -n '70,92p'`; harness HEAD `b65773b` [1st]. |
| Gate code | `_resolve_runtime` (lines 70–90 [1st]): `if not runtime.get("api_key") and not runtime.get("base_url"): raise RuntimeError("No provider configured...")` — either-or gate, line 81 the receipted wall. Identical to the 0558 fire. |
| Runtime config presence (api_key/base_url values set?) | **UNMEASURED** [1st] — `resolve_runtime_provider` cannot be executed in this git-only lane; no values quoted, none invented. |
| W2-isolation settle-condition (`W2-ISOLATION-RUN-DESIGN-20261107.md`) | SPEC ON-BRANCH [1st]: blob `6677abc2…` + status `482b2714…`, byte-identical to 0558. Cannot run: window values unmeasured. |
| k-term two-tier re-measure | NOT RUN. Baseline [2nd] (ADJUDICATION-NEGENTROPY-20261106): kept-rates 0.42/0.29/0.26/0.32, flat 0.26–0.42, no class separation. |
| Budget consolidation re-verify | NOT RUN. Baseline [2nd] (NEGENTROPY-SWEEP-C-BUDGET-20261106): decision-core 3.00 > clock/exec-time 2.83 > next-action 2.33 > scope 2.00; descriptive weights only. |

**Verdict: SEPARATION-UNMEASURED.** W2 confound live [2nd]: "It survives into `summary_text` in runs 2–3 yet the answer is `""` in all three runs."
**Settle-condition re-armed:** the next fire re-attempts the values check (`resolve_runtime_provider` output / eval-start evidence past line 81); on OPEN, the W2-isolation re-run executes per its spec.

## (b) THE SEAM-SCAN — every fire, window or no

| Seam | Status this pass |
|---|---|
| Read-burn / harness-deadline | Correction `9836333f5a` stands [1st, blob carried via 0558 lineage]; no new harness commit since the prior fires (harness HEAD still `b65773b` [1st]). Read-burn 5-why countermeasure remains undelivered. |
| Alpha fair-share posture | Code receipts exist on-branch (commits `3bb910af78` fair-share 429 handling; `0c7c60acf6` fair-share review; `d5bbdbe3eb` free-tier 429 cooldown) [1st, git log]. Live fair-share state UNMEASURED. |
| Fabric latest conclusions | `FABRIC-CONCLUSIONS-20261108.md` landed [1st, HEAD commit `677319b8df`]: 31 forks' hosted-runner verdicts — 30/31 RED (checkout-class) at the universal pin, 30/30 GREEN at per-fork pins, study fork (`hermes-agent`) GREEN @ 02:00. Per-fork `gh api …/fabric-battery.yml/runs` reads remain UNMEASURED (git-only lane). FABRIC-RECEIPTS file unchanged: 60 queued + 1 in_progress + 0 concluded (blob `37e7347b…`, 70 lines [1st, counts re-derived by grep-class read this pass]). |
| Roster / `:free` catalog | No new `:free` additions receipted [1st]: `git ls-tree HEAD studies/rfc-143379-rig/` shows no roster/catalog rows new since 0558; WAVE3-UNIFIED-FOLD-20261108 confirms seats/legs unchanged from V5. |

## (c) THE SWEEP'S RECEIPT — counts + delta

**Counts:** window: code-RECEIPTED (harness `b65773b`, lines 70–90) / values-UNMEASURED (0 credential values quoted) → SEPARATION-UNMEASURED · seams scanned: 4 (read-burn, alpha, fabric, roster) + 2 baselines carried · fabric cells this pass: receipts-file 60 queued + 1 in_progress + 0 concluded (unchanged); conclusions artifact: 30/31 RED @ universal pin, 30/30 GREEN @ per-fork pins + study-fork GREEN · `:free` additions: 0 quoted · new branch commits since prior sweep: 10 (not 17).

**Delta vs prior sweep (NEGENTROPY-SWEEP-20261108-0558, commit `c544d3ad55`):** PAPER MOVED, WINDOW DID NOT. Changed since 0558 — 10 commits (`c6999a82e6` LENS-STATE, `2957b18c4f` LENS-OUTCOME, `0be4eb528e` LENS-ARC, `f7d2e0de3f` LENS-READINESS, `d8febd2bd9` essence lens, `19197ed624` LENS-STATE, `6384e594ad` SWAP-PLAN, `b9abe04a80` falsification harness scripts — the blind's catch's build-task CLOSED [1st, commit subject], `0fee90d07a` Track1 #139606 composition, `677319b8df` FABRIC-CONCLUSIONS). The directorate: the licensed-fan's eight-lens wave completed and folded (WAVE3-UNIFIED-FOLD-20261108: READY-WITH-NAMED-SEAMS [1st]), the rig's acceptance-scripts now exist on-branch (blind catch closed), and the fabric's per-fork conclusions are rowed (30/31 RED @ universal pin is a NEW verdict line — it quantifies what the receipts file's 60-queued row left open).
Unchanged, therefore: window code receipt identical (harness `b65773b`, line-81 either-or gate); W2 spec/status blobs byte-identical; FABRIC-RECEIPTS still 60 queued + 1 in_progress + 0 concluded; harness-deadline correction unmodified; arm verdicts stand exactly as 20261106 baselines left them (k-term flat, budget descriptive-only, W2 confound live, SEPARATION-UNMEASURED).
**The one honest new fact this fire adds is the fabric's per-fork scoreboard:** the conclusions artifact gives the fleet its first complete hosted-runner census — RED-heavy at the universal pin, GREEN at per-fork pins — while the LLM window that gates the W2 settle-condition remains, as always, unmeasured in this lane.

**Finding one line:** NEGENTROPY-SWEEP-20261108-0759 — window code-receipted (harness b65773b, line-81 either-or gate) but runtime values UNMEASURED → SEPARATION-UNMEASURED; 10 new commits since 0558 (licensed-fan eight-lens wave + falsification scripts landed, fabric conclusions: 30/31 RED @ universal pin, 30/30 GREEN @ per-fork pins), receipts-file still 60 queued + 1 in_progress + 0 concluded, settle-condition re-armed.

**Next mechanism's one line:** the 09:57 fire re-attempts the window's *values* check (resolve_runtime_provider output or eval-start evidence past line 81) and, on OPEN, runs the W2-isolation settle-condition with its spec on-branch — until then the arm holds SEPARATION-UNMEASURED, receipts only, and the eight-lens paper is receipted as exactly that.
