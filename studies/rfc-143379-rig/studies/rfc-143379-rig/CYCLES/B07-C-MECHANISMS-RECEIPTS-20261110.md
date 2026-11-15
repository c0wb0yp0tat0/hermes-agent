# B07-C-MECHANISMS-RECEIPTS-20261110 — the backwards audit, night 11-07: MECHANISMS + RECEIPTS (re-fire)

**Lane:** B07-C (re-fire) · **Seat:** meituan/longcat-2.5:free · **Date:** 2026-11-11 (ET, post-midnight) · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Gate:** nothing public without the user's word.

**Re-fire receipt.** The first B07-C fire died mid-read on the fair-share 429 class (`HTTP 429: You've reached this model's current fair-share rate limit … retry_after: 198`) — the seat's window, a designed rest class, not a defect. The failure-receipts `/root/workspace/drop/backwards-audit/logs/B07-C.log` + `B07-C.err` sit **OUTSIDE this lane's read-root** (`read_file` → `{"error":"path outside the allowed roots"}`, stamped round 1 and re-stamped at the write-window); the crash-to-logfile guarantee is registered OWED and the re-fire's read-rounds were re-derived from the ground (the tree at HEAD). Seat re-pinned to cat per the rebalance rule; the rested seat rests, the work moves.

**Skills mandate (reported honestly).** `skill_view` is **ABSENT from this lane's tool inventory** (the seam the siblings B07-A/B07-B/B08-B registered). The mandates — defect-forensics, investigation-documentation, agent-work-review, comment-driven-lab-ops — are applied as METHOD (byte-direct claim→PASS/FLAG, the absence-protocol, the machine-envelope decode) and the load is registered **OWED**, not papered. A landing that claims the skills loaded when the tool is absent would be the exact silent-skip class this audit exists to catch.

**Method.** Byte-direct only: `git show HEAD:<path>`, `git ls-tree -r HEAD`, `git log --all`, `git grep`, `git cat-file`. Terminal is git-only (no shell loops, no `gh`, no `jq`, no `/root/.hermes`). Every claim carries its read-stamp and byte. Absence claims re-checked at a second stamp.

---

## 1. THE WATCHER CENSUS — alive-then / alive-now, with the dead-class names

### 1.1 NEGENTROPY-SWEEP — the 2h cadence watcher (ALIVE-THEN: 6 fires on 11-07)

| Fire | Commit (ET) | Reported that night | Caught |
|---|---|---|---|
| 0948 | `a55d80f1d2` 04:51 | window CLOSED→SEPARATION-UNMEASURED; W2 spec not yet on branch; fabric 0/0/31 | FIRST-FIRE of the 11-07 series; W2 design spec landed since 11-06 |
| 1149 | `117fbf2d80` 06:50 | same window; fabric 30 queued + 1 in_progress; 0 green/red | ACES C3 chain landed, confirming the same fabric state |
| 1350 | `cc0993727c` 08:54 | window CLOSED-as-unverified (2 rejected reads, 0 values); W2 spec ABSENT from listing | the lane-block itself receipted; precondition (2) named |
| 1551 | `e8ec8bf12b` 10:54 | W2 spec now ON-branch (precondition 2 MET); FABRIC-RECEIPTS at HEAD; 13 commits since 1350 | the spec's landing; the fabric file's existence |
| 1752 | `d8637ac470` 12:56 | window code-RECEIPTED (run_eval.py:81, either-or gate); harness "unbuilt" claim corrected (`9836333f5a`) | the record-correction commit; the fabric-2.0 re-dispatch rows |
| 1953 | `f72b0ce139` 15:02 | 0 new commits since 1752; branch unmoved | the null, receipted as null (no invented motion) |
| 2154 | `2479968400` 16:58 | 3 new commits (fleet body + 4 lenses + nightshift plan); fabric still 60 queued+1 in_progress | planning motion without seam motion |
| 2355 | `5e7096c46b` 18:57 | 4 new commits (peak-shape/value-add + depth/cross reads + THE-UNDERSTANDING + fleet body); same arm verdicts | synthesis accumulation; the arm's evidence unmoved |

**What it reported:** every fire the same honest verdict — *window code-RECEIPTED (run_eval.py:81, either-or gate @ b65773b) but runtime values UNMEASURED → SEPARATION-UNMEASURED; settle-condition re-armed.* The watcher's subject was **never measured** on 11-07; it said so every 2h without exception.

