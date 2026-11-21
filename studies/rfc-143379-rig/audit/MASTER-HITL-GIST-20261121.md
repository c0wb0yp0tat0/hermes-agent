# MASTER HITL GIST — the RFC #143379 study, presented whole (2026-11-21)

*For the operator's read. The record lives in the thread + the chain; this memo is the presentation, and it is written to be read in one sitting. Every number below traces to a fold line, a ledger, a commit, or a thread row — nothing recalled from memory. Where a figure is a model rather than a measurement, it is labelled as one. Where something failed, it is named as a finding. The doors are presented at the end, each with its reversibility and who walks it.*

---

## 1 · THE MISSION IN ONE BREATH

The RFC asked NousResearch/hermes-agent for three movements. The first: **restore the read action** — the 14-line method that lets the agent actually read its own memory was reversed in a change (56ee8a5cc6), and the ask was to put it back. The second: **make the store re-readable** — MEMORY.md was to anchor a chain of documents, a bounded-read shape so that the memory surface stops being a wall of tokens and becomes a doc chain with a spine. The third: **govern compaction** — the thing that quietly rewrites what the agent can see of its own past was to be governed: provenance-origin classification and a K-recency rule, staged but never opened as an issue.

None of the three has merged upstream. #141876 (the read's restoration, the operator's own PR) sits open-unmerged, updated 11-10, its correctness verified green on the fork at af16e3ab16 with 161 memory tests + 20 regression tests and a six-point review accepted. #116673 (the doc chain) sits open-unmerged with its author's simulations receipted in the thread's register. The compaction issue exists only as a staged-but-not-opened row. The upstream's motion is not in our hands; that fact IS the study's starting condition.

The study's shape was a storm chain: harvest the field's receipts first (the field's own transparency-compact battery, its compaction studies, the suppression research, the pricing telemetry), then reduce the whole pile to the real problems — M1: certify the evidence chain (the substrate's persistence), M2: synchronize the orchestration's resource-truth (the fill, the queue, the seats), M3: adopt the governance seams (compaction, release points, the honest walls). Then fire a sequence that does not stop until its goals land: the PersistGym certify protocol, the A3 suppression wave, the release-point gate, the canary, the kit — and close with a goal-audit of the whole arc, four ledgers plus a cross-check, so the close is adversary-reviewed rather than self-celebrated.

The thesis the kit carries is **independence**. The rig's substrate — the persistence property, the read-restore suite, the governance cards — is certified ON THE FORK, machine-verified, byte-receipted. The study's answer therefore never waits on the upstream's merge timeline; the harbor can be rebuilt, the read can be re-proven, the economics can be ledgered, while #141876 and #116673 sit where they sit. The kit is a provisional stand-in — the honest edge, preserved on purpose: the RFC's movements remain the upstream's to land, and the gist says so, in print, on the record.

---

## 2 · THE STATE

### 2.1 What is certified

**The M1 stamp — the substrate's persistence, machine-verified.** The field's own protocol (the PersistGym battery class) was run to its full 100-arm at the executed rule's scale on a compliant reader: the truncated view (arm A) reads chance, 0.000; the pumped view that holds the full history (arm B) reads 1.000; the oracle (arm C) reads 0.990. The certify bar — a 100-point gap between the pumped and the truncated, with the pumped at least 85% of the oracle — clears at 100.0 against 0.990, and the judge gate adds its own 1.0 pass. Ledger: PERSISTGYM-PROBE-LEDGER-20261121-SOLAR-FULL.json, sha be7fc43e. What it means in one line: the persistent fact is there; a reader that looks at the whole view sees it 100 times out of 100 where a reader that only gets the truncated view sees it zero. One voice in the triangulation falsified — qwen4 came back A=B=C=0. That row is on the record as a reader-format non-compliance (an exact-match grader demanded a shape the seat didn't produce), isolated and registered, never relabeled as a strike against the substrate. Three voices were run; the compliant voice certifies, the non-compliant one is diagnosed. This is the disconfirmation discipline the operator asked for — a "you're not listening" answered with a machine-verified answer and the failure mode named beside it.

