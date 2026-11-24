# Harness pass 2: LLM-as-judge, Selective Context, HELM, Model Cards, Reproducibility report
def windows(text, kws, before=250, after=1400):
    out = []
    for kw in kws:
        i = text.find(kw)
        if i >= 0:
            out.append(f"--- [{kw}] ---\n" + text[max(0, i - before):i + after])
        else:
            out.append(f"--- [{kw}] NOT FOUND ---")
    return "\n\n".join(out)

# 1) Judging LLM-as-a-Judge (Zheng et al.)
goto_url("https://arxiv.org/html/2306.05685v3")
wait_for_load()
art = js("(()=>{const e=document.querySelector('article')||document.body;return e.innerText.slice(0,90000)})()")
print("===== LLM-AS-JUDGE (2306.05685) =====")
print(windows(art, ["position bias", "agreement", "verbosity", "self-enhancement", "human", "80%", "limited reasoning"]))
print("LEN", len(art))

# 2) Selective Context abstract
goto_url("https://arxiv.org/abs/2310.06201")
wait_for_load()
body = js("(()=>document.body.innerText.slice(0,20000))()")
print("===== SELECTIVE CONTEXT (2310.06201) =====")
print(windows(body, ["self-information", "compress", "Abstract", "improve"]))

# 3) HELM project page
goto_url("https://crfm.stanford.edu/helm/")
wait_for_load()
body2 = js("(()=>document.body.innerText.slice(0,30000))()")
print("===== HELM PAGE =====")
print(windows(body2, ["transparency", "living", "scenario", "metric", "reproducible"]))

# 4) Model Cards for Model Reporting
goto_url("https://arxiv.org/abs/1810.03993")
wait_for_load()
body3 = js("(()=>document.body.innerText.slice(0,20000))()")
print("===== MODEL CARDS (1810.03993) =====")
print(windows(body3, ["Abstract", "model card", "transparent", "performance"]))

# 5) Reproducibility report 2003.12206 (ar5iv) - 85% vs 4%
goto_url("https://ar5iv.labs.arxiv.org/html/2003.12206")
wait_for_load()
art2 = js("(()=>{const e=document.querySelector('.ltx_page_content')||document.body;return e.innerText.slice(0,120000)})()")
print("===== REPRO REPORT (2003.12206) =====")
print(windows(art2, ["85%", "checklist", "reproduction package", "code", "participants"]))
print("LEN", len(art2))
