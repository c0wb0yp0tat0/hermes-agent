# SANITY-SOLAR — dual-purpose think-tank check (solar / hy)

## Verdict lines

- WORK: READY-WITH-CORRECTIONS
- INSTRUMENTS (six uses): HOLD — each surfaced a real gap; none alone is fatal at the artifact
  level, but the reply and child must close the gaps before they become committed record.

---

## Purpose A — the work

### A1. The record vs the reply vs the child

The staged reply (`01-THE-REPLY.md`) and the child (`02-THE-CHILD.md`) sit against `05-VERIFICATION.md`
(the three-contour battery receipt), `06-MATRIX.md` (the MAP matrix + rulers R1-R5), and the partner
comments in `04-PARTNER-COMMENTS.md`. The matrix is the spine: every reply row's basis must be
checked against the receipt, and the registry of asks must be audited.

### A2. The 20-row MAP check (matrix row → status → basis)

The reply's MAP matrix carries 20 rows. Each row's basis was checked against `05-VERIFICATION.md`,
`06-MATRIX.md` and the receipts. Results below.

| # | Row (claimed) | Status | Basis (file + line/section) | Check outcome |
|---|---|---|---|---|
| 1 | Fixed read answers both stores on our layer | PASS | 05-VERIFICATION.md §receipt pve1; `06-MATRIX.md` row 1 | Basis holds: pve1 shows memory 11 + user 13, twice-read byte-identical, hash unchanged |
| 2 | View sanitized on every contour | PASS | 05-VERIFICATION.md pve1/WSL2/native; `06-MATRIX.md` row 2 | Basis holds: BLOCKED marker + blocked index, threat_text_leaked false on all three |
| 3 | Read holds a real lock, both backends | PASS | 05-VERIFICATION.md structural 50/50; `06-MATRIX.md` row 3 | Basis holds: structural 50/50 inside/outside on all three; live-held probes refused (26/25/10 sets) |
| 4 | Windows/mSvcrt contour verified, not assumed | PASS | 05-VERIFICATION.md native Win py3.14.7 msvcrt; `06-MATRIX.md` row 4 | Basis holds: true msvcrt.locking numbers from real Windows python |
| 5 | Miss path clean and byte-safe | PASS | 05-VERIFICATION.md corrupt-file cell; `06-MATRIX.md` row 5 | Basis holds: success false, read error, file hash unchanged on 3 contours |
| 6 | Dispatch arm reaches the read | PASS | 05-VERIFICATION.md §receipt; `06-MATRIX.md` row 6 | Basis holds: `_memory_tool('read',…)` returns (success, payload w/3 entries) on all three |
| 7 | THIS session's tool surface exposes no read action | MEASURED, by design | 05-VERIFICATION.md Telegram session; `06-MATRIX.md` row 7 | Basis holds: memory tool = operations only; docs + PR #12831 quoted |
| 8 | Installed store is spec-2 shaped (no lock on read) | MEASURED | 05-VERIFICATION.md §receipt item 4; `06-MATRIX.md` row 8 | Basis holds: `_file_lock` only L257/L350; read body L441-455 holds none |
| 9 | Harness writes must be explicit UTF-8 | EARNED | 05-VERIFICATION.md §discovery log item 5; `06-MATRIX.md` row 9 | Basis holds: cp1252 default on Win py3.14.7 → lone 0xA7; strict utf-8-sig read refused; harness fixed |
| 10 | kvnloo ran macOS/fcntl only | MEASURED | 05-VERIFICATION.md item 6; `06-MATRIX.md` row 10 | Basis holds: both comments name py3.15.2 macOS fcntl; no Windows mention |
| 11 | Prediction commit-ready | PASS | 06-MATRIX.md row 11; sha 337e87d1…e0e7 embedded | Basis holds: placeholders 0 |
| 12 | Staged reply answers every named ask | PASS | R2 probe `06-MATRIX.md`; reply/child `01`/`02` | Basis holds: R2 probe 13/13 named asks present (see A4) |
| 13 | Bundle ships only named seams | PASS | `06-MATRIX.md` row 13; 05-VERIFICATION.md §receipt item 3 | Basis holds: memory_tool seam real head + declared out-of-scope registry; registry seam mirrors tools/registry.py:272-275; utils verbatim atoms |
| 14 | Prediction file committed & embedded | PASS | 06-MATRIX.md row 11 | Basis holds: sha embedded; placeholders 0 |
| 15 | Dispatch label is "success" not a message | PASS | 06-MATRIX.md row 6 (operator-corrected) | Basis holds: my first assertion was wrong, corrected; payload contract measured |
| 16 | Structural hook row 3 is the deterministic lock test | PASS | 05-VERIFICATION.md item 4 | Basis holds: NBLCK on MEMORY.md.lock from a second fd; refused 50/50 inside, acquired 50/50 outside |
| 17 | Native Windows coverage runs real artifact | PASS | 05-VERIFICATION.md §receipt native row | Basis holds: real msvcrt.locking + real read + sanitize on py 3.14.7 |
| 18 | Live-held counts provenance resolved (C1) | PASS | 05-VERIFICATION.md §live-held dual-run provenance | Basis holds: run 1 25/52/5, run 2 26/25/10, dry re-run 23; cited by run, never mixed |
| 19 | The box is flat neutral | READY-WITH-CORRECTIONS | register audit A6 | The register is plausibly flat-neutral, but the reply never names the neutral bins explicitly; needs the four bins named |
| 20 | The 14 LPs woven (not forced) | READY-WITH-CORRECTIONS | register audit A6 | Per-LP evidence present but not all 14 are independently traceable to a specific file line in the staged files |

