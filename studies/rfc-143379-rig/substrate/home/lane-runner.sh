#!/usr/bin/env bash
# lane-runner.sh — Phase B dispatch skeleton for ACES lane launches.
#
# Web-first sources (binding, verified against local reality on this host):
#  - CI failure triage buckets (real regression; flaky/timing; runner/env;
#    network/infra; dependency/service) — negiadventures.github.io/blog/ci-failure-triage-ai-coding-agents.html
#  - 15 flaky-build categories (flaky tests, network issues, dependency
#    resolution) — arxiv.org/html/2602.02307v1
#  - GitHub API rate limiting: 403/429 with x-ratelimit-remaining=0 +
#    Retry-After header — docs.github.com/en/rest/using-the-rest-api/rate-limits
#  - Exponential-backoff retry, never blanket retry —
#    adaptive-enforcement-lab.com/patterns/github-actions/actions-integration/error-handling/rate-limiting/
#  - "check the artifact before declaring death" doctrine —
#    deepdive-mission-flow/LIVING-HOME-REPO-BRIDGE/IN-FLIGHT-ISSUES-FIX-PLAN.md (Phase A grading contract)
#  - agents-fleet worktree lifecycle: `git worktree add .worktrees/{id} -b worker/{id}`
#    (https://doc.agents-fleet.ai/advanced/worktrees)
#  - Hermes CLI: `--resume <session>` / `-c` recover a session by id;
#    `--pass-session-id` injects the session id; exit codes 0=ok,
#    1=partial/budget/never-ran, 130=interrupted, 75=EX_TEMPFAIL (rate-limited →
#    requeue) — (https://hermes-agent.nousresearch.com/docs/reference/cli-commands;
#    `hermes chat --help`)
#  - 429 tail shape: "429" + "resets at HH:MM" — local: /root/scripts/fair-share-probe.py
#  - git worktree add/remove/prune/list (git-scm.com/docs/git-worktree)
#  - Hermes fallback providers: 404 triggers immediate fallback
#    (https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers/)
#

set -uo pipefail

LANE_NAME="${LANE_NAME:-ldlane}"

# ── CONFIGURATION: fallback ladder for catalog drift recovery ──
# Priority: 1. LANE_MODEL (from brief), 2. fallback_providers from config, 3. hardcoded ladder
FALLBACK_LADDER=(
  "poolside/laguna-s-2.1:free"
  "poolside/laguna-xs-2.1:free"
  "deepseek/deepseek-v4-flash-0731"
)

DRIFT_LOG="/root/scripts/var/catalog-drift.log"
CATALOG_DRIFT_LEDGERR="$DRIFT_LOG"
MAX_PROBES_PER_ID=3
JITTER_MAX=2

# ── lane contract (ENFORCED by head grading: a dirty-base deliverable = hand-back) ──
print_contract() {
  cat >&2 <<'EOF'
=== LANE CONTRACT (Phase B, ENFORCED) ===
  * Work in an ISOLATED git worktree off origin/main (the bridge checkout).
  * Commit ONE deliverable on its own branch (lane/<session>).
  * Rebase CLEAN onto origin/main before landing; never commit on a dirty base.
  * If the mission does not touch the bridge checkout (no git repo / no origin/main),
    enforcement DEGRADES to a scratch dir + warning (contract not enforceable).
  * GRADE requires a canonical, locatable artifact (fixed --artifact, fresh mtime)
    AND PR confirmation (--repo + --pr-branch). 429-tail may override a non-zero
    exit ONLY when artifact+PR pass AND the log shows "429" + "resets at HH:MM".
    Any ambiguity -> GRADE: HEAD REVIEW (exit 2), NEVER auto-success.
============================ end contract ============================
EOF
}

