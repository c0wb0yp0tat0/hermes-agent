# Cache Index — "The Sam Altman Firing" Deep-Dive

**Video:** `https://www.youtube.com/watch?v=_eYTkvZqbnQ` (runtime ~39:58)
**Method:** Doc-driven, no-assume, objective. Text/transcript-only for Stages 1–2; visuals deferred per user.
**Workflow status:**
- [x] Stage 1 — Framing analysis: fact vs. opinion vs. rhetoric → `01_framing.md`
- [x] Stage 2 — Sources inventory (identify, don't yet verify) → `02_sources.md`
- [x] Stage 3 — Assess each source the same way (verification pass) → `03_verification.md` (**ALL 19 cached sources reviewed, incl. addendum §3.11**)
- [x] Stage 4 — Root-layer dig — Part A (creator context: AI In Context / 80,000 Hours) → `04_creator_context.md`; Part B (Musk v. Altman docket 4:24-cv-04722-YGR + exhibits DX-304/315/1046/309/302/1048 + S11 corroboration) → `04b_root_layer_exhibits.md`. **Root-layer claim VERIFIED at primary-document tier.**
- [x] Stage 5 — Regroup & discuss — THIS ROUND
- [x] Stage 6 — Tangents held (see `02_sources.md` "Flagged Tangents" + `03_verification.md` §3.10)
- [x] Stage 7 — Q/C/C surfaced at regroup

**Note on Obsidian:** `OBSIDIAN_VAULT_PATH` unset and no vault at `~/Documents/Obsidian Vault` → would require setup, which user excluded. Note-tracking kept in the file-based cache (working, under budget).

**Budget:** 12 GB cap lifted by user (mid-session). Cache total ≈ 11.1 MB of available space — storage was never a binding constraint; the real limits were extract-tool truncation (resolved) and DocumentCloud auth-walling (handled via viewer-page text).

**Raw material:**
- `transcript_raw.txt` — full YouTube transcript (1,177 lines, ~45K chars), fetched via youtube-transcript-api.
- NOTE: Transcript is auto-captioned; minor artifacts expected (see Stage 1, item on "$13").

**Legend for claim tags:**
- `[FACT]` verifiable external assertion
- `[QUOTE]` attributed speech — verify accuracy + provenance
- `[OPINION]` creator's interpretation / value judgment
- `[FRAME]` rhetorical or narrative device
- `[UNVERIFIED]` asserted as fact, no source shown in video, needs check
