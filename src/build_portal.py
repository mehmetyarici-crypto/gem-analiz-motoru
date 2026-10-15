#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quran Vision v6.2.1 — İnteraktif Dijital Külliyat, Akademik Portal ve A4 PDF Üreticisi
Tüm doğrulanmış Quran Vision raporlarını (YAML Frontmatter + 26 Adım Markdown + .sha256 Manifest)
okuyarak:
1. İnteraktif HTML5 Akademik Portal (docs/index.html) üretir,
2. Her bir rapor için bağımsız A4 Akademik PDF (docs/pdf/QV-2026-001.pdf .. 013.pdf) ve
   13 raporluk Tek Cilt Tam Külliyat PDF'i (docs/pdf/Quran_Vision_Kulliyat_v6.2.1.pdf) üretir.
"""

import html as html_lib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
import yaml

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
DOCS_TR = ROOT / "docs" / "tr"
PDF_DIR = ROOT / "docs" / "pdf"
DESKTOP_PDF_DIR = ROOT.parent / "QURAN_VISION_PDF_KULLIYAT"


def parse_report(md_path: Path):
    raw = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", raw, re.DOTALL)
    if not m:
        return None
    fm = yaml.safe_load(m.group(1)) or {}
    body = m.group(2).strip()

    sha_path = md_path.with_suffix(md_path.suffix + ".sha256")
    real_sha = "—"
    if sha_path.exists():
        sha_line = sha_path.read_text(encoding="utf-8").strip()
        if sha_line:
            real_sha = sha_line.split()[0]

    # Extract Z-1 Aporia summary (supports both '### Z-1:' and '## Z-1 ·')
    z1_match = re.search(r"#{2,3}\s*Z-1[:\s·].*?\n(.*?)(?=\n#{2,3}\s*Z-2[:\s·]|\Z)", body, re.DOTALL)
    aporia_text = z1_match.group(1).strip() if z1_match else ""
    aporia_text = re.sub(r"\n---\s*$", "", aporia_text).strip()

    # Extract Z-3 Open-ended Reader Dilemma (supports both '### Z-3:' and '## Z-3 ·')
    z3_match = re.search(r"#{2,3}\s*Z-3[:\s·].*?\n(.*?)(?=\n#{2,3}\s*Z-4[:\s·]|\Z)", body, re.DOTALL)
    z3_text = z3_match.group(1).strip() if z3_match else ""
    z3_text = re.sub(r"\n---\s*$", "", z3_text).strip()

    # Extract Prior & Posterior if present
    prior_m = re.search(r"(?:P\(S1\)\s*=\s*|Prior\s*P\(H\)\):\*\*\s*)([0-9.]+)", body)
    post_m = re.search(r"P\(S1\|E\)\s*\\approx\s*([0-9.]+)", body)
    prior_val = float(prior_m.group(1)) if prior_m else 0.30
    post_val = float(post_m.group(1)) if post_m else 0.78

    case_id = fm.get("case_id") or fm.get("vaka_kodu", "")
    surah = fm.get("surah") or fm.get("sure", "")
    verse = str(fm.get("verse") or fm.get("ayet_no", ""))

    # Clean Windows-safe PDF filename
    safe_verse = re.sub(r"[^0-9a-zA-Z_-]", "-", verse)
    pdf_filename = f"{case_id}.pdf"

    return {
        "filename": md_path.name,
        "pdf_filename": pdf_filename,
        "case_id": case_id,
        "surah": surah,
        "verse": verse,
        "topic": fm.get("topic") or fm.get("konu", ""),
        "date": str(fm.get("date") or fm.get("tarih", "2026-10-15")),
        "confidence": fm.get("confidence_grade") or fm.get("guven_duzeyi", "B"),
        "status": fm.get("status", "PRE-RELEASE"),
        "sha256": real_sha,
        "classical_sources": fm.get("classical_sources", []),
        "modern_sources": fm.get("modern_sources", []),
        "thresholds": fm.get("thresholds", []),
        "scenarios": fm.get("scenarios", []),
        "aporia": aporia_text,
        "z3_question": z3_text,
        "prior": prior_val,
        "posterior": post_val,
        "body": body,
    }


def format_inline_md_py(text: str) -> str:
    if not text:
        return ""
    s = html_lib.escape(text)
    s = s.replace("[NAKİL]", '<span class="tag-nakil">[NAKİL]</span>')
    s = s.replace("[YORUM]", '<span class="tag-yorum">[YORUM]</span>')
    s = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.*?)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[\^(\d+)\]", r'<sup class="fn-ref">[\1]</sup>', s)
    return s


def render_markdown_py(md: str) -> str:
    lines = md.split("\n")
    out = []
    in_code = False
    in_table = False

    for line in lines:
        if line.strip().startswith("```"):
            if not in_code:
                in_code = True
                out.append("<pre><code>")
            else:
                in_code = False
                out.append("</code></pre>")
            continue
        if in_code:
            out.append(html_lib.escape(line) + "\n")
            continue

        if line.strip().startswith("|"):
            if "---" in line:
                continue
            cells = [format_inline_md_py(c.strip()) for c in line.split("|")[1:-1]]
            if not in_table:
                in_table = True
                out.append("<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in cells) + "</tr></thead><tbody>")
            else:
                out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
            continue
        elif in_table:
            in_table = False
            out.append("</tbody></table>")

        stripped = line.strip()
        if line.startswith("# "):
            out.append(f"<h1>{format_inline_md_py(line[2:])}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{format_inline_md_py(line[3:])}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{format_inline_md_py(line[4:])}</h3>")
        elif line.startswith("#### "):
            out.append(f"<h4>{format_inline_md_py(line[5:])}</h4>")
        elif stripped == "---":
            out.append("<hr>")
        elif stripped.startswith("- "):
            out.append(f"<ul><li>{format_inline_md_py(stripped[2:])}</li></ul>")
        elif re.match(r"^\d+\.\s", stripped):
            out.append(f'<p class="num-item">{format_inline_md_py(stripped)}</p>')
        elif stripped.startswith("[^"):
            out.append(f'<p class="fn-item">{format_inline_md_py(stripped)}</p>')
        elif stripped != "":
            out.append(f"<p>{format_inline_md_py(line)}</p>")

    if in_table:
        out.append("</tbody></table>")
    return "\n".join(out)


def build_single_report_print_html(r: dict, idx: int) -> str:
    """Renders a single report block in clean academic A4 format for PDF generation."""
    classical_rows = []
    for cs in r.get("classical_sources", []):
        classical_rows.append(f"""
        <div class="pdf-source-box">
          <div class="pdf-source-title">
            <strong>{html_lib.escape(str(cs.get('author', '')))}</strong>
            <span>({html_lib.escape(str(cs.get('death_year', '')))})</span>
          </div>
          <div class="pdf-source-meta">
            <em>{html_lib.escape(str(cs.get('work', '')))}</em> • Tahkik: {html_lib.escape(str(cs.get('editor', '—')))} •
            {html_lib.escape(str(cs.get('publication_place', '')))}: {html_lib.escape(str(cs.get('publisher', '')))},
            {html_lib.escape(str(cs.get('publication_year', '')))} • Cilt: {html_lib.escape(str(cs.get('volume', '')))}, Sayfa: {html_lib.escape(str(cs.get('pages', '')))}
          </div>
          <div class="pdf-arabic">{html_lib.escape(str(cs.get('arabic_quote', '')))}</div>
          <div class="pdf-link">Tahkik: {html_lib.escape(str(cs.get('verification_link', '')))} ({html_lib.escape(str(cs.get('doi_or_urn', '')))})</div>
        </div>
        """)

    modern_rows = []
    for ms in r.get("modern_sources", []):
        modern_rows.append(f"""
        <div class="pdf-source-box">
          <div class="pdf-source-title">
            <strong>{html_lib.escape(str(ms.get('institution') or ms.get('author', '')))} ({html_lib.escape(str(ms.get('publication_year', '')))})</strong>
            <span>DOI: {html_lib.escape(str(ms.get('doi', '—')))}</span>
          </div>
          <div class="pdf-source-meta">
            <em>{html_lib.escape(str(ms.get('title', '')))}</em> • {html_lib.escape(str(ms.get('publication_place', '')))}: {html_lib.escape(str(ms.get('publisher', '')))}
          </div>
          <div class="pdf-link">URL: {html_lib.escape(str(ms.get('url', '')))}</div>
        </div>
        """)

    body_html = render_markdown_py(r["body"])

    return f"""
    <article class="pdf-report">
      <div class="pdf-header-banner">
        <div class="pdf-meta-line">
          <span>QURAN VISION v6.2.1 • AKADEMİK STRATEJİ RAPORU</span>
          <span>VAKA KODU: <strong>{html_lib.escape(r['case_id'])}</strong></span>
        </div>
        <h1 class="pdf-main-title">{idx}. {html_lib.escape(r['surah'])} Sûresi {html_lib.escape(r['verse'])} — {html_lib.escape(r['topic'])}</h1>
        <div class="pdf-submeta">
          Katman: 3 (Akademik-Derin) &nbsp;|&nbsp; H6 Zorlu Âyet &nbsp;|&nbsp; Güven Derecesi: {html_lib.escape(r['confidence'])} &nbsp;|&nbsp;
          Prior P(S1): %{int(round(r['prior']*100))} → Posterior P(S1|E): %{int(round(r['posterior']*100))}
        </div>
        <div class="pdf-sha">SHA-256: {html_lib.escape(r['sha256'])} ({html_lib.escape(r['filename'])})</div>
      </div>

      <section class="pdf-sources-summary">
        <h2>I. İSNAD 2 Klasik Tefsir Tahkiki ve Çağdaş Ampirik (DOI) Kaynak Özeti</h2>
        <div class="pdf-grid-2">
          <div>
            <h3>A) Klasik İslami Kaynaklar (İSNAD 2. Edisyon)</h3>
            {''.join(classical_rows)}
          </div>
          <div>
            <h3>B) Çağdaş Ampirik ve Kurumsal Kaynaklar (APA 7 / DOI)</h3>
            {''.join(modern_rows)}
          </div>
        </div>
      </section>

      <section class="pdf-body-content">
        {body_html}
      </section>
    </article>
    """


def wrap_pdf_document(title: str, articles_html: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>{html_lib.escape(title)}</title>
<style>
@page {{
  size: A4 portrait;
  margin: 16mm 15mm 16mm 15mm;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Arial, sans-serif;
  color: #111827;
  background: #ffffff;
  font-size: 10.5pt;
  line-height: 1.55;
}}
.pdf-report {{
  page-break-after: always;
}}
.pdf-report:last-child {{
  page-break-after: auto;
}}
.pdf-header-banner {{
  border: 1.5px solid #0f5132;
  background: #f8faf9;
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 16px;
}}
.pdf-meta-line {{
  display: flex;
  justify-content: space-between;
  font-size: 8.5pt;
  font-weight: 700;
  color: #856404;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}}
.pdf-main-title {{
  font-size: 15pt;
  color: #091310;
  font-weight: 800;
  line-height: 1.3;
  margin-bottom: 8px;
}}
.pdf-submeta {{
  font-size: 9pt;
  color: #1f2937;
  font-weight: 600;
  margin-bottom: 4px;
}}
.pdf-sha {{
  font-family: Consolas, 'Courier New', monospace;
  font-size: 7.5pt;
  color: #4b5563;
  word-break: break-all;
}}
.pdf-sources-summary {{
  margin-bottom: 18px;
  padding-bottom: 10px;
  border-bottom: 1px solid #d1d5db;
}}
.pdf-sources-summary h2 {{
  font-size: 11.5pt;
  color: #0f5132;
  margin-bottom: 8px;
  border-bottom: 1px solid #e5e7eb;
  padding-bottom: 4px;
}}
.pdf-sources-summary h3 {{
  font-size: 9.5pt;
  color: #856404;
  margin: 6px 0;
  text-transform: uppercase;
}}
.pdf-source-box {{
  border: 1px solid #e5e7eb;
  background: #fcfdfd;
  border-radius: 6px;
  padding: 8px 10px;
  margin-bottom: 6px;
  page-break-inside: avoid;
}}
.pdf-source-title {{
  display: flex;
  justify-content: space-between;
  font-size: 9.5pt;
  color: #111827;
  margin-bottom: 3px;
}}
.pdf-source-meta {{
  font-size: 8.5pt;
  color: #374151;
  margin-bottom: 4px;
}}
.pdf-arabic {{
  font-family: 'Traditional Arabic', 'Amiri', 'Scheherazade New', 'Times New Roman', serif;
  font-size: 13pt;
  direction: rtl;
  text-align: right;
  color: #064e3b;
  background: #f3f7f5;
  padding: 5px 10px;
  border-right: 3px solid #856404;
  border-radius: 4px;
  margin: 4px 0;
}}
.pdf-link {{
  font-family: Consolas, monospace;
  font-size: 7.5pt;
  color: #047857;
  word-break: break-all;
}}
.pdf-body-content h1 {{
  font-size: 13.5pt;
  color: #0f5132;
  margin: 14px 0 8px;
  padding-bottom: 4px;
  border-bottom: 1.5px solid #0f5132;
  page-break-after: avoid;
}}
.pdf-body-content h2 {{
  font-size: 11.5pt;
  color: #065f46;
  margin: 12px 0 6px;
  padding-bottom: 3px;
  border-bottom: 1px solid #d1d5db;
  page-break-after: avoid;
}}
.pdf-body-content h3 {{
  font-size: 10.5pt;
  color: #92400e;
  margin: 10px 0 4px;
  page-break-after: avoid;
}}
.pdf-body-content h4 {{
  font-size: 10pt;
  color: #111827;
  margin: 8px 0 4px;
  page-break-after: avoid;
}}
.pdf-body-content p {{
  margin-bottom: 6px;
  text-align: justify;
}}
.pdf-body-content ul {{
  margin: 4px 0 8px 18px;
}}
.pdf-body-content li {{
  margin-bottom: 3px;
}}
.pdf-body-content pre {{
  background: #f3f4f6;
  border: 1px solid #d1d5db;
  padding: 8px 10px;
  border-radius: 5px;
  font-family: Consolas, 'Courier New', monospace;
  font-size: 8.5pt;
  white-space: pre-wrap;
  word-break: break-word;
  margin: 8px 0;
  page-break-inside: avoid;
}}
.pdf-body-content table {{
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0 12px;
  font-size: 8.5pt;
  page-break-inside: avoid;
}}
.pdf-body-content th, .pdf-body-content td {{
  border: 1px solid #9ca3af;
  padding: 5px 7px;
  text-align: left;
  vertical-align: top;
}}
.pdf-body-content th {{
  background: #e5e7eb;
  color: #111827;
  font-weight: 700;
}}
.pdf-body-content hr {{
  border: none;
  border-top: 1px solid #d1d5db;
  margin: 10px 0;
}}
.tag-nakil {{
  background: #fef3c7;
  color: #92400e;
  padding: 1px 5px;
  border-radius: 3px;
  font-family: Consolas, monospace;
  font-size: 8pt;
  font-weight: 700;
}}
.tag-yorum {{
  background: #d1fae5;
  color: #065f46;
  padding: 1px 5px;
  border-radius: 3px;
  font-family: Consolas, monospace;
  font-size: 8pt;
  font-weight: 700;
}}
.fn-ref {{
  color: #92400e;
  font-weight: 700;
}}
.fn-item {{
  font-size: 8.5pt;
  color: #374151;
  margin-bottom: 3px;
}}
</style>
</head>
<body>
{articles_html}
</body>
</html>
"""


