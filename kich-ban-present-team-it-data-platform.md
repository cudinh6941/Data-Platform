# HƯỚNG DẪN PRESENT DATA PLATFORM TRƯỚC TEAM I&T (PTSC QUẢNG NGÃI)

> **Thời lượng gợi ý:** ~40–45 phút (15–20 phút Phần 1 · 20–25 phút Phần 2 & Chốt đầu mối)
> **Tài liệu mở sẵn trên máy:**
> - **Phần 1 (Hệ thống TCT):** `20260810_Slide_Hoi thao Data Platform_Phien Sang.pdf` & `20260810_Slide_Hoi thao Data Platform_Phien Chieu.pdf`
> - **Phần 2 (Mô hình dự kiến PQN):** `slide-thuyet-trinh-lanh-dao-data-platform-quang-ngai.html` (mở sẵn **Slide 08**) + `slide-ky-thuat-data-platform-quang-ngai.html` (**S13 → S19**)

---

## PHẦN 1 — HỆ THỐNG DATA PLATFORM CỦA TỔNG CÔNG TY (15–20 phút)
*(Nguyên tắc: dùng file PDF gốc của TCT nhưng **nhảy thẳng vào các trang trọng tâm**, không lật tuần tự hết 100+ trang.)*

| Thứ tự | Nội dung cần nói với team I&T | File & Trang PDF TCT | Điểm nhấn nhanh |
|---|---|---|---|
| 1 | **Hành trình dữ liệu & Tech Stack Hybrid** *(On-Prem tầng 10 TCT + Cloud Fabric)* | `Phien Sang.pdf` — **tr. 14** *(và phần 3 tầng RAW/SILVER/GOLD tr. 29–31)* | Nói rõ tách lớp: On-Prem xử lý/lưu dữ liệu gốc (dHCI, Iceberg, Trino/Flink, WSO2 ESB, Debezium/Airbyte, MDM); Cloud Fabric F16 chỉ nhận dữ liệu tổng hợp/chuẩn hóa cho BI & AI. |
| 2 | **Landing Zone, QC & Kiểm soát dữ liệu** | `Phien Sang.pdf` — **tr. 23–24** | 100% gói qua QC (dbt/Great Expectations), có bước Data Owner bấm Approve/Reject; lỗi/từ chối giữ ở vùng cách ly, trả ticket về nguồn sửa. |
| 3 | **Kiến trúc an ninh 10 vùng (Security Zones)** | `Phien Sang.pdf` — **tr. 25** | Chỉ rõ Data Platform nằm ở **Vùng 4**, trục tích hợp ESB nằm ở **Vùng 5**, SIEM giám sát ở **Vùng 3**. |
| 4 | **Chuẩn hóa mã: Ánh xạ 3 tầng & PPDM Dual-Code** | `Phien Sang.pdf` — **tr. 36–39** *(cùng slide MDM tr. 52 Phiên Chiều)* | Tách bạch 9 miền dữ liệu chủ (Đơn vị → TCT → PVN, giữ nguyên mã đơn vị) và dữ liệu kỹ thuật (`P3.ME ↔ NORSOK:ME`). |
| 5 | **Quản trị 5 cấp & Mô hình Hub–Spoke–Tenant (L1–L4)** | `Phien Chiều.pdf` — **tr. 38, 46, 52, 55–59** *(cơ chế chi phí tr. 62–63)* | Đơn vị chỉ nắm **Cấp 3 (Data Owner)** và **Cấp 4 (Data Steward)**; PQN thuộc **Nhóm 4 (L3–L4, chưa chốt)** — chốt sau khảo sát GĐ2A. |

> **Câu chuyển sang Phần 2:** *"Đó là khung chung của TCT. Giờ mình hạ xuống bài toán thực tế tại **PTSC Quảng Ngãi**: 6 hệ thống của mình sẽ nối vào đó thế nào, L3 hay L4 ảnh hưởng gì tới team I&T, và tuần tới đoàn 30/11 vào thì mỗi anh em phụ trách phần nào."*

---

## PHẦN 2 — HỆ THỐNG DỰ KIẾN & MÔ HÌNH CỦA PTSC QUẢNG NGÃI (20–25 phút)

