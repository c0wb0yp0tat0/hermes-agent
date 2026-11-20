# NEGENTROPY-SWEEP-20261120-1020

seat: recurring negentropy-sweep lane (scheduled sweep, no_agent arm, 2h cadence)
branch: `study/rfc-143379-rig-20261105` (local checkout; push target per contract) — see the ref-split finding
fire time: 2026-11-20T10:20Z
the gate: "the gate: nothing public without the user's word."
register: [1st] re-read by this lane this pass (git ls-remote, git log, git ls-tree, working-tree reads) · [2nd] carried from study docs · HEAD-RECON for the template reconstruction. ABSENT + named: the W2 lane's own artifact, the k-term re-measure raw data, the scribe tunnel — none reachable from this lane.

## 1. THE WINDOW-CHECK (the gate)
Carried [2nd] from the last sweep artifact on the branch (`NEGENTROPY-SWEEP-20261120-1020.md`, the 10:20 fire; predecessor 0957). This fire re-gauged; no new windowed evidence landed.

| windowed item | state | receipt |
|---|---|---|
| W2-isolation settle-condition | NOT-RUN — no new evidence; the settle still awaits the W2 lane's own fire | [2nd] 1020 window-check; [1st] no W2 artifact in the branch listing |
| k-term two-tier re-measure | NOT-RUN — baseline kept-rates 0.42/0.29/0.26/0.26, span 0.26–0.42, flat; the budget's class ordering presupposes differential keep-rates, the flat k-term contradicts it | [2nd] 1020/0957 artifacts |
| budget consolidation re-verify | NOT-RUN — decision-core 3.00 > clock/exec 2.83 > next-action 2.33 > scope 2.00 | [2nd] 1020/0957 artifacts |

Verdict: window unchanged; all three stay carried, none settled. The flat k-term remains the live contradiction.

## 2. THE SEAM-SCAN (every fire, window or no)
| seam | current state | receipt |
|---|---|---|
| read-burn harness-deadline seam | OPEN — the harness deadline can cut the read-burn before the fold checks finish; no lane owns the race. Live in this very fire: the read-gate fired at ~round 13 ("artifact due within 13 rounds"). | [1st] this pass |
| fold checks (scribe cell → get_memory byte-compare; served `?raw=1` grep) | NOT-RUN — no scribe tunnel reachable; terminal is git-only | [2nd] 1020 artifact; [1st] terminal policy |
| token watcher's single-source line | DEGRADED — the watcher's "single source" is split across two refs: 5 HOLD/CORRECTION rows sit on the date-suffixed branch while canonical lags | [1st] git log: da3e422e98..db6b42e43a ahead of canonical 093147d789 |
| machine-layer wire-checks (scribe tunnel, runners, Harbor/local-LM) | NOT-RUN — no runner/Harbor access from this lane | [1st] terminal git-only |
| dispositions | AUTO-CONTINUE (sweep cadence) / HOLD-SAFE (apex hold stands) / NEEDS-THE-CHAIR (ref split + path doubling) | [1st] watcher row db6b42e43a; [2nd] 1020 artifact |

## 3. THE ENTROPY CLASSES (CTO freedom applies)
- DEAD SURFACE — canonical `study/rfc-143379-rig` is 5 commits stale (093147d789, the 0819 sweep) while the live line is `study/rfc-143379-rig-20261105`. Countermove: one explicit ref-reconciliation (ff canonical to the date-suffixed head) or a named retirement of canonical.
- LOOSE THREAD — unrowed landing / duplicate fire: a prior `NEGENTROPY-SWEEP-20261120-1020.md` already exists at the same 10:20 fire label (10:20:19Z). This artifact supersedes it at the same path. Countermove: the head names fire labels uniquely (1020-a/1020-b) or the lane appends a supersession line.
- LOOSE THREAD — orphan sentinel: the "armed-but-unfed sentinel" (0819 commit message) is still unfed; no lane has named its feed. Countermove: feed it or retire it by name.
- FRICTION — path doubling: tracked sweep artifacts live at `studies/rfc-143379-rig/studies/rfc-143379-rig/…` (doubled) while the contract's artifact path is `studies/rfc-143379-rig/…` (single). Countermove: fix the mapping once (symlink or contract correction).
- FRICTION — shallow clone: `.git/shallow` truncates history, so `git log -- <path>` returns empty and the delta baseline cannot be diffed by path. Countermove: `git fetch --unshallow` on the study branch, or name a baseline blob.
- UNSPOKEN — the watcher's "local==remote ab1ac8bfbe" line is self-referential: the row's parent IS ab1ac8bfbe, so the equality is trivially true and verifies nothing about the wire. Countermove: compare against the remote ref's sha at fire time, not the row's own parent.
- UNSPOKEN — the apex hold has been re-gauged 5× with no state change; the hold is now a standing ritual, not a gauge. Countermove: name the exact condition that would lift the hold, or lift it.

## 4. THE ORDERED NEXT-MOVES
1. Reconcile the ref split: ff `study/rfc-143379-rig` to the date-suffixed head (or retire it). Gate: the gate. Seat: head.
2. Fix the artifact path doubling (nested vs contract path). Gate: the gate. Seat: head.
3. Feed or retire the armed-but-unfed sentinel. Gate: the gate. Seat: head.
4. Re-measure the k-term two-tier on a fresh baseline (flat 0.42/0.29/0.26/0.26 contradicts the budget ordering). Gate: the gate. Seat: k-term lane.
5. Set the W2-isolation settle-condition's exact pass/fail. Gate: the gate. Seat: W2 lane.

## 5. THE COMPOSE-CHECK + RECEIPT STAMPS
1. verdict line — window unchanged; ref split + path doubling named. [1st]
2. entropy classes — 7 findings, each with its countermove. [1st]
3. ordered next-moves — 5, each with gate + seat. [1st]
4. register — [1st]/[2nd]/HEAD-RECON tagged throughout; ABSENT items named. [1st]
5. gate verbatim — present in the header. [1st]
6. window-check table — 3 rows, receipts. [2nd]+[1st]
7. seam-scan table — 5 rows, receipts. [1st]
8. loop-state line — below. [1st]

## 6. THE LOOP-STATE LINE
CONTINUE + the head reconciles the canonical/date-suffixed ref split and the artifact path doubling; the next sweep re-gauges the windowed items and the sentinel's feed. Receipt: [1st] `git ls-remote` (4 rig branches: canonical 093147d789, -20261105 1e7fc2ef11, -20261114, -20261115), `git log` (5 watcher rows ahead of canonical), `.git/shallow` present.