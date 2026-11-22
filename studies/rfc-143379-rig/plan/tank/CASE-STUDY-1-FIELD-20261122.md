# CASE-STUDY-1-FIELD-20261122 — the field case's intake map + the case-study's shape + the strip-contract

The first field case's intake (solar, pin VERIFIED this time): the director's live contour, receipted, plus the shape the pilot kit's instruments would apply to it — and the strip-contract that keeps the pilot's raw side on his side. The field comments (`c-6411683234`, `c-6515564390`) are carried in full at the gate; the pilot kit's surfaces (the OPUS, the rung-1 receipt, the armor) are re-derived from the cited files' bytes. Nothing is invented; a non-reproduction is a QUESTION with receipts.

---

## 0. THE INTAKE'S MAP

### 0.1 The director's contour (occupancy history, receipted)
| Probe | Date | Occupancy | % of 4,000 |
|---|---|---|---|
| pre-consolidation (the anchor-full wall) | 29.10 | 3,844 | 96% |
| post-consolidation | 29.10 | 2,930 | 73% |
| probe (now) | 30.10 | 3,376 | 84% |

The now contour is **24 entries — after two standing entries landed back**:
- **vision fix**
- **external-bot convention**

### 0.2 The read-missing confirmation (byte-check 0 — the P1-seam field-confirmed on a live profile)
- The released build has **NO `MemoryStore.read`** → the **doc-chain is the read path** (MEMORY.md anchor + CONTEXT.md + references/).
- The probe's **`byte-check: 0 — read missing on this build`** confirms the **P1-seam on a live profile** (the field comment's "Field results, as promised" line). One clear line.

### 0.3 The accounting flag worded for the RFC
- Probe reports **3,376 chars** vs the client's live `memory` snapshot of **2,930**. The delta is almost certainly **session-snapshot lag** (the snapshot is taken at turn-start, before the last two entries landed) — **NOT an accounting mismatch**. Worth flagging for the RFC if anyone compares probe vs runtime mid-run.

### 0.4 The discipline-shape
- `MEMORY.md` = anchor, standing rules only (`[ПРАВИЛО]`-tagged).
- `CONTEXT.md` = procedures/state; `references/` = canonical detail (rules-2026-10-06.md, rules-31-32-34.md).
- The triage **IS** the consolidation walk: the **3,844 → 2,930** walk, entry-by-entry (stays/moves).
- The one implicit-to-explicit: the **two-passes cadence** — pass one the pointer, pass two the detail (which the pilot said he would make explicit).

---

## 1. THE CASE-STUDY'S SHAPING

### 1.1 What the kit measures
- **the read-gap's price**: what a missing `MemoryStore.read` costs the profile (the doc-chain serves reads; each re-read is a gate).
- **the hot-tier's occupancy**: the anchor-full wall (96% → 73% → 84%) — the never-cram economy.
- **the consolidation walk's economics**: the 3,844 → 2,930 walk entry-by-entry.

### 1.2 What the pilot runs
- His documented probes: the baseline/post/now occupancy readings (3,844 → 2,930 → 3,376).
- The read-gap measurement: **`byte-check: 0`** on the released build.
- The **K-gate / read-concurrency harness** (named by the pilot's ask) run against live state.

### 1.3 THE STRIP-CONTRACT
- **raw secrets / raw session content NEVER leave the pilot's side** — the pilot's honesty boundary.
- The pilot strips: his raw session content, his raw memory bytes, and his private-repo logs (private repo access works for him; he sanitizes before any release for study).
- What the kit receives: **sanitized evidence only** (the contour, the probe readings, the receipted claims).
- **The not-for-its-sake gate: every element names its live use in the case-study.** Nothing is collected for its own sake.

---

## 2. THE SELF-PERPETUATION NOTE (the next measured gates)

- the **read-concurrency / K-gate probe measured on live state** (the pilot's ask).
- the **two-passes cadence** made explicit in the discipline (pass one pointer, pass two detail).
- the **accounting flag** as a first-fidelity RFC flag (probe vs runtime mid-run lag).
- the **doc-chain-as-read-path** as the verified read path (`byte-check: 0`).
- the **P1-seam** as the field-confirmed seam on a live profile.

---

## 3. THE DELIVERY

- Path: `studies/rfc-143379-rig/plan/tank/CASE-STUDY-1-FIELD-20261122.md`
- Committed as `kanban-pilot` (study path only; no push; no `checkout`/`stash`/`rm`; index-lock → wait ~10s, retry once).

---

## 4. REPORT LINES

- **sha**: `<commit sha of the kanban-pilot commit>`
- **occupancy history**: 3,844 → 2,930 → 3,376 (96% → 73% → 84%; the two landed-back entries: vision fix + external-bot convention).
- **read-missing confirmation**: byte-check 0 — the released build has NO `MemoryStore.read`; the doc-chain is the read path; the P1-seam is field-confirmed on a live profile.
- **strip-contract**: raw secrets / raw session content NEVER leave the pilot's side — sanitized evidence in, the pilot's boundary intact.
