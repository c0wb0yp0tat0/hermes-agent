# LENS-OUTCOME-20261108 — the OUTCOME lens: what the study's record yields for RFC #143379

**Seat:** stealth/crouton-alpha · **Branch:** study/rfc-143379-rig-20261105 (fork-only; nothing public) · **Date:** 2026-11-08
**Gate:** the gate: nothing public without the user's word (verbatim, non-negotiable)
**Contract:** PROPOSALS ONLY — draft-material staged at homebase for operator approval; nothing proposed on any owner's surface; owners' surfaces stay theirs; external readiness is internal, never a license to post.
**Register:** receipts, never claims — a delta without its receipt is an opinion; a proposal without its owner-scope mark is drift.

---

## Ground carried (summaries, lean reads)

- PR #1 thread: 272 comments per `ALLPRS-READ-20261107.md` (later 282 rows per `FLEET-CYCLE-BODY-20261108-053342.md`); thread is the study's running machine-log: demand-age FAIL, scaling NO, constraints recency-truncate worst/pinning 0, competition NOT-CONFIRMED, archive FAIL, aliasing×proximity CONFIRMED-BOTH, ACES loop converged twice, kit-fold complete, read-restore fix+proof upstream.
- PR body: downstream-only verification record — improver-loop converged no-improvement proved twice; runner-matrix three surfaces receipted; kit first-shape complete; read-restore moved with real fix+proof upstream; sweeps hold honestly; frame landed; no upstream writes.
- Study verdicts: `RFC-GUIDANCE-20261105.md`, `GOVERNANCE-LENS-E2E-20261107.md`, `WAVE3-UNIFIED-FOLD-20261108.md` (READY-WITH-NAMED-SEAMS), `ACES-*` audits, `HONEST-WALLS-CENSUS-20261106.md` (40 markers), `EXP-PROBE-BANKS-CERT-20261106.md` (CLEAN), `NEGENTROPY-SWEEP-C-BUDGET-20261106.md`.

---

## The deltas — each receipted, each framed as the record's contribution in the collaborators' own register

Owner-scope key: `[OWNER: RFC-authors]` = for RFC #143379 discussion authors · `[OWNER: PR-authors #116673/#141876/#139606]` = PR-surface authors · `[OWNER: study/operator]` = staged here, operator decides.

### D1. K-recency hard window fails the RFC's own gate at 300+ cycles, at every horizon
- **Delta offered:** Replace hardness as proposed with the measured shape; the gate's bar stands, the probe's fixes apply to the probe not the bar.
- **Receipt:** `RFC-GUIDANCE-20261105.md` §The gate, measured 1: means erosion 4× +23.9 → +0.6pp, deep sub-zero excursions seed-universal; scaled-K underperforms fixed-K10 (arm: NO). PR-surface corroboration: `ALLPRS-READ` demand-age FAIL / scaling NO.
- **Register framing:** "The read restore (#141876) stays landing-order first — nothing above it can be certified without it; the gate's failures change what the memory-side must guarantee." — guidance §landing-path 1.
- **Proposal (staged):** draft wording for RFC discussion replacing hard-window hardness with pinned exact-literal path.
- **Owner-scope:** `[OWNER: RFC-authors]` — proposal only, not posted.

### D2. Excursions are aliasing × cumulative-proximity, not noise / not single-rivals
- **Delta offered:** Fault-class pair with predictor strength; field corroboration named.
- **Receipt:** `RFC-GUIDANCE-20261105.md` §2: evidence-mass predictor R² = 0.655 (bar 0.35); alias-only keeps minima deep; recent-mass alone raises them; RoPE 2605.15514 / Sirens 2609.26718 cited. `ALLPRS-READ`: aliasing×proximity CONFIRMED-BOTH.
- **Register framing:** fault-classes, not hunches — in collaborators' measurement language.
- **Proposal (staged):** add aliasing/proximity as named fault-classes in any RFC revision's failure taxonomy.
- **Owner-scope:** `[OWNER: RFC-authors]`

