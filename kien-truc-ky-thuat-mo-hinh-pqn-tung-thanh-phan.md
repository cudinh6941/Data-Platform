# KIẾN TRÚC KỸ THUẬT MÔ HÌNH PQN — TỪNG THÀNH PHẦN ĐẢM NHIỆM GÌ

*Bản deep-dive kỹ thuật cho Phần 2 bài trình bày team I&T tuần sau (30/11–04/12).
Dùng kèm dàn ý `dan-y-thuyet-trinh-team-it-data-platform.md` (Phần 2, các mục
P2-1 → P2-10). Soạn 27/11/2026.*

## 0. Cách đọc file này — quy ước nguồn

- **"Tài liệu nói"** = có trong tài liệu, ghi rõ nguồn (Báo cáo đề xuất kỹ thuật
  = TCT-DP_Bao_cao_de_xuat_ky_thuat_Final, 82 trang; phiên chiều = slide hội
  thảo 10/08/2026, 63 slide, số slide in; phiên sáng = slide hội thảo
  10/08/2026, 48 slide; phụ lục YCKT = Phụ lục 02 hợp đồng -2026/PTSC-QN/MHH).
- **"Suy ra / đề xuất của em"** = KHÔNG có trong tài liệu, là cách đọc kỹ thuật
  từ kiến trúc Hub áp xuống mô hình đơn vị. Ghi rõ từng chỗ — khi trình bày
  với team phải nói "đây là cách mình hiểu, chờ đoàn khảo sát xác nhận", đừng
  nói như đã chốt.
- Mô hình mặc định: **L3 Tenant trên Hub**. L4 Spoke chỉ khi đủ 4 tiêu chí
  (phiên chiều slide in 50). Mọi chỗ viết "Spoke" đều là phương án có điều kiện.

---

## 1. Bức tranh tổng — mô hình PQN gồm 3 tầng

```
TẦNG 1 — TẠI ĐƠN VỊ (Quảng Ngãi)
  6 hệ thống nguồn: Cảng · ERP FAST · MESX · Bán hàng · E-Office · HRM
  + Agent thu thập / API kết nối từng hệ  →  đẩy lên Hub qua đường truyền

TẦNG 2 — TENANT QUẢNG NGÃI TRÊN HUB (phân vùng riêng, L3)
  Vùng lưu trữ riêng · Pipeline riêng · Workspace BI riêng
  Cách ly bằng RBAC / ABAC theo tenant — đơn vị chỉ thấy dữ liệu của mình

TẦNG 3 — DÙNG CHUNG TẠI HUB TCT (trung tâm)
  Trục tích hợp Vùng 5 (ESB + API Gateway + Kafka + CDC/ETL) · MDM Golden Record
  Lakehouse trung tâm · SIEM tập trung · SSO tập trung · Microsoft Fabric / Power BI
```

Ba nguyên tắc xuyên suốt cả bài (nhắc ở đầu, giữa, cuối):

1. **Dữ liệu gốc không bao giờ lên Cloud** — chỉ dữ liệu đã làm sạch, chuẩn
   hóa, tổng hợp mới lên OneLake/Fabric; dữ liệu gốc ở lại on-prem tại Việt
   Nam. (Báo cáo kỹ thuật §3.2–3.4; phiên chiều.)
2. **Trục ESB duy nhất ở Hub TCT** — đơn vị không bao giờ tự xây Hub, Spoke
   cũng không có ESB riêng. Cái bắt buộc là cả Vùng 5 (trục chung), không
   phải chỉ ESB. (Phụ lục YCKT §1–§2; phiên sáng trang in 25.)
3. **Đơn vị là Data Owner** — dữ liệu vào vùng dùng chung chỉ sau khi đơn vị
   duyệt ở Landing Zone. (Phiên chiều; Báo cáo kỹ thuật §4.2.7.)

---

## 2. Từng thành phần — đảm nhiệm cái gì

*12 phân hệ theo Báo cáo kỹ thuật Chương 3 §3.2 (tr. 16–18/83), cộng hạ tầng
cụm Hub §2.2. Mỗi phân hệ ghi 4 ý: công cụ đề xuất trong tài liệu, chạy ở
đâu, đảm nhiệm gì cho Quảng Ngãi, team Quảng Ngãi phải làm gì với nó.*

### Nhóm A — Thu thập & tích hợp (dữ liệu đi VÀO)

#### A1. Phân hệ thu thập dữ liệu (Ingestion) — Phân hệ 1

- **Tài liệu nói:** thu thập từ nhiều nguồn (file, API, cơ sở dữ liệu, IoT…),
  chuẩn hóa đầu vào rồi đưa vào lưu trữ trung tâm. Chạy cả on-prem lẫn Cloud.
- **Công cụ đề xuất:** một trong các công cụ sau (có thể kết hợp): **Airbyte /
  IBM StreamSets / Apache NiFi** — 400+ connector. CDC (bắt thay đổi theo thời
  gian thực): **Debezium / IBM Data Replication / Maxwell / Kafka Connector
  (MySQL)**. (Báo cáo kỹ thuật §4.1.)
- **Chạy ở đâu:** Ingestion on-prem nằm trên Node 5 của cụm Hub (Query +
  Metadata + Ingestion). Phía đơn vị chỉ có **agent thu thập** đặt tại chỗ
  (phiên chiều: tenant "chỉ cần agent thu thập hoặc kéo trực tiếp qua API").
- **Đảm nhiệm gì cho Quảng Ngãi:** đây là "cái phễu" đầu tiên — mọi dữ liệu
  từ 6 hệ đều phải qua Ingestion trước khi vào Lakehouse. Nó quyết định dữ
  liệu lấy theo lô (batch, vd: file Excel/CSV xuất định kỳ) hay theo dòng
  (stream/CDC, vd: thay đổi trong DB vừa phát sinh đã đẩy lên).
