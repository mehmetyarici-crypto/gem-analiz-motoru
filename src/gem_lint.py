#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEM Linter — Dil Güvenliği Denetçisi (İki Dilli v5.1.6)
GEM v5.1.3 Bölüm 18.1 kurallarına göre rapor dosyalarını tarar.

Kullanım:
    python gem_lint.py dosya_adi.md

Çıktı:
    - Yasaklı kelimeler varsa SATIR NUMARASI ile uyarır
    - Zorunlu bölümler eksikse bildirir
    - Sonuç: GEÇTİ / ŞARTLI / DÜŞTÜ
"""

import sys
import os


# ============================================
# NORMALİZASYON — Unicode, apostrof, Türkçe karakterler
# ============================================
NORMALIZE_HARITA = {
    "ī": "i", "ş": "s", "ğ": "g", "ü": "u", "ö": "o", "ç": "c", "ı": "i",
    "ā": "a", "ṣ": "s", "ḍ": "d", "ṭ": "t", "ẓ": "z", "ḥ": "h",
    "â": "a", "î": "i", "û": "u", "é": "e", "è": "e",
    "ʿ": "", "ʾ": "", "ʼ": "",
    "'": "", "\u2019": "", "`": "", "´": "",
    "\u201c": "", "\u201d": "",
}


def normalize(metin):
    """Metni karşılaştırma için normalize eder."""
    if not metin:
        return ""
    metin = metin.lower()
    for eski, yeni in NORMALIZE_HARITA.items():
        metin = metin.replace(eski, yeni)
    return metin


# ============================================
# YASAKLI KELİMELER — Hard Fail (Bölüm 18.1)
# ============================================
YASAKLI_KELIMELER = {
    # --- Türkçe ---
    "mükemmel": "Mutlak başarı iddiası — Sıfır İlke 3 ihlali",
    "%100": "Sayısal kesinlik iddiası — Bölüm 9 ihlali",
    "kesinlikle": "Mutlak kesinlik iddiası — Bölüm 18.1 ihlali",
    "tartışmasız": "Tartışma reddi — Bölüm 18.1 ihlali",
    "sıfır zafiyet": "Kusursuzluk iddiası — Bölüm 18.1 ihlali",
    "sıfır metodolojik zafiyet": "Kusursuzluk iddiası — Bölüm 18.1 ihlali",
    "ispatlanmıştır": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
    "onaylandı (tam uyum)": "Kendi kendine tam puan — Bölüm 18.1 ihlali",
    "tam uyum": "Kendi kendine tam puan — Bölüm 18.1 ihlali",
    # --- İngilizce ---
    "flawless": "Mutlak başarı iddiası — Sıfır İlke 3 ihlali",
    "100%": "Sayısal kesinlik iddiası — Bölüm 9 ihlali",
    "absolutely": "Mutlak kesinlik iddiası — Bölüm 18.1 ihlali",
    "indisputably": "Tartışma reddi — Bölüm 18.1 ihlali",
    "zero vulnerability": "Kusursuzluk iddiası — Bölüm 18.1 ihlali",
    "proven": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
}


# ============================================
# KOŞULLU YASAKLI — Uyarı Verir (Hard Fail Değil)
# ============================================
KOSULLU_YASAKLI = {
    "mutlak": "Naṣṣ bağlamı dışındaki mutlaklık iddiası olabilir — bağlamı kontrol et",
    "absolute": "Naṣṣ bağlamı dışındaki mutlaklık iddiası olabilir — bağlamı kontrol et",
}


# ============================================
# İSTİSNALAR — Bu İfadeler Geçiyorsa Uyarı Vermez
# ============================================
ISTISNA_IFADELERI = [
    # --- Türkçe bağlamlar ---
    "mutlak mülkiyet", "mutlak sahip", "mutlak egemenlik",
    "mutlak caydırıcılık", "mutlak adalet", "mutlak otorite",
    "mutlak koruma", "mutlak güvenlik", "mutlak bağlılık",
    "mutlak yokluk", "mutlak varlık",
    # --- İngilizce bağlamlar ---
    "absolute ownership", "absolute sovereign", "absolute sovereignty",
    "absolute divine", "absolute god", "absolute deterrence",
    "absolute destruction", "absolute justice", "absolute authority",
    "absolute property", "absolute security", "absolute reliability",
    "absolute protection", "absolute pacifist", "absolute pacifism",
    "absolute ritualized", "absolute obligation", "absolute market",
    "absolute labor", "absolute static", "absolute boundary",
    "absolute absence", "absolute deterrent",
]


# ============================================
# ÖZ-DENETİM SATIRLARI — Atlanacak
# ============================================
OZ_DENETIM_ISARETLERI = [
    "yasaklı kelime",
    "forbidden word",
    "kullanılmamıştır",
    "not been used",
    "strictly avoided",
]


# ============================================
# ZORUNLU BÖLÜMLER — İki Dilli
# ============================================
ZORUNLU_BOLUMLER = [
    ["yorumcu konumu", "interpreter position", "interpreters position"],
    ["zemahşerî", "zamakhshari", "zamahşeri"],
    ["falsifiabilite", "falsifiability"],
    ["tipping point", "tipping point"],
    ["n4", "n4"],
    ["s7", "s7"],
    ["zayıflık", "weakness"],
    ["geliştirme", "development"],
    ["geliştirme önerisi", "development suggestion"],
    ["öz-denetim", "self-audit", "self audit"],
    ["dil güvenliği", "language safety"],
    ["karar kolu", "decision branch"],
    ["aktör", "actor"],
    ["retrodiction", "retroadiction"],
    ["karşıt ilke", "counter-principle", "counter principle"],
]


# ============================================
# UYARI KELİMELERİ — Dikkat Gerektirir
# ============================================
UYARI_KELIMELERI = {
    "doğrulandı": "Retrodiction sonucu — 'Kısmen' ile birlikte kullanıldı mı kontrol et",
    "sabit": "Bilgi tabanı — katmanlı mı (İlke/Uygulama) kontrol et",
    ">%": "Sayısal olasılık — Bölüm 9 kapsamına giriyor mu kontrol et",
}


# ============================================
# YAZIM HATALARI
# ============================================
YAZIM_DUZELTMELERI = {
    "casser auda": "jasser auda",
    "cassar auda": "jasser auda",
    "ibn aşür": "ibn âşûr",
    "ibn asur": "ibn âşûr",
    "zamahşeri": "zemahşerî",
    "zamahşerî": "zemahşerî",
    "ragıb": "râgıb",
    "retroadiction": "retrodiction",
}


def tara(dosya_adi):
    """Rapor dosyasını tarar ve sonuç üretir."""

    if not os.path.exists(dosya_adi):
        print(f"❌ HATA: '{dosya_adi}' dosyası bulunamadı.")
        sys.exit(1)

    with open(dosya_adi, "r", encoding="utf-8") as f:
        satirlar = f.readlines()

    # Tüm metni normalize et
    metin_birlesik = normalize("".join(satirlar))

    # Öz-denetim işaretlerini de normalize et
    oz_denetim_norm = [normalize(i) for i in OZ_DENETIM_ISARETLERI]

    bulgular = []
    yasak_sayisi = 0
    uyari_sayisi = 0
    yazim_hata_sayisi = 0
    eksik_bolumler = []

    # Normalize edilmiş istisna listesi
    istisna_norm = [normalize(i) for i in ISTISNA_IFADELERI]

    # --- 1. Yasaklı kelime taraması (hard fail) ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_norm = normalize(satir)

        # Öz-denetim satırı mı?
        if any(isaret in satir_norm for isaret in oz_denetim_norm):
            continue

        for yasakli, aciklama in YASAKLI_KELIMELER.items():
            yasakli_norm = normalize(yasakli)
            if yasakli_norm in satir_norm:
                yasak_sayisi += 1
                bulgular.append({
                    "tur": "YASAKLI",
                    "satir": satir_no,
                    "kelime": yasakli,
                    "aciklama": aciklama,
                })

    # --- 2. Koşullu yasaklı (mutlak/absolute) ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_norm = normalize(satir)

        if any(isaret in satir_norm for isaret in oz_denetim_norm):
            continue

        for kosullu, aciklama in KOSULLU_YASAKLI.items():
            kosullu_norm = normalize(kosullu)
            if kosullu_norm in satir_norm:
                istisna_var = any(ist in satir_norm for ist in istisna_norm)
                if istisna_var:
                    continue
                uyari_sayisi += 1
                bulgular.append({
                    "tur": "UYARI",
                    "satir": satir_no,
                    "kelime": kosullu,
                    "aciklama": aciklama,
                })

    # --- 3. Yazım hataları ---
    for yanlis, dogru in YAZIM_DUZELTMELERI.items():
        yanlis_norm = normalize(yanlis)
        if yanlis_norm in metin_birlesik:
            yazim_hata_sayisi += 1
            bulgular.append({
                "tur": "YAZIM",
                "satir": "-",
                "kelime": yanlis,
                "aciklama": f"Olması gereken: '{dogru}'",
            })

    # --- 4. Diğer uyarı kelimeleri ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_norm = normalize(satir)
        for uyari, aciklama in UYARI_KELIMELERI.items():
            uyari_norm = normalize(uyari)
            if uyari_norm in satir_norm:
                uyari_sayisi += 1
                bulgular.append({
                    "tur": "UYARI",
                    "satir": satir_no,
                    "kelime": uyari,
                    "aciklama": aciklama,
                })

    # --- 5. Zorunlu bölüm kontrolü (iki dilli) ---
    for bolum_cift in ZORUNLU_BOLUMLER:
        bulundu = any(normalize(bolum) in metin_birlesik for bolum in bolum_cift)
        if not bulundu:
            eksik_bolumler.append(bolum_cift[0])

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
    # Karar sadece hard fail'lere bakar; uyarılar ve eksik bölümler karara etki etmez
    toplam_sorun = yasak_sayisi + yazim_hata_sayisi

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
        sys.exit(2)
    elif toplam_sorun > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python gem_lint.py dosya_adi.md")
        print("Örnek:   python gem_lint.py ornek-rapor.md")
        sys.exit(1)

    tara(sys.argv[1])
