# BÁO CÁO PHÂN TÍCH TÀI LIỆU TỔNG CÔNG TY PTSC

## Level & Phân loại Đơn vị (L1, L2, L3, L4, Hub-Spoke)
Tìm thấy 32 trang liên quan.

### Mục 1
```
--- Trang 19 [Từ khóa: quy chế, quản trị dữ liệu, đơn vị thành viên] ---
01 · BỐI CẢNH
VÌ SAO CẦN KHUNG QUẢN TRỊ DỮ LIỆU
Vì sao PTSC cần Khung quản trị dữ liệu
● Hiện trạng: dữ liệu nằm phân tán trong từng hệ thống nghiệp vụ, thiếu
chuẩn chung giữa các đơn vị, báo cáo còn phụ thuộc tổng hợp thủ công
● Petrovietnam vừa ban hành hệ thống văn bản mới: Quy chế Quản trị
dữ liệu và 04 Quy định hướng dẫn (danh mục và siêu dữ liệu; chất
lượng và làm sạch; chia sẻ và chuyển giao; kiểm soát truy cập và
đánh giá nội bộ)
● PTSC là đơn vị thành viên, bắt buộc tuân thủ và đồng bộ toàn bộ hệ thống
văn bản này
● Nghĩa vụ pháp lý mới: Luật Dữ liệu, Luật Chuyển đổi số, Luật Bảo vệ dữ
liệu cá nhân, Luật An ninh mạng, Khung kiến trúc dữ liệu quốc gia
MỤC TIÊU
Quản lý dữ liệu như tài sản chiến lược
Theo nguyên tắc
Đúng · Đủ · Sạch · Sống · Thống nhất ·
Dùng chung
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 15
```

### Mục 2
```
--- Trang 35 [Từ khóa: fabric, onelake, hybrid, đơn vị thành viên] ---
011. NỀN TẢNG ĐÃ CÓ TỪ GIAI ĐOẠN 1
PHẠM VI
Văn phòng Tổng công ty PTSC
BỘ TIÊU CHUẨN
Kiến trúc dữ liệu, kiến trúc – quản trị Master Data, tiêu
chuẩn tích hợp toàn hệ sinh thái CNTT
NỀN TẢNG Dữ LIỆU HYBRID — IMIP DATA PLATFORM
CLOUD
Microsoft Fabric / OneLake (20TB), Purview, 70 người
dùng
⌂ ON-PREM
Thu thập dữ liệu, Lakehouse, ESB, MDM, Xử lý dữ liệu,
Text-to-data, Quản trị siêu dữ liệu, SIEM
THIẾT KẾ TÍCH HỢP
8
Phần mềm nguồn
35
Quy trình liên phòng ban
50
```

### Mục 3
```
--- Trang 36 [Từ khóa: đơn vị thành viên, hạ tầng] ---
022. SỰ CẦN THIẾT MỞ RỘNG CỦA TCT VÀ ĐƠN VỊ
1 Dữ liệu nằm ở đơn vị thành viên:  Phần lớn dữ liệu sản xuất – kinh doanh phát sinh tại các đơn vị; không mở
rộng thì giá trị nền tảng dừng ở Văn phòng Tổng công ty
2 Báo cáo hợp nhất thủ công:  Tổng hợp tài chính – nhân sự – SXKD toàn Tổng công ty và báo cáo Tập đoàn
PVN hiện chậm, không nhất quán danh mục
3 Master Data không thống nhất:  Khách hàng, nhà cung cấp, vật tư, dự án… lệch nhau giữa các đơn vị → sai
lệch số liệu hợp nhất, cản trở AI/phân tích liên đơn vị
4 Yêu cầu pháp lý mới:  Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (hiệu lực 01/01/2026), Luật An ninh mạng
2025, luật dữ liệu, luật CDS → cần quản trị, giám sát, truy vết dữ liệu thống nhất
5 Thời điểm tối ưu:  Mở rộng ngay sau GĐ1 kế thừa trọn bộ tiêu chuẩn, hạ tầng, kinh nghiệm → rẻ và nhanh hơn
nhiều so với từng đơn vị tự đầu tư riêng lẻ
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 3 · LỘ TRÌNH TRIỂN KHAI MỞ RỘNG 31
```

### Mục 4
```
--- Trang 37 [Từ khóa: vận hành, quy chế, quyết định, đơn vị thành viên] ---
2.1 KHUNG TUÂN THỦ: BVDLCN – AN NINH MẠNG – DỮ LIỆU –
CHUYỂN ĐỔI SỐ
Luật Nghĩa vụ chính đối với PTSC Triển khai tại đơn vị thành viên
BVDLCN
91/2025/QH15
(01/01/2026)
Quy chế xử lý DLCN; hồ sơ DPIA; hồ sơ chuyển
DLCN ra nước ngoài; quyền chủ thể dữ liệu; thông
báo vi phạm 72 giờ
Bộ hồ sơ mẫu từ TCT — đơn vị lập theo mẫu; nhãn DLCN
trong catalog + che dữ liệu; quyền chủ thể qua MDM (soft-
delete có kiểm soát); DPO 2 cấp; kịch bản + diễn tập 72
giờ
An ninh mạng
2025
Phân loại hệ thống theo cấp độ an toàn; phương án
bảo đảm thẩm định trước vận hành; giám sát, ứng
cứu sự cố
TCT xác định cấp độ một lần, đơn vị thừa hưởng khung
```

### Mục 5
```
--- Trang 38 [Từ khóa: level, vận hành, quản trị dữ liệu, governance, bảo mật, phân quyền, quyết định, hybrid] ---
MÔ HÌNH PHÂN CẤP VAI TRÒ QUẢN TRỊ DỮ LIỆU PTSC (5 LEVELS)
4 LEVEL ĐIỀU HÀNH – 1 LEVEL TRIỂN KHAI – 1 LEVEL KỸ THUẬT
LEVEL
1
ENTERPRISE
DATA GOVERNANCE
Hội đồng Quản trị Dữ liệu
(Data Governance Council)
THÀNH PHẦN VAI TRÒ CHÍNH TRỌNG TÂM
• HĐQT & Ban TGĐ
• Lãnh đạo cấp cao PTSC
• Đại diện các khối trọng yếu
Định hướng
chiến lược  dữ liệu
Phê duyệt chính sách,
tiêu chuẩn dữ liệu
Quyết định dữ liệu
dùng chung
Giám sát Data
```

