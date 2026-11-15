# FORK-RUNNER FLEET — the 31-fork runner surface's creative utilization (2026-11-07)

**Seat:** `stealth/crouton-alpha` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Lane:** copycat
**Register:** receipts, never claims — every workflow claim below carries a tree-read quote, or it is marked UNMEASURED. This lane's terminal is git-only (commit/push/rebase), so the live `gh api` reads in §1 could not be executed here; §1 names that gap instead of filling it with invented fork names.

---

## (a) THE FLEET'S INVENTORY (live-read — honest delta)

**Fork-count: UNMEASURED in this lane, vs the brief's 31.**
Mission brief, §1: *"The account holds 31 forked repos"* and *"the correction: the 31 forks = the fork RUNNERS, not the repo-map."* The intended call is:

```
gh api "users/c0wb0yp0tat0/repos?fork=true&per_page=100"   # names + pushed_at, counted against 31
gh api repos/<owner>/<fork>/git/trees/<sha>?recursive=1     # .github/workflows presence (named candidates only)
gh api repos/<owner>/<fork>/actions/runners                  # 1 online, the labels
```

Receipt — tool constraint (this lane): the terminal tool accepts *git commit/push/rebase only*; no `gh` execution was possible, and `/root/.hermes/plans/2026-11-07_0135-reapex-shift.md` sits outside this lane's read roots. Therefore **no fork name beside `hermes-agent`, no `pushed_at`, and no `.github/workflows` presence is claimed in this artifact.** The delta between the brief's 31 and this lane's verified count (1) is named here as **UNMEASURED (30 uninventoried)**; the head's execution pass must run the calls above and receipt them before any registration. The register rule holds: *never claim a fork's workflow without the tree-read's quote.*

**The one verified runner line (brief-supplied, not live-read):** mission brief, §1 — *"the rig's self-hosted runner (`pve1-avrea-parallel`, labels `self-hosted,Linux,X64,avrea-ubuntu-latest`, status ONLINE) is registered on ONE of them."* The study fork is `hermes-agent` (this repo); the runners-API line (`1 online, the labels`) is to be re-quoted live by the head before any new registration.

| # | Fork | pushed_at | `.github/workflows` (tree-read quote) | Runner now? |
|---|---|---|---|---|
| 1 | `hermes-agent` (the study fork) | UNMEASURED in lane | UNMEASURED in lane (no tree-read quoted) | Yes — `pve1-avrea-parallel`, `avrea-ubuntu-latest` (brief-supplied line above) |
| 2–31 | UNMEASURED — head to fill from the forks API | — | — | No (design only, §2) |

---

## (b) THE REGISTRATION MAP (fork-by-fork design — never executed by this lane)

**Mechanics per fork** (identical shape, per-repo because GitHub registers runners *per repository* — each fork needs its own token + config):

```bash
# per fork F = <owner>/<fork>:
TOK=$(gh api repos/F/actions/runners/registration-token --jq .token)
RUNNER_ALLOW_RUNASROOT=1 ./config.sh \
  --url https://github.com/F --token "$TOK" \
  --labels avrea-ubuntu-latest,self-hosted \
  --unattended --replace
# one config directory (e.g. actions-runner_F/) per registration; service name per fork.
```

**Fleet width:** 1 rig, N registrations. After each registration, the per-repo list `gh api repos/F/actions/runners` should show the rig once per registered fork — the fleet's width is the count of forks whose runners list carries `pve1-avrea-parallel` with `avrea-ubuntu-latest`, receipted per fork.

**Routing rule (the base-label universal-match lesson):** a workflow job picks up the rig only when **the label exists workflow-side AND the runner carries it on that repo.** So every candidate fork's avrea job must name `avrea-ubuntu-latest` in `runs-on`, and that fork must hold a registration. A fork with the label but no registration queues forever; a registration with no avrea-labeled job idles. `self-hosted`/`Linux`/`X64` alone do not route avrea work — `avrea-ubuntu-latest` is the discriminating label.

**Which forks take registration (design, pending §1):** Tier 1 = the study fork (`hermes-agent`, already registered). Tier 2 = forks whose tree-read shows a `.github/workflows` file that can host an avrea-labeled verification job (head to receipt per fork). Tier 3 = the rest — no registration until a workflow surface exists. No fork is claimed workflow-bearing until its tree-read is quoted.

---

## (c) THE CREATIVE USES (the endeavor's value-shape)

1. **Account-wide verification fabric.** The study fork's matrix (the falsifier-battery + the repo's own suite at the pin) is the reference leg; each Tier-2 fork becomes a second verification surface at the same rig — its own workflows run where they already exist, receipted the same way. No fork's workflow is claimed until its tree-read is quoted (§1 register).
2. **Dual-surface matrix per fork.** For every registered fork, the same pinned head + same recipe runs on two legs — the Avrea self-hosted leg and GitHub's hosted leg — side-by-side, divergence as data. AVREA-LEG-CONTRACT, *The leg's purpose*: *"Run OUR hosted verification on the self-hosted Avrea surface side-by-side with GitHub's free window — the SAME pinned heads + the SAME recipe, the divergence as data. The parallel is the point, never the replacement."*
3. **Same-pin sequencing per fork.** Concurrency groups keep one run per pin per fork, surface-suffixed (e.g. `verify-<pin>-avrea` / `verify-<pin>-hosted`), so the two legs never cancel each other and never double-spend a pin. This extends the contract's governance frame — *"validation moments, never churn - one run per pin, no re-dispatch without a named reason."*
4. **One-run-per-pin stewardship, extended fork-by-fork.** The per-pin budget travels with the pin across forks: a pin verified on the study fork is not re-dispatched on a sibling fork without a named reason; each fork's receipts accrue at the rig's own pace. Receipt shape per run is the contract envelope (`id / run / pin / requested / executed / assert / battery / summary / conclusion / receipt_url`), the pin asserted *before* the suite.
5. **Disk/thermal guards.** The rig's runner workspace drains at a disk threshold, **only after a live-worker check** — never drain under a running job. The contract's corrected truth governs: *"the true constraints are the rig's own cpu/disk/energy - the stewardship, not a platform quota."* Self-hosted means GitHub's hosted free-meter classes never apply; the stewardship is the meter.

---

## (d) THE GATES + THE STEWARDSHIP

- **This lane DESIGNS; it never registers.** The map (§b), the recipients (Tier 1/2/3), the routing rule, and these gates are the lane's whole output. **Registration EXECUTION rides the head's pass** under the user's standing green light.
- **The two-way door:** every registration is reversible — `gh api repos/F/actions/runners/<id> -X DELETE` (and `./config.sh remove`) tears a fork back out; a bad registration is a removal, never a stuck fleet.
- **Fork-only; nothing public.** AVREA-LEG-CONTRACT, *The operating rules*: *"Nothing public beyond the fork (the fork IS the hub — the study's home)"* and *"No upstream merge, no push to any other repo, no model credentials, no production profile."*
- **The quiet boundaries hold:** no upstream merge, no push to any other repo, receipts in `studies/rfc-143379-rig/RECEIPTS.md` first.
- **The wall clause (binding, verbatim):** *"A non-reproduction is a QUESTION, not a stop — the minimal experiment that moves the wall is constructed before any "unreproducible" verdict. A "green here / can't reproduce" without the construction is a hypothesis, not a finding."*

**Honest close:** the inventory (§a) is the open item — 1 verified fork against the brief's 31, the remaining 30 UNMEASURED pending the head's live `gh api` reads. The design (§b–d) is complete and executable by the head; no registration was performed or claimed by this lane.
