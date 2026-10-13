#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEM Linter — Dil Güvenliği Denetçisi
GEM v5.1.3 Bölüm 18.1 kurallarına göre rapor dosyalarını tarar.

Kullanım:
    python gem_lint.py dosya_adi.md

Çıktı:
    - Yasaklı kelimeler varsa SATIR NUMARASI ile uyarır
    - Zorunlu bölümler eksikse bildirir
    - Sonuç: GEÇTİ / ŞARTLI / DÜŞTÜ
"""

import sys
import re
import os


# ============================================
# YASAKLI KELİMELER (Bölüm 18.1)
# ============================================
YASAKLI_KELIMELER = {
    "mükemmel": "Mutlak başarı iddiası — Sıfır İlke 3 ihlali",
    "%100": "Sayısal kesinlik iddiası — Bölüm 9 ihlali",
    "kesinlikle": "Mutlak kesinlik iddiası — Bölüm 18.1 ihlali",
    "tartışmasız": "Tartışma reddi — Bölüm 18.1 ihlali",
    "sıfır zafiyet": "Kusursuzluk iddiası — Bölüm 18.1 ihlali",
    "sıfır metodolojik zafiyet": "Kusursuzluk iddiası — Bölüm 18.1 ihlali",
    "ispatlanmıştır": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
    "onaylandı (tam uyum)": "Kendi kendine tam puan — Bölüm 18.1 ihlali",
    "tam uyum": "Kendi kendine tam puan — Bölüm 18.1 ihlali",
}

# "mutlak" istisnası: nass bağlamında kullanılırsa serbest
MUTLAK_ISTISNA_KELIMELERI = ["mutlak mülkiyet", "mutlak sahip", "mutlak egemenlik"]


# ============================================
# ZORUNLU BÖLÜMLER (Katman 3 rapor için)
# ============================================
ZORUNLU_BOLUMLER = [
    "yorumcu konumu",
    "zemahşerî",
    "falsifiabilite",
    "tipping point",
    "n4",
    "s7",
    "zayıflık",
    "geliştirme",
    "geliştirme önerisi",
    "öz-denetim",
    "dil güvenliği",
    "karar kolu",
    "aktör",
    "retroadiction",
    "karşıt ilke",
]


# ============================================
# UYARI KELİMELERİ (Dikkat gerektirir ama yasak değildir)
# ============================================
UYARI_KELIMELERERI = {
    "doğrulandı": "Retroadiction sonucu — 'Kısmen' ile birlikte kullanıldı mı kontrol et",
    "sabit": "Bilgi tabanı — katmanlı mı (İlke/Uygulama) kontrol et",
    ">%": "Sayısal olasılık — Bölüm 9 kapsamına giriyor mu kontrol et",
}


# ============================================
# YAZIM HATALARI KONTROLÜ
# ============================================
YAZIM_DUZELTMELERI = {
    "casser auda": "jasser auda",
    "cassar auda": "jasser auda",
    "ibn aşür": "ibn âşûr",
    "ibn asur": "ibn âşûr",
    "zamahşeri": "zemahşerî",
    "zamahşerî": "zemahşerî",
    "ragıb": "râgıb",
}


def tara(dosya_adi):
    """Rapor dosyasını tarar ve sonuç üretir."""

    if not os.path.exists(dosya_adi):
        print(f"❌ HATA: '{dosya_adi}' dosyası bulunamadı.")
        sys.exit(1)

    with open(dosya_adi, "r", encoding="utf-8") as f:
        satirlar = f.readlines()

    metin_birlesik = "".join(satirlar).lower()
    bulgular = []
    yasak_sayisi = 0
    uyari_sayisi = 0
    yazim_hata_sayisi = 0
    eksik_bolumler = []

    # --- 1. Yasaklı kelime taraması ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_lower = satir.lower()

        for yasakli, aciklama in YASAKLI_KELIMELER.items():
            if yasakli in satir_lower:
                # "mutlak" istisna kontrolü
                if yasakli == "mutlak":
                    istisna_var = any(i in satir_lower for i in MUTLAK_ISTISNA_KELIMELERI)
                    if istisna_var:
                        continue
                yasak_sayisi += 1
                bulgular.append({
                    "tur": "YASAKLI",
                    "satir": satir_no,
                    "kelime": yasakli,
                    "aciklama": aciklama,
                })

    # --- 2. Yazım hataları ---
    for yanlis, dogru in YAZIM_DUZELTMELERI.items():
        if yanlis in metin_birlesik:
            yazim_hata_sayisi += 1
            bulgular.append({
                "tur": "YAZIM",
                "satir": "-",
                "kelime": yanlis,
                "aciklama": f"Olması gereken: '{dogru}'",
            })

    # --- 3. Uyarı kelimeleri ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_lower = satir.lower()
        for uyari, aciklama in UYARI_KELIMELERERI.items():
            if uyari in satir_lower:
                uyari_sayisi += 1
                bulgular.append({
                    "tur": "UYARI",
                    "satir": satir_no,
                    "kelime": uyari,
                    "aciklama": aciklama,
                })

    # --- 4. Zorunlu bölüm kontrolü ---
    for bolum in ZORUNLU_BOLUMLER:
        if bolum not in metin_birlesik:
            eksik_bolumler.append(bolum)

    # ============================================
    # SONUÇ RAPORU
    # ============================================
    print("=" * 60)
    print("   GEM LINTER — Dil Güvenliği Denetim Raporu")
    print("   Dosya:", dosya_adi)
    print("=" * 60)
    print()

    if bulgular:
        print("📋 BULGULAR:")
        print("-" * 60)
        for b in bulgular:
            ikon = {"YASAKLI": "🚫", "YAZIM": "✏️", "UYARI": "⚠️"}[b["tur"]]
            print(f"  {ikon} [{b['tur']}] Satır {b['satir']}: '{b['kelime']}'")
            print(f"     → {b['aciklama']}")
        print()
    else:
        print("✅ Yasaklı kelime, yazım hatası veya uyarı bulunamadı.")
        print()

    if eksik_bolumler:
        print("📋 EKSİK ZORUNLU BÖLÜMLER:")
        print("-" * 60)
        for e in eksik_bolumler:
            print(f"  ❌ '{e}' bölümü bulunamadı.")
        print()

    # --- Nihai karar ---
    print("=" * 60)
    toplam_sorun = yasak_sayisi + yazim_hata_sayisi + len(eksik_bolumler)

    if yasak_sayisi > 0:
        karar = "🔴 DÜŞTÜ"
        gerekce = f"{yasak_sayisi} yasaklı kelime bulundu. Rapor derlenemez."
    elif toplam_sorun > 3:
        karar = "🟡 ŞARTLI"
        gerekce = f"{toplam_sorun} sorun bulundu. Düzeltilmeden yayınlanmamalı."
    elif toplam_sorun > 0:
        karar = "🟡 GEÇTİ (Şartlı)"
        gerekce = f"{toplam_sorun} küçük sorun var. Düzeltilmesi önerilir."
    else:
        karar = "🟢 GEÇTİ"
        gerekce = "Temel kontroller geçti. Red Team incelemesi önerilir."

    print(f"  SONUÇ: {karar}")
    print(f"  Gerekçe: {gerekce}")
    print(f"  Yasaklı kelime: {yasak_sayisi}")
    print(f"  Yazım hatası: {yazim_hata_sayisi}")
    print(f"  Uyarı: {uyari_sayisi}")
    print(f"  Eksik bölüm: {len(eksik_bolumler)}")
    print("=" * 60)

    # Çıkış kodu
    if yasak_sayisi > 0:
        sys.exit(2)   # DÜŞTÜ
    elif toplam_sorun > 0:
        sys.exit(1)   # ŞARTLI
    else:
        sys.exit(0)   # GEÇTİ


# ============================================
# ANA GİRİŞ
# ============================================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python gem_lint.py dosya_adi.md")
        print("Örnek:   python gem_lint.py ornek-rapor.md")
        sys.exit(1)

    tara(sys.argv[1])