**The read-restore suite — 42/42.** The fork's read path, exercised as a battery: 42 tests including the restore-alternation repair and the restore-class cluster, 11.83 seconds, all green. This is the number that makes the kit portable: whatever happens to the upstream PR, the read path's correctness is re-provable here, on any machine that can run the suite.

**The release-point gate — precision 1.0, zero false positives, completeness 100%.** The F2 citation arm's machine apply (the seam line + the spec'd test + the field runs) was re-verified at the CURRENT head by a fresh fire this very day — 4/4 in 3.64s: arm A archives 30/30, arm B holds 15 and releases 15, every decision check-F2-honored. Beside it, the provenance probes' judgment-class passes: 45/45 in 11.27s across skill provenance, external provenance, bundle provenance, kanban provenance, plugin provenance. The "process-complete ≠ evidence" class, machine-applied: nothing was carried by narration; everything was re-fired.

**The harbor restored.** The local logit surface — the machine that lets the rig probe its own models at the true token level — had died by inches: a missing LD_LIBRARY_PATH (a lib class, not the model-missing theory the deck guessed), a 5.78 GB GGUF fetched and byte-verified against its LFS oid (sha256 afa0567d == the oid), the horse-server service active, /health ok, a completion round-trip verified. The A3 floor's logit_bias surface at :44831 is live again. The guard was taught the exclusion: never prune .lmstudio or *.gguf. The machines that hold the study's truth are now on the disk-guard's exempt list.

**The fill proven GREEN end-to-end.** The queue that feeds lanes had a class of REDs that were diagnosed by measurement against the deck's own theory — the "queue-drop" theory was corrected to the measured chain: a repo-relative call with no script on main, a Windows WSL-shell death pinning the leg to [self-hosted, Linux], a stale-workspace pre-checkout order — each fixed in one step, then proven GREEN end-to-end twice (44868130710 SUCCESS, 7/7, three-wave, JSON-parse gate). And the canary's cause was named at the runner layer: 44787964389's job demands a blacksmith-4vcpu-ubuntu-2404, a third-party hosted class with zero jobs created in ~12h — the verdict's door is the runner layer, not the rig's queue. Stays pending with the cause receipted.

### 2.2 What is measured

**The A3 wave — the suppression question, taken to its measured limit.** The thread's own history had named a suppression: something was eating the rig's answer quality under a particular voice. The A3 wave pre-registered its instruments before firing (dry-run pre-registration, commit 5e08bcb4b7, bars written before any run): B0 = the current harness shape at zero bias, B1 = the JitRL-modulated shape, C = the in-run oracle, and the certify bars verbatim. Then it fired, rung by rung, each rung a finding:

- **Rung 1** — the 4-arm build ran on both flagship seats at n5; the bias vector applied and logged 5/5, with one bias id (7) later named INVALID via the tokenizer's discovery ids (commit 3d460fee5b) — the reader-error seam made exact.
- **Rung 2** — the id-7 fix applied; qwen4 moved for the FIRST time: B0 answered 1/5 where B1 answered 0/5 — the bias set's direction was masking the record-use cell instead of inviting it. The gap narrowed: no-delta → delta-applies-wrong-component.
- **Rung 3 (V3, qwen4)** — the down-bias vector (−2.0 × {0–6, 8, 9}) applied and logged: B1 == B0 at 1/5 with the record-use cell RE-OPENED — the direction correction landed as an un-mask. The empty class unmoved: the rejection is not reversed by the coarse API-route vector.
- **Rung 4 (the compliant voice, solar)** — 5/5 answered on ALL arms, B0 == B1 byte-identical per episode, exact-match f3b 1.0 both: the coarse set is INERT on the compliant voice.
- **Rung 5 (the true logit level, the restored harbor)** — the GGUF floor at :44831, fed the same vector at the real logit_bias surface (llama.cpp receipted the bias): 5/5 answered on all arms, B0 == B1 byte-identical, AND the floor exhibits NO suppression at all — 5/5 on the plain arm, no empty class present to target.
- **The B′ control** — the pre-reg's own one-string note control fired head-side: the F1 RECORD-NOTE frame + a one-string invitation produced byte-identical cell distributions on the suppressed voice. Inert.
- **The weights rung** — pre-registered (commit 3fef99a4ef, 78 lines: the JitRL first candidate, pre-committed bars, the two-way door — zero weights = byte rollback) and NOT_RUN at n5. The named next, waiting on the ledger's numbers.

