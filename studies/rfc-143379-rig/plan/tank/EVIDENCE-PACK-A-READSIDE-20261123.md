# EVIDENCE-PACK-A — READ-SIDE / PR EVIDENCE PACK
**kvnloo engagement · development inputs · gathered 2026-11-23**

*Seat under this pass: `meituan/longcat-2.5:free`. Scope: LOCAL reads only — every path below was read from disk this pass; nothing was fetched, nothing public, no installs, no push, no checkout/stash/rm, writes only under `studies/rfc-143379-rig/`. Digest = `sha256` first 12 hex of the file bytes at read time (method reproducible). Paths are relative to `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/` unless absolute. Thread-side comment ids that the local corpus does NOT hold are labelled **NOT-HELD-LOCAL (UNKNOWN-local)** and paired with the local artifact that carries the same fact. Nothing below is invented; every figure resolves to the cited bytes.*

---

## 0 · ANCHORS READ THIS PASS (the record's spine)

| row-id | anchor | path | digest |
|---|---|---|---|
| A0-1 | the master (append-only §7 fold) | `MISSION-BRIEF-MASTER-20261119.md` | `d6928143e941` |
| A0-2 | the current seat/registry materialization | `plan/SEAT-REGISTRY-20261123.md` | `0cff6a5b450b` |
| A0-3 | the matrix legs' record | `plan/tank/MATRIX-LEGRUNS-20261123.md` | `4348f5da90d4` |
| A0-4 | the AM-S3 cold re-verification | `plan/tank/REVERIFY-AMS3-20261123.md` | `266004098c79` |
| A0-5 | the runners/registry act | `plan/tank/ACT3-RUNNER-REGISTRY-20261123.md` | `1c64f6b1b753` |
| A0-6 | the per-fire seat-liveness act | `plan/tank/ACT2-SEAT-PROBE-20261123.md` | `f305b445b2ea` |
| A0-7 | the full-exploration sweep (the 18-surface round) | `plan/tank/MAIN-LOOP-FULL-EXPLORATION-20261122.md` | `30b77cbe9bfe` |

---

## A1 · THE RESTORE'S PINS + THE READ-SUITE 4/4 AT THE RESTORE PIN

| row-id | item | receipt | digest | what the bytes hold |
|---|---|---|---|---|
| A1-1 | restore pin: plan value vs tree object | `plan/tank/MATRIX-LEGRUNS-20261123.md` §1–§2 (leg:R) + master fold §7-bq | `4348f5da90d4` | the plan's packet records the pin as **`6609dac951`**; the tree object is **`6609dacba9`**; §7-bq answers the discrepancy with receipts — *"the tree's 6609dacba9 — the plan's 6609dac951 was a TYPO"*. The **dual-label seam is retained**, never reconciled-away (also §7-bs: "the 6609dac951-pin seam retained (pr-141876 = 6609dacba9)"). |
| A1-2 | pushed-truth vs local ref | master fold §7-bd (`2ef28c2ee3`/`2c923ec118`) + `ACT3-RUNNER-REGISTRY-20261123.md` §4–§5 (seam S3) | `d6928143e941`, `1c64f6b1b753` | §7-bd: the fork's `fix/restore-read-action` `ls-remote` == **`6609dac951`** (pushed truth); ACT3 S3: the live branch + local ref are **`6609dacba9`**, and `6609dac951` is **not a resolvable local object**. Both values carried. |
| A1-3 | read-suite 4/4 at the restore pin (R leg) | `plan/tank/MATRIX-LEGRUNS-20261123.md` §2 leg:R; committed **`9d74420def`** (master §7-bq) | `4348f5da90d4` | on pr-141876 (tree `6609dacba9`): the **verbatim packet reproduced 4/4 FAIL** with the predicted call-shape errors; the **N10-re-scoped Ran-4-tests-OK exit-0**. |
| A1-4 | the four fork pins (registry form) | `plan/SEAT-REGISTRY-20261123.md` "The forks" table | `0cff6a5b450b` | study HEAD **`f652b71b4e`** (pre-restore, no read arm) · pr-139606 **`d1bdb4582c`** (write-gate, feat/135039) · pr-141876 **`6609dac951`** (restore, fix/restore-read-action) · a9c65dc4 **`a9c65dc43d`** (combined, memory-chain-doc-read-combined). |

