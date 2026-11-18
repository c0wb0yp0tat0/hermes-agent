# NIGHTSHIFT-LENS-2-20261118 — the provider-absence battery
seat: meituan/longcat-2.5:free · scribe-cell: rig-nightshift-lens2 · STAGE 2 (all-fleet think-tank planning), LENS-2 slice
sources: NIGHTSHIFT-BEARINGS-20261118.md [B]; MISSION-MAP-20261118.md [M]. Quote-not-assert: every claim tagged [B] mined / [M] operator's words / [R] my reasoning.

## 0. The test the operator named
The scenario's seed [B]: when the provider's reads never restore, the kit reads ITS OWN cells; candidate (c), the read-side scribe-cell fallback, is designed but unwired. This lens specifies the falsifier-first battery that PROVES the reads work with the provider surface removed. A battery that cannot fail is not a test — every leg carries a kill switch (the result that would falsify the claim).
Provider-absent mode (all legs): the harness suppresses the provider read surface; the only read paths are the scribe cells, the doc-chain, and the local files.

## 1. THE BATTERY — four legs
### LEG-1 CELLS-ONLY READS (paged, byte-verified)
- Probe: for each tracked artifact A: (i) `scribe cells register --list` → cell name for A; (ii) `scribe cells read --cell <A> --offset k --limit m`, k=0..end; (iii) concatenate pages, sha256 vs A's recorded digest; (iv) assert provider-call counter == 0.
- Expected: full bytes return across pages; digests match; multi-page artifacts page ≥2×; zero provider reads.
- Pass bar: x/y = verified/tracked, 20/20 green; any digest mismatch or provider call kills the leg.
- Kill switch: one artifact whose bytes exist only on the provider side.

### LEG-2 COLD-START READS (seam decks + doc-chain, provider-absent)
- Probe: fresh session, provider suppressed; read `014-handoff-20261118` + MISSION-MAP + the doc-chain segments from cells only; emit a continuation note naming the active steers and the loop state.
- Expected: seam wiring resolves with no provider; the note's steer IDs (STEER-1..8) and loop-state line match the record.
- Pass bar: cold-start assembly green; cited steers == record; zero provider reads.
- Kill switch: the continuation cannot name the current stage without provider context.

### LEG-3 TRUNCATION-FALLBACK PATH
- Probe: pick an artifact larger than the read window; issue a plain file read with no offset → capture the head+tail + hint; assert the kit detects truncation, falls back to the cell, returns full bytes, digest-matches.
- Expected: truncation detected from the hint/short byte count; fallback fires; full bytes; digest green.
- Pass bar: fallback on the FIRST truncation signal; full-byte return; digest match; latency ≤ 2 read windows.
- Kill switch: the kit accepts the truncated body as complete.

### LEG-4 WRITE PATH PROVIDER-ABSENT
- Probe: provider suppressed; produce a new brief; the write-time assert runs (bytes hashed → named cell → byte-verify); then a session throw; re-read the cell and compare.
- Expected: write lands provider-absent; the register gains the cell; bytes persist across the throw; digest match.
- Pass bar: assert fires on 100% of writes; persistence green; zero provider reads.
- Kill switch: the write blocks awaiting provider confirmation.

## 2. The battery's home (fire-sequence ride)
- Home: a named runner arm / lane leg in STAGE 3 (THE FIRE), fired with each read-solution build.
- Cadence: per loop cycle after a build delta, plus a standing nightly sweep [B crons].
- Artifacts: `BATTERY-LOG-<date>.md` (per-leg rows), the F1 pass-rate ledger, the cells' byte-integrity receipt.
- Two-way door: reversible — if the cells prove insufficient (LEG-1 fails), drop to the doc-chain/gist layer (the substrate-of-substrates [B]) and re-run; the battery retires only after F1 plateaus twice.

## 3. The F1 measure (terminal contract)
- Pass rate = green legs / 4 per run (x/4); per-leg sub-metrics (verified/tracked) recorded alongside.
- No-improvement rule [M AMENDMENT-2]: two consecutive runs with zero pass-rate gain → F1 plateaus; the loops then hold on F1.
- Integrity: the battery is evidence, not assertion — each row cites the raw command output digest.

## 4. LP envelope (one line per leg)
- LEG-1 Bias for action: on the first truncation signal, serve the cell immediately; do not wait for a provider restore.
- LEG-2 Invent and simplify: boot the arc from local seam decks — no provider in the cold-start path.
- LEG-3 Dive deep: chase the truncation signal to the head+tail hint before choosing the fallback.
- LEG-4 Deliver results: the write lands and persists with the provider unable to confirm.

## 5. Storm-context riders (corroboration of class, never adoption)
- SELD: the battery IS a read-side evidence plane — leg pass bars are evidence-gated.
- AskALCF: each leg admits only on evidence (digest/counter), with a commit gate on the log row.
- CoMem: byte-verified paged reads = fidelity-ladder L2 (full-fidelity bytes).
- Reward-Driven Collider: the per-cycle cadence is the adaptive envelope; pass-rate is the reward signal.
- MemCredit: the cells are the memory bank; rho=(V-λH)/b prices which bytes stay hot.
- DISCERN: LEG-4's write-time assert is the L0 write-gate, provider-absent.
- Four misc: compile-time gating (provider-suppression flag); stage-decoupled evaluation (legs independent of build); validity decay (stale cells re-verified); three-state delegation (legs dispositioned green/red/blocked).

## 6. Compose-check table (eight marks)
| # | mark | state | evidence |
|---|------|-------|----------|
| 1 | quote-not-assert | FIRED | claims tagged [B]/[M]/[R], short attributed quotes only |
| 2 | first/second-hand separation | FIRED | [B]/[M] mined vs [R] reasoned, labeled inline |
| 3 | trace-to-pack | FIRED | every mechanism cites BEARINGS or MISSION-MAP |
| 4 | no-echo | FIRED | original prose; no block copied from the pack |
| 5 | no-placeholder | FIRED | all four legs fully specified with probes/bars |
| 6 | record's-terms-only / wall clause | FIRED | no public writes named; RFC quiet |
| 7 | measure defined | FIRED | F1 pass-rate x/4 + no-improvement-twice |
| 8 | two-way door named | FIRED | substrate fallback + post-plateau retirement rule |

LOOP-STATE LINE: `LENS-2 LANDED - PROVIDER-ABSENCE BATTERY SPECIFIED - four legs, F1 measured, two-way door held.`