### Mục 6
```
--- Trang 41 [Từ khóa: spoke, level, chi phí, vận hành, hybrid, đơn vị thành viên] ---
01 TÓM TẮT ĐIỀU HÀNH
Mở rộng Data Platform đến các đơn vị thành viên theo mô hình Hub-
Spoke
01
Nền tảng Giai đoạn 1 đã vận hành
Nền tảng hybrid IMIP Data Platform, 8 phần
mềm nguồn, 35 quy trình liên phòng ban, 50
API chuẩn — phạm vi Văn phòng Tổng công ty.
02
Phần lớn dữ liệu nằm ở đơn vị
Không mở rộng thì giá trị nền tảng dừng ở Văn
phòng Tổng công ty; báo cáo hợp nhất vẫn thủ
công và Master Data vẫn lệch giữa các đơn vị.
03
Điều kiện bắt buộc cho AI, IoT, BI
Chuyển đổi số mức 3 trở lên yêu cầu dữ liệu tự
động, chính xác đến mức realtime; mức 4 –5
yêu cầu ứng dụng AI, IoT và kết nối IT –OT.
04
```

### Mục 7
```
--- Trang 42 [Từ khóa: đơn vị thành viên, hạ tầng] ---
02 BỐI CẢNH VÀ SỰ CẦN THIẾT
Năm lý do bắt buộc mở rộng nền tảng dữ liệu đến đơn vị thành viên
1 Dữ liệu nằm ở đơn vị thành viên Phần lớn dữ liệu sản xuất – kinh doanh phát sinh tại các đơn vị.
2 Báo cáo hợp nhất còn thủ công Tổng hợp tài chính – nhân sự – SXKD toàn Tổng công ty và báo cáo Tập đoàn PVN hiện chậm, không nhất quán
danh mục.
3 Master Data không thống nhất Khách hàng, nhà cung cấp, vật tư, dự án lệch nhau giữa các đơn vị, gây sai lệch số liệu hợp nhất và cản trở phân
tích liên đơn vị.
4 Yêu cầu pháp lý mới Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (hiệu lực 01/01/2026), Luật An ninh mạng 2025, Luật Dữ liệu, Luật
Chuyển đổi số yêu cầu quản trị, giám sát và truy vết dữ liệu thống nhất.
5 Thời điểm tối ưu Mở rộng ngay sau Giai đoạn 1 kế thừa trọn bộ tiêu chuẩn, hạ tầng và kinh nghiệm — rẻ và nhanh hơn nhiều so
với từng đơn vị tự đầu tư riêng lẻ.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 3 · LỘ TRÌNH TRIỂN KHAI MỞ RỘNG 37
```

### Mục 8
```
--- Trang 44 [Từ khóa: spoke, vận hành] ---
03 MỤC TIÊU VÀ NGUYÊN TẮC
Mục tiêu là hệ thống dữ liệu hợp nhất toàn Tổng công ty
TỔNG QUÁT
Hệ thống dữ liệu hợp nhất toàn Tổng công ty theo mô hình Hub-Spoke; dữ liệu là tài sản do Tổng công ty làm chủ, độc lập
với vòng đời phần mềm nghiệp vụ tại từng đơn vị.
CỤ THỂ — CHUẨN XÁC SAU KHẢO SÁT
Chuẩn hóa và đồng bộ Master
Data dùng chung
Golden Record thống nhất cho các
danh mục trọng yếu.
Tự động hóa báo cáo hợp nhất
Tài chính – nhân sự – SXKD từ 3 –4
đơn vị thí điểm về Tổng công ty.
Kho dữ liệu chuyên ngành tại đơn
vị lớn
Đơn vị làm chủ vận hành spoke, tuân
thủ khung quản trị chung.
Nền tảng sẵn sàng cho phân tích
nâng cao
```

## Hạ tầng TCT đã xây dựng (MinIO, Fabric, Lakehouse, dHCI, Zones)
Tìm thấy 48 trang liên quan.

### Mục 1
```
--- Trang 10 [Từ khóa: vận hành, quyết định] ---
LỘ TRÌNH & DÒNG DỮ LIỆU
Lộ trình chuyển đổi & vòng đời dữ liệu PTSC
HIỆN TẠI · 6/2026 GĐ 1 · 2026 – 2027 GĐ 2 · 2028+
Khối Quản trị điều hành (Nghiệp vụ) Khối Vận hành Sản xuất (Chuyên ngành)
TCKT VP KHĐT PC TM CN KTSX NCPT QTNL TK VPĐDT ATCL
1. Lĩnh vực tàu dịch vụ dầu khí
2. Lĩnh vực phương tiện nổi
3. Lĩnh vực Cơ khí dầu khí
4. Lĩnh vực xây lắp công trình công nghiệp trên bờ
5. Lĩnh vực Căn cứ Cảng
6. Lĩnh vực xây lắp công trình biển và vận hành bảo dưỡng
(O&M)
7. Lĩnh vực Khảo sát và sửa chữa công trình ngầm
8. Lĩnh vực NLTTNK
Nhận diện
Cơ hội & Thách thức
Thu thập dữ liệu
Các ứng dụng & hệ
thống
```

### Mục 2
```
--- Trang 35 [Từ khóa: fabric, onelake, hybrid, đơn vị thành viên] ---
011. NỀN TẢNG ĐÃ CÓ TỪ GIAI ĐOẠN 1
PHẠM VI
Văn phòng Tổng công ty PTSC
BỘ TIÊU CHUẨN
Kiến trúc dữ liệu, kiến trúc – quản trị Master Data, tiêu
chuẩn tích hợp toàn hệ sinh thái CNTT
NỀN TẢNG Dữ LIỆU HYBRID — IMIP DATA PLATFORM
CLOUD
Microsoft Fabric / OneLake (20TB), Purview, 70 người
dùng
⌂ ON-PREM
Thu thập dữ liệu, Lakehouse, ESB, MDM, Xử lý dữ liệu,
Text-to-data, Quản trị siêu dữ liệu, SIEM
THIẾT KẾ TÍCH HỢP
8
Phần mềm nguồn
35
Quy trình liên phòng ban
50
```

