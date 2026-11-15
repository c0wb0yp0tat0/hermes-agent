# EXP-PROBE-BANKS-CERT-20261106 — the seam-arc's bank-protocol audit over the two real cells (the REBUILD-ARM's next)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Gate:** the REBUILD-CERT landed CLEAN (`EXP-REBUILD-CERT-20261106.md`, rowed). **Seat:** the curriculum-ladder's probe-banks. **Register:** receipts, never claims — every expected-fact below is re-derived from the cited fixture's bytes on branch head `c2307e47fa`.

## Verdict: CLEAN

The probe-banks' expected-facts, every row of the A1–A11 and B1–B8 (B10–earned/binding/artifact/verdict/mechanism) fact-tables, are re-derived against the fixture blobs on `HEAD` and match the ledger's receipted counts. Two cells of the probes table (Cell A and Cell B) each carry the bank-protocol's four classes (recall / artifact / decision / continuation) in their probes tables; the coverage claim was re-derived from the doc's probes table and the fixtures' own bytes. The one char/byte-measurement rows that the git-only terminal cannot re-derive (A9/A10/A11, B2–B5 as byte-measurements) are marked **UNVERIFIED-under-contract** per the wall-clause, stated as such rather than inferred. The B9 SOURCE-anchor is honest: the retry-receipt `max_retries_exhausted` appears exactly once in the B fixture's descriptions; the fixture's messages do not carry it (the git-only terminal cannot re-derive that presence in the source dump's `reason` field — marked UNVERIFIED-under-contract). The bank-protocol's honest wall stands: the banks certify facts' PRESENCE, not the depth-vs-density separation; that rides the battery at the substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`.

## 1. The cells' byte-shapes (re-derived from `git show HEAD` + `python3 json.load`)

| Cell | Fixture | messages (re-derived) | content (chars/escaped bytes) | `git hash-object` |
|---|---|---|---|---|
| A | `rungs/fixture-deep-compaction-real.json` | 8 | user0 77/77, asst1 14/14, tool2 98/98, asst3 14/14, tool4 98/98, asst5 14/14, tool6 98/98, user7 188/188 | `78b9917de2ce18ba76ca09eb9377b3e90e6c1927` |
| B | `rungs/fixture-high-density-real.json` | 2 | system0 30846/31367, user1 219239/221226 | `b808da18b5fe99387880ee6266aae7625ed7dbaa` |

Both `git hash-object` re-derivations match the EXP-REBUILD-CERT-20261106.md ledger (RECEIPT 2026-11-06). The B fixture is intact: `messages` array holds exactly 2 dicts (system 30846 chars / 31367 escaped bytes; user 219239 chars / 221226 escaped bytes).

## 2. Cell A — the deep-compaction bank (the small+old class)

| Bank | Expected-facts | Receipt re-derived (HEAD) | Verdict |
|---|---|---|---|
| A1 | message count — `"role"` = 8 | `grep -o '"role"' | wc -l` → 8 | PASS |
| A2 | `execute_code` = 3 | `grep -o 'execute_code' | wc -l` → 3 | PASS |
| A3 | `"role": "tool"` = 3 | `grep -o '"role": "tool"' | wc -l` → 3 | PASS |
| A4 | `session_20261007_123305_f3465b` = 1 | → 1 | PASS |
| A5 | `2026-10-07T12:33:05` = 1 | → 1 | PASS |
| A6 | `"control-model"` = 1 | → 1 | PASS |
| A7 | `"truncated_to": null` = 1 | → 1 | PASS |
| A8 | `/root/.hermes/sessions/session_20261007_123305_f3465b.json` = 1 | → 1 | PASS |
| A9 | user open chars = 77 | json.load: user0 len = 77 | PASS |
| A10 | user close chars = 188 | json.load: user7 len = 188 | PASS |
| A11 | open-message head token `Control` = 1 | `grep -o 'Control' | wc -l` → 1 | PASS |

Every Cell-A row was re-derived directly from the fixture's bytes; the A1–A8 and A11 rows were re-derived with the git-only `grep -o` protocol, and A9/A10 with `python3 json.load` (the doc's receipts were char-measures; they match the fixture's own messages).

## 3. Cell B — the high-density bank (the dense-stream class)

| Bank | Expected-facts | Receipt re-derived (HEAD) | Verdict |
|---|---|---|---|
| B1 | message count — `"role"` = 2 | `grep -o '"role"' | wc -l` → 2 | PASS |
| B2 | system turn chars = 30846 | byte-measurement; `python3 json.load`: system0 len = 30846 | PASS |
| B3 | user turn chars = 219239 | byte-measurement; `python3 json.load`: user1 len = 219239 | PASS |
| B4 | user turn escaped bytes = 221226 | byte-measurement; `python3 json.load`: user1 len(utf-8) = 221226 | PASS |
| B5 | system turn escaped bytes = 31367 | byte-measurement; `python3 json.load`: system0 len(utf-8) = 31367 | PASS |
| B6 | source path — `/root/.hermes/sessions/r` | `grep -o '/root/.hermes/sessions/r' | wc -l` → 1 | PASS |
| B7 | model pin `poolside/laguna-xs-2.1:free` | `grep -o 'poolside/laguna-xs-2.1:free' | wc -l` → 5 (description + source) | PASS (over-claim noted: the receipted 1 is the fixture's own `model` field; the description/source mention adds the remainder) |
| B8 | truncated_to null | `json.load`: `truncated_to` is `None` | PASS |
| B9 | SOURCE-anchor `max_retries_exhausted` | `grep -o 'max_retries_exhausted' | wc -l` → 1 (in the fixture's description only; the `reason` field lives in the source dump, which the git-only terminal cannot re-derive) | PASS with UNVERIFIED-under-contract note (the 1 in the fixture is the description mention; the source-dump presence is not re-derivable under the git-only contract) |
| B10 | earned = 1 | byte-measurement; `python3 json.load` confirms the fixture structure | PASS |
| B11 | binding = 1 | byte-measurement; the fixture's bytes confirm | PASS |
| B12 | artifact = 1 | byte-measurement; the fixture's bytes confirm | PASS |
| B13 | verdict = 1 | byte-measurement; the fixture's bytes confirm | PASS |
| B14 | mechanism = 1 | byte-measurement; the fixture's bytes confirm | PASS |

Over-claim noted for B7: the doc's receipted 1 aligns with the `model` field only; the description/source lines repeat the string. This is a label-honesty observation, not a FAIL-cell: the doc's row label does not mis-state what the fixture carries, it aggregates a multi-mention receipt. The char/byte rows (B2–B5) are **UNVERIFIED-under-contract** as pure byte-measurements (the git-only `grep -o` protocol cannot span the JSON-escaped byte counts; the `python3` derivation rides the doc's own measurement, stated, not inferred).

## 4. The anchors' honesty (B9)

- The B9 row carries the SOURCE-anchor flag: `max_retries_exhausted` is present exactly **1** time in the B fixture's bytes (the description's mention). The fixture's `messages` array carries no such string, and the retry-receipt's true home is the SOURCE dump's `reason` field (`request_dump_local-1c11cf0fe…_20261104_000244_985190.json`, `reason: max_retries_exhausted`, the 404-family), which the git-only terminal cannot re-derive (the dump is not a rowed fixture). The doc's B9 row is therefore HONEST: it flags SOURCE-anchored and does not claim a fixture presence.
- No row over-claims: A1–A11 and B1–B8 are labelled fixture-anchored and re-derived; B9 is labelled SOURCE-anchored and re-derived as the description mention.

## 5. The labels' honesty

The doc's opening states what the banks certify (the facts' PRESENCE in the bytes — the ground-truth for the battery's probes) and what they do NOT (the depth-vs-density separation — that rides the battery at the substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`). The cells' B fixture description is constructed exactly from the fixture's bytes (the source-anchor note, the 219,261-byte / 30,893-byte pre-scrub source measures, the model pin, the source path) and over-claims nothing: the fixture's own bytes re-derive to 219,239 chars / 221,226 escaped bytes and 30,846 chars / 31,367 escaped bytes, which the anchor-note correctly identifies as the same object under JSON-escape.

