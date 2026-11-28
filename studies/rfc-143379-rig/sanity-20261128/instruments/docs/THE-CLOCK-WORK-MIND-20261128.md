# THE CLOCK-WORK MIND — instruments from the two time/entropy pieces, cross-read against the whole RFC

**Date:** 2026-11-28 · **Status:** extraction complete, candidates only — none adopted, nothing public
**Source:** "When Time Is Built From Entropy" (`149ab6004085`) and "When Time Isn't Ticking" (`1dd4667395bc`), R.T. Stone & G.W. Brown — the other grandfather's clock work; the papers behind them: Barontini's cold-atom test of the problem of time (Phys. Rev. Research), Kiefer & Zych's "Entropy as a Clock"
**Register:** [1st] = re-read this pass · [2nd] = carried from a study/RFC document, not re-derived · ABSENT+named = unreceived, never invented
**Cross-read:** the whole RFC — body (20,308 B, 161 lines) + all 72 comments fetched and indexed (`rfc-crossread/`), plus a sampled dive into `studies/rfc-143379-rig/` (370 MB, 26,298 files — top-level docs + the negentropy arm, deliberately not the whole tree)

---

## 1 · The three lenses the clock work gives

| lens | the article's version | the rig's existing word for it |
|---|---|---|
| **the external clock** | a clock is judged against a reference chain — GPS → PTP → network → device; the drift is the error, and keeping sync is the work | the RFC's **provenance** and **lock order**; the study's **loop-state token** and **board mirror** |
| **the internal clock** | time need not be fundamental — entropy flow inside a closed system can serve as the clock; the record's own state is the time | the RFC's **K-recency** and the compaction gate; the study's **k-term** and **kept-rates** |
| **the relational clock** | a clock is never just a clock — it is a civilization deciding how events belong together; order comes from relations, not an outside tick | the RFC's **archive-before-stub** one-way door; **provenance-origin**; the **"second witness"** |

The grandfather's own line — *you never really understand a system until you can break it and fix it yourself* — is the extraction rule: an instrument is only accepted here if it can be broken on purpose and repaired.

---

## 2 · The instruments

### I1 — The Internal Clock (entropy-as-clock)
**Source:** the BEC's entropy flow as the only clock in the box; the system does not import time, it reads its own state.
**Rig mapping:** the record's own aging/state (entries, chars, last-read, generation) as the clock for compaction decisions — not the wall clock, not the turn counter.
**Concrete form:** a per-entry internal time tuple, and a per-class survival rate over compaction generations.
**Falsifier:** if the internal clock's rate does not separate the classes it orders, the clock is decorative. **The study already ran this:** the k-term kept-rates are flat 0.26–0.42 across the four classes (`ADJUDICATION-NEGENTROPY-20261106` §k-term) — no k≈1/k≈0 split. The budget's class ordering FALLS on the k-term and must re-ground on probe lift (3.0 − baseline median). I1 is the instrument that makes that failure visible, not a fix for it.
**Status:** CANDIDATE · class-checked · not adopted. The study owns the re-grounding row.

### I2 — The Drift Gauge
**Source:** shift a clock against its reference and it either stays synchronized or drifts; the drift is information, not noise.
**Rig mapping:** the delta between the durable record and its representation (the summary), measured per compaction — the summary's claims against the record's bytes; the miss-trend as the drift's sign.
**Concrete form:** one drift reading per compaction cycle: byte/claim delta + survival rate + the direction of any contradiction (the summary flipping a constraint counts as a drift event, not a rounding error).
**Falsifier:** the drift must be monotone with loss — if the summary contradicts the record while the gauge reads zero, the gauge measures the wrong pair.
**RFC cross-read [1st]:** the RFC already names the class in these words — "the drift class" is 130 of the 300 most recent open issues, 43%, ~7,300 extrapolated (`6378725575`); the K-recency reversal −3.5pp at 300 cycles is the same drift inside one window (`rfc-body.md` L47–49, L108–111); kvnloo's field table shows the per-generation shape — ~95% → ~60% → ~40% → 20–50% (`7106956922`); 3oltan's cold pointer is the drift's early signal (`6362735198`).
**Study cross-read [1st]:** the sweep's own drift rows — the phantom branch, the disk map trailing the wire map, the FLEET-CYCLE-BODY label/file mismatch (`NEGENTROPY-SWEEP-20261122-0441` §3). The study's countermove is already a drift-gauge row: byte-verify every archive name against its commit label.
**Status:** CANDIDATE · class-checked · not adopted. Strongest overlap: the RFC's own "drift class" — this instrument is not new vocabulary.

