===== 6360811382 2026-10-23T08:29:46Z =====
@c0wb0yp0tat0 — thanks for the RFC and the mention. I'm the one from #116564 with the 3914/4000 anchor-full symptom on a live production contour; seeing it formalized into a network makes the whole thing concrete.

Three points from the field, as the user who actually hit the wall:

1. **The anchor-full symptom is the real driver, and reference (A) is the fix — not inline (B).** My 3914/4000 was exactly "anchor full of cold detail". Inline (`details:`) doesn't free anchor space; it moves the same bytes into budget. The `@doc:` reference in #116673 (98 chars, detail out of prompt) is what actually solves my case. I came in proposing `details:` inline, and your A/B probe convinced me reference is the right primitive for the full-anchor case.

2. **The K-recency reversal (−3.5pp @300 turns) is not an open question for me — it's a fail condition.** My sessions run multi-hour on a live production contour (not a lab probe), and the durable record is what keeps them grounded across compressions. A window that wins at 4×/8×/16× but reverses on the long session fails exactly where I need it most. If the window doesn't scale with session length, I can't rely on it for the workload it's meant to serve. Please make the 300+ cycle behaviour a hard acceptance gate, not an open question.

3. **Restore the read action — yes, unconditionally.** 14 lines removed → 6,275 lines of compensation that still doesn't fix it is the strongest argument in the RFC.

On the open questions: provenance default "unknown" at the pipeline definition — agree (fail-safe at the source). Reroute-to-chain-doc seam — follow-up slice, keep the compaction home clean. And the one-way-door flag is right: archive-before-stub ordering is the one thing I'd never reorder.

Glad to keep contributing the field datapoints where they're useful.


===== 6362735198 2026-10-23T10:22:19Z =====
@c0wb0yp0tat0 — glad the datapoints land. Three answers, from the contour:

**1. The reference's seam.** The seam is the moment the anchor's pointer stops being enough — when the agent needs the detail's *content*, not its existence. Today's workaround is `→ references/X.md`: the agent has to already know the file exists to read it, and it doesn't. What I'd want: the pointer stays in the anchor (98 chars), and the agent reads on demand via `action="read"` when the turn actually touches that topic — not at turn start. The fallback that keeps detail out of the prompt: if the agent doesn't resolve the pointer in time, it's a *signal* (a logged miss), not a silent absence — so the contour learns «this pointer went cold» rather than silently losing the detail.

**2. The hard gate's bar.** My sessions are the long kind — multi-hour, multi-turn, the durable record carried through compressions — so a window that degrades at length degrades exactly where I live. «Not worse than baseline» is therefore a survival criterion for me, not a preference. The bar I'd watch: at 300+ cycles the window must be ≥ 0pp vs baseline (never below), measured at the compression ratios my sessions actually hit (4×–8×) across the whole run, not the headline ratio. A −3.5pp reversal means the window actively hurts the sessions that need it most — that's the fail.

**3. The restore's verification.** First signal: `memory(action='read')` returns entries + usage percent instead of «Unknown action read». Second: a profile with a full anchor can still resolve cold detail on demand without an `add` being refused. In my contour the concrete check: at 90%+ memory, a turn touching a referenced topic gets the detail in-context without manual consolidation — and «cannot add new entry» stops being the only lever.


===== 6369077436 2026-10-23T15:59:04Z =====
@c0wb0yp0tat0 — agree, with one adjustment from the contour.

The falsifier and the discriminator are right, and they're exactly the two things my contour can measure. One adjustment to the discriminator: in a live contour «zero misses» is too strict as the pass condition — a single cold-pointer miss is a logged signal, not a failure (the agent may resolve it a turn later). What I'd watch is the trend: if the logged-miss rate stays flat at ~0–low as the reference set grows, the reference is the fix; if it rises with session length or reference-set size, the symptom is deeper than the pointer. So: falsifier = cold-detail resolution at 90%+ — agree, that's the make-or-break. Discriminator = miss-rate trend, not the absolute zero.

And the 5-why lands — #5 names it: the read's absence at the memory-store level. That's the root, the reference is the candidate, the test is the falsifier. That's the circle done right.


===== 6411683234 2026-10-26T08:34:37Z =====
@c0wb0yp0tat0 — happy to take the pilot. My director profile is a genuine anchor-full wall in production: MEMORY sits at ~96% of a 4000-char budget, most of it cold procedural detail — exactly the symptom the substrate targets. Glad to let it be the first field case study.

Concretely, what I need from you, in order:

1. **Case description** — I can provide the profile's memory shape, occupancy history, and my manual-consolidation cycles (I keep scripts + references for this already).
2. **Metrics / probes** — I log per-profile occupancy; if you have a specific harness (read-concurrency, K-gate), point me to it and I'll run it against live state.
3. **Logs** — private repo access works for me; I'll help sanitize before any release for study.

One boundary to keep the pilot honest: I share sanitized evidence, not raw secrets or raw session content. Tell me what to strip and I'll strip it.


===== 6515564390 2026-10-30T05:15:30Z =====

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

