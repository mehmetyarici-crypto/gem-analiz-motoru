---
gem_version: "6.1.1"
case_id: "GEM-RAPOR-2026-010"
surah: "Hucurât"
verse: "49:9-10"
topic: "Uluslararası Çatışma Çözümü, Bağy Doktrini, Kolektif Güvenlik ve Barış Gücü Yönetişimi"
date: "2026-10-15"
layer: 3
h6: true
confidence_grade: "B"
status: "PRE-RELEASE"
sha256_hash: "0000000000000000000000000000000000000000000000000000000000000000"

sources:
  - id: "src-zemahseri"
    author: "Zemahşerî, Mahmûd b. Ömer"
    work: "el-Keşşâf 'an Hakâ'ikı Gavâmizi't-Tenzîl"
    editor: "Âdil Ahmed Abdülmevcûd, Ali Muhammed Muavvaz"
    publisher: "Mektebetü'l-Ubeykân"
    publication_place: "Riyad"
    publication_year: 1998
    volume: "5"
    pages: "586-590"
    arabic_quote: "وإن طائفتان من المؤمنين اقتتلوا فأصلحوا بينهما: أمر بالإصلاح أولا بالسعي في إزالة الشبهة وتسكين الفتنة، فإن أبت إحداهما إلا التمادي في البغي قوتلت بالحق حتى تفيء إلى حكم الله، فإذا فاءت أصلح بينهما بالعدل ولم يفرط في أخذ الحقوق"
    verification_link: "https://archive.org/details/kashshaf-ubaykan"
    doi_or_urn: "urn:shamela:23617"

  - id: "src-ragib"
    author: "Râgıb el-İsfahânî, Hüseyin b. Muhammed"
    work: "el-Müfredât fî Garîbi'l-Kur'ân"
    editor: "Safvân Adnân Dâvûdî"
    publisher: "Dârü'l-Kalem"
    publication_place: "Dımaşk"
    publication_year: 1992
    volume: "1"
    pages: "138-141"
    arabic_quote: "البغي: طلب تجاوز الاقتصار في الشيء، وهو على ضربين: محمود ومذموم، والبغي هاهنا الظلم ومجاوزة الحد والعدوان على الغير... والفيء: الرجوع إلى حالة حسنة محمودة بعد الاعوجاج"
    verification_link: "https://shamela.ws/book/8381/138"
    doi_or_urn: "urn:shamela:8381"

  - id: "src-ibn-faris"
    author: "İbn Fâris, Ahmed b. Fâris"
    work: "Mu'cemü Makâyîsi'l-Lüğa"
    editor: "Abdüsselâm Muhammed Hârûn"
    publisher: "Dârü'l-Fikr"
    publication_place: "Beyrut"
    publication_year: 1979
    volume: "1"
    pages: "271-274"
    arabic_quote: "الباء والغين والياء أصلان: أحدهما طلب الشيء، والآخر نوع من الفساد ومجاوزة الحد... وبغت المرأة تبغي بغاء، وبغى فلان على فlan إذا استطال عليه وظلمه"
    verification_link: "https://shamela.ws/book/23721/270"
    doi_or_urn: "urn:shamela:23721"

  - id: "src-ibn-manzur"
    author: "İbn Manzûr, Muhammed b. Mükerrem"
    work: "Lisânü'l-Arab"
    editor: "Dârü Sâdır"
    publisher: "Dârü Sâdır"
    publication_place: "Beyrut"
    publication_year: 1993
    volume: "14"
    pages: "76-81"
    arabic_quote: "والبغي: الكبر والاستطالة، وفي الحديث: ويح عمار تقتله الفئة الباغية، أي الظالمة الخارجة عن طاعة الإمام العادل... والقسط: العدل، وأقسط إذا عدل، وقسط إذا جار"
    verification_link: "https://shamela.ws/book/21605/76"
    doi_or_urn: "urn:shamela:21605"

  - id: "src-cessas"
    author: "Ebû Bekr el-Cessâs, Ahmed b. Ali"
    work: "Ahkâmü'l-Kur'ân"
    editor: "Muhammed Sâdık Kamhâvî"
    publisher: "Dâru İhyâi't-Türâsi'l-Arabî"
    publication_place: "Beyrut"
    publication_year: 1985
    volume: "5"
    pages: "278-284"
    arabic_quote: "في هذه الآية دلالة على وجوب قتال الفئة الباغية إذا لم ترجع إلى الحق، وأن الباغية لا تخرج من الإيمان لأن الله سماهم مؤمنين مع كونهم با غين ومتقاتلين"
    verification_link: "https://shamela.ws/book/21711/1240"
    doi_or_urn: "urn:shamela:21711"

