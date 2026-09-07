import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# =========================================================================
# BÁO CÁO DATA PLATFORM PTSC QUẢNG NGÃI - VERSION 8 (CẬP NHẬT KIẾN TRÚC CHI TIẾT)
# Cập nhật theo đúng file: kien_truc_data_platform_chi_tiet.md
# =========================================================================

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BL = prs.slide_layouts[6]

# BẢNG MÀU CHUYÊN NGHIỆP PTSC
NAVY = RGBColor(0, 40, 85)          # #002855 - Brand Chính
BLUE = RGBColor(0, 80, 157)         # #00509D - Primary
TEAL = RGBColor(0, 128, 128)        # #008080 - Accent Tech
GRAY_DARK = RGBColor(40, 50, 60)    # #28323C - Text chính
GRAY_MED = RGBColor(140, 150, 160)  # #8C96A0 - Border
GRAY_LIGHT = RGBColor(245, 247, 250)# #F5F7FA - Background Card
WHITE = RGBColor(255, 255, 255)
BLACK = RGBColor(30, 30, 30)

BLUE_SOFT = RGBColor(230, 240, 250)
GREEN = RGBColor(20, 120, 60)
GREEN_SOFT = RGBColor(230, 245, 235)
RED = RGBColor(180, 40, 40)
RED_SOFT = RGBColor(253, 238, 238)
GOLD = RGBColor(180, 110, 0)
GOLD_SOFT = RGBColor(254, 246, 230)
PURPLE = RGBColor(126, 34, 206)
PURPLE_SOFT = RGBColor(250, 245, 255)

def shape(s, l, t, w, h, bg=None, line=None, line_w=Pt(1), rounded=False):
    st = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    sp = s.shapes.add_shape(st, l, t, w, h)
    if bg:
        sp.fill.solid(); sp.fill.fore_color.rgb = bg
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = line; sp.line.width = line_w
    else:
        sp.line.fill.background()
    return sp

def text(s, l, t, w, h, txt, sz=11, bold=False, color=GRAY_DARK, align=PP_ALIGN.LEFT):
    bx = s.shapes.add_textbox(l, t, w, h)
    tf = bx.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0.04)
    p = tf.paragraphs[0]; p.text = txt
    p.font.size = Pt(sz); p.font.bold = bold; p.font.color.rgb = color
    p.alignment = align
    return bx

def header(s, title, category="PTSC QUẢNG NGÃI — BÁO CÁO NỀN TẢNG DỮ LIỆU", num=""):
    shape(s, Inches(0), Inches(0), Inches(13.333), Inches(1.15), NAVY)
    shape(s, Inches(0), Inches(1.15), Inches(13.333), Inches(0.04), BLUE)
    shape(s, Inches(0.8), Inches(0.15), Inches(0.08), Inches(0.85), GOLD)
    text(s, Inches(1.05), Inches(0.16), Inches(10.5), Inches(0.26), category.upper(), 9.5, True, RGBColor(180, 210, 245))
    text(s, Inches(1.05), Inches(0.42), Inches(10.5), Inches(0.65), title, 16.5, True, WHITE)
    if num:
        shape(s, Inches(12.0), Inches(0.22), Inches(0.7), Inches(0.65), line=RGBColor(60, 100, 150), rounded=True)
        text(s, Inches(12.0), Inches(0.32), Inches(0.7), Inches(0.4), num, 13, True, GOLD, PP_ALIGN.CENTER)

def note(s, txt):
    n = s.notes_slide.notes_text_frame
    n.text = (n.text + "\n" + txt).strip()

def arrow_shape(s, l, t, direction="right", w=Inches(0.4), h=Inches(0.3)):
    st = MSO_SHAPE.RIGHT_ARROW if direction == "right" else MSO_SHAPE.DOWN_ARROW
    sp = s.shapes.add_shape(st, l, t, w, h)
    sp.fill.solid(); sp.fill.fore_color.rgb = BLUE
    sp.line.fill.background()
    return sp

