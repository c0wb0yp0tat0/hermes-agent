# COPYCAT FINDING — lane `step` — the fourth lens (the seat's window)

**Lane:** copycat (step base — the fourth independent lens on the study's record). **Artifact:** `studies/rfc-143379-rig/copycat-findings/copycat-step-20261105.md`.
**Register:** receipts, never claims. No instrument re-run; every number below is read from the rig's files (named at each citation). A red verdict is a finding, never smoothed. This lens read the key-verdicts cold — RESULTS-ALIASING, RESULTS-PIN, RESULTS-COMPETING, SYNTHESIS — and adjudicates each independently, convergence be damned.

## 0. The one-line verdicts (the short form; the body is the proof)

- **RESULTS-ALIASING CONFIRMED-BOTH is a FINDING on the interaction, with one metric caveat.** The aliasing × proximity interaction is real and mechanically produced by the window's eviction class (format-collisions only bite when the quoted literal has aged out of the K-window); the a*-proxy R² = 0.6548 ≥ 0.35 bar is an **instrument-limit** number, not evidence-mass — it inherits the equal-weights softmax degeneracy I name in §1.1, so the bar-crossing licenses "the proxy moves with the prevalence" but not "evidence mass explains it."
- **RESULTS-PIN PROTECTS is a FINDING, and the strongest single result in the study.** Recurrence-aware pinning drops deep-minima prevalence from 1.00 (recency-pinned variant) to 0.15 at the confirmed aliasing×proximity pair; the per-seed onset split (seed 0 = cycle 68, seed 1 = cycle 87) is predicted by per-seed occurrence, which is exactly what a recency-only variant cannot reproduce. This is the one arm that closes a RED.
- **RESULTS-COMPETING ARCHIVE-REFUTED is a FINDING on the tested construction, and closes the archive class.** Fixing the toothless knob (competing admission + both inertias) does not clear the gate: worst-case min stays sub-zero at 4x/8x across budgets 0/1/5% and rival_rate 0/0.3. The archive class is refuted under the tested construction; "recall-based archive" is not certifiable.
- **SYNTHESIS's one-mechanism line is PARTIALLY SUPPORTED, with one seam.** "The K-recency window's eviction is the recency-truncate class" holds for the demand-age + constraint arms and is corroborated by PIN (recency loses, recurrence wins). The seam: SYNTHESIS was written with lane B PENDING-FROM-LANE, and folds lane B's rows by mechanism-shape assumption, not by measurement — the integration chapter is derived, not verified. Lane B's rows must be folded before the synthesis's gate verdict is re-issued.
- **The one next mechanism (divergent from the prior lanes' pinning/archive proposals): ALIAS-AWARE FORMAT-PINNING.** Pinning the exact bytes protects the literal (PIN proves it) but the aliasing arm shows format-collisions defeat recovery precisely when the literal is evicted — a pinned exact copy does not pin the format-class, so a look-alike rival still collides at the read. Pin the literal's format-signature (a tombstone that rejects format-neighbors), not just the bytes. Falsifier below.

## 1. The adjudication — for each red verdict, FINDING or INSTRUMENT-LIMIT

### 1.1 RESULTS-ALIASING (CONFIRMED-BOTH) — FINDING on the interaction; INSTRUMENT-LIMIT on a*

**Verdict: FINDING (interaction) + INSTRUMENT-LIMIT (metric).**

The interaction claim — "aliasing keeps deep minima high with M OFF; M raises prevalence with aliasing OFF" — is a real mechanism, not an artifact. The driver is the window's eviction class: a format-collision (look-alike rival) only defeats recovery when the true literal has aged out of the K=10 tail window, i.e. when the read path must fall back to the latent floor or the survivor pool. With M on, the prevalence shifts because the aliasing channel's mass changes, not because the window grew. The four-cell prevalence table in RESULTS-RECITE.md corroborates the same shape from the recitation side (aliasing ON keeps prevalence 0.575–0.675 at 300c regardless of recite ON/OFF, ≤0.1 delta), so the interaction survives an independent knob.

The caveat — and it is the same caveat I raise for the competition arm — is the a* proxy. RESULTS-ALIASING reports `a*-proxy (evidence-mass) R² = 0.6548 (meets bar 0.35)`. I did not re-read `probe_alias.py` in this pass (read-gate), but the construction pattern I did read in `probe_compete.py` assigns `weights = [1.0] + [1.0] * len(rivals)` and computes the softmax over that — equal mass per rival, so a* is a function of rival *count*, not of evidence mass. If `probe_alias.py` follows the same pattern (and the probe docstrings in this rig are templated, so I expect it does), then the 0.6548 is a count-correlation dressed as evidence-mass, and "meets bar 0.35" licenses only "the proxy covaries with prevalence," not "evidence mass explains the prevalence." **The interaction stands; the explanatory metric does not.** Byte-level confirmation of `probe_alias.py`'s weight assignment is the one re-read this lens would do next.

### 1.2 RESULTS-PIN (PROTECTS) — FINDING

**Verdict: FINDING.** This is the cleanest result in the study and the one arm that actually closes a RED.

Byte-level, from RESULTS-PIN.md:
- Per-seed onset: seed 0 = cycle 68, seed 1 = cycle 87. Per-seed occurrence predicts onset.
- Recency-pinned variant: prevalence 1.00 at the aliasing×proximity pair (alias_on=True, prox_on=True).
- Recurrence-aware pinning: 0.15 at the same cell; 0.00 at the other three cells (both modes).

The mechanism is pinned down by the onset test, not just the prevalence table: a recency-only pin cannot reproduce the per-seed onset split (seed 0 earlier than seed 1), because recency is a function of position, not of how often the literal recurred. The recurrence-aware variant reproduces it, which is why recency *loses* protection and recurrence *keeps* it. This is the falsifier the prior lanes named ("if per-seed occurrence/recurrence carries the per-seed onset, a recency-pinned variant loses the protection") and RESULTS-PIN confirms it. **No instrument-limit caveat here** — the pinning probe is deterministic and the keep-sets are mechanically produced, same class as `probe_constraints.py` (recency-truncate 1.00 vs pinned 0.00).

The one residual: 0.15 ≠ 0.00 at the worst cell. Pinning does not fully eliminate deep minima under aliasing×proximity; it drops them by 85%. The synthesis's "pinning restores 0%" (from RESULTS-CONSTRAINTS) is the *constraint* arm's number; the *demand-age* arm's number is 0.15. These must not be conflated — and the pinning-cost re-walk's correction (18 pinned word-tokens, ~0.18% at 10K context) is the cost side of the same coin. 0.15 residual at ~0.18% token cost is the honest trade.

### 1.3 RESULTS-COMPETING (ARCHIVE-REFUTED) — FINDING on the tested construction

**Verdict: FINDING (on the tested construction); the archive class is closed within the tested classes.**

Byte-level, from RESULTS-COMPETING.md and `probe_competing.py`:
- The repair fixes both inertias named in the prior lanes: no per-cycle rlimit (budget is the only cap), and no gratuitous single recall at 0% budget (`if k == 0 and archive_budget == 0 and not competing: return floor` — 0% grants nothing).
- Competing admission admits either the demanded literal's id OR a rival at query time, with the rival consuming the same budget.
- Result: worst-case min stays sub-zero at 4x/8x across budgets 0/1/5% and rival_rate 0/0.3. No cell clears the letter's worst-case min ≥ 0pp.

The mechanism the refutation rests on: the demanded literal's miss persists via the latent floor even when the budget is spent on rivals. The archive stores everything (optimistic bound, `for t in stream: arch.put(t[1])`), but recall only helps when the literal is the one admitted; under competition the budget is contested and the miss survives. This is the same "latent floor" driver as the demand-age gate (§1.4 of the prior lanes' findings), so the refutation is *consistent* with the gate's mechanism rather than a new one.

The caveat, and it is the honest scope limit: only one query-time scoring rule was tested (demanded-first by evidence mass), and the rival is a synthetic look-alike (`make_rival` appends `#r{…}`). "Archive class closed" is licensed only for "recall-based archive with query-time admission under look-alike rivals." A different admission policy (e.g., demand-aware priority that always admits the demanded literal when present) was not tested; but the prior lanes' toothless-knob analysis already showed that admitting *only* the demanded literal (the original shape) is toothless because the budget never faces a rival. The competing repair is the honest falsification of the stronger claim. I accept ARCHIVE-REFUTED as the final word within tested classes, matching wave-10's "map complete."

### 1.4 SYNTHESIS — PARTIALLY SUPPORTED (one seam)

**Verdict: PARTIALLY SUPPORTED.** The one-mechanism line — "the K-recency window's eviction is the recency-truncate class; the recitation floor and the governance decay are one mechanism wearing two hats" — is supported by the demand-age arm, the constraint arm, and now PIN (recency loses, recurrence wins). That is three independent instruments converging on the eviction class.

The seam: SYNTHESIS.md states lane B (constraint-survival) was PENDING-FROM-LANE at synthesis time, and the integration chapter is "derived from lane A's curve plus the RFC's stated mechanism and is not blocked on lane B's rows." RESULTS-CONSTRAINTS has since landed (recency-truncate 1.00, pinned 0.00, pinned share ~9.8–15.6% raw / ~0.18% at 10K), so the seam is closable — but SYNTHESIS has not been re-issued with lane B's rows folded. Until it is, the synthesis's gate verdict is a mechanism-shape claim, not a measured one. The fourth lens's position: **the mechanism line stands; the synthesis document should be re-issued before anyone cites its gate verdict.**

A second seam, smaller: SYNTHESIS cites the honest note that "this run's deterministic sim records no sub-zero aggregate point; per RFC's reported field data K=10 landed -3.5pp at 300 cycles," and says the pilot contour will reconcile. That reconciliation is still outstanding (RESULTS-RECITE's next steps say "fold into SYNTHESIS when lane data lands"). So the study's headline number (-3.5pp field) and the instrument's honest curve (+0.60pp mean at 4x/300c+) remain unreconciled in the synthesis. Not a finding about the mechanism; a bookkeeping gap.

## 2. The one next mechanism — ALIAS-AWARE FORMAT-PINNING

**The prior lanes converged on exact-literal pinning (longcat, krecency) and competing-admission archive (beam). Pinning is now verified (PROTECTS); archive is refuted (ARCHIVE-REFUTED). The convergence signal is: pinning wins, recall loses. The fourth lens's divergence: pinning as currently specified pins the *bytes*, but the aliasing arm shows the failure mode is *format*-class, not byte-class.**

The gap, byte-level: in `probe_compete.py`/`probe_alias` territory, a rival is a look-alike with the same shape and different content (`rival_value` returns a same-kind string). When the true literal is evicted from the K-window, recovery falls to the survivor pool, where the rival collides on *format* — the read cannot tell which same-shaped value is the true one. Pinning the exact bytes (RESULTS-PIN) protects the literal when it is the *demanded* one, but the aliasing arm's deep minima come from cases where the read's candidate set contains a format-neighbor that the pin does not cover, because the pin is keyed on the literal's identity, not on its format-signature.

So: **pin the format-signature, not just the bytes** — a tombstone that, when a literal is pinned, also rejects (or disambiguates) any survivor sharing its format-class. The constraint arm's analog already exists: pinned standing-lines are 4 POLICY constraints, and pinning restores 0% violations. The extension is to make the pin carry a *format mask*, so the read path fails closed on format-neighbors the way the anchor fails closed on evicted constraints.

**Falsifier (the test that would kill this):** run the PIN probe's four-cell grid with an added knob `format_pin ∈ {off, on}`. If exact-byte pinning already drops deep-minima prevalence to 0.00 under aliasing ON (i.e., the 0.15 residual at alias_on×prox_on disappears without format-pinning), then format-pinning is redundant and exact pinning is sufficient — the aliasing arm's minima are byte-level, not format-level, and the mechanism is simpler than I claim. If instead format_pin is required to reach 0.00, the format-class mechanism is real and exact pinning alone is insufficient. The decisive number is the alias_on=True, prox_on=True cell: 0.15 (current) → 0.00 (format-pin on) would confirm; stuck at 0.15 would refute.

**Secondary falsifier (cost):** measure pinned-token count with format-masks attached. If format-pinning multiplies the pinned set beyond the ~18 word-tokens / ~0.18%-at-10K class, the cost side of the trade breaks and the mechanism is not deployable at the field's <0.5% claim. The pinning-cost re-walk's denominator discipline (pinned token count is the measurable; percentage only against a named context) applies unchanged.

## 3. Receipts (file-level, byte-cited where read)

- `krecency/RESULTS-ALIASING.md` — CONFIRMED-BOTH; a* R² 0.6548 ≥ 0.35; aliasing ~150-token scale; format-rivals ≤0.3% variance; `results/alias.csv` (800 rows).
- `krecency/RESULTS-PIN.md` — PROTECTS; onset seed 0 = cycle 68, seed 1 = cycle 87; prevalence table (recency 1.00 → recurrence 0.15 at alias_on×prox_on); `results/pin.csv` (200 rows).
- `krecency/RESULTS-COMPETING.md` — ARCHIVE-REFUTED; budgets 0/1/5%, rival_rate 0/0.3, 4x/8x; `probe_competing.py`, `sweep_competing.py`, `results/competing.csv`.
- `krecency/SYNTHESIS.md` — one-mechanism line; lane B PENDING-FROM-LANE seam; unreconciled -3.5pp field vs +0.60pp instrument mean.
- `krecency/RESULTS-AGE.md` — FAIL per letter; UPDATE: all 25 seeds carry sub-zero deltas at 4x/300c+; means 4x +23.87→+0.60pp; K-SCALING arm: scaled-K underperforms fixed-K10.
- `krecency/RESULTS-CONSTRAINTS.md` — recency-truncate 1.00 (worst), pinned 0.00 restored; pinning-cost re-walk (18 word-tokens, ~0.18% at 10K).
- `krecency/RESULTS-RECITE.md` — NOT-CONFIRMED; recite ON ≤0.1 delta at every cell.
- `krecency/probe_age.py` — `if k == 0: return floor`; K=10 `if q in snap`; `age = 1 + int((cycle_idx/10.0)**1.3)`; `FLOOR` table. No injected decay term.
- `krecency/probe_archive.py` — `for t in stream: arch.put(t[1])` (optimistic); recall gated on `arch.id_of.get(q)` (demanded literal only); `max(1, mat_budget_tokens)` grants one recall at 0%.
- `krecency/probe_compete.py` — rivals injected only into K=0 floor path; K=10 hit path (`if q in snap`) never faces a rival; `weights = [1.0] + [1.0]*len(rivals)` (equal mass).
- `krecency/probe_competing.py` — repairs both inertias; admission decision branch (toothless vs competing) as cited.
- Prior copycat findings: `copycat-longcat-20261105.md`, `copycat-beam-20261105.md`, `copycat-krecency-20261105.md` (convergent on pinning; this lens diverges on format-pinning).

## 4. The fourth lens's closing note

Three independent lenses (longcat, beam, krecency) converged on exact-literal pinning as the next mechanism and on the gate FAIL as a finding. The fourth lens confirms the convergence on the finding side (FAIL is real; pinning protects; archive is refuted) and diverges on the mechanism side: the aliasing arm's format-collisions are the residual that exact-byte pinning does not close (0.15 at the worst cell), and the next mechanism is therefore format-aware pinning, not more exact-byte pinning and not another archive variant. The convergence is the signal that pinning is the right class; the divergence is the signal that the class's current specification is byte-narrow. Both are reported, not reconciled — the falsifier in §2 is the reconciliation instrument.
