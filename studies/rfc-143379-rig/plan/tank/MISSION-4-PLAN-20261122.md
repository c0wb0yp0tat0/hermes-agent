# MISSION-4-PLAN-20261122

**Frame:** the #5320 sizing/silent-compression measurement applied to OUR pilot substrate (the rig's own anchor at 2,112/2,200 = 96%, the pinned class the field case describes). The route: PLANNER (this file: applications' map + depth-ledger) → EXECUTOR (completeness double-check + application) → SANITY (adjudication) → FOLD → hy's approve-or-reloop gate. The plan and the sealed artifacts are never altered — every proposal is a design. Nothing public; #5320's issue QUIET; #157065 READ-ONLY.

**Anchor pass (receipts):** `/root/.hermes/memories/MEMORY.md` = 2,112 chars over the 2,200 cap → **88-char room** (wc -m: 2112). USER.md = 1,346 chars over the 1,375 cap → **29-char room**. Config defaults: `memory_char_limit: 2200`, `user_char_limit: 1375`, both enabled. Memory tool: file-backed, `tools/memory_tool_store.py`.

## 1. THE APPLICATIONS' MAP

**P1 — the method's LOCAL RUN.** The same measurement-on-tool-calls method (comment 6761022718's method: read-only SQL over the session ledger, the calls are the truth, snapshot-lag inverted class) applied to the rig's own store `/root/.hermes/state.db` (`messages` where `tool_name='memory'`, read-only).
- Receipted numbers (SQL, 2026-11-22): 163 memory calls over 23 sessions; 106 successful writes; **29 cap-hit-in-same-session saves (27.4% of successes)**; attempts per cap-hit save: **median 3, max 10, min 1** (field case: median 2, max 3); 29 cap-hit saves across 20 sessions; **2 cap-hit saves with no recovery in the same session** (tool-loop cap 'consolidation failed 4 times' windows); recovery shapes: **patch-recorded 2, removes 0**; success usage buckets: 99 at 90–99%, 3 at 100% ('100% — 2,540/2,200 chars', a ledger anomaly vs the 2,200 cap — receipted verbatim), 4 other.
- Live target: `/root/.hermes/state.db` — this is OUR substrate's ledger; the field case (~50 writing sessions, ~70 successes, ~half cap-hit, median 2/max 3, 4-in-5 patch) is the benchmark, not our number.

**P2 — the silent-compression's LOCAL EVIDENCE.** Our own memory-ops audit. Receipts: (a) the ledger shows 29 cap-hit-in-session saves, each a rejection plus a rewrite of older entries to make room — the store pins at 96% (anchor 2,112/2,200) and the usage buckets show 99 of 106 successes between 90–99%; (b) the no-record-no-prompt class is PRESENT locally: the store logs the *cap error* in each call result ("Applying all N operations would put memory at X/2,200 chars: free at least Y chars more. Add removes or shortening patches of other stale entries to the same batch, then retry") but records no separate compression event — the shortening is visible only through the failure message; (c) the anchor register is already compressed to the cap (10 §-entries, avg 211.2 chars/entry, 2,112 chars, last § entry 'OPERATING DOCTRINE → chain 001' a long detail-bearing block); (d) the chain's downstream home is `/root/.hermes/memories` (MEMORY.md / USER.md register) plus the memory-chain INDEX.md at http://100.112.72.20:8789/memory-chain/INDEX.md — the detail-retention question is where the compression lands: in the same file the chain reads. No compression log exists anywhere in the local stores.

**P3 — the zero-sum decision's LOCAL STATE.** The anchor's 88-char room (2,112/2,200; 2,200 − 2,112 = 88) is the ready-to-hit-the-cap measure; the defaults' decision local shape = config.yaml `memory_char_limit: 2200` / `user_char_limit: 1375`, both enabled; USER.md 1,346/1,375 (29-char room). The field economics: the rejections are NOT the cost (recovery = one extra call); the cost is the zero-sum budget the model rewrites on every save. Raising the default or scaling with context window would remove most churn at this usage level — for our anchor that is a decision, not a change: the design (P4 gate + P5 compact notation) is the proposal; the anchor stays at 2,112/2,200 UNCHANGED. The chain's role as the downstream home is preserved (chain INDEX at the local server; register at the anchor file).

