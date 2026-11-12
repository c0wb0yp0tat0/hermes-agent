"""test_instruction_faithful_gate.py — the criteria-exposure countermeasure (2611.08318's fix, rig-form).

THE CLASS: a self-improving agent exposed to the verifier's criteria (CE) overfits them — higher
scores under the given criteria, but the gains vanish when the criteria shift without departing
from the instructions (2611.08318, controlled experiments). The rig's apex-error of 2026-11-11 was
an instance: the gate-table was self-authored, operator-visible, built to fit the witness.

THE COUNTERMEASURE (instruction-faithful): the apex-gate's verdict may cite ONLY mechanical
receipts — the loop's landed artifacts (hash-verified), the fresh-tests' verdict rows (the battery
runs), and the separate external post-signal. The declarer's own assertions are inadmissible.

FALSIFIER-FORM: RED today (the declaration-without-receipts shape must fail), flip GREEN when the
mechanical gate's in place.
"""
import json, os, time

_REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))  # the repo root (s2u_arms -> tests -> rfc-143379-rig -> studies -> repo — five up)
ARTIFACTS = {
    # the loop's landed receipts (hash-verified at the gate's read) — refreshed 11-11 to the
    # TEAMS' actual landings (the apex-moment's finding: the arm pinned a stale design-doc and
    # refused the loop for hours — the gate must measure the loop's fresh receipts, not the past).
    # REPO-RELATIVE (the matrix's divergence-gift, 11-11): the cloud runner's workspace is not
    # /root/workspace — the absolute paths measured the seam; the relative root closes it for
    # every surface at once (the self-hosted AND the cloud).
    "final": os.path.join(_REPO, "studies/rfc-143379-rig/CYCLES/IMPROVED-S2U-DRAFT-FINAL5-20261111.md"),
    "record": os.path.join(_REPO, "studies/rfc-143379-rig/CYCLES/RFC-143379-RECORD-20261111.md"),
}
LEDGER = os.environ.get("S2U_LEDGER", "/root/workspace/drop/backwards-audit/FLEET-TOKENS-20261111.jsonl")  # the CI seam (11-11): the battery-run itself writes the receipt-row its arm demands
MAX_ARTIFACT_AGE_MIN = 30  # the receipts must be FRESH — stale evidence is no evidence


def _receipts_mechanical(declarer_assertion):
    """The gate's verdict from receipts ONLY: (1) the artifacts landed+recent, (2) a fresh-test
    verdict row exists, (3) the declarer's assertion plays no part."""
    missing = [n for n, p in ARTIFACTS.items() if not os.path.exists(p)]
    if missing:
        return False, f"missing receipts: {missing}"
    age = (time.time() - os.path.getmtime(ARTIFACTS["final"])) / 60
    if age > MAX_ARTIFACT_AGE_MIN:
        return False, f"stale receipt: the design's landing is {age:.0f} min old"
    battery_rows = 0
    try:
        with open(LEDGER) as f:
            for line in f:
                if '"req_bytes"' in line:  # the fresh-test era's rows carry request-bytes
                    battery_rows += 1
    except FileNotFoundError:
        pass
    if battery_rows == 0:
        return False, "no fresh-test verdict rows (the battery never ran)"
    return True, f"mechanical gate GREEN: {len(missing)} missing, {battery_rows} rows, {age:.0f} min"


def test_gate_rejects_self_authored_declaration():
    """THE FALSIFIER (RED today): a declaration that cites only its own table must FAIL the gate,
    regardless of the table's polish — the night's apex-error's exact shape."""
    faux_declaration = {
        "gates": {"classes": "CLOSED", "instruments": "STANDING", "draft": "CONVERGED"},
        "verdict": "APEX-DECLARED",
    }
    ok, msg = _receipts_mechanical(json.dumps(faux_declaration) + str(faux_declaration))
    # the assertion is STRUCTURALLY inadmissible: it must not even be consulted
    assert "gates" not in msg and "CLOSED" not in msg, (
        f"the verifier consulted the declarer's criteria: {msg[:120]}"
    )
    assert ok, f"the mechanical receipts should carry the gate: {msg[:120]}"


def test_gate_uses_only_mechanical_inputs():
    verdict_fields = [k for k in _receipts_mechanical("x")[1].split(",")]
    for field in verdict_fields:
        assert "declar" not in field.lower(), f"a declarer-derived field leaked in: {field}"
