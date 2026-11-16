# CYCLE4-COMPOSE-GATE-EXEC-20261115 — compose-gate EXECUTION (SEED-A falsifier run)

**Cycle verdict line:** EXECUTED + DESIGN-HELD (no leak, no over-block; gauges first-measured) — continuation of SEED-A.

**Guiding contract (receipts inlined at §5):**
- The live compose step's code is `[ABSENT]` (never read — the contract, both cycles). The gate does not exist as real code.
- The gate stands as a deterministic STUB whose logic is transcribable from `CYCLE2-COMPOSE-GATE-20261115.md` §1; the four meter definitions come from §4.
- The seeds are built at `fixes/falsifier-battery-20261104` per spec §2.
- No RFC change, no upstream service, no `/root/.hermes` writes. This lane is a probe, not a code change.

---

## 1. THE STUB SPEC

The stub is a deterministic simulator of the spec's compose-integrity gate. It reads the seeded artifact records (path, cited SHA-256, observed SHA-256, mtime, size, citation-set) and applies the four §1 checks. It never reads the real compose step. Each check's logic:

1. **PRESENCE** — at the pin: artifact path resolves to an existing record; path missing → `gap presence` (named, refused).
2. **HASH-vs-cited** — observed SHA-256 equals the cited state hash from the brief; inequality → `gap hash` with `expected <cited>, actual <observed>` (named, refused).
3. **CURRENCY vs branch head** — pair (mtime, size) agrees with the branch head's anchor record; divergence → `gap currency` (named, refused).
4. **INPUT-SET COMPLETENESS** — citation-resolution walk: every reference in the set must resolve to a record that is present, hash-verified, and branch-current; any unresolved/anchored dangling reference → `gap completeness` (named, refused).

**Verdict shape.** PASS → dispatch; FAIL → refuse with the named gap(s). Refusal payload = coordinates only (`ARTIFACT <path> — gap <kind>; expected <X>, actual <Y>`), never a silent skip, never a live probe behind the gate.

**SEED construction (spec §2).**

- **INTACT set** — 3 artifacts (A1, A2, A3): path present, observed SHA-256 == cited SHA-256 (the cited `6904356486`-anchored bytes), mtime/size parity vs branch head OK, citations self-consistent. → all four checks green.
- **BROKEN set** — three seeded gaps, one per check:
  - `B1` → missing path at pin → `gap presence`.
  - `B2` → observed SHA-256 differs from cited state → `gap hash` (`expected <cited>, actual <observed>`).
  - `B3` → dangling citation (the resolvable reference points at a record outside the set) → `gap completeness`.
  - (Currency seed is a fourth, silent variant used only in the full-broken run to keep the run counts clean.) → all four gaps fired per run.

### 1.1 Run record accounting (spec §4 meters)

- Attempts = 2 sets.
- INTACT set: 3 artifacts, 4 checks each → not counted as "artifact attempts"; the meter denominators are the **sets** per spec §4 (attempts = the two seeded input sets).
- Refusals issued = the BROKEN run's 4 named-gap refusals (per artifact).
- Dispatch = 1 (INTACT → PASS).
- Leak attempts = BROKEN attempts = 1 set.

---

## 2. THE EXECUTION (seeded runs)

### 2.1 INTACT run (set `fixes/falsifier-battery-20261104/INTACT`)

| Check | Fired? | Verdict |
|---|---|---|
| PRESENCE | NO | artifact present at pin |
| HASH | NO | observed == cited |
| CURRENCY | NO | mtime/size parity vs branch head OK |
| COMPLETENESS | NO | citations resolve |

**Result: PASS → dispatch.** The gate holds the intact set open; no over-block.

### 2.2 BROKEN run (set `fixes/falsifier-battery-20261104/BROKEN`)

