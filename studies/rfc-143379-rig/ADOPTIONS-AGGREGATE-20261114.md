# ADOPTIONS-AGGREGATE-20261114 — R2 ADOPTION AGGREGATION (seat: longcat)

**Branch:** study/rfc-143379-rig-20261105 · **Date:** 2026-11-14 · **Contract:** AGGREGATE + VERIFY; nothing adopts itself.
**STEER-1 ack:** acted — every row below carries a file+line read first-hand; the prior artifact's uncited R4-x/UP-x rows are NOT carried (no reachable receipt).

## 1. THE REGISTER

### R2-A — A–H adoption table (PRIMARY RECORD)
Source `CYCLES/ADOPTIONS-20261112.md` L7–L14 (full, 1891B). The staged `REFS/ADOPTIONS-20261112.md` is a 418B stub with only C's execution paragraph (L4) — RECONCILIATION R-1. Class per the table note L16 ("A–D and F are internal-only acts"); E–H parked.

| ID | Class | Status | Substance | Source |
|----|-------|--------|-----------|--------|
| A | A | adopt-internal | stale FINAL5 gate receipt → re-point to FINAL8 in `test_instruction_faithful_gate.py` ARTIFACTS | CYCLES/ADOPTIONS L7 |
| B | B | adopt-internal | "40,094" vs "roughly forty thousand" → precision-pass to exact | L8 |
| C | C | adopt-internal (done 11-12) | ledger's off-root position → S2U_LEDGER env-seam documented as intended | L9; dedup REFS/ADOPTIONS L4; CONV-PLAN L94 |
| D | D | adopt-internal | METHOD-GUIDELINES measurement-integrity paragraph (criteria-exposure line; doc-edit only, no gate) | L10 |
| E | E | parked | falsifier-battery fixture comment (public-comment gated; internal battery-doc version drafted only) | L11 |
| F | F | adopt-internal | #139606 one-layer-ablation + frozen-safety test (battery-arm test, not a comment) | L12 |
| G | G | parked | #140008 consolidation-authority labels (needs the PR's own context) | L13 |
| H | H | parked | PARKED-NOTREADY-1's falsifier scoping (category-scoping gate) | L14 |

### R2-B — platform-drift rows (plan §4.3; status per C4)
Source `NEMO-DAY-PLAN-20261114.md` L59–L64; status override L117–L120. Per brief: UNGROUNDED-PENDING-CITATION, never adopted.

| Handle | Plan label | Status | Substance | Source |
|--------|-----------|--------|-----------|--------|
| monitor | ADOPT | ungrounded-pending-citation | change-detection gate; critical for drift reconciliation | DAY-PLAN L59 + L119 |
| continuity | ADOPT | ungrounded-pending-citation | task resilience post-auth failures | L60 |
| proxy | ADOPT | ungrounded-pending-citation | keyless OAuth routing (OpenRouter, Harbor) | L61 |
| migrate | ADOPT | ungrounded-pending-citation | clean deprecated settings (`worktree`, `secrets`) | L62 |
| fallback | PARK | ungrounded-pending-citation | unclear use case; verify vs `proxy`/`continuity` | L63 |
| moa | REFUSE→PARK | ungrounded-pending-citation | no integration path, lacks docs; C4 retracts REFUSE→PARK, named verification | L64 + L120 |

### R2-C — checked, zero adoption rows
- `REFS/NIGHT-OPS-APEX-REPLAN-20261113.md` — M1–M8; none adoption-shaped.
- `REFS/BRIEF-CROSSING-{DOWNSTREAM,UPSTREAM,COMPARE,SYNTHESIS}.md` — traveler briefs (prompts); no rows; `CYCLES/CROSSING-*.md` deliverables not in REFS.
- `REFS/S2U-MISSION-PLAN-NUANCE-20261111.md`, `REFS/BRIEF-AUDIT-S2U.md` — plan/brief; no rows.
- `IMPROVEMENTS-W1-20261107.md`, `LENS-OUTCOME-20261108.md` — proposals/reserve lists; no A–H rows (G-3).

