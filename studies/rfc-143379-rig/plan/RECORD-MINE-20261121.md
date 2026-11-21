# RECORD-MINE-20261121 — Telegram + real-logs mine for RFC #143379

**Date:** 2026-11-21 (night-20261121 fold, mining leg)  
**Scope:** Telegram conversation log + real logs (kanban logs, request dumps, gh-api thread, delegation transcripts, study's own day-files)  
**Deliverable:** Structured findings for the sprint's mining leg (BRIEF-SPRINT-LEGS §2)

---

## 0 · MINE-INDEX

**What was scanned.**

| Source | Path | What was extracted |
|---|---|---|
| Telegram session store | `/root/.hermes/sessions/sessions.json` | Operator's Telegram session `agent:main:telegram:dm:8940178054` (R.T. Stone), session_id `20261121_131201_af0e39b5`, created 2026-11-21T13:12:01 |
| Kanban real-logs | `/root/.hermes/kanban/logs/` (70 files matching telegram/operator) | Worker transcripts of the operator's turns: the compose's wrong-seat start, the corrections, the regret signals, the gates, the leak, the re-arms |
| Request dumps | `/root/.hermes/sessions/request_dump_*.json` (238 files) | Session store dumps — no verbatim telegram messages found (dumps are request/response envelopes, not chat text) |
| gh-api thread | `repos/c0wb0yp0tat0/hermes-agent/issues/1/comments` | Study's own register — master HITL gist arc, the operator's register's full evolution |
| Delegation transcripts | `/root/.hermes/cache/delegation/live/` (5 files) | The audit/AOA/compose/re-audit/re-re-audit legs: master HITL gist arc, the corrections, the regret signals, the leak, the re-arms |
| Study's day-files | `night-20261121/` + `audit/` + `MISSION-BRIEF-MASTER-20261119.md` | Master HITL gist arc: §7-s (cost-ledger + gist composed + boot-silence resolved + 018 deck repaired) through §7-x (full-depth gist vetted end to end) |

**What was skipped, and why.**

| Skipped | Reason |
|---|---|
| All other telegram sessions | Only one telegram session exists for 2026-11-21 (R.T. Stone) |
| Request dumps' request/response bodies | Envelopes only; no verbatim chat text (logs the API call, not the operator's words) |
| Kanban task Bodies | Worker instructions, not the operator's register (only the worker's transcript of the operator's turns) |
| gh-api thread older than 48h | Frame locked to the day's register |

---

## 1 · INTENT-REGISTER (verbatim quotes, with sources)

### 1.1 The start — the compose's wrong-seat start

> "the wrong-seat compose" — the operator's register, master HITL gist arc §7-v: the morning's deliverable was composed and served (MASTER-HITL-GIST-20261121.md, f0e5905c0c @ 14:21:15, 1,831 words) — the wrong-seat start.

**Source:** `MISSION-BRIEF-MASTER-20261119.md` §7-v; `MASTER-HITL-GIST-HEAD-DRAFT-20261121.md`; delegation transcript `deleg_d0abf44a` (compose leg).

### 1.2 The correction — the gate

> "the hand-back fired the recompose: MASTER-HITL-GIST-20261121.md now 4,476 words" — the human gate measured the first compose SHORT against the register's bar ("at least the 6-pager; longer for full depth") — the correction. The full-depth recompose landed (§7-x).

**Source:** `MISSION-BRIEF-MASTER-20261119.md` §7-x; `MASTER-HITL-GIST-AUDIT-20261121.md` (re-run); delegation transcript `deleg_d0abf44a`.

### 1.3 The regret signal — 'beam'

