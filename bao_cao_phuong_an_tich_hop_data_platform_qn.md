# TỔNG CÔNG TY CỔ PHẦN DỊCH VỤ KỸ THUẬT DẦU KHÍ VIỆT NAM
## CÔNG TY CỔ PHẦN DỊCH VỤ DẦU KHÍ QUẢNG NGÃI PTSC
---
**Số:** ...... /BC-DKQN-TK&R&D  
*Quảng Ngãi, ngày 11 tháng 09 năm 2026*

# BÁO CÁO NGHIÊN CỨU TÀI LIỆU DATA PLATFORM TCT VÀ ĐỀ XUẤT PHƯƠNG ÁN KIẾN TRÚC TÍCH HỢP HỆ THỐNG CNTT PTSC QUẢNG NGÃI

* **Kính gửi:** 
  * Ban Chỉ đạo Chuyển đổi số Tổng công ty PTSC;
  * Ban Nghiên cứu Phát triển & Chuyển đổi số (NCPT & CĐS) Tổng công ty PTSC;
  * Ban Quản trị Dự án Giải pháp Nền tảng Dữ liệu (HDP26) Tổng công ty PTSC.

---

## PHẦN I: TIẾP THU Ý KIẾN CHỈ ĐẠO CỦA TỔNG CÔNG TY & BỐI CẢNH BÁO CÁO

### 1.1. Bối cảnh triển khai phần mềm nghiệp vụ tại PTSC Quảng Ngãi
Căn cứ Kế hoạch Chuyển đổi số năm 2026 của PTSC Quảng Ngãi (Công văn số 1153/DKQN-HCNS ngày 26/04/2026), nhằm số hóa quy trình quản trị sản xuất kinh doanh trong các lĩnh vực chế tạo cơ khí siêu trường siêu trọng, gia công kết cấu năng lượng tái tạo ngoài khơi và dịch vụ cảng biển Dung Quất, Công ty Cổ phần Dịch vụ Dầu khí Quảng Ngãi (PTSC Quảng Ngãi) đã chủ động xây dựng phương án triển khai 02 phần mềm nghiệp vụ trọng điểm trong năm 2026:
1. **Phần mềm Quản lý công tác An toàn - Sức khỏe - Môi trường (HSEQ).**
2. **Phần mềm Quản lý Mua sắm hàng hóa và dịch vụ (Procurement Management).**

Ngày 19/06/2026, PTSC Quảng Ngãi đã có văn bản báo cáo và gửi hồ sơ kỹ thuật đề xuất triển khai 02 phần mềm trên lên Ban NCPT & CĐS Tổng công ty.

### 1.2. Ý kiến phản hồi và định hướng chỉ đạo của Ban Dự án CĐS Tổng công ty
Sau khi rà soát hồ sơ, ngày 06/07/2026 và ngày 01/08/2026, Ban Dự án Chuyển đổi số Tổng công ty (đầu mối là Chuyên gia Quản trị Chiến lược Phan Thị Ngọc Vân) đã có văn bản phản hồi và kết luận chỉ đạo:
* **Đối với Phần mềm HSEQ:** TCT đánh giá giải pháp cơ bản đáp ứng các yêu cầu tích hợp theo định hướng chung; PTSC Quảng Ngãi được phép tiếp tục triển khai theo kế hoạch.
* **Đối với Phần mềm Quản lý Mua sắm hàng hóa, dịch vụ:** Ban Dự án CĐS TCT đã đưa ra cảnh báo kỹ thuật rất xác đáng:
  > *"Phương án hiện tại tập trung đáp ứng nhu cầu Quy trình nghiệp vụ với phạm vi tích hợp nội bộ giữa MESx – PMSx – FBO. Tuy nhiên, khi mở rộng kết nối với các hệ thống hiện hữu khác của PTSC Quảng Ngãi (eOffice, FAST, IRTECH, VTI…) và các nền tảng dùng chung của Tổng công ty trong tương lai, **mô hình kết nối trực tiếp sẽ làm gia tăng đáng kể số lượng API, chi phí quản lý tích hợp, nhiều rủi ro về ATTT**.*
  > *Do đó, đề nghị PTSC Quảng Ngãi nghiên cứu lộ trình chuyển sang kiến trúc tích hợp tập trung thông qua **Data Platform (ESB/API Gateway, MDM, Data Lakehouse…)** để bảo đảm khả năng mở rộng, quản trị dữ liệu và kết nối đồng bộ với Tổng công ty...*
  > ***Kết luận: Đề nghị PTSC Quảng Ngãi tạm thời giãn tiến độ triển khai Phần mềm Quản lý mua sắm hàng hóa, dịch vụ để phối hợp cùng BDA CĐS Tổng công ty rà soát, thống nhất kiến trúc tích hợp tổng thể, bảo đảm đồng bộ với Data Platform và các nền tảng dùng chung của Tổng công ty, tránh phát sinh đầu tư chồng chéo và chi phí chuyển đổi trong giai đoạn sau.***"

