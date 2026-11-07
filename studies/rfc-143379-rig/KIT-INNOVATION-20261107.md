# KIT-INNOVATION-20261107 — the substrate pilot kit, innovated-first (2026-11-07)

**Seat:** `stealth/crouton-alpha` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public) · **Lane:** copycat · **Register:** receipts, never claims — every claim traces to a file on this branch or a commit in its log.
**THE NORTH (binding, `NEXT-SHIFT-PLAN-20261107.md` header):** the study's aim is the substrate pilot kit — OURS, innovated-FIRST, never an as-is kit; the kit's pilot starts with 3oltan-seo AFTER the read-restore PR fix passes; the machinery's outputs feed the kit, the landings gate the pilot, never the reverse. This document is fork-only substrate work, not a recommendation to ship anything as-is and not a move aimed at the upstream lines' landings.

---

## (a) THE SUBSTRATE INVENTORY — the receipted components a pilot kit is built from

Each component: the claim + its receipt + the revision it gives the kit.

### A1. The verification-fabric's per-fork independent receipts (FABRIC-RECEIPTS)

**Claim:** The platform-side verification has true breadth independent of any one surface: 31 forks, each its own hosted-runner window, each dispatched the same pinned battery, each returning its own receipt.
**Receipts:** `GITHUB-RUNNER-FABRIC-20261107.md` (`6fef8e3379`) — the live inventory, counted exactly: 31 forks, zero delta vs the brief's 31 (`gh api "users/c0wb0yp0tat0/repos?fork=true&per_page=100"` → 31; count query → `31`), full name·default_branch·pushed_at table receipted verbatim. `FABRIC-RECEIPTS-20261107.md` — the amplifier's launch: deployed+dispatched 2026-11-07 01:52–01:57 ET at the universal pin `54395f9b4f0cc1d0a840ec2640580e7af9c4ed25`, 31 runs receipted with distinct run-ids (`agent-governance-toolkit … 42349103810` → `projectsend … 42349177806`); the inputs-encoding finding banked (422→204 on `-f inputs=` double-escape; `--input -` object form), commit `9dc35ee053`. Later evolution receipted in `FLEET-CYCLE-BODY-20261107-1403.md` (`f084af11cf`): fabric 2.0 per-fork-pin re-dispatch at `2becb714af` — 30/31 RED at the universal pin on the checkout-class, then 30/30 GREEN at the per-fork pins + the study fork's own GREEN + the subject-variant wave GREEN (py + js + session-runtime-lint cells). Honest seams banked in the same receipts: workflow presence per fork UNMEASURED in the git-only lane (`GITHUB-RUNNER-FABRIC-20261107.md` L7/49, "no fork's workflow presence is claimed here"); conclusions absent at the C3 ground (30 `queued`, 1 `in_progress`); the weak-receipt arm's settle-condition closed in C3 (31 run-ids scan-verified distinct, `42349103810 … 42349191196` — AUDIT-C3 row 6, REVIEW-C3 C3-6).
**Revision to the kit:** The kit's verification layer is per-fork independent receipts, never a single-surface claim — the "hosted trio" class (one fork's window) is demoted to a surface, the 31-fork fabric is the breadth. Per-fork pins derived from a universal-pin RED are a kit mechanism (the checkout-class finding), and distinct-run-id is the kit's receipt-granularity floor.

### A2. The improver-loop's honest-termination proof (the ACES cycle, converged twice)

**Claim:** The ACES loop terminates honestly on a real no-improvement, and that termination is itself receipted — twice.
**Receipts:** `ACES-IMPROVE-C3-20261107.md` (`c9a0325719`) — cycle 3 names **0 improvements**; the 7 seed arms are re-examined, not re-named (1 closed, 2 partially satisfied, 4 standing unchanged); the stop-line is NO-IMPROVEMENTS. `ACES-AUDIT-C3-20261107.md` (`ca15b98e1f`) — **11 CONFIRMED / 0 NUANCED / 0 REFUTED**, READY-FOR-THE-REVIEW, every row re-derived independently. `ACES-REVIEW-C3-20261107.md` — the chain's end applies the audit's catches in a corrections-ledger (C3-1…C3-9, each APPLIED—CONFIRMED or KEPT OPEN honestly, nothing smoothed). `FLEET-CYCLE-BODY-20261107-1403.md` records the convergence confirmed a second time: cycle-4 named 0 improvements again (AUDIT-C4 11/11 CONFIRMED, REVIEW-C4 `ccd33a1ebf`); the constant copycat confirmed zero in-substance divergences across C1–C3, C4 honestly UNMEASURED at read time (`e1d9b0c51b`).
**Revision to the kit:** Honest termination is a kit feature, not a failure mode — the loop's product is the *converged state plus the backlog's honest classification* (closed / partial / standing). Zero new claim bytes → zero new improvements is the loop's receipt discipline, so a kit that ships the loop ships a stop-condition it can prove it met.

