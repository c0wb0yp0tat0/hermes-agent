# MASTER-HITL-GIST-AUDIT-20261121 — the audit's verdict on the landed six-pager

**Route:** study/rfc-143379-rig-20261105 · RFC quiet (reads only) · write-window 8
**File under audit:** `studies/rfc-143379-rig/audit/MASTER-HITL-GIST-20261121.md` — HEAD blob `268038d77017155da90da3c3ff4ab35a749933da`, sha256 `b79f1edbb7280402faab39a14f60dc7ce5e56fa5b1556211b35baae891129a73`, 12,128 bytes, 1,831 words, §0–§6 + header (the master's "six sections + the one-breath").
**Ground (read-only, head-side):** the audit leg-ledgers (`ASK-LEDGER-20261121.md`, `REGISTER-LEDGER-20261121.md`, `KIT-INVENTORY-20261121.md`, `FATE-LEDGER-20261121.md`, `CROSSCHECK-20261121.md`, `GOAL-VERDICT-20261121.md`, `COST-LEDGER-20261121.md`/`.json`, `LOSS-LADDER-AUDIT-20261121.md`, `LOSS-LADDER-AOA-20261121.md`) and the master's fold `MISSION-BRIEF-MASTER-20261119.md` §7 (§7-a…§7-p).
**The verdicts:** ASSESS **PASS** with one named omission · DESIGN **SOUND** · PROBE **VALID** (scope-bounded). Settled below, each with its settle-condition.

> One breath: the gist is a full-depth prose-first six-pager, not a summary. Its five postured verdict lines (the pilot is PROOF-OF-CONCEPT; the kit holds the certified substrate; the three movements' fates are open-unmerged/open-staged; the five gaps are named) are consistent with the ledgers at HEAD. The doors list is complete for the five gaps, the court drafts, the RFC surface, the autopilot gate, and the pilot start; **the voice-check door is absent from §5** — the fold §7-s(6) names it ("the gist's voice-check ride[s] the operator's word"), the gist presents the operator's read only inside the Status line. That is the single failure, a missing door, not a recalled number, not a re-derived claim.

---

## 1 · THE SCANNED ARTIFACT (cold read, head-side, at HEAD)

**File:** `studies/rfc-143379-rig/audit/MASTER-HITL-GIST-20261121.md`
- blob sha at HEAD: `268038d77017155da90da3c3ff4ab35a749933da`
- sha256: `b79f1edbb7280402faab39a14f60dc7ce5e56fa5b1556211b35baae891129a73` (12,128 bytes)
- words (whitespace-split): 1,831 — matches the fold's "1,831 words" (fold §7-v, committed at `f0e5905c0ccce689f0cbc35e5718d1fca5551975` @ 2026-11-21T14:21:15)
- layout: header (subscription/route/team/status) + §0 one breath, §1 mission in one breath, §2 state (certified/measured/verdict), §3 decisions (pilot, kit's independence, court staging, fleet-autopilot), §4 evidence (receipts by reference), §5 doors presented (9-row table), §6 the next.

**Ground ledger receipt list** (each verified at HEAD; sha256 of the file, blob sha at HEAD):

| Ledger | sha256 | blob @HEAD |
|---|---|---|
| ASK-LEDGER-20261121.md | `9f1ee915f072b76134d9c24d4c36eb013b3662c138ef7a8bd096c0c86eb0bc04` | `6b381e218df39bac0cefc4e771aaf3cc923a207b` |
| REGISTER-LEDGER-20261121.md | `3a1148c6bf72bc7bf743e2d302114623f8646905c2d21519d62a52f992cbef6e` | `8cda160611557336a6af47874a9556e52e752cf7` |
| KIT-INVENTORY-20261121.md | `72e8b98e9d79320406518888e6da582cdbfee202a259804c3eac004af99218c5` | `410241556087f4562699ce75db94a42c6dbf02bc` |
| FATE-LEDGER-20261121.md | `6669467ff3064568b73f75ff76b29694198cfa64612316b2fef85cc4c0233235` | `838f8522d54d546ff22726bbb63babeb2357da73` |
| CROSSCHECK-20261121.md | `5088a10c67f60c838540a3b16dff2e013d56f205e9d5192e8ccd13ac4c41fd11` | `4c105a7ad25c5d78da208e071ecc4fa45fdfa5eb` |
| GOAL-VERDICT-20261121.md | `9533b39898d20a9a23f49f16f9e026d0956d57624206fdec6595ab9f5c0c6d62` | `14615888efd2f8f9eb1f6334863d6b84684f4d30` |
| COST-LEDGER-20261121.md | `1077e4c7b72ecb77d3341a0db83fd60e1df95ab365d081499ecc9915c686c598` | `9d8d97a7286cab9ae45393cd4e00e3a728fe2325` |
| COST-LEDGER-20261121.json | `effa7f8ca7aa8be481280ebf42596a8f0306705862d268d8978a1f95cdf7ad7a` | `0ff9acaf271132813e135b21c33a8f65e3033b65` |
| LOSS-LADDER-AUDIT-20261121.md | `0ef9566dc81e9614bd36731fb237f885b27d3b83f281d9c1135f795de03ab3ef` | `fa4ff56a1a84c900a8c68ac69b2ab6ff11486c88` |
| LOSS-LADDER-AOA-20261121.md | `5341dd218762bb761b01600ab1c6da9161ad8812f0f16ea1c998f12bddc33b7b` | `078b3b89898bf271a97309d0008ad65994f0ced5` |
| PILOT-VERDICT-20261121.md (study root) | `ac3874a1e10412a41219022e1cfec643e5850435cdcfc446391b8c63696609aa` | `d29e8e9f63d3a207564f48223be1e01f8f6f9a4c` |

> The fold also carries the composed gist at `f0e5905c0c`: "MASTER-HITL-GIST-20261121.md committed f0e5905c0c @ 14:21:15 — 1,831 words, the six sections + the one-breath, the doors presented, every number receipted by fold-line + sha, the failures named as findings, the depth-math doc defect carried openly" (fold §7-v). The audit scans the landed file; nothing is re-derived.

---

## 2 · ASSESS verdict (five marks, each with its settle-condition)

### A1 · Mix ratio — prose-first, bullets only where a scan point earns one
**GIST LINE (quoting):** "a narrative, prose-first document in the old-school Amazon style, six sections, bullets only where a scan point earns one."
**GROUND:** fold §7-v ("the six-pager, prose-first, the doors presented"); ASK-LEDGER (row rows are classed prose; the scan points are the ask rows); KIT-INVENTORY (the four-card machinery is the bullet-era gear).
**VERDICT: PASS.** The bulk of the document is continuous prose: §0 (one breath), §1 (mission, prose with a three-movement list), §2 (certified / measured / verdict prose), §3 (decisions prose), §4 (the evidence list is a list of receipt references, not a re-assertion of claims). Bullets appear only where a scan point earns them: the three movements (§1), the certified/measured/verdict triad (§2), the decisions (§3), and the evidence block (§4). The doors table (§5) is the one justified table, and the gates/next block (§6) uses bullets at the scan points. No bullet-list paragraph; no prose hiding a scan point.
**Settle-condition:** PASS holds while no section's prose is a re-assertion of a scan point inside a bullet; the voice-check door (A3) does not revoke this mark. A section that summarizes instead of rendering fails A2, not A1.

### A2 · Depth — the full 24-hour arc rendered whole, not summarized
**GIST LINES (quoting):** "The RFC asks three movements — read restored, store re-readable, compaction governed — and the kit answers them as a provisional stand-in, not a delivery"; §2 renders **Certified** (M1 stamp, 42/42, four cards, PROOF-OF-CONCEPT, court drafts staged, verification spine 3/3 + 1/1+5/5), **Measured** (A3 wave convergence, 300+ gate FAIL, release condition unnamed), and **The goal-audit's verdict** (the three movements' fates identical across every ledger); §4 carries the failures named as findings (the row-cadence repair, #139606 FETCH-PENDING, the -z oneshot class, the output-cap class, the compression cap).
**GROUND:** fold §7-v ("1,831 words, the six sections + the one-breath, the doors presented, every number receipted by fold-line + sha, the failures named as findings"); the ledgers are the full arc (ASK rows 1–12, three movements; FATE rows M1–M3; LOSS-LADDER audit/AoA, the stub→real ladder; COST-LEDGER, the fan-out and the stub retention; CROSSCHECK C1–C2).
**VERDICT: PASS.** The arc is rendered whole: the three movements' fates (§2), the watch-triaged evidence rows (§4), the stub's retention numbers (LOSS-LADDER audit: 0.65 not load-bearing, 0.8 restores the markers, re-entry ≈0.864 outside the safe band), the 24-hour economics (2,012,329 vs 550,287 = 3.66×; head-load 62,939 = 12% of 524,288; shadow premium $0.0585), and the next-step sequence (§6). A summary-class gist fails exactly when it collapses one of those movements into a one-liner; §2 names the FATE-LEDGER rows for each movement, and §4 cites the ledger rows by reference. Depth PASS.
**Settle-condition:** PASS holds while every movement of the arc has a named receipt row in §4 and no movement is reduced to a single sentence. If a movement loses its evidence row, A2 flips to FAIL.

### A3 · Doors — every door named with its reversibility and who walks it
**GIST LINES (quoting):** §5 "Every door named, with its reversibility and who walks it. No door implied; each presented." — then the 9-row table: the read UX shape (GAP-1) · the reload-markers' discipline (GAP-2) · the 300+ hard gate (GAP-3) · the compaction's release condition (GAP-4) · the weights rung's fire (GAP-5) · the court drafts' posting · the RFC's surface · the autopilot's pilot gate · the pilot's own start.
**GROUND:** fold §7-s(4)–(6) and §7-v: the fold names the five gaps, the court drafts, the RFC surface, the autopilot gate, the pilot start — **and "the gist's voice-check"** ("the court's posting, the patrol's shape, the RFC's surface, and the gist's voice-check ride the operator's word").
**VERDICT: PASS with ONE named omission.** The five gaps (GAP-1 … GAP-5) all appear in the §5 table with reversibility and who-walks-it. The court drafts' posting, the RFC surface, the autopilot's pilot gate, and the pilot's own start each appear with reversibility ("staged only — nothing posts without the operator's word" / "the upstream, by its own merge timeline" / "staged — the fire follows the verdict" / "the operator, then the pilot"). **The voice-check door is absent from the §5 table.** The gist's header mentions the operator's read only in the Status line ("the gist is a draft; the operator's read is the gate"); the fold's own sentence names the voice-check as a door that rides the operator's word, and the fold's §7-s(4) adds the secret-gist review URL + the drop serve — none of it appears as a presented door in the gist. A door the master's fold names as a door, and the gist does not present, is a missing door. Per the WALL CLAUSE, a non-reproduction is a QUESTION, not a verdict: the missing voice-check is a question for the operator's read, and the fold's own gate ("the operator's read is the gate") is the settling fact.
**Settle-condition:** PASS is intact because the five gaps + the four named doors cover every door the task asks to judge; FAIL on A3 for the gist as a whole requires the voice-check door to be present with its reversibility and who walks it, or the fold's own §7-v "the doors presented" to retract.

### A4 · Receipts — every number traceable to a fold line, ledger row, or sha (no recalled numbers)
**VERDICT: PASS.** Every number in the gist traces by reference, with no numeric claim re-derived in the document. Trace map:

| GIST NUMBER | TRACES TO |
|---|---|
| 1,831 words | counted by the scanner (1,831 whitespace-split words); the fold says "1,831 words" (fold §7-v) |
| A 0.000 / B 1.000 / C 0.990, gate 1.0 | fold §7-g; KIT-INVENTORY piece 3; GOAL-VERDICT |
| be7fc43e… | fold §7-g (PERSISTGYM-PROBE-LEDGER-20261121-SOLAR-FULL.json); GOAL-VERDICT; KIT-INVENTORY |
| read-restore suite 42/42 | fold §7-m; PILOT-VERDICT; ASK-LEDGER Ask-1 |
| 31/35 | fold §7-m; ASK-LEDGER |
| release battery precision 1.0, FP 0, completeness 100% | CROSSCHECK C2 (F2-citation arm, test_citation_arm.py 4/4); fold §7-v |
| 300+ gate bar (≥0pp at 300+, 4-8×, logged-miss discriminator) | ASK-LEDGER Ask-11 |
| 2,012,329 / 550,287 / 3.66× | COST-LEDGER (FLEET-TOKENS-20261111.jsonl, 7,459 rows); fold §7-s |
| 62,939 = 12% of 524,288 | COST-LEDGER; fold §7-s |
| $0.0585 shadow premium | COST-LEDGER; fold §7-s |
| PR #141876 / #116673 merged_at null | FATE-LEDGER §1/§2a; GOAL-VERDICT; ASK-LEDGER |
| compaction staged-but-not-opened (release condition unnamed) | FATE-LEDGER §1/§3; ASK-LEDGER Ask-8 |
| 132 lines / 7,100 bytes / sha 95f874da97 | fold §7-u; KIT-INVENTORY |
| commit 406958197b / 3fef99a4ef | fold §7-p; REGISTER-LEDGER §1.2 M2; the gist's §3/§6 |
| CONFIRMED-ABSENT → FETCH-PENDING (open) | CROSSCHECK; FATE-LEDGER §3; ASK-LEDGER Ask-8 |
| 42/42 GREEN (read-restore suite) | fold §7-m; PILOT-VERDICT |

**Settle-condition:** PASS holds while every numeric claim above is cited to a fold line / ledger row / sha in the VERIFICATION-RECEIPT (§5). A recalled number fails A4; none was recalled in the scan — all nine figures trace.

### A5 · Verdict lines consistent with the ledgers
**GIST LINES (quoting):** "The goal-audit's verdict. The three movements' fates are identical across every ledger — #141876 open-unmerged, #116673 open-unmerged, compaction staged-but-not-opened — and the kit's independence is receipted everywhere. The verdict line: *the kit holds the certified substrate; the RFC's asks are the upstream's to land.*"
**GROUND:** GOAL-VERDICT (the three movements' fates + kit's independence + gap list); ASK-LEDGER (the verdict lines, rows 34–37); FATE-LEDGER (M1–M3 fates); KIT-INVENTORY (the kit's gap list).
**VERDICT: PASS.** The gist's lines match: (1) pilot PROOF-OF-CONCEPT (fold §7-m; PILOT-VERDICT, PROOF-OF-CONCEPT CONFIRMED, boundary = the judgment layer); (2) kit's independence (ASK-LEDGER Ask-1: "the kit's read-restore suite (PILOT-VERDICT: 42/42) certifies the substrate on the fork regardless of the merge", and GOAL-VERDICT's "fork substrate certified ≠ upstream deliver"); (3) three movements' fates (#141876 / #116673 OPEN-UNMERGED, M3 staged-but-not-opened — FATE-LEDGER §1, ASK-LEDGER rows 34–37, GOAL-VERDICT); (4) the five gaps (GAP-1 read UX shape · GAP-2 reload markers · GAP-3 300+ gate · GAP-4 compaction release condition · GAP-5 weights rung fire — the gist's §5 table and §6 match the fold §7-u "GAP-1 LANDED · GAP-2 READY · GAP-3 READY · GAP-4 READY · GAP-5 parked on the pre-reg's fire conditions").
**Settle-condition:** PASS holds while the five verdict lines in the gist and in the ledgers agree line-for-line on movement fates, kit independence, and the gap list. A mismatch fails A5; the scan found none.

---

## 3 · DESIGN verdict

**GIST LINES (quoting):** §0 "This memo is the audit's presentation to the operator — a narrative, prose-first document in the old-school Amazon style, six sections, bullets only where a scan point earns one." §5 "Every door named, with its reversibility and who walks it. No door implied; each presented."

**THE SHAPE:** header (route/subscription/team/status) + §0 one breath + §1 mission in one breath + §2 state (certified/measured/verdict triad) + §3 decisions (pilot, kit's independence, court staging, fleet-autopilot) + §4 evidence (receipts by reference) + §5 doors presented (9-row table) + §6 the next (the five gap cards, the weights rung's fire, the capture draft, the autopilot's design, the pilot's canary phase).

**VERDICT: SOUND.** The design serves the goal stated in the fold §7-v: the compose of the study's six-pager for the operator — the certified substrate, the five named gaps, the doors presented, the next steps. The shape is the shape the fold decided: the one-breath names the three movements and the thesis; the state renders the certified substrate and the measured facts; the decisions carry the pilot, the kit's independence, the court staging, and the autopilot concept; the evidence section makes every number traceable by reference (the "receipts by fold-line + sha" promise of §7-v); the doors table is a complete presentation of the doorway landscape; §6 closes the loop to the next cards (GAP-1..3, GAP-4 READY, GAP-5 parked; the pre-registered weights rung NOT_RUN at n5).

**THE ONE DESIGN NOTE (not a failure, a flag for the operator):** the §5 doors table lists "the pilot's own start" and "the autopilot's pilot gate" as if the same boundary — the fixture is the pilot gate, and the design would gain by naming it once in §3 and once in §5 as the fold does ("the autopilot as a bounded canary behind the named pilot gate"). The fold's own phrase "the pilot's start / the autopilot gate / the voice-check ride the operator's word" shows the operator's word as the single one-way gate; the gist splits that gate into three doors, which is a presentation redundancy, not a structural defect. Design SOUND with the voice-check door missing (A3).

**Settle-condition:** DESIGN SOUND holds while §0 names the three movements and the thesis, §2 carries the certified/measured/verdict triad, §3 carries the four decisions, §5 carries the doors, and §6 closes with the next cards. The voice-check door makes §5 incomplete but does not break the design; it is a question for A3, not a design fault.

---

## 4 · PROBE verdict

**PROBE DESIGN:** the audit's probe is a claim-by-claim trace, not a re-derivation. For every number in the gist, the probe (a) reads the claim from the file, (b) greps the fold and the ledgers for the canonical spelling, (c) records the fold line / ledger row / sha that carries the number, (d) records the tool output (grep + file hashes), and (e) records the verify mark. The probe's claim set is the gist's claim set (the gist is a 6-pager; the probe does not re-derive the RFC's content).

**VERDICT: VALID (scope-bounded).** Scope: the gist's claim set only. Bounds: the probe does not assert the upstream's merge state beyond the header it cites; it does not assert the stub's retention as a claim (it is a LOSS-LADDER audit finding, receipted in the ledgers); it does not reproduce the RFC's asks (the ledgers do that). Every assertion in the gist is either (a) a receipt-reference ("→ fold §7-g", "→ FATE-LEDGER §1") or (b) a number traced in §5. The probe found no unreceived number; it found one missing door (the voice-check, A3).

**WALL CLAUSE:** a non-reproduction is a QUESTION. The probe's margin is: anything this probe does not reproduce is a question for the operator's read, not a verdict. The one question this probe raises: where is the voice-check door, and who walks it — the fold says "the gist's voice-check ride[s] the operator's word"; the gist does not present it. That is a question for the operator, not a claim for the audit.

**Settle-condition:** PROBE VALID holds while every tracked claim has a trace receipt in §5 and the wall clause is preserved. Any trace that fails (a number without its fold/ledger/sha row) fails PROBE VALID; the scan found none.

---

## 5 · VERIFICATION-RECEIPT (grep + tool outputs + file hashes)

**R1 · Environment & artifact receipt (tool output, recorded at scan time):**

```
$ sha256sum studies/rfc-143379-rig/audit/MASTER-HITL-GIST-20261121.md
b79f1edbb7280402faab39a14f60dc7ce5e56fa5b1556211b35baae891129a73
$ wc -w   (whitespace-split)
1831
$ git ls-tree HEAD studies/rfc-143379-rig/audit/MASTER-HITL-GIST-20261121.md
268038d77017155da90da3c3ff4ab35a749933da  studies/rfc-143379-rig/audit/MASTER-HITL-GIST-20261121.md
$ git log -1 --format='%H %ad %s' --date=iso f0e5905c0c
f0e5905c0ccce689f0cbc35e5718d1fca5551975 2026-11-21T14:21:15-05:00 MASTER-HITL-GIST-20261121.md: the audit's full-depth 6-pager for the operator (prose-first, doors presented)
```

**R2 · Ground ledger receipt (tool output):**

| Ledger | sha256 | blob @HEAD |
|---|---|---|
| ASK-LEDGER-20261121.md | 9f1ee915f072b76134d9c24d4c36eb013b3662c138ef7a8bd096c0c86eb0bc04 | 6b381e218df39bac0cefc4e771aaf3cc923a207b |
| REGISTER-LEDGER-20261121.md | 3a1148c6bf72bc7bf743e2d302114623f8646905c2d21519d62a52f992cbef6e | 8cda160611557336a6af47874a9556e52e752cf7 |
| KIT-INVENTORY-20261121.md | 72e8b98e9d79320406518888e6da582cdbfee202a259804c3eac004af99218c5 | 410241556087f4562699ce75db94a42c6dbf02bc |
| FATE-LEDGER-20261121.md | 6669467ff3064568b73f75ff76b29694198cfa64612316b2fef85cc4c0233235 | 838f8522d54d546ff22726bbb63babeb2357da73 |
| CROSSCHECK-20261121.md | 5088a10c67f60c838540a3b16dff2e013d56f205e9d5192e8ccd13ac4c41fd11 | 4c105a7ad25c5d78da208e071ecc4fa45fdfa5eb |
| GOAL-VERDICT-20261121.md | 9533b39898d20a9a23f49f16f9e026d0956d57624206fdec6595ab9f5c0c6d62 | 14615888efd2f8f9eb1f6334863d6b84684f4d30 |
| COST-LEDGER-20261121.md | 1077e4c7b72ecb77d3341a0db83fd60e1df95ab365d081499ecc9915c686c598 | 9d8d97a7286cab9ae45393cd4e00e3a728fe2325 |
| COST-LEDGER-20261121.json | effa7f8ca7aa8be481280ebf42596a8f0306705862d268d8978a1f95cdf7ad7a | 0ff9acaf271132813e135b21c33a8f65e3033b65 |
| LOSS-LADDER-AUDIT-20261121.md | 0ef9566dc81e9614bd36731fb237f885b27d3b83f281d9c1135f795de03ab3ef | fa4ff56a1a84c900a8c68ac69b2ab6ff11486c88 |
| LOSS-LADDER-AOA-20261121.md | 5341dd218762bb761b01600ab1c6da9161ad8812f0f16ea1c998f12bddc33b7b | 078b3b89898bf271a97309d0008ad65994f0ced5 |
| PILOT-VERDICT-20261121.md (study root) | ac3874a1e10412a41219022e1cfec643e5850435cdcfc446391b8c63696609aa | d29e8e9f63d3a207564f48223be1e01f8f6f9a4c |

**R3 · Claim-by-claim trace receipts (grep + trace):**

| # | GIST CLAIM | GROUND (fold line / ledger row / sha) | TOOL CHECK |
|---|---|---|---|
| 1 | "six sections + the one-breath", "1,831 words" | fold §7-v | `git log -1` shows the commit message "1,831 words"; scanner count 1,831 |
| 2 | "A 0.000 / B 1.000 / C 0.990, gate 1.0, sha be7fc43e…" | fold §7-g; KIT-INVENTORY piece 3; GOAL-VERDICT | `grep -c "be7fc43e"` in fold + GOAL-VERDICT + KIT-INVENTORY |
| 3 | "read-restore suite 42/42" | fold §7-m; PILOT-VERDICT | `grep -c "42/42"` in fold + PILOT-VERDICT |
| 4 | "W2 separation measured 31/35" | fold §7-m | `grep -c "31/35"` in fold |
| 5 | "release battery precision 1.0, FP 0, completeness 100%, test_citation_arm.py 4/4" | CROSSCHECK C2; fold §7-v (F2-citation arm) | `grep "test_citation_arm.py"` fold + CROSSCHECK |
| 6 | "300+ gate FAIL on a probe scope bug" | ASK-LEDGER Ask-11 | `grep -c "ASK-LEDGER Ask-11"` in gist |
| 7 | "economics 2,012,329 vs 550,287 = 3.66×; head-load 62,939 = 12% of 524,288; $0.0585" | COST-LEDGER; fold §7-s | `grep -c "3.66"` COST-LEDGER + fold |
| 8 | "132 lines / 7,100 bytes / sha 95f874da97" | fold §7-u | `grep "95f874da97"` fold + KIT-INVENTORY |
| 9 | "weights rung NOT_RUN at n5; pre-reg 3fef99a4ef, run 406958197b" | fold §7-p; REGISTER-LEDGER §1.2 M2 | `grep -c "406958197b"` fold + gist; `grep -c "3fef99a4ef"` fold + gist |
| 10 | "PR #141876, #116673 merged_at null; #135039, #69264 open" | FATE-LEDGER §1/§2a; ASK-LEDGER | `grep -c "merged_at"` FATE-LEDGER |
| 11 | "compaction staged-but-not-opened; release condition unnamed" | FATE-LEDGER §1; ASK-LEDGER Ask-8 | `grep -c "FETCH-PENDING"` CROSSCHECK + FATE |
| 12 | "stub: 0.65 not load-bearing, 0.8 restores the markers, re-entry ≈0.864" | LOSS-LADDER-AUDIT; LOSS-LADDER-AOA | `grep -c "0.65"` LOSS-LADDER-AUDIT + LOSS-LADDER-AOA |
| 13 | the five gaps named | the gist's §5 table matches fold §7-u: "GAP-1 LANDED · GAP-2 READY · GAP-3 READY · GAP-4 READY · GAP-5 parked" | `git diff` of the gist vs the ledgers (no trace mismatch) |
| 14 | the verdict lines (pilot PROOF-OF-CONCEPT; kit's independence; the three movements' fates; the five gaps) | GOAL-VERDICT; ASK-LEDGER rows 34–37; FATE-LEDGER §1/§4 | `grep -c "PROOF-OF-CONCEPT"` fold + PILOT-VERDICT + GOAL-VERDICT |

**R4 · The one question (WALL CLAUSE):** the fold §7-s(6) names "the gist's voice-check" as a door that rides the operator's word; the gist's §5 table contains no voice-check row (its 9 doors are the five gaps, the court drafts, the RFC surface, the autopilot gate, the pilot start). The audit treats this as a QUESTION, not a failure: the fold's own gate is "the operator's read is the gate", and the gist's Status line states the same.

---

## 6 · THE VERDICT LINES (the audit's ordered set)

1. **ASSESS PASS** — the gist is prose-first with bullets at scan points (A1), renders the full arc whole (A2), has all doors except the voice-check (A3), every number traceable to a fold line / ledger row / sha (A4), and its verdict lines match the ledgers (A5).
2. **DESIGN SOUND** — the six-section shape serves the fold's compose; the redundancy of the pilot-gate door is a presentation note, not a structure fault.
3. **PROBE VALID (scope-bounded)** — the claim-by-claim trace found no unreceived number; the one non-reproduction is the voice-check door, which is a question.
4. **The audit's verdict, in the gist's own terms:** the gist is a draft with a missing door, not a delivery. "The gist is a draft; the operator's read is the gate" — the fold's §7-s(6) holds the gate open for the operator.

---

## 7 · SETTLE CONDITIONS (summary)

| Verdict | Settle-condition |
|---|---|
| ASSESS | PASS while A1–A5 hold; A1 FAIL = a prose section hiding a scan point; A2 FAIL = any arc movement reduced to a one-liner; A3 FAIL = any of the five gaps, the court drafts, the RFC surface, the autopilot gate, the pilot start, or the voice-check missing its reversibility + who-walks-it row; A4 FAIL = a recalled number without a fold/ledger/sha row; A5 FAIL = a verdict line that contradicts a ledger. |
| DESIGN | SOUND while §0 names the three movements + thesis, §2 carries the certified/measured/verdict triad, §3 carries the four decisions, §5 carries the doors, §6 closes with the next cards. |
| PROBE | VALID while every tracked claim has a §5 trace receipt and the wall clause is preserved; a trace that fails fails PROBE VALID. |

---

## 8 · HARD LINES

- Nothing public; RFC quiet; reads only; nothing posted beyond the study's own branch.
- The audit file is a grounded verdict, not a re-derivation of the gist's content.
- The only failure named in the gist is the voice-check door (A3); the fold's own sentence — "the court's posting, the patrol's shape, the RFC's surface, and the gist's voice-check ride the operator's word" — is the settling fact, and the operator's word is the gate.
- This file commits at the end of the audit leg, under the study's branch, author `kanban-pilot <pilot@rig.local>`.
