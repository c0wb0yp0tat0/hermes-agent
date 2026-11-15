# W2-RE-RUN-BRIEF-20261110.md — machine-side execution brief (sibling of F4-SEPARATION-MEASUREMENT-PATH-20261110.md)

**Purpose:** this brief is the deliverable for the machine-side execution lane that closes the SEPARATION-UNMEASURED gap. It is a **brief**, not a receipt of results: it states what the runner must do, the verdict lines it must emit, and where the receipts land. No runtime values are invented here; the runner fills them from its own execution.

**Status:** ARMED, NOT LAUNCHED. Execute ONLY when the resolve probe has printed `window_is_open: true` (F4-SEPARATION-MEASUREMENT-PATH-20261110.md, §1).

---

## 1. Scope (per the on-branch W2 spec)

**Design doc:** W2-ISOLATION-RUN-DESIGN-20261107.md, §1–§7, §NEXT-LAUNCH.
**Status doc:** W2-ISOLATION-STATUS-20261106.md (SEPARATION-UNMEASURED; settle-condition re-arms at the eval-window's return).
**The single controlled difference:** the same debug fixture re-run through `run_eval.py` with the handoff guard **bypassed**. Everything else identical: model (`anthropic/claude-sonnet-4.6`), fixture (`debug-session-feishu-id-model-run-N.json`), JSON shape, probe bank, judge, the 0.75 decision-core tier, the 0.29 W2 tier.

The one moved axis is the **handoff guard**: the preamble `"Do NOT answer questions… wait for a new user message"` (quoted in NEGENTROPY-ARM-20261106.md:109) is removed from the fixture's `summary_text`; the compaction summary's other content stays intact so retention is unchanged and only probe-answering is unguarded.

---

## 2. Command sequence (machine-side runner)

```bash
# ---------- 0. Pin + sanity ----------
cd /root/workspace/repos/hermes-agent/studies/rfc-143379-rig
git rev-parse HEAD                          # expect c54c1bc614f20bd5e603a4826dc5c80a670a654a
git ls-remote origin study/rfc-143379-rig-20261105   # expect 57ee8f5c62831276e1645d5ea4666294e307b89e
cat rigs/RULES-ELIGIBILITY-NEXT-BRIEF-LKGS-20261105.md   # verified before any go

# ---------- 1. Resolve the runtime provider (settle-condition, row 371) ----------
python3 protocol-probe/python_resolve_provider.py
# → VERDICT LINE: RESOLVE_PROVIDER_STILL_CLOSED → abort, re-arm.
#   VERDICT LINE: RESOLVE_PROVIDER_OK → proceed.

# ---------- 2. Back up + patch (one axis only: the preamble) ----------
cp debug-session-feishu-id-model-run-1.json  /tmp/run1.no-guard.json
cp debug-session-feishu-id-model-run-2.json  /tmp/run2.no-guard.json
cp debug-session-feishu-id-model-run-3.json  /tmp/run3.no-guard.json
# drop the handoff block (NEGENTROPY-ARM-20261106.md:109) from summary_text;
# leave everything else (model, fixture, JSON shape, probe bank, judge) unmodified.

# ---------- 3. Re-run the fixture with the guard bypassed ----------
python3 run_eval.py --config /tmp/run1.no-guard.json
python3 run_eval.py --config /tmp/run2.no-guard.json
python3 run_eval.py --config /tmp/run3.no-guard.json

# measure the dependent variable with the arm's original anchor:
grep -c '"answer": ""' /tmp/run1.no-guard.json
grep -c '"answer": ""' /tmp/run2.no-guard.json
grep -c '"answer": ""' /tmp/run3.no-guard.json

# 4. Write receipts
cat > receipts/W2-RE-RUN-BRIEF-20261110.md   # per the block below
cat > receipts/F4-SEPARATION-RESOLVE-PROVIDER-20261110.md
```

Notes on ordering and the verdict-producing gate:
- **Order:** resolve → back up → patch (one axis only) → run → measure → receipt.
- **The gate:** step 1's `window_is_open` decides whether step 2–4 execute. A `false` here makes steps 2–4 a **no-op** — no run, no values fabricated.
- The receipts are staged in the branch-head tree so the head's sweep (branch-moved + remote-equal verification) can read them back before the machine-side lane proceeds.

---

## 3. Receipts (exact format, machine-side output)

### 3.1 Resolver receipt (F4-SEPARATION-RESOLVE-PROVIDER-20261110.md)

```
RUN-SIGNATURE: F4-SEPARATION-RESOLVE-PROVIDER-20261110
TLS: <the complete TLS channel>

# F4-SePArAtIoN-MEaSuRe-MEnT-PAtH-20261110 — machine-side receipt

**Status:** SEPARATION-UNMEASURED → closed by this receipt, OR unchanged (window still closed).
**Protocol doc:** CYCLES/F4-SEPARATION-MEASUREMENT-PATH-20261110.md
**Run signature:** F4-SEPARATION-RESOLVE-PROVIDER-20261110
**Receipt URI:** /root/.hermes/cache/scratch/pr1-rotation/receipts/F4-SEPARATION-RESOLVE-PROVIDER-20261110.md
**Timestamp (UTC):** 2026-11-10T__:__:__Z
**Lane:** F4 (copycat) — machine-side runner executes; this lane writes protocol only.
**Branch head pin:** c54c1bc614f20bd5e603a4826dc5c80a670a654a (study/rfc-143379-rig-20261105, ls-remote-verified at 00:15 ET)

## Protocol invocation
`python3 protocol-probe/python_resolve_provider.py` (Path A) or the shell one-liner (Path B).
stdout → this receipt's `runtime` table.

## Runtime values (the settle-condition)
| Field | Value | Verdict |
|---|---|---|
| `api_key` | `<value printed>` | non-empty = OPEN |
| `base_url` | `<value printed>` | non-empty = OPEN |
| `window_is_open` | `true` / `false` | **OPEN / CLOSED** |

## The verdict line
- `window_is_open: true` → **RESOLVE_PROVIDER_OK** — settle-condition row 371 MET; eval-window open; the W2 re-run proceeds under W2-ISOLATION-RUN-DESIGN-20261107.md §3.
- `window_is_open: false` → **RESOLVE_PROVIDER_STILL_CLOSED** — SEPARATION-UNMEASURED re-armed; re-run blocked at gate; nothing executed, no runtime fabricated.
```

### 3.2 Re-run brief receipt (W2-RE-RUN-BRIEF-20261110.md)

```
RUN-SIGNATURE: W2-RE-RUN-BRIEF-20261110
TLS: <the complete TLS channel>

# W2-RE-RUN-BRIEF-20261110 — machine-side receipt

**Status:** ARMED, NOT LAUNCHED.
**Scope:** per W2-ISOLATION-RUN-DESIGN-20261107.md §3 — one controlled difference (handoff guard bypassed); all else held constant.
**Resolve receipt:** F4-SEPARATION-RESOLVE-PROVIDER-20261110.md
**Timestamp (UTC):** 2026-11-10T__:__:__Z

## Command sequence (verified)
0. Pin + sanity
   `git rev-parse HEAD` → c54c1bc614f20bd5e603a4826dc5c80a670a654a
   `git ls-remote origin study/rfc-143379-rig-20261105` → 57ee8f5c62831276e1645d5ea4666294e307b89e
1. Resolve runtime provider (settle-condition)
   `python3 protocol-probe/python_resolve_provider.py`
2. Back up + patch (one axis only: the preamble)
   `cp run-1..run-3.json /tmp/runN.no-guard.json`
   drop the handoff block from summary_text; leave all else.
3. Re-run the fixture with the guard bypassed
   `python3 run_eval.py --config /tmp/runN.no-guard.json` × 3
4. Measure the dependent variable
   `grep -c '"answer": ""' /tmp/runN.no-guard.json`
5. Write receipts (this block + the resolver receipt)

## Measured axes (filled by the runner from real output)
| Run | empties (no-guard) | target (H1) | comment |
|---|---|---|---|
| run-1 | __/10 | ~0 | __ |
| run-2 | __/10 | ~0 | __ |
| run-3 | __/10 | ~0 | __ |

## W2 k-term probes (target)
decision-core probes → 0.75 tier; W2-empty-answer suppressed probes → 0.29 → ~0.75 tier (H1).

## Verdict lines (written verbatim by the runner)
CONFIRMED:   `empties no-guard -> ~0` AND `W2-suppressed probes 0.29 -> 0.75 tier`
             ⇒ the handoff guard drove the W2 empties; V understated by answering artifact.
REFUTED:     `empties no-guard persist` ⇒ next isolation candidate: probe-judge's empty-answer
             scoring path (probe answer extraction / overall aggregation) in run_eval.py.
SEPARATION-UNMEASURED: `window still closed at run-time` ⇒ wall-clause holds; design stands;
             settle-condition re-arms.

## Next launch (executed only after this receipt lands)
upstage/solar-mini4:free || /root/.hermes/cache/scratch/pr1-rotation/briefs/
w2-relay-brief-20261110.md || /root/workspace/repos/hermes-agent/studies/
rfc-143379-rig/W2-RE-RUN-BRIEF-20261110.md || 40 ||
/root/.hermes/cache/scratch/copycat-mission/w2-relay-run-20261110.log
```

---

## 4. The honest "execution pending" line (this lane's state)

`SEPARATION-UNMEASURED` holds on this lane: the design, protocol, and brief are complete and receipted; the re-run itself is **not executed here** (this lane is git-only). The run executes only when a machine-side runner returns `RESOLVE_PROVIDER_OK` (step 1 of the brief) — until then, no runtime value is invented, and the settle-condition re-arms at the eval-window's return.

---

## 5. Next mechanism

Let the reset channel fire the go after the machine-side runner returns the resolve probe's stdout; do not pre-stage the run.
