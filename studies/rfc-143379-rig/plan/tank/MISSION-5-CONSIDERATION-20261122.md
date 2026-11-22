# MISSION-5-CONSIDERATION-20261122 — the Mandate least-privilege pattern, assessed for OUR unattended crons

**Frame line: 0 installs · 0 public · RFC #143379 + #5320 + #157065 QUIET · nothing public · study paths only.**
The Mandate plugin is never installed into this rig — its pattern is the dish (the inventory, the drafts, the
comparisons, the recommendation). The crons' code is never altered; the drafts are designs for the readiness
loop's consideration. The post + repo reads are done (the fetched files: /tmp/nous-post.json,
/tmp/mandate-resolved.html, and the web-cache's GitHub page) — verified, read-only. The rig's own instruments
are the comparison's ground: the stall-alarm's two-observation liveness, the GATE LAW's five doors (the
rulebook's approval-wire), the honest-receipts' ledger, the egress-discipline, the write-freshness guard.

---

## 1. Input read (the contract, in full)

**The post.** Syndication read at `/tmp/nous-post.json` (NousResearch's Hackathon 6th-place post, replied under
the 5th-place Ariadne post): "6th place: Mandate, by @JoePro — Hermes cron jobs run every night with the full
toolset and nobody watching. Mandate watches what a job actually does, proposes a least-privilege rulebook, and
once you approve it, blocks every call outside it." Shape: watch → propose → approve → block.

**The repo.** JoeProAI/mandate (web-cache full GitHub page, read-only): MIT; Python 92.8%; 16 commits; the v0.23.0
/ v0.23.1 support + the measured make-prove CI matrix + the Leash-Line proof notes; hooks `pre_tool_call`,
`post_tool_call`; one policy per cron job id; observe → propose → approve → enforce; fails closed; stdlib only;
no outbound network; SQLite store per job. Proof class: recorded real-model traces, replayed free via
`make bench` (140/140 attack calls blocked, 39/1038 legit calls falsely blocked). Not installed.

**The rig's own unattended surfaces.** `/root/.hermes/cron/jobs.json` (the scheduled jobs registry) +
`/root/.hermes/scripts/` (stall-alarm.py, motion_watch.py, arxiv-watch.py, storm-cue.py, lab-learning-watch.py,
dream-run.py, reapex-harvest.py, runner-workspace-guard.sh, kit-gate-watch.sh, negentropy-sweep-arm.sh,
anchor-rot-watcher.py) + `/root/.hermes/cron/scripts/` (anchor-rot-watcher.py, nous-free-tier-watch.py) +
anchors `/root/.hermes/memories/MEMORY.md` + `USER.md` (read in full, one pass).

---

## 2. The inventory — what OUR unattended jobs ACTUALLY call

Registry: `/root/.hermes/cron/jobs.json`. 21 jobs defined; **10 are no-agent script-crons** (the unattended
surfaces). Of these, the **four cron-style crons** (interval, scripted, no model, deliver origin/local) are:

| # | Cron | script | tools | network targets | write-paths |
|---|------|--------|-------|-----------------|-------------|
| 1 | motion-watch hermes-agent tickets (every 30m) | motion_watch.py | `gh api` (subprocess, 3-attempt, GET only) | `api.github.com` — repos/NousResearch/hermes-agent/issues/{n}, /issues/{n}/comments, /issues/{n}/files, gists/{g}, /gists/{g}/comments | state json `/root/.hermes/scripts/var/motion_watch_state.json`; appends to chain digest `/root/workspace/master-page/memory-chain/007-tracker-digest.md` |
| 2 | dream-run daily consolidation (0 14 * * *) | dream-run.py | filesystem only (`open`, `shutil`, `os`) | none | appends `/root/workspace/master-page/memory-chain/009-wins.md`; tombstones into `DOCS/.tombstoned/` |
| 3 | arxiv pre-print watch (0 6 * * *) | arxiv-watch.py | stdlib `urllib.request` | `export.arxiv.org/api/query` (GET, no key) | atomic write via `os.replace` to `/root/.hermes/cache/scratch/arxiv-watch/state.json` |
| 4 | web storm cue (0 8 * * *) | storm-cue.py | filesystem only (`os`, `datetime`, `json`) | none | none (prints the cue; state read-only) |
| 5 | stall-alarm (board lifecycle) (every 15m) | stall-alarm.py | `hermes kanban list/log/reclaim/dispatch` (subprocess) | none | seen-state json `/root/.hermes/cache/scratch/stall-alarm-seen.json`; the two-observation liveness also drives kanban reclaim + re-dispatch |
| 6 | runner-workspace-guard (disk) (every 15m) | runner-workspace-guard.sh | bash (`df`, `pgrep`, `du`) | none | state `/root/.hermes/state/runner-guard.state`; drains only `/opt/actions-runner/_work` (idle) |
| 7 | learning-watch (lab habits) (every 15m) | lab-learning-watch.py | `gh api` + `gh search prs` (GET, 2 users, repos + open PRs) | `api.github.com` | seen-state json `/root/.hermes/cache/scratch/lab-learning-watch-seen.json` |
| 8 | kit-gate-watch (every 30m) | kit-gate-watch.sh | `gh api` GET `/pulls/116673` (read-only) | `api.github.com` | none (exit 0 quiet path) |
| 9 | negentropy-sweep (every 120m) | negentropy-sweep-arm.sh | `hermes chat` probe + `nohup python3 copycat-harness.py` | none direct (probe is local) | artifacts `/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/NEGENTROPY-SWEEP-*.md`; log `/root/.hermes/cache/scratch/copycat-mission/`; brief restored from repo template |
| 10 | reapex-harvest (every 60m) | reapex-harvest.py | `gh api` (workflows runs for 7 seats, issues/1/comments length, free-roster cache) | `api.github.com` | state json `/root/.hermes/scripts/var/reapex-harvest.state` |

**Tool-usage map (per job):** the attritional surfaces are `gh api` (3, 6, 7, 8, 10 — GitHub REST GET, only);
`urllib`/std-lib (3); `hermes kanban` subprocess (5); filesystem writes (1, 2, 3, 4, 5, 6, 9, 10) — always local,
never the repo tree, never a public surface; `hermes chat` probe (9, the harness's own gate). No `curl`, no
`patch`, no installs, no network writes, no public writes. The four crons' allowed-calls boundary (the drafts,
Section 4) is a subset of exactly these observed surfaces: tools = gh-get + std-lib-http + local fs + hermes
kanban; network targets = api.github.com, export.arxiv.org; write-paths = local state/digest dirs only.

---

## 3. The pattern's design-integrity (the data comparisons)

### 3.1 Mandate's watch → propose → approve → block loop vs the rig's own instruments

| Mandate step | Rig's native instrument | Match |
|---|---|---|
| **watch** | stall-alarm's two-observation liveness (silent when healthy, NEW problems alerted, persistence → reclaim + re-dispatch same cycle, bounded) | **strong** — the rig's watchers (motion-watch, arxiv-watch, lab-learning-watch, kit-gate-watch, reapex-harvest, negentropy-arm) are the native observers; the Mandate's watch = the rig's two-observation liveness class |
| **propose** | per-job manifest: the tool-usage map, the allowed-calls boundary (tools / network targets / write-paths) | **strong** — the rig already carries a per-job shape (jobs.json + scripts); the rulebook's "one policy per cron job id" = the rig's per-job dispatch |
| **approve** | the operator's word — GATE LAW final form (the word gates ONLY public writes outside PR #1 + deep deletions/money; internal doors act, never wait) | **partial** — the Mandate's approve step is a *self-imposed* gate inside the plugin, which the rig's law names as the FABRICATED-GATE class |
| **block** | the violation alarm (exit-1 NEW rows + fail-closed internal gates + the anchor-rot-watcher's +0-decay freshness markers) | **strong** — block-on-violation ≈ the rig's fail-closed guard |

The rig's watching-class is **two-observation** (the stall-alarm's `seen` set: baseline records, NEW-only
alerts, persistence check before acting). The Mandate's watch is single-observation per rule (observed runs →
rulebook). The rig does not need the plugin's approval prompt: it has the operator's word as the only gate,
and every other hold is a defect.

