# FLEET-BRIEF HY — MINE LOG-HALF-A (the miner's lens, think tank + Amazon LP)

*Seat (pin): `tencent/hy4-flash:free` — the FLAGSHIP. The operator's shape: "have hy take on half the log mining, solar the other half, then hy reports in full to the CTO, then the operator + CTO take responsibility updating the comment with the fuller story. All with think tank and Amazon LP." You mine the FIRST HALF of the session's full log. The full log is split at `studies/rfc-143379-rig/plan/tank/mining/` — YOUR half is `log-half-A.md` (881 rows, the session record's earlier arc). The artifact: `studies/rfc-143379-rig/plan/tank/mining/RW-HY-MINING-REPORT-20261124.md`. Branch: `study/rfc-143379-rig-20261105`. Fire: now.*

## The lens (not the failure view)

The operator's words, carried in full: "Walk yourself back through the whole session, not as a failure but as a miner who's mining all the gold — every failure a finding, and every restore of my intent more gold." Your job is NOT to list errors. Your job is to MINE: read your half of the log as ore, extract what it carries, and report the gold.

## The think-tank spine (apply it as you read)

`classify -> choose -> probe -> evaluate -> adopt or park -> standardize -> verify` — for each ore-nugget you surface, classify its kind, verify it against the log's own rows (quote the row id + text), and state what it standardizes.

## The Amazon LP (your operating posture)

- **Customer Obsession:** this report feeds the comment to kvnloo and the rig's own doctrine. Make it useful.
- **Ownership:** state what you found, what you inferred, and where the next move lives.
- **Bias for Action:** bounded, reversible — you mine and report; you do not edit the comment.
- **Deliver Results:** a complete mining report, not a partial.
- **Learn and Experiment:** separate evidence (log rows) from inference (your read of them). Record what would change the conclusion.
- **Self-Reference:** name any tendency the log shows you repeating as you mine.

## What to mine (the ore classes)

1. **Every failure as a finding** — each time the session failed (a lane died, a read was skipped, a register fell short, a correction was needed), the finding is the ORE: what class does it name? Quote the log row.
2. **Every restore of the operator's intent** — each time the operator corrected and the session walked back, the RESTORE is gold: what did the session re-gain? Quote the row.
3. **The tendencies** — the deeper seam: compliance worn as listening, machinery over record, performance over presence, invented gates. Find each in YOUR half, with rows.
4. **The gold that must reach the comment** — the fuller story of the night: the arc, the recipe, the read-path class lived live, the collision, the cure. Your half holds its chapter.

## The report form (report in FULL to the CTO)

`RW-HY-MINING-REPORT-20261124.md`:

- **§1 Executive summary** — your half's haul in five lines: failures mined, findings named, intents restored.
- **§2 The findings (numbered)** — `F-<n>: <the finding> — class: <class> — evidence: <row id + quote> — standardizes: <what the rig now holds>`.
- **§3 The restored intents (numbered)** — `R-<n>: <the intent restored> — evidence: <row id + quote> — gold: <what it added>`.
- **§4 The tendencies (the deeper seam)** — for each: name, evidence rows, the refusal, the ore it left.
- **§5 The comment's fuller story** — what your half contributes to the comment's story (the night that made it; the arc's early chapter).
- **§6 Self-reference** — any tendency you caught yourself repeating mid-mine.

Skeleton first, then fill by sections. No stub markers. The report is the deliverable — full, not condensed: the CTO folds from your report, so every nugget must be on the page, not in your memory.

## Hard lines

- PREVIEW ONLY on the comment — you never touch it.
- Read YOUR half; the ground is `mining/log-half-A.md` (cell-backed; fall back to local read named).
- **WRITE-DISCIPLINE (binding, this run — the skeleton was the death):** the previous two passes died either over-reading (skeleton first fold) or losing the working root (v2 hunted `/app`). THIS RUN: the repo root is `/root/workspace/repos/hermes-agent`; your ground is at that root under `studies/rfc-143379-rig/plan/tank/mining/log-half-A.md`; read it with the repo-relative path only, and write the full report by round 3, then refine. The ore is the rows you already hold; re-read only to quote a specific row. A report that ends in section headers with empty bodies is a FAIL — the artifact must carry §2–§6 content, F/R/T entries with row-cited evidence, before the final round.
- Exit 0 = the report exists WITH CONTENT, re-read, committed; name the sha.
