

## 1. BỐI CẢNH — ĐỌC KỸ TRƯỚC KHI LÀM

- **Người thuyết trình:** cán bộ IT, Ban Dự án Chuyển đổi số, PTSC Quảng Ngãi. Anh mới vào đơn vị, là đầu mối dự án Data Platform (DP) của đơn vị, không phải chuyên gia từng hệ thống — vai trò là người hỏi và tổng hợp, không phải người biết hết đáp án.
- **Người nghe:** Giám đốc PTSC Quảng Ngãi + Ban lãnh đạo đơn vị. Giám đốc rất bận, **KHÔNG theo dõi chi tiết DP**. Ông cần nghe bằng tiếng Việt thường, mỗi slide một ý, và cuối buổi phải biết mình cần quyết cái gì.
- **Mục tiêu buổi họp:** lãnh đạo hiểu (1) DP là gì và giải quyết nỗi đau nào, (2) Quảng Ngãi đang ở đâu, (3) đơn vị phải làm gì, và (4) RA 4 QUYẾT ĐỊNH ở cuối buổi.
- **Bối cảnh thời gian:** đoàn khảo sát của Tổng công ty về đơn vị từ **thứ Hai 30/11/2026** (tuần sau). Buổi thuyết trình này diễn ra trước đó.

## 2. NHIỆM VỤ

Làm **MỘT bộ PowerPoint duy nhất** kết hợp hài hòa 2 thứ:
- (a) Bộ 15 slide HTML hiện tại (`ptsc-data-platform-slides.html`) — giữ lại toàn bộ chiều sâu kỹ thuật của nó (CDC, ESB, Landing Zone, Lakehouse, MDM, Dual-Code…), nhưng viết lại bằng ngôn ngữ lãnh đạo hiểu được.
- (b) Mạch kể chuyện cho lãnh đạo: mở đầu bằng nỗi đau → DP là gì → kiến trúc tổng quan → dữ liệu chạy thế nào → đơn vị phải làm gì → chi phí → lộ trình → **quyết định**.

**Không giới hạn số lượng slide** — dùng bao nhiêu slide cũng được, miễn mạch truyện xuyên suốt. Dự kiến khoảng 22 slide theo dàn bài ở mục 3.

## 3. DÀN BÀI ĐẦY ĐỦ (LÀM ĐÚNG THỨ TỰ NÀY)

### Phần 0 — Mở đầu
1. **Trang bìa:** "PTSC Data Platform — PTSC Quảng Ngãi: dữ liệu đang ở đâu, đi về đâu, đơn vị phải làm gì". Ghi rõ người trình bày + ngày họp (để trống ngày nếu chưa biết).
2. **3 nỗi đau hiện tại:** (a) Dữ liệu kẹt trong từng phần mềm riêng (silo), không nói chuyện được với nhau; (b) Báo cáo tổng hợp bằng Excel ghép tay — toàn PTSC có **310 báo cáo rời rạc**; (c) Mã lệch giữa các hệ thống — ví dụ minh họa: cùng một nhà cung cấp, FAST ghi `NCC-001`, MESX ghi `KH-118` (ghi rõ đây là ví dụ minh họa, không phải mã thật).
3. **Data Platform là gì — 1 câu + 3 trụ cột:** "DP không thay thế phần mềm cũ — nó là lớp nền để dữ liệu từ 6 hệ thống cũ chảy chung, sạch và dùng được." 3 trụ cột: Nhà máy dữ liệu (Lakehouse) · Trục tích hợp (ESB) · Phiên dịch mã chuẩn.

