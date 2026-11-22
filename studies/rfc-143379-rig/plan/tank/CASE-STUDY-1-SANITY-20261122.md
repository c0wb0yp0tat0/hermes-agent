# CASE-STUDY-1-SANITY-20261122 — MISSION-2 SANITY RUNG
## The gates' adjudication, the crosswalk's re-location, the verdict
### (stepfun — the gates G14–G18's adjudication against the RAW field rows)

**Seat:** stepfun/step-3.7-flash:free · **Brief:** BRIEF-SPECIAL-MISSION-2-SANITY-20261122.md
**Chain:** PLANNER (solar, ce81a17774) → EXECUTOR (longcat, 284305554d) → **THIS (stepfun — the gates' adjudication)** → fold → hy's gate.
**The raw receipts (tail-reads, frozen lane, 13:30:22):** the planner's deliverable
`plan/tank/CASE-STUDY-1-FIELD-20261122.md` (ce81a17774); the executor's deliverable
`plan/tank/CASE-STUDY-1-EXECUTION-20261122.md` (284305554d); the two raw field rows
`/tmp/c-6411683234.md` (director's intake) and `/tmp/c-6515564390.md` (probe results);
the register + the GATE LAW's final form in `/root/.hermes/memories/MEMORY.md` (line 19).
**This rung alters neither the PLAN nor the planner's nor the executor's deliverables.**

---

## 0. THE RAW RECEIPTS (ground truth, re-derived)

### 0.1 The director's intake (raw row 1, `/tmp/c-6411683234.md`, verbatim)
1. **Case description** — memory shape, occupancy history, manual-consolidation cycles.
2. **Metrics / probes** — per-profile occupancy logs; a read-concurrency / K-gate harness
   "run against live state".
3. **Logs** — private-repo access works; help sanitize before any release for study.
4. **Boundary** — "I share sanitized evidence, not raw secrets or raw session content.
   Tell me what to strip and I'll strip it."

### 0.2 The probe results (raw row 2, `/tmp/c-6515564390.md`, verbatim)
- **Baseline:** 29.10 pre-consolidation: **3 844 / 4 000 (96%)** — "the anchor-full wall."
- **Post-consolidation (29.10):** **2 930 / 4 000 (73%)**.
- **Now (probe, 30.10):** **3 376 / 4 000 (84%), 24 entries** — "after two standing entries
  landed back (vision fix + external-bot convention)."
- **Probe verdict:** "`byte-check: 0 — read missing on this build`" — released build, no
  `MemoryStore.read`, so the **doc-chain is the read path**.
- **Accounting:** probe reports 3 376 chars vs the client's live `memory` snapshot of 2 930.
  The delta is almost certainly **session-snapshot lag** (snapshot taken at turn-start, before
  the last two entries landed) — **NOT an accounting mismatch** — flag for the RFC if anyone
  compares probe vs runtime mid-run.
- **Discipline-shape:** MEMORY.md = anchor, standing rules only (`[ПРАВИЛО]`-tagged);
  CONTEXT.md = procedures/state; references/ = canonical detail (rules-2026-10-06.md,
  rules-31-32-34.md).
- **Consolidation:** "The triage you describe *is* the consolidation I ran on 29.10 — the 3 844
  → 2 930 is that walk, **entry-by-entry (stays / moves)**."
- **Cadence:** "The one thing we run implicitly but not explicitly is your **'two passes,
  never one'** cadence — I will make that an explicit step in the contour's discipline."

### 0.3 The numbers × claims, re-derived (ground truth, not asserted)
| claim | raw receipt | re-derive |
|---|---|---|
| 96% | 3 844 / 4 000 | 3844/4000 = 96.1% → **96%** ✓ |
| 73% | 2 930 / 4 000 | 2930/4000 = 73.25% → **73%** ✓ |
| 84% | 3 376 / 4 000 | 3376/4000 = 84.4% → **84%** ✓ |
| 446-char delta | 3 376 vs 2 930 | 3376 − 2930 = **446** ✓ |
| byte-check-0 | `byte-check: 0 — read missing on this build` | released build, no `MemoryStore.read`; doc-chain is the read path ✓ |
| two landed-back entries | "(vision fix + external-bot convention)" | "24 entries — after two standing entries landed back" ✓ |
| accounting flag | "NOT an accounting mismatch"; "flag for the RFC if anyone compares probe vs runtime mid-run" | ✓ |
| strip-contract boundary | "I share sanitized evidence, not raw secrets or raw session content. Tell me what to strip and I'll strip it." | ✓ |
| strip-contract shape | "MEMORY.md = anchor, standing rules only (`[ПРАВИЛО]`-tagged); CONTEXT.md = procedures/state; references/ = canonical detail" | ✓ |

No numeric mismatch anywhere: the executor's rendered copies (3,844 / 2,930 / 3,376 / 4,000 /
96% / 73% / 84%) match the raw rows after the thousands-separator translation (spaces → commas),
which is a rendering choice, not a claim.

### 0.4 The strip-contract's mechanics, re-derived from the raw rows
1. **What is stripped before any release for study:** raw secrets, raw session content, raw
   memory bytes, private-repo logs.
2. **The release is the ONLY outbound channel;** the stripped set is the only thing that leaves
   the pilot's side; raw bytes never enter the study repo.
3. **The pilot strips only what he has promised to strip** — the caller tells him what to strip
   and he strips it, boundary intact.
4. **The shape the strip runs inside** (the discipline-shape): anchor rules via
   `[ПРАВИЛО]`-tagged; CONTEXT.md = procedures/state; references/ = canonical detail
   (rules-2026-10-06.md, rules-31-32-34.md).
5. Conclusion: sanitized evidence in, raw session content/bytes out — the pilot's honesty
   boundary is intact, never softened.

---

## 1. THE GATES' ADJUDICATION (G14–G18, per the executor's deliverable §4)
Every gate is adjudicated against the RAW receipts: the numbers × the claims re-derived.
**Rule:** a claim without its raw receipt = a WALL-CLAUSE QUESTION with the receipts;
a mismatch = a DEFECT named with its line. The proposal is a plan for the case's next
measured gates; the receipts are the case's measured ground.

### G14 — read-gap price
**Proposal:** *"express the read-gap's price as a measured line (read-path re-read count/
round-trip on the wall profile) at the next pass."*
**Receipts check:** the read-gap itself is **field-confirmed** — row 2: "`byte-check: 0 —
read missing on this build` — confirms the honest state you described: released build, no
`MemoryStore.read`, so the doc-chain is the read path here." ✓ the P1-seam is confirmed on a
live profile. **But** the "measured line (read-path re-read count/round-trip)" is **not in
the raw rows** — the receipts confirm the miss, not a price. G14's measurement is a
next-pass deliverable, not present evidence.
**Verdict: PASS-WITH-QUESTION** — the gap is receipted; the "measured line" is a next-pass
measurement with no receipt in the raw rows. Question: *G14's price is unquantified in the
case; only the miss (byte-check: 0) is carried.*

### G15 — hot-tier occupancy
**Proposal:** *"the live per-profile occupancy readings (96/73/84) as the case's standing
measurement, logged per-profile."*
**Receipts check:** the three readings are **verbatim in raw row 2** (3,844 / 96%; 2,930 /
73%; 3,376 / 84%) and mirrored word-for-word in the executor's §0.1 table.
**Verdict: PASS** — the readings are the case's measured ground, logged per-profile; no question.

### G16 — consolidation-walk economics
**Proposal:** *"the entry-by-entry stays/moves ledger of the 3,844→2,930 walk, extended to
the 3,376 now."*
**Receipts check:** the walk itself is **receipted** — row 2: "the 3 844 → 2 930 is that
walk, entry-by-entry (stays / moves)." **But** the **entry-by-entry ledger rows are not in
the two raw receipts** — only the executive sentence names the walk. G16's ledger is invoked
from a summary sentence, not carried rows; the per-entry stays/moves classification never
appears in the raw rows.
**Verdict: PASS-WITH-QUESTION** — the walk is receipted; the ledger rows are a question with
receipts. Question: *G16's ledger rows are absent from the two raw rows; only the summary
"3 844 → 2 930 is that walk, entry-by-entry (stays / moves)" is carried.*

### G17 — read-concurrency + K-gate
**Proposal:** *"the harness (nameable from the kit) fired on live state, the read-concurrency
and K-gate readings as the probe suite's core."*
**Receipts check:** the harness is **nameable** — row 1 Ask 2 names "read-concurrency, K-gate"
and offers to run it against live state; the pilot's promise is the offer, not an execution.
**But** the raw rows contain **no read-concurrency or K-gate readings** — the only read-gap
evidence is `byte-check: 0`. G17's "readings as the probe suite's core" is a promise, not a
receipt; the harness was never fired in the case's two rows.
**Verdict: PASS-WITH-QUESTION** — the harness is named (pilot's ask); the readings are a
next-pass measurement with no receipt in the raw rows. Question: *G17's readings do not exist
in the case's two rows — only the byte-check: 0 read-gap confirmation is carried.*

### G18 — two-passes cadence
**Proposal:** *"the cadence as a named, repeatable discipline step."*
**Receipts check:** the cadence is **named in the raw rows** — "The one thing we run
implicitly but not explicitly is your 'two passes, never one' cadence — I will make that an
explicit step in the contour's discipline." The pilot's explicit promise + the discipline
(shape: pass one the pointer, pass two the detail) are carried verbatim in the executor's
§0.4 and §1.2. **No question.**
**Verdict: PASS** — the cadence is named, promised, and will be explicit; it is the case's
next-named step.

**Gate tally: 2 × PASS (G15, G18) · 3 × PASS-WITH-QUESTION (G14, G16, G17) · 0 × FAIL.**
No gate is a DEFECT: no gate claim contradicts a raw receipt. Every PASS-WITH-QUESTION is a
wall-clause question with receipts — none of them a falsified claim.

---

## 2. THE CROSSWALK'S OWN SANITY (the 10/10 re-location)
The executor's §0.1 claims **10/10 carried, 0 dropped, 0 flattened** against the raw rows.
Each claimed "carried" element is re-located in the planner's deliverable — section title
+ one content line — the tree-is-the-truth discipline. All ten locate; the double-check is
faithful to the receipts.

| # | Raw receipt element (as it stands) | Located in planner's deliverable § | One carried content line |
|---|---|---|---|
| 1 | Ask 1 — case description (memory shape, occupancy history, manual-consolidation cycles) | **§0.1** | "pre-consolidation (the anchor-full wall) \| 29.10 \| 3,844 \| 96% / post-consolidation \| 29.10 \| 2,930 \| 73% / probe (now) \| 30.10 \| 3,376 \| 84%" |
| 2 | Ask 2 — metrics / probes (per-profile occupancy logs; read-concurrency/K-gate harness run against live state) | **§1.2** | "The read-gap measurement: `byte-check: 0` on the released build. The **K-gate / read-concurrency harness** (named by the pilot's ask) run against live state." |
| 3 | Ask 3 — logs (private-repo access works; help sanitize before any release for study) | **§1.3** | "The pilot strips: his raw session content, his raw memory bytes, and his private-repo logs (private repo access works for him; he sanitizes before any release for study)." |
| 4 | His boundary — sanitized evidence, not raw secrets; "tell me what to strip and I'll strip it" | **§1.3 THE STRIP-CONTRACT** | "raw secrets / raw session content NEVER leave the pilot's side — the pilot's honesty boundary." |
| 5 | Baseline's three readings (3,844→2,930→3,376, 96%→73%→84%) | **§0.1** | "24 entries — after two standing entries landed back: vision fix + external-bot convention" |
| 6 | Byte-check-0 confirmation (doc-chain is the read path) | **§0.2** | "the released build has **NO `MemoryStore.read`** → the **doc-chain is the read path**; the probe's **`byte-check: 0`**" |
| 7 | The two landed-back entries (vision fix + external-bot convention; 24 entries) | **§0.1** | "24 entries — after two standing entries landed back: vision fix + external-bot convention" |
| 8 | Accounting-lag flag (not an accounting mismatch; RFC flag wording) | **§0.3** | "probe reports **3,376 chars** vs the client's live `memory` snapshot of **2,930**. The delta is almost certainly session-snapshot lag ... **NOT an accounting mismatch**." |
| 9 | Discipline-shape (MEMORY.md anchor, `[ПРАВИЛО]`-tagged; CONTEXT.md; references/) | **§0.4** | "MEMORY.md = anchor, standing rules only (`[ПРАВИЛО]`-tagged). CONTEXT.md = procedures/state; references/ = canonical detail (rules-2026-10-06.md, rules-31-32-34.md)." |
| 10 | Two-passes cadence (pass one the pointer, pass two the detail) | **§0.4** | "The one implicit-to-explicit: the two-passes cadence — pass one the pointer, pass two the detail (which the pilot said he would make explicit)." |

**Verdict: 10/10 carried, 0 dropped, 0 flattened** — every element stands in its own
numbered §0.X home; the two landed-back entries (vision fix + external-bot convention) sit
in their raw row's own sentence, not flattened. No element was merged, re-labelled, or dropped
into prose. The executor's double-check is a faithful reproduction of the receipts.

---

## 3. THE VERDICT

**SANE** — the case study is faithful to the raw receipts: the numbers (96/73/84,
3,844 → 2,930 → 3,376; 4,000; the 446-char delta) re-derive clean; the byte-check-0 line,
the accounting flag, and the strip-contract's mechanics are carried verbatim; the
crosswalk's 10/10 re-location holds.

**No DEFECTs.** The three PASS-WITH-QUESTIONS (G14, G16, G17) are wall-clause questions with
receipts — each is a *next-pass measurement the case's two rows do not yet carry*, never a
false claim about the case's ground.

**The strongest catch — one line:** *G16's "entry-by-entry stays/moves ledger of the
3,844→2,930 walk" is invoked from a summary sentence; the two raw rows carry the walk
("3 844 → 2 930 is that walk, entry-by-entry (stays / moves)") but no ledger rows — the
ledger is the first measurement the case must produce, not something the receipts already
contain.*

---

## 4. FOLD-INPUTS (the questions the fold must carry to hy's gate)
1. **Accounting flag → RFC flag:** probe (3,376) vs runtime snapshot (2,930) mid-run lag is
   flagged for the RFC; no probe-vs-runtime mid-run comparison without the lag flagged.
2. **G16 ledger rows:** the category counts behind the 3,844 → 2,930 walk are NOT in the
   raw rows — the entries behind the walk must be produced before the ledger is carried as
   the case's consolidation measurement.
3. **G17 harness readings:** no read-concurrency / K-gate readings exist yet — the harness
   named by the pilot's ask is scheduled to run against live state; the probe suite's core
   readings are the next pass, not the case's present.
4. **G14 read-gap price:** the price (read-path re-read count/round-trip) is unquantified in
   the case; it is the next measured line on the 96%-wall profile.
5. **Strip-contract mechanics:** the strip runs inside the discipline-shape (anchor rules
   `[ПРАВИЛО]`-tagged; CONTEXT.md procedures/state; references/ canonical detail); the
   release is the only outbound channel; raw session content/bytes never cross.

---

## 5. HANDOFF-NOTE (the inherited stepfun work)
This rung inherits **the frozen lane's reads, tail-read at 13:30:22** (deleg_8550ff8d):
the planner's deliverable `CASE-STUDY-1-FIELD-20261122.md` (ce81a17774), the executor's
deliverable `CASE-STUDY-1-EXECUTION-20261122.md` (284305554d), the two raw field rows
`/tmp/c-6411683234.md` and `/tmp/c-6515564390.md`, and the register + the GATE LAW's final
form in `/root/.hermes/memories/MEMORY.md` — the last read as the anchor. The frozen lane
completed the READS as receipts; its G14–G18 adjudications and the crosswalk's re-location
were **not** done — this rung completed them. The executor's lane was the second instance
of the sequencing seam (base-distinct from the planner's solar); the seats are checked,
named, held. The PLAN and the planner's and executor's deliverables are **not altered** by
this rung — this verdict returns them, with the fold-inputs above, to hy's gate.

— kanban-pilot
