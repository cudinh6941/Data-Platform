# ĐÁNH GIÁ DÀN BÀI SLIDE & CHECKLIST DỮ KIỆN — THUYẾT TRÌNH DATA PLATFORM

*Soạn ngày 25/11/2026. Đối chiếu dàn bài `slide-outline.md` (10 slide, cấu trúc Nancy Duarte Sparkline, "Tech Dark Mode × Swiss Grid", mỗi slide < 40 chữ) với toàn bộ 7 nhóm tài liệu gốc: 2 tài liệu 2025, 2 deck hội thảo 08/2026, Phụ lục hợp đồng 02, PDT27, và 5 tài liệu mới trong Drive (HSYC GĐ1, yêu cầu POC, slide kick-off, Data Kit).*

**Kết luận một dòng:** Khung kể chuyện Sparkline tốt, giữ được — nhưng dàn bài có **4 lỗi dữ kiện nghiêm trọng** (M&C không phải ví dụ L4; "0đ CAPEX" gây hiểu lầm; "TCT không lấy dữ liệu" nói quá; "Bronze" không tồn tại trong tài liệu), **3 ví dụ minh họa bịa** (BOM-01/M001, e-Office duyệt trả về ERP, P3.ME → Deliverable → NORSOK:ME), và **đối tượng nghe + phong cách thiết kế sai với thực tế** của anh (lãnh đạo đơn vị Quảng Ngãi, slide trắng công sở — không phải lãnh đạo TCT, không phải Dark Mode). Sửa theo mục 4 là dùng được.

---

## 1. BẢNG VERDICT NHANH — 10 SLIDE

| Slide | Tiêu đề | Verdict | Lỗi chính |
|---|---|---|---|
| 01 | PTSC Data Platform | **Giữ** | Thiếu tên chính thức dự án; cấm dùng tên "IMIP" |
| 02 | 3 Nỗi đau hiện tại | **Sửa** | Ví dụ `BOM-01 vs M001` bịa (0 kết quả); không có số liệu thời gian báo cáo hay số đơn vị lệch mã |
| 03 | Data Platform là gì? | **Giữ** | Ẩn dụ tốt; cần nói rõ "phiên dịch" là ánh xạ mã chuẩn TCT trước, chuẩn quốc tế chỉ cho dữ liệu chuyên ngành |
| 04 | 3 Tầng giá trị Lakehouse | **Sửa** | "Bronze" **không tồn tại** trong tài liệu — pipeline là RAW → SILVER → GOLD; "Bản ghi vàng" là sản phẩm của MDM, không phải tên tầng GOLD |
| 05 | Trục tích hợp ESB | **Sửa** | Sơ đồ luồng sai vị trí e-Office; ví dụ "e-Office duyệt trả kết quả về ERP" **không có trong tài liệu** |
| 06 | Phiên dịch chuẩn PPDM | **Sửa** | Chuỗi mũi tên `P3.ME → Deliverable → NORSOK:ME` sai cấu trúc; Dual-Code chỉ áp cho dữ liệu kỹ thuật/chuyên ngành, không phải toàn bộ dữ liệu chủ |
| 07 | Mô hình Hub – Spoke | **Sửa** | **PTSC M&C không phải ví dụ L4** (chưa chốt L3 hay L4); "0đ CAPEX" gây hiểu lầm (L3 vẫn trả license + triển khai + tích hợp); "5 cấp" là quản trị, không phải thuộc tính Hub–Spoke; số lượng đơn vị theo cấp cộng ra 21 ≠ 17 — **không được trích** |
| 08 | Chủ quyền dữ liệu | **Sửa** | "TCT không lấy dữ liệu — cách ly tuyệt đối" **nói quá**: dữ liệu dùng chung và tổng hợp vẫn đưa lên Hub (có duyệt); log kiểm toán đổ về SIEM trung tâm |
| 09 | Vai trò Đơn vị: 4 việc của Data Owner | **Sửa** | "Cử đầu mối 5 cấp" **sai**: 5 cấp là mô hình quản trị, đơn vị chỉ nắm Cấp 3 (Lãnh đạo đơn vị = Data Owner) + Cấp 4 (đầu mối từng miền); không có tỷ lệ chia sẻ OPEX nào trong tài liệu |
| 10 | Lộ trình & Quyết định | **Sửa** | **Không có một mốc thời gian thống nhất nào** trong tài liệu (3 phiên bản mâu thuẫn nhau); không có tên đơn vị thí điểm nào; 3 hành động thì giữ được, cần sửa câu chữ |

---

## 2. GÓP Ý CHI TIẾT TỪNG SLIDE

### Slide 01 — PTSC Data Platform (Giữ)
- **Đúng:** mở đầu bằng một câu định vị là đúng kiểu Sparkline (hook).
- **Thiếu:** tên chính thức chương trình. Dùng: **"Dự án Nền tảng dữ liệu (Data Platform) — Giai đoạn 1"**, mã dự án **HDP26**, hợp đồng **1-2026/PTSC-CDS/HĐ**, chủ trì: Ban Dự án Chuyển đổi số (PTSC-CDS), nhà thầu liên danh HIPT-AITS (nguồn: slide kick-off 04/03/2026).
- **Cấm:** không dùng tên **"IMIP"** trên slide — dù deck hội thảo có ghi "IMIP Data Platform", đây là tên bị cấm trong tài liệu trình lãnh đạo theo quy định của anh.
- **Bối cảnh phiên họp:** ghi rõ "Thuyết trình cho lãnh đạo PTSC Quảng Ngãi" — không phải "Ban Lãnh đạo PTSC & Lãnh đạo Đơn vị thành viên" (xem mục 5a).

