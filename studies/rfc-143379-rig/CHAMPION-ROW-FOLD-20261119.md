# CHAMPION-ROW-FOLD-20261119 — the Luna leg folded into the champion row + the probe's costed rows

Seat: copycat (fold lane) · branch `study/rfc-143379-rig-20261105` · RFC #143379. Gate: "nothing public without the user's word." RFC QUIET. Artifacts only; committed before exit. Wall clause: "a non-reproduction is a QUESTION, not a stop." Append-only. Ground read once (head's receipts trusted): `probes/BATTERY-LUNA-LEDGER-20261119.json`, `-R2.json`, `CONFIRMATION-CYCLE-LUNA-20261119.md`, `RETRIEVER-RESHAPE-20261119.md` verdict tail, `probes/BATTERY-FULL-LEDGER-20261119.json`, git `bec0a684bf`/`7d07f2d35c`.

## §1 ADJUDICATION
1. **INCONCLUSIVE twice.** R1 `7a59483cec`: A 0/40 (E 40, `empty_reason seat`, C5a 40), B 19/40 = 0.475, C 29/40 = 0.725. R2 `103225e6e7`: A identical 0.0, B 23/40 = 0.575, C 29/40 = 0.725. B−A = 47.5 / 57.5 pts (≥ 20 both); 0.85×C = 0.61625; B = 0.475 / 0.575 both below → neither CERTIFY nor FALSIFY [1][2].
2. Confirmation landed `CONFIRMED-NO-IMPROVEMENTS`; four candidates rejected with rows (B answered 26→31 in-band; C wrong 1→4 regression; bridge 0.9→0.925 envelope; all-harness f3b) [3].
3. Reshape **falsified: no gain**, n=20 same seeds 0–19 paired: B′ 8/20 vs banked R1 10/20, R2 9/20; answered 10/20 vs 15/20, 12/20; mean F3b 0.85 (3 harness misses, flakiness ~15%) fired the INCONCLUSIVE trigger. Named: **barrier = the seat's record-USE, not presentation**; store-class reshape stays closed [4].
4. Flakiness: 503-window ~85% loss vs 4–9% baseline; S8 split kept the middleware measurement clean (HEAD-RECON) [3].
5. Cost: $0.467/exec → $18.68/paid arm; shadow R1 $37.36, R2 $37.36, pilots $18.68+$18.68 = $112.08; account actual $61.99 (operator billing telemetry) — labeled, never merged [1][2][3][5].

## §2 THE CHAMPION-ROW UPDATE (append verbatim to `SPRINT-FIRE-SEQUENCE-20261119.md` §33)
### §33 UPDATE — 2026-11-19 (fold lane; append-only)
**Luna leg's row:** **INCONCLUSIVE twice** (R1 `7a59483cec`, R2 `103225e6e7`): A 0.0 (40/40 empty, `seat`) both; B 0.475 / 0.575; C 0.725 both; B−A 47.5 / 57.5 ≥ 20 both; B < 0.85×C = 0.61625 both. Per the row's rule ("CERTIFY → arm B is champion; else arm A stands and the falsify receipt is the row"), **arm A stands; the INCONCLUSIVE pair is the honest row** — no threshold flipped. Second eyes: `CONFIRMED-NO-IMPROVEMENTS` [3].
**Dead-end registry, appended candidate:** RETRIEVER RESHAPE (attribution failure → reshape, never store) **falsified at n=20, same seeds 0–19, paired**: B′ 8/20 vs R1 10/20, R2 9/20; answered 10/20 vs 15/20, 12/20; mean F3b 0.85. Seed receipt: `BATTERY-LUNA-PILOT-RESHAPE-20261119-R2.json`; tail on `RETRIEVER-RESHAPE-20261119.md` [4]. Barrier named: seat's **record-USE**, not presentation.
**Registry read — what remains unexplored, named (no new plan, no invention):** (i) the seat's record-USE channel — a QUESTION, not a plan; (ii) 503-window ~85% loss vs 4–9% baseline — measurement-class residual; (iii) F6 cert-door packet — chair-gated, ABSENT; (iv) store-class reshape — closed by pre-registration. **Pre-registered dead-ends stay closed:** attribution failure → reshape (now falsified), never store; regime reversal → trim governor steps; blind 429 retry → forbidden; door-first route B → not recommended; local-LM oracle → void [3][4].
**Next sprint-mission (as landings decide):** the bench door's missing reception — the **read-path regression tests packet** — is the plan's smallest fireable two-way door; named as the champion's next, with the F6 door's submission standing alongside (packet absent, chair-gated).

