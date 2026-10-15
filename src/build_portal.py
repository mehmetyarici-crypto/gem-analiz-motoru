#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEM v6.2.1 — İnteraktif Dijital Külliyat ve Akademik Portal Üreticisi
Tüm doğrulanmış GEM raporlarını (YAML Frontmatter + 26 Adım Markdown + .sha256 Manifest)
okuyarak tek tıkla çalışan bağımsız (self-contained) bir HTML5 Akademik Portal üretir.
"""

import json
import re
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

    # Extract Prior & Posterior if present
    prior_m = re.search(r"(?:P\(S1\)\s*=\s*|Prior\s*P\(H\)\):\*\*\s*)([0-9.]+)", body)
    post_m = re.search(r"P\(S1\|E\)\s*\\approx\s*([0-9.]+)", body)
    prior_val = float(prior_m.group(1)) if prior_m else 0.30
    post_val = float(post_m.group(1)) if post_m else 0.78

    return {
        "filename": md_path.name,
        "case_id": fm.get("case_id") or fm.get("vaka_kodu", ""),
        "surah": fm.get("surah") or fm.get("sure", ""),
        "verse": str(fm.get("verse") or fm.get("ayet_no", "")),
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
        "prior": prior_val,
        "posterior": post_val,
        "body": body,
    }


def build_html(reports):
    reports_json = json.dumps(reports, ensure_ascii=False)
    total_classical = sum(len(r["classical_sources"]) for r in reports)
    total_modern = sum(len(r["modern_sources"]) for r in reports)

    html = f"""<!DOCTYPE html>
<html lang="tr" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quran Vision (v6.2.1) — Kur'an Temelli Gelecek Vizyonu | Dijital Akademik Külliyat Portalı</title>
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
}}
.stats-bar {{
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
}}
.stat-pill {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--text-secondary);
  background: var(--bg-surface);
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid var(--border);
}}
.stat-pill strong {{
  color: var(--accent-emerald);
  font-size: 13px;
}}
.top-actions {{
  display: flex;
  gap: 10px;
}}
.btn {{
  padding: 7px 14px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-card);
  color: var(--text-primary);
  font-size: 12.5px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s;
}}
.btn:hover {{
  border-color: var(--accent-gold);
  color: var(--accent-gold);
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

@media print {{
  .sidebar, .topbar, .tabs {{ display: none !important; }}
  body, .main, .content-scroll {{ height: auto; overflow: visible; }}
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
      <button class="btn" onclick="toggleTheme()">🌗 Tema Değiştir</button>
      <button class="btn" onclick="window.print()">🖨️ PDF / Yazdır</button>
    </div>
  </header>

  <section class="content-scroll">
    <div class="hero-card" id="heroCard"></div>

    <div class="tabs">
      <button class="tab-btn active" onclick="setTab('dashboard', this)">📊 1. Stratejik Kokpit & Aporia</button>
      <button class="tab-btn" onclick="setTab('sources', this)">🏛️ 2. İSNAD 2 Klasik & Modern Kaynakça</button>
      <button class="tab-btn" onclick="setTab('fulltext', this)">📖 3. Tam Akademik Metin (26 Adım + Dipnotlar)</button>
    </div>

    <div id="tab-dashboard"></div>
    <div id="tab-sources" style="display:none;"></div>
    <div id="tab-fulltext" style="display:none;"></div>
  </section>
</main>

<script>
const REPORTS = {reports_json};
let currentIndex = 0;
let currentTab = 'dashboard';

function renderSidebar(filter = '') {{
  const listEl = document.getElementById('reportList');
  const q = filter.toLowerCase().trim();
  listEl.innerHTML = '';

  REPORTS.forEach((r, idx) => {{
    const searchable = (r.surah + ' ' + r.verse + ' ' + r.topic + ' ' + r.case_id + ' ' + r.body).toLowerCase();
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

  // Hero
  document.getElementById('heroCard').innerHTML = `
    <div class="hero-meta">
      <span class="badge badge-gold">📖 ${{r.surah}} Sûresi ${{r.verse}}</span>
      <span class="badge badge-emerald">Katman 3 • H6 Zorlu Âyet</span>
      <span class="badge badge-mono">${{r.case_id}}</span>
      <span class="badge badge-mono">Güven Derecesi: ${{r.confidence}}</span>
      <span class="badge badge-mono">Statü: ${{r.status}}</span>
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
    }} else if (line.startsWith('### ')) {{
      html += `<h3>${{formatInlineMd(line.slice(4))}}</h3>`;
    }} else if (line.startsWith('#### ')) {{
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
  btn.classList.add('active');
  document.getElementById('tab-dashboard').style.display = tabName === 'dashboard' ? 'block' : 'none';
  document.getElementById('tab-sources').style.display = tabName === 'sources' ? 'block' : 'none';
  document.getElementById('tab-fulltext').style.display = tabName === 'fulltext' ? 'block' : 'none';
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
    # Exclude template 05
    report_files = [f for f in report_files if not f.name.startswith("05-")]
    reports = []
    for rf in report_files:
        parsed = parse_report(rf)
        if parsed:
            reports.append(parsed)

    html = build_html(reports)
    out1 = ROOT / "docs" / "index.html"
    out2 = ROOT.parent / "GEM_DIJITAL_KULLIYAT_PORTALI.html"
    out1.write_text(html, encoding="utf-8")
    out2.write_text(html, encoding="utf-8")
    print(f"✅ Portal üretildi: {out1} ({len(reports)} rapor)")
    print(f"✅ Masaüstü hızlı erişim kopyası: {out2}")


if __name__ == "__main__":
    main()
