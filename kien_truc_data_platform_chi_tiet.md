# BẢN ĐẶC TẢ KIẾN TRÚC TỔNG THỂ NỀN TẢNG DỮ LIỆU (HYBRID DATA PLATFORM)
## MÔ HÌNH HUB - SPOKE GIỮA TỔNG CÔNG TY VÀ PTSC QUẢNG NGÃI (LEVEL 3)

---

> **Tài liệu tham chiếu:**
> * *Báo cáo Đề xuất Kỹ thuật Nền tảng Dữ liệu PTSC (Trang 16–38, 59, 78)*
> * *Slide Hội thảo Data Platform Tổng công ty – Phiên Sáng & Phiên Chiều (Trang 21–25, 45, 51–56)*
> * *Quy chế Quản trị Dữ liệu PTSC (Mô hình 5 Cấp & Chuẩn PPDM)*

---

## 1. SƠ ĐỒ KIẾN TRÚC TỔNG THỂ TOÀN HỆ THỐNG (END-TO-END ARCHITECTURE)

Sơ đồ dưới đây mô tả chi tiết toàn bộ luồng dữ liệu đi qua 4 tầng: **Nguồn nội bộ Quảng Ngãi ➔ Trạm trung chuyển & Vùng đệm kiểm duyệt (Landing Zone) ➔ Nền tảng On-premise Hub tại TCT ➔ Nền tảng Cloud Fabric (Tenant L3) & Dashboard điều hành**.

