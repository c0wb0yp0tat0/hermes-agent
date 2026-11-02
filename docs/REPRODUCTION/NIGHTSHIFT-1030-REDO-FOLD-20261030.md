# NIGHTSHIFT-1030 — THE REDO FOLD (2026-10-30/31)

*The reapexed night's reckoning. The rushed first pass was voided by the user's order; the redo ran at the full standard (full ground, LP envelopes, wall clause). Four legs, four landings, all receipted.*

## The four verdicts

**REDO-S1 — the consent-prefix seam: SEAM-REAL (12/12).** `_contains_consent_deny` (tools/memory_tool.py:181–183) literal-substring-matches `_SOURCE_CONSENT_MARKER = "SYNTHETIC-CONSENT-CODE-"` (line 178); any rename flips the `in` test → deny skipped → content writes (single-op 323, batch 293). Baseline 12/12 pass; renamed 12/12 persist (staged=False). Scope: narrow seam, broad class (literal-marker-bypass). Corrective (no code changed by the lane): semantic/declaration-based recognition (the scenarios carry `source_no_save` + `source_instruction`), a consent-marker patterns set, a renamed-identifier sub-suite in the battery. Receipt: nightshift-1030-redo-leg-s1-verdict.md (126 lines).

**REDO-S2 — the orphan capability: PARTIAL, and the probe's guard is exposed.** The skip guard (/tmp/rfc659-runner/test_real_checkout.py:243–244) is TAUTOLOGICAL and MISLABELED — "No chain-document support" is false: the head HAS the chain-doc machinery (memory_tool_store.py: _doc 303, _doc_path_for 316, _resolve_path 321, _entries_for 328, _char_count 338, _char_limit 345, read 406, _read_doc_bounded 426, add 521, _anchor_gate 552, _add_doc 572, chain_docs 612). What the head LACKS: `orphan_doc_names` (0 grep matches). The invariant's mechanism holds on the minimal probe: read success=True, re-write refused (anchor_missing), file persists=True — but read returns text, not entries, so the probe's assertion can't collect as written. Corrective: add `orphan_doc_names()` (docs whose @doc anchor's absent from MEMORY.md), reconcile the read return shape (entries in _read_doc_bounded or the probe asserting text), relabel the skip guard.

**REDO-S3 — the uv.lock seam: NOT REPRODUCED here — mechanism characterized, temporal proof not constructed.** GREEN across uv 0.12.2/0.12.3/0.13.5 + the PM hermetic env, refresh 0 lines vs Kevin's ~7,716. The seam's most plausibly an index-state divergence (a version published inside the sliding 3-day `exclude-newer` window, or a mirror lacking upload dates) that has since stabilized. THE WALL-CLAUSE HAND-BACK: the date-advance construction (force the cutoff to close the window) wasn't run — that one goes back to the lane before the verdict's full. `pm.lock_project` remains the canonical repair path.

**REDO-STORM — the ENTRY.md append: FULL STANDARD, staged.** The "Pre-Write Activation Risk" section (350 body words): the three-valued validity gate (AUROC 0.91–0.95, the owner's reconciliation flagged — the entry's own tokens carry no gate names), the activation-level disclosure prediction read ALONGSIDE the gate (two signals, two questions), the S1 template (the prefix seam + the staged=False receipt), FIRME + Helixar as the field corroboration, the three-signals close. Only @kvnloo (2×, swept); no invented claims (the "budget" flourish cut). The gist was NOT touched — the append sits at NIGHT-1030-ENTRY-APPEND-DRAFT.md for the user's glance.

## The loop-state line

**FOUR LEGS LANDED, FULL STANDARD → the seams' closures are named and candidate-shaped**: S1's semantic consent-deny, S2's orphan_doc_names + the read-shape reconciliation + the skip-guard relabel, S3's temporal construction (hand-back), STORM's append draft. The code-level fixes land on the forked candidate ONLY at the user's word (public-surface writes). The append lands at the glance. The hold items (the L0 probe-layer issue + the #139606 entrapment comment) remain at the CTO gate per the user's READY/NOT-READY list.

## The disk line

93% used / ~5.0G free — BELOW the watcher's 7G floor (the alarm's due; it has not fired). Sweep: the day's /tmp debris (the rfc659-runner clone, the temp worktrees) reclaims the headroom; the watcher floor plus the sweep are this fold's action items.

## The day's own ledger (the redo's lessons)

- Rushed briefs = rushed work = redo — the cost of mood-driven dispatch (the user's correction; the doctrine now: the brief is the standard whether the mood is calm or not).
- Artifacts, not self-reports — the wrong-handle landing proved the lane's own summary missed its defect; every landing is read at the artifact.
- The board's spawner needs a git repo at its workspace — the worktree-repo fix.
- Direct-SQL card writes went to a phantom board; the CLI's the canonical board interface — verify through the dispatcher's own view.
- The LP envelope lives in the briefs: the wall clause (a non-reproduction is a question; construct the minimal case that moves it).
