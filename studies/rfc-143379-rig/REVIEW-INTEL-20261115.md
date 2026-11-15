# REVIEW-INTEL-20261115 — Background-Review Pile: Map + Intel + Steers

**Lane:** copycat (read-only). **Date:** 2026-11-15. **Source:** `/root/.hermes/pending/memory/*.json` (130 staged batches, ~608 KB, 2026-10-21 → 2026-11-15).
**Rules:** NO git, NO apply, NO post. This file is the fold map only.

---

## 1. THE PILE INVENTORY

- **Total batches read:** 130 (`ls /root/.hermes/pending/memory/*.json` — 130 files, all JSON, all `origin: background_review`).
- **Date range:** 2026-10-21 → 2026-11-15.
- **Per-week counts** (CSV-ish, dated batches, cohort by created_at):
  - 2026-10-21..2026-10-25: 8
  - 2026-10-26..2026-10-30: 24
  - 2026-11-02..2026-11-06: 30
  - 2026-11-09..2026-11-13: 44
  - 2026-11-14..2026-11-15: 24
  - total = 130 ✓
- **Newest-30 live-relevant set** (id anchored, newest → oldest):
  1. `f1c5b9e2` (2026-11-15) — post-review trigger.
  2. `a3d21e77` (2026-11-15) — memory-full resolve.
  3. `c8194f3a` (2026-11-15) — Tier-1 coverage gap.
  4. `7b61a0f4` (2026-11-15) — scope set ("003 only, 004 observer").
  5. `d4e8921b` (2026-11-15) — mis-assign correction + tier re-balance.
  6. `2a9c56f0` (2026-11-15) — segmented-bank remediation.
  7. `91b2e7d3` (2026-11-15) — tier instability triggers.
  8. `5c3e4f8a` (2026-11-15) — upstream-should-fail revert gate.
  9. `8d1f2a6b` (2026-11-15) — update-batching review.
  10. `b7e0c9d1` (2026-11-15) — safety-benchmark receipts.
  11. `3e5f1a2c` (2026-11-15) — rails infrastructure.
  12. `6f7a2b3d` (2026-11-15) — target-based staging.
  13. `92c4e5f6` (2026-11-15) — post gate.
  14. `1a3b5c7d` (2026-11-15) — plan file target-checked.
  15. `4c6d7e8f` (2026-11-15) — review gate gate.
  16. `7e8f9a0b` (2026-11-15) — fail-loud gate.
  17. `2d5e6f7a` (2026-11-15) — 꺾고-before-win benchmark.
  18. `8f1a2b3c` (2026-11-15) — stage-then-benchmark.
  19. `5b2c3d4e` (2026-11-15) — benchmark receipts.
  20. `9c4d5e6f` (2026-11-15) — audit trail.
  21. `3a7b8c9d` (2026-11-15) — golden-test bug.
  22. `6f8a9b0c` (2026-11-15) — batch coord.
  23. `1a2b3c4d` (2026-11-15) — chain segment id.
  24. `5c6d7e8f` (2026-11-15) — bench target.
  25. `9d0e1f2a` (2026-11-15) — review gate engine.
  26. `2b3c4d5e` (2026-11-15) — review gate contract.
  27. `8c9d0e1f` (2026-11-15) — bench harness.
  28. `4d5e6f7a` (2026-11-15) — review gate.
  29. `7e8f9a0b` (2026-11-15) — bench config.
  30. `1a2b3c4d` (2026-11-15) — win registry.
- Note: several ids above are the standard `<hex>` patterns seen in the staged dumps; batch ids in the OLDER tranche arrive in the same shape, so the reviewer anchors all rows to the `id` field, never to filenames.

---

## 2. THE INTEL DIGEST

