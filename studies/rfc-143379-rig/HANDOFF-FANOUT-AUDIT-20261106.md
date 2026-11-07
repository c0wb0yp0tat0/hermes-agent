# HANDOFF-FANOUT — AUDIT LENS (eye 2/4): the receipts re-verification

**Study:** RFC #143379 · branch `study/rfc-143379-rig-20261105` (fork-only; nothing public).
**Audit seat:** this file. **Source doc re-verified:** `NIGHTSHIFT-HANDOFF-20261107.md`.
**Ground rule:** re-derive every receipt from the branch + the thread + the ledger. Never from the
doc's self-report and never from eye-1's verdict. Verdict classes: CONFIRMED (reproduced) / REJECTED
(byte-difference) / NUANCED (boundary).

---

## A. Receipts ledger re-verification (the 8 numbered products in the handoff doc)

### A1. The negentropy sweep 3/4 (A · B · C) — REJECTED / NUANCED (boundary)

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| A — `ab57948466`, RESERVATION-DOES-NOT-LIFT (local-lift/global-zero) | `git rev-parse --verify` → OK (local); `git ls-remote origin` → **NO** for `ab57948466` on `refs/heads/study/rfc-143379-rig-20261105`. The SHAs ride the remote only as handles; the commit itself is not on the study branch. | **NUANCED** — the name exists in the ledger/canon, the byte point is held, but the SHA is not a live commit on the remote branch. |
| B — `6524d1c5cd`, k-term two-tier: non-suppressed anchors 0.75 vs W2-empty 0.29 | `git rev-parse --verify` → OK (local); **NO** on remote. | **NUANCED** — same boundary: the value pair is on the record but the SHA is not branch-bound. |
| C — `3ddd351070`, budget consolidation (four protected-classes + loss-weights + one-anchor necessary-not-sufficient) | `git rev-parse --verify` → OK (local); **NO** on remote. | **NUANCED** — same boundary. |
| D — W2-isolation run-design, NOT LANDED (429/401/401/read-sink) | NOT-RUN in ledger; `RECEIPTS.md` carries no D receipt. | **CONFIRMED** (the doc's own negative is reproduced). |

**Overall A–C:** the three SHAs ride the doc but do not ride the remote of the study branch; the handoff
doc's own "all landed + rowed" is too strong. The values are on the record; the commits are not on the branch.

### A2. The operator-comment's eye-chain: CLOSED + POSTED (`6701129752`)

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| Comment id `6701129752` (the fluent-hallucination mechanism-comment) | `git rev-parse --verify 6701129752` → **fatal: unknown revision** (no such commit in the repo). `git ls-remote` for `6701129752` → no match. | **REJECTED** — the comment id is not a commit on the branch, and the thread-side read (the eye-chain vet → fixes → audit → fixes-2 → AoA voice-pass) cannot be re-derived from the branch. The chain's name is on the record, the id is not branch-bound. |

### A3. The citation-canon: 31 handles VERIFIED + 2 ORPHANED run-ids CAUGHT

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| 31 handles VERIFIED + 2 ORPHANED run-ids `42250764897` · `42229976556` now receipted (`440270349e`) | The CITATION-CANON-20261106 table shows the 31 handles VERIFIED (all `git rev-parse` OK, all `git ls-remote` YES for the study branch), but the two run-ids have NO ledger-row in `RECEIPTS.md` (NO / ORPHANED). | **NUANCED** — the 31-handle count reproduces; the two orphans were CLOSED only against the canon table, not against the ledger. The handoff doc says "now receipted" — that is not reproduced on the branch: the canon table is the receipted record, and the ledger rows are absent. |

### A4. The honest-walls census: 40 markers (8 / 8 / 16 / 8)

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| CENSUS-COMPLETE, 40 markers (8 NOT-RUN · 8 UNMEASURED · 16 WALL-CLAUSED · 8 MARKED-OPEN) | `HONEST-WALLS-CENSUS-20261106.md` enumerates 40 rows with settle-conditions; the sub-list is under-specified (3 entries with a named class but no fixed experiment). | **NUANCED** — the count reproduces (40), the class split reproduces (8/8/16/8), but 3 markers are UNDER-SPECIFIED (settle-condition is a named class, not a fixed experiment). |

### A5. The sessions-verification: 7 head-sessions + 135 machinery

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| 7 head-sessions (~14h41m closed + 1 open) · 135 machinery (22 subagent-lanes · 108 crons · 5 shadows) | `SESSIONS-VERIFICATION-20261106.md` re-derived from `sqlite3 /root/.hermes/state.db`: 7 heads (criterion a: `agent:main:telegram:dm:8940178054`, parent NULL, msg>=3, started>=2026-11-05T16:00Z); 22 subagent-lanes + 108 crons + 5 shadows = 135. | **CONFIRMED** (the ledger reproduces from the store) — sub-clause: 3 of 7 durations await the messages-table re-check (`c845488c0e`, PARTIAL). |

### A6. The volunteer-loop LIVE

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| Pilgrim onboarded; his posts flow the sanity-gate; each completed leg earns the next gist | The branch has `GIST-SANITY-20261106.md` (four real defects, FIXES-NEEDED) and an eye3-sanity vest (`GIST-SANITY-EYE3-20261106.md`); the loop is live in the thread but the run-side ledger has no Pilgrim-specific receipt row. | **NUANCED** — the protocol is banked; the live-loop posture is on the record in the thread, but no ledger receipt for the loop's own legs exists on the branch. |

### A7. The negentropy D-run-design (re-fire) — NOT LANDED

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| D (W2-isolation run-design) NOT LANDED; four class-deaths (429/401/401/read-sink); bounded-skeleton re-fire = next-session's first arm | No receipt row for D in `RECEIPTS.md`; `W2-ISOLATION-STATUS-20261106.md` (sentinel) records the class-deaths. | **CONFIRMED** (the doc's negative is reproduced; the ledger agrees). |

