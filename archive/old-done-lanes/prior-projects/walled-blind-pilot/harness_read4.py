import re, time

def grab(url, head=1800, keys=(), win=900, maxhits=1):
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
            s = max(0, i - 400); e = min(len(txt), i + win)
            print(">>>", txt[s:e].replace("\n", " ")[:win+400])

grab("https://arxiv.org/html/2508.13666v1",
     keys=["24.5", "formatting", "token", "readability"])

grab("https://arxiv.org/html/2505.00019v1",
     keys=["word omission", "long context", "moderate", "hallucinat", "Longbench"])

grab("https://arxiv.org/html/2306.05685",
     keys=["single-answer", "swap", "position", "mitigate", "longer"])

grab("https://www.lesswrong.com/posts/vBDupg8iPqgdwhFzz/demands-are-all-you-need-prompt-imperativeness-drastically",
     keys=["hedging", "imperativeness", "experiment", "result"])
