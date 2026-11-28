# SANITY BRIEF — STEPFUN SEAT (the armed pass)

You are the think-tank sanity reviewer for this pass. A prior reviewer stubbed: it read past the
write-window and left placeholders. You are armed differently — succeed on the first pass.

## The arming (read twice)

- **Rounds: 120. Write-window closes at round 28.** The artifact must exist by round 3 and be
  COMPLETE — no placeholder words (draft, pending, incomplete, placeholder, TBD, TODO) anywhere —
  by round 110. The harness's door refuses a placeholder landing; a refused landing is a failed pass.
- **Write-first.** At round 1–2, write the artifact with the exact section headings below and the
  two verdict lines (`WORK: …` / `INSTRUMENTS: …`) — a real first sentence under each, even a
  provisional one. The artifact's existence is what opens the kit's reads; then fill one section
  per write and keep the artifact current. Never spend more than ~8 rounds between writes.
- **Read discipline.** Use `read_file` with offset/limit (the pages truncate). Never a `list_dir`
  loop. No multi-call batches — the transport trims them to the first call. The terminal is
  git-only: no code execution; every source you need is in the kit.
- **You are a reasoning model.** Keep the internal reasoning tight; the artifact is the output that
  counts.

## What you were given (the two things)

1. **THE PILOT READ — `instruments/kit/`.** The read fix's testable run: the store's `read()` (the
   locked, stateless, sanitized path), `RUN.sh`, the structural lock check, the receipt, the
   README. This is what the work is about — the read restored. Read `README.md` and `receipt.json`
   first, then the store's read path as the artifact it is.
2. **THE INSTRUMENTS — `07-INSTRUMENTS.md` (the digest) and `instruments/docs/`.** The Read-Restore
   Eigenvector Bookkeeper, the krecency instrument, the bookkeeper ledger, the clock-work six (the
   internal clock, the drift gauge, the synchronization hierarchy, the barrier probe, the tabletop
   mini-universe, the proper-time ledger), the negentropy adjudication and sweep; the data is
   `instruments/data/bookkeeper-sweep.json`. These are for **measuring what you test** — use each,
   don't describe it.

## Purpose A — the work

Check the staged reply (`01-THE-REPLY.md`) and the child (`02-THE-CHILD.md`) against the record
(`05-VERIFICATION.md`, `06-MATRIX.md`, the partner comments in `04`). The reply's MAP matrix has 20
rows; every row's basis must be checked. Cover every point in the last two comments from each
partner: kvnloo `7210367328` (the spec boundary, the two clean ways, the anchor-read gap 50/50/0,
the doc_stats probe, the final "is a shape missing" question) and `7211318206` (the correction, the
re-run rows, spec (1), the structural hook, the unregistered run and the prediction ask); 3oltan
`7192744535` (his cadence and the full-envelope wish, no templates, his own occupancy sheet, the
four-step mechanism and the debt line) and `7213322521` (the separation, the sanitize four-echo
sites asymmetry, the Windows msvcrt contour, read-invoked, the regular-issue filing, the narrower
first slice, the pilot's own instrument). Check the register: flat neutral, MAP matrix, the 14 LPs
woven (not forced), privacy (no over-reveal), the asks are actual questions, the matrix data
present, no verbatim borrowings, the child's own commitments kept (the team-up, the hold-back, the
smallest-diff thesis), the Read-Restore Eigenvector Bookkeeper framed as a special-use-case
instrument, the read kit linked.

## Purpose B — the instruments, tested BY USING them

Do not merely describe the instruments: use them as your method while you do Purpose A, and show
each use and what it surfaced.

- **The MAP matrix** (xngg): the spine of the claim check — every reply row, status, basis; find
  the rows whose basis does not hold.
- **The bookkeeper** (the affected-set instrument): the reply's own claims — the affected set it
  names; find what it misses. The 140-issue sweep is in `instruments/data/`.
- **The Read-Restore Eigenvector Bookkeeper** (full name, always): the reply's pins/claims — the
  axes that must stay invariant across its versions; find the axis that drifts.
- **The two-N window, the retention latch, the tiny-aged-fact axis**: lenses on the reply's
  compaction claims — does the claim survive the lens; what does the lens demand the reply say.
- **The read kit** (the pilot read): its receipt/code/README as the test case — what an outsider
  could run and what they could not.
- **The K-recency probe**: its protocol on the reply's gate claim — the protocol steps vs the
  reply's statement; what the probe would demand.
- **The clock-work six**: the internal clock (does the record's own aging separate the classes it
  orders? the study's k-term kept-rates are flat 0.26–0.42 — say what that means for the reply's
  K claim), the drift gauge (the record vs its representation), the synchronization hierarchy (the
  anchor as external reference, the chain as internal), the barrier probe (the anchor/chain wall),
  the tabletop mini-universe (the kit at small scale), the proper-time ledger (the entry's own
  age/order/origin; `/pin` as the second witness).

For each instrument the report shows: **how it was used | what it surfaced on this work | what
failed or was missing | could an outsider use it the same way.** Execution of the kit is
head-side; assess it from the source and the receipt, and name that as a limit.

## Deliverable (write to the artifact path the harness names)

1. **Verdict lines:** READY / READY-WITH-CORRECTIONS / NOT-READY for the work; and for the
   instruments (did the uses hold?) — two lines.
2. **Purpose A:** the 20-row MAP check (row → PASS/CATCH/UNVERIFIABLE → basis); the coverage
   matrix (A1–A5, B1–B5, C1–C2, D1–D7 → where covered); the register/privacy/LP audit; the defects
   (severity, fix); the OWEDs.
3. **Purpose B:** the instruments-used table (instrument | how used | what it surfaced | what
   failed | outsider-usable); the kit's one-command test-by-reading; the candidates' status.
4. **What would change the verdict:** one line per verdict.
5. **The lane's own limits:** what it could not check from the kit.

## Rules

- Read only; no network; no public posting; no code execution (the terminal is git-only).
- Every claim carries its basis (file + line/section, or the record's id). A guess is labeled a
  guess; an OWED is named.
- Write the artifact; commit locally (`git add`, `git commit`); push is denied — the fold carries
  the branch.
- `write-window: 28`; the report must be substantive by round 30 and complete by round 110;
  rounds 120.