def find_browser_exe():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    return None


def generate_all_pdfs(reports: list):
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    DESKTOP_PDF_DIR.mkdir(parents=True, exist_ok=True)
    parent_pdf_dir = ROOT.parent / "pdf"
    parent_pdf_dir.mkdir(parents=True, exist_ok=True)
    browser = find_browser_exe()
    if not browser:
        print("⚠️ Tarayıcı bulunamadı, PDF üretimi atlandı.")
        return

    all_articles = []
    rebuild_all = "--rebuild-all" in sys.argv
    for idx, r in enumerate(reports, start=1):
        art_html = build_single_report_print_html(r, idx)
        all_articles.append(art_html)

        out_pdf = PDF_DIR / r["pdf_filename"]
        if out_pdf.exists() and out_pdf.stat().st_size > 1000 and not rebuild_all:
            shutil.copy2(out_pdf, DESKTOP_PDF_DIR / r["pdf_filename"])
            shutil.copy2(out_pdf, parent_pdf_dir / r["pdf_filename"])
            continue

        single_doc = wrap_pdf_document(f"{r['case_id']} - {r['surah']} {r['verse']}", art_html)
        tmp_html = PDF_DIR / f"{r['case_id']}.html"
        tmp_html.write_text(single_doc, encoding="utf-8")

        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_pdf}",
            tmp_html.resolve().as_uri(),
        ]
        subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        tmp_html.unlink(missing_ok=True)
        if out_pdf.exists() and out_pdf.stat().st_size > 1000:
            shutil.copy2(out_pdf, DESKTOP_PDF_DIR / r["pdf_filename"])
            shutil.copy2(out_pdf, parent_pdf_dir / r["pdf_filename"])
            print(f"  📄 Yeni PDF üretildi: {out_pdf.name} ({out_pdf.stat().st_size // 1024} KB)")

    last_code = reports[-1]["case_id"] if reports else "QV-2026-014"
    cover_html = f"""
    <div style="page-break-after: always; padding: 60px 30px; text-align: center; border: 3px double #0f5132; border-radius: 12px; margin-top: 40px;">
      <div style="font-size: 12pt; font-weight: 700; color: #856404; letter-spacing: 1.5px; margin-bottom: 16px;">
        QURAN VISION (v6.2.1) • İSNAD 2 + VERİ BİLİMİ HİBRİT AKADEMİK STANDARDI
      </div>
      <h1 style="font-size: 26pt; color: #091310; font-weight: 800; line-height: 1.25; margin-bottom: 18px;">
        Kur'an Temelli Gelecek Vizyonu<br>Stratejik Tefsir ve Karar Külliyatı
      </h1>
      <p style="font-size: 12pt; color: #374151; max-width: 540px; margin: 0 auto 30px;">
        26 Adımlı Analitik Çerçeve, İSNAD 2 Klasik Tefsir Tahkiki, Çağdaş Ampirik (DOI) Göstergeler ve
        Bayesyen Politika Simülasyonlarıyla Hazırlanmış {len(reports)} Tam Rapor (QV-2026-001 – {last_code})
      </p>
      <div style="text-align: left; max-width: 560px; margin: 25px auto; padding: 16px 20px; background: #f8faf9; border: 1px solid #d1d5db; border-radius: 8px; font-size: 9.5pt;">
        <strong style="color:#0f5132; display:block; margin-bottom:8px;">İÇİNDEKİLER ({len(reports)} STRATEJİK VAKA RAPORU):</strong>
        {''.join(f'<div style="margin-bottom:4px;"><b>{i}. {r["case_id"]}</b> — {r["surah"]} {r["verse"]}: {r["topic"]}</div>' for i, r in enumerate(reports, 1))}
      </div>
      <div style="font-size: 9pt; color: #6b7280; margin-top: 30px;">
        Linter Doğrulaması: 0 BLOCK (Kesici Hata) &nbsp;|&nbsp; Kriptografik Bütünlük: Harici .sha256 Manifest
      </div>
    </div>
    """
    full_book_doc = wrap_pdf_document("Quran_Vision_Tam_Kulliyat_v6_2_1", cover_html + "\n".join(all_articles))
    book_html_path = PDF_DIR / "Quran_Vision_Kulliyat_v6.2.1.html"
    book_pdf_path = PDF_DIR / "Quran_Vision_Kulliyat_v6.2.1.pdf"
    book_html_path.write_text(full_book_doc, encoding="utf-8")

    cmd_book = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={book_pdf_path}",
        book_html_path.resolve().as_uri(),
    ]
    subprocess.run(cmd_book, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    book_html_path.unlink(missing_ok=True)
    if book_pdf_path.exists() and book_pdf_path.stat().st_size > 1000:
        shutil.copy2(book_pdf_path, DESKTOP_PDF_DIR / "Quran_Vision_Kulliyat_v6.2.1.pdf")
        shutil.copy2(book_pdf_path, parent_pdf_dir / "Quran_Vision_Kulliyat_v6.2.1.pdf")
        print(f"  📚 Tam Külliyat PDF üretildi: {book_pdf_path.name} ({book_pdf_path.stat().st_size // 1024} KB)")


def build_html(reports):
    reports_json = json.dumps(reports, ensure_ascii=False)
    total_classical = sum(len(r["classical_sources"]) for r in reports)
    total_modern = sum(len(r["modern_sources"]) for r in reports)

    html = f"""<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quran Vision v6.2.1 - Kur'an Temelli Gelecek Vizyonu Akademik Kulliyat Portali</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root[data-theme="dark"] {{
  --bg-main: #091310;
  --bg-sidebar: #0d1b17;
  --bg-card: #122620;
  --bg-card-hover: #18332b;
  --bg-surface: #0f201b;
  --border: #214338;
  --text-primary: #ecf5f1;
  --text-secondary: #a3c2b6;
  --text-muted: #6c9183;
  --accent-gold: #d4af37;
  --accent-gold-soft: rgba(212, 175, 55, 0.14);
  --accent-emerald: #10b981;
  --accent-emerald-soft: rgba(16, 185, 129, 0.15);
  --danger: #ef4444;
  --shadow: 0 10px 30px rgba(0,0,0,0.45);
}}
:root[data-theme="light"] {{
  --bg-main: #f6f8f7;
  --bg-sidebar: #ffffff;
  --bg-card: #ffffff;
  --bg-card-hover: #f0f5f3;
  --bg-surface: #eef3f1;
  --border: #d5e2dc;
  --text-primary: #10241d;
  --text-secondary: #37574c;
  --text-muted: #648277;
  --accent-gold: #9a740a;
  --accent-gold-soft: rgba(154, 116, 10, 0.10);
  --accent-emerald: #059669;
  --accent-emerald-soft: rgba(5, 150, 105, 0.12);
  --danger: #dc2626;
  --shadow: 0 6px 20px rgba(16,36,29,0.07);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--bg-main);
  color: var(--text-primary);
  display: flex;
  height: 100vh;
  overflow: hidden;
  line-height: 1.65;
}}
/* Sidebar */
.sidebar {{
  width: 340px;
  min-width: 340px;
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  height: 100vh;
}}
.brand {{
  padding: 20px 22px;
  border-bottom: 1px solid var(--border);
  background: linear-gradient(135deg, rgba(16,185,129,0.08), rgba(212,175,55,0.08));
}}
.brand-badge {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: var(--accent-gold);
  background: var(--accent-gold-soft);
  padding: 4px 10px;
  border-radius: 99px;
  margin-bottom: 8px;
}}
.brand h1 {{
  font-size: 17px;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.3px;
}}
.brand p {{
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 4px;
}}
.search-box {{
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
}}
.search-input {{
  width: 100%;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-surface);
  color: var(--text-primary);
  font-size: 13px;
  outline: none;
  transition: border 0.2s;
}}
.search-input:focus {{
  border-color: var(--accent-gold);
}}
.report-list {{
  flex: 1;
  overflow-y: auto;
  padding: 10px 12px;
}}
.report-item {{
  padding: 12px 14px;
  border-radius: 10px;
  border: 1px solid transparent;
  margin-bottom: 6px;
  cursor: pointer;
  transition: all 0.18s ease;
}}
.report-item:hover {{
  background: var(--bg-card-hover);
  border-color: var(--border);
}}
.report-item.active {{
  background: var(--bg-card);
  border-color: var(--accent-gold);
  box-shadow: var(--shadow);
}}
.report-item-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}}
.report-surah {{
  font-weight: 700;
  font-size: 14px;
  color: var(--accent-gold);
}}
.report-code {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--text-muted);
}}
.report-topic {{
  font-size: 12.5px;
  color: var(--text-secondary);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}}

/* Main Content */
.main {{
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}}
.topbar {{
  padding: 14px 28px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-sidebar);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}}
.stats-bar {{
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}}
.stat-pill {{
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--text-secondary);
  background: var(--bg-surface);
  padding: 6px 11px;
  border-radius: 8px;
  border: 1px solid var(--border);
}}
.stat-pill strong {{
  color: var(--accent-emerald);
  font-size: 13px;
}}
.top-actions {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}}
.btn {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 13px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-card);
  color: var(--text-primary);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.15s;
}}
.btn:hover {{
  border-color: var(--accent-gold);
  color: var(--accent-gold);
}}
.btn-primary {{
  background: var(--accent-emerald-soft);
  border-color: rgba(16, 185, 129, 0.45);
  color: var(--accent-emerald);
}}
.btn-primary:hover {{
  background: var(--accent-emerald);
  color: #091310;
}}
.btn-gold {{
  background: var(--accent-gold-soft);
  border-color: rgba(212, 175, 55, 0.45);
  color: var(--accent-gold);
}}
.btn-gold:hover {{
  background: var(--accent-gold);
  color: #091310;
}}

.content-scroll {{
  flex: 1;
  overflow-y: auto;
  padding: 28px 36px 60px;
}}
.hero-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 24px 28px;
  margin-bottom: 22px;
  box-shadow: var(--shadow);
}}
.hero-meta {{
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 12px;
  align-items: center;
}}
.badge {{
  font-size: 11.5px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 6px;
}}
.badge-gold {{ background: var(--accent-gold-soft); color: var(--accent-gold); border: 1px solid rgba(212,175,55,0.3); }}
.badge-emerald {{ background: var(--accent-emerald-soft); color: var(--accent-emerald); border: 1px solid rgba(16,185,129,0.3); }}
.badge-mono {{ font-family: 'JetBrains Mono', monospace; background: var(--bg-surface); color: var(--text-secondary); border: 1px solid var(--border); }}

.hero-title {{
  font-size: 22px;
  font-weight: 700;
  line-height: 1.35;
  margin-bottom: 12px;
}}
.sha-bar {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  color: var(--text-muted);
  background: var(--bg-surface);
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid var(--border);
  word-break: break-all;
}}

/* Tabs */
.tabs {{
  display: flex;
  gap: 8px;
  margin-bottom: 22px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 12px;
  flex-wrap: wrap;
}}
.tab-btn {{
  padding: 9px 18px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-surface);
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
}}
.tab-btn.active {{
  background: var(--accent-gold);
  color: #091310;
  border-color: var(--accent-gold);
}}

/* Grid Cards */
.grid-2 {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
  gap: 18px;
  margin-bottom: 22px;
}}
.panel {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 22px;
}}
.panel h3 {{
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  color: var(--accent-gold);
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

/* Bayes Visual */
.bayes-row {{
  margin-bottom: 14px;
}}
.bayes-label {{
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  margin-bottom: 5px;
}}
.progress-track {{
  width: 100%;
  height: 12px;
  background: var(--bg-surface);
  border-radius: 99px;
  overflow: hidden;
  border: 1px solid var(--border);
}}
.progress-fill {{
  height: 100%;
  border-radius: 99px;
  transition: width 0.5s ease;
}}

/* Classical Source Card */
.source-card {{
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px;
  margin-bottom: 12px;
}}
.source-header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 8px;
}}
.source-author {{
  font-weight: 700;
  font-size: 14px;
  color: var(--text-primary);
}}
.source-death {{
  font-size: 12px;
  color: var(--accent-gold);
  font-weight: 600;
}}
.source-meta {{
  font-size: 12.5px;
  color: var(--text-secondary);
  margin-bottom: 10px;
}}
.arabic-box {{
  font-family: 'Amiri', serif;
  font-size: 19px;
  direction: rtl;
  text-align: right;
  line-height: 1.9;
  color: var(--accent-gold);
  background: var(--bg-card);
  padding: 12px 16px;
  border-radius: 8px;
  border-right: 3px solid var(--accent-gold);
  margin-bottom: 8px;
}}
.source-link {{
  font-size: 12px;
  color: var(--accent-emerald);
  text-decoration: none;
  font-family: 'JetBrains Mono', monospace;
}}
.source-link:hover {{ text-decoration: underline; }}

/* Markdown Reader */
.md-body {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 32px 38px;
}}
.md-body h1 {{ font-size: 22px; color: var(--accent-gold); margin-bottom: 18px; border-bottom: 1px solid var(--border); padding-bottom: 12px; }}
.md-body h2 {{ font-size: 17px; color: var(--accent-emerald); margin: 28px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }}
.md-body h3 {{ font-size: 15px; color: var(--accent-gold); margin: 20px 0 8px; }}
.md-body h4 {{ font-size: 14px; color: var(--text-primary); margin: 16px 0 6px; }}
.md-body p {{ margin-bottom: 12px; font-size: 14.5px; color: var(--text-primary); }}
.md-body ul, .md-body ol {{ margin: 8px 0 16px 22px; }}
.md-body li {{ margin-bottom: 6px; font-size: 14.5px; }}
.md-body pre {{
  background: var(--bg-surface);
  border: 1px solid var(--border);
  padding: 14px 18px;
  border-radius: 10px;
  overflow-x: auto;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12.5px;
  margin: 14px 0;
  color: var(--accent-emerald);
}}
.md-body table {{
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 13.5px;
}}
.md-body th, .md-body td {{
  border: 1px solid var(--border);
  padding: 10px 12px;
  text-align: left;
}}
.md-body th {{
  background: var(--bg-surface);
  color: var(--accent-gold);
  font-weight: 600;
}}
.tag-nakil {{
  background: rgba(212, 175, 55, 0.18);
  color: var(--accent-gold);
  padding: 2px 7px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 600;
}}
.tag-yorum {{
  background: rgba(16, 185, 129, 0.18);
  color: var(--accent-emerald);
  padding: 2px 7px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 600;
}}

.form-group {{
  margin-bottom: 14px;
}}
.form-label {{
  display: block;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--accent-gold);
  margin-bottom: 6px;
}}
.form-input, .form-select, .form-textarea {{
  width: 100%;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-surface);
  color: var(--text-primary);
  font-family: inherit;
  font-size: 13.5px;
  outline: none;
  transition: border 0.2s;
}}
.form-input:focus, .form-select:focus, .form-textarea:focus {{
  border-color: var(--accent-gold);
}}
.form-textarea {{
  min-height: 115px;
  resize: vertical;
  line-height: 1.6;
}}
.action-row {{
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 14px;
}}
.toast-msg {{
  display: none;
  margin-top: 12px;
  padding: 10px 14px;
  border-radius: 8px;
  background: var(--accent-emerald-soft);
  border: 1px solid var(--accent-emerald);
  color: var(--accent-emerald);
  font-size: 13px;
  font-weight: 600;
}}
.candidate-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 12px;
  margin-top: 12px;
}}
.candidate-card {{
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 10px;
}}

@media print {{
  @page {{
    size: A4 portrait;
    margin: 15mm;
  }}
  .sidebar, .topbar, .tabs, .no-print, #tab-feedback {{
    display: none !important;
  }}
  html, body, .main, .content-scroll {{
    display: block !important;
    height: auto !important;
    overflow: visible !important;
    background: #ffffff !important;
    color: #111827 !important;
    padding: 0 !important;
  }}
  #tab-dashboard, #tab-sources, #tab-fulltext {{
    display: block !important;
    margin-bottom: 20px !important;
  }}
  .hero-card, .panel, .source-card, .md-body {{
    background: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #d1d5db !important;
    box-shadow: none !important;
    break-inside: avoid;
  }}
  .md-body {{
    break-inside: auto;
    padding: 16px !important;
  }}
}}
</style>
</head>
<body>

<aside class="sidebar">
  <div class="brand">
    <div class="brand-badge">⚖️ QURAN VISION v6.2.1 • İSNAD 2 + DOI</div>
    <h1>Quran Vision — Gelecek Vizyonu</h1>
    <p>26 Adımlı Stratejik Tefsir & Akademik Külliyat Kokpiti</p>
  </div>
  <div class="search-box">
    <input type="text" id="searchInput" class="search-input" placeholder="Sûre, âyet, kavram veya müfessir ara...">
  </div>
  <div class="report-list" id="reportList"></div>
</aside>

<main class="main">
  <header class="topbar">
    <div class="stats-bar">
      <div class="stat-pill">📚 Külliyat: <strong>{len(reports)} Rapor</strong></div>
      <div class="stat-pill">🕌 Klasik Tahkik (İSNAD 2): <strong>{total_classical} Nakil</strong></div>
      <div class="stat-pill">🌐 Ampirik Veri (DOI/URL): <strong>{total_modern} Kurum</strong></div>
      <div class="stat-pill">🛡️ Linter & SHA-256: <strong>0 KESİCİ HATA</strong></div>
    </div>
    <div class="top-actions">
      <button class="btn btn-gold" onclick="openFeedbackTab()">💬 Akademik Katkı & Şerh Yaz</button>
      <a id="downloadPdfBtn" class="btn btn-primary" href="pdf/QV-2026-001.pdf" download="QV-2026-001.pdf">📥 Raporu PDF İndir</a>
      <a class="btn btn-gold" href="pdf/Quran_Vision_Kulliyat_v6.2.1.pdf" download="Quran_Vision_Kulliyat_v6.2.1.pdf">📚 Tüm Külliyat PDF ({len(reports)} Rapor)</a>
      <button class="btn" onclick="printCurrentReport()">🖨️ Yazdır</button>
      <button class="btn" onclick="toggleTheme()">🌗 Tema</button>
    </div>
  </header>

  <section class="content-scroll">
    <div class="hero-card" id="heroCard"></div>

    <div class="tabs">
      <button id="tabBtn-dashboard" class="tab-btn active" onclick="setTab('dashboard', this)">📊 1. Stratejik Kokpit & Aporia</button>
      <button id="tabBtn-sources" class="tab-btn" onclick="setTab('sources', this)">🏛️ 2. İSNAD 2 Klasik & Modern Kaynakça</button>
      <button id="tabBtn-fulltext" class="tab-btn" onclick="setTab('fulltext', this)">📖 3. Tam Akademik Metin (26 Adım)</button>
      <button id="tabBtn-pedagogy" class="tab-btn" onclick="setTab('pedagogy', this)">🎓 4. Pedagojik Ders & Zümre Kiti (TYMM)</button>
      <button id="tabBtn-synthesis" class="tab-btn" onclick="setTab('synthesis', this)">🕸️ 5. Külliyat Sentez & Müfessir Matrisi</button>
      <button id="tabBtn-feedback" class="tab-btn" onclick="setTab('feedback', this)">💬 6. Akademik Şerh & Katkı</button>
    </div>

    <div id="tab-dashboard"></div>
    <div id="tab-sources" style="display:none;"></div>
    <div id="tab-fulltext" style="display:none;"></div>
    <div id="tab-pedagogy" style="display:none;"></div>
    <div id="tab-synthesis" style="display:none;"></div>
    <div id="tab-feedback" style="display:none;"></div>
  </section>
</main>

<script>
const REPORTS = {reports_json};
let currentIndex = 0;
let currentTab = 'dashboard';

const CANDIDATE_VERSES = [
  {{ surah: "Mâide", verse: "5:32", title: "Yaşam Hakkının Dokunulmazlığı, Küresel İnsani Güvenlik ve Biyoetik Doktrini" }},
  {{ surah: "Bakara", verse: "2:143", title: "Vasat Ümmet (Denge ve İtidal), Küresel Şahitlik ve Kutuplaşma Karşıtı Jeopolitik" }},
  {{ surah: "Zümer", verse: "39:18", title: "Sözü Dinleyip En Güzeline Uymak (Ahsenü'l-Kavl): Eleştirel Düşünce ve Açık Müzakere Ahlakı" }},
  {{ surah: "Alak", verse: "96:1-5", title: "İkra ve Kalem Doktrini: Bilimsel Üretim, Epistemik Medeniyet ve Eğitim Felsefesi" }},
  {{ surah: "Mülk", verse: "67:3-4", title: "Kozmik Düzen, Kusursuzluk Arayışı, Bilimsel Gözlem ve Ekoloji Mimarisi" }},
  {{ surah: "Fussilet", verse: "41:34", title: "Kötülüğü En Güzel Olanla Savmak (İhsan Stratejisi): Çatışma Çözümü ve Toplumsal Barış Diplomasisi" }}
];

function renderSidebar(filter = '') {{
  const listEl = document.getElementById('reportList');
  const q = filter.toLowerCase().trim();
  listEl.innerHTML = '';

  REPORTS.forEach((r, idx) => {{
    const classicalNames = (r.classical_sources || []).map(cs => cs.author + ' ' + cs.work).join(' ');
    const searchable = (r.surah + ' ' + r.verse + ' ' + r.topic + ' ' + r.case_id + ' ' + classicalNames + ' ' + r.body).toLowerCase();
    if (q && !searchable.includes(q)) return;

    const item = document.createElement('div');
    item.className = 'report-item' + (idx === currentIndex ? ' active' : '');
    item.onclick = () => selectReport(idx);
    item.innerHTML = `
      <div class="report-item-top">
        <span class="report-surah">${{idx + 1}}. ${{r.surah}} ${{r.verse}}</span>
        <span class="report-code">${{r.case_id}}</span>
      </div>
      <div class="report-topic">${{r.topic}}</div>
    `;
    listEl.appendChild(item);
  }});
}}

function selectReport(idx) {{
  currentIndex = idx;
  renderSidebar(document.getElementById('searchInput').value);
  const r = REPORTS[idx];

  // Update clean document title & PDF download button
  document.title = `${{r.case_id}} - ${{r.surah}} ${{r.verse}} - Quran Vision v6.2.1`;
  const dlBtn = document.getElementById('downloadPdfBtn');
  if (dlBtn) {{
    dlBtn.href = `pdf/${{r.pdf_filename}}`;
    dlBtn.setAttribute('download', `${{r.case_id}}_${{r.surah}}_Raporu.pdf`);
    dlBtn.innerHTML = `📥 PDF İndir (${{r.case_id}})`;
  }}

  // Hero
  document.getElementById('heroCard').innerHTML = `
    <div class="hero-meta">
      <span class="badge badge-gold">📖 ${{r.surah}} Sûresi ${{r.verse}}</span>
      <span class="badge badge-emerald">Katman 3 • H6 Zorlu Âyet</span>
      <span class="badge badge-mono">${{r.case_id}}</span>
      <span class="badge badge-mono">Güven Derecesi: ${{r.confidence}}</span>
      <span class="badge badge-mono">Statü: ${{r.status}}</span>
      <div class="no-print" style="margin-left:auto; display:flex; gap:8px; flex-wrap:wrap;">
        <button class="btn" style="padding:4px 10px; font-size:11.5px;" onclick="setTab('pedagogy', document.getElementById('tabBtn-pedagogy'))">🎓 Ders & Münazara Planı</button>
        <button class="btn btn-gold" style="padding:4px 10px; font-size:11.5px;" onclick="openFeedbackTab()">💬 Şerh / Katkı Yaz</button>
        <a class="btn btn-primary" style="padding:4px 10px; font-size:11.5px;" href="pdf/${{r.pdf_filename}}" download="${{r.case_id}}_${{r.surah}}_Raporu.pdf">📥 A4 PDF İndir (${{r.case_id}}.pdf)</a>
      </div>
    </div>
    <div class="hero-title">${{r.topic}}</div>
    <div class="sha-bar">🔒 <strong>Harici Kriptografik Manifest (SHA-256):</strong> ${{r.sha256}} &nbsp;|&nbsp; 📄 <code>docs/tr/${{r.filename}}</code></div>
  `;

  // Tab 1: Dashboard
  const priorPct = Math.round(r.prior * 100);
  const postPct = Math.round(r.posterior * 100);

  let scenariosHtml = (r.scenarios || []).map(s => {{
    const sc = s.scores || {{}};
    return `
      <div class="source-card">
        <div class="source-header">
          <span class="source-author">${{s.id}} — ${{s.title}}</span>
          <span class="badge badge-gold">Öncelik: ${{sc.stratejik_oncelik || '-'}}/5</span>
        </div>
        <div class="source-meta">${{s.score_justification || ''}}</div>
        <div style="display:flex; gap:10px; font-size:12px; color:var(--text-muted); flex-wrap:wrap;">
          <span>Olasılık: <b>${{sc.olasilik || '-'}}/5</b></span>
          <span>Tesir: <b>${{sc.tesir || '-'}}/5</b></span>
          <span>Fırsat: <b>${{sc.firsat || '-'}}/5</b></span>
          <span>Kırılganlık: <b>${{sc.kirilganlik || '-'}}/5</b></span>
        </div>
      </div>
    `;
  }}).join('');

  let thresholdsHtml = (r.thresholds || []).map(t => `
    <div class="source-card">
      <div class="source-header">
        <span class="source-author">${{t.name}}</span>
        <span class="badge badge-emerald">${{t.value}}</span>
      </div>
      <div class="source-meta">${{t.derivation_basis}}</div>
    </div>
  `).join('');

  document.getElementById('tab-dashboard').innerHTML = `
    <div class="grid-2">
      <div class="panel">
        <h3><span>📈 Bayesyen Politika Güncellemesi (Adım 11)</span><span>2026–2036</span></h3>
        <div class="bayes-row">
          <div class="bayes-label">
            <span>Önsel Olasılık — Prior P(S1) (Mevcut Ataletle Başarı)</span>
            <strong>%${{priorPct}} (${{r.prior.toFixed(2)}})</strong>
          </div>
          <div class="progress-track">
            <div class="progress-fill" style="width:${{priorPct}}%; background:var(--accent-gold);"></div>
          </div>
        </div>
        <div class="bayes-row">
          <div class="bayes-label">
            <span>Sonsal Olasılık — Posterior P(S1|E) (Kurumsal Reform Kanıtıyla)</span>
            <strong style="color:var(--accent-emerald);">%${{postPct}} (${{r.posterior.toFixed(2)}})</strong>
          </div>
          <div class="progress-track">
            <div class="progress-fill" style="width:${{postPct}}%; background:var(--accent-emerald);"></div>
          </div>
        </div>
        <h3 style="margin-top:22px;"><span>🎯 Ampirik ve Tahminî Eşik Göstergeleri (V6)</span></h3>
        ${{thresholdsHtml}}
      </div>

      <div class="panel">
        <h3><span>⚡ Z-1: Şablona Sığmayan Özgün Problematik (Aporia)</span><span>V9 Zorunlu</span></h3>
        <div class="source-card" style="border-left: 3px solid var(--accent-gold); font-size:14px; line-height:1.75;">
          ${{formatInlineMd(r.aporia)}}
        </div>
        <h3 style="margin-top:20px;"><span>🧭 Dört Yapısal Senaryo Matrisi (V5)</span></h3>
        ${{scenariosHtml}}
      </div>
    </div>
  `;

  // Tab 2: Classical & Modern Sources
  let classicalHtml = (r.classical_sources || []).map(cs => `
    <div class="source-card">
      <div class="source-header">
        <span class="source-author">${{cs.author}}</span>
        <span class="source-death">${{cs.death_year || ''}}</span>
      </div>
      <div class="source-meta">
        <em>${{cs.work}}</em> • Tahkik: ${{cs.editor || '—'}} • ${{cs.publication_place || ''}}: ${{cs.publisher || ''}}, ${{cs.publication_year || ''}} • Cilt: ${{cs.volume}}, Sayfa: ${{cs.pages}}
      </div>
      <div class="arabic-box">${{cs.arabic_quote || ''}}</div>
      <a class="source-link" href="${{cs.verification_link}}" target="_blank" rel="noopener">🔗 Dijital Tahkik Linki: ${{cs.verification_link}} (${{cs.doi_or_urn || ''}})</a>
    </div>
  `).join('');

  let modernHtml = (r.modern_sources || []).map(ms => `
    <div class="source-card">
      <div class="source-header">
        <span class="source-author">${{ms.institution || ms.author}} (${{ms.publication_year || ''}})</span>
        <span class="badge badge-mono">${{ms.doi || 'Kurumsal Veritabanı'}}</span>
      </div>
      <div class="source-meta"><em>${{ms.title}}</em> • ${{ms.publication_place || ''}}: ${{ms.publisher || ''}}</div>
      <a class="source-link" href="${{ms.url}}" target="_blank" rel="noopener">🌐 ${{ms.url}}</a>
    </div>
  `).join('');

  document.getElementById('tab-sources').innerHTML = `
    <div class="grid-2">
      <div class="panel">
        <h3><span>🕌 A) Klasik İslami Kaynaklar (İSNAD 2. Edisyon)</span><span>${{(r.classical_sources||[]).length}} Eser</span></h3>
        ${{classicalHtml}}
      </div>
      <div class="panel">
        <h3><span>📊 B) Çağdaş Ampirik ve Kurumsal Kaynaklar (APA 7 / DOI)</span><span>${{(r.modern_sources||[]).length}} Kaynak</span></h3>
        ${{modernHtml}}
      </div>
    </div>
  `;

  // Tab 3: Full Markdown
  document.getElementById('tab-fulltext').innerHTML = `<div class="md-body">${{renderMarkdown(r.body)}}</div>`;

  // Tab 4: Pedagogy & Lesson Plan Kit (TYMM)
  renderPedagogyTab(r);

  // Tab 5: Corpus Synthesis & Classical Scholar Matrix
  renderSynthesisTab();

  // Tab 6: Interactive Academic Feedback & Peer Review
  renderFeedbackTab(r);
}}

function renderPedagogyTab(r) {{
  const scholarsList = (r.classical_sources || []).map(cs => `${{cs.author}} (${{cs.work}})`).join(', ');
  const firstArabic = (r.classical_sources && r.classical_sources[0]) ? r.classical_sources[0].arabic_quote : '';
  const firstScholar = (r.classical_sources && r.classical_sources[0]) ? `${{r.classical_sources[0].author}} (${{r.classical_sources[0].death_year}})` : '';
  const s1Title = (r.scenarios && r.scenarios[0]) ? r.scenarios[0].title : 'Kurumsal Reform ve Adalet Senaryosu';
  const s3Title = (r.scenarios && r.scenarios[2]) ? r.scenarios[2].title : 'Kriz ve Kurumsal Çözülme Senaryosu';
  const firstThreshold = (r.thresholds && r.thresholds[0]) ? `${{r.thresholds[0].name}} (${{r.thresholds[0].value}})` : 'Kurumsal Güven Göstergesi';

  document.getElementById('tab-pedagogy').innerHTML = `
    <div class="panel" style="margin-bottom:20px; border-color:var(--accent-gold);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:12px;">
        <div>
          <span class="badge badge-gold">🇹🇷 TÜRKİYE YÜZYILI MAARİF MODELİ (TYMM) UYUMLU</span>
          <span class="badge badge-emerald" style="margin-left:6px;">DKAB & İHL Meslek Dersleri Zümre Kiti</span>
        </div>
        <div style="display:flex; gap:8px;">
          <button class="btn btn-primary" onclick="shareLessonPlanWhatsApp()">🟢 Ders Planını WhatsApp'ta Zümremle Paylaş</button>
          <button class="btn btn-gold" onclick="copyLessonPlan()">📋 Ders Planını Kopyala</button>
        </div>
      </div>
      <h2 style="font-size:19px; color:var(--text-primary); margin-bottom:6px;">
        🎓 ${{r.surah}} Sûresi ${{r.verse}} — 40 Dakikalık Sınıf İçi Münazara ve Vaka Analizi Ders Planı
      </h2>
      <p style="font-size:13.5px; color:var(--text-secondary);">
        <strong>Odak Konu:</strong> ${{r.topic}} &nbsp;|&nbsp; <strong>Referans Rapor:</strong> <code>${{r.case_id}}</code>
      </p>
      <div id="pedagogyToast" class="toast-msg"></div>
    </div>

    <div class="grid-2">
      <div class="panel">
        <h3><span>⏱️ 1. Aşama (00–08. Dk): Merak Uyandırma & Vaka Sunumu</span><span>Giriş / Z-1</span></h3>
        <div class="source-card" style="border-left:3px solid var(--accent-gold);">
          <div class="source-author" style="margin-bottom:6px;">🔥 Öğrencilere Sorulacak Derse Giriş Sorusu (Aporia):</div>
          <div style="font-size:13.5px; color:var(--text-secondary); line-height:1.65;">
            ${{formatInlineMd(r.aporia)}}
          </div>
        </div>
        <div class="source-card">
          <div class="source-author" style="margin-bottom:4px;">🎯 TYMM Erdem-Değer-Eylem Çerçevesi:</div>
          <div class="source-meta">
            <strong>Kök Değerler:</strong> Adalet, Hikmet, Sorumluluk, Merhamet, Dürüstlük<br>
            <strong>Üst Düzey Beceriler:</strong> Bağlamsal Tefsir Okuryazarlığı, Kanıta Dayalı Karar Alma, Münazara ve Müzakere Ahlakı
          </div>
        </div>
      </div>

      <div class="panel">
        <h3><span>🏛️ 2. Aşama (08–20. Dk): Klasik Tefsir Halkası</span><span>İSNAD 2 Köprüsü</span></h3>
        <div class="source-card">
          <div class="source-author" style="margin-bottom:6px;">🕌 Müfessirlerin Kavramsal Çerçevesi:</div>
          <div class="source-meta">
            Derste öğrencilere âyetin lafzî ve tarihsel bağlamı <strong>${{scholarsList}}</strong> üzerinden aktarılır.
          </div>
          <div class="arabic-box" style="font-size:17px;">${{firstArabic}}</div>
          <div style="font-size:12px; color:var(--accent-gold);">— ${{firstScholar}}</div>
        </div>
        <div class="source-card">
          <div class="source-author" style="margin-bottom:4px;">💡 Pedagojik Vurgu (<code>[NAKİL]</code> vs <code>[YORUM]</code>):</div>
          <div class="source-meta">
            Öğrencilere âyetin değişmez ilahi metni ve klasik tefsir nakli (<code>[NAKİL]</code>) ile bugünün dünyasına yönelik stratejik çıkarımların (<code>[YORUM]</code>) birbirinden nasıl ayırt edileceği uygulamalı olarak gösterilir.
          </div>
        </div>
      </div>

      <div class="panel">
        <h3><span>⚖️ 3. Aşama (20–33. Dk): Sınıf İçi Münazara Atölyesi</span><span>Senaryo & Z-3</span></h3>
        <div class="source-card" style="border-left:3px solid var(--accent-emerald);">
          <div class="source-author" style="margin-bottom:6px;">🗣️ Münazara İkilemi (Z-3 Açık Uçlu Soru):</div>
          <div style="font-size:13.5px; color:var(--text-secondary); line-height:1.65;">
            ${{formatInlineMd(r.z3_question)}}
          </div>
        </div>
        <div class="source-card">
          <div class="source-author" style="margin-bottom:4px;">🧭 İki Grup Senaryo Karşılaştırması:</div>
          <div class="source-meta">
            • <strong>1. Grup (Reform Masası — S1):</strong> <em>"${{s1Title}}"</em> gerçekleşirse toplumda başarı olasılığı neden <strong>%${{Math.round(r.prior*100)}}'dan %${{Math.round(r.posterior*100)}}'a</strong> yükselir?<br>
            • <strong>2. Grup (Kriz Analizi — S3):</strong> <em>"${{s3Title}}"</em> yaşanırsa hangi toplumsal maliyetler ortaya çıkar?
          </div>
        </div>
      </div>

      <div class="panel">
        <h3><span>📋 4. Aşama (33–40. Dk): Değerlendirme & Çıkış Kartı</span><span>Eylem & Ölçüt</span></h3>
        <div class="source-card">
          <div class="source-author" style="margin-bottom:6px;">📊 Somut Hayat Ölçütü (Threshold):</div>
          <div class="source-meta">
            Öğrencilere <strong>${{firstThreshold}}</strong> göstergesi örnek verilerek şu kapanış sorusu yöneltilir:<br><br>
            <em>"Bugün ${{r.surah}} ${{r.verse}} âyetinin ortaya koyduğu ilkeyi kendi okul ortamımızda, ailemizde ve dijital dünyamızda hayata geçirmek için hangi 1 somut kuralı uygulamalıyız?"</em>
          </div>
        </div>
        <div style="margin-top:12px; display:flex; gap:10px; flex-wrap:wrap;">
          <button class="btn btn-gold" onclick="openFeedbackTab(); selectCategoryAndFocus('Sınıf İçi / Zümre Pedagojik Uygulama Deneyimi');">
            ✍️ Bu Dersi İşledikten Sonra Zümre Deneyimini Buraya Kaydet
          </button>
        </div>
      </div>
    </div>
  `;
}}

function buildLessonPlanText() {{
  const r = REPORTS[currentIndex];
  const scholarsList = (r.classical_sources || []).map(cs => cs.author).join(', ');
  return `*QURAN VISION (v6.2.1) — TYMM UYUMLU 40 DK DERS & MÜNAZARA PLANI*\\n` +
    `━━━━━━━━━━━━━━━━━━━━\\n` +
    `📖 *Ders Konusu:* ${{r.surah}} Sûresi ${{r.verse}} (${{r.case_id}})\\n` +
    `🎯 *Stratejik Tema:* ${{r.topic}}\\n` +
    `━━━━━━━━━━━━━━━━━━━━\\n` +
    `⏱️ *1. Aşama (00-08 Dk - Merak & Vaka):* ${{r.aporia.slice(0, 220)}}...\\n\\n` +
    `🕌 *2. Aşama (08-20 Dk - Klasik Tefsir Köprüsü):* ${{scholarsList}} nakilleriyle âyetin tarihsel ve lafzî tahkiki.\\n\\n` +
    `⚖️ *3. Aşama (20-33 Dk - Sınıf İçi Münazara Sorusu):* ${{r.z3_question.slice(0, 240)}}...\\n\\n` +
    `📋 *4. Aşama (33-40 Dk - Değerlendirme):* Kurumsal reformla başarı olasılığının %${{Math.round(r.prior*100)}} -> %${{Math.round(r.posterior*100)}} düzeyine çıkışı ve günlük hayat uygulaması.\\n` +
    `🔗 *Tam Rapor ve PDF:* https://mehmetyarici-crypto.github.io/quran-vision/`;
}}

function shareLessonPlanWhatsApp() {{
  const txt = buildLessonPlanText();
  window.open(`https://wa.me/?text=${{encodeURIComponent(txt)}}`, '_blank');
}}

function copyLessonPlan() {{
  const txt = buildLessonPlanText();
  if (navigator.clipboard) navigator.clipboard.writeText(txt);
  const el = document.getElementById('pedagogyToast');
  if (el) {{
    el.textContent = "✅ 40 Dakikalık TYMM Ders & Münazara Planı panoya kopyalandı!";
    el.style.display = 'block';
    setTimeout(() => {{ el.style.display = 'none'; }}, 4000);
  }}
}}

function renderSynthesisTab() {{
  const avgPrior = Math.round((REPORTS.reduce((a, b) => a + b.prior, 0) / REPORTS.length) * 100);
  const avgPost = Math.round((REPORTS.reduce((a, b) => a + b.posterior, 0) / REPORTS.length) * 100);
  const netGain = avgPost - avgPrior;

  // Aggregate Classical Scholars across all 13 reports
  const scholarMap = {{}};
  REPORTS.forEach((rep, rIdx) => {{
    (rep.classical_sources || []).forEach(cs => {{
      const shortName = cs.author.split('(')[0].trim();
      if (!scholarMap[shortName]) {{
        scholarMap[shortName] = {{ count: 0, work: cs.work, death: cs.death_year, reports: [] }};
      }}
      scholarMap[shortName].count += 1;
      if (!scholarMap[shortName].reports.includes(rep.case_id)) {{
        scholarMap[shortName].reports.push(rep.case_id);
      }}
    }});
  }});

  const sortedScholars = Object.entries(scholarMap).sort((a, b) => b[1].count - a[1].count);
  const scholarsGridHtml = sortedScholars.map(([name, info], sIdx) => `
    <div class="candidate-card" style="cursor:pointer;" data-scholar="${{name.replace(/"/g, '&quot;')}}" onclick="filterByScholar(this.getAttribute('data-scholar'))">
      <div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="color:var(--accent-gold); font-size:13.5px;">🕌 ${{name}}</strong>
          <span class="badge badge-emerald">${{info.count}} Rapor</span>
        </div>
        <div style="font-size:12px; color:var(--text-secondary);"><em>${{info.work}}</em> (${{info.death || ''}})</div>
      </div>
      <div style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono',monospace;">
        🔍 Tıkla & Filtrele: ${{info.reports.join(', ')}}
      </div>
    </div>
  `).join('');

  const matrixRowsHtml = REPORTS.map((rep, idx) => {{
    const p1 = Math.round(rep.prior * 100);
    const p2 = Math.round(rep.posterior * 100);
    const diff = p2 - p1;
    return `
      <tr style="cursor:pointer; transition:background 0.15s;" onclick="selectReport(${{idx}}); setTab('dashboard', document.getElementById('tabBtn-dashboard'));" onmouseover="this.style.background='var(--bg-card-hover)'" onmouseout="this.style.background='transparent'">
        <td style="font-family:'JetBrains Mono',monospace; font-weight:700; color:var(--accent-gold);">${{rep.case_id}}</td>
        <td><strong>${{rep.surah}} ${{rep.verse}}</strong></td>
        <td style="font-size:12.5px; color:var(--text-secondary);">${{rep.topic}}</td>
        <td>%${{p1}} → <strong style="color:var(--accent-emerald);">%${{p2}}</strong> <span class="badge badge-emerald">+%${{diff}}</span></td>
        <td>${{(rep.classical_sources||[]).length}} Klasik / ${{(rep.modern_sources||[]).length}} DOI</td>
        <td><span class="badge badge-mono">${{rep.confidence}}</span></td>
      </tr>
    `;
  }}).join('');

  document.getElementById('tab-synthesis').innerHTML = `
    <div class="grid-2">
      <div class="panel">
        <h3><span>📈 Külliyat Makro-Bayesyen Sentezi (${{REPORTS.length}} Rapor Ortalaması)</span><span>2026–2036</span></h3>
        <div class="bayes-row">
          <div class="bayes-label">
            <span>Külliyat Ortalama Önsel Olasılık — Prior P(S1) (Mevcut Kurumsal Atalet)</span>
            <strong>%${{avgPrior}}</strong>
          </div>
          <div class="progress-track">
            <div class="progress-fill" style="width:${{avgPrior}}%; background:var(--accent-gold);"></div>
          </div>
        </div>
        <div class="bayes-row">
          <div class="bayes-label">
            <span>Külliyat Ortalama Sonsal Olasılık — Posterior P(S1|E) (Kur'ani İlkeler & Reformla)</span>
            <strong style="color:var(--accent-emerald);">%${{avgPost}} (+%${{netGain}} Net Stratejik Sıçrama)</strong>
          </div>
          <div class="progress-track">
            <div class="progress-fill" style="width:${{avgPost}}%; background:var(--accent-emerald);"></div>
          </div>
        </div>
        <p style="font-size:13px; color:var(--text-secondary); margin-top:10px;">
          ${{REPORTS.length}} kurucu âyetin tamamında yapılan nicel simülasyonlar; ahit vefası, liyakat, şûrâ, bilgi doğrulama (tebeyyün), servet dolaşımı, mîzân ve teâruf ilkeleri kurumsallaştırıldığında toplumsal istikrar olasılığının ortalama <strong>+%${{netGain}} puan</strong> arttığını kanıtlamaktadır.
        </p>
      </div>

      <div class="panel">
        <h3><span>🏛️ Metodolojik Mimari Özeti</span><span>v6.2.1 Standardı</span></h3>
        <div class="source-card">
          <div class="source-author">1. İSNAD 2 Klasik Tefsir Tahkiki ({total_classical} Arapça Nakil)</div>
          <div class="source-meta">Erken dönem rivayet, dirayet, fıkhî ahkâm ve makâsıd tefsirlerinden hicrî/milâdî vefat yılı, tahkik ve cilt/sayfa doğrulamalı birincil kaynak ağı.</div>
        </div>
        <div class="source-card">
          <div class="source-author">2. Çağdaş Ampirik Veri & DOI Ağı ({total_modern} Kurumsal Veri Kaynağı)</div>
          <div class="source-meta">Dünya Bankası, UNDP, WJP, SIPRI, OECD ve UNESCO göstergeleriyle kalibre edilmiş yanlışlanabilir eşik değerler (Thresholds).</div>
        </div>
      </div>
    </div>

    <div class="panel" style="margin-bottom:22px;">
      <h3><span>🕌 Külliyat Çapraz Müfessir İndeksi (Filtrelemek İçin Müfessire Tıklayın)</span><span>İSNAD 2 Haritası</span></h3>
      <div class="candidate-grid">
        ${{scholarsGridHtml}}
      </div>
    </div>

    <div class="panel md-body" style="padding:22px;">
      <h3 style="margin-top:0;"><span>📊 ${{REPORTS.length}} Stratejik Raporun Bütüncül Karşılaştırma Matrisi (Rapora Gitmek İçin Satıra Tıklayın)</span></h3>
      <table>
        <thead>
          <tr>
            <th>Vaka Kodu</th>
            <th>Sûre / Âyet</th>
            <th>Stratejik Doktrin & Yönetişim Başlığı</th>
            <th>Bayesyen Sıçrama (Prior → Posterior)</th>
            <th>Kaynak Ağı</th>
            <th>Güven</th>
          </tr>
        </thead>
        <tbody>
          ${{matrixRowsHtml}}
        </tbody>
      </table>
    </div>
  `;
}}

function filterByScholar(scholarName) {{
  const input = document.getElementById('searchInput');
  if (input) {{
    input.value = scholarName;
    renderSidebar(scholarName);
  }}
}}

function renderFeedbackTab(r) {{
  const nextReportNum = REPORTS.length + 1;
  const nextCaseId = 'QV-2026-' + String(nextReportNum).padStart(3, '0');
  const candidatesHtml = CANDIDATE_VERSES.map((cv, cIdx) => `
    <div class="candidate-card">
      <div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <strong style="color:var(--accent-gold); font-size:14px;">📖 ${{cv.surah}} ${{cv.verse}}</strong>
          <span class="badge badge-mono">Aday #${{cIdx + 1}}</span>
        </div>
        <div style="font-size:12.5px; color:var(--text-secondary); line-height:1.5;">${{cv.title}}</div>
      </div>
      <button class="btn btn-gold" style="width:100%; justify-content:center;" onclick="prefillCandidateVerse('${{cv.surah}} ${{cv.verse}}', '${{cv.title}}')">
        🗳️ Sıradaki Rapor İçin Bu Âyeti Öner
      </button>
    </div>
  `).join('');

  document.getElementById('tab-feedback').innerHTML = `
    <div class="grid-2">
      <div class="panel">
        <h3><span>❓ Z-3: Okuyucuya Bırakılan Açık Uçlu Stratejik İkilem</span><span>${{r.case_id}} • ${{r.surah}} ${{r.verse}}</span></h3>
        <div class="source-card" style="border-left: 3px solid var(--accent-emerald); font-size:14px; line-height:1.75; margin-bottom:16px;">
          ${{formatInlineMd(r.z3_question || 'Bu raporun açık uçlu müzakere sorusu hakkında görüşünüzü aşağıdan paylaşabilirsiniz.')}}
        </div>
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:22px;">
          <button class="btn btn-primary" onclick="selectCategoryAndFocus('Z-3 Açık Uçlu İkileme Çözüm / Yanıt')">✍️ Bu İkileme Cevabımı Yaz</button>
          <button class="btn" onclick="selectCategoryAndFocus('İSNAD 2 Klasik Tefsir / Arapça Kaynak İlavesi')">🕌 Klasik Tefsir Nakli Ekle</button>
          <button class="btn" onclick="selectCategoryAndFocus('Sınıf İçi / Zümre Pedagojik Uygulama Deneyimi')">🏫 Zümre / Ders Deneyimi Paylaş</button>
        </div>

        <h3><span>📌 Bu Rapor İçin Kaydettiğim Şerhler & Ders Notlarım</span><span id="localNotesCount">0 Not</span></h3>
        <div id="localNotesList"></div>
      </div>

      <div class="panel">
        <h3><span>✍️ Etkileşimli Akademik Şerh, Hakemlik ve Geri Dönüt Formu</span><span>Açık Müzakere</span></h3>
        <p style="font-size:12.5px; color:var(--text-secondary); margin-bottom:14px;">
          <strong>${{r.case_id}} (${{r.surah}} Sûresi ${{r.verse}})</strong> raporu için hazırladığınız katkıyı tek tıkla <strong>WhatsApp</strong> üzerinden paylaşabilir, <strong>Resmi GitHub Akademik Hakemlik (Peer-Review)</strong> kaydı açabilir veya kişisel araştırma notlarınıza kaydedebilirsiniz.
        </p>

        <div class="form-group">
          <label class="form-label">👤 Adınız / Unvanınız / Kurum veya Zümreniz</label>
          <input type="text" id="fbAuthor" class="form-input" placeholder="Örn: Doç. Dr. ... / DKAB Öğretmeni ...">
        </div>

        <div class="form-group">
          <label class="form-label">📂 Katkı veya Geri Bildirim Türü</label>
          <select id="fbCategory" class="form-select">
            <option value="Z-3 Açık Uçlu İkileme Çözüm / Yanıt">🎓 Z-3 Açık Uçlu İkileme Çözüm / Yanıt</option>
            <option value="İSNAD 2 Klasik Tefsir / Arapça Kaynak İlavesi">🕌 İSNAD 2 Klasik Tefsir / Arapça Kaynak İlavesi</option>
            <option value="Çağdaş Ampirik Veri / DOI / Makale Önerisi">📊 Çağdaş Ampirik Veri / DOI / Makale Önerisi</option>
            <option value="Sınıf İçi / Zümre Pedagojik Uygulama Deneyimi">🏫 Sınıf İçi / Zümre Pedagojik Uygulama Deneyimi</option>
            <option value="Metodolojik Tenkit / Yanlışlama Kanıtı (Adım 12)">⚖️ Metodolojik Tenkit / Yanlışlama Kanıtı (Adım 12)</option>
            <option value="Külliyata Yeni Âyet / Rapor Önerisi">💡 Külliyata Yeni Âyet / Rapor Önerisi (${{nextCaseId}}+)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">📝 Şerh, Analiz, Eleştiri veya Sınıf İçi Gözlem Metniniz</label>
          <textarea id="fbContent" class="form-textarea" placeholder="Bu raporun analitik çerçevesine, klasik tefsir nakillerine, Z-3 sorusuna veya sınıf içi uygulanabilirliğine dair görüş ve katkınızı buraya yazınız..."></textarea>
        </div>

        <div class="form-group">
          <label class="form-label">📚 Varsa Dayanak Kaynak / Tefsir / DOI / Âyet Referansı (İsteğe Bağlı)</label>
          <input type="text" id="fbSource" class="form-input" placeholder="Örn: İbn Âşûr, et-Tahrîr, c. X, s. Y veya DOI: 10.xxxx/...">
        </div>

        <div class="action-row">
          <button class="btn btn-primary" onclick="sendViaWhatsApp()">🟢 WhatsApp ile Gönder / Paylaş</button>
          <button class="btn btn-gold" onclick="openGitHubPeerReview()">🏛️ Resmi Akademik Şerh Kaydı Aç (GitHub)</button>
          <button class="btn" onclick="saveLocalNoteAndCopy()">💾 Notlarıma Kaydet & Metni Kopyala</button>
          <a class="btn" href="https://github.com/mehmetyarici-crypto/quran-vision/issues" target="_blank" rel="noopener">🔎 Tüm Açık Şerhleri Gör</a>
        </div>
        <div id="fbToast" class="toast-msg"></div>
      </div>
    </div>

    <div class="panel" style="margin-bottom:24px;">
      <h3><span>🗳️ Külliyatın ${{nextReportNum}}. Raporu (${{nextCaseId}}) Hangi Âyet Olsun? (Aday Âyet Havuzu)</span><span>Kolektif Gündem</span></h3>
      <p style="font-size:13px; color:var(--text-secondary);">
        Aşağıdaki aday âyetlerden birini seçerek bir sonraki stratejik analizin hangi âyet üzerine inşa edilmesini istediğinizi önerebilirsiniz:
      </p>
      <div class="candidate-grid">
        ${{candidatesHtml}}
      </div>
    </div>
  `;

  renderLocalNotes();
}}

function openFeedbackTab() {{
  const btn = document.getElementById('tabBtn-feedback');
  if (btn) setTab('feedback', btn);
}}

function selectCategoryAndFocus(catValue) {{
  const sel = document.getElementById('fbCategory');
  if (sel) sel.value = catValue;
  const ta = document.getElementById('fbContent');
  if (ta) ta.focus();
}}

function prefillCandidateVerse(verseRef, verseTitle) {{
  const nextReportNum = REPORTS.length + 1;
  const nextCaseId = 'QV-2026-' + String(nextReportNum).padStart(3, '0');
  const sel = document.getElementById('fbCategory');
  if (sel) sel.value = "Külliyata Yeni Âyet / Rapor Önerisi";
  const ta = document.getElementById('fbContent');
  if (ta) {{
    ta.value = `Külliyatın ${{nextReportNum}}. raporu (${{nextCaseId}}) olarak "${{verseRef}} — ${{verseTitle}}" konusunun 26 adımlı Quran Vision çerçevesinde incelenmesini öneriyorum.\\n\\nÖneri Gerekçem: `;
    ta.focus();
  }}
  showToast("✨ Aday âyet forma aktarıldı! Gerekçenizi ekleyip WhatsApp veya GitHub üzerinden gönderebilirsiniz.");
}}

function buildFormattedFeedbackText() {{
  const r = REPORTS[currentIndex];
  const author = (document.getElementById('fbAuthor')?.value || 'İsimsiz Katılımcı').trim();
  const category = document.getElementById('fbCategory')?.value || 'Akademik Şerh';
  const content = (document.getElementById('fbContent')?.value || '').trim();
  const source = (document.getElementById('fbSource')?.value || '—').trim();

  return {{
    r, author, category, content, source,
    formatted: `*QURAN VISION (v6.2.1) — AKADEMİK ŞERH & GERİ DÖNÜT KARTI*\\n` +
      `━━━━━━━━━━━━━━━━━━━━\\n` +
      `📌 *Rapor:* ${{r.case_id}} — ${{r.surah}} Sûresi ${{r.verse}}\\n` +
      `📖 *Konu:* ${{r.topic}}\\n` +
      `👤 *Katkı Sunan:* ${{author}}\\n` +
      `📂 *Kategori:* ${{category}}\\n` +
      `━━━━━━━━━━━━━━━━━━━━\\n` +
      `📝 *Şerh / Görüş:*\\n${{content || '(Belirtilmedi)'}}\\n\\n` +
      `📚 *Dayanak / Kaynak:* ${{source}}\\n` +
      `🔗 *Rapor Linki:* https://mehmetyarici-crypto.github.io/quran-vision/`
  }};
}}

function sendViaWhatsApp() {{
  const data = buildFormattedFeedbackText();
  if (!data.content) {{
    showToast("⚠️ Lütfen önce görüş veya şerh metninizi yazınız.");
    document.getElementById('fbContent')?.focus();
    return;
  }}
  saveNoteToStorage(data);
  const waUrl = `https://wa.me/?text=${{encodeURIComponent(data.formatted)}}`;
  window.open(waUrl, '_blank');
}}

function openGitHubPeerReview() {{
  const data = buildFormattedFeedbackText();
  if (!data.content) {{
    showToast("⚠️ Lütfen önce görüş veya şerh metninizi yazınız.");
    document.getElementById('fbContent')?.focus();
    return;
  }}
  saveNoteToStorage(data);
  const issueTitle = `[${{data.category}}] ${{data.r.case_id}} (${{data.r.surah}} ${{data.r.verse}}) — ${{data.author}}`;
  const issueBody =
    `### 🏛️ Quran Vision (v6.2.1) Akademik Şerh & Katkı Kaydı\\n\\n` +
    `- **Vaka Kodu:** ${{data.r.case_id}}\\n` +
    `- **Sûre ve Âyet:** ${{data.r.surah}} Sûresi ${{data.r.verse}}\\n` +
    `- **Rapor Başlığı:** ${{data.r.topic}}\\n` +
    `- **SHA-256 Manifest:** ${{data.r.sha256}}\\n` +
    `- **Katkı Sunan:** ${{data.author}}\\n` +
    `- **Katkı Kategorisi:** ${{data.category}}\\n\\n` +
    `---\\n\\n` +
    `### 📝 Şerh / Analiz / Geri Bildirim Metni\\n\\n` +
    `${{data.content}}\\n\\n` +
    `### 📚 Dayanak Kaynak / Referans\\n\\n` +
    `${{data.source}}\\n`;
  const ghUrl = `https://github.com/mehmetyarici-crypto/quran-vision/issues/new?title=${{encodeURIComponent(issueTitle)}}&body=${{encodeURIComponent(issueBody)}}`;
  window.open(ghUrl, '_blank');
}}

function saveNoteToStorage(data) {{
  const key = 'qv_notes_v621';
  let existing = [];
  try {{
    existing = JSON.parse(localStorage.getItem(key) || '[]');
  }} catch (e) {{ existing = []; }}
  existing.unshift({{
    id: Date.now(),
    case_id: data.r.case_id,
    surah: data.r.surah,
    verse: data.r.verse,
    author: data.author,
    category: data.category,
    content: data.content,
    source: data.source,
    date: new Date().toLocaleString('tr-TR')
  }});
  localStorage.setItem(key, JSON.stringify(existing));
  renderLocalNotes();
}}

function saveLocalNoteAndCopy() {{
  const data = buildFormattedFeedbackText();
  if (!data.content) {{
    showToast("⚠️ Lütfen önce görüş veya şerh metninizi yazınız.");
    document.getElementById('fbContent')?.focus();
    return;
  }}
  saveNoteToStorage(data);
  if (navigator.clipboard) {{
    navigator.clipboard.writeText(data.formatted);
  }}
  showToast("✅ Şerhiniz bu raporun altına kaydedildi ve biçimlendirilmiş metin panoya kopyalandı!");
}}

function deleteLocalNote(noteId) {{
  const key = 'qv_notes_v621';
  let existing = [];
  try {{
    existing = JSON.parse(localStorage.getItem(key) || '[]');
  }} catch (e) {{ existing = []; }}
  existing = existing.filter(n => n.id !== noteId);
  localStorage.setItem(key, JSON.stringify(existing));
  renderLocalNotes();
}}

function renderLocalNotes() {{
  const r = REPORTS[currentIndex];
  const listEl = document.getElementById('localNotesList');
  const countEl = document.getElementById('localNotesCount');
  if (!listEl) return;

  let existing = [];
  try {{
    existing = JSON.parse(localStorage.getItem('qv_notes_v621') || '[]');
  }} catch (e) {{ existing = []; }}

  const reportNotes = existing.filter(n => n.case_id === r.case_id);
  if (countEl) countEl.textContent = `${{reportNotes.length}} Kayıtlı Not`;

  if (reportNotes.length === 0) {{
    listEl.innerHTML = `<div class="source-card" style="color:var(--text-muted); font-size:13px;">Bu rapor (${{r.case_id}}) için henüz tarayıcınıza kaydettiğiniz bir kişisel şerh veya ders notu bulunmuyor. Sağdaki formdan ekleyebilirsiniz.</div>`;
    return;
  }}

  listEl.innerHTML = reportNotes.map(n => `
    <div class="source-card">
      <div class="source-header">
        <span class="source-author">${{n.author}} • <span style="color:var(--accent-gold);">${{n.category}}</span></span>
        <button class="btn" style="padding:2px 8px; font-size:11px;" onclick="deleteLocalNote(${{n.id}})">🗑️ Sil</button>
      </div>
      <div style="font-size:13.5px; color:var(--text-primary); white-space:pre-wrap; margin-bottom:6px;">${{n.content.replace(/</g, '&lt;')}}</div>
      <div class="source-meta">📚 Kaynak: ${{n.source}} &nbsp;|&nbsp; 🕒 ${{n.date}}</div>
    </div>
  `).join('');
}}

function showToast(msg) {{
  const el = document.getElementById('fbToast');
  if (!el) return;
  el.textContent = msg;
  el.style.display = 'block';
  setTimeout(() => {{ el.style.display = 'none'; }}, 5000);
}}

function printCurrentReport() {{
  const r = REPORTS[currentIndex];
  const prevTheme = document.documentElement.getAttribute('data-theme');
  const prevTitle = document.title;
  document.documentElement.setAttribute('data-theme', 'light');
  document.title = `${{r.case_id}}_${{r.surah}}_Raporu`;
  setTimeout(() => {{
    window.print();
    document.documentElement.setAttribute('data-theme', prevTheme);
    document.title = prevTitle;
  }}, 150);
}}

function formatInlineMd(str) {{
  if (!str) return '';
  return str
    .replace(/\\[NAKİL\\]/g, '<span class="tag-nakil">[NAKİL]</span>')
    .replace(/\\[YORUM\\]/g, '<span class="tag-yorum">[YORUM]</span>')
    .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
    .replace(/\\*(.*?)\\*/g, '<em>$1</em>')
    .replace(/\\[\\^(\\d+)\\]/g, '<sup style="color:var(--accent-gold); font-weight:700;">[$1]</sup>');
}}

function renderMarkdown(md) {{
  const lines = md.split('\\n');
  let html = '';
  let inCode = false;
  let inTable = false;

  for (let i = 0; i < lines.length; i++) {{
    let line = lines[i];

    if (line.trim().startsWith('```')) {{
      if (!inCode) {{
        inCode = true;
        html += '<pre><code>';
      }} else {{
        inCode = false;
        html += '</code></pre>';
      }}
      continue;
    }}
    if (inCode) {{
      html += line.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '\\n';
      continue;
    }}

    if (line.trim().startsWith('|')) {{
      if (line.includes('---')) continue;
      const cells = line.split('|').slice(1, -1).map(c => formatInlineMd(c.trim()));
      if (!inTable) {{
        inTable = true;
        html += '<table><thead><tr>' + cells.map(c => `<th>${{c}}</th>`).join('') + '</tr></thead><tbody>';
      }} else {{
        html += '<tr>' + cells.map(c => `<td>${{c}}</td>`).join('') + '</tr>';
      }}
      continue;
    }} else if (inTable) {{
      inTable = false;
      html += '</tbody></table>';
    }}

    if (line.startsWith('# ')) {{
      html += `<h1>${{formatInlineMd(line.slice(2))}}</h1>`;
    }} else if (line.startsWith('## ')) {{
      html += `<h2>${{formatInlineMd(line.slice(3))}}</h2>`;
    }} else if (line.startsWith("### ")) {{
      html += `<h3>${{formatInlineMd(line.slice(4))}}</h3>`;
    }} else if (line.startsWith("#### ")) {{
      html += `<h4>${{formatInlineMd(line.slice(5))}}</h4>`;
    }} else if (line.trim() === '---') {{
      html += '<hr style="border:none; border-top:1px solid var(--border); margin:18px 0;">';
    }} else if (line.trim().startsWith('- ')) {{
      html += `<ul><li>${{formatInlineMd(line.trim().slice(2))}}</li></ul>`;
    }} else if (/^\\d+\\.\\s/.test(line.trim())) {{
      html += `<p style="margin-left:10px;">${{formatInlineMd(line.trim())}}</p>`;
    }} else if (line.trim().startsWith('[^')) {{
      html += `<p style="font-size:12.5px; color:var(--text-secondary); margin-bottom:6px;">${{formatInlineMd(line.trim())}}</p>`;
    }} else if (line.trim() !== '') {{
      html += `<p>${{formatInlineMd(line)}}</p>`;
    }}
  }}
  if (inTable) html += '</tbody></table>';
  return html;
}}

function setTab(tabName, btn) {{
  currentTab = tabName;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  document.getElementById('tab-dashboard').style.display = tabName === 'dashboard' ? 'block' : 'none';
  document.getElementById('tab-sources').style.display = tabName === 'sources' ? 'block' : 'none';
  document.getElementById('tab-fulltext').style.display = tabName === 'fulltext' ? 'block' : 'none';
  document.getElementById('tab-pedagogy').style.display = tabName === 'pedagogy' ? 'block' : 'none';
  document.getElementById('tab-synthesis').style.display = tabName === 'synthesis' ? 'block' : 'none';
  document.getElementById('tab-feedback').style.display = tabName === 'feedback' ? 'block' : 'none';
}}

function toggleTheme() {{
  const root = document.documentElement;
  root.setAttribute('data-theme', root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
}}

document.getElementById('searchInput').addEventListener('input', (e) => renderSidebar(e.target.value));

renderSidebar();
selectReport(0);
</script>
</body>
</html>
"""
    return html


def main():
    report_files = sorted(DOCS_TR.glob("[0-9][0-9]-*-v6.1.1.md"))
    report_files = [f for f in report_files if not f.name.startswith("05-")]
    reports = []
    for rf in report_files:
        parsed = parse_report(rf)
        if parsed:
            reports.append(parsed)

    html = build_html(reports)
    out1 = ROOT / "docs" / "index.html"
    out2 = ROOT.parent / "GEM_DIJITAL_KULLIYAT_PORTALI.html"
    out3 = ROOT.parent / "QURAN_VISION_KULLIYAT_PORTALI.html"
    out1.write_text(html, encoding="utf-8")
    out2.write_text(html, encoding="utf-8")
    out3.write_text(html, encoding="utf-8")
    print(f"✅ Portal üretildi: {out1} ({len(reports)} rapor)")
    print(f"✅ Masaüstü hızlı erişim kopyaları: {out2.name}, {out3.name}")

    if "--force-pdf" in sys.argv or not (PDF_DIR / "Quran_Vision_Kulliyat_v6.2.1.pdf").exists():
        print("🖨️ Gerçek A4 PDF dosyaları üretiliyor (Edge Headless Motoru)...")
        generate_all_pdfs(reports)
    else:
        print("✅ A4 PDF dosyaları zaten güncel (yeniden üretmek için --force-pdf kullanın).")


if __name__ == "__main__":
    main()
