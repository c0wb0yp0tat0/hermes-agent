# LANE-CA AUDIT — the verification-readiness layer, audited cold (iteration 2, 2026-11-21)

**Lane:** CA (BRIEF 3, proxy-approved dispatch) · blind-panel posture: the artifact is read COLD, the ground is named, no sibling content supplied as ground.
**Artifact under test:** `plan/tank/lane-c-verification-readiness-20261121.md` (iteration 1). sha256 at audit: `0df5c57ba236d2d18da69ce75c56e914c2a834e02630fdd0b9370660d9628e70`, size 18,978 B / 318 lines.
**Deliverable:** `plan/tank/lane-ca-audit-20261121.md` (this file — replaces the iteration-1 CA record; that record stays in git history, history never rewritten).
**Author:** kanban-pilot <pilot@rig.local>
**Method:** read the artifact in full; read the four named ground files in full (PILOT-KIT-PLAN §9 + stage 3 · FINAL-LEG-PLAN ARM 4 · LOSS-LADDER-AUDIT · MASTER-HITL-GIST-AOA); read the two skills' reality (`blind-agent-panels`, `external-readiness-review`); re-derive the four guarantees with local read-only checks; extend the open threads with NEW threads; report every non-reproduction as a QUESTION with a receipt, never as a silent stop.
**Grounding legend:** DOC-GROUNDED = file + section cited · SKILL-GROUNDED = skill rule cited · LOCAL-VERIFIED = re-derived by a read-only command this pass · UNVERIFIABLE-FROM-GROUND = not in the named ground; carried as a question with a receipt.

**WALL CLAUSE (verbatim, LOSS-LADDER-AUDIT §0/§6):** *a non-reproduction is a QUESTION, not a stop.* Applied here: an ungrounded claim is a question with receipts, not an assertion that the claim is false.

---

## VERDICT

**ADAPT — the layer is a sound SPEC of the verification guarantees, but not yet an EXECUTABLE one.**

In the layer's own gate vocabulary (§6): **NOT-READY with named seams.** In the pilot-kit's GO / ADAPT / PARK vocabulary: **ADAPT** — the direction is right, four concrete seams block READY, each with a checkable close condition below. No claim is made that the layer is wrong; the claim is that its guarantees are stated but not yet runnable on the artifact's own terms.

The four guarantees, each scored:

| Guarantee | Verdict | One-line reason |
|---|---|---|
| G2a — base-diversity gate real (≥2 distinct bases) | **PARTIALLY EXECUTABLE** | Threshold + rule grounded, but the gate's measurable is the wrong variable (`runner/heap` vs the ground's pinned **model base**) and no family of distinct bases is on record. |
| G2b — blind-panel protocol complete | **MOSTLY COMPLETE, NOT LANDED** | All three mission-named dimensions present (blindness, real-work missions, mediator reconciliation); two skill-mandated controls absent (target hard-pin + coverage check; brief-neutrality check). No panel row landed. |
| G3 — nine conditions with checkable done-whens | **FAIL ON FORM** | C1–C9 mirror the skill's nine areas and each done-when is a checkable state; but §4's own promise — a CHECKLIST table `(Action \| Artifact \| Done-when)` per condition — has **zero** tables in the file. |
| G4 — one-run-per-pin enforceable | **RULE ONLY, NOT ENFORCEABLE** | Rule + registry role + two-way door defined; registry file and verifier absent (0 hits), and two structural conflicts with panel/iteration dispatch are unresolved. |

None of these is a contradiction of the ground. All four are "defined, not closed," which is exactly the layer's own G2/G3/G4 = OPEN (§6:267–269). The audit's job is to make each OPEN gate's close condition executable, not to smuggle an OPEN gate into PASS.

---

## A · BASE-DIVERSITY GATE — receipts

**Claim traced:** §2:99–105 — BASE-DIVERSE iff a family holds ≥2 distinct pinned bases and the claim is not "same-base"; default family = execution / audit / blind panel; "at least two of the three must be pinned to distinct runner/heap identities as recorded in the run's own config row."

