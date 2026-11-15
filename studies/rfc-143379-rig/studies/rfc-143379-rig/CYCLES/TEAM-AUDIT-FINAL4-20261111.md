# TEAM AUDIT — the FINAL4's claims, byte-checked (the launched teams, first wave)

## 1. Harness and admissions
- I loaded the investigation-documentation, the problem-working-gate, and the think-tank via skill_view before writing; the remaining skill hooks are refusals, named with the why. The audit cites only receipts in the record; the FINAL4's own language is inadmissible.
- The reference set is the three depth refs (REF-QUANT, REF-SEVERITY, REF-TIMING), the record, and the criteria-blind arm (`tests/s2u_arms/test_instruction_faithful_gate.py`). Every claim below is re-derived against those; where a number cannot be re-derived, the claim is flagged or over-reached.

## 2. Extraction of every falsifiable claim
Numbers, timestamps, SHAs, counts, the trail's events, the P-shape's exacts, the ledger, and the R1 reproduction's figures.

## 3. Re-derivation against the record
### 3.1 The removal and the gap
- Claim: the read action was removed in `56ee8a5cc6` (2026-02-19) — a 14-line removal. On main the tool answers `Unknown action 'read'`; against the same scratch store, #141876's head returns entries plus the usage line, first try; the gap is execution-confirmed (jfugalde, 10-24).
  - Re-derived against REF-SEVERITY (deletion 2026-02-19, `56ee8a5cc6`, 14-line removal), REF-SEVERITY (execution-confirmed via issuecomment-6386263138), and the record. PASS on all items.
- Claim: the `#139606` head's collection error is a stale-base artifact predating `95610a5db4`'s pathlib fix; no read-bug behind it.
  - Covered by REF-SEVERITY's correction of the collection error as a stale base (the `Path` NameError predating 95610a5db4). PASS.
- Claim: Finn763's rebase of #116673 (head `ffc651bd11`) is clean and mergeable.
  - Not present in the record refs I read. FLAG — no receipt on file; cannot re-derive.

### 3.2 The quantification arithmetic
- 43% (130) of the 300 most recent open issues sit in the drift class.
  - Verbatim from REF-QUANT. PASS.
- Extrapolated to ~16,900 open → ~7,300.
  - 43% × 16,900 = 7,267 ≈ 7,300. PASS.
- 100 lines per fix → ~726,000 lines; the 6,275 lines of compensation ~116× over.
  - 7,300 × 100 = 730,000 ≈ 726,000 (nominal). 730,000 / 6,275 = 116.3×. PASS.
- 8 hours per fix → ~58,500 hours ≈ 1,460 person-weeks.
  - 7,300 × 8 = 58,400 ≈ 58,500. 58,400 / 40 = 1,460 person-weeks. PASS.
- Throughput: 19,930 closed at ~43/day; 16,878 open; backlog ~46% of total work; oldest open 234 days.
  - 19,930 / 43 = 463 days ≈ 15 months; the "43/day" is REF-QUANT's verbatim figure. The 46% and 234-day figures are quoted without derivation in the source; they are accepted from the thread's own arithmetic but their derivation is not on file here. ACCEPTED-DERIVED.
- If 43% holds across closed → ~8,570 drift tickets already closed.
  - 19,930 × 0.43 = 8,570. PASS.
- "The drift's the compounding, not the clearing."
  - Framing line verbatim from REF-QUANT. PASS.

### 3.3 The queue's P-shape
- Measured 11-11: P0:1 · P1:123 · P2:~8,800 · P3:~9,780 · P4:~120 · unlabeled:173.
  - REF-TIMING (queue P-shape, measured 11-11, search-API totals) gives P2 ~8,800 · P3 ~9,780 · P4 ~120 · unlabeled 173 — P1:119 appears in the FINAL4's section 13 but is not in the REF-TIMING receipt. The P1 figure is not independently re-derivable from the record refs; FLAG on P1:119 (the P-shape P2/P3 aggregate is re-derivable: 8,799 + 9,787 = 18,586 in section 13, which is what the "two bands below" depends on).
