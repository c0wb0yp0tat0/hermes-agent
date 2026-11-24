import re, time, json

def grab(url, head=3000, keys=(), win=1800, maxhits=2, js_expr=None):
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
        if js_expr:
            res = js(js_expr)
            print("="*90)
            print("URL:", url)
            print("JS_EXTRACT:")
            print(str(res)[:6000])
            return
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

# FAQ: extract full answers for membership and canonization speed
grab("https://opusdei.org/en-us/faq/opus-dei/",
     js_expr="(()=>{const el=document.querySelector('#who-belongs-to-opus-dei'); return el?el.innerText:'NO_WHO_SECTION';})()")
grab("https://opusdei.org/en-us/faq/opus-dei/",
     js_expr="(()=>{const all=document.querySelectorAll('h2,h3'); const out=[]; all.forEach(h=>{if(/canonized|belongs|members/i.test(h.innerText)){let s=h.parentElement?h.parentElement.innerText:''; out.push(h.innerText+' :: '+s.slice(0,1200));}}); return out.join('\n---\n');})()")

grab("https://www.vatican.va/archive/ccc_css/archive/catechism/p2s1c1a1.htm",
     keys=["Opus Dei", "Work of God", "1174", "1175", "Hours", "office"])

grab("https://opusdei.org/en/article/prelature-of-opus-dei/",
     head=2500,
     keys=["28 November 1982", "Ut sit", "personal prelature", "canon 294"])

grab("https://www.nytimes.com/books/first/t/tapia-threshold.html",
     head=4000,
     keys=["report", "Opus Dei", "Tapia", "director", "provincial"])