### Slide 02 — 3 Nỗi đau hiện tại (Sửa)
- **Ví dụ `BOM-01 vs M001`: BỊA.** Grep toàn bộ 7 nhóm tài liệu: **0 kết quả**. Không có mã nào tên BOM-01 hay M001.
- **Ví dụ thay thế có nguồn:** dùng ví dụ minh họa đã dùng nhất quán từ trước — nhà cung cấp **FAST: NCC-001** vs **MESX: KH-118** — nhưng phải ghi chú rõ **đây là ví dụ minh họa, không phải dữ liệu thật**. (Cả hai mã này cũng không xuất hiện trong tài liệu; chúng chỉ là ví dụ do Muse đặt ra để diễn giải.)
- **Số liệu dùng được (có nguồn):**
  - **310 báo cáo** hiện có tại PTSC (slide "Hiện trạng dữ liệu – Báo cáo tại PTSC", deck hội thảo) — dùng được cho ý "báo cáo nhiều mà rời rạc".
  - **8 phần mềm nguồn, 35 quy trình liên phòng ban, 50 API chuẩn** — phạm vi Giai đoạn 1 tại Cơ quan TCT (deck phiên chiều, slide "5 lý do mở rộng"). Đây là số của **Văn phòng TCT**, không phải toàn Tổng công ty — ghi rõ phạm vi khi dùng.
  - "Báo cáo hợp nhất vẫn thủ công, chậm, không kịp thời" — chỉ có mô tả định tính trong deck; **không có con số ngày/giờ nào** (xem mục 3).
- **Không được đưa lên slide:** "số đơn vị gặp lỗi lệch mã" (không có số liệu), "số ngày làm báo cáo thủ công" (không có số liệu), "tổng số hệ thống toàn TCT" (không có con số tổng; chỉ có 8 hệ thống nguồn GĐ1 tại CQTCT và 6 hệ thống tại Quảng Ngãi theo danh sách làm việc của anh — danh sách này còn chờ phòng CNTT xác nhận đầy đủ).
- **Câu chữ đề xuất:** "Dữ liệu kẹt trong silo — 310 báo cáo rời rạc; báo cáo hợp nhất còn tổng hợp thủ công, chậm; mã dữ liệu chủ lệch nhau giữa các hệ thống (ví dụ minh họa: NCC-001 vs KH-118)."

### Slide 03 — Data Platform là gì? (Giữ)
- **Đúng:** "Không thay thế phần mềm cũ" — khớp PDT27 ("không làm lại quy trình nghiệp vụ đang chạy tốt, chỉ chuẩn hóa lớp tích hợp") và HSYC GĐ1 (phạm vi trọn gói chỉ tích hợp, không thay phần mềm).
- **Ẩn dụ "Nhà máy · Bưu điện · Phiên dịch":** dùng được, nhưng "Phiên dịch" cần nói đúng: DP dịch mã nội bộ sang **mã chuẩn TCT trước**, rồi sang mã chuẩn PVN (bảng ánh xạ 3 tầng). Chuẩn quốc tế (NORSOK/ISO/CFIHOS) chỉ áp cho dữ liệu kỹ thuật/chuyên ngành trong khung PPDM (xem slide 06), không phải cho toàn bộ dữ liệu chủ.
- **Danh sách hệ thống cũ vẫn giữ:** tại Quảng Ngãi là 6 hệ thống (phần mềm cảng, ERP FAST, MESX, phần mềm bán hàng, E-Office, HRM). Tại CQTCT GĐ1 là 8 hệ thống nguồn (không liệt kê tên trong deck — đừng bịa tên).

### Slide 04 — 3 Tầng giá trị Lakehouse (Sửa)
- **"Bronze" là SAI.** Grep toàn bộ tài liệu: **"Bronze" = 0 kết quả**, "Medallion" = 0 kết quả. Pipeline trong tài liệu yêu cầu POC và HSYC là **RAW → SILVER → GOLD** (3 lớp, không có Bronze).
- **"Bản ghi vàng" ≠ tầng GOLD.** "Bản ghi vàng" (Golden Record) là sản phẩm của **MDM** — một bản ghi chuẩn duy nhất sau khi gộp các bản trùng/lệch. Tầng GOLD là lớp dữ liệu đã xử lý phục vụ báo cáo/AI. Hai khái niệm khác nhau; đừng viết "dữ liệu thô qua 3 tầng thành Bản ghi vàng".
- **Ví dụ đầu ra tầng GOLD có nguồn (dùng được):** 5 bảng GOLD trong bộ Data Kit của POC — `golden_asset_utilization`, `golden_customer_porfolio` (sai chính tả "porfolio" trong file gốc), `golden_employee_performance`, `golden_product_performance`, `golden_transaction_summary`. Hoặc ví dụ gần lãnh đạo hơn: **20 báo cáo BI tự động** trong phạm vi GĐ1 (báo cáo kỹ thuật, mục dịch vụ BI) và báo cáo Kết quả HĐSXKD bằng Excel (phạm vi trọn gói GĐ1 theo HSYC).
- **Câu chữ đề xuất:** "Dữ liệu thô (RAW) được làm sạch qua SILVER thành GOLD — 5 bảng GOLD phục vụ dashboard và AI; dữ liệu chủ được gộp thành Bản ghi vàng duy nhất."

### Slide 05 — Trục tích hợp ESB (Sửa)
- **Sơ đồ luồng sai:** `ERP/HRM/CMMS ↔ ESB ↔ e-Office → DP` đặt e-Office như một trạm trung gian giữa ESB và DP — sai. E-Office là một hệ thống nguồn như ERP/HRM/CMMS. Luồng đúng: **ERP / HRM / CMMS / E-Office → ESB (Zone 5 tại Hub) → Landing Zone → Lakehouse (DP)**. Chiều về: mã chuẩn + Bản ghi vàng + báo cáo trả về hệ thống nguồn.
- **Ví dụ "e-Office duyệt trả kết quả về ERP": KHÔNG CÓ trong tài liệu.** Grep "PR → E-Office → PO" và mọi biến thể: **0 kết quả**. Đây là ví dụ minh họa cũ đã từng bị gắn cờ là "chỉ mang tính minh họa".
- **Ví dụ thay thế có nguồn:**
  - Tiêu chí POC: dữ liệu chủ mới tạo ở **1 phần mềm phải đồng bộ sang tối thiểu 2 phần mềm còn lại qua ESB** (yêu cầu POC, tiêu chí 3).
  - Phụ lục hợp đồng 02, §2: luồng 2 chiều bắt buộc qua ESB/API Gateway và/hoặc Kafka, **kể cả chiều nhận dữ liệu chủ đã chuẩn hóa về** để cập nhật an toàn vào phần mềm; kèm API E-Office có tên thật: `CreateTicket`, `ApproveSignEO`, `UpdateDocument`, `UpdateInvoice`.