```mermaid
graph TB
    %% ==========================================
    %% TẦNG 1: NGUỒN DỮ LIỆU NỘI BỘ QUẢNG NGÃI
    %% ==========================================
    subgraph TANG_1 ["TẦNG 1: CƠ SỞ DỮ LIỆU & PHẦN MỀM NỘI BỘ (PTSC QUẢNG NGÃI)"]
        direction TB
        S1[("FAST Accounting<br>• Sổ cái, Công nợ<br>• Doanh thu, Chi phí<br>(SQL Server)")]
        S2[("MESx - PMSx - FBO<br>• Tiến độ xưởng cơ khí<br>• Vật tư chế tạo<br>• Nhân lực ca kíp<br>(PostgreSQL)")]
        S3[("VTI - IRTECH<br>• Khai thác Cầu Cảng<br>• Sản lượng bãi, nâng hạ<br>• Nhật trình xe cẩu, tàu<br>(MySQL/Oracle)")]
        S4[("HSEQ & Mua sắm<br>• Đang chuẩn hóa chuẩn API<br>• Quy trình phê duyệt<br>• Quản lý nhà thầu phụ<br>(REST API Ready)")]
        S5[("File nghiệp vụ phân tán<br>• File Excel dự toán<br>• Bảng chấm công ngoài bãi<br>• Hồ sơ nghiệm thu PDF")]
    end

    %% ==========================================
    %% TẦNG 2: TRẠM TRUNG CHUYỂN & VÙNG ĐỆM LANDING ZONE
    %% ==========================================
    subgraph TANG_2 ["TẦNG 2: TRẠM TRUNG CHUYỂN SPOKE & CỔNG PHÊ DUYỆT (NỘI BỘ QUẢNG NGÃI)"]
        direction TB
        Agent["Integration Agent / CDC<br>(Thu thập dữ liệu tự động / Batch / API)"]
        
        LZ["VÙNG ĐỆM KIỂM DUYỆT (LANDING ZONE)<br>• Lưu trữ tạm thời dữ liệu trích xuất<br>• Kiểm tra cấu trúc Schema<br>• Đối soát mã Master Data"]

        subgraph GATEWAY ["CỔNG PHÊ DUYỆT & BẢO MẬT (DATA GOVERNANCE GATEWAY)"]
            direction LR
            DO_Gate{"LÃNH ĐẠO ĐƠN VỊ<br>(Data Owner Cấp 3)<br>Kiểm duyệt & Approve"}
            Masking["Module Lọc & Che dữ liệu (Masking)<br>• Tách thông tin lương cá nhân<br>• Ẩn số CCCD/Tài khoản ngân hàng<br>• Giữ lại dữ liệu mật kinh doanh"]
        end
    end

    %% ==========================================
    %% TẦNG 3: HẠ TẦNG ON-PREMISE HUB TẠI TỔNG CÔNG TY
    %% ==========================================
    subgraph TANG_3 ["TẦNG 3: NỀN TẢNG ON-PREMISE HUB TẬP TRUNG (DATA CENTER TỔNG CÔNG TY)"]
        direction TB
        
        subgraph ZONE_SEC ["Phân vùng Mạng & An toàn thông tin (8 Zones)"]
            WAF["Firewall & WAF"]
            VPN_GW["VPN IPSec Gateway<br>(Đường hầm mã hóa Site-to-Site)"]
        end

        subgraph INTEGRATION_BUS ["Trục tích hợp & Quản trị dữ liệu lõi"]
            ESB["Trục tích hợp ESB (WSO2 / Camel)<br>• API Gateway tập trung<br>• Message Broker (Kafka)"]
            MDM["Hệ thống Dữ liệu chủ MDM<br>• 29 Danh mục Master Data<br>• Bản ghi vàng (Golden Record)<br>• Khử trùng lặp mã Nhà cung cấp/Vật tư"]
        end

        subgraph ONPREM_LAKE ["Hồ chứa dữ liệu tại chỗ (On-premise Lakehouse)"]
            Bronze[("BRONZE ZONE<br>Raw Data Store<br>(MinIO S3 - Delta/Parquet)<br>Lưu vết dữ liệu gốc")]
            Silver[("SILVER ZONE<br>Cleaned Data Store<br>Dữ liệu đã chuẩn hóa, gán nhãn")]
        end

        subgraph SEC_MONITOR ["Giám sát An ninh & Kiểm toán"]
            SIEM["Hệ thống SIEM / SOC 24/7<br>• Audit Log toàn bộ truy cập<br>• Phát hiện dò quét dữ liệu trái phép"]
            IAM_Local["Quản lý định danh IAM / Keycloak<br>Phân quyền RBAC theo Domain"]
        end
    end

    %% ==========================================
    %% TẦNG 4: NỀN TẢNG ĐÁM MÂY CLOUD FABRIC & TIÊU THỤ
    %% ==========================================
    subgraph TANG_4 ["TẦNG 4: CLOUD DATA PLATFORM & PHÂN VÙNG TENANT L3 (MICROSOFT FABRIC)"]
        direction TB
        
        subgraph TENANT_QN ["WORKSPACE L3 - PTSC QUẢNG NGÃI (ĐỘC LẬP HOÀN TOÀN)"]
            Gold_QN[("GOLD ZONE (OneLake)<br>• Dữ liệu tổng hợp SXKD<br>• Báo cáo Doanh thu - Dòng tiền<br>• Báo cáo Khai thác Cảng")]
            Pipeline_QN["Data Factory Pipelines<br>(Tự động tính toán số liệu nội bộ)"]
            Semantic_QN["Semantic Models (Đo lường KPI)<br>• Tỷ lệ hoàn thành ngân sách<br>• Năng suất cẩu bãi, vòng quay tàu"]
            PBI_QN["Power BI Reports (Nội bộ QN)<br>• Dashboard Ban Giám đốc QN<br>• Dashboard Trưởng phòng Kế toán/Cảng"]
        end

        subgraph TENANT_TCT ["WORKSPACE TỔNG CÔNG TY (HỢP NHẤT TOÀN TCT)"]
            Gold_TCT[("Kho dữ liệu Hợp nhất TCT<br>(Chỉ nhận số liệu tổng hợp)")]
            PBI_TCT["Dashboard Lãnh đạo TCT<br>(Báo cáo Hợp nhất 17 ĐVTV)"]
        end

        Purview["Microsoft Purview<br>Data Governance & Catalog toàn hệ thống"]
    end

    %% ==========================================
    %% KẾT NỐI VÀ DÒNG CHẢY DỮ LIỆU
    %% ==========================================
    S1 & S2 & S3 & S4 & S5 -->|Trích xuất định kỳ/CDC| Agent
    Agent --> LZ
    LZ --> DO_Gate
    
    DO_Gate -->|Từ chối/Reject| LZ
    DO_Gate -->|Chấp thuận/Approve| Masking
    
    Masking ==>|Truyền an toàn qua kênh VPN| VPN_GW
    VPN_GW --> WAF --> ESB
    
    ESB <--> MDM
    ESB --> Bronze
    Bronze -->|Xử lý làm sạch & biến đổi| Silver
    
    Silver ==>|Chỉ đẩy số liệu tổng hợp & chuẩn hóa| Gold_QN
    Gold_QN --> Pipeline_QN --> Semantic_QN --> PBI_QN
    
    Silver -->|Trích xuất số liệu hợp nhất TCT| Gold_TCT --> PBI_TCT
    
    ESB -.->|Ghi vết kiểm toán| SIEM
    IAM_Local -.->|Xác thực phân quyền| ESB
    Purview -.->|Quản trị siêu dữ liệu| Gold_QN & Gold_TCT

    %% Styling
    classDef qn fill:#eff6ff,stroke:#1d4ed8,stroke-width:2px,color:#1e3a8a;
    classDef tct fill:#f0fdf4,stroke:#15803d,stroke-width:2px,color:#14532d;
    classDef cloud fill:#faf5ff,stroke:#7e22ce,stroke-width:2px,color:#581c87;
    classDef gate fill:#fffbeb,stroke:#b45309,stroke-width:2px,color:#78350f;
    
    class S1,S2,S3,S4,S5,Agent,LZ,TENANT_QN,Gold_QN,Pipeline_QN,Semantic_QN,PBI_QN qn;
    class TANG_3,WAF,VPN_GW,ESB,MDM,Bronze,Silver,SIEM,IAM_Local,TENANT_TCT,Gold_TCT,PBI_TCT tct;
    class TANG_4,Purview cloud;
    class DO_Gate,Masking gate;
```

