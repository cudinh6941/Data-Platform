# DÀN Ý BỘ WEB SLIDE ĐẦY ĐỦ (15 SLIDE) — THEO DẤU HÀNH TRÌNH DỮ LIỆU

*Thiết kế theo mạch kể chuyện **Micro → Hệ thống → Tổng quan → Đánh đổi với Đơn vị chủ quản**, giao diện **Industrial Dark Mode (`#060B19`, Glassmorphism 1px Cyan & Cam)** với luồng hạt dữ liệu chạy động và tương tác sáng đèn từng thành phần. Thuần giải thích bản chất cho Lãnh đạo khối Kinh tế, không đặt yêu cầu ra quyết định.*

---

## PHẦN I · MICRO (MỔ XẺ TỪNG CƠ CHẾ BÊN TRONG — SLIDE 01 ĐẾN 07)
1. **Slide 01 — Điểm xuất phát & `Debezium CDC` / `Airbyte`:** Chứng từ lưu ở `6 hệ thống` nguồn → `Transaction Log` → `CDC` hút nhẹ không làm chậm máy kế toán (toggle *Query thẳng ↔ CDC*).
2. **Slide 02 — Tổng đài `ESB` (`WSO2 / Camel`) & `Idempotency`:** `E-Office` là nguồn ngang hàng; vào Zone 5 gắn `CorrelationId`, lọc `Idempotency` chống trùng khi lag mạng, đồng bộ 2 chiều (`50 API`, `35 quy trình`).
3. **Slide 03 — Vùng đệm `Landing Zone` & Bộ lọc `QC` (`dbt / Great Expectations`):** Gói sạch chờ `Data Owner` bấm `Approve` qua `SILVER`; gói lỗi rẽ nhánh về vùng cách ly sửa ở nguồn.
4. **Slide 04 — Kho `Lakehouse` (`Apache Iceberg / Parquet`) & `Time-Travel`:** Lưu ảnh chụp bất biến + đọc nhanh qua `Trino / ClickHouse / Spark / Flink`; kéo thanh `Time-Travel` kiểm toán quá khứ.
5. **Slide 05 — Chuỗi `RAW → SILVER → GOLD` & `5 Bảng GOLD`:** Làm rõ cấu trúc 3 lớp xử lý, 5 bảng GOLD POC (`golden_*`) và phân tách **Tầng GOLD ≠ Bản ghi vàng (MDM)**.
6. **Slide 06 — `MDM` (10 chức năng) & Phép gộp “Bản ghi vàng”:** 3 mã lệch (`NCC-001`, `KH-118`, `DT-09` minh họa) → `Matching + Survivorship` + `Soft-delete` → **1 Golden Record** đẩy ngược về nguồn qua ESB.
7. **Slide 07 — Bộ phiên dịch mã (`Ánh xạ 3 tầng` & `PPDM Dual-Code`):** Tách rõ **9 lĩnh vực dữ liệu chủ** (`Đơn vị → TCT → PVN`) và **Kỹ thuật chuyên ngành** (`DISCIPLINE_CODE_XREF`: `P3.ME ↔ NORSOK:ME = EXACT`, `Deliverable D1–D8`).

## PHẦN II · HỆ THỐNG (KẾT NỐI THÀNH DÂY CHUYỀN & VỎ BẢO VỆ — SLIDE 08 ĐẾN 10)
8. **Slide 08 — Dây chuyền 5 Trạm Hợp nhất (`End-to-End 2 chiều`):** Ghép Slide 01–07 thành 1 bảng mạch chạy hạt liên hoàn kèm dòng hồi lưu Bản ghi vàng về phần mềm gốc.
9. **Slide 09 — Lớp vỏ An ninh 4 Tầng (`Landing Zone · RBAC · Purview DLP · SIEM`):** Tích hợp cơ chế cảnh báo SIEM thật (*login fail 5 lần/2 phút*, *cấp role DBA bất thường tự tạo ticket*) & Luật `91/2025/QH15`.
10. **Slide 10 — Tổ chức Con người Vận hành (Mô hình Quản trị 5 Level):** Cấp 1 (HĐQT/TGĐ), Cấp 2 (Khối), **Cấp 3 (Lãnh đạo Đơn vị = Data Owner, chịu accountability)**, **Cấp 4 (Đầu mối tối đa 9 miền)**, Cấp 5 (Ban NCPT & CĐS — vận hành kỹ thuật, không sở hữu dữ liệu nghiệp vụ).

## PHẦN III · TỔNG QUAN (BỨC TRANH MACRO HYBRID & ĐẦU RA — SLIDE 11 ĐẾN 13)
11. **Slide 11 — Kiến trúc Vật lý Hybrid (`On-Prem 8 Node dHCI` + `Fabric Cloud`):** Dữ liệu nhạy cảm/cốt lõi ở lại Tầng 10 (`8 node dHCI`, `~40 TB → 200 TB+`); Cloud (`Fabric F16 / OneLake 20 TB`, `70 người dùng`) chỉ nhận dữ liệu tổng hợp & chuẩn hóa.
12. **Slide 12 — Mô hình Tổng thể `Hub – Spoke – Tenant` (`17 Đơn vị / 4 Nhóm` & Tiêu chí `L1–L4`):** Tương tác click khối `Tenant L1–L3`, `Spoke L4` (`4 tiêu chí, DBI > 3,5`), `ESB`, `Hub`; vị trí **Nhóm 4 (Quảng Ngãi: L3–L4, chốt sau khảo sát GĐ2A)**.
13. **Slide 13 — Đầu ra trên Bàn Sếp (`20 BI` · `Text-to-Data` · `Catalog Lineage`):** Thử hỏi tiếng Việt truy vấn `5 bảng GOLD` và xem truy vết nguồn gốc dữ liệu tiếng Việt trên Purview.

## PHẦN IV · ĐÁNH ĐỔI VỚI ĐƠN VỊ CHỦ QUẢN (SLIDE 14 ĐẾN 15)
14. **Slide 14 — Chi phí Thực tế (`L1–L4`) & Cơ chế Phương án 3:** Ma trận chi phí 7 hạng mục theo Phiên chiều P62 (`L3` không mất dHCI nhưng vẫn trả license, triển khai, tích hợp & vận hành phân bổ; thiếu ngân sách TCT ứng trước & ghi nợ; cơ chế phân bổ xây ở GĐ2A).
15. **Slide 15 — Tổng kết Bài toán Đánh đổi (Lợi ích ↔ Hạn chế & Lộ trình 3 Dải):** Trình bày thẳng thắn 3 lợi ích, 3 hạn chế/ràng buộc vận hành và bức tranh lộ trình 3 dải (*Đã diễn ra: 04/03 & 27/08/2026 · Dự kiến PDT27: Combo 12/2026 · Chưa thống nhất: GĐ2 & ngày khảo sát GĐ2A*).
