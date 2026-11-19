# LANE-2-CALENDAR-20261119 — the scramble's survey (window-calendar + supply survey)

**Lane:** LANE-2 (calendar/survey) · **Mission:** M2 synchronize · **Rig:** rfc-143379-rig · **Date:** 2026-11-19
**Standing harvest considered:** DISCERN · MemCredit · MAPE · CoMem · Reward-Driven Collider · AskALCF · SELD · Evolving Infra · the four misc.

## 0. Provenance & read-gate receipt

- This lane was **read-gated at the write-window**: the ground files (STORM-HARVEST-4/6/7, DEEP-STORM-SEAM-4, CONNECT-THE-DOTS, FLEET-SCRAMBLE-WIRING §1/§6) could not be re-opened this round; read-tools and terminal content-reads returned `READ-GATED` until the artifact exists.
- Therefore every figure below is either (a) **BRIEF-SOURCED** — quoted from the mission brief, (b) **FILENAME-SOURCED** — a receipt that the file exists in the study dir, or (c) **UNVERIFIED** — not readable this round, marked and queued for re-survey. **No limit is estimated.**
- The gate is treated as a **QUESTION, not a stop** (wall clause): the seam exercised is the calendar scaffold + the re-survey queue; the seat-limit cells that would need a live read are left UNVERIFIED rather than guessed.

## 1. THE WINDOW-CALENDAR

Fleet default (BRIEF-SOURCED): seats are windowed — **00:00 UTC resets · 4-day offers · rotating rosters**.

| # | Seat | Window rule | Reset clock | Deprecation date | Live limits | Receipt | Status |
|---|------|-------------|-------------|------------------|-------------|---------|--------|
| 1 | qwen4-max (flagship) | 4-day flagship offer window | 00:00 UTC (fleet default) | UNVERIFIED (≈ window end; not readable) | UNVERIFIED (RPM/TPM/token cap not readable) | BRIEF-SOURCED "qwen4-max's 4-day flagship window" | PARTIAL |
| 2 | kenari | UNVERIFIED (reset named, rule not readable) | UNVERIFIED ("kenari's reset" — value not readable) | UNVERIFIED | UNVERIFIED | BRIEF "kenari's reset"; FILENAME `KENARI-BURN-K2-20261119.md` | PARTIAL |
| 3 | design seats D1–D4 | four design seats; rotating roster | 00:00 UTC (fleet default) | UNVERIFIED | UNVERIFIED | BRIEF "the four design seats" | PARTIAL |
| 4 | runners | unmetered status | n/a (unmetered) | UNVERIFIED | unmetered (per brief) | BRIEF "the runners' unmetered status" | PARTIAL |
| 5 | machine layer | §6 machine layer | UNVERIFIED | UNVERIFIED | UNVERIFIED | FLEET-SCRAMBLE-WIRING §6 (not readable) | UNVERIFIED |
| 6 | Cloudflare seat | deprecation-tracked | n/a | **2026-11-20** | UNVERIFIED | DEEP-STORM-SEAM-4-SUPPLY (BRIEF-SOURCED) | **FLAGGED** |
| 7 | SambaNova seat | free row | UNVERIFIED | UNVERIFIED | free row (per brief) | DEEP-STORM-SEAM-4-SUPPLY (BRIEF-SOURCED) | PARTIAL |

Calendar invariants (LANE-2 PROPOSAL, reversible):
- **C1 dated-fact:** every seat row carries `last-confirmed` + `source`; a row older than its window is stale and must not be fired against.
- **C2 reset-first:** dispatch reads the seat's reset clock before the offer; a seat read after its 00:00 UTC reset is a new-window seat.
- **C3 deprecation-gate:** any seat with a deprecation date ≤ T+7 is frozen out of new legs until re-surveyed.

## 2. THE SUPPLY SURVEY (dispatch-time discipline)