---

## 2. CỔNG QUYẾT ĐỊNH DỮ LIỆU: CÁI GÌ ĐẨY LÊN, CÁI GÌ GIỮ LẠI?

Đây là cơ chế kỹ thuật cốt lõi giải tỏa lo lắng của Ban Giám đốc về an toàn bí mật kinh doanh. Dữ liệu trước khi ra khỏi mạng nội bộ của Quảng Ngãi phải đi qua **Bộ lọc phân loại 3 mức**:

```mermaid
flowchart TD
    Start([Dữ liệu phát sinh tại PTSC Quảng Ngãi]) --> Classify{Phân loại Dữ liệu theo Quy chế}

    %% Nhánh 1: Dữ liệu Cấm ra ngoài / Cực mật
    Classify -->|MỨC 1: DỮ LIỆU BÍ MẬT & CÁ NHÂN| LocalOnly[GIỮ LẠI 100% TẠI QUẢNG NGÃI]
    LocalOnly --> N1["• Chi tiết mức lương từng cán bộ, nhân viên<br>• Số CCCD, số tài khoản ngân hàng cá nhân<br>• Dự toán nội bộ các gói thầu đang chuẩn bị đấu thầu<br>• Hồ sơ khiếu nại, tranh chấp hợp đồng riêng"]
    N1 --> LocalDB[("Cơ sở dữ liệu On-prem nội bộ QN<br>Không kết nối ra Internet")]

    %% Nhánh 2: Dữ liệu Nghiệp vụ chuyên ngành
    Classify -->|MỨC 2: DỮ LIỆU CHUYÊN NGÀNH NỘI BỘ| WorkspaceL3[LƯU VÀO WORKSPACE L3 CỦA QUẢNG NGÃI]
    WorkspaceL3 --> N2["• Chi tiết nhật trình từng chuyến xe cẩu, tàu lai dắt tại Cảng<br>• Sản lượng chi tiết từng phân xưởng cơ khí Dung Quất<br>• Nhật ký công trường, chấm công hàng ngày theo ca kíp<br>• Báo cáo quản trị tài chính nội bộ phục vụ riêng Ban Giám đốc QN"]
    N2 --> MaskingProcess[Qua bước Masking / Làm sạch dữ liệu cá nhân]
    MaskingProcess --> TenantCloud[("Đẩy vào Tenant L3 trên Fabric<br>(Chỉ User Quảng Ngãi xem được, TCT không thấy)")]

    %% Nhánh 3: Dữ liệu Dùng chung & Hợp nhất
    Classify -->|MỨC 3: DỮ LIỆU BÁO CÁO HỢP NHẤT| SharedHub[ĐỒNG BỘ VỀ HUB TỔNG CÔNG TY]
    SharedHub --> N3["• Báo cáo tổng hợp Doanh thu - Lợi nhuận định kỳ<br>• Tổng số lượng lao động & Tổng quỹ lương công ty<br>• Danh mục Master Data: Mã Khách hàng, Nhà cung cấp chuẩn<br>• Báo cáo An toàn HSE, sự cố kỹ thuật theo quy định TCT"]
    N3 --> Approval{Lãnh đạo Đơn vị Duyệt<br>Approve / Reject}
    Approval -->|Chấp thuận| HubSync[("Đẩy về Data Hub TCT<br>Phục vụ Báo cáo Hợp nhất Lãnh đạo TCT")]
    Approval -->|Từ chối| Hold["Tạm dừng, yêu cầu phòng ban chỉnh sửa lại"]

    classDef red fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef blue fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef green fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    
    class LocalOnly,N1,LocalDB red;
    class WorkspaceL3,N2,MaskingProcess,TenantCloud blue;
    class SharedHub,N3,Approval,HubSync green;
```

---

## 3. CƠ CHẾ VÙNG ĐỆM KIỂM DUYỆT (LANDING ZONE) HOẠT ĐỘNG THẾ NÀO?

Tại **Trang 23–24 Slide Phiên Sáng**, TCT cam kết: *"Dữ liệu không bị lấy tùy ý; mỗi đơn vị có Landing Zone riêng để kiểm duyệt trước khi đưa vào vùng dùng chung"*.