Rows 1-18 of the matrix are sound. Rows 19-20 are the only two that require the reply to say more
explicitly than the staged files currently do.

### A3. Partner comments coverage (last two comments each)

**kvnloo 7210367328** — the reply must cover:
- spec boundary: covered by row 8 (spec-2 measured) and by the reply's spec (1) decision; needs an
  explicit statement of the boundary (what the read fix does NOT change).
- the two clean ways: covered via the two clean ways (a) restore read action and wire surface, (b)
  keep stateless and answer from the frozen snapshot; explicitly named.
- the anchor-read gap 50/50/0: two anchors (11 + 13 entries) read; the reply must say the gap is the
  surface, not the store; the 0 = nothing leaked in the view.
- doc_stats probe: covered via the doc_stats probe point; needs an explicit receipt line for it.
- final "is a shape missing" question: REPLIED — a shape is missing: the read surface + the
  connector, and that is the child's ask (E6). The reply must say this explicitly.

**kvnloo 7211318206** — the reply must cover:
- the correction: the correction (dispatch label "success" not a message; my first assertion was
  wrong) is covered in row 15.
- the re-run rows: rows 1-18 are re-run rows; the reply should say which rows are re-run and which
  are new.
- spec (1): covered by the statelesness evidence (row 8) and the stateless claim row 3 of the
  battery; needs an explicit "spec (1)" statement.
- the structural hook: covered by row 16.
- the unregistered run: the run is registered as run 2 / the dry re-run; the reply must say which
  run the row cites.
- the prediction ask: covered by row 11 (sha embedded, placeholders 0).

**3oltan 7192744535** — the reply must cover:
- his cadence (the read-battery cadence) and full-envelope wish: covered via the battery and the
  r1-r5 rulers; the wish is unmet only for rows 19-20 below.
- no templates: the reply should state no template was used; the audit used the custom rulers.
- his own occupancy sheet: covered via his own rows in the matrix.
- the four-step mechanism: covered by the spine (classify→probe→evaluate→adopt→standardize→verify
  + ACES loop).
- the debt line: the reply must name the debt — the missing read surface, the unregistered run
  naming, the 14-LP traceability — and what the child must pay down.

**7213322521** — the reply must cover:
- the separation: covered by the read-kit vs store separation (receipt item 3).
- the sanitize four-echo-sites asymmetry: the reply must state the asymmetry explicitly (which
  four sites, which one runs the sanitizer, which one leaks).
- the Windows msvcrt contour: covered by row 4.
- read-invoked: covered by row 6 (dispatch arm) and row 7 (no read in this session).
- the regular-issue filing: covered by the register audit A6.
- the narrower first slice: the reply must state the narrower slice explicitly (the field points
  name 12 cells; the battery covers 12 cells; the full 35-cell suite is parked).
- the pilot's own instrument: the pilot's instrument is the read kit; the reply must name it as
  such.

### A4. Coverage matrix (A1-A5, B1-B5, C1-C2, D1-D7 → where covered)

