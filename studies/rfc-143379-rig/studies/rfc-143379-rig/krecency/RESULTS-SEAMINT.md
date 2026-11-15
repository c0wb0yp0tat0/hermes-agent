# RESULTS-SEAMINT.md

## Seam-Integration Arm - retention-latch on the real ground

Verdict: **LATCH-NOOP**. The literal-pin alone already carries the real conversation-streams (deep-minima prevalence 0.00), so the retention-latch's standing redundancy is named - a finding, not a failure.

| variant | deep_minima_prevalence | reserved_set_size |
|---|---|---|
| none | 0.80 | 26 |
| literal-pin | 0.00 | 26 |
| pin+retention-latch | 0.00 | 26 |

Cost-line: reserved-set size on real streams = 26 (tiny+old literals, <=6 chars). The latch does not drop prevalence below the pin-alone 0.00 (floor already reached); it is redundant on the real ground. Derived-never-injected: every knob param.
