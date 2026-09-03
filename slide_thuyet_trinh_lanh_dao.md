# BÁO CÁO BAN GIÁM ĐỐC (BẢN CHÍNH THỨC V5)
## PHƯƠNG ÁN TRIỂN KHAI DATA PLATFORM & TRỤC TÍCH HỢP CÔNG TY – TCT
**File trình chiếu PowerPoint tương ứng:** [bao_cao_dataplatform_ptsc_qn_v5.pptx](file:///d:/My%20Profiles/DataPlatform/bao_cao_dataplatform_ptsc_qn_v5.pptx)  
*(Được xây dựng trên cơ sở đối chiếu trực tiếp với các tài liệu kỹ thuật và Quy chế Quản trị Dữ liệu chính thức của Tổng công ty PTSC)*

---

### MỤC LỤC & KỊCH BẢN THUYẾT TRÌNH (SPEAKER NOTES) CHI TIẾT

#### SLIDE 1: TRANG TIÊU ĐỀ
* **Tiêu đề chính:** BÁO CÁO BAN GIÁM ĐỐC: PHƯƠNG ÁN TRIỂN KHAI DATA PLATFORM VÀ TRỤC TÍCH HỢP DỮ LIỆU CÔNG TY – TCT
* **Căn cứ:** Thực hiện theo đúng Chỉ đạo mục 9 của Ban Giám đốc và Chiến lược CĐS Tổng công ty.
* **Đơn vị báo cáo:** Tổ Công tác CĐS & CNTT – PTSC Quảng Ngãi.
> 🎙️ **Kịch bản nói:** *"Kính thưa Ban Giám đốc, hôm nay bộ phận CNTT xin báo cáo toàn diện 4 nội dung theo đúng chỉ đạo số 9 của Ban Giám đốc, có đối chiếu trực tiếp với các tài liệu kỹ thuật và quy chế quản trị dữ liệu của Tổng công ty để Ban Giám đốc có bức tranh đầy đủ và an tâm nhất."*

---

#### SLIDE 2: BỐI CẢNH — TẠI SAO PHẢI LÀM TRONG NĂM 2026?
* **Lộ trình 3 Giai đoạn của TCT:**
  * *Giai đoạn 1 (2024–2025):* TCT đã nghiệm thu nền tảng lõi. Phạm vi mới chỉ áp dụng tại Cơ quan TCT, **chưa bao gồm các Đơn vị thành viên**.
  * *Giai đoạn 2 (2026–2027) - MỐC BẮT BUỘC:* Trọng tâm mở rộng đến các Đơn vị thành viên (Quảng Ngãi bắt đầu kết nối). Đây là chỉ tiêu KPI Chuyển đổi số do TCT giao.
  * *Giai đoạn 3 (2028+):* Khai thác toàn diện AI/ML và kết nối IT-OT.
* **Căn cứ pháp lý mới:** Nghị quyết số 10/NQ-HĐQT-PTSC; Luật Dữ liệu (01/7/2025) và Luật Bảo vệ DLCN 91/2025/QH15 (01/01/2026).
> 🎙️ **Kịch bản nói:** *"TCT đã hoàn thành xong Giai đoạn 1 tại Cơ quan TCT. Giai đoạn 2026-2027 chính là mốc thời hạn bắt buộc mở rộng kết nối dữ liệu từ các đơn vị thành viên. Nếu chậm trễ, đơn vị sẽ bị đánh giá chậm tiến độ theo Nghị quyết của HĐQT Tổng công ty."*

---

#### SLIDE 3: HIỆN TRẠNG DỮ LIỆU TẠI QUẢNG NGÃI
* **3 Nút thắt lớn:**
  1. *Dữ liệu phân mảnh:* 4 phần mềm (Kế toán, Nhân sự, Vật tư, Dự án) hoạt động riêng rẽ, phụ thuộc xuất Excel thủ công, mất 3–5 ngày mới có báo cáo tổng hợp.
  2. *Lệch 29 chuẩn Master Data:* Mã danh mục của QN chưa khớp 29 danh mục chuẩn do TCT ban hành, nếu đẩy lên ngay sẽ bị lỗi và từ chối.
  3. *Thiếu kỹ sư Data Engineering:* IT nội bộ giỏi mạng, máy chủ và vận hành nhưng chưa có kinh nghiệm viết đường ống dữ liệu (ETL). Tự mày mò sẽ mất 8–12 tháng và nguy cơ trễ hạn.
> 🎙️ **Kịch bản nói:** *"Nhìn thẳng vào thực tế Quảng Ngãi: 4 phần mềm rời rạc, mã danh mục chưa khớp chuẩn TCT, và anh em IT nội bộ chưa từng làm chuyên sâu về Data Engineering. Nếu tự nghiên cứu từ đầu thì rất khó kịp mốc 2026 của TCT."*

---

#### SLIDE 4: DATA PLATFORM LÀ GÌ?
* **So sánh Trước và Sau:**
  * *Trước đây (Ốc đảo):* Mỗi phần mềm là một ao nước đóng kín, cán bộ phải "xách xô Excel" ghép file thủ công, số liệu dễ vênh nhau giữa các phòng.
  * *Khi có Data Platform (Đường ống tự động):* Dữ liệu tự động hút về một trạm xử lý, làm sạch, quy đổi mã và bơm lên bảng Dashboard cho Sếp mỗi sáng. Một nguồn sự thật duy nhất (Single Source of Truth).
> 🎙️ **Kịch bản nói:** *"Nói một cách hình tượng, Data Platform giống như hệ thống đường ống nước tự động. Gom dữ liệu các phòng ban về một trạm lọc sạch rồi tự bơm lên vòi nước tại phòng Ban Giám đốc mỗi sáng, không còn cảnh xách xô Excel thủ công."*

---

#### SLIDE 5: VỊ THẾ QUẢNG NGÃI TRONG MÔ HÌNH HUB-SPOKE CỦA TCT
* **Phân loại 4 Level của TCT:**
  * *L1 (Chi nhánh):* Vận hành như 1 ban TCT.
  * *L2 (Đơn vị nhỏ):* Dùng chung Tenant trên Hub, chỉ kéo dữ liệu qua Agent/API.
  * *L3 (Đơn vị lớn - PTSC Quảng Ngãi):* Được cấp Workspace L3 riêng trên Hub TCT. **KHÔNG CẦN mua máy chủ dHCI tiền tỷ tại đơn vị**. Tận dụng máy chủ ảo (VM) sẵn có để làm trạm trung chuyển.
  * *L4 (Đơn vị đặc biệt lớn - PTSC M&C):* Tự đầu tư cụm dHCI riêng tại chỗ.
* 👉 **Kết luận:** Quảng Ngãi tiết kiệm tối đa ngân sách vì không phải mua sắm máy chủ lưu trữ đắt tiền.
> 🎙️ **Kịch bản nói:** *"Theo quy hoạch của TCT, Quảng Ngãi là Level 3 Spoke. Ban Giám đốc hoàn toàn yên tâm là chúng ta KHÔNG phải bỏ tiền mua máy chủ dHCI hàng tỷ đồng như cấp L4, mà chỉ cần tận dụng máy chủ sẵn có tại phòng Server của mình."*

---

#### SLIDE 6: TỔNG CÔNG TY ĐÃ XÂY DỰNG NHỮNG GÌ? (NỀN TẢNG HYBRID ĐÃ CÓ)
* **Cloud (Azure):** Microsoft Fabric / OneLake (dung lượng khởi điểm 20 TB), Microsoft Purview quản trị danh mục, bản quyền Power BI Enterprise, cấp sẵn phân vùng Workspace L3 cho Quảng Ngãi.
* **On-Premise (Datacenter TCT):** Cụm lưu trữ MinIO Lakehouse, Trục tích hợp doanh nghiệp (ESB), Hệ thống Quản trị dữ liệu chủ (MDM Golden Record), Trung tâm giám sát SIEM & SOC.
* **Tiêu chuẩn sẵn sàng:** Đã ban hành 29 Danh mục Master Data và 50 API chuẩn kết nối. Đã thông suốt 8 phần mềm và 35 quy trình nội bộ TCT.
> 🎙️ **Kịch bản nói:** *"TCT đã xây xong nền tảng Hybrid hoàn chỉnh: Cloud có Microsoft Fabric 20TB, On-premise có MinIO và hệ thống chuẩn hóa MDM. TCT đã mở sẵn làn đường cho Quảng Ngãi, chỉ chờ chúng ta xây đường nhánh đấu nối vào."*

---

#### SLIDE 7: QUY CHẾ QUẢN TRỊ DỮ LIỆU & CHỦ QUYỀN CỦA QUẢNG NGÃI
* **Khung Quản trị 5 Cấp theo chuẩn Petrovietnam:**
  * *Cấp 1 & 2:* Hội đồng Quản trị Dữ liệu & Hội đồng Dữ liệu khối (Chính sách vĩ mô).
  * *CẤP 3: CHỦ QUẢN DỮ LIỆU — LÃNH ĐẠO ĐƠN VỊ (QUẢNG NGÃI):* **Nắm quyền sở hữu nghiệp vụ (Business Ownership). Toàn quyền phê duyệt phân loại dữ liệu, QUYẾT ĐỊNH DỮ LIỆU NÀO ĐƯỢC CHIA SẺ VÀ DỮ LIỆU NÀO Ở LẠI NỘI BỘ. Trách nhiệm giải trình đặt ở cấp này.**
  * *Cấp 4:* Quản trị miền dữ liệu (Data Stewards - Ánh xạ kỹ thuật).
  * *Cấp 5:* Ban NCPT&CĐS TCT: Đơn vị vận hành kỹ thuật — **KHÔNG SỞ HỮU DỮ LIỆU NGHIỆP VỤ CỦA ĐƠN VỊ**.
> 🎙️ **Kịch bản nói:** *"Đây là câu trả lời then chốt cho Ban Giám đốc: Theo Quy chế quản trị dữ liệu của PTSC, Lãnh đạo Đơn vị là Chủ quản Dữ liệu Cấp 3 (Data Owner). Sếp có quyền quyết định tối cao: dữ liệu nào chuyển đi, dữ liệu nào giữ lại. Ban CNTT của TCT ở Cấp 5 chỉ là thợ kỹ thuật vận hành máy, không có quyền lấy dữ liệu nghiệp vụ của mình."*

---

#### SLIDE 8: NGUYÊN TẮC BẢO MẬT & DỮ LIỆU NÀO ĐƯỢC CHUYỂN?
* **Dữ liệu ở lại nội bộ Quảng Ngãi (On-premise):**
  * Dữ liệu chuyên ngành chi tiết, nhật trình thi công, chi tiết thiết bị xưởng.
  * Dữ liệu nhạy cảm kinh doanh: Định mức giá thầu, chi phí riêng từng dự án, biên lợi nhuận.
  * Dữ liệu cá nhân chưa xử lý (lương thưởng, hồ sơ chi tiết theo Luật BVDLCN).
  * Toàn bộ cơ sở dữ liệu sản xuất gốc đặt tại đơn vị.
* **Dữ liệu được phép đồng bộ về TCT:**
  * 29 Danh mục Master Data dùng chung (đã ánh xạ chuẩn).
  * Báo cáo số liệu tổng hợp (Aggregated Data) phục vụ hợp nhất số liệu toàn tổng.
  * Dữ liệu đã được che mờ (Data Masking) theo Nghị định 13.
  * Dữ liệu chuyển vào Tenant riêng biệt, cách ly hoàn toàn với các đơn vị thành viên khác.
> 🎙️ **Kịch bản nói:** *"Nguyên tắc của TCT rất rõ: Dữ liệu chi tiết nhạy cảm và bí mật kinh doanh lưu giữ tại Quảng Ngãi. Chỉ dữ liệu tổng hợp và danh mục dùng chung mới đồng bộ về TCT sau khi đã che mờ bảo mật. Quảng Ngãi giữ quyền kiểm soát 100%."*

---

#### SLIDE 9: KIẾN TRÚC TRỤC TÍCH HỢP HYBRID (MINIO + FABRIC)
* **Luồng 4 bước kỹ thuật:**
  1. *Nguồn dữ liệu QN:* Kế toán, Nhân sự, Vật tư, Dự án.
  2. *Trạm trung chuyển (VM tại QN):* Trích xuất bản sao ở chế độ **CHỈ ĐỌC (Read-Only)** $\rightarrow$ Ánh xạ 29 Master Data $\rightarrow$ Che mờ dữ liệu cá nhân $\rightarrow$ Mã hóa AES-256.
  3. *Kênh truyền bảo mật:* Đường hầm VPN Site-to-Site mã hóa riêng biệt nối sang TCT Datacenter.
  4. *Hạ tầng Hybrid TCT:* Lưu trữ on-prem tại MinIO Lakehouse + Bơm vào Workspace L3 trên Microsoft Fabric Cloud $\rightarrow$ Tự động kích hoạt Dashboard Power BI cho Ban Giám đốc.
> 🎙️ **Kịch bản nói:** *"Đúng kiến trúc Hybrid của TCT: Dữ liệu từ QN đi qua đường hầm VPN, tiếp đất an toàn vào MinIO on-premise và Workspace L3 trên Microsoft Fabric Cloud để xuất ra Dashboard Power BI cho Ban Giám đốc xem mỗi ngày."*

---

#### SLIDE 10: SO SÁNH 2 PHƯƠNG ÁN THEO CHỈ ĐẠO BAN GIÁM ĐỐC
* **Phương án 1 (Thuê TCT làm hộ từ A-Z):**
  * *Bất khả thi:* Ban CNTT TCT không đủ người xuống tận QN bóc tách từng phần mềm nội bộ; xếp hàng chờ TCT thì chắc chắn trễ mốc 2026; TCT chỉ làm báo cáo vĩ mô, không có báo cáo quản trị chi tiết cho Ban Giám đốc QN.
* **Phương án 2 (Phát triển riêng đồng bộ TCT - Có thuê NCC):**
  * *Khuyến nghị chọn:* NCC làm việc trực tiếp tại QN; chủ động hoàn thành trong 3–4 tháng; xây dựng đúng các Dashboard điều hành đo ni đóng giày cho Ban Giám đốc QN; tận dụng miễn phí hạ tầng đám mây TCT đã mua.
> 🎙️ **Kịch bản nói:** *"So sánh 2 phương án: TCT chỉ làm Hub chung, không đủ người làm thay QN. Chọn Phương án 2 thuê NCC phát triển riêng đồng bộ TCT là phương án khả thi duy nhất để đảm bảo tiến độ 2026 và có báo cáo phục vụ đúng Sếp."*

---

#### SLIDE 11: CƠ CẤU ĐẦU TƯ & CẤU TRÚC CHI PHÍ (THEO PHƯƠNG ÁN 3 CỦA TCT)
| STT | Cấu phần chi phí (Theo chuẩn TCT) | Nội dung & Trách nhiệm thực hiện | Dự toán ngân sách |
| :---: | :--- | :--- | :---: |
| **1** | Hạ tầng phần cứng tại Đơn vị | Tận dụng máy chủ ảo (VM) sẵn có của Quảng Ngãi | **0 VNĐ (Đơn vị tự có)** |
| **2** | Hạ tầng Cloud Hub & Bản quyền khung | Microsoft Fabric, MinIO, Purview, MDM do TCT đầu tư sẵn | **TCT ĐÃ ĐẦU TƯ** |
| **3** | Dịch vụ: Khảo sát & Thiết kế kiến trúc | Khảo sát CSDL 4 phần mềm + Lập bảng ánh xạ 29 Master Data | **[Chờ NCC báo giá sau khảo sát GĐ1]** |
| **4** | Dịch vụ: Xây dựng Trục tích hợp & ETL | Lập trình đường ống trích xuất, làm sạch, mã hóa VPN lên TCT | **[Chờ NCC báo giá sau khảo sát GĐ1]** |
| **5** | Dịch vụ: Xây dựng Dashboard Power BI | Xây dựng các bảng báo cáo quản trị phục vụ Ban Giám đốc QN | **[Chờ NCC báo giá sau khảo sát GĐ1]** |
| **6** | Đào tạo chuyển giao & Bảo hành | Bàn giao mã nguồn, đào tạo đội ngũ IT Quảng Ngãi làm chủ 100% | **[Chờ NCC báo giá sau khảo sát GĐ1]** |
| **7** | Chi phí vận hành nền tảng hàng năm | TCT phân bổ chi phí theo mức độ sử dụng thực tế (Usage-based) | **Theo cơ chế TCT ban hành** |

* **Nguyên tắc tài chính:** Tiết kiệm hàng tỷ đồng phần cứng/license nhờ TCT; chi phí thuê NCC sẽ được xác định chuẩn xác sau khi hoàn thành Giai đoạn 1 khảo sát nội bộ và nhận báo giá cạnh tranh.
> 🎙️ **Kịch bản nói:** *"Về chi phí, chúng tôi bám sát Phương án 3 của TCT: TCT đã gánh phần Cloud và phần mềm khung. Phần chi phí thuê NCC triển khai đường ống tại chỗ, chúng tôi xin phép để trống và sẽ xác định chính xác sau khi khảo sát kỹ thuật ở Giai đoạn 1, tránh đưa con số cảm tính trước khi gặp nhà cung cấp."*

---

#### SLIDE 12: ĐẦU RA CỤ THỂ — BAN GIÁM ĐỐC NHẬN ĐƯỢC GÌ?
1. *Dashboard điều hành trực quan Real-time:* Xem số liệu SXKD, doanh thu, dòng tiền, nhân sự trên PC/Mobile mỗi sáng.
2. *Dữ liệu tự động, hết phụ thuộc Excel:* Không còn cảnh chờ đợi 3–5 ngày để các phòng ban tổng hợp số liệu.
3. *Một nguồn sự thật duy nhất:* Số liệu Kế toán, Vật tư, Nhân sự đồng bộ, minh bạch khi giải trình.
4. *Hoàn thành đúng hạn chỉ tiêu CĐS của TCT:* Đáp ứng Nghị quyết 10 HĐQT PTSC và tuân thủ Luật Bảo vệ DLCN.
> 🎙️ **Kịch bản nói:** *"4 kết quả cụ thể khi dự án hoàn thành: Ban Giám đốc có Dashboard xem tức thời trên điện thoại; giải phóng sức lao động thủ công; số liệu khớp nhau 100%; và hoàn thành xuất sắc nhiệm vụ CĐS của TCT."*

---

#### SLIDE 13: KẾ HOẠCH TRIỂN KHAI 3 GIAI ĐOẠN
* **Giai đoạn 1 (Tháng 3–4/2026): Khảo sát & Đề bài kỹ thuật — NỘI BỘ TỰ CHỦ TRÌ (CHI PHÍ 0 VNĐ)**
  * Thành lập Tổ công tác Data Platform nội bộ.
  * Khảo sát CSDL 4 phần mềm nghiệp vụ và lập bảng ánh xạ 29 Master Data.
  * Lập Hồ sơ yêu cầu kỹ thuật (TOR) để mời các NCC gửi đề xuất và báo giá cạnh tranh.
* **Giai đoạn 2 (Tháng 5–7/2026): Lựa chọn NCC & Triển khai Trục tích hợp (Giai đoạn chính)**
  * Lựa chọn NCC tối ưu; dựng trạm trung chuyển trên VM; viết đường ống ETL và kiểm thử thông luồng lên TCT.
* **Giai đoạn 3 (Tháng 8/2026 trở đi): Bàn giao & Khai thác**
  * Nghiệm thu; bàn giao mã nguồn; đào tạo IT Quảng Ngãi làm chủ 100%; đưa vào sử dụng Dashboard Power BI.
> 🎙️ **Kịch bản nói:** *"Lộ trình 3 giai đoạn rất rõ: Giai đoạn 1 nội bộ tự làm hoàn toàn miễn phí trong 2 tháng để ra bài toán chuẩn; sau đó mới tổ chức mời thầu NCC trong Giai đoạn 2; và Giai đoạn 3 là nghiệm thu, bàn giao để IT nội bộ làm chủ."*

---

#### SLIDE 14: KIẾN NGHỊ BAN GIÁM ĐỐC PHÊ DUYỆT (CALL TO ACTION)
1. **Phê duyệt chủ trương lựa chọn Phương án 2:** Công ty chủ động phát triển Trục tích hợp dữ liệu riêng đồng bộ với TCT (thuê NCC chuyên nghiệp tư vấn & triển khai).
2. **Phê duyệt thành lập Tổ công tác Data Platform nội bộ:** Gồm Bộ phận CNTT chủ trì kỹ thuật và Key users các phòng ban để thực hiện ngay Giai đoạn 1 (chi phí 0 VNĐ).
3. **Cho phép tiếp xúc các Nhà cung cấp (NCC) để lấy báo giá cạnh tranh:** Căn cứ trên bài toán kiến trúc đã xây dựng để lấy báo giá chính thức, hoàn thiện dự toán chi tiết trình Ban Giám đốc phê duyệt trước khi ký kết.
> 🎙️ **Kịch bản nói:** *"Kính thưa Ban Giám đốc, bộ phận CNTT kính đề xuất Ban Giám đốc thông qua 3 chủ trương nêu trên để chúng tôi kịp triển khai ngay Giai đoạn 1 trong tháng 3 và đảm bảo tiến độ chung của Tổng công ty. Xin trân trọng cảm ơn Ban Giám đốc!"*

---

#### SLIDE 15: TRANG KẾT THÚC
* Lời cảm ơn và kính mời Ban Giám đốc cho ý kiến chỉ đạo.
