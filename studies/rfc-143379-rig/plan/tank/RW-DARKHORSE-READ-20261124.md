# RW-DARKHORSE-READ-20261124 — darkhorse read, RETRIEVED from the committed record

Lane: copycat (retriever). Branch: `study/rfc-143379-rig-20261105`.
Mission: assemble the star addition from bytes ALREADY MEASURED and committed (Luna's substrate work). NO new probes, NO floor fires. Every number carries a retrieval receipt (file + path/line). A number without a receipt is named missing, never invented.

> Draft written to release the rig's write-window read-gate; enriched from the committed record below, then re-read and committed. No number below lacks a receipt.

## 1. Retrieval table (number -> source byte)

| Star number | Verbatim value | Source file | Receipt (json path / line) |
|---|---|---|---|
| n per arm | `6` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.n_per_arm` |
| cost per exec | `0.467` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.cost_per_exec` |
| B1 accuracy | `0.333` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.arms.B1.accuracy` |
| B1 correct | `2` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.arms.B1.correct` |
| B1 abstain | `4` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.arms.B1.eahq.ABSTAIN` |
| B1 sensitivity abstention | `0.667` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.arms.B1.sensitivity_abstention` |
| C accuracy | `0.5` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.arms.C.accuracy` |
| C correct | `3` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.arms.C.correct` |
| B >= 0.85C | `false` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.decision_rule.B_over_0.85C`, line 735 |
| pre-committed rule | see §2 | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.decision_rule.pre_committed`, line 737 |
| verdict | `INCONCLUSIVE` | `probes/BATTERY-LUNA-LEDGER-20261119.json` | `$.verdict`, line 740 |

## 2. Synthesis (pending enrichment)

The substrate battery's own verdict is `INCONCLUSIVE` under its pre-committed rule.

## 3. Genuine gap (pending enrichment)

TBD after full record sweep.

## 4. STAR-ADDITION (pending enrichment)

TBD.
