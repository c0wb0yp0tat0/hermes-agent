# hy — HITL GIST / flagship plan (RFC #143379)

**DRAFT — nothing is posted. This document is the human-in-the-loop review artifact; the posting word is the operator's alone.**

[Executive Summary]

**State.** The read-restore track is receipted, not resolved. The receipt `3ff6aee4…fba9` has not moved across any runner. Our main comment (7185328530) carried the condition, the `268bb091` reproduction, the 34/34 suite, the kit, the trinity's instruments, the advisory, and the child-RFC shape. 3oltan-seo's contour run (7183339657) held as-at-pin GREEN / lock-removed GREEN / cache-write-restored GREEN / both-removed RED, envelope as predicted, his gate held open; his two kit notes — Python 3.10+/PEP 604 and the `PILOTKIT-` prefix seam — both landed. kvnloo's cold run (7186196454) found two real faults: the cold `sh RUN.sh` failed on the `store_source` fallback because the shipped name was missing, and the envelope stubs `fcntl=None`, so rows 1–2 never exercised the lock — his table 5/5 against real-fcntl 0/5 establishes that determinism is not lock-order. He prescribed one small diff in `_add_doc` (locked re-read → append → write under the anchor's lock, one regression test with real fcntl) and answered the summary-class question: the useful check is whether `read()` was called at all on that turn. Our reply (7186351716) received his findings with his measurements, named the probe fix, agreed the morning team-up, carried the trackers' weight, stated the divergence, put the @xngg1021 guidance ask in its own section, and closed in the operator's register. The probe fix is pushed at `de705780` (real fcntl/msvcrt, done-wait dropped, shipped-name fallback added); the local post-fix run reads GREEN·GREEN·GREEN·RED with the receipt still unmoved.

**Next move.** Confirm the pushed fix with an independent cold re-run, then land kvnloo's `_add_doc` diff with one real-fcntl regression test, bring both to the morning session, and hold the guidance fold until guidance is actually received. The confirmation leg never precedes its artifact: the artifact (`de705780`) exists, so verification runs first among the active work.

**Decision asked.** (1) Release the posting word on the suggested reply in [Artifact]. (2) Confirm the fleet seats in the assignment plan. (3) Rule on the divergence — whether governance-fork lanes may verify clean against the governance surface and report "unexpected greens" as governance-clean rather than read-restore-green. (4) Any pending public-surface change waits on the CTO's word; no re-ask, no self-gate. The thesis stays withheld.

[Analysis Brief]

**(a) What we think we know — receipted, not inferred.** The condition and its `268bb091` reproduction and the 34/34 suite are in the main comment. The receipt `3ff6aee4…fba9` is unmoved across our run, 3oltan-seo's contour run, and the local post-fix run. Both of kvnloo's cold-start faults are concrete and measured, and his determinism-versus-lock-order distinction holds on the evidence: a stubbed `fcntl=None` cannot exercise the lock, so 5/5 there is not a lock result. His prescription and his summary-class answer are on record. His trackers' weight is on record — Nov 25th, 57/56, the P4-undersell quote, the roadmap line, OpenClaw's double P0 cell, the memory-trust thesis. The probe fix is pushed at `de705780` with the three named changes; the local result after the fix is GREEN·GREEN·GREEN·RED, receipt unmoved. Everything above this line is measured or quoted. What is not known is held as open questions, never positions: the outcome of an independent re-run of `de705780`; the content of @xngg1021's guidance; the P0's fate; the maintainers' decision.

**(b) What we hope — the outside, held as hope, not fact.** We hope the maintainers read the read-restore condition as a class and not a one-off; we hope the P0 resolves in a direction that keeps the store landing small; we hope @xngg1021's guidance sharpens the fold rather than re-scoping it; we hope the memory-trust thesis — the through-line of the trackers' weight — gains a second independent reader. None of this is receipted, so none of it drives a commitment. The standing harvest is corroboration of class only, with design staying ours: SELD and AskALCF corroborate the `read()`-called evidence plane and the evidence-gated commit discipline of the verification leg; DISCERN's write-gate with SPA-DREAM's read path corroborate the locked re-read → append → write ordering; MemCredit's memory-economy arbitration and CoMem's fidelity-ladder selection corroborate the memory-trust thesis and the contour's as-at pinning; Reward-Driven Collider's adaptive envelope corroborates the envelope instrument; MAPE's design-space search, Evolving Infra's agent-adaptive serving, and the four misc items — compile-time gating, stage-decoupled evaluation, validity decay, three-state delegation — corroborate probe search, serving, and the delegation shape respectively. These are lenses, never adoptions, and nothing in the landing is resized to fit them.

**(c) The fleet assignment plan.** Two forks carry the work. The study fork, `c0wb0yp0tat0/hermes-agent` at `study/rfc-143379-rig-20261105`, holds the read-restore class, which stays the highest priority. The governance fork, `c0wb0yp0tat0/agent-governance-toolkit` (fork=true), holds governance-surface verification; that is where "unexpected greens" like the study's peak are explained — they verify clean against the governance surface, not the read-restore one, and are reported as such. Fleet: hy and solar at flagship; the free pool of laguna, longcat, stepfun, and the proven bases fills the seats.

