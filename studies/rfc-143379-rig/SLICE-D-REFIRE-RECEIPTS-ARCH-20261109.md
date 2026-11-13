# SLICE-D REFIRE — receipts-architecture (t=0)

## 1. Schema-rows' confirmation (5-field compliance)

Ring-0 receipt (ring-0-byte-closure-1957.md) fields:
- ring-id ✓
- g-arc ✓
- receipt-path ✓
- artifact-sha256 ✓
- land-timestamp ✓
All 5 present. Compliant.

## 2. Receipts-dir's seeding-inventory

Present: ring-0-byte-closure-1957.md (1 row).
First pass landings must add: G0-G4 arming-rows' receipts (5 rows, one per gate), first dispatch delivery receipt (t=0+10m), first verification probe receipt (t=0+20m), mid-hour drift receipt (t=0+35m), second dispatch receipt (t=0+50m, conditional), hour-close sealed artifact (t=0+58m).

## 3. Ledger's opening-entries' rows (launch-pass landings)

Arming-rows: G0 θ0 armed T-0 (always on); G1 θ1 armed T-15m; G2 θ2 armed T-10m; G3 θ3 armed T-5m; G4 θ4 armed T-2m.
Coverage: 6 first-hour items (t=0+0m … t=0+58m) each with exit criterion.
Progress-row's receipt: hour-close sealed artifact committed (item 6) = ring-0 pattern (byte-closure triple: HEAD, diff-stat empty, sha256).

## 4. DIRECT-APPLICABLE rows (traced)

- D1: Receipt schema = 5-field (source: ring-0-byte-closure-1957.md lines 3-7).
- D2: Arming sequence G0-G4 (source: LAUNCH-EXECUTION-PLAN §1.1).
- D3: t=0 trigger = operator's GO single-signal (source: §2, §3).
- D4: First-hour 6-item block (source: §1.3).
- D5: Ledger's 5 findings + 1 in-flight (source: G0-LEDGER entries 1-5 + ~08:0X row).

## 5. 5-why + webstorm (depth-clause)

Why receipts must be byte-direct: ledger entry 2 (audit-lens byte-misread) shows surface-inferred verdicts get refuted. Why 5 fields: ring-0's triple (HEAD/diff/sha) is the verification core; the 5 fields wrap it with identity+time. Why operator's word sets t=0: no partial fire (§3 hard rule) — clock is a consequence, not a trigger. Webstorm: the receipts-dir is currently seeded with only the ring-0 row; every launch-pass landing must mint its own receipt in the same 5-field shape, or the ledger's "honest findings" meter loses its byte-evidence and reverts to surface-inference (the refuted pattern).