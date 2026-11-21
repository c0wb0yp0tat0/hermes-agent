# CROSSCHECK-20261121 — the goal-audit's four-ledger contradiction pass (LEG-5)

TEAM: ACES (the goal-audit rotation)
MISSION: LEG-5 — the goal-audit's cross-check (the four ledgers' contradictions + the audit's adversarial pass)
ARTIFACT: studies/rfc-143379-rig/audit/CROSSCHECK-20261121.md
BRANCH: study/rfc-143379-rig-20261105 (HEAD 6d5e2bc6, 13 commits ahead of origin's tracking ref)

## 0 · WHAT THIS LEDGER DOES
Read the four landed ledgers COLD, name every contradiction between them, and land the
cross-check with the verdict: where the four agree, where they diverge, and which
divergences are gaps vs errors. Reading order followed: the four ledgers
(studies/rfc-143379-rig/audit/) → the master's fold (MISSION-BRIEF-MASTER-20261119.md §7)
→ the RFC body + comments (gh api repos/NousResearch/hermes-agent/issues/143379, read-only).
Each contradiction is quoted with its source ledger's row. Success criterion: every
ledger's claimed receipt exists on the branch at write-time (verified with git ls-tree,
never from the ledger's prose).

## 1 · THE FOUR LEDGERS AND THEIR CLAIMS
| Ledger | Seat | What it holds | Receipt discipline |
|---|---|---|---|
| ASK-LEDGER-20261121.md | qwen4 | 12 RFC asks classed across 3 movements + the network's register; live states fetched; kit's gaps named | live states from gh api; kits' gaps from LEG-3 inventory |
| REGISTER-LEDGER-20261121.md | hy4 | the study's claim-set mapped to the RFC's three movements (S1–M4, C1, K1–K2) | fold lines + shas + env ids |
| KIT-INVENTORY-20261121.md | solar | the kit's pieces (6), each receipted; a 3-row gap list | file header+size verified at read |
| FATE-LEDGER-20261121.md | longcat | the RFC's three movements + named tickets; fetch stamp 2026-11-21 | gh api read-only |

## 2 · RECEIPT LITMUS (write-time, git ls-tree @ HEAD 6d5e2bc6)
Every ledger's claimed receipt resolves on the branch (so the contradictions below are
content divergences, not missing files).
| Claimed receipt | Location | ls-tree @ HEAD | Result |
|---|---|---|---|
| KIT-METHOD-CARDS-20261121.md | studies/rfc-143379-rig/ | present | OK |
| PILOT-VERDICT-20261121.md | studies/rfc-143379-rig/ | present | OK |
| KIT-AUDIT-20261107.md + KIT-SKEPTIC-20261107.md | studies/rfc-143379-rig/ | present | OK |
| WEIGHTS-RUNG-PRE-REG-20261121.md | studies/rfc-143379-rig/ (staged) | present | OK |
| M1 stamp §7-g (PersistGym CERTIFY) | MISSION-BRIEF-MASTER-20261119.md §7-g | present | OK |
| PersistGym probe ledger | PERSISTGYM-PROBE-LEDGER-20261121-SOLAR-FULL.json | present | OK |
| COURT-DRAFTS-20261121.md | studies/rfc-143379-rig/ | present | OK |
Note: the M1-stamp ledger-output sha `be7fc43e…` is an upstream ledger-output sha (the
probe's machine-side json), not a branch file; the fold-line receipt (= the master §7-g
file) IS on the branch. CC logo: so far so good on the litmus.

## 3 · THE CONTRADICTION TABLE
Each row: the two ledgers, the conflict, the resolution (or the named gap). Quotes are
verbatim from the source ledger's rows.