Cơ chế vận hành vùng đệm gồm 4 bước kỹ thuật nghiêm ngặt:

```
[4 Phần mềm QN: FAST, MESx, VTI, HSEQ]
                    │
                    ▼  (Bước 1: Trích xuất tự động vào nửa đêm)
┌───────────────────────────────────────────────────────────┐
│              LANDING ZONE (VÙNG ĐỆM NỘI BỘ)                │
│                                                           │
│  [Bảng dữ liệu thô vừa trích xuất]                         │
│  ├── Doanh thu các dự án tháng vừa qua                     │
│  ├── Danh sách Nhà cung cấp vật tư mới phát sinh           │
│  └── Sản lượng bãi cảng hàng hóa                          │
│                                                           │
│  [Hệ thống tự động chạy Validation Rule]:                 │
│  1. Kiểm tra Schema: Đúng định dạng số/chữ/ngày tháng?     │
│  2. Kiểm tra Master Data: Mã nhà cung cấp có trong MDM?   │
│  3. Kiểm tra An toàn: Có bị dính thông tin cá nhân (PII)? │
└───────────────────────────────────────────────────────────┘
                    │
                    ▼  (Bước 2: Hiển thị thông báo kiểm duyệt)
┌───────────────────────────────────────────────────────────┐
│     GIAO DIỆN PHÊ DUYỆT CỦA DATA STEWARD & DATA OWNER     │
│                                                           │
│  • Cán bộ phụ trách dữ liệu (IT QN): Soát lỗi kỹ thuật    │
│  • Lãnh đạo Đơn vị (Data Owner QN): Duyệt nội dung        │
│                                                           │
│  [Nút BẤM: APPROVE] ───────────────► [Nút BẤM: REJECT]    │
│         │                                    │            │
└─────────┼────────────────────────────────────┼────────────┘
          │ (Bước 3: Cho phép truyền)          │ (Bước 4: Hủy luồng)
          ▼                                    ▼
[Mã hóa đẩy qua VPN về Hub]          [Gửi email cảnh báo lỗi]
```

---

## 4. MA TRẬN PHÂN QUYỀN (RBAC / ABAC) GIỮA CÁC ĐỐI TƯỢNG

Hệ thống sử dụng cơ chế định danh tập trung (Microsoft Entra ID / Azure AD) kết hợp phân quyền theo vai trò (Role-Based Access Control):

| Đối tượng người dùng | Xem số liệu Quảng Ngãi | Xem số liệu ĐVTV khác (M&C, POS...) | Xem Báo cáo Hợp nhất TCT | Quyền hạn trên Tenant L3 Quảng Ngãi |
| :--- | :---: | :---: | :---: | :--- |
| **Ban Giám đốc PTSC Quảng Ngãi** | ✅ **Toàn quyền 100%** | ❌ **Không** | ✅ **Chỉ tiêu TCT giao cho QN** | **Data Owner Cấp 3:** Quyết định phê duyệt dữ liệu, xem toàn bộ Dashboard nội bộ. |
| **Trưởng phòng / Key User QN** | 🟡 **Theo phân quyền** *(Phòng nào thấy phòng đó)* | ❌ **Không** | ❌ **Không** | **Data Contributor:** Xem Dashboard chuyên ngành của phòng mình phụ trách. |
| **Admin IT PTSC Quảng Ngãi** | 🔧 **Quản trị kỹ thuật** | ❌ **Không** | ❌ **Không** | **Data Steward Cấp 4:** Quản trị luồng Pipeline, tạo báo cáo, phân quyền User nội bộ. |
| **Lãnh đạo Ban TGĐ Tổng công ty** | 🟡 **Chỉ xem số liệu tổng hợp hợp nhất** | ✅ **Xem tổng hợp các ĐVTV** | ✅ **Toàn quyền TCT** | Không có quyền xem chi tiết nội bộ trong Tenant QN; chỉ xem báo cáo hợp nhất trên Hub. |
| **Đội IT TCT (Admin Level 5)** | ⚙️ **Chỉ thấy trạng thái Server/Kênh mạng** | ⚙️ **Chỉ thấy Server/Kênh mạng** | ⚙️ **Vận hành hạ tầng** | **Không được cấp quyền mở xem dữ liệu nghiệp vụ**. Nếu cố tình truy cập sẽ bị SIEM ghi vết và cảnh báo vi phạm. |
| **Các Đơn vị bạn (PTSC M&C, POS...)** | ❌ **Tuyệt đối cấm** | ❌ **Chỉ thấy đơn vị họ** | ❌ **Không** | Bị cô lập 100% bởi phân vùng Tenant riêng biệt. |

---