### Mục 3
```
--- Trang 50 [Từ khóa: spoke, vận hành, governance, fabric, hạ tầng] ---
066. PHƯƠNG ÁN KIẾN TRÚC: MÔ HÌNH HUB-SPOKE
HUB — Data Platform tại Tổng công ty (GĐ1)
Lakehouse trung tâm · MDM Golden Record · Governance/SIEM
tập trung · Fabric/Power BI
Chi nhánh
Như một ban TCT (không dựng spoke)
Đơn vị nhỏ
Tenant trên hub (không dựng spoke)
Đồng bộ dữ liệu dùng chung + dữ liệu tổng hợp qua ESB / API chuẩn (near real -time / batch)
SPOKE
Đơn vị 1
SPOKE
Đơn vị 2
SPOKE
Đơn vị 3
SPOKE
Đơn vị 4
Dữ liệu chuyên ngành lưu tại đơn vị lớn — đơn vị nhỏ chạy trên hạ tầng hub theo mô hình multi-tenant (chi tiết slide 7). Spoke tái sử dụng chính nền tảng IMIP Data
Platform (cấu hình quy mô nhỏ) → đồng nhất công nghệ, kỹ năng vận hành và bộ triển khai mẫu khi nhân rộng.
```

### Mục 4
```
--- Trang 51 [Từ khóa: spoke, workspace, chi phí, vận hành, governance, fabric, hạ tầng] ---
04 MÔ HÌNH KIẾN TRÚC ĐỀ XUẤT
Hub tại Tổng công ty, spoke tại đơn vị lớn, tenant cho đơn vị nhỏ
HUB — TỔNG CÔNG TY
Data Platform
Lakehouse trung tâm MDM · Golden Record Governance · SIEM Fabric / Power BI
Đồng bộ dữ liệu dùng chung và dữ liệu tổng hợp qua ESB / API chuẩn — near real-time hoặc batch
SPOKE — ĐƠN VỊ LỚN
Đơn vị 1 Đơn vị 2 Đơn vị 3 Đơn vị 4
Dữ liệu chuyên ngành lưu tại đơn vị. Spoke tái sử dụng chính nền tảng
IMIP Data Platform ở cấu hình quy mô nhỏ — đồng nhất công nghệ, kỹ
năng vận hành và bộ triển khai mẫu khi nhân rộng.
TENANT TRÊN HUB — ĐƠN VỊ NHỎ VÀ CHI NHÁNH
Chi nhánh Vận hành như một ban của Tổng công ty
Đơn vị nhỏ Workspace / tenant riêng trên hub
Không trang bị Data Platform riêng, chỉ cần agent thu thập dữ liệu tại chỗ
hoặc kéo trực tiếp qua API. Không phát sinh CAPEX hạ tầng và đội vận
hành riêng — chi phí vận hành chung phân bổ theo mức sử dụng.
Tôn trọng chủ quyền dữ liệu và đặc thù
nghiệp vụ
```

### Mục 5
```
--- Trang 61 [Từ khóa: spoke, level, dung lượng, chi phí, vận hành, hạ tầng] ---
08 CHI PHÍ VÀ CƠ CHẾ ĐẦU TƯ
Bảy cấu phần chi phí của phương án mở rộng
01
Hạ tầng
Hạ tầng dHCI tại đơn vị áp dụng
L4; mở rộng dung lượng hub cho
các level còn lại. Tận dụng máy
chủ sẵn có của đơn vị nếu đáp
ứng.
02
License phần mềm nền tảng
Bản quyền 12 tháng cho cloud và
các phần mềm nền tảng; quy mô
theo số đơn vị kết nối và phân
vùng dữ liệu.
03
Dịch vụ triển khai Data
Platform
Triển khai nền tảng tại spoke hoặc
```

### Mục 6
```
--- Trang 62 [Từ khóa: l3, level, chi phí, vận hành, phân quyền, hạ tầng] ---
08 CHI PHÍ VÀ CƠ CHẾ ĐẦU TƯ
Chi phí phát sinh theo từng level triển khai
Nhóm Hạng mục chi phí L1 L2 L3 L4
Hàng hóa
Hạ tầng dHCI riêng tại đơn vị Không Không Không Có
License phần mềm nền tảng Không Không Có Có
Dịch vụ
Triển khai Data Platform Không Có Có Có
Phần mềm dùng chung với Tổng công ty — thiết kế và triển khai tích
hợp Không Có Có Có
Phần mềm dùng chung — thiết kế và triển khai dữ liệu Không Có Có Có
Phần mềm riêng hoặc mới — thiết kế và triển khai tích hợp Có Có Có Có
Phần mềm riêng hoặc mới — thiết kế và triển khai dữ liệu Có Có Có Có
Vận hành Chi phí vận hành nền tảng Phân bổ theo
mức sử dụng
Phân bổ theo
mức sử dụng
Phân bổ theo
mức sử dụng
```

### Mục 7
```
--- Trang 7 [Từ khóa: vận hành, bảo mật, fabric, hybrid, hạ tầng] ---
3 MÔ HÌNH DATA PLATFORM PHỔ BIẾN HIỆN NAY
Hiện nay, có 03 mô hình kiến trúc Nền tảng Dữ liệu (Data Platform) phổ biến:
1
Mô hình kiến trúc Nền tảng dữ liệu triển khai tại chỗ (On-Premise
Data Platform): Hạ tầng và dữ liệu được triển khai, quản lý tại chính hệ
thống máy chủ nội bộ của Tổng công ty PTSC. Mô hình này cho phép
kiểm soát toàn bộ dữ liệu, nhưng đòi hỏi đầu tư lớn vào ứng dụng, hạ
tầng công nghệ, an toàn thông tin, bảo trì và nhân sự vận hành tại chỗ.
Mô hình kiến trúc Nền tảng dữ liệu Điện toán đám mây (Cloud Data
Platform): Nền tảng dữ liệu điện toán đám mây được xem xét áp dụng
các sản phẩm thương mại của các hãng lớn trên thời giới như Fabric
Azure, AWS, Google Cloud Platform…. Khi đó, PTSC không cần đầu tư
máy chủ vật lý, dễ dàng mở rộng và tiếp cận các công nghệ phân tích dữ
liệu tiên tiến (AI, ML). Tuy nhiên, cần cân nhắc yếu tố pháp lý, bảo mật và
kiểm soát dữ liệu.
Mô hình kiến trúc Nền tảng dữ liệu triển khai kết hợp tại chỗ và trên
đám mây (Hybrid Data Platform): Nền tảng Hybrid, multi-cloud, multi-
site được xem xét áp dụng là kết hợp giữa On-Premise và On-Cloud cho
phép sở hữu và kiểm soát hoàn toàn dữ liệu gốc tại chỗ (on-prem), đồng
```

