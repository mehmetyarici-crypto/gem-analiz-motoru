# GEM Linter (v6.2.1) — Kural ve Denetim Rehberi

Bu belge, `src/gem_lint.py` tarafından uygulanan biçimsel denetim kurallarını, hata seviyelerini, muafiyetleri ve linter'ın sınırlarını açıklar.

---

## 1. Denetim Seviyeleri ve Çıkış Kodları

| Seviye | Çıkış Kodu | Anlamı ve Etkisi |
|---|---|---|
| **KESİCİ (BLOCK)** | `2` | Hard Fail. Kural ihlali vardır; rapor yayımlanamaz, ön sürüm dahi olamaz. |
| **UYARI (WARN)** | `1` | Dikkat gerektiren hususlar veya ön sürüm bildirimleri. `PRE-RELEASE` olarak yayımlanabilir. |
| **GEÇTİ (PASS)** | `0` | Kesici hata ve uyarı yoktur; hakem değerlendirmesine hazır. |

---

## 2. Kural Dizini

### Dil Güvenliği ve Otorite Denetimi
- **L-1801 (KESİCİ):** Yasaklı ifade tespiti (Türkçe: `kesinlikle`, `şüphesiz`, `tartışmasız`, `mükemmel`, `%100`, `sıfır zafiyet`, `ispatlanmıştır`, `onaylandı`; İngilizce: `flawless`, `100%`, `absolutely`, `indisputably`, `zero vulnerability`, `proven`).
- **L-1802 (UYARI):** Koşullu ifade tespiti (`mutlak`, `absolute`). Nass veya teknik bağlam dışında uyarı verir.
- **L-1001 (KESİCİ):** Sahte otorite/onay ifadeleri (`akademik olarak tescillenmiş`, `kusursuz analiz motoru`).

### V1–V11 Metodoloji ve İSNAD 2 Kaynakça Doğrulama Modülleri
- **L-0000 / L-0002 (KESİCİ):** v6.x raporlarında YAML frontmatter eksikliği veya YAML sözdizimi parse hatası.
- **L-0100 / L-0101 (KESİCİ):** V1 Kaynak Kartı eksikliği; klasik kaynaklarda (`classical_sources` / `sources`) müellif ve eser adı zorunludur.
- **L-0102 / L-0103 (UYARI):** Klasik kaynaklarda cilt/sayfa veya dijital tahkik linki eksikliği.
- **L-0104 (KESİCİ):** Çağdaş kaynaklarda (`modern_sources`) yazar/kurum veya eser/rapor başlığı eksikliği.
- **L-0105 (UYARI):** Çağdaş kaynaklarda (`modern_sources`) izlenebilir DOI veya resmi URL bağlantısı eksikliği.
- **L-0106 (UYARI):** Klasik kaynaklarda (`classical_sources`) İSNAD 2 standardı gereği müellif vefat tarihi (`death_year: "ö. H/M"`) eksikliği.
- **L-0201 / L-0202 (KESİCİ):** V2 İhlali; metinde `[NAKİL]` ve `[YORUM]` etiketlerinin bulunmaması.
- **L-0301 (KESİCİ):** V3 İhlali; `Z-2 Görüş İhtilafı Cetveli` eksikliği.
- **L-0302 (KESİCİ):** Yorumu mutlaklaştıran ifadeler (`tek sonuç`, `başka yorum yok`).
- **L-0401 (UYARI):** `PRE-RELEASE` durumunda SHA-256'nın sıfırlardan oluşan yer tutucu olması.
- **L-0402 / L-0403 (KESİCİ):** Nihai yayında sahte/geçersiz hash veya 64 haneli onaltılık olmayan değer.
- **L-0404 (KESİCİ):** Harici `.sha256` manifest dosyasındaki özet ile rapor baytlarının uyuşmaması.
- **L-0502 (KESİCİ):** V5 İhlali; senaryolar için puan gerekçelendirmesinin (`score_justification`) eksik veya yetersiz olması.
- **L-0602 (KESİCİ):** V6 İhlali; ampirik olmayan eşiklerin `[TAHMİNÎ EŞİK]` etiketi taşımaması.
- **L-0701 (UYARI):** V7 İhlali; metinde ampirik veri kurumlarına (Dünya Bankası, WJP, UNESCO, TÜİK, SIPRI vb.) atıf yapıldığı halde izlenebilir URL/DOI veya `modern_sources` kaydının bulunmaması.
- **L-0801 / L-0802 (KESİCİ):** V8 İhlali; Hume Giyotini (is-ought) ve falsifiabilite protokolünün bulunmaması.
- **L-0901 (KESİCİ):** V9 İhlali; `Z-1 Şablona Sığmayan Özgün Problematik` (Aporia) bölümünün bulunmaması.
- **L-1002 (KESİCİ):** V10 İhlali; `Z-4 Standart Sınır Beyanı` bölümünün eksikliği.
- **L-1101 / L-1103 (KESİCİ):** V11 İhlali; `PEER-REVIEWED` / `EXTERNALLY-REVIEWED` statüsünde hakem adı veya hakem değerlendirme raporunun bulunmaması.
- **L-2001 / L-2002 / L-2003 (KESİCİ):** 26 zorunlu analiz adımının, Katman 3 ve H6 bölümlerinin eksikliği.

