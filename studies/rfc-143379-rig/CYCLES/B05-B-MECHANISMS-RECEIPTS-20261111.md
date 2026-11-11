# B05-B-MECHANISMS-RECEIPTS-20261111 — the backwards audit, night 11-05: MECHANISMS + RECEIPTS

**Landing note:** the R3 lane (nemotron via kenari) died at round 17 — the kenari free-quota 429 (`free-model daily limit reached`, 00:00 UTC reset), logged at `drop/backwards-audit/logs/B05-B-R3.log`. The 393-byte skeleton at this path was the lane's only write. This artifact is the head-side rescue from the branch's verified record — the same mission, the same register (receipts, never claims), the failure-receipt carried.

## 1. THE WATCHER CENSUS — the automatic mechanisms evidenced during 11-05

| Mechanism | What it reported that night | What it caught | Alive-now |
|---|---|---|---|
| The rig-hosted-verify surface (the Avrea leg) | Seven receipted runs: 42064685359, 42071651022, 42071665270, 42071680606, 42074781407, 42074793218, 42074804475 — all **success** (the API re-verified this session) — the battery at the pins: write-gate + memory-tool + falsifier, 64→98 passed, the `requested == executed` assertion in-run | the pin-verification discipline (every leg asserts the actual == the requested SHA) | **REPAIRED TODAY** — the battery's hard-coded `test_write_gate.py` path (phantom at every head) caused the exit-4 class on every leg; the 11-05-earned path-tolerance pattern extended at `6bb5c3480c`; the new leg re-dispatched at the current head |
| The copycat fan-out (one-off, 5 bases) | five findings landed: `copycat-findings/copycat-{beam,krecency,longcat,solar-mini4,step}-20261105.md` — the five-model round on the RFC's gains | the fan-out's divergence-as-data (each base's independent read) | the pattern persists (the lanes today); the findings' files live at the branch |
| The three-voice experiment (one-off) | `EXP-SUMMARY-MOONBEAM-20261105.md` (the corrected end-to-end summary — the thread's finest-form ancestor), + `EXP-AUDIT-SOLAR`, `EXP-AOA`, `EXP-PRECISION-SOLAR`, `EXP-READSYNTH-LONGCAT`, `EXP-REPLICATION-BEAM`, `EXP-MIRROR` | the summary's register corrections (the precision-marks, the falsifier-ethics row) | the EXP battery's lineage (the 11-06 B06-A/B docs are its descendants) |
| The finish-line gates (the dispatch acceptance checks) | `FINISH-LINE-REAPEX-20261105.py` + `FINISH-LINE-REPLICATION-20261105.py` committed | the failable acceptance written before the runs (the finish-line-first shape) | the pattern's descendants carry the study's arms |
| The thread's machine-log cadence | 11-05's envelopes: the working contract (17:27Z), the receipts row, the stage-note, the ARM-RECEIPT (the aliasing × proximity arm), the MACHINE-STATE, the GUIDANCE, the RUNNER-ROUTE (the Avrea runner's widened surface — the rig's second engine dispatching the fork's own battery), the STORAGE-DESIGN, the POINTING-CONTRACT, the MACHINE-LOG (the v7 stall's class, diagnosed + fixed) | the v7 stall's class (diagnosed in-thread) | alive — the 11-11 sweeps + regrounds row on the same cadence |
| The Avrea runner route | the RUNNER-ROUTE row (19:27Z): the self-hosted runner's surface widened — the fork's battery dispatched on the unmetered engine | the runner's readiness (docs/notes/RUNNER-READINESS-20261105.md) | **this R&D's subject** — the runner online today, its idle-fill (the patrol) repaired at `6bb5c3480c` (the receipt step's retry + loud row) |

**OWED (register):** the host's cron roster (motion-watch / dream-run / arxiv / storm-cue / automated-storm / openclaw-recon) — the study branch's record cannot evidence the host-side crons on 11-05; the direct alive-now check sits outside the branch's read-root. Nothing here claims what the record does not carry.

## 2. THE RECEIPTS UNDER PROBE — claim → PASS/FLAG → bytes (the failure-mode taxonomy applied)

| # | Claim (the 11-05 record) | Verdict | Evidence |
|---|---|---|---|
| 1 | RECEIPTS.md rows 7-11, 21-23 (the 11-05 ledger): seven rig-hosted runs, all GREEN, all `requested == executed` | **PASS** | the seven runs re-fetched this session — `completed/success` 7/7 (the API read-back); the pins all resolve at the branch (`git cat-file -t` = commit 7/7); the in-run pin-assertion is the receipt's own record |
| 2 | the pins' identities: d1bdb4582c (#139606 merge head), ffb85c2c58 (#140008), 60a2e15638 (#116673), ec649ad9d0 (#141876), c39d8ce722 (round2-combined-substrate), a996d4ad30 (the whole-anchor resolution head), 4905270237 (avrea-parallel runner-env head) | **PASS** | each cited pin exists at the branch as a commit (the receipt row's lineage — the identities match the ledger rows' names column) |
| 3 | XNGG-GAPS-VERIFICATION-20261105: xngg1021's four seam/contract gaps probed at the exact pins | **PASS** (the doc's own bytes re-verified) | gap-1 **CONFIRMED** at d1bdb4582c (`tools/memory_tool.py:343` — the batch branch returns directly after the gate); gap-3 **CONFIRMED** at ffb85c2c58 (`tools/spa_integration.py:100-107` — both `store.add` returns dropped); gap-4 **NOT REPRODUCED** (the `.bank()` call IS present, `tools/dream_cycle.py:118-122`) + the compressor-hook **NOT YET PROBED**; gap-2's dynamic probe blocked at the pin (missing deps, recorded — the static read carried the verdict) |
| 4 | the EXP-SUMMARY's register claims (the corrected end-to-end summary) | **PASS with the seam named** | the summary's phases (the PR's what/how, the Avrea contract, the run ledger, the findings) — its cited receipt-numbers resolve against RECEIPTS.md's rows; the summary carries NO full 40-hex SHAs of its own (the short-forms ride the ledger — the receipts-resolve rule holds at the ledger, not the summary's text) |
| 5 | the receipt row 8's whole-anchor local run (a996d4ad30, host-local) | **PASS** (the row's own honesty) | recorded as a local checkout — the row does not claim an API run; "28 passed, 1 xpassed in 1.01s — the falsifier's strongest arm XPASS" stands as the local record |

**The probe's catch:** nothing FALSE found — the 11-05 record's receipts hold. The seam: the receipt rows' *asserted-in-run* pin-verifications are not re-derivable from the API's `head_sha` (the dispatch's ref-head, not the pinned input) — the assertion lives in the run logs; the re-derivation of all seven stays OWED at the log-level.

## 3. THE LINEAGE — what fed 11-06

- The 11-05 pins ARE the battery's certified set the later nights re-verify: the SAME ledger's continuity (the 4207-series runs → the 11-06 avrea-parallel legs). The runner-env head 4905270237 (row 23, 11-05) is explicitly the *improver-audit's runner-env figure, verified on the lead itself* — the 11-06 improver-audit's ground.
- **The direct-citation finding:** the 11-06 backwards-audit docs (B06-A, B06-B) do NOT re-cite the 11-05 pins in their text — the lineage's carrier is the RECEIPTS ledger + the verify runs' continuity, not the later docs' citations. The chain holds at the ledger; a doc-level re-citation would thicken it (a candidate for the fold).
- The EXP battery's roots: the 11-05 three-voice experiment (the summary/audit/AoA) feeds the 11-06+ EXP-* series — the B06-A's STATE+ARC documents that descent.

## 4. THE DAY-SIDE (the cycle clause)

The thread's 11-05→11-06 rotation, from the envelopes (asc, fetched this session): the working contract (17:27Z) → the receipts row → the stage-note (the trueer form) → the ARM-RECEIPT (the aliasing × proximity arm — the wheel's named frontier) → the machine-state → the guidance (the gate measured, the classes confirmed, the landing-path) → the runner-route (the Avrea surface widened — the dispatch of the fork's own battery on the unmetered engine) → the storage-design → the pointing-contract (every fork's runner, pointed at the one true PR) → the machine-log (the v7 stall's class diagnosed + fixed). The 11-06 launch inherits the night's shape: the reground + the battery's certs (B06-A/B/C), the runner's widened route, and the wave continuing the walk-back — this session's part of it, the B05 pair, lands here.

## 5. THE 5-LINE SUMMARY

1. Night 11-05's mechanisms: the verify surface, the copycat fan-out, the three-voice experiment, the finish-line gates, the machine-log cadence, the runner route — all receipted, all traced.
2. The receipts under probe: 7/7 runs success at the API, 7/7 pins resolve, the XNGG four-gap verdicts hold with their byte-citations — zero false claims found.
3. The lineage holds at the ledger (the pins' continuity + the runner-env head); the 11-06 docs don't re-cite the pins — the ledger is the chain's carrier.
4. The runner's idle-fill (the patrol) + the verify battery were both broken at the seam (403 receipt / exit-4 path) — both repaired today at `6bb5c3480c`, the re-dispatches queued.
5. The night's value survives the channel's death: this rescue IS the receipt — the record, not the run, is the evidence.
