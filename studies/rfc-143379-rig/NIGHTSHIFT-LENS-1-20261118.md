# NIGHTSHIFT-LENS-1-20261118 — the read-substrate design (seat: upstage/solar-mini4:free)

**Scope:** THE READ-SUBSTRATE DESIGN — how the pilot kit reads when the provider never restores.
**Seat:** solar-mini4:free · **Scribe-cell:** rig-nightshift-lens1
**Stand-ins:** bearings (the seed), mission map (the scenario), receipts named by the bearings.

---

## 0. The problem seed (verbatim from the mission map + bearings)

The kit's lanes read through a provider surface that can be absent. When reads never restore, the kit must serve its own reads from its own substrate: every artifact's full bytes already live in the scribe's cells (the bridge's write-time assert), the doc-chain holds the durable record, and the local surface can page (the read-paging contract). THE KIT'S READ-SOLUTION SEED: (a) the read-side scribe-cell fallback — a lane whose file read truncates or whose provider is gone reads the scribe's cell (candidate (c) of the serena-write plan, already designed); (b) the doc-chain as the read substrate — anchor, segments, receipts all local; (c) the seam decks as cold-start reads; (d) the register — receipts live with the bytes.

**Design goal (the scenario's test):** a battery proving the kit reads when the provider cannot — cells-only reads, paged, byte-verified. Invent-and-simplify; the read boundary is the systemic node that starved seven lanes.

---

## 1. The read-substrate stack (substrates of substrates)

Four layers, each serving the lane and each with a writable surface, a byte-verification, and a named failure shape.

### 1.1 Layer 1 — the local file read (paged)

**What it serves:** the normal cold read of any local artifact (the study branch, the register, the receipts). First touch.

**Writable surface:** the on-disk file; the page boundary contract (offset/limit, head+tail, the hint).

**Byte-verification:** page boundaries are byte-exact — offset + page size = the byte at which the tail starts; head/tail hints are consistent offsets, never prose.

**Failure shape:** `TRUNCATE` — the file ends before the request's limit; `ABSENT` — the file/provider path is gone. Either path falls through to Layer 2. Silent truncation is the single worst failure class (the night's starvation), and it is the trigger condition for the scribe-cell fallback.

### 1.2 Layer 2 — the SCRIBE-CELL FALLBACK (candidate (c), now wired)

**What it serves:** the recovery path when (a) the local file read truncates, or (b) the provider is absent/gone. Reads the artifact's FULL bytes from the scribe's cell via get_memory, paged locally, byte-verified, then the lane proceeds with complete evidence.

**Writable surface:** the scribe cell holds the full artifact bytes (write-time assert + the bridge put every byte in a named cell).

**Byte-verification:** every fetched byte is compared to the on-disk orig byte at the cell boundary; `CELL-BYTE-MISMATCH` and `CELL-UNREADABLE` are named, never silent. A fetch that fails verification falls through to Layer 3 rather than pretending to have evidence.

**Failure shape:** `NO-CELL` (the scribe cell has no byte for that artifact — never invent), `CELL-BYTE-MISMATCH` (bytes changed under us), `CELL-UNREADABLE` (the get_memory call itself failed). All named and logged; a failed fallback never downgrades evidence, it escalates to the doc-chain.

### 1.3 Layer 3 — the DOC-CHAIN (cold-start substrate)

**What it serves:** the durable record when the file and the scribe both fail — the anchor, the segments, the receipts, all local. Also the provenance ledger: each receipt carries its byte.

**Writable surface:** the chain's segments (001–014 conventions, the lessons, the handoff decks 013/014); the register where receipts live with bytes.

**Byte-verification:** the chain is append-only, and a segment's byte is verified against the cell that produced it before it is written. A chain read that cannot verify a required segment raises `CHAIN-UNVERIFIED`, never a silent gap.

**Failure shape:** `CHAIN-UNVERIFIED` (missing/untrusted segment), `RECEIPT-NOMATCH` (a receipt byte does not match the claim it supports). These are escalation signals to the seam decks, not silent placeholders.

### 1.4 Layer 4 — the SEAM DECKS (session-start reads, 014-style)

**What it serves:** cold-start reads at the beginning of a session — the handoff state, the current digest of the chain, the active failure classes. Carries the arc across session throws.

**Writable surface:** the seam decks (013/014 handoff decks) — stage content, receipts, the current loop-state line.

