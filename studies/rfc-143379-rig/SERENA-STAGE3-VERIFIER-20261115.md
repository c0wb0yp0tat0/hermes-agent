# SERENA-STAGE3-VERIFIER-20261115.md

**Stage 3 of the M1.5 two-way-door sprint.** This document defines the acceptance
battery the borrowed-serena integration must pass before the door can close toward
adoption. It covers the verifier spec, the probe shape, the door-closure term,
the meters, and the honest markers. The standing contract is respected: the live
serena mcp internals and the stage-2 harness-leg implementation are not read
here; the design read once, the code never. Everything else is inline.

---

## 1. THE VERIFIER SPEC

The verifier is the acceptance battery for the borrowed-serena integration.
It is a re-read receipt battery, not an appeal to the model's claim. After every
landing, the surface is re-read and the bytes are verified; the model's claim is
not the source of truth.

### 1.1 Postcondition checks

Each write's typed postcondition is verified against the executor's receipt.

- **Hash verification.** The receipt's hash must match the bytes on disk. The
  hash is computed on the landed blob and compared against the digest embedded in
  the receipt; a mismatch is a failure.
- **Typed postcondition fidelity.** The executor's receipt states the postcondition
  the write was supposed to satisfy (e.g., tag set, field updated, record created).
  The verifier re-reads the surface and checks that the postcondition holds in
  the bytes. The model's proposal is here only as the expectation; the receipt and
  the re-read are the evidence.
- **One receipt per claim.** Each write claim carries a receipt (inline-crate,
  design-note, or absent). The verifier checks the receipt's presence and its
  internal consistency; an absent receipt is a failure for the purposes of the
  battery.

### 1.2 Authority gate

The write path's authority attribution is the storm's authority-collapse steer.
The borrow carries a write path in which a privileged-scope write is authorized
only when authority is present and attributed.

- **Which surface authorized the write.** Each write records the surface that
  authorized it (the authority marker carried with the claim). The verifier
  re-reads the receipt and the write record to confirm the marker is present and
  attributable to a real surface.
- **Fail-closed on missing authority.** For privileged scopes, if the authority
  marker is absent, the verifier refuses the write. The door holds closed
  (experimental) rather than opening on an un-attributed claim. This is the
  fail-closed rule: no authority marker means no acceptance, and the unauthorized
  write's claim is not trusted.
- **Precision of the gate.** A write that matches a real authorized marker is
  passed; a write whose claim is unverified or whose marker is bogus is refused.
  The battery measures this precision (see the meters).

### 1.3 Fallback tests

The verifier exercises the fallback path so that the door's knowledge is not
dependent on a single transport.

- **stdio-launch.** The primary path is stdio-launch of the serena mcp tool.
- **HTTP fallback.** If stdio fails, the verifier exercises the HTTP fallback
  exactly once. The fallback's receipt must be landed and verified.
- **Fallback exercised once.** The fallback path is run exactly once per
  verifier pass. One landing, one receipt. This keeps the battery bounded and the
  measurement clear: either the fallback lands and its receipt is verified, or
  the door holds and the alternative is named.

### 1.4 The re-read receipt

After N landings (N is a fixed, small number, e.g. 2), the surface is re-read.

- **Bytes verified, never the model's claim.** The re-read is the ground truth.
  The verifier compares the re-read bytes to the hashed bytes in the receipt.
  A match closes the claim's postcondition; a mismatch is a failure regardless of
  what the model claimed.
- **Receipt attached to the landed claim.** The re-read receipt is the
  post-landing attestation that the write is real. A door that can account for
  bytes, not just words, is closable; a door that rests on claims alone holds.

---

## 2. THE PROBE SHAPE (THE FALSIFIER)

The probe is a seeded verification experiment run against the borrowed-serena
integration. It has two write classes, a verifier run, and measured criteria.

### 2.1 The two write classes

- **(a1) Authorized write.** The authority marker is present, the receipt's hash
  matches the disk bytes, and the executor's typed postcondition holds. This is
  the write the battery must accept and pass.
