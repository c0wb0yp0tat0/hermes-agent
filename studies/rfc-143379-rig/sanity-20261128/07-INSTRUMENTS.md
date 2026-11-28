# 07-INSTRUMENTS — the instruments digest (the kit's companion)

**Built:** 2026-11-28 · **Status:** all candidates, class-checked, none adopted · **Register:** [1st] = re-read this pass · [2nd] = carried from a receipt, not re-derived

The kit ships instruments, not just claims. Each row: what it tests, the receipt, the status, the
falsifier. The gate stays failed, not waived; no instrument is a commitment.

**Sources:** the pilot read is `instruments/kit/` (the store's `read()`, RUN.sh, the structural
check, `hybrid_battery.py`, the receipt); the instruments' docs are `instruments/docs/` (the
Read-Restore Eigenvector Bookkeeper, the krecency instrument, the bookkeeper ledger, the
clock-work six, the negentropy adjudication/sweep); the data is `instruments/data/`.

## A · The read instruments (the work's own)

| # | instrument | tests | receipt | status | falsifier |
|---|---|---|---|---|---|
| A1 | **the read kit** (phase-1 + structural check + hybrid battery) | the store's read path on any contour, one command | `RUN.sh`; receipt `3ff6aee4…fba9`; 12/12 cells on pve1/fcntl/py3.13.5 | CANDIDATE, runnable | a contour where the receipt does not reproduce |
| A2 | **the read-invoked counter** | whether the read is called at all (vs read-failed) | the schema field; the session's own surface | CANDIDATE | invoked=0 while the session claims restore |
| A3 | **the structural lock check** | the lock's presence, not its timing (two directions) | `STRUCTURAL-LOCK-CHECK-20261127.py`; receipt `.json` | CANDIDATE | a pass where the structural row and the output row disagree |

## B · The compaction lenses (N1–N3)

| # | instrument | tests | receipt | status | falsifier |
|---|---|---|---|---|---|
| B1 | **N1 the two-N window** | retention across two windows, not one | the 17.9% K=10 carry (conditioned) | CANDIDATE | whole-corpus carry below the window's bar |
| B2 | **N2 the retention latch** | reserved literals surviving the rewrite | 1.00 → 0.00 at 3 literals / 3 tokens; 18 tokens vs the field's 47 | CANDIDATE | a latch that holds where the field's does not |
| B3 | **N3 the tiny-aged-fact axis** | the seam's lost facts (tiny + old) | 17/21 lost (81%) tiny and old | CANDIDATE | a seam where the lost facts are neither |

## C · The clock-work six (the new R&D proposals)

The problem-of-time lens (Barontini's cold-atom test; Kiefer & Zych's "Entropy as a Clock"): time
read from a system's own state, not an external tick.

| # | instrument | tests | status | falsifier |
|---|---|---|---|---|
| C1 | **the internal clock** | the record's own aging as the clock | CANDIDATE | **already met in the study:** k-term kept-rates flat 0.26–0.42 across the four classes — the rate does not separate the classes it orders (`ADJUDICATION-NEGENTROPY-20261106`) |
| C2 | **the drift gauge** | the record against its representation, per compaction | CANDIDATE | a summary that contradicts the record while the gauge reads zero |
| C3 | **the synchronization hierarchy** | the anchor as external reference, the chain as internal; the lock order | CANDIDATE | a single-lock writer that clobbers |
| C4 | **the barrier probe** | the anchor/chain wall, and what crosses it unaccounted | CANDIDATE | **already met in the study:** the read-burn gate; the orphan edge; the remove echo |
| C5 | **the tabletop mini-universe** | the kit at small scale; the contours as the multi-unit test | CANDIDATE | a tabletop pass that fails the 300-cycle field |
| C6 | **the proper-time ledger** | each entry's age/order/origin; `/pin` as the second witness | CANDIDATE | a summary contradicting a pin; an unresolvable origin |

## D · The probes and bookkeepers

| # | instrument | tests | receipt | status |
|---|---|---|---|---|
| D1 | **the Read-Restore Eigenvector Bookkeeper** | pins as explicit eigen-axes; projection error per class | the special-use-case framing (not part of the diff) | CANDIDATE (the eigen lens's fourth) |
| D2 | **the K-recency probe** | the window's gain at 300+ cycles, 4×–8× | the field's −3.5pp; the scope bug | FAILED (probe's bug), not waived |
| D3 | **the bookkeeper** | the read-gap class across the backlog | 140-issue sweep JSON; 300 scanned | CANDIDATE (a tracker, not a gate) |

## The one line

The kit's instruments are the work's own receipts; the clock-work six are the new proposals. Two
already carry a recorded failure (C1, C4) — that is the extraction's honesty, not its defect.
