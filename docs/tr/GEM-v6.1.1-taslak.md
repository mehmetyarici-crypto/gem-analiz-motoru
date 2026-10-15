# KUR'AN TEMELLİ GELECEK VİZYONU (GEM) — v6.1.1
## Metodoloji, Analiz Mimarisi ve Doğrulama Standardı

- **Sürüm:** `v6.1.1` (Akademik Atıf & İSNAD 2 Genişletmesi: `v6.2.1`)
- **Tarih:** 15 Ekim 2026
- **Önceki sürüm:** `v6.0.0`
- **Kapsam:** Katman 3; 26 analiz adımı, beş makro faz ve Z-1..Z-5 (Z-4.5 Kaynakça dahil) ekleri
- **Durum:** Aktif Standart (`PRE-RELEASE` Külliyat). `src/gem_lint.py` v6.1.1 denetçisi, 9 otomatik birim testi ve 12 stratejik analiz raporu tamamlanmıştır.
- **Geçiş notu:** v6.0.0 korunur; bu belge onun yerine geriye dönük olarak uygulanmaz.

---

## 1. Amaç ve sınırlar

GEM, Kur'an âyetleri üzerine filolojik, tefsirî, usûlî ve ampirik politika analizini düzenleyen bir çalışma çerçevesidir. Bir fetva, bağlayıcı yargı kararı, ilahî muradın tek temsili veya kendi başına akademik hakemlik değildir. Şablona ve linter'a uyum, yorumun doğruluğunu ya da bilimsel geçerliliğini kanıtlamaz.

### Temel ilkeler

1. **Otorite sınırı:** Çıktı analitik bir yorumdur; dinî veya hukuki yetkili karar yerine geçmez.
2. **Determinizm sınırı:** Toplumsal sonuçlar kaçınılmaz kabul edilmez; insan iradesi, kurumlar ve bağlam değerlendirilir.
3. **Epistemik tevazu:** Kesinlik ve kusursuzluk iddiaları kullanılmaz. Kaynak, çıkarım, varsayım ve belirsizlik birbirinden ayrılır.
4. **Rol ayrımı:** Analiz, karşı okuma, kalite kontrol ve dış değerlendirme farklı işlevlerdir. Aynı kişi birden çok işlev üstlenirse bu durum açıklanır; bağımsızlık iddiası kurulmaz.
5. **Olgu-değer ayrımı:** Ampirik bulgular normatif öncülleri tek başına üretmez. Normatif bir yorum ampirik veriyle doğrudan yanlışlanmış sayılmaz; yorumun tarihsel, dilsel ve metinsel dayanakları ise kanıt üzerinden tartışılabilir.
6. **Orantılı yöntem:** Bir alan âyet veya araştırma sorusu için uygulanabilir değilse içerik uydurulmaz; “uygulanamaz” gerekçesi kaydedilir.

---

## 2. Doğrulama modülleri (V1–V11)

Bu modüller tasarım gereklilikleridir. Herhangi birinin listelenmesi, modülün linter tarafından başarıyla uygulandığını veya akademik incelemenin yapıldığını göstermez.

