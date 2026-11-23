# EVIDENCE-PACK-B — COMPACTION / GOVERNANCE + RIG-ASSETS EVIDENCE PACK
**kvnloo engagement · development inputs · gathered 2026-11-23**

*Seat under this pass: `meituan/longcat-2.5:free`. Scope: LOCAL reads only — every path below was read from disk this pass; nothing fetched, nothing public, no installs, no push, no checkout/stash/rm, writes only under `studies/rfc-143379-rig/`. Digest = `sha256` first 12 hex of the file bytes at read time. Paths are relative to `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/` unless absolute. Thread-side ids the local corpus does NOT hold are labelled **NOT-HELD-LOCAL (UNKNOWN-local)**. Nothing invented.*

---

## 0 · ANCHORS READ THIS PASS

| row-id | anchor | path | digest |
|---|---|---|---|
| B0-1 | the RFC record (the K-recency + governed-compaction bytes) | `CYCLES/RFC-143379-RECORD-20261111.md` | `d33354718e7b` |
| B0-2 | the RFC anchor (the field bar) | `RFC-ANCHOR-20261119.md` | `b4a52342c945` |
| B0-3 | the batteries' matrix | `plan/tank/STAGE-PLAN-BATTERIES-20261123.md` | `f1cbb5e3adfb` |
| B0-4 | the revised stage plan (the amended gates) | `plan/tank/REVISED-STAGE-PLAN-20261123.md` | `064f8d04eded` |
| B0-5 | the master (append-only §7 fold) | `MISSION-BRIEF-MASTER-20261119.md` | `d6928143e941` |
| B0-6 | the governance lens | `GOVERNANCE-LENS-E2E-20261107.md` | `b52fcd964b5c` |
| B0-7 | the compaction audit | `CYCLES/C5-COMPACTION-AUDIT-20261108.md` | `1f646ea392e2` |
| B0-8 | the lens outcome (governance-line ownership) | `LENS-OUTCOME-20261108.md` | `4a6901f61f2b` |
| B0-9 | the rough draft (the /pin slice + the latest field data) | `plan/tank/ROUGH-DRAFT-ENGAGEMENT-KVNLOO-20261123.md` | `c4c74f785491` |
| B0-10 | the assessment ask (the harness adoption) | `plan/tank/ASSESSMENT-ASK-20261123.md` (1,544 bytes) | `a4d9fdaa9fcc` |

---

## B1 · THE K-RECENCY FIGURES (as the record holds them)

Receipt: `CYCLES/RFC-143379-RECORD-20261111.md` digest `d33354718e7b` (lines 49, 109–112) + `RFC-ANCHOR-20261119.md` digest `b4a52342c945` (line 12).

