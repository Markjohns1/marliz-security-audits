import os
import re
import markdown

# Setup paths
base_path = r'c:\Users\User\Downloads\marliz-security-audits\Field-Manual'
output_path = r'c:\Users\User\Downloads\marliz-security-audits\THE_MARLIZ_INTEL_FIELD_MANUAL_OFFICIAL_BOOK.html'

parts = [
    "Part-1-Vibe-Coding",
    "Part-2-Offensive-Security",
    "Part-3-Defensive-Security",
    "Part-4-Incident-Response",
    "Part-5-Business-of-Security",
    "Part-6-Tools-of-the-Trade"
]

# Updated HTML Template with Centering for Screen
html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>THE MARLIZ INTEL FIELD MANUAL - OFFICIAL EDITION</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@900&family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing: border-box; }
        
        @page { 
            size: A4; 
            margin: 0; 
        }

        body { 
            background: #2c2c2e; /* Darker background for monitor viewing */
            font-family: 'IBM Plex Sans', sans-serif; 
            color: #1a1a1a; 
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 0;
        }
        
        /* PAGE SYSTEM - LOCKED TO A4 DIMENSIONS */
        .page { 
            width: 210mm; 
            min-height: 297mm; 
            position: relative; 
            background: white; 
            padding: 35mm 25mm 30mm 35mm; /* 35mm Gutter for binding */
            margin-bottom: 40px; /* Space between pages in browser */
            box-shadow: 0 20px 50px rgba(0,0,0,0.5); /* Shadow for premium feel */
            overflow: hidden; 
        }
        
        @media print {
            body { background: white; padding: 0; }
            .page { margin: 0; box-shadow: none; page-break-after: always; }
        }

        /* Publication Header */
        .page::before { 
            content: "MARLIZ INTEL // FIELD MANUAL // SEC_OPS_V1"; 
            position: absolute; top: 15mm; right: 25mm; 
            font-family: 'JetBrains Mono', monospace; 
            font-size: 8pt; color: #bbb; 
        }

        /* --- FRONT COVER (Native HTML) --- */
        .external-cover { 
            background: linear-gradient(135deg, #0a0a0f 0%, #1a1520 100%); 
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        
        /* --- TYPOGRAPHY --- */
        h1 { font-family: 'Montserrat', sans-serif; font-size: 38pt; font-weight: 900; line-height: 1; border-bottom: 12px solid #FF5722; padding-bottom: 20px; margin-bottom: 50px; text-transform: uppercase; }
        h2 { font-family: 'Montserrat', sans-serif; font-size: 24pt; color: #FF5722; text-transform: uppercase; margin-top: 60px; margin-bottom: 25px; border-left: 8px solid #FF5722; padding-left: 20px; }
        h3 { font-family: 'Montserrat', sans-serif; font-size: 18pt; color: #333; margin-top: 40px; margin-bottom: 20px; }
        p { line-height: 1.85; text-align: justify; margin-bottom: 20px; font-size: 11pt; }
        
        .drop-cap p:first-of-type::first-letter {
            float: left;
            font-family: 'Montserrat', sans-serif;
            font-size: 5.5em;
            line-height: 0.8;
            padding: 10px 15px 0 0;
            color: #FF5722;
            font-weight: 900;
        }

        /* --- CODE BLOCKS --- */
        pre {
            background: #0d0d12 !important;
            color: #00FF41 !important;
            padding: 25px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 10pt;
            border-left: 10px solid #FF5722;
            margin: 30px 0;
            white-space: pre-wrap;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            page-break-inside: avoid;
        }
        code { font-family: 'JetBrains Mono', monospace; background: #f0f3f6; color: #e83e8c; padding: 2px 5px; border-radius: 3px; }
        pre code { background: none; color: inherit; padding: 0; }

        /* --- TOC --- */
        .toc-list { list-style: none; padding: 0; }
        .toc-item { 
            display: flex; justify-content: space-between; align-items: baseline; 
            margin-bottom: 15px; font-family: 'Montserrat'; font-weight: 700; text-transform: uppercase; 
            font-size: 1.2em;
        }
        .toc-item::after { content: " ...................................................................................................................."; color: #ccc; flex-grow: 1; margin: 0 10px; overflow: hidden; }
    </style>
</head>
<body>

    <!-- PAGE 1: FRONT COVER -->
    <div class="page external-cover">
        <div style="font-family:'JetBrains Mono'; color:#00C2FF; letter-spacing:10px; margin-bottom:20px;">THE</div>
        <h1 style="border:none; color:white; font-size:75pt; font-family:'Orbitron'; line-height:0.85;">MARLIZ<br>INTEL</h1>
        <div style="background:#FF5722; color:#000; padding:15px 50px; font-size:28pt; font-weight:900; margin-top:20px; letter-spacing:4px;">FIELD MANUAL</div>
        <div style="margin-top:120px; color:#00C2FF; font-size:18pt; font-weight:700; border-left:4px solid #FF5722; padding-left:20px;">PRACTICAL CYBERSECURITY FROM<br>THE KENYAN DIGITAL FRONTLINES</div>
    </div>

    <!-- PAGE 2: TABLE OF CONTENTS -->
    <div class="page">
        <h1>TABLE OF CONTENTS</h1>
        <div class="toc-list">
"""

html_end = """
    <!-- PAGE: BACK COVER -->
    <div class="page" style="background:#050505; color:white; display:flex; flex-direction:column; justify-content:center; padding:80px;">
        <div style="border-left:12px solid #FF5722; padding-left:30px;">
            <h1 style="border:none; color:white; font-size:45pt; line-height:1.1;">"THE FRONTEND IS A LION.<br>THE BACKEND IS A LAMB."</h1>
        </div>
        <div style="margin-top:80px; font-family:'JetBrains Mono'; color:#666; font-size:10pt;">MARLIZINTEL.COM // NAIROBI INTELLIGENCE BUREAU // 2026</div>
    </div>
</body>
</html>
"""

# START CONVERSION
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_start)
    
    # Generate TOC Entries
    for part in parts:
        name = part.replace('-', ' ').upper()
        f.write(f'<div class="toc-item"><span>{name}</span></div>')
    f.write('</div></div>')

    # Process Chapters
    for part in parts:
        f.write(f'<div class="page"><h1 style="margin-top:100px;">{part.replace("-", " ").upper()}</h1></div>')
        part_dir = os.path.join(base_path, part)
        
        chapters = sorted([c for c in os.listdir(part_dir) if c.endswith('.md')])
        for chapter in chapters:
            with open(os.path.join(part_dir, chapter), 'r', encoding='utf-8') as cf:
                md_text = cf.read()
                # Use real markdown to html library
                inner_html = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])
                f.write(f'<div class="page"><div class="drop-cap">{inner_html}</div></div>')

    f.write(html_end)

print("SUCCESS: Centered Publication Manual Generated.")