| Kod | Gereklilik | Uygulama sınırı |
|---|---|---|
| **V1** | Kaynak künyesi ve izlenebilir atıf | İki katmanlı kaynakça (`classical_sources` + `modern_sources`). Klasik kaynaklarda İSNAD 2 vefat tarihi (`death_year: "ö. H/M"`), eser, muhakkik, cilt-sayfa ve Arapça nakil; çağdaş kaynaklarda kurum/yazar, başlık, yıl ve DOI/URL belirtilir. Künye varlığı doğruluk garantisi değildir. |
| **V2** | Nakil, tercüme ve yorum ayrımı | Doğrudan alıntı `[NAKİL]`, tercüme `[TERCÜME]`, analistin çıkarımı `[YORUM]` etiketiyle ayrılır. Alıntı kaynağa bağlanır. |
| **V3** | İhtilaf ve alternatif okumalar | H6 veya yorumu anlamlı biçimde etkileyen ihtilaflarda ilgili görüşler ve delilleri gösterilir. İlgisiz görüş türü sırf sayı tamamlamak için eklenmez; kapsam dışı bırakma gerekçelendirilir. |
| **V4** | Dosya bütünlüğü | SHA-256 yalnızca belirli dosya baytlarının değişmediğini, güvenilir bir referans özetiyle karşılaştırıldığında gösterir. Kaynak doğruluğunu veya yazar kimliğini kanıtlamaz. Özet, kendi içinde değişen rapor alanına yazılmaz; ayrı manifestte veya sürüm kaydında tutulur. |
| **V5** | Senaryo puanları | Ölçek, yön ve puan gerekçesi tanımlanır. Bileşik puan kullanılacaksa formül ve ağırlıklar önceden belirtilir; veri yoksa puan ampirik ölçüm gibi sunulmaz. |
| **V6** | Eşiklerin kökeni | Her eşik veri temelli, mevzuat/kurum standardından alınmış veya analitik öneri olarak sınıflanır. Son durumda `[TAHMİNÎ EŞİK]` ve belirsizlik notu kullanılır. |
| **V7** | Ampirik verinin izlenebilirliği | Kurumun yanında veri seti/rapor adı, sürüm veya yayın yılı, tablo/değişken, erişim tarihi ve mümkünse kalıcı bağlantı verilir. Ölçüm tanımı ve kapsam sınırlılıkları belirtilir. |
| **V8** | Sınırlı yanlışlanabilirlik | Test edilebilir politika hipotezleri için ölçüm planı yazılır. Normatif önerme ile bu önermenin ampirik uygulama iddiası ayrı tutulur. |
| **V9** | Âyete özgü açık problem | Âyete özgü çözümlenmemiş gerilim varsa açıklanır. Belirgin bir problem saptanmamışsa bu sonuç ve taramanın sınırı kaydedilir; yapay bir aporia üretilmez. |
| **V10** | Sınır beyanı | Raporun ne olduğu ve ne olmadığı belirtilir. Beyan, linter uyumunu, akademik geçerliliği veya dış onayı kendiliğinden tesis etmez. |
| **V11** | Değerlendirme kaydı | İç kontrol, dış uzman görüşü ve hakemli yayın birbirinden ayrılır. Her statünün kanıtı ve incelenen rapor sürümü kaydedilir. |

---

## 3. Rapor metaverisi ve bütünlük kaydı

Rapor YAML frontmatter kullanıyorsa, YAML geçerliliği ve alan tipleri sürümlenmiş bir şemayla denetlenmelidir. Şema doğrulaması semantik doğrulama değildir. Aşağıdaki örnek şematik taslaktır; yer tutucular gerçek raporda doldurulmalı, otomatik üretilen alanlar elle doğrulanmış gibi gösterilmemelidir.

```yaml
---
gem_version: "6.1.1"
case_id: "GEM-RAPOR-2026-0XX"
surah: "Sûre adı"
verse: "X:Y"
topic: "Konu başlığı"
date: "YYYY-MM-DD"
layer: 3
h6: true
confidence_grade: "B" # A, B veya C; sayısal olasılık değildir
status: "PRE-RELEASE" # DRAFT, PRE-RELEASE, EXTERNALLY-REVIEWED

classical_sources: [] # İSNAD 2: id, author, death_year ("ö. H/M"), work, editor, publisher, volume, pages, arabic_quote, verification_link
modern_sources: []    # APA 7 / DOI: id, institution/author, title, publication_year, url, doi
thresholds: []
scenarios: []

peer_review:
  status: "PRE-RELEASE"
  internal_linter_verified: true
  reviewer_name: null
  reviewer_institution: null
  review_date: null
  review_notes: null
---
```

### Hash kaydı

- Hash, frontmatter içindeki kendisini değiştiren alana yazılmaz (`0000...` yer tutucu olarak bırakılır).
- Raporun sabitlenmiş sürümü için SHA-256 ayrı bir `.sha256` manifestinde veya sürüm kontrolü release kaydında saklanır.
- Üretim ve doğrulama aynı dosya baytları, satır sonu (LF normalizasyonu) ve kapsam tanımını kullanır.
- İmzalı commit veya imzalı manifest ek provenance sağlayabilir. İmza anahtarının güven zinciri ayrıca doğrulanmadıkça imza tek başına akademik onay sayılmaz.

### Kaynak kaydı (İSNAD 2 + Veri Bilimi Hibriti)