### 3.2 GATE LAW's five doors vs the rulebook's approval-wire

GATE LAW (final): *the word gates ONLY public writes outside PR #1 + deep deletions/money; any other hold is a
FABRICATED gate (defect); alarms ACT, never wait.* The Mandate's `approve` lives outside that law — it is a
second approval-wire that the rig's five doors do not map to. **Unmapped rulebook-hold = the fabricated-gate
class.** The design must name its approval-wire explicitly: for our unattended jobs the wire is the operator's
word **only** for the single public surface (the PR #1 comment thread), and every other hold is self-fired by
the rig's own alarms. The draft's approval-wire is therefore: (a) public writes outside PR #1 — the operator's
word, never the plugin's; (b) everything else — the rig's internal doors act. A draft that leaves the plugin's
`approve` step unmapped is a defect, not a design.

### 3.3 honest-receipts' ledger vs the Mandate's "proof"

The rig's honest-receipts' ledger = receipts re-derived from actual bytes (ls-remote tips, gh api output,
hashes, the anchor's hard-line markers, the two-observation seen-states) — independent re-derivation, not
prose. The Mandate's proof = a self-reported measured run (proof/proof.json, PROOF.md, bench README: 140/140,
39/1038, make prove wall-clock) — a reproducible **self-report**, not an independently re-derived receipt.
Comparison: the Mandate's proof is the rig's *receipt-grade self-report* class; it is open (raw traces in the
repo, free replay) but it must be re-derived from the ledger's job-id/version/sha256/command-lines fields
before it counts as receipt-grade. The rig's ledger is the stricter class; the pattern's proof is accepted as
self-report only when it carries receipts, not summaries.

### 3.4 egress-discipline vs the rulebook's network-boundaries

Egress discipline (rig's own): the word gates ONLY public writes outside PR #1 + deep deletions/money; internal
doors act; the anchors' hard-line markers are the +0-decay surface. The rulebook's network-boundaries: a
per-job policy of tools / paths / commands / hosts / limits, enforced in `pre_tool_call`, fail-closed on any
mismatch, never outbound network (hosts: [] default), stdlib only, reads/writes only its own data dir.
Comparison: the pattern's boundary discipline (per-job, least-privilege, read-file/terminal/write/path/host/
command) maps 1:1 to the rig's egress discipline — the rig's five doors are the internal expression of the
rulebook's per-job boundaries, and the rig already enforces per-domain egress without the plugin.

### 3.5 write-freshness guard vs the block-on-violation

Rig's write-freshness guard: the anchor-rot-watcher's +0-decay hard-line markers (MEMORY.md/USER.md/CHAIN 001)
rows an alert when a marker rots out; the ledger re-derives keys each run; the stall-alarm's seen-state is a
staleness detector (NEW-only alerts, baseline records the first observation). Mandate's block-on-violation: a
changed policy whose sha256 no longer matches its approval is blocked; fail-closed if Mandate errors in enforce
mode. Comparison: both are freshness guards over *a policy/marker that can rot between runs*; the rig's is
per-marker and local (+0-decay, proven in the field), the Mandate's is per-policy sha256 (per-job, in the
SQLite store). The design adopts the rig's +0-decay as the anchor freshness guard and the policy sha256 as
the per-job freshness checkpoint — the rulebook's "changed policy blocked" is the rig's write-freshness guard
for the rulebook itself.

---

## 4. The drafts — rulebook drafts per job (as DESIGNS, never changes to the crons' code)

The four crons' manifests (the per-job designs):

**#1 motion-watch (cron every 30m).** tools: `gh api` GET — issues/{n}, /comments, /files, gists/{g}, /comments
(seeking stewards c0wb0yp0tat0 / iainlane and defect-class paths agent/, cli/, memory.md, stage/, yaml/,
tools/patch). network: `api.github.com` only. write: state json + chain digest append. **Allowed boundary:
read-only GET against NousResearch/hermes-agent; hosts=[github.com]; commands: none (tool-call only); write:
state + digest.**

**#2 dream-run (0 14 * * *).** tools: filesystem only. write: 009-wins.md append + tombstone move. **Allowed
boundary: read/write only under /root/workspace/master-page/memory-chain; no network; no repo writes.**

