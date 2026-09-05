import pypdf
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

def search_terms_in_file(filepath, terms):
    reader = pypdf.PdfReader(filepath)
    results = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        matched = [t for t in terms if t.lower() in text.lower()]
        if matched:
            results.append((i + 1, matched, text))
    return results

files = glob.glob('TCT/*.pdf')

print("--- 1. TÌM KIẾM 'KICK OFF' ---")
kickoff_res = search_terms_in_file('TCT/TCT-DP_Slide_Kick off_Final.pdf', ['phân công', 'vai trò', 'trách nhiệm', 'đơn vị', 'tiến độ', 'kế hoạch', 'master data', 'danh mục', 'l3', 'level'])
for p, terms, text in kickoff_res:
    print(f"\n[Kick off - Page {p}] Matched: {terms}")
    print(text[:800])

print("\n--- 2. TÌM KIẾM 'MASTER DATA' & '29' TRONG TẤT CẢ FILE ---")
for f in files:
    res = search_terms_in_file(f, ['29 danh mục', 'danh mục dữ liệu', 'master data management', 'mdm', 'danh mục'])
    if res:
        print(f"\nFile: {f} ({len(res)} pages matched)")
        for p, terms, text in res:
            # check if 29 is in text
            if '29' in text or 'danh mục' in text.lower():
                print(f"  Page {p} (Terms: {terms}):")
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                for l in lines[:10]:
                    print("    ", l[:120])