- **(a2) Unauthorized write.** The authority marker is absent, the claim is
  unverified, and the postcondition is not attributable to any surface. The
  battery must refuse this write and name the authority gap.

The probe seeds both classes in the same population so the verifier is exercised
under realistic mix, and the measured criteria are reported per class.

### 2.2 The verifier run

The verifier runs over both classes and reports:

- the authorized write's receipt verified and the re-read matching the receipt;
- the unauthorized write refused, with the authority gap named;
- the fallback path exercised once (HTTP when stdio fails), its receipt landed.

### 2.3 The measured criteria

- **Authorized write.** Receipt hash verified against the disk bytes; re-read
  matches the receipt. Pass.
- **Unauthorized write.** Refused; the authority gap named. Pass.
- **Fallback.** Exercised once; its receipt landed and verified. Pass.
- **Fallback encoding.** The fallback path is run exactly once; if the first
  attempt fails, the door holds rather than retreating into a second, unbounded
  attempt.

### 2.4 The FLAG condition

The battery is flagged if:

- the unauthorized write's claim passes — the authority gate leaks; or
- the re-read mismatch is accepted — the door accepted bytes it should have
  refused.

If either fires, the door HOLDS open: the PoC does not close to adoption, and the
alternative is named (source-attribution revocation, executor-side enforcement).
If neither fires, the verifier passes and the door may close toward adoption for
the chair's decision, but M2's dispatch is never delayed by this verdict.

**Battery home:** `fixes/falsifier-battery-20261104`, on the write-path axis.

---

## 3. THE DOOR-CLOSURE TERM

The two-way-door's verdict contract is fixed by the verifier, and the adoption
stays with the chair.

- **Verifier measured pass = door CLOSES toward adoption.** The borrowed try
  lands, receipts attach, the authority gate holds, the fallback lands; the door
  closes toward adoption, with the receipts attached and the evidence recorded.
  The adoption itself is the chair's call (the needs-the-chair grid), not the
  verifier's.
- **Verifier FLAG = door HOLDS.** The borrow stays experimental, the hole is
  named, the fallback or alternative is identified, and the door holds open.
- **M1.5 gate stands.** Whatever the door's verdict, M2's dispatch is never
  delayed by the M1.5 verdict. The redundancy of the two-way door is M2/M3's
  leverage, and M1.5 must never gate M2.
- **Door is reversible.** The door closes and holds only by the same
  reversible-to-open terms it opened: the receipts are kept, the authority gap
  is named, and if the flag fires the door re-opens to adoption on the chair's
  terms.

---

## 4. THE METERS

| Meter | Definition | Target |
|---|---|---|
| **receipt-fidelity** | verified receipts / writes | receipts that hash-verified and passed the postcondition check |
| **authority-gate-precision** | authorized passed + unauthorized refused / attempts | authorized writes passed, unauthorized writes refused |
| **re-read-match** | re-reads byte-matching the receipt / re-reads run | re-reads matching the receipt bytes |
| **fallback-success** | HTTP fallback landings / fallback attempts | the fallback landing once, its receipt verified |
| **run record** | `[ABSENT]` unless the fold's execution lands | `[ABSENT]` until the fold runs |

The run record stays `[ABSENT]` until the fold's execution lands, per the
contract. All four measurements above are units tracked against the ticket
legend (see the study's meter table).

---

## 5. THE HONEST MARKERS + TWO-WAY DOOR

- **`[ABSENT]`:** the live serena mcp internals (not read — the contract), the
  stage-2 harness-leg implementation (the design read once, the code never).
  The verifier's value is unverified until execution.
- **Adoption is the chair's.** The verifier does not adopt; it only closes the
  door toward the chair's decision.
- **If the authority gate leaks (FLAG):** the design note stands and the
  alternatives are named — source-attribution revocation and
  executor-side enforcement — never forced. The door holds open and the borrow
  stays experimental.

---

*The verifier completes the M1.5 two-way-door sprint. Its value is unverified
until execution; the honest markers and the door contract are fixed in advance so
that the verdict is a measurement, not a claim.*
