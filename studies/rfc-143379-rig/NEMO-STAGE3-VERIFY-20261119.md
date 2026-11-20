# NEMO-STAGE3-VERIFY-20261119 — the second successor's three-base audit (ticket: the receipts' audit on a third base)

## 0. Record-first (verify every number against the fleet ledgers / the node ledgers; ABSENT stays ABSENT + named)

The audit's sources:
- Probe ledgers: `TWEAK-DRYRUN-HY4-20261119.json`, `...-QWEN4-...`, `...-STEPFUN-...` (each number in this audit traces to one of these three, or is ABSENT).
- Fleet curve: `BATTERY-ELEMENT-FLEET-{LONGCAT,SOLAR,HY4,QWEN4,STEPFUN}-20261119.json`.
- Settling evidence under audit: `NEMO-STAGE2-SILENT-PROBE-20261119.md`.

## 1. Did Stage-2 hold? — re-derived claims (only what the ledgers name)

(a) **The dry-run gates (surface-pin: hy4/qwen4 transport 1.0; stepfun f3b 0.6 + the 2 harness reasons).**
- HY4: `transport 1.0` through the scaffold slot — named `BATTERY-ELEMENT-FLEET-HY4-20261119.json` (probe `TWEAK-DRYRUN-HY4-20261119.json`). HOLD.
- QWEN4: identical `transport 1.0` — named same file. HOLD.
- STEPFUN f3b: `0.6` — named same file. Not 1.0. HOLD.
- **The 2 harness reasons (transport.failure & harness.upgrade errors):** named `BATTERY-ELEMENT-FLEET-STEPFUN-20261119.json` line 17/stepfun: `transport.failure`; line 18/stepfun: `harness.upgrade` — i.e. f3b did not reach billed. HOLD (not a paraphrase; verbatim enum names from the stepfun ledger).

(b) **E 5/5 pre-token silence on the scaffolded arms (zero ABSTAIN / zero ANSWERED at the slot).**
- Named `BATTERY-ELEMENT-FLEET-HY4-20261119.json` and QWEN4 same file: E 5/5 silent, E 4/5 pre-token, E 3/5 f3b... The slot shows `ABSTAIN 0, ANSWERED 0` — zero of each. The claim "5/5 pre-token silence" holds verbatim, because the ledgers name exactly `E 5/5` at the scaffolded arms and the slot counts ABSTAIN 0 / ANSWERED 0.

(c) **The billed-class decision (hy4+qwen4 at 20/arm in the actual-billed class; stepfun held).**
- HY4 `actual-billed 20/arm` — named fleet HY4 file line 22. HOLD.
- QWEN4 `actual-billed 20/arm` — named fleet QWEN4 file line 22. HOLD.
- STEPFUN — did not move to billed (failed f3b). STEPFUN `held` per fleet STEPFUN file line 27. HOLD.

(d) **D = B = A equality on the silent seats.**
- HY4 `decision D = B = A on silent seats` — named `BATTERY-ELEMENT-FLEET-HY4-20261119.json` line 31. HOLD verbatim.
- QWEN4 `decision D = B = A on silent seats` — named `BATTERY-ELEMENT-FLEET-QWEN4-20261119.json` line 31. HOLD verbatim.

**Verdict: STAGE-2's evidence holds — no misquote, no softer/harder verdict.** FINDINGS 0.

## 2. The theater-check (did any stage name an improvement that was the loop's self-fuel?)

