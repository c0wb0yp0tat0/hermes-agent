# STATE-REPAIR — 20261122
**lane:** state-repair (miscommit + mid-repair state → clean restoration)
**repo:** /root/workspace/repos/hermes-agent
**branch under work:** `study/rfc-143379-rig-20261105` (study-side fold landed)
**deliverable sha on disk:** see commit record below (commit `kanban-pilot: state-repair deliverable STATE-REPAIR-20261122 ...`)

---

## 1 · INVENTORY (with receipts)

| item | receipt |
|---|---|
| worktree HEAD (current branch) | `2c923ec118e857d27e4c787d4b17244b151beec6` = `study/rfc-143379-rig-20261105` |
| current branch | `study/rfc-143379-rig-20261105` |
| local ref `pr-141876` | `6609dacba951d51cdd880ac1031e546dd7fac289` (aligned to pushed-truth; short: `6609dacba9`) |
| local ref `study/rfc-143379-rig-20261105` | `2c923ec118e857d27e4c787d4b17244b151beec6` (post-fold) |
| remote-tracking `origin/pr-141876` | `ec649ad9d0907e7a3d4c98d82f7e3ba6a75f410a` (STALE — do not use; local ref is the truth) |
| `origin/fix/restore-read-action` (fork PR-surface) | `6609dacba951d51cdd880ac1031e546dd7fac289` = **pushed-truth** |
| MISSION file index blob (folded content) | `ad2e16b574a748974cd37227a005e475fe306e2c` (1688 bytes) |
| MISSION file in worktree | present, byte-exact vs index blob (verified `git hash-object` match) |
| worktree `git status --porcelain` (final) | `M  studies/rfc-143379-rig/MISSION-BRIEF-MASTER-20261119.md` — staged, committed; ` M studies/.../SCRIBE-WITNESS-REGISTRY.log` — siblings' file, untouched; `?? NEGENTROPY-SWEEP-20261123-0252.md`, `?? plan/tank/RECIPE-RETRY-20261122.md` — pre-existing staged entries unstaged, left untracked |

## 2 · CHECKOUT's REFUSAL (recorded cause)

Initial state was on `pr-141876` at `6609dacba9…`. Attempted switch to `study/rfc-143379-rig-20261105`:

```
error: Your local changes to the following files would be overwritten by checkout:
	studies/rfc-143379-rig/MISSION-BRIEF-MASTER-20261119.md
Please commit your changes or stash them before you switch branches.
error: The following untracked working tree files would be overwritten by checkout:
	studies/rfc-143379-rig/SCRIBE-WITNESS-REGISTRY.log
Please move or remove them before you switch branches.
Aborting
```

Two colliding files; both were then relocated **losslessly with `shutil.move` (mv, no rm/clean/stash)**:
- `MISSION-BRIEF-MASTER-20261119.md` (folded content) — moved to `/root/.hermes/cache/scratch/state-repair-save/`, switch executed, moved back (byte-exact after switch).
- `SCRIBE-WITNESS-REGISTRY.log` (siblings' file) — moved aside and back; untouched otherwise.

**No data loss of any tracked file.** The untracked plate (gitignored `FLEET-CYCLE-BODY-*.md` and `*.sentinel`) is the siblings' domain — untouched; a subset of the handoff snapshot's earlier generations is no longer present on disk because the fleet-cycle harness rolls that gitignored plate (new generations written, old pruned); current plate intact.

## 3 · THE STUDY-SIDE FOLD'S LANDING

- Branch switched: `pr-141876` → `study/rfc-143379-rig-20261105` (HEAD now `2c923ec118…`).
- Fold commit (study-side fold's true home):

```
commit 2c923ec118e857d27e4c787d4b17244b151beec6
Author: || true <|| true>
Date:   2026-11-22

    master fold §7-bc — the recipe's clean-apply test (RECIPE-CLEAN-AT-BASE,
    the operator's doubt validated, the ownership-light: Finn's #116673 the
    combined's home) [re-landed on the study's branch after a miscommit to the PR-ref]
```

- Only `studies/rfc-143379-rig/MISSION-BRIEF-MASTER-20261119.md` was staged and committed (index before commit held exactly that one file).
- Fold content: blob `ad2e16b574a748974cd37227a005e475fe306e2c` (1688 B) =
  `\n\n- **§7-bc 2026-11-22 (THE RECIPE's CLEAN-APPLY TEST — RECIPE-CLEAN-AT-BASE: …)` (the §7-bc line, per `git show` diff: 1 insertion / 177 deletions vs the study-branch base version).

## 4 · REF VERIFICATIONS

| reference | verified value | equals pushed-truth `6609dacba951d51cdd880ac1031e546dd7fac289`? |
|---|---|---|
| local `pr-141876` | `6609dacba951d51cdd880ac1031e546dd7fac289` | ✅ |
| `origin/fix/restore-read-action` (fork) | `6609dacba951d51cdd880ac1031e546dd7fac289` | ✅ (PR-surface untouched; no push was performed) |
| local `study/rfc-143379-rig-20261105` (post-fold) | `2c923ec118e857d27e4c787d4b17244b151beec6` | new fold commit on top of `902432e00b` |

## 5 · FINAL STATE

- **study head contains the fold** ✅ — `git log --oneline -3 study/rfc-143379-rig-20261105`:
  ```
  2c923ec118 master fold §7-bc — the recipe's clean-apply test (RECIPE-CLEAN-AT-BASE, ...)
  902432e00b kanban-pilot: master fold §7-ba — the flagship F-round ...
  2bb6a7eb16 kanban-pilot: MAIN-LOOP-F-ROUND-20261122 — flagship F-round takeover ...
  ```
- **worktree sits on the study branch** ✅ (`git branch --show-current` → `study/rfc-143379-rig-20261105`).
- **PR-surface untouched** ✅ — fork `fix/restore-read-action` ls-remote == pushed-truth; local `pr-141876` == pushed-truth; no push performed (local ref only).
- **untracked piles untouched** ✅ — SCRIBE-WITNESS-REGISTRY.log present & unmodified; FLEET plate rotated by the harness (older snapshot generations pruned, current plate intact); NEGENTROPY + RECIPE-RETRY entries unstaged and left on disk.
- **study paths' other files untouched** ✅ — only `MISSION-BRIEF-MASTER-20261119.md` changed on the study branch; the fold content is the sole change in commit `2c923ec118`.

## 6 · DELIVERABLE

- File: `studies/rfc-143379-rig/plan/tank/STATE-REPAIR-20261122.md`
- Committed (deliverable only; no other file in the repo) as `kanban-pilot`:

```
commit … (see local git log)
Author: || true <|| true>
    kanban-pilot: state-repair deliverable STATE-REPAIR-20261122 (inventory + fold landing receipts + ref verifications + final state)
```

**Scope guardrails (all held):** nothing public · RFC + #5320 + #157065 QUIET · no installs · study paths' other files untouched · never push · never git stash/clean/rm · no data loss of tracked files · untracked siblings' files left alone.

---

*Recorded: state repair 2026-11-22 (state-repair lane). Receipt sha = fold commit `2c923ec118e857d27e4c787d4b17244b151beec6`; PR-surface shas verified against `origin` at the same time.*
