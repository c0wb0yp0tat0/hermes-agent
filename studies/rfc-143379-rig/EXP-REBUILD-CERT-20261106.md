# EXP-REBUILD-CERT-20261106 — the stress-cells' independent certification (the ACES-loop's audit-pass, flight 1; 2026-11-06 06:35)

## Verdict: CLEAN

The rebuild's two new fixtures pass every byte-adjudication they are held to. The rebuild's
cell-substance is real; the verdict rides the fixtures the receipts ledger cites, nothing else.
The ladder's depth-vs-density separation is NOT certified by these bytes — witness those
bytes below.

## 1. Byte-verification (the receipts ledger vs `git hash-object`)

| Ledger-cited blob | Fixture | Re-derived `git hash-object` | MATCH |
|---|---|---|---|
| `78b9917de2ce18ba76ca09eb9377b3e90e6c1927` | `rungs/fixture-deep-compaction-real.json` | `78b9917de2ce18ba76ca09eb9377b3e90e6c1927` | YES |
| `b808da18b5fe99387880ee6266aae7625ed7dbaa` | `rungs/fixture-high-density-real.json` | `b808da18b5fe99387880ee6266aae7625ed7dbaa` | YES |

Both cited blobs re-derive identically on the branch head `c2307e47fa`. The receipts ledger
is internally consistent with the bytes on disk.

## 2. Pairwise-distinctness (messages-content sha256, per the receipts ledger)

Ledger pairwise table (RECEIPT 2026-11-06):
- deep-real `13283b9f4ab7…` vs high-real `409536cff4ab…` → differ (False)
- deep-real vs rung-1 `b992e29b7d7f…` → differ (False)
- high-real vs rung-1 → differ (False)

Witness from the fixtures (head fields):
- Cell A `source`: `/root/.hermes/sessions/session_20261007_123305_f3465b.json`
- Cell B `source`: `/root/.hermes/sessions/request_dump_local-1c11cf0fe057f35a3bca5f3620cfdd96484f99b7f10109464792c8f92ac7815d_20261104_000244_985190.json`
- Cell A `messages` head: 8 (roles assistant/tool, tool_calls present)
- Cell B `messages` head: 2 (system + 219,239-byte user turn)

Cross-check the prior LADDER-AUDIT (`AUDIT-LADDER-RUNGS-20261106.md`) charge against these cells:
- Old rungs 4-5 were byte-identical in messages to rung-1 (`deep == high == config: True`);
  `source` identical in all three (the old config fixture class).
- The new cells clear that exact charge: distinct `source` lines, distinct message
  structures (8-message compaction-path vs 2-message dense-stream), no shared messages content.

## 3. Labels' honesty

Cell A `description` (deep-compaction): "The rig's real turn-session transcript (2026-10-07…),
the compaction-path's structural receipts (message_count 8, session_start 2026-10-07T12:33:05,
platform cli). Distinct source from every other rung; the small+old class's real bytes."
→ Constructed exactly from the fixture's bytes.

Cell B `description` (high-density): "The rig's recurrence-bearing real stream (the request-dump
family …), the membership wave-18's real-ground class): one dense 219,261-byte user turn vs
the 30,893-byte retained system … the retry-captures (max_retries_exhausted) as the stream's
recurrence receipts."
→ Constructed exactly from the fixture's bytes.

The honest label the rebuild carries: SEPARATION is NOT certified by the build — it rides the
battery (the run-side, at the substrate-pin `a996d4ad`). No description over-claims what the
fixtures alone can deliver.

## 4. Per-claim table

| Claim | Byte-evidence | Verdict |
|---|---|---|
| Ledger cited blobs match branch bytes | `git hash-object` re-derived, both fixtures | PASS |
| New cells are distinct from rung-1 | `source` differs; messages differ | PASS |
| New cells distinct from each other | `source` different; message counts 8 vs 2 | PASS |
| Old rungs 4-5 identical to rung-1 (old charge) | verified: `AUDIT-LADDER-RUNGS-20261106.md` | PASS (old charge cleared) |
| Depth-vs-density separation certified by the build | battery measurement required | UNVERIFIED (substrate-pin battery rides the ledger) |

## 5. Corrective / noted items

- None.

## 6. The one next-mechanism line (evidence-to-evidence: these fixtures only)

The probe-banks ride the two fixtures above; their expected-facts derive from the fixture heads
(source lines + messages shape): deep-real carries a 3-call compaction-loop receipt and a
session-dump source; high-real carries a 219,239-byte dense user turn and a request-dump source;
both scrubbed_by the same scrubbing_passes list, `truncated_to: null`. The weighting-separation
question rides the battery at the substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`.
