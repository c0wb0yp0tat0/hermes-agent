# COST-LEDGER-20261121 — the palette's delegation economics on the free roster (the arc-survival gap-F close)

TEAM: ACES · the economics class
MISSION: COST-LEDGER — one standard fan-out's ledger, measured; the head-side comparator; the delta verdict; the keep/scale/tune recommendation.
GATE: "nothing public without the user's word." · RFC #143379 QUIET (read-only).
WALL CLAUSE (verbatim): "a non-reproduction is a QUESTION, not a stop."
DOORS: read-only telemetry + the harness's rows · nothing billed beyond the free roster's fair-share · additive · commit at the end.
ARTIFACT (workspace): `/root/workspace/kanban-pilot-workdir/.worktrees/t_fbd600c9/COST-LEDGER-20261121.md`
RECEIPT (machine rows): `probes/COST-LEDGER-20261121.json`

---

## 0 · THE VERDICT (one breath)

The doctrine's claim — "the palette costs $0 and it is the kit's own instrument" (CTO-FREEDOM-FIVEWHY, FIX 1) — is **CONFIRMED in dollars and QUALIFIED in tokens**. On the free roster the four-seat fan-out's marginal dollar cost is **$0.00**; what it spends is fair-share quota: **2,012,329 tokens** against a modelled single-thread **550,287** — a **3.66× token amplification**, so the field's line ("multi-agent consumes more tokens") is TRUE at the grain. But the shadow premium at the published paid rate is only **$0.0585** (5.8 ¢), and what it buys is decisive: **487,348 tokens of head-context** that never enter the head's window. The single-threaded equivalent **crosses the 524,288 compression trigger** (550,287 > 524,288, 1.05×); the fan-out's head-load is **62,939 tokens (12% of the trigger)**. **Recommendation: KEEP the palette as the long-arc default, SCALE it to every long arc, TUNE the per-lane prompt duplication — with fair-share (not dollars) as the scaling ceiling.**

## 1 · THE CLAIM UNDER TEST

| Source | The line |
|---|---|
| Field (as stated in the card) | "multi-agent consumes more tokens; the performance gains justify the cost." |
| CTO-FREEDOM-FIVEWHY-20261121, FIX 1 | "any long arc ... opens with the supervisor palette ... all free-tier ... the head reduced to look-and-verify. The palette costs $0 and it is the kit's own instrument." |
| ARC-LONGEVITY-STORM-20261121, mechanism 3 | "the head's window stays lean because the judgment work runs in independent lanes — the session-pressure never accumulates to the compression trigger's speed." |

GAP-F, named here: those three lines assert an economics that the rig had never ledgered. This card is the ledger they were owed. (No pre-existing "GAP-F" label was found in the record; the gap is named by this card, not invented from a prior one.)

## 2 · METHOD (and what is measured vs derived)