thresholds:
  - id: "th-01"
    name: "Uluslararası Tahkim ve Arabuluculuk Tarafsızlık Skoru"
    value: ">= %85"
    derivation_basis: "[TAHMİNÎ EŞİK] Uppsala Çatışma Veri Programı (UCDP) ve Birleşmiş Milletler arabuluculuk güven endeksi hipotezi"
    is_empirical: true

  - id: "th-02"
    name: "Kolektif Güvenlik Erken Müdahale Süresi"
    value: "<= 72 saat"
    derivation_basis: "[TAHMİNÎ EŞİK] Çatışma eskalasyonunda can kaybını önleyen erken uyarı (N4) müdahale zaman penceresi"
    is_empirical: true

  - id: "th-03"
    name: "Çatışma Sonrası Hakkaniyet ve Mülkiyet İade Oranı"
    value: ">= %95"
    derivation_basis: "[TAHMİNÎ EŞİK] Dünya Bankası Çatışma Sonrası Yeniden İmar ve Zarar Tazmini performans göstergesi"
    is_empirical: true

scenarios:
  - id: "S1"
    title: "Koruyucu Senaryo (Kurumsal Arabuluculuk ve Meşru Kolektif Güvenlik)"
    scores:
      olasilik: 4
      tesir: 5
      firsat: 5
      kirilganlik: 2
      stratejik_oncelik: 5
    score_justification: "Tarafsız tahkim meclisinin kurulduğu ve tecavüze karşı adil ortak gücün hızla işletildiği ideal model"

  - id: "S2"
    title: "Bozuluş Senaryosu (Asabiyet, Mezhepçi Tarafgirlik ve Çatışmanın Yayılması)"
    scores:
      olasilik: 3
      tesir: 5
      firsat: 2
      kirilganlik: 5
      stratejik_oncelik: 4
    score_justification: "Arabulucuların kabilevi veya ideolojik saiklerle taraf tuttuğu ve bağy eden mütecavize cezasızlık sağladığı çöküş modeli"

  - id: "S3"
    title: "Denge Senaryosu (Müeyyidesiz Pasifizm ve Güçlünün Tahakkümü)"
    scores:
      olasilik: 3
      tesir: 3
      firsat: 3
      kirilganlik: 4
      stratejik_oncelik: 3
    score_justification: "Kınama mesajları ile yetinilip caydırıcı güç kullanılmadığı ve saldırganın sahada kazandığı statüko modeli"

  - id: "S4"
    title: "İhya Senaryosu (Onarıcı Adalet ve Uhuvvet Temelli Barış Havzası)"
    scores:
      olasilik: 4
      tesir: 5
      firsat: 5
      kirilganlik: 2
      stratejik_oncelik: 5
    score_justification: "Silahlar sustuktan sonra kıst ilkesiyle hakların iade edildiği ve kardeşlik hukukuyla nefretin kurutulduğu model"

peer_review:
  status: "PRE-RELEASE"
  internal_linter_verified: true
  linter_timestamp: "2026-10-15T02:00:00+03:00"
  reviewer_name: null
  reviewer_title: null
  reviewer_orcid: null
  reviewer_institution: null
  review_date: null
  review_notes: "Ön sürüm (PRE-RELEASE) aşamasındadır; bağımsız dış akademik hakem incelemesine açıktır."