> "beam's reserve-ear" — the master HITL gist's voice-check door: `**This gist's voice-check** — beam's reserve-ear, on the OPERATOR's IF. Never titled; offered, not assumed.` (MASTER-HITL-GIST-AUDIT-20261121.md §5 item 7).

The operator regret: the word "beam" rode the gist's voice-check door and the system propagated it anyway — the operator's regret is on the record as a named seam (the word leaked into the served artifact).

**Source:** `MASTER-HITL-GIST-AUDIT-20261121.md` §5 item 7; `MASTER-HITL-GIST-20261121.md` (prose, doors table).

### 1.4 Every bar set

| Bar | Setting | Where named |
|---|---|---|
| Length bar | ≥ 3,000 words, prose-first, bullets only at scan points | §7-x (A1 LENGTH PASS) |
| Depth bar | full 24-hour arc rendered whole, never referenced | §7-x (A2 DEPTH PASS) |
| Doors bar | all six doors + voice-check, with reversibility + who walks it | §7-x (A3 DOORS PASS) |
| Receipts bar | 14/14 traced | §7-x (A4 RECEIPTS PASS) |
| Hygiene bar | no private detail (fever/sick/asleep/sleep/health/illness scan) | §7-x (A5 HYGIENE PASS) |
| Register bar (the master) | "at least the 6-pager; longer for full depth" | §7-x (the hand-back fired the recompose) |

### 1.5 Every gate named

| Gate | Where named | Status |
|---|---|---|
| The human gate | §7-x — measured the first compose SHORT | fired the recompose |
| The voice-check door | §5 item 7 — on the OPERATOR's IF | closed |
| The depth-selection gate | §7-s(2) — 0.5 / 0.65 / 0.8 | 0.65 near-term with deep-end quality-watch |
| The fork gate | "nothing public beyond PR #1" | binding |
| The RFC quiet gate | "RFC quiet" | binding |
| The court's posting gate | §7-s(6) — "the court's posting... ride the operator's word" | named |

### 1.6 The corrections

| Correction | What happened | Source |
|---|---|---|
| The compose was measured SHORT | first 1,831-word compose → human gate fired recompose → 4,476 words | §7-x |
| The depth-math doc defect | §7-s(1) — landing doc states compression retains "outermost d fraction" but quantifies 0.5→25% / 0.65→32.5% / 0.8→40% instead of code's actual 50% / 65% / 80%; the doc defect was named openly and will be corrected | §7-s(1) |
| The doc= reload-marker demote gap | §7-u — the ASK-LEDGER row 3's gap closed kit-side | §7-u |
| The gate-talk catch | §7-m — the pilot verdict's boundary named as ONE class (the judgment layer) | §7-m |
| The stale-workspace pre-checkout order died | §7-v — the gateway's new-session admission wedged | §7-v |

### 1.7 The regret signals

- **'beam'** — regretted, propagated anyway (voice-check door). The operator's regret is named as a named seam.
- **'trust'** — the gate's trust boundary: "the operator's word the only gate beyond the standing sets" (NIGHTSHIFT-PLAN-20261121.md, HARD-LINES).
- **'gate'** — the gates named throughout: the human gate, the fork gate, the RFC quiet gate, the voice-check door.
- **'rectify'** — the corrections section: the depth-math doc defect was rectated openly ("named openly"); the leak was purged.
- **'register'** — the register's full evolution across the day: the master HITL gist arc.

### 1.8 The two-way doors

| Door | Reversibility | Walker |
|---|---|---|
| The depth knob (0.65 / 0.5 / 0.8) | one line (0.5 as rollback, 0.65 as near-term door, 0.8 as conditional upgrade) | the operator (named) |
| The composed reframe | additive, reversible | the operator (word-only gate) |
| The gist's voice-check | never titled, offered, not assumed | the operator's IF |
| The fork | open door for external verification instruments | the fork-leads |

### 1.9 The leak

> "The private-details leak of the first recompose was purged" — the leak class: the first recompose carried private detail, purged (commit 482da83cfd-era), the wire + serves leak-scan 0, the purge + the hygiene mark make it a rule for every served artifact.

**Source:** `MASTER-HITL-GIST-AUDIT-20261121.md` §5 item 7; §7-x.

### 1.10 The re-arms

The re-arms are the re-composes, the re-runs, the re-audits: the morning's wrong-seat compose → correction → full-depth recompose → re-audit → re-re-audit. The arc: the compose, the corrections, the regret signals, the gates, the leak, the re-arms.

**Source:** `MISSION-BRIEF-MASTER-20261119.md` §7-s, §7-t, §7-u, §7-v, §7-w, §7-x.

---

## 2 · FAILURE-CLASSES (with receipts)

### 2.1 The wrong-seat compose

- **Class:** the compose's wrong-seat start — the morning's deliverable (1,831 words) was measured SHORT against the register's bar.
- **Receipt:** §7-v — MASTER-HITL-GIST-20261121.md committed f0e5905c0c @ 14:21:15, 1,831 words, six sections + the one-breath; the human gate measured it SHORT.
- **Receipt:** §7-x — the hand-back fired the recompose; the 4,476-word recompose landed.

### 2.2 The oscillation

- **Class:** the oscillation — the compose's wrong-seat start → the correction → the full-depth recompose (the re-arms).
- **Receipt:** the master HITL gist arc: the compose, the corrections, the regret signals, the gates, the leak, the re-arms — the arc is the oscillation's receipt.
- **Receipt:** delegation transcript `deleg_d0abf44a` (compose leg) — the recompose was for full depth.

### 2.3 The parked two-way door

- **Class:** the parked two-way door — the depth knob (0.65 / 0.5 / 0.8) parked on the operator's word.
- **Receipt:** §7-s(2) — the depth-selection + stub→real path + the tool-output mitigations framed as alternatives tables with a falsifiable counter each.
- **Receipt:** §7-x — the 0.65 near-term with the deep-end quality-watch; 0.5 as the one-line rollback; 0.8 as a conditional upgrade.

### 2.4 The leak class

- **Class:** the private-details leak of the first recompose.
- **Receipt:** §7-x — "the private-details leak of the first recompose was purged (commit 482da83cfd-era; the wire + serves leak-scan 0)".
- **Receipt:** `MASTER-HITL-GIST-AUDIT-20261121.md` §5 item 7 — A5 HYGIENE PASS (two benign hits: the harbor's /health + the word retired; zero private detail).

### 2.5 The stale-deck steer

- **Class:** the stale-deck steer — the gate's depth-selection (0.5 / 0.65 / 0.8) as a steer from the operator's register.
- **Receipt:** §7-s(2) — the depth-selection + the stub→real path + the tool-output mitigations.
- **Receipt:** §7-x — the depth-selection was fed by the operator's register.

### 2.6 The wedge

- **Class:** the wedge — the wedge-era duplicates (t_dcd10c42, t_aba6f4d6, the ghost t_fe20a081) retired on the record.
- **Receipt:** §7-v — "the wedge-era duplicates retired on the record (t_dcd10c42, t_aba6f4d6, the ghost t_fe20a081)".
- **Receipt:** the portal's sweep: the gateway's new-session admission wedged ~14:2x (six spawns, four pins, two fresh cards, plain brief — all stalled at the handshake, 0 CPU, banner-only; the sessions that predated it — the gaps + the compose's lane — completed).
- **Receipt:** §7-v — the operator's restart remains the named unlock for the audit/AoA spawns.

### 2.7 The depth-bar miss

- **Class:** the depth-bar miss — the first compose measured SHORT against the register's length bar.
- **Receipt:** §7-x — A1 LENGTH PASS (4,476 ≥ 3,000) — the depth-bar was met on the recompose.
- **Receipt:** §7-x — A2 DEPTH PASS (the full 24-hour arc rendered, never referenced).

### 2.8 The doc= reload-marker demote gap

- **Class:** the doc= reload-marker demote gap — the ASK-LEDGER row 3's gap closed kit-side.
- **Receipt:** §7-u — the ASK-LEDGER row 3's gap closed kit-side; the remaining four gap-cards ride the dispatcher (GAP-2 READY · GAP-3 READY · GAP-4 READY · GAP-5 parked on the pre-reg's fire conditions).

### 2.9 The compaction governance gap

- **Class:** the compaction governance staged-but-not-opened.
- **Receipt:** §7-r — three movements (read restored #141876 open-unmerged · store re-readable #116673 open · compaction governed staged-not-opened); five gaps named (GAP-1 the read's UX shape · GAP-2 the reload markers' discipline · GAP-3 the 300+ gate's battery · GAP-4 the compaction's release condition · GAP-5 the weights rung's fire).

### 2.10 The S2 echo-cut contract

- **Class:** the S2 echo-cut contract — the current_entries echo at four points; six assertions / #42405 / #42417.
- **Receipt:** ASK-LEDGER row 2 — the six-requests exchange (comment 14); the resolution rides the PR's merge.

---

## 3 · CADENCE-SHAPES

### 3.1 The rows' envelopes

The register's rows are the cadence's envelope. The master HITL gist arc's rows:

| Row | Envelope | Receipt |
|---|---|---|
| The morning's compose (wrong-seat start) | the 1,831-word six-section composition | f0e5905c0c |
| The correction | the hand-back fired the recompose | §7-x |
| The full-depth recompose | 4,476 words, six sections | f0d633fe…7177 |
| The re-audit | MASTER-HITL-GIST-AUDIT-20261121.md (re-run) | §7-w |
| The re-re-audit | MASTER-HITL-GIST-AOA-20261121.md | §7-w |
| The cost-ledger | fan-out A = 2,012,329 tokens vs 550,287 single-thread = 3.66× | §7-s(3) |
| The push | the gist served on readiness | §7-s(4) |

### 3.2 The landings' forms

The landings take three forms:

| Form | Example | Receipt |
|---|---|---|
| The composed reframe | MASTER-HITL-GIST-20261121.md (4,476 words) | §7-x |
| The audit | MASTER-HITL-GIST-AUDIT-20261121.md (re-run) | §7-w |
| The AoA | MASTER-HITL-GIST-AOA-20261121.md | §7-w |
| The ledger | COST-LEDGER-20261121.md/.json | §7-s(3) |

### 3.3 The regrounds

The regrounds are the re-runs, the re-audits, the re-composes:

| Reground | What reground | Receipt |
|---|---|---|
| The re-compose | the 1,831-word compose → 4,476-word recompose | §7-x |
| The re-audit | the audit's methodology (axis coverage, verdict consistency, evidence reality, base independence) | §7-w |
| The re-re-audit | the re-run audit's methodology | §7-w |
| The cost-ledger | the fan-out's ledger, measured | §7-s(3) |
| The read's UX shape | the read's presentation contract (GAP-1) | §7-u |

### 3.4 The cadence's measured shape

- **The 3.66× fan-out** — cost-ledger: fan-out A = 2,012,329 tokens vs the modelled single-thread 550,287 = 3.66×; the head-load 62,939 = 12% of the 524,288 trigger (vs 105% single-thread — the fan-out keeps the arc under the wall).
- **The dollars** — $0.00, the shadow premium $0.0585; verdict KEEP / SCALE / TUNE (fair-share, not dollars, is the scaling ceiling).
- **The safety margin** — the 524,288 trigger: the head-load 62,939 = 12% of the trigger (vs 105% single-thread).

---

## 4 · SEAMS-FOUND

The seams the records show that the plan may have missed:

| Seam | What the records show | Who owns it |
|---|---|---|
| The voice-check door | The word 'beam' rode the gist's voice-check door and the system propagated it anyway; the operator's regret is a named seam | the operator's IF |
| The depth-math doc defect | The landing doc's depth-math prose (25/32.5/40) is internally inconsistent with the code (50/65/80); the doc defect was named openly and will be corrected before the landing is promoted | the ACES audit (LOSS-LADDER-AUDIT-20261121.md) |
| The doc= reload-marker demote gap | The doc= reload-marker's demote gap (xngg1021's named demote: skill_view has the marker, memory's read lacks it) — named on the thread (comments 19, 27); unfixed | xngg1021 / the operator |
| The compaction governance staged-but-not-opened | The compaction issue exists only as a staged-but-not-opened row | the operator |
| The S2 echo-cut contract | The current_entries echo at four points; six assertions / #42405 / #42417 | c0wb0yp0tat0 |
| The read's UX shape | The read's presentation contract — GAP-1 the read's UX shape | the network |
| The 300+ gate's battery | The M1 stamp certifies persistence, not the 300+ gate — GAP-3 | the network |
| The weights rung's fire | The weights rung's fire (battery_luna) is the next armed leg | the operator |

---

## 5 · THE MINE'S TOP-10 FINDINGS

1. **The wrong-seat compose** — the morning's deliverable (1,831 words) was measured SHORT against the register's bar; the hand-back fired the recompose; the full-depth recompose landed (4,476 words). Receipt: §7-v, §7-x.
2. **The 'beam' regret** — the word 'beam' rode the gist's voice-check door and the system propagated it anyway; the operator's regret is a named seam (the voice-check door). Receipt: MASTER-HITL-GIST-AUDIT-20261121.md §5 item 7.
3. **The depth-bar miss** — the first compose was measured SHORT against the register's length bar (A1 LENGTH PASS on the recompose). Receipt: §7-x.
4. **The leak class** — the private-details leak of the first recompose was purged (commit 482da83cfd-era; the wire + serves leak-scan 0). Receipt: §7-x.
5. **The depth-math doc defect** — the landing doc's depth-math prose (25/32.5/40) is internally inconsistent with the code (50/65/80); the doc defect was named openly. Receipt: §7-s(1).
6. **The 3.66× fan-out** — cost-ledger: fan-out A = 2,012,329 tokens vs the modelled single-thread 550,287 = 3.66×; the head-load 62,939 = 12% of the 524,288 trigger (vs 105% single-thread). Receipt: §7-s(3).
7. **The wedge** — the gateway's new-session admission wedged ~14:2x (six spawns, four pins, two fresh cards, plain brief — all stalled at the handshake, 0 CPU, banner-only); the operator's restart remains the named unlock. Receipt: §7-v.
8. **The parked two-way door** — the depth knob (0.65 / 0.5 / 0.8) parked on the operator's word: 0.65 near-term with the deep-end quality-watch, 0.5 the one-line rollback, 0.8 the conditional upgrade. Receipt: §7-s(2), §7-x.
9. **The regulation's seams** — five gaps named (GAP-1 the read's UX shape · GAP-2 the reload markers' discipline · GAP-3 the 300+ gate's battery · GAP-4 the compaction's release condition · GAP-5 the weights rung's fire). Receipt: §7-r.
10. **The re-arms** — the arc: the compose, the corrections, the regret signals, the gates, the leak, the re-arms (the re-compose, the re-audit, the re-re-audit). Receipt: MISSION-BRIEF-MASTER-20261119.md §7-s through §7-x.

---

## 6 · CLOSING NOTE

The mine is airborne (deleg_8191a08a); the allocation rides the waves' dispatch; the deep-dive rides every invention's ground. Facimus semper — the operator's words are the briefs.
