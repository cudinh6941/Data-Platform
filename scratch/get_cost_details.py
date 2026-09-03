import re

file_path = r"d:\My Profiles\DataPlatform\scratch\pdf_analysis.txt"
content = open(file_path, "r", encoding="utf-8").read()

# Search for specific terms about cost, budget, quota, spoke level in TCT proposals
matches = re.findall(r"--- Trang \d+.*?(?:kinh phí|ngân sách|chi phí|đầu tư|phân bổ|tài chính|giải pháp|mô hình hub-spoke|l3|quảng ngãi|chi nhánh|spoke).*?(?=\n--- Trang|\Z)", content, re.IGNORECASE | re.DOTALL)

with open(r"d:\My Profiles\DataPlatform\scratch\cost_and_spoke_details.txt", "w", encoding="utf-8") as f:
    f.write(f"Total matching pages: {len(matches)}\n\n")
    for m in matches:
        # Check if it has cost or spoke details
        if any(w in m.lower() for w in ["chi phí", "ngân sách", "đầu tư", "phân bổ", "quota", "dung lượng", "mô hình hub"]):
            f.write(m[:1200] + "\n" + "="*50 + "\n\n")

print("Saved cost and spoke details to scratch/cost_and_spoke_details.txt")