- **Team Quảng Ngãi làm gì:** với từng hệ, xác định phương thức lấy dữ liệu
  (xem §4) — DB gì, có API không, xuất file được không, vendor có hợp tác
  không. Đây là thông tin phải có TRƯỚC khi đoàn khảo sát tới (phiếu phỏng
  vấn từng hệ đã có sẵn câu hỏi này).

#### A2. Trục tích hợp ESB — Phân hệ 3 (CHỈ on-prem)

- **Tài liệu nói:** nền tảng trung gian kết nối, truyền dữ liệu giữa các hệ
  thống khác nhau, đảm bảo tích hợp nhanh, ổn định, linh hoạt. **Không sử
  dụng trên Cloud.** (Báo cáo kỹ thuật §3.2.)
- **Công cụ đề xuất:** một trong các công cụ sau (có thể kết hợp): **Apache
  Camel, WSO2 Enterprise Integrator, IBM App Connect Enterprise**. (Báo cáo
  kỹ thuật §4.3.3.)
- **Chạy ở đâu:** on-prem tại Hub, trong Vùng 5. Không có bản sao tại đơn vị.
- **Đảm nhiệm gì cho Quảng Ngãi:** ESB là "tổng đài" cho luồng giao dịch
  request–response: dịch giao thức/định dạng, định tuyến, đồng bộ 2 chiều.
  Ví dụ: mã chuẩn từ MDM trả về FAST đi qua ESB; yêu cầu tra cứu dữ liệu
  dùng chung đi qua ESB. Phụ lục YCKT bắt buộc: tích hợp qua **MỘT trục ESB
  dùng chung**; ngoại lệ SaaS chỉ khi có văn bản chấp thuận của PTSC.
- **Điểm team hay hiểu sai (nhắc 2 lần trong bài):** ESB KHÔNG chứa API
  Gateway, Kafka hay CDC/ETL. Cả 4 là anh em trong Vùng 5, cùng hội tụ về
  Landing Zone. Cái bắt buộc là cả Vùng 5, không phải mọi luồng đều qua ESB.

#### A3. API Gateway — thành phần trong Vùng 5

- **Tài liệu nói:** Vùng 5 gồm API Gateway, ESB/WSO2, Kafka, Airbyte/CDC,
  ETL/ELT, Data Validation & Quality. (Phiên sáng trang in 25.)
- **Đảm nhiệm gì cho Quảng Ngãi:** kiểm soát truy cập API — ai được gọi API
  nào, giới hạn ra sao, ghi nhật ký ra sao. Mọi API của nền tảng (vd: 50 API
  chuẩn GĐ1) đều đi qua đây. Khi hệ của đơn vị "kéo trực tiếp qua API" lên
  Hub thì chính là gọi qua API Gateway.
- **Team Quảng Ngãi làm gì:** khi tích hợp hệ mới, đăng ký API qua Gateway
  thay vì mở cổng trực tiếp vào DB Hub. (Suy ra từ kiến trúc Vùng 5 — tài
  liệu không viết quy trình đăng ký cụ thể.)

#### A4. Kafka — luồng sự kiện (Event Streaming), trong Vùng 5

- **Tài liệu nói:** Kafka nằm trong Vùng 5; đồng bộ luồng sự kiện; log hệ
  thống có thể forward qua Kafka tới SIEM. (Phiên sáng; Báo cáo kỹ thuật
  §4.11.)
- **Đảm nhiệm gì cho Quảng Ngãi:** chở các **sự kiện** — vd: vừa tạo 1 nhà
  cung cấp mới trong FAST → sự kiện đẩy lên ngay, không chờ chạy batch đêm.
  Đây là 1 trong 2 nhịp của nền tảng (nhịp theo sự kiện + nhịp quét định kỳ).
- **Phân biệt với ESB cho team:** ESB = hỏi–đáp có trả lời ngay (vd: tra cứu
  mã chuẩn); Kafka = thông báo sự kiện 1 chiều, ai đăng ký thì nhận (vd: có
  dữ liệu mới). Hai thứ khác nhau, không thay nhau được.

#### A5. CDC / ETL / ELT — đồng bộ khối lượng lớn từ DB, trong Vùng 5

- **Tài liệu nói:** CDC bắt thay đổi trong DB nguồn theo thời gian thực
  (Debezium / Maxwell / Kafka Connector); ETL/ELT xử lý, làm sạch, chuẩn
  hóa, chuyển đổi dữ liệu phục vụ báo cáo, phân tích, AI. (Báo cáo kỹ thuật
  §4.1, §4.7.)
- **Đảm nhiệm gì cho Quảng Ngãi:** chở dữ liệu **khối lượng lớn** — vd: đồng
  bộ toàn bộ danh mục vật tư FAST↔MESX, hoặc chạy batch đêm nạp dữ liệu ngày
  vào Lakehouse. CDC là cách "không làm chậm phần mềm cũ": đọc nhật ký thay
  đổi của DB thay vì quét toàn bộ bảng.
- **Phụ lục YCKT bắt buộc (§2):** CDC/tăng dần (incremental) + backfill/
  replay (nạp bù / chạy lại); khóa chính ổn định + ánh xạ ID MDM; idempotency
  + correlationId + upsert + retry (gửi trùng không nhân đôi, có mã theo dõi,
  gửi lại được).

### Nhóm B — Lưu trữ & xử lý (dữ liệu ở ĐÂU và BIẾN ĐỔI thế nào)

#### B1. Phân hệ lưu trữ dữ liệu — Lakehouse (Data lakehouse) — Phân hệ 2

