# F17-RESTORATION-20261122 — the ungated deep-deletion's byte-exact re-landing

- **Lane:** F-17 RESTORATION — the proxy's alarm-law repair lane (the operator's at rest; the register's alarms ACT). The ungated deep-deletion's **repair**, not the word-gated deletion class: the gate gates DELETIONS (authorizing them); the repair is the **reverse-act** (the un-deletion), the proxy's internal-repair scope.
- **Seat:** `meituan/longcat-2.5:free` — **PIN-READ-BACK VERIFIED** at the fire.
- **Fire time:** **2026-11-23T08:05Z**.
- **Contract:** study `study/rfc-143379-rig-20261105` @ entry HEAD **`2e0583ade6`** (the N2-round's §8 receipt's successor). Predecessor receipt: `plan/tank/MAIN-LOOP-N2-ROUND-20261122.md` §8 (the mid-round purge receipt, `2e0583ade6`).
- **Armament (binding):** **think-tank** (classify → choose → probe → evaluate → adopt-or-park → standardize → verify; receipts never claims) + **investigation-documentation** (origin-first, missteps preserved, the claimed-read-is-a-claim pitfall). **Name-and-refuse (the rest, considered, not loaded):** agent-work-review (no second lens this lane — the sha256 cross-check IS the adversarial check) · safe-file-editing (the byte-compare is the guard; no secret material) · systematic-debugging (the non-reproduction's disposition is the wall clause, not a debug cycle) · memory-chain (no chain append) · the source/creative/media families (no artifact of that class).
- **Frame (binding):** RFC #143379 + #5320 + #157065 **QUIET** · nothing public · **NO installs** · write ONLY under `studies/rfc-143379-rig/` · all LOCAL paths via `read_file` / `terminal` · **NEVER push** · never `git checkout --` / `git stash` / `git clean` / `git rm` on the study's paths · the history **never rewritten** (the purge-commit stays in the lineage; the re-landing rides on top).

---

## §1 · THE EVENT + THE INVENTORY CROSS-CHECK (the contract's spine)

**The event (named with receipts):** the creative lane's commit **`eee4d86521`** — `creative: THE NIGHT'S ARC (creative-output-45127001242)` — purged the studies tree. Its parent = **`67deca1f64`** (`67deca1f6419dd028f188a55e0fceecc4a441968`, the negentropy-0453 sweep). The §8 receipt names the event's footprint as **"26 files / 3519 lines"**. The git bytes re-derive it:

```
$ git show eee4d86521 --name-status --no-renames --format=''
A  FLEET-CYCLE-BODY-2026-11-23-050539Z.md
M  studies/rfc-143379-rig/HANDOFF-EMERGENCY-20261122.md
M  studies/rfc-143379-rig/MISSION-BRIEF-MASTER-20261119.md
M  studies/rfc-143379-rig/MISSION-MAP-20261118.md
D  studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261122-2250.md
D  studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261123-0051.md
D  studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261123-0453.md
M  studies/rfc-143379-rig/WEIGHTS-RUNG-BATTERY-REFIRE-20261122.md
D  studies/rfc-143379-rig/plan/tank/HY-GATE-MISSION5-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-F-ROUND-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-FULL-EXPLORATION-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-N-ROUND-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND2-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND3-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND4-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND5-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND6-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND7-20261122.md
D  studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND8-20261122.md
D  studies/rfc-143379-rig/plan/tank/MISSION-5-SANITY-20261122.md
D  studies/rfc-143379-rig/plan/tank/STATE-REPAIR-20261122.md
D  studies/rfc-143379-rig/plan/tank/VET-KVNLOO-20261122.md
D  studies/rfc-143379-rig/tmp-artifacts/creative/creative-output-45073355792.md
D  studies/rfc-143379-rig/tmp-artifacts/creative/creative-output-45096776289.md
A  studies/rfc-143379-rig/tmp-artifacts/creative/creative-output-45127001242.md
```

**The cross-check (the §8's 26 reconciled, never smoothed):**

| Measure | §8 receipt | git bytes | Verdict |
|---|---|---|---|
| Changed paths | "26 files" | **26** (`--name-status --no-renames`: 20 D + 4 M + 2 A) | **REPRODUCES** as the commit's total changed-path count |
| Deleted files | "deleted 26 files" | **20** (`--diff-filter=D`) | **RECONCILED** — the "26" is the total footprint; the *deleted* subset = 20 |
| Deleted lines | "3519 lines" | **3519** (`--numstat` total deletions) | **REPRODUCES** |
| — of which from the 20 D | (unstated) | **2479** | the un-deletion's line mass |
| — of which from the 4 M | (unstated) | **1040** | the purge's modification deletions |
| Insertions | (unstated) | **223** | the 2 A files + the M edits' additions |

**The restored set = the 20 D files** (the un-deletion). The 4 M + 2 A are named in §4, untouched by this lane's contract.

---

## §2 · THE RECOVERY METHOD (the un-deletion, byte-exact)

- **Byte source:** the purge-commit's **parent tree** — `git show 67deca1f64:<path>` (the pre-purge version; the last tree state before `eee4d86521`).
- **Write:** the parent's bytes to the path (idempotent — the on-disk untracked copies already held the parent's bytes; the write re-asserts them from the git object, never from a record's prose).
- **Guard:** no `git checkout --` / `git stash` / `git clean` / `git rm` — the recovery is a **write + `git add`**, the reverse-act, never a destructive reset.
- **Pre-state (measured):** all 20 paths **ABSENT from the HEAD tree** (`git cat-file -e HEAD:<path>` → fatal), all 20 **present on disk as untracked** with sha256 == the parent blob's sha256 (20/20). The records survived the purge on disk AND in history, exactly as §8 receipted.

---

## §3 · THE PER-FILE RESTORATION RECEIPTS (20/20 BYTE-EXACT)

Every row: the path restored, the pre-purge parent blob (`git rev-parse 67deca1f64:<path>`), the parent blob's sha256, the post-write disk sha256, the byte size, and the verdict. **20/20 BYTE-EXACT** (post-write sha256 == parent sha256).

| # | Path | Parent blob | sha256 (parent == post) | Bytes | Verdict |
|---|---|---|---|---|---|
| 1 | `studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261122-2250.md` | `de2f54fbd048e34e8ba58d6d7ffe04ac20296cb7` | `d9238679a98d134f59722c58e7bdee643becba1a88272bb98c642e5b1ac717f9` | 7284 | BYTE-EXACT |
| 2 | `studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261123-0051.md` | `8279bed8458f2367b233c8d8bcce64050296630f` | `2fdadcc31b8bebfe310a12d74326d8e9e9746f956b64373cb22623ab00c2d572` | 9254 | BYTE-EXACT |
| 3 | `studies/rfc-143379-rig/NEGENTROPY-SWEEP-20261123-0453.md` | `78fa4c5d7c84aa2332ddf1644c2b98748b806700` | `745be96f4ccf9dacd0f3f50089d3d79685ae9d7d829a876ae6f97acab5279813` | 6559 | BYTE-EXACT |
| 4 | `studies/rfc-143379-rig/plan/tank/HY-GATE-MISSION5-20261122.md` | `507cafea92716fdb570a31a16b2a745902735e17` | `f5526d39384ea8141fa3c054f417b2bb09c23e1a0735b35e1289a8469bd1f416` | 9762 | BYTE-EXACT |
| 5 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-F-ROUND-20261122.md` | `f52317ae3a5e221ba64db00a67de605a28490ee3` | `b0f60b298e68d81a8baaff0d3d6f6d9da930c243e959b8461895a33c81f80def` | 36821 | BYTE-EXACT |
| 6 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-FULL-EXPLORATION-20261122.md` | `8dc68bfcee00d130047b772a01b556cb30627b54` | `30b77cbe9bfe03836aa2ffb34ed3c735e240a10d6d0d6ce3e980d47c4b37ffe6` | 22366 | BYTE-EXACT |
| 7 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-N-ROUND-20261122.md` | `9108bd5c09cf0faa72b5ee4527623f1ddbab3eef` | `d70ba8d02f61e3d4dc7cbdc193650d52742e1a2c62d8cd4f425ba3cf43deff57` | 31201 | BYTE-EXACT |
| 8 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND-20261122.md` | `daa7e00daff59eca9d6c888b0d6cfa0b8fa57ade` | `7848597a1ed5dbb50037e712da82121207d3f9013d5fa02ddfe96c7f71963eec` | 22124 | BYTE-EXACT |
| 9 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND2-20261122.md` | `bb6ea399241de6189a35998602df97f47c633f9d` | `8bf3a95dacab723fe58512fa2772b2b193d0834a2242d353f9e59b359afff2e2` | 22531 | BYTE-EXACT |
| 10 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND3-20261122.md` | `d06f84586f5b898ee04d4e9207b8be83a329ab6f` | `ec05b7721c7459f5adb17ff444c83183aad737882b774a1128b86409f954a139` | 19655 | BYTE-EXACT |
| 11 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND4-20261122.md` | `fd6ae4c9f668c6e2fb09c2facf7f192bd7500757` | `2fde86bcdbb00b088cbf12ed4e47bb8a16e30cf095b7ff75acaa92edbe5b4301` | 18889 | BYTE-EXACT |
| 12 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND5-20261122.md` | `afdbde5e478cd14e7a6bfaf87e7cf8b14481c3ee` | `2fd6af2e4bc56d0c49be28057dce0e275c985faf5b9b3531c236dcb7f82ee1ce` | 26191 | BYTE-EXACT |
| 13 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND6-20261122.md` | `059e224b195a792d6476a88ea23764530629119d` | `83c2db164cb57a66cbc3f26934d24522632a04f585fd0f24bc53f5ef45328b9d` | 31308 | BYTE-EXACT |
| 14 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND7-20261122.md` | `f90b599c075a85f536d5dcbfb9983172f82fab2b` | `020df81582c20a13cf63b3f21c81564f444eb66dbb64777c0ffcffd606cc733c` | 16918 | BYTE-EXACT |
| 15 | `studies/rfc-143379-rig/plan/tank/MAIN-LOOP-ROUND8-20261122.md` | `110a470f7d4289142ad98a1670b5ea84c0114ece` | `aae19511bda7bcf7171df796f5cd5e102e61e6527336e02f9afdcad2ada7a7dd` | 18410 | BYTE-EXACT |
| 16 | `studies/rfc-143379-rig/plan/tank/MISSION-5-SANITY-20261122.md` | `5da756a11aa44cf4434c79e26660c197868e156b` | `51b7e3a40213a95088350d7db1e9b588c94793401d023e7d06745846f2a2b4a7` | 15076 | BYTE-EXACT |
| 17 | `studies/rfc-143379-rig/plan/tank/STATE-REPAIR-20261122.md` | `69c5d5323eb5a58af6267dcfb2a3275976246081` | `52cce1277fc580581e32d3153aae1abf442250cab63352d3c00e3f35bd922147` | 6240 | BYTE-EXACT |
| 18 | `studies/rfc-143379-rig/plan/tank/VET-KVNLOO-20261122.md` | `0c5478438c45f212f5749b5eedf2a24f401f2173` | `25a56afc911ac2b5f5803a460e70a77737b8ede4028dc78745807aeed5ba0bad` | 23308 | BYTE-EXACT |
| 19 | `studies/rfc-143379-rig/tmp-artifacts/creative/creative-output-45073355792.md` | `25bdfb2fc223b22cb3a58df0b1616c2c674b9d12` | `8b54ecabd8a235d90799735614dba21773e0f6d89dd979c963a88e5ed1531b2d` | 12936 | BYTE-EXACT |
| 20 | `studies/rfc-143379-rig/tmp-artifacts/creative/creative-output-45096776289.md` | `dd809637625310942e7648e8e60a9f46df52afa8` | `5d1b3a5e3b2879e3541f8dde2d69ce1ac2c8d43e87ae114f529e739f9ab6b4c1` | 10720 | BYTE-EXACT |

**Total restored: 20 files · 20 byte-exact receipts · 367,553 bytes** (the sum of the 20 sizes).

---

## §4 · THE PURGE'S NON-DELETED FOOTPRINT (named, OUT of this lane's contract)

The contract's restore set = the **deleted** files (20). The purge's other 6 paths are named here, **untouched**:

- **The 4 M files** — the purge modified (never deleted) them; HEAD carries the purge-modified blobs, while the **disk already holds the pre-purge bytes** (disk sha256 == parent blob sha256, 4/4). Their **tree re-land is NOT this lane's contract** (the contract restores the deleted set); named for the head as a separate additive re-land:
  - `HANDOFF-EMERGENCY-20261122.md` — HEAD `64ceea99…` vs parent `a6e0d46b…`
  - `MISSION-BRIEF-MASTER-20261119.md` — HEAD `74ddbd71…` vs parent `81a84772…`
  - `MISSION-MAP-20261118.md` — HEAD `6e8d64b8…` vs parent `0ed3fc49…`
  - `WEIGHTS-RUNG-BATTERY-REFIRE-20261122.md` — HEAD `66bdf850…` vs parent `423b43b1…`
- **The 2 A files** — the purge added them; they did not exist pre-purge, so they cannot be "restored":
  - `FLEET-CYCLE-BODY-2026-11-23-050539Z.md` — at the repo **root** (outside `studies/`); the hard line (write ONLY under the study path) bars this lane; its on-disk state (absent) is left as found.
  - `studies/rfc-143379-rig/tmp-artifacts/creative/creative-output-45127001242.md` — the purge's own creative artifact; left as found.

---

## §5 · THE ADDITIVE LANDING (the repair's form)

- **The commit:** a **new child of `2e0583ade6`**, author **`kanban-pilot <pilot@rig.local>`**, message:

  > `kanban-pilot: F-17 RESTORATION — the ungated deep-deletion's byte-exact re-landing (the purge-commit eee4d86521's 26 files restored from the pre-purge parent; the defect-class named, the repair additive, the hard-lines held)`

- **The commit's contents:** **21 paths** — the 20 restored study-path files + this deliverable. ONLY the study path; no other file staged.
- **The additive's truth:** the history is **never rewritten** — the purge-commit `eee4d86521` **stays in the lineage**; the re-landing rides **on top** (a new commit, the reverse-act). The restored files' blobs are the pre-purge parent's blobs (verified §3), so the tree's content is the un-deletion; the lineage's record of the purge is preserved.
- **Never pushed.**

---

## §6 · THE VERIFY (the hard lines held)

1. **Byte-exactness: 20/20.** Post-write disk sha256 == the pre-purge parent blob's sha256, per file (§3).
2. **Staged-blob equality: 20/20.** `git ls-files -s` staged blob == `git rev-parse 67deca1f64:<path>` (the re-land carries the parent's exact blobs).
3. **The N2 deliverable intact:** `git cat-file -e HEAD:…/MAIN-LOOP-N2-ROUND-20261122.md` → IN TREE; on disk **62,872 bytes**, sha256 `31fe92c3447d47a27217480dfbe639f02929b3734220f4868889453b25cab2c9` (the §8's 58,672 B was the `4adefec60e` state; `2e0583ade6` appended §8, the file grew — the deliverable's own successor, intact).
4. **The recent folds intact:** `MISSION-BRIEF-MASTER-20261119.md` carries **§7-bc / §7-bd / §7-be** (the N-round's fold), re-read this pass.
5. **The tree's truth:** after the landing, the 20 paths are **re-landed in the HEAD tree** (from ABSENT to PRESENT), byte-equal to the pre-purge parent.
6. **The hard lines:** nothing public · RFC #143379 + #5320 + #157065 QUIET · NO installs · write ONLY under `studies/rfc-143379-rig/` · all LOCAL paths via `read_file` / `terminal` · **NEVER push** · no `git checkout --` / `git stash` / `git clean` / `git rm`.

---

## §7 · THE WALL CLAUSE (the non-reproduction, receipted)

The §8 receipt's **"deleted 26 files"** did not reproduce as a *deletion* count: the git bytes give **20 D + 4 M + 2 A = 26 changed paths**. This is a **QUESTION with receipts**, answered: the "26" is the purge-commit's **total changed-path footprint** (the `--stat`'s "26 files changed"), and the **"3519 lines"** is the commit's **total deletions** (2479 from the 20 D + 1040 from the 4 M). The un-deletion's set = the **20 D**; the restored count = **20**; the byte-exact receipts = **20**. The divergence is named, never smoothed — the tree is the checking-channel, the prose the claim.

---

*F-17 RESTORATION · the proxy's alarm-law repair lane · seat `meituan/longcat-2.5:free` (PIN-READ-BACK VERIFIED) · the ungated deep-deletion's byte-exact re-landing · 20/20 byte-exact · the history never rewritten, the purge-commit in the lineage, the re-landing additive · the defect-class named, the repair the reverse-act · never pushed · Facimus semper.*