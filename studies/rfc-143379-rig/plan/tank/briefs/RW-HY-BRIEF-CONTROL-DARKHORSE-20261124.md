# FLEET-BRIEF HY — CONTROL THE DARKHORSE (the floor's drown-proof read, fired BY YOU)

*Seat (pin): `tencent/hy4-flash:free` — the CONTROLLER. The operator's standing (2026-11-24): "Hy was supposed to be babysitting… hy controlling darkhorse themselves (the point)." The floor = the local GGUF at `127.0.0.1:44831` (served id: `/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf`). The harness gate now WHITELISTS `curl -s [-m N] http://127.0.0.1:44831` in lanes — the floor's control channel is yours. Branch: `study/rfc-143379-rig-20261105`. Fire: now.*

## The mission

The full reply (`RW-FULL-REPLY-20261124.md`) needs its star addition: the floor's OWN drown-proof read. You ARE its babysitter: fire the three probes, capture its answers verbatim, assemble the record. The floor answers SMALL probes (measured: 13–19 s per 80-token probe, content-bearing with a `thinking` prefix); it HANGS on big payloads — so each probe is ONE short question, clamped.

## The three probes (fire each with curl, exactly this shape)

**PROBE 1 — the weakest clause (the pre-registration paragraph's weakest line).**
```bash
curl -s -m 90 http://127.0.0.1:44831/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf","messages":[{"role":"user","content":"GROUND-143379: quote the weakest line in this sentence. The arm is pre-registered: test test_doc_reader_and_writer_keep_latest_live_state at a9c65dc4, row 7143199711, predicts green 17/17 as at a9c65dc4, red 16/1 both removed."}],"max_tokens":80}'
```

**PROBE 2 — the peer-ear (the opening's off beat).**
```bash
curl -s -m 90 http://127.0.0.1:44831/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf","messages":[{"role":"user","content":"GROUND-143379: ONE phrase in this opening would make a peer pause. Opening: You are right, and I should have caught it. The claim came from your 11-23 matrix. Quote the phrase."}],"max_tokens":80}'
```

**PROBE 3 — the unsourced clause (the channel paragraph).**
```bash
curl -s -m 90 http://127.0.0.1:44831/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf","messages":[{"role":"user","content":"GROUND-143379: quote any clause in this sentence that reads as unsourced. The rate moved 0 to 70 percent on channel alone: raw 0 of 40 answered, history visible 26 then 31, fact in question 29."}],"max_tokens":80}'
```

## The required artifact

`/root/workspace/repos/hermes-agent/studies/rfc-143379-rig/plan/tank/RW-DARKHORSE-READ-20261124.md`:
1. Each probe's full execution receipt: the exact curl fired, HTTP status, finish_reason, dt, and the floor's answer BYTES verbatim.
2. The synthesis: for each probe, the floor's quoted clause/line/phrase — byte-verified to the reply's actual sentences (diff-style receipt: reply sentence vs floor's quote).
3. A verdict: what the floor's read ADDS to the reply (a named clause, a tightened register beat) — plus the floor's reading's own weak spot (whatever the floor missed, named honestly).
4. The star block: the exact text to append to the reply as its star addition, marked `## STAR-ADDITION`.

## Write-window

`write-window: 9` — probes by round 7, the record by round 12. NO stub markers. If a probe hangs (no JSON in 90 s), receipt it as the floor's hang class and CONTINUE with the next probe — the class is named, never a wall.

## Hard lines (binding)

- PREVIEW ONLY — nothing posts to the RFC surface; PR #1 the only other allowed surface. The reply file itself is NOT modified by you — your star block rides the artifact; the head applies it at the fold.
- No installs. All reads LOCAL (read_file the reply for byte-verification). `git add` + commit locally, NEVER push/pull. Never checkout/stash/rm. `ls-remote` first.
- THE WITNESS RULE: every quoted floor-word is the answer's real bytes; a quote not in the transcription is a strike, never a pass.

## Emission

Exit 0 = the record EXISTS on disk, re-read, committed; the report names the sha + the three dt's. No tool-call syntax in final words.

## The armament + name-and-refuse

**Armed:** think-tank (the spine; the wall clause) · the floor's greens recipe (small probes, clamped, content-bearing) · investigation-documentation (per-probe receipts).
**Refused:** any public write · installs · web reads · memory-chain · config/gateway · github writes · coding legs · fan-outs · creative families.

## The LP envelope

- **Customer Obsession:** the floor's own read lands in the reply it will sign — its words, its receipts.
- **Ownership:** the seam is yours until the record is on disk, re-read, committed.
- **Bias for Action:** the floor answers in seconds; fire all three NOW.
- **Dive Deep:** per-probe bytes.
- **Deliver Results:** the star addition receipted, the reply's drown-proof complete.

**THE WALL CLAUSE:** a non-reproduction is a QUESTION with a constructed minimal move — the smaller probe, the clamped budget, the re-run — before any verdict. A real wall lands with its receipts, named as a finding.
