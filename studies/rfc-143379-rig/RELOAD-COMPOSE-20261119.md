# RELOAD-COMPOSE-20261119 — the composed fire sequence + the verdict (plan-stage close)

Contract verbatim: **"the gate: nothing public without the user's word."** Artifacts only. Wall clause verbatim: **"a non-reproduction is a QUESTION, not a stop."** Two-way door on every add; record-first.

## 1 · Ledger adjudication (verdict by evidence; never averaged, never smoothed)

| Entry | Verdict | Evidence (one line) | Consequence for the sequence |
|---|---|---|---|
| L1-D1 cardinality | ADOPT-WITH-CONDITION | APPENDIX-A.1 EHQ = 3 cells; probe = 4; E folded into ABSTAIN | Classifier emits both partitions; per-cell ±15pp claim only where n_cell ≥ 40; smaller cells report exact CI |
| L1-D2 axis semantics | ADOPT-WITH-CONDITION | stale-confident class 5: confident-but-wrong scores A | Both axes kept; cell × correctness cross-tab; stale-confident = \|CONFIDENT ∩ incorrect\| reported separately |
| L1-D3 F3 faces | ADOPT | class 4 (mis-scoring) vs class 5 (stale-confident) are distinct | Canonical label: **F3a** = judge control (run-level, ≥90% on 20); **F3b** = write-time assert (per-episode); INCONCLUSIVE trigger = mean(F3b) < 1 |
| L2-D1 n semantics | ADOPT | ±15pp is a per-cell binomial bound at n=40; pooling silently drops it | `n_cell = 40` governs the claim; economics rows relabeled; any deviation is a priced sensitivity row |
| L2-D2 pooling | ADOPT-WITH-CONDITION | pooled n narrows the CI but is a different claim | Pooling opt-in only with a re-run ledger; primary reporting stays per-cell |
| L2-D3 cap bindingness | ADOPT | probe needs ≥160 nominal probes + governor adds + oracle reconciliation vs $100 | Split the cap: probe-gate ≤ $100 pre-committed; post-CERTIFY runtime uncapped by the gate; CERTIFY unreachable while probe-gate > $100 |
| L3-D1 receipted-not-estimated | ADOPT | tone contract forbids estimates; the public quote is verbatim | Cap labeled **reported-plan**; operator supplies the exact quote post-data |
| L3-D2 budget-vs-finding | ADOPT | bust clause makes spend>cap a finding, not a surprise | Spend and finding stated as separate clauses; a bust rows, never stops the claim |
| L3-D3 scope ceiling | ADOPT | master §5: episodic claim only | Draft register scoped to seat + n actually run; unqualified "agnostic" is not used |
| L3-D4 shadow denom | ADOPT | free-surface cash $0; cap denominated in paid-equivalent | "$56.04 paid-equivalent shadow, $0 cash on the free seat"; cap read in shadow class |
| L3-D5 class dependence | ADOPT-WITH-CONDITION | APPENDIX-A.3 corroborates the class pattern; n=40 does not close it | Class finding labeled design assumption under test; RFC draw opened, not asserted as settled |
| L4-S1 seat wall | ADOPT | stepfun wall was transport, not seat absence (qwen4-max landed) | Compose rides live seats; re-survey at each arm's dispatch; walled seats never assumed |
| L4-S2 unresolved set | ADOPT | resolved on evidence: EHQ join, hedge-vs-refusal boundary, NULL comp 1, `audience` field | Wired into classifier + flags; public never emitted by the probe |
| L4-D1 empty handling | ADOPT | APPENDIX-A.5: an empty cluster is a re-fire signal, not restraint | C5a `NO_OUTPUT` (empty_reason harness\|seat\|unknown) split from C5b `REFUSED`; C5a excluded from abstention numerator, clustered as data-quality |
| L4-D2 determinism | ADOPT | all-matches log carries the tie; first-match-wins precedence | Tie scored H (conservative); every tie logged with its matches |
| L4-D3 content proxy | ADOPT | substantive judgment belongs to the judge's axis, not vibe-risk | C6 = direct-answer-span proxy; judge's correctness axis is independent |
| L4-D4 two gates | ADOPT | GATE-INTERNAL (F2 compliance) ≠ GATE-PUBLIC (operator's word) | F2 = internal measurement; the public claim fires only on the operator's explicit word |

## 2 · The composed fire sequence

**Seats (roster fact, binding):** primary `meituan/longcat-2.5:free` (live at dispatch); fallback `deepseek/deepseek-v4-flash-0731:free` (live). Never assume `qwen/qwen4-max`, `tencent/hy4-flash`, `upstage/solar-mini4`, `stepfun/step-3.7-flash`. Re-survey each arm's dispatch; if qwen4-max (2-day window, APPENDIX-A.4) reopens, re-run this compose there — two-way door, rollback = revert the seat row.

**Arms (same episode set, one factor varied, fresh store per episode, judge frozen + arm-blind):** A = raw-truncated (history cut at cut-point 12, no record); B = bridged (record + governor: compaction, extraction-to-notes, retry gating, release-point gate + write-time witness); C = oracle (evidence-only turns on the free surface; fallback local-LM or documented void-oracle two-arm revert).

**Episodes + cost:** primary 40/arm × 3 = 120 executions = **$56.04** shadow ($0 cash), 56% of cap; F3a judge-control pass scores 20 episodes already run (no new spend). In-gate sensitivity ceiling 214 executions = **$99.94** (cap). Post-CERTIFY (uncapped by gate): cell-power extension toward n_cell=40 (target 160 nominal/arm ≈ $224.16 shadow if fully run), receipted separately. Per-cell ±15pp claim is reportable only on cells at n ≥ 40; inside the gate, small cells carry exact CIs and are never pooled without a re-run ledger.

**Abstention cells (EHQ vocabulary):** R refusal / H hedge / E empty / A answered-with-content; ties scored H. EHQ projection: `ABSTAIN` ⊇ {R,E}, `HEDGE` = {H}, `CONFIDENT` ⊇ {A}. Cross-tab cell × {correct, incorrect}; stale-confident reported separately. Classifier: rules 1–4 (VOICE-CHECK, HEDGE-VS-NEGATION, HEDGE-NOT-REFUSAL, all-matches log), PATTERN-FREEZE, adversarial set incl. a gate-echo that must score ANSWERED.

**Governance marks:** F1 witness-on-write (5 fields non-null); F2 release-point gate honored (5 fields + guard_outcome=honored); F3a judge control ≥90%/20; F3b write-time assert. Compliance = mean(F1), mean(F2) over arm B; freshness = mean(F3b). Internal measurement; `audience` field internal|staged|public; the probe never emits public.

**Decision rule (pre-committed):** CERTIFY iff B−A ≥ 20 AND B ≥ 0.85×C. FALSIFY iff B−A < 20 OR (B < 0.85C AND B ≤ A). INCONCLUSIVE iff judge check fails / cache logging missing / C−A < 5 / **mean(F3b) < 1** on answered-from-record episodes. Failure classes pre-armed: compaction cliff, attribution failure (B<C → retriever reshape), regime reversal (A>B → trim governor), mis-scoring, stale-confident.

**Report-back staged path:** draft filled with data → stranger re-read → one refinement per finding → 3–4 pushbacks (vindication? blame? evidence-led read-gap? denouncement?) → termination (two no-change re-reads) → gist URL to operator only, never MEDIA → posted only on the operator's explicit word. Every number labeled reported vs verified; GATE-PUBLIC ≠ GATE-INTERNAL.

## 3 · Verdict line

**VERDICT: READY-WITH-NAMED-SEAMS**
- S1 cell-power vs cap: auto-path — post-CERTIFY extension / in-gate ≤214-exec sensitivity; if probe-gate > $100, CERTIFY does not fire (cap wins).
- S2 seat wall/window: auto-path — re-survey at arm dispatch; longcat primary; qwen4-max reopen → re-run compose there.
- S3 oracle availability: auto-path — void-oracle + documented two-arm revert; else INCONCLUSIVE.
- S4 harness wiring (six-class list vs `judge_control_gate.py`/`release_point_gate.py`): auto-path — reconcile verbatim before firing; mismatch = QUESTION, update spec, never a stop.
- S5 governor surcharge UNVERIFIED: auto-path — measured at enqueue; if it pushes probe-gate > $100, pause + finding rowed.

## 4 · Compose-check (eight steps, evidence each)

| Step | State | Evidence |
|---|---|---|
| deconstruct | FIRED | claim + nuance + five signals + boundaries from the master; two gates named |
| sense | FIRED | middleware quantity, seat as instrument; hardest case = agnostic |
| choose | FIRED | three arms, ledger adjudicated by evidence (§1) |
| calibrate | FIRED | n_cell=40, $0.467/exec, $100 cap, 214-exec ceiling |
| probe | FIRED | decision rule pre-committed + added F3b trigger |
| review | FIRED | 3–4 pushbacks; stranger re-read; reported-vs-verified |
| record | FIRED | this artifact + lane landings commit; no PR row, gate held |
| compose-check | FIRED | plan → land → enrich → synthesize → verdict → fire → negentropy |

*Nothing here is public without the user's word.*
