# COPYCAT-REVIEW-20261107 — the constant copycat's first pass (2026-11-07)

**Seat:** `stealth/crouton-alpha` · **Lane:** copycat (constant) · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Register:** receipts, never claims · **Round-budget:** 40.
**Ground (cold, independent):** `ACES-IMPROVE-20261107.md` (`e640efb7a3`) + `ACES-AUDIT-20261107.md` (`9769ab931d`) + `ACES-REVIEW-20261107.md` (`5e0774420b`) + `ACES-IMPROVE-C2-20261107.md` (`1ee6d87cbe`) + `ACES-AUDIT-C2-20261107.md` (`93ced6090b`) + `ACES-REVIEW-C2-20261107.md` (`653f535bfd`) + `ACES-IMPROVE-C3-20261107.md` (`c9a0325719`) + `ACES-AUDIT-C3-20261107.md` (`ca15b98e1f`) + `ACES-REVIEW-C3-20261107.md` (`98e8de2303`) + `FABRIC-RECEIPTS-20261107.md` at HEAD (`50c7d71535`) + `git log` to HEAD. Thread tail via `gh api`: UNMEASURED in this git-only lane — flagged, never filled in. **C4 artifact:** none landed as of this pass (no `*C4*` file at HEAD; last ACES landing `98e8de2303` + 2 fabric/fleet landings `2becb714af`, `50c7d71535`) — noted, not invented.

---

## (a) AGREEMENT-DIVERGENCE TABLE — the loop's verdicts vs the copycat's independent re-read

| Cycle | Loop's claim (as landed) | Copycat re-read | Convergence / Divergence | Receipt |
|---|---|---|---|---|
| **C1** IMPROVE (`e640efb7a3`) | 14 named, 7 seams. | 14 IMP-1…14 rows present in file; seam count 7 as claimed. Count re-derives. | **CONVERGES** | File `ACES-IMPROVE-20261107.md` CLASS-COUNTS table, cold-read. |
| **C1** IMP-1 / SEAM-1 (restore 6th goal row) | Named as a real gap. | The IMPROVE's own receipt quotes only AoA `c54c1bc614` §2A (5 rows), never the plan's §1. Byte check available to the next leg shows the plan carries 6 rows. The claim as *receipted* was weak even in C1. | **DIVERGES from the IMPROVE** (the loop's own AUDIT already caught this — credited) | `e640efb7a3` IMP-1 receipt column: quotes AoA only. AUDIT `9769ab931d` IMP-1 REFUTED (plan §1 six rows). |
| **C1** AUDIT (`9769ab931d`) | 9 CONFIRMED / 2 NUANCED / 3 REFUTED (IMP-1/6/7 fall on the 5-vs-6 miscount); REVISIONS-NEEDED. | Per-row re-read matches: REFUTED 3 = IMP-1,6,7; NUANCED 2 = IMP-3,8; the 5-vs-6 premise is AoA's, contradicted by plan + audit's own six-row table (AUDIT §CORRECTIONS-LEDGER C-1). Tally 9+2+3 = 14 re-adds. | **CONVERGES** | `9769ab931d` CLASS-COUNTS line + per-row ledger. |
| **C1** REVIEW (`5e0774420b`) | Corrections C-1…C-5 applied (C-1/2/3 struck, C-4 downgraded, C-5 kept open); 3 review additions; 5 standing seams. | Ledger applied as stated; additions are real rows (falsifier §5 locator, APEX staleness, IMP-5 weak receipt) in file. C-5/IMP-8 honestly kept open (thread UNMEASURED, delivery vs ack distinguished). | **CONVERGES** | `5e0774420b` corrections-ledger table. |
| **C2** IMPROVE (`1ee6d87cbe`) | 7 improvements named (IMP-C2-1…7); stop-line NOT carried. | 7 rows, each with receipt, in file. Count re-derives. | **CONVERGES** | `1ee6d87cbe` counts + ledger. |
| **C2** AUDIT (`93ced6090b`) | 4 CONFIRMED / 4 NUANCED / 0 REFUTED; REVISIONS-NEEDED (IMP-C2-1/7 receipts stale: 16→30 rows + header; IMP-C2-4/5 under-credited). | NUANCED verdicts re-derive: worktree FABRIC-RECEIPTS at audit time had grown 16→30 rows and gained a header after IMPROVE's read; FABRIC `6fef8e3379` L104 coexistence + L75 probe removal-trigger ("installed `read`") are real bytes the IMPROVE under-credited. 4+4+0 = 8 rows re-adds. | **CONVERGES** | `93ced6090b` per-row ledger (IMP-C2-1,4,5,7 NUANCED evidence-words). |
| **C2** REVIEW (`653f535bfd`) | 8-row corrections-ledger (3 confirmed, 4 nuanced-corrected, 0 refuted in substance); CONTINUE; 7-arm seed. | Ledger matches AUDIT's catches row-for-row (C2-1…C2-7 + stop-line). The seed's 7 arms are verbatim statuses, nothing closed by fiat. | **CONVERGES** | `653f535bfd` (a)+(d). |
| **C3** IMPROVE (`c9a0325719`) | 0 improvements; NO-IMPROVEMENTS stop-line; 7 arms re-examined (1 closed, 2 partial, 4 standing). | `git log --oneline 653f535bfd..c9a0325719` = only `c9a0325719` (zero intervening landings pre-C3) — count re-derives. Fabric status at HEAD (31 rows, 30 `queued`, 1 `in_progress` `dsh-node-addon-require-builtin`, no conclusion column) matches the C3 claim. Arm-3 closure (31 distinct run-ids `42349103810…42349191196`) meets the REVIEW-C2 (d) settle-condition as written. | **CONVERGES** | `c9a0325719` counts; FABRIC-RECEIPTS at HEAD (31-row table, run-id column filled, status-only). |
| **C3** AUDIT (`ca15b98e1f`) | 11 CONFIRMED / 0 NUANCED / 0 REFUTED; READY-FOR-THE-REVIEW; stop-line CONFIRMED. | 11 rows re-add (counts 3 + arms 7 + stop-line 1). Zero new commits pre-C3 + zero landed conclusions + thread UNMEASURED (flagged, never filled in) ⇒ no new improvement can attach — the stop-line logic re-derives. | **CONVERGES** | `ca15b98e1f` per-row ledger 1–11. |
| **C3** REVIEW (`98e8de2303`) | NO-IMPROVEMENTS; confirmation cycle arms, then shift HOLDS; 8-arm seed. | Verdict logic re-derives from C3/AUDIT-C3 evidence. Yield sequence 9→7→0, refuted 3→0→0 is a clean convergence signal, not a count artifact. Seed (8 arms + C1 ten-arm backlog) carries statuses without inventing closures. | **CONVERGES** | `98e8de2303` (b)–(d). |
| **C4** | *(none landed)* | No `ACES-*C4*` artifact at HEAD `50c7d71535`; `git ls-remote origin study/rfc-143379-rig-20261105` = local HEAD (landing-gate holds, no C4 bytes to re-read). | **NO DIVERGENCE — UNMEASURED** | `git ls-files` (no C4) + `git ls-remote` at read time. |

**Divergences found: zero in substance.** The only divergence is C1's IMP-1/6/7 family — and that was caught by the loop's own AUDIT, not missed by it. No seam the loop missed is re-derived in this pass.

---

## (b) THE VERDICT

**The loop's convergence CONFIRMED — the no-improvement's real.** Three independent cycles converge on the same evidence to the same conclusion: C1's refutations are byte-earned (plan §1 six rows vs AoA's five-row premise), C2's nuances are re-derived (fabric file grew post-read, coexistence and removal-trigger bytes exist), and C3's 11/11 CONFIRMED stop-line re-derives from 0 new commits + 0 landed conclusions + honestly-flagged UNMEASURED thread. The arm-3 closure is backlog-settlement, not new product. No divergence is named; the copycat adds none by fiat.

