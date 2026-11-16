# NEGENTROPY SWEEP — REGULAR ROW 2026-11-16 (sweep lane, the lock)

**Artifact path:** `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261116-1133.md`
**Branch:** `study/rfc-143379-rig-20261105` (c0wb0yp0tat0/hermes-agent) — verify `ls-remote` before each landing; pull --rebase on rejection.
**Discipline:** read cold once, fold sense, land the row, verify against DISK never the ledger. Nothing public without the user's word; the RFC upstream stays QUIET.

---

## 1. WHAT'S NEW (landings since the last sweep)

- **NEGENTROPY-SWEEP-20261116-0128.md** — new sweep row (the day's ~0128 landing); named but the tail was not re-read after the write-gate opened (absent at read; still counted as the day's scan set).
- **NEGENTROPY-SWEEP-20261116-0329.md.sentinel** — sentinel present, marking the ~0329 sweep pass; a full re-read was blocked by the write-gate.
- **Handoff 013** (chain segment `013-handoff-20261116.md`, minted 02:40 UTC): M1 COMPLETE & apex HELD (`CONFIRMATION-CYCLE-20261115.md` @ `5d195d8b4e`, row `6905713953`); M2 IN FLIGHT (solar, `proc_077d43703f9d`); M3 STAGED/GREEN-LIT; two runners in_progress (avrea battery `43792970990` pinned `5d195d8b4e` + matrix `43792973524`); seats: solar/stepfun/longcat trio (fair-use fan), kenari RESERVED (dots-3-note-preview is the catalog's "spot"), Nemo PAID (anti-stall), Harbor `:44831`, Serene scribe asset. Branch `5d195d8b4e` == remote (verify ls-remote before every landing). Hardenings all live: G14/G15/G16 + launch-precondition receipt. The only intentional bias: bias for action.
- Read-cold facts captured at the lock: harness md5 delta open-verify (`25b3b8a5` live vs banked `23154f50` = G7fix backup; +G13 layer on the head), disk 91% (guard armed ≥92%), kanari read-only (canary rule, never spent), envoy/keyless gateway unreachable at probe (2026-11-15 ~02:05), kenv.free = exactly 3 (solar/longcat/stepfun, correctly pinned all along; the 02:05 "stepfun/longcat free zones ENDED" claim was withdrawn).

## 2. WHAT'S STALE (dead refs / superseded / disk-contradicted)

- **Sweep lines 0518/0522** (rows `6889951863`, plus the per-minute capture) were folded & rowed at SB5+jury time; they are history, not a current signal — the designated 120m arm (`negentropy-sweep-arm.sh`, job `1d96d5a292d1`) keeps the cadence; no duplicate sweep-cron remains.
- **The 02:05 "stepfun/longcat free zones ENDED" claim (SB8 READ)** — probed fresh against the PLAN's pins (`stepfun-5-preview`/`longcat-2.5-preview`): withdrawn. The PLAN's line "nous free = exactly 3" was right the entire time (02:05 EST probes: solar + stepfun + longcat LIVE). Kept only as the roster-correct-I lesson.
- **Harness md5 banked `23154f50...`**: superseded by live `25b3b8a5...` (+G13 layer); the delta to diff at the first fold is OPEN VERIFY, not a failure. Backups `.bak-20261114-G6G7` + `.bak-20261114-G7fix` present on head-side only.
- **Sentinels** (`.sentinel` files under the rig dir): metadata markers, not artifacts — listed for the record, prune nothing.

## 3. WHAT CAN DIE (regenerables, the offload-with-manifest gate holds)

- **Clone caches / old logdirs / duplicate sweep-cron entries**: dead — sweep-cron id removed, designated arm keeps 120m; logdirs are regenerated before fires.
- **Old G6/G7 backup bytes** (`23154f50` vs live `25b3b8a5`): verified against the head-side file, kept on disk; the banked block is the delta, not a prune candidate.
- **The 02:05 SB8 read claim**: dead as a statement, kept as a record row (the roster-correct-I note).

## 4. THE CHAIN CARRY (the fold's finding — one dated bullet)

- **HOLD at the converged state** (2026-11-16 ~02:40 UTC): M1 apex HELD / M2 in flight / M3 staged; the rig's governing discipline holds — read-cold once, fold sense, land rows, verify against DISK never the ledger, nothing public without the chair.

## 5. THE STATE OF THE RIG (one line)

The sweep lane's floor is live (rig dir listed, 2+1 seed lines read), the harness's md5 delta is an open-verify bookmarked to the first fold, and the chain holds the M2/M3 transition as the durable carrying line; the sweep is a sensor, not a writer, and the seed rows above are the day's complete scan set. Remote == local at `5d195d8b4e` as of the lock (verify again before the next landing).