### Phần I — Kiến trúc tổng quan
4. **Vì sao chọn Hybrid:** dữ liệu nhạy cảm ở lại on-prem, dữ liệu tổng hợp chuẩn hóa mới lên Cloud. Cụm dHCI **8 node** tại tầng 10 Cơ quan TCT (~40 TB, mở rộng trên 200 TB) + Microsoft Fabric **Capacity F16, OneLake 20 TB, 70 người dùng thường xuyên, Purview 500 assets**.
5. **Mô hình Hub – Spoke – Tenant (L1–L4):** chèn sơ đồ L3 Tenant. Quảng Ngãi thuộc **Nhóm 4 (đơn vị lớn, L3–L4)** — mức chính thức **chưa chốt, chốt sau khảo sát GĐ2A**.
6. **Mô hình Hub – Spoke – Tenant (tiếp):** chèn sơ đồ L4 Spoke. Ghi rõ 4 tiêu chí lên L4: (1) khối lượng dữ liệu lớn, (2) phân tích chuyên ngành cường độ cao, (3) ràng buộc lưu trữ tại chỗ, (4) đủ đội IT vận hành. Và ghi rõ: **đơn vị không bao giờ tự xây Hub** — Hub chỉ có ở TCT; Spoke cũng **không có ESB riêng** (trục ESB duy nhất đặt ở Hub).
7. **Kiến trúc an ninh 10 vùng (bắt buộc phải có):** liệt kê đủ 10 vùng — 1 Internet Edge, 2 DMZ, 3 Security (NGFW/SIEM), 4 Server Farm (chứa Data Platform), 5 Tích hợp & Đệm (ESB/API Gateway/Kafka/CDC + kiểm tra chất lượng), 6 Shared Services, 7 Storage, 8 Vận hành, 9 Backup & DR, 10 Out-of-band. Nhấn mạnh vùng 5: ESB chỉ là 1 trong 4 "anh em" trong vùng 5, không phải chứa tất cả.
8. **Chủ quyền dữ liệu — 3 lớp:** (a) Kỹ thuật: cách ly truy cập bằng RBAC/ABAC theo tenant, đơn vị duyệt tại Landing Zone trước khi dữ liệu vào vùng dùng chung; (b) Nội dung: dữ liệu chia 3 nhóm — dùng chung / chỉ tổng hợp mới đưa lên / chi tiết chuyên ngành giữ tại chỗ; (c) Quản trị: đơn vị là Data Owner, TCT là chủ nền tảng. **Và nói rõ giới hạn trung thực:** audit log của mọi đơn vị đổ về SIEM trung tâm; ở tầng hạ tầng sâu nhất, đơn vị vận hành nền tảng về mặt lý thuyết có khả năng truy cập — kiểm soát làm cho mọi truy cập đều phải có quyền, có mục đích, có dấu vết. **TUYỆT ĐỐI KHÔNG viết "TCT không lấy dữ liệu" hay "cách ly tuyệt đối".**

