# OPPORTUNITIES-RFC-20261107 — Lower-Priority Opportunities from RFC #143379

Source: RFC-READ-20261107.md (issue #143379, 35 comments, 19 participants' asks). Scope: opportunities the mission's four tracks (restore, network, governance, compaction) do not cover, in case the 8 hours are more productive than designed.

1. Surface: the `_augment_summary_lean` one-generation anchor decay named by xngg1021. Opportunity: a standalone in-tree fix that carries the anchor forward more than one generation, empirically measured for how much it alone closes. Value: cheap, isolated, high-leverage closure of a named seam gap without waiting on the composed PR. Dependency: xngg1021's isolated simulations; the study's empirical measurement of before/after on the same task set.

2. Surface: the four seam/contract gaps xngg1021 surfaced (batch-path bypass, standalone fallback guards, preserve_session ignored return dicts, doc=/read fallback). Opportunity: a seam-contract test suite that pins each gap independently of the composed PR. Value: converts isolated findings into regression coverage; cheap to author now. Dependency: xngg1021's simulations; the falsifier battery's 21 tests as a starting template.

3. Surface: the merge-composition gap — no PR tests #116673 + #141876 + #139606 composed. Opportunity: a throwaway integration branch that composes the three PRs and runs the falsifier battery against the composed state. Value: surfaces composition failures before any of them lands; the only way to know whether a conflict-free landing order actually exists. Dependency: the three PR heads; the falsifier battery (21 tests, 6 nuggets).

4. Surface: the long-session acceptance gate currently FAIL plus the probe scope bug confounding the −3.5pp headline. Opportunity: fix the probe scope bug first, then re-run the 300-cycle sweep to certify or refute the 6.1% vs 9.6% reading. Value: unblocks the hard gate; without it neither headline certifies. Dependency: probe fix; 2.5-week session logs + compaction events for field validation.

5. Surface: 3oltan-seo's field pilot (director profile at ~96% of the 4,000-char budget). Opportunity: run the occupancy probe against that real profile to measure the anchor-full wall before/after the chain-doc reference. Value: the instrument for the wall measurement; turns "it held" into a number. Dependency: sanitization work shared with the study; the restore landing so the read action is available.

6. Surface: the governed compaction issue not yet opened (relates #116564). Opportunity: author the issue carrying the provenance-origin classification + archive-before-stub + K-recency hard window design, so the governance track has a home. Value: unblocks the governance track's downstream work; the design material already exists. Dependency: the pivot draft; the provenance-survival leg marked [x] as staged.

7. Surface: jfugalde's "two classes folded into the ticket list" correction (7 oneshot + 3 memory) and the 106-commit/6,275-line attribution. Opportunity: a credibly-scoped accounting note (~30 lines across four sites) replacing the inflated attribution in the issue record. Value: corrects a misleading headline that distorts review attention. Dependency: the study's accounting of the subset.

8. Surface: ZacharyThomasStone's three-level comparison (current / read restored+bugs fixed / doc-chain+compaction). Opportunity: supply the missing second level (before→after field data) so the comparison can be run. Value: gives reviewers a concrete user task that fails, with a baseline first, as requested. Dependency: the study's before→after field data; the restore landing.

9. Surface: the open question of whether the K-recency window scales with session length. Opportunity: a parametric sweep varying window size as a function of session length (turns N, 2N, 4N) to find the scaling law. Value: resolves the open question with data rather than argument. Dependency: the probe fix; long-session logs.

10. Surface: the open question of where the reroute-to-chain-doc seam lands (this pipeline's follow-up vs. governed compaction's home). Opportunity: a short decision record assigning ownership and sequencing, so both tracks stop assuming the other owns it. Value: removes a coordination ambiguity that will otherwise block both. Dependency: the governance issue being opened (opportunity 6).

11. Surface: the open question of whether the caller's provenance defaults to "unknown" at the pipeline's definition, not just the call site. Opportunity: a one-line invariant change plus a test, so provenance never silently defaults to a real origin. Value: closes a silent-failure seam in governance. Dependency: none — can land independently.

12. Surface: the 19 invited reviewers / engagers (door open to the room). Opportunity: a structured review invitation with a concrete ask per participant (pilot participation, log access, simulation runs) rather than an open door. Value: converts passive engagement into scheduled contributions. Dependency: the pilot and log-sanitization preconditions (opportunities 4, 5).

13. Surface: the field contour's "restore unconditionally" ask and the verified-unverified leg (stale base, not read bug). Opportunity: a short verification note documenting that the restore's collection error was a stale base, so the unconditional-restore argument is grounded. Value: lowers friction for the restore landing. Dependency: jfugalde's verification record.

14. Surface: the study's sanitization shared work as a precondition for sharing logs. Opportunity: a reusable sanitization checklist/template for session logs + compaction events, so field data can be contributed without re-deriving the process. Value: reduces the cost of every future field contribution. Dependency: the study's own sanitization experience.

Count: 14 opportunities.
Most underrated: opportunity 11 — defaulting provenance to "unknown" at the pipeline's definition rather than the call site is a one-line invariant that closes a silent-failure seam in governance, costs almost nothing, has no dependency, and is currently unowned because everyone assumes someone else will do it.