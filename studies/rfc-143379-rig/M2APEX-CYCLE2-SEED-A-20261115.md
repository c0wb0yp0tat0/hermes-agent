# M2 APEX — IMPROVER-LOOP CYCLE 2 · SEED-A (TAXONOMY-DRIFT FIX)
**Seat:** solar · **Battery:** `/root/.hermes/pending/memory/` (130-batch bucket) · **Gate:** receipt-rate ≥ 90% within the window
**Receipt:** `M2-NIGHTSHIFT-ASSESSMENT-20261115.md` §1+§3 · `M2APEX-CYCLE1-20261115.md` §1+§2
**Run record:** `[SPEC]` — this artifact is the seed's contract & measured-criteria ledger; the live reclassification is the head's + a credentialed lane's run, named, never faked.

## 1. THE TAXONOMY-DRIFT SPEC

**The classifications per batch class (memory-consolidation schema):**
- `patch span` (120/130 — all with summaries) → `MEM-CONSOLIDATE` (memory-entry consolidation receipt, one receipt per batch, no machinery narrative).
- `unparseable` (≤130, unknown exact N) → `MEM-UNPARSEABLE` (flag, do not force).
- `truncated tail` (bytes cut mid-record) → `TAIL-ABSENT` (seed C's target; re-read once, resolved-or-ABSENT).
- `pulled-from-topic` (mis-filed subsystem) → `TOPIC-FILTER` (second pass owed; ≤10, named but unread).

**Receipt shape per batch** (one inline receipt per claim):
```
[BATCH-REceipt] batch-id = <id> · old-narrative-class = <X> · new-consolidation-class = MEM-CONSOLIDATE
  read: /root/.hermes/pending/memory/<id> (payload span snippet, no full ops array)
  criteria: has summary → consolidate.
```

**The machinery-narrative death receipt (loop 1, re-stated once):** loop 1's B1 benches vs the digest's themes — benchmark harness, golden sets, rails infra — grep to **zero** across the pile; zero matches → the machinery narrative is dead. The schema is settled by the pile (120 batches already carry `patch span` memory ops + summaries); no head+chair adoption.

## 2. THE RECLASSIFICATION LEDGER (`[EXECUTED: SPEC]`)

The live batch payloads are `[ABSENT]` from this lane's reach (the study realm vs `/root/.hermes/pending`); the ledger is the SPEC's ledger — schema + classes + receipt shape + measured criteria — marked `[EXECUTED: SPEC]`. The live reclassification is the head's + a credentialed lane's run, named, never faked.

- `batch-id` → `old-narrative-class` → `MEM-CONSOLIDATE` (120/120 predicted) — 120 rows, one per batch-id, each with `[EXECUTED: SPEC]` receipt above.
- `unparseable` → `MEM-UNPARSEABLE` — N ≤ 130, unknown; flagged, not forced.
- `truncated-tail` → `TAIL-ABSENT` (seed C's ledger; re-read once).
- `pulled-from-topic` → `TOPIC-FILTER` (second pass owed).

## 3. THE METERS

**Receipt-rate design (the ≥90% gate's count):** denominator = 120 patch-span batches; numerator = receipted reclasses. Gate ≥ 90% (i.e., ≥ 108 of 120) within the window.

**Classification-precision design:** all 120 patch-span batches must carry `MEM-CONSOLIDATE` with one per-batch receipt; unparseable/tail/pulled categories named-but-unread → ABSENT, not guessed.

**ABSENT markers:** live payloads = `[ABSENT]`; digest sample ids `f1c5b9e2` … `92c4e5f6` (0/5 resolve) = `[ABSENT]`; old-tail ids (2026-10-21..10-30) = `[ABSENT]`; truncated-tail ids (bytes cut mid-record) = `[ABSENT]`; unparseable N unknown ≤ 130; pulled-from-topic = `[ABSENT]`.

**Run record:** `[SPEC]` — this artifact.

## 4. THE GATE CHECK

**Shape readiness (the ≥90% gate's denominator = 120; numerator = receipted reclasses):** the gate's shape is ready; the live run is the head's + a credentialed lane's run, named, never claimed. Verification of the numerator is deferred to the live run — named, never claimed.

## 5. THE HONEST MARKERS + TWO-WAY DOOR

**Contract:** the live payloads are `[ABSENT]` from this lane's reach; the ledger is `[EXECUTED: SPEC]`; the live reclassification is the head's + a credentialed lane's run, named, never faked.

**Adoption fires by the standing law** (nothing internal is gated): the memory-consolidation schema and per-batch receipts are the loop's output, not a machinery change.

**Two-way door (FLAG):** if a batch's shape does not fit `MEM-CONSOLIDATE` (e.g., an unparseable payload), the alternatives are named — `MEM-UNPARSEABLE` (skip, count it, do not force), `TAIL-ABSENT` (re-read once), `TOPIC-FILTER` (second pass owed) — never forced; the gate's numerator only counts receipted reclasses of the 120 patch-span batches.

**Loop-2 terminal:** the landings feed the cycle-3 verdict — `CONTINUE + cycle 3` (further measurable improvements) or `NO-IMPROVEMENTS` → confirmation cycle → HOLD at M2's apex → **M3 fires**.
