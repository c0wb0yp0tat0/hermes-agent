# L-2-ECONOMICS-ENRICHED-20261119.md — E1 enrichment (probe-design arm-structure + abstention axis cross-weighted into the economics scale contract)

## Contract status
- Gate (verbatim): "the gate: nothing public without the user's word."
- Two-way door: every add names its reversibility (see each [REVERSIBLE] tag).
- Wall clause: "a non-reproduction is a QUESTION, not a stop."
- Review-loop: draft → stranger re-read → one refinement per finding → 3–4 adversarial pushbacks → termination (no-change re-read, twice).
- Rhythm: one section per write, skeleton by round 4, ≤6,000 chars/write, commit before exit.

## 1. What the probe's arm structure adds to the cost rows
The economics contract's L-2 rows are static; the probe's three-arm structure (E1 brief §E1 seam: `L-1-PROBE-DESIGN-20261119.md`) makes them per-episode load-bearing, not scenario-only.

- **The governor's per-episode adds [REVERSIBLE: toggle the per-episode gate per run; removal is a flag, not a delete].**
  The governor arm is the cost-bearing row that turns the economics' episode ceiling into an enforced per-episode spend floor. Where the economics contract says "each episode costs X", the probe adds: governor per-episode cap + the marginal probe-surcharge that applies *inside* the episode at the enqueue point. Cost row new = `governor_per_episode × episodes + surcharge_per_enqueue`; the arm pins it so the cost table is reproducible episode-to-episode rather than aggregate.
- **The oracle arm's free-surface claim [REVERSIBLE: free-surface reads are opt-in; the claim becomes a measured upper bound, not an assumption].**
  The oracle arm asserts a free-surface (zero-oversight) read path. The economics contract gains a second claim row: `free_surface_claim_cost = base − (oracle_findings × meter)`. The arm's presence means the "free surface" is not a given; it is a measured claim that the cost rows must carry a reconciliation ledger against the governor arm. Where the governor charges per-episode, the oracle charges nothing but is instrumented for the convergence check.

Receipt: L-1 arms give the cost rows a per-episode, per-phase granularity the static table lacks; the two-way door is that both adds are flag-toggleable with zero re-architecture.

## 2. Where the abstention axis's n-requirements meet the economics' 40/arm
The abstention axis in L-1 requires n=40 per cell to hold the rate math (±15pp at n=40) — that is the anchor. The economics contract's `40/arm` must be read as the *cell* n, not the *arm* n.

- **Receipted rate math:** the ±15pp bound is a per-cell binomial bound at n=40; it does not automatically hold when cells are pooled across R/H/E/A or when one arm's abstention rate shifts the effective n. To keep the ±15pp claim honest, the cost rows must carry the per-cell n as a priced input, not the pooled n.
- **The R/H/E/A cells:** 4 cells × n=40 = 160 nominal probes minimum. The economics' `40/arm` is the per-cell requirement, and the probe structure forbids merging cells unless a re-weighted confidence interval is re-run. Cost row new: `n_cell × 4 + CI_path_cost` — the four cells are priced explicitly; any deviation from n=40/cell is a priced sensitivity row, not an accounting convenience.
- **Divergence with the economics (named, not smoothed):** the L-1 abstention axis's n=40 is a *per-cell* requirement for the rate claim; the L-2 contract states "40/arm" which reads like a *per-arm total*. If "40/arm" is total across R/H/E/A, the cells are under-powered and ±15pp does not hold per cell. Resolution recorded as a named divergence: L-1's abstention sample-size requirement governs the claim (n=40/cell), and L-2's 40/arm must be interpreted as the per-cell floor. The economics rows must be re-labelled `n_cell = 40 (per cell, per abstention axis)` so the rate math stays receipted.
- **Abstention cost row:** abstention is not free. The axis's n-requirements translate into a priced row: `abstention_rejection_cost = n_abstained × per_rejection`; the economics contract cannot claim the ±15pp bound without budgeting for the probes that abstain, because each abstention reduces the effective n below the receipted 40/cell.

## 3. The CERTIFY bar vs the pre-committed $100 cap
The decision rule's CERTIFY bar and the economics' pre-committed $100 cap interact at the commit point.