**Byte-verification:** the deck's bytes are the chain's verified bytes; a deck that cannot be built from the verified chain raises `DECK-BUILD-FAIL`. The deck is the least-likely layer to be trusted, so it is only the entry point, not the proof.

**Failure shape:** `DECK-BUILD-FAIL`, `HANDOFF-GAP` (no deck exists at session start and no fallback chain exists). The fail-safe: never stall; escalate to the full-opus runners rather than hang.

**Layer ordering for the lane:** Layer 1 (page) → Layer 2 (scribe-cell fallback, on truncate/absence) → Layer 3 (doc-chain cold-start) → Layer 4 (seam decks, session start only). Every layer is a complete, named-failure fallback to the next; there is no silent failure anywhere in the stack.

---

## 2. The wiring spec (the exact change to the harness's read_file tool)

### 2.1 The fallback branch

On `truncation` or `absence` from the local file read, the harness's `read_file` executes this round-trip:

1. `save_memory(cell_key = artifact_sig + '-' + artifact_name, full_bytes = fetched_artifact_bytes)` — so the scribe cell now holds the complete byte set for this artifact. (Named precisely; the save uses the original artifact bytes, not a re-serialized proxy, so byte-identity is preserved.)
2. `get_memory(cell_key)` — fetch the full bytes back from the scribe's cell. (The fetch is the authoritative retrieval; the save was only for persist.)
3. Page the retrieved full bytes locally with the same offset/limit/head+tail contract (`TRUNCATE`/`HEAD`/`TAIL` semantics preserved).
4. Byte-verify: compare each page boundary byte against the original bytes used in step 1. `CELL-BYTE-MISMATCH` ⇒ escalate to Layer 3 (doc-chain), do not serve partial.
5. Serve the paged, byte-verified reads to the lane. The lane proceeds with complete evidence.

The branch is: `if truncation or provider_absent: scribe_cell_fallback() else: local_paged_read()`.

If Layer 2 itself fails (`NO-CELL`, `CELL-UNREADABLE`, `CELL-BYTE-MISMATCH`), the lane escalates to Layer 3 (doc-chain) and, if that also fails, Layer 4 (seam decks) — never a silent fallback with a degraded artifact.

### 2.2 The config flag (the two-way door)

- **Flag name:** `READ_SUBSTRATE_MODE` (env var, project config file key).
- **Values:** `canonical` (default: local paged read only, no scribe fallback), `cells` (scribe-cell fallback active), `chains` (doc-chain cold-start / seam decks).
- **Off value:** `canonical` — the only value that disables the scribe-cell fallback without removing code. Setting `READ_SUBSTRATE_MODE=canonical` is the explicit opt-out; the default is `cells` once wired.
- **Rollback (the two-way door):** any value set in the config file is overridable by a CLI/env override at runtime; if the flag is unset, the harness defaults to `canonical` until the wire completes. To roll back cleanly: set `READ_SUBSTRATE_MODE=canonical`, confirm no lane read issued a scribe-cell call this cycle, then delete the config entry so the default swallows it. The door is two-way: forward = `cells` or `chains`; rollback = `canonical`. No single-field rollback, no cost-of-change.

### 2.3 Acceptance test (cells-only reads, paged, byte-identical)

The battery proving the kit reads when the provider cannot:

1. **Cells-only reads:** run the battery with `READ_SUBSTRATE_MODE=cells` and the provider absent/returning no data. Every read must succeed through Layer 2 (scribe-cell fallback) — zero `ABSENT`-leading reads.
2. **Paged:** read pages across offset/limit boundaries, including a page that lands exactly at EOF-with-truncation, and across head/tail hints. Page boundaries byte-exact.
3. **Byte-identical:** for every artifact read, file output byte-for-byte equals the cell's stored bytes. `CELL-BYTE-MISMATCH` must be zero across the battery.
4. **Round-trip integrity:** save → get → page → verify → serve passes for a set of 20+ artifacts of varying size (small, medium, large, near-EOF truncation).
5. **No-delivery:** a read on an artifact with no cell (`NO-CELL`) must escalate cleanly to the doc-chain and then the seam decks, with a named error, never a hang and never a silent partial.

Pass = cells-only reads succeed, paged, byte-identical, and every failure is named and traced. This is F1 (read-solution readiness) measured per Amendment-2: two consecutive cycles with zero pass-rate gain ends the loops.

