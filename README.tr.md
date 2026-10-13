[English](README.md) | **Türkçe**

# GEM — Kur'an Temelli Stratejik Analiz Çerçevevesi

> **Bu proje dini otorite iddia etmez.** Çıktılar yorumdur, hüküm değildir.
> Kehanet, fetva veya kesin tarih iddiası taşımaz.

---

## Bu proje nedir?

GEM (Gelecek Eksenli Muhakeme), Kur'an ayetlerini **stratejik analiz** yöntemleriyle
inceleyen, **26 adımlı** bir düşünce ve denetim çerçevesidir.

### Ne yapar?
- Ayet metnini **dilbilimsel** olarak analiz eder (siyak-sibak, nüzul, hitap)
- **Makasıd** (amaçlar) çıkarır
- Çağdaş sorunlarla **eşleştirir**
- **Senaryo** üretir (4 olasılık)
- **Karar kolu** önerir (10 alanlı)
- Kendi analizini **eleştirir** (Red Team, falsifiabilite, öz-denetim)

### Ne yapmaz?
- Fetva vermez
- Dini otorite iddia etmez
- Geleceği tahmin etmez
- Kesin hüküm vermez

---

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `YONTEM.md` | 26 adımlı yöntemin özeti |
| `gem_lint.py` | Dil güvenliği denetçisi (Python) |
| `ornek-rapor.md` | Rapor şablonu |

---

## Hızlı Başlangıç

```bash
# Dil denetçisini çalıştır
python gem_lint.py ornek-rapor.md
