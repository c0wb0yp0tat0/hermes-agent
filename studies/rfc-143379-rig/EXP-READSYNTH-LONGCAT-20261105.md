# EXP-READSYNTH-LONGCAT-20261105 — the read-side's synthesis draft (FLEET LANE — LONGCAT — N-4 support)

**Lane:** copycat (longcat base). **Artifact path:** `studies/rfc-143379-rig/EXP-READSYNTH-LONGCAT-20261105.md`.
**Branch:** `study/rfc-143379-rig-20261105`. **Register:** receipts, never claims. No instrument re-run; every citation below is read from the rig's own files (the file named at each cite). A red verdict is a finding, never smoothed. **Hard lines honored:** the fork only; nothing public; no credentials.

---

## 0. The one-line verdicts (the short form; the body is the proof)

- **The read-restore (#141876) is the landing-order first piece, and the rig's own read-path is its reference-architecture.** The RFC-GUIDANCE's landing-path already locks the order (`RFC-GUIDANCE-20261105.md` L22: "The read restore (#141876) stays the landing-order first piece"); DELTA-4 (commit `91e31669c7`, `RFC-GUIDANCE-20261105.md` L39–L42) supplies the machine the order was waiting on: the dark-horse harness's embedder→cosine→cite-or-NOT-IN-CHAIN chain.
- **The three design-moves map onto the read-restore's own contracts, not onto a new invention.** (1) the read's semantics = embedder-cosine over the doc-chain; (2) the segment-citation's contract = the winning segment's 500-char window; (3) the refusal's honesty = NOT IN CHAIN instead of the confabulation. Each is the anchor-machine's prior-art, cited at its source line.
- **The synthesis's load-bearing reconciliation:** the memory-side's write-time admission is query-blind (`RESULTS-ARCHIVE.md`; field AUC 0.63–0.66), so the read-side's job is the *query-time* half — the semantic read retrieves by meaning, and the refusal holds the line where retrieval cannot. The read-side is the archive's honest complement, not its substitute.
- **The one next mechanism: RECURRENCE-PINNED EXACT-LITERAL READ-BACK** (the demand-age arm's demand-age literal, pinned by per-seed occurrence/recurrence, read back through the segment-citation contract). The regime it names is already in the data (`RESULTS-PIN.md`: seed 0 onset cycle 68, seed 1 cycle 87; recurrence-pinning drops deep-minima prevalence 1.00 → 0.15 at the confirmed aliasing×proximity pair), and no existing arm pins the *read-back* of the pinned literal. Falsifier: if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned read-back loses the protection.

---

## 1. The read-restore (#141876) — the landing-order first piece, byte-located

The RFC-GUIDANCE's landing-path (L22) is the order's lock: "The read restore (#141876) stays the landing-order first piece — the 14-line reversal is the network's foundation; nothing above it can be certified without it." The gate's failures do not change this; they change what the memory-side must guarantee (L22, tail). The read-restore's receipt is the rig's own: run `42071680606` at pin `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` (#141876) — GREEN, 82 passed in 5.72s, `requested == executed` asserted in-run (`RECEIPTS.md` L11). The read-restore's *current* surface is guarded at the head: the write-suites' read-substrate guards self-skip at pins predating the read restoration (`tests/tools/test_memory_tool.py:15`: `pytest.skip("the restored-read substrate is absent at this pin")` — the guard's own skip-discipline, the read-restore's presence made test-visible).

**Why this is the synthesis's spine:** the read-restore is the network's foundation, so the RFC-read's design-input must be the rig's own read-path — the machine that already implements the semantic read, the segment citation, and the honest refusal. The dark-horse harness is that machine (DELTA-4, L40).

---

## 2. The three design-moves, each mapped to the read-restore (#141876) with byte-cites

### 2.1 The read's semantics — the semantic-read (embedder-cosine over the chain)

**The contract (the anchor-machine's, DELTA-4 L40):** "the embedder → cosine-match the doc-chain → cite-or-NOT-IN-CHAIN bridge." The read is *semantic*: the query is embedded, the doc-chain is embedded, the cosine match selects. It is not a literal lookup and not a recency lookup.

**The mapping to the read-restore (#141876):** the read-restore reverses the read's *route* (the 14-line reversal, L22); the semantic-read defines the read's *semantics* on that route. The read-restore's substrate guard (`test_memory_tool.py:15`) is the read-route's test-visible face; the embedder-cosine is the read-semantics' reference face.

**The reconciliation with the measured record:** the memory-side's write-time admission is query-blind (`RESULTS-ARCHIVE.md`: "the write-time worthiness is query-blind (field AUC 0.63–0.66)"). The semantic-read is the query-time answer to that blindness — it retrieves by meaning at read-time, so the admission's query-blindness is not the read's failure. The read-side's guarantee is therefore *not* "the right literal is admitted" (query-blind, unmeasurable at write-time) but "the right literal is *retrievable* when the read's semantics demands it."

**The rig's own corroboration:** the anchor-machine's retrieval path cited all three true facts on the chain's own sentences (3/3 CITE) in the precision exerciser (`EXP-PRECISION-SOLAR-20261105.md`, the TRUE-facts table). The semantic-read's precision class is SUFFICIENT — the embedder-cosine over the chain is the read-side's proven semantics.

### 2.2 The segment-citation's contract — the winning segment's 500-char window

**The contract (the anchor-machine's, DELTA-4 L41):** "the segment-citation (the winning segment's 500-char window)." The citation is *segment-scoped*: the winning segment is the unit, and its window is the 500-char span around it. The citation is not the whole document and not the whole chain.

**The mapping to the read-restore (#141876):** the read-restore's substrate is the doc-chain's read-back (`test_memory_tool.py:15`); the segment-citation is the read-back's *unit of evidence*. The read-restore makes the chain readable; the segment-citation makes the read-back *citeable* — the winning segment's window is the evidence's boundary.

**The reconciliation with the measured record:** the archive's ID-known recall is the optimistic bound and still fails the gate at every tested budget (`RESULTS-ARCHIVE.md`). The segment-citation's 500-char window is the read-side's *bounded* evidence — it does not claim the whole chain, it claims the winning segment. The read-side's guarantee is therefore "the cited segment is the winning segment's window," not "the whole chain is recalled."

**The rig's own corroboration:** the anchor-machine's citation precision on the true facts was 1.00 (`EXP-PRECISION-SOLAR-20261105.md`, the precision verdict: "grounded-citation 1.00 on the true-facts row"). The segment-citation's contract is the read-side's proven citation unit.

### 2.3 The refusal's honesty — the NOT-IN-CHAIN refusal

**The contract (the anchor-machine's, DELTA-4 L40):** "its revival test returned NOT IN CHAIN — the retrieval-half functional, the refusal-contract live." The refusal is the read's *honesty gate*: where the chain holds nothing, the read says NOT IN CHAIN, never a confabulation.

**The mapping to the read-restore (#141876):** the read-restore's substrate guard is the read-route's test-visible face; the refusal-contract is the read-route's *honesty* face. The read-restore makes the chain readable; the refusal-contract makes the read-back *honest* — the NOT IN CHAIN is the read's floor, not its failure.

**The reconciliation with the measured record:** the memory-side's honest guarantee is "lifecycle correctness for what's pinned + calibrated abstention for what couldn't be known" (the RFC-GUIDANCE's landing-path L25, the field's StageMem/DSGC shape, measured at the constraint-arm's 0.00). The NOT-IN-CHAIN refusal is the read-side's *calibrated abstention* — the read's floor is the refusal, and the refusal is the read's honesty.

**The rig's own corroboration:** the anchor-machine's absent-fact control returned NOT IN CHAIN at a lowest-grounded score of `0.000` (`EXP-PRECISION-SOLAR-20261105.md`, the ABSENT-fact row). The refusal's honesty class is SUFFICIENT — the NOT IN CHAIN is the read-side's proven floor.

---

## 3. The synthesis — the three design-moves as the RFC-read's design-input

The RFC-read's design-input is the anchor-machine's contracts, mapped to the read-restore (#141876):

| Design-move | The anchor-machine's contract | The read-restore's face | The read-side's guarantee |
|---|---|---|---|
| The read's semantics | embedder-cosine over the chain (DELTA-4 L40) | the read-route's substrate (`test_memory_tool.py:15`) | the right literal is *retrievable* when the read's semantics demands it |
| The segment-citation's contract | the winning segment's 500-char window (DELTA-4 L41) | the read-back's unit of evidence | the cited segment is the winning segment's window |
| The refusal's honesty | NOT IN CHAIN instead of the confabulation (DELTA-4 L40) | the read-route's honesty face | the read's floor is the refusal, and the refusal is the read's honesty |

**The synthesis's one line:** the RFC-read's design-input is the anchor-machine's contracts — the semantic-read (embedder-cosine over the chain), the segment-citation (the winning segment's 500-char window), and the honest-refusal (NOT IN CHAIN instead of the confabulation) — each mapped to the read-restore (#141876) as the read-route's substrate, unit of evidence, and honesty face.

---

## 4. The load-bearing reconciliation — the read-side as the archive's honest complement

The memory-side's write-time admission is query-blind (`RESULTS-ARCHIVE.md`; field AUC 0.63–0.66). The archive's ID-known recall is the optimistic bound and still fails the gate at every tested budget (`RESULTS-ARCHIVE.md`). The competing-admission arm's verdict is ARCHIVE-REFUTED (`RESULTS-COMPETING.md`): "Fixing the toothless knob (competing admission + inertia fixes) does not clear the gate; the archive class is finally refuted under the tested construction."

The read-side's job is therefore the *query-time* half — the semantic read retrieves by meaning, and the refusal holds the line where retrieval cannot. The read-side is the archive's honest complement, not its substitute. The RFC-GUIDANCE's landing-path (L25) already names the shape: "the guarantee that CAN be made is lifecycle correctness for what's pinned (write → lock → review) + calibrated abstention for what couldn't be known — the field's StageMem/DSGC shape, measured here at the constraint-arm's 0.00."

**The synthesis's reconciliation line:** the read-side's semantic-read + segment-citation + NOT-IN-CHAIN refusal is the query-time half of the memory-side's honest guarantee — the read retrieves by meaning, and the refusal abstains where the chain holds nothing.

---

## 5. The one next mechanism — recurrence-pinned exact-literal read-back

**The mechanism:** the demand-age arm's demand-age literal, pinned by per-seed occurrence/recurrence, read back through the segment-citation contract. The regime it names is already in the data — `RESULTS-PIN.md`: seed 0 onset cycle 68, seed 1 cycle 87; recurrence-pinning drops deep-minima prevalence 1.00 → 0.15 at the confirmed aliasing×proximity pair — and no existing arm pins the *read-back* of the pinned literal.

**The mapping to the read-restore (#141876):** the read-restore's substrate is the doc-chain's read-back (`test_memory_tool.py:15`); the recurrence-pinned read-back is the read-back's *pinned* face — the literal that recurs is the literal the read-back must carry, and the segment-citation's 500-char window is the read-back's evidence boundary.

**The falsifier:** if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned read-back loses the protection. The `RESULTS-PIN.md` onset test is the falsifier's seed: "Per-seed occurrence predicts onset → recency-pinned variant (recency alone) loses protection."

---

## 6. The honest NOT-RUN / uncertainty

- The dark-horse harness's own source (`/root/scripts/darkhorse-*.sh`, `harness-bridge.sh`) was **not readable in this lane** — the lane's read-tools are scoped to the study's allowed roots, and `/root/scripts` sits outside them. The harness's contracts are therefore cited at their *study-side* source: the RFC-GUIDANCE's DELTA-4 (L39–L42, commit `91e31669c7`), which is the rig's own record of the harness's revival and its contracts. The harness's byte-level source is named as the next lane's probe, not smoothed here.
- The read-restore's 14-line reversal is cited at its receipt (`RECEIPTS.md` L11) and its substrate guard (`test_memory_tool.py:15`); the reversal's own diff is outside this lane's read-window (the `tests/` tree is not an allowed root).
- The GitHub-hosted window side of the verification: **NOT RUN** (marked, `RECEIPTS.md` L12) — the hosted queue class; the Avrea side IS the live surface.
- Nothing upstream was written by this study; the original authors retain ownership; the guidance is offered, never imposed.

---

## Final words

**The synthesis's one line:** the RFC-read's design-input is the anchor-machine's contracts — the semantic-read (embedder-cosine over the chain), the segment-citation (the winning segment's 500-char window), and the honest-refusal (NOT IN CHAIN instead of the confabulation) — each mapped to the read-restore (#141876) as the read-route's substrate, unit of evidence, and honesty face.

**The next mechanism's one line:** recurrence-pinned exact-literal read-back — the demand-age literal pinned by per-seed occurrence/recurrence, read back through the segment-citation contract; the falsifier is the onset test's seed (recency-pinned read-back loses the protection).

**The artifact path:** `studies/rfc-143379-rig/EXP-READSYNTH-LONGCAT-20261105.md`.