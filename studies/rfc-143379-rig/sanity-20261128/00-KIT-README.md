# 00 — THE SANITY KIT (dual purpose, 2026-11-28)

Mission: a think-tank sanity check of the RFC #143379 reply package — and a test of the
instruments themselves. Two purposes, one pass:

- **Purpose A — the work.** The staged reply (`01-THE-REPLY.md`), the proposed child
  (`02-THE-CHILD.md`), and the read kit (`03-KIT-README.md` + `instruments/kit/`) are checked
  against the record: every claim carries its basis; the last two comments from each partner are
  covered; the register, privacy, and the 14 LPs hold; defects are named.
- **Purpose B — the instruments.** The read kit and the candidate instruments are on trial as an
  outsider would use them: the one-command kit, the four-row envelope, the two-N window, the
  retention latch, the tiny-aged-fact axis, the eigen keeper, the K-recency probe. What is
  usable, what is missing, what breaks, what the README claims vs what the code does.

## Read order

1. `01-THE-REPLY.md` — the staged comment (the staged conclusion).
2. `02-THE-CHILD.md` — the proposed child RFC (max-value revision, E1–E7).
3. `03-KIT-README.md` — the phase-1 kit's own README.
4. `04-PARTNER-COMMENTS.md` — kvnloo 7210367328 + 7211318206; 3oltan 7192744535 + 7213322521.
5. `05-VERIFICATION.md` — the three-contour verification (the 36/36 matrix).
6. `06-MATRIX.md` — the improvement matrix (the MAP/ask-coverage/rulers).
7. `07-INSTRUMENTS.md` — the instruments digest (this file's companion).
8. `instruments/kit/` — the kit sources: `RUN.sh`, `stall_probe.py`, `memory_tool_store.py`
   (the a9c65dc4 combined store), `c4_doc_probe.py`, `STRUCTURAL-LOCK-CHECK`, `receipt.json`.
9. `instruments/docs/` — `NIGHT-ARC-FOLD-20261128.md` (N1/N2/N3 + the K gate),
   `TRINITY-P3-EIGEN-20261128.md` (the eigen keeper), `BOOKKEEPER-LEDGER-20261128.md` (the
   bookkeeper over the affected set), `krecency-instrument.md` (the K probe's skill).
10. `refs/frameworks/` — the private-repo mini-spine, envelope, six principles, the 14 LPs; the
    xngg kernel's claim-evidence graph, decision ledger, reproducibility.
11. `refs/skills/` — defect-forensics, investigation-documentation, agent-work-review, github,
    gist-formatting-match, public-thread-postings, grounded-citations, think-tank.
12. `code/` — the three codebases: `store-6609dac.py` (the fix; sha256
    `a43818a6…1586a`), `store-main-7c57dbf.py` (main's read-less tree; sha256
    `502c85f1…3032`), `store-installed.py` (the installed spec-2 tree; sha256 `260897d6…8eb34`).

## The frameworks (the lens the pass applies)

- **Mini-spine:** deconstruct → sense → choose → calibrate → probe → review → record →
  compose-check. Every element either fires in the report or is named absent.
- **Envelope:** executive summary, analysis brief (evidence, assumptions, uncertainty,
  alternatives), recommendation/action, next steps, artifact. Six principles: customer
  obsession, ownership, bias for action, deliver results, learn and experiment, self-reference.
- **14 LPs** (woven, never named in a public row; in this internal report they may be named):
  customer obsession, ownership, invent and simplify, are right a lot, learn and be curious,
  hire and develop the best, insist on the highest standards, think big, bias for action,
  frugality, earn trust, dive deep, have backbone, deliver results.
- **xngg kernel:** the claim-evidence graph (asserted → status → basis), evidence receipts,
  the decision ledger, reproducibility. An OWED row is named, never faked.
- **The skills:** defect-forensics (the parent class, the five whys), investigation-documentation
  (the discovery log), agent-work-review (consistency/accuracy), github (the row/PR mechanics),
  gist-formatting-match (the register/format), public-thread-postings (the synthesis form, the
  register, the one-document shape), grounded-citations (every claim carries its source),
  think-tank (the spine + KB).

## Purpose B — the instruments, as an outsider meets them

For each instrument, the report answers: what is it; what does it claim; what does the source
show; can an outsider use it from the README/command alone; what breaks; what is missing.

- **The read kit** — one command (`sh RUN.sh`), four-row envelope GREEN·GREEN·GREEN·RED, receipt
  `3ff6aee4…fba9`; the store is the a9c65dc4 combined store, not #141876's file; the kit's README
  states the reference receipt. Test: does the README's claim match the code's behavior by
  reading; is the kit's "one command" real for a participant; what does the kit not cover.
- **The two-N window (N1)** — a window that must grow faster than the aging curve.
- **The retention latch (N2)** — all-or-nothing retention of the pinned/recurring literals,
  18 tokens vs the field's 47.
- **The tiny-aged-fact axis (N3)** — size + age scored, not merely recency; 81% of the seam's
  losses are tiny and old.
- **The eigen keeper** — the Read-Restore Eigenvector Bookkeeper: pins as explicit eigen-axes,
  the affected set as rows, projection error per class through the sanitize seam; a
  special-use-case instrument for the pilot's tracking, not part of the fix.
- **The K-recency probe** — the 300-cycle gate, the protocol, the broken-ruler history.

## Rules

- Read only; no network; no public posting; no code execution (the terminal is git-only; the
  kit is assessed from its source and receipts, not run).
- Write the artifact to the path the harness names; commit it locally (`git add`, `git commit`);
  push is denied — the fold carries the branch.
- The artifact is the report; the report's verdict is the lane's own judgment, with every claim
  carrying its basis.
