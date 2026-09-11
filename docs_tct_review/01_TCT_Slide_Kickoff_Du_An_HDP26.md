# BÁO CÁO RÀ SOÁT TÀI LIỆU TCT SỐ 01
## Tên tài liệu: Lễ Khởi Động Dự Án Giải Pháp Nền Tảng Dữ Liệu (Data Platform) - Giai Đoạn 1
* **Tên file gốc:** `TCT-DP_Slide_Kick off_Final.pdf` (27 trang)
* **Thời gian sự kiện:** Ngày 04 tháng 03 năm 2026 tại Tòa nhà PetroVietnam Tower, Số 1 Lê Duẩn, P. Bến Nghé (Sài Gòn), Q.1, TP. Hồ Chí Minh.
* **Mã dự án:** `HDP26` (Hybrid Data Platform 2026)
* **Số hợp đồng:** `1-2026/PTSC-CDS/HĐ`
* **Các bên tham gia:**
  * **Chủ đầu tư (Bên A):** Tổng công ty Cổ phần Dịch vụ Kỹ thuật Dầu khí Việt Nam (PTSC).
  * **Nhà thầu triển khai (Bên B):** Liên danh Công ty Cổ phần Tập đoàn HiPT - Công ty Cổ phần Tin học - Viễn thông Hàng không (Liên danh HiPT - AITS).

---

### 1. Bối cảnh, Tầm nhìn & Mục tiêu Dự án
* **Chiến lược "Data First":** Dự án xuất phát từ 5 trụ cột chuyển đổi số của PTSC, xác định dữ liệu là tài sản cốt lõi. Mục tiêu chuyển từ quản lý thủ công, dữ liệu rời rạc tại từng phòng ban/đơn vị thành tri thức số hợp nhất toàn Tổng công ty.
* **Quy mô triển khai giai đoạn 1:**
  * Thời gian thực hiện hợp đồng: **18 tháng**.
  * Trong đó: **6 tháng xây dựng hệ thống** (01/04/2026 đến 27/08/2026); **12 tháng tiếp theo vận hành, hỗ trợ kỹ thuật** (27/08/2026 đến 27/08/2027).
  * Địa điểm triển khai chính: PetroVietnam Tower, Số 1 Lê Duẩn, TP.HCM.
* **Ba hạng mục sản phẩm đầu ra chính:**
  1. **Trung tâm Vận hành Dữ liệu (Data Operation Center - DOC):** Hệ thống màn hình điều hành, giám sát KPI thời gian thực cho Ban lãnh đạo TCT.
  2. **Nền tảng Dữ liệu Hợp nhất (Hybrid Data Platform):** Trục tích hợp, hồ dữ liệu Datalakehouse, các công cụ phân tích truy vấn dữ liệu.
  3. **Hạ tầng CNTT & An toàn thông tin (ATTT) phục vụ dữ liệu:** Phần cứng máy chủ, hệ thống lưu trữ, phân vùng bảo mật, bản quyền phần mềm và kênh mạng kết nối.

---

### 2. Mô hình Kiến trúc & Công nghệ Lựa chọn
* **Kiến trúc Hybrid Data Platform (Multi-site, Multi-cloud):**
  * **Multi-site (Đa điểm):** Hạ tầng lưu trữ on-premise tại Cơ quan Tổng công ty (CQTCT) liên kết mạng với các Đơn vị Thành viên (ĐVTV) trải dài trên các vị trí địa lý (Quảng Ngãi, Vũng Tàu, Hải Phòng, Hà Nội...).
  * **Multi-cloud (Đa đám mây):** Tận dụng ưu thế linh hoạt, khả năng mở rộng của các nhà cung cấp điện toán đám mây (VNPT Cloud, Microsoft Azure...).
* **Phạm vi tính năng:** Bao gồm **12 phân hệ chức năng** đáp ứng chu trình khép kín: *Tích lũy - Tích hợp - Đồng bộ - Phân chia - Phân tích - Quản trị dữ liệu lớn*.
* **4 Năng lực công nghệ cốt lõi:**
  1. **Trục tích hợp (ESB / Message Bus):** Kết nối liên thông mọi phần mềm nghiệp vụ hiện hữu và tương lai.
  2. **Hồ lưu trữ Lakehouse:** Lưu trữ dữ liệu thô (Raw), dữ liệu chuẩn hóa (Silver) và dữ liệu mô hình hóa phân tích (Gold) trên nền công nghệ hiện đại.
  3. **Giao diện phân tích ngôn ngữ tự nhiên (Text-to-Data / AI):** Cho phép người dùng nghiệp vụ và lãnh đạo truy vấn dữ liệu bằng câu hỏi thông thường.
  4. **Khả năng co giãn (Scalability):** Mở rộng linh hoạt theo chiều ngang (thêm dung lượng lưu trữ) và chiều dọc (thêm tính năng/module).