usage() {
  cat <<'EOF'
lane-runner.sh — ACES lane dispatch skeleton (Phase B + Phase A grading contract)

USAGE:
  lane-runner.sh [options] -- <lane command...>
  lane-runner.sh --worktree-standard        print the enforced contract
  lane-runner.sh --grade [options]          run ONLY the grading contract (self-test)
  lane-runner.sh --probe-only               probe the fallback ladder without launching
  lane-runner.sh --help

GRADE CONTRACT (Phase A — grades by ARTIFACT + PR, not exit code):
  1. Canonical artifact: --artifact <path> (fixed, not env-derived). Fresh check:
     the artifact's mtime must fall in the run window
     [start - 5m, start + 10m] (RUN_WINDOW_START). A stale/missing artifact
     NEVER grades as success.
  2. PR confirmation: --repo O/R + --pr-branch <prefix>. Grade requires an
     open-or-merged PR whose headRefName matches the prefix (gh pr list).
     A PR-less landing -> HEAD REVIEW.
  3. Bounded 429-tail override: a non-zero exit is overridden to VERDICT-429-TAIL
     ONLY when (a) the log tail contains "429" + "resets at HH:MM" AND (b) the
     artifact+PR checks pass; then retry the grade ONCE after the reset window
     (HH:MM parsed from the log). A 120s decision timeout bounds the wait; beyond
     it -> HEAD REVIEW.
  4. Ambiguity -> HEAD REVIEW: any grade that is not (a) clean success or
     (b) 429-tail success prints "GRADE: HEAD REVIEW <reason>" and exits 2 —
     partial artifacts, missing paths, PR-less landings, truncation/timeout tails.
     NEVER auto-success on ambiguity.

OPTIONS:
  --worktree / --no-worktree   enforce / skip worktree isolation (auto: on if git repo)
  --artifact PATH              canonical, locatable artifact path for the verdict/grade line
  --log FILE                   log path (default: scratch/<lane-session>.run.log)
  --resume SESSION             hermes session to resume (forwarded to the lane command)
  --repo O/R                   repo for PR confirmation (owner/repo)
  --pr-branch PREFIX           PR headRefName prefix to match (gh pr list)
  --rc CODE                    exit code to grade against (self-test / --grade default 0)
  --dry-run                    resolve worktree + contract; run no lane command
  --probe-only                 probe fallback ladder without launching the lane
  --model MODEL_ID             model id for catalog drift probe (required for --probe-only)
  --task-fit REQUIREMENT       mission task category (e.g., "judgment_leg" or "cheap_recon")
EOF
}

# ── resolve an ISOLATED worktree off origin/main (fail-closed -> degrade) ──
# Sets WORKTREE_DIR, WORKTREE_BRANCH, WORKTREE_TOPLEVEL, CLEANUP=1.
resolve_worktree() {
  git rev-parse --is-inside-work-tree >/dev/null 2>&1 || return 1
  git rev-parse --verify --quiet origin/main >/dev/null 2>&1 || return 1
  WORKTREE_TOPLEVEL="$(git rev-parse --show-toplevel)"
  # agents-fleet pattern: .worktrees/{agentId} on a worker/{agentId} branch.
  WORKTREE_DIR="$WORKTREE_TOPLEVEL/.worktrees/$LANE_SESSION"
  WORKTREE_BRANCH="lane/$LANE_SESSION"
  # -b => new branch off origin/main; fail-closed if it collides.
  git worktree add -b "$WORKTREE_BRANCH" "$WORKTREE_DIR" origin/main >/dev/null 2>&1 || return 1
  CLEANUP=1
  return 0
}

# ── diagnostic verdict line, echoed on ANY exit (Phase A groundwork) ──
# Format: LANE session=<id recoverable via `hermes --resume`> artifact=<path> exit=<code>
emit_verdict() {
  local sid="$1" art="$2" rc="$3"
  printf 'LANE session=%s artifact=%s exit=%s\n' "$sid" "${art:-<unset>}" "$rc"
}

# ── CATALOG DRIFT: Guarded launch probe system ──

# Check if an id has recent 429 pattern (never self-trigger 429s)
check_recent_429() {
  local id="$1"
  local log="${2:-$LOG}"
  [ -f "$log" ] || return 1
  # Look for recent 429 associated with this model/provider
  if tail -n 100 "$log" 2>/dev/null | grep -q "429.*$id\|$id.*429"; then
    return 0  # has 429 pattern
  fi
  return 1  # no 429 pattern
}

