import re

file_path = r"d:\My Profiles\DataPlatform\scratch\pdf_analysis.txt"
content = open(file_path, "r", encoding="utf-8").read()

print(f"Total characters in analysis: {len(content)}")

# Let's search for mentions of "Level 3" or "L3" or "Quảng Ngãi" or "phân loại"
print("\n--- Mentions of Level 3 / L3 / Đơn vị thành viên ---")
matches = re.findall(r"(?:level\s*3|l3|phân loại đơn vị|đơn vị thành viên|mô hình hub|governance|quy chế|chi phí|quota|dung lượng).*?(?=\n---|\Z)", content, re.IGNORECASE | re.DOTALL)
print(f"Found {len(matches)} match snippets")
for m in matches[:15]:
    snippet = m[:300].replace('\n', ' ')
    print(f">> {snippet}\n")
