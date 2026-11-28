# SANITY-SOLAR — dual-purpose think-tank check (solar / hy)

## Verdict lines

- WORK: READY-WITH-CORRECTIONS
- INSTRUMENTS (six uses): HOLD — each surfaced a real gap; none alone is fatal at the artifact
  level, but the reply and child must close the gaps before they become committed record.

## Purpose A

### A1. The record vs the reply vs the child
The staged reply (01-THE-REPLY.md) and the child (02-THE-CHILD.md) sit against 05-VERIFICATION.md
(the three-contour battery receipt), 06-MATRIX.md (the MAP matrix + rulers R1-R5), and the partner
comments in 04-PARTNER-COMMENTS.md. The matrix is the spine: every reply row's basis must be
checked against the receipt, and the registry of asks must be audited.

### A2. The 20-row MAP check (matrix row → status → basis)
The reply's MAP matrix carries 20 rows. Each row's basis was checked against 05-VERIFICATION.md,
06-MATRIX.md and the receipts.

| # | Row (claimed) | Status | Basis (file + line) | Check outcome |
|---|---|---|---|---|
| 1 | Fixed read answers both stores | PASS | 05-VERIFICATION.md §receipt pve1; 06-MATRIX.md row 1 | Holds: memory 11 + user 13, twice-read byte-identical, hash unchanged |
| 2 | View sanitized on every contour | PASS | 05/06 row 2 | Holds: BLOCKED marker + blocked index, threat_text_leaked false on all three |
| 3 | Read holds a real lock, both backends | PASS | 05 §receipt structural 50/50; 06 row 3 | Holds: 50/50 inside/outside on all three; live-held probes refused (26/25/10) |
| 4 | Windows/mSvcrt contour verified | PASS | 05 native Win py3.14.7; 06 row 4 | Holds: real msvcrt.locking numbers on real Windows python |
| 5 | Miss path clean and byte-safe | PASS | 05 corrupt-cell; 06 row 5 | Holds: success false, read error, hash unchanged on 3 contours |
| 6 | Dispatch arm reaches the read | PASS | 05 receipt; 06 row 6 | Holds: _memory_tool('read') returns success+payload w/3 entries on all three |
| 7 | THIS session's tool surface exposes no read action | MEASURED, by design | 05 Telegram session; 06 row 7 | Holds: memory tool = operations only; docs + PR #12831 quoted |
| 8 | Installed store is spec-2 shaped (no lock on read) | MEASURED | 05 §receipt item 4; 06 row 8 | Holds: _file_lock only L257/L350; read body L441-455 holds none |
| 9 | Harness writes must be explicit UTF-8 | EARNED | 05 §discovery log item 5; 06 row 9 | Holds: cp1252 default on Win py3.14.7 → lone 0xA7; strict utf-8-sig refused; harness fixed |
| 10 | kvnloo ran macOS/fcntl only | MEASURED | 05 item 6; 06 row 10 | Holds: both comments name py3.15.2 macOS fcntl; no Windows mention |
| 11 | Prediction commit-ready | PASS | 06 row 11; sha 337e87d1…e0e7 embedded | Holds: placeholders 0 |
| 12 | Staged reply answers every named ask | PASS | 06 R2 probe; reply/child 01/02 | Holds: 13/13 named asks present (see A4) |
| 13 | Bundle ships only named seams | PASS | 06 row 13; 05 §receipt item 3 | Holds: memory_tool seam real head + declared out-of-scope registry; registry seam mirrors tools/registry.py:272-275; utils verbatim atoms |
| 14 | Prediction file committed & embedded | PASS | 06 row 11 | Holds: sha embedded; placeholders 0 |
| 15 | Dispatch label is "success" not a message | PASS | 06 row 6 (operator-corrected) | Holds: my first assertion was wrong, corrected; payload contract measured |
| 16 | Structural hook row 3 is the deterministic lock test | PASS | 05 item 4 | Holds: NBLCK on MEMORY.md.lock from second fd; refused 50/50 inside, acquired 50/50 outside |
| 17 | Native Windows coverage runs real artifact | PASS | 05 §receipt native row | Holds: real msvcrt.locking + real read + sanitize on py 3.14.7 |
| 18 | Live-held counts provenance resolved (C1) | PASS | 05 §live-held dual-run provenance | Holds: run1 25/52/5, run2 26/25/10, dry re-run 23; cited by run, never mixed |
| 19 | The box is flat neutral | READY-WITH-CORRECTIONS | register audit A6 | Register plausibly flat-neutral but the reply never names the four bins explicitly |
| 20 | The 14 LPs woven (not forced) | READY-WITH-CORRECTIONS | register audit A6 | Per-LP evidence present but not all 14 traceable to a specific file line in the staged files |

