# NEGENTROPY-SWEEP-20261121-0630 — the scheduled sweep's receipt

the gate: nothing public without the user's word

**Seat:** copycat (`stealth/crouton-alpha`) · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Fire:** 2026-11-21 06:30 UTC · **Register:** receipts, never claims · **Hand-separation:** [1st] = re-read by this lane this pass; [2nd] = carried, not re-derived. **Prior sweep:** `NEGENTROPY-SWEEP-20261121-0429.md` (`c0058d5d34`) — the delta baseline. **Head:** local==remote==`5868b595a1` [1st]. **Read-window:** closed at this fire (write-window open) — `PILOT-VERDICT-20261121.md`'s body is **ABSENT from this pass**, carried [2nd] from its commit message (`3f99fda76f`); the bytes I did re-read first-hand are tagged [1st].

## 1. THE WINDOW-CHECK (the gate)

| Item | State | Receipt |
|---|---|---|
| W2-isolation settle-condition | **HOLD-SAFE / NOT CLOSED** | Carried [2nd] from 0429: "close only when 47's outcome lands; no 47 artifact in the tree". The eval-window is still closed — no eval-start receipt on the branch; `W2-ISOLATION-RUN-DESIGN-20261107.md` §6 wall-clause stands [1st, re-read]. Countermove: the closure is gated on the runtime values, not on any fork artifact — name the window's return as the settle trigger. |
| k-term two-tier re-measure | **NOT RUN** | Baseline [2nd] from `ADJUDICATION-NEGENTROPY-20261106.md`: kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42 flat — the budget's class ordering presupposes differential keep-rates; the flat k-term contradicts it. No k-term instrument landed since; the new A3 wave is a *different* battery (`battery_luna`, logit-bias arms) [1st]. Countermove: land the re-measure or strike it with a dated decision. |
| Budget consolidation re-verify | **NOT RUN** | Baseline [2nd] from `NEGENTROPY-SWEEP-C-BUDGET-20261106.md`: decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00. No re-derivation commit since 0429. Countermove: same — land or strike. |

**The label collision (this fire's prize):** the PILOT commit's "W2 separation measured" [2nd, `3f99fda76f`] names the **workflow-presence** separation (`probes/w2-presence-20261121.json`: 31/35 forks carry ≥1 workflow, latest-run conclusions 31 present / 0 absent [1st, re-read]). The window-check's **W2-isolation** is census #20 / budget §(d) W2 — the **empty-answer guard-bypass** [1st, census re-read]. Two markers share the label "W2"; the pilot's closure receipt must not be read as the guard-isolation's. Countermove: rename the workflow-presence marker (W2f / presence-separation) so no wall hides behind a shared label.

## 2. THE SEAM-SCAN (every fire)

| Seam | Current state | Receipt |
|---|---|---|
| Read-burn harness-deadline | **OPEN** (carried) | 0429 read it OPEN; no commit since touches it. The R2 build is **superseded by verification** [2nd, `3f99fda76f`]: the write-window READ-GATE + byte-budget breaker exist and are hard-enforced (`copycat-harness.py:663` READ-GATED, `:537-552` HARNESS_BUDGET_CHARS 2K floor). Countermove: re-classify the seam CLOSED-BY-VERIFICATION or name the residue. |
| Fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | **LIVE** | The byte-compare path is wired (B1-RECEIPT `3edfaadd56`: `READ_SUBSTRATE_MODE=cells` → get_memory → sha256 → paged serve, `source: scribe-cell`, CELL-BYTE-MISMATCH/NO-CELL fallbacks) [2nd, MISSION-MAP]. This fire the A3 floor json shows `reader_calls: 5` per arm with `reader_last_error: null` [1st] — the fold path executed. The served `?raw=1` grep: NOT RE-RUN. |
| Token watcher single-source line | **CONTRADICTED, worsened** | `MISSION-MAP-20261118.md` line 35 still names STAGE-1-fires while the appended watcher rows carry STAGE-3/4 landings; the map grew two more HOLD rows this pass (`91f682b651`, `9df677a7eb`) [1st]. Countermove: flip line 35 to a token the watcher owns. |
| Machine-layer wire-checks | **local-LM now LIVE** | Scribe tunnel live (above). Harbor restored, sha-verified `:44831` [2nd, `e9025f396e`]. **New:** the A3 floor ran on a LOCAL LM Studio seat (`/root/.lmstudio/.../DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf`) [1st] — local-LM is a measured surface, a real change since 0429. Runners: HOLD-SAFE. |
| Dispositions | AUTO-CONTINUE: the A3 next rungs · HOLD-SAFE: W2-isolation, k-term, budget · NEEDS-THE-CHAIR: none new (the public-writes hold is the only chair-gate) | [1st] |

## 3. THE ENTROPY CLASSES

- **DEAD SURFACE:** the vendored `hermes_cli` mirror (0228's prize) — still unrowed; no commit since. Countermove: delete or row it.
- **LOOSE THREADS (unrowed):** (a) `probes/BATTERY-FULL-LEDGER-20261119.json` **deleted in the working tree, uncommitted** [1st, `git status`]; (b) `SCRIBE-WITNESS-REGISTRY.log` modified, uncommitted [1st]; (c) `tmp-artifacts/runner-recon-20261120.log` untracked [1st]; (d) the map's watcher-row pile (line 35 stale, rows accumulating); (e) the W2 label collision (§1). Countermove: commit-or-revert the working-tree trio; rename W2.
- **FRICTION:** the sweep's own cadence — 0429→0630 with 12 commits landed; the window's three items are carried unchanged because the eval-window is closed, so the sweep's core is a re-receipt. Countermove: give the carried items a strike-or-land deadline (validity decay: a carried wall's settle-condition decays if never re-attempted).
- **UNSPOKEN:** the PILOT-VERDICT's "PROOF-OF-CONCEPT CONFIRMED" closes the pilot question, but its own boundary is the **judgment layer** — and the A3 floor reads the GAP as moved **decision→representation** ("the floor has no suppression to target", `3d1ba778a7`). The pilot solved the question it asked, not the one the rig needs. Countermove: name the representation layer as the next pilot question, not a victory lap. (Storm-corroboration, class-only: SELD's read-side evidence-plane and AskALCF's commit-gate are the same discipline — receipt the boundary, don't adopt it.)

