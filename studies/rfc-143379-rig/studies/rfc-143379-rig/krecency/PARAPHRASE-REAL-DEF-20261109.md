# PARAPHRASE_REAL — the definition (the gap's closure, the failure-clause's F2)

**The RFC's protocol line:** "paraphrase real, not mocked, for the certifying run (mock +1.1pp is a sanity check only)."

**The definition:** paraphrase_real is the instrument's transformation of the probe's stream tokens — each cycle-call may carry a `paraphrase_fn(token) -> token'` that rewrites the quoted/queried literal into a semantically-equivalent but surface-different form (synonym substitution, case/word-order variance), so the retrieval must match the CONTENT, never the surface bytes. Its contract:
1. A paraphrase_fn, when provided, is applied to the queried literal BEFORE the window-check (the query's surface differs from the stored token's).
2. The k=0 baseline stays paraphrase-blind (the 1/ratio named baseline — the seam's registered, never silent).
3. The certifying re-run with paraphrase_real defined (a concrete fn: case-variance + synonym tails) executes within the sprint's first hour and lands its receipt in krecency/results/ — a claim of the paraphrase-dimension without that receipt stays STANDING per the guard-clause door #3.
