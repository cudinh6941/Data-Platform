import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_table_borders(table, color="D0D5DD", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(f'''
            <w:tblBorders {nsdecls("w")}>
                <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
                <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
                <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
                <w:insideV w:val="none"/>
                <w:left w:val="none"/>
                <w:right w:val="none"/>
            </w:tblBorders>
        ''')
        tblPr[0].append(borders)

def format_row(row):
    trPr = row._element.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def create_callout_box(doc, text_content, title="LƯU Ý CHIẾN LƯỢC / CHỈ ĐẠO CỦA TCT", bg_hex="F0F4F8", border_color="003366"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Cm(16.5)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=160, bottom=160, left=220, right=220)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:top w:val="none"/>
            <w:right w:val="none"/>
            <w:bottom w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"📌 {title}\n")
    run_t.font.name = "Arial"
    run_t.font.size = Pt(10.5)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(0, 51, 102)
    
    run_c = p.add_run(text_content)
    run_c.font.name = "Arial"
    run_c.font.size = Pt(9.5)
    run_c.font.italic = True
    run_c.font.color.rgb = RGBColor(30, 41, 59)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

print("Starting document creation...")
doc = docx.Document()

# Page Setup: A4, Margins 2cm
sections = doc.sections
for s in sections:
    s.page_width = Cm(21.0)
    s.page_height = Cm(29.7)
    s.top_margin = Cm(2.0)
    s.bottom_margin = Cm(2.0)
    s.left_margin = Cm(2.5)
    s.right_margin = Cm(2.0)

# Set Normal style font
style = doc.styles['Normal']
style.font.name = 'Arial'
style.font.size = Pt(11)
style.font.color.rgb = RGBColor(33, 37, 41)
style.paragraph_format.line_spacing = 1.25
style.paragraph_format.space_after = Pt(4)

# ----------------- HEADER: QUỐC HIỆU / CƠ QUAN -----------------
tbl_header = doc.add_table(rows=1, cols=2)
tbl_header.alignment = WD_TABLE_ALIGNMENT.CENTER
cell_l, cell_r = tbl_header.rows[0].cells
cell_l.width = Cm(8.5)
cell_r.width = Cm(8.0)

p_l = cell_l.paragraphs[0]
p_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_l.paragraph_format.space_after = Pt(2)
r_l1 = p_l.add_run("TỔNG CÔNG TY CỔ PHẦN DỊCH VỤ\nKỸ THUẬT DẦU KHÍ VIỆT NAM\n")
r_l1.font.size = Pt(9.5)
r_l1.font.bold = True
r_l2 = p_l.add_run("CÔNG TY CỔ PHẦN DỊCH VỤ\nDẦU KHÍ QUẢNG NGÃI PTSC\n")
r_l2.font.size = Pt(10)
r_l2.font.bold = True
r_l2.font.color.rgb = RGBColor(0, 51, 102)
r_l3 = p_l.add_run("Số:       /BC-DKQN-TK&R&D")
r_l3.font.size = Pt(9.5)
r_l3.font.italic = True

p_r = cell_r.paragraphs[0]
p_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_r.paragraph_format.space_after = Pt(2)
r_r1 = p_r.add_run("CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM\n")
r_r1.font.size = Pt(10)
r_r1.font.bold = True
r_r2 = p_r.add_run("Độc lập – Tự do – Hạnh phúc\n")
r_r2.font.size = Pt(10)
r_r2.font.bold = True
r_r3 = p_r.add_run("-------------------\n")
r_r3.font.size = Pt(9)
r_r4 = p_r.add_run("Quảng Ngãi, ngày 11 tháng 09 năm 2026")
r_r4.font.size = Pt(9.5)
r_r4.font.italic = True

p_sep = doc.add_paragraph()
p_sep.paragraph_format.space_before = Pt(8)
p_sep.paragraph_format.space_after = Pt(6)

# ----------------- DOCUMENT TITLE -----------------
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(6)
p_title.paragraph_format.space_after = Pt(4)
r_t1 = p_title.add_run("BÁO CÁO\n")
r_t1.font.size = Pt(14)
r_t1.font.bold = True
r_t1.font.color.rgb = RGBColor(0, 51, 102)

r_t2 = p_title.add_run("V/v Nghiên cứu tài liệu Data Platform của Tổng công ty và Đề xuất phương án\nkiến trúc tích hợp hệ thống phần mềm tại PTSC Quảng Ngãi")
r_t2.font.size = Pt(13)
r_t2.font.bold = True
r_t2.font.color.rgb = RGBColor(0, 51, 102)

# ----------------- RECIPIENT (KÍNH GỬI) -----------------
p_kg = doc.add_paragraph()
p_kg.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_kg.paragraph_format.left_indent = Cm(1.5)
p_kg.paragraph_format.space_before = Pt(6)
p_kg.paragraph_format.space_after = Pt(12)
r_kg_lbl = p_kg.add_run("Kính gửi: \n")
r_kg_lbl.font.bold = True
r_kg_lbl.font.size = Pt(11)

recipients = [
    "Ban Chỉ đạo Chuyển đổi số Tổng công ty PTSC;",
    "Ban Nghiên cứu Phát triển & Chuyển đổi số (NCPT & CĐS) Tổng công ty PTSC;",
    "Ban Quản trị Dự án Giải pháp Nền tảng Dữ liệu (HDP26) Tổng công ty PTSC."
]
for rc in recipients:
    r_rc = p_kg.add_run(f"  - {rc}\n")
    r_rc.font.size = Pt(11)
    r_rc.font.bold = True

def add_heading_1(title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0, 51, 102)
    return p

