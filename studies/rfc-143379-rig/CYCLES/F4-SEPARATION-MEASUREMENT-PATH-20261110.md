# F4-SEPARATION-MEASUREMENT-PATH-20261110 — the MEASUREMENT PROTOCOL + the MACHINE-SIDE BRIEF

**Lane:** F4 (copycat — SPEC/PROTOCOL lane). This lane does NOT execute the run. The experiment it specifies is the W2 isolation re-run (the "single controlled difference," probe-answering isolated from the handoff guard). This lane writes two artifacts, on demand and re-executable by a python/shell-reach machine-side lane:

1. **THE MEASUREMENT PROTOCOL** — exactly what must be executed to close the SEPARATION-UNMEASURED gap: the import path for `resolve_runtime_provider`, the command to print the runtime values, the expected output shape, and the exact receipt format the machine-side run must produce (`named JSON/MD` + timestamp + run signature).
2. **THE W2-RE-RUN's BRIEF** — a complete, self-contained brief for the machine-side execution lane: command sequence, receipt path, pass/fail verdict lines, and the re-run's scope, per the on-branch W2 spec.

---

## 0. Standing state (SEPARATION-UNMEASURED)

- **Status:** SEPARATION-UNMEASURED (W2-ISOLATION-STATUS-20261106.md, Receipt 3 / run_eval.py:81; W2-ISOLATION-RUN-DESIGN-20261107.md, §5(c)).
- **The wall:** eval-runtime LLM-window CLOSED — `run_eval.py` gates on `runtime.get("api_key") and runtime.get("base_url")`; `api_key`/`base_url` are absent at the machine boundary. Run cannot execute; the design is the deliverable until the window opens.
- **The lane's honesty band:** the exact line number of the handoff preamble inside the fixture's `summary_text` ("debug run-1 line 10") is carried from the arm's receipt and was NOT re-counted by this lane; if a single-check shows it differs, the arm's quote stands and this row is marked UNVERIFIED. No other receipt failed the single-check.
- **Gate:** nothing public without the user's word. Fork-only; no execution here.

---

## 1. THE MEASUREMENT PROTOCOL

### 1.1 What the protocol closes

The protocol closes the one runtime value the git-only lane could not observe: **does `resolve_runtime_provider` return a non-empty `api_key` or `base_url`?** — the settle-condition row 371 of the omnibus audit. A non-empty return = the eval-window is open and the re-run is unblocked; an empty return = SEPARATION-UNMEASURED persists.

### 1.2 Import path for `resolve_runtime_provider`

Two supported import paths (one python-one shell). Whichever is present in the machine-side environment, use it; the receipt records BOTH the invoked path and the resolved values.

**Path A — python (recommended for a typed contract):**

```python
# protocol-probe/python_resolve_provider.py
import importlib, json, sys, datetime, hashlib

def resolve_module():
    candidates = [
        "hermes_compression_eval.runtime.provider",   # the receipted module (env + cwd root)
        "hermes_compression_eval.run_eval",           # fallback surface (run_eval.py hosts resolve_runtime_provider)
    ]
    for name in candidates:
        try:
            return importlib.import_module(name)
        except ModuleNotFoundError:
            continue
    return None

mod = resolve_module()
if mod is None:
    print(json.dumps({
        "protocol": "F4-SEPARATION-MEASUREMENT-PATH",
        "command": "import resolve_runtime_provider via hermes_compression_eval.runtime.provider (or run_eval fallback)",
        "status": "MODULE_NOT_FOUND",
        "imported": [],
        "runtime": {},
        "evidence": "python3 cannot import resolve_runtime_provider from any candidate surface",
    }, indent=2))
    sys.exit(2)

probe = mod.resolve_runtime_provider
if not callable(probe):
    print(json.dumps({
        "protocol": "F4-SEPARATION-MEASUREMENT-PATH",
        "command": "import resolve_runtime_provider via hermes_compression_eval.runtime.provider (or run_eval fallback)",
        "status": "NOT_CALLABLE",
        "imported": [name for name in ["hermes_compression_eval.runtime.provider", "hermes_compression_eval.run_eval"] if name in sys.modules],
        "runtime": {},
        "evidence": f"module imported but resolve_runtime_provider is not callable (type={type(probe).__name__})",
    }, indent=2))
    sys.exit(3)

runtime = probe(debug="./rungs/fixture-deep-compaction-real.json")
if not isinstance(runtime, dict):
    runtime = {"raw": runtime, "note": f"probe returned non-dict of type {type(runtime).__name__}"}

print(json.dumps({
    "protocol": "F4-SEPARATION-MEASUREMENT-PATH",
    "command": "import resolve_runtime_provider via hermes_compression_eval.runtime.provider (or run_eval fallback)",
    "status": "CALLED",
    "module_imported": [name for name in ["hermes_compression_eval.runtime.provider", "hermes_compression_eval.run_eval"] if name in sys.modules],
    "runtime": runtime,
    "window_is_open": bool(runtime.get("api_key") or runtime.get("base_url")),
}, indent=2))
```

