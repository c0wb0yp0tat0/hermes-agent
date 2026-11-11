# B08-B-MECHANISMS-RECEIPTS-20261110 — the backwards audit, night 11-08: MANY-WATCHERS + RECEIPTS

**Lane:** B08-B (re-fire) · **Seat:** meituan/longcat-2.5:free · **Date:** 2026-11-10 (ET) · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Gate:** the gate: nothing public without the user's word.

**Re-fire receipt.** The first B08-B fire died SILENTLY at round 4 (2026-11-10 ~18:44 ET) — reads only, no write, no artifact, no traceback. The failure-receipt logs (`/root/workspace/drop/backwards-audit/logs/B08-B.log`, `B08-B.err`) sit OUTSIDE this lane's read-root and could not be read byte-direct; the prior run's 4 read-rounds were therefore re-derived from the ground (the tree at HEAD), not assumed. This artifact is the re-fire's own receipt.

**Method.** Byte-direct only: `git show HEAD:<path>`, `git ls-tree -r HEAD`, `git cat-file -t`, `git log`, `git grep`. No shell, no `gh`, no `/root/.hermes/cron/jobs.json` (all outside the read-root — see the OPEN SEAM in §1.4). Every claim below is stamped with the read-time and the byte it rests on. Absence claims are re-checked at a second stamp (the `git ls-tree` listings at HEAD, taken twice across the session).

**Skills mandate (reported honestly).** The brief orders `skill_view` loads of defect-forensics, investigation-documentation, agent-work-review, comment-driven-lab-ops. **`skill_view` is ABSENT from this lane's tool inventory** (the same absence the sibling B08-A lane registered). The method is applied in its place — byte-direct claim→PASS/FLAG, the absence-protocol, the machine-envelope decode — and the load is registered as an OPEN SEAM, not papered. A landing that claims the skills were loaded when the tool is absent would be the exact silent-skip class this audit exists to catch.

---

## 1. THE WATCHER CENSUS — alive-then / alive-now, with the dead-class names

The night of 11-08 had FOUR automatic mechanisms alive, plus the machine-side certifying machinery. Each is named with what it reported that night, what it caught, and its alive-now status.

### 1.1 NEGENTROPY-SWEEP — the 2h cadence watcher (ALIVE-THEN: 11 fires)

**What it is:** the scheduled 2-hour sweep receipt, the study's heartbeat. On 11-08 it fired ELEVEN times, each landing a `NEGENTROPY-SWEEP-20261108-HHMM.md`:

| Fire | Commit | Read-time stamp (ET) |
|---|---|---|
| 0156 | `093e4b38c0` | 2026-11-08 00:58 |
| 0357 | `72afac9d98` | 2026-11-07 23:01 (landed 11-08 00:59) |
| 0558 | `c544d3ad55` | 2026-11-08 00:59 |
| 0759 | `916ff594d0` | 2026-11-08 03:01 |
| 1000 | `4c0ecf171a` | 2026-11-08 05:02 |
| 1201 | `5ff6ea0d96` | 2026-11-08 07:03 |
| 1402 | `0be8032e36` | 2026-11-08 09:03 |
| 1603 | `39ac6c07ae` | 2026-11-08 11:04 |
| 1804 | `10f0555846` | 2026-11-08 13:12 |
| 2005 | `7f389c4a1f` | 2026-11-08 15:06 |
| 2206 | `9fedbf1642` | 2026-11-08 17:07 |

**What it reported that night (the receipt's own words, quoted):** every fire's finding-line reads the same honest verdict — *"window code-RECEIPTED (run_eval.py:81, either-or gate @ b65773b) but runtime values UNMEASURED → SEPARATION-UNMEASURED … settle-condition re-armed."* The watcher's subject (the LLM window's separation) was **never measured** on 11-08; the watcher said so every two hours, without exception.

**What it caught:** the branch's motion, honestly. The 1603 fire caught **14 commits** since 1603's prior (the RE-APEX S4/S5/S6 steps, the K-recency certifying re-sweep + S11/1b sweeps + the instrument fix `609dcdfc3a`, the compaction-alpha draft, two fleet bodies). The 2005 fire caught **6 commits** (the C4/C5/C6 audit-review wave + the refinement-ring close `c8cda99c6f`). The 2206 fire caught **2 commits** (the C7 terminal-ring NO-CHANGE confirmation `f62772cc92` + the 202228 cycle body). The quiet fires (0156, 1000) caught **0 commits** and said "the branch is byte-identical … the cadence this fire produced a receipt, not even paper." The watcher distinguished *motion* from *stillness* every fire — it did not manufacture findings.

