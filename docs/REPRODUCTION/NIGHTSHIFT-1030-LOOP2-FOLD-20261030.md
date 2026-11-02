# NIGHTSHIFT-1030 — LOOP 2 FOLD (the closures' verification)

*The second loop took the first loop's closure candidates and verified them. Three legs, three verdicts, all receipted.*

## The three verdicts

**LOOP2-S1 — the consent-deny closure: FIX-VERIFIED.** The semantic recognition candidate (declaration-based: `source_no_save`/`source_instruction`, not the marker literal) closes the seam: all 12 renamed-identifier scenarios now DENY (staged=False), original-marker controls hold, normal operational writes unaffected. The battery's renamed sub-suite is shaped: `tests/tools/test_consent_deny_renamed.py` (8 single-op + 4 batch renamed tests), the fix04 additions (`renamed_scenarios.json`, `test_no_save_never_lands_renamed_identifier`, `test_op_consent_denied_detects_renamed_markers`), the integration patterns (mixed batches filtered, all-denied batches rejected, writes unaffected).

**LOOP2-S2 — the orphan capability closure: FIX-VERIFIED, with a self-correction.** The missing piece is ONLY `orphan_doc_names()` — the probe collects with it: `ORPHANS=['rfc-orphan-contract']`, `READ={'success': True, 'entries': [...]}`, all asserted outcomes ×3 runs. The read-return-shape sub-claim from loop 1 was first-hand inaccurate (the head's `read()` already returns entries) — corrected by construction; choice (a) adopted (no read-contract edit). The skip guard's relabel drafted.

**LOOP2-S3 — the lock seam's temporal wall: WALL-MOVED.** The construction reproduced the failure: `exclude-newer = "3 days"` is a MOVING cutoff (uv's `ExcludeNewerValue::timestamp()` = now - span, recomputed per call); the closed-window construction (a file:// index with no data-upload-time attributes) → uv excludes all files, warns, resolution fails. Mechanism PROVEN date-bound. The durable fix — pin an ABSOLUTE exclude-newer date — verified as the right shape. Receipts: /root/.hermes/cache/scratch/leg-s3/verdict_wall_moved.md.

## The loop-state line

**LOOP 2 COMPLETE — ALL THREE CLOSURES VERIFIED IN-SCRATCH.** The landing candidates, ready to become real code on the forked candidate: (1) the semantic consent-deny + the renamed sub-suite; (2) `orphan_doc_names()` + the guard relabel; (3) the absolute-date lock pin. THE LANDINGS ON THE PUBLIC BRANCH + THE ENTRY-APPEND sit at the user's word (public-surface gates are theirs by right). The holds (the L0 probe-layer issue, the #139606 entrapment comment) remain at the CTO gate.

## The fold's own line

Disk: 93% / ~5.0G free — below the watcher's 7G floor (the alarm remains due; the sweeps have not reclaimed the balance — the next sweep's scope: the older scratch passes + the worktrees). The false-alarm class is NOT at play — the level is real and named.

## The second loop's lessons (banked)

- The falsifier cycle corrects its own prior claims (loop 2 receipted that loop 1's "read returns text" was inaccurate — the construction IS the disconfirmation).
- The wall clause works when the brief arms it: the date-advance construction moved the wall in one leg.
- The loop clauses compound: each pass's closures become the next pass's missions — the loop runs to zero remaining seams.
