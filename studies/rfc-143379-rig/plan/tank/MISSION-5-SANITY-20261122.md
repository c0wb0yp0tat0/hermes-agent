# MISSION-5-SANITY-20261122 — the consideration's claims re-derived at the tree

*Seat: meituan/longcat-2.5:free (PIN-READ-BACK VERIFIED at the fire). Rung: the consideration's second pair of eyes. The consideration under review: `plan/tank/MISSION-5-CONSIDERATION-20261122.md` (29fc0de53d). The tree is the truth: every claim below was re-derived at the local files; a non-reproduction is a QUESTION with receipts. The plan, the crons' code, the sealed armor, and the anchors were NOT altered. Nothing public; RFC #143379 + #5320 + #157065 quiet; no installs; write only under `studies/rfc-143379-rig/`; all local paths read via read_file/terminal; never pushed.*

**Inputs read in full:** the brief (`plan/tank/briefs/BRIEF-SPECIAL-MISSION-5-SANITY-20261122.md`) · the consideration (all 198 lines) · `/root/.hermes/cron/jobs.json` (64,480 chars, 21 jobs) · the 10 named scripts + `headroom-sweep.sh` + `anchor-rot-watcher.py` + `nous-free-tier-watch.py` + `/root/scripts/copycat-harness.py` · `/tmp/nous-post.json` · the web-cache's GitHub page (`/root/.hermes/cache/web/github.com-c2b7800238.md`, JoeProAI/mandate) and the cached README (`/root/.hermes/cache/web/raw.githubusercontent.com-b26459a0aa4a5e6b.cache.md`, sha256 `ca5c9f03262a10f7f996aa803b26a33f41a236f876c105da50367ff79de08271`) · the anchors `MEMORY.md` + `USER.md` + `HANDOFF-EMERGENCY-20261122.md` · the Hermes cron source (`cron/scheduler.py`, `cron/jobs_invariants.py`).

---

## 1. THE INVENTORY RE-DERIVED JOB-BY-JOB (claim (a))

**Count claim:** "21 jobs defined; 10 are no-agent script-crons" (consideration line 36). Tree: `jobs.json` has 21 entries; `no_agent:true` + `script` non-null = **10**; `script` non-null = **11**. **CONFIRMED** as stated. But see the headroom-sweep QUESTION below.

