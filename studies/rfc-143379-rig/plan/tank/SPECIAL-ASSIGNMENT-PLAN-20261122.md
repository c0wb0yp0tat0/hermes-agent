# SPECIAL-ASSIGNMENT-PLAN-20261122 — the xngg1021-guidance application to the pilot substrate (the think-tank + LP + SME ACES team shape)

*PLAN (SOLAR) · the nitty-gritty · the under-pursued portions of comment 6401350441 applied to the subjects' matrix (qwen free primary / deepseek / luna / Nemo) · the runner matrix's legs (pve1-avrea-parallel / p0tat0 / c0wb0y / cloud) · the sanity's gates (STEPFUN) · run in parallel with the main mission (the settlement · ARM 5 · the staged 6/7), one lane per seat, the smart parallelism's sequencing; upon this assignment's conclusion its outputs FOLD INTO the main mission's loop with no derail, no skew.*

---

## I. THE ANTI-FLATENING DEPTH LEDGER

The plan's PRIMARY purpose is that NOTHING about our methods and the complex fleet is flattened: the methods' depths and the fleet's complex truth are CARRIED, never genericized. A line that genericizes a method or a fleet mechanic is a FLATTENING = a finding, flagged in the record.

### I-A. The methods' depths (preserved, never genericized)

| # | Method | Preserved depth | A flattening (finding) if it happens |
|---|---|---|---|
| M1 | The **copycat transport's** full chain | `sentinel-done` → `content-continuation` → **write-window read-gate** → `emission-format` parser → **8192-cap** → `429-backoff`. Every leg is intact; the read-gate must survive any copycat reuse, not collapse to a "reuse the harness" blur. | "Just reuse the copycat harness" — a blur that drops the read-gate and the 8192-cap. |
| M2 | The **harness's write-window read-gate** | Write → read-back in one window with the full terminal attestation (`success/done/target/usage/entry_count/message/note`), equality resolution through ONE structural resolver (whole-anchor resolution), the read-back contract on the single-op path (the 3 blind spots: `add` returns None, `remove` substring-vs-exact, `patch` substring-vs-sibling), the batch path as the single authoritative gateway (memory_tool.py:331–369 → `store.apply_batch` under the store lock). | "Read back what you wrote" — a genericization that drops the terminal attestation and the structural resolver. |
| M3 | The **envelope's clauses** | The fair-share envelopes per runner, the **one-lane-per-seat law** (a double-booked seat 429s both), the flagship windows FIRST on the heavy arms (the settlement on qwen's LAST day; ARM 4 on hy4's week), the runners' legs ride the fills/patrols' queue state file, the wave's legs keep priority, the secondary seats carry audits/batteries/mechanical legs, the beam NEVER rides the main fleet, the seat-truth probe at every fire (the responding model MUST match the requested pin — a bare-name 404 is the catalog-literal class). | "Distribute the load" — drops the one-lane-per-seat law, the measured envelopes, and the fire-time seat-truth probe. |
| M4 | The **LP/think-tank subtleties** | Customer Obsession (the plan serves 3oltan-seo's pilot's substrate — the anchor-full wall, measured at 3 844/4 000 = 96% pre-consolidation on 29.10); Ownership; Invent and Simplify (simplify the APPLICATION, never the methods); Are Right A Lot (disconfirm every plan-line before landing it); Bias for Action; Dive Deep (the current-state verification, not the comment's 10-25 snapshot). | "Be customer-obsessed / be lean" — adjectives that flatten the pilot's wall and the measurements. |
| M5 | The **reload-marker's coverage asymmetry** (Portion 1) | The skill_view wire is VERIFIED in local main: `context_compressor.py:1722–1729` (`_sum_skill_view` + ghost-skill defense, `SKILL_PRUNED_MARKER_PREFIX`), `context_compressor_tail.py:11–12, 46–107` (`demote_stale_tail_tools` special-cases `skill_view_names_by_call_id` so a demoted `skill_view` body appends `[SKILL_PRUNED]` and tells the model to re-call `skill_view(name=...)` — #32106). The MEMORY-doc read class's equivalent wire is the GAP to carry, never close-by-genericization. | "Just wire memory the same way" — a genericization that drops the doc-target from the demoted summary and the session_search footer's role. |

### I-B. The fleet's complex truth (preserved, never genericized)

| # | Fleet nuance | Preserved depth | A flattening (finding) if it happens |
|---|---|---|---|
| F1 | The **runners' matrix's mechanics** | `pve1-avrea-parallel` (THIS host, self-hosted = unmetered), `p0tat0` (Linux 241, c0wb0yp0tat0), `c0wb0y` (Windows 241, privileged-seat class), `cloud` (the hosted ubuntu-latest, the public-wave legs, the platform's queue's verdicts). Per-runner legs, mirrors' re-arm, the refspec main-only, the stale-push hazard on the shared branch `study/rfc-143379-rig-20261105` (ls-remote before fold), the beam `reflection/beam-1.0-501b-a23b` (Kenari — select legs only, NEVER main fleet, its name NEVER on a pilot-facing surface). | "The fleet is 4 runners" — a count that drops the host inheritance, the legs' assignment, the stale-push hazard, the refspec, the beam reservation. |
| F2 | The **seats' windows** | Primary flagships: qwen4-max:free (LAST DAY — the settlement's route) · hy4-flash:free (the week — ARM 4's route). Secondary: solar-mini4 · longcat-2.5 · step-5-preview (429 at last probes — re-probe per ring). Other keyless: probed at the ring when named classes exhausted. The flagship windows first on the heavy arms. | "Every seat is the same" — a genericization that drops the last-day urgency, the windows, the per-seat credentials. |
| F3 | The **one-lane-per-seat law** | A doubled-ticketed seat 429s BOTH. The seat-truth probe at every fire: the responding model MUST match the requested pin — a bare-name 429/404 is the catalog-literal class, not a substitute. | "Multiple lanes per seat are fine" — a flattening that breaks the fair-share envelopes and the fire-time truth. |
| F4 | The **fair-share envelopes** | Per runner: the ring's economy is measured, not assumed; a double-booked seat 429s both; the idle fills fill the gap; the beam rides select legs only. The registry's per-runner envelopes are measured at the writing and appended to as the phase lands. | "The envelope is a target share" — a genericization that drops the live per-runner measurement and the fire-time seat-truth probe. |

---

## II. THE THREE UNDER-PURSUED PORTIONS × THE SUBJECTS' MATRIX

### Portion 1 — The reload-marker's coverage asymmetry

**The current state (verified at the arm, main's truth today, not the comment's 10-25 snapshot):**
- VERIFIED the wire that EXISTS: skill_view in the lean-mode demotion path (`context_compressor_tail.py:46–107` special-cases `skill_view_names_by_call_id`, appending `[SKILL_PRUNED]` + the `reload with skill_view(name=...)` instruction; the body-level glue is `context_compressor.py:1722–1729`).
- VERIFIED the GAP with the receipt: the demoted `memory(action="read", doc=...)` result carries NO equivalent wire. Repo grep of `agent/context_compressor.py` shows `_TOOL_RESULT_SUMMARIZERS` maps `"memory": _sum_template("[memory] {action} on {target}", action="?", target="?")` (line 1970) — a generic 1-line summary whose `{target}` defaults to `"?"` (the `doc=` target is dropped) plus `_demote_tool_result_at` (`context_compressor.py:3184–3212`) rewrites it in place with no reload marker, no session_search footer, no @doc re-read guidance. `demote_stale_tail_tools` (`context_compressor_tail.py:56–85`) has no memory special case — only `skill_view`.
- The stale tool-result summary template (`_summarize_tool_result` → `_summarize_tool_result_unguarded` → `_TOOL_RESULT_SUMMARIZERS.get(tool_name)`) has no per-tool recovery path for memory.

**The under-pursued application (per subject, the substrate's read-design, invented + simplified against the exposure):**
- The substrate's chain-reads (the big segments: segment 002 at 371KB) are pulled as tool-results into long contexts. Each subject's read-design: (a) **lean-first reads** — prefer 1,500-chars-or-less print/read tool results so they don't trip `_LEAN_TAIL_DEMOTE_MIN_CHARS = 1_500` in `demote_stale_tail_tools`; (b) **receipted byte-verification** — after any demotion of a memory-read result, verify the doc bytes by re-reading the target (`memory(action="read", doc="...")`), never by trusting a generic `[memory] read on ?`; (c) **the re-read discipline** — after ANY compaction, re-anchor + re-read the owning segment, never the summary (the #116673 two-pass cadence inherited from the pilot kickoff: the anchor is the pointer, the doc is the detail, pass one the pointer, pass two the detail).
- The first verification this team makes (live, before inventing): grep `context_compressor.py`'s handling of the memory-read tool results — DONE above, receipt in §VI; the rig-side mitigation the pilot substrate carries even before the platform's wire lands: fold-time/read-time rule — on a demoted memory-read stub, the agent MUST attempt the re-read of the named doc target, falling back to `session_search(query=..., session_id='...')` only when the re-read itself is demoted.
- The hot-anchor sizing discipline is the sibling lever the pilot carries (Portion 2): the standing invariants that would live at `MEMORY.md` position 0 are sized into the hot tier first, and only episodic/long-tail reference spills into `@doc:`.

### Portion 2 — The hot-anchor sizing's economics

**The current state (verified, #5320's measurements, cited in the RFC record):**
- #5320 = 4,200 AWQ sweep runs + 824 official `Qwen/Qwen3.8-27B-FP8` replication runs across 7 interference regimes (5,024 controlled runs).
- At the `2,200 / 1,375` default: `MEMORY.md / USER.md` covered **35% of facts / 22.2% of preferences**.
- Raising the position-0 hot tier to `3,750–5,000 / 2,350–3,000` chars (e.g., `4,000 / 2,500`, which @learn2000 corroborated in production on #5320) lifted fact coverage to **60%–80%** while maintaining **100% behavioral accuracy, 100% tool accuracy, and 0% spurious tool calls** on FP8.
- Live datapoint from the pilot's substrate: the anchor-full wall (3 844/4 000 = 96% on 29.10), post-consolidation 29.10 = 2 930/4 000 (73%), now 30.10 = 3 376/4 000 (84%, 24 entries). The never-cram law's residue: position-0 standing invariants must stay in the hot tier; the never-cram rule means every compaction re-reads the anchor + the owning segment.
- NoLiMa (ICML 2025, arXiv:2502.05167) — 11/13 models drop below 50% of baseline at 32K once surface lexical matching is removed; offloading standing rules that fit inside a ~4,000-char hot anchor out to cold `@doc:` files exposes them to NoLiMa-style lexical-mismatch misses on `action="read"`.

**The under-pursued application (per subject, the substrate's own position-0 experiment):**
- The substrate's OWN anchor's sizing discipline measured: what CAN live at position-0 with coverage intact given the platform's cap. The pilot's wall profile: MEMORY sits at ~96% of a 4,000-char budget, most of it cold procedural detail. The measured layers' priority (not assumed): the pilot's run is a live measurement, and the per-subject discipline is the same: each subject's position-0 hot tier is set, read, and measured at the ring; the layers' priority is measured, not assumed — the anchor's 96% squeeze is the live datapoint the plan measures against.
- Application to each subject (the subjects' matrix: qwen free primary / deepseek / luna / Nemo): the hot-tier sizing is a per-subject experiment — qwen free (primary) carries the settlement route; the hot tier is sized to the measured coverage floor, and the cold `@doc:` segments (segment 002 = 371KB) are read as tool-results into long contexts only when they can't fit in the anchor.

### Portion 3 — The long-context lexical-mismatch exposure (NoLiMa-validated)

**The current state (web-verified; cited in the RFC record):**
- NoLiMa (ICML 2025, arXiv:2502.05167): 11/13 models below 50% of baseline at 32K once surface lexical matching is removed (verified web-verified).
- The chain-reads' exposure: the pilot substrate's docs (the big segments: segment 002 at 371KB) pulled as tool-results into long contexts.

**The under-pursued application (per subject, the substrate's read-design, invented + simplified):**
- The substrate's read-design against the exposure: (a) **lean-first reads** (Portion 1a) so the long-context pull stays bounded; (b) **receipted byte-verification** — after any long-context read of a chain doc, verify the bytes by re-reading the named target, never by trusting a summary; (c) **the re-read discipline** — after any compaction, re-read the anchor + the owning segment.
- Per subject: qwen free (primary) carries the settlement route and the anchor sizing; the long-context exposure is measured per subject at the ring so the read-design's simplification (not the method's) is validated per socket. The chain docs are pulled as tool-results into long contexts only when they can't fit inside the ~4,000-char hot anchor — the standing invariants stay in the hot tier per Portion 2.

---

## III. THE RUNNER MATRIX'S LEGS

| Runner | Machine | Status | Legs (the substrate's plan) |
|---|---|---|---|
| **pve1-avrea-parallel** | THIS host (pve-1) | online · busy=false | the harness's execution legs, the batteries' runs (the A3/WEIGHTS battery probes landed 2026-11-22), the private-repo legs (self-hosted = unmetered) |
| **p0tat0** | Linux 241 (c0wb0yp0tat0) | online · busy=false | the fills/patrols' shared load, the mirrors' re-arm (ls-remote before fold; the refspec main-only; the stale-push hazard) |
| **c0wb0y** | Windows 241 | online · busy=false | the same, PRIVILEGED-seat class |
| **cloud** | hosted ubuntu-latest | the API's legs' queue | the public-wave legs, the platform's queue's verdicts (the seat-truth probe at every fire: the responding model MUST match the requested pin — a bare-name 404 is the catalog-literal class) |

Runner-leg assignment per subject: qwen free (primary) runs the settlement route and the anchor-sizing experiment on the hottest legs first; deepseek / luna / Nemo run the read-design measurements across the batteries. The one-lane-per-seat law: no seat is booked twice; the fair-share envelopes are measured at the ring per runner, not assumed.

---

## IV. THE SANITY'S GATES (STEPFUN — the tail)

The executor's outputs' verification per the dry-run ruler; the seat probed at the fire (a 429 = the slot's report, not a substitute). The gates, per leg:

| Gate | What it checks | Who passes it | Receipt |
|---|---|---|---|
| G1 — the memory-read reload gate | A demoted `memory(action="read", doc=...)` result carries a reload path that points at re-reading the named doc target (not `session_search`), or the fold-time/read-time rule is visibly applied. | The plan's runner lanes (pve1-avrea-parallel first) | §VI receipt — the gap is closed at the substrate, not in the platform |
| G2 — the anchor-size measurement | The substrate's position-0 hot tier is sized, measured, and the coverage floor (≥ the measured 60–80% plateau on the pinned subjects) is reported per subject. | The weights battery (A3 probes landed) | §II.2 measurement per subject |
| G3 — the NoLiMa long-context gate | The chain-reads (segment 002 = 371KB) are read-design'd for lexical-mismatch exposure; the lean-first reads + receipted byte-verification + re-read discipline are present in the executor's logs. | The executor's logs + the runner lanes | §II.3 per-subject read-design |
| G4 — the fair-share fire probe | At every fire, the responding model matches the requested pin (one-lane-per-seat law); a bare-name 404/429 is the catalog-literal class. | The seat registry's per-runner envelopes | §III fire probe |
| G5 — the fold-in | The assignment's outputs fold into the main loop with no derail, no skew; the plan's order intact (SOLAR → LONGCAT → STEPFUN → FOLD-IN). | The main mission's order (protect) | §I.A.4 · §II |

---

## V. THE NOT-FOR-ITS-SAKE GATE — every planned step names its LIVE TARGET

An output that cannot name its LIVE TARGET (the real seam it closes on the rig or the pilot's substrate) is a FINDING, flagged in the record — never a shipped artifact. Every plan-line below names its target:

| # | Plan-line | LIVE TARGET (the seam it closes) |
|---|---|---|
| P1 | Grep `context_compressor.py`'s handling of the memory-read tool results (the FIRST verification this team makes) | **The demoted memory-read recovery path** — the missing reload wire for `memory(action="read", doc=...)` (segment 002 → the chain-reads' demote-stub) |
| P2 | Design the rig-side mitigation (fold-time/read-time rule the PILOT substrate carries before the platform's wire lands) | **The demoted memory-read stub** — the `@doc:` re-read vs `session_search` seam, now carried by the pilot substrate |
| P3 | The substrate's read-design (the lean-first reads, the receipted byte-verification, the re-read discipline) | **The NoLiMa long-context lexical exposure** — the chain-reads' demote-stub and the long-context pulls (segment 002 = 371KB) |
| P4 | The anchor's sizing discipline measured per subject (the position-0 experiment) | **The hot-anchor coverage squeeze** — the anchor's 96% squeeze, the never-cram law's residue, the #5320 60–80% plateau |
| P5 | The runner-leg assignment + the fair-share fire probe | **The one-lane-per-seat law + the fair-share envelopes** + the seat-truth probe at every fire |
| P6 | The fold-in into the main loop (no derail, no skew) | **The settlement · ARM 5 · the staged 6/7** — the main mission's order, protected |

---

## VI. THE CURRENT-STATE VERIFICATION'S RECEIPTS

The current-state verification, not the comment's 10-25 snapshot — the receipt for the first step:

1. **Portion 1's first verification — the memory-read tool results' handling (live grep, `agent/context_compressor.py` in local main):**
   - `context_compressor.py:1722–1729`: `_sum_skill_view` + ghost-skill defense (`SKILL_PRUNED_MARKER_PREFIX`) — VERIFIED, the wire that EXISTS.
   - `context_compressor.py:1970`: `_TOOL_RESULT_SUMMARIZERS` maps `"memory": _sum_template("[memory] {action} on {target}", action="?", target="?")` — the demoted memory-read result is a generic `[memory] read on ?` whose `{target}` defaults to `"?"` (the `doc=` target is dropped), with NO reload marker, NO `session_search` footer, NO `@doc:` re-read guidance.
   - `context_compressor_tail.py:46–107` (`demote_stale_tail_tools`): special-cases only `skill_view_names_by_call_id` — no memory special case.
   - `context_compressor.py:3184–3212` (`_demote_tool_result_at`): rewrites the old tool-result bodies in place with the generic summary — no recovery path for memory.
   - Conclusion: the gap's current state on the local main = the MEMORY-doc read class has NO equivalent wire for the reload-marker's coverage asymmetry. The plan carries the rig-side mitigation (the fold-time/read-time rule) on the PILOT substrate, ahead of the platform's wire.

2. **Portion 2's current-state measurement (verified, #5320, cited in RFC-143379-RECORD-20261111.md:398–401):** `2,200/1,375` → 35%/22.2% coverage; `4,000/2,500` → 60–80% coverage with 100% behavioral accuracy + 0% spurious tool calls (FP8). Live datapoint: the pilot's wall 3 844/4 000 = 96% pre-consolidation (29.10) → 3 376/4 000 = 84% (30.10). NoLiMa (ICML 2025, arXiv:2502.05167) — 11/13 models below 50% of baseline at 32K once surface lexical matching is removed.

3. **Portion 3's current-state exposure (verified):** the chain-reads (segment 002 = 371KB) as tool-results into long contexts; NoLiMa-validated.

---

## VII. OPEN-ITEMS

| # | Open item | Status | Receipts |
|---|---|---|---|
| O1 | The platform's `memory(action="read", doc=...)` reload wire (context_compressor_tail.py) — carried by the pilot substrate FIRST via P2/P5; the platform wire lands when it lands (a QUESTION, not a blocker) | OPEN | §VI.1 receipt; §V P1/P2 |
| O2 | Per-subject measurements of the anchor's sizing discipline (the position-0 experiment) on deepseek / luna / Nemo — the pilot's live wall profile is the measurement source | OPEN | §II.2 · §IV G2 |
| O3 | The long-context read-design's per-subject validation on the 371KB segment 002 pull | OPEN | §II.3 · §IV G3 |
| O4 | The runner-matrix legs' measured fair-share envelopes after the A3/WEIGHTS battery probes land | OPEN | §III · §IV G4 |
| O5 | The main mission's settlement · ARM 5 · staged 6/7 order — the plan runs alongside and folds in; the fold-in is a STEPFUN gate, not skipped | OPEN | §IV G5 · §I.A.4 |

---

*THE ARMAMENT LINE: think-tank (the spine) + the SME substrate skills (krecency-instrument · aces-harness-probes where apt) + investigation-documentation; name-and-refuse the rest. THE WALL CLAUSE: a non-reproduction is a QUESTION with receipts. THE PLAN GUARD: the main mission's order is not altered — this runs alongside and folds in. HARD LINES: nothing public · RFC #143379's upstream issue QUIET · no installs · write ONLY under studies/rfc-143379-rig/ · the subjects' access = the fleet's existing channels ONLY · all LOCAL reads via read_file · NEVER push · never checkout/stash/rm. THE LP COMPACT: Customer Obsession (the plan serves 3oltan-seo's pilot's substrate) · Ownership · Invent and Simplify (the plan simplifies the application, never the methods) · Are Right A Lot (disconfirm every plan-line before landing it) · Bias for Action · Dive Deep (the current-state verification, not the comment's snapshot) · Deliver Results. THE EMISSION CONTRACT: exit 0 = the deliverable at the named path with the plan + the targets + the receipts inside. THE TERMINATION CHECK: one review round; no measurable change x2 -> PARK. THE ANCHOR: MEMORY.md + USER.md (the register + the GATE LAW's final form). SELF-FIRE: complete, commit, report — never wait.*
