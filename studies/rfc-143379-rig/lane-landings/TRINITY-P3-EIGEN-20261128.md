# TRINITY-P3-EIGEN — Eigenvalues-own-numbers (2026-11-28)
Artifact path: studies/rfc-143379-rig/lane-landings/TRINITY-P3-EIGEN-20261128.md
Source: REFS2/REFS2-3-EIGEN.md (head pre-read; member wall after opening)

## Executive Summary
The eigenvalue lens yields four instrument candidates for the study's own machinery: (1) Invariance-Spectrum Report — decay eigenvalues per content class; (2) K-Window Eigenvalue Filter — spectral truncation for recency; (3) Fleet Cadence Resonance Detector — avoid provider-rotation resonance; (4) Read-Restore Eigenvector Bookkeeper — pin/frame for sanitize seams. The pilot falsifier "cold-detail >= 90%" formalizes as verbatim eigenvalue >= 1.0 under the read-restored harness. No contradictions between the REFS2-3 packet and the kitted context; the spec-1/spec-2 lock-shape difference is a class mismatch, not a receipt conflict.

## Analysis Brief
Source: REFS2-3-EIGEN.md — London Millennium Bridge (160 pedestrians tipped its natural frequency; "a rhythm that had been sitting in its blueprints all along"); "Eigen" = own; eigenvalues are scale factors along eigenvectors that stay invariant.
Core transfer: eigenvalues → invariance under the memory compaction/decay operator; K-window → largest-eigenvalue filter; pin → explicit eigenvector bookkeeping; resonance → fleet cadence warning.
Problem surface: memory-read restore (a43818a6…), K-recency window, pilot's gate (cold-detail >= 90%; miss-rate discriminator), sanitize/echo seams, instrument family (pin, frame, verify loop).
Class-check: storm-context mechanisms treated as corroboration of class only (DISCERN write-gate L0, MAPE design-space probes, AskALCF evidence-gated admission, SELD read-side verifier); no adoption.

## Recommendation-Action Plan
1. Run the Invariance-Spectrum Report on the 24h corpus to compute decay eigenvalues per content class; verify verbatim eigenvalue >= 1.0 against the pilot gate.
2. Calibrate K using spectral elbow method on the recurrence stream (currently K=10 carry 17.9%; cross-request carry 100%).
3. Implement the Resonance Detector as a harness-AB variant: probe at shifted cadences to detect correlation with the longcat-404 rotation.
4. Extend the three-contour battery with the Eigenvector Bookkeeper: track projection error per class through the sanitize seam.

## Next Steps-Exploration
- Un-park the long-session recurrence ground (needs a successful long-session transcript).
- Port the full 35-cell suite to the bundle (currently 12 cells cover the named properties).
- Wire the read action through the gateway surface (F5 gap; installed runtime registers read, session schema does not).
- Answer PR #12831's rationale in the child (E6).

## Artifact

### MAP matrix
| # | Asserted | Status | Basis |
|---|---|---|---|
| M1 | Verbatim content class has eigenvalue ~1.0 under read-restored harness | PENDING | Invariance-Spectrum Report on 24h corpus (empirical half-life 0.484/0.573, 1.00×75 verbatim from half-life study) |
| M2 | K-window acts as largest-eigenvalue filter on recency stream | PENDING | Spectral elbow calibration on recurrence data (K=10 carry 17.9%) |
| M3 | Fleet cadence resonance detectable via harness-AB | PENDING | A/B probe at shifted cadences vs longcat-404 rotation pattern (all 24h failures = NotFoundError on meituan/longcat-2.5:free) |
| M4 | Read-restore eigenvector bookkeeper tracks sanitize projection error | PENDING | Three-contour battery extension (current 36/36 cells; add per-class projection error) |

### OWED register
| Item | Description | Outcome |
|---|---|---|
| REFS2-3-EIGEN.md | HEAD pre-read packet (member wall after opening) | Loaded (opening + transfer hooks used; body not invented) |
| VERIFICATION-PILOT-KIT-THREE-CONTOURS-20261127.md | Kitted context 1 | Loaded |
| IMPROVEMENT-MATRIX-20261127.md | Kitted context 2 | Loaded |
| BATTERY-README.md | Kitted context 3 | Loaded |
| FINDINGS-PILOT-KIT-ON-OUR-LAYER-20261127.md | Kitted context 4 | Loaded |
| steer/trinity-eigen.md | Steer channel | Loaded (no steer at launch) |
| pin-framework | Mandatory skill | Registered (file reads as proxy for load; no skill_view available) |
| investigation-documentation | Mandatory skill | Registered |
| agent-work-review | Mandatory skill | Registered |
| defect-forensics | Mandatory skill | Registered |
| aces-harness-probes | Mandatory skill | Registered |
| krecency-instrument | Mandatory skill | Registered |

