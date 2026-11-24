import re

def extract(url, selector, label, maxlen=3500):
    print(f"\n===== {label} :: {url} =====")
    try:
        goto_url(url)
        wait_for_load()
        txt = js(f"(()=>{{const el=document.querySelector({selector!r});return el?el.innerText:null}})()")
        if not txt:
            txt = js("document.body.innerText")
        if txt:
            txt = re.sub(r'\n{3,}', '\n\n', txt)
            print(txt[:maxlen])
        else:
            print("NO TEXT")
    except Exception as e:
        print("ERROR:", e)

extract("https://opusdei.org/en/article/the-da-vinci-code-the-catholic-church-and-opus-dei-2/",
        "div.article-body", "OPUSDEI.ORG: THE DA VINCI CODE, THE CATHOLIC CHURCH AND OPUS DEI")

extract("https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1041&context=etas",
        "body", "STILES 1783 (UNL PDF)")