## §3 THE LUNA LEG'S COSTED ROW INSIDE THE PROBE (append verbatim JSON to `probes/BATTERY-FULL-LEDGER-20261119.json`)
```json
"luna_leg_20261119": {
  "class": "LUNA-LEG cost rows (fold-in; leg ledgers stay primary)",
  "planning_estimate_usd_per_exec": 0.467,
  "shadow_rows": [
    {"run": "R1", "file": "BATTERY-LUNA-LEDGER-20261119.json", "ts": "2026-11-19T14:04:30Z", "n_per_arm": 40, "paid_arms": ["A","B"], "usd": 37.36},
    {"run": "R2", "file": "BATTERY-LUNA-LEDGER-20261119-R2.json", "ts": "2026-11-19T14:09:50Z", "n_per_arm": 40, "paid_arms": ["A","B"], "usd": 37.36},
    {"run": "PILOT-RESHAPE", "file": "BATTERY-LUNA-PILOT-RESHAPE-20261119.json", "n_per_arm": 20, "paid_arms": ["A","Bp"], "usd": 18.68},
    {"run": "PILOT-RESHAPE-R2", "file": "BATTERY-LUNA-PILOT-RESHAPE-20261119-R2.json", "n_per_arm": 20, "paid_arms": ["A","Bp"], "usd": 18.68}
  ],
  "shadow_total_usd": 112.08,
  "account_actual": {"source": "operator billing telemetry at measurement", "usd": 61.99, "label": "ACTUAL — the planning estimate billed below itself; classes labeled, never merged"},
  "receipts": ["[1]","[2]","[4]","[5]"]
}
```

## §4 THE LOOP-STATE LINE
`HOLD-AT-APEX → HOLD-AT-APEX` — the champion holds arm A with the INCONCLUSIVE receipt pair; the reshape falsification joins the dead-end registry; the bench door's read-path regression tests packet is the champion's next fireable two-way door (F6 submission alongside). Receipts [1][2][3][4][5].

## §5 COMPOSE-CHECK TABLE (8 steps)
| # | Step | Evidence / receipt |
|---|---|---|
| 1 | Read the champion row's §33 rule | BORROWED: brief §THE GROUND quote of §33 (`SPRINT-FIRE-SEQUENCE-20261119.md` §33) |
| 2 | Read the leg's R1/R2 ledgers (arms, cells, costs) | IN-LANE: `BATTERY-LUNA-LEDGER-20261119.json`, `-R2.json` arm blocks |
| 3 | Re-applied the pre-committed rule (B−A ≥ 20 ∧ B < 0.85×C) | IN-LANE: §1a numbers [1][2] |
| 4 | Read the confirmation cycle + hold-contract | BORROWED/IN-LANE: `CONFIRMATION-CYCLE-LUNA-20261119.md` §1–§3 |
| 5 | Read the reshape verdict tail + seed-level pilot receipt | IN-LANE: `RETRIEVER-RESHAPE-20261119.md` verdict; `BATTERY-LUNA-PILOT-RESHAPE-20261119-R2.json` |
| 6 | Fold the costed row (shadow + telemetry, labeled) | IN-LANE: ledger `cost` fields; git `7d07f2d35c` (billing telemetry $61.99) |
| 7 | Registry read + next-mission naming (read-path tests packet; F6 alongside) | BORROWED: brief §THE GROUND + git `bec0a684bf` dispatch |
| 8 | Append-only + wall-clause check (non-reproduction = QUESTION) | IN-LANE: blocks quoted verbatim; no existing bytes rewritten |

Storm-context corroboration (class, not adoption): the fold is a read-side evidence-plane operation (SELD's read-side verifier class; DISCERN's SPA-DREAM read path) with evidence-gated admission (AskALCF) and L2-fidelity note selection (CoMem). Design stays ours.

**Loop-state:** `HOLD-AT-APEX → HOLD-AT-APEX (the champion row holds arm A; the read-path tests packet arms from the champion; the head wires the fold-in).`