- **Tài liệu nói:** kết hợp ưu điểm data warehouse + data lake, lưu cả dữ
  liệu có cấu trúc và phi cấu trúc, phục vụ BI và AI trên một nền tảng duy
  nhất. Chạy cả on-prem lẫn Cloud. (Báo cáo kỹ thuật §3.2.)
- **Công cụ đề xuất:** **MinIO** (lưu trữ tương thích S3) + định dạng phân
  tích **Parquet + Apache Iceberg** (table format); hỗ trợ ORC, Avro; tích
  hợp tốt Spark, Trino, Kafka, Airbyte, OpenMetadata. (Báo cáo kỹ thuật §4.2.)
- **Chạy ở đâu:** on-prem trên Node 1–2 (Storage Node: 16 vCPU, 128 GB RAM,
  20 TB HDD + 1 TB SSD mỗi node); Cloud là OneLake 20 TB (chỉ nhận dữ liệu
  đã chuẩn hóa/tổng hợp).
- **3 tầng dữ liệu trong Lakehouse — nói bằng tiếng Việt thường cho team:**
  - **RAW (thô):** dữ liệu vừa lấy về, giữ nguyên như ở hệ nguồn. Lưu **3
    bản**: 1 bản chính tại Data Center, 1 bản tại DR (site dự phòng), 1 bản
    tại on-prem Data Platform. (Báo cáo kỹ thuật §2.2.3.)
  - **SILVER (đã làm sạch):** qua kiểm lỗi + làm sạch + chuẩn hóa. Đây là
    tầng Landing Zone "duyệt" xong mới được vào.
  - **GOLD (sản phẩm dữ liệu):** đã tổng hợp, gắn mã chuẩn, sẵn sàng cho báo
    cáo/AI. Lưu **2 bản**, bản chính tại on-prem Data Platform.
- **Đảm nhiệm gì cho Quảng Ngãi:** tenant Quảng Ngãi là **1 phân vùng riêng
  trong Lakehouse Hub** — dữ liệu chuyên ngành của đơn vị nằm trong phân vùng
  đó, cách ly bằng RBAC/ABAC, đơn vị khác không thấy.
- **Team Quảng Ngãi làm gì:** đo khối lượng dữ liệu từng hệ (tổng hiện tại +
  tốc độ tăng/năm) — vì dung lượng tenant + đường truyền phụ thuộc trực tiếp
  vào con số này, mà hiện tại **chưa đo** (câu hỏi cho đoàn khảo sát + việc
  CNTT đang được nhờ làm).

#### B2. Phân hệ biến đổi / xử lý dữ liệu (Transform) — Phân hệ 7

- **Tài liệu nói:** xử lý, làm sạch, chuẩn hóa, chuyển đổi dữ liệu (ETL/ELT)
  phục vụ báo cáo, phân tích, đào tạo mô hình AI. Chạy cả on-prem lẫn Cloud.
  (Báo cáo kỹ thuật §3.2.)
- **Công cụ đề xuất:** **Apache Spark, Apache Flink, Hadoop MapReduce,
  Airflow, Presto/Trino** (hoặc tương đương). (Báo cáo kỹ thuật §4.7.3.)
- **Chạy ở đâu:** on-prem trên Node 3–4 (Processing: 32 vCPU, 128 GB RAM,
  2 TB SSD mỗi node); Flink/Trino cũng nằm trong Vùng 4 (Internal/Server
  Farm) cùng Superset, K8s, AI-GPU.
- **Đảm nhiệm gì cho Quảng Ngãi:** đây là "dây chuyền làm sạch" — biến RAW
  thành SILVER rồi GOLD: kiểm lỗi theo 8 tiêu chí chất lượng, chuẩn hóa định
  dạng, gộp trùng, gắn mã chuẩn. Hai nhịp: chạy theo sự kiện (Flink/stream)
  và chạy theo lô định kỳ (Spark/Airflow/batch).
- **Team Quảng Ngãi làm gì:** định nghĩa **quy tắc kiểm lỗi (DQ rules)** cho
  dữ liệu của mình — vd: mã vật tư thiếu mã số thuế thì lỗi loại gì, ai xử
  lý. Phụ lục YCKT bắt buộc: DQ rules + danh sách lỗi + dữ liệu bị cách ly
  (quarantine).

#### B3. Workflow / Airflow — điều phối chạy batch (nằm trong Phân hệ 7 + Node 8)

- **Tài liệu nói:** Node 8 cụm Hub = **Workflow automation + MDM** (32 vCPU,
  128 GB RAM, 1 TB SSD). Airflow nằm trong danh sách công cụ Transform.
  (Báo cáo kỹ thuật §2.2.2, §4.7.3.)
- **Đảm nhiệm gì cho Quảng Ngãi:** đặt lịch + giám sát các job chạy định kỳ:
  batch đêm nạp dữ liệu, quét đối sánh mã định kỳ, làm mới GOLD, chạy lại
  (replay) khi lỗi. Nếu job lỗi giữa chừng thì Airflow là nơi đầu tiên team
  vận hành nhìn vào.

### Nhóm C — Dữ liệu chủ (cái làm cho dữ liệu KHỚP NHAU)

#### C1. Phân hệ quản lý dữ liệu chủ — MDM — Phân hệ 4

- **Tài liệu nói:** xây dựng và duy trì bộ mã dữ liệu dùng chung toàn hệ
  thống, đảm bảo nhất quán, toàn vẹn, đồng bộ giữa các hệ thống. **Đầy đủ
  10 chức năng trên on-prem; trên Cloud chỉ có chức năng 9** (Công bố và
  chia sẻ dữ liệu chủ). (Báo cáo kỹ thuật §3.2, §4.2.)