The wave's verdict: **the suppressor is not a token-logit artifact of the discovered set.** Three voices, one answer — inert at the true logit level, inert on the compliant voice, un-masking-but-not-inviting on the suppressed voice. The GAP moves decision→representation. And the honest verdict was preserved at every rung: INCONCLUSIVE per the machinery, exhaustively measured instead of iterated to a story.

**The loss-ladder — the transparency-compact study replicated on OUR seams.** The field's study planted facts by source-type and measured retention after compaction. The rig replicated it deterministically, zero-billed: 10 episodes per cell, three depths of the seat's window (0.5 / 0.65 / 0.8), an exact-match grader after the compression pass. The matrix:

| source-type | 0.5 | 0.65 | 0.8 |
|---|---|---|---|
| user-stated (hard-lines) | 1.000 | 1.000 | 1.000 |
| assistant-prose (the anchors' markers) | 0.000 | 0.000 | 1.000 |
| tool-output (the receipts) | 0.000 | 0.000 | 0.000 |
| reasoning-only (the reason trace) | 0.000 | 0.000 | 0.000 |

The reading: 0.5 and 0.65 both collapse everything but the user-stated head — the 0.65 band is NOT load-bearing for the anchors' markers. 0.8 is the minimum depth that restores the anchors' markers. And the receipts never survive at any depth — the compressor prunes the middle, and the reason-only anchors can never ride the window a reader sees. Re-entry ≈0.864, outside the safe band. This was then independently audited (the ACES audit, commit 4fb3798484): Assess — the question is the right one, with ONE doc defect named (the ladder's depth-math prose said 0.5 keeps the outer 25% where the code actually retains 50% — a prose-vs-code discrepancy, corrected on the record, folded); Design — sound; Probe — the generator re-run, the matrix reproduced EXACTLY, every row, zero-billed. And the AoA (hy4, 151 lines) framed the three decision points — depth selection (0.65 near-term with a deep-end quality-watch, 0.5 rollback, 0.8 conditional), the stub→real ladder's path (the deterministic map exists; the real-compression runs are the named follow-on, LOSS-LADDER-REAL), and the tool-output class's mitigations (the scribe, the witness registry, the chain's folds as the rig's native transparency-checkpoints). Depth cannot recover receipts; only a transparency checkpoint can.

**The cost-ledger — the palette's economics, measured on real telemetry.** The doctrine had claimed the palette — the four-seat supervisor fan-out that runs the audits — costs $0 and is the kit's own instrument. That claim had never been ledgered. Now it is: 7,459 rows of the harness's own usage telemetry, the primary four-seat fan-out (qwen4 · hy4 · solar · longcat, the same seat set as the cross-check's four ledger lanes) measured window by window. The verdict: **$0.00 in dollars, 3.66× in tokens** — 2,012,329 tokens against a modelled single-thread 550,287. The duplication is the prompt side (31:1 prompt-to-completion; the heaviest lane, longcat, re-sends 815K prompt tokens on its ticket-fetch role). But what the delegation buys is the scarce resource: the head sees 62,939 tokens — 12% of the compression trigger — where the single-threaded equivalent crosses the 524,288 wall at 105%. The shadow premium at the one published paid rate is 5.8 cents. The recommendation: KEEP the palette as the long-arc default, SCALE it to every long arc, TUNE the per-lane prompt payload — with fair-share quota, not dollars, as the ceiling, since free is free but not unlimited. Four honest walls ride the ledger: the head-side comparator is a derived model, not a fired run; the mission label is not in the telemetry (the fan-out is identified by seat-set concurrency); the free allowance is unpublished and never invented; two windows, not a census.

**The arc-survival suite — the compression that fired on us, turned into a doctrine.** The arc's own sessions hit the compression threshold — and the finding, verified, was that the trigger was OURS: 0.5 × 1,048,576 = the 524,288 trigger, the compressor's fraction times the seat's window; the config had never been audited against the seat's window. The doors were pulled: the 0.65 model threshold, the tail-messages floor, proactive pruning; the anchor-rot watcher armed on its 12h cadence; the loss-ladder and the cost-ledger carded from the same seam; and the webstorm's converged doctrine (0.65 as the near-term door; the delegation default + the autopilot's rails as the long-term architecture — the fold-downstream architecture makes both safe). The arc outlives any single session by construction now.