## 5. BẢNG ĐẶC TẢ CÁC THÀNH PHẦN KỸ THUẬT CỐT LÕI (TECHNICAL STACK)

| Thành phần | Công nghệ / Nền tảng áp dụng | Vị trí đặt | Chức năng chi tiết trong hệ thống |
| :--- | :--- | :---: | :--- |
| **Spoke Integration Agent** | Docker Container / Light Service | On-prem QN | Tự động đọc dữ liệu từ FAST, MESx, VTI đẩy vào Landing Zone nội bộ. |
| **Landing Zone Staging** | Local Database / Folder bảo mật | On-prem QN | Vùng đệm tạm thời để thực hiện kiểm tra chất lượng và duyệt dữ liệu. |
| **Kênh truyền bảo mật** | IPSec VPN Tunnel (AES-256) | DC QN ↔ DC TCT | Kênh truyền dữ liệu riêng biệt qua mạng nội bộ ngành, không lộ IP ra Internet. |
| **Trục tích hợp (ESB)** | WSO2 Enterprise Integrator / Apache Camel | On-prem Hub TCT | Tiếp nhận API, định tuyến dữ liệu, chuyển đổi định dạng và điều phối tải. |
| **Hồ chứa dữ liệu On-prem** | MinIO Object Storage (S3 API), Iceberg/Parquet | On-prem Hub TCT | Lưu trữ dữ liệu thô (Bronze) và dữ liệu chi tiết an toàn trong két sắt nội bộ. |
| **Hệ thống Dữ liệu chủ (MDM)** | Master Data Management Hub | On-prem Hub TCT | Chuẩn hóa danh mục khách hàng, nhà cung cấp, vật tư theo bản ghi chuẩn TCT. |
| **Giám sát An ninh (SIEM/SOC)** | Centralized SIEM (Wazuh / Splunk) | On-prem Hub TCT | Giám sát 24/7, ghi nhận log ai xem gì, lúc nào để chống rò rỉ dữ liệu. |
| **Phân vùng Tenant L3** | Microsoft Fabric Workspace Capacity | Microsoft Cloud | Không gian lưu trữ đám mây riêng của Quảng Ngãi để xử lý dữ liệu báo cáo. |
| **Hồ chứa đám mây** | OneLake Storage (Delta Parquet) | Microsoft Cloud | Chứa dữ liệu đã tinh chế (Gold Zone) phục vụ tính toán phân tích tốc độ cao. |
| **Quản trị Danh mục Cloud** | Microsoft Purview | Microsoft Cloud | Quản lý vòng đời dữ liệu, siêu dữ liệu (Metadata) và truy vết nguồn gốc (Lineage). |
| **Báo cáo trực quan (BI)** | Power BI Service & Mobile App | Web & Điện thoại | Giao diện Dashboard cho Ban Giám đốc và cán bộ quản lý xem số liệu tức thì. |

---

## 6. ÁNH XẠ PHẦN MỀM NỘI BỘ QUẢNG NGÃI VÀO CHUẨN PPDM FRAMEWORK (DUAL-CODE ARCHITECTURE)

> **Tham chiếu:** *Slide Hội thảo Data Platform – Phiên Sáng (Trang 35–39): Mô hình ngành PPDM, Kiến trúc mã kép Dual-Code, Chuỗi giá trị P1→P7 & 8 Deliverables D1–D8.*

Tổng công ty đã xây dựng hệ thống phân loại hoạt động theo chuẩn **PPDM (Professional Petroleum Data Management)** kết hợp **Dual-Code Architecture**: mỗi hoạt động có đồng thời **Mã nội bộ PTSC (Company Code)** và **Mã chuẩn quốc tế (NORSOK / ISO / VSIC 2018)**, liên kết qua bảng `DISCIPLINE_CODE_XREF` với mức tin cậy `EXACT / PARTIAL / NONE`.

Để đảm bảo dữ liệu từ Quảng Ngãi khi đẩy về Hub TCT được gắn đúng nhãn ngành và truy vết nguồn gốc xuyên suốt chuỗi giá trị, các phần mềm nội bộ QN được ánh xạ vào mô hình PPDM như sau:

