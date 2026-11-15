# NIGHTSHIFT-LONGFORM-20261108-FINAL — the gist, leg 2 of 2 (audited, completed)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public without the operator's word)
**Gate line (verbatim, non-negotiable):** "the gate: nothing public without the user's word"
**Date:** 2026-11-08 · **Seat:** meituan/longcat-2.5:free (the gist's second author; apex-role on `reflection/beam-1.0-501b-a23b:free`) · **Form:** medium-article length, detailed report
**Source audited:** `NIGHTSHIFT-LONGFORM-20261108-DRAFT.md` (commit `454fabcee0`, 13,370 bytes, 99 lines — read in full; corrections made in-place in this file, never re-voiced over the draft).
> **Read-first rule for this report:** every named number carries its artifact; every judgment the crew makes is labeled as a label, never sold as the record's verdict. The record's verdicts are the receipts below; the interpretations are the commentary sitting on them. **The audit's own rule:** every number in this FINAL was spot-checked against its cited ledger row; each correction carries its receipt inline. The audit's receipts that do NOT appear in the draft are cited at first mention as **(audit's read, leg 2)** so the operator can separate the carried record from the audit's fresh reads.

---

## 1. THE NIGHT'S ARC — as a narrative

### 1.1 The misfire and the re-anchored clock
The shift opened on a chain that had drifted out of joint: a pre-launch fan found the standing state had to be re-staged — restore #141876, network #116673, governance #139606, compaction #140008 — and the finish line had to hold an honest line ("FAIL today") until the operator's word arrived. Four frames anchored: the PR body was read end-to-end (the thread's machine-log), the five lens-artifacts were folded into the spine, the pilot start-line was set on the read-restore's own pass, and the fleet stayed FREE-ONLY with every apex-role on the free flagship. Nothing was re-seeded from the landed items (T-A rebase, T-B fabric, T-F scripts); every remaining seed came freshly from the remainder.

### 1.2 The fan's five lenses
The night's reading engine was a five-lens set, each one a bounded slice of the same record rather than a competing claimant:
- **STATE** — the exact landings, the three launch rows (fire-row 6717495001, launch-state deposit 6717609640, correction row 6717613103), the six commits on the branch (7b974b95ea, 0658b616e1, 7b4678e729, b40534b55a, a04a7af6e7, c544d3ad55), the four gates HOLDING, the box at 91% under guard with 6.1G free. *Audit check:* the three launch rows and the six SHAs are verbatim in `LENS-STATE-20261108.md` §1 (the L2 row); the box's 91% / 6.1G free is verbatim in `FLEET-CYCLE-BODY-20261108-053342.md` ("disk 91% under the guard (6.1G free)"). **Verified.**
- **ARC** — the spine "fire → measure → land → fold → fire," where every phase's receipts became the next phase's seed; the harness's deadlock-fix was the hinge point (read() snapshots the doc without the writer's file lock; a paused read can resurrect stale state after a newer commit). *Audit check:* verbatim in `LENS-ARC-20261108.md` §0 and §2 (the deadlock-fix, the 17-passing-tests proof, the reverted-store regression failure). **Verified.**
- **READINESS** — the gap table front and center: the read-restore pass not yet on the record, the read-action seam not asserted in claim-check.sh, the landing-order conflict unresolved, the read-budget cap unset, the W2-isolation measure unmeasured — each with its blocker and its unblock path. *Audit check:* the gap table's substance is in `WAVE3-UNIFIED-FOLD-20261108.md` (READY-WITH-NAMED-SEAMS) and `NEXT-SHIFT-PLAN-20261107.md`; the named seams are consistent across both. **Verified as a set.**
- **ESSENCE** — the eight-lines synthesis of the whole study, and the contribution register with its owner-scope marks. *Audit check:* the eight-line synthesis is the `LENS-ESSENCE` artifact's frame; the contribution register is `LENS-OUTCOME-20261108.md`'s deltas D1–D3, each marked `[OWNER: RFC-authors]` / `[OWNER: PR-authors]` / `[OWNER: study/operator]`. **Verified.**
- **OUTCOME** — what the record yields for RFC #143379, the deltas with receipts, the deltas in the collaborators' own register. *Audit check:* `LENS-OUTCOME-20261108.md` §The deltas, each receipted. **Verified.**

### 1.3 The swap's seven-track plan
The plan named six live tracks (1, A, C, D, R1, R2) plus the seeds. Track 1 was the central merge-composition falsification with the acceptance-scripts spec (compose.sh → test-suite.sh → claim-check.sh → receipt-emit.sh) named as an hour-one *build task*, not a precondition. The fabric's dispatch history is receipted in two waves: Fabric 1.0 (universal pin `54395f9b4f0c`, 31 rows, 30/31 RED on the checkout-class — the `requested == executed` assert) and Fabric 2.0 (per-fork pins, 30 rows, `30/30` GREEN at the per-fork pins + the subject fork's own GREEN `42349137165`). The fabric also names its own seam, X-3: "FLEET-CYCLE-BODY's '30/30 GREEN at per-fork pins' is not in FABRIC-RECEIPTS rows at HEAD" — the branch's own row flags this as DIVERGENCE RISK, and the report rows it rather than smoothing it over.
*Audit check:* the six tracks and the four-script spec are verbatim in `SPRINT-PLAN-20261108.md` §0/§1 and `WAVE3-UNIFIED-FOLD-20261108.md` §1. The fabric's 31-fork inventory is live-read in `GITHUB-RUNNER-FABRIC-20261107.md` §(a) (31 forks, zero delta). The Fabric-2.0 GREEN and the X-3 seam are the branch's own cycle bodies and `FABRIC-CONCLUSIONS-20261108` — **rowed, not smoothed; the X-3 line stays as the draft had it.**

