# FLEET-BRIEF LONGCAT — ADJUDICATE ALL OF THEM (the full-reply arc's three surfaces)

*Seat (pin): `meituan/longcat-2.5:free` — the adjudicator. The operator's word (2026-11-24): "Long cat adjudicates all of them then beam does it thing, then we preview." Adjudicate THREE surfaces against the ground: the sanity verdict, the launch receipt, and the full reply itself. Branch: `study/rfc-143379-rig-20261105`. Fire: now, after the sanity + launch receipt land.*

## The mission

The pair previews only what survives a cold adjudication. The three surfaces, checked against their grounds:

**SURFACE 1 — `RW-FULL-REPLY-SANITY-20261124.md` (the solar verdict, CLEAN):** the sanity's receipts carry phrases that do NOT sound like the reference's actual text (its step-quotes mention `close()`, `fsync()`, `flush-path mirror`, `0001` — the stall-on-read reference has seed-initial/reader-snapshot/Event-block/writer-commit, no fsync machinery). **Adjudicate: are the sanity's quoted steps really in `KVNLOO-STALL-ON-READ-REFERENCE-20261124.md`? Are its numeric receipts real (443/64-64 came from kvnloo's matrix row, not `rw-probe-out.json`)? A phantom receipt in the sanity verdict = the verdict is CLEAN-with-phantoms, not CLEAN.**

**SURFACE 2 — `RW-FULL-REPLY-LAUNCHED-20261124.md` (the hy launch receipt):** does it carry a real comment id + a byte-identical verification of the live comment vs the committed reply? Or placeholders / escaped-fetch claims? (The interim-note arc shipped a fake-id receipt and an invented PATCHED-CLEAN — the class is known.)

**SURFACE 3 — `RW-FULL-REPLY-20261124.md` (the reply):** the six checks the sanity claimed — repeated cold, with the real bytes:
1. Kvnloo's quotes (row 7143199711) present in the reference verbatim (the real four steps: seed initial; reader snapshot + Event block; writer commits latest; assert...). Name any step that is not the reference's.
2. The two-machine claim (green/green/green/red, live-list `["initial"]`) — matches `RW-FINDING-STALL-ON-READ-20261124.md` + `rw-probe-out.json` byte-level.
3. Numbers: 443/64-64, 89/89, 297/297, 17/17, 16/1, B1 0.333, C 0.5, B≥0.85C False, abstention 0.667 — each traces to its record file or the operator's stated numbers; a number without a receipt = ISSUES.
4. The channel paragraph — matches the operator's 40-probe numbers (raw 0/40 · 26 · 31 · 29 · the channel's-rate line); no invented figures.
5. Register: no body pair-metadata; one em-dash per sentence; @kvnloo open; the credit line.
6. Footer: Nemo-named, last line.

## The adjudication record

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-ADJUDICATION-20261124.md`

1. The three surfaces' verdicts, each with its receipts — the sanity's phantom-check first (this run's headline), the launch receipt's integrity, the reply's six checks cold.
2. The corrections block: any fix each surface needs, byte-cited (the phantom quotes trimmed, the receipts re-sourced, the reply lines corrected).
3. The pair's one-liner: what survives to the beam's register pass.

## Write-window

`write-window: 11` — reads first, the verdict's skeleton by round 10, deepened after. NO stub markers; a phantom named is a finding, never a pass.

## Hard lines

- PREVIEW ONLY — nothing posts; the RFC surface untouched; PR #1 the only other allowed surface (and only the machinery's cadence).
- No installs. All reads LOCAL (the committed grounds + `rw-probe-out.json`). `git add` + commit locally — NEVER push/pull. Never checkout/stash/rm. `ls-remote` first.
- THE WITNESS RULE: a quote not in its source's bytes = the phantom class, named and struck; a receipt without its trace = ISSUES.

## Emission

Exit 0 = the adjudication EXISTS on disk, re-read, committed; the report names the sha. No tool-call syntax in final words.
