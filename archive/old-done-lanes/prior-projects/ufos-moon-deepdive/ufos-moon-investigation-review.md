# Investigation Review: "Giant UFOs near the Moon" — a verification, root-cause, and methodology record

**Document type:** Peer-reviewable investigative trail (not a journal paper)
**Compiled by:** Hermes Agent (cloud model) assisted by an offline reasoning model, under the `two-model-reasoning` workflow
**Citations:** Mechanically grounded to retrieved sources via a citation ledger. Every `[n]` maps to a URL in the Sources block; no citation was authored from memory.
**Status:** Verification complete. The primary claim is real as a *document*; its conclusions are not established by evidence.

---

## 0. Provenance — how this inquiry began

This investigation started from a **news-alert pop-up** delivered to the user, not from primary literature. The headline read:

> *"A trio of Ukrainian researchers has claimed to have detected more than 20 giant Unidentified Flying Objects (UFOs) moving at high speeds near the Moon."*

It was accompanied by a bullet summary asserting the study was titled **"UFO Dynamics on the Moon"**, authored by **Boris Zhilyaev, Vladimir Petukhov, and Sergey Pokhvala** of Ukraine's Main Astronomical Observatory, that the objects measured **15–25 miles (≈25–40 km)** across, that the Moon "serves as a base for UFOs," that craft could reach Earth in **20 minutes**, and that observations were made in **August–September 2025** in Vinarivka (Kyiv region).

The originating news items themselves are tabloid / wire aggregation, e.g. Irish Star[11], The News (Pakistan)[12], IBTimes UK[13], Daily Mail[14], Free Press Journal[15]. None of these is a primary source. The framing ("secret alien base," "fleet of UFOs") is the press's echo of the authors' own language in the preprint's abstract and conclusion.

The explicit task was: (1) verify what is actually true, (2) deep-dive the residual anomaly, and (3) produce a coherent, non-flattened path a peer could audit. This document is that path.

---

## 1. Verification layer — what is real vs. embellished

### 1.1 The paper is real
The study "UFO Dynamics on the Moon" by Zhilyaev, Petukhov, Pokhvala exists, is hosted on the Main Astronomical Observatory (NASU) forum as a PDF[1], is mirrored on ResearchGate[2], and carries a DOI 10.13140/RG.2.2.13866.79042. It reports high-speed video (20 fps, ZWO ASI294 Pro on an Intes-Alter M603 telescope) of the sky near the Moon during August–September 2025, claims "more than 20 objects," classifies them as "atmospheric" and "continental," and asserts disc-shaped objects of ~25–40 km and toroidal objects of ~36 km at ~11 km/s, concluding "the Moon serves as a base for UFOs."[1]

### 1.2 What is NOT established
- **It is not peer-reviewed.** It appears only on ResearchGate / Academia.edu / the MAO forum — not in a refereed journal.[2]
- **No space agency confirms it.** NASA, ESA, and mainstream observatories have issued no corroboration. Objects 25–40 km across orbiting the Moon would be visible to the Lunar Reconnaissance Orbiter and every lunar observer; the silence is itself evidence of non-confirmation.
- **The "20 minutes to Earth" figure is internally inconsistent** with the paper's own stated speed of 11 km/s (which implies ~9.7 hours for the lunar distance). It is asserted, not derived.[1]
- **The "25–40 km" size is not measured from the images.** The paper's own text describes its atmospheric "objects" as 2×2 pixels — i.e., unresolved, at the size of the telescope's point-spread function. At the Moon's distance a 2-pixel feature is ~3 km, not 25–40 km. The large size is *assigned* by an albedo/distance formula, not *seen*.

### 1.3 The authors have a prior, formally repudiated track record
The same group published "Unidentified Aerial Phenomena I & II" (2022, arXiv 2211.17085[3]) claiming "phantom" objects 3–12 m wide at up to 15 km/s over Kyiv. That work was reviewed by Ukraine's National Academy of Sciences, which concluded it was **"pseudo-scientific in form and content… full of inaccuracies, simplifications, fabrications and outright manipulations,"** and that the conclusions were "mostly absurd."[4] The academy's critique centered on the same distance-estimation method reused in the Moon paper.

