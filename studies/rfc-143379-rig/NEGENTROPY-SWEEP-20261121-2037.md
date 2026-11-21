# NEGENTROPY-SWEEP-20261121-2037 — the recurring sweep

**Seat:** the recurring negentropy-sweep lane (cadence 2h, no_agent arm) · **Branch:** `study/rfc-143379-rig-20261105` · **Fire time:** 2026-11-21T20:37 · **HEAD:** `bf59cf19ae` (merge #14; base `cf2f0554bb`)
**The gate (verbatim):** "the gate: nothing public without the user's word."
**Register:** receipts, never claims. **[1st]** = re-read by this lane this pass (git-tree / log / grep at HEAD); **[2nd]** = carried from a study doc; unreceived fact = **ABSENT + named**. Tags: `IN-LANE` / `BORROWED <source>` / `HEAD-RECON`.

## 1 · THE WINDOW-CHECK (the gate)

| # | Standing item | State this pass | Receipt |
|---|---|---|---|
| W-A | **W2-isolation settle-condition** — flip `SEPARATION-UNMEASURED` → `MEASURED`/`REFUTED` | **NOT-RUN.** Run-design verdict-line still `SEPARATION-UNMEASURED` (empty counts 2/5/4, pin `c54c1bc614`). The 11-10 cycle docs (`CYCLES/F4-SEPARATION-MEASUREMENT-PATH-20261110.md`, `CYCLES/W2-RE-RUN-BRIEF-20261110.md`) exist; their verdict-lines were **gated this pass — ABSENT + named**. | `IN-LANE git ls-tree`; `BORROWED APEX-OF-APEXES-20261107` row-1 |
| W-B | **k-term two-tier re-measure** (baseline kept-rates 0.42/0.29/0.26/0.32, span 0.26–0.42, flat) | **PARTIAL.** Two-tier surface exists (`§4`: W2-empty suppressed 0.00 ×6; non-suppressed anchors 0.75 ×10) but is **internally inconsistent** — `§3` lists the same W2-suppressed continuation probes at **0.29**, `§4` at **0.00**. No fresh re-measure landed. | `IN-LANE NEGENTROPY-SWEEP-B-KTERM-20261106 §3/§4`; `BORROWED AUDIT-OPERATOR-COMMENT-20261106` I-3/I-5 |
| W-C | **budget consolidation re-verify** (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | **RECEIPTED, not re-verified.** Weights trace to `NEGENTROPY-SWEEP-C-BUDGET-20261106` (E-3 loss-geometry); the landed gist repeats them. No independent re-derivation this pass. | `IN-LANE git grep '2.83\|3.00'`; `BORROWED KIT-INNOVATION-20261107` |

## 2 · THE SEAM-SCAN (every fire, window or no)

| Seam | Current state | Receipt |
|---|---|---|
| read-burn harness-deadline | Drift fixed at the ledger (`COMMIT-BANK-PIN-20261121` §3: 2,940 commits, max-run 99); fold §6 row-1 auto-continue still names the harness enforcement | `IN-LANE` log `a1b98e9b2f`; `BORROWED` fold §6 |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | **Unrowed.** No fold-check artifact on the branch; the arming's "kit-bench-runner write-gate coverage check" likewise unrowed | `IN-LANE git ls-tree`; `BORROWED` arming |
| token watcher's single-source line | **Stale.** `NEGENTROPY-LOOP-20261119-v2` names `receipts/loop-state-negentropy.jsonl`; its loop-state "next" is the 11-19 fire's hold-audit — two days cold | `IN-LANE` arming record |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | **ABSENT + named** — no receipt this pass | `IN-LANE` |
| dispositions | **AUTO-CONTINUE:** W-C re-verify; the sentinel cleanse. **HOLD-SAFE:** W-A (needs the eval-window); the gist's voice-check door. **NEEDS-THE-CHAIR:** nothing public (gist posting); pilot start | `IN-LANE` |

## 3 · THE ENTROPY CLASSES (CTO freedom applies)

- **Dead surface — `PROBE-SPLIT-PROPOSAL-20261121.md` (6,631 B), re-cut from the 8,085-B `SPLIT-PROPOSAL-DRAFT-20261121.md`.** Two proposals for one split, neither rowed. *Countermove:* supplant draft with proposal (or delete both) and row the split.
- **Loose thread — k-term §3/§4 inconsistency (0.29 vs 0.00).** Audit flagged the "0.75 vs 0.00" inversion; the file carries both. *Countermove:* one tier-set surface, one number per probe.
- **Loose thread — LOSS-LADDER depth-math prose (25/32.5/40% vs code's 50/65/80%).** Audit names a required doc-fix; unrowed. *Countermove:* correct the doc, then promote.
- **Orphan sentinels — `W2-ISOLATION-STATUS-20261106.md.sentinel`, `W2-ISOLATION-RUN-DESIGN-20261107.md.sentinel`.** *Countermove:* clear or row.
- **Friction — the six-pager's voice-check door absent from §5** (audit's single named omission; fold §7-s(6) names it). Committed-not-posted satisfies the gate's letter; the door's absence is its spirit. *Countermove:* present the door with reversibility + who walks it.
- **UNSPOKEN — the branch carries production merges.** HEAD `bf59cf19ae` = #14, second parent `8b26420885` (openclaw-gateway PR); base `cf2f0554bb` = #13, second parent `d6721aaac6` (copycat refactor). The "study-only" branch is a merge target for production. *Countermove:* name the tracking intent (fork-of-record vs study-silo).
- **Storm-corroboration (class, not adoption):** fold checks = **SELD-class read-side evidence-plane verifier**; commit discipline = **AskALCF-class evidence-gated admission**; stub→real ladder = **CoMem-class fidelity ladder** (L1 bounds, L2 certifies); three dispositions = **three-state delegation**; the stale 11-19 token = **validity decay**.

## 4 · THE ORDERED NEXT-MOVES

1. **Re-measure the k-term two tiers into one surface** (resolve §3 0.29 vs §4 0.00). Gate: one number per probe. Seat: k-seam.
2. **Read + flip the W2-isolation settle-condition** (`W2-ISOLATION-STATUS-20261106.md` + `CYCLES/F4-…-20261110`). Gate: `SEPARATION-UNMEASURED` → `MEASURED`/`REFUTED`. Seat: W2.
3. **Re-verify the budget consolidation against the landed gist.** Gate: gist budget lines == `NEGENTROPY-SWEEP-C-BUDGET-20261106`. Seat: budget.
4. **Row the voice-check door into the gist §5.** Gate: door presented with reversibility + who-walks-it. Seat: the master.
5. **Land `LOSS-LADDER-REAL-20261121`** (named stub→real ladder). Gate: matrix reproduces shape-wise + `cost_total` recorded. Seat: ACES.
6. **Fix the LOSS-LADDER landing doc's depth-math prose.** Gate: doc fractions == code (50/65/80). Seat: ACES.
7. **Supplant the stale token-watcher single source.** Gate: token's file names the current fire. Seat: Nemo.
8. **Clear the two `.sentinel` orphans.** Gate: no sentinel orphans. Seat: infra.

## 5 · THE COMPOSE-CHECK + RECEIPT STAMPS (eight steps, HEAD-RECON from the mission spine)

1. Read the ground — `IN-LANE`: log/ls-tree/grep at `bf59cf19ae`; the 11-18-1836 delta baseline.
2. Form the adjudication — `IN-LANE`: §1 states, §3 findings.
3. Name every finding with its countermove — `IN-LANE`: §3, each bulleted *Countermove*.
4. Receipt every claim — `IN-LANE`: [1st]/[2nd]/BORROWED tags throughout.
5. Order the next-moves with gates — `IN-LANE`: §4, eight moves, each gated.
6. State the loop-state — `IN-LANE`: §6.
7. Write the artifact — this file, `NEGENTROPY-SWEEP-20261121-2037.md`.
8. Commit + push — terminal, git-only, before exit.

## 6 · THE LOOP-STATE LINE

**CONTINUE + re-measure the k-term two tiers into one surface (next-move 1).** Receipt: `IN-LANE NEGENTROPY-SWEEP-B-KTERM-20261106 §3/§4`; flip condition = next-move 1's gate.
