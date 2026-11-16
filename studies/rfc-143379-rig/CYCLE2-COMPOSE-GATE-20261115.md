# CYCLE-2 SEED-A — Pre-Compose Integrity Gate (Compose-Failure Class Elimination)

## 1. THE GATE SPEC

**Purpose.** Before any lane-ride dispatch (the day's compose step), validate every input artifact's integrity at the seam. The gate sits *before* the ride fires, so the compose-failure class (read-scatter ×3, write-overwrite ×1, the four FAILED-REDEEMED rides of `SPRINT-PLAN-20261115.md` §1) dies at the gate, never in the ride.

**Checks (per input artifact).**
1. **PRESENCE at the pin.** Artifact exists at its referenced path; missing artifact = named gap → refuse.
2. **HASH vs cited state.** Artifact bytes' SHA-256 matches the brief's cited state hash; mismatch = named gap → refuse.
3. **CURRENCY vs branch head.** Artifact's mtime/size (or a stored checksum parity) agrees with the branch head; stale = named gap → refuse.
4. **INPUT-SET COMPLETENESS.** No dangling references between the briefs and the plan; every citation resolves to a present, hash-verified, branch-current artifact.

**Refusal shape.** Dispatch refuses with the *named gap*: `REFUSED: <artifact path> — gap <presence|hash|currency|completeness>; expected <X>, actual <Y>`. Never a silent skip; never a live-encode/write probe behind the gate.

**Integration point.** The gate sits at the compose step's launch seam — same point the day's launch-preconditions hardened — so the gate evaluates on the first attempt for the next sprint-plan composition. Pass ⇒ dispatch; fail ⇒ refuse + named-gap payload; no silent pass.

## 2. THE PROBE SHAPE (the falsifier)

Seed two compose-input sets at `fixes/falsifier-battery-20261104`:
- **INTACT set** — all artifacts present, hashes matching, branch-current.
- **BROKEN set** — one artifact missing, one hash stale, one dangling reference (exactly the failure class the gate catches).

Run the gate over both. Measured criteria:
- INTACT set → PASSES and dispatches (no over-block).
- BROKEN set → REFUSES with named gaps (which artifact, which hash, which ref) — no silent pass.
- FLAG condition: BROKEN set dispatches (the gate leaks) OR INTACT set refuses (the gate over-blocks) → gate FLAGGED; design note stands, alternatives named (byte-verify at dispatch; branch-head check tightening), never forced.

## 3. THE NAMED-GAP TERM

Refusal payload = coordinates only: artifact path, expected vs actual hash, dangling reference. Example:
`REFUSED: <artifact> — gap hash; expected <brief-cited SHA-256>, actual <observed SHA-256>` (or `gap presence` / `gap completeness` / `gap currency` with the concrete ref). The refuse is actionable for the human or the head — never a wall.

## 4. THE METERS

- **Gate precision** = (intact dispatched + broken refused) / attempts
- **Leak-rate** = broken dispatched / broken attempts (FLAG's fuel)
- **Over-block-rate** = intact refused / intact attempts
- **Gap-actionability** = refusals naming their coordinates / refusals issued
- **Run record** = `[ABSENT]` until the fold's execution lands.

## 5. THE HONEST MARKERS + TWO-WAY DOOR

- `[ABSENT]`: the live compose step's code (not read — the contract); the probe's value unverified until execution; the adoption is the chair's.
- If the gate leaks or over-blocks: the design note stands and the alternatives are named — byte-verify at dispatch, branch-head check tightening — never forced.

*One tool call per round; skeleton by round 3; ≤6,000 chars/write; commit+push ONCE at the END.*