### Phần II — Dữ liệu chạy thế nào (lấy từ bộ HTML, viết lại cho lãnh đạo)
9. **Hành trình 1 gói dữ liệu — 5 trạm tổng quan:** vẽ 1 sơ đồ thẳng: Nguồn → ESB → Landing Zone + QC → Lakehouse + MDM → BI/AI, kèm mũi tên ngược (trả mã chuẩn về nguồn). Đây là slide bản đồ, các slide sau đi từng trạm.
10. **Trạm 1 — CDC đọc ngầm:** "Khi nhân viên bấm Lưu ở phần mềm cũ, máy đọc dòng thay đổi từ sổ ghi chép của cơ sở dữ liệu (Transaction Log) — không truy vấn trực tiếp vào phần mềm nguồn nên không tranh tài nguyên lúc nhập liệu." Công cụ: Debezium (thời gian thực), Airbyte (gom theo lịch). Ghi chú: phương thức kết nối từng hệ thống **chốt sau khảo sát**, không khẳng định cả 6 hệ thống đều nối bằng CDC.
11. **Trạm 2 — Trục ESB + chống trùng:** thay nối tay đôi 1–1 bằng 1 trục duy nhất (WSO2/Camel, đặt ở vùng 5 tại Hub). Mỗi gói dữ liệu được gắn mã vận đơn (CorrelationId) để truy vết; gửi lặp do rớt mạng thì máy tự bỏ qua nhờ chống trùng (Idempotency). E-Office là phần mềm nguồn ngang hàng (API thật: CreateTicket, ApproveSignEO, UpdateDocument, UpdateInvoice), không phải trạm trung gian.
12. **Trạm 3 — Landing Zone + QC + duyệt:** dữ liệu mới nằm ở vùng đệm riêng của đơn vị, chưa ai khác thấy. Máy tự kiểm tra (dbt / Great Expectations): thiếu mã số thuế, trùng ID, thông tin nhạy cảm thì che lại. **100% gói dữ liệu phải qua QC; gói lỗi bị chặn sang vùng cách ly, trả về sửa tại nguồn rồi nộp lại** — không viết "100% gói qua QC" kiểu gây hiểu là 100% đạt. Gói sạch chờ **Data Owner của đơn vị bấm Approve** mới vào vùng dùng chung.
13. **Trạm 4 — Lakehouse Iceberg + Time-Travel:** lưu linh hoạt như hồ dữ liệu, truy vấn nhanh như kho dữ liệu. Mỗi lần cập nhật lưu một ảnh chụp bất biến — kéo thanh thời gian là xem được số liệu ở mốc cũ để đối chiếu kiểm toán. (Các con số trong bảng ví dụ phải ghi rõ **"số liệu minh họa"**.)
14. **Trạm 5 — MDM, 1 Bản ghi vàng duy nhất:** gộp các bản ghi trùng lệch thành 1 hồ sơ chuẩn do TCT quản trị. Ví dụ minh họa: `NCC-001` (FAST) + `KH-118` (MESX) → 1 Golden Record, giữ liên kết cả mã gốc, chỉ soft-delete có kiểm soát. MDM có 10 chức năng (mô hình, tích hợp, làm sạch, đối khớp & gộp, quản trị, phiên bản, luật nghiệp vụ, phân cấp, công bố, phân quyền).
15. **Phiên dịch mã — 2 cơ chế, đừng trộn:** (a) Dữ liệu chủ (9 lĩnh vực: Đơn vị, Dự án, Khách hàng, Nhà cung cấp, Hợp đồng, Tài sản, Vật tư/Dịch vụ, Nhân sự, Bộ mã dùng chung) dùng **bảng ánh xạ 3 tầng**: Mã đơn vị → Chuẩn TCT → Chuẩn PVN (2 cột chuẩn để trống cho tới khi TCT ban hành — đơn vị không tự bịa mã chuẩn). (b) Dữ liệu kỹ thuật chuyên ngành dùng **PPDM Dual-Code**: ví dụ `P3.ME` ↔ `NORSOK:ME` mức EXACT qua bảng DISCIPLINE_CODE_XREF; D1–D8 là thực thể giao nhận (deliverable) riêng, không phải một mắt xích trong chuỗi `P3.ME → Deliverable → NORSOK:ME`.
16. **Đầu ra trên bàn lãnh đạo:** 20 báo cáo BI tự động (GĐ1) + hỏi bằng tiếng Việt (Text-to-Data) + Catalog tiếng Việt xem nguồn gốc số liệu (Lineage). **5 bảng GOLD là bảng demo theo yêu cầu POC, xây trên dữ liệu mẫu — ghi rõ nhãn này trên slide, đừng trình bày như sản phẩm thật.** Tên bảng giữ nguyên như trong Data Kit, kể cả tên `golden_customer_porfolio` (ghi chú nhỏ: tên gốc trong Data Kit).

