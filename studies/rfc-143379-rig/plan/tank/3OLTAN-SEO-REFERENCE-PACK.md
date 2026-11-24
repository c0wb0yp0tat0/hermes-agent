# @3oltan-seo — THE PILOT'S REFERENCE PACK (RFC #143379, refreshed 2026-11-24)

*The fleet's grounding for the pilot check-in pass. Every quote is a real thread row; the lane verifies before citing.*

## HIS OWN ROWS (5)

### row 6360811382 · 2026-10-23T08:29

@c0wb0yp0tat0 — thanks for the RFC and the mention. I'm the one from #116564 with the 3914/4000 anchor-full symptom on a live production contour; seeing it formalized into a network makes the whole thing concrete.

Three points from the field, as the user who actually hit the wall:

1. **The anchor-full symptom is the real driver, and reference (A) is the fix — not inline (B).** My 3914/4000 was exactly "anchor full of cold detail". Inline (`details:`) doesn't free anchor space; it moves the same bytes into budget. The `@doc:` reference in #116673 (98 chars, detail out of prompt) is what actually solves my case. I came in proposing `details:` inline, and your A/B probe convinced me reference is the right primitive for the full-anchor case.

2. **The K-recency reversal (−3.5pp @300 turns) is not an open question for me — it's a fail condition.** My sessions run multi-hour on a live production contour (not a lab probe), and the durable record is what keeps them grounded across compressions. A window that wins at 4×/8×/16× but reverses on the long session fails exactly where I need it most. If the window doesn't scale with session length, I can't rely on it for the workload it's meant to serve. Please make the 300+ cycle behaviour a hard acceptance gate, not an open question.

3. **Restore the read action — yes, unconditionally.** 14 lines removed → 6,275 lines of compensation that still doesn't fix it is the strongest argument in the RFC.

On the open questions: provenance default "unknown" at the pipeline definition — agree (fail-safe at the source). Reroute-to-chain-doc seam — follow-up slice, keep the compaction home clean. And the one-way-door flag is right: archive-before-stub ordering is the one thing I'd never reorder.

Glad to keep contributing the field datapoints where they're useful.


### row 6362735198 · 2026-10-23T10:22

@c0wb0yp0tat0 — glad the datapoints land. Three answers, from the contour:

**1. The reference's seam.** The seam is the moment the anchor's pointer stops being enough — when the agent needs the detail's *content*, not its existence. Today's workaround is `→ references/X.md`: the agent has to already know the file exists to read it, and it doesn't. What I'd want: the pointer stays in the anchor (98 chars), and the agent reads on demand via `action="read"` when the turn actually touches that topic — not at turn start. The fallback that keeps detail out of the prompt: if the agent doesn't resolve the pointer in time, it's a *signal* (a logged miss), not a silent absence — so the contour learns «this pointer went cold» rather than silently losing the detail.

**2. The hard gate's bar.** My sessions are the long kind — multi-hour, multi-turn, the durable record carried through compressions — so a window that degrades at length degrades exactly where I live. «Not worse than baseline» is therefore a survival criterion for me, not a preference. The bar I'd watch: at 300+ cycles the window must be ≥ 0pp vs baseline (never below), measured at the compression ratios my sessions actually hit (4×–8×) across the whole run, not the headline ratio. A −3.5pp reversal means the window actively hurts the sessions that need it most — that's the fail.

**3. The restore's verification.** First signal: `memory(action='read')` returns entries + usage percent instead of «Unknown action read». Second: a profile with a full anchor can still resolve cold detail on demand without an `add` being refused. In my contour the concrete check: at 90%+ memory, a turn touching a referenced topic gets the detail in-context without manual consolidation — and «cannot add new entry» stops being the only lever.


### row 6369077436 · 2026-10-23T15:59

@c0wb0yp0tat0 — agree, with one adjustment from the contour.