### Bước 1 · Chiếu luồng tổng thể của PQN *(3–5 phút)*
- Mở **Slide 08 — Bức tranh tổng (Sơ đồ động)** trong `slide-thuyet-trinh-lanh-dao-data-platform-quang-ngai.html`.
- Bấm lần lượt **4 nút luồng** (`1 · Đi lên`, `2 · Đi xuống`, `3 · Giám sát`, `4 · Từ chối ở LZ`) để anh em I&T thấy rõ:
  - 6 hệ thống nguồn PQN (**Cảng · ERP FAST · MESX · Bán hàng · E-Office · HRM**) → SD-WAN/VPN → **1 trục ESB duy nhất tại Hub TCT** (PQN không có ESB riêng).
  - E-Office là **nguồn ngang hàng** qua API thật; bảo dưỡng nằm trong **MESX**.

### Bước 2 · Chi tiết thiết kế & triển khai L3 vs L4 tại PQN *(8–10 phút)*
- Chuyển sang `slide-ky-thuat-data-platform-quang-ngai.html` và đi lần lượt **S13 → S17**:
  - **S13 (Thiết kế hệ thống L3 Tenant):** 6 PM tại PQN + VM Agent nhẹ → SD-WAN/VPN mTLS (dòng gói dày) → Vùng 5 ESB & Landing Zone riêng → Vùng 4 Tenant PQN (RBAC/ABAC) → Fabric Workspace.
  - **S14 (Chi tiết chuẩn bị & làm theo L3):** 3 mảng cụ thể của team I&T: (1) đo WAN, mở firewall/mTLS, cấp VM Agent; (2) mở read-only/Transaction Log, retention đủ dài, gắn nhãn PII; (3) vận hành Landing Zone (Ticket sửa nguồn + Approve/Reject) & ánh xạ mã. Nhấn mạnh 0 mua dHCI, 0 trực K8s/Storage lõi.
  - **S15 (Thiết kế hệ thống L4 Spoke):** Nếu đủ 4 tiêu chí (`DBI > 3,5`), đặt cụm dHCI/Lakehouse/Storage ngay tại phòng máy PQN để xử lý chi tiết/OT tại chỗ, chỉ đẩy tổng hợp qua WAN (dòng thưa) — nhưng **không có Hub/ESB riêng**.
  - **S16 (Làm thêm gì khi lên L4):** Đầu tư cụm dHCI + SAN + Backup/DR tại chỗ, tự trực vận hành 24/7 K8s/MinIO/Iceberg/Patching theo SLA TCT.
  - **S17 (Ma trận đối chiếu L3 vs L4):** So sánh 7 tiêu chí (kể cả ước tính tham khảo ~16,8 tỷ vs ~40,4 tỷ trong 5 năm) để team I&T tự đánh giá năng lực.

### Bước 3 · Rà tác động kỹ thuật & Chốt đầu mối 6 hệ thống *(8–10 phút)*
- Mở **S18 (Tác động kỹ thuật lên 6 hệ thống tại PTSC Quảng Ngãi)**.
- Đi từng dòng từ 1 → 6 để **chốt tại chỗ trong buổi họp**:
  1. **Tên đầu mối IT PQN** phụ trách từng hệ thống *(điền vào cột `[Chốt tên IT]`)*.
  2. **DB engine / Server hiện tại** *(SQL Server, Oracle, API...)* — xem hệ thống nào bật được Debezium CDC (đọc Transaction Log), hệ thống nào phải dùng Airbyte/API.
  3. **Rà phần mềm cũ / hệ thống ngưng hoạt động** xem còn dữ liệu lịch sử cần giữ hay đối chiếu không.

### Bước 4 · Chốt việc làm trước 30/11 & 5 câu hỏi hỏi đoàn TCT *(5 phút)*
- Mở **S19 (Checklist 73 mục & 5 câu hỏi kỹ thuật)**.
- Thống nhất 3 đầu việc tuần sau trước khi đoàn khảo sát TCT vào:
  1. Chốt danh sách **6 hệ thống × 3 đầu mối** (Key user + IT + Kỹ thuật).
  2. Hoàn thiện **8 phần / 73 mục khảo sát**.
  3. Chuẩn bị sẵn tài khoản read-only/log (để test kết nối, không đụng DB sản xuất giờ cao điểm) và thông số SD-WAN/VPN.
- Thống nhất **5 câu hỏi kỹ thuật** sẽ hỏi thẳng đoàn TCT ngày 30/11 (tiến độ thật GĐ1 sau mốc 27/08/2026, phương thức CDC vs Airbyte từng PM, cơ chế duyệt batch vs row-level & SLA ở Landing Zone, danh sách SAP S/4HANA & spec API ESB, ngưỡng sizing L3 vs L4).
