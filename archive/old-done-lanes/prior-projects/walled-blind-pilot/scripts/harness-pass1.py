# Harness pass 1: NeurIPS checklist + Preregistration-for-AI-agents (2026) + compression empirical study
def windows(text, kws, before=250, after=1400):
    out = []
    for kw in kws:
        i = text.find(kw)
        if i >= 0:
            out.append(f"--- [{kw}] ---\n" + text[max(0, i - before):i + after])
        else:
            out.append(f"--- [{kw}] NOT FOUND ---")
    return "\n\n".join(out)

# 1) NeurIPS paper checklist guidelines
goto_url("https://neurips.cc/public/guides/PaperChecklist")
wait_for_load()
body = js("(()=>{const e=document.querySelector('main')||document.body;return e.innerText.slice(0,60000)})()")
print("===== NEURIPS CHECKLIST =====")
print(windows(body, ["error bars", "hyperparameters", "Limitations", "compute", "statistical", "code, data", "range of results", "number of runs", "broadly applicable"]))
print("LEN", len(body))

# 2) Preregistration for Experiments with AI Agents (2026)
goto_url("https://arxiv.org/html/2606.11217v1")
wait_for_load()
art = js("(()=>{const e=document.querySelector('article')||document.body;return e.innerText.slice(0,90000)})()")
print("===== PREREG AI AGENTS (2606.11217) =====")
print(windows(art, ["template", "model identifiers", "prompt text", "pilot", "confirmatory", "lock", "specification search", "generation parameters"]))
print("LEN", len(art))

# 3) Empirical study on prompt compression (2505.00019)
goto_url("https://arxiv.org/html/2505.00019v1")
wait_for_load()
art2 = js("(()=>{const e=document.querySelector('article')||document.body;return e.innerText.slice(0,90000)})()")
print("===== EMPIRICAL COMPRESSION STUDY (2505.00019) =====")
print(windows(art2, ["hallucination", "information loss", "long contexts", "compression ratio", "All methods", "MaHR", "short contexts"]))
print("LEN", len(art2))