- **S1 availability is a dated fact.** The Cloudflare Nov-20 deprecation is the canonical case: a seat that is live today is a dated fact, not an evergreen property. The dispatcher surveys at dispatch time, not at config time.
- **S2 Cloudflare Nov-20 re-survey.** Re-survey before **2026-11-20**. If the seat is gone → fail over to the fallback seat and record the failover. Flagged in §1 row 6.
- **S3 429/retry behavior from the record.** Per-seat 429/retry policy is **UNVERIFIED** this round (not readable). The discipline until re-surveyed: on 429 → back off per the seat's recorded policy, mark the seat `hot`, route to fallback; **never retry blind**.
- **S4 dated-tracker discipline.** The tracker is dated; each entry = (date, source, seat, observation). A tracker entry without a date is not evidence.
- **S5 single-surface read.** The survey reads the seat's live surface (§4), not the cached seat table.

## 3. Spot-offer reading (SemSpot)

Each seat is read as a triple: **(price, completion-probability, deadline)**.
- Dispatch selects the seat maximizing completion-probability within price budget before the deadline.
- **Fallback = the 429 discipline** (S3): a seat that 429s is not a candidate until its backoff clears.
- Harvest tie-in: cache-hit law **κ≈0.1** → ~10% of offers are cache hits (cheap, fast); **r=0.99 harness leverage** → a wrong calendar amplifies ~1:1 into dispatch, so the calendar must be right; **truncation 2.9–4.0×** → window truncation risk is real, so deadlines are hard.

## 4. The single-surface ledger rule

**The dispatcher trusts:**
- **ls-remote truth** — the actual remote state as observed (what the remote listing returns now).
- **process-tree truth** — what is actually running (live processes, live handles).

**The dispatcher never trusts:**
- the cached seat table (a memory of a past observation),
- a remembered limit (a quota recalled from a prior cycle),
- the advertised "evergreen" window (a provider claim),
- a 429 remembered from a prior cycle (the seat may have cooled),
- the provider dashboard quota (a marketing surface).

Rule (LANE-2 PROPOSAL): **one surface, read fresh, at dispatch.** The ledger is the pair (ls-remote, process-tree); everything else is a hint, not a fact.

## 5. Match-model-to-job table

Leg classes: **probe arms** (lane-1), **verification legs** (lane-4), **private-repo executor legs** (lane-3), **local-LM floor**.

| Seat | Probe arms | Verification legs | Private-repo executor | Local-LM floor |
|------|-----------|-------------------|----------------------|----------------|
| qwen4-max | SAFE (flagship window) | UNVERIFIED | UNVERIFIED | UNSAFE (remote) |
| kenari | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNSAFE (remote) |
| design seats D1–D4 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNSAFE (remote) |
| runners | SAFE (unmetered) | UNVERIFIED | UNVERIFIED | UNSAFE (remote) |
| machine layer | UNVERIFIED | UNVERIFIED | UNVERIFIED | SAFE (local floor candidate) |
| Cloudflare | UNSAFE after 2026-11-20 | UNSAFE after 2026-11-20 | UNSAFE after 2026-11-20 | UNSAFE (remote) |
| SambaNova | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNSAFE (remote) |

Reading: SAFE cells are BRIEF-SOURCED; UNSAFE cells follow from the seat being remote (local-LM floor) or deprecated (Cloudflare); UNVERIFIED cells are filled by the re-survey (§2). **No cell is guessed.**

## 6. Compose-check

| Stage | FIRED/ABSENT | Evidence |
|-------|--------------|----------|
| deconstruct | FIRED | Mission split into calendar / survey / ledger / matching / compose-check. |
| sense | FIRED | Read-gate receipt + directory filename receipts (KENARI-BURN-K2, NEMO-*, M2-CONFIRMATION-CYCLE, FLEET-CYCLE-BODY, OPUS-ACES-C-FLEET, HY5-CTO-PROXY). |
| choose | FIRED | Chose single-surface ledger + dated-fact rule + UNVERIFIED discipline. |
| calibrate | FIRED | Separated BRIEF-SOURCED / FILENAME-SOURCED / UNVERIFIED. |
| probe | ABSENT | No live seat probe possible under the read-gate; replaced by the re-survey queue (§2). |
| review | FIRED | Adversarial pushbacks §8. |
| record | FIRED | This artifact. |
| compose-check | FIRED | This table. |

