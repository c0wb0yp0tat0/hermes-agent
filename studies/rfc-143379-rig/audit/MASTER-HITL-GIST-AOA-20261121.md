# MASTER-HITL-GIST-AOA-20261121 — the audit's methodology report on MASTER-HITL-GIST-AUDIT-20261121

**Route:** study/rfc-143379-rig-20261105 · RFC quiet (reads only) · write-window 8
**Audited file:** `studies/rfc-143379-rig/audit/MASTER-HITL-GIST-AUDIT-20261121.md` (committed `8e856c4c8059bacd316066d5230f0121a896f4fa` @ 2026-11-21 15:32:03)
**Ground (read-only):** the audit's own §1–§8, the master's fold `MISSION-BRIEF-MASTER-20261119.md` §7 (§7-s(4)–(6) name the voice-check door; §7-v records the compose), and the audit leg-ledgers.
**Scope:** the audit's methodology only — axis coverage (§2/§3/§4 all present with settle-conditions), verdict consistency (§6 ordered set vs the §2/§3/§4 verdicts), evidence reality (VERIFICATION-RECEIPT R1/R2/R3 re-checked against the actual files), and base independence (named constraint, recorded).

---

## M1 · Axis coverage — PASS

| Axis | Where | Settle-condition present |
|---|---|---|
| Assess | §2, marks A1–A5 (mix ratio / depth / doors / receipts / verdict lines), each with its own settle-condition, and the §7 settle-condition table re-lists them | Yes |
| Design | §3, with its settle-condition at §4's §3 | Yes |
| Probe | §4, with its settle-condition at §4's §4 | Yes |

The audit's §7 settle-condition table covers ASSESS, DESIGN, PROBE with explicit conditions. No axis is missing and each verdict section is bound to a settlement rule. **Axis coverage PASS.**

## M2 · Verdict consistency — PASS (no self-contradiction)

The audit's ordered verdict set (§6) and its three verdicts (§2 ASSESS, §3 DESIGN, §4 PROBE) are consistent:

- **ASSESS PASS** is a document-level verdict: the gist is prose-first with bullets at scan points (A1), renders the full arc whole (A2), has all doors except the voice-check (A3), every number traceable to a fold line / ledger row / sha (A4), and its verdict lines match the ledgers (A5). The A3 mark explicitly names the omission as a question for the operator under the wall clause — not a recalled number, not a re-derived claim.
- **DESIGN SOUND** is the shape verdict: §0 names the three movements + thesis, §2 carries the certified/measured/verdict triad, §3 carries the four decisions, §5 carries the doors, §6 closes with the next cards. The §5 "pilot gate / pilot start" split is a presentation redundancy, flagged, not a structure fault; the §7-s(6) sentence shows the operator's word as the single one-way gate.
- **PROBE VALID (scope-bounded)** is the method verdict: claim-by-claim trace, not re-derivation; the one non-reproduction (the voice-check door) is a question, not a verdict.
- **Consistency check:** ASSESS PASS (with one omission) ⇒ DESIGN SOUND ⇒ PROBE VALID (scope-bounded) is not self-contradictory; the audit does not claim the gist is delivered, only that it is a draft with a named missing door. §6(4) ("the gist is a draft with a missing door, not a delivery") ties the ordered set together.

No contradiction across the verdicts was found. The receipt errors in M3 are receipt errors, not verdict contradictions.

## M3 · Evidence reality — PARTIAL FAIL

Re-checked every hash/quote in the VERIFICATION-RECEIPT (R1/R2/R3) against the actual files (git ls-tree HEAD, sha256sum, grep) at HEAD of `study/rfc-143379-rig-20261105` (= commit `8e856c4c80`).

**R1 · artifact receipt — OK (all verified):**

- blob sha at HEAD `268038d77017155da90da3c3ff4ab35a749933da` ✓
- sha256 `b79f1edbb7280402faab39a14f60dc7ce5e56fa5b1556211b35baae891129a73` (12,128 bytes) ✓
- words (whitespace-split) `1831` ✓
- `git log -1 --format='%H %ad %s' --date=iso f0e5905c0c` → `f0e5905c0ccce689f0cbc35e5718d1fca5551975 2026-11-21T14:21:15-05:00` ✓

**R2 · ledger receipt — sha256 11/11 OK; blob @HEAD 6/11 OK; 5/11 WRONG** (actual blob @HEAD at the audited branch HEAD):