### A8. The shape-contract on the thread (6699545792)

| Handoff-doc claim | Receipt source (branch) | Re-derived verdict |
|---|---|---|
| 6699545792 — the next-stage sequence's standing brief; every reader honors it | Not reachable on the branch as a commit; the thread-side record carries the brief. | **NUANCED** — on the thread, yes; on the branch, no commit-shaped receipt exists. |

---

## B. The audit's own defect-lens: the misfi-vehicle / the misattribution

- **Misfi-vehicle:** the SHA-heavy reading. The handoff doc asserts "all landed + rowed" (A1) and "now
  receipted" (A3) from doc-self-report. The branch re-derivation rejects the byte-level equality:
  `ab57948466`, `6524d1c5cd`, `3ddd351070` are not on the remote branch; `6701129752` is not a commit at all.
  The misfi is that the doc treats "on the record" as "on the branch."
- **Misattribution:** the citation-canon's "now receipted" implicitly attributes the two run-ids'
  closure to `RECEIPTS.md` rows; the ledger carries no such rows. The closure is the canon table's own
  repair, not a ledger receipt — a boundary, not a byte-match.

---

## C. Overall ledger

| # | Receipt | Verdict |
|---|---|---|
| A1 | Negentropy A/B/C — zero of the three SHAs on remote; values on the record | **NUANCED** (boundary) |
| A2 | Operator-comment `6701129752` — not a commit on the branch | **REJECTED** |
| A3 | Canon 31 handles — reproduced; 2 run-ids "now receipted" — ledger rows absent | **NUANCED** (boundary) |
| A4 | Census 40 markers — count + split reproduced; 3 under-specified | **NUANCED** (boundary) |
| A5 | Sessions 7 heads / 135 machinery — reproduced from the store | **CONFIRMED** (with PARTIAL sub-clause) |
| A6 | Volunteer loop LIVE — protocol banked; no loop-leg receipt on branch | **NUANCED** (boundary) |
| A7 | D run-design NOT LANDED — reproduced | **CONFIRMED** |
| A8 | Shape-contract 6699545792 — thread-only; branch-only posture | **NUANCED** (boundary) |

**Overall verdict:** PARTIAL — the handoff doc's negative claims (A7, D NOT LANDED) and one positive
claim (A5 sessions) reproduce exactly from the branch + the ledger; the positive claims that run on
doc-self-report (A1's "all landed + rowed", A2's comment id, A3's "now receipted", A4's under-specified
markers, A6's loop legs, A8's thread-only brief) are NUANCED with boundaries, and A2 is the only one that
carries a genuine REJECTED byte-difference. The misfi-vehicle is the SHA→remote equality assumption; the
misattribution is the ledger-row claim on the two run-ids.

---

## D. The register (the branch's own tree)

| Item | Local | Remote (`study/rfc-143379-rig-20261105`) | Status |
|---|---|---|---|
| `8b0a2af584` — night summary (EXP-SUMMARY-NIGHT-20261106) | OK | NO | NOT branch-bound |
| `6701129752` — operator-comment eye-chain id | NO | NO | REJECTED |
| `ab57948466` | OK | NO | NUANCED (boundary) |
| `6524d1c5cd` | OK | NO | NUANCED (boundary) |
| `3ddd351070` | OK | NO | NUANCED (boundary) |
| 31 canon handles | OK | YES | VERIFIED |
| run-ids `42064685359` · `42193148018` | — | — | ledger rows YES |
| run-ids `42250764897` · `42229976556` | — | — | NO ledger rows (ORPHANED per canon) |
| `6fea1f079a` — census settle-condition marker | — | — | on the record (census) |
| `c845488c0e` — sessions-verify | — | — | PARTIAL sub-clause |
| `440270349e` — the "now receipted" sha | — | — | not a ledger row in `RECEIPTS.md`; canon-citied only |
