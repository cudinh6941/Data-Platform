import pypdf
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

tct_dir = r"d:\My Profiles\DataPlatform\TCT"

files = [
    "TCT-DP_Slide_Kick off_Final.pdf",
    "20260810_Slide_Hoi thao Data Platform_Phien Chieu.pdf",
    "20260810_Slide_Hoi thao Data Platform_Phien Sang.pdf",
    "TCT-DP_Bao cao de xuat ky thuat_Final - Data Flatform.pdf",
    "Slide Tóm tắt lựa chọn giải pháp Hybrid Data Platform PTSC.pdf"
]

keywords = ["tiến độ", "kế hoạch triển khai", "lộ trình", "18 tháng", "mốc", "milestone", "giai đoạn 1", "giai đoạn 2", "giai đoạn 2a"]

for f in files:
    path = os.path.join(tct_dir, f)
    if not os.path.exists(path):
        continue
    reader = pypdf.PdfReader(path)
    print(f"\n==================== {f} (Tổng: {len(reader.pages)} trang) ====================")
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ''
        # Check if any keyword matches
        matches = [kw for kw in keywords if kw in text.lower()]
        if matches:
            for line in text.split('\n'):
                line_lower = line.lower()
                if any(kw in line_lower for kw in ['tiến độ', 'kế hoạch', 'lộ trình', 'tuần', 'tháng', 'mốc', 'milestone', '2026', '2027']):
                    if len(line.strip()) > 3:
                        print(f"  [Trang {idx+1}] {line.strip()}")