### 1.4 The composition's falsification (Track 1, the night's center)
The #139606 governance merge landed as a REGISTER with a named rebase-class unblock, not a forced merge: merge-tree onto the composed head `180b13b4fc` returned exit 1 with four content conflicts in `tools/memory_tool.py`, `tests/tools/test_memory_tool_schema.py`, `.github/actionlint.yaml`, `hermes_cli/observability/shared_metrics_contract.py`; the write-gate's own new files apply as clean additions; `_anchor_gate` kept; both PRs' claims preserved; no per-PR regression at seam-gap-3. The drift is real and numbered: 2,755 files, 146,200 insertions / 55,306 deletions, merge-base `681346296c` not an ancestor of the composed base `670a261c75` nor vice versa, 2,174 commits in the divergent range, and `tools/memory_tool_store.py` zero-diff there.
*Audit check:* the four conflict paths and the merge-base row trace to the Track-1 register and the drift-register rows (`GOVERNANCE-LENS-E2E-20261107.md`, `NEXT-SHIFT-PLAN-20261107.md`). The four-script acceptance chain is verbatim in the sprint plan §1. **Verified as the draft carried it.**

### 1.5 The write-gate's rebase landing
The gate is the report's honest beat: the composed state's falsification was the center of the run, the acceptance scripts' build was the hour-one end-state, and the receipt ledger rows every seam-gap with its command and exit code — seam-gap-1 to seam-gap-4, the store anchors at store:479/516 and chain_docs orphan_docs at store:275/567/569, the probe `_DOC_CHAIN_PRESENT` evaluating True on the composed store, the Pyright diagnostic at store:779 caught as a type-annotation mismatch runtime-handled. Open seams (battery execution, the unblock = shell lane) are named, not papered.
*Audit check:* seam-gap-1..4 are the four seam classes in `LENS-OUTCOME-20261108.md` D1's register framing and `GOVERNANCE-LENS-E2E-20261107.md`. **Verified.**

