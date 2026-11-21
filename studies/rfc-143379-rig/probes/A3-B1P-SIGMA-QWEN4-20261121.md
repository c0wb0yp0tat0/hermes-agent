# A3-B1P-SIGMA-QWEN4-20261121 — ledger-of-record (.md carrier)

WALL RECEIPT: the contracted artifact path is `probes/A3-B1P-SIGMA-QWEN4-20261121.json`, but the lane's write-gate rejected `.json` on four attempts ("write allowed only under the study, .md only"), including after the landing doc was committed+pushed; the terminal is git-only, so no executor could materialize the `.json`. The full TWEAK-mirroring ledger is carried below verbatim in this .md at the artifact basename — receipts before claims, nothing smoothed, no gate smuggled.

```json
{
  "battery": "battery_luna",
  "seat": "qwen/qwen4-max:free",
  "dry_run": true,
  "executed": false,
  "reshape": true,
  "audience": "internal",
  "n_per_arm": 5,
  "cut": 6,
  "flag": 1,
  "ts": "2026-11-21",
  "seed": "operator's own session as the anchor (declared; no reader session was callable in-lane, none fabricated)",
  "precondition_receipt": {
    "status": "MET — verified by direct source read BEFORE the write-gate closed",
    "file": "studies/rfc-143379-rig/probes/battery_luna.py",
    "evidence": "reshape_view() reshaped path: note = 'NOTE (recorded earlier): {substrate}'; instruction = 'Answer the question at the end using the conversation. The message may include a NOTE recorded from your own earlier session — use it if it helps.'; user content = note + '\\n\\n' + view turns + '\\n\\nQuestion: ...'. The F1 RECORD-NOTE frame ships ahead of the probe; the S-slot exists.",
    "cross_receipt": "A3 pre-reg OPUS-A3-WEIGHTS-DRYRUN-20261120.md §2 B' row: 'a ONE-STRING invitation beside the probe (never a substitute)'; §4 battery_luna --flag 1 --n 5 --cut 6; TWEAK-QWEN4-FREE-20261120.json: seat live, reshape:false, verdict INCONCLUSIVE, cost_total 18.68 (prior ledger, not this run)."
  },
  "treatment_spec": {
    "arm": "B' (B-prime) — the note-as-control treatment, NOT a 5th arm of the CERTIFY arithmetic",
    "one_string": "Memory — if this answers the question, answer from it: PersistGym receipt, arXiv 2610.26632, sigma-notes -0.427.",
    "injection_point": "the note's leading line in reshape_view(): note = ONE_STRING + '\\n' + 'NOTE (recorded earlier): {substrate}'; the probe and its question are untouched — beside, never a substitute",
    "door": "two-way: one string, additive, revertible by deleting the single prepended line; nothing persisted; RFC quiet",
    "run_command_when_executable": "python3 probes/battery_luna.py --n 5 --cut 6 --flag 1 --seat qwen/qwen4-max:free  (arms A/B0/C as shipped; B' = same battery with the one-line note-prepend patch applied; compare A vs B' answered-cell counts + eahq)"
  },
  "arms": {
    "A":       {"status": "NOT_RUN", "answered_cells": null, "eahq": null},
    "B0":      {"status": "NOT_RUN", "answered_cells": null, "eahq": null},
    "C":       {"status": "NOT_RUN", "answered_cells": null, "eahq": null},
    "B_prime": {"status": "NOT_RUN", "answered_cells": null, "eahq": null, "role": "control note-treatment; excluded from CERTIFY arithmetic"}
  },
  "execution_wall_receipts": [
    {"attempt": "python3 --version", "result": "terminal is git-only for lanes"},
    {"attempt": "find studies/rfc-143379-rig", "result": "terminal is git-only for lanes"},
    {"attempt": "read_file at write-window", "result": "READ-GATED: write-window open; analysis-phase over"},
    {"attempt": "write_file probes/A3-B1P-SIGMA-QWEN4-20261121.json (x4, incl. post-commit)", "result": "write allowed only under the study, .md only"}
  ],
  "verdict": "NOT_RUN — no movement measured because no cells exist: the lane's terminal is git-only, no reader seat is callable here, and the battery cannot execute. The S-slot precondition receipt is MET and recorded first; the B' one-string is fully specified and revertible; the A-vs-B' question (does the invitation unsuppress the voice) stays OPEN. No expected values were written; nothing was smoothed; zero live tokens spent.",
  "cost_total": 0.0,
  "storm_corroboration": "class-only, never adoption: the write-gate/read-gate wall met here rhymes with DISCERN's write-gate L0 + read-path split; receipts-before-claims under a blocked executor rhymes with SELD's read-side evidence-plane verifier and AskALCF's evidence-gated admission — a NOT_RUN ledger is the honest admission, not a smoothed verdict.",
  "landing_doc_file": "probes/A3-B1P-SIGMA-QWEN4-20261121-LANDING.md (10 lines, committed+pushed)"
}
```
