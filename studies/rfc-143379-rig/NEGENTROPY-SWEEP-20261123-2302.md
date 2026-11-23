# NEGENTROPY-SWEEP-20261123-2302

**seat:** the recurring negentropy-sweep lane (the scheduled sweep's harness ride · cadence 2h · no_agent arm)
**branch:** `study/rfc-143379-rig-20261105`
**fire:** 2026-11-23 23:02 **UTC** (zone stated per §3-F3 · the stamp is the artifact name)
**gate, verbatim:** "the gate: nothing public without the user's word." — artifacts only; the RFC upstream stays QUIET; nothing posts.
**VERDICT:** HOLD-WITH-NAMED-SEAMS — the wiring survives the mission set except where a human/probe is named below.

## THE REGISTER (binding)
- **[1st]** re-read by this lane this pass: `NEGENTROPY-SWEEP-20261123-2101.md` (full, the delta baseline); `NEGENTROPY-SWEEP-20261119-2214.md` (full, the format precedent + the eight compose-check steps); `NEGENTROPY-ARM-EXECUTE-20261119.md` + `-brief.md` (full); `NEGENTROPY-SWEEP-RECURRING-brief.md`; the master brief's fold tail (§7-ci `e87b2994`, §7-cj `feca68112d`/`91767a63`); `git log --oneline -30`; the tree listing of `studies/rfc-143379-rig/` (**1122** immediate children — a full product-repo mirror) and of `…/studies/rfc-143379-rig/` (**666** tracked files — the nested self-copy); `git merge-base --is-ancestor` on `67fef5d710` and `256c9c296b` (both rc=0).
- **[2nd]** carried, not re-derived: the windowed measurements (kept-rates 0.42/0.29/0.26/0.26; consolidation 3.00/2.83/2.33/2.00), the STEER lineage, the fold-check wiring, the hold-audit verdict.
- **ABSENT + named:** no W2-isolation run record; no k-term re-measure artifact; no budget re-verify; no machine-layer liveness row (head-executed per the ARM boundary); the Arm D scaffold's current tree state (dirty at 2214, not re-derived here); a full sorted enumeration of the sweep series (the read-gate closed before it could prove 2101 is the last fire).
- Tags: `IN-LANE` · `BORROWED <source>` · `HEAD-RECON`.
- Storm-context, class-corroboration only: validity decay + stage-decoupled evaluation (§1, §3-U1), MemCredit's ρ=(V−λH)/b as the keep-rate proxy (§1), SELD's read-side evidence-plane verifier as the fold's class (§2), DISCERN's write-gate L0 (the gate), AskALCF's commit gate (next-moves 2–4).

## 1 · THE WINDOW-CHECK (the gate)

| item | state | receipt |
|---|---|---|
| **W2-isolation settle-condition** (clean unmeasured/only-litmus window · continuous telemetry · settle held until validated) | **NOT-RUN** — still unrun; the newest sweep artifact carries the same NOT-RUN row and no run record exists in-plane. | `BORROWED …2101 §1; …2214 §1` |
| **k-term two-tier re-measure** (baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat) | **NOT-RUN.** The flat span still contradicts the budget's class ordering, which presupposes differential keep-rates. The candidate mechanism (`probes/battery_luna.py`, ABSTAIN/ANSWERED at the slot) is **ABSENT this pass** (tree state not re-derived). Keep-rate ≈ ρ's V-term proxy (MemCredit). | `BORROWED …2214 §1` + `ABSENT` |
| **budget consolidation re-verify** (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | **CHECKED as carried [2nd]** — figures unchanged; no fresh re-measure exists; the SCOPE-lane freshness audit stays misrouted (ABSENT). | `BORROWED …2214 §1` |

Windowed-class verdict: both measurement gates remain unrun while content legs keep landing — **validity decay is the live risk**; see §3-U1.

## 2 · THE SEAM-SCAN (every fire, window or no)

| seam | current state | receipt |
|---|---|---|
| **read-burn harness-deadline seam** | **ACTIVE — felt this pass.** Mid-analysis the read-tools returned `READ-GATED: the write-window is open`; the terminal's content-reads blocked. The standing seam, same class as 2214. | `IN-LANE` |
| **fold checks** (scribe cell → get_memory byte-compare; served `?raw=1` grep) | **WIRED, not re-run in-lane.** Machine-side folds are landing: the master brief carries blob-verified rows §7-ci `e87b2994`, §7-cj `feca68112d`/`91767a63`. Class: SELD's read-side evidence-plane verifier. | `IN-LANE` (master tail) + `BORROWED …ARM §4` |
| **token watcher's single-source line** | **STALE [1st] — four days on.** The declared single source `NEGENTROPY-ARM-EXECUTE-20261119.md` still reads `UPDATED 2026-11-19 ~21:xx EST` — the placeholder never landed — and names STEER-3 while the channel has moved through STEER-11 to the §7-cj flagship rows. | `IN-LANE` (arm §1 line 6) |
| **machine-layer wire-checks** (scribe tunnel, runners, Harbor/local-LM) | **ABSENT + named** — no tracked rows this pass; SSH/tunnel/liveness are head-executed per the ARM boundary; a lane never fabricates a run it cannot perform. | `ABSENT` |
| **dispositions** | **AUTO-CONTINUE** folds + the improvement-loop arc (closed 3/3) · **HOLD-SAFE** the window probes + the stale token · **NEEDS-THE-CHAIR** the mirror-plane freeze + baseline/index receipting. | `IN-LANE` |

## 3 · THE ENTROPY CLASSES (CTO freedom applies)

**Dead surface.**
- **D1 · the nested self-mirror.** `studies/rfc-143379-rig/studies/rfc-143379-rig/` holds **666 tracked files** — a frozen second-level copy of the study plane whose newest sweep is `20261115-1724`, eight days behind the outer plane; and the outer plane itself mirrors the product repo (**1122** entries: pyproject.toml, uv.lock, tests/, web/, website/). *Countermove:* stamp `MIRROR-FROZEN-<date>` at the nested root (or quarantine it) so no lane reads frozen bytes as live, and receipt the freeze date.

**Loose threads.**
- **L1 · the incomplete prior artifact.** `NEGENTROPY-SWEEP-20261123-2101.md` ends "Sections 3–6 land in the next write" — never completed; this fire supplies the missing core classes. Its sibling `…-20261123-1056.md` uses bracket placeholders (superseded format). *Countermove:* a one-line superseding pointer in 2101's header to this artifact; leave 1056 as archive.
- **L2 · the template's loss event.** The recurring template records it lived untracked in scratch and was lost, rebuilt 11-19; the branch copy is now the only source. *Countermove:* keep the branch copy authoritative; never dual-home.
- **L3 · orphan sentinels.** None receivable this pass (no watcher PID/process rows in the ground read). **ABSENT + named** — not silently passed.

**Friction points.**
- **F1 · receipt drift.** The 2101 header stamps branch `hermes-agent-registry/crowns-dispatch-rig` while the live branch is `study/rfc-143379-rig-20261105`. *Countermove:* stamp the live HEAD SHA + branch at fire time.
- **F2 · read-gate friction** (above): the deadline burned the read phase again; the sweep's ground shrinks each fire.
- **F3 · zone labels.** Fire stamps read UTC while older labels say EST (2214-U2) — the token cannot be ordered monotonically. *Countermove:* every `UPDATED` line carries an explicit zone; this header does.

**UNSPOKEN things.**
- **U1 · the priority inversion, sharpened (the prize).** Content legs keep landing — the improvement loop closed 3/3, the flagship response+plan landed §7-cj — while BOTH standing measurement gates sit unrun and the Arm D re-measure mechanism is uncommitted/unreceived. The loop produces deliverable-mass faster than it resolves its own falsifiability; the k-term's flat kept-rates leave the budget's class ordering **unfalsifiable**, and no corpus doc says so. *Countermove:* the next-mission gate either RUNS both probes or RETIRES them with a recorded reason; if run, Arm D's ABSTAIN/ANSWERED split is the protocol.
- **U2 · the sweep's own baseline is unreceipted.** The read-gate closed before the sweep series could be enumerated, so the delta baseline rests on the newest artifact received in this pass's tree listing. *Countermove:* record the sweep index (fire N of M) in every artifact header so deltas are receipted, never assumed.
- **U3 · the silent upstream.** Still zero external output; the gate held. *Countermove:* keep the gate verbatim in each header; name the publish friction when a lane would post.

## 4 · THE ORDERED NEXT-MOVES
1. **Append the token line with a zone** — `UPDATED 2026-11-23 23:02 UTC · <live stage> · <owner>`. Gate: the file's own append-only rule. Seat: head. Auto-path: append, never rewrite.
2. **Commit-or-revert the Arm D scaffold** (with any registry-dirty limb, same element arc). Gate: the fold's byte-identity. Seat: head.
3. **Run-or-retire W2-isolation.** Gate: clean window + continuous telemetry. Seat: head/Nemo. Retired ⇒ a recorded-reason row.
4. **Run-or-retire the k-term two-tier re-measure** (Arm D protocol). Gate: the two-tier protocol. Seat: head.
5. **Freeze-stamp the nested mirror plane** (`MIRROR-FROZEN-<date>`) + point 2101's header at this artifact. Gate: receipt discipline. Seat: head.
6. **Record the sweep index (fire N/M)** in every header. Gate: monotonic token orderability. Seat: head.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS
1. **Delta vs baseline** — baseline …2101; deltas: read-gate felt live, nested-mirror counted (666/1122), token placeholder confirmed unfilled, priority inversion sharpened. Evidence: §1–§3.
2. **Register honored** — [1st]/[2nd]/ABSENT separated; no silent pass. Evidence: the register block.
3. **No ABSENT invented** — the rates are carried [2nd], not re-measured; the Arm D tree state and the liveness rows are named ABSENT. Evidence: register + §1–§2.
4. **The gate held** — nothing posted; the RFC upstream untouched; artifacts only. Evidence: header gate line.
5. **CTO freedom applied** — the unexpected finding (U1) is reported, not censored. Evidence: §3-U1.
6. **Every finding has its countermove** — D1 / L1–L3 / F1–F3 / U1–U3 each carry one. Evidence: §3.
7. **Loop-state receipted** — CONTINUE + the exact next move. Evidence: §6.
8. **Shape/size** — one artifact, six sections, ≤6,000 chars per write. Evidence: this file.

## 6 · THE LOOP-STATE LINE
`CONTINUE + next move #1: append the arm's UPDATED line with an explicit zone (23:02 UTC), lifting the four-day placeholder defect; then #5 freeze-stamp the nested mirror plane.`
Receipt: `IN-LANE` (arm §1 line 6 + this fire's tree counts) · `BORROWED NEGENTROPY-SWEEP-20261119-2214 §6`.