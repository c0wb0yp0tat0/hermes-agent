# L-2 — The economics + scale contract (longcat-2.5:free), 2026-11-19

*The leg's cost + scale contract, so L-1 sizes the probe against a real budget. Record-first: receipts named; unread receipts UNVERIFIED, never estimated.*

## 0 · Seat + receipts
- Lane seat: **longcat-2.5:free** (master §2). The lane's run is free; the rows below are the *paid-equivalent shadow class* denominating the cap, since the probe's marginal cash on the free surface is $0.
- Read: `LUNA-MIDDLEWARE-MISSION-20261119.md`; `STORM-HARVEST-4-ECONOMICS-20261119.md`.
- **UNVERIFIED (write-gated):** `LANE-2-CALENDAR-20261119.md`, `5Y-NOTE-7-STORM-20261119.md`, `FLEET-SCRAMBLE-WIRING-20261119.md` §1+§6. Numbers traceable only to those are marked UNVERIFIED.

## 1 · The cost rows
**Luna per-episode:** base **$0.406** (field-measured $0.406/run class; Harvest-4 R1 lineage $0.21→$0.12 with harness) **+ caching overhead 15%** (byte-stable prefix + cache-write; Harvest-4 R1/R4) = **$0.467/episode**.
- **Raw-truncated:** $0.467. PersistGym's truncation shape (94%→48% cache, 2.9–4.0× cost for fewer tokens, R2) is the measured risk the bridged arm is built against; the raw arm's cache-hit is logged, not assumed.
- **Bridged:** $0.467 + the governor — **cheap, deterministic, local** (release-point gate + write-time scribe witness; no extra model tokens). Marginal model spend ≈ $0; the governor's exact dollar figure is **UNVERIFIED**. The bridge's cost is latency, not tokens.
- **Oracle:** **the free/available surface — NOT the paid row** (master §2/§5; shown-fact control on the same seat). Same $0.467 equivalent; no paid spend unless named + justified.

**Per-arm at §2's scale: 40 × $0.467 = $18.68/arm; 3 arms = $56.04 (paid-equivalent).** Free-surface cash: $0.

## 2 · The scale recommendation
- **40 episodes/arm × 3 arms = 120.** Small-scale, long enough to gather data, enough for the abstention + governance axes to produce measurable rates — **not a 200/arm campaign**.
- Why 40: abstention is a rate; at n=40 a ~30% rate carries ±15pp (95%), and a ≥20pp raw-vs-bridged gap is ~2 SE — measurable. Governance is a witnessed-interaction count; 40 gives a bounded rate. 200/arm is 5× the spend for a CI the mandate doesn't ask for.
- **Pre-committed cap: $100 paid-equivalent (≈214 episodes).** 120 sits at 56% of cap. Named before the fire; a bust is a finding, not a surprise.
- Class corroboration (never adoption): MemCredit's rho=(V−λH)/b bank arbitration = the same denominated-cap class; AIMD's adaptive envelope = the same additive-increase/multiplicative-decrease class as §4; AskALCF's evidence-gated admission = the same admit-on-evidence class as the stop-rule.

## 3 · The seat map
| Arm | Primary surface | Fallback | Notes |
|---|---|---|---|
| Raw-truncated Luna | Luna free route (availability) | free-tier fallback | cache-hit logged; truncation cost is the measured risk |
| Bridged Luna | Luna free route + governor | free-tier fallback | gate + witness same route; governor local |
| Oracle Luna | free/available surface (shown fact) | free-tier fallback | **NOT the paid row**; paid only if named + justified |
| Machine layer | free floor (local) | — | deterministic wire-checks; no per-token cost |
- **Kenari stays reserve; stepfun fully included** (L-3's seat, stepfun/step-3.7-flash:free — free-tier fallback + report-back seat).
- **429/reset discipline:** the calendar's ledger rule is a *single-surface ledger* — an episode's spend rowed once, on the surface that served it; a 429/reset is counted, not silently retried into a second charge. Exact rule **UNVERIFIED**; the class is count-don't-double-spend. SELD's read-side evidence-plane verifier is the same class.

## 4 · The bust-protection clause
The leg **pauses and the finding is rowed** when any of:
1. Total paid-equivalent spend **> $100** (≈214 episodes).
2. Per-arm spend **> $40** (≈86 episodes/arm).
3. Episodes **> 200/arm** — the mandate's ceiling.
4. Any paid-row spend without a named, justified line (the oracle seat is free/available, not paid).
5. Cache-hit collapse on the bridged arm → an economics *finding* (wall clause: a non-reproduction is a QUESTION, not a stop).
- **Two-way door:** the pause rolls back to the plan stage — no fire, no public surface, no report-back. Every move names its rollback: scale is a dial (40↔200/arm), cap is a dial ($100), seat is a two-way route switch (Luna↔free-tier fallback).

## 5 · The compose-check
| Step | State | Evidence |
|---|---|---|
| deconstruct | FIRED | cost rows, scale, seat map, bust clause |
| sense | FIRED | free cash $0; the cap is a shadow paid-equivalent class (Harvest-4) |
| choose | FIRED | 40/arm × 3; $100 cap; Kenari reserve / stepfun included |
| calibrate | FIRED | $0.406 + 15%; 2.9–4.0× truncation penalty; UNVERIFIED honest |
| probe | FIRED | cost rows = the probe's budget; bust numbers = its stop-rule |
| review | FIRED | paid-row exclusion named; 200/arm red line; wall clause held |
| record | FIRED | artifact + commit; receipts named; UNVERIFIED explicit |
| compose-check | FIRED | plan → land → enrich → synthesize → verdict → fire → negentropy |

## 6 · Hand-off
- **L-1:** 40/arm × 3; $100 paid-equivalent cap; bust numbers pre-committed.
- **L-4:** the governor's cost is latency, not tokens — a compliance/witness row, not a dollar row.
- **L-3:** a held bridged cache-hit is a credit-where-credit line for the report-back's tone.