| Phần mềm nội bộ QN | Mã ngành PPDM (Primary) | Mã ngành PPDM (Support) | Deliverable liên quan | Ghi chú ánh xạ |
| :--- | :---: | :---: | :---: | :--- |
| **FAST Accounting** | — | **S1** (Corporate Governance / Finance) | D1 (Contract Package) | Cung cấp dữ liệu Doanh thu – Chi phí – Dòng tiền – Công nợ; phục vụ báo cáo hợp nhất tài chính TCT theo VSIC 2018. |
| **MESx – PMSx – FBO** | **P5** (Fabrication) | **S4** (Asset Management) | D6 (FAT/ITR Package) | Quản lý tiến độ xưởng cơ khí Dung Quất, vật tư chế tạo, nhân lực ca kíp. Deliverable chính: hồ sơ nghiệm thu chế tạo (FAT). |
| **VTI – IRTECH (Cảng)** | **P6** (T&I / Marine Services) | **S4** (Asset Management) | D7 (CFIHOS Handover + Marine Svc.) | Sản lượng bãi cảng, nhật trình xe cẩu – tàu lai dắt. Ánh xạ vào mảng dịch vụ cảng & vận tải biển. |
| **HSEQ** | — | **S3** (HSE) | Xuyên suốt P1→P7 | An toàn lao động, sự cố kỹ thuật, báo cáo HSE theo quy định TCT. Chạy song song toàn chuỗi qua `SUPPORT_FUNC_LINK` với vai trò `VERIFY / APPROVE`. |
| **Module Mua sắm** | **P4** (Procurement) | **S1** (Corporate Governance) | D4 (Purchase Requisition), D5 (Material Supply) | Đề xuất mua hàng, quản lý nhà thầu phụ, đối soát mã nhà cung cấp chuẩn MDM. |
| **File Excel / PDF phân tán** | Tùy nội dung | Tùy nội dung | — | Dự toán, chấm công bãi, nghiệm thu → cần số hóa và gắn nhãn Discipline Code trước khi đẩy vào Landing Zone. |

**Nguyên tắc bất biến khi ánh xạ** *(theo 5 nguyên tắc PPDM của TCT – Trang 39 Slide Phiên Sáng):*

1. **Không FK trực tiếp giữa Discipline → Discipline** — mọi liên kết chỉ thông qua Deliverable (bảng `DISCIPLINE_DELIVERABLE`).
2. **Company Code là display key** — sử dụng mã nội bộ dạng `VNG-ME-DS-0001`, không dùng surrogate key số.
3. **Mapping tại cấp thấp nhất** (Sub-Discipline) — ví dụ: `P5.ME → NORSOK:ME = EXACT`.
4. **Không sửa code, chỉ retire** — khi thay đổi: set `expiry_date`, tạo bản ghi mới.
5. **Mở rộng bằng dữ liệu, không bằng schema** — thêm ngành/phần mềm mới chỉ cần `INSERT`, không đổi cấu trúc bảng.

---

## 7. TIÊU CHUẨN KỸ THUẬT TÍCH HỢP BẮT BUỘC (13 ĐIỀU KHOẢN TỪ PHỤ LỤC TCT)

> **Tham chiếu:** *Phụ lục về yêu cầu tích hợp Data Platform (Văn bản chính thức TCT – PTSC-ADM-RG08-FM10, 5 trang).*
> Đây là bộ tiêu chuẩn bắt buộc mà **mọi nhà cung cấp phần mềm** (kể cả phần mềm đã triển khai tại QN như FAST, VTI, MESx) phải tuân thủ khi tích hợp với Data Platform của TCT.

