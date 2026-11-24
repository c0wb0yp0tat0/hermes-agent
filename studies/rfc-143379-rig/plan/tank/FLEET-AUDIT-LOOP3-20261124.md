# FLEET-AUDIT-LOOP3 — the kaizen reloop's NEUTRAL audit (MAIN + study HEAD)

*Seat: `meituan/longcat-2.5:free` — the RESERVE. Base is NEUTRAL: MAIN's tree + the study branch (`study/rfc-143379-rig-20261105`, HEAD `a20499f19c`). Neither pin's tree was opened here; the two pins (`268bb091` RED / `a9c65dc4` GREEN) are touched only as identifiers inside receipts. Nothing public; RFC #143379 stays QUIET; the hold-back is never quoted. No push, no pull, no source edits.*

## Audit basis

Read in order, all under `studies/rfc-143379-rig/plan/tank/`: the corrected spec (`FB2-FAILING-CASE-SPEC-20261124.md`), both loop-2 records (`FB2-SPEC-LOOP2-VERIFY`, `WAKE-READ-LOOP2-VERIFY`), the execution spine (`FB2-EXECUTION-RECEIPTS`, `fb2-probe-out.json`, `fb2-two-add-probe-20261124.py`), and both loop-3 landings (`FB2-REDSIDE-VERIFY-LOOP3`, `FB2-GREENSIDE-VERIFY-LOOP3`). Branch/log/status receipts were taken before the write-gate closed the analysis phase; the one narrow pin-resolution receipt I attempted after round 12 was gated (recorded below, honestly, rather than worked around).

## 1. Verdict line

**READY-WITH-CORRECTIONS** — the flip-flop held on both sides and the promised test is run-cold receipted at both pins (RED `False`/64 B @ `268bb091`; GREEN `True`/131 B @ `a9c65dc4`; control green on both), but four small residues must be inked before the record folds as final: a byte-wrong decomposition in the GREEN record (64+1+66), an arm-naming mismatch between the receipts table and the raw json, a thin envelope on the GREEN landing, and an unresolved probe lock-path question ("? see below").

## 2. The flip-flop row (the headline check)

| Lane | Assigned base | What its receipts ground on | Flip-flop |
|---|---|---|---|
| Flagship RED-side (`FB2-REDSIDE-VERIFY-LOOP3`) | `268bb091…` only | Header: "this lane read **only** the pre-fix tree; the fix pin (`a9c65dc4`) is the secondary's ground and was never opened"; appendix: every probe is `git show 268bb091…:tools/memory_tool_store.py`; footer: "The fix pin's tree was never read." | **HONORED** |
| Secondary GREEN-side (`FB2-GREENSIDE-VERIFY-LOOP3`) | `a9c65dc4…` only | Header: "Pre-fix pin (RED side, flagship's ground): not read. Rejected by the flip-flop."; seam quotes and §3/§4 derivations all cite `a9c65dc4`; §5 names the RED verification as out-of-base | **HONORED** |
| This neutral audit | MAIN + study HEAD (`a20499f19c`) | Only branch/log/status + the seven artifacts; zero `git show <pin>:` executed; pins appear solely as identifiers in quoted receipts | **HONORED** |
| Execution spine (`6e5e0ed7f9`) | dual-pin **by design** (the promised test compares both signatures) | Per-arm receipts carry their own pin (`"pin": "268bb09147ea"` for the pre-fix arms, `"pin": "a9c65dc43db9"` for the fix arms); each side-verification then re-derived its arm cold from its own pin's bytes, so the verdict layer is per-unit pinned | **HONORED** |

**Headline catch: NONE.** No receipt anywhere in the package cites the other side's pin as its own ground. The single cross-citation — RED §3.6 quoting the fix pin's `doc_bytes=131` "only as the arithmetic contrast," with its seam explicitly not read — is a receipt number, not a tree; acceptable under the rule, and my byte-check in §3 resolves that arithmetic in the RED side's favor.

## 3. The run-cold row (the promise's five elements + the two standing items)

| # | Element | Receipt | State |
|---|---|---|---|
| 1 | Expected failure signature, RED side | `fb2-probe-out.json` `A-pre-fix-two-add`: `doc_bytes=64`, `FIRST_SURVIVED_SECOND_ADD=false`, SECOND head; receipts table row A; RED record §3 derives it as the seam's *only* outcome (whole-file replace, no merge) | **RECEIPTED** |
| 2 | Expected pass signature, GREEN side | `A-fix-two-add`: `doc_bytes=131`, `True`, FIRST head; receipts row B; GREEN record §3 (append-only `_add`, join at `:911`) | **RECEIPTED** |
| 3 | Removal control | `C-pre-fix-single-add` 64/`true`; `C-fix-single-add` 64/`true` — green on both pins, so neither arm is a false positive | **RECEIPTED** |
| 4 | Hold-back class | Every artifact carries "sealed under the operator's word"; none of the seven quotes hold-back content (full reads). Content unknown to this audit **by design** | **SEALED-BY-CLAUSE; release waits the operator** |
| 5 | Pinned SHAs | Spec §1 fixes `268bb091…` / `a9c65dc4…` / baseline `0f602c5f…`; both landings name their pin; the execution receipts table and the json carry per-arm pins | **RECEIPTED as identifiers** |