Kaynaklar iki katmanlı olarak tutulur:
1. **`classical_sources`**: Klasik İslami kaynaklar için `id`, `author`, İSNAD 2 standardında vefat tarihi (`death_year: "ö. H/M"`), `work`, `editor` (tahkik), `publisher`, `publication_place`, `publication_year`, `volume`, `pages`, `arabic_quote` ve `verification_link` / `doi_or_urn` kaydedilir.
2. **`modern_sources`**: Çağdaş kurumsal ve ampirik kaynaklar için `id`, `institution` / `author`, `title`, `publication_year`, `url` ve `doi` kaydedilir.
Metin içindeki nakiller ve ampirik iddialar standart Markdown dipnotlarıyla (`[^1]`, `[^2]`) `Z-4.5: AKADEMİK KAYNAKÇA` bölümüne bağlanır. Arapça alıntı yalnızca gerçekten kontrol edildiyse eklenir; linter, alıntının asıl eserde bulunduğunu teyit edemez.

---

## 4. Analiz mimarisi: beş makro faz, 26 adım

Makro fazlar gezinme ve rapor düzeni içindir; adım numaralarının yerine geçmez. Aynı içerik iki yerde tekrarlanmaz: bir bölümdeki bulgu diğerinde kaynak kimliği veya bölüm numarasıyla çapraz bağlanır.

### Faz I — Kimlik, metin ve bağlam

**Adım 00 — Künye ve giriş:** Vaka kodu, âyet, konu, tarih, sürüm, katman, H6, dil, güven derecesi ve rapor statüsü.

**Adım 00-5 — Dil ve semantik matrisi:** Katman 3 + H6 raporlarında zorunludur. Diğer raporlarda araştırma sorusuna göre kullanılır. Her kaynak için `[NAKİL]`, gerekiyorsa `[TERCÜME]` ve `[YORUM]` ayrılır.

