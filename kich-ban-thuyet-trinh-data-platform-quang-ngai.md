# KỊCH BẢN THUYẾT TRÌNH — PTSC DATA PLATFORM (BẢN CHO LÃNH ĐẠO)

> **Slide đi kèm:** `slide-thuyet-trinh-lanh-dao-data-platform-quang-ngai.html` (26 slide)
> **Người trình bày:** Cán bộ IT, đầu mối dự án Data Platform, PTSC Quảng Ngãi *(xưng **em** với Giám đốc & Ban Lãnh đạo)*
> **Nhịp thao tác mới trên slide:** Deck phân tách rõ **9 slide kể chuyện / chốt ý** (`2, 3, 4, 5, 10, 19, 21, 25, 26`) giữ chế độ làm mờ mặc định (chỉ câu hỏi lớn hiện rõ, bấm `Space` / `↓` hoặc click vào từng ô mờ để mở sáng từng lớp) và **17 slide sơ đồ, mô phỏng & bảng số liệu** (`1, 6–9, 11–18, 20, 22–24`) hiện rõ toàn bộ ngay từ đầu để em thao tác trực tiếp ngay trên sơ đồ/nút bấm.
> **Phím tắt:** `→` sang trang · `Space` / `↓` mở từng lớp · `↑` lùi lại · `N` xem ghi chú.

---

## 0. TƯ THẾ ĐỨNG & NGUYÊN TẮC NÓI VỚI LÃNH ĐẠO

### Tư thế của em
Em là người mới về đơn vị, đóng vai **đầu mối tổng hợp hồ sơ từ Tổng công ty và các phòng ban**, mang lên báo cáo Giám đốc để **xin định hướng và chốt quyết định** — không phải lên giảng coông nghệ.

### 3 nguyên tắc nói để lãnh đạo nghe là hiểu ngay
1. **Không đọc nguyên văn thuật ngữ tiếng Anh:** Trên slide có chữ *Hybrid, Hub–Spoke–Tenant, CDC, ESB, Lakehouse, MDM, SIEM* (vì đó là tên gọi trong hồ sơ TCT), nhưng **miệng em phải dịch ngay sang hình ảnh đời thường**:
   - *Hybrid* → **"Kết hợp: giữ đồ nhạy cảm ở nhà, chỉ đưa báo cáo sạch lên mây"**
   - *Hub – L3 Tenant* → **"Thuê một phòng riêng có khóa ngay trong trụ sở máy chủ của Tổng công ty"**
   - *L4 Spoke* → **"Tự dựng một trạm máy chủ riêng ở Quảng Ngãi và tự nuôi người trực"**
   - *ESB* → **"Một cửa khẩu / trạm trung chuyển chung"**
   - *CDC đọc log* → **"Đọc từ cuốn sổ ghi chép phụ của phần mềm, không động vào lúc nhân viên đang nhập"**
   - *Landing Zone* → **"Phòng đệm riêng của Quảng Ngãi để mình tự kiểm và bấm duyệt trước khi giao"**
   - *MDM / Golden Record* → **"Một hồ sơ chuẩn duy nhất"**
   - *SIEM / Audit log* → **"Camera an ninh và sổ nhật ký ra vào không xóa được"**
2. **Mỗi slide chỉ mở đúng thứ đang nói:** Ở **9 slide có nhịp mở dần** (`2, 3, 4, 5, 10, 19, 21, 25, 26`), Giám đốc không bị phân tâm đọc chữ trước — cứ hỏi xong → bấm `Space` mở đúng ý đó → nói gọn 2–3 câu. Còn **17 slide sơ đồ, mô phỏng & bảng số liệu** (`1, 6–9, 11–18, 20, 22–24`) đã hiện đủ ngay từ đầu để em vừa chỉ vừa bấm nút minh họa trực tiếp.
3. **Minh bạch tuyệt đối:**
   - Ví dụ `NCC-001` / `KH-118` và số liệu Time-Travel: **luôn nói "đây là ví dụ minh họa"**.
   - Chi phí L3/L4: **luôn nói "ước tính tham khảo, chưa phải số của PTSC"**.
   - Cái gì chưa chốt (chọn L3 hay L4, lịch khảo sát GĐ2A, bản nháp PDT27, tỷ lệ chia tiền): **nói thẳng "chưa chốt, chờ Tổng công ty"**.
   - Tuyệt đối không nói *"cách ly tuyệt đối"* hay *"Tổng công ty không lấy dữ liệu của mình"*.

---

## 1. MỞ ĐẦU (≈ 2,5 phút)

### Slide 1 — Trang bìa *(Mở sẵn hoàn chỉnh)* ⏱ 30 giây
**Em nói:**
> "Kính thưa Giám đốc và Ban Lãnh đạo. Từ thứ Hai tuần tới 30/11, đoàn khảo sát của Tổng công ty sẽ về làm việc tại đơn vị mình về dự án Data Platform — nền tảng dữ liệu dùng chung toàn PTSC.
> Hôm nay em không đến để nói về kỹ thuật. Em xin phép báo cáo nhanh 3 việc: nền tảng này giải quyết vướng mắc gì cho mình, Quảng Ngãi mình đang đứng ở đâu, và cuối buổi em xin Giám đốc chốt 4 việc để đơn vị chủ động đón đoàn."

*(Bấm `→` sang Slide 2.)*

---

### Slide 2 — *“Tại sao báo cáo từ 6 phần mềm cũ đang chậm và lệch số?”* ⏱ 2 phút
*(Vừa sang slide, chỉ câu hỏi hiện rõ, 3 ô bên dưới đang mờ — đọc câu hỏi rồi mới bấm từng nhịp.)*

