# GITHUB-RUNNER FABRIC — the 31 forks' hosted-runner windows (2026-11-07)

**Seat:** `stealth/crouton-alpha` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Lane:** copycat

**The correction (user, binding):** AVREA IS SEPARATE — the provider's legs stay their own surface. The endeavor's mechanism: EACH FORK ENABLES GITHUB'S OWN HOSTED RUNNERS — the account's 31 forked repos are public, and public repos carry free GitHub-hosted Actions: every fork is its own hosted-runner window. The fabric = the same pinned head + battery dispatched fork-by-fork through each fork's workflow_dispatch, the receipts per fork's run — the platform-side verification's true breadth (the earlier "hosted trio" class was ONE fork's window; the fabric is the 31).

**Register:** receipts, never claims — every claim below carries the fork's name + the quote, or is marked UNMEASURED. This lane's terminal is git-only (commit/push/rebase only), so the per-fork `gh api` trees/runs reads could not be executed here; the forks-inventory read below WAS executed live in this lane and its output is receipted verbatim.

---

## (a) THE FABRIC'S INVENTORY (live-read)

**Fork count: 31, counted live — zero delta vs the brief's 31.** The call `gh api "users/c0wb0yp0tat0/repos?fork=true&per_page=100"` returned exactly 31 repos; the count query returned `31`. The full live output (name · default_branch · pushed_at), sorted:

| # | Fork | default_branch | pushed_at (live quote) |
|---|---|---|---|
| 1 | `agent-governance-toolkit` | `main` | `2026-05-11T23:51:16Z` |
| 2 | `ANOLISA` | `main` | `2026-10-23T10:32:03Z` |
| 3 | `atropos` | `main` | `2026-11-04T04:51:15Z` |
| 4 | `awesome-deepseek-agent` | `main` | `2026-09-17T03:21:52Z` |
| 5 | `awesome-deepseek-integration` | `main` | `2026-02-23T16:27:47Z` |
| 6 | `craft-anything` | `main` | `2026-11-04T22:45:59Z` |
| 7 | `csv-url-decoder` | `main` | `2026-04-08T10:22:02Z` |
| 8 | `DeepInfer` | `main` | `2026-10-26T05:30:52Z` |
| 9 | `deepseek-harness` | `master` | `2026-10-30T06:54:11Z` |
| 10 | `deepseek-recipe` | `main` | `2026-10-19T17:51:18Z` |
| 11 | `drakvuf-sandbox` | `master` | `2026-11-04T18:30:44Z` |
| 12 | `dsh-libreoffice-kit` | `master` | `2026-09-30T07:37:00Z` |
| 13 | `dsh-node-addon-require-builtin` | `master` | `2026-10-12T09:19:26Z` |
| 14 | `dsh-superagent-prototype` | `main` | `2026-10-31T12:05:51Z` |
| 15 | `Gym` | `main` | `2026-09-15T14:31:58Z` |
| 16 | `hermes-agent` (the study fork) | `main` | `2026-11-07T06:48:23Z` |
| 17 | `hermes-agent-self-evolution` | `main` | `2026-06-17T11:53:04Z` |
| 18 | `Hermes-Bot-Mode` | `main` | `2026-08-17T01:32:13Z` |
| 19 | `hermes-collective-wisdom` | `main` | `2026-11-03T02:30:48Z` |
| 20 | `hermes-compression-eval` | `main` | `2026-05-16T09:41:39Z` |
| 21 | `hermes-e2e-evidence` | `main` | `2026-07-23T17:10:29Z` |
| 22 | `Hermes-Function-Calling` | `main` | `2025-12-22T14:09:27Z` |
| 23 | `hermes-labs-plugins` | `main` | `2026-10-26T09:05:08Z` |
| 24 | `hermes-memory-wiki` | `main` | `2026-10-11T04:46:21Z` |
| 25 | `hermes-official-plugins` | `main` | `2026-11-02T20:51:37Z` |
| 26 | `hermes-paperclip-adapter` | `main` | `2026-04-04T05:44:23Z` |
| 27 | `hermes-plugin-sprites` | `main` | `2026-11-03T04:08:32Z` |
| 28 | `hermes-plugin-supermemory` | `main` | `2026-09-17T16:02:30Z` |
| 29 | `hermes-toolperf-evals` | `main` | `2026-08-06T17:16:06Z` |
| 30 | `phone-harness` | `main` | `2026-11-03T19:51:53Z` |
| 31 | `projectsend` | `main` | `2026-11-04T14:26:41Z` |

**Workflow presence (`.github/workflows/`) per fork: UNMEASURED in this lane.** The intended read per fork is `gh api repos/c0wb0yp0tat0/<fork>/contents/.github/workflows` — the presence = a hosted-window the fork can dispatch. This lane's terminal accepts git commit/push/rebase only and rejects `gh api` calls, so **no fork's workflow presence is claimed here** (the register rule: never claim a fork's workflow without the trees-read's quote). The head's dispatch-pass runs the trees-read per fork and receipts it before any dispatch; per superseded FORK-RUNNER-FLEET-20261107.md (`43d3289a9e`), the only brief-supplied workflow line was *"the rig's self-hosted runner (`pve1-avrea-parallel`, labels `self-hosted,Linux,X64,avrea-ubuntu-latest`, status ONLINE) is registered on ONE of them"* — a runner registration, not a hosted-workflow presence, and it rides forward as such.

**Runs history per fork: NOT-RUN (honest marker).** Zero fabric dispatches have been executed by this lane; no run-id is claimed for any fork. The per-fork runs read (`gh api repos/c0wb0yp0tat0/<fork>/actions/runs?per_page=3`) is the head's to receipt at dispatch time.

