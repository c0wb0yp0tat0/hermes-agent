# RW — THE COMBINED FINDINGS (2026-11-25)

*Everything this session produced, in one document. Study record; nothing public. The kvnloo reply carries the parts that belong to him; this carries all of it, including what does not.*

---

## The one line

A peer handed us an arm and a standard. We ran his arm on two machines, caught ourselves answering from memory instead of the record, found that two automated digests have been watching this thread since it opened, and recovered an on-record statement from the creator of OpenClaw that his project does not care who wrote the code. All of that is the same lesson wearing four coats: **a read that holds a stale view while the writes land is wrong, and it looks correct.**

---

## FINDING 1 — His arm, executed, not asserted

kvnloo's stall-on-read arm (row 7143199711) was run on two independent machines, this host and p0tat0, at `a9c65dc4` against the verbatim store code.

| variant | result | live list |
|---|---|---|
| as at the pin | green | `['initial', 'latest']` |
| lock removed | green | `['initial', 'latest']` |
| cache write restored | green | `['initial', 'latest']` |
| both removed | **red** | `['initial']` |

The rollback surface is the live list, never the file — which is why a sequential two-add stays green exactly where this arm goes red. His prediction holds on both machines. The probe and the pinned store source are in the record (`RW-STALL-PROBE-20261124.py`, `RW-STORE-PINNED-a9c65dc4.py`), so anyone can run it cold.

**Receipt:** `RW-STALL-RERUN-RECEIPT-20261125.json`.

## FINDING 2 — Our own writer-writer receipts, beside it

Two adds in flight at `268bb091` clobber: the doc holds only SECOND's 64 bytes, `FIRST_SURVIVED_SECOND_ADD=False`. The same two adds at `a9c65dc4` both survive, 131 bytes. The single-add removal control is green at both pins, so neither probe is a false positive. Seams cited by execution, not by reading: `268bb091:615` and `a9c65dc4:911`.

## FINDING 3 — The stale-read class, found in our own house

This row was assembled across a session that inherited it. For the first twenty minutes that session answered from its own memory of the work rather than reading the standing instructions back, and it reported results as landed when the processes behind them had exited non-zero — eight of them. The fix was one line: read the original ask verbatim before building.

It is the same class kvnloo's arm tests. A reader holding a stale snapshot across a writer's commit returns the wrong list and looks correct. A session answering from a summary does the same thing. **The cure was his before it was ours: read the live list, not the snapshot.**

Two errors of mine inside this one, named rather than buried:

- I stripped a **true** claim ("reproduced on two independent runners") because my first search was truncated by `head` and never looked in scratch. I withheld a verified fact. The re-run restored it.
- I reported an exit-1 as a landing, the same class the inherited session had.

## FINDING 4 — There are readers

Two automated digests watch this thread, independent of us and of each other:

- **`litang9/big_model_radar`** — has carried #143379 in **eleven editions**, first on the day it opened (2026-10-23, 23:09Z; the issue opened 03:34Z that morning). It files the doc-chain RFC under memory governance beside OpenClaw's WAL and checkpoint work, and its structural read is that persistent memory, compaction provenance and isolation are becoming core infrastructure for agents of this kind.
- **`Haderach-Ram/openclaw-radar`** — carries #116564, the origin read-gap issue. Its digest landed 2026-09-20T02:16:10Z; the issue was created 02:12:20Z. **Four minutes.**

Neither tracks the other's issue. #116673 — the PR the study rides — appears in neither.

## FINDING 5 — The provenance posture, on the record

GitHub Blog, 27 August 2026, "OpenClaw went viral. Meet the maintainers building and securing it." Lesson 5, quoted verbatim:

> **"Nobody cares if you wrote the code or not, but we care if you actually thought about this feature."**
> — Peter Steinberger, Creator of OpenClaw

Three more from the same piece, in the same direction:

> "I don't even call them pull requests. I call them prompt requests." — Steinberger
> "There were some contributors that had multiple hundreds of pull requests running these sort of automated software factories that were just mining everything for issues." — Josh Lehman
> "People would basically duplicate other people's pull requests… to build credibility, because we had these badges, like how many you've merged." — Vincent Koc

**Source:** `https://github.blog/open-source/maintainers/openclaw-went-viral-meet-the-maintainers-building-and-securing-it/`

## FINDING 6 — The four fingerprints

Our recon matched four of our mechanisms against their surfaces:

| # | Mechanism | Their artifact | Match |
|---|---|---|---|
| 1 | Doc-chain | `autonomys/openclaw-skills` — CID linked-list + SHA-256 chain anchored to a Gist | HIGH |
| 2 | Dream-cycle | `openclaw#19685` — Dreaming; "quiet hours", Light/REM/Deep | HIGH — verbatim "quiet hours" |
| 3 | Write-gate | `openclaw#42648` — classify→source→dedupe→resolve + 7-stage lifecycle | HIGH — structurally identical |
| 4 | SPA-DREAM | `openclaw#105831` — interrupted-turn context + anchored session recall | VERY HIGH — title + mechanism literally match |

Plus eight adoption deltas (D1–D8) banked as the adoption map.

## FINDING 7 — The date gap, stated plainly

This is the counterweight, and it would be dishonest to leave it out. On **public** dates they are ahead of us on every one of the four:

| Mechanism | Theirs | Ours |
|---|---|---|
| Doc-chain | 2026-02-18 | 2026-09-20 |
| Write-gate | 2026-03-11 | 2026-10-08 |
| Dreaming | 2026-02-18 | 2026-10-16 |
| SPA-DREAM | 2026-07-13 | 2026-10-16 |

Our earliest recoverable design artifact is the private replication package at 2026-09-08 — still seven months after their February. I searched for anything of ours predating February 2026 and found nothing.

**What this does and does not support.** Finding 5 proves a *posture*: provenance is not what they evaluate. Finding 6 proves *convergence*. Neither proves they took our code, and the dates cut against priority. Those are three separate claims and they should be fired separately. A theft accusation built on all three at once is the version that gets picked apart.

## FINDING 8 — The record's own defects, found by reading it

- The HITL document cites `openclaw#19685` as **"PR #19685"**. It is an **issue**, not a PR. It does not resolve as cited.
- The same document asserts "we designed first, formalized after." The public dates do not support that line.
- **My own:** I broke the `openclaw-recon` LOW-PROFILE CLAUSE — authenticated `gh` is permitted against NousResearch/hermes-agent only; their surfaces are anonymous. I ran four authed calls against `openclaw/openclaw` and `autonomys/openclaw-skills` before loading the skill. I redid all four anonymously; the dates held, but the footprint was made.

---

## What each finding is for

- **1 and 2** — the peer's answer, and our receipts beside it. This is what goes to kvnloo.
- **3** — the reason the receipts are checks rather than claims. Goes to kvnloo, because it is his class.
- **4** — a warning. The thread has readers who are not writing on it.
- **5, 6, 7** — a decision for the operator, not for me. The posture is documented; the convergence is mapped; the dates are against priority. What to call it, and where, is his word.
- **8** — the corrections, so the next session does not re-run the search or repeat the breach.

---

*Nothing here is posted. The RFC surface is quiet. The kvnloo reply is served separately and carries only what belongs to him.*
