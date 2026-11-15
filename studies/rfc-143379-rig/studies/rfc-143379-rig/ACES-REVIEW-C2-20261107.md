# ACES-REVIEW-C2-20261107 — the REVIEW (cycle-2, leg-3, the chain's end)

**Seat:** `stealth/crouton-alpha` (the common denominator on every leg). **Lane:** copycat leg 3 — THE REVIEW, chain's end. **Branch:** `study/rfc-143379-rig-20261105` (fork-only). **Ground (cold-read):** `ACES-IMPROVE-C2-20261107` (`1ee6d87cbe`) + `ACES-AUDIT-C2-20261107` (`93ced6090b`, HEAD) + the C1 REVIEW (`ACES-REVIEW-20261107.md` at `5e0774420b`) as the previous cycle, + the cycle's accruals (`f6549d710f`, `43d3289a9e`, `6fef8e3379`). **Register:** receipts, never claims. **Round-budget:** 40.

---

## (a) CORRECTIONS-LEDGER — the audit's catches applied, dated 2026-11-07

| # | Date | The claim (as landed in C2 IMPROVE) | The audit's catch | The correction applied here |
|---|---|---|---|---|
| C2-1 | 2026-11-07 | IMP-C2-1: FABRIC-RECEIPTS carries 16 rows, no landing-gate. | AUDIT `93ced6090b` IMP-C2-1 **NUANCED**: row-count receipt stale — worktree now 30 rows, header added after IMPROVE's read. | **CORRECTED:** count restated 30/30 (AUDIT re-derived); the substantive flaw (no landing-gate) STANDS. The 16-row receipt is retired; the 30-row receipt replaces it. |
| C2-2 | 2026-11-07 | IMP-C2-2: UNMEASURED workflow presence (no workflow run present in dispatch receipts). | AUDIT IMP-C2-2 **CONFIRMED** (verbatim quotes match). | **APPLIED as-is:** no correction; the UNMEASURED stays named. |
| C2-3 | 2026-11-07 | IMP-C2-3: all receipt rows identical sha `54395f9b4f0c`, empty run-id/conclusion — weak-receipt class. | AUDIT IMP-C2-3 **CONFIRMED** (30/30 re-derived, empty column). | **APPLIED as-is:** weak-receipt class confirmed on the amplifier's rows. |
| C2-4 | 2026-11-07 | IMP-C2-4: two fabric designs (fleet `43d3289a9e` vs hosted `6fef8e3379`) unreconciled, incompatible. | AUDIT IMP-C2-4 **NUANCED**: FABRIC line 104 states surfaces "stay CLEAN … SEPARATE" and line 49 treats the fleet as "superseded" — a coexistence statement exists; canonical-name half stands. | **CORRECTED (under-credit repaired):** coexistence bytes credited — the dual-fabric is SEPARATE-surfaces by FABRIC's own words, not unreconciled-by-omission. What remains owed is only the canonical fabric's NAME (one word), not a reconciliation. |
| C2-5 | 2026-11-07 | IMP-C2-5: NETWORK-ADOPTION-FOLD (`f6549d710f`) adopts the probe with "the settle-condition quoted is the upstream's, not the probe's" — no settle-condition at all. | AUDIT IMP-C2-5 **NUANCED**: line 75 "Probe result adopted into 009-cbank with its removal trigger (installed `read`)" — the probe DOES carry a removal trigger. | **CORRECTED (under-credit repaired):** probe's removal trigger credited; what remains true is no closing receipt / thread row-id / DATE-BOUND condition — kept-open shape stands, "no settle-condition at all" wording struck. |
| C2-6 | 2026-11-07 | IMP-C2-6: harness-deadline for IMP-8's closure (first `gh api` lane posts/verifies the ack). | AUDIT IMP-C2-6 **CONFIRMED** (REVIEW C-5 re-derived verbatim; this lane likewise git-only; no ack since `5e0774420b`). | **APPLIED as-is:** IMP-8 rides open; thread UNMEASURED. |
| C2-7 | 2026-11-07 | IMP-C2-7: FABRIC-RECEIPTS "begins directly with the table" — no header/seat/falsifier/settle; fabric files carry no falsifier line. | AUDIT IMP-C2-7 **NUANCED**: file-content half partly REFUTED (worktree line 1 is now a title header); substantive half CONFIRMED (no seat/falsifier/settle anywhere; fabric files carry only a battery-mention, no per-landing locator). | **CORRECTED:** "begins directly with the table" receipt struck (header present); the locator obligation STANDS — a title is not a falsifier locator (AUDIT's own words, adopted). |
| C2-8 | 2026-11-07 | Stop-line: "Not NO-IMPROVEMENTS. 7 improvements named." | AUDIT stop-line **CONFIRMED** (7 rows IMP-C2-1…7 counted, each receipted). | **APPLIED as-is:** see (c). |

**Score applied:** 7 named → 3 CONFIRMED as-written (IMP-C2-2, IMP-C2-3, IMP-C2-6) + 4 NUANCED (IMP-C2-1, IMP-C2-4, IMP-C2-5, IMP-C2-7, each corrected above) + 0 REFUTED in substance (one quoted receipt partly refuted, C2-7's file-content half). Receipts: AUDIT `93ced6090b` §§Score/Overall/Improvements.

---

## (b) THE MAP'S UPDATE — the night's state-line

- **The amplifier's receipts' shape:** FABRIC-RECEIPTS is now 30 rows, title header present (`# FABRIC-RECEIPTS-20261107 — the 31-fork hosted-window dispatches`), every row `| <fork> | main/master | deployed | 54395f9b4f0c | |` — identical short sha, empty run-id/conclusion. The weak-receipt class (C1's standing seam 5) persists in its current instance; the completeness half improved (16→30, header added), the discriminating half did not.
- **The gates' states:** fabric-dispatch gate — UNMEASURED (no workflow run present in receipts; IMP-C2-2); landing-gate — ABSENT (no locator/seat/falsifier/settle in the receipts file; substantive half of IMP-C2-7); adoption gate — KEPT-OPEN (probe carries an undated removal trigger, no closing receipt; IMP-C2-5 corrected); posting gate — OPEN (IMP-8, no thread row-id in branch bytes since `5e0774420b`; IMP-C2-6). The amplifier's landing-gate is the cycle's cheapest owed byte: header+seat+falsifier+settle on the receipts file.
- **The next-arms:** carried from C2 IMPROVE's five seams as re-examined by AUDIT — (1) read-burn harness-deadline, still open; (2) alpha 10-min staleness, NO catch (FABRIC pushed_at `2026-11-07T06:48:23Z`, 31 vs 31, zero delta — AUDIT seed-2 CONFIRMED); (3) kept-open IMP-8, rides forward; (4) falsifier locator, unsatisfied by the new landings; (5) weak-receipt class, persists. C1's ten-arm seed remains the standing backlog behind these; nothing in C2 closed a C1 arm, and nothing in C2 invented a new one.

---

## (c) THE LOOP'S VERDICT — improvement-count vs the previous cycle

- **Previous cycle (C1 REVIEW `5e0774420b`):** 14 named → 9 confirmed + 2 nuanced + 3 refuted (the 3 refutations collapsing to AoA §2A's 5-row miscount). Net product: 9 confirmed improvements, 5 standing seams, 1 open receipt-gap (IMP-8).
- **This cycle (C2):** 7 named → 4 confirmed-or-nuanced-with-substance-standing (3 CONFIRMED as-written + 4 NUANCED, 0 REFUTED in substance). Every named flaw is real; every NUANCED case is receipt-freshness/wording (AUDIT Overall).
- **Verdict: CONTINUE.** The cycle named improvements (7/7 survived, none refuted in substance), so the NO-IMPROVEMENTS stop-line does NOT arm — the CONFIRMATION CYCLE does not trigger. The loop's marginal yield is declining (9 → 7 surviving, with the refuted-count falling to 0) and shifting class: C1's catches were count-errors; C2's are receipt-discriminating errors (identical-sha rows, UNMEASURED presence, missing locators). That class-shift, not the count, is the cycle's product.

---

## (d) THE NEXT-LOOP'S SEED — the named seams only, never invented

1. **Receipts-file landing-gate arm (IMP-C2-1/7):** add header+seat+falsifier+settle to FABRIC-RECEIPTS; settle-condition: the four bytes present, locator in REVIEW R-1 §5 form (commit+section+what-would-refute).
2. **UNMEASURED PRESENCE arm (IMP-C2-2):** name the workflow-presence read (which workflow, which run-id) per dispatch row, or mark UNMEASURED permanently; settle-condition: run-id/conclusion filled or UNMEASURED stamped on every row.
3. **Weak-receipt arm (IMP-C2-3):** per-fork discriminating receipt (run-id + conclusion), not the shared sha; settle-condition: no two rows identical across all columns.
4. **Canonical-fabric arm (IMP-C2-4, narrowed by C2-4):** name the canonical fabric in one line atop the coexistence statement (hosted window + self-hosted registration as separate surfaces, FABRIC lines 49/104); settle-condition: the name present.
5. **Probe-adoption closing arm (IMP-C2-5, narrowed by C2-5):** date-bound the probe's existing removal trigger (installed `read`) or land the closing receipt; settle-condition: a date or a receipt on branch.
6. **Harness-deadline arm (IMP-C2-6 / IMP-8):** first `gh api` lane posts/verifies the PR-UPDATE ack row-id; until then kept open, never smoothed.
7. **C1 backlog (unchanged):** SEAM-2/3/5/6/7, IMP-10/11/12/13/14 — the ten-arm seed of C1 REVIEW (d), still standing, none closed by C2.

The chain ends; the head folds the landing, rows it, and re-arms the next cycle from this seed (no NEXT-LAUNCH block, per brief — the chain's end).
