# GEM v6.1.1 — GitHub ve Uygulama Yol Haritası

- **Hazırlanma tarihi:** 15 Ekim 2026
- **Amaç:** v6.1.1 metodoloji taslağını quran-vision deposuna güvenli, izlenebilir ve test edilebilir biçimde taşımak.
- **Durum:** Plan. GitHub'da değişiklik yapılmadı; push, merge veya release gerçekleştirilmedi.
- **Kapsam:** Dokümantasyon, örnek rapor, linter, testler, CI ve sürümleme.

## 1. Mevcut durum

| Alan | 15 Ekim 2026 itibarıyla görülen durum | Sonuç |
|---|---|---|
| GitHub `main` | v5.2.0 tam talimatı mevcut; son görülen commit `67730bf` | v6.1.1 henüz GitHub'da yayımlı değil. |
| Açık PR #2 | Türkçe README yolları ve içindekiler güncellemesi; taslak | Dosya yolları/komutlar gözden geçirilip kontroller çalıştırılmadan merge edilmemeli. |
| Açık PR #3 | Linter'a İngilizce yasaklı terimler ekleme; taslak | `absolute` bağlam istisnası ve yerel linter değişikliğiyle çakışma incelenmeli. |
| Yerel `quran-vision` klonu | `main` ile `origin/main` aynı; `src/gem_lint.py` değiştirilmiş | **Kullanıcı değişikliği.** Commit, reset, checkout veya üzerine yazma yapılmamalı. Önce yedek/diff kaydı ve kullanıcının kararı gerekir. |
| v6.1.1 standardı | Üst çalışma alanındaki `docs/KUR_AN_TEMELLI_GELECEK_VIZYONU_GEM_v6.1.1.md` içinde | Dosya `quran-vision` klonunun dışında; GitHub PR'ına kendiliğinden girmez. |
| Test/CI | Yerel klonun görünen proje ağacında test ve workflow dosyası bulunmuyor | Linter değişiklikleri için otomatik güvence henüz tanımlı değil. |
| README | Dosya tablosu `src/gem_lint.py` derken hızlı başlangıç `python gem_lint.py` diyor | Tek kanonik komut/yol belirlenmeli; İngilizce README de eşlenmeli. |

GitHub durumu değişebileceğinden PR numarası ve main commit'i işleme başlamadan yeniden doğrulanmalıdır.

## 2. Karar ilkeleri

1. `main` dalına doğrudan yazılmaz; her değişiklik ayrı branch ve PR ile sunulur.
2. Mevcut `src/gem_lint.py` değişikliği kullanıcıya aittir. İncelenmeden geri alınmaz, başka commit'e karıştırılmaz ve PR #3 ile otomatik birleştirilmez.
3. Metodoloji belgesi, linter, şablon ve örnek rapor aynı anda v6.1.1 uyumlu ilan edilmez. Her bileşenin durumu ayrı gösterilir.
4. Linter sonucu yalnızca tanımlı biçimsel kontrolleri ifade eder; tefsir doğruluğu, kaynak tahkiki veya hakem bağımsızlığı onayı değildir.
5. `GEM-V520-TALIMAT.md` tarihsel v5.2.0 kaydı olarak korunur. Güncel sürüme geçiş README ve sürüm dizini üzerinden gösterilir.
6. Yeni hakem, veri tabanı, hash veya akademik onay bilgisi doğrulanmadıkça örnek/yer tutucu değerler gerçek kayıt gibi yayımlanmaz.

## 3. Aşamalar ve kabul ölçütleri

### Aşama 0 — Çalışma ağacını koru

**İşler**

- `git -C quran-vision status --short --branch`, `git diff -- src/gem_lint.py` ve açık PR durumunu kaydet.
- Kullanıcının linter değişikliğinin bir kopyasını veya patch kaydını al; yalnızca kullanıcı onayıyla commit/branch işlemi yap.
- PR #2 ve #3'ün güncel head/base commit'lerini, değişen dosyalarını ve kontrollerini karşılaştır.

**Kabul ölçütü:** Mevcut kullanıcı diff'i kaybolmadan korunmuş; hangi dosyanın hangi PR'a ait olduğu açık.

### Aşama 1 — v6.1.1 dokümantasyon PR'ı

**Önerilen branch:** `docs/gem-v6.1.1-standard`

**Repo içine eklenecek/güncellenecek dosyalar**

