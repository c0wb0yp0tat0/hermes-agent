# HY4-ACES-LOOP-PLAN-FINAL-20261118

## The Loop
Six stages with reconciled seats, inputs, outputs, and gates:

### S1: Spine Assembly
- **Seat**: `tencent/hy4-flash:free`
- **Input**: HITL-SPINE day-one + HITL-MEMO Parts 1/4/5
- **Output**: `HY4-LOOP-SPINE-20261118.md` (receipt ids, counting rule, two surfaces named)
- **Gate**: Re-read receipt ids, re-derive count, zero guessed counts.
- **Scribe**: `rig-hy4-loop-spine`

### S2: Draft
- **Seat**: `upstage/solar-mini4:free`
- **Input**: S1 spine + regroup-memo bar
- **Output**: `HY4-REGROUP-MEMO-20261118.md` (verdict line, risks, next-launch block, carry-in, receipt stamps, loop-state line)
- **Gate**: All five shapes present, <=120 lines, zero emojis, receipt density 1.0, register slips 0.
- **Scribe**: `rig-hy4-loop-draft`

### S3: Critique
- **Seat**: `stepfun/step-3.7-flash:free`
- **Input**: S2 draft + S1 spine
- **Output**: `HY4-CRITIQUE-20261118.md` (numbered deltas citing draft line + spine receipt)
- **Gate**: >=1 delta per category (receipt/count/register/opportunity) or nil.
- **Scribe**: `rig-hy4-loop-critique`

### S4: Revision
- **Seat**: `tencent/hy4-flash:free`
- **Input**: S2 draft + S3 critique
- **Output**: `HY4-REGROUP-MEMO-20261118-REV1.md`
- **Gate**: Closure 1.0 (every delta landed or refused with spine-backed reason).
- **Scribe**: `rig-hy4-loop-revision`

### S5: Verification
- **Seat**: `upstage/solar-mini4:free` (primary) + `beam-1-0:free` (Kenari beam-vs-dots A/B)
- **Input**: REV1 + S1 spine
- **Output**: `HY4-VERIFIED-20261118.md` (three-state verdicts: CONFIRMED/REFUTED/NOT-CONFIRMED)
- **Gate**: Every receipt CONFIRMED, count agrees, and A/B agree.
- **Scribe**: `rig-hy4-loop-verify`

### S6: Landing
- **Seat**: Head fold (no model seat)
- **Input**: REV1 + verification verdict
- **Output**: Branch with memo + sentinel + loop records
- **Gate**: Byte-identity (scribe cell sha == committed artifact sha), memo-grade checklist 3/3 PASS, fold sha recorded.
- **Scribe**: `rig-hy4-loop-landing`

## The Board and Rotation

The board is a fixed-rotation council with three seats:

- **Drafter**: `upstage/solar-mini4:free` (S2 Draft)
- **Independent Verifier**: `stepfun/step-3.7-flash:free` (S3 Critique)
- **Third Eye**: `tencent/hy4-flash:free` (S4 Revision) + `beam-1-0:free` (S5 Verification)

**Rotation Rule**: A base that drafted an artifact cannot critique, revise, or verify it.

## The Firing Map

The firing map is sequential, with one harness command per stage:

- **S1**: `python3 /root/scripts/copycat-harness.py --model tencent/hy4-flash:free --brief .../HY4-LOOP-S1-BRIEF.md --artifact .../HY4-LOOP-SPINE-20261118.md --rounds 8 --logfile .../HY4-LOOP-S1-LOG.md`
- **S2**: `python3 /root/scripts/copycat-harness.py --model upstage/solar-mini4:free --brief .../HY4-LOOP-S2-BRIEF.md --artifact .../HY4-REGROUP-MEMO-20261118.md --rounds 8 --logfile .../HY4-LOOP-S2-LOG.md`
- **S3**: `python3 /root/scripts/copycat-harness.py --model stepfun/step-3.7-flash:free --brief .../HY4-LOOP-S3-BRIEF.md --artifact .../HY4-CRITIQUE-20261118.md --rounds 5 --logfile .../HY4-LOOP-S3-LOG.md`
- **S4**: `python3 /root/scripts/copycat-harness.py --model tencent/hy4-flash:free --brief .../HY4-LOOP-S4-BRIEF.md --artifact .../HY4-REGROUP-MEMO-20261118-REV1.md --rounds 6 --logfile .../HY4-LOOP-S4-LOG.md`
- **S5a**: `python3 /root/scripts/copycat-harness.py --model upstage/solar-mini4:free --brief .../HY4-LOOP-S5-BRIEF.md --artifact .../HY4-VERIFIED-20261118.md --rounds 5 --logfile .../HY4-LOOP-S5-LOG.md`
- **S5b**: `python3 /root/scripts/copycat-harness.py --model beam-1-0:free --brief .../HY4-LOOP-S5B-BRIEF.md --artifact .../HY4-VERIFIED-AB.md --rounds 3 --logfile .../HY4-LOOP-S5B-LOG.md`
- **S6**: `git -C /root/workspace/repos/hermes-agent add studies/rfc-143379-rig && git -C /root/workspace/repos/hermes-agent commit -q -m "HY4 ACES loop: memo-grade deliverable + verification" && git push origin study/rfc-143379-rig-20261105`

## The Scribe Cells

- `rig-hy4-loop-spine`
- `rig-hy4-loop-draft`
- `rig-hy4-loop-critique`
- `rig-hy4-loop-revision`
- `rig-hy4-loop-verify`
- `rig-hy4-loop-landing`

## The Peaking Measurements

- **S1**: Receipt coverage = 1.0, rule stated, two surfaces named, longest answer < cap.
- **S2**: Shape 5/5, lines <=120, emojis 0, receipt density 1.0, register slips 0.
- **S3**: Yield = >=1 delta per category, 100% cite draft line + spine receipt.
- **S4**: Closure = 1.0, receipts re-derived, register re-clean.
- **S5**: Agreement = every receipt CONFIRMED, count agrees, A/B agree.
- **S6**: Landing checklist = sha match, 3/3 PASS, fold sha.

## The Conflicts Resolved

1. **Seat Assignment for S1**: Leg A assigned `tencent/hy4-flash:free` to S1, while Leg B assigned it to the planner lane (Kenari beam). **Resolved**: S1 is assigned to `tencent/hy4-flash:free` as per Leg A, with the planner lane role clarified as a separate rotation.

2. **Seat Assignment for S2**: Leg A assigned `tencent/hy4-flash:free` to S2, while Leg B assigned it to `upstage/solar-mini4`. **Resolved**: S2 is assigned to `upstage/solar-mini4` as per Leg B.

3. **Verification Seat**: Leg A assigned `upstage/solar-mini4` (primary) and `beam-1-0:free` (Kenari beam-vs-dots A/B) to S5. **Resolved**: Confirmed as per Leg A and B.

## Open Items

- **Unverified**: The `dots-3-note-preview:free` model id remains unconfirmed.
- **Unresolved**: The live `HARNESS_MAX_TOKENS` value and scribe authentication.

---