- **Grounded rule:** PILOT-KIT-PLAN §3-L3 "the audit/AoA route shared ONE pinned base (`upstage/solar-mini4:free`) — the flip-flop rule was named, not honored"; §4 Stage 3 "the audit's base-diversity as a standing verification mark — never a named-constraint again." FINAL-LEG ARM 4: "Gate: a verification run whose bases are distinct." The threshold (≥2 distinct) is a faithful translation. **DOC-GROUNDED.**
- **The variable mismatch (the load-bearing finding).** The ground's diversity variable is the **pinned model base** — a provider-qualified ID such as `upstage/solar-mini4:free` (MASTER-HITL-GIST-AOA M4, §130–131: the shared base is named). The artifact's measurable is **"distinct runner/heap identities"** (§2:104–105). Those are different units: two runs of the *same* model on two different hosts (pve1 / p0tat0 / c0wb0y / cloud — PILOT-KIT-PLAN §2 "runners") satisfy "distinct runner identities" while remaining single-base — i.e. the literal gate can PASS while the ground's intent FAILS. **LOCAL-VERIFIED:** the term `runner/heap` occurs only at artifact line 104; `solar-mini4` at lines 74, 83 (the compose base, correctly named). **Seam, with a close condition:** redefine the gate's measurable as distinct pinned **model-base IDs**, and add the explicit exclusion "two runs of one model on two hosts are not base-diverse."
- **Skill nuance carried, not invented:** `blind-agent-panels` pitfall "Both delegate children inherit the parent model … the pin is GLOBAL … for per-lane model diversity: re-pin sequentially + `delegate_task`." So a *parallel* blind panel is normally **one** base replicated across child IDs, not "a third base" by construction (artifact §2:102–104 labels the panel "a third base, different runner"). The family can still reach ≥2 distinct bases (compose=solar-mini4, panel=one pinned free base, audit=another), but the artifact must say the diversity is at the *dispatch-pin* level, not the *child-ID* level.
- **Not demonstrated:** no family-of-distinct-bases row is on record for this gate. G2 remains OPEN per §6:267 and per the study's own continuation rows (MAIN-LOOP-ROUND7:65 measures the registry/bases absent). A gate that has never fired is a rule, not a receipt. **WALL-CLAUSE posture:** the non-demonstration is a QUESTION — "which run's config row is the BASE-DIVERSE receipt?" — not a claim that diversity is impossible.

**Guarantee verdict:** PARTIALLY EXECUTABLE. Fix the variable; then fire one family and record its config row.

---

## B · BLIND-PANEL PROTOCOL — receipts

**Claim traced:** §3:114–147.

The three dimensions the mission asks about are all present and skill-faithful:

- **Blindness in the briefs — PRESENT.** §3:127–134: the brief names artifact path + questions and does NOT describe content; the skill's non-negotiable ("the blind condition is only as blind as the brief … naming its shape pre-seeds the lanes") is quoted correctly. Workers read chain files with `read_file` FIRST — SKILL-GROUNDED (`blind-agent-panels`: "delegate briefs must state the local-read path … never `web_extract` on private IPs").
- **Real-work missions — PRESENT.** §3:132–134 carries discovery → harness page reading → retry-once-then-fallback → stop at CAPTCHA/2FA, and explicitly forbids a separate supervisor-side research lane. SKILL-GROUNDED (rules 1–3; `browser-harness-sop` method).
- **Mediator reconciliation — PRESENT.** §3:143–147: "convergences weighted; divergences treated as signal, never averaged … FOUND-PARTIAL on the same claim from two panels is a named seam … nothing reconciled away by a majority." SKILL-GROUNDED (rule 6, verbatim intent). The parent-verifies-on-disk rule (skill rule 5) is also present at §3:138–141, including the correct treatment of an empty `{}` summary with a written artifact as a *self-report miss, not a missing artifact*.

**Two skill-mandated controls absent (the findings):**

1. **No target hard-pin / sibling-read forbid / coverage check.** The skill's pitfall "Audit rotations collapse to one target unless the target is hard-pinned … forbid reading sibling artifacts … verify coverage (every target audited exactly once)" has no counterpart in §3. The artifact says workers "read the rig's chain files" (plural, broad) — a lane can drift to a sibling artifact and the protocol has no coverage row to catch it. Close condition: pin the exact target path in each brief + forbid sibling reads + add a post-landing coverage table (one row per target, audited exactly once).
2. **No brief-neutrality check.** The skill's pitfall "scrutinize the brief for the parent's own verdicts BEFORE dispatch — a brief's invented framing becomes the lane's 'independent' output" has no counterpart. §3 requires the brief not describe *content*, but does not forbid a parent verdict or evaluative label. Close condition: an adversary pass over each brief that removes any verdict the user did not state.

