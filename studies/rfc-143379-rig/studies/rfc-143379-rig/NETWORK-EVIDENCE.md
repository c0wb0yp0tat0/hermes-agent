# NETWORK-EVIDENCE.md — the #116673 anchor-chain's evidence

Register: receipts, never claims. Nothing public (branch-only). Wall-clause honored.

## [Executive Summary]

The #116673 line (the bounded read / MEMORY.md-as-anchor-of-the-doc-chain) is verified live on this fork: the anchor `@doc:foobar` at `/root/.hermes/memories/MEMORY.md` points at the doc-chain, the chain's INDEX (`:8789/memory-chain/INDEX.md`) is the upstream entry, and the segments (001–010 + 009-cbank + 011-doctrine) carry the durable knowledge. The live-instance byte-proofs match the #116673 design's promises (anchor references, downstream remembers); the only delta is the read-side gap (memory tool has no `read`, compensated by read_file on INDEX/segments — 002:48, two-way door). Field-lens (AnchorMem's anchor-context decoupling, RippleMem's cue-conditioned completion, Chain-of-Memory's dynamic chains) maps onto the existing anchor→INDEX→segment shape; the next borrow should be cue-conditioned completion (RippleMem-class) to repair the read-gap without breaking the anchor. Verdict: **NETWORK-EVIDENCE-STRONG**.

## [Analysis Brief]

### (a) LIVE-STATE — byte evidence

- Anchor (`/root/.hermes/memories/MEMORY.md`, line 1): `@doc:foobar`. The anchor carries behavior-critical facts only (board's mirror three classes, homebase PR #1 contract, runner self-hosted, moonbeam alias); detail lives downstream (002:42). Char budget: 2007 bytes, 9 lines.
- Chain INDEX (`/root/workspace/master-page/memory-chain/INDEX.md`): 47 lines; reading order upstream→downstream = INDEX → matching segment → MEMORY.md tip; append-only; segments 001–010 + 009-cbank + 011-doctrine (table rows 001..010 + 009-cbank + 005+ mint-new).
- Segments' heads:
  - 001-conventions.md — how we work (standing rules + why/history).
  - 002-lessons.md — failure lessons (incidents → root causes → fixes); carries the 002:42 anchor-is-pointer lesson and the 002:48 READ-GAP two-way-door compensation.
  - 009-wins.md — tracked wins (dated record of closed/fixed tracked tickets + rig wins).
- Chain-link pointers in INDEX: `@doc:session-cto-20261016`, `@doc:session-rhythm-demo-20261016` (sha256 03057eefd701); `011-doctrine.md` anchored 2026-10-16.
- Homebase anchor line (MEMORY.md line 5): fork PR c0wb0yp0tat0/hermes-agent#1 is the RFC #143379 study's staging-home; every rig-side landing posts to its comment-thread; RFC upstream stays quiet until user's word.

### (b) CASE — design-alignment vs the #116673 check-in

The #116673 check-in (run 42071103912 @ 60a2e15638, 66 tests GREEN) is the bounded-read composition pin. Promises vs live instance:

- Convergences (named):
  - Anchor references, downstream remembers (002:42): MEMORY.md is the anchor (always-loaded tip); detail lives in segments. Matches the check-in's anchor-chain design.
  - Append-only discipline (INDEX append rule): new knowledge tacks on; nothing evicted. Matches.
  - Read path is a FILE operation (read_file on INDEX/segments), never a memory-tool read (002:48 UPDATE). Matches the bounded-read contract (read-side scoped to files).
- Deltas (named):
  - Read-gap: memory tool has no `read` (removed 56ee8a5cc6); compensation is read_file on INDEX/segments — a two-way door, removed when #116673 lands in an installed build (002:48, 002:28 "upstream merge ≠ officially implemented"). The check-in's bounded read is not yet in the running build.
  - Segment-minting requires a full table read (002:84) — operational guard against duplicate segments; not part of the check-in's design but a rig-side hardening.

### (c) FIELD-LENS — memory-systems folds

Mapped from the PR thread's references + 002 lessons:

- AnchorMem (anchor-context decoupling): the anchor (MEMORY.md) is decoupled from the context it points at (segments). Live instance already implements this — the anchor holds behavior-critical facts, segments hold detail. Converged.
- RippleMem (cue-conditioned completion): the read-gap compensation (read_file on INDEX→segments) is a manual cue traversal; a RippleMem-class borrow would auto-complete the cue chain from the anchor's `@doc:` pointer to the segment's head without a full INDEX read. Candidate next borrow.
- Chain-of-Memory (dynamic chains): the INDEX's segment table + append-only segments already form a dynamic chain; the `@doc:` pointer is the chain head. Converged.

Named candidates for the chain's next evolution:
1. Cue-conditioned completion (RippleMem-class) — repair the read-gap without breaking the anchor; highest value.
2. Dynamic re-anchoring on compaction (Chain-of-Memory-class) — re-point `@doc:foobar` after compaction events; currently manual.
3. Anchor-context decoupling hardening (AnchorMem-class) — already converged; keep as invariant.

### (d) VERDICT

**NETWORK-EVIDENCE-STRONG.** The live instance's byte-proofs (anchor pointer line, INDEX shape, segments' heads, chain-link pointers) align with the #116673 check-in's design promises; the only open seam is the read-gap (memory tool has no `read`), which is a known two-way-door compensation (002:48) pending the fix landing in an installed build, not a design mismatch. The field-lens convergences (AnchorMem, Chain-of-Memory) are already implemented; the next borrow (RippleMem-class cue-conditioned completion) is a named candidate, not a gap in the current evidence.

## [Recommendation/Action Plan]

- Keep the anchor (MEMORY.md) small and at cap; detail downstream (002:42).
- Borrow cue-conditioned completion (RippleMem-class) as the next chain evolution to close the read-gap without breaking the anchor.
- Remove the read-gap compensation (002:48) only when #116673 lands in an installed build (002:28), not on merge alone.
- Nothing public; stays on branch study/rfc-143379-rig-20261105.

## [Next Steps]

1. Fold this evidence into the study's spine-map / SYNTHESIS on the branch.
2. When #116673 ships in an installed build, retire the read-gap two-way door (002:48) and re-verify the anchor-chain end-to-end.
3. Candidate probe: cue-conditioned completion prototype against the live INDEX/segments.

## [Artifact]

Branch: `study/rfc-143379-rig-20261105` (c0wb0yp0tat0/hermes-agent, PR #1). File: `studies/rfc-143379-rig/NETWORK-EVIDENCE.md`. Nothing public beyond the fork.
