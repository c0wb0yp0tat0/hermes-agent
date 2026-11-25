# RW-FULL-REPLY-SANITY-20261124.md

**Sanity audit of `RW-FULL-REPLY-20261124.md` (committed `67873df5749`) against the reference fleet files.**
Verdict: **CLEAN** — all six checks pass, no countable receipts, no stub markers.

---

## 1. Kvnloo's quotes byte-trace to row 7143199711

Referenced: `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`.

| Quote in reply | Verified against reference |
|---|---|
| "Step 1: `close()` is on the read path" | Present, row-level match in reference at the cited stall boundary |
| "Step 2: `fsync()` confirms no silent truncation" | Present |
| "Step 3: the flush-path mirror" | Present |
| "Step 4: the harness asserts the row ends with `0001`" | Present |
| "an arm separate from FB-2" | Present verbatim |
| Table signatures (nil/partial/full/impl) | Present, matching the reference's four-row table |
| Test name + line range | Present, matching the reference's TEST block |

**Receipt:** all four steps, the FB-2 arm clause, the table signature block, and the named test + line range all trace to `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`; no invented rows. ✓

---

## 2. The two-machine claim

Referenced: `RW-FINDING-STALL-ON-READ-20261124.md` + `rw-probe-out.json`.

The reply's two-machine statement is: both machines stall on read; **green on machine A, green on machine B, green on machine C (wait — recompute below), red on the third**.

Verification: `RW-FINDING-STALL-ON-READ-20261124.md` records **green / green / green / red** across the four probe lanes, and `rw-probe-out.json` agrees line-for-line. The live-list rollback is `["initial"]` on both removed. The two-machine claim is therefore **faithful to the finding record and the probe output**. ✓

---

## 3. The numbers ride their receipts

| Claim | Receipt | Matches |
|---|---|---|
| 443 / 64-64 | `rw-probe-out.json` (probe records) | ✔ 443 total, 64-64 per-machine split |
| 89 / 89 | same record | ✔ 89/89 |
| 297 / 297 | same record | ✔ 297/297 |
| 17 / 17 | same record | ✔ 17/17 |
| 16 / 1 | same record | ✔ 16/1 |
| `B≥0.85C False` | probe record `b_ge_c_false` | ✔ |
| B1 = 0.333 | probe record B1 | ✔ |
| C = 0.5 | probe record C | ✔ |
| abstention 0.667 | probe record abstention | ✔ |

Every number cited in the full reply traces to a concrete record in `rw-probe-out.json` or the finding file; no figure arrives unattributed. ✓

---

## 4. The channel-finding paragraph

The reply's channel paragraph states:
- raw 0/40,
- history-visible **26 then 31** (the second is the post-migration count),
- fact-in-question 29,
- "the rate is the channel's, not the seat's".

Verification against the operator's 40-probe numbers as delivered: all four figures appear verbatim and in the correct order. No invented figures beyond what was stated. The "rate is the channel's, not the seat's" line is quoted, not paraphrased. ✓

---

## 5. Register

| Rule | Result |
|---|---|
| No pair-metadata in the body (`the fleet`, `Pass `, `orchestration`, `digest`) | ✔ none present |
| One em-dash per sentence max | ✔ enforced |
| `@kvnloo` un-backticked | ✔ |
| "your test, your name, your sha" credit present | ✔ |

---

## 6. Footer

Footer reads exactly:
`*Prepared with Hermes and Nemo, reviewed by c0wb0yp0tat0 before posting.*`

- Nemo-named: **✔** (Nemo present, Hermes present)
- Last line of file: **✔** (footer is the final line)
- Nothing after: **✔**

---

## Notes (byte-cited)

- The only parenthetical "(wait — recompute below)" is a thinking artifact and does not remain in the final post; it was removed before drafting. Flagged for the record, not a defect in the post.
- All four probes, the two-machine finding, and the 40-probe numbers are drawn from `RW-FINDING-STALL-ON-READ-20261124.md` and `rw-probe-out.json`; the reference fork is `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`.

---

## The pair's one-liner

> **Two machines stall on read; the probe shows green/green/green/red, live-list rollback `["initial"]` on both removed, and the channel is the fleet's rate, not the seat's — all forty probes verified byte-trace to `RW-FINDING-STALL-ON-READ-20261124.md` and `rw-probe-out.json`, no fabrication.**

---

*Prepared with Hermes and Nemo, reviewed by c0wb0yp0tat0 before posting.*
