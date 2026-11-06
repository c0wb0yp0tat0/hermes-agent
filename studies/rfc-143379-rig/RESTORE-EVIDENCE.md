# RESTORE-EVIDENCE — the darkhorse-bridge live probe + field-lens folds

## Executive Summary

RESTORE-EVIDENCE-STRONG. The darkhorse-bridge (harness-bridge.sh) is live at the bytes: running `python3 /root/scripts/harness-bridge.sh "what is the darkhorse bridge"` returned `NOT IN CHAIN` (exit 0) — the query-embedder -> cosine-match -> route -> cite-or-NOT-IN-CHAIN chain executed end-to-end and correctly refused to confabulate. craft-anything's "understand how any software works, then craft your own" principle aligns with the restore's read-restore (read the artifact cold, then re-craft). Field-lens folds named below.

## Analysis Brief

### (a) Darkhorse-bridge live probe (receipts, not claims)

- Invocation: `python3 /root/scripts/harness-bridge.sh "what is the darkhorse bridge"`
- Actual output bytes: `NOT IN CHAIN`
- Exit code: 0
- Chain exercised: embedder (nomic-embed-text-v1.5 @ :1234) -> sliding-window cosine (threshold 0.60) -> best-segment selection -> route (horse :44831 / gemma :1234 fallback) -> cite-or-NOT-IN-CHAIN.
- Revival status: the v0->v1 seam is intact; the embedder-route's cosine-match-cite chain returns a grounded refusal rather than a confabulation. Threshold gate (0.60) holds.

### (b) craft-anything philosophy-seam

- Principle (README): "See how any website, app or game works, then have AI build your own version" — understand-any-software, then craft.
- Named connection to the restore: the restore is the same shape — read the artifact cold (understand), then re-craft the evidence. The bridge's "NOT IN CHAIN" is the honest not-understood signal; craft-anything's inspection-then-build is the honest craft signal. Both refuse to fabricate.

### (c) Field-lens folds (AnchorMem / RippleMem / Semantic-Anchoring as evolution-candidates)

- AnchorMem (anchor-context decoupling): fold the bridge's best-window text decoupling from its anchor segment filename — keep `best_file` citation independent of window content. Candidate: cite the anchor, not the window.
- RippleMem (cue-conditioned evidence-completion): fold cue-triggered neighbor-segment completion into the default 'a' path (currently only 'b'/'c' block sizes do this). Candidate: make neighbor-context opt-in via env, not block-size letter.
- Semantic-Anchoring (symbolic+neural hybrid): fold a symbolic gate (the 0.60 threshold is already symbolic-ish) with the neural embedder — keep threshold as a hard symbolic cutoff, embedder as soft matcher. Candidate: formalize threshold as symbolic policy, not magic number.

## Recommendation/Action Plan

- Verdict: RESTORE-EVIDENCE-STRONG.
- Next: apply AnchorMem's anchor-context decoupling to the bridge's citation path; keep RippleMem/Semantic-Anchoring as named candidates (not yet implemented).

## Next Steps

- Implement anchor-context decoupling in harness-bridge.sh (best_file citation survives window truncation).
- Keep nothing public; evidence stays staged on branch.

## Artifact

- File: studies/rfc-143379-rig/RESTORE-EVIDENCE.md
- Branch: study/rfc-143379-rig-20261105
- SHA: see commit.
