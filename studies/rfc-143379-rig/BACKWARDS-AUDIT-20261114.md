# BACKWARDS-AUDIT-20261114 — R4 apex-residue reconciliation

**Lane:** copycat · **Ring:** R4 (APEX-RESIDUE RECONCILIATION) · **Seat:** longcat (`meituan/longcat-2.5:free`; the plan's fallback — the first ride died at round 8 on stepfun's fair-share 429) · **Harness:** hardened (one call/round; git-only terminal) · **Date:** 2026-11-14 · **Branch:** `study/rfc-143379-rig-20261105`.

**RECEIPTS (stamped 2026-11-14).** IN-LANE: brief; packet `REFS/R4-GROUND-20261114.md`; `FINAL5-8-FOLD-20261114.md` (R3 handoff, whole); plan `NEMO-DAY-PLAN-20261114.md` (**CLIPPED 12K, read once**); convergence plan `REFS/NEMO-CONVERGENCE-PLAN-20261114.md` (**CLIPPED 12K, read once**); `ACES-AUDIT-C3` / `ACES-AOA-B05` / `ACES-AUDIT-B05` (whole); steer channel (**STEER-1 acknowledged** — drop/ outside roots; ground from REFS/). BORROWED: kilo.ai chain 001 (11-10); harness md5 `8996fd99ff1b7d6f055af7fda8883434`; backwards-audit/memory-chain reads (earlier Nemo legs); NEMO-REGROUP gist crown table (external). Clip rule: the two clipped files are never re-read; tails grounded from the packet, never invented. Commits cited from `git log` IN-LANE.

## 1. THE RECONCILIATION TABLE

