import re, time

def grab(url, head=1500, keys=(), win=900, maxhits=1):
    for attempt in (1, 2):
        try:
            goto_url(url)
            wait_for_load()
            break
        except Exception as e:
            print("NAV_ERROR", url, "attempt", attempt, repr(e)[:150])
            time.sleep(2)
    else:
        print("NAV_FAILED", url)
        return
    try:
        txt = js("document.body.innerText")
    except Exception as e:
        print("JS_ERROR", url, repr(e)[:150])
        return
    if not txt or len(txt) < 200:
        print("EMPTY_OR_SHORT", url, "len=", len(txt) if txt else 0)
        return
    print("="*90)
    print("URL:", url)
    print("TITLE:", js("document.title"))
    print("LEN:", len(txt))
    print("---HEAD---")
    print(txt[:head].replace("\n", " "))
    low = txt.lower()
    for k in keys:
        hits = [m.start() for m in re.finditer(re.escape(k.lower()), low)]
        print(f"---KEY '{k}' hits={len(hits)}---")
        for i in hits[:maxhits]:
            s = max(0, i - 350); e = min(len(txt), i + win)
            print(">>>", txt[s:e].replace("\n", " ")[:win+350])

grab("https://arxiv.org/html/2306.05685",
     keys=["position bias", "verbosity", "self-enhancement", "agreement"])

grab("https://arxiv.org/html/2310.05736v2",
     keys=["compression ratio", "GSM8K", "drop", "performance"])

grab("https://arxiv.org/html/2403.12968",
     keys=["compression ratio", "performance", "faithful", "degrad"])

grab("https://arxiv.org/html/2407.15504v1",
     keys=["distortion", "query-aware", "gap", "LLMLingua"])

grab("https://arxiv.org/html/2506.22316v3",
     keys=["score", "bias", "tendency", "lenien", "5"])

grab("https://arxiv.org/html/2307.03172v2",
     keys=["middle", "position", "accuracy", "context"])
