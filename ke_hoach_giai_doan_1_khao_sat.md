# KẾ HOẠCH HÀNH ĐỘNG CHI TIẾT - GIAI ĐOẠN 1
**Trọng tâm: Khảo sát hệ thống và Chuẩn hóa dữ liệu (Master Data)**

Giai đoạn này là nền tảng (nguyên liệu) cho toàn bộ dự án. Làm tốt Giai đoạn 1 thì Giai đoạn 2 mới có thể tự động hóa được.

## 1. Mục tiêu
* Có cái nhìn toàn cảnh về dữ liệu hiện tại của đơn vị (Data Catalog).
* Hoàn thành bộ "Từ điển" (Bảng ánh xạ/Mapping Table) để khớp mã của Quảng Ngãi với 29 danh mục Master Data của Tổng công ty.

## 2. Nhân sự tham gia
* **Đội IT (Kỹ thuật):** Phụ trách khảo sát cấu trúc hệ thống, kiểm tra khả năng trích xuất dữ liệu.
* **Key Users (Nghiệp vụ):** Kế toán trưởng, Trưởng phòng Nhân sự, Trưởng phòng Vật tư... chịu trách nhiệm rà soát và chốt quy tắc đổi mã dữ liệu.

## 3. Các bước thực hiện cụ thể

### Bước 1.1: Thống kê và lập danh mục nguồn dữ liệu (Data Catalog)
* **IT** lập danh sách toàn bộ các phần mềm đang vận hành (Ví dụ: FAST, Bravo, HRM, Phần mềm nội bộ tự viết...).
* Trả lời các câu hỏi kỹ thuật cho từng phần mềm:
  * Hệ quản trị CSDL là gì? (SQL Server, MySQL, Oracle...)
  * Dữ liệu lưu trên máy chủ nào? Có quyền truy cập Admin không?
  * Đơn vị cung cấp phần mềm có cho phép chọc thẳng vào Database không, hay phải xin mở cổng API?

### Bước 1.2: Đối chiếu và lập Bảng Ánh xạ Master Data (Mapping)
* **IT** xuất (export) toàn bộ danh sách mã nhân viên, mã vật tư, mã phòng ban, mã dự án... từ các phần mềm hiện tại ra Excel.
* **Key Users** dùng file Excel đó, đối chiếu với tài liệu "29 danh mục Master Data" của TCT để làm bảng quy đổi.
  * *Ví dụ: Mã Hợp Đồng đang lưu là `HĐ-2025/11` -> Tra theo chuẩn TCT phải đổi thành `HD-QNG-2025-0011`.*
* Bảng ánh xạ này sẽ được lưu lại làm "Từ điển" cung cấp cho máy chủ ETL ở Giai đoạn 2.

### Bước 1.3: Đánh giá bảo mật và Phân loại dữ liệu nhạy cảm
* **IT và Ban lãnh đạo** rà soát xem trong các bảng dữ liệu chuẩn bị đẩy đi, cột nào chứa thông tin nhạy cảm (Lương chi tiết, SĐT, Số CMND...).
* Đánh dấu các cột này là `[Cần Masking]`. Đến giai đoạn lập trình, IT sẽ viết lệnh tự động làm mờ/mã hóa các cột này để tuân thủ Nghị định 13 trước khi đẩy lên mạng TCT.

## 4. Kết quả cần đạt (Deliverables)
* [ ] File Excel Danh mục nguồn dữ liệu (Data Catalog).
* [ ] Bảng ánh xạ Master Data (Từ điển Mapping) đã được các phòng ban ký chốt.
* [ ] Danh sách các trường dữ liệu nhạy cảm cần che mờ (Masking List).