**#3 arxiv-watch (0 6 * * *).** tools: stdlib http GET. network: export.arxiv.org only, no key. write: state
json (atomic os.replace). **Allowed boundary: GET only, arxiv.org; no writes outside the arxiv state file.**

**#4 web-storm-cue (0 8 * * *).** tools: filesystem only. **Allowed boundary: read-only against the chain
segments and arxiv state; prints the cue; no writes.**

The watchers' manifests (the same pattern, per job, as designs):

**#5 stall-alarm (every 15m).** tools: `hermes kanban list/log/reclaim/dispatch` (read the board; the alarm is
the actor, never a word-gate). write: seen-state json. **Allowed boundary: read-only board inspection + the
alarm's two-observation liveness (baseline → NEW-only alerts → reclaim + re-dispatch on persistence, bounded
by max-retries and failure-limit).**

**#6 runner-workspace-guard (every 15m).** tools: bash disk inspection. write: guard state. **Allowed boundary:
read-only disk inspection; drain only the idle `/opt/actions-runner/_work` scratch; NEVER prune /root/.lmstudio
or *.gguf (harbor model, 2026-11-21 exclusion).**

**#7 lab-learning-watch (every 15m).** tools: `gh api` + `gh search prs` (GET). write: state json. **Allowed
boundary: read-only GET of kvnloo/xngg1021 repos + open PRs; no writes outside the seen-state json.**

**#8 kit-gate-watch (every 30m).** tools: `gh api` GET /pulls/116673. **Allowed boundary: read-only; exit 0 on
the quiet path.**

**#9 negentropy-sweep (every 120m).** tools: `hermes chat` probe + harness arm. write: artifacts under the
study paths + scratch logs. **Allowed boundary: probe + artifact paths only; no network writes; the brief
absence is a visible failure (no silent skip).**

**#10 reapex-harvest (every 60m).** tools: `gh api` GET (workflow runs, comment count, free-roster cache).
write: state json. **Allowed boundary: read-only GET; no writes outside the state file.**

The approval-wire for every draft: the operator's word, for the single public surface (PR #1 comment) only;
every other hold is the rig's internal doors acting (two-observation liveness → NEW-only alarm → fail-closed
block). The violation's alarm = the rig's exit-1 NEW rows + the anchor-rot-watcher's +0-decay freshness marker
for the rulebook sha256, re-fed by the per-job manifests.

---

## 5. The recommendation

**Adopt-the-pattern, re-wired into the rig's own laws** — the pattern's four mechanics (observe → propose a
minimal per-job policy → the operator's word approves the single public surface only → block every call outside
it) fit the rig's five doors exactly, and the rig already carries the watch, the manifest, the block and the
freshness guards. The adaptation required (the reasons):

1. **Rewire the approval-wire.** The Mandate's `approve` step is a *self-imposed gate* that the rig's GATE LAW
   names as the fabricated-gate class. The design maps the wire to the rig's law: the operator's word gates
   ONLY public writes outside PR #1 + deep deletions/money; every other hold self-fires.
2. **Rewire the proof.** The Mandate's "proof" is a self-reported measured run; the rig's honest-receipts'
   ledger requires receipts re-derived from bytes (job-id/version/sha256/command-lines), so the pattern's
   proof becomes per-job ledger rows, not prose summaries.
3. **Refeed the freshness guard.** The rulebook's changed-policy sha256 check becomes the per-job freshness
   checkpoint; the rig's +0-decay markers remain the anchor freshness guard.
4. **Keep the watchers as the native observers.** The rig's four crons + the watchers ARE the watch step;
   the Mandate's observation machinery is not needed on top, it is the rig's own liveness.

**Spine:** the rig's own laws' fit — watch (two-observation liveness), propose (per-job manifests), approve
(operator's word, one public surface), block (violation alarm + fail-closed), freshness (+0-decay + sha256).
Nothing is installed; nothing is public.

---

*Deliverable: /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/MISSION-5-CONSIDERATION-20261122.md
— committed as kanban-pilot, study paths only, never pushed, never checked-out/stashed/rm'd.*
