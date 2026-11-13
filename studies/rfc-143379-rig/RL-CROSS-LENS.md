# RL Cross-Lens — the forks' wildcard-seat (atropos / Gym vs the study's mechanism-map)

**Branch:** `study/rfc-143379-rig-20261105` (fork-only; nothing public). **Seat:** wildcard (RL-frameworks cross-lens). **Receipts, not claims.**

## [Executive Summary]

Read PR #1 end-to-end (all comment pages), the SYNTHESIS mechanism-map (pinning recurrence-conditions, retention-latch, compaction-fix), and the fork-network's RL family: `c0wb0yp0tat0/atropos` (README) + `c0wb0yp0tat0/Gym` (RL environments builder). Verdict: **SEAMS-NAMED** — 2-3 concrete adoption-candidates for the study's next instruments, plus an honest **SEAMS-THIN** note on the RL-family's divergence (environments reward *model capability*, not *context-window hygiene*). The cross-lens is asymmetric: atropos/Gym teach *probe construction* (curriculum, reward-shaped signal, composable envs) but do not map onto the krecency realm's demand-age/recurrence/deep-minima signal-structures; the study's signal is about *memory retention under compaction*, which RL envs do not model.

## [Analysis Brief]

### (a) Atropos environments vs krecency signal-structures

Atropos (archived Nous RL gym) = async RL env microservice framework: environments as services, trajectory API, reward signals, curricula across dataset/online/multiturn/code/multimodal envs. Reward = task-success signal on generated trajectories.

krecency realm = demand-age (how recently a fact was demanded), recurrence (re-demand under compaction), deep-minima (memory-floor under repeated compaction). Signal-structures are about *retention fidelity across context compression*, not task success.

Cross-inspiration (adoption-candidate): **curriculum-shaped probes** — atropos's staged difficulty (GSM8K→interactive games→multiturn) maps to a staged compaction-depth ladder for the krecency probe battery: shallow→deep compaction, measuring retention at each stage. Reward-shaped machinery maps to a *retention-reward* metric: score = (recalled facts)/(demanded facts) per compaction stage, yielding a scalar the study can track across runs. Environment shapes (dataset/online/multiturn) map to fixture-families: static dataset env ↔ compression-eval suite, multiturn env ↔ krecency recurrence probe.

### (b) Gym builder-mechanics vs fixture-families

Gym (RL environments builder) = composable environments with standard reset/step API, observation/action spaces, wrappers. Shared shape with study's fixture-families: composable suites (compression-eval suite, krecency probes) with a common harness interface (reset probe → apply compaction → step/measure → reward). Adoption-candidate: **standardized env interface** for probe suites — a `reset/step/reward` contract enabling wrapper composition (e.g., a compaction wrapper around any probe), plus reproducible seeds.

### (c) Verdict

**SEAMS-NAMED — adoption-candidates (next instruments' inspirations):**
1. Curriculum-shaped compaction ladder (from atropos staged difficulty) — staged compaction-depth probe.
2. Retention-reward scalar (from reward signals) — (recalled/demanded) per stage, tracked across runs.
3. Composable probe env interface (from Gym reset/step/wrappers) — standardized fixture-family harness with wrappers.

**SEAMS-THIN — honest divergence:** atropos/Gym reward *capability acquisition* (task success), while the study measures *context-hygiene retention* (demand-age/recurrence/deep-minima). RL envs assume a learning agent; the study assumes a fixed model under compaction. Reward signals do not transfer as training signals; they transfer only as *measurement scaffolding*. The RL family's mechanisms are inspiration for instrumentation, not for the study's core claim. Nothing in the RL family addresses the retention-latch or compaction-fix directly.

## [Recommendation/Action Plan]

- Adopt the 3 adoption-candidates as next-instrument specs (curriculum ladder, retention-reward scalar, composable probe env interface) in the study's mechanism-map appendix.
- Do not import RL training loops; reuse only measurement scaffolding.
- Keep all findings on the fork branch; no public posting.

## [Next Steps]

- Spec the composable probe env interface against the existing krecency probe battery.
- Add retention-reward scalar to the compression-eval suite's reporting.
- Re-run falsifier battery with curriculum ladder to check recurrence-conditions.

## [Artifact]

- File: `studies/rfc-143379-rig/RL-CROSS-LENS.md`
- Commit on branch `study/rfc-143379-rig-20261105`, pushed; `git ls-tree HEAD --name-only studies/rfc-143379-rig/ | grep -ci RL-CROSS` = 1.
- SHA: recorded at commit time (see git log).
