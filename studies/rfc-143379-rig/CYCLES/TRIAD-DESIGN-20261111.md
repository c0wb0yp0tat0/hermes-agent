# TRIAD-DESIGN — the triangulation's maximization (plan leg, ANCHOR-style)

**Lane:** copycat (design) · **Date:** 2026-11-11 · **Branch:** `study/rfc-143379-rig-20261105` · **Gate:** nothing public without the operator's word.
**Mission:** maximize the information the fleet's surfaces yield; every instrument-design serves the broken-arrow synthesis's verification.
**Traceability:** every row cites its seed — LANDING-ASSESSMENT-20261111 (LA), S2U-MISSION-PLAN-NUANCE-20261111 (MP), FLEET-TRUTH (FT = CIRCLE-BACK-FREE-FLOOR + FREE-CREDENTIAL-LEDGER-20261111), RFC-143379-RECORD-20261111 (REC), DOCTRINE (002-lessons + process-rulings-20261111, DO), IDEA-BANK (IB). The star's claims are the synthesis's four (below).

## 0. The synthesis's claims (the star the battery serves)
- **C1 — the read's absence at the pinned head.** The pinned head's read surface returns nothing where the record says bytes live. (REC; LA)
- **C2 — the dispatch's unknown-action answer.** The dispatch's answer names an action the contract cannot bind. (MP; REC)
- **C3 — the hand-back sites.** The sites where the fleet hands work back are unverified at the current head. (LA; FT)
- **C4 — the restore-head's counterfactual.** The restore-head's counterfactual (what the head would read if restored) is untested. (REC; LA)

## 1. The surface-map
| id | surface | host-class | meter | role in the triad |
|---|---|---|---|---|
| S1 | avrea-cloud | cloud | 2-vcpu, free-meter | the free seat; the throttled bias |
| S2 | self-hosted | full-host | full-host | the unbounded bias; the control |
| S3 | github-hosted | runner | hosted | the third failure-domain; the citation leg |
| S4 | the hub | pinned head | read-only | C1's surface (the read's absence) |
| S5 | the dispatch | contract | read/write | C2's surface (the unknown-action answer) |
| S6 | the hand-back sites | fleet | write | C3's surface |
| S7 | the restore-head | counterfactual | replay | C4's surface |

## 2. The battery-matrix (instrument × surface × order)
| order | instrument | surface | why there | receipt |
|---|---|---|---|---|
| 1 | claims-probe (I1) | S4 → S1/S2 | C1 first; the absence is the star | absence-row |
| 2 | contract-arms (I2) | S5 → S3 | C2; the unknown-action bound | arm-table |
| 3 | R1/R2 reproductions (I4) | S1 + S2 | the abstention/litm repros; the twin bias | repro-row |
| 4 | falsifier-battery (I3) | S4/S5/S7 | the falsifier-triad | falsifier-table |
| 5 | sweep/stress selectors (I5) | S1/S2/S3 | the drift-spread under load | sweep-rows |
| 6 | fleet-vitals (I6) | S1/S2/S3 | the watchers' floors | vitals-rows |

## 3. The divergence-classes (expected biases; FINDINGS vs noise)
| class | seam | FINDING when | noise when |
|---|---|---|---|
| D1 surface-bias | cloud/self-hosted/github | same battery diverges across surfaces | — |
| D2 meter-bias | free-meter vs full-host | state artifact (not resource) | throttle/timing |
| D3 pin-drift | pinned head vs current head | bytes moved | — |
| D4 count-drift / number-seam | the count's edge | repeatable at head | one-off |
| D5 stale-state | the read's freshness | a live lane stale | — |
| D6 phantom-SHAs | the anchor's reality | anchor unattached | — |
| D7 false byte-claims | the claim's byte | claim ungrounded | — |
| D8 compose-spines | the entry record | spine broken | — |

## 4. The combos
**(a) The falsifier-triad.** One claim, three independently re-derived falsifiers (from the current bytes, not the record): C1's absence, C2's unknown-action, C4's counterfactual. A claim survives only if all three fail to falsify it; any one falsifying is a FINDING. (DO: falsifier-ethics)
**(b) The twin-avrea mirror (creative).** Run the SAME battery on S1 and S2 in the same window; diff the receipts byte-for-byte. The cloud/self-hosted divergence is the data — a divergence the single-surface run cannot see. Justification: the triad's three failure-domains are the same battery; the mirror collapses two domains into one controlled comparison, doubling the information per minute. (IB: the two-way doors; MP: the runner-pair)

## 5. The ROI-ranking + the recommendation
| rank | move | information/minute | cost |
|---|---|---|---|
| 1 | twin-avrea mirror (b) | highest — two domains, one run | low (idle seats) |
| 2 | falsifier-triad (a) | high — three falsifiers, one claim | low |
| 3 | claims-probe at S4 | high — the star's absence | low |
| 4 | contract-arms at S5 | medium — C2's bound | low |
| 5 | sweep/stress selectors | medium — drift under load | medium |
| 6 | fleet-vitals | floor — the watchers | low |

**Recommendation first:** fire the twin-avrea mirror (b) as the opening move — it is the only combo that yields a cross-domain divergence in a single window — then the falsifier-triad (a) on C1/C2/C4, then the claims-probe at S4. The mirror's divergence decides which of D1/D2 is a FINDING; the triad then tests the star's claims against it.