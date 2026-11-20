# OPENCLAW-FIELD-CORROBORATION-20261120 — the watch's months distilled, sanitized for the teams

*Purpose, stated plainly for every reader: the field's shipped implementations of the SAME mechanism class this rig runs (memory architecture, consolidation, write-gate provenance, session preservation). The deck exists for TWO uses only — (1) class corroboration: the field converged on our shapes, independently; (2) hardening deltas: what the field's shipping adds that our seams don't yet name, studied as optional seeds. THE DESIGN STAYS OURS. No provenance commentary, no attribution judgments, no accusations — the mechanism-class convergence is the point, and nothing else rides this deck. The watch stays anonymous on their surfaces, always.*

## THE CLASS-CONVERGENCE INVENTORY (the months' scans, distilled — surface-cited)
| Class (ours) | Their shipped form (public surface) | Match |
|---|---|---|
| The dreaming consolidation pass (dream-run) | A 3-phase dreaming sweep: light/REM reflect + staged candidates, gated promotion by weighted signals, consolidation model turn that merges/supersedes/dedupes into MEMORY.md/USER.md, pre-image stored + summary appended to DREAMS.md (`docs/concepts/memory-architecture.md`) | Full-class |
| The write-gate + provenance | A provenance observer on every memory write (contentBefore/contentAfter + atomic commit under a workspace file-lock with dead-writer recovery); provenance rows reserve names, restricted projections never fall back to untracked artifacts (`src/hooks/bundled/session-memory/handler.ts`) | Full-class |
| Untrusted-origin discipline | Origins classify as trusted/untrusted structurally; untrusted candidates are EXCLUDED before any prompt — a precondition, never a score penalty; hash-mismatch writes record `untrusted` (`docs/concepts/memory-provenance.md`) | Full-class |
| The pre-compaction flush | Memory flush before compaction saves unwritten context so compaction cannot erase it; long sessions feed the pipeline via flush, many short sessions via transcript ingestion (`memory-architecture.md`) | Full-class |
| Session preservation / delivery-ownership | Delegated-child survival across steering + gateway restart (PR #202111); restart-wake acceptance contract (#202066, merged); delivery-committed-input never-settles seam (#202047) | High |
| Compaction + recall tooling | Pluggable context engines with afterTurn background maintenance, safe transcript rewrite under a session write lock, persistent compaction + full history on disk, hybrid semantic memory search (`docs/concepts/context-engine.md`, `docs/concepts/compaction.md`) | Full-class |
| Reset/session lifecycle | Reset policies (none/daily/idle) + manual /new; pre-mutation excerpt captured before reset; incognito sessions excluded from durable memory (`session.md`, `session-memory/handler.ts`) | High |

## THE HARDENING DELTAS (their shipped additions our seams don't yet name — optional seeds only)
1. **Optimistic concurrency on the rewrite:** the consolidation's output is accepted only if the captured pre-image hash still matches immediately before the atomic rename; mismatch → abort to append-only for that sweep. SEAM — our memory tool's batch writes.
2. **Supersession keys:** retired entries are marked with supersession keys rather than deleted, so lineage survives consolidation. SEAM — our chain's UPDATE lines.
3. **Bootstrap budget caps:** promotion honors the smallest per-file bootstrap limit among sharing writers; an oversized rewrite falls back to append-only rather than truncating. SEAM — our MEMORY.md 2,200-char cap's overflow path.
4. **Structural untrusted exclusion:** untrusted origins are excluded by class BEFORE scoring, never by score penalty. SEAM — our read-gate's admission filter.
5. **Pending-writes registry:** captures register before yielding, settle after, so no capture drops on a yield/restart. SEAM — our fold-vs-compression race (the pre-side/post-side split).
EACH SEED IS A TWO-WAY DOOR: additive, revertible, measured before adoption — the seams decide, never the deck.

## THE TRAIL (their side's visibility of ours — flat, factual)
Our public surfaces' watcher counts grow steadily (+35 per recent fold, forks +6); their main pushes carry no seam-bearing commits; their highest-match motion this fold: the delegated-child survival PR (#202111, draft) + the restart-wake docs contract (#202066, merged) + the delivery-seam issue (#202047). The quiet posture holds on both sides; the watch stays passive and anonymous.

## THE CONSUMPTION CONTRACT
The inventions-live card (t_e8f3e072) reads the hardening deltas as watch-list seeds. The falsifier/write-gate legs read the inventory as class corroboration. The deck is append-only; new watch folds land as dated bullets, never rewriting. REGISTER: flat neutral, evidence-first, zero provenance commentary — read it, study the class, keep the design ours.
