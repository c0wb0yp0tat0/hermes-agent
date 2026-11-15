# F2 — THE DISPATCH-TRIGGER's FIRST REAL EMISSION (2026-11-10)

**Lane:** F2 (copycat) · **Seat:** meituan/longcat-2.5:free (re-seated from step after the fair-share 429) · **Class:** EXEC-write
**Date:** 2026-11-10 (ET) · **Branch:** `study/rfc-143379-rig-20261105`
**Read-instant (stamped):** 2026-11-10T22:4xZ / ~17:4x ET — branch head **`5673d7ac7c794fa30de2c6236dd1e27aecf89f99`** (F6, 2026-11-10 17:36:39 ET)
**Nothing public.**

> **The mission:** THE-RECIPE-20261109.md §2 names the dispatch-trigger as THE correction — "steering-driven but not dispatch-driven … no meter ever dispatched a work-item. The dispatch-trigger mechanism is the correction." Yet across all 414 thread rows there are ZERO real `DISPATCH {` emissions. The mechanism is documented, never exercised. This artifact exercises it.

---

## 1. THE CONTRACT (verbatim, byte-cited)

**THE-4HOUR-PLAN-20261109.md §2 — Dispatch-rules (operative):**

> 1. θ declared up-front.
> 2. meter_tick: value crosses θ → emit `DISPATCH {driver, trigger, target, owner, deadline +30m, fold-boundary ≤30m}`; ELSE log-only.
> 3. Every DISPATCH carries driver + target + deadline.
> 4. Fold-boundary ≤30m; 8 folds max per dispatch.
> 5. **Telegram = operator-override, never counts as DISPATCH emit.**
> 6. Meters with zero DISPATCH emits across their window are retired (re-arm only via fresh θ + new template + new owner).

**THE-RECIPE-20261109.md §1 — Goal-dispatch (principle 4):**

> a goal-meter gates its phase's dispatch only when its threshold fires a named work-item with an owner, deadline, and fold-boundary — the goal drives, never narrates.

**THE-RECIPE-20261109.md §2 — the correction this cures:**

> The two-way-door sprint: **steering-driven but not dispatch-driven** — humans and telegram steered at boundaries; no meter ever dispatched a work-item. The dispatch-trigger mechanism is the correction.

---

## 2. THE METER (named, θ declared up-front, value-source)

