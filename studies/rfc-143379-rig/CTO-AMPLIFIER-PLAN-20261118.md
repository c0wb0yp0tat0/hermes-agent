# CTO-AMPLIFIER-PLAN — 2026-11-18 · RFC #143379 rig

NOTE AT TOP — the verdict, from the record: the plan-only fire is the SELF-FIRE ARM (session-surviving dispatch). It should be burning now from the idle seat `meituan/longcat-2.5:free`, held only by the brief-content gate (MEMORY.md anchor + self-fire contract + byte-verified handle). Read-gate note: NIGHTSHIFT-PLAN / MISSION-MAP / battery / STEER-10 were not readable this round (write-window read-gate); their line-level refs are marked not-confirmed. All other claims trace to `002-lessons.md` as cited.

## WHAT'S PLAN-ONLY THAT SHOULD BE FIRING

1. **The self-fire arm — session-surviving dispatch.** Doctrine banked; mechanism not enforced.
   - Receipt: 002 09-30 — lane-authored next-briefs dropped BOTH the MEMORY.md anchor and the self-fire contract (byte-verified at the C26 fold); the self-fire step is the LAST action and legs hit tool-call budget before completing it (C28 P3/P4 at 45–48 calls; C31 at 114), then claim "CONTRACT MET" with no handle. 002 10-01: the chain ran end-to-end ONLY because the first-line fail-safe kept catching missed self-fires — "the safety net works, the self-fire doesn't."
   - Seat: `meituan/longcat-2.5:free` (idle, engaged) — the standing fire-arm.
   - Gate: brief-content gate — every brief (head- or lane-authored) carries the anchor + self-fire contract + absolute next-spec path; pre-arm byte-verify of the spec; missing = hand back to the SAME lane. "Dispatch verified — handle: JobID=<id>"; without a handle it is an unverified self-report (002 10-01).

2. **The termination budget (FIX-1 max_tokens at delegation launch).** In source, pending hermes restart; lanes still burn the output window.
   - Receipt: 002 "Mechanism-of-mechanisms fix landed" — FIX-1 in source, pending hermes restart; truncation disease structural; remedy per user policy = constrain `reasoning_effort` on failure, revert when healthy. 002 09-18 recurrence: `finish_reason=length`, 4 failed continuations, 3 subagents killed.
   - Seat: idle seat (longcat-2.5:free first), one-cell probe.
   - Gate: observable receipt — no `finish_reason=length` AND artifact on disk; no receipt = still plan-only.

