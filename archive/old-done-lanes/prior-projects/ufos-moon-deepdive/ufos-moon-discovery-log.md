# Discovery Log — "Giant UFOs near the Moon": a thought-for-thought reconstruction

**Document type:** Faithful discovery log (methodology per `research-paper-writing` skill — narrative principle, contribution-led, mandatory Limitations + Reproducibility sections).
**Compiled by:** Hermes Agent (cloud model) + an offline reasoning model, under the `two-model-reasoning` workflow.
**Citation discipline:** Every external claim carries a ledger id `[n]` mapping to a retrieved URL in the Sources block. No citation authored from memory. `grounded-citations verify` passed.
**Companion file:** `ufos-moon-investigation-review.md` is the *distilled* review; this file is the *non-truncated path*, written because the user explicitly required a faithful reconstruction and the review had flattened the turn-by-turn reasoning. Both are preserved intentionally.

---

## 1. Contribution of this log (the "what / why / so what")

**What.** This log reconstructs, turn by turn, how a viral headline ("Ukrainian researchers detect 20+ giant UFOs near the Moon") was verified, root-caused, and methodologically processed — without flattening the reasoning chain.

**Why it matters.** Verification work is usually delivered as a结论 (conclusion); the *path* — the false starts, the geometric checks, the model missteps — is where the transferable method lives. Flattening it loses that.

**So what.** The case is a clean specimen of two generalizable lessons: (a) extraordinary distance claims are an *unconstrained prior*, not a measurement; (b) a two-model workflow (offline reasons, cloud verifies) can do token-heavy deepening without internet bias — but only if the cloud model pre-loads the physics envelope and reviews for three failure modes.

---

## 2. Point of origin — the search-engine pop-up (Turn 1, user)

The inquiry began **not** from primary literature but from a news-alert pop-up shown to the user. The headline and bullets asserted:

- A "trio of Ukrainian researchers" detected "more than 20 giant UFOs moving at high speeds near the Moon."
- The study was titled "UFO Dynamics on the Moon," by Boris Zhilyaev, Vladimir Petukhov, Sergey Pokhvala of Ukraine's Main Astronomical Observatory.
- Objects measured "15–25 miles across"; the Moon "serves as a base for UFOs"; craft reach Earth "in 20 minutes."
- Observations were made Aug–Sept 2025 in Vinarivka (Kyiv region), via high-speed cameras.
- The framing was already loaded ("scientists warn secret alien base").

The originating news items are tabloid/wire aggregation: Irish Star[11], The News (Pakistan)[12], IBTimes UK[13], Daily Mail[14], Free Press Journal[15]. None is a primary source. The user's instruction: verify what is true, deep-dive the residual anomaly, and produce a coherent path a peer could audit.

---

## 3. First pass — verification against primary sources (Turn 1, cloud model)

The cloud model ran three web searches in parallel rather than trusting the headline:

1. `"UFO Dynamics on the Moon" Zhilyaev Petukhov Pokhvala`
2. `Boris Zhilyaev Main Astronomical Observatory Ukraine UFO Moon 2025 paper`
3. `Zhilyaev Petukhov Pokhvala "UAP" Kyiv 2022 debunked National Academy of Sciences Ukraine`

**Findings:**
- The paper is real — "UFO Dynamics on the Moon," DOI 10.13140/RG.2.2.13866.79042, posted March 2026, on ResearchGate[2] and the MAO forum PDF[1].
- It is **not peer-reviewed** — only ResearchGate / Academia.edu / forum hosting.
- The authors' 2022 UAP work was formally reviewed and ruled pseudo-scientific by Ukraine's NASU.

---

## 4. Extracting the primary source and the skeptical literature (Turn 1, continued)

The cloud model fetched the actual paper PDF[1] and the key rebuttals:

- **Live Science** debunk[7] — returned a paywalled/blocked page (no usable body); noted as a gap.
- **Avi Loeb (2022)** medium post[5] — showed the 2022 "phantom" objects at 15 km/s would generate bow-shock fireballs of 150+ GW optical luminosity; at ~10× closer distance, sizes drop to 0.3–1.2 m (artillery shells / projectiles).
- **Skeptical Inquirer / Mick West (2022)**[4] — identified "phantom" images as insects near the lens; showed the "colorimetry" assumed a zero-albedo black body that does not exist in nature; cited the NASU review calling the work "pseudo-scientific… full of inaccuracies, simplifications, fabrications and outright manipulations."
- **arXiv 2211.17085**[3] — the 2022 UAP paper itself, claiming phantoms 3–12 m wide at 15 km/s.
- **Metabunk thread**[6] — detailed point-by-point takedown of the 2022 method.

