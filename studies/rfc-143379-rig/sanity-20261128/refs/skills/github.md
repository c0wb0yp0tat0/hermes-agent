---
name: github
description: "GitHub via gh CLI: PRs, issues, reviews, repos, auth."
version: 2.0.0
author: Ben Barclay (benbarclay), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [github, gh, git, pull-requests, issues, code-review, repos, auth, ci]
    category: software-development
    related_skills: [codebase-inspection, requesting-code-review]
---

# GitHub

Work GitHub end to end with the `gh` CLI (REST fallback where noted): auth,
issues, the PR lifecycle, issue-to-PR delivery, code review, and repo
management. This skill consolidates six former skills; each workflow lives
complete in its reference file — ALWAYS read the matching reference before
starting that workflow, the body below only routes.

## Routing

| Task | Read first |
|---|---|
| Auth broken / new machine / token or SSH setup / gh login | `references/auth.md` |
| Create, triage, label, assign, close issues | `references/issues.md` |
| Branch, commit, open PR, watch CI, merge | `references/pr-workflow.md` |
| Carry an ISSUE to a verified PR (full delivery loop) | `references/issue-to-pr.md` |
| Review someone's PR: diffs, inline comments, verdict | `references/code-review.md` |
| Clone/create/fork repos, remotes, releases | `references/repo-management.md` |
| Stage private previews / companions / progress (create, visibility gate, sync) | `references/gh-gists.md` |

Supporting assets: `scripts/gh-env.sh` + `scripts/git-credential-token.py`
(auth helpers), `templates/` (PR bodies, bug report, feature request),
`references/ci-troubleshooting.md`, `references/conventional-commits.md`,
`references/github-api-cheatsheet.md`, `references/review-output-template.md`.

## Core discipline (applies to every workflow)

- Preflight once per session: `gh auth status` — if it fails, go to
  `references/auth.md` before anything else.
- Prefer `gh` over raw REST; drop to `gh api` only for endpoints the
  porcelain lacks (the cheatsheet lists them).
- Never report CI green without checking `gh pr checks` yourself; never
  claim merged without verifying `state,mergedAt`.
- Read full context before writing: `gh issue view --comments` /
  `gh pr view --comments` — decisions live in threads, not titles.
- If `gh issue view` aborts with "Projects (classic) is being deprecated" (repos
  carrying classic projects), read the thread over REST: `gh api
  repos/O/R/issues/<n>` for the body and `gh api
  repos/O/R/issues/<n>/comments --paginate --jq '.[] |
  {user:.user.login,created_at,body}'`. The GraphQL path pulls `projectCards`
  and fails before rendering — the failure is the view command's, not the
  issue's.
- Sweep for duplicates before creating anything:
  `gh pr list --search` / `gh issue list --search`.
- **Workflow-dispatch inputs must nest under `inputs` (earned 2026-11-18):** `gh api repos/O/R/actions/workflows/<file>/dispatches` rejects a flat `-f head_sha=...` beside `-f ref=...` with `"head_sha" is not a permitted key` even when the workflow's `on: workflow_dispatch` declares that input — the API only accepts inputs nested in the JSON body (`{"ref": ..., "inputs": {"head_sha": ..., "battery": "union"}}` via `--input -`). The error message is a payload-shape tell, not a workflow-state tell: verify the fork's workflow YAML first (`.../contents/.github/workflows/<file>.yml`) to distinguish a genuinely absent input from a flat-payload rejection. Also: dispatch to each fork's copy by its default branch, skip repositories where the account has Actions disabled (HTTP 422 "Actions has been disabled") and ROW the disabled set — coverage is dispatched/total with the disabled named, never silent.

## Verification

- The workflow's own reference file defines done for that task.
- Cross-cutting: every claim about remote state (CI, merge, release,
  issue state) is backed by a fresh `gh` read, never memory.
