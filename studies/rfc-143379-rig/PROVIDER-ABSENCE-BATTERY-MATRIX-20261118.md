# PROVIDER-ABSENCE-BATTERY-MATRIX-20261118 — the B3 matrix, filed from the copycat lane
seat: hy4 (matrix) of STAGE-3 / B3 · execution seats = stepfun (legs) + hy4 (matrix), per NIGHTSHIFT-PLAN §THE FIRE B3 · scribe-cell: this MATRIX lane · RFC #143379 · runtime lane class: **git-only terminal**.

sources read once each: `NIGHTSHIFT-LENS-2-20261118.md` [L2] · `NIGHTSHIFT-PLAN-20261118.md` [P].
STORM-CONTEXT (corroboration of class, never adoption): SELD — the matrix is a read-side evidence plane, every row evidence-gated; AskALCF — legs admit only on digest/counter evidence with a commit gate on the log row; CoMem — byte-verified paged reads are fidelity-ladder L2; DISCERN — LEG-4's write assert is the L0 write-gate; MemCredit — cells are the priced memory bank; Reward-Driven Collider — pass-rate is the cycle reward; four misc — compile-time gating / stage-decoupled evaluation / validity decay / three-state delegation (green/red/blocked).

## 0. EXECUTION BOUNDARY — the honesty gate (read this before the verdict)
This lane's terminal is git-only. Verbatim tool receipt: `terminal is git-only for lanes`. The battery's probe primitives are therefore **unexecutable from here**:
- no `scribe cells register --list` / `scribe cells read ...` (no CLI reachable),
- no provider-call counter and no provider-suppression flag harness,
- no `sha256sum` / digest computation,
- no session-throw / re-read persistence harness.

What IS reachable: `read_file` (paged, with an explicit head+tail+hint truncation signal), `write_file` (byte write lands), and `git` (commit/push only). Consequence, per the brief ("the honest partial beats the claimed green"): **no leg is fully executable in this lane.** Each leg below is adjudicated NOT-RUN as a battery leg, with (a) the exact reason, (b) the partial observation that genuinely IS available, (c) the kill-switch disposition, and (d) the seat that CAN run it. No digest, counter zero, or latency figure is fabricated; receipts that cannot be produced here are named as ABSENT-FROM-LANE and required from the executor seat.

## 1. THE MATRIX — four legs

| Leg | Probe (from [L2] §1) | Pass bar | Result | Kill-switch check | Executor seat |
|---|---|---|---|---|---|
| **LEG-1 cells-only paged reads** | list cell per tracked artifact → page k=0..end → concat → sha256 vs recorded digest → provider counter 0 | 20/20 verified; any digest mismatch or provider call kills | **NOT-RUN** | NOT-TESTED — cannot enumerate cells | stepfun legs seat (B3) with scribe CLI + counter harness |
| **LEG-2 cold-start reads** | fresh session, provider suppressed, read 014 handoff + map + chain from cells → note naming STEER-1..8 + loop state | cell-sourced assembly green; cited steers == record; counter 0 | **NOT-RUN** (cell path) | NOT FIRED in local-read sense (stage named from local record) — see §2 | stepfun legs seat with fresh-session harness + counter |
| **LEG-3 truncation-fallback** | plain read of large artifact → head+tail+hint → detect → fall back to cell → full bytes → digest → latency ≤2 windows | fallback on FIRST signal; full bytes; digest green | **NOT-RUN** (fallback/digest) | NOT FIRED — truncation explicitly signaled, not silently accepted — see §2 | stepfun legs seat (cell fallback + digest + latency clock) |
| **LEG-4 write path provider-absent** | provider suppressed → new brief → assert (hash→cell→verify) → session throw → re-read → digest → counter 0 | assert on 100% writes; persistence green; counter 0 | **NOT-RUN** (assert/throw portion) | NOT FIRED in the write-lands sense (no provider needed) — see §2 | stepfun legs seat (scribe CLI + throw harness + counter) |

