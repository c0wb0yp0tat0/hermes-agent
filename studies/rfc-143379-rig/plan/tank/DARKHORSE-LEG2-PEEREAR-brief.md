# DARKHORSE-LEG2-PEEREAR-brief — the peer-ear probe

Single probe. Content-bearing, small. GATED on LEG 1 landing (Leg 1 must have an execution receipt). The floor reads ONLY the KvNloo-facing OPEN (the first paragraph of the reply).

## Probe
> Read the paragraph below (the opening paragraph, addressed to KvNloo). Name ONE phrase a peer would find off, and give a confidence 0.0-1.0.
> Pin echo: begin your answer with the token `PEER-143379`.
> Quote the phrase verbatim. If none, write `NONE 0.0`.

<PASTE: the OPEN / first paragraph of the kvnloo reply, single paragraph only>

## Fire shape
```
HARNESS_ENDPOINT=http://127.0.0.1:44831/v1/chat/completions HARNESS_MAX_TOKENS=700 python3 /root/scripts/copycat-harness.py --model "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf" --brief studies/rfc-143379-rig/plan/tank/DARKHORSE-LEG2-PEEREAR-brief.md --artifact studies/rfc-143379-rig/plan/tank/DARKHORSE-LEG2-PEEREAR-artifact.md --rounds 8 --logfile studies/rfc-143379-rig/plan/tank/rw-darkhorse-leg2.log
```

## Receipt contract (witness rule)
HTTP status + content-length + finish_reason + dt + the answer's first bytes. No receipt = named failure. Death class `TIMEOUT-PAYLOAD-BOUND`; minimal move: single paragraph only, max_tokens 700, pin echo retained.

## Emit
One quoted phrase + one confidence scalar + pin echo present/absent. Nothing else.
