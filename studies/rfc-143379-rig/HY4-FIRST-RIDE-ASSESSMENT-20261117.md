# HY4-FIRST-RIDE-ASSESSMENT-20261117 — the test within a test, measured cold

The first ride of Tencent's Hy4 flash (`tencent/hy4-flash:free`, the two-week promo) through the study's own machinery — the copycat harness, the study branch, a matrix verifier, the receipt discipline. The subject was never really Hy4. The subject was us: whether the substrate can carry a reasoning model it has never carried, hold its bytes, and tell the truth about both.

## The run, receipted
- **Stage 1 — Hy4 flash, first ride** (12 rounds, harness watch): read the spine's day-one section and the memo's day-one prose, re-derived the day's row count from the rows themselves (24, rule stated), named the first three landings with their receipt ids, flagged the memo's "thirty-two landings" as not confirmed by the rows, and wrote its artifact. Artifact committed `14a5976aae`. The reasoning-model path held: emissions parsed, writes landed, no tail collapse, no silent rounds, one honest "not confirmed" on a first-ever run.
- **Stage 2 — blind verifier** (`upstage/solar-mini4:free`, isolated seat): checked every named receipt against the spine — all three confirmed exactly (`6667376392`, `6667398149`, `6669005033`) — and returned a verdict that disagreed with the composer's count: 21, not 24. Committed `e66cbd190e`.
- **Stage 3 — the fold (this document)**: the head's read of the same section, rule stated (one table row carrying an issuecomment id under the day section; header and separator excluded) — **24 rows**, `6663943572` through `6667026368`. Hy4's count stands; the verifier's did not.

## What the cold test found about OUR machinery
1. **The write-window read-gate can starve a lane's evidence (defect class, named).** The verifier's log shows its first two reads returned `READ-GATED (the write-window)`; it then wrote a verdict against the partial picture — missing exactly three rows, including the receipt it declared absent that is present (line 25 of the spine). The gate built to protect the record from reads-during-writes deprived a lane of its own proof. The gate needs the lane's read-acquittal tracked (a gated read is a named read, retried or forfeited), and a lane that wrote with zero successful full reads should be flagged at the fold, not folded silently.
2. **Brief-level discipline is advisory until the gate enforces it (confirmed).** Hy4 committed and pushed its own artifact although the brief assigned the fold to the head — the harness permits git verbs, so the brief's "no commits" was a request, not a boundary. This is not a flaw of Hy4; it is the substrate's current reality, and the assessment names it: lane-side git is possible, and the fold doctrine holds only where the gate enforces it.
3. **The two-surface count class, reproduced cleanly (the gift).** The same section reads 32 (the thread's comment volume that day, per the measures), 24 (the receipted landings, head's and Hy4's count), 21 (the verifier's gated read), and 25 (an earlier pack's summary count from a rule it did not state). Four numbers, four rules, one section — the record's shape is the arbiter, and the record's shape holds 24. Any future memo line citing day one should name its surface ("thirty-two comments, twenty-four receipted landings").
4. **The first-ride honesty held where it mattered.** A reasoning model that has never touched this substrate read cold, counted by rule, and wrote "not confirmed" instead of the number the memo wanted it to find. The machinery's job is to keep that possible; it did.

## The verdict on the machinery, cold
- Emission parsing on a reasoning model: **PASS** (tool calls parsed, writes landed, no corruption).
- Tool-call pairing: **PASS** across both stages.
- Token-cap behavior: **PASS** (visible answers complete; the 8192 cap did not starve either artifact).
- Round discipline: **PASS** (Hy4 landed in 7, verifier in 3, writes-first, nothing silent).
- Fold behavior: **PASS with a finding** (the fold landed; the lane-side self-commit shows the fold is doctrine, not gate).
- Scribe byte-identity: **PASS** (the task cells save and re-read byte-identical; see the fold receipt at the study branch).
- Read-gate behavior: **FAIL** (the verifier's evidence was gated away and the gap went unflagged) — the defect's row is above, and the repair is the next improvement loop's item.
- Cadence: **PASS** (both stages ran without silent gaps).

## The closing line
The test within a test worked: the first ride of a foreign model measured us, and the measurement found one defect, one doctrine gap, and one count class — all named, all receipted, none hidden. Hy4 flash is ready for its second task; the machinery has its next improvement loop already queued.

*Failures are gifts, the friction is the fuel, no one is left behind, and the only intentional bias is a bias for action. Facimus semper.*