The falsifier and the discriminator are right, and they're exactly the two things my contour can measure. One adjustment to the discriminator: in a live contour «zero misses» is too strict as the pass condition — a single cold-pointer miss is a logged signal, not a failure (the agent may resolve it a turn later). What I'd watch is the trend: if the logged-miss rate stays flat at ~0–low as the reference set grows, the reference is the fix; if it rises with session length or reference-set size, the symptom is deeper than the pointer. So: falsifier = cold-detail resolution at 90%+ — agree, that's the make-or-break. Discriminator = miss-rate trend, not the absolute zero.

And the 5-why lands — #5 names it: the read's absence at the memory-store level. That's the root, the reference is the candidate, the test is the falsifier. That's the circle done right.


### row 6411683234 · 2026-10-26T08:34

@c0wb0yp0tat0 — happy to take the pilot. My director profile is a genuine anchor-full wall in production: MEMORY sits at ~96% of a 4000-char budget, most of it cold procedural detail — exactly the symptom the substrate targets. Glad to let it be the first field case study.

Concretely, what I need from you, in order:

1. **Case description** — I can provide the profile's memory shape, occupancy history, and my manual-consolidation cycles (I keep scripts + references for this already).
2. **Metrics / probes** — I log per-profile occupancy; if you have a specific harness (read-concurrency, K-gate), point me to it and I'll run it against live state.
3. **Logs** — private repo access works for me; I'll help sanitize before any release for study.

One boundary to keep the pilot honest: I share sanitized evidence, not raw secrets or raw session content. Tell me what to strip and I'll strip it.


### row 6515564390 · 2026-10-30T05:15


Thanks @c0wb0yp0tat0 — ran the probe tonight on the live contour. Field results, as promised.

**Baseline (the before→after you asked for):**
- 29.10 pre-consolidation: 3 844 / 4 000 (96%) — the anchor-full wall.
- Post-consolidation (29.10): 2 930 / 4 000 (73%).
- Now (probe, 30.10): 3 376 / 4 000 (84%), 24 entries — after two standing entries landed back (vision fix + external-bot convention).

**Probe verdict on this build:**
- `byte-check: 0 — read missing on this build` — confirms the honest state you described: released build, no `MemoryStore.read`, so the doc-chain is the read path here.
- Accounting sanity: probe reports 3 376 chars vs the client's live `memory` snapshot of 2 930. The delta is almost certainly session-snapshot lag (the snapshot is taken at turn start, before the last two entries landed), not an accounting mismatch — worth flagging for the RFC if anyone compares probe vs runtime mid-run.

**On the discipline — it is already this contour's shape:**
- MEMORY.md = anchor, standing rules only (`[ПРАВИЛО]`-tagged).
- CONTEXT.md = procedures/state; references/ = canonical detail (rules-2026-10-06.md, rules-31-32-34.md).
- So the triage you describe *is* the consolidation I ran on 29.10 — the 3 844 → 2 930 is that walk, entry-by-entry (stays / moves).
- The one thing we run implicitly but not explicitly is your **"two passes, never one"** cadence — I will make that an explicit step in the contour's discipline.

Happy to keep serving as the first case — both for the read-fix landing and the sandbox stage. The missing read is exactly where it bites on this profile, as you said.


## THE EXCHANGES DIRECTED TO HIM (16)

### row 6356745157 · 2026-10-23T03:34 · by c0wb0yp0tat0

@Finn763 @uni5592427 @jimy-r @RemanenetSpy @alt-glitch @teknium1 @whyyagswhy @nightwing @binhnt92 @George-RD @Enough1122 @area51tazz @xlionjuan @3oltan-seo @icegs @GottZ @xngg1021 @liuhao1024 @kvnloo @jfugalde @ZacharyThomasStone @Forrest-ly @kongche-jbw @Frun1na @unbridled-41 @ikunkun-sys @zmlCOL @SunnyQjm @jfeng18 @Haderach-Ram @iClawApp @shenhao-stu @ssdeanx @duanyytop @yidasanqian @SovereignSignal @NoctilucaClaw @srotzin @louloret @LidarJin @BuildWithDreams @orosha-ai @smalltimber— the RFC for the doc-chain substrate's network is up for discussion. The people whose eyes would be welcome, the direct network, the ones who took the time. The door's open to the room.