| STT | Nhóm tiêu chuẩn | Yêu cầu cốt lõi | Ứng dụng tại Quảng Ngãi |
| :---: | :--- | :--- | :--- |
| **1** | Giao diện tích hợp chuẩn | Phần mềm phải cung cấp **REST API** hoặc cho phép truy cập trực tiếp CSDL qua **CDC** (Change Data Capture). | Yêu cầu FAST (SQL Server) mở CDC; VTI/IRTECH mở REST API hoặc cho phép đọc DB replica. |
| **2** | Hỗ trợ Change Data Capture | Phải có cơ chế CDC hoặc Change Log Table để phát hiện và đồng bộ thay đổi dữ liệu theo thời gian thực hoặc near-realtime. | MESx (PostgreSQL) kích hoạt Logical Replication / Debezium CDC. |
| **3** | Backfill & Replay | Hỗ trợ cơ chế **backfill/replay theo khoảng thời gian** (time window) để xử lý dữ liệu đến muộn (late arriving) và tái đồng bộ khi sự cố. | Quan trọng khi Pipeline QN bị gián đoạn → cần replay lại dữ liệu từ mốc thời gian cụ thể. |
| **4** | Ổn định khóa chính (Primary Key) | Khóa chính các thực thể lõi (tổ chức, tài sản, nhân sự, hợp đồng...) phải **ổn định, không thay đổi theo thời gian**. Cam kết mapping ID nội bộ với MDM/ESB của TCT. | Đối soát mã Nhà cung cấp, mã Vật tư giữa FAST ↔ MDM Hub TCT. |
| **5** | Bảo mật tích hợp & IAM | Hỗ trợ **OAuth 2.0 / OpenID Connect** và/hoặc **mTLS** cho API; cho phép tích hợp IAM/SSO hiện có (Keycloak/ADFS/LDAP). | Tất cả API từ QN về Hub TCT phải qua xác thực OAuth 2.0 token, không dùng Basic Auth. |
| **6** | Quản lý Metadata & Data Dictionary | Cung cấp **ERD, Data Dictionary** (mô tả bảng/cột/kiểu/ràng buộc); cam kết cập nhật tài liệu khi thay đổi version. | Yêu cầu các vendor cung cấp ERD cho Data Platform đồng bộ vào Data Catalog (Purview). |
| **7** | Hiệu năng kênh tích hợp | Cam kết **Scalability** cho API & Batch; không giới hạn tích hợp bởi license; không ảnh hưởng hiệu năng giao dịch online khi chạy job trích xuất. | Đảm bảo job trích xuất đêm từ FAST/VTI không gây chậm phần mềm vào giờ làm việc. |
| **8** | Idempotent & Traceability | API/Message phải **idempotent** (gửi lại nhiều lần cùng request ID không gây trùng dữ liệu); hỗ trợ **correlationId / traceId** end-to-end. | Mỗi giao dịch đồng bộ từ QN về Hub mang correlation ID → truy vết toàn luồng qua ESB, Data Platform. |
| **9** | Môi trường kiểm thử DEV/UAT | Cung cấp **môi trường DEV/UAT** với API tương đương production; cung cấp dữ liệu mẫu và kịch bản test tích hợp 2 chiều. | Trước khi go-live Pipeline QN, test đầy đủ trên môi trường UAT của từng phần mềm. |
| **10** | Cam kết mở / Không khóa vendor | Không giới hạn số interface; cấu hình/API tích hợp có thể truy cập bởi đội kỹ thuật QN/TCT, **không phụ thuộc độc quyền vendor**. | Đảm bảo khi hết hợp đồng bảo trì với vendor, QN vẫn tự vận hành được Pipeline. |
| **11** | Chất lượng dữ liệu & Đối soát | Cung cấp bộ **Data Quality Rules** tối thiểu (null/format/uniqueness/FK/code list); có cơ chế **quarantine** bản ghi lỗi. | Landing Zone QN chạy Validation Rule tự động → tách riêng bản ghi lỗi để phòng ban chỉnh sửa. |
| **12** | Giám sát vận hành tích hợp | Cơ chế giám sát: số lượng giao dịch, tỷ lệ lỗi, số lần retry, độ trễ đồng bộ (lag/latency); cung cấp **Runbook** xử lý sự cố. | Tích hợp metric giám sát Pipeline QN vào hệ thống SIEM/SOC tập trung của Hub TCT. |
| **13** | Quản lý thay đổi Schema | Tất cả interface/API/file schema phải có **versioning**; đảm bảo **backward compatible**; có **deprecation policy** khi loại bỏ version cũ. | Khi vendor nâng cấp FAST hoặc VTI → phải thông báo trước và đảm bảo Pipeline không bị gãy. |

**Cách áp dụng thực tế tại PTSC Quảng Ngãi:**

Khi làm việc với các nhà cung cấp phần mềm hiện tại (FAST, VTI/IRTECH, MESx...), đội IT Quảng Ngãi sử dụng đúng 13 điều khoản trên làm **checklist đàm phán kỹ thuật** để yêu cầu vendor mở API, cung cấp tài liệu ERD và cam kết hỗ trợ tích hợp. Các điều khoản này đã được Tổng công ty ban hành chính thức dưới dạng **Phụ lục hợp đồng bắt buộc** cho mọi dự án triển khai phần mềm mới hoặc gia hạn hợp đồng phần mềm hiện hữu.

---

## 8. LỘ TRÌNH DÀI HẠN: ĐIỀU KIỆN "TỐT NGHIỆP" TỪ LEVEL 3 LÊN LEVEL 4 (SPOKE RIÊNG)

> **Tham chiếu:** *Slide Hội thảo Data Platform – Phiên Chiều (Trang 50, 55, 59): Tiêu chí nâng level, Mô hình phục vụ đơn vị nhỏ vs đơn vị lớn.*

Tổng công ty xác định rõ: **Level 3 là mức tối ưu nhất cho PTSC Quảng Ngãi ở giai đoạn hiện tại**, vì tiết kiệm chi phí đầu tư hạ tầng (không phát sinh CAPEX cho cụm dHCI riêng), vẫn được cấp Tenant/Workspace riêng biệt hoàn toàn trên Hub TCT, và đủ đáp ứng nhu cầu báo cáo điều hành nội bộ.

Tuy nhiên, TCT cũng đã quy hoạch sẵn **lộ trình nâng cấp lên Level 4** cho các đơn vị đủ điều kiện, dự kiến xem xét trong **giai đoạn chuyển đổi số thứ ba (sau năm 2028)**:

