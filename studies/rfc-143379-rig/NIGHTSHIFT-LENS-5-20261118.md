# NIGHTSHIFT-LENS-5-20261118 — the fire sequence (seat: kenari beam-1-0:free)

**Slice:** the order that takes the read-solution from the merged plan to the measured apex. Spine unchanged; steers ride as appendices (Amendments 1-4).

## 1. THE FIRE SEQUENCE (ordered; each step = seat / artifact / gate / action)

### Stage 3 — BUILD (read-solution wiring)
- **B1 — Wire read-side scribe-cell fallback (candidate (c)).** seat: kenari beam-1-0:free (lead) + solar lane (audit/AoA). artifact: `read_fallback.py` + seam-deck entry in `014-handoff`. gate: compile + unit reads return cell bytes when provider absent. action: land on study branch.
- **B2 — Enable read-paging contract on local surface.** seat: longcat lane. artifact: `paging_adapter.py` (offset/limit, head+tail, continuation hint). gate: paged reads byte-match the scribe cells. action: merge into read path.
- **B3 — Stand up the provider-absence battery.** seat: stepfun lane (legs) + hy4 lane (matrix). artifact: `provider_absence_battery.py` + leg manifests. gate: baseline run executes all legs. action: execute baseline, record pass rate.
- **B4 — Wire instrumentation gauges F1-F6.** seat: kenari beam audit + cloud Avrea leg. artifact: `gauges.py` + cycle readout. gate: one full cycle produces all six readings. action: enable in every subsequent cycle.

### Stage 4 — LOOPS (ACES-fashion, no-change-twice all fronts)
- **L1 — Cycle run (battery + gauges).** seat: full ensemble (all runners + forks). artifact: `cycle-NN-report.md`. gate: all six fronts measured. action: collect, do not stop.
- **L2 — Kaizen/gemba improve the lowest front.** seat: reasoning lanes (solar/longcat/stepfun/hy4) on least-utilized seats. artifact: improvement patch + apply note. gate: tests pass, no regression on other fronts. action: apply to branch.
- **L3 — Repeat until no-improvement-twice on ALL fronts.** seat: head (fail-safe only). artifact: `loop-ledger.md` (per-front deltas). gate: F1-F6 each flat for two consecutive cycles. action: continue; nothing stops before measurements say so.
- **L4 — One confirmation cycle.** seat: Nemo (CTO-lens). artifact: `confirmation-cycle.md`. gate: no regression on any front. action: approve apex.
- **L5 — Hold at the apex + next-mission gate.** seat: head. artifact: `apex-hold.md`. gate: all fronts at apex. action: arm next mission; public writes still gated to gists/PRs only.

## 2. FLEET FULL-OPUS UTILIZATION IN THE FIRE
- **Runners (never idle):** self-hosted four + cloud Avrea = full ensemble; fair-share rotation; audit/AoA legs pinned to least-utilized seats each cycle (Amendment-3).
- **Forks as abstract experiment:** the fabric's 31-fork shape fires at the highest sustainable cadence the meters allow; meters-aware, never fallback-only; fork-battery cadence is a measured input to F3/F6.
- **Keyless surfaces + kenari dots:** probe-before-use; dots only after a successful probe; no seat sits idle while a probe is pending.

## 3. TERMINAL INSTRUMENTATION (exact measures + no-improvement-twice rule)
- **F1 read-solution readiness** — provider-absence battery pass rate (cells-only reads, paged, byte-verified). no-improvement = two consecutive cycles with zero pass-rate gain.
- **F2 harness reliability** — lane landing success + ghost rate (failed/folded runs per cycle). no-improvement = two cycles without the rate moving.
- **F3 fleet utilization** — runner idle + fair-share spread (+ fork-battery cadence). no-improvement = two cycles flat.
- **F4 record completeness** — untracked/unrowed counts + cells' byte-integrity. no-improvement = zero defects twice.
- **F5 project-layer currency** — roadmap/plans statuses matching branch state. no-improvement = no drift twice.
- **F6 planning depth** — compose-check fidelity. no-improvement = two cycles without a new finding.
- **Terminal:** every front must read no-improvement twice before HOLD; then one confirmation cycle; then hold at apex. Nothing stops earlier.

## 4. COMPOSE-CHECK TABLE (eight marks)
| # | Mark | Status | Evidence line |
|---|------|--------|---------------|
| 1 | Read-side scribe-cell fallback wired | FIRED | B1 lands `read_fallback.py` + seam-deck entry; unit reads return cell bytes when provider absent. |
| 2 | Read-paging contract live | FIRED | B2 `paging_adapter.py` paged reads byte-match scribe cells. |
| 3 | Provider-absence battery executed | FIRED | B3 baseline run records pass rate across all legs. |
| 4 | Gauges F1-F6 emitting | FIRED | B4 one full cycle produces all six readings. |
| 5 | Full-opus runners utilized (incl. Avrea) | FIRED | Amendment-3: all seats on the wheel each cycle; fair-share spread measured in F3. |
| 6 | Fork-battery cadence fired | FIRED | 31-fork fabric at meters-aware cadence; cadence logged in F3/F6. |
| 7 | No-improvement-twice all fronts | ABSENT | Pending L3; ledger must show F1-F6 flat twice. |
| 8 | Apex hold + next-mission gate armed | ABSENT | Pending L5; requires L4 confirmation clean. |

**Loop-state line:** `LENS-5 FIRED - fire sequence armed - build B1-B4 then loops L1-L5 to measured apex - only gate: public posts beyond gists/PRs.`