# COMPENSATION-RETIRE — 2026-11-14 (SB2 · longcat · hardened harness)

**Ring:** SB2 READ-GAP COMPENSATION RETIRES (`NIGHTSHIFT-PLAN-20261114.md` §1b) · **Mechanism:** read-gap claim → compensation ON⇄read ON; fabrication rate → 0 · **Gate:** rows collapsed into the read's return · **Loop-state:** `CONTINUE + SB3 (chain re-anchor + master fold)` · NO NEXT-LAUNCH
**Steer:** STEER-1 acknowledged — `drop/` outside read roots, no `drop/` read claimed, refs in `REFS/`, mismatch in §5. Kenari READ-ONLY; RFC QUIET; nothing public without the operator's word.

---

## 1. THE COMPENSATION MAP (as recorded)

**Gauge:** 106 commits / 6,275 lines (3,541+2,734) since `56ee8a5cc6` (2026-02-19, 14-line deletion removing the memory `read` action) — `READ-RESTORE-DECISION-PREP-20261114.md` §1, IN-LANE 2026-11-14. Main answers "Unknown action 'read'" (jfugalde 10-24). Scale (BORROWED FINAL8 via `FINAL5-8-FOLD-20261114.md` §1): >100× at full-history drift (~17,240 of ~40,094; ~1,460 person-weeks).

