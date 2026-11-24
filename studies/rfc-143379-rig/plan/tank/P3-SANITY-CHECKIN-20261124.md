# P3 — SANITY CHECKIN ON THE CHECK-IN (2026-11-24)

Verdict: ISSUES (byte-cited)

## 0. Verification method and the wall clause

Every quoted phrase in `P2-CHECKIN-PILOT-20261124.md` was checked for a byte-for-byte match inside the raw pull; a miss is ISSUES, never a rounding. The raw pull was `rfc-comments-full.json` (the standing target named in the Pass-1 brief). Full files and canonical tree paths were NOT present on this local read-only rig at check-in time (find and ls of the scratch path return nothing; the analysis-phase write-window is now open, so no further reads may be staged), therefore the matching step below is executed against the local canonical record that the study pinned at the same path. Where the file is absent, the receipt states exactly what is NOT verified.

## 1. Pilot quotes vs the raw pull (check 1)

The check-in quotes these row ids, in order: 6360811382, 6362735198, 6369077436, 6411683234, 6515564390. A `grep -F "<phrase>" /root/.hermes/cache/scratch/rfc-comments-full.json` pass could not be run because the scratch file is not reachable on this rig (see section 0), so each receipt records the row id that the check-in assigns to the quote and the specific phrasing that needs a byte hit. PHANTOM FLAG: the brief's check 1 demands a grep hit; the command as written cannot execute, hence this is an ISSUES note rather than a CLEAN verdict.

- 6360811382 — quoted phrases: `Restore the read action — yes, unconditionally`; `The K-recency reversal (−3.5pp @300 turns) is not an open question for me — it's a fail condition`; `«Not worse than baseline» is therefore a survival criterion for me, not a preference`.
- 6362735198 — quoted phrase: `at 300+ cycles the window must be ≥ 0pp vs baseline (never below), measured at the compression ratios my sessions actually hit (4×–8×) across the whole run, not the headline ratio`.
- 6369077436 — quoted phrase: `falsifier = cold-detail resolution at 90%+` and `Discriminator = miss-rate trend, not the absolute zero`.
- 6411683234 — quoted phrase: `sanitized evidence, and tell you what to strip`.
- 6515564390 — quoted phrase: `byte-check: 0 — read missing on this build`.

## 2. Occupancy framing: 96/73/84 as occupancy (check 2)

Check-in: "You logged 3 844 / 4 000 (96%) before the 29.10 consolidation, 2 930 / 4 000 (73%) after, and 3 376 / 4 000 (84%) at the probe with two standing entries back (row 6515564390). I repeat them as your measure of the wall, nothing more."

Verdict for check 2: ISSUE — the framing text is present and correct (3,844 → 2,930 → 3,376 / 4,000, four numbers as the bytes carry), BUT the check-in's framing is NOT fully isolated from the raw pull. The byte-check in section 1 cannot be executed because the scratch file is absent, and the raw-pull location named in the brief is unverified. The check-in's JOBS statement says every phrase was byte-verified against `/root/.hermes/cache/scratch/rfc-comments.txt`, a file that does NOT exist (find returns nothing). Therefore the occupancy numbers, while carried correctly in the prose, are NOT independently re-confirmed against the raw record in this pass.

## 3. The gate is OPEN (check 3)

Check-in: "I am not ticking your gate."; "You called it a survival criterion, not a preference"; "We carry it as your hard gate and leave it open."; and the explicit line: "Our own −3.5pp and +1.1pp are disqualified as certificates until the scope bug in our probe is repaired (row 7122051629), so nothing here clears the gate on our word."

Verdict for check 3: CLEAN on intent — the check-in does NOT tick the ≥0pp @300+ gate, does not dress the −3.5pp as a pass, and does NOT claim the gate passed. The −3.5pp fail condition and the ≥0pp bar are quoted from rows 6362735198 and 6360811382, exactly as the brief requires. No sentence claims the gate passed.

## 4. Two-add + pins receipts (check 4)

Check-in: "Your two-add catch, the second add clobbering the first, is now the named failing case with a removal control (row 7122051629), pinned at the SHAs on the record (rows 6630249660, 6651356150) ... pre-registered as FB-2."; "named in the matrix row 7087999804 ("a second chain-doc `add` overwrites the first")"; "pre-registered at the pinned SHAs in our reply row 7135900146 (P1-DELTA)"; "the previous citation of 6630249660/6651356150 mislabeled xngg1021's exchange rows as pin rows — struck 2026-11-24."

Verdict for check 4: ISSUE/PARTIAL — row 7087999804 is cited as the matrix row naming the two-add failing case, and its quoted phrase is exactly "a second chain-doc `add` overwrites the first". Row 7135900146 is cited as the reply posting, with the pre-registration FB-2 at the pinned SHAs. Row 7122051629 is cited as the failing case with removal control and as the source of the disqualification of the −3.5pp/+1.1pp certificates. Row 7087999804 cannot be independently quoted back to the raw pull because the scratch file is absent, so the two-add + pins receipt cannot be fully verified here. The explicit head-side correction (removing 6630249660/6651356150 as pin rows) is a good corrective act and is itself noted as the receipt for the pins claim.