- **[Bấm `Space` — Lớp 1 · Kẹt trong 6 phần mềm riêng]:**
  > "Thứ nhất, hiện tại đơn vị mình có 6 phần mềm: Cảng, kế toán FAST, vật tư bảo dưỡng MESX, Bán hàng, E-Office và nhân sự HRM. Mỗi phần mềm giống như một phòng riêng đóng cửa, không tự nói chuyện được với nhau."
- **[Bấm `Space` — Lớp 2 · 310 báo cáo ghép tay Excel]:**
  > "Thứ hai, vì không liên thông nên mỗi khi cần báo cáo tổng hợp, anh em vẫn phải xuất Excel ra ghép tay. Theo thống kê của Tổng công ty, toàn PTSC đang có tới 310 báo cáo rời rạc như vậy, vừa mất thời gian vừa dễ sai." *(lưu ý: 310 là số toàn PTSC)*
- **[Bấm `Space` — Lớp 3 · Lệch mã danh mục + Áp lực pháp lý]:**
  > "Thứ ba, mỗi phần mềm đặt mã một kiểu. Ví dụ minh họa — không phải mã thật — cùng một nhà cung cấp, kế toán ghi là `NCC-001`, bên vật tư lại ghi là `KH-118`, máy không tự hiểu hai mã đó là một. Cộng thêm Luật Bảo vệ dữ liệu cá nhân có hiệu lực từ 01/01/2026 đòi hỏi phải quản lý dữ liệu tập trung và truy vết được."

**➜ Câu nối sang Slide 3:**
> "Nghe 3 chuyện này, câu hỏi đầu tiên chắc chắn là: vậy mình có phải đập bỏ 6 phần mềm đang chạy để mua phần mềm mới không?" *(Bấm `→`)*

---

### Slide 3 — *“Data Platform thực chất là gì với PTSC Quảng Ngãi?”* ⏱ 1,5 phút
*(Đọc câu hỏi trên slide, dừng 1 giây rồi bấm.)*

- **[Bấm `Space` — Lớp 1 · Định nghĩa 1 câu + Góc nhìn nhân viên]:**
  > "Nói ngắn gọn để Ban Lãnh đạo dễ hình dung: **Data Platform không phải là một phần mềm mới** để thay thế kế toán FAST, MESX hay nhân sự HRM. Nó là **hạ tầng trung gian dùng chung** do Tổng Công ty xây ở phía sau, để gom, làm sạch và chuẩn hóa dữ liệu từ 6 hệ thống rời rạc của mình thành một nguồn sự thật thống nhất. Với anh em nhân viên tác nghiệp, nó gần như **vô hình** — anh em vẫn dùng đúng 6 phần mềm cũ, nhập liệu như cũ, chỉ phải sửa tại nguồn nếu cổng kiểm duyệt báo nhập sai hoặc thiếu."
- **[Bấm `Space` — Lớp 2 · Góc nhìn Giám đốc đơn vị]:**
  > "Còn với Giám đốc và Ban Lãnh đạo đơn vị, cái được trực tiếp nhất là **bỏ cảnh cuối tháng ngồi ghép file Excel 6 mảng**, có số liệu sạch để điều hành. Đổi lại, đơn vị mình cần làm 3 việc: cử đầu mối duyệt dữ liệu đi lên, mở cổng cho 6 phần mềm kết nối, và chia sẻ chi phí vận hành theo gói."
- **[Bấm `Space` — Lớp 3 · 3 cái KHÔNG PHẢI]:**
  > "Em xin chốt thêm **3 cái KHÔNG PHẢI** để mình thống nhất kỳ vọng ngay từ đầu: một là **không thay thế** phần mềm đang chạy ổn; hai là Quảng Ngãi **không tự đi xây** một trung tâm dữ liệu riêng tốn kém mà dùng chung trục của TCT; và ba là nền tảng **không tự làm sạch** được nếu ở dưới vẫn nhập ẩu hoặc TCT chưa ban hành bộ mã chuẩn."

**➜ Câu nối sang Slide 4:**
> "Vậy toàn bộ cái hạ tầng trung gian đó sẽ đặt ở đâu? Đặt hết ở phòng máy nội bộ, đưa hết lên mạng đám mây, hay kết hợp?" *(Bấm `→`)*

---

## 2. CHẶNG 2 — KIẾN TRÚC: ĐẶT Ở ĐÂU, AI GIỮ, CÓ AN TOÀN KHÔNG (≈ 8 phút)

### Slide 4 — *“Đặt Data Platform ở đâu: tại chỗ, lên mây, hay kết hợp?”* ⏱ 1 phút
- **[Bấm `Space` — Lớp 1 · 100% Tại chỗ]:**
  > "Nếu đặt hết tại chỗ: kiểm soát chặt nhưng tiền mua máy chủ rất nặng, nâng cấp chậm và khó dùng các công cụ phân tích AI mới."
- **[Bấm `Space` — Lớp 2 · 100% Lên mây]:**
  > "Nếu đẩy hết lên mây: làm nhanh, nhưng toàn bộ dữ liệu tài chính, lương, hợp đồng gốc của mình phải đưa ra ngoài, vừa ngại bảo mật vừa tốn chi phí lưu trữ."
