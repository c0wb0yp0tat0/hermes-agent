# LOOP5-THINKTANK-FOLD-20261101 — think-tank triple-down over loop-five's landings

Fold over loop-five's three receipted landings. Spine applied in order: classify → choose → probe → evaluate → adopt-or-park → standardize → verify. Skills loaded per binding order: think-tank §2 (envelope + spine + 40/8 by VOI) → head-supervisor-think-tank → mission-shaping → agent-work-review. Calibration clause: the skills inform, judgment decides — the spine runs, never the checklist.

Nothing public. No pushes. Append/serve gates are the user's word.

---

## 0. The landings (all receipted on disk)

1. **LEG-GATES** — patch-a's sub-suite gains the McNemar acceptance bar; patch-b's read entries route through source addresses; patch-c's lock pin re-verified under the packaged suite. Receipts: `IMPROVEMENT-LOOP-ROUND4-20261101.md` §READY 1-2, `NIGHTSHIFT-1030-PLAN-20261030.md` §§S1-S3, `NIGHTSHIFT-1030-LOOP2-FOLD-20261030.md`, `NIGHTSHIFT-1030-REDO-FOLD-20261030.md` §§REDO-S1/S2/S3, scratch `leg-s3/verdict_wall_moved.md`.
2. **LEG-APPEND** — the ENTRY draft harmonized with the projection's names (address/traversal/marginal-value). Receipt: `NIGHT-1030-ENTRY-APPEND-DRAFT.md` (2843 bytes) + change-why in `IMPROVEMENT-LOOP-ROUND4-20261101.md` §READY 3 and `NIGHTSHIFT-1030-REDO-FOLD-20261030.md` §REDO-STORM.
3. **LEG-SEAM** — `FOLLOWUP-SEAM-OPTION-BRIEFS-20261101.md` (247 lines): option (a) already-pinned-probe mode (guard byte-identity, skip-injection path, acceptance run) and option (b) four encoding-freshness tests (VERIFIED GREEN — 23 passed = 16 original + 7 new). Receipts cited therein: runner head `5184f7a1`, candidate `b84150e9be`, consent fixture sha `f9076148…`, in-tree probe blob `4e5bfc5d…`.

---

## 1. CLASSIFY (domain per landing, per need not per mission)