# Probe a single model id with bounded backoff
# Returns 0 if model responds OK, 1 otherwise
probe_model_id() {
  local model_id="$1"
  local attempt="$2"
  local wait_sec="$3"
  
  # Exponential backoff with jitter: base 5s * 2^(attempt-1) + random(0,jitter_max)
  local base_wait=$((5 * (2 ** (attempt - 1))))
  local jitter=$((RANDOM % (JITTER_MAX + 1)))
  local total_wait=$((base_wait + jitter))
  
  [ $attempt -gt 1 ] && sleep "$total_wait"
  
  # Launch test: hermes chat -q "Reply with exactly: OK" -m <id>:free
  local result
  [ "${model_id##*:}" != "free" ] && model_id="${model_id}:free"
  result=$(hermes chat -q "Reply with exactly: OK" -m "$model_id" --oneshot 2>&1)
  local exit_code=$?
  
  if [ $exit_code -eq 0 ] && printf '%s\n' "$result" | tr -d '\r' | grep -q "^OK$"; then
    echo "OK"
    return 0
  fi
  return 1
}

# TASK-FIT verification: check if model category matches mission requirement
# Returns 0 if fit, 1 if NO FIT
verify_task_fit() {
  local model_id="$1"
  local requirement="$2"
  
  # Model naming convention check (judgment-leg vs cheap-recon style)
  # Extract capability from model id or manifest
  case "$requirement" in
    judgment_leg|judgment-leg|leg|deep)
      # These models should have deeper reasoning capability
      if printf '%s\n' "$model_id" | grep -qiE 'leg|deep|reason|opous|opus'; then
        return 0
      elif printf '%s\n' "$model_id" | grep -qi 'llama|claude|sonnet|opus'; then
        return 0
      fi
      return 1
      ;;
    cheap_recon|recon|cheap|fast)
      # These are for lightweight tasks
      if printf '%s\n' "$model_id" | grep -qiE 'xs|mini|fast|quick|recon'; then
        return 0
      fi
      # Assume smaller models are cheaper
      if printf '%s\n' "$model_id" | grep -qiE 'xs|mini|tiny|small'; then
        return 0
      fi
      return 1
      ;;
    *)
      # Unknown requirement, accept by default
      return 0
      ;;
  esac
}

# Log catalog drift event
log_catalog_drift() {
  local dead_id="$1"
  local probed_ids="$2"
  local final_id="$3"
  local timestamp
  timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
  
  mkdir -p "$(dirname "$CATALOG_DRIFT_LEDGERR")"
  
  {
    printf '%s CATALOG-DRIFT: %s 404\\' "$timestamp" "$dead_id"
    printf 'd -> probed %s -> used %s\\n' "$probed_ids" "$final_id"
  } >&2
  {
    printf '%s CATALOG-DRIFT: %s 404\\' "$timestamp" "$dead_id"
    printf 'd -> probed %s -> used %s\\n' "$probed_ids" "$final_id"
  } >>"$CATALOG_DRIFT_LEDGERR"
}

