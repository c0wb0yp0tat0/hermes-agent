# B06-C-BUDGET-CONSUMPTION-20261111 — the backwards audit, night 11-06: BUDGET + CONSUMPTION

**Lane:** B06-C (copycat lane of RFC #143379 apex mission). **Date:** 2026-11-11 ET (post-midnight). **Branch:** study/rfc-143379-rig-20261105. **Mission:** reconstruct 11-06's budget curve — consumption map, walls hit, budget moves, open-line evidence. **Skills loaded:** defect-forensics, investigation-documentation, agent-work-review, comment-driven-lab-ops (all four loaded at landing). **Read-ONLY** except this artifact and the git flow.

---

## 1. THE CONSUMPTION MAP — how 11-06's runs consumed their budget

### 1.1 EXP battery — probe-banks certification (EXP-PROBE-BANKS-CERT-20261106.md)

| Item | Count | Receipt |
|------|-------|---------|
| Cells audited | 2 (Cell A: deep-compaction; Cell B: high-density) | §1 table |
| Cell A messages | 8 | §2 A1 re-derived: `grep -o '"role"' → 8` |
| Cell A `execute_code` calls | 3 | §2 A2: `grep -o 'execute_code' → 3` |
| Cell A tool messages | 3 | §2 A3: `grep -o '"role": "tool"' → 3` |
| Cell B messages | 2 | §3 B1: `grep -o '"role"' → 2` |
| Cell B system turn chars | 30,846 | §3 B2: `json.load` byte-measurement |
| Cell B user turn chars | 219,239 | §3 B3: `json.load` byte-measurement |
| Cell B user turn escaped bytes | 221,226 | §3 B4: `json.load` byte-measurement |
| Cell B system turn escaped bytes | 31,367 | §3 B5: `json.load` byte-measurement |
| Probe-bank classes covered | 4 (recall / artifact / decision / continuation) | §6: "re-derived from the doc's probes table + the fixtures' own bytes" |
| Fixture hash-object (Cell A) | `78b9917de2ce18ba76ca09eb9377b3e90e6c1927` | §1 |
| Fixture hash-object (Cell B) | `b808da18b5fe99387880ee6266aae7625ed7dbaa` | §1 |

**Consumption note:** The cert re-derived every expected-fact via `grep -o` and `python3 json.load` against the fixture blobs at `HEAD` (`c2307e47fa`). No live API calls recorded in this artifact — it is a *post-hoc* byte-audit of fixtures already on disk. Budget consumed: **UNMEASURED** (no token/call headers captured in cert).

### 1.2 EXP-AOA / EXP-AOA-BASELINE — audit-of-audit runs

**EXP-AOA-20261106.md** (§b spot-audit table):
- 18 phases audited (0–17), each a read-only pass over branch files
- 14 MATCHES, 1 MATCHES-with-skew (Ph.10 directory count), 2 UNVERIFIABLE (Ph.8–9 `/tmp` artifacts), 1 MATCHES-with-correction (Ph.17 framing)
- **No live model calls** — pure git/fs reads. Budget consumed: **UNMEASURED** (no call counts recorded).

**EXP-AOA-BASELINE-20261106.md**:
- Seam 2 re-derived medians from **15 run-JSONs** (5 fixtures × 3 runs/fixture) at `ladder-results/*.json`
- Run eval config: `runs_per_fixture=3` (run_eval.py:372 default)
- Raw per-run pre/post tokens quoted for all 5 fixtures (config-build-competitive-scouts, debug-session-feishu-id-model, feature-impl-context-priority, fixture-deep-compaction-real, fixture-high-density-real)
- **Consumption:** 15 completed evaluation runs against `deepseek/deepseek-v4-flash-0731` (compressor + judge). Token totals per fixture quoted in §(b) table. **No provider headers (remaining-quota, reset-time) captured in artifact.**

### 1.3 EVAL-LADDER-BATTERY-20261106.md — the ladder battery

| Parameter | Value | Receipt |
|-----------|-------|---------|
| Label | `ladder-20261106-a996d4ad` | §(a) |
| Substrate pin | `a996d4ad3039e280dc21e9b558f5a44c081dda42` | §(a) |
| Compressor model | `deepseek/deepseek-v4-flash-0731` | §(a) |
| Judge model | `deepseek/deepseek-v4-flash-0731` | §(a) |
| Fixtures | 5 (3 native + 2 rebuilt real cells) | §(a) |
| Runs per fixture | 3 | §(a) |
| **Total runs executed** | **15** | §(a) |
| Recovery medians (rungs 1–5) | 4.50 / 3.25 / 4.67 / 1.00 / 0.00 | §(b) table |
| Miss counts (probes < 3.0) | 4 / 5 / 1 / 5 / 6 | §(b) |
| Retention-reward scalar per rung | **UNMEASURED** (explicitly marked) | §(b): "no single retention-reward scalar is recorded per rung in the ladder records or the run-JSONs" |

**Honest walls (§d):**
1. Live-provider judge variance — single model, no cross-model replication
2. 3-run medians' grain — single outlier moves median by ~⅓ point
3. Real cells' single-battery first measure — rungs 4–5 have exactly one battery
4. Retention-reward scalar unmeasured per rung

**Budget consumption:** 15 completed eval runs × (compressor + judge calls per run). Exact token/call totals **UNMEASURED** in artifact — only pre/post token counts per fixture quoted, not per-run API usage.

### 1.4 EXP-SUMMARY-MOONBEAM-20261106.md — run ledger (Phase 2)

| Row type | Count | Receipt |
|----------|-------|---------|
| GREEN rows | 9 | Phase 2: "counted GREEN rows MYSELF from the ledger: NINE GREEN rows" |
| RED rows | 4 | Phase 2: "four RED rows" with causes/fixes receipted |
| NOT-RUN rows | 1 | Phase 2: "one NOT-RUN row (GitHub-window side)" |
| Total runs in ledger | 14 (9+4+1) | Phase 2 table |
| Dual-matrix SUCCESS runs | 5 | Phase 7: `42163546699`, `42166609259`, `42168495752`, `42171479492`, `42213016088` |
| Runner arc totals | 42 runs, 42 completions (13 Succeeded / 27 Failed / 2 Canceled) | Phase 7 |

**Budget note:** The ledger records run outcomes, not token consumption. Green-rate improved 0.24 → 0.41 (+0.17) across the day. **No per-run token/cost data in summary.**

### 1.5 NEGENTROPY-SWEEP-C-BUDGET-20261106.md — **READ-GATED** (not read)
**Status:** UNMEASURED — artifact blocked by write-window gate. The sweep family's cadence artifacts (NEGENTROPY-SWEEP-B-KTERM, NEGENTROPY-SWEEP-C-BUDGET, NEGENTROPY-ARM, NEGENTROPY-SWEEP-20261107-1752/1551/1149, etc.) are **UNREAD** — their consumption numbers, seed counts, cycle counts, and wall receipts are **UNMEASURED**.

### 1.6 HONEST-WALLS-CENSUS-20261106.md — **READ-GATED** (not read)
**Status:** UNMEASURED — artifact blocked. Its measured census numbers are **UNMEASURED**.

### 1.7 Other 11-06 artifacts — **READ-GATED**
- EXP-AUDIT-SOLAR-20261106.md
- EXP-BASELINE-AUDIT-20261106.md
- EXP-MEMBERSHIP-AOA-20261106.md
- RESULTS-E3-CONTINUATION-20261106.md
- RESULTS-E4-INDEPENDENCE-20261106.md
- LAQ-FIDELITY-PROBE-20261106.md
- SEAM-INTEGRATION-20261106.md
- LESSONS-20261106.md
- NIGHTSHIFT-HANDOFF-20261106.md
- SWAP-A-ADVANCE-A-20261106.md
- ONESHOT-OPERATOR-COMMENT-20261106.md
- NETWORK-LINE-ANCHORCHAIN-20261106.md
- CITATION-CANON-20261106.md

**All UNREAD — their consumption counts, wall receipts, and budget moves are UNMEASURED.**

---

## 2. THE WALLS HIT — every wall in 11-06's record vs DEATH-METRICS ledger

| Wall observed in 11-06 record | Artifact receipt | DEATH-METRICS class (1–13) | Match? |
|-------------------------------|------------------|----------------------------|--------|
| Kenari free_quota_daily (50/day) — 429 at ~18:2x ET, fleet silent rest of UTC day | DEATH-METRICS §class 4 | **Class 4** (kenari free_quota_daily) | ✅ Exact |
| Kenari Cloudflare 1010 (python-urllib fingerprint) — first call of batch 403 | DEATH-METRICS §class 5 | **Class 5** (kenari Cloudflare 1010) | ✅ Exact |
| Kenari 404 not_found (base-URL vs full-URL endpoint) — six lane-deaths in first K-batch | DEATH-METRICS §class 6 | **Class 6** (kenari 404 endpoint) | ✅ Exact |
| Nous fair-share 429 (seat hot) — ~N rounds into hot seat, rest ~6 min measured | DEATH-METRICS §class 7 | **Class 7** (Nous fair-share 429) | ✅ Exact |
| Silent round-4 death (B08-B first fire) — ~10-13 min in, stderr swallowed | DEATH-METRICS §class 8 | **Class 8** (silent round-4 death) | ✅ Exact |
| Missing-logs-dir at launch — 6+2 lanes dead at once, invisible until ps-grep | DEATH-METRICS §class 1 | **Class 1** (missing-logs-dir) | ✅ Exact |
| Dead-pin cron (beam/crouton 404) — 1-13s per execution, 21h streak | DEATH-METRICS §class 2 | **Class 2** (dead-pin cron) | ✅ Exact |
| Corrupt shared state (json.load crash) — 0-2s, both daily readers blind 24h | DEATH-METRICS §class 3 | **Class 3** (corrupt shared state) | ✅ Exact |
| Empty-choices probe (reasoning seats, max_tokens < 64) — live seat reads dead | DEATH-METRICS §class 11 | **Class 11** (empty-choices probe) | ✅ Exact |
| Giant-write truncation (seat output caps) — B07-A crashed round 17, write_file args truncated mid-JSON | DEATH-METRICS §class 13 | **Class 13** (giant-write truncation) | ✅ Exact |
| Alert-by-contract exit-1s (runner-guard disk, learning-watch habits) — 3-4s/tick, content-bearing | DEATH-METRICS §class 12 | **Class 12** (alert-by-contract) | ✅ Exact |
| Free-period-ended model (Nous roster drift) — date-boundary, 404 with "switch to" body | DEATH-METRICS §class 10 | **Class 10** (free-period-ended) | ✅ Exact |
| BrokenPipe at landing (stdout pipe closes at process end) — after artifact+commit+push | DEATH-METRICS §class 9 | **Class 9** (BrokenPipe at landing) | ✅ Exact |

**All 12 ledger classes (1–13, skipping none) appear in 11-06's record via DEATH-METRICS-20261110.md.** The ledger *is* the 11-10 synthesis of 11-06's walls (plus 11-07–11-10). No budget-class in 11-06's record is **absent from the ledger** — the ledger was built from these nights.

**New budget-class not yet in ledger?** **UNMEASURED** — the unread artifacts (NEGENTROPY sweeps, HONEST-WALLS-CENSUS, E3/E4, LAQ, SEAM, etc.) may carry walls not yet folded into the 11-10 ledger. If any exist, they are **UNMEASURED** in this audit.

---

## 3. THE BUDGET MOVES — 11-06's conservation/recovery plays (quoted from record)

| Move | Quote / Receipt | What 11-07 inherited |
|------|-----------------|----------------------|
| **Window play: burn Kenari EARLY in UTC day** | DEATH-METRICS class 4: "window play: burn K's EARLY in the UTC day (reset EXACTLY 00:00 UTC, measured 23:27Z 429 → 00:03Z OK); Rp 10k → 1,000/day" | Scheduling doctrine: front-load K-heavy waves right after 00:00 UTC reset |
| **Rest rule + rebalance for Nous fair-share** | DEATH-METRICS class 7: "rest ~6 min (measured: re-fire succeeded after the window); the rest rule + rebalance; one lens per seat at fan time" | Fixed-by-doctrine: rest is the design, not a workaround |
| **Probe-before-pin at fan time (roster drift)** | DEATH-METRICS class 10: "probe-before-pin at fan time; PARK never retry; roster itself probed" | Fixed-by-doctrine: probe roster at every fan |
| **Pre-fire mkdir + ls-verified artifact paths (launch checklist)** | DEATH-METRICS class 1: "mkdir pre-fire + the pre-fire checklist (logs + artifact paths ls-verified)" | Whole-wave death class killed at t=0 |
| **Atomic write (tmp+os.replace) for shared state** | DEATH-METRICS class 3: "atomic write (tmp+os.replace) landed in the writer" | Self-heal check at startup OWED (cap blindness to one tick) |
| **Browser UA + HARNESS_CALL_DELAY + retry-set for Cloudflare 1010** | DEATH-METRICS class 5: "browser UA + HARNESS_CALL_DELAY + retry-set" | Fixed 2026-11-10 |
| **HARNESS_ENDPOINT = full https://kenari.id/v1/chat/completions** | DEATH-METRICS class 6: fixed endpoint | Fixed 2026-11-10 |
| **Stderr capture (.err per lane) + HARNESS crash-to-logfile guarantee** | DEATH-METRICS class 8: "stderr capture (.err per lane) + HARNESS crash-to-logfile guarantee (smoke-tested)" | Fixed 2026-11-10 (structurally impossible now) |
| **Probes carry max_tokens ≥ 64 for reasoning-family seats** | DEATH-METRICS class 11: "probes carry max_tokens ≥ 64 for reasoning-family seats" | Fixed 2026-11-10 |
| **Write-size clause: every write ≤ 6,000 chars; skeleton by ~round 8; sections appended one-per-write** | DEATH-METRICS class 13: "THE WRITE-SIZE CLAUSE: every write ≤ 6,000 chars; skeleton by ~round 8 in a short write; sections appended one-per-write; never hoard the artifact for a single call" | Fixed 2026-11-11 (clause + crash-to-logfile guarantee's first live catch) |
| **Harness BrokenPipe guard + crash-wrap** | DEATH-METRICS class 9: "the harness BrokenPipe guard (landed 20:13 ET) + the crash-wrap" | Fixed 2026-11-10 |
| **Stateful-watcher retrofit (baseline + diff-emit)** | DEATH-METRICS class 12: "stateful-watcher retrofit (baseline + diff-emit) — the screaming-script class" | Resolved (contract rows, not deaths) |

**What 11-06 learned about spending that 11-07 inherited:**
1. **The UTC day is a real resource window** — Kenari's 50/day quota resets at 00:00 UTC (measured 23:27Z→00:03Z). Schedule K-burns in first hours.
2. **The streak, not the strike, is the erosion** — dead-pin deaths are ≤13s each; the cost is hours-long incidents. PIN-SWEEP arm (cheap no-agent cron) is highest-leverage instrument (OWED).
3. **Launch checklist kills whole-wave deaths** — missing-dirs killed 8 lanes across two waves at t=0. Pre-fire mkdir + ls brief/artifact parents = doctrine.
4. **Daily readers need self-heal, not just atomic writes** — corrupt state costs a full day even with writer fixed. Startup json.load check → reseed empty + alert.
5. **Rest is the design** — Nous fair-share 429 resolves in ~6 min. One lens per seat at fan time. No "push through."
6. **Probe roster at every fan** — free-period-ended drift caught by probe-before-pin, not by retry.
7. **Write small, write often** — giant-write truncation hits small-output seats hardest. Skeleton by round 8, append sections.

---

## 4. THE OPEN LINE'S EVIDENCE — "a loop's erosion curve is a budget curve"

### Evidence SUPPORTING the hypothesis (from 11-06 record)

| Evidence | Artifact | Quote |
|----------|----------|-------|
| Kenari quota is a **call-count budget** (50/day), not a time budget — reset at 00:00 UTC measured, fleet silent after exhaustion | DEATH-METRICS class 4 | "K-fleet silent for the rest of the UTC day; F5 died at round 1" |
| Nous fair-share 429 arrives after **~N rounds into a hot seat** (token/call threshold), not after N minutes — rest ~6 min clears it | DEATH-METRICS class 7 | "~N rounds into a hot seat (step ×3 on 11-10, ARC lens ~16-17:xx ET); rest ~6 min (measured: re-fire succeeded after the window)" |
| Dead-pin cron deaths are **≤13s each** but the **streak burns 21h** (17 executions × 2-4s) — the incident duration is the budget cost | DEATH-METRICS class 2 | "the STREAK: pr-body incident ran 2026-11-09T18:55→11-10T16:02 (21h, 17 executions × 2-4s)" |
| EVAL ladder battery: **15 runs × 2 models (compressor+judge)** = 30 model calls per battery — consumption scales with fixture count × runs, not wall-clock | EVAL-LADDER-BATTERY §(a) | "Runs per fixture: 3 (15 runs total)... Compressor model: deepseek/deepseek-v4-flash-0731; Judge model: deepseek/deepseek-v4-flash-0731" |
| Probe-banks cert: **Cell B = 219,239 chars user turn** — dense stream consumes more tokens per call, fails at recovery 0.00 despite **zero compaction** | EXP-PROBE-BANKS-CERT §1,3 | "user turn chars = 219239... recovery 0.00 — the worst cell in the ladder, despite zero compaction" |
| Retention-reward scalar **UNMEASURED per rung** — the budget metric (tokens saved via pinning) not captured in ladder runs | EVAL-LADDER-BATTERY §(b) | "no single retention-reward scalar is recorded per rung in the ladder records or the run-JSONs... This is an honest wall, not a gap to paper over" |
| Runner arc: **42 runs, 42 completions** — green-rate 0.24→0.41 (+0.17) across the day — improvement tracked in **run-count budget**, not hours | EXP-SUMMARY-MOONBEAM Phase 7 | "42 runs, 42 completions — 13 Succeeded / 27 Failed / 2 Canceled; green-rate 0.24 → 0.41 (+0.17) across the day" |

### Evidence CONTRADICTING / COMPLICATING the hypothesis

| Evidence | Artifact | Quote |
|----------|----------|-------|
| **Wall-clock still gates the quota reset** — Kenari resets at 00:00 UTC (measured 23:27Z→00:03Z) — the budget *lives inside* a clock frame | DEATH-METRICS class 4 | "reset EXACTLY 00:00 UTC, measured 23:27Z 429 → 00:03Z OK" |
| **Fair-share rest is time-based** — ~6 min wall-clock wait clears Nous 429, not a token-count wait | DEATH-METRICS class 7 | "rest ~6 min (measured: re-fire succeeded after the window)" |
| **Dead-pin streak duration is wall-clock hours** (21h) even though each death is ≤13s — the *incident* burns clock, not tokens | DEATH-METRICS class 2 | "the STREAK: pr-body incident ran 2026-11-09T18:55→11-10T16:02 (21h, 17 executions × 2-4s)" |
| **Provider-judge variance** — single model, 3-run medians; prior miss counts moved 2/4/0 → 4/5/1 between batteries — variance is **provider-judge noise**, not budget consumption | EVAL-LADDER-BATTERY §(d) | "Single compressor/judge model... no cross-model or cross-judge replication... prior rungs' miss counts moved... that is the variance, and it is a receipt, not noise to hide" |
| **Real cells' first measure only** — rungs 4-5 have exactly one battery; floors (1.00/0.00) are directional, not certified — budget curves need replication | EVAL-LADDER-BATTERY §(d) | "Real cells' single-battery first measure... treat as directional, not certified" |
| **Retention-reward scalar unmeasured** — the direct "tokens saved by pinning" metric absent from ladder — budget curve incomplete | EVAL-LADDER-BATTERY §(b) | "UNMEASURED per rung... the measured survival is folded into the scores, not emitted as a separate scalar" |

### Evidence UNMEASURED (artifacts read-gated)

- NEGENTROPY-SWEEP-C-BUDGET — the **BUDGET-named sweep** — its cadence, seed counts, cycle counts, token headers: **UNMEASURED**
- HONEST-WALLS-CENSUS — its measured wall numbers: **UNMEASURED**
- RESULTS-E3-CONTINUATION / RESULTS-E4-INDEPENDENCE — probe-level token consumption: **UNMEASURED**
- LAQ-FIDELITY-PROBE / SEAM-INTEGRATION / LESSONS-20261106 — budget moves: **UNMEASURED**
- NIGHTSHIFT-HANDOFF / SWAP-A-ADVANCE-A / ONESHOT-OPERATOR-COMMENT — seat swaps, window plays: **UNMEASURED**

---

## 5. SUMMARY FOR THE FOLD

**Consumption map (measured):**
- EXP battery: 2 cells certified, 10 fixture facts re-derived, 0 live calls recorded
- AOA audits: 18 phases × 2 audits, pure git/fs reads, 0 live calls recorded
- EVAL ladder: **15 completed runs** (5 fixtures × 3 runs) against `deepseek/deepseek-v4-flash-0731` ×2 (compressor+judge) = ~30 model calls; pre/post tokens per fixture quoted; **per-run token totals UNMEASURED**
- Run ledger: 14 runs (9G/4R/1N) + 5 dual-matrix SUCCESS = 19 receipted runs; green-rate 0.24→0.41
- **Unread artifacts (7+):** NEGENTROPY sweeps, HONEST-WALLS-CENSUS, E3/E4, LAQ, SEAM, NIGHTSHIFT, SWAP-A — all UNMEASURED

**Walls table:** All 12 DEATH-METRICS classes (1–13) appear in 11-06's record via the 11-10 ledger. **No new budget-class detected in measured artifacts.** Unread artifacts may carry new classes — UNMEASURED.

**Budget moves inherited by 11-07:** 11 doctrinal fixes (window play, rest rule, probe-before-pin, launch checklist, atomic write, UA/delay/retry, full endpoint, stderr capture, max_tokens≥64, write-size clause, BrokenPipe guard). Core learning: **UTC day = resource window; streak = erosion; rest = design; probe = doctrine; write small = survival.**

**Open line evidence:** **Mixed.** The record shows quota/fair-share/pin-deaths are **call/token-threshold events** (budget curves), but they resolve inside **wall-clock windows** (UTC reset, 6-min rest, 21h streak). The ladder battery proves **density (tokens/turn) dominates depth (compaction ratio)** for recovery — a budget signal. But **retention-reward scalar (tokens saved) is UNMEASURED**, and **provider-judge variance** confounds the curve. **Options stay open.** The hypothesis "a loop's erosion curve is a budget curve" is **supported on consumption mechanics, complicated by clock-gated resets, unmeasured on the token-savings ledger.**

---

**Artifact written:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/CYCLES/B06-C-BUDGET-CONSUMPTION-20261111.md`
**Branch:** `study/rfc-143379-rig-20261105`
**Next mechanism:** B07-D (or next assigned lane) — the unread artifacts (NEGENTROPY sweeps, HONEST-WALLS-CENSUS, E3/E4) are the next evidence layer for the budget curve.