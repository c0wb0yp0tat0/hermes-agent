# S6 RE-APEX — NAMING-CONVENTION NOTE
Receiver: step (WRITE-class)

## 1. Identified families (artifact-name prefixes)

| Family | Observed tokens | Role |
|--------|----------------|------|
| `RESULTS-*` | RESULTS-ARCHIVE, RESULTS-AUDIT, RESULTS-COMPETE, RESULTS-COMPETING, RESULTS-COMPOSE, RESULTS-CONSTRAINTS, RESULTS-CROSSINGS, RESULTS-FORMATPIN, RESULTS-INTENT, RESULTS-RESERVE, RESULTS-RETENTION, RESULTS-SEAMFIX, RESULTS-SEAMMECH, RESULTS-ANCHOR, RESULTS-ALIASING, RESULTS-AGE, RESULTS-PORTABILITY, RESULTS-RECITE | Research output / probe outcomes |
| `NEGENTROPY-SWEEP*` | NEGENTROPY-SWEEP-20261107-* | Sweep/iteration records |
| `LENS-*` | LENS-OUTCOME, LENS-ESSENCE, LENS-ARC | Epistemic/lens framing notes |
| `NEXT-SHIFT-PLAN*` | NEXT-SHIFT-PLAN, NEXT-SHIFT-PLAN-AOA | Plan hand-off |
| `GOVERNANCE-LENS*` | GOVERNANCE-LENS-E2E | Governance lens |
| `ACES-*` | ACES-REVIEW, ACES-AUDIT, ACES-REVIEW-C4 | ACES review artifacts |
| `IMPROVEMENTS*` | IMPROVEMENTS-W1, IMPROVEMENTS-1 | Improvement drafts |
| `EXP-*` | EXP-AOA, EXP-PROBE-BANKS-CERT | Experiment probes |
| `EVAL-*` | EVAL-LADDER-BATTERY | Eval artifacts |
| `CITATION-*` | CITATION-CANON | Citation canon |
| `NETWORK-*` | NETWORK-LINE-ANCHORCHAIN | Network model |
| `FLEET-CYCLE*` | FLEET-CYCLE-BODY | Fleet cycle |
| `ENRICHMENT-*` | ENRICHMENT-AUDIT | Enrichment audit |
| `HITL-*` | HITL-GAINS-SKEPTIC, HITL-GAINS-DRAFT | Human-in-the-loop gains |
| `WAVE3-*` | WAVE3-UNIFIED-FOLD | Wave 3 fold |
| `KIT-*` | KIT-SYNTH-2 | Kit synthesis |
| `VALUE-ADD-*` | VALUE-ADD-SYNTH | Value synthesis |
| `THE-UNDERSTANDING*` | THE-UNDERSTANDING | Understanding notes |
| `CROSS-READ*` | CROSS-READ | Cross-reading |
| `ALLPRS-READ*` | ALLPRS-READ | All-participants read |
| `NIGHTSHIFT*` | NIGHTSHIFT-HANDOFF, NIGHTSHIFT-LONGFORM | Shift hand-off |
| `ONESHOT-*` | ONESHOT-OPERATOR-COMMENT | One-shot comments |
| `MINES-*` | MINES | Mines |
| `SWAP-*` | SWAP-A-ADVANCE-A | Swap advance |
| `FINISH-LINE*` | FINISH-LINE-REPLICATION | Replication script |
| `TRUSTER-*` | TRUSTER-E2E | Truster E2E |
| `READ-FIX*` | READ-FIX-COMMENT-STAGED | Read-fix comment |

## 2. Exceptions / variants

- `.sentinel` suffix: files ending in `.md.sentinel` are gating/status markers, not plain notes (e.g., ACES-REVIEW-C4-20261107.md.sentinel, LENS-ESSENCE-20261108.md.sentinel).
- `.py` scripts: Python utilities that share prefix space but are code, not markdown notes.
- `CROSS-READ-20261107.md`: family is ad-hoc; date suffix without a more granular qualifier.
- `THE-UNDERSTANDING-20261107.md`: underscore prefix family is singular and semantic, not systematic.
- `tmp-artifacts/` location: re-apex artifacts live under `tmp-artifacts/`, not the study root.

## 3. Rename-plan scope

- **In scope**: regularize date-suffix formatting to `YYYYMMDD` consistently (some already are, e.g., 20261106; others use hyphens like 20261107, and some embed HHMM like 20261108-1603).
- **In scope**: decide `.sentinel` discipline — either promote to `.md` with content, or keep `.sentinel` and document as a meta-artifact family.
- **In scope**: map ad-hoc prefixes (`THE-UNDERSTANDING`, `CROSS-READ`, `ALLPRS-READ`, `MINES`) to either an existing family or retire them into an `ODD-*` family if they remain non-standard.
- **Out of scope**: renaming `.py` scripts; those are tools, not notes.
- **Out of scope**: renaming `rungs/` and `krecency/` fixture/data files unless they become top-level study artifacts.

## 4. Receiver check (read-back)

- **Check A**: Do all current top-level `.md` files map to one of the families listed above or to the exceptions in §2?  
  *Receiver should enumerate any unmatched files.*
- **Check B**: Are `.sentinel` files exclusively gating artifacts and never contain divergent prose?  
  *Receiver should spot-check for stray content.*
- **Check C**: Does the date-suffix variance (`-` vs no separator, with/without HHMM) exceed the rename-plan tolerance?  
  *Receiver should count variants.*
