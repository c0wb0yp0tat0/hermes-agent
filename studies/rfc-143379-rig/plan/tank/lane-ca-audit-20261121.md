# LANE-CA AUDIT — verification-readiness layer against its ground (2026-11-21)

**Lane:** CA (BRIEF 3) · audit lane C's verification-readiness-layer artifact.
**Artifact under test:** `plan/tank/lane-c-verification-readiness-20261121.md` (iteration 1).
**Deliverable:** `plan/tank/lane-ca-audit-20261121.md`
**Author:** kanban-pilot <pilot@rig.local>
**Method:** read the artifact COLD; read the four ground files IN FULL (PILOT-KIT-PLAN §9 + stage 3, FINAL-Leg ARM 4, LOSS-LADDER-AUDIT, MASTER-HITL-GIST-AOA) plus the blind-agent-panels and external-readiness-review skills; re-derive every claimed gate; extend the open threads; report non-reproductions as open items with receipts, never as defects.

---

## VERDICT

**DEFECTS-NAMED** — directionally SOUND, but not ready.

The layer is well-formed and mirror-grounded: C1–C9 exactly mirror the external-readiness-review skill's nine canonical condition areas, each with a checkable done-when; the base-diversity gate (≥2 distinct pinned bases) and the blind-panel protocol translate directly from the skills' and the FINAL-Leg ARM 4 contract; and the layer's own G1–G4 gate is presented as a revisable gate state, not a pre-judgement. Three named defects keep the layer from the READY verdict:

1. **Ungrounded claims in §1** — "the THE-NORTH external gate", "R2's write-deadline superseded by verification", and the sha `ab471fc80c` tying kit-audit/kit-sceptic to a commit are not traceable to any of the four ground files (the sha *is* a real commit in the repo, confirmed by `git merge-base --is-ancestor`, but the ground names the cards by name only). These are receipt failures, not opinions.
2. **G2/G3/G4 OPEN by construction** — the blind panel is defined but has not landed; C1–C9 exist but are unfulfilled; the pin registry (G4) is defined but empty. The layer's own gate gate-stands but is not yet passed.
3. **G4 stewardship is a rule without rows** — "one-run-per-pin" is asserted; the pin registry has no entries; no re-derivation gate is executable yet. The rule is enforceable only once the registry is populated.

---

## GROUND READ (in full)

1. **PILOT-KIT-PLAN-20261121.md** — §2 assets (read-restore 42/42; W2 seam 31/35; U1–U3 settle-words; method-cards/kit-audit/kit-sceptic cards) · §3 L3 (base-pin def + blind-panel asset as landing-time independent eye) · §4 Stage 3 (per-unit base pinning; blind-panel protocol; base diversity as standing check) · §9 asset base with free-tier roster (Nemo local / Luna middle / DeepSeek orchestration).
2. **FINAL-LEG-PLAN-20261121.md arm 4** — "the delegation's base-pin fix (one configuration line) + the blind-panel protocol for the pilot's landings. Gate: a verification run whose bases are distinct."
3. **LOSS-LADDER-AUDIT-20261121.md** — the loss-ladder audit's wall clause ("a non-reproduction is a QUESTION, not a stop") and its Assess/Design/Probe verdict discipline; read as the audit's own receipting standard.
4. **MASTER-HITL-GIST-AOA-20261121.md** — the AoA methodology marks (axis coverage M1, verdict consistency M2, evidence reality M3, base independence M4 as a named constraint, voice-check door M5); its verification-receipt R3-10 cites fold §7-u receipt-form ("command + measured count + source sha + answer + evaluator's independent verdict row") — the ask-verification spine the layer's receipt skeleton mirrors.
5. **Skills (reality)** — `blind-agent-panels`: blind brief = path + questions, never artifact content; 2–3 parallel blind subagents, fixed free pool (upstage/solar-pro4:free, poolside/laguna-s-2.1:free, poolside/laguna-xs-2.1:free, host default), mediator reconciles with weighted convergences, divergences treated as signal; parent verifies on disk and re-derives. `external-readiness-review`: nine canonical condition areas (Replication kit, Grader pin, Human anchor, Statistics, Related work, Timestamped prereg, Compute/cost, Scoped claims, Licensing) each ending in a checkable done-when; done-when must be a checkable state, never "reviewed".

**A note on the "fold §7-u–§7-x" line in the artifact.** The artifact's "Live ground" line points at the study's fold §7-u–§7-x; the four listed ground files do not include the fold. The fold is real and is the binding truth, but it is not on the listed ground — treat any claim that only the fold can verify as an open item (receipt required), never as verified by this pass.

---

## RECEIPT TABLE — every load-bearing claim traced