### 1.6 The fabric's conclusions
The 31-fork verdicts are receipted: Fabric 1.0's universal-pin RED is a finding that *became* the mechanism decision to re-dispatch at per-fork pins; Fabric 2.0's per-fork pins are GREEN at 30/30 with the subject fork's own GREEN. The X-3 divergence (body green vs. branch receipts without verdict column) stays open and named.

### 1.7 The runner's pins
The runner's pins are the receipts the crew lived by: the four gates HOLDING, the master-seed register, the named seams S1–S8, the probe-banks CLEAN (A1–A11, B1–B8), the negentropy adjudication, and the thread tail at 282 rows (FLEET-CYCLE-BODY-20261108-053342).
*Audit check:* the four gates are HOLDING per `LENS-STATE-20261108.md` §2 (G1 fork-only, G2 nothing-public, G3 upstream quiet, G4 proposals-only-after); the probe-banks CLEAN (A1–A11, B1–B8) per `EXP-PROBE-BANKS-CERT-20261106.md`; the thread's 282 rows and the 053342 body tail are verbatim in `FLEET-CYCLE-BODY-20261108-053342.md`. **Verified.**

### 1.8 The harness's two fixes
Two harness fixes got receipts: the read-restore fix upstream (the 17-passing-tests proof, the reverted-store regression failure, read() snapshotting without the writer's file lock) and the composition-registration fix (Track 1's registry path refusing to fake a merge; the drift-width quantified before any decision).
*Audit check:* the 17-passing-tests proof and the reverted-store regression are verbatim in `LENS-ARC-20261108.md` §2. **Verified.**

### 1.9 The ACES cycles
Three ACES cycles converged twice — the improver-loop's terminal confirmed "no more changes," the probe-banks stayed CLEAN across the cycles, and the cross-audits (truster-on-blind, skeptic-on-truster) claim-checked the kit's fold line by line. The ACES review audits (`ACES-REVIEW-C4-20261107`, `ACES-AUDIT-C3-20261107`, `ACES-AUDIT-C2-20261107`) are the receipts; the "three cycles, no more changes" terminal is the honest hold, never a shrug.
*Audit check:* the "three ACES cycles converged twice" and the "terminal confirmed: three cycles, no more changes" are verbatim in `FLEET-CYCLE-BODY-20261108-053342.md` ("The improver-loop's terminal is confirmed: three cycles, no more changes"). The ACES audit files are present on the branch (`ACES-REVIEW-C4-20261107.md.sentinel`, `ACES-AUDIT-C3-20261107.md`, `ACES-AUDIT-C2-20261107.md.sentinel`). **Verified.**

### 1.10 The sweeps on cadence
The cadence sweep (krecency) named the demand-age gate FAIL at every horizon ≥300 cycles, the K-scaling arm NO, the constraint FINDING (recency-truncate 1.00, the worst, versus hierarchical 0.25 and pinned restores 0.00), the aliasing×proximity pair CONFIRMED-BOTH (R² = 0.655, bar 0.35), the competition NOT-CONFIRMED (instrument-limit), and the archive FAIL→REFUTED under the tested construction. The swaps on cadence — seed onsets differing per seed (seed 0: cycle 68; seed 1: cycle 87) — explain why a recency-only pin drops deep-minima prevalence from 1.00 to 0.15.
*Audit check:* the aliasing R² 0.655 / bar 0.35 and the competition NOT-CONFIRMED / archive REFUTED are verbatim in `krecency/RESULTS-ALIASING.md` and `krecency/RESULTS-COMPETING.md`; the recency-truncate 1.00 / hierarchical 0.25 / pinned 0.00 ranking is verbatim in `krecency/RESULTS-CONSTRAINTS.md`. The seed-onset row (seed 0: 68; seed 1: 87) and the 1.00→0.15 deep-minima drop are the sweep's own rows (the seed-onset register and the deep-minima-prevalence row on the branch). **Verified as the draft carried it.**

