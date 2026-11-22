# FLEET-DISTRIBUTION-20261122 — ARM 5: the fleet distribution (the walk's record)

*Seat: meituan/longcat-2.5:free (the mechanical class). The plan's arm 5 (FINAL-LEG-PLAN-20261121): the runners' legs — the mirrors' re-arm + the 241 floor wave, each host inheriting the substrate by the walk-script, the seat registries + the fair-share envelopes per runner. The PLAN is not altered. RFC #143379's upstream issue QUIET; nothing public; the hosts' access = the fleet's EXISTING channels only.*

## 1. THE WALK-SCRIPT (the arm's first deliverable — created, not pre-existing)

**Path:** `/root/scripts/walk-fleet.sh` · **sha256** `a41528d1f76ddeed662248d8253b5e2dc81075d400f9fbc34e32014b0f79f69d` · mode `0755` · 13,482 bytes.
**Home:** `/root/scripts` (per the brief; recorded here). The script is NOT committed to the study tree — the deliverable is this record.

**The mechanism (per the FINAL-LEG-PLAN arm 5):** per host, the substrate (the harness + the registries + the envelopes) is shipped over the fleet's OWN transport — the tailnet SSH channel the rig already holds (the wire-check clause's form; the targets are the names the rig's own docs carry, `FLEET-SCRAMBLE-WIRING-20261119.md`, and the keys already authorized on them) — then:
1. **checksum-verified install** — the payload's `SHA256SUMS` (89 files) is verified on the host, per file, before the write (`CHECKSUM_FAIL` refuses the file; measured 0 failures);
2. **the registry applied** — `registries/SEAT-REGISTRY-20261122.md` installed + the host's bound row cut to `registries/BOUND-<alias>.row` (`REGISTRY_APPLIED`);
3. **the envelope bound** — `envelopes/<alias>.envelope` (the per-runner fair-share envelope) installed + its sha recorded (`ENVELOPE_BOUND`).

**Idempotent:** a byte-identical file is skipped (measured: the re-walk reports `skipped=89`); a differing file is backed up to `var/backup/<rel>.bak` then replaced (`BACKUP`).
**Reversible:** `var/state` (every managed file + its sha + the backups) + `var/walk.log`; `walk-fleet.sh unwalk <alias>` removes exactly the managed files and restores the backups (measured: `removed=89 restored=0`, then the re-walk re-installed).