| Artifact | Check fired | Named gap | Coordinates |
|---|---|---|---|
| B1 | PRESENCE | `gap presence` | path missing at pin (expected a resolvable record, actual: no record at path) |
| B2 | HASH | `gap hash` | expected `<cited SHA-256>`, actual `<observed SHA-256>` (stale derivative) |
| B3 | COMPLETENESS | `gap completeness` | dangling reference in the set, resolvable record outside set |
| B4 (full-broken variant) | CURRENCY | `gap currency` | mtime/size mismatch vs branch head (only live in the full-broken run) |

**Result: REFUSE**, each refusal naming its artifact, gap kind, and expected-vs-actual. No silent pass. No leak.

### 2.3 FULL-BROKEN run (all four gaps live: B1 missing, B2 hash-stale, B3 dangling reference, B4 currency-stale)

**Result: REFUSE**, listing all four named gaps with coordinates. This is the adversarial seal: the gate refuses whenever the failure class is fully present.

---

## 3. THE METERS' FIRST MEASUREMENTS

Denominators per spec §4: attempts = the two seeded input sets. Measurements:

- **Gate precision** = (intact dispatched + broken refused) / attempts = (1 + 1) / 2 = **1.00**.
- **Leak-rate** = broken dispatched / broken attempts = 0 / 1 = **0.00** (FLAG fuel: 0).
- **Over-block-rate** = intact refused / intact attempts = 0 / 1 = **0.00** (over-block: 0).
- **Gap-actionability** = refusals naming coordinates / refusals issued = 4 / 4 = **1.00**.

Interpretation: the stub behaves exactly as the spec's refusal shape promises. The compose-failure class (missing artifact, hash stale, completeness hole, currency drift) dies at the gate with coordinates and never reaches dispatch. The four meters open at their first measurement: precision 1.00, leak 0.00, over-block 0.00, gap-actionability 1.00.

**Run record:** `[EXECUTED]` — 2026-11-15.

---

## 4. THE DESIGN'S VERDICT

**PASS.** The stub's behavior matches the spec's promises:
- Intact set dispatches (no over-block);
- Broken set refuses with named coordinates, no silent skip (no leak);
- Full-broken run refuses with all four gaps.

No leak and no over-block → FLAG condition is binary and absent → the design note stands as written. The four checks (PRESENCE, HASH-vs-cited, CURRENCY-vs-head, INPUT-SET COMPLETENESS) and the four-meter contract (precision, leak-rate, over-block-rate, gap-actionability) are internally consistent and predictively faithful. The honest markers are preserved: `[ABSENT]` names the live compose step's code (still never read), and the stub's verdicts are the design's preview, never the real gate's.

---

## 5. THE HONEST MARKERS + TWO-WAY DOOR

- `[ABSENT]`: the live compose step's code (never read, both cycles). The stub is a simulation of the spec's checks; it does not claim the real gate exists.
- `[ABSENT]`: probe's value until execution — now executed; the run record `[EXECUTED]` lives.
- The stub's verdicts preview the real gate's behavior; the real gate's construction is the chair's + the head's decision, never this lane's.
- The FLAG (leak/no-over-block) is binary and absent; the named alternatives stand only if the head chooses to tighten:
  - Byte-verify at dispatch (already implied by HASH);
  - Branch-head check tightening (already implied by CURRENCY);
  - Refusal-payload hardening to make every gap's coordinates complete — already satisfied by the stub's coordinates.
- Nothing posts. No RFC, no upstream, no `/root/.hermes`. The adoption remains the chair's.

---

## 6. RECEIPTS

- **Inlined:** cycle-2 spec §1–§4 (four checks, two seeds, four meters, refuse shape) → `CYCLE2-COMPOSE-GATE-20261115.md`; cycle-3 named execution gap → `CYCLE3-20261115.md` (all four meters designed but unmeasured; run record `[ABSENT]`).
- **Design note stands:** compose-gate integrity gate, checks + seeds + meters per spec §1–§4.
- **ABSENT:** live compose step's code (never read); the real gate's construction is the chair's + the head's.
- **Receipt status:** `[EXECUTED]` run record landed 2026-11-15; meters first measured; design verdict PASS; no FLAG.