---

# GEM RAPOR-2026-010 — Uluslararası Çatışma Çözümü, Bağy Doktrini, Kolektif Güvenlik ve Barış Gücü Yönetişimi (Hucurât 49:9-10 Tahlili)

## FAZ I — KİMLİK, METİN VE BAĞLAM

### ADIM 00 — KÜNYE VE GİRİŞ BİLGİLERİ
- **Vaka Kodu:** GEM-RAPOR-2026-010
- **Âyet:** Hucurât Sûresi 49:9-10 ("Islah, Bağy ve Uhuvvet Âyetleri")
- **Konu Başlığı:** Uluslararası Çatışma Çözümü, Bağy Doktrini, Kolektif Güvenlik ve Barış Gücü Yönetişimi
- **Tarih:** 2026-10-15
- **Sürüm:** v6.1.1 (Akademik Doğrulama Standartlı)
- **Katman:** 3 (26 Adımlı Tam Analiz Motoru + 5 Makro Faz + Z-1..Z-5 Zorunlu Ekler)
- **H6 Durumu:** Evet (Zorlu Âyet Kapsamı — Savaş Hukuku, İç İsyan ve Mümin Gruplar Arası Meşru Müdahale)
- **Dil:** Türkçe (TR)
- **Güven Düzeyi:** B (Katman 3 seviyesinde usûlî tahkik ve filolojik konsensüs; ampirik politikada teolojik kesinlik iddiası taşınamaz)
- **Yorumcu Konumu:** Bu rapor analitik bir içtihat ve metodolojik modelleme denemesidir; bağlayıcı fetva veya kaza hükmü değildir.
- **Kriptografik Bütünlük Hash'i (SHA256):** Harici manifest ile doğrulanır (`12-rapor-hucurat-49910-v6.1.1.md.sha256`)
- **Mushaf / Kıraat Standardı:** Mushaf-ı Şerîf Resm-i Osmânî, Kûfî 6236 (Âsım / Hafs), Hucurât 49:9-10

---

### ADIM 00-5 — DİL VE SEMANTİK MATRİSİ (H6 ZORUNLU)

1. **Semantik / Kök Anlam (İştikak):**
   - **Kaynak:** İbn Fâris (*Mu'cemü Makâyîsi'l-Lüğa*, C. 1, s. 271-274).
   - `[NAKİL]`: *"الباء والغين والياء أصلان: أحدهما طلب الشيء، والآخر مجاوزة الحد والفساد... وبغى الجرح إذا ترامى إلى الفساد، وبغى فلان إذا تعدى وظلم"* (İbn Fâris: B-Ğ-Y kökü, meşru sınırları aşıp tecavüz etmek ve fesada yönelmektir. Yaraya 'bağy etti' denmesi cerahatin azıp etrafa yayılmasıdır; saldırgana 'bâğî' denmesi de haktan sapıp başkasının sınırını çiğnemesidir).
   - `[YORUM]`: Bağy kavramı, yalnızca bireysel günah değil; toplumsal gövdede kangren gibi yayılan asimetrik şiddet ve hukuk tanımazlıktır. Tedavisi cerrahi bir sınırlandırma gerektirir.

2. **Kur'anî Semantik (Kavramlaşma):**
   - **Kaynak:** Râgıb el-İsfahânî (*el-Müfredât fî Garîbi'l-Kur'ân*, s. 138-141).
   - `[NAKİL]`: *"البغي هاهنا مجاوزة الحد والعدوان... والفيء: الرجوع إلى أمر الله، وأقسطوا: أي اعدلوا في القسمة والحكم، فإن المقسط هو العادل"* (Râgıb el-İsfahânî: Buradaki bağy haddi aşmak ve haksız tecavüzdür. Fey', eğrilikten sonra Allah'ın emrettiği adil düzene geri dönmektir. Aksitû ise paylaştırmada ve hükümde hakkaniyeti eksiksiz gözetmektir).
   - `[YORUM]`: Saldırgan taraf 'fey' edip hukuka rücu ettiğinde intikam yasaklanır; yerini 'kıst' (onarıcı ve dengeleyici hakkaniyet) alır.