```mermaid
flowchart LR
    subgraph HIEN_TAI ["GIAI ĐOẠN HIỆN TẠI (2026–2028)"]
        L3["PTSC Quảng Ngãi<br><b>LEVEL 3</b><br>• Tenant riêng trên Hub TCT<br>• Không CAPEX hạ tầng<br>• Đội IT vận hành Pipeline cơ bản"]
    end

    subgraph DANH_GIA ["XÉT ĐỊNH KỲ HÀNG NĂM"]
        direction TB
        TC1["① Khối lượng & tốc độ tăng dữ liệu<br>Đẩy thô về Hub tốn kém hơn<br>xử lý tại chỗ (băng thông, lưu trữ)?"]
        TC2["② Nhu cầu phân tích chuyên ngành<br>cường độ cao<br>Dữ liệu sensor/IoT/thời gian thực<br>mà độ trễ qua Hub không đáp ứng?"]
        TC3["③ Ràng buộc pháp lý / hợp đồng<br>Dữ liệu buộc phải lưu và<br>xử lý tại đơn vị?"]
        TC4["④ Năng lực vận hành<br>Đội CNTT đơn vị đủ khả năng<br>vận hành nền tảng theo chuẩn TCT?"]
    end

    subgraph TUONG_LAI ["SAU 2028 (NẾU ĐỦ ĐIỀU KIỆN)"]
        L4["PTSC Quảng Ngãi<br><b>LEVEL 4</b><br>• Cụm dHCI riêng tại đơn vị<br>• Hybrid Data Platform đầy đủ<br>• IT-OT / IoT / Realtime quy mô lớn<br>• Đội vận hành nền tảng chuyên trách"]
    end

    L3 --> TC1
    TC1 --> TC2 --> TC3 --> TC4
    TC4 -->|"Đạt mức trưởng thành số ≥ 3.5"| L4
    TC4 -->|"Chưa đạt → Giữ L3"| L3

    classDef current fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a;
    classDef eval fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;
    classDef future fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;

    class L3 current;
    class TC1,TC2,TC3,TC4 eval;
    class L4 future;
```

### Bảng so sánh chi phí & lợi ích giữa L3 và L4

| Tiêu chí | Level 3 (Hiện tại) | Level 4 (Tương lai) |
| :--- | :--- | :--- |
| **Chi phí hạ tầng (CAPEX)** | Không phát sinh — dùng chung Hub TCT | Cao — phải đầu tư cụm dHCI riêng tại đơn vị |
| **Chi phí vận hành (OPEX)** | Thấp — phân bổ theo mức sử dụng | Cao — cần đội vận hành nền tảng chuyên trách |
| **Quyền dữ liệu chuyên ngành** | Có phân vùng Tenant riêng, nhưng hạ tầng nằm tại Hub | Chủ động hoàn toàn — dữ liệu lưu và xử lý tại đơn vị |
| **Khả năng Real-time / IoT / OT** | Hạn chế — phụ thuộc băng thông và độ trễ về Hub | Chủ động hoàn toàn — xử lý tại chỗ, không phụ thuộc Hub |
| **Yêu cầu đội IT** | Data Owner + Data Steward + đầu mối kỹ thuật | Đội vận hành nền tảng đầy đủ theo chuẩn TCT |
| **Mức trưởng thành số (DBI)** | Từ 2.0 đến 3.5 | Trên 3.5 |
| **Thời điểm xem xét** | Áp dụng ngay | Sau 2028, xét định kỳ hàng năm |

### Nhận định chiến lược

Với quy mô hiện tại của PTSC Quảng Ngãi (4 mảng chính: Cơ khí chế tạo, Khai thác Cảng, Dịch vụ tàu biển, Dịch vụ hỗ trợ), **Level 3 là lựa chọn tối ưu** vì:
- **Tiết kiệm ngân sách tối đa**: Không phải đầu tư hạ tầng phần cứng dHCI hàng tỷ đồng.
- **Vẫn có không gian riêng hoàn toàn**: Tenant L3 trên Fabric được cô lập 100%, TCT và các đơn vị bạn không thể nhìn thấy dữ liệu chuyên ngành nội bộ.
- **Tận dụng năng lực Hub**: Hệ thống MDM, ESB, SIEM, Purview đã được TCT đầu tư và vận hành sẵn — QN chỉ cần tập trung vào nghiệp vụ, không cần lo vận hành hạ tầng nặng.
- **Giữ lộ trình mở**: Khi nhu cầu dữ liệu IoT/sensor từ bãi cảng hoặc xưởng Dung Quất tăng đột biến, QN hoàn toàn có thể đề xuất nâng lên L4 dựa trên 4 tiêu chí định lượng rõ ràng của TCT.

---

