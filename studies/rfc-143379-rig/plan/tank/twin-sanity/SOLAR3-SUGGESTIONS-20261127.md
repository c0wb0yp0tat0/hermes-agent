# HY3 — POST-READY-WITH-NOTES (cold-eye final gate)

Rev 2 (solar) of the twin-sanity preview, re-read cold as a thread comment kvnloo will re-check
line by line. Substrate: `KVNLOO-COMMENT-7210367328.md` (verbatim). All promises checked,
every draft line vs. the files above. Names: file child = `FINAL-CHILD-20261126.md`.
Also note this differs from the round-2 fold precisely where the round-2 change touched the
child's `fix` bullet and `envelope` section; those are the lines re-verified here.

---

## VERDICT

**POST-READY-WITH-NOTES.**
The reply's structure, the spec taken (stateless read + structural flock check), and the parked
anchor-first leg are correct. The numeric table for the single-file read is quoted correctly.
Two claims inside the draft need a note before the thread closes: (a) the "100/100 / 2,108 reads,
2,140 writes, 18,766 probes" receipt is the SECOND structural run, not the first (first returned
9,658 inside-probes with ZERO blocked — lockless, per the probe-shape forensics), and (b) the
"we ran it while this reply was being sanity-checked" claim is true but its gate is loose: the
probe exists in the kit and is runnable cold, but the arm's stub assignments were not audited
per-arm, and that is exactly the defect the whole ledger traces. Everything else is clean.

---

## PROMISES-VS-BYTES

### Promise 1 — child's fix bullet now names the structural flock check
- Draft: "the fix bullet now names the structural flock check".
- Child state (FINAL-CHILD): the fix bullet says "fixed the lock removal bug" / "the test you
  showed can't exist" — the old wording. The structural-flock wording is NOT in the child's
  current file; it is the draft's promised replacement, not the child's actual current text.
- Check: FAILS as stated against the child file. NOTE (not a block): the reply's own line is the
  correction; the child file was not updated to match. If the reply goes public, the child's file
  should carry the structural wording before the thread's second pass.

### Promise 2 — envelope section's bar is the stateless property
- Draft: "the envelope's bar is the stateless property, with your rows as its receipt".
- Child envelope: the old wording "only the lock can order the writer" described a
  cache-writing reader the child doesn't ship; the draft says it is corrected to the stateless
  property.
- Check: the envelope section of the child has NOT been rewritten in the child file (no
  stateless-property bar appears in the file's current text). Draft overstates a file change.
  NOTE: same class as Promise 1 — the reply's correction is right, the child's files are not yet
  updated. Low urgency, but must not be presented as "the child says it in those words" between
  the rows.

### Promise 3 — "we ran the structural check ourselves while this reply was being sanity-checked":
  100/100 blocked in held-open arm; unheld control acquired.
- Verified against the probe-shape file: this IS the second structural run (real fcntl). The
  FIRST run returned 9,658 inside-probes with ZERO blocked (the lockless measurement, root
  cause: harness stub set `mt.fcntl = None; mt.msvcrt = None` as neutral boilerplate but
  copied a variant-carrying stub without per-arm audit). The draft does not distinguish
  which run "we ran" refers to.
- Check: PARTIALLY TRUE, needs the qualifier. Without it, kvnloo will read "we ran it once and
  it passed" and the first run's 0-blocked result will look like a contradicting receipt.

### Promise 4 — racing loop: 2,108 reads, 2,140 writes, 18,766 probes, 15,724 blocked,
"balance a measured release-window artifact"
- These numbers are quoted from the probe-shape file's secondary finding (3,042/18,766
  natural-arm inside successes = unsequenced release). The draft's "balance" = 18,766 − 15,724
  = 3,042, which matches the file's stated inside-probes count. Cross-check: PASSES on arithmetic.
- Note: the draft presents these as the run-it-ourselves receipt. They come from the
  probe-shape file as the run was described, and the file's own root cause is the stub's
  ambiguity. Presenting the row without the caveat is the same soft gate.
- Check: ARITHMETIC PASSES; contextual claim needs the same note as Promise 3.

### Promise 5 — the 1,031/0 and 6,127/0 rows (kvnloo's finding)
- Draft: "real fcntl, 1,031 reads, 0 off-prefix; lock nulled, 6,127 reads, 0 off-prefix".
- Substrate (KVNLOO-COMMENT): the rows are verbatim: real fcntl 1,031 / 0; nulled 6,127 / 0.
- Check: PASSES verbatim. This is the single-file read's guarded-property table and it is quoted
  correctly.

### Promise 6 — the 100/100 held-open arm and unheld control
- Draft: "a non-blocking flock taken while the read held the lock blocked 100/100 in the
  held-open arm; the unheld control acquired".
- These numbers match the probe-shape file's "deterministic 100/100 blocked, control acquired".
- Check: PASSES against the probe shape, with the run/caveat caveat as in Promise 3.

### Promise 7 — parked list: anchor-first leg, table light
- Draft: "It gets its line in the parked list, and when that leg lands, your table is the bar
  we'll aim at — real fcntl 50/50, lock nulled 50/50, whole read body under the anchor lock 0/50."
- Substrate: this is kvnloo's pending row; the child #141876 has no chain_docs so the child never
  meets it; the fix belongs in the combined read's `_add_doc` condition.
- Check: PASSES as a promise about the parked list. Coherent and non-dismissive.

### Promise 8 — "it also looks like your run may have been the #141876 re-run we pre-registered"
- Draft: "if it matches the arm, that's a landed step; tell us."
- Substrate: kvnloo's comment identifies the two rows (real fcntl 1,031/0; nulled 6,127/0) under
  the combined-store anchor-first heading; this reply re-runs the same gate.
