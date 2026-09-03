import os
import re

file_path = r"d:\My Profiles\DataPlatform\scratch\pdf_analysis.txt"
out_path = r"d:\My Profiles\DataPlatform\scratch\tct_findings_report.md"

content = open(file_path, "r", encoding="utf-8").read()

# Topics to extract
topics = {
    "Level & Phân loại Đơn vị (L1, L2, L3, L4, Hub-Spoke)": r"(?:level\s*[1-4]|l[1-4]\b|hub-spoke|spoke|quảng ngãi|đơn vị thành viên)",
    "Hạ tầng TCT đã xây dựng (MinIO, Fabric, Lakehouse, dHCI, Zones)": r"(?:minio|fabric|onelake|lakehouse|dhci|8 zone|vùng mạng|kiến trúc tổng thể)",
    "Quy chế quản lý & Chủ quyền dữ liệu (Governance, Data Owner, Quyền quyết định)": r"(?:quản trị dữ liệu|governance|data owner|chủ sở hữu|quy chế|chia sẻ dữ liệu|bảo mật dữ liệu|nghị định 13|masking|nhạy cảm)",
    "Chi phí & Phân bổ tài chính (Duy trì, License, Mở rộng, Ngân sách)": r"(?:chi phí|license|bản quyền|phí duy trì|phân bổ|ngân sách|đầu tư|tài chính|thuê ngoài)",
    "Dung lượng & Khả năng lưu trữ (Quota, Dung lượng, Storage)": r"(?:dung lượng|quota|storage|terabyte|tb|gb|mở rộng|lưu trữ)"
}

# Split analysis by pages
pages = re.split(r"(?=--- Trang \d+)", content)

results = {k: [] for k in topics}

for p in pages:
    for topic_name, pattern in topics.items():
        if re.search(pattern, p, re.IGNORECASE):
            # Extract header and first few lines
            lines = p.strip().splitlines()
            if lines:
                results[topic_name].append("\n".join(lines[:20]))

with open(out_path, "w", encoding="utf-8") as out:
    out.write("# BÁO CÁO PHÂN TÍCH TÀI LIỆU TỔNG CÔNG TY PTSC\n\n")
    for topic_name, matches in results.items():
        out.write(f"## {topic_name}\n")
        out.write(f"Tìm thấy {len(matches)} trang liên quan.\n\n")
        for idx, m in enumerate(matches[:8], 1): # Top 8 matches
            out.write(f"### Mục {idx}\n```\n{m}\n```\n\n")

print("Report written successfully to scratch/tct_findings_report.md")
