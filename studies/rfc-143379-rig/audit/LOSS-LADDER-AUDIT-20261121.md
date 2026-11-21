# LOSS-LADDER-AUDIT-20261121 — assess + design + probe verdicts (retention matrix)

TEAM: ACES (the independence audit rotation)
MISSION: the LOSS-LADDER landing audit — Assess / Design / Probe verdicts on
        commit 08b15cac75 (the retention matrix's ledger, the landing doc, the generator)
EVIDENCE (cold-read at git show 08b15cac75:path):
        probes/LOSS-LADDER-20261121.json  (retention matrix's ledger) — the claim
        probes/LOSS-LADDER-20261121.md    (landing doc)           — the claim's prose
        probes/loss_ladder.py             (generator)            — the zero-billed stub class
BRANCH: study/rfc-143379-rig-20261105 · RFC quiet · HEAD 08b15cac75
ARTIFACT (absolute path): /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/audit/LOSS-LADDER-AUDIT-20261121.md

---

## 0 · THE VERDICT (one breath)

The LOSS-LADDER landing's claim is **valid for the stub it names**: re-running the
generator reproduces the retention matrix EXACTLY, and that matrix supports every
element of the verdict ("0.65 is NOT load-bearing; 0.8 restores the anchors' markers;
receipts (tool-output) + reasoning-only stay 0.0 at every depth"). The three verdicts
below (Assess / Design / Probe) are each receipted on the reproduction run.

The landing doc's **depth-math prose is internally inconsistent with the code** (it
states the compression retains "the outermost d fraction" but then quantifies
0.5→25% / 0.65→32.5% / 0.8→40% instead of the code's actual 50% / 65% / 80%).
Read literally, the 40% figure would NOT restore the anchors' markers at 0.8. The
matrix and verdict are unaffected (the block placement dominates), but the doc must
be corrected before the landing is promoted. See ASSESS §5 and the boundary probes.

Wall clause (verbatim): *a non-reproduction is a QUESTION, not a stop.*

---

## 1 · THE FILES (cold-read, at 08b15cac75)

### 1.1 retention ledger — LOSS-LADDER-20261121.json
- matrix (per source-type × depth, 10 episodes each): user-stated 1/1/1, assistant-prose
  0/0/1, tool-output 0/0/0, reasoning-only 0/0/0.
- verified (averaged): 0.5→{1.0,0.0,0.0,0.0}; 0.65→{1.0,0.0,0.0,0.0}; 0.8→{1.0,1.0,0.0,0.0}.
- decision_rule: load_bearing=[user-stated, assistant-prose, tool-output]; all_lb_intact_0.65=false;
  anchor_markers_restored_at_0.8=0.8; reasoning_only_zero_at_all_depths=true.
- per_episode: 10 rows (episode 0-9, four facts each, retained per depth).
- cost_total=0.0; seed-derived SHA-256 episodes (deterministic); additive (appends to ledger).

### 1.2 landing doc — LOSS-LADDER-20261121.md
- Retention table (0.5 / 0.65 / 0.8) identical to the ledger.
- Verdict: "0.65 is NOT load-bearing ... 0.8 restores the anchors' markers; receipts and
  reasoning-only stay 0.0 at every depth."
- Mirrors ContextCompressor: at depth d retains outermost d fraction (head+tail), compacts middle.
- Wall clause (verbatim, line 64): "*a non-reproduction is a QUESTION, not a stop.*"

### 1.3 generator — loss_ladder.py
- TWEAK/NATIVE battery class: 4 source-types, 3 depths, 10 episodes, fixed 2082-char window.
- Blocks: user-stated [0,64) head; filler1 [64,700); assistant-prose [700,800) anchors' markers;
  filler2 [800,900); tool-output [900,1100) receipts; filler3 [1100,1249); tail [1249,2082).
- compress_window(depth d): keep_each = ceil(2082·d/2) per side; retained = window[:keep_each] +
  window[2082-keep_each:]  →  total retained ≈ 2082·d (i.e. 50% / 65% / 80% at 0.5/0.65/0.8).
- ExactMatchJudge: normalised gold fact is a substring of normalised retained window.

---

## 2 · ASSESS verdict

THE QUESTION IS THE RIGHT ONE, and the matrix's scoping MATCHES the claim's.

- The question framed is the correct one: which depth keeps the load-bearing classes
  intact? The claim names those classes explicitly (user-stated hard-lines + assistant-
  prose anchors' markers + tool-output receipts), and the matrix scores exactly those.
- The ledger's OWN honesty is the deciding point: the seat is "STUB reader + deterministic
  stub compression pass (zero-billed)". The matrix measures retention under that stub, and
  the claim is explicitly scoped to that stub ("the rig's own seams — the TWEAK/NATIVE
  battery class"). The scoping matches the claim: the matrix is not presented as a real-
  compressor measurement; it is a stub model.
- However, the landing doc overreaches slightly in prose: its depth-math enumeration
  (0.5→25%, 0.65→32.5%, 0.8→40%) is half the code's actual retention (50% / 65% / 80%).
  The code's keep_each = ceil(2082·d/2) applies the "/2" per SIDE (head and tail), so total
  retained = d (not d/2). Read literally, the doc's 40% figure would not restore the
  anchors' markers at 0.8 — contradicting the very verdict it accompanies. The doc must be
  corrected to state the actual fractions (or the formula). This is a documentation error,
  not a content error: the matrix and verdict come from the code, which reproduces.
- Net ASSESS: the question is right; the matrix is correctly scoped to the claim's stake;
  one documentation defect (the depth-math prose) must be fixed. Verdict: MATCH (with a
  named doc fix).

### 2.1 ASSESS — matrix scoping vs claim, receipted

| Claim element | Matrix scope | Scoping verdict |
|---|---|---|
| "0.65 is NOT load-bearing" | scores 0.65 on 4 source-types | MATCH (matrix includes 0.65) |
| "0.8 restores the anchors' markers" | assistant-prose scored at 0.8 | MATCH (1.0 at 0.8) |
| "receipts stay 0.0 at every depth" | tool-output at 0.5/0.65/0.8 | MATCH (0.0 at all three) |
| "reasoning-only stays 0.0 at every depth" | reasoning-only at 0.5/0.65/0.8 | MATCH (0.0 at all three) |
| "use 10 eps/cell" | n_per_depth=10, 10 episodes | MATCH (10 episodes logged) |

---

## 3 · DESIGN verdict

The battery's design is sound for its stated purpose (replicate the field's planted-fact
retention protocol on a zero-billed deterministic stub). All four design choices are
consistent and reproducible:

- **10 eps/cell** — n_per_depth=10, 10 episodes logged; deterministic so the curve is
  identical episode to episode (no sampling variance, no multiple-comparison problem).
- **Depths 0.5/0.65/0.8** — the seat's window fractions; 0.65 is the deployed depth, 0.8
  is the "restore" probe. Consistent with the claim's fractions. ✓
- **Outermost-depth-fraction-retained pass** — compress_window keeps head+tail (mirror of
  ContextCompressor's head/tail+summary), compacts the middle. Mirrors the rig's compressor. ✓
- **ExactMatchJudge (normalised substring)** — F3 canonical grader; a gold fact must appear
  in the retained window. A fair exact-match test for retained-facts. ✓

One design note (not a defect, but a boundary worth recording): the anchor-marker block
[700,800) is positioned so that 0.8 (keep_each=833) retains it but 0.65 (677) does not.
Because the block starts at 700, assistant-prose actually re-enters at d ≈ 0.768
(keep_each ≥ 800); and because tool-output starts at 900, it re-enters only at d > 899/1041
≈ 0.864. So "receipts 0.0 at every depth" is exactly-true for {0.5,0.65,0.8} but the
boundary is sharp — the claim's "every depth" is bounded by the tested depths. Good to
record as a boundary note, not a flaw; the stub says exactly what it says.

Net DESIGN: sound for the stub. Verdict: SOUND.

---

## 4 · PROBE verdict

The generator re-ran under the stub (zero-billed: STUB reader + deterministic stub
compression pass, cost_total 0.0). The matrix REPRODUCED EXACTLY.

Reproduction receipt (regenerated ledger vs original, identical after stripping the
runtime timestamp `ts`):

| depth | user-stated | assistant-prose | tool-output | reasoning-only | claim check |
|---|---|---|---|---|---|
| 0.5 | 1.0 | 0.0 | 0.0 | 0.0 | head-only ✓ |
| 0.65 | 1.0 | 0.0 | 0.0 | 0.0 | not load-bearing ✓ |
| 0.8 | 1.0 | 1.0 | 0.0 | 0.0 | restores markers ✓ |

- VERDICT REPRODUCTION: MATCHED (verified against the JSON ledger, all 10 episodes/six
  source-type×depth cells, plus the decision_rule fields all_lb_intact_0.65=false,
  anchor_markers_restored_at_0.8=0.8).
- cost_total=0.0 (zero-billed stub class) — the run is non-billing; the reproduction is
  deterministic and free.
- Boundary probes (documenting the block-placement thresholds):
  - assistant-prose [700,800) → retained once keep_each ≥ 800, i.e. d ≈ 0.768.
  - tool-output [900,1100) → retained once keep_each ≥ 900, i.e. d > 899/1041 ≈ 0.864.
  - reasoning-only → never in the window (the reasoning field is not part of the
    window), so 0.0 at ALL depths, not just the tested three.

Net PROBE: the matrix reproduces; the verdict's validity holds for the stub at the
tested depths; one boundary note (tool-output re-entry ≈ 0.864) qualifies the
"every depth" phrasing. Verdict: VALID (scope-bounded to {0.5, 0.65, 0.8}).

---

## 5 · THE VERDICT'S VALIDITY (does the matrix support the claim?)

| Verdict clause | Matrix support | Valid? |
|---|---|---|
| "0.65 is NOT load-bearing" | assistant-prose 0.0 + tool-output 0.0 at 0.65; only user-stated 1.0 | YES |
| "0.8 restores the anchors' markers" | assistant-prose 1.0 at 0.8 | YES |
| "receipts (tool-output) 0.0 at every depth" | tool-output 0.0 at 0.5/0.65/0.8 | YES (scoped to tested depths; re-entry ≈ 0.864) |
| "reasoning-only 0.0 at every depth" | reasoning-only 0.0 at 0.5/0.65/0.8 | YES (reasoning trace outside window) |
| "0.65 rides on head-only retention" | user-stated 1.0 at 0.5/0.65; assistant-prose 0.0 at 0.65 | YES |

Every clause of the verdict is supported by the reproduced matrix. The claim is
accurate for the stub it names and at the depths it names.

---

## 6 · THE WALL CLAUSE (verbatim)

*a non-reproduction is a QUESTION, not a stop.*

(Verified in two places: LOSS-LADDER-20261121.md line 64, and the ledger's decision_rule
"rule" + verdict fields — the probe did not stop; it reproduced, which the clause itself
prescribes.)

---

## 7 · FOLDS & RECEIPTS

- Every matrix cell reproduces from the code (10 episodes × 4 source-types × 3 depths =
  120 booleans; averaged to the verified table above).
- The ledger's `ts` was refreshed by the reproduction run; the matrix is unchanged.
- The block placement drives the boundary: keep_each = ceil(2082·d/2) per side; the
  assistant-prose/tool-output blocks sit in the compacted middle at 0.65 but in the head
  at 0.8.
- The doc's depth-math prose (25%/32.5%/40%) is half the code's actual fractions
  (50%/65%/80%) — a documentation fix required (see §2).
- Replication of the landing doc's own depth-math would NOT restore the anchors at 0.8;
  only the code's actual compression does. The doc's initial sentence ("retains the
  outermost d fraction") is correct; the "So" clause is not.

---

## 8 · THE STUB-TO-REAL LADDER (follow-on, named)

The stub's curve is a lower-bound model of the rig's real ContextCompressor (zero-billed,
deterministic, head+tail-protected, middle compacted). The follow-on that names the
bridge:

**LOSS-LADDER-REAL-20261121** — replay the identical 4 source-types × 3 depths
(0.5 / 0.65 / 0.8) on the rig's ACTUAL ContextCompressor (token-billed, real head/tail
protection + real summary-middle), with the sameExactMatchJudge and the same 10-episode
seeded fixture. Acceptance: (a) the matrix reproduces shape-wise (user-stated 1.0 at all
three; assistant-prose 0.0 at 0.65 → 1.0 at 0.8; tool-output 0.0 at all three; reasoning-
only 0.0 at all three) at the three tested depths, and (b) records cost_total. This is the
stub-to-real ladder: the stub bounds the claim; the real run certifies it.

---

## 9 · HARD LINES

nothing public · RFC quiet (reads only) · no installs · no self-fire · zero-billed stub
reproduction (cost_total 0.0) · artifact only, committed before exit · no git checkout --
/ rm -rf / stash · terminal is git-only · commit at the end.
