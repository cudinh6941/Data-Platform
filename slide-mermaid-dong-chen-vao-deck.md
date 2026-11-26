# SLIDE SƠ ĐỒ ĐỘNG — KHỐI CHÈN SẴN CHO BỘ SLIDE ĐÃ CÓ

## Cách chèn (cho agent, 5 phút)

1. Mở file HTML bộ slide kết hợp (`slide-thuyet-trinh-lanh-dao-data-platform-quang-ngai.html`).
2. Tìm slide L4 Spoke (tiêu đề chứa "L4" / "Spoke") — paste toàn bộ khối `<section ...>...</section>` trong khung code bên dưới NGAY SAU thẻ đóng `</section>` của slide đó (tức là trước slide 10 vùng an ninh).
3. Sửa `data-slide="?"` thành số đúng (số của slide L4 + 1), rồi ĐÁNH LẠI số `data-slide` cho mọi slide sau nó.
4. Chèn 1 mục vào mảng `SPEAKER_NOTES` ở đúng vị trí tương ứng (nội dung ở cuối file này).
5. Mở file kiểm tra: đi từ slide trước qua slide này rồi sang slide sau phải mượt, 3 nút luồng chạy đúng, bấm node sáng đúng đường nối.

Khối này TỰ CHỨA CSS + JS của riêng nó (class tiền tố `mmap-`), không phụ thuộc class của bộ slide cũ — paste vào là chạy. Nội dung + quan hệ lấy đúng từ file Mermaid `so-do-kien-truc-tong-the-data-platform.md` (đã vẽ lại bằng tay cho layout sạch, vì layout tự động của Mermaid bị rối).

## Khối code — copy nguyên khung này, paste vào file HTML của bộ slide