# Probe the fallback ladder on 404, with bounded backoff and skip-429 logic
# Arguments: $1 = primary model id, $2 = task-fit requirement (optional)
# Returns: "used=<model_id>" on success, empty on total failure
probe_fallback_ladder() {
  local primary_id="$1"
  local task_requirement="${2:-}"
  local probed_ids=()
  local used_id=""
  
  # Build full ladder: primary first, then fallbacks
  local ladder=()
  ladder+=("$primary_id")
  for fallback in "${FALLBACK_LADDER[@]}"; do
    ladder+=("$fallback")
  done
  
  # For each id in ladder, probe with backoff
  for attempt_id in "${ladder[@]}"; do
    # Skip if recent 429 pattern detected
    if check_recent_429 "$attempt_id" "$LOG"; then
      continue
    fi
    
    # Probe with bounded backoff (max 3 probes per id)
    local probe_result
    for probe_attempt in $(seq 1 $MAX_PROBES_PER_ID); do
      probe_result=$(probe_model_id "$attempt_id" "$probe_attempt" "$LOG")
      if [ "$probe_result" = "OK" ]; then
        break
      fi
    done
    
    if [ "$probe_result" = "OK" ]; then
      # TASK-FIT verification
      if [ -n "$task_requirement" ] && ! verify_task_fit "$attempt_id" "$task_requirement"; then
        # Report NO FIT but continue to next fallback
        printf 'CATALOG-DRIFT: %s 404\\' "$attempt_id" >&2
        printf 'd -> probed %s -> NO FIT for %s\\n' "${probed_ids[*]}" "$task_requirement" >&2
        probed_ids+=("$attempt_id:fit-fail")
        continue
      fi
      
      used_id="$attempt_id"
      break
    else
      probed_ids+=("$attempt_id")
    fi
  done
  
  if [ -n "$used_id" ]; then
    # Log the drift
    local probed_str=""
    for pid in "${probed_ids[@]}"; do
      probed_str="$probed_str $pid"
    done
    log_catalog_drift "$primary_id" "$probed_str" "$used_id"
    printf 'CATALOG-DRIFT: %s 404\\' "$primary_id" >&2
    printf 'd -> probed%s -> used %s\\n' "${probed_str:-none}" "$used_id" >&2
  fi
  
  echo "$used_id"
}

# ── Phase A: grading contract helpers ──

# Stat an epoch-mtime portably (Linux `stat -c %Y` then BSD `stat -f %m`).
file_mtime() {
  stat -c %Y "$1" 2>/dev/null || stat -f %m "$1" 2>/dev/null || echo 0
}

# (1) Canonical artifact + freshness. mtime must be in [start-300, start+600].
# Echoes a short reason token; returns 0 pass / 2 fail.
check_artifact() {
  local art="${1:-}" start="${RUN_WINDOW_START:-$(date +%s)}"
  if [ -z "$art" ] || [ ! -e "$art" ]; then echo "unset_or_missing"; return 2; fi
  local now mtime lo hi
  now="$(date +%s)"
  mtime="$(file_mtime "$art")"
  if [ -z "$mtime" ] || [ "$mtime" -le 0 ] 2>/dev/null; then echo "unreadable_mtime"; return 2; fi
  lo=$(( start - 300 ))          # 5m before start (grace)
  hi=$(( start + 600 ))          # 10m after start (run window)
  if [ "$mtime" -lt "$lo" ]; then echo "stale_before_window"; return 2; fi
  if [ "$mtime" -gt "$hi" ]; then echo "future_outside_window"; return 2; fi
  echo "ok"; return 0
}

# (2) PR confirmation: --repo + --pr-branch must resolve to an open/merged PR.
# Echoes a short reason token; returns 0 pass / 2 fail. PR-less (args unset),
# missing gh, or no matching headRefName -> fail.
check_pr() {
  local repo="${REPO:-}" prbranch="${PR_BRANCH:-}"
  if [ -z "$repo" ] || [ -z "$prbranch" ]; then echo "no_pr_args"; return 2; fi
  if ! command -v gh >/dev/null 2>&1; then echo "gh_missing"; return 2; fi
  local merged open
  merged="$(gh pr list --repo "$repo" --state merged --json headRefName --limit 100 2>/dev/null || true)"
  open="$(gh pr list --repo "$repo" --state open --json headRefName --limit 100 2>/dev/null || true)"
  if printf '%s\n' "$merged" "$open" | grep -q "\"headRefName\": \"${prbranch}\""; then
    return 0
  fi
  echo "no_matching_pr"; return 2
}

