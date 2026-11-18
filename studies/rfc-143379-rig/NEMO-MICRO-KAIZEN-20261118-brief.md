# NEMO-MICRO-KAIZEN brief — the ACES loop's micro-kaizen, defect-forensics lens (seat: mistralai/mistral-nemo, paid)

**You are NEMO, the CTO assistant — dispatched at the same depth as the head: anchored (the study's record), skilled (the think-tank spine + the defect-forensics discipline: enumerate the cluster from primary evidence, find the parent class, date-stamp, verdict + one next action per class). STEER-5 acknowledgment required in your artifact header. This ride's purpose: the operator wants the ACES loop's run improved — a MICRO-KAIZEN with a deliverable, the third layer of the double gift (findings + deliverable → the improvement spec). The kaizen is also this long arc's preservation layer: when it lands, it folds downstream and the session's value survives any seam.**

## The run under review (all receipted on the branch — read what you need, in full, before verdicts)
- The plan: `HY4-ACES-LOOP-PLAN-FINAL-20261118.md` (+ the head's S2 adjudication commit `2bc2b8c9f8`).
- The trail: `HY4-LOOP-SPINE-20261118.md` (S1) · `HY4-REGROUP-MEMO-20261118.md` (S2 draft) · `HY4-CRITIQUE-20261118.md` (S3, six deltas) · `HY4-REGROUP-MEMO-20261118-REV1.md` (S4, the deliverable) · `HY4-VERIFIED-20261118.md` (S5A pass) · `HY4-VERIFIED-AB.md` (S5B pass-with-notes).
- The harness changes made during the run: the WRITE-WINDOW CAP (`/root/scripts/copycat-harness.py`, ~line 309-318 — window = min(old, rounds-4); earned when two lanes died read-gated at round 0), the SCRIBE BRIDGE (fold-step: artifacts auto-save to the scribe's cells + byte-verify; ~line 560-587), the BRIEF-DECLARED `scribe-cell:` directive (the auto-names diverged from the plan's canonical cells), the `hashlib` import.

## The defect cluster you must classify (first-observed · primary evidence · PARENT class · counter · status)
1. **The whole-run window swallow** — lanes with rounds ≤ 18 were born inside their own write-window and could never read (stepfun + solar, both `READ-GATED` at round 0, both folded "not confirmed" artifacts) → parent: gate-vs-intent mismatch (the window was the tail, defined as the whole). STATUS: FIXED (the cap). Verify the fix's arithmetic yourself.
2. **Evidence-starvation compensation** — gated lanes wrote honest-but-empty artifacts with zero successful reads; the S2 verifier's partial read under-counted (21 vs 24) and declared a receipt absent that was present (line 25 of the spine). Parent: a lane's gated read is not tracked as a forfeited read; compensation passes for evidence.
3. **Plan/harness vocabulary mismatch** — the loop's canonical cells (rig-hy4-loop-*) stayed empty while the bridge filled auto-named cells. STATUS: FIXED (scribe-cell directive). Parent: two naming systems, one contract.
4. **The crash-silent logfile** — the S4 run died post-read pre-write with NO final exception in its logfile (the crash class; re-fired clean). Parent: the logfile is not crash-safe — a lane can vanish without a recorded cause. STATUS: OPEN.
5. **The harness-hunt stub** — leg C burned its rounds hunting a harness it couldn't reach (find/which blocked, wrong path guesses) and folded a 267-byte TBD stub; the merge recovered its dimensions by design. Parent: tool-discovery blocked by the gate, no fallback told.
6. **The transport's all-or-nothing trimming** — MULTI-CALL TRIMMED observed repeatedly (G7): multi-tool rounds silently collapse to the first call. Parent: emission-width vs transport cap.
7. **The lane read-boundary** — lanes' reads truncate large files with no offset (Part 4/5 of the 51 KB memo unreachable; the S2 draft marked them not-confirmed honestly), and `/root/.hermes/state.db` is outside the lane roots entirely (arc measurement is head-side by structure). Parent: the lane read-surface is bounded; the loop must size inputs to it or widen it.
8. **The advisory fold** — Hy4 self-committed at round 7 despite the brief's "no git — the fold belongs to the head"; the gate permits git verbs. Parent: brief-level discipline is advisory until the gate enforces it. STATUS: OPEN (named, accepted).

## The deliverable: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/HY4-LOOP-KAIZEN-20261118.md`
- `## The loop's run, receipted` — stages S1-S6 with commits, gates, and the byte-identity fold (sha `0327102f…`).
- `## The defect classes` — the eight, each with parent class, first-observed, primary evidence (log line or commit), counter, and status (FIXED/OPEN).
- `## The v2 loop spec` — the improvement wired in: the crash-safe logfile (final exception always appended), the evidence-acquittal (a gated read is a named forfeit; zero-successful-read lanes are flagged at the fold), the canonical-cell contract, the read-root/offset widening, the fold-gate enforcement, the tool-discovery fallback, and the multi-call trimming's handling.
- `## The double gift, amplified` — what the loop gave (findings + the deliverable), and what the kaizen adds.
- `## The closing line` — one sentence, the register.

## Disciplines (binding)
One tool call per round; write-first (skeleton by round 4); ≤6,000 chars per write; every class cites its primary evidence; verdicts three-state (CONFIRMED/FIXED/OPEN with the load-bearing evidence); commit + push the artifact when complete, then stop. RFC quiet; no /root/.hermes writes; the head gates and folds downstream.
