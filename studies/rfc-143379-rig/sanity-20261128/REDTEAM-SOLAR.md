# REDTEAM-SOLAR — flipped-codebase adversarial pass

## 1. Base line (the flipped base)

This round reads the **opposite** codebase as the primary base. The reply/child claims are
evaluated against the flipped tree; the fix tree (`code/store-6609dac.py`, sha256
`a43818a6…1586a`) is cited **only for contrast**, never as the base.

- **`code/store-main-7c57dbf.py`** — main's read-less tree. sha256 `502c85f1…3032`. Expected
  pins: `MAIN_PIN=7c57dbf`, `HASH=502c85f1`.
- **`code/store-installed.py`** — the installed spec-2 tree. sha256 `260897d6…8eb34`. Expected
  pins: `INSTALLED_PIN=…`, `HASH=260897d6`.
- **Fix tree (contrast only):** `code/store-6609dac.py`, sha256 `a43818a6…1586a`.

The key behavioral fact of the flipped base: the main/installed trees are **read-less** —
they contain no `read()`/`GET`/`cmd-history read`, and therefore the read-kit's "one-command
read" story **cannot** land on those trees. Any reply row that asserts a `read()` behavior on
the flipped base is overclaiming by construction.

## 2. Strikes table

| Strike | Severity | Claim (reply/child) | Opposite tree's evidence | Disposition |
|---|---|---|---|---|
| **S1 — read-less main exposed** | Critical | The reply says the reply-path works by reading the reply/read-write store, i.e. the flip does not break it. | `code/store-main-7c57dbf.py` (sha256 `502c85f1…3032`) has no read implementation; the read-kit's "one-command read" cannot be executed there. | **Rejected on base.** The reply cannot cite the flip's tree as evidence of work without an explicit read-layer activation condition. |
| **S2 — spec-2 installed read is a different contract** | Critical | The reply presents the installed tree as a drop-in for the flip's read behavior. | `code/store-installed.py` (sha256 `260897d6…8eb34`) is spec-2: its read contract is dated/stale against the current protocol step ordering. | **Rejected as contrast.** The reply must isolate the installed tree's behavior rather than imply parity with the fix tree. |
| **S3 — MAP row overclaim: echo sites** | Material | "Echo sites" detected on the flip tree. | Against `store-main-7c57dbf.py` and `store-installed.py` (read-less), the read-side echo cannot be observed; only the write/error path is present. | **Rejected on evidence.** The echo claim requires a read channel; the flipped base lacks one. |
| **S4 — MAP row overclaim: structural check** | Material | Structural check passes on the flipped base. | The structural checker only inspects the store's write/error surface; on a read-less tree it cannot distinguish a missing read from a present one. | **Rejected on evidence.** Structural pass is necessary, not sufficient, on the opposite tree. |
| **S5 — MAP row overclaim: read-invoked counter** | Material | "Read-invoked counter" shows X on the flip. | A read-invoked counter increments only when a read path runs; on the read-less main/installed trees there is no counter event. | **Rejected on evidence.** The counter value is unverifiable and possibly zero. |
| **S6 — bookkeeper omission: reply-vs-opposite set gap** | Material | The reply's affected set is complete. | The opposite tree exposes a set (no read layer, no thread-register, no spec-2 parity) that the reply's ledger omits. | **Included in ledger.** The reply must add the read-layer absence to its affected set. |
| **S7 — eigen-axis drift under flip** | Material | The axis (e.g. read gating) should be invariant. | The flip changes the store from read-capable to read-less; the axis drifts from "read-invoked" to "read-absent". | **Dropped.** Record the drift as a version shift, not a stable axis. |
| **S8 — two-N window / retention latch / tiny-aged-fact** | Minor | Reply claims compaction of old entries in a two-N window. | The reply is silent on how `retention_latch`, `two_N`, and `tiny_aged_fact` are computed on a read-less tree. | **Silence noted.** The reply must supply the algorithm or withdraw the compaction claim. |
| **S9 — read-kits claim verification** | Critical | The kit's one-command read + receipt + a9c65dc4 combined store claim. | Against the flipped base, the a9c65dc4 combined store is not the #141876 file; the receipt and one-command claim have no read surface to write to. | **Rejected on base.** The kit claims must be re-run on the fix tree (read-capable) to be validated. |
| **S10 — K-recency probe vs protocol steps** | Material | Reply's gate statement matches protocol steps. | The flipped base's step ordering (read-less) makes the gate statement unfalsifiable: the probe would read nothing. | **Rejected as stated.** The reply must show the probe actually executes a read on the base. |