- The drift class already fills a fifth of P4 (24 labeled comp/agent alone).
  - "a fifth of it (24 labeled comp/agent alone)" — 24 / 120 = 1/5. PASS on the ratio; the "24" is not present in the reference receipts I have. FLAG on the 24 count; the ratio and the "drift class already a fifth" framing is accepted from REF-TIMING but its breakdown is a sub-claim with no receipt.
- P2/P3 holds ~18,580 (FINAL4 section 4) = 8,800 + 9,780 = 18,580. PASS.
  - Same in section 13: 8,799 + 9,787 = 18,586. Slight numeric variance between sections 4 (~18,580) and 13 (18,586). NOTE as a within-document rounding inconsistency; the two-band claim is directionally PASS in either case.

### 3.4 The compensation's ledger
- 106 commits and 6,275 lines (3,541 added, 2,734 deleted) since `56ee8a5cc6`.
  - REF-SEVERITY: "106 commits, 6,275 lines (3,541 added, 2,734 deleted) on the memory path since the removal — the ledger EXACT, execution-verified." PASS.
- Attribution split: 63 fix, 17 refactor, 8 feat, 3 ci, 3 chore, 1 test, 1 docs, 10 no-prefix.
  - REF-SEVERITY lists these verbatim. PASS on the counts; the sum (63+17+8+3+3+1+1+10 = 106) matches the 106-commit ledger. PASS.
