# NEGENTROPY-SWEEP-20261123-0453 — the recurring sweep (copycat lane, RFC #143379 apex)

**Seat:** the recurring negentropy-sweep lane (copycat lane) · **Branch:** `study/rfc-143379-rig-20261105` · **Fire time:** 2026-11-23 ~04:53 · **The gate (verbatim):** "the gate: nothing public without the user's word." · **Register:** receipts, never claims; [1st] = re-read by this lane this pass (git-tree / HEAD / log), [2nd] = carried from a study doc; ABSENT + named = never invented. RFC #143379 upstream QUIET.

## 1 · THE WINDOW-CHECK (the gate)
| # | Item | State this fire | Receipt |
|---|---|---|---|
| W2 | W2-isolation settle-condition | **ANSWERED-PARTIAL** — refire #5 landed: fresh window 14/20 HTTP 200 + 6/20 429 (upstream-capacity, retry-after 30 rolling); 13 null-200 reasoning-exhaustion + 1 incorrect truncated fact prefix; correct=false, f1=f2=f3b=1; verdict UNKNOWN per the dry-run ruler; door twice-verified. The settle-condition is DISCHARGED (partial), not pending. | [1st] commit `63be1db046` + `2c43477992` (log, this fire); [2nd] 0051/0252 |
| K | k-term two-tier re-measure | **NOT-RUN** — no artifact. Baseline contradiction stands: kept-rates 0.42/0.29/0.26/0.26 (span 0.26–0.42, flat) vs the budget's differential-keep-rate presupposition. | [2nd] 0051/0252; [1st] no new artifact in the HEAD tree |
| B | budget consolidation re-verify | **NOT-RUN** — no artifact. Ordering stands: decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00. | [2nd] 0051/0252 |

## 2 · THE SEAM-SCAN (every fire)
| Seam | Current state | Receipt |
|---|---|---|
| read-burn harness-deadline | The harness's 120-char error capture hid the `retry-after` header; refire #3's observation-only transport logger surfaced it (384→371s, fixed reset epoch ≈13:29:35Z). Refire #5: 14/20 200 + 6/20 429. Seam CLOSED by instrumentation; the seat's fair-share/capacity wall is the live blocker. | [1st] WEIGHTS-RUNG-BATTERY-REFIRE §3.2; [2nd] 0051 |
| fold checks (scribe cell → get_memory byte-compare; `?raw=1` grep) | Byte-identical=True observed on every landed lane per the arming; but the 0051 lane found its OWN artifact's scribe cell absent (write-without-cell protocol regression). | [1st] ARM-EXECUTE §2; [2nd] 0051 |
| token watcher's single-source line | Token name `NEGENTROPY-LOOP-20261119-v2`; the ARM-EXECUTE file names ITSELF the single source. The file `NEGENTROPY-LOOP-20261122` is ABSENT/phantom (in no branch file). | [1st] ARM-EXECUTE §1 + git grep; [2nd] 1848 |
| machine-layer wire-checks | Carried, 4-day-stale: scribe tunnel :24282 REACHABLE; Harbor :44831 LIVE; SSH 192.168.1.241 REACHABLE (disk 29%). Not re-run (terminal git-only). | [2nd] ARM-EXECUTE §4 (2026-11-19) |
| dispositions | AUTO-CONTINUE: probe / bench door / governance / calendar re-surveys / fold+scribe+rows. NEEDS-THE-CHAIR: the fire's READY verdict; any public move; the RFC upstream's quiet. | [1st] ARM-EXECUTE §5/§6 |

## 3 · THE ENTROPY CLASSES (CTO freedom)
- **Dead surface:** the nested duplicate tree `studies/rfc-143379-rig/studies/rfc-143379-rig/` (34 stale sweep artifacts) — never read as ground. Countermove: archive-or-flatten; never read.
- **Loose threads:**
  - (a) `NEGENTROPY-SWEEP-20261123-0252.md` — UNTRACKED (unrowed landing; a sweep artifact never committed). Countermove: the fold rows it; never silently carried.
  - (b) `plan/tank/RECIPE-RETRY-20261122.md` — UNTRACKED. Countermove: same.
  - (c) `SCRIBE-WITNESS-REGISTRY.log` — MODIFIED, uncommitted fold drift. Countermove: the fold rows it.
  - (d) Branch divergence: local HEAD `f652b71b4e` ≠ origin `4b6636c6f2` (ls-remote truth); tracking ref stale at `857268bec3`. The lane never pushes; the fold carries. Countermove: name it; the fold pushes at the all-clear.
  - (e) Stale-headline thread: fires #4/#5 appended to the battery record while H1 said fire #3. The refire #5 close commit (`2c43477992`) may have fixed it. Countermove: re-verify H1 at the next read.
  - (f) Phantom token name `NEGENTROPY-LOOP-20261122` in the brief text. Countermove: stamp the token name from the watcher's output, not the brief.
- **Friction points:** the seat's 429 fair-share/capacity wall blocks the settlement; the 2h cadence vs the 4-day-stale wire-checks; the harness's 120-char truncation (now instrumented).
- **UNSPOKEN (the prize):** the sweep is a lane whose own landings are fragile — 0252 untracked, 0051 landed but its scribe cell absent. The dead-surface it sweeps is, in part, itself. And the loop-state token's "single source" is a file that is itself only local until the fold pushes — the token's publication IS the fold's push. Countermove: land this artifact + commit; the fold's push is the token's true publication.

## 4 · THE ORDERED NEXT-MOVES
1. Land this artifact + commit (the lane's final step). Gate: the branch. Seat: the lane.
2. The fold: row the untracked 0252 sweep + RECIPE-RETRY + the registry drift; push `f652b71b4e` → origin. Gate: the branch. Seat: the fold.
3. Re-verify the battery record's H1 after refire #5. Gate: the branch. Seat: the next sweep.
4. Land or strike the absent token file. Gate: the branch. Seat: the head/arm.
5. Re-run the k-term two-tier + budget consolidation when a lane with the budget artifacts fires. Gate: the artifact. Seat: the budget lane.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
- deconstruct: FIRED — window-check + seam-scan + entropy classes, each receipted.
- sense: FIRED — delta baseline (0051 committed + 0252 untracked) + ARM record + refire battery.
- choose: FIRED — W2 pending→answered-partial; k-term/budget stay NOT-RUN.
- calibrate: FIRED — ls-remote truth (origin `4b6636c6f2`) vs local HEAD (`f652b71b4e`); no estimate.
- probe: FIRED — git log grep for the refire #5 close; the token grep.
- review: FIRED — the unexpected finding named (the sweep's own landing fragility).
- record: FIRED — this artifact.
- compose-check: FIRED — the loop-state line below.

## 6 · THE LOOP-STATE LINE
`CONTINUE + the fold rows the untracked 0252 sweep + RECIPE-RETRY + the registry drift and pushes f652b71b4e → origin; the next sweep re-verifies the battery H1 after refire #5.` Receipt: [1st] git status/ls-remote/log this fire; [2nd] 0051/0252.

STORM-CONTEXT corroboration (class, not adoption): this sweep is the read-side evidence-plane verifier (SELD class); the gate is the write-gate L0 (DISCERN); the 4-day-stale wire-checks are validity-decay (misc); the window-check vs the fold's push is stage-decoupled evaluation (misc).