### 1.3. Tinh thần tiếp thu và kết quả nghiên cứu tài liệu của PTSC Quảng Ngãi
Thực hiện nghiêm túc chỉ đạo của Ban Dự án CĐS Tổng công ty và ý kiến chỉ đạo trực tiếp của Lãnh đạo Phòng Thiết kế & R&D PTSC Quảng Ngãi (anh Bùi Lực ngày 29/08/2026), Tổ CNTT & CĐS PTSC Quảng Ngãi đã tạm dừng các thủ tục mua sắm độc lập, tập trung toàn bộ nguồn lực kỹ thuật nghiên cứu thấu đáo bộ hồ sơ kỹ thuật tại thư mục `TCT` do TCT cung cấp, bao gồm:
1. `TCT-DP_Slide_Kick off_Final.pdf`: Quyết định và Kế hoạch khởi động dự án HDP26 giữa PTSC và Liên danh HiPT - AITS (Hợp đồng 1-2026/PTSC-CDS/HĐ).
2. `Slide Tóm tắt lựa chọn giải pháp Hybrid Data Platform PTSC.pdf`: Đề xuất kiến trúc Hybrid Multi-site Multi-cloud và 6 nguyên tắc vàng.
3. `TCT-DP_Bao cao de xuat ky thuat_Final - Data Flatform.pdf`: Bản đặc tả kỹ thuật chi tiết 82 trang về 12 phân hệ chức năng, hồ dữ liệu Lakehouse 3 vùng và hạ tầng phần cứng.
4. `20260810_Slide_Hoi thao Data Platform_Phien Sang.pdf`: Chiến lược dữ liệu tập đoàn, xóa bỏ ốc đảo 310 báo cáo, cơ chế luồng dữ liệu 2 chiều.
5. `20260810_Slide_Hoi thao Data Platform_Phien Chieu.pdf`: Mô hình Hub-and-Spoke, định vị đơn vị thành viên, quản trị dữ liệu 5 cấp và 7 cấu phần chi phí đầu tư.
6. `Phu luc ve yeu cau tich hop Data Platform.pdf`: Bộ quy chuẩn kỹ thuật bắt buộc 13 tiêu chí tích hợp hệ thống (Mẫu `PTSC-ADM-RG08-FM10`).

---

## PHẦN II: KHÁI QUÁT NHẬN THỨC VỀ KIẾN TRÚC ENTERPRISE DATA PLATFORM TCT

Qua quá trình nghiên cứu tài liệu kỹ thuật, PTSC Quảng Ngãi hoàn toàn đồng thuận và đánh giá rất cao tầm nhìn kiến trúc của Tổng công ty:

### 2.1. Đánh giá về Mô hình Kiến trúc Hybrid Data Platform (Multi-site, Multi-cloud)
TCT đã lựa chọn chính xác khi không áp dụng mô hình Pure Cloud (làm bùng nổ chi phí thuê bao OPEX hàng tháng khi dung lượng dữ liệu sản xuất phình to) hay mô hình On-Premise đơn lẻ (thiếu tính linh hoạt). Việc đặt Core Datalakehouse tại Data Center TCT kết hợp điện toán đám mây cho các tác vụ AI/Text-to-Data giúp cân bằng hoàn hảo giữa hiệu năng xử lý, bảo đảm an toàn dữ liệu dầu khí theo Nghị định 13/2023/NĐ-CP và tối ưu hóa chi phí đầu tư (TCO).

