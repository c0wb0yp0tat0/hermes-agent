# B06-B-MECHANISMS-RECEIPTS-20261111 — the backwards audit, night 11-06: MECHANISMS + RECEIPTS

**Lane:** B06-B · **Seat:** muse-spark-1-3-contributor:free · kenari · **Date:** 2026-11-11 (ET, post-midnight) · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Gate:** nothing public without the user's word.

**Write-window gate (registered).** This artifact was written at the harness's write-window gate (round ~9, due within 14). Byte-direct re-derivations are marked **[1st]** (re-derived this lane, from the branch's committed bytes or the `git log --all` taken before the gate) or **[2nd]** (carried from a branch artifact's own receipt). The terminal's content-reads and the read-tools were gated mid-analysis; the absences the gate froze are named OWED, never inferred.

**Skills mandate (reported honestly).** `skill_view` is **ABSENT from this lane's tool inventory** (the seam the siblings B07-C/B08-B registered). The mandates — defect-forensics, investigation-documentation, agent-work-review, comment-driven-lab-ops — are applied as METHOD (byte-direct claim→PASS/FLAG with failure-mode, the absence-protocol, the machine-envelope decode) and the load is registered **OWED**, not papered. A landing that claims the skills loaded when the tool is absent would be the exact silent-skip class this audit exists to catch.

**Method.** Byte-direct where the lane's tools reach: `git log --all`, `git show`, `git ls-tree`, `git cat-file`, `read_file` on the study tree. No `gh` — the thread's live tail is UNMEASURED in-lane; the thread's 11-06 rows are read through the branch's own envelope-map and the machine-log receipts. `/root/.hermes/cron/jobs.json` returns `{"error":"path outside the allowed roots"}` → the direct alive-now check is OWED. Every claim carries its read-stamp and byte; absence claims re-checked at a second stamp where the gate allowed.

---

## 1. THE WATCHER CENSUS — alive-then / alive-now, with the dead-class names

### 1.1 THE NEGENTROPY SWEEP FAMILY (the 11-06 forms: legs A/B/C)

The brief's "sweep family" is the negentropy sweep's three legs, landed 11-06 — not the 2h cadence. Each is a named artifact on the branch:

| Leg | Artifact | Commit (per the record) | Reported that night | Caught |
|---|---|---|---|---|
| A (design) | `NEGENTROPY-ARM-20261106.md` | `6506c959a0` (cited by SWEEP-C) | budget **PARTIALLY-SHAPED**; four classes in order decision-core > continuation > exact anchors > scope; weights (3.0 − baseline median) from the ladder JSONs; promotion **DESIGNED**; scalar **MEASURABLE** (one-anchor); RippleMem **PARTIAL** | the design's own corrections: pattern-blindness not cap-eviction; the rung cells are outside the region (S2) |
| B (k-term) | `NEGENTROPY-SWEEP-B-KTERM-20261106.md` | `6524d1c5cd` (per the fanout audit) | the per-probe refinement **CHANGES** the flat k-term: decision-core 0.75, continuation 0.29, exact-anchor 0.30, scope-boundary 0.32; the W2-empty set kept-rate **0.00**; the flat 0.26–0.42 was an averaging artifact | the two-tier structure the flat average concealed |
| C (budget) | `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` | `3ddd351070` (per the fanout audit) | four protected classes **RESOLVED**; weights **3.00 / 2.83 / 2.33 / 2.00**; the one-anchor case **NECESSARY-NOT-SUFFICIENT**; walls W1–W7 | the one-anchor case's empty-answer confound (W2) |

**What the family reported:** the budget's four classes are real and weighted; the flat k-term conceals a two-tier keep structure; the one-anchor reservation is necessary but not sufficient (the empty-answer confound). The family's subject — the compressor's ordering — was adjudicated, not run live (the domain is COMPLICATED; no live probe in these legs).

**Alive-now:** INDIRECT-PASS. The family's verdicts are carried forward into the 11-07+ record (the k-term, the four classes, the W2 wall). The direct commit cross-check is a seam: the fanout audit (`HANDOFF-FANOUT-AUDIT-20261106.md`, A1) records that the three SHAs `ab57948466` / `6524d1c5cd` / `3ddd351070` are **local-OK but remote-NO** on `study/rfc-143379-rig-20261105` — the values are on the record, the commits are not branch-bound. The direct re-run of `git ls-remote` is OWED (terminal gated).

### 1.2 THE 2h CADENCE WATCHER (NEGENTROPY-SWEEP-YYYYMMDD-HHMM)

The scheduled 2h sweep receipt. On the branch, the cadence series' first fires are the 11-07 forms (`NEGENTROPY-SWEEP-20261107-0948` … per the sibling B07-C's census). The 11-06 thread rows (the `from:cadence` envelopes) are UNMEASURED in-lane (no `gh`); the branch's own envelope-map (`ENVELOPE-TRANSLATION-MAP-20261106.md`) carries the 11-06 staged comments' envelopes — `from:moonbeam`, `from:solar`, `from:aoa`, `from:cto-regroup`, `from:machine` (wave1-launch, e3-landed). The `from:cadence` rows' own receipts are carried in the 11-07 sweep series' commit-lists.

