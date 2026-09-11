# BÁO CÁO RÀ SOÁT TÀI LIỆU TCT SỐ 02
## Tên tài liệu: Báo Cáo Đề Xuất Mô Hình Kiến Trúc Giải Pháp Nền Tảng Dữ Liệu Kết Hợp (Hybrid Data Platform)
* **Tên file gốc:** `Slide Tóm tắt lựa chọn giải pháp Hybrid Data Platform PTSC.pdf` (59 trang)
* **Đơn vị soạn thảo:** Tổ Dữ liệu - Ban Dự án Chuyển đổi số PTSC.
* **Mục đích tài liệu:** Trình bày căn cứ chiến lược, phân tích hiện trạng bất cập, so sánh các mô hình kiến trúc công nghệ trên thị trường và bảo vệ quyết định lựa chọn mô hình **Hybrid Data Platform (Multi-site, Multi-cloud)** trước Ban Lãnh đạo Tổng công ty.

---

### 1. Hiện Trạng & Điểm Nghẽn Cốt Lõi Về Dữ Liệu Tại PTSC (Giai đoạn 2024 - 2026)
Tài liệu chỉ ra 4 "nỗi đau" (pain points) lớn nhất của PTSC trước khi có Data Platform:
1. **Dữ liệu phân mảnh và cô lập (Silo Data):** PTSC có hơn 310 danh mục báo cáo khác nhau nhưng dữ liệu nằm rải rác trên nhiều phần mềm độc lập, bảng tính cá nhân hoặc hệ thống kế toán, nhân sự riêng lẻ.
2. **Quy trình tổng hợp báo cáo thủ công qua SharePoint/OneDrive:** Dữ liệu đầu vào cho Power BI chủ yếu được tải lên các thư mục Excel trên Microsoft 365 SharePoint, phụ thuộc hoàn toàn vào con người cập nhật, dễ sai lệch và thiếu tính thời gian thực.
3. **Master Data quản lý thủ công:** Dữ liệu danh mục dùng chung (Mã khách hàng, Mã nhà cung cấp, Mã dự án, Danh mục tài sản, Cơ cấu tổ chức) đang quản lý bằng các file Excel trên SharePoint, dẫn đến tình trạng "một đối tượng có nhiều mã khác nhau" giữa TCT và các ĐVTV.
4. **Nguy cơ rò rỉ và thiếu an toàn an ninh dữ liệu:** Khi dữ liệu chưa được gom về một mối có kiểm soát phân quyền chặt chẽ, việc gửi các file Excel qua email, Zalo hay lưu trữ cá nhân vi phạm nghiêm trọng các chuẩn mực ATTT và Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân.

---

### 2. So Sánh 3 Mô Hình Kiến Trúc & Lý Do Chọn "Hybrid Data Platform"
TCT đã so sánh chi tiết 3 mô hình Data Platform phổ biến trên thế giới:

| Tiêu Chí So Sánh | 1. On-Premise Data Platform | 2. Pure Cloud Data Platform | 3. Hybrid Data Platform (Lựa chọn của PTSC) |
| :--- | :--- | :--- | :--- |
| **Bản chất hạ tầng** | 100% đặt tại Data Center của PTSC. | 100% thuê dịch vụ Public Cloud (Azure, AWS, GCP). | Kết hợp Data Center nội bộ (Core Lakehouse) và Public Cloud (AI, Text-to-Data, BI). |
| **Chi phí đầu tư (TCO)** | CAPEX ban đầu rất lớn (mua sắm phần cứng, SAN, máy chủ); khấu hao 5 năm. | CAPEX thấp nhưng OPEX hàng tháng tăng phi mã theo lưu lượng đọc/ghi và dung lượng lưu trữ. | **Tối ưu TCO:** Tận dụng hạ tầng on-premise sẵn có cho dữ liệu nền tảng lớn; dùng Cloud cho các tác vụ cần co giãn tức thời. |
| **Tuân thủ pháp lý (Compliance)** | Rất cao, đáp ứng tuyệt đối lưu trữ dữ liệu dầu khí và an ninh nội bộ tại Việt Nam. | Rủi ro lưu trữ dữ liệu xuyên biên giới nếu dùng Cloud nước ngoài; chi phí Cloud nội địa cao. | **Đạt chuẩn 100%:** Dữ liệu nhạy cảm lưu on-prem; dữ liệu phi nhạy cảm, phục vụ AI/Text-to-Data đưa lên Cloud. |
| **Khả năng kiểm soát & Chống khóa nhà cung cấp** | Tự chủ hoàn toàn mã nguồn mở, không bị Vendor khóa chặt. | Rất dễ bị phụ thuộc vào hệ sinh thái độc quyền của một hãng Cloud (Vendor Lock-in). | **Đa đám mây (Multi-cloud):** Kiến trúc mở (Open Lakehouse formats: Iceberg/Delta Lake, Trino, MinIO), dễ chuyển dịch. |
| **Năng lực mở rộng (Scalability)** | Chậm chạp, mỗi lần nâng cấp phải đấu thầu mua phần cứng mới (mất vài tháng). | Cực kỳ nhanh, chỉ cần vài cú click chuột để tăng vCPU/RAM. | **Linh hoạt:** Khi phát sinh bài toán phân tích lớn đột xuất hoặc mô hình AI nặng, có thể mở rộng ngay trên Cloud. |