### Mục 8
```
--- Trang 14 [Từ khóa: dung lượng, vận hành, quản trị dữ liệu, governance] ---
NỀN TẢNG DỮ LIỆU (DATA PLATFORM)
15++ công cụ
cho 5 vai trò
Data governance
• Trục tích hợp: WSO2; Apache Camel..
• Ingestion realtime & batch: Airbyte, Debezium,
Dragster..
• Lưu trữ Lakehouse: Apache Iceberg, Parquet..
• Truy vấn & xử lý: Trino, ClickHouse, Flink, Spark
• Chất lượng dữ liệu: dbt, Great Expectations
• Công cụ vẽ biểu đồ, báo cáo tự động
• Công cụ phân tích máy học ML
• Công cụ giám sát an ninh SIEM
• Truy vấn tiếng Việt
• Time-travel dữ liệu / SSO / truy vết người dùng
Khả năng mở rộng theo cả chiều ngang (thêm dung lượng dữ
liệu) và chiều dọc (thêm nhiều tính năng khác)
Data Platform là giải pháp công nghệ đáp
ứng nhu cầu Tích luỹ - Tích hợp - Đồng bộ
```

## Quy chế quản lý & Chủ quyền dữ liệu (Governance, Data Owner, Quyền quyết định)
Tìm thấy 87 trang liên quan.

### Mục 1
```
--- Trang 5 [Từ khóa: vận hành, quản trị dữ liệu] ---
BỐI CẢNH
Hiện trạng thế giới về mô hình quản trị dữ liệu thông minh cho các tập đoàn dịch vụ dầu khí
THỰC TRẠNG / VẤN ĐỀ
Xu hướng công nghệ
chung
• Tự động hoá, robotic
• Cá nhân hoá & đa
phương tiện (thiết bị
di động, tài khoản cá
nhân)
• Thời gian thực: AI
camera/giám sát,
mạng xã hội
Dữ liệu chuyên ngành
• Thăm dò, khảo sát
• Xây lắp
• Khai thác dầu khí
• Vận tải, đường ống,
kho bãi
```

### Mục 2
```
--- Trang 6 [Từ khóa: vận hành, quản trị dữ liệu, phân quyền] ---
TIÊU CHUẨN QUỐC TẾ
Nền tảng quản trị dữ liệu theo chuẩn PPDM — Tóm tắt 5 đặc điểm cốt lõi
1 · Cấu trúc mô hình
Mô hình linh hoạt theo thực thể Site / Location / Area / Cluster / Hierarchy chuẩn PPDM; hỗ trợ trực quan hoá không gian (spatial); mở
rộng không giới hạn qua cấu hình khai báo.
2 · Hợp nhất
Ghi nhận thuộc tính, quan hệ của site / liên hệ / tài sản trong một mô hình mở rộng; nhập–xuất dữ liệu hàng loạt có kiểm tra hợp lệ;
phân loại theo vùng thương mại & phân cấp site; tích hợp dữ liệu từ các ứng dụng chuyên sâu trong lĩnh vực dầu khí.
3 · Làm sạch
Chuẩn hoá dữ liệu theo tiêu chuẩn ngành/tổ chức; tự sinh mã site; kiểm tra hợp lệ theo quy tắc tự định nghĩa; chống trùng lặp; tuỳ
biến quy tắc làm sạch riêng cho dữ liệu chuyên sâu lĩnh vực dầu khí.
4 · Quản trị
Quản lý vòng đời site tập trung; bản đồ hoá dữ liệu (tích hợp Google Maps); quản lý hợp đồng & tài sản, vận hành tài sản cố định,
kiểm kê theo site (tích hợp Oracle); lưu vết kiểm toán; phân quyền theo vai trò (RBAC) tới từng thuộc tính.
5 · Chia sẻ
Cung cấp "bản ghi vàng" (golden record) cho toàn bộ ứng dụng & hệ thống phân tích; giao diện tra cứu, tìm kiếm linh hoạt; chia sẻ dữ
liệu liền mạch qua web service.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 1 · MÔ HÌNH KIẾN TRÚC DỮ LIỆU 06
```

### Mục 3
```
--- Trang 7 [Từ khóa: quản trị dữ liệu] ---
HIỆN TRẠNG PTSC
Hiện trạng hệ thống CSDL của PTSC
Vấn đề trọng tâm:  Hiện đang chưa liên kết được mô hình quản trị định lượng tổng thể
CL Chiến Lược Tầm Nhìn Và Chiến Lược Mô Hình Hoạt Động Thiết Lập Và Giám Sát Mục Tiêu
CT Cấu trúc tổ chức Cơ Cấu Tổ Chức (Chức Năng) Quản Trị Tập Đoàn (Cấp Độ Tập Đoàn & Tổng công ty & Đơn vị)
QT Quy trình & Hệ
Thống Tối Ưu Hoá Quy Trình Hệ Thống - Số Hóa Doanh Nghiệp Quản Lý KPI
DL Dữ Liệu Quản trị dữ liệu Thu Thập Lưu Trữ Dữ Liệu Trực Quan Hóa / Sử dụng
Dữ Liệu
Trí Tuệ Nhân Tạo & Máy
Học
Tự động hoá, điều khiển
từ xa, Digital Twin / IoT
CN Con Người Kiểm Tra Sức Khỏe Văn hóa Và Mức Độ Thống
Nhất Doanh Nghiệp Xây Dựng Năng Lực Thưởng & Khuyến Khích
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 1 · MÔ HÌNH KIẾN TRÚC DỮ LIỆU 07
```

### Mục 4
```
--- Trang 9 [Từ khóa: quản trị dữ liệu] ---
KẾ HOẠCH HÀNH ĐỘNG
Các hành động trọng tâm cần thực hiện
CL Chiến Lược
Mô Hình Hoạt Động
Chuẩn hoá và số hoá phân loại các mảng, tên và mã dịch vụ theo tiêu chuẩn
quốc tế.
Thiết Lập Và Giám Sát Mục Tiêu
Đồng bộ và số hoá quản trị chiến lược (ESG, CĐS, kinh doanh...); thiết lập quy
trình và số hoá việc đặt mục tiêu, giao việc, theo dõi, giám sát – báo cáo (hiện
đang trùng lặp >50%).
CT Cấu trúc tổ chức
Cơ Cấu Tổ Chức
Thiết lập cấu trúc tổ chức và quy trình báo cáo đánh giá rõ ràng đối với các
Ban dự án; kết nối mô hình quản trị Nhân tài vào Mục tiêu.
Quản Trị Điều Hành
Thiết lập mô hình quản trị điều hành theo Chiến lược – Giải pháp – Nhiệm vụ –
Mục tiêu – Vụ việc.
QT Quy trình & Hệ
Thống
```