**Not landed:** the verdict vocabulary `FOUND-EXACT / FOUND-PARTIAL / NOT-FOUND / GUESSED-WRONG` appears 4× in the artifact, all in the template/protocol description (§1 row, §3.4) — LOCAL-VERIFIED by grep. Zero landed panel rows exist. The protocol is complete enough to dispatch; G2 stays OPEN until a panel row is on disk.

**Guarantee verdict:** MOSTLY COMPLETE on the three named dimensions; two controls short of the skill; un-landed. ADAPT, not reject.

---

## C · NINE READINESS CONDITIONS — receipts

**Claim traced:** §4:151–217, preamble line 153: "Each condition ends with a CHECKLIST table (Action | Artifact | Done-when). A done-when is a checkable state, never 'reviewed' / 'done'."

- **Mirror — VERIFIED.** C1 Replication kit · C2 Grader pin · C3 Human anchor · C4 Statistics · C5 Related work · C6 Timestamped prereg · C7 Compute/cost · C8 Scoped claims · C9 Licensing. This is the `external-readiness-review` skill's nine canonical areas, in order and by name. DOC-GROUNDED (skill §"nine canonical condition areas").
- **Done-when checkability — VERIFIED for all nine.** Each ends in a checkable state with an observable: C1 `sha256sum -c SHA256SUMS` exits 0; C2 pin alone + kernel reproduces the count; C3 session log shows control-score spread / κ defined with the NULL-with-named-seam clause; C4 MDDL + Wilson CI + grader variance + effective-n + per-cell failure bound; C5 3+ cited lines, no overclaim; C6 timestamped link + internal freeze seal; C7 cost rows + `cost_total=0.0` + UNVERIFIABLE markers; C8 overstatement→replacement table retaining scope variables; C9 license URL + declared license + fair-use factors, lowest byte-preserving-risk option. No "reviewed"/"done" appears as a done-when. SKILL-GROUNDED + DOC-GROUNDED.
- **The form failure — CONFIRMED.** LOCAL-VERIFIED: `grep -nE '^\| *(Action|Done-when)'` on the artifact returns **0** rows. §4 promises a `(Action | Artifact | Done-when)` table per condition; **none of C1–C9 has one.** The `external-readiness-review` deliverable contract requires "one section per condition … each ending with a CHECKLIST table of `Action | Artifact | Done-when`" — so the artifact fails both its own stated form and the skill's contract. This is the single clearest executable gap: a done-when without its Action and Artifact columns is a tag, not a checklist.

**Guarantee verdict:** FAIL ON FORM (fixable additively). The nine done-whens themselves survive the audit; only the promised tables are missing. That is ADAPT, not PARK.

---

## D · ONE-RUN-PER-PIN STEWARDSHIP — receipts

**Claim traced:** §5:220–254.

- **Rule — DEFINED and grounded in posture.** "Each pin exactly once per study lifecycle"; "the dispatcher stands as the pin registry's only writer"; "a second run … allowed only after the pin's first receipt is re-derived by an outsider — the re-derivation is the gate"; the free-tier roster (Nemo local / support seats / flagships-first rotation / Nemo-Luna-DeepSeek as layers) matches PILOT-KIT-PLAN §9 and FINAL-LEG "THE WINDOW CLAUSE." DOC-GROUNDED.
- **Registry absent — CONFIRMED.** LOCAL-VERIFIED: a whole-study `find` for `*pin_registry*`, `pins.json`, `verify_pin*` returns **0** files. The rule has no rows and no verifier; G4 cannot be READY (§6:269; the layer honestly keeps it OPEN). Per the wall clause: the empty registry is not "one-run-per-pin is false" — it is the QUESTION "where is the first pin row + its re-derivation receipt?" with a receipt (the 0-hit find).
- **Two structural conflicts, unresolved:**
  1. **Panel vs. one-run** — a 2–3 member blind panel on a single global dispatch pin (skill rule: pin is GLOBAL) is multiple *runs* of one pin. The artifact names this as its own O1 (§7:282–287) but does not decide the unit: is "one run" per pin-instance or per pin-ID across a panel? Close condition: name the unit explicitly and state whether a panel consumes N pins or one pin with N children.
  2. **Iteration/audit-of-audit vs. one-run** — the skill's standing loop requires "another iteration = re-dispatch the same angle with its own prior report as input" and the audit-of-audit chain re-runs the same model across layers. One-run-per-lifecycle collides with that unless "lifecycle" is scoped per phase. The artifact does not name this at all. Close condition: scope "lifecycle" (per phase / per study) and reconcile with the skill's re-dispatch rule.

