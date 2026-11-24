# FB2 RFC REPLY BEAM REPORT — 2026-11-24

**Verdict: CLEAN-WITH-NOTES**

The reply at `plan/tank/FB2-RFC-REPLY-20261124.md` (51 lines, read in full) delivers the promised test as a thread comment for the lab: six scannable beats, every bar pre-registered, the hold-back sealed, and the confirmation handed back. All six checks land; two cadence/register notes survive, both byte-cited below. Receipt method: the terminal is git-only for lanes, so the six greps were run as line-cited scans against the committed reply bytes.

## The six checks

### Check 1 — The lab reads it, not the pair — PASS

Case-insensitive scan of the 51-line body for the nine banned tokens:

| token | hits |
|---|---|
| `the pair` | 0 |
| `our loops` | 0 |
| `kaizen` | 0 |
| `flip-flop` | 0 |
| `the fleet` | 0 |
| `study landing` | 0 |
| `NOT posted` | 0 |
| `staging` | 0 |
| `more to come` | 0 |

Zero on all nine = pass. The opening (L1) addresses `@kvnloo` and lab; the close (L51) asks the run back ("Your run confirms base-red at `268bb091`, combined-green at `a9c65dc4`…").

### Check 2 — The five elements scannable — PASS

Bold-header scan (`**the `):

| beat | line |
|---|---|
| `**the pre-registration**` | 5 |
| `**the pins**` | 14 |
| `**the signatures**` | 24 |
| `**the acceptance rows**` | 34 |
| `**the wake read**` | 45 |
| `**the ask back**` | 49 |

Six beats present = pass.

### Check 3 — The hold-back, clause only — PASS

Withheld class per spec §5: **the BATCH-PATH double-add**. Content-hint token scan: `batch` 0, `bulk` 0, `double-add` 0, `BATCH-PATH` 0, `batched` 0. The clause-only mention is present verbatim at L12: "One hold-back class, withheld by clause — its signature is deliberately not written where a runner can read it… It stays withheld." No expected signature, no class name, no hint.

### Check 4 — The bars are the spec's own — PASS

Three spot-checks against `FB2-FAILING-CASE-SPEC-20261124.md`:

| bar | reply | spec | verdict |
|---|---|---|---|
| removal control | L11, L30 | §4 | match — green all three pins; RED invalidates the probe, never the finding |
| C1 | L38 | §7 | match — 100% byte-verbatim, RED MAIN / GREEN branch, removal control RED, one lost fails |
| C2 | L39 | §7 | match — plain refusal, no eviction, no silent eviction-by-summary, drop/overwrite fails |

C3 (L40) and C4 (L41) also match §7 word-for-word (C4 tightens "his" to "the", strength intact). Softening-token scan: `probably` 0, `likely` 0, `suggest` 0.

### Check 5 — The ear's kindness — PASS WITH ONE CADENCE NOTE

- **40-hex census:** four full hexes, each exactly once — `0f602c5f6f18615632535251d62a2db74ce93b69` (L20), `268bb09147eaf948ece6a1beecd92a2268a5fc95` (L21), `a9c65dc43db9000e8b6e238b50916aa6fa32ff08` (L22), `8ba4b344766e50c2e3eeaba84f4349276a1be021` (L47). Later mentions use the 8-hex names (`268bb091` L26/32/51; `0f602c5f` L26; `a9c65dc4` L28/32/51).
- **Em-dash census:** 17 total; one-per-sentence holds everywhere except L32 (two em-dashes in one sentence). See note 1.
- **Declaratives / chains:** short declaratives throughout; hyphen compounds only (`marker-bearing`, `whole-file`, `byte-verbatim`, `read-less`, `chain-doc`, `eviction-by-summary`, `byte-compared`, `no-cache-write`), no em-dash chains, probe flags ride inline.

### Check 6 — The one-document shape — NOTE

- One reply body, linear beat order, no branching structure, no re-telling: pass.
- **Path references to the study's files: 0.** Zero occurrences of `.md`, `studies/`, or `plan/tank` in the body. Closest anchors are thread-side (`row 7122688366` L41/L43, `decision ledger #113309` L40). See note 3.

## Notes block

1. **Byte-cited cadence tweak (L32).** "`268bb091` gave RED — SECOND's 64 bytes only, `False`; `a9c65dc4` gave GREEN — 131 bytes, both present, `True`; the control was green on both." is one sentence carrying two em-dashes. Split at the first semicolon ("…`False`. `a9c65dc4` gave GREEN — …") or drop one dash.
2. **Byte-cited register tweak (L32).** "already executed on our side" carries pair-voice; "already executed" keeps the register lab-facing. Not a banned token, non-blocking.
3. **Byte-cited shape gap (check 6).** The study's files are not referenced by path. If the head wants the lab to reach the room beneath, one line pointing at `studies/rfc-143379-rig/plan/tank/FB2-FAILING-CASE-SPEC-20261124.md` and `FB2-EXECUTION-RECEIPTS-20261124.md` closes it; the composer's self-contained mandate argues the other way, so this is surfaced, not imposed.
4. **Byte-cited mention form (L1).** `@kvnloo` rides inside backticks, which suppresses the platform mention if posted as-is; drop the backticks at post time if a true ping is wanted, keep them if quiet staging is intended.

## Cross-check

The sanity lens landed (`FB2-RFC-REPLY-SANITY-20261124.md`): CLEAN-WITH-NOTES, its one FAIL (C4 truncation) retired by head-side adjudication as a phantom read of a mid-write draft — the committed C4 quote is byte-identical to spec §7, confirmed independently here at L43.

## The pair's line

Yes — this reads as the follow-up for their lab: it opens for @kvnloo, fixes every bar before the run, delivers the six beats scannable, seals the hold-back, and hands the confirmation back; the surviving notes are cadence polish, not register damage.