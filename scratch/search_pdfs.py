import os
import sys
from pypdf import PdfReader

tct_dir = r"d:\My Profiles\DataPlatform\TCT"
out_file = r"d:\My Profiles\DataPlatform\scratch\pdf_analysis.txt"

files = [f for f in os.listdir(tct_dir) if f.endswith(".pdf")]

keywords = [
    "quảng ngãi", "l3", "spoke", "level 3", "level", "workspace", "dung lượng", "quota", 
    "chi phí", "phí duy trì", "vận hành", "quy chế", "quản trị dữ liệu", "governance",
    "bảo mật", "zone", "phân quyền", "quyết định", "nhạy cảm", "masking",
    "minio", "fabric", "onelake", "hybrid", "đơn vị thành viên", "dự toán", "hạ tầng"
]

with open(out_file, "w", encoding="utf-8") as out:
    out.write("=== PHÂN TÍCH TOÀN DIỆN CÁC FILE PDF TỔNG CÔNG TY ===\n\n")
    
    for f in files:
        path = os.path.join(tct_dir, f)
        out.write(f"\n=======================================================\n")
        out.write(f"FILE: {f}\n")
        out.write(f"=======================================================\n")
        try:
            reader = PdfReader(path)
            out.write(f"Tổng số trang: {len(reader.pages)}\n\n")
            
            for idx, page in enumerate(reader.pages):
                page_num = idx + 1
                text = page.extract_text() or ""
                text_lower = text.lower()
                
                # Check match
                matched_kws = [kw for kw in keywords if kw in text_lower]
                if matched_kws:
                    out.write(f"--- Trang {page_num} [Từ khóa: {', '.join(matched_kws)}] ---\n")
                    # Clean up text lines
                    lines = [line.strip() for line in text.splitlines() if line.strip()]
                    out.write("\n".join(lines[:35])) # First 35 lines of matching page
                    out.write("\n\n")
        except Exception as e:
            out.write(f"Lỗi khi đọc file {f}: {e}\n")

print("Done! Check scratch/pdf_analysis.txt")