# (3a) 429-tail detection. Echoes reset_at "HH:MM" (or nothing); returns 0 if the
# log tail contains "429" + "resets at HH:MM", else 1.
detect_429_tail() {
  local log="$1"
  [ -f "$log" ] || return 1
  local tail reset_at
  tail="$(tail -n 40 "$log" 2>/dev/null || true)"
  printf '%s' "$tail" | grep -q '429' || return 1
  reset_at="$(printf '%s' "$tail" | grep -oE 'resets at [0-9]{2}:[0-9]{2}' | tail -1 | awk '{print $3}')"
  [ -n "$reset_at" ] || return 1
  printf '%s' "$reset_at"
  return 0
}

# (3b) Bounded wait until the 429 reset window. Returns 0 if waited (within
# 120s), 1 on decision timeout (>120s away) or sleep failure.
wait_429_reset() {
  local reset_at="$1"
  local now_h now_m rh rm wait_sec
  now_h="$(date +%H)"; now_m="$(date +%M)"
  rh="${reset_at%%:}"; rm="${reset_at#*:}"
  wait_sec=$(( (rh*60+rm) - (now_h*60+now_m) ))
  [ "$wait_sec" -le 0 ] && wait_sec=$((wait_sec + 720))   # wrap past midnight
  [ "$wait_sec" -lt 1 ] && wait_sec=1
  if [ "$wait_sec" -gt 120 ]; then return 1; fi          # decision timeout
  sleep "$wait_sec" 2>/dev/null || return 1
  return 0
}

# ── Phase A grading contract orchestrator ──
# Grades by artifact + PR (+ 429-tail override). Sets globals GRADE_RC and prints
# the GRADE line on stderr. Returns 0 always (GRADE_RC carries the verdict).
grade_verdict() {
  local rc="${GRADE_RC_INPUT:-${RC:-0}}"
  local art_result pr_result reset_at log_has_429

  # (1) canonical artifact freshness — required for any non-HEAD-REVIEW grade
  art_result="$(check_artifact "$ARTIFACT")" || {
    printf 'GRADE: HEAD REVIEW reason=artifact:%s\n' "$art_result" >&2
    GRADE_RC=2; return 0
  }

  # (2) PR confirmation — required for clean success and for 429-tail override
  log_has_429="no"
  reset_at="$(detect_429_tail "$LOG")" && log_has_429="yes"
  if ! pr_result="$(check_pr)" ; then
    printf 'GRADE: HEAD REVIEW reason=pr:%s log_429_tail=%s\n' "$pr_result" "$log_has_429" >&2
    GRADE_RC=2; return 0
  fi

  # artifact + PR both pass
  if [ "$rc" = 0 ]; then
    printf 'GRADE: SUCCESS artifact=%s pr=%s/%s\n' "$ARTIFACT" "${REPO:-}" "${PR_BRANCH:-}" >&2
    GRADE_RC=0; return 0
  fi

  # (3) bounded 429-tail override (rc != 0)
  if [ "$log_has_429" = "yes" ]; then
    echo "lane-grade: 429-tail (resets at $reset_at); bounded wait (120s) then ONE grade retry" >&2
    if ! wait_429_reset "$reset_at"; then
      printf 'GRADE: HEAD REVIEW reason=429_decision_timeout(reset>120s_away)\n' >&2
      GRADE_RC=2; return 0
    fi
    # retry once: re-verify artifact freshness + PR (429 cleared, re-echo verdict)
    art_result="$(check_artifact "$ARTIFACT")" || {
      printf 'GRADE: HEAD REVIEW reason=429_retry_artifact:%s\n' "$art_result" >&2
      GRADE_RC=2; return 0
    }
    if ! check_pr >/dev/null 2>&1; then
      printf 'GRADE: HEAD REVIEW reason=429_retry_pr_failed\n' >&2
      GRADE_RC=2; return 0
    fi
    printf 'GRADE: VERDICT-429-TAIL session=%s artifact=%s rc=%s\n' "$LANE_SESSION" "$ARTIFACT" "$rc" >&2
    GRADE_RC=0; return 0
  fi

  # non-zero exit, not a 429-tail -> ambiguity
  printf 'GRADE: HEAD REVIEW reason=nonzero_exit:%s_no_429_tail\n' "$rc" >&2
  GRADE_RC=2; return 0
}

