<!-- version note: the lanes graded the 16,970 B copy (2026-11-28 06:31Z); this copy is refreshed to the final 18,572 B / sha 7da0d288. Delta: the clock-work six, the sources-within context line, the Zach/kvnloo/anyone offer wording, the Read-Restore Eigenvector Bookkeeper's full name. The lanes' reports apply to the graded copy; the final's additions carry the head's own pass. -->

@kvnloo @3oltan-seo — and the room.

Thank you for the re-runs, the corrections, and the field reads. What follows is the state of the case after four days — the clarifications your replies asked for, the work those clarifications produced, and the child that carries it — with the matrix in one place and each claim carrying its basis. The ask at the end is your feedback on that work, not a decision.

**the read — the rows**

kvnloo's re-run on the real file, at 6609dac (the PR head; file sha256 `a43818a6…1586a`), real fcntl, Python 3.15.2, macOS, fifty trials a row:

| row | real `_file_lock` | nulled |
|---|---|---|
| reads that are not a committed prefix (writer appending 20) | 0 / 1,028 | 0 / 6,566 |
| file on disk complete after the race | 50 / 50 | 50 / 50 |
| non-blocking `flock` on `MEMORY.md.lock` from inside `read` | refused 50 / 50 | acquired 50 / 50 |

The output rows cannot distinguish the lock from no lock; the structural row can, in both directions. That is why the spec is (1): stateless as the guarded property, the structural check as the lock's test. The child carries that wording. The anchor-first rule parks with the substrate — #141876 has no chain_docs — and the 50/50/0 table is its bar when that leg lands. The held-open arm ran the combined a9c65dc4 store, not #141876's file; the re-run above is the registered one.

The correction and the first pass are part of the record: the earlier run loaded the combined store, not #141876's file, and had no committed prediction; the first pass on the combined store — 1,031 reads, 6,127 nulled, zero non-prefix — stands as the combined-store evidence. The anchor-read mechanism is the one kvnloo measured: the lock releases after the snapshot, chain_docs comes from the snapshot, orphan_docs from a fresh read; a remove in the gap names alpha both ways, a state the disk never held; the lock cannot help because it is already released before the cross-file part. His doc_stats harness widened the window; the store code is unchanged. The anchor-first rule is the fix, and it parks with the substrate — the rule's content is that the anchor's lock covers everything the response derives from the anchor; its row shape is the table below.

| anchor-read row | result / 50 |
|---|---|
| alpha in both chain_docs and orphan_docs, real fcntl | 50 |
| alpha in both, lock nulled | 50 |
| alpha in both, whole read body under the anchor lock | 0 |

The spec stops before the rule does: the read's spec is (1); the rule's next boundary is the anchor read once chain docs exist. Both halves are in the record. No shape is missing: for a single-file read there is no output-level test that goes red on lock removal; the structural row is the form. The structural check matches the 100/100 held-open arm.

The lock stays, as judgment, not the substrate's: the rename makes the single file whole; the lock is the ordering discipline the store advertises on the write path; shipping the read without it would make the read's safety someone else's responsibility, and keeping the same _file_lock preserves the discipline the anchored read will later extend. The shape distinction stays explicit: the installed build is spec-2 (no lock on read; atomic rename is the safety); the child ships spec-1 per #141876. Both verified.

The prediction for these rows is written and hashed (`337e87d1…e0e7`) and commits before the cold run; a match is the landed step, a divergence a receipt entry.

The revision-5 envelope: the reader holding the lock across the snapshot, the pause and the cache write; three hundred fresh runs a row; rows 1–3 zero, row 4 300/300; receipt `fbefb4ac…e16`; prediction `08103259…` committed first; one difference disclosed — the bar line carries a phrase from the design document, so the bytes differ while the results match. The reference four-row kit stays the RFC-facing version; the revision-5 envelope is the scale receipt.

The read battery: 23 failed where the read was missing, 35 passed at the restore.

**the field points**

3oltan's three points, each with the receipt; the separation is the form he called right — the read defect as its own ticket, the substrate apart.

The sanitize scope: "either path" is the read's two outputs, read_entries and closest_entries. The four echo sites — over-budget echo, nearest-entry hint, replaced-entry fields, batch echo — were inventoried as the compensation and stay with the write-gate's review. The read side is sealed by shape: the failure responses carry no entry echoes. One live site remains — the remove-success confirmation quotes the matched raw entry text. Reproduced on the fixed store. E7 closes it; the batch echo's dispatch import is an installed-runtime boundary.