### 2.2. Trục Tích Hợp (ESB / Kafka / API Gateway) - Giải pháp xóa bỏ "Mạng nhện API"
Nhược điểm lớn nhất của mô hình tích hợp trực tiếp Point-to-Point cũ giữa MESx – PMSx – FBO chính là sự phụ thuộc chặt chẽ (tight coupling). Khi phát sinh thêm eOffice, FAST, IRTECH, VTI... việc kết nối tay đôi độc lập sẽ dẫn tới nguy cơ bùng nổ API theo cấp số nhân $\frac{N(N-1)}{2}$, chi phí quản trị bảo trì khổng lồ và rất dễ đứt gãy dây chuyền khi một hệ thống thay đổi cấu trúc bảng. Việc cắm tất cả hệ thống vào một Trục tích hợp tập trung thông qua hàng đợi thông điệp (Kafka) là giải pháp duy nhất để mở rộng bền vững.

### 2.3. Quản trị Dữ liệu Chủ (MDM) - Cốt lõi của mô hình ERP liên thông
Dữ liệu chỉ có thể liên thông thông suốt giữa Mua sắm - Kế toán - Kho khi có chung một bộ từ điển định danh: Mã Nhà cung cấp (Vendor ID), Mã Vật tư (Item Code), Mã Dự án (Project Code). Nền tảng MDM của TCT sẽ đóng vai trò tạo lập **"Bản ghi Vàng" (Golden Record)**, loại bỏ triệt để tình trạng một đối tượng có nhiều mã khác nhau giữa các hệ thống.

### 2.4. Định vị của PTSC Quảng Ngãi trong Mô hình Hub-and-Spoke
Căn cứ tiêu chí phân nhóm 17 Đơn vị Thành viên của TCT, PTSC Quảng Ngãi được định vị thuộc nhóm **Spoke Level 3** (Đơn vị có hệ sinh thái ứng dụng nghiệp vụ riêng, quy mô sản xuất lớn). Tuy nhiên, với đặc thù sản xuất cơ khí siêu trường siêu trọng và cảng biển có khối lượng dữ liệu phát sinh hàng ngày rất lớn, Quảng Ngãi cần một lộ trình tiến lên **Spoke Level 2 (nghĩa là có Hồ dữ liệu nội bộ tại chỗ - Local Lakehouse)** để tự chủ phân tích tác chiến mà không gây nghẽn đường truyền mạng lên Hub TCT.

---

## PHẦN III: THỰC TRẠNG HỆ THỐNG VÀ PHƯƠNG ÁN ĐIỀU CHỈNH THIẾT KẾ TÍCH HỢP TẠI PTSC QUẢNG NGÃI

### 3.1. Thực trạng hiện tại của hệ sinh thái CNTT tại PTSC Quảng Ngãi (As-Is: Chưa tích hợp tập trung)
PTSC Quảng Ngãi xin báo cáo trung thực bức tranh hiện trạng hệ thống CNTT tại đơn vị tính đến tháng 9/2026:
1. **Tình trạng phân mảnh, ốc đảo dữ liệu (Data Silos):**
   * Các phần mềm nghiệp vụ hiện hữu hoàn toàn chạy độc lập, chưa có trục tích hợp hay cơ chế chia sẻ dữ liệu tự động.
   * Phần mềm Kế toán - Tài chính - Kho: Sử dụng phần mềm **FAST Accounting** (CSDL SQL Server). Dữ liệu nhập thủ công, chưa liên thông với quy trình mua sắm hay hợp đồng.
   * Phần mềm Văn phòng số: Sử dụng **e-Office (BTEC)** cho trình ký, văn bản đi/đến. Chưa tích hợp ký số cho các quy trình mua sắm vật tư hay hồ sơ kỹ thuật.
   * Phần mềm Quản lý Cảng biển: Sử dụng phần mềm **IRTECH** quản lý kho bãi, cầu cảng Dung Quất, cân xe độc lập.
   * Phần mềm Quản lý Tài sản: Sử dụng **VTI** theo dõi máy móc thiết bị thi công, cẩu trục độc lập.