1. **Kök ve sözlük anlamı:** İbn Fâris (*Makâyîs*) ve/veya Râgıb el-İsfahânî (*el-Müfredât*); kelime ve soruya uygun olan seçilir.
2. **Kur'an içi kavram kullanımı:** Kavramsal bir iddia kuruluyorsa Râgıb'a ek olarak ilgili âyet kullanımları doğrudan taranır. Tek bir sözlük kaynağı bütün Kur'an kullanımını temsil ediyor sayılmaz.
3. **Nahiv ve belâğat:** Zemahşerî (*el-Keşşâf*) başta olmak üzere kullanılan tefsir kaynağı; nakil ile yorum ayrılır.
4. **Klasik lisan ve kullanım:** İbn Manzûr (*Lisânü'l-Arab*) veya soruya uygun başka bir lügat/korpus kaynağı. Şiir veya tarihsel örnek, kaynağı doğrulanmadan eklenmez.

Her alt alanın uygulanabilirliği belirtilir. “Dört kaynak zorunlu” kuralı yoktur; seçimin gerekçesi ve eksik kalan kanıt açıkça yazılır.

**Adım 01 — Lafzî tahlil:** Arapça metin, kelime/gramer çözümlemesi ve anlam tercihleri. Adım 00-5'teki nakiller tekrarlanmaz; ilgili kayda atıf yapılır.

**Adım 02 — Mantıksal semantik ve karşıt ilke:** Önerme, koşul, istisna, kapsam ve alternatif maslahatlar; metin içi kanıt ile analitik çıkarım ayrılır.

**Adım 03 — Ethos, Logos, Pathos ve olgu-değer köprüsü:** Ahlaki yük, akıl yürütme ve duygusal etki incelenir. Olgusal öncüllerden normatif sonuç çıkarılırken aradaki normatif öncül görünür kılınır.

**Adım 04 — Makasıd:** Zarûriyyât, hâciyyât ve tahsîniyyât değerlendirmesi; kullanılan makasıd yaklaşımı ve kaynaklar belirtilir. Beş temel koruma alanı otomatik ve bağlamsız eşleştirilmez.

**Adım 04b — Yorumcu konumu:** Usûlî/mezhebî tercih, felsefi yaklaşım, analistin sınırlılıkları ve farklı bir yaklaşımın muhtemel sonucu açıklanır.

**Adım 05 — Siyak-sibak (S1–S7):** Kodların anlamı bu sürümde sabittir: S1 önceki âyet; S2 sonraki âyet; S3 sûre başı/pasaj konumu; S4 sûre sonu ve bütünlük; S5 sûre teması; S6 nüzul bağlamı; S7 bağlamdan koparma riski. Mushaf sırası, gerekirse ayrı bir not olarak eklenir; S kodları yeniden tanımlanmaz.

**Adım 06 — Çapraz âyet analizi:** İlgili âyetler ve ilişki türü (açıklama, tahsis, takyid, benzer tema veya gerilim) gerekçesiyle verilir. Asgari sayı, ilgisiz âyet eklemeyi teşvik etmemelidir.

### Faz II — Sistem ve gelecek modellemesi

**Adım 07 — Sistem haritası (CLD):** Temel değişkenler, nedensel varsayımlar, R/B döngüleri, gecikmeler, kırılma noktaları, geri döndürülebilirlik ve belirsizlikler gösterilir. Nedensel diyagram, tek başına nedensellik kanıtı değildir.

**Adım 08 — Dört senaryo:** Koruyucu, bozulma, denge ve ihya/dönüşüm senaryoları; koşullar, sinyaller, ufuk, aktör ve puanlama gerekçesi. Senaryolar öngörü veya olasılık tahmini değilse bu açıkça belirtilir.

**Adım 09 — Zaman ufku:** H1 (0–3), H2 (3–10), H3 (10–30), H4 (30+ yıl). Bu ufuklar bağlama göre değiştirilebilir ve değişiklik açıklanır.

**Adım 10 — Morfolojik gözlem:** Kullanılan dilbilimsel/morfolojik yöntemin adı, veri kaynağı ve sınırlılıkları verilir. Ebced veya numerolojik çıkarım analitik kanıt olarak kullanılmaz.

**Adım 10b — Belirsizlik ve karar stratejisi:** Risk, ölçülebilir belirsizlik ve derin belirsizlik ayrılır; robust, uyarlamalı veya koruyucu strateji seçiminin gerekçesi yazılır.

### Faz III — Sınama, karşı okuma ve ahlakî değerlendirme

**Adım 11 — Sekiz iç denetim:** Metin, bağlam, kaynak, karşıt ilke, veri, dil, rol ayrımı ve geri çekilebilirlik kontrolleri uygulanır. Her sonuç kısa gerekçeyle yazılır. İç denetim, bağımsız uzman incelemesi değildir.

**Adım 12 — Red Team ve sınanabilirlik:** Güçlü karşı okumalar sunulur; mümkünse analistin kendi yorumunu zorlayan kanıt da değerlendirilir. Ampirik politika hipotezinde şunlar belirtilir: hipotez, ölçülen sonuç, hedef nüfus/kapsam, zaman penceresi, veri kaynağı, eşik veya karşılaştırma ve sonucu hangi durumda revize edeceği. Eşik gerekçesi yoksa tahminî olduğu açıklanır. Normatif önerme ile ampirik uygulama iddiası ayrı tutulur.

**Adım 13 — Enfüs-Âfâk ve Kalp Fıkhı:** Âyetin insanın iç dünyası ve ahlaki yönelişi (enfüs) ile toplumsal, kurumsal ve maddi gerçeklikler (âfâk) arasındaki ilişkisi incelenir. Her raporda içsel-ahlakî boyut en azından kısa biçimde ele alınır. “Kalp fıkhı” bu standartta niyet, vicdan, ahlaki muhasebe ve karakterin eyleme etkisini inceleyen analitik bir mercek anlamındadır; bağımsız bir fıkıh disiplini, fetva veya ilahî muradın kesin bilgisi iddiası taşımaz.

- **Enfüs:** Âyetin niyet, yöneliş, ahlaki zaaf ve sorumlulukla ilişkisi.
- **Âfâk:** Bu yönelişlerin toplumsal ve kurumsal şartlarda nasıl görünür sonuçlara dönüştüğü.
- **Karşılıklı etki:** Dış düzenin insanın ahlaki imkânlarını nasıl etkilediği; bireysel ve ortak eylemin dış düzeni hangi gerekçelendirilebilir mekanizmalarla etkileyebileceği.
- **Karar köprüsü:** İçsel değerlendirme Adım 02'deki normatif gerekçeye ve Adım 15'teki karar koluna bağlanır. Bu bağ kendiliğinden varsayılmaz; gerekçesi, sınırı ve mümkünse gözlenebilir mekanizması belirtilir.
- **Tasavvufî/işârî okuma:** Kullanılıyorsa kaynak, gelenek ve yorum yöntemi belirtilir; bu okumanın lafzî/bağlamsal tahlil ve fıkhî hükümle aynı statüde olmadığı açıklanır. Belirli bir tasavvufî tevil üretmek zorunlu değildir. Bu bölüm ampirik kanıt veya tek başına politika gerekçesi sayılmaz.

### Faz IV — Bayes, karar ve etik denetim

**Adım 14 — Erken uyarı ve Bayes güncellemesi (uygulanabilirse):** Gösterge kodları `EU-01` biçimindedir; N4 gibi başka bağlam kodlarıyla karıştırılmaz. Bayes yalnızca ölçülebilir ampirik hipotezler için uygulanır:

$$P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}$$

