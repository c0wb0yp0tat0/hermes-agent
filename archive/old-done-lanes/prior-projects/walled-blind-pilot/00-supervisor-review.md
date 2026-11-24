# COMPLETE FINDINGS — Walled-Blind Compression Experiment (Waves 1–6)

**Compiled:** 2026-08-19 · **Host:** pve-1 · **Purpose:** full, uncondensed review record — every finding from the supervisor's review and all five worker research passes, verbatim from their on-disk deliverables.

---

## How to read this document

This file contains, **in full and unedited**:

| Section | Source file | Status |
|---|---|---|
| PART 0 — Supervisor's review | (this session, reconstructed verbatim) | Operative |
| PART 1 — Worker A, verification vs literature (harness batch) | `worker-A-verification-v2.md` | Operative |
| PART 2 — Worker A, verification (search batch) | `worker-A-verification.md` | Preserved-selected (Worker D audit) |
| PART 3 — Worker B, decision evidence (harness batch) | `worker-B-decisions-v2.md` | Operative |
| PART 4 — Worker B, decision brief (search batch) | `worker-B-decisions.md` | Preserved-selected (Worker D audit) |
| PART 5 — Worker C, external readiness (harness batch) | `worker-C-readiness-v2.md` | Operative |
| PART 6 — Worker C, external readiness (search batch) | `worker-C-readiness.md` | Preserved-selected (Worker D audit) |
| PART 7 — Worker C iteration 2, executable pre-share package | `worker-C-iteration2.md` | Operative — the share-side operative artifact |
| PART 8 — Worker D, audit of the disregarded batch | `worker-D-disregarded-audit.md` | Operative — verdict: PRESERVE-SELECTED |
| PART 9 — Master assessment (consolidation + execution plan) | `00-MASTER-ASSESSMENT.md` | Operative — synthesis layer |

**Provenance notes:**
- The three source documents under review (`loop-closure-six-pager-DRAFT.md`, `hermes-replicable-pattern.md`, `wave6-grading-finding.md`) are not re-printed here — they were supplied by the owner and are the object of the review; every finding below cites them.
- "Harness batch" = research executed with the browser-harness method (`BU_CDP_URL=http://127.0.0.1:9222 uvx browser-use`). "Search batch" = web_search/web_extract only. Both sets are preserved; Worker D audited the set-aside (search-batch) reports and their corrections are catalogued in PART 8.
- All online claims in every report carry their source URLs; grounding taxonomy (DOC-GROUNDED / ONLINE-GROUNDED / UNVERIFIABLE) is used per report.
- What remains UNVERIFIABLE from this host (on-disk artifacts on the original host) is stated in PART 0 §5 and PART 9 Part 6.

---

# PART 0 — SUPERVISOR'S REVIEW

*Reconstructed verbatim from the supervisor's review message of 2026-08-19, the first full pass over the three source documents. This review was performed before any worker was dispatched; the workers were blind to it.*

## Scope
Full read of all three; arithmetic re-derived by hand; cross-doc consistency traced claim-by-claim. Byte-level artifacts (seals, logs, audits, directory state) live on the other host — flagged as unverifiable from here rather than asserted.

## Bottom line
Coherent, honestly scoped, internally consistent on every headline number re-derivable from the documents. **One real discrepancy** (manifest seal hash) that needs a byte-level resolution on the other host, plus four minor editorial items. The epistemic discipline holds up to the standard.

## 1. Cross-doc consistency — verified

| Claim | Status |
|---|---|
| W1: 52.9%, 12/12, control caught 0/12 (teeth = can fail) | ✓ six-pager = pattern |
| W3: HURT ≤60%, cliff at 40%, B2 qualifiers die first | ✓ six-pager = pattern |
| W5: NO ADOPTION; 20-reserved PRESERVED; cliff between 20–30% | ✓ |
| W6: 17/17 near-ceiling; confab 4/4; deletion 3/4 (B4 INCONCLUSIVE); inter-rater 6/6 HIGH | ✓ six-pager = pattern = finding |
| B4 drift: ref-anchor P2=3/15 vs frozen 13/15 (P2=1), not patched | ✓ all three |
| Decision record: nothing adopted, KEEP FULL PROSE, G1–G4 open | ✓ six-pager = pattern §4 lifecycle |