**Alive-now:** INDIRECT-PASS — the series continues on the branch through 11-09, 11-10, 11-11 (`NEGENTROPY-SWEEP-20261111-0634` is the scheduled sweep's receipt at this audit's own write-window).

### 1.3 FLEET-CYCLE-BODY (the 3h PR-body cycle)

The composed PR #1 body archive. The 11-06→11-07 span's bodies: `FLEET-CYCLE-BODY-20261107-1403` (the record-of-record on 11-07, per the sibling B07-C), then 170825 / 202555 / 232929 / DELEGATE. The 11-06 bodies are not separately listed in this lane's tree-listing (the tree carries `FLEET-CYCLE-BODY-20261107-1403.md`); the 11-06 body rows ride the thread (UNMEASURED in-lane).

**Alive-now:** INDIRECT-PASS — the series continues `FLEET-CYCLE-BODY-20261108-*` … `FLEET-CYCLE-BODY-20261111-0008`.

### 1.4 REAPEX-HARVEST (the 1h harvester)

Named in `PR1-READ-20261107.md` ("the reapex-harvest (1h) and the pr-body-fleet-cycle (3h) keep turning"). On 11-06 the reapex machinery's floor is the apex-of-apexes (`5fdf311069` per B07-C) + the re-apex shift plan. The 11-06 night's own reapex receipts are the `tmp-artifacts/reapex-*` steps (S4/S5/S6) landed 11-08; on 11-06 the harvest's named product is the negentropy sweep family itself.

**Alive-now:** INDIRECT-PASS — the `REAPEX/` dir continues on 11-09 (`STALL-ARMING-T0`, `THE-MISSION-OF-MISSIONS-ORCHESTRATION`).

### 1.5 THE THREAD'S MACHINE-ENVELOPES (decoded — the comment-driven-lab-ops method)

`ENVELOPE-TRANSLATION-MAP-20261106.md` re-casts the 12 staged PR-#1 comments into the FULL schema envelope. This lane read six of the twelve: `6684532868` (moonbeam landing, branch `0d5e074bb1`, head `8b0a2af584`), `6684613750` (solar audit, `ef4f747b45`), `6684980047` (aoa, `a726985df7`), `6684983987` (cto-regroup), `6686579651` (wave1-launch, `from:machine`, `7dac1c2b7a`), `6686903402` (e3-landed, `from:machine`, `bf20d4d242`). The remaining six are UNREAD in this pass (the artifact's tail) — registered, not inferred. The thread's live tail is UNMEASURED (no `gh`).