- **Đúng và giữ:** "Xóa bỏ kết nối chằng chịt; đồng bộ 2 chiều; Audit Log" — khớp nguyên tắc "một ESB dùng chung duy nhất" (Phụ lục 02, §1) và yêu cầu idempotency/correlationId (Phụ lục 02, §2 nhóm 9).
- **Câu chữ đề xuất:** "Một trục ESB duy nhất tại Hub thay cho kết nối chằng chịt 1–1; dữ liệu chủ đồng bộ 2 chiều, mọi giao dịch ghi Audit Log."

### Slide 06 — Phiên dịch chuẩn PPDM (Sửa)
- **Chuỗi `P3.ME → Deliverable → NORSOK:ME` SAI cấu trúc.** Tài liệu gốc (deck phiên sáng, mục 3.2 "PPDM Framework — Dual-Code Architecture") nói:
  - **P3.ME** là mã nội bộ (Company Code): P3 = Engineering (ngành kỹ thuật), ME = Mechanical (cơ khí, mã ngành con). Mã nội bộ là display key, không bao giờ sửa — chỉ retire.
  - **NORSOK:ME** là mã chuẩn quốc tế đối ứng. Hai mã nối nhau qua bảng **DISCIPLINE_CODE_XREF**, với độ tin cậy EXACT / PARTIAL / NONE. Ví dụ đúng trong tài liệu: **"P3.ME — NORSOK:ME = EXACT"** (ánh xạ ở cấp ngành con thấp nhất).
  - **Deliverable (D1–D8)** là một thực thể khác: "hợp đồng" giữa hai ngành (producer → deliverable → consumer), ví dụ D1 Contract Package, D3 Design Package, D4 Purchase Requisition, D7 CFIHOS Handover. Deliverable **không nằm trong chuỗi ánh xạ mã** — đừng vẽ mũi tên P3.ME → Deliverable → NORSOK:ME.
- **"Chuẩn PPDM":** PPDM là tên khung mô hình (PPDM Association Reference), không phải tên một bộ chuẩn. Các chuẩn đối ứng thật: **NORSOK Z-DP-002, ISO 15926 / 14224 / 19008, VSIC 2018, CFIHOS 2.0**. Tiêu đề nên là "Phiên dịch chuẩn quốc tế (NORSOK / ISO / CFIHOS) trong khung PPDM".
- **Phạm vi áp dụng — điểm quan trọng nhất:** Dual-Code chỉ áp cho **dữ liệu kỹ thuật/chuyên ngành dầu khí** (EPCI & vận hành, chuỗi giá trị P1→P7, 8 deliverable). Toàn bộ dữ liệu chủ (9 lĩnh vực: Đơn vị, Dự án, Khách hàng, Nhà cung cấp, Hợp đồng, Tài sản, Vật tư/Dịch vụ, Nhân sự, Bộ mã dùng chung) dùng **bảng ánh xạ mã 3 tầng** (mã đơn vị → mã chuẩn TCT → mã chuẩn PVN), không dùng Dual-Code. Đừng để lãnh đạo hiểu rằng mọi mã đều "dịch sang NORSOK".
- **"Cho khách hàng Tây":** sửa thành **"cho đối tác và khách hàng quốc tế"** — tài liệu nói "tương thích chuẩn quốc tế phục vụ tích hợp với đối tác & client" và "báo cáo song song theo VSIC 2018".
- **Câu chữ đề xuất:** "Giữ nguyên mã nội bộ (P3.ME); ánh xạ sang chuẩn quốc tế (NORSOK:ME = EXACT) qua bảng đối chiếu — phục vụ đối tác quốc tế, không đổi mã cũ."

### Slide 07 — Mô hình Hub – Spoke (Sửa — slide nhiều lỗi nhất)
- **LỖI 1 — "PTSC M&C" không phải ví dụ L4.** Deck phiên chiều (slide in 50, trang PDF 55) ghi rõ: *"Riêng PTSC M&C sẽ có phiên thảo luận riêng về mô hình kiến trúc dữ liệu để xác định áp dụng L3 hoặc L4."* M&C thuộc Nhóm 4 (đơn vị lớn, L3–L4) cùng với PPS, POS, Quảng Ngãi, Thanh Hóa — mức độ **chưa chốt**. Không có đơn vị nào được nêu tên là L4 trong tài liệu. **Bỏ M&C khỏi slide, hoặc ghi đúng: "M&C — đang thảo luận riêng L3 hay L4".**
- **LỖI 2 — "0đ CAPEX" gây hiểu lầm.** Bảng chi phí theo cấp (slide in 58, trang PDF 62): hạ tầng dHCI riêng tại đơn vị: L1/L2/L3 = Không, L4 = Có. Nhưng **License phần mềm: L3 = Có**; Triển khai Data Platform: L3 = Có; tích hợp phần mềm dùng chung và phần mềm riêng: L3 = Có; vận hành: L3 = phân bổ theo mức sử dụng. Nghĩa là Tenant L3 **không tốn CAPEX hạ tầng**, nhưng vẫn trả license, triển khai, tích hợp, dữ liệu và phí vận hành phân bổ. Hero metric đúng phải là **"0 CAPEX hạ tầng"**, không phải "0đ CAPEX".
- **LỖI 3 — "5 cấp" đặt sai chỗ.** "5 cấp" là **mô hình quản trị dữ liệu 5 cấp** (deck phiên chiều, slide in 16 và 40), không phải thuộc tính của Hub–Spoke. Đặt nó làm hero metric của slide topology là sai ngữ cảnh — chuyển sang slide 09.
- **LỖI 4 — Số lượng đơn vị theo cấp KHÔNG ĐƯỢC TRÍCH.** Deck ghi L1·5, L2·2, L3·13, L4·1 = **21 đơn vị**, trong khi chính deck nói có **17 đơn vị** — mâu thuẫn nội bộ, đã biết từ trước. Không đưa con số 5/2/13/1 lên slide. Chỉ được nói: "17 đơn vị và chi nhánh được phân về 4 nhóm triển khai; danh sách và mức áp dụng cho từng đơn vị được chốt sau khảo sát Giai đoạn 2A."
- **"2 chiều":** giữ — luồng 2 chiều là thật (đi lên + trả về, xem slide 05).
- **"L4 tự chủ Spoke IoT":** sửa thành **"L4 tự chủ Spoke — dữ liệu chuyên ngành và OT quy mô lớn giữ tại đơn vị"**. Deck định nghĩa L4 bằng 4 tiêu chí tốt nghiệp (khối lượng dữ liệu, phân tích chuyên ngành cường độ cao, ràng buộc lưu trữ tại chỗ, năng lực vận hành) — "IoT" một mình là hẹp và gây hiểu lầm.
- **Tiêu chí phân loại L1–L4 (có nguồn, dùng được):** theo pháp nhân, quy mô và mức trưởng thành số (DBI). L1: chi nhánh trực thuộc, DBI 0–2, dùng chung 100%. L2: chi nhánh trực thuộc, DBI 0–2, dùng chung trên 70%. L3: pháp nhân độc lập hoặc chi nhánh có nhu cầu dữ liệu lớn, DBI 2–3,5, đăng ký thêm phân vùng tenant. L4: pháp nhân độc lập, DBI trên 3,5, tự đầu tư dHCI.
- **Câu chữ đề xuất:** "TCT đầu tư Hub trung tâm; đơn vị nhỏ dùng Tenant (0 CAPEX hạ tầng); đơn vị lớn đủ điều kiện mới tự chủ Spoke."

