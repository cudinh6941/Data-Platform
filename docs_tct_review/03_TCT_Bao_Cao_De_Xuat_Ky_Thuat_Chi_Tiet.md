# BÁO CÁO RÀ SOÁT TÀI LIỆU TCT SỐ 03
## Tên tài liệu: Báo Cáo Phân Tích - Đề Xuất Kỹ Thuật Giải Pháp Nền Tảng Dữ Liệu PTSC
* **Tên file gốc:** `TCT-DP_Bao cao de xuat ky thuat_Final - Data Flatform.pdf` (82 trang)
* **Cơ quan ban hành:** Ban Dự án Chuyển đổi số - Tổng công ty PTSC.
* **Đặc điểm tài liệu:** Đây là **tài liệu kỹ thuật nền tảng, đồ sộ và chi tiết nhất** của TCT, quy định cụ thể kiến trúc hệ thống, danh mục 12 phân hệ phần mềm, thiết kế cấu trúc dữ liệu, luồng tích hợp ESB, mô hình Data Governance 5 cấp và cấu hình phần cứng/Cloud chi tiết.

---

### 1. Kiến Trúc Lưu Trữ Datalakehouse 3 Phân Vùng (Medallion Architecture)
TCT quy định kiến trúc dữ liệu bắt buộc phải tổ chức qua 3 phân vùng xử lý logic khép kín:
1. **Phân vùng Dữ liệu Thô (Landing Zone / Raw / Bronze):**
   * **Đặc điểm:** Tiếp nhận dữ liệu nguyên trạng từ các hệ thống nguồn (FAST, HRM, ERP, SCADA, File Excel...) mà không can thiệp logic nghiệp vụ.
   * **Tính chất:** Bất biến (Immutable), lưu trữ đầy đủ lịch sử theo dòng thời gian (time-series, historical snapshots). Định dạng lưu trữ nén tối ưu (Parquet / Object Storage).
2. **Phân vùng Dữ liệu Chuẩn hóa (Standardized Zone / Staging / Silver):**
   * **Đặc điểm:** Dữ liệu sau khi đi qua bộ lọc kiểm tra chất lượng (Data Quality Rules).
   * **Thao tác xử lý:** Ép kiểu dữ liệu chuẩn (casting data types), xử lý lỗi font ký tự UTF-8, loại bỏ trùng lặp (deduplication), tách các trường dữ liệu gộp, và áp dụng quy tắc làm sạch.
3. **Phân vùng Dữ liệu Phân tích Tinh chế (Curated Zone / Serving / Gold):**
   * **Đặc điểm:** Dữ liệu được mô hình hóa theo cấu trúc đa chiều (Star Schema: Bảng Fact và các bảng Dimension) hoặc One Big Table (OBT).
   * **Mục đích:** Cung cấp nguồn cấp dữ liệu tốc độ cao cho Power BI, Apache Superset, báo cáo Ban lãnh đạo và các mô hình học máy (Machine Learning / AI).

---

### 2. Danh Mục & Chức Năng Của 12 Phân Hệ Nền Tảng
Báo cáo kỹ thuật xác định 12 phân hệ cấu thành Data Platform hoàn chỉnh của PTSC:

1. **Phân hệ Thu thập & Chuyển đổi dữ liệu (ETL / ELT / CDC):**
   * Hỗ trợ trích xuất dữ liệu hàng loạt theo lịch (Batch via Apache Airflow) và trích xuất dữ liệu thay đổi theo thời gian thực dựa trên nhật ký CSDL (Log-based Change Data Capture - CDC via Debezium/Kafka Connect).
2. **Phân hệ Lưu trữ Datalakehouse:**
   * Nền tảng Object Storage (MinIO / Ceph S3-compatible), định dạng bảng mở (Delta Lake / Apache Iceberg) và công cụ truy vấn phân tán tốc độ cao (Trino / StarRocks / ClickHouse).
3. **Phân hệ Trục tích hợp (Enterprise Service Bus - ESB & Message Broker):**
   * Đóng vai trò “xương sống liên thông” toàn Tổng công ty dựa trên Apache Kafka và API Gateway, xử lý hàng triệu thông điệp bất đồng bộ, chống tắc nghẽn hệ thống.
4. **Phân hệ Quản lý Dữ liệu Chủ (Master Data Management - MDM):**
   * Tạo lập "Bản ghi Vàng" (Golden Record) duy nhất cho các thực thể danh mục cốt lõi: Khách hàng, Nhà thầu, Nhà cung cấp, Dự án, Nhân sự, Tài sản/Thiết bị, Mã vật tư.
5. **Phân hệ Báo cáo & Trực quan hóa (BI & Analytics):**
   * Kết nối cổng Power BI Gateway phục vụ hệ thống báo cáo hiện hữu của TCT và triển khai công cụ phân tích tự phục vụ mã nguồn mở (Apache Superset) cho người dùng diện rộng.
