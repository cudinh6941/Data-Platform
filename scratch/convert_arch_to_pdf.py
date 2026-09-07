import os
import re
import subprocess

def md_to_html(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_md = f.read()

    lines = raw_md.split('\n')
    html_body = []
    in_code = False
    code_type = ''
    code_buf = []
    in_table = False
    table_buf = []

    def format_inline(text):
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
        return text

    def process_table(t_lines):
        if not t_lines:
            return ''
        h = t_lines[0].strip().strip('|').split('|')
        rows = t_lines[2:] if len(t_lines) > 2 and '---' in t_lines[1] else t_lines[1:]
        res = ['<div class="table-wrap"><table><thead><tr>']
        for c in h:
            res.append(f'<th>{format_inline(c.strip())}</th>')
        res.append('</tr></thead><tbody>')
        for r in rows:
            cells = r.strip().strip('|').split('|')
            res.append('<tr>')
            for c in cells:
                res.append(f'<td>{format_inline(c.strip())}</td>')
            res.append('</tr>')
        res.append('</tbody></table></div>')
        return ''.join(res)

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('```'):
            if not in_code:
                in_code = True
                code_type = line.replace('```', '').strip()
                code_buf = []
            else:
                in_code = False
                code_str = '\n'.join(code_buf)
                if code_type == 'mermaid':
                    html_body.append(f'<div class="mermaid-box"><pre class="mermaid">\n{code_str}\n</pre></div>')
                else:
                    html_body.append(f'<pre class="code-block"><code>{code_str}</code></pre>')
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Table processing
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if not in_table:
                in_table = True
                table_buf = [line]
            else:
                table_buf.append(line)
            i += 1
            continue
        else:
            if in_table:
                in_table = False
                html_body.append(process_table(table_buf))
                table_buf = []

        # Blockquote / Callout
        if line.startswith('>'):
            bq_text = line[1:].strip()
            bq_text = re.sub(r'\[!(NOTE|TIP|IMPORTANT|WARNING)\]', r'<span class="badge badge-\1">[\1]</span>', bq_text)
            bq_text = format_inline(bq_text)
            html_body.append(f'<blockquote class="callout">{bq_text}</blockquote>')
            i += 1
            continue

        # Headings
        if line.startswith('# '):
            html_body.append(f'<h1 class="doc-title">{format_inline(line[2:].strip())}</h1>')
        elif line.startswith('## '):
            html_body.append(f'<h2 class="section-title">{format_inline(line[3:].strip())}</h2>')
        elif line.startswith('### '):
            html_body.append(f'<h3 class="sub-title">{format_inline(line[4:].strip())}</h3>')
        elif line.startswith('#### '):
            html_body.append(f'<h4 class="sub2-title">{format_inline(line[5:].strip())}</h4>')
        elif line.startswith('---'):
            html_body.append('<hr class="divider"/>')
        elif line.strip():
            txt = format_inline(line.strip())
            if txt.startswith('* '):
                html_body.append(f'<li class="bullet">{txt[2:]}</li>')
            elif re.match(r'^\d+\.\s', txt):
                clean_num = re.sub(r'^\d+\.\s', '', txt)
                html_body.append(f'<li class="numbered">{clean_num}</li>')
            else:
                html_body.append(f'<p class="para">{txt}</p>')
        i += 1

    if in_table:
        html_body.append(process_table(table_buf))

    html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Bản đặc tả kiến trúc Hybrid Data Platform - PTSC Quảng Ngãi</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
    mermaid.initialize({{
        startOnLoad: true,
        theme: 'neutral',
        themeVariables: {{
            primaryColor: '#e0f2fe',
            primaryTextColor: '#0369a1',
            primaryBorderColor: '#0284c7',
            lineColor: '#0284c7',
            fontFamily: 'Segoe UI, Arial, sans-serif',
            fontSize: '12px'
        }},
        flowchart: {{
            useMaxWidth: false,
            htmlLabels: true,
            curve: 'basis'
        }}
    }});
</script>
<style>
    @page {{
        size: A4 portrait;
        margin: 16mm 14mm 16mm 14mm;
    }}
    body {{
        font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
        font-size: 10.5pt;
        line-height: 1.5;
        color: #1e293b;
        background: #ffffff;
        margin: 0;
        padding: 0;
    }}
    .header-banner {{
        border-bottom: 2.5px solid #003366;
        padding-bottom: 6px;
        margin-bottom: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .corp-name {{
        font-size: 10.5pt;
        font-weight: bold;
        color: #003366;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .doc-meta {{
        font-size: 8.5pt;
        color: #64748b;
        text-align: right;
    }}
    h1.doc-title {{
        font-size: 17pt;
        font-weight: 800;
        color: #002855;
        margin: 0 0 6px 0;
        line-height: 1.25;
        text-transform: uppercase;
    }}
    h2.section-title {{
        font-size: 12.5pt;
        font-weight: 700;
        color: #004080;
        border-left: 4px solid #0284c7;
        padding-left: 8px;
        margin-top: 22px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }}
    h3.sub-title {{
        font-size: 11pt;
        font-weight: 700;
        color: #0f172a;
        margin-top: 14px;
        margin-bottom: 6px;
        page-break-after: avoid;
    }}
    h4.sub2-title {{
        font-size: 10pt;
        font-weight: 700;
        color: #334155;
        margin-top: 10px;
        margin-bottom: 4px;
        page-break-after: avoid;
    }}
    p.para {{
        margin: 5px 0;
        text-align: justify;
    }}
    li.bullet {{
        margin-left: 20px;
        margin-bottom: 3px;
        list-style-type: square;
    }}
    li.numbered {{
        margin-left: 20px;
        margin-bottom: 3px;
    }}
    hr.divider {{
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 14px 0;
    }}
    blockquote.callout {{
        background: #f8fafc;
        border-left: 3.5px solid #0284c7;
        margin: 10px 0;
        padding: 8px 12px;
        font-size: 9.5pt;
        color: #334155;
        border-radius: 0 4px 4px 0;
    }}
    .badge {{
        font-weight: bold;
        color: #0369a1;
    }}
    .table-wrap {{
        width: 100%;
        margin: 12px 0;
        page-break-inside: avoid;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 9pt;
    }}
    th {{
        background: #003366;
        color: #ffffff;
        font-weight: 600;
        padding: 7px 9px;
        text-align: left;
        border: 1px solid #002855;
    }}
    td {{
        padding: 6px 9px;
        border: 1px solid #cbd5e1;
        vertical-align: top;
    }}
    tr:nth-child(even) {{
        background: #f8fafc;
    }}
    .mermaid-box {{
        margin: 14px 0;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 10px;
        text-align: center;
        page-break-inside: avoid;
        overflow-x: auto;
    }}
    pre.mermaid {{
        margin: 0;
        display: inline-block;
    }}
    pre.code-block {{
        background: #0f172a;
        color: #f8fafc;
        padding: 10px;
        border-radius: 4px;
        font-family: Consolas, Monaco, monospace;
        font-size: 8.5pt;
        white-space: pre-wrap;
        page-break-inside: avoid;
    }}
    code {{
        background: #f1f5f9;
        color: #0f172a;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: Consolas, Monaco, monospace;
        font-size: 8.5pt;
    }}
</style>
</head>
<body>
<div class="header-banner">
    <div class="corp-name">TỔNG CÔNG TY CỔ PHẦN DỊCH VỤ DẦU KHÍ VIỆT NAM — PTSC QUẢNG NGÃI</div>
    <div class="doc-meta">TÀI LIỆU KỸ THUẬT NỘI BỘ<br>MÃ LƯU TRỮ: PTSC-QN-DP-ARCH-2026</div>
</div>
{''.join(html_body)}
</body>
</html>'''

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'HTML written successfully to {html_path}')

if __name__ == '__main__':
    md_file = 'kien_truc_data_platform_chi_tiet.md'
    html_file = 'scratch/rendered_arch.html'
    pdf_file = 'kien_truc_data_platform_chi_tiet.pdf'
    
    md_to_html(md_file, html_file)
    
    edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    html_abs = os.path.abspath(html_file)
    pdf_abs = os.path.abspath(pdf_file)
    
    cmd = [
        edge_path,
        '--headless',
        '--disable-gpu',
        '--virtual-time-budget=10000',
        '--run-all-compositor-stages-before-draw',
        f'--print-to-pdf={pdf_abs}',
        html_abs
    ]
    print('Starting Edge headless to convert HTML to PDF...')
    res = subprocess.run(cmd, capture_output=True)
    print('Return code:', res.returncode)
    if os.path.exists(pdf_abs):
        print(f'SUCCESS: PDF generated at {pdf_abs} (Size: {os.path.getsize(pdf_abs)} bytes)')
    else:
        print('ERROR: PDF was not generated.')