- **[Bấm `Space` — Lớp 3 · Kết hợp (Hybrid)]:**
  > "Vì vậy Tổng công ty chọn phương án thứ 3 — gọi là **kết hợp (Hybrid)**: dữ liệu gốc và dữ liệu nhạy cảm **giữ lại tại chỗ**, chỉ những số liệu đã lọc sạch và tổng hợp mới **đưa lên mây** để làm báo cáo."

**➜ Câu nối sang Slide 5:** "Cụ thể phần giữ lại tại chỗ và phần đưa lên mây gồm những gì?" *(Bấm `→`)*

---

### Slide 5 — *“Kiến trúc Hybrid giữ gì ở lại, đưa gì lên Cloud?”* ⏱ 1,5 phút
- **[Bấm `Space` — Lớp 1 · Phần giữ lại tại chỗ]:**
  > "Phần giữ tại chỗ được đặt ở tầng 10 Cơ quan Tổng công ty: là cụm máy chủ 8 node, hiện khoảng 40 TB và mở rộng được trên 200 TB. Toàn bộ dữ liệu gốc, nhạy cảm và hệ thống giám sát an ninh nằm ở đây."
- **[Bấm `Space` — Lớp 2 · Phần trên mây]:**
  > "Còn phần trên mây (Microsoft Fabric) chỉ nhận số liệu đã tổng hợp và chuẩn hóa để phục vụ 70 người dùng thường xuyên xem biểu đồ và phân tích."

**➜ Câu nối sang Slide 6:** "Tổng công ty có nhiều đơn vị thành viên — vậy PTSC Quảng Ngãi mình sẽ đứng vào mô hình này theo cách nào?" *(Bấm `→`)*

---

### Slide 6 — *“Thuê phân vùng L3 Tenant trên Hub vận hành ra sao?”* ⏱ 1,5 phút
*(Hiện đầy đủ ngay từ đầu — chú ý dịch ngay chữ Hub–Spoke–Tenant cho sếp dễ hình dung.)*

- **Phía đơn vị → Phòng riêng ở TCT:**
  > "Tổng công ty ví mô hình này giống như trụ sở chính và các chi nhánh. Thay vì mỗi đơn vị tự mua máy chủ riêng, ở mức **L3 (thuê phân vùng riêng)**, 6 phần mềm ở Quảng Ngãi giữ nguyên tại chỗ, chỉ mở cổng đẩy dữ liệu qua trục chung vào **một căn phòng riêng có khóa mang tên PTSC Quảng Ngãi** đặt ngay trên máy chủ của Tổng công ty. Mình không phải mua máy chủ, không phải nuôi đội trực hạ tầng."
- **Vị thế của Quảng Ngãi:**
  > "Theo xếp nhóm, Quảng Ngãi thuộc Nhóm 4 — nhóm đơn vị lớn, có thể ở mức L3 (thuê phòng trên Tổng công ty) hoặc L4 (tự đặt trạm riêng). **Hiện chưa chốt mức nào**, sẽ chốt sau đợt khảo sát Giai đoạn 2A."

**➜ Câu nối sang Slide 7:** "Vậy khi nào thì Quảng Ngãi mới cần tự dựng một trạm máy chủ riêng (gọi là L4 Spoke)?" *(Bấm `→`)*

---

### Slide 7 — *“Khi nào Quảng Ngãi mới cần L4 Spoke riêng?”* ⏱ 1,5 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Trạm riêng tại đơn vị & 4 điều kiện:**
  > "Để tự dựng trạm máy chủ riêng ở đơn vị thì phải tốn tiền đầu tư máy chủ và tự trực vận hành, chỉ nên làm khi thực sự cần. Tài liệu Tổng công ty đặt ra **4 điều kiện bắt buộc**: một, lượng dữ liệu rất lớn; hai, cần phân tích chuyên ngành tại chỗ liên tục; ba, có quy định bắt buộc lưu tại chỗ; và bốn, **đủ đội IT tự vận hành**."
- **Giới hạn cứng:**
  > "Có hai nguyên tắc cố định: **đơn vị không bao giờ tự xây trung tâm lớn**, và kể cả lên L4 thì đơn vị cũng **không tự làm trục kết nối riêng** — mọi kết nối liên thông vẫn phải đi qua trục duy nhất ở Tổng công ty."

**➜ Câu nối sang Slide 8:** "Giờ em xin gom tất cả những mảnh vừa nói thành một bức tranh tổng thể trên một trang để Ban Lãnh đạo dễ hình dung." *(Bấm `→`)*

---

### Slide 8 — *“Toàn bộ 4 lớp kiến trúc kết nối với nhau ra sao?”* ⏱ 2 phút ⭐
*(Hiện đầy đủ ngay từ đầu — vừa nói vừa bấm thẳng các nút luồng trên sơ đồ.)*

- **[Bấm `1 · Đi lên`]:** "Đây là đường đi lên: từ 6 phần mềm của Quảng Ngãi → qua đường truyền bảo mật → vào cửa khẩu chung ở Tổng công ty → qua phòng kiểm duyệt riêng của mình (Landing Zone) → vào kho lõi → rồi mới lên mây để vẽ báo cáo. **Dữ liệu thô không lên mây.**"
- **[Bấm `2 · Đi xuống`]:** "Còn đây là đường đi xuống: báo cáo và bộ mã chuẩn được trả ngược về cho đơn vị dùng."
- **[Bấm `3 · Giám sát`]:** "Mọi hoạt động ở kho lõi đều được ghi sổ nhật ký đẩy về hệ thống giám sát an ninh."
- **[Bấm `4 · Từ chối`]:** "Còn nếu đơn vị mình không duyệt ở phòng đệm, gói dữ liệu bị giữ yên trong **Vùng cách ly**, không vào kho chung, hệ thống chỉ gửi thông báo lỗi về cho người phụ trách để sửa tại phần mềm gốc."

