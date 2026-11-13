# THE NEMO-BRIDGE (the memory-tool hybrid scope, 11-11)

## The gap
Nemo-class seats are tool-shy: they produce prose-promises ("I will use the read_file tool") instead of tool_calls (R3: 14 promises, 0 calls). The native instruction-boundary fails.

## The vehicle
The rig's memory-tool (tools/memory_tool.py, 485 lines): the persistent curated store, the batch-entry resolution, the write-gate + staging, the provenance rows. Its proven power: making agent outputs GROUNDED (read-gated, write-staged, entry-formed).

## The bridge (the hybrid)
A memory-first tool wrapper — buildable as `scripts/memory_bridge.py`:
1. STORE-LOAD: import load_on_disk_store(); the lane's mission-brief curates the relevant memory-blocks into the request's system-turn.
2. MEMORY-PING: every tool-opportunity is attached to a required read-back — the agent must cite the entry it read before ANY act; the act is framed as "record/update this entry" (a memory operation), not a free-standing tool call.
3. WRITE-BACK: the lane's outputs route through the store's gate (the entry-form, the provenance-row, the staged write) — the outputs ARE memory-writes, gated like the memory-tool itself.
4. THE NEMO-TEST (the falsifier): the A/B — the same task with vs without the bridge on mistral-nemo (tools request + max_tokens 400): the bridged request must elicit a tool_calls response; the unbridged must not (or a weaker one). The bridge WORKS iff Nemo flips.

## The deliverable
The first-pass read-side scaffold (the store-load + the system-block assembler + the ping-requirement) — working, testable against Nemo tonight.

## THE WIDER DOOR (the operator's read, 11-11)
The bridge is seat-agnostic — it lifts ANY tool-shy model, and the highest-need members of that class are the LOCAL models (the small/quantized seats whose tool_calls emission is unreliable). The bridge makes the local floor viable: the same bridged payload against the local endpoint (llama.cpp/sandbox-LM serve) is a config change, not a rebuild. The sustainable door now has its enabler; the local POC's shape is the bridge + the local serve.
