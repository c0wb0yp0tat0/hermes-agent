# REGISTER-LEDGER — the study's register → the RFC #143379 three movements (2026-11-21)

Seat: tencent/hy4-flash:free · Branch: study/rfc-143379-rig-20261105 · RFC quiet · write-window: 8
Class: **register** — receipts, never claims; never smooth. Every row below is *what the study holds, with its receipt*, not a re-assertion of the claim.

## 0. Provenance and read discipline

The register has two legs, read this leg as required:

- **Master's fold (distilled landings):** `studies/rfc-143379-rig/MISSION-BRIEF-MASTER-20261119.md` §7 (§7-a…§7-p). This carries the older rows' substance.
- **Machine-log recent register:** PR `c0wb0yp0tat0/hermes-agent#1` — 1,131 comments (`issues/1.comments = 1131`, state closed, updated 2026-11-21T14:35:48Z), last 60 read via `gh api repos/c0wb0yp0tat0/hermes-agent/issues/1/comments?per_page=60&page=19` (51 comments on that page, 2026-11-20T19:21Z → 2026-11-21T14:32Z). The full 1,100+ thread's classification is LEG-1's class; this leg takes the recent rows only.

Re-derivation note: the recent register is *mostly* cadence/re-grounding envelopes; its substantive rows are the fold-landing envelopes (m1-stamp, l1…l5, a3-wave-convergence, pilot-solved, the FILL-LEG run rows), plus open seams (fill-122 FAILURE, night-close, integration correction, armd-kit). They corroborate the fold rather than add new claims. Where a SHA could not be re-derived inside this leg it is marked `not re-derived this leg` and the receipt is the path/envelope id alone.

## 1. The claim classes (the study's claim-set, by class)

### 1.1 SUBSTRATE

- **S1 — the M1 stamp (PersistGym CERTIFY).** Fold line §7-g: VERDICT CERTIFY — solar full-N 100/arm, A 0.000 / B 1.000 / C 0.990; B−A=100.0 ≥ 20 ∧ B ≥ 0.85·C; judge gate 1.0; ledger `PERSISTGYM-PROBE-LEDGER-20261121-SOLAR-FULL.json` sha `be7fc43e…`. Triangulation: the qwen4-voice's FALSIFY (`bacc436d`, A=B=C=0) is registered as exact-match non-compliance (format class), not the substrate; the compliant voice certifies. The pumped B-view surfaces the persistent fact 100% where the truncated A-view shows 0%. The study's wording: "M1 = the substrate's persistence property, machine-verified." Recent-register receipts: envelopes `20261121-certify-triangulation` (id 7055531330), `20261121-m1-stamp` (id 7055622807), `20261121-m1-stamp-erratum` (id 7055626467). Protocol ancestry folded just above §7-g: P4 `PERSISTGYM-PROBE-20261119.md` (commits `70c1f9edc0` + `5ed4cd5e86`).
- **S2 — the fill GREEN / harbor restored / canary's cause named.** Fold line §7-k: fill run `44868130710` SUCCESS — 7/7, three-wave, JSON-parse gate, full-leg slot; canary `44787964389` root cause NAMED = runner harness class (per-run fixture absent; no upload field), model side reads 0.984 GREEN on `7ad1b08b6d`; retry `44859360354` SUCCESS; "HARBOR RESTORED." Recent-register receipts: FILL-LEG envelopes `44854746984` (id 7055746857), `44868130710` (id 7057539747), `44874772317` (id 7058500488); fill-122 `44892997287` FAILURE at main `7ad1b08b6d` (id 7061690591). Ancestry: P4 dispatch receipts `44619039714` RED / `44745081209` GREEN (run-receipt sha `0129701b…`) / `44750545821` GREEN (sha `f29f7b28…`).

### 1.2 MACHINERY