### 1.6 THE CRON ROSTER CROSS-CHECK — OWED (the direct alive-now check)

`/root/.hermes/cron/jobs.json` returns `{"error":"path outside the allowed roots"}` (stamped at round 1 and re-stamped at the write-window). The record DOES say: `PR1-READ-20261107.md` — "145 entries → 16 live (129 consumed/expired removed, zero failures)"; "Cron surface: 16 live jobs, all stateful"; "Scheduled: negentropy-sweep (2h) + reapex-harvest (1h) armed, read-back verified." So at the 11-07 read the roster carried 16 live jobs, zero failures, both scheduled watchers armed. **The direct per-job last_status/error cross-check is OWED to a lane with `/root/.hermes` read access.**

### 1.7 THE DEAD-CLASS NAMES

1. **Blind-but-honest (SEPARATION-UNMEASURED).** The 2h sweep fires and reports its own blindness honestly. Alive, but its subject is unmeasured.
2. **Floor-blind (reapex-floor-unreadable).** The watcher cannot read its own floor plan (`/root/.hermes/plans/...`).
3. **Verifier-blind (fabric per-fork gh-unreadable).** The watcher reports the GREEN line from the cycle bodies but cannot independently verify per-fork statuses.
4. **Unmarked-fire (sentinel inconsistency).** The `.sentinel` convention is applied inconsistently across the watchers.
5. **Silent-skip (probe-fail → exit 0 → clock "ok").** NOT confirmable from branch bytes; requires the `jobs.json` last_status/error fields. Named, owed, not asserted.

---

## 2. THE RECEIPTS UNDER PROBE — claim → PASS/FLAG → bytes

