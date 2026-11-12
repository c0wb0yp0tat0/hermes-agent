# CRITERIA-BLIND SELF-TEST — REPORT (2026-11-11)

## STEP 1 — EXECUTE (the arm under test)

Arm: `tests/s2u_arms/test_instruction_faithful_gate.py`
Command: `cd /root/workspace/repos/hermes-agent && python3 -m pytest studies/rfc-143379-rig/tests/s2u_arms/test_instruction_faithful_gate.py -q`

**VERDICTS: PASS / PASS** (both rig-form tests executed cleanly on the paid generative tier).

Test 1 `test_gate_rejects_self_authored_declaration`: PASS
- `assert "gates" not in msg and "CLOSED" not in msg` — the declarer's table (gates.classes=CLOSED) never appears in the gate's verdict.
- `assert ok` — the mechanical receipts carried the gate.

Test 2 `test_gate_uses_only_mechanical_inputs`: PASS
- every field in the verdict was built from artifacts/ledger rows, none derived from the declarer.

## STEP 2 — INTERROGATE MY OWN VERDICT (self-test)

### (a) Origin of the verdict
The report's "reason the gate refuses" is **derived from the test's actual output**, not from expectation:
- If a test had failed, the gate would have quoted a stale receipt by name and age (`"stale receipt: the design's landing is N min old"`) — that is precisely the shape the test asserts must appear when fresh-artifact proof is absent. No such reason was emitted, because the three artifacts exist and are fresh (<30 min), and the ledger rows carry `"req_bytes"` in the fresh-test era.

### (b) Criteria-blind survival
**Yes.** The gate's acceptance criterion is mechanical: (1) the three ARTIFACTS exist, (2) each is <30 min old, (3) the ledger contains ≥1 row carrying `"req_bytes"`. The declarer's `"gates"` table and `"verdict"` field are structurally inadmissible — the assertions explicitly forbid the gate from ever consulting them. A criteria-blind auditor re-running the gate against the receipt files alone would reach the same GREEN, because the verdicts are receipts-only; my report's language about the "reason the gate refuses" is descriptive only and carries no evidential weight.

### (c) Weakest assumption
**The fixed ARTIFACTS list with hash-verified landed receipts.** The gate hardcodes `design`, `synthesis`, `record` paths and checks existence + mtime. It can be fooled:
- **Missing receipt:** if any artifact is deleted, the gate returns `missing receipts: [...]` — honest but brittle; the gate does not verify *content* hashes, only existence, so a stale or placeholder file with the same name still passes.
- **Mtime replay:** mtime is writable/tamperable; a stale receipt can be "recent" by touching it. The gate trusts the clock, not provenance.
- **Ledger discriminator:** the row filter `"req_bytes" in line` is a string containment test — any line carrying that substring passes, even if it is a malformed or out-of-era echo. A spoofed ledger row (or a test fixture re-used from the battery) can manufacture the third receipt out of band.

**Concrete improvement to the arm:** replace existence/mtime with a content-hash receipt (e.g., SHA-256 of the file compared to a pinned manifest) and make the ledger discriminator exact: require the row's `"req_bytes"` to be parsed with a schema validator (JSON field) rather than a substring grep, and tie the epoch freshness to the ledger row's own timestamp field rather than to the artifact's mtime. This closes both the content-integrity hole and the clock-replay hole with mechanical receipts the gate can actually trust.