**➜ Câu nối sang Slide 9:** "Nhìn bức tranh lớn như vậy, chắc Ban Lãnh đạo sẽ đặt câu hỏi: hệ thống này bảo vệ an ninh bằng mấy lớp?" *(Bấm `→`)*

---

### Slide 9 — *“Nền tảng đặt ở vùng nào & chặn tấn công ra sao?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Sơ đồ 10 vùng & Bảng 10 vùng:**
  > "Hạ tầng được chia làm 10 lớp hàng rào an ninh, từ cổng internet ngoài cùng tới kho lưu trữ dự phòng. Kho dữ liệu nằm sâu ở Vùng 4, còn trục kết nối chung nằm ở Vùng 5 — giống như trạm kiểm soát hải quan gồm 4 bộ phận chứ không chỉ có một." *(Bấm **Mô phỏng tấn công**)*: "Nếu có truy cập trái phép từ ngoài vào, các lớp tường lửa đầu sẽ chặn ngay và hệ thống giám sát bật báo động."

**➜ Câu nối sang Slide 10:** "Bảo mật với bên ngoài là một chuyện. Còn câu hỏi thẳng thắn nhất trong nội bộ: **dữ liệu của Quảng Ngãi đưa lên đó thì rốt cuộc ai sở hữu, Tổng công ty có xem hết được không?**" *(Bấm `→`)*

---

### Slide 10 — *“Dữ liệu của đơn vị do ai sở hữu & kiểm soát thế nào?”* ⏱ 1,5 phút ⭐
- **[Bấm `Space` — Lớp 1 · Phân quyền & Duyệt]:**
  > "Về kỹ thuật: mỗi đơn vị có phân quyền riêng, mình chỉ thấy số liệu của mình; và dữ liệu bắt buộc phải qua **nút duyệt của đơn vị** mới vào vùng dùng chung."
- **[Bấm `Space` — Lớp 2 · Chia 3 nhóm & Vai trò]:**
  > "Về nội dung: chỉ danh mục dùng chung và số liệu tổng hợp mới đưa lên; chi tiết chuyên ngành giữ tại chỗ. Đơn vị là **chủ sở hữu dữ liệu**, Tổng công ty chỉ là người vận hành nền tảng."
- **[Bấm `Space` — Lớp 3 · Nói thật phần giới hạn]:**
  > "Em xin báo cáo trung thực với Giám đốc điểm này: ở tầng máy chủ sâu nhất, người quản trị hệ thống về mặt lý thuyết vẫn có khả năng kỹ thuật để chạm tới. Vì vậy mình không dựa vào lời hứa suông, mà kiểm soát bằng nguyên tắc: **mọi lần truy cập đều phải có quyền, có mục đích và để lại dấu vết nhật ký không xóa được** gửi về hệ thống giám sát trung tâm."

**➜ Câu nối sang chặng 3 (Slide 11):**
> "Giờ mình đã rõ kiến trúc và quyền sở hữu. Phần tiếp theo em xin mời Ban Lãnh đạo đi theo hành trình thực tế của **một chứng từ**: từ lúc nhân viên bấm Lưu ở phần mềm cũ cho tới khi hiện lên bàn Giám đốc." *(Bấm `→`)*

---

## 3. CHẶNG 3 — HÀNH TRÌNH 5 TRẠM CỦA DỮ LIỆU (≈ 8 phút)

### Slide 11 — *“Một gói dữ liệu đi qua 5 trạm nào rồi quay về nguồn?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu — bấm thẳng nút `▶ Chạy thử 1 gói dữ liệu`.)*

- **[Bấm `▶ Chạy thử 1 gói dữ liệu`]:**
  > "Mời Giám đốc nhìn hạt sáng chạy qua 5 trạm: **1. Lấy từ phần mềm nguồn → 2. Qua cửa khẩu chung → 3. Qua phòng kiểm duyệt của đơn vị → 4. Vào nhà máy chế biến & gộp hồ sơ → 5. Lên báo cáo & hỏi đáp tiếng Việt** — rồi chạy ngược lại trả mã chuẩn về cho phần mềm cũ. Sau đây em xin giải thích từng trạm bằng đúng câu hỏi thực tế."

**➜ Câu nối sang Slide 12:** "Trạm đầu tiên: lấy dữ liệu từ phần mềm kế toán, kho vào giờ cao điểm thì có làm treo máy của nhân viên không?" *(Bấm `→`)*

---

### Slide 12 — *“Lấy dữ liệu có làm chậm phần mềm kế toán, kho không?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Giải thích CDC & Đồng hồ tải:**
  > "Bình thường nếu máy khác vào hỏi trực tiếp thì phần mềm kế toán sẽ bị chậm ngay" *(bấm **Cách cũ**: đồng hồ vọt lên 92%)*. "Nhưng cách mới giống như **đứng cạnh đọc từ cuốn sổ ghi chép phụ** của cơ sở dữ liệu" *(bấm **CDC**: còn 14%)* — "nhân viên nhập liệu vẫn chạy êm mượt, không bị tranh tài nguyên."
- **Lưu ý khảo sát:**
  > "Tuy nhiên, trong 6 phần mềm ở Quảng Ngãi, không phải phần mềm nào cũng đọc sổ phụ được. Cách kết nối từng phần mềm sẽ chốt sau tuần khảo sát."