- **M1 — the A3 wave's convergence.** Fold lines §7-h…§7-n: the suppressor is registered as *not a token-logit artifact* — verbatim, prefix-gated, guide and paraphrase arms all converge (§7-h `a51e50b7be`, baseline brackets; §7-l `773c877bda`, verbatim B1 registration; §7-j citation provenance 7/7, prefix-gated at n5; §7-o read-only sweep `b703bd20d9`). The weights rung is the named next rung and is registered NOT_RUN at n5 (§7-p; pre-registration `OPUS-A3-WEIGHTS-DRYRUN-20261120.md` commit `5e08bcb4b7`, re-prereg `3fef99a4ef`, NOT_RUN commit `406958197b`). Study's fold wording: "converged at the read; weights rung next." Recent-register receipt: envelope `20261121-a3-wave-convergence` (id 7058621937); ancestry envelopes `20261121-l1-b1v3` (7057409061), `20261121-l5-verbatim-wave` (7057586058).
- **M2 — the B′ control.** Fold line §7-p: the one-string free control B′ registered inert at n5, with the n5→n10 validity seam named (the control inherits the same validity question as the C-arm bracket). Relevance here: the control row exists in the register; its n10 extension is not claimed.
- **M3 — the pilot verdict.** Fold line §7-m: PILOT VERDICT = PROOF-OF-CONCEPT; boundary = the judgment layer; pilot `20261121-gray-phase1-full.json` sha `b39f578e…`; 42/42 GREEN, zero violations, no field-report; qwen+hy4 polish = "definitional / dictionary-lookup," not generative; fill-122 → no-go. Recent-register receipt: envelope `20261121-pilot-solved` (id 7058604295).
- **M4 — the verification spine (hermes-rlm family first-hand receipted).** Fold lines §7-i / §7-p: R2's sweep **3/3** on the hermes-rlm family (R2.1 summary.json sha `19f53a37…`; R2.4 scaling branch `c458dd0`; OpenClaw / Claude-GLM-5.1 / Codex corroborations), R3's **1/1 + 5/5** (R3 prefix + the 5/5 row). The spine's function in the register: external disconfirmation receipted first-hand, not adopted as a claim. Recent-register receipts: envelopes `20261121-l2-court-drafts` (7057456632), `20261121-l3-citation-provenance` (7057470726), `20261121-l4-machine-closures` (7057585797). Ancestry: champion readiness §7-f `CHAMPION-ROW-READINESS-20261120.md`.

### 1.3 COURT

- **C1 — the court drafts.** Fold line §7-i: `COURT-DRAFTS-20261121.md` — the R2/R3 verifier drafts that carry the verification spine's first-hand receipts (see M4). Class distinction: the drafts are the *court's* record; the spine is the *machinery* that produced it. Recent-register receipt: envelope `20261121-l2-court-drafts` (7057456632). SHA of the drafts file: not re-derived this leg (path only).

### 1.4 KIT

- **K1 — the kit's method cards.** Path `studies/rfc-143379-rig/KIT-METHOD-CARDS-20261121.md` (present on the study branch; content/SHA not re-derived this leg under the write-gate). The study's method-card layer: the reusable cards that make the above receipts reproducible; carried from §7-e (`8e02a752a3`) into the 11-21 kit work. Recent-register receipt: envelope `20261121-armd-kit` (7062507520).
- **K2 — kit / verification-support receipt cluster (ancestry, folded).** A3 dry-run pre-reg `5e08bcb4b7`; 4-arm build `784dbd8691`+`ed78f78896`; GGUF-floor spec `3d460fee5b` (bias-id 7 INVALID); V2 dry-runs `742c13d679`; P3 `93f8f0fc81`; NM-3 canary R2 `b277e23ed8` (model sha `415501bd…`, 5-shard sha256 `1b72ab1e…`, egress 6,755,531,557 bytes); closing seal `2f3d62206e`; LENS-E `9070c2ae1e`+`8e25b7ecac`. Registered as support receipts, not new claims.

## 2. Mapping table — claim × the RFC's three movements

Movements (from the RFC asks): **R1 = read restored** · **R2 = store re-readable** · **R3 = compaction governed**.
Cell values: `direct answer` / `evidence` / `machinery` / `none`.

| Claim (§) | Receipt (fold line + sha / id) | Class | R1 read restored | R2 store re-readable | R3 compaction governed |
|---|---|---|---|---|---|
| S1 M1 stamp (§7-g) | §7-g · `be7fc43e…` · FALSIFY `bacc436d` · env 7055622807 | substrate | evidence | **direct answer** | none |
| S2 fill GREEN / harbor restored / canary cause (§7-k) | §7-k · run `44868130710` · canary `44787964389` · env 7057539747 | substrate | **machinery** | evidence | none |
| M1 A3 wave convergence (§7-h…n) | §7-h `a51e50b7be`, §7-l `773c877bda`, §7-n `8b34988206`, §7-o `b703bd20d9`, §7-p `406958197b` | machinery | evidence | none | **evidence** |
| M2 B′ control (§7-p) | §7-p · pre-reg `3fef99a4ef` · NOT_RUN `406958197b` | machinery | none | none | **evidence** |
| M3 pilot verdict (§7-m) | §7-m · `b39f578e…` · env 7058604295 | machinery | none | evidence | **evidence** |
| M4 verification spine (§7-i/§7-p) | §7-i · R2.1 sha `19f53a37…` · R2.4 `c458dd0` · R2 3/3 · R3 1/1+5/5 | machinery | **evidence** | evidence | evidence |
| C1 court drafts (§7-i) | §7-i · `COURT-DRAFTS-20261121.md` · env 7057456632 (sha not re-derived) | court | evidence | evidence | **evidence** |
| K1 method cards | `KIT-METHOD-CARDS-20261121.md` · env 7062507520 (sha not re-derived) | kit | machinery | machinery | machinery |
| K2 support-receipt cluster | §7-a…e · `5e08bcb4b7`, `b277e23ed8`, `93f8f0fc81`, `2f3d62206e`, … | kit | machinery | machinery | machinery |