---

### 3. Bộ 6 Nguyên Tắc Vàng Lựa Chọn Giải Pháp Kỹ Thuật
Ban dự án TCT xác lập 6 nguyên tắc bất di bất dịch định hình toàn bộ thiết kế hệ thống:
1. **Tuân thủ pháp lý về bảo vệ dữ liệu:** Tuân thủ Luật An ninh mạng 2018, Nghị định 53/2022/NĐ-CP (lưu trữ dữ liệu tại Việt Nam) và Nghị định 13/2023/NĐ-CP (Bảo vệ dữ liệu cá nhân - PDPD).
2. **Quyền sở hữu và toàn quyền kiểm soát CSDL:** PTSC phải sở hữu 100% dữ liệu, schema, logic chuyển đổi; các nhà cung cấp phần mềm không được khóa chặt CSDL hoặc đòi phí trích xuất phi lý.
3. **Kiến trúc mô hình dữ liệu hiện đại và linh hoạt:** Sử dụng công nghệ Datalakehouse, tách biệt Compute và Storage, hỗ trợ đồng thời xử lý hàng loạt (Batch) và luồng dữ liệu thời gian thực (Streaming/CDC).
4. **Đảm bảo khả năng chuyển đổi, tái sử dụng và mở rộng (Scalability & Reusability):** Thiết kế dạng module hóa, cho phép các Đơn vị Thành viên cắm/rút hệ thống mà không làm gián đoạn toàn bộ nền tảng.
5. **Đảm bảo An toàn thông tin (Bảo mật - Toàn vẹn - Sẵn sàng theo chuẩn ISO 27001):** Phân vùng mạng nghiêm ngặt, mã hóa dữ liệu khi truyền (In-transit: TLS/mTLS) và khi lưu trữ (At-rest: AES-256), tích hợp IAM tập trung.
6. **Bám sát lộ trình Chiến lược Chuyển đổi số PTSC (2024 - 2035):** Trở thành bệ phóng cho các bài toán tối ưu hóa vận hành, quản trị dự án EPC, dịch vụ tàu dịch vụ dầu khí, cảng biển và năng lượng tái tạo ngoài khơi (Offshore Wind).

---

### 4. Ý Nghĩa & Khuyến Nghị Trọng Tâm Cho PTSC Quảng Ngãi
1. **Định hướng công nghệ đồng nhất:** PTSC Quảng Ngãi không nên đầu tư một kho dữ liệu độc lập, khép kín, công nghệ dị biệt; thay vào đó, hạ tầng dữ liệu tại Quảng Ngãi phải tuân thủ chuẩn Hybrid Data Platform mà TCT đã vạch ra.
2. **Giải bài toán chi phí (CAPEX vs OPEX):** Nhận thức rõ chiến lược TCT chọn Hybrid giúp Quảng Ngãi tránh bẫy chi phí Cloud đắt đỏ hàng tháng, tận dụng máy chủ nội bộ kết hợp kênh truyền VPN về TCT.
3. **Chuẩn bị dữ liệu sạch cho Master Data:** Tài liệu nhấn mạnh việc xóa bỏ "Excel-based Master Data". Quảng Ngãi cần khẩn trương rà soát lại các bộ mã danh mục nội bộ (Mã vật tư FAST, Mã nhân sự, Mã dự án chế tạo) để sẵn sàng khớp nối với trục MDM của TCT.
