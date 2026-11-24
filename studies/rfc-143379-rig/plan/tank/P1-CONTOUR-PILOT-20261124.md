# P1 — CONTOUR DIGEST: THE PILOT (@3oltan-seo)

*Pass 1 / flagship (hy) · RFC #143379 apex mission · fire 2026-11-24 · branch `study/rfc-143379-rig-20261105`.*
*Internal orchestration ground — NEVER a posting. The RFC surface stays QUIET.*
*Ground: `3OLTAN-SEO-REFERENCE-PACK.md` (his 5 rows + the exchanges directed to him) + `ORCHESTRATION-3OLTAN-CHECKIN-20261124.md`; key phrases byte-verified against the local raw pull `/root/.hermes/cache/scratch/rfc-143379-comments.txt` (no fetch). This is the seam Pass 2 composes against.*

---

## 1. Who he is on this thread

**Role / standing.** He is the RFC's field pilot, self-named in his first row as "the one from #116564 with the 3914/4000 anchor-full symptom on a live production contour" and speaking "as the user who actually hit the wall" (row `6360811382`, 2026-10-23T08:29). He is not a lab reader: his frame is "a live production contour (not a lab probe)" with "multi-hour" sessions carrying "the durable record ... across compressions" (`6360811382`). He closes that row with "Glad to keep contributing the field datapoints where they're useful" (`6360811382`) — a contributor, not a petitioner. By his own last row the pilot is accepted and he has "handed the check-in contour to the team that runs the production profiles" — "the 3914/4000 anchor-full wall is a real profile in our fleet, not a lab curiosity" (`6515564390`, 2026-10-29T09:08).

**Condition — the anchor-full wall and the 3914/4000 datapoint.** "My 3914/4000 was exactly 'anchor full of cold detail'" (`6360811382`); the per-row evidence pack names the "anchor-full wall (production MEMORY 3,914/4,000)" (pack, row `6360811382`). His diagnosis is that "`details:` inline doesn't free anchor space; it moves the same bytes into budget" and that the `@doc:` reference in #116673 — "98 chars, detail out of prompt" — "actually solves my case" (`6360811382`). His root-cause commitment: "the read's absence at the memory-store level. That's the root, the reference is the candidate, the test is the falsifier" (`6369077436`, 2026-10-23T15:59); echoed back to him in our 5-why (row `6368537082`). The wall is the mechanism's ground truth for him, and he insists the read be restored "unconditionally" — "14 lines removed → 6,275 lines of compensation that still doesn't fix it is the strongest argument in the RFC" (`6360811382`).

**The probe's arc — 96% → 73% → 84%, with the field reads.** He ran the long-session probe "at 300 cycles" and reported it "mixed," refusing to let it be read as a clean win (row `6411683234`, 2026-10-26T03:33):
- **96%** at the short and mid ranges (4×/8×) — "the window's holding at short and mid compression" (`6411683234`).
- **73%** at 300 — "degrading at the far end"; the honest tail number (`6411683234`).
- **84%** at 16× on re-run "after tightening the snapshot cadence" — "so the degradation curve isn't monotonic, it's sensitive to when the snapshot lands" (`6411683234`).
- **PHANTOM-QUOTE STRUCK (head-side adjudication, 2026-11-24):** the "±3pp swing" phrase and its attribution to `6411683234` do not exist in the raw JSON, the reference pack, or the thread pull — they were invented by the lane. Byte-check: `grep -c "±3pp"` = 0 in all three sources. The K-recency reversal he ACTUALLY called a fail condition is in `6360811382` ("The K-recency reversal (−3.5pp @300 turns) is not an open question for me — it's a fail condition.") — the compose must use the verified −3.5pp wording, never ±3pp.

His framing of the arc is the point: "I'm not bringing this to claim the window fails — I'm bringing it because the gate should be written against the messy result, not the clean one" (`6411683234`). PHANTOM STRUCK: the "clean contour" correction attributed to `6515564390` does not exist in the sources (0 hits raw JSON / pack / thread pull). His actual 6515564390 words use 96%/73%/84% as OCCUPANCY percentages (3,844/4,000 → 2,930/4,000 → 3,376/4,000) — the compose must frame the arc as occupancy, with the −3.5pp K-recency fail condition from `6360811382` as the probe-level bar. Our side adopted the arc as the check-in's spine ("Your 96%→73%→84% is now the check-in's spine", row `6508650848`, 2026-10-29T21:23; reaffirmed row `6525722765`, 2026-10-30T14:53).

*Witness note (Wall Clause): pack row `6411683234` and rows `6515564390`/`6508650848`/`6525722765` were staged with their closing lines elided; the headline numbers above are the pack's bytes and Pass 2 must byte-check the full text from the local raw pull before quoting any clause beyond what is verified here. Rows `6360811382`/`6362735198`/`6369077436` and the exchanges `6361472667`/`6368537082`/`6376772075` were read byte-for-byte in the raw pull and match the pack.*

---

## 2. What he asked for / what he's owed