**Table discipline / non-smoothing:** no row is blank-filled to look complete. S1 answers R2 and is only *evidence* for R1 (the persistence property certifies under a compliant reader; it does not by itself restore a broken read path). S2 is *machinery* for R1 (the tooling channel restored) but explicitly does not certify any substrate property. M1/M2/M3 are *evidence* for R3, not a governed-compaction answer: the judgment layer is the registered boundary, and the weights rung is NOT_RUN. K1/K2 are *machinery* throughout — the study holds the receipts, not the RFC's deployment. "none" means no registered relevance, not a refutation.

## 3. Recent register (last 60 thread comments — the machine-log's current rows)

Read as the fold's live index, not as new claims:

- `20261121-certify-triangulation` (7055531330) · `20261121-m1-stamp` (7055622807) · `20261121-m1-stamp-erratum` (7055626467) — S1 landed and corrected on the wire same-minute.
- `20261121-batch-truth` (7055348209, finding) · `20261121-champion-row-landed` (7055360128) · `20261121-recovery-sweep` (7055293870) — §7-f/§7-k ancestry.
- FILL-LEG run envelopes: `44854746984` (7055746857) · `44868130710` (7057539747) · `44874772317` (7058500488) — S2's run rows.
- `20261121-l1-b1v3` (7057409061) · `20261121-l2-court-drafts` (7057456632) · `20261121-l3-citation-provenance` (7057470726) · `20261121-l4-machine-closures` (7057585797) · `20261121-l5-verbatim-wave` (7057586058) — the A3 + court + spine fold lines (§7-h…l).
- `20261121-pilot-solved` (7058604295) · `20261121-a3-wave-convergence` (7058621937) — §7-m/§7-n landings.
- Open / non-claim rows: fill-122 FAILURE (7061690591) · `20261121-night-close` (7062050444) · `20261121-integration` correction (7062308666) · `20261121-armd-kit` (7062507520) — register the seam, do not smooth it.
- The rest of the last 60 = hourly cadence + scheduled re-grounding envelopes (state rows, no new claim class).

## 4. Register verdicts — the three movements

- **R1 — read restored.** What the STUDY holds: the harbor/tooling is restored and receipted — fill `44868130710` SUCCESS (7/7, JSON-parse gate) with canary `44787964389`'s cause named as the runner harness class, not the substrate (§7-k, S2); plus the verification spine's first-hand 3/3 + 1/1+5/5 receipts showing the read path works under an external pair (§7-i/§7-p, M4/C1). This is *machinery + evidence*, not a substrate certificate for "reads are restored" in general. What remains upstream's: the RFC-side read-path semantics and deployment — the study never claims to have restored the upstream's own read path; its receipts certify only the rig's cells. Certifying evidence: S2 (run + root-cause) and M4/C1 (spine).
- **R2 — store re-readable.** What the STUDY holds: a direct answer at the substrate layer — the M1 stamp CERTIFYs the persistence property under a compliant reader (§7-g, S1: A 0.000 → B 1.000, B−A=100 ≥ 20, B ≥ 0.85·C, judge gate 1.0, ledger sha `be7fc43e…`), with the qwen4 FALSIFY registered as reader non-compliance (`bacc436d`), i.e. the store is re-readable when read to protocol. This is the one row that is a `direct answer`, and it is *bounded to the substrate property* — not a claim that the upstream's store is re-readable. What remains upstream's: the upstream's store format, reader implementation, and the reader-compliance fix that the FALSIFY row diagnoses. Certifying evidence: S1 (CERTIFY + triangulation).
- **R3 — compaction governed.** What the STUDY holds: evidence and a named boundary, not a governance answer — the A3 wave converges that the suppressor is not a token-logit artifact and the judgment layer / weights are the next rung, which is NOT_RUN at n5 (§7-h…p, M1/M2); the pilot registers PROOF-OF-CONCEPT with the boundary = the judgment layer (§7-m, M3); the court drafts + spine provide first-hand verifier receipts (§7-i, C1/M4). What remains upstream's: the actual compaction-governance mechanism and its enforcement — the study explicitly stops at the judgment layer; B′ is inert at n5 with the validity seam open, and the weights rung is pre-registered but not fired. Certifying evidence: M1/M2/M3 + C1/M4 (all *evidence*, none `direct answer`).