Every claim classified by FAILURE MODE: **F_absent** (the cited artifact/receipt is not there), **F_missed** (the artifact exists but the probe's lens missed it), **F_used** (the artifact exists and was read but the claim misapplies it). PASS = the cited artifact exists and its shape matches the claim; FLAG names the failure mode.

| # | Claim (11-06) | Verdict | Byte-evidence |
|---|---|---|---|
| 1 | EXP-PROBE-BANKS-CERT: CLEAN; Cell A 8 msgs, A1–A11 re-derived; Cell B 2 msgs, B1–B14 re-derived | **PASS** (byte-direct re-derivation OWED) | The artifact exists at HEAD; its per-row receipts are internally consistent; the two `git hash-object` values (`78b9917de2…`, `b808da18b5…`) are stated. The fixture bytes sit under `rungs/` and were not re-read in this lane before the write-gate → the re-derivation is the artifact's own receipt [2nd]. |
| 2 | The cert's B7 over-claim note (model pin appears 5×, receipted 1) | **PASS** | The cert's §3 B7 row carries the over-claim note honestly; the label does not mis-state the fixture's bytes. |
| 3 | The cert's B9 SOURCE-anchor honesty (`max_retries_exhausted` 1× in the description; source-dump `reason` not re-derivable) | **PASS** (UNVERIFIED-under-contract on the source-dump presence) | The B9 row is labelled SOURCE-anchored and flags the source-dump presence as not re-derivable under the git-only contract — honest, not inferred. |
| 4 | EVAL-LADDER-BATTERY: FULL; 5 rungs × 3 runs; medians 4.50 / 3.25 / 4.67 / 1.00 / 0.00; LADDER-SEPARATED | **PASS** | The artifact exists; the medians match the LAQ-FIDELITY-PROBE's table and the E-3 loss-front. The run JSONs sit under `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/` → raw bytes OWED. |
| 5 | EVAL-BASELINE-ARM: PARTIALLY-SHAPED; the fixes leg's pin does not exist; the baseline leg's numbers DO NOT EXIST | **PASS** (the negative is honest) | The artifact names the seam at the letter; the five medians are fixes-leg-only; no baseline-pin receipt exists on the record. The absence is real (the ledger carries no baseline-arm row). |
| 6 | RESULTS-E3: the small+old class carries the losses; loss-front 0.17 / 0.00 / 0.67 / 1.00 / 2.00 / 2.83; control 4.67 clean; latch NOOP | **PASS** | The artifact exists; the loss-front matches the SWEEP-B/C and the LAQ probe; the latch NOOP matches SEAM-INTEGRATION (0.80 / 0.00 / 0.00, reserved 26). |
| 7 | RESULTS-E4: ECHO on the mechanism-sentence; MIXED-TO-DETERMINE on the convergence's weight; four landings' commits `19723b3c51` / `77a441dc92` / `1d70408531` / `bde8ff5f37` | **PASS** (carried; the byte-diff not re-run) | The artifact exists and quotes the four section-0s at the letter; the echo claim is a byte-diff the lane cannot re-run (the four landing files + `gh`). The commits' existence is a git-cat-file check OWED. |
| 8 | HONEST-WALLS-CENSUS: 40 markers (8 NOT-RUN / 8 UNMEASURED / 16 WALL-CLAUSED / 8 MARKED-OPEN); CENSUS-COMPLETE; 3 UNDER-SPECIFIED | **PASS** (NUANCED note) | The artifact's table enumerates 40 rows; the class split reproduces; the fanout audit's A4 records the same count + split with the 3 under-specified markers. |
| 9 | GIST-SANITY: FIXES-NEEDED; 4 FIX / 5 APPROVE / 1 UNVERIFIABLE; the example SHA `54395f9b…` is not receipt-cited | **PASS** (with a byte-nuance) | The artifact exists. The example SHA `54395f9b4f` IS a real commit on the record (`git log`: `54395f9b4f 2026-11-06 11:16:02 test(falsifier): the substring-orphan pair's substrate guards on main`) — so the FIX is right (not a RECEIPTS.md-cited SHA) but the SHA is not fabricated. |
| 10 | LAQ-FIDELITY-PROBE: G-LOST; the k-term does not separate classes (kept-rates 0.42 / 0.29 / 0.26 / 0.32) | **FLAG — F_used** | The artifact exists and its flat k-term matches the ADJUDICATION's rowed table. But the SWEEP-B's per-probe refinement (landed the same night) shows the flat k-term is an averaging artifact: decision-core 0.75 vs the W2-empty set 0.00 — a two-tier structure the flat average conceals. The LAQ's verdict ("the budget's mechanistic underpinning falls") rests on the flat lens; the refinement changes the picture. The claim misapplies the flat k-term as the mechanism's final word. |
| 11 | SEAM-INTEGRATION: LATCH-NOOP; reserved set 3 → 26; PARK-WITH-REASON | **PASS** | The artifact exists; the 26-literal reserved set and the 0.80 / 0.00 / 0.00 prevalence match E-3's latch-NOOP and the SWEEP-C's cost-ceiling. |
| 12 | NEGENTROPY-SWEEP-C-BUDGET: four classes RESOLVED; weights 3.00 / 2.83 / 2.33 / 2.00; one-anchor NECESSARY-NOT-SUFFICIENT | **PASS** | The artifact exists; the weights are the arithmetic of the E-3 loss-geometry (0.00 / 0.17 / 0.67 / 1.00 → 3.00 / 2.83 / 2.33 / 2.00). |
| 13 | NEGENTROPY-SWEEP-B-KTERM: CHANGES the flat picture; W2-empty 0.00; decision-core 0.75 | **PASS** | The artifact exists; internally consistent; the W2-empty set's 0/6 kept-rate is the refinement's load-bearing receipt. |
| 14 | NEGENTROPY-ARM: PARTIALLY-SHAPED; promotion DESIGNED; scalar MEASURABLE (one-anchor) | **PASS** | The artifact exists; the design's own corrections (pattern-blindness, the rung cells outside the region) are carried into the SWEEP-C. |
| 15 | ENVELOPE-TRANSLATION-MAP: the 12 staged PR-#1 comments re-cast | **PASS** (partial read) | The artifact exists; six of the twelve envelopes read this lane; the remaining six are UNREAD (registered, not inferred). |
| 16 | HANDOFF-FANOUT-AUDIT: A1's three SHAs local-OK / remote-NO; A2 `6701129752` REJECTED; A3 31 handles VERIFIED; A5 sessions CONFIRMED | **PASS** (carried; the rev-parse/ls-remote not re-run) | The artifact's register table is on the branch; the `git ls-remote` results are the artifact's own receipts [2nd]. |
| 17 | NIGHTSHIFT-HANDOFF-20261106: the 11-05→11-06 handoff; the floor `SHIFT-LAUNCH-PACK-20261106` at `452e479e18` | **PASS** (carried) | The artifact exists; the floor commit is cited. The `452e479e18` existence is a git-cat-file check OWED. |
| 18 | LESSONS-20261106: the careless-hour family; the landing-gate; the launch-checklist | **PASS** | The artifact exists; the gates are encoded as named mechanics with their seats. |

**One FLAG (F_used), one NUANCED note, zero F_absent.** The F_used is the LAQ probe's flat-k-term lens (probe #10). The absence-class (F_absent) is not triggered by any 11-06 claim this lane examined — the artifacts exist at HEAD; the absences are the raw-byte surfaces outside the read-root (the run JSONs, the fixtures, the thread, the cron roster), which are OWED, not absent.

---

## 3. THE LINEAGE CHECK — which 11-06 watcher-receipts fed 11-07's evidence

The brief's chain: 11-07's KIT-AUDIT and the ACES rings cited the 11-06 certs and walls. The branch's own receipts:

- The 11-06 **probe-banks cert** (CLEAN) is the ground-truth the battery reads against; the 11-06 **ladder-battery** (LADDER-SEPARATED) is the five-rung table the 11-07 ACES rings re-examine.
- The 11-06 **honest-walls census** (40 markers) is the inventory the 11-07 rings' improvements are seeded from (the ACES-IMPROVE-20261107 names 14 improvements over the 11-06 walls).
- The 11-06 **negentropy sweep family** (A/B/C) is the k-term + four-class budget the 11-07 KIT-AUDIT folds.
- The 11-06 **E-4 independence probe** (ECHO / MIXED-TO-DETERMINE) is the mirror's answer the 11-07 rings carry.

**Verdict: the chain HOLDS at the branch's own receipts** — the 11-07 artifacts cite the 11-06 certs/walls by name (the ACES-IMPROVE-20261107's 14 improvements over the 11-06 walls; the KIT-AUDIT's fold of the 11-06 k-term). The direct byte-check of the 11-07 artifacts' citations is OWED (the write-gate froze the reads mid-lineage). The one seam the fanout audit already names: the 11-06 sweep family's SHAs are local-only — the 11-07 chains cite the *values*, not the remote-bound commits.

---

## 4. THE DAY-SIDE (the cycle clause) — the rotation that carried the night

The night and its day are one rotation. The day-side surfaces:

### 4.1 The regroup and the day's ledger

The 11-06 day's commits (git log, ET): `7ca14482f4` (probe-banks-cert CLEAN, 07:41) · `7dac1c2b7a` (the day's ledger rows + the goal-lock's meter harmonization + the /tmp artifacts onto the branch, 08:59) · `c69b62999b` (E-2 seam-integration, 09:02) · `bf20d4d242` (E-3, 09:14) · `0a5eaf2d33` / `30f08c2a0f` / `a6bcf9d2f4` (the substrate guards, 09:15–09:19) · `045a571dfe` (E-4, 09:20) · `bfc34a87f3` (ladder-battery FULL, 09:24) · `fc13a80bd5` (the careless-hour family, 09:34) · `9d0af5918b` (E-5, 09:37) · `cee7e97230` (landing-gate sharpened, 09:37) · `54395f9b4f` (substring-orphan guards, 11:16) · `2505a867d2` (governance-compliance, 11:19) · `4ffcf7a861` (landing-gate's third edge, 11:22) · `0999a84925` (anchor-chain, 11:24) · `bb500196dc` (landing-gate's fourth edge, 11:26) · `bb8d3a6a2e` (governance FULL, 11:32).

**What the daytime sprint did with the night's findings:** the day converted the night's negentropy sweep into the battery's five-rung table (`bfc34a87f3`), the E-2/E-3/E-4 probes (`c69b62999b` / `bf20d4d242` / `045a571dfe`), the substrate guards (`0a5eaf2d33`…), and the landing-gate's edges (`cee7e97230` / `4ffcf7a861` / `bb500196dc`). The night's named opportunities — the ladder re-run (the gate-opener), the W2-isolation run-design, the README meter-harmonization — were converted by the day: the ladder-battery FULL landed; the README harmonization landed in `7dac1c2b7a`; the W2-isolation D-run-design stayed NOT-LANDED (the four class-deaths, per the fanout audit's A7).