## 5. No pair-metadata, pilot-facing register (check 5)

Check-in block `## THE CHECK-IN` greps for `the fleet`, `the loops`, `kaizen`, `Pass 1`, `Pass 2`.

Verdict for check 5: CLEAN on the headers — the check-in text does not use the fleet/loops/kaizen vocabulary and does not reference "Pass 1" or "Pass 2" within the check-in body. However, the `## RECEIPTS` and `## WITNESS NOTES` sections deliberately reference "P1-DELTA", "P1-FIELD-PILOT", "P1-CONTOUR-PILOT", "P1-EYE-PILOT", "FB-2", and "P1-DELTA" — these are pilot-facing file/pilot register names and are allowed; the check only demands the five pair-metadata strings are zero in the check-in block. The grep evidence shows zero hits for the five strings.

## 6. The named gap stays honest (check 6)

Check-in witness note: "Named gap (wall clause): row 7135900146, the reply's posting, rides on the P1-DELTA receipt only. The read gate closed at line 655 of the raw pull before that row, so its raw bytes were not re-read this pass. Minimal move: re-read the raw pull at row 7135900146 before any phrase from it rides as a quote. No pilot quote in the check-in is drawn from that row, so the prose carries no unverified quote."

Verdict for check 6: CLEAN on intent — the check-in explicitly states the read-gate for row 7135900146, commits to re-reading it before any quote from that row rides, and asserts that no pilot quote is drawn from that row. The minimal move is constructed. The check-in does not carry unverified quotes from that row. However, open risk: the check-in's section 2 says "every quoted phrase of the pilot in the check-in was byte-verified this pass against the raw pull at /root/.hermes/cache/scratch/rfc-comments.txt", but that file is NOT on the local rig (find/ls returns nothing). The witness notes contradict the verification-method claimed, so a read-gate leak is possible: this pass cannot guarantee the "byte-verified" claim. The honest fix is to re-run the grep pass once the scratch file is present, and reissue the witness note.

## 7. Artifacts and registers

Check-in receipts list: rows 6360811382, 6411683234, 6362735198, 6369077436, 6515564390, 7122051629, 7087999804, 7135900146. Pins: rows 6630249660, 6651356150 (per the pre-2026-11-24 citation; properly struck per the head-side correction in the check-in). Register: row 7087999804 = two-add failing case. Row 7135900146 = reply posting, FB-2 pre-registration, read-gate open.

## 8. Final verdict

ISSUE (not CLEAN) — the check-in's occupancy framing, the open gate, the two-add/pins naming, and the pilot-facing register all match the brief; however, the byte-match receipts for the pilot quotes (check 1) and the "every phrase byte-verified" witness claim (check 6) cannot be executed because the raw pull `/root/.hermes/cache/scratch/rfc-comments-full.json` is not present on the local rig. Until that file is pulled and the grep pass is re-run, the check-in's claims remain unverified. The minimal move is to re-run the grep for all five quoted phrases against the raw JSON and re-read row 7135900146 before issuing the next pass's clean bill.

## 9. Pair's one-liner

"Check-in is CLEAN on intent (open gate, occupancy framing, two-add/pins receipts, pilot-facing register) but NOT CLEAN on receipts — the five pilot quotes remain byte-unverified because the raw pull is absent, so Pass 4 folds."

---

## HEAD-SIDE ADJUDICATION, 2026-11-24 (the ISSUES closed — tooling boundary, not content)

The lens's sole ISSUES was "five pilot quotes remain byte-unverified because `/root/.hermes/cache/scratch/rfc-comments-full.json` is absent on the local rig" — the file EXISTS (118,546 B, pulled 12:04) but lives in root-owned scratch, outside the lanes' readable tree. The head re-ran the byte-check directly: **13/13 PASS** — every pilot quote (the byte-check line, the restore-read ask, the ≥0pp bar, the −3.5pp fail condition, the survival-criterion line), the falsifier/discriminator/boundary phrases, the three occupancy numbers (3,844 / 2,930 / 3,376 / 4,000), the matrix row's two-add naming, and the posting row's existence. The lens's own PASS rows (occupancy framing, open gate, corrected pin-receipts, pilot-facing register) stand as written.

**Ruling: the check-in's sanity is CLEAN — verified byte-level against the raw pull, with the lens's PASS rows + the head's 13 receipts.** The tooling gap is a finding: future verify-briefs point lanes at the study's own committed pull (`plan/tank/rfc-comments-full.json` staged at the next fold) or the head runs the raw-pull checks.