### Phần III — Đơn vị phải làm gì
17. **4 việc của đơn vị:** (1) Con người: lãnh đạo làm Data Owner (Cấp 3), cử đầu mối miền dữ liệu (Cấp 4, tối đa 9 miền); (2) Mở cổng: lắp agent/API nối 6 hệ thống vào Landing Zone; (3) Duyệt dữ liệu: kiểm tra và Approve/Reject tại Landing Zone; (4) Chi phí: theo cơ chế Phương án 3 (xem slide 19).
18. **Quản trị 5 cấp — đơn vị chỉ nắm 2 cấp:** Cấp 1 Hội đồng Quản trị Dữ liệu (TCT) · Cấp 2 Hội đồng khối (TCT) · **Cấp 3 Chủ quản dữ liệu = Lãnh đạo đơn vị (Data Owner, chịu trách nhiệm giải trình)** · **Cấp 4 Đầu mối miền (Data Steward)** · Cấp 5 Vận hành kỹ thuật (Ban NCPT & CĐS, không sở hữu dữ liệu nghiệp vụ). Nhấn mạnh: đơn vị KHÔNG phải cử người cho cả 5 cấp.
19. **Chuẩn bị đón đoàn khảo sát (từ 30/11/2026):** hồ sơ 8 phần / 73 việc đã chuẩn bị; mỗi hệ thống có 3 đầu mối (key user + IT + kỹ thuật); danh sách 6 hệ thống (Cảng, FAST, MESX, Bán hàng, E-Office, HRM) cần IT xác nhận đầy đủ, kể cả hệ thống ngầm/hệ thống chết. **Câu hỏi đầu tiên phải hỏi đoàn: tiến độ thực tế của GĐ1 so với các mốc hợp đồng** (theo hợp đồng: bàn giao license 01/04/2026, hạ tầng 15/06/2026, đưa vào sử dụng 27/08/2026 — hôm nay đã ~3 tháng sau mốc đó mà chưa có xác nhận tiến độ thực tế).

### Phần IV — Chi phí, lộ trình, quyết định
20. **Chi phí theo cấp L1–L4 (bảng đúng theo slide in 58, trang PDF 62, phiên chiều):** Hạ tầng dHCI riêng: L1/L2/L3 Không, L4 Có · License nền tảng: L1/L2 Không, L3/L4 Có · Triển khai DP: L1 Không, L2/L3/L4 Có · Tích hợp & dữ liệu phần mềm dùng chung: L1 Không, L2/L3/L4 Có · Tích hợp & dữ liệu phần mềm riêng/mới: Có ở mọi cấp · Vận hành: L1–L3 phân bổ theo mức sử dụng, L4 tự vận hành. License tính 12 tháng, gồm 10 mục: Cloud, Ingestion, Lakehouse, ESB, MDM, Phân quyền Data Operation, Xử lý dữ liệu, Text-to-data, SIEM, Quản trị siêu dữ liệu. Viết đúng: **"0 CAPEX hạ tầng dHCI"** cho L1–L3 — không viết "0đ CAPEX" (L3 vẫn trả license, triển khai, tích hợp, vận hành phân bổ).
21. **Phương án 3 (cơ chế đầu tư kiến nghị):** TCT đầu tư Hub, nền tảng dùng chung, bản quyền khung & tiêu chuẩn; đơn vị đầu tư/thuê Spoke + tích hợp nội bộ theo định mức chuẩn; đơn vị chưa có nguồn kinh phí thì TCT đầu tư trước và **ghi nợ**; tỷ lệ phân bổ cụ thể xây dựng trong GĐ2A (chưa có tỷ lệ — không tự bịa tỷ lệ).
22. **Ước tính chi phí L3 vs L4 (ghi rõ là ƯỚC TÍNH):** Năm đầu L3 ~10,0 tỷ, L4 ~22,0 tỷ; 5 năm L3 ~16,8 tỷ, L4 ~40,4 tỷ (chênh ~23,6 tỷ). Phí vận hành tính từ năm 2 (L3 0,6 tỷ/năm, L4 2,4 tỷ/năm) nên KHÔNG nằm trong tổng năm đầu. **Trên slide phải ghi to, rõ: "Số ước tính theo giả định thị trường, KHÔNG phải số liệu PTSC. Khái toán chính thức chỉ có sau khảo sát GĐ2A + sizing."** Phần tích hợp + dữ liệu cho 6 hệ thống (~7,1 tỷ) tốn như nhau ở cả 2 phương án — tiền chênh nằm ở hạ tầng, license và vận hành riêng.
23. **Lộ trình 3 dải — trung thực, không che mâu thuẫn:** (a) ĐÃ DIỄN RA: kick-off 04/03/2026, GĐ1 theo hợp đồng đưa vào sử dụng 27/08/2026 (hợp đồng 18 tháng, consortium HIPT-AITS); (b) DỰ KIẾN (theo PDT27 — BẢN NHÁP chưa phê duyệt): đăng ký Combo/Nhóm 12/2026, ESB tại CQTCT 03/2027, các nhóm triển khai trong 2027; (c) CHƯA THỐNG NHẤT: GĐ2 là 2026–2027 hay 2028+ (các tài liệu nói khác nhau), ngày khảo sát GĐ2A chờ TCT chốt.
24. **QUYẾT ĐỊNH XIN GIÁM ĐỐC (slide cuối — bắt buộc):** 4 quyết định, mỗi cái có người chịu trách nhiệm + hạn: (1) Ký giao đầu mối dự án DP của đơn vị; (2) Chỉ định Data Owner (lãnh đạo đơn vị) + Data Steward theo 9 miền dữ liệu; (3) Đồng ý gửi văn bản 4 câu hỏi cho TCT (Quảng Ngãi có nằm trong danh sách SAP S/4HANA không; kênh/mẫu/hạn đăng ký Combo/Nhóm tháng 12; thời gian khảo sát GĐ2A và đơn vị cần chuẩn bị gì; PDT27 bản 29/10/2026 đã phê duyệt chưa, nếu có bản mới xin gửi); (4) Chuẩn bị đăng ký Combo/Nhóm tháng 12/2026.

