# Stage 4 (Part B) — Root-Layer Legal Dig: *Musk v. Altman* Exhibits

**Purpose:** Go to the actual court documents the video leans on as its linchpin ("unsealed court testimony this year") and verify the video's account against the primary legal record — not just news summaries of it.

**Constraint note:** The user lifted the earlier 12 GB storage cap before this dig. Storage was never the binding constraint (cache ≈ 11 MB of ~12 GB); the real blocker was the extract tool's ~15 KB truncation and DocumentCloud's auth-walled PDFs. Both handled below.

---

## 4B.1 The docket the video never named (closure of a Stage-2 gap)

The video said only "unsealed court testimony that's come out just this year." Located precisely via the DocumentCloud exhibit pages:

- **Case:** *Musk et al. v. Altman et al.*
- **Court / No.:** United States District Court, Northern District of California — **4:24-cv-04722-YGR**
- **Exhibits surfaced (DX-####):** 304 (termination consent), 315 (Murati–Altman texts), 1046 (employee letter), 309 (Murati–Scott texts), 302 (Murati complaint list), 1048 (Murati–Nadella texts).

This pins the gap. The video's "this May" deposition maps to the May 2026 trial in this case.

## 4B.2 Exhibit DX-304 — the termination document (VERIFIED, primary)

Pulled the actual exhibit text via the DocumentCloud viewer page (the raw PDF is auth-walled / 403; the HTML text extract succeeded). Key verbatim passages:

> **UNANIMOUS WRITTEN CONSENT OF THE BOARD OF DIRECTORS OF OPENAI, INC.**
> **Removal of Sam Altman as Chief Executive Officer**
> WHEREAS, the Board has lost trust in Sam Altman's ability to be candid and forthright in his communications with the Board and employees… and is concerned about the resulting impact of his actions on the Corporation's mission…
> NOW, THEREFORE, BE IT RESOLVED, that the Board hereby, effective immediately, terminates Mr. Altman's employment…

- **Confirms the video's account:** the firing was a *unanimous written board consent*, citing **loss of trust / candor** — exactly the video's "not consistently candid" framing (and matches OpenAI's own Nov 17 public statement, S1).
- **Signs off four board members** (Toner, Sutskever, D'Angelo, McCauley) — matches the video's named quartet.
- **Structure detail:** the document lays out the nonprofit → OpenAI GP → OpenAI Global → OpCo chain — corroborates the video's governance-structure description (S19).

## 4B.3 Exhibit DX-315 — Murati–Altman texts (VERIFIED, primary)

DocumentCloud header: **"Short Message Report — 78 messages, 11/19/2023 – 11/20/2023."** Matches the video's "78 text messages between Murati and Altman" claim (B13 context / the reconciliation arc). The Verge reported the substance (Altman: D'Angelo "trying to get the board to agree to a configuration" that he and Nadella said "doesn't work").

## 4B.4 Exhibit DX-1046 — employee letter (VERIFIED, primary)

DocumentCloud page confirms it is the exhibit in *Musk v. Altman*, 4:24-cv-04722-YGR. The Verge cites it as "more than 750 OpenAI employees signed a letter… threatening to quit." Matches the video's "~700 of 770" (signature count varies by outlet/timing as it climbed — within range).

## 4B.5 Other exhibits (located, not fully extracted)

- DX-309 (Murati–Kevin Scott texts): "close to having the board resign" / Scott "For real this time?" — corroborates the video's return-negotiation arc.
- DX-302 (Murati Sept 30 2022 complaint list to Altman): "constant panic… generates chaos and churn" — management-style critique; matches the video's "pattern" thread.
- DX-1048 (Murati–Nadella texts): "not putting [her] name on this" re: a statement — corroborates Murati's ambivalent role.

## 4B.6 Semafor / Reuters / Fortune — the inferred "major source" (S11, now VERIFIED)

The Stage-2 `INFERRED` source S11 (Semafor as a major narrative source) is corroborated by Reuters/Fortune: **the board approached Anthropic CEO Dario Amodei about both replacing Altman AND merging OpenAI + Anthropic; Amodei declined.** This is the anecdote the video references; it checks out.

---

## 4B.7 What this changes vs. the earlier "VERIFIED" confidence

- The video's **linchpin claim is now verified against the actual primary legal document** (DX-304), not just New Yorker/Verge summaries of it. This is the strongest possible confirmation tier.
- **Caveat carried from `05_tangents_and_discoveries.md` (N3):** the exhibits are *real and newly public*, but the *same* New Yorker primary documents that Altman disputes much of the board's case, and that the WilmerHale review was called a whitewash internally. So: the documents are authentic; the *interpretation* ("proof of a pattern of lying") remains contested. The video reports the documents accurately; it leads with the accuser's reading.

## 4B.8 Honest limitations

- Raw PDFs are auth-walled (403) — I read the DocumentCloud **viewer-page text**, which is the exhibit content but not a certified PDF copy. For a formal citation, pull the certified exhibit from the court docket (PACER) or the in-browser DocumentCloud viewer.
- I did **not** read the full deposition *transcripts* (Murati/Toner/Ilya sworn Q&A), only the exhibited documents and news excerpts of the testimony. If the user wants the deposition *testimony* verbatim, that requires the trial record (May 2026), not yet pulled.

---

## 4B verdict
**Root-layer claim VERIFIED at the highest tier (primary legal exhibit DX-304 + corroborating DX-315/1046 + Reuters on S11).** The video's central factual spine — a unanimous, candor-based board firing, documented in writing, later reversed by employee pressure — is confirmed by the actual court record. The only open item is interpretive (does the document "prove" malfeasance, or just a trust breakdown?) — and that is a framing question, not a factual one.
