from pypdf import PdfReader

pdf_path = r"d:\My Profiles\DataPlatform\TCT\Slide Tóm tắt lựa chọn giải pháp Hybrid Data Platform PTSC.pdf"
reader = PdfReader(pdf_path)

with open(r"d:\My Profiles\DataPlatform\scratch\hybrid_summary_extract.txt", "w", encoding="utf-8") as f:
    f.write(f"Total pages: {len(reader.pages)}\n\n")
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        f.write(f"--- Trang {idx+1} ---\n")
        f.write(text[:1200] + "\n\n")

print("Done extracting hybrid summary PDF")