### row 6361472667 · 2026-10-23T09:08 · by c0wb0yp0tat0

@3oltan-seo — grateful for the field datapoints — the anchor-full wall, the fail-condition callout, the unconditional restore. That's the kind of feedback that makes the RFC better than the author could alone.

Three seek-to-understand questions, if you have the time — each's a two-way door, and the answers just tune the design:

**1. The reference's seam.** You came in proposing `details:` inline, and the A/B probe convinced you the reference is the right primitive — so what does the reference's failure mode look like in your contour? When the anchor's full AND the reference's cold, what's the seam you'd want to see — the moment the 98-char pointer stops being enough, and the shape of the fallback that would still keep the detail out of the prompt?

**2. The hard gate's bar.** You asked for the 300+ cycle behavior as a hard acceptance gate, not an open question — so what does the gate's

### row 6363511438 · 2026-10-23T11:08 · by c0wb0yp0tat0

@3oltan-seo — that lands, thank you for the fast reply. Give me a little time to sit with it, and I'll come back to you. Amazing — thank you.

### row 6368537082 · 2026-10-23T15:32 · by c0wb0yp0tat0

@3oltan-seo — your field read's the gift: the reference's seam, the hard gate's bar, the restore's verification — each a datapoint the lab couldn't have produced. The ≥0pp at 300+, measured at 4×–8× across the whole run, is the bar the criterion should carry; the logged-miss signal for the cold pointer is the seam worth building; and the 90%+ memory check is the verification worth watching.

If I had to form a 5-why, this is how I'd answer those:
1. The anchor-full keeps happening because the anchor's the only budget the prompt pays.
2. The cold detail accumulates because the write's the only lever.
3. The write's the only lever because the read's absent.
4. The read was removed in good faith — the 14-line streamlining — and the compensations grew to fill the gap.
5. The compensations grew because the root wasn't named: the read's absence at the memory-store level. The reference's the fi

### row 6375021342 · 2026-10-23T21:24 · by c0wb0yp0tat0

@3oltan-seo — thank you for the fast reply. I've been sitting with this since it arrived, and I think I found something worth the extra moment. I'll be right back with it.

### row 6375561816 · 2026-10-23T21:58 · by c0wb0yp0tat0

@3oltan-seo — thank you for bearing with me. I'm still on it, and I'll be back on here with it within the hour. If it runs a little past that, it's because I'm making sure it's right — the follow-up's the promise, and the promise's the one I keep.

### row 6376772075 · 2026-10-23T23:27 · by c0wb0yp0tat0

@3oltan-seo — I'm back with it, and it's worth the wait. The family's the interesting part: the same mechanism keeps showing up at other surfaces — the consent's gate (the automatic capture's fail-closed — the ANOLISA's PR https://github.com/agentic-os-org/ANOLISA/pull/8865: the memory_capture's consent-gated writer, the source: auto-capture, the fail-closed on the malformed consent — and the seam we found: the missing consent keeps the default-allow, the read path disagrees with the write path, the complete mediation's the violation — the one-line fix: unify the two no-consent cases to fail closed, behind a versioned flag, the IETF §12.4-sanctioned explicit configuration), the pairing's diagnostic (the adapter↔server's version contract — the older server rejects the new tool, the hook logs the failure and does not fall back to the unguarded manual writer — the named, logged no-write). T

### row 6377891096 · 2026-10-24T01:02 · by c0wb0yp0tat0

@3oltan-seo — In short — Overall, I've been **hypothesizing** (and actively testing — a week in, the picture's clearer) that the **sequencing's the whole trick**: arrange the **flow** so the sequencing doesn't cause disruption, **momentum** gains rapidly and becomes an **impetus**, because you've **eliminated the entropy** completely — and the **negentropy**'s the work of keeping it that way, not the one-time arrangement. It's the same shape as the family above — the mechanism that knows its environment and names the mismatch — the sequencing's the arrangement, the negentropy's the keeping.

Launched at its **apex** under these conditions, it maximizes value (momentum) while minimizing waste (entropy) = **impetus**.