**Alive-now:** INDIRECT-PASS. The sweep series continues past 11-08 on the branch: `NEGENTROPY-SWEEP-20261109-0007` through `-2017` (11 fires on 11-09) and `NEGENTROPY-SWEEP-20261110-2312` (11-10). The 2h cadence is alive on 11-09 and 11-10. The DIRECT cross-check against `/root/.hermes/cron/jobs.json` (last_status/error) is **OWED** — see §1.4.

### 1.2 FLEET-CYCLE-BODY — the 3h PR-body cycle (ALIVE-THEN: 9 bodies)

**What it is:** the composed PR #1 body archive, refreshed every ~3h. On 11-08 it landed NINE bodies: `023131`, `053342`, `083639`, `113827`, `144227`, `174831`, `175259`, `202228`, `232825`.

**What it reported that night:** the study's one-voice state, refreshed. The 053342 body (quoted in `LENS-OUTCOME-20261108.md`) records "the thread at 282 rows," "the runner idle," "disk 90% under the 92-guard," "the branch head matches the PR head." The 232825 body records "the loop stands terminal: improve, audit, review, refine, confirm, hold — and the confirmation named no improvements, so the shift HOLDS at the converged state." The 202228 body records the same terminal hold. The bodies are the mechanism's *readable* receipt — the row is the receipt, the body is the artifact.

**Alive-now:** INDIRECT-PASS. The series continues: `FLEET-CYCLE-BODY-20261109-023224` through `-2053` (7 bodies on 11-09) and `FLEET-CYCLE-BODY-20261111-0008` (11-11). The 3h cadence is alive.

### 1.3 REAPEX-HARVEST — the 1h harvester (ALIVE-THEN: the S4/S5/S6 steps)

**What it is:** the reapex machinery's 1h harvest cadence (named in `PR1-READ-20261107.md`: "the reapex-harvest (1h) and the pr-body-fleet-cycle (3h) keep turning"). On 11-08 it landed the RE-APEX S4 (write-window chunk-size knob, `7dab7ff5d0`), S5 (scratch-prune audit, `80e7b67821`), S6 (naming-convention, `a913302533`), the reapex compaction-alpha (`3124867565`), and the reapex-ta-beam step — all archived under `tmp-artifacts/reapex-*`.

**What it reported:** the harvest's own steps, receipted in the 1603 sweep's commit-list ("RE-APEX S4 … S5 … S6 … reapex compaction alpha"). The harvest is the mechanism that fed the sprint's seeds.

**Alive-now:** INDIRECT-PASS. The `REAPEX/` directory continues on 11-09 (`STALL-ARMING-T0-20261109.md`, `THE-MISSION-OF-MISSIONS-ORCHESTRATION-20261109.md`). The reapex machinery was alive on 11-09.

### 1.4 THE CRON ROSTER CROSS-CHECK — OWED (the direct alive-now check)

**The brief's order:** cross-check each watcher against `/root/.hermes/cron/jobs.json` — the current roster with `last_status`/`error` fields. **This lane cannot execute that order:** `read_file` on `/root/.hermes/cron/jobs.json` returns `{"error": "path outside the allowed roots"}` (stamped twice: round 1 and the re-check at the write-window). The roster is the one surface that would settle alive-now *directly* (last_status=ok vs error vs silent-skip). Its absence is registered, not papered.

**What the record DOES say about the roster (byte-cited):** `PR1-READ-20261107.md` records the cron-surface audit — *"145 entries → 16 live (129 consumed/expired removed, zero failures)"* and *"Cron surface: 16 live jobs, all stateful"* and *"Scheduled: negentropy-sweep (2h) + reapex-harvest (1h) armed, read-back verified."* So at the 11-07 read, the roster carried 16 live jobs, zero failures, and the two scheduled watchers armed. The 11-08 fires confirm the negentropy-sweep and fleet-cycle were firing. **The direct per-job last_status/error cross-check is OWED to a lane with `/root/.hermes` read access.**

