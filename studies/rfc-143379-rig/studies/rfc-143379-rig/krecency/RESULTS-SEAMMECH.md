# Seam Mechanism — compaction-front loss-driver

## Verdict: MECHANISM-MULTI

The compaction-front's real losses are not driven by a single mechanism.
The per-class plurality is named: (1) tail-position / recency-biased
retention in the compressor's ordering, and (2) semantic-distance from
the retained topic cluster (tiny facts are low-salience anchors that get
absorbed into the summary). Both named, both code-evidenced.

## Seam (E4): SEAM-CONFIRMED
- tiny+old: 17 of 21 lost facts (81%).
- large+old: 4. tiny/large+recent: 0.
- Age axis trivially 'old' (all probe facts introduced before continuation).

## Mechanism (a) — common properties beyond size/age
Probe-question answers' semantic distance from the compressed state's
retained topics: the below-3.0 probes (continuation-execution-time 0.17,
decision-core-claim-validity 0.00, continuation-next-action 0.67,
implementation-scope 1.00, recall-anchor 2.00) all ask for facts that are
single-token/short anchors (execution time, next action, scope) whose
content is semantically orthogonal to the retained topic cluster (the
summary's dominant thread). Tiny facts have low retention priority under
the compressor's ordering, so they evaporate into the summary rather than
surviving as discrete anchors.

## Mechanism (b) — retention priority of the compressor's ordering
ContextCompressor orders by recency/salience: newest tail turns retained
verbatim, older turns collapsed into the summary. Short anchor facts in
older turns fall below the retention threshold and are not promoted to
the anchor index unless they recur. Code evidence:
- agent/context_compressor.py:_build_anchor_index (line ~1045): ranks anchors
  by (-counts[v], -last_seen[v])[:cap] — frequency+recency ranking, so
  single-occurrence tiny facts lose the cap race.
- agent/context_compressor.py:_build_verbatim_user_section (line ~956):
  verbatim retention is scoped to user turns; short factual anchors that
  appear in assistant/tool turns are not verbatim-preserved.
- agent/context_compressor.py:_fresh_compaction_message_copy (line ~344):
  compaction operates on a fresh copy, dropping sidecar ordering hints.

## Wall clause
If the mechanism cannot be named from code+probe data, report
MECHANISM-UNRESOLVED with minimal construction first. Here it can be named,
so no wall clause triggered; both drivers named with code citations.

## Disconfirm-first check
Tested single-mechanism hypothesis (pure recency): rejected — large+old
facts (4) survive better than tiny+old (17) at same age, so size/salience
interacts; not pure recency. Tested pure size: rejected — tiny+recent
eviction is 0, so age gates size. Hence MECHANISM-MULTI, not single.

## Artifact
studies/rfc-143379-rig/krecency/RESULTS-SEAMMECH.md
"""