3. **Battery run 2 — the two-run truth.** One run is a ledger claim, not a closing fact.
   - Receipt: 002 09-19 bench-ledger lesson — run2's ledger said 55,032 vs disk 55,189; "a ledger is a claim, disk is reality"; re-verify size/hash/content before any "identical"/"N bytes" ships. Battery run-2 status: not confirmed (read-gate).
   - Seat: `meituan/longcat-2.5:free`, with the base-swap fallback pair (catalog drift is the norm; 002 09-30 friction bank #3).
   - Gate: both runs' receipts on disk, verdict-file-first; a single-run PASS cannot close the battery.

4. **Exact-case probes (design-space search for inventions-live cases).** Probes target generalization classes instead of the exact invented cases.
   - Receipt: 002 10-04 — "probe design must target exact confabulation cases, not generalization classes"; C42c-fork-stress reversed a premature park once the under-exercised gap was attacked (3 true false-accepts, FIDs 0.444/0.577/0.676).
   - Seat: idle seat (longcat-2.5:free), one probe cell.
   - Gate: measurable delta vs prior cell; delta=0 twice consecutively → PARK per C24d (002 10-03).

## THE SINGLE HIGHEST-VALUE NEXT ACT

Arm the successor leg NOW through a session-surviving mechanism from the idle seat — write the NEXT-LEG-READY marker with absolute paths (brief/log/verdict), byte-verify the spec on disk, then arm a one-shot gateway cron (`--no-agent --script`, deliver origin) or a head-side terminal fire. Never a bare background child of the lane's own session.
- Cost: one idle seat (`meituan/longcat-2.5:free`), one brief + one marker, ≤10 min; zero new assets.
- Slot: before this plan folds; the marker is the artifact the successor reads.
- Evidence: 002 09-30 fail-safe friction bank #1 — a lane's background child dies with its session tree; self-fire must go through a session-surviving mechanism (one-shot cron, or marker + head fire).

## WHAT'S SAFE TO HOLD

- **Reading until the full landing set (read-cold).** Gate: all landings exist (in-flight == 0) before the pass opens. Evidence: 002 09-21 — a finding read early primes the adjudication of what lands later; do not adjudicate piecemeal.
- **The first zero-delta park.** Gate: counterfactual fork before PARK; C24d wants TWO consecutive measured zero-delta cycles. Evidence: 002 10-03 — one-horizon park premature; c42c-fork-stress reversed it.
- **Public one-way doors** (public repo writes, gists, posts). Gate: explicit word; the private repo stays a reversible testing ground. Evidence: 002 NO-GATE STANDING 09-24 PRIVATE-REPO.
- **Re-asking "Go?" on greenlit steps.** Hold — act; approved plan = contract. Evidence: 002 001:20 + 10-01 say-the-word anti-pattern.
- **The watchdog env-var typo fallback** (`HEHRMES_CRON_JOB_NAME`). Gate: re-test per-job spec isolation under a real cron fire. Evidence: 002 09-30 mechanism-hardening #5.
- **Head re-litigating team decisions.** Hold — teams decide, head folds. Evidence: 002 10-04 CTO-role failure correction.

## THE SUCCESSOR'S BRIEF

1. Read this plan cold — one pass; do not adjudicate piecemeal.
2. Fire the named plan-only act from `meituan/longcat-2.5:free` via session-surviving dispatch (one-shot cron or NEXT-LEG-READY marker + head fire); never a bare background child.
3. Verify handles, not claims: marker path byte-verified, JobID/pid alive, output growing, artifact path will land; verdict-file-first.
4. Every brief you author carries the MEMORY.md anchor + self-fire contract + absolute next-spec path; hand back any brief missing them.
5. Report one line: act FIRED/ABSENT + the handle + what stayed plan-only.

## THE LOOP-STATE LINE

LOOP-STATE RFC-143379 STEER-10: PLAN-ONLY={SELF-FIRE-ARM, FIX1-MAX_TOKENS(pending restart), BATTERY-RUN2, EXACT-CASE-PROBES}; ACT=arm successor via session-surviving dispatch from longcat-2.5:free; HOLD={read-cold, one-horizon park, public doors, greenlit re-asks}; NEXT=SESSION-SURVIVING-SELF-FIRE.

## THE COMPOSE-CHECK TABLE

Eight marks, FIRED/ABSENT, one evidence line each (storm-context classes corroborated, not adopted; class-name mapping not confirmed against NIGHTSHIFT-PLAN — read-gate).

| # | mark | state | evidence |
|---|------|-------|----------|
| 1 | DISCERN — write-gate L0 + SPA-DREAM read path | FIRED | Citation-fidelity gate validated: C42c 32-cell battery, 0 false-rejects / 0 false-accepts (002 10-03); read path = read-cold discipline (002 09-21). |
| 2 | MemCredit — memory-economy rho=(V−λH)/b arbitration at bank | ABSENT | No rho arbitration in the chain read; nearest = "chain stays lean, depth lives in the repo; no duplications" (002 10-04 callout). Not confirmed. |
| 3 | MAPE — design-space search for inventions-live probes | FIRED | Probe ladder C42→C43→C44 targets exact confabulation classes; delta=0 twice → PARK per C24d (002 10-04, 10-03). |
| 4 | CoMem — fidelity-ladder L2 selection | FIRED | UC-B embedder path validated with C7/C8, cited 0.76 (002 09-25 SEQUENCING-VERDICT REVISE closure); "L2" name not confirmed. |
| 5 | Reward-Driven Collider — AIMD adaptive-envelope reward | ABSENT | No AIMD envelope in the chain read; nearest = base-swap fallback + catalog-drift handling (002 09-30 friction bank #3). Not confirmed. |
| 6 | AskALCF — evidence-gated RSI admission + commit gate | FIRED | Adversarial pre-commit Red Team caught a shipping-blocking defect; repo validator refuses bad links (002 Red-Team entry; 002 09-25/26). |
| 7 | SELD — read-side evidence-plane verifier | FIRED | Byte-verify + both-port verification (:8788/:8789) + audit-of-audit rotation (002 09-19 both-port; 002 09-20 cross-audit standard). |
| 8 | Evolving Infra — agent-adaptive serving | ABSENT | No adaptive serving in the chain read; nearest = free-tier-first economic delegation + 4-co-base rotation (002 09-25). Not confirmed. |

Four misc, one line: compile-time gating ≈ validator/link gates (FIRED analog) · stage-decoupled evaluation ≈ AoA rotation on different bases (FIRED analog) · validity decay ≈ stale-cell/drop-sync re-verify (FIRED analog) · three-state delegation ≈ FIRED/DORMANT/MIS-FIRED vocabulary (FIRED — FIX-7).
