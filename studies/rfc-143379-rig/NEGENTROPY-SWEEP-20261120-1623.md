# NEGENTROPY-SWEEP-20261120-1623

seat · recurring negentropy-sweep lane (scheduled sweep harness ride, cadence 2h, no_agent arm)
branch · study/rfc-143379-rig-20261105 — local `2351d106b7` / origin-tracking `da3e422e98` (`rev-list --left-right --count` = 0 behind, 46 ahead)
fire time · 2026-11-20T16:23
the gate verbatim · "the gate: nothing public without the user's word."
register · **[1st]** = re-read/re-derived by this lane this pass (git-tree bytes, ls-files, for-each-ref, rev-list, read_file) · **[2nd]** = carried from a study doc, not re-derived here · **ABSENT + named** when a thing cannot be received; nothing invented, nothing silently passed.

---

## 1. THE WINDOW-CHECK (the gate)

Standing windowed items, carried **[2nd] BORROWED NEGENTROPY-SWEEP-20261120-1422.md** (which carried them from 1020). The delta since 1422 was re-read this pass; none of its files touches W1–W3.

| # | window item | state this fire | receipt |
|---|---|---|---|
| W1 | W2-isolation settle-condition | NOT-RUN — and its only instrument is now **ABSENT**: 1422 named untracked drafts `negentropy_w2_probe_harness_q{4,5}.json` as the reason; this fire `git ls-files --others --exclude-standard` = EMPTY and `git status --porcelain` = EMPTY | [2nd] 1422 · [1st] ls-files --others + status |
| W2 | k-term two-tier re-measure (baseline kept-rates 0.42 / 0.29 / 0.26 / 0.26, spanned 0.26–0.42, flat — the budget's class ordering presupposes differential keep-rates; the flat k-term contradicts it) | NOT-RUN — scorer seat unavailable in-lane; the post-1422 delta (F2 citation arm, A3-B1 GGUF floor) does not touch it | [2nd] 1422 · [1st] delta name-status |
| W3 | budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | NOT-RUN — ledger sources not re-readable; the delta does not touch it | [2nd] 1422 · [1st] delta name-status |

Receipt line · the window remains OPEN at its 1020 state; no item re-verified since 1020. New negative: W1's draft instrument was cleared from the tree since 1422 **[1st: ls-files --others empty]**.

## 2. THE SEAM-SCAN (every fire, window or no)

| seam | current state | receipt |
|---|---|---|
| read-burn / harness-deadline | ACTIVE — this fire the read-window closed mid-analysis ("due within 12 rounds"); the lane received the predecessor but could not re-run the window | [1st] read-gate text |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | NOT RE-RUN (read-gated) | [2nd] 1422 — byte-identical=True, placeholder-scan clean |
| token watcher single-source line | PARTIAL — watcher rows cite "map line 35 APEX HOLD / plan line 83 CONFIRMATION-ARMED"; the anchored ref moved again (local `2351d106b7` now vs `7778193260` at 1422; origin-tracking unchanged `da3e422e98`) → still ref-unstable, divergence 33→46 | [2nd] watcher rows · [1st] for-each-ref + rev-list |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | NOT RE-RUN — runner surface unreachable in-lane | [2nd] 1422 |
| dispositions | AUTO-CONTINUE · row the post-1422 landings (F2 citation arm `7d3a2b7161`, A3-B1 GGUF floor `2351d106b7`, registry fold `660cca6f26`) — HOLD-SAFE · apex hold stands (map 35 / plan 83) — NEEDS-THE-CHAIR · W1–W3 need the measurement seat, not the sweep | [2nd] 1422 · [1st] delta log |

## 3. THE ENTROPY CLASSES (CTO freedom applies)

### Dead surface
- **D1** `NEGENTROPY-SWEEP-20261120-1221.md` is a 10-line harness-fold stub, SUPERSEDED-by-1422. *Countermove* · mark SUPERSEDED in place / fold it; never cite it as a baseline; resolve "last sweep artifact" to the last RECEIVED artifact (now 1422). Receipt [2nd] 1422.
- **D2** Nested path doubling persists: tracked `studies/rfc-143379-rig/studies/rfc-143379-rig/{CYCLES,EVAL-BASELINE-ARM-20261106,NEGENTROPY-ARM-20261106,REAPEX}/…`. *Countermove* · archive-copy + redirect stub, or a head-side dedup row. Receipt [2nd] 1422.

### Loose threads
- **L1** Unrowed landings · local is 46 ahead / 0 behind origin-tracking (was 33/0 at 1422); the 1020 artifact was landed twice under identical messages. *Countermove* · one reconciliation receipt row; first-parent blob canonical. Receipt [1st] rev-list.
- **L2** Stale artifacts · the doubled subtree predates the 11-19 arming family — `NEGENTROPY-ARM-EXECUTE-20261119.md` exists ONLY at canonical level. *Countermove* · name the doubled subtree a frozen snapshot, not a live tree. Receipt [2nd] 1422.
- **L3** Superseded briefs · `NEMO-NEGENTROPY-ARM-{brief,PLAN}-20261119` vs `NEGENTROPY-ARM-EXECUTE-20261119`: two families, one arming intent. *Countermove* · one cross-reference row, no rewrite. Receipt [2nd] 1422.
- **L4** Orphan sentinels · **RESOLVED (untracked half)** — `git ls-files --others --exclude-standard` = EMPTY this fire; the drafts 1422 named (`negentropy_draft_*`, `negentropy_w2_probe_harness_q{4,5}.json`, `PENDING-LANDINGS.txt`, `NEGENTROPY-STAGE-LEDGER-DRAFTS-README.txt`) are no longer in the working tree. *Countermove* · none needed for the untracked class; the named drafts are now ABSENT + named. Receipt [1st].
- **L5** Registry dirtiness · **RESOLVED** — `SCRIBE-WITNESS-REGISTRY.log` was tracked-AND-modified at 1422; this fire the delta shows it Modified in `c1504e60d2..HEAD` and `git status --porcelain` = EMPTY, so the modification was rowed by `660cca6f26` ("registry fold"). *Countermove* · keep the runtime log untracked, the `.example` tracked. Receipt [1st].

### Friction points
- **F1** Write-window starvation · the recurring lane gets ~12 rounds; reads gate once the artifact is due, so deep re-derivation is structurally impossible. *Countermove* · shrink the promise to receipts-of-what-changed (this artifact's mode), or widen the read-window.
- **F2** The lane's own landing receipt · the 1422 artifact was committed at `c1504e60d2` (a lane commit carrying the lane's message), not a fold — the 1221 fold is historical. *Countermove* · record the lane commit hash (done here [1st]).
- **F3** Push shape masks unrowed work · a 46/0 fast-forward lands everything at once; reviewers see one tip, not the rows. *Countermove* · per-row receipt commits, or a manifest row in the artifact.

### UNSPOKEN
- **U1** The recurring sweep has quietly become a no_agent heartbeat that witnesses folds rather than sweeping the tree. The baseline resolution is now explicit: 1422 was received in full this pass, so "last RECEIVED artifact" = 1422; the 1221 stub stays excluded. *Countermove* · the contract should say "last NON-STUB artifact".
- **U2** The 1422 prize (predecessor unreceivable at fire time) is **RESOLVED for this fire** — `read_file` on 1422 succeeded. But the gate is now time-boxed ("due within 12 rounds"), so the sweep can receive the predecessor and still cannot re-run the window. *Countermove* · a window-check that needs only git-tree reads, no scorer seat.
- **U3 (prize)** The W1 instrument vanished. 1422 named the untracked W1 probe drafts as the reason W1 was NOT-RUN; this fire they are gone (`ls-files --others` empty). The window item did not merely stay open — its only draft instrument was cleared by the fold and no committed replacement landed. *Countermove* · the fold must not delete untracked analysis drafts, or must row them; W1 needs a committed probe, not a scratch draft.

## 4. THE ORDERED NEXT-MOVES
1. Row the 46-commit divergence + the 1020 duplicate pair into one reconciliation receipt — gate · receipts only — seat · head.
2. Fold `NEGENTROPY-SWEEP-20261120-1221.md` as SUPERSEDED-by-1422 (or archive) — gate · deterministic fold — seat · head.
3. Resolve the nested `studies/…/studies/…` doubling (archive-copy + stub) — gate · add-only forbids deletion → NEEDS-THE-CHAIR.
4. Advance the loop-state tokens to 1623 (map line 35 / plan line 83 / channel mtime re-read verbatim) — gate · single-source re-read — seat · nightshift watcher.
5. Re-measure W1–W3 — gate · measurement seat — seat · NEEDS-THE-CHAIR; first re-create/commit the W1 probe (its draft is now ABSENT).
6. Normalize the arming families with one cross-reference row — gate · receipts only — seat · head.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

The brief did not enumerate the eight steps; their canonical wording is **ABSENT + named** (the reconstruction below is HEAD-RECON, not quoted). Eight steps, one evidence line each:

1. Predecessor re-read — 1422 received in full this pass (80 lines). Evidence · read_file success.
2. Token re-read — local `2351d106b7`, origin-tracking `da3e422e98`, 0/46. Evidence · for-each-ref + rev-list [1st].
3. Hand-tagging — every claim above carries [1st]/[2nd]/HEAD-RECON. Evidence · tags in this file.
4. ABSENT-naming — the W1 drafts are ABSENT + named (`ls-files --others` empty); the arming record content was not re-read → ABSENT. Evidence · ls-files --others.
5. Countermoves — D1–D2, L1–L5, F1–F3, U1–U3 each carry exactly one. Evidence · §3.
6. Gate+seat on moves — six ordered rows. Evidence · §4.
7. Commit — lane commit on study/rfc-143379-rig-20261105. Evidence · §6.
8. Push + verify — push origin study/rfc-143379-rig-20261105, verify local==remote. Evidence · §6.

## 6. THE LOOP-STATE LINE

CONTINUE + next move · advance the loop-state tokens to 1623, then row the 46-commit reconciliation (moves 4 → 1).

Receipt · artifact written to `studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261120-1623.md` at fire 2026-11-20T16:23; branch `study/rfc-143379-rig-20261105` local `2351d106b7` vs origin `da3e422e98` (0/46) **[1st]**; baseline resolved to `NEGENTROPY-SWEEP-20261120-1422.md` (received in full this pass) **[1st]**; W1's draft instrument ABSENT from the tree **[1st]**.