### Slide 08 — Chủ quyền dữ liệu (Sửa)
- **"TCT không lấy dữ liệu của Đơn vị — cách ly tuyệt đối" là NÓI QUÁ, phải sửa.** Sự thật theo tài liệu:
  - Dữ liệu dùng chung (9 lĩnh vực dữ liệu chủ) và dữ liệu tổng hợp **vẫn đưa lên Hub** — chỉ có dữ liệu chuyên ngành chi tiết là giữ tại đơn vị. Đơn vị duyệt/không duyệt tại Landing Zone **trước khi** dữ liệu vào vùng dùng chung.
  - "Cách ly" trong tài liệu là **cách ly bằng RBAC/ABAC theo tenant**: "Đơn vị chỉ thấy dữ liệu của mình; audit log và lineage tách theo tenant" (deck phiên chiều, slide Tenant). Đó là cách ly **truy cập**, không phải cách ly vật lý tuyệt đối.
  - **Nhật ký kiểm toán (audit log) của mọi đơn vị đổ về SIEM tại Hub** để giám sát tập trung (deck phiên chiều) — tức là có một luồng dữ liệu luôn chảy lên, không "tuyệt đối" nào ở đây.
  - Tầng vận hành (Cấp 5, Ban NCPT & CĐS) "không sở hữu dữ liệu nghiệp vụ" — đây là câu đúng để trích.
- **Viết lại theo 3 lớp (có nguồn):**
  1. **Kỹ thuật:** tenant riêng + RBAC/ABAC + đơn vị duyệt tại Landing Zone + audit log về SIEM trung tâm.
  2. **Nội dung:** phân loại dữ liệu 3 nhóm — dùng chung / chỉ đưa tổng hợp / giữ tại chỗ.
  3. **Quản trị:** đơn vị = Chủ sở hữu dữ liệu (Data Owner), TCT = Chủ sở hữu nền tảng và quản trị; Khung quản trị của Petrovietnam ràng buộc cả TCT.
- **Giới hạn trung thực (nói nếu lãnh đạo hỏi vặn):** ở tầng hạ tầng sâu nhất, đơn vị vận hành nền tảng về mặt lý thuyết có khả năng truy cập — các biện pháp kiểm soát làm cho mọi truy cập đều phải có quyền, có mục đích, có dấu vết. Đừng hứa "tuyệt đối" vì không chứng minh được.
- **Công cụ quản trị nêu trong slide:** Purview (500 assets — số tài liệu, đã xác nhận) và MDM (10 chức năng) là đúng. Thêm: dữ liệu cá nhân tuân thủ Luật Bảo vệ dữ liệu cá nhân 91/2025 (hiệu lực 01/01/2026).
- **Câu chữ đề xuất:** "Đơn vị là chủ sở hữu dữ liệu — duyệt trước khi chia sẻ; TCT chỉ vận hành nền tảng, không sở hữu dữ liệu nghiệp vụ."

### Slide 09 — Vai trò Đơn vị: 4 việc của Data Owner (Sửa)
- **"Cử đầu mối 5 cấp" là SAI.** 5 cấp là mô hình quản trị (xem slide 07 lỗi 3): Cấp 1 Hội đồng Quản trị Dữ liệu; Cấp 2 Hội đồng dữ liệu khối/chuyên ngành; **Cấp 3 Chủ quản dữ liệu (Trưởng Ban / Lãnh đạo đơn vị) — trách nhiệm giải trình nằm ở cấp này**; Cấp 4 Quản trị miền dữ liệu (nhân sự đầu mối Phòng/Ban/Đơn vị); Cấp 5 Đơn vị vận hành hệ thống (Ban NCPT & CĐS — **không sở hữu dữ liệu nghiệp vụ**). Đơn vị chỉ nắm **Cấp 3 + Cấp 4**: Lãnh đạo đơn vị làm Data Owner, cử đầu mối từng miền dữ liệu (tối đa 9 miền, miền nhỏ có thể chung một người).
- **"Chia sẻ OPEX/License":** Phương án 3 (deck phiên chiều, slide in 59, trang PDF 63) quy định: TCT đầu tư Hub, nền tảng dùng chung, bản quyền khung và bộ tiêu chuẩn; đơn vị đầu tư hoặc thuê Spoke và tích hợp nội bộ; **đơn vị chưa có nguồn chi phí được TCT đầu tư trước và ghi nợ**; **cơ chế phân bổ chi phí cụ thể xây dựng trong Giai đoạn 2A**. **Không có tỷ lệ hay con số chia sẻ nào** — đừng đưa tỷ lệ lên slide; ghi "cơ chế phân bổ xây dựng trong GĐ2A".
- **4 việc của đơn vị (viết lại cho đúng):**
  1. **Con người:** Lãnh đạo đơn vị làm Data Owner (Cấp 3); cử Steward/đầu mối từng miền dữ liệu (Cấp 4).
  2. **Mở cổng dữ liệu:** lắp agent thu thập tại chỗ hoặc kéo trực tiếp qua API (mô hình Tenant — deck phiên chiều, slide Tenant).
  3. **Duyệt tại Landing Zone:** duyệt/không duyệt trước khi dữ liệu vào vùng dùng chung; dữ liệu bị từ chối nằm lại vùng cách ly, sửa ở nguồn rồi nộp lại.
  4. **Chi phí:** trả license + triển khai + tích hợp + phí vận hành phân bổ theo mức dùng (Phương án 3); chưa có ngân sách thì TCT đầu tư trước, ghi nợ.