- **10 chức năng (Báo cáo kỹ thuật §4.2):**
  1. Mô hình hóa dữ liệu (Data Modeling) — vẽ ERD, định nghĩa thực thể.
  2. Tích hợp dữ liệu (Data Integration) — nhận dữ liệu chủ từ các hệ.
  3. Làm sạch và chuẩn hóa (Cleansing & Standardization).
  4. So khớp và gộp dữ liệu (Matching & Merging) — fuzzy theo mã số thuế,
     tên, địa chỉ.
  5. Quản trị và giám sát dữ liệu (Governance & Stewardship) — Steward
     phân xử khi máy không quyết được.
  6. Quản lý phiên bản và lịch sử (Versioning & History).
  7. Quy tắc nghiệp vụ và luồng phê duyệt (Business Rules & Workflow).
  8. Quản lý quan hệ và phân cấp (Hierarchy & Relationship).
  9. Công bố và làm giàu dữ liệu chủ (Publishing & Syndication) — trả mã
     chuẩn + Bản ghi vàng về các hệ. Đây là chức năng duy nhất cũng có trên
     Cloud.
  10. Quản lý truy cập và bảo mật (RBAC & Security).
- **Công cụ đề xuất: TÀI LIỆU KHÔNG NÊU TÊN SẢN PHẨM MDM.** Đừng tự đặt tên
  sản phẩm khi trình bày. (Đây là 1 trong những điểm tài liệu để trống.)
- **Chạy ở đâu:** on-prem trên Node 8 (Workflow automation + MDM). Golden
  Record do **HQ sở hữu** — đơn vị không tự phát hành mã chuẩn.
- **9 domain dữ liệu chủ:** Đơn vị, Dự án, Khách hàng, Nhà cung cấp, Hợp
  đồng, Tài sản, Vật tư/Dịch vụ, Nhân sự, Bộ mã dùng chung.
- **Đảm nhiệm gì cho Quảng Ngãi:** MDM là "phiên dịch mã chuẩn" — giữ nguyên
  mã cũ tại đơn vị (FAST vẫn ghi NCC-001), tự động ánh xạ lên mã chuẩn TCT
  (vd minh họa: NCC-PTSC-0001) và mã PVN. Bảng ánh xạ 3 tầng (mã đơn vị →
  mã chuẩn TCT → mã PVN) **vừa là đầu vào vừa là đầu ra** của MDM: đơn vị
  nộp danh sách mã của mình, MDM đối chiếu và trả lại mã chuẩn.
- **Team Quảng Ngãi làm gì:** xuất file mã từng hệ + điền phiếu bộ mã
  (FAST/MESX đã phát phiếu; HRM → Bán hàng → Cảng → E-Office theo thứ tự
  FAST → MESX → HRM → Bán hàng → Cảng → E-Office). Cột mã chuẩn TCT/PVN
  **để trống** — bộ mã chuẩn chưa ban hành xuống đơn vị (câu hỏi số 6 gửi
  đoàn khảo sát). Nguồn tin cậy cho vật tư là FAST hay MESX — chưa quyết
  (câu hỏi số 5 gửi đoàn; comment PDT27 đề xuất "vật tư → ERP" nhưng ở
  Quảng Ngãi vật tư nằm cả 2 hệ).

### Nhóm D — Khai thác (dữ liệu TRẢ VỀ để dùng)

#### D1. Phân hệ công cụ xây dựng báo cáo BI — Phân hệ 8

- **Tài liệu nói:** cho phép người dùng xây dựng, trực quan hóa, phân tích
  dữ liệu bằng báo cáo, dashboard, biểu đồ tương tác phục vụ ra quyết định.
  Chạy cả on-prem lẫn Cloud. (Báo cáo kỹ thuật §3.2.)
- **Công cụ đề xuất:** **Power BI** (trên Fabric, cho 70 người dùng thường
  xuyên) + **Superset** trên on-prem (Vùng 4 đã có sẵn — báo cáo cơ bản
  không cần Cloud). Power BI Gateway để truy vấn dữ liệu on-prem.
  (Báo cáo kỹ thuật §4.8.)
- **Đảm nhiệm gì cho Quảng Ngãi:** đây là "đầu ra" mà lãnh đạo và team nhìn
  thấy mỗi ngày — dashboard hợp nhất thay cho 310 báo cáo rời rạc ghép tay
  Excel. Tenant có workspace BI riêng trên Hub.
- **Team Quảng Ngãi làm gì:** thu thập nhu cầu báo cáo/dashboard của lãnh
  đạo đơn vị (1 trong 7 việc phải làm đã chốt từ 23/10) — BI xây theo nhu
  cầu thật, không xây theo suy đoán.

#### D2. Phân hệ khai thác dữ liệu bằng ngôn ngữ tự nhiên — Text-to-data — Phân hệ 9

- **Tài liệu nói:** người dùng truy vấn dữ liệu, sinh báo cáo/biểu đồ bằng
  câu hỏi tự nhiên (Natural Language Query — NLQ), không cần viết mã. Chạy
  cả on-prem lẫn Cloud. (Báo cáo kỹ thuật §3.2, §4.9.)
- **Công cụ đề xuất:** **Power BI Q&A** (truy vấn NLQ) — có thể nhúng báo cáo
  Power BI vào ứng dụng nội bộ, cổng dữ liệu. (Báo cáo kỹ thuật §4.8–4.9.)
- **Đảm nhiệm gì cho Quảng Ngãi:** "hỏi bằng tiếng Việt" — vd: "doanh thu
  bán hàng quý này theo khách hàng" → tự sinh biểu đồ. Đây là 1 trong 2
  nhánh của luồng đi xuống (nhánh còn lại là MDM trả trực tiếp mã chuẩn +
  Bản ghi vàng).