Three independent expert responses to the 2022 work are on record:
- **Mick West (Skeptical Inquirer / Metabunk):** identified the "phantom" images as insects a few feet from the lens — uneven frame spacing, curved paths, RGB contrast matching a nearby bug — and showed the "special colorimetry" assumed a near-zero albedo that does not exist in nature.[4][6]
- **Avi Loeb (Harvard Galileo Project):** showed that at 15 km/s in the atmosphere the claimed objects would generate bow-shock fireballs of 150+ GW optical luminosity; if ~10× closer (≈1 km), sizes drop to 0.3–1.2 m and speeds to ~1.5 km/s — i.e., artillery shells or ordinary projectiles.[5]
- **NASU review panel:** the formal institutional repudiation cited above.[4]

---

## 2. Geometric audit (cloud-model computation, reproducible)

Using the hardware stated in the paper (Intes-Alter M603, focal length 1125 mm; ZWO ASI294 Pro, 4.63 µm pixels), the plate scale is:

```
plate_scale = 206.265 × 4.63 / 1125 = 0.849 arcsec/pixel
```

Angular sizes at the Moon (mean distance 384,400 km):

| Claimed object | Angular size at Moon | Pixels across (expected) |
|---|---|---|
| 25 km | 13.41 arcsec | ~15.8 px |
| 40 km | 21.46 arcsec | ~25.3 px |
| 36 km (toroid) | 19.32 arcsec | ~22.8 px |

But the paper states its atmospheric objects are **2×2 pixels** — unresolved. A 2-pixel feature at lunar distance is only **~3.16 km**, not 25–40 km. **The images cannot depict 25–40 km objects.** The size is a free parameter of a formula, not a measurement.

**Travel-time contradiction:** 384,400 km ÷ 20 min = 320 km/s required. The paper's own 11 km/s gives 384,400 / 11 / 3600 ≈ **9.7 hours**. The headline travel-time is unsupported by the paper's own numbers.

**Loeb-style fireball check (reproduced):** a 1.2 m object at 15 km/s in air radiates ~229 GW optically; a 10 m object ~16,000 GW. Such fireballs are not "dark phantoms." At ~1 km distance and ~1 m size the luminosity collapses to trivial levels — consistent with a near-field projectile, not a craft.

---

## 3. The deep-dive — distilling to the furthest root

Stripping the tabloid gloss ("alien base") and the lazy rebuttal ("just flies"), the friction survives at three layers:

**Layer 1 — The observers are genuinely competent.** Zhilyaev's group has a real publication record in stellar high-speed photometry and micro-variability (e.g., "What limits the precision of ground-based stellar photometry and positional measurements").[19] They know how to run a CMOS camera at 20 fps, do Fourier analysis, and calibrate frames. This is not a prank; it is a competent method applied to a geometry where its hidden assumptions silently break.

**Layer 2 — The reported signal sits in a legitimate gray zone.** Two mainstream facts bracket the claim: (a) **Atmospheric scintillation** (Osborn et al. 2015) is a dominant noise source in high-speed photometry of bright objects, producing ~0.01–0.1% fluctuations at up to ~10 Hz — exactly the "few-Hz flicker with harmonics" described.[18] (b) **Transient Lunar Phenomena** (Crotts 2009, *ApJ* 697:1) are a real, studied subject — short-lived brightness/colour changes on the Moon whose "existence as a coherent phenomenon is largely unsettled."[8][9] So "something flickering near/over the Moon at a few Hz" is not inherently absurd.

**Layer 3 — The fatal break is in the inference chain, not the raw measurement.** The leap from "I see a flickering point" → "25–40 km, lunar distance, 11 km/s" requires three unproven assumptions: (a) the object is not a near-field artifact; (b) the distance is the Moon (384,400 km); (c) the albedo assumption is valid. The size formula `r = R·√(β·Ω·(α_moon/α))` is driven entirely by assumed distance R and albedo α. Change R from 384,400 km to 1 metre and the "giant craft" becomes a bug.

