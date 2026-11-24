import re, time

def grab(url, head=2500, keys=(), win=1600, maxhits=2):
    for attempt in (1, 2):
        try:
            goto_url(url)
            wait_for_load()
            break
        except Exception as e:
            print("NAV_ERROR", url, "attempt", attempt, repr(e)[:200])
            time.sleep(2)
    else:
        print("NAV_FAILED", url)
        return
    try:
        txt = js("document.body.innerText")
    except Exception as e:
        print("JS_ERROR", url, repr(e)[:200])
        return
    if not txt or len(txt) < 200:
        print("EMPTY_OR_SHORT", url, "len=", len(txt) if txt else 0)
        return
    print("="*90)
    print("URL:", url)
    print("TITLE:", js("document.title"))
    print("LEN:", len(txt))
    print("---HEAD---")
    print(txt[:head].replace("\n", " ")[:head])
    low = txt.lower()
    for k in keys:
        hits = [m.start() for m in re.finditer(re.escape(k.lower()), low)]
        print(f"---KEY '{k}' hits={len(hits)}---")
        for i in hits[:maxhits]:
            s = max(0, i - 500); e = min(len(txt), i + win)
            print(">>>", txt[s:e].replace("\n", " ")[:win+500])

grab("https://arxiv.org/html/2604.02985v1",
     head=3000,
     keys=["structured", "rate adherence", "quality loss", "conclusion", "synthetic"])

grab("https://arxiv.org/html/2604.13066v1",
     head=3000,
     keys=["lossless", "compression ratio", "repetitive", "savings", "token"])

grab("https://arxiv.org/html/2508.19282v3",
     head=3000,
     keys=["lossless", "compression ratio", "retrieval", "performance", "RAG"])