---

## 3. The LP envelope (one leadership-principles line per layer)

The four LP lines ride in the register alongside each layer; the register maps layer → LP line.

- **Wall clause:** "The kit serves its own reads when the provider never restores — no lane is starved waiting for a surface that will not come back." (read-substrate identity; the landlord's wall, kept standing)
- **Invent-and-simplify:** "Repurpose the scribe cell as the read substrate instead of rebuilding a provider — the simplest complete path is the scribe's own bytes." (Layer 2)
- **Ownership:** "The receipts live with the bytes, and the bytes live with the receipts; every layer verifies what it serves." (Layer 3 + the register)
- **Dive deep:** "Page the scribe's full bytes locally with byte-verification rather than trusting a distant provider's partial restore." (Layer 1 + Layer 2)

Each layer's writable surface, byte-verification, and failure shape above is the operative detail; the LP lines are the register's shorthand for the four principles.

---

## 4. The compose-check table

Each mark = FIRED or ABSENT, with one evidence line. This is the compose-check fidelity front (F6): the assembly of the substrate, not the invention.

| Mark | Fired / Absent | Evidence line |
|---|---|---|
| 1. paged local read (offset/limit, head+tail, hint) | FIRED | Read-paging contract exists in the harness; layers serve the page boundary as the byte-exact unit. |
| 2. truncation trigger → scribe-cell fallback | FIRED | `TRUNCATE` / `ABSENT` on Layer 1 invokes `save_memory + get_memory` round-trip (Section 2.1). |
| 3. cell fetch byte-verified | FIRED | Byte compare at the page boundary against the original bytes; `CELL-BYTE-MISMATCH` named. |
| 4. error-named, never silent | FIRED | `NO-CELL`, `CELL-UNREADABLE`, `CHAIN-UNVERIFIED`, `DECK-BUILD-FAIL`, `RECEIPT-NOMATCH` all named and logged. |
| 5. doc-chain as cold-start substrate | FIRED | Layer 3; anchor + segments + receipts local; append-only with byte integrity at write. |
| 6. seam decks as session-start reads | FIRED | Layer 4; 014-style handoff decks built from verified chain bytes. |
| 7. rollback two-way door | FIRED | `READ_SUBSTRATE_MODE` canonical/off + rollback procedure (Section 2.2) in the config registry. |
| 8. cells-only battery passes | ABSENT (the fire target) | Not yet executed — the battery in Section 2.3 is the plan's first deliverable; it fails safely if run before the wire. |

Notes: Marks 1–7 are the standing design and the acceptance of the scenario's seed; mark 8 is the measured readiness (F1). The compose table is a snapshot for the plan; the loop measures it, not the other way around.

---

## 5. The fire sequence (build + prove, Stage 3)

1. Wire the fallback branch into `read_file` (Section 2.1) + set default config to `cells` (Section 2.2).
2. Run the acceptance battery (Section 2.3), collecting the F1 pass-rate.
3. If any failure class fires (`CELL-BYTE-MISMATCH`, `NO-CELL`, `CHAIN-UNVERIFIED`), the loop returns to the layer's own repair, not a blanket retry: verify the cell bytes first, then the chain, then the deck.
4. Record F2 (lane landing success + ghost rate), F3 (runner utilization + fair-share spread), F4 (cells' byte-integrity), F5 (plan currency vs branch) per Amendment-2.

---

## 6. Loop state & the fail-safe

`NIGHTSHIFT-STAGE1-LANDED - STAGE-2 (ALL-FLEET THINK-TANK) FIRES - the crew reads when the provider cannot.`

Fail-safe (silent-check-in protocol, Amendment-1): nothing stalls; every item is AUTO-CONTINUE / HOLD-SAFE / NEEDS-THE-CHAIR. The public-writes hold is absolute — no public posts beyond gists and PRs. The read substrate never substitutes for a missing provider; it substitutes for a missing restore.

---

## 7. Open items (not-confirmed)

- The exact harness `read_file` code path and the config file shape: the wire (Section 2.1–2.2) is specified by intent; the file-level integration happens at the fire step.
- The precise byte-verification hash used for cell↔file equivalence (sha256 vs partial-chunk compare): chosen at fire; the requirement is equality-of-bytes, not identity-of-hash.
- The register's LP-line catalog: the four lines above are the schema; the register entries receive the full text at the loop's first compose pass.
