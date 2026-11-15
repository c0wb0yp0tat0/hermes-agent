# NETWORK-LINE-ANCHORCHAIN-20261106.md — the anchor-chain's live-instance mechanics (the #116673 read-side evidence)

**Status: COMPLETE — the fork's own live instance, derived (read-side only; the chain reads, never writes).**
`NETWORK-EVIDENCE.md` = NETWORK-EVIDENCE-STRONG (round-10 artifact, in place on the branch).
This page is the line's NEXT ring: the anchor-chain mechanics as staged evidence for the #116673 adoption case.
Register: receipts, never claims.

---

## [Executive Summary]

The #116673 line (bounded read / `MEMORY.md`-as-anchor-of-the-doc-chain) is verified live on this fork.
The anchor `@doc:foobar` at `/root/.hermes/memories/MEMORY.md` points at the doc-chain; the chain's INDEX
(`:8789/memory-chain/INDEX.md`) is the upstream entry; the segments (001–010 + 009-cbank + 011-doctrine) carry
the durable knowledge. The live-instance byte-proofs match the #116673 design's promises (anchor references,
downstream remembers, append-only, read path is a file op). The only delta is the read-gap (memory tool has no
`read`; compensated by `read_file` on INDEX/segments — 002:48, two-way door). Field-lens (AnchorMem's
anchor-context decoupling, RippleMem's cue-conditioned completion, Chain-of-Memory's dynamic chains) maps onto
the existing anchor→INDEX→segment shape; the next borrow is cue-conditioned completion (RippleMem-class) to repair
the read-gap without breaking the anchor. Verdict: **NETWORK-EVIDENCE-STRONG**.

---

## [Analysis Brief]

### (a) LIVE-STATE — byte evidence (the anchor's structure + the chain's reading-order)

**1. The anchor — `/root/.hermes/memories/MEMORY.md` (line 1)**

- Receipt: `read_file` on `/root/.hermes/memories/MEMORY.md` (round-10, 2026-11-06).
- Byte: `@doc:foobar` — the anchor is a single canonical doc-name pointer, nothing else.
- Behavioural contract (chain 001 L93 / 009-compensation-bank.md): the memory doc IS the read path
  (INDEX → segments → receipts); detail lives downstream (002:42); the doc holds anchors only, never full story.
- The companion file `/root/.hermes/memories/USER.md` is the second always-loaded anchor; both are
  frozen load-time snapshots (memory tool caps 2,200 / 1,375; removed `read` 2026-02-19, commit 56ee8a5cc6).
- Receipts: `MEMORY.md` line 1 (@doc:foobar) + 009-cbank table + 002:42.

**2. The chain's reading order (upstream → downstream) — INDEX at
`/root/workspace/master-page/memory-chain/INDEX.md`**

- Operational line: `served :8789/memory-chain/` (INDEX header, 2026-09-18, hub pve-1, skill `memory-chain`).
- Reading order per the INDEX: (1) this INDEX; (2) the segment matching the task (table); (3) `MEMORY.md` — the
  always-loaded *tip* of the chain: anchors only, never the whole story.
- The owning segments (from the INDEX table + the chain's own files):

  | # | File | Owns | Signature |
  |---|---|---|---|
  | 001 | 001-conventions.md | how we work: standing rules + why/history | L93 re-anchor cadence + L94 compensation-banking pattern |
  | 002 | 002-lessons.md | failure lessons → root causes → fixes | 002:42 anchor-is-pointer; 002:48 READ-GAP two-way-door; 002:84 full-table read for minting |
  | 004 | 004-network.md | hosts, projects, parked items, doors | the doc-chain viability ACES cycle + the 116673 regression pass + UDM record (2026-10-12) |
  | 005 | 005-skills-inventory.md | rig's full skill library (133 skills, 18 categories) | keep-list; mint-new segments |
  | 006 | 006-external-frameworks.md | community repos mirroring the mechanism framework | Finn763/expert-roster (master-skill/index/on-demand triad = our anchor+chain) + xngg1021/academic-research-kernel (MAP matrix ≈ claim-evidence graph) |
  | 009 | 009-compensation-bank.md | rig's reversible compensations + removal triggers keyed to INSTALLED fixes | read-gap workaround, twice-read discipline, re-anchor cadence, gist anchor + chain mirror, -z oneshot |
  | 009 | 009-wins.md | dated record of closed/fixed tickets + rig wins (watchdog = sensor) | 2026-10-14 battery-loop full coverage + #116673 value-add fully verified |
  | 011 | 011-doctrine.md | the universal standard: quality-first, fold = one expression | anchors hold deliberate entries (800+ docs); chain holds depth; append-only |
  | 005+ | (min) new segments are minted here, never appended to existing | operational guard against duplicate segments |

- The C28 segmented view (SEGMENT_INDEX.md, boundary-aligned at lesson markers) confirms the same structure:
  25 segments, 113 lessons, 91,881 chars; the anchor/INDEX/segment shape is the frame.

**3. The chain's reading-order in practice (the #116673 line's read-side)**

