import pypdf
r = pypdf.PdfReader('/root/.hermes/webui/attachments/6e6e05ded0cc/80_000_Hours_How_to_make_a_difference_with_your_career.pdf')
print('PAGES:', len(r.pages))
out=[]
for i,p in enumerate(r.pages):
    t=p.extract_text() or ''
    out.append(f'===== PAGE {i+1} =====\n'+t)
txt='\n'.join(out)
open('80k_career_guide.txt','w').write(txt)
print('CHARS:', len(txt))