#### D3. Thư viện mô hình học máy — AI/ML — Phân hệ 10 (CHỈ Cloud)

- **Tài liệu nói:** tập hợp thuật toán, công cụ, môi trường huấn luyện mô
  hình học máy phục vụ dự báo, phân tích nâng cao. **Không sử dụng on-prem —
  chỉ chạy trên Cloud** (Microsoft Fabric hoặc tương đương). (Báo cáo kỹ
  thuật §3.2, §4.10.)
- **Đảm nhiệm gì cho Quảng Ngãi:** phân tích nâng cao/dự báo — vd: dự báo
  nhu cầu vật tư, phát hiện bất thường. Lưu ý: AI/ML chỉ làm việc trên dữ
  liệu **đã chuẩn hóa/tổng hợp** trên Cloud, không bao giờ chạm dữ liệu gốc.

### Nhóm E — Quản trị, phân quyền & bảo mật (ai được thấy gì, ai chịu trách nhiệm)

#### E1. Quản lý và phân quyền cho các vai trò — Data Operation / RBAC — Phân hệ 5

- **Tài liệu nói:** xác định, phân quyền theo vai trò trong chu trình vận
  hành dữ liệu (DataOps), đảm bảo người dùng chỉ truy cập đúng phạm vi dữ
  liệu và chức năng được cấp. Chạy cả on-prem lẫn Cloud. (Báo cáo kỹ thuật
  §3.2.)
- **Đảm nhiệm gì cho Quảng Ngãi:** đây là "cái khóa" của tenant — RBAC/ABAC
  theo tenant đảm bảo đơn vị chỉ thấy dữ liệu của mình. Mức độ bảo mật không
  phụ thuộc vị trí lưu trữ mà phụ thuộc phân cấp phân quyền (phiên chiều
  slide in 42).
- **Team Quảng Ngãi làm gì:** rà soát ai trong đơn vị được quyền gì trên dữ
  liệu nào — danh sách này là 1 phần của hồ sơ khảo sát (người phụ trách).

#### E2. Phân hệ quản lý định danh tập trung và SSO — Phân hệ 6

- **Tài liệu nói:** quản lý danh tính người dùng tập trung, đăng nhập một
  lần (Single Sign-On) để truy cập nhiều hệ thống. Chạy cả on-prem lẫn Cloud.
  (Báo cáo kỹ thuật §3.2.)
- **Công cụ đề xuất:** nền tảng mã nguồn mở như **Keycloak** hoặc thương mại
  như **Azure AD (Entra ID)**. (Báo cáo kỹ thuật §4.6.)
- **Chạy ở đâu:** Node 6 cụm Hub (Governance + API + IAM: 16 vCPU, 64 GB
  RAM, 1 TB SSD).
- **Đảm nhiệm gì cho Quảng Ngãi:** 1 tài khoản đăng nhập 1 lần vào mọi hệ
  trên nền tảng — không còn mỗi hệ 1 mật khẩu. Tài liệu yêu cầu: OAuth2/
  OIDC/mTLS + IAM/SSO (phụ lục YCKT §2).

#### E3. Phân hệ kiểm soát hệ thống và giám sát an ninh — Monitor / SIEM — Phân hệ 11 (CHỈ on-prem)

- **Tài liệu nói:** theo dõi hoạt động toàn hệ thống, phát hiện sự cố kỹ
  thuật, rò rỉ dữ liệu, truy cập trái phép, cảnh báo sớm nguy cơ an ninh.
  **Không sử dụng trên Cloud.** (Báo cáo kỹ thuật §3.2, §4.11.)
- **Chạy ở đâu:** Node 7 cụm Hub (SIEM & Monitoring: 32 vCPU, 256 GB RAM,
  4 TB SSD — node mạnh nhất cụm). Log forward qua Syslog/Kafka/Elastic.
- **Đảm nhiệm gì cho Quảng Ngãi:** nhật ký audit của tenant đổ về SIEM tập
  trung tại Hub (tách theo tenant) — **riêng với dữ liệu nghiệp vụ**, không
  lẫn vào Lakehouse. POC GĐ1 có tiêu chí: cảnh báo đăng nhập sai 5 lần/2
  phút. Đây cũng là 1 trong 4 luồng trên sơ đồ Mermaid (luồng SIEM).
- **Giới hạn thật (nói thẳng với team):** ở tầng hạ tầng sâu nhất, đơn vị
  vận hành nền tảng về mặt kỹ thuật có khả năng truy cập — kiểm soát bằng
  phân quyền, ghi nhật ký, truy vết, chứ không phải "cách ly tuyệt đối".

#### E4. Phân hệ quản trị siêu dữ liệu — Metadata Governance — Phân hệ 12

- **Tài liệu nói:** kiểm soát quyền truy cập, bảo mật, kiểm duyệt nội dung,
  theo dõi lịch sử thay đổi, truy vết hành vi trên dữ liệu. Chạy cả on-prem
  lẫn Cloud. (Báo cáo kỹ thuật §3.2.)
- **Công cụ đề xuất:** một trong các công cụ sau (có thể kết hợp):
  **OpenMetadata, Apache Atlas, Amundsen, DataHub**. (Báo cáo kỹ thuật
  §4.12.3.)
- **Đảm nhiệm gì cho Quảng Ngãi:** "bản đồ + lý lịch" của dữ liệu — dữ liệu
  này từ hệ nào, qua những bước nào, ai đã sửa, ai đã xem (data lineage).
  Khi lãnh đạo hỏi "con số này từ đâu ra", Metadata Governance là nơi trả
  lời. Phụ lục YCKT bắt buộc vendor giao ERD + từ điển dữ liệu + metadata
  cho Data Catalog.