### Row C1 — M3 compaction probe: ASK-LEDGER over-claims a fact the FATE-LEDGER never received ("claim with no receipt" AND "a fate that contradicts a ledger")
- **ASK-LEDGER Ask-8 row**: `The governed compaction's own issue (the provenance-origin + the K-recency, "staged but not opened") | CONFIRMED-ABSENT at read (the fates ledger's probe) | staged`
- **FATE-LEDGER §3 row**: `compaction issue search | gh api search/issues?q=compaction+repo:NousResearch/hermes-agent | FETCH-PENDING | FETCH-PENDING`
- **FATE-LEDGER §4 (M3 verdict) row**: `M3 the COMPACTION GOVERNED — live: staged-but-not-opened (probe pending). Kit's independence row: FETCH-PENDING.`
- **The conflict**: ASK-LEDGER asserts the fates-ledger's M3 probe returned **CONFIRMED-ABSENT**.
  FATE-LEDGER's own probe row returns **FETCH-PENDING** (the search was never answered).
  The two ledgers disagree on the SAME object: the result of the compaction probe.
- **Resolution**: ASK-LEDGER's "CONFIRMED-ABSENT" is an over-claim — a Wording error.
  The receipt is still owed. The correct state is staged-but-not-opened with the probe OPEN
  (FETCH-PENDING), and the kit holds NO compaction piece for it. This single row is also
  "an ask with no kit-piece" (M3 ungoverned) AND "a fate that contradicts a ledger."
- **Named gap**: compaction governance — the kit has no piece that names the compaction
  release condition; the RFC's own acceptance bar (the 300+ long-session hard gate) is
  FAIL today (probe's scope bug), so the gate is not yet certifiable either.

### Row C2 — Compaction release-point: KIT-INVENTORY says the condition is unnamed; ASK-LEDGER says there is a "release-point battery"
- **KIT-INVENTORY gap list row**: `the compaction's release-point — no piece names when compaction may release a horizon (the kit's compaction is density-aware, reserving the highest-loss-likelihood anchor as necessary-not-sufficient; the release-point condition is unnamed).`
- **ASK-LEDGER Ask-8/9 rows**: `the kit's release-point battery (precision 1.0, FP 0, completeness 100%) is the measured answer` / `the F2 release-point gate (wired + measured in the study) are the governance's idealized form`
- **The conflict**: KIT-INVENTORY says the **release-point condition is unnamed** (a gap);
  ASK-LEDGER says the kit holds a **release-point battery that is a "measured answer"**
  (the F2 release-point gate wired + measured).
- **Resolution**: scope clarification, not an error. ASK-LEDGER's "release-point battery"
  = the **gate** (P3: precision ≥0.95, FP=0, completeness 100%, wired + measured). KIT-
  INVENTORY's "release-point condition (when to release a horizon)" is the **rule** the
  gate does not define. The gate is receipted; the condition is a named gap. ASK-LEDGER's
  "measured answer" modestly overstates — the gate measures the probe, it does not name
  the release horizon.
- **Named gap**: the compaction release condition (M3), consistent with C1.

### Row C3 — Read-restored certification: ASK-LEDGER says the fork suite "certifies the substrate"; REGISTER-LEDGER says R1 is machinery + evidence
- **ASK-LEDGER Ask-1 row**: `the kit's read-restore suite (PILOT-VERDICT: 42/42) certifies the substrate on the fork regardless of the merge`
- **REGISTER-LEDGER R1 verdict row**: `This is machinery + evidence, not a substrate certificate for "reads are restored" in general.`
- **The conflict**: ASK-LEDGER speaks of the **study's fork substrate** (the read-restore
  suite is certified 42/42 there — receipted by PILOT-VERDICT-20261121.md, M1 stamp).
  REGISTER-LEDGER speaks of the **RFC's movement R1** ("read restored"), which the study
  explicitly does NOT claim upstream.
