# THE CONTROL OVERLAP — the abstraction over the contingency family

**Date:** 2026-11-28 · **Input:** the seven contingency-shaped tables (four count-bearing, two rate-only, one seats) · **Status:** internal; nothing posted

## 1 · The inventory, restated

| # | table | the instrument | the outcome | the cells |
|---|---|---|---|---|
| 1 | 6609dac read × lock, 2×2 | the output row | reads not a committed prefix | 0/1,028 vs 0/6,566; complete 50/50 both |
| 2 | structural lock, 2×2 | the structural check | refused / acquired | 50/50 inside; 50/50 outside; three contours |
| 3 | anchor-read, 3-cell | the anchor | chain doc / orphan / alone | 50 / 50 / 0 |
| 4 | four-variant envelope, 4 cells | the fix's arms | green / red | G · G · G · RED (rollback) |
| 5 | 12-cell battery | the contours | cell pass | 12/12 green |
| 6 | k-term, class × kept | the class ordering | kept rate | 0.42/0.29/0.26/0.32; empties 24/36/22/48 |
| 7 | generation × survival | the compaction | survival | 95 → 60 → 40 → 20–50% |

## 2 · The overlap: the control

Every table has the same skeleton — **the instrument's state × the outcome's state, cells filled
with counts** — and the same meaning: *does the instrument move the outcome?* The answer lives in
the **control cell**: the row where the instrument is removed, or the null condition, or the
absence of the treatment. Strip the tables and the control is the overlap; the instrument is the
variable, the control is the constant.

| table | the control cell | verdict |
|---|---|---|
| 6609dac 2×2 | the lock nulled | **NULL** — 0 vs 0 non-prefix, 50/50 vs 50/50 complete. The output row cannot distinguish lock from no lock; the structural row is the witness. |
| structural 2×2 | outside the lock | **SEPARATES** — 50/50 refused inside vs 50/50 acquired outside; the condition moves the outcome. |
| anchor 3-cell | the anchor alone (0) | **SEPARATES** — 50/50/0; the pointer's two destinations are distinguishable from no pointer. |
| envelope 4 | both removed | **SEPARATES** — the rollback appears only when both arms are removed; the controls stand. |
| 12-cell battery | none (all green) | **PORTABILITY** — no failure cell, so no separation; it proves the battery travels, not that any arm separates. |
| k-term | the four classes | **UNMEASURABLE** — the raw counts are not on this host; the flatness (0.26–0.42) is the finding, but the control's cells are missing. |
| generation × survival | none (no control arm) | **RATE** — a percentage curve, not a contingency. |
| seats × legs | the seat | **REAL / UNMEASURABLE** — solar separates (real reports); hy is unmeasurable (stubs, refused); stepfun pending. |

## 3 · The abstraction

A contingency table is **a control test wearing four columns.** Its vocabulary is four states:

1. **SEPARATES** — the control moves the outcome; the instrument carries the claim.
2. **NULL** — the control does not move; the table reports no separation, and any claim resting on
   that table is unsupported (the 6609dac output row is a null; the structural row is its witness).
3. **PORTABILITY** — no failure cell; the table proves the instrument travels, not that it separates.
4. **UNMEASURABLE** — the control's cells are missing (the ladder JSONs; the generation arm; the
   stubs). The honest move is to name the missing cell, not to read the rate as a separation.

The four count-bearing tables all have their control; the two rate-only tables are exactly the ones
where the control is missing. That is the overlap abstraction: **the family is one table — the
instrument against its control — and the only differences are which instrument, which outcome, and
whether the control cell exists.**

## 4 · The two overlaps, and the center of the potatoes

The questions table's overlap was **the read** (every question asks whether the record can be read
again). The contingency family's overlap is **the control** (every table asks whether the instrument
moves its outcome). They meet at the same place:

```
        the question: the read
                │
        the control's cell: the lock's structural check
                │
   mechanism ── THE READ-RESTORE ── myth-principle
   (it works)     (witnessed by its control)   (it makes the trust testable)
                │
        the carrier: the record
```

The read-restore is the potatoes' center; the control is its witness. A read without a control is a
story; a control without a read is a null. The center holds both: **the read, witnessed by the
structural check** — the one cell that can distinguish what the output rows cannot.

## The one line

The questions overlap on the read; the contingencies overlap on the control; the center of the
potatoes is the read-restore with its control — the instrument and the cell that makes it a table.