- Code-read receipt (XNGG-GAPS-VERIFICATION-20261105.md, gap-2 refuted at pin d1bdb4582c): `tools/memory_tool.py:280-283`
  already carries the `if name is None: return target, ("Invalid chain doc name…")` guard — the read-side resolves
  target names through the doc-name path, not a blind string op.
- The read path on this rig = `read_file` on INDEX → segment → receipt; the memory tool's *static* shape is
  add/replace/remove only (removed `read` 2026-02-19). The two-way door is open (002:48), removed when
  #116673 lands INSTALLED in the running build (009-cbank row-1 removal gate: `gh api pulls/116673 --jq .merged`
  = true AND installed `tools/memory_tool.py` enum contains `"read"`).

### (b) THE LIVE-INSTANCE BYTES — receipts vs. claims

| Claim (proposed by the arm) | Receipt | Verdict |
|---|---|---|
| The anchor `@doc:foobar` at MEMORY.md line 1 is the tip of the chain; detail loads downstream | `read_file` on MEMORY.md → line 1 = `@doc:foobar`; 001 L93 + 002:42 + 009-cbank | **Fired** — anchor is-pointer, read path is file op |
| The chain INDEX (`:8789/memory-chain/INDEX.md`) is the upstream entry; reading order = INDEX → segment → MEMORY.md | INDEX header + reading-order block; 002, 004, 011 authored to that shape | **Fired** — the READ order is wired |
| The segments carry the durable knowledge (001 conventions, 002 lessons, 009 wins + cbank, 011 doctrine) | 001/002/009-cbank/009-wins/011-doctrine reads (round-10) | **Fired** — the depth is real |
| The chain IS append-only; nothing is ever evicted | 001 L1 + 011-doctrine (2026-10-16) + 002 lessons | **Fired** — append-only, not a rotation diary |
| The memory tool has no `read` (removed 56ee8a5cc6); the rig compensates with `read_file` | XNGG-GAPS gap-2 refuted at pin; 009-cbank row-1 | **Fired** — the delta is named and compensated |
| #116673 promises (anchor refs, writes refused until anchor links doc, orphan_docs visibility, anchor cap only) | 004-network.md ACES cycle + 001/002/009 bullets; 002:42 | **Converged** — design + live instance match |

### (c) FIELD-LENS — memory-systems folds (borrowed, not owned)

- **AnchorMem (anchor-context decoupling):** the anchor (MEMORY.md) is decoupled from the context it points at
  (segments/INDEX). Live instance ALREADY implements this — the anchor holds 2007 bytes of behaviour-critical facts
  plus `@doc:foobar`; the memory (1,334 rendered chars, 7 role/fact anchors) is a load-time snapshot, not the story.
  The #116673 pattern *calls this explicitly* (`@doc:<name>` anchor refs, writes refused until anchor links doc).
