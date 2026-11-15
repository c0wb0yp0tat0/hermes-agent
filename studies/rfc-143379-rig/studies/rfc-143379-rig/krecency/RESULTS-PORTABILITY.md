# RESULTS-PORTABILITY — portability arm (E1)

Verdict: PORTABILITY-GAP. Real literal-streams (mined from the repo's own git log:
commit SHAs, changed paths, flag-like subject tokens; 59877 literals) do not
reproduce the synthetic 0.15-protection shape: at the fused cell (alias-on x
proximity-on) every pinning variant (none / literal / literal+membership) stays at
0.80 deep-minima prevalence. The recurrence that protects in the synthetic stream
is absent in real loads (each SHA/path is effectively unique), so exact-literal
pinning has nothing to pin.

## Real-vs-synthetic table
| variant | synthetic prevalence | real prevalence |
|---|---|---|
| none | 1.00 | 0.80 |
| literal | 0.15 | 0.80 |
| literal+membership | 0.15 | 0.80 |

## Stream provenance
- Source: `git log` of c0wb0yp0tat0/hermes-agent (commit SHAs + changed paths + --flag tokens from subjects).
- Count: 59877 literals. No hand-written curves; derived-never-injected.
- Redaction: no credentials; [REDACTED] markers (none present) retained.

CSV: results/portability.csv
EOF