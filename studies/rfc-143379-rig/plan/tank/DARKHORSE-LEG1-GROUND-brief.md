# DARKHORSE-LEG1-GROUND-brief — the floor's ground-read probe

Single probe. Content-bearing, small. The floor reads ONE section of the kvnloo reply: the PRE-REGISTRATION paragraph only (paste that single paragraph as the payload — do not paste the full reply).

## Probe
> Read the paragraph below (the PRE-REGISTRATION paragraph of a peer reply). Answer only:
> (a) quote any clause in it that reads as unsourced;
> (b) quote the weakest line in it.
> Pin echo: begin your answer with the token `GROUND-143379`.
> If a field has no candidate, write `NONE`. Quote verbatim; do not paraphrase.

<PASTE: the PRE-REGISTRATION paragraph of the kvnloo reply, single paragraph only>

## Fire shape
```
HARNESS_ENDPOINT=http://127.0.0.1:44831/v1/chat/completions HARNESS_MAX_TOKENS=700 python3 /root/scripts/copycat-harness.py --model "/root/.lmstudio/models/imported/DeepSeek-V4-Pro-Qwen3.5-9B-MTP/DeepSeek-V4-Pro-Qwen3.5-9B-MTP-Q4_K_M.gguf" --brief studies/rfc-143379-rig/plan/tank/DARKHORSE-LEG1-GROUND-brief.md --artifact studies/rfc-143379-rig/plan/tank/DARKHORSE-LEG1-GROUND-artifact.md --rounds 8 --logfile studies/rfc-143379-rig/plan/tank/rw-darkhorse-leg1.log
```

## Receipt contract (witness rule)
HTTP status + content-length + finish_reason + dt + the answer's first bytes. No receipt = named failure, never a pass. Client-side 540s timeout / payload-bound hang = death class `TIMEOUT-PAYLOAD-BOUND`; minimal move: re-fire with the single paragraph only, max_tokens 700, pin echo retained.

## Emit
One unsourced clause (verbatim) + one weakest line (verbatim) + pin echo present/absent. Nothing else.