- **Chạy ở đâu:** Node 5 cụm Hub (Query + Metadata + Ingestion).

### Nhóm F — Hạ tầng (cái MÁY CHẠY các phân hệ trên)

#### F1. Cụm dHCI tại tầng 10 Cơ quan TCT — 8 node (Báo cáo kỹ thuật §2.2.2, tr. 59–60/83)

| Node | Loại | Cấu hình | Chạy cái gì |
|---|---|---|---|
| 1–2 | Storage Node | 16 vCPU, 128 GB RAM, 20 TB HDD + 1 TB SSD mỗi node | Lakehouse (MinIO/Iceberg) — dữ liệu RAW/SILVER/GOLD |
| 3–4 | Processing | 32 vCPU, 128 GB RAM, 2 TB SSD mỗi node | Transform (Spark/Flink/Trino) |
| 5 | Query + Metadata + Ingestion | 16 vCPU, 128 GB RAM, 1 TB SSD | Trino query, Metadata Governance, Ingestion |
| 6 | Governance + API + IAM | 16 vCPU, 64 GB RAM, 1 TB SSD | RBAC, API Gateway, SSO (Keycloak/Azure AD) |
| 7 | SIEM & Monitoring | 32 vCPU, 256 GB RAM, 4 TB SSD | SIEM tập trung, giám sát an ninh |
| 8 | Workflow automation + MDM | 32 vCPU, 128 GB RAM, 1 TB SSD | Airflow, MDM (Golden Record) |

- Mạng nội cụm: **10 Gbps** node-to-node, uplink ra ngoài ≥ 1–2 Gbps, độ
  trễ nội cụm ≤ 1–2 ms. Dung lượng khởi điểm **~40 TB, mở rộng > 200 TB**.
- Ảo hóa: **VMware vSphere/ESXi**, Tanzu Kubernetes Grid (K8s), Aria
  Operations giám sát. Sao lưu: **Veeam Data Platform Foundation** (Backup
  & Replication v12, Veeam ONE) — khôi phục theo nhật ký, hàng ngàn điểm hồi
  phục/ngày cách nhau vài giây, phát hiện ransomware trên bản sao lưu theo
  thời gian thực.
- **Team Quảng Ngãi cần nhớ:** cụm này ở TCT, không phải ở đơn vị. Với L3,
  đơn vị **không mua máy** (0 CAPEX hạ tầng dHCI) — dùng chung cụm này qua
  tenant. Chỉ khi lên L4 mới mua cụm riêng (xem §6).

#### F2. Microsoft Cloud — Fabric (Báo cáo kỹ thuật §3.3; phiên chiều)

- **Fabric Capacity F16, OneLake 20 TB, Power BI, Purview 500 tài sản, 70
  người dùng thường xuyên** — các con số này đã được 2 tài liệu xác nhận.
- Chỉ nhận dữ liệu **đã chuẩn hóa/tổng hợp** (GOLD + dữ liệu dùng chung).
  Dùng cho: Power BI lãnh đạo xem mọi nơi, thuê máy phân tích nặng/AI,
  sandbox DEV/Test. AI/ML library (Phân hệ 10) chỉ chạy ở đây.

---

## 3. Theo chân 1 bản ghi đi qua từng thành phần

*Ví dụ minh họa (ghi rõ là minh họa, không phải mã thật): 1 nhà cung cấp mới
được tạo trong FAST với mã NCC-001; cùng đối tác đó MESX đang ghi KH-118.*

| Bước | Thành phần | Đầu vào → Đầu ra | Ai bấm nút / ai quyết |
|---|---|---|---|
| 1. Thu thập | A1 Ingestion (CDC — Debezium) | Thay đổi trong DB FAST → sự kiện đẩy lên Hub ngay | Tự động (CDC đọc nhật ký DB, không quét bảng) |
| 2. Vào trục chung | A2 ESB + A3 API Gateway + A4 Kafka (Vùng 5) | Sự kiện qua Vùng 5 → kiểm tra sơ bộ (QC cửa vào: đúng định dạng, đủ trường bắt buộc?) | Tự động theo quy tắc; gói lỗi bị chặn ngay ở Vùng 5, **không vào Landing Zone** |
| 3. Đơn vị duyệt | Landing Zone (phân vùng tenant) | Gói dữ liệu chờ duyệt → Duyệt / Từ chối | **Đơn vị bấm Duyệt** (Data Owner/Steward). Từ chối → nằm lại khu cách ly trong LZ, thông báo + danh sách lỗi gửi Steward + key user hệ nguồn, sửa tại nguồn, gửi lại bản mới |
| 4. Lưu thô | B1 Lakehouse — tầng RAW (MinIO/Iceberg) | Dữ liệu duyệt xong → lưu RAW, 3 bản sao | Tự động |
| 5. Làm sạch | B2 Transform (Spark/Flink) + B3 Airflow | RAW → kiểm lỗi 8 tiêu chí → SILVER | Quy tắc DQ do team đơn vị định nghĩa; job chạy theo lịch Airflow hoặc theo sự kiện |
| 6. Gộp trùng | C1 MDM — chức năng 3+4 (Matching & Merging) | SILVER (NCC-001) + dữ liệu MESX (KH-118) → đối sánh fuzzy (mã số thuế, tên, địa chỉ) → **1 Bản ghi vàng** + mã chuẩn minh họa NCC-PTSC-0001 | Máy đối sánh; trường hợp máy không quyết được → **Data Steward phân xử** (chức năng 5) |
| 7. Lưu sản phẩm | B1 Lakehouse — tầng GOLD | Bản ghi vàng → GOLD, 2 bản sao | Tự động |
| 8a. Trả về trực tiếp | C1 MDM — chức năng 9 (Publishing) | Mã chuẩn + Bản ghi vàng → ghi ngược về FAST/MESX qua ESB (upsert, có correlationId) | Tự động; cơ chế ghi ngược từng hệ do thiết kế tích hợp quyết (chưa có trong tài liệu — câu hỏi cho đoàn) |
| 8b. Trả về qua khai thác | D1 Power BI / Superset + D2 Text-to-data | GOLD → dashboard, báo cáo, hỏi bằng tiếng Việt | Người dùng cuối |
| Song song | E3 SIEM + E4 Metadata | Mọi bước trên đều ghi log → SIEM (audit) + Metadata (lineage: bản ghi này từ FAST, qua những bước nào, ai sửa) | Tự động; SIEM cảnh báo đăng nhập sai 5 lần/2 phút |