### Mục 5
```
--- Trang 19 [Từ khóa: quy chế, quản trị dữ liệu, đơn vị thành viên] ---
01 · BỐI CẢNH
VÌ SAO CẦN KHUNG QUẢN TRỊ DỮ LIỆU
Vì sao PTSC cần Khung quản trị dữ liệu
● Hiện trạng: dữ liệu nằm phân tán trong từng hệ thống nghiệp vụ, thiếu
chuẩn chung giữa các đơn vị, báo cáo còn phụ thuộc tổng hợp thủ công
● Petrovietnam vừa ban hành hệ thống văn bản mới: Quy chế Quản trị
dữ liệu và 04 Quy định hướng dẫn (danh mục và siêu dữ liệu; chất
lượng và làm sạch; chia sẻ và chuyển giao; kiểm soát truy cập và
đánh giá nội bộ)
● PTSC là đơn vị thành viên, bắt buộc tuân thủ và đồng bộ toàn bộ hệ thống
văn bản này
● Nghĩa vụ pháp lý mới: Luật Dữ liệu, Luật Chuyển đổi số, Luật Bảo vệ dữ
liệu cá nhân, Luật An ninh mạng, Khung kiến trúc dữ liệu quốc gia
MỤC TIÊU
Quản lý dữ liệu như tài sản chiến lược
Theo nguyên tắc
Đúng · Đủ · Sạch · Sống · Thống nhất ·
Dùng chung
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 15
```

### Mục 6
```
--- Trang 20 [Từ khóa: quy chế] ---
02 · CẤU TRÚC
KHUNG GỒM NHỮNG GÌ
Khung gồm những gì
• Quy chế: 7 chương, 30 điều — nguyên tắc, phân loại, miền
dữ liệu, vai trò, trách nhiệm
• 13 phụ lục, tổ chức theo 5 nhóm đối ứng hệ thống văn bản
Petrovietnam
• Mỗi phụ lục có bảng đối chiếu sang biểu mẫu tương ứng của
Petrovietnam để thuận tiện kiểm tra tuân thủ
Nhóm A Danh mục, siêu dữ liệu và lưu trữ 5 phụ lục
Nhóm B Chất lượng và làm sạch 2 phụ lục
Nhóm C Chia sẻ, kết nối và chuyển giao 3 phụ lục
Nhóm D Kiểm soát truy cập và đánh giá nội bộ 2 phụ lục
Nhóm E Mở rộng riêng của PTSC 1 phụ lục
CƠ CẤU 13 PHỤ LỤC GỒM:
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 16
```

### Mục 7
```
--- Trang 21 [Từ khóa: vận hành, quy chế, quản trị dữ liệu, phân quyền] ---
02 · CẤU TRÚC
MÔ HÌNH QUẢN TRỊ 5 CẤP
Mô hình quản trị dữ liệu 5 cấp
Cấp Chủ thể Vai trò chính
Cấp 1 Hội đồng Quản trị Dữ liệu (và Văn phòng Quản trị
Dữ liệu) Định hướng chiến lược; phê duyệt chính sách, tiêu chuẩn; xử lý xung đột liên miền
Cấp 2 Hội đồng Dữ liệu khối / chuyên ngành Điều phối liên Ban; đồng bộ tiêu chuẩn giữa các miền dữ liệu
Cấp 3 Chủ quản dữ liệu (Trưởng Ban) Quản lý nghiệp vụ dữ liệu của miền; phê duyệt phân loại, chất lượng, truy cập, chia sẻ. Trách nhiệm giải trình đặt ở
cấp này
Cấp 4 Quản trị miền dữ liệu Siêu dữ liệu, từ điển, quy tắc chất lượng; chuẩn hóa, ánh xạ; xử lý vấn đề dữ liệu
Cấp 5 Đơn vị vận hành hệ thống dữ liệu (Ban NCPT&CDS) Vận hành nền tảng, phân quyền, giám sát, sao lưu. Không sở hữu dữ liệu nghiệp vụ
Tên gọi các vai trò thống nhất với Quy chế Quản trị dữ liệu của Petrovietnam. Chủ sở hữu dữ liệu theo định nghĩa của Tập đoànlà tổ chức — tức PTSC.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 17
```

### Mục 8
```
--- Trang 22 [Từ khóa: quyết định] ---
03 · VAI TRÒ
CHỦ QUẢN DỮ LIỆU
Trưởng Ban/ Lãnh đạo Đơn vị - Chủ quản dữ liệu cần làm gì?
1 Phê duyệt phân loại và gắn nhãn dữ liệu của miền phụ trách (Cấp 4 đề xuất)
2 Quyết định định nghĩa dữ liệu, quy tắc nghiệp vụ, tiêu chuẩn chất lượng, ngưỡng
lỗi, từ điển dữ liệu
3 Xác định thời hạn lưu trữ cho mọi nhóm dữ liệu của miền — điều kiện để vận
hành vòng đời và tiêu hủy
4 Thẩm định và phê duyệt yêu cầu truy cập, chia sẻ, chuyển giao trong phạm vi
phân cấp
5 Phê duyệt bản ghi chuẩn khi các hệ thống có dữ liệu mâu thuẫn
6 Xác định dữ liệu cá nhân trong miền để áp dụng biện pháp bảo vệ theo luật
7 Chỉ định nhân sự Quản trị miền dữ liệu (Cấp 4) và bảo đảm nguồn lực
8 Có quyền dừng cung cấp, chia sẻ dữ liệu nếu yêu cầu vi phạm quy định hoặc gây
mất an toàn
Chất lượng dữ liệu là một tiêu chí đánh giá mức độ hoàn thành nhiệm vụ.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 18
```

## Chi phí & Phân bổ tài chính (Duy trì, License, Mở rộng, Ngân sách)
Tìm thấy 54 trang liên quan.

### Mục 1
```
--- Trang 5 [Từ khóa: vận hành, quản trị dữ liệu] ---
BỐI CẢNH
Hiện trạng thế giới về mô hình quản trị dữ liệu thông minh cho các tập đoàn dịch vụ dầu khí
THỰC TRẠNG / VẤN ĐỀ
Xu hướng công nghệ
chung
• Tự động hoá, robotic
• Cá nhân hoá & đa
phương tiện (thiết bị
di động, tài khoản cá
nhân)
• Thời gian thực: AI
camera/giám sát,
mạng xã hội
Dữ liệu chuyên ngành
• Thăm dò, khảo sát
• Xây lắp
• Khai thác dầu khí
• Vận tải, đường ống,
kho bãi
```

