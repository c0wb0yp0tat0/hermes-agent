# STAKE-TELEGRAM-20261109 — Telegram Chat-Layer Contract

**Status:** DIRECT-APPLICABLE · staging-build · 4-hour follow-up sprint
**Surface:** telegram-command-surface (chat layer)
**Scope:** operator-prompt templates · evidence-cadence schedule · handoff format spec · fold-boundary steering channel (operator override on dispatches)
**Visibility:** internal only (nothing public)

---

## 1. Operator-prompt shape (chat → head)

Constraint: ≤2 lines. One named artifact. No status-restatement.

**Template (canonical):**
```
<prompt-verb>: <artifact-path>
<optional 2nd line: one constraint or override>
```

**Rules:**
- Line 1 MUST name exactly one artifact path (relative to repo root or `studies/rfc-143379-rig/`).
- Line 1 ≤ 120 chars.
- Line 2 optional; if present, ≤ 120 chars; carries a single constraint, override, or question — never a status summary.
- No "status:", "done:", "progress:" prefixes. No restating what already shipped.
- Verbs allowed: `build`, `audit`, `verify`, `compose-check`, `fold`, `override`, `handoff`, `review`.

**Examples (valid):**
```
build: studies/rfc-143379-rig/STAKE-TELEGRAM-20261109.md
verify: compose-check
```
```
override: dispatch D-7 fold-boundary
no new artifacts this block
```

**Invalid (reject):**
- Multi-artifact lists on line 1.
- Lines beginning with status/restatement ("Done so far:", "We have built...").
- Prompts >2 lines.

---

## 2. Evidence-cadence (head → operator)

Cadence: every 3–5 turns OR on artifact-completion, whichever comes first.
Payload: exactly three fields, no narrative.

**Format:**
```
CHANGED: <what changed, ≤1 line>
EVIDENCE: <pointer — file path + line/section or commit sha>
NEXT-BLOCKER: <single blocker or "none">
```

**Rules:**
- No prose beyond the three fields.
- `EVIDENCE` must be a concrete pointer (path:line, section heading, or sha). "see above" forbidden.
- `NEXT-BLOCKER` names one blocker; if multiple, list the gating one only.
- Cadence resets after each emission; track turn counter in head state.

---

## 3. Handoff format (machine-parseable, ≤6 lines)

```
GOAL: <one line>
DONE: <comma-separated artifact list>
NEXT: <next action, one line>
BLOCKER: <blocker or "none">
ARTIFACT-PATH: <primary artifact path>
```

**Rules:**
- Exactly 5 fields, in this order. Optional 6th line: `NOTES:` (≤1 line) for non-blocking context.
- Each field ≤ 1 line. Total ≤6 lines.
- `ARTIFACT-PATH` must resolve to an existing file at handoff time.
- Parseable by regex: `^(GOAL|DONE|NEXT|BLOCKER|ARTIFACT-PATH|NOTES): .*$`

---

## 4. Fold-boundary steering channel (operator override on dispatches)

The operator may override a dispatch at a fold boundary. Channel: a single telegram message tagged `override:`.

**Schema:**
```
override: <dispatch-id> <action>
<optional: reason, ≤1 line>
```

**Actions:** `hold` | `skip` | `reroute:<target>` | `pause-sprint`

**Rules:**
- Override applies only at fold boundaries (between blocks), never mid-block.
- `hold`: dispatch queued, not executed; re-evaluated next fold.
- `skip`: dispatch dropped; logged to handoff `DONE` as `skipped:<id>`.
- `reroute:<target>`: dispatch reassigned to named surface/agent.
- `pause-sprint`: freezes all dispatches; requires explicit `resume` to continue.
- Overrides are append-only in the audit trail (never deleted).
- Operator override takes precedence over head's plan; head acknowledges via evidence-cadence `CHANGED: override applied`.

---

## 5. Compose-check (self-verification)

Run before declaring the slice done:
1. Prompt-template lint: every sample prompt ≤2 lines, contains one artifact path.
2. Handoff regex parse: all 5 required fields present, in order.
3. Evidence-cadence: last emission within last 5 turns OR on artifact-completion.
4. Fold-override: override schema validates; actions in allowed set.

**Compose-check result (this slice):** PASS — templates, cadence, handoff, override channel all specified; artifact written at `studies/rfc-143379-rig/STAKE-TELEGRAM-20261109.md`.

---

## 6. Handoff (this slice)

GOAL: specify telegram chat-layer contract for 4-hour sprint
DONE: STAKE-TELEGRAM-20261109.md
NEXT: compose-check verify; await operator fold-override
BLOCKER: none
ARTIFACT-PATH: studies/rfc-143379-rig/STAKE-TELEGRAM-20261109.md
`, "path": "/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/STAKE-TELEGRAM-20261109.md"}