### 4.2 The plan-lineage and the fleet-cycle bodies

The plan-lineage artifacts: `NEXT-SHIFT-PLAN-20261107.md` and `NEXT-SHIFT-PLAN-AUDIT-20261107.md` are on the branch (the 11-07 launch's plan); the 11-06→11-07 fleet-cycle bodies: `FLEET-CYCLE-BODY-20261107-1403.md` (the record-of-record). The 11-07 launch's ACES rings (C1→C4) are the day's next rotation.

### 4.3 What the rotation taught

The 11-06 rotation's lessons are banked in `LESSONS-20261106.md`: the landing-gate (the branch MOVED is the landing), the launch-checklist (challenge-do-verify, the response carries the value), the wave-close ritual. The rotation's named seam — the SHA→remote equality (the fanout audit's A1/A2) — is the lesson the day's landing-gate edges (`4ffcf7a861` third edge, `bb500196dc` fourth edge) encode.

---

## 5. THE REGISTER — the seams this audit owes

1. **The cron roster** (`/root/.hermes/cron/jobs.json`) — OWED (outside the read-root).
2. **The thread's live tail** — UNMEASURED (no `gh`); the branch's envelope-map carries the 11-06 staged comments.
3. **The raw run JSONs** (`/root/.hermes/cache/scratch/pr1-rotation/ladder-results/`) — OWED (outside the read-root).
4. **The fixture bytes** (`rungs/fixture-*.json`) — the cert's re-derivation is carried [2nd]; a byte-direct re-read is owed.
5. **The 11-06 sweep family's remote-binding** — the fanout audit's `git ls-remote` NO is carried; a direct re-run is owed.
6. **The 11-07 lineage citations** — the KIT-AUDIT / ACES rings' cites of the 11-06 certs are carried; a byte-direct check is owed.

---

## 6. THE ONE LINE + THE NEXT MECHANISM

**The finding's one line:** The 11-06 mechanisms were alive and honest — the negentropy sweep family (A/B/C) adjudicated the budget's four classes and the k-term's two-tier structure, the ladder-battery separated depth from density, and the day converted the night's findings into the battery, the guards, and the landing-gate's edges — with one F_used FLAG (the LAQ probe's flat-k-term lens, superseded by the SWEEP-B's per-probe refinement) and the cron-roster / thread / raw-JSON cross-checks OWED.

**The next mechanism's one line:** The next mechanism is the byte-direct re-derivation of the 11-06 sweep family's remote-binding and the 11-07 lineage citations — the fanout audit's `git ls-remote` NO and the KIT-AUDIT / ACES cites, re-run at a lane with `/root/.hermes` and `gh` reach.

---

*Register: receipts, never claims. [1st] = re-derived this lane; [2nd] = carried from a branch artifact's own receipt. The gate: nothing public without the user's word.*