```html
<section class="slide mmap-slide" data-slide="?" data-act="PHẦN I · TỔNG QUAN" data-title="Bức tranh tổng — Sơ đồ động">
  <style>
    .mmap-slide h2{font-size:30px;margin:0 0 6px;color:#F1F5F9}
    .mmap-slide .mmap-sub{color:#94A3B8;font-size:15px;margin:0 0 14px}
    .mmap-slide .mmap-btns{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:10px}
    .mmap-slide .mmap-btns button{cursor:pointer;border:1px solid #22D3EE;background:transparent;color:#22D3EE;
      padding:8px 15px;border-radius:10px;font-size:14px;font-weight:600;font-family:inherit}
    .mmap-slide .mmap-btns button.on{background:#22D3EE;color:#060B19}
    .mmap-slide .mmap-btns button.mmap-o{border-color:#FB923C;color:#FB923C}
    .mmap-slide .mmap-btns button.mmap-o.on{background:#FB923C;color:#060B19}
    .mmap-slide .mmap-btns button.mmap-r{border-color:#F87171;color:#F87171}
    .mmap-slide .mmap-btns button.mmap-r.on{background:#F87171;color:#060B19}
    .mmap-slide .mmap-btns button.mmap-g{border-color:#475569;color:#94A3B8}
    .mmap-slide .mmap-legend{font-size:13px;color:#94A3B8;margin-bottom:10px}
    .mmap-slide .mmap-legend b{color:#E6EDF7}
    .mmap-slide .mmap-legend .sw{display:inline-block;width:26px;height:0;border-top:3px solid #06B6D4;vertical-align:middle;margin:0 4px}
    .mmap-slide .mmap-legend .sw.dash{border-top-style:dashed;border-top-color:#FB923C}
    .mmap-slide .mmap-legend .sw.red{border-top-color:#F87171}
    .mmap-slide .mmap-board{background:rgba(255,255,255,.03);border:1px solid #1E293B;border-radius:16px;padding:6px}
    .mmap-slide .mmap-board svg{width:100%;height:auto;display:block}
    .mmap-slide .mmap-board svg text{font-family:"Be Vietnam Pro",system-ui,sans-serif}
    .mmap-slide .mmap-info{min-height:42px;margin-top:10px;padding:9px 14px;border:1px solid #1E293B;border-radius:10px;
      background:#0B1526;font-size:14px;color:#CBD5E1}
    .mmap-slide .mmap-info b{color:#22D3EE}
    .mmap-slide .mmap-cap{font-size:12px;color:#64748B;margin-top:8px}
    .mmap-slide svg .mmap-node,.mmap-slide svg .mmap-edge{transition:opacity .45s ease}
    .mmap-slide svg .mmap-edge{pointer-events:none}
    .mmap-slide svg.mmap-dim .mmap-node,.mmap-slide svg.mmap-dim .mmap-edge{opacity:.14}
    .mmap-slide svg .mmap-edge.mmap-on{stroke-width:3.5px !important;
      stroke-dasharray:10 7 !important;animation:mmap-dash 1s linear infinite}
    @keyframes mmap-dash{to{stroke-dashoffset:-17}}
    .mmap-slide svg .mmap-node.mmap-on{filter:drop-shadow(0 0 7px rgba(34,211,238,.9))}
    .mmap-slide svg .mmap-node.mmap-on rect{stroke-width:3px !important}
    @media (prefers-reduced-motion: reduce){
      .mmap-slide svg .mmap-edge.mmap-on{animation:none}
      .mmap-slide svg .mmap-node,.mmap-slide svg .mmap-edge{transition:none}
    }
  </style>

  <h2>Bức tranh tổng — toàn bộ Data Platform trên một trang</h2>
  <p class="mmap-sub">6 hệ thống ở Quảng Ngãi &rarr; qua 1 trục ESB duy nhất &rarr; vào Hub của Tổng công ty &rarr; lên Cloud. Bấm 1 nút để xem từng đường đi, một đường một lúc.</p>

  <div class="mmap-btns">
    <button id="mmap-b-up" onclick="mmapPlay('up')">1 &middot; Đi lên — dữ liệu thô lên Hub</button>
    <button id="mmap-b-down" class="mmap-o" onclick="mmapPlay('down')">2 &middot; Đi xuống — mã chuẩn trả về</button>
    <button id="mmap-b-siem" class="mmap-r" onclick="mmapPlay('siem')">3 &middot; Giám sát — log về SIEM</button>
    <button class="mmap-g" onclick="mmapPlayAll()">&#9654; Chạy thử toàn bộ</button>
    <button class="mmap-g" onclick="mmapReset()">Xóa animation</button>
  </div>
  <div class="mmap-legend"><b>Chú thích:</b><span class="sw"></span> đi lên (nét liền xanh)
    <span class="sw dash"></span> đi xuống (nét đứt cam)
    <span class="sw red"></span> log giám sát (đỏ)
    &nbsp;·&nbsp; Bấm vào 1 hộp bất kỳ để xem nó nối với đâu.</div>

  <div class="mmap-board">
  <svg id="mmap-svg" viewBox="0 0 1240 800" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" aria-label="Sơ đồ tổng thể Data Platform PTSC">
    <defs>
      <marker id="mmap-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0 0L10 5L0 10z" fill="#64748B"></path>
      </marker>
    </defs>

    <!-- 4 CỘT -->
    <rect x="16" y="16" width="284" height="768" rx="14" fill="rgba(52,211,153,.05)" stroke="rgba(148,163,184,.35)" stroke-width="1.5"/>
    <text x="30" y="46" font-size="12" letter-spacing="2" fill="#94A3B8">ĐƠN VỊ — PTSC QUẢNG NGÃI</text>
    <rect x="316" y="16" width="120" height="768" rx="14" fill="rgba(148,163,184,.05)" stroke="rgba(148,163,184,.35)" stroke-width="1.5"/>
    <text x="326" y="46" font-size="12" letter-spacing="2" fill="#94A3B8">ĐƯỜNG TRUYỀN</text>
    <rect x="456" y="16" width="448" height="768" rx="14" fill="rgba(96,165,250,.05)" stroke="rgba(148,163,184,.35)" stroke-width="1.5"/>
    <text x="470" y="46" font-size="12" letter-spacing="2" fill="#94A3B8">HUB — TỔNG CÔNG TY (TẠI CHỖ)</text>
    <rect x="924" y="16" width="300" height="768" rx="14" fill="rgba(147,197,253,.05)" stroke="rgba(148,163,184,.35)" stroke-width="1.5"/>
    <text x="938" y="46" font-size="12" letter-spacing="2" fill="#94A3B8">MICROSOFT CLOUD — FABRIC</text>

    <!-- CỘT ĐƠN VỊ: 6 HỆ THỐNG -->
    <g class="mmap-node" id="n-s1" style="cursor:pointer">
      <rect x="36" y="70" width="174" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="89" font-size="13" font-weight="600" fill="#E6EDF7">Phần mềm Cảng</text>
      <text x="48" y="106" font-size="11" fill="#94A3B8">khai thác cảng</text>
    </g>
    <g class="mmap-node" id="n-s2" style="cursor:pointer">
      <rect x="36" y="128" width="174" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="147" font-size="13" font-weight="600" fill="#E6EDF7">ERP FAST</text>
      <text x="48" y="164" font-size="11" fill="#94A3B8">tài chính · mua sắm</text>
    </g>
    <g class="mmap-node" id="n-s3" style="cursor:pointer">
      <rect x="36" y="186" width="174" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="205" font-size="13" font-weight="600" fill="#E6EDF7">MESX</text>
      <text x="48" y="222" font-size="11" fill="#94A3B8">vật tư · tài sản · bảo dưỡng</text>
    </g>
    <g class="mmap-node" id="n-s4" style="cursor:pointer">
      <rect x="36" y="244" width="174" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="263" font-size="13" font-weight="600" fill="#E6EDF7">Phần mềm Bán hàng</text>
      <text x="48" y="280" font-size="11" fill="#94A3B8">bán hàng · thu tiền</text>
    </g>
    <g class="mmap-node" id="n-s5" style="cursor:pointer">
      <rect x="36" y="302" width="174" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="321" font-size="13" font-weight="600" fill="#E6EDF7">E-Office</text>
      <text x="48" y="338" font-size="11" fill="#94A3B8">văn bản · trình ký</text>
    </g>
    <g class="mmap-node" id="n-s6" style="cursor:pointer">
      <rect x="36" y="360" width="174" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="379" font-size="13" font-weight="600" fill="#E6EDF7">HRM</text>
      <text x="48" y="396" font-size="11" fill="#94A3B8">nhân sự · tổ chức</text>
    </g>
    <!-- Thanh thu thập dọc -->
    <g class="mmap-node" id="n-ag" style="cursor:pointer">
      <rect x="232" y="70" width="60" height="336" rx="10" fill="rgba(52,211,153,.14)" stroke="#34D399" stroke-width="1.5"/>
      <text transform="rotate(-90 262 238)" x="262" y="238" font-size="12" letter-spacing="2" fill="#A7F3D0" text-anchor="middle">TÁC NHÂN THU THẬP</text>
    </g>
    <g class="mmap-node" id="n-mh" style="cursor:pointer">
      <rect x="36" y="452" width="256" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="471" font-size="13" font-weight="600" fill="#E6EDF7">Màn hình khai thác</text>
      <text x="48" y="488" font-size="11" fill="#94A3B8">Dashboard · Phòng điều hành</text>
    </g>
    <g class="mmap-node" id="n-pd" style="cursor:pointer">
      <rect x="36" y="514" width="256" height="46" rx="9" fill="rgba(52,211,153,.10)" stroke="#34D399" stroke-width="1.5"/>
      <text x="48" y="533" font-size="13" font-weight="600" fill="#E6EDF7">Phê duyệt</text>
      <text x="48" y="550" font-size="11" fill="#94A3B8">Data Owner · Data Steward</text>
    </g>

    <!-- ĐƯỜNG TRUYỀN -->
    <g class="mmap-node" id="n-nw" style="cursor:pointer">
      <rect x="328" y="368" width="96" height="80" rx="10" fill="rgba(148,163,184,.10)" stroke="#94A3B8" stroke-width="1.5"/>
      <text x="376" y="394" font-size="12" font-weight="600" fill="#E6EDF7" text-anchor="middle">SD-WAN</text>
      <text x="376" y="412" font-size="12" font-weight="600" fill="#E6EDF7" text-anchor="middle">VPN</text>
      <text x="376" y="430" font-size="11" fill="#94A3B8" text-anchor="middle">Zero Trust</text>
    </g>

    <!-- HUB -->
    <g class="mmap-node" id="n-z5" style="cursor:pointer">
      <rect x="476" y="150" width="180" height="100" rx="10" fill="rgba(96,165,250,.12)" stroke="#60A5FA" stroke-width="1.5"/>
      <text x="488" y="178" font-size="13" font-weight="600" fill="#E6EDF7">Zone 5 — Tích hợp &amp; Đệm</text>
      <text x="488" y="198" font-size="11" fill="#94A3B8">ESB WSO2 · API Gateway</text>
      <text x="488" y="216" font-size="11" fill="#94A3B8">Kafka · CDC · Airbyte</text>
      <text x="488" y="234" font-size="11" fill="#94A3B8">Kiểm tra chất lượng</text>
    </g>
    <g class="mmap-node" id="n-lz" style="cursor:pointer">
      <rect x="676" y="150" width="208" height="100" rx="10" fill="rgba(96,165,250,.12)" stroke="#60A5FA" stroke-width="1.5"/>
      <text x="688" y="178" font-size="13" font-weight="600" fill="#E6EDF7">Landing Zone</text>
      <text x="688" y="198" font-size="11" fill="#94A3B8">Đơn vị phê duyệt trước khi</text>
      <text x="688" y="216" font-size="11" fill="#94A3B8">vào vùng dùng chung</text>
    </g>
    <g class="mmap-node" id="n-z4" style="cursor:pointer">
      <rect x="560" y="290" width="324" height="120" rx="10" fill="rgba(96,165,250,.14)" stroke="#60A5FA" stroke-width="1.5"/>
      <text x="572" y="318" font-size="13" font-weight="600" fill="#E6EDF7">Zone 4 — Server Farm (vùng lõi)</text>
      <text x="572" y="338" font-size="11" fill="#94A3B8">Lakehouse Iceberg · MinIO</text>
      <text x="572" y="358" font-size="11" fill="#94A3B8">MDM 10 chức năng · Golden Record</text>
      <text x="572" y="378" font-size="11" fill="#94A3B8">BI Superset · K8s · Trino · Flink</text>
    </g>
    <g class="mmap-node" id="n-z3" style="cursor:pointer">
      <rect x="676" y="450" width="208" height="60" rx="10" fill="rgba(96,165,250,.12)" stroke="#60A5FA" stroke-width="1.5"/>
      <text x="688" y="476" font-size="13" font-weight="600" fill="#E6EDF7">Zone 3 — Security</text>
      <text x="688" y="494" font-size="11" fill="#94A3B8">SIEM — nhận audit log</text>
    </g>
    <text x="476" y="548" font-size="11" fill="#64748B">7 vùng còn lại — chi tiết ở slide sau</text>
    <g class="mmap-node" id="n-z1" style="cursor:pointer"><rect x="476" y="560" width="52" height="44" rx="8" fill="rgba(96,165,250,.07)" stroke="#475569" stroke-width="1"/><text x="502" y="578" font-size="11" font-weight="600" fill="#CBD5E1" text-anchor="middle">Zone 1</text><text x="502" y="594" font-size="10" fill="#94A3B8" text-anchor="middle">Edge</text></g>
    <g class="mmap-node" id="n-z2" style="cursor:pointer"><rect x="534" y="560" width="52" height="44" rx="8" fill="rgba(96,165,250,.07)" stroke="#475569" stroke-width="1"/><text x="560" y="578" font-size="11" font-weight="600" fill="#CBD5E1" text-anchor="middle">Zone 2</text><text x="560" y="594" font-size="10" fill="#94A3B8" text-anchor="middle">DMZ</text></g>
    <g class="mmap-node" id="n-z6" style="cursor:pointer"><rect x="592" y="560" width="52" height="44" rx="8" fill="rgba(96,165,250,.07)" stroke="#475569" stroke-width="1"/><text x="618" y="578" font-size="11" font-weight="600" fill="#CBD5E1" text-anchor="middle">Zone 6</text><text x="618" y="594" font-size="10" fill="#94A3B8" text-anchor="middle">Dịch vụ</text></g>
    <g class="mmap-node" id="n-z7" style="cursor:pointer"><rect x="650" y="560" width="52" height="44" rx="8" fill="rgba(96,165,250,.07)" stroke="#475569" stroke-width="1"/><text x="676" y="578" font-size="11" font-weight="600" fill="#CBD5E1" text-anchor="middle">Zone 7</text><text x="676" y="594" font-size="10" fill="#94A3B8" text-anchor="middle">Lưu trữ</text></g>
    <g class="mmap-node" id="n-z8" style="cursor:pointer"><rect x="708" y="560" width="52" height="44" rx="8" fill="rgba(96,165,250,.07)" stroke="#475569" stroke-width="1"/><text x="734" y="578" font-size="11" font-weight="600" fill="#CBD5E1" text-anchor="middle">Zone 8</text><text x="734" y="594" font-size="10" fill="#94A3B8" text-anchor="middle">Vận hành</text></g>
    <g class="mmap-node" id="n-z9" style="cursor:pointer"><rect x="766" y="560" width="52" height="44" rx="8" fill="rgba(96,165,250,.07)" stroke="#475569" stroke-width="1"/><text x="792" y="578" font-size="11" font-weight="600" fill="#CBD5E1" text-anchor="middle">Zone 9</text><text x="792" y="594" font-size="10" fill="#94A3B8" text-anchor="middle">Backup</text></g>
    <g class="mmap-node" id="n-z10" style="cursor:pointer"><rect x="824" y="560" width="52" height="44" rx="8" fill="rgba(96,165,250,.07)" stroke="#475569" stroke-width="1"/><text x="850" y="578" font-size="11" font-weight="600" fill="#CBD5E1" text-anchor="middle">Zone 10</text><text x="850" y="594" font-size="10" fill="#94A3B8" text-anchor="middle">OOB</text></g>

    <!-- CLOUD -->
    <g class="mmap-node" id="n-cl" style="cursor:pointer">
      <rect x="944" y="290" width="260" height="120" rx="10" fill="rgba(147,197,253,.10)" stroke="#93C5FD" stroke-width="1.5"/>
      <text x="956" y="318" font-size="13" font-weight="600" fill="#E6EDF7">OneLake 20 TB</text>
      <text x="956" y="338" font-size="11" fill="#94A3B8">Power BI · Purview</text>
      <text x="956" y="358" font-size="11" fill="#94A3B8">Workspace riêng từng tenant</text>
      <text x="956" y="378" font-size="11" fill="#94A3B8">AI · Text-to-data</text>
    </g>
    <g class="mmap-node" id="n-rule" style="cursor:pointer">
      <rect x="944" y="450" width="260" height="60" rx="10" fill="rgba(147,197,253,.07)" stroke="#475569" stroke-width="1"/>
      <text x="956" y="476" font-size="11" fill="#CBD5E1">Chỉ dữ liệu đã chuẩn hóa</text>
      <text x="956" y="494" font-size="11" fill="#CBD5E1">mới lên Cloud — dữ liệu thô ở lại</text>
    </g>

    <!-- ĐƯỜNG NỐI -->
    <!-- Đi lên -->
    <path id="e-s1-ag" class="mmap-edge" d="M210 93 H232" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-s2-ag" class="mmap-edge" d="M210 151 H232" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-s3-ag" class="mmap-edge" d="M210 209 H232" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-s4-ag" class="mmap-edge" d="M210 267 H232" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-s5-ag" class="mmap-edge" d="M210 325 H232" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-s6-ag" class="mmap-edge" d="M210 383 H232" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-ag-nw" class="mmap-edge" d="M262 406 C 262 436, 296 408, 328 408" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-nw-z5" class="mmap-edge" d="M424 388 C 456 380, 456 200, 476 200" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-z5-lz" class="mmap-edge" d="M656 200 H676" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-lz-z4" class="mmap-edge" d="M760 250 C 760 272, 722 268, 722 290" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <path id="e-z4-cl" class="mmap-edge" d="M884 350 H944" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <!-- Giám sát -->
    <path id="e-z4-z3" class="mmap-edge" d="M780 410 V450" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#mmap-ar)"/>
    <!-- Phê duyệt (đi qua khe giữa 2 panel, tránh cắt hộp) -->
    <path id="e-lz-pd" class="mmap-edge" d="M676 200 H446 V640 H120 V560" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="5 5" marker-end="url(#mmap-ar)"/>
    <!-- Đi xuống: 2 đường về chung 1 trục dưới cùng -->
    <path id="e-z4-mh" class="mmap-edge" d="M892 410 V700 H164 V498" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="5 5" marker-end="url(#mmap-ar)"/>
    <path id="e-cl-mh" class="mmap-edge" d="M1074 410 V700 H164 V498" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="5 5" marker-end="url(#mmap-ar)"/>

    <!-- Nhãn đường -->
    <text x="300" y="632" font-size="11" fill="#64748B">Đơn vị phê duyệt</text>
    <text x="560" y="692" font-size="11" fill="#64748B">Mã chuẩn · Bản ghi vàng · Báo cáo BI trả về đơn vị</text>
    <text x="792" y="434" font-size="11" fill="#64748B">Audit log</text>
  </svg>
  </div>

  <div class="mmap-info" id="mmap-info">Chưa chạy luồng nào — bấm 1 nút ở trên, hoặc bấm vào 1 hộp trong sơ đồ.</div>
  <p class="mmap-cap">Nguồn: sơ đồ tổng thể (file Mermaid so-do-kien-truc-tong-the-data-platform.md) — slide 25 bộ slide hội thảo phiên sáng 08/2026; Đề xuất kỹ thuật TCT-DP (2025). Sơ đồ vẽ theo dạng Tenant (L3/L4 chốt sau khảo sát GĐ2A).</p>

  <script>
  (function(){
    var svg = document.getElementById('mmap-svg');
    var NS = 'http://www.w3.org/2000/svg';
    var XLINK = 'http://www.w3.org/1999/xlink';
    var sleep = function(ms){ return new Promise(function(r){ setTimeout(r, ms); }); };
    var token = 0;
    var FLOWS = {
      up:   { color:'#0891B2', dot:'#06B6D4', label:'Đi lên — dữ liệu thô lên Hub',
              edges:['e-s1-ag','e-s2-ag','e-s3-ag','e-s4-ag','e-s5-ag','e-s6-ag','e-ag-nw','e-nw-z5','e-z5-lz','e-lz-z4','e-z4-cl'],
              steps:[['s1','s2','s3','s4','s5','s6'],['ag'],['nw'],['z5'],['lz'],['z4'],['cl']] },
      down: { color:'#EA580C', dot:'#FB923C', label:'Đi xuống — mã chuẩn trả về',
              edges:['e-z4-mh','e-cl-mh'],
              steps:[['z4','cl'],['mh']] },
      siem: { color:'#DC2626', dot:'#F87171', label:'Giám sát — log về SIEM',
              edges:['e-z4-z3'],
              steps:[['z4'],['z3']] }
    };
    var NAMES = { s1:'Phần mềm Cảng', s2:'ERP FAST', s3:'MESX', s4:'Phần mềm Bán hàng', s5:'E-Office', s6:'HRM',
      ag:'Tác nhân thu thập', nw:'Đường truyền SD-WAN/VPN', z5:'Zone 5 — Tích hợp & Đệm (ESB)', lz:'Landing Zone',
      z4:'Zone 4 — Server Farm (Lakehouse + MDM)', z3:'Zone 3 — Security (SIEM)', cl:'Microsoft Cloud — Fabric',
      mh:'Màn hình khai thác', pd:'Phê duyệt (Data Owner/Steward)',
      z1:'Zone 1 — Internet Edge', z2:'Zone 2 — DMZ', z6:'Zone 6 — Shared Services', z7:'Zone 7 — Storage',
      z8:'Zone 8 — Management & Operations', z9:'Zone 9 — Backup & DR', z10:'Zone 10 — Out-of-band Management',
      rule:'Quy tắc: dữ liệu thô không lên Cloud' };
    var INFO = { z5:'Trục ESB duy nhất tại Hub (vùng 5) — mọi trao đổi giữa đơn vị và Hub đều đi qua đây, gắn mã vận đơn và ghi audit log.',
      lz:'Vùng đệm riêng của Quảng Ngãi — đơn vị mình duyệt rồi dữ liệu mới vào vùng dùng chung. Gói lỗi bị chặn lại ở đây.',
      z4:'Vùng lõi: kho Lakehouse (Iceberg · MinIO) + MDM 10 chức năng, nơi sinh ra Bản ghi vàng.',
      cl:'Chỉ nhận dữ liệu đã làm sạch, chuẩn hóa và tổng hợp — dữ liệu thô không lên Cloud.',
      ag:'Thu thập tại chỗ (API · CDC · ETL · File) hoặc Hub kéo qua API — cơ chế chốt theo từng hệ thống khi khảo sát.',
      mh:'Báo cáo BI tại chỗ (Superset) và báo cáo Power BI / phân tích AI từ Cloud đều về màn hình này.' };
    function nodeEl(k){ return svg.querySelector('#n-' + k); }
    function clearDots(){ svg.querySelectorAll('circle.mmap-dot').forEach(function(c){ c.remove(); }); }
    function clearAll(){
      svg.querySelectorAll('.mmap-on').forEach(function(e){ e.classList.remove('mmap-on'); });
      svg.classList.remove('mmap-dim'); clearDots();
      svg.querySelectorAll('.mmap-edge').forEach(function(p){ p.style.stroke = ''; });
    }
    function spawnDot(pathEl, color, dur){
      var c = document.createElementNS(NS, 'circle');
      c.setAttribute('r', '7'); c.setAttribute('fill', color); c.setAttribute('class', 'mmap-dot');
      var am = document.createElementNS(NS, 'animateMotion');
      am.setAttribute('dur', dur + 's'); am.setAttribute('repeatCount', 'indefinite');
      var mp = document.createElementNS(NS, 'mpath');
      mp.setAttributeNS(XLINK, 'xlink:href', '#' + pathEl.id);
      am.appendChild(mp); c.appendChild(am); svg.appendChild(c);
    }
    function setInfo(html){ document.getElementById('mmap-info').innerHTML = html; }
    function markBtn(name){
      ['up','down','siem'].forEach(function(n){
        var b = document.getElementById('mmap-b-' + n); if(b) b.classList.remove('on');
      });
      var b = document.getElementById('mmap-b-' + name); if(b) b.classList.add('on');
    }
    async function play(name, myToken){
      var f = FLOWS[name]; var my = (myToken !== undefined ? myToken : ++token);
      clearAll(); markBtn(name); svg.classList.add('mmap-dim');
      f.edges.forEach(function(id){
        var p = document.getElementById(id); if(!p) return;
        p.classList.add('mmap-on'); p.style.stroke = f.color; spawnDot(p, f.dot, 1.4);
      });
      for(var i = 0; i < f.steps.length; i++){
        if(my !== token) return;
        f.steps[i].forEach(function(k){ var g = nodeEl(k); if(g) g.classList.add('mmap-on'); });
        setInfo('<b>' + f.label + ':</b> đang sáng tới ' + f.steps[i].map(function(k){ return NAMES[k] || k; }).join(' + '));
        await sleep(500);
      }
      if(my !== token) return;
      setInfo('<b>' + f.label + ':</b> ' + f.steps.flat().map(function(k){ return NAMES[k] || k; }).join(' → '));
    }
    window.mmapPlay = function(name){ play(name); };
    window.mmapReset = function(){
      token++; clearAll(); markBtn('');
      setInfo('Đã xóa animation — sơ đồ trở về trạng thái đầy đủ.');
    };
    window.mmapPlayAll = async function(){
      var my = ++token;
      await play('up', my);   if(my !== token) return; await sleep(1200);
      await play('down', my); if(my !== token) return; await sleep(1200);
      await play('siem', my);
    };
    // Bấm vào 1 hộp: chỉ sáng các đường nối tới hộp đó
    svg.querySelectorAll('g.mmap-node').forEach(function(g){
      g.addEventListener('click', function(){
        var key = g.id.replace(/^n-/, '');
        token++; clearAll(); markBtn(''); svg.classList.add('mmap-dim');
        var links = [];
        svg.querySelectorAll('path.mmap-edge').forEach(function(p){
          var parts = p.id.replace(/^e-/, '').split('-');
          if(parts.indexOf(key) !== -1){
            p.classList.add('mmap-on'); p.style.stroke = '#22D3EE'; spawnDot(p, '#22D3EE', 1.4);
            links.push((NAMES[parts[0]] || parts[0]) + ' ↔ ' + (NAMES[parts[1]] || parts[1]));
          }
        });
        g.classList.add('mmap-on');
        var extra = INFO[key] ? '<br>' + INFO[key] : '';
        setInfo('<b>' + (NAMES[key] || key) + '</b> nối với: ' + (links.join(' · ') || 'không có đường nối trực tiếp — hộp này chỉ mang tính tham chiếu') + extra);
      });
    });
  })();
  </script>
</section>
```

