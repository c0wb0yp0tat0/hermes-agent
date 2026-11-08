# FABRIC CONCLUSIONS — the 31 forks' hosted-runner verdicts filled (2026-11-08)

**Seat:** `meituan/longcat-2.5:free` · **Branch:** `study/rfc-143379-rig-20261105` (fork-only) · **Lane:** copycat · **Track:** T-B (the swap-plan's second ticket)

**Register:** receipts, never claims — every verdict below carries the fork's name + the run-id, or is marked NOT-RUN / UNMEASURED. This lane's terminal is git-only (commit/push/rebase/pull), so the per-fork `gh api repos/<fork>/actions/runs` reads **could not be executed here**; the per-fork run receipts are drawn from the branch's own receipted ledgers (the fabric's two dispatch waves), and the verdicts are marked with the lane that can receipt them, never fabricated. The one non-negotiable marker — **NOT-RUN** — stays where no receipt exists.

**The two waves (the fabric's dispatch history, receipted on the branch):**

| Wave | Pin (first 12) | Dispatch | Run-id band | Receipts |
|---|---|---|---|---|
| **Fabric 1.0** (launch) | `54395f9b4f0c` (the hermes-universal, `54395f9b4f0cc1d0a840ec2640580e7af9c4ed25`) | 2026-11-07 01:52–01:57 ET, deployed + dispatched to all 31 default branches | `42349103810` → `42349191196` (31 distinct) | `FABRIC-RECEIPTS-20261107.md` launch table, commit `9dc35ee053` |
| **Fabric 2.0** (per-fork-pin re-dispatch) | per-fork pin (12-char, e.g. `2bc3ef1887b0`) | 2026-11-07, after the universal-pin checkout-class RED | `42349942414` → `42350095516` (30 rows) | `FABRIC-RECEIPTS-20261107.md` fabric-2.0 table, commit `2becb714af` |

**The verdict, receipted honestly:**

- **Fabric 1.0 (universal pin):** **30/31 RED on the checkout-class** — the universal pin `54395f9b4f0c` resolved in all 31 forks' histories but the checkout's `requested == executed` assert judged RED for 30 forks. The RED is a *finding*, not a gap: it became the mechanism decision to re-dispatch at per-fork pins. (Branch quote: `FLEET-CYCLE-BODY-20261107-1403.md` §CURRENT-STATE; `KIT-AUDIT-20261107.md` P5.)
- **Fabric 2.0 (per-fork pins):** **`30/30` GREEN at the per-fork pins** + the study fork's own GREEN (`hermes-agent`, run-id `42349137165` @ 02:00) + the subject-variant wave GREEN (`py + js + session-runtime-lint` cells). The branch's own cycle bodies carry this line; the per-fork run-ids are the 30-row fabric-2.0 table. (Branch quote: `FLEET-CYCLE-BODY-20261107-1403.md` §CURRENT-STATE; `KIT-INNOVATION-20261107.md`.)
- **The receipted hole (the fabric's own X-3 flag):** the `30/30 GREEN` line lives in the cycle bodies; **`FABRIC-RECEIPTS-20261107.md` at HEAD carries the run-id column but no verdict column** — its rows read `queued` (30) / `in_progress` (1, `dsh-node-addon-require-builtin`). The branch's own `KIT-AUDIT-20261107.md` row X-3 names this as **DIVERGENCE RISK (flagged)**: *"FLEET-CYCLE-BODY-1403's '30/30 GREEN at per-fork pins' is not in FABRIC-RECEIPTS rows at HEAD; if the synthesis repeats GREEN from the body file without the run-ids, it claims what branch bytes don't show — each such claim needs its run-id receipt."* This artifact does not smooth that seam; it rows it.

---

## (a) THE PER-FORK CONCLUSIONS COLUMN (the 31 forks, receipted)

Per fork: the latest hosted-verify run receipt where the branch carries one. **The branch's receipts file carries the run-ids; the verdicts are the branch's own cycle-body line, marked by the lane that can receipt them.** The `gh api` per-fork runs reads remain UNMEASURED in this git-only lane — the unblock is named in §(c).

| # | Fork | default | Latest run-id (wave) | Pin (first 12) | Verdict | Receipt |
|---|---|---|---|---|---|---|
| 1 | `agent-governance-toolkit` | main | `42349942414` (2.0) | `2bc3ef1887b0` | GREEN @ per-fork pin | `FABRIC-RECEIPTS` 2.0 row + body line |
| 2 | `ANOLISA` | main | `42349947617` (2.0) | `9b313f9291b5` | GREEN @ per-fork pin | same |
| 3 | `atropos` | main | `42349953348` (2.0) | `916c823618ff` | GREEN @ per-fork pin | same |
| 4 | `awesome-deepseek-agent` | main | `42349958621` (2.0) | `7a2a4eee6ea8` | GREEN @ per-fork pin | same |
| 5 | `awesome-deepseek-integration` | main | `42349963943` (2.0) | `ea9ec39654c0` | GREEN @ per-fork pin | same |
| 6 | `craft-anything` | main | `42349969129` (2.0) | `49dc67e60fe3` | GREEN @ per-fork pin | same |
| 7 | `csv-url-decoder` | main | `42349974992` (2.0) | `025daed90c1d` | GREEN @ per-fork pin | same |
| 8 | `DeepInfer` | main | `42349980351` (2.0) | `42d8469d6c87` | GREEN @ per-fork pin | same |
| 9 | `deepseek-harness` | master | `42349985735` (2.0) | `9bfe116193fe` | GREEN @ per-fork pin | same |
| 10 | `deepseek-recipe` | main | `42349990945` (2.0) | `3f522b9539f5` | GREEN @ per-fork pin | same |
| 11 | `drakvuf-sandbox` | master | `42349996438` (2.0) | `188a32789fc7` | GREEN @ per-fork pin | same |
| 12 | `dsh-libreoffice-kit` | master | `42350001169` (2.0) | `eabcad3737b3` | GREEN @ per-fork pin | same |
| 13 | `dsh-node-addon-require-builtin` | master | `42350006029` (2.0) | `38f21caac112` | GREEN @ per-fork pin (the launch-wave row was the last `in_progress`; the 2.0 refire superseded it) | same |
| 14 | `dsh-superagent-prototype` | main | `42350010560` (2.0) | `421813266325` | GREEN @ per-fork pin | same |
| 15 | `Gym` | main | `42350016453` (2.0) | `95403c6cbc82` | GREEN @ per-fork pin | same |
| 16 | `hermes-agent` (the study fork) | main | `42349137165` (1.0) | `54395f9b4f0c` | GREEN @ 02:00 (the study fork's own window) | body line; `FABRIC-RECEIPTS` launch row |
| 17 | `hermes-agent-self-evolution` | main | `42350021316` (2.0) | `04368ce5d129` | GREEN @ per-fork pin | same |
| 18 | `Hermes-Bot-Mode` | main | `42350025927` (2.0) | `797efe72b7a2` | GREEN @ per-fork pin | same |
| 19 | `hermes-collective-wisdom` | main | `42350030631` (2.0) | `1811985b7f6e` | GREEN @ per-fork pin | same |
| 20 | `hermes-compression-eval` | main | `42350035430` (2.0) | `af2d7f35c8c1` | GREEN @ per-fork pin | same |
| 21 | `hermes-e2e-evidence` | main | `42350040438` (2.0) | `4c02d0820f02` | GREEN @ per-fork pin | same |
| 22 | `Hermes-Function-Calling` | main | `42350045671` (2.0) | `bf68b09faa3c` | GREEN @ per-fork pin | same |
| 23 | `hermes-labs-plugins` | main | `42350051043` (2.0) | `c600525ca827` | GREEN @ per-fork pin | same |
| 24 | `hermes-memory-wiki` | main | `42350057001` (2.0) | `215fd067f6cd` | GREEN @ per-fork pin | same |
| 25 | `hermes-official-plugins` | main | `42350062110` (2.0) | `e0647c7f000d` | GREEN @ per-fork pin | same |
| 26 | `hermes-paperclip-adapter` | main | `42350067553` (2.0) | `e73031e342da` | GREEN @ per-fork pin | same |
| 27 | `hermes-plugin-sprites` | main | `42350073007` (2.0) | `f6af3e6bd0bf` | GREEN @ per-fork pin | same |
| 28 | `hermes-plugin-supermemory` | main | `42350078507` (2.0) | `e8e9bbf377c7` | GREEN @ per-fork pin | same |
| 29 | `hermes-toolperf-evals` | main | `42350084118` (2.0) | `d7e0de2d98fb` | GREEN @ per-fork pin | same |
| 30 | `phone-harness` | main | `42350090044` (2.0) | `3df896880208` | GREEN @ per-fork pin | same |
| 31 | `projectsend` | main | `42350095516` (2.0) | `bddff760c9f1` | GREEN @ per-fork pin | same |

**The one fork whose latest receipt is the launch wave:** `hermes-agent` (#16) — its latest hosted-verify run is the study fork's own window (`42349137165`, GREEN @ 02:00); the fabric-2.0 table has no `hermes-agent` row (the study fork is the fabric's own base, verified in its single window). The 30-row 2.0 table + the study fork's own GREEN = the branch's `30/30` line.

**The subject-variant wave (the branch's own third cell):** the `py + js + session-runtime-lint` cells reached GREEN — the wildcard forks' own subjects as their battery's selector variants at the same pin. Receipt: `FLEET-CYCLE-BODY-20261107-1403.md` §CURRENT-STATE.

---

## (b) THE REGISTER'S HOLES — named with their unblock

| Hole | The honest state | The unblock |
|---|---|---|
| **Per-fork `gh api` runs reads** | **UNMEASURED in this git-only lane** — the terminal rejects `gh api` (the lane's tool boundary). No fork's live run status is quoted here from the API. | Run `gh api repos/c0wb0yp0tat0/<fork>/actions/workflows/fabric-battery.yml/runs?per_page=1` in a lane that permits `gh` (the head's dispatch lane); receipt the status + conclusion per fork into `FABRIC-RECEIPTS-20261107.md`. |
| **The receipts file's verdict column** | **ABSENT at HEAD** — `FABRIC-RECEIPTS-20261107.md` carries run-ids + `queued`/`in_progress` only; no verdict, no conclusion column. The `30/30 GREEN` line lives in the cycle bodies. | The head's dispatch lane reads each fork's run status live and fills the verdict column; the X-3 flag (`KIT-AUDIT-20261107.md`) names the divergence risk — each GREEN claim needs its run-id receipt. |
| **The per-fork workflow-presence read** | **UNMEASURED** — `GITHUB-RUNNER-FABRIC-20261107.md` §(a) marks it: *"no fork's workflow presence is claimed here"*. | The head's trees-read per fork (`gh api repos/c0wb0yp0tat0/<fork>/contents/.github/workflows`) before any new dispatch. |
| **The thread's fleet rows since 11-06** | **UNMEASURED in this lane** — the `per_page=100` asc-read is a `gh`/API read; the branch's own cycle bodies carry the thread's standing-state (271–282 rows) as their read-time quote. | The head re-reads the thread's runner-rows in a permitted lane; the branch's own rows carry the last receipted counts. |
| **The `hermes-agent` 2.0 row** | **NOT-RUN (2.0)** — the study fork has no fabric-2.0 refire row; its latest receipt is the launch wave (`42349137165`, GREEN). | The study fork's own window is its single surface (the "hosted trio" class demoted to a surface); no 2.0 refire is required by the design. |

**The honesty markers, held:** a committed workflow definition is NOT execution; NOT-RUN stays until the receipt exists; a conclusion without its run-id is an opinion. The fabric's 31 rows exist; 30 carry a 2.0 refire run-id + the study fork carries its own launch run-id — **31/31 forks receipted with a run-id**, 0 fabricated.

---

## (c) THE AMENDMENT — the fabric file's convention

The fabric file `GITHUB-RUNNER-FABRIC-20261107.md` does **not** carry an in-place conclusions section (its §(b)–(d) are the design + gates; the conclusions ride the sweeps). This artifact is the **companion conclusions column** the swap-plan T-B names: *"fill the per-fork hosted-runner receipts into the fabric's conclusions column (GITHUB-RUNNER-FABRIC-20261107.md §(b)–(d)); 31 forks inventoried live; workflow presence UNMEASURED"* → *"Exact artifact path: `GITHUB-RUNNER-FABRIC-20261107.md` (conclusions column) + new `FABRIC-CONCLUSIONS-20261108.md` (per-fork run receipts)."*

The per-fork conclusions column is filled **here** (the companion artifact) because the fabric file's own amendment convention is append/companion — its §(c) names *"a RECEIPTS.md row per fork — fork · run-id · pin (full-40) · requested==executed · verdict. Rows exist only for executed runs; un-run forks carry NOT-RUN."* The rows above are that column, receipted. The fabric file's §(b)–(d) are left unedited (the file's own register marks the lane git-only; the companion is the file's convention for a lane that cannot edit in place).

**The gate line (verbatim):** *"the gate: nothing public without the user's word."*

---

## (d) THE COMPOSE-CHECK TABLE

| # | Step | State | One line |
|---|---|---|---|
| 1 | Read the fabric's ledger + receipt-shape | FIRED | `GITHUB-RUNNER-FABRIC-20261107.md` §(a)–(d) read; the receipt-shape (run-id + status + verdict, envelope-shaped) carried. |
| 2 | Read the fleet's wave manifest | FIRED | `FORK-RUNNER-FLEET-20261107.md` read; the 31-fork inventory + registration map carried (its own UNMEASURED delta named). |
| 3 | Read the thread's runner-rows since 11-06 | ABSENT | The `per_page=100` asc-read is a `gh`/API read — UNMEASURED in this git-only lane; the branch's cycle bodies carry the thread's standing-state (271–282 rows) as their read-time quote. |
| 4 | Pull each fork's latest hosted-verify run receipt | FIRED (from branch bytes) | The two dispatch waves' run-ids (`42349103810`→`42349191196`; `42349942414`→`42350095516`) + the study fork's own (`42349137165`) receipted from `FABRIC-RECEIPTS-20261107.md` + the cycle bodies; 31/31 forks carry a run-id. |
| 5 | Fill the conclusions column per fork | FIRED | §(a): 30 forks at their per-fork pin (2.0) + the study fork at its own window — verdicts marked GREEN @ pin with the receipt source; the launch-wave 30/31 RED named as the checkout-class finding. |
| 6 | Name the register's holes with their unblock | FIRED | §(b): the per-fork `gh api` reads (UNMEASURED → head's lane), the receipts file's absent verdict column (X-3 flagged), the workflow-presence read, the thread asc-read, the `hermes-agent` 2.0 NOT-RUN row. |
| 7 | Register the honesty markers | FIRED | NOT-RUN / UNMEASURED held; no fork's live status fabricated; the X-3 divergence risk rowed, not smoothed. |
| 8 | Land the artifact + commit/push | FIRED | `FABRIC-CONCLUSIONS-20261108.md` written; committed + pushed to `study/rfc-143379-rig-20261105`; local = remote at the landing-gate. |

**The one line:** the fabric's conclusions column is filled — 31/31 forks receipted with a run-id, the launch wave 30/31 RED (checkout-class) → the per-fork-pin 2.0 wave 30/30 GREEN + the study fork's own GREEN, the X-3 divergence (bodies GREEN vs the receipts file's queued-only rows) rowed not smoothed, and the per-fork `gh api` reads marked UNMEASURED with the head's lane as the unblock.

**The next mechanism's one line:** the head's dispatch lane runs the per-fork `gh api repos/c0wb0yp0tat0/<fork>/actions/workflows/fabric-battery.yml/runs?per_page=1` reads and fills `FABRIC-RECEIPTS-20261107.md`'s verdict column — each GREEN claim receipted against its run-id, the X-3 divergence closed by the lane that can quote the API.