2. **Thực trạng Phần mềm HSEQ:** Hiện đang trong giai đoạn thuê nhà thầu xây dựng các phân hệ nghiệp vụ nội bộ độc lập (quản lý rủi ro an toàn, sự cố, cấp phép an toàn PTW), **chưa kết nối với bất kỳ trục tích hợp hay nền tảng dữ liệu tập trung nào**.
3. **Thực trạng Phần mềm Quản lý Mua sắm:** Đang dừng lại ở hồ sơ thiết kế tích hợp trực tiếp nối dây tay đôi giữa 3 bên (`MESx – PMSx – FBO`). **PTSC Quảng Ngãi đã nghiêm túc dừng toàn bộ tiến độ mua sắm theo đúng chỉ đạo của Ban Dự án TCT** để tái thiết kế phương án kiến trúc tổng thể.

### 3.2. Phương án Kiến trúc Tích hợp Tập trung Đề xuất Điều chỉnh (To-Be)
Tiếp thu trọn vẹn chỉ đạo của TCT, PTSC Quảng Ngãi đề xuất phương án kiến trúc mới, xóa bỏ hoàn toàn kết nối tay đôi, tổ chức lại hệ sinh thái CNTT của Công ty xoay quanh **Hồ dữ liệu nội bộ (Local Data Store / Lakehouse)** và **Trạm tích hợp Spoke Level 3**:

```
[MÔ HÌNH HIỆN TRẠNG (AS-IS) - CÁT CỨ, CHƯA TÍCH HỢP]
  [FAST Kế Toán]     [e-Office Ký Số]     [HSEQ (Đang xây)]     [IRTECH Cảng]
         │                  │                    │                    │
         └── (Rời rạc) ──────┴─── (Nhập thủ công) ─┴── (Chưa kết nối) ─┘
  [PM Mua Sắm]: Bản vẽ cũ nối dây tay đôi MESx - PMSx - FBO (ĐÃ TẠM DỪNG TIẾN ĐỘ)

--------------------------------------------------------------------------------

[MÔ HÌNH MỚI ĐỀ XUẤT (TO-BE) - TÍCH HỢP TẬP TRUNG GẮN VỚI HỒ DỮ LIỆU NỘI BỘ]

  +-----------------------------------------------------------------------------+
  |               HỆ SINH THÁI ỨNG DỤNG NGHIỆP VỤ PTSC QUẢNG NGÃI               |
  |                                                                             |
  |  [PM Mua Sắm Mới]   [FAST Kế Toán/Kho]   [e-Office Ký Số]   [HSEQ Nội Bộ]   |
  |         │                   │                   │                 │         |
  +---------┼───────────────────┼───────────────────┼─────────────────┼---------+
            │                   │                   │                 │
            ▼                   ▼                   ▼                 ▼
  +-----------------------------------------------------------------------------+
  |              HỒ DỮ LIỆU NỘI BỘ & TRẠM TÍCH HỢP SPOKE QUẢNG NGÃI             |
  |                                                                             |
  |  1. LOCAL DATA LAKEHOUSE / ODS:                                             |
  |     - Lưu trữ dữ liệu vận hành chi tiết: Mua sắm, Kho, Kế toán, HSEQ, Cảng. |
  |     - Cung cấp Dashboard điều hành nội bộ tức thời cho BGĐ PTSC Quảng Ngãi.  |
  |     - Hoạt động độc lập trong mạng LAN, không sợ đứt cáp Internet/VPN.     |
  |                                                                             |
  |  2. SPOKE INTEGRATION GATEWAY:                                              |
  |     - API Gateway & Reverse Proxy (Xác thực Token, điều phối kết nối).      |
  |     - Kafka Connector / Data Sync Agent (Lọc dữ liệu đẩy lên TCT).          |
  |     - Bộ lọc Data Quality & Bảng cách ly lỗi (Quarantine).                  |
  +--------------------------------------+--------------------------------------+
                                         │
                                         │ Kênh truyền bảo mật chuyên dụng
                                         │ IPSec VPN Site-to-Site
                                         ▼
+-------------------------------------------------------------------------------+
|                      HUB DATA PLATFORM TỔNG CÔNG TY PTSC                      |
|                                                                               |
|  [Trục Tích Hợp ESB]   <--->   [Phân Hệ MDM]   <--->   [Enterprise Lakehouse] |
|  (Kafka / API Gateway)         (Master Data Hub)       (Landing - Silver - Gold)|
|                                                                  │            |
|                                                                  ▼            |
|                                                       [Trung Tâm Báo Cáo DOC] |
+-------------------------------------------------------------------------------+
```