### I3 — The Synchronization Hierarchy
**Source:** the external reference chain (GPS → PTP → network → device); each level synchronizes to the one above; a break at any level is a frame error, not a local bug.
**Rig mapping:** the write path's reference hierarchy — the anchor is the external reference, the chain docs the internal; the lock order (anchor first, then doc) is the sync order; a writer that takes the doc lock alone is out of frame.
**Concrete form:** a sync-tree ledger: for each write, which lock(s) were taken, in what order, and which level the read's snapshot came from. The tree's drift = a writer entering below its reference.
**Falsifier:** a single-lock writer that still serializes correctly is a counterexample; a correctly locked writer that still clobbers is the hierarchy's leak.
**RFC cross-read [1st]:** kvnloo's two-writer rule tested as shipped (`7155449141`); the lock order stated plainly — anchor first, then doc; anchor-only and USER.md writes take a single lock, no cycle (`7181202866`); the gate-before-lock race named and closed by the anchor's lock held through the doc write (`7185328530`). The RFC body carries the landing order as policy (`rfc-body.md` L99).
**Study cross-read [1st]:** the arm plan's standardize list is a sync hierarchy — the loop-state token single-source, the board's mirror discipline, fold byte-verification (`NEMO-NEGENTROPY-ARM-PLAN-20261119`).
**Status:** CANDIDATE · class-checked · not adopted. Strongest overlap: the two-writer rule is the hierarchy's first photographed instance.

### I4 — The Barrier Probe
**Source:** the 675 nm optical barrier splitting the BEC — a controlled wall, and the physics is in what crosses it.
**Rig mapping:** the anchor/chain boundary — the anchor's lock as the wall; the chain docs, orphans, and the reroute-to-chain-doc seam as the two sides; the read as the flow.
**Concrete form:** a barrier test that holds a write/remove on one side and reads the other, then reverses; the crossing (or refusal) is the receipt. The 50/50/0 anchor-read row is the first barrier receipt.
**Falsifier:** any state that crosses the barrier unaccounted — the orphan edge, the `@doc:foobar`/`foo` substring bleed (`6651356150`), the two-writer clobber (`7141681989`), the remove echo.
**RFC cross-read [1st]:** the anchor-read gap — `chain_docs` from the locked snapshot vs `orphan_docs` from a fresh disk read (`7210367328`); the anchor's lock held through the doc write (`7185328530`); the kit's probe must load real `fcntl` and drop `done.wait` so only `_file_lock` serializes (`7186196454`).
**Study cross-read [1st]:** the read-burn gate is the same wall in the machinery — non-git terminal refused, the write-window blocking reads (`NEGENTROPY-SWEEP-20261122-0441` §2). The study lives behind this barrier daily; the instrument already has a habitat.
**Status:** CANDIDATE · class-checked · not adopted.

### I5 — The Tabletop Mini-Universe
**Source:** the 120 ms tabletop run — the entire universe in a box small enough to break and fix; the multi-unit test across rooms/buildings/gravitational fields is the honesty check.
**Rig mapping:** the phase-1 pilot kit is the tabletop; the three contours (pve1 fcntl 3.13.5, WSL2 fcntl 3.11.9, native Windows 3.14.7) are the multi-unit deployment; the 300+ cycle contour is the field.
**Concrete form:** run the full system at small scale with the receipt as the internal clock; then re-run the same receipt across environments and compare the drift.
**Falsifier:** a tabletop pass that does not survive the field's length — the 300-cycle gate is exactly this falsifier, and today it reads FAIL (6.1% vs 9.6% baseline, −3.5pp; ruler broken, gate not waived — `rfc-body.md` L108–111).
**RFC cross-read [1st]:** the stress battery (200/200, 800/800, 100/100, 20/20) is the tabletop's first receipt (`rfc-body.md` L49); 3oltan's 300+ ≥0pp bar at 4×–8× is the field's acceptance (`6362735198`); the kit's determinism row is the receipt (`7186196454`).
**Study cross-read [1st]:** the lanes are the tabletop in operation — the copycat harness, the read-gate, the 60-round runs; the kit is their productized form (`sanity-20261128/`).
**Status:** CANDIDATE · class-checked · not adopted. The kit exists; this names what it is.

### I6 — The Proper-Time Ledger
**Source:** a clock is never just a clock — it is how events are ordered and made to belong together; each event carries its own relation to the others.
**Rig mapping:** each entry's own time (age, generation, last-read, origin) plus the ordering rule the compaction must honor — archive-before-stub is the one-way door; the pin is the second witness the summary does not author.
**Concrete form:** an entry-proper-time ledger the compaction reads: age, generation, origin hash, pin status; the compaction's summary is checked against it, not against itself.
**Falsifier:** the summary contradicting a pin, or an entry whose origin is unresolvable after compaction — both are ledger failures, not summary failures.
**RFC cross-read [1st]:** the one-way door — keep the archive before the stub, always (`rfc-body.md` L145); provenance survives with a resolvable origin (`L112`); the provenance loss is leg 4's second sub-cause (`L71`). kvnloo's pin rows are the ledger's first written form — 100% of pins survive 4 compactions verbatim, no second store, a contradiction between pin and summary flagged not kept (`7122500729`); the "second witness" framing is his (`7106956922`); xngg's pin-exemption from the iterative `_previous_summary` rewrite is the ledger's mechanism (`6401144230`).
**Study cross-read [1st]:** the arm plan's fold byte-verification and token single-source are the same ledger discipline applied to the study's own record (`NEMO-NEGENTROPY-ARM-PLAN-20261119`).
**Status:** CANDIDATE · class-checked · not adopted. Strongest overlap: `/pin` is the ledger's first fielded row.