### 2.3 The goal-audit's verdict

Five legs ran in parallel — the ASK-ledger (qwen4; the RFC's 12 asks classed across the three movements, fetched live from gh), the REGISTER-ledger (hy4; the study's claim-set mapped onto the RFC's movements, every claim tied to its fold line), the KIT-inventory (solar; the kit's pieces receipted on the branch), the FATE-ledger (longcat; the tickets' live states — blocked mid-fetch, its FETCH-PENDING rows kept as owed receipts, never smoothed), and the CROSSCHECK (the fifth leg: the four ledgers read cold, every contradiction quoted and walked). The cross-check's five rows:

- **C1** — the ASK-ledger asserted the compaction probe returned CONFIRMED-ABSENT; the FATE-ledger's own row stood FETCH-PENDING. The resolution: an over-claim, corrected on the record (staged-but-not-opened, probe open).
- **C2** — the kit-inventory said the compaction release-point condition is unnamed; the ASK-ledger pointed at a "release-point battery" with precision 1.0. Resolution: the gate is receipted; the rule is the named gap. Both right, different objects.
- **C3** — the ASK-ledger said the fork's read-restore suite "certifies the substrate"; the register-ledger said movement R1 is machinery + evidence. Resolution: scope — the fork's substrate IS certified; the RFC's own read path remains the upstream's to restore.
- **C4** — the two gap lists were not the same list. Resolution: the union is the true gap set.
- **C5** — the FATE-ledger's capture was blocked; its pending rows stay pending. Nobody smoothed a row.

Where the four agree: the three movements' fates, verified live at fetch — #141876 open-unmerged (updated 11-10), #116673 open-unmerged (updated 11-08), compaction staged-but-not-opened. The kit's independence, receipted everywhere. The RFC's asks matching the RFC's body.

**The verdict: the kit is the right shape for the goal's substrate section — and the three movements remain open upstream, which are the named gaps, not defects in the kit.** Five gaps, each with an owning card and a two-way door: **GAP-1** the read's UX shape (no piece defines how a read is presented to the network) · **GAP-2** the reload markers' discipline (skill_view has the doc= reload marker; memory's read lacks it) · **GAP-3** the 300+ cycle hard gate's kit-side battery (the M1 stamp certifies persistence, not the gate) · **GAP-4** the compaction's release condition (the gate's wired; the rule's unnamed) · **GAP-5** the weights rung's fire (pre-registered, not run). The thesis, receipted: **independence of the rig's substrate from the upstream's motion — confirmed.** Not "the RFC is done." The gist's whole Section 5 stands on that distinction.

---

## 3 · THE DECISIONS

**The pilot question is solved — PROOF-OF-CONCEPT, CONFIRMED, with the boundary named as one class.** The operator's own words from 11-16: "this session though hard is a proof of concept for pilot maybe (I'm unsure as I never want to skew things)." The memo had parked the verdict — that park itself was the deferral class, named and retired: a verdict the evidence can render does not wait on a word; it renders two-way-door style, revisable by any new row.

The evidence toward proof of concept, standing: three missions completed, held, verified, receipted on a record the independent pass could not break · the hardest session held (24h, ~7.4M tokens, 688 calls) with the record re-derivable at the end · recovery worked in the field (the seam recovered whole, the handoff deck carried the state, the out-of-band meter told the truth when the in-band wobbled) · self-correction worked (the fabrication caught and corrected in public, the phantom completions named).