**P4 — the surface-pressure GATE's DESIGN (designed, not altered into the sealed armor).** The G14-adjacent gate ROW for the readiness loop, as a proposal:
- Threshold: 90% of the 2,200 cap (1,980/2,200) for the memory register — leave 220 chars of headroom before the hard cap; USER.md 90% = 1,237/1,375.
- Warning shape: a single in-conversation GATE ROW (part of the G14-adjacent armor, not a new tool/endpoint) carrying current usage %, chars free, and the drop candidates (the oldest/least-recent entries), with the user's explicit choice; no second silent retry.
- User-choose-not-model-shorten contract: before the hard cap, the model presents the shape (e.g., 2–3 candidates, one-line each) and the user chooses what to drop or patch; the default path is no model shortening at all. The gate fires BEFORE the rejection, so the user selects what to compress — the no-record-no-prompt class is killed at the source, not patched after.
- Status: DESIGN ONLY. Not written into config.yaml, not written into MEMORY.md, not pushed. The readiness loop's next gate, designed.

**P5 — the lossless-encoding's LOCAL APPLICATION.** The complementary axis with the sizing decision: #5320 enlarges the container; #157065 shrinks what's put in it. Read-only assessment of OUR anchor's own encodings:
- Anchor density (receipted): MEMORY.md 2,112 chars / 10 entries = 211.2 chars/entry; the register is mixed prose + key=value; the longer entries (e.g., 'OPERATING DOCTRINE → chain 001', 'GATE LAW (final): the word gates ONLY public writes outside PR #1 + deep deletions/money; internal doors act, never wait') carry the natural-language wrapper the compact guidance would strip.
- The design (proposal for the readiness loop, never a change): default the write guidance (prompt_builder.py ~L227) to compact machine-readable notation — `key=value`, semicolon-separated, no subjects/connectors/parentheticals — 'BMP → PNG, not JPG: nothing lost semantically; ~1/3 the characters'; same caps (1,375/2,200) hold more facts; new users benefit most (no config discovery needed).
- Live target: the guidance text only; the anchor's register is untouched; the GATE LAW's entries untouched.
- Ledger lines added by the amendment (committed b949067310): (1) lossless-vs-lossy distinction (BMP→PNG, never JPG — the silent-compression's opposite); (2) the 1/3-density claim; (3) container-vs-content complementarity (#5320 enlarges the container, this shrinks what's put in it); (4) the 974→442 stable run (author: 8 entries, no semantic loss, behavior stable).

## 2. THE DEPTH-LEDGER (lines that must never flatten)

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

## 3. THE EXECUTOR'S HANDOFF (concrete questions with receipts)

1. Is the local ledger complete? Verify from the receipted SQL above: 163 calls / 23 sessions / 106 successes / 29 cap-hit saves (27.4%) — the receipts are in the tool-call results, not in the store's appearance.
2. Re-confirm the anchor's 88-char room (wc -m = 2,112 over 2,200) and the config defaults (`memory_char_limit: 2200`, `user_char_limit: 1375`, both enabled) — receipts: wc -m / grep config.yaml.
3. Confirm the memory chain's local reachability (INDEX.md returns HTTP 200 at http://100.112.72.20:8789/memory-chain/INDEX.md) and its relation to the register — receipted.
4. Does the readiness loop accept P4's gate row as a design (threshold 90% = 1,980/2,200, single gate-row, user-choose-not-model-shorten contract)? — it must remain a design, not a change to the sealed artifacts.
5. Does the readiness loop accept P5's compact-notation guidance as a proposal (prompt_builder.py ~L227, BMP→PNG not JPG, ~1/3 chars, no config/schema/behavior change)? — acceptance is a paper design; the anchor is never touched.
6. Measurement for the next iteration: re-run the same SQL over the next ~5 weeks of sessions and compare shares (cap-hit share, attempts median/max, patch share) — the field numbers are the benchmark, our numbers are the local receipt.

## 4. THE PLAN'S FRAME LINES (what must not flatten)

- The plan and the sealed artifacts are never altered — proposals are designs; the anchor (2,112/2,200, 88-char room) and the GATE LAW (final form: word gates ONLY public writes outside PR #1 + deep deletions/money; internal doors act, never wait) are immutable.
- Every application names its live target: P1 = /root/.hermes/state.db (read-only SQL); P2 = the ops' ledger + the anchor register; P3 = config.yaml defaults + anchor; P4 = a designed gate-row (not written); P5 = a guidance proposal (not written).
- The discipline: our substrate reproduces the field class (cap-pinning 96%, zero-sum rewrite, silent shortening, no record, no prompt, user sees 'memory works') — the mission's point is that the measurement now runs ON US, with receipts, before the readiness loop decides.
- Emission contract: this file is the deliverable; exit 0 = the map + ledger + handoff inside (it is).