### LEG-1 — cells-only paged reads: NOT-RUN
- Exact reason: `scribe`, `sha256sum`, and the provider-call counter all require a shell; the lane terminal is git-only (`terminal is git-only for lanes`). No cell path is reachable via `read_file`.
- Partial observation: none — cells cannot be enumerated or read from this lane.
- Kill switch ("one artifact whose bytes exist only on the provider side"): **NOT-TESTED**. Honest mark: untested, not passed.
- To run: stepfun legs seat executes the 20-artifact page-and-digest sweep; hy4 (this seat) records the verified/tracked ledger row.

### LEG-2 — cold-start reads: NOT-RUN (cell-sourced leg)
- Exact reason: a fresh session with provider suppressed and cell-sourced reads of 014-handoff + MISSION-MAP + doc-chain cannot be assembled here; no cell CLI, no session harness, no counter.
- Partial observation (REAL RECEIPT [R3]): the current stage **is** nameable from local artifacts alone — [P]'s loop-state line reads `STAGE-3-IN-FLIGHT - B1 WIRED + PROBED - B2-B4 ARMED`; [P]'s seam ladder names STEER-8 as the latest steer in the STEER-1..8 channel.
- Kill switch ("cannot name the stage without provider context"): **NOT FIRED** in the local-read sense — the stage was named from a local record with no provider. This is a partial kill-switch check only; the cell-path + counter portion is NOT-RUN and does not convert to a green leg.
- To run: stepfun legs seat runs the actual fresh-session cold start with the counter.

### LEG-3 — truncation-fallback path: NOT-RUN (fallback/digest portion)
- Exact reason: although the truncation *signal* is observable, the fallback-to-cell, full-byte return, digest match, and latency clock cannot execute (no cell CLI / digest / clock).
- Partial observation (REAL RECEIPT [R2]): `read_file` on [P] returned content containing `…[middle elided at read-time]…` with `page.hint = "use offset/limit to page further (e.g. offset=301)"` and `page = {offset:1, limit:300, total_lines:83}`. The substrate explicitly signals truncation and refuses to present the elided body as complete.
- Kill switch ("the kit accepts the truncated body as complete"): **NOT FIRED** — truncation surfaced with a named hint; this is a genuine disconfirming observation on this read substrate. Fallback-to-cell remains NOT-RUN.
- To run: stepfun legs seat drives the plain-read → signal → cell fallback → digest → latency chain.

### LEG-4 — write path provider-absent: NOT-RUN (assert/throw portion)
- Exact reason: the write-time assert (hash→named cell→byte-verify), the session throw, the re-read persistence check, and the counter cannot execute here (no shell / cell CLI).
- Partial observation (REAL RECEIPT [R5]): this matrix file is being written via `write_file` with no provider surface at all; [P]'s substrate ceiling for the matrix cell — "FIRED if artifact exists at path" — is satisfied for the *write-lands* class. The full battery leg is stricter and is not discharged.
- Kill switch ("the write blocks awaiting provider confirmation"): **NOT FIRED** in the write-lands sense — the byte write landed without any provider. Assert/persistence remains NOT-RUN.
- To run: stepfun legs seat runs the assert + throw + re-read + counter sequence.

## 2. F1 PASS-RATE LEDGER (terminal contract, [L2] §3)
- **Fully-green legs / 4 = 0/4** for this lane's baseline run. This is a lane-honest zero of *completed* legs, **not** a claim that the battery fails — no leg could be driven with shell primitives here.
- Per-leg verified/tracked: LEG-1 0/20 (unmeasured, no cells) · LEG-2 unmeasured (cell path) · LEG-3 unmeasured (fallback/digest) · LEG-4 unmeasured (assert/persistence).
- Kill-switch dispositions observed: **3 NOT FIRED (partial observations), 1 NOT-TESTED**. A non-firing kill switch from a partial observation does **not** equal a pass; it is recorded as such and no more.
- No-improvement rule ([M AMENDMENT-2] via [L2]/[P]): baseline run #1; a plateau requires two consecutive runs with zero pass-rate gain — not reached.
- The first *real* F1 pass rate is owed by the stepfun legs seat with a shell; this matrix is the ledger frame that seat fills.

