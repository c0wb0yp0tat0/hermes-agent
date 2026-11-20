# NEGENTROPY-SWEEP-20261120-0417 — the recurring sweep (cadence 2h, no_agent arm)

**SEAT** copycat lane (negentropy-sweep) · **BRANCH** study/rfc-143379-rig-20261105 · **FIRE** 2026-11-20 04:17 (zone unresolved, U2 carried) · **THE GATE (verbatim): "the gate: nothing public without the user's word."** — artifacts only; the RFC upstream stays QUIET; nothing posts.

## THE REGISTER (binding)
- **[1st]** re-read this pass: `git rev-parse HEAD`=976a93ee95; `git rev-parse origin/study/rfc-143379-rig-20261105`=206324e7c5; `git status --porcelain` = one tracked modified `SCRIBE-WITNESS-REGISTRY.log`; `git log --oneline -15` (top: 976a93ee95 watcher HOLD row → 0be441fadd LEDGER NAMES FINALIZED → a9f77719b3 KIND REFRESH → 7fb037b018 FLEET-CYCLE-BODY-20261120T004648Z → b2a1593dfd watcher ~21:3x → 78b94272b9 sweep 0216 → 4ebb1c8584 ELEMENT-VERIFY STEP RESTORED → fe5e87f0b5 OPENCLAW deck → 5e488fec14 OPENCLAW-FIELD-CORROBORATION → 5fc47bca51 CONSOLIDATED-HARVEST-INPUT → 81fdd28be2 CTO-FREEDOM-HARVEST); the mission-map on-disk tail (150 lines, ending the ~23:1x row, local==remote 7952f135b3); NEGENTROPY-SWEEP-20261120-0015 (full, paged) + 20261119-2214 (§1/§2/§4); the 0216 sweep's §1–§6 headers + selected lines (git grep); committed probe bytes (TWEAK-BILLED-QWEN4-FREE-20261119, TWEAK-BILLED-HY4-FREE-20261120, NATIVE-RUNG-{QWEN4,HY4}-FREE, MASTER-STAGE3-LEDGER, MASTER-DRY-RUN-LUNA, ARM-D-DESIGN, battery_luna.py + dry-run output).
- **[2nd]** carried: the windowed measurements (kept-rates 0.42/0.29/0.26/0.26 flat; consolidation 3.00 > 2.83 > 2.33 > 2.00); the arm's §1 token line (STEER-3 + the unfilled `~21:xx` placeholder) BORROWED 0015 register; the 0216 sweep's full body (only headers + grep lines received).
- **ABSENT + named:** the 0216 artifact's full text (read-gated mid-analysis); the local-vs-origin ahead/behind count (read-gated); no W2-isolation run record; no k-term re-measure artifact; the served `?raw=1` grep; the scribe-cell → get_memory byte-compare.

## 1 · THE WINDOW-CHECK (the gate) — carried [2nd], none re-run (no_agent arm)
| item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT RUN — no run record on the branch | [2nd] 0015 §1; ABSENT |
| k-term two-tier re-measure (0.42/0.29/0.26/0.26 flat — contradicts the budget's class ordering) | NOT RUN — no re-measure artifact | [2nd] 0015 §1; ABSENT |
| budget consolidation re-verify (3.00>2.83>2.33>2.00) | NOT RUN — carried | [2nd] 0015 §1 |
| Arm D scaffold | COMMITTED — dce95d54d3; battery_luna.py + dry-run output in tree | [1st] git grep + log |
| TWEAK-BILLED-{HY4,QWEN4}-FREE ledgers | COMMITTED — 0be441fadd; both in probes/ | [1st] git grep + log |

## 2 · THE SEAM-SCAN (every fire)
- **read-burn harness-deadline seam — ACTIVE, felt live again.** The write-window opened and the terminal's content-reads gated mid-analysis (the 0216's exact signature); this sweep wrote on the bytes already in hand. [1st] the read-gate notice + the paged 0015/2214 reads.
- **fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep)** — NOT RUN (read-gated). ABSENT + named; the 0216's ACTIVE reading stands as the last receipt.
- **token watcher's single-source line — BROKEN AT THE WIRE (new).** HEAD's own commit subject is a watcher HOLD row reporting `local==remote 0be441fadd`, while the origin-tracking ref reads 206324e7c5 — a sha named by no watcher row. The "single-source" line is not single. [1st] git rev-parse (both) + the log subject. Countermove: the next fold ls-remote-verifies before any "local==remote" claim; HOLD-SAFE.
- **machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM)** — NOT RUN (read-gated; no_agent arm). ABSENT + named.
- **dispositions:** the sweep's receipts AUTO-CONTINUE; the wire divergence HOLD-SAFE (auto-path: the watcher's next fold ls-remote + ancestry-check); the registry commit-or-revert HOLD-SAFE (auto-path: the head's fold — not this lane's file).