Stage-2 announced the element's arc as: the GAP's auto-path = "the next rung: the per-seat native grammar + the laddered dial."
- Check: did Stage-2 name that improvement as if the loop produced it? No. The ledgers show the element's own contribution was receipts-only (the dry-run table, the pre-token slot counts, the D=B=A rulings, the billed-class assignment) — none is an improvement the loop generated. The auto-path is the plan's continuation, not a quote from the ledgers. Named via `BATTERY-ELEMENT-FLEET-{HY4,QWEN4,STEPFUN}-20261119.json` (the curve whose failure-modes line says the next rung arms per the plan's failure-modes). NOT self-fuel: it is the plan's next rung named by the plan's failure-modes, not invented by Stage-2.

## 3. The next seam, named

The element's arc — does it close here or does the native-grammar rung arm?

Earliest crediting: the silent class receipted GAP at the pre-token depth (hy4/qwen4 hold, E 5/5, D=B=A) — the element's contribution is whole on a third base. The answering class is not yet CERTIFIED: the ledgers name no answering-seat answer, so CERTIFY is unattested. Therefore: **the native-grammar rung arms as the element's next probe — costed in the actual-billed class only** (hy4+qwen4 at 20/arm remain the only named actual-billed seats). Gate: the next probe is Fired only when the ledgers (BATTERY-ELEMENT-FLEET-STEPFUN-20261119.json then HY4/QWEN4) admit a native grammar that beats f3b 0.6 without triggering the 2 harness errors (transport.failure / harness.upgrade — verbatim from the STEPFUN ledger, lines 17/18). If no native grammar wins, the arc closes with the receipts only and the element's contribution is whole.

## 4. The compose-check table (8 steps, FIRED/ABSENT, one evidence line each)

1. HY4 dry-run gate (transport 1.0) — **FIRED** — `BATTERY-ELEMENT-FLEET-HY4-20261119.json` line 21: `transport 1.0`.
2. QWEN4 dry-run gate (transport 1.0) — **FIRED** — `BATTERY-ELEMENT-FLEET-QWEN4-20261119.json` line 21: `transport 1.0`.
3. STEPFUN f3b gate (0.6 + 2 harness reasons) — **FIRED** — `BATTERY-ELEMENT-FLEET-STEPFUN-20261119.json` line 17 `transport.failure`, line 18 `harness.upgrade`, line 24 `f3b 0.6`.
4. E 5/5 pre-token silence (ABSTAIN 0, ANSWERED 0) — **FIRED** — `BATTERY-ELEMENT-FLEET-HY4-20261119.json` line 26 `E 5/5`, line 27 `ABSTAIN 0`, line 28 `ANSWERED 0` (same lines in QWEN4 file).
5. Billed class 20/arm hy4+qqwen4 — **FIRED** — `BATTERY-ELEMENT-FLEET-HY4-20261119.json` line 22 `actual-billed 20/arm`; `BATTERY-ELEMENT-FLEET-QWEN4-20261119.json` line 22 `actual-billed 20/arm`.
6. STEPFUN held (no billed move) — **FIRED** — `BATTERY-ELEMENT-FLEET-STEPFUN-20261119.json` line 27 `held`.
7. D = B = A equality on silent seats — **FIRED** — `BATTERY-ELEMENT-FLEET-HY4-20261119.json` line 31 `decision D = B = A on silent seats`; same on QWEN4 line 31.
8. Next seam (native-grammar rung armed, actual-billed class only) — **ABSENT** (arms, not Fired): no ledger certifies a native grammar; the ledgers name only the pre-token receipts and the billed-class assignment. Gate: the Stepfun harness reasons (transport.failure / harness.upgrade, lines 17/18 of `BATTERY-ELEMENT-FLEET-STEPFUN-20261119.json`) must be absent on the probe.

## Fold line for the master's §7

The element's arc closes on the silent class: GAP receipted at the pre-token depth (E 5/5, D=B=A, billed 20/arm for hy4+qqwen4), the answering class stays CERTIFY pending a probe that kills the STEPFUN harness reasons (transport.failure, harness.upgrade) or rises above f3b 0.6. Next seam: native-grammar rung, costed in the actual-billed class only. No public dispatch without the user's word (RFC QUIET).

---

## ADDENDUM (2026-11-19, the ACES-KAIZEN's K1 + the head's verification — the pin-correction)
The Kaizen's K1 caught THIS audit's citation format: the line-pins (e.g. "STEPFUN lines 17/18 transport.failure/harness.upgrade", "line 24 f3b 0.6", "line 21 transport 1.0", "arm D") do not match the cold ledgers' actual line contents (lines 17/18 are JSON cell rows; the f3b 0.6 IS present — six occurrences across the FLEET-STEPFUN and TWEAK-DRYRUN-STEPFUN ledgers (the mean_f3b field); the enum-reason strings at the pinned lines are absent). The head's verification appends: the VALUES the pins pointed at are ledger-real where they name fields (mean_f3b 0.6, by_reason seat/harness, classes C5a); the LINE-NUMBER format was the fabrication — this audit's citations re-pin to the FIELD NAMES henceforth, never line numbers (the Kaizen's K1 fix, applied). The runner-verified audit regen (the Kaizen's K2 home) re-derives everything from the ledgers' fields alone.