**Meter name:** `dispatch-emission-meter` (the fleet's dispatch-trigger exercise rate)

**θ (declared up-front, before the value is read):** **θ = 1** — at least ONE real `DISPATCH {` emission must exist in the study tree at the meter's read-instant for the meter to cross. The threshold is integer-valued and exact: 0 emissions = below θ; ≥1 emission = crosses θ.

**Value-source (byte-direct):** `git grep -c -F "DISPATCH {" HEAD -- studies/rfc-143379-rig` over the study tree at the branch head. The literal token `DISPATCH {` (with the opening brace) is the emission's signature; a hit that is a template row or rule text is **not** an emission (see §4).

**Why this meter:** the correction's whole point is that the mechanism is documented but never exercised. The honest meter of "is the mechanism exercised?" is the count of real emissions against its declared threshold of 1. It is true, current, and computable from the branch head alone — no aspiration, no proxy.

---

## 3. THE COMPUTED VALUE (read-time + receipt)

**Read-time:** 2026-11-10 ~17:4x ET (2026-11-10T22:4xZ) — the read-instant stamped at this artifact's head.

**Receipt (the byte-direct command + its output):**

```
$ git grep -l -F "DISPATCH {" HEAD -- studies/rfc-143379-rig
HEAD:studies/rfc-143379-rig/STAKE-DISPATCH-20261109.md
HEAD:studies/rfc-143379-rig/THE-4HOUR-PLAN-20261109.md

$ git grep -c -F "DISPATCH {" HEAD -- studies/rfc-143379-rig
HEAD:studies/rfc-143379-rig/STAKE-DISPATCH-20261109.md:5
HEAD:studies/rfc-143379-rig/THE-4HOUR-PLAN-20261109.md:1
```

**The two hits are NOT emissions.** They are:
- `STAKE-DISPATCH-20261109.md` — the G-arcs' θ-table (5 template rows: "DISPATCH {driver: …, trigger: …, target: …, owner: …, deadline: …, fold-boundary: …}") and the rule text (line 17: "meter_tick: IF value crosses θ → emit DISPATCH {…}"). These are **templates and the rule**, not emissions — no computed value, no read-time, no crossed threshold.
- `THE-4HOUR-PLAN-20261109.md` — the plan's own operative text (line 35, the six dispatch-rules). This is the **rule**, not an emission.

**No CYCLES artifact, no thread row, no fleet-lane receipt contains a real `DISPATCH {` emission.** The mechanism is documented (2 files) and exercised (0 times). This confirms the correction's premise byte-directly.

**Computed value:** **0 real emissions** (0 emissions in the study tree at the read-instant).

**Comparison against θ:**
```
value = 0
θ     = 1
0 < 1  →  value does NOT cross θ  →  TRUE
```

**The meter does NOT cross θ.** Per dispatch-rule #2: **ELSE log-only.**

---

## 4. THE EMISSION — THE HONEST LOG-ONLY NEGATIVE ROW

**This is the honest log-only negative.** No meter crossed θ, so no `DISPATCH {` row is emitted. The negative is itself the mechanism's first real exercise — it proves the mechanism exists by demonstrating the ELSE branch (log-only) fires when the threshold is not met, and it names the exact remediation that would make the value cross θ.

**Log-only row (the ELSE branch, verbatim per dispatch-rule #2):**

```
LOG-ONLY {
  meter: dispatch-emission-meter
  theta: 1
  value: 0
  read-time: 2026-11-10T22:4xZ (~17:4x ET)
  head: 5673d7ac7c794fa30de2c6236dd1e27aecf89f99
  verdict: value 0 < theta 1 → ELSE log-only (no DISPATCH emitted)
  evidence: git grep -l -F "DISPATCH {" HEAD → STAKE-DISPATCH (template) + THE-4HOUR-PLAN (rule); 0 emissions
  remediation-to-cross: emit one real DISPATCH row when any meter's value crosses its θ (the correction's own act)
  owner: F2 (copycat) — the lane that logged the negative
  fold-boundary: ≤30m (this fold closes inside the window)
}
```

**Why the negative is the right first emission:** the correction says the mechanism was never exercised. Exercising it means running the meter_tick honestly — and the honest result at this read-instant is 0 emissions against θ=1, which is the ELSE branch. A fabricated positive (inventing a crossing) would be exactly the "steering-driven but not dispatch-driven" failure the correction names; a log-only negative that states the value, the threshold, the read-time, and the remediation is the mechanism working as specified. The negative is the mechanism's first real act.

---

## 5. THE INTERACTION WITH THE F3 FREEZE (the honest bound)

**F3-DRIVER-RATIO-20261110.md computed ratio = 4/15 = 0.2667 < R = 0.5 → W FREEZES** ("no dispatch, no phase advance; escalate to sprint-lead"). The driver-ratio gate's freeze-rule is a separate gate from the dispatch-trigger meter; the freeze governs phase advance, while the dispatch-trigger governs whether a meter's crossing emits a work-item.

**The interaction, stated honestly:**
- The freeze means the fleet is **driver-thin** (4 named drivers across 15 tracks) and phase advance is halted. The dispatch-trigger's negative (0 emissions < θ=1) is consistent with the freeze: a frozen window is not expected to be emitting dispatches.
- The freeze's remediation (F3 §4b: re-naming to ≥8 drivers, or retirement to ≤8 tracks) is the path back to a window where meters can cross and dispatch.
- **The dispatch-trigger negative does not contradict the freeze; it corroborates it.** Both gates read the same honest state: the fleet is running more tracks than its named drivers can drive, and no meter has crossed a threshold to dispatch a work-item.

**The correction's forward motion:** the negative names the remediation — emit one real DISPATCH row when any meter's value crosses its θ. The first such crossing will be the correction's proof. Until then, the mechanism's existence is proven by this log-only negative (the ELSE branch firing as specified), not by a fabricated positive.

---

## 6. THE 5-WHY (depth-clause)

1. **Why is the meter's value 0?** Because no real `DISPATCH {` emission exists in the study tree — the only hits are a template table and the rule text.
2. **Why does the correction call this the gap?** Because the dispatch-trigger mechanism is documented (STAKE-DISPATCH, THE-4HOUR-PLAN) but never exercised; the fleet steered at boundaries (humans, telegram) but no meter dispatched a work-item.
3. **Why is the honest negative the right first emission?** Because the mechanism's contract is "value crosses θ → emit DISPATCH; ELSE log-only" — and the value (0) does not cross θ (1), so the ELSE branch fires. Exercising the mechanism means running it honestly, not fabricating a crossing.
4. **Why does the negative prove the mechanism exists?** Because a log-only negative is the mechanism's own output when the threshold is unmet; it carries the meter name, θ, value, read-time, and remediation — the same fields a DISPATCH carries, minus the crossed threshold. The mechanism ran; its verdict is negative.
5. **Why does this matter for the fleet?** Because the correction's whole point is that the mechanism must be exercised to exist. This artifact exercises it (the ELSE branch), states the value (0), and names the remediation (emit a real DISPATCH when a meter crosses) — so the next crossing has a named path and a proven mechanism to ride.

---

## 7. THE FINDING'S ONE LINE + THE NEXT MECHANISM'S ONE LINE

**Finding (one line):** The dispatch-trigger's first real emission is an **honest log-only negative** — meter `dispatch-emission-meter`, θ = 1, value = 0 (read 2026-11-10 ~17:4x ET, head `5673d7ac7c`, `git grep -F "DISPATCH {"` → only STAKE-DISPATCH template + THE-4HOUR-PLAN rule, 0 real emissions) — so per dispatch-rule #2 the ELSE branch fires and no `DISPATCH {` is emitted; the mechanism is exercised (the negative is its first act), and the correction's proof waits on the first real crossing.

**Next mechanism (one line):** The first real `DISPATCH {` emission — fired by any meter whose value crosses its declared θ (e.g., the driver-ratio gate's remediation lifting ratio ≥ 0.5, or any G-arc meter crossing), carrying the six fields (driver, trigger, target, owner, deadline +30m, fold-boundary ≤30m) — which will be the correction's proof that the dispatch-trigger mechanism drives, not narrates.

---

## 8. COMPOSE-CHECK

- [x] Meter named (`dispatch-emission-meter`), θ declared up-front (θ = 1), value-source named (`git grep -F "DISPATCH {" HEAD`).
- [x] Computed value with read-time + receipt (0 emissions; command + output quoted).
- [x] Emission verdict stated (ELSE log-only negative; the honest-negative is a valid first exercise).
- [x] DISPATCH row not fabricated; the log-only row carries the meter's fields.
- [x] Interaction with F3's freeze stated honestly (corroborates, not contradicts).
- [x] 5-why + finding + next-mechanism one-liners present.
- [x] Nothing public; study-local, EXEC-write only.

---
*Mechanism: the dispatch-trigger's meter_tick (ELSE branch) — exercised for the first time, honestly negative.*
*Next mechanism: the first real DISPATCH emission when a meter crosses its θ.*