| Ledger | sha256 claimed | sha256 OK | blob @HEAD claimed | blob @HEAD actual | result |
|---|---|---|---|---|---|
| ASK-LEDGER-20261121.md | `9f1ee915...bc04` | OK | `6b381e218df39bac0cefc4e771aaf3cc923a207b` | `6b381e218df39bac0cefc4e771aaf3cc923a207b` | OK |
| REGISTER-LEDGER-20261121.md | `3a1148c6...ef6e` | OK | `8cda160611557336a6af47874a9556e52e752cf7` | `3f5dc36789ac8a63dc7ba4e7091cc9c9d1aed25d` | **MISMATCH** |
| KIT-INVENTORY-20261121.md | `72e8b98e...c5` | OK | `410241556087f4562699ce75db94a42c6dbf02bc` | `410241556087f4562699ce75db94a42c6dbf02bc` | OK |
| FATE-LEDGER-20261121.md | `6669467f...35` | OK | `838f8522d54d546ff22726bbb63babeb2357da73` | `838f8522d54d546ff22726bbb63babeb2357da73` | OK |
| CROSSCHECK-20261121.md | `5088a10c...d11` | OK | `4c105a7ad25c5d78da208e071ecc4fa45fdfa5eb` | `9f8c268a158b6d55bac52e70964f617db41dbe68` | **MISMATCH** |
| GOAL-VERDICT-20261121.md | `9533b398...6d62` | OK | `14615888efd2f8f9eb1f6334863d6b84684f4d30` | `14615888efd2f8f9eb1f6334863d6b84684f4d30` | OK |
| COST-LEDGER-20261121.md | `1077e4c7...98` | OK | `9d8d97a7286cab9ae45393cd4e00e3a728fe2325` | `9d8d97a7286cab9ae45393cd4e00e3a728fe2325` | OK |
| COST-LEDGER-20261121.json | `effa7f8c...7a` | OK | `0ff9acaf271132813e135b21c33a8f65e3033b65` | `0ff9acaf271132813e135b21c33a8f65e3033b65` | OK |
| LOSS-LADDER-AUDIT-20261121.md | `0ef9566d...ef` | OK | `fa4ff56a1a84c900a8c68ac69b2ab6ff11486c88` | `078b3b89898bf271a97309d0008ad65994f0ced5` | **MISMATCH** |
| LOSS-LADDER-AOA-20261121.md | `5341dd21...b7b` | OK | `078b3b89898bf271a97309d0008ad65994f0ced5` | `fa4ff56a1a84c900a8c68ac69b2ab6ff11486c88` | **MISMATCH** |
| PILOT-VERDICT-20261121.md (study root) | `ac3874a1...09aa` | OK | `d29e8e9f63d3a207564f48223be1e01f8f6f9a4c` | `285064eb74c977ce783a8610a2ccc37644b9fdd9` | **MISMATCH** |

Findings: sha256 of the 11 files all re-derive with `sha256sum`; the blob @HEAD table is wrong in 5 rows. REGISTER-LEDGER and CROSSCHECK carry stale blob SHAs; LOSS-LADDER-AUDIT and LOSS-LADDER-AOA carry each other's blobs (swapped pair); PILOT-VERDICT's claimed blob `d29e8e9f63d3a207564f48223be1e01f8f6f9a4c` is not a valid object in this repository (`git cat-file -t` fails — not a commit, tree, blob, or tag), while the actual HEAD blob is `285064eb74c977ce783a8610a2ccc37644b9fdd9`. These are receipt errors inside the audit's own VERIFICATION-RECEIPT — they do not contradict the audit's verdicts, but they are factual errors in the receipt that must be corrected before the receipt can be relied on as-is.

**R3 · claim-by-claim trace receipts — spot-checked, 13/14 OK; 1 citation inaccuracy.**

| # | Claim | Tool check | Result |
|---|---|---|---|
| 1 | "six sections + the one-breath", "1,831 words" | fold §7-v commit message + scanner count | OK |
| 2 | A 0.000 / B 1.000 / C 0.990, gate 1.0, sha `be7fc43e…` | fold §7-g (line 85); KIT-INVENTORY; GOAL-VERDICT | OK |
| 3 | read-restore suite 42/42 | fold §7-m; PILOT-VERDICT | OK |
| 4 | W2 separation measured 31/35 | fold §7-m | OK |
| 5 | release battery precision 1.0, FP 0, completeness 100%, `test_citation_arm.py 4/4` | fold + CROSSCHECK: fold has 1 hit, CROSSCHECK 0 | **citation inaccuracy**: the F2-citation-arm sentence is at fold `§7-j` (L3 landing), not `§7-v`; the fold's §7-v does not carry the F2-citation-arm line |
| 6 | 300+ gate FAIL on a probe scope bug | ASK-LEDGER Ask-11 row in gist | OK |
| 7 | economics 2,012,329 vs 550,287 = 3.66×; head-load 62,939 = 12% of 524,288; $0.0585 | COST-LEDGER + fold §7-s | OK |
| 8 | 132 lines / 7,100 bytes / sha `95f874da97` | fold §7-u | OK |
| 9 | weights rung NOT_RUN at n5; pre-reg `3fef99a4ef`, run `406958197b` | fold §7-p | OK |
| 10 | PR #141876, #116673 merged_at null; #135039, #69264 open | FATE-LEDGER (merged_at ×4) | OK |
| 11 | compaction staged-but-not-opened; release condition unnamed | FETCH-PENDING in CROSSCHECK (×12) + FATE (×15) | OK |
| 12 | stub: 0.65 not load-bearing, 0.8 restores the markers, re-entry ≈0.864 | LOSS-LADDER-AUDIT + LOSS-LADDER-AOA | OK |
| 13 | five gaps match fold §7-u (GAP-1 LANDED · GAP-2 READY · GAP-3 READY · GAP-4 READY · GAP-5 parked) | gist §5 table vs fold | OK |
| 14 | verdict lines (pilot PROOF-OF-CONCEPT; kit's independence; three movements' fates; five gaps) | fold + PILOT-VERDICT + GOAL-VERDICT | OK |