### 3.1 The irreducible root
The critics have shown the objects **cannot be** what the authors claim (Loeb's fireball physics; West's insect identification; NASU's pseudo-science ruling). They have **not** shown what the objects **are**. None positively identified the signal; the authors **never released raw frames** (West requested them, received no reply)[4], and **never ran a control that localizes distance** — e.g., a synchronized second camera at a parallax baseline, or an aperture-cover near-field test.

> **The furthest root is not in nature — it is in non-disclosure.** The scientific question is currently *unanswerable from available evidence*. The friction is partly manufactured by the absence of the one dataset that would settle it.

---

## 4. Two-model reasoning methodology (the meta-layer)

A parallel objective was to develop and validate a workflow that lets a **local/offline reasoning model** (no web tools) do the token-heavy concept-deepening, while the **cloud model** handles fact-verification, caveat-injection, and review. This was saved as the `two-model-reasoning` skill.

### 4.1 The pattern
- **Cloud model = fact-verifier + caveat-injector + reviewer** (two short passes).
- **Offline model = reasoning engine** (the long chain).
- Compensate for the offline model's missing tools by **pre-searching for it**: the cloud model distills findings into a *Verified Facts* block plus a *Physics Envelope* (mechanisms the offline model is cleared to use).

### 4.2 Application to this case
The offline model was handed the verified facts (a signal exists: low-contrast ≤10% flicker at ~1–10 Hz, sometimes traversing a bright disk; distance unknown/unconstrained) and an envelope pre-loaded to prevent known drift: cosmic rays/hot pixels; atmospheric scintillation (modulates, does not create); rolling-shutter (distorts an existing moving signal, smears **along** the read axis, does not generate points); near-field objects (top real-world match); dual-camera parallax (only decisive distance test).

### 4.3 Iteration record
- **Round 1 (offline, unguided):** missed cosmic-ray artifacts; got rolling-shutter smear direction backwards (said "perpendicular"); hedged on the control instead of committing.
- **Round 2 (v3 prompt):** cloud injected two corrections (rolling-shutter ≠ source; near-field is the top match). Offline output then: ranked all four classes correctly (near-field #1, scintillation #2, cosmic ray #3, rolling-shutter #4/eliminated as source); correctly stated smear is *along* the scan axis; committed to dual-camera parallax; identified distance D as the debate-collapser; demoted EM-field checks to a useful *secondary* probe.
- **Residual nit:** §4 of the final offline pass flirted with "null-of-parallax ⇒ new physical interaction," a slight overreach — a null parallax more simply means "not a distant object" (i.e., mundane near-field/instrumental). Noted but not re-run, as it does not affect the core conclusion.

### 4.4 Why this is responsible
The offline model independently re-derived the two load-bearing findings: (a) the "extraordinary" conclusion is an **unconstrained prior, not a measurement** (Bayesian multimodality in distance); (b) **parallax is the only thing that settles it**. Its weaknesses (cosmic-ray omission, §4 waffle, abstract conclusion) were all fixable by tighter cloud-side pre-loading — i.e., the failure was in the *interface*, not the reasoning engine.

---

## 5. What a peer should be able to audit here

1. **Primary document:** the paper PDF[1] and its ResearchGate mirror[2].
2. **Prior work + institutional critique:** arXiv 2211.17085[3], Skeptical Inquirer[4], Loeb[5], Metabunk[6].
3. **Reproducible arithmetic:** plate-scale and size/travel-time calculations in §2 (inputs are the paper's own stated hardware).
4. **Legitimate-science anchors:** stellar photometry record[19], scintillation physics[18], TLP literature[8][9].
5. **Methodology:** the `two-model-reasoning` skill and the round-by-round offline outputs (available on request).

---

## 6. Limitations & honest statements

- The moon-paper PDF was read via extraction; figures are described from the extracted text, not independently re-rendered. Image-level re-analysis would require the authors' raw `.SER`/video frames, which were **not released**.
- All skepticism cited here (West, Loeb, NASU) addresses the *2022* Kyiv papers directly; the Moon paper reuses the same method and is critiqued by extension, not by a separate NASU ruling on the 2026 document.
- No claim in this document should be read as establishing that the anomalous signals are *definitively* insects, shells, or sensor artifacts. The honest finding is: **they are unlocalized; the extraordinary interpretation is unsupported; the mundane interpretation is unexcluded; and the raw data needed to decide is withheld.**

---

## 7. Bottom line

- **Real:** a self-published preprint by three Ukrainian astronomers claims giant objects near the Moon from backyard-class telescope video.
- **Not established:** any object is large, fast, extraterrestrial, Moon-based, or real at all. The paper's own numbers contradict its size and travel-time claims, and its distance method was formally ruled pseudo-scientific by the authors' own academy.
- **Most likely explanation:** near-field phenomena (insects, dust, debris, optical/sensor artifacts) misinterpreted through a broken distance/albedo calculation — the same error pattern from 2022.
- **Why it is viral:** the authors' own breathless framing is catnip for tabloids, which report the claims without the debunking context.

The single most important unknown that collapses the entire debate is **the distance to the features**, answerable only by a dual-camera parallax baseline — an experiment the authors had the means to run (they claimed a two-station setup in 2022) but did not honestly apply. Until raw frames are released or parallax is measured, the question is empirically open by omission, not by mystery.

---

## Appendix A — Related query: excluded source (audit trail)

**Date checked:** 2026-08-05 (session). **Reason for check:** user flagged an X/Twitter link as possibly relevant to the investigation.

- **Link:** https://x.com/david_tornai/status/2085004377916596244
- **Author:** @David_TornAI (David Marco), posted 2026-08-05T14:05:55Z; ~182 likes, 56 retweets.
- **Content:** A promotional thread for "NotebookLM + Google Antigravity" AI prompt templates (research-assistant, YouTube breakdown, content-repurposing, study-guide, business-idea, meeting-notes, knowledge-base, deep-learning prompts). Generic AI-product marketing; no reference to UFOs, the Moon, Zhilyaev/Petukhov/Pokhvala, or Ukraine.
- **Relevance determination:** **Not relevant.** No connection to the subject matter. Excluded from the source ledger and from the body of this document.
- **Why logged:** To preserve audit completeness — the link was checked at the user's initiative and consciously discarded, so the decision is on record rather than silently dropped. It is *not* cited as evidence and does *not* inform any conclusion in §1–§7.
- **Methodology note:** The link was retrieved via web extraction rather than assessed from its URL/handle alone, because social-media previews can imply a context the post does not deliver. This "fetch, don't assume" habit is part of the verification discipline documented in §4.

---

## Sources

[1] https://www.mao.kiev.ua/media/kunena/attachments/0/UFOdynamicsMoon.pdf
[2] https://www.researchgate.net/publication/403225173_UFO_Dynamics_on_the_Moon
[3] https://arxiv.org/abs/2211.17085
[4] https://skepticalinquirer.org/2022/12/ufos-over-kyiv/
[5] https://avi-loeb.medium.com/down-to-earth-limits-on-unidentified-aerial-phenomena-in-ukraine-6d8bb9f64f85
[6] https://www.metabunk.org/threads/ukrainian-uap-study-observation-of-events.12607/
[7] https://www.livescience.com/ukraine-uap-report-debunked
[8] https://iopscience.iop.org/article/10.1088/0004-637X/697/1/1
[9] https://www.popastro.com/lunar/transient-lunar-phenomena-tlp/
[10] https://www.yahoo.com/news/science/articles/ukrainian-scientists-claim-20-giant-153816973.html
[11] https://www.irishstar.com/news/world-news/scientists-warn-secret-alien-base-37516193
[12] https://www.thenews.com.pk/latest/1411296-more-than-20-giant-ufos-speed-across-the-moon-ukrainian-study-sparks-alien-debate
[13] https://www.ibtimes.co.uk/ukrainian-astronomers-ufo-evidence-moon-1812552
[14] https://www.dailymail.com/sciencetech/article-16028077/scientists-ukraine-ufo-fleet-moon.html
[15] https://www.freepressjournal.in/lifestyle/ufo-mystery-what-flew-across-the-moon-ukrainian-scientists-document-more-than-20-unidentified-aerial-objects
[16] https://nypost.com/2022/09/14/ukrainian-astronomers-claim-ufos-everywhere-over-kyiv/
[17] https://english.nv.ua/nation/ukrainian-astronomers-observe-bizarre-aerial-phenomena-over-kyiv-50269993.html
[18] https://arxiv.org/abs/1506.06921
[19] https://www.researchgate.net/publication/241280921_What_limits_the_precision_of_ground-based_stellar_photometry_and_positional_measurements
