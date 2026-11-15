# RFC-UPDATE-LENS-20261107 — DRAFT MATERIAL FOR RFC #143379 (RFC-UPDATE)

**Status:** DRAFT for operator approval. Nothing posts anywhere public. Fork-only, branch `study/rfc-143379-rig-20261105`.

**Register:** factual, evidence-cited, no machinery-vocabulary, no internal names. Per line: honest state (evidence, receipts, measured gaps), the delta the study produced, and the proposed update's shape (3-5 sentences).

---

## 1. The restore (read-restore)

**Honest state.** The read-restore PR #116673 is open and unmerged, last updated 2026-10-27 — 11 days stale at this study's bearings-read. Its pass is the pilot's start-line; until it merges, direct reads stay locked and the compensation loop (demoted re-reads, ~64 MB of spillover plus session-store) keeps running. Evidence: PR state from the thread's public record; `READ-GAP-COST-20261107.md` §§(a)–(c).

**Delta the study produced.** Quantified the read-gap's cost: ~64 MB of compensation storage (12 MB spillover / 117 files + 52 MB sessions), 5 corrected drift-events (2 direct read-path-mechanic), and the 11-day closed gate as the binding dependency. Also verified and struck a fabricated receipt (`6709010002`) — no invented receipt stands.

**Proposed update shape.** Report the read-restore as the gating dependency: the pilot's time, not bytes, is the real tax, and the compensation loop is bounded but self-sustaining while the gate stays closed. State that the measured cost is ~64 MB plus 5 events plus 11 days, of which 2 events are direct read-path-mechanic and the staleness is the load-bearing seam. Propose the update note that nothing in the leg releases the read-path lock until the fix merges, and that the pilot starts only after that pass. Keep the framing as a gate, not a goal.

## 2. The network

**Honest state.** Per-fork independent receipts span 31 forks, each its own hosted-runner window on the same pinned battery with distinct run-ids — breadth of runner-windows is confirmed, but conclusions are pending (30 queued, 1 in progress). Same-account forks mean hosted-window independence, not organizational independence. Evidence: `GITHUB-RUNNER-FABRIC-20261107.md` (6fef8e3379); `FABRIC-RECEIPTS-20261107.md`.

**Delta the study produced.** Separated breadth (measured, 31 forks) from conclusion (unmeasured, conclusions pending), and narrowed the independence claim to runner-window independence with the same-account caveat named. Also receipted the fabric as dispatched-not-concluded.

**Proposed update shape.** State that the network's breadth claim is confirmed at 31 distinct run-ids on a single pinned battery, with each fork as its own hosted-runner window. Note that conclusions are pending and that a conclusions column is required before any readiness claim. Clarify that independence is runner-window independence, not contributor or account independence, and that the same-account caveat is a named, receipted limitation rather than an oversight.

## 3. The governance

**Honest state.** Honest-termination proof is receipted twice (C3 and C4, zero improvements each, 11 CONFIRMED / 0 NUANCED / 0 REFUTED per cycle), with a corrections ledger C3-1…C3-9. The audit seat is same-family decorrelation, not cross-family independence. Receipt-discipline (envelope ledger, goal-lock, NOT-RUN markers) is real, with 3 of 40 markers under-specified. Evidence: `ACES-IMPROVE-C3-20261107.md` (c9a0325719); `ACES-AUDIT-C3-20261107.md` (ca15b98e1f); `ACES-REVIEW-C3-20261107.md`.

**Delta the study produced.** Ratified the terminal vocabulary (`complete` / `no_change` / `blocked` / `failed`, plus the named missing verdict `THRASHING`) and reclassified `no_change` as a terminal, never a failure. Also elevated the NOT-RUN census repair and the audit-independence caveat to named, receipted readiness gaps rather than footnotes.

**Proposed update shape.** Report the governance layer as having a twice-receipted honest-termination proof with terminal vocabulary ratified and `no_change` treated as a terminal outcome. Disclose that the audit is same-family decorrelation, not cross-family, and that the NOT-RUN census has 3 under-specified markers pending repair. Propose the update note that governance readiness is gated on census tightening and on an explicit independence statement, not on the termination proof alone.

## 4. The compaction

**Honest state.** Compaction-front healing is preparation, not arrival: guard-preamble plus empty-answer receipts banked, isolate re-run pending, separation unmeasured. The seam-cleared arc is machinery. The read-gap's drift is the one measured negative; the W2 separation is unmeasured; the ACES loop is self-referential. Evidence: `W2-ISOLATION-STATUS-20261106.md` (847c61ac4f); `READ-GAP-COST-20261107.md`.

**Delta the study produced.** Relabeled the two scientific fronts honestly: one measured negative (read-path-mechanic drift), one unmeasured separation, one self-referential loop — preparation and machinery, not proven science. Also recorded the machinery-vs-science ratio as a non-negotiable framing repair rather than a caveat.

**Proposed update shape.** State that the compaction front has banked guard-preamble and empty-answer receipts but has not yet demonstrated separation, which remains unmeasured pending the isolate re-run. Note that the seam-cleared arc is machinery and that the read-gap drift is the only measured negative to date. Propose the update label these fronts as preparation and machinery rather than proven science, with the machinery-vs-science ratio stated as a non-negotiable framing constraint.

---

**Receipts (cold):** `READ-GAP-COST-20261107.md` (e0673b6dda) · `RIG-INTENT-20261107.md` (2e9a6870bd) · `KIT-SYNTH-2-20261107.md` (KIT-SYNTH-2 fold) · `GITHUB-RUNNER-FABRIC-20261107.md` (6fef8e3379) · `FABRIC-RECEIPTS-20261107.md` · `ACES-IMPROVE-C3-20261107.md` (c9a0325719) · `ACES-AUDIT-C3-20261107.md` (ca15b98e1f) · `ACES-REVIEW-C3-20261107.md` · `W2-ISOLATION-STATUS-20261106.md` (847c61ac4f).

**Boundary:** fork-only; nothing public without the operator's word.
