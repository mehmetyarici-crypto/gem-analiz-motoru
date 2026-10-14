#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEM Linter v5.2.1 — Dil Güvenliği Denetçisi (İki Dilli + v5.2.0 Kuralları + False Positive Düzeltmeleri)
GEM v5.2.0 Bölüm 18.1 + 18.1-B muafiyet kurallarına göre rapor dosyalarını tarar.

Kullanım:
    python gem_lint.py dosya_adi.md
    python gem_lint.py dosya_adi.md --katman 3
    python gem_lint.py dosya_adi.md --katman 3 --h6

Çıktı:
    - Yasaklı kelimeler varsa SATIR NUMARASI ile uyarır
    - Tırnak içindeki yasaklı kelimeler MUAF sayılır (18.1-B)
    - Zorunlu bölümler eksikse bildirir
    - Falsifiabilite standardı (zaman + endeks + eşik) kontrolü
    - Bayes alanı kontrolü (Katman 3)
    - 3'lü Dil Matrisi kontrolü (H6)
    - Sonuç: GEÇTİ / ŞARTLI / DÜŞTÜ

v5.2.0 Değişiklikleri:
    - 18.1-B Muafiyet: tırnak içindeki yasaklı kelimeler ihlal sayılmaz
    - Yeni yasaklı kelimeler eklendi (TR + EN)
    - Yeni uyarı kelimeleri eklendi
    - Falsifiabilite standardı kontrolü eklendi (Değişiklik 2)
    - Bayes alanı kontrolü eklendi (Değişiklik 3)
    - 3'lü Dil Matrisi kontrolü eklendi (Değişiklik 4)
    - --katman ve --h6 komut satırı seçenekleri eklendi
    - Yazım düzeltmeleri genişletildi
    - Mevcut v5.1.6 normalizasyon sistemi korundu

v5.2.1 Düzeltmeleri (False Positive):
    - "is-ought" arama kelimeleri genişletildi (raporlarda farklı başlıkla geçiyor)
    - "künye" arama kelimeleri genişletildi (raporlarda farklı başlıkla geçiyor)
    - "hume" arama kelimeleri genişletildi (raporlarda farklı başlıkla geçiyor)
    - Yazım kontrolü düzeltmesi: normalize edilmiş "beccaria", "de soto", "şatibî"
      kontrolü daha hassas yapıldı