- `docs/tr/GEM-v6.1.1-taslak.md`: v6.1.1 standardı; üst çalışma alanındaki belge gözden geçirilip bu konuma aktarılır.
- `docs/tr/GEM-v6.1.1-yol-haritasi.md`: bu planın repo içindeki sürümü veya PR açıklamasında kısa plan.
- `YONTEM.md` ve `METHOD.md`: yalnızca kısa özet ve sürüm durumu; tam standardı kopyalayıp iki ayrı kaynak yaratmama.
- `README.tr.md` ve `README.md`: güncel v5.2/v6.1.1 taslak durumunu, doğru bağlantıları ve doğru komutu gösterme.
- `CHANGELOG.md` (yoksa): v5.2.0, v6.0.0 ve v6.1.x değişiklik geçmişi; doğrulanmamış yayın iddiası olmadan.

**Kabul ölçütü**

- v6.1.1 belgesi açıkça `DRAFT`/taslak statüsünde.
- Adım 13 enfüs-âfâk ve kalp fıkhı çerçevesinde; v6.1.1 değişikliği ve sınırları belgede mevcut.
- README yolları ve çalıştırma komutu depodaki gerçek dosyalarla eşleşiyor.
- Eski sürüm metinleri geriye dönük değiştirilmiş gibi sunulmuyor.

### Aşama 2 — Linter sözleşmesi ve test paketi

**Branch:** `feat/gem-lint-v6.1`

**Ön koşul:** Aşama 0 tamamlanmalı; kullanıcıya ait yerel linter diff'iyle PR #3 karşılaştırılmalı. Kanonik linter yolu `src/gem_lint.py` olarak kararlaştırılmalı; kök dizindeki/başka klonlardaki kopyalar varsa senkron politikası yazılmalı.

**Eklenecek dosyalar**

- `tests/test_gem_lint.py`: olumlu/olumsuz ve sınır durumu testleri.
- `tests/fixtures/`: geçerli ve hatalı YAML, eksik alan, yanlış hash, alıntı istisnası, sürüm/statü uyuşmazlığı örnekleri.
- `requirements-dev.txt` veya proje standardına uygun test bağımlılık tanımı (`pytest`, YAML kütüphanesi).
- `.github/workflows/tests.yml`: desteklenen Python sürümlerinde test ve sözdizimi kontrolü.
- Gerekirse `docs/tr/linter-kurallari.md`: linter'ın denetlediği ve denetleyemediği hususlar.

**Linter için asgari davranış**

- Sürüm kontrollü YAML şema doğrulaması; hatalar satır/alan bilgisiyle raporlanmalı.
- Hash belirlenmiş kapsamda gerçekten hesaplanmalı ve ayrı manifestle karşılaştırılmalı; hash kendi kendisini içeren değişken alanda tutulmamalı.
- Eksik içerik alanları yalnızca sözcük varlığıyla “geçti” sayılmamalı. Linter semantik doğrulama yapamadığını belirtmeli.
- Çıkış kodları ve durumlar belgelenmeli; format kontrolü “akademik onay” gibi sunulmamalı.
- `absolute/mutlak` gibi koşullu terimler için bağlam istisnaları test edilmeli; kör literal eşleşme kullanılmamalı.

**Kabul ölçütü**

- Testler CI'da desteklenen Python sürümlerinde geçiyor.
- Her kural için beklenen sonuç veren en az bir olumlu ve olumsuz test var; istisna kurallarının sınır testleri mevcut.
- CLI yardım metni, README komutu ve gerçek dosya yolu tutarlı.
- Değişiklik özeti, geriye uyumluluk ve bilinen kısıtlar PR'da yazılı.

### Aşama 3 — v6.1.1 rapor şablonu ve pilot

**Branch:** `docs/gem-v6.1.1-template`

**Dosyalar**

- `docs/tr/05-ornek-rapor-v6.1.1.md`: yeni şablon; mevcut `04-ornek-rapor.md` tarihsel olarak korunur.
- İhtiyaç varsa eşlenik `docs/en/` şablonu; çeviri kontrol edilmeden İngilizce sürüm “eşdeğer standart” ilan edilmez.
- En az bir pilot rapor yalnızca kopya/ayrı dosya olarak hazırlanır; yayımlanmış v5.2 raporunun üzerine yazılmaz.

**Kabul ölçütü**

- 26 adım, koşullu alanlar ve `NOT_VERIFIED` linter durumu şablonda doğru.
- Adım 13 içsel ahlak, dış koşullar ve karar köprüsünü ayırıyor; tasavvufî/işârî yorum kaynak ve yöntemle sınırlı.
- Her kaynak iddiası izlenebilir; doldurulmamış alanlar açıkça placeholder veya “uygulanamaz” olarak kalıyor.
- Pilot linter'dan geçirilmiş ve tüm bulgular insan tarafından değerlendirilmiş; linter sonucu tefsir veya akademik doğruluk onayı diye sunulmamış.