**➜ Câu nối sang Slide 13:** "Lấy dữ liệu ra rồi thì đi tiếp ra sao? Có sợ rớt mạng làm chứng từ bị ghi trùng 2 lần không?" *(Bấm `→`)*

---

### Slide 13 — *“Nối 6 phần mềm qua 1 trục ESB có hết rối & hết trùng đơn?”* ⏱ 1,5 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **So sánh 1–1 vs 1 Trục:**
  > *(Bấm **So sánh cách cũ (1–1)** rồi tắt đi)*: "Thay vì 6 phần mềm nối chằng chịt với nhau như mạng nhện, tất cả chỉ đi qua **một cửa khẩu duy nhất** ở Vùng 5."
- **Chống trùng & Quy tắc:**
  > *(Bấm **Gửi 1 gói bị lặp mạng**)*: "Mỗi gói đi qua đều được đóng dấu mã số duy nhất. Nếu mạng chập chờn gửi lặp lại một đơn hàng, cửa khẩu tự nhận ra dấu cũ và **gạt bỏ ngay gói trùng** — không bao giờ bị tính doanh thu hay xuất kho hai lần. Lưu ý thêm là E-Office ở đây cũng là một phần mềm nguồn ngang hàng, còn mảng vật tư bảo dưỡng của mình là MESX."

**➜ Câu nối sang Slide 14:** "Câu hỏi quan trọng nhất để bảo vệ uy tín số liệu của đơn vị: nếu dữ liệu nhập sai hoặc còn lọt thông tin nhạy cảm thì sao?" *(Bấm `→`)*

---

### Slide 14 — *“Dữ liệu sai hoặc nhạy cảm lọt lên kho chung thì sao?”* ⏱ 2 phút ⭐
*(Hiện đầy đủ ngay từ đầu.)*

- **Sơ đồ lọc & Nguyên tắc kiểm soát:**
  > "Trước khi vào kho dùng chung, 100% gói dữ liệu đi vào **phòng đệm riêng của Quảng Ngãi** và qua bộ kiểm tra tự động: bắt lỗi thiếu mã số thuế, trùng mã, hoặc che thông tin cá nhân nhạy cảm."
  > *(Bấm **Thả gói lỗi**)*: "Gói bị lỗi hoặc do đơn vị **bấm Từ chối** sẽ **nằm yên ở Vùng cách ly**, tuyệt đối không vào kho chung và cũng không ghi đè ngược phần mềm nguồn. Hệ thống chỉ mở phiếu báo lỗi gửi cho người điều phối và người nhập liệu của phần mềm đó để **sửa tận gốc tại phần mềm nguồn rồi nộp lại bản mới**."
- **Quyền bấm nút của đơn vị:**
  > *(Thử bấm nút **APPROVE / REJECT**)*: "Chỉ khi người phụ trách của đơn vị **bấm Approve (Duyệt)** thì gói sạch mới đi tiếp. Em nhấn mạnh hai trạng thái khác nhau: *chưa duyệt* là đang chờ, còn *không duyệt* là từ chối đưa vào cách ly."

**➜ Câu nối sang Slide 15:** "Gói sạch được duyệt rồi thì bên trong kho chế biến thế nào, và nếu tháng sau phát hiện hồi xưa sửa nhầm thì có lật lại được số cũ không?" *(Bấm `→`)*

---

### Slide 15 — *“Làm sạch thế nào & sửa nhầm có quay lại bản cũ được?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **3 phễu lọc & Quay ngược thời gian:**
  > *(Bấm **Chạy lọc qua 3 phễu**)*: "Dữ liệu đi qua 3 lớp tinh chế: từ thô → sạch → tổng hợp, giống lọc quặng thành vàng."
  > *(Kéo thanh trượt Time-Travel)*: "Mỗi lần có điều chỉnh, hệ thống đều **chụp giữ lại nguyên trạng bản cũ**, nên sếp cần đối chiếu lại số tồn kho của đúng ngày đầu kỳ tháng trước vẫn lôi ra xem được nguyên vẹn. Các con số hiển thị trên bảng này là **số liệu minh họa** để giải thích cách hệ thống lưu vết."

**➜ Câu nối sang Slide 16:** "Còn nỗi đau thứ ba lúc đầu — cùng một nhà cung cấp mà kế toán ghi `NCC-001`, kho ghi `KH-118` — nền tảng gộp kiểu gì?" *(Bấm `→`)*

---

### Slide 16 — *“Cùng 1 đối tác ở FAST và MESX lệch mã thì gộp kiểu gì?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Gộp 3 → 1 & 10 chức năng:**
  > *(Bấm nút **Bật/Tắt Gộp 3 → 1**)*: "Hệ thống tự đối chiếu tên, mã số thuế, địa chỉ rồi **gộp thành 1 hồ sơ chuẩn duy nhất** (ví dụ minh họa: `NCC-001` và `KH-118` quy về một mối). Hai thẻ trùng không bị xóa mất dấu vết mà chỉ **ẩn có kiểm soát**, vẫn giữ cầu nối với mã cũ. Bộ quản trị danh mục chuẩn này có sẵn 10 chức năng từ kiểm trùng, lưu phiên bản tới phân quyền duyệt."

**➜ Câu nối sang Slide 17:** "Nhưng khi gộp lại rồi thì dùng bộ mã của Quảng Ngãi, của Tổng công ty, hay chuẩn quốc tế?" *(Bấm `→`)*

---