## 4. 8 LỖI BẮT BUỘC SỬA (ĐỐI CHIẾU BỘ HTML CŨ)

| # | Lỗi trong bộ cũ | Sửa thành |
|---|---|---|
| 1 | Slide ESB ghi nguồn "HRM / CMMS" | CMMS không nằm trong 6 hệ thống của Quảng Ngãi (bảo dưỡng nằm trong MESX) — đổi thành MESX |
| 2 | KPI "100% gói dữ liệu qua QC" | Viết: "100% gói dữ liệu phải qua QC; gói lỗi bị chặn lại, không vào SILVER" (100% trong POC là tỷ lệ phát hiện lỗi) |
| 3 | Nhắc "ClickHouse" | Bỏ — không có trong tài liệu nào; chỉ giữ Trino/Flink |
| 4 | 5 bảng GOLD trình bày như sản phẩm thật | Thêm nhãn: "Bảng GOLD demo theo yêu cầu POC — dữ liệu mẫu, chưa phải số liệu thật" |
| 5 | KPI "0% gây chậm màn hình nhập liệu" | Viết: "không truy vấn trực tiếp vào phần mềm nguồn nên không tranh tài nguyên lúc nhập liệu" |
| 6 | "6 hệ thống kết nối qua CDC/Airbyte" | Viết: "phương thức kết nối từng hệ thống chốt sau khảo sát" |
| 7 | "GĐ1 sử dụng 27/08/2026" ghi như sự thật | Viết: "Theo hợp đồng GĐ1 đưa vào sử dụng 27/08/2026 — tiến độ thực tế cần hỏi Taskforce/đoàn khảo sát" |
| 8 | Tên bảng `golden_customer_porfolio` | Giữ nguyên tên gốc, thêm ghi chú "(tên gốc trong Data Kit)" |

## 5. QUY TẮC DỮ KIỆN — VI PHẠM LÀ HỎNG BÀI

