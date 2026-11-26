# THE-COMPLETENESS-CHECK — hy4 (copycat lane)

**Seat:** tencent/hy4-flash:free · **Lane:** copycat · **Date:** 2026-11-26
**Subject:** completeness assurance over the compiled four-part RFC #143379 comment, 22:30 EST → present.
**Artifact:** `studies/rfc-143379-rig/THE-COMPLETENESS-CHECK-hy4-SEC.md`

---

## 0. Scope, method, and the wall clause

**What I checked.** The compiled four-part comment against (a) the period's documented work, (b) the operator's 22:30→present steers, and (c) the NousResearch + security material the operator named as a dropped item.

**The compiled four (in the comment's order), as identified in the brief:**
1. **THE REPLY-CORE** — his condition accepted, `268bb091` reproduced, the C4 append validated, both doors, the default named. (`RFC-REPLY-ALL-FINDINGS-20261126.md` + `REPLY-KVNLOO-SBI-20261126.md`.)
2. **THE EMPIRICAL BLOCK** — the C4 triangle, the condition-matrix verdicts, the kit's byte-trust.
3. **THE KIT** — its pieces + the practice guides, as links.
4. **THE TRINITY** — the three-minds spec, standalone. (`THE-THREE-MINDS-20261126.md`.)

The gist's preview copy is `RFC-COMMENT-COMPILED-20261126.md`, byte-identified `39c08a96`.

**Verdict vocabulary.** `PRESENT` (content or link) · `MISSING-LOAD-BEARING` (absent and material for kvnloo/the maintainers — severity + placement named) · `CORRECTLY-INTERNAL` (absent by design — fleet machinery, pair process, storm detail) · `QUESTION` (unverifiable — never a guess).

**Wall-clause / read-gate note.** During the analysis phase the read-tools and terminal content-reads were gated (write-window open). Verdicts on the *contents* of the compiled four are therefore taken from the brief's itemisation of those four parts, which is the authoritative description supplied with the mission. Where a verdict depends on bytes I could not independently inspect, I say so explicitly and attach `QUESTION`/`VERIFY` rather than assert. Nothing in this file edits the comment; these are suggestions only, and nothing posts without the operator's word.

---

## 1. Period's documented work — per-item verdicts

| # | Documented item | Verdict | Citation / note |
|---|---|---|---|
| 1.1 | **C4 receipts** — gate-replace `SILENT-OVERWRITE` · gate-append `BOTH-SURVIVE` · fix-pin §-append (`C4-RECEIPTS-20261126.json` + `c4_doc_probe.py`) | **PRESENT** | The C4 triangle rides in part 2 (empirical block); the C4 append validation rides in part 1 (reply-core); `c4_doc_probe.py` rides in part 3 (the kit) as a link. |
| 1.2 | **Condition-matrix verdicts**, C1–C5 per-condition (`THE-CONDITION-MATRIX-NOTES`) | **PRESENT** | Named explicitly as part 2's "condition-matrix verdicts." |
| 1.3 | **Kit byte-trust** — bare-environment cold run (`PROBE_REPO=/nonexistent`, `/tmp/kitto`), envelope + `3ff6aee4` identical | **PRESENT** | Named explicitly as part 2's "kit's byte-trust." The `3ff6aee4` hash is the receipt; verify it renders as a link in the gist copy (see §4 `QUESTION`). |
| 1.4 | **Parity 14/14** (gist vs drop canonicals — mirror-drift close) | **CORRECTLY-INTERNAL** | Pair's canonical-verification machinery; not a claim for kvnloo. It is the *proof of the preview's bytes*, not part of the receiver's argument. Stays out by design. |
| 1.5 | **Twins' post-landing verification** (solar: gist byte-parity + live-read items; hy4: skeleton) | **CORRECTLY-INTERNAL** | Pair process / post-landing QA. No receiver value. Stays out. |
| 1.6 | **Findings-treatment** (`FINDINGS-TREATMENT-20261126.md` — seven failure classes, 5-whys, cures) | **CORRECTLY-INTERNAL** *(with one `QUESTION`)* | Methodology of *how* the findings were processed — internal. **QUESTION:** if any of its cures matured into a shipped kit instrument, that instrument belongs in part 3 as a link; the treatment write-up itself does not. |
| 1.7 | **Storm's close** (fleet-determinism mechanism-wise closure; Windows leg's parked architecture-block) | **CORRECTLY-INTERNAL** | Fleet machinery + a parked (unshipped) leg. Explicitly out of the comment by design. |
| 1.8 | **Earlier thread-event: kvnloo's own reply** (anchor-gate condition, lock-order, his run-table) | **PRESENT** (as context) | The reply-core *is* the answer to his condition — "his condition accepted," "both doors," "the default named" are the steelman-first engagement with his anchor-gate condition and run-table. It is the receiver's own words already on the thread; re-quoting would breach the "receipts as links, not quotes" steer. No action. |