## 2. Arithmetic re-derivation — all pass
- 17 real cells = 4 (b1) + 5 (b2) + 4 (b4) + 4 (b6) ✓; 25-cell audit = 17 + 4 DEL + 4 ctrl ✓
- base = P1–P4, total = base + P5 — every row in finding §3–§5 re-summed correctly (bases 10–12, totals 12–15)
- DEL verdicts under amendment-002 table: b1/b2/b6 docked-and-named → HURT ✓; b4 undocked → INCONCLUSIVE ✓ (correctly never PRESERVED)
- ctrl cells: P1=1 dock → TEETH under cl.1 dominance ✓; PASS at bases 9/10, FAIL at 8/7 — matches the rubric (PASS = base ≥ 9, no part 0, P3 & P5 ≠ 0) ✓
- Inter-rater 6/6 ✓; b4-20-unreserved no-op INCONCLUSIVE carried with no weight ✓

## 3. The one real discrepancy — wave-6 manifest seal
- **Finding** (the sealed record, full hash, four places): manifest seal = `6461c201…`, recomputed, round-trips; the post-O3 re-seal is `6461c201…`.
- **Pattern §5b**: the same post-O3 re-seal = `44a18890…`.
- **Six-pager §2**: "wave-6 manifest `44a18890…`; consult leg re-derived seal `6461c201…` — both verify." That labels `6461c201` a consult-leg re-derivation — contradicting the finding, which says it is the manifest's own verified seal.

Two different hashes for what reads as the same file. Unresolvable from the three docs — the discipline's own P10 says the FILE wins. Needs one recomputation on the other host: which hash is the current wave-6 answer-pack manifest seal (minus the seal section, am.§4 boundary)? One of the three docs carries a stale or mislabeled value.

Related question: the six-pager §5 closure added a W6 ledger line to MANIFEST — is that ledger a *different* file from the sealed answer-pack manifest? If the same file, `6461c201` cannot still round-trip post-closure.

## 4. Minor editorial flags
- **W2 row** in the six-pager table is "(per record)" — the only blank in the narrative; fill or footnote before sign-off.
- **Pattern §6**: "The original four items…" then lists **five**.
- **Six-pager §2** calls amendment-001 the "frozen dock predicate" — per the finding header and pattern §6, 001 is the instrument-validity controls amendment; the deletion-dock decision table is **amendment-002's** subject (001 cl.3 originated it). Loose label.
- "Cliff at 40%" (W3–5 merged row) sits next to W5's "true cliff between 20–30%"; a fresh reader could take the coarser number as final — add a pointer.

## 5. Not verifiable from here (on-disk claims)
Lottery seal reproducibility; 8/8 rulebook tests; byte audit 25/25; deletion logs; tokenizer loud-fail; ledger + experiment-conclusion edits; the seal recomputations. Not doubted — outside what these three files can prove.

## 6. Assessment
The genuinely strong parts: no adoption/permanence/generalizability claims; INCONCLUSIVE never counted as PRESERVED; drift reported loudly, never patched; controls in every batch; consult objections recorded and folded forward-only. That's the discipline working as documented.

Recommendation at the time: **resolve the seal discrepancy before the §5/§7 sign-off** — record hygiene, exactly the class of thing the intern leg caught at closure.

*(Later passes added: the grader-identity contradiction [local vs cloud backend — PART 7 §C2.3], the W1 "caught 0/12" ambiguity, cross-wave comparability under amendment-001/002, and the transform-unspecified 52.9% — see Parts 1–9.)*

---