Standing caveat (not a divergence, kept open): the thread tail remains UNMEASURED in every git-only lane including this one (IMP-8 / arms 6 in every cycle). Convergence is on branch bytes; a thread-side landing could still re-open C-5/IMP-8. The loop never smoothed this — credited.

---

## (c) THE COPYCAT'S OWN ADDITIONS (never invented, always receipted)

1. **Post-C3 fabric drift exists and the loop's arm-2 status already covers it.** Two landings postdate the last ACES cycle: `2becb714af` (FABRIC-RECEIPTS fabric-2.0 re-dispatch rows, per-fork pins) and `50c7d71535` (fleet-cycle-body delegate). HEAD FABRIC-RECEIPTS (70 lines) still has no `seat`/`falsifier`/`settle` string (grep count 0), still status-only with no conclusions — so arms 1, 2, 7 stand exactly as C3 REVIEW's seed states; the drift does not close any arm, and claiming otherwise would be invention. Receipt: `git show HEAD:studies/rfc-143379-rig/FABRIC-RECEIPTS-20261107.md` (grep `seat|falsifier|settle` = 0 matches; table still `queued`); `git log --oneline 98e8de2303..HEAD` = `2becb714af`, `50c7d71535`.
2. **Sentinel sidecar files are accumulating untracked in the worktree** (14 × `*.sentinel` under `studies/rfc-143379-rig/`, all `??` in `git status`). No loop artifact names them; they are not improvements (no claim attaches) but they are a new unnamed gap the loop's lenses did not see: they will never land-gate and will keep polluting `git status` for every future lane. Named here only, not fixed. Receipt: `git status --short` at read time (14 `??` sentinel entries).
3. **C4 has not landed — the confirmation cycle the C3 REVIEW ordered is the one outstanding pass.** The C3 REVIEW's stop-line is conditional ("one confirmation cycle re-runs C3's ground unchanged; the shift then HOLDS"). This copycat pass is *not* that cycle and does not discharge it. Receipt: no `ACES-*C4*` at HEAD; `98e8de2303` (d) seed.

The chain ends; the copycat's verdict folds at the head's boundary; its row rides the landing. No self-fire chain.