### 3.3. Thiết kế luồng nghiệp vụ Mua sắm - Kế toán - Ký số theo định hướng ERP dùng chung
Phần mềm Quản lý Mua sắm mới sẽ được điều chỉnh thiết kế để đáp ứng nguyên tắc **"Dữ liệu nhập một lần duy nhất (Single Data Entry)"**:
1. **Lấy Master Data từ MDM TCT:** Khi tạo PR/PO, phần mềm tự động gọi API lấy danh mục Nhà cung cấp, Vật tư chuẩn từ MDM TCT; không cho phép cán bộ tự tạo mã rác.
2. **Ký số tập trung qua e-Office:** Toàn bộ hồ sơ RFQ, Bảng so sánh giá, Hợp đồng tự động đẩy sang e-Office qua API để ký số. Trạng thái ký duyệt tự động trả về phần mềm Mua sắm.
3. **Tự động đồng bộ FAST Kế toán - Kho:** Sau khi nghiệm thu hàng hóa tại cảng/kho xưởng, hóa đơn và biên bản tự động đẩy sang FAST qua API để sinh Phiếu nhập kho và ghi nhận công nợ. Nhân viên kế toán không phải gõ lại số liệu thủ công.
4. **Tự động đồng bộ Quản lý Tài sản VTI:** Thiết bị, phương tiện mua sắm tự động đồng bộ sang VTI để theo dõi khấu hao và lịch kiểm định an toàn.

### 3.4. Cam kết tuân thủ 13 Tiêu chí Kỹ thuật Tích hợp của TCT (Mẫu PTSC-ADM-RG08-FM10)
PTSC Quảng Ngãi đưa toàn bộ 13 tiêu chí bắt buộc vào hồ sơ mời thầu:
* Bắt buộc có trường `updated_at` phục vụ CDC (Tiêu chí 3).
* Định danh khóa chính ổn định, mapping với MDM TCT (Tiêu chí 4).
* Xác thực Token OAuth2.0 / JWT tích hợp IAM Keycloak (Tiêu chí 5).
* Bàn giao đầy đủ ERD và Data Dictionary bằng tiếng Việt (Tiêu chí 6).
* Cam kết không thu phụ phí API và chống Vendor Lock-in (Tiêu chí 7, 10).
* Cơ chế Idempotent Upsert, gắn `traceId` truy vết và bảng cách ly dữ liệu lỗi Quarantine (Tiêu chí 8, 11).

---

## PHẦN IV: KẾ HOẠCH HÀNH ĐỘNG TRIỂN KHAI TẠI PTSC QUẢNG NGÃI (3 GIAI ĐOẠN)

Nhằm vừa giải quyết bài toán cấp bách nội bộ, vừa khớp nối hoàn hảo với lộ trình golive của TCT (tháng 8/2026), PTSC Quảng Ngãi xây dựng lộ trình hành động 3 giai đoạn:

