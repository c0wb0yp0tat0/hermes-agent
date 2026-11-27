# HY3 — TWIN-SANITY, ROUND 3 (final preview to kvnloo)

*Cold read of the FINAL preview (DRAFT-REPLY-KVNLOO-20261127.md) as a thread comment kvnloo will re-check line by line, on the round-2 substrate + everything the fold changed. SUGGESTIONS ONLY; the draft is untouched. Verified against all five primaries: KVNLOO-COMMENT-7210367328, DRAFT-REPLY-KVNLOO-20261127, FIVE-WHYS-PROBE-SHAPE, STORM-HARVEST-1-LOCK-FIDELITY, FINAL-CHILD-20261126.*

## VERDICT
**POST-READY-WITH-NOTES.** The load-bearing promise holds: the child file actually carries the corrected structural wording in BOTH the fix bullet and the envelope bar. Every cited number reconciles against the substrate rows and the two structural receipts. The acknowledgment is clean and the close is thread-correct. Notes below are sharpness items for a line-by-line re-checker, not blockers — none flips the verdict. (Full POST-READY is withheld only for the ~4 notes under THREAD-IQ/REGISTER.)

## PROMISES-VS-BYTES

### Numbers — every one cross-checked
- Draft: *"real fcntl, 1,031 reads, 0 off-prefix; lock nulled, 6,127 reads, 0 off-prefix."*
  Verify: substrate §1 table — real `fcntl` **1,031** reads / **0** not-a-committed-prefix; nulled **6,127** / **0**. **MATCH** ("off-prefix" = "not a committed prefix"). [HIGH]
- Draft: *"a non-blocking flock taken while the read held the lock blocked 100/100 in the held-open arm; the unheld control acquired."*
  Verify: FIVE-WHYS — second run "deterministic **100/100** blocked, control acquired"; STORM-HARVEST §1 — "100/100 EWOULDBLOCK, observed." **MATCH** (two independent receipts). [HIGH]
- Draft: *"In the racing read/write loop (2,108 reads, 2,140 writes, 18,766 probes), 15,724 blocked, the balance a measured release-window artifact."*
  Verify: FIVE-WHYS secondary finding — "inside successes (**3,042/18,766**)" from unsequenced release; STORM-HARVEST §1 names the same "3,042 'inside successes' ... exactly as the man page predicts." **15,724 + 3,042 = 18,766** — arithmetic and characterization both reconcile. Sub-counts 2,108/2,140 are not in these two receipts (runner report would confirm). **MATCH** on the cited totals. [MED-HIGH]
- Draft: *"real fcntl 50/50, lock nulled 50/50, whole read body under the anchor lock 0/50."*
  Verify: substrate §2 table — real `fcntl` **50**, lock nulled **50**, whole-read-body-under-anchor-lock **0**, all "/50". **MATCH**. [HIGH]

### Promises about the child — THE load-bearing check (both verified TRUE)
- Draft: *"the child now says it in those words."* / *"the fix bullet now names the structural flock check, and the envelope's bar is the stateless property, with your rows as its receipt."*
  Verify FINAL-CHILD fix bullet: *"One regression test with real fcntl — the **structural flock check**: a non-blocking flock on `MEMORY.md.lock`, taken while the read holds it, must fail (contention errnos: EACCES, EAGAIN, EWOULDBLOCK — per the lock-fidelity harvest, 2026-11-27). The guarded property is **stateless**: the live list unchanged after a read that races a writer."* → names the structural flock check verbatim-in-substance and states stateless as the guarded property. **MATCH**. [HIGH]
  Verify FINAL-CHILD envelope ("The correctness envelope (the read's bar)"): *"the reader holds the store's lock across the snapshot and never writes the live list ... contention is the lock's own signature — the structural check (above), **not an output-level red**."* → bar is the stateless property + structural check, not an output-level red. **MATCH**. [HIGH]
- Draft: *"Its fix bullet claimed 'fails when the lock is removed' ... its envelope section's 'only the lock can order the writer'."* (the OLD strings)
  Verify: neither phrase appears anywhere in FINAL-CHILD; both are gone, replaced by the structural wording above. **MATCH**. [HIGH]
- Draft's *"with your rows as its receipt — real fcntl, 1,031 ... 6,127 ..."*: the child envelope actually cites a DIFFERENT kvnloo arm (comment 7187597182, "300 fresh runs per row ... 0/300 ... 300/300, receipt `fbefb4ac…e16`"), not the 1,031/6,127 rows from THIS comment. The 1,031/6,127 rows are kvnloo's new substrate numbers, so "your rows" is accurate attribution and the stateless bar is truly the child's — but the phrasing reads as if those exact rows are already in the child. **SOFT MISMATCH** — see THREAD-IQ note 1. [MED-HIGH]

