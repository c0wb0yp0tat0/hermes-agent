# The Return Slice — fourth lens (hosted-custom-code architecture)

**Register:** plain, evidence-carrying. **Limit:** ~10 min. **Doctrine:** results close the loop through the same spine.

## 1. THE RESULTS' UPLOAD (artifacts → repo release/run-surface)

- **upload-artifact lifecycle:** `actions/upload-artifact@v4`, name `run-<run_id>-<sha>`; retention 7 days (free-tier); path `.avrea/runs/<run_id>/`. One artifact per run, never partial; partial upload = run marked `upload-incomplete`, no receipt.
- **run-summary:** appended to `$GITHUB_STEP_SUMMARY` (markdown table: run_id, sha, verdict, artifact link). Mirrors to issue comment receipt-row.
- **issue-comment receipt-row:** on the tracking issue, a single comment per run (idempotent: find by `<!-- receipt:run_id -->` marker, edit if exists). Columns: `run_id | sha | verdict | artifact | ts`. No narrative; rows only.

## 2. THE RECEIPT's RETURN (results → study-records)

- **receipt-file landing on branch:** runner writes `receipts/<run_id>.json` and pushes to `study/rfc-143379-rig-20261105`.
- **Honest constraint-read (token-scope):** the default `GITHUB_TOKEN` is **read-only on push** for forks/PR branches from workflow runs in many configs; `contents: write` on the workflow's own token only works for the same repo's default branch or when explicitly granted. Cross-fork push (runner → origin study branch) requires a PAT with `contents:write` scoped to that repo, stored as repo secret `AVREA_PUSH_PAT`. Without it, push fails with 403 — this is the honest limit; do not paper over with `git config` tricks.
- **Fallback (head's pull-and-commit):** if runner lacks push permission, runner commits receipt to a patch artifact; head (operator machine) runs `git pull --rebase && git am <patch>` then pushes with its own creds. Receipt file lands on branch via head, marked `landed-by: head` in JSON. Receipt row still cites runner run_id + sha.

## 3. THE LEDGER'S CLOSE (finding-rows → G0-ledger)

- **Integration:** executed-run findings append rows to `G0-ledger.md` (append-only, never edit prior rows). Each row: `run_id | sha | finding | verdict | receipt-file | landed-by`.
- **Rule:** a run with no receipt-file on branch does not close a ledger row; row stays `pending-receipt`. Fold-gate: fold only when both fast (per-run) and slow (fold) receipts present.
- **Zero-delta:** measured delta = 0 across a fold → terminal, honest-negative accepted.

## Token-scope summary (honest limits)
- `GITHUB_TOKEN` (auto): read on forks, write only same-repo default branch with `contents: write`; cannot push to study branch from a fork-runner in most setups.
- `AVREA_PUSH_PAT` (secret): required for runner direct push; scope `contents:write` on target repo only.
- No secret in code; fallback path exists for air-gapped/no-PAT case.