## 3 · THE ENTROPY CLASSES (the sweep's core)
- **THE PRIZE — tree-amnesia via the archiver's merge (a9f77719b3 KIND REFRESH).** The sibling's archive merge "took our history but dropped 17K lines from the tree"; the night's landings (element/Luna/Kaizen artifacts, the probe ledgers + dry-runs, the harvest decks, the ARMD scaffold + the element-verify step) were re-landed additively, the archiver's composition untouched. Class: **the branch's tree is not guaranteed by its history** — a merge can amputate bytes and only a re-land restores them; the mission's own thesis (reads never restore) turned on the branch itself. Countermove: the per-fire tree-hash receipt must cover the restored set, not only the new commit; the KIND REFRESH row is the receipt.
- **the wire divergence** — origin-tracking 206324e7c5 ≠ HEAD 976a93ee95; the ahead/behind count ABSENT (read-gated). Class: stale-tip / moved-tip. Countermove: ls-remote + ancestry before push; pull --rebase on rejection.
- **the map-vs-HEAD staleness** — HEAD's map tail ends at the ~23:1x row (local==remote 7952f135b3) while HEAD's own commit subject names 0be441fadd; the map's last row and HEAD's subject disagree on the tip. Class: the map's freshness is asserted, not verified. Countermove: the next watcher fold re-reads map line 35 + plan line 83 verbatim and states the tip sha it actually saw.
- **the registry dirtiness — now the last surviving item of the 0015 D2 pair** (battery_luna.py committed at dce95d54d3). It has now survived the 0216 and 0417 fires. Countermove: the head's fold commits-or-reverts it; not this lane's file.
- **the unrowed-landings thread — PARTLY ROWED.** The 0216's next-move #1 (row OPENCLAW deck / FIELD-CORROBORATION / CONSOLIDATED-HARVEST) is discharged by the ~21:3x watcher row (b2a1593dfd lists all three). But landings since — 7fb037b018 FLEET-CYCLE-BODY, a9f77719b3 KIND REFRESH, 0be441fadd LEDGER NAMES, 4ebb1c8584 ELEMENT-VERIFY RESTORED — are not in the map's tail as read. Countermove: the next watcher fold rows them.
- **loose thread — the arm's §1 token line still carries STEER-3 + the unfilled `~21:xx` placeholder** [2nd] 0015; no receipt of the head's UPDATED append. Countermove: the head appends or the sweep names it ABSENT.
- **UNSPOKEN — the sweep's own read-gate is the seam's best evidence.** The lane that scans for read-burn was itself burned by the deadline this pass; the artifact was written on partial bytes (the 0216 body unread). The class is not the gate's existence but its asymmetry: the sweep can name the seam only by hitting it.

## 4 · THE ORDERED NEXT-MOVES
1. **Row the post-0216 landings** (FLEET-CYCLE-BODY, KIND REFRESH, LEDGER NAMES, ELEMENT-VERIFY RESTORED) — gate: the watcher's per-landing row rule; seat: the nightshift watcher.
2. **Commit-or-revert the registry** — gate: the fold's clean-tree check; seat: the head (not this lane's file).
3. **ls-remote + ancestry-verify the wire divergence** (origin 206324e7c5 vs HEAD 976a93ee95) before any push — gate: the watcher's fold; seat: the watcher.
4. **The three windowed probes** (W2-isolation, k-term re-measure, consolidation re-verify) — gate: the head's fire; seat: the head/pair; no_agent arm cannot run them.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
1. seat/branch/fire/gate — IN-LANE (this header).
2. register — IN-LANE (git rev-parse/status/log) · BORROWED 0015.
3. window-check — [2nd] 0015 §1; ABSENT run records named.
4. seam-scan — IN-LANE (the read-gate felt this pass) · [2nd] 0216 headers.
5. entropy classes — IN-LANE (KIND REFRESH row + the rev-parse pair).
6. next-moves — IN-LANE.
7. loop-state — IN-LANE.
8. no public surface touched — IN-LANE (artifacts only; nothing posted).

## 6 · THE LOOP-STATE LINE
**CONTINUE + next move #1: the watcher rows the post-0216 landings (FLEET-CYCLE-BODY, KIND REFRESH, LEDGER NAMES, ELEMENT-VERIFY RESTORED) and ls-remote-verifies the wire divergence (origin 206324e7c5 vs HEAD 976a93ee95) before any push.** Receipt: IN-LANE (git log --oneline -15 + git rev-parse + git status + the map's tail rows) · BORROWED NEGENTROPY-SWEEP-20261120-0216 §6.