### Mục 2
```
--- Trang 10 [Từ khóa: vận hành, quyết định] ---
LỘ TRÌNH & DÒNG DỮ LIỆU
Lộ trình chuyển đổi & vòng đời dữ liệu PTSC
HIỆN TẠI · 6/2026 GĐ 1 · 2026 – 2027 GĐ 2 · 2028+
Khối Quản trị điều hành (Nghiệp vụ) Khối Vận hành Sản xuất (Chuyên ngành)
TCKT VP KHĐT PC TM CN KTSX NCPT QTNL TK VPĐDT ATCL
1. Lĩnh vực tàu dịch vụ dầu khí
2. Lĩnh vực phương tiện nổi
3. Lĩnh vực Cơ khí dầu khí
4. Lĩnh vực xây lắp công trình công nghiệp trên bờ
5. Lĩnh vực Căn cứ Cảng
6. Lĩnh vực xây lắp công trình biển và vận hành bảo dưỡng
(O&M)
7. Lĩnh vực Khảo sát và sửa chữa công trình ngầm
8. Lĩnh vực NLTTNK
Nhận diện
Cơ hội & Thách thức
Thu thập dữ liệu
Các ứng dụng & hệ
thống
```

### Mục 3
```
--- Trang 14 [Từ khóa: vận hành] ---
THAM KHẢO — HIỆU QUẢ CẢNG BIỂN
Ví dụ tham khảo: đo lường hiệu quả vận hành cảng biển
Gợi ý ứng dụng cho PTSC:  các chỉ số về thời gian quay vòng tàu, thời gian chờ cầu cảng và phân bổ thời gian cập cảng là ví dụ tham khảo tốt khi xây dựng bộ KPI giám sát cho dịch
vụ cảng & logistics của PTSC.
Nguồn tham khảo: Port Economics & Management  (PEMP)
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 1 · MÔ HÌNH KIẾN TRÚC DỮ LIỆU 12
```

### Mục 4
```
--- Trang 32 [Từ khóa: chi phí] ---
A. TẦM QUAN TRỌNG CỦA VIỆC TRIỂN KHAI
DATA PLATFORM
B. MÔ HÌNH VÀ PHƯƠNG ÁN TRIỂN KHAI MỞ
RỘNG DATA PLATFORM
C. LỘ TRÌNH MỞ RỘNG DATA PLATFORM (Dự
kiến)
D. CẤU TRÚC CHI PHÍ DỰ KIẾN VÀ KIẾN NGHỊ
— MỤC LỤC
Nội dung trình bày
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 3 · LỘ TRÌNH TRIỂN KHAI MỞ RỘNG 27
```

### Mục 5
```
--- Trang 36 [Từ khóa: đơn vị thành viên, hạ tầng] ---
022. SỰ CẦN THIẾT MỞ RỘNG CỦA TCT VÀ ĐƠN VỊ
1 Dữ liệu nằm ở đơn vị thành viên:  Phần lớn dữ liệu sản xuất – kinh doanh phát sinh tại các đơn vị; không mở
rộng thì giá trị nền tảng dừng ở Văn phòng Tổng công ty
2 Báo cáo hợp nhất thủ công:  Tổng hợp tài chính – nhân sự – SXKD toàn Tổng công ty và báo cáo Tập đoàn
PVN hiện chậm, không nhất quán danh mục
3 Master Data không thống nhất:  Khách hàng, nhà cung cấp, vật tư, dự án… lệch nhau giữa các đơn vị → sai
lệch số liệu hợp nhất, cản trở AI/phân tích liên đơn vị
4 Yêu cầu pháp lý mới:  Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (hiệu lực 01/01/2026), Luật An ninh mạng
2025, luật dữ liệu, luật CDS → cần quản trị, giám sát, truy vết dữ liệu thống nhất
5 Thời điểm tối ưu:  Mở rộng ngay sau GĐ1 kế thừa trọn bộ tiêu chuẩn, hạ tầng, kinh nghiệm → rẻ và nhanh hơn
nhiều so với từng đơn vị tự đầu tư riêng lẻ
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 3 · LỘ TRÌNH TRIỂN KHAI MỞ RỘNG 31
```

### Mục 6
```
--- Trang 41 [Từ khóa: spoke, level, chi phí, vận hành, hybrid, đơn vị thành viên] ---
01 TÓM TẮT ĐIỀU HÀNH
Mở rộng Data Platform đến các đơn vị thành viên theo mô hình Hub-
Spoke
01
Nền tảng Giai đoạn 1 đã vận hành
Nền tảng hybrid IMIP Data Platform, 8 phần
mềm nguồn, 35 quy trình liên phòng ban, 50
API chuẩn — phạm vi Văn phòng Tổng công ty.
02
Phần lớn dữ liệu nằm ở đơn vị
Không mở rộng thì giá trị nền tảng dừng ở Văn
phòng Tổng công ty; báo cáo hợp nhất vẫn thủ
công và Master Data vẫn lệch giữa các đơn vị.
03
Điều kiện bắt buộc cho AI, IoT, BI
Chuyển đổi số mức 3 trở lên yêu cầu dữ liệu tự
động, chính xác đến mức realtime; mức 4 –5
yêu cầu ứng dụng AI, IoT và kết nối IT –OT.
04
```

### Mục 7
```
--- Trang 42 [Từ khóa: đơn vị thành viên, hạ tầng] ---
02 BỐI CẢNH VÀ SỰ CẦN THIẾT
Năm lý do bắt buộc mở rộng nền tảng dữ liệu đến đơn vị thành viên
1 Dữ liệu nằm ở đơn vị thành viên Phần lớn dữ liệu sản xuất – kinh doanh phát sinh tại các đơn vị.
2 Báo cáo hợp nhất còn thủ công Tổng hợp tài chính – nhân sự – SXKD toàn Tổng công ty và báo cáo Tập đoàn PVN hiện chậm, không nhất quán
danh mục.
3 Master Data không thống nhất Khách hàng, nhà cung cấp, vật tư, dự án lệch nhau giữa các đơn vị, gây sai lệch số liệu hợp nhất và cản trở phân
tích liên đơn vị.
4 Yêu cầu pháp lý mới Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (hiệu lực 01/01/2026), Luật An ninh mạng 2025, Luật Dữ liệu, Luật
Chuyển đổi số yêu cầu quản trị, giám sát và truy vết dữ liệu thống nhất.
5 Thời điểm tối ưu Mở rộng ngay sau Giai đoạn 1 kế thừa trọn bộ tiêu chuẩn, hạ tầng và kinh nghiệm — rẻ và nhanh hơn nhiều so
với từng đơn vị tự đầu tư riêng lẻ.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 3 · LỘ TRÌNH TRIỂN KHAI MỞ RỘNG 37
```

