# LOSS-LADDER-AOA-20261121 — analysis of alternatives (depth · stub→real · the tool-output class)

TEAM: ACES · the think-tank AoA rotation
MISSION: the loss-ladder's decision points — depth selection · the stub→real ladder's path · the tool-output class's zero-at-every-depth
EVIDENCE (cold-read; recomputed from the ledger, not from prose):
        probes/LOSS-LADDER-20261121.json  — verified matrix + decision_rule (recomputed: user-stated 10/10/10,
          assistant-prose 0/0/10, tool-output 0/0/0, reasoning-only 0/0/0 over 10 episodes/cell)
        probes/LOSS-LADDER-20261121.md    — the landing doc (depth-math prose defect named in the audit)
        probes/loss_ladder.py             — the deterministic zero-billed generator
        audit/LOSS-LADDER-AUDIT-20261121.md — Assess/Design/Probe verdicts + boundary thresholds
        audit/ARC-LONGEVITY-STORM-20261121.md — the two-way door's arc-length table + the deep-end quality watch
        audit/SCRIBE-WITNESS-REGISTRY.log  — the witness row's shape (artifact|hash|HEAD|hermes-agent)
        think-tank SKILL.md §"THE BRIEF'S ARMAMENT" — the wall clause's binding form
BRANCH: study/rfc-143379-rig-20261105 · RFC quiet · pre-write HEAD 46512eef87 (local == ls-remote)
ARTIFACT (absolute path): /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/audit/LOSS-LADDER-AOA-20261121.md

---

## 0 · THE VERDICT (one breath)

Three decisions, one frame: **the depth knob buys arc length, not evidence; the tool-output class is out of the depth knob's reach.** Recommendation set: (1) **0.65** as the near-term depth door with a *named deep-end quality-watch*, 0.5 as the one-line rollback, 0.8 as a conditional upgrade — never as a receipt-recovery play; (2) the **hybrid** stub→real ladder — deterministic stub as the gate (already green, zero-billed), real `/compress` runs as the certificate; (3) the **rig's native transparency-checkpoint** as the tool-output mitigation, instantiated by one-line signature rows + witness-registry rows + fold-downstream, gated by a *recoverability canary*. Each recommendation carries its counter below; none of them is an upstream or config change without the operator's word.

Scope clause (carried from the audit, never smoothed): the matrix is valid **for the stub at the three tested depths**. `tool-output = 0.0 at every depth` is exactly true for {0.5, 0.65, 0.8}; the stub's boundary is d ≈ 0.864, and reasoning-only is outside the window at all depths.

---

## 1 · THE DECISION FRAME (what the alternatives are alternatives to)

The ladder's landing (08b15cac75) measured planted facts by source-type × depth under a deterministic, zero-billed stub compression pass (head+tail retained, middle compacted; `keep_each = ceil(2082·d/2)` per side). Recomputed from the raw ledger:

| depth | user-stated | assistant-prose | tool-output | reasoning-only | load-bearing classes intact? |
|---|---|---|---|---|---|
| 0.5 | 1.0 | 0.0 | 0.0 | 0.0 | no — head only |
| 0.65 | 1.0 | 0.0 | 0.0 | 0.0 | no — head only (`all_lb_intact_0.65 = false`) |
| 0.8 | 1.0 | 1.0 | 0.0 | 0.0 | no — markers restored, receipts still gone (`min_depth_keep_load_bearing = null`) |

`decision_rule` (verbatim key line): *the 0.65 band rides on head-only retention: it keeps the user-stated hard-lines but not the anchors' markers or the receipts; 0.8 is the minimum depth that restores the anchors' markers.*

