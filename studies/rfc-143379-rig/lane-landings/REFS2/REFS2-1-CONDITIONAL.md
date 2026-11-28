# REFS2-1 — CONDITIONAL PROBABILITY SHRINKS THE SAMPLE SPACE (head pre-read)
Source: https://iknahar.medium.com/conditional-probability-shrinks-sample-space-35262e87c5e3
(Medium, Kamrun Nahar, ML/stats-with-Python writer; fetch = HTTP 500 — the title + the core are
textbook-standard; the packet is the mechanism, honestly labeled HEAD-DISTILLED, not quoted.)
CORE: P(A|B) = P(A∩B)/P(B). Conditioning REPLACES the sample space with B — the denominator
shrinks to the conditioning set, so a rare event inside B becomes large relative to B, and a
common event outside B disappears from view. The posterior redistributes mass by evidence.
THE PYTHON TIP: filter-then-measure — measure rates on the CONDITIONED rows (df[cond]) before
ever quoting a whole-corpus rate; the whole-run average is the un-conditioned baseline.
TRANSFER HOOKS (for the study): (1) the miss-rate discriminator measured conditioned on the
topic's last-touch age (P(miss | anchor-cold) vs P(miss | in-window)) — the whole-run rate hid
the failure (the air mass); conditioned rates amplify it. (2) The K-window claim is itself a
conditional: P(correct | literal in K-window) — the correct comparison basis. (3) A divided
gate: the write-gate's outcomes conditioned on action (read vs write) instead of pooled.
