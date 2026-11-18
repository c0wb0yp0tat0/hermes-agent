# HY4-ACES-LOOP-PLAN-20261118 — the fleet plans Hy4's redo (seat: meituan/longcat-2.5:free)

Stage 2 of the Hy4 remedy: the ACES think-tank loop Hy4 rides so its deliverable reaches the regroup-memo caliber. Read: `HOW-EQUIP-HY4-20261117.md` @753ead5dd4; `SKILL.md`; `HITL-MEMO-20261116.md`; `HY4-FIRST-RIDE-ASSESSMENT-20261117.md`; `NEMO-HY4-START-PLAN-20261117.md` + briefs; `NEMO-MOMENTUM-REGROUP-20261116.md` (caliber comparator); harness argparse (`--model --brief --artifact --rounds --logfile`). Not confirmed: the dots leg id; the live `HARNESS_MAX_TOKENS` value; scribe auth.

## 1. The loop — six stages, each exit-gated
The three-stager (compose -> verify -> fold) expands to six because ride 1's miss was a process gap (single-shot, no critique, no re-verification). Write-gate class lands as a per-stage exit gate; verdicts are three-state — CONFIRMED / REFUTED / NOT-CONFIRMED (ride 1's vocabulary).

**S1 spine-assembly** · Hy4 itself (`tencent/hy4-flash:free`) · in: HITL-SPINE day-one + HITL-MEMO Parts 1/4/5 · out: `HY4-LOOP-SPINE-20261118.md` (rows with receipt ids, counting rule stated, two surfaces named) · GATE: every receipt id re-read from the spine; count re-derived by rule; zero guessed counts ("not confirmed" where rows don't carry it) · scribe `rig-hy4-loop-spine` · receipt: commit sha + scribe sha + rounds.

**S2 draft** · Hy4 itself · in: S1 spine + regroup-memo bar · out: `HY4-REGROUP-MEMO-20261118.md` in the comparator's shape — verdict line; §1 risks named first (status + countermove); §2 next-launch block in order (seat/artifact/gate/action); §3 carry-in; §4 receipt stamps; loop-state line; <=120 lines, zero emojis, every factual line receipt-backed, opportunities who/where/when, no meta · GATE: all five shapes present; <=120 lines; 0 emojis; receipt density 1.0 on factual lines; register slips 0 · scribe `rig-hy4-loop-draft` · receipt: sha + longest answer vs cap.

**S3 critique** · `stepfun/step-3.7-flash:free` — did NOT draft, blind to the composer log · in: S2 draft + S1 spine only · out: `HY4-CRITIQUE-20261118.md`, numbered deltas citing draft line + spine receipt · GATE: >=1 delta per category (receipt/count/register/opportunity) or a spine-cited nil · scribe `rig-hy4-loop-critique` · receipt: sha + delta count.

**S4 revision** · Hy4 itself · in: S2 draft + S3 critique · out: `HY4-REGROUP-MEMO-20261118-REV1.md` · GATE: closure 1.0 — every delta landed or refused with a spine-backed reason; counts re-derived; receipts re-cited; register clean · scribe `rig-hy4-loop-revision` · receipt: sha + closure tally.

**S5 verification** · `upstage/solar-mini4:free` (isolated primary; never drafted) + Kenari beam-vs-dots A/B second blind leg (`beam-1-0:free`; dots id not confirmed — re-probe, `longcat-2.5:free` stands in) · in: REV1 + S1 spine ONLY (blind to the critique) · out: `HY4-VERIFIED-20261118.md` — per-receipt CONFIRMED/REFUTED/NOT-CONFIRMED with the receipt id, plus the §4 receipt stamps re-checked against a fresh read; count verdict with rule · GATE: every memo receipt CONFIRMED; count agrees; both legs agree else a named delta · scribe `rig-hy4-loop-verify` · receipt: sha + verdict tally.

**S6 landing** · head fold (no model seat; the fold is not a drafting act) · in: REV1 + verification verdict · out: branch carries the memo + sentinel + loop records · GATE: byte-identity (scribe cell sha == committed artifact sha); memo-grade checklist 3/3 PASS; fold sha recorded · scribe `rig-hy4-loop-landing` · receipt: fold sha.

Loop-state: `CONTINUE + Hy4 rides when the plan lands`.

## 2. Peaking plan — measurement per stage
Class corroborations only (design stays ours): write-gate L0 = per-stage exit gates; evidence-gated admission = gate before the next stage; read-side evidence-plane verifier = S5; AIMD envelope = rounds policy below; validity decay = receipts re-established at S5, never carried from S2.
- **S1**: receipt coverage = distinct spine ids cited / total counted rows (bar 1.0); rule stated; two surfaces named; longest answer < cap.
- **S2**: shape 5/5; lines <=120; emojis 0; receipt density 1.0; register slips 0; opportunities closed (all); longest answer < cap.
- **S3**: yield = deltas per category, >=1 or spine-cited nil; 100% cite draft line + spine receipt.
- **S4**: closure = 1.0; receipts re-derived; register re-clean.
- **S5**: agreement = every receipt CONFIRMED + count agrees + A/B agree; any REFUTED -> named delta -> one bounded revision round (max 2, then head adjudicates).
- **S6**: landing checklist = sha match + 3/3 PASS + fold sha.
- Envelope (AIMD-class): S1 8, S2 8, S3 5, S4 6, S5 5 (+3 A/B); +1 on truncation or READ-GATED forfeit, -1 on a clean pass; cap raised only on measured truncation.

## 3. Board wiring
Drafter: Hy4 (S1/S2/S4). Critic: `step-3.7-flash:free` — did not draft, cold read. Verifier: `solar-mini4:free` in a fresh process, isolated, blind to the critique; second blind leg = the beam-vs-dots A/B. Diversity: drafter != critic != verifier; no seat sees another seat's log; my seat (`longcat-2.5:free`) is the planning lane and stands in for the dots leg. Blind doctrine: critic reads draft+spine; verifier reads REV1+spine, never the critique; every verdict three-state and carrying the receipt id checked. Fold head-owned.

## 4. Firing brief — sequential, one command per stage
Stage briefs cut from §1 by the head at fire time: `HY4-LOOP-S1-BRIEF.md` … `S6` (<=6,000 chars each). Shape: `python3 /root/scripts/copycat-harness.py --model <id> --brief <path> --artifact <path> --rounds <n> --logfile <path>`.
- S1: `--model tencent/hy4-flash:free --brief .../HY4-LOOP-S1-BRIEF.md --artifact .../HY4-LOOP-SPINE-20261118.md --rounds 8 --logfile .../HY4-LOOP-S1-LOG.md`
- S2: `--model tencent/hy4-flash:free --brief .../HY4-LOOP-S2-BRIEF.md --artifact .../HY4-REGROUP-MEMO-20261118.md --rounds 8 --logfile .../HY4-LOOP-S2-LOG.md`
- S3: `--model stepfun/step-3.7-flash:free --brief .../HY4-LOOP-S3-BRIEF.md --artifact .../HY4-CRITIQUE-20261118.md --rounds 5 --logfile .../HY4-LOOP-S3-LOG.md`
- S4: `--model tencent/hy4-flash:free --brief .../HY4-LOOP-S4-BRIEF.md --artifact .../HY4-REGROUP-MEMO-20261118-REV1.md --rounds 6 --logfile .../HY4-LOOP-S4-LOG.md`
- S5a: `--model upstage/solar-mini4:free --brief .../HY4-LOOP-S5-BRIEF.md --artifact .../HY4-VERIFIED-20261118.md --rounds 5 --logfile .../HY4-LOOP-S5-LOG.md`
- S5b: `--model beam-1-0:free --brief .../HY4-LOOP-S5B-BRIEF.md --artifact .../HY4-VERIFIED-AB.md --rounds 3 --logfile .../HY4-LOOP-S5B-LOG.md` (dots leg same shape)
- S6: `git -C /root/workspace/repos/hermes-agent add studies/rfc-143379-rig && git -C /root/workspace/repos/hermes-agent commit -q -m "HY4 ACES loop: memo-grade deliverable + verification" && git push origin study/rfc-143379-rig-20261105`

Order sequential; stop at the first failed gate (retry once, then head repairs). Loop-state: `CONTINUE + Hy4 rides when the plan lands`.

## 5. Risks + refusals
- Single-shot flattening -> six mandatory gates; nothing skippable; the loop-state line requires CONTINUE.
- Cap starvation -> write-first skeleton, longest-answer measured, cap raised only on measured truncation.
- Register drift -> critique category + S5 re-check; zero meta-vocabulary bar.
- Receipt drift -> blind S5 re-reads receipts from the spine; three-state verdicts; A/B second leg; two-surface counts named.
- READ-GATED forfeits -> fix assumed live (lane read-acquittal tracked; zero-successful-read lanes flagged at fold); a gated stage does not pass; retry once.
- CREATOR-GAP stays a gap: content-null parse artifact when max_tokens expires mid-thinking — null content is never a verdict; re-run with a raised cap and record it; free-plan allowance unpublished — probe, never invent a cap; lane-side git possible — fold doctrine holds only where the gate enforces it; spotty free legs (solar-mini pairing probes, kenari rate limits) — retry once, then pass with a named gap.
- Refusals/not-confirmed: dots leg id; live cap value; scribe auth. No claim beyond my reads.

Tail: one write; §1-§5 present; commands use the harness's real flags; claims trace to the reads listed.