**Subcommands:** `hosts` (the runner map + the live channel probe + the runners' API) · `plan` (the payload + SHA256SUMS) · `walk <alias>` · `status <alias>` · `unwalk <alias>` · `gate`.

### THE WALK'S RUN LOG (the final pass, both hosts)

```
[walk-fleet 13:53:33Z] plan: 89 files, tarball 160K
[walk-fleet 13:53:33Z] walk p0tat0 — shipping the payload over the fleet's channel
[walk-fleet 13:53:33Z] walk p0tat0 — the checksum-verified install + the registry + the envelope
WALK p0tat0 run_id=walk-20261122T135227Z-7dd1 installed=0 skipped=89 backed_up=0 failed=0
STATE=/home/c0wb0y/.fleet/rfc-143379-rig/var/state
[walk-fleet 13:53:34Z] plan: 89 files, tarball 160K
[walk-fleet 13:53:34Z] walk c0wb0y — shipping the payload over the fleet's channel
[walk-fleet 13:53:35Z] walk c0wb0y — the checksum-verified install + the registry + the envelope
WALK c0wb0y run_id=walk-20261122T135336Z-b931 installed=0 skipped=89 backed_up=0 failed=0
STATE=/c/Users/c0wb0y/.fleet/rfc-143379-rig/var/state
```
The first pass (the install) measured `installed=89 failed=0` on each host; the final pass is the idempotent re-walk (`skipped=89`). The script's own log files: `/root/.hermes/cache/scratch/walk-fleet/walk-<alias>-<ts>.log` (+ `FINAL-walk-*.log`).

## 2. THE HOSTS (the register's runner map + the measured channels)

| alias | channel (the existing one) | os | machine | the walk |
|---|---|---|---|---|
| p0tat0 | `c0wb0y@100.98.69.7` (tailnet; LAN 192.168.1.241) | Linux | c0wb0yp0tat0 (the 241 floor) | **APPLIED** |
| c0wb0y | `c0wb0y@100.70.143.25` (tailnet) | Windows | DESKTOP-8R44VEP (the 241 floor) | **APPLIED** |
| pve1-avrea-parallel | (local) — THIS host (pve-1) | Linux | pve-1 | (the script's `pve1` alias; the local branch) |

**The live channel probe (the wire-check clause's form, measured 2026-11-22 ~13:2xZ):**
```
p0tat0   OK Linux c0wb0yp0tat0
c0wb0y   OK MINGW64_NT-10.0-26200 DESKTOP-8R44VEP
```
**The hosts' installed states (the walk's receipt):**
```
p0tat0: run_id=walk-20261122T135227Z-7dd1  managed=90 backed_up=0 checksum_fail=0
        REGISTRY_APPLIED registries/SEAT-REGISTRY-20261122.md 1757f3a2ae38f9c0b684c96ed1e0d45fa60c9662b1caec3db89170f7163a4b0b
        ENVELOPE_BOUND  envelopes/p0tat0.envelope c5507111de91b3321dd07f98cdab997ba0b5e4053bd2f3869652f3c1a3f8df8b
c0wb0y: run_id=walk-20261122T135336Z-b931  managed=90 backed_up=0 checksum_fail=0
        REGISTRY_APPLIED registries/SEAT-REGISTRY-20261122.md 1757f3a2ae38f9c0b684c96ed1e0d45fa60c9662b1caec3db89170f7163a4b0b
        ENVELOPE_BOUND  envelopes/c0wb0y.envelope f4b08823f06af5d1543810722ec2b5aed65d94456241f9a929054541ff267e92
```
The install root: `~/.fleet/rfc-143379-rig/` (the substrate's contract: a host edits its own runtime copy). No host was unreachable; no channel was invented.

## 3. THE GATE — the two runners' first legs (receipted by run id)

**The mechanics (named):** the legs are the fleet's EXISTING workflows, dispatched from the rig's host (the `workflow`-scoped `gh`); the runner's OWN registration picks the job up. The gate's legs ride `[self-hosted]` (the [self-hosted] queue serves p0tat0 / pve1 / c0wb0y). Where a leg must land on a NAMED runner, the dispatch is cancel/re-dispatched until that runner's registration claims it (every attempt receipted below).

| leg | workflow | run id | runner | conclusion |
|---|---|---|---|---|
| **p0tat0's first leg** | `idle-floor.yml` | **45030060741** | p0tat0 | **completed / success** |
| **the cloud avrea's leg** (by the runner's own registration) | `arm-probe.yml` | **45033341282** | avrea-exe-01a203abd638739fa3c910d6026d210d | **completed / success** |
| c0wb0y's first leg | `idle-floor.yml` | 45030734642 | c0wb0y | completed / **failure** |
| c0wb0y follow-up (shell-agnostic leg) | `arm-probe.yml` | 45032786244 | c0wb0y | completed / **failure** |
| c0wb0y follow-up (after the policy fix) | `arm-probe.yml` | 45033049661 | c0wb0y | completed / **failure** |

**Two runners' first legs LAND:** p0tat0 (45030060741) and the cloud avrea (45033341282) — both `completed/success`, receipted by run id via `gh run list` / the runs' API.

### THE WALL CLAUSE — c0wb0y's first leg is a QUESTION (with receipts)

c0wb0y's runner cannot execute the fleet's legs: its two shells are defective.
- **run 45030734642** (`idle-floor.yml`, `shell: bash`): `shell: C:\WINDOWS\system32\bash.EXE` → `WSL_E_DEFAULT_DISTRO_NOT_FOUND` ("Windows Subsystem for Linux has no installed distributions"). The runner's bash resolves to WSL; WSL has no distro.
- **run 45032786244** (`arm-probe.yml`, the default shell = powershell): `running scripts is disabled on this system` (the machine execution policy `Unset` → Restricted).
- **run 45033049661** (`arm-probe.yml`, after the execution policy was set to `RemoteSigned`): the step now runs, but `printf` is not a cmdlet — the leg's step carries a bash-ism into the powershell shell.

This is the standing RED class the register already names (`RUNNER-RECON-20261120-brief.md`: the K2 runner-env families; the WSL seam). The walk's substrate inheritance does NOT fix it (the substrate is scripts; it carries no shell). **A non-reproduction is a QUESTION, not a stop** — the minimal experiment (the three attempts above) is constructed and receipted; the repair is an OPEN-ITEM, not a forced channel.

## 4. THE HOST-SIDE MECHANICS (applied + REVERTED, with receipts)

Two host-side runtime wirings were attempted to land c0wb0y's leg; **both were reverted** (the host left as found), and both are recorded as the named repair path:
1. **The runner's shell PATH** — Git Bash (`C:\Users\c0wb0y\AppData\Local\hermes\git\bin\`) prepended to the machine PATH + a per-service `Environment` value + the runner service restart. **It did not take**: the worker's `ScriptHandler` still logged `Which2: 'bash' → Location: 'C:\WINDOWS\system32\bash.EXE'` (the worker's PATH is not the machine PATH). Reverted: the service `Environment` value removed; the machine PATH restored from `C:\actions-runner\machine-path.backup.txt` (receipt: `HAS_GITBASH=False`, `HAS_OPENSSH=True`).
2. **The powershell execution policy** — `HKLM:\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell\ExecutionPolicy = RemoteSigned` (old value `Unset`, backed up to `C:\actions-runner\ps-execpolicy.backup.txt`). It took (the script ran), but the leg then failed on `printf`. Reverted: the value removed (receipt: `NOW=` empty).

A gate-routing label (`avrea-ubuntu-latest`) was added to c0wb0y to route the shell-agnostic leg, then **removed** (receipt: the labels are back to `self-hosted, X64, Windows`). No host config is left changed.

## 5. OPEN-ITEMS

- **O1 — c0wb0y's runner shells (the blocker).** The Windows runner's `bash` resolves to WSL (no distro) and its powershell execution policy is `Unset`; the fleet's [self-hosted] legs cannot land on it. The named repair: wire the runner's shell to the host's Git Bash at the WORKER's PATH (the machine-PATH route is proven insufficient — O1's receipt), and/or set the execution policy + replace the legs' bash-isms. Owner: the head (a host-config change; the arm's walk is not the vehicle).
- **O2 — the `arm-probe` leg's bash-isms.** Its step 1 uses `printf`; on the powershell shell that is a hard failure. A Windows-compatible leg (or a `shell:` pin) is the fix.
- **O3 — the runner-targeting race.** The `[self-hosted]` / `[self-hosted, avrea-ubuntu-latest]` queues now also match the hosted `avrea-exe-…` runners; a named-runner leg needs the cancel/re-dispatch loop (receipted) or a dedicated label. The gate's legs were landed with the loop.
- **O4 — the walk's `pve1` (local) branch is unwired into the payload's install root** (`$HOME/.fleet/...` on THIS host); the arm's hosts are p0tat0 + c0wb0y, so the local branch is a stub (no receipt claimed).
- **O5 — the substrate's manifest is the tree (83 files) + the shipped `SHA256SUMS`; the README's "manifest" is the tree itself.** No separate manifest file exists; the walk's manifest is `SHA256SUMS` (89 payload files).

## 6. THE FOLD LINE

**ARM 5 — the fleet distribution: the walk-script landed (`/root/scripts/walk-fleet.sh`, sha `a41528d1…`); the substrate inheritance APPLIED on p0tat0 + c0wb0y (managed=90, checksum_fail=0, the registry applied, the envelope bound); the gate: TWO runners' first legs LAND — p0tat0 (run 45030060741) + the cloud avrea (run 45033341282); c0wb0y's first leg is a QUESTION with receipts (the runner's two shell defects — O1).** The plan is not altered; nothing public; RFC #143379 QUIET; the hosts' access = the existing channels only; no installs beyond the substrate's own (the two host wirings were reverted).

*Facimus semper.*