- **"Đơn vị không phải code":** đúng tinh thần — đơn vị không xây nền tảng, chỉ chuẩn bị dữ liệu và con người. Giữ câu này.

### Slide 10 — Lộ trình & Quyết định (Sửa)
- **Không có một mốc thời gian thống nhất nào — đây là điểm phải trình bày trung thực, không được vẽ một Gantt "thực tế" duy nhất.** Ba phiên bản trong tài liệu mâu thuẫn nhau:
  - Deck phiên chiều: **GĐ1 2026–2027, GĐ2 2028+** (slide "5 lý do mở rộng" và slide 5.3).
  - Deck phiên sáng: **"CSDL dùng chung giai đoạn 2 (tại các Đơn vị)" nằm trong 2026–2027** — mâu thuẫn với deck chiều.
  - PDT27 (bản nháp chưa phê duyệt, 29/10/2026): business Go-live 31/12/2026, cắt 1–1 sang ESB đầu 03/2027, các Nhóm triển khai trong 2027.
  - Mốc thật duy nhất đã xảy ra: hợp đồng GĐ1 kick-off 04/03/2026, **đưa vào sử dụng 27/08/2026**, vận hành đến 27/08/2027 (slide kick-off). Hôm nay 25/11/2026 đã qua mốc go-live gần 3 tháng — tiến độ thực tế phải hỏi Taskforce.
  - **GĐ2A không có ngày trong bất kỳ tài liệu nào.**
- **Cách trình bày timeline trên slide:** đừng vẽ Gantt liền mạch. Vẽ 3 dòng riêng: (a) **Đã xảy ra** — kick-off 04/03/2026, go-live GĐ1 27/08/2026; (b) **Sắp tới, đã định** — đăng ký Combo/Nhóm tháng 12/2026 (theo PDT27); (c) **Chưa thống nhất, chờ TCT xác nhận** — GĐ2, lịch khảo sát GĐ2A, lộ trình từng Nhóm. Ghi rõ "các tài liệu chưa thống nhất về mốc mở rộng đơn vị".
- **"Đơn vị thí điểm": KHÔNG CÓ tên trong tài liệu.** Deck chiều chỉ nhắc "đơn vị thí điểm" chung chung (không nêu tên). PDT27 có Nhóm 1 (5 chi nhánh + Petro Hotel, từ 01/04/2027) — đó là **đợt triển khai đầu tiên**, không phải "đơn vị thí điểm" theo nghĩa POC. Đừng ghi tên đơn vị thí điểm nào lên slide.
- **3 hành động (giữ, sửa câu chữ):**
  1. Thành lập tổ công tác — sửa thành **"Ký giao nhiệm vụ đầu mối dự án dữ liệu tại đơn vị"** (Taskforce cấp TCT đã có — 15+ chuyên gia; đơn vị cần là quyết định giao nhiệm vụ + đầu mối của mình).
  2. Khảo sát hệ thống nguồn — giữ; cụ thể: kiểm kê 6 phần mềm + phỏng vấn từng hệ thống + đo dung lượng dữ liệu thật.
  3. Thống nhất cơ chế dữ liệu — giữ; cụ thể: bảng ánh xạ mã 3 tầng + phân công Data Owner/Steward + quy trình duyệt Landing Zone.
- **"The Big Ask" cho buổi họp này (xem mục 3):** Giám đốc quyết 3 việc trong buổi họp — ký giao đầu mối, chỉ định người phụ trách dữ liệu, đồng ý gửi văn bản hỏi TCT. Không xin phê duyệt ngân sách (không có số), không xin phê duyệt "Governance 5 cấp" (đó là khung của TCT/PVN, không phải việc lãnh đạo đơn vị phê duyệt).

---

## 3. CHECKLIST DỮ KIỆN ĐÃ ĐIỀN — PHẦN B

Mỗi dòng: giá trị tìm được (kèm nguồn) hoặc **KHÔNG CÓ trong tài liệu** + làm gì thay thế. Không bịa số nào.