## M4 · Base independence — NAMED CONSTRAINT, recorded on the record

This AOA route is the delegation's shared pinned base `upstage/solar-mini4:free`. The spawn path is broken for an independent second leg: the audit-of-the-audit route is delivered through the same pinned base as the parent study leg, so it cannot claim a different compute/actor than the study leg, and the fold's own sentence ("the operator's read is the gate"; "the sessions that predated it — the gaps + the compose's lane — completed"; "the operator's restart remains the named unlock for the audit/AoA spawns") marks the audit/AoA spawns as restart-gated, not free-standing.

Consequence, recorded here: this AOA re-checks the audit's VERIFICATION-RECEIPT (grep + sha256 + tool output) and does not re-derive the audit's own tables; the audit's scope ("the audit's methodology only — never re-derive the audit's own tables") is respected. The ledger blob re-verification in M3 used the repository's own git objects, so the finding is on the record independently of the pinned base. This is a named constraint of the run, not a hidden defect and not a defect in the audit's published verdicts.

## M5 · Voice-check door — FOUND and verified on the record

The audit's one named omission is confirmed against the fold and the gist:

- Fold §7-s(6) names it: "...RFC quiet; the court's posting, the patrol's shape, the RFC's surface, and the gist's voice-check ride the operator's word." (fold line 95)
- Fold §7-s(4) adds the secret-gist review URL + the drop serve (card t_505521f2 completed; the operator's Telegram subscribed) — the gist contains none of: "secret" (grep 0), "t_505521f2" (grep 0), "drop serve" (grep 0), "voice-check" (grep 0).
- The gist's §5 table ("THE DOORS, PRESENTED", 9 rows) lists: GAP-1 read UX shape · GAP-2 reload-markers' discipline · GAP-3 300+ hard gate · GAP-4 compaction's release condition · GAP-5 weights rung's fire · the court drafts' posting · the RFC's surface · the autopilot's pilot gate · the pilot's own start. **No voice-check row.**

The audit's verdict stands: ASSESS PASS with one named omission — the voice-check door is a missing door, not a recalled number, not a re-derived claim. The guess is settled by the fold's own gate ("the operator's read is the gate").

---

## SETTLE CONDITIONS

| Axis | Verdict | Settle-condition |
|---|---|---|
| Axis coverage | **PASS** | Holds while Assess/Design/Probe are all present, each with its settle-condition; the audit's §7 table re-states them. |
| Verdict consistency | **PASS** | Holds while no self-contradiction exists across the ORDERED set (ASSESS PASS w/ one omission · DESIGN SOUND · PROBE VALID scope-bounded) and the §6(4) summary ties the set together. |
| Evidence reality | **PARTIAL FAIL** | Holds while every hash/quote in the VERIFICATION-RECEIPT re-derives against the actual files. sha256 11/11 OK; blob @HEAD 6/11 OK; 5/11 wrong (M3 table). The R3 citation inaccuracy (claim 5: test_citation_arm.py at fold §7-j, not §7-v) is a second receipt error. |
| Base independence | **NAMED CONSTRAINT** | Holds while the spawn-path constraint is recorded on the record here, named (delegation's pinned base upstage/solar-mini4:free), and not presented as a hidden defect. |
| Voice-check door | **FOUND** | Holds while the door is presented in the gist's §5 with its reversibility and who walks it, or the fold's §7-v "doors presented" retracts. The gist's §5 lacks it — the audit's single named omission is verified. |

## OVERALL METHODOLOGY VERDICT

PASS with findings. The audit's Assess/Design/Probe verdicts (assess prose-first, one named omission; design sound; probe valid scope-bounded) stand; the one named omission — the voice-check door — is verified against the fold's §7-s(6) and the gist's §5. The VERIFICATION-RECEIPT needs the 5 ledger blob @HEAD corrections (M3) before the audit's receipt table is accurate as written; the sha256 table (11/11) and all other R3 traces checked clean.

---

## HARD LINES

- Nothing public; RFC quiet; reads only; nothing posted beyond the study's own branch.
- This file is a grounded methodology report on the audit; it does not re-derive the audit's own tables or the gist's content.
- The only failure named in the audit is the voice-check door (A3) — verified: the fold's §7-s(6) names it, the gist's §5 table lacks it.
- The VERIFICATION-RECEIPT's ledger blob @HEAD table carries 5 wrong rows (REGISTER-LEDGER, CROSSCHECK, LOSS-LADDER-AUDIT/AOA swapped pair, PILOT-VERDICT); the sha256 table (11/11) and all R3 traces re-derived clean except claim 5's fold citation.
- Base independence: the spawn path is broken for a second independent leg; this route shares the delegation's pinned base `upstage/solar-mini4:free` — a named constraint of the run, recorded on the record, not a hidden defect.
- This file commits under the study's branch, author `kanban-pilot <pilot@rig.local>`.