- **The interaction:** CERTIFY is a decision bar on the economics artifact (the artifact is CERTIFIED when the cost rows close with the probe's per-cell receipts in place). The $100 cap is a pre-committed budget ceiling. They do not conflict by themselves: the cap binds the *spend*, CERTIFY binds the *claim*.
- **The divergence (named):** the pre-committed $100 cap is a ceiling on *new* spend; the probe structure requires n=160 nominal probes minimum (4 cells × 40) plus the per-episode governor adds, plus the oracle free-surface reconciliation. If the probe's per-probe cost × 160 exceeds $100, the cap is violated before CERTIFY can fire. Evidence: L-1's rate math needs n=40/cell; L-2's cap has no cell-level budget line.
- **Resolution (recorded, not smoothed):** the two-way door closes the gap — split the $100 cap into (a) the probe-gate budget (fixed, ≤$100 pre-committed), and (b) the post-CERTIFY runtime budget (uncapped, since CERTIFY is the commit gate for the public artifact itself). CERTIFY fires only when the cell-level receipts (n=40 per cell) are in the cost rows *and* the pre-committed $100 probe-gate cap is respected. If the probe-gate can't be covered by $100, the CERTIFY bar is NOT met — the cap is the harder constraint, and it is the divergence the RELOAD compose must reconcile.
- **Receipted lesson:** the economics' $100 cap is the binding constraint; the probe design's n-requirements are the claim; CERTIFY merges them at the commit gate, and the cap wins.

## 4. Divergence record (evidence, not smoothed)
- **D1 — n semantics:** L-1's abstention axis requires n=40 *per cell*; L-2's 40/arm reads as per-arm total. Resolution: L-1 governs the claim; L-2 rows must say `n_cell = 40`.
- **D2 — Pooling:** pooling R/H/E/A before the CI re-run silently drops the ±15pp bound. Evidence: the binomial bound is per-cell; a pooled n=160 would give a narrower interval but the claim is per-cell, so pooling is a QUESTION, not a stop. [REVERSIBLE: pooling is opt-in only with a re-run ledger.]
- **D3 — Cap bindingness:** the $100 cap binds before CERTIFY if probe-gate > $100; CERTIFY is unreachable until the cap is respected. Resolution: split cap into probe-gate (≤$100) and post-CERTIFY budget.

## 5. Compose-check table (FIRED)
| Step | Evidence | FIRED/ABSENT |
|---|---|---|
| 1. Read target cold, in full | L-2-ECONOMICS-20261119.md read on disk; E1-BRIEF read first | FIRED |
| 2. Read own lane artifact + chain APPENDIX-A | L-1 probe design + APPENDIX-A (inherited) | FIRED |
| 3. Enrich without rewriting target shape | Cost rows gain per-episode governor adds + oracle free-surface claim; L-2 shape preserved | FIRED |
| 4. Divergence named with evidence | D1–D3, each with receipt | FIRED |
| 5. Compose-check closes artifact | Table above, 5 rows, all FIRED | FIRED |
| 6. Record-first, receipts on every claim | All rows carry receipts (#1–#5) | FIRED |
| 7. Rhythm honored | Skeleton → real content; one section per write; ≤6,000 chars; commit before exit | FIRED |

## Two-way door register (every add reversible)
- Governor per-episode adds [REVERSIBLE: flag-toggle, no re-architecture]
- Oracle free-surface claim [REVERSIBLE: opt-in measured bound, ledger-reconcilable]
- n_cell = 40 cell relabel [REVERSIBLE: can revert to pooled n with CI re-run]
- Cap split (≤$100 probe-gate / post-CERTIFY) [REVERSIBLE: mergeable back with re-budget]

## Wall clause
A non-reproduction is a QUESTION, not a stop — the $100 cap, the n=40/cell rate math, and the CERTIFY bar are all questioned (not halted) when the probe-gate exceeds the cap or the cell n drops; the economics rows record the question and re-run the CI.

--- End of enriched artifact. The RELOAD compose's input set is complete; the reconcile follows on the flagship with D1–D3 resolved by evidence.