**Guarantee verdict:** RULE ONLY, NOT ENFORCEABLE. The rule is sound as governance; enforcement awaits a seeded registry, a verifier, and the two unit decisions.

---

## E · CLAIM-BY-CLAIM RECEIPT TABLE

| # | Claim (artifact line) | Ground / skill / local check | Status |
|---|---|---|---|
| R1 | Read-restore 42/42 GREEN (§1:34) | PILOT-KIT §2 "read-restore 42/42"; MASTER-AoA §5 R3-10 "42/42" | VERIFIED (DOC) |
| R2 | W2 31/35 (§1:36) | PILOT-KIT §2 "W2 seam closed 31/35"; MASTER-AoA R3-10 | VERIFIED (DOC) |
| R3 | Census 3 under-specified, settle-words (§1:37) | PILOT-KIT §2 "U1–U3 settle-words" | VERIFIED (loose: U1–U3 ≈ 3) |
| R4 | kit-audit + kit-sceptic present by name (§1:37–38) | PILOT-KIT §2 names all three cards | VERIFIED (name only) |
| R5 | sha `ab471fc80c` ties the cards to a commit (§1:38) | `git merge-base --is-ancestor ab471fc80c HEAD` → yes (LOCAL); no named-ground file carries the sha | COMMIT REAL; NOT IN GROUND → question with receipt |
| R6 | "THE-NORTH external gate" (§1:34) | grep over the four named ground files → 0 hits (LOCAL) | UNVERIFIABLE-FROM-GROUND → question |
| R7 | "R2's write-deadline superseded by verification" (§1:35) | no row in the four named ground files | UNVERIFIABLE-FROM-GROUND → question |
| R8 | model sha `415501bd…` = staged pin, live-HF + byte-identical (§1:47) | external/live claim; this pass read no external pages per artifact's own legend | UNVERIFIABLE (online) → question, not disputed |
| R9 | ≥2 distinct bases gate (§2:99–105) | PILOT-KIT §3-L3/§4-Stage3; FINAL-LEG ARM 4 | RULE VERIFIED; MEASURABLE MISMATCH (§A); not fired |
| R10 | blind brief = path + questions, not content (§3:127) | blind-agent-panels "pitfalls: blind condition" | VERIFIED (SKILL) |
| R11 | 2–3 parallel blind workers, fixed pool (§3:122–126) | blind-agent-panels pool: solar-pro4:free, laguna-s-2.1:free, laguna-xs-2.1:free, host default | VERIFIED (SKILL); base diversity at pin level, not child ID |
| R12 | mediator: convergences weighted, divergences signal, not averaged (§3:143–147) | blind-agent-panels rule 6 | VERIFIED (SKILL) |
| R13 | C1–C9 mirror nine areas, checkable done-when (§4) | external-readiness-review nine areas + deliverable contract | VERIFIED (mirror + checkability) |
| R14 | "each condition ends with a CHECKLIST table" (§4:153) | grep for table rows → 0 (LOCAL) | CONTRADICTED BY ARTIFACT → form failure |
| R15 | pin registry sole writer = dispatcher (§5:235–237) | posture grounded; registry/verifier files → 0 (LOCAL) | RULE VERIFIED; ENFORCEMENT ABSENT |
| R16 | "Live ground: fold §7-u–§7-x" (header:18) | fold is not among the four named ground files | question with receipt (read fold with its own receipt) |

---

## F · EXTENSIONS — NEW threads continuing O1–O5

These are **new**, not restatements. Each is defined / measured / revertible in the layer's own idiom. Thread numbers continue the artifact's O1–O5 (§7:280–305).

**O6 — Correct the base-diversity measurable (extends O5).** The gate at §2:104–105 measures "distinct runner/heap identities"; the ground measures distinct **pinned model-base IDs**. Define the check as: family is BASE-DIVERSE iff `grep -oE '[a-z0-9._-]+/[a-z0-9._-]+:free' <run-config> | sort -u | wc -l` ≥ 2 **and** the family's claim is not "same-base," with the explicit exclusion that two runs of one model on two hosts do not count. *Measured:* one command + the run's config row; a two-host/one-model fixture must score 1, not 2. *Revertible:* additive method-card line; G2 stays OPEN until it passes. This sharpens the prior E1 check by fixing the *variable*, not just adding the command.