Prior için kaynak/veri veya uzman kanaati yöntemi, tarih, kapsam ve belirsizlik aralığı kaydedilir. Veri temelli olmayan prior “öznel uzman yargısı” olarak işaretlenir; sahte nesnellik verilmez. Likelihood ve karşı-hipotez altındaki likelihood ayrı gerekçelendirilir. Brier skoru tahmin kalibrasyonunu sonradan değerlendirebilir, prior kaynağı yerine geçmez. Delphi kullanılırsa uzman seçimi ve uzlaşı yöntemi açıklanır; uzlaşı nesnel base-rate sayılmaz. Uygun veri veya model yoksa posterior hesaplanmaz ve neden belirtilir.

**Adım 15 — Karar kolları ve kaldıraç bağlantısı:** Her karar kolu yetkili aktör, hedef değişken, araç, ufuk, ölçüt, trade-off, ikinci derece etki, geri dönüş yolu ve etik denetim içerir. CLD kullanılmışsa ilgili döngü/değişken, önerilen müdahale ve beklenen mekanizma Adım 07'ye açık atıfla bağlanır. Meadows kaldıraç noktaları yararlıysa kullanılır; zorunlu taksonomi değildir.

**Adım 16 — Önyargı ve taraflılık denetimi:** Doğrulama yanlılığı, otoriteye aşırı dayanma, güncellik, grup düşüncesi, korku ve çıkar çatışması incelenir; risk ve önlem kaydedilir.

### Faz V — Güven, sorumluluk ve izleme kaydı

**Adım 17 — Güven düzeyi:** A/B/C nitel dereceleri kullanılır; anlamı ve ölçütleri raporda açıklanır. Teolojik veya ahlaki hükümlere sayısal olasılık verilmez.

**Adım 17b — Aktör haritası:** İlgili güç odakları, uygulayıcılar, etkilenen gruplar, dengeleyiciler ve gelecek nesiller değerlendirilir. İlgisiz aktör kategorileri gerekçesiz biçimde doldurulmaz.

**Adım 18 — Bilgi tabanı ve zayıflıklar:** Her önemli iddianın bilgi statüsü (kaynakla desteklenen, yorum, varsayım, araştırma notu) ve raporun başlıca zayıflıkları kaydedilir.

**Adım 18.1 — Dil güvenliği:** Mutlak kesinlik ve kendini onaylayan dil taranır. Alıntı veya kural açıklaması istisnaları, rapor gövdesindeki iddia gibi yorumlanmayacak şekilde linter'da bağlamlı ele alınmalıdır.

**Adım 19 — İzleme ve geriye dönük sınama:** Ölçülebilir KPI, kaynak, ölçüm sıklığı, sorumlu ve revizyon kuralı belirtilir. Retrodiction için dönem, o dönemde yapılacak öngörü, gözlenen sonuç, karşı örnek ve sınırlılık kaydedilir. Sonuçlar “doğrulandı” gibi kesin ifadeler yerine kanıtın gücüyle orantılı anlatılır.

**Adım 20 — Açık sorular ve varsayımlar:** Numaralı açık sorular, kritik varsayımlar, yanıtlayacak veri/araştırma ve sorumlu takip adımı yazılır.