### A3. The receipt-discipline's mechanics (the envelope ledger, the goal-lock, the NOT-RUN honesty-markers)

**Claim:** The study's receipt machinery — the mechanism envelope, per-arm goal-locks with settle-conditions, and the NOT-RUN/UNMEASURED/WALL-CLAUSED/MARKED-OPEN census — is what makes every other component trustworthy.
**Receipts:** `FLEET-CYCLE-BODY-20261107-1403.md` — the mechanism envelope as the study's one place (Executive Summary + CURRENT STATE + Standing Plan, each rowed on arrival, local = remote verified at every landing-gate). `NEXT-SHIFT-PLAN-20261107.md` §1 — the goals table: each arm's done = a receipted verdict-shape with the receipt named (e.g. goal 1: the filled skeleton's result file + the W2-ISOLATION-STATUS verdict-line flipped from SEPARATION-UNMEASURED). `HONEST-WALLS-CENSUS-20261106.md` — **40 markers enumerated: 8 NOT-RUN, 8 UNMEASURED, 16 WALL-CLAUSED, 8 MARKED-OPEN**, each quoted verbatim with its settle-condition; verdict CENSUS-COMPLETE; the census's own UNDER-SPECIFIED list non-empty (3 entries) and flagged, not smoothed. `HITL-GAINS-SKEPTIC-20261107.md` — the counter-pass that re-derives the non-progress ledger (four lines STAGED, gates untouched) and is wrong only if it reads waiting as drift.
**Revision to the kit:** The kit carries receipt-discipline as its operating system: envelope ledger per component, goal-locked arms with named closing receipts, and the honest-marker census as a first-class status vocabulary. A kit component's state is always one of the four marker classes or a receipt — never an adjective.

### A4. The compaction-front healing (the scientific front #1)

**Claim:** The tiny+old loss-class walked driver-by-driver and healed — 3-block composition, 5/5→0/5, blind-audit-reproduced.
**Receipts:** `EXP-SUMMARY-NIGHT-20261106.md` — "the compaction-front's tiny+old loss-class walked driver-by-driver and HEALED (3-block composition, 5/5→0/5, blind-audit-reproduced)". `EVAL-LADDER-BATTERY-20261106.md` — the five-rung ladder measured in place (15 runs at substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`): recovery medians 4.50 / 3.25 / 4.67 / 1.00 / 0.00; verdict LADDER-SEPARATED — recovery does not track compaction depth (deepest compaction, rung 3, recovers best at 4.67); it tracks fact-density / tiny+old-anchor survival (the E-3 small+old class). `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` — the four protected classes RESOLVED with weights from the E-3 loss-geometry (decision-core w 3.00 > clock/exec-time w 2.83 > next-action w 2.33 > scope w 2.00); the one-anchor case NECESSARY-NOT-SUFFICIENT (the verbatim `open_id is app-scoped` survives into summary_text yet the answer is `""` in all three runs — Wall W2); pattern-blindness correction (Cell A literals match no pattern in `_ANCHOR_PATTERNS` — C2 has no class for these strings).
**Revision to the kit:** The kit's compaction component is density-aware, not depth-aware — protection budgets keyed to the four weighted classes, reserving the highest-loss-likelihood anchor as necessary-not-sufficient, with the pattern-blindness wall named as a known gap.

### A5. The seam-cleared arc (the scientific front #2)

**Claim:** The seam-arc walked ordering-NULL → literals-partial → derivations-partial → anchors-effective → composition-marginal → intents-SEAM-CLEARED; the audit's REPRODUCTION-DIVERGENT at +0.33 (the grain) was CONFIRMED at the substance.
**Receipts:** `EXP-SUMMARY-NIGHT-20261106.md` — the six-movement walk; the fix quantified: derivations ~120 + time-anchors ~60 + forward-intents ~60 = ~240 tokens (2.4%) heuristic, the #140008-line's candidate. `FLEET-CYCLE-BODY-20261107-1403.md` — the four-movement walk lifts the below-3.0 hold 5/5 → 1/5, the median 0.67 → 3.00, on ~60 tokens (0.6%) of time-anchor block (`847c61ac4f`; W2-isolation SEPARATION-UNMEASURED per the wall-clause — the eval-runtime cannot execute the isolate re-run yet). `krecency/SYNTHESIS.md` — the K-recency gate's measured FAIL (the one experiment that converts preparation into arrival, unmeasured), with the one-mechanism line: the recitation floor and the governance decay are one window wearing two hats.
**Revision to the kit:** The kit's seam component ships the quantified heuristic (≈240 tokens, 2.4%) as its current best composition, with the +0.33 grain-divergence recorded as a known instrument correction — and the K-recency FAIL as the kit's measured negative result, the counterweight that keeps the healing claim honest.

### A6 (bonus). The enrichment arc's closed loop

**Claim:** The enrichment producer→audit→correction loop closes inside a cycle, each step receipted.
**Receipts:** `FLEET-CYCLE-BODY-20261107-1403.md` — producer `204bf6c672` (`PR-ENRICHMENT-20261107.md`, after three zero-write deaths, each evidenced with its class named); independent audit `537d2c3bda` (verdict PASS, per-axis ledger); record correction `f084af11cf` (the artifact's own drift named: mangled refs + scope-exceed + the body's restore receipted). `ENRICHMENT-AUDIT-20261107.md` — per-axis receipts, e.g. A1 amplifier claims CONFIRMED against `9dc35ee053`, A10 the audit-vs-review count difference (4 vs 3) marked NUANCED not REFUTED.
**Revision to the kit:** A producer/audit/correction closed loop with zero-write deaths evidenced rather than hidden is the kit's self-repair component.

---

## (b) THE INNOVATION-CANDIDATES — what the kit must BE beyond the as-is assembly

Each candidate is grounded ONLY in the study's actual findings, named with its evidence and its open question. These are **proposals, never settled design**.

### B1. A first-class NOT-RUN status as a kit state, not a caveat

**Evidence:** `HONEST-WALLS-CENSUS-20261106.md`'s 40-marker census (8 NOT-RUN, 8 UNMEASURED, 16 WALL-CLAUSED, 8 MARKED-OPEN), each with a settle-condition; the fabric's queued/conclusion-less rows at the C3 ground, held open rather than filled in; `HITL-GAINS-SKEPTIC-20261107.md`'s "waiting ≠ drift" distinction.
**Proposal:** The kit's component register treats NOT-RUN as a terminal honest state with a named settle-condition — a component can be *complete-as-NOT-RUN*, and the register never forces a run to close a marker.
**Open question:** What is the kit's staleness rule — after how many cycles does a NOT-RUN marker's settle-condition get re-examined, and by which lane? (The census names 3 UNDER-SPECIFIED markers whose settle-conditions are class-level, not experiment-level — the kit needs to know whether class-level settle-conditions suffice.)

### B2. Per-fork independence as the kit's breadth measure

**Evidence:** The 31-fork fabric (`GITHUB-RUNNER-FABRIC-20261107.md`, `FABRIC-RECEIPTS-20261107.md`) replacing the "hosted trio" (one fork's window); the per-fork-pin re-dispatch turning 30/31 RED into 30/30 GREEN (`FLEET-CYCLE-BODY-20261107-1403.md`).
**Proposal:** The kit measures verification breadth as the count of *independent* per-fork receipt surfaces (distinct run-id, distinct pin where the class demands it), not as run volume on one surface. A kit claim's confidence is a function of fork-independence, never of a single window's greens.
**Open question:** Which surfaces must be fork-independent for a kit component to be pilot-eligible — all 31 forks, or a named quorum? The study's receipts show the fabric exists; the eligibility threshold is not in the bytes.

### B3. The harness write-deadline as a designed pressure-point, not a lore seam

**Evidence:** ACES C3 Arm 6 / IMP-8 (harness-deadline) STANDS, kept open — no PR-UPDATE ack in branch bytes since `5e0774420b`, thread UNMEASURED in the git-only lane, "neither confirmed nor refuted from branch bytes — kept open, never smoothed" (`ACES-AUDIT-C3-20261107.md` row 9; `ACES-REVIEW-C3-20261107.md` C3-9). The brief names it: "the harness write-deadline — named, unbuilt."
**Proposal:** The kit treats the write-deadline as a named, bounded, falsifiable pressure-point: a deadline with a settle-condition (a receipted ack or a wall-clause), part of the kit's design review, never an ambient convention.
**Open question:** Is the deadline's settle-condition a thread row-id (the head's posting) or a branch-byte artifact? IMP-8's kept-open status is precisely because the two have never coincided in the receipts — the kit must pick one and price the other as a wall.

### B4. The eval pending the provider-window as a scheduled kit instrument

**Evidence:** `EXP-SUMMARY-NIGHT-20261106.md` — "the composition's full-eval at the provider-window's return (the ladder's ready)"; `EVAL-LADDER-BATTERY-20261106.md` superseding `LADDER-PARTIAL` "the window is open and all 15 runs executed"; W2-isolation SEPARATION-UNMEASURED "per the wall-clause — the eval-runtime cannot execute the isolate re-run yet" (`FLEET-CYCLE-BODY-20261107-1403.md`).
**Proposal:** The kit wires its eval instruments to the provider-window as a standing schedule: each pending eval is a rung with a named window-condition, so the kit's readiness advances on the window's return, not on ad-hoc re-attempts.
**Open question:** What does the kit do while the window is closed — hold (the study's current register) or run a degraded local proxy? The battery's PARTIAL→FULL history shows the window returning; the bytes contain no degraded-proxy run.

### B5. Honest termination + the backlog's classification as shippable kit machinery

**Evidence:** ACES converged twice on NO-IMPROVEMENTS (`ACES-IMPROVE-C3-20261107.md`; AUDIT-C4/REVIEW-C4 per `FLEET-CYCLE-BODY-20261107-1403.md`); the C3 backlog classified 1 closed + 2 partial + 4 standing, each with its settle-condition; the enrichment arc's zero-write deaths evidenced with classes named (`f084af11cf` cycle-body).
**Proposal:** The kit ships the loop *with* its termination proof and its backlog classification — a converged loop is a delivered component, and its standing arms are the kit's named next-work, not debris.
**Open question:** At pilot time, does a converged loop with 4 standing arms count as ready, or must the standing arms' settle-conditions be re-fired first? The study's bytes record the convergence, not the eligibility verdict.

### B6. The one-anchor necessary-not-sufficient pattern as a kit reservation theorem

**Evidence:** `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` — reserving `open_id is app-scoped` verbatim into summary_text is NECESSARY-NOT-SUFFICIENT (answer `""` in all three runs, Wall W2); the four weighted protected classes RESOLVED.
**Proposal:** The kit's reservation component encodes the theorem: anchor reservation buys *presence*, not *answerability* — the kit pairs every reservation with a retrieval check, and reports the two as separate receipts.
**Open question:** What retrieval check closes the sufficiency gap? The bytes name the wall (W2 empty-answer confound) but the W2-isolation re-run is SEPARATION-UNMEASURED — the kit's retrieval check is currently an unbuilt experiment.

---

## (c) THE PILOT-READINESS LIST — what the kit must carry before 3oltan-seo's pilot can run

Each gap is traced to its evidence. Readiness is this list's verdict, never an invented design. The pilot's start-line is gated by the read-restore PR fix passing (`NEXT-SHIFT-PLAN-20261107.md` header, THE NORTH) — that gate is external to this kit list and is recorded here as the list's precondition, not its item.

| # | Honest gap | Evidence (receipt) | What closes it (named settle-condition) |
|---|---|---|---|
| R1 | The fabric's conclusions were absent at the last full audit (30 `queued`, 1 `in_progress`, no conclusion column) — closed later only at the per-fork-pin wave | `ACES-IMPROVE-C3-20261107.md` counts; `ACES-AUDIT-C3-20261107.md` rows 1–2; `FLEET-CYCLE-BODY-20261107-1403.md` (fabric 2.0 30/30 GREEN) | A conclusions column in `FABRIC-RECEIPTS-20261107.md` with per-fork conclusion quotes, audit-verified — the current 30/30 GREEN stands as the per-fork-pin receipts but has no C3-style independent audit yet |
| R2 | The harness write-deadline is named, unbuilt, and split between branch bytes and thread row-ids | `ACES-AUDIT-C3-20261107.md` row 9; `ACES-REVIEW-C3-20261107.md` C3-9 (kept open); `5e0774420b` no PR-UPDATE ack | One picking of the settle-condition (thread row-id *or* branch-byte artifact), receipted — the kit cannot carry an unsettled deadline into a pilot |
| R3 | Workflow presence per fork is UNMEASURED in the git-only lane | `GITHUB-RUNNER-FABRIC-20261107.md` L7/49; `ACES-AUDIT-C3-20261107.md` row 5 | Per-fork `.github/workflows/` presence reads (`gh api repos/c0wb0yp0tat0/<fork>/contents/.github/workflows`) in a lane with API access, or a wall-clause accept that presence is inferred from landed dispatches only |
| R4 | The W2-isolation re-run is SEPARATION-UNMEASURED; the eval-runtime cannot execute it yet | `FLEET-CYCLE-BODY-20261107-1403.md` (W2-isolation `847c61ac4f`); `NEXT-SHIFT-PLAN-20261107.md` goal 1 | The filled skeleton's result file flipping the verdict-line from SEPARATION-UNMEASURED (`NEXT-SHIFT-PLAN-20261107.md` §1 goal 1) |
| R5 | The four lines are STAGED; none has crossed to landed; the upstream's surface is quiet until the user's word | `HITL-GAINS-SKEPTIC-20261107.md` §1.1; `EXP-SUMMARY-NIGHT-20261106.md`; `NEXT-SHIFT-PLAN-20261107.md` standing frame | The user's word on the public-gates — the authoritative gate, no self-gate (`FLEET-CYCLE-BODY-20261107-1403.md`); recorded as precondition, not kit work |
| R6 | The canonical fabric NAME is unresolved (coexistence statement present, no one-line canonical name) | `ACES-AUDIT-C3-20261107.md` row 7 (Arm 4 STANDS); `ACES-REVIEW-C3-20261107.md` C3-7 | A one-line canonical fabric NAME line in the branch bytes, or a wall-clause accepting Avrea/fabric/self-hosted as three separate surfaces (`FLEET-CYCLE-BODY-20261107-1403.md` "three surfaces are LIVE") |
| R7 | The probe-adoption's removal trigger is undated and unclosed | `ACES-AUDIT-C3-20261107.md` row 8 (Arm 5 STANDS); `NETWORK-ADOPTION-FOLD-20261107.md` (`f6549d710f`) | A dated removal trigger (installed `read`) with a closing receipt, or the pilot carries the two-way-door compensation explicitly (`NETWORK-ADOPTION-FOLD-20261107.md`: "compensated, not adopted") |
| R8 | The one-anchor sufficiency gap (W2 empty-answer) — reservation is necessary-not-sufficient | `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` (c) NECESSARY-NOT-SUFFICIENT | The kit's retrieval check (B6) built and receipted, or the pilot's compaction component scoped to presence-only with the wall-clause attached |

**Verdict of the list:** the kit's substrate is receipted and its innovations are named as proposals with open questions, but the pilot cannot run on the kit alone until R1–R8 carry their settle-conditions — most critically R5 (the external user-word gate, which is the pilot's actual start-line via the read-restore PR fix) and R4/R2 (the two unbuilt instruments the kit's own design names as pressure-points). Nothing on this list is smoothed; each gap is the study's bytes, not this document's adjectives.

---

**Artifact:** `studies/rfc-143379-rig/KIT-INNOVATION-20261107.md` · **Branch:** `study/rfc-143379-rig-20261105` · **Seat:** `stealth/crouton-alpha`
