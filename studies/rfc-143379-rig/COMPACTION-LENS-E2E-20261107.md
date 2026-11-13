# COMPACTION-LENS-E2E-20261107 — Compaction-line lens on MISSION-8H-V3

## 1. Lens reading (cold)
- Mission: MISSION-8H-V3-20261107.md (8h, 4 tracks, cycle-3 polish).
- RFC four lines per RFC-READ-20261107.md: Restore, Network, Governance, **Compaction**.
- Compaction-line real state (RFC-READ §four-lines): K-recency sweep +2.2/+1.1/+2.3pp at 4×/8×/16× (150-cycle); 300-cycle reversal 6.1% vs 9.6% baseline (−3.5pp); long-session hard gate FAIL; probe-scope confound open → neither headline certifies.

## 2. Verdict: GAPS
The mission's central track (Merge-Composition Falsification of #116673+#141876+#139606) serves the compaction-line only indirectly. It does NOT serve the compaction-line's real, blocking state: the measured reversal, the long-session gate FAIL, and the probe-scope confound.

## 3. Named gaps (missed angles)
1. **Reversal unaddressed.** 300-cycle reversal (−3.5pp) has no dedicated task; mission has no K-recency scaling probe.
2. **Long-session gate FAIL unaddressed.** No track owns re-running / un-failing the long-session hard gate; only the compose track.
3. **Probe-scope confound open.** No task to fix/replicate the probe-scope bug before re-measuring; headline still non-certifying.
4. **Anchor decay (`_augment_summary_lean` one-generation)** named by xngg1021 but not in mission tasks; empirical measurement missing.
5. **3oltan-seo's 300+ cycle hard acceptance gate** not reflected as a mission acceptance criterion.
6. **Field data (2.5-week session logs)** mentioned in RFC gaps but no sanitization/measurement task in mission.
7. **Probe-scope confound's angles**: (a) scope of measurement, (b) 4×/8×/16× window scaling, (c) 300-turn session length — none calibrated.

## 4. Value the mission DOES deliver to compaction line
- Compose track could surface seam gaps affecting compaction (#139606 interactions).
- Track D read-gate watch keeps RFC-READ consumed (includes compaction line).
- Byte-verify habit improves receipt credibility for future compaction claims.

## 5. Compose-check table (mandatory)
| Seam | #116673 | #141876 | #139606 | Compaction-line impact |
|---|---|---|---|---|
| apply-clean | conflict both ways w/ #141876 | restored read | network | indirectly |
| tests-pass | bounded read | restore | network | none direct |
| no-regression | read/patch semantics | entries+usage | chain-doc | none direct |
| receipts | need-id→task | need-id→task | need-id→task | none direct |
| compaction state | N/A | N/A | N/A | NOT covered by compose track |

## 6. Top gap
The mission never owns the compaction-line's blocking measurements (reversal, gate FAIL, probe confound) as a named track or acceptance criterion.

## FINAL SUMMARY
- file: /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/COMPACTION-LENS-E2E-20261107.md
- verdict: GAPS
- top gap: no named owner for the compaction-line's blocking measurements (300-cycle reversal, long-session gate FAIL, probe-scope confound)