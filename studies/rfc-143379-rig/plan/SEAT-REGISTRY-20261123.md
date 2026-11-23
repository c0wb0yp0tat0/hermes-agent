# SEAT-REGISTRY — the executor's runner/seats map (materialized from the approved STAGE-PLAN-FLEETMATRIX-20261123.md, 94fbb17b2d; no inventions)

## The runners (the walk-fleet's map, probed live 2026-11-23)
| alias | channel | os | machine | busy |
|---|---|---|---|---|
| p0tat0 | c0wb0y@100.98.69.7 | Linux | c0wb0yp0tat0 (241) | false |
| c0wb0y | c0wb0y@100.70.143.25 | Windows | DESKTOP-8R44VEP (241) | false |
| pve1 | (local) | Linux | pve-1 (THIS host) | false |

## The forks (the approved plan's table 1-b)
| fork | sha | identity |
|---|---|---|
| study HEAD | f652b71b4e | pre-restore (no read arm) |
| pr-139606 | d1bdb4582c | write-gate (feat/135039) |
| pr-141876 | 6609dac951 | restore (fix/restore-read-action) |
| a9c65dc4 | a9c65dc43d | combined (memory-chain-doc-read-combined) |

## The seats (per the plan's 1-c + the fleet-doctrine)
- Flagship-class: hy4-flash:free (the window), solar-mini4:free (the secondary), longcat-2.5:free + stepfun-3.7-flash:free (the support).
- The paid seat: openai/gpt-6-luna (the trusted window, the intended carriers).
- The local seat: the darkhorse (the DeepSeek-V4-Pro-Qwen3.5-9B at 44831 — host-matched tasking only).
- The envelope: the dispatch pacing cap per runner (the fair-share slot per the free-meter).

## The legs (the executor's runner-assignments, per the plan's 12-leg matrix)
- The negative-control legs: study HEAD × every runner — NOT-RUN-with-reason (the read-arm's absence), never a failed run.
- The combination legs: pr-141876 × p0tat0/c0wb0y/pve1 (the 4/4 read-suite's verification), pr-139606 × pve1 (the write-gate S7's verify), a9c65dc4 × p0tat0 (the combined's chain-docs) — each boarded with its envelope-receipt.
