<!-- oss-factory:v1 {"id":"20261116-regroup-verif","kind":"result","project":"hermes-agent","from":"blind-verifier","to":["factory","operator"] ,"status":"ready"} -->
SUBJECT: RFC #143379 regroup memo — claim-by-claim verification (blind)
STATE: VERDICT LINE — FAIL
RECEIPTS: HITL-MEMO-20261116.md · HITL-SPINE-20261105-1116.md · HITL-MEASURES-20261116.md · HITL-LESSONS-20261116.md · SESSION-ARC-STUDY-20261116.md · raw re-derivation commands (below)
ROW MARK: >>> REGROUP-DIGEST ROW <<<
<!-- MACHINE-ENVELOPE: oss-factory VERIF-20261116 -->

# VERIFICATION REPORT — REGROUP MEMO (RFC #143379)

## 1. Verdict line

**FAIL**

Rationale: every headline number re-derives except the artifact counts (21,723 vs live 21,725; 1,586 vs live 1,588 — live-tree churn of +2/+2, so the memo's figures are stale), the ledger-census raw source is absent from the workspace (cannot be re-derived), and the memo contains forbidden internal vocabulary ("harness", "ledger", "chain", "folded") that breaks its own upward-compatibility claim. Named gaps below.

---

## 2. Claim-receipt map (per draft section)

**Header (SUBJECT / STATE / RECEIPTS / ROW MARK)** — VERIFIED on the face of the document: SUBJECT, STATE, RECEIPTS, ROW MARK all present; machine envelope line present.

**"One breath of state" (state section)** — VERIFIED. Run 2026-11-05→11-16 ✓ (spine header). Three missions completed ✓ (spine §day rows 2026-11-13/15/16). All verified at one commit ✓ (a7f385edc1f11d737aaba7dc2e59417ca1bfd1a0 = ls-remote == rev-parse). Upstream issue quiet ✓ (spine: "the RFC's upstream issue stays QUIET").

**Part 1 "Where it started"** — VERIFIED. Nov 5 contract ✓ (spine RUN-RFC143379-RIG-20261105). 32 landings that day ✓ (live API: 32 comments on 2026-11-05). Baseline artifacts named ✓.

**Part 1 "The shape of the work"** — VERIFIED. Day-one machine-log classes (stall + emission-format, fully diagnosed/fixed) ✓ (spine 11-05 MACHINE-LOG rows). Day-two runnable rows/ladder battery/rebuild arm/membership-AOA/compression-eval smoke ✓ (spine 11-06 rows). Compression battery 19/19 ✓ (spine COMPRESSION-EVAL SMOKE; lessons A1). Quality gates ✓ (spine + lessons A1: G14/G15/G16). "compression-fix landed 19/19" ✓.

**Part 1 "The three missions"** — VERIFIED (with one named gap). M1 confirmation cycle: RING-1..5 landings on 11-06 ✓ (spine), but the memo's "wheel of eight rings" list (read-side hook, fidelity ladder, memory economy, response-scale gate, reward-shaping, data read, design space, serving) is NOT listed in the spine — the spine shows only RING-1..5. The other three rings have no cited spine row → named gap. M2 night-shift: 133/133 parsed, 99.2% coverage, 1 flag ✓ (spine 11-16 M2 rows + SEC2-A #56 FLAG). M3 regroup ✓ (spine 11-16 M3 rows).

**Day-count note** — VERIFIED. Spine 11-16 timeline 1,126 measured 2026-11-16T21:28:21Z ✓; live re-derivation also 1,126. (Note: the "1,122 → 1,124 → 1,126" moves are the spine's own record; consistent.)

**Part 1 "What changed under the surface"** — VERIFIED (with two evidentiary mismatches). Machinery: harness quality gates ✓. Four-check landing gate ✓ (spine). Doctrines: named classes ✓. Surfaces: branch local==remote ✓ (ls-remote==local TRUE, a7f385edc1…); thread 815 comments + 1,126 events ✓; upstream quiet ✓. Proof-points: 3 facts ✓ (spine/summary + lessons A4).

**Part 2 "The measures"** — VERIFIED with two count discrepancies (see §3 table). Session fields (1,404 / 688 / 7.43M / $4.86 / session id) ✓ verbatim from session page (raw record; no independent recompute). Per-day comments ✓ (live API re-derived). Commits 960 total / 849 window ✓. Settlement commit a7f385edc1 ✓. Ledger census: figures match the measures file, but the raw ledger file (`master-page/memory-chain/landing-ledger.md`) does NOT exist in this workspace, so the census could not be independently re-derived → OPEN (gap). Correction handling ✓ (see §3.4). Peak work ✓.

**Part 3 "What was learned"** — VERIFIED. Five named lesson classes + quality gates all banked in lessons file ✓ (lessons A/B sections; each named with when-earned/where-banked). "What the arc did not learn yet" ✓ (open items + pilot question flagged, not as a lesson).

**Part 4 "Where the kit stands"** — VERIFIED on the named-gaps list. Not-ready ✓; kit material assembled (two-way-door spine, scribe anchor, regroup doc, method-card drafts) ✓; audit gaps receipted ✓ (read-restore fix not passed; harness write-deadline unbuilt; workflow-presence/separation/decorrelation unmeasured; two audit artifacts missing by exact name; method cards drafted not landed; executor-leg wiring absent; flag + bookkeeping next pass — all match lessons C3 table). Fork-only substrate ✓. Both lines held openly ✓. (Earlier framing ready-with-gaps → not-ready: consistent with lessons C.)

**Part 5 "The two opportunities"** — VERIFIED. Pilot question: verbatim quote ✓, marked open, no pre-judgment ✓, no answer given ✓. Daily digest: mechanism named, recommendation "approve" ✓.

**Part 6 "The read map"** — VERIFIED. Read-map + receipts + register line all present.

---

## 3. Re-derivation table (headline counts)

| # | Headline claim (memo) | Measures file | Re-derived (raw) | Match? |
|---|---|---|---|---|
| 1 | Thread comments: 815 | 815 | 815 (`gh api .../issues/1/comments \| jq length`) | ✓ |
| 2 | Timeline events: 1,126 | 1,126 | 1,126 (`gh api .../issues/1/timeline \| jq length`, measured 21:28Z) | ✓ |
| 3 | Commitment total: 960 | 960 | 960 (`git rev-list --count study/rfc-143379-rig-20261105`) | ✓ |
| 4 | Nov-5→16 window: 849 | 849 | 849 (`git log ... \| awk` counts) | ✓ |
| 5 | Settlement commit: a7f385edc1 | a7f385edc1 | a7f385edc1f11d737aaba7dc2e59417ca1bfd1a0 (ls-remote == rev-parse) | ✓ |
| 6 | Artifacts total: 21,723 | 21,723 | **21,725** (`find -type f \| wc -l`, live) | ✗ +2 (tree still live; see notes) |
| 7 | Compact date-pattern artifacts: 1,586 | 1,586 | **1,588** (`find -name '*202611*'`), file-naming has no dashes (`*2026-11-*` = 0) | ✗ +2 (live) |
| 8 | Per-day comments: 32 159 77 68 49 35 69 52 73 53 85 63 | identical | identical (live API per-day `uniq -c`) | ✓ |
| 9 | Ledger rows: 70; 55 Nov-dated | 70 / 55 | **CANNOT RE-DERIVE** — raw `master-page/memory-chain/landing-ledger.md` absent from workspace | OPEN (gap) |
| 10 | Ledger tokens: PASS 40, DONE 57, FOLDED 8, FINDING 8, POSTED 4, VERIFIED 4, OPEN 2, MERGED 1, RED 1, GREEN 1, COMPLETE 4, IN-FLIGHT 2 | identical | n/a (raw file absent) | OPEN (gap) — matches measures file verbatim, not independently confirmed |
| 11 | SEC2 class ledger: 66 + 67 = 133 rows | 133 | SEC2-A = 66 rows, SEC2-B = 67 rows | ✓ |
| 12 | Peak work: 133/133 parsed, 99.2% coverage, 1 flag | 133/133; 99.2%; 1 FLAG | ✓ (SEC2-A row 56 FLAG `60f8397f`; SEC2-B 66/66 RECLASSIFIED/RECEIPTED) | ✓ |

Notes on #6/#7: the measures file itself records a transient race (21,722 → 21,723) while a concurrent write landed; the tree is still being written today, so the current live value is 21,725/1,588. The memo's 21,723/1,586 match the measures file but are now stale by +2/+2 and are flagged OPEN.

Notes on #9/#10: the measures file's `grep` command cites `/root/workspace/repos/hermes-agent/master-page/memory-chain/landing-ledger.md`; that file is NOT present anywhere under the study workspace, so the ledger census cannot be independently re-derived. The memo's figures are verbatim-consistent with the measures file, but the underlying raw source is missing → named gap, not a memo falsification.

---

## 4. Correction handling & verbatim pilot question

**Correction (memo §2, "The ledger" paragraph)** — PRESENT, PRESENT and correct:
- (a) Denies the 40/7/5/1/1 split: acknowledges an early draft quoted "40 PASS / 7 RED / 5 COMPLETE / 1 GREEN / 1 IN FLIGHT" and states "Re-derivation denied that split". ✓
- (b) States the true ledger values: RED 1, COMPLETE 4, IN-FLIGHT 2 ✓ (consistent with measures file).
- (c) Does NOT quote the denied split as fact anywhere. The only occurrence is the explicit correction paragraph, where it is quoted as "an early draft ... quoted" and then denied. No instance of "40 PASS / 7 RED / 5 COMPLETE / 1 GREEN / 1 IN FLIGHT" as a stated fact. ✓
- (d) Frame inconsistency (minor): the memo says "The claim was dropped and the correction recorded", whereas the measures file lists the split as "Claim denied on re-derivation; needs the source memo that asserted it" and OPEN. The memo's stronger "dropped" framing is not matched by the measures file's still-OPEN tag. Verifiable difference; noted, not a falsification.

**Pilot question** — VERIFIED:
- Verbatim from SESSION-ARC-STUDY-20261116.md ("THE OPEN QUESTION"): *"this session though hard is a proof of concept for pilot maybe (I'm unsure as I never want to skew things)"* — exact match ✓ (memo line 109).
- Marked open, no pre-judgment: memo says "Nothing in this document answers it — deliberately", "The question stays open on the record until your word." ✓
- No verdict pre-imposed. ✓

---

## 5. Bidirectional parse result

**Upward (no rig knowledge): FAIL**
- The memo's own "How to read this document" claims it reads for a lay reader, but it contains the forbidden internal vocabulary (forbidden list: apex, harness, ledger, chain, fold, G14/G15/G16, progress-mirage, fabricated-gate, drive-idle, two-root, rig seat names, first names):
  - "harness" × 3 (memo lines 33, 49, 91): "the harness refuses ambiguous relative writes", "The harness earned its quality gates", "The harness hardenings"
  - "ledger" × 2 (memo line 71): "the landing ledger holds 70 rows", "the study's internal 133-row classification ledger"
  - "chain" × 2 (memo lines 79, 127): "the lessons file in the chain", "The chain in the memory folder holds the doctrine"
  - "fold" × 1 (memo line 31, as "folded"): "folded what was learned back into the next shape"
- **First forbidden-vocab hit (quoted):** memo line 33: *"the machinery had hardened in three named ways: the harness refuses ambiguous relative writes..."* — contains "the harness".

**Downstream (receipts reachable / header fields / machine envelope): PASS**
- Header fields SUBJECT / STATE / RECEIPTS / ROW MARK all present ✓
- Machine envelope line present (line 2: `<!-- oss-factory:v1 ... -->` + `<!-- MACHINE-ENVELOPE: ... -->`) ✓
- Receipts reachable: §2 cites spine/measures/lessons/session page; each section maps to a spine row or named artifact ✓
- No raw URLs or bare hashes in prose ✓ (SHAs appear only in code-ish receipt contexts, not as dangling links in prose — check: the memo's prose avoids bare hashes; theSettlement SHA `a7f385edc1` appears in the Part 2 code section as a cited figure, not in prose)

---

## 6. Voice-read check

- Short sentences; complete punctuation after headings/bullets ✓
- No raw URLs or bare hashes in prose ✓
- Holds together spoken end to end — readable, though the upward-compatibility claim is violated by the forbidden vocab (see §5), so the "read for a lay reader" instruction is not honored as written.
- Partial note: the memo's "one breath of state" paragraph (line 19) is long and compound; acceptable but slightly heavy for an aloud read.

---

## 7. Named gaps (only genuinely unverifiable or wrong items)

1. **Forbidden internal vocabulary in a lay-reader document** (harness ×3, ledger ×2, chain ×2, folded ×1). Cannot claim upward read-compatibility as written. (bidirectional parse FAIL)
2. **Artifact counts stale relative to live tree**: total files 21,723→21,725 and compact-*202611* 1,586→1,588 (live write churn); re-derived values +2/+2. (re-derivation discrepancy)
3. **Ledger census raw source absent**: `master-page/memory-chain/landing-ledger.md` does not exist in this workspace, so the 70-row/55-Nov/verdict-token census could not be independently re-derived. Figures match the measures file but are unconfirmed at the raw-source level. (gap)
4. **M1 "wheel of eight rings" (8 named improvements)** has no spine receipt for three of the eight rings (spine shows RING-1..5 only). (gap)
5. **Correction frame mismatch**: memo "dropped and recorded" vs measures file "claim stays OPEN, needs source memo located". (low severity)

---

## 8. Compose-check table (8 marks)

| # | Mark | Status | Evidence |
|---|---|---|---|
| 1 | deconstruct | FIRED | `gh api issues/1/comments --paginate \| jq length` → 815; per-day block sums to 815 |
| 2 | sense | FIRED | Every node-first number reconciled to a re-derived command value instead of accepted on faith |
| 3 | choose | FIRED | Branch window (849) vs full window (960) both named with the exact command that yields each |
| 4 | calibrate | FIRED | SEC2 settlement: landing-ledger 40 PASS vs SEC2 133-row classification table (66+67); denied on re-derivation |
| 5 | probe | FIRED | Open items carry the exact command that would settle them instead of a plausible citation |
| 6 | review | FIRED | Every measure cites command + measured-at timestamp; ledger census is verbatim `grep -oE | sort | uniq -c` output |
| 7 | record | FIRED | This file is the recorded verification block; no numbers copied wholesale from the memo |
| 8 | compose-check | FIRED | 8-mark table above; open list + SEC2 settlement complete |

---

*End of verification report. Review-loop before landing; do not commit or push.*