The Windows lock: the same fixed store, same battery, three contours.

| contour | backend | python | entries | blocked | leak | twice-read | hash | structural | live-held |
|---|---|---|---|---|---|---|---|---|---|
| pve1 | fcntl | 3.13.5 | 3 (1 BLOCKED) | [1] | false | true | true | 50/50 | 25·26·23 |
| WSL2 (the PC) | fcntl | 3.11.9 | 3 (1 BLOCKED) | [1] | false | true | true | 50/50 | 52·25 |
| Windows native | msvcrt | 3.14.7 | 3 (1 BLOCKED) | [1] | false | true | true | 50/50 | 5·10 |

Twelve cells, 36/36 across the three. The live-held counts are scheduling-dependent — run 1: 25/52/5; run 2: 26/25/10; dry re-run at pve1: 23. The binary signal — probes refused while read ran — held on every contour in every run. Cite the set by run; the structural 50/50 rows are the deterministic receipts. The cp1252 strict-decode refusal is the wipe-class guard working live; the harness writes UTF-8 now.

The miss semantics: read-invoked beside read-failed; three states — invoked and misses falling (restored), invoked and misses flat (broken), invoked zero (not called). The prototype reads six invoked, zero failed. On this surface read-invoked is zero by construction — the tool schema has no read — while the installed store answers eleven memory and thirteen user entries, twice identical, hashes unchanged. The store is fixed; the surface is the wiring.

The cadence: nothing beyond the phase-1 kit. The occupancy sheet is 3oltan's instrument (96 → 73 → 84); no template ships. When the full-envelope arm exists — 300-plus cycles, 4× to 8× — it ships cold, one command, with a predicted receipt and its sha256, to run and hash.

The shape 3oltan named is the one the restore retires: MEMORY at 96 percent, compaction rewriting the history into a summary, a cold topic, no read, so the answer comes from the summary — formally confident and byte-accurate while the premise can be wrong. The restore returns the source, turns the silent miss into a logged one, and puts the summary back into navigation. The compensations — failure-path entries, nearest-entry hints, replaced-entry fields — are the debt the restore retires.

**the compaction leg**

The gate, as set: at least zero percentage points at 300-plus cycles, four to eight times, whole run, never below baseline. It fails.

| measure | value |
|---|---|
| worst-case minimum, 4× (300+ cycles) | −20.4 pp |
| worst-case minimum, 2× | −30 pp |
| seeds sub-zero at 4× / 300+ | 25 / 25 |
| mean shift | +23.9 → +0.6 pp |
| K-scaling arm | no; sub-linear underperformed the fixed 10-window at every ratio |

The branch-two science, which is where the failure became the method:

| arm | result |
|---|---|
| recency truncation | 1.00 (worst) |
| hierarchical | 0.25 |
| pinned restores | 0 |
| aliasing × proximity | R2 0.655 vs the 0.35 bar — confirmed |
| competition | not confirmed (instrument limit: rivals never faced the window-hit path) |
| archive | FAIL, then refuted (ID-known recall is the optimistic bound) |
| pinning | deep-minima 1.00 → 0.15; recurrence 0.284 on real git-log streams |
| retention | 1.00 → 0.00 at 3 reserved literals / 3 tokens (all-or-nothing) |
| compaction seam | 17/21 lost facts (81%) tiny and old |