**Z-1 — Özgün problematik (koşullu):** Âyete özgü çözümlenmemiş bir gerilim varsa tartışılır; yoksa “belirgin özgün problem saptanmadı” denebilir. Zorunlu olan aporia üretmek değil, soruyu dürüstçe ele almaktır.

**Z-2 — Görüş ihtilafı cetveli (koşullu):** H6 veya yorumu etkileyen gerçek ihtilaf varsa ilgili klasik ve çağdaş okumalar kaynaklarıyla karşılaştırılır. Mezhep, tasavvufî/işârî yaklaşım ve tarihselci yaklaşım yalnızca konuya uygunsa yer alır; “bâtınî” ayrı bir gelenek adı olarak kullanılıyorsa tanımlanır.

### Adım 16 sonrası kalite kapısı

Yayıma geçmeden önce: adımların uygulanabilirliği ve gerekçeleri kontrol edildi mi; kaynaklar nakil iddialarına bağlandı mı; ölçülebilir hipotezler normatif iddialardan ayrıldı mı; zayıflık ve belirsizlikler görünür mü; linter sürümü ve sonucu doğru statüde mi; dış değerlendirme yapıldıysa kanıtı kaydedildi mi? “Evet” kutuları tek başına kalite kanıtı değildir.

---

## 5. Zorunlu ve koşullu ekler (Z-1–Z-5 ve Z-4.5)

Z ekleri, analiz adımlarına eklenen otomatik onay testleri değildir. İlgili olduklarında raporun sonunda yer alırlar; uygulanabilir olmadıkları durumda kısa gerekçe verilir.

- **Z-1 — Özgün problematik:** Adım 02/04 ile bağlantılı, âyete özgü gerilim ve sınırlar.
- **Z-2 — Görüş ihtilafı:** Adım 04b/06 ile bağlantılı, gerçekten ilgili alternatif görüşler ve dayanakları.
- **Z-3 — Varsayım, zayıflık ve geliştirme:** Önemli sınırlılıklar, açık sorular ve somut geliştirme adımları.
- **Z-4 — Sınır beyanı:** Raporun analitik niteliği, fetva olmadığı, çıkarım/varsayım sınırları ve denetim statüsü. Linter sonucu veya hakem incelemesi yapılmadıysa yapılmış gibi yazılmaz.
- **Z-4.5 — Akademik kaynakça (İSNAD 2 ve APA / DOI bibliyografyası):** Klasik İslami kaynakların İSNAD 2. Edisyon kurallarına göre (müellif, vefat yılı `ö. H/M`, eser, tahkik, cilt, basım yeri/yayınevi/yılı), çağdaş kurumsal ve ampirik kaynakların ise APA 7 / DOI standardına göre alfabetik listelendiği ve metin içi dipnotların (`[^1]`, `[^2]`) yer aldığı bibliyografya bölümü.
- **Z-5 — İnceleme kaydı:** İnceleyen kişi/kurum (paylaşımı uygunsa), rapor sürümü/hash'i, tarih, karar, kapsam ve inceleme kaydı. PR bağlantısı denetlenebilir iz sağlar ama tek başına hakemlik niteliğini kanıtlamaz. GPG/PGP imzası ek güvence olarak isteğe bağlıdır; kullanılan anahtar ve doğrulama yöntemi açıklanır.

### Yayın statüleri

- `DRAFT`: Çalışma sürümü.
- `PRE-RELEASE`: Yazar/ekip içi kontroller tamamlanmış; bağımsız dış inceleme tamamlanmamış sürüm.
- `EXTERNALLY-REVIEWED`: Belirli sürüm için bağımsız dış değerlendirme kaydı mevcut. Bu statü hakem kararının kabul olduğu veya bilimsel uzlaşı bulunduğu anlamına gelmez.

Statü, linter tarafından tek başına yükseltilmez. İnceleme yapan kişinin yazarla ilişkisi ve çıkar çatışması mümkün olduğu ölçüde beyan edilir.

---

## 6. Linter ve doğrulama beyanı

Linter (`src/gem_lint.py` v6.1.1) yalnızca uygulandığı ve test edildiği kuralları denetler. Anahtar sözcük bulunması bir bölümün bilimsel içeriğini, Arapça alıntının doğruluğunu, nedensel diyagramın geçerliliğini veya hakem bağımsızlığını kanıtlamaz. “Akademik olarak doğrulandı” gibi genel sonuç üretmez.

