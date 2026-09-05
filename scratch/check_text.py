import pypdf
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('TCT/*.pdf'):
    reader = pypdf.PdfReader(f)
    print(f"\n==========================================")
    print(f"FILE: {f} - Pages: {len(reader.pages)}")
    has_text = 0
    for i, p in enumerate(reader.pages):
        t = p.extract_text() or ""
        if len(t.strip()) > 30:
            has_text += 1
    print(f"Pages with extractable text: {has_text} / {len(reader.pages)}")
