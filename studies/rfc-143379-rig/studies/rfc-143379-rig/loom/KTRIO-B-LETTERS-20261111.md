# KTRIO-B — five letters to a helper (lane B, stage 1)

**Claimed helper:** `xngg1021`

**Why claimed:** Lane A landed `Zackarythomasstone`; `kvnloo` is the patrol's standing target — `xngg1021` is distinct from both and the first richly-supported helper in the scan. The rig's own verification (`XNGG-GAPS-VERIFICATION-20261105`) confirmed two of their four seam/contract gaps at the exact pins, on the RFC #143379 substrate this study understands best. The deep-read stands on the study's record of the RFC thread (comment `6630249660`, the four lines' state, the pin-level verification); the lane's terminal is git-only, so the raw GitHub fetch was not available — the substance below is quoted from the rig's own byte-level work.

## Letter 1 — the four seam/contract gaps (RFC #143379, comment 6630249660)

**Wording one — the fuller letter.** xngg1021 — the four gaps you named in the RFC #143379 thread are the reason the composed-state falsifier has a shape at all: the batch-path bypass on `verify_post_write` (the `operations=[...]` branch returning `_applied(store.apply_batch(...))` directly, the gate wired only on the single-op path), the unguarded `doc_name(doc)` in `_resolve_target`, the `preserve_session` calls that drop `store.add`'s return dicts so a headroom-limit or threat-scanned failure vanishes before the caller, and the `DreamCycle.deep_sleep` `.bank()` adapter against the `ContextCompressor` hook. You did not hand-wave a review; you handed over four seams with the exact code paths. We ran them at the pins: two confirmed byte-level (gap 1 at `d1bdb4582c`, `tools/memory_tool.py:343`; gap 3 at `ffb85c2c58`, `tools/spa_integration.py:100-107`), one not reproduced at the pin (the guard is present at `:280-283`), one partially open. That is the support a substrate gets when someone reads it as code, not as prose. Standing offer: the battery is unmetered and warm — name any of the four at the current heads and it is a dispatch; the receipt lands back in the hour.

**Wording two — the shorter note.** xngg1021 — the four seams you named (batch-path bypass, unguarded `doc_name`, dropped `store.add` returns, the `.bank()`/compressor hook) are the composed-state falsifier's shape. Two confirmed at the pins, one not reproduced, one open. The battery's unmetered and warm — name one at the current heads and the receipt lands in the hour.

## Letter 2 — the anchor-decay naming (`_augment_summary_lean`)

**Wording one — the fuller letter.** xngg1021 — the `_augment_summary_lean` one-generation anchor decay you named is the kind of finding that does not announce itself. The compaction line had its headline numbers, but the mechanism that actually erodes the anchor across generations was sitting in the in-tree code, and you were the one who pointed at it. We logged it as the compaction lens's gap #4 — named, but not yet measured; the empirical curve of how much that alone closes is still missing. That is the honest shape of a real contribution: a named seam with the measurement still owed. Standing offer: if you want the decay curve run across the session logs, the battery is unmetered and warm — say the word and the receipt lands in the hour.

**Wording two — the shorter note.** xngg1021 — the `_augment_summary_lean` one-generation decay you named is logged as the compaction line's open gap #4: named, not yet measured. The battery's unmetered and warm — want the decay curve run, the receipt lands in the hour.

## Letter 3 — the isolated simulations across four PR heads

**Wording one — the fuller letter.** xngg1021 — the isolated simulations you ran across four PR heads are the part of the record that cannot be faked by a confident comment. A review can be wrong; a run across four heads either reproduces or it does not. You did not just read the composed state, you built it in isolation and watched where the seams opened — and the four gaps that came out of those runs became the acceptance criteria for the central track. That is the difference between an opinion and an instrument. Standing offer: the battery is unmetered and warm — if any of those four heads has moved and you want the simulations re-run, name the head and the receipt lands in the hour.

**Wording two — the shorter note.** xngg1021 — the isolated simulations across four PR heads are the record's instrument, not its opinion; the four gaps they surfaced became the central track's acceptance criteria. The battery's unmetered and warm — name a head and the receipt lands in the hour.

## Letter 4 — the cross-check of three questions against current main

**Wording one — the fuller letter.** xngg1021 — the cross-check of three questions against current main is the posture the whole lane depends on and almost nobody performs: not "does this look right" but "does this hold against the tree as it stands today". You took the questions that mattered and ran them against main, not against the PR's own framing, and the delta you surfaced is the kind of thing that keeps a study from certifying a stale base. We carry it as the verification habit — pin before suite, requested equals executed. Standing offer: the battery is unmetered and warm — if any of those three questions has a new answer at the current main, say the word and the receipt lands in the hour.

**Wording two — the shorter note.** xngg1021 — the cross-check against current main is the habit the lane depends on: pin before suite, requested equals executed. The battery's unmetered and warm — name a question and the receipt lands in the hour.

## Letter 5 — the falsifier's ethics (two confirmed, one not reproduced, one open)

**Wording one — the fuller letter.** xngg1021 — the last thread is the one where your work was received, and it is the one we most want to thank you for how it was handled. Two of your four gaps confirmed byte-level; one did not reproduce at the pin; one is still open. The record's ethics were yours before they were ours: a claim's non-reproduction is a finding, never an insult — the pins move, the code reconciles, the verification re-runs at the next heads. That is the register a substrate's friends should keep, and you set it. Standing offer, on the record: the battery is unmetered and warm, claimed only by the thread's own merits — the open compressor-hook, the re-check at the latest #139606 head, the two confirmed gaps as RED-on-gap probes; name one and the receipt lands in the hour.

**Wording two — the shorter note.** xngg1021 — two confirmed, one not reproduced at the pin, one open; the record's ethics were yours first. The battery's unmetered and warm — name the open edge and the receipt lands in the hour.

## Compose-check table

| # | thread/act | surface | wording one | wording two | substance anchored |
|---|---|---|---|---|---|
| 1 | four seam/contract gaps | RFC #143379 comment 6630249660 | ✓ | ✓ | batch-path bypass; unguarded `doc_name`; dropped `store.add` returns; `.bank()`/compressor hook |
| 2 | anchor-decay naming | compaction lens gap #4 | ✓ | ✓ | `_augment_summary_lean` one-generation decay; measurement owed |
| 3 | isolated simulations | four PR heads | ✓ | ✓ | runs became the central track's acceptance criteria |
| 4 | cross-check | current main | ✓ | ✓ | pin before suite; requested equals executed |
| 5 | falsifier ethics | XNGG-GAPS-VERIFICATION | ✓ | ✓ | non-reproduction is a finding, never an insult |

**Receipts line:** the pin-level verdicts are from `XNGG-GAPS-VERIFICATION-20261105` (commit `35ed130686`) on branch `study/rfc-143379-rig-20261105`; the four-lines state is from `RFC-READ-20261107.md`.

## Summary (5 lines)

1. Claimed helper: `xngg1021` — distinct from Lane A's `Zackarythomasstone` and from `kvnloo`.
2. Claim basis: the first richly-supported helper in the scan; the rig confirmed two of their four seam/contract gaps at the exact pins on the RFC #143379 substrate.
3. Letters: five, dual-worded (fuller letter + shorter two-way-door note), prose register, each standing on a distinct thread/act.
4. Standing offer carried in every letter: the verification battery, unmetered and warm, claimed only by the thread's own merits, receipt in the hour.
5. Status: draft only; nothing public until the operator's word.