## 3. Strongest counter-case

The strongest single argument that would sink the reply/child, **if true**:

> **The reply's core claim is that the store works on the flipped base. But the flipped base
> (`store-main-7c57dbf.py`, sha256 `502c85f1…3032`; `store-installed.py`, sha256
> `260897d6…8eb34`) is a read-less tree: it exposes no read path (no GET/history read, no
> thread-register read, no spec-2 read gate). The reply's instrument rows (MAP echo/structural/
> read-invoked, read-kit receipt, K-recency probe) all assert a `read()` behavior that cannot
> execute on the evidence. If the reply's numbers, receipts, and gate statement were produced on
> this base, they are false or unsupported; if produced elsewhere, the reply fails to say so.

**Evidence:** `00-KIT-README.md`, `01-THE-REPLY.md`, `02-THE-CHILD.md`, `03-KIT-README.md`,
`04-PARTNER-COMMENTS.md`, `05-VERIFICATION.md`, `06-MATRIX.md`, `07-INSTRUMENTS.md`, plus
`code/store-main-7c57dbf.py` (sha256 `502c85f1…3032`) and `code/store-installed.py`
(sha256 `260897d6…8eb34`).

## 4. Instrument attacks

| Instrument | How used | What it surfaced against the flipped base | What broke | The falsifier the reply omits or states |
|---|---|---|---|---|
| **MAP matrix** (attack grid) | Re-based every reply row on main-7c57dbf and installed-260897d6. | Rows S3–S5 fail: echo sites, structural check, read-invoked counter all require a read path that the flipped base lacks. | The attack grid cannot discriminate read style on a read-less tree. | Reply states a read path exists; the tree shows none. |
| **Bookkeeper** (miss-finder) | Compare reply's affected set with what the opposite tree exposes. | The reply omits: read-layer absence, thread-register non-visibility, spec-2 parity failure. | The ledger is incomplete for the flip. | The reply's ledger omits the read-layer absence. |
| **Eigen keeper** (drift-finder) | Track axes invariant across reply versions under the flip. | The axis that drifts is the read contract: `read-` capability / spec-2 parity / `two-N` computation. | The axis drifts under the flip; it cannot serve as a stable invariant. | The reply assumes the axis is invariant; the flip breaks it. |
| **Two-N window + retention latch + tiny-aged-fact** (compaction lenses) | Apply each lens to the reply's compaction claim. | The reply is silent on how `retention_latch`, `two_N`, `tiny_aged_fact` are computed on a read-less tree. | The compaction claim is unverifiable; it may overclaim old-entry eviction. | The reply must say how the three numbers are computed. |
| **Read kit** (test case) | Assess the kit's own claims (a9c65dc4 combined store vs #141876 file, receipt, one-command) against the flipped base. | The kit's claims assume a read-capable store; the flipped base has none, so the receipt has no write surface and the a9c65dc4 vs #141876 comparison is unsupported. | The kit's one-command claim cannot be executed head-side on the opposite tree. | The kit is validated only on the fix tree (read-capable). |
| **K-recency probe** (protocol attack) | Check the reply's gate statement against the protocol steps on the flipped base. | The gate statement is unfalsifiable on the flip: the probe would read nothing. | The probe's read-side gate cannot be asserted. | The reply must show the probe executes a real read on the base. |

*Execution note:* the kit's execution is head-side (source/receipt-based); it cannot be run
against `store-main-7c57dbf.py` or `store-installed.py` because those trees lack the read
layer needed to produce a receipt. This is a limit of the red team, not of the kits.

## 5. What would change the verdict

If the reply/child explicitly ties each of its core claims (read-kit receipt, MAP counter
values, gate statement, compaction numbers) to the **fix tree** (`store-6609dac.py`,
sha256 `a43818a6…1586a`) or to an explicitly activated read layer on the flipped base, the
verdicts for S1–S5 and S9/S10 would need to be reopened. Absent that, the reply stays
**rejected on base**.

## 6. Red team's own limits

- Could not execute the read kit head-side on the flipped base (no read surface).
- Could not run a K-recency probe against the read-less trees (nothing to read).
- Could not verify the reply's internal numbers or receipts beyond the stated records.
- Could not run the reply's code against a live store; the analysis is source- and receipt-based.
- No network; no public posting; terminal limited to git-only operations.
