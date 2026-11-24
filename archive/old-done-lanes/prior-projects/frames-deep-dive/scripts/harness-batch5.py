import re, time

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
            print(str(res)[:8000])
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

# FAQ full answer extraction
grab("https://opusdei.org/en-us/faq/opus-dei/",
     js_expr="(()=>{const sec=document.getElementById('who-belongs-to-opus-dei'); if(!sec) return 'NO_SECTION'; let el=sec; let out=[]; for(let i=0;i<6 && el;i++){out.push('['+i+'] '+el.tagName+' class='+(el.className||'')); el=el.parentElement;} const t=sec.closest('section')||sec.parentElement; return out.join('\\n')+'\\nTEXT:\\n'+(t?t.innerText.slice(0,3000):'NO_TEXT');})()")

grab("https://opusdei.org/en-us/faq/opus-dei/",
     js_expr="(()=>{const t=document.body.innerText; const i=t.indexOf('How did Josemaria Escriva get canonized so quickly'); return i>=0?t.slice(i, i+1800):'NOT_FOUND';})()")

grab("https://www.usccb.org/prayer-and-worship/liturgy-of-the-hours",
     head=2500,
     keys=["Work of God", "Opus Dei", "Divine Office", "hours"])

grab("https://www.vatican.va/archive/ENG0015/_P51.HTM",
     head=3000,
     keys=["1174", "1175", "Opus Dei", "Work of God", "office"])

grab("http://news.bbc.co.uk/2/hi/europe/4249444.stm",
     head=3000,
     keys=["Da Vinci", "members", "mortification", "controversial", "million"])