**O7 — Define the unit of "one run per pin" for panels and iterations (extends O1).** Two-way door, no constraint imposed: (a) a blind panel consumes one pin per child (sequential re-pin per the skill), so a 3-member panel spends 3 pins; or (b) "one run" is counted at the pin-ID level and a panel is one pin with N children — in which case §5 must say so explicitly and the registry row must carry the child count. Extend the same decision to the skill's iteration/audit-of-audit re-dispatch: scope "lifecycle" as per-phase or per-study. *Measured:* a registry row schema that can represent the chosen unit; a panel dispatch whose child count matches. *Revertible:* a documented unit definition; no pin is retired without a receipt either way.

**O8 — Deliver the missing CHECKLIST tables (extends O4 / closes the C-form failure).** Add an `Action | Artifact | Done-when` table under each of C1–C9; the done-when text already audited in §C moves into the third column, and an Action + Artifact column is supplied per condition (e.g. C1 Action "pack + hash", Artifact "kit zip + SHA256SUMS"; C4 Action "compute MDDL/Wilson/grader-variance/effective-n", Artifact "stats appendix + rubric_sensitivity.py output"). *Measured:* `grep -c` of table rows goes 0 → 9. *Revertible:* additive tables; the layer's gate states do not move until the tables' done-whens fire.

**O9 — Add brief-neutrality + target-pinning controls to the panel protocol (extends O1/O3).** Insert two pre-dispatch rows into §3: (i) an adversary pass that strips any parent verdict/evaluative label from the brief (skill framing-contamination pitfall); (ii) a target hard-pin + forbid-sibling-reads clause, followed by a post-landing coverage table asserting every target audited exactly once (skill rotation-collapse pitfall). *Measured:* a brief diff with zero parent verdicts; a coverage table with one row per target and no duplicate/zero rows. *Revertible:* protocol additions; a dispatch without them is a named seam, not a silent panel.

---

## G · OPEN ITEMS — non-reproductions carried as QUESTIONS, with receipts

1. **Q-THE-NORTH** — which named-ground line defines the "THE-NORTH external gate" (§1:34)? Receipt: grep over the four ground files → 0. Needs the fold §7-u receipt or a drop from §1.
2. **Q-R2** — which ledger row shows "R2's write-deadline superseded by verification" (§1:35)? Receipt: no row in the four ground files. Needs the R2 ledger or the fold's write-window read-gate + byte-budget breaker line.
3. **Q-ab471fc80c** — real ancestor commit (LOCAL `merge-base` ✓) but not in the named ground. Receipt: PILOT-KIT §2 names the cards without a sha. Keep the sha, cite the repo commit, mark the ground gap.
4. **Q-model-sha** — `415501bd…` = staged pin / live-HF / byte-identical reassembly (§1:47) is an online claim; this pass read no external pages (per the artifact's own legend). Receipt: artifact header:21. Not disputed; needs an ONLINE-GROUNDED pass with URL.
5. **Q-fold** — the "Live ground: fold §7-u–§7-x" line names a fold not in the four files. Receipt: header:18. Read the fold with its own sha/line receipt before treating fold-only claims as verified.
6. **Q-panel-row** — no landed blind-panel row exists. Receipt: verdict vocabulary occurs 4×, all in template/protocol text; zero landed rows. G2 stays OPEN.
7. **Q-registry** — no pin registry / `verify_pin.py` on disk. Receipt: study-wide `find` → 0 files. G4 stays OPEN.

---

## H · HARD LINES

nothing public · RFC #143379 + #5320 + #157065 QUIET · no installs · write only under the study · no `git checkout --` / `rm -rf` / stash · this file commits under `study/rfc-143379-rig-20261105` as `kanban-pilot <pilot@rig.local>` · the four OPEN gates stay OPEN on the record; no seam smoothed into a PASS.

*Facimus semper. The layer is a structure; the structure is the record; the record corrects itself out loud.*

*— kanban-pilot <pilot@rig.local>, 2026-11-21, iteration 2 (lane CA, BRIEF 3)*
