# T-A RE-APEX — the write-gate's rebase (EXEC-class; landing-set only)
**Lane:** beam (copycat). **Branch:** `study/rfc-143379-rig-20261105`.
**Pins:** write-gate head `d1bdb4582cd5d16be6a6b486f696f8240c222b96`; composed head `180b13b4fc` (base `670a261c75` + #141876 `ec649ad9d0` + #116673 `60a2e15638` + read-union reconciliation).
**Deliverable:** rebased head's evidence (landing-set whitelist), artifact on branch.
**Gate line (verbatim):** "the gate: nothing public without the user's word"

## §0 Status
Preliminary — rebase operation in progress. Evidence rows to be appended after execution.

## §1 Operation plan (landing-set whitelist)
1. Re-cut write-gate's own commits off drift base `681346296c` onto composed head `180b13b4fc`.
2. Landing-set whitelist = `tools/write_gate.py` + `tests/tools/test_write_gate.py` (clean additions) + unioned `tools/memory_tool.py` hunks (gate's refusals + restored read + chain-docs) + 3 collateral conflicts resolved by union (`.github/actionlint.yaml`, `hermes_cli/observability/shared_metrics_contract.py`, `tests/tools/test_memory_tool_schema.py`).
3. Drift range `681346296c..pr-139606` (2,174 commits) EXCLUDED — not carried.
4. Rebased head = composed head + write-gate commits only.

## §2 Evidence (pending)
(to be filled)