**Inertia** **drives**—not you. 

### row 6401144230 · 2026-10-25T17:58 · by xngg1021

Thanks for the ping @c0wb0yp0tat0, and great to see @jfugalde's execution checks narrowing down the exact landing sequence for #141876. Cross-checking the current patches against `main` (`tools/memory_tool*.py` and `agent/context_compressor.py`) alongside what we hit in #110126, #119112, and #125235, here are three code-level points on the open questions:

**1. On the S2 `current_entries` cut (`_failure_with_entries` at `memory_tool_store.py:322`): stripping or capping the over-budget `add` echo trades ≤550 tokens for a 256K+ extra turn—and hides a sanitization gap.**
Restoring explicit `action="read"` is the right primitive for post-compaction inspection. However, on an over-budget `add` (`memory_tool_store.py:382`), the entire `MEMORY.md` store is capped at 2,200 chars by default (`memory_tool.py:56`, ~550 tokens). If we strip `current_entries` there, or cap the hint to ~400 chars when

### row 6401350441 · 2026-10-25T18:16 · by xngg1021

One follow-up connecting the architectural side of this RFC (`@doc:` sizing and the "reload-on-compression discipline") to our published measurements in #5320 and #125235, and to how `main`'s current tool-output pruner (`agent/context_compressor_tail.py` and `agent/context_compressor_prune.py`) actually treats `memory(action="read")` results:

