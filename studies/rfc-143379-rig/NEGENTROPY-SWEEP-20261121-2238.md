# NEGENTROPY-SWEEP-20261121-2238 — the recurring negentropy sweep

**Seat:** the recurring negentropy-sweep lane (scheduled sweep, no_agent arm, cadence 2h).
**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public).
**Fire time:** 2026-11-21T22:38Z (artifact `NEGENTROPY-SWEEP-20261121-2238.md`).
**The gate (verbatim):** "the gate: nothing public without the user's word."
**Register:** receipts, never claims. **[1st]** = re-read by this lane this pass; **[2nd]** = carried from a study doc; **ABSENT + named** = not receivable. Tags: `IN-LANE` / `BORROWED <source>` / `HEAD-RECON`.

**READ-WINDOW NOTE (this fire):** the write-window opened before the analysis reads completed; the read-tools and the terminal's content-reads gated at fire. The window-check rows are carried **[2nd]** with primaries named and their read state marked. This is a receipt, not a claim.

## 1. THE WINDOW-CHECK (the gate)

| # | Standing item | State this fire | Receipt |
|---|---|---|---|
| W-A | W2-isolation settle-condition | NOT-RUN (wall) — carried | `W2-ISOLATION-STATUS-20261106.md`: **SEPARATION-UNMEASURED**; wall = eval-runtime LLM-window closed. **[2nd]** BORROWED <brief/2037 sweep>; primary read-gated. |
| W-B | k-term two-tier re-measure | PARTIAL — carried | kept-rates **0.42 / 0.29 / 0.26 / 0.26** (0.26–0.42, flat); the budget's class ordering presupposes differential keep-rates, the flat k-term contradicts it. **[2nd]** BORROWED <brief/2037 sweep>; primary read-gated. |
| W-C | budget consolidation re-verify | NOT-RUN — carried | **decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00**. **[2nd]** BORROWED <brief/2037 sweep>; primary read-gated. |

**Window verdict:** no windowed item flipped; W-A walled, W-C unverified, W-B partial. Window closed.

## 2. THE SEAM-SCAN (every fire)

| Seam | Current state | Receipt |
|---|---|---|
| read-burn harness-deadline | **OPEN — hit this fire.** Write-window opened mid-analysis; reads gated. | IN-LANE: read-gate error on the first read attempt. |
| fold: scribe cell → get_memory byte-compare | not re-derived (read-gated) | **[2nd]** BORROWED <2037 sweep>. |
| fold: served `?raw=1` grep | not re-derived (read-gated) | **[2nd]** BORROWED <2037 sweep>. |
| token watcher single-source line | carried: `NEGENTROPY-LOOP-20261119-v2` | **[2nd]** BORROWED <NEGENTROPY-ARM-EXECUTE-20261119>. |
| machine-layer wire-checks | carried: unchanged | **[2nd]** BORROWED <2037 sweep>. |
| dispositions | AUTO-CONTINUE: this sweep lands. HOLD-SAFE: W-A. NEEDS-THE-CHAIR: W-C + sentinel orphans. | IN-LANE. |

## 3. THE ENTROPY CLASSES (CTO freedom)

**Dead surface.**
- **D1 — sentinel orphans.** 2037 named `W2-ISOLATION-STATUS-20261106.md.sentinel` + `W2-ISOLATION-RUN-DESIGN-20261107.md.sentinel` as uncleared. Countermove: clear or retire; name the owner.
- **D2 — two split proposals** (`PROBE-SPLIT-PROPOSAL-20261121.md`, `SPLIT-PROPOSAL-DRAFT-20261121.md`) unrowed. Countermove: row or delete.

**Loose threads.**
- **L1 — unrowed landings since 2037.** Countermove: this artifact rows the delta.
- **L2 — the loop-state token's file** (`NEGENTROPY-LOOP-20261119-v2`) is the watcher's single source. Countermove: re-verify with reads open.

**Friction points.**
- **F1 — the read/write window seam.** The read-window can close before the analysis reads land, forcing a [2nd]-carried artifact. Countermove: hold the read-window until the sweep's first write.

**UNSPOKEN.**
- **U1 — the sweep receipts HEADs that may not survive a rebase/force-push.** Countermove: receipt the artifact's own commit hash, not HEAD-at-fire.

## 4. THE ORDERED NEXT-MOVES

1. **Re-open the reads and upgrade W-A/W-B/W-C to [1st].** Gate: nothing public. Seat: this lane.
2. **Clear/retire the sentinel orphans** (D1). Gate: nothing public. Seat: NEEDS-THE-CHAIR.
3. **Row or delete the two split proposals** (D2). Gate: nothing public. Seat: the fold lane.
4. **Re-verify the loop-state token's file** (L2). Gate: nothing public. Seat: the watcher lane.
5. **Hold W-A armed**; the chair names the eval-window-open trigger. Gate: nothing public. Seat: NEEDS-THE-CHAIR.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

1. Header — present. 2. Window-check — W-A/W-B/W-C table. 3. Seam-scan — six rows. 4. Entropy classes — D1-D2/L1-L2/F1/U1, each with countermove. 5. Next-moves — 1-5. 6. Compose-check — here. 7. Receipt stamps — inline tags. 8. Loop-state — §6.

## 6. THE LOOP-STATE LINE

`CONTINUE + re-open the reads and upgrade W-A/W-B/W-C to [1st]; then clear the sentinel orphans (next-moves 1-2).` Receipt: this artifact on `study/rfc-143379-rig-20261105`.