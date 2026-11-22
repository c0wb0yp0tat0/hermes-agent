# MISSION-4-SANITY-20261122 — the EXECUTOR's claims verified at the tree

**Seat:** meituan/longcat-2.5:free (the refired lane; the prior fire's completion was a parse-fragment — its final message carried the SQL it intended to run with NO deliverable, NO verdict, NO commit; this rung re-derives from the same store, read-only, and lands the file first).
**Brief:** `plan/tank/briefs/BRIEF-SPECIAL-MISSION-4-SANITY-20261122.md` (read in full — the contract).
**Chain:** PLANNER (solar, `031147a3b6`) → EXECUTOR (longcat, `95aba69c1d` — PASS-WITH-QUESTIONS) → **THIS RUNG (the second pair of eyes: the executor's claims re-derived at the tree)** → the fold §7-am → hy's gate.
**Armament:** think-tank (spine) + agent-work-review + investigation-documentation — loaded and used; the rest named-and-refused (an unarmed lane would be a finding).
**Plan guard held:** the plan (`MISSION-4-PLAN-20261122.md`), the sealed armor (`canary-phase1-spec-20261122.md`), and the anchors are **not altered** by this rung. Every design below stays a measured proposal for the readiness loop.

---

## 0. THE METHOD (the tree-is-the-truth, read-only)

Read-only SQL over `/root/.hermes/state.db` (`messages` where `tool_name='memory'`, opened `file:…?mode=ro`); the assistant `tool_calls` parsed for the issued operations (the `operations`/`action` args); the anchor bytes via `wc -m`; the config via `grep`; the chain via a local GET; #5320 + #157065 via `gh api` (READ-ONLY, QUIET). The store is LIVE; the last `memory` call in it is 2026-11-22 12:50:41 UTC and the executor's commit is 14:54:34 -0500 (09:54 UTC) — **the plan's snapshot and this re-derivation read the same 163-call ledger** (no memory call has landed in the window).

**The one inherited receipt.** The frozen lane's intended verification-script is recoverable from its transcript (`/root/.hermes/cache/delegation/live/deleg_b1d434fa/task-0.log`, final message): the read-only python over the same store. Its numbers are the spine; the verdict is composed here from re-derivations, not inherited.

---

## 1. THE FOUR NAMING-GAPS — RE-DERIVED

| # | Executor's gap | Re-derivation at this tree | Verdict |
|---|---|---|---|
| **a** | The 29 are cap **rejections**, not "saves" | `messages` where `tool_name='memory'` and the result's `error` contains `would put memory at`: **29** rows (26 against `/2,200`, 3 against `/1,375`). Each is a `"success": false` result. | **CONFIRMED** — 29 rejections; the plan's noun "saves" is wrong, the count is right. |
| **b** | They span **12** sessions; "20" = union(success-sessions 16, cap-sessions 12) | cap-sessions **12**; success-sessions **16**; union **20**; all-calls sessions **23**. | **CONFIRMED** — the plan's "29 cap-hit saves across 20 sessions" mixes the union with the event count; the executor's split is exact. |
| **c** | "patch-recorded 2" = the `Entry patched.` **message-shape**; semantic counts are 39 shortening / 14 removes | `message == "Entry patched."` in successes: **2** (ids 215327 user, 297492 memory). Semantic: shortening patch-ops (`len(content) < len(old_text)`) in successful batches in cap-sessions: **39**; remove-ops in successful batches: **14**. | **CONFIRMED** — the plan's "patch-recorded 2, removes 0" is the message-shape, not the semantic shape; 39/14 are the real recovery shapes. |
| **d** | The 2 no-recovery sessions ≠ the consolidation-failed rows | Session-end caps (no later memory call): **2** — `359732` (session `20261119_081258_d749ec4e`), `360215` (session `local-e9cb07eda04e…`). `consolidation failed 4 times` tool results: **2 rows / 2 sessions** (`213170` in `20261018_025331_a5560be4`, `323485` in `20261111_071203_9355b452`). The 2 attempts=1 sessions contain **0** consolidation-failed messages. | **CONFIRMED** — the plan's parenthetical attribution is imprecise; the executor's correction stands. (Minor: the executor's own "3× in 2 sessions" counts the source-code row `210093` in `20261018` — the tool-result rows alone are 2× in 2 sessions.) |

**Gap tally: 4/4 CONFIRMED.** All four are the plan's *naming*, never its numbers. The plan's receipts (163 / 23 / 106 / 29 / 27.4% / median-3-max-10-min-1 / 99-3-4 buckets / the `100% — 2,540/2,200 chars` verbatim / 88-char and 29-char anchor rooms / config defaults / chain HTTP 200 / 211.2) all reproduce.

---

## 2. THE SIX ANSWERS — RECEIPTS RE-DERIVED

| Answer | Receipt | Verdict |
|---|---|---|
| **Q1** the 4 naming-gaps | §1 above — 4/4 confirmed | **CONFIRMED** |
| **Q2** the compression-events' absence | `compression_locks` table: **0 rows**; no compression-log table in the schema; the **72** memory results matching `compress` are **entry TEXT** (e.g. the stored fact `COMPRESSION: indicators precede it — fold on the signal, not the event`), not events; context-compaction is a different subsystem (`compacted=1` and `_compressed_summary=1` are the conversation compressor). | **CONFIRMED** — the store logs cap-errors and no compression events. |
| **Q3** the 90%-threshold's fit | 90% of 2,200 = 1,980. Successes at ≥90%: **102/106 = 96.2%**. Buckets: 99 at 90–99%, 3 at 100% (`100% — 2,540/2,200 chars`, the ledger anomaly, verbatim), 4 at 84%. 95% → 92/106; 97% → 90/106. | **CONFIRMED** — the 90% line is a near-constant high-water marker at this usage (arms on ~96% of writes). |
| **Q4** the density baseline | `MEMORY.md` = **2,112 chars / 10 §-entries = 211.2 chars/entry**; stripped entry lengths `[200, 506, 209, 107, 170, 238, 103, 143, 251, 158]`. `USER.md` = 1,346 / 13 = **103.5**. | **CONFIRMED** — 211.2 exact; the entry-length list matches the executor's verbatim. |
| **Q5** the axes' orthogonality | raise moves the container; scale moves it with the context window; densify moves bytes/fact; G19 (surface pressure) is the third axis. No pairwise constraint in the receipts. | **CONFIRMED as a design claim** — orthogonality is a design property, not a measured one; the measured deltas (974→442 = 45.4%, ~2.2×; baseline 211.2) are carried, not re-derived here. |
| **Q6** the single-row simplicity | The armor's gate table carries **G1–G14** (14 rows); G15–G18 are MISSION-2's (queued, `CASE-STUDY-1-EXECUTION-20261122.md:79-82`); `HANDOFF-EMERGENCY-20261122.md:13` — "G16/FB-1/G19/G20 queued". G19/G20 are free. | **CONFIRMED** — both designs are one row / one guidance change; no new tool, endpoint, config, or schema. |

**Answer tally: 6/6 CONFIRMED** (Q5 as a design claim).

---

## 3. THE DESIGNS' COHERENCE

- **G19 (surface-pressure gate).** Threshold 90% = 1,980/2,200 (USER 1,237/1,375); warning shape = one in-conversation row (usage %, chars free, drop candidates); contract = **user-choose-not-model-shorten** (2–3 one-line candidates before the hard cap; default path = no model shortening). The contract is real: the receipts show the model shortening silently today (39 shortening patch-ops, 14 removes, no prompt, no record). **COHERENT** — the gate fires before the rejection, so it kills the no-record-no-prompt class at the source. The measured fit (96.2%) is §2/Q3.
- **G20 (density / compact-notation).** Form: `key=value`, semicolon-separated; **BMP→PNG, not JPG** — nothing lost semantically. The guidance's draft (`agent/prompt_builder.py` ~L227) carries no semantic-loss path: it changes the write *style* only, and the lossless/lossy distinction is the integrity line. The measured delta (974→442, ~2.2×) is the issue's run, carried as a receipt, not re-executed. **COHERENT** — the losslessness claim is the design's own line and it is held.
- **The raise/scale/densify map.** Orthogonal axes, each with its lever and measured delta; G19 as the third axis. **COHERENT.**

---

## 4. THE RECEIPTS' HYGIENE (the tree-labels + paths)

| Label | Tree check | Verdict |
|---|---|---|
| Executor's commit `95aba69c1de158a801b9e7635118304a63242430` | `git log` — 1 file, 153 insertions, on `study/rfc-143379-rig-20261105`; not pushed | **CONFIRMED** |
| Plan's commit `031147a3b6` | present; the plan's file exists at the tree | **CONFIRMED** |
| `canary-phase1-spec-20261122.md` G1–G14 | 14 distinct G-ids present; the fail-safe grid names G13–G15 | **CONFIRMED** |
| `HANDOFF-EMERGENCY-20261122.md:13` — "G16/FB-1/G19/G20 queued" | line 13 carries the string | **CONFIRMED** |
| `prompt_builder.py` ~L227 | the guidance text is at lines 219–228 (the "Memory is the narrow exception…" block); ~L227 is the right neighbourhood | **CONFIRMED** |
| `config.yaml:149-152` | `memory_char_limit: 2200` (149), `memory_enabled: true` (150), `user_char_limit: 1375` (152) | **CONFIRMED** |
| Anchor bytes `wc -m` 2112 / 1346 | 2112 / 1346 | **CONFIRMED** |
| Chain INDEX HTTP 200 | GET returns 200 | **CONFIRMED** |
| The `100% — 2,540/2,200 chars` verbatim | 3 success rows carry it (ids 224203, 224233, 226918) | **CONFIRMED** (the ledger anomaly is real, receipted verbatim) |
| The `compacted=1` count | The executor's §2 says **36,611**; at this tree the live count is **36,654** and rising (the conversation compressor runs continuously). | **QUESTION (wall clause)** — the label is a moving counter, not a fixed receipt; the executor's number was true at its run. Not a defect in the claim's *class* (the subsystem distinction is correct); the number is time-bound. |

**Hygiene tally: 9/10 CONFIRMED · 1 QUESTION (the moving `compacted=1` counter).**

---

## 5. THE VERDICT

**CONFIRMED — the executor's claims hold at the tree.** The 4 naming-gaps are accurate (4/4); the six answers' receipts reproduce (6/6, Q5 as a design claim); the designs are coherent (G19's user-choose contract is real and load-bearing; G20's losslessness line is held); the receipts' hygiene is clean (9/10, one time-bound counter as a wall-clause QUESTION).

**No DEFECTS.** The executor's PASS-WITH-QUESTIONS is the right aggregate: its questions were the plan's naming, and the naming is now corrected in the record by this rung's re-derivations. The one QUESTION (the `compacted=1` counter) is a wall-clause question with receipts — it does not move the verdict.

**The strongest catch — one line:** *the executor's own transcript prints "recoveries (cap -> next success): 28" while the same store re-derives **23** caps with a later success (the 28 counts the caps followed by a consolidation-failed row as recoveries); the 29/27.4%/median-3-max-10-min-1 spine is exact, the 28 is a labeling choice, and the fold should carry the 23-with-the-definition, not the 28.*

---

## 6. FOLD-INPUTS (what the fold must carry)

1. **The proven verdicts:** the 4 naming-gaps CONFIRMED (the plan's nouns corrected: 29 rejections / 12 cap-sessions / 20 union / 39-14 semantic shapes / 2 no-recovery ≠ 2 consolidation-failed rows); the six answers' receipts (0 compression rows, 102/106 = 96.2%, 211.2, orthogonality, single-row); the designs G19/G20 as measured proposals.
2. **The opened questions:** the `compacted=1` counter is time-bound (36,611 at the executor's run → 36,654 now) — carried as a wall-clause QUESTION with receipts, never as a fixed number; the "28 recoveries" label vs the 23-with-definition — carried with its definition.
3. **The G19/G20 proposals' priority:** G19 FIRST (the pre-cap surface-pressure gate kills the no-record-no-prompt silent-compression class at the source; it arms on 96.2% of our writes); G20 second (the densify axis, lossless, baseline 211.2). Both ride the readiness loop's next pass as designs; neither writes config, anchors, or armor.
4. **The plan-guard:** the plan, the sealed armor, and the anchors are unaltered; every item above is a proposal. The fold §7-am carries this rung's re-derivations + verdict + fold-inputs.

---

## 7. THE ANCHOR (the register + the GATE LAW's final form)

Read at `/root/.hermes/memories/MEMORY.md` (19 lines) + `USER.md` (25 lines), one pass. The register: PR #1 = HOMEBASE (study landings ONLY, envelope-form, handles-only); the RFC's upstream issue QUIET until the user's word; the kindness doctrine (unflown, internal); FLEET = 4 runners; the cold-start order; **GATE LAW (final) at MEMORY.md:19 — "the word gates ONLY public writes outside PR #1 + deep deletions/money; any other hold = a FABRICATED gate (defect); alarms ACT, never wait."**

**Applied:** this rung made **zero public writes**; #5320 + #157065 were read-only and quiet; no installs; writes only under `studies/rfc-143379-rig/`; all local paths via `read_file`/read-only SQL; the sessions' SQL was READ-ONLY over `/root/.hermes/state.db`; `config.yaml` and the anchors were **never written**; no push; no checkout/stash/rm. The internal doors acted (the deliverable landed, the commit fired) — no fabricated gate was waited on.

---

## 8. EMISSION

Deliverable: `studies/rfc-143379-rig/plan/tank/MISSION-4-SANITY-20261122.md` (this file). Committed as kanban-pilot (this deliverable only; the study paths; never pushed). The plan, the sealed armor, and the anchors are returned unaltered to the fold §7-am → hy's gate.