### Promises about the errnos citation
- Child fix bullet cites "contention errnos: EACCES, EAGAIN, EWOULDBLOCK — per the lock-fidelity harvest." Verify STORM-HARVEST §2: filelock's `_CONTENTION_ERRNOS: {EACCES, EAGAIN, EWOULDBLOCK}`, "a test that only catches EWOULDBLOCK will flake/false-pass"; Meta-finding: "The one spec change the child should take: contention errnos = {EACCES, EAGAIN, EWOULDBLOCK}." The child took it. **MATCH — properly sourced.** [HIGH]

### Promises about the parked list / pre-registered re-run
- Draft: *"it parks with the substrate ... It gets its line in the parked list."* → substrate: "belongs with the parked substrate, not the child ... worth a line in the parked list"; FINAL-CHILD "Separated — out of this ticket (named, parked)" lists the doc-chain substrate and pins. **CONSISTENT**. Whether a parked-list file was edited is outside the five primaries. [MED]
- Draft: *"your run may have been the #141876 re-run we pre-registered — if it matches the arm, that's a landed step; tell us."* → hedged ("may have been", "if"), not an assertion; bar is the 50/50/0/50 table. FINAL-CHILD envelope confirms the re-run is "pre-registered in the same envelope." **Rhetorically safe, consistent.** [HIGH]
- Draft: *"#141876 has no `chain_docs`, so the child never meets it"* → substrate: "#141876 has no `chain_docs`." FINAL-CHILD is read-path-only and names the doc-chain substrate as parked. **MATCH**. [HIGH]

## THREAD-IQ
Direct answers: "(1) is the spec" commits unambiguously to his option (1), exactly his closing question. "You're right that the child still said it the old way" is an unhedged, clean acknowledgment and matches the FIVE-WHYS parent-class finding (the rig's own envelope was the first instance). "tell us" / "If you see another, name it" are invitations, not defenses — kvnloo-friendly.
1. **Envelope-receipt conflation (note 1):** because the child envelope cites the 300/300 `fbefb4ac` arm, not 1,031/6,127, a line-by-line re-checker may ask "your rows are in the child?" Be ready: "the child cites the earlier arm; your new rows are the cleaner receipt we're adopting for the stateless bar." No falsehood, but answer it plainly.
2. **The omitted first structural run:** "we ran it ... 100/100 ... control acquired" presents only the clean second run. FIVE-WHYS records a first run at 9,658 probes / 0 blocked (lockless stub). Publicly fine if the "runnable cold" probe is the FIXED harness; if he pulls a stale stub, 0/100. Ensure the kit probe is the post-fix, control-arm version before claiming "runnable cold."
3. **"the balance a measured release-window artifact"** is a characterization without a number in the draft. If asked, the balance is 3,042; naming it would preempt the question.
4. "the lock stays — as our own judgment, not the substrate's" is a clean ownership statement and STORM-HARVEST §4 backs it (rename gives whole-file reads, does not order the live list — "shape-(1) remains the honest choice"). Good.

## REGISTER
- Receipt chain: FIVE-WHYS documents both structural runs + the secondary finding; STORM-HARVEST corroborates 100/100 and 3,042 with external citations and supplies the errno source; RUNNER-SANITY-REPORT-\* files exist in the directory. "The probe is in the kit, runnable cold" is defensible ONLY if the shipped probe is the audited/fixed harness (per-arm stub audit; deterministic arm asserts, natural arm observes — FIVE-WHYS "adopted"). [MED — runner report / kit contents not among the five primaries; confirm before posting]
- "we ran it while this reply was being sanity-checked" is consistent with the forensics timeline (the structural runs are dated 2026-11-27, same as this reply). [MED-HIGH]

## NOTES
- CONFIDENCE: number reconciliation = HIGH (each matches a substrate row or a named receipt; 15,724 arithmetic = HIGH). Child-byte verification = HIGH (both fix bullet and envelope carry the structural wording; both old strings absent). Errno sourcing = HIGH. Thread-IQ reads = HIGH. Register completeness = MED (runner report / kit not in primaries). Envelope-receipt phrasing = MED-HIGH.
- VERDICT rule applied: had FINAL-CHILD NOT carried the corrected structural wording in both the fix bullet and the envelope bar, this would flip to HOLD — the reply's central promise would be false on the public thread. It does carry them; verdict stands POST-READY-WITH-NOTES.
- Next mechanism: fold-side — carry the branch at the all-clear (push is the fold's, never the lane's).