### A3. Partner comments coverage (last two comments each)
- kvnloo 7210367328: spec boundary (row 8), two clean ways (a restore read action + wire surface;
  b keep stateless + answer from frozen snapshot), anchor-read gap 50/50/0 (anchors 11+13 read,
  gap = surface, 0 leaked), doc_stats probe (needs an explicit receipt line), "is a shape missing"
  → REPLIED: the missing shape is the read surface + connector (child's E6); must be stated
  explicitly in the reply.
- kvnloo 7211318206: correction (row 15), re-run rows (rows 1-18 are re-run), spec (1) (stateless
  evidence row 8 + battery stateless claim), structural hook (row 16), unregistered run (named as
  run 2/dry re-run), prediction ask (row 11).
- 3oltan 7192744535: cadence + full-envelope wish (battery + r1-r5), no templates (custom rulers),
  his own occupancy sheet (his own matrix rows), four-step mechanism (classify→probe→evaluate→
  adopt→standardize→verify + ACES loop), debt line (missing read surface, unregistered run
  naming, 14-LP traceability).
- 7213322521: separation (read-kit vs store, receipt item 3), sanitize four-echo-sites asymmetry
  (unstated in reply — fix item), Windows msvcrt contour (row 4), read-invoked (rows 6-7), regular-
  issue filing (register audit A6), narrower first slice (12-cell vs 35-cell — unstated in reply),
  pilot's own instrument (read kit).

### A4. Coverage matrix (A1-A5, B1-B5, C1-C2, D1-D7)
A1→A2/A3/A6/A7 · A2→A2 · A3→A3 · A4→A4 · A5→A6 · B1→A2 · B2→A7 · B3→A8 · B4→A9 · B5→A10 ·
C1→A11 · C2→A10 · D1→A12 · D2→A13 · D3→A3 (row 18) · D4→A6 · D5→A6 · D6→A5/A14 · D7→A10.

### A5. Register / privacy / LP audit
- Register flat neutral: the reply must state the four bins (kept/parked/rejected/new) and that
  no row is over-marked; this is a fix item (D1).
- MAP matrix: 20 rows, all checked in A2; rows 19-20 need the reply to say more.
- 14 LPs: per-LP evidence present, but ~4 of the 14 are not independently traceable to an
  explicit staged file line — the LP list needs a one-line provenance for each (D2).
- Privacy: no over-reveal; receipts contain record's own names/paths, report cites the record.
- The asks are actual questions: every ask in the two last comments is answered with a real
  decision or an honest "not yet / parked" + un-park condition.

### A6. Defects (severity, fix)
- D1 HIGH — reply does not name four register bins → append four-bin summary.
- D2 HIGH — 14-LP provenance not written per-LP → add LP table with file+line.
- D3 MEDIUM — anchor-read gap 50/50/0 not stated as distinct claim → state anchors 11+13, gap =
  surface, 0 leaked.
- D4 MEDIUM — doc_stats probe no explicit receipt line → add it.
- D5 MEDIUM — unregistered run not named → name run 2/dry re-run.
- D6 MEDIUM — four-echo-sites sanitize asymmetry unstated → state which site sanitizes, the leak
  check.
- D7 MEDIUM — narrow-first-slice unstated → state 12-cell vs 35-cell.
- D8 LOW — eigen keeper axis drift un-named → name invariant axes.
- D9 LOW — K-recency probe demand un-stated → state the long-session transcript demand.

### A7. Bookkeeper (affected-set) — used on the reply's own claims
The reply's named claims are complete for the partner points, but the child edits E1-E5 + E6 are
NOT listed as affected items, and the unregistered run is not a named item; the hold-back and
team-up are not in the set. What the reply misses: (1) child edits in the affected set; (2) the
unregistered run as its own item; (3) the hold-back statement and the smallest-diff thesis.

### A8. Eigen keeper (invariant axes) — used on the reply's pins
Invariant axes: read fix (store a43818a6…1586a), spec-2 vs spec-1 (do not conflate), gate 50/50/0,
child's commitments (team-up, hold-back, smallest-diff).
The axis that drifts: the dispatch-label claim (row 15) — the correction itself is not carried
into the reply; rows 19-20 (flat neutral, 14 LPs) are asserted rather than shown.

### A9. Two-N window / retention latch / tiny-aged-fact — lenses on compaction
- Two-N window: claim survives if stated as two windows (50+50) with 0 leaked; reply does not
  state the windows explicitly.
- Retention latch: claim survives if latch is release-on-completion; reply does not state it.
- Tiny-aged-fact axis: claim survives if hash before/after + sha256 id given; reply gives only
  the unchanged status.

### A10. Read kit — used as test case (receipt/code/README)
The kit (readkit-bundle + hybrid_battery.py + store sha a43818a6…1586a) claims three contours
green, sanitized, stateless, real msvcrt/fcntl lock. Outsider: can run the one-command test-by-
reading (A12) and sha256sum on the store. Could not: full 35-cell suite (parked), WSL2 native
contour (no Windows host), full battery byte-for-byte (bundle is read-relevant import surface).
Kit's own claims not shown: four-echo-sites asymmetry, narrow first slice; read-invoked claim
lives only in the receipt.

### A11. K-recency probe — used on the gate claim
The probe's protocol demands (1) a 24h corpus, (2) the record (not the reply) prove the gate
(row 3/16 cite the receipt), (3) a successful long-session transcript to un-park the
K-recency ground. The reply does not state the demand.

### A12. One-command test-by-reading
`python3 hybrid_battery.py <bundle>` (bundle = readkit-bundle/) then
`sha256sum <bundle>/tools/memory_tool_store.py` → a43818a6…1586a. Runner: outsider.

### A13. Candidates' status
- Long-session recurrence ground: PARKED (needs transcript in dumps).
- 35-cell suite port: PARKED (needs contour table → entire battery).
- Gateway read wiring: PARKED (needs child to land).
- E6: STAGED (waits the word).

### A14. Child's own commitments kept
Team-up (read kit + battery) kept; hold-back (E6 not answered yet) kept; smallest-diff thesis
(E1-E5 are the smallest diff) kept; eigen keeper framed as special-use-case instrument (A15).

### A15. Eigen keeper framed as special-use-case instrument
Framed as a pin-discipline ruler for version invariance, not a general ledger — kept in the
report.

### A16. Read kit linked
Linked via bundle name, battery, store sha, and the reproducibility section of 05-VERIFICATION.md.

## Purpose B

### B1. Instruments-used table
| Instrument | How used | What surfaced | What failed / missing | Outsider-usable? |
|---|---|---|---|---|
| MAP matrix (xngg) | Spine of claim check; every row's basis checked | Rows 1-18 grounded; rows 19-20 asserted | Rows 19-20 need explicit statement | Yes |
| Bookkeeper | Applied to reply's claims: backlog, partner points, child edits, run | Partner points complete; child edits + run not listed | Missing child edits, run item, hold-back | Yes |
| Eigen keeper | Applied to pins: read fix, spec, gate, commitments | Axes mostly held; dispatch-label drift + asserted rows 19-20 | Correction note not carried; basis of 19-20 not shown | Yes |
| Two-N window | Lens on 50/50/0 | Survives if stated as two windows w/ 0 leaked | Windows not stated explicitly | Yes |
| Retention latch | Lens on lock claim | Survives if release-on-completion | Not stated | Yes |
| Tiny-aged-fact axis | Lens on hash claim | Survives if hash pair + sha256 given | Only unchanged status given | Yes |
| Read kit | Test case | Claims held; receipt shows numbers | Full suite, byte-for-byte battery not staged | Yes (A12) |
| K-recency probe | On gate claim | Demands long-session transcript | Demand not stated | Yes |

### B2. One-command test-by-reading
`python3 hybrid_battery.py <bundle>` then `sha256sum <bundle>/tools/memory_tool_store.py` →
a43818a6…1586a.

### B3. Candidates' status
PARKED: long-session recurrence ground, 35-cell suite port, gateway read wiring · STAGED: E6.

## What would change the verdict
- WORK: reply adds the four register bins, LP provenance table, anchor gap 50/50/0, doc_stats
  receipt line, run name, four-echo-sites asymmetry, narrow-first-slice → READY.
- INSTRUMENTS: reply adds the two-N windows, latch release-on-completion, hash pair, correction
  note, four-echo-sites asymmetry → HOLD→READY.

## The lane's own limits
- From the kit, the lane could not execute the WSL2 or native Windows command (no Windows host /
  WSL2 in the sandbox); the WSL2/native numbers are cited from the record (05-VERIFICATION.md),
  not re-run.
- The full 35-cell battery was not ported byte-for-byte (bundle = read-relevant import surface).
- The reply's "is a shape missing" answer and E6 closure were not in the staged reply (child
  commitments).
- The L2 audit (seven independent passes) was not re-run by this lane.
