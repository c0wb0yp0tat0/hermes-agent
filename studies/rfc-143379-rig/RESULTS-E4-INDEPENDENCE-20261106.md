# RESULTS-E4-INDEPENDENCE-20261106 — the mirror's independence-probe (E-4)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public beyond the fork). **Seat:** the handoff's E-4 — the paid-leg's named question, run on the record's own terms. **Gated on:** `RESULTS-E3-CONTINUATION-20261106.md` (E-3's CELL-DEPENDENT), and the `NIGHTSHIFT-HANDOFF-20261106.md` line 112 (the fourth/last open question: "the four fleet landings' section-0 source-shape diff — the shared brief's echo vs the models' agreement — the convergence-signal's own audit"). **Register:** receipts, never claims. No instrument re-run; every string below is quoted from the branch's bytes.

---

## 0. The one-line verdict

**ECHO (in the mechanism-sentence's text) — MIXED-TO-DETERMINE (in the convergence's load-bearing weight).** The three fleet lanes' section-0s (krecency, longcat, solar-mini4) carry the **same next-mechanism sentence near-verbatim**; the fourth landing (step `bde8ff5f37`) is a **distinct-text, same-mechanism** lean. The mechanism name is therefore **brief-carried**; the pinning's weight rests on `RESULTS-PIN`'s own receipt (the base falsifier's measured margin), never on the four echoed sentences.

---

## (a) The source-shape diff — the four landings' section-0s side by side

The four landings, by commit:
- `19723b3c51` — krecency lane (106 lines)
- `77a441dc92` — longcat lane (144 lines)
- `1d70408531` — solar-mini4 lane (106 lines)
- `bde8ff5f37` — step lane (87 lines) — the step-designation's landing

### The four next-mechanism sentences (the object of the diff, quoted at the letter)

**krecency §0, bullet 5:**
> "**The one next mechanism: EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency.** The regime it names is already in the data — `seed 0` carries sub-zero deltas from cycle 60, `seed 1` from cycle 80 — and no existing arm pins. Falsifier: if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection."

**solar-mini4 §0, bullet 5:** identical, **token-for-token** (the only diffs in the whole file are the lane-name and the artifact path — 3 lines / 15,553 bytes vs 15,544):
> "**The one next mechanism: EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency.** The regime it names is already in the data — `seed 0` carries sub-zero deltas from cycle 60, `seed 1` from cycle 80 — and no existing arm pins. Falsifier: if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection."

**longcat §0, bullet 5:** the same sentence with one comma-level variation:
> "**The one next mechanism: EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency.** The regime it names is already in the data — `seed 0` carries sub-zero deltas from cycle 60**;** `seed 1` starts at cycle 80 — and no existing arm pins. **The** falsifier: if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection."

**step §0, bullet 5 (the fourth lens):** **a different sentence, naming a different candidate:**
> "**The one next mechanism (divergent from the prior lanes' pinning/archive proposals): ALIAS-AWARE FORMAT-PINNING.** Pinning the exact bytes protects the literal (PIN proves it) but the aliasing arm shows format-collisions defeat recovery precisely when the literal is evicted — a pinned exact copy does not pin the format-class, so a look-alike rival still collides at the read. Pin the literal's format-signature (a tombstone that rejects format-neighbors), not just the bytes."

### The shared-phrasing inventory

**Exact repeated strings (the receipts; quoted):**

1. The next-mechanism sentence, token-for-token — krecency ≡ solar-mini4; longcat differs by 2 tokens. Contains, verbatim in all three:
   - "**EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency**"
   - "The regime it names is already in the data — `seed 0` carries sub-zero deltas from cycle 60, `seed 1` from cycle 80 — and no existing arm pins."
   - "if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection."
2. The gate verdict sentence, token-for-token — krecency ≡ solar-mini4; longcat in paraphrase:
   > "The demand-age instrument is *derived* (no hand-injected decay term): `probe_age.py` returns the latent floor for K=0 and the literal's own presence in the K=10 snapshot otherwise; the per-cell min is `-floor` whenever the quoted literal is out-of-window and its survival coin misses."
3. The instrument's own record, quoted verbatim in both krecency and solar-mini4 §0 bullet 1:
   > "the noise floor's excursions, not a long-session-only collapse" — `RESULTS-AGE.md` UPDATE.
4. The `probe_age.py` byte-level bullets, near-identical across krecency/longcat/solar-mini4 §1.1:
   - "K=0 returns the constant floor: `if k == 0: return floor`, with `FLOOR = {2: 0.30, ...}`."
   - "K=10 scores a hit iff `q in snap` (the literal is among the last K of the stream); otherwise it survives with probability `floor` (`if rng.random() < float(floor): hits += 1`)."
   - "The query is `idx = max(0, n - 1 - age)` with `age = 1 + int((cycle/10)**1.3)`, and `n = max(ratio+1, cycle)`. The window is the *tail* `stream[-k:]`."
   - "So the per-cell score is one of three values: `1.0` (in-window), `floor` (survived), or `0.0` (missed). The per-cell delta is therefore **either `1-floor` (positive), `0` (survived), or `-floor` (missed)**."
   - "There is no aggregation trick that can hide it, and no hand-written decay curve multiplying hits (contrast `probe.py`, where `hits = int(round(hits * decay))` — the injected class the instrument parks as NOT EVIDENCE). `probe_age.py` has no such term."
5. The competition arm's instrument-limit sentence — krecency ≡ solar-mini4, token-for-token:
   > "the model built rivals that touch *only* the K=0 floor path and never the K=10 hit path (`probe_compete.py`), so a* is degenerate and the rival sweep cannot move the letter."
6. The archive arm's constructional sentence — krecency ≡ solar-mini4, token-for-token:
   > "the budget knob admits the demanded literal's ID and never a competing one (`probe_archive.py`), so the budget is toothless by construction (the "constructional-knob check" in `krecency-instrument/SKILL.md`)."
7. The constraint arm's finding sentence — krecency ≡ solar-mini4, token-for-token:
   > "recency-truncate is the worst strategy (violation 1.00) and pinning restores 0.00; this is the mechanism that names the K-recency window's eviction class."

**The distinct leans (named):**

- **longcat §0 bullet 3** — the archive arm's FAIL is "real under its (optimistic) conditions, but the mechanism is partly instrument-authored" (vs krecency/solar-mini4's "a constructional instrument-limit").
- **longcat §0 bullet 1** — "FINDING … with one protocol artifact named" (vs the others' bare FINDING).
- **beam §0 bullet 5** — "COMPETING-ADMISSION ARCHIVE (demand-age level)" — a **different candidate mechanism** (the archive-repair), not pinning.
- **step §0 bullet 5** — "ALIAS-AWARE FORMAT-PINNING" — a **different candidate** (format-signature, not bytes).
- **beam §0 bullet 2** — the scaled-K arm's NO "is a FINDING on the tested formula, with a protocol caveat" (the beam's addition; the others don't carry it).
- **step §0 bullet 4** — the SYNTHESIS seam: "written with lane B PENDING-FROM-LANE, and folds lane B's rows by mechanism-shape assumption, not by measurement — the integration chapter is derived, not verified."

### The shared-token count

| Pair | Diff lines (insertions/deletions) | Bytes | Note |
|---|---|---|---|
| krecency vs solar-mini4 | 3 / 3 | 15,544 vs 15,553 | the lane-name + artifact path only |
| krecency vs longcat | 93 / 55 | 15,544 vs 22,909 | longcat carries distinct adjudications + a §5 NOT-RUN register |
| krecency vs beam | 65 / 74 | 15,544 vs 22,300 | beam carries distinct candidate + scaled-K caveat |
| beam vs longcat | 102 / 73 | — | the two longest, most distinct |

The next-mechanism sentence itself: **krecency ≡ solar-mini4 = 100% identical; longcat = 98% identical (2 tokens); step = 0% identical (a different candidate).** The shared-verbatim block across the three lanes (the gate-verdict sentence + the `probe_age.py` bullets + the competition/archive/constraint sentences) runs to roughly **450 words of the section-0s' ~600 words** — the section-0s' prose is, for the three fleet lanes, a **template with a lane-name slot**.

---

## (b) The verdict — ECHO / AGREEMENT / MIXED-TO-DETERMINE

### Verdict: **ECHO** on the mechanism-sentence's text; **MIXED-TO-DETERMINE** on the convergence's weight.

**Receipt 1 (the echo).** The three fleet lanes' next-mechanism sentences are the same text (§(a) items 1–7). The mechanism name "EXACT-LITERAL PINNING (demand-age arm) with per-seed occurrence-count / recurrence / recency" is **not four independent arrivals** — it is **one sentence, copied**. The falsifier clause is copied too. The gate-verdict sentence and the `probe_age.py` bullets are copied. This is the **shared brief's echo**: the lane briefs (the record's own lane-dispatch texts) framed the next mechanism, and the lanes' section-0s reproduce the frame.

**Receipt 2 (the agreement-signal that survives).** The **distinct** leans are real and independent:
- longcat's "partly instrument-authored" archive read (vs the others' "constructional") — a different adjudication of the same arm.
- beam's scaled-K caveat + the archive-repair candidate — a different candidate mechanism, reached from a different reading of the same `RESULTS-AGE.md` K-SCALING table.
- step's alias-aware format-pinning candidate + the SYNTHESIS's "derived, not verified" seam — a different candidate **and** a different verdict on the integration chapter.
These are **not** echoes: they are the same record read with different adjudicative weight. The agreement-signal is **the distinct leans**, not the shared sentences.

**Receipt 3 (the fourth lens breaks the echo).** The step lane's next-mechanism sentence is a **different candidate** (ALIAS-AWARE FORMAT-PINNING) that **cites the pinning only as a premise** ("PIN proves it") and then diverges. This is the strongest single piece of evidence that the lanes were **not** merely parroting a planted conclusion — at least one lane **read past the frame**. The step lane's section-0 is also the only one that names the SYNTHESIS's own seam (lane B PENDING-FROM-LANE, "derived, not verified").

**Receipt 4 (the beam's file is the fifth, and the SYNTHESIS's WAVE-8 fold is the beam's own text).** `ddaaa83f8e` (WAVE 8) folds the beam lane's three additions into the head's SYNTHESIS — the beam's **distinct** reads (the a*-equal-weights mechanism, the two archive inertias, the scaled-K caveat) are the ones the head adopted. The head's WAVE-9 fold then cites the solar lane's "own-bytes, zero echo" content-check — **but the content-check's object was the krecency sibling**, and the solar file is 3-lines-different from the krecency file (§(a)). The "zero echo" claim is **against the wrong sibling**: the solar lane's section-0 is byte-identical to the krecency lane's, so the content-check that cleared it as "own-bytes" was a check against a file that is itself the echo.

### The verdict's sharpening

The four-lens convergence the record leans on is **two different things**:
1. **The mechanism-name convergence** (four lanes name exact-literal pinning) — **ECHO-CARRIED**. The name is brief-carried; the three fleet lanes' sentences are one text; the step lane's distinct candidate shows the frame was not universal, but the name itself is not four independent arrivals.
2. **The mechanism's load-bearing weight** (the pinning actually protects) — **NOT carried by the convergence at all**. It is carried by `RESULTS-PIN`'s own receipt: recurrence-aware pinning drops the deep-minima prevalence at the confirmed aliasing×proximity pair-ON cell from **1.00 (recency-pinned) to 0.15**, and the onset-test explains why (per-seed onsets differ: seed 0 = cycle 68, seed 1 = cycle 87 — per-seed occurrence predicts the onset, a recency-only pin loses the protection). That is a **measured margin in the record's own CSV** (`results/pin.csv`, 200 rows), independent of any lane's sentence.

So: **subtract the echo, and the four-lens claim's weight shifts entirely to the falsifier's own receipt (`RESULTS-PIN`) — never to the echoed sentences.** The convergence's rhetorical weight ("four independent lenses agree") is not evidence of the mechanism; the `RESULTS-PIN` margin is. The echoed sentences are the **brief's** receipt, not the models'.

---

## (c) The convergence-signal's sharpening — what the four-lens claim means once the echo is subtracted

**The claim, as the record leans on it** (SYNTHESIS WAVE 9): "four independent lenses now agree (the wheel, the guidance, the longcat lane, the solar lane), with the falsifier's PROTECTS verdict (1.00->0.15) behind the agreement. The convergence's signal: cross-model, byte-verified (the content-check vs the sibling: own-bytes, zero echo), receipted."

**Once the echo is subtracted:**
- The "four independent lenses" are **not four independent texts**. Three are one text (krecency ≡ solar-mini4 ≡ longcat's §0). The fourth (step) **diverges on the candidate**. The "cross-model" claim is **not** a cross-model convergence of independently-derived prose; it is **one brief's frame, reproduced**.
- The "content-check vs the sibling: own-bytes, zero echo" is **mis-aimed**: the solar file is 3-lines-different from the krecency file (the lane-name + artifact path), so the check that cleared it was a check against its own echo. The check's **object** was the sibling it echoed, not an independent text.
- The **genuine** convergence signal is **not** the shared sentences — it is the **distinct leans** (longcat's "partly instrument-authored", beam's scaled-K caveat + archive-repair candidate, step's format-pinning candidate + the SYNTHESIS-seam verdict). Those are the same record read with different adjudicative weight, and they are **the agreement-signal the record should cite** — not the copied next-mechanism sentence.
- The **load-bearing** convergence is the **PROTECTS margin** (`RESULTS-PIN`): 1.00 → 0.15 at the worst cell, with the onset-test's per-seed explanation. That margin is **one instrument's measured result**, not a convergence of four texts. It stands on its own; the four-lens agreement adds **no** weight to it.

**The sharpened claim:** the record's four-lens convergence is **a brief-echo in its prose and a single-instrument measurement in its weight**. The pinning mechanism is **PROTECTS** because `RESULTS-PIN` measured it, not because four lanes named it. The lanes' convergence is **corroboration of the record's framing**, not independent verification of the mechanism.

---

## (d) The honest limits — what the diff cannot tell

1. **The briefs themselves are the seed the record mandated.** The lane briefs (the record's own dispatch texts) framed the next mechanism; the question is the **DEGREE** of the echo, not its presence. This probe measures the degree: **three of four section-0s carry the frame verbatim; one diverges.** The echo is **real and large** in the prose; it is **not total**.
2. **The diff cannot separate "the brief planted it" from "the models read the same record and wrote the same sentence".** Both produce the same bytes. The diff's evidentiary value is **negative** (the shared sentences are not independent arrivals) and **positive on the distinct leans** (the lanes did diverge where the record gave them room). It cannot adjudicate intent.
3. **The briefs are not in the branch's bytes.** The lane-dispatch texts are not committed as files (the `copycat-findings/` directory holds the findings, not the briefs); the "brief" is the record's own framing, reconstructible from the SYNTHESIS's waves + the guidance's landing-path + the lane files' shared sentences. This probe's echo-object is therefore **the shared sentences themselves**, not a brief-file diff. The brief's exact wording is **not byte-verifiable** here — a named limit.
4. **The step lane's divergence is the strongest anti-echo receipt, and it is one lane.** One divergent candidate (format-pinning) does not clear the other three; it bounds the echo's reach, not its absence.
5. **The `RESULTS-PIN` margin is the load-bearing receipt, and it is one instrument.** The probe does not re-run it; it cites it. The margin's own honesty (the recurrence-weighted membership's later REFUTED-BY-REPLICATION, SYNTHESIS wave 15) is a **separate** seam — the base pinning's 1.00 → 0.15 stands, the membership-enhancement's evidence was its injected onsets. The four-lens convergence is **not** the thing that would catch that; the E2 replication was.

---

## The one-line verdict (the finding's own form)

**ECHO in the mechanism-sentence's text (three of four section-0s carry the frame verbatim; the fourth diverges on the candidate); the four-lens convergence's weight rests on `RESULTS-PIN`'s own 1.00 → 0.15 receipt, never on the echoed sentences.**

---

*Register: receipts, never claims. No instrument re-run; no meters spent; no model credentials. Every quoted string is from the branch `study/rfc-143379-rig-20261105` (`copycat-findings/copycat-{krecency,longcat,solar-mini4,beam,step}-20261105.md`, `krecency/RESULTS-PIN.md`, `krecency/SYNTHESIS.md` waves 5–9, `git show bde8ff5f37`, `git show ddaaa83f8e`, `git show 19723b3c51`, `git show 77a441dc92`, `git show 1d70408531`). The diff's line-counts are `git diff --no-index` over the branch's blobs.*