| Ruler | Item | Covered where |
|---|---|---|
| A1 | The reply checked against the record | A2, A3, A6, A7 |
| A2 | The 20-row matrix basis check | A2 |
| A3 | Every point of each partner's last two comments | A3 |
| A4 | Coverage matrix entries stated | A4 |
| A5 | Register audit | A6 |
| B1 | MAP matrix used as spine | A2 |
| B2 | Bookkeeper on the reply's own claims | A7 (below) |
| B3 | Eigen keeper on the reply's pins | A8 (below) |
| B4 | Two-N window / retention latch / tiny-aged-fact axis on compaction | A9 (below) |
| B5 | Read kit used as test case | A10 (below) |
| C1 | K-recency probe used on the gate claim | A11 (below) |
| C2 | Kit's own claims under the sanity lenses | A10 |
| D1 | One-command test-by-reading | A12 (below) |
| D2 | Candidates' status | A13 (below) |
| D3 | Run provenance (C1) | A3 row 18 |
| D4 | The 14 LPs woven | A6 |
| D5 | No verbatim borrowings | A6 |
| D6 | Child's own commitments kept | A5, A14 |
| D7 | Read kit linked | A10 |

### A5. Register / privacy / LP audit

- Register flat neutral: the register should be a flat neutral table (no over-marking, no
  over-revealing). The reply state the four bins explicitly (kept / parked / rejected / new) and
  that no row is over-marked.
- MAP matrix: 20 rows, all present and all checked in A2; the only rows that need the reply to say
  more are 19 and 20.
- 14 LPs: per-LP evidence is present in the file, but 4 LPs (out of the 14 woven) are not traceable
  to an explicit line in the staged file — the LP list must be written out with a one-line
  provenance for each. Not fatal; the reply/child must add the trace.
- Privacy: no over-reveal. The receipts contain real usernames and path names; that is the
  record's own data, and the report cites the record, not a third party. No personally
  identifying data beyond the record's own names is introduced.
- The asks are actual questions: every ask in the two last comments is answered with a real
  decision or an honest "not yet / parked" + the un-park condition. None is replaced with a
  assertion.

### A6. Defects (with severity and fix)

| # | Severity | Defect | Fix |
|---|---|---|---|
| D1 | HIGH | The reply does not name the four register bins explicitly (keep/park/reject/new) | Append the four-bin register summary; state flatness with a line |
| D2 | HIGH | The 14-LP provenance is not written out per-LP | Add an LP table with file+line provenance for all 14 |
| D3 | MEDIUM | The anchor-read gap 50/50/0 is not stated as a distinct claim | State it as a distinct claim in the reply: anchors 11+13 read, gap = surface, 0 leaked |
| D4 | MEDIUM | doc_stats probe has no explicit receipt line in the reply | Add the doc_stats probe receipt line |
| D5 | MEDIUM | The unregistered run is not named as a run | Name the run (run 2 / dry re-run) explicitly in the reply |
| D6 | MEDIUM | The four-echo-sites sanitize asymmetry is not stated | State which site sanitizes, which three echo, and the leak check |
| D7 | MEDIUM | The narrow-first-slice claim is not stated | State the 12-cell slice vs the 35-cell suite |
| D8 | LOW | The eigen keeper's axis that drifts (read fix) is not named | Name the invariant axes: read stateless, spec-2 vs spec-1, gate, child commitments |
| D9 | LOW | The K-recency probe's demand on the gate claim is not stated | State what the probe demands (a successful long-session transcript) |

### A7. The bookkeeper (affected-set instrument) — used on the reply's own claims

Applied to the reply's own claims: the backlog shortlist, the partner points, the child edits E1-E6
plus E6.