### Mục 8
```
--- Trang 43 [Từ khóa: chi phí, vận hành] ---
02 BỐI CẢNH VÀ SỰ CẦN THIẾT
Data Platform là điều kiện bắt buộc để đạt mức trưởng thành số cao
hơn
Không có Data Platform
Dữ liệu phân tán trong nhiều phần mềm; chi phí phát triển tính năng và
vận hành tăng nhanh; phụ thuộc nhà cung cấp phần mềm.
Khai thác dữ liệu bằng Excel
Tra cứu, xuất Excel và mapping tay; không có nơi thu thập và xử lý dữ liệu
lớn cho chuỗi giao dịch 5 –10 năm.
Quản trị tổng thể liên Phòng/Ban
Không có nơi quản lý liên kết và đồng bộ dữ liệu giữa các phần mềm
nghiệp vụ rời rạc, bao gồm Master Data.
ĐỊNH HƯỚNG CHUYỂN ĐỔI SỐ
CĐS Mức 3
Yêu cầu dữ liệu nhanh hơn, chính xác hơn đến mức realtime — không
thể thực hiện bằng sức người và Excel.
CĐS Mức 4 – 5
Bắt buộc ứng dụng AI, IoT và kết nối IT với OT.
Data Platform là công nghệ bắt buộc phải có.
```

## Dung lượng & Khả năng lưu trữ (Quota, Dung lượng, Storage)
Tìm thấy 113 trang liên quan.

### Mục 1
```
--- Trang 6 [Từ khóa: vận hành, quản trị dữ liệu, phân quyền] ---
TIÊU CHUẨN QUỐC TẾ
Nền tảng quản trị dữ liệu theo chuẩn PPDM — Tóm tắt 5 đặc điểm cốt lõi
1 · Cấu trúc mô hình
Mô hình linh hoạt theo thực thể Site / Location / Area / Cluster / Hierarchy chuẩn PPDM; hỗ trợ trực quan hoá không gian (spatial); mở
rộng không giới hạn qua cấu hình khai báo.
2 · Hợp nhất
Ghi nhận thuộc tính, quan hệ của site / liên hệ / tài sản trong một mô hình mở rộng; nhập–xuất dữ liệu hàng loạt có kiểm tra hợp lệ;
phân loại theo vùng thương mại & phân cấp site; tích hợp dữ liệu từ các ứng dụng chuyên sâu trong lĩnh vực dầu khí.
3 · Làm sạch
Chuẩn hoá dữ liệu theo tiêu chuẩn ngành/tổ chức; tự sinh mã site; kiểm tra hợp lệ theo quy tắc tự định nghĩa; chống trùng lặp; tuỳ
biến quy tắc làm sạch riêng cho dữ liệu chuyên sâu lĩnh vực dầu khí.
4 · Quản trị
Quản lý vòng đời site tập trung; bản đồ hoá dữ liệu (tích hợp Google Maps); quản lý hợp đồng & tài sản, vận hành tài sản cố định,
kiểm kê theo site (tích hợp Oracle); lưu vết kiểm toán; phân quyền theo vai trò (RBAC) tới từng thuộc tính.
5 · Chia sẻ
Cung cấp "bản ghi vàng" (golden record) cho toàn bộ ứng dụng & hệ thống phân tích; giao diện tra cứu, tìm kiếm linh hoạt; chia sẻ dữ
liệu liền mạch qua web service.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 1 · MÔ HÌNH KIẾN TRÚC DỮ LIỆU 06
```

### Mục 2
```
--- Trang 7 [Từ khóa: quản trị dữ liệu] ---
HIỆN TRẠNG PTSC
Hiện trạng hệ thống CSDL của PTSC
Vấn đề trọng tâm:  Hiện đang chưa liên kết được mô hình quản trị định lượng tổng thể
CL Chiến Lược Tầm Nhìn Và Chiến Lược Mô Hình Hoạt Động Thiết Lập Và Giám Sát Mục Tiêu
CT Cấu trúc tổ chức Cơ Cấu Tổ Chức (Chức Năng) Quản Trị Tập Đoàn (Cấp Độ Tập Đoàn & Tổng công ty & Đơn vị)
QT Quy trình & Hệ
Thống Tối Ưu Hoá Quy Trình Hệ Thống - Số Hóa Doanh Nghiệp Quản Lý KPI
DL Dữ Liệu Quản trị dữ liệu Thu Thập Lưu Trữ Dữ Liệu Trực Quan Hóa / Sử dụng
Dữ Liệu
Trí Tuệ Nhân Tạo & Máy
Học
Tự động hoá, điều khiển
từ xa, Digital Twin / IoT
CN Con Người Kiểm Tra Sức Khỏe Văn hóa Và Mức Độ Thống
Nhất Doanh Nghiệp Xây Dựng Năng Lực Thưởng & Khuyến Khích
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 1 · MÔ HÌNH KIẾN TRÚC DỮ LIỆU 07
```

### Mục 3
```
--- Trang 8 [Từ khóa: vận hành] ---
ĐỊNH HƯỚNG
Định hướng
• Hướng đến một trung tâm dữ liệu sạch, đáng tin cậy — kết nối phương tiện, thiết bị, con người và hệ thống thành một mạng lưới cộng tác
thông minh, xoá bỏ các đảo dữ liệu (data silo), nâng cao khả năng dự đoán và minh bạch trong vận hành. Mỗi mắt xích — từ bãi chứa đến kho,
đến điều phối — vận hành đồng bộ, hiệu quả.
• Cho phép mở rộng thông minh theo quy mô kinh doanh — khả năng mở rộng linh hoạt, tăng trưởng cùng doanh nghiệp.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 1 · MÔ HÌNH KIẾN TRÚC DỮ LIỆU 08
```

