# AVREA LEG CONTRACT — the fork's parallel verification surface (2026-11-05)

## The leg's purpose
Run OUR hosted verification on the self-hosted Avrea surface side-by-side with GitHub's free window — the SAME pinned heads + the SAME recipe, the divergence as data. The parallel is the point, never the replacement.

## The envelope (every run's receipt shape)
```
envelope:
  id:            <runner-id>_<run-id>_<pin>
  run:           <GitHub run id>
  pin:           <exact SHA, the checkout's target>
  requested:     <the dispatch's head_sha input>
  executed:      <git rev-parse HEAD after checkout>
  assert:        requested == executed (hard step, before the suite)
  battery:       <the test set actually collected at the pin>
  summary:       <pytest tail: N passed / M failed / K skipped / xpassed>
  conclusion:    <success | failure>
  receipt_url:   <the run page>
```
The pin is asserted BEFORE the suite; the receipt is written only from the run's actual conclusion — a committed workflow definition is NOT execution (the NOT-RUN marker is the honest state until the receipt exists).

## The meter budget
- 4-vCPU class = 1,500 min/mo on the free meter. Validation moments, never churn: one run per pin, no re-dispatch without a named reason.
- The label IS the budget: prefer `avrea-ubuntu-latest` (2-vCPU, 3,000 min) for light pins; the 4-vCPU for the full-suite pins.

## The battery
- The repo's own uv recipe verbatim (uv python install 3.14 + HERMES_DISABLE_LAZY_INSTALLS=1 uv sync --locked --python 3.14 --extra all --group dev --extra anthropic --extra mistral --extra fal --extra modal --extra daytona --extra parallel-web).
- Path-tolerant collection: the falsifier-battery is branch-local, absent on older pins — include it only when `[ -d tests/falsifier-battery ]`; a missing path is a collection error (exit 4), never an assertion failure.
- Call through `uv run pytest` — the synced venv's interpreter, never the PATH's system python.

## The wall clause (binding)
A non-reproduction is a QUESTION, not a stop — the minimal experiment that moves the wall is constructed before any "unreproducible" verdict. A "green here / can't reproduce" without the construction is a hypothesis, not a finding.

## The operating rules
- Nothing public beyond the fork (the fork IS the hub — the study's home); the nous surface waits on the user's word.
- No upstream merge, no push to any other repo, no model credentials, no production profile.
- Receipts land in `studies/rfc-143379-rig/RECEIPTS.md` first, then the threads if asked.
- Every run-receipt claims only what the run's log shows; NOT-RUN stays until the receipt exists.