| # | job (jobs.json) | script path (tree) | exists | consideration's surface claim | tree re-derivation | verdict |
|---|---|---|---|---|---|---|
| 1 | motion-watch | `/root/.hermes/scripts/motion_watch.py` (290 lines) | ✓ | `gh api` subprocess, 3-attempt, GET only; state json + chain digest | `gh(path)` = `subprocess.run(["gh","api",path])`, `range(3)`, GET only; `STATE_FILE=…/var/motion_watch_state.json`; appends `007-tracker-digest.md`; reads issues 60040/5320/5323/5324/5325/157065/143379 + comments/files + gists 72222659/86807254 | **CONFIRMED** |
| 2 | dream-run | `…/dream-run.py` (100 lines) | ✓ | filesystem only; appends 009-wins + tombstone | `os/re/sys/datetime/hashlib/shutil`; appends `009-wins.md`; `shutil.move` to `sessions/.tombstoned/` | **CONFIRMED** |
| 3 | arxiv pre-print watch | `…/arxiv-watch.py` (77 lines) | ✓ | stdlib `urllib` to export.arxiv.org; state json | `urllib.request.urlopen("https://export.arxiv.org/api/query…")`; `os.replace` state.json | **CONFIRMED** |
| 4 | web storm cue | `…/storm-cue.py` (68 lines) | ✓ | filesystem only; no writes | `os/json/datetime`; reads chain mtimes + arxiv state; no writes | **CONFIRMED** |
| 5 | stall-alarm | `…/stall-alarm.py` (115 lines) | ✓ | `hermes kanban list/log/reclaim/dispatch`; seen-state | `sh()` kanban list/log/reclaim/dispatch + `ps`/`pgrep`; seen-state json | **CONFIRMED** (ps/pgrep sit outside the consideration's four named categories — minor) |
| 6 | runner-workspace-guard | `…/runner-workspace-guard.sh` (59 lines) | ✓ | "drains only `/opt/actions-runner/_work` (idle)" (line 46) | `rm -rf "$RUNNER_WORK"/*` **plus** `rm -f /tmp/battery-receipt.txt /tmp/avrea-* /tmp/gh-cli-cache/*` (line 45) | **DEFECT** — the "only" is false |
| 7 | learning-watch | `…/lab-learning-watch.py` (72 lines) | ✓ | `gh api` + `gh search prs`; seen-state | `gh api repos/{user}/{repo}`; `gh search prs --author … --state open`; seen-state | **CONFIRMED** |
| 8 | kit-gate-watch | `…/kit-gate-watch.sh` (11 lines) | ✓ | `gh api` GET `/pulls/116673`; no writes | `gh api repos/NousResearch/hermes-agent/pulls/116673 --jq …`; no writes; exit 0 | **CONFIRMED** |
| 9 | negentropy-sweep | `…/negentropy-sweep-arm.sh` (26 lines) | ✓ | "network: none direct (probe is local)" (line 49) | `timeout 60 hermes chat -q … -m "$SEAT"` → `https://inference-api.nousresearch.com/v1` (`config.yaml:176`); `nohup python3 /root/scripts/copycat-harness.py` → `urllib` POST to `inference-api.nousresearch.com/v1/chat/completions` + `SCRIBE_URL http://127.0.0.1:24282` + `subprocess.run(["bash","-lc",cmd])` (harness lines 11, 163, 292, 397) | **DEFECT** — the network claim is false; the harness surface is under-scoped |
| 10 | reapex-harvest | `…/reapex-harvest.py` (67 lines) | ✓ | `gh api` (7 seats, comments length, free-roster); state | `gh api repos/c0wb0yp0tat0/{7 seats}/actions/workflows/fabric-battery.yml/runs?per_page=1`; `gh api …/issues/1/comments?per_page=100 --jq length`; reads `models_dev_cache.json`; state | **CONFIRMED** |

**Job-by-job result: 8/10 rows exact; rows 6 and 9 falsified.**

**The aggregate boundary sentence (lines 52–57) — re-derived.** The consideration's own per-job map (line 54) names `hermes chat` probe (job 9); the summary two lines later (line 56) drops it. Concretely:
- Line 52: "`gh api` (3, 6, 7, 8, 10)" — **false**: 3 = arxiv (`urllib`), 6 = runner-guard (bash `df/du/rm`); the `gh api` jobs are **1, 7, 8, 10** (1 is omitted).
- Line 53: "filesystem writes (1, 2, 3, 4, 5, 6, 9, 10)" — 4 (storm-cue) writes nothing.
- Line 56: "tools = gh-get + std-lib-http + local fs + hermes kanban" — omits `hermes chat` (9) and the harness's `bash -lc` + `urllib`.
- Line 56: "network targets = api.github.com, export.arxiv.org" — omits `inference-api.nousresearch.com` (9's `hermes chat` + harness).
- Line 57: "write-paths = local state/digest dirs only" — omits dream-run's `009-wins.md` (chain) and 9's study artifacts + scratch logs.
- Line 55: "The four crons' allowed-calls boundary (the drafts, Section 4)" — Section 4 carries **10** drafts; "four" is stale (the four crons = #1–4 per §4's own split, yet the sentence's list includes `hermes kanban` (#5) and omits `hermes chat` (#9)).

**QUESTION (with receipts):** `headroom-sweep.sh` is an 11th script-bearing job (`jobs.json`: `script=headroom-sweep.sh`, `no_agent=null`, `model=upstage/solar-mini4:free`, every 360m). Hermes runs a non-`no_agent` job's `script` as a **pre-run wake-gate** (`cron/scheduler.py:2291-2295`); `headroom-sweep.sh:19` is `rm -rf "$d"` over lane clones/sandboxes. So a destructive script executes unattended every 360m, and the inventory's "10 … (the unattended surfaces)" (line 36) under-scopes it. **What would settle it:** the operator's/head's intent on whether a pre-run-gate script counts as an unattended surface; the tree says it fires pre-agent on every tick.

---

## 2. THE COMPARISONS' INTEGRITY (claim (b))

**Two-observation-liveness mapping.** `stall-alarm.py`'s `seen` set is a true two-observation gate: first observation → "first observation, watching (acts on persistence)" (line 65); persistence → `reclaim` + `dispatch` (lines 61–62). **CONFIRMED for stall-alarm.** But `lab-learning-watch.py`'s `seen` set is a **baseline-dedup**, not a persistence-before-action gate: first run records + exits 0 (lines 53–61); later runs print unseen lines and exit 0 (lines 62–70). The §3.1 watch row (line 67) lists `lab-learning-watch` among "the rig's two-observation liveness class" — an over-reach. **Minor DEFECT (line 67).**

**Five-doors' approval-wire's re-winding.** The design names the operator's word **explicitly** and correctly at line 84: "(a) public writes outside PR #1 — the operator's word, never the plugin's". **But** the same section's parenthetical (line 83) and §4 (line 166) name the gated surface as **"the single public surface (the PR #1 comment thread)"**. The GATE LAW final form (MEMORY.md:19; HANDOFF-EMERGENCY-20261122.md:6) gates **public writes OUTSIDE PR #1** — PR #1's thread is the homebase where study landings post freely (MEMORY.md:3). So lines 83/166 contradict line 84 and the pressed-law: they put the gate ON the exempt surface. **DEFECT-NAMED (lines 83, 166).** (The §3.2 quote at line 79 also omits the HANDOFF's "the RFC's surface, the autopilot's pilot gate" — minor.)

---

## 3. THE RECOMMENDATION'S COHERENCE (claim (c))

The one-pager's four elements are named: per-job manifests (§4, 10 drafts), the approval-wire (line 166), the violation-alarm (line 168), the policy-sha freshness (§3.5, §5.3). "No hidden gate / no install / no code-change" is present (§3.2; §4 header "as DESIGNS, never changes to the crons' code"; §5 line 193 "Nothing is installed"). Defects:
- **Policy-sha freshness is attributed to the wrong instrument.** Line 168–169: "the anchor-rot-watcher's +0-decay freshness marker **for the rulebook sha256**". `cron/scripts/anchor-rot-watcher.py` has **no sha256 logic** — its markers are substring checks over MEMORY.md/USER.md/CHAIN 001 (lines 12–22); `grep sha256` over the scripts = 0 hits. The +0-decay markers and a rulebook-sha256 checkpoint are two different mechanisms; the design conflates them. **DEFECT-NAMED (line 168–169).**
- **#6's boundary repeats the false row-6 claim** ("drain only the idle `/opt/actions-runner/_work` scratch", line 150; the script also removes three `/tmp` patterns, line 45). **DEFECT-NAMED (line 150).**
- **The manifests are inert.** `grep -rin manifest` over the scripts = 0 real reads (only a message string in `headroom-sweep.sh:26`). "Re-fed by the per-job manifests" (line 169) names a mechanism with no tree bearer; as a proposal this is fine, as a present-tense mechanism it is not. **Minor coherence gap.**
- **"exit-1 NEW rows"** (§3.1 block row, line 70) fits `stall-alarm` (exit 1, line 104) but not `lab-learning-watch` (exit 0 on new, line 70 of that script). **Minor label imprecision.**

---

## 4. THE RECEIPTS' HYGIENE (claim (d))

- **Paths.** The 10 script paths all exist at the named locations. **DEFECT:** lines 27–29 list `anchor-rot-watcher.py` under `/root/.hermes/scripts/`; the file lives at `/root/.hermes/cron/scripts/anchor-rot-watcher.py` (the `/root/.hermes/scripts/` listing has no such file). The consideration lists it in **both** dirs.
- **Labels.** Line 15–16: "score 57 likes, 4 replies" — `favorite_count=57` ✓, but `reply_count=null`; the 4 is `conversation_count`. The post quote's second half ("Hermes cron jobs run every night…") is **not** in `/tmp/nous-post.json` (its `text` = "6th place: Mandate, by @JoePro" + a t.co link). The mandate repo's numbers (140/140, 39/1038, 92.8%, MIT, v0.23.0/v0.23.1, `pre_tool_call`, `sqlite`, `stdlib`, fail-closed) are grounded in the cached page. The cached README exists with its recorded sha.

---

## 5. THE VERDICT

- **(a) INVENTORY: DEFECTS-NAMED.** 10/10 jobs exist at the named paths; the count 21/10 is exact; 8/10 surface rows exact. Falsified: row 6 (line 46, "drains only `/opt/actions-runner/_work`" — line 45 also removes `/tmp` patterns), row 9 (line 49, "none direct (probe is local)" — `hermes chat` + harness hit `inference-api.nousresearch.com`), and the aggregate lines 52–57 (gh-numbering 3/6; network targets omit the nous inference API; write-paths omit chain/study paths; "four crons" stale). QUESTION: headroom-sweep.sh's unattended pre-run `rm -rf`.
- **(b) COMPARISONS: DEFECTS-NAMED.** The two-observation mapping is true for stall-alarm (lab-learning's seen-state is a baseline-dedup, not a persistence gate — line 67 over-reach). The approval-wire names the operator's word explicitly and correctly at line 84, **but** lines 83/166 name the gated surface as the PR #1 comment thread — the surface the GATE LAW exempts; the law gates public writes OUTSIDE PR #1.
- **(c) RECOMMENDATION: DEFECTS-NAMED.** The four one-pager elements are present, but the policy-sha freshness is attributed to the anchor-rot-watcher, which has no sha256 logic (line 168–169); #6's boundary repeats the false "drain only" claim (line 150); the manifests are inert (no cron reads them).
- **(d) RECEIPTS: DEFECTS-NAMED.** `anchor-rot-watcher.py` misattributed to `/root/.hermes/scripts/` (lines 27–29); "4 replies" is `conversation_count`; the post quote's second half is ungrounded in `/tmp/nous-post.json`.

**AGGREGATE: DEFECTS-NAMED.** The consideration's per-job inventory is largely exact (8/10) and its headline count is exact, but its aggregate boundary sentence is falsified at the tree (job 9's provider call + harness; the gh-numbering), two per-job rows are false, the approval-wire's surface-naming contradicts the pressed-law it quotes, the policy-sha freshness is assigned to an instrument that does not implement it, and one receipt path is wrong. Not CONFIRMED; the defects are named with lines and receipts.

**STRONGEST CATCH:** the approval-wire's surface inversion — lines 83/166 gate "the PR #1 comment thread", the exact surface the GATE LAW final form exempts (the word gates public writes **outside** PR #1; PR #1 is the ungated homebase). That is the fabricated-gate class the consideration itself warns about. (Strongest inventory catch: job 9's network surface — `hermes chat` + `copycat-harness.py` → `inference-api.nousresearch.com` + a local scribe + `bash -lc` — contradicts "network targets = api.github.com, export.arxiv.org" and "none direct (probe is local)".)

---

## 6. THE FOLD-INPUTS (what the fold must carry)

1. **The verified inventory (corrected).** The 10 no-agent script-crons + paths + surfaces as in §1, with row 6's write-surface widened to include the three `/tmp` removals (line 45) and row 9's network widened to `inference-api.nousresearch.com` (+ the harness's local scribe + `bash -lc`). The count 21 jobs / 10 no-agent script-crons stands; `headroom-sweep.sh` is carried as an **opened question** (an 11th script-bearing job whose destructive pre-run `rm -rf` fires every 360m).
2. **The re-wired design's one-pager (corrected).** The four elements: per-job manifests (§4) · the approval-wire = **the operator's word over public writes OUTSIDE PR #1** (line 84; fix lines 83/166) · the violation-alarm's fail-closed (exit-1 NEW rows; note lab-learning exits 0) · the freshness guard = the anchor-rot-watcher's +0-decay markers **plus a to-be-built policy-sha256 checkpoint** (not the anchor-rot-watcher, which has no sha256). No hidden gate; no install; no code-change; the manifests are data with no tree bearer yet (named as a gap).
3. **The opened questions.** (i) headroom-sweep's unattended-surface status; (ii) the stale "four crons" count (Section 4 has 10 drafts); (iii) the lab-learning two-observation over-reach (baseline-dedup ≠ persistence gate); (iv) the manifests' tree bearer (no cron reads them); (v) the post-quote's ungrounded second half + the "4 replies" label.

---

*Deliverable: `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/MISSION-5-SANITY-20261122.md` — committed as kanban-pilot, study paths only, never pushed, never checked-out/stashed/rm'd. The consideration's code, the plan, the crons, and the anchors are untouched.*