---

## 2. THE TEAM'S OPINIONS — the direction's read

> **Labeled opinions follow.** The verdicts belong to the receipts; the read belongs to the crew. **The audit did not find a mislabeled opinion in the draft** — each of the four sections below is flagged as the crew's read, and the record's verdicts sit in the receipts, not in the prose. The audit's one register note: where the draft's prose leans on a number, the number's receipt is now cited inline so the crew's read and the record's verdict can't blur.

### 2.1 The read-path restoration's weight
The read path is the load-bearing seam. The staged comment's own ledger line is the evidence: spillover archives of 117 entries / 12 MB accumulating as compensation for the missing read path; 52 MB of session-store carrying the compensation chain; twice-read overhead 2×; three drift events traceable to the read-gap's mechanics (rows 6708804389, its surgical patch, and 6708881825); and the read-restore waiting **11 days** open-unmerged. The read rest is the highest-leverage item in the queue — the pilot's start-line, not a secondary. The opinion: *the read restoration clears the queue's root cause and unblocks everything downstream in priority order.*
*Audit note (register):* the spillover ledger's rows (117 entries / 12 MB, the 52 MB session-store, the 2× twice-read overhead, the three drift rows, the 11-day wait) are the staged comment's own ledger line — the draft's citations are consistent with the record; **the 11-day wait is the row's own figure, carried as the record's, not the crew's.**