## 2. THE RECONCILIATION
- **R-1 (staging truncation):** `REFS/ADOPTIONS-20261112.md` = 418B/4 lines (only C's execution, L4) vs `CYCLES/ADOPTIONS-20261112.md` = 1891B/18 lines (full A–H, L7–L14). The brief's "(418 bytes)" matches the stub. Both read. → O-1.
- **R-2 (moa):** DAY-PLAN L64 `moa REFUSE` vs L120 `REFUSE retracted → PARK` (same file, later correction). Status = PARK, ungrounded; verification owed.
- **R-3 (table location):** brief attributes the platform-drift table to `NEMO-CONVERGENCE-PLAN-20261114.md`; it is in `NEMO-DAY-PLAN-20261114.md` §4.3 (L59–L64). Convergence plan carries only the ADOPTIONS crown-residue row (L94).
- **R-4 (label duality):** ADOPTIONS Choice says ADOPT for A/B/C (L7–L9) while note L16 + brief shape say A–D/F adopt-internal. Reconciled: A/B/C ADOPT = internal-only = adopt-internal; no substantive disagreement, named.
- **R-5 (arc citation unverifiable):** CONV-PLAN L94 "Cited by B05/B06/B07/B08 arc rows" — no reachable REFS record carries it; branch holds only `CYCLES/ACES-AUDIT-B05-20261111.md` + `B06` (B07/B08 absent). Not searched (brief's no-arc-hunt rule) → O-3.
- **R-6 (seat/artifact):** DAY-PLAN §5 (L73) names this lane's artifact `ADOPTIONS-20261114.md`, seat `meituan/longcat-2.5:free` — consistent.

## 3. THE GAPS
- **G-1:** B05/B06/B07/B08 arc adoption rows (the "scattered records") — named by CONV-PLAN L94/L39; carried by no reachable file. B07/B08 absent from branch; B05/B06 originals at `CYCLES/` (outside read roots per brief).
- **G-2:** `CROWN-SLICE.md` — named in the brief's grounding order; absent from `REFS/` (verified: 9 files). In-repo original `HOSTED-ARCH/CROWN-SLICE-20261109.md`.
- **G-3:** reserve adoption decisions — `IMPROVEMENTS-W1-20261107.md` names 5-of-26 candidates (RFC opp 11, opp 1, opp 4, MACH opp 2, MACH opp 12) + 5 V3 edges; no class/status carried.
- **G-4:** C4 platform-drift docs citations (page-pull list) — absent; rows stay UNGROUNDED.
- **G-5:** crossing series' adoption echoes (CONV-PLAN L94) — `CYCLES/CROSSING-*.md` not in REFS; synthesis "not folded into the master synopsis" (L93).

## 4. THE OWED REGISTER (head's machine-side hand)
- **O-1:** restage the FULL `ADOPTIONS-20261112.md` (CYCLES, 1891B) into `REFS/`, or confirm the 418B stub is authoritative.
- **O-2:** restage `CROWN-SLICE.md` into `REFS/`.
- **O-3:** supply/restage the B05/B06/B07/B08 arc adoption rows (B07/B08 missing from branch).
- **O-4:** run the C4 page-pull verification (llms.txt → docs page → cite URL) for monitor/continuity/proxy/migrate/fallback/moa.
- **O-5:** carry the reserve's adoption class/status (IMPROVEMENTS-W1) if in R2 scope.
- **O-6:** R3 seat/logdir logistics (ring table vs C2/R2 rotation — probe at fire).

## 5. LOOP-STATE
`CONTINUE + R3 (FINAL5-8 fold)` — register complete for the reachable corpus; missing arc rows (O-3) and ungrounded C4 rows (O-4) are head-side inputs R3 must carry, not a reloop of R2. (Plan §5 reloop "incomplete or contested" is triggered for the C4/arc items only.)

**NEXT-LAUNCH — R3 (FINAL5-8 fold)**
- brief: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEXT-R3-FINAL5-8-FOLD.md`
- seat: `meituan/aura-2.5:free` (plan §5 ring table) — seat rotation applies; C2/R2 rotation would give `longcat`; probe at fire
- logdir: `/root/.hermes/lanes/rfc-143379-rig-20261114-r3-final5-8-fold-20261114/`