### Mục 4
```
--- Trang 10 [Từ khóa: vận hành, quyết định] ---
LỘ TRÌNH & DÒNG DỮ LIỆU
Lộ trình chuyển đổi & vòng đời dữ liệu PTSC
HIỆN TẠI · 6/2026 GĐ 1 · 2026 – 2027 GĐ 2 · 2028+
Khối Quản trị điều hành (Nghiệp vụ) Khối Vận hành Sản xuất (Chuyên ngành)
TCKT VP KHĐT PC TM CN KTSX NCPT QTNL TK VPĐDT ATCL
1. Lĩnh vực tàu dịch vụ dầu khí
2. Lĩnh vực phương tiện nổi
3. Lĩnh vực Cơ khí dầu khí
4. Lĩnh vực xây lắp công trình công nghiệp trên bờ
5. Lĩnh vực Căn cứ Cảng
6. Lĩnh vực xây lắp công trình biển và vận hành bảo dưỡng
(O&M)
7. Lĩnh vực Khảo sát và sửa chữa công trình ngầm
8. Lĩnh vực NLTTNK
Nhận diện
Cơ hội & Thách thức
Thu thập dữ liệu
Các ứng dụng & hệ
thống
```

### Mục 5
```
--- Trang 20 [Từ khóa: quy chế] ---
02 · CẤU TRÚC
KHUNG GỒM NHỮNG GÌ
Khung gồm những gì
• Quy chế: 7 chương, 30 điều — nguyên tắc, phân loại, miền
dữ liệu, vai trò, trách nhiệm
• 13 phụ lục, tổ chức theo 5 nhóm đối ứng hệ thống văn bản
Petrovietnam
• Mỗi phụ lục có bảng đối chiếu sang biểu mẫu tương ứng của
Petrovietnam để thuận tiện kiểm tra tuân thủ
Nhóm A Danh mục, siêu dữ liệu và lưu trữ 5 phụ lục
Nhóm B Chất lượng và làm sạch 2 phụ lục
Nhóm C Chia sẻ, kết nối và chuyển giao 3 phụ lục
Nhóm D Kiểm soát truy cập và đánh giá nội bộ 2 phụ lục
Nhóm E Mở rộng riêng của PTSC 1 phụ lục
CƠ CẤU 13 PHỤ LỤC GỒM:
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 16
```

### Mục 6
```
--- Trang 22 [Từ khóa: quyết định] ---
03 · VAI TRÒ
CHỦ QUẢN DỮ LIỆU
Trưởng Ban/ Lãnh đạo Đơn vị - Chủ quản dữ liệu cần làm gì?
1 Phê duyệt phân loại và gắn nhãn dữ liệu của miền phụ trách (Cấp 4 đề xuất)
2 Quyết định định nghĩa dữ liệu, quy tắc nghiệp vụ, tiêu chuẩn chất lượng, ngưỡng
lỗi, từ điển dữ liệu
3 Xác định thời hạn lưu trữ cho mọi nhóm dữ liệu của miền — điều kiện để vận
hành vòng đời và tiêu hủy
4 Thẩm định và phê duyệt yêu cầu truy cập, chia sẻ, chuyển giao trong phạm vi
phân cấp
5 Phê duyệt bản ghi chuẩn khi các hệ thống có dữ liệu mâu thuẫn
6 Xác định dữ liệu cá nhân trong miền để áp dụng biện pháp bảo vệ theo luật
7 Chỉ định nhân sự Quản trị miền dữ liệu (Cấp 4) và bảo đảm nguồn lực
8 Có quyền dừng cung cấp, chia sẻ dữ liệu nếu yêu cầu vi phạm quy định hoặc gây
mất an toàn
Chất lượng dữ liệu là một tiêu chí đánh giá mức độ hoàn thành nhiệm vụ.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 18
```

### Mục 7
```
--- Trang 23 [Từ khóa: phân quyền, quyết định, nhạy cảm] ---
03 · VAI TRÒ
PHÂN LOẠI & GẮN NHÃN
Phân loại và gắn nhãn dữ liệu theo 6 chiều
Chiều phân loại Nhãn Cấp quyết định
1. Tính chất chia sẻ Công khai / dùng chung / dùng chung có điều kiện / dùng riêng Cấp 3 phê duyệt
2. Mức độ quan trọng Cốt lõi / quan trọng / khác Cấp 1 ban hành tiêu chí
3. Tính chất bí mật Công khai / nội bộ / mật (bí mật nội bộ) Cấp 1 và Văn phòng
4. Dữ liệu cá nhân Cá nhân cơ bản / cá nhân nhạy cảm / không phải dữ liệu cá nhân Cấp 1 ban hành tiêu chí
5. Nguồn gốc Gốc / phát sinh / được chia sẻ / tổng hợp, phân tích Cấp 3 phê duyệt
6. Vòng đời Tạo lập / đang sử dụng / lưu trữ / lưu giữ lâu dài / hết thời hạn / xóa, hủy Cấp 3 phê duyệt
Mỗi tài sản dữ liệu mang đồng thời 6 nhãn và được gán về đúng một miền dữ liệu. Nhãn quyết định chính sách phân quyền, chia sẻ, lưu trữ và tiêu hủy.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 19
```

### Mục 8
```
--- Trang 29 [Từ khóa: vận hành, phân quyền] ---
05 · VẬN HÀNH
12 QUY TRÌNH SỐ HÓA
Mười hai quy trình quản trị dữ lieu được số hóa trên Data Platform
Quy trình Cấp phê duyệt Quy trình Cấp phê duyệt
1. Đăng ký tài sản dữ liệu Cấp 3 7. Yêu cầu truy cập, phân quyền Cấp 3
2. Siêu dữ liệu và luồng truy xuất Cấp 4 8. Phân loại và gắn nhãn Cấp 3
3. Chất lượng và làm sạch Cấp 3 9. Từ điển nghiệp vụ, chỉ tiêu Cấp 3
4. Quản lý thay đổi Cấp 3 10. Vòng đời, lưu trữ, tiêu hủy Cấp 3
5. Quản lý sự cố dữ liệu Cấp 3 11. Kết nối, chia sẻ, chuyển giao Cấp 3
6. Dữ liệu chủ, bản ghi chuẩn Cấp 3 12. Đánh giá nội bộ, khắc phục Cấp 1
Mọi quy trình đều tạo hồ sơ điện tử và lưu vết. Trưởng Ban là cấp phê duyệt ở 10 trên 12 quy trình.
HỘI THẢO DATA PLATFORM  ·  PHIÊN CHIỀU 2 · CHÍNH SÁCH DỮ LIỆU 24
```

