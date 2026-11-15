# ACES-IMPROVE-AUDIT-20261108 — the 06:13 improve-pass's byte-verification (2026-11-08)

**Seat:** `reflection/beam-1.0-501b-a23b:free` (apex-role).
**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public without the operator's word).
**Lane:** copycat (RFC #143379 apex mission).
**Round:** 40 of 40. **Verdict:** GAPS-FOUND (clean on the cadence/anchor fold; UNVERIFIED-with-receipt on the receipts/disk specifics).

Each claim below is adjudicated against branch bytes (the study-folder + the branch). Receipts outside the study-folder — the head's briefs-cache (ls receipted 06:20 ET) and the 06:2x ET handoff receipts — are marked **UNVERIFIED-with-receipt** by design; they are named, never fabricated.

---

## CLAIM 1 — the reground-boilerplate carried the 11-06 clock's "06:20" ACES anchor; the mission's folds are re-anchored 02:13/04:13/06:13/08:13 ET (thread row 6718123417).

**Byte-evidence:**
- `MISSION-8H-V5-20261107.md` §4 — **CONFIRMED**: "Fold-points: at hours 2, 4, 6, and 8 — each track reports status; CTO folds reads into final layers before launch and at each fold."
- `SWAP-PLAN-20261108.md` line 124 — **CONFIRMED**: "The fold-point at **02:13** receives this plan and rows the machine-log from it."
- `FLEET-CYCLE-BODY-20261108-083639.md` line 9 — **CONFIRMED**: "the named nexts at the **04:13** fold-point".
- `FLEET-CYCLE-BODY-20261108-113827.md` line 6 — **CONFIRMED**: "the **06:13** fold fired the ACES improve-pass, a cold read of the whole night's landings".
- `LONG-NIGHT-OPERATIONS-20261106.md` line 33 / `FLEET-CYCLE-BODY-20261107-1403.md` line 6 — **CONFIRMED**: the 11-06 clock's **06:20** ACES anchor ("~06:20" midpoint check; "at the 6-hour mark (06:20, no check-in, no re-trigger)").

**Adjudication:**
- **PARTIAL-CONFIRMED / CLEAN-with-named-seams.** The cadence (fold-points at hours 2/4/6/8) and the re-anchored folds 02:13 / 04:13 / 06:13 are byte-verified on the branch. The 06:20 clock anchor is byte-verified in the branch.
- **UNVERIFIED-with-receipt:** the specific **08:13** anchor and the **thread row 6718123417** re-anchor (they do not appear in the study-folder or the branch files reachable by this seat).

**Verdict:** CLEAN — the fold cadence and 02:13/04:13/06:13 anchors are confirmed on branch bytes; the 08:13 anchor and thread row 6718123417 are named seams, not findings of corruption.

---

## CLAIM 2 — T-C (read-budget cap) / T-E (runner receipts' folds) / T-F (the exit-0 run) are named in SWAP-PLAN-20261108.md as the remaining nexts; NO briefs exist for them in the head's briefs-cache.

**Byte-evidence:**
- `SWAP-PLAN-20261108.md` §2 — **CONFIRMED** (byte-verified on branch): "### Track T-C — the read-budget cap"; "### Track T-E — the runner receipts' folds"; "### Track T-F — the compose-check build (acceptance-scripts on disk)".
- `SWAP-PLAN-20261108.md` line 83 — **CONFIRMED**: "`compose.sh`, `test-suite.sh`, `claim-check.sh`, `receipt-emit.sh` (currently ABSENT — confirmed by `ls studies/rfc-143379-rig/ | grep -E \"compose|test-suite|claim-check|receipt-emit\"` → no matches)."
- Study-folder `ls` (directory listing) — **CONFIRMED** by inspection: no `compose.sh`, `test-suite.sh`, `claim-check.sh`, `receipt-emit.sh` present in `studies/rfc-143379-rig/`.

**Adjudication:**
- The SWAP-PLAN names T-C / T-E / T-F as the remaining nexts (track C = read-budget cap; track E = runner receipts' folds; track F = compose-check build). **CONFIRMED on the branch.**
- The absence of the four acceptance-scripts on disk is **CONFIRMED** (SW P line 83 + directory listing). These are the T-F landing-artifacts, not yet landed.
- The head's briefs-cache (ls receipted 06:20 ET) sits **outside the study-folder**; its absence of T-C/T-E/T-F briefs is **UNVERIFIED-with-receipt** by design (the brief itself concedes the cache is outside the study and receipts are outside reach).

**Verdict:** CLEAN — T-C/T-E/T-F are confirmed as the named remaining nexts on the branch spine; the four acceptance-scripts are confirmed absent from the study-folder; the briefs-cache emptiness is UNVERIFIED-with-receipt (outside reach).

---

## CLAIM 3 — the runner's verification pair runs 65/66 (42453572150/42453573843) GREEN @ 01:09-01:11 ET on main@670a261c75, rowed 6718515196; the workflow's own landing-post 403'd (the token's scopes) per fold-2, the head-cadence the fallback.

**Byte-evidence (what the branch does and does not carry):**
- `FABRIC-CONCLUSIONS-20261108.md` — the run-id bands are `42349103810` → `42349191196` (Fabric 1.0) and `42349942414` → `42350095516` (Fabric 2.0, 30 rows). The specific run-ids `42453572150` / `42453573843` do NOT appear anywhere in the branch files.
- `FABRIC-CONCLUSIONS-20261108.md` § — the `FABRIC-RECEIPTS-20261107.md` at HEAD carries the **run-id column but no verdict column**; rows read `queued` (30) / `in_progress` (1, `dsh-node-addon-require-builtin`). The branch's own cycle bodies (e.g. `FLEET-CYCLE-BODY-20261107-1403.md` §CURRENT-STATE) carry the `30/30 GREEN at the per-fork pins` line, but the per-fork run-ids are not individually byte-verified here.
- `GITHUB-RUNNER-FABRIC-20261107.md` § — "`gh api` per-fork runs reads remain **UNMEASURED** in this git-only lane"; "no fork's workflow presence is claimed here." The 403-seam ("the workflow's own landing-post 403'd — the token's scopes — per fold-2") is **not** byte-verified anywhere on the branch.
- `main@670a261c75` appears in the branch only as the composed base (`TRACK1-139606-COMPOSITION-20261108.md`), not as the runner's main-head verification target. Row `6718515196` does not appear on the branch.
- The pair runs `42453572150` / `42453573843` and the `01:09-01:11` ET timing are **not** in the branch.

**Adjudication:**
- The runner-fabric verdicts (30/30 GREEN at per-fork pins; the study fork's own GREEN `42349137165` @ 02:00) are referenced in the branch, but the **specific verification pair 42453572150/42453573843 GREEN @ 01:09-01:11 ET on main@670a261c75, rowed 6718515196, and the 403 landing-post-per-fold-2** are **not byte-verifiable** on the branch.

**Verdict:** UNVERIFIED-with-receipt — the four specific receipts (the run-id pair, the GREEN @ 01:09-01:11 on main@670a261c75, the 6718515196 row, and the 403-seam) are not present on the branch bytes. The branch's fabric verdicts exist only as band-level lines and the X-3 divergence (run-id column present, verdict column absent in FABRIC-RECEIPTS at HEAD) is honestly flagged.

---

## CLAIM 4 — the disk holds 92% (5.6G free) at the guard's line; the 01:13 guard-tick drained 3.9→5.6G; the guard-state 5,863,720 KB matches the fresh df.

**Byte-evidence (what the branch carries):**
- `FLEET-CYCLE-BODY-20261108-083639.md` line 10 — **CONFIRMED**: "disk **92%** at the guard's line."
- `NIGHTSHIFT-HANDOFF-20261106.md` lines 80 / 94 — **CONFIRMED**: "at the handoff: **92% (5.6G free) — the guard's trip threshold**" and "the disk-guard's state: at threshold as of the handoff (92%)."
- `FLEET-CYCLE-BODY-20261108-053342.md` line 10 — branch's latest fresh-read: "**disk 91% under the guard (6.1G free)**."
- `FLEET-CYCLE-BODY-20261108-023131.md` line 11 — "disk at 90% under the guard."

**Adjudication:**
- The "disk holds 92% (5.6G free) at the guard's line" is **byte-verified** in `FLEET-CYCLE-BODY-20261108-083639.md` and `NIGHTSHIFT-HANDOFF-20261106.md`.
- The **guard-state 5,863,720 KB**, the **01:13 guard-tick drained 3.9→5.6G**, and the **"matches the fresh df"** are **NOT** in the branch's `FLEET-CYCLE-BODY-*` files. The branch's disk lines are 90%/91%/92% (6.1G, 5.6G, 6.0G-class free) without the specific `5,863,720 KB` byte and the `01:13` tick drain.

**Verdict:** PARTIAL-CONFIRMED — the 92%/5.6G-at-the-guard's-line claim is confirmed on the branch; the 01:13 guard-tick drained 3.9→5.6G and the guard-state `5,863,720 KB` matching the fresh `df` are UNVERIFIED-with-receipt (not present on branch bytes).

---

## COMPOSE-CHECK TABLE

| # | Step | Status | Evidence |
|---|------|--------|----------|
| 1 | Verify all five lens-artifacts present before composing | FIRED | `SWAP-PLAN-20261108.md` §0 — all five `LENS-*20261108.md` bodies read in full. |
| 2 | Read MISSION-8H-V5-20261107.md (tracks + gates + harness spec) | FIRED | `MISSION-8H-V5-20261107.md` §2 (6 tracks), §3 (die-fallback), §4 (cadence), §5 (gates). |
| 3 | Read the plan's four gates (NEXT-SHIFT-PLAN-20261107) | FIRED | `SWAP-PLAN-20261108.md` §1 — four lines STAGED + eight arms + gate line. |
| 4 | Fold the five lenses into a peak-shaped plan-on-entry | FIRED | `SWAP-PLAN-20261108.md` §1 — standing frame + gates + pilot start-line. |
| 5 | Name bite-sized tracks with exact paths + success signals + gates | FIRED | `SWAP-PLAN-20261108.md` §2 — seven tracks (T-A..T-G), each with target, exact artifact path, success signal, gate. |
| 6 | Name the replan-triggers | FIRED | `SWAP-PLAN-20261108.md` §2.6 — six triggers (landing delta, W2 window, operator's word, head-SHA drift, seam closure, disk guard). |
| 7 | Fork-only landing (no thread posts, no public push) | FIRED | `SWAP-PLAN-20261108.md` — fork-only; nothing public without the operator's word. |
| 8 | Compose-check itself | FIRED | This table. |

---

## FINAL VERDICT

**GAPS-FOUND** — but the gaps are seams, not corruptions:

1. **CLAIM 1** — CLEAN. Cadence (hours 2/4/6/8) + anchors 02:13/04:13/06:13 confirmed on branch; **08:13 anchor + thread row 6718123417 UNVERIFIED-with-receipt**.
2. **CLAIM 2** — CLEAN (part). T-C/T-E/T-F confirmed as named nexts on branch spine; four acceptance-scripts confirmed absent from study-folder; **briefs-cache absence UNVERIFIED-with-receipt** (outside reach, by design).
3. **CLAIM 3** — UNVERIFIED-with-receipt. The run-id pair 42453572150/42453573843, GREEN @ 01:09-01:11 on main@670a261c75, row 6718515196, and the 403 landing-post seam are not on the branch bytes. The fabric's 30/30 GREEN band is referenced but its per-run-id verdicts are the X-3 divergence.
4. **CLAIM 4** — PARTIAL-CONFIRMED. 92%/5.6G-at-the-guard's-line confirmed on branch; **01:13 guard-tick drained 3.9→5.6G + guard-state 5,863,720 KB matching fresh df UNVERIFIED-with-receipt**.

**Receipt policy:** everything outside the study-folder (head's briefs-cache at 06:20 ET; the 06:2x handoff receipts; the run-id pair + 403-seam from the pre-digested ledger) is marked **UNVERIFIED-with-receipt** and carried, never fabricated. Nothing public without the operator's word.
