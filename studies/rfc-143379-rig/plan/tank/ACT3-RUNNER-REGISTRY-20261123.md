# ACT3-RUNNER-REGISTRY-20261123 — the runners'/registry verification (AM-F1 + the G3 seat-liveness gate)

*Seat: `meituan/longcat-2.5:free` — PIN-READ-BACK VERIFIED at probe #1 (this fire). Branch: `study/rfc-143379-rig-20261105`. Date: 2026-11-23. Deliverable path (this file): `studies/rfc-143379-rig/plan/tank/ACT3-RUNNER-REGISTRY-20261123.md`.*
*This leg verifies, it does not fire a lane, run a battery, or render an audit/verdict. The plan, the sealed artifacts, the crons, the anchors, and the sibling plates are left AS FOUND; the master's append-only; nothing public; RFC #143379 + #5320 + #157065 QUIET; no installs; never push; never `git checkout --` / `git stash` / `git rm -rf`; write only under the study; local config left AS FOUND (overridden per-commit).*
*Emission contract: this file lands on disk FIRST with the receipts inside, then the commit, then the report's sha. A parse-fragment-only response has NOT landed. Exit 0 = deliverable on disk then sha.*

---

## 0. The armament — the skill-stack DUMPED (the skill-dump doctrine)

**USED (loaded via `skill_view` this pass; each named with WHY):**

