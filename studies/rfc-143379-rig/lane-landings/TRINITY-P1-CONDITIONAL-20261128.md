# TRINITY-P1-CONDITIONAL — verdict artifact (2026-11-28)

Skeleton (title + inventory) — delivery envelope for the CONDITIONAL-probability (P1) wave.

## Inventory

| # | Candidate | Borrows | Measure | Banner |
|---|---|---|---|---|
| C1 | Miss-rate discriminator under the K-window | REFS2-1 | P(miss\|anchor-cold) vs P(miss\|in-window) | candidate |
| C2 | K-window claim re-anchored (conditional basis) | REFS2-1 | P(correct\|literal in window) vs P(correct\|outside) | candidate |
| C3 | Divided write-gate (action-conditioned) | REFS2-1 | outcomes read vs write instead of pooled | candidate |
| C4 | Harness-delta ledger / same-model-two-harnesses AB | REFS2-2 | harness-level deltas on one model | candidate |

## MAP matrix (asserted → status → basis)

| row | asserted | status | basis |
|---|---|---|---|
| M1 | cold-detail ≥ 90 pct is the pilot falsifier | candidate | REFS2-1 filtered on last-touch age |
| M2 | K-window claim measured on conditioned rows | candidate | REFS2-1 filter-then-measure |
| M3 | write-gate split by action | candidate | REFS2-1 divided gate |

## OWED register (load attempts + outcome)

| skill | load attempt | outcome |
|---|---|---|
| pin-framework | load | staged, no take |
| investigation-documentation | load | staged |
| agent-work-review | load | staged |
| defect-forensics | load | staged |
| aces-harness-probes | load | staged |
| krecency-instrument | load | staged |

Walled/partial: REFS2-2 full body (member wall after opening); REFS2-1 content verified open.
No claims in this artifact are invented — all instrument mechanics quote REFS2-1/REFs-2 PACKETS.

## ENRICHMENT-BY-hy4 (round A)

Lens: REFS2-2 (AGI and the harness) — the model is not the system; context/tools/gates/guardrails
decide what capability becomes in the world. Three additive items; no silent rewrites.
Provenance note: REFS2-2 body recovered from the git object (member-walled in tree) = HEAD-RECON.

**A1 — CONTRADICTION FLAG on C1/C2/M1–M3 (observation ≠ intervention).** Every P1 rate is an
observational conditional: filter-then-measure on `df[cond]` [BORROWED REFS2-1]. The harness
lens says the outcome is decided by a harness *setting*, and the RFC's experiment is a
same-model two-harness AB — a `do`, not a `|`. `P(miss | anchor-cold)` need not equal
`P(miss | do(anchor-cold))`: cold-anchor is itself a harness routing decision, so the
conditioned rate can be confounded by *which* questions were sent cold. FLAG (do not rewrite
C1): keep the discriminator as a necessary signal, but require the read-flip AB to identify
the harness effect before M1's ≥90 pct is called a falsifier. [IN-LANE harness; BORROWED REFS2-1]

**A2 — NEW candidate C5: the Tahoe price-taking guardrail.** The Tahoe bot did not fail for
lack of capability; it agreed to a price it never checked — a harness failure, not a model
failure [IN-LANE, REFS2-2 opening]. Study analogue to add to C3: a write-gate that stamps
"verified" on *action alone* is our Tahoe — a lock with no price-taking. C5: before stamping,
the gate must evaluate the claim's asserted quantity against the conditioned denominator
(the `df[cond]` rate from C1), and a read with no lock stays unverified. Same model, two
harnesses: the delta is the guardrail. [IN-LANE]

**A3 — python-mechanics note (operationalize C4).**
```python
df["layer"] = df["change_kind"].map(lambda k: k if k in {"MODEL","HARNESS","CHANNEL"} else "UNCLASSIFIED")
for L in ("MODEL","HARNESS","CHANNEL"):
    d = df[df["layer"] == L]                  # filter-then-measure, REFS2-1
    print(L, len(d), d.loc[d.action=="write","outcome"].mean())
ab = df.groupby(["model_id","harness_id"]).outcome.mean().unstack()
print(ab.diff(axis=1))                        # harness delta, model held fixed
```
[IN-LANE ledger; BORROWED REFS2-1 filter-then-measure]

**OWED — full stack dump-and-refuse (hy4 round A).** USED: pin-framework (classifier/lint
posture), investigation-documentation (ledger is the documentation), aces-harness-probes
(same-model two-harness AB), REFS2-2-HARNESS (my lens), REFS2-1 (conditioning arithmetic).
REFUSED: agent-work-review (no agent trace here), defect-forensics (root-cause claim exceeds
the evidence), krecency-instrument (would silently rewrite C1/C2 — flag only), DESIGN-LINT
(additive only, no edits), REFS2-3-EIGEN (stepfun's lens, not this seat). [IN-LANE / BORROWED as
named above]
