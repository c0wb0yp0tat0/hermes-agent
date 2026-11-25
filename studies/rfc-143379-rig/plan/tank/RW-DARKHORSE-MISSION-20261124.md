# RW-DARKHORSE-MISSION-20261124 — the launched darkhorse mission record

**FINDING (one line):** The darkhorse launch was BUILT (three phased leg briefs on disk) but did not land — every leg is a NAMED FAILURE with no execution receipt, because this lane's terminal is git-only and the write-window gate blocks the harness fire; verdict **DIED-RECEIPTED**, death class `EXECUTION-AUTHORITY-WALL` (not the prior `TIMEOUT-PAYLOAD-BOUND`).

**Seat / scope:** copycat lane, branch `study/rfc-143379-rig-20261105`. PREVIEW ONLY — nothing posted to the RFC surface; local commit only, no push/pull. All reads local; no installs, no web, no memory-chain, no config/gateway, no public writes.

---

## 1. What the launch built (the mission's shape)

The three phased legs were constructed as small, content-bearing, pin-echoed probes per Luna's greens recipe (small payloads, max_tokens clamped ~512-1024, real content, pin echo). The leg briefs are on disk:

- `plan/tank/DARKHORSE-LEG1-GROUND-brief.md` — ground-read: floor reads ONLY the PRE-REGISTRATION paragraph; emits (a) unsourced clause, (b) weakest line; pin `GROUND-143379`; clamped 700.
- `plan/tank/DARKHORSE-LEG2-PEEREAR-brief.md` — peer-ear: floor reads ONLY the KvNloo-facing OPEN paragraph; emits ONE off phrase + confidence; pin `PEER-143379`; clamped 700. Gated on Leg 1 receipt.
- `plan/tank/DARKHORSE-LEG3-SYNTH-brief.md` — synthesis (assembly is mine): byte-verify each quoted line to the source kvnloo reply; emit byte-cited drown-proof record. Gated on Leg 1 and Leg 2 receipts.

Harness fire shape (per leg, endpoint at the floor `127.0.0.1:44831`):
```
HARNESS_ENDPOINT=http://127.0.0.1:44831/v1/chat/completions HARNESS_MAX_TOKENS=700 python3 /root/scripts/copycat-harness.py --model "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf" --brief <leg brief> --artifact <leg artifact> --rounds 8 --logfile <leg log>
```

## 2. Execution receipts — per leg (witness rule applied)

The witness rule: a leg's receipt is its HTTP status + content-length + finish_reason + dt + the answer's bytes; a leg without a receipt is a **named failure, never a pass**. No HTTP receipt exists for any leg, so none is counted as a pass and no answer bytes are invented.

| Leg | HTTP | content-length | finish | dt | answer head | status |
|-----|------|----------------|--------|----|-------------|--------|
| LEG 1 ground | — | — | — | — | — | **NAMED FAILURE — no receipt** |
| LEG 2 peer-ear | — | — | — | — | — | **NAMED FAILURE — no receipt** (also gated: Leg 1 did not land) |
| LEG 3 synthesis | — | — | — | — | — | **NAMED FAILURE — no receipt** (also gated: Legs 1-2 did not land) |

No `copycat-harness.py` invocation was made; no request reached `127.0.0.1:44831`; no raw harness JSON/stdout exists. These tables are deliberately empty — filling them would violate the witness rule.

### The wall receipts (what was actually observed)

- Attempting to run the harness command returned verbatim: `error: "terminal is git-only for lanes"`. Confirmed with a second probe (`echo test`) — same result. **The lane's terminal admits git only; it cannot execute the python harness / HTTP fire.**
- Attempting to read the study tree to obtain the source text for byte-verification returned verbatim: `READ-GATED: the write-window is open ... The read-tools AND the terminal's content-reads stay blocked until the artifact exists.` **The write-window blocks content reads, so the PRE-REGISTRATION paragraph and OPEN paragraph text could not be retrieved to seed the probes or to byte-verify quotes.**

Death class for all three legs: `EXECUTION-AUTHORITY-WALL` (no fire authority + no read authority), **distinct from** the two prior attempts' `TIMEOUT-PAYLOAD-BOUND` death (raw read + copycat lane, both 540s timeouts, receipted in NEMO-WATCH §9 and RECIPE-RETRY §4 per the brief). This launch's failure is at the fire gate, not at generation — it never reached the model, so it neither reproduces nor refutes the payload-bound class.

## 3. Final drown-proof record (Leg 3 synthesis)

**Not assembled — no quotable lines with byte citations exist.** Leg 3 requires (1) Leg 1 and Leg 2 answers and (2) byte-matching each quoted line to the source kvnloo reply. Both inputs are absent: no leg answers (no receipts) and no source text (read-gated). Producing named clauses here would be fabrication, which the drown-proof design forbids. Per the brief, "no line without a byte citation counts" — so the record has zero lines and is explicitly EMPTY, not passed.

What a landed Leg 3 would contain (contract held ready in `DARKHORSE-LEG3-SYNTH-brief.md`): each named line as (verbatim quote, source file, byte offset, span-sha256); any quote that fails byte match marked `UNSOURCED-BYTE-CHECK-FAIL`.

## 4. Minimal moves (wall clause — a question with a constructed smaller move, not a bare verdict)

The wall is a question — "can this lane fire the floor?" — answered NO by two receipts. The minimal move for a re-run is a smaller, authorized fire, not a verdict on the floor:

1. **Execution authority:** re-run each leg under a seat whose terminal can execute `python3 /root/scripts/copycat-harness.py` against `127.0.0.1:44831`, or have the launcher (hy4-flash) fire the three briefs as written. Preserve raw JSON/stdout as each leg's receipt.
2. **Source text:** lift the write-window read-gate (or receive the two paragraphs from a read-authorized lane) so the single PRE-REGISTRATION paragraph and single OPEN paragraph can be pasted into Legs 1-2 and byte-verified in Leg 3.
3. **Payload discipline retained:** one paragraph per probe, max_tokens 700, pin echo required. If a re-fire still times out at ~540s, that is a genuine `TIMEOUT-PAYLOAD-BOUND` death — receipt it (HTTP, content-length, finish, dt, answer head) and halve the payload (paragraph → its first sentence) as the next smaller probe before any floor verdict.

## 5. Verdict

**DIED-RECEIPTED.** The floor's drown-proof read did not land on this lane: all three legs are named failures with no execution receipts, and the death class is `EXECUTION-AUTHORITY-WALL` (git-only terminal + write-window read-gate), receipted by the two verbatim error strings in §2. This is a finding, as the mission allows. It does **not** establish that the floor itself is payload-bound today — that question stays OPEN until an execution-authorized re-run produces per-leg HTTP receipts. Wire integrity of the build is intact: three leg briefs on disk, harness shape correct, witness rule upheld (no fabricated bytes), gates declared.

**Gate:** PREVIEW ONLY; nothing posted; RFC surface quiet; local commit only; no push/pull.

---

### Next mechanism
SELD (read-side evidence-plane verifier) is the natural next mechanism: it supplies exactly the missing capability — byte-verifying each quoted line against the source evidence plane — so that when an execution-authorized lane fires these legs, Leg 3's byte citations are machine-checked rather than asserted.