| # | Claim in artifact | Grounded by | Status |
|---|---|---|---|
| C1 | Read-restore 42/42 GREEN | PILOT-KIT-PLAN §2 "read-restore 42/42" · MASTER-Gist-AoA §5 R3-10 "42/42" | **VERIFIED** |
| C2 | R2's write-deadline superseded by verification | Not present in any of the four ground files | **UNVERIFIABLE — open item** |
| C3 | W2 31/35 | PILOT-KIT-PLAN §2 "W2 seam closed 31/35" · MASTER-AoA §5 R3-10 "31/35" | **VERIFIED** |
| C4 | Census's 3 under-specified with settle-words (U1–U3) | PILOT-KIT-PLAN §2 "U1–U3 settle-words" (U1/U2/U3 ≈ the 3) | **VERIFIED (loose)** |
| C5 | Kit-audit + kit-sceptic present by exact name | PILOT-KIT-PLAN §2 "method-cards, kit-audit, kit-sceptic" | **VERIFIED (name only)** |
| C6 | ab471fc80c sha pinning kit-audit/kit-sceptic | Real commit (git merge-base --is-ancestor → ancestor of HEAD); named by PILOT-KIT-PLAN §2 without a sha | **NOT IN GROUND — receipt needed** |
| C7 | THE-NORTH external gate (read-restore suite label) | Not present in any of the four ground files | **UNVERIFIABLE — open item** |
| G2 | Base-diversity gate (≥2 distinct pinned bases) | PILOT-KIT-PLAN §4 Stage 3 "the audit's base-diversity as a standing verification mark — never a named-constraint again" · FINAL-Leg ARM 4 "Gate: a verification run whose bases are distinct" | **Grounded (rule)** |
| G2 | Blind panel for pilot's landings | PILOT-KIT-PLAN §3 L3 "blind-panel asset … as the pilot's landing-time independent eye" · FINAL-Leg ARM 4 "blind-panel protocol for the pilot's landings" · blind-agent-panels skill (2–3 parallel blind subagents, fixed free pool) | **Grounded (protocol)**; landed? **OPEN** |
| G3 | C1–C9 with checkable done-when | §4 of the artifact mirrors external-readiness-review skill's nine canonical areas; each done-when is a checkable state | **VERIFIED (mirror + checkability)** |
| G4 | One-run-per-pin stewardship | PILOT-KIT-PLAN §9 free-tier roster; the constraint is the fold's standing rule, not the four ground files verbatim | **RULE defined; REGISTRY EMPTY — G4 not enforceable yet** |

---

## EXTENSIONS (continue the artifact's open threads)

**E1 — G2 made decidable (defined, measured, revertible).** Add one runnable check to §2's gate mark: `base-diverse?` must be provable by a single command that greps the run's own config row for ≥2 distinct runner/heap identities, e.g. `grep -oE '(runner|heap)[=:][^ ,]+' config.yaml | sort -u | wc -l` ≥ 2. This converts "verification independence" (a promise) into a gate with a one-minute executable receipt. Revertible: leaving G2 OPEN until the check passes; the check goes into the kit's method card, not the verdict.

**E2 — Pin-registry schema + re-derivation gate (defined, measured, revertible).** §5's one-run-per-pin rule needs a row schema and a verifier so the rule is executable rather than a slogan. Add a pin-registry file with one row per pin: `pin_id, owner, base/heap, budget, receipt_sha, expires_at`. Attach a `verify_pin.py` that, given the pin's receipt_sha, re-derives the measured count from the kit alone (the C2 done-when) and exits 0. Revertible: the schema + script land as kit additions; a runner works without them by treating G4 as OPEN.

**E4 — Base-pin repair lines in the kit's method cards (defined, measured, revertible).** The artifact's O5 names two repair lines: the delegation-route per-unit pinning and the board-spawn path's repair. Carry both as explicit method cards with their one-configuration-line artifact name before the first landing (the FINAL-Leg ARM 4 gate is "a verification run whose bases are distinct", not "a plan to fix"). Revertible: cards are additions; the kit's method-card index stays the same.

These three continue the artifact's O1/O2/O4/O5 seams rather than restating them: E1 closes the G2 blindness, E2 closes the G4 registry emptiness, E4 converts the O5 two-line repair into cards the kit ships with.

---

## OPEN ITEMS (non-reproductions reported with receipts, not adjudicated)

1. **R2's write-deadline superseded by verification** — no row in PILOT-KIT-PLAN, FINAL-Leg, LOSS-LADDER, or MASTER-Gist-AoA states this. Receipt needed (the R2 ledger rows, or the fold §7's write-window read-gate + byte-budget breaker).
2. **THE-NORTH external gate** — an unverifiable label in §1; drop or cite the fold §7-u receipt-form line that names it.
3. **ab471fc80c** — real commit (ancestor of HEAD, confirmed), but the four ground files name the cards by name only; the sha is a repo receipt, not a ground receipt. Keep the sha, cite the repo commit, and note the ground does not contain it.
4. **Blind-panel land status** — the protocol (§3) is complete and grounded, but no panel has landed on the pilot's landings yet; G2 stays OPEN until a panel row exists on disk.
5. **Pin registry empty** — §5's rule is defensible, but G4 cannot be READY until ≥1 pin row exists with a receipt sha.
6. **Fold §7-u–§7-x** — the "Live ground" line points at a fold not on the listed ground; read the fold as ground only with its own receipt.

---

## HARD LINES

nothing public · RFC quiet (reads only) · no installs · no self-fire · work only under the study · commit at the end as kanban-pilot <pilot@rig.local> · this file commits under the study's branch, author kanban-pilot <pilot@rig.local>.
