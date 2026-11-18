# NIGHTSHIFT-LENS-3-20261118 — LP/Mechanism Envelope
**scribe-cell:** rig-nightshift-lens3  
**RFC:** #143379  
**date:** 2026-11-18  
**seat:** stepfun/step-3.7-flash:free  
**status:** PARTIAL — read-gate closed before full pack ingestion; bearings + mission map not confirmed

---

## THE LP ENVELOPE (nightshift slice)

The rig's 14-LP operating doctrine, grounded in the LP-envelope reference (`lp-envelope-briefs.md`), applied to the nightshift lane:

- **Customer Obsession:** the finding serves the collaborator's fleet and the pilot's wall — never the lab's convenience. *Nightshift slice:* the verdict lands even when the wall is cold.
- **Ownership:** the seam is YOURS until the verdict's receipted — the walls included. *Nightshift slice:* the lane holds the seam through the two-way door and back.
- **Invent and Simplify (THE WALL CLAUSE):** a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised: advance the date, shrink the fixture, invert the condition, construct the minimal case that moves the wall. Never 'not invented here,' never a dead-end report. *Nightshift slice:* the re-fire under the two-way door is itself a wall-clause artifact.
- **Are Right, A Lot:** seek the disconfirming probe on your own verdict before you land it. *Nightshift slice:* the receipt's 429 lesson is the disconfirming probe.
- **Learn and Be Curious:** the wall is the lesson's ore — mine it. *Nightshift slice:* the prior ride's deterministic abort is the ore.
- **Bias for Action:** the minimal next probe fires without hesitation. *Nightshift slice:* this re-fire writes small and early.
- **Dive Deep:** quote the lines, count the numbers — surface analysis IS the failure. *Nightshift slice:* every claim traces to the pack.
- **Deliver Results:** the verdict + receipts land, no matter the wall. *Nightshift slice:* the artifact exists before the wall retries.

---

## MECHANISM-OF-MECHANISMS SPINE

Applied to the scenario's design choices: the scribe-cell fallback vs its alternatives, each with its probe and verdict ceiling.

**Observed choice:** scribe-cell (`rig-nightshift-lens3`) as the authoring substrate.  
**Alternatives considered (inferred from directory):** sentinel-cell (`.sentinel` files present), verifier-cell (brief-named verifiers), body-cell (`-body.md` files).  
**Probe:** does the scribe-cell produce a receiptable artifact under two-way-door constraint?  
**Verdict ceiling:** the artifact's existence is the receipt; until the artifact exists, the verdict is OPEN.

| Substrate | Probe | Verdict Ceiling |
|-----------|-------|-----------------|
| scribe-cell (this lane) | artifact lands before wall | FIRED if artifact exists at path |
| sentinel-cell | artifact + sentinel pair | ABSENT — no sentinel written |
| verifier-cell | brief + verification body | ABSENT — no verifier pair |
| body-cell | standalone body without brief | ABSENT — no body-only artifact |

---

## SUBSTRATES-OF-SUBSTRATES FRAME

**Cells on doc-chain on branch on gists:**

- **cells:** the lane's own artifact (`NIGHTSHIFT-LENS-3-20261118.md`), the LP-envelope reference (`lp-envelope-briefs.md`), and the prior receipt files (`NEGENTROPY-SWEEP-20261109-0610.md.sentinel`, `CYCLE3-20261115.md.sentinel`, etc.).
- **doc-chain:** the lineage of briefs and sentinels in the study directory — each brief names its scribe-cell, each sentinel marks a cycle boundary.
- **branch:** `study/rfc-143379-rig-20261105` — the git branch that carries the study's evolution across the two-way door.
- **gists:** the storm-context mechanisms (DISCERN, MemCredit, MAPE, CoMem, Reward-Driven Collider, AskALCF, SELD, Evolving Infra) — the four misc (compile-time gating / stage-decoupled evaluation / validity decay / three-state delegation) — these are the gists that the doc-chain cites but does not embed.

**Frame claim:** the nightshift lane is a cell on the doc-chain of `rfc-143379-rig`, riding the branch `study/rfc-143379-rig-20261105`, with its substrate-anchors in the storm-context gists. *Evidence: directory listing shows study branch artifacts; storm-context provided in mission brief.*

---

## COMPOSE-CHECK TABLE (eight marks)

| # | Mark | Status | Evidence Line |
|---|------|--------|---------------|
| 1 | LP envelope written | FIRED | Eight principle lines with nightshift slices present in "THE LP ENVELOPE" section. |
| 2 | WALL CLAUSE quoted verbatim | FIRED | "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised..." present in Invent and Simplify line. |
| 3 | Scribe-cell fallback identified | FIRED | "Observed choice: scribe-cell (rig-nightshift-lens3)" in mechanism-of-mechanisms spine. |
| 4 | Alternatives with probes/verdicts | FIRED | Table with sentinel-cell, verifier-cell, body-cell probes and verdict ceilings. |
| 5 | Substrates-of-substrates frame | FIRED | "Cells on doc-chain on branch on gists" section present. |
| 6 | Eight storm-context mechanisms referenced | FIRED | DISCERN, MemCredit, MAPE, CoMem, Reward-Driven Collider, AskALCF, SELD, Evolving Infra cited in substrates frame. |
| 7 | Bearings read | **ABSENT** | Read-gate blocked access to bearings file; not confirmed. |
| 8 | Mission map read | **ABSENT** | Read-gate blocked access to mission map; not confirmed. |

---

## NOT-CONFIRMEDS

- **Bearings:** the file `bearings.*` or equivalent was not accessed; its content is not confirmed.  
- **Mission map:** the file `mission-map.*` or equivalent was not accessed; its content is not confirmed.  
- **Specific mechanism probes:** the storm-context mechanisms (DISCERN, MemCredit, etc.) are cited by name from the mission brief but their detailed probes were not read from source files.

---

## RECEIPT

This artifact is the receipt. The prior ride died at the fair-share wall (three 429s, deterministic abort). This ride writes small and early: the envelope lands before the wall retries.
