[English](README.md) | **Türkçe**

# GEM — Kur'an Temelli Stratejik Analiz Çerçevesi

> **Bu proje dini otorite iddia etmez.** Çıktılar yorumdur, hüküm değildir.
> Kehanet, fetva veya kesin tarih iddiası taşımaz.

---

## İçindekiler

- [Bu proje nedir?](#bu-proje-nedir)
- [Ne yapar?](#ne-yapar)
- [Ne yapmaz?](#ne-yapmaz)
- [Sürümler ve Belgeler](#sürümler-ve-belgeler)
- [Dosyalar](#dosyalar)
- [Hızlı Başlangıç](#hızlı-başlangıç)

---

## Bu proje nedir?

GEM (Gelecek Eksenli Muhakeme), Kur'an ayetlerini **stratejik analiz** yöntemleriyle
inceleyen, **26 adımlı** ve **5 makro fazlı** bir düşünce ve denetim çerçevesidir.

### Ne yapar?
- Âyet metnini **dilbilimsel** olarak analiz eder (siyak-sibak, nüzul, hitap, lügat matrisi).
- **Makasıd** (yüksek amaçlar) çıkarır.
- Çağdaş kriz ve meselelerle **eşleştirir**.
- **Senaryo** üretir (4 olasılık).
- **Karar kolları** önerir (uygulanabilir politika ve kaldıraç noktaları).
- Kendi analizini **eleştirir** (Red Team, ampirik falsifiabilite, öz-denetim, önyargı filtreleri).

### Ne yapmaz?
- Fetva vermez.
- Dini otorite veya nihai hakikat iddiası taşımaz.
- Gaybı veya geleceği mutlak olarak tahmin etmez.
- Kesin kazi hüküm üretmez.

---

## Sürümler ve Belgeler

- **v6.1.1 (Güncel Taslak):** [docs/tr/GEM-v6.1.1-taslak.md](docs/tr/GEM-v6.1.1-taslak.md) — 26 adım, 5 makro faz, Enfüs-Âfâk ve Kalp Fıkhı merceği, kaynak tahkiki ve sınır beyanı.
- **Yol Haritası:** [docs/tr/GEM-v6.1.1-yol-haritasi.md](docs/tr/GEM-v6.1.1-yol-haritasi.md) — GitHub geçiş ve test planı.
- **Değişiklik Kütüğü:** [CHANGELOG.md](CHANGELOG.md) — Sürüm tarihçesi.
- **v5.2.0 (Arşiv):** [GEM-V520-TALIMAT.md](GEM-V520-TALIMAT.md) — Tarihsel sürüm kaydı.

---

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `YONTEM.md` | 26 adımlı yöntemin özeti ve faz yapısı |
| `src/gem_lint.py` | Biçimsel dil ve şablon denetçisi (Python) |
| `docs/tr/04-ornek-rapor.md` | Tarihsel rapor şablonu (v5.2.0) |
| `docs/tr/GEM-v6.1.1-taslak.md` | Güncel v6.1.1 metodoloji standardı |
| `docs/tr/GEM-v6.1.1-yol-haritasi.md` | Uygulama ve entegrasyon yol haritası |

---

## Hızlı Başlangıç

```bash
# Biçimsel denetçiyi çalıştır
python src/gem_lint.py docs/tr/04-ornek-rapor.md
```