6. **Phân hệ Danh mục Dữ liệu & Phả hệ (Data Catalog & Lineage):**
   * Quản lý từ điển dữ liệu tập trung (Data Dictionary), lập bản đồ nguồn gốc dòng chảy dữ liệu (Lineage) từ hệ thống nguồn cấp 3 đến báo cáo cấp lãnh đạo.
7. **Phân hệ Kiểm soát Chất lượng Dữ liệu (Data Quality - DQ):**
   * Thiết lập bộ luật tự động kiểm tra: Tính duy nhất (Uniqueness), Tính đầy đủ (Completeness - Not Null), Tính hợp lệ định dạng (Validity), và Tính toàn vẹn tham chiếu (Referential Integrity). Tự động cô lập bản ghi lỗi (Quarantine table).
8. **Phân hệ Điều phối Luồng xử lý (Data Workflow Orchestration):**
   * Sử dụng Apache Airflow để lập lịch, giám sát các luồng Pipelines xử lý dữ liệu phức tạp theo đồ thị có hướng không chu trình (DAGs).
9. **Phân hệ Khai thác Dữ liệu bằng Ngôn ngữ Tự nhiên (Text-to-Data / AI):**
   * Tích hợp các mô hình ngôn ngữ lớn (LLM) và kỹ thuật RAG (Retrieval-Augmented Generation), cho phép cán bộ quản lý gõ câu hỏi bằng tiếng Việt để sinh câu lệnh SQL và trả kết quả biểu đồ tức thì.
10. **Thư viện Máy học & Khoa học Dữ liệu (Machine Learning / MLOps):**
    * Môi trường phát triển và triển khai mô hình dự báo (dự báo hỏng hóc thiết bị tàu/giàn khoan, dự báo chi phí dự án EPC, tối ưu tồn kho vật tư).
11. **Phân hệ Giám sát An ninh Dữ liệu & Ghi vết (Data Security & Audit):**
    * Kiểm soát truy cập dựa trên vai trò và thuộc tính (RBAC/ABAC), mã hóa dữ liệu nhạy cảm (Data Masking / Tokenization), ghi nhật ký kiểm toán (Audit Logs) mọi hành vi truy cập dữ liệu.
12. **Phân hệ Quản trị Metadata (Metadata Governance):**
    * Quản lý vòng đời dữ liệu, chính sách lưu trữ (Data Retention), xóa dữ liệu quá hạn, và gắn nhãn phân loại bảo mật (Public, Internal, Confidential, Strictly Confidential).

---

### 3. Thiết Kế Hạ Tầng Phần Cứng & Mạng Kết Nối
* **Hạ tầng On-Premise Data Center PTSC:**
  * Cụm máy chủ phiến (Blade/Rack Servers) năng lực xử lý cao, hỗ trợ ảo hóa VMware vSphere Enterprise Plus hoặc cụm KVM mã nguồn mở.
  * Hệ thống lưu trữ SAN tốc độ cao kết hợp NAS Object Storage mở rộng theo Terabyte/Petabyte.
  * Mạng chuyển mạch trung tâm 10Gbps/25Gbps dự phòng kép (Active-Active).
* **Hạ tầng Điện toán Đám mây (Cloud Infrastructure):**
  * Triển khai cụm Kubernetes phục vụ các dịch vụ ứng dụng microservices, Text-to-Data và cổng API ngoài.
* **Mô hình Mạng kết nối Đơn vị Thành viên:**
  * Kết nối giữa TCT và các ĐVTV (như PTSC Quảng Ngãi) được thực hiện thông qua kênh truyền riêng số liệu chuyên dùng (MPLS WAN) kết hợp đường hầm bảo mật **IPSec VPN Site-to-Site dự phòng**.
  * Bắt buộc cấu hình chính sách tường lửa (Firewall Rules) chặt chẽ, chỉ mở các dải IP và cổng dịch vụ được phép (Kafka Port, API Port, Database Port chỉ định).

---

### 4. Ý Nghĩa & Bài Học Chiến Lược Cho PTSC Quảng Ngãi
1. **Khớp nối chuẩn 3 tầng dữ liệu:** Đội ngũ kỹ thuật PTSC Quảng Ngãi không cần viết các câu lệnh phức tạp kết nối trực tiếp CSDL sản xuất lên báo cáo. Thay vào đó, tuân thủ đúng 3 tầng: Đẩy dữ liệu thô vào Landing Zone -> TCT/ĐVTV làm sạch sang Silver -> Mô hình hóa sang Gold.
2. **Không lo ngại việc Vendor trói chân:** TCT đã định hướng kiến trúc mở (Trino, Delta Lake, Kafka). Điều này bảo vệ Quảng Ngãi khi làm việc với các đơn vị cung cấp phần mềm nội bộ (như FAST Accounting hay phần mềm nhân sự).
3. **Tiêu chuẩn an toàn thông tin bắt buộc:** Quảng Ngãi phải rà soát lại tường lửa, dải mạng nội bộ và các cơ chế chứng thực người dùng (Active Directory/LDAP) để sẵn sàng đồng bộ vào hệ thống IAM tập trung của TCT.