# ── [--probe-only] fixture self-test ──
# Simulates a 404 launch → verifies ladder probe + drift log entry
fixture_self_test() {
  local test_model="solar-pro4:free"  # known dead model for testing
  
  echo "Fixing-C lane self-test: probing with fake 404 model..." >&2
  
  # Run the probe (should detect 404 and try fallbacks)
  local result
  local old_log_size=0
  [ -f "$CATALOG_DRIFT_LEDGERR" ] && old_log_size=$(wc -c < "$CATALOG_DRIFT_LEDGERR")
  
  result=$(probe_fallback_ladder "$test_model" "")
  local probe_exit=$?
  
  # Verify drift log was written (or at least the function ran)
  if [ -f "$CATALOG_DRIFT_LEDGERR" ]; then
    local new_log_size
    new_log_size=$(wc -c < "$CATALOG_DRIFT_LEDGERR")
    if [ "$new_log_size" -gt "$old_log_size" ]; then
      echo "fixture-self-test: PASS (drift log entry written)" >&2
      return 0
    fi
  fi
  
  # Even if no log written, check we got a used_id back
  if [ -n "$result" ]; then
    echo "fixture-self-test: PASS (probe returned: $result)" >&2
    return 0
  fi
  
  echo "fixture-self-test: FAIL (no drift log, no result)" >&2
  return 1
}

# ── args ──
RUN_WORKTREE=1
ARTIFACT=""
LOG=""
RESUME=""
DRY_RUN=0
REPO=""
PR_BRANCH=""
GRADE_RC_INPUT=0
LANE_CMD=()
ACTION=""
PROBE_ONLY=0
LANE_MODEL=""
TASK_FIT=""
RC=0

while [ $# -gt 0 ]; do
  case "$1" in
    --grade) ACTION=grade; shift ;;
    --worktree-standard) ACTION=standard; shift; break ;;
    --probe-only) PROBE_ONLY=1; shift ;;
    --model) LANE_MODEL="${2:-}"; shift 2 ;;
    --task-fit) TASK_FIT="${2:-}"; shift 2 ;;
    --help|-h) usage; exit 0 ;;
    --worktree) RUN_WORKTREE=1; shift ;;
    --no-worktree) RUN_WORKTREE=0; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    --artifact) ARTIFACT="${2:-}"; shift 2 ;;
    --log) LOG="${2:-}"; shift 2 ;;
    --resume) RESUME="${2:-}"; shift 2 ;;
    --repo) REPO="${2:-}"; shift 2 ;;
    --pr-branch) PR_BRANCH="${2:-}"; shift 2 ;;
    --rc) GRADE_RC_INPUT="${2:-0}"; shift 2 ;;
    --) shift; LANE_CMD=("$@"); break ;;
    --*) echo "lane-runner: unknown option: $1" >&2; usage; exit 2 ;;
    *) echo "lane-runner: unexpected arg: $1" >&2; usage; exit 2 ;;
  esac
done

[ "$ACTION" = standard ] && { print_contract; exit 0; }

# ── [--probe-only] fixture self-test ──
if [ "$PROBE_ONLY" = 1 ]; then
  fixture_self_test
  exit $?
fi

# lane session id; Phase A populates it from the hermes session id at run time
# (recoverable via `hermes --resume`). Skeleton stubs a stable token for now.
LANE_SESSION="${LANE_NAME}-$(date +%s)"
LOG="${LOG:-/root/.hermes/cache/scratch/${LANE_SESSION}.run.log}"
mkdir -p "$(dirname "$LOG")"
# run-window start epoch; grading uses max(start-5m, start+10m) for artifact freshness.
RUN_WINDOW_START="${RUN_WINDOW_START:-$(date +%s)}"

# forward --resume to the lane command (a `hermes chat` invocation)
RESUME_FLAG=()
[ -n "$RESUME" ] && RESUME_FLAG=(--resume "$RESUME")

# ── --grade: run ONLY the grading contract (self-test / CI verdict) ──
if [ "$ACTION" = grade ]; then
  grade_verdict
  exit "${GRADE_RC:-2}"
