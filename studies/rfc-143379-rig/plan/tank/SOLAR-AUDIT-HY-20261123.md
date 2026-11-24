# SOLAR-AUDIT-HY-20261123 — STAGE-2 AUDIT: HY'S STAGE-ONE REGROUP

**Branch:** `study/rfc-143379-rig-20261105` · **Head:** `5f23c1dfc1` (audit commit; the WIP landed at `1d1110d070`)
**Scope:** audit of `HY-SANITY-ENRICH-20261123.md` + `HY-REGROUP-WIP-20261123.md` against the receipts and the register. `REGROUP-COMPLETE-20261123.md` is the comparison object and is **not** edited.
**Arsenal:** agent-work-review (verdict form) + investigation-documentation (receipts form); think-tank spine for the enrichment classes. Refused: think-tank-feedback/blind-panel (single-lens scope), systematic-debugging (no non-reproduction), external-readiness (nothing public).

---

## A. THE 12 CHECK ROWS — RE-DERIVED

| # | Check (as asserted) | Status | Re-derivation (receipt → basis) | Caveat |
|---|---|---|---|---|
| 1 | Kevin's probe table verbatim (MAIN 409/read unknown; #116673 16/16 race red; +b6ff7dae 17/17; ec649ad9 443 + 64/64; round2-gate 297/297 race red) | **HOLDS** | kvnloo-comment §4-9 ≤ A5-1/A5-3/B2b-1: ec649ad9 443 pass + 64/64, race gone only with hardened read; fix-in-ours confirmed (remove either → green, both → red); round2-gate 297 green + race red | none |
| 2 | Kevin's three findings (fix already in ours; two-add overwrite/FB-2; 88/88 dispatch gap; recipe) | **HOLDS** | kvnloo-comment §13-15 ≤ A6-1/A6-2/A6-3 (FB-2 repro FIRST_SURVIVED_SECOND_ADD=False), A7-1 (88/88 claim carried), A8-1 (recipe 7/7 clean at base) | **88/88 suite result NOT re-executed locally** — VET A7-2 tags claim #12 UNVERIFIED. Re-run at the restore pin before stage three consumes the "88/88 = our held receipt" line. |
| 3 | "His three answers settled design" (no pinned/episodic classifier, no K window; read counts only for skills; harness 5/5 green, both controls red) | **HOLDS** | kvnloo-comment §23-25 ≤ B2b-1/B2b-2/B2b-3; EVIDENCE-PACK-A A8/A10 | none |
| 4 | Recipe: honored as reference, clean at base, executed as re-derivation at pins | **HOLDS** | RECIPE-RETRY-20261122 (bb75740491e3) ≤ A8-1 (7/7 clean at base 0f602c5f, exit 0); cross-lineage abort identified as the prior's cause | none |
| 5 | Field data exactness (95/60/40/20-50; flipped standing instruction; nothing leaked; durable record with pointer) | **HOLDS** | kvnloo-fields §3-16 ≤ B5-1..B5-4, B1-3..B1-6 | Figures restated without the caveats (half data local handoff engine; one summary model; one operator's sessions) — added as a scope line, not a downgrade |
| 6 | /pin slice (commands; off-unless-used; user-only scope; ## Pinned by the user block; mechanical carry; cap-with-refusal; single-ledger #113309; 4x 100% survival + removal control) | **HOLDS** | kvnloo-fields §18-26 ≤ B5-5/B6-5 ≤ PIN-AMPLIFIER ≤ THINKTANK-1 T-6/T-23 | none |
| 7 | Salvage (#137650 on MAIN for #158289; memory-side follow-ups) | **HOLDS** | kvnloo-comment §33 ≤ B0-9 (ROUGH-DRAFT §"A second pair of eyes"); IMPROVE-ROUND-1 S2 | Salvage carried as a QUESTION with a "we can do" premise DOUBTED (unverified). No overclaim. |
| 8 | Consent-deny pre-registration (ungated add 116788; round-2 consent-deny candidate fix) | **HOLDS** | kvnloo-comment §34 ≤ S3 (IMPROVE-ROUND-3 HOLDS); IMPROVE-ROUND-1 S3 | none |
| 9 | Families 136535/136541/154023/154177 = one class (what-the-summary-may-not-author) | **HOLDS** | kvnloo-fields §24 ≤ B5-6; IMPROVE-ROUND-1 S6 | The "0 of 16" figure is carried, not locally held — flag as CARRIED (suggestions file only). |
| 10 | Sibling: async-delegation completion picked as User asked; add-on not new PR | **HOLDS** | kvnloo-fields §24 ≤ S4/IMPROVE-ROUND-1 (UNKNOWN: no local record; held receipt = 88/88 dispatch gap) | D4 applied in §Three: "I will not call it receipted on our side yet; acceptance conditional on local reproduction; the receipt we actually hold is our own dispatch-gap case; phrase drops if no local row lands." |
| 11 | Probes door (what's next in our fork; run probes there) | **HOLDS** | kvnloo-comment §36 ≤ S5/IMPROVE-ROUND-2 (HOLD); A6-3 (FB-2 armed) | none |
| 12 | Close-out (no reply needed before close-out; we will write at close-out with receipts; prepared with an AI agent and reviewed before posting) | **HOLDS** | kvnloo-fields §1 + §26 ≤ REGROUP-COMPLETE §45 | none |

## B. LOAD-BEARING CLAIMS 13-28 — RE-DERIVED (abbreviated)

| # | Claim (as asserted) | Status | Re-derivation |
|---|---|---|---|
| 13 | "All three lanes confirmed D1" is itself re-derived false | **HOLDS** (falsification-classed, NOT converged) | AOA-NINE-AXIS:64,125 ("D1 confirmed by all three lanes") vs ARMAMENT-REPASS C3 (BA = byte equality, AA = SHA equality, CA 0 hits) and FAN2-BA A4 (grep '\bG1\b|\bI2\b' = 0). WIP §Two keeps the seam open. Confirmed: this is the instance of the unanimity blind spot — the WIP keeps the D1-falsification language as a falsification-classed claim. |
| 14 | Fan closed 3-for-3 on amended gates | **HOLDS** | THINKTANK-1 T-27 (CA 31/2/1, BA 16/3/2, AoA ADJUSTED); FAN2-BA/AA/CA verdicts |
| 15 | Improvement loop closed 3-for-3 (eight regroup questions vetted) | **HOLDS** | IMPROVE-ROUND-1/2/3 + THINKTANK-1 T-16 (N3-N8: +4/+6/+3/+1/+1/+0; cumulative +94; E-gates HOLD) |
| 16 | Registry READY, runners walked 2/0, both registries byte-identical | **HOLDS** | MISSION-BRIEF-MASTER §7-bw fold (audit cites the fold; the WIP does not restate it — citation-discipline note, not a defect) |
| 17 | Read-suite 4/4 at the restore pin, reproducing failures on main | **HOLDS** | EVIDENCE-PACK-A A1-3 ≤ A1-2/A1-3 |
| 18 | Composed tree ec649ad9: 443 pass + dispatch 64/64, race green | **HOLDS** | EVIDENCE-PACK-A A5-1 |
| 19 | Race disappears only with hardened read | **HOLDS** | A5-1/A5-3 (remove lock alone → green; no-cache-write alone → green; both → red) |
| 20 | Write arm's repair inherits combined tree's doc semantics | **HOLDS** | EVIDENCE-PACK-A A9-2 |
| 21 | FB-2 armed with a removal control | **HOLDS** | A6-3 + IMPROVE-ROUND-2 S2 |
| 22 | Gate battery 300+: 3 PASS / 4 BLOCKED on quota, not certified | **HOLDS** | EVIDENCE-PACK-B B2a-3 (7 rungs) + B2a-4 (certification NOT-YET-CERTIFIED) |
| 23 | Improver loop curve to the knee, stopping on its own evidence when the design space was exhausted | **HOLDS** | MAIN-LOOP-N8 (d21e8863ba, +0 total-zero) + THINKTANK-1 T-16 (8/8 E-gates HOLD at named owner-beats). The exhaustion claim is a MEASURED loop-termination claim (delta collapse +10/+12/+15/+15/+7/+3/+4/+1 = +66, 0 consecutive zero-delta), NOT a page-shape convergence claim. No flag. |
| 24 | "We are not bringing a request to your instrument; a second instrument of our own" | **HOLDS** | §One roll-up citations (MISSION §7-bw/§7-ck, EVIDENCE-PACK-A, EVIDENCE-PACK-B, THINKTANK-1) |
| 25 | Two checked bars re-derived at the pins | **HOLDS** | EVIDENCE-PACK-B B1-1..B1-6 + RFC-ANCHOR line 12 |
| 26 | Two open bars named by receipt | **HOLDS** | A6-3 (FB-2) + B2a-3 (3 PASS/4 BLOCKED) |
| 27 | Three blind lanes closed on the record | **HOLDS** | THINKTANK-1 T-27; IMPROVE-ROUND-1/2/3 |
| 28 | "Kit with receipts, standing beside yours, not under it" | **HOLDS** | §One roll-up as above |

## C. ARITHMETIC 29-31 — RE-DERIVED

| # | Claim | Status | Re-derivation |
|---|---|---|---|
| 29 | 647,716,330 − 641,262,336 = 6,453,994 | **RE-DERIVED** | BA D1; ARMAMENT-REPASS §1.1 (`python3 -c 'print(647716330-641262336)'` → 6453994). ✓ |
| 30 | round2-gate 297 reads green, race red | **RE-DERIVED** | kvnloo-comment §9. ✓ |
| 31 | ec649ad9 443 pass + dispatch 64/64 | **RE-DERIVED** | A5-1/B2a-1. ✓ |

## D. DELTA MANIFEST D1–D6 — VALUE / RISK / CORRECTNESS

| Delta | What it adds | Value | Risk | Correctness |
|---|---|---|---|---|
| D1 | Field data exactness (13-of-16 opening-ask loss; 92%→97% first-hop-only "Open asks"; no-effect larger summarizer; +20–33 search-back; three caveats) | HIGH — load-bearing evidence for the long-session gate's class | LOW — scope caveat included | RE-DERIVED from kvnloo-fields §3-16 + B5-1..B5-4; externally corroborated by the compaction-decay literature (steering class 2) |
| D2 | /pin mechanics (command set; off-unless-used; user-only protected scope; "## Pinned by the user" block; mechanical carry; cap-with-refusal; single ledger entry; 4x 100% survival + removal control) | HIGH — the first receipted piece of governed compaction | LOW — design stance, not a shipped piece | RE-DERIVED from kvnloo-fields §18-26 + PIN-AMPLIFIER + B5-5/B6-5 |
| D3 | Broken-ruler caveat (−3.5 and +1.1 disqualified until probe fixed; gate stands; protocol's first step is the fix) | HIGH — prevents certifying the wrong number | LOW — hard-line stance | RE-DERIVED from B1-5 + B1-4 (−9.2..+10.2 spread) |
| D4 | Sibling receipt precision (report-received + conditional on local reproduction; 88/88 dispatch gap as held receipt; phrase-drop if no local row) | MEDIUM — trims an overclaim, not a loss | LOW | RE-DERIVED from IMPROVE-ROUND-1 S4 (no local record of the async-delegation seam) + FAN2-CA D-2 (phantom PIN claim). Phrase-drop clause = falsification guard. |
| D5 | Redaction framing (paper-pass vs general-pass demoted to secondary) | LOW–MEDIUM — reduces framing risk | LOW | RE-DERIVED from IMPROVE-ROUND-1 S5/B0-9. Accept (framing demotion). |
| D6 | Kit roll-up receipts + D1-seam naming (keep all-three divergence open) | MEDIUM — names the AoA's all-three claim vs ARMAMENT-REPASS C3 | LOW — naming a seam is not endorsing the claim | RE-DERIVED: D6 does NOT smooth the seam; §One names the divergence (AOA-NINE-AXIS:64,125 vs ARMAMENT-REPASS C3/FAN2-BA A4). |

No delta fails its re-derive. The overclaim was D4's pre-correction "receipted" (see E); nothing else to rename.

## E. THE ADJUST VERDICT CHECKED

- **Overclaim real?** YES. REGROUP-COMPLETE §Three asserted "receipted" for the async-delegation sibling. No local record holds that seam (IMPROVE-ROUND-1 S4 UNKNOWN; FAN2-CA D-2 phantom-PIN class; kvnloo-fields §24: offered as an add-on commit, not a new PR). D4's correction is correct: report-received + conditional-on-local-reproduction; 88/88 dispatch gap is the held receipt; phrase drops if no local row lands.
- **Three value-add omissions real?** YES. (1) field data exact figures + caveats (REGROUP-COMPLETE §Two carries only "95, 60, 40, 20 to 50… restated as its opposite, with nothing leaked" — no numbers, no caveats); (2) /pin mechanics (only "an amplifier, a control surface" — no commands, scope, block, carry, cap); (3) broken-ruler caveat (REGROUP-COMPLETE §Two names harness 3ec4157e as "the cleanest second-lab signal" with no disqualification).
- **Anything hy missed still missing?** The fan-2 lanes' refresh of the AoA (BA-5/CA-6 stale citations, AM-C1/AM-C2/B1 content-gate rows) is fan-2's leg, not hy's stage-one scope — not a defect in hy's work. The WIP's own scope (response + delta manifest + kit roll-up) is complete against the register. **One recommendation:** re-run the 88/88 suite locally (VET A7-2 tags it UNVERIFIED) at the restore pin before stage three consumes the "88/88 = our held receipt" line.

## F. WIP REGISTER COMPLIANCE (PUBLIC FORM)

- §Three: 0 headers, 0 bullets, 0 **bold**, 0 em dashes, 0 arrows (verified programmatically).
- Gratitude frame: open "I am grateful you stayed with it" + close "Thank you again, @kvnloo — for the instruments and the patience. We will write at the close-out, with receipts." Both present.
- One ask in one breath (§Three): "Here is the one thing I would ask of you before your MAIN probe runs, @kvnloo: take our failing-case spec as your pre-registration, FB-2 as the named failing case, the removal control, and one hold-back class…" — one ask, delivered in one breath.
- **Register: COMPLIANT.**

## G. STEERING ENRICHMENTS (ADD-ONLY, ALL EXTERNAL, ALL RECEIPTS)

**(1) Exhaustion check.** The method of exhaustion is the ε-δ limit's precursor: an explicit error bound (the ε) and a halving operation (Seldin 1990; UBC notes). Verify the WIP names its error bounds (the UNKNOWNs and settle-conditions as the ε) for every load-bearing claim.
- The WIP's UNKNOWN register is named plainly (§Seven: settlement OUTCOME UNKNOWN; act-4 fire void-class; qwen free-tier ended; B2 NOT advanced; content-bearing window window-conditional). These are the ε for the kit's readiness claims. The load-bearing numbers are all tied to named receipts (EVIDENCE-PACK-A/B, kvnloo-comments, THINKTANK-1).
- Every quantified claim in §One/§Two/§Three is receipted at the number level (e.g., "443 test green with 64-of-64 dispatch" ← A5-1; "3 PASS / 4 BLOCKED" ← B2a-3; "95/60/40/20-50" ← kvnloo-fields). No claim reads as converged from the shape of the page: the one exhaustion claim ("design space exhausted") is a measured loop-termination claim, receipted by the delta collapse and E-gate closure (THINKTANK-1 T-16), not by page shape.
- **Result: no page-shape convergence flagged.** The WIP names its ε (UNKNOWN register) for every load-bearing claim.

**(2) Field's decay shape.** Kevin's 95/60/40/20-50 curve is independently externally corroborated by the compaction literature: the Compaction Cliff (arXiv 2608.22752) measures 53% to 10% across five rounds on production configs; the Compaction Half-Life study fits per-round survival 0.484 to 0.573 and finds a 2.7x budget yields no claimable round-5 difference while a verbatim-preservation instruction yields s=1.000 — the same geometric decay and the same mechanism as the /pin-as-amplifier.
- **Rarity class:** the literature's measured failure mode is availability-loss with abstention, ZERO corruption. Kevin's flipped standing instruction is the rare corruption case beyond their envelope. The WIP's emphasis on the flipped instruction is therefore **right and rare, not overstated** — and this is exactly where the hy enrichment adds value (the WIP's scope line notes the local-handoff-borrow half, keeping the field data inside its envelope).
- **Result: the D1 addition is externally corroborated and not overstated.**

**(3) Unanimity blind spot.** Agreement-only signals cannot certify correctness — a theorem (Agreement Is Not Truth, EMNLP 2026) proves no procedure reading only the answer distribution separates a majority-right from a majority-wrong instance; 60% of wrong answers sit in the high-consistency region (When Judges Agree and Are Wrong, arXiv 2610.21128); and 13.4% of unanimous medical votes are wrong where process signals (not final agreement) discriminate (ProbeGuard, arXiv 2610.07570).
- Apply to this audit: do not trust hy's ADJUST verdict on its agreement with itself — re-derive the receipts (done, Section A). The ADJUST verdict rests on receipt re-derivation (each of the 12 check rows re-derived against the cited receipts), not on agreement with itself — the correct disposition.
- The WIP keeps the D1-falsification language as a **falsification-classed claim**: §Two states the all-three claim is "re-derived false" with the seam OPEN (AOA-NINE-AXIS:64,125 vs ARMAMENT-REPASS C3/FAN2-BA A4, no CA hit). This is precisely the theorem's instance, and the WIP's handling is the compliant one: the claim is falsified, the seam is named, nothing converged.
- **Result: the D1-falsification language is kept as a falsification-classed claim; the ADJUST verdict is receipt-based, not agreement-based.**

## H. VERDICT ROWS (ASSERTED → STATUS → BASIS)

| Asserted | Status | Basis |
|---|---|---|
| All 12 check rows | **HOLDS** | Receipt re-derivation in Section A; 12/12 hold |
| Load-bearing claims 13-28 | **HOLDS** | Section B (with the 88/88 re-run recommendation) |
| Arithmetic 29-31 | **RE-DERIVED** | Section C |
| D1–D6 | **ACCEPTED IN WIP** | Section D — all re-derive; no delta fails |
| ADJUST verdict (overclaim / omissions / missed) | **CORRECT** | Section E |
| WIP public form | **COMPLIANT** | Section F |
| External enrichments G1–G3 | **PASS** | Section G |
| **OVERALL VERDICT** | **SOUND** | All asserted rows re-derive; register compliant; all named deltas accepted |

## I. DELTAS — STAGE THREE CALLS

| Delta | Stage-three call |
|---|---|
| D1 | **ACCEPT** — externally corroborated; keep the caveats line; keep the all-three seam open (falsification-classed) |
| D2 | **ACCEPT** — design stance, not a shipped piece; name the owner in stage three |
| D3 | **ACCEPT** — gate stands; no certifying run on the old probe |
| D4 | **ACCEPT** — apply the phrase-drop clause fully at the receiver; re-run 88/88 locally first (VET A7-2 UNVERIFIED) |
| D5 | **ACCEPT** — paper-pass demoted to secondary; keep the primary variable (class coverage) |
| D6 | **ACCEPT** — keep the divergence open; never smooth the all-three claim |

## J. ARMAMENT ROW

**USED:** agent-work-review (the verdict form), investigation-documentation (the receipts form), think-tank (the enrichment spine). **REFUSED (named, with why):** think-tank-feedback/supervisor-delegation/blind-agent-panels (single-lens, single-opinion scope), systematic-debugging (no non-reproduction in this audit), external-readiness (nothing public), codex/claude-code/opencode (no delegate coder), web-storm/web-search/tools (the web storm is complete; its outputs are add-only inputs), memory-chain (no chain append), hermes-agent/hermes-gateway-ops (no config change), safe-file-editing (no secret-bearing file), creative/design/media (no artifact generation).

*Emission contract:* file on disk first, then commit, then sha. Nothing public · RFC #143379/#5320/#157065 QUIET · no installs · study paths only · never push · index-locked 10s retry.