---

## 4. 6 hệ thống Quảng Ngãi — nối vào từng thành phần thế nào

*Danh sách làm việc (chờ CNTT xác nhận đầy đủ — có thể còn hệ ngầm/hệ chết).
Phương thức nối của từng hệ là **CHƯA CHỐT, chờ khảo sát GĐ2A quyết theo
từng hệ** — bảng dưới chỉ liệt kê các phương thức CHUẨN mà phụ lục YCKT cho
phép (REST + OpenAPI, JDBC/ODBC, file mở: CSV/Excel/JSON/XML/Parquet/Avro)
và thông tin cần thu thập để quyết. Đừng trình bày bất kỳ phương án nối nào
như đã quyết.*

| Hệ | Dữ liệu chính | Domain dữ liệu chủ liên quan | Cần xác minh để chọn cách nối |
|---|---|---|---|
| Phần mềm cảng | Vận hành cảng, tàu, hàng hóa | Khách hàng, Hợp đồng, Dự án | DB gì? Có API không? Xuất file được không? |
| ERP FAST | Tài chính, mua sắm, kho, nhà cung cấp | Nhà cung cấp, Vật tư/Dịch vụ, Khách hàng, Hợp đồng | DB gì? CDC đọc được nhật ký DB không? Vendor hợp tác không? (Phiếu phỏng vấn FAST đã hỏi) |
| MESX | Vật tư/tài sản + bảo dưỡng sửa chữa | Vật tư/Dịch vụ, Tài sản | Trùng vật tư với FAST ở mức nào? Tạo mã vật tư ở đâu trước — FAST hay MESX? (đã có trong phiếu MESX) |
| Phần mềm bán hàng | Bán hàng, khách hàng, doanh thu | Khách hàng, Hợp đồng | Khách hàng trùng FAST/Cảng ra sao? |
| E-Office | Văn bản, phê duyệt, công văn | Đơn vị, Nhân sự | Phụ lục YCKT nêu tên 4 API E-Office: CreateTicket / ApproveSignEO / UpdateDocument / UpdateInvoice |
| HRM | Nhân sự, tổ chức, lương | Nhân sự, Đơn vị | Chỉ ghi cấu trúc trường, **không lấy dữ liệu cá nhân thật**; nguồn tin cậy cho nhân sự/tổ chức |

**Chồng lấn dữ liệu chủ (nói 1 slide):** nóng nhất Vật tư/Tài sản FAST ↔
MESX; Khách hàng ở 3 hệ (FAST/Bán hàng/Cảng); Nhân sự/Đơn vị gốc ở HRM.
Đây chính là việc của MDM (C1) — và là lý do bảng ánh xạ mã 3 tầng phải làm
trước.

---

## 5. Ai vận hành cái gì — HQ / đơn vị / vendor

*Theo Phương án 3 (phiên chiều slide in 59): HQ đầu tư Hub + khung dùng
chung; đơn vị đầu tư/thuê spoke + tích hợp nội bộ; đơn vị chưa có ngân sách
được HQ đầu tư trước, ghi nợ.*

| Nhiệm vụ | HQ (TCT) | Đơn vị (Quảng Ngãi) | Vendor / nhà thầu |
|---|---|---|---|
| Vận hành cụm Hub 8 node, Lakehouse, SIEM, SSO | X (đội vận hành Hub) | — | — |
| Vận hành ESB + MDM Golden Record | X | — | — |
| Vận hành Fabric/Power BI | X (thuê Microsoft) | — | Microsoft |
| Agent thu thập tại đơn vị, kết nối 6 hệ lên Hub | Hướng dẫn, cấp chuẩn | **X (team I&T đơn vị)** | Hỗ trợ theo hợp đồng tích hợp |
| Duyệt/từ chối ở Landing Zone | — | **X (Data Owner/Steward)** | — |
| Xuất file mã, điền phiếu bộ mã, đối chiếu mã | — | **X (key user từng hệ)** | — |
| Định nghĩa quy tắc kiểm lỗi (DQ) cho dữ liệu mình | Phê duyệt khung | **X** | — |
| Vận hành L3 (phân bổ theo mức sử dụng) | X (tính phí theo dùng) | Dùng, trả phí phân bổ | — |
| Vận hành L4 (nếu lên) | Giám sát theo chuẩn TCT | **X (đội riêng tại đơn vị)** | — |
| Triển khai tích hợp 6 hệ + làm sạch dữ liệu | Khung + chuẩn | **X (đơn vị chi trả)** | Thi công theo gói thầu |

---

## 6. Nếu lên L4 — thành phần nào chuyển xuống Spoke

*Đề xuất thu nhỏ của em từ cấu hình cụm Hub (Báo cáo kỹ thuật §2.2.2) —
KHÔNG có tài liệu nào cho cấu hình Spoke của đơn vị. Phần cứng Spoke ước
~8,5 tỷ (khoảng 6–12 tỷ), chỉ là phần cứng, chưa phải tổng 22 tỷ năm đầu L4.*

