# PROBE-BANKS-20261106 — the seam-arc's bank-protocol over the two real cells (the REBUILD-ARM's next)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Gate:** the REBUILD-CERT landed CLEAN (`EXP-REBUILD-CERT-20261106.md`, rowed). **Seat:** the curriculum-ladder's probe-banks. **Register:** receipts, never claims — every expected-fact below is grep-verified present in the cited fixture's bytes by the build script (deterministic, no model).

**The bank-protocol (the seam-arc's):** recall / artifact / decision / continuation — each bank's probes ask at the continuation point, and every probe's expected-facts MUST be present in the fixture's messages (the ground-truth the probes are read against).

**The anchor-note (the number-seam, named):** the fixtures' descriptions carry source-era sizes (deep: the raw turn-session; high: `219,261`-byte user turn, `30,893`-byte system — the source dump's pre-scrub measures). The fixtures' OWN bytes re-derive differently under JSON-escape: high's user turn = 219,239 chars / 221,226 escaped bytes; system = 30,846 chars / 31,367 escaped bytes. Both anchors are true of their own object; the banks' expected-facts are FIXTURE-anchored unless flagged SOURCE-anchored. The one retry-receipt (`max_retries_exhausted`) lives in the SOURCE dump's `reason` field (verified live: the raw `request_dump_local-1c11cf0fe…_20261104_000244_985190.json`, `reason: max_retries_exhausted`, the 404-family) — it does NOT appear in the fixture's messages; the retry-receipt row is flagged SOURCE-anchored accordingly.

**The honest wall:** the banks certify the facts' PRESENCE in the bytes (the ground-truth for the battery's probes) — they do NOT certify the depth-vs-density separation; that rides the battery at the substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`.

## The cells' byte-shapes (measured 2026-11-06, the build)

| Cell | Fixture | messages | shape |
|---|---|---|---|
| A | `rungs/fixture-deep-compaction-real.json` | 8 | the compaction-path: user open → 3× (assistant `execute_code` → tool) → user close; source `session_20261007_123305_f3465b`, model `control-model` |
| B | `rungs/fixture-high-density-real.json` | 2 | system 30846 chars + user 219239 chars (the many-facts-per-turn density shape); source the request-dump family `local-1c11cf0fe…`, model `poolside/laguna-xs-2.1:free` |

## Cell A — the deep-compaction bank (the small+old class)

| Bank | Expected-facts (byte-verified, the fixture's own bytes) | Receipt (occurrences in the fixture) | Anchor |
|---|---|---|---|
| A1 | message count — `"role"` | 8 | fixture |
| A2 | execute_code loop calls — `execute_code` | 3 | fixture |
| A3 | tool-output pairs — `"role": "tool"` | 3 | fixture |
| A4 | session id token — `session_20261007_123305_f3465b` | 1 | fixture |
| A5 | session start stamp — `2026-10-07T12:33:05` | 1 | fixture |
| A6 | model pin — `"control-model"` | 1 | fixture |
| A7 | truncated_to null — `"truncated_to": null` | 1 | fixture |
| A8 | source path — `/root/.hermes/sessions/session_20261007_123305_f3465b.json` | 1 | fixture |
| A9 | user open message chars — `77` | 1 | fixture |
| A10 | user close message chars — `188` | 1 | fixture |
| A11 | open-message head token — `Control` | 1 | fixture |

## Cell B — the high-density bank (the dense-stream class)

| Bank | Expected-facts (byte-verified, the fixture's own bytes) | Receipt (occurrences in the fixture) | Anchor |
|---|---|---|---|
| B1 | message count — `"role"` | 2 | fixture |
| B2 | system turn chars — `30846` | 1 | fixture |
| B3 | user turn chars — `219239` | 1 | fixture |
| B4 | user turn escaped bytes — `221226` | 1 | fixture |
| B5 | system turn escaped bytes — `31367` | 1 | fixture |
| B6 | source path — `/root/.hermes/sessions/request_dump_local-1c11cf0fe057f35a3b` | 1 | fixture |
| B7 | model pin — `"poolside/laguna-xs-2.1:free"` | 5 | fixture |
| B8 | truncated_to null — `"truncated_to": null` | 1 | fixture |
| B9 | retry receipt IN fixture — `max_retries_exhausted` | 1 | source-anchored |
| B10-earned | dense-turn token 'earned' — `earned` | 136 | fixture |
| B10-binding | dense-turn token 'binding' — `binding` | 122 | fixture |
| B10-artifact | dense-turn token 'artifact' — `artifact` | 125 | fixture |
| B10-verdict | dense-turn token 'verdict' — `verdict` | 83 | fixture |
| B10-mechanism | dense-turn token 'mechanism' — `mechanism` | 87 | fixture |

## The probes (the bank-protocol's four classes, both cells)

| Probe | Class | Cell | Asks (at the continuation point) | Ground-truth (the expected-facts above) |
|---|---|---|---|---|
| `recall-session-identity` | recall | A | the session's identity and start | A4 + A5 + A8 |
| `recall-loop-sequence` | recall | A | the compacted loop's structure | A2 + A3 + A9 + A11 |
| `artifact-message-shape` | artifact | A | the transcript's message count | A1 + A3 |
| `artifact-tool-calls` | artifact | A | the tool-call path | A2 + A1 |
| `decision-tool-choice` | decision | A | the chosen tool on every call | A2 + A3 |
| `decision-model-pin` | decision | A | the session's engine | A6 + A7 |
| `continuation-close-intent` | continuation | A | the close-message's intent | A10 + A11 |
| `recall-stream-source` | recall | B | the stream's provenance | B6 + B7 |
| `recall-retry-receipt` | recall | B | the retry-capture's receipt | B9 (SOURCE-anchored) |
| `artifact-turn-shape` | artifact | B | the turn's shape | B1 + B2 + B3 + B4 + B5 |
| `artifact-density-receipts` | artifact | B | the many-facts-per-turn receipts | B10-earned + B10-binding + B10-artifact |
| `decision-truncation` | decision | B | the retention state | B8 |
| `continuation-forward-vocab` | continuation | B | the stream's forward vocabulary | B10-verdict + B10-mechanism |

## The verification receipts (the build's own run)

- Cell A fixture `sha256`: a0e7f43d31cb3ebe…
- Cell B fixture `sha256`: 902eb3ca675f5035…
- A1 message count: 8×
- A2 execute_code loop calls: 3×
- A3 tool-output pairs: 3×
- A4 session id token: 1×
- A5 session start stamp: 1×
- A6 model pin: 1×
- A7 truncated_to null: 1×
- A8 source path: 1×
- A9 user open message chars: 1×
- A10 user close message chars: 1×
- A11 open-message head token: 1×
- B1 message count: 2×
- B2 system turn chars: 1×
- B3 user turn chars: 1×
- B4 user turn escaped bytes: 1×
- B5 system turn escaped bytes: 1×
- B6 source path: 1×
- B7 model pin: 5×
- B8 truncated_to null: 1×
- B9 retry receipt IN fixture: 1×
- B10-earned dense-turn token 'earned': 136×
- B10-binding dense-turn token 'binding': 122×
- B10-artifact dense-turn token 'artifact': 125×
- B10-verdict dense-turn token 'verdict': 83×
- B10-mechanism dense-turn token 'mechanism': 87×

**Built deterministically by `build-probe-banks.py` (no model, no invention); every expected-fact's occurrence counted in the fixture's raw bytes before this doc was emitted — any absent fact aborts the build.**
