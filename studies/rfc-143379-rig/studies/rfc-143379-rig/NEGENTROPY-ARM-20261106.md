# NEGENTROPY-ARM-20261106 — the order the compression must reserve (design leg, apex seat)

the gate: nothing public without the user's word

**Branch:** `study/rfc-143379-rig-20261105` (fork only). **Domain:** COMPLICATED (expert analysis of the compressor's ordering; no live probe in this leg). **Register:** receipts, never claims. **Hand-separation:** **[1st]** = re-read by this lane at the cited file:line or JSON line this pass. **[2nd]** = carried from a study doc and not re-derived here.

## [Executive Summary]

| part | verdict | one line |
|---|---|---|
| (1) Budget | **PARTIALLY-SHAPED** | Four classes in order: decision-core > continuation (next-action, scope) > exact anchors (clock and identity literals) > scope boundaries. The weights are (3.0 − baseline median), but they come from the ladder JSONs, not from the krecency CSVs (see Seam S1). |
| (2) Promotion | **DESIGNED** | A reserved tier inside `_build_anchor_index`, ahead of the `(-counts,-last_seen)[:cap]` sort and below the 7,000-char budget. It promotes single-occurrence literals in **non-user** turns plus forward-intent lines. Re-injection rides `_augment_summary_lean`. Success signal: the debug fixture's decision-core and next-action probes at ≥ 3.0. |
| (3) Scalar | **MEASURABLE**, one-anchor case only | R = per-literal survival × probe lift, computed from the battery's own JSONs (`expected_facts` vs `summary_text` vs per-probe `overall`). The full-budget scalar stays a QUESTION: judge-gated and empty-answer-confounded (Wall W2). |
| (4) RippleMem borrow | **PARTIAL** | The cue → completion idea fits the *read side* (the session_search recovery footer). It does not do the *write-side reservation* this arm needs. The seam is the cue key = the reserved literal. |

Status vocabulary: the reservation tier is **DORMANT**, at the *described* rung only. The lean anchor index and the verbatim user section are **FIRED** in the battery's runs (the headings are present in `summary_text`, see 2a).

---

## [Analysis Brief]

### Ground actually read (first-hand)
- Pinned substrate `/root/workspace/repos/hermes-agent_battery` @ `a996d4ad30` (= the battery's substrate pin, PROBE-BANKS-20261106). File: `agent/context_compressor.py`.
- Ladder run JSONs and `report.md` at `/root/.hermes/cache/scratch/pr1-rotation/ladder-results/`.
- `krecency/RESULTS-{RETENTION,SEAMMECH,ANCHOR,INTENT,AGE}.md`, `krecency/results/{anchor,intent}.csv`, `SEAM-INTEGRATION-20261106.md`, `PROBE-BANKS-20261106.md`, `RESULTS-E3-CONTINUATION-20261106.md`, `NETWORK-LINE-ANCHORCHAIN-20261106.md`, `rungs/fixture-deep-compaction-real.json`.
- Not reachable or not found: no generator script exists for `krecency/results/{anchor,intent}.csv`. Commits `cf922040eb` and `d7cf7ba1ba` each add only the RESULTS doc plus the CSV (`git show --stat`). `git grep` finds no `.py` that writes them. 002-lessons was read; its text carries no eviction-and-absorption entry (the brief names one; none was found → CREATOR-GAP, not filled).

### Code facts [1st], `agent/context_compressor.py` @ a996d4ad30
- **C1** `:1045` `_build_anchor_index`. `:1047` user turns pass through `_typed_user_text`; **all roles' string content is harvested**. `:1053–1061` per-pattern `counts` and `last_seen`. `:1064` `ranked = sorted(counts, key=lambda v: (-counts[v], -last_seen[v]))[:cap]`. `:1066` stops at `_LEAN_ANCHOR_BUDGET_CHARS` (`:1030` = 7_000).
- **C2** `:1031–1039` `_ANCHOR_PATTERNS` = PRs/issues, commits, branches, files, errors, handles, urls only. **There is no timestamp, session-id, model-name, or null-literal pattern.**
- **C3** `:956` `_build_verbatim_user_section`. `:961` skips any non-user role. `:932` budget 24_000 chars. `:933` per-message cap 4_000.
- **C4** `:344–348` `_fresh_compaction_message_copy` = `msg.copy()` plus a pop of `_DB_PERSISTED_MARKER`, nothing else.
- **C5** `:3669–3680` `_augment_summary_lean` appends the anchor, user-verbatim, and recovery sections in lean mode (`:3671`), each only `if heading not in summary` (`:3678`).

**Correction to the record (disconfirm-first).** SEAMMECH and SEAM-INTEGRATION [2nd] say the cap race evicts the tiny+old anchors and that the fresh-copy "drops sidecar ordering hints". At the pin, both are mis-aimed:
1. Cell A's anchors (`2026-10-07T12:33:05`, `session_20261007_123305_f3465b`, `control-model`, `truncated_to: null`) match **no** pattern in C2, so they never enter the race. The loss is **pattern-blindness**, not cap-eviction. The caps (40–120 per class) are rarely binding on a 59-message session.
2. Worse, those four Cell A literals live in the fixture's **metadata** (`rungs/fixture-deep-compaction-real.json:3,4,6,7`), not in `messages` (from `:24`; user open at `:27`). The compressor never sees them. Those probes (`recall-session-identity`, `decision-model-pin`) test facts outside the compressed region, so no reservation could lift them. They must be **excluded** from the arm's success signal. This is Seam S2.
3. C4 strips one persistence marker only. It is not an ordering-hint channel. It matters for the design only as a constraint: a reservation must live in the summary text, not in a message sidecar key.

### The real decision losses are phrase-class, not literal-class [1st]
The debug fixture's (`debug-session-feishu-id-model`) failing probes expect **phrases**:
- decision-core (`run-1.json:161–164`): `"technically valid"`, `"correct"`, `"open_id is app-scoped"`
- next-action (`:184–188`): `"close the PR"`, `"implement ourselves"`, `"cleaner"`, `"less complex"`
- scope (`:208–212`): `"use union_id"`, `"or user_id"`, `"canonical identity"`, `"cross-app stable ID"`

`open_id is app-scoped` **does** survive into `summary_text` in run 2 (line 10 hit ×4) and run 3 (line 10). Yet the decision-core answer is `""` in all three runs (`run-{1,2,3}.json:158` region, `"answer": ""`). So for decision-core, survival in the summary is necessary but **not sufficient**: the answer is empty. This is Wall W2.

The debug summary's Anchor Index carried only `urls:` (run-1 summary_text tail). No phrase-class verdict survived as an anchor, because C2 has no class for it.

---

## (1) THE NEGENTROPY BUDGET — PARTIALLY-SHAPED

**Definition:** the negentropy budget N is the smallest ordered set of verbatim strings from the compacted region whose survival is enough for the continuation probes to clear 3.0. Each class is weighted by its measured deficit w = (3.0 − baseline median).

| order | class | example bytes | weight source A: ladder `report.md` [1st] | weight source B: E-3 / krecency CSV [2nd] | where it lives |
|---|---|---|---|---|---|
| 1 | decision-core verdict | `open_id is app-scoped`, `technically valid` | 3.0 − 0.83 = **2.17** | 3.0 − 0.00 = 3.00 | assistant turns |
| 2 | next-action / forward-intent | `close the PR`, `implement ourselves` | 3.0 − 0.00 = **3.00** | 3.0 − 0.67 = 2.33 | assistant turns |
| 3 | scope boundary | `use union_id`, `canonical identity` | 3.0 − 0.00 = **3.00** | 3.0 − 1.00 = 2.00 | assistant turns |
| 4 | clock and exec-time anchors | the scouts' execution time | 3.0 − 1.00 = **2.00** | 3.0 − 0.17 = 2.83 | user and assistant |
| 5 | recall anchor | `same user has different Open IDs` | 3.0 − 2.33 = 0.67 | 3.0 − 2.00 = 1.00 | tool and assistant |

**Order rationale:** decision-core comes first despite its lower weight under source A, because next-action and scope are *derived from* it. The expected next-action is to close the PR and implement it ourselves; that follows only once the claim is valid but the scope is overbuilt (`run-1.json:136–141`).

**Cost ceiling [2nd]:** about 240 tokens covers the derivations, time-anchor, and forward-intent blocks (RESULTS-INTENT cost-line), against 26 tokens for the 26-literal latch (SEAM-INTEGRATION) and 3 tokens at the death-cell (RESULTS-RETENTION).

**Seams named, which is why this is only PARTIALLY-SHAPED:**
- **S1:** the two weight sources disagree. E-3's medians (0.17 / 0.00 / 0.67 / 1.00 / 2.00) match `krecency/results/anchor.csv:2`, which has no generator in the tree. The ladder's own medians are 1.00 / 0.83 / 0.00 / 0.00 / 2.33. **Source A is the receipt of record** until the CSV's provenance is shown.
- **S2:** Cell A's identity and model probes are outside the region (see above). Excluded from N.
- **S3:** the class boundary between a literal and a phrase is not yet operational. The proposed rule is below in 2b.

## (2) THE VERBATIM-ANCHOR PROMOTION — DESIGNED

### 2a. What fires today [1st]
- `report.md` and run `summary_text` contain `## Anchor Index (mechanically extracted, exact)` and `## User Messages (verbatim, newest first)` (scouts run-1 line 10).
- The lean path is live (C5). The gap is not wiring. The gap is what the two builders admit: C2 is pattern-blind to class 1–4 strings, and C3 is user-only.

### 2b. The mechanism (shape only; the wiring is the head's next fire)
A third tier, **`_build_reserved_anchor_section(turns)`**, is appended through the same `_augment_summary_lean` tuple (C5, `:3673–3676`) under its own heading `## Reserved Anchors (verbatim, order-bearing)`. Re-injection is therefore post-summary and idempotent, using the `:3678` heading guard. No sidecar keys are used, so it survives C4 by construction.

**Selection rule (deterministic, LLM-free, same family as C1):**
1. **Scope:** assistant **and** tool turns, plus user turns already outside C3's budget. This closes C3's `:961` gap.
2. **Candidates:**
   - (i) single-occurrence literals from new patterns C2 lacks: ISO timestamps `\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?`, cron and time-of-day, `session_[0-9_a-f]+`, `key: null|true|false`.
   - (ii) **forward-intent and verdict lines**: whole sentences containing a modal or decision cue (`next|we should|will|plan|verdict|correct|valid|wrong|instead|scope`), capped at 200 chars each.
3. **Rank:** invert C1's key for this tier: `(counts[v] == 1, last_seen[v])`. Single-occurrence and old literals rank *first*, because the cap race is exactly what loses them (SEAMMECH E4 [2nd]: tiny+old 17/21 lost).
4. **Promotion from C1 (the brief's counts / last_seen → verbatim):** any C1 value that was cut at `:1064` with `counts[v]==1` moves to this tier, with C1's output unchanged. C1's `counts` and `last_seen` dicts are the input. Promotion is a set difference (harvested minus ranked).
5. **Budget:** a hard cap of 1,000 chars (≈ 250 tokens, matching the 240-token receipt). Fill in budget order 1→5 from section (1).

### 2c. Success signal (measurable, pre-registered)
- **Fixture:** `debug-session-feishu-id-model`, 3 runs, same compressor and judge as `summary.json` (`deepseek/deepseek-v4-flash-0731`).
- **PASS:** `decision-core-claim-validity` and `continuation-next-action` each have median ≥ 3.0, and `feature-impl-context-priority` holds at ≥ 4.5 with no new misses (the control).
- **Mechanism check (judge-free):** every `expected_facts` phrase for those two probes appears verbatim in `summary_text`.
- **Falsifier:** the phrases are present in `summary_text` but the median stays below 3.0. That would prove the loss is W2 (answer suppression), not order loss, and the promotion is the wrong lever.

## (3) THE RETENTION-REWARD SCALAR — MEASURABLE, one-anchor case

**Definition (smallest reservable unit):** for a probe p with expected facts F_p and compressed summary S, a fact f is *kept* when it occurs verbatim in S.

- Per-probe keep-rate: k_p = |{f ∈ F_p : f ⊂ S}| / |F_p|. This is deterministic and needs no model.
- Retention reward: R = Σ_p w_p · k_p / Σ_p w_p, using the section (1) source-A weights.
- Order-validity term (the negentropy proper): V = corr(k_p, overall_p) across probes and runs. A keep only counts as order if a kept fact predicts a scored answer.

**Data source [1st]:** every run JSON already carries `expected_facts`, `answer`, `overall`, and `compression.summary_text`. R is computable today from the 15 staged files, with no new run needed.

**Walls:**
- **W1, judge coupling:** the compressor and the judge are the same model (`summary.json`). R's k-term is judge-free. V inherits the judge.
- **W2, empty-answer confound [1st]:** the `"answer": ""` counts per file include debug 2 / 5 / 4, deep-compaction 3 / 3 / 3, high-density 4 / 5 / 6, and control 1 / 1 / 1 (git grep -c). The summary's handoff preamble instructs "Do NOT answer questions… wait for a new user message" (debug run-1 line 10). Empty answers score 0 regardless of retention, so V is understated until probe answering is separated from the handoff guard.
- **W3:** Cell A is outside the region (S2) and Cell B is not compressed (63633→63633, `report.md`). The scalar is undefined on both rung cells and must be computed on the three suite fixtures only.

**What would settle the full scalar:** one re-run of the debug fixture with probe answering isolated from the handoff guard. If V > 0 there, R is a keep-reward. If V ≈ 0, retention is not the binding constraint.

## (4) THE RIPPLEMEM BORROW — PARTIAL

- **What the record says [2nd]:** RippleMem is cue-conditioned completion, mapped to the *read path*: auto-routing a `read` request by cue (NETWORK-LINE-ANCHORCHAIN:88–93). It is "not yet in the running build" (same, :93), and there is no implementation in the study tree (RESTORE-EVIDENCE:31, "named candidates (not yet implemented)").
- **Fit:** this arm needs a *write-time* choice of what to keep. Cue-conditioned completion is *read-time* recovery. They are complementary, not substitutes. The substrate already has a read-time hook: `_build_recovery_footer` (`:986–1000`) names `session_search(query='<keywords>', session_id=…)`.
- **The seam (nameable):** each reserved anchor from 2b becomes the **cue key** for a RippleMem-style completion against `session_search`. The reservation guarantees that the cue survives. The completion recovers the context around it. This is feasible on existing surfaces with no new store.
- **Not borrowable:** RippleMem's behavior-memory mechanics themselves. No source code or paper text is staged on the branch, and this lane will not invent them (CREATOR-GAP).

## (5) SEAMS FOR THE ADJUDICATION LEG (the blind second base)
1. **S1:** do E-3's baseline medians derive from any run, or only from `krecency/results/anchor.csv`, which has no generator? Re-derive them from the ladder JSONs.
2. **S2:** confirm that Cell A's A4–A8 literals are in fixture metadata only, not in `messages`, and so outside the compressor's input.
3. **C2 claim:** confirm that no `_ANCHOR_PATTERNS` entry matches ISO timestamps, session ids, or `key: null`, and that the cap at `:1064` is therefore not the binding cause for those classes.
4. **W2:** is the empty-answer rate driven by the handoff preamble or by the probe harness? This decides whether any retention arm can move the decision-core median.
5. **2b rank inversion:** does reserving single-occurrence old strings flood the 1,000-char tier on a long session? Test on `feature-impl-context-priority`, where the control must hold.
6. **002-lessons:** the brief cites an eviction-and-absorption law; this lane did not find one. Locate it or mark it CREATOR-GAP.

## [Recommendation / Action Plan]
**One reversible next action:** compute R (section 3, the k-term only) over the 15 staged run JSONs. This is read-only and judge-free.
- **Success:** a per-probe k_p table showing k ≈ 1 for decision-core's `open_id is app-scoped` with answer `""`, which confirms W2, and k = 0 for the next-action and scope phrases, which confirms the promotion's target.
- **Then:** the head wires 2b behind the lean mode guard and re-runs the debug fixture against 2c.

## [Artifact]
`studies/rfc-143379-rig/NEGENTROPY-ARM-20261106.md` on `study/rfc-143379-rig-20261105`.

the gate: nothing public without the user's word