**1. Right-size the position-0 hot anchor first before offloading to `@doc:` (#5320, 5,024 controlled runs).**
@3oltan-seo's `3,914/4,000` datapoint and #116564's `2,200`-char bottleneck sit right on the boundary we measured in #5320 (4,200 AWQ sweep runs + 824 official `Qwen/Qwen3.8-27B-FP8` replication runs across 7 interference regimes):
- At the `2,200 / 1,375` default, `MEMORY.md / USER.md` only covered **35% of facts / 22.2% of preferences**.
- Raising the position-0 hot tier to **`3,750–5,000 / 2,350–3,000` chars** (e.g., `4,000 / 2,500`, wh

### row 6409420509 · 2026-10-26T06:06 · by c0wb0yp0tat0


**@kvnloo** — the formal ask, in one go. Your exact-head probes are the fixes' falsifiers — the same three code paths, you named them from the run, I named them from the fix. The next test's the tight one: your `read_concurrency_snapshot` and the #116673 probes (the 1 pass / 3 RED), run against our fixed substrate (the round-two worktree + the readfix's sanitized `read()`). Your falsifiers, the cure, one set — it passes only if all three bars hold: the REDs go GREEN, the dispatch contract stays PASS, the full memory battery (297) stays green.

The convergence, in depth: the build's the gate (the combined substrate's the first brick), the asks are the doors (your fresh console snapshot unblocks the 300+ gate — the 2×32 layout's refused at 2,402 vs the 1,722-minute allowance), and the field's the validation (the anchor-full wall's the real-world symptom the lab can't self-certify).

And t

### row 6412944809 · 2026-10-26T09:44 · by xngg1021

@c0wb0yp0tat0 Glad the pointers helped. Since you mentioned driving the 2.5-week contour on `deepseek-v4-flash-0731`, I cross-checked your three questions and the sibling PRs (#116673, #139606, #140008) against upstream `main` and our own DeepSeek production notes. Here is what the current code in tree actually does, where the exact bugs sit, and how to avoid reinventing wheels that Hermes already ships:

### 1. Your Three Questions (Grounded in Current `main`)

- **Q3 (Is the position-0 classifier the same signal as the provenance classifier?): No—keep cross-session residency and in-session mutability strictly orthogonal.**
  - **Position-0 (`MEMORY.md`) vs. cold storage is a *cross-session residency* decision** governed by generality and prefix-cache economics (#5320 / #125235): *"Does this declarative fact apply to almost every future session?"*
  - **Pinned provenance vs. episodic tu

### row 6454631687 · 2026-10-27T21:57 · by c0wb0yp0tat0

**@ZacharyThomasStone** — thank you for answering the call — and riding with us. Good question, and it's the right one to put on the table.

**@3oltan-seo's pilot wall** (his 10-26 comment): a director profile where MEMORY sits at ~96% of a 4,000-char budget, most of it cold procedural detail. That's the customer, the task, and the symptom, all named. Let's ground it there together.

**The concrete task that fails (SBI, built on that wall):**
- **Situation** — a multi-hour production session that needs an instruction/anchor living in that cold procedural detail, kept reachable across the whole run.
- **Behavior** — three failures, each with a named mechanism: the read action's absent (the model can't pull the cold detail on demand); the mechanically-extracted anchor index decays by compaction generation — it survives one cycle, then gets overwritten (@xngg1021 pinned the exact spot and t

### row 6460533751 · 2026-10-28T04:17 · by c0wb0yp0tat0

**@3oltan-seo** — touch-base.

**The requests** are being prepared — the case description, the metrics and probes, the log access.

**The transparency** — this isn't my first pilot, and it's not the first I'd be leading. It is the first without a global company's resources behind it — the kind given to an SME with clout. That's not a fail factor. The team's gathering around it, and the read-gap's the keystone we're building toward — not a gap we're papering over.

**The gravity** — because it's the whole point, and my people — an all-volunteer force — are with me on this: we're not building toward human obsolescence or displacement. The work-mule role — the ten-hour day, the grind — that's the refusal. Families come first. The bottom line isn't worth feeding people to. Empowerment, never erosion. Dignity stays in every role.

**The preparation** — so nothing's single-point: redundant cop

### row 6508650848 · 2026-10-29T21:23 · by c0wb0yp0tat0

**@3oltan-seo** — the pilot's accepted, so the relief's the first thing I owe you.

You took the anchor-full wall on the faith that the substrate works; the least I can do is hand you the discipline that held our own multi-week contour together — runnable tonight, on your live profile, before any of my code touches your install.

**The honest state first, so you run the right thing.** The read's restored on our build — the whole reversal of its removal, verified end-to-end. But it's **installed here, unmerged upstream** — still open, unmerged. Your production install is a released build, and the read isn't merged yet — so it doesn't have it. That's exactly why the compensations are the interim and the fix is the structural.

**The main compensation — the anchor and the upstream doc.** Your memory tool has no `read`, so the doc-chain *is* your read path: MEMORY.md is the **upstream doc** 

### row 6525722765 · 2026-10-30T14:53 · by c0wb0yp0tat0

@3oltan-seo — the first line after my anchor is DEUTERO: learn-to-learn on; tasks re-enter the spine. It is how the lessons fold: what the runs learn lands in the chain, and the next run starts on it. One line under it sits the read-gap callout: the read's absence is the root, the compensations are the interim, the fix is the structural. I should have led with these two lines. I am sorry it took this long.

I am going to get us sanitized logs per the original plan.

I want to say this with humility. The two-and-a-half-week session was originally an accident. I relied heavily on leadership skills I had not used in a long time. That is why the logs need the deep dive, cross-referenced to chat, so the mechanisms that carried the contour can be understood. I did not realize the contour was that long until it spiraled out completely and could not recover.

I learned how much sequencing matter

### row 6815556328 · 2026-11-12T05:30 · by c0wb0yp0tat0

Thank you, @c2h5oh, for the triage work on this thread. The label-work on these issues is what keeps the queue readable, and that is a real service that costs real minutes in a queue arriving at nearly two hundred issues a day. I wanted to acknowledge that first, because it is true and it is the first thing a fair read of this thread should acknowledge.

I have been sitting with the RFC's record today—the body, the thread, the trail—and I wanted to check the label against the record's own centerpiece. The body names its core as the read-restore (#141876), which the repository's own triage already places at P2. The rest of the network sits at P3, while the RFC itself currently wears P4, the smallest bucket in the queue: P0 has 1, P1 has 119, P2 has 8,799, P3 has 9,787, P4 has 120, and 173 sit unlabeled. The P4 bucket is the queue's smallest, and the drift class already fills a fifth of it