| skill | WHY (this leg) |
|---|---|
| **think-tank** | the spine — `classify → choose → probe → evaluate → adopt-or-park → standardize → verify`. This leg IS a classify (the rows' classes) → probe (the live channels/pins) → evaluate (the row-by-row re-verification) → verify (the verdicts). Its binding lines rode the brief: the wall clause (a non-reproduction is a QUESTION with receipts), the failure-is-the-finding, the fleet-scale verification (testimony is not evidence — every material claim re-derived), the number-seam (disagreeing records → hunt the RAW receipt). |
| **investigation-documentation** | the receipts' form — the discovery log (origin → turns → limitations → reproducibility) and the citation/identifier discipline. The deliverable is a peer-reviewable verification log; every row carries its primary source (the walk state / the ls-remote / the probe JSON). |
| **defect-forensics** | the stale-row/void classes — the parent-class hunt, date-stamp everything, root-vs-amplifier, the CLASS not the flagged instance, the failure-is-the-finding. The moved-head and void-class seams are its classes; the a9c65dc4 dangling pin is a parent-class hunt (one pin, three refs, no live branch). |
| **agent-work-review** | the verdict's form — full reads → extraction → consistency matrix → arithmetic re-derivation → identifier cross-check → epistemic scoping → asserted → status → basis. The registry ↔ act-2 ↔ live-refs cross-check is exactly a consistency matrix + identifier cross-check. |

**REFUSED (considered, NOT loaded — no load in a mechanical verification leg; each named with WHY):**

| refused | WHY |
|---|---|
| blind-agent-panels · supervisor-delegation · think-tank-feedback | no consensus fan-out for a mechanical verification; the rows are measured, not adjudicated by a panel |
| codex · claude-code · opencode | no delegate coder — the deliverable is a study-path append, written here |
| aces-harness-probes · evaluating-llms-harness · local-llm-serving · llama-cpp · serving-llms-vllm | no install, no harness/serving change; the local floor is read-only-probed |
| two-model-reasoning | no offline-reasoner leg in a mechanical verification |
| web-storm · grounded-citations · arxiv · browser-harness-sop · ddg-cli-search | no field search — LOCAL receipts only (the hard line) |
| memory-chain | no chain append this pass |
| hermes-agent · hermes-gateway-ops | no config/gateway change |
| safe-file-editing | no secret-bearing file edited |
| systematic-debugging | armed only on a non-reproduction; the wall clause governs |
| github · github-auth · github-code-review · github-issues · github-pr-workflow · github-repo-management | no PR/issue/write; the fork refs verified via local `git ls-remote` (read-only) |
| the creative/design/media families | out of scope for a verification leg |

*A lane that does not demonstrate the dump-and-refuse has not adhered. This leg arms only the four above.*

**The anchor (one pass, binding):** `/root/.hermes/memories/MEMORY.md` + `USER.md` read in full this pass. The load-bearing anchor facts: the study-repo's branch is shared with a sibling's archiver — **stale pushes revert/stack the head; the tracking ref can lie (refspec main-only); per fold: `ls-remote` first** (this leg did `ls-remote` first — see §4); the GATE LAW's exact form (the ONLY gate = public writes outside PR #1; any other hold = a fabricated gate); FLEET = 4 runners (pve1-avrea-parallel = THIS host · p0tat0 = Linux 241 · c0wb0y = Windows 241 · cloud); Facimus semper; the fleet is it/its.

---

## 1. The inputs read (full reads, this pass)

| input | pin / path | role |
|---|---|---|
| `plan/tank/REVISED-STAGE-PLAN-20261123.md` | the revision (12 amendments) | the act-3 clause (§3 row 3, AM-F1) + the G3 seat-liveness gate + the G4 base-diversity gate |
| `plan/SEAT-REGISTRY-20261123.md` | the CURRENT register (governs) | the runners / forks / seats / legs rows |
| `plan/SEAT-REGISTRY-20261122.md` | the prior register | the continuity check (byte-identity) |
| `plan/tank/ACT2-SEAT-PROBE-20261123.md` | `caa9468556` | the just-landed per-fire liveness matrix (the cross-check base) |

**The act-3 clause (verbatim, §3 row 3):** `RUNNER/REGISTRY VERIFICATION (AM-F1): Walked actual (installed 2 / failed 0) + SEAT-REGISTRY-20261122.md presence verified; heartbeat re-verifies registry rows; absent row/failed walk = named failure class.` Receipt: Heartbeat log + registry-row check.
**The G3 gate (verbatim, §3):** `the seat-liveness gate — the read-back pin: the responding model == the requested pin at every fire, receipted.`
**The G4 gate (verbatim, §3):** `the base-diversity gate (>= 2 distinct bases; AoA distinct from all three audits) — re-verify after any pivot.`

---

## 2. Probe #1 — the seat read-back (the dispatch contract, this fire)

**The spawn pins AND read-backs the config's model == the brief's seat.** Config read-back (`/root/.hermes/config.yaml`): `delegation.model: meituan/longcat-2.5:free` — **matches the brief's seat**. The responding model is then read back from the wire (not assumed):

```json
{"requested_model": "meituan/longcat-2.5:free", "pin": "PIN-90AF232492", "question_sha": "d809471c4746bc2b", "http": 200, "dt": 4.1, "responding_model": "meituan/longcat-2.5:free", "content_head": "PIN-90AF232492\n143379 is best known as an RFC number, specifically RFC 143379, w", "content_len": 232, "finish_reason": "stop", "prompt_tokens": 79, "completion_tokens": 84, "reasoning_tokens": null, "pin_echo_in_content": true}
```

**VERIFIED:** the responding model IS `meituan/longcat-2.5:free`; the PIN echoed in content; content-bearing (232 bytes, `finish = stop`). The dispatch contract's probe #1 holds at this fire.

---

## 3. The runners — the walked actual + the live channels (re-measured, counts not adjectives)

**The live channel probe (`/root/scripts/walk-fleet.sh hosts`, 2026-11-23T14:36Z):**

| alias | channel | os | machine | channel probe | API |
|---|---|---|---|---|---|
| p0tat0 | `c0wb0y@100.98.69.7` | Linux | c0wb0yp0tat0 (241) | **OK** Linux c0wb0yp0tat0 | online · busy=false |
| c0wb0y | `c0wb0y@100.70.143.25` | Windows | DESKTOP-8R44VEP (241) | **OK** MINGW64_NT-10.0-26200 DESKTOP-8R44VEP | online · busy=false |
| pve1 | (local) | Linux | pve-1 (THIS host) | — (local) | online · busy=false |

**The walk receipts (re-measured this fire):**

| alias | run_id | ts | managed | backed_up | checksum_fail | REGISTRY_APPLIED | ENVELOPE_BOUND | WALK_SUMMARY |
|---|---|---|---|---|---|---|---|---|
| p0tat0 | `walk-20261123T143628Z-a76c` | 2026-11-23T14:36:28Z | 90 | 2 | 0 | `0cff6a5b…f4973` | `c5507111…df8b` | **installed=2 skipped=87 backed_up=2 failed=0** |
| c0wb0y | `walk-20261123T143737Z-e7be` | 2026-11-23T14:37:37Z | 90 | 2 | 0 | `0cff6a5b…f4973` | `f4b08823…67e92` | **installed=2 skipped=87 backed_up=2 failed=0** |

**WALKED ACTUAL: installed = 2 / failed = 0** (p0tat0 + c0wb0y; pve1 is THIS host, not a walked remote). The counts are re-measured, not adjectives. The registry's applied sha on both runners (`0cff6a5b450bf819bb59b8e1404f05f7204777b95ded50083e3b4bbda94f4973`) **equals** the local registry's sha256 (§4) — the runners carry the CURRENT register.

---

## 4. The registry — presence + every row re-verified against the measured channel

**Presence + continuity:** both registers present and **byte-identical**:
`SEAT-REGISTRY-20261122.md` == `SEAT-REGISTRY-20261123.md` == `sha256 0cff6a5b450bf819bb59b8e1404f05f7204777b95ded50083e3b4bbda94f4973`. The current (20261123) governs; continuity clean. The runners' applied sha matches — the register is materialized AND deployed.

**Row-by-row re-verification (the measured channel vs the register's row):**

| registry row | register says | measured this fire | status |
|---|---|---|---|
| runners · p0tat0 | c0wb0y@100.98.69.7 · Linux · c0wb0yp0tat0 (241) · busy false | OK Linux c0wb0yp0tat0 · online busy=false · walk 2/0 | **CONSISTENT** |
| runners · c0wb0y | c0wb0y@100.70.143.25 · Windows · DESKTOP-8R44VEP (241) · busy false | OK MINGW64_NT-10.0-26200 DESKTOP-8R44VEP · online busy=false · walk 2/0 | **CONSISTENT** |
| runners · pve1 | (local) · Linux · pve-1 · busy false | local · online busy=false | **CONSISTENT** |
| forks · study HEAD | `f652b71b4e` · pre-restore | resolves locally; ancestor of the branch HEAD; **the branch HEAD moved** (see §5 seam S1/S2) | **PIN OK · STALE LABEL** |
| forks · pr-139606 | `d1bdb4582c` · write-gate | live `refs/heads/feat/135039-write-gate` = `d1bdb4582c` | **CONSISTENT** |
| forks · pr-141876 | `6609dac951` · restore | live `refs/heads/fix/restore-read-action` = `6609dacba9`; `6609dac951` NOT resolvable locally | **IDENTIFIER SEAM (S3)** |
| forks · a9c65dc4 | `a9c65dc43d` · combined | resolves locally; **no live branch carries it** | **DANGLING-PIN SEAM (S4)** |
| seats · flagship | hy4-flash (window) · solar-mini4 (secondary) · longcat + stepfun (support) | hy4 VOID-CLASS · solar WORKABLE · longcat WORKABLE · stepfun VOID-CLASS | **CONSISTENT (this fire)** |
| seats · paid | openai/gpt-6-luna | 200 / content 126 / stop / PIN | **CONSISTENT (PAID-OK)** |
| seats · local | the darkhorse (GGUF @44831, host-matched) | 200 / content 1736 / finish=length / PIN (280s budget) | **CONSISTENT (caveat held)** |
| seats · envelope | the dispatch pacing cap per runner | the walk's ENVELOPE_BOUND receipted per runner | **CONSISTENT** |
| legs · negative-control | study HEAD × every runner — NOT-RUN-with-reason | the read arm is absent at `f652b71b4e` (the pre-restore pin) | **CONSISTENT** |
| legs · combination | pr-141876 × p0tat0/c0wb0y/pve1 · pr-139606 × pve1 · a9c65dc4 × p0tat0 | the plan's AM-F3 leg-set; the runners are online/ready | **CONSISTENT (ready-to-dispatch)** |

**An absent row or failed walk = a named failure class:** none absent; no failed walk (failed=0 on both). The registry's rows hold against the measured channel. The seams are the fork-row identifier/branch seams (§5), not absent rows.

---

## 5. The forks — re-verified against the LIVE refs (`ls-remote` first, per the anchor)

**The wire's `ls-remote` (2026-11-23, origin = `c0wb0yp0tat0/hermes-agent`):**

| fork (registry row) | registry pin | live ref | status |
|---|---|---|---|
| study HEAD | `f652b71b4e` | `refs/heads/study/rfc-143379-rig-20261105` = **`a848d06254199bf628e1c1124e69a68f95983f01`** | **MOVED HEAD — S1** |
| pr-139606 | `d1bdb4582c` | `refs/heads/feat/135039-write-gate` = `d1bdb4582cd5d16be6a6b486f696f8240c222b96` | **MATCH** |
| pr-141876 | `6609dac951` | `refs/heads/fix/restore-read-action` = `6609dacba951d51cdd880ac1031e546dd7fac289` | **IDENTIFIER SEAM — S3** |
| a9c65dc4 | `a9c65dc43d` | **no live branch carries it** (ls-remote: no `combined-substrate` branch) | **DANGLING-PIN — S4** |

**The other live substrate arms (the amended plan's AM-F3 fork-set), for completeness:** `re-cut-write-gate-surgical` = `9811e52752` ✓ · `round2-gate` = `268bb09147` ✓ · `round2-combined-substrate` = `c39d8ce722` ✓.

**The named stale-row / identifier seams (never reconciled away):**

- **S1 — the wire's study-branch head MOVED.** The context's last-read `bac2672b3594` → the live `ls-remote` **`a848d06254`**. The local tracking ref `origin/study/rfc-143379-rig-20261105` = `687e69d020` is ALSO stale vs the live remote. The anchor's own warning ("the tracking ref can lie; per fold: `ls-remote` first") is borne out. Named, not reconciled.
- **S2 — the study-branch ref moved since the plan's revision.** The plan's AM-F3 records the branch ref `9d56caa557` at revision time; the local branch HEAD is now **`caa9468556`** (the ACT-2 landing) and the live remote is `a848d06254`. The registry's "study HEAD" row labels `f652b71b4e` — the pre-restore pin, which still resolves and is an ancestor of `caa9468556`, but is **no longer the branch HEAD**. The label is stale; the pin is sound.
- **S3 — the pr-141876 identifier seam (both values retained).** The registry records `6609dac951`; the live branch + the local ref are `6609dacba9`; `6609dac951` is not a resolvable local object. Both values retained as the seam, never reconciled.
- **S4 — the a9c65dc4 dangling-pin seam.** `a9c65dc43d` resolves locally (`rev-parse` OK) but is carried by **no** live branch: `git rev-list --all | grep -c ^a9c65dc43d` = 0; `git for-each-ref --contains a9c65dc43d` = empty; `ls-remote` shows no `combined-substrate` branch. The reflog records it as "a9c65dc4 remote LIVE" at an earlier point. The pin is a local-only commit whose branch is gone from the live remote. Named.
- **S5 — the registry's fork table is the stale 4-hero form.** The register is materialized from the pre-revision `94fbb17b2d` (four hero-forks); the amended plan AM-F3's fork-set is **eight** rows. The four named in this leg are verified above; the other four (`re-cut-write-gate-surgical` · `r2gate` · `r2cs`/`r2cs-sync` · `origin/fix/restore-read-action`) are named in the plan and their live refs verified in the same table. The register is stale relative to the amendment — named, not silently substituted.

---

## 6. The seats — cross-checked against act-2's verdicts (AM-C1: liveness measured at each fire, never inherited)

**This fire's re-probe (all seats, one shot each, the act-2 form; raw rows in the appendix):**

| seat | act-2 verdict | THIS fire (re-measured) | cross-check |
|---|---|---|---|
| `meituan/longcat-2.5:free` | WORKABLE (PIN-70FABE99E3) | **200 · content 232 · stop · PIN-90AF232492 echoed** | **REPRODUCED** |
| `upstage/solar-mini4:free` | WORKABLE | **200 · content 118 · stop · PIN echoed** | **REPRODUCED** |
| `openai/gpt-6-luna` | PAID-OK | **200 · content 126 · stop · reasoning 342 · PIN echoed** | **REPRODUCED** |
| local darkhorse (GGUF @44831) | WORKABLE (finish=length caveat) | **200 · content 1736 · finish=length · PIN echoed** (280s budget) | **REPRODUCED** (caveat held) |
| `tencent/hy4-flash:free` | VOID-CLASS (200/null) | **200 · content null · finish=length · reasoning 512** | **REPRODUCED** |
| `stepfun/step-3.7-flash:free` | VOID-CLASS (429) | **429 · retry_after 435** (was 1177) | **REPRODUCED** |
| `qwen/qwen4-max:free` | DEAD (404) | **404 · free period ended** | **REPRODUCED** |

**No liveness was inherited from act-2's receipt** — every seat was re-probed at this fire. The matrix is stable across the two fires (the two VOID-classes and the DEAD seat reproduce; the three content-bearing seats reproduce).

**The probe-harness seam (named, not a seat verdict):** the local darkhorse's first fire at this leg returned a 90s `TimeoutError` — the same seam act-2 recorded (its success took 103.5s). Re-probed at a 280s budget: 200 / content 1736 / PIN echoed. The seat is WORKABLE; the 90s budget was the harness's seam, not the seat's verdict.

**The lane roles (AM-C1):** lane-BA `meituan/longcat-2.5:free` @ p0tat0 · lane-AA `stepfun/step-3.7-flash:free` @ c0wb0y · lane-CA `tencent/hy4-flash:free` @ cloud · the AoA's fourth base = `upstage/solar-mini4:free` (base-distinct from all three audits).

---

## 7. The verdicts

### 7.1 The registry's live-state — **READY**
3/3 runners online · busy=false; the walked actual **installed = 2 / failed = 0** (re-measured); the register present and byte-identical across both dates, and the runners' applied sha matches the local register's sha256; every registry row re-verified against the measured channel; the fork rows re-verified against the live refs. The seams (S1–S5) are named, none silently substituted.

### 7.2 Act-4's battery-board readiness — **mechanically READY; B2's verdict-readiness UNKNOWN**
- **B1's receipts are landed** (`plan/tank/B1-A3-ARC-FIRE-20261123.md`): the A3-ARC fire ran the class protocol WITH the content-gate; the gate FAILED (4 dispatch probes + 20 cells, all HTTP 200 / `content = null` / `reasoning = completion = max_tokens` / `finish = length`, reproduced at 256 and 128). **Battery-verdict = UNKNOWN (VOID-class + no valid seat set); 4 immutable bars, 0 evaluable, 4 NOT EVALUABLE.**
- **B2's firing-position = UNCHANGED / NOT ADVANCED** (AM-B3): already fired #0–#5, all UNKNOWN; the measurement apparatus is mechanically READY (judge-control 20/20, 4-arm ledger, `BIAS_V3` delta, two-way door byte-identical, zero new weight files) while **verdict-readiness remains UNKNOWN** — the one missing ingredient is a content-bearing window.
- **The content-bearing seats named from act-2 — `longcat` · `solar` · `luna` — are all re-verified content-bearing at THIS fire** (§6). The board's candidate set holds; B2's verdict still needs a valid content-bearing 4-arm set (a void fire leaves the position at NOT ADVANCED).

### 7.3 Act-5's fan-readiness — **the pinned fan is NOT fire-ready; the diversity gate is satisfiable NOW**
- **The three audit lanes' pinned bases:** BA = longcat (**content-bearing**), AA = stepfun (**429 transport-void**), CA = hy4-flash (**200/null content-void**). The pinned fan has **only 1 content-bearing base** → it is **NOT fire-ready as pinned**; a drained/frozen pin is never re-fired in the same window (AM-C1), so AA and CA require a **ledgered pivot** (the lane's role kept).
- **The base-diversity gate (≥ 2 distinct bases) is re-verified NOW and SATISFIED with margin:** the content-bearing set at this fire = **{longcat, solar, luna} = 3 distinct bases**; any single-seat pivot leaves ≥ 2. The AoA's fourth base = `upstage/solar-mini4:free` — **distinct from all three audit lanes** (CA hy4 · BA longcat · AA stepfun) and **content-bearing NOW**. A pivot that collapses diversity would be a named constraint, never a silent pass.
- The fan still fires only after acts 2–3 pass (this receipt IS act-3's); the AoA stays BLOCKED on its six-check landing gates.

---

## 8. The named failure classes / seams (the findings)

| id | class | finding |
|---|---|---|
| S1 | stale-row seam | the wire's study-branch head moved: `bac2672b3594` (context last-read) → `a848d06254` (live); the local tracking ref `687e69d020` is also stale |
| S2 | stale-row seam | the study-branch ref moved since the revision: `9d56caa557` → `caa9468556` (local) / `a848d06254` (live); the registry's "study HEAD" label (`f652b71b4e`) is the pre-restore pin, no longer the branch HEAD |
| S3 | identifier seam | pr-141876: registry `6609dac951` vs live/local `6609dacba9`; both retained |
| S4 | dangling-pin seam | a9c65dc4's pin `a9c65dc43d` resolves locally but is carried by no live branch (local or remote); reflog records it as "remote LIVE" earlier |
| S5 | stale-form seam | the registry's fork table is the pre-revision 4-hero form; the amended AM-F3 fork-set is 8 rows |
| S6 | probe-harness seam | the local darkhorse's 90s timeout (act-2's success took 103.5s); re-probed at 280s → 200/content — a harness seam, not a seat verdict |

**The failures are the findings.** No seam was reconciled away; each is named with its receipts.

---

## 9. Emission contract + hard lines

This file was written on disk FIRST with the receipts inside (§2–§6 + the appendix), then committed as `kanban-pilot` with **only this path staged**, on the current HEAD re-checked at commit, never pushed; the master's append-only; the plan, sealed artifacts, crons, anchors, and sibling plates left AS FOUND; local config left AS FOUND. A parse-fragment-only response has NOT landed. Exit 0 = deliverable on disk then sha.

---

## Appendix — the raw receipts (verbatim)

**A1 · this fire's seat probe (all seats, one shot each):**

```json
{"requested_model": "meituan/longcat-2.5:free", "pin": "PIN-90AF232492", "question_sha": "d809471c4746bc2b", "http": 200, "dt": 4.1, "responding_model": "meituan/longcat-2.5:free", "content_head": "PIN-90AF232492\n143379 is best known as an RFC number, specifically RFC 143379, w", "content_len": 232, "finish_reason": "stop", "prompt_tokens": 79, "completion_tokens": 84, "reasoning_tokens": null, "pin_echo_in_content": true}
{"requested_model": "tencent/hy4-flash:free", "pin": "PIN-D555EA7361", "question_sha": "fbb8f8e11a03a9b7", "http": 200, "dt": 6.4, "responding_model": "tencent/hy4-flash:free", "content": null, "content_head": "", "content_len": 0, "finish_reason": "length", "prompt_tokens": 80, "completion_tokens": 512, "reasoning_tokens": 512, "pin_echo_in_content": false, "reasoning_content_head": "We need answer user query. Need obey? Need reason.\n\nUser say"}
{"requested_model": "upstage/solar-mini4:free", "pin": "PIN-06EBAEC3EE", "question_sha": "e442d6746b331c2f", "http": 200, "dt": 0.9, "responding_model": "upstage/solar-mini4:free", "content_head": "PIN-06EBAEC3EE\n\nThe number 143379 is best known as a study identification number", "content_len": 118, "finish_reason": "stop", "prompt_tokens": 119, "completion_tokens": 34, "reasoning_tokens": 0, "pin_echo_in_content": true}
{"requested_model": "stepfun/step-3.7-flash:free", "pin": "PIN-4E31663E93", "question_sha": "2d49be97ebd93435", "http": 429, "http_body": "{\"status\":429,\"message\":\"You've reached this model's current fair-share rate limit. It adapts to demand — retry after the indicated delay, or try an alternate model.\",\"reason\":\"rate_limited\",\"retry_after\":435,\"alternates\":[\"deepseek/deepseek-chat-v3.1\",\"~openai/gpt-luna-latest\",\"deepseek/deepseek-ch", "dt": 0.3, "responding_model": null, "content_len": 0}
{"requested_model": "qwen/qwen4-max:free", "pin": "PIN-B6ACD6F27E", "question_sha": "7bea786018b127a9", "http": 404, "http_body": "{\"status\":404,\"message\":\"This model's free period has ended. To continue using Qwen4 Max, switch to 'qwen/qwen4-max'.\"}", "dt": 0.2, "responding_model": null, "content_len": 0}
{"requested_model": "openai/gpt-6-luna", "pin": "PIN-61CB753407", "question_sha": "209a00d99672bab2", "http": 200, "dt": 5.5, "responding_model": "openai/gpt-6-luna", "content_head": "PIN-61CB753407\n143379 is not a recognized RFC number, and I can’t identify it as", "content_len": 126, "finish_reason": "stop", "prompt_tokens": 65, "completion_tokens": 380, "reasoning_tokens": 342, "pin_echo_in_content": true}
{"requested_model": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf", "pin": "PIN-FBE313B8DE", "question_sha": "84e109d20ab2e684", "http": -1, "error": "TimeoutError: timed out", "dt": 90.1}
```

**A2 · the local darkhorse's re-probe (280s budget; the 90s was a harness seam):**

```json
{"requested_model": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf", "pin": "PIN-1C9DC02D52", "question_sha": "b4dc3667a8d0cd0f", "http": 200, "dt": 107.0, "responding_model": "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf", "content_head": "<think>\nThinking Process:\n\n1.  **Analyze the Request:**\n    *   **Role:** Probe ", "content_len": 1736, "finish_reason": "length", "prompt_tokens": 74, "completion_tokens": 512, "reasoning_tokens": null, "pin_echo_in_content": true}
```

**A3 · the config read-back:** `/root/.hermes/config.yaml` → `delegation.model: meituan/longcat-2.5:free`.

**A4 · the live refs (`git ls-remote origin`, 2026-11-23):**
`feat/135039-write-gate` = `d1bdb4582c…` · `fix/restore-read-action` = `6609dacba9…` · `re-cut-write-gate-surgical` = `9811e52752…` · `round2-combined-substrate` = `c39d8ce722…` · `round2-gate` = `268bb09147…` · `study/rfc-143379-rig-20261105` = **`a848d06254…`** · `study/rfc-143379-rig` = `cc6bf0827f…` · `study/rfc-143379-rig-20261114` = `113ed9e3d6…` · `study/rfc-143379-rig-20261115` = `f15d9ac682…`. Local branch HEAD = `caa9468556`; local tracking ref = `687e69d020`; context last-read = `bac2672b3594`.

**A5 · the register's sha256:** `0cff6a5b450bf819bb59b8e1404f05f7204777b95ded50083e3b4bbda94f4973` (both dates; == the runners' applied sha).

*Facimus semper — the failures are findings. The fleet is it/its.*
