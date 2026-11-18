# NIGHTSHIFT-PLAN-20261118 — the merged plan
compose seat: tencent/hy4-flash:free · scribe-cell: rig-nightshift-reload · RFC #143379

## The mission
Nous never restores reads. The pilot kit must therefore serve its own reads from its own substrate — every artifact's full bytes already sit in the scribe's cells, the doc-chain holds the durable record, the local surface can page. Our first word is ours: we innovate the read boundary first, the node that starved seven lanes, rather than wait on a provider that will not return. The green light stands for the whole mission. The only gate: nothing public beyond gists and PRs — no comment posts, no upstream opens. Everything else fires.

## THE READ-SOLUTION
Four layers, each with a writable surface, a byte-verification and a named failure shape. No silent failure anywhere; every failure escalates, never downgrades evidence.
1. **Local paged read** — first touch; offset/limit with head/tail hint. Failures `TRUNCATE` / `ABSENT` (silent truncation is the worst class) fall through.
2. **Scribe-cell fallback** — on truncate/absence the wired round-trip runs: `save_memory(full bytes)` → `get_memory` → page locally with the same contract → byte-verify each page boundary against the originals → serve. Failures `NO-CELL` / `CELL-UNREADABLE` / `CELL-BYTE-MISMATCH` escalate to Layer 3, never serve a partial.
3. **Doc-chain cold start** — anchor, segments, receipts, all local, append-only, verified at write. Failures `CHAIN-UNVERIFIED` / `RECEIPT-NOMATCH` escalate to the decks.
4. **Seam decks** — 014-style session-start handoff built from verified chain bytes; least-trusted, entry point not proof. Failures `DECK-BUILD-FAIL` / `HANDOFF-GAP` never stall — escalate to the full-opus runners.
Order 1→2→3→4. Two-way door `READ_SUBSTRATE_MODE` (env/config): `canonical` (off; rollback; default until the wire lands) / `cells` (default once wired) / `chains` (doc-chain + decks); config is overridable at runtime; rollback = set `canonical`, confirm no cell call this cycle, delete the entry. The substrate substitutes for a missing restore, never for a missing provider.

## THE BATTERY
Four legs, provider suppressed, each with a kill switch (the result that falsifies the claim):
- **LEG-1 cells-only** — list cell, page it, sha256 vs recorded digest, provider-call counter 0; 20/20 verified. Kill: one artifact whose bytes exist only on the provider side.
- **LEG-2 cold-start** — fresh session, read 014 handoff + mission map + chain from cells, emit a note naming STEER-1..8 and the loop state. Kill: cannot name the stage without provider context.
- **LEG-3 truncation-fallback** — plain read of a large artifact → detect short count/hint, fall back to cell, full bytes, digest green, latency ≤2 read windows. Kill: truncated body accepted as complete.
- **LEG-4 write-path** — write while provider suppressed → assert fires (hash→cell→verify), session throw, re-read persisted, digest green. Kill: write blocks awaiting provider confirmation.
Home: a named runner leg in STAGE 3 (B3), executed every STAGE 4 loop cycle (L1) plus a standing nightly sweep; artifacts `BATTERY-LOG-<date>.md`, the F1 ledger, the byte-integrity receipt. F1 pass rate = green legs /4 with per-leg verified/tracked rows; no-improvement = two consecutive cycles with zero pass-rate gain → plateau. Two-way door: if LEG-1 fails, drop to the doc-chain/gist layer and re-run; the battery retires only after F1 plateaus twice.

## THE ENVELOPE
**The eight LP lines, with the nightshift slice:** Customer Obsession — the finding serves the collaborator's fleet and the pilot's wall, verdict lands even when the wall is cold. Ownership — the seam is ours until the receipt lands, held through the two-way door and back. **Invent and Simplify (THE WALL CLAUSE, verbatim):** "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised: advance the date, shrink the fixture, invert the condition, construct the minimal case that moves the wall. Never 'not invented here,' never a dead-end report." *Slice:* the re-fire under the two-way door is itself a wall-clause artifact. Are Right, A Lot — seek the disconfirming probe before landing; the 429 receipt is it. Learn and Be Curious — the wall is the lesson's ore (the prior deterministic abort). Bias for Action — the minimal next probe fires without hesitation; write small and early. Dive Deep — quote the lines, count the numbers; every claim traces to the pack. Deliver Results — verdict + receipts land no matter the wall; the artifact exists before the wall retries.

**Mechanism-of-mechanisms spine** — observed substrate: scribe-cell; probe: does it produce a receiptable artifact under the two-way door; verdict ceiling = the artifact's existence (OPEN until it lands). Alternatives, honestly marked:

| Substrate | Probe | Ceiling |
|---|---|---|
| scribe-cell (this lane) | artifact lands before the wall | FIRED if artifact exists at path |
| sentinel-cell (`.sentinel`) | artifact + sentinel pair | ABSENT — no sentinel written |
| verifier-cell (brief-named) | brief + verification body | ABSENT — no verifier pair |
| body-cell (`-body.md`) | standalone body without brief | ABSENT — no body-only artifact |