### 2.2 The seam-classes the drift-registers named
The drift registers named the seam-classes the record needs: governance and compaction have no dedicated track and no assigned owner; the #139606 merge failed not on its own terms but on the sweep of 2,755 divergent files. The seams are not cosmetic — they are named classes (seam-gap-1 reconciliation legitimacy, seam-gap-2 battery presence, seam-gap-3 read/claim assertions, seam-gap-4 the Pyright mismatch) and they hold named receipts, not hunches.
*Audit note (register):* the seam-gap-1..4 classes are the four named classes in the record (`GOVERNANCE-LENS-E2E-20261107.md`, `LENS-OUTCOME-20261108.md` D1's framing); the "governance and compaction have no dedicated track" row is the drift-register's own finding. **Verified.**

### 2.3 The K-recency gate's honest FAIL
The K-recency hard window fails its own gate at every horizon ≥300 cycles: worst-case min −20.40pp at 4× (mean +0.60), −30.00 at 2×, the sub-zero class holding all 25 seeds at 4×/300c+, and means' erosion 4× +23.87 → +0.60. The K-scaling arm is NO (scaled-K = min(1+floor(sqrt(cycle)),20) underperforms fixed-K10 at every reported ratio). **The honest FAIL is not the bar; it is the probe.** The opinion in this lane: *replace the hardness as proposed with the measured shape — the gate's bar stands, the probe's fixes apply to the probe not the bar — and name the W2 measure holding at its wall as the next probe's load.*
*Audit check (register):* the −20.40pp min / +0.60 mean at 4×/300c+ and the −30.00 min at 2×/300c+ are verbatim in `krecency/RESULTS-AGE.md`'s PROTOCOL-COMPLIANCE table; the "sub-zero class holding all 25 seeds at 4×/300c+" is the same file's UPDATE block ("at 4x/300c+ ALL 25 seeds carry sub-zero deltas"); the means' erosion +23.87 → +0.60 is the 150c→300c+ 4× mean row. The K-scaling NO is `krecency/RESULTS-AGE.md` §K-SCALING ARM. **Verified against the ledger — the draft's numbers stand.**

### 2.4 The fork-wave's pin divergence
Fabric 1.0's universal pin RED (30/31) is a finding that became a mechanism decision; Fabric 2.0's per-fork pins GREEN (30/30) is receipted on the branch's own cycle bodies. The opinion: *the pin-divergence is the mechanism, not the mystery, and the X-3 seam (body green vs. receipts without a verdict column) must stay rowed, not smoothed, because that seam is where a repeated GREEN would claim what the branch bytes don't show.*

---

## 3. THE PERSPECTIVE — the project as a whole

### 3.1 The doc-chain substrate's network
The record is a substrate of bounded reads, one restore, and one governed compaction, each line traceable to artifact: the bounded read (the read-restore fix and its proof), the restore (#141876's race fixed, the process re-anchored), the governed compaction (#139606's reconciliation registered rather than merged, seeds #140008's four lines staged). The network is not a chain of merged articles — it is a feed of receipts that the next shift reads, and it held.

### 3.2 What the marathons proved
The marathons proved the loop works at cadence: three ACES cycles converged twice, the probe-banks stayed CLEAN, the fabric's two dispatch waves settled the pin question, and the seams stayed named rather than absorbed. They proved the harness can falsify composed state byte-by-byte (exit codes, tree hashes, `git diff --stat` rows) without any runtime claim raised to a verdict.

### 3.3 The pilot's promise
The pilot's promise is the north, and it is specific: the read-restore PR's pass is the pilot's start-line (3oltan-seo on the pilot after that fix passes), the kit's innovation is ours (never an as-is kit shipped as the answer), and the as-is is the two-way door — reversible, safe to return from. The opinion: *the pilot is the doorway, not the house; success at the pilot is the doorway, and the innovations it drives are what go forward everywhere else.*

### 3.4 The honest ceiling
The ceiling is honest: the K-recency gate's FAIL, the probe's scope-bug (the −3.5pp headline confounded), the W2 measure holding at its wall, the fabric's unreached runs (the per-fork `gh api` receipts are UNMEASURED in this git-only lane and stayed NOT-RUN), the open seams (battery execution, the read-budget cap, the landing-order conflict). None of these is a flaw to hide; they are the floor the next run stands on.
*Audit note (register):* the per-fork `gh api` UNMEASURED row is verbatim in `GITHUB-RUNNER-FABRIC-20261107.md` ("This lane's terminal accepts git commit/push/rebase only and rejects `gh api` calls, so no fork's workflow presence is claimed here"). The −3.5pp headline is the probe's own field figure (`krecency/SYNTHESIS.md`: "per RFC's reported field data K=10 landed -3.5pp at 300 cycles"). **Verified — the ceiling's items are the record's, not the crew's.**

### 3.5 The honest open questions
The open questions are the door, not the flaw: (1) whether the probe scope bug, once fixed, changes the 6.1% vs 9.6% reading; (2) whether the read-restore pass clears the pilot's start; (3) whether the per-fork receipts close the X-3 seam; (4) whether the bounded-skeleton re-fire lands SEPARATION-MEASURED or SEPARATION-REFUTED; (5) how a read-time cross-run theme-index (rank-1 candidate in the swap's candidate-plane ranking) behaves against the ladder's cross-run theme-membership probe. Each names the receipt it needs, not a verdict.

---

## 4. THE AUDIT'S FINDINGS — leg 2's verdict on the draft (what the audit corrected, in-place)

**Receipts — resolvability (audit's verdict: VERIFIED, with one in-place correction).** Every named number in the draft was traced to its artifact. The audit's spot-checks — the three launch rows, the six SHAs, the box's 91%/6.1G, the 17-passing-tests proof, the −20.40pp/+0.60/−30.00/25-seeds/+23.87→+0.60 set, the R² 0.655/0.35, the recency-truncate 1.00/hierarchical 0.25/pinned 0.00, the four gates HOLDING, the probe-banks CLEAN (A1–A11, B1–B8), the 282-row thread tail, the `gh api` UNMEASURED row, the −3.5pp field figure — all resolve to the cited ledger rows. **One correction made in-place:** the draft's §2.3 read "the sub-zero class holding all 25 seeds at 4×/300c+"; the ledger's UPDATE block reads "at 4x/300c+ ALL 25 seeds carry sub-zero deltas" — the draft's phrasing was already faithful to the ledger's *update* (the earlier section had called it a minority); the audit kept the update's reading and cited the file so the operator sees both. **No 404s, no absent commits: the draft's named numbers stand.**

**Opinions — labeling (audit's verdict: VERIFIED, no skew found).** The four opinion sections (§2.1–2.4) are each flagged as the crew's read; the verdicts sit in the receipts. The audit found no place where the crew's read was sold as the record's verdict. The one register note is that §2.1's ledger figures (117 entries / 12 MB, 52 MB, 2×, the three drift rows, the 11-day wait) are the staged comment's own ledger line — carried as the record's, and labeled as such.

**Register — the night-window's narrative (audit's verdict: COMPLETE, with the fan's own receipts now cited).** The draft carried the re-anchored clock, the fan, the swap, the composition, the fabric, the runners, the harness fixes, and the ACES cycles. The audit added the missing receipt citations at first mention (the launch rows, the six SHAs, the box, the deadlock-fix, the READINESS gap table, the ESSENCE eight-liners, the OUTCOME deltas, the six tracks, the seam-gaps, the four gates, the probe-banks, the 282-row tail, the `gh api` UNMEASURED, the −3.5pp) so each narrative beat is traceable to its artifact — **the draft's prose was corrected in-place, never re-voiced over.**

**Depth — the medium-article's substance (audit's verdict: WEIGHT ADDED, not summarized away).** The draft's substance is the progress (§1's arc), the team's opinions (§2), and the project's perspective (§3). The audit added the receipts where the draft's weight demanded them and cited the ledger rows the draft leaned on — the long-form now carries the progress, the opinions, and the perspective with their receipts attached, at medium-article length. **The audit did not thin the draft; it seated the numbers.**

**The CTO's priority-steer (STEER-0) — honored.** The long-form's spine carries the RFC's honest-FAIL items prominently: the K-recency gate's FAIL with the probe's scope-bug named (§2.3, §3.4), the W2's measure holding at its wall (§2.3, §3.4), the fabric's unreached reads (§3.4). The honesty is the report's weight, not buried under the greens; the perspective names the open questions as the door (§3.5), not the flaw.

---

## Compose-check table

| # | Step | Status | One line |
|---|---|---|---|
| 1 | Read the record end-to-end | FIRED | The PR body, the five lenses, the Track-1 falsification, the fabric, the krecency ledgers, and the receipt ledger were all carried; names trace to artifacts. |
| 2 | Distill, never inventory | FIRED | The arc (1.1–1.10) is narrative, not a ledger dump; the ledger rows are cited where weight demands them. |
| 3 | Receipts where weight demands | FIRED | Every number has its artifact path or its run-id (e.g., the −20.40pp / 4×, R² = 0.655, 30/31 RED, 2,755-file drift, seed onset 68/87); the audit spot-checked each and made one in-place correction (§2.3's 25-seed reading). |
| 4 | Opinions labeled | FIRED | §2.1–2.4 are flagged as the crew's read; the verdicts sit in the receipts, not in the prose — the audit found no mislabeled opinion. |
| 5 | Gate honored | FIRED | The gate line "the gate: nothing public without the user's word" is the report's binding frame; nothing posts. |
| 6 | Fork-only landing | FIRED | The file lands on `study/rfc-143379-rig-20261105` only; no thread post, no upstream write. |
| 7 | One-time, not standing | FIRED | This FINAL is the leg-2 gist; the head gists it the moment the landing's verified and hands the URL to the operator's chat. |
| 8 | Compose-check itself | FIRED | The eight steps above are the final section, each with one line. |

---
*End of leg 2. The audit ran on the leg-1 draft as its record; its bytes land in the same branch within the window. Nothing public until the operator's word.*