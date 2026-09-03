import re

content = open(r"d:\My Profiles\DataPlatform\scratch\detailed_expansion_plan.txt", "r", encoding="utf-8").read()

sections = content.split("==================== MỤC ")

print(f"Total sections: {len(sections)}")

# Search for sections with "hub-spoke" or "chi phí" or "chủ quản"
with open(r"d:\My Profiles\DataPlatform\scratch\key_extracts_for_user.txt", "w", encoding="utf-8") as out:
    for s in sections[1:]:
        header_match = re.search(r"^(\d+).*?---\s*Trang\s*(\d+)", s, re.DOTALL)
        sec_num = header_match.group(1) if header_match else "?"
        page_num = header_match.group(2) if header_match else "?"
        
        # Check if text has important keywords
        keywords_matched = [w for w in ["hub-spoke", "phân loại", "quy chế", "chủ quản", "chi phí", "ngân sách", "lộ trình", "phương án", "bảo mật", "masking"] if w in s.lower()]
        if len(keywords_matched) >= 2:
            out.write(f"\n################### MỤC {sec_num} (Trang {page_num}) [Từ khóa: {', '.join(keywords_matched)}] ###################\n")
            out.write(s.strip()[:1400])
            out.write("\n")

print("Saved key extracts to scratch/key_extracts_for_user.txt")