## SPEAKER NOTES — chèn nguyên văn vào mảng SPEAKER_NOTES, đúng vị trí slide mới

> "Slide bản đồ tổng: toàn bộ Data Platform trên một trang. Đi theo 3 đường, một đường một lúc — đi lên (dữ liệu thô từ 6 hệ thống qua ESB, Landing Zone, Lakehouse/MDM lên BI), đi xuống (mã chuẩn + Bản ghi vàng trả về phần mềm nguồn), giám sát (log về SIEM). Khi lãnh đạo hỏi 'chỗ này nằm đâu', quay lại slide này và bấm đúng chế độ luồng để chỉ. Nhớ nhấn: chỉ có MỘT trục ESB duy nhất ở Hub, đơn vị không có ESB riêng; dữ liệu thô không lên Cloud."

## Kiểm tra sau khi chèn (riêng slide này)

- [ ] Slide nằm đúng vị trí: sau slide L4 Spoke, trước slide 10 vùng an ninh?
- [ ] Điều hướng OK: từ slide trước sang slide mới rồi sang slide sau mượt, số slide không lệch, ghi chú các slide sau không bị sai?
- [ ] 3 nút chế độ luồng hoạt động: bấm nút nào chỉ luồng đó sáng + chạy, các đường khác mờ xuống?
- [ ] Node sáng lần lượt đúng thứ tự ở chế độ Đi lên (nguồn → Tác nhân → Mạng → Zone 5 → LZ → Zone 4 → Cloud)?
- [ ] Bấm 1 node thì chỉ đường nối tới node đó sáng, khung giải thích hiện đúng nội dung?
- [ ] Nút "Chạy thử toàn bộ" chạy hết 3 chế độ rồi dừng ở chế độ Giám sát?
- [ ] Legend đủ 3 loại đường? Số nguồn ghi ở chân slide?
- [ ] Mở bằng Chrome test ở 1280×720 và 1920×1080: không tràn chữ, không chồng lấn, không che node?
