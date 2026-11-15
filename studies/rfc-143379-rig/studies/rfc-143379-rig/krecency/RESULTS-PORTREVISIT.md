# RESULTS-PORTREVISIT — portability-revisit arm (re-run)

Verdict: PORTABILITY-RECURRED. Real conversation streams (mined from
/root/.hermes/sessions/request_dump_*.json, 147 dumps) DO reproduce the
synthetic 0.15-protection shape at the fused cell: none stays 0.80,
literal and literal+membership drop to 0.00 deep-minima prevalence. The
recurrence that protects in the synthetic stream IS present in real loads
(path/sha/flag literals recur across turns; recurrence rate 0.2842).

## Fused-cell table
| variant | deep-minima prevalence |
|---|---|
| none | 0.80 |
| literal | 0.00 |
| literal+membership | 0.00 |

## Stream provenance
- Source: /root/.hermes/sessions/request_dump_*.json (147 dumps, span 2026-11-04..2026-11-05).
- Mined per turn in conversation order: SHA-like, path-like, flag-like literals.
- Count: 15702 literals (sha 3194, path 9272, arg 3236); 1031 unique; 293 recurring (>=3); recurrence rate 0.2842.
- Redaction: no credentials; mined literals only (dumps' content stays on the rig).

CSV: results/portrevisit.csv
EOF