| row-id | figure | the bytes |
|---|---|---|
| B1-1 | **headline (150-cycle sweep, 2×–32×, K=10)** | **+1.1 / +2.2 / +1.1 / +2.3 / +2.2 pp**; at the headline ratios **4× / 8× / 16× = +2.2 / +1.1 / +2.3 pp** |
| B1-2 | honest scope of that number | the pipeline's **real** compressor ratios; the paraphrase step **mocked**; pruning off; the probe's own **K=0** baseline (not the paper's 20.4/15.6/15.1) |
| B1-3 | **long-session reversal** | **300 cycles, K=10 lands 6.1 % against the 9.6 % baseline = −3.5 pp** |
| B1-4 | **the spread** | across runs the 300-cycle delta was **non-reproducible: −9.2 to +10.2 pp**, root-tracing to a **scope bug in the probe itself** — the measurement, not the window, was confounded |
| B1-5 | **the broken-ruler receipt** | "A broken ruler, not a reading: it can't certify the window safe, nor broken." Both the **−3.5 pp headline and the +1.1 pp mock-stable are disqualified as certifying evidence** until the probe's fixed. Under **mock-forced paraphrase** the window held stable at **+1.1 pp** |
| B1-6 | **the gate stands** | the long-session hard gate: at **300+ cycles, exact-recitation ≥ 0 pp vs baseline at every ratio in 4×–8×**, judged across the whole run; any single sub-zero point fails (the field's bar, 3oltan-seo). Status **FAIL-with-broken-ruler**; Governance Decay (arXiv 2606.22528) is the tail a soft gate lets through |
| B1-7 | the falsifier's status | the 150-cycle falsifier **PASS** is necessary but **not sufficient**; the 300-cycle gate **FAIL** — the gate is a question, not a waiver |

---

## B2 · THE GAP-3 GATE BATTERY + THE `3ec4157e` HARNESS ROWS

### B2a · the GAP-3 300+ gate battery (the kit-side instrument)

| row-id | item | receipt | digest | state |
|---|---|---|---|---|
| B2a-1 | the battery's matrix row | `plan/tank/STAGE-PLAN-BATTERIES-20261123.md` row **B4** | `f1cbb5e3adfb` | **7 rungs**: config · Gate S · junction completeness (J3/J4) · read-side decision gate · channel choice (2611.19700) · resolution variance (2611.23068) · 300+ gate criterion. Bar: **anchor-full wall, ≥0pp at 300+ cycles, 4–8×, logged-miss discriminator**. Model-execution rows recorded **BLOCKED** if quota is exhausted — **never fabricated**. Certification = **NOT-YET-CERTIFIED** |
| B2a-2 | the instrument + ledger on disk | `…/GAP-3-300-gate-battery/` (`battery.py`, `ledger.json`, `run-record.md`, `verdict.json`, `verdict-row.md`) | `a42ddc3fa945` · `8ae10dcd7610` · `b6c6bdeab66c` · `7f0c105a21fb` · `850996a26b3c` | generated 2026-11-22T07:32:38Z |
| B2a-3 | the measured rows | `verdict-row.md` | `850996a26b3c` | config **PASS** · Gate S **PASS** (47/69 vacuous = **0.6812**) · channel-choice **PASS** (cited, not re-measured) · junctions **BLOCKED** · read-side decision gate **BLOCKED** · resolution-variance **BLOCKED** · 300+ gate criterion **BLOCKED** (structure PASS; execution pending quota) → **3 PASS / 4 BLOCKED** |
| B2a-4 | the certification rule | same | `850996a26b3c` | **NOT-YET-CERTIFIED — pending model execution**; the M1 stamp certifies persistence of the iterate-do-not-one-shot method, **not** the gate |
| B2a-5 | the re-derivation | `plan/tank/IMPROVER-LOOP-20261122.md` | `199732893721` | `battery.py` re-imported + `run_all(build_fixture())` re-executed in memory: statuses `PASS,PASS,BLOCKED,BLOCKED,PASS,BLOCKED,BLOCKED` = **7/7 MATCH** vs on-disk `verdict.json`; `round(47/69,4)=0.6812`; certification NOT-YET-CERTIFIED |
| B2a-6 | the landing | master fold §7-z | `d6928143e941` | the GAP-3 battery **landed** (`745fb50378`, the M1 stamp's complement) |
| B2a-7 | thread-side anchor | the parent brief's id **`7076012199`** | — | **NOT-HELD-LOCAL (UNKNOWN-local)** — local equivalent: the rows above |

### B2b · the shared harness `3ec4157e` (the candidate fixed instrument)

| row-id | item | receipt | state |
|---|---|---|---|
| B2b-1 | the harness row | `plan/tank/ROUGH-DRAFT-ENGAGEMENT-KVNLOO-20261123.md` ("Your three questions", Q2) digest `c4c74f785491`; `plan/tank/ASSESSMENT-ASK-20261123.md` | the shared harness at **`3ec4157e`**, stacked on the composed tree, **one labeled set and one fixture**: the first test resolves cold doc pointers after a reload; the second runs our worst-point K-gate — **our −3.5 fails it; 5/5 green; both removal controls red** |
| B2b-2 | our ruler's state (why the harness matters) | same | "Our own ruler is broken, the minus 3.5 spread from **minus 9.2 to plus 10.2** under our old probe, so the RFC can certify nothing with it." |
| B2b-3 | the adoption | same + `ASSESSMENT-ASK-20261123.md` | the harness is **adopted as the candidate fixed instrument** for the long-session gate, run **head-to-head with our fixed probe**, under the RFC's protocol: swept **past 300 cycles**, **named baseline**, **real paraphrase**, the **whole per-cycle curve at every ratio in 4×–8×**, **one sub-zero point fails the gate**; **the instrument that survives takes the bar** |

---

## B3 · THE N-ROUNDS' CURVES + THE SETTLEMENT FIRE-5

| row-id | round | receipt (commit) | digest | curve |
|---|---|---|---|---|
| B3-1 | **N3** | `plan/tank/MAIN-LOOP-N3-ROUND-20261123.md` (`a2ecd2a48e`) | `1b37b50dad1d` | N17–N24 8/8, **+4**; cumulative **+81**; F-18 named on the head's own MASTER-REPAIR (the purge-commit's INTERMEDIATE parent restored instead of the true pre-purge peak) |
| B3-2 | **N4** (+ F-18 repaired) | `plan/tank/MAIN-LOOP-N4-ROUND-20261123.md` (deliverable `d22b00f89`; repair `26bcbe526e`) | `b0e649a04df1` | N25–N32 8/8, **+6**; cumulative **+87**. The repair: **67 insertions / 0 deletions, 51 fold headers, ALL 17 absent fold-lines restored byte-exact** (14 from the true-peak `902432e00b` + 3 from `76beff109b`); the master's 94,636-B substance + the night's folds now ONE at HEAD (**102,553 B**) |
| B3-3 | **N5** | `plan/tank/MAIN-LOOP-N5-ROUND-20261123.md` (`c0f7710460`) | `f941066a4798` | N33–N40 8/8, **+3**; cumulative **+90**; five zero-delta PARK-candidates; the design-space's exhausted at the gates |
| B3-4 | **N6** (+ the knee) | `plan/tank/MAIN-LOOP-N6-ROUND-20261123.md` (`56da134c76`) | `e765d9c22b79` | N41–N48 8/8, **+1**; cumulative **+93**; **seven of eight design-targets PARKED byte-stable**; the knee's reached |
| B3-5 | N7 (knee-verdict) | `plan/tank/MAIN-LOOP-N7-ROUND-20261123.md` (`6738ebb3a9`) | `4d105f3d7395` | **+1 → +94**; the tail `+6/+3/+1/+1`; the DESIGN-space exhausted by the loop's own evidence; **E-phase opened** (E1–E8 at named owner-beats) |
| B3-6 | N8 (total-zero) | `plan/tank/MAIN-LOOP-N8-ROUND-20261123.md` (`8cd385bc9c`) | `ced1dc0b2b1b` | **+0** — the first total-zero; PARK-confirmation-by-total-zero ACHIEVED; 8/8 E-gates HOLD; the loop continues into the EVENT-DRIVEN E-WATCH |
| B3-7 | **settlement fire-5** | `plan/tank/SETTLEMENT-FIRE5-20261123.md` (`ba4bae8886`); master §7-bn | `82f5af07e937` | the 5th fire rode a **fresh CONTENT-BEARING window** (HTTP 200 + visible content + **16 reasoning-tokens**, PIN-read-back verified): **NO at the outcome level** (UNKNOWN holds; bars immutable/unevaluable; C unmeasurable; settlement deferred) · **YES at the evidence level** (fire-#4's reasoning-exhaustion-24 void **FALSIFIED as a totality**, reclassified window-conditional). Delta **+1 tree-receipted property**; disconfirmed ×6; **CONTINUE** |
| B3-8 | the thread-side anchors | the parent brief's ids **`7102134501`** (+81) · **`7102296742`** (+87, F-18) · **`7102543806`** (+90) · **`7102618998`** (+93, knee) · **`7102980930`** (settlement fire-5) | — | **NOT-HELD-LOCAL (UNKNOWN-local)** — 0 local hits each; local equivalents are the round files/folds above |

---

## B4 · THE NEGENTROPY SWEEPS — W2 / k-TERM STATE (five receipts + the loop-state lines)

| row-id | sweep | digest | W2-isolation | k-term two-tier | loop-state line (verbatim gist) |
|---|---|---|---|---|---|
| B4-1 | `NEGENTROPY-SWEEP-20261122-2250.md` | `d9238679a98d` | **ANSWERED-PARTIAL, not settled.** Fire #5 fresh window: **14/20 HTTP 200 + 6/20 HTTP 429**; content-void persists (13 null-200 + 1 visible-but-INCORRECT `"fact"`); verdict UNKNOWN | **NOT-RUN.** Baseline kept-rates **0.42/0.29/0.26/0.26** flat (0.26–0.42) — contradicts the budget's differential-keep-rate ordering | **CONTINUE +** carry the three unrowed windowed items (W2-isolation, k-term two-tier, budget consolidation) and the truncation-metric carrier; the token-watcher bearer + fold-check bearer stay ABSENT + named |
| B4-2 | `NEGENTROPY-SWEEP-20261123-0051.md` | `2fdadcc31b8b` | STILL ANSWERED-PARTIAL — the battery's artifact is the settle-decider and no fire #6 landed | **NOT-RUN (carried 5 fires)** — flat 0.26–0.42 | **CONTINUE +** re-base the wire hash from `ls-remote` at the next fire and read the refire #5 battery's artifact |
| B4-3 | `NEGENTROPY-SWEEP-20261123-0252.md` | `cf98cd87dae2` | STILL ANSWERED-PARTIAL (carried) | **NOT-RUN (carried 6 fires)** | **CONTINUE +** same; no windowed item advanced this fire |
| B4-4 | `NEGENTROPY-SWEEP-20261123-1458.md` | `592b31dd0f68` | **NOT MET.** No bar-level measurement (no valid 4-arm n5 set; C unmeasurable). Fire #5's content-bearing window **FALSIFIES fire #4's void as a seat-constant** | **MEASURED, PENDING RECONCILE.** Leg-B DID the per-probe two-tier split: **high-keep 0.75 vs W2-empty-suppressed 0.00**; the flat 0.26–0.42 was an **averaging artifact**; the budget's class ordering **SUPPORTED at the high-keep tier**; the "NOT RUN" carry is **stale** | **CONTINUE +** land the 1458 artifact (local commit; never push); hand the second additive fold repair (N25) + the two-VOID-class naming to the head-at-fold |
| B4-5 | `NEGENTROPY-SWEEP-20261123-1659.md` | `54b3d9359d1c` | **NOT SETTLED (carried).** Condition = content-bearing fire-5 evidence at the true wire tip; read-gate refused the settlement bytes | **PARTIAL.** The leg-B file is on disk but **untracked at HEAD**; kept-rates flat [2nd] | Verdict **HOLD-SAFE** — two of three carriers have no committed home, so the window cannot close even when its evidence arrives; friction: a receipt that cannot be re-read cannot decay |

Cross-cutting receipts named in these files: the **dead surfaces** (the nested-clone trunk `studies/rfc-143379-rig/studies/rfc-143379-rig/`; the orphan sentinels; the root `FLEET-CYCLE-BODY-*` corpus), the **divergence 52-ahead / 22-behind**, and the countermove: stamp carried window receipts with a **validity-decay date**.

---

## B5 · THE `/pin` SLICE + THE FIELD DATA (kvnloo's latest comment)

Receipt: `plan/tank/ROUGH-DRAFT-ENGAGEMENT-KVNLOO-20261123.md` §"Your latest: the field data and the /pin slice", digest `c4c74f785491`.

| row-id | item | the bytes |
|---|---|---|
| B5-1 | **the survival curve** | owner messages surviving the summaries at about **95 / 60 / 40 / 20–50 %** across **four compactions** |
| B5-2 | the verbatim-block scope | the verbatim block on main covers **only the region compacted this time**; the opening ask is **gone from the verbatim block in 13 of 16 later summaries** in one sample |
| B5-3 | the flipped-instruction case | a standing privacy instruction **restated as its opposite without leaking** |
| B5-4 | **the durable-record-wins conclusion** | a durable record outside the summary, with a pointer in it, that the agent re-reads. The per-project ask list **survived days and carried the flipped instruction**; the goal file and append-only log **survived every compaction**; **one search back into history was worth 20–33 points** in the published scorecard. "Independently confirmed before the close-out." |
| B5-5 | **the `/pin` slice** | user-scoped, **off unless used**, carried mechanically in a **pinned block of every summary**, never re-summarized, never evicted, **capped with refusal like memory**, stored as a **pin entry in the decision ledger `113309`** rather than a second store; **tested at 4× with 100 % survival and a removal control**; the archive-before-stub / hard-window family in its simplest form; principle: **add onto what exists, never open anything parallel** |
| B5-6 | the receipts around it | the related issues **`136535` · `136541` · `154023` · `154177`** receipted with the **steer-gap** and **replay-frame** findings; KoNit-K's add-on offer named the right shape; **/pin is on the table as the first piece of the governed-compaction leg** |
| B5-7 | thread-side anchor | the parent brief's id **`7106956922`** | **NOT-HELD-LOCAL (UNKNOWN-local)** — 0 local hits; local equivalent: the section above |

---

## B6 · THE GOVERNED-COMPACTION — STAGED STATUS

| row-id | item | receipt | digest | state |
|---|---|---|---|---|
| B6-1 | the separation | `CYCLES/RFC-143379-RECORD-20261111.md` lines 85 / 99 / 153 | `d33354718e7b` | the governed compaction is **a separate issue — relates to `#116564` (the parent gap)** — the **provenance-origin classification, the archive-before-stub, the K-recency hard window**; **staged but not opened**; the issue's to be opened by its author |
| B6-2 | the missing home | `LENS-OUTCOME-20261108.md` §D8; `GOVERNANCE-LENS-E2E-20261107.md` | `4a6901f61f2b` · `b52fcd964b5c` | the governance line has **no home**: the governed-compaction issue is **unopened** and the **provenance-default invariant is unowned**; the proposal is **staged for the chair, never filed/posted** |
| B6-3 | the draft's content | `CYCLES/C5-COMPACTION-AUDIT-20261108.md` line 57 | `1f646ea392e2` | a valid draft first slice: **provenance-origin schema present** with the pipeline-definition default; **archive-before-stub ordering present** with the explicit `archive_ref` requirement; the **K-recency 2N parameter cited** to the S11-sweep; the **staged-for-chair / never-posted** clause present |
| B6-4 | the greenfield finding | `plan/tank/ROUGH-DRAFT-ENGAGEMENT-KVNLOO-20261123.md` Q1 | `c4c74f785491` | the cut's classifier: **no pinned or episodic classifier; position and budget only**; the head decays after the first pass; memory results are pruned like any other content; re-evaluated every pass; `MEMORY.md` reloaded on each commit; **no K window anywhere** → the governed compaction's assumed greenfield: **provenance-origin classification, archive-before-stub, a hard window; nothing in main conflicts or delivers** |
| B6-5 | the first piece | same file §"Your latest" | `c4c74f785491` | **`/pin` fits as a first piece of governed compaction** — the archive-before-stub/hard-window family in its simplest form; the ledger `113309` as its home |
| B6-6 | the staged-not-opened row | master §7-r (GOAL-VERDICT) | `d6928143e941` | the RFC asks three movements: read restored (#141876 open-unmerged) · store re-readable (#116673 open) · **compaction governed staged-not-opened**; GAP-4 = the compaction's release condition |

---

## B7 · THE PILOT'S STANDING ROWS

| row-id | row | receipt | digest | content |
|---|---|---|---|---|
| B7-1 | **3oltan-seo's field bar** | `RFC-ANCHOR-20261119.md` line 12; `CYCLES/RFC-143379-RECORD-20261111.md` line 110 | `b4a52342c945` · `d33354718e7b` | at **300+ agent cycles, exact-recitation ≥ 0 pp vs baseline at every ratio in 4×–8×**, evaluated across the whole run, any single sub-zero point fails — "a multi-hour production contour does not ship on a short-session extrapolation." The field's symptom: an anchor-full wall, **3,844/4,000 (96 %)**, most of it cold procedural detail |
| B7-2 | **ZTS's three-level comparison** | `CYCLES/RFC-143379-RECORD-20261111.md` COMMENT `6443308757` (ZacharyThomasStone, 2026-10-27) + the reply mapping; `plan/tank/OFFER-TERMS-3OLTAN-20261123.md` | `d33354718e7b` · `47552ab43826` | **Level 1** the current system (unmitigated wall) · **Level 2** read restored + anchor/reload fixed (the cheap additive baseline) · **Level 3** the proposed doc-chain + compaction changes. The offer names the same three levels: L1 current main without the read · **L2 the restored substrate (this offer's head)** · L3 the doc-chain + the governed compaction **when its staged issue opens** |
| B7-3 | **the record-mine's intent-register** | `plan/RECORD-MINE-20261121.md` §1 | `dcdbf859cfab` | the operator's register rendered: every bar set (length ≥3,000 words · depth · doors · receipts 14/14 · hygiene), every gate named (human gate · voice-check door · depth-selection · fork gate · RFC-quiet · court's posting), the corrections (the SHORT compose → recompose; the depth-math defect; the doc= demote gap; the wedge-era duplicates), the regret signals ('beam' leaked via the voice-check door), the leak class (purged; wire + serves leak-scan 0), the re-arms |
| B7-4 | the offer's conditions | `plan/tank/OFFER-TERMS-3OLTAN-20261123.md` | `47552ab43826` | the **two-add repair lands before any cartridge runs, no exception**; the assessment's verdict precedes the offer; the redaction contract signed by both sides; the offer never claims main nor an unsigned readiness |

---

## B8 · RIG-ASSETS CROSS-CHECK

### B8a · the working-notes corpus — identity search (labelled, not guessed)

| row-id | candidate checked | result |
|---|---|---|
| B8a-1 | `/root/workspace/notes/unresolved-questions.md` | the old **local-LLM setup notes** (last updated 2026-08-30) — **not** a rig working-notes corpus |
| B8a-2 | `/root/workspace/drop/NOTES.md` + `/root/workspace/master-page/NOTES.md` | identical **PVE-1 service & video notes** — not the rig corpus |
| B8a-3 | `/root/workspace/drop/prior-projects/notes/` | holds the **same** `unresolved-questions.md` — not the rig corpus |
| B8a-4 | `/root/.hermes/**` (filenames `*working*`) | none |
| B8a-5 | **corpus identity** | **UNKNOWN** — no file/dir named as a rig "working-notes corpus" was found. This pack therefore treats the **rig study dir itself** as the working corpus under cross-check, and names that substitution explicitly rather than silently. |

### B8b · coverage vs the public surfaces

| row-id | surface | what the record holds that the surface cites | gap (path-named) |
|---|---|---|---|
| B8b-1 | **the tank** | `plan/tank/` = **76 `.md`** + `plan/tank/briefs/` = **11**; every tank file read this pass carries its digest above; the master's §7 fold cites each landing by commit | — |
| B8b-2 | **the sweeps** | **119** `NEGENTROPY-SWEEP-*.md` under the study root; the five key ones digested above | **370 orphan `.sentinel` siblings** (`*.md.sentinel`) sit beside the sweep files — the orphan-sentinel class named in sweep 1458 |
| B8b-3 | **the nested-clone dead surface** | — | `studies/rfc-143379-rig/studies/rfc-143379-rig/` — **774 files, 11 MB** nested trunk; named a dead surface by sweep 1458 (two tracked copies of sweeps B/C); countermove: quarantine/named-read-only, head |
| B8b-4 | **the chain's segments** | `/root/workspace/master-page/memory-chain/` (served `:8789`) + `/root/workspace/drop/memory-chain/` (served `:8788`): `INDEX.md` **byte-identical** between the two; sampled segments `001-conventions.md` · `002-lessons.md` · `009-wins.md` · `015-handoff-20261119.md` · `016-fleet-orchestration-handoff-20261120.md` · `020-HANDOFF-20261122.md` all **byte-identical**; the INDEX's cited docs exist locally (`landing-ledger.md`; `repos/mechanism-of-mechanisms/NAVIGATION.md`; `repos/mechanism-of-mechanisms/docs/mission-flow/LIVING-HOME-REPO-BRIDGE/SMALL-MODEL-MEMORY-ACES.md`) | segments present: 001–010 · 012–020 · the `c28-*` segmented set; the chain is **append-only** and owns no rig-receipt content — it does not carry the tank/sweep digests (the rig corpus's job, not the chain's) |
| B8b-5 | **the private-repo mirrors under `/root/workspace`** | only **`/root/workspace/repos/hermes-agent/`** carries `studies/rfc-143379-rig/`; the rig study is reachable there | the other mirrors — `hermes-agent_battery` · `hermes-agent-fetch` · `hermes-agent-red-before` · `hermes-agent-fb-battery` · `hermes-compression-eval` · `mechanism-of-mechanisms` · `mechanism-of-mechanisms-bridge` · `academic-research-kernel` · `expert-roster` · `agent-governance-toolkit` — **do not carry the rig corpus** → **no mirror redundancy**; rows here cite only public-side equivalents, the private side used as source-truth cross-check only |
| B8b-6 | **the worktree state** | read-only observation at gather time | **4 `D` (deleted-in-worktree) `FLEET-CYCLE-BODY-*.md`** files — the root corpus named in sweep 1458; never touched by this pass (no checkout/stash/rm) |
| B8b-7 | **the GAP-3 battery's home** | — | it lives **outside** the study tree at `/root/workspace/kanban-pilot-workdir/.worktrees/t_2a6b031f/docs/mission-flow/GAP-3-300-gate-battery/` — read this pass, cited by path |

---

## B9 · WALL-CLAUSE QUESTIONS + UNKNOWN REGISTER (Pack B)

| row-id | question / unknown | basis |
|---|---|---|
| B9-1 | The k-term contradiction is unresolved: the budget's class ordering presupposes differential keep-rates, but the carried measure is flat (0.42/0.29/0.26/0.26). Sweep 1458 corrects it (leg-B two-tier: 0.75 vs 0.00) and names the reconciliation DIV-D1 — **is the reconciliation landed?** | sweep 1458 §"Self-correction" + UNSPOKEN; 1659: the leg-B file is **untracked at HEAD** |
| B9-2 | The W2 settle-condition: fire-#5's evidence class moved (content-bearing) but the condition is **NOT MET** (no bar-level measurement). Is the condition retired under the amended gate regime or re-fired as fire #6? | sweep 1458 UNSPOKEN (i); master §7-bs |
| B9-3 | The thread-side anchors (`7076012199` · `7102134501` · `7102296742` · `7102543806` · `7102618998` · `7102980930` · `7106956922`) | **NOT-HELD-LOCAL (UNKNOWN-local)** — 0 local hits each; local equivalents cited per row |
| B9-4 | The working-notes corpus identity (B8a-5) | **UNKNOWN**; substitution stated |
| B9-5 | Fresh-fire longcat re-probe (see Pack A A11-3) | owed, not run this pass (LOCAL-only clause) |

*No personal identifiers; the strip-contract held. Study paths only.*