### D3. Constraint-pinning works; recency-truncation is the worst strategy (1.00)
- **Delta offered:** Pinned constraints survive at 0% violation; OLD-literal pins at ~0.18% token cost (~18 tokens vs field's ~47).
- **Receipt:** `RFC-GUIDANCE-20261105.md` §3 + §landing-path 2; field DSGC recency retains prerequisite chains in only 0.07 of runs. `ALLPRS-READ`: constraints recency-truncate worst/pinning 0.
- **Proposal (staged):** recommend pinned exact-literal path as gate-convergent answer.
- **Owner-scope:** `[OWNER: RFC-authors]` + `[OWNER: PR-authors]` for any pin-path PR.

### D4. Archive ID-known recall is the optimistic bound; admission is query-blind
- **Delta offered:** Even under optimistic bound, gate fails at every tested budget; honest guarantee = lifecycle correctness for pinned + calibrated abstention (field AUC 0.63–0.66; StageMem/DSGC shape).
- **Receipt:** `RFC-GUIDANCE-20261105.md` §4 + landing-path 3. Constructional re-adjudication (delta 2026-11-05): budget knob admits only demanded literal's ID (`probe_archive.py:93`) — toothless-knob class; exhaustive verdict requires competing-admission arm.
- **Proposal (staged):** do not enlarge budgets as fix; name lifecycle + query-time recall as the recovery locus.
- **Owner-scope:** `[OWNER: RFC-authors]`

### D5. Competition arm NOT-CONFIRMED, precision-added — rivals never face the K=10 window-hit path
- **Delta offered:** a* degenerate against the only path that matters; constructional seam named with bytes.
- **Receipt:** `RFC-GUIDANCE-20261105.md` DELTA 2026-11-05 item 2 (longcat lane, byte-verified).
- **Proposal (staged):** any competition claim must re-run with rivals on window-hit path before RFC reliance.
- **Owner-scope:** `[OWNER: PR-authors]` / `[OWNER: RFC-authors]`

### D6. Read-restore is landing-order first; kvnloo independently fixed same race class
- **Delta offered:** read() snapshots without writer's file lock; paused read can restore stale state after newer commit — 17 passing tests, reverted store fails regression.
- **Receipt:** `THE-UNDERSTANDING-20261107.md` (kvnloo corroboration); `FLEET-CYCLE-BODY-20261108-053342.md`: read-restore head carries real fix+proof upstream, PR open beside that motion; `ALLPRS-READ`: pilot gated on read-restore passing.
- **Proposal (staged):** treat read-path fragility as validated class with named fix, not only study observation.
- **Owner-scope:** `[OWNER: PR-authors #141876]` — study does not write upstream.

### D7. Composed state of #116673 + #141876 + #139606 is untested; xngg1021's four seam gaps unverified in composition
- **Delta offered:** No PR tests composed state; acceptance criteria = four seam gaps (batch-path bypass, standalone fallback guards, preserve_session ignored return dicts, doc=/read fallback).
- **Receipt:** `IMPROVEMENTS-1-20261107.md` §(c)+(d); `TRUSTER-E2E-20261107.md` Track 1 central; `GOVERNANCE-LENS-E2E-20261107.md` compose-check table gaps on governance/compaction lines.
- **Proposal (staged):** one track concentrates on composing+falsifying that single composed state (compose.sh → test-suite.sh → claim-check.sh → receipt-emit.sh), per `WAVE3-UNIFIED-FOLD-20261108.md`.
- **Owner-scope:** `[OWNER: PR-authors]` (composition) — staged as falsifier spec, never posted.

### D8. Governance line has no home: governed-compaction issue unopened, provenance-default invariant unowned
- **Delta offered:** provenance defaults to "unknown" at pipeline definition; archive-before-stub; reroute-to-chain-doc seam ownership ambiguous.
- **Receipt:** `GOVERNANCE-LENS-E2E-20261107.md` verdict GAPS, named gaps 1–5.
- **Proposal (staged):** open governed-compaction issue + assign provenance-default invariant owner — as draft material for operator, not filed.
- **Owner-scope:** `[OWNER: RFC-authors]` (governance line) / `[OWNER: study/operator]` for staging.

### D9. Honest walls: 40 markers inventoried; GitHub-hosted window NOT RUN; recitation-length class named not measured
- **Delta offered:** Census-complete inventory with settle-conditions — every NOT-RUN stays until receipt replaces it.
- **Receipt:** `HONEST-WALLS-CENSUS-20261106.md` (40 markers: 8 NOT-RUN, 8 UNMEASURED, 16 WALL-CLAUSED, 8 MARKED-OPEN); `RFC-GUIDANCE-20261105.md` honest NOT-RUN section.
- **Proposal (staged):** carry walls verbatim into any RFC-facing summary; do not smooth.
- **Owner-scope:** `[OWNER: RFC-authors]` — transparency delta.

### D10. Budget consolidation: four protected classes weighted, one-anchor necessary-not-sufficient (W2 empty-answer confound)
- **Delta offered:** decision-core w3.00 > clock/exec-time 2.83 > next-action 2.33 > scope 2.00; reserving `open_id is app-scoped` survives into summary_text yet answer "" in all 3 runs.
- **Receipt:** `NEGENTROPY-SWEEP-C-BUDGET-20261106.md` executive summary + walls W1–W7.
- **Proposal (staged):** protect decision-core verbatim first in any compaction budget the RFC blesses.
- **Owner-scope:** `[OWNER: RFC-authors]` (compaction line)

### D11. Probe-banks certify facts' PRESENCE (CLEAN), not depth-vs-density; battery at substrate-pin a996d4ad…
- **Delta offered:** Bank-protocol audit re-derived cells A (8 msgs) / B (2 msgs, 219239-char user) match ledger; honest wall stands.
- **Receipt:** `EXP-PROBE-BANKS-CERT-20261106.md` verdict CLEAN, fixture hashes 78b9917… / b808da1….
- **Proposal (staged):** cite as verification-strength receipt; do not overclaim depth separation.
- **Owner-scope:** `[OWNER: RFC-authors]`

### D12. ACES improver loop converged twice — no-improvement is the honest terminal
- **Delta offered:** 0 new improvements after convergence; stops are findings, not failures.
- **Receipt:** `ACES-REVIEW-20261107.md` corrections ledger; `ACES-AUDIT-C3-20261107.md` tally 11 CONFIRMED, stop-line NO-IMPROVEMENTS; `ALLPRS-READ`: improver-loop converged no-improvement proved twice.
- **Proposal (staged):** RFC-facing summaries should report convergence as terminal state.
- **Owner-scope:** `[OWNER: RFC-authors]`

---

## Compose-check table

| # | Step | Status | One line |
|---|---|---|---|
| 1 | Read PR #1 thread end-to-end (asc + paginate every page) | ABSENT (lane-bound) | git-only lane; no `gh api` — thread state carried via ALLPRS (272→282 rows) + FLEET-CYCLE, 400-mid-read protocol not executable here. |
| 2 | Read PR body | FIRED | ALLPRS-READ-20261107 §1: downstream-only, no upstream writes, pilot gated on read-restore. |
| 3 | Read study-folder verdicts | FIRED | 12+ docs read first-hand this pass: RFC-GUIDANCE, GOVERNANCE-LENS, WAVE3-FOLD, ACES-*, HONEST-WALLS, EXP-PROBE-BANKS, NEGENTROPY-BUDGET, IMPROVEMENTS-1, MINES, THE-UNDERSTANDING, VALUE-ADD, CROSS-READ, TRUSTER-E2E. |
| 4 | Receipt every delta | FIRED | D1–D12 each carries file+section/byte receipt; no evidenceless claim. |
| 5 | Owner-scope mark per proposal | FIRED | Every proposal tagged [OWNER: RFC-authors] / [PR-authors] / [study/operator]. |
| 6 | Proposals only, nothing on owners' surfaces | FIRED | All material staged in this file; zero upstream/PR posts made. |
| 7 | Staged at homebase, nothing public without operator's word | FIRED | Artifact at `studies/rfc-143379-rig/LENS-OUTCOME-20261108.md`; gate line verbatim in header. |
| 8 | Compose-check table present, eight steps FIRED/ABSENT | FIRED | This table — 7 FIRED, 1 ABSENT honestly marked with lane-bound reason. |

---

## Honest NOT-RUN / uncertainty

- GitHub-hosted window side: NOT RUN (per census rows 1–2, guidance) — not re-verified here.
- Recitation-length class: named, not measured.
- Thread end-to-end re-read: ABSENT in this git-only lane; carried summaries used, never invented.
- No upstream writes by this study; original authors retain ownership; guidance offered, never imposed.
