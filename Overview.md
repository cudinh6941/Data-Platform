\# KẾ HOẠCH TRIỂN KHAI DATA PLATFORM - PTSC QUẢNG NGÃI (L3 SPOKE)



\## 1. ĐỊNH VỊ KIẾN TRÚC \& PHÂN LOẠI (LEVEL 3)

Theo chiến lược Data Platform của Tổng công ty (TCT) PTSC, PTSC Quảng Ngãi được định vị ở \*\*Level 3 (Đơn vị lớn)\*\* trong mô hình Hub-Spoke:

\- \*\*Không xây dựng:\*\* Không tự xây dựng Cụm máy chủ lưu trữ Data Platform (dHCI) tại Quảng Ngãi (không làm L4).

\- \*\*Quyền lợi \& Không gian:\*\* Được cấp \*\*Tenant/Workspace riêng biệt hoàn toàn\*\* trên hệ thống hạ tầng tập trung của TCT (Hub), có phân vùng lưu trữ lớn và license nền tảng bổ sung (Microsoft Fabric, PowerBI).

\- \*\*Mô hình kết nối:\*\* Các phần mềm nội bộ (Silo DB) tại Quảng Ngãi sẽ được trích xuất, chuẩn hóa và "bơm" trực tiếp lên Workspace L3 tại Hub TCT qua đường truyền mạng bảo mật.



\## 2. SƠ ĐỒ KIẾN TRÚC LUỒNG DỮ LIỆU TẠI PTSC QUẢNG NGÃI

Quảng Ngãi chỉ đóng vai trò là "Trạm trung chuyển \& Tích hợp" (Data Integration Gateway), không đóng vai trò "Kho lưu trữ vĩnh viễn".



\[Local Database QN] (HRM, Kế toán, Vật tư...) 

&#x20;      │

&#x20;      ▼

\[Data Integration Server QN] (Cài đặt Airbyte / dbt / API Gateway) 

&#x20;  - Nhiệm vụ: HÚT dữ liệu thô định kỳ -> LÀM SẠCH -> ĐỔI MÃ (Mapping Master Data)

&#x20;      │

&#x20;      ▼

\[VPN / SD-WAN (Zone 1 <-> Zone 3 TCT)] (Mã hóa SSL/IPSec)

&#x20;      │

&#x20;      ▼

\[TCT HUB: L3 WORKSPACE - PTSC QUẢNG NGÃI] 

&#x20;  - Lưu trữ tại: MinIO (On-premise) \& Microsoft Fabric OneLake (Cloud)

&#x20;  - Khai thác: Báo cáo Power BI nội bộ Ban Giám đốc QN \& Báo cáo gửi TCT.



\## 3. CÁC TIÊU CHUẨN TUÂN THỦ BẮT BUỘC (COMPLIANCE)

\- \*\*Chuẩn hóa Master Data:\*\* Dữ liệu trước khi đẩy lên Hub phải được ánh xạ đúng chuẩn \*\*29 danh mục Master Data\*\* của TCT (Ví dụ: Mã nhân sự, Mã vật tư, Mã hợp đồng...).

\- \*\*Bảo mật (ATTT):\*\* Tuân thủ quy hoạch 8 Zones của TCT. Máy chủ đẩy dữ liệu phải nằm trong \*Internal Service Zone\*, kết nối qua kênh truyền mã hóa.

\- \*\*Pháp lý (NĐ 13):\*\* Có cơ chế Masking (che dấu) dữ liệu cá nhân nhạy cảm của CBNV trước khi đồng bộ hoặc đưa lên báo cáo.



\---



\## 4. KẾ HOẠCH HÀNH ĐỘNG (ROADMAP TRIỂN KHAI) CỦA PTSC QUẢNG NGÃI



\### GIAI ĐOẠN 1: KHẢO SÁT \& CHUẨN BỊ HẠ TẦNG MẠNG (Thực hiện bởi IT nội bộ)

\- \[ ] \*\*Rà soát Database:\*\* Thống kê toàn bộ database của các phần mềm nội bộ hiện có và chuẩn bị triển khai.

\- \[ ] \*\*Ánh xạ Master Data:\*\* Đối chiếu cấu trúc dữ liệu hiện hành với 29 danh mục Master Data TCT yêu cầu. Lập bảng Mapping chuẩn.

\- \[ ] \*\*Thiết lập Network:\*\* Cấu hình kênh truyền bảo mật (VPN Site-to-Site/SD-WAN) kết nối an toàn từ Datacenter PTSC Quảng Ngãi tới Tầng 10 CQTCT. Đảm bảo tuân thủ thiết kế 8 Zones.



\### GIAI ĐOẠN 2: XÂY DỰNG TRẠM TRUNG CHUYỂN DỮ LIỆU (Outsource + IT giám sát)

\- \[ ] \*\*Triển khai Integration Server:\*\* Cấp phát 1-2 máy chủ (VM) nội bộ tại Quảng Ngãi để làm máy chủ ETL/Tích hợp.

\- \[ ] \*\*Phát triển luồng tích hợp (Data Pipeline):\*\* Thuê đối tác (Vendor) dùng Airbyte/dbt hoặc tự viết API để kết nối vào các Local Database.

\- \[ ] \*\*Thiết lập tác vụ đồng bộ:\*\* Cấu hình lập lịch (Scheduler) tự động hút, chuẩn hóa và đẩy dữ liệu lên \*\*Workspace L3\*\* của Quảng Ngãi trên TCT Hub (Batch hoặc Near-realtime).



\### GIAI ĐOẠN 3: TIẾP NHẬN BẢN QUYỀN \& XÂY DỰNG BÁO CÁO (IT + Business Users)

\- \[ ] \*\*Nhận bàn giao Tenant L3:\*\* Phối hợp TCT để nhận quyền quản trị Workspace L3 trên Microsoft Fabric / PowerBI / MinIO.

\- \[ ] \*\*Phân quyền nội bộ (RBAC):\*\* Cấu hình IAM/Keycloak phân quyền cho từng user tại Quảng Ngãi truy cập kho dữ liệu của đơn vị mình.

\- \[ ] \*\*Thiết kế Dashboard:\*\* Phát triển các báo cáo Power BI khai thác trực tiếp dữ liệu từ Workspace L3 phục vụ điều hành mảng tại Quảng Ngãi.

\- \[ ] \*\*Đào tạo Data cơ bản:\*\* Đào tạo chuyển giao vận hành ETL và kỹ năng Data Engineering cơ bản cho đội ngũ IT hiện tại (vốn chỉ chuyên Network/System).