**Path B — shell (one-liner, minimal deps):**

```bash
python3 - <<'PY'
import json, sys
sys.path.insert(0, "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig")
try:
    from hermes_compression_eval.runtime.provider import resolve_runtime_provider  # receipted surface
    mod = "hermes_compression_eval.runtime.provider"
except Exception:
    try:
        from hermes_compression_eval.run_eval import resolve_runtime_provider  # run_eval fallback
        mod = "hermes_compression_eval.run_eval"
    except Exception as e:
        print(json.dumps({"protocol":"F4-SEPARATION-MEASUREMENT-PATH","command":"import resolve_runtime_provider","status":"MODULE_NOT_FOUND","imported":[],"runtime":{},"evidence":str(e)}, indent=2)); sys.exit(2)
rt = resolve_runtime_provider(debug="./rungs/fixture-deep-compaction-real.json")
print(json.dumps({"protocol":"F4-SEPARATION-MEASUREMENT-PATH","command":"import resolve_runtime_provider","status":"CALLED","module_imported":[mod],"runtime":rt,"window_is_open":bool(rt.get("api_key") or rt.get("base_url"))}, indent=2))
PY
```

### 1.3 Expected output shape

A single `stdout` JSON object of the shape below. `window_is_open: true` is the **settle-condition** trigger (row 371); `window_is_open: false` reconfirms SEPARATION-UNMEASURED and re-arms the re-run.

```json
{
  "protocol": "F4-SEPARATION-MEASUREMENT-PATH",
  "command": "import resolve_runtime_provider via hermes_compression_eval.runtime.provider (or run_eval fallback)",
  "status": "CALLED",
  "module_imported": ["hermes_compression_eval.runtime.provider"],
  "runtime": {
    "api_key":   "<non-empty string>",
    "base_url":  "<non-empty string>"
  },
  "window_is_open": true
}
```

