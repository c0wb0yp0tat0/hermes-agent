# SPRINT-PLAN-20261108 — the 3-hour loop-sprint's launch-brief (the standby's fire, 2026-11-08)

**Seat:** reflection/beam-1.0-501b-a23b:free (apex-role — the plan is the apex role).
**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public without the operator's word).
**Date:** 2026-11-08. **Lane:** copycat (RFC #143379 apex mission).
**Gate (verbatim, non-negotiable):** "the gate: nothing public without the user's word" — fork-only, no thread posts, upstream quiet, proposals-only-after.
**Mission state ground:** READY-WITH-NAMED-SEAMS (WAVE3-UNIFIED-FOLD-20261108); six tracks live (1, A, C, D, R1, R2); four gates HOLDING; thread tail 282 rows (FLEET-CYCLE-BODY-20261108-053342); six landed commits on the branch (7b974b95ea, 0658b616e1, 7b4678e729, b40534b55a, a04a7af6e7, c544d3ad55).

**Operator's window:** intense, ~3 hours, as many loops as fit; then the cats' long-form HITL report (medium-article length) served via gist to chat. Nothing public without the operator's word.

---

## 0. THE STANDING FRAME (binding — carried, not re-litigated)

- Four lines STAGED: restore #141876 · network #116673 · governance #139606 · compaction #140008.
- TRUTH-FINISH-LINE honest ("FAIL today" until the word).
- Fleet FREE-ONLY; re-apex standing — every apex-role on `reflection/beam-1.0-501b-a23b:free`.
- Pilot start-line = the read-restore PR's pass (#141876) — not the upstream landings, not shipping the kit as-is (THE NORTH, binding).
- The landed items are NOT re-seeded: T-A the rebase, T-B the fabric, T-F the scripts have landed; the seeds below come only from the remainder (opportunities / missed / standby / improvements).

---

## 1. THE SEEDS — each loop-cycle's seed, named from the remainder

Each seed's chain shape is the three sub-passes **improve → audit → review**. A seed without its success signal is a wish; every seed below carries one. Landed items (T-A rebase, T-B fabric, T-F scripts) are excluded.

The 6 primary seeds (guaranteed in the 3-hour window) + 3 stretch seeds (fire only if a primary cycle closes early). Overflow queue parked for a later window.

### Primary seeds (cycles 1–6)

| Cycle | Seed (source) | Improve (sub-pass) | Audit (sub-pass) | Review (sub-pass, apex/flagship) | Success signal (receipt) |
|---|---|---|---|---|---|
| 1 | **S1 — Provenance defaults to "unknown" at pipeline definition** (RFC opp 11; IMPROVEMENTS-W1 #1) | Add the one-line invariant + test in the governed-compaction path. | Byte-verify the invariant present; run the test; confirm zero new failures. | Review-pass confirms no regression + seam closed. | Invariant landed + test green + review row on the branch. |
| 2 | **S2 — `_augment_summary_lean` one-generation anchor decay fix** (RFC opp 1; IMPROVEMENTS-W1 #2) | Carry the anchor forward more than one generation in-tree. | Before/after measurement on the same task set; quote both numbers. | Review-pass judges the delta against the bar. | Measured before/after receipt on the branch (anchor survival rate). |
| 3 | **S3 — Fix the probe scope bug, re-run the 300-cycle sweep** (RFC opp 4; IMPROVEMENTS-W1 #3) | Fix the scope bug confounding the −3.5pp headline. | Re-run the 300-cycle sweep; certify or refute the 6.1% vs 9.6% reading. | Review-pass records the certification verdict. | Sweep receipt + headline certified/refuted on the branch. |
| 4 | **S4 — Chunked/batched writes + dry-run in the copycat-harness write-gate** (MACH opp 2; IMPROVEMENTS-W1 #4) | Expose the chunked-write knob + dry-run mode for over-budget writes (refuse-without-write). | Over-budget write returns dry-run refusal with no write; in-budget write lands. | Review-pass confirms the gate contract holds. | Knob present + dry-run receipt on the branch. |
| 5 | **S5 — Scratch-prune artifact allowlist / protected paths** (MACH opp 12; IMPROVEMENTS-W1 #5) | Add protected paths to the prune config. | Prune leaves protected artifacts in place; non-protected pruned. | Review-pass confirms no in-progress work lost. | Allowlist receipt on the branch. |
| 6 | **S6 — Hour-8 operator-chair handoff named receiver** (MISSED #1) | Name the operator's chair as receiver in the fold's thread row. | Row present with receiver named; no staged proposal lacks a receiver. | Review-pass confirms the receiver clause holds. | Receiver-named row receipt on the branch. |

### Stretch seeds (cycles 7–9, fire only if a primary cycle closes early)

| Cycle | Seed (source) | Improve / Audit / Review | Success signal |
|---|---|---|---|
| 7 | **S7 — People-facing surfaces (comms read-gate-to-people)** (MISSED #2) | Assign a comms surface; draft a read-gate-to-people note; audit the surface named + note staged; review. | Comms surface + staged note receipt. |
| 8 | **S8 — 'Assumed done' baseline snapshot at t=0** (MISSED #3) | Baseline snapshot rows for kit smoke-green + machinery standing; audit rows present; review. | Baseline snapshot receipt. |
| 9 | **S9 — Silent-failure liveness probe between fold-points** (MISSED #4) | Define the liveness probe; audit it fires between folds; review. | Liveness probe receipt. |

### Overflow queue (parked — fires only if all 9 cycles close with time to spare, else next window)

- S10 — Launch pre-flight checklist + on-call at 23:59:50 (MISSED #5).
- S11 — K-recency scaling sweep: window size as f(session length) N/2N/4N (RFC opp 9).
- S12 — Seam-contract test suite pinning the four gaps independently (RFC opp 2).
- S13 — Author the governed-compaction issue (provenance-origin + archive-before-stub + K-recency hard window) (RFC opp 6).
- S14 — 3oltan-seo occupancy probe against the real director profile (RFC opp 5).
- S15 — Credibly-scoped accounting note for jfugalde's 106-commit/6,275-line attribution (RFC opp 7).
- S16 — Supply the missing second level for ZacharyThomasStone's three-level comparison (RFC opp 8).
- S17 — Cron-surface audit lane (idle/stale, dedup, retry caps) (MACH opp 1).
- S18 — Fork-status sweep (drift > N commits / stale PRs, auto-label) (MACH opp 3).
- S19 — Mine-class registry with per-class detector + suggested lane (MACH opp 4).
- S20 — Stale-entry reaper (re-validate staged entries before write) (MACH opp 6).
- S21 — Model-availability probe + fallback chain (MACH opp 7).
- S22 — Transport health-check with IPv4 fallback (MACH opp 8).
- S23 — Host-storage recovery lane wired into gateway exit diag (MACH opp 9).
- S24 — Trace-export backoff + queue with drop-on-overflow (MACH opp 10).
- S25 — Managed-worker sync-rpc moved off the event loop (MACH opp 11).
- S26 — Scratch-prune protected paths (already S5) — skip.
- S27 — ACES-AUDIT-C2 re-run (STANDBY fallback-wave #1).
- S28 — ACES-IMPROVE deepening (STANDBY fallback-wave #2).
- S29 — Memory-chain append (STANDBY fallback-wave #3).
- S30 — Living-home update (STANDBY fallback-wave #4).
- S31 — Skill authoring pass (STANDBY fallback-wave #5).
- S32 — Gateway-restart pending + ENOSPC host-storage recovery (IMPROVEMENTS-1 overlooked needs #6/#7) — fold into S4/S10 as needed.

**Rule:** a seed that cannot state its success signal does not fire; it parks.

---

## 2. THE CADENCE — cycles' order + seats' rotation + how many cycles fit

### Cycle order
Reserve-sharpening first (S1–S5, highest value-to-spend, lowest dependency), then the missed-edges (S6–S9, closing the hour-8 handoff gaps before the HITL), then overflow. Substrate before surfaces before amplifier (IMPROVEMENTS-1 #c): composed-state-facing seeds first, machinery last.

### Seats' rotation (five-model rotation)
The five seats, in rotation order:
1. **M1 — `reflection/beam-1.0-501b-a23b:free`** (the flagship; apex-role).
2. **M2 — `meituan/longcat-2.5:free`**.
3. **M3 — `stealth/crouton-alpha`**.
4. **M4 — `upstage/solar-mini4:free`**.
5. **M5 — `stepfun/step-3.7-flash:free`** (retires on its 429/401/401 triple → fall back to M1).

**Resting-seat rule:** after a model runs a cycle's three sub-passes, it rests the next cycle; the next model in rotation takes the next cycle. Cycle n's lead seat = model ((n−1) mod 5)+1, skipping any retired/unavailable model and falling back to M1. The **review sub-pass of every cycle runs on M1 (the flagship)** regardless of the lead seat, per the re-apex standing (every apex-role rides the flagship). No single point of failure: a dead seat is skipped, never blocks the cycle.

### How many cycles the 3-hour window fits
- **6 primary cycles guaranteed** (S1–S6), at ~30 min each (improve 12 + audit 10 + review 8).
- **Up to 9 cycles (S1–S9)** if sub-passes run lean (~20 min each).
- Overflow queue parks; nothing is force-fired past the boundary.

### Silence-when-healthy
A healthy cycle reports only at its review sub-pass; a silently-dead cycle is caught by the liveness probe (S9) once it lands, and by the fold-point receipts otherwise.

---

## 3. THE BOUNDARY — the window's edge and what happens at it

- **Edge:** ~3 hours from sprint start (intense loop-sprint). At the edge the sprint stops firing new cycles.
- **In-flight cycle:** completes its current sub-pass, then finishes the review sub-pass if within 5 minutes of the edge; otherwise parks mid-cycle with a `PARKED-AT-<subpass>` receipt and the partial work staged for the next window.
- **Seeds remaining** (primary not closed, stretch not fired, overflow) go to the overflow queue with their partial receipts; they are NOT dropped, NOT re-invented next window.
- **At the edge the HITL's authors gather** (§4) to write the long-form report. No new sprint work starts after the gather.
- **Gates hold throughout and at the edge:** fork-only, nothing public without the operator's word, upstream quiet, proposals-only-after. No thread posts, no upstream writes, no public surface touched by the sprint or the HITL.

---

## 4. THE HITL'S SLOT — the long-form's brief-seed (medium-article length, served via gist to chat)

The HITL long-form is authored at the boundary by the cats (the team). Its brief-seed, so the authors gather with a shared starting point:

**(a) The nightshift's progress narrative.** What landed, receipted: the five lenses (STATE/ARC/READINESS/ESSENCE/OUTCOME) composed on all five; the swap's seven-track plan (T-A rebase, T-B fabric, T-F scripts landed; T-C/D/E/G owed); the composed state's falsification (seam-gaps 1–4, conflict register, rebase-class adjudication, receipt ledger); the wave-3 fold (READY-WITH-NAMED-SEAMS, seam-register S1–S8); the receipt ledger's rows; six landed commits; three launch rows on PR #1 (6717495001 / 6717609640 / 6717613103); four gates holding; machinery on 15m sweep + fleet cycle; six operator-reviews pending. The krecency drift-registers (demand-age FAIL ≥300; K-scaling NO; constraint pinning 0 violations vs recency-truncate worst; aliasing×proximity CONFIRMED-BOTH R²=0.655; archive FAIL→REFUTED). The probe-banks CLEAN (A1–A11, B1–B8).

**(b) The team's opinions on the direction.** The composed-state falsification sits at the center, not the landings; the read-restore PR's pass is the pilot's start-line (not shipping the kit as-is); the kit is innovated-first (never an as-is kit; the kvnloo lab builds theirs independently); the fleet is free-only with the re-apex flagship; the improver loop converged twice with no improvement honestly proved (the hold is the honest terminal); the acceptance scripts are an hour-one build task, not a launch precondition; nothing ships that does not serve the needs or the composition track. The reserve's five (provenance default, anchor decay, probe scope, chunked writes, prune allowlist) are the highest value-to-spend; the missed five (operator-chair, people-facing surfaces, assumed-done baselines, silent-failure classes, launch pre-flight) are real edges, not cosmetic.

**(c) The perspective on the project as a whole.** A private proving ground: it decides by measurement rather than argument whether three proposed fixes for the agent memory system are safe enough to recommend, and writes nothing to any public surface. The read-restore repairs a race (paused read resurrecting stale state); the network and governance fixes are carried as named seams (no dedicated track, no assigned owner yet); the hardest measurement is negative (hard recency window fails its own gate at 300+ cycles); where the memory proposal survives it survives by pinning; the verdict is ready-with-named-seams; every delta is staged at homebase for approval; nothing proposed anywhere public. The essence is a one-time cure for overload, never a standing briefing.

**Delivery:** the long-form is served via a gist to the chat, medium-article length, authored by the cats at the boundary. Nothing public without the operator's word — the gist is the operator's to post.

---

## 5. Compose-check table

| # | Step | Status | One line |
|---|---|---|---|
| 1 | Read the ledger/standby/harvests end-to-end (summaries carried) | FIRED | The five lenses, SWAP-PLAN, TRACK1 falsification + rebase, WAVE3 fold, receipt ledger, standby/opportunities/missed, negentropy sweeps, fleet-cycle body, improvements, and ACES review were carried as summaries; landed items excluded from re-seeding. |
| 2 | Distill, never inventory | FIRED | Thirty-one candidate seeds distilled to nine firing cycles plus a parked overflow queue; the full remainder stays in its source files. |
| 3 | Speakable coherence | FIRED | Each seed names its source, its three sub-passes, and its success signal, so the plan holds together when read aloud. |
| 4 | Receipts where weight demands | FIRED | Every success signal cites a receiptable artifact or measurement; the 300-cycle sweep and the before/after anchor measurement carry their measured receipts. |
| 5 | Gate honored | FIRED | The artifact lands on the study branch only; no thread posts, no upstream writes, no public surface touched. |
| 6 | Fork-only landing | FIRED | The file is committed to the study branch and pushed there, with no thread post made. |
| 7 | One-time, not standing | FIRED | The sprint plan is a single launch-brief for this 3-hour window, not a standing mechanism that re-briefs. |
| 8 | Compose-check itself | FIRED | This table is the last section, with its eight steps marked fired or absent, each in one line. |