"""

import sys
import re
import os


# ============================================
# NORMALİZASYON — Unicode, apostrof, Türkçe karakterler
# (v5.1.6'dan korundu)
# ============================================
NORMALIZE_HARITA = {
    "\u0307": "", "İ": "i",
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
# v5.2.0 — 18.1-B MUAFİYET: TIRNAK İÇİ KONTROL
# ============================================
CITIRNAK_MUAFIYET_REGEX = re.compile(r'"[^"]*"|\'[^\']*\'|«[^»]*»')


def citirnak_muaf_mi(satir, kelime):
    """
    18.1-B muafiyet kontrolü:
    Kelime tırnak içinde mi? Öyleyse muaf.
    """
    citirnaklar = CITIRNAK_MUAFIYET_REGEX.findall(satir)
    for c in citirnaklar:
        if normalize(kelime) in normalize(c):
            return True
    return False


# ============================================
# YASAKLI KELİMELER — Hard Fail (Bölüm 18.1)
# v5.2.0: 3 yeni TR + 3 yeni EN eklendi
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
    # --- v5.2.0 Yeni Türkçe ---
    "kanıtlanmıştır": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
    "herkesçe bilinmektedir": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
    "tartışmaya kapalı": "Tartışma reddi — Bölüm 18.1 ihlali",
    # --- İngilizce ---
    "flawless": "Mutlak başarı iddiası — Sıfır İlke 3 ihlali",
    "100%": "Sayısal kesinlik iddiası — Bölüm 9 ihlali",
    "absolutely": "Mutlak kesinlik iddiası — Bölüm 18.1 ihlali",
    "indisputably": "Tartışma reddi — Bölüm 18.1 ihlali",
    "zero vulnerability": "Kusursuzluk iddiası — Bölüm 18.1 ihlali",
    "proven": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
    # --- v5.2.0 Yeni İngilizce ---
    "universally known": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
    "beyond dispute": "Tartışma reddi — Bölüm 18.1 ihlali",
    "definitively proven": "Kanıt kesinliği iddiası — Bölüm 18.1 ihlali",
}


# ============================================
# KOŞULLU YASAKLI — Uyarı Verir (Hard Fail Değil)
# (v5.1.6'dan korundu)
# ============================================
KOSULLU_YASAKLI = {
    "mutlak": "Naṣṣ bağlamı dışındaki mutlaklık iddiası olabilir — bağlamı kontrol et",
    "absolute": "Naṣṣ bağlamı dışındaki mutlaklık iddiası olabilir — bağlamı kontrol et",
}


# ============================================
# İSTİSNALAR — Bu İfadeler Geçiyorsa Uyarı Vermez
# (v5.1.6'dan korundu)
# ============================================
ISTISNA_IFADELERI = [
    # --- Türkçe bağlamlar ---
    "mutlak mülkiyet", "mutlak sahip", "mutlak egemenlik",
    "mutlak caydırıcılık", "mutlak adalet", "mutlak otorite",
    "mutlak koruma", "mutlak güvenlik", "mutlak bağlılık",
    "mutlak yokluk", "mutlak varlık",
    "mutlak kurulduğu", "mutlak kılmak",
    "mutlak dokunulmazlık",
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
# (v5.1.6'dan korundu)
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
# (v5.1.6 + v5.2.0 + v5.2.1 genişletmeleri)
# ============================================
ZORUNLU_BOLUMLER = [
    ["yorumcu konumu", "interpreter position", "interpreters position",
     "yorumcu konum", "yorumlayıcı konum"],
    ["zemahşerî", "zamakhshari", "zamahşeri", "keşşaf", "kashshaf"],
    ["falsifiabilite", "falsifiability", "yanlışlanabilirlik"],
    ["tipping point", "tipping point", "kırılma noktası"],
    ["n4", "n4"],
    ["s7", "s7"],
    ["zayıflık", "weakness"],
    ["geliştirme", "development"],
    ["geliştirme önerisi", "development suggestion"],
    ["öz-denetim", "self-audit", "self audit", "oz-denetim"],
    ["dil güvenliği", "language safety", "dil guvenligi"],
    ["karar kolu", "decision branch", "karar kol"],
    ["aktör", "actor", "aktor"],
    ["retrodiction", "retroadiction", "retrodiksiyon", "geriye dönük"],
    ["karşıt ilke", "counter-principle", "counter principle",
     "karsit ilke", "muhalif ilke", "çapraz ilke"],
    # --- v5.2.0 Yeni + v5.2.1 genişletmeleri ---
    ["is-ought", "is ought", "is–ought", "is-ought köprüsü",
     "is ought köprüsü", "mevcut-olması gereken", "descriptive-normative",
     "is-ought bridge", "is ought bridge",
     "olduğu gibi-olması gereken", "var olan-olması gereken",
     "olan-olması gereken", "vekalet", "geçiş köprüsü"],
    ["hume", "hume", "hume giyotini", "humes guillotine",
     "hume guillotine", "hume's guillotine",
     "olgu-değer ayrımı", "descriptive-normative gap",
     "olgu ve değer ayrımı", "değer yargısı ayrımı"],
    ["künye", "rapor künyesi", "rapor kimliği", "rapor başlığı",
     "identification", "metadata", "report id", "report metadata",
     "rapor no", "rapor numarası", "girdi kaydı", "kaynak sayfası",
     "rapor bilgileri", "bilgi kutusu", "info box", "rapor künyesi",
     "rapor tanıtım", "adım 00", "adim 00", "step 00", "giriş bilgileri"],
    ["güven düzeyi", "confidence level", "guven duzeyi"],
    ["bilgi düzeyi", "knowledge level", "bilgi duzeyi"],
]

# v5.2.0 — Katman 3 ek zorunlu bölümler
KATMAN3_EK_ZORUNLU = [
    ["zaman aralığı", "zaman araligi", "time range", "time window",
     "time period", "zaman penceresi", "yıllık pencere", "yillik pencere"],
    ["endeks", "index", "veri kaynağı", "veri kaynagi", "data source",
     "veri tabanı", "veri tabani", "database", "dünya bankası",
     "dunya bankasi", "world bank", "tüik", "undp", "gini", "transparency",
     "hukukun üstünlüğü", "rule of law"],
    ["sayısal eşik", "sayisal esik", "numerical threshold",
     "quantitative threshold", "eşiği", "esigi", "threshold",
     "eşik değeri", "esik degeri"],
    ["prior", "prior", "önsel", "öncül", "oncul", "önceki olasılık",
     "onceki olasilik", "başlangıç olasılığı", "baslangic olasiligi"],
    ["posterior", "posterior", "sonsal", "güncellenmiş olasılık",
     "guncellenmis olasilik", "güncel olasılık", "sonraki olasılık"],
    ["bayes", "bayes", "bayesian", "bayesyen", "bayesçi", "bayesci",
     "olasılık güncelleme", "olasilik guncelleme"],
]

# v5.2.0 — H6 Zorlu Âyet raporları için ek zorunlu
H6_EK_ZORUNLU = [
    ["3'lü dil matrisi", "3-lu dil matrisi", "triple linguistic matrix",
     "üçlü dil matrisi", "uc lu dil matrisi", "üclü dil matrisi",
     "3 lu dil matrisi", "uc'lü dil matrisi"],
    ["ibn fâris", "ibn faris", "ibn fāris", "maqayis", "makayis",
     "makayisu'l-luga", "makayisul luga", "maqāyīs", "mufradat",
     "müfredat", "mufredat", "isfahani", "isfahâni"],
    ["ibn manzûr", "ibn manzur", "lisanu'l-arab", "lisanul arab",
     "lisan al-arab", "lisanül-arab", "lisânü'l-arab", "lisān",
     "ibn manzur", "ibn menzur", "ibn manzûr"],
]


# ============================================
# UYARI KELİMELERİ — Dikkat Gerektirir
# (v5.1.6 + v5.2.0 yenileri)
# ============================================
UYARI_KELIMELERI = {
    "doğrulandı": "Retrodiction sonucu — 'Kısmen' ile birlikte kullanıldı mı kontrol et",
    "sabit": "Bilgi tabanı — katmanlı mı (İlke/Uygulama) kontrol et",
    ">%": "Sayısal olasılık — Bölüm 9 kapsamına giriyor mu kontrol et",
    # --- v5.2.0 Yeni ---
    "ampirik olarak sabit": "Somut veri kaynağı belirtilmeli (v5.2.0 Test 7b)",
    "genel olarak bilinmektedir": "Somut veri kaynağı belirtilmeli (v5.2.0 Test 7b)",
    "empirically established": "Somut veri kaynağı belirtilmeli (v5.2.0 Test 7b)",
    "well established": "Somut veri kaynağı belirtilmeli (v5.2.0 Test 7b)",
}


# ============================================
# YAZIM HATALARI
# (v5.1.6 + v5.2.0 genişletmeleri)
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
    # --- v5.2.0 Yeni ---
    "ibn fâris": "İbn Fâris (büyük harfle başlamalı)",
    "ibn manzur": "İbn Manzûr (büyük harfle başlamalı)",
    "ibn manzûr": "İbn Manzûr (büyük harfle başlamalı)",
    "beccaria": "Beccaria (büyük harfle başlamalı)",
    "de soto": "De Soto (büyük harfle başlamalı)",
    "şatibî": "Şâtıbî",
    "shatibi": "Shāṭibī",
    "ibnu'l-kayyim": "İbnü'l-Kayyim",
    "ibn kayyim": "İbnü'l-Kayyim",
}


# ============================================
# FALSIFİABİLİTE STANDARDI KONTROLÜ (v5.2.0 Değişiklik 2)
# ============================================
FALSIF_KRITERLERI = {
    "zaman aralığı": ["zaman aralığı", "zaman penceresi", "yıl", "yıllık",
                       "time range", "time window", "year", "annual",
                       "pencere", "window", "dönem", "period"],
    "endeks/kaynak": ["endeks", "index", "veri kaynağı", "data source",
                       "veri tabanı", "database", "dünya bankası", "world bank",
                       "tüik", "undp", "gini", "transparency",
                       "hukukun üstünlüğü", "rule of law"],
    "sayısal eşik": ["≥ %", ">= %", "eşik", "threshold", "eşiği",
                      "≥ 0", ">= 0", "puan", "score", "oran", "rate"],
}


def falsifiabilite_kontrol(metin_norm):
    """Falsifiabilite standardı kontrolü (v5.2.0)."""
    eksikler = []
    for kriter, ifadeler in FALSIF_KRITERLERI.items():
        bulundu = any(normalize(i) in metin_norm for i in ifadeler)
        if not bulundu:
            eksikler.append(kriter)
    return eksikler


# ============================================
# ANA TARAMA FONKSİYONU
# ============================================
def tara(dosya_adi, katman=3, h6=False):
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
    muaf_sayisi = 0
    eksik_bolumler = []

    # Normalize edilmiş istisna listesi
    istisna_norm = [normalize(i) for i in ISTISNA_IFADELERI]

    # --- 1. Yasaklı kelime taraması (hard fail + 18.1-B muafiyet) ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_norm = normalize(satir)

        # Öz-denetim satırı mı?
        if any(isaret in satir_norm for isaret in oz_denetim_norm):
            continue

        for yasakli, aciklama in YASAKLI_KELIMELER.items():
            yasakli_norm = normalize(yasakli)
            if yasakli_norm in satir_norm:
                # v5.2.0 — 18.1-B Muafiyet: tırnak içinde mi?
                if citirnak_muaf_mi(satir, yasakli):
                    muaf_sayisi += 1
                    continue

                yasak_sayisi += 1
                bulgular.append({
                    "tur": "YASAKLI",
                    "satir": satir_no,
                    "kelime": yasakli,
                    "aciklama": aciklama,
                })

    # --- 2. Koşullu yasaklı (mutlak/absolute) + tırnak muafiyeti ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_norm = normalize(satir)

        if any(isaret in satir_norm for isaret in oz_denetim_norm):
            continue

        for kosullu, aciklama in KOSULLU_YASAKLI.items():
            kosullu_norm = normalize(kosullu)
            if kosullu_norm in satir_norm:
                # v5.2.0 — Tırnak muafiyeti
                if citirnak_muaf_mi(satir, kosullu):
                    muaf_sayisi += 1
                    continue

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
            # "retroadiction" kontrolü: retroadiction geçerli olabilir
            if yanlis == "retroadiction" and "retrodiction" in metin_birlesik:
                continue
            # v5.2.1 — "beccaria" / "de soto" / "şatibî" kontrolü:
            # Raporda zaten doğru yazılıp yazılmadığını kontrol et
            if yanlis == "beccaria":
                # "Beccaria" (büyük harfle) zaten varsa uyarı verme
                if re.search(r'[Bb]eccaria', "".join(satirlar)):
                    # Büyük harfle başlıyor mu kontrol et
                    for s in satirlar:
                        if "Beccaria" in s:
                            continue_flag = True
                            break
                    else:
                        continue_flag = False
                    if continue_flag:
                        continue
            if yanlis == "de soto":
                if "De Soto" in "".join(satirlar):
                    continue
            if yanlis == "şatibî":
                if "Şâtıbî" in "".join(satirlar):
                    continue

            yazim_hata_sayisi += 1
            bulgular.append({
                "tur": "YAZIM",
                "satir": "-",
                "kelime": yanlis,
                "aciklama": f"Olması gereken: '{dogru}'",
            })

    # --- 4. Diğer uyarı kelimeleri + tırnak muafiyeti ---
    for satir_no, satir in enumerate(satirlar, 1):
        satir_norm = normalize(satir)
        for uyari, aciklama in UYARI_KELIMELERI.items():
            uyari_norm = normalize(uyari)
            if uyari_norm in satir_norm:
                # v5.2.0 — Tırnak muafiyeti
                if citirnak_muaf_mi(satir, uyari):
                    continue
                uyari_sayisi += 1
                bulgular.append({
                    "tur": "UYARI",
                    "satir": satir_no,
                    "kelime": uyari,
                    "aciklama": aciklama,
                })

    # --- 5. Zorunlu bölüm kontrolü (iki dilli + v5.2.1 genişletmeleri) ---
    for bolum_cift in ZORUNLU_BOLUMLER:
        bulundu = any(normalize(bolum) in metin_birlesik for bolum in bolum_cift)
        if not bulundu:
            eksik_bolumler.append(bolum_cift[0])

    # --- 6. Katman 3 ek zorunlu bölümler (v5.2.0 + v5.2.1) ---
    if katman >= 3:
        for bolum_cift in KATMAN3_EK_ZORUNLU:
            bulundu = any(normalize(b) in metin_birlesik for b in bolum_cift)
            if not bulundu:
                eksik_bolumler.append(f"[K3] {bolum_cift[0]}")

    # --- 7. H6 ek zorunlu bölümler (v5.2.0 + v5.2.1) ---
    if h6:
        for bolum_cift in H6_EK_ZORUNLU:
            bulundu = any(normalize(b) in metin_birlesik for b in bolum_cift)
            if not bulundu:
                eksik_bolumler.append(f"[H6] {bolum_cift[0]}")

    # --- 8. Falsifiabilite standardı kontrolü (v5.2.0) ---
    fals_eksikler = falsifiabilite_kontrol(metin_birlesik)

    # ============================================
    # SONUÇ RAPORU
    # ============================================
    print("=" * 60)
    print("   GEM LINTER v5.2.1 — Dil Güvenliği Denetim Raporu")
    print(f"   Dosya: {dosya_adi}")
    print(f"   Katman: {katman} | H6: {'Evet' if h6 else 'Hayır'}")
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

    if muaf_sayisi > 0:
        print(f"📋 MUAFİYET (18.1-B): {muaf_sayisi} tırnak içi kullanım muaf sayıldı.")
        print()

    if eksik_bolumler:
        print("📋 EKSİK ZORUNLU BÖLÜMLER:")
        print("-" * 60)
        for e in eksik_bolumler:
            print(f"  ❌ '{e}' bölümü bulunamadı.")
        print()

    if fals_eksikler:
        print("📋 FALSIFİABİLİTE STANDARDI (v5.2.0 Değişiklik 2):")
        print("-" * 60)
        for f_item in fals_eksikler:
            print(f"  ⚠️ '{f_item}' unsuru eksik.")
        print()

    # --- Nihai karar ---
    print("=" * 60)
    # Karar hard fail'lere bakar; uyarılar ve eksik bölümler karara etki etmez
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
    elif fals_eksikler:
        karar = "🟡 GEÇTİ (Şartlı)"
        gerekce = "Falsifiabilite standardı eksik. v5.2.0 Değişiklik 2 gereği tamamlanmalı."
    else:
        karar = "🟢 GEÇTİ"
        gerekce = "Temel kontroller geçti. Red Team incelemesi önerilir."

    print(f"  SONUÇ: {karar}")
    print(f"  Gerekçe: {gerekce}")
    print(f"  Yasaklı kelime: {yasak_sayisi}")
    print(f"  Muaf (18.1-B): {muaf_sayisi}")
    print(f"  Yazım hatası: {yazim_hata_sayisi}")
    print(f"  Uyarı: {uyari_sayisi}")
    print(f"  Eksik bölüm: {len(eksik_bolumler)}")
    print(f"  Falsifiabilite eksik: {len(fals_eksikler)}")
    print("=" * 60)

    # Çıkış kodu
    if yasak_sayisi > 0:
        sys.exit(2)   # DÜŞTÜ
    elif toplam_sorun > 0 or fals_eksikler:
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
        print()
        print("Seçenekler:")
        print("  --katman 3    Katman 3 ek zorunlu bölümler (Bayes, Falsifiabilite)")
        print("  --h6          Zorlu Âyet (H6) ek zorunlu bölümler (3'lü Dil Matrisi)")
        print()
        print("Örnek:   python gem_lint.py ornek-006-maide-538.md --katman 3 --h6")
        sys.exit(1)

    dosya = sys.argv[1]
    katman = 3
    h6 = False

    # Argümanları işle
    if "--katman" in sys.argv:
        idx = sys.argv.index("--katman")
        if idx + 1 < len(sys.argv):
            try:
                katman = int(sys.argv[idx + 1])
            except ValueError:
                katman = 3

    if "--h6" in sys.argv:
        h6 = True

    tara(dosya, katman=katman, h6=h6)