**Section-1 result:** every documented work item that is load-bearing for the receiver is present in the four; every absent item is internal machinery/process/parked work and correctly stays out. No load-bearing omission in the period's documented work.

---

## 2. The operator's named omission — THE SECURITY-PAGE READ (11-26)

This is the cold read that "made the operator pause." Checked item by item. The four parts, as itemised in the brief, contain **no** security-page material: part 1 is the reply-core, part 2 the empirical block, part 3 the kit links, part 4 the trinity. So each sub-item below is assessed as **absent from the four** and then verdicts load-bearing vs internal.

### 2.1 Published HIGH advisory `GHSA-p22p-9ph6-gmrh`
- **Verdict: MISSING-LOAD-BEARING. Severity: HIGH.**
- **Why load-bearing:** it is a *published HIGH* advisory in the very repo under discussion (`NousResearch/hermes-agent/security`), published 11-19 — one week before this read — and it is the terminal-backend **env-file class, the sibling of the credential-scoping section** the RFC engages. A live, repo-local, current HIGH advisory adjacent to the exact section is decisive material for kvnloo/the maintainers; its absence is not neutral.
- **Placement:** part 1 (THE REPLY-CORE), as a **linked receipt** alongside the credential-scoping discussion / triage framing — link only, per the "receipts as links, not quotes" steer. NOT a quote block.

### 2.2 Policy doctrine — "The only security boundary against an adversarial LLM is the operating system. Nothing inside the agent process constitutes containment — not the approval gate, not output redaction, not any pattern scanner, not any tool allowlist."
- **Verdict: MISSING-LOAD-BEARING. Severity: HIGH.**
- **Why load-bearing:** the repo's own published policy explicitly denies that in-process approval gates / redaction / scanners / allowlists are containment. **Conditional (wall clause):** this is load-bearing *if* the four parts advance any in-process control as a security boundary — which the "both doors," "default named," and "type/security" framing make plausible but which I could not byte-verify during the gated phase (`QUESTION`, verify against `39c08a96`). If the comment makes no such security claim, the doctrine drops to internal context. On the balance of the RFC's own security framing, it belongs in front of the receiver.
- **Placement:** part 1, as a **link** to the security page with at most the single doctrine line surfaced; or a one-line pointer in the part-2 framing link. Link-first, quote-minimal.

### 2.3 §3 welcome-line — "limits of an in-process heuristic this policy does not treat as a boundary… welcome as regular issues or PRs"
- **Verdict: MISSING-LOAD-BEARING (secondary). Severity: MEDIUM.**
- **Why:** it is the textual support for 2.2's doctrine and tells maintainers how such findings are actually triaged (regular issues/PRs, not security boundaries). Load-bearing only as the corroborating anchor for 2.2/2.4; not standalone.
- **Placement:** ride the same security-page link as 2.2/2.4; no separate block.

### 2.4 Type/security-triaging framing (RFC's own label + the advisory's currency)
- **Verdict: MISSING-LOAD-BEARING. Severity: MEDIUM–HIGH.**
- **Why:** the RFC labels itself type/security while a HIGH advisory in the same repo is one week old — the triage classification is timely and material to how maintainers route the issue. It is the bridge that makes 2.1 relevant to *this* RFC rather than generic background.
- **Placement:** part 1 reply-core, one linked clause tying the security label to the live advisory.