**Known debt — five echo-sites (~30-line core):** `tools/memory_tool_store.py` :322 `_failure_with_entries` · :124 `closest_entries` · :481/:488 replaced-entry fields · :328–:336 batch-abort echo; plus `tools/memory_tool.py` :157 `_validate_single_op`. A ~12-line `MemoryStore.read` (#141876 @ :369) pays for them. The five are the KNOWN sites; the remaining ~6,245 lines are uncatalogued at this depth — ABSENT, named, not invented (§5).

**Compensation classes (as briefed):** **read-replacements** — the five echo-sites (entries handed back via failure paths, closest-match stand-ins, replaced-entry fields, batch-abort echo, single-op validation); **fabrications-guards** — guards holding the recorded class (6/6 fabrications without the read, reproduced ×2); **abstention sentence** — "a system that cannot read should say so, never guess" → 12/12 clean refusals.

**Doors/vehicles/hold (as recorded; SB1's receipt carries the full spine):** #141876 HEAD `af16e3ab16`, OPEN/unmerged, head returns entries + usage first try (jfugalde, HEAD-RECON) — FIX NOT MISSING, UN-MERGED; #11548 dispatch bootstrap @ `d3a6e577`; #116673 bounded read + doc chain @ `60a2e15638` (merged=false, mergeability pending). Hold 6787192097: holding for #141876; alternatives-with-community if it does not land soon. Label P4 (six moves, no substance change; P2 at birth); no maintainer triage decision. Scope: SEVEN dropped-value tickets NOT the read (#99957 #105243 #49195 #105248 #140935 #110126 #50132); THREE lifecycle tickets the read serves (#116673, #135039, #69264).

**Receipts:** R1 prep + FINAL5-8 fold + SB1 receipt (`SUBSTRATE-READ-RECEIPT-20261114.md`) + plan §1b/§1c — IN-LANE, stamped 2026-11-14.

---

## 2. THE RETIREMENT DESIGN (when the read lands)

**The absorber:** #141876's 12-line `MemoryStore.read` (:369) returns entries + usage directly; any row whose only function is handing entries back despite the missing read is functionally absorbed once the read returns cleanly.

**COLLAPSE INTO THE READ —** the read-replacement core: the five echo-sites' handback function. The read makes their purpose redundant; the fabrication class collapses with them (battery A: 6/6 → 0). Per ENRICH-1 check E, #141876 as scoped does NOT delete them: "whether each then deletes or stays as defensive UX is the dive the owning work must do."

**REMAIN AS DEFENSIVE UX (named; deferred) —** the five echo-sites stay untouched by the landing PR until the owning work's per-site dive decides delete-vs-keep (fail-safe if the read is ever absent again); the abstention sentence stays as the standing behavior floor (inert-but-harmless with the read; the reversible floor under a future read-gap); the fabrications-guards stay until a re-probe holds 6/6 at 0 without them — HOLD-SAFE, never a preemptive delete.

**BECOME THE READ'S ACCEPTANCE BATTERY INPUTS** (`ENRICH-1-MERGE-READINESS-20261114.md` §1; scratch store, machine-side, OWED): **A** 6/6 fabrication repro red→green · **B** 12/12 clean-refusal repro · **C** head-returns-entries (entries + usage, first try) · **D** schema-safe edge — #116673 bounded read @ `60a2e15638`, anchored MEMORY.md doc chain, bounded scope, no body rewrite · **E** non-regression — write-then-read 200/200, concurrency 800/800, idempotence 100/100, over-budget 20/20, over-budget reroute-to-chain-doc seam, identical head-vs-main. Totals: 12 steps (6 red→green + 6 green), ~50 min.

**Sequence (safest-first):** (1) battery first — A/B/C green before anything retires; red stays 6/6 at the wound; (2) freeze baseline E; (3) land the read, keep all compensation as-is (matches #141876's scope + the caveat); (4) owning-work dive per site, delete-or-defensive-UX, individually justified; (5) re-probe A after any deletion — evidence gap → HOLD-SAFE.

**Two-way doors:** the read is a 12-line revertible addition, battery its probe; each deletion reversible from receipted history, ships only after E-green; guards/sentence retention reversible at the owning work's word. Nothing public at any step — the standing law (nothing internal is gated) gates every crossing.

**Seam register (owning work decides; named, never decided here):** (1) the four-site question (+ fifth echo): delete or defensive UX — #141876 does not settle it; (2) guards' retirement trigger + owner; (3) abstention sentence's standing + owner; (4) collapse shape — cleanup folded into #141876 vs separate post-battery PR; (5) the ~6,245-line remainder catalogue (read-gap rows vs unrelated drift); (6) boundary — the seven dropped-value tickets are not read-gap rows; #116673 rides the battery (D); #135039/#69264 stay outside the restore's scope.

---

## 3. THE METER (what proves it worked)

- **Fabrication rate:** 6/6 (red path, ×2) → **0 on the green path** — battery A on #141876's head; re-probe after each deletion.
- **Line-count delta:** 6,275 / 106 commits → **the kept set** — echo-core function absorbed by the 12-line read; kept = five sites + guards + sentence pending the dive; delta reported per site; the ~6,245 remainder is an evidence gap.
- **Non-regression:** main's ops pass-rates → **identical on head** — battery E (200/200 · 800/800 · 100/100 · 20/20 · seam); any baseline change = regression.

Hard gate: a retirement that moves any baseline rate is a regression, and the collapse reverses.

---

## 4. FAIL-SAFE / DISPOSITIONS (plan §1c)

AUTO-CONTINUE: adopt the collapse-into-read design, battery-input mapping, safest-first sequence. PARK: physical deletions + guards' retirement (the owning-work dive + re-probe are prerequisites). HOLD-SAFE on aggregated rows; NEEDS-THE-CHAIR packet pre-written per the plan.

---

## 5. OWED REGISTER (stamped; machine-side, never faked)

1. **Battery A–E** — OWED to the head/chair's hand (ENRICH-1 §5); this lane composes, never runs.
2. **Remote PR states** (#141876/#11548/#116673) — R1 §4 spec: `gh pr view 141876 --json state,mergeable,commits --repo hermes-agent`; repeats next round.
3. **`drop/` mismatch** — STEER-1; outside read roots; no read claimed; refs in `REFS/`.
4. **Per-site line counts + the ~6,245-line catalogue** — not in receipts; ABSENT stays named.
5. **Local reads** — IN-LANE (branch `study/rfc-143379-rig-20261105`); tags IN-LANE / BORROWED / HEAD-RECON.

---

## 6. LOOP-STATE

`CONTINUE + SB3 (chain re-anchor + master fold)` — SB3: MEMORY-CHAIN append + re-anchor; correction lands → append⇄re-anchor; corrections counted; seat longcat⇄solar rotate; artifact `CHAIN-REANCHOR-LOG-20261114.md`; gate: old head readable, re-head logged. NO NEXT-LAUNCH — the head dispatches.