- **Telemetry (measured):** `/root/workspace/drop/backwards-audit/FLEET-TOKENS-20261111.jsonl`, **7,459 rows**, 2026-11-12 → 2026-11-21 UTC. Written by the harness at `copycat-harness.py:168-175` on each response's `usage` block. Fields: `t`, `model`, `endpoint`, `prompt`, `completion`, `total` (+ `req_bytes` on Nous-route rows). Read-only; no lane fired for this card.
- **Fan-out selection:** 10-minute buckets with ≥3 distinct models after 2026-11-20. Two windows qualify: **A (primary, 14:30Z, four seats)** and **B (replication, 11:20Z, three seats)**. A is the standard four-seat bounded-audit shape (qwen4 · hy4 · solar · longcat = the same seat set as CROSSCHECK §1's four ledger lanes).
- **Cost (measured-at-rate):** free roster → **$0.00** marginal. Shadow price for comparison uses the one published paid rate in the record, `tencent/hy4-flash` = **$0.04 / 1M in, $0.14 / 1M out** (NEMO-HY4-START-20261117-brief.md). The same brief says the free-plan allowance is **UNPUBLISHED — never invent a cap**; no cap is assumed here.
- **Head-side comparator (DERIVED, not a fired run):** the same bounded audit single-threaded. Model = *one read of the source at the mean lane prompt + all verdicts authored in the one window*. It is a model, not a reproduction — per the wall clause a non-reproduction stays a QUESTION, not a stop, and is labelled as such rather than smoothed into a measurement.
- **Compression trigger:** **524,288** tokens = 0.5 × 1,048,576 (ARC-LONGEVITY-STORM § THE FINDING).

## 3 · THE PER-LANE ROWS (the harness's usage telemetry, primary fan-out A)

Window **2026-11-21 14:34:32Z → 14:44:48Z** (UTC). 179 rows.

| Lane (seat) | rows | prompt | completion | total | req_bytes | first→last (UTC) |
|---|---:|---:|---:|---:|---:|---|
| `meituan/longcat-2.5:free` | 69 | 815,205 | 35,235 | 850,440 | 2,603,369 | 14:34:32→14:44:48 |
| `qwen/qwen4-max:free` | 40 | 373,437 | 10,495 | 383,932 | 1,263,656 | 14:34:54→14:43:03 |
| `tencent/hy4-flash:free` | 30 | 471,264 | 12,090 | 483,354 | 1,591,977 | 14:34:54→14:38:00 |
| `upstage/solar-mini4:free` | 40 | 289,484 | 5,119 | 294,603 | 934,594 | 14:34:52→14:35:59 |
| **FAN-OUT TOTAL** | **179** | **1,949,390** | **62,939** | **2,012,329** | **6,393,596** | 14:34:32→14:44:48 |

Replication **fan-out B** — window 11:29:46Z→11:44:49Z, 120 rows, 3 seats: longcat 40 rows / 390,054 / 18,591 / 408,645; qwen4 40 / 364,235 / 17,474 / 381,709; solar 40 / 356,042 / 6,053 / 362,095. Total **1,110,331 prompt / 42,118 completion / 1,152,449**. (A 1-row stepfun seat-probe in the window is excluded from B's lanes; it is not a ledger lane.) Both windows and all per-lane figures are byte-identical to `probes/COST-LEDGER-20261121.json`.

## 4 · THE HEAD-SIDE COMPARATOR (derived)

| Quantity | Fan-out A (measured) | Head-side single-thread (modelled) | Δ |
|---|---:|---:|---|
| Prompt tokens ingested | 1,949,390 | 487,348 (mean lane prompt) | +1,462,042 duplicated by lanes |
| Completion tokens authored | 62,939 | 62,939 (same verdicts, one author) | 0 |
| Total tokens | **2,012,329** | **550,287** | **+1,462,042 = 3.66×** |
| Tokens entering the head's window | **62,939** (verdicts only) | 550,287 (whole audit) | **−487,348** |
| Share of the 524,288 compression trigger | 12.0% | 105.0% | fan-out under / head over |
| Shadow cost @ hy4-flash paid rate | $0.086787 | $0.028305 | +$0.058482 |
| Actual cost, free roster | **$0.00** | $0.00 (model) | $0.00 |

Replication B: amplification **2.80×** (1,152,449 / 412,228), head-context saved **370,110** tokens, head-load **42,118 (8.0% of trigger)** vs single-thread 412,228 (78.6% — under the trigger). B confirms A's direction at a smaller mission; only A's single-thread crosses the wall.

## 5 · THE DELTA VERDICT

1. **The field's token line is TRUE, at the grain.** Four independent lanes each re-send their own standing context: 1.95M prompt tokens to produce 62.9K of verdict — a **31:1 prompt-to-completion ratio**. The duplication, not the verdicts, is the 3.66×.
2. **"Costs $0" is TRUE in dollars, FALSE as a resource claim.** Marginal dollars are zero on the free roster; the real meter is **fair-share quota** (the 429s that the 5-why already named on stepfun/qwen4). Scaling the palette is bounded by rate limits, not by an invoice.
3. **What the delegation buys is the scarce resource.** The head sees **62,939 tokens**, not 1.95M: **487,348 tokens — 93% of one compression trigger — are kept off the head's window.** On the primary fan-out the single-threaded audit **crosses the 524,288 trigger** while the fan-out stays at 12%. This is the ARC-LONGEVITY mechanism 3 claim, now receipted: delegation is an arc-survival lever, not a convenience.
4. **The shadow premium is trivial in absolute terms** — 5.8 ¢ for the primary fan-out at the one published paid rate. Even fully priced, the economics favor the fan-out for any long arc where head-context is the critical path (CTO-FREEDOM-FIVEWHY WHY 4).

## 6 · RECOMMENDATION — KEEP / SCALE / TUNE

- **KEEP** the supervisor palette as the standing long-arc default (CTO-FREEDOM-FIVEWHY FIX 1 stands; this ledger is its receipt). No reversal: the dollar cost is zero and the head-context gain is measured.
- **SCALE** to every long arc (night/wave/multi-leg). The binding constraint to watch is **fair-share**, not dollars — dispatch must keep the seat-probe cadence that avoids 429 wedges; the palette is free but not unlimited.
- **TUNE** one thing: **per-lane standing-context duplication** (31:1 prompt:completion). The lever is the lane's prompt footprint (the rig's read-gate + window cap already bound rounds; bound the *bytes* re-sent per lane next). Heaviest lane is longcat at 815,205 prompt tokens (42% of fan-out A) — task-driven (its FATE-style ticket fetch carries the large body), so trim the source payload before trimming the lane.
- **Do not tune** the head-side default back toward single-thread on cost grounds: the 5.8 ¢ premium is not the trade's deciding term, and the single-thread crosses the compression wall.

## 7 · HONEST WALLS (carried, not invented)

1. **The head-side comparator is modelled, not fired** — one read of the source at the mean lane prompt + all verdicts in one window. Per the wall clause, "a non-reproduction is a QUESTION, not a stop": the number is labelled DERIVED and the alternative head context (a head already carrying a night's window) would only widen the gap in the fan-out's favor. Not asserted as measured.
2. **Mission label is not in the telemetry.** The rows carry model/tokens/timestamps, not a mission id; A is identified as a *representative bounded-audit fan-out* by its four-seat concurrency and seat set (CROSSCHECK §1), not by a label in the row. B's exact mission is likewise unnamed.
3. **Free-plan allowance is unpublished** — no cap, quota, or dollar value is invented for free tokens; the shadow rate is the published paid hy4-flash rate used only as a comparator.
4. **Two windows, not a census** — A and B are the qualifying concurrent fan-outs on 2026-11-21 in this ledger; single-lane traffic is not attributed to a fan-out.
5. **Paid-rate market risk**: $0.04/$0.14 is a dated rate from a rig brief, not a live quote. If prices move, re-run `probes/COST-LEDGER-20261121.json` with the new rate; the dollar verdict is robust while the premium stays cents.

## 8 · RECEIPTS & REPRODUCTION

- Telemetry: `wc -l /root/workspace/drop/backwards-audit/FLEET-TOKENS-20261111.jsonl` → 7459; harness write path `copycat-harness.py:168-175`.
- Wall clause: study `audit/CHAMPION-ROW-FOLD-20261119.md` line 3 and `LUNA-LEG-AUDIT-20261119-brief.md` line 3 — "a non-reproduction is a QUESTION, not a stop."
- Palette doctrine: `audit/CTO-FREEDOM-FIVEWHY-20261121.md` lines 15/24/27.
- Compression trigger: `audit/ARC-LONGEVITY-STORM-20261121.md` lines 7-9 (0.5 × 1,048,576 = 524,288).
- Paid comparator: `NEMO-HY4-START-20261117-brief.md` line 11 ($0.04/$0.14 per 1M; free allowance unpublished).
- Re-derive: load the jsonl, bucket by UTC 10-minute window, sum `prompt`/`completion`/`total` per `model` in 14:30Z→14:45Z and 11:20Z→11:45Z; compare with `probes/COST-LEDGER-20261121.json`. No network calls; no lanes fired.

---

*Facimus semper — the ledger renders on the record; the record corrects itself out loud.*
