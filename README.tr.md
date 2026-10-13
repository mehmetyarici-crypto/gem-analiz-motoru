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

## İçindekiler

- [Metodoloji (Türkçe)](YONTEM.md)
- [Methodology (English)](METHOD.md)
- [Örnek 004 — Tevbe 9:5 (Türkçe)](docs/tr/01-ornek-004-tevbe-95.md)
- [Example 004 — Tawbah 9:5 (English)](docs/en/example-004-tawbah-95.md)
- [Örnek 005 — Nisâ 4:34 (Türkçe)](docs/tr/02-ornek-005-nisa-434.md)
- [Example 005 — Nisā 4:34 (English)](docs/en/example-005-nisa-434.md)
- [Örnek 006 — Mâide 5:38 (Türkçe)](docs/tr/03-ornek-006-maide-538.md)
- [Example 006 — Māʾida 5:38 (English)](docs/en/example-006-maide-538.md)
- [Rapor Şablonu (Türkçe)](docs/tr/04-ornek-rapor.md)
- [Report Template (English)](docs/en/example-report-template.md)
- [gem_lint.py](src/gem_lint.py)

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
```
