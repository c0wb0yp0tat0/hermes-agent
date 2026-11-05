# RFC #143379 rig study — the verification receipts and the leg's contract

The rig's downstream-only verification record for [RFC #143379](https://github.com/NousResearch/hermes-agent/issues/143379) — one place, honest to the NOT-RUN marker. **No upstream posts, no upstream code changes.** Original upstream authors retain their ownership.

- `RECEIPTS.md` — the receipt ledger: every pinned run with requested == executed asserted in-run, the real numbers, the NOT-RUN markers.
- `AVREA-LEG-CONTRACT.md` — the leg's operating contract: the envelope schema, the meter budget, the wall clause.
- The falsifier battery lives on the fork's `fixes/falsifier-battery-20261104` (referenced, not duplicated); the receipt-comment template on `main` at `docs/notes/RECEIPT-COMMENT-TEMPLATE.md`.

## The evidence, as it stands

**Run 1 — the Avrea leg's first pinned receipt.** [Run 42064685359](https://github.com/c0wb0yp0tat0/hermes-agent/actions/runs/42064685359), 2026-11-05, pin `d1bdb4582cd5d16be6a6b486f696f8240c222b96` (#139606's merge head — the seven-stage write-gate acceptance pipeline). The pin was asserted in-run (`requested_sha == executed_sha == d1bdb4582…`) before the suite; the battery at that head: **117 passed, 10 skipped in 6.49s**. The 10 skips are the doc-chain probes — that pin predates the doc-chain store's arms; skipped with `-rs` reasons, never silently (the skip-reasons discipline). This qualifies THAT pin's checked-out source, nothing else.

**Run 2 — the falsifier battery at the whole-anchor landing.** Host-local run at `a996d4ad3039e280dc21e9b558f5a44c081dda42` (the "whole-anchor structural resolution — the strengthened arms flip GREEN" commit): `uv run pytest tests/falsifier-battery -rs -q` → **28 passed, 1 xpassed in 1.01s**. The xpassed is an expected-failure that PASSED — the strengthened nugget-6 arm flipping on the resolution. The battery: 11 arms (nugget 1–6, the mutated substring-orphan case, the #141876 composition arms).

**The composition's four pins** (all open upstream, per the RFC's network): `d1bdb4582` #139606 (the write-gate) · `ffb85c2c58` #140008 (session preservation + dream cycle) · `60a2e15638` #116673 (the bounded read — MEMORY.md anchors a doc chain) · `ec649ad9d` #141876 (the read restore — the RFC's landing-order first piece).

## Reproduce

```bash
# The pinned Avrea run (one dispatch per pin; the meter is 4-vCPU, 1,500 min/mo):
gh workflow run rig-hosted-verify-avrea.yml -R c0wb0yp0tat0/hermes-agent --ref main \
  -f head_sha="d1bdb4582cd5d16be6a6b486f696f8240c222b96"

# The falsifier battery at the whole-anchor head (local checkout of
# fixes/falsifier-battery-20261104):
uv run pytest tests/falsifier-battery -rs -q
```

## Execution state (honest)

- `d1bdb4582`: **RUN — GREEN** (117 passed / 10 skipped, requested == executed).
- `ffb85c2c58` / `60a2e15638` / `ec649ad9d`: **NOT RUN** — each receipt appears here when the runner lands the pin.
- The GitHub-window side: **NOT RUN** (the hosted queue class on this account) — the Avrea side is the live surface; divergence is data.
- The 300+ cycle long-session gate at 4×–8× (the RFC's hard gate): **NOT RUN** on a fixed ruler — the RFC's probe scope bug is acknowledged and no certifying run happens on the old probe (the RFC's own measurement protocol).

No origin publication, no merge, no model credential, no production user profile was used.