| Thành phần | L3 Tenant (mặc định) | L4 Spoke (có điều kiện) |
|---|---|---|
| Lakehouse (MinIO/Iceberg) | Phân vùng trên Hub | **Chuyển xuống Spoke** — 2 node Storage (16 vCPU, 128 GB RAM, 20 TB HDD + 2 TB SSD mỗi node) |
| Transform (Spark/Flink/Trino) + BI Superset | Trên Hub | **Chuyển xuống Spoke** — 2 node Processing/Query (32 vCPU, 128–256 GB RAM, 2–4 TB NVMe mỗi node) |
| Governance + API + Workflow + Monitor | Trên Hub | **Chuyển xuống Spoke** — 1 node kết hợp (16–32 vCPU, 128 GB RAM, 2 TB SSD) |
| ESB | Hub | **Ở LẠI Hub** — Spoke không có ESB riêng |
| MDM Golden Record | Hub (HQ sở hữu) | **Ở LẠI Hub** — Spoke chỉ nhận mã chuẩn về, không tự phát hành |
| SIEM | Hub | **Ở LẠI Hub** — log Spoke forward về SIEM Hub; Spoke **không** có node SIEM riêng |
| AI/ML library | Cloud (Fabric) | Cloud (không đổi) |
| Đội vận hành | Không cần đội riêng | **Phải có đội riêng tại đơn vị**, vận hành theo chuẩn TCT; phí vận hành ~2,4 tỷ/năm (tính từ năm thứ 2) |
| Mạng | Đẩy toàn bộ dữ liệu lên Hub (dòng dày) | Chỉ đồng bộ dùng chung + tổng hợp lên Hub (dòng thưa hơn) |

4 tiêu chí xét lên L4 (phiên chiều slide in 50): (1) khối lượng + tốc độ
tăng dữ liệu lớn; (2) phân tích chuyên ngành cường độ cao/thời gian thực;
(3) ràng buộc pháp lý/hợp đồng buộc lưu tại chỗ; (4) đủ đội IT tự vận hành
theo chuẩn TCT. Quyết định sau khảo sát GĐ2A + đăng ký tháng 12/2026.

---

## 7. Những gì KHÔNG được nói như đã chốt trong bài team

- **Không nêu tên sản phẩm MDM** — tài liệu không nêu tên. (Lỗi deck HTML cũ
  từng mắc: ghi tên sản phẩm không có trong tài liệu.)
- **Không chốt cách nối từng hệ** (CDC hay API hay file) — chờ khảo sát GĐ2A.
  Lỗi deck cũ: "6 hệ thống kết nối qua CDC/Airbyte" như sự thật.
- **Không trình bày cấu hình Spoke 5 node như tài liệu** — đó là đề xuất thu
  nhỏ của em từ cấu hình Hub; tài liệu không cho cấu hình Spoke.
- **Không trình bày chi tiết nội bộ của tenant** (vd: tenant có node riêng
  nào) — tài liệu chỉ nói tenant là phân vùng riêng trên Hub + agent/API tại
  đơn vị; phần còn lại trong file này là cách đọc kỹ thuật, đã ghi rõ "suy
  ra".
- **Không đưa con số chi phí 10 tỷ / 22 tỷ** như số của PTSC — đó là ước tính
  theo giả định (đã ghi rõ trong file mô hình chi phí), chỉ dùng với lãnh đạo.
- **Không chốt GĐ2 = 2026–2027 hay 2028+** (2 tài liệu vênh nhau), không chốt
  Combo 2 cho Quảng Ngãi, không trích số đếm level 21 vs 17 đơn vị.

---

## 8. Gợi ý chia slide cho Phần 2 kỹ thuật

*Tổng Phần 2 kỹ thuật ≈ 12–14 slide (bản 90 phút). Mỗi dòng = 1 slide.*

1. Bức tranh tổng 3 tầng (§1) — vẽ lại sơ đồ 3 tầng, 3 nguyên tắc vàng.
2. Nhóm A: Thu thập & tích hợp — Ingestion + CDC (§A1, A5).
3. Nhóm A (tiếp): Vùng 5 — ESB + API Gateway + Kafka (§A2–A4) — slide
   "4 anh em, không phải ESB chứa hết".
4. Nhóm B: Lakehouse RAW → SILVER → GOLD + 3 bản/2 bản sao (§B1).
5. Nhóm B (tiếp): Transform + Airflow (§B2–B3).
6. Nhóm C: MDM 10 chức năng + 9 domain (§C1) — slide nặng nhất, cho 5 phút.
7. Nhóm D: Khai thác — Power BI/Superset + Text-to-data + AI/ML (§D1–D3).
8. Nhóm E: RBAC + SSO + SIEM + Metadata (§E1–E4) — slide bảo mật.
9. Nhóm F: Cụm Hub 8 node + Fabric (§F1–F2) — bảng node.
10. Theo chân 1 bản ghi (§3) — dùng sơ đồ Mermaid động (slide 7 deck Giám
    đốc) chạy từng luồng, đối chiếu bảng §3.
11. 6 hệ thống + bảng chồng lấn (§4).
12. Ai vận hành cái gì (§5).
13. Nếu lên L4 (§6) — bảng so sánh L3/L4 theo thành phần.
14. Chưa chốt (§7) + việc của từng người (P2-10 trong dàn ý).

*File này là nội dung chi tiết cho các slide trên. Khi dựng slide, mỗi
thành phần chỉ giữ 3 ý trên slide (tên + đảm nhiệm gì + chạy ở đâu), chi tiết
còn lại cho vào ghi chú diễn giải.*