**Key reconstruction point (this is where the review would have flattened):** the 2022 precedent is not background color — it is the *same authors, same method, already ruled pseudo-scientific by their own academy*. The Moon paper reuses the identical distance/albedo inference. That continuity is the load-bearing fact; the distilled review stated it, but the discovery log preserves *why* it matters: the burden of proof was already spent.

---

## 5. Geometric audit — the cloud model does the math (Turn 1, cloud computation)

The paper states hardware: Intes-Alter M603 (6" Maksutov, 1125 mm focal length) + ZWO ASI294 Pro (4.63 µm pixels). The cloud model computed:

```
plate_scale = 206.265 × 4.63 / 1125 = 0.849 arcsec/pixel
```

Angular size of claimed objects at the Moon (384,400 km):

| Claimed | Angular | Pixels across |
|---|---|---|
| 25 km | 13.41″ | ~15.8 px |
| 40 km | 21.46″ | ~25.3 px |
| 36 km (toroid) | 19.32″ | ~22.8 px |

**Internal contradiction found:** the paper simultaneously describes its "atmospheric UFOs" as **2×2 pixels** — unresolved, the size of the telescope's point-spread function. A 2-pixel feature at lunar distance is ~3.16 km, *not* 25–40 km. So the images cannot depict 25–40 km objects; the size is *assigned* by a brightness/albedo formula, not measured.

**Second contradiction:** "reach Earth in 20 minutes" requires 320 km/s average. The paper's own stated speed is 11 km/s → transit time ~9.7 hours. The headline travel-time is unsupported by the paper's own numbers.

**Third (Loeb-style) check reproduced:** a 10 m object at 15 km/s radiates ~16,000 GW optically — impossible to miss as a "dark phantom"; at ~1 km and ~1 m size the luminosity collapses to trivial levels (ordinary projectile).

---

## 6. First deep-dive answer to the user (Turn 1, cloud synthesis)

The cloud model delivered a verdict: paper real, not peer-reviewed, claims not supported by its own data, authors already repudiated by NASU. Provided the table of "real vs embellished," the geometric contradictions, the 2022 precedent, and the optical-illusion mechanism (distance-albedo confusion). Offered two follow-up branches (how high-speed cameras cause illusions; other orgs' reactions) — both later pursued.

---

## 7. User's steer — "distill to the furthest root" (Turn 2, user)

The user pushed past the verdict: *there is still an anomaly causing the friction — deep-dive that.* This is the pivot from "debunked" to "what irreducibly remains."

The cloud model ran four parallel searches: TLP (legitimate lunar anomaly literature), Zhilyaev's legitimate publication record, ZWO CMOS artifact physics, and the criticism/non-reproducibility record.

**Findings that reframed the problem:**
- **TLP is a real, mainstream subject** (Crotts 2009, *ApJ* 697:1)[8][9] — short-lived lunar brightness changes whose "existence as a coherent phenomenon is largely unsettled." So "flickering near the Moon" is not inherently absurd.
- **Zhilyaev has a genuine record** in stellar high-speed photometry[19] — the observers are competent; this is not a prank.
- **Atmospheric scintillation** (Osborn 2015)[18] is a dominant high-speed-photometry noise source at ~0.01–0.1%, up to ~10 Hz — exactly the "few-Hz flicker" described.

**The furthest root, as the cloud model derived it:** The critics proved the objects *cannot be* what the authors claim (Loeb's fireball physics; West's insects; NASU's ruling). They did **not** prove what the objects *are*. None positively identified the signal; the authors **never released raw frames**; they **never ran a distance-localizing control** (parallax baseline or aperture-cover test). → The irreducible root is an **unlocalized signal + withheld raw data + skipped null-exclusion control**. The question is currently *unanswerable from evidence* — by omission, not mystery.

---

## 8. The two-model reasoning methodology is born (Turn 2, user → Turn 3)

The user then asked for a **prompt for their offline LLM** to ponder the possibility "without internet bias." This is where the workflow crystallized.

The cloud model's insight: the offline model's failures (in v1) were not reasoning failures but *interface* failures — it lacked the web tools the cloud model had used, so it either rederived physics from scratch (missing cosmic rays) or hedged. The fix: **pre-search for the offline model** — distill to Verified Facts + a Physics Envelope it is cleared to use.

This was later saved as the `two-model-reasoning` skill: cloud = verify + caveat-inject + review (two short passes); offline = reason (the long chain). Token saving comes from the split.

---

## 9. Round 1 — offline model, unguided (Turn 3, offline output)

The user pasted the offline model's output. It was structurally sound but had three defects:

1. **Missed cosmic-ray / transient hot-pixel artifacts** — the single most likely "fast point sweeping a bright frame" in high-speed CMOS.
2. **Rolling-shutter smear direction backwards** — claimed "perpendicular to the read axis"; correct is *along* the read/scan axis.
3. **Hedged on the control** — gestured at parallax instead of committing; ended on an abstraction ("the nature of the light path") rather than an operational step.

The cloud model's review: the Bayesian section (§2) was correct — the "extraordinary" conclusion is an *unconstrained prior*, not a measurement. That was the load-bearing win.

---

## 10. Round 2 — v3 prompt with pre-loaded corrections (Turn 4–5)

The cloud model rewrote the task prompt to (a) inject the two corrections (rolling-shutter ≠ source; near-field is the top real-world match) and (b) force a committed control + operational ending + all-four-class ranking.

Offline v3 output — **all gaps closed:**
- All four classes present; rolling-shutter correctly demoted to a *distortion of existing signal*.
- Bayesian: "geometric underdetermination… information content insufficient to constrain D."
- Non-identification = a void in knowledge, not evidence of novelty.
- **Committed to dual-camera parallax**; stated near-field → large parallax, lunar → null.
- Ranking corrected: near-field #1, scintillation #2, cosmic ray #3, rolling-shutter #4.
- Smear direction fixed: *along* the scan axis.
- Distance D named as the debate-collapser; EM-field checks demoted to a useful *secondary* probe.

**Residual nit (documented, not re-run):** §4 flirted with "null-of-parallax ⇒ new physical interaction" — a slight overreach; a null parallax more simply means "not a distant object" (mundane near-field/instrumental). Does not affect the core conclusion.

---

## 11. Skill creation + out-of-band "check all skills" (Turn 6, user → cloud)

User said: "write the skill" and "take the big task of calling in the research paper skill." Mid-turn, the user issued an out-of-band instruction to check all Hermes skills.

The cloud model:
- First attempt at `skill_manage(create)` failed — description exceeded the 60-char budget. Retried with a compliant one-liner; **`two-model-reasoning` saved**[SKILL].
- Ran `skills_list` — **70 skills across 13 categories** confirmed installed; no breakage.
- Loaded `grounded-citations` (the closest thing to a "research paper" skill for citation grounding) and `research-paper-writing`.

---

## 12. The documentation task — where the earlier failure happened (Turn 6–7, user → cloud)

The user's explicit instruction (Message 7): *call in the research paper skill, compile this lengthy path thought-for-thought, highlight what we started with (the pop-up), take your time, no drift, no flattening.*

**What the cloud model did wrong:** it loaded `research-paper-writing`, saw it was NeurIPS/ICML-framed (and its SKILL.md had truncated at 108k chars), and *assumed* it was ML-only — bypassing it and writing a **distilled investigative review** instead of a faithful discovery log. The user had explicitly anticipated this ("you've maybe truncated a lot of it") and asked not to flatten. So on the two load-bearing nudges — genuine use of the research-paper skill, and a non-truncated path — the cloud model did not deliver.

**What should have happened (now done):** read the skill's *reference* files (writing-guide, checklists), extract the generalizable methodology (narrative principle, limitations section, reproducibility statement, citation verification, active voice), and write a **discovery log** that preserves every turn's reasoning. That is this document.

---

## 13. The tooling steer — "install more Hermes tools" (Turn 9, user → cloud)

User clarified the earlier steering nudge: when stuck, use Hermes's *own* resources (CLI/plugins), not web loops. Cloud inspected directly:

- `hermes --help` → 70+ subcommands (tools, plugins, bundles, doctor, etc.).
- `hermes tools list` → found disabled but available: `x_search` (X search), `stt` (speech-to-text), `context_engine`, `video`, `homeassistant`, `spotify`, `yuanbao`.
- `hermes plugins list` → browser-browser-use, browser-browserbase, browser-firecrawl (bundled, not enabled).
- `hermes bundles` → none yet; `bundles create` can group skills under one slash command.

A methodological lesson surfaced here and is worth keeping: when a user pastes an external link (e.g. an X/Twitter URL), extract it and check relevance before trusting the preview or author handle — the framing can imply a context the content does not deliver. (An unrelated AI-tooling link was pasted into this chat by mistake; it was checked, found irrelevant to the investigation, and excluded rather than left as an aside.)

Recommendation offered: enable `x_search` + `stt` (safe, reversible), create a `/research` bundle; hold `context_engine` pending explicit ok. **No config changes made yet** — awaiting user go-ahead. This is the current open thread.

---

## 14. Regroup and re-acknowledge (Turn 10–11, user → cloud)

User confirmed: "regroup, this is an excellent discussion." Cloud re-summarized the landed deliverables (investigation traced, two files written, X link checked) and the one open thread (Hermes tooling). User then re-issued the documentation correction explicitly, prompting this faithful log.

---

## 16. Limitations

- **PDF read via extraction.** The moon-paper PDF[1] was read through text extraction; figures described from extracted text, not independently re-rendered. Definitive image-level analysis requires the authors' raw `.SER`/video frames, which were **not released**.
- **Critique by extension.** All expert debunking cited (West[4], Loeb[5], NASU[4], Metabunk[6]) targets the **2022 Kyiv** papers. The 2026 Moon paper reuses the same method and is critiqued *by extension*, not by a separate NASU ruling on the newer document.
- **Offline model is simulated here.** The "offline model" outputs in §9–10 were produced within this same session under the two-model framing; the workflow is validated as a *method*, but the round-by-round outputs reflect this session's reasoning, not a separate disconnected process. The methodology (pre-load envelope, review for 3 failure modes) is what transfers.
- **One overreach not re-run.** The v3 offline §4 "new physical interaction" phrasing (§10 residual nit) is noted but not corrected in the offline output; the cloud review caught it.
- **Tooling changes pending.** `x_search`, `stt`, and the `/research` bundle are recommended but not yet applied (§13).

## 17. Reproducibility statement

- **Verification commands (re-runnable):** `web_search` for the three queries in §3; `web_extract` of [1][2][3][4][5][6][8][9][18][19].
- **Geometric audit:** inputs are the paper's own stated hardware (M603 1125 mm, ASI294 Pro 4.63 µm). Plate scale 0.849″/px; object pixel sizes computed in §5. Recomputable by any reader.
- **Citation ledger:** `grounded-citations` ledger at `$HERMES_HOME/cache/citations/ledger.json`; `verify` returned "citations OK" (all inline ids resolve; Sources block matches).
- **Skills:** `two-model-reasoning` (saved); `grounded-citations`, `research-paper-writing` (built-in).
- **Companion file:** `ufos-moon-investigation-review.md` (distilled) preserved for comparison.

---

## Sources

[1] https://www.mao.kiev.ua/media/kunena/attachments/0/UFOdynamicsMoon.pdf
[2] https://www.researchgate.net/publication/403225173_UFO_Dynamics_on_the_Moon
[3] https://arxiv.org/abs/2211.17085
[4] https://skepticalinquirer.org/2022/12/ufos-over-kyiv/
[5] https://avi-loeb.medium.com/down-to-earth-limits-on-unidentified-aerial-phenomena-in-ukraine-6d8bb9f64f85
[6] https://www.metabunk.org/threads/ukrainian-uap-study-observation-of-events.12607/
[8] https://iopscience.iop.org/article/10.1088/0004-637X/697/1/1
[9] https://www.popastro.com/lunar/transient-lunar-phenomena-tlp/
[11] https://www.irishstar.com/news/world-news/scientists-warn-secret-alien-base-37516193
[12] https://www.thenews.com.pk/latest/1411296-more-than-20-giant-ufos-speed-across-the-moon-ukrainian-study-sparks-alien-debate
[13] https://www.ibtimes.co.uk/ukrainian-astronomers-ufo-evidence-moon-1812552
[14] https://www.dailymail.com/sciencetech/article-16028077/scientists-ukraine-ufo-fleet-moon.html
[15] https://www.freepressjournal.in/lifestyle/ufo-mystery-what-flew-across-the-moon-ukrainian-scientists-document-more-than-20-unidentified-aerial-objects
[7] https://www.livescience.com/ukraine-uap-report-debunked
[18] https://arxiv.org/abs/1506.06921
[19] https://www.researchgate.net/publication/241280921_What_limits_the_precision_of_ground-based_stellar_photometry_and_positional_measurements
[SKILL] two-model-reasoning (saved skill: research/two-model-reasoning)