---

### 3. Lộ trình Triển khai Tổng thể & Vị trí của Đơn vị Thành viên
* **Giai đoạn 1 (Năm 2026 - CQTCT làm hạt nhân):**
  * Xây dựng trục dữ liệu và nền tảng lõi tại CQTCT.
  * Chuẩn hóa danh mục báo cáo và hệ thống ứng dụng dùng chung tại các Ban chức năng CQTCT (Tài chính Kế toán, Kỹ thuật Sản xuất, Thương mại, An toàn Chất lượng, Kế hoạch Đầu tư, Quản trị Nguồn Nhân lực...).
* **Giai đoạn 2 (Mở rộng kết nối 2 chiều đến các Đơn vị Thành viên):**
  * Kết nối dữ liệu 2 chiều (Bidirectional data flow) giữa Hub Data Platform của TCT và hệ thống CNTT của các ĐVTV.
  * **Đơn vị Thành viên được chỉ định thí điểm mở rộng:** Slide trang 19 nêu rõ các đơn vị đại diện gồm **PTSC Quảng Ngãi**, **PTSC Hà Nội**...
  * **Nguyên tắc xuyên suốt:** Dùng chung tài nguyên - Chuẩn hóa định danh - Tránh đầu tư trùng lặp phân tán.

---

### 4. Cơ cấu Tổ chức Dự án & Cơ chế Phối hợp 3 Cấp
Mô hình quản trị dự án được phân cấp rõ ràng để đảm bảo ra quyết định nhanh chóng:
* **Cấp 1 - Ban Chỉ đạo Dự án (Steering Committee):**
  * Đại diện PTSC: **Ông Phạm Văn Hùng** - Phó Tổng Giám đốc PTSC (Trưởng Ban chỉ đạo).
  * Đại diện HiPT - AITS: **Ông Hoàng Văn Ninh** (Trưởng Ban chỉ đạo Bên B).
  * Quyền hạn: Quyết định mục tiêu chiến lược, ngân sách, phạm vi hợp đồng lớn.
* **Cấp 2 - Ban Quản trị Dự án (Project Management Office - PMO):**
  * Giám đốc dự án PTSC: **Ông Nguyễn Đức Thiện** (Trưởng Ban Quản trị) & **Bà Phan Thị Ngọc Vân** (Phó GĐ dự án).
  * Giám đốc dự án HiPT - AITS: **Ông Nguyễn Kim Cương**.
  * Quyền hạn: Điều hành nghiệp vụ, kiểm soát tiến độ từng mốc, phân giải xung đột kỹ thuật.
* **Cấp 3 - Đội Triển khai Kỹ thuật (Working Squads):**
  * **Tổ Dữ liệu & R&D PTSC:** Ông Nguyễn Văn Phát, Huỳnh Minh Nhẫn phối hợp Nhóm Dữ liệu & Báo cáo HiPT (Ông Nguyễn P. Ngọc Tuấn).
  * **Tổ Số hóa Quy trình (SHQT) PTSC:** Ông Nguyễn Quốc Thống phối hợp Nhóm Số hóa - Tích hợp HiPT (Ông Nguyễn Xuân Thịnh).
  * **Tổ Hạ tầng & ATTT / Phòng CNTT PTSC:** Ông Nguyễn Văn Minh phối hợp Nhóm Hạ tầng HiPT (Ông Hoàng Văn Ninh) & Nhóm Phần mềm Data Platform (Ông Nguyễn Đình Công).
  * Đầu mối tại các ĐVTV: Lãnh đạo Ban/Tổ CĐS và cán bộ kỹ thuật IT/Nghiệp vụ chuyên trách.

---

### 5. Ý nghĩa & Tác động Cốt lõi đối với PTSC Quảng Ngãi
1. **PTSC Quảng Ngãi là đơn vị trọng điểm:** Được nêu tên trực tiếp trong kiến trúc mở rộng giai đoạn tiếp theo của TCT. Do đó, việc chủ động chuẩn bị năng lực, hệ thống và nhân sự là trách nhiệm chiến lược.
2. **Tuân thủ cơ chế làm việc của Ban Dự án TCT:** Mọi đề xuất, khảo sát và tích hợp dữ liệu của Quảng Ngãi sẽ làm việc trực tiếp với Cấp 2 (Ban Quản trị của anh Nguyễn Đức Thiện) và Cấp 3 (Tổ Dữ liệu của anh Nguyễn Văn Phát, Tổ Hạ tầng của anh Nguyễn Văn Minh).
3. **Mốc thời gian cấp bách:** Khi hệ thống Core của TCT golive vào tháng 8/2026, các ĐVTV sẽ phải sẵn sàng cổng giao tiếp để bơm dữ liệu về và khai thác dữ liệu báo cáo quản trị.
