# THE MISSION-OF-MISSIONS — ORCHESTRATION (BEAM, 2026-11-09)

Register: plain, evidence-carrying. Direct-applicable: arming-sequence, state-transitions, chair protocol. Nothing else.

## 1. THE PERPETUAL-LOOP — full mechanism (state machine)

States (S0..S6). Transitions fire on named triggers only.

- **S0 IDLE** → trigger: operator word `go` (chair protocol §2) OR cron at mission-clock restart-point (§4). Guard: byte-closure triple holds (HEAD==pinned SHA, diff --stat empty, plan sha256 recorded). On pass → S1; on fail → S0 with `pending-receipt` row.
- **S1 ARM** (t=0..60): hour-1 six-item shape executes (B4 probe, K-recency honest-negative, certifying re-run, instrument-inclusive sweep, upstream-mergeable pass, gates' frame). No re-plan. Roles load: METER-BUS, GATE-KEEPER, FANOUT-HANDLER. → S2 at t=60.
- **S2 FAN** (t=60..90): Lanes A–E arm in parallel (dependency-collapse). Lane A C44-pilot at actual params; B gate-scan; C G5–G7 field-populate; D SOFT-pool queue; E fleet baseline. → S3 at t=90 (fold-1 trigger).
- **S3 FOLD** (~90m): fast-cadence per-leg receipts present → slow cadence folds. Sub-mission splits arm (A: gate-sweep+temp-sweep; D: one seed per SOFT item). Swap-rotation: seats re-arm per evidence. 24-fold artifact per fold (per-leg receipts + fold receipt + grader citation + independent-witness line). → S4.
- **S4 CHECK** (fold-2 at ~180m): dependency-collapse check (parallel-armed-gates/total-gates ≥0.5); compounding-rate check (fan-out-per-finding ≥2); recursive-breadth (splits double); fleet-scaling (concurrency ≥1.5×). Any check < threshold → that fold flagged SOFT (budget cost 1), never dismissed. → S5 at t=270 (fold-3) or zero-delta → S6-terminal.
- **S5 AUDIT** (t=270..420): audit + AoA land; joint-failure rows adjudicate (single receipt); G5–G7 field-completeness 3/3 = fire-ready; SOFT seeds enter split queue; C24d zero-delta check (measured delta=0 across a fold → terminate, honest-negative accepted). → S6 if zero-delta else S3 (next fold).
- **S6 TERMINAL** (t=600..720): terminal fold; endurance-clause verified (three one-way doors: secret publish, upstream merge without pilot-line pass, paraphrase claim without certifying re-run); fleet-scaling check; terminal metric (12h task-equivalents vs 8h ~800, ratio >8×); handoff receipt written. → S0 (loop restarts at mission-clock restart-point §4).

Self-perpetuation rule: S6 always returns to S0; the loop never stops except on zero-delta fold (S5→S6-terminal accepted as terminal, not failure) or operator `no-go`.

## 2. THE OPERATOR'S CHAIR — minimal definition

The operator sees only:
- **Surface:** one page per fold — the fold's 24-fold artifact (per-leg receipts + fold receipt + grader citation + independent-witness line) + the three gate statuses (evidence/verification/fold) + the chair's one-line verdict prompt.
- **Word needed when:** (a) S0→S1 launch (go/no-go on byte-closure triple); (b) any SOFT-flagged fold (budget cost 1) — operator confirms admit or rejects; (c) any one-way door (publish secret / upstream merge / paraphrase claim) — explicit go required; (d) terminal metric ratio ≤8× — operator decides continue vs close. Nothing else.
- **Protocol:** operator speaks one word — `go` / `no-go` / `admit` / `reject`. No elaboration requested. Chair never blocks on anything other than the four triggers above. All other transitions fire autonomously on evidence.

## 3. THE AMPLIFICATION ENGINE — growth mechanics

- Capacity-per-phase growth-ratio ≥2× (60–240 → 240–420 → 420–600 → 600–720), measured as (legs-armed × folds-completed × seeds-emitted) ratio phase-over-phase. Linear re-scale rejected by design.
- Compounding-rate: fan-out-per-finding ≥2 at every fold (successor-arcs / findings). <2 → fold flagged SOFT.
- Recursive-breadth: sub-mission splits double per phase where evidence permits (splits_n+1 = 2×splits_n).
- Fleet-scaling: concurrency-per-seat grows ≥1.5× per phase.
- Dependency-collapse: parallel-armed-gates/total-gates ≥0.5 by fold-2.
- Terminal: 12h task-equivalents vs 8h ~800, ratio >8× or flagged for head review.
- Grader: every meter cites its grader (external byte-direct audit / independent witness / certifying re-run within window); ungraded meters do not count; standing = graded + receipt on disk.

## 4. THE MISSION-CLOCK — restart-point

The clock re-anchors where solar's execution begins: **the mission-clock restart-point = S0 IDLE at the moment the byte-closure triple holds and the operator says `go`**, i.e. the launch's t=0. Solar's execution begins at that same instant; the clock does not run before the triple holds. Phase minutes (0–60/60–240/240–420/420–600/600–720) are measured from this restart-point, not from wall-clock. On any restart (S6→S0 or zero-delta terminal), the clock re-anchors to the new go moment; prior-phase minutes are not carried. The restart-point marker is the single source of phase timing for the entire loop.
## THE STANDING-DEPTH CLAUSE (binding, the operator's steer 2026-11-09)
Every lane, on every task: runs its OWN 5-why (the task's root-question from its own lens — the chain, counterfactual-validated, ending in its systemic remediation) AND its own webstorm (the possibilities' sweep from its lens — 2-3 mechanisms, each with its adoption-seam + its meter) BEFORE producing its deliverable. The 5-why + the webstorm ride the landing as the lane's depth-evidence. A landing without them is an incomplete landing — the full-team method includes each member's own inquiry, never just the fan's assignment.

## THE SKILL-INVENTORY MANDATE (binding, the operator's steer 2026-11-09 — the made-skills must never be forgotten)
Every lane's brief, on every task: BEFORE planning, scans the full skill-inventory (the chain's 005-skills-inventory — 129 skills, 18 categories, the rig's made-toolkit) and loads EVERY skill that matches its task-class — naming each load with its why at the landing's report. The made-skills are the expert-lens; a brief that doesn't reach for them is under-primed, and a landing that doesn't report its loads is incomplete. The inventory's the library; the usage's the point.
