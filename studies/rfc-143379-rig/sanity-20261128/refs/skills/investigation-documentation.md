---
name: investigation-documentation
description: "Document verifications as peer-reviewable discovery logs."
version: 1.0.0
license: MIT
---

# Investigation Documentation — Discovery Logs

## When to use
After you have verified a claim, news item, or "alert" for a user who wants a coherent, auditable path a peer could review. Also when the user says "compile the path," "document how we got here," or "no drift / don't truncate."

## Two deliverable types — do not conflate
- **Discovery log (faithful):** turn-by-turn reconstruction of the reasoning chain. Preserves each step, the false starts, the geometric checks, the model missteps. This is what a peer audits.
- **Distilled review (synthesis):** compressed verdict + evidence. Useful as a summary, but it FLATTENS the method.

Rule: if the user asked for a faithful trail ("thought for thought," "highlight where we started," "no flattening"), give them the discovery log. Do NOT substitute a distilled review. When comparing, keep BOTH files; do not overwrite one with the other.

## Structure of a discovery log (generalizable from research-paper-writing)
1. **Lead with the origin.** Start from where the user actually began — a news-alert pop-up, a pasted headline, a screenshot. Name the originating (often non-primary) sources explicitly.
2. **Reconstruct each turn** as a numbered section: what the user asked, what was searched/extracted, what was found, what the geometric/arithmetic check showed, what the next steer was. Preserve missteps as sections, not footnotes.
3. **End with Limitations + Reproducibility sections** (from research-paper-writing, not ML-specific): state what was read via extraction vs re-rendered, what critique is "by extension," what raw data was withheld, and give re-runnable commands + the citation-ledger location.
4. **Remove accidental content.** If an unrelated link/item was pasted by mistake (e.g., from another chat), check relevance and DELETE it — do not leave it as an "aside." A neutral one-line lesson can be folded into a thematically appropriate section instead.

## Citation discipline (use grounded-citations)
- Register every source at retrieval with `sources.py add`; cite inline as [n]; render the Sources block with `sources.py render --cited-in <file>`.
- Run `sources.py verify <file>` and require "citations OK" before delivering. No memory-authored citations.
- Orphan ids in the ledger that the body doesn't cite are fine; orphan ids in the BODY that aren't in Sources are a failure — fix the Sources block, not the body.

## Skill-consultation discipline (load-bearing lesson)
When the user says "call in the research paper skill" (or names any skill to use): **actually load and read its `references/` directory.** Do not judge a skill irrelevant from its SKILL.md title or intro. `research-paper-writing`'s SKILL.md truncates at ~108k chars and is framed for NeurIPS/ICML — its transferable methodology lives in `references/writing-guide.md` (narrative principle, Gopen & Swan clarity, active voice) and `references/checklists.md` (mandatory Limitations + Reproducibility sections, citation verification). Those apply to ANY peer-reviewable document.

## Relationship to two-model-reasoning
The discovery log is typically the OUTPUT of a `two-model-reasoning` investigation: the cloud model verifies + reviews, the offline model reasons, and the log documents the whole path. Use both together.

## Pitfalls
- **A claimed grounding read is a claim — verify it against the turn's tool calls (earned 10-02).** "Re-anchored" / "grounded on MEMORY.md" asserted without executed reads (the file, the INDEX, the owning segments, the skills) is an unverified self-report, the same class as a lane claiming "facts preserved: ALL" without a token scan. The user audits this directly: a session that said "re-anchored" repeatedly while showing no reads was caught cold ("you must've just glanced at it and not actually processed what it said"). The grounding pass is visible in the tool calls — anchor → INDEX → owning segments → skills → then act. Never narrate the ritual; execute it, and when the user flags a claimed read, the fix is the full read on the record, not a re-assertion.
- Substituting a distilled review for a requested faithful log (flattening).
- Judging a named skill irrelevant by its title and bypassing it.
- Leaving an accidentally-pasted unrelated item as an aside instead of removing it.
- Citation drift: body cites an id the Sources block omits, or vice versa.
- **Folding a causal claim from a correlation (binding, earned 09-25):** a finding that two events correlate (a model worked at 09:xx and 404'd by 17:xx) is a VERIFIED TIMELINE; the causal claim (demand pressure removed it) is a HYPOTHESIS unless the mechanism was directly observed. Bank the timeline with causation labeled UNKNOWN — never fold a plausible mechanism as a lesson. When the user flags uncertainty about a banked lesson, the flag is a trigger: re-examine the entry, strip the unverified causal claim, and keep only what the evidence holds. A correlation stays a correlation until proven otherwise.

## Support files
- `templates/discovery-log.md` — starter skeleton for a faithful discovery log.