| # | Dữ kiện Part B yêu cầu | Kết quả | Nguồn / Làm gì thay thế |
|---|---|---|---|
| B1 | Đối tượng nghe cụ thể | **Sửa đối tượng:** lãnh đạo **PTSC Quảng Ngãi** (Giám đốc + phòng CNTT), không phải Ban TGĐ TCT hay Giám đốc các đơn vị L1–L4 | Xem mục 5a — dàn bài hiện tại nhắm sai khán giả |
| B2 | Thời lượng trình bày | **KHÔNG CÓ trong tài liệu** — do anh quyết | Đề xuất: 30–40 phút trình bày + 15 phút hỏi đáp (khớp dàn ý 18–20 slide đã soạn ngày 25/11) |
| B3 | Thông điệp chốt (Big Ask) | **KHÔNG CÓ trong tài liệu** — do anh quyết | Đề xuất: Giám đốc quyết 3 việc (ký giao đầu mối; chỉ định người phụ trách dữ liệu; đồng ý gửi văn bản hỏi TCT). Không xin phê duyệt ngân sách hay Governance 5 cấp (xem slide 10) |
| B4 | Tổng số hệ thống tại TCT & đơn vị | **Một phần:** GĐ1 = **8 phần mềm nguồn** tại CQTCT (deck chiều); Quảng Ngãi = **6 hệ thống** (danh sách làm việc của anh, chờ CNTT xác nhận). **Không có** con số tổng toàn TCT | Không bịa tổng số; ghi rõ phạm vi từng con số |
| B5 | Số ngày/giờ làm báo cáo thủ công | **KHÔNG CÓ trong tài liệu** — chỉ có mô tả định tính "báo cáo hợp nhất vẫn thủ công, chậm, không kịp thời" (deck chiều) | Bỏ khỏi slide; hoặc đo thực tế tại đơn vị rồi mới đưa số |
| B6 | Số đơn vị gặp lỗi lệch mã | **KHÔNG CÓ trong tài liệu** | Bỏ khỏi slide |
| B7 | Số lượng đơn vị theo cấp L1–L4 | **KHÔNG DÙNG ĐƯỢC:** deck ghi L1·5, L2·2, L3·13, L4·1 = 21, mâu thuẫn với "17 đơn vị" | **Không trích con số**; chỉ nói "17 đơn vị và chi nhánh, chốt sau khảo sát GĐ2A" |
| B8 | Tên đơn vị tiêu biểu theo cấp | **Một phần:** Nhóm 4 (đơn vị lớn, L3–L4): M&C, PPS, POS, **Quảng Ngãi**, Thanh Hóa; Nhóm 1: Văn phòng Hà Nội, Miền Trung, Petro Hotel, Long Phú; Nhóm 2: G&S, Supply Base, Marine; Nhóm 3: Phú Mỹ, Đình Vũ, Sao Mai Bến Đình, PVS An ninh dầu khí, Shipyard (deck chiều, slide in 51, trang PDF 56) | Dùng tên nhóm được, nhưng **mức L3/L4 của từng đơn vị chưa chốt** — M&C là ví dụ rõ nhất (đang thảo luận riêng) |
| B9 | Tiêu chí phân loại L1–L4 | **Có:** pháp nhân, quy mô, mức trưởng thành số (DBI); L1 DBI 0–2 dùng chung 100%; L2 DBI 0–2 dùng chung >70%; L3 DBI 2–3,5 + phân vùng tenant; L4 DBI >3,5 + tự đầu tư dHCI; 4 tiêu chí tốt nghiệp lên L4 (deck chiều, slide in 48–50) | Dùng nguyên văn |
| B10 | Phạm vi tích hợp & dữ liệu GĐ1 | **Có:** 8 hệ thống nguồn, 35 quy trình liên phòng ban, **50 API chuẩn**, **20 báo cáo BI tự động** (deck chiều + báo cáo kỹ thuật); 9 lĩnh vực dữ liệu chủ; 10 quy trình nghiệp vụ phải thiết kế tích hợp (HSYC Bảng 1) | Dùng được; ghi rõ "phạm vi Văn phòng TCT" |
| B11 | Ví dụ đầu ra tầng GOLD | **Có:** 5 bảng GOLD trong Data Kit POC (xem slide 04) | Dùng 5 tên bảng GOLD hoặc 20 báo cáo BI |
| B12 | Lộ trình Roll-out (mốc Quý/Năm) | **Có nhưng MÂU THUẪN:** GĐ1 2026–2027, GĐ2 2028+ (deck chiều) vs GĐ2 tại đơn vị 2026–2027 (deck sáng) vs roll-out đơn vị 2027 (PDT27, nháp chưa duyệt) vs go-live GĐ1 27/08/2026 (hợp đồng thật) | Trình bày 3 dòng riêng (đã xảy ra / sắp tới / chưa thống nhất) — xem slide 10 |
| B13 | Đơn vị thí điểm | **KHÔNG CÓ tên trong tài liệu** — chỉ nhắc chung chung "đơn vị thí điểm" (deck chiều) | Bỏ khỏi slide; PDT27 Nhóm 1 (5 chi nhánh + Petro Hotel) là đợt triển khai đầu, không phải đơn vị thí điểm |
| B14 | Chi phí CAPEX/OPEX (số tiền) | **KHÔNG CÓ trong tài liệu** — không một con số tiền dự án nào trong cả 7 nhóm tài liệu; khái toán chi tiết trình tại GĐ2A | Chỉ trình bày **cơ cấu 7 cấu phần chi phí** (deck chiều, slide in 57) + Phương án 3 (xem B15). Số dự toán L3/L4 của anh (năm đầu ~10 tỷ vs ~22 tỷ) là **giả định theo thực tế, ghi rõ là giả định, không phải số TCT** |
| B15 | Cơ chế chia sẻ OPEX/License, tỷ lệ | **Một phần:** Phương án 3 — TCT đầu tư Hub/nền tảng dùng chung/bản quyền khung/tiêu chuẩn; đơn vị đầu tư hoặc thuê Spoke + tích hợp nội bộ; đơn vị chưa có nguồn được TCT **đầu tư trước và ghi nợ**; cơ chế phân bổ cụ thể **xây dựng trong GĐ2A**. **Không có tỷ lệ hay con số nào** | Ghi đúng câu chữ Phương án 3; không bịa tỷ lệ |
| B16 | Tên chính thức dự án, bối cảnh, đơn vị chủ trì | **Có:** "Dự án Nền tảng dữ liệu (Data Platform) — Giai đoạn 1", mã **HDP26**, hợp đồng **1-2026/PTSC-CDS/HĐ**, chủ trì Ban Dự án Chuyển đổi số (PTSC-CDS), nhà thầu liên danh HIPT-AITS (slide kick-off) | Dùng nguyên văn; cấm tên "IMIP" |
| B17 | Số liệu hạ tầng Hub | **Có:** dHCI **8 node** (2 lưu trữ, 2 xử lý, 1 truy vấn+metadata, 1 quản trị+API, 1 SIEM+giám sát, 1 workflow+MDM); dữ liệu ban đầu **~40 TB**, mở rộng **200 TB+**; **70 người dùng** thường xuyên; **Microsoft Fabric Capacity F16, OneLake 20 TB, Purview 500 assets**, bản quyền 12 tháng (báo cáo kỹ thuật tr. 58–60/83 + HSYC Bảng 3 — F16 đã xác nhận bằng 2 tài liệu) | Dùng được; ghi cả 2 nguồn |
| B18 | Số báo cáo hiện có tại PTSC | **Có:** **310 báo cáo** (slide "Hiện trạng dữ liệu – Báo cáo tại PTSC", deck hội thảo) | Dùng cho slide 02 |
| B19 | Quy trình 2 chiều thực tế | **Có (dạng yêu cầu, không phải ví dụ chạy thật):** POC tiêu chí 3 (đồng bộ dữ liệu chủ qua tối thiểu 3 phần mềm); Phụ lục 02 §2 (luồng 2 chiều bắt buộc, API E-Office có tên: CreateTicket, ApproveSignEO, UpdateDocument, UpdateInvoice) | Dùng tiêu chí POC làm ví dụ; ghi rõ là yêu cầu nghiệm thu, chưa phải hệ thống đang chạy |

