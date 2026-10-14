[English](README.md) | **Türkçe**

# GEM — Kur'an Temelli Stratejik Analiz Çerçevesi

> **Bu proje dini otorite iddia etmez.** Çıktılar yorumdur, hüküm değildir.
> Kehanet, fetva veya kesin tarih iddiası taşımaz.

---

## İçindekiler

- [Bu proje nedir?](#bu-proje-nedir)
- [Ne yapar?](#ne-yapar)
- [Ne yapmaz?](#ne-yapmaz)
- [Yayımlanan GEM v6.1.1 Raporları (Külliyat)](#yayımlanan-gem-v611-raporları-külliyat)
- [Sürümler ve Rehberler](#sürümler-ve-rehberler)
- [Dosyalar](#dosyalar)
- [Hızlı Başlangıç](#hızlı-başlangıç)

---

## Bu proje nedir?

GEM (Gelecek Eksenli Muhakeme), Kur'an ayetlerini **stratejik analiz** yöntemleriyle
inceleyen, **26 adımlı** ve **5 makro fazlı** bir düşünce ve denetim çerçevesidir.

### Ne yapar?
- Âyet metnini **dilbilimsel** olarak analiz eder (siyak-sibak, nüzul, hitap, 4'lü lügat matrisi).
- **Makasıd** (yüksek amaçlar) çıkarır.
- Çağdaş kriz ve meselelerle **eşleştirir**.
- **Senaryo** üretir (4 yapısal olasılık).
- **Karar kolları** önerir (uygulanabilir politika ve kaldıraç noktaları).
- Kendi analizini **eleştirir** (Red Team, ampirik falsifiabilite, öz-denetim, önyargı filtreleri).

### Ne yapmaz?
- Fetva vermez.
- Dini otorite veya nihai hakikat iddiası taşımaz.
- Gaybı veya geleceği mutlak olarak tahmin etmez.
- Kesin kazi hüküm üretmez.

---

## Yayımlanan GEM v6.1.1 Raporları (Külliyat)

Aşağıdaki raporlar, GEM v6.1.1 standardına tam uyumlu olarak hazırlanmış ve kriptografik harici manifestlerle doğrulanmıştır:

| No | Âyet | Konu Başlığı | Rapor Dosyası | Durum |
|:---:|:---:|:---|:---|:---:|
| **01** | **Tevbe 9:5** | Ahit İhlali, Caydırıcılık ve Meşru Savunma Hukuku | [`docs/tr/06-pilot-tevbe-95-v6.1.1.md`](docs/tr/06-pilot-tevbe-95-v6.1.1.md) | `PRE-RELEASE` |
| **02** | **Nisâ 4:34** | Aile İçi Yönetişim, Kavamiyyet ve Şiddetsiz Nasihat Doktrini | [`docs/tr/07-pilot-nisa-434-v6.1.1.md`](docs/tr/07-pilot-nisa-434-v6.1.1.md) | `PRE-RELEASE` |
| **03** | **Mâide 5:38** | Mülkiyet, Hırsızlık Cezası, Zaruret ve Sosyal Güvenlik | [`docs/tr/08-pilot-maide-538-v6.1.1.md`](docs/tr/08-pilot-maide-538-v6.1.1.md) | `PRE-RELEASE` |
| **04** | **Bakara 2:256** | İnanç ve Vicdan Özgürlüğü, İkrâh Yasağı ve Çoğulculuk | [`docs/tr/09-rapor-bakara-2256-v6.1.1.md`](docs/tr/09-rapor-bakara-2256-v6.1.1.md) | `PRE-RELEASE` |
| **05** | **Nisâ 4:58** | Kamu Yönetişimi, Liyakat, Yargı Bağımsızlığı ve Adalet | [`docs/tr/10-rapor-nisa-458-v6.1.1.md`](docs/tr/10-rapor-nisa-458-v6.1.1.md) | `PRE-RELEASE` |
| **06** | **Âl-i İmrân 3:159** | Kriz Yönetişiminde İstişare (Şûrâ), Liderlik ve Azim | [`docs/tr/11-rapor-ali-imran-3159-v6.1.1.md`](docs/tr/11-rapor-ali-imran-3159-v6.1.1.md) | `PRE-RELEASE` |
| **07** | **Hucurât 49:9–10** | Çatışma Çözümü, Uluslararası Tahkim, Bağy Hukuku ve Barış Gücü | [`docs/tr/12-rapor-hucurat-49910-v6.1.1.md`](docs/tr/12-rapor-hucurat-49910-v6.1.1.md) | `PRE-RELEASE` |

---

## Sürümler ve Rehberler

- **v6.1.1 (Güncel Standart):** [docs/tr/GEM-v6.1.1-taslak.md](docs/tr/GEM-v6.1.1-taslak.md) — 26 adım, 5 makro faz, Enfüs-Âfâk ve Kalp Fıkhı merceği, kaynak tahkiki ve sınır beyanı.
- **Akademik Hakem Rehberi:** [docs/tr/akademik-hakem-rehberi.md](docs/tr/akademik-hakem-rehberi.md) — 5 boyutlu hakemlik inceleme rubriği ve Z-5 formu.
- **Yol Haritası:** [docs/tr/GEM-v6.1.1-yol-haritasi.md](docs/tr/GEM-v6.1.1-yol-haritasi.md) — GitHub geçiş ve test planı.
- **Linter Kuralları:** [docs/tr/linter-kurallari.md](docs/tr/linter-kurallari.md) — Biçimsel denetim kural rehberi.
- **Değişiklik Kütüğü:** [CHANGELOG.md](CHANGELOG.md) — Sürüm tarihçesi.
- **v5.2.0 (Arşiv):** [GEM-V520-TALIMAT.md](GEM-V520-TALIMAT.md) — Tarihsel sürüm kaydı.

---

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `YONTEM.md` | 26 adımlı yöntemin özeti ve 5 makro faz yapısı |
| `src/gem_lint.py` | Biçimsel dil, şema ve manifest denetçisi (Python) |
| `docs/tr/05-ornek-rapor-v6.1.1.md` | Resmi v6.1.1 rapor şablonu |
| `docs/tr/GEM-v6.1.1-taslak.md` | Güncel v6.1.1 metodoloji standardı |
| `docs/tr/akademik-hakem-rehberi.md` | Bağımsız dış hakemlik değerlendirme kılavuzu |

---

## Hızlı Başlangıç

```bash
# Şablonu veya raporları denetle
python src/gem_lint.py docs/tr/05-ornek-rapor-v6.1.1.md --katman 3 --h6
python src/gem_lint.py docs/tr/11-rapor-ali-imran-3159-v6.1.1.md --katman 3 --h6

# Test paketini çalıştır
pytest tests/ -v
```
