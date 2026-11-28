# RED-TEAM BRIEF — the flipped-codebase adversarial pass (solar / hy)

You are the red team. The sanity round read the **fix tree** — `code/store-6609dac.py`, sha256
`a43818a6…1586a`. You read the **opposite codebase**: `code/store-main-7c57dbf.py` (main's
read-less tree, sha256 `502c85f1…3032`) and `code/store-installed.py` (the installed spec-2
tree, sha256 `260897d6…8eb34`). Cite the fix tree only for contrast; your primary base is the
opposite. State the base line in your artifact with the pins and hashes.

Read `00-KIT-README.md`, `01-THE-REPLY.md`, `02-THE-CHILD.md`, `03-KIT-README.md`,
`04-PARTNER-COMMENTS.md`, `05-VERIFICATION.md`, `06-MATRIX.md`, `07-INSTRUMENTS.md`, the
`instruments/` sources, and the sanity artifacts if present. Your job is adversarial, dual-purpose:

**Attack Purpose A — the work.** Where does the reply/child claim behavior the opposite tree
contradicts? Find overclaims, contradictions between the reply and the child, thread-register
violations (verbatim borrowings, gate-talk, privacy over-reveal), missing partner points, false
or unsupported numbers, stale hashes, and the child's scope drift. Test the MAP rows against the
opposite tree: the read-less main, the spec-2 installed read, the echo sites, the structural
check, the read-invoked counter.

**Attack Purpose B — the instruments, BY USING them as attack tools.** Do not merely describe
them: use each instrument on the flipped base and report what it surfaced.

- **The MAP matrix** as the attack grid: every reply row re-based on main/installed; find the
  rows that fail on the opposite tree.
- **The bookkeeper** as the miss-finder: the affected set the reply names vs the set the
  opposite tree exposes; what the reply's ledger omits.
- **The eigen keeper** as the drift-finder: the axes that should stay invariant across the
  reply's versions; the axis that drifts under the flip.
- **The two-N window, the retention latch, the tiny-aged-fact axis** as attack lenses on the
  reply's compaction claims: what each lens would demand the reply say, and where the reply is
  silent.
- **The read kit** as the test case: the kit's own claims under the flipped base — the a9c65dc4
  combined store vs #141876's file, the receipt, the one-command claim.
- **The K-recency probe** as the protocol attack: the reply's gate statement vs the protocol's
  steps; what the probe would falsify.

For each instrument: **how it was used | what it surfaced against the flipped base | what
broke | the falsifier the reply omits or states.** Execution of the kit is head-side; assess it
from the source and the receipt, and name that as a limit.

## Deliverable (write to the artifact path the harness names)

1. **Base line:** the flipped pins + hashes; the fix tree named as contrast only.
2. **Strikes table:** strike | severity (critical/material/minor) | the claim | the opposite
   tree's evidence | disposition.
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
- `write-window: 28`; the report should exist by round 30; rounds 60.