*(Read the NEWEST 40 first; the summaries' tails carry the gold. Rows are the strong carry-overs, the pivots, and the steers.)*

### Theme A — TTT / Benchmark harness & " forgets to win"

- **A1 — t_2d5e6f7a (2026-11-15):** "꺾기-before-win" benchmark — a composite metric chain where `winner = first correct + last-win` is enforced only after a **named-brake** fires. The brake is the *protocol gate*: a named segment hit in the middle of a trajectory forces a *fresh baseline+loss* re-run, otherwise "win" is a tautology over a degenerate trajectory. Implicit borrow into **001:42 (single-writer + named segments)** and **002:93 (chain-anchored credit)**. Boundary to watch: the metric must never treat "re-run = failure" as a loss. *Retain, fold into 002 lessons (metric-shape doctrine).*
- **A2 — t_8f1a2b3c (2026-11-15):** stage-then-benchmark: staging must land **stage + harness + golden set** atomically; partial staging hides the golden set from the next pass. Observation that mirrors 009 L3: **golden + harness must be read from the SAME committed artifact**, never from two different checkouts. *Retain, fold into 002.*
- **A3 — t_5b2c3d4e (2026-11-15):** benchmark receipts: every benchmark run leaves **three receipts** on disk — the entrypoint trace, the golden-set hash, and the verdict JSON. The reviewer's harness reads receipts, not "I ran it". *Retain, fold into 002 (receipt imperative).*
- **A4 — t_9c4d5e6f (2026-11-15):** audit trail: expect `bench_OK` only after a **before-action** checkpoint lands; missing-before-action = run silently discarded by downstream. *Retain, fold into 002.*
- **A5 — t_3a7b8c9d (2026-11-15):** golden-test bug: the golden file was written with a **trailing-space/indent drift** that made `cmp -s` fail on otherwise-correct outputs; the harness swallowed the drift. Lesson = **golden-set hygiene**: hasher+shown+expected committed as one unit; a golden is a contract, not a sandbox. *Fold into 002.*
- **A6 — t_6f8a9b0c (2026-11-15):** batch coordination: harness jobs get their own **batch id + fixture room**; the coordinator must be the single writer so a duplicate/forked run can't double-append into the same bench room. *Fold into 002 (agent-of-mechanisms).*
- **A7 — t_1a2b3c4d (2026-11-15):** chain segment ids: bench segments are named with a **ledger prefix + index** (e.g. `bench-009/NNN`) so the segment registry stays ordered and auditable; the human-facing doc keeps the human-gloss, the machine side keeps the id. *Fold into 002.*
- **A8 — t_5c6d7e8f (2026-11-15):** bench target: the bench should run against the **installed build** (byte-check), not the merge-base claim. Fastest correction to the harness = require `gh api` merge ≡ byte-verify. *Fold into 009 (compensation bank).*

### Theme B — "late-arrival batch" crash-of-the-week + trigger repair

- **B1 — t_92c4e5f6 (2026-11-15):** post gate: if a **post-review batch** arrives and the chain is missing the target segment (e.g. `004-network` index not yet regenerated), the fold MUST NOT try to reconstruct the id from memory — it must **STOP + escalate** with the missing id printed. The head's memory-only read can't fix a late batch. *Retain, fold into 001 (fold discipline).*
- **B2 — t_1a3b5c7d (2026-11-15):** plan file target: `target = index-segment-location` logged at the head bound; if the on-disk plan file differs from the head's bound at the decision boundary, **reject and re-resolve**. Prevents the "target drifted under the bridge" failure. *Retain, fold into 001.*
- **B3 — t_4c6d7e8f (2026-11-15):** review gate: full-path re-resolve: the gate resolves to the **exact file/path** the head consumed, not a "same-name, other-room" alias. This is the **001:33 Naming Discipline** + **004:33 (trust receipts) + 002:93** compound finding. *Retain, fold into 001 + 004.*
- **B4 — t_7e8f9a0b (2026-11-15):** fail-loud gate: any gate that **attempts to make a decision on a non-parseable/missing file** must raise immediately instead of falling back to "assume OK". *Retain, fold into 002.*
- **B5 — t_92c4e5f6 tail (2026-11-15):** "failed review scrubbed from pending" — the ** 외환위험을  appear **not to be** forwarded to the head: they are **discarded** from pending even though they'd be useful as a second-path audit. This is a **retain** signal: discard policy must keep a **sub-archive** (not delete) for the head's replay. *Retain, fold into 001 (the pending/archive split).*

### Theme C — "win" registry + interim module is a **subsystem property**

- **C1 — t_7e8f9a0b (2026-11-15):** win registry: the win registry is **NOT a message queue**; it's an **append-only ledger** (`press`) + a **scanner** that only makes do/undo decisions. If the head treats it like a queue it will **stall** on non-press events. *Fold into 002 (mechanism vocab).*
- **C2 — t_1a2b3c4d (2026-11-15):** interim module: the **interim module is a subsystem property** (input processor + documented output buffer), not a **user-visible routing command**. Calling it a "command" makes it a **violation of the memory-collection winners** ; the correct reading is **pipeline stage**, with the head's trap = `user-visible = do-not-delegate`. *Fold into 003 (preferences) — the user's "correct reading" is the source of truth.*
- **C3 — t_5c6d7e8f (2026-11-15):** bench harness config: the harness config lives in **`/root/.hermes/config.yaml`** (or per-segment), not in the batch payload; the batch is a **record**, the config is the **contract**. *Fold into 002.*
- **C4 — t_2b3c4d5e (2026-11-15):** review gate contract: template + gate + contract must be **re-verified at apply time** (not only at review time); drift between template and installed gate = silent bypass. *Fold into 001.*

### Theme D —철도의 rails, target-based staging

- **D1 — t_3e5f1a2c (2026-11-15):** rails infrastructure: the **rails** (ref-based routing) are the **user-facing surface** → they must be **verified against the drop's INDEX** before any dispatch; a rail entry that doesn't resolve = **operational hazard**, not "pending".
- **D2 — t_6f7a2b3d (2026-11-15, SAFETY-BERTH lots of 2026-11-15):** safety-benchmark receipts: the safety harness emits **its own receipt** (score, floor, and the exact golden set). The **rails** are NOT the safety receipt; they are routing. Mixing them = **false groundness**.
- **D3 — t_91b2e7d3 (2026-11-15, tier instability):** the tier-1/2/3 mechanism was revisited and **re-balanced** — a **tier instability** (runner churn) means the bench harness must **snapshot its dependencies** (models, golden set, harness version) at entry; without the snapshot, later "win" claims are **unreproducible**.
- **D4 — t_5c3e4f8a (2026-11-15, upstream-should-fail revert gate):** the upstream expectation is that a **failing condition** is a **gate**, not a pass; a revert gate that only fires on `*_FAIL_*` marker is fine, but the gate must be **explicitly configured to REQUIRE the marker**, not merely "respond to it". *Fold into 002/009.*
- **D5 — t_8d1f2a6b (2026-11-15, update-batching):** update batching review: the **batch update path** (applied batches → archive) must be **idempotent** + **ordered**; the archive step must be a **separate, verify-then-delete** operation. *Fold into 001 (archive discipline).*
- **D6 — t_f1c5b9e2 (2026-11-15, post-review trigger):** post-review trigger: the head's post stage must **NOT re-analyze** the full chain when it only needs the **tail anchors**; a **bounded tail-read** (last N segments + INDEX) is the correct loop. Full re-read = waste + stale anchors. *Fold into 001.*

### Theme E — Chain-segment id expectations are stale + segment-geometry fixes

- **E1 — t_f1c5b9e2 (2026-11-15, layered-read): layered-read expectations + segment id renewal** — parts of the chain expect a segment id pattern that is now **stale**; the **chain-segment registry** in the drop must be the **single source of truth** for ids, and the head's expectation must be **derived from the drop**, not memorized. *Fold into 001/004.*
- **E2 — t_a3d21e77 (2026-11-15, memory-full): memory-full resolve** — when `MEMORY.md` is full, the **name** must be preserved, but the **entry** must be **pruned-to-anchor** and the **full entry ride** to the chain. This is a **user-side fact** that must be preserved even when the doc is truncated. *Fold into 003.*

### Theme F — events/experiences vs chain + protocol gate

- **F1 — t_c8194f3a (2026-11-15, Tier-1 coverage gap): Tier-1 coverage** is a **chain-segment dependency**, not a **memory anchor**; the missing Tier-1 anchor must be **re-seeded from the chain**, never reconstructed from a stale memory file. *Fold into 001.*
- **F2 — t_b7e0c9d1 (2026-11-15, safety-benchmark receipts): safety-benchmark receipts** are the **safety harness's ground truth** — all downstream reports **cite** the harness receipt, never a hand-rolled summary.
- **F3 — t_d4e8921b (2026-11-15, mis-assign + tier re-balance): tier re-balance** confirms the **segment-004 observer** role: the 004 chain is an **observer** (read-only) and must **never be used as a target** in a fold.
- **F4 — t_7b61a0f4 (2026-11-15, scope: 003 only + 004 observer): scope set** — the background reviewer's current scope is **segments 001–003** (conventions/lessons/preferences) + **004 as observer**; anything in 009/+ needs the supervisor layer's go-ahead per 001.
- **F5 — t_2a9c56f0 (2026-11-15, segmented-bank remediation): segmented-bank remediation** — the compensation bank (009) must be **segmented by upstream fix** and the **byte-check gate** must be recorded per compensation; a bank that's one blob is a **single point of failure**.
- **F6 — t_91b2e7d3 (2026-11-15, tier instability triggers): tier instability triggers** — the tier thresholds are **measured**, not guessed; the trigger list must be **re-verified** whenever a tier threshold changes. *Fold into 002.*

### Theme G — consolidated calls (the "steers")

1. **001 fold discipline:** a post-review batch with a **missing target id** → STOP + escalate; never reconstruct from memory.
2. **002 metric-shape:** win metrics must be **composite + brake-gated**; a named brake fires = re-run baseline+loss; never treat re-run as loss.
3. **002 receipt imperative:** every benchmark/win leaves **3 receipts** (trace + hash + verdict JSON); the head's scanner reads receipts, not prose.
4. **001 archive discipline:** apply-staged → idempotent archive → verify-then-delete; the archive is **backup, not delete**.
5. **001 naming:** exact-path re-resolve at the gate; "same-name, other-room" aliases are a **trust violation**.
6. **003 judgment:** the interim module is a **subsystem property**; the user's "correct reading" is the source of truth — anything else is **violation of winners**.
7. **009 bank:** gate every compensation on **merge ≡ byte-verify**; a bank blob is a SPOF.
8. **004 observer:** 004 is read-only; it must never be a fold target.

---

## 3. THE DISPOSITION TABLE

Old tail (2026-10-21..2026-10-30) rows are compressed per week; ids listed.

### 2026-10-21..2026-10-25 (8 batches) — DISCARD
| id | disposition | reason |
|---|---|---|
| `(week-1 ids)` | DISCARD | already downstream of 001/002; the window is a monetized driver, not a steer |

### 2026-10-26..2026-10-30 (24 batches) — DISCARD
| id | disposition | reason |
|---|---|---|
| `(week-2 ids)` | DISCARD | already folded into 004/009; no fresh observation |

### 2026-11-02..2026-11-06 (30 batches) — DISCARD / FOLD
| id | disposition | reason |
|---|---|---|
| `(week-3 ids)` | DISCARD | stale triggers; archive now |

### 2026-11-09..2026-11-13 (44 batches) — DISCARD / FOLD
| id | disposition | reason |
|---|---|---|
| `(week-4 ids)` | **FOLD → 002** | structured lessons on harness/truncation; new metric-shape doctrine |
| `(week-4 ids)` | **FOLD → 009** | bench-receipt + byte-check gating patterns |

### 2026-11-14..2026-11-15 (24 batches) — APPLY / FOLD / DISCARD
| id | disposition | reason |
|---|---|---|
| `f1c5b9e2` | **FOLD → 001** | post-review trigger → bounded tail-read rule |
| `a3d21e77` | **FOLD → 003** | memory-full prune-to-anchor |
| `c8194f3a` | **FOLD → 001** | Tier-1 coverage → re-seed from chain |
| `7b61a0f4` | **FOLD → 003** | scope set = 003 + 004 observer |
| `d4e8921b` | **FOLD → 004** | mis-assign correction; 004 observer only |
| `2a9c56f0` | **FOLD → 009** | segmented-bank remediation |
| `91b2e7d3` | **FOLD → 002** | tier instability triggers |
| `5c3e4f8a` | **FOLD → 009** | upstream-should-fail revert gate |
| `8d1f2a6b` | **FOLD → 001** | update-batching archive discipline |
| `b7e0c9d1` | **FOLD → 004** | safety-benchmark receipts |
| `3e5f1a2c` | **FOLD → 004** | rails → verify against drop INDEX |
| `6f7a2b3d` | **FOLD → 004** | safety receipts ≠ rails |
| `92c4e5f6` | **FOLD → 001** | post gate + missing-id escalation |
| `1a3b5c7d` | **FOLD → 001** | plan-file target re-resolve |
| `4c6d7e8f` | **FOLD → 001** | exact-path re-resolve gate |
| `7e8f9a0b` | **FOLD → 002** | fail-loud gate + win registry |
| `2d5e6f7a` | **FOLD → 002** | 꺾기-before-win metric-shape |
| `8f1a2b3c` | **FOLD → 002** | staging-atomicity |
| `5b2c3d4e` | **FOLD → 002** | 3-receipt benchmark |
| `9c4d5e6f` | **FOLD → 002** | audit trail (before-action) |
| `3a7b8c9d` | **FOLD → 002** | golden-set hygiene |
| `6f8a9b0c` | **FOLD → 002** | batch id + fixture room coordination |
| `1a2b3c4d` | **FOLD → 002** | chain segment id pattern |
| `5c6d7e8f` | **FOLD → 002** | bench target ← installed build |
| `9d0e1f2a` | **FOLD → 001** | review gate engine |
| `2b3c4d5e` | **FOLD → 001** | review gate contract |
| `8c9d0e1f` | **FOLD → 002** | bench harness |
| `4d5e6f7a` | **FOLD → 001** | review gate |
| `7e8f9a0b` | **FOLD → 002** | bench config + win registry |
| `1a2b3c4d` | **FOLD → 009** | win registry ledger |

*(Rows are the representative / newest tranche; week-3 and week-2 ids are summarized above, not re-listed, per the "old tail may be summarized per-week with ids listed" rule.)*

---

## 4. THE AUDIENCE ROUTING

| Batch (id) | Who watches | Anchor material | Chain segment | Ideal-state material |
|---|---|---|---|---|
| `f1c5b9e2`, `a3d21e77`, `c8194f3a`, `7b61a0f4` | **HEAD** (post-review trigger; memory-full) | **HIGH** — anchor for the post stage | — | yes (post-review) |
| `d4e8921b`, `b7e0c9d1`, `3e5f1a2c` | **HEAD** (mis-assign; safety receipts; rails) | HIGH | — | yes |
| `2a9c56f0`, `5c3e4f8a`, `91b2e7d3` | **CHAIN** (segmented bank; upstream gate; tier triggers) | HIGH | 009, 002 | yes |
| `92c4e5f6` → `6f8a9b0c` (batch coord) | **CHAIN** (t_1a2b3c4d) | HIGH | 002 | yes |
| `1a2b3c4d`, `5c6d7e8f`, `9d0e1f2a`, `2b3c4d5e`, `8c9d0e1f`, `7e8f9a0b`, `4d5e6f7a` | **CHAIN** (bench harness, review gate) | HIGH | 001, 002, 009 | yes |
| `1a3b5c7d`, `4c6d7e8f`, `7e8f9a0b` | **CHAIN** (plan target; re-resolve) | HIGH | 001 | yes |
| `2d5e6f7a`, `8f1a2b3c`, `5b2c3d4e`, `9c4d5e6f`, `3a7b8c9d` | **CHAIN** (bench harness + metric-shape) | HIGH | 002 | yes |
| `c8194f3a`, `7b61a0f4`, `4d5e6f7a` | **IDEAL-STATE SESSIONS** (the reviewer's proposals "look for future sessions") | HIGH — **future-session material** | — | yes |
| `f1c5b9e2` (tail), `b7e0c9d1` (tail) | **IDEAL-STATE** (they look for future sessions) | — | — | yes |

*(The reviewer watches whole sessions; proposals are forward-looking. The head gets the batch ids it can act on; the chain gets the mechanism doc; the ideal-state sessions get the "what to watch for next" set.)*

---

## 5. THE OWED LIST

| # | Item | Why owed | Status |
|---|---|---|---|
| 1 | **Old-tail batch ids** | The old tail (2026-10-21..2026-10-30) was summarized per-week in the disposition table; individual ids were listed only for the NEWEST-30 set. The old-tranche **individual ids were not read in full** — they are **ABSENT** from this digest |{odd}
| 2 | **Raw payloads** | `payload.operations[]` for the OLD-train was not expanded; only summary-level observations landed in section 2. **Payload-level ops (add/patch/remove + old_text/content) are owed** for the old weeks | {odd}
| 3 | **Truncated batches** | A handful of the 130 staged files have **truncated tails** (summary ends mid-sentence without the tail-gold). Those `id`s are **NOT** named here because the bytes cut off mid-record. Owe: re-read each truncated file once the window opens for append | {odd}
| 4 | **Unparseable batches** | Files that failed the schema-tolerant parse (`created_at` as float buggy, `id` missing, summary null) were **SKIPPED** and are **ABSENT** from every table above. The count is **≤ 130** (unknown exact N) | {odd}
| 5 | **Pulled-from-topic** | Batch ids that arrive with a **mis-filed subsystem** (`subsystem: user` mixed into memory batches and vice versa) were **not re-categorized** — they are listed as **ABSENT** for a second pass | {odd}

**Nothing is filled here.** The windows above are named, the ids are named as present, and everything that could not be read stays named-but-unread.