---

## A2 · THE MATRIX LEGS — pve1 (`9d74420def`)

Receipt: `plan/tank/MATRIX-LEGRUNS-20261123.md`, digest `4348f5da90d4`; master fold §7-bq.

| row-id | leg | measured state (bytes) | status |
|---|---|---|---|
| A2-1 | **R** — pr-141876 × pve1 | verbatim read-suite packet 4/4-FAIL with the predicted call-shape errors; N10-re-scoped Ran-4-tests-OK exit 0 | LANDED |
| A2-2 | **P** — pr-139606 S7 | `verify_post_write` present **2 rows** vs **0** elsewhere (the write-gate's presence proof) | LANDED |
| A2-3 | **C** — a9c65dc4 chain-docs | the chain-docs surface + **14 tests** + the read-surface | LANDED |
| A2-4 | **H** — negative controls | recorded **NOT-RUN-with-reason** (the read arm's absence at study HEAD), never a failed run | NOT-RUN-WITH-REASON |
| A2-5 | the verdict | **F-16 CONFIRMED** — no single fork carries read+S7+chain-docs; the full combination remains UNTESTED (its leg awaits the MERGED substrate, #116673's lineage, not a runner) | CONFIRMED |

Remainders named in the same fold: p0tat0/c0wb0y support legs (R/P/C cross-runner determinism) + cloud precision legs, ready-to-dispatch.

---

## A3 · THE AM-S3 RE-VERIFY (`4c049ec82b`)

Receipt: `plan/tank/REVERIFY-AMS3-20261123.md`, digest `266004098c79`; master fold §7-bt.

| row-id | item | what the bytes hold |
|---|---|---|
| A3-1 | fan 3/3 | **CONFIRMED** — no seat fired at landing, no matrix-fork ground; the verdicts stand, their seams stay open |
| A3-2 | B1 fire | **CONFIRMED** — the VOID-class UNKNOWN is exactly AM-B1's prescribed outcome; re-read, never re-fired |
| A3-3 | matrix legs | **ADJUSTED-NEEDS** — 4 of AM-F3's 8 arms lack leg-rows: `re-cut-write-gate-surgical` · `r2gate` · `r2cs`/`r2cs-sync` · `origin/fix/restore-read-action` + F-16 |
| A3-4 | seams | SW-1's phantom shas · the superseding sends · the AA's byte-identical siblings · the pr-141876 dual-label · the three study-refs — **NONE reconciled-away** |
| A3-5 | next-act sequence | ACT-2 per-fire seat-liveness probe → ACT-3 runners/registry → ACT-4 batteries → ACT-5 the fan's RE-FIRE (stale landings cannot be reused); the gather is **NOT acceptance-ready** (G5–G7/G18 UNKNOWN; AoA's 8 settle-conditions open) |

---

## A4 · THE FORK SET vs THE LIVE REFS (this fire's re-verification)

Receipt: `plan/tank/ACT3-RUNNER-REGISTRY-20261123.md` §4–§5, digest `1c64f6b1b753` (wire `ls-remote` first, per the anchor).

| row-id | fork | registry pin | live ref (measured) | status |
|---|---|---|---|---|
| A4-1 | study HEAD | `f652b71b4e` | `refs/heads/study/rfc-143379-rig-20261105` = **`a848d06254199bf628e1c1124e69a68f95983f01`** | **S1 MOVED HEAD** (the label `f652b71b4e` is the pre-restore pin, still an ancestor, no longer the branch head) |
| A4-2 | pr-139606 | `d1bdb4582c` | `refs/heads/feat/135039-write-gate` = `d1bdb4582cd5d16be6a6b486f696f8240c222b96` | **MATCH** |
| A4-3 | pr-141876 | `6609dac951` | `refs/heads/fix/restore-read-action` = `6609dacba951d51cdd880ac1031e546dd7fac289` | **S3 IDENTIFIER SEAM** (both retained) |
| A4-4 | a9c65dc4 | `a9c65dc43d` | no live branch carries it (`rev-list --all` count 0; `for-each-ref --contains` empty; no `combined-substrate` branch) | **S4 DANGLING-PIN** |
| A4-5 | the other AM-F3 arms | — | `re-cut-write-gate-surgical` = `9811e52752` ✓ · `round2-gate` = `268bb09147` ✓ · `round2-combined-substrate` = `c39d8ce722` ✓ | verified |
| A4-6 | registry form | 4-hero table | the amended AM-F3 fork-set is **8 rows**; the register is the stale 4-hero form | **S5 STALE-FORM** |

---

## A5 · THE COMPOSED-TREE EVIDENCE (443 pass / 64-of-64)

| row-id | item | receipt | status |
|---|---|---|---|
| A5-1 | the composed tree `ec649ad9` | master §7-at (the fold quotes the helper's reply to the RFC comment **`7087999804`** — **LOCALLY HELD**: it appears in `MISSION-BRIEF-MASTER-20261119.md`, `plan/tank/MAIN-LOOP-FULL-EXPLORATION-20261122.md`, `plan/tank/VET-KVNLOO-20261122.md`) | **MAIN + #116673 + #141876 `ec649ad9`: 443 pass + the dispatch contract 64/64**; race green; 17/17 on the b6ff7dae stack; the race disappears only when the restore's hardened read is present |
| A5-2 | the same row, our side | `plan/tank/ROUGH-DRAFT-ENGAGEMENT-KVNLOO-20261123.md` ("On your probe table") digest `c4c74f785491` | "The composed tree at ec649ad9: race green, 443 pass, dispatch contract 64 of 64… the strongest confirmation that the restore is the right precondition" |
| A5-3 | the fix-already-in-ours check | master §7-at(2) + `ROUGH-DRAFT…` Finding 1 | removing the lock **or** the no-cache-write alone stays green; removing **both** turns red; the restored read with the collaborator's hardening carries both |
| A5-4 | thread-side receipt anchors | the parent brief's ids **`7088029750` · `7104461078` · `7105992714`** ("our receipts") | **NOT-HELD-LOCAL (UNKNOWN-local)** — a full-corpus grep returns 0 files for each; the local equivalents are the §7-at fold line and the ROUGH-DRAFT row above |

---

## A6 · THE VET's REPRODUCTION + FB-2

| row-id | item | receipt | status |
|---|---|---|---|
| A6-1 | the VET's crown reproduction | master §7-az (commit **`9ce4e0078c`**); `plan/tank/VET-KVNLOO-20261122.md` digests `25a56afc911a` | the two-add-overwrite **REPRODUCED by executing the verbatim `_add_doc` body against a temp dir — `FIRST_SURVIVED_SECOND_ADD=False`**; the atomic-write semantics confirmed at `utils.py:361`; the catch is REAL, independently confirmed |
| A6-2 | the two-add class | master §7-at(3) | `_add_doc` (`memory_tool_store.py:580-618`) writes content as the whole file → a second chain-doc add overwrites the first; a two-add probe fails there and passes on the combined tree; the 297-battery does NOT cover it |
| A6-3 | **FB-2** | master §7-at carrier list; `ROUGH-DRAFT…` Finding 2 | the two-add-probe is armed as the armor battery's next falsifier (**FB-2**) |
| A6-4 | the adjudication | §7-az | **ACCEPT-WITH-CONDITIONS** — accept the material as stage-3 input; REFUSE the implied "green transfers to our tree", the opinion-as-fact interpretations, the unverified methodology, and any recipe-execution on that rung; six conditions enumerated |
| A6-5 | thread-side anchors | the parent brief's ids **`7089118650`** (the VET reproduction) · **`7088131689`** (FB-2) | **NOT-HELD-LOCAL (UNKNOWN-local)** — 0 local files; the local equivalents are the §7-az fold and the two tank files above |

---

## A7 · THE 88/88 DISPATCH-GAP ROW

| row-id | item | receipt | status |
|---|---|---|---|
| A7-1 | the claim | master §7-at(4): "#141876's tests stay **88/88** with the read-dispatch line deleted; the handler-path test + the doc-argument fix added" | **CARRIED** |
| A7-2 | the independent tagging | `plan/tank/VET-KVNLOO-20261122.md` claim #12 | tagged **`[UNVERIFIED]`** — "Asserted suite result; not re-executed; commit pr-141876 exists locally but its suite was not run." |
| A7-3 | the gap's meaning + conditions | `plan/tank/ROUGH-DRAFT-ENGAGEMENT-KVNLOO-20261123.md` Finding 3 | the suite tested the method, not the seam; with the read dispatch line deleted 88/88 still passed. Conditions: **the handler-level test goes through the actual dispatch**; **the one-line doc-argument fix covers Finn's new parameter**; both ride with #141876 when it lands, authorship kept. |
| A7-4 | thread-side anchor | the parent brief's id **`7089118650`'s conditions** | **NOT-HELD-LOCAL (UNKNOWN-local)** — the conditions' local home is the §7-at fold + Finding 3 above |

---

## A8 · THE RECIPE VERDICT — `RECIPE-CLEAN-AT-BASE`

| row-id | item | receipt | status |
|---|---|---|---|
| A8-1 | the verdict | master §7-bc (clean-apply test `deleg_4936a00a`, solar — commit **`00fdffb216`**) | isolated worktree at base `0f602c5f6f18` + cherry-pick `-x` of the full range = **7/7 commits applied CLEANLY, exit 0, no conflicts** → **RECIPE-CLEAN-AT-BASE**; the recipe was never broken — the prior PR-branch abort was the 1674-ahead cross-lineage graft (target-selection finding) |
| A8-2 | the retry record | `plan/tank/RECIPE-RETRY-20261122.md` digest `bb75740491e3` | the clean-apply test's own record (base-anchored lineage recommended; the fix is NOT applied onto the PR-branch) |
| A8-3 | thread-side anchor | the parent brief's id **`7090433601`** | **NOT-HELD-LOCAL (UNKNOWN-local)** — local equivalent: §7-bc + the retry record |

---

## A9 · THE PR-SIDE MOVEMENT STATUS (as the record holds it)

| row-id | movement | receipt | status |
|---|---|---|---|
| A9-1 | **handler-test adoption** | master §7-at(4); `ROUGH-DRAFT…` Two + Finding 3; `plan/tank/ASSESSMENT-ASK-20261123.md` | the handler-level dispatch test rides **with #141876**, **authorship kept**; it goes through the actual dispatch (not the method) |
| A9-2 | **two-add repair** | master §7-at(3); `ROUGH-DRAFT…` Two + Finding 2 | the repair **inherits the combined tree's doc semantics** (the behavior where the probe passes), rather than re-inventing the write side; it lands in **the fork's own gate home before anything pilot-adjacent rides it** |
| A9-3 | **Finn's-seat law** | master §7-bc ("THE OWNERSHIP-LIGHT"); `ROUGH-DRAFT…` Two | the combined-lineage's natural home is **Finn763's #116673** (the chain-docs PR); the where-it-lands decision is **the operator's/Finn's seat**; #116673 re-cuts on top of #141876; nothing moves on that PR's public surface without him |
| A9-4 | the recipe's execution rule | `ROUGH-DRAFT…` "The recipe"; §7-bc | the cherry-pick recipe is **not executed raw**; the compose is **re-derived, receipted, then proposed**; clean at its own base |
| A9-5 | upstream track | `ROUGH-DRAFT…` Two; `ASSESSMENT-ASK-20261123.md` | the upstream merge is the public track and proceeds **in parallel**; the kit's measured state waits on nothing; the assessment targets the **composed head, never the pre-fix branch**; the verdict precedes any field offer |

---

## A10 · THE RECORD-MINE (`7070397783`)

| row-id | item | receipt | digest |
|---|---|---|---|
| A10-1 | the mine | `plan/RECORD-MINE-20261121.md` | `dcdbf859cfab` |
| A10-2 | its shape | same file §0 mine-index · §1 **intent-register** (verbatim quotes + sources: the bars set, the gates named, the corrections, the regret signals, the leak, the re-arms) · §2 failure-classes 2.1–2.10 · §4 seams-found · §5 top-10 findings | — |
| A10-3 | standing rows it holds | §1.4 bars (length ≥3,000 words · depth · doors · receipts 14/14 · hygiene) · §1.5 gates (human gate, voice-check door, depth-selection, fork gate, RFC-quiet gate, court's posting gate) · §1.6 corrections (the SHORT compose → recompose; the depth-math defect; the doc= demote gap; the wedge-era duplicates) | — |
| A10-4 | thread-side anchor | the parent brief's id **`7070397783`** | **NOT-HELD-LOCAL (UNKNOWN-local)** — local equivalent: the file above |

---

## A11 · SEAT / DISPATCH-CONTRACT STANDING RECEIPT (longcat, PIN echo)

| row-id | item | receipt | digest | status |
|---|---|---|---|---|
| A11-1 | probe #1, fire 1 | `plan/tank/ACT2-SEAT-PROBE-20261123.md` §2 | `f305b445b2ea` | requested `meituan/longcat-2.5:free`; **PIN `PIN-70FABE99E3` echoed in content**; content-bearing; finish stop |
| A11-2 | probe #1, fire 2 (same day) | `plan/tank/ACT3-RUNNER-REGISTRY-20261123.md` §2 | `1c64f6b1b753` | responding model IS `meituan/longcat-2.5:free`; **PIN `PIN-90AF232492`** echoed; content 232 B; finish stop |
| A11-3 | **this fire's fresh probe** | — | — | **NOT-RUN-THIS-PASS** — reason: the gathering pass is **LOCAL reads only / nothing public**; no external inference call was made. Standing receipt: the two rows above (same seat, same day, two fires). **Wall-clause QUESTION, not a silent pass**: a fresh-fire re-probe is owed to the head if this pack is used as a dispatch input. |

---

## A12 · WALL-CLAUSE QUESTIONS + UNKNOWN REGISTER (Pack A)

| row-id | question / unknown | basis |
|---|---|---|
| A12-1 | Is the pr-141876 identifier `6609dac951` vs `6609dacba9` a live divergence or a labeling seam? | §7-bd (ls-remote 6609dac951) vs ACT3 S3 (live/local 6609dacba9); both retained, never reconciled-away |
| A12-2 | Do the thread-side receipt ids `7088029750` / `7104461078` / `7105992714` correspond to our three composed-tree confirmations? | 0 local hits; the local equivalents are the §7-at fold + the ROUGH-DRAFT probe-table row |
| A12-3 | Was the 88/88 suite result ever re-executed locally? | VET claim #12 `[UNVERIFIED]`; no local re-run receipt found |
| A12-4 | Fresh-fire longcat re-probe (A11-3) | owed, not run this pass |
| A12-5 | All other thread-side ids in the parent brief (`7089118650` · `7088131689` · `7090433601` · `7070397783`) | **NOT-HELD-LOCAL (UNKNOWN-local)** — local equivalents cited at A6-5, A7-4, A8-3, A10-4 |

*No personal identifiers; the strip-contract held. Study paths only.*