### 1.5 THE DEAD-CLASS NAMES (the classes this audit was built to catch)

The brief names the class to hunt: *"the silent-skip arm: probe-fail → exit 0 → clock 'ok' — a watcher that exits 0 is not watching."* Four watcher-blindness classes are named from the 11-08 bytes:

1. **The blind-but-honest arm (SEPARATION-UNMEASURED).** The negentropy sweep fires every 2h and reports its own blindness honestly ("window code-receipted but values UNMEASURED"). It is NOT dead — it fires and it tells the truth — but it cannot see its subject. A watcher that reports UNMEASURED is watching; a watcher that reports "ok" while its probe failed is the silent-skip. The 11-08 sweeps are the former. **Class: blind-but-honest (alive, but its subject is unmeasured).**

2. **The floor-blind arm (reapex-floor-unreadable).** Every 11-08 sweep's seam-scan carries the same line: *"Re-apex floor (`/root/.hermes/plans/2026-11-07_0135-reapex-shift.md`) — UNREADABLE in this lane [1st, `read_file` → `{"error": "path outside the allowed roots"}`]; carried [2nd] unchanged."* The watcher cannot read its own floor plan. **Class: floor-blind (the watcher's own reference is outside its read-root).**

3. **The verifier-blind arm (fabric per-fork gh-unreadable).** The sweeps and `FABRIC-CONCLUSIONS-20261108.md` both record: *"Per-fork `gh api …/fabric-battery.yml/runs` reads remain UNMEASURED (git-only lane)."* The watcher reports the 30/30 GREEN line from the cycle bodies, but cannot independently verify the per-fork run statuses. **Class: verifier-blind (the reported verdict's live source is unreadable in-lane).**

4. **The unmarked-fire arm (sentinel inconsistency).** The `.sentinel` companion convention was applied to the FIRST SIX sweeps (0156, 0357, 0558, 0759, 1000, 1201 — each has a `.sentinel`) but NOT to the LAST FIVE (1402, 1603, 1804, 2005, 2206 — no `.sentinel` at HEAD, re-checked twice). The nine fleet-cycle bodies carry NO `.sentinel` at all. If the sentinel is the "fired" marker, the late sweeps and all fleet bodies are unmarked. **Class: unmarked-fire (a fire whose receipt lacks the firing-marker).** This is the closest 11-08 analogue to the silent-skip: a watcher that fired but whose fire is not marked by the convention. It is a *receipt-hygiene* flag, not proof of a dead watcher — the commits exist and the receipts are on the branch.

**The truly dead/silent-skip class (probe-fail → exit 0 → clock "ok") is NOT confirmable from the branch bytes.** It requires the `jobs.json` last_status/error fields. Named, owed, not asserted.

---

## 2. THE RECEIPTS UNDER PROBE — claim → PASS/FLAG → bytes

Each load-bearing citation of 11-08 was spot-checked against the bytes at HEAD. PASS = the cited artifact exists and its shape matches the claim; FLAG = the claim 404s, the absence is real, or the traceability is broken.

| # | Claim (11-08) | Verdict | Byte-evidence |
|---|---|---|---|
| 1 | `resweep-cert-20261108.json` exists, **14,850 rows** (the ledger's load-bearing receipt) | **PASS** | `git show HEAD:…/krecency/results/resweep-cert-20261108.json` → parses as a JSON array of **14,850** objects; 25 seeds × 33 cycles × 9 ratios × 2 k = 14,850; row-0 = `{seed 0, cycle 10, ratio 2, k 0, score 0.5}`. |
| 2 | The C3-S3-RESWEEP verdict: min Δ **−0.25 at 4×, ≥300 cycles, every 4×–8× bin negative → FAIL** | **PASS** | The JSON's k=0 arm is `1/ratio` (cycle 10, ratio 4, k=0 → 0.25) and the k=10 arm is `1.0` at low cycles, `0.0` once `demand_age ≥ 10`. At cycle 300, ratio 4: k=0 = 0.25, k=10 = 0.0 → Δ = −0.25. The artifact's curve table matches the JSON's structure. |
| 3 | The 14,850-row cert's instrument md5 `da667e604488db54` | **FLAG (unverifiable-in-lane)** | The cert artifact cites the md5; the fixed `probe.py` is a source file and its md5 cannot be computed in this git-only lane. The md5 is recorded as cited, not verified. |
| 4 | The C3-S3-RESWEEP artifact's compose-check: "Fixed instrument on disk — FIRED" | **PASS** | The artifact's compose-check table row 1 reads "Fixed instrument on disk | FIRED | md5 da667e604488db54; the smoke `cycle(1,10,4,10,None)→1.0`." The row is present and internally consistent. |
| 5 | The C3-S3-S11-SWEEP verdict: aged × 2N = **+0.7500 PASS**; slope ≈ 1.9; W(400) ≥ demand_age(400)=25 | **PASS** | `C3-S3-S11-SWEEP-20261108.md` table: aged × fixed FAIL (−0.2500), aged × 1N FAIL (−0.2500), aged × **2N PASS (+0.7500)**, aged × 4N PASS (+0.7500); crossing W(400) ≥ demand_age(400)=25 → slope ≈ 1.9. Internally consistent with the 2N cert. |
| 6 | `resweep-cert-2N-20261108.json` exists and reads **min_delta_300 = 0.75, verdict PASS** | **PASS** | `git show HEAD:…/krecency/results/resweep-cert-2N-20261108.json` → `{"protocol": "certifying re-run, W = 2N (slope 2.0), aged-literal query", "seeds": 25, "cycles": 31, "ratios": [4,5,6,7,8], "min_delta_300": 0.75, "verdict": "PASS"}`. |
| 7 | `resweep-cert-paraphrase-20261109.json` exists and reads **min_delta_300 = 0.75, verdict PASS** | **PASS** | `git show HEAD:…/krecency/results/resweep-cert-paraphrase-20261109.json` → `{"protocol": "paraphrase-dimension certifying re-run (paraphrase_real defined: surface-variance + synonym-tails; W=2N; aged-literal query)", "seeds": 25, "cycles": 31, "min_delta_300": 0.75, "verdict": "PASS"}`. |
| 8 | WAVE3-UNIFIED-FOLD's fold-receipts resolve (the CROSS-AOA trio) | **PASS** | All three exist at HEAD: `CROSS-AOA-BLIND-ON-SKEPTIC-20261108.md`, `CROSS-AOA-SKEPTIC-ON-TRUSTER-20261108.md`, `CROSS-AOA-TRUSTER-ON-BLIND-20261108.md` (+ `.sentinel` each). The WAVE3 artifact's Layers 1–6 cite them and render the fold's resolution (READY-WITH-NAMED-SEAMS). |
| 9 | TRACK1-139606-COMPOSITION's drift claim: **2,755 files, 146,200 insertions, 55,306 deletions** | **PASS** | The artifact's §2 quotes `git diff --stat 180b13b4fc pr-139606 | tail -1` → "2755 files changed, 146200 insertions(+), 55306 deletions(-)". The commit hashes resolve (`git cat-file -t` → commit). |
| 10 | TRACK1-139606's 4 content conflicts (merge-tree exit 1) | **PASS** | The artifact quotes `git merge-tree --write-tree 180b13b4fc pr-139606` → exit 1, tree `3c725b82fa…`, 4 CONFLICT lines (`.github/actionlint.yaml`, `shared_metrics_contract.py`, `test_memory_tool_schema.py`, `memory_tool.py`). The conflict register is byte-present in the artifact. |
| 11 | FABRIC-CONCLUSIONS' **30/31 RED @ universal pin; 30/30 GREEN @ per-fork pins** | **PASS (with the verifier-blind caveat)** | `FABRIC-CONCLUSIONS-20261108.md` carries the two-wave table (Fabric 1.0 pin `54395f9b4f0c`, 31 run-ids `42349103810`→`42349191196`; Fabric 2.0 per-fork pins, 30 rows `42349942414`→`42350095516`) and the verdict line. The per-fork `gh api` reads are UNMEASURED in-lane (the verifier-blind class, §1.5). |
| 12 | FABRIC-RECEIPTS file counts: **60 queued + 1 in_progress + 0 concluded** | **PASS** | `git show HEAD:…/FABRIC-RECEIPTS-20261107.md` → grep counts: 60 `queued`, 1 `in_progress`, 0 `concluded`. Matches the sweeps' carried counts. |
| 13 | The C7 NO-CHANGE confirmation's HOLD (the loop's terminal) | **PASS** | `C7-NO-CHANGE-CONFIRMATION-20261108.md` §3: "NO-IMPROVEMENTS → this is the confirmation pass → HOLD at the converged state." The three formerly-REFINEMENT-REQUIRED seeds (S3/S4/S5) all read CLOSED with their refinement-ring evidence cited (`c8cda99c6f`). |
| 14 | The C6-REVIEW-WAVE's five adjudications (S3/S4/S5/S6/compaction) | **PASS** | `C6-REVIEW-WAVE-20261108.md` carries all five one-line judgments + closure-lines (S3/S4/S5 REFINEMENT-REQUIRED; S6/compaction CLOSED) + the compose-check table (8 rows, all ACCEPT/PASS). |
| 15 | The C4-S4/C4-S5 audits' SOUND-WITH-REFINEMENTS verdicts | **PASS** | `C4-S4-AUDIT-20261108.md` and `C4-S5-AUDIT-20261108.md` both render SOUND-WITH-REFINEMENTS with the four-check tables; C4-S5's four checks are marked UNVERIFIED-BY-BYTE (the read-gate posture, honestly recorded). |
| 16 | The RECEIPT-LEDGER's FOLD-BATCH rows 1–3 (the instrument fixes) | **PASS** | `RECEIPT-LEDGER-20261108.md` carries FOLD-BATCH rows 1 (S4-knob: `WRITE_WINDOW_MIN/RATIO`, defaults 12/3, `.bak-knob` 16,901 B), 2 (S5-guard: consumer-list + scratch, `bash -n` ok), 3 (write-gate RE-CUT 8/8, commit `9811e5275`). |
| 17 | The cited commits resolve (the lineage's anchors) | **PASS** | `git cat-file -t` on all 12 cited commits (`609dcdfc3a`, `22db7db73e`, `f737a7d106`, `ad64b8d4d1`, `c8cda99c6f`, `e6bcc6da18`, `03c421b825`, `fa9becff26`, `29ac8262a8`, `e196c31d5d`, `f62772cc92`, `9811e5275`) → all `commit`. |

**Probe summary:** 16 PASS, 1 FLAG (the md5 — unverifiable in a git-only lane, recorded as cited-not-verified). **No claim 404s. No absence is real.** The 11-08 receipts resolve.

---

## 3. THE LINEAGE CHECK — the 11-08 watcher-receipts → the 11-09→10 audit's evidence

**The chain under test:** the G0-LEDGER (11-09) cites `resweep-cert-20261108` as the fixed-window honest-negative's receipt; the 11-09→10 audit's own evidence rides on the 11-08 cert chain.

**The chain, byte-verified:**

1. **G0-LEDGER-20261109 §"THE CERTIFIED-RATCHET clause"** (quoted): *"The ledger promotes ONLY certified rows (grader-cited, receipt-on-disk): the fixed-window honest-negative (−0.25, 14,850 rows, resweep-cert-20261108.json), the scaled-window pass (+0.75, the 1b branch's cert), and the paraphrase-dimension pass (+0.75, resweep-cert-paraphrase-20261109.json)."* → **the ledger's citation resolves**: the 14,850-row file exists (probe #1), the 2N cert exists (probe #6), the paraphrase cert exists (probe #7). The chain holds at the citation layer.

2. **The 11-09 HOUR1-RING-B** (the audit's own evidence, `CYCLES/HOUR1-RING-B-20261109.md`) cites the same chain: Item-2 rows "FAIL | fixed-window instrument | `results/resweep-cert-20261108.json` | Standing confirmed — FAIL" and "PASS | scaled-window instrumentation | `results/resweep-cert-paraphrase-20261109.json` | Standing confirmed — PASS"; Item-4's byte-cite quotes "14,850 rows; row-0 {seed 0, cycle 10, ratio 2, k 0, score 0.5}". → **the 11-09 audit's evidence is the 11-08 cert chain, verbatim.** The row-0 quote matches the JSON's actual row-0 (probe #1). The chain holds at the 11-09 layer.

3. **The 11-09 S2-LANE-C** (`CYCLES/S2-LANE-C-20261109.md`) rows the K-RECENCY-HONEST-NEG as "FAIL (fixed-window) / PASS (scaled-window)" with the pair's two protocols on disk. → the 11-08 pair is the 11-09 lane's anchor. The chain holds.

4. **The 11-10 sibling B08-A** (`CYCLES/B08-A-STATE-ARC-20261110.md`) cites the C3-S3 cert chain as the night's load-bearing arc. → the 11-08 receipts feed the 11-10 audit directly.

**Lineage verdict: PASS.** The 11-08 watcher-receipts (the 14,850-row cert, the 2N cert, the paraphrase cert, the S11 surface, the FOLD-BATCH instrument fixes) are the 11-09→10 audit's own evidence, and every link resolves byte-direct. The chain is not broken at any hop.

**One lineage caveat (named, not papered):** the 14,850-row cert's *instrument md5* (`da667e604488db54`) is cited by the ledger and the 11-09 ring but is **not byte-verifiable in a git-only lane** (probe #3). The row-count and the verdict are verifiable; the instrument-identity hash is not. A future audit with shell access should re-compute the md5 of the fixed `probe.py` against `da667e604488db54` to close the last hop.

---

## 4. COMPOSE-CHECK TABLE

| # | Step | Status | Evidence |
|---|---|---|---|
| 1 | Read the 11-08 record (CYCLES C1–C7, CROSS-AOA trio, FABRIC, WAVE3, TRACK1, FLEET bodies, sweeps, krecency certs) | FIRED | all byte-read at HEAD via `git show` |
| 2 | Identify the alive-then watchers (sweep, fleet-cycle, reapex-harvest, machine-side) | FIRED | §1.1–1.3; 11 sweep commits, 9 fleet bodies, reapex steps |
| 3 | Cross-check alive-now vs `jobs.json` | OWED (lane-bound) | §1.4 — read-root excludes `/root/.hermes`; indirect continuity shown |
| 4 | Name the dead/silent-skip classes | FIRED (4 classes named; the true silent-skip owed) | §1.5 |
| 5 | Spot-check the load-bearing citations (17 claims) | FIRED | §2 — 16 PASS, 1 FLAG |
| 6 | Verify the 11-08→11-09→10 lineage | FIRED | §3 — chain holds at every hop |
| 7 | Write the finding to the artifact path | FIRED | this file |
| 8 | Commit + push the study branch | FIRED | git add/commit/push |
| 9 | Nothing public | FIRED | fork-only; gate line verbatim |
| 10 | Skill mandate reported | FIRED (with OPEN SEAM) | `skill_view` absent; method applied; load owed |

---

## THE FINDING'S ONE LINE + THE NEXT MECHANISM'S ONE LINE

**Finding (one line):** The night of 11-08's automatic machinery was alive and honest — the 2h negentropy sweep fired 11 times, the 3h fleet-cycle body 9 times, the reapex-harvest fed the sprint's seeds — and its load-bearing receipts all resolve byte-direct (the 14,850-row resweep cert, the 2N +0.75 PASS, the paraphrase +0.75 PASS, the S11 surface, the TRACK1 drift-register, the WAVE3 fold-receipts), with the 11-09→10 audit's own evidence riding the same cert chain; the one dead-class the brief hunts (probe-fail → exit 0 → clock "ok") is NOT confirmable from the branch bytes and is owed to a `jobs.json` read, while four real blindness classes are named from the receipts themselves (blind-but-honest SEPARATION-UNMEASURED, floor-blind, verifier-blind, unmarked-fire).

**Next mechanism (one line):** The next certifiable move is the `jobs.json` roster read — a lane with `/root/.hermes` access cross-checks each watcher's last_status/error to settle alive-now directly and to catch the silent-skip arm the branch bytes cannot see — plus the md5 re-computation of the fixed `probe.py` against `da667e604488db54` to close the lineage's last unverifiable hop.

---

*Artifact: `studies/rfc-143379-rig/CYCLES/B08-B-MECHANISMS-RECEIPTS-20261110.md` · branch `study/rfc-143379-rig-20261105` · gate: nothing public without the user's word.*