Uygulanan kontroller ve testler şunları kapsar:

1. Sürüm kontrollü YAML şema doğrulaması ve iki katmanlı kaynakça (`classical_sources` + `modern_sources`, `L-0101..L-0106`) kontrolleri.
2. Hash'i belirtilen kapsamda hesaplayıp ayrı `.sha256` manifestiyle karşılaştırma (`L-0404`).
3. Eşik, Bayes ve falsifiabilite alanlarının yapısal tutarlılığını kontrol etme; semantik doğrulama iddiasında bulunmama.
4. Alıntı muafiyetleri ve dil güvenliği için yanlış pozitif/negatif testleri.
5. Rapor statüsü ile inceleme kanıtının ayrılması (`L-1101..L-1104`).
6. Kuralları kapsayan otomatik birim testleri (`tests/test_gem_lint.py`).

---

## 7. Sürüm geçmişi

### v6.0.0'dan v6.1.0'a

1. Adım 17–20 ve kalite kapısı geri eklendi; 26 adımın kapsamı açıklandı.
2. S1–S7 kodları sabitlendi; erken uyarı kodları `EU-XX` yapılarak N4 çakışması önlendi.
3. Dil matrisi dört araştırma boyutunu kapsayacak biçimde geliştirildi; her kaynak her raporda zorunlu tutulmadı.
4. Bayes prior, likelihood, öznel uzman yargısı ve kalibrasyon ayrıştırıldı; Brier ve Delphi'nin sınırları açıklandı.
5. CLD ile karar kolu arasında izlenebilir müdahale zinciri tanımlandı.
6. Hash özeti kendi içinde değişen dosyaya gömülmedi; hash'in kanıtlayabildiği ve kanıtlayamadığı şeyler ayrıldı.
7. V1–V11 modülleri ve linter'ın yetenekleri hakkında doğrulanmamış akademik/otomatik başarı iddiaları kaldırıldı.
8. Z-1/Z-2 ve dış inceleme şartları uygulanabilirlik ve kanıt durumuna bağlandı; imza zorunlu değil, isteğe bağlı güvence olarak tanımlandı.
9. “Mısrî” etiketi kapsamı belirsiz kullanımdan çıkarıldı; irfanî/tasavvufî inceleme yöntemi açıkça tanımlandı.
10. Beş makro faz gezinme düzeni olarak eklendi; adım içeriğinin yerine geçmediği belirtildi.

### v6.1.0'dan v6.1.1'e

1. Adım 13, enfüs-âfâk ilişkisi ve kalp fıkhı analitik merceği olarak tanımlandı.
2. İçsel-ahlakî boyutun her raporda ele alınması; belirli tasavvufî/işârî tevilin ise kaynak ve yöntem bulunduğunda kullanılması ayrıştırıldı.
3. İçsel değerlendirmeden karar koluna geçişin gerekçelendirilmesi, otomatik normatif veya ampirik çıkarım sayılmaması şartı eklendi.

### v6.2.0 ve v6.2.1 (Külliyat ve Akademik Atıf Standardizasyonu)

1. 12 stratejik analiz raporu (`06`–`17`) v6.1.1 Katman 3 + H6 standardında üretildi ve harici `.sha256` manifestolarıyla doğrulandı.
2. İSNAD 2 + Veri Bilimi Hibriti iki katmanlı kaynakça (`classical_sources` + `modern_sources`), metin içi dipnotlar (`[^1]`) ve `Z-4.5: AKADEMİK KAYNAKÇA` bölümü sisteme entegre edildi.
3. `src/gem_lint.py` içine `L-0104`, `L-0105` ve `L-0106` (`death_year`) denetim kuralları eklendi.

---

## 8. Uygulama ve sürümleme notu

Bu belge metodolojik standardın v6.1.1 / v6.2.1 referans metnidir. `src/gem_lint.py`, test paketi (`tests/test_gem_lint.py`), rapor şablonu (`docs/tr/05-ornek-rapor-v6.1.1.md`) ve 12 raporluk külliyat bu standartla tam hizalanmıştır; v5.2.0 ve v6.0.0 raporları tarihsel arşiv olarak korunur.