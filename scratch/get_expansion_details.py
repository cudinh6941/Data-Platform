import re

content = open(r"d:\My Profiles\DataPlatform\scratch\pdf_analysis.txt", "r", encoding="utf-8").read()

pages = re.split(r"(?=--- Trang \d+)", content)

interesting_pages = []
for p in pages:
    p_lower = p.lower()
    if any(term in p_lower for term in ["mô hình hub-spoke", "mở rộng", "chi phí", "ngân sách", "kinh phí", "lộ trình triển khai mở rộng", "đơn vị thành viên", "chủ sở hữu dữ liệu", "phương án kiến trúc"]):
        interesting_pages.append(p)

with open(r"d:\My Profiles\DataPlatform\scratch\detailed_expansion_plan.txt", "w", encoding="utf-8") as out:
    for idx, p in enumerate(interesting_pages):
        out.write(f"\n==================== MỤC {idx+1} ====================\n")
        out.write(p[:1500])
        out.write("\n")

print(f"Wrote {len(interesting_pages)} interesting pages to scratch/detailed_expansion_plan.txt")