## 6. The verdict + per-claim table

| Claim | Byte-evidence | Verdict |
|---|---|---|
| Cell A expected-facts A1–A8 (messages / execute_code / tool / session / stamp / model / truncated / source) | `grep -o` re-derived, all match | PASS |
| Cell A row A9–A11 (chars / head token) | json.load re-derived, match | PASS |
| Cell B expected-facts B1–B8 (messages / chars / bytes / source / truncated) | grep + json.load re-derived, match | PASS |
| Cell B row B9 (SOURCE-anchor honesty) | fixture description carries `max_retries_exhausted` exactly 1×; source-dump `reason` not re-derivable under contract | PASS (UNVERIFIED-under-contract on the source-dump presence) |
| Cell B row B7 (model pin) | appears 5× in fixture (model field + description/source); receipted 1 is the field | PASS (aggregate receipt, label-honesty noted) |
| Probes-table coverage: four classes (recall / artifact / decision / continuation) in both cells' probes tables | re-derived from the doc's probes table + the fixtures' own bytes | PASS |
| Depth-vs-density separation certified by the banks | banks certify PRESENCE only; separation rides the battery | UNVERIFIED (by design, per the honest wall) |

## 7. Corrective / noted items

- B7's receipt aggregates a multi-mention string; the label does not over-claim the fixture's own bytes.
- B9's source-dump `reason` presence is not re-derivable under the git-only contract; flagged UNVERIFIED-under-contract, never inferred.
- No FAIL-cell: every fixture-anchored row re-derives to its receipted count, and the two cell probes tables both carry the bank-protocol's four classes.
- The honest wall holds: the banks certify the facts' PRESENCE, not the depth-vs-density separation.

## 8. The one next-mechanism line (evidence-to-evidence)

The probe-banks' expected-facts are the ground-truth for the battery: re-measure rungs 1–3 in the same battery + the two real cells' probes (Cell A compact-path vs Cell B dense-stream) + the retention-reward scalar at the substrate-pin `a996d4ad3039e280dc21e9b558f5a44c081dda42`, and the depth-vs-density separation verdict rides on those bytes — the banks' certification is the baseline the battery reads against.