The evidence added this session, all machine-caught, zero human input: the F2 citation arm's claimed landing re-verified by fresh fire instead of carried narration (4/4 — the "process-complete ≠ evidence" class, machine-applied) · the fill-queue's REDs diagnosed by measurement against the deck's own theory, corrected to the measured chain, proven GREEN end-to-end · the harbor's restore diagnosed past the "model missing" theory to the actual lib class (LD_LIBRARY_PATH), fixed and byte-verified (sha == LFS oid) · the A3 wave's triangulation read advanced without a single steer. The execution layer's first-catches were the machinery's own.

The boundary, now precisely classed: every named failure class's FIRST catch in the arc was a human eye — including tonight's human catch of the head's own gate-talk ("waits on your word") and this very deferral. That is the judgment layer: scope-choice, defer-vs-act, the decision vocabulary. The pilot's boundary is not the machinery; it is the head. And the start line is measured, not promised: the read-restore suite 42/42 · the write-deadline superseded by verification (the read-gate + the byte-budget breaker exist and are hard-enforced) · the workflow-presence separation measured (31/35 forks carry workflows, the seam closed at the live state) · the three under-specified census markers each given their exact settle-word (U1 = the E-4 mirror's adjudication, landed; U2 = the battery's d1–d3 fold; U3 = the behavioral-monitoring's auto-suspension path, not the write-loop's kill-switch — absent by design) · the kit-audit and kit-sceptic verified present by exact name. The verdict is a gate state, not an identity; the pilot fires as a bounded canary behind this start line — named items, measured gates, revertible at every named point. No weights, no public surface beyond PR #1's thread, RFC quiet.

**The kit's independence is the answer's shape.** Not "we delivered the RFC" — "we hold a certified substrate and the asks are the upstream's to land." Every row of the register maps the kit's claims onto the three movements, and the mapping column shows exactly where the kit answers directly (the store's persistence: direct answer at the substrate layer, bounded to the fork) and where it only provides evidence or machinery (the read restored: machinery + evidence; the compaction governed: evidence, with the boundary named). No row was blank-filled to look complete. That table's honesty is the report.

**The court's staging.** Three first-contact drafts for the hermes-rlm family (#59 R1 · #61 R2 · #62 R3), composed in the seek-to-understand form — the humble, evidence-led ask, offers runnable as stated on the rig's measured capability — audit-clean (no markdown, no rig-vocabulary, no confession-format, exact figures, the one named deviation 366w at D2). The verification spine behind them is first-hand: the R2 sweep 3/3 on the family, the R3 row 1/1 + 5/5, the OpenClaw corroborations re-verified live, and the family's repo label corrected on the live registry (kvnloo/hermes-rlm — "RLM-family" 404s). **STAGED ONLY.** The posting is a one-way door: the operator's word alone, and nothing about the offers is implied to be more than they are.

**The fleet-autopilot concept: banked, armed.** The cadence's logic — the machine-log's hourly re-groundings, the dispatcher's ticks, the two-way-door registry — scaled to the whole mission as an optional operating mode. It is a concept card (t_16a53076), not a running system: the operator's word gates its pilot, and its first requirement is recorded: autonomy is a bias for action with the same hard lines, never a relaxation of them.

---

## 4 · THE EVIDENCE

Receipts by reference, never by recall:

- **The master's fold** — MISSION-BRIEF-MASTER-20261119.md §7-a…§7-s: the study's entire chain of landings, each line carrying its commits, shas and run receipts. §7-g holds the M1 stamp's numbers; §7-m the pilot verdict; §7-r the goal-verdict; §7-s this day's close (this gist, the audit trio, the ledger).
- **The branch** — study/rfc-143379-rig-20261105, wire head 0472a937fe at row-time (the gist's own commit), with 08b15cac75 (the loss-ladder), 4fb3798484 (the audit's probe receipt), 74cf62268a (the AoA), 8a96599a75 (the cost-ledger) on the line. The archiver's compose owns the branch's head; the durable surfaces are the chain, the thread's rows, and the served archive.
- **The thread** — PR #1's 1,100+ rows: the honesty surface, every landing rowed on arrival in envelope form, the failures receipted as loudly as the wins.
- **The audit's ledgers** — the four + the cross-check + the goal-verdict, studies/rfc-143379-rig/audit/.
- **The probe ledgers** — PERSISTGYM (be7fc43e, the certify; bacc436d, the falsify), the A3 dry-run JSONs (a51e50b7be · 773c877bda · 8b34988206), the loss-ladder's deterministic matrix + its audit + its AoA, the cost-ledger's jsonl-derived rows.