Expected values: **`api_key`** = the OpenAI key (the receipted run-side arm asserts the eval-window's returned key matches this), **`base_url`** = the endpoint the eval-runtime is pinned to at the wall's return; both non-empty. If either is missing, the field value is `null`/`""` and `window_is_open: false`.

### 1.4 Receipt format (machine-side run)

The machine-side lane MUST write the receipt to:

```
/root/.hermes/cache/scratch/pr1-rotation/receipts/F4-SEPARATION-RESOLVE-PROVIDER-20261110.md
```

(forked study branch tree; the parent dir is the seeded receipt bucket, so the file appears in the git-visible witness set once staged — the bucket is inside the branch head so it must be `git add`'d with the protocol doc).

Content (verbatim JSON table, then rendered MD):

```
RUN-SIGNATURE: F4-SEPARATION-RESOLVE-PROVIDER-20261110
TLS: { "the entire TLS channel" }
```

```markdown
# F4-SePArAtIoN-MEaSuRe-MEnT-PAtH-20261110 — machine-side receipt

**Status:** SEPARATION-UNMEASURED → closed by this receipt, OR unchanged (window still closed).
**Protocol doc:** CYCLES/F4-SEPARATION-MEASUREMENT-PATH-20261110.md
**Run signature:** F4-SEPARATION-RESOLVE-PROVIDER-20261110
**Receipt URI:** /root/.hermes/cache/scratch/pr1-rotation/receipts/F4-SEPARATION-RESOLVE-PROVIDER-20261110.md
**Timestamp (UTC):** 2026-11-10T__:__:__Z
**Lane:** F4 (copycat) — machine-side runner executes; this lane writes protocol only.
**Branch head pin:** c54c1bc614f20bd5e603a4826dc5c80a670a654a (study/rfc-143379-rig-20261105, ls-remote-verified at 00:15 ET)

## Protocol invocation
`python3 /root/workspace/repos/hermes-agent/studies/rfc-143379-rig/protocol-probe/python_resolve_provider.py`
(or the shell one-liner, Path B). stdout → this receipt's `runtime` table.

## Runtime values (the settle-condition)
| Field | Value | Verdict |
|---|---|---|
| `api_key` | `<value printed>` | non-empty = OPEN |
| `base_url` | `<value printed>` | non-empty = OPEN |
| `window_is_open` | `true` / `false` | **OPEN / CLOSED** |

## The verdict line
- If `window_is_open: true` → **RESOLVE_PROVIDER_OK** — settle-condition row 371 MET; eval-window open; the W2 re-run proceeds under W2-ISOLATION-RUN-DESIGN-20261107.md §3.
- If `window_is_open: false` → **RESOLVE_PROVIDER_STILL_CLOSED** — SEPARATION-UNMEASURED re-armed; re-run blocked at gate; nothing executed, no runtime fabricated.
```

Notes on the receipt:
- The filename is the **run signature** — no run output exists until a real machine-side execution returns, so no value is invented here; the machine-side lane fills the `<value printed>` slots from its own stdout.
- The receipt is staged with the protocol doc and committed+pushed with the W2 re-run's brief (`W2-RE-RUN-BRIEF-20261110.md`), so the machine-side witness lives in the same tree head for the head's sweep to verify.

---

## 2. THE W2-RE-RUN'S BRIEF (machine-side execution)

### 2.1 Self-contained brief

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
W2-RELAY-BRIEF-20261110 — machine-side execution lane
Status: ARMED, NOT LAUNCHED. Execute ONLY when resolve_runtime_provider
prints window_is_open: true (F4-SEPARATION-MEASUREMENT-PATH-20261110.md §1).
If the resolve probe still prints window_is_open: false, do NOT execute.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PURPOSE
  Probe the single controlled difference in W2-ISOLATION-RUN-DESIGN-20261107.md §3:
  the same debug fixture re-run through run_eval.py with the handoff guard BYPASSED,
  everything else identical (model, fixture, JSON shape, probe bank, judge).
  The handoff preamble "Do NOT answer questions… wait for a new user message"
  (debug run-1 summary_text line 10, quoted in NEGENTROPY-ARM-20261106.md:109)
  is removed; the compaction summary's other content stays intact. Retention is
  unchanged; only probe-answering is unguarded.

TASK
  1. Confirm window open
     - python3 protocol-probe/python_resolve_provider.py
     - VERDICT LINE: RESOLVE_PROVIDER_STILL_CLOSED → abort, re-arm.
     - VERDICT LINE: RESOLVE_PROVIDER_OK → proceed.

  2. Re-run the debug fixture with the guard bypassed
     - Keep the exact debug fixture at its pinned argv path:
         /root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-1.json
         /root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-2.json
         /root/.hermes/cache/scratch/pr1-rotation/ladder-results/debug-session-feishu-id-model-run-3.json
     - Patch ONLY the preamble: in the run's config JSON, drop the handoff block
       (NEGENTROPY-ARM-20261106.md:109) from summary_text; leave everything else
       (model, fixture, JSON shape, probe bank, judge) unmodified.
     - Invoke run_eval.py with the same env/cwd/args as the original run; the guard
       at run_eval.py:81 sees a populated runtime and no longer blocks at the wall.

  3. Measure per the design's measured axes
     DEPENDENT VARIABLE (the design's target): `'"answer": ""` count per run.
       Example: debug run-1 → 2/10 empty answers under the guard; under H1 the
       no-guard re-run moves this toward ~0. Use the same anchor as §2 of the
       arm (git grep -c '\"answer\": \"\"') over the re-run JSONs.

     W2 k-term probes (NEGENTROPY-SWEEP-B-KTERM-20261106.md): decision-core probes
       keep at 0.75 tier; W2-empty-answer suppressed probes keep at 0.29 tier;
       the no-guard re-run must move the W2-suppressed probes from the 0.29 tier
       toward the 0.75 tier (H1), i.e., the exact-phrase retention for the six
       suppressed probes must become non-zero.

  4. Record receipts
     - Write the per-run measured table (run-1-no-guard: empties X/10; run-2: Y/10;
       run-3: Z/10; W2 probe rates) to the run's log.
     - The run-side arms the re-run at the eval-window's return;
       the head's sweep verifies the landing (branch-moved + remote-equal).

PASS/FAIL VERDICT LINES (written verbatim to the run log and the receipt)
  CONFIRMED:   `empties no-guard -> ~0` AND `W2-suppressed probes 0.29 -> 0.75 tier`
               ⇒ the handoff guard drove the W2 empties; the V-understatement's
               mechanism is named. The 0.29 tier's suppression is an answering
               artifact, not a retention loss.
  REFUTED:     `empties no-guard persist` ⇒ another driver: the design names the
               next isolation candidate — the probe-judge's empty-answer scoring
               path (probe answer extraction / overall aggregation) in run_eval.py,
               isolated next with the judge's empty-answer rule relaxed.
  SEPARATION-UNMEASURED: `window still closed at run-time` ⇒ the wall-clause holds
               (F4 §0); the design stands as the spec; the settle-condition re-arms.

SCOPE (per the on-branch W2 spec)
  - Holds constant: model anthropic/claude-sonnet-4.6 (debug-class), fixture
    debug-session-feishu-id-model, JSON shape, probe bank, judge, the 0.75 decision-
    core tier, the 0.29 W2 tier.
  - Moves exactly one axis: the handoff guard (preamble removed / left intact).
  - NOT executed by this lane: the run itself. This brief is the spec for the
    machine-side lane; no runtime values are invented here.

RECEIPT PATH
  /root/.hermes/cache/scratch/pr1-rotation/receipts/W2-RE-RUN-BRIEF-20261110.md
  (staged with this brief; the run's own output lands inside this file).

NEXT-LAUNCH
  upstage/solar-mini4:free || /root/.hermes/cache/scratch/pr1-rotation/briefs/
  w2-relay-brief-20261110.md || /root/workspace/repos/hermes-agent/studies/
  rfc-143379-rig/W2-RE-RUN-BRIEF-20261110.md || 40 ||
  /root/.hermes/cache/scratch/copycat-mission/w2-relay-run-20261110.log
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.2 Machine-side command sequence (from the brief)

```bash
# 0. Pin + sanity
cd /root/workspace/repos/hermes-agent/studies/rfc-143379-rig
git rev-parse HEAD                      # expect c54c1bc614f20bd5e603a4826dc5c80a670a654a
git ls-remote origin study/rfc-143379-rig-20261105  # expect 57ee8f5c62831276e1645d5ea4666294e307b89e
cat rugs/RULES-ELIGIBILITY-NEXT-BRIEF-LKGS-20261105.md   # verified before any kickoff

# 1. Resolve the runtime provider (the settle-condition, row 371)
python3 protocol-probe/python_resolve_provider.py
# VERDICT LINE: RESOLVE_PROVIDER_STILL_CLOSED → abort, re-arm.  RESOLVE_PROVIDER_OK → proceed.

# 2. Back up + patch (one axis only: the preamble)
cp debug-session-feishu-id-model-run-1.json  /tmp/run1.no-guard.json
cp debug-session-feishu-id-model-run-2.json  /tmp/run2.no-guard.json
cp debug-session-feishu-id-model-run-3.json  /tmp/run3.no-guard.json
# drop the handoff preamble from summary_text (NEGENTROPY-ARM-20261106.md:109); leave all else.

# 3. Invoke run_eval.py with the guard bypassed (same env/cwd/args as the original run)
python3 run_eval.py --config /tmp/run1.no-guard.json   # ... run-2, run-3 likewise
# capture the per-run empties query with the arm's original grep:
grep -c '"answer": ""' /tmp/runN.no-guard.json

# 4. Write receipts
cat > receipts/W2-RE-RUN-BRIEF-20261110.md   # per the brief's receipt block
cat > receipts/F4-SEPARATION-RESOLVE-PROVIDER-20261110.md
```

Notes on the receipt category, command ordering, and the verdict-producing gate:
- Order: resolve → back up → patch (one axis only) → run → measure → receipt.
- The verdict-producing gate is the `window_is_open` field from step 1; a `false` here makes steps 2-4 a **no-op** (no run executed, no values fabricated).
- The receipt files are placed in the branch-head tree so the head's sweep (git log / ls-remote verify) can read them back before the machine-side lane proceeds.

---

## 3. The honest "execution pending" line

`SEPARATION-UNMEASURED` holds on this lane: the design (W2-ISOLATION-RUN-DESIGN-20261107.md §1–§7) is complete and receipted; the protocol (§1) and the machine-side brief (§2) are written and re-executable; the run itself awaits the eval-window opening. This lane cannot execute the run (git-only), so the honest verdict is **protocol written, execution pending machine-side** — no runtime value is invented, and the settle-condition re-arms whenever the eval-window returns.

---

## 4. Status register (receipts, never claims)

| # | Item | State |
|---|---|---|
| A | W2-ISOLATION-RUN-DESIGN-20261107.md (on-branch spec) | read, quoted as found |
| B | W2-ISOLATION-STATUS-20261106.md (SEPARATION-UNMEASURED verdict) | read, Receipt 3 / run_eval.py:81 |
| C | SEPARATION-UNMEASURED rows in sweep files | confirmed present (grep on branch head) |
| D | `resolve_runtime_provider` callback within run_eval.py | NOT re-hunted by this lane (git only; python import validated by the machine-side runner) |
| E | Exact preamble line number in debug run-1 `summary_text` | UNVERIFIED (arm's "debug run-1 line 10" stands; noted in §0) |
| F | Protocol + brief | WRITTEN to CYCLES/F4-SEPARATION-MEASUREMENT-PATH-20261110.md + sibling W2-RE-RUN-BRIEF-20261110.md; staged; execution pending machine-side |

---

## 5. Next mechanism

Let the reset channel fire the go after the machine-side runner returns the resolve probe's stdout; do not pre-stage the run.