- The affected set the reply names is complete for the partner points (both kvnloo comments, both
  3oltan points, all of 7213322521's points) — but the reply does NOT explicitly list the *child
  edits* E1-E5 + E6 as an affected set item, and does not name the unregistered run as a separate
  affected item.
- What the reply misses: (1) the child edits E1-E5 + E6 are not listed as an affected set; (2) the
  unregistered run is not named as its own item; (3) the reply does not say what the child must
  not touch (the hold-back) or what the child must keep (the team-up, the smallest-diff thesis).
- Verdict: the reply's own claims are checked, but the bookkeeper shows the child's edits are not
  in the affected set; the reply must carry them into the register.

### A8. The eigen keeper (invariant axes) — used on the reply's pins/claims

Axes that must stay invariant across the reply's versions:
1. The read fix — the fixed store a43818a6…1586a is the reference; the reply does not drift it.
2. The spec — spec-2 (no lock on read) is the measured fact for the installed store; spec-1 is the
   child's shape; the reply must not conflate them.
3. The gate — the gate claim is that the read is gated by a real lock; the reply must keep the
   50/50/0 shape (inside blocked, outside acquired, zero leaked).
4. The child's commitments — the team-up, the hold-back, the smallest-diff thesis, the eigen
   keeper as a special-use-case instrument.

The axis that drifts: the dispatch label claim. The reply's row 15 states the label is "success",
not a message; this is a correction within the reply, and it is correct, but the comment on the
correction itself is not present (the operator's note that the first assertion was wrong is not
carried into the reply). Failing to carry the correction note into the reply would be the drift.
Also, the reply's pinning rows 19-20 (flat neutral, 14 LPs woven) are asserted rather than shown;
that is the drift on the eigen keeper: the reply pins the register as flat neutral, but the basis
is not shown.

### A9. The two-N window, the retention latch, the tiny-aged-fact axis — used as lenses on the
compaction claims

- Two-N window: the reply claims the 50/50/0 hold; the lens demands the reply state the N and the
  second N — e.g., first 50 probes, second 50 probes, 0 leaked — and that the probes were refused
  while read ran. The reply does not state the two windows explicitly; this is a fix item.
- Retention latch: the claim that the lock is held and released on read() must state the latch as
  release-on-completion, not hold-open. The reply does not say release-on-completion; this is a
  fix item.
- Tiny-aged-fact axis: the reply claims the file hash is unchanged across reads; the lens demands
  the hash before/after pair + the sha256 id; the reply does not give the hash value, only the
  unchanged status. This is a minor fix item.

### A10. The read kit — used as the test case under the sanity lenses

The kit (the `readkit-bundle/` + `hybrid_battery.py` + store sha a43818a6…1586a) claims: three
contours green, sanitized, stateless, real lock on msvcrt and fcntl, Windows verified not assumed.

- What an outsider could run: the one-command test-by-reading (`python3
  hybrid_battery.py <bundle>`), plus `sha256sum` on the store — §A12.
- What an outsider could NOT run from the kit as staged: (1) the full 35-cell suite (parked);
  (2) the WSL2 native contour without the Windows host path; (3) the full battery byte-for-byte
  (only the read-relevant import surface is bundled).
- What the kit's own claims do not show: the four-echo-sites asymmetry details, the narrow
  first slice claim, and the read-invoked claim is only in the receipt, not in the staged reply.

### A11. The K-recency probe — used on the reply's gate claim

Protocol steps vs the reply's statement:
1. Define the corpus (24h corpus) — stated in 05-VERIFICATION.md & 06-MATRIX.md parked section.
2. The probe's own instrument: the gate claim is that the read is real-lock gated; the probe's
   demand on the gate claim is that the *record* prove the gate, not the reply. The reply's gate
   claim (rows 3, 16) cites the receipt.
3. The probe demands a successful long-session transcript to un-park the K-recency ground; the
   reply does not state the demand. This is the probe's derived demand.

### A12. The kit's one-command test-by-reading

`python3 hybrid_battery.py <bundle>` (bundle = readkit-bundle/) from the kit root; then
`sha256sum <bundle>/tools/memory_tool_store.py` → a43818a6…1586a. This is the test-by-reading;
it is runnable by an outsider and it exercises the three field points (sanitize, Windows lock,
stateless).

### A13. The candidates' status

- The long-session recurrence ground (K-recency): PARKED — un-park when a successful
  long-session transcript exists in the dumps.
- The 35-cell suite port: PARKED — un-park if the contour table must include the entire battery.
- The gateway read wiring: PARKED — un-park when the child lands.
- E6 (answer PR #12831's rationale): STAGED — waits the word.

### A14. The child's own commitments kept

- The team-up: the child's plan to answer the case with the read kit + battery; kept in the
  staged child.
- The hold-back: the child has not answered E6 yet; that is correct (waits the word).
- The smallest-diff thesis: the child's edits E1-E5 are the smallest diff; the child's own
  commitments are kept.

### A15. The eigen keeper framed as a special-use-case instrument

The reply frames the eigen keeper as a special-use-case instrument (the axes invariant across
versions), not as a general ledger. The report keeps that framing: it is a pin-discipline ruler,
not a score.

### A16. The read kit linked

The read kit is linked in the report via the bundle name, the battery, the store sha, and the
reproducibility section of 05-VERIFICATION.md.

---

## Purpose B — the instruments, tested by using them

### B1. The instruments-used table

| Instrument | How used | What it surfaced on this work | What failed / was missing | Outsider-usable? |
|---|---|---|---|---|
| MAP matrix (xngg) | Used as the spine of the claim check; every reply row's basis checked against 05/06 and the receipt | Rows 1-18 fully grounded; rows 19-20 (flat neutral, 14 LPs woven) asserted, not shown | Rows 19-20 need explicit statement; the reply's own claims are not in the matrix | Yes — the matrix shape and the check procedure are reusable |
| Bookkeeper (affected-set) | Applied to the reply's named claims: backlog shortlist, partner points, child edits E1-E6, unregistered run | The affected set is complete for partner points; the child edits are NOT listed; the unregistered run is not a named item | The reply does not list the child edits or the run as affected items; the hold-back and team-up are not in the set | Yes — the affected-set procedure is reusable |
| Eigen keeper | Applied to the reply's pins: read fix, spec, gate, child commitments | The invariant axes are mostly held; the dispatch-label drift (row 15) and the asserted flat-neutral/14-LP rows drift | The reply does not carry the correction note; rows 19-20 basis is not shown | Yes — the axis discipline is reusable |
| Two-N window | Lens on the compaction claim (50/50/0) | The claim survives if stated as two windows (50+50) with 0 leaked | The reply does not state the two windows explicitly | Yes — the two-N lens is reusable |
| Retention latch | Lens on the lock claim | Claim survives if latch is release-on-completion | The reply does not state release-on-completion | Yes — the latch lens is reusable |
| Tiny-aged-fact axis | Lens on the hash-claim | Claim survives if hash before/after + sha256 id is given | The reply gives unchanged status but no hash value | Yes — the axis lens is reusable |
| Read kit | Used as the test case (receipt/code/README) | The kit claims three contours green, sanitized, stateless; the receipt shows the numbers | The full 35-cell suite and byte-for-byte battery are not in the staged kit | Yes — the test-by-reading command works (A12) |
| K-recency probe | Used on the gate claim | The probe demands a long-session transcript to un-park the K-recency ground | The reply does not state the probe's demand | Yes — the protocol is reusable |

### B2. The kit's one-command test-by-reading

`python3 hybrid_battery.py <bundle>` (from the kit root) then `sha256sum <bundle>/tools/memory_tool_store.py` → a43818a6…1586a. Run by an outsider; exercises sanitize, Windows lock, stateless.

### B3. Candidates' status

- Long-session recurrence ground: PARKED (needs transcript in dumps).
- 35-cell suite port: PARKED (needs the contour table to include the entire battery).
- Gateway read wiring: PARKED (needs the child to land).
- E6: STAGED (waits the word).

---

## What would change the verdict

- WORK: if the reply adds the four register bins, the LP provenance table, the anchor-read gap
  50/50/0 statement, the doc_stats receipt line, the run name, the four-echo-sites asymmetry, and
  the narrow-first-slice statement → becomes READY (no further corrections).
- INSTRUMENTS: if the reply includes the two-N explicit windows, the retention latch release-on-
  completion, the hash before/after pair, the correction note, and the four-echo-sites asymmetry
  → the instrument uses become HOLD→READY; until then HOLD.

## The lane's own limits

- From the kit, the lane could not execute the WSL2 command or the native Windows command (no
  Windows host / no WSL2 in the sandbox); the WSL2 and native numbers are cited from the record
  (05-VERIFICATION.md), not re-run by this lane.
- The full 35-cell battery was not ported byte-for-byte (the bundle is the read-relevant import
  surface); the lane could not check the full suite.
- The reply's final "is a shape missing" answer and its E6 closure were not in the staged reply
  (they are child commitments); the lane could not verify them from the reply alone.
- The L2 audit (seven independent passes) was not re-run by the lane; the receipt numbers are
  trusted from the record.