**Substrates of substrates — cells on the doc-chain on the branch on the gists:** the lane artifacts + LP reference + receipts are the cells; the brief/sentinel lineage (001–014, lessons, handoffs 013/014) is the doc-chain; `study/rfc-143379-rig-20261105` is the branch; the storm-context mechanisms (DISCERN, MemCredit, MAPE, CoMem, Reward-Driven Collider, AskALCF, SELD, Evolving Infra) and the four misc (compile-time gating / stage-decoupled evaluation / validity decay / three-state delegation) are the gists the chain cites but does not embed. **Lens 3's ABSENTs are closed here from the compose's own reads:** the bearings confirm the read boundary as the systemic node, the scribe as read substrate, the two-way door and full-runner doctrine as standing, and the scenario's test as a real cells-only battery; the mission map confirms the three-mission sequence, the scenario (Nous never restores), the contract, the seam, and Amendments 1–4 / the addendum. Both sources were read directly.

## THE SEAM & THE TRIGGER
**Cold start — three-rung ladder, in order:** 014 handoff (where the deck is) → mission map (what the mission is) → steer channel (what changed, latest STEER-8). All local branch artifacts; a throw costs three reads, not a re-brief. **Pointer renewal:** each landing writes its artifact, byte-verifies into its scribe cell, then advances the map's loop-state line to the next stage token — the deck's live pointer, so any throw resumes at the exact stage.
**Fail-safe (nothing stalls; only public writes are an absolute hold):** **AUTO-CONTINUE** — the five lenses + swap-and-enrich + reload compose (STAGE 2 armed on STAGE-1-LANDED); STAGE 3 build + battery and STAGE 4 loops ending on no-improvement-twice; the never-idle runner/fork ensemble; gists and PRs. **HOLD-SAFE** (named auto-path) — public posts beyond gists/PRs → stage text as a private draft row, post nothing; upstream RFC #143379 → stay one-way/quiet, record locally; live-end config changes → document + sandbox-test in a fork; Darkhorse pick/host → park board-ready shapes, fire nothing; any self-imposed gate → fire when ready. **NEEDS-THE-CHAIR** (four true one-way doors, each pre-written as a context/options/recommendation/reversibility/cost packet so an absent chair costs a read, not a stall): re-shape the plan's spine; reverse the public-writes hold or open the upstream RFC; flip the live background-review toggle after sandbox verification; commit Darkhorse spend/hosting.
**Stage-advance watcher — ALREADY WIRED as a live cron** (its job id lives in the head's record). The mission map's loop-state line is the single source of truth; the cron reads this plan's loop-state line each tick and advances only when the prior landing is byte-verified in its cell: `STAGE-2-ARMED`→dispatch, `PLAN-LANDED`→STAGE 3 fire, all six fronts no-improvement-twice→HOLD. Strictly seam-internal: posts nothing public, opens nothing upstream, touches no live config; a present head overrides; re-arming = resetting the token.

## THE FIRE
**STAGE 3 — BUILD (seat / artifact / gate / action):**
- **B1** Wire read-side scribe-cell fallback — kenari beam-1-0 (lead) + solar lane (audit/AoA); `read_fallback.py` + seam-deck entry in `014-handoff`; gate: compile + unit reads return cell bytes when provider absent; land on branch.
- **B2** Enable read-paging contract — longcat lane; `paging_adapter.py` (offset/limit, head+tail, hint); gate: paged reads byte-match cells; merge into read path.
- **B3** Stand up provider-absence battery — stepfun (legs) + hy4 (matrix); `provider_absence_battery.py` + leg manifests; gate: baseline runs all legs; execute baseline, record pass rate.
- **B4** Wire instrumentation F1–F6 — kenari beam audit + cloud Avrea leg; `gauges.py` + cycle readout; gate: one full cycle yields all six readings; enable in every cycle.
**STAGE 4 — LOOPS:** **L1** cycle run (battery+gauges), full ensemble incl. forks → `cycle-NN-report.md`, all six fronts measured, collect-don't-stop. **L2** kaizen/gemba improve the lowest front, reasoning lanes on least-utilized seats, patch + apply note, tests pass no regression. **L3** repeat until no-improvement-twice on all fronts (head, fail-safe only), `loop-ledger.md` per-front deltas, F1–F6 flat two cycles. **L4** one confirmation cycle, Nemo CTO-lens, `confirmation-cycle.md`, no regression → approve apex. **L5** hold at apex + next-mission gate, head, `apex-hold.md`, public writes still gists/PRs only.
**Six fronts / instrumentation & terminal:** F1 read-solution readiness (battery pass rate, cells-only+paged+byte-verified; flat = two cycles zero gain), F2 harness reliability (landing success + ghost rate), F3 fleet utilization (runner idle + fair-share spread + fork-battery cadence), F4 record completeness (untracked/unrowed + cells' byte-integrity), F5 project-layer currency (roadmap/plans vs branch), F6 planning depth (compose-check fidelity). Every front must read no-improvement twice → one confirmation cycle → hold; nothing stops earlier.
**Full-opus utilization:** all runners never idle — self-hosted four + cloud Avrea — fair-share rotation, audit/AoA pinned to least-utilized seats; the fabric's 31 forks fire as the abstract experiment at the highest meters-aware sustainable cadence (never fallback-only), cadence logged into F3/F6; keyless surfaces + kenari dots probe-before-use, no seat idle while a probe is pending. The closing ritual (Nemo CTO-lens + head's no-lens pass → READY/NOT-READY) precedes the fire.

## THE CONFLICTS RECONCILED
- **Battery's home:** the battery lens seats it as a STAGE 3 runner leg with a nightly sweep; the fire lens builds it at B3 (STAGE 3) and re-runs it in L1 (STAGE 4). Resolution: one battery, built in STAGE 3, executed every STAGE 4 cycle plus nightly. Evidence: lens-2 §2 + lens-5 B3/L1.
- **Flag's default:** the read lens says `canonical` until the wire lands, `cells` once wired. These are one two-state door, not a contradiction: canonical is the pre-wire/rollback state, cells the post-B1 state. Evidence: lens-1 §2.2.
- **Trigger's cadence / existence:** the seam lens marked the loop-state watcher ABSENT and designed a 30-minute tick; the operator's standing record says it is ALREADY WIRED as a live cron (job id in the head's record). Resolution: the later operator state governs — treat it as live at 30 minutes (faster than the 3h fleet cycle), lens-4's ABSENT being the earlier design point. Evidence: lens-4 §3 compose mark 4 + brief/head's record.
- **Wall clause:** two carriers exist — lens 1's read-substrate identity ("the kit serves its own reads when the provider never restores") and lens 3's Invent-and-Simplify clause. Both stand: lens 1's is the read boundary's identity, lens 3's is the envelope's verbatim wall clause quoted above. Evidence: lens-1 §3, lens-3 envelope.

## THE OPEN ITEMS
- **Hash choice:** sha256 vs partial-chunk compare for cell↔file equivalence — chosen at the fire; the requirement is equality-of-bytes, not identity-of-hash.
- **Config file shape:** the exact read_file code path and the `READ_SUBSTRATE_MODE` config entry's file-level shape — specified by intent, integrated at B1/B2.
Neither is a placeholder in the plan; both are named decisions reserved for the build.

## THE LOOP-STATE LINE
PLAN-LANDED - STAGE 3 ARMED - the watcher fires the build.

## THE COMPOSE-CHECK TABLE
| # | Mark | Fired / Absent | Evidence line |
|---|---|---|---|
| 1 | Mission, scenario, ours-first, green light, only gate | FIRED | Two-line scenario + innovated-first north + gists/PRs-only gate present. |
| 2 | Four-layer read stack + wired round-trip + two-way door | FIRED | Layers 1–4 with named failures; save→get→page→verify branch; `READ_SUBSTRATE_MODE`. |
| 3 | Battery four legs, kill switches, F1, two-way door | FIRED | LEG-1..4 with falsifiers; x/4 measure + no-improvement-twice + plateau retirement. |
| 4 | Envelope whole; lens-3 ABSENTs closed | FIRED | Eight LP lines + verbatim wall clause + alternatives table + cells-on-chain frame; bearings + map read directly. |
| 5 | Seam ladder, pointer renewal, fail-safe, four chair-packets | FIRED | 014→map→channel; landing-verifies-then-fires; three dispositions with packets. |
| 6 | Stage-advance watcher wired | FIRED | Live cron, job id in head's record, reads this plan's loop-state line. |
| 7 | Fire sequence + six fronts + full-opus | FIRED | B1–B4 seat/artifact/gate/action; L1–L5; F1–F6 terminal; all runners + Avrea + 31 forks. |
| 8 | Executed battery / apex hold | ABSENT (fire target) | Battery is the plan's first deliverable; L3/L5 terminal pending the build. |

## APPENDIX-A (2026-11-18, the CTO-lens's additions, accepted — no-lens pass rendered READY-WITH-NAMED-SEAMS; the fire proceeds)
1. DISK-HEADROOM GUARD AT LOOP-TOP (STAGE 4, each confirmation cycle's top): a beam-audit leg checks df; with ~1 point of headroom + B1/B2 writing, the cycle defers when the 92% guard is within reach. Costed 1 round, slotted L1-loop-top.
2. HANDOFF-RECEIPT ARTIFACT (STAGE 4, the next-mission gate): a one-page receipt (state held, seams open, chair packets unused) closes the fail-safe table's one GAP and gives the apex its payload.
3. FAIR-SHARE TELEMETRY INTO F3 (STAGE 3, B4): wall hits + rotation switches logged into the F3 gauge — tonight's three eaten 429s become a measured signal, not an anecdote.
## LOOP-STATE LINE (updated)
`CYCLE-4-ARMED (the fourth measurement; F1/F3 plateaued, F2/F4 one-flat, F5/F6 moved — the all-six terminal awaits the remaining counters) - the loops run until all six fronts read no-improvement twice; the watcher's next tick sees the exact cycle command.`
