# NEGENTROPY-SWEEP-20261120-1422

seat · recurring negentropy-sweep lane (scheduled sweep harness ride, cadence 2h, no_agent arm)
branch · study/rfc-143379-rig-20261105 — local `7778193260` / origin-tracking `da3e422e98` (`rev-list --left-right --count` = 33 ahead, 0 behind)
fire time · 2026-11-20T14:22
the gate verbatim · "the gate: nothing public without the user's word."
register · **[1st]** = re-read/re-derived by this lane this pass (git-tree bytes, ls-files, for-each-ref, rev-list, merge-base, read-file refusals) · **[2nd]** = carried from a study doc, not re-derived here · **ABSENT + named** when a thing cannot be received; nothing invented, nothing silently passed.

---

## 1. THE WINDOW-CHECK (the gate)

Standing windowed items, carried **[2nd] BORROWED NEGENTROPY-SWEEP-20261120-1020.md**. None re-run this fire: the harness closed reads mid-analysis ("READ-GATED: the write-window is open … analysis-phase is over"), so no scorer/probe seat was reachable.

| # | window item | state this fire | receipt |
|---|---|---|---|
| W1 | W2-isolation settle-condition | NOT-RUN — probe scripts exist only as untracked drafts (`negentropy_w2_probe_harness_q4/q5.json`) | [2nd] 1020 · [1st] git-status untracked listing |
| W2 | k-term two-tier re-measure (baseline kept-rates 0.42 / 0.29 / 0.26 / 0.26, spanned 0.26–0.42, flat — the budget's class ordering presupposes differential keep-rates; the flat k-term contradicts it) | NOT-RUN — scorer seat unavailable in-lane | [2nd] 1020 |
| W3 | budget consolidation re-verify (decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00) | NOT-RUN — ledger sources not re-readable under the write-gate | [2nd] 1020 |

Receipt line · the window remains OPEN at its 1020 state; no item has been re-verified since 1020 **[1st: this table]**.

## 2. THE SEAM-SCAN (every fire, window or no)

| seam | current state | receipt |
|---|---|---|
| read-burn / harness-deadline | ACTIVE — this fire: the read-window closed with the artifact due ("8 rounds left"); the prior fire landed its artifact through a fold commit instead of a lane commit | [1st] read_file refusal text · [1st] `1f4982076f` |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | NOT RE-RUN (read-gated) | [2nd] 1020 — byte-identical=True, placeholder-scan clean |
| token watcher single-source line | PARTIAL — watcher rows cite "map line 35 APEX HOLD / plan line 83 CONFIRMATION-ARMED", channel mtime 14:40, confirmation landing 5,860 B sha `ececd55d…30cb`; but the branch ref the watcher anchors has MOVED (origin/study/… = `da3e422e98` now; earlier rows named `db6b42e43a`) → the single-source line is no longer ref-stable | [2nd] watcher rows · [1st] for-each-ref + rev-list |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | NOT RE-RUN — runner surface unreachable in-lane | [2nd] 1020 |
| dispositions | AUTO-CONTINUE · row the post-0417 landings + advance tokens — HOLD-SAFE · apex hold stands (map 35 / plan 83) — NEEDS-THE-CHAIR · W1–W3 need the measurement seat, not the sweep | [2nd] 1020 · [1st] watcher rows |

## 3. THE ENTROPY CLASSES (CTO freedom applies)

### Dead surface
- **D1** `NEGENTROPY-SWEEP-20261120-1221.md` is tracked and is the immediate predecessor of this fire, yet it is a 10-line stub: it was landed by the harness fold commit `1f4982076f` ("HARNESS-FOLD: lane artifact folded deterministically"), not by a lane commit. *Countermove* · mark SUPERSEDED-by-1422 in place / fold it; never cite it as a baseline; resolve "last sweep artifact" to the last RECEIVED artifact (1020). Receipt [1st] `show --stat` (1 file, 10 insertions) + `merge-base --is-ancestor 1f4982076f HEAD` (exit 0).
- **D2** Nested path doubling persists: tracked `studies/rfc-143379-rig/studies/rfc-143379-rig/{CYCLES,EVAL-BASELINE-ARM-20261106,NEGENTROPY-ARM-20261106,REAPEX}/…`. *Countermove* · archive-copy + redirect stub, or a head-side dedup row. Receipt [1st] ls-files.

### Loose threads
- **L1** Unrowed landings · local is 33 ahead / 0 behind origin-tracking, and the 1020 artifact was landed TWICE under identical messages (`247c136f93` and `a8fc1340d9`). *Countermove* · one reconciliation receipt row; first-parent blob canonical. Receipt [1st].
- **L2** Stale artifacts · the doubled subtree predates the 11-19 arming family — `NEGENTROPY-ARM-EXECUTE-20261119.md` exists ONLY at canonical level, absent from the duplicate. *Countermove* · name the doubled subtree as a frozen snapshot, not a live tree. Receipt [1st].
- **L3** Superseded briefs · `NEMO-NEGENTROPY-ARM-{brief,PLAN}-20261119` vs `NEGENTROPY-ARM-EXECUTE-20261119`: two families, one arming intent. *Countermove* · one cross-reference row, no rewrite. Receipt [1st].
- **L4** Orphan sentinels · untracked drafts incl. `negentropy_draft_20261119.md`, `negentropy_draft_*_v{2,3}.md`, `negentropy_w2_probe_harness_q{4,5}.json`, `NEGENTROPY-STAGE-LEDGER-DRAFTS-README.txt`, `PENDING-LANDINGS.txt` — the missing analysis, un-rowed. *Countermove* · row or delete; treat the drafts as the unwritten 1221. Receipt [1st].
- **L5** Registry dirtiness survives · `SCRIBE-WITNESS-REGISTRY.log` is tracked AND modified (status M). *Countermove* · untrack the runtime log, keep the `.example`. Receipt [1st].

### Friction points
- **F1** Write-window starvation · the recurring lane gets ~8 rounds; reads gate once the artifact is due, so deep re-derivation is structurally impossible. *Countermove* · shrink the promise to receipts-of-what-changed (this artifact's mode), or widen the read-window.
- **F2** The lane cannot commit its own bytes · the 1221 landing is a harness-authored fold; the lane's receipt for its own artifact is indirect. *Countermove* · the fold body must carry the lane's exact message (it does) and the lane must record the fold hash (done here [1st]).
- **F3** Push shape masks unrowed work · a 33/0 fast-forward lands everything at once; reviewers see one tip, not the rows. *Countermove* · per-row receipt commits, or a manifest row in the artifact.

### UNSPOKEN
- **U1** The recurring sweep has quietly become a no_agent heartbeat that witnesses folds rather than sweeping the tree. The register's "carried [2nd] from the last sweep artifact" now silently resolves to 1020 — two fires back. *Countermove* · state the skip explicitly (done here); the contract should say "last NON-STUB artifact".
- **U2 (prize)** The previous fire's artifact could NOT be re-received at this fire even though it sits on the branch: the read-gate made the lane's own predecessor unreadable at fire time. *Countermove* · a fold-time assertion that an artifact carries ≥1 non-placeholder claim, else fold-as-STUB and exclude from baselines.

## 4. THE ORDERED NEXT-MOVES
1. Row the 33-commit divergence + the 1020 duplicate pair into one reconciliation receipt — gate · receipts only — seat · head.
2. Fold `NEGENTROPY-SWEEP-20261120-1221.md` as SUPERSEDED-by-1422 (or archive) — gate · deterministic fold — seat · head.
3. Resolve the nested `studies/…/studies/…` doubling (archive-copy + stub) — gate · add-only forbids deletion → NEEDS-THE-CHAIR.
4. Advance the loop-state tokens to this fire (map line 35 / plan line 83 / channel mtime re-read verbatim) — gate · single-source re-read — seat · nightshift watcher.
5. Re-measure W1–W3 (k-term two-tier, W2 settle, budget re-verify) — gate · measurement seat — seat · NEEDS-THE-CHAIR.
6. Normalize the arming families with one cross-reference row — gate · receipts only — seat · head.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS

The brief did not enumerate the eight steps; their canonical wording is **ABSENT + named** (the reconstruction below is HEAD-RECON, not quoted). Eight steps, one evidence line each:

1. Predecessor re-read — 1020 artifact received in full this pass; 1221 not receivable (read-gate) → named ABSENT. Evidence · read_file success on 1020; `1f4982076f` stat = 10 insertions.
2. Token re-read — origin/study/… = `da3e422e98`, local `7778193260`, 33/0. Evidence · for-each-ref + rev-list [1st].
3. Hand-tagging — every claim above carries [1st]/[2nd]/HEAD-RECON. Evidence · tags in this file.
4. ABSENT-naming — the arming record `NEGENTROPY-ARM-EXECUTE-20261119.md` was not re-readable at fire time; its content is ABSENT, not paraphrased. Evidence · read_file refusal.
5. Countermoves — D1–D2, L1–L5, F1–F3, U1–U2 each carry exactly one. Evidence · §3.
6. Gate+seat on moves — six ordered rows. Evidence · §4.
7. Commit — lane commit on study/rfc-143379-rig-20261105; fold hash recorded if folded. Evidence · §6.
8. Push + verify — push origin study/rfc-143379-rig-20261105, verify local==remote. Evidence · §6.

## 6. THE LOOP-STATE LINE

CONTINUE + next move · advance the loop-state tokens to 1422, then row the 33-commit reconciliation (moves 4 → 1).

Receipt · artifact written to `studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261120-1422.md` at fire 2026-11-20T14:22; branch `study/rfc-143379-rig-20261105` local `7778193260` vs origin `da3e422e98` (33/0) **[1st]**; baseline resolved to `NEGENTROPY-SWEEP-20261120-1020.md` because the 1221 predecessor is a 10-line harness-fold stub **[1st]**.
