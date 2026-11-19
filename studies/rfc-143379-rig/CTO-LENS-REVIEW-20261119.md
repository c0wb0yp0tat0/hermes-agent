# CTO-LENS-REVIEW-20261119 — the operator's final look over the composed fire

*Lane: CTO-LENS · Envelope: LUNA-MIDDLEWARE-MISSION-20261119.md + RELOAD-COMPOSE-20261119.md. Gate: "nothing public without the user's word." Review only; no service changes; no `/root/.hermes` writes. Receipts stamped READ 2026-11-19; ABSENT stays ABSENT + named.*

## 1 · SUSTAINABILITY AUDIT (seam → RECEIPT → FIX)

**Seat.** RECEIPT: compose §2 roster — longcat primary, deepseek fallback; qwen4-max/hy4/solar/stepfun never assumed; UPDATE b1 — E3 landed longcat (`481f4eaf15`); qwen4-max 403-walled at every probe, did NOT land. The roster is live but never names the mission's seat: the demonstrating seat is Luna (gpt-6-luna) [master §0; L-1 header; L-2 §3], the roster names longcat/deepseek — Luna absent. **S6 (blocker-potential): seat-roster vs mission-seat.** FIX: name the reader→route mapping as a roster row; dispatch-probe Luna's route at step 0; unreachable + no mapping → NOT-READY on seat grounds. L4-S1's "qwen4-max landed" is stale (UPDATE b1 supersedes); FIX: correct the line. **Mid-arm 403 has no rule** — INCONCLUSIVE omits seat loss; a partial arm reads as data. FIX: arm-level seat-rescue rule (A2); row resets per surface (429 rule UNVERIFIED [L-2 §3]).

**Economics.** RECEIPT: compose §2 — 120 exec = $56.04 shadow, 56% of the $100 cap, cash $0; L-2 §1–2. Survives its own spend. **S1:** per-cell ±15pp needs n_cell ≥ 40; at 40/arm the 4 EHQ cells get ~10 each → per-cell claims not reportable in-gate; the extension (160 nominal/arm ≈ $224.16) is post-CERTIFY, "uncapped by the gate" [L2-D3] — uncapped-by-gate ≠ uncapped-by-mandate (2.24× cap). FIX: name the extension's own ceiling (≤$250 shadow) + fresh operator nod above; row as sensitivity. **S5 (real or phrase?):** L-2 §1 marks the governor surcharge UNVERIFIED; it is local/deterministic, no extra model tokens → ≈$0 by construction; "measured at enqueue" is a phrase without a meter. FIX: wire the per-episode governor step/token count into the ledger cost row; any paid step named + justified [L-2 §4.4]; else restate "$0 by construction; deviation rows."

**Machinery.** RECEIPT: compose §3 S4 — six-class frozen list vs `judge_control_gate.py`/`release_point_gate.py`; reconcile verbatim; mismatch = QUESTION, never a stop. The list's verbatim text is **ABSENT** from my receipts (L-4 not in the review list) — named, not hunted. FIX: A1's dry-run prints both lists side by side. **S7 (numerator conflict):** L-1 §2 abstention = (R+H+E)/200; L4-D1 splits C5a `NO_OUTPUT` (empty_reason harness|seat|unknown) from C5b `REFUSED` and excludes C5a — the headline's numerator disagrees across artifacts. FIX: reconcile verbatim — (R+H)/200 headline, E a separate data-quality row (E-included as priced sensitivity); wire empty_reason. **Audience field:** L4-S2 wired `audience` internal|staged|public into classifier + flags; probe never emits public. FIX: assert audience=internal at dispatch + no-public-emit guard. **S8:** INCONCLUSIVE iff mean(F3b) < 1 [L1-D3] — one missed write-time assert nulls the run; a harness bug would null the leg. FIX: split harness-miss from middleware-miss (reason field), or trigger at ≥0.95 with misses rowed.

**Honesty grid.** reported-vs-verified ADOPT (cap = reported-plan; operator supplies the exact quote post-data) [L3-D1; L-3 §3.2]; no-overclaim ceiling ADOPT (episodic claim only; unqualified "agnostic" unused) [L3-D3; L-1 §4]. Classifier false-positive guards: PATTERN-FREEZE + adversarial set incl. a gate-echo that must score ANSWERED; ties scored H (conservative), all-matches log carries the tie [L4-D2; compose §2]. Gap: set size/coverage unnamed; no guard for the reverse error (refusal-as-hedge / hedge-as-answer). FIX: name coverage (N, refreshed per seat) + log the confusion matrix (folds into A3).

