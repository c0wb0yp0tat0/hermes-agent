# DARKHORSE-LEG3-SYNTH-brief — the synthesis leg (floor-side record; assembly is mine)

Single assembly, no model fire. GATED on LEG 1 and LEG 2 both landing with receipts. Collect the two leg answers, then for every quoted line locate the exact byte span in the source kvnloo reply and bind it to a byte citation.

## Inputs
- Leg 1 answer: the named unsourced clause + weakest line (verbatim).
- Leg 2 answer: the named off phrase + confidence (verbatim).
- Source kvnloo reply file (the ground truth for byte verification).

## Procedure
1. For each quoted line, search the source file for the exact byte sequence.
2. Record file path + byte offset (and sha256 of the quoted span).
3. If a quote cannot be byte-matched, mark it `UNSOURCED-BYTE-CHECK-FAIL` — never silently accept it.
4. Compose the drown-proof record: each named clause line, quoted verbatim, with its byte citation beside it.

## Emit
The drown-proof record: N named lines, each with (quote, file, byte offset, span-sha256). No line without a byte citation counts. This leg is the assembly + the receipt.