**Tổng kết checklist: 19 dòng — Có đầy đủ 7 dòng (B9, B10, B11, B16, B17, B18, B19), cộng B1 đã xác định lại đối tượng nghe từ ngữ cảnh; Một phần hoặc mâu thuẫn 5 dòng (B4, B7, B8, B12, B15); Không có đáp án trong tài liệu 6 dòng (B2, B3, B5, B6, B13, B14).**

---

## 4. DÀN BÀI ĐÃ CHỈNH SỬA HOÀN CHỈNH (10 SLIDE, GIỮ CẤU TRÚC SPARKLINE)

*Giữ nhịp Sparkline của bản gốc. Mỗi slide: tiêu đề → thông điệp cốt lõi (≤ 40 chữ) → dữ kiện dùng → ghi chú diễn giải (speaker notes).*

| # | Tiêu đề | Nhịp | Thông điệp cốt lõi | Dữ kiện dùng (có nguồn) |
|---|---|---|---|---|
| 01 | **Nền tảng dữ liệu PTSC — Giai đoạn 1** | Hook | Dự án Nền tảng dữ liệu (HDP26): biến dữ liệu phân mảnh thành tài sản dùng chung của toàn Tổng công ty. | Tên chính thức + mã HDP26 + hợp đồng 1-2026/PTSC-CDS/HĐ + liên danh HIPT-AITS (slide kick-off). **Không dùng tên "IMIP".** |
| 02 | **3 nỗi đau hiện tại** | What Is | 310 báo cáo rời rạc; báo cáo hợp nhất còn làm thủ công, chậm; mã dữ liệu chủ lệch nhau giữa các hệ thống. | 310 báo cáo (deck hội thảo); 8 hệ thống nguồn GĐ1 tại CQTCT (deck chiều); ví dụ minh họa NCC-001 vs KH-118 — ghi rõ là ví dụ minh họa. *Speaker note: không có số ngày làm báo cáo hay số đơn vị lệch mã trong tài liệu — đừng bịa.* |
| 03 | **Data Platform là gì?** | What Could Be | Không thay thế phần mềm cũ — DP là Nhà máy Lakehouse, Trục ESB và bộ ánh xạ mã chuẩn. | 6 hệ thống Quảng Ngãi vẫn giữ nguyên; PDT27: không làm lại quy trình đang chạy tốt. *Speaker note: "ánh xạ mã" = bảng 3 tầng (mã đơn vị → mã chuẩn TCT → mã chuẩn PVN); chuẩn quốc tế chỉ cho dữ liệu chuyên ngành.* |
| 04 | **3 lớp giá trị Lakehouse** | Proof | Dữ liệu thô (RAW) làm sạch qua SILVER thành GOLD — 5 bảng GOLD phục vụ dashboard và AI. | Pipeline RAW → SILVER → GOLD (yêu cầu POC + HSYC); 5 bảng GOLD trong Data Kit; 20 báo cáo BI tự động GĐ1. *Speaker note: "Bản ghi vàng" (Golden Record) là sản phẩm của MDM, khác với tầng GOLD — đừng đồng nhất hai khái niệm.* |
| 05 | **Một trục ESB duy nhất** | Relief | Một trục ESB tại Hub thay cho kết nối chằng chịt 1–1; dữ liệu chủ đồng bộ 2 chiều, mọi giao dịch ghi Audit Log. | Nguyên tắc một ESB dùng chung (Phụ lục 02 §1); luồng 2 chiều bắt buộc (Phụ lục 02 §2); tiêu chí POC: đồng bộ qua tối thiểu 3 phần mềm. *Speaker note: luồng đúng là hệ thống nguồn → ESB (Zone 5) → Landing Zone → Lakehouse; e-Office là hệ thống nguồn, không phải trạm trung gian.* |
| 06 | **Ánh xạ mã: giữ mã cũ, nói chuẩn quốc tế** | Insight | Giữ nguyên mã nội bộ (P3.ME); ánh xạ sang chuẩn quốc tế (NORSOK:ME = EXACT) — không đổi mã cũ. | P3.ME — NORSOK:ME = EXACT, bảng DISCIPLINE_CODE_XREF, độ tin cậy EXACT/PARTIAL/NONE (deck sáng, mục 3.2); chuẩn đối ứng: NORSOK Z-DP-002, ISO 15926/14224/19008, VSIC 2018, CFIHOS 2.0. *Speaker note: Dual-Code chỉ cho dữ liệu kỹ thuật/chuyên ngành; dữ liệu chủ 9 lĩnh vực dùng bảng ánh xạ 3 tầng. Deliverable D1–D8 là "hợp đồng" giữa các ngành, không nằm trong chuỗi ánh xạ mã.* |
| 07 | **Hub – Spoke – Tenant: đơn vị ở đâu?** | Solution | TCT đầu tư Hub trung tâm; đơn vị nhỏ dùng Tenant (0 CAPEX hạ tầng); đơn vị lớn đủ điều kiện mới tự chủ Spoke. | 17 đơn vị/chi nhánh, 4 nhóm; mức từng đơn vị chốt sau khảo sát GĐ2A (deck chiều, slide in 51); tiêu chí L1–L4 theo pháp nhân/quy mô/DBI + 4 tiêu chí tốt nghiệp lên L4; **không trích số lượng 5/2/13/1 (cộng ra 21 ≠ 17)**; **không nêu M&C làm ví dụ L4**. *Speaker note: Quảng Ngãi thuộc Nhóm 4 (đơn vị lớn, L3–L4) — chưa chốt; L3 là mặc định hợp lý, L4 chỉ khi có số liệu chứng minh.* |
| 08 | **Chủ quyền dữ liệu: ai sở hữu, ai vận hành?** | Trust | Đơn vị là chủ sở hữu dữ liệu — duyệt trước khi chia sẻ; TCT chỉ vận hành nền tảng, không sở hữu dữ liệu nghiệp vụ. | Cách ly RBAC/ABAC theo tenant; duyệt tại Landing Zone; audit log đổ về SIEM Hub; Cấp 5 (Ban NCPT & CĐS) không sở hữu dữ liệu nghiệp vụ (deck chiều). *Speaker note: đừng hứa "cách ly tuyệt đối" — dữ liệu dùng chung và tổng hợp vẫn lên Hub; giới hạn trung thực: tầng hạ tầng có khả năng truy cập về mặt lý thuyết, mọi truy cập đều có quyền, có mục đích, có dấu vết.* |
| 09 | **Đơn vị phải làm 4 việc** | Action | Đơn vị không phải code — chỉ cử người, mở cổng dữ liệu, duyệt chia sẻ và chịu phần chi phí của mình. | Cấp 3: Lãnh đạo đơn vị = Data Owner (trách nhiệm giải trình ở cấp này); Cấp 4: đầu mối từng miền dữ liệu (tối đa 9 miền); Tenant chỉ cần agent thu thập hoặc API; Phương án 3: TCT đầu tư trước, ghi nợ nếu đơn vị chưa có nguồn; cơ chế phân bổ xây dựng trong GĐ2A — **không có tỷ lệ**. *Speaker note: "5 cấp" là mô hình quản trị toàn TCT, không phải 5 đầu mối đơn vị phải cử.* |
| 10 | **Lộ trình & 3 quyết định xin trong buổi họp** | Urgency | Đã có: kick-off 04/03/2026, go-live GĐ1 27/08/2026. Sắp tới: đăng ký Combo/Nhóm tháng 12/2026. Còn lại: chờ TCT xác nhận. | 3 dòng thời gian riêng (đã xảy ra / sắp tới / chưa thống nhất); **GĐ2A không có ngày**; không có tên đơn vị thí điểm. 3 quyết định xin: (1) ký giao nhiệm vụ đầu mối; (2) chỉ định người phụ trách dữ liệu từng miền; (3) đồng ý gửi văn bản hỏi TCT. *Speaker note: nếu lãnh đạo hỏi "bao giờ xong?", trả lời: mốc mở rộng đơn vị chưa thống nhất giữa các tài liệu — đã đưa vào văn bản hỏi TCT.* |

