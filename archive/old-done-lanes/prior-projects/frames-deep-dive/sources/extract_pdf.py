import sys
try:
    import fitz
except ImportError:
    try:
        import pymupdf as fitz
    except ImportError:
        print("NO_FITZ"); sys.exit(1)
d = fitz.open(sys.argv[1])
print("PAGES:", d.page_count)
for i in range(d.page_count):
    t = d[i].get_text()
    if t.strip():
        print(f"===PAGE {i+1}===")
        print(t)
