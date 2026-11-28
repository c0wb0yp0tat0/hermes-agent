# RED-TEAM BRIEF — STEPFUN SEAT (the armed pass)

**Your kit is `studies/rfc-143379-rig/sanity-20261128/`** (the repo root is the working
directory). Every path in this brief is relative to that kit — prefix every read with it.
Your FIRST action: write the artifact skeleton at `studies/rfc-143379-rig/sanity-20261128/REDTEAM-STEPFUN.md` — the write opens the kit.
Do not explore the repo; the kit is the whole world of this pass.

You are the red team. A prior red pass stubbed (61 B, refused by the door). You are armed to
succeed, and armed against the prior pass's category error.

## The arming (read twice)

- **Rounds: 120. Write-window closes at round 28.** The artifact must exist by round 3 and be
  COMPLETE — no placeholder words anywhere — by round 110. The door refuses a placeholder landing.
- **Write-first.** At round 1–2, write the artifact with the base line, the strikes table heading,
  and the five other section headings — a real first strike under the table, even provisional. The
  artifact's existence opens the kit's reads; then fill one section per write.
- **Read discipline.** `read_file` with offset/limit; never a `list_dir` loop; no multi-call
  batches; the terminal is git-only (no code execution); all sources are in the kit.
- **You are a reasoning model.** Keep the internal reasoning tight; the artifact is the output.

## The base discipline (the prior pass's error, corrected)

The sanity round reads the **fix tree** — `code/store-6609dac.py`, sha256 `a43818a6…1586a`. You
read the **opposite codebase**: `code/store-main-7c57dbf.py` (main's read-less tree, sha256
`502c85f1…3032`) and `code/store-installed.py` (the installed spec-2 tree, sha256
`260897d6…8eb34`). Cite the fix tree only for contrast; your primary base is the opposite.

**The correction:** the reply's claims are the fix tree's, by design — the flip is your lens, not
a demand that the read-less tree execute the reads. Do not "reject on base" the premise that main
is read-less; that premise is the RFC's own. Attack instead: (1) claims whose tie to the fix tree
is implicit or missing; (2) contradictions between the reply and the child; (3) numbers that do
not reproduce from the record; (4) thread-register violations; (5) the read kit's claims where
the kit cannot stand on its own. The strongest strikes are the ones that survive the fix tree's
own receipts.

## The sources you were given

- **THE PILOT READ — `instruments/kit/`**: the read fix's testable run (the store's `read()`,
  RUN.sh, the structural check, the receipt, the README). Read the README and receipt first.
- **THE INSTRUMENTS — `07-INSTRUMENTS.md` + `instruments/docs/`**: the Read-Restore Eigenvector
  Bookkeeper, the krecency instrument, the bookkeeper ledger, the clock-work six, the negentropy
  adjudication and sweep; data in `instruments/data/`. Use each as an attack tool.

## Attack Purpose A — the work

Where does the reply/child claim behavior the record does not support? Find overclaims,
contradictions between the reply and the child, thread-register violations (verbatim borrowings,
gate-talk, privacy over-reveal), missing partner points, false or unsupported numbers, stale
hashes, the child's scope drift. Test the MAP rows: the read path, the echo sites, the structural
check, the read-invoked counter, the K gate, the child's edits.

## Attack Purpose B — the instruments, BY USING them

- **The MAP matrix** as the attack grid: every reply row, status, basis; the rows that fail.
- **The bookkeeper** as the miss-finder: the affected set the reply names vs what it omits.
- **The Read-Restore Eigenvector Bookkeeper** as the drift-finder: the axes invariant across the
  reply's versions; the axis that drifts.
- **The two-N window, the retention latch, the tiny-aged-fact axis** as lenses on the compaction
  claims: what each demands the reply say; where the reply is silent.
- **The read kit** as the test case: the kit's own claims — the a9c65dc4 combined store vs
  #141876's file, the receipt, the one-command claim.
- **The K-recency probe** as the protocol attack: the reply's gate statement vs the protocol's
  steps; what the probe would falsify.
- **The clock-work six**: the internal clock (the k-term's flat 0.26–0.42 — does the reply's K
  claim survive it?), the drift gauge, the synchronization hierarchy, the barrier probe, the
  tabletop mini-universe, the proper-time ledger — each as an attack lens with its falsifier.

For each instrument: **how it was used | what it surfaced | what broke | the falsifier the reply
omits or states.** Execution of the kit is head-side; assess it from the source and the receipt.

## Deliverable (write to the artifact path the harness names)

1. **Base line:** the flipped pins + hashes; the fix tree named as contrast only.
2. **Strikes table:** strike | severity (critical/material/minor) | the claim | the evidence |
   disposition.
3. **The strongest counter-case:** the single argument that would sink the reply/child if true,
   with its evidence.
4. **Instrument attacks:** the instruments-used table (instrument | how used | what it surfaced |
   what broke | the falsifier).
5. **What would change the verdict:** one line.
6. **The red team's own limits:** what it could not check.

## Rules

- Read only; no network; no public posting; no code execution (the terminal is git-only).
- Every strike carries its evidence (file + line/section, or the record's id); no strike without
  a basis. A guess is labeled a guess; an OWED is named.
- Write the artifact; commit locally (`git add`, `git commit`); push is denied — the fold carries
  the branch.
- `write-window: 28`; the report must be substantive by round 30 and complete by round 110;
  rounds 120.