- **RippleMem (cue-conditioned completion):** the chain's read-side works because the segments name their topic
  (002 = lessons, 009-cbank = compensations, 011 = doctrine); the INDEX dictates the selection (task → segment).
  This is a **cue-conditioned **shape** — but the completion is *file-op* (read_file), not *cue-conditioned*
  in the RippleMem sense. The borrow for the #116673 read-gap: make the cue-conditioned completion part of the
  *read path* (auto-route the `read` request to INDEX→segment by cue) — the anchor stays, the cue becomes a
  routing key. **Not yet in the running build** (the read-gap standstill is the gate).
- **Chain-of-Memory (dynamic chains):** the chain's own last row (011-doctrine + new segments minted via 005+:)
  is a growing, role-scoped chain; the read-side doesn't care about membership growth — it reads the index.
  Dynamic-chain dynamics are a *future* borrow for the write-side (which is not this lane's lane).

### (d) THE #116673-ALIGNMENT MAP — the chain's design vs the PR's shape

| PR #116673 shape | Chain's live shape (this fork) | Alignment |
|---|---|---|
| Anchor references (`@doc:<name>`); writes refused until anchor links doc | `@doc:foobar` + INDEX → segment routing; the memory tool refuses/writes only on add/replace/remove | **Aligned** — anchor-centric, write-gated |
| `orphan_docs` visibility | The compensation-bank rows + 002:48 keep orphan-bait out of the read path (index→segment is the gate) | **Aligned** — read-side is the orphan filter |
| Cap on anchor only (anchor holds behaviour-critical facts, detail downstream) | MEMORY.md = 2,007 bytes, 9 lines; segments 001–010 + cbank + 011 carry the rest | **Aligned** |
| Read path: recall must be a read path, not a file op (falsifier: rip out `read` → 4 tests fail) | The rig's read-side IS a file op (read_file INDEX → segment); the memory tool removed `read` 2026-02-19 | **Converged on shape; delta on instrument** — the *shape* matches, the *tool* does not |
| Append-only discipline (new knowledge tacks on; nothing evicted) | 001 L1 + 011-doctrine; 005+ mint-new | **Aligned** |
| Read-gap / read-back: the memory tool's `read` removed 56ee8a5cc6 → 002:48 two-way door | The rig's `read_file` compensation (009-cbank row-1, removal gate named) | **Aligned** — the compensation is the transfer; the gate is the release |

The alignment map is a **shape map**, not a code-verified map: the PR is OPEN/unmerged on upstream (009-cbank
row-1: `merge=false`). Where the fork's instance *already* implements the design is the anchor-context decoupling,
the INDEX-first read order, the append-only convention, and the anchor-cap discipline — those are the five receipts
for the adoption case. The remaining delta (read action absent in the running build) is a *compensation gap on the
rig side*, not a design gap on the PR side.

### (e) THE FOLD — recommendation + the honest walls

**Recommendation (one reversible next action):**

- **Keep the anchor as the read-side tip; keep the INDEX→segment file-op as the read path; keep the
  compensation-bank row-1 removal gate in place.** The read-gap is *compensated*, not *cured* — the rig's
  read-side is a two-way door (002:48), and the gate is honest until the upstream PR lands INSTALLED.

**What the live instance PROVES the line can SHOW the network (the adoption case's deepest evidence):**

1. The anchor→chain shape is *live*, not hypothetical: `@doc:foobar` + INDEX (`:8789/memory-chain/`) + segments
   are read, served, and wired today, on this fork.
2. The read-side obeys the #116673 design's contract: anchor references, write-gating, append-only, and the
   anchor-cap discipline — verified by the ACES test cycle (004-network.md) + the regression pass (2026-10-12,
   read-branch triad: baseline 81 → read-branch removed 4 failed/77 passed → restore 81).
3. The field-lenses map onto the rig: AnchorMem's decoupling, RippleMem's cue-conditioned shape, Chain-of-Memory's
   dynamic chain — all are *already* the rig's shape, so the borrow is about *routing*, not *reinventing*.

**The honest walls (what the read-side cannot prove without the upstream's own eyes):**

- **The read action itself is NOT in the running build.** The memory tool removed `read` (56ee8a5cc6); the
  compensation is `read_file` on INDEX/segments — a two-way door, removed only when the installed build carries
  `"read"` (009-cbank row-1 gate). The fork cannot prove #116673's *read* until upstream ships it.
- **The upstream's eyes are not the fork's.** The PR is OPEN/unmerged; the fork has *no* merged fix, no
  installed `read`, and no `gh api` replay of the upstream's own CI against the pinned heads (the XNGG-GAPS
  probes are static line-reads + pattern checks at d1bdb4582c / ffb85c2c58; the dynamic probe of gap-2's
  read-path was blocked by the pin's missing deps — recorded, not fabricated).
- **The read-gap compensation is a two-way door, not a fix.** It is reversible (009-cbank row-1 gate) but it
  does not replace the PR; the network must be told the compensation exists, and that the removal trigger is
  `merge=true` AND `installed-grep>0`, not `merge=true` alone.
- **Not-run / uncertainty (from the standing brief):** the GitHub-hosted window side of the verification is
  NOT RUN (marked); the recitation-length class (the wheel's third) is named, not measured; the fleet's
  independent adjudications are landing in-thread as they complete. None of these change the fork's
  NETWORK-EVIDENCE-STRONG verdict — they sit on the *upstream* side of the adoption case.

**Bottom line for the #116673 adoption case:** the fork's live instance is the *strongest possible* evidence
the line can show *before* the upstream merges: the anchor-chain mechanics are real, wired, and self-consistent
on the fork; the read-gap is named, compensated, and gated; the field-lenses are already the rig's shape. The
adoption case does not wait on the fork — it waits on the break-glass gate (installed `read`), then the fork's
active hand is only to *keep the door open*.

---

## [Artifact register — receipts, never claims]

| # | Receipt | Source | State |
|---|---|---|---|
| R1 | Anchor pointer `@doc:foobar` at MEMORY.md line 1; 2,007 bytes, 9 lines; 001 L93 + 002:42 + 009-cbank disposition | `read_file` on `/root/.hermes/memories/MEMORY.md`; 001/002/009-cbank reads | **Fired** |
| R2 | Chain INDEX at `:8789/memory-chain/INDEX.md`; operational 2026-09-18, hub pve-1; reading order = INDEX → segment → MEMORY.md | INDEX header + reading-order block + 002/004/011 | **Fired** |
| R3 | Segments carry durable knowledge: 001 conventions (L93/L94), 002 lessons (002:42, 002:48, 002:84), 004-network (ACES cycle, 2026-10-12 regression triad), 005+ mint-new, 009-cbank rows 1–5, 009-wins (2026-10-14 battery-loop full + #116673 value-add verified), 011-doctrine (anchored 2026-10-16, 800+ docs) | 001/002/004/005/009-cbank/009-wins/011 reads | **Fired** |
| R4 | C28 segmented view: 25 segments, 113 lessons, 91,881 chars; boundary-aligned | SEGMENT_INDEX.md | **Fired** |
| R5 | Read-side code: `tools/memory_tool.py:280-283` guard present; `read` removed 2026-02-19 (56ee8a5cc6); compensation = `read_file` on INDEX/segments (009-cbank row-1 gate: `merged=true` AND `installed-grep>0`) | XNGG-GAPS-VERIFICATION-20261105.md + 009-cbank read | **Fired** |
| R6 | #116673 design alignment: anchor refs + write-gated, orphan filter, anchor cap, append-only, read-back compensated | 004-network.md ACES + 001/002/009 + R5 | **Converged** (upstream OPEN/unmerged) |
| R7 | Field-lens mapping: AnchorMem (decoupled anchor), RippleMem (cue-conditioned shape), Chain-of-Memory (dynamic chain) | 004-network.md + 001/009 + 006-external-frameworks | **Mapped** |
| R8 | Not-run / uncertainty: GitHub-hosted window NOT RUN (marked); recitation-length class named, not measured; fleet adjudications landing in-thread; upstream's own CI not replayed on the fork | standing brief + XNGG-GAPS + RFC-GUIDANCE-20261105 | **Named, not fabricated** |

**Register rule:** every bullet above is a receipt (date + asserted→status→basis); nothing is a claim without
a provenance entry. The fork's chain reads; it never writes the chain in this lane.