---

## 3. Muafiyetler (18.1-B ve Bağlam Kuralları)

1. **Tırnak Muafiyeti (18.1-B):** Tırnak içinde (`"..."`, `'...'`, `«...»`, `“...”`) veya satır içi kod bloklarında (`` `...` ``) geçen yasaklı kelimeler alıntı kabul edilir ve ceza uygulanmaz.
2. **Blok Alıntı ve Kaynak Nakli:** `>` ile başlayan blok alıntılar ve `[NAKİL]` satırları klasik metin aktarımı sayıldığından dil filtresinden muaftır.
3. **Öz-Denetim Muafiyeti:** Raporun kendi iç denetiminde geçen `"yasaklı kelime kullanılmamıştır"` gibi negatif bildirimler muaf tutulur.
4. **Bağlamsal İstisnalar:**
   - **Teolojik ve Epistemik Sınır Bağlamı:** `mutlak mülkiyet`, `mutlak adalet`, `mutlak nass`, `mutlaklaştırılamaz`, `mutlaklaştırma`, `absolute divine` vb.
   - **Teknik Bağlam:** `absolute path`, `absolute threshold`, `absolute import`, `mutlak yol`.

---

## 4. Linter'ın Yapabildikleri ve Sınırları

### Linter Ne Yapar?
- Dosya biçimini, YAML alan tiplerini ve şema gerekliliklerini doğrular.
- Belirlenmiş 26 adım ve eklerin metinde mevcut olup olmadığını kontrol eder.
- Dil güvenliği ve kendi kendini onaylama yasağına uyumu tarar.
- Kriptografik SHA-256 bütünlüğünü harici manifest veya frontmatter üzerinden hesaplar.
- İki rapor arasındaki çapraz benzerlik (Cross-Similarity) oranını ölçer.

### Linter Ne Yapmaz?
- **Tefsir Doğrulaması Yapmaz:** Bir tefsir çıkarımının dinî veya akademik doğruluğunu denetleyemez.
- **Kaynak Sıhhati Denetlemez:** Verilen bir Arapça ibarenin veya matbu sayfa numarasının asıl kitapta gerçekten olup olmadığını teyit edemez (bunun için uzman hakem gerekir).
- **Bilimsel Onay Vermez:** Linter'dan 0 hata ile geçmek, bir çalışmanın "bilimsel olarak kanıtlandığı" anlamına gelmez; yalnızca biçimsel ve yapısal standartlara uyduğunu gösterir.
