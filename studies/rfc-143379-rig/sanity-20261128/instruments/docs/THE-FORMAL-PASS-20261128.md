# THE FORMAL PASS — chi-square / Fisher on the contingency family

**Date:** 2026-11-28 · **Scope:** the count-bearing tables where a test is defined; the rest are
named as untestable/deterministic, never faked · **Status:** internal; nothing posted

## 0 · The rule this pass runs under

The counts are **deterministic receipts** (fixed code, fixed seeds, fixed contours), not random
samples. A p-value here formalizes the design's separation under the exchangeability null (the
labels permuted) — it does not license a population inference. Where a cell has n=1 or no
failures, the exact test is inapplicable and says so.

## 1 · The structural lock, 2×2 — SEPARATES (perfect)

| | refused | acquired |
|---|---|---|
| inside the lock | 50 | 0 |
| outside the lock | 0 | 50 |

Fisher exact, one-sided: **p = 1/C(100,50) = 9.91 × 10⁻³⁰**; two-sided doubles it to
**1.98 × 10⁻²⁹** (the mirrored table is equally extreme). Risk difference **100 pp**; Cramér's V =
**1.0**. The separation is perfect under the
null; this is the table the reply's structural claim rests on.

## 2 · The 6609dac read × lock, 2×2 — NULL

| | reads not a committed prefix | reads fine |
|---|---|---|
| lock present | 0 | 1,028 |
| lock nulled | 0 | 6,566 |

Fisher exact, two-sided: **p = 1.0** — no events, no table as extreme as the observed; Cramér's
V = **0**. The test formalizes the null: **the output row carries no lock signal.** The structural
row (§1) is the witness, not this table. (File complete 50/50 in both cells — also no signal.)

## 3 · The anchor-read, 3-cell — SEPARATES

Counts 50 / 50 / 0 (anchor → chain doc, anchor → orphan, anchor alone). Goodness of fit vs uniform
(expected 33.3 each): **χ² = 50.0, df = 2, p = e⁻²⁵ = 1.39 × 10⁻¹¹**; Cramér's V = **0.50**. The
pointer's two destinations are distinguishable from no pointer; the three-cell table is a real
spread, not a null.

## 4 · The four-variant envelope — A RECEIPT, NOT A SAMPLE

Four cells, one deterministic run each (GREEN · GREEN · GREEN · RED). n=1 per cell: **no test is
defined.** The envelope's claim is byte-determinism — the same store and seed produce the same
receipt sha256 (`3ff6aee4…fba9`) — which a p-value would only obscure. Verdict: RECEIPT.

## 5 · The 12-cell battery — PORTABILITY

12/12 green; no failure cell, so no association test exists. The exact 95% Clopper–Pearson bound on
the pass rate: **0.735 ≤ p ≤ 1.0** (12/12). Descriptive only — the contours are a fixed set, not a
sample. Verdict: PORTABILITY, with the bound named.

## 6 · The k-term, class × kept — OWED (the counts are missing)

Rates 0.42 / 0.29 / 0.26 / 0.32; empties 24 / 36 / 22 / 48; overalls 2.61 / 2.75 / 3.08 / 2.13.
The 2×4 (kept/lost × class) needs the raw kept counts per class; the 16 ladder JSONs are not on
this host. **The test is owed with the extraction**; the flat rates (0.26–0.42) are the finding
that motivates it. No p-value is manufactured here.

## 7 · The generation × survival — RATES, NO TEST

~95% → ~60% → ~40% → 20–50% across four generations; no control arm, no counts. A rate curve, not
a contingency.

## 8 · The seats × legs — n=4, not significant

solar 2/2 real; hy 0/2 (stubs, one refused). Fisher exact on [[2,0],[0,2]]: **p = 1/3 = 0.333**
(n=4). The seats' difference is not statistically established; the sample is the seats, and the
finding is qualitative — one seat reports, one stubs. Stepfun pending.

## 9 · The etc.: effect sizes, family, power

- **Effect sizes:** structural V=1.0, anchor V=0.50, 6609dac V=0 — perfect / moderate / none.
- **Family:** the four count-bearing tables test different instruments against different outcomes;
  no simultaneous family, no correction required. If treated as an exploratory family of four:
  Bonferroni α = 0.0125; the structural (1e-29) and the anchor (1.4e-11) survive; the 6609dac
  (p=1) does not; the envelope is untestable.
- **Power:** the structural's perfect separation needs no power argument; the anchor's n=100 with
  a 50/50/0 spread is far past any power floor; the seats' n=4 has no power — hence the refusal to
  claim a seat difference.

## 10 · What the pass changes

Nothing in the reply, the child, or the tables. It converts the control-overlap's four states into
numbers: **SEPARATES** (structural, anchor), **NULL** (6609dac), **PORTABILITY** (12-cell),
**RECEIPT** (envelope), **OWED** (k-term), **RATES** (generation), **n=4** (seats). The formal pass
is the contingency family's own control: where it is silent (the envelope, the k-term), the silence
is named, not filled.