| Work stream | Owner / seat | Fork / branch | Depends on | Gate |
|---|---|---|---|---|
| 1. Probe-fix verification re-run | laguna; solar shadows | study fork, `study/rfc-143379-rig-20261105` | Artifact `de705780` (pushed, exists) | Independent cold run reproduces GREEN·GREEN·GREEN·RED, receipt unmoved `3ff6aee4…fba9`, and rows 1–2 now exercise real fcntl. This is the confirmation leg; it never precedes its artifact. |
| 2. `_add_doc` landing diff + real-fcntl regression test | hy (flagship) | study fork, same branch | Stream 1 green — real fcntl confirmed usable in the rig | Locked re-read → append → write under the anchor's lock; one regression test that fails when the lock is removed; one small diff on the store, no new mechanism. |
| 3. Morning team-up with kvnloo | hy, paired with solar | study fork, same branch | Streams 1 and 2 in hand | Bring a verified result and the diff; accept his measurements over assertions; review the diff before any claim of landing. |
| 4. @xngg1021 guidance fold | solar, one free-pool lane supporting | governance fork where the guidance bears on the governance surface | Guidance actually received (external gate) | Fold only on receipt; never guess its content; if it bears on governance, verify clean against that surface. Held — not started. |
| 5. Radar watch | longcat + stepfun; governance-fork lanes on the governance surface | both forks, read-only | None — continuous throughout | Log the two trackers, the memory-trust thesis, and the P0 watch; classify any unexpected green by which surface it verifies clean against before reporting it. |

Sequencing is dependency-first. Stream 1 runs now because its artifact is already pushed. Streams 2 and 3 key off stream 1 and run together in the morning, with the diff reviewed before any landing claim. Stream 4 is parked on an external gate. Stream 5 runs underneath all of it. No confirmation leg is scheduled ahead of its artifact.

[Recommendation / Action Plan]

1. **Verify the probe fix.** Owner laguna, solar shadowing. Independent cold re-run of `de705780` on the study branch. Gate: reproduced GREEN·GREEN·GREEN·RED, receipt unmoved, real fcntl exercised in rows 1–2. Until that gate closes, the fix is pushed and locally green, not confirmed.
2. **Land the store diff.** Owner hy. Implement the one-diff prescription in `_add_doc` plus one real-fcntl regression test. Gate: the test fails when the lock is removed; the change stays one small diff on the store; no new mechanism. If the test does not discriminate lock-present from lock-removed, do not land.
3. **Hold the morning session.** Owners hy and solar. Bring the verified stream-1 result and the stream-2 diff to kvnloo; review his findings against his measurements. Gate: his review of the diff before any public claim of landing.
4. **Park the guidance fold.** Owner solar on the governance fork. Do not fold @xngg1021's guidance until it arrives; when it does, route it to the surface it bears on and verify clean there. Gate: receipt of the actual guidance.
5. **Keep the radar on.** Owners longcat and stepfun. Continuous watch of the two trackers, the memory-trust thesis, and the P0; classify unexpected greens by surface. Gate: report only what is receipted; hold the rest as questions.
6. **Posting.** Only on the operator's word. The reply below is staged, not sent; pending public-surface changes await the CTO's word, with no re-ask and no self-gate.

[Next Steps / Exploration]

We are watching four things and treating each as open, not settled: the independent re-run result for `de705780` (a divergence there holds streams 2 and 3); kvnloo's read of the `_add_doc` diff at the morning session (a finding there changes the diff, not the mechanism); @xngg1021's guidance (its content could re-scope stream 4 — we hold the seat and do not guess the answer to the ask); and the maintainers' decision and the P0's fate, read through the two trackers and the memory-trust thesis. What could change the plan: a re-run that does not reproduce the local four-cell result; a regression test that cannot tell lock-present from lock-removed; guidance that lands on the governance surface and turns an "unexpected green" into a governance-clean result; a public-surface change that requires the CTO's word before it fires. Two-way doors, kept open deliberately: revert the store diff if the regression test does not discriminate; keep the reply unposted until the word; re-scope or stand down the morning session if stream 1 does not confirm; park the guidance fold indefinitely rather than fold on assumption. The thesis stays withheld, and the harvest stays corroboration of class, never adoption.

[Artifact]

*Suggested next comment to the thread — addressees @kvnloo, @3oltan-seo, @xngg1021. Full text, staged only; postable after the operator's word.*

---

@kvnloo @3oltan-seo @xngg1021 —

Following up on the read-restore thread.

@kvnloo — your cold-run findings were right, and we acted on both. The shipped-name fallback is fixed, and the probe now carries a real fcntl/msvcrt lock with the done-wait dropped; that is pushed as `de705780`. On our side the local run after the fix reads GREEN·GREEN·GREEN·RED with the receipt still at `3ff6aee4…fba9`. The distinction you drew between determinism and lock-order is the thing we are holding onto: 5/5 with fcntl stubbed out was never evidence the lock works, and 0/5 with the real lock is. On the summary-class question we are with your answer — the useful check is whether `read()` was called at all on that turn, not what came back. We have an independent cold re-run of the fix queued and will post its result before we call it confirmed.

On the store, we are taking your landing as you drew it: in `_add_doc`, a locked re-read, an append, and a write under the anchor's lock, with one regression test using real fcntl. One small diff on the store, no new mechanism. We will bring the diff to the morning session for your review.

@3oltan-seo — your contour run held up: as-at-pin green, lock-removed green, cache-write-restored green, both-removed red, receipt unmoved, envelope as predicted. Both of your kit notes landed — Python 3.10+/PEP 604 and the `PILOTKIT-` prefix seam. Thank you for keeping your gate open.

@xngg1021 — the guidance ask, in its own section. We put it to you before, and we would value your read before we finalize the store landing: given the read-restore condition and the one-diff landing described above, where does this sit with you, and is there a correction you want us to fold in? We are holding the seat open and will not guess at your answer.

Morning it is. We hold to two things here: we do not guess, and the results arrive.

*Prepared with Hermes and reviewed by @c0wb0yp0tat0 before posting.*
