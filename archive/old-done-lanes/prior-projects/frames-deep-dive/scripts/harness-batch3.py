import re, time

def grab(url, head=3000, keys=(), win=1800, maxhits=2):
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
    if not txt or len(txt) < 100:
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
            s = max(0, i - 400); e = min(len(txt), i + win)
            print(">>>", txt[s:e].replace("\n", " ")[:win+400])

grab("https://en.wikipedia.org/wiki/Depictions_of_the_Great_Seal_of_the_United_States",
     head=2500,
     keys=["Wallace", "Hunt", "1935", "FDR", "Roosevelt", "dollar", "reverse"])

grab("http://www.ewtn.com/library/CURIA/CBISUTSI.HTM",
     head=2500,
     keys=["personal prelature", "28 November 1982", "charism", "lay faithful", "clergy"])

grab("https://opusdei.org/en-us/faq/opus-dei/",
     head=2500,
     keys=["90", "countries", "members", "85", "000"])