- **Không bịa số, bịa ngày, bịa định nghĩa.** Cái nào không có trong tài liệu thì ghi rõ "chưa có / chờ xác nhận / chờ khảo sát GĐ2A", hoặc bỏ khỏi slide.
- **Không trích số lượng đơn vị theo cấp L1–L4** (tài liệu ghi 17 đơn vị nhưng bảng phân cấp cộng ra 21 — mâu thuẫn, không trích). Được nêu tên nhóm: Nhóm 4 gồm M&C, PPS, POS, Quảng Ngãi, Thanh Hóa. **Không nêu M&C làm ví dụ L4** — M&C còn đang thảo luận riêng L3 hay L4.
- **Không dùng tên "IMIP"** trong bất kỳ slide nào.
- **Không đưa mốc thời gian nào thành cam kết** — GĐ2A không có ngày trong tài liệu; PDT27 là bản nháp chưa phê duyệt, mọi mốc của nó phải ghi "(dự kiến, bản nháp)".
- **Mọi con số chi phí đều là ước tính** (mục 3, slide 22) — không trình bày như số liệu PTSC.
- **Trích nguồn trên từng slide** (ghi nhỏ ở chân slide): khi trích slide hội thảo phiên chiều, ghi CẢ số slide in VÀ trang PDF (ví dụ: "Phiên chiều, slide in 58, trang PDF 62"). Nguồn chính: slide hội thảo sáng/chiều 10/08/2026, Báo cáo kỹ thuật TCT-DP, Phụ lục hợp đồng 02, PDT27 (nháp), hồ sơ yêu cầu GĐ1 + POC + kick-off (hợp đồng 1-2026/PTSC-CDS/HĐ).
- **"Bronze" không tồn tại** — pipeline là RAW → SILVER → GOLD. "Bản ghi vàng" (Golden Record) là sản phẩm của MDM, khác với tầng GOLD.

## 6. PHONG CÁCH TRÌNH BÀY — BẮT BUỘC

- **PowerPoint (.pptx), chỉnh sửa được. Nền trắng. Header xanh navy #1F4E79. Tiêu đề xanh đậm #1F3864. Font Calibri. Bảng plain, hàng xen kẽ #F2F2F2, tiêu đề nhóm #D9E2F3. Footer mỗi slide: "PTSC Quảng Ngãi". KHÔNG dùng Dark Mode, KHÔNG dùng nền đen, KHÔNG làm kiểu "AI-generated".**
- Mặt slide thoáng: mỗi slide một ý chính, chữ lớn, đọc được khi chiếu phòng họp (cỡ chữ nội dung tối thiểu 18pt). Phần giải thích dài đưa vào **Speaker Notes** của PowerPoint, không nhồi lên mặt slide.
- Sơ đồ L3/L4 chèn nguyên file PNG đã có (không vẽ lại, không đổi nội dung sơ đồ).
- Mọi slide có số nguồn ở chân slide (mục 5).

## 7. ĐẦU RA

- File: `slide-thuyet-trinh-lanh-dao-data-platform-quang-ngai.pptx`
- Kèm file PDF xuất từ PowerPoint để xem trước.

## 8. TỰ KIỂM TRA TRƯỚC KHI GIAO (CHECKLIST — PHẢI TICK HẾT)

- [ ] Đủ 24 slide theo dàn bài mục 3, đúng thứ tự (nỗi đau → DP là gì → kiến trúc → 5 trạm → đơn vị làm gì → chi phí → lộ trình → 4 quyết định)?
- [ ] 8 lỗi ở mục 4 đã sửa hết?
- [ ] Có slide 10 vùng an ninh? Có slide đoàn khảo sát 30/11? Có slide 4 quyết định cuối?
- [ ] Không còn từ "tuyệt đối", "0đ CAPEX", "Bronze", "IMIP", "ClickHouse", "CMMS" (trong danh sách hệ thống Quảng Ngãi)?
- [ ] Số ước tính chi phí có ghi rõ "ước tính, không phải số liệu PTSC"?
- [ ] Mọi mốc PDT27/GĐ2A có ghi "dự kiến / chưa thống nhất"?
- [ ] Nền trắng, header #1F4E79, Calibri, footer PTSC Quảng Ngãi?
- [ ] Speaker Notes đã viết cho mọi slide?
- [ ] Mở file PPTX kiểm tra: không tràn chữ, không chồng lấn, sơ đồ PNG hiển thị đủ?