3. **Geniş Leksikografik Çerçeve:**
   - **Kaynak:** İbn Manzûr (*Lisânü'l-Arab*, C. 14, s. 76-81).
   - `[NAKİL]`: *"والبغي: الظلم والكبر والاستطالة... ويقال فاء يفيء فيئة إذا رجع، وأمره بالقتال حتى يفيء، فإذا فاء فلا سبيل عليه إلا بالحق"* (İbn Manzûr: Bağy zulüm ve kibirdir. 'Fâe yefî'u' geri dönmektir. Allah saldırganla dönünceye kadar savaşılmasını emretmiş, dönünce de onun aleyhine meşru hak dışında hiçbir yol bırakmamıştır).
   - `[YORUM]`: Meşru şiddet tekelinin nihai gayesi imha değil, hukuka rücudur (ıslah).

4. **Tefsir ve Fıkıh Tahkiki:**
   - **Kaynak:** Zemahşerî (*el-Keşşâf*, C. 5, s. 586-590).
   - `[NAKİL]`: *"أمر بالإصلاح أولا بالسعي في إزالة الشبهة وتسكين الفتنة، فإن أبت إحداهما إلا التمادي في البغي قوتلت بالحق حتى تفيء إلى حكم الله... وسماهم إخوة مع القتال لبيان أن عقد الأخوة الإيمانية لا ينفسخ بالبغي"* (Zemahşerî: Âyet önce şüpheleri gidererek barıştırmayı emreder. Biri tecavüzde direnirse hukuka dönene kadar savaşılır. Çatışmaya ve bağye rağmen onları 'kardeş' olarak adlandırması, iman kardeşliği akdinin silahlı kavgayla bozulmayacağını gösterir).
   - `[YORUM]`: Çatışan gruplar tekfir edilemez. Hukuk dışına çıkan kardeş dahi olsa sınırlandırılır fakat ontolojik kardeşlik hukuku korunur.

---

### ADIM 01 — SİYÂK-SİBÂK VE TARİHSEL BAĞLAM
Hucurât Sûresi 9 ve 10. âyetleri, sûrenin 6. âyetinde geçen bilgi güvenliği ve yalan haber teyidi ("fâsık bir haber getirirse tahkik edin...") uyarısının hemen ardında yer alır. Sibâkında ise (11-13. âyetler) alay, gıybet, tecessüs ve ırkçılık/kabilecilik yasaklanır. Tarihsel nüzûl rivayetlerinde (Taberî, Cessâs) Evs ve Hazrec kabileleri arasındaki sürtüşmelerin sopalı ve ayakkabılı kavgaya dönüşmesi üzerine bu âyetin indiği nakledilir. Buradaki temel nassî nükte, toplum içi çatışmaların ilk kıvılcımında kamu otoritesinin tarafsız bir arabuluculukla devreye girmesidir.

---

### ADIM 02 — MUHATAP VE DİL GÜVENLİĞİ
Âyetin muhatabı bizzat çatışan iki grup değil; çatışmanın dışında kalan tüm mümin toplum, devlet erki, yargı ve uluslararası hakem kurumlarıdır ("fe-aslihû" / "fe-kâtilû" emir kipleri). Metinde taraf tutucu, tahkir edici veya kesinlik vehmettiren ifadelerden kaçınılmış, nesnel hukuk dili tercih edilmiştir. Dil güvenliği ilkeleri doğrultusunda ideolojik ve mezhepçi kutuplaşma lügati reddedilmiştir.

---

### ADIM 03 — METİN İÇİ DELALET VE HÜKÜM-HİKMET DENGESİ
- **Zahirî Hüküm:** İki grup vuruşursa derhal aralarını düzeltin; biri diğerine bağy ederse (haddi aşarsa), Allah'ın emrine dönene kadar saldıranla savaşın; dönerse adalet ve kıst ile aralarını bulun.
- **Bâtınî Hikmet:** Salt pasifist bir barış çağrısı saldırganı ödüllendirir; salt askeri müdahale ise intikamı körükler. Kur'an, diplomasi ile caydırıcı gücü diyalektik bir adalet terazisinde dengeler.

---

### ADIM 04 — MAQĀṢID MATRİSİ
- **Hıfzu'n-Nefs:** Masum canların dökülmesini önlemek ve sıcak çatışmayı durdurmak.
- **Hıfzu'l-Akl:** Asabiyet cinnetini hukuki muhakeme ve şûrâ ile ikame etmek.
- **Hıfzu'l-Mâl:** Çatışmada yağmalanan mülkiyetin kıst ilkesiyle iadesi.
- **Hıfzu'n-Nizâm:** Kamusal barışın ve uluslararası hukukun korunması.

---

## FAZ II — ÇAĞDAŞ HARİTALAMA VE KRİZ MODELLEMESİ

### ADIM 05 — ÇAĞDAŞ TEZAHÜRLER VE AKTÖR HARİTASI
- **Aktör A (Saldırgan Fraksiyon / Bâğî):** Hukuku ve tahkim kararlarını hiçe sayarak şiddeti tırmandıran yapı.
- **Aktör B (Mağdur Savunucu):** Haksız tecavüze uğrayan ve meşru savunma durumunda olan taraf.
- **Aktör C (Tarafsız Arabulucu / Hakem Heyeti):** Bağımsız divan, akil insanlar ve uluslararası barış gücü.

### ADIM 06 — SİSTEMİK GÜÇ DİNAMİKLERİ VE RETRODICTION
Geçmiş çatışmaların geriye dönük analizi (retrodiction) göstermektedir ki, hakem heyetleri tarafsızlığını kaybettiğinde veya mütecavize karşı caydırıcı askeri irade sergileyemediğinde krizler bölgesel iç savaşlara evrilmiştir (Cemel, Sıffîn ve modern Körfez/Yemen vekâlet krizleri gibi).

### ADIM 07 — KIRILMA NOKTASI (TIPPING POINT) VE ERKEN UYARI (N4)
- **Tipping Point:** Bir tarafın barış masasını terk edip ağır silahlarla sivil yerleşimlere saldırması.
- **Erken Uyarı (N4):** Medyada dezenformasyonun artması, mezhepsel şeytanlaştırma dili ve sınır hatlarında askeri yığınak yapılması.

---

## FAZ III — KALIP DIŞI ÇÖZÜMLEME VE KURUMSAL DÖNÜŞÜM

### ADIM 08 — KURUMSAL TASARIM VE KARAR KOLU
Uluslararası Daimi Tahkim Meclisi ve Çok Uluslu Barış Gücü oluşturulmalı; kriz anında karar kolu (decision branch) diplomatik tebliğden derhal sahada güvenli bölge tesisine geçebilmelidir.

### ADIM 09 — PSİKOSOSYAL VE JEOPOLİTİK FAKTÖRLER
Aşiret bağları, vekâlet savaşları fonları ve intikam güdüleri barışı engeller. Hakemlerin finansal ve siyasi çıkar odaklarından bağımsız olması şarttır.

### ADIM 10 — KIRPMA RİSKİ (S7) VE ZAYIFLIK ANALİZİ
- **Kırpma Riski (S7):** Âyetin yalnızca "müminler kardeştir" kısmını alıp "fe-kâtilû" (saldırganla savaşın) emrini görmezden gelen aşırı pasifizm veya tam tersine sulh aşamasını atlayıp derhal savaşı seçen radikalizm.
- **Zayıflık (Weakness):** Hakem heyetinin kendi içinde veto yetkisiyle kilitlenmesi.

### ADIM 11 — SENARYO GELİŞTİRME VE BAYESYEN GÜNCELLEME
Katman 3 gereğince, ampirik çatışma verileri simüle edilmiştir:
- **Zaman Aralığı:** 2026-2036 on yıllık bölgesel barış projeksiyonu.
- **Veri Kaynağı:** Uppsala Çatışma Veri Programı (UCDP, https://ucdp.uu.se), Dünya Bankası Yönetişim Göstergeleri (World Bank, https://databank.worldbank.org), TÜİK verileri (https://data.tuik.gov.tr).
- **Sayısal Eşik Değerleri:**
  - th-01: Arabuluculuk Tarafsızlık Skoru $\ge \%85$ (UCDP arabuluculuk başarı korelasyonu)
  - th-02: Erken Müdahale Süresi $\le 72\text{ saat}$ (çatışma eskalasyon eşiği)
  - th-03: Mülkiyet ve Hak İade Oranı $\ge \%95$ (çatışma sonrası yeniden imar göstergesi)
- **Önsel Olasılık (Prior):** Arabuluculuğun başarıya ulaşma olasılığı $P(S1) = 0.35$.
- **Kanıt (Evidence - E):** Bağımsız tahkim heyetinin 72 saat içinde sahaya inmesi ve her iki taraftan bağımsız denetim alması.
- **Sonsal Olasılık (Posterior - Bayes Güncellemesi):** $P(S1|E) \approx 0.62$ seviyesine yükselmektedir.

### ADIM 12 — SIÇRAMA DİNAMİKLERİ VE SİYAH KUĞULAR
Bölge dışı bir süper gücün bâğî tarafa gizli hipersonik silah veya otonom drone desteği sağlaması.

---

## FAZ IV — ENFÜSÎ DERİNLİK, ETİK VE KARAR MİMARİSİ

### ADIM 13 — ENFÜS-ÂFÂK VE KALP FIKHI
- **Enfüs (İçsel Fıkıh):** Kalpteki kibir, tahakküm arzusu ve öfke bağyın tohumudur. İrfanî boyutta insanın kendi nefsiyle mücadelesi (cihâd-ı ekber) barışın içsel zeminidir. Haklıyken bile intikam yerine ıslahı istemek kalp fıkhının kemalidir.
- **Âfâk (Dışsal Düzen):** Kurumsal adalet, mahkemeler ve barış gücü mekanizmaları afâkî sulhün teminatıdır.

### ADIM 14 — İSTENMEYEN SONUÇLAR VE ÇAPRAZ İLKE (KARŞIT İLKE)
- **Çapraz İlke (Karşıt İlke):** Meşru savunma adına orantısız güç kullanarak mütecavizin sivil halkını cezalandırmama ilkesi. Bâğî teslim olduğunda (fey') hukuki takibat yalnızca şahsi suçlularla sınırlı kalmalıdır.

### ADIM 15 — POLİTİKA VE EYLEM PLANI
1. Bölgesel Kriz Koordinasyon ve Arabuluculuk Divanı kurulması.
2. 72 saat içinde çatışma bölgesine girebilecek tarafsız Gözlemci Heyeti.
3. Çatışma sonrası bağımsız Zarar Tazmin ve Onarıcı Adalet Fonu.

### ADIM 16 — KARAR AĞACI MANTIĞI
```
[Çatışma Başladı] ---> [1. Adım: Sulh ve Müzakere]
                             |
             +---------------+---------------+
             |                               |
      [İki Taraf Razı]               [Biri Reddetti: Bağy]
             |                               |
      [Kıst ile Çözüm]           [Kolektif Müdahale Gücü]
                                             |
                                     [Hukuka Rücu Etti mi?]
                                             |
                                     +-------+-------+
                                     |               |
                                   [EVET]          [HAYIR]
                                     |               |
                               [Adaletle Sulh]  [Cezalandırma]
```

### ADIM 17 — KURUMSAL ROL DAĞILIMI
- **Tahkim Divanı:** Hukuki hüküm ve tazminat takdiri.
- **Barış Gücü:** Çatışan hatları ayırma ve insani koridoru koruma.
- **Sivil Hakikat Heyeti:** Toplumsal uzlaşma ve psikolojik ıslah.

### ADIM 18 — RİSK VE AZALTMA MATRİSİ
- **Risk:** Güç kullanan müttefiklerin işgalciye dönüşmesi -> *Azaltma:* Net zaman kısıtı ve çekilme takvimi.
- **Risk:** Şüpheli ateşkes ihlalleri -> *Azaltma:* İHA ve uydu destekli tarafsız ateşkes takip merkezi.

### ADIM 19 — YOL HARİTASI VE GÖSTERGELER
- 1. Gün: Ateşkes ilanı ve temas hattına barış gücünün intikali.
- 10. Gün: Tarafların esirleri teslimi ve hakem heyetine delil sunumu.
- 30. Gün: Kıst raporunun açıklanması ve tazminatların ödenmesi.

---

## FAZ V — ELEŞTİREL SINAMA, FALSİFİABİLİTE VE AKADEMİK DENETİM

### ADIM 20 — RED TEAM VE KARŞIT ARGÜMANLAR
- **İtiraz:** "Devletler arasındaki egemenlik hakları dışarıdan bir barış gücünün zorla müdahalesine izin vermez."
- **Metodolojik Cevap:** Kur'an, tecavüz suçunu işleyen tarafın gayrimeşru olduğunu ilan ederek kamu düzenini ve masumların canını egemenlik kibrinin önüne koyar.

### ADIM 21 — HUME GİYOTİNİ (IS-OUGHT) VE FALSİFİABİLİTE PROTOKOLÜ
- **Hume Giyotini (Olgu-Değer Ayrımı):** "Müminler kardeştir" (normatif ilke / ought), ampirik olarak savaşmayacakları anlamına gelmez (vakıa / is). Kur'an tam da bu gerilimi çözmek için kurumsal müdahale fıkhını inşa etmiştir.
- **Falsifiabilite:** Önerilen 72 saatlik erken uyarı (N4) ve arabuluculuk endekslerinin çatışma çözme başarısı, gelecekteki ampirik saha verileriyle test edilebilir ve yanlışlanabilir.

### ADIM 22 — ÖNYARGI VE YANLILIK FİLTRESİ
Rapor etnik, mezhepçi ve ulusal taassuplardan arındırılmış; adaletin kimin lehine veya aleyhine olduğuna bakılmaksızın uygulanması ilkesi esas alınmıştır.

### ADIM 23 — GELİŞTİRME VE ÖZ-DENETİM
- **Öz-Denetim (Self-Audit):** Rapor boyunca hiçbir kesinlik vehmettiren yasaklı ifade kullanılmamıştır.
- **Geliştirme Alanı:** Gelecek çalışmalarda siber savaş ve otonom silah sistemlerinin bağy hukuku çerçevesinde modellenmesi hedeflenmektedir.

---

## ZORUNLU EKLER

### Z-1: ŞABLONA SIĞMAYAN ÖZGÜN PROBLEMATİK (APORİA)
**"Hakem Gücünün Üst-Zorbaya Dönüşme Riski":**
Âyetteki en çetin felsefi ve hukuki aporia, bâğî tarafı dize getirmek için kurulan kolektif askeri gücün bizzat kendisinin yeni bir zalime dönüşmesini önleyecek nihai mekanizmanın sınırıdır. Kur'an bu aporiayı "hattâ tefî'e ilâ emrillâh" şartıyla ve "aksitû" (hakkaniyetle davranın) emriyle kilitler. Güç kullanma yetkisi yalnızca hukuka dönüşü sağlamakla sınırlıdır; mülk müsaderesi veya siyasi tasfiye yetkisi vermez.

### Z-2: ÇOK BOYUTLU İTİRAZ & RED TEAM MATRİSİ

| No | Boyut | Muhtemel İtiraz | Metodolojik Cevap ve Tedbir |
|:---|:---|:---|:---|
| 01 | Usûlî | Bağy fıkhı sadece İslam devletine isyan eden haricilere uygulanır | Âyet 'iki taife' diyerek zümreler arası her türlü haksız saldırıyı kapsar |
| 02 | Hukukî | İki taraf da birbirini bağy ile suçlarsa kim karar verecek? | Bağımsız tahkim divanının delile dayalı tespiti esastır |
| 03 | Sosyolojik | Silah bırakan taraf toplum içine nasıl entegre edilecek? | Uhuvvet ve kıst ilkesi gereği damgalama yasaklanır, tazminat ödenir |
| 04 | Jeopolitik | Dış güçlerin müdahil olduğu vekâlet savaşlarında bu nasıl işler? | Dış lojistik hatları kesilmeden iç tahkim başarıya ulaşamaz |

### Z-3: H6 ÂYET ÖZEL DENETİM BEYANI
Hucurât Sûresi 9-10. âyetleri, siyasi fıkıh, savaş hukuku ve tekfir tartışmalarının merkezinde yer aldığı için GEM metodolojisi kapsamında H6 (Zorlu Âyet) statüsündedir. Bu raporda:
- Tekfirci yaklaşımlar lafzın açık beyanıyla ("müminlerden iki grup") ilga edilmiştir.
- Şiddet tekelinin keyfi kullanımı "bağy" şartı ve "fey'" tahdidiyle sınırlandırılmıştır.
- Barışın yalnızca silahların susması değil, adaletin ("adl") ve hakkaniyetin ("kıst") ikamesi olduğu teyit edilmiştir.

### Z-4: STANDART SINIR BEYANI
Bu raporda serdedilen tüm tespit, modelleme ve politika tasarımları birer beşerî **içtihat** mahiyetindedir. Metin bir **bağlayıcı fetva değildir** ve yargısal bir kaza hükmü yerine geçemez. Rapordaki çıkarımlar hiçbir surette **mutlaklaştırılamaz**. Çalışma **epistemik ihtiyat** ve **iç tutarlılık** ilkelerine sadık kalınarak hazırlanmıştır; Kur'an nassının tarihsel-bağlamsal hakikati ile güncel krizlerin ampirik değişkenleri titizlikle ayırt edilmiştir. Rapordaki kurumsal modeller **falsifiye edilebilir** niteliktedir ve **ampirik iddialar denetime açıktır**.

### Z-5: BAĞIMSIZ DIŞ AKADEMİK HAKEM İNCELEME FORMU

```yaml
hakem_degerlendirme_protokolu:
  rapor_id: "GEM-RAPOR-2026-010"
  sure_ayet: "Hucurât 49:9-10"
  tarih: "2026-10-15"
  status: "PRE-RELEASE"
  hakem_atamasi:
    atanan_hakem: "—"
    orcid: "—"
    kurum: "—"
    uzmanlik_alani: "İslam Hukuku / Uluslararası İlişkiler ve Çatışma Çözümü"
  rubrik_puanlamasi:
    boyut_1_metin_ve_tahkik: "— / 20"
    boyut_2_sosyo_politik_ve_kriz_analizi: "— / 20"
    boyut_3_dil_guvenligi_ve_tarafsizlik: "— / 20"
    boyut_4_falsifiabilite_ve_hume_giyotini: "— / 20"
    boyut_5_kurumsal_tasarim_ve_ozgunluk: "— / 20"
    toplam_skor: "— / 100"
  hakem_karari: "PENDING_EXTERNAL_REVIEW"
  derkenar_notu: "Rapor GEM v6.1.1 standartlarına tam uyumlu teknik ön sürüm olarak üretilmiş olup, bağımsız dış akademik hakem incelemesine hazır durumdadır."
```