### Aşama 4 — Yayın ve sürümleme kapısı

- Dokümantasyon PR'ı ve linter PR'ı ayrı incelenir; aynı linter dosyasını değiştiren PR'lar karşılaştırılmadan paralel merge edilmez.
- Gerekli review, CI ve README bağlantı kontrolleri tamamlanır.
- Standardın durumu `DRAFT` → `PRE-RELEASE` olarak güncellenebilir; bağımsız inceleme yoksa `EXTERNALLY-REVIEWED` denmez.
- `v6.1.1` tag/release ancak standard, şablon, linter, testler ve changelog aynı sürüm numarası ve uyumluluk beyanıyla hazır olduğunda çıkarılır.
- v5.2.0/v6.0.0 raporları arşivlenir; yeni sürüme taşınan raporlar yeni dosya ve yeni sürüm kaydı alır.

## 4. GitHub PR sırası

1. **PR #2 — README:** taslak branch güncel mi, dosya yolları ve komut doğru mu kontrol et; test/markdown link kontrolünden sonra merge kararı ver.
2. **PR #3 — İngilizce terimler:** kullanıcı diff'iyle karşılaştır; `absolute` koşullu istisnasını ve mevcut Türkçe kuralları bozmayan testleri eklemeden merge etme.
3. **PR A — v6.1.1 standardı:** yalnızca doküman, README bağlantıları ve sürüm özeti.
4. **PR B — linter v6.1:** kod, testler ve CI; PR #3 ile çakışma çözüldükten sonra.
5. **PR C — şablon/pilot:** şablon ve örnek rapor; PR A/B'deki gerçek kuralları temel alır.
6. **Release:** tüm PR'lar ve kabul ölçütleri tamamlandıktan sonra.

PR numaraları değişebileceğinden bunlar sabit görev kimliği değil, 15 Ekim 2026'da görülen mevcut PR'lardır.

## 5. Tamamlanan Dosyalar ve Politikalar (v6.2.1 İtibarıyla)

- [x] `docs/tr/GEM-v6.1.1-taslak.md` ve yöntem özetleri (`YONTEM.md`, `METHOD.md`).
- [x] `docs/tr/05-ornek-rapor-v6.1.1.md` resmi şablonu ve 12 stratejik analiz raporu (`06`–`17`).
- [x] `tests/test_gem_lint.py` (9 birim testi) ve `tests/fixtures/`.
- [x] `requirements-dev.txt` test bağımlılıklarının belgelenmesi.
- [x] `.github/workflows/tests.yml` CI otomasyonu.
- [x] `CHANGELOG.md` sürüm geçmişi (`v5.2.0` -> `v6.0.0` -> `v6.1.1` -> `v6.2.0` -> `v6.2.1`).
- [x] Harici `.sha256` manifest üretme/doğrulama yöntemi ve çapraz platform LF normalizasyonu (`.gitattributes`).
- [x] İki katmanlı İSNAD 2 + Veri Bilimi Hibrit Kaynakça (`classical_sources` + `modern_sources`), `Z-4.5` bölümü ve `L-0104..L-0106` linter kuralları.
- [x] `docs/tr/akademik-hakem-rehberi.md` 5 boyutlu hakem değerlendirme rubriği ve Z-5 kayıt protokolü.
- [x] `README.tr.md`, `README.md`, `YONTEM.md`, `METHOD.md` ve linter komutlarının karşılıklı link kontrolü.

## 6. Kalıcı İlkeler ve Sınırlar

- `GEM-V520-TALIMAT.md` dosyasını v6.1.1 metniyle üzerine yazmamak (tarihsel arşiv olarak korunur).
- Hakem adı, ORCID, veri kaynağı, eşik veya kriptografik imza uydurmamak; dış hakem incelemesi tamamlanana kadar raporları `PRE-RELEASE` statüsünde tutmak.
- Linter'dan 0 KESİCİ hata ile geçmeyi "biçimsel ve yapısal iç tutarlılık" olarak tanımlamak; bağımsız dış hakem onayı yerine ikame etmemek.

## 7. Tamamlanma Durumu

v6.1.1 metodoloji geçişi ve v6.2.1 İSNAD 2 akademik kaynakça standardizasyonu; standart belgesi, şablon, 12 raporluk külliyat, `.sha256` manifestoları, `src/gem_lint.py` denetçisi ve 9/9 pytest test paketiyle tamamlanmış ve `origin/main` üzerinde etiketlenmiştir. Bağımsız dış akademik hakem incelemesi (`EXTERNALLY-REVIEWED`) aşaması açık süreç olarak devam etmektedir.