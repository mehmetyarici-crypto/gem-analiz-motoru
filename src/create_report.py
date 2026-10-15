#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quran Vision v6.2.1 — İki Aşamalı Akademik Rapor Üretim ve Editoryal Mühürleme Boru Hattı (create_report.py)

Mimari İlke (Human-in-the-Loop / Başeditör Kapısı):
  1. AŞAMA (--stage draft):
     - Raporu şablondan üretir veya mevcut taslağı `gem_lint.py` ile denetler.
     - Yerel önizleme için web portalını günceller (PDF ve .sha256 mührü basmaz, GitHub'a göndermez).
     - Başeditör Arapça İSNAD 2 ibarelerini, cilt/sayfa numaralarını ve DOI linklerini yerel ekranda denetler.

  2. AŞAMA (--stage seal / --stage publish):
     - Başeditör onayından sonra harici `.sha256` kriptografik bütünlük manifestini üretir.
     - `gem_lint.py --katman 3 --h6` çalıştırarak **0 BLOCK (Kesici Hata)** şartını zorunlu tutar.
     - `build_portal.py --force-pdf` çalıştırarak hem interaktif portalı hem de tekil + tam külliyat A4 PDF'lerini derler.
"""

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
DOCS_TR = ROOT / "docs" / "tr"
LINT_SCRIPT = ROOT / "src" / "gem_lint.py"
PORTAL_SCRIPT = ROOT / "src" / "build_portal.py"
TEMPLATE_FILE = DOCS_TR / "05-ornek-rapor-v6.1.1.md"


def compute_sha256_manifest(md_path: Path) -> Path:
    digest = hashlib.sha256(md_path.read_bytes()).hexdigest()
    sha_path = md_path.with_suffix(md_path.suffix + ".sha256")
    sha_path.write_text(f"{digest}  {md_path.name}\n", encoding="utf-8")
    return sha_path


def run_linter(md_path: Path) -> int:
    cmd = [sys.executable, str(LINT_SCRIPT), str(md_path), "--katman", "3", "--h6"]
    proc = subprocess.run(cmd)
    return proc.returncode


def scaffold_new_report(case_id: str, surah: str, verse: str, topic: str, out_filename: str) -> Path:
    target = DOCS_TR / out_filename
    if target.exists():
        print(f"ℹ️ Rapor dosyası zaten mevcut: {target}")
        return target
    raw = TEMPLATE_FILE.read_text(encoding="utf-8")
    raw = re.sub(r'^case_id:\s*".*?"', f'case_id: "{case_id}"', raw, flags=re.MULTILINE)
    raw = re.sub(r'^surah:\s*".*?"', f'surah: "{surah}"', raw, flags=re.MULTILINE)
    raw = re.sub(r'^verse:\s*".*?"', f'verse: "{verse}"', raw, flags=re.MULTILINE)
    raw = re.sub(r'^topic:\s*".*?"', f'topic: "{topic}"', raw, flags=re.MULTILINE)
    raw = re.sub(r'^status:\s*".*?"', 'status: "DRAFT"', raw, flags=re.MULTILINE)
    target.write_text(raw, encoding="utf-8")
    print(f"📝 Yeni taslak şablondan oluşturuldu (status: DRAFT): {target}")
    return target


def main():
    parser = argparse.ArgumentParser(description="Quran Vision v6.2.1 — İki Aşamalı Akademik Rapor Boru Hattı")
    parser.add_argument("report", nargs="?", help="İşlenecek rapor dosyası (örn. docs/tr/19-rapor-hucurat-4913-v6.1.1.md)")
    parser.add_argument("--stage", choices=["draft", "seal", "publish"], default="draft",
                        help="draft: Taslak denetimi ve yerel önizleme | seal: SHA-256 mühürleme + 0 BLOCK kontrolü + PDF derleme | publish: seal + git commit/push")
    parser.add_argument("--scaffold", action="store_true", help="Şablondan yeni bir DRAFT rapor dosyası oluştur")
    parser.add_argument("--case-id", default="QV-2026-014", help="Yeni rapor vaka kodu")
    parser.add_argument("--surah", default="Hucurât", help="Yeni rapor sûre adı")
    parser.add_argument("--verse", default="49:13", help="Yeni rapor âyet numarası")
    parser.add_argument("--topic", default="", help="Yeni rapor stratejik başlığı")
    args = parser.parse_args()

    if args.scaffold:
        if not args.report:
            print("❌ --scaffold için hedef dosya adını belirtmelisiniz.")
            sys.exit(1)
        md_path = scaffold_new_report(args.case_id, args.surah, args.verse, args.topic, Path(args.report).name)
    else:
        if not args.report:
            print("❌ Lütfen işlenecek rapor dosyasını belirtin.")
            sys.exit(1)
        md_path = Path(args.report)
        if not md_path.exists():
            md_path = DOCS_TR / Path(args.report).name
        if not md_path.exists():
            print(f"❌ Dosya bulunamadı: {args.report}")
            sys.exit(1)

    if args.stage == "draft":
        print("══════════════════════════════════════════════════════════════════")
        print(f"🔍 [AŞAMA 1: TASLAK & YEREL ÖNİZLEME] {md_path.name}")
        print("══════════════════════════════════════════════════════════════════")
        print("ℹ️ Geçici doğrulama için .sha256 kontrolü yapılıyor...")
        compute_sha256_manifest(md_path)
        rc = run_linter(md_path)
        if rc >= 2:
            print("⚠️ Taslakta kesici (BLOCK) bulgular var. Mühürleme öncesi düzeltilmelidir.")
            sys.exit(rc)
        subprocess.run([sys.executable, str(PORTAL_SCRIPT)], check=True)
        print("\n✅ [AŞAMA 1 TAMAMLANDI] Taslak (0 KESİCİ HATA) yerel portala (http://localhost:8080) yüklendi.")
        print("👉 Başeditör olarak Arapça İSNAD 2 ibarelerini, cilt/sayfa numaralarını ve DOI linklerini")
        print("   kontrol ettikten sonra mühürlemek ve PDF üretmek için şu komutu çalıştırın:")
        print(f"   python src/create_report.py {md_path.name} --stage seal")

    elif args.stage in ("seal", "publish"):
        print("══════════════════════════════════════════════════════════════════")
        print(f"🔒 [AŞAMA 2: BAŞEDİTÖR MÜHÜRLEME & A4 PDF DERLEME] {md_path.name}")
        print("══════════════════════════════════════════════════════════════════")
        content = md_path.read_text(encoding="utf-8")
        if 'status: "DRAFT"' in content:
            content = content.replace('status: "DRAFT"', 'status: "PRE-RELEASE"')
            md_path.write_text(content, encoding="utf-8")
            print("🔄 Rapor statüsü DRAFT -> PRE-RELEASE olarak güncellendi.")

        sha_path = compute_sha256_manifest(md_path)
        print(f"🔐 Harici Kriptografik Manifest üretildi: {sha_path.name}")

        rc = run_linter(md_path)
        if rc >= 2:
            print("❌ KESİCİ HATA (BLOCK): Rapor linter denetiminden geçemedi! Yayın durduruldu.")
            sys.exit(rc)

        print("🌐 Web Portalı ve A4 Akademik PDF Külliyatı yeniden derleniyor...")
        subprocess.run([sys.executable, str(PORTAL_SCRIPT), "--force-pdf"], check=True)
        print(f"\n🎉 [MÜHÜRLEME TAMAMLANDI] {md_path.name} 0 KESİCİ HATA ile külliyata eklendi!")


if __name__ == "__main__":
    main()
