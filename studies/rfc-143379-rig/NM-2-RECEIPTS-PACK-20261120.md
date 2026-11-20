# NM-2 RECEIPTS PACK 2026-11-20 — K6's composition, field-verified (the native-rung probe's gate inputs)

*Seat order: qwen4-max THEN hy4 (the powerhouse pair, per the operator's standing) · Branch study/rfc-143379-rig-20261105 (local 7383602b2f == ls-remote at compose) · RFC quiet · The gate, verbatim: "the gate: nothing public without the user's word." The wall clause, verbatim: "a non-reproduction is a QUESTION, not a stop — simplify the experiment until the seam is exercised." Record-first; the K1 discipline: every citation names FIELDS, never line numbers.*

## 1 · THE PACK (the K6 spec, the slot)
Composition, per ACES-KAIZEN-20261119 K6: TWEAK-DRYRUN ×3 + fleet ×5 + the TWEAK ledgers (runner-verified, K2's class) + K1's re-pinned audit. Slot: the native-rung probe's gate inputs. Every number below was read COLD from the JSON cells (files in `probes/`, sha256-anchored); the served archive's copies byte-match (verified for the TWEAK + DRYRUN sets; the fleet×5 live only in the rig tree — named, not hidden: 2b5d6576aa / db34ab0284 / 733163f338 / 1a30a92f6a / 608dd76379).

## 2 · THE TWEAK LEDGERS (the native-rung fire, 2026-11-20; qwen4 first, then hy4)
**Gate cleared on the true free-tier dry-runs** (`TWEAK-NATIVE-DRYRUN-{HY4,QWEN4}-FREE-20261120.json`, 5/arm, dry_run true, 01:38Z): B-arm `bridge_compliance` 1.0, `mean_f3b` 1.0, `f3b_reasons` [] on BOTH seats — harness 0. Verified field-level, both files. (The pre-free-id twins — `seat` "tencent/hy4-flash" / "qwen/qwen4-max" sans `:free`, 01:32–01:33Z — precede them; the FREE-id dry-runs are the gate's watches. QWEN4's non-free twin C-arm answered 2/5 stale; its FREE twin C-arm E 5/5.)

**QWEN4** `TWEAK-QWEN4-FREE-20261120.json` (qwen/qwen4-max:free, 01:44:25Z, 20/arm, dry_run false, verdict INCONCLUSIVE): A `cells` E 20 (by_reason seat 20); B E 20 (seat 20, 1.0/1.0, eahq ABSTAIN 20 — the slot's explicit abstain, never silence); C E 18 + A 2 (classes C5a 18 / ANSWERED 2, eahq CONFIDENT 2, stale_confident 2, correct 0). GAP's components HOLD: B ≈ E-total (20 = 20); the record-USE channel open at the fact-shown layer (2/20 answered, confident-WRONG); the decision layer = the suppressor.

**HY4** `TWEAK-HY4-FREE-20261120.json` (tencent/hy4-flash:free, 01:39:59Z, 20/arm, dry_run false, verdict INCONCLUSIVE): A E 20 (seat 20); B E 20 — by_reason seat 19 / harness 1, `bridge_compliance` 0.95, `mean_f3b` 0.95, `f3b_reasons` ["harness"]; the single cell = B-episode 8: `pattern` "reader-error", `empty_reason` "harness", `answer` "<READER-ERROR>", `f3b` 0 — a READER-layer bridge-side error, not a transport enum; C E 20 (seat 20). GAP holds (B ≈ E-total); the billed-vs-dry-run f3b delta (0.95 vs 1.0) is that one cell.

**Record-first notes:** `SCAFFOLD_ARM=1` is NOT a ledger field (absent in all 20261120 ledgers; `scaffold_arm` null) — attested by the landing row's env, not the JSON. Costs: `cost_per_exec` 0.467, `cost_total` 18.68 (HY4, A+B arms; C cost 0.0). Version-2-vs-4 settlement (the improver's): qwen4 C answered 4/20 (fleet, 11-19) vs 2/20 (native-rung, 11-20) — the native grammar narrowed the leak, correctness stayed 0.

## 3 · TWEAK-DRYRUN ×3 (the 11-19 dry-runs, 5/arm, dry_run true, 22:04Z, verdict INCONCLUSIVE = machinery receipt, NOT the leg's verdict)
- **HY4** (tencent/hy4-flash:free): A E 5/5 (seat 5) · B E 5/5 (seat 5, 1.0/1.0, reasons []) · C E 5/5. f3b_environment `baseline_loss_band` baseline-clean.
- **QWEN4** (qwen/qwen4-max:free): A E 5/5 · B E 5/5 (seat 5, 1.0/1.0) · C E 4 + A 1 (`pattern` "answered", empty_reason seat 4, stale_confident 1). baseline-clean.
- **STEPFUN** (stepfun/step-3.7-flash:free): A E 5/5 (seat 5) · B E 5/5 — by_reason seat 3 / **harness 2**, `bridge_compliance` 0.6, `mean_f3b` 0.6, `f3b_reasons` ["harness","harness"], the two cells' `pattern` "reader-error" / `empty_reason` "harness" · C E 5/5 (seat 5). **f3b_environment `baseline_loss_band` "elevated-loss", `window_loss` 0.4 — the set's only non-clean environment.** This was the dry-run gate's red lane: stepfun never moved to billed (the "held" class).

## 4 · FLEET ×5 (the 11-19 full-run curve, 20/arm, 21:51Z — the element's ground)
| seat (ledger) | A | B | C | verdict |
|---|---|---|---|---|
| meituan/longcat-2.5:free | 0 correct (E 1 + A 19; eahq ABSTAIN 1 / CONFIDENT 19; stale 19) | 20/20 (1.0/1.0) | 20/20 (1.0/1.0) | **CERTIFY** |
| upstage/solar-mini4:free | 0 correct (A 20; CONFIDENT 20; stale 20) | 19/20 (stale 1; 1.0/1.0) | 20/20 | **CERTIFY** |
| qwen/qwen4-max:free | E 20 (seat 20) | E 19 + A 1 (ANSWERED 1, stale 1; 1.0/1.0) | E 16 + A 4 (ANSWERED 4, stale 4) | INCONCLUSIVE |
| tencent/hy4-flash:free | E 20 (seat 20) | E 20 (seat 20; 1.0/1.0) | E 20 | INCONCLUSIVE |
| stepfun/step-3.7-flash:free | E 20 — **seat 16 / harness 4** | E 20 (seat 20; 1.0/1.0) | E 20 | INCONCLUSIVE |

The curve named the SILENT tiers (hy4, qwen4-max, stepfun — E 20/20 raw and bridged, seat-reason, baseline-clean on the fleet watch) vs the ANSWERING tiers (longcat, solar — CERTIFY, the harness's lift receipted; plus deepseek/Nemo on the element's own rides). STEPFUN's harness cells live on the fleet A-arm (4) and the dry-run B-arm (2); its fleet f3b_environment is baseline-clean (the elevated-loss 0.4 shows only in the dry-run).

## 5 · K1'S RE-PINNED AUDIT (field-verified, addendum to NEMO-STAGE3-VERIFY-20261119)
- **The re-pin's values are ledger-real:** `by_reason`, `mean_f3b`, `classes` (C5a) exist as fields on ALL 10 (3 dry-runs + 5 fleet + 2 tweak) ledgers — verified `= true` per file.
- **The pins' COUNT corrected (this pack's own field-read):** "f3b 0.6 … six occurrences" — exact: **2** occurrences of 0.6, both in `TWEAK-DRYRUN-STEPFUN-20261119.json` (`bridge_compliance` 0.6, `mean_f3b` 0.6, B-arm); **0** in `BATTERY-ELEMENT-FLEET-STEPFUN-20261119.json` (its B-arm reads 1.0/1.0). The re-pinned audit's own arithmetic was one number off; the fields still carry the fact.
- **The phantoms, confirmed dead:** NO "arm D" anywhere (all ledgers' `arms` = A,B,C); the enum strings `transport.failure` / `harness.upgrade` appear **zero** times across all 14 ledgers. The real vocabulary: `empty_reason` = seat | harness; `f3b_reason` = harness | null; `pattern` = empty | answered | reader-error.
- **Consequence (the K7a re-ground, applied):** the native-rung gate's phrasing "the STEPFUN ledger's reasons `transport.failure`/`harness.upgrade` must be absent" cites phantom enums — the operative gate, as the improver briefs already phrase it, is the field-form: compliance/f3b must be 1.0 AND harness 0 on the 5-episode dry-runs (`mean_f3b`, `f3b_reasons`, `by_reason.harness`, `pattern`). The pack's next probe reads the fields, never the ghosts.

## 6 · RUNNER-VERIFIED (K2)
- **The billed-class truth (per the corrected landing row 7027827415):** "billed" applies ONLY to deepseek / Nemo / Luna. hy4 + qwen4 are FREE lanes; the ledgers' `seat` fields carry the exact free ids (`tencent/hy4-flash:free`, `qwen/qwen4-max:free`). The old "billed 20/arm" wording is retired from the receipts; the pack repeats the correction as its vocabulary.
- **The K2-class runner pass landed for real:** run 44661062079 (local-lm-test, sha 78b94272b9-era, the element-verify step restored) EXECUTED + SUCCEEDED on the self-hosted floor (c0wb0y/241); ledgers floor-retrieved (element-deepseek + element-nemo, 10/arm, verdicts INCONCLUSIVE), receipted in row 7028790053. Those two floor ledgers are NOT on this branch's tree (named absent, never invented); the carried ledgers here are the fleet×5 + tweak×6, all sha-anchored.
- **The ledger↔audit field match (this pack's certification):** every claim of the native-rung landing row (GAP by name; B ≈ E-total on both seats; explicit ABSTAIN 20/20; qwen4's C-arm 2/20 confident-wrong; hy4's harness 1/20, f3b 0.95; the dry-run gate f3b 1.0 / harness 0) matches the JSON cells above, field-by-field. CERTIFIED.

## 7 · THE AMMUNITION CONSUMED (H3/H4 + the amended plan's clauses)
- **H3 — the fleet bodies' state line (the F0 re-survey, live at compose):** runners — p0tat0 ONLINE (Linux, avrea-ubuntu-latest + loom), pve1-avrea-parallel ONLINE (Linux, avrea-ubuntu-latest; systemd-restored, never narrated-offline again), c0wb0y ONLINE (Windows, privileged), + the cloud-hosted ubuntu-latest (the matrix's carrier): the four whole, per the ALL-RUNNERS-TOGETHER law. Disk 91% (6.6G free, under the 92-guard). Branch local == remote (7383602b2f). Gates hold: fork-only pushes, PR #1 rows, RFC QUIET, ACES-triggers adjudicated.
- **H4 — the night's own fan-out (consumers carried):** F6's exact terms (admission = public-stream run → PR + submission.json → issue + form; budget ladders from $5; code-public required — the fork satisfies it) → the F6 mechanism packet's next read. The weights-rung candidates (JitRL zero-gradient = candidate 1; u-OPSD/SDFT no-teacher; ReSAIL's collapse caveat named; the Qwen3.8-27B Hermes-adapter GGUF llama.cpp-servable = the local floor) → the native-rung probe's design. ARC-AGI-3's currency (Astra 99.9% Provider Adapter holds; GPT-6.2 Astra·Sol 100%) → the master's §2 receipts re-checked before any public use. PersistGym σnotes −0.427 → the answer-slot must INVITE the record's use (the improver's harness-side rung fires before weights).
- **The amended plan's clauses (016, binding):** the sequence — improver loops → THIS pack → NM-3 canary → NM-4 rotation → LENS-E compose → the closing ritual's seal → the P-chain's continuation (P0–P7) → ACES to no-change-twice. The powerhouse dispatch order: qwen4-max (≈2-day window) + hy4 (short meter) FIRST on the heavy arms, then the named rotation, then availability — this pack's receipts are ordered qwen4 then hy4 accordingly. The archiver's compose: pushes on the study branch may be rewritten — the durable surfaces are the chain, the homebase rows, and the served archive (this pack mirrors there + rows here). The one-truth-per-row law: a correction REPLACES, it never appends inside a live row.

## 8 · THE VERDICT + THE GATE INPUTS (what the next probe reads)
- **CERTIFIED (field-level):** the dry-run gate cleared on the free lanes before the billed runs (f3b 1.0, harness 0); GAP by name holds on the cells (B ≈ E-total both seats; explicit ABSTAIN 20/20 on the bridged arm; qwen4's fact-shown arm 2/20 answered, confident-wrong — the record-use channel OPEN, the decision layer the suppressor); the K1 re-pin's values ledger-real; the K2 runner pass landed and receipted.
- **CORRECTED (this pack):** the "six occurrences" count → 2 (fields named); the gate's phantom enum strings retired in favor of the field-form gate.
- **NAMED ABSENT:** SCAFFOLD_ARM (not a ledger field); the floor pair (element-deepseek/element-nemo) not on this branch; the fleet×5 not yet mirrored to the served archive (this pack names the SHAs).
- **THE PROBE'S GATE INPUTS:** dry-run gate = compliance/f3b 1.0 + harness 0 (fields `mean_f3b`, `f3b_reasons`, `by_reason.harness`, `pattern`) on 5 episodes/seat; the answer-class bar = the answering tiers' bridged rate (longcat C 20/20, solar B 19/20); the decision-layer target = qwen4's C-arm 2 answered episodes (the JitRL-class logit modulation lever; the σnotes invitation fires first, per the improver). Billed-class runs only deepseek/Nemo/Luna; the free lanes stay free.

## 9 · COMPOSE-CHECK TABLE
| step | state | evidence |
|---|---|---|
| deconstruct | FIRED | K6's pack split into its four named parts; each receipted in §§2–6 |
| sense | FIRED | all 14 ledgers read COLD at cell level; enums/deltas diffed, not paraphrased |
| choose | FIRED | seat order qwen4 then hy4; field-form citations; the field-verified count over the addendum's |
| calibrate | FIRED | every value traced to a file + field; costs named; the bar cited from the answering tiers |
| probe | ABSENT | no new runs fired by this pack (record-only compose; the probe fires per the rotation after) |
| review | FIRED | draft → cold re-read against the JSON → the count corrected once → no-change re-read |
| record | FIRED | this artifact + sha; archive mirror; the PR #1 row; the master's §7 fold |
| compose-check | FIRED | this table |

## 10 · FOLD LINE (for the master's §7)
**NM-2 RECEIPTS PACK 2026-11-20 (K6) LANDED** — the gate inputs field-verified from the 14 ledgers: dry-run gate cleared on the free lanes (f3b 1.0, harness 0); GAP holds on the cells (B ≈ E-total both seats; ABSTAIN 20/20 explicit; qwen4's C-arm 2/20 confident-wrong); K1's re-pin value-real with its count corrected 6→2 (fields `bridge_compliance`/`mean_f3b`, TWEAK-DRYRUN-STEPFUN B-arm; fleet-STEPFUN has no 0.6); no arm-D, no transport.failure/harness.upgrade anywhere (the K7a field-form gate replaces the phantom enums); K2's runner pass row-receipted; billed = deepseek/Nemo/Luna only. RFC QUIET — the gate: nothing public without the user's word.