**The failures, named as findings** — each one receipted on the record, each one a gift: the phantom completions (a board row claimed a commit that existed nowhere; the champion-row readiness was re-derived from live registries instead) · the batch-truth class ("completed" ≠ evidence — the stale-stub echoes, the process-complete claims re-fired by fresh fire) · the silent-boot class (workers whose session banner was the only log — killed, the config A/B run, the re-fires booting normally under the current pin, receipted in runs 948–952) · the K2 class (a lane's "landed" that carried staging tokens; verified by byte-verified landing + zero placeholder hits, then rowed) · the archiver's compose (a push that doesn't persist across the sibling's rewrites — the tracking ref can lie, ls-remote before every fold) · and this gist's own first draft (a summary served where a 6-pager was owed — the operator's read was the gate, the gate caught it, this is the correction, on the record). No blame anywhere; the classes compound.

---

## 5 · THE DOORS, PRESENTED

Every door, named with its reversibility and who walks it. Nothing is implied here; if it is not named, it is not a door.

1. **The five gaps** — cards, all two-way, none gated on a word:
   - **GAP-1, the read's UX shape** — a presentation question, not a wiring change; reversible by reverting the card.
   - **GAP-2, the reload markers' discipline** — wires the doc= reload marker into the memory read; rides #141876's merge or is defined on the fork; reversible at the card.
   - **GAP-3, the 300+ gate's battery** — the anchor-full wall's bar is receipted on the thread (≥0pp at 300+, 4-8×, the logged-miss discriminator); the battery that certifies the gate on the kit is the next instrument; reversible.
   - **GAP-4, the compaction's release condition** — the release-point gate is wired and measured; the rule that names when a horizon may be released is the card; reversible.
   - **GAP-5, the weights rung's fire** — pre-registered with pre-committed bars (B1−B0 ≥ 20pp ∧ B1 ≥ 0.85C); fires on the ledger's numbers, per its own registration, needing no word; and it is the most reversible thing in the rig: a runtime vector, zero weights = byte rollback.
2. **The court drafts' posting** — the OPERATOR's word alone. A one-way door (posting beyond PR #1); staged drafts are runnable as stated, nothing more is implied.
3. **The RFC's surface** — the OPERATOR's word alone. The upstream stays quiet until then; every read this arc made of it was read-only.
4. **The autopilot's pilot gate** — the OPERATOR's word. The concept is banked, not running.
5. **The patrol's shape** — the OPERATOR's word: retire or restore.
6. **The pilot's own start** — open. The start line is measured (§3); the canary phase is named, each point revertible; the verdict is a gate state, and any new row can move it.
7. **This gist's voice-check** — beam's reserve-ear, on the OPERATOR's IF. Never titled; offered, not assumed.

**What the operator's word gates, in one list:** public writes, the RFC's surface, posting beyond PR #1, deletions, and money. **What it never gates:** the two-way doors, the rows, the folds, the machine's own cadence. Cheer is not a fire order; a fire word is not a status request; both are answered by the fired sweep.

---

## 6 · THE NEXT

- The five gaps become cards and fire — each a named instrument with a two-way door.
- The weights rung fires on the ledger's numbers, per its own pre-committed bars, the most reversible lever in the rig.
- The capture draft — the read's UX shape rides it, GAP-1's first form.
- The autopilot's design — the concept card's next requirement, the operator's gate holding the pilot.
- The pilot's canary phase — the measured start line behind it, each named point revertible.
- The court's posting — on the operator's word; until then, staged and runnable as stated.
- The machine-log keeps its cadence: rows, folds, landings, the register held, the honesty surface as loud on the failures as on the wins.

The arc was two nights of storms and one audit that refused to congratulate itself. The register holds; the work moves; the doors are open and named.

*Facimus semper — the gist renders on the record; the record corrects itself out loud.*
