# MASTER-TEAM-M3-20261119.md — the M3 adoption sprint (2026-11-19)

Workbench for **M3 — THE GOVERNANCE SEAMS ARE UN-ADOPTED**. Verb: **adopt**. Two named probes: **(A)** the release-point rule, wired into the rig's compaction writes; **(B)** the 70% law, wired as the fire-decision gate. Each names its hook point, its reversibility, its rollback.

## 0. The gate, verbatim

> "the gate: nothing public without the user's word." — RFC QUIET. Nothing moves public/permanent until the user speaks.

## 1. Place in the sequence

Master step 3, alongside M2's synchronize, after M1's certify. Probe A rides compaction episodes M1's battery measures; Probe B's decision record lands on M2's single surface.

## 2. Probe A — the release-point rule, wired

Rule, verbatim: *"release a block only when the teacher can cite the event that ended its use."*

**Wiring points.** The check lands at each release decision in the rig's three-deep compaction path — no new battery:
- `hermes_state_compression.py` — candidate selection: require the field `ending_event` (pointer to the last consumer event) before a block advances.
- `hermes_state_mutation_compress.py` — mutation/summary write: an uncited candidate is deferred, not dropped; deferral + missing citation logged.
- `hermes_bootstrap.py` — archive/rebuild read-back: deferred blocks stay byte-intact (archive-before-stub), so a deferral is a hold, never a loss.
- Existing battery `tests/e2e/core/compaction/*` gains ONE arm — the citation arm — replaying released blocks against the field's non-re-observable-fact class.

**The check.** Citation = named event id + consuming turn. No citation ⇒ held + logged with reason. Provenance-origin classification and the K-recency window stay eligibility inputs; the citation is the new gate on top.
**Reversibility.** `shadow` (log would-be releases; zero behavior change) → `enforce` (defer uncited); flag-flips on the existing path.
**Rollback.** Flip back; held blocks re-admit next cycle (nothing destroyed). Worst case: latency, not loss.
**Cost.** No new billed class; rides compaction episodes already run (API-class pennies incurred). No arithmetic theater.

## 3. Probe B — the 70% law, wired

Law, verbatim: *"with about 70% of the data you wish you had — waiting for 90% or more means you are likely moving too slow."*

**The fire-decision gate.** Every planning move carries `door` (one-way/two-way) + `data_fraction`. Two-way + ≥~70% ⇒ **fire; no further word**. One-way ⇒ named reversible act + rollback, then fire. The record lands in the F2 machinery (the chain's probe/run-record lane), inheriting M1's run-log discipline (seed, template, input-logging switch).

**Anti-pattern gates, named and refused.** (i) re-ask loop — a second word after the approved fire (the day's repeated re-asks were this in action); (ii) ratification-as-gate on a two-way door; (iii) checklist-shaped verification blocking a reversible act. Instances recorded with refuser + why; the record enforces, not a new gate.

**Reversibility.** Record + discipline, not a process lock; rollback = revert to gating, record kept, moves re-fire. One-way doors still get Dive Deep.
**Cost.** Zero billed; spends attention, not dollars.

## 4. Fit with the existing machinery

The release-point gate is already in the battery — Probe A extends it with one arm (Invent and Simplify: adopt the simpler mechanism, never "not invented here"). F2 is the probe-record lane both probes write to; M2's single-surface rule keeps it one ledger. Class-corroboration only: A is the harvest's write-gate L0 class (cite-or-hold); B is firing on a measured signal, not a permission gate.

## 5. Two-way doors on every move

| Move | Reversibility | Rollback |
|---|---|---|
| Probe A adopt → un-adopt | flag `shadow`→`enforce`→off | held blocks re-admit; bytes intact |
| Probe B fire → refire | record field + discipline | revert to gating; record kept |
| Public → private | the gate | re-arm to last private value |
| Cost → stop | cap stop | COST-OVER recorded |

## 6. The compose-check table (8 steps, FIRED/ABSENT, one evidence line each)

| # | Step | State | Evidence line |
|---|---|---|---|
| 1 | Citation arm wired into the compaction battery | FIRED/ABSENT | arm run log; cited vs. deferred counts |
| 2 | `shadow`→`enforce` both exercised | FIRED/ABSENT | flag history + deferral log |
| 3 | Rollback exercised (held blocks re-admit) | FIRED/ABSENT | re-admission record; byte-intact proof |
| 4 | Fire-decision gate live on every move | FIRED/ABSENT | decision records in the F2 lane |
| 5 | Anti-pattern gates named/refused in-record | FIRED/ABSENT | instances + whys |
| 6 | Approved fire executed once, no further word | FIRED/ABSENT | one execution vs. repeated asks |
| 7 | Cost confined to existing billed classes | FIRED/ABSENT | telemetry-only rows |
| 8 | Nothing public without the user's word | FIRED/ABSENT | gate; public surface = 0 until the word |

## 7. Loop-closing clause

Doctrine observed → doctrine wired → wiring audited by the record. Newly-arrived governance instruments become first-class legs with named budgets or explicit refusals with why (verification-channel appendix).

## 8. Fold for the master's §7

M3's label: **the governance seams are un-adopted** — the release-point rule and the 70% law were filed, not wired. Both are now named probes (citation arm in the compaction battery; fire-decision gate in the decision record), each with shadow/enforce reversibility and byte-intact rollback, at no new billed class.
