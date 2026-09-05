# BÁO CÁO BAN GIÁM ĐỐC (BẢN CHÍNH THỨC V6)
## PHƯƠNG ÁN TRIỂN KHAI DATA PLATFORM & TRỤC TÍCH HỢP CÔNG TY – TCT
**File trình chiếu PowerPoint tương ứng:** [bao_cao_dataplatform_ptsc_qn_v6.pptx](file:///d:/My%20Profiles/DataPlatform/bao_cao_dataplatform_ptsc_qn_v6.pptx)  
*(Được xây dựng trên cơ sở đối chiếu trực tiếp với các tài liệu kỹ thuật và Quy chế Quản trị Dữ liệu chính thức của Tổng công ty PTSC)*

---

### MẠCH NỘI DUNG 4 PHẦN CHẶT CHẼ
1. **Phần 1 (Slide 1–4): Bản chất Data Platform của TCT** — Tại sao TCT làm, Nó thực ra là gì (3 tầng kiến trúc), TCT đã mua sắm và hoàn thành những gì?
2. **Phần 2 (Slide 5–8): Vị thế & Chi tiết tại Quảng Ngãi** — Vị thế Level 3 Spoke, 3 nút thắt phần mềm tại QN, Chủ quyền Data Owner Cấp 3 của Lãnh đạo, Nguyên tắc bảo mật On-premise vs Hub.
3. **Phần 3 (Slide 9–11): Cách thức kết nối Trục tích hợp** — Sơ đồ luồng 4 bước dữ liệu, So sánh 2 phương án (TCT làm hộ vs Thuê NCC), Cơ cấu chi phí Phương án 3 của TCT.
4. **Phần 4 (Slide 12–15): Kế hoạch hành động & Việc cần làm ở Giai đoạn tới** — 4 Giá trị cụ thể & Bài toán Quick-Win 4–6 tuần, Kế hoạch 3 Giai đoạn (Trọng tâm GĐ1), Cam kết nguồn lực các phòng ban & An toàn NCC, Kiến nghị Ban Giám đốc phê duyệt.

---

### MỤC LỤC & KỊCH BẢN THUYẾT TRÌNH (SPEAKER NOTES) CHI TIẾT

#### SLIDE 1: TRANG TIÊU ĐỀ
* **Tiêu đề chính:** BÁO CÁO BAN GIÁM ĐỐC: PHƯƠNG ÁN TRIỂN KHAI DATA PLATFORM VÀ TRỤC TÍCH HỢP DỮ LIỆU CÔNG TY – TCT
* **Căn cứ:** Thực hiện theo đúng Chỉ đạo mục 9 của Ban Giám đốc và Chiến lược CĐS Tổng công ty.
* **Đơn vị báo cáo:** Tổ Công tác CĐS & CNTT – PTSC Quảng Ngãi.
> 🎙️ **Kịch bản nói:** *"Kính thưa Ban Giám đốc, hôm nay bộ phận CNTT xin báo cáo toàn diện phương án triển khai Data Platform theo đúng chỉ đạo số 9 của Ban Giám đốc. Bài báo cáo được cấu trúc mạch lạc thành 4 phần: đi từ bản chất giải pháp của TCT để Lãnh đạo hiểu rõ nó thực ra là gì, sau đó đến vị thế và hiện trạng tại Quảng Ngãi, cách thức kết nối trục dữ liệu, và cuối cùng là các việc cụ thể chúng ta cần làm ngay ở giai đoạn tới."*

---

#### SLIDE 2: BỨC TRANH TOÀN TỔNG — TẠI SAO TỔNG CÔNG TY XÂY DỰNG DATA PLATFORM?
* **Thực trạng toàn tổng theo tài liệu TCT:**
  * 80% dữ liệu SXKD, nhân lực, công trình nằm phân tán ở hơn 10 Đơn vị thành viên (như Quảng Ngãi, M&C, Dịch vụ...).
  * Tồn tại hàng chục "Ốc đảo phần mềm" cát cứ, không có ngôn ngữ chung.
  * TCT mất 2–3 tuần xin file Excel ghép số thủ công để nộp Tập đoàn PVN, số liệu vênh lệch liên tục.
  * Nghĩa vụ tuân thủ pháp lý mới: Luật Dữ liệu, Luật BVDLCN, Quy chế Quản trị Dữ liệu Petrovietnam.
* **Mục tiêu của TCT:**
  * Xây dựng Hồ dữ liệu dùng chung (Data Lakehouse) gom dữ liệu toàn tổng về một nơi.
  * Ban hành 29 Danh mục Master Data làm "ngôn ngữ chuẩn chung".
  * Nghị quyết 10/NQ-HĐQT bắt buộc các ĐVTV phải hoàn thành kết nối trong giai đoạn 2026–2027.
> 🎙️ **Kịch bản nói:** *"Kính thưa Ban Giám đốc, tại sao TCT lại rầm rộ triển khai Data Platform? Vì thực tế 80% số liệu sản xuất kinh doanh nằm tại các đơn vị thành viên như chúng ta, chứ không nằm ở văn phòng TCT. Trước đây TCT muốn tổng hợp số liệu nộp Tập đoàn PVN phải gửi công văn xin từng file Excel của từng công ty con, mất cả tháng mà số liệu vẫn vênh nhau. Do đó, TCT ban hành Nghị quyết bắt buộc xây dựng Data Platform dùng chung để kết nối dữ liệu toàn tổng."*

---

#### SLIDE 3: DATA PLATFORM THỰC RA LÀ GÌ? (ĐỊNH NGHĨA & 3 TẦNG BẢN CHẤT)
* **Khẳng định cốt lõi:** Data Platform **KHÔNG PHẢI là phần mềm mới bắt nhân viên gõ máy nhập liệu thêm**. Không thay thế các phần mềm hiện hữu (Kế toán, HRM, Vật tư giữ nguyên).
* **Bản chất 3 tầng kỹ thuật (theo tài liệu TCT):**
  1. *Tầng 1 (Thu thập - Ingestion):* Các đường ống tự động hút bản sao dữ liệu (Read-Only) từ các phần mềm đang chạy ngầm ban đêm, không làm phiền ai.
  2. *Tầng 2 (Hồ chứa & Chuẩn hóa - Lakehouse + MDM):* Trạm gom dữ liệu về, lọc rác, khử trùng lặp và tự động quy đổi mã theo 29 danh mục chuẩn của TCT (Tạo Một nguồn sự thật duy nhất).
  3. *Tầng 3 (Báo cáo thông minh - Power BI Dashboard):* Vòi nước sạch cho Lãnh đạo — xem số liệu SXKD, dòng tiền, nhân sự tức thời trên điện thoại/laptop mỗi sáng.
> 🎙️ **Kịch bản nói:** *"Nói một cách dân dã nhất để Ban Giám đốc hình dung: Hiện nay mỗi phòng ban của chúng ta giống như một cái giếng nước riêng. Mỗi lần Sếp cần báo cáo, nhân viên phải xách từng xô nước (làm từng file Excel) mang lên. Data Platform chính là Mạng lưới đường ống ngầm và Nhà máy lọc nước: Nó tự hút nước từ các giếng, lọc sạch phèn, quy đổi chuẩn mã TCT, rồi lắp sẵn một cái vòi nước sạch là màn hình Dashboard ngay trên bàn làm việc của Sếp. Sếp chỉ việc mở điện thoại là thấy toàn cảnh công ty mỗi sáng."*

---

#### SLIDE 4: TỔNG CÔNG TY ĐÃ ĐẦU TƯ NHỮNG GÌ? (NỀN TẢNG HYBRID ĐÃ HOÀN THÀNH)
* **Hạ tầng Cloud TCT đã mua:** Microsoft Fabric OneLake (20TB), bản quyền Power BI Enterprise, Microsoft Purview, và cấp sẵn phân vùng Workspace L3 cho Quảng Ngãi.
* **Hạ tầng On-premise tại Datacenter TCT:** Cụm lưu trữ MinIO Lakehouse, Trục tích hợp ESB, Hệ thống MDM 29 danh mục, Trung tâm giám sát an ninh mạng SIEM/SOC.
* 👉 **Ý nghĩa lớn với Quảng Ngãi:** TCT đã chi hàng chục tỷ làm xong "Đường cao tốc" và mở sẵn làn riêng cho Quảng Ngãi. **Quảng Ngãi KHÔNG PHẢI BỎ TIỀN MUA MÁY CHỦ ĐẮT TIỀN**, mà chỉ cần xây dựng đường nhánh (Trạm trung chuyển) để đấu nối vào.
> 🎙️ **Kịch bản nói:** *"TCT đã hoàn thành Giai đoạn 1 và đầu tư trọn gói nền tảng Hybrid rất đắt tiền: Cloud có Microsoft Fabric 20TB và bản quyền Power BI, On-premise có MinIO và hệ thống chuẩn hóa MDM. TCT đã trải thảm xong đường cao tốc cho chúng ta. Quảng Ngãi tiết kiệm được hàng tỷ đồng tiền máy chủ và bản quyền phần mềm."*

---

#### SLIDE 5: VỊ THẾ QUẢNG NGÃI TRONG MÔ HÌNH HUB-SPOKE CỦA TCT (LEVEL 3)
* **Phân loại 4 Level của TCT:**
  * L1 (Chi nhánh) & L2 (Đơn vị nhỏ): Dùng chung hệ thống, không có không gian riêng.
  * **L3 (Đơn vị lớn — PTSC Quảng Ngãi):** Được cấp Workspace L3 riêng biệt hoàn toàn trên Hub TCT. Tận dụng máy chủ ảo (VM) sẵn có tại QN làm trạm trung chuyển. Không cần mua máy chủ dHCI.
  * L4 (Đơn vị đặc biệt lớn — PTSC M&C): Tự đầu tư cụm máy chủ dHCI riêng tại chỗ.
* 👉 **Kết luận:** Quảng Ngãi vừa có chủ quyền không gian riêng, vừa tiết kiệm tối đa ngân sách đầu tư.
> 🎙️ **Kịch bản nói:** *"Trong 4 cấp phân loại của TCT, Quảng Ngãi là Level 3 Spoke. Ban Giám đốc hoàn toàn an tâm là chúng ta không phải bỏ ra hàng chục tỷ mua sắm máy chủ dHCI như đơn vị L4 (M&C), mà được TCT cấp riêng một phân vùng dữ liệu độc lập trên hệ thống của TCT."*

---

#### SLIDE 6: HIỆN TRẠNG DỮ LIỆU TẠI QUẢNG NGÃI (3 NÚT THẮT CẦN THÁO GỠ)
* **3 Nút thắt lớn:**
  1. *Dữ liệu phân mảnh (Silo):* 4 phần mềm (Kế toán, Nhân sự, Vật tư, Dự án) hoạt động riêng rẽ, chuyển số liệu bằng Excel thủ công, mất 3–5 ngày mới có báo cáo tổng hợp.
  2. *Lệch 29 chuẩn Master Data:* Mã danh mục của QN chưa khớp 29 danh mục chuẩn do TCT ban hành, nếu đẩy lên ngay sẽ bị hệ thống TCT từ chối tiếp nhận.
  3. *Thiếu kỹ sư Data Engineering:* IT nội bộ giỏi hạ tầng, mạng và hỗ trợ nhưng chưa từng viết đường ống dữ liệu (ETL). Tự mày mò sẽ mất 8–12 tháng và nguy cơ trễ hạn 2026.
> 🎙️ **Kịch bản nói:** *"Nhìn thẳng vào thực tế Quảng Ngãi: 4 phần mềm đang cát cứ, mã danh mục chưa khớp 29 chuẩn của TCT, và anh em IT nội bộ vốn chỉ quen quản trị mạng chứ chưa có kinh nghiệm viết đường ống dữ liệu lớn. Nếu để anh em tự nghiên cứu thì chắc chắn không kịp mốc đánh giá 2026 của TCT."*

---

#### SLIDE 7: QUY CHẾ QUẢN TRỊ DỮ LIỆU TCT & CHỦ QUYỀN CỦA QUẢNG NGÃI
* **Khung Quản trị 5 Cấp theo chuẩn Petrovietnam:**
  * Cấp 1 & 2: Hội đồng Quản trị Dữ liệu TCT (Chính sách vĩ mô).
  * **CẤP 3: CHỦ QUẢN DỮ LIỆU (DATA OWNER) — LÃNH ĐẠO ĐƠN VỊ THÀNH VIÊN (QUẢNG NGÃI):** Nắm quyền sở hữu nghiệp vụ (Business Ownership). Toàn quyền quyết định dữ liệu nào được chia sẻ và dữ liệu nào giữ lại nội bộ. Trách nhiệm giải trình đặt ở cấp này.
  * Cấp 4: Quản trị miền dữ liệu (Key users các phòng ban).
  * Cấp 5: Ban NCPT&CĐS TCT: Đơn vị vận hành kỹ thuật — **TUYỆT ĐỐI KHÔNG SỞ HỮU DỮ LIỆU NGHIỆP VỤ CỦA ĐƠN VỊ**.
> 🎙️ **Kịch bản nói:** *"Đây là điều Ban Giám đốc băn khoăn nhất: Liệu TCT có lấy hết dữ liệu của mình không? Câu trả lời trong Quy chế của TCT nêu rất rõ: Lãnh đạo Đơn vị là Data Owner Cấp 3. Sếp có quyền quyết định tối cao dữ liệu nào chuyển đi, dữ liệu nào giữ lại. Ban CNTT của TCT ở Cấp 5 chỉ là bộ phận vận hành kỹ thuật hạ tầng, không có quyền can thiệp vào dữ liệu nghiệp vụ của đơn vị."*

---

#### SLIDE 8: NGUYÊN TẮC BẢO MẬT: DỮ LIỆU NÀO Ở LẠI, NÀO ĐI?
* **Dữ liệu ở lại nội bộ Quảng Ngãi 100% (On-premise):**
  * Định mức đơn giá thầu, chi phí riêng từng dự án, biên lợi nhuận, chiến lược thương mại.
  * Nhật trình thi công, nhật ký xưởng, thông số bảo dưỡng thiết bị chi tiết.
  * Bảng lương chi tiết, hồ sơ sức khỏe CBNV theo Luật BVDLCN.
  * Toàn bộ cơ sở dữ liệu sản xuất gốc đặt tại đơn vị.
* **Dữ liệu được phép đồng bộ về TCT Hub:**
  * 29 Danh mục Master Data dùng chung đã ánh xạ chuẩn.
  * Báo cáo số liệu tổng hợp (Doanh thu tổng, Sản lượng tổng, Số lượng lao động).
  * Dữ liệu đã che mờ (Data Masking) theo Nghị định 13.
  * Chuyển vào Tenant L3 cách ly hoàn toàn với các đơn vị khác.
> 🎙️ **Kịch bản nói:** *"Nguyên tắc của TCT rất sòng phẳng: Toàn bộ bí mật kinh doanh, giá thầu và dữ liệu cá nhân chi tiết nằm lại 100% tại máy chủ Quảng Ngãi. Chỉ các số liệu tổng hợp và danh mục mã dùng chung mới chuyển lên TCT sau khi đã che mờ bảo mật. Quảng Ngãi kiểm soát hoàn toàn."*

---

#### SLIDE 9: KIẾN TRÚC TRỤC TÍCH HỢP HYBRID (DỮ LIỆU ĐI NHƯ THẾ NÀO?)
* **Luồng 4 bước kỹ thuật:**
  1. *Nguồn dữ liệu QN:* Kế toán, Nhân sự, Vật tư, Dự án (giữ nguyên hiện trạng).
  2. *Trạm trung chuyển (VM tại QN):* Trích xuất bản sao **CHỈ ĐỌC (Read-Only)** $\rightarrow$ Lọc sạch $\rightarrow$ Ánh xạ 29 Master Data $\rightarrow$ Che mờ dữ liệu cá nhân $\rightarrow$ Mã hóa AES-256.
  3. *Kênh truyền bảo mật:* Đường hầm VPN Site-to-Site nối thẳng về Datacenter TCT, tuân thủ quy hoạch 8 Zones an toàn thông tin.
  4. *Hạ tầng Hybrid TCT:* Lưu trữ tại MinIO On-premise + Bơm vào Workspace L3 trên Microsoft Fabric $\rightarrow$ Kích hoạt Dashboard Power BI cho Ban Giám đốc.
> 🎙️ **Kịch bản nói:** *"Dữ liệu sẽ chảy qua 4 bước: Từ phần mềm nội bộ, trạm trung chuyển VM tại QN hút bản sao chỉ đọc, tự động lọc sạch và đổi mã chuẩn TCT, mã hóa đường hầm VPN đẩy lên Workspace của mình trên TCT để xuất ra báo cáo cho Ban Giám đốc."*

---

#### SLIDE 10: SO SÁNH 2 PHƯƠNG ÁN THEO CHỈ ĐẠO BAN GIÁM ĐỐC
* **Phương án 1 (Thuê TCT làm hộ từ A–Z):**
  * *Bất khả thi:* Ban CNTT TCT không đủ người xuống cắm chốt tại QN; xếp hàng sau hơn 10 đơn vị thì chắc chắn trễ mốc 2026; TCT chỉ xây báo cáo vĩ mô phục vụ TCT, không xây Dashboard điều hành cho Sếp QN.
* **Phương án 2 (Phát triển riêng đồng bộ TCT - Có thuê NCC):**
  * *Khuyến nghị chọn:* NCC chuyên nghiệp cử kỹ sư làm việc trực tiếp tại QN; hoàn thành trong 3–4 tháng; đo ni đóng giày các Dashboard phục vụ đúng Ban Giám đốc QN; bàn giao mã nguồn 100% và tận dụng miễn phí hạ tầng TCT.
> 🎙️ **Kịch bản nói:** *"So sánh 2 phương án: TCT chỉ làm Hub chung, không thể làm thay cho mình được. Phương án 2 thuê NCC chuyên nghiệp phát triển riêng đồng bộ với chuẩn TCT là phương án khả thi duy nhất để vừa kịp tiến độ năm 2026, vừa có Dashboard phục vụ đúng nhu cầu điều hành của Ban Giám đốc."*

---

#### SLIDE 11: CƠ CẤU ĐẦU TƯ & CẤU TRÚC CHI PHÍ (THEO PHƯƠNG ÁN 3 CỦA TCT)
* **Cấu phần chi phí chuẩn TCT:**
  * 1. Hạ tầng phần cứng tại Đơn vị: Tận dụng máy chủ ảo (VM) sẵn có $\rightarrow$ **0 VNĐ (Tự có)**.
  * 2. Hạ tầng Cloud Hub & Bản quyền khung: Microsoft Fabric, MinIO, PowerBI $\rightarrow$ **TCT ĐÃ ĐẦU TƯ**.
  * 3. Dịch vụ Khảo sát, Thiết kế kiến trúc, Viết luồng ETL, Xây Dashboard, Đào tạo $\rightarrow$ **[Chờ NCC báo giá sau khảo sát GĐ1]**.
  * 4. Phí duy trì nền tảng hàng năm: TCT phân bổ theo mức độ sử dụng thực tế.
* 👉 **Nguyên tắc tài chính:** Tiết kiệm hàng tỷ đồng phần cứng/license; chi phí thuê NCC sẽ được xác định chính xác sau Giai đoạn 1 khảo sát nội bộ và nhận báo giá cạnh tranh.
> 🎙️ **Kịch bản nói:** *"Về chi phí, chúng tôi bám sát Phương án 3 của TCT: TCT đã gánh phần Cloud và phần mềm khung. Chi phí thuê NCC triển khai tại chỗ, chúng tôi xin phép để trống và sẽ xác định chính xác sau khi khảo sát kỹ thuật ở Giai đoạn 1 để có báo giá cạnh tranh minh bạch nhất."*

---

#### SLIDE 12: ĐẦU RA CHO BAN GIÁM ĐỐC & BÀI TOÁN "THẮNG NHANH" (QUICK-WIN)
* **4 Giá trị Ban Giám đốc nhận được:**
  1. Dashboard điều hành trực quan xem trên Mobile/PC mỗi sáng trước giờ giao ban.
  2. Chấm dứt phụ thuộc báo cáo Excel thủ công, không còn chờ 3–5 ngày.
  3. Một nguồn sự thật duy nhất: Số liệu Kế toán, Dự án, Vật tư đồng bộ 100%.
  4. Hoàn thành xuất sắc nhiệm vụ Chuyển đổi số của TCT.
* **Bài toán thí điểm Quick-Win (4–6 tuần):**
  * Đề xuất thí điểm trước mảng **"Quản lý Doanh thu & Chi phí Dự án trọng điểm"**.
  * Tuần 1–2: Trích xuất CSDL Dự án & Kế toán (Read-only).
  * Tuần 3–4: Viết luồng ETL làm sạch & ánh xạ mã công trình.
  * Tuần 5–6: Bàn giao Dashboard đầu tiên cho Ban Giám đốc trải nghiệm trên điện thoại.
> 🎙️ **Kịch bản nói:** *"Để Ban Giám đốc không phải chờ đợi lâu, chúng tôi đề xuất làm ngay 1 bài toán thí điểm thắng nhanh trong 4 đến 6 tuần đầu tiên: Dashboard Doanh thu và Chi phí Dự án. Chỉ sau hơn 1 tháng, Sếp sẽ cầm điện thoại xem được số liệu thực tế ngay, tạo niềm tin cho toàn bộ dự án."*

---

#### SLIDE 13: KẾ HOẠCH HÀNH ĐỘNG 3 GIAI ĐOẠN (TRỌNG TÂM GIAI ĐOẠN 1)
* **Giai đoạn 1 (Tháng 3–4/2026): Khảo sát & Đề bài kỹ thuật — NỘI BỘ TỰ LÀM (CHI PHÍ 0 VNĐ):**
  * 1. Thành lập Tổ công tác Data Platform nội bộ (CNTT + Key Users).
  * 2. Lập danh mục nguồn dữ liệu 4 phần mềm (Data Catalog).
  * 3. Lập bảng đối chiếu ánh xạ với 29 Master Data của TCT.
  * 4. Hoàn thiện Hồ sơ yêu cầu kỹ thuật (TOR) để mời các NCC gửi báo giá cạnh tranh.
* **Giai đoạn 2 (Tháng 5–7/2026): Triển khai Trục tích hợp (Thuê NCC):**
  * Lựa chọn NCC, cấp VM trung chuyển, viết luồng ETL, cấu hình VPN và thiết kế Dashboard.
* **Giai đoạn 3 (Tháng 8/2026 trở đi): Bàn giao & Khai thác (IT Quảng Ngãi làm chủ):**
  * Nghiệm thu, bàn giao 100% mã nguồn, đưa vào sử dụng chính thức và báo cáo hoàn thành KPI TCT.
> 🎙️ **Kịch bản nói:** *"Lộ trình 3 giai đoạn rất rành mạch: Giai đoạn 1 nội bộ tự làm hoàn toàn miễn phí trong 2 tháng để ra bài toán chuẩn; sau đó mới tổ chức mời thầu NCC trong Giai đoạn 2; và Giai đoạn 3 là nghiệm thu, bàn giao để IT nội bộ làm chủ 100%."*

---

#### SLIDE 14: CAM KẾT NGUỒN LỰC CÁC PHÒNG BAN & AN TOÀN KHI THUÊ NCC
* **Cam kết với các phòng ban (Không gây quá tải):**
  * Không phát sinh công việc nhập liệu thêm (hệ thống tự đọc ngầm).
  * Key Users mỗi phòng chỉ tham gia 2–3 buổi phỏng vấn (1–2 giờ/buổi).
  * 90% công việc kỹ thuật do CNTT và NCC đảm nhiệm.
* **Cam kết an toàn khi thuê NCC:**
  * Chỉ cấp quyền Đọc (Read-Only) trên bản sao CSDL.
  * Ký cam kết bảo mật thông tin (NDA) theo Luật BVDLCN.
  * Bắt buộc bàn giao 100% mã nguồn và tài liệu kiến trúc.
  * Thiết kế hệ thống nội bộ chạy độc lập, không lo bị gián đoạn nếu TCT chậm trễ.
> 🎙️ **Kịch bản nói:** *"Slide này giải tỏa 2 mối lo lớn nhất: Các phòng ban yên tâm không bị đè thêm việc gõ Excel, và Ban Giám đốc hoàn toàn yên tâm về an toàn dữ liệu khi thuê NCC vì chỉ cấp quyền đọc bản sao và bàn giao 100% mã nguồn."*

---

#### SLIDE 15: KIẾN NGHỊ BAN GIÁM ĐỐC PHÊ DUYỆT (CALL TO ACTION)
1. **Phê duyệt chủ trương lựa chọn Phương án 2:** Công ty chủ động phát triển Trục tích hợp dữ liệu riêng đồng bộ với TCT (thuê NCC chuyên nghiệp tư vấn & triển khai).
2. **Phê duyệt thành lập Tổ công tác Data Platform nội bộ:** Gồm Bộ phận CNTT chủ trì kỹ thuật và Key users các phòng ban để thực hiện ngay Giai đoạn 1 (chi phí 0 VNĐ).
3. **Cho phép tiếp xúc các NCC để lấy báo giá cạnh tranh:** Căn cứ trên bài toán kỹ thuật để hoàn thiện dự toán chi tiết trình Ban Giám đốc phê duyệt trước khi ký kết.
> 🎙️ **Kịch bản nói:** *"Kính thưa Ban Giám đốc, bộ phận CNTT kính đề xuất Ban Giám đốc thông qua 3 chủ trương nêu trên để chúng tôi kịp triển khai ngay Giai đoạn 1 trong tháng 3 và đảm bảo tiến độ chung của Tổng công ty. Xin trân trọng cảm ơn Ban Giám đốc!"*