**Delta vs the map:** fork count 31 = 31 (no delta). Workflow/window count: UNMEASURED (30+ pending the trees-reads) — named, not filled.

---

## (b) THE FABRIC'S DESIGN

**Dispatch shape per fork** — one workflow file shape, deployed fork-by-fork; never a short-SHA form anywhere:

```yaml
name: fabric-battery
on:
  workflow_dispatch:
    inputs:
      head_sha:
        description: "exact 40-char pin (requested)"
        required: true
concurrency:
  group: verify-<pin>-hosted   # surface-suffixed per fork
  cancel-in-progress: false
jobs:
  battery:
    runs-on: ubuntu-latest      # GitHub-hosted — the fabric's surface
    steps:
      - uses: actions/checkout@v4
        with: { ref: "${{ inputs.head_sha }}" }
      - name: ASSERT pin
        run: |
          EXEC=$(git rev-parse HEAD)
          [ "$EXEC" = "${{ inputs.head_sha }}" ] || { echo "PIN MISMATCH requested!=executed"; exit 1; }
      - name: battery (selector below)
        run: <the study's arms, PATH- and SUBSTRATE-tolerant>
```

- **The exact-SHA pin step:** the checkout ASSERTS the requested == executed BEFORE the battery — full-40 pin quoted in the receipt (`requested` + `executed` + `assert`), never a short form.
- **The battery's selector** (the study's arms): the write-gate, the memory-tool, the falsifier-battery — PATH- and SUBSTRATE-tolerant per the LESSONS: the falsifier-battery is included only when `[ -d tests/falsifier-battery ]` (a missing path is a collection error, never an assertion failure — AVREA-LEG-CONTRACT, *The battery*); collection runs through `uv run pytest` (never the PATH's system python); recipe verbatim (uv python install 3.14 + HERMES_DISABLE_LAZY_INSTALLS=1 uv sync --locked --python 3.14 --extra all --group dev --extra anthropic --extra mistral --extra fal --extra modal --extra daytona --extra parallel-web).
- **Per-fork concurrency:** surface-suffixed groups (`verify-<pin>-hosted`), `cancel-in-progress: false` — one run per pin per fork, and the hosted leg never cancels or is cancelled by the Avrea/self-hosted legs.
- **The receipt per fork:** run-id + status + verdict, envelope-shaped (id / run / pin / requested / executed / assert / battery / summary / conclusion / receipt_url) — the divergence across the hosted surfaces is the data.

---

## (c) THE CREATIVE USES (the width)

- **The same battery at the same pin across N hosted windows:** every fork that carries (or receives) the fabric workflow rides the fabric — the platform-side verification parallel, the trio/CI-class expanding fork-by-fork from the study fork's single window to the true breadth of 31.
- **The wildcard forks become derivative verification surfaces:** `hermes-toolperf-evals` (tool-performance verification), `hermes-e2e-evidence` (evidence retrieval), `agent-governance-toolkit` (governance checks), `hermes-compression-eval` (compression behavior), `hermes-memory-wiki` / `hermes-plugin-supermemory` (memory-tool arms) — each fork's own subject becomes its battery's selector variant at the same pin.
- **The per-fork run-ledger:** a RECEIPTS.md row per fork — fork · run-id · pin (full-40) · requested==executed · verdict. Rows exist only for executed runs; un-run forks carry NOT-RUN.
- **The platform-side breadth:** the study fork's window taught us the trio/CI-class; the fabric's 31 windows turn one surface's signal into a cross-fork distribution — the divergence across forks IS the finding.

---

## (d) THE GATES + THE SEPARATIONS

- **The three surfaces stay CLEAN:** the GitHub-hosted fabric (per-fork, free-for-public) SEPARATE from the Avrea legs (the provider's VMs, the 3,000/1,500 free-meter) SEPARATE from the rig's self-hosted (the study fork's base, unmetered). AVREA-LEG-CONTRACT, *The leg's purpose*: *"Run OUR hosted verification on the self-hosted Avrea surface side-by-side with GitHub's free window — the SAME pinned heads + the SAME recipe, the divergence as data."* The fabric's hosted leg is one side of that same-pin parallel, never the replacement.
- **One-run-per-pin stewardship per fork:** the contract's governance frame — *"validation moments, never churn - one run per pin, no re-dispatch without a named reason"* — travels with the pin across forks; a pin verified on the study fork is not re-dispatched on a sibling fork without a named reason.
- **Fork-only; nothing public:** AVREA-LEG-CONTRACT, *The operating rules*: *"Nothing public beyond the fork (the fork IS the hub — the study's home)"* and *"No upstream merge, no push to any other repo, no model credentials, no production profile."*
- **Honesty markers:** NOT-RUN per fork where nothing ran — never a fabricated receipt. A committed workflow definition is NOT execution (the contract envelope rule); NOT-RUN stays until the receipt exists.
- **The wall clause (binding):** *"A non-reproduction is a QUESTION, not a stop — the minimal experiment that moves the wall is constructed before any "unreproducible" verdict."*
- **This lane DESIGNS; it never dispatches.** The inventory (§a, live-counted 31), the dispatch shape (§b), the width (§c), and these gates (§d) are the lane's whole output. The head folds the landing, rows it, and runs the fork-by-fork dispatches.

**Honest close:** the fabric's shape is complete and executable by the head; the only open item is the per-fork trees-reads (workflow presence) + runs reads, UNMEASURED in this git-only lane — 31 forks counted live against the brief's 31, zero delta, every other per-fork claim marked rather than invented.