### Contradiction flags
- FLAG-C1: Installed read is spec-2 (no lock; atomic rename safety) while #141876 child ships spec-1 (lock-holding). Status: class mismatch, not receipt conflict. Both shapes verified in field. Basis: F3/F4 in FINDINGS-PILOT-KIT-ON-OUR-LAYER-20261127.md + kvnloo 7211318206.
- FLAG-C2: This session's tool surface exposes no read action, while the installed memory_tool.py registers it (L119/L412). Status: surface gap, not contradiction. Basis: F5 in FINDINGS-PILOT-KIT-ON-OUR-LAYER-20261127.md.
- No contradictions between REFS2-3-EIGEN.md packet and kitted context.

## ENRICHMENT-BY-solar (round A)
Lens packet: REFS2-1-CONDITIONAL (member wall, head-distilled) — P(A|B) = P(A∩B)/P(B); conditioning replaces the sample space with B; posterior redistributes mass by evidence; python tip: filter-then-measure (measure rates on the conditioned rows before quoting whole-corpus rates). Three genuine additions, all grounded in the target's own M2/K-window claim and its recorded flags.

**E1 — The K-window claim is itself a conditional; the quoted rate is not it (extends candidate C2).** M2 quotes whole-run rates — K=10 carry 17.9%, cross-request carry 100% — as if they were the K-window effect. But the K-window filter IS the conditioning event P(correct | literal in window). The 17.9% is P(correct ∩ tap), which includes non-taps; the 100% cross-request figure is an unconditioned denominator artifact. Filter-then-measure: restrict the recurrence stream to rows where the literal was inside the K-window, THEN measure correctness. These are two distinct statistics and both must be reported; quoting the whole-run rate as the conditional is the "quote the unconditioned rate" error. Structurally, "in-window" is a function of anchor age — a stale anchor can never be in-window — so the K-window claim is conditionally dependent on anchor recency, which the eigenvalue framing (largest-eigenvalue on recency) assumes but never states.

**E2 — New discriminator: miss-rate conditioned on topic last-touch age (the whole-run rate hid the failure).** The pilot gate "cold-detail >= 90%" is a whole-corpus quote that hides the failure. Split the corpus by the topic anchor's last-touch age into "anchor-cold" (last touch older than K epochs) and "in-window" (last touch within K), then report P(miss | anchor-cold) and P(miss | in-window) as separate rows, filter-then-measure on the conditioned rows. Ground it in the real failure signature: all 24h failures were NotFoundError on meituan/longcat-2.5:free — those are almost certainly the anchor-cold rows. A single whole-run miss rate cannot separate "the corpus is hard" from "anchor-cold taps fail"; the conditional does.

**E3 — Divided gate: read-gate outcomes conditioned on action (read vs write), not pooled.** The target records (FLAG-C2 / F5) that the session surface exposes no read action while the installed memory_tool.py registers it (L119/L412). The "read-restored harness" measurement behind M2 is only valid when the read action is actually available — when it is blocked, "read-restored" degenerates to write-only. The proper gate is a 2×2 by action × window-age: measured P(correct) separately for read-available/read-blocked × in-window/anchor-cold. The existing 17.9% pools all four cells and therefore cannot support "K acts as the window filter."

**E4 — Python-mechanics note (filter-then-measure).** Any rate quoted from the corpus must be computed as filtered-row statistics — e.g. df[df.anchor_age > K].mean() / df[df.window_hit].correct.mean() — never as a whole-corpus rate. Apply this to M1 (verbatim eigenvalue), M2 (K-window), and the miss-rate discriminator of E2.

**Contradictions flagged.**
- FLAG-C3: M2 states K=10 carry 17.9% as a whole-corpus rate, but the 100% cross-request carry shows the denominator is the full corpus; the number therefore cannot support "K acts as the window filter" without the conditioned base. Status: statistical gating error, flagged before the instrument is implemented. It conflicts with the K-window claim as a conditional unless E1/E2 are adopted.
