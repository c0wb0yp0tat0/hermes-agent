# CASE-STUDY-1-EXECUTION-20261122 — MISSION-2 EXECUTOR RUNG DELIVERABLE

*Slot: the field-case mission's EXECUTOR rung (longcat). Chain: PLANNER (solar, ce81a17774) → THIS (longcat — the completeness double-check + measurement-map) → sanity → fold → hy's gate. Seat: meituan/longcat-2.5:free (probed 200 at the fire; base-distinct from the planner's solar — the sequencing's law). The PLAN and the planner's deliverable are NOT altered — this rung's mandate: verify the intake's completeness + deepen the case's operational shape.*

---

## 0. THE TWO-ROW VERDICT

### 0.1 Completeness double-check: 10/10 carried, 0 dropped, no flattening

Re-read the planner's intake map (CASE-STUDY-1-FIELD-20261122.md, ce81a17774) against the two raw field rows byte-for-byte — FIRST the director's intake (scratch `/tmp/c-6411683234.md`, verified current: identical to the repo record `COMMENT 6411683234`), then the probe results (scratch `/tmp/c-6515564390.md`, verified current):

| # | Element (as it stands in the RAW rows) | Carried in the planner's deliverable? | Evidence line (with the exact words carried) | Status |
|---|---|---|---|---|
| 1 | Ask 1 — **case description** (his profile's memory shape, occupancy history, manual-consolidation cycles) | YES | §0.1: "pre-consolidation (the anchor-full wall) | 29.10 | 3,844 | 96%" / "post-consolidation | 29.10 | 2,930 | 73%" / "probe (now) | 30.10 | 3,376 | 84%" — the occupancy history the profile supplies | CARRIED |
| 2 | Ask 2 — **metrics / probes** (per-profile occupancy logs; read-concurrency/K-gate harness run against live state) | YES | §0.2 (byte-check: 0 — no `MemoryStore.read`; doc-chain is the read path) and §1.2 ("the K-gate / read-concurrency harness (named by the pilot's ask) run against live state") | CARRIED |
| 3 | Ask 3 — **logs** (private-repo access works; help sanitize before any release for study) | YES | §1.3: raw session content / raw memory bytes / private-repo logs are stripped before any release for study; sanitized evidence in | CARRIED |
| 4 | His boundary — sanitized evidence, not raw secrets or raw session content; "tell me what to strip and I'll strip it" | YES | §1.3 THE STRIP-CONTRACT, verbatim | CARRIED |
| 5 | Baseline's three readings (29.10 pre 3,844/4,000 96%; 29.10 post 2,930/4,000 73%; 30.10 now 3,376/4,000 84%) | YES | §0.1 the occupancy-history table, the three rows word-for-word identical, incl. the 24-entry count | CARRIED |
| 6 | Byte-check-0 confirmation (`byte-check: 0 — read missing on this build`; released build, no `MemoryStore.read`; doc-chain is the read path) | YES | §0.2 verbatim ("the released build has NO `MemoryStore.read` → the doc-chain is the read path"; "the probe's `byte-check: 0`") | CARRIED |
| 7 | The two landed-back entries (vision fix + external-bot convention; 24 entries) | YES | §0.1: "24 entries — after two standing entries landed back: vision fix + external-bot convention" | CARRIED |
| 8 | Accounting-lag flag (probe 3,376 chars vs live `memory` snapshot 2,930; delta is session-snapshot lag, taken at turn-start before the last two entries landed; NOT an accounting mismatch; flag for the RFC if anyone compares probe vs runtime mid-run) | YES | §0.3 verbatim, incl. the exact "not an accounting mismatch" wording + the RFC flag wording | CARRIED |
| 9 | Discipline-shape (MEMORY.md anchor, `[ПРАВИЛО]`-tagged standing rules; CONTEXT.md procedures/state; references/ canonical detail rules-2026-10-06.md, rules-31-32-34.md) | YES | §0.4 verbatim | CARRIED |
| 10 | Two-passes cadence (pass one the pointer, pass two the detail — "the one thing we run implicitly but not explicitly… I will make that an explicit step in the contour's discipline") | YES | §0.4: "The one implicit-to-explicit: the two-passes cadence — pass one the pointer, pass two the detail (which the pilot said he would make explicit)" | CARRIED |

**Verdict: 10/10 carried, 0 dropped, 0 flattened.** Every element stands in its own numbered subsection of the intake map (the asks stay in order; the readings, the byte-check, the accounting flag, the discipline-shape, and the cadence each have their own §0.X home). No element was merged, re-labelled, or dropped into a prose block. The only sub-element not a separate §0.X row is #7 (the two landed-back entries), which sits inside the readings sentence of §0.1 — that is the raw rows' own sentence structure, not a flattening (both pieces travel together from one source sentence, and both words are carried verbatim).

### 0.2 The two raw rows, re-derived (receipt for the double-check)

`/tmp/c-6411683234.md` (director's intake, verbatim): offer + the three asks in order + the boundary.
`/tmp/c-6515564390.md` (probe results, verbatim): the baseline's three readings + `byte-check: 0` + the accounting-snapshot-lag flag + the discipline-shape + the two-passes cadence (explicit promise).

Both were read from the scratch directly (never `web_extract`), and the intake copy was confirmed against the repo record (`CYCLES/RFC-143379-RECORD-20261111.md`, "COMMENT 6411683234") — identical text, no drift.

---

## 1. THE MEASUREMENT-MAP (the application — the concrete what-runs-where)

Every instrument, at its live use. Not-for-its-sake gate: each row names the case's live use before it names the tool.

| Live use | Instrument | What runs where | Named to |
|---|---|---|---|
| **The read-gap's price** on a 96%-wall profile | The kit's armory's fold-time / read-time rule — the G14 gate (`canary-phase1-spec-20261122.md` §3 G14: `memory(action, doc)` call shape, `_STORE_ACTIONS` = {add,replace,remove,patch}, no read arm, no doc param, the inline `_memory` executor forwards no doc, demote-stub recovery pointer = `session_search`) | The released build carries `byte-check: 0 — read missing`; the doc-chain (MEMORY.md anchor + CONTEXT.md + references/) serves reads; each re-read is a gate on his 96%-wall profile | The price of a missing read = the doc-chain re-read round-trip, visible in the probe's live reads at 3,376 chars / 84% occupancy (the wall is where the miss bites, as the pilot said) |
| **The hot-tier occupancy's live shape** | The director's per-profile occupancy logs + the probe's readings | Live run: 3,844/4,000 (96%) → 2,930/4,000 (73%) → 3,376/4,000 (84%); the 2,930 anchor is the consolidation-walker's reference point | The 2,930-anchor's live shape — the never-cram economy, measured per-profile, logged by the director himself |
| **The consolidation-walk's economics** | The entry-by-entry walk the triage already ran (and the discipline-shape says he will make explicit) | The 3,844 → 2,930 walk, entry-by-entry, stays/moves as classified | The walk's cost = entries touched × time-per-entry; the walk is done when the live 3,376 now contour is classified entry-by-entry (the two landed-back entries included) |
| **The probes he runs** | The per-profile occupancy logs (his documented practice); the read-concurrency + K-gate harness named by the pilot's ask | Against live state — the read-concurrency + K-gate harness is nameable from the kit (the planner's deliverable §1.2 already carries it as "the K-gate / read-concurrency harness (named by the pilot's ask) run against live state") | The probe suite is read-to-the-case, never read-into-the-case: every probe measures the director's contour, and nothing else |

---

## 2. THE STRIP-CONTRACT'S OPERATIONAL FORM (the sanitization mechanics for HIS data)

The pilot's honesty boundary intact, never softened:

- **What he strips (before any release for study):** his raw session content, his raw memory bytes, and his private-repo logs.
- **What stays on his side:** everything raw — the stripped set is the only thing that leaves his side; the release is the ONLY outbound channel.
- **How the private-repo logs ride:** he holds private-repo access; the release is the sole-egress route (the kit's G4 rule — sole private-repo release `nm3-canary-r1-20261120`, `egress_secondary_downloads` 0), so the sanitized evidence rides the same one-way, byte-counted channel as the kit's own egress, and the raw bytes never enter the study repo.
- **The not-for-its-sake gate, applied to his data:** every element names its live use in the case study (§1). Nothing is collected for its own sake; the release is the only surfacing, and it carries sanitized evidence only.

---

## 3. THE SELF-PERPETUATION NOTE (the next measured gates)

These runners' verdicts become the readiness loop's next measured gates (the kaizen improver loop's next pass):

1. **The read-concurrency / K-gate probe measured on live state** — the pilot's ask (§1, row 4); the gate that moves the read-gap from "confirmed missing" to "quantified price".
2. **The two-passes cadence made explicit** — pass one the pointer, pass two the detail, in the discipline (§0.4 + the pilot's own explicit promise); the gate is that the cadence is now a named step, not an implicit habit.
3. **The accounting flag as a first-fidelity RFC flag** — probe (3,376) vs runtime snapshot (2,930) mid-run lag; the gate is that no one compares probe vs runtime mid-run without flagging the lag.
4. **The doc-chain-as-read-path** — the verified read path (`byte-check: 0` field-confirmed on a live profile); the gate is the read-path rule re-checked at every fold (G14 HOLD, the kit's precondition, never the substrate's rule).
5. **The P1-seam** — the field-confirmed seam on a live profile (the missing read, exactly where it bites on his 96%-wall profile); the gate is the read-gap's price quantified on his wall profile.
6. **The consolidation-walk ledger** — the entry-by-entry stays/moves classification, run to the new 3,376-now contour, closing the walk's economics on live state (the 3,844→2,930 walk plus the two landed-back entries plus whatever the 446-char rise costs in re-entry).

---

## 4. THE GATES' PROPOSAL (the measured gates for the case)

| Gate | What it measures | Proposal |
|---|---|---|
| **G14 read-gap price** | The doc-chain re-read cost on the 96%-wall profile (the byte-check: 0's price) | Proposed gate: express the read-gap's price as a measured line (read-path re-read count/round-trip on the wall profile) at the next pass |
| **G15 hot-tier occupancy** | The 2,930-anchor's live shape and the never-cram economy | Proposed gate: the live per-profile occupancy readings (96/73/84) as the case's standing measurement, logged per-profile |
| **G16 consolidation-walk economics** | The entry-by-entry stays/moves ledger of the 3,844→2,930 walk, extended to the 3,376 now | Proposed gate: the walk ledger carried as the case's consolidation measurement |
| **G17 read-concurrency + K-gate** | The pilot's ask, run against live state | Proposed gate: the harness (nameable from the kit) fired on live state, the read-concurrency and K-gate readings as the probe suite's core |
| **G18 two-passes cadence** | The discipline made explicit (pointer pass, detail pass) | Proposed gate: the cadence as a named, repeatable discipline step |

---

## 5. THE DOORS (named, waiting — OUTSIDE this rung's scope, per FLP:30 / AOA:139-146)

Court's posting · the RFC #143379 upstream surface (QUIET until the operator's word) · the autopilot's pilot gate · the voice-check's shape. Named and waiting; none gates this deliverable.

---

*Facimus semper — the record is on disk, the bytes are on the record, the record corrects itself out loud. The delivery is written, the double-check is closed, the measurement-map is laid. — kanban-pilot*