**Security-read summary:** the security read is **not** correctly-internal. Its four sub-items are MISSING-LOAD-BEARING, led by the HIGH advisory link and the OS-boundary doctrine (both HIGH). The operator's "you dropped all that nous research security stuff" is substantiated: the security-read's findings deserve an explicit verdict (this file) and, as suggestions, linked receipts in the reply-core. All four carry a `QUESTION` on exact placement pending byte-verification of `39c08a96` against the gist copy (see §4).

---

## 3. The NousResearch research trail — per-item verdicts

| # | Item | Verdict | Reasoning / placement |
|---|---|---|---|
| 3.1 | **Five-paper dive set** (SJC 83% · LOHA/ACD 20.4/15.6/15.1 · NoLiMa 11-of-13@32K · the Cliff 53/10+96) | **CORRECTLY-INTERNAL** *(except GovDecay, split out at 3.2)* | Broad literature diving is the fleet's/pair's research lens; dumping five papers into a maintainer reply is noise, not a receipt. Stays out by design. |
| 3.2 | **Governance Decay ↔ pin-mechanism field-claim** (GovDecay 43%/1% + the carried-verbatim treatment) | **MISSING-LOAD-BEARING. Severity: MEDIUM.** | This one connects directly to the **fix-pin §-append** (a C4 receipt in the reply-core). If the pin field-claim rides in the comment, the 43%/1% evidence is its supporting receipt and should ride with it as a **link**. **QUESTION:** verify whether the field-claim/verbatim treatment is already linked in part 1 or 2; if it is, this collapses to PRESENT. Placement if absent: part 2 empirical block, linked. |
| 3.3 | **Three field-invites** (Yash + the Cliff authors + the wave's invitations — "LIVE on the RFC already") | **CORRECTLY-INTERNAL / already-on-thread** | They are live on the RFC already; re-including them in the compiled preview is redundant. No receiver value added. Stays out by design. |

**Section-3 result:** the research trail is correctly internal *as a set*; the single load-bearing thread — GovDecay 43%/1% ↔ the pin field-claim — is a candidate MISSING-LOAD-BEARING receipt, flagged `QUESTION` for byte-verification.

---

## 4. Register / steer cross-check (the form, not the content)

- **Four things, none dropped:** reply-core · empirical block · kit · trinity are all present as parts 1–4. The trinity rides as standalone part 4, satisfying "operator must SEE it before deciding its place" and "per the four things instruction." **PRESENT.**
- **SBI register** (one person, plain prose, steelman first, one ask in one breath): the reply-core is "his condition accepted" (steelman first) — consistent on the brief's account. Byte-level register check = `QUESTION` (gated read).
- **Receipts as links, not quotes; kit instruments as links with nothing dangled:** the security material and the GovDecay receipt, if added, must enter as gist-rendered links, never quotes — this is the mechanism by which the §2/§3 omissions should be remedied.
- **Cherishment + fixed sign-off:** not independently verifiable during the gated phase — `QUESTION`; no change suggested.

---

## 5. Final line

**Named omissions — the four are NOT yet complete for the receiver:**

1. **The security-page read (all four sub-items)**

   — HIGH advisory `GHSA-p22p-9ph6-gmrh` link (HIGH), the OS-boundary doctrine link (HIGH), the §3 welcome-line anchor (MEDIUM), and the type/security-triage framing (MEDIUM–HIGH) — all currently absent from the four, all load-bearing for kvnloo/the maintainers, all to ride as **linked receipts in the reply-core (part 1)**, with byte-placement `QUESTION` against gist `39c08a96`.
2. **The GovDecay 43%/1% ↔ pin-mechanism field-claim link (MEDIUM)** — absent, load-bearing as the pin receipt, to ride in the empirical block (part 2) *if* not already linked (`QUESTION`).

Everything else in the period's documented work is `PRESENT` or `CORRECTLY-INTERNAL`. These are suggestions, not edits; nothing posts without the operator's word.