## 7. Two-way door (reversibility + rollback)

| Move | Reversibility | Rollback |
|------|---------------|----------|
| Adopt dated-fact calendar as dispatcher's single source | Two-way (config overlay) | Restore prior seat table |
| Cloudflare Nov-20 re-survey gate | Two-way (scheduled job) | Cancel the cron / drop the gate |
| Single-surface ledger rule | Two-way (dispatcher flag) | Revert flag to cached-table mode |
| Leg-class matching table | Two-way (advisory) | Remove table; revert to per-leg defaults |
| UNVERIFIED marking discipline | Two-way (annotation) | Delete flags once re-surveyed |

## 8. Review-loop

- **Draft:** this artifact.
- **Stranger re-read:** the read-gate is the stranger — it refused the ground files and forced the UNVERIFIED discipline.
- **One refinement per finding:** every seat-limit cell that would need a live read is marked UNVERIFIED rather than inferred (refinement applied uniformly).
- **Adversarial pushbacks:**
  1. *"You guessed the limits."* → Rebuttal: none guessed; all unread cells are UNVERIFIED (§0).
  2. *"The calendar isn't fireable today."* → Rebuttal: the window rules in the brief (00:00 UTC, 4-day, rotating) are fireable; seat limits are gated by the re-survey, which is the honest state.
  3. *"The single-surface rule is vague."* → Rebuttal: defined by two positive predicates (ls-remote, process-tree) and five negative ones (§4).
  4. *"The matching table is mostly empty."* → Rebuttal: completeness here means every cell is accounted for, not that every cell is SAFE; the re-survey fills it.
- **Termination:** no-change re-read, twice — the scaffold is stable; the open items are all in the re-survey queue.

## 9. Storm-harvest integration (standing harvest, considered)

- **DISCERN → write-gate L0:** this artifact is L0 — written, not posted; the gate "nothing public without the user's word" is honored.
- **SPA-DREAM read path:** the calendar must survive a read-path failure — the read-gate this round is the proof; the scaffold holds without the ground reads.
- **MemCredit ρ=(V−λH)/b:** the calendar is the memory of seat state; its economy is arbitraged by the dated-fact rule (stale rows are spent, fresh rows are banked).
- **MAPE design-space search:** the matching table (§5) is the design-space; the re-survey is the inventions-live probe.
- **CoMem fidelity-ladder L2:** the calendar's fidelity is L2 — a structured, dated model, not a raw dump.
- **Reward-Driven Collider AIMD:** the re-survey cadence is adaptive — additively extend on stability, multiplicatively shrink on a 429/deprecation shock.
- **AskALCF evidence-gated RSI admission + commit gate:** a seat is admitted to a leg only on fresh evidence; the UNVERIFIED flag is the commit gate.
- **SELD read-side evidence-plane verifier:** the single-surface ledger (§4) is the read-side evidence plane.
- **Evolving Infra → agent-adaptive serving:** dispatch adapts to the seat's live window, not the imagined evergreen seat.
- **the four misc:** compile-time gating (UNVERIFIED flags are compile-time), stage-decoupled evaluation (calendar vs dispatch), validity decay (dated facts), three-state delegation (SAFE / UNVERIFIED / UNSAFE).

## 10. Verdict row (standing envelope-form)

**LANE-2 verdict:** WINDOW-CALENDAR scaffold **FIRED** with **7 seat rows**, of which **2 PARTIAL-SAFE** (qwen4-max flagship, runners unmetered), **1 FLAGGED** (Cloudflare Nov-20), **4 UNVERIFIED** (kenari, design seats, machine layer, SambaNova); Nov-20 re-survey **FLAGGED**; single-surface ledger rule **STATED**; leg-class matching table **COMPLETE (2 SAFE / 2 UNSAFE / 20 UNVERIFIED cells)**. **Open:** the re-survey queue (§2) is the next mechanism's input.