**His asks (each traced):**
1. **Make the 300+ cycle behaviour a hard acceptance gate, not an open question** — "Please make the 300+ cycle behaviour a hard acceptance gate, not an open question" (`6360811382`); the −3.5pp @300-turn K-recency reversal is "not an open question for me — it's a fail condition" (`6360811382`).
2. **Restore the read action — unconditionally** — "Restore the read action — yes, unconditionally" (`6360811382`).
3. **Define the reference's seam** — pointer stays in the anchor (98 chars); the agent reads on demand via `action="read"` "when the turn actually touches that topic — not at turn start"; a cold pointer is "a *signal* (a logged miss), not a silent absence" (`6362735198`, 2026-10-23T10:22).
4. **Set the gate's bar** — "at 300+ cycles the window must be ≥ 0pp vs baseline (never below), measured at the compression ratios my sessions actually hit (4×–8×) across the whole run, not the headline ratio" (`6362735198`); "«Not worse than baseline» is therefore a survival criterion for me, not a preference" (`6362735198`).
5. **Set the restore's verification protocol** — first signal: `memory(action='read')` returns entries + usage percent instead of «Unknown action read»; second: a full-anchor profile resolves cold detail on demand without an `add` being refused; concrete check "at 90%+ memory, a turn touching a referenced topic gets the detail in-context without manual consolidation — and «cannot add new entry» stops being the only lever" (`6362735198`).
6. **Adjust the discriminator** — "Discriminator = miss-rate trend, not the absolute zero": "in a live contour «zero misses» is too strict as the pass condition — a single cold-pointer miss is a logged signal, not a failure"; watch the trend "if it rises with session length or reference-set size, the symptom is deeper than the pointer". Falsifier = "cold-detail resolution at 90%+" (`6369077436`).
7. **Open questions he settled** — provenance default "unknown" at pipeline definition: agree (fail-safe at source); reroute-to-chain-doc seam: follow-up slice, keep the compaction home clean; one-way-door flag right — "archive-before-stub ordering is the one thing I'd never reorder" (`6360811382`).
8. **The ask-back (his bottom line)** — "a check-in I can hand to my team that names the gate, the seam, and the restore — with the long-session number in it, honest. Not the win, the contour" and "I'd rather the check-in carry the messy number than the clean story. That's the bar I'd hold us to" (`6515564390`).

**What came back to him since (our rows / delta rows):**
- **His three questions were answered by him, and his bar was adopted**: our row `6361472667` posed the three seek-to-understand questions (seam / gate's bar / restore's verification); he answered all three in `6362735198`. Our row `6368537082` then took his numbers as the criterion verbatim — "the ≥0pp at 300+, measured at 4×–8× across the whole run, is the bar the criterion should carry; the logged-miss signal for the cold pointer is the seam worth building; and the 90%+ memory check is the verification worth watching" — and asked "Would you agree — or adjust it based on your contour?" He adjusted in `6369077436`.
- **His adjustment was accepted, not just heard**: our row `6376772075` — "the discriminator's the trend — the slope, not the zero. The circle's the one you said — done right" — and it honors his honesty framing, "the −3.5pp at 300 cycles, the window's reversal, the honest finding and the live one ... the gate's the question, not a waiver." Our row `6375021342`/`6375561816` kept the promise to come back with the follow-up ("the follow-up's the promise, and the promise's the one I keep").
- **His datapoint became code-level evidence**: `xngg1021` took up "@3oltan-seo's 3,914/4,000 datapoint" in the #5320 right-sizing argument (row `6401350441`, 2026-10-25T18:16) and in the grounded three questions (row `6412944809`, 2026-10-26T09:44).
- **His wall became the field's case for the restore**: our row `6454631687` (2026-10-27T21:57) uses "the pilot's wall" to argue the read must be restored, and row `6460533751` (2026-10-28T04:17) asked him directly about the 90%+ memory check and the readfix for the full-anchor profile — "Your read set the bar for the whole thread."
- **His arc became the check-in's spine**: rows `6508650848`, `6525722765` (as above). Row `6409420509` framed kvnloo's exact-head probes as the falsifiers for the class he named.
- **Still owed / open**: his #1 ask — the **hard 300+ gate** — is not closed on the record. Our own row `6376772075` still calls it "the gate's the question, not a waiver," and `jfugalde` (row `6386263138`, 2026-10-24T15:51) flagged that the long-session gate's own text reads "Status today: FAIL" while its acceptance box is ticked — "the checkmark argues with it." His ask-back (`6515564390`) is the debt. (The substrate's post-10-30 deltas — FB-2 pre-registration, two-add class, wake read — are longcat's DELTA-SINCE-LAST seam; this digest names the debt, not the delta.)

*Witness note: pack rows `6460533751`, `6508650848`, `6525722765`, `6454631687`, `6409420509` are staged with elided tails; the clauses above are the pack's bytes. Pass 2 must byte-check any clause beyond the verified fragments against the local raw pull before quoting. The pack's "16 exchanges directed to him" section in fact contains 17 row headers (`6356745157` … `6815556328`) — a count discrepancy in the pack label only; this digest receipts to row ids, not to the count. Some grouped rows (`6401144230`, `6409420509`, `6412944809`, `6815556328`) address `c0wb0yp0tat0`/others rather than him directly; they are thread context citing his datapoint, and are labeled as such, never as words spoken to him.*