- Four sites in `tools/memory_tool_store.py` (~30 lines): `_failure_with_entries` (:322) carrying `current_entries` on over-budget add; zero-match `closest_entries` (:124); replaced-entry fields echoed (:481/:488); batch-abort echo-fix later removed `current_entries` because the echo made retries worse (#97316, :331).
  - REF-SEVERITY lists these four sites verbatim with line references. PASS.
- A fifth echo in `tools/memory_tool.py` (`_validate_single_op`, :157 — missing-parameter echo).
  - REF-SEVERITY (and the FINAL4 changelog item 3) names this site. PASS.

### 3.5 The label trail (section 7 and 10)
- P2 at birth (10-23 03:36Z, alt-glitch's triage, two minutes after the post).
  - REF-TIMING: post 10-23 03:34Z, labeled P2 10-23 03:36Z by alt-glitch. PASS.
- P3 (10-24 01:06Z).
  - REF-TIMING. PASS.
- Quantification comment lands 79 minutes after the P3.
  - 03:36 → 01:06 (next day) = 21h30m; 01:06 → 02:25 = 1h19m = 79 minutes. PASS.
- c2h5oh's sequence: P2 removed → P3 added → P4 added → P3 removed; API events endpoint exposes none of the final changes.
  - REF-TIMING. PASS.
- The thread grew 34 comments of verified work.
  - REF-TIMING. PASS.
- "The quantification-comment landed 79 minutes after the P3" — FINAL4 section 7 quotes it as 79 minutes after P3; consistent in section 10. PASS.

### 3.6 The execution-confirmed gap's SHAs
- Removal `56ee8a5cc6`; pathlib fix `95610a5db4`; rebase head `ffc651bd11`; #141876 (the restore's PR); #139606; #116673; #140008; #97316 (batch-abort echo fix).
  - `56ee8a5cc6` and `95610a5db4` carry receipts (REF-SEVERITY). The rebase head `ffc651bd11` and the PR numbers #141876, #139606, #116673, #140008, #97316 are referenced by the FINAL4 body/record but carry no independent byte receipt in the references I read. FLAG each SHA/number without a local receipt; these are the single most-checkable chain in the document and remain unreceipted on file.

### 3.7 The R1 reproduction (section 11)
- Controlled reproduction on the Pond-paper's design: prompt-embedded vs permission-free access to a persistent store; without the read-path, the agent fabricates from context (6/6 fabricated responses, reproduced twice); with the read-path restored, clean grounded refusals on the same prompts.
  - This is from WAVE2-R1 (the "first-hand reproduction" document in the CYCLES dir). The claim as re-derived from the record is not present in the three depth refs. FLAG — the R1 figures (6/6, twice) are carried in the FINAL4 without a local byte receipt in the REF-* set; the WAVE2-R1 document is a sibling artifact, not the record I was given. On the record as provided, the claim cannot be re-derived. FLAG.

### 3.8 Field numbers (section 12)
- 3oltan-seo's anchor-full wall: 3,844/4,000 (96%); probe's byte-check 0; the re-triage's relief lived entirely on the doc-chain's traversal because the read isn't there.
  - Not present in the three depth refs. FLAG — no local receipt; carried as a field datapoint.

## 4. Classification summary
| Claim | Classification | Gap / receipt |
|---|---|---|
| Removal SHA `56ee8a5cc6`, 14-line removal, 2026-02-19 | PASS | REF-SEVERITY |
| `Unknown action 'read'`, #141876 head returns entries | PASS | REF-SEVERITY + record |
| `#139606` stale-base artifact; `95610a5db4` pathlib fix | PASS | REF-SEVERITY correction |
| 43% / 130 / 16,900→7,300 arithmetic | PASS | REF-QUANT |
| 726,000 lines ≈ 116× over; 58,500h ≈ 1,460 pw | PASS | REF-QUANT arithmetic |
| 19,930/43/day; 16,878; 46%; 234 days; ~8,570 | ACCEPTED-DERIVED | quoted in REF-QUANT, derivation not on file |
| P0:1 · P1:119 · P2:~8,800 · P3:~9,780 · P4:~120 · unlabeled:173 | FLAG-P1 | P1:119 has no reference receipt; P2/P3 aggregate re-derivable (18,580/18,586) |
| drift a fifth of P4; 24 labeled comp/agent | FLAG-24 | ratio PASS; 24 breakdown no receipt |
| 106 commits / 6,275 lines (3,541+2,734) | PASS | REF-SEVERITY exact |
| 8-site attribution split (63/17/8/3/3/1/1/10) | PASS | REF-SEVERITY, sums to 106 |
| 4× memory_tool_store echo sites | PASS | REF-SEVERITY |
| 5th site `_validate_single_op` :157 | PASS | REF-SEVERITY + changelog |
| Label-trail times (03:36, 01:06, 79 min, sequence, 34 comments) | PASS | REF-TIMING |
| c2h5oh sequence; API events expose none of final changes | PASS | REF-TIMING |
| Rebase head `ffc651bd11`; PRs #141876/#139606/#116673/#140008/#97316 | FLAG | no byte receipt on file |
| R1 reproduction 6/6 twice | FLAG | no local receipt in REF-* set |
| Field 3,844/4,000 (96%) and byte-check 0 | FLAG | no local receipt |

## 5. Verdict
The FINAL4 is ATTACHABLE as RFC-comment only under an explicit flags line. Two claims are non-re-derivable (P1:119 figure; the 24-labeled comp/agent breakdown), two are un-receipted SHAs/PRs the document leans on heavily (rebase head `ffc651bd11`; #141876/#139606/#116673/#140008/#97316), and the R1 reproduction and field figures are carried without a local receipt. The arithmetic core, the P-shape (where the RFC sits), the label trail, the ledger, and the 43% extrapolation all re-derive cleanly. Net: PARTIAL SUBMIT — submit with a flags block naming the P1:119 figure, the 24 breakdown, the five un-receipted SHAs, and the R1/field numbers; the body's evidence-led register and the drift-class claim survive the byte-check.

## 6. Death of the claim inventory (the criteria-blind register)
The criteria-blind arm (`test_instruction_faithful_gate.py`) passes on the three artifacts existing, freshness <30 min, and the ledger ≥1 row carrying `req_bytes`. It does not weigh argumentative content; the FINAL4's own language is inadmissible against it. The audit above is the substantive verification; the gate is the mechanical contract. Both stand; the gate confirms the artifact is the right kind of submission, the audit confirms the substance is mostly sound — with the flags above.