| Landing | Sub-item | Domain | Rationale |
|---|---|---|---|
| LEG-GATES | patch-a sub-suite + McNemar acceptance bar (paired comparison, 2.7pt-drop blocker) | **complicated** | Statistical gate where expertise intervenes — paired binary outcomes, McNemar at α=0.05, 53–78% retention band. The 2.7pt drop is the failure mode the gate blocks. Apply expertise, not a rote standard. |
| LEG-GATES | patch-b routing (entries' addresses point at source) | **clear** | Deterministic path exists — addresses resolve to raw source turns; 16 passed in 1.18s, probe collects. Apply the standard. |
| LEG-GATES | patch-c re-verified lock (5 passed, `uv lock --check` exit 0, 327 packages, no cross-touch) | **clear** | Deterministic verification already run; absolute exclude-newer date verified. Apply the standard. |
| LEG-APPEND | ENTRY draft harmonized with projection's names (address/traversal/marginal-value) | **complicated** | Framing/terminology reconciliation where expertise intervenes — the gate vs. activation-prediction distinction, FIRME/Helixar corroboration, owner's reconciliation flagged (gate tokens absent from the entry's own carriers). |
| LEG-SEAM | Option (a) already-pinned-probe mode (guard byte-identity, skip-injection) | **complicated** | Runner-side guard logic — byte-identity verification of fixture + probe superset + base defs + consent parametrization; acceptance conditions require expertise to define. |
| LEG-SEAM | Option (b) four encoding-freshness tests | **clear** | Verified green against `MemoryStore`: 23 passed = 16 + 7 new, 0.41s. Apply the standard. |

Loop-five as a whole sits in **complicated** (timing-embedding of statistical + framing + seam decisions). No complex/chaotic reclassification needed — every bounded probe the landings required has already run and is receipted. No predictive certainty is claimed beyond receipts.

---

## 2. CHOOSE (mechanisms by VOI — ADOPT / ADOPT-CANDIDATE / PARK / DMISS)

Each entry carries observable evidence, a rollback note, and a success signal (40/8 method-card shapes).

### 2.1 Statistical gate — McNemar, paired comparison, 2.7pt-drop blocker (patch-a)
- **Decision: ADOPT** (as the pass bar for the consent sub-suite).
- Evidence: field-measured 2.7-point drop without the gate; 12 renamed-identifier scenarios (`SYNTHETIC-CONSENT-CODE-PX7412` → `PRIVATE-EXPERIMENT-IDENTIFIER-NQ9281`) persisted the replacement identifier into USER.md/MEMORY.md (staged=False) under the prefix-only gate; MemCodex formula — d-tok ≤ 0, d-acc ≥ 0, McNemar α=0.05, 53–78% retention threshold. Receipts: `IMPROVEMENT-LOOP-ROUND4-20261101.md` §READY 1; `NIGHTSHIFT-1030-PLAN-20261030.md` §S1; `NIGHTSHIFT-1030-REDO-FOLD-20261030.md` §REDO-S1.
- Rollback: revert the gate criterion to the prefix-only check; the renamed sub-suite (`tests/tools/test_consent_deny_renamed.py`, 8 single-op + 4 batch) remains as a regression test.
- Success signal: all 12 renamed scenarios deny (staged=False) under the McNemar bar; zero false passes.

### 2.2 Routing rule — entries' addresses point at source, src(x) → raw turns (patch-b)
- **Decision: ADOPT.**
- Evidence: 16 passed in 1.18s; probe collects; compaction-staleness gap (88.4% recall @2.0k tokens vs. 63.0% @3.9k content-only) is the same seam the read-return-shape correction touched; choice (a) adopted (no read-contract edit) per `NIGHTSHIFT-1030-LOOP2-FOLD-20261030.md` §LOOP2-S2.
- Rollback: restore content-copy routing; entries re-carry addresses on next sync.
- Success signal: READ returns entries whose addresses resolve to raw source turns; zero content-copy drift.

### 2.3 Absolute lock pin — `uv lock --check` exit 0, 327 packages, no cross-touch (patch-c)
- **Decision: ADOPT-CANDIDATE** (verified in-scratch; public-branch landing awaits the user's word).
- Evidence: 5 passed; `uv lock --check` exit 0; 327 packages; no cross-touch; temporal wall moved — absolute exclude-newer date (the sliding 3-day `exclude-newer` was the mechanism; `ExcludeNewerValue::timestamp()` recomputed per call). Receipts: `NIGHTSHIFT-1030-PLAN-20261030.md` §S3; `NIGHTSHIFT-1030-LOOP2-FOLD-20261030.md` §LOOP2-S3; scratch `leg-s3/verdict_wall_moved.md`.
- Rollback: revert to the sliding 3-day exclude-newer; `pm.lock_project` remains the canonical repair path.
- Success signal: `uv lock --check` exit 0 on the published head `b84150e9be`; reproducible install.

### 2.4 Seam option (a) — already-pinned-probe mode
- **Decision: ADOPT-CANDIDATE** (shaped, not merged; depends on (b)).
- Evidence: guard spec — fixture sha256 `f9076148…` must match runner's own; probe superset must define all four encoding-freshness defs plus five base defs + consent parametrization; skip-injection path records `probe_source: candidate-in-tree`, `injection: skipped`; end-to-end produces receipt with `encoding_freshness` 7/7 and `required_green: true`.
- Rollback: remove `--already-pinned-probe` flag and conditional block; single-file, single-hunk deletion; `probe_source` field becomes optional/absent (old receipts remain valid).
- Success signal: 14 existing selftests still pass + new `test_already_pinned_probe_mode` (i–iv); end-to-end receipt on `b84150e9be`.

### 2.5 Seam option (b) — four encoding-freshness tests
- **Decision: ADOPT** (verified green).
- Evidence: `python3 -m pytest tests/tools/test_rfc_homework.py -q` → 23 passed in 0.41s (16 original + 7 new); four defs appended verbatim; no change to the existing 16. Receipt: `FOLLOWUP-SEAM-OPTION-BRIEFS-20261101.md` §Verification.
- Rollback: delete the appended block; probe returns to 16/16 green. No other file touched.
- Success signal: 23/23 green; `encoding_freshness` selector collects 7/7.

### 2.6 ENTRY append — Pre-Write Activation Risk (address/traversal/marginal-value)
- **Decision: ADOPT-CANDIDATE** (staged as draft; gist append gated on the user's glance/word).
- Evidence: 350 body words; three-valued validity gate (AUROC 0.91–0.95, owner's reconciliation flagged — the entry's own carriers name no gate tokens); activation-level disclosure prediction read ALONGSIDE the gate (two signals, two questions, both at the address layer, content fetched on traversal); S1 template (prefix seam + staged=False receipt); FIRME (source/time/context provenance) + Helixar (8-field convergence) corroboration; `@kvnloo` ×2 swept. Receipts: `NIGHT-1030-ENTRY-APPEND-DRAFT.md`; `IMPROVEMENT-LOOP-ROUND4-20261101.md` §READY 3; `NIGHTSHIFT-1030-REDO-FOLD-20261030.md` §REDO-STORM.
- Rollback: gist not touched; draft sits at `NIGHT-1030-ENTRY-APPEND-DRAFT.md`.
- Success signal: gist append lands with the three signals named; no invented claims.

### 2.7 Held at gates (PARK, not dismissed)
- **VoI-as-rho scorer** — waits the world-model interface contract.
- **CORAL cycle** — waits the checkpoint state format.
- **LoCoMAP prefetch** — waits the history-horizon axis schema.
- Named, not fired. `IMPROVEMENT-LOOP-ROUND4-20261101.md` §"The NOT-READY trio."

### 2.8 DMISS
- None this loop. No mechanism dismissed. The three NOT-READY items are PARKed, not dismissed.

---

## 3. PROBE (gaps a bounded probe would settle)

1. **LEG-IMPROVER formal pass** — the improver's channel refused twice (503 class). Bounded probe: re-run the moment the channel opens; until then the deliverable lands from the verified record (stalled-lane doctrine). Named, not settled. Receipt: `IMPROVEMENT-LOOP-ROUND4-20261101.md` header.
2. **(a)↔(b) end-to-end dependency** — (a) alone refuses on the current substrate until (b) lands (the encoding selector would collect 0 cases). Probe: run (a) against `b84150e9be` with the (b)-extended probe present → receipt with `encoding_freshness` 7/7. Settled only after (b) merges. Receipt: `FOLLOWUP-SEAM-OPTION-BRIEFS-20261101.md` §§Option (a) acceptance test, "The pick."
3. **S3 temporal construction (date-advance)** — hand-back to the lane; not run in the redo. Bounded probe available: force the cutoff to close the window. Receipt: `NIGHTSHIFT-1030-REDO-FOLD-20261030.md` §REDO-S3.
4. **Lock pin on the published head** — `uv lock --check` against `b84150e9be` not yet run. Probe available; pending the user's word on public-branch writes.

---

## 4. EVALUATE (loop-five verdict on the substrate's candidacy — certification window readiness)

The landings changed the substrate's candidacy in four ways: (i) the consent sub-suite now carries a statistical acceptance bar (McNemar) that blocks the overfitting-shaped false pass; (ii) routing points entries at source (16/16 green); (iii) the lock pin is re-verified (5/5, exit 0); (iv) the seam is shaped both sides ((a)+(b)). The ENTRY append harmonizes with the projection's names.

Certification window readiness: the runner can emit `encoding_freshness` 7/7 + `required_green: true` once (b) lands and (a) runs against the published head. The improver's formal pass is the remaining certification gate (channel dark). The three NOT-READY items (VoI-as-rho, CORAL, LoCoMAP) stay held at the CTO gate per the user's READY/NOT-READY list.

**Verdict: CANDIDATE-READY** — pending (b)-merge + (a)-run + improver pass. Not yet certified. No public writes, no pushes.

---

## 5. ADOPT-OR-PARK (standardized statuses, with evidence)

| Mechanism | Status | Evidence |
|---|---|---|
| Statistical gate (McNemar) | **FIRED** | 2.7pt-drop blocker named; McNemar bar defined; 12 renamed scenarios' deny outcome measured. |
| Routing rule (source addresses) | **FIRED** | 16 passed in 1.18s; entries address source; probe collects. |
| Absolute lock pin | **FIRED in-scratch** (ADOPT-CANDIDATE on public branch) | 5 passed; `uv lock --check` exit 0; 327 packages; no cross-touch. |
| Seam option (b) | **FIRED** | 23 passed = 16 + 7; 0.41s. |
| Seam option (a) | **DORMANT** | Shaped, not merged; depends on (b). |
| ENTRY append | **DORMANT** | Staged draft; gist append gated on user's word. |
| VoI-as-rho / CORAL / LoCoMAP | **CORRECTLY-ABSENT** | NOT-READY, held at gates; not applicable to this loop's scope. |
| Improver formal pass | **MIS-FIRED (as channel)** | Channel refused twice (503); deliverable landed from verified record per stalled-lane doctrine; pass itself pending, not dismissed. |

Status vocabulary (binding): FIRED / DORMANT / MIS-FIRED / CORRECTLY-ABSENT — each with observable evidence, never a bare claim.

---

## 6. STANDARDIZE (loop six's armament — mechanism-selected, not invented)

Brief shape for the next loop:

**Next probes**
1. (b)'s tests integration into the in-tree probe's shape — done (23 green); verify no regression on the existing 16.
2. Certification window readiness check — run (a) against `b84150e9be` with the (b)-extended probe → receipt `encoding_freshness` 7/7 + `required_green: true`.
3. Improver's formal pass — re-run when the channel opens; re-certify the whole set.

**Seams**
- S1 consent-prefix (semantic recognition) — closure candidate shaped; renamed sub-suite in battery.
- S2 orphan (`orphan_doc_names` + read-shape reconciliation + skip-guard relabel) — shaped.
- S3 uv.lock (absolute exclude-newer date; date-advance construction hand-back) — shaped.
- Runner seam (a)+(b) — shaped both sides.

**Gates**
- Public-surface writes gated on the user's word (nothing pushed, nothing public).
- Append/serve gates are the user's word (contract).
- Improver pass pending channel (503 class).

**Success criterion for loop six:** receipt with `encoding_freshness` 7/7 + `required_green: true` on the published head; improver pass green; zero remaining seams or named hand-backs.

---

## 7. VERIFY (compose-check — the fold's claims' receipted paths)

| Claim | Receipted path |
|---|---|
| patch-a McNemar bar | `IMPROVEMENT-LOOP-ROUND4-20261101.md` §READY 1; `NIGHTSHIFT-1030-PLAN-20261030.md` §S1; `NIGHTSHIFT-1030-REDO-FOLD-20261030.md` §REDO-S1 |
| patch-b routing, 16 passed in 1.18s | `NIGHTSHIFT-1030-PLAN-20261030.md` §S2; `NIGHTSHIFT-1030-LOOP2-FOLD-20261030.md` §LOOP2-S2 |
| patch-c lock, 5 passed, exit 0, 327 pkgs | `NIGHTSHIFT-1030-PLAN-20261030.md` §S3; `NIGHTSHIFT-1030-LOOP2-FOLD-20261030.md` §LOOP2-S3; scratch `leg-s3/verdict_wall_moved.md` |
| ENTRY append draft (2843 bytes) | `NIGHT-1030-ENTRY-APPEND-DRAFT.md`; `IMPROVEMENT-LOOP-ROUND4-20261101.md` §READY 3; `NIGHTSHIFT-1030-REDO-FOLD-20261030.md` §REDO-STORM |
| Seam option (a)/(b) spec | `FOLLOWUP-SEAM-OPTION-BRIEFS-20261101.md` (247 lines); receipts cited therein (runner `5184f7a1`, candidate `b84150e9be`, fixture sha `f9076148…`, probe blob `4e5bfc5d…`) |
| (b) 23 passed | `FOLLOWUP-SEAM-OPTION-BRIEFS-20261101.md` §Verification; pytest 23 passed in 0.41s |
| Improver channel 503 | `IMPROVEMENT-LOOP-ROUND4-20261101.md` header |

All claims traceable to receipted paths. Nothing fabricated. Nothing public.

---

## Contract

- Nothing public; no pushes.
- Append/serve gates are the user's word.
- Disk: see `df -h /` output below.

---

## Disk (df -h /)

```
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/pve-root   70G   60G  6.1G  91% /
```