---

## 3 · The cross-read matrix (the whole RFC, one line per instrument)

| instrument | the RFC's own word | body line | comment receipt | study receipt | verdict |
|---|---|---|---|---|---|
| I1 internal clock | K-recency, the long-session gate | L47–49, L107–110 | `6401144230` (pin exemption), `7106956922` (per-generation table) | `ADJUDICATION-NEGENTROPY` (k-term flat 0.26–0.42 → FALLS) | candidate; the rate that fails is already named |
| I2 drift gauge | "the drift class" — 43% of 300 recent issues | L17 (the compensation churn), L47, L108 | `6378725575`, `7106956922`, `6362735198` | `NEGENTROPY-SWEEP` §3 (wire/disk drift, label mismatch) | candidate; vocabulary is the RFC's own |
| I3 sync hierarchy | the landing order, the two-writer rule | L99, L145 | `7155449141`, `7181202866`, `7185328530` | `NEMO-ARM-PLAN` (token single-source, mirror, fold byte-verify) | candidate; first instance photographed |
| I4 barrier probe | the anchor's lock, the anchor-read gap | L94, L145 | `7210367328`, `7185328530`, `7141681989`, `7186196454` | `NEGENTROPY-SWEEP` §2 (the read-burn gate) | candidate; habitat exists |
| I5 tabletop mini-universe | the stress battery, the 300+ gate | L49, L108 | `6360811382`, `6362735198`, `7186196454` | the lanes + `sanity-20261128/` | candidate; the kit exists |
| I6 proper-time ledger | archive-before-stub (one-way), provenance-survival | L71, L77, L145 | `7122500729`, `7106956922`, `6401144230` | `NEMO-ARM-PLAN` (fold verification) | candidate; `/pin` is its first row |

**What the cross-read changes:** nothing in the RFC contradicts any instrument. Three overlaps are load-bearing — I2 is literally the RFC's "drift class", I3 is literally the two-writer/lock-order rule, I6 is literally the one-way door plus `/pin`. Two instruments (I1, I4) already have a recorded failure in the study: the k-term's flatness and the read-burn gate. One (I5) already has a working artifact: the kit. The extraction therefore adds naming and a formal shape, not a claim of novelty.

---

## 4 · The study dive (sampled — 370 MB, 26,298 files; top-level docs + the negentropy arm only)

- **The study's own entropy vocabulary is the articles' vocabulary.** `NEGENTROPY-SWEEP-20261122-0441` names six entropy classes — the phantom branch, the loose thread, the mis-receipt, the friction (disk map trails wire), the unspoken hold posture — each with a countermove. That is the "negentropy's the work of keeping it" line from the RFC's own proof-note (`6377891096`), operationalized.
- **The k-term failure is the sharpest study-side finding.** `ADJUDICATION-NEGENTROPY-20261106`: the budget's class ordering (decision-core > continuation > exact anchors > scope) presupposes differential keep-rates, but the measured kept-rates are flat 0.26–0.42 across all four classes. The mechanistic underpinning FALLS; re-ground on probe lift. This is I1's falsifier already met — and a reminder that a clock's rate is only useful if it separates the classes it orders.
- **The read-burn gate is the barrier, lived.** The study's lanes run git-only terminals; the write-window blocks all reads afterward — a controlled wall with the receipt on the other side. I4 is the study's daily condition, named.
- **The wire/disk drift is the reference-frame drift.** The local HEAD `af584b8a0a` vs wire `7f99a01eff` (empty merge-base), the disk map trailing the wire map by blob hash, the label/file mismatch — the study's own drift gauge is byte-verification, per archive, per fold.
- **The arm plan is the sync hierarchy, written as rules.** Loop-state token single-source, board mirror discipline, fold byte-verification, supply re-survey, SSH wire-check — each a level of the reference chain, each with a testable check.
- **The gate holds.** "Nothing public without the user's word" is stamped on the study's own sweeps; the extraction stays internal.

---

## 5 · Disposition

- All six are **candidates**, class-checked against the framework, **not adopted**, **nothing public**.
- The strongest three for the table's instruments (if the pair wants them): **I2 the drift gauge** (the RFC's own class, now formalized), **I6 the proper-time ledger** (`/pin` as its first row), **I5 the tabletop mini-universe** (the kit, already built).
- I1 and I4 are offered as **falsifier-bearing** instruments: the study has already broken them once, which is the article's own acceptance rule.
- I3 is the **policy-shaped** one: it names the lock order as a reference hierarchy, which the RFC already enforces in code.
- The reply and the child stay untouched; the instruments live here, in the drop, and in the chain fold — never in the public surface without the word.

*Artifact path:* `/root/workspace/drop/rfc143379-20261125-reply-stage/THE-CLOCK-WORK-MIND-20261128.md`