---

## 5. HAI GHI CHÚ KHUNG

### 5a. Đối tượng nghe — viết lại phần mở đầu cho lãnh đạo đơn vị Quảng Ngãi
Dàn bài gốc nhắm **"Ban Lãnh đạo PTSC & Lãnh đạo Đơn vị thành viên"** — tức là lãnh đạo cấp Tổng công ty cộng với Giám đốc các đơn vị. Nhưng nhu cầu thật của anh là **thuyết trình cho lãnh đạo đơn vị Quảng Ngãi** (Giám đốc đơn vị + phòng CNTT), người **không theo dõi chi tiết DP** và chính anh là người thông tin cho ông ấy. Hai khán giả này cần hai bài khác nhau:
- **Bài cho lãnh đạo Quảng Ngãi (bài này):** trọng tâm là "đơn vị mình phải làm gì, tốn bao nhiêu (dự toán), quyết cái gì trong buổi họp" — 6 hệ thống của đơn vị, đăng ký Combo/Nhóm tháng 12, 3 quyết định xin ngay. Bớt phần kiến trúc tổng thể TCT, tăng phần việc của đơn vị.
- **Bài cho lãnh đạo TCT (nếu anh thực sự cần):** trọng tâm là rollout 17 đơn vị, Phương án 3, cơ chế ghi nợ, mốc GĐ2/GĐ2A — và phải nói rõ các tài liệu chưa thống nhất về mốc thời gian. Đây là một bài khác, không phải chỉ đổi tiêu đề.
- **Quyết định cần anh chốt:** bài này là bài cho lãnh đạo Quảng Ngãi (theo mục 4). Nếu anh muốn bài cho TCT thì nói em, em soạn dàn bài riêng.

### 5b. Thiết kế — nên dùng slide trắng công sở, không dùng Tech Dark Mode
- **Quy tắc đứng của anh cho slide lãnh đạo:** PowerPoint chỉnh sửa được, nền trắng, header xanh đậm, bảng Calibri trơn, ghi chú nguồn chính xác ở chân slide, footer đơn vị. Dàn bài gốc đề xuất **"Tech Dark Mode × Swiss Grid"** + Chart.js + HTML — **trái với quy tắc này**.
- **Lý do thực tế, không phải gu thẩm mỹ:** (1) anh từng chê giao diện tối là "hơi tối tăm quá" và đã phải làm lại bản sáng; (2) lãnh đạo đơn vị đọc slide in giấy và chiếu máy chiếu phòng họp — nền tối khó đọc, khó in; (3) slide HTML/Chart.js không chỉnh sửa được bằng PowerPoint như lãnh đạo quen dùng, và khó đưa vào hồ sơ giấy tờ của đơn vị.
- **Giữ lại được từ dàn bài gốc:** kỷ luật **mỗi slide < 40 chữ** (tốt — giữ), cấu trúc **Sparkline** (tốt — giữ), dùng số liệu nổi bật làm hero metric (giữ, nhưng chỉ dùng số có nguồn). Bỏ: nền tối, Chart.js/HTML, bố cục bất đối xứng Swiss Grid.
- **Đề xuất cụ thể:** PowerPoint trắng, header #1F4E79, tiêu đề #1F3864, Calibri, mỗi slide 1 ý chính + 1 số liệu hero (có nguồn) + 1 sơ đồ đơn giản; chi tiết dài chuyển hết vào Speaker Notes (đúng như Part B mục 3.4 của dàn bài gốc đã đề xuất).

---

