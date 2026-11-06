# THE NIGHTSHIFT-HANDOFF — 11-05 → 11-06 (the mirror's design)

**The one line:** the 11-06 shift-leader fires from the first turn — grounded on the full record, holding the verified state, armed with the exact first-turn sequence and the ranked fire-order — without re-asking the user anything.

**The floor and the house:** `SHIFT-LAUNCH-PACK-20261106.md` (on this branch, `452e479e18`) is the midnight-operable floor — its state and fire-order stand. This design is the house the floor promised: the complete state-inventory, the cadence's continuity, the launch-pack, the sustain-conditions, and the next-shift's fire-order, each line traceable to the thread, the ledger, or a live read taken at handoff.

**Reading order for the 11-06 leader (binding):** this design → the launch-pack (the floor) → the thread end-to-end (the record — the two-part grounding contract's part one) → the seed. This design assumes the launch-pack's structure; where they speak of the same thing, the design's text is the deepened form.

---

## PART A — THE STATE-INVENTORY (the run's standing, verified at handoff 2026-11-06)

### A1. The verdicts' map (the exact-literal record)
The gate's question — the K-recency hard window at the RFC's letter (300+ cycles, worst-case min) — is measured, and every counter attempted carries a receipted verdict:

| The instrument | The verdict | The exact-literal |
|---|---|---|
| The demand-age gate | **FAIL at every horizon ≥300** | the worst-case min −20.40pp at 4× (mean +0.60); −30.00 at 2×; the sub-zero class holds ALL 25 seeds at 4×/300c+ (the floor's excursions, never a long-session-only collapse); means' erosion 4× +23.87 → +0.60 |
| The K-scaling arm | **NO** | scaled-K = min(1+floor(sqrt(cycle)),20) underperforms fixed-K10 at every reported ratio (the full 4×–8× band); one scaling tested, nothing more claimed |
| The constraint arm | **FINDING** | recency-truncate 1.00 (the worst — the K-recency window's own eviction class) > hierarchical 0.25 > summarize-as-rule = head-retain 0.00; pinned restores 0.00 for all; the pinning-cost: 18 tokens vs the field's ~47, ~0.18% at production scale (the raw 9.84% was the sim's 183-token denominator — superseded) |
| The aliasing × proximity arm | **CONFIRMED-BOTH** | the evidence-mass a*-proxy R² = 0.6548 (bar 0.35); aliasing keeps the deep minima high with the proximity-mass OFF; the proximity-mass alone raises prevalence with aliasing OFF; 800 rows |
| The competition arm | **NOT-CONFIRMED (instrument-limit, three precision-adds)** | the wrong-probe read (wave-4) → the byte-level path-limitation (rivals fire on the latent/survivor path only; the K=10 window-hit path never faces one — `probe_compete.py`) → the equal-weights a* mechanism (`[1.0]+[1.0]*n` — the softmax tracks rival-count, not evidence-mass). NOT a field finding; the probe couldn't touch the path that matters |
| The archive arm | **FAIL → REFUTED under the tested construction** | ID-known recall is the optimistic bound; the budget knob admits only the demanded literal's ID (the toothless-knob); the competing-admission repair (`9c3e89566d`, 19,800 rows) does not clear the gate — the deep minima persist at the taxed budgets; the archive class closed |
| The recitation arm | **NOT-CONFIRMED** | the recite-knob changes prevalence ≤0.1 at every cell/cycle — not the residual; the wheel complete within the tested classes |
| **The pinning arm (the adopted counter)** | **PROTECTS** | recurrence-aware exact-literal pinning drops the deep-minima prevalence at the confirmed aliasing×proximity pair-ON cell from 1.00 (the recency-pinned variant) **to 0.15**; the onset-test explains why: per-seed onsets differ (seed 0: cycle 68; seed 1: cycle 87) — per-seed occurrence predicts the onset, a recency-only pin loses the protection exactly as the falsifier predicted |
| The membership-ring (V1) | **CONFIRMED, then REFUTED under replication** | the original's probe hard-coded its own landmarks (`SEEDS_ONSET = {0: 60, 1: 80}` — the R²'s base); the honest-blind replication (the onsets derived from the stream's own cells) measured R² = 0.0000, weighted = uniform = 1.0000 — no signal, no protection. The circularity's signature, caught by the landmark-gate it birthed (delta-6) |
| The format-adversary (V3) | **FORMAT-AWARE-NOOP** | the triple at the alias+proximity-ON cell: no-pin 1.00 / literal-pin 0.15 / format-aware 0.15 — the format-mask adds zero for +6 tokens; the exact-byte pinning already caps the residual; filed by its own test |
| The portability-arm (E1) | **PORTABILITY-GAP, then PORTABILITY-RECURRED** | the git-log's recurrence-free real streams held 0.80 at the fused cell (the protection is recurrence-conditioned); the real conversation dumps — 147 session-dumps, 15,702 literals (SHA 3194 / path 9272 / arg 3236, 1,031 distinct, recurrence-rate 0.2842/0.3715, 293 recurring) — drop to **0.00** (none 0.80 / literal 0.00 / membership 0.00): the pinning fails only where literals don't recur; the E1-gap honest-closed at `2c3a5402dd` |
| The crossings-arm (E3) | **CELL-DEPENDENT** | the small+old death-cell holds 1.00 across EVERY variant (+0.85 vs the 0.15-bar — the pinning powerless there); the other quadrants 0.00 (strongest protection); the shape recurrence-free — the cell-dependence is the geometry's property, not the stream's |
| The generality-arm (E2) | **REFUTED under replication** | the same circularity-class; the n-panel blind-replicated with no signal |
| The compaction-seam (E4) | **SEAM-CONFIRMED** | the real suite's loss-data classified: the tiny+old quadrant holds 17/21 lost facts (81%; large+old 4; recent 0) — the SAME geometry is the pinning's death-cell AND the compaction-front's loss-cell; the tiny-aged facts are the system's universal fragility-point |
| **Invention-1 — the retention-latch** | **RETENTION-BREAKS-THE-CELL** | small+old-aware retention at full strength (r=1.0) drops the death-cell's prevalence **1.00 → 0.00** at the cost of **3 reserved literals** (3 tokens); the intermediate strengths hold 1.00 — all-or-nothing at this cell, not a dial but a latch |

**The mechanism's conditions, compressed into one map:** the exact-literal pinning's protection rides recurrence-rich AND non-small+old uses; the small+old is the universal loss-cell; the retention-latch — not the pinning — is the seam's design-target. `SYNTHESIS.md` waves 1–18 carry every fold; the derived-never-injected discipline is grep-verified on every probe; `probe.py` (the injected governance_decay term) stays PARKED — NOT-EVIDENCE.

### A2. The frontier's closure
The bearings' five open edges are all receipted: **E5 ✓** (the simplify-core `krec_core.py`, the sameness-gate: 7/7 identity cells, 200-cell 0-diffs — `636648310c`) · **E1 ✓** (PORTABILITY-GAP → PORTABILITY-RECURRED) · **E3 ✓** (CELL-DEPENDENT) · **E2 ✓-refuted** (the circularity's catch) · **E4 ✓** (SEAM-CONFIRMED, 81%). The wheel of measured counter-classes is closed; the inventing-phase has its ground and its first standing result (Invention-1). The record's open questions now: the convergence-independence question (the mirror's fifth lens — the four landings' section-0 source-shape diff: the shared brief's echo vs the models' agreement — ARMED, not yet run), the continuation-loss's mechanism (E4's why: the forward-facts' eviction vs retention at the compressed-state's construction — named, not yet probed), the anchor's precision (the CACHE_THRESHOLD 0.60 re-calibration at the current chain's grounded-minimum — named), the network's deep-looks (the governance-toolkit / toolperf READMEs head-side — named), and the generation-leg's restore (the 9B's re-download — the device-side, the user's glance).

### A3. The in-flights (as of the handoff's live reads)
- **The dual-surface's landing-row — VERIFIED COMPLETED, NOT YET POSTED:** run `42163546699` = **SUCCESS on BOTH legs** — "Avrea full-suite (main)" on the hosted surface ("GitHub Actions 1000001316") AND on the self-hosted surface ("pve1-avrea-parallel"). The thread's last row on it said "in progress"; the completion is newer than the thread. The 11-06 leader posts the landing-row: both legs GREEN, the divergence-as-data noted, the same pinned head on both runners, fail-fast off. (The matrix's earlier collision-class — the workflow-level matrix-context, the 422s, the rebase-wiped matrix — is receipted on the record; the fix's the job-level context.)
- **The union's full-battery run — VERIFIED COMPLETED, NOT YET ROWED:** run `42160049664` = **SUCCESS** (the union @ the new head). Its GREEN row lands in RECEIPTS.md and posts to the thread.
- **Three matrix-lineage runs PENDING in the queue** (`42163543142`, `42163542578`, `42163542489` — the dual-restored dispatch's family): pending as of the handoff read; their rows land as they resolve — PENDING keeps its marker until a receipt replaces it, exactly like NOT-RUN.
- **The network's deep-looks** (the governance-toolkit's and the toolperf's READMEs — head-side reads, the mission-map's next rung): named, not yet executed.
- **The compaction-annex's fold** (DELTA-5's measurement-surface into the study's compaction-side) and the **continuation-loss pattern-probe**: named candidates.
- **The fleet's circle: complete 4/4** — longcat (`77a441dc92`) · beam (`19723b3c51`, + the competing-admission candidacy, verdict ARCHIVE-REFUTED) · solar-mini4 (`1d70408531`, + the precision-lane's THRESHOLD-CLASS) · the step-designation (`bde8ff5f37`, on the beam-seat's rotation — the swap recorded, the designation held). The paid-leg's mirror-verdict (`c2874c6a6c` — the independence-question + the GREEN-count's harmonization `eb00e5e294`).
- **The anchor's revival**: retrieval-half live (NOT-IN-CHAIN's the honest-refusal's proof); the generation-half's engine is the device-side door, at the user's glance; the threshold's re-calibration is the named next.

### A4. The ledger's one-to-one (the number-seam's rule, live)
The ledger (`RECEIPTS.md`) is the truth's home — counted from the file, NEVER from the summaries (the day's own lesson: README "five" < summary "eight" < ledger "nine" — the seam closed by counting the rows, `eb00e5e294`). Current state: eight run-backed GREEN rows (the composition pins, the leads, the whole-anchor twice) + the apex-day rows (the falsifier's GREEN `42096454325`; the RED-chain `42096273475` / `42096589644` / `42098517565` / `42103142238` / `42146442559` / `42146330495`, each with its cause) + the first guarded GREEN `42148028348` (16 passed / 77 skipped-with-reasons / 0 failed) + the sweep-arm's GREEN `42150952031`. The rows one-to-one with the runs; the REDs each carry their OWN cause (never the previous run's); the guarded-GREEN's arc (5→1→0) is the discipline's proof; the runner's day-slope +0.17 (green-rate 0.24 → 0.41) is on the record. The two new rows (A3) are the leader's first additions.

---

## PART B — THE CADENCE'S CONTINUITY (the loop's binding rules)

### B1. The machine-log's rule — NEVER silent
Every rig-side landing posts to PR #1's comment-thread ON ARRIVAL: the arms, the sweeps, the results, the gates, the fleet's findings, the stalls, the REDs, EVERY test-feeder (the fork-experiments included) — rowed as they resolve, envelope-formed (the Executive Summary / Analysis Brief / Recommendation / Next Steps / Artifact shape; the machine-envelope id/kind/from/to/status in the header; handles-only, no internal vocab — the thread's public face stays the envelope's). A stall posts like a landing — its cause named, its fix in the SAME comment (the ownership comma-precision: the fix AND the cause in one receipt). Nothing a model does stays off the thread; the false-claims register stays empty.

### B2. The quiet-boundaries (absolute)
- **The RFC's upstream issue (#143379): QUIET until the user's word.** No byte, never, in this arc.
- **The owners' surfaces are theirs.** The xngg-thread's verification material is staged at homebase, ready for the word to share — never posted early. The enrichment-candidates (the AC3-line, the retrieval-scope, the lesson-bank fold, the #139606 idempotency-line, the #25309 swimlane-line) are internal proposal-notes only, waiting on their owners' word AND the user's gate.
- **The fork-only rule:** the rig rides publicly nowhere but PR #1's thread. No credentials, ever; the session-dumps' mined literals stay redacted (the portrevisit's provenance line: no credentials, content stays on the rig).
- **The user's word is the only gate.** The HITL-READY seven candidates sit staged; the approved-public moves fire on the word — no re-ask, no self-gate, but equally never before it.

### B3. The loop's contract (the self-perpetuating form)
ARM with the finish-line-first (the failable check, written before the run) → GROUND (every starting-lane reads PR #1's thread end-to-end via the API, THEN its seed — no lane starts cold) → RUN (the ready-nodes in parallel, each under its frozen brief, the think-tank's spine + the LP-armament) → FOLD (every landing to the thread, the ledger's row) → VERIFY (the finish-line at the last landing; two consecutive PASSes with zero new classes = the no-improvement proof; a third run confirms it) → RE-ARM (the next ring's nodes from the record's grown candidates). The thread is the ground and the record; the anchor's untouched by curation; the fold routes downstream.

---

## PART C — THE LAUNCH-PACK (the first-turn's script for the 11-06 leader)

Fire in this exact order — the user's word is already on the record; nothing here re-asks it.

**Turn 1 — ground (the LOOK's groundwork):**
1. Read this design (the house), then the launch-pack on the branch (the floor).
2. Read the thread end-to-end: `gh api "repos/c0wb0yp0tat0/hermes-agent/issues/1/comments?per_page=100"` → file → read ALL (84 comments as of this handoff; the loop's contract: the grounding-comments ARE you).
3. Read the anchor: `/root/.hermes/memories/MEMORY.md`; the memory-chain at `/root/workspace/master-page/memory-chain/` (INDEX.md first); the `cto-session-brief` + `think-tank` skills.

**Turn 1 — the LOOK (live, before any movement):**
4. The runs' statuses: `gh api "repos/c0wb0yp0tat0/hermes-agent/actions/runs?per_page=10"` — expect: `42163546699` completed-success (the dual, both legs), `42160049664` completed-success (the union), the three matrix-pendings unresolved. PENDING stays PENDING until a receipt replaces it.
5. The disk: `df -h /` — at the handoff: **92% (5.6G free) — the guard's trip threshold.** The guard (`/root/.hermes/scripts/runner-workspace-guard.sh`, v2, the SINGLE disk owner) is ARMED as the Hermes cronjob "runner-workspace-guard (disk)" — every 15m, enabled:true, deliver origin (verified at handoff; the system crontab is NOT its home — do not re-add it there). Its contract: drains the regenerable runner-scratch at ≥92%, NEVER while a Runner.Worker is live (the 13:45Z lesson), stateful alert (exit-1 on the first trip and on each real regression), the top-consumers named when the drain's exhausted. The machine-log already records the storage-design: the PR is the face, the private repo the storage, the local disk the cache — nothing canonical lives only locally.
6. The seats' liveness: the runner's listener (`ps aux | grep actions-runner` — the pve1-avrea-parallel runner WAS alive and idle at handoff); the fleet's seats (the circle 4/4 — no seat owed); the step-seat's fair-share window (the 429-class: re-probe every roster round if a seat's needed; the paid-seat ONLY on the user's explicit word).

**Turn 1 — the movement (never the standing-by):**
7. Post the pending landing-rows (A3 — verified, ready to fire): the dual's both-legs SUCCESS (`42163546699`, hosted + avrea, the same pinned head, the divergence noted) and the union's GREEN (`42160049664`); add their ledger-rows (the one-to-one, held). If a matrix-pending resolved, its row posts on arrival too.
8. Re-arm the loop: the seam's design-implication arm (the fire-order's #2) dispatches — its brief carries the two-part grounding line and the frozen contracts.
9. The next-beat's arming: the leader names the ring's finish-line (a real failable check) before the run — the launch-pack's fire-order #3–4, deepened in Part E below.

**The no-standing-by, the no-flattening:** the LOOK feeds the movement the same turn — statuses, disk, seats, THEN the next-arm's dispatch. The depth's the standard: the continuously-working contract means the next meaningful iteration, never the activity for its own sake; a FAIL verdict is a finding, never smoothed; finishing early means more loops, never shorter.

---

## PART D — THE SUSTAIN-CONDITIONS (the standing frame)

- **The disk-guard's state:** at threshold as of the handoff (92%); the guard armed (the Hermes cronjob, 15m, enabled); the manager's contract: the drain only when idle, the state-file alert, the single-owner rule (no other process decides the disk). The watch's rhythm: the cache-clean after heavy runs (the uv-cache class — 750MiB proven regenerable), the guard's state watching in every LOOK. The scratch's 24h-prune applies to the run-trails (regenerable by design); the receipts are canonical on the remote, never only local.
- **The meters' truth:** the Avrea runner is SELF-HOSTED — GitHub Actions usage is free for self-hosted runners; the provider's free-meter classes (3,000/1,500 min) apply to its hosted VMs only, NEVER the rig's host. The contract's "meter budget" is self-imposed stewardship — the governance-frame (one run per pin, no re-dispatch without a named reason) kept by CHOICE, not necessity. The README's goal-lock was corrected to the self-hosted truth on the record (`aa665da915`); the discipline-layer table's "3 of 6" line is the stewardship-era framing — the corrected reading governs.
- **The seats' rotation:** the fair-share's windows respected (the step-seat's 429-drain → PARKED with the reason, re-probed every roster round — the finding eventually rode the beam-seat's rotation, the swap recorded, the designation held); the probe-before-pin (a dispatch ALWAYS carries the full 40-char SHA — the abbreviated-pin class cost two runs and is owned twice on the record); the paid-seat only on the user's explicit word.
- **The two-writer discipline:** the ledger == the thread, rows one-to-one with the runs; the machine's voice (the landing-step) and the head's cadence both write to the ONE thread, never two records; the dual surfaces (avrea + hosted) row into the same ledger, divergence as data, never smoothed; each RED's own cause (never the previous run's class); a receipt means the executing surface checked out exactly the listed SHA before its suite.
- **The sessions-pressure's counters:** (1) **the proud-hour** — the proud hour is the careless hour; the abbreviated-pin recurred exactly in the proud hours; the class-map's two entries keep the discipline spoken-and-executed, never spoken-not-executed; the record says so in the same comment as the fix. (2) **the landmark-gate** — every instrument's review asks the circularity-question FIRST: does the predictor KNOW its own answer? (a hard-coded landmarks-table in the probe = the injection's signature); a CONFIRMED flagged by the check MUST carry its replication-arm — the honest-blind replier is the truth-maker, and a replication that zeroes the signal REFUTES the original's CONFIRMED on the record (the membership-ring's exact shape). (3) **the number-seam** — count from the ledger, never from the summaries; the register's count is the file's rows, the run-sizes cited per pin (the "28 passed, 1 xpassed in 1.01s" is the whole-anchor host-local row — a single-pin number, never a global battery total); the triple-drift (five/eight/nine) closed by counting, and the count keeps closing as the rows accrue.

---

## PART E — THE NEXT-SHIFT'S FIRE-ORDER (the candidates ranked, the gates sequenced)

The frontier's named candidates, sorted by value-of-information from the record's own closing. **Each landing gates the next** — a cell blocks its successor; nothing dispatches before its gate opens; every landing posts on arrival.

**E-1 → the recency-landing rows (the day's freshness — fires immediately, gates nothing):** the dual's both-legs SUCCESS (`42163546699` — hosted "GitHub Actions 1000001316" + self-hosted "pve1-avrea-parallel", the same pinned head, the divergence-as-data noted) and the union's GREEN (`42160049664`) — posted to the thread, rowed in the ledger, the matrix-pendings' resolution-rows as they land. The thread's current truth refreshed within the first turn.

**E-2 → the seam's design-implication arm (the mechanism's first adoption-candidate — fires after E-1):** the retention-latch's real-compaction integration — Invention-1's r=1.0/3-literals verdict (1.00→0.00 at the death-cell) is the record's first standing invention, and the seam's named design-target ("the retention, not the pinning"). The arm: the small+old-aware retention mapped onto the real compression-fixtures' construction (the compaction-front's own cells), its falsifier stated in advance, its cost-line (the reserved-literals' 3-token budget) re-measured at the real loads. The launch-pack's fire-order's #3 names the same arm — this is its deepened brief. Its red is a finding, never smoothed.

**E-3 → the continuation-loss pattern-probe (the E4-mechanism — gated by the seam-arm's landing):** WHY the forward-facts evict at the compressed-state's construction (the three-fixture suite's measured loss-front: continuation-execution-time 0.17, decision-core-claim-validity 0.00, continuation-next-action 0.67, implementation-scope 1.00, recall-upstream-confirmation 2.00; the feature-impl's clean profile as the control slice — the loss is content-patterned, not uniform). The probe's falsifier: if the small+old class carries the continuation-losses, the retention-latch's adoption gets its real-side receipt.

**E-4 → the mirror's independence-probe (the fifth lens — gated by E-3):** the four fleet landings' section-0 source-shape diff — the shared brief's echo vs the models' agreement — the convergence-signal's own audit. Its verdict sharpens (or bounds) the four-lens convergence the record leans on; it is the paid-leg's named question, run on the record's own terms, its answer either way a receipt.

**E-5 → the network's wildcards (the fork-network's mission-map — PARALLEL-eligible, gated by the runner's availability):** the governance-toolkit's and the toolperf's deep-looks (their READMEs' head-side reads — the governance-line's and the compaction-line's feeders); the compression-eval's full-fixture suite (the smoke's single-fixture floor superseded by the medians — the RFC-compaction's measurement-surface, provider-configured, never CI); the ANOLISA-docs read and the roster-shape draft (the orchestration-namesake + the apex-dump's evolution — second-order, as the seats free). The map's 31 forks stay pre-positioned; nothing touches another fork's surface — the deep-looks READ, never write.

**E-6 → the anchor's precision-leg + the generation-leg's restore (the device-side, the user's glance):** the CACHE_THRESHOLD 0.60's re-calibration at the current chain's grounded-minimum (the C27-era knee vs today's representations — the threshold-class's live measurement) and, behind the user's word, the generation-engine's restore. The engine's the whole route's single-point; the retrieval-half's already alive.

**The loop, at full strength:** ARM → GROUND → RUN → FOLD → VERIFY → RE-ARM, the launch-pack's ring. The peak-everything loop holds until the no-improvement's proven — the finish-line's failable check written FIRST, two consecutive PASSes with zero new classes, then a third run confirms, then the fold's proof lands and the arc re-arms from the grown candidates.

---

## PART F — THE GOAL'S POINTER (the true finish-line, never confused with the inventory's gate)

The finish-line is the GOAL's arrival, line by line — PR #1 is where the evidence accumulates en route, never the arrival itself: **the read-restore (#141876) merged upstream · the network-anchor's adoption (#116673) · the governance's landing (#139606) · the compaction/dream-cycle's fixes (#140008)** — each with its fruition-condition, each pending the user's word and the owners' windows. The inventory-gate's place is the ledger's: guarding the record's truth, never standing in for the goal. The HITL-READY seven candidates sit staged for the human's read; the approved public moves fire on the CTO's word — no re-ask, no self-gate, and equally never before it. The RFC's upstream issue stays quiet; the owners keep their scopes; the rig rides publicly nowhere but here.

**The closing line:** the 11-06 shift-leader fires properly because the record is complete, the state is verified, the gates are named, and the word is already on the record — the loop perpetuates itself through the one place, and the one place is this thread.