### Slide 17 — *“Mã đơn vị, mã TCT/PVN và mã kỹ thuật khớp nhau ra sao?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Dữ liệu chủ 3 tầng:**
  > "Có hai cách làm riêng biệt. Với 9 nhóm dữ liệu quản trị chung (đơn vị, nhà cung cấp, vật tư, nhân sự…), mình giữ nguyên mã đang dùng ở Quảng Ngãi, rồi dùng bảng đối chiếu 3 cột: **Mã đơn vị → Chuẩn Tổng công ty → Chuẩn PVN**. Hiện 2 cột chuẩn kia Tổng công ty chưa ban hành nên để trống chờ, đơn vị không tự bịa."
- **Mã kỹ thuật:**
  > *(Bấm **Lật thẻ**)*: "Còn riêng dữ liệu kỹ thuật chuyên ngành thì giữ nguyên mã nội bộ (ví dụ `P3.ME`) và gắn thêm một mã đối chiếu chuẩn quốc tế (`NORSOK:ME`) chạy song song."

**➜ Câu nối sang Slide 18:** "Đi hết 5 trạm rồi — vậy cuối cùng **trên bàn của Giám đốc sẽ có gì?**" *(Bấm `→`)*

---

### Slide 18 — *“Sau tất cả, Giám đốc nhận được gì trên bàn?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Báo cáo, Hỏi tiếng Việt & Lưu ý hàng mẫu:**
  > *(Bấm **Gõ hỏi tiếng Việt**)*: "Giai đoạn 1 dự kiến có **20 báo cáo quản trị tự động**, và sếp có thể **gõ câu hỏi bằng tiếng Việt** để hệ thống tự vẽ biểu đồ ngay, kèm danh mục tra xem con số đó lấy từ chứng từ nào ra. Em xin lưu ý rõ: 5 bảng tổng hợp đang chiếu ở cột bên phải hiện chỉ là **bảng chạy thử (demo) trên dữ liệu mẫu** để kiểm tra năng lực hệ thống, chưa phải số liệu thật của Quảng Ngãi."

**➜ Câu nối sang chặng cuối (Slide 19):**
> "Vậy là xong phần nền tảng chạy thế nào. Giờ đến phần thực tế nhất cho Ban Lãnh đạo: **PTSC Quảng Ngãi mình phải làm gì, tốn bao nhiêu, và hôm nay cần quyết việc gì?**" *(Bấm `→`)*

---

## 4. CHẶNG 4 — ĐƠN VỊ LÀM GÌ, TỐN GÌ, QUYẾT GÌ (≈ 6 phút)

### Slide 19 — *“PTSC Quảng Ngãi phải làm 4 việc gì (không cần tự code)?”* ⏱ 1 phút
- **[Bấm `Space` lần lượt 1 → 2 → 3 → 4]:**
  > "Đơn vị mình **không phải tự lập trình**, chỉ cần làm 4 việc:
  > 1. **Cử người** phụ trách dữ liệu ở 2 cấp (không cử tràn lan).
  > 2. **Mở cổng** 6 phần mềm để nền tảng kết nối lấy dữ liệu.
  > 3. **Kiểm và bấm duyệt** dữ liệu của mình tại phòng đệm trước khi đưa lên kho chung.
  > 4. **Chịu phần chi phí** của đơn vị theo cơ chế chia sẻ chung."

**➜ Câu nối sang Slide 20:** "Cụ thể việc thứ nhất — cử người — thì mình phải cử ai và bao nhiêu người?" *(Bấm `→`)*

---

### Slide 20 — *“Trong 5 cấp quản trị TCT, đơn vị chỉ cần cử ai?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Bức tranh 5 cấp & 2 cấp của Quảng Ngãi:**
  > "Tổng công ty đặt ra 5 cấp quản trị dữ liệu. Cấp 1, 2 và cấp kỹ thuật vận hành nền tảng (Cấp 5) là của Tổng công ty. Quảng Ngãi mình **chỉ nắm đúng 2 cấp**: **Cấp 3** là Lãnh đạo đơn vị — chịu trách nhiệm cao nhất và bấm duyệt chia sẻ dữ liệu; **Cấp 4** là các đầu mối chuyên môn phối hợp làm sạch và kiểm tra chất lượng (tối đa theo 9 nhóm dữ liệu)."

**➜ Câu nối sang Slide 21:** "Thứ Hai 30/11 đoàn khảo sát Tổng công ty sẽ về. Vậy đơn vị mình đã chuẩn bị gì và cần hỏi lại đoàn điều gì?" *(Bấm `→`)*

---

### Slide 21 — *“Đón đoàn 30/11: đã chuẩn bị gì & hỏi ngay TCT câu nào?”* ⏱ 1,5 phút ⭐
- **[Bấm `Space` — Lớp 1 · Đã chuẩn bị]:**
  > "Về phần mình, bộ hồ sơ khảo sát 8 phần / 73 việc đã chuẩn bị sẵn; mỗi phần mềm trong 6 phần mềm bố trí đủ 3 đầu mối (người dùng chính, IT và kỹ thuật) — và cần rà cả những phần mềm cũ đang ngưng nếu còn dữ liệu."
- **[Bấm `Space` — Lớp 2 · Câu hỏi em sẽ hỏi thẳng đoàn TCT]:**
  > "Ngược lại, em đề xuất mình hỏi thẳng đoàn Tổng công ty hai nhóm câu hỏi ngay tuần sau:
  > - **Thứ nhất, tiến độ thật Giai đoạn 1:** Hợp đồng ghi 27/08/2026 đưa vào sử dụng, nay đã quá khoảng 3 tháng nhưng đơn vị chưa nhận được xác nhận tiến độ thực tế.
  > - **Thứ hai, 3 điểm vận hành ở phòng đệm duyệt dữ liệu:** duyệt theo lô hay từng dòng; có vài dòng lỗi thì chặn cả lô hay chỉ giữ riêng dòng lỗi; và thời gian chờ duyệt tối đa là bao lâu."

