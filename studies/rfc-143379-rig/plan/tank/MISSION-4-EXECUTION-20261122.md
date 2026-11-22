# MISSION-4-EXECUTION-20261122

**Frame:** the EXECUTOR rung of the sizing/silent-compression mission (the #5320 usage-measurement applied to OUR pilot substrate). Seat: meituan/longcat-2.5:free (pin-read-back verified at the fire). Chain: PLANNER (solar, `031147a3b6` — the applications' map P1–P5 + the depth-ledger 11 + the handoff's six) → **THIS RUNG (the completeness double-check + the six answers + the designs' landing)** → the sanity → the fold §7-am → hy's gate. The plan, the sealed armor, and the anchors are NOT altered by this rung; every design below is a MEASURED PROPOSAL for the readiness loop. Nothing public; #5320 + #157065 QUIET (read-only); no installs; writes only under `studies/rfc-143379-rig/`.

**Inputs read in full:** the brief (`plan/tank/briefs/BRIEF-SPECIAL-MISSION-4-EXECUTOR-20261122.md`) · the plan (`plan/tank/MISSION-4-PLAN-20261122.md`, `031147a3b6`) · the #5320 comment (`/tmp/c-5320-6761022718.md`) · the #157065 issue (via `gh api`, read-only) · the kit's surfaces (`plan/tank/OPUS-PILOT-KIT-20261121.md`; the armor's gate table in `plan/tank/canary-phase1-spec-20261122.md`; the master's folds `MISSION-BRIEF-MASTER-20261119.md` §7) · the anchors (`/root/.hermes/memories/MEMORY.md`, `USER.md`) · the store (`/root/.hermes/state.db`, READ-ONLY).

---

## 1. THE COMPLETENESS DOUBLE-CHECK — the plan's receipts RE-DERIVED

**Method:** read-only SQL over `/root/.hermes/state.db` (`messages` where `tool_name='memory'`, opened `file:…?mode=ro`); the anchor bytes via `wc -m`; the config via `grep`; the chain via a local GET. The store is LIVE; the last `memory` call in it is 2026-11-22 12:50:41, and the plan's commit is 14:37:30, so the plan's snapshot and this re-derivation read the same 163-call ledger.

| # | Plan's receipt | Re-derived at this tree | Verdict |
|---|---|---|---|
| 1 | 163 memory calls | **163** (`role='tool'`, `tool_name='memory'`) | REPRODUCES |
| 2 | 23 sessions | **23** distinct `session_id` | REPRODUCES |
| 3 | 106 successful writes | **106** (`success:true`) | REPRODUCES |
| 4 | 29 cap-hit-in-same-session saves (27.4%) | **29** cap rejections (`error` contains `would put memory at`); 29/106 = **27.36%** | REPRODUCES as a count; **label caveat** (see Q1) |
| 5 | attempts per cap-hit save: median 3, max 10, min 1 | **median 3, max 10, min 1** (cap rejection → next success, inclusive) | REPRODUCES |
| 6 | 2 cap-hit saves with no recovery | **2** with no later memory call at all (`359732`, `360215`); 4 more with later calls but no later success | REPRODUCES (count); **attribution caveat** (see Q1) |
| 7 | 29 cap-hit saves across 20 sessions | 29 events span **12** sessions; **20** = union(success-sessions 16, cap-sessions 12) | QUESTION (definitional) |
| 8 | recovery shapes: patch-recorded 2, removes 0 | **2** = the count of successes whose result `message` is literally `Entry patched.`; **0** remove-messages. Semantic counts: **39** shortening patches + **14** remove ops in successful batches | QUESTION (label) |
| 9 | usage buckets: 99 at 90–99%, 3 at 100%, 4 other | **99** (90–99%), **3** (100%), **4** (84%) | REPRODUCES |
| 10 | `100% — 2,540/2,200 chars` verbatim | the same string, **3×** | REPRODUCES |
| 11 | anchor 88-char room (2,112/2,200) | `wc -m` = **2112**; 2200−2112 = **88** | REPRODUCES |
| 12 | USER.md 29-char room (1,346/1,375) | `wc -m` = **1346**; 1375−1346 = **29** | REPRODUCES |
| 13 | config defaults 2,200 / 1,375, both enabled | `memory_char_limit: 2200`, `user_char_limit: 1375`, `memory_enabled: true` | REPRODUCES |
| 14 | chain INDEX HTTP 200 | **HTTP 200** at `http://100.112.72.20:8789/memory-chain/INDEX.md` | REPRODUCES |
| 15 | density 211.2 chars/entry | 2112 / 10 §-entries = **211.2** | REPRODUCES |
| 16 | depth-ledger 11 lines | **11** lines present (plan §2:31–41), each un-flattened | REPRODUCES |

**VERDICT: PASS-WITH-QUESTIONS.** 12 of 16 receipts reproduce exactly (the SQL spine, the anchor rooms, the config, the chain, the density, the ledger); 2 reproduce with a named caveat (the 29's label; the 2's attribution); 2 are definitional QUESTIONS (the "20 sessions"; the "patch-recorded 2 / removes 0"). All four gaps are in the plan's *naming*, not its numbers: (a) the 29 are cap **rejections**, not "saves"; (b) the 29 span **12** sessions, and 20 is the union of success-sessions and cap-sessions; (c) "patch-recorded 2" is the `Entry patched.` **message-shape** count, not a count of shortening patches (the semantic local count is far higher). No receipt is fabricated; the gaps are named, not smoothed. The wall clause holds: each non-reproduction is a QUESTION with receipts, below.

---

## 2. THE HANDOFF'S SIX QUESTIONS — ANSWERS WITH RECEIPTS

### Q1 — the cap-hits' recovery-shapes' local distribution
**Answer: the local recovery is a retry-then-rewrite shape, pervasive and lossy; the plan's "2" understates it.**
- 29 cap rejections; **23** have a later success in the same session; **4** have later calls but no later success (`213153`, `213155`, `285444`, `285446`); **2** have no later memory call at all (`359732`, `360215`).
- Attempts (cap rejection → next success, inclusive): distribution `{1:2, 2:12, 3:7, 4:3, 5:1, 6:2, 7:1, 10:1}` → **median 3, max 10, min 1**. The field case's median 2 / max 3 is the same class with shorter tails; ours run longer (the max-10 chain is a 9-retry streak).
- Recovery writes: **23/23** record `patched_entries`; **6/23** record `removed_entries`.
- Successful-batch patch-ops: **39** shortening patches, **14** remove ops (raw, incl. retries: 91 shortening patch-ops / 21 remove ops).
- The plan's "patch-recorded 2" reproduces **only** as the count of successes whose result `message` is `Entry patched.` (2 of 106). Under the semantic reading (shortening patches) the local count is 39 in successful batches. The P2 receipt's specific "100→78" and "220→82" halvings **do not appear anywhere** in the ledger (searched all patch ops).
- The plan's parenthetical attribution of the 2 no-recovery cases to "tool-loop cap 'consolidation failed 4 times' windows" is imprecise: the `consolidation failed 4 times` tool result appears **3× in 2 sessions** (`20261018_025331_a5560be4` ×2, `20261111_071203_9355b452` ×1), while the 2 attempts=1 cases are `359732` / `360215`, in sessions with **0** consolidation-failed messages.

### Q2 — the compression-events' absence confirm
**Answer: CONFIRMED. The store logs cap-errors; it logs no compression events.**
- The 29 cap rejections carry the cap-error string verbatim in their results.
- `compression_locks` table: **0 rows**. No compression-log table exists in the schema.
- The **72** memory results matching `compress` are **entry TEXT**, not events (e.g. the stored fact `COMPRESSION: indicators precede it — fold on the signal, not the event`).
- Context-compaction is a **different subsystem**: 36,611 `compacted=1` messages and 195 `_compressed_summary=1` messages are the conversation compressor, not the memory store.
- Net: the shortening is visible only through the failure message and the `patched_entries` diff — the no-record-no-prompt class is present locally, exactly as the field case describes.

### Q3 — the 90%-threshold's fit for OUR usage
**Answer: the 90% line is a near-constant high-water marker at our usage, not a rare warning; it is defensible as the "leave 220 chars" line.**
- 90% of 2,200 = **1,980**. Successes at ≥90%: **102/106 = 96.2%**.
- Distribution: 99 at 90–99%, 3 at 100%, 4 at 84%. Current anchor **2,112/2,200 = 96.0%**; USER.md **1,346/1,375 = 97.9%** (90% = 1,237.5).
- The threshold sits **below** our steady state, so it arms on ~96% of successful writes. If a rarer warning were wanted: 95% → 92/106 (86.8%); 97% → 90/106 (84.9%).
- The 90% choice = "leave 220 chars of headroom before the hard cap"; measured, that is the right order for a *pre-cap* marker whose job is to fire before the rejection, not to be exceptional.

### Q4 — the density-baseline's stable form
**Answer: 211.2 chars/entry, receipted from the anchor's own bytes; it is the densify axis's denominator.**
- `MEMORY.md` = **2,112 chars / 10 §-entries = 211.2 chars/entry**; entry lengths `[200, 506, 209, 107, 170, 238, 103, 143, 251, 158]`.
- The register is **mixed prose + key=value**; the long entries (`Homebase` 506, `GATE LAW` 251, `Cold-start` 238) carry the natural-language wrapper the compact guidance would strip.
- `USER.md` = **1,346 / 13 = 103.5 chars/entry** (denser already).
- Stable form: the baseline is the anchor's own measured density, taken from `wc -m`; it is not a target, it is the measured starting point for the densify axis.

### Q5 — the complementarity's design-integrity (raise / scale / densify)
**Answer: the three axes are orthogonal; they do not conflict.**
- **raise** moves the container (2,200 → N). **scale** moves the container with the context window (N = f(context)). **densify** moves the content (chars/entry ÷ ~3).
- raise/scale change the *cap*; densify changes the *bytes per fact*. Both reduce cap-pressure; neither constrains the other.
- Measured deltas: densify ≈ 1/3 the characters (the issue's run 974 → 442 = **45.4%**, ~2.2×); the anchor's 211.2 chars/entry is the baseline. raise/scaling deltas are the decision's to price (the field case: raising or scaling "would remove most of the churn at this usage level").
- The lossless/lossy distinction is the integrity line: **densify = BMP→PNG** (nothing lost semantically); the silent compression = **JPG** (details drop, no record, no prompt). The gate (G19) is the third axis (surface pressure); it is orthogonal to both.

### Q6 — the gate-row's single-row simplicity
**Answer: both designs are single-row; no new tool, endpoint, config, or schema.**
- The armor's gate table currently carries **G1–G14** (14 rows). **G15–G18** are MISSION-2's (queued). **G19/G20 are free** (`HANDOFF-EMERGENCY-20261122.md:13` — "G16/FB-1/G19/G20 queued").
- G19 (surface-pressure) = **one row**: threshold + warning shape + user-choice contract. G20 (density) = **one guidance change** at `prompt_builder.py` ~L227.
- Neither writes config.yaml, the anchors, or the sealed armor.

---

## 3. THE PLAN'S §3 SIX QUESTIONS — MAPPED

1. **Is the local ledger complete?** Yes. 163 / 23 / 106 / 29 / 27.4% all reproduce from the tool-call results; the calls are the truth, the snapshot-lag class is inverted. The three label gaps are named in §1.
2. **The anchor's 88-char room + config defaults?** Confirmed: `wc -m` 2112 over 2200; `memory_char_limit: 2200`, `user_char_limit: 1375`, `memory_enabled: true`.
3. **The chain's reachability + relation?** HTTP 200. Relation: the chain INDEX is the downstream home; the register is the anchor file; the compression lands on the anchor, the chain keeps the detail.
4. **P4's gate row accepted as a design?** Yes, as **G19**, design only.
5. **P5's compact-notation accepted as a proposal?** Yes, as **G20**, paper design; the anchor is never touched.
6. **The next iteration's measurement?** Re-run the same read-only SQL over the next ~5 weeks; compare cap-hit share, attempts median/max, patch share. The field numbers (~50 sessions, ~70 successes, ~half cap-hit, median 2/max 3, 4-in-5 patch) are the benchmark; ours are the local receipt.

---

## 4. THE DESIGNS' LANDING — MEASURED PROPOSALS (recorded, never written into config/anchors/armor)

### G19 — the surface-pressure gate (the readiness loop's next gate-DESIGN)
- **Live target:** the armor's gate table (a new row), NOT written.
- **Threshold:** 90% of 2,200 = **1,980/2,200** (leave 220 chars headroom). USER.md 90% = **1,237/1,375**.
- **Warning shape:** a single in-conversation gate row carrying current usage %, chars free, and the drop candidates (oldest / least-recent entries).
- **Contract:** user-choose-not-model-shorten. Before the hard cap the model presents 2–3 one-line candidates; the user chooses what to drop or patch; the default path is **no model shortening at all**. The gate fires BEFORE the rejection, so the no-record-no-prompt class is killed at the source.
- **Measured fit:** arms on 102/106 (96.2%) of our successful writes; the current anchor (96.0%) is above it.

### G20 — the density / compact-notation guidance (the lossless axis)
- **Live target:** the write-style guidance text at `agent/prompt_builder.py` ~L227, NOT written.
- **Form:** default the `memory`/`user` write guidance to compact machine-readable notation — `key=value`, semicolon-separated, no subjects/connectors/parentheticals. **BMP→PNG, not JPG**: nothing lost semantically; ~1/3 the characters.
- **Baseline:** the anchor's **211.2 chars/entry** (2,112/10), receipted; USER.md 103.5.
- **Scope:** guidance text only; no config change, no schema change, no behavior change to the memory tool; the anchors and the GATE LAW's entries untouched.

### The sizing-decision's design-space map (raise vs scale vs densify)
| Axis | Lever | Measured delta | Conflict with the others |
|---|---|---|---|
| **raise** | container 2,200 → N | removes most churn at this usage (field) | none; orthogonal |
| **scale** | container = f(context window) | ties headroom to the model's window | none; orthogonal |
| **densify** | chars/entry ÷ ~3 | 974 → 442 = 45.4% (~2.2×); baseline 211.2 | none; lossless (BMP→PNG) |
| **G19 (surface pressure)** | pre-cap warning + user choice | fires on 96.2% of writes at our usage | none; the third axis |

**The plan-guard held:** the plan, the sealed armor, and the anchors are unaltered; every item above is a proposal.

---

## 5. THE DEPTH-LEDGER (the plan's 11 lines, carried un-flattened)

1. The method's tool-call truth — the calls are the truth; the snapshot-lag class inverted (field) and our local ledger (163 calls) confirm.
2. The half-of-writes-hit-the-cap's share — field ~half; local 27.4% — same class, different usage intensity; both receipted.
3. The median-2-max-3 attempts — field; local median 3, max 10 — same class, our recovery tails run longer.
4. The 4-in-5 shortening-patches — field; local patch-recorded 2/106 successes, removes 0 — same class, our recoveries are 'Entry patched.' rewrites.
5. The rejection-vs-rewrite economics — rejections aren't the cost; the zero-sum rewrite is; raising defaults/scaling would remove most churn at this usage level (field ~30% vs ~27% rejection shares).
6. The surface-pressure's user-choice contract — high-water warning before the hard cap, user chooses what to drop, model shortens silently is the failure mode (P4 design).
7. The caveat's confound — frequency vs cap-share distinction (~2/3 calls in last week; ~30% vs ~27% rejection share before/after).
8. Lossless-vs-lossy distinction (P5) — BMP→PNG, never JPG: the silent-compression's opposite; no semantic loss, no prompt.
9. The 1/3-density claim (P5) — comparable facts fit in ~1/3 the characters.
10. The container-vs-content complementarity (P5) — #5320 enlarges the container; #157065 shrinks what's put in it.
11. The 974→442 stable run (P5) — author's run, 8 entries, no semantic loss, behavior stable.

---

## 6. THE PLAN-GUARD + HARD LINES (held)

- The plan (`031147a3b6`), the sealed armor, and the anchors are **never altered** by this rung; the designs are proposals.
- Nothing public; #5320 + #157065 QUIET (read-only); no installs; writes only under `studies/rfc-143379-rig/`; all local paths via `read_file`/read-only SQL; never push; never checkout/stash/rm; the sessions' SQL is READ-ONLY over `/root/.hermes/state.db`; `config.yaml` and the anchors are **never written**.
- The anchor pass: `MEMORY.md` 2,112/2,200 (88-char room), `USER.md` 1,346/1,375 (29-room), the GATE LAW's final form present (`MEMORY.md:19` — the word gates ONLY public writes outside PR #1 + deep deletions/money; internal doors act, never wait).

---

## 7. THE SEAL (receipts)

- **The plan's receipts:** `/root/.hermes/state.db` (read-only; 163 calls / 23 sessions / 106 successes / 29 cap rejections / median 3, max 10, min 1 / 99-3-4 usage buckets); `/root/.hermes/memories/MEMORY.md` (`wc -m` 2112); `/root/.hermes/memories/USER.md` (`wc -m` 1346); `/root/.hermes/config.yaml:149-152`; `http://100.112.72.20:8789/memory-chain/INDEX.md` (HTTP 200).
- **The kit's surfaces:** `plan/tank/OPUS-PILOT-KIT-20261121.md`; the armor's gate table `plan/tank/canary-phase1-spec-20261122.md` (G1–G14); `MISSION-BRIEF-MASTER-20261119.md` §7; `HANDOFF-EMERGENCY-20261122.md:13` (G19/G20 queued).
- **The inputs:** `plan/tank/briefs/BRIEF-SPECIAL-MISSION-4-EXECUTOR-20261122.md`; `plan/tank/MISSION-4-PLAN-20261122.md` (`031147a3b6`); `/tmp/c-5320-6761022718.md`; `gh api repos/NousResearch/hermes-agent/issues/157065`.
- **The wall-clause gaps (4):** the "saves" label (29 = rejections); the 2's attribution (the consolidation-failed sessions are not the attempts=1 sessions); the "20 sessions" (12 actual; 20 = union); the "patch-recorded 2 / removes 0" (message-shape count; semantic counts 39 / 14). Each with its receipts above; none smoothed.

*A non-reproduction is a QUESTION with receipts. The tree is the truth; the receipts are re-derived; the designs are proposals.*