def add_heading_2(title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(15, 76, 129)
    return p

def add_heading_3(title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.italic = True
    r.font.color.rgb = RGBColor(51, 51, 51)
    return p

# ----------------- PHẦN I -----------------
add_heading_1("PHẦN I: TIẾP THU Ý KIẾN CHỈ ĐẠO CỦA TỔNG CÔNG TY & BỐI CẢNH BÁO CÁO")

add_heading_2("1.1. Bối cảnh triển khai phần mềm nghiệp vụ tại PTSC Quảng Ngãi")
p = doc.add_paragraph(
    "Căn cứ Kế hoạch Chuyển đổi số năm 2026 của PTSC Quảng Ngãi (Công văn số 1153/DKQN-HCNS ngày 26/04/2026), "
    "nhằm số hóa quy trình quản trị sản xuất kinh doanh trong các lĩnh vực chế tạo cơ khí siêu trường siêu trọng, "
    "gia công kết cấu năng lượng tái tạo ngoài khơi và dịch vụ cảng biển Dung Quất, Công ty Cổ phần Dịch vụ Dầu khí Quảng Ngãi "
    "(PTSC Quảng Ngãi) đã chủ động xây dựng phương án triển khai 02 phần mềm nghiệp vụ trọng điểm trong năm 2026 bao gồm:\n"
    "1. Phần mềm Quản lý công tác An toàn - Sức khỏe - Môi trường (HSEQ);\n"
    "2. Phần mềm Quản lý Mua sắm hàng hóa và dịch vụ (Procurement Management System)."
)

add_heading_2("1.2. Ý kiến phản hồi và định hướng chỉ đạo của Ban Dự án CĐS Tổng công ty")
p = doc.add_paragraph(
    "Sau khi nhận được hồ sơ đề xuất và tài liệu khớp nối kỹ thuật của PTSC Quảng Ngãi, ngày 06/07/2026 và ngày 01/08/2026, "
    "Ban Dự án Chuyển đổi số Tổng công ty (đầu mối là Chuyên gia Quản trị Chiến lược Phan Thị Ngọc Vân) đã có văn bản trao đổi "
    "và kết luận chỉ đạo cụ thể như sau:\n"
    "• Đối với Phần mềm HSEQ: Giải pháp cơ bản đáp ứng định hướng tích hợp chung; PTSC Quảng Ngãi được phép tiếp tục triển khai theo kế hoạch.\n"
    "• Đối với Phần mềm Quản lý Mua sắm hàng hóa, dịch vụ: Ban Dự án CĐS TCT đã đưa ra cảnh báo kỹ thuật rất xác đáng:"
)

callout_van = (
    "\"Phương án hiện tại tập trung đáp ứng nhu cầu Quy trình nghiệp vụ với phạm vi tích hợp nội bộ giữa MESx – PMSx – FBO. "
    "Tuy nhiên, khi mở rộng kết nối với các hệ thống hiện hữu khác của PTSC Quảng Ngãi (eOffice, FAST, IRTECH, VTI…) và các nền tảng "
    "dùng chung của Tổng công ty trong tương lai, mô hình kết nối trực tiếp sẽ làm gia tăng đáng kể số lượng API, chi phí quản lý tích hợp, "
    "nhiều rủi ro về ATTT.\n\n"
    "Do đó, đề nghị PTSC Quảng Ngãi nghiên cứu lộ trình chuyển sang kiến trúc tích hợp tập trung thông qua Data Platform "
    "(ESB/API Gateway, MDM, Data Lakehouse…) để bảo đảm khả năng mở rộng, quản trị dữ liệu và kết nối đồng bộ với Tổng công ty...\n\n"
    "Kết luận: Đề nghị PTSC Quảng Ngãi tạm thời giãn tiến độ triển khai Phần mềm Quản lý mua sắm hàng hóa, dịch vụ để phối hợp cùng "
    "BDA CĐS Tổng công ty rà soát, thống nhất kiến trúc tích hợp tổng thể, bảo đảm đồng bộ với Data Platform và các nền tảng dùng chung "
    "của Tổng công ty, tránh phát sinh đầu tư chồng chéo và chi phí chuyển đổi trong giai đoạn sau.\""
)
create_callout_box(doc, callout_van, title="TRÍCH KẾT LUẬN CHỈ ĐẠO CỦA BDA CĐS TCT (EMAIL NGÀY 01/08/2026)")

add_heading_2("1.3. Tinh thần tiếp thu và kết quả nghiên cứu tài liệu của PTSC Quảng Ngãi")
p = doc.add_paragraph(
    "Quán triệt nghiêm túc chỉ đạo của Ban Dự án CĐS TCT và ý kiến chỉ đạo trực tiếp của Lãnh đạo Phòng Thiết kế & R&D PTSC Quảng Ngãi "
    "(anh Bùi Lực ngày 29/08/2026), Tổ CNTT & CĐS PTSC Quảng Ngãi đã tạm dừng toàn bộ các thủ tục mua sắm độc lập, "
    "chủ động nghiên cứu toàn diện bộ hồ sơ kỹ thuật tại thư mục 'Hồ sơ yêu cầu mua sắm' do Tổng công ty cung cấp, bao gồm:\n"
    "1. Quyết định và Kế hoạch khởi động dự án HDP26 giữa PTSC và Liên danh HiPT - AITS (Hợp đồng số 1-2026/PTSC-CDS/HĐ);\n"
    "2. Báo cáo đề xuất lựa chọn giải pháp Hybrid Data Platform (Multi-site, Multi-cloud) và Bộ 6 nguyên tắc vàng;\n"
    "3. Báo cáo phân tích - đề xuất kỹ thuật chi tiết 82 trang về 12 phân hệ chức năng, hồ dữ liệu Lakehouse 3 vùng và hạ tầng phần cứng;\n"
    "4. Tài liệu Hội thảo Data Platform ngày 10/08/2026 (Phiên sáng & Phiên chiều) về cơ chế chia sẻ dữ liệu 2 chiều và mô hình Hub-Spoke;\n"
    "5. Phụ lục hợp đồng về yêu cầu tích hợp kỹ thuật bắt buộc 13 tiêu chí (Biểu mẫu chuẩn PTSC-ADM-RG08-FM10).\n\n"
    "PTSC Quảng Ngãi xin báo cáo thực trạng hiện tại, phương án điều chỉnh thiết kế tích hợp và kế hoạch hợp tác triển khai chi tiết như sau:"
)

# ----------------- PHẦN II -----------------
add_heading_1("PHẦN II: KHÁI QUÁT NHẬN THỨC VỀ KIẾN TRÚC ENTERPRISE DATA PLATFORM TCT")

add_heading_2("2.1. Đánh giá về Mô hình Kiến trúc Hybrid Data Platform (Multi-site, Multi-cloud)")
p = doc.add_paragraph(
    "Qua nghiên cứu tài liệu kỹ thuật của TCT, PTSC Quảng Ngãi hoàn toàn đồng thuận với quyết định lựa chọn mô hình Hybrid Data Platform "
    "của Ban Chỉ đạo Tổng công ty. Việc kết hợp giữa hạ tầng On-premise Data Center tại Tòa nhà PetroVietnam Tower (đóng vai trò Core Datalakehouse "
    "lưu trữ dữ liệu nhạy cảm, khối lượng lớn, tối ưu hóa chi phí đường truyền và TCO) với hạ tầng Public Cloud (cho các dịch vụ co giãn linh hoạt, "
    "phân tích ngôn ngữ tự nhiên Text-to-Data / AI) là một chiến lược rất bài bản, cân bằng hoàn hảo giữa tính tự chủ công nghệ, tuân thủ nghiêm "
    "Nghị định 13/2023/NĐ-CP và bài toán ngân sách dài hạn."
)

add_heading_2("2.2. Nhận thức về vai trò 'xương sống' của Trục tích hợp (ESB / Kafka / API Gateway)")
p = doc.add_paragraph(
    "PTSC Quảng Ngãi nhận thức rõ: Nhược điểm lớn nhất của mô hình tích hợp trực tiếp Point-to-Point cũ giữa MESx – PMSx – FBO chính là việc "
    "tạo ra sự phụ thuộc chặt chẽ (tight coupling). Khi phát sinh thêm eOffice, FAST, IRTECH, VTI... việc duy trì hàng chục kết nối tay đôi độc lập "
    "sẽ dẫn tới 'bùng nổ API' theo cấp số nhân N*(N-1)/2, chi phí bảo trì khổng lồ và tiềm ẩn nguy cơ đứt gãy dữ liệu dây chuyền khi một hệ thống thay đổi cấu trúc bảng.\n\n"
    "Việc TCT trang bị Trục tích hợp ESB dựa trên nền tảng Apache Kafka và API Gateway sẽ đóng vai trò giải phóng các hệ thống khỏi sự phụ thuộc "
    "trực tiếp. Các hệ thống chỉ cần giao tiếp bất đồng bộ qua hàng đợi thông điệp (Message Queue), đảm bảo an toàn tuyệt đối và khả năng mở rộng vô hạn."
)

add_heading_2("2.3. Quản trị Dữ liệu Chủ (Master Data Management - MDM) - Nền tảng của mô hình ERP liên thông")
p = doc.add_paragraph(
    "Tài liệu kỹ thuật của TCT đã chỉ ra điểm nghẽn lớn nhất trong quản trị hiện nay là sự phân mảnh danh mục (Master Data) khi được quản lý "
    "bằng các file Excel rời rạc trên SharePoint. Việc TCT triển khai Phân hệ MDM nhằm tạo lập 'Bản ghi Vàng' (Golden Record) duy nhất cho "
    "Nhà cung cấp, Khách hàng, Vật tư và Dự án chính là điều kiện tiên quyết để quy trình Mua sắm của Quảng Ngãi liên thông mượt mà với phân hệ "
    "Kế toán - Tài chính và Quản lý Kho của FAST."
)

add_heading_2("2.4. Định vị của PTSC Quảng Ngãi trong Mô hình Hub-and-Spoke")
p = doc.add_paragraph(
    "Căn cứ tiêu chí phân nhóm 17 Đơn vị Thành viên của TCT, PTSC Quảng Ngãi được định vị thuộc nhóm Spoke Level 3:\n"
    "• Đặc điểm: Đơn vị sản xuất cơ khí và cảng biển quy mô lớn, có hệ thống phần mềm nghiệp vụ chuyên thù (FAST, Nhân sự, Cảng, Dự án);\n"
    "• Lộ trình nâng cấp lên Spoke Level 2 (Có Hồ dữ liệu nội bộ tại chỗ): Do đặc thù khối lượng dữ liệu gia công cơ khí, nhật ký máy móc và cân xe cảng rất lớn, "
    "Quảng Ngãi cần một Hồ dữ liệu nội bộ (Local Lakehouse) tại chỗ để tự chủ điều hành tác chiến tức thì, không làm nghẽn đường truyền mạng VPN về Hub TCT."
)

# ----------------- PHẦN III -----------------
add_heading_1("PHẦN III: THỰC TRẠNG HỆ THỐNG VÀ PHƯƠNG ÁN ĐIỀU CHỈNH THIẾT KẾ TÍCH HỢP TẠI PTSC QUẢNG NGÃI")

add_heading_2("3.1. Thực trạng hiện tại của hệ sinh thái CNTT tại PTSC Quảng Ngãi (As-Is: Chưa tích hợp tập trung)")
p = doc.add_paragraph(
    "PTSC Quảng Ngãi xin báo cáo trung thực bức tranh hiện trạng hệ thống CNTT tại đơn vị tính đến tháng 9/2026:\n"
    "1. Tình trạng phân mảnh, ốc đảo dữ liệu (Data Silos):\n"
    "   - Toàn bộ các phần mềm hiện hữu đều chạy độc lập, dữ liệu nhập liệu thủ công lặp lại và chưa có trục tích hợp nào kết nối chúng với nhau.\n"
    "   - Kế toán - Tài chính - Kho: Sử dụng FAST Accounting (CSDL SQL Server), số liệu kho và công nợ chưa liên thông với mua sắm.\n"
    "   - Văn phòng số: Sử dụng e-Office (BTEC) cho luồng công văn, chưa tích hợp ký số tự động cho quy trình mua sắm hay hợp đồng.\n"
    "   - Quản lý Cảng: Sử dụng phần mềm IRTECH theo dõi cầu cảng, kho bãi Dung Quất và cân xe độc lập.\n"
    "   - Quản lý Tài sản: Sử dụng phần mềm VTI theo dõi cẩu trục, xe cơ giới độc lập.\n"
    "2. Thực trạng Phần mềm HSEQ: Đang trong giai đoạn thuê đối tác phát triển các phân hệ nghiệp vụ an toàn nội bộ (sự cố, đánh giá rủi ro, cấp phép PTW), "
    "chưa hề kết nối hay tích hợp với bất kỳ nền tảng tập trung nào.\n"
    "3. Thực trạng Phần mềm Quản lý Mua sắm: Đang dừng lại ở hồ sơ thiết kế tích hợp trực tiếp nối dây tay đôi giữa MESx – PMSx – FBO. "
    "PTSC Quảng Ngãi đã nghiêm túc dừng toàn bộ tiến độ mua sắm theo đúng chỉ đạo của Ban Dự án TCT để tái cấu trúc lại phương án."
)

add_heading_2("3.2. Phương án Kiến trúc Tích hợp Tập trung Đề xuất Điều chỉnh (To-Be)")
p = doc.add_paragraph(
    "Tiếp thu trọn vẹn chỉ đạo của TCT, PTSC Quảng Ngãi đề xuất phương án kiến trúc mới, xóa bỏ hoàn toàn kết nối tay đôi, "
    "tổ chức lại hệ sinh thái CNTT của Công ty xoay quanh Hồ dữ liệu nội bộ (Local Data Lakehouse / ODS) và Trạm tích hợp Spoke Level 3:"
)

callout_arch = (
    "SƠ ĐỒ NGUYÊN LÝ KIẾN TRÚC MỚI ĐỀ XUẤT (TO-BE):\n\n"
    "[1. HỆ SINH THÁI ỨNG DỤNG NGHIỆP VỤ NỘI BỘ QUẢNG NGÃI]\n"
    "   • Phần mềm Quản lý Mua sắm (Xây mới chuẩn RESTful API)\n"
    "   • Phần mềm Kế toán - Kho FAST (Hiện hữu, mở CSDL Read-only an toàn)\n"
    "   • Phần mềm e-Office Ký số BTEC (Hiện hữu, tích hợp API ký duyệt)\n"
    "   • Phần mềm HSEQ (Đang xây dựng, tích hợp luồng sự cố & an toàn)\n"
    "   • Phần mềm Quản lý Cảng Dung Quất IRTECH & Quản lý Tài sản VTI\n\n"
    "           │ (Giao thức chuẩn RESTful API / Message Queue)\n"
    "           ▼\n"
    "[2. HỒ DỮ LIỆU NỘI BỘ & TRẠM TÍCH HỢP SPOKE QUẢNG NGÃI]\n"
    "   • Hồ dữ liệu nội bộ (Local Data Lakehouse / ODS):\n"
    "       - Lưu trữ dữ liệu vận hành chi tiết mảng Cơ khí, Cảng, Mua sắm, Kho, HSEQ.\n"
    "       - Cung cấp Dashboard điều hành nội bộ tức thời cho BGĐ PTSC Quảng Ngãi.\n"
    "       - Hoạt động độc lập trong mạng LAN, không bị gián đoạn khi mạng VPN chập chờn.\n"
    "   • Trạm tích hợp Spoke Gateway:\n"
    "       - API Gateway & Reverse Proxy (Xác thực Token, bảo mật kênh truyền).\n"
    "       - Kafka Connector / Data Sync Agent (Lọc dữ liệu đẩy lên Hub TCT).\n"
    "       - Bộ lọc Data Quality & Bảng cách ly lỗi (Quarantine table).\n\n"
    "           │ (Kênh truyền bảo mật chuyên dụng IPSec VPN Site-to-Site)\n"
    "           ▼\n"
    "[3. HUB DATA PLATFORM TỔNG CÔNG TY PTSC]\n"
    "   • Trục tích hợp ESB / API Gateway tập trung\n"
    "   • Phân hệ Dữ liệu Chủ MDM (Bơm danh mục chuẩn Golden Record về ĐVTV)\n"
    "   • Hồ dữ liệu Enterprise Lakehouse 3 phân vùng (Bronze - Silver - Gold)\n"
    "   • Trung tâm Vận hành Điều hành Dữ liệu DOC (Phục vụ Lãnh đạo TCT & ĐVTV)"
)
create_callout_box(doc, callout_arch, title="MÔ HÌNH KIẾN TRÚC TÍCH HỢP MỚI ĐỀ XUẤT CỦA PTSC QUẢNG NGÃI", bg_hex="F8FAFC", border_color="0EA5E9")

add_heading_2("3.3. Thiết kế luồng nghiệp vụ Mua sắm - Kế toán - Ký số theo định hướng ERP dùng chung")
p = doc.add_paragraph(
    "Nhằm đáp ứng yêu cầu cốt lõi của TCT: 'Dữ liệu chỉ được nhập một lần trên một hệ thống, các bước nghiệp vụ được cập nhật tự động "
    "giữa các phần mềm, hạn chế nhập liệu lặp lại và đảm bảo tính nhất quán của dữ liệu', quy trình Mua sắm mới sẽ được thiết kế lại như sau:\n\n"
    "1. Khởi tạo Yêu cầu Mua sắm (PR) và lấy Dữ liệu Chủ (MDM):\n"
    "   - Cán bộ tạo PR/PO trên Phần mềm Mua sắm chỉ được chọn Nhà cung cấp, Nhóm vật tư từ danh mục chuẩn do MDM của TCT đồng bộ về. "
    "Tuyệt đối không tự do gõ tay mã nhà cung cấp hoặc mã vật tư mới.\n\n"
    "2. Ký số và Phê duyệt tập trung trên e-Office (BTEC):\n"
    "   - Hồ sơ Yêu cầu báo giá (RFQ), Bảng tổng hợp so sánh giá, Đơn đặt hàng (PO) và Hợp đồng sau khi lập trên Phần mềm Mua sắm sẽ tự động "
    "đẩy sang e-Office thông qua API.\n"
    "   - Lãnh đạo các cấp duyệt và ký số trực tiếp trên e-Office. Trạng thái phê duyệt và file hợp đồng đã ký số tự động trả ngược về Phần mềm Mua sắm.\n\n"
    "3. Tự động đồng bộ sang FAST Kế toán - Kho (Xóa bỏ nhập liệu thủ công):\n"
    "   - Khi hàng hóa về cảng/kho và biên bản nghiệm thu được ký xác nhận trên Phần mềm Mua sắm, hệ thống tự động đẩy dữ liệu sang FAST qua API.\n"
    "   - FAST tự động sinh Phiếu nhập kho, ghi nhận công nợ Nhà cung cấp theo đúng số PO và số Hợp đồng. Nhân viên kế toán không phải nhập lại.\n\n"
    "4. Tự động đồng bộ Quản trị Tài sản (VTI):\n"
    "   - Với các vật tư, thiết bị mua sắm thuộc diện tài sản cố định/công cụ dụng cụ (cẩu, xe chuyên dụng, máy móc gia công), dữ liệu tự động đồng bộ "
    "sang phần mềm VTI để phục vụ theo dõi khấu hao, bảo dưỡng định kỳ."
)

add_heading_2("3.4. Cam kết tuân thủ 13 Tiêu chí Kỹ thuật Tích hợp của TCT (Biểu mẫu PTSC-ADM-RG08-FM10)")
p = doc.add_paragraph(
    "PTSC Quảng Ngãi đưa toàn bộ 13 tiêu chí bắt buộc trong Phụ lục hợp đồng của TCT vào tiêu chuẩn thiết kế hệ thống mới:"
)

# Table 13 criteria
tbl_crit = doc.add_table(rows=14, cols=3)
tbl_crit.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(tbl_crit)

headers = ["Tiêu Chí Kỹ Thuật", "Yêu Cầu Chuẩn Của TCT", "Giải Pháp Triển Khai Tại PTSC Quảng Ngãi"]
col_widths = [Cm(3.8), Cm(6.2), Cm(6.5)]

hdr_cells = tbl_crit.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].width = col_widths[i]
    set_cell_background(hdr_cells[i], "003366")
    set_cell_margins(hdr_cells[i], top=140, bottom=140, left=140, right=140)
    p = hdr_cells[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

crit_data = [
    ("1. Giao tiếp & Cơ chế trích xuất", "Hỗ trợ API chuẩn (RESTful/Kafka) hoặc trích xuất CSDL trực tiếp (CDC/Read-only Replica).", "Phần mềm Mua sắm xây mới 100% chuẩn RESTful API. FAST hiện hữu cấp tài khoản CSDL Read-only an toàn để Agent trích xuất."),
    ("2. Tần suất & Tải hệ thống", "Phù hợp nghiệp vụ, không làm nghẽn giao dịch online của người dùng.", "Thiết lập lịch trích xuất mẻ nặng vào ban đêm (00:00 - 04:00). Các giao dịch duyệt PO/PR truyền theo thời gian thực tải nhẹ."),
    ("3. Trích xuất thay đổi (CDC)", "Có cột dấu vết thời gian (created_at, updated_at) hoặc cờ xóa mềm (is_deleted).", "Toàn bộ bảng dữ liệu Mua sắm bắt buộc có trường updated_at. Đội kỹ thuật chỉ cần lọc WHERE updated_at >= YESTERDAY là trích xuất chính xác."),
    ("4. Khóa chính & MDM", "Khóa chính cố định; đồng bộ định danh với Master Data của TCT.", "Khóa chính sinh tự động (UUID/Identity). Mọi mã Nhà cung cấp, Vật tư, Dự án đều map trực tiếp với mã MDM TCT."),
    ("5. Bảo mật & IAM/SSO", "Hỗ trợ OAuth2.0, OpenID Connect, mTLS; tích hợp IAM Keycloak/LDAP.", "Áp dụng xác thực Token OAuth2.0/JWT. Sẵn sàng tích hợp hệ thống xác thực người dùng Active Directory với Keycloak TCT."),
    ("6. Metadata & ERD", "Cung cấp ERD logic/physical, Data Dictionary và bảng ánh xạ trường dữ liệu.", "Bắt buộc Vendor bàn giao đầy đủ ERD và Từ điển dữ liệu bằng tiếng Việt trước khi nghiệm thu từng phân hệ."),
    ("7. Hiệu năng & Bản quyền mở", "Không giới hạn kết nối bởi license; không phụ phí API; cam kết mở rộng.", "Ghi rõ trong điều khoản hợp đồng: Không thu phụ phí bản quyền kết nối API, không áp đặt hạn mức (rate limit) bất hợp lý."),
    ("8. Idempotency & Truy vết", "Gửi lại nhiều lần không sinh trùng dữ liệu; hỗ trợ traceId / correlationId.", "Áp dụng cơ chế Upsert semantics và gắn mã traceId cho từng giao dịch mua sắm để truy vết lỗi xuyên mạng."),
    ("9. Môi trường DEV/UAT", "Cung cấp môi trường Sandbox/UAT giống hệt Production để test tích hợp.", "Thiết lập môi trường UAT độc lập trên hạ tầng máy chủ ảo hóa nội bộ; cung cấp bộ dữ liệu mẫu để test 2 chiều với TCT."),
    ("10. Chống Vendor Lock-in", "Khách hàng nắm toàn quyền cấu hình, không phụ thuộc độc quyền vào Vendor.", "PTSC Quảng Ngãi làm chủ cấu hình interface và CSDL; nhà thầu phải bàn giao tài liệu kỹ thuật hoàn chỉnh."),
    ("11. Chất lượng dữ liệu", "Có quy tắc Data Quality; có bảng cách ly bản ghi lỗi (Quarantine table).", "Thiết lập bộ lọc kiểm tra dữ liệu trước khi đẩy đi; các bản ghi lỗi format/null được đưa vào bảng tạm để xử lý riêng."),
    ("12. Giám sát & Vận hành", "Có dashboard giám sát lưu lượng, cảnh báo độ trễ và Runbook ứng cứu sự cố.", "Cung cấp giao diện theo dõi trạng thái đồng bộ API, ghi nhật ký kiểm toán (Audit Logs) tập trung."),
    ("13. Quản lý phiên bản Schema", "API có versioning (/v1, /v2), tương thích ngược và thông báo trước thay đổi.", "Mọi thay đổi API/Schema phải thông báo trước tối thiểu 30 ngày và duy trì phiên bản cũ chạy song song.")
]

for row_idx, (col1, col2, col3) in enumerate(crit_data):
    row = tbl_crit.rows[row_idx + 1]
    format_row(row)
    bg = "F9FAFB" if row_idx % 2 == 1 else "FFFFFF"
    for c_idx, val in enumerate([col1, col2, col3]):
        cell = row.cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_background(cell, bg)
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(8.5)
        if c_idx == 0:
            r.font.bold = True

p_space = doc.add_paragraph()
p_space.paragraph_format.space_before = Pt(4)

# ----------------- PHẦN IV -----------------
add_heading_1("PHẦN IV: KẾ HOẠCH HÀNH ĐỘNG TRIỂN KHAI TẠI PTSC QUẢNG NGÃI (3 GIAI ĐOẠN)")
p = doc.add_paragraph(
    "Để vừa giải quyết bài toán cấp bách nội bộ, vừa đồng bộ với thời điểm golive Hệ thống Core Data Platform của TCT (dự kiến tháng 8/2026), "
    "PTSC Quảng Ngãi xây dựng lộ trình hành động 3 giai đoạn chặt chẽ:"
)

add_heading_2("Giai đoạn 1: Khảo sát Hiện trạng, Chuẩn hóa Hồ sơ & Chuẩn bị Dự án (Tháng 3 - Tháng 5/2026)")
p = doc.add_paragraph(
    "• Thành lập Tổ công tác Data Platform PTSC Quảng Ngãi: Phân vai cụ thể theo mô hình 5 Cấp độ của TCT "
    "(Data Owner: Lãnh đạo Công ty; Data Stewards: Trưởng/Phó phòng Kế toán, Nhân sự, Dự án, Cảng; Data Custodian: Cán bộ CNTT);\n"
    "• Rà soát danh mục các phần mềm nghiệp vụ hiện hữu (FAST, e-Office, IRTECH, HSEQ); chuẩn bị văn bản hành chính gửi các nhà cung cấp "
    "phần mềm yêu cầu phối hợp kỹ thuật theo Phụ lục PTSC-ADM-RG08-FM10 (Lưu ý: Mô hình ERD và Data Dictionary yêu cầu ở đây thuần túy là "
    "cấu trúc CSDL các bảng dữ liệu nghiệp vụ - Data Schema, tuyệt đối không can thiệp hay yêu cầu bàn giao mã nguồn phần mềm - Source Code của Vendor);\n"
    "• Hoàn thiện lại Hồ sơ yêu cầu kỹ thuật Phần mềm Mua sắm theo kiến trúc Tích hợp Tập trung, đính kèm Phụ lục 13 tiêu chí kỹ thuật;\n"
    "• Báo cáo Ban Giám đốc Công ty và trình Ban Dự án CĐS TCT phê duyệt phương án điều chỉnh."
)

add_heading_2("Giai đoạn 2: Ký Hợp đồng với HiPT-AITS, Xây dựng Hồ Dữ Liệu Nội Bộ & Tích hợp Thí điểm (Tháng 5 - Tháng 8/2026)")
p = doc.add_paragraph(
    "• Ký hợp đồng dịch vụ kỹ thuật triển khai trọn gói từ A-Z với Liên danh HiPT - AITS:\n"
    "   - Khảo sát & Bóc tách CSDL chuyên sâu: Chuyên gia Data Architect của HiPT - AITS trực tiếp chủ trì làm việc kỹ thuật chuyên sâu "
    "với các nhà cung cấp phần mềm hiện hữu (kỹ sư FAST, BTEC, IRTECH...) để bóc tách cấu trúc CSDL (Data ERD), biên soạn Từ điển dữ liệu "
    "(Data Dictionary) và thiết lập Bảng ánh xạ dữ liệu (Data Mapping Matrix) khớp 1-1 với chuẩn TCT. (Tổ CNTT&CĐS Quảng Ngãi chủ trì, điều phối và nghiệm thu);\n"
    "   - Cài đặt và cấu hình Hồ dữ liệu nội bộ (Local Data Lakehouse / ODS) trên hạ tầng máy chủ ảo hóa sẵn có tại phòng Server Quảng Ngãi;\n"
    "   - Xây dựng các luồng Data Pipelines tự động hút dữ liệu từ FAST, Phần mềm Mua sắm mới, HSEQ và Cảng IRTECH về Hồ nội bộ;\n"
    "   - Thiết kế và triển khai hệ thống Dashboard báo cáo quản trị tác nghiệp phục vụ Ban Giám đốc và các Phòng ban Quảng Ngãi (chạy nội bộ LAN);\n"
    "• Kết nối Thử nghiệm với TCT:\n"
    "   - Phối hợp Phòng CNTT TCT thiết lập đường hầm bảo mật IPSec VPN Site-to-Site giữa Quảng Ngãi và Tòa nhà PetroVietnam Tower;\n"
    "   - Cài đặt Spoke Gateway Agent và tiến hành kiểm thử UAT luồng đồng bộ dữ liệu hai chiều với Hub TCT."
)

add_heading_2("Giai đoạn 3: Golive Toàn diện, Khai thác Báo cáo DOC & Mở rộng (Sau Tháng 8/2026)")
p = doc.add_paragraph(
    "• Đưa Phần mềm Quản lý Mua sắm và Hồ dữ liệu nội bộ vào vận hành sản xuất chính thức;\n"
    "• Tự động bơm dữ liệu giao dịch sạch từ Hồ nội bộ về phân vùng Tenant của Quảng Ngãi trên Hub TCT; tiếp nhận Master Data từ TCT;\n"
    "• Phối hợp với TCT đưa các chỉ số KPI trọng yếu của Quảng Ngãi lên Trung tâm Điều hành Dữ liệu DOC Tổng công ty."
)

# ----------------- PHẦN V -----------------
add_heading_1("PHẦN V: ĐỀ XUẤT CHỦ TRƯƠNG, KIẾN NGHỊ & KẾ HOẠCH HỢP TÁC VỚI LIÊN DANH HIPT - AITS")
p = doc.add_paragraph(
    "Để đảm bảo việc triển khai tại PTSC Quảng Ngãi đạt hiệu quả cao nhất, đúng pháp lý, không phát sinh chi phí đập đi xây lại "
    "và hoàn toàn tương thích với hệ thống của TCT, PTSC Quảng Ngãi kính đề xuất Ban Chỉ đạo và Ban Dự án CĐS TCT xem xét chỉ đạo các nội dung sau:"
)

add_heading_2("5.1. Chấp thuận cho phép tiếp tục triển khai Phần mềm Quản lý Mua sắm")
p = doc.add_paragraph(
    "Kính đề nghị Ban Dự án CĐS và Ban NCPT Tổng công ty xem xét chấp thuận phương án kiến trúc tích hợp tập trung đã được điều chỉnh tại Báo cáo này, "
    "chính thức cho phép PTSC Quảng Ngãi tiếp tục triển khai các thủ tục lựa chọn đối tác phát triển Phần mềm Quản lý Mua sắm hàng hóa, dịch vụ."
)

add_heading_2("5.2. Đề xuất Chủ trương Ký Hợp đồng Triển khai Trọn gói từ A-Z với Liên danh HiPT - AITS")
p = doc.add_paragraph(
    "PTSC Quảng Ngãi nhận thức sâu sắc rằng: Hợp đồng của TCT với Liên danh HiPT - AITS chỉ bao gồm phạm vi Cơ quan TCT; phần hạ tầng và tích hợp "
    "tại đơn vị thành viên do đơn vị tự chủ ngân sách. Nếu Quảng Ngãi tự làm hoặc thuê một đơn vị thứ ba bên ngoài để xây dựng Hồ dữ liệu nội bộ, rủi ro không tương thích "
    "về công nghệ, schema và bảo mật với Hub TCT là rất lớn.\n\n"
    "Do đó, PTSC Quảng Ngãi kính đề xuất Ban Chỉ đạo CĐS TCT ủng hộ chủ trương để PTSC Quảng Ngãi ký hợp đồng dịch vụ kỹ thuật trực tiếp với chính "
    "Liên danh HiPT - AITS (Tổng thầu gói HDP26 của TCT) để thực hiện trọn gói từ A-Z các hạng mục tại Quảng Ngãi:\n"
    "1. Thiết kế chi tiết & Cài đặt Hồ dữ liệu nội bộ (Local Data Lakehouse / ODS) tương thích hoàn toàn với nền tảng TCT;\n"
    "2. Chủ trì làm việc kỹ thuật với các Vendor phần mềm nội bộ: Chuyên gia của HiPT - AITS trực tiếp làm việc với FAST, BTEC (eOffice), IRTECH "
    "để bóc tách mô hình CSDL (Data ERD), lập Data Dictionary và cấu hình các đường ống hút dữ liệu tự động (CDC / Batch API);\n"
    "3. Xây dựng Data Pipelines tích hợp toàn diện từ FAST, Phần mềm Mua sắm mới, HSEQ và Cảng IRTECH về Hồ dữ liệu nội bộ;\n"
    "4. Xây dựng hệ thống Báo cáo Quản trị Nội bộ (Dashboards) phục vụ Ban Giám đốc và các phòng chức năng PTSC Quảng Ngãi;\n"
    "5. Thiết lập kênh đồng bộ hai chiều an toàn với Hub TCT và tiếp nhận Master Data;\n"
    "6. Đào tạo chuyển giao công nghệ & Bảo hành, bảo trì trọn gói."
)

add_heading_2("5.3. Kế hoạch Làm việc 3 Bên và Kiến nghị TCT hỗ trợ")
p = doc.add_paragraph(
    "1. Đăng ký buổi làm việc 3 bên: Kính đề nghị Ban Dự án CĐS TCT chủ trì một buổi làm việc kỹ thuật giữa BDA CĐS TCT – Liên danh HiPT-AITS – PTSC Quảng Ngãi "
    "(trực tuyến hoặc tại VP TCT) để bàn giao tài liệu đặc tả interface chuẩn và thống nhất phạm vi công việc (SOW) khảo sát tại Quảng Ngãi;\n"
    "2. Hỗ trợ chính sách chi phí ưu đãi: Kính đề nghị TCT có ý kiến định hướng với Liên danh HiPT - AITS áp dụng khung đơn giá dịch vụ ưu đãi cho PTSC Quảng Ngãi "
    "(kế thừa nền tảng công nghệ đã phát triển ở gói thầu TCT), giúp đơn vị tối ưu hóa chi phí đầu tư;\n"
    "3. Về Bản quyền & Mạng: Đề nghị Phòng CNTT TCT (anh Nguyễn Văn Minh) cấp dải IP quy hoạch cho Tenant Quảng Ngãi, hướng dẫn cấu hình VPN IPSec "
    "và làm rõ cơ chế phân bổ bản quyền Power BI dùng chung;\n"
    "4. Về cơ chế làm việc và đàm phán với các Nhà cung cấp phần mềm:\n"
    "       - Đối với các nhà cung cấp phần mềm dùng chung phổ biến trong toàn Tổng công ty (đặc biệt là FAST, BTEC e-Office): "
    "Kính đề nghị Ban Dự án CĐS TCT chủ trì làm việc ở cấp Tập đoàn để thống nhất Thỏa thuận khung (Framework Agreement / MOU) "
    "về quy chuẩn tích hợp và chính sách chi phí hỗ trợ kỹ thuật chuẩn hóa, tạo cơ sở pháp lý và kinh tế thuận lợi để các Đơn vị Thành viên "
    "(như PTSC Quảng Ngãi) làm việc với các chi nhánh đối tác, tránh tình trạng từng đơn vị bị ép giá dịch vụ riêng lẻ;\n"
    "       - Đối với các phần mềm nghiệp vụ nội bộ đặc thù của Quảng Ngãi (như IRTECH Cảng Dung Quất, VTI Quản lý tài sản, HSEQ): "
    "PTSC Quảng Ngãi với tư cách Chủ đầu tư (Bên A trong hợp đồng) sẽ trực tiếp chủ trì đàm phán, làm việc với các nhà cung cấp; "
    "đề nghị TCT phê duyệt áp dụng chính thức Phụ lục PTSC-ADM-RG08-FM10 làm căn cứ pháp lý bắt buộc để Quảng Ngãi yêu cầu các đối tác này "
    "phối hợp kỹ thuật với Tổng thầu Liên danh HiPT - AITS bóc tách CSDL phục vụ tích hợp."
)

# ----------------- KẾT LUẬN & CHỮ KÝ -----------------
add_heading_1("KẾT LUẬN")
p = doc.add_paragraph(
    "PTSC Quảng Ngãi cam kết chủ động nguồn lực, tuân thủ tuyệt đối chuẩn mực kỹ thuật của Tổng công ty và quyết tâm trở thành Đơn vị Thành viên "
    "kiểu mẫu đi đầu trong toàn hệ thống PTSC về chuyển đổi số và khai thác nền tảng dữ liệu.\n\n"
    "Kính mong Ban Lãnh đạo Tổng công ty, Ban NCPT & CĐS và Ban Dự án Data Platform TCT sớm xem xét, chấp thuận các đề xuất trên để PTSC Quảng Ngãi "
    "kịp thời triển khai các bước tiếp theo đúng tiến độ chung. PTSC Quảng Ngãi trân trọng cảm ơn sự quan tâm, chỉ đạo của Lãnh đạo Tổng công ty và Ban Dự án TCT./."
)

p_sign_sep = doc.add_paragraph()
p_sign_sep.paragraph_format.space_before = Pt(8)

# Table Signatures
tbl_sign = doc.add_table(rows=1, cols=2)
tbl_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
cell_s_l, cell_s_r = tbl_sign.rows[0].cells
cell_s_l.width = Cm(8.5)
cell_s_r.width = Cm(8.0)

p_sl = cell_s_l.paragraphs[0]
p_sl.paragraph_format.space_after = Pt(2)
r = p_sl.add_run("Nơi nhận:\n")
r.font.size = Pt(9.5)
r.font.bold = True
r.font.italic = True
recipients_sub = [
    "Như trên;",
    "Ban Giám đốc Công ty (để b/c);",
    "Phòng TCKT, HCNS, ĐHDA (để p/h);",
    "Lưu: VT, TK&R&D."
]
for rs in recipients_sub:
    r_sub = p_sl.add_run(f"- {rs}\n")
    r_sub.font.size = Pt(9)
    r_sub.font.italic = True

p_sr = cell_s_r.paragraphs[0]
p_sr.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sr.paragraph_format.space_after = Pt(2)

r_s1 = p_sr.add_run("TM. TỔ CÔNG TÁC CNTT & CĐS\n")
r_s1.font.size = Pt(10)
r_s1.font.bold = True
r_s2 = p_sr.add_run("Tổ trưởng\n\n\n\n\n")
r_s2.font.size = Pt(9.5)
r_s2.font.italic = True
r_s3 = p_sr.add_run("ĐOÀN HÙNG HUÂN\n\n")
r_s3.font.size = Pt(10)
r_s3.font.bold = True

r_s4 = p_sr.add_run("XÁC NHẬN CỦA LÃNH ĐẠO PHÒNG THIẾT KẾ & R&D\n")
r_s4.font.size = Pt(10)
r_s4.font.bold = True
r_s5 = p_sr.add_run("Trưởng phòng\n\n\n\n\n")
r_s5.font.size = Pt(9.5)
r_s5.font.italic = True
r_s6 = p_sr.add_run("BÙI LỰC")
r_s6.font.size = Pt(10)
r_s6.font.bold = True

try:
    output_path = r"d:\Data-Platform\bao_cao_phuong_an_tich_hop_data_platform_qn.docx"
    doc.save(output_path)
    print(f"Successfully saved Word document to: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")
except PermissionError:
    output_path = r"d:\Data-Platform\bao_cao_phuong_an_tich_hop_data_platform_qn_v2.docx"
    doc.save(output_path)
    print(f"Original file was open in Word. Saved updated version to: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")
