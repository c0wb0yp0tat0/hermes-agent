# CYCLE2-M15-CAPTURE-20261115 — the M1.5 capture probe (Improvement 3: the write-path lessons into the framework's method cards)

**Seat:** longcat · probe-at-fire · the improver loop's second pass. **Mechanism:** the Capture Pipeline (harvest → refine → distill → fold) applied to M1.5's receipts. **Gate:** the method-card draft reviewed by the head before M2's dispatch — IN-LANE from M1.5's landed stages; the M2 gate stands untouched.

## 1 · THE CAPTURE SPEC

**HARVEST — the four receipts (INLINE-crate):**
- **R1 · the live write + re-read byte-match.** `studies/rfc-143379-rig/SERENA-BORROWED-TRY-20261115.md` @ `ae468b13bf` (branch `study/rfc-143379-rig-20261105`). `POST /save_memory {"memory_name":"rig-borrowed-try-20261116T000647Z", …}` → `status: success`; `POST /get_memory` (same name) → **byte-identical** re-read. `[EXECUTED]` 2026-11-16T00:06:47Z, tunnel pid 72595 (127.0.0.1:24282). Success is not a postcondition; the re-read is.
- **R2 · the 500-as-gift contract discovery.** Same artifact @ `ae468b13bf`. Probe 1's guessed payload → **500 Internal Server Error**; the seam named: the dashboard.js payload is the contract's source (`memory_name` + `content`), never the guessed shape. The failure was received as data, not frustrated past.
- **R3 · the scribe's verified surface.** `studies/rfc-143379-rig/SERENA-FLEET-SCRIBE-20261116.md` @ `1089e7155f`. save→success, get→byte-identical; `last_execution` → `Task-2:SaveMemory, finished_successfully: true, task_id 2869270607056`; `get_tool_stats` live; 40+ tools at `get_tool_names`; honest limit: `list_memories` 404 at the root route.
- **R4 · the DOOR-CLOSES-TOWARD-ADOPTION verdict.** Same artifact as R1 @ `ae468b13bf`. The verdict rides the measured landing; the adoption fires freely — the only gates are public writes beyond PR #1 + gists; the symbol-level write proof is the leg's integration run (next).

**REFINE — the abstract shape.** M1.5-specific (the coordinates): the tunnel, the serena memory surface, the dashboard.js payload, the receipt names. Fleet-standard (the lessons): (i) a write is not a receipt — the re-read is; (ii) a probe's failure is a finding whose seam is read from the client's contract source; (iii) a third, independent receipt surface (the scribe's cells) makes any lane/seat a verifier; (iv) a door verdict rides the measured landing, never a promise.

**DISTILL — the four method-card entries (each with its source footnote):**
- **Card W · write-with-postcondition.** A write's postcondition is the re-read; the write is the attempt, the re-read is the proof. *Source: R1.*
- **Card B · read-back-byte-check.** The check is byte-identical / hash-equal, never the claim; the receipt name is the handle. *Source: R1 (+ R3's scribe re-read).*
- **Card J · JS-as-contract-source.** The client's payload shape is the contract; a 500 names the seam — review the dashboard's JS first, never a blind retry. *Source: R2.*
- **Card D · two-way-door verdict.** The verdict rides the measured landing (CONTINUE + next / DONE / BLOCKED); the adoption fires freely — the only gates are public writes beyond PR #1 + gists; the door is reversible by construction. *Source: R4 (+ R3's door).*

**FOLD — the cards' home (DRAFT, never a silent edit).** Two candidate homes, both `[ABSENT]` (content not read — the contract): `mechanism-of-mechanisms/docs/method-cards.md` and the living-home `mechanism-of-mechanisms-bridge/docs/method-cards.md`. The proposal lands as a draft naming its adoption gate: **the head's review before M2's dispatch**. The ADOPTION fires by the standing law.

## 2 · THE PROBE SHAPE (the falsifier)

(a) **Seed** the four receipts R1–R4. (b) **Run** the pipeline: harvest → refine → distill → fold. (c) **Measured criteria:** each receipt lands in ≥1 card with its source tagged (4/4); the distill preserves the honest markers (`[EXECUTED]`, the 500's seam); the fold's draft names its adoption gate. (d) **FLAG:** a receipt lost in the pipeline (harvested but cardless, refined but source-less) OR the distill invents a lesson no receipt supports → the capture is **FLAGGED**. Battery home: `fixes/falsifier-battery-20261104` — `[ABSENT]` (not located in the read paths; named, not verified). Class-corroboration, not adoption: the read-back byte-check is SELD's read-side evidence-plane verifier in the write lane; the fold's adoption gate is AskALCF's evidence-gated commit gate at the framework door; the invention-rate is MAPE's inventions-live probe.

## 3 · THE SOURCE-TAGGING TERM

Every distilled lesson carries its receipt's coordinates — **the artifact path + the commit** (never a vibe). R1/R2/R4: `studies/rfc-143379-rig/SERENA-BORROWED-TRY-20261115.md` @ `ae468b13bf`; R3: `studies/rfc-143379-rig/SERENA-FLEET-SCRIBE-20261116.md` @ `1089e7155f`; branch `study/rfc-143379-rig-20261105`. A lesson without its source is a claim; **the source IS the card's footnote.**

## 4 · THE METERS

- **capture-yield** = receipts with cards / receipts harvested = **4/4** (by the draft's design; the probe measures it).
- **source-fidelity** = lessons tagged with coordinates / lessons distilled = **4/4**.
- **invention-rate** = lessons without supporting receipts / lessons distilled = **0/4** (the FLAG's fuel).
- **fold-readiness** = the draft's gates named / the draft's sections = **1/1** (the adoption gate named).
- **the run record** — `[ABSENT]` unless the fold's execution lands.

## 5 · THE HONEST MARKERS + TWO-WAY DOOR

- `[ABSENT]` — the mechanism repo's method-cards current content (not read — the contract; the fold's target is a draft, never a silent edit).
- `[ABSENT]` — the probe's value, unverified until execution.
- The adoption fires by the standing law; nothing posts; the RFC + upstream stay QUIET.
- **If the capture invents (the FLAG):** the design note stands and the alternatives are named — the receipt-set re-read, the source-tag check — never forced.

**Loop-state: CAPTURE-SPEC'D + the fold's draft awaiting the head's review before M2's dispatch — the cards' adoption the chair's.**