**➜ Câu nối sang Slide 22:** "Câu hỏi tiếp theo chắc chắn Ban Lãnh đạo quan tâm nhất: chọn phương án nào thì Quảng Ngãi phải trả những khoản tiền nào?" *(Bấm `→`)*

---

### Slide 22 — *“Chọn L3 hay L4 thì đơn vị phải trả những khoản nào?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu — biểu đồ cột tự chạy khi mở slide.)*

- **Bảng trách nhiệm & So sánh L3 vs L4:**
  > "Nếu ở mức **L3 (thuê phân vùng trên Tổng công ty)**: đơn vị **không mất tiền đầu tư máy chủ riêng**, nhưng **vẫn phải trả** tiền bản quyền hàng năm (10 mục), tiền triển khai, tiền kết nối 6 phần mềm của mình và phí vận hành phân bổ."
  > *(Bấm chuyển giữa **L3** và **L4**)*: "Còn nếu lên L4 (làm trạm riêng tại Quảng Ngãi) thì đơn vị gánh thêm toàn bộ tiền mua máy chủ và tự nuôi bộ máy vận hành."

**➜ Câu nối sang Slide 23:** "Vậy khoản nào Tổng công ty bỏ vốn, khoản nào đơn vị mình trả?" *(Bấm `→`)*

---

### Slide 23 — *“Phương án 3 phân chia vốn giữa TCT và đơn vị ra sao?”* ⏱ 1 phút
*(Hiện đầy đủ ngay từ đầu.)*

- **Phần TCT vs Phần Đơn vị & Điểm chưa chốt:**
  > "Theo Phương án 3 được đề xuất: Tổng công ty lo đầu tư trung tâm, nền tảng dùng chung và bản quyền khung — nếu đơn vị nào chưa có nguồn tiền ngay thì Tổng công ty **đầu tư trước và ghi nợ**. Đơn vị lo phần kết nối nội bộ, máy chủ riêng (nếu chọn L4) và phí vận hành phân bổ theo mức dùng. **Tỷ lệ chia tiền cụ thể sẽ xây dựng ở Giai đoạn 2A, hiện chưa có tỷ lệ.**"

**➜ Câu nối sang Slide 24:** "Dù chưa có con số chốt từ Tổng công ty, em xin gửi Giám đốc một khung ước tính thị trường để dễ hình dung quy mô." *(Bấm `→`)*

---

### Slide 24 — *“Ước tính chi phí 5 năm giữa L3 và L4 chênh bao nhiêu?”* ⏱ 1 phút ⭐
*(Hiện đầy đủ ngay từ đầu — đọc ngay cảnh báo trước khi nói số.)*

> "Em xin nhấn mạnh: đây là **con số ước tính tham khảo theo thị trường, không phải báo giá chính thức của PTSC**. Con số chính thức chỉ có sau khi khảo sát."
- **So sánh 5 năm:**
  > "Ước tính trong 5 năm: nếu thuê phân vùng **L3** tốn khoảng **16,8 tỷ** (năm đầu ~10 tỷ, vận hành ~0,6 tỷ/năm). Còn nếu tự dựng trạm **L4** tốn khoảng **40,4 tỷ** (năm đầu ~22 tỷ, vận hành ~2,4 tỷ/năm) — chênh hơn **23 tỷ**. Đáng chú ý là phần **kết nối 6 phần mềm (~7,1 tỷ) thì phương án nào cũng tốn ngang nhau**."

**➜ Câu nối sang Slide 25:** "Về mặt thời gian, mọi thứ hiện tại đã chắc chắn tới đâu?" *(Bấm `→`)*

---

### Slide 25 — *“Lộ trình thực tế: đâu là mốc đã ký, dự thảo & điểm chưa chốt?”* ⏱ 1,5 phút
- **[Bấm `Space` — Lớp 1 · Đã diễn ra]:**
  > "Thứ nhất, phần đã diễn ra theo hợp đồng Giai đoạn 1: khởi động 04/03/2026, theo hợp đồng đưa vào dùng 27/08/2026 — tiến độ thật thế nào tuần sau em sẽ hỏi đoàn."
- **[Bấm `Space` — Lớp 2 · Dự kiến (chưa duyệt)]:**
  > "Thứ hai, phần dự kiến theo bản nháp ngày 29/10: tháng 12/2026 đăng ký nhóm triển khai, tháng 03/2027 xong trục kết nối tại Tổng công ty, năm 2027 triển khai các đơn vị — nhưng bản này **chưa được phê duyệt**."
- **[Bấm `Space` — Lớp 3 · Điểm chưa thống nhất]:**
  > "Thứ ba, giữa các tài liệu của Tổng công ty vẫn đang lệch nhau về mốc Giai đoạn 2 (2026–2027 hay từ 2028) và chưa chốt ngày khảo sát Giai đoạn 2A. Em báo thẳng để Giám đốc nắm đủ thông tin."

**➜ Câu nối sang slide cuối (Slide 26):**
> "Từ toàn bộ nội dung trên, hôm nay em xin phép trình Giám đốc thông qua 4 quyết định cụ thể trước khi đoàn Tổng công ty về vào thứ Hai." *(Bấm `→`)*

