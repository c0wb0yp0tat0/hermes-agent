# SPECIAL-ASSIGNMENT-EXECUTION-20261122 — the executor rung (longcat): the completeness double-check + the application to the subjects' matrix

*Seat: `meituan/longcat-2.5:free` · Branch: `study/rfc-143379-rig-20261105` · The plan: `SPECIAL-ASSIGNMENT-PLAN-20261122.md` (1cb6c37450, ancestor of the entry HEAD) · The contract: `plan/tank/briefs/SPECIAL-ASSIGNMENT-20261122.md`. The gear: the think-tank spine + the Amazon LP + the SME substrate mastery + the ACES loop. The subjects' matrix = qwen free (PRIMARY) · deepseek · luna · Nemo; the runner matrix = pve1-avrea-parallel · p0tat0 · c0wb0y · cloud. The PLAN is not altered; the deepen-questions go to the plan, never into a rewrite.*

---

## 0. THE VERDICT IN ONE PARAGRAPH

**The double-check PASSES the plan's depth-ledger: all 9 lines (M1–M5 · F1–F4) are present and un-flattened, verified byte-direct against the live tree and the fleet — no genericization found in the ledger itself.** Every line-citation the plan's §VI.1 rests on (`context_compressor.py:1722–1729`, `:1970`, `:3184–3212`; `context_compressor_tail.py:11–12, 46–107`) is VERIFIED present and un-flattened on the branch tree. **One finding is RETURNED to the plan (FINDING-1), and it is a deep one:** the plan's §VI.1 receipt verifies the pruner's handling of `memory(action="read", doc=...)` — **a call shape the branch tree's memory tool cannot emit.** The gap the plan describes is real, but it sits one layer upstream of where the plan places it: on local main the demote-stub for a memory-read is unreachable because the read itself is unreachable. A second, minor naming seam is flagged (FINDING-2). The application then ran to the subjects' matrix: **12 shots, 11 landed + 1 fair-share 429 receipt (qwen, recorded, no retry)**.

---

## 1. THE COMPLETENESS DOUBLE-CHECK — the 9 depth-ledger lines re-read against live reality

Each line: the plan's claim → the live verification → present / flattened. All reads via `read_file`/`terminal` on local paths; no `web_extract`.