The AoA's three decision points are orthogonal and must not be collapsed: depth changes **how much of the window rides**; the stub→real ladder changes **which compressor's evidence is load-bearing**; the tool-output mitigation changes **where a receipt lives after the cut**. A depth increase cannot substitute for a recovery path (receipts re-enter only at d ≈ 0.864, past the storm's 0.75 safe-band ceiling).

---

## 2 · DECISION POINT 1 — THE DEPTH SELECTION

**Question:** which threshold — 0.5 (status quo), 0.65 (the field-band / arc-length), or 0.8 (the marker-restoring) — becomes the standing depth?

### 2.1 Alternatives × trade rows

| alternative | trigger (tokens) | est. arc length | retained classes (stub) | deep-end quality-watch | cost / revert | safe-band status |
|---|---|---|---|---|---|---|
| **A1 · 0.5 (status quo)** | 524,288 | ~12h @ 44K/h | user-stated only | none needed — shallowest cut; interpretation near ceiling | no change; baseline | baseline |
| **A2 · 0.65 (field-band)** | ~681K | ~15–16h (+30–40%) | user-stated only — **identical retention to 0.5** | **required** — last ~10% of the band starts to thin; watch the message-buffer's parse seams | one line (one-line rollback) | the storm's recommended near-term door |
| **A3 · 0.8 (marker-restoring)** | ~838,861 (arithmetic: 0.8 × 1,048,576) | ~19h (derived, **not measured** by the storm's table) | user-stated + assistant-prose markers; **tool-output still 0.0** | **heavier** — beyond the storm's 0.75 "ceiling of the safe band"; interpretation 0.88 @ 512K–1M ("recoverable but less influential") | one line, but no measured quality floor at this depth | **outside the storm's safe band** |

Arc-length rows for 0.5/0.65 are the storm's measured table; the 0.8 row is arithmetic only and is labelled as such. The retention rows are recomputed from the ledger. The quality rows are the storm's wave-2 receipts (retrieval 0.989–1.000 at ceiling; no measured quality benefit below ~250K; prefill −19% per depth-doubling, decode −9.5% at 1M).

### 2.2 Recommendation

**A2 (0.65), with the deep-end quality-watch as a condition of adoption — not as a footnote.** Reasons: (a) it is the storm's converged near-term door, exactly "+30–40% length, one-line revertible," matching the operator's "a touch better than baseline" framing; (b) the stub shows no retention loss relative to 0.5 (both are head-only), so the change does not trade away any class the stub currently keeps; (c) what it *does* drop is already carried out-of-window by the fold-downstream architecture — compressed sessions lose nothing load-bearing when the chain's UPDATEs + the thread rows + the anchors hold the seam; (d) 0.8 buys the anchors' markers but not the receipts, so it answers a different question than the one the receipt-class gap poses.

**A1 (0.5) stays as the rollback**, not as a rival: it is the conservative floor if the watch fires. **A3 (0.8) is a conditional upgrade**, gated on the DP2 real-compression run certifying both marker restoration under the real compressor and an acceptable quality floor at depth — and even then it is not a receipt fix.

### 2.3 Counter (the strongest disconfirmation, stated so it can kill the recommendation)

The 0.65 gain may be mostly inert: at 0.65 the added context is middle that the pass compacts, so the extra arc length holds *nothing new* for the classes that matter — if the real compressor's summary-middle is lossy for anchors and receipts, the longer arc is head-only for ~15h instead of ~12h, and the lever is DP3's recovery path, not depth. Reinforcing: the measured interpretation score at the deep end (0.88 @ 512K–1M) means "available" does not equal "influential," so arc length alone cannot carry a move to 0.8 either. **Falsifier:** if the real run shows the added band's facts are recovered at or below the 0.5 baseline, hold at 0.5 and spend the move on DP3.

---

## 3 · DECISION POINT 2 — THE STUB→REAL LADDER'S PATH

**Question:** does the ladder stop at the deterministic map, or does it cross to real-compression runs — and if it crosses, by what methodology and whose card?

### 3.1 Alternatives × trade rows

| alternative | evidence class | cost | determinism / reproducibility | what it can certify | failure mode |
|---|---|---|---|---|---|
| **B1 · deterministic map only** | stub ledger (already reproduced; `cost_total = 0.0`) | zero-billed | exact; every cell re-derives | bounds the claim — "the head+tail model keeps X, drops Y" | cannot certify the real compressor's summary-middle; a stub verdict promoted to "real" is an over-claim |
| **B2 · real-compression runs only** | sessions' `/compress` events (token-billed, real head/tail + real summary-middle) | billed; seat-dependent | nondeterministic; session scheduling (cooldown damper, ~12h cadence) | certifies the finding on the actual cut | no guaranteed `/compress` event to measure; a single run is an anecdote, not a matrix |
| **B3 · hybrid — stub as gate, real as certificate** (recommended) | both, in sequence: stub first (green), real second | stub 0 + real billed (recorded) | stub exact; real bounded by its own receipt | the stub bounds the claim; the real run certifies it — the audit's own §8 framing | real shape may differ from stub shape; that difference must be diagnosed, never forced to match |

### 3.2 Recommendation

**B3, with the real leg shaped as the runner-side card below.** The stub is not a placeholder to be discarded — it is the gate: it already reproduces exactly, it is free, and it owns the boundary knowledge (assistant-prose re-entry d ≈ 0.768; tool-output d ≈ 0.864; reasoning-only never). The real leg exists to answer the one question the stub structurally cannot: does the *actual* head/tail protection + summary-middle preserve the same classes at the same depths? Keep them as two rungs, not two rival methods.

**The runner-side card's shape — `LOSS-LADDER-REAL-20261121`** (the name carried from audit §8):
- **Methodology (three beats, in order):** (1) plant the identical 4 source-types × 3 depths (0.5 / 0.65 / 0.8), 10 seeded episodes, in a **real session**; (2) let the session's real `/compress` event fire — never a simulated cut, never a hand-rolled compressor; (3) **measure after** with the same `ExactMatchJudge` (normalised substring) against the same fixture.
- **Acceptance:** (a) the matrix reproduces shape-wise at the three tested depths (user-stated 1.0 at all three; assistant-prose 0.0 at 0.65 → 1.0 at 0.8; tool-output 0.0 at all three; reasoning-only 0.0 at all three), and (b) `cost_total` is recorded — a billed run with no cost row is not a receipt.
- **Pre-registration before firing:** if the real shape diverges, record the divergence as a *model difference* with the compressor's actual head/tail/summary boundaries — do not tune the stub to agree.

### 3.3 Counter

Real `/compress` runs are billed, nondeterministic, and may be unschedulable (no live session at the cut, cooldown damper, ~12h cadence); the card can legitimately return "no event to measure" — that is a wall, and per the wall clause it must be met with a *constructed* minimal experiment (shrink the fixture to one planted episode, advance to a session already near the threshold, invert the order so the plant precedes the cut) before verdicting "unreproducible." And because the real compressor's summary-middle is not a literal head/tail slice, a shape mismatch is expected and is not a stub failure — forcing a match would fabricate agreement. **Falsifier:** if the real run cannot fire after the wall-construction attempts, the claim stays scope-bounded to the stub; it is not promoted.

---

## 4 · DECISION POINT 3 — THE TOOL-OUTPUT CLASS'S ZERO-AT-EVERY-DEPTH

**Question:** receipts (tool-output) are 0.0 at all three tested depths and re-enter only at d ≈ 0.864 — past the safe band. Which mitigation gets them back?

### 4.1 Alternatives × trade rows (the mitigation matrix)

| alternative | mechanism | what survives the cut | what it costs | native? | gate to count it as a mitigation |
|---|---|---|---|---|---|
| **C1 · one-line tool-signature rows (the scribe)** | transparency-compact's tool-call → one-line signature; the rig's rows/receipts are the same class | the tool's **identity** (call + target) in the retained prose region | the tool's **output** is not in the row — a signature is not a receipt | yes — the rig's row habits | a signature row must name the artifact it refers to, or it is unresolvable after the cut |
| **C2 · the witness registry** | `SCRIBE-WITNESS-REGISTRY.log`'s row shape: `artifact \| hash \| HEAD \| hermes-agent`; transparency-compact's "removed tool-outputs recoverable via a subagent lookup" | a **pointer + integrity hash** to the pre-cut output | a lookup step is required post-compression; the lookup is billed and must actually fire | yes — the registry log already exists | recoverability is measured end-to-end (the fact comes back), never asserted from the registry's existence |
| **C3 · the chain's folds** | append-only segments + thread rows; "if the journal is newer than the checkpoint, the journal wins" | the **substance** outside the compressed window | needs BOTH sides: pre-side (fold on the indicator) and post-side (re-injection on first read) — a half-built defense is orphaned | yes — the memory-chain is the unbounded layer | a canary (an injected known change confirmed by an actual read) proves the post-side fired |
| **C4 · the rig's native transparency-checkpoint** (recommended composite) | checkpoint written in the band (~80%, not at the edge): USER messages + assistant prose verbatim, tool-calls as signatures, tool-outputs recoverable via lookup; missing checkpoint named loudly | the composite: head verbatim + signature rows + a recovery path | success-only path (a compression abort fires no capture); more failsafes = more collision surfaces — do not stack a new fork beside it | **yes — native** | the checkpoint's post-side re-injection is wired and canary-tested |

### 4.2 Recommendation

**C4, instantiated by C1 + C2 + C3 — adopt the native transparency-checkpoint as the composite, not as a fourth competing mechanism.** Reasons: (a) the field's transparency-compact and the rig's own design are the same class (the audit's ARC-LONGEVITY-STORM wave-2 states the correspondence), so there is nothing to import — the rig already runs head-verbatim + signature rows + recoverable tool-outputs + fold-downstream in its own dialect; (b) the data says depth cannot do this job — receipts re-enter only at 0.864, and even 0.8 keeps them at 0.0, so the mitigation must be **out-of-window**, not a deeper cut; (c) each support mechanism covers the others' hole: C1 keeps the call's identity when the output is cut, C2 keeps an integrity-checked pointer to the output, C3 keeps the substance in the durable record and re-injects it. (d) The composite has a built-in honesty gate — a missing checkpoint is *named loudly*, never silent.

**The gate that makes it count:** a recoverability canary. Plant a known tool fact, let a real compression fire, then confirm the fact is returned by the actual post-compression read path. A registry row that exists but was never looked up is not a mitigation.

### 4.3 Counter

The checkpoint is a **success-only** path: on a compression abort (truncated summary / fail-closed rejection) there is no capture, and a subagent lookup is billed — so "recoverable" is a claim that can fail exactly when it is needed. A one-line signature preserves the tool's identity but not its content, so C1 alone would be mistaken for a fix. And the memory doctrine's own warning applies: every extra failsafe is a collision surface, so stacking a bespoke new recovery beside the native checkpoint is the failure shape, not the remedy. **Falsifier:** if the canary's post-side read does not return the planted fact, the composite is half-built and the tool-output class stays at 0.0 for all operative purposes.

---

## 5 · FOLLOW-ON CARDS' SHAPES

Four cards, each with its own two-way door; none fires an upstream or rig-config change without the operator's word.

1. **`LOSS-LADDER-DOCFIX-20261121`** — *the one-file doc correction.* Fix the landing doc's depth-math prose: it says "0.5 keeps the outer 25%, 0.65 the outer 32.5%, 0.8 the outer 40%" while the code's `keep_each = ceil(2082·d/2)` per side retains 50% / 65% / 80% total. State the actual fractions or the formula (the first sentence, "retains the outermost d fraction," is already correct). Acceptance: the corrected doc reproduces the matrix's depths; zero prose/code contradiction. Reversible: doc-only. (Named in audit §2.)
2. **`LOSS-LADDER-REAL-20261121`** — *the runner-side stub→real certificate.* Shape is §3.2: plant → real `/compress` → measure-after; 4×3, 10 seeded episodes, same `ExactMatchJudge`; acceptance = shape-wise reproduction at the three depths + `cost_total` recorded; divergences recorded as model differences. Reversible: a probe artifact, no runtime state. (Named in audit §8.)
3. **`DEPTH-GATE-20261121`** — *the near-term door + the watch.* Adopt 0.65 with the deep-end quality-watch as a named row (parse seams at depth; interpretation 0.88 @ 512K–1M), keep 0.5 as the rollback, record 0.8 as conditional on card 2. Acceptance: the threshold line identified and watched; rollback is one line. **Fire gate:** rig-config changes need the operator's go-ahead — this card stages the decision, it does not flip the line.
4. **`TOOL-RECOVERY-CANARY-20261121`** — *make the checkpoint's post-side real.* Wire C1 signature rows + C2 witness rows + C3 fold-downstream into C4's re-injection path; acceptance: a planted tool fact is returned by the actual post-compression read, and a missing checkpoint is named (never silent). Reversible: row additions + a canary; no new failure fork.

---

## 6 · THE WALL CLAUSE (verbatim)

*a non-reproduction is a QUESTION, not a stop.*

(Verbatim source: `probes/LOSS-LADDER-20261121.md` line 64; re-printed in `audit/LOSS-LADDER-AUDIT-20261121.md` §6. The binding form in the think-tank skill's "THE BRIEF'S ARMAMENT" reads, verbatim: "a non-reproduction is a QUESTION, not a stop — the lane constructs the minimal experiment that moves the wall (advance the date, shrink the fixture, invert the condition, close the window) before it verdicts \"unreproducible\"; a \"green here / can't reproduce\" verdict without the construction is a hypothesis, and the hit-wall-without-a-construction landing means the brief never armed the LP." Applied here to DP2's unschedulable `/compress` and DP3's canary: construct the minimal experiment before verdicting "unreproducible.")

---

## 7 · FOLDS & RECEIPTS

- Retention rows recomputed from `LOSS-LADDER-20261121.json` (`matrix` → 10/10/10, 0/0/10, 0/0/0, 0/0/0 counts; `verified` → the four decimals; `decision_rule` → `all_lb_intact_0.65=false`, `min_depth_keep_load_bearing=null`, `anchor_markers_restored_at_0.8=0.8`, `reasoning_only_zero_at_all_depths=true`).
- Boundary thresholds (d ≈ 0.768 assistant-prose, d ≈ 0.864 tool-output, reasoning-only never) from the audit's §4 boundary probes; they qualify "at every depth" to the three tested depths.
- Arc-length rows (524,288 / ~681K / ~15–16h) from ARC-LONGEVITY-STORM's two-way-door table; the 0.8 row is labelled derived, not measured.
- Deep-end quality rows from ARC-LONGEVITY-STORM wave-2 (retrieval 0.989–1.000; interpretation 0.88 @ 512K–1M; smooth depth profile; no measured benefit below ~250K).
- Witness-row shape from `SCRIBE-WITNESS-REGISTRY.log`; the pre/post-side split, success-only capture, and canary discipline from the `memory-chain` skill's compression protocol.
- No upstream mutation, no config flip, nothing public, RFC quiet; artifact committed before exit; terminal is git-only; commit at the end.

---

*Facimus semper — the alternatives land on the record; the record states its own counter.*