fi

print_contract

# ── Phase B: enforce the worktree standard (degrade when no git/bridge checkout) ──
if [ "$RUN_WORKTREE" = 1 ]; then
  if resolve_worktree; then
    echo "lane: worktree=$WORKTREE_DIR branch=$WORKTREE_BRANCH (origin/main)"
  else
    echo "lane: WARNING — no git repo or origin/main; worktree isolation not enforceable; using scratch dir" >&2
    WORKTREE_DIR="$(mktemp -d /root/.hermes/cache/scratch/lane.XXXXXX)"
    CLEANUP=1
  fi
else
  WORKTREE_DIR="$(mktemp -d /root/.hermes/cache/scratch/lane.XXXXXX)"
  CLEANUP=1
fi

# ── CATALOG DRIFT: launch test + probe fallback ladder on 404 ──
# Check if we have a model to use
if [ -n "$LANE_MODEL" ]; then
  echo "lane: using model $LANE_MODEL"
  
  # Quick probe: is the model alive?
  model_live=$(probe_model_id "$LANE_MODEL" 1 "$LOG")
  
  if [ "$model_live" != "OK" ]; then
    # Model 404'd - probe the fallback ladder
    echo "lane: model $LANE_MODEL 404'd, probing fallback ladder..." >&2
    used_model=$(probe_fallback_ladder "$LANE_MODEL" "$TASK_FIT")
    
    if [ -z "$used_model" ]; then
      echo "lane: ALL model probes FAILED - no fallback available" >&2
      echo "CATALOG-DRIFT: $LANE_MODEL 404'd → all fallbacks exhausted" >&2
      RC=1
    else
      echo "lane: using fallback model $used_model"
      LANE_MODEL="$used_model"
    fi
  fi
fi

# ── Phase A: run the lane, capture exit code (NOT its exit — verdict is next) ──
if [ "$DRY_RUN" = 1 ]; then
  echo "lane: dry-run — resolved worktree, no lane command executed"
elif [ "${#LANE_CMD[@]}" -gt 0 ]; then
  : > "$LOG"
  cd "$WORKTREE_DIR" || { echo "lane: cannot cd to $WORKTREE_DIR" >&2; RC=1; }
  if [ "$RC" -eq 0 ]; then
    # Prepare model flag if we have a validated model
    MODEL_FLAG=()
    if [ -n "$LANE_MODEL" ]; then
      MODEL_FLAG=(--model "$LANE_MODEL")
    fi
    # lane command is expected to invoke `hermes chat` (prints session id on exit).
    "${LANE_CMD[@]}" "${RESUME_FLAG[@]}" "${MODEL_FLAG[@]}" 2>&1 | tee -a "$LOG"
    RC=${PIPESTATUS[0]}
  fi
else
  echo "lane-runner: no lane command (use: lane-runner.sh -- <cmd> ...)" >&2
  RC=0
fi

# ── diagnostic verdict line on ANY exit ──
emit_verdict "$LANE_SESSION" "$ARTIFACT" "$RC"

# ── Phase A grading contract: grade by artifact + PR (+ 429-tail override) ──
GRADE_RC=0
if [ "$DRY_RUN" = 0 ] && [ -n "$ARTIFACT" ]; then
  grade_verdict
fi

# ── cleanup: reap the worktree (Phase A may keep it on HEAD REVIEW -> reviewed by head) ──
if [ "${CLEANUP:-0}" = 1 ] && [ "$DRY_RUN" = 0 ]; then
  if [ -n "${WORKTREE_TOPLEVEL:-}" ]; then
    git -C "$WORKTREE_TOPLEVEL" worktree remove --force "$WORKTREE_DIR" 2>/dev/null || true
    git -C "$WORKTREE_TOPLEVEL" worktree prune 2>/dev/null || true
  else
    rm -rf "$WORKTREE_DIR" 2>/dev/null || true
  fi
fi

exit "${GRADE_RC:-$RC}"