### Giai đoạn 1: Khảo sát Hiện trạng, Chuẩn hóa Hồ sơ & Chuẩn bị Dự án (Tháng 3 - Tháng 5/2026)
* Thành lập Tổ công tác Data Platform PTSC Quảng Ngãi theo mô hình 5 Cấp độ của TCT (Data Owner, Data Stewards, Data Custodians).
* Rà soát danh mục các phần mềm nghiệp vụ hiện hữu (FAST, e-Office, IRTECH, HSEQ); chuẩn bị văn bản hành chính gửi các nhà cung cấp phần mềm yêu cầu phối hợp kỹ thuật theo Phụ lục PTSC-ADM-RG08-FM10.
  *(Lưu ý: Mô hình ERD và Data Dictionary yêu cầu ở đây thuần túy là cấu trúc CSDL các bảng dữ liệu nghiệp vụ - Data Schema, tuyệt đối không can thiệp hay yêu cầu bàn giao mã nguồn phần mềm - Source Code của Vendor).*
* Hoàn thiện lại Đặc tả yêu cầu kỹ thuật (TOR) Phần mềm Mua sắm theo kiến trúc Tích hợp Tập trung, đính kèm Phụ lục 13 tiêu chí kỹ thuật.
* Báo cáo Ban Giám đốc Công ty và trình Ban Dự án CĐS TCT phê duyệt phương án điều chỉnh.

### Giai đoạn 2: Ký Hợp đồng với HiPT-AITS, Xây dựng Hồ Dữ Liệu Nội Bộ & Tích hợp Thí điểm (Tháng 5 - Tháng 8/2026)
* **Ký hợp đồng dịch vụ kỹ thuật trọn gói từ A-Z với Liên danh HiPT - AITS:**
  * **Khảo sát & Bóc tách CSDL chuyên sâu:** Chuyên gia Data Architect của HiPT - AITS trực tiếp chủ trì làm việc kỹ thuật chuyên sâu với các nhà cung cấp phần mềm hiện hữu (kỹ sư FAST, BTEC, IRTECH...) để bóc tách cấu trúc CSDL (Data ERD), biên soạn Từ điển dữ liệu (Data Dictionary) và thiết lập Bảng ánh xạ dữ liệu (Data Mapping Matrix) khớp 1-1 với chuẩn TCT. (Tổ CNTT&CĐS Quảng Ngãi đóng vai trò chủ trì, điều phối và nghiệm thu kết quả).
  * Cài đặt và cấu hình **Hồ dữ liệu nội bộ (Local Data Lakehouse / ODS)** trên hạ tầng máy chủ ảo hóa sẵn có tại phòng Server Quảng Ngãi.
  * Xây dựng các luồng Data Pipelines tự động hút dữ liệu từ FAST, Phần mềm Mua sắm mới, HSEQ và Cảng IRTECH về Hồ nội bộ.
  * Xây dựng hệ thống Dashboard báo cáo quản trị điều hành sản xuất kinh doanh phục vụ Ban Giám đốc và các Phòng ban Quảng Ngãi (chạy nội bộ mạng LAN).
* **Kết nối Thử nghiệm với TCT:**
  * Phối hợp Phòng CNTT TCT thiết lập đường hầm bảo mật IPSec VPN Site-to-Site giữa Quảng Ngãi và Tòa nhà PetroVietnam Tower.
  * Cài đặt Spoke Gateway Agent và tiến hành kiểm thử UAT luồng đồng bộ dữ liệu hai chiều với Hub TCT.

### Giai đoạn 3: Golive Toàn diện, Khai thác Báo cáo DOC & Mở rộng (Sau Tháng 8/2026)
* Đưa Phần mềm Quản lý Mua sắm và Hồ dữ liệu nội bộ vào vận hành sản xuất chính thức.
* Tự động bơm dữ liệu giao dịch sạch từ Hồ nội bộ về phân vùng Tenant của Quảng Ngãi trên Hub TCT; tiếp nhận Master Data từ TCT.
* Phối hợp với TCT đưa các chỉ số KPI trọng yếu của Quảng Ngãi lên Trung tâm Điều hành Dữ liệu DOC Tổng công ty.

---

## PHẦN V: ĐỀ XUẤT CHỦ TRƯƠNG, KIẾN NGHỊ & KẾ HOẠCH HỢP TÁC VỚI LIÊN DANH HIPT - AITS

