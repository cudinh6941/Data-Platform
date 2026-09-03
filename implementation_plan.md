# Kế hoạch triển khai Data Platform tại PTSC Quảng Ngãi (Vai trò: L3 Spoke)

Chào bạn, dựa trên tài liệu `Overview.md` và các tài liệu của Tổng công ty (TCT), mình xin tóm tắt lại vai trò của PTSC Quảng Ngãi một cách dễ hiểu nhất:

**PTSC Quảng Ngãi KHÔNG cần phải tự xây một hệ thống Data Platform to lớn (không cần mua server lưu trữ khủng).** 
Thay vào đó, Quảng Ngãi đóng vai trò là một **"Trạm thu phí & Bơm dữ liệu" (Data Integration Gateway)**. 
Nhiệm vụ chính của Quảng Ngãi là: 
1. Lấy dữ liệu từ các phần mềm đang dùng tại Quảng Ngãi (Nhân sự, Kế toán, Vật tư...).
2. "Gọt giũa" lại dữ liệu cho đúng chuẩn của Tổng công ty (ánh xạ theo 29 danh mục Master Data).
3. Bơm dữ liệu đó lên "Đám mây/Hệ thống trung tâm" (Hub) của Tổng công ty thông qua một đường mạng bảo mật.
4. Sau đó, nhân sự Quảng Ngãi sẽ được cấp tài khoản để lên hệ thống trung tâm đó xem báo cáo (qua Power BI).

Để làm được việc này, chúng ta cần đi từng bước. Dưới đây là kế hoạch chi tiết và những thông tin mình cần bạn cung cấp để làm rõ ngữ cảnh.

## Open Questions (Câu hỏi khảo sát hiện trạng)

> [!IMPORTANT]
> Để lên được phương án kỹ thuật chi tiết cho Giai đoạn 1 và 2, bạn hãy giúp mình trả lời các câu hỏi sau về hiện trạng tại PTSC Quảng Ngãi nhé:

1. **Về Hệ thống dữ liệu hiện tại (Source Systems):**
   - Hiện tại PTSC Quảng Ngãi đang dùng những phần mềm nội bộ nào (Ví dụ: Phần mềm Kế toán FAST/Bravo, Phần mềm Nhân sự, Quản lý vật tư...)? 
   - Các phần mềm này đang dùng hệ quản trị cơ sở dữ liệu gì (SQL Server, Oracle, MySQL, Excel...)? Có được phép truy cập trực tiếp vào Database không hay phải qua API?

2. **Về Chuẩn hóa dữ liệu (Master Data):**
   - Bạn đã nhận được tài liệu chi tiết về **"29 danh mục Master Data"** (ví dụ: quy định mã nhân viên, mã phòng ban, mã vật tư) từ Tổng công ty chưa? 

3. **Về Hạ tầng mạng & Server (Infrastructure):**
   - Đội ngũ IT nội bộ của Quảng Ngãi có sẵn sàng cấp phát 1-2 máy chủ ảo (VM) để cài đặt các tool hút dữ liệu (ETL) không? Cấu hình dự kiến ra sao?
   - Đường truyền mạng kết nối từ Quảng Ngãi ra Tổng công ty (Tầng 10 CQTCT) hiện nay đã có VPN Site-to-Site hay SD-WAN chưa?

4. **Về Nguồn lực triển khai:**
   - Quảng Ngãi dự kiến tự làm (in-house) phần "Hút và đẩy dữ liệu" này hay sẽ thuê đối tác (vendor) bên ngoài vào làm (theo Giai đoạn 2 của roadmap có nhắc đến Outsource)?

---

## Proposed Changes (Kế hoạch hành động đề xuất)

Dựa trên roadmap chung, công việc của PTSC Quảng Ngãi sẽ được chia làm 3 giai đoạn chính. Hiện tại, chúng ta sẽ tập trung giải quyết **Giai đoạn 1**.

### Giai đoạn 1: Khảo sát & Chuẩn bị hạ tầng (Focus hiện tại)
*Thực hiện bởi: Đội IT nội bộ PTSC Quảng Ngãi.*

- **Bước 1. Lập danh sách CSDL (Data Cataloging):** Thống kê lại toàn bộ các nguồn dữ liệu đang có (như đã hỏi ở câu 1). Xác định xem dữ liệu nào cần đẩy lên TCT.
- **Bước 2. Ánh xạ dữ liệu (Data Mapping):** Lấy dữ liệu thực tế tại Quảng Ngãi đối chiếu với 29 danh mục Master Data của TCT. Nếu mã vật tư ở Quảng Ngãi khác mã TCT, cần lập một bảng quy đổi (Mapping Table).
- **Bước 3. Chuẩn bị Network:** Phối hợp với IT Tổng công ty để thiết lập kênh truyền VPN an toàn từ Quảng Ngãi ra TCT (tuân thủ quy hoạch 8 Zones).

### Giai đoạn 2: Xây dựng Trạm trung chuyển dữ liệu (ETL Server)
*Thực hiện: IT Quảng Ngãi phối hợp cùng đối tác/nhà thầu.*

- **Bước 1:** Cài đặt 1 server ảo (VM) tại Quảng Ngãi.
- **Bước 2:** Cài đặt phần mềm tích hợp dữ liệu (như Airbyte, dbt, hoặc viết script Python).
- **Bước 3:** Tạo các "luồng" (pipeline) để tự động hút dữ liệu từ DB Quảng Ngãi -> lọc & đổi mã -> đẩy lên hệ thống của TCT (Workspace L3).
- **Bước 4:** Lên lịch (Schedule) cho luồng này chạy tự động (ví dụ: mỗi đêm chạy 1 lần).

### Giai đoạn 3: Xây dựng Báo cáo & Phân quyền
*Thực hiện: IT và người dùng nghiệp vụ (Business Users).*

- **Bước 1:** Nhận tài khoản quản trị Workspace của Quảng Ngãi trên hệ thống Microsoft Fabric / Power BI của TCT.
- **Bước 2:** Phân quyền cho nhân sự Quảng Ngãi (ai được xem báo cáo nào).
- **Bước 3:** Dùng Power BI kéo thả dữ liệu để tạo ra các Dashboard báo cáo phục vụ cho Ban Giám đốc Quảng Ngãi.

## Verification Plan

Sau khi bạn trả lời các câu hỏi trên, mình sẽ hỗ trợ bạn:
1. Lên cấu trúc bảng Mapping (Ánh xạ dữ liệu).
2. Lựa chọn công nghệ ETL phù hợp (Ví dụ nếu tự làm thì có thể dùng Python, Airbyte).
3. Lập danh sách các task công việc chi tiết (To-do list) để bạn dễ dàng theo dõi và báo cáo tiến độ.
