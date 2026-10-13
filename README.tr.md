[English](README.md) | **Türkçe**

## İçindekiler

- <a>Metodoloji (Türkçe)</a>
- <a>Methodology (English)</a>
- <a>Örnek 004 — Tevbe 9:5 (Türkçe)</a>
- <a>Example 004 — Tawbah 9:5 (English)</a>
- <a>Örnek 005 — Nisâ 4:34 (Türkçe)</a>
- <a>Example 005 — Nisā 4:34 (English)</a>
- <a>Örnek 006 — Mâide 5:38 (Türkçe)</a>
- <a>Example 006 — Māʾida 5:38 (English)</a>
- <a>Rapor Şablonu (Türkçe)</a>
- <a>Report Template (English)</a>
- <a>gem_lint.py</a>

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
| `src/gem_lint.py` | Dil güvenliği denetçisi (Python) |
| `docs/tr/04-ornek-rapor.md` | Rapor şablonu |

---

## Hızlı Başlangıç

```bash
# Dil denetçisini çalıştır
python src/gem_lint.py docs/tr/04-ornek-rapor.md