Để đảm bảo việc triển khai tại PTSC Quảng Ngãi đạt hiệu quả cao nhất, đúng pháp lý, không phát sinh chi phí đập đi xây lại và tương thích tuyệt đối với TCT, PTSC Quảng Ngãi kính đề xuất các nội dung trọng tâm sau:

### 5.1. Chấp thuận cho phép tiếp tục triển khai Phần mềm Quản lý Mua sắm
Kính đề nghị Ban Dự án CĐS và Ban NCPT Tổng công ty **xem xét chấp thuận phương án kiến trúc tích hợp tập trung đã được điều chỉnh tại Báo cáo này**, chính thức cho phép PTSC Quảng Ngãi tiếp tục triển khai các thủ tục lựa chọn đối tác phát triển Phần mềm Quản lý Mua sắm hàng hóa, dịch vụ.

### 5.2. Đề xuất Chủ trương Ký Hợp đồng Triển khai Trọn gói từ A-Z với Liên danh HiPT - AITS
PTSC Quảng Ngãi nhận thức sâu sắc rằng: Hợp đồng của TCT với Liên danh HiPT - AITS chỉ bao gồm phạm vi Cơ quan TCT; phần hạ tầng và tích hợp tại đơn vị thành viên do đơn vị tự chủ ngân sách. Nếu Quảng Ngãi tự làm hoặc thuê một đơn vị thứ ba bên ngoài để xây dựng Hồ dữ liệu nội bộ, rủi ro không tương thích về công nghệ, schema và bảo mật với Hub TCT là rất lớn.

Do đó, **PTSC Quảng Ngãi kính đề xuất Ban Chỉ đạo CĐS TCT ủng hộ chủ trương để PTSC Quảng Ngãi ký hợp đồng dịch vụ kỹ thuật trực tiếp với chính Liên danh HiPT - AITS (Tổng thầu gói HDP26 của TCT) để thực hiện trọn gói từ A-Z các hạng mục tại Quảng Ngãi:**
1. **Thiết kế chi tiết & Cài đặt Hồ dữ liệu nội bộ (Local Data Lakehouse / ODS):** Khảo sát hạ tầng server hiện có của Quảng Ngãi, cài đặt hệ thống lưu trữ và cơ sở dữ liệu phân tích tương thích hoàn toàn với nền tảng TCT;
2. **Chủ trì làm việc kỹ thuật với các Vendor phần mềm nội bộ:** Chuyên gia của HiPT - AITS trực tiếp làm việc với FAST, BTEC (eOffice), IRTECH để bóc tách mô hình CSDL (Data ERD), lập Data Dictionary và cấu hình các đường ống hút dữ liệu tự động (CDC / Batch API);
3. **Xây dựng Data Pipelines tích hợp toàn diện:** Cấu hình trọn vẹn luồng dữ liệu tự động từ FAST, Mua sắm mới, HSEQ và Cảng IRTECH đổ về Hồ dữ liệu nội bộ;
4. **Xây dựng Báo cáo Quản trị Nội bộ:** Thiết kế hệ thống Dashboard điều hành sản xuất kinh doanh theo thời gian thực phục vụ Ban Giám đốc và các phòng chức năng của PTSC Quảng Ngãi;
5. **Thiết lập kênh đồng bộ hai chiều với Hub TCT:** Đảm bảo dữ liệu từ Hồ nội bộ Quảng Ngãi đẩy lên Hub TCT không bao giờ bị lỗi và tiếp nhận Master Data mượt mà;
6. **Đào tạo chuyển giao công nghệ & Bảo hành, bảo trì trọn gói.**

### 5.3. Kế hoạch Làm việc 3 Bên và Kiến nghị TCT hỗ trợ
1. **Đăng ký buổi làm việc 3 bên:** Kính đề nghị Ban Dự án CĐS TCT chủ trì một buổi làm việc kỹ thuật giữa **BDA CĐS TCT – Liên danh HiPT-AITS – PTSC Quảng Ngãi** (trực tuyến hoặc tại VP TCT) để:
   * Bàn giao tài liệu đặc tả API/Kafka interface chuẩn của TCT;
   * Thống nhất phạm vi công việc (SOW) và kế hoạch khảo sát kỹ thuật của HiPT-AITS tại Quảng Ngãi.