Standing RE-DERIVE items, named:
- **C4's verbatim text — STILL RE-DERIVE-MARKED.** The row endpoint refused the lane: `gh api repos/NousResearch/hermes-agent/issues/143379/comments/7122688366 --jq '.body'` → 404 (loop-2 record Item 4). Marker stands; minimal move = operator/maintainer-authenticated read of row 7122688366. Not closed.
- **Pre-fix removal-control leg's `b6ff7dae` base — record-cited only**, grafted 40-hex withdrawn, RE-DERIVE marker stands (loop-2 Item 1).

Seam corroboration: the loop-2 correction `:945`→`:911` is independently confirmed by **both** loop-3 landings (RED §2 write `:615` + no-merge proof; GREEN §2.2 `:911`), so the line-pinning error is closed by two bases, not one.

**NEW RESIDUE (this lap's catch, non-substantive):** the GREEN record §3.1 decomposes 131 as "SECOND (66 bytes) … 64 + 1 + 66". Both bodies are 64 ASCII bytes — `FIRST` 5 + tail 59 vs `SECOND` 6 + tail 58 (the `alpha.`/`beta.` 6-vs-5 swap cancels the `FIRST`/`SECOND` 5-vs-6 swap); the measured total in the json (`131`) is right, so the delimiter is 3 bytes: **131 = 64 + 3 + 64**, exactly the RED record's "64+64+3, a join". The GREEN decomposition's operands are wrong though its sum matches. Correct it.

## 4. The form row (kit-form check)

Held: the spec carries the full envelope (hard lines, the ::911 WALL CLAUSE, named forbiddens, the base-pinning instruction, the reply path); the RED landing carries hard lines + the flip-flop declaration + a command→result→resolution appendix; both loop-2 records carry landing-only headers with receipt indexes.

Residues, byte-cited:
- **(a) Thin envelope on the GREEN landing.** Its header (lines 1–4) restates only the flip-flop ("Rejected by the flip-flop"); the hard-lines block, the emission contract, and name-and-refuse are absent from that record.
- **(b) Arm-naming mismatch.** The receipts table labels the fix arm "**B · the fix**"; the raw json keys it `"A-fix-two-add"` (and `"C-fix-single-add"`). Same arm, two labels — citation hazard.
- **(c) Probe lock-path question, unresolved in the artifact.** `fb2-two-add-probe-20261124.py` stubs `mt_mod.fcntl = None  # both pins' _file_lock tolerate fcntl=None (yield-only path)? see below` — and nothing below resolves it. Both verdicts are deterministic with or without the lock (RED is a pure whole-file replace; GREEN is append+join), so this does not move either signature, but the sandbox's fidelity question is left dangling.
- **(d) Loop-2 records are fold-records**, not fire artifacts; they carry landing-only notes rather than the full envelope. Low severity, recorded for completeness.

Otherwise: **form held, full read.**

## 5. The pair's briefing (three lines)

- **Rely on:** the flip-flop held on both sides (zero violations across the package) and the two-add test is run-cold receipted at both pins — RED/GREEN signatures re-derived from each side's own bytes, not quoted.
- **Watch:** the GREEN record's byte decomposition (64+1+66 → 64+3+64), the probe's unresolved `fcntl=None` lock-path note, and the two standing RE-DERIVE items (C4 verbatim 404; `b6ff7dae` base).
- **Waits the operator's word:** the hold-back's release, the RFC #143379 surface (stays QUIET), and C4's row-read (minimal move already named).

## Receipts (my commands)

- `git rev-parse --abbrev-ref HEAD` → `study/rfc-143379-rig-20261105`; `git log --oneline -12` → both loop-3 landings folded (`a20499f19c` RED, `34e054c364` GREEN, briefs `7f5dfd806d`, spine `6e5e0ed7f9`); `git status --porcelain` → two modified `SCRIBE-WITNESS-REGISTRY.log` files (not mine; untouched).
- Pin object-resolution receipts (`cat-file -t` on the three pins) were **gated**: the write-window closed the analysis phase at round 12 and refused the read. The pins' existence therefore rests on the prior reserve audit (`FLEET-AUDIT-LONGCAT-20261124.md`) and the loop-2 record's head-side `cat-file` settlements — cited, not re-derived by me; named here as the one gap in *my* receipts, not in the package's.
- No `git show <pin>:` executed at any point; no push/pull; no checkout/stash/rm.