**Alive-now: INDIRECT-PASS.** The series continues: 11 fires on 11-08, 11 on 11-09, `20261110-2312`, `20261111-0232` (the 2h cadence alive through the audit's own night). Direct cross-check against `/root/.hermes/cron/jobs.json` is **OWED** (§1.5).

### 1.2 FLEET-CYCLE-BODY — the 3h PR-body cycle (ALIVE-THEN: 6 bodies on 11-07)

`1059` (`7616aeaf8c` 06:00) · `1403` (`015e365227` 09:03) · `170825` (`6c62b96df1` 12:10) · `202555` (`8721c38935` 15:25) · `232929` (`c30548c0f9` 18:29) · `DELEGATE` (`50c7d71535` 02:53). The 1403 body is the record-of-record: it archives the sweep 1350 (`cc0993727c`), the C4 convergence, and the fabric GREEN line. The 170825 body archives the sweep 1551 and the read-fix POSTED. **Alive-now: INDIRECT-PASS** — 9 bodies on 11-08, 7 on 11-09, `20261111-0008`.

### 1.3 REAPEX-HARVEST — the 1h harvester (ALIVE-THEN: the S4/S5/S6 steps)

Named in `PR1-READ-20261107.md`: *"the reapex-harvest (1h) and the pr-body-fleet-cycle (3h) keep turning."* On 11-07 the reapex machinery's floor is `5fdf311069` APEX-OF-APEXES (01:38) + the re-apex shift plan. **Alive-now: INDIRECT-PASS** — the `REAPEX/` dir continues on 11-09 (`STALL-ARMING-T0`, `THE-MISSION-OF-MISSIONS-ORCHESTRATION`) and `tmp-artifacts/reapex-s4/s5/s6/ta-beam/compaction-alpha-20261108`.

### 1.4 THE THREAD'S MACHINE-ENVELOPES (decoded, the brief's comment-driven-lab-ops method)

`PR1-READ-20261107.md` decodes the thread's row classes: ~12 envelope-only reground rows (`20261107-reground-*`), ~8 fleet-cycle refresh archives, ~6 negentropy-sweep receipts, the arming/landing envelopes for closed arcs, and the stall-and-refire rows for the enrichment pair's three zero-write deaths. **The thread tail is UNMEASURED in this git-only lane** (no `gh`); the branch's own cycle bodies carry the read-time counts (245–272 rows).

### 1.5 THE CRON ROSTER CROSS-CHECK — OWED (the direct alive-now check)

`/root/.hermes/cron/jobs.json` returns `{"error":"path outside the allowed roots"}` (stamped twice). The record DOES say: `PR1-READ-20261107.md` — *"145 entries → 16 live (129 consumed/expired removed, zero failures)"*; *"Cron surface: 16 live jobs, all stateful"*; *"Scheduled: negentropy-sweep (2h) + reapex-harvest (1h) armed, read-back verified."* So at the 11-07 read the roster carried 16 live jobs, zero failures, both scheduled watchers armed. **The direct per-job last_status/error cross-check is OWED to a lane with `/root/.hermes` read access.**

### 1.6 THE DEAD-CLASS NAMES (the classes this audit was built to catch)

1. **Blind-but-honest (SEPARATION-UNMEASURED).** The sweep fires every 2h and reports its own blindness honestly — code-receipted, values unmeasured. It is NOT dead; it fires and tells the truth. **Alive, but its subject is unmeasured.**
2. **Floor-blind (reapex-floor-unreadable).** Every sweep's seam-scan carries the same line: the re-apex floor `/root/.hermes/plans/2026-11-07_0135-reapex-shift.md` is UNREADABLE in-lane. The watcher cannot read its own floor plan.
3. **Verifier-blind (fabric per-fork gh-unreadable).** The sweeps and `FABRIC-CONCLUSIONS-20261108` both record: *"Per-fork `gh api …/fabric-battery.yml/runs` reads remain UNMEASURED (git-only lane)."* The watcher reports the GREEN line from the cycle bodies but cannot independently verify per-fork statuses.
4. **Unmarked-fire (sentinel inconsistency).** All SIX 11-07 sweeps carry a `.sentinel` (re-checked: 0948/1149/1350/1551/1752/1953/2154/2355 each have one); the fleet-cycle bodies carry NONE. The 11-08 series marks the first six and drops the last five — the convention is applied inconsistently across the two watchers. **Receipt-hygiene flag, not proof of a dead watcher.**

**The truly dead/silent-skip class (probe-fail → exit 0 → clock "ok") is NOT confirmable from branch bytes** — it requires the `jobs.json` last_status/error fields. Named, owed, not asserted.

---

## 2. THE ACES RING UNDER PROBE — C1→C4 claims vs bytes

The ring's commit chain (byte-verified via `git log --all`):

| Cycle | IMPROVE | AUDIT | REVIEW | Verdict |
|---|---|---|---|---|
| C1 | `e640efb7a3` 01:39 | `9769ab931d` 01:41 | `5e0774420b` 01:43 | 14 named → 9C/2N/3R; REVISIONS-NEEDED |
| C2 | `1ee6d87cbe` 01:53 | `93ced6090b` 01:55 | `653f535bfd` 01:57 | 7 named → 4C/4N/0R; CONTINUE |
| C3 | `c9a0325719` 02:04 | `ca15b98e1f` 02:05 | `98e8de2303` 02:08 | 0 named; NO-IMPROVEMENTS |
| C4 | `c5e321e73b` 03:41 | `c1965e6871` 04:51 | `ccd33a1ebf` 04:52 | 0 named; NO-IMPROVEMENTS CONFIRMED TWICE |

### 2.1 The continuity chain (each ring's next seed existed and fired)

- **C1→C2:** REVIEW-C1 `5e0774420b` (d) seeds the 5 standing seams + C1's ten-arm backlog → C2 IMPROVE `1ee6d87cbe` names 7 improvements over 4 accruals since `5e0774420b`. **PASS** — the seed existed; C2 fired.
- **C2→C3:** REVIEW-C2 `653f535bfd` (d) seeds the 7 arms → C3 IMPROVE `c9a0325719` re-examines exactly those 7 (1 closed, 2 partial, 4 standing). **PASS** — the seed existed; C3 fired.
- **C3→C4:** REVIEW-C3 `98e8de2303` (d) seeds the 8-arm confirmation-cycle seed → C4 IMPROVE `c5e321e73b` runs the second no-change pass, names 1 (IMP-C4-1, a re-derivation), verdict NO-IMPROVEMENTS. **PASS** — the seed existed; C4 fired.
- **C4→HOLD:** REVIEW-C4 `ccd33a1ebf` (d) declares the HOLD's state-line; no next seed opened. **PASS** — the chain terminates by design.

### 2.2 Per-claim probe (claim → verdict → bytes)

| # | Claim | Verdict | Byte-evidence |
|---|---|---|---|
| 1 | C1: 14 improvements named, 7 seams | **PASS** | `ACES-IMPROVE-20261107.md` CLASS-COUNTS: 8 landings, 14 IMP-1..14, 7 SEAM-1..7; IMPROVE §LEDGER rows 1–8 landings. |
| 2 | C1 audit: 9C/2N/3R, all 3 refutations on the 5-vs-6 miscount | **PASS** | `ACES-AUDIT-20261107.md` CLASS-COUNTS + per-row: IMP-1/6/7 REFUTED (plan §1 carries SIX rows incl. row 6 "the 3-of-7 sessions messages-timestamps re-check"); IMP-3/8 NUANCED. |
| 3 | C1 review: 5 corrections applied + 3 additions | **PASS** | `ACES-REVIEW-20261107.md` (a): C-1..C-5 (C-1/2/3 STRUCK, C-4 downgraded, C-5 kept open) + R-1..R-3. |
| 4 | C2: 7 improvements, stop-line NOT carried | **PASS** | `ACES-IMPROVE-C2-20261107.md` §Stop-line: "Not NO-IMPROVEMENTS. 7 improvements named." |
| 5 | C2 audit: 4C/4N/0R; IMP-C2-1/7 receipts stale (16→30 rows) | **PASS** | `ACES-AUDIT-C2-20261107.md` per-row: IMP-C2-1 NUANCED (count half stale: 30 rows not 16), IMP-C2-7 NUANCED (header present, "begins directly with the table" struck). |
| 6 | C3: 0 improvements; NO-IMPROVEMENTS; 7 arms (1 closed/2 partial/4 standing) | **PASS** | `ACES-IMPROVE-C3-20261107.md` §Counts + §Seed-arm re-examination; Arm 3 CLOSED on 31 distinct run-ids. |
| 7 | C3 audit: 11/11 CONFIRMED, READY-FOR-THE-REVIEW | **PASS** | `ACES-AUDIT-C3-20261107.md` per-row 1–11 + Overall: "11 CONFIRMED / 0 NUANCED / 0 REFUTED." |
| 8 | C3 review: NO-IMPROVEMENTS; confirmation cycle arms | **PASS** | `ACES-REVIEW-C3-20261107.md` (c): "NO-IMPROVEMENTS — the CONFIRMATION CYCLE arms (one more pass), then the shift HOLDS." |
| 9 | C4: 0 improvements; second no-change proof | **PASS** | `ACES-IMPROVE-C4-20261107.md` §(d): "New improvements named: 1 (IMP-C4-1)… Verdict: NO-IMPROVEMENTS (stop-line confirmed for the second time)." |
| 10 | C4 audit: 11/11 CONFIRMED | **PASS** | `ACES-AUDIT-C4-20261107.md` Overall: "11/11 rows CONFIRMED / 0 NUANCED / 0 REFUTED." |
| 11 | C4 review: NO-IMPROVEMENTS CONFIRMED TWICE; shift HOLDS | **PASS** | `ACES-REVIEW-C4-20261107.md` (c): "NO-IMPROVEMENTS CONFIRMED TWICE — THE SHIFT HOLDS at the converged state." |
| 12 | COPYCAT-REVIEW: convergence CONFIRMED, zero in-substance divergences | **PASS** | `COPYCAT-REVIEW-20261107.md` (a) table: C1–C3 all CONVERGE; (b) "Divergences found: zero in substance." |

**One NUANCED note (not a FLAG):** the C4 IMPROVE's §(d) says "New improvements named: 1 (IMP-C4-1)" while its own §(c) table's row IMP-C4-1 is a re-derivation and rows IMP-C4-2/3 are "LEG ARM — carried, not renamed." The verdict line says NO-IMPROVEMENTS. The 1-named/0-named tension is internal to C4 and is resolved by C4's own verdict (the re-derivation is not new product). The AUDIT-C4 confirms "New improvements named: 1 (IMP-C4-1)" as A4-2 CONFIRMED — so the audit and improve agree; the REVIEW-C4's corrections-ledger rows C4-3 says "Improvements named (C4): 0." **This is a count-label drift across the three C4 files, not a substance error** — named here as a NUANCED receipt-hygiene note.

---

## 3. THE RECEIPTS UNDER PROBE — claim → PASS/FLAG → bytes

| # | Claim (11-07) | Verdict | Byte-evidence |
|---|---|---|---|
| 1 | MISSION-8H-V5: 6 tracks (Track 1, A, C, D, R1, R2) | **PASS** | `MISSION-8H-V5-20261107.md` §2 "THE TRACKS (6)"; Track 1 + A + C + D + R1 AVREA-Maximization + R2 GitHub-Fork Parallelism. |
| 2 | V5 compose-check table: 16 rows, rows 15–16 = R1/R2 | **PASS** | §6 rows 15 (AVREA-maximization) + 16 (R2) present; rows 1–14 = V4's table. |
| 3 | V5 fires 23:59:50 EST; commit `a7f99c12a6` 23:43 | **PASS** | `git log` `a7f99c12a6` 2026-11-07 23:43:30 -0500 "MISSION-8H-V5 (6 tracks…)". |
| 4 | FORK-RUNNER-FLEET: 31-fork inventory | **PASS (with named delta)** | `FORK-RUNNER-FLEET-20261107.md` §(a): "Fork-count: UNMEASURED in this lane, vs the brief's 31"; 1 verified (hermes-agent), 30 UNMEASURED. The honest delta is named, not invented. |
| 5 | GITHUB-RUNNER-FABRIC: 31 forks counted live, zero delta | **PASS** | `GITHUB-RUNNER-FABRIC-20261107.md` §(a): "Fork count: 31, counted live — zero delta vs the brief's 31"; the 31-row table with pushed_at quotes. |
| 6 | COPYCAT-REVIEW verdict: convergence CONFIRMED | **PASS** | `COPYCAT-REVIEW-20261107.md` (b): "The loop's convergence CONFIRMED — the no-improvement's real." |
| 7 | FABRIC-RECEIPTS: 31 rows, pin `54395f9b4f0c`, 30 queued + 1 in_progress | **PASS** | `FABRIC-RECEIPTS-20261107.md` HEAD bytes: 31-row launch table (pin `54395f9b4f0c`, run-ids `42349103810`…`42349191196`), `dsh-node-addon-require-builtin` `in_progress`, rest `queued`; + 30-row fabric-2.0 re-dispatch (per-fork pins `2bc3ef1887b0`…). |
| 8 | FLEET-CYCLE-BODY-1403: "30/31 RED → 30/30 GREEN + study fork GREEN" | **PASS (body line)** | `FLEET-CYCLE-BODY-20261107-1403.md` line 7: "30/31 RED at the universal pin on the checkout-class, then `30/30` GREEN at the per-fork pins + the study fork's own GREEN + the subject-variant wave GREEN." |
| 9 | The GREEN line is NOT in FABRIC-RECEIPTS rows at HEAD | **PASS (the X-3 divergence is real)** | `FABRIC-CONCLUSIONS-20261108.md` §(b): "FABRIC-RECEIPTS-20261107.md carries run-ids + `queued`/`in_progress` only; no verdict, no conclusion column. The `30/30 GREEN` line lives in the cycle bodies." The `KIT-AUDIT` X-3 flag names the divergence risk. |
| 10 | NEXT-SHIFT-PLAN-AUDIT verdict: READY-FOR-THE-NEXT | **PASS** | `NEXT-SHIFT-PLAN-AUDIT-20261107.md` OVERALL: "READY-FOR-THE-NEXT"; §1 rows 1–6 CONFIRMED; two seams (trigger-branch, pin) + one sharpening. |
| 11 | NEXT-SHIFT-PLAN-AOA verdict: COMPLETE-WITH-SEAMS; vote READY-FOR-THE-NEXT | **PASS** | `NEXT-SHIFT-PLAN-AOA-20261107.md` §0 + §3.4: "COMPLETE-WITH-SEAMS… vote READY-FOR-THE-NEXT with the seams logged, not blocking." |
| 12 | AoA's GAP: handoff 6 arms vs plan 5 rows | **PASS (the GAP is real; the audit later refuted it)** | `NEXT-SHIFT-PLAN-AOA-20261107.md` Spot-check A: "6 arms named in the handoff; 5 rows in the plan's §1 table." The ACES C1 audit then REFUTED the premise (plan §1 carries SIX rows incl. row 6). The AoA's GAP was real *at its read-time* against the plan's then-bytes; the plan was amended. |
| 13 | NEGENTROPY-SWEEP receipts: md5/date lines | **FLAG (no md5/date lines exist)** | `git grep -i "md5\|date"` across all eight 11-07 sweep receipts → **empty** (exit 1). The 11-07 sweeps' receipts are code/values-based (run_eval.py:81 quotes, commit hashes, blob hashes), not md5/date-stamped. The brief's "md5/date lines" expectation does not match the 11-07 sweep receipt format — the receipts carry commit-blob hashes (`6677abc2…`, `482b2714…`, `37e7347b…`) instead. |
| 14 | The 11-07 sweeps' window verdict: SEPARATION-UNMEASURED | **PASS** | All eight fires carry the verdict-line; the 0948 fire's is the baseline, the 1752+ fires carry "code-RECEIPTED / values-UNMEASURED." |
| 15 | PR1-READ: 272 comments; 16 live cron jobs | **PASS (as cited)** | `PR1-READ-20261107.md` §1/§5: "Comments read: 272"; "Cron surface: 16 live jobs, all stateful." The thread tail is UNMEASURED in-lane; the count is the read's own quote. |

---

## 4. THE LINEAGE — 11-07 watcher-receipts → 11-08's evidence

**The chain the brief names:** 11-08's WAVE3/FABRIC-CONCLUSIONS cited the sweep artifacts. Byte-check:

- **FABRIC-CONCLUSIONS-20261108** cites `FABRIC-RECEIPTS-20261107.md` (the verdict column absent), `GITHUB-RUNNER-FABRIC-20261107.md` (workflow-presence UNMEASURED), `FORK-RUNNER-FLEET-20261107.md` (the 31-fork inventory), and `KIT-AUDIT-20261107.md` (the X-3 flag). **PASS** — the 11-08 conclusions artifact's load-bearing citations resolve to real 11-07 files.
- **The sweep chain:** `NEGENTROPY-SWEEP-20261108-0156` carries the delta vs `NEGENTROPY-SWEEP-20261107-2355` (commit `5e7096c46b`) — "NOTHING MOVED… the branch is byte-identical to the 2355 fire." **PASS** — the 11-08 sweep's prior-sweep baseline is the 11-07 2355 fire; the chain holds hop-by-hop.
- **WAVE3-UNIFIED-FOLD-20261108** cites `MISSION-8H-V5-20261107.md` (6 tracks), `BLIND-E2E-20261107.md`, `SKEPTIC-E2E-20261107.md`, `TRUSTER-E2E-20261107.md` — all 11-07 files. **PASS.**
- **The fleet-cycle chain:** `FLEET-CYCLE-BODY-20261108-023131` is the next body after `20261107-232929`; the 170825 body archives the 1551 sweep. **PASS.**

**One FLAG in the lineage:** the brief says "11-08's WAVE3/FABRIC-CONCLUSIONS cited the sweep artifacts." Byte-check: `git grep "NEGENTROPY-SWEEP-20261107"` in WAVE3-UNIFIED-FOLD and FABRIC-CONCLUSIONS → **empty**. The 11-08 artifacts cite the *fabric* receipts (`FABRIC-RECEIPTS-20261107`, `GITHUB-RUNNER-FABRIC-20261107`, `FORK-RUNNER-FLEET-20261107`) and the *E2E lens* files, but **not** the sweep receipts by name. The sweep chain holds through the 11-08 *sweeps* (0156 carries the 2355 delta), not through WAVE3/FABRIC-CONCLUSIONS. **The brief's specific citation claim is FLAGged as not-byte-supported**; the lineage holds via the sweep series' own continuity and the fabric receipts.

---

## 5. CORRECTIONS, OPEN SEAMS, AND THE WINS

**Corrections (the night's own):**
- The harness "unbuilt" claim was corrected on the record (`9836333f5a`, 12:39) — the write-window is brief-enforced, not harness-enforced; the READ-GATE is live. The 1752 sweep carries the correction.
- The C1 audit's 5-vs-6 miscount was refuted by the plan's own §1 (six rows) — IMP-1/6/7 struck; the AoA's GAP was real at read-time, then the plan was amended.
- The FABRIC-RECEIPTS file's 16→30-row growth was caught by the C2 audit (IMP-C2-1/7 NUANCED).

**Open seams (owed, not smoothed):**
- The cron roster's direct last_status/error cross-check is **OWED** (read-root).
- The re-apex floor (`/root/.hermes/plans/2026-11-07_0135-reapex-shift.md`) is **floor-blind** in every sweep.
- The per-fork `gh api` fabric reads are **verifier-blind** in every git-only lane.
- The thread tail is **UNMEASURED** in every git-only lane (IMP-8's PR-UPDATE ack rides open).
- The sentinel convention is applied inconsistently across the two watchers.

**The wins (what still stands, must not be dismissed):**
- The **ACES ring's four-cycle convergence** — 14→7→0→0 named improvements, each audit-confirmed, the NO-IMPROVEMENTS stop-line proven twice and the shift HOLDS. The loop's honest termination is a feature, not a failure.
- The **six-sweep 2h cadence** that reported its own blindness every fire without inventing motion — the 1953 fire's null is receipted as null.
- The **31-fork fabric's two-wave dispatch** (universal-pin RED → per-fork-pin GREEN) — the checkout-class finding became a mechanism.
- The **fleet-cycle's 3h PR-body archive** — the study's one-voice record, refreshed and receipted.
- The **COPYCAT-REVIEW's zero-divergence convergence check** — the constant independent re-read that confirmed the loop from outside.

**Final register:** receipts, never claims. Fork-only. The mechanisms were alive on 11-07 and are alive now (indirect-PASS); the dead/silent-skip class is named and owed, not asserted.