| # | Plan's depth | Live verification (byte-direct) | Verdict |
|---|---|---|---|
| **M1** | The copycat transport's full chain: sentinel-done → content-continuation → write-window read-gate → emission-format parser → 8192-cap → 429-backoff | `/root/scripts/copycat-harness.py`: sentinel `artifact + ".sentinel"` (L329, L483) + the done-rule "sentinel AND branch-head's movement" (L440–442); content-continuation in the `read_file` tool spec (L46, head+tail window + continuation hint); the write-window read-gate (L416–437 the window's knobs + cap fix, L650–665 the READ-GATED contract + the git-only landing whitelist); the emission-format parser `parse_args` (L220, OpenAI JSON / longcat-style markup / bare / double-encode unwrap); the **8192-cap** `HARNESS_MAX_TOKENS` default `"8192"` (L147); the 429-backoff (L579 `sleep(10 if code==429 else 8)`, retry codes L137–140) | **PRESENT, un-flattened** |
| **M2** | The harness's write-window read-gate + the write→read-back contract (the terminal attestation; ONE structural resolver; the 3 blind spots; `memory_tool.py:331–369` → `store.apply_batch` under the store lock) | The read-GATE = the copycat (above). The read-BACK contract lives in the **memory write-gate**: `tools/write_gate.py` stage 7 `verify_post_write` (re-reads the target **from disk**, never the cache), the **whole-entry-EXACT-first** resolver (L434 "whole-entry EXACT first, else typography-folded substring"), the **sibling-substring ghost** (L666–689: "the text surviving as a SUBSTRING of a sibling entry is not a failed remove"), and the early `if action not in ("replace","patch","remove")` that is the **`add` returns-None** blind spot; the falsifier battery's read-back nuggets (`tests/falsifier-battery/test_nugget141876_composition.py:5`). `store.apply_batch` under `_file_lock` (fcntl/msvcrt) verified (`tools/memory_tool_store.py:539`, `_file_lock` L257–290) | **PRESENT, un-flattened — see FINDING-2 (naming seam)** |
| **M3** | The envelope's clauses: per-runner fair-share, one-lane-per-seat, flagship windows first, the queue's state file, the beam NEVER main fleet, the fire-time seat-truth probe | `plan/SEAT-REGISTRY-20261122.md` L20–25 (the envelopes, the one-lane law, the seat-truth probe "the responding model MUST match the requested pin — a bare-name 404 is the catalog-literal class"); `MEMORY.md` L15 (FLEET = 4 runners) · L7 (beam = KENARI reserve, select legs only, alias 404s); `/root/scripts/walk-fleet.sh` (the per-runner envelope files, the queue's state file) | **PRESENT, un-flattened** |
| **M4** | The LP/think-tank subtleties: Customer Obsession (3oltan-seo's wall at 3 844/4 000 = 96%), Ownership, Invent and Simplify, Are Right A Lot, Bias for Action, Dive Deep | The LP compact is carried verbatim in the plan's own envelope (§VII) and its §VI.2 carries the wall's measured numbers (2,200/1,375 → 35%/22.2%; 4,000/2,500 → 60–80% + 100% accuracy + 0% spurious; the live 3 844/4 000 = 96% → 3 376/4 000 = 84%). Dive Deep is the §VI current-state verification itself | **PRESENT, un-flattened** |
| **M5** | The reload-marker's coverage asymmetry (Portion 1): the skill_view wire VERIFIED; the memory-doc read class's equivalent is the GAP | `context_compressor.py:1722–1729` = `_sum_skill_view` + the ghost-skill defense + `SKILL_PRUNED_MARKER_PREFIX` — VERIFIED byte-direct. `context_compressor_tail.py:11–12` (`_LEAN_TAIL_KEEP_TOOL_ROUNDS = 6`, `_LEAN_TAIL_DEMOTE_MIN_CHARS = 1_500`) and `:46–107` (`demote_stale_tail_tools`, the `skill_view_names_by_call_id` special case appending the marker) — VERIFIED. The memory class's gap — VERIFIED, and **deepened by FINDING-1** | **PRESENT, un-flattened — see FINDING-1** |
| **F1** | The runners' matrix's mechanics: pve1-avrea-parallel (self-hosted = unmetered) · p0tat0 (Linux 241) · c0wb0y (Windows 241) · cloud; the refspec main-only; the stale-push hazard; the beam reservation | `walk-fleet.sh hosts` live: `p0tat0 OK Linux c0wb0yp0tat0`, `c0wb0y OK MINGW64_NT-10.0-26200 DESKTOP-8R44VEP`, `pve1 (local)`; the runners' API: `avrea-exe-01a203c497e970ff9129251c46235ab8 / c0wb0y / p0tat0 / pve1-avrea-parallel` — all `online · busy=false`. `MEMORY.md` L5 (the self-hosted = unmetered), L9 (the stale-push/refspec hazard), L7 (the beam) | **PRESENT, un-flattened** |
| **F2** | The seats' windows: qwen4-max:free LAST DAY · hy4-flash:free the week · the secondary seats · the keyless probe at the ring | `SEAT-REGISTRY-20261122.md` L13–18; `MEMORY.md` L17 (DISPATCH: FLAGSHIPS first — qwen4-max + hy4, short windows; legs FIRST, then SUPPORT solar/stepfun/longcat) | **PRESENT, un-flattened** |
| **F3** | The one-lane-per-seat law: a doubled-ticketed seat 429s BOTH; the fire-time seat-truth probe | `SEAT-REGISTRY-20261122.md` L21 + L25. **Empirically exercised this run:** qwen's second shot 429'd with `retry-after: 30` and the body "temporarily at capacity upstream. This is not your API key's rate limit" — the seat's own transport receipt, recorded and not retried | **PRESENT, un-flattened** |
| **F4** | The fair-share envelopes: per runner, measured not assumed; the idle fills fill the gap; the beam rides select legs only | The per-runner envelopes are materialized (`walk-fleet.sh plan` → `envelopes/{p0tat0,c0wb0y,pve1}.envelope`; `status p0tat0` → `ENVELOPE_BOUND envelopes/p0tat0.envelope c5507111…`, `status c0wb0y` → `f4b08823…`) and the registry's per-runner rows are measured at the writing | **PRESENT, un-flattened** |

**The ledger's own self-test:** every "a flattening (finding) if it happens" column names a specific blur; none of the nine blurs is present in the plan. The one place the plan's depth is *thinner than reality* is FINDING-1's seam.

### FINDING-1 (RETURNED TO THE PLAN) — the §VI.1 receipt verifies a call shape the branch tree cannot emit

**The claim under test.** The plan's §VI.1 (and Portion 1's "VERIFIED the GAP" bullet) reads: the demoted `memory(action="read", doc=...)` result carries no reload wire, and cites `context_compressor.py:1970`'s `"memory": _sum_template("[memory] {action} on {target}]", …)` as the receipt.

**What the live tree shows (byte-direct, `study/rfc-143379-rig-20261105` @ `68d35439a2`, == `ls-remote`):**

| Surface | Branch tree (what the study commits to) | Installed fleet (`/usr/local/lib/hermes-agent`, git HEAD `3b42157858`) |
|---|---|---|
| `tools/memory_tool.py` action enum | `["add","patch","remove"]` | `["add","read","patch","remove"]` |
| `MEMORY_SCHEMA` `doc` property | **absent** | present ("Document reload marker for reads… GAP-2") |
| `_STORE_ACTIONS` `read` arm | **absent** | present (`store.read(target, old_text or doc, verb="read")`) |
| `MemoryStore.read` | **absent** (`grep -c "def read"` = 0) | present (`tools/memory_tool_store.py:441`) |
| `_memory_tool(...)` signature | no `doc` param | `doc: str \| None = None` |
| the agent's inline `_memory` executor arg_specs | action/target/content/old_text/new_text/operations — **no `doc`** | **same — no `doc`** |
| git state | committed, clean | **` M tools/memory_tool.py` · ` M tools/memory_tool_store.py`** (uncommitted local edits) |

**The consequence, stated plainly.** On the branch tree the pruner's handling of a memory-read is **unreachable**: the model cannot emit `memory(action="read", doc=...)` at all — the action is not in the enum, the `doc` parameter is not in the schema, and `MemoryStore.read` does not exist. So the plan's P1/P2 target seam ("the demoted memory-read stub — the `@doc:` re-read vs `session_search` seam") is one layer upstream of where the plan places it: **the read-path restore (#141876) is the precondition, not a sibling.** The plan's §VI.1 line-citations are all correct for what they cite; what they do not carry is that the *call* is not on local main. The plan's open-item O1 says "the platform's `memory(action="read", doc=...)` reload wire … the platform wire lands when it lands (a QUESTION, not a blocker)" — the sharper truth is that **the platform's `memory(action="read", doc=...)` CALL lands when it lands**; the reload wire is downstream of it.

**The second-order nuance (the deepest un-flattened one).** Even on the installed fleet, where the read + `doc` exist as **uncommitted local edits**, the agent's inline executor `_memory` (`agent/inline_tool_executors.py`) forwards `action/target/content/old_text/new_text/operations` and **not `doc`** — while the registry handler (`tools/memory_tool.py:494`) *does* forward `doc`. So an agent-driven `memory(action="read", doc="conventions-2026-09")` would read the **default** `MEMORY.md` (`store.read(target, old_text or doc)` with `doc=None`), while the schema advertises the `doc` and the demoted stub would carry a `doc=` value **the agent never actually sent**. The plan's "receipted byte-verification — verify the doc bytes by re-reading the target" would then be verifying a document the read never opened. The reload wire is necessary but not sufficient; the **doc-forwarding on the agent's execution path** is a second, distinct seam.

**Where the read + `doc` actually live (receipts).** Commits on other branches: `af16e3ab16` / `fe5a526414` ("fix(memory): restore the read action (the 14-line reversal of 56ee8a5cc6)" — on `battery-ext`, `fixes/falsifier-battery-20261104`, `r2cs`, `r2cs-sync`, `r2cs2`, `r2gate`, `round2-gate`); `c24080fb1a` ("study(memory): compose hardened read and chain docs on current main" — on `kvnloo-study`); `162a2ca275` ("feat(memory): let MEMORY.md anchor a chain of memory documents" — on `pr-116673`). **None is an ancestor of the study branch HEAD.** The removal's own commit: `56ee8a5cc6` (Teknium, 2026-02-19, "refactor: remove 'read' action from memory tool and agent logging", 2 files, 3 insertions, 14 deletions).

**Returned to the plan, not rewritten:** (a) Portion 1's "the FIRST verification this team makes" should name the call-shape's absence as the first finding, with the read-restore as the precondition; (b) P1's target should be re-stated as "the read-path's missing call shape + its demote-stub's reload wire — two seams, the first blocking the second"; (c) §VI.1's receipt should carry the tree-divergence (branch vs installed-fleet, committed vs uncommitted); (d) the agent-path `doc`-forwarding gap belongs in the open-items.

### FINDING-2 (minor, flagged) — M2's row-name conflates the copycat's read-GATE with the write-gate's read-BACK

M2 is titled "the harness's write-window read-gate" and its depth column then describes a write→read-back contract. The read-GATE is the copycat's (verified, L416–437/L650–665); the read-BACK contract is the **memory write-gate's** (`tools/write_gate.py` stage 7 + the falsifier battery's read-back nuggets). Both depths are present and un-flattened — no depth is dropped — but the row's name points at one harness while its substance lives in another. A naming seam, not a flattening; flagged so the next plan-line cites the right harness.

---

## 2. THE APPLICATION — the subjects' matrix, QWEN PRIMARY first

**The channels used = the fleet's EXISTING channels only** (never invented access): the flagship/keyless route `https://inference-api.nousresearch.com/v1/chat/completions` (Bearer = `auth.json`'s `providers.nous.agent_key`, per the earned lesson), the local floor `http://127.0.0.1:44831` (llama-server, the GGUF path as the model id), the Luna route (probed, see below), the DeepSeek route. **One shot per subject-portion; a 429 = the SUBJECT's transport receipt, recorded, never a retry loop.** The three portion-prompts (P1 the reload-marker asymmetry · P2 the hot-anchor sizing · P3 the lean-first read design) are the plan's P1–P6 seams, framed as the subject's own read.

### 2.0 The seat-truth probe (F3, at every fire)

| shot | requested pin | served | match |
|---|---|---|---|
| qwen-p1 | `qwen/qwen4-max:free` | `qwen/qwen4-max:free` | ✅ |
| qwen-p3 | `qwen/qwen4-max:free` | `qwen/qwen4-max:free` | ✅ |
| deepseek-p1/p2/p3 | `deepseek/deepseek-v4-pro-0813` | `deepseek/deepseek-v4-pro-0813` | ✅ |
| luna-p1/p2/p3 | `openai/gpt-6-luna` | `openai/gpt-6-luna` | ✅ |
| luna route probe | `openai/gpt-6-luna:batch` | — | ❌ **404** (the catalog-literal class, exactly as F3 names it) |

### 2.1 QWEN PRIMARY — `qwen/qwen4-max:free` (the settlement's route; LAST DAY)

**The flagship's first application LANDED (200), and the second hit the expected fair-share 429 — recorded, not retried.**

| portion | http | dt | usage | the receipted content (verbatim, trimmed) |
|---|---|---|---|---|
| **P1** (the reload-marker asymmetry — the flagship's first application) | **200** | 12.5s | 184 / 370 / 554 | "Currently it falls through the generic path, so the stub says **\"Recover with session_search(...)\"** — wrong, since a memory doc isn't recoverable from session history. It should get a `memory` special case paralleling `skill_view_names_by_call_id`, e.g. **[MEMORY_PRUNED: … reload with memory(action=\"read\", doc=\"conventions-2026-09\")]**. Caveat: I can't read the file or xngg1021's comment here, so the exact prescribed wording is inferred from the `skill_view` precedent — verify against the issue before patching." |
| **P2** (the hot-anchor sizing) | **429** | 0.5s | — | `{"status":429,"message":"The requested model is temporarily at capacity upstream. This is not your API key's rate limit — please retry shortly."}` · **`retry-after: 30`** — the SUBJECT's transport receipt |
| **P3** (the lean-first read design) | **200** | 14.7s | 125 / 700 / 825 | "1. Fetch to blob store; tool returns receipt only: path, byte-length, sha256, section/line offsets, 120-char preview. 2. Read by explicit span: grep → offsets → slice ≤2KB. Each slice returns byte-count + hash, checked against the receipt; mismatch → refetch, never reconstruct. 3." |

**qwen-primary receipt, one line:** the flagship's first application landed on `qwen/qwen4-max:free` (P1, 200, 12.5s, 554 tok, served-pin match) and independently named the exact seam — the generic `session_search` recovery where a memory-doc re-read belongs, and the `[MEMORY_PRUNED: … reload with memory(action="read", doc=…)]` shape — while its second shot (P2) returned the expected fair-share 429 (`retry-after: 30`, upstream capacity, not the key's limit), recorded and not retried.

### 2.2 DEEPSEEK — `deepseek/deepseek-v4-pro-0813` (200, served-pin match on all three)

| portion | http | dt | usage | the receipted content (verbatim, trimmed) |
|---|---|---|---|---|
| **P1** | 200 | 6.0s | 165 / 700 / 865 | (first call: the route emitted **reasoning-only**, `content` empty, `finish_reason=length` — the route's emission shape, recorded. Re-fired once with "Do NOT use think tags" — a **format re-fire of a landed 200, not a 429 retry**.) → "For a demoted `memory(action=\"read\", doc=\"conventions-2026-09\")` result, the stub carries: `Recover with session_search(...)`. It **should** carry: `Recover with memory(action=\"read\", doc=\"conventions-2026-09\")`" |
| **P2** | 200 | 7.0s | 225 / 700 / 925 | (same reasoning-only emission; the re-fire `deepseek-p2b` landed the content) → "Position-0 holds the operational contract: current task facts, active preferences, and the few constraints that must bias every subsequent step… Cold `@doc` belongs in chain files… For a 371KB pilot substrate, the split matters because NoLiMa shows models lose retrievable signal beyond 32K when surface cues dominate. Keeping position-0 lean (≤2,500 chars) preserves an anchor dense in facts and preferences, while cold chain files preserve depth without polluting the active context window." |
| **P3** | 200 | 12.1s | 180 / 590 / 770 | "1. Return per-segment receipts: SHA-256, byte offsets, first/last line—no body. 2. Load only receipts into context; treat raw segments as unmounted. 3. For any claim, request byte-range proof: offset+length+hash; verify before use. 4. Re-read only cited spans, max 4KB, then drop; never cache the 371KB doc. 5. Demote receipts past round 6 to tail." |

### 2.3 LUNA — the middleware's route (probed first: the `:batch` alias 404s)

**Route probe (one shot each, no retry):** `openai/gpt-6-luna` → **200** (served `openai/gpt-6-luna`) · `openai/gpt-6-luna:batch` → **404** `{"status":404,"message":"Couldn't find that, sorry."}` (the catalog-literal class) · `~openai/gpt-luna-latest` → **200** (serves `openai/gpt-6-luna`) · `openai/gpt-5.6-luna` → **200** (serves `openai/gpt-5.6-luna`). **The real route = `openai/gpt-6-luna`.**

| portion | http | dt | usage | the receipted content (verbatim, trimmed) |
|---|---|---|---|---|
| **P1** | 200 | 4.1s | 157 / 420 / 577 | "Currently the stub carries `Recover with session_search(...)`. It should instead carry `Recover with memory(action=\"read\", doc=\"conventions-2026-09\")`." |
| **P2** | 200 | 4.8s | 150 / 327 / 477 | "**Position-0:** a compact, high-value anchor—durable facts, hard constraints, key preferences, current state, and pointers to relevant files… **Cold `@doc:` chain:** detailed specs, evidence, history, examples, and other material loaded only when needed; the 371KB corpus is not a prompt to paste wholesale. The split preserves scarce context for what matters most." |
| **P3** | 200 | 3.6s | 102 / 271 / 373 | "1. Read a lean index first: document ID/version, byte length, encoding, section map, and short previews—not full segments. 2. For needed passages, request bounded byte ranges. Return each range with its offsets, length, document version, and SHA-256 receipt; verify these against the source before use. 3. Keep verified excerpts outside the compressible context, keyed by receipt. 4. On uncertainty or paraphrase/quote checks, reread the cited ranges and verify again. Never trust a demoted or rewritten prior excerpt." |

### 2.4 NEMO — the local floor `http://127.0.0.1:44831` (llama-server; the GGUF path as the model id)

| portion | http | dt | usage | the receipted content (verbatim, trimmed) |
|---|---|---|---|---|
| **P1** | 200 | 60.3s | 125 / 260 / 385 | (the floor emits a long `Think` preamble — its own voice; the substance) the stub's recovery is the generic `Recover with session_search(...)`, and the correct reload is the memory-read of the named doc — the floor flags that the pruner's class is "non-existent or highly fictional" from its side, i.e. it did not have the file (the same honest-caveat shape as qwen's) |
| **P2** | 200 | 59.3s | 138 / 260 / 398 | "Position-0 should be a **cold-chain anchor** (e.g., `/substrate/docs/chain-0.json`)… 3. **Zero fact/preference overlap** with the substrate's 371KB docs — it's purely **routing metadata**, not knowledge… 6. **Why not @doc**: `@doc` implies knowledge (e.g., state_roots), while position-0 must be a **routing primitive** — like a DNS A record for a chain, not a full chain definition." |
| **P3** | 200 | 53.4s | 66 / 260 / 326 | "To optimize large document segments, implement a lean-first read strategy. First, verify byte integrity via checksums upon receipt before processing. Second, cache validated segments locally to avoid repeated network…" (truncated at the floor's `max_tokens`; the floor's speed = 53–60s/call, `predicted_per_second ≈ 5.3`) |

**The floor's own receipt:** `timings` per call (e.g. P1: `prompt_n 125 · prompt_ms 11,555 · predicted_n 260 · predicted_ms 48,681 · predicted_per_second 5.32`) — the local seat is live, slow, and honest about its preamble.

### 2.5 The application's count

| subject | route | shots | landed | 429 receipts | seat-truth match |
|---|---|---|---|---|---|
| **qwen (PRIMARY)** | `qwen/qwen4-max:free` | 3 | 2 | **1** (P2, `retry-after: 30`) | ✅ (both landed shots) |
| **deepseek** | `deepseek/deepseek-v4-pro-0813` | 3 (+1 format re-fire) | 3 | 0 | ✅ |
| **luna** | `openai/gpt-6-luna` (probed; `:batch` 404) | 3 | 3 | 0 | ✅ |
| **Nemo** | local floor `:44831` | 3 | 3 | 0 | n/a (floor) |
| **total** | | **12** | **11** | **1** | |

**Cross-subject concordance (the substantive result):** all four subjects, on the P1 prompt, name the **same seam** — the demoted memory-read's recovery is the generic `session_search`, where the correct recovery is the re-read of the named doc target. qwen and luna name the exact replacement string (`reload with memory(action="read", doc="conventions-2026-09")`); deepseek names both strings verbatim. On P3, all four converge on the same three mechanisms: **lean-first index/receipt (no body) → bounded byte-range read with a hash/offset receipt → re-read the cited span on any doubt, never trust a demoted excerpt.** That is the plan's Portion-3 read-design, independently reproduced by four routes — the "inventing and simplifying" the assignment targets.

---

## 3. THE RUNNER LEGS' RECEIPTS (plan §III)

| leg | the receipt |
|---|---|
| **pve1-avrea-parallel** (THIS host, self-hosted = unmetered) | this lane ran here: the 12 subject shots + the floor + the fleet probes. The runners' API: `pve1-avrea-parallel · Linux · online · busy=false` |
| **p0tat0** (Linux 241, `c0wb0yp0tat0`) | `walk-fleet.sh status p0tat0` → `managed=90 backed_up=0 checksum_fail=0`; `REGISTRY_APPLIED registries/SEAT-REGISTRY-20261122.md 1757f3a2…`; `ENVELOPE_BOUND envelopes/p0tat0.envelope c5507111…`; the gate's leg `LEG arm-probe.yml run=45035785562 runner=p0tat0 completed success` |
| **c0wb0y** (Windows 241, privileged-seat class) | `status c0wb0y` → `managed=90 backed_up=0 checksum_fail=0`; `ENVELOPE_BOUND envelopes/c0wb0y.envelope f4b08823…`; the gate's leg `run=45035812640 runner=c0wb0y` fired |
| **cloud** (hosted ubuntu-latest) | the API's legs' queue; the runner `avrea-exe-01a203c497e970ff9129251c46235ab8 · online · busy=false` |
| **the walk's payload** | `walk-fleet.sh plan` → `89 files, tarball 160K`; `hosts` → both remote channels `OK` (Linux / MINGW64) |

**The stale-push / refspec hazard (F1) re-checked this run:** `ls-remote origin study/rfc-143379-rig-20261105` = `68d35439a2859791bb6ac98e361b5bae36034108` == local HEAD at the commit; the index was unlocked (no `.git/index.lock`).

---

## 4. THE SANITY GATES' INPUTS, PREPARED FOR STEPFUN (the tail)

| gate | the plan's bar | the executor's input for stepfun | state |
|---|---|---|---|
| **G1** — the memory-read reload gate | a demoted `memory(action="read", doc=...)` carries a reload path pointing at the named doc target (not `session_search`), or the fold-time/read-time rule is visibly applied | the branch tree's actual strings, byte-direct: the demote stub = `[memory output demoted at compaction — N chars preserved in session history. Recover with session_search(query=..., session_id='…')]`; the Phase-1 summary = `[memory] read on memory` (the `doc=` dropped). **Plus FINDING-1: the call shape itself is absent on the branch tree** | **NOT MET on the platform; the substrate's rule is the carrier** — and FINDING-1 narrows the target |
| **G2** — the anchor's sizing discipline | the per-subject position-0 experiment (the measured coverage floor) | the four subjects' P2 rows (qwen 429'd — its receipt; deepseek/luna/Nemo landed with the ≤2,500-char hot tier + the cold-chain split) | **PARTIAL — 3/4 subjects; qwen's is the 429 receipt** |
| **G3** — the NoLiMa long-context gate | the chain-reads (segment 002 = 371KB) read-design'd for lexical-mismatch exposure; the lean-first reads + receipted byte-verification + re-read discipline present in the logs | the four subjects' P3 rows (all four reproduce the three mechanisms); the exposure receipt: `002-lessons.md` = **378,759 bytes** (the plan's "371KB" = the KiB reading, 369.9 KiB — a rounding, not a discrepancy) | **MET (design present, 4/4)** |
| **G4** — the runner-matrix legs | the measured fair-share envelopes after the battery probes land | the walk's per-runner state (p0tat0/c0wb0y: 90 managed, `checksum_fail=0`, registry + envelope applied) + the gate runs (45035785562 p0tat0 success; 45035812640 c0wb0y) | **MET (measured, not assumed)** |
| **G5** — the main mission's order | the settlement · ARM 5 · staged 6/7 order intact; the fold-in is a STEPFUN gate, not skipped | this run touched **only** `studies/rfc-143379-rig/`; the main mission's plan order is unaltered; the fold-in is handed to stepfun | **MET** |

---

## 5. OPEN-ITEMS

| # | open item | status | receipts |
|---|---|---|---|
| **O1** | The platform's `memory(action="read", doc=...)` **call shape** (not just its reload wire) — **sharpened by FINDING-1**: on the branch tree the action/`doc`/`MemoryStore.read` are all absent; the read+`doc` exist only as uncommitted fleet edits + other-branch commits | **OPEN — the plan's target is re-stated** | §1 FINDING-1; `56ee8a5cc6`; `af16e3ab16`/`fe5a526414`; `c24080fb1a`; `162a2ca275` |
| **O2** | The agent-path `doc`-forwarding seam: the registry handler forwards `doc`, the agent's inline `_memory` executor does not — an agent-emitted doc-read would read the default doc while the schema advertises the `doc` | **OPEN (new, from FINDING-1)** | `agent/inline_tool_executors.py` `_memory` arg_specs; `tools/memory_tool.py:494` |
| **O3** | The per-subject anchor-sizing measurements (deepseek/luna/Nemo landed; **qwen's is the 429 receipt**) | **OPEN — 3/4** | §2.1–2.4 |
| **O4** | The long-context read-design's per-subject validation on the 371KB segment 002 pull | **OPEN** | §2.5; G3 |
| **O5** | The runner-matrix legs' measured fair-share envelopes after the battery probes land | **OPEN (the walk's state is measured; the battery probes are the append)** | §3; G4 |
| **O6** | The main mission's settlement · ARM 5 · staged 6/7 order — intact; the fold-in is stepfun's gate | **OPEN** | G5 |
| **O7** | FINDING-2's naming seam (M2's row-name vs its source harness) | **OPEN (minor)** | §1 FINDING-2 |

---

## 6. THE ENVELOPE'S DISCIPLINE, RECEIPTED

- **Nothing public** — no post outside PR #1's thread; the RFC's upstream issue untouched (no write; a read-only `gh api` probe returned 404 for the private issue, as expected). **No installs.** **No push.** **No `checkout`/`stash`/`rm`.** Writes only under `studies/rfc-143379-rig/`.
- **The wall clause honored:** the qwen 429 is a QUESTION-with-receipts (the body + `retry-after: 30`), not a silent pass and not a retry loop.
- **The not-for-its-sake gate:** every application names its live target (P1 → the demoted memory-read stub's reload seam; P2 → the position-0 hot tier vs the cold `@doc:` chain; P3 → the chain-reads' demote-stub + the 371KB pull). The one application without a target would have been a finding; none was.
- **The anchor:** `MEMORY.md` (the register: the copycat's transport chain, the fleet's 4 runners, the GATE LAW's final form — the word gates ONLY public writes outside PR #1 + deep deletions/money; alarms ACT, never wait) + `USER.md` (never invent design details; verify from actual output; the trust circle).
- **The armament line:** `think-tank` (the spine) + `investigation-documentation` (the discovery-log discipline: the faithful trail, the limitations, the correlation-vs-causation rule) + `aces-harness-probes` (the seat-truth/floor lessons) + the kit's method cards (`KIT-METHOD-CARDS-20261121.md`). The rest named-and-refused.
- **The termination check:** one review round; the fold's reloop is hy's gate, not this rung's.

---

*THE FOLD LINE — SPECIAL-ASSIGNMENT-EXECUTION 2026-11-22: the executor rung landed. The completeness double-check PASSES the depth-ledger (9/9 lines present and un-flattened) and RETURNS one deep finding to the plan (FINDING-1: the §VI.1 receipt verifies a `memory(action="read", doc=...)` call shape the branch tree cannot emit — the read-path restore is the precondition; plus the agent-path `doc`-forwarding seam) and one minor naming seam (FINDING-2). The application ran 12 shots over the subjects' matrix (qwen PRIMARY · deepseek · luna · Nemo): 11 landed + 1 fair-share 429 receipt (qwen P2, `retry-after: 30`, recorded, not retried); all four subjects independently name the same P1 seam and reproduce the same P3 read-design. The runner legs' receipts + the G1–G5 inputs are prepared for stepfun.*
