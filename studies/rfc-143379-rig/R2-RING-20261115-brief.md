# R2 RING — THE FIDELITY-LADDER L2 SELECTION + MISSINGNESS PROBE — 2026-11-15

## The contract (hard)
- **READING ANYTHING IS A CONTRACT VIOLATION** (the read-scatter class, receipted five times tonight). Everything you need is inline. Round 1 = write the skeleton; afterwards write only.
- ONE TOOL CALL PER ROUND. NEVER run git (the harness folds the commit itself — the fold-step). Appends ≤ 6,000 chars.
- The artifact: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/R2-L2-SELECTION-20261115.md`

## THE TARGET (inline — SPRINT-PLAN §3-R2, the storm harvest's axis b)
The fidelity ladder's **L2 stage** currently has two named gaps (the harvest + prior folds): (1) the **selection algorithm** — which memories survive a compression step — is unspecified (the field's candidate: CoMem 2611.16384, query-guided contrastive selective compression, 4× matches uncompressed at 4×, needle retention at 64×); (2) the **missingness verifier** — the ladder cannot detect when evidence silently lost — is absent (the field's candidate: SELD 2611.12903, no-training/no-labels preference-shift detection, 83% vs 70%). The kanban steer t_6f304f19 names this pairing. THE RING: design the L2 selection + missingness probe for the rig's ladder — the mechanism adaptation, never adoption: keep the mechanism, adapt the interfaces, leave the papers' surfaces.

## THE DELIVERABLE — five sections:
1. **THE L2 SELECTION SPEC** — the selection algorithm adapted for the rig's ladder: the inputs (the compression candidates + the query context), the contrastive scoring (CoMem's shape: keep what the query-contrast preserves; drop what the contrast ignores — the needle-retention criterion), the thresholds (the 4×-compression target with the needle-retention floor), and the integration point (the ladder's L2 selection step, between the candidate pool and the compression).
2. **THE MISSINGNESS VERIFIER SPEC** — the read-side evidence-plane verifier (SELD's shape): the no-training preference-shift detector run over the pre/post-compression read-back; the floor calibrated to the 83%-detection rate (the MEASURED criteria: shift over the floor = evidence-loss flag; under = clean); the verifier's position (the ladder's L2 exit, after the selection, before the fold).
3. **THE PROBE SHAPE (the falsifier)** — the seeded experiment: (a) seed a memory batch with a KNOWN non-redundant record (the needle); (b) run the selection with query-context A (where the needle's relevant — expect kept) and query-context B (where it's not — expect the needle's fate measured, never silently dropped); (c) run the verifier over both outcomes; (d) the measured criteria: context-A keeps the needle (PASS), context-B's drop is FLAGGED by the verifier (the missingness is visible, never silent). Battery home: `round2-combined-substrate` (the substrate battery's selection/missingness axis). Runner: the p0tat0 probe surface executes the battery slice at the fold (the receipt).
4. **THE METERS** — selection precision (needles kept in context-A), missingness detection (flags over the floor), the 4×-compression ratio with the needle-retention floor, the run record (run id, seed, contexts, verdicts) — honest, no runs tonight unless the fold's execution lands: `[ABSENT]` if not executed.
5. **THE HONEST MARKERS + TWO-WAY DOOR** — `[ABSENT]`: the ladder's current L2 code paths (not read — the contract), the live ladder's candidate pools; the design's value is unverified until the probe executes — the adoption is the chair's (SPRINT-PLAN §4); if the probe disproves either mechanism's fit, the design note stands and the alternatives are named, never forced.

## Binding
- Receipts per claim (INLINE-crate / DESIGN-NOTE / ABSENT). ABSENT stays ABSENT + named.
- The RFC + upstream stay QUIET. Nothing posts.
- End condition: the file > 8,000 chars with all five sections; then stop. No git.