## 3. RECEIPTS — raw, named, never a silent skip
OBSERVED from this lane (cite-able now):
- **R1** — capability boundary: tool returned `terminal is git-only for lanes`.
- **R2** — LEG-3 truncation signal: `read_file` on [P] returned `…[middle elided at read-time]…` + `hint: use offset/limit to page further (e.g. offset=301)`; `page {offset:1, limit:300, total_lines:83}`.
- **R3** — LEG-2 stage-nameable: [P] loop-state `STAGE-3-IN-FLIGHT - B1 WIRED + PROBED - B2-B4 ARMED`; seam ladder names STEER-8 latest of STEER-1..8.
- **R4** — F1 contract: [L2] `Pass rate = green legs / 4` and `two consecutive runs with zero pass-rate gain → F1 plateaus`.
- **R5** — write-lands: this MATRIX artifact is filed at the artifact path via `write_file`, no provider surface (satisfies [P]'s matrix-cell existence ceiling).

ABSENT-FROM-LANE (named gaps — the executor seat MUST supply; do not fabricate):
- sha256 per-artifact cell↔file digests (20 rows, equality-of-bytes per [P] OPEN ITEM — sha256 chosen here as the equality witness),
- provider-call counter zeros (one per leg),
- named errors `TRUNCATE` / `ABSENT` / `NO-CELL` / `CELL-UNREADABLE` / `CELL-BYTE-MISMATCH` / `CHAIN-UNVERIFIED` / `DECK-BUILD-FAIL` / `HANDOFF-GAP` (evidence of escalation, not silence),
- LEG-3 latency readings (≤2 read windows), LEG-4 throw/re-read digest pairs.
Each ABSENT above is a tracked gap, not a skipped leg re-labeled green.

## 4. TWO-WAY DOOR / ESCALATION (held, not flipped)
- `READ_SUBSTRATE_MODE` stays `canonical` in this lane ([P]: default until the wire lands, rollback state); no live config was touched, no mode flip performed.
- Failure path per [P]: never serve a partial — TRUNCATE/ABSENT → cell → chain → decks → full-opus runners; cells fail → drop to doc-chain/gist layer and re-run.
- Retirement: battery retires only after F1 plateaus twice ([L2] §2, [P]). Held.

## 5. LOOP-STATE LINE
`B3-LANDED (MATRIX seat) - PROVIDER-ABSENCE-BATTERY MATRIX FILED - four legs adjudicated, 0/4 fully green from git-only lane, all NOT-RUN with exact reasons + named executor seats, 3 kill-switch partials + 1 untested - first real F1 pass rate pending the stepfun legs seat with a shell.`

## 6. COMPOSE-CHECK TABLE (eight marks)
| # | mark | state | evidence |
|---|------|-------|----------|
| 1 | quote-not-assert | FIRED | Claims tagged [L2]/[P]; receipts tagged OBSERVED vs ABSENT-FROM-LANE. |
| 2 | first/second-hand separation | FIRED | [L2]/[P] mined from source; lane observations are first-hand tool receipts; adjudication reasoned. |
| 3 | trace-to-pack | FIRED | Every leg/probe/pass-bar/kill-switch cites [L2] §1 or [P] §THE BATTERY. |
| 4 | no-echo | FIRED | Original matrix prose; no block copied from the pack. |
| 5 | no-placeholder | FIRED — with named gaps | No leg silently skipped; every NOT-RUN has reason + executor seat; receipts absent are named, not faked. |
| 6 | record's-terms-only / wall clause | FIRED | No public writes; RFC quiet; no live config flip. |
| 7 | measure defined | FIRED | F1 x/4 baseline = 0/4 lane-honest; per-leg rows; no-improvement-twice not reached. |
| 8 | two-way door named | FIRED | canonical held; doc-chain fallback + post-plateau retirement stated. |