| # | Residue row (handle) | STATUS | Receipt (source + stamp) | ACES decision it connects to |
|---|---|---|---|---|
| 1 | FINAL5→FINAL8 chain (S2U draft evolution) | APPLIED | `FINAL5-8-FOLD-20261114.md` IN-LANE 11-14; FINAL5/7/8 read IN-LANE; FINAL6 ABSENT (named); commit `70f6e5fd8c` | R3 FINAL5-8 FOLD (plan C3) — folded; master fold OWED (r19) |
| 2 | S2U original draft `rfc-143379-seek-to-understand-draft.md` | BLOCKED | ABSENT everywhere; convergence plan §1.3 IN-LANE (clipped) + packet §2.3 | R3 fold root — absent-target rule holds; never invented |
| 3 | Kettering pair (`KETTERING-NIGHT` + `-BROKEN-ARROW`) | LEFT | convergence plan §2.2 IN-LANE (clipped); packet §4.1 | R4/master fold OWED — never landed in backwards-audit |
| 4 | APEX docs (`APEX-OF-APEXES` + `APEX-FOLD`) | LEFT | convergence plan §2.2 IN-LANE (clipped); packet §4.1 | R4/master fold OWED — apex residue not yet in backwards-audit |
| 5 | CROSSING series (…SYNTHESIS last landing) | LEFT | convergence plan §2.2 IN-LANE (clipped); `REFS/BRIEF-CROSSING.md` cited | R4/master fold OWED — synthesis not folded |
| 6 | ADOPTIONS ledger-seam | APPLIED | R2 aggregation; plan §2.2; commits `674634c23c` + restage `2e496c9a4a` | R2 adoption aggregation — aggregated |
| 7 | storm harvest residue (30/31-RED→30/30-GREEN wave; X-3 divergence row; READY enrichment proposals) | LEFT | plan §2.2 crown table (clipped) + packet §4.1; `REFS/CROWN-SLICE.md` staged `2e496c9a4a` | R4/master fold OWED — partially processed, never full treatment |
| 8 | negentropy sweeps' apex residue | LEFT | packet §4.1; plan §1.2 (negentropy Processed 1 row) | R4 — NOT yet in backwards-audit |
| 9 | never-idle 4th seat (avrea-exe hosted pool, per-claim VMs) | LEFT/UNVERIFIED | plan §0 fold-in 3 IN-LANE; packet §4.1 | R5/machine-side — never-idle law unverified end-to-end in fork branches |
| 10 | headroom/motion/guard LEFT — 23:24 100%-disk event | UNVERIFIED | packet §4.1; plan §1.2 (headroom/workspace-guard Partial; F7 disk drain logged) | R5 repair backlog (disk headroom) |
| 11 | quiet classes LEFT — free-tier churn w/o artifact; learning-watch aggregation; C42 override signal | LEFT/UNVERIFIED | packet §4.1 | R4/R5 — named, not folded |
| 12 | web-storm cue `805d5b2598d2` | LEFT | plan §1.2 (Unprocessed, 0 traces) IN-LANE; packet §2.2 | R4 — a cue only; the storm itself is bee6af00a7b2 |
| 13 | night-shift cadence `73b6105a4bb8` | LEFT/UNVERIFIED | packet §2.2/§2.3; plan §1.2 | R5 — fired 13:36, never re-fired; cause subsumed by auth-class |
| 14 | nous-free watch `277944dcce67` | APPLIED (HEALED) | packet §2.2 — 16:28 re-fire SILENT = surface stable | cron-auth class closure (R5) |
| 15 | C42 citation-fidelity probe (4 PASS + 1 CONFABULATION_RISK, fid 0.000) | BLOCKED/UNVERIFIED | packet §2.3; plan §1.2 (C42 Partial) | R5/chair — gate passed against it; post-generation override signal |
| 16 | night-shift ticks (deferred) | LEFT/UNVERIFIED | packet §2.3 — cause subsumed by auth-class finding | R5 |
| 17 | harness family G6/G7/G13 | APPLIED | brief §2 closures; commit `70f53793ec` (SMOKE certifying ride) | R5/machine-side — installed + smoke-certified |
| 18 | cron-auth class (missing auth.json) | APPLIED (healed+verified) | plan §3.1/C4 IN-LANE — auth.json regen 16:11; crons re-fired (machine-side; no lane commit) | R5 closure |
| 19 | master synopsis fold (FINAL5→FINAL8 row + FINAL8 ask citation) | OWED | `FINAL5-8-FOLD-20261114.md` §4.1 IN-LANE | R3/R4 — machine-side hand |
| 20 | door-state refresh (#141876; P4; holding comment 6787192097) | OWED | `FINAL5-8-FOLD-20261114.md` §2C/§4.3 IN-LANE | R3 — machine-side hand |
| 21 | read-restore decision (R1 decision-prep) | LEFT (chair's call) | plan C3 IN-LANE; R1 artifact commit `d5b9d40121` | R1 — chair's call |
| 22 | kindness main-file fix | LEFT (CTO-gated) | plan C3 R5 IN-LANE — named pending, never fired without word | R5/chair |

No row dies silently: BLOCKED (2, 15) carry their reason; LEFT rows carry their owner; UNVERIFIED rows carry the open question.

## 2. THE CLOSURES
- **cron-auth class → healed+verified.** Crons (`nous-free-tier-watch`, `runner-never-idle-cadence`) failed on the missing `auth.json`; the doctor/update regenerated it 16:11; all cron failures pre-date it; crons re-fired; the nous-free watch's 16:28 re-fire returned SILENT = surface stable. Machine-side (plan C4; **no lane commit** — the regen is the head's run).
- **FINAL5-8 chain → R3 folded.** `FINAL5-8-FOLD-20261114.md` landed (longcat); FINAL8 read IN-LANE before citing; FINAL6 named ABSENT. Commit `70f6e5fd8c`.
- **adoption scatter → R2 aggregated.** `ADOPTIONS-AGGREGATE-20261114` landed; full ADOPTIONS + CROWN-SLICE restaged into REFS. Commits `674634c23c` + `2e496c9a4a`.
- **harness family → G6/G7/G13 installed + smoke-certified.** Commit `70f53793ec`.

## 3. THE OPEN CELLS
- **Chair's calls:** the read-restore decision (R1 decision-prep — label trail, both vehicles #11548/#116673, holding comment 6787192097); the kindness main-file fix (CTO-gated, named pending).
- **UNVERIFIED:** the 23:24 100%-disk event's cause; the C42 post-generation override signal (fid 0.000 gate pass vs the CONFABULATION_RISK row).
- **Machine-side OWED:** master synopsis fold; door-state refresh; R5 repair backlog (colibri re-ride, cron verification, disk headroom, 4th-seat claim).

## 4. THE OWED REGISTER (exact run specs for the head's machine-side hand)
1. **Master fold:** insert the FINAL5→FINAL8 chain row (FINAL6 ABSENT/record-only) + the FINAL8 ask citation into the master synopsis; the master must have read FINAL8 before citing (receipt: R3's IN-LANE read, 11-14).
2. **Door-state refresh:** quietly re-verify #141876 (no maintainer triage decision), the label (P4), holding comment 6787192097; update if any moved; no posting.
3. **R5 repair backlog:** colibri re-ride; cron verification rows (`73b6105a4bb8` night-shift; `277944dcce67` nous-free); disk headroom (23:24 100% event); the kindness-patrol workflow fix is a main-branch file → CTO-gated, never fired without word.
4. **C42 probe:** name the post-generation override signal; re-derive fid 0.000 against the 4 PASS + 1 CONFABULATION_RISK rows.
5. **kilo.ai live re-probe** (BORROWED chain 001: nemotron-ultra:free + north-mini-code:free, ~200 req/h/IP, 45s/IP pacing).
6. **Page-pull list:** fetch llms.txt/llms-full.txt/README via the docs site; cite the URL; then the adoption rows ground.
7. **4th seat:** claim/verify the avrea-exe hosted pool (per-claim VMs) per the convergence plan's seat-hunt mechanics.
8. **R4 launch package:** brief path + seat + logdir; probe at fire.

## 5. LOOP-STATE
`CONTINUE + R5 (repair backlog, machine-side — the head's)`
(NO NEXT-LAUNCH block — R5 is machine-side; the head holds it.)