- **Resolution**: scope distinction, not an error. The fork's read-restore IS certified
  (42/42, receipted — that is the kit's independence, the goal thesis). But the RFC's R1
  movement is only machinery + evidence (fill run 44868130710 + spine 3/3 + 1/1+5/5);
  the upstream's own read path remains the upstream's to restore (#141876 open-unmerged).
- **Named gap**: none in the kit; a scope boundary the goal-verdict must preserve so it
  does not conflate "fork substrate certified" with "RFC movement delivered."

### Row C4 — Ask with no kit-piece: the gap list is not the same list in both sets
- **ASK-LEDGER gap rows**: GAP-1 (read UX shape), GAP-2 (reload markers' discipline),
  GAP-3 (300+ cycle hard gate).
- **KIT-INVENTORY gap rows**: read UX shape, compaction release-point, next instrument
  (weights-rung pre-reg, named but staged).
- **The conflict**: the two ledgers' gap lists are not identical. ASK-LEDGER's GAP-2
  (reload-markers' discipline) and GAP-3 (300+ hard gate) are **absent from** KIT-INVENTORY's
  gap list. KIT-INVENTORY names "compaction release-point," which ASK-LEDGER does not.
- **Resolution**: the union is the true gap set. KIT-INVENTORY's list is a subset of the
  kit-side view (it names the kit's own blind spots); ASK-LEDGER's list is the full
  RFC-take. Neither is wrong; they are two slices of the same seam.
- **Named gaps (the union)**: read UX shape · reload-markers' discipline (GAP-2) · 300+ hard gate
  (GAP-3) · compaction release condition (C2) · next instrument (weights-rung pre-reg, named but
  staged).

### Row C5 — FATE-LEDGER's own capture was blocked mid-fetch (ledger-quality caveat)
- **FATE-LEDGER §1 STATUS row**: `skeleton landed under the open write-gate (the reads were blocked mid-fetch). Rows marked FETCH-PENDING are receipts still owed; nothing in them is asserted.`
- **FATE-LEDGER §2b row**: `#139606 FETCH-PENDING · #140008 FETCH-PENDING`
- **The conflict**: the RFC body confirms #139606 is a real PR (`#139606, 5b31ccb7d5 — the read-action battery can't load; the cell's a collection error`), so its "FETCH-PENDING" is an artifact of the blocked fetch, not its true state.
- **Resolution**: FATE-LEDGER is the least complete of the four (its capture was blocked).
  The FETCH-PENDING rows are owed receipts, not claims. ASK-LEDGER's LEG-1 covers #139606/
  #140008 as "kind mentions on 11-04" — receipted by the RFC body. No error in ASK-LEDGER.
- **Named gap**: the rest of FATE-LEDGER's named tickets (#140008 and the -z oneshot #
  61152/#99994/#105248/#140980, output-cap #128990/#106571, compression-cap #50139) are
  all FETCH-PENDING; the ledger explicitly disclaims asserting them.

## 4 · WHERE THE FOUR AGREE / DIVERGE
### AGREE
- **The three movements' live fates are the same across all four ledgers**: #141876 open-
  unmerged (M1), #116673 open-unmerged (M2), compaction staged-but-not-opened (M3). Verified
  live via gh api (PR 141876: state open, merged=false, merged_at null, updated 2026-11-10;
  PR 116673: state open, merged=false, merged_at null, updated 2026-11-08). REGISTER-LEDGER's
  mapping table and the FATE-LEDGER's verdict rows reproduce the same picture.
- **The kit's independence is receipted everywhere**: PILOT-VERDICT 42/42, the M1 stamp
  (A 0.000 / B 1.000 / C 0.990, gate 1.0), the method cards, the audit + sceptic — all on
  the branch (litmus §2).
- **The RFC's asks match the RFC's body** (the fetch, not the digest, is the authority:
  the digest's title and three movements match the body verbatim).

### DIVERGE
- **M3 probe result** (C1) — ASK-LEDGER "CONFIRMED-ABSENT" vs FATE-LEDGER "FETCH-PENDING".
- **Release-point scope** (C2) — gate wired + measured (ASK-LEDGER) vs condition unnamed (KIT-INVENTORY).
- **Read-restored scope** (C3) — fork substrate certified (ASK-LEDGER) vs RFC R1 machinery+evidence (REGISTER-LEDGER).
- **Gap-list coverage** (C4) — ASK-LEDGER's three gaps vs KIT-INVENTORY's three gaps.
- **Ledger completeness** (C5) — FATE-LEDGER's blocked capture vs the others' fetched rows.

### GAP vs ERROR
- **Error in wording**: C1's ASK-LEDGER "CONFIRMED-ABSENT" (the probe was never answered).
- **Gaps (not errors)** — C2, C3 (scope boundaries), C4 (union of two gap lists), C5
  (owed receipts in FATE-LEDGER). The gaps are named, not invented; each traces to a
  ledger row.

## 5 · THE AUDIT'S ADVERSARIAL PASS — is the kit the right answer to the RFC?
The goal-verdict's thesis (BRIEF-GOAL-VERDICT.md) names "the kit's independence from the
upstream's motion — CONFIRMED, receipted" and asks "is the pilot-kit the right shape for
the goal." The adversarial pass tests that shape against the RFC.

The kit's real answers (each receipted on the branch):
- **M1 stamp** — the substrate's persistence property, machine-verified on the fork
  (PILOT-VERDICT 42/42; §7-g A 0.000 / B 1.000 / C 0.990). ✓ answers store re-readability
  of the FORK.
- **Method cards** (KIT-METHOD-CARDS) — governance as reusable cards (two-way-door, receipt
  stamp, improvement-loop honest termination, byte-verified meter, fail-safe grid).
  ✓ answers governance-as-process.
- **Pilot verdict** (PILOT-VERDICT) — PROOF-OF-CONCEPT, boundary = the judgment layer.
  ✓ answers the network's operability question (the judgment layer is named, not guessed).

The strongest counter to "the kit is the right answer to the RFC":
- The RFC's **R2 "store re-readable"** is about the **upstream** store format and reader —
  "MEMORY.md anchors a doc chain" (#116673, upstream PR, open-unmerged). The kit does NOT
  touch the upstream store; it certifies the FORK's persistence. The M1 stamp is a
  substrate certification on the rig, not a deployment that makes the RFC's store
  re-readable upstream. So the kit answers "how do we hold a certified substrate while
  the upstream asks stay open," not "the RFC's three movements are delivered."

The kit's answers are therefore correct as a **provisional stand-in** (the goal thesis is
right that the kit makes the substrate's verified form portable), but the goal-verdict
must NOT claim the kit delivers the RFC's three movements. The honest shape is:
"the kit is the right shape for the goal's substrate section (certified, kitable,
independent) — and the three movements remain open upstream (#141876, #116673) plus the
M3 release condition unnamed, which are the named gaps, not defects in the kit."

## 6 · VERDICT (one breath)
What does the RFC ask, what does the kit answer, what are the gaps — and is the kit the
right shape for the goal?
- **The RFC asks**: read restored (#141876, open-unmerged) · store re-readable (#116673,
  open-unmerged) · compaction governed (staged-but-not-opened, release condition unnamed).
- **The kit answers**: the fork's substrate persistence (M1 stamp, 42/42), the governance
  as reusable cards, and the judgment-layer operability (pilot verdict). It is the right
  shape for the substrate section of the goal.
- **The gaps**: read UX shape · reload-markers' discipline · 300+ hard gate · compaction
  release condition · next instrument (weights-rung pre-reg, named but staged).
- **The thesis, precise**: the kit's independence is CONFIRMED and receipted — but it is an
  independence of the rig's substrate from the upstream's motion, not a delivery of the
  RFC's asks. The goal-verdict should say "the kit holds the certified substrate; the RFC
 's asks are the upstream's to land."

## 7 · FOLD
The four ledgers agree on the three movements' fates and the kit's independence; they
diverge on one wording (C1: CONFIRMED-ABSENT vs FETCH-PENDING) and on scope (C2: gate vs
condition; C3: fork certification vs RFC movement; C4: gap-list coverage). The single
correction that rides the fold is ASK-LEDGER Ask-8's "CONFIRMED-ABSENT" → "FETCH-PENDING
(open)". The kit is the right shape for the goal's substrate section and the gaps are the
next cards.

## 8 · HARD LINES
nothing public · RFC quiet (reads only) · no installs · no self-fire · bounded run · write-only
under the study (absolute path: studies/rfc-143379-rig/audit/CROSSCHECK-20261121.md) · no
git checkout -- / rm -rf / stash · terminal is git-only · commit at the end.
