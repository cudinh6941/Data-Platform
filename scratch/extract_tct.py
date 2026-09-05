import pypdf
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('TCT/*.pdf')
print('Found files:', files)

for f in files:
    try:
        reader = pypdf.PdfReader(f)
        num_pages = len(reader.pages)
        print(f"\n==========================================")
        print(f"FILE: {f} ({num_pages} pages)")
        print(f"==========================================")
        
        matches = []
        for i, page in enumerate(reader.pages):
            txt = page.extract_text() or ''
            found_kws = []
            for kw in ['Master Data', '29', 'Level 3', 'L3', 'Trách nhiệm', 'RACI', 'Quảng Ngãi', 'ĐVTV', 'Hub', 'Spoke']:
                if kw.lower() in txt.lower():
                    found_kws.append(kw)
            if found_kws:
                matches.append((i+1, found_kws, txt))
        
        print(f"Total matching pages: {len(matches)}")
        for page_num, kws, txt in matches[:10]: # sample first 10
            print(f"\n--- Page {page_num}: Keywords {kws} ---")
            lines = [line.strip() for line in txt.split('\n') if line.strip()]
            for line in lines[:15]:
                print("  ", line[:100])
    except Exception as e:
        print(f"Error reading {f}: {e}")