## 4. THE ORDERED NEXT-MOVES

1. Flip `MISSION-MAP-20261118.md` line 35's loop-state token to a watcher-owned token. Gate: the map's line names the record's actual stage. Seat: head.
2. Rename the workflow-presence W2. Gate: no two walls share a label. Seat: copycat.
3. Land the A3 next rungs — B′ sigma-notes control + the weights layer. Gate: a measured arm (INCONCLUSIVE is honest). Seat: the A3 wave.
4. Commit-or-revert the working-tree trio. Gate: clean tree. Seat: head.
5. Strike-or-land the k-term + budget re-verify. Gate: a dated decision. Seat: copycat.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

1. Question held: what changed since 0429, what entropy remains — evidence: 12 commits (`c0058d5d34..HEAD`).
2. Ground read [1st]: 0429, 0228, 1157, W2-PRESENCE, W2-ISOLATION, MISSION-MAP, A3 floor json, census.
3. Register: [1st]/[2nd] tagged per row; the pilot body named ABSENT.
4. Hand-separation: the A3 floor json + census + git status are [1st]; harbor-restored + R2-superseded are [2nd] (commit messages).
5. No invention: the W2 collision is named, not smoothed; the working-tree trio is receipted from `git status`.
6. Gate: nothing public; artifact only; RFC upstream QUIET.
7. Countermoves: every finding carries one.
8. Receipts: local==remote==`5868b595a1` [1st].

## 6. THE LOOP-STATE LINE

`CONTINUE + flip the MISSION-MAP line-35 token (the watcher's single-source) and rename the workflow-presence W2 — the window's three items stay HOLD-SAFE/carried (eval-window closed), and the A3 wave's next rungs (B′ sigma-notes + the weights layer) are the live next mechanism.`

**Finding one line:** NEGENTROPY-SWEEP-20261121-0630 — 12 commits since 0429 (PILOT SOLVED PROOF-OF-CONCEPT, census U1–U3 retired, A3 floor INCONCLUSIVE); window 3/3 still carried (eval-window closed) with a W2 label collision (workflow-presence ≠ guard-isolation); the working tree carries an uncommitted deletion + modification + untracked log.

**Next mechanism's one line:** the A3 wave's next rungs — the B′ sigma-notes control + the weights layer — move the suppression GAP from the decision layer to the representation layer, the pilot's actual boundary.