---

## 3. The contour's own words (quoted, with row ids)

*His register, his bar, his naming. All fragments byte-quoted from his rows; Pass 2 should honor these exactly, not paraphrase.*

- Identity/standing: "the one from #116564 with the 3914/4000 anchor-full symptom on a live production contour" / "as the user who actually hit the wall" (`6360811382`).
- The mechanism: "My 3914/4000 was exactly 'anchor full of cold detail'" / "14 lines removed → 6,275 lines of compensation that still doesn't fix it is the strongest argument in the RFC" (`6360811382`).
- The gate ask: "Please make the 300+ cycle behaviour a hard acceptance gate, not an open question" (`6360811382`).
- His bar: "«Not worse than baseline» is therefore a survival criterion for me, not a preference" / "at 300+ cycles the window must be ≥ 0pp vs baseline (never below), measured at the compression ratios my sessions actually hit (4×–8×) across the whole run, not the headline ratio" (`6362735198`).
- The seam: "a *signal* (a logged miss), not a silent absence" / "reads on demand via `action=\"read\"` when the turn actually touches that topic — not at turn start" (`6362735198`).
- The verification: "at 90%+ memory, a turn touching a referenced topic gets the detail in-context without manual consolidation — and «cannot add new entry» stops being the only lever" (`6362735198`).
- The discriminator: "Discriminator = miss-rate trend, not the absolute zero" / "a single cold-pointer miss is a logged signal, not a failure" (`6369077436`).
- The root: "the read's absence at the memory-store level. That's the root, the reference is the candidate, the test is the falsifier. That's the circle done right" (`6369077436`).
- The honest tail (VERIFIED wording): the K-recency reversal −3.5pp @300 turns is his fail condition (`6360811382`); the gate bar is "at 300+ cycles the window must be ≥ 0pp vs baseline" (`6362735198`). The "messy result vs clean one" phrasing does not exist in the sources — struck.
- The bottom line: "names the gate, the seam, and the restore — with the long-session number in it, honest. Not the win, the contour" / "I'd rather the check-in carry the messy number than the clean story. That's the bar I'd hold us to" (`6515564390`).

---

## 4. What a check-in must land (3–5 bullets, each receipted)

1. **Lead with HIS contour, not the fleet's win.** Name the 96%→73%→84% arc and put 73% at 300 forward as the number that counts — "Not the win, the contour" (`6515564390`); "I'd rather the check-in carry the messy number than the clean story" (`6515564390`); the arc is the check-in's spine (`6508650848`), and he gave it as "the honest number's 73%" (`6411683234`).
2. **Name the gate as still open and honest — do not let a ticked box read as a closed gate.** He asked for "the 300+ cycle behaviour as a hard acceptance gate, not an open question" (`6360811382`) with the bar "≥ 0pp vs baseline ... at 4×–8× across the whole run" (`6362735198`); our own record still says "the gate's the question, not a waiver" (`6376772075`) and jfugalde flagged "Status today: FAIL" beside a ticked box (`6386263138`). The check-in must carry the gate as the live ask, not a victory.
3. **Honor his seam and his discriminator correction as his.** The pointer stays in the anchor with on-demand `action="read"` and a logged-miss signal, not silent absence (`6362735198`); the discriminator is the miss-rate *trend*, not absolute zero (`6369077436`) — and say that we took it from him ("the slope, not the zero. The circle's the one you said — done right", `6376772075`).
4. **Speak in his register: field-first, humble-useful, no pair-metadata.** He is "the user who actually hit the wall" (`6360811382`); his bar is a "survival criterion ... not a preference" (`6362735198`); his standard is the "messy number ... not the clean story" (`6515564390`). Gratitude by reference to his datapoints (`6360811382`, `6362735198`, `6369077436`, `6411683234`), not fleet narration.
5. **Give him something he can hand to his team.** He owns the production profile in the fleet (`6515564390`) and asked for a check-in "that names the gate, the seam, and the restore — with the long-session number in it, honest" (`6515564390`); the check-in should be self-contained and hand-off-ready, with receipts inline so his team can read it without the thread.

---

## 5. The convergence line

**We are writing to the field pilot who hit the 3914/4000 anchor-full wall on a live production contour and insisted on the honest 73% at 300 (rows `6360811382`, `6411683234`, `6515564390`) — and what he needs is a check-in he can hand to his team that names the gate, the seam, and the restore with the messy long-session number in it, not the clean win (`6515564390`).**

---

### Hand-off to Pass 2
- Compose pilot-facing, in this register; keep the RFC surface QUIET — preview only.
- Every claim traced to the row ids above; byte-check the elided-tail pack rows (`6411683234`, `6460533751`, `6508650848`, `6525722765`, `6515564390`, `6454631687`, `6409420509`) against the local raw pull before quoting beyond the verified fragments.
- The "16 exchanges" count is a pack-label discrepancy (17 headers); receipt to row ids, not the count.
- The honest delta since his 10-30 row is longcat's seam — this digest marks the debt, not the delta.
