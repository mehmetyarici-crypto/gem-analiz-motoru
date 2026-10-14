# Değişiklik Geçmişi (Changelog)

Bu belgede GEM (Kur'an Temelli Gelecek Vizyonu) çerçevesinin sürüm değişiklikleri belgelenmektedir.

---

## [v6.2.0] — 2026-10-15 (Stratejik Külliyat / Corpus Release)

### Eklenen ve Güncellenen Hususlar
- **11 Raporluk Tam Stratejik Külliyat (Corpus Expansion):** GEM v6.1.1 standardına tam uyumlu, 26 adımlı, Katman 3 ve H6 Zorlu Âyet denetimlerinden 0 KESİCİ (BLOCK) hata ile geçmiş 11 resmi rapor yayımlandı:
  1. `06-pilot-tevbe-95-v6.1.1.md`: Ahit İhlali, Caydırıcılık ve Meşru Savunma Hukuku
  2. `07-pilot-nisa-434-v6.1.1.md`: Aile İçi Yönetişim, Kavamiyyet ve Şiddetsiz Nasihat
  3. `08-pilot-maide-538-v6.1.1.md`: Mülkiyet, Hırsızlık Cezası, Zaruret ve Sosyal Güvenlik
  4. `09-rapor-bakara-2256-v6.1.1.md`: İnanç ve Vicdan Özgürlüğü, İkrâh Yasağı ve Çoğulculuk
  5. `10-rapor-nisa-458-v6.1.1.md`: Kamu Yönetişimi, Liyakat, Yargı Bağımsızlığı ve Adalet
  6. `11-rapor-ali-imran-3159-v6.1.1.md`: Kriz Dönemlerinde İstişare (Şûrâ), Liderlik ve Azim
  7. `12-rapor-hucurat-49910-v6.1.1.md`: Çatışma Çözümü, Uluslararası Tahkim, Bağy Hukuku ve Barış Gücü
  8. `13-rapor-isra-1736-v6.1.1.md`: Epistemik Sorumluluk, Bilgi Doğrulama, Bilişsel Güvenlik ve Yapay Zekâ
  9. `14-rapor-hasr-597-v6.1.1.md`: Servet Konsantrasyonu, İktisadi Sirkülasyon ve Anti-Oligarşi
  10. `15-rapor-rum-3022-v6.1.1.md`: Ontolojik Çoğulculuk, Dilsel/Etnik Çeşitlilik ve Birlikte Yaşama
  11. `16-rapor-enam-6151152-v6.1.1.md`: Evrensel Ahlak Dekalogu, Temel Haklar, Mîzân ve Adli Tarafsızlık
- **Akademik Hakem Rehberi ve Değerlendirme Rubriği:** 5 boyutlu (Metin/Tahkik, Sosyo-Politik/Kriz, Dil Güvenliği, Falsifiabilite/Hume Giyotini, Kurumsal Tasarım/Özgünlük), her biri 20 puanlık resmi değerlendirme kılavuzu (`docs/tr/akademik-hakem-rehberi.md`) sisteme eklendi.
- **Çapraz Platform Kriptografik Bütünlük (.gitattributes & LF Normalizasyonu):** Windows (CRLF) ile Linux (LF) ortamları arasındaki satır sonu uyuşmazlığını gideren `.gitattributes` yapılandırması ve hem ham bayt hem evrensel LF hash doğrulama motoru `gem_lint.py` içine entegre edildi.
- **Linter & Test Otomasyonu:** Katman 3 + H6 gereksinimleri, yasaklı kelime filtreleri ve harici manifest üretim/denetim mekanizmaları %100 test kapsamıyla güvenceye alındı.

---

## [v6.1.1] — 2026-10-15 (Taslak / Standard Draft)

### Eklenen ve Güncellenen Hususlar
- **Adım 13 (Enfüs-Âfâk ve Kalp Fıkhı):** İçsel-ahlakî yöneliş (enfüs) ile toplumsal/kurumsal şartlar (âfâk) analitik mercekle ayrıştırıldı. “Kalp fıkhı” niyet, vicdan ve ahlaki muhasebe merceği olarak tanımlandı; fetva veya müstakil fıkıh iddiası taşımadığı belirtildi.
- **İşârî / Tasavvufî Tevil Sınırı:** İşârî tevilin ancak güvenilir kaynak ve yöntem bulunduğunda kullanılabileceği, fıkhî hüküm ve ampirik politika ile aynı statüde sayılamayacağı açıklandı.
- **Kod Standardizasyonu:** Siyak-sibak kodları `S1–S7` olarak sabitlendi; Erken Uyarı kodları `EU-01..EU-n` biçiminde tekleştirilerek nüzul `N4` koduyla karışması önlendi.
- **Beş Makro Faz:** 26 adımın okunabilirliğini artırmak üzere 5 Makro Faz (Faz I–V) tanımlandı; adımların içeriğinin yerini almadığı belirtildi.
- **Kriptografik Bütünlük (Manifest Mimarisi):** SHA-256 hash özetinin dosyanın kendi içine yazılma paradoksu giderildi; özetin harici `.sha256` manifestinde veya release kaydında tutulması ilkesi getirildi.
- **Yayın Statüleri:** `DRAFT`, `PRE-RELEASE`, `EXTERNALLY-REVIEWED` statüleri ve dış hakem inceleme koşulları netleştirildi.

---

## [v6.0.0] — 2026-10-14 (Mimari Reform)

### Eklenen ve Güncellenen Hususlar
- **V1–V11 Doğrulama Modülleri:** Akademik ve metodolojik kalite gereklilikleri sisteme eklendi.
- **Filolojik Tahkik (`[NAKİL]` / `[YORUM]`):** Klasik ibare ile modern analist çıkarımının katı biçimde ayrılması zorunlu kılındı.
- **Hermenevtik Çoğulculuk (Z-2):** En az 3 farklı klasik mezhep ve çağdaş ekolü içeren Görüş İhtilafı Cetveli zorunlu hale getirildi.
- **Aporia ve Problem Karşılama (Z-1):** Şablona sığmayan teolojik gerilim ve açık aporiaların dürüstçe tartışılması kuralı getirildi.
- **Hume Giyotini ve Sınırlandırılmış Yanlışlanabilirlik (V8):** İlahi nassın ampirik teste tabi tutulması kategorik hatası düzeltildi; Popperci yanlışlanabilirlik yalnızca dünyevî yönetim/politika hipotezlerine bağlandı.
- **Epistemik Dürüstlük (Z-4, Z-5):** Yapay "Sınıf A / Onaylandı" etiketleri yasaklandı; standart sınır beyanı ve bağımsız hakem kayıt protokolü getirildi.
- **Yapılandırılmış Metaveri:** YAML frontmatter formatı ile makine tarafından okunabilir metaveri yapısı kuruldu.

---

## [v5.2.0] — Tarihsel Sürüm (Arşiv)

- 26 adımlı tam analiz motoru (Katman 3), 3'lü çerçeve (Ethos/Logos/Pathos), erken uyarı sinyalleri ve karar kolları kurgulandı.
- `GEM-V520-TALIMAT.md` tarihsel referans olarak arşivde muhafaza edilmektedir.