---

## 5. CHỐT 4 QUYẾT ĐỊNH (≈ 3 phút)

### Slide 26 — *“Hôm nay xin Giám đốc chốt 4 quyết định nào?”* ⏱ 3 phút ⭐
*(Bấm `Space` mở **từng dòng một** — đọc xong dòng nào thì dừng 2–3 giây chờ Giám đốc gật đầu/cho ý kiến rồi mới bấm sang dòng tiếp theo!)*

- **[Bấm `Space` — Lớp 1 · Quyết định 1]:**
  > "**Quyết định 1:** Ký giao đầu mối dự án Data Platform của PTSC Quảng Ngãi — hạn trước 30/11 để thứ Hai có người đại diện làm việc chính thức với đoàn Tổng công ty."
- **[Bấm `Space` — Lớp 2 · Quyết định 2]:**
  > "**Quyết định 2:** Chỉ định Lãnh đạo làm Data Owner (người chịu trách nhiệm và duyệt dữ liệu) cùng các đầu mối phòng ban phụ trách chất lượng theo 9 nhóm dữ liệu — hạn trước 30/11."
- **[Bấm `Space` — Lớp 3 · Quyết định 3]:**
  > "**Quyết định 3:** Cho phép gửi văn bản 4 câu hỏi lên Tổng công ty ngay trong tuần: (1) Quảng Ngãi có nằm trong danh sách SAP S/4HANA không; (2) Kênh, mẫu và hạn đăng ký tháng 12; (3) Lịch khảo sát GĐ2A & đơn vị cần chuẩn bị gì; (4) Bản kế hoạch 29/10 đã duyệt chưa."
- **[Bấm `Space` — Lớp 4 · Quyết định 4 + Cảm ơn]:**
  > "**Quyết định 4:** Giao Phòng CNTT và đầu mối chuẩn bị sẵn hồ sơ đăng ký triển khai vào tháng 12/2026. Em xin trân trọng cảm ơn Giám đốc và Ban Lãnh đạo, và xin ý kiến chỉ đạo của Giám đốc ạ."

---

## 6. BỎ TÚI TRẢ LỜI NHANH KHI LÃNH ĐẠO HỎI VẶN

| Câu Giám đốc dễ hỏi | Cách em trả lời gọn, đúng mực |
|---|---|
| *"Tức là Tổng công ty lấy hết dữ liệu của mình à?"* | Dạ không ạ: số liệu nghiệp vụ chi tiết giữ tại chỗ, mình chỉ đưa danh mục dùng chung và số tổng hợp lên, và **mình tự bấm duyệt** ở phòng đệm trước. Tuy nhiên về kỹ thuật sâu nhất ở máy chủ thì mình kiểm soát bằng phân quyền, mục đích và nhật ký không xóa được chứ không hứa cách ly tuyệt đối. |
| *"Có phải thay 6 phần mềm đang chạy không?"* | Dạ không ạ, giữ nguyên 100%, anh em làm việc bình thường trên phần mềm cũ. |
| *"Quảng Ngãi mình là L3 hay L4?"* | Dạ mình nằm trong Nhóm 4 (có thể L3 hoặc L4), **chưa chốt** — Tổng công ty sẽ khảo sát rồi mới chốt ạ. |
| *"Cuối cùng đơn vị tốn bao nhiêu tiền?"* | Dạ hiện chưa có số chốt và chưa có tỷ lệ phân bổ (chờ Giai đoạn 2A). Con số ~16,8 tỷ (L3) hay ~40,4 tỷ (L4) cho 5 năm chỉ là ước tính thị trường để Ban Lãnh đạo tham khảo quy mô thôi ạ. |
| *"Nếu dữ liệu có lỗi hoặc mình không đồng ý cho lên thì sao?"* | Dạ khi em hoặc lãnh đạo bấm Từ chối ở phòng đệm, gói đó bị giữ yên ở Vùng cách ly, không lên kho chung và không sửa ngược phần mềm gốc; hệ thống chỉ báo về cho người nhập liệu sửa lại cho đúng rồi nộp lại. |
| *"Câu nào em chưa biết / chưa có trong tài liệu"* | "Dạ phần này tài liệu hiện tại chưa chốt rõ, em xin ghi nhận để hỏi thẳng đoàn khảo sát Tổng công ty ngày 30/11 rồi báo cáo lại Giám đốc ngay ạ." *(Tuyệt đối không đoán.)* |

---

## 7. CHECKLIST 5 PHÚT TRƯỚC GIỜ HỌP
- [ ] Điền ngày họp vào Slide 01 trong file HTML.
- [ ] Mở file trên máy chiếu ở chế độ toàn màn hình (`F11`), kiểm tra Slide 02 đang ở trạng thái **mờ nội dung bên dưới** khi mới mở trang.
- [ ] Bấm thử các nút ở **Slide 08 (Bức tranh tổng)** và **Slide 22 (L3/L4)** để chắc chắn không lỗi trình duyệt.
- [ ] In sẵn 1 tờ **Slide 21 (Câu hỏi hỏi đoàn TCT)** và **Slide 26 (4 Quyết định)** để Giám đốc xem/bút phê trực tiếp.
- [ ] Nếu phòng họp chỉ cho nói **15 phút**: bỏ lướt các slide `4, 6, 7, 9, 12, 15, 16, 17, 23`; giữ trọng tâm **`2, 3, 5, 8, 10, 14, 19, 21, 22, 24, 26`**.