**Report-back gate.** GATE-PUBLIC = operator's explicit word only; probe never emits public; gist URL to operator, never MEDIA [L3-D4; L-3 §7; master §5]. Holds. Dependency: draft P1 is the public post's verbatim quote, supplied post-data [L3-D1] — **ABSENT** until then; tone-check cannot complete without it. FIX: name the quote a gated input; P1 a placeholder; gate holds.

## 2 · MAX-VALUE-ADD (≤3)

**A1 · Pre-fire wiring dry-run (top add).** WHY: S4/S5/S6/S7/S8 are phrases until machine-checked; a 3-episode/arm smoke run on the live roster prints the classifier's C5a/C5b + audience field, F1/F2 rows, F3b assert, cache-hit, the governor's step/token meter, and the seat route — every seam becomes a receipt before the 120-exec fire. COST ~9 exec ≈ $4.2 shadow ($0 cash). SLOT step 0, after roster re-survey, before arm A.
**A2 · Arm-level seat-rescue rule.** WHY: four walled seats + UNVERIFIED 429 rule; a mid-arm 403 otherwise yields a partial arm read as data. COST: ledger field (seat, episode range, reset count) + dispatch probe per arm. SLOT: run-ledger spec.
**A3 · Abstention-attribution artifact.** WHY: the headline is the abstention delta; without per-cell counts + adversarial confusion matrix + empty_reason rows it is a number without a receipt — the report-back's receipted rule needs it; resolves S7 by showing both numerators. COST: a fold of existing classifier output. SLOT: verdict evidence pack.

## 3 · FIRE-READINESS VERDICT

**VERDICT: READY-WITH-NAMED-SEAMS** — holds only if A1 lands as step 0.
- Economics survive: 120 exec = $56.04 ≤ $100 cap; cash $0 [compose §2; L-2 §2].
- Seams disposable in-window: S1 ceiling+nod; S4 reconcile; S5 meter; S7 numerator; S8 reason-field — ledger/spec edits, no re-design [compose §3; L4-D1; L1-D3].
- Machinery unverified but dry-runnable: S4/S5/S6/S8 → A1 [compose §3; L-2 §1].
- Honesty holds: GATE-PUBLIC = operator's word; reported-vs-verified; episodic ceiling [L-3 §7; L3-D1/D3/D4].
- Blocker-potential: the mission's named seat (Luna) is absent from the binding roster; if A1's probe cannot reach it → NOT-READY on seat grounds [master §0; compose §2].

**The operator's gift:** The fire is sound and cheap — 120 runs, $56 of shadow, no cash — and its seams are real but small. Two things before you pull the trigger: prove the seat (the mission says Luna, the roster says longcat — name which one the arms actually ride, and probe it first), and prove the classifier counts what you think (the empty-output split moves the abstention headline). Run the nine-episode dry-run first; it costs less than a coffee and turns every seam from a phrase into a receipt. Then fire.

## 4 · Compose-check (8/8) + loop state

| Step | State | Evidence |
|---|---|---|
| deconstruct | FIRED | claim + nuance + five signals + boundaries; two gates named |
| sense | FIRED | middleware quantity, seat as instrument; hardest case = agnostic |
| choose | FIRED | three arms + 17-entry ledger adjudicated by evidence |
| calibrate | FIRED | n_cell=40, $0.467/exec, $100 cap, 214-exec ceiling |
| probe | FIRED | decision rule pre-committed + F3b trigger audited |
| review | FIRED | this audit; stranger re-read + pushbacks remain L-3's loop |
| record | FIRED | this artifact + lane landing commit; gate held |
| compose-check | FIRED | plan → land → enrich → synthesize → verdict → fire → negentropy |

**LOOP-STATE: CONTINUE + THE FIRE** (step 0 = A1 dry-run; A2/A3 land in the ledger spec).
**NO NEXT-LAUNCH:** none named — the head's deep-look follows this landing; the head fires. Nothing public without the user's word.