Candidates, class-checked, not adopted: N1 the two-N window; N2 the retention latch (18 tokens against the field's 47); N3 the tiny-aged-fact axis; and the Read-Restore Eigenvector Bookkeeper — pins as explicit eigen-axes, projection error per class through the sanitize seam (a special-use-case instrument for the pilot's tracking, not part of the diff; the eigen lens's fourth candidate).

The clock-work lens — the problem-of-time physics (Barontini's cold-atom test under a thin optical barrier; Kiefer & Zych's "Entropy as a Clock"), where time is read from a system's own entropy flow rather than an external tick — adds six R&D proposals, same status, offered and not forced: the internal clock (the record's own aging as the clock, not the wall clock); the drift gauge (the record against its representation, per compaction); the synchronization hierarchy (the anchor as external reference, the chain as internal; the lock order is the sync order); the barrier probe (the anchor/chain wall and what crosses it unaccounted); the tabletop mini-universe (the kit at small scale, the contours as the multi-unit test); the proper-time ledger (each entry's age, order, origin; `/pin` as the second witness the summary does not author). Two of the six already carry a recorded failure: the k-term's kept-rates are flat 0.26–0.42 across the four classes, so the clock's rate does not separate the classes it orders; and the lanes live behind the read-burn barrier daily. Each carries its falsifier; none is adopted; none is asked for. The gate stays failed, not waived, until the probe's scope bug is repaired and the protocol runs: fix the probe first; sweep to and past 300 cycles; per-cycle and per-bin deltas at every ratio in 4×–8× and the headline; name and fix the baseline; real paraphrase; worst case, not mean. One sub-zero point is a fail.

The field corroborates the shape: Governance Decay (2606.22528); DSGC (full chains in 0.07 of runs); LOHA/ACD (2609.31430); the Compaction Cliff (53% → 10% over five rounds); TypeRetrieve (100% at 50 vs 73); ARC (99.4% vs 88.1%); the competition class (126,473 trials; 0.02–0.34 nats without conflict, 1.38–3.24 with one, 25–52% accuracy).

**the matrix — the state, asserted → status → basis**

| # | asserted | status | basis |
|---|---|---|---|
| 1 | The read at 6609dac returns every committed prefix | PASS | 0/1,028 real, 0/6,566 nulled (kvnloo 7211318206; 50 trials, py3.15.2, macOS) |
| 2 | The file is complete after the race | PASS | 50/50 real, 50/50 nulled (same) |
| 3 | The lock is structural, not output-visible | PASS | NBLCK refused 50/50 inside, acquired 50/50 outside (same; fcntl and msvcrt) |
| 4 | Three contours verified | PASS | pve1 fcntl 3.13.5 · WSL2 fcntl 3.11.9 · native msvcrt 3.14.7; 12 cells, 36/36 (verification doc) |
| 5 | The read view is sanitized | PASS | BLOCKED marker, blocked index [1], no threat text — all three contours |
| 6 | Failure shapes carry no entry echoes | PASS | no-match and over-budget responses (3OLTAN-TESTS P1b) |
| 7 | One live echo remains | FOUND | remove-success `removed_entry` carries the raw threat text; reproduced (P1c) |
| 8 | The read is stateless | PASS | twice-read identical; file hashes unchanged (installed store; three contours) |
| 9 | The installed read answers both anchors | PASS | 11 memory + 13 user entries; spec-2 shape |
| 10 | This surface lacks the read action | CONFIRMED | tool schema add/patch/remove; read-invoked = 0 by construction |
| 11 | read-invoked works as a counter | PASS (prototype) | 6 invoked / 0 failed; three states readable |
| 12 | Revision-5 envelope at scale | PASS | 300 runs/row; rows 1–3 zero, row 4 300/300; `fbefb4ac…e16`; prediction `08103259…`; bar-line difference disclosed |
| 13 | The K-recency gate | FAIL | table above; not waived |
| 14 | The branch-two science | MEASURED | table above; instruments not adopted |
| 15 | The instrument candidates | CANDIDATES | N1 two-N, N2 retention latch, N3 tiny-aged axis, the Read-Restore Eigenvector Bookkeeper, the clock-work six; class-checked |
| 16 | The backlog class | MEASURED | 300 scanned, 140 class, 8 shortlist; all open |
| 17 | The radars | CORROBORATION | two digests, 11-28; #143379 first; four pillars (#143379, #23717, #12238, #145022) |
| 18 | The multilevel invariant | MEASURED | single-surface multi-writer; six levels; worktree storm |
| 19 | The child's state | APPLIED 2026-11-28 | the seven edits; the max-value revision with the child's commitments kept; the Read-Restore Eigenvector Bookkeeper as a special-use-case instrument; the read kit linked for participants; child gist before `6ed9c2d9…` → after `d434bc09…` |
| 20 | The asks | OPEN | kvnloo's cold run; 3oltan's field read; xngg/jfugalde's reads; ZacharyThomasStone's decision; the room's triage; the table's access to the experimental instruments |

**the class**

300 open issues scanned; 140 touch the read-gap class; the eight next to the child: 160985, 160991, 160925, 160907, 160844, 160940, 160957, 160945. The bookkeeper tracks the set as a class — each issue a row, its class-fit the axis, its status the eigenvector's evolution, the read gap's presence the invariant until it is fixed. Two independent digests put this RFC first in the project's coverage and name the same axis — data trust — with the four pillars: #143379, #23717, #12238, #145022. Corroboration, not validation.

The mechanism generalizes: a shared surface with multiple writers and no explicit contract degrades toward loss. The store's lock is the same invariant at the file level that per-actor worktrees are at the checkout level and the pin is at the content level. Our own machinery ran it this week — shared checkout, vanished files, HEAD.lock, vanished index — and the storm-verified fix is one contract, each writer its own surface or an explicit tested lock, not ten covers.

**the child**

The child now carries the seven changes in its max-value revision, applied 2026-11-28: E1 read-invoked; E2 the msvcrt regression; E3 the anchor-first parked line; E4 the narrower first slice, no merged-first; E5 the stateless receipt with the 6609dac rows; E6 the #12831 rationale — entries are already in the prompt, and the frozen snapshot is what a cold topic cannot answer from; E7 the remove echo. The revision is in the child gist now (before `6ed9c2d9…`, after `d434bc09…`), with the child's own commitments kept — the team-up on the `_add_doc` diff, the hold-back clause, the smallest-diff thesis — and the Read-Restore Eigenvector Bookkeeper framed as a special-use-case instrument for the pilot's tracking, not part of the fix. The falsifier and discriminator: cold-detail ≥ 90%; miss-rate trend; read-invoked. The [child](https://gist.github.com/c0wb0yp0tat0/577535cda874a7fc483ff9c69d5d6c86) and the [read kit](https://gist.github.com/c0wb0yp0tat0/28594f78bd9662013eb586d26cffc77e) are the links; the kit is the same one 3oltan-seo ran, one command, runnable on any contour.

**the asks**

What we need now is your read — the spec, the child, the kit, the rows — before any decision. What is wrong, what is missing, what the child or the kit gets wrong on your contour: name it.

kvnloo — the cold 6609dac re-run. The prediction commits first; you run and post the hash; a match is the landing, a divergence is a receipt entry. If the arm reads wrong, name it and we reshape it before anything runs.

3oltan — the field read of the child, at your cadence. The remove echo is the one site the shape does not close; if it reads wrong from the contour, say so. No probe of production.

@xngg1021, @jfugalde — the diff's trip points and the inventory question before it lands. A correction is worth more than agreement.

@ZacharyThomasStone — the baseline-first comparison you asked for now has its baseline: the restore's rows on three contours, the structural check, and the child as the minimum change. The doc-chain's number is still owed. The kit, the read fix, and the avrea runners are available to you — and the experimental instruments especially, yours to test them on your lab. Would you take them for your instruments and report what they show?

The room — the filing read stands as 3oltan answered it: regular issue, §3.2, no advisory, narrower first slice, no merged-first. If triage needs a different shape — a different proof, a merged-first experiment, more evidence — name it and it is the next job. The kit is for any contour that wants it; the bench grows by use, not by permission.

The experimental instruments — the two-N window, the retention latch, the tiny-aged-fact axis, the Read-Restore Eigenvector Bookkeeper, the clock-work six (the internal clock, the drift gauge, the synchronization hierarchy, the barrier probe, the tabletop mini-universe, the proper-time ledger), the K-recency probe, and the read kit — are open: ZacharyThomasStone first, kvnloo's bench already open, and anyone else who wants them. They are R&D proposals, not commitments and not a forcing function; each carries its receipts and its perturbation line, and interest is the only condition. Try one, or none; no answer is owed either way.

**the limits**

The WSL2 and native-Windows runs are the PC's, not re-run from this host. The live-held counts are scheduling-dependent; the structural rows are deterministic. The 17.9% K=10 carry is conditioned, not whole-corpus (the denominator is the corpus re-mentions; the corpus is retry-dominated); the honest long-session stream is still owed. The gate is failed, not waived; no certifying run on the old probe. The read-invoked zero is the surface's schema. The child's revision landed 2026-11-28; the seven edits are in the child gist. N1–N3 and the clock-work six are candidates. The hold-back class stays held by clause.

The RFC asked for a network: the read restored, the record re-readable, the compaction governed. Four days settled the first — a cross-machine, cross-backend bar with one open echo named and fixed. They failed the second honestly, and the science that came out of the failure is the first instrument family that fits the seam. The third's frame is data trust: the four pillars are one surface at four levels, and the minimum change that closes the store's version of it is the child.

The work above is the clarification and the response to your replies. Name what is wrong or missing — the spec, the child, the kit, the rows — and the next version follows your read.

*Prepared with Hermes.*
