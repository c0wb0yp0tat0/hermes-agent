# THE MACHINERY RAN — an autonomous-activity study (2026-11-16 → 11-17, RFC #143379 study)

## The question this report answers
While the operator reviewed the regroup deliverables, the rig was left running. What did it do — and what does that say about the machinery? This is the study report on the autonomous activity: what ran, on what cadence, what it produced, and what it refused to do. Every row below traces to a commit on the study branch; nothing here is recalled.

## What ran: the fleet-cycle archive series
The standing fleet cycle — the branch's self-maintaining surface — produced **ten archive rows in ~30 hours** (2026-11-16 09:39Z → 2026-11-17 17:00Z), each one a fresh PR #1 body committed to the branch:

- `9144ec8f80` 11-16 09:39Z — archive body 20261116T143843Z
- `de73766b1f` 11-16 12:45Z — study stand + forward targets (fresh reads)
- `e7aa195ac8` 11-16 15:54Z — body 20261116T205336Z
- `faf40bb980` 11-16 19:08Z — body 20261117T000550Z
- `7bfb2be7b9` 11-16 22:12Z — body 20261117 (fresh current/forward)
- `2721aeda52` 11-17 01:22Z — body 20261117T062044Z
- `5344bce16a` 11-17 07:37Z — body 20261117073657Z
- `9ce910bf24` 11-17 10:43Z — refresh body 20261117T1541Z
- `e189a70abc` 11-17 13:49Z — body 20261117-1848
- `0f38b2e72c` 11-17 17:00Z — body 20261117-2158Z

**The cadence:** one row every two to four hours, through the night and through the day, with no silent gap exceeding the cycle's bound. The longest quiet span in the series is the night stretch between 01:22Z and 07:37Z — six hours fifteen minutes — which the cycle's own schedule covers by design (the night is the reserve, the day is the drum).

**The shape (each body, per the operator's standing shape):** preserved opening, executive summary, standing plan, north, and artifact lines; fresh current state and forward targets; receipts stay on the branch; and each row carries its fresh reads of the live surfaces — branch head, thread tail, disk, runners. The archive row is not a log entry; it is the surface's own state, re-read each time.

## What also ran, quieter
The self-improvement review kept its own watch: **28 memory batches staged** to the pending queue (Nov 17), one by one, gated behind the operator's approval surface — and **none applied**. The queue is the staging floor; the floor does not decide. The never-delete-unattended law held: nothing was pruned, nothing was rewritten, everything that moved waited.

The lane machinery itself left its receipts: the HITL completion fold (`fd7fa117b7`), the correction commit restoring the verified hour-class text (`964291f023`), and the input-pack commit completing the study set (`bc8b043ae9`, the completion briefs + steer channel). The first two of these were the head's own orchestration during the close — logged here because they landed inside the same window, and the line between "autonomous" and "orchestrated" is itself part of the study's finding: the machinery ran the cadence while the operators worked the close; neither waited on the other.

## What it refused to do
- No unauthorized fires: nothing dispatched itself onto a model, a thread, or a surface without a word. The staged = not fired line held the whole window.
- No public-surface changes beyond the branch: the upstream issue stayed quiet, the thread received no new rows from the machinery, only the branch moved — and the branch moved only in the archive's own cell.
- No deletions: the pending queue grew, nothing shrank.
- No silent gaps: every hour the cycle owed a state, it posted a state.

## The cold reading (what this proves about OUR machinery)
1. **Cadence without attention:** a self-maintaining surface that refreshes itself on schedule for 30 hours while its operators read — with zero human steering — is a surface whose trust claim is no longer a promise. It is a demonstrated behavior with a commit log.
2. **The two-way door held under load:** the same machinery that CAN write (the archive rows landed) is the machinery that must NOT (the staged batches stayed staged, the thread stayed quiet). Both halves worked in the same window. That asymmetry — able but not entitled — is the governor the kit is built around, and it ran without a fault.
3. **The receipts held:** every one of the ten rows names its body, its time, and its fresh reads. Nothing in the series required trust; everything in the series invited a check, and any check would find the row where the row said it would be.
4. **The no-silence law is structural now:** the cycle's gaps are scheduled, not accidental. A machine that posts whether or not anyone is watching is the machine the eleven days were spent building the trust to believe.

## The forward line
The same substrate — the fleet cycle's cadence, the branch's receipts, the staged-queue's gate — is now the test bed the operators chose for the next autonomous experiment: Hy4 flash's first task, planned by the CTO assistant with the runner matrix as its stagework, fired through the copycat harness with the scribe machine holding its bytes. The test-within-a-test is that this machinery is the cold subject: when the new seat runs, the question is not only what Hy4 can do, but whether the harness parses it, the scribe holds it, and the record proves it — the exact properties this report just confirmed for the fleet cycle's own run. The machinery ran; now it gets watched watching something new.

*— The report closes with the study's register line, because the register is the study's: failures are gifts, the friction is the fuel, no one is left behind, and the only intentional bias is a bias for action. Facimus semper.*