def numbered_label(s, l, t, num, col=BLUE, sz=Inches(0.35)):
    sp = s.shapes.add_shape(MSO_SHAPE.OVAL, l, t, sz, sz)
    sp.fill.solid(); sp.fill.fore_color.rgb = col
    sp.line.fill.background()
    text(s, l, t + Inches(0.02), sz, sz, str(num), 11, True, WHITE, PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 1: COVER
# =========================================================================
s1 = prs.slides.add_slide(BL)
shape(s1, Inches(0), Inches(0), Inches(13.333), Inches(7.5), NAVY)
shape(s1, Inches(0), Inches(0), Inches(13.333), Inches(0.1), GOLD)
shape(s1, Inches(0), Inches(7.35), Inches(13.333), Inches(0.15), BLUE)
shape(s1, Inches(1.0), Inches(1.8), Inches(0.12), Inches(3.2), GOLD)

text(s1, Inches(1.3), Inches(1.8), Inches(11.0), Inches(0.4),
     "TỔNG CÔNG TY CỔ PHẦN DỊCH VỤ DẦU KHÍ VIỆT NAM — CÔNG TY CỔ PHẦN DỊCH VỤ DẦU KHÍ QUẢNG NGÃI",
     10.5, True, RGBColor(180, 210, 245))
text(s1, Inches(1.3), Inches(2.25), Inches(11.0), Inches(1.3),
     "BÁO CÁO THỰC HIỆN CHỈ ĐẠO BAN GIÁM ĐỐC:\nPHƯƠNG ÁN TRIỂN KHAI NỀN TẢNG DỮ LIỆU & TRỤC TÍCH HỢP",
     22, True, WHITE)
text(s1, Inches(1.3), Inches(3.6), Inches(11.0), Inches(0.5),
     "Bản đặc tả Kiến trúc kỹ thuật Hybrid Data Platform Hub-Spoke (Level 3) & Kế hoạch hành động",
     13, False, RGBColor(210, 225, 245))

shape(s1, Inches(1.3), Inches(4.3), Inches(10.5), Inches(0.02), RGBColor(60, 90, 130))

parts = [
    "Phần A — Tổng quan Nền tảng Dữ liệu TCT: Kiến trúc Hybrid, kết quả GĐ1, Nghị quyết HĐQT",
    "Phần B — Hiện trạng PTSC Quảng Ngãi: 4 hệ thống, văn bản TCT khuyến nghị rà soát Mua sắm",
    "Phần C — Đặc tả Kiến trúc Kỹ thuật 4 Tầng: Spoke, Landing Zone, Cổng duyệt dữ liệu, Tenant L3",
    "Phần D — Kế hoạch Hành động & Kiến nghị: 3 Chặng triển khai, bảo vệ ngân sách công ty"
]
for i, p in enumerate(parts):
    numbered_label(s1, Inches(1.3), Inches(4.5 + i * 0.46), i + 1, GOLD, Inches(0.28))
    text(s1, Inches(1.7), Inches(4.5 + i * 0.46), Inches(10.0), Inches(0.35), p, 10.5, False, RGBColor(220, 235, 255))

shape(s1, Inches(0.8), Inches(6.4), Inches(11.7), Inches(0.7), line=RGBColor(40, 70, 110), rounded=True)
text(s1, Inches(1.0), Inches(6.5), Inches(6.0), Inches(0.3),
     "Đơn vị thực hiện:  Tổ Công tác Chuyển đổi số & CNTT  –  PTSC Quảng Ngãi", 10.5, color=WHITE)
text(s1, Inches(7.5), Inches(6.5), Inches(4.8), Inches(0.3),
     "Kính trình:  Ban Giám đốc Công ty PTSC Quảng Ngãi", 10.5, True, RGBColor(253, 224, 71))

note(s1, "Báo cáo phương án triển khai Nền tảng Dữ liệu theo chỉ đạo của Ban Giám đốc và văn bản khuyến nghị mới nhất từ Ban Dự án Chuyển đổi số TCT.")

# =========================================================================
# SLIDE 2: MỤC LỤC
# =========================================================================
s2 = prs.slides.add_slide(BL)
header(s2, "NỘI DUNG BÁO CÁO", "TỔNG QUAN CHƯƠNG TRÌNH", "")
toc = [
    ("PHẦN A", "TỔNG QUAN NỀN TẢNG DỮ LIỆU TCT", "Kiến trúc Hybrid Data Platform, kết quả Giai đoạn 1 tại TCT và Nghị quyết số 10/NQ-HĐQT.", BLUE, BLUE_SOFT, "Slide 03–04"),
    ("PHẦN B", "HIỆN TRẠNG TẠI PTSC QUẢNG NGÃI", "Vị thế Level 3, 4 hệ thống phần mềm, văn bản TCT khuyến nghị giãn tiến độ phần mềm Mua sắm.", TEAL, RGBColor(230, 248, 246), "Slide 05–07"),
    ("PHẦN C", "ĐẶC TẢ KIẾN TRÚC KỸ THUẬT 4 TẦNG", "Sơ đồ kiến trúc tổng thể, Cổng quyết định dữ liệu 3 mức, Vùng đệm Landing Zone và Ma trận RBAC.", GOLD, GOLD_SOFT, "Slide 08–12"),
    ("PHẦN D", "KẾ HOẠCH HÀNH ĐỘNG & KIẾN NGHỊ", "Lộ trình 3 chặng, giải pháp xử lý gói Mua sắm & HSEQ, phân bổ ngân sách và kiến nghị phê duyệt.", GREEN, GREEN_SOFT, "Slide 13–18")
]
for i, (part, title, desc, col, bg_c, slides_range) in enumerate(toc):
    y = Inches(1.5 + i * 1.35)
    shape(s2, Inches(0.8), y, Inches(11.7), Inches(1.2), bg_c, col, Pt(1.5), rounded=True)
    shape(s2, Inches(0.8), y, Inches(1.5), Inches(1.2), col, rounded=False)
    text(s2, Inches(0.8), y + Inches(0.35), Inches(1.5), Inches(0.5), part, 14, True, WHITE, PP_ALIGN.CENTER)
    text(s2, Inches(2.5), y + Inches(0.15), Inches(7.5), Inches(0.35), title, 13, True, col)
    text(s2, Inches(2.5), y + Inches(0.55), Inches(7.5), Inches(0.55), desc, 10.5, color=BLACK)
    shape(s2, Inches(10.2), y + Inches(0.35), Inches(2.0), Inches(0.5), col, rounded=True)
    text(s2, Inches(10.2), y + Inches(0.42), Inches(2.0), Inches(0.35), slides_range, 11, True, WHITE, PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 3: BỐI CẢNH TCT
# =========================================================================
s3 = prs.slides.add_slide(BL)
header(s3, "BỐI CẢNH CHIẾN LƯỢC: TỔNG CÔNG TY HOÀN THÀNH GIAI ĐOẠN 1", "PHẦN A: TỔNG QUAN NỀN TẢNG DỮ LIỆU TCT", "01")
facts = [
    ("Giai đoạn 1 đã hoàn thành (8/2026)", "TCT đã nghiệm thu Nền tảng Hybrid: MinIO On-prem, Microsoft Fabric OneLake 20TB, 50 API và 35 quy trình."),
    ("Nghị quyết 10/NQ-HĐQT bắt buộc", "Mốc 2026–2027: Các đơn vị thành viên (như Quảng Ngãi) phải hoàn thành kết nối — đây là KPI Chuyển đổi số bắt buộc."),
    ("Dữ liệu cốt lõi nằm tại Đơn vị", "Hơn 80% dữ liệu SXKD phát sinh tại đơn vị. Không kết nối đơn vị thì nền tảng TCT không phát huy được giá trị."),
    ("Khung pháp lý an toàn thông tin mới", "Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, Luật An ninh mạng bắt buộc quản trị và truy vết dữ liệu tập trung.")
]
for i, (title, desc) in enumerate(facts):
    y = Inches(1.5 + i * 1.35)
    shape(s3, Inches(0.8), y, Inches(11.7), Inches(1.15), WHITE, BLUE, Pt(1), rounded=True)
    shape(s3, Inches(0.8), y, Inches(0.1), Inches(1.15), BLUE)
    numbered_label(s3, Inches(1.1), y + Inches(0.35), i + 1, BLUE)
    text(s3, Inches(1.6), y + Inches(0.15), Inches(10.5), Inches(0.3), title, 12, True, NAVY)
    text(s3, Inches(1.6), y + Inches(0.48), Inches(10.5), Inches(0.55), desc, 10.5, color=BLACK)

# =========================================================================
# SLIDE 4: GIẢI PHÁP HYBRID
# =========================================================================
s4 = prs.slides.add_slide(BL)
header(s4, "GIẢI PHÁP HYBRID DATA PLATFORM: ĐẦU TƯ TẬP TRUNG TẠI TỔNG CÔNG TY", "PHẦN A: TỔNG QUAN NỀN TẢNG DỮ LIỆU TCT", "02")
shape(s4, Inches(0.8), Inches(1.5), Inches(5.6), Inches(4.5), WHITE, BLUE, Pt(1.5), rounded=True)
shape(s4, Inches(0.8), Inches(1.5), Inches(5.6), Inches(0.6), BLUE)
text(s4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(0.4), "ON-PREMISE (DATA CENTER TỔNG CÔNG TY)", 12, True, WHITE, PP_ALIGN.CENTER)
onprem_items = [
    "Hạ tầng máy chủ dHCI công nghệ cao đã đầu tư",
    "MinIO S3 Object Storage — Lưu trữ dữ liệu thô & chi tiết",
    "Trục tích hợp ESB (WSO2) — Kết nối API tập trung",
    "Hệ thống MDM — 29 Danh mục Dữ liệu chủ toàn TCT",
    "Hệ thống SIEM / SOC — Giám sát an ninh mạng 24/7"
]
for j, it in enumerate(onprem_items):
    text(s4, Inches(1.2), Inches(2.3 + j * 0.65), Inches(5.0), Inches(0.5), f"• {it}", 10.5, False, BLACK)

shape(s4, Inches(6.9), Inches(1.5), Inches(5.6), Inches(4.5), WHITE, PURPLE, Pt(1.5), rounded=True)
shape(s4, Inches(6.9), Inches(1.5), Inches(5.6), Inches(0.6), PURPLE)
text(s4, Inches(6.9), Inches(1.6), Inches(5.6), Inches(0.4), "CLOUD (MICROSOFT FABRIC / ONELAKE)", 12, True, WHITE, PP_ALIGN.CENTER)
cloud_items = [
    "Microsoft Fabric Capacity F16 tính toán hiệu năng cao",
    "OneLake Storage 20TB — Hồ dữ liệu phân tích tập trung",
    "Microsoft Purview — Quản trị danh mục siêu dữ liệu",
    "Power BI Service — Phục vụ Dashboard Web & Mobile",
    "Cấp riêng Workspace L3 độc lập cho PTSC Quảng Ngãi"
]
for j, it in enumerate(cloud_items):
    text(s4, Inches(7.3), Inches(2.3 + j * 0.65), Inches(5.0), Inches(0.5), f"• {it}", 10.5, False, BLACK)

shape(s4, Inches(0.8), Inches(6.2), Inches(11.7), Inches(0.8), GOLD_SOFT, GOLD, Pt(1), rounded=True)
text(s4, Inches(1.0), Inches(6.25), Inches(11.3), Inches(0.7),
     "KẾT LUẬN CHO QUẢNG NGÃI: TCT đã đầu tư hàng chục tỷ cho toàn bộ hạ tầng phần cứng và bản quyền phần mềm.\n"
     "PTSC Quảng Ngãi KHÔNG PHẢI MUA SẮM MÁY CHỦ — chỉ cần xây dựng Trạm Spoke để kết nối vào hệ sinh thái dùng chung.",
     10.5, True, NAVY, PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 5: VỊ THẾ LEVEL 3
# =========================================================================
s5 = prs.slides.add_slide(BL)
header(s5, "VỊ THẾ PTSC QUẢNG NGÃI: LEVEL 3 TRONG MÔ HÌNH HUB-SPOKE CỦA TCT", "PHẦN B: HIỆN TRẠNG TẠI QUẢNG NGÃI — PHÂN LOẠI ĐƠN VỊ", "03")
levels = [
    ("L1 — CHI NHÁNH NHỎ", "Văn phòng Hà Nội, Miền Trung, Petro Hotel... Dùng chung 100% như một Ban của TCT. Không có Tenant riêng.", GRAY_DARK, GRAY_LIGHT, False),
    ("L2 — DÙNG CHUNG CÓ PHẦN MỀM RIÊNG", "Chi nhánh Supply Base, Marine... Dùng chung ERP/HRM TCT và tích hợp thêm dữ liệu thăm dò, tàu bè.", GRAY_DARK, GRAY_LIGHT, False),
    ("L3 — ĐƠN VỊ LỚN (PTSC QUẢNG NGÃI)", "PTSC Quảng Ngãi, PPS, POS, Thanh Hóa...\nĐược cấp Workspace L3 riêng biệt trên Hub TCT.\nKhông cần đầu tư máy chủ dHCI tiền tỷ.\nTối ưu chi phí, làm chủ Dashboard quản trị riêng.", BLUE, BLUE_SOFT, True),
    ("L4 — ĐƠN VỊ ĐẶC THÙ (PTSC M&C)", "PTSC M&C tự đầu tư hạ tầng Hybrid Data Platform riêng tại chỗ do khối lượng dữ liệu công trình biển và OT quá lớn.", GRAY_DARK, GRAY_LIGHT, False),
]
for i, (title, desc, col, bg_c, highlight) in enumerate(levels):
    x = Inches(0.8 + i * 2.95)
    border_w = Pt(2.5) if highlight else Pt(1.0)
    shape(s5, x, Inches(1.5), Inches(2.75), Inches(4.5), bg_c, col, border_w, rounded=True)
    shape(s5, x, Inches(1.5), Inches(2.75), Inches(0.65), col)
    text(s5, x, Inches(1.55), Inches(2.75), Inches(0.55), title, 10.5, True, WHITE, PP_ALIGN.CENTER)
    text(s5, x + Inches(0.12), Inches(2.3), Inches(2.5), Inches(3.5), desc, 10, color=BLACK)

shape(s5, Inches(0.8), Inches(6.2), Inches(11.7), Inches(0.8), BLUE_SOFT, BLUE, Pt(1), rounded=True)
text(s5, Inches(1.0), Inches(6.25), Inches(11.3), Inches(0.7),
     "QUYẾT ĐỊNH CỦA TCT TẠI HỘI THẢO (TRANG 56): PTSC Quảng Ngãi thuộc Nhóm 4 (Đơn vị lớn L3-L4).\n"
     "Quảng Ngãi vừa có không gian lưu trữ độc lập (Tenant L3), vừa không phát sinh chi phí đầu tư phần cứng ban đầu.",
     10.5, True, NAVY, PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 6: HIỆN TRẠNG 4 HỆ THỐNG & EMAIL KHUYẾN NGHỊ CỦA TCT
# =========================================================================
s6 = prs.slides.add_slide(BL)
header(s6, "HIỆN TRẠNG HỆ THỐNG VÀ VĂN BẢN CHỈ ĐẠO MỚI NHẤT TỪ TỔNG CÔNG TY", "PHẦN B: HIỆN TRẠNG TẠI QUẢNG NGÃI — VẤN ĐỀ CẦN GIẢI QUYẾT", "04")

shape(s6, Inches(0.8), Inches(1.4), Inches(5.6), Inches(4.6), WHITE, BLUE, Pt(1.5), rounded=True)
shape(s6, Inches(0.8), Inches(1.4), Inches(5.6), Inches(0.45), BLUE)
text(s6, Inches(0.8), Inches(1.45), Inches(5.6), Inches(0.35), "4 HỆ THỐNG PHẦN MỀM THỰC TẾ TẠI QUẢNG NGÃI", 11, True, WHITE, PP_ALIGN.CENTER)

softwares = [
    ("FAST Accounting", "Kế toán, tài chính, hóa đơn, công nợ — Đang chạy ổn định"),
    ("MESx – PMSx – FBO", "Quản lý sản xuất, tiến độ xưởng cơ khí Dung Quất, vật tư"),
    ("VTI – IRTECH", "Quản lý khai thác Cảng PTSC Quảng Ngãi, cầu bãi, thiết bị"),
    ("HSEQ & Mua sắm hàng hóa", "Đang lập phương án mua sắm và xây dựng quy trình")
]
for i, (name, desc) in enumerate(softwares):
    y = Inches(2.0 + i * 0.95)
    shape(s6, Inches(1.0), y, Inches(5.2), Inches(0.85), GRAY_LIGHT, GRAY_MED, Pt(0.5), rounded=True)
    text(s6, Inches(1.15), y + Inches(0.08), Inches(4.9), Inches(0.25), f"• {name}", 10.5, True, NAVY)
    text(s6, Inches(1.15), y + Inches(0.35), Inches(4.9), Inches(0.45), desc, 9.5, color=BLACK)

shape(s6, Inches(6.9), Inches(1.4), Inches(5.6), Inches(4.6), RED_SOFT, RED, Pt(1.5), rounded=True)
shape(s6, Inches(6.9), Inches(1.4), Inches(5.6), Inches(0.45), RED)
text(s6, Inches(6.9), Inches(1.45), Inches(5.6), Inches(0.35), "CẢNH BÁO TỪ BDA CĐS TỔNG CÔNG TY (EMAIL 07/09/2026)", 11, True, WHITE, PP_ALIGN.CENTER)

text(s6, Inches(7.1), Inches(1.95), Inches(5.2), Inches(3.9),
     "Ý KIẾN PHÓ GIÁM ĐỐC BDA TCT (CHỊ PHAN THỊ NGỌC VÂN):\n\n"
     "1. Nguy cơ kết nối trực tiếp (Point-to-Point):\n"
     "   Phương án tích hợp nội bộ giữa MESx – PMSx – FBO nối sang FAST, VTI, IRTECH... sẽ làm bùng nổ số lượng API, chi phí tích hợp và rủi ro mất ATTT.\n\n"
     "2. Yêu cầu chuyển sang Kiến trúc Trục tích hợp (ESB / Data Platform):\n"
     "   TCT yêu cầu Quảng Ngãi tích hợp tập trung qua ESB/MDM của Data Platform.\n\n"
     "3. Đề nghị tạm thời giãn tiến độ Phần mềm Mua sắm:\n"
     "   Tạm dừng để rà soát kiến trúc tổng thể, tránh đầu tư chồng chéo.",
     10, False, BLACK)

shape(s6, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.85), GOLD_SOFT, GOLD, Pt(1), rounded=True)
text(s6, Inches(1.0), Inches(6.2), Inches(11.3), Inches(0.75),
     "Ý NGHĨA QUAN TRỌNG: TCT khuyến nghị hoàn toàn đúng về mặt kỹ thuật. Đây là cơ hội để Quảng Ngãi dừng kết nối 'mạng nhện',\n"
     "chuyển sang Trục tích hợp chuẩn TCT để tiết kiệm hàng trăm triệu chi phí viết API và tránh bị TCT từ chối sau này.",
     10, True, NAVY, PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 7: QUY CHẾ 5 CẤP & QUYỀN LÃNH ĐẠO ĐƠN VỊ
# =========================================================================
s7 = prs.slides.add_slide(BL)
header(s7, "QUY CHẾ QUẢN TRỊ DỮ LIỆU PTSC: MÔ HÌNH 5 CẤP VÀ QUYỀN CỦA ĐƠN VỊ", "PHẦN B: HIỆN TRẠNG TẠI QUẢNG NGÃI — CHỦ QUYỀN DỮ LIỆU", "05")
gov_levels = [
    ("CẤP 1–2: HỘI ĐỒNG QUẢN TRỊ DỮ LIỆU & HỘI ĐỒNG DỮ LIỆU KHỐI (TCT)", "Định hướng chiến lược dữ liệu toàn PTSC. Phê duyệt chính sách, tiêu chuẩn. Điều phối liên Ban, đồng bộ Master Data.", GRAY_DARK, GRAY_LIGHT, False),
    ("CẤP 3: CHỦ QUẢN DỮ LIỆU — LÃNH ĐẠO ĐƠN VỊ (PTSC QUẢNG NGÃI)",
     "• Quản lý nghiệp vụ dữ liệu của đơn vị; TRÁCH NHIỆM GIẢI TRÌNH ĐẶT Ở CẤP NÀY.\n"
     "• Toàn quyền quyết định dữ liệu nào được chia sẻ, dữ liệu nào giữ lại nội bộ.\n"
     "• Có quyền DỪNG CHIA SẺ KHẨN CẤP nếu phát hiện nguy cơ mất an toàn thông tin.\n"
     "• Phê duyệt bản ghi chuẩn khi dữ liệu giữa các phần mềm nội bộ có mâu thuẫn.",
     GREEN, GREEN_SOFT, True),
    ("CẤP 4: QUẢN TRỊ MIỀN DỮ LIỆU (DATA STEWARDS — IT & NGHIỆP VỤ QN)", "Phụ trách từ điển dữ liệu, ánh xạ danh mục, kiểm soát chất lượng dữ liệu và cấu hình phân quyền trên Tenant L3.", GRAY_DARK, GRAY_LIGHT, False),
    ("CẤP 5: ĐƠN VỊ VẬN HÀNH NỀN TẢNG (BAN NCPT&CĐS TCT / HIPT-AITS)",
     "Chỉ vận hành hạ tầng máy chủ, đường truyền mạng, bảo mật. TUYỆT ĐỐI KHÔNG ĐƯỢC XEM DỮ LIỆU NGHIỆP VỤ CỦA ĐƠN VỊ.", RED, RED_SOFT, False),
]
y_pos = Inches(1.4)
for title, desc, col, bg_c, highlight in gov_levels:
    h = Inches(1.9) if highlight else Inches(1.0)
    border_w = Pt(2.5) if highlight else Pt(1.0)
    shape(s7, Inches(0.8), y_pos, Inches(11.7), h, bg_c, col, border_w, rounded=True)
    shape(s7, Inches(0.84), y_pos + Inches(0.04), Inches(0.1), h - Inches(0.08), col)
    text(s7, Inches(1.2), y_pos + Inches(0.08), Inches(11.0), Inches(0.35), title, 11.5, True, col)
    text(s7, Inches(1.2), y_pos + (Inches(0.5) if highlight else Inches(0.38)), Inches(11.0), Inches(1.3 if highlight else 0.55), desc, 10, color=BLACK)
    y_pos += h + Inches(0.12)

# =========================================================================
# SLIDE 8: CỔNG QUYẾT ĐỊNH DỮ LIỆU (3 MỨC PHÂN LOẠI)
# =========================================================================
s8 = prs.slides.add_slide(BL)
header(s8, "CỔNG QUYẾT ĐỊNH DỮ LIỆU: CÁI GÌ ĐẨY LÊN, CÁI GÌ GIỮ LẠI NỘI BỘ?", "PHẦN C: ĐẶC TẢ KIẾN TRÚC KỸ THUẬT — BẢO VỆ CHỦ QUYỀN DỮ LIỆU", "06")

decisions = [
    ("MỨC 1: BÍ MẬT & NHẠY CẢM", "GIỮ LẠI 100% NỘI BỘ QUẢNG NGÃI", RED, RED_SOFT,
     ["• Chi tiết mức lương từng cán bộ, nhân viên", "• Số CCCD, số tài khoản ngân hàng cá nhân", "• Định mức đơn giá, dự toán thầu mật", "• Hồ sơ khiếu nại, hợp đồng nhạy cảm", "", "LƯU TRỮ TẠI CHỖ:", "CSDL On-prem QN, cấm truyền ra ngoài."]),
    
    ("MỨC 2: CHUYÊN NGÀNH NỘI BỘ", "LƯU VÀO TENANT L3 TRÊN CLOUD", BLUE, BLUE_SOFT,
     ["• Nhật trình xe cẩu, tàu lai dắt tại Cảng QN", "• Sản lượng chi tiết xưởng cơ khí Dung Quất", "• Nhật ký công trường, chấm công ca kíp", "• Báo cáo điều hành phục vụ riêng Ban Giám đốc", "", "PHÂN VÙNG CÁCH LY:", "Chỉ User QN xem được, TCT không thấy."]),
    
    ("MỨC 3: DÙNG CHUNG & HỢP NHẤT", "ĐỒNG BỘ VỀ HUB TỔNG CÔNG TY", GREEN, GREEN_SOFT,
     ["• Báo cáo tổng hợp Doanh thu - Lợi nhuận", "• Tổng số lao động & Quỹ lương toàn công ty", "• 29 Danh mục Master Data (Mã KH, NCC)", "• Báo cáo sự cố an toàn HSE định kỳ", "", "ĐIỀU KIỆN TRUYỀN:", "Lãnh đạo QN bấm APPROVE mới truyền đi."])
]

for i, (lvl, action, col, bg_c, items) in enumerate(decisions):
    x = Inches(0.8 + i * 4.05)
    shape(s8, x, Inches(1.4), Inches(3.7), Inches(5.5), bg_c, col, Pt(1.5), rounded=True)
    shape(s8, x, Inches(1.4), Inches(3.7), Inches(0.7), col)
    text(s8, x, Inches(1.43), Inches(3.7), Inches(0.3), lvl, 10, True, WHITE, PP_ALIGN.CENTER)
    text(s8, x, Inches(1.75), Inches(3.7), Inches(0.3), action, 10.5, True, RGBColor(254, 240, 138), PP_ALIGN.CENTER)
    
    for j, it in enumerate(items):
        is_hd = (j == 0 or j == len(items)-2)
        c = col if is_hd else BLACK
        text(s8, x + Inches(0.15), Inches(2.3 + j * 0.45), Inches(3.4), Inches(0.4), it, 10, is_hd, c)

# =========================================================================
# SLIDE 9: KIẾN TRÚC TỔNG THỂ 4 TẦNG (END-TO-END)
# =========================================================================
s9 = prs.slides.add_slide(BL)
header(s9, "KIẾN TRÚC TỔNG THỂ 4 TẦNG: TỪ HỆ THỐNG NGUỒN ĐẾN DASHBOARD ĐIỀU HÀNH", "PHẦN C: ĐẶC TẢ KIẾN TRÚC KỸ THUẬT — SƠ ĐỒ END-TO-END", "07")

pipe_4t = [
    ("TẦNG 1: NGUỒN DỮ LIỆU", "NỘI BỘ QUẢNG NGÃI", BLUE, BLUE_SOFT,
     ["Hệ thống nghiệp vụ QN:", "• FAST Kế toán & Hóa đơn", "• MESx-PMSx xưởng cơ khí", "• VTI-IRTECH quản lý Cảng", "• HSEQ & Mua sắm", "• Excel dự toán, chấm công", "", "Hoạt động bình thường."]),
    
    ("TẦNG 2: SPOKE & VÙNG ĐỆM", "LANDING ZONE & CỔNG DUYỆT", TEAL, RGBColor(230, 248, 246),
     ["Xử lý an toàn tại chỗ:", "• Agent trích xuất tự động", "• Landing Zone kiểm duyệt", "• Masking ẩn dữ liệu cá nhân", "• Cổng duyệt Data Owner:", "  [APPROVE] hoặc [REJECT]", "", "Chỉ truyền dữ liệu đã duyệt."]),
    
    ("TẦNG 3: ON-PREM HUB TCT", "DATA CENTER TỔNG CÔNG TY", GOLD, GOLD_SOFT,
     ["Hạ tầng lõi bảo mật:", "• Đường hầm VPN IPSec", "• Trục tích hợp ESB (WSO2)", "• MDM: 29 Danh mục chuẩn", "• MinIO Lakehouse (Bronze)", "• SIEM giám sát 24/7", "", "TCT vận hành hạ tầng."]),
    
    ("TẦNG 4: CLOUD FABRIC", "TENANT L3 & DASHBOARD", PURPLE, PURPLE_SOFT,
     ["Khai thác thông minh:", "• OneLake Storage (Gold)", "• Workspace L3 riêng của QN", "• Pipeline tự tính toán KPI", "• Power BI Mobile / Web", "• Dashboard Ban Giám đốc", "", "Xem tức thời trên điện thoại."])
]

for i, (t_name, t_sub, col, bg_c, lines) in enumerate(pipe_4t):
    x = Inches(0.6 + i * 3.1)
    shape(s9, x, Inches(1.5), Inches(2.75), Inches(5.4), bg_c, col, Pt(1.5), rounded=True)
    shape(s9, x, Inches(1.5), Inches(2.75), Inches(0.65), col)
    text(s9, x, Inches(1.53), Inches(2.75), Inches(0.35), t_name, 10.5, True, WHITE, PP_ALIGN.CENTER)
    text(s9, x, Inches(1.88), Inches(2.75), Inches(0.25), t_sub, 8.5, True, RGBColor(254, 240, 138), PP_ALIGN.CENTER)
    for j, l in enumerate(lines):
        bold_line = (j == 0 or j == len(lines)-1)
        c = col if bold_line else BLACK
        text(s9, x + Inches(0.12), Inches(2.35 + j * 0.45), Inches(2.5), Inches(0.4), l, 10, bold_line, c)
    if i < 3:
        arrow_shape(s9, Inches(3.42 + i * 3.1), Inches(4.0), "right", Inches(0.3), Inches(0.22))

# =========================================================================
# SLIDE 10: QUY TRÌNH VÙNG ĐỆM LANDING ZONE (4 BƯỚC)
# =========================================================================
s10 = prs.slides.add_slide(BL)
header(s10, "QUY TRÌNH KIỂM SOÁT VÙNG ĐỆM (LANDING ZONE): DỮ LIỆU KHÔNG THỂ TỰ Ý ĐẨY ĐI", "PHẦN C: ĐẶC TẢ KIẾN TRÚC KỸ THUẬT — CƠ CHẾ LANDING ZONE", "08")

lz_steps = [
    ("BƯỚC 1: TRÍCH XUẤT NỬA ĐÊM", "AGENT NỘI BỘ ĐỌC READ-ONLY", BLUE,
     "Vào 23h00 hàng ngày, Agent tự động kết nối (quyền chỉ đọc) vào FAST, MESx, VTI để lấy bản sao dữ liệu phát sinh trong ngày đưa vào Vùng đệm Landing Zone nội bộ. Tuyệt đối không làm ảnh hưởng phần mềm đang chạy."),
    
    ("BƯỚC 2: KIỂM TRA TỰ ĐỘNG", "VALIDATION & MASKING RULE", TEAL,
     "Hệ thống tự động chạy bộ lọc 3 lớp:\n1. Kiểm tra cấu trúc Schema (đúng định dạng số, ngày tháng).\n2. Đối soát mã Nhà cung cấp, vật tư với MDM TCT.\n3. Che mờ dữ liệu cá nhân (ẩn số CCCD, tài khoản ngân hàng)."),
    
    ("BƯỚC 3: PHÊ DUYỆT ĐIỆN TỬ", "DATA STEWARD & DATA OWNER", GOLD,
     "Hiển thị bảng tổng hợp trên giao diện nội bộ:\n• IT Quảng Ngãi (Data Steward) soát lỗi kỹ thuật.\n• Lãnh đạo Đơn vị (Data Owner) xem và bấm: [APPROVE] (Cho phép truyền) hoặc [REJECT] (Hủy luồng, giữ lại chỉnh sửa)."),
    
    ("BƯỚC 4: MÃ HÓA & TRUYỀN TẢI", "VPN IPSEC SANG HUB TCT", GREEN,
     "Chỉ các gói dữ liệu có chữ ký điện tử APPROVE mới được kích hoạt mã hóa AES-256 và truyền qua đường hầm VPN IPSec sang Hub TCT. Hệ thống SIEM ghi nhận Audit Log đầy đủ.")
]

for i, (st_t, st_sub, col, desc) in enumerate(lz_steps):
    y = Inches(1.5 + i * 1.35)
    shape(s10, Inches(0.8), y, Inches(11.7), Inches(1.2), WHITE, col, Pt(1.5), rounded=True)
    shape(s10, Inches(0.8), y, Inches(3.2), Inches(1.2), col, rounded=False)
    numbered_label(s10, Inches(1.0), y + Inches(0.4), i + 1, WHITE, Inches(0.4))
    text(s10, Inches(1.5), y + Inches(0.25), Inches(2.4), Inches(0.35), st_t, 10.5, True, WHITE)
    text(s10, Inches(1.5), y + Inches(0.65), Inches(2.4), Inches(0.3), st_sub, 8.5, True, RGBColor(254, 240, 138))
    text(s10, Inches(4.2), y + Inches(0.15), Inches(8.1), Inches(0.9), desc, 10.5, color=BLACK)

# =========================================================================
# SLIDE 11: MA TRẬN PHÂN QUYỀN RBAC & CÔ LẬP TENANT L3
# =========================================================================
s11 = prs.slides.add_slide(BL)
header(s11, "MA TRẬN PHÂN QUYỀN RBAC: CÔ LẬP DỮ LIỆU TUYỆT ĐỐI THEO TỪNG VAI TRÒ", "PHẦN C: ĐẶC TẢ KIẾN TRÚC KỸ THUẬT — AN TOÀN TRUY CẬP", "09")

shape(s11, Inches(0.8), Inches(1.4), Inches(11.7), Inches(0.45), NAVY)
text(s11, Inches(0.9), Inches(1.48), Inches(3.0), Inches(0.3), "ĐỐI TƯỢNG NGƯỜI DÙNG", 10.5, True, WHITE)
text(s11, Inches(4.0), Inches(1.48), Inches(2.6), Inches(0.3), "DỮ LIỆU QUẢNG NGÃI", 10.5, True, WHITE, PP_ALIGN.CENTER)
text(s11, Inches(6.7), Inches(1.48), Inches(2.6), Inches(0.3), "DỮ LIỆU ĐVTV KHÁC", 10.5, True, WHITE, PP_ALIGN.CENTER)
text(s11, Inches(9.4), Inches(1.48), Inches(3.0), Inches(0.3), "QUYỀN TRÊN TENANT L3", 10.5, True, WHITE, PP_ALIGN.CENTER)

rbac_rows = [
    ("Ban Giám đốc PTSC Quảng Ngãi", "TOÀN QUYỀN 100% NỘI BỘ", "KHÔNG THỂ XEM", "Data Owner Cấp 3: Xem toàn bộ Dashboard, duyệt dữ liệu đi", GREEN),
    ("Trưởng phòng / Key User QN", "THEO PHÒNG BAN PHỤ TRÁCH", "KHÔNG THỂ XEM", "Data Contributor: Xem Dashboard chuyên ngành của phòng", BLUE),
    ("Bộ phận IT PTSC Quảng Ngãi", "QUẢN TRỊ LUỒNG KỸ THUẬT", "KHÔNG THỂ XEM", "Data Steward Cấp 4: Quản trị luồng ETL, phân quyền User QN", BLUE),
    ("Ban Lãnh đạo Tổng công ty", "CHỈ XEM SỐ TỔNG HỢP HỢP NHẤT", "XEM TỔNG HỢP TOÀN TCT", "Không có quyền truy cập vào bảng chi tiết trong Tenant QN", GOLD),
    ("Đội IT TCT (Admin Level 5)", "BỊ CẤM XEM DỮ LIỆU NGHIỆP VỤ", "BỊ CẤM XEM DỮ LIỆU", "Chỉ vận hành máy chủ, mở xem sẽ bị SIEM báo động đỏ", RED),
    ("Đơn vị bạn (PTSC M&C, POS...)", "TUYỆT ĐỐI BỊ CÔ LẬP 100%", "CHỈ XEM ĐƠN VỊ HỌ", "Bị chặn hoàn toàn bởi kiến trúc Multi-tenancy độc lập", RED)
]

for i, (usr, qn_d, other_d, perm, col) in enumerate(rbac_rows):
    y = Inches(1.95 + i * 0.82)
    bg = WHITE if i % 2 == 0 else GRAY_LIGHT
    shape(s11, Inches(0.8), y, Inches(11.7), Inches(0.76), bg, GRAY_MED, Pt(0.5))
    text(s11, Inches(0.95), y + Inches(0.2), Inches(3.0), Inches(0.4), usr, 10.5, True, BLACK)
    text(s11, Inches(4.0), y + Inches(0.2), Inches(2.6), Inches(0.4), qn_d, 10, True, col, PP_ALIGN.CENTER)
    text(s11, Inches(6.7), y + Inches(0.2), Inches(2.6), Inches(0.4), other_d, 10, True, RED if "BỊ" in other_d or "KHÔNG" in other_d else BLACK, PP_ALIGN.CENTER)
    text(s11, Inches(9.4), y + Inches(0.12), Inches(3.0), Inches(0.55), perm, 9.5, False, BLACK, PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 12: SO SÁNH 2 PHƯƠNG ÁN & BÀI HỌC TỪ EMAIL TCT
# =========================================================================
s12 = prs.slides.add_slide(BL)
header(s12, "SO SÁNH 2 PHƯƠNG ÁN TRIỂN KHAI THEO CHỈ ĐẠO BAN GIÁM ĐỐC", "PHẦN C: ĐẶC TẢ KIẾN TRÚC KỸ THUẬT — LỰA CHỌN TỐI ƯU", "10")

shape(s12, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4), RED_SOFT, RED, Pt(1.5), rounded=True)
shape(s12, Inches(0.8), Inches(1.4), Inches(5.6), Inches(0.5), RED)
text(s12, Inches(0.8), Inches(1.42), Inches(5.6), Inches(0.4), "PHƯƠNG ÁN 1: CHỜ TỔNG CÔNG TY TRIỂN KHAI", 12, True, WHITE, PP_ALIGN.CENTER)

pa1 = [
    ("Khả thi nhân lực", "KHÔNG ĐẢM BẢO", RED, "Ban NCPT&CĐS TCT chỉ vận hành Hub chung, không đủ kỹ sư cắm chốt tại Quảng Ngãi để bóc tách CSDL 4 phần mềm."),
    ("Tiến độ thực hiện", "RỦI RO TRỄ HẠN CAO", RED, "Hơn 10 đơn vị đang xếp hàng. Email ngày 07/09 của TCT cho thấy TCT đang quá tải và đề nghị giãn tiến độ."),
    ("Nghiệp vụ nội bộ", "CHỈ LÀM BÁO CÁO TCT", RED, "TCT chỉ tập trung lấy số hợp nhất cho TCT. Không xây dựng Dashboard điều hành riêng cho Giám đốc Quảng Ngãi."),
    ("Mức độ tự chủ", "PHỤ THUỘC HOÀN TOÀN", RED, "Mọi sửa đổi luồng dữ liệu đều phải làm công văn xin TCT, rất chậm trễ và quan liêu.")
]
for i, (crit, val, v_col, desc) in enumerate(pa1):
    y = Inches(2.1 + i * 1.1)
    shape(s12, Inches(1.0), y, Inches(5.2), Inches(0.95), WHITE, GRAY_MED, Pt(0.5), rounded=True)
    text(s12, Inches(1.15), y + Inches(0.05), Inches(2.5), Inches(0.25), crit, 10, True, BLACK)
    text(s12, Inches(3.5), y + Inches(0.05), Inches(2.5), Inches(0.25), val, 10, True, v_col, PP_ALIGN.RIGHT)
    text(s12, Inches(1.15), y + Inches(0.32), Inches(4.9), Inches(0.55), desc, 9.5, color=BLACK)

shape(s12, Inches(6.9), Inches(1.4), Inches(5.6), Inches(5.4), GREEN_SOFT, GREEN, Pt(2.0), rounded=True)
shape(s12, Inches(6.9), Inches(1.4), Inches(5.6), Inches(0.5), GREEN)
text(s12, Inches(6.9), Inches(1.42), Inches(5.6), Inches(0.4), "PHƯƠNG ÁN 2 (ĐỀ XUẤT): CHỦ ĐỘNG + LÀM VIỆC 3 BÊN VỚI TCT", 11, True, WHITE, PP_ALIGN.CENTER)

pa2 = [
    ("Khả thi nhân lực", "LÀM VIỆC VỚI HIPT-AITS", GREEN, "Làm việc trực tiếp với Liên danh tư vấn của TCT để chuẩn hóa kiến trúc ESB theo đúng khuyến nghị của chị Vân Phan."),
    ("Tiến độ thực hiện", "CHỦ ĐỘNG, 3–4 THÁNG", GREEN, "Chủ động gửi email chốt mốc giãn tiến độ gói Mua sắm (đến hết tháng 10/2026) để kịp tiến độ SXKD của công ty."),
    ("Nghiệp vụ nội bộ", "THIẾT KẾ RIÊNG CHO QN", GREEN, "Vừa đồng bộ dữ liệu chuẩn lên TCT, vừa xây dựng trọn bộ Dashboard quản trị trực tiếp cho Ban Giám đốc QN."),
    ("Mức độ tự chủ", "LÀM CHỦ MÃ NGUỒN 100%", GREEN, "Tự chủ vận hành sau bàn giao, tận dụng miễn phí 100% hạ tầng máy chủ và bản quyền Fabric do TCT đầu tư.")
]
for i, (crit, val, v_col, desc) in enumerate(pa2):
    y = Inches(2.1 + i * 1.1)
    shape(s12, Inches(7.1), y, Inches(5.2), Inches(0.95), WHITE, GRAY_MED, Pt(0.5), rounded=True)
    text(s12, Inches(7.25), y + Inches(0.05), Inches(2.4), Inches(0.25), crit, 10, True, BLACK)
    text(s12, Inches(9.5), y + Inches(0.05), Inches(2.7), Inches(0.25), val, 10, True, v_col, PP_ALIGN.RIGHT)
    text(s12, Inches(7.25), y + Inches(0.32), Inches(4.9), Inches(0.55), desc, 9.5, color=BLACK)

# =========================================================================
# SLIDE 13: CƠ CẤU CHI PHÍ
# =========================================================================
s13 = prs.slides.add_slide(BL)
header(s13, "CƠ CẤU ĐẦU TƯ VÀ DỰ TOÁN NGÂN SÁCH (THEO KHUNG CHI PHÍ CỦA TCT)", "PHẦN D: KẾ HOẠCH HÀNH ĐỘNG — TỐI ƯU NGÂN SÁCH", "11")

cost_rows = [
    ("1", "Hạ tầng máy chủ tại đơn vị", "Tận dụng máy chủ ảo (VM) sẵn có tại Datacenter QN", "0 VNĐ (Tự có)", GREEN),
    ("2", "Hạ tầng Cloud Hub & Bản quyền khung", "Microsoft Fabric 20TB, MinIO, Power BI Enterprise, Purview", "TCT đã đầu tư", BLUE),
    ("3", "Dịch vụ: Khảo sát & Thiết kế kiến trúc", "Khảo sát CSDL 4 phần mềm, lập bảng ánh xạ 29 Master Data", "[Chờ NCC báo giá]", GOLD),
    ("4", "Dịch vụ: Xây dựng Trục tích hợp (ETL)", "Lập trình luồng trích xuất, chuẩn hóa, mã hóa và truyền VPN", "[Chờ NCC báo giá]", GOLD),
    ("5", "Dịch vụ: Xây dựng Dashboard Power BI", "Thiết kế mô hình dữ liệu và các bảng báo cáo quản trị", "[Chờ NCC báo giá]", GOLD),
    ("6", "Đào tạo chuyển giao & Bảo hành", "Bàn giao mã nguồn, đào tạo IT QN vận hành độc lập", "[Chờ NCC báo giá]", GOLD),
    ("7", "Chi phí vận hành nền tảng hàng năm", "TCT phân bổ theo mức sử dụng thực tế (Usage-based)", "Theo cơ chế TCT", GRAY_DARK),
]

shape(s13, Inches(0.8), Inches(1.4), Inches(11.7), Inches(0.4), NAVY)
text(s13, Inches(0.9), Inches(1.45), Inches(0.6), Inches(0.3), "STT", 10, True, WHITE, PP_ALIGN.CENTER)
text(s13, Inches(1.6), Inches(1.45), Inches(3.2), Inches(0.3), "CẤU PHẦN CHI PHÍ", 10, True, WHITE)
text(s13, Inches(4.9), Inches(1.45), Inches(4.5), Inches(0.3), "NỘI DUNG THỰC HIỆN", 10, True, WHITE)
text(s13, Inches(9.5), Inches(1.45), Inches(2.9), Inches(0.3), "DỰ TOÁN", 10, True, WHITE, PP_ALIGN.CENTER)

for i, (stt, comp, desc, cost, c_col) in enumerate(cost_rows):
    y = Inches(1.85 + i * 0.58)
    bg = WHITE if i % 2 == 0 else GRAY_LIGHT
    shape(s13, Inches(0.8), y, Inches(11.7), Inches(0.53), bg, GRAY_MED, Pt(0.5))
    text(s13, Inches(0.9), y + Inches(0.1), Inches(0.6), Inches(0.3), stt, 10, True, BLACK, PP_ALIGN.CENTER)
    text(s13, Inches(1.6), y + Inches(0.1), Inches(3.2), Inches(0.3), comp, 10, True, BLACK)
    text(s13, Inches(4.9), y + Inches(0.1), Inches(4.5), Inches(0.3), desc, 9.5, color=BLACK)
    text(s13, Inches(9.5), y + Inches(0.1), Inches(2.9), Inches(0.3), cost, 10, True, c_col, PP_ALIGN.CENTER)

shape(s13, Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.9), GOLD_SOFT, GOLD, Pt(1.0), rounded=True)
text(s13, Inches(1.1), Inches(6.05), Inches(11.1), Inches(0.8),
     "NGUYÊN TẮC TÀI CHÍNH: Tiết kiệm tối đa chi phí hạ tầng phần cứng nhờ tận dụng đầu tư sẵn có của TCT.\n"
     "Kinh phí dịch vụ kết nối sẽ được xác định chính xác sau khi khảo sát Giai đoạn 2A cùng BDA TCT và Liên danh HIPT-AITS.",
     10.5, True, NAVY, PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 14: KẾ HOẠCH GIAI ĐOẠN 1 (KHẢO SÁT & CHUẨN BỊ NỘI BỘ)
# =========================================================================
s14 = prs.slides.add_slide(BL)
header(s14, "GIAI ĐOẠN 1 CHI TIẾT: KHẢO SÁT, CHUẨN HÓA DỮ LIỆU & LÀM VIỆC VỚI TCT", "PHẦN D: KẾ HOẠCH HÀNH ĐỘNG — CHẶNG 1 (THÁNG 9–11/2026)", "12")

gd1_tasks = [
    ("1.1", "Thành lập Tổ Công tác Nền tảng Dữ liệu", BLUE, BLUE_SOFT,
     ["Lãnh đạo Đơn vị làm Tổ trưởng (Data Owner Cấp 3)", "IT chủ trì kỹ thuật; Key Users từ Kế toán, Cảng, Dự án", "Ban hành Quyết định chính thức làm căn cứ phối hợp"]),
    ("1.2", "Họp 3 bên với BDA TCT & Liên danh HIPT-AITS", TEAL, RGBColor(230, 248, 246),
     ["Thống nhất kiến trúc ESB theo khuyến nghị của TCT", "Gài tiêu chuẩn kết nối API vào gói thầu Mua sắm & HSEQ", "Chốt mốc giãn tiến độ gói Mua sắm đến hết 31/10/2026"]),
    ("1.3", "Rà soát CSDL 4 phần mềm & Ánh xạ Master Data", GOLD, GOLD_SOFT,
     ["Trích xuất cấu trúc bảng của FAST, MESx, VTI", "Lập bảng đối chiếu danh mục Khách hàng, NCC với MDM TCT", "Làm sạch số liệu trùng lặp trước khi kết nối"]),
    ("1.4", "Chuẩn bị Hạ tầng mạng & Thiết lập VPN IPSec", GREEN, GREEN_SOFT,
     ["Cấu hình 01 máy ảo VM tại Datacenter QN làm Spoke Agent", "Thiết lập đường truyền bảo mật VPN IPSec về DC TCT", "Sẵn sàng tiếp nhận bàn giao Tenant L3 trên Microsoft Fabric"])
]
for i, (code, t_name, col, bg_c, bullets) in enumerate(gd1_tasks):
    x = Inches(0.8 + i * 2.95)
    shape(s14, x, Inches(1.5), Inches(2.75), Inches(5.4), bg_c, col, Pt(1.5), rounded=True)
    shape(s14, x, Inches(1.5), Inches(2.75), Inches(0.65), col)
    numbered_label(s14, x + Inches(0.15), Inches(1.62), code, WHITE, Inches(0.38))
    text(s14, x + Inches(0.6), Inches(1.55), Inches(2.05), Inches(0.55), t_name, 10, True, WHITE)
    for j, b in enumerate(bullets):
        text(s14, x + Inches(0.12), Inches(2.4 + j * 0.95), Inches(2.5), Inches(0.85), f"• {b}", 10, False, BLACK)

# =========================================================================
# SLIDE 15: KẾ HOẠCH GIAI ĐOẠN 2 (TRIỂN KHAI TRỤC TÍCH HỢP & ETL)
# =========================================================================
s15 = prs.slides.add_slide(BL)
header(s15, "GIAI ĐOẠN 2 CHI TIẾT: XÂY DỰNG TRỤC TÍCH HỢP & BƠM DỮ LIỆU TỰ ĐỘNG", "PHẦN D: KẾ HOẠCH HÀNH ĐỘNG — CHẶNG 2 (QUÝ 1/2027)", "13")

gd2_steps = [
    ("BƯỚC 1: TIẾP NHẬN TENANT L3", "TCT BÀN GIAO PHÂN VÙNG CLOUD", BLUE,
     "TCT cấp quyền quản trị Workspace L3 trên Microsoft Fabric cho IT Quảng Ngãi. Kiểm tra thông tuyến mạng VPN Site-to-Site giữa DC QN và Hub TCT an toàn tuyệt đối."),
    ("BƯỚC 2: DỰNG SPOKE & LANDING ZONE", "CÀI ĐẶT AGENT TẠI MÁY CHỦ QN", TEAL,
     "Cài đặt Spoke Integration Agent trên máy chủ ảo QN. Cấu hình luồng đọc Read-Only trích xuất dữ liệu từ FAST, MESx, VTI đổ vào Vùng đệm Landing Zone nội bộ."),
    ("BƯỚC 3: XÂY DỰNG LUỒNG PIPELINE & MASKING", "CHUẨN HÓA & LÀM SẠCH DỮ LIỆU", GOLD,
     "Lập trình luồng ETL tự động: Lọc bỏ dữ liệu rác, ánh xạ mã Master Data, che mờ thông tin cá nhân (CCCD, tài khoản). Thiết lập giao diện phê duyệt Approve/Reject cho Lãnh đạo."),
    ("BƯỚC 4: KẾT NỐI VỀ HUB & ĐỒNG BỘ THỬ NGHIỆM", "CHẠY THỬ NGHIỆM TRUYỀN DỮ LIỆU", GREEN,
     "Bơm dữ liệu thử nghiệm từ Landing Zone lên OneLake Gold Zone. Kiểm tra đối soát số liệu khớp 100% với hệ thống gốc. Kích hoạt giám sát an ninh mạng SIEM 24/7.")
]
for i, (st_t, st_sub, col, desc) in enumerate(gd2_steps):
    y = Inches(1.5 + i * 1.35)
    shape(s15, Inches(0.8), y, Inches(11.7), Inches(1.2), WHITE, col, Pt(1.5), rounded=True)
    shape(s15, Inches(0.8), y, Inches(3.2), Inches(1.2), col, rounded=False)
    numbered_label(s15, Inches(1.0), y + Inches(0.4), i + 1, WHITE, Inches(0.4))
    text(s15, Inches(1.5), y + Inches(0.25), Inches(2.4), Inches(0.35), st_t, 10.5, True, WHITE)
    text(s15, Inches(1.5), y + Inches(0.65), Inches(2.4), Inches(0.3), st_sub, 8.5, True, RGBColor(254, 240, 138))
    text(s15, Inches(4.2), y + Inches(0.15), Inches(8.1), Inches(0.9), desc, 10.5, color=BLACK)

# =========================================================================
# SLIDE 16: KẾ HOẠCH GIAI ĐOẠN 3 (BÀN GIAO DASHBOARD & LÀM CHỦ 100%)
# =========================================================================
s16 = prs.slides.add_slide(BL)
header(s16, "GIAI ĐOẠN 3 CHI TIẾT: BÀN GIAO, KHAI THÁC DASHBOARD & ĐÀO TẠO CHUYỂN GIAO", "PHẦN D: KẾ HOẠCH HÀNH ĐỘNG — CHẶNG 3 (QUÝ 2/2027 TRỞ ĐI)", "14")

gd3_steps = [
    ("BƯỚC 1: XÂY DỰNG MÔ HÌNH NGỮ NGHĨA", "SEMANTIC MODEL & STAR SCHEMA", BLUE,
     "Tổ chức dữ liệu dạng bảng Fact/Dimension tối ưu. Định nghĩa các công thức đo lường KPI tài chính, tiến độ xưởng cơ khí, năng suất cẩu bãi Cảng PTSC Quảng Ngãi."),
    ("BƯỚC 2: XUẤT BẢN DASHBOARD POWER BI", "BÁO CÁO BAN GIÁM ĐỐC TRÊN MOBILE", TEAL,
     "Thiết kế Dashboard trực quan theo đúng yêu cầu điều hành của Giám đốc và các Phó Giám đốc. Cài đặt ứng dụng Power BI Mobile trên iPad/điện thoại cho các Sếp."),
    ("BƯỚC 3: ĐÀO TẠO & CHUYỂN GIAO MÃ NGUỒN", "IT QUẢNG NGÃI LÀM CHỦ 100%", GOLD,
     "Bàn giao toàn bộ tài liệu kiến trúc, mã nguồn luồng ETL. Đào tạo chuyên sâu cho đội ngũ IT Quảng Ngãi để tự quản trị, tự sửa đổi báo cáo mà không phụ thuộc bên ngoài."),
    ("BƯỚC 4: NGHIỆM THU & ĐƯA VÀO VẬN HÀNH CHÍNH THỨC", "GO-LIVE TOÀN DIỆN & BẢO HÀNH", GREEN,
     "Ký biên bản nghiệm thu đưa vào vận hành chính thức. Thiết lập cam kết SLA hỗ trợ kỹ thuật và bắt đầu chu kỳ tự động đồng bộ dữ liệu hợp nhất định kỳ về TCT.")
]
for i, (st_t, st_sub, col, desc) in enumerate(gd3_steps):
    y = Inches(1.5 + i * 1.35)
    shape(s16, Inches(0.8), y, Inches(11.7), Inches(1.2), WHITE, col, Pt(1.5), rounded=True)
    shape(s16, Inches(0.8), y, Inches(3.2), Inches(1.2), col, rounded=False)
    numbered_label(s16, Inches(1.0), y + Inches(0.4), i + 1, WHITE, Inches(0.4))
    text(s16, Inches(1.5), y + Inches(0.25), Inches(2.4), Inches(0.35), st_t, 10.5, True, WHITE)
    text(s16, Inches(1.5), y + Inches(0.65), Inches(2.4), Inches(0.3), st_sub, 8.5, True, RGBColor(254, 240, 138))
    text(s16, Inches(4.2), y + Inches(0.15), Inches(8.1), Inches(0.9), desc, 10.5, color=BLACK)

# =========================================================================
# SLIDE 17: TIMELINE TỔNG THỂ
# =========================================================================
s17 = prs.slides.add_slide(BL)
header(s17, "LỘ TRÌNH TRIỂN KHAI TỔNG THỂ: 3 CHẶNG VỀ ĐÍCH TRONG NĂM 2026–2027", "PHẦN D: KẾ HOẠCH HÀNH ĐỘNG — TIẾN ĐỘ THỰC HIỆN", "15")

phases = [
    ("CHẶNG 1: CHUẨN BỊ & KHẢO SÁT", "T9/2026 – T11/2026", "KHẢO SÁT, HỌP 3 BÊN VỚI TCT & SIZING", "NỘI BỘ QN TỰ CHỦ TRÌ (0 VNĐ)", BLUE, BLUE_SOFT,
     ["• Thành lập Tổ công tác Nền tảng Dữ liệu QN", "• Gửi email chốt mốc giãn tiến độ Mua sắm", "• Họp 3 bên trực tuyến với BDA TCT & HIPT-AITS", "• Hoàn thành khảo sát CSDL & ánh xạ Master Data"]),
    
    ("CHẶNG 2: KẾT NỐI & DỰNG SPOKE", "T12/2026 – T3/2027", "XÂY DỰNG TRỤC TÍCH HỢP & LANDING ZONE", "CẤP TENANT & CHẠY THỬ NGHIỆM", TEAL, RGBColor(230, 248, 246),
     ["• TCT bàn giao Workspace Tenant L3 trên Fabric", "• Thông tuyến mạng VPN IPSec bảo mật", "• Cài đặt Spoke Agent, xây dựng luồng ETL", "• Thử nghiệm cơ chế phê duyệt Landing Zone"]),
    
    ("CHẶNG 3: BÀN GIAO & KHAI THÁC", "T4/2027 – T6/2027", "XUẤT BẢN DASHBOARD & CHUYỂN GIAO", "IT QUẢNG NGÃI LÀM CHỦ 100%", GREEN, GREEN_SOFT,
     ["• Thiết kế Dashboard Power BI phục vụ Sếp QN", "• Cài app Power BI Mobile trên iPad Ban Giám đốc", "• Bàn giao 100% mã nguồn luồng dữ liệu", "• Nghiệm thu chính thức, hoàn thành KPI Chuyển đổi số"])
]
for i, (p_name, p_time, p_title, p_lead, col, bg_c, deliverables) in enumerate(phases):
    x = Inches(0.8 + i * 4.05)
    shape(s17, x, Inches(1.5), Inches(3.7), Inches(5.4), bg_c, col, Pt(1.5), rounded=True)
    shape(s17, x, Inches(1.5), Inches(3.7), Inches(0.7), col)
    text(s17, x, Inches(1.53), Inches(3.7), Inches(0.32), p_name, 10.5, True, WHITE, PP_ALIGN.CENTER)
    text(s17, x, Inches(1.85), Inches(3.7), Inches(0.3), p_time, 9.5, True, RGBColor(254, 240, 138), PP_ALIGN.CENTER)
    
    shape(s17, x + Inches(0.15), Inches(2.3), Inches(3.4), Inches(0.55), WHITE, GRAY_MED, Pt(0.5), rounded=True)
    text(s17, x + Inches(0.2), Inches(2.32), Inches(3.3), Inches(0.25), p_title, 9.5, True, col, PP_ALIGN.CENTER)
    text(s17, x + Inches(0.2), Inches(2.58), Inches(3.3), Inches(0.22), p_lead, 8.5, True, GRAY_DARK, PP_ALIGN.CENTER)
    
    for j, d in enumerate(deliverables):
        text(s17, x + Inches(0.15), Inches(3.05 + j * 0.55), Inches(3.4), Inches(0.5), d, 10, False, BLACK)
    
    shape(s17, x + Inches(0.15), Inches(5.3), Inches(3.4), Inches(1.45), WHITE, col, Pt(1.0), rounded=True)
    res_text = (
        "MỤC TIÊU CỐT LÕI:\nBảo vệ ngân sách, làm việc 3 bên với TCT, gài chuẩn ESB vào gói Mua sắm." if i == 0 else
        "MỤC TIÊU CỐT LÕI:\nThông tuyến VPN, nhận Tenant L3, dữ liệu chảy tự động vào Landing Zone." if i == 1 else
        "MỤC TIÊU CỐT LÕI:\nSếp xem Dashboard trên mobile hàng ngày, IT QN tự chủ vận hành 100%."
    )
    text(s17, x + Inches(0.25), Inches(5.4), Inches(3.2), Inches(1.25), res_text, 10, True, col)

# =========================================================================
# SLIDE 18: KIẾN NGHỊ & ĐỀ XUẤT BAN GIÁM ĐỐC
# =========================================================================
s18 = prs.slides.add_slide(BL)
header(s18, "KIẾN NGHỊ VÀ ĐỀ XUẤT XIN PHÊ DUYỆT CỦA BAN GIÁM ĐỐC", "PHẦN D: KẾ HOẠCH HÀNH ĐỘNG — ĐỀ XUẤT PHÊ DUYỆT", "16")

recs = [
    ("1. PHÊ DUYỆT CHỦ TRƯƠNG TẠM GIÃN TIẾN ĐỘ PHẦN MỀM MUA SẮM",
     "Đồng ý chủ trương tạm giãn tiến độ gói thầu Phần mềm Mua sắm (đến hết 31/10/2026) theo đúng văn bản khuyến nghị của BDA CĐS Tổng công ty (chị Phan Thị Ngọc Vân), nhằm rà soát và bổ sung tiêu chuẩn kết nối Trục tích hợp ESB vào HSMT, tránh đầu tư chồng chéo.",
     BLUE, BLUE_SOFT),
    
    ("2. CHO PHÉP GỬI EMAIL PHẢN HỒI CHÍNH THỨC & HỌP 3 BÊN VỚI TCT",
     "Cho phép Bộ phận CNTT gửi email phản hồi chính thức cho BDA TCT để: (1) Chốt mốc thời gian hỗ trợ; (2) Đăng ký Quảng Ngãi làm đơn vị thí điểm GĐ 2A; (3) Tổ chức ngay buổi họp trực tuyến 3 bên với BDA TCT và Liên danh tư vấn HIPT-AITS trong tuần tới.",
     TEAL, RGBColor(230, 248, 246)),
    
    ("3. KÝ QUYẾT ĐỊNH THÀNH LẬP TỔ CÔNG TÁC QUẢN TRỊ DỮ LIỆU",
     "Kính trình Giám đốc Công ty ký ban hành Quyết định thành lập Tổ Công tác Quản trị Dữ liệu PTSC Quảng Ngãi (đã có Dự thảo kẹp kèm). Phân công Lãnh đạo Đơn vị làm Data Owner Cấp 3; giao các phòng Kế toán, Cảng, Dự án, Mua sắm cử đầu mối phối hợp cùng IT.",
     GREEN, GREEN_SOFT)
]

for i, (title, desc, col, bg_c) in enumerate(recs):
    y = Inches(1.5 + i * 1.6)
    shape(s18, Inches(0.8), y, Inches(11.7), Inches(1.45), bg_c, col, Pt(2.0), rounded=True)
    shape(s18, Inches(0.8), y, Inches(0.12), Inches(1.45), col)
    numbered_label(s18, Inches(1.1), y + Inches(0.2), i + 1, col, Inches(0.38))
    text(s18, Inches(1.6), y + Inches(0.18), Inches(10.5), Inches(0.35), title, 12, True, col)
    text(s18, Inches(1.6), y + Inches(0.58), Inches(10.5), Inches(0.8), desc, 10.5, color=BLACK)

shape(s18, Inches(0.8), Inches(6.35), Inches(11.7), Inches(0.7), GOLD_SOFT, GOLD, Pt(1), rounded=True)
text(s18, Inches(1.0), Inches(6.42), Inches(11.3), Inches(0.55),
     "KÍNH TRÌNH BAN GIÁM ĐỐC XEM XÉT VÀ CHO Ý KIẾN CHỈ ĐẠO ĐỂ TỔ CÔNG TÁC KHẨN TRƯƠNG TRIỂN KHAI!",
     11.5, True, NAVY, PP_ALIGN.CENTER)

# LƯU FILE
output_path = "bao_cao_dataplatform_ptsc_qn_v8.pptx"
prs.save(output_path)
print(f"SUCCESS: Saved PowerPoint deck to {output_path} (Total slides: {len(prs.slides)})")
