# TEAM FRESH-EYES — Un-primed read adjudication
**Artifact:** IMPROVED-S2U-DRAFT-FINAL4-20261111.md  
**Read mode:** Cold / un-primed (no record, no night, no rig)  
**Skills:** No skill_view tool is loadable at this lane's dispatch; the all-skills default is named-refused. Proceeding with read_file, write_file, list_dir, terminal only. The calibration-clause applies.

---

## Landing assessment

### (a) Does the ask land in the first screen?
**No.** The title ("the corrective final: the read-restore underneath the P4 label") hints at a mismatch but never states it. Section 1 ("What I'm trying to understand") spends 147 words on context before the conflict appears. The actual request — "re-triage the RFC's label against its own body's centerpiece" — doesn't surface until §9, eight sections and ~2,500 words later. A maintainer reading cold has no idea what is being asked of them in the first scroll.

### (b) Does the evidence order build the case or bury it?
**It buries it.** The document opens with context (§1), then jumps to a core wound (§2), then floods the reader with quantification (§3), queue shape (§4), execution ledger (§5), user cost (§6), hinge (§7), and open doors (§8) before finally reaching the ask (§9). The evidence is strong, but the ordering is thematic rather than argumentative: it piles corroboration before the reader knows what is being corroborated. The repetition of queue shape (§4, §10, §13) and label trail (§7, §10) makes the middle feel like a loop, not a ladder.

### (c) Where would a busy maintainer's eye skip, and what would they miss?
- **Skip §3 (quantification):** "43% drift class," "~726,000 lines," "~58,500 hours" — too many big numbers without a plain-language anchor. The maintainer misses the single most powerful fact: nearly half of recent issues share one root cause.
- **Skip §10 and §13:** These sections repeat the queue shape and label trail already given in §4 and §7. The maintainer treats them as padding and scrolls past, missing nothing new.
- **Miss §9 (the ask):** Because it is at the bottom, after the changelog and verdict, the maintainer may never reach it. They leave knowing the problem but not what the author wants.

### (d) Is the register one a maintainer would answer, or one they'd skim?
**They'd skim.** The register is dense with internal jargon ("drift class," "compensation," "execution ledger," "read-gap's measured signature," "category-fluctuation exhibit"). Sentences like "The drift's the compounding, not the clearing" are memorable but opaque to a cold reader. The gratitude (§8) and two-way-door framing are well-calibrated, but they arrive after the maintainer has already bounced off the jargon wall.

### (e) Tone: humility without deference, firmness without demand
**Mostly there, but it gets lost in density.** The document names specific reviewers (jfugalde, xngg1021, Finn763), cites exact commits and line numbers, opens two-way doors in §8, and avoids ultimatums. That is the correct operator tone. However, the tone is buried under academic sentence architecture ("the execution-confirmed gap," "the compensation's true shape"). A skeptical maintainer would not find the humility; they would find a wall.

---

## The three highest-leverage edits

### Edit 1 — Surface the ask in the opening (replace title + §1)
**Current text:**
```
# RFC #143379 — the corrective final: the read-restore underneath the P4 label, quantified by the record's own thread

## 1. What I'm trying to understand

I'm reading the RFC's full record end to end — body and thread — and the label trail. The body's own theme: the durable record survives the session's compression with its provenance intact, and the agent re-reads it rather than make the user repeat — the read restored, the store re-readable, the compaction governed, as one network. The body names the restore (#141876) as the retrieval the listening mechanism rides on; the repo's triage has it P2. The RFC itself wears P4. Underneath the label question is the severity question: is this a nice-to-have pilot, or the memory path's core capability missing? The thread's own numbers answer it — and so does the queue's own shape.
```

**Replacement text:**
```
# RFC #143379 — the read-restore is P2; the label should match

The RFC's body names #141876 (the read-restore) as its centerpiece. That work is triaged P2 in the repo. The RFC itself is labeled P4. **Ask:** re-triage the RFC to match its own centerpiece, and explain the P2→P3→P4 trail if the P4 is intentional.

The body's theme: the durable record survives session compression with provenance intact, and the agent re-reads it rather than make the user repeat. The thread's numbers and the queue's shape confirm this isn't a nice-to-have pilot — it's the memory path's core wound.
```

**Why:** The current version buries the request eight sections deep. A maintainer reading cold needs the conflict (P2 centerpiece, P4 label) and the ask in the first 100 words. This edit turns the title into a headline and the opening into a brief, so the reader knows immediately whether to keep reading.

---

### Edit 2 — Delete the duplicated queue-shape section (§13)
**Current text (§13):**
```
## 13. The queue's exact shape (measured twice, corrected)

P0: 1 · P1: 119 · P2: 8,799 · P3: 9,787 · P4: 120 · unlabeled: 173 (exact-label counts, 11-11, sample-verified against the substring-collision class). The P4 bucket is the queue's smallest; the drift class already fills a fifth of it; the RFC sits two bands below where the queue works (~18,586 in P2/P3). The label's departure from the queue's own shape is measured, not asserted.
```

**Replacement text:**
```
[Removed — duplicates the queue P-shape already measured in §4.]
```

**Why:** Three passes over the same P-shape numbers (§4, §10, §13) create fatigue. The first measurement (§4) is sufficient; repeating it with "exact" counts in §13 adds no new argument, only length. A maintainer who sees the same stat three times assumes padding and stops reading.

---

### Edit 3 — Translate "drift class" into plain language in §3
**Current text:**
"Of the 300 most recent open issues, 43% (130) sit in the drift class — the session, the memory, the context, the compression, the state, the persistence, the recovery."

**Replacement text:**
"Of the 300 most recent open issues, 43% (130) are about session memory, context compression, or state persistence — the exact class broken by removing the read-action in `56ee8a5cc6`."

**Why:** "Drift class" is internal jargon that forces the reader to decode the next clause before the evidence lands. Plain language lands the fact immediately: nearly half of recent issues trace to one root cause. The quantified follow-up (~7,300 open issues, ~726,000 lines of compensation) then has an anchor instead of hanging in jargon-space.

---

## Verdict

**Would this comment get a substantive reply from a skeptical maintainer?**  
**No.**

**The one condition that flips it:**  
Surface the ask in the opening paragraph and delete the duplicated sections (§10 and §13). The underlying evidence is strong — specific commits, line numbers, named reviewer executions, quantified queue impact, a measured label trail — but it is currently packaged as a research dossier rather than a maintainer request. If the first screen states the conflict (P2 centerpiece, P4 label) and the request (re-triage or explain), a skeptical maintainer has a clear entry point. Without that, the comment reads like background reading they don't have time for.