2. **Đề nghị TCT hỗ trợ chính sách chi phí ưu đãi:** Kính đề nghị TCT có ý kiến định hướng với Liên danh HiPT - AITS áp dụng khung đơn giá dịch vụ ưu đãi cho PTSC Quảng Ngãi (trên cơ sở kế thừa các kết quả nghiên cứu, nền tảng công nghệ đã phát triển ở gói thầu TCT), giúp đơn vị tối ưu hóa chi phí đầu tư.
3. **Về Bản quyền & Mạng:** Kính đề nghị Phòng CNTT TCT (anh Nguyễn Văn Minh) cấp dải IP quy hoạch cho Tenant Quảng Ngãi, hướng dẫn cấu hình VPN IPSec và làm rõ cơ chế phân bổ bản quyền Power BI dùng chung.
4. **Về cơ chế làm việc và đàm phán với các Nhà cung cấp phần mềm:**
   - *Đối với các nhà cung cấp phần mềm dùng chung phổ biến trong toàn Tổng công ty (đặc biệt là Công ty CP Phần mềm FAST, Công ty BTEC - e-Office):* Kính đề nghị Ban Dự án CĐS TCT chủ trì làm việc ở cấp Tập đoàn để thống nhất **Thỏa thuận khung (Framework Agreement / MOU)** về quy chuẩn tích hợp và chính sách chi phí hỗ trợ kỹ thuật chuẩn hóa, tạo cơ sở pháp lý và kinh tế thuận lợi để các Đơn vị Thành viên (như PTSC Quảng Ngãi) làm việc với các chi nhánh đối tác, tránh tình trạng từng đơn vị bị ép giá dịch vụ riêng lẻ.
   - *Đối với các phần mềm nghiệp vụ nội bộ đặc thù của Quảng Ngãi (như IRTECH Cảng Dung Quất, VTI Quản lý tài sản, HSEQ):* PTSC Quảng Ngãi với tư cách Chủ đầu tư (Bên A trong hợp đồng) sẽ trực tiếp chủ trì đàm phán, làm việc với các nhà cung cấp; đề nghị TCT phê duyệt áp dụng chính thức Phụ lục `PTSC-ADM-RG08-FM10` làm căn cứ pháp lý bắt buộc để Quảng Ngãi yêu cầu các đối tác này phối hợp kỹ thuật với Tổng thầu Liên danh HiPT - AITS bóc tách CSDL phục vụ tích hợp.

---

## KẾT LUẬN

PTSC Quảng Ngãi cam kết chủ động nguồn lực, tuân thủ tuyệt đối chuẩn mực kỹ thuật của Tổng công ty và quyết tâm trở thành Đơn vị Thành viên kiểu mẫu đi đầu trong toàn hệ thống PTSC về chuyển đổi số và khai thác nền tảng dữ liệu.

Kính mong Ban Lãnh đạo Tổng công ty, Ban NCPT & CĐS và Ban Dự án Data Platform TCT sớm xem xét, chấp thuận các đề xuất trên để PTSC Quảng Ngãi kịp thời triển khai các bước tiếp theo đúng tiến độ chung.

Trân trọng kính báo./.

---
**Nơi nhận:**
- Như trên;
- Ban Giám đốc Công ty (để báo cáo);
- Phòng TCKT, HCNS, ĐHDA (để phối hợp);
- Lưu: VT, TK&R&D.

**TM. TỔ CÔNG TÁC CNTT & CĐS**  
*Tổ trưởng*  
*(Đã ký)*  
**ĐOÀN HÙNG HUÂN**

**XÁC NHẬN CỦA LÃNH ĐẠO PHÒNG THIẾT KẾ & R&D**  
*Trưởng phòng*  
*(Đã ký)*  
**BÙI LỰC**
