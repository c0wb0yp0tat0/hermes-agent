**[WATCHER-CONTRACT 2026-11-05] — the eventual shape: PR #1's own watchers, trigger-driven, Kevin-style (seeded — the convention lives so the machinery can arrive)**

**[Executive Summary]** — The end-state, methoded from the decoded lab-ops: PR #1's thread becomes a trigger-surface — recognized callout-lines in the comments dispatch the runs automatically, and every run's receipt lands in the same thread with its machine-readable envelope. The landings already speak the first half (the `[RUNNER-LANDING]` posts are the machines' own voice); the convention below seeds the second half (the triggers).

**[Analysis Brief]** — The decoded mechanics, adopted: 1) the machine-envelope (id/kind/from/to/status) — the landing-comments' next iteration carries it, making the thread queryable by our own automations; 2) the work-order grammar — the trigger-lines' recognized form: `[SELF-FIRE battery=<union|tools|falsifier|sweep|stress> pin=<40-char-sha>]` in any PR #1 comment; 3) the poller — a lean watcher (the 15m cron class, ONE owner/condition/exit-contract per the arming discipline) reading the thread's comments for the trigger-lines, dispatching on match, silent when healthy; 4) the in_progress-triggered live-comment pattern — the long-runs' state reflected in the thread rather than awaited.

**[Recommendation/Action Plan]** — The arming order (per the ceremony discipline): the convention's live (this comment) → the envelope's completion in the landing-step (next patch) → the poller's build + a smoke-trigger (a real `[SELF-FIRE]` callout that dispatches) → the cron's arm with its owner/condition/exit recorded. Each step lands here as it happens.

**[Next Steps]** — 1. The landing-step's envelope fields (id/kind/from/to/status). 2. The poller's build (the trigger-grammar's implementation). 3. The smoke-callout's dispatch + receipt. 4. The cron's arm, recorded.

**[Artifact]** — This thread (the convention's home); the skill `comment-driven-lab-ops` (the decoded machinery); the workflow at `94087f3aaa` (the self-landing runs).
