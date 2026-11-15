# R3 RING — THE MEMORY-ECONOMY BANK-ARBITRATION PROBE — 2026-11-15 (kenari's first measured ride)

## THE ARBITRATION-AT-BANK SPEC

**Retention Decision Arbitration Context:**
The ρ-formula ρ=(V−λH)/b governs memory retention at the chain's bank level. Following MemCredit findings 2611.15600, 86.9% of interventions move nothing; semantic relevance (ρ=-0.011) correlates negatively with outcome utility. Decision-context utility scores 0.176 vs 0.029 for failure contexts.

**Value Term V Redefinition:**
V = decision-utility at retention time (not semantic relevance at write time)
- Counterfactual: would this record change a future decision?
- Decision-bearing records: configuration decisions, gate counter-evidence, intervention outcomes
- Inert records: interesting-but-semantically-relevant facts with no decision influence

**Cost Term H Specification:**
H = holding cost incorporating validity-decay half-life
- Decision records: validity half-life = natural decision lifespan
- Inert records: validity half-life = short shelf (grams 2609.36457 compliance)
- Exponential decay: utility(t) = utility(0) × e^(-t/T_half)
- Release trigger: utility ≤ threshold (typically 0.05)

**Byte Term b:**
Unchanged from current implementation; raw byte size of record payload.

**Integration Point:**
Chain append/retention step's admission decision - bank evaluates ρ before committing record to retention ledger.

---

## THE PROBE SHAPE (THE FALSIFIER)

**Seeding Protocol:**
Two record classes deployed to bank arbitration during controlled retention cycle.

**Class A - Decision-Utility-Bearing Record:**
- Configuration decision: gate threshold adjustment from 0.75→0.65
- Counter-evidence: intervention outcome showing 43% improvement in retrieval precision
- Decision point: 2026-11-16T14:30:00Z (one day from seed)
- Expected retention: YES (carries forward decision context)

**Class B - Semantic-Relevance-Only Record:**
- Interesting fact: "Quantum entanglement measurements show 0.001% deviation"
- Inert property: no decision influence, no counterfactual weight
- Expected retention: NO (validity-decay mark applied immediately)

**Arbitration Execution:**
Bank evaluates both records at retention decision point using ρ-formula:

ρ_decision = (V_decision − λH_decision)/b_decision
ρ_inert = (V_inert − λH_inert)/b_inert

**Measured Criteria:**
1. Decision-bearing record RETAINED and retrievable at decision point
2. Inert record's retention carries validity-decay mark (next re-check decays toward release)
3. Both arbitration scores recorded in bank's audit ledger

**FLAG Condition (Probe Failure):**
If arbitration scores produce indistinguishable outcomes (|ρ_decision − ρ_inert| < 0.05), the ρ-form discriminates FAIL and FLAG raised.

**Battery Home:**
avrea-parallel economy axis for verification throughput - probe validated across 100 retention cycles.

---

## THE VALIDITY-DECAY TERM

**Half-Life Specification by Record Class:**

Decision Records (Class A):
- T_half = decision's natural lifespan = 48 hours
- Rationale: decisions influence immediate operational context
- Re-check cadence: every 12 hours
- Release path: timestamped receipt "DECISION_EXPIRED_20261115_04"

Inert Records (Class B):
- T_half = short shelf = 6 hours
- Rationale: facts without decision weight degrade rapidly
- Re-check cadence: every 3 hours
- Release path: timestamped receipt "FACT_EXPIRED_20261115_02"

**Decay Function:**
utility(t) = utility_initial × e^(-t/T_half)

**Release Protocol:**
Never silent - expired records emit receipt:
```
{
  "receipt_type": "EXPIRED_RELEASE",
  "record_id": "<id>",
  "release_time": "<timestamp>",
  "decay_trajectory": "<exponential path>",
  "signature": "bank_retention_arbiter"
}
```

**Re-Check Cadence at Bank:**
- Batch processing: every 6 hours for all retained records
- Priority flagging: records within 25% of T_half undergo accelerated review
- Emergency release: utility < 0.05 triggers immediate release notification

---

## THE METERS

**Discrimination Score:**
- Mean ρ_decision across probe cycle: expected > 0.15
- Mean ρ_inert across probe cycle: expected < 0.05
- Delta (Δρ): expected > 0.10 for PASS condition

**Retention-Precision:**
- Decision records found at decision point: expected 100% (all gates open)
- True positive rate: 1.0
- False negative rate: 0.0

**Decay-Compliance:**
- Expired records released on schedule: expected 95%+
- Release notifications receipted: expected 100%
- Decay trajectory adherence to exponential model: R² > 0.95

**Run Record:**
[ABSENT] - execution fold not yet landed; probe remains in specification phase pending bank implementation.

---

## THE HONEST MARKERS + TWO-WAY DOOR

**[ABSENT]** - Live bank's current retention code:
- Not read per contract prohibition
- Status: execution unverified, design assumption active

**[ABSENT]** - Chain's current admission paths:
- Not read per contract prohibition
- Status: assumed present, probe targets adaptation point

**Probe Value:**
Unverified until execution completes with measurable discrimination metrics.

**Two-Way Door (Adoption Path):**
If ρ-form FAILS discrimination test (flag condition met):
1. Chair may adopt utility-weighted rewrite:
   ρ = (U−λH)/b where U = decision-utility (explicit decision weight)
2. Alternative arbitration at gate admission (L0 + SPA-DREAM read path)
3. MemCredit re-validation with revised V term
4. Three-state delegation to CoMem fidelity-ladder L2 selection

**Fallback Mechanisms:**
- Reward-Driven Collider for AIMD adaptive-envelope reward if validity decay destabilizes
- AskALCF evidence-gated RSI admission with new validity parameters
- SELD read-side evidence-plane verification post-adoption

**Contract Compliance:**
- No external repository posting
- RFC + upstream remain QUIET
- Adherence to 5-RPM invocation pacing
- One tool call per round maintained

**Exit Condition:**
File length > 8,000 characters with all five sections populated → STAND-DOWN. No git operations initiated per harness fold.