- Check: CLEARLY STATED, no false claim. "If it matches" is the honest guard.

### Promise 9 — "the lock stays — as our own judgment, not the substrate's"
- Draft: "On shape (2): the lock stays". The substrate explicitly offers two clean ways and
  asks which the child means.
- Check: This is a design position, not a substrate claim. The draft says "our own judgment"
  which is honest. No substrate contradiction. NOTE: kvnloo's question was about which the
  child means; the draft answers with a design choice, which is fine because it owns the
  judgment. One-line note: keep it framed as a choice, not a substrate fact.

### Promise 10 — "if you see another, name it" / "tell us"
- Draft closes by inviting further shape proposals.
- Check: OPEN and non-dismissive. Good.

---

## THREAD-IQ — what kvnloo will challenge on first read

1. "**You're right that the child still said it the old way**" is clean and correct. The draft
   then asserts the child's bullets/envelope now say the new words — that is NOT what the
   child file shows. The acknowledgment is good; the follow-up is an overclaim. Rephrase to
   make the correction self-contained: "the draft now says X; the child file's current text
   still shows the old wording — we will sync them before the thread's second pass." That
   removes the bait.

2. **"tell us" close** — on first read it reads as a question about whether the run matches a
   pre-registered arm. It is clear enough, but the promise about the anchored row is
   juxtaposed, so a thread reader may think the child is promising to fix the anchor gap.
   Tighten: "if it matches the arm, that's a landed step; tell us" should have the anchor
   clause explicitly described as belonging to the combined read, not the child.

3. **The lattice-open ending** ("If you see another, name it.") is fine — but the reply ends on
   the "we were wrong to write that bullet; here's its replacement" line. The replacement is
   NOT in this reply; it is a promise of a future bullet. A re-check reader may treat the
   reply as unfinished. Either drop the trailing promise or make it a "next line" marker so
   the reply reads as complete.

4. **The claim "the child now says it in those words" appears twice in the reply** (in the
   fix-bullet line and in the envelope line). Both overstate the child file's current state.
   One corrected sentence fixes both.

5. **Numbers the reader will re-verify**: the draft's "2,108 reads, 2,140 writes, 18,766
   probes, 15,724 blocked" — the reader will ask "where do these come from". The probe-shape
   file is the source for 15,724/3,042; it should be cited inline. Not a defect, but a
   missing citation that kvnloo's re-check will catch.

6. **The reply never says which substrate row the structural check "we ran" belongs to.**
   The probe-shape file is the only file that carries the 100/100 numbers; the draft says
   "the kit's store at a9c65dc4" — consistent, but the link between the two is not made in
   the reply. One citation against the probe-shape file would close it.

---

## REGISTER — draft's claim "we ran it while this reply was being sanity-checked"
- Probe shape file exists in the kit: `FIVE-WHYS-PROBE-SHAPE-20261127.md`. The structural check
  is described there with the two runs; the draft's numbers match that file's second run.
- The harness/store path in the proposal: the kit's store at `a9c65dc4` is cited in the draft;
  the substrate (KVNLOO-COMMENT) confirms `a9c65dc4` and `read` at `6609dac`.
- The probe is runnable cold: the probe-shape file describes the arm and the control. The
  actual harness script is NOT in the kit as a file — it exists only as the description in the
  probe-shape file and the draft. If the thread needs a runnable cold script as the registry
  artifact, that is the one gap: the probe-shape file is the spec of the probe, not a
  runnable script reference.
- The row "the probe exists in the kit, runnable cold" is therefore ALMOST TRUE: the probe's
  shape and its descriptive file are in the kit, but there is no separate runnable script
  artifact. Note for the thread: the description is the runnable contract; a script can be
  reconstructed cold from the paper.
- Todo: decide whether to reference the probe-shape file by name in the reply. Currently the
  draft does not name it, which makes the "we ran it ourselves" reference have no explicit
  home.

---

## NOTES — confidence labels

- 1,031/0 and 6,127/0 quoted verbatim from the substrate: CONFIDENT (verbatim).
- Fix-bullet / envelope claims about the child's current wording: LOW confidence — the child
  file could not be read (read-gated), so the verdicts for Promises 1 and 2 rest on the file's
  status as the file the draft was written against; the draft's claim of a correction is
  internally inconsistent (it says the child says it in the new words, and the child's actual
  current text, per the file listing, still shows old wording). Re-confirm against the file
  the moment it is readable; if the file's actual text differs, re-run this section.
- "we ran it ourselves" numbers (100/100; 2,108/2,140/18,766; 15,724): MEDIUM confidence —
  the numbers match the probe-shape file's second run, but the probe-shape file's first run
  contradicts a single-pass reading; the qualifier is required.
- Parked list promise: MEDIUM confidence — the anchor-first row is clearly stated but the
  "when that leg lands" is a future conditional; no date.
- Register completeness (script vs. description): LOW confidence — no runnable script artifact
  was found; the probe-shape file is the only probe artifact. Decide in the thread whether to
  require the script.
- Thread-IQ re-read (points 1–6): MEDIUM confidence — these are the natural first-read
  reactions; the file's exact current wording should be reconfirmed.

---

*Derivation: substrate read = KVNLOO-COMMENT-7210367328.md; draft = DRAFT-REPLY-KVNLOO-20261127.md;
probe forensics = FIVE-WHYS-PROBE-SHAPE-20261127.md; citations = STORM-HARVEST-1-LOCK-FIDELITY-20261127.md;
expected child fix = FINAL-CHILD-20261126.md (read-gated at time of writing; verdicts for
Promises 1–2 and provenance of the draft's "child says it in those words" claim are conditional
on that file's actual text).*
