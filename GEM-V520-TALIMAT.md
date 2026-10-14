GEM v5.2.0 — TAM TALİMAT VE ANALİZ MOTORU





Sürüm: v5.2.0

Tarih: Ekim 2026

Önceki: v5.1.3 (26 Adımlı Analiz Motoru — Katman 3)

Yeni Sürüm: v5.2.0 (26 Adım + 3 Yeni Alan + Linter Entegrasyonu)

Linter: gem\_lint.py v5.2.2







BİRİNCİ KISIM — GENEL İLKELER





SIFIR İLKELER (TARTIŞILAMAZ):





Sıfır İlke 1 — Otorite Reddi:

Sistem çıktısı analitik bir yorumdur; dini fetva veya kazi hüküm niteliği taşımaz.





Sıfır İlke 2 — Determinizm Reddi:

Suç, ceza, savaş veya toplumsal olaylar mekanik kader değildir. Adil iktisat, ıslah modelleri ve insan iradesi eğilimleri değiştirebilir.





Sıfır İlke 3 — Kesinlik Yasağı:

Hiçbir rapor "mükemmel", "%100", "kesinlikle", "tartışmasız", "sıfır zafiyet" gibi mutlak başarı veya kusursuzluk iddiası içeremez.





Sıfır İlke 4 — Rol Ayrımı:

Analyst, Red Team, QC, Karar Mercii rolleri ayrı ayrıdır; tek kişide birleşemez.





Bölüm 9 — Sayısal Olasılık Yasağı:

Teolojik, ahlaki veya ontolojik çıkarımlara sayısal olasılık verilemez. A/B/C güven düzeyleri kullanılır. Bayes güncellemesi YALNIZCA ölçülebilir göstergelerde (Adım 14/15/19) çalışır; Bölüm 9 yasağı aynen geçerlidir.







İKİNCİ KISIM — 26 ADIMLI ANALİZ MOTORU (v5.2.0)





Her rapor şu adımlardan oluşur. Değişiklik yapılan adımlar \[v5.2.0] etiketiyle işaretlenmiştir.







ADIM 00 — KÜNYE VE GİRİŞ BİLGİLERİ





Rapor başlığı formatı:

GEM RAPOR-2026-0XX — \[Âyet Konusu]





Zorunlu alanlar:



Vaka kodu (örn. GEM-RAPOR-2026-004)

Âyet (sûre:âyet numarası)

Konu başlığı

Tarih

Sürüm (v5.2.0)

Katman (3)

H6 durumu (Evet/Hayır)

Dil (TR / EN)





ADIM 00-5 — 3'LÜ DİL MATRİSİ \[v5.2.0 YENİ — H6 ZORUNLU]





Bu adım YALNIZCA Katman 3 + H6 raporlarında zorunludur. Diğer durumlarda opsiyoneldir.





Format:





3'lü Dil Matrisi:





1\.

Semantik / Kök Anlam:

Kaynak: İbn Fâris (Makâyîsü'l-Lüğa) veya Râgıb el-İsfahânî (el-Müfredât)

Kök: \[âyetteki ana kelimenin kök anlamı]

Sonuç: \[kök anlamından çıkan ilk sonuç]



2\.

Nahiv / Belâğat ve İ'câz:

Kaynak: Zemahşerî (el-Keşşâf)

Tahlil: \[belâğat açısından âyetin yapısı]

Sonuç: \[belâğattan çıkan ikinci sonuç]



3\.

Lisan / Klasik Kullanım:

Kaynak: İbn Manzûr (Lisânü'l-Arab)

Kullanım: \[kelimenin klasik Arapçadaki kullanım alanı]

Sonuç: \[klasik kullanımdan çıkan üçüncü sonuç]





Çapraz Kontrol: Üç sonuç birbirini doğruluyor mu? Uyuşmazlık varsa açıklanır.





Kural: Zemahşerî (2. sıra) HER durumda zorunludur. 1. ve 3. sıra H6 kapsamına bağlıdır.







ADIM 01 — LAFZÎ TAHLİL





Âyetin Arapça metni

Kelime kelime anlam

Zemahşerî (el-Keşşâf) lafzı incelenir — bu zorunludur

\[v5.2.0] H6 raporlarında 3'lü Dil Matrisi'ndeki sonuçlarla çapraz kontrol





ADIM 02 — MANTIKSAL SEMANTİK ANALİZ





Âyetin mantıksal yapısı (koşul, sonuç, istisna)

Kavramsal alanlar

Bağlam içi semantik ilişkiler





ADIM 03 — ÜÇLÜ ÇERÇEVE (ETHOS / LOGOS / PATHOS)





Ethos: Ahlaki yük

Logos: Mantıksal yapı

Pathos: Duygusal etki





ADIM 04 — AMACI (MAKASID) ANALİZİ





Makasıd geleneğine göre âyetin amacı

Şâtıbî, İbn Âşûr, İbnü'l-Kayyim referansları

Beş korunması gereken amaç (can, mal, akıl, nesil, din)





ADIM 04b — YORUMCU KONUMU (GADAMER H3) \[v5.2.0 SIKILAŞTIRILDI]





Zorunlu alanlar:



1.Hangi usul ekolü (Şâfiî / Hanefî / Mâlikî / Hanbelî / Zâhirî / Çoğulcu)

2.Hangi felsefi perspektif (makasıd / pozitivizm / eleştirel realizm / sistemler kuramı vb.)

3.Hangi alternatif perspektiften farklı sonuç üretilebileceği





ADIM 05 — SİYAK-SİBAK ANALİZİ (S1-S7)





S1: Önceki âyet

S2: Sonraki âyet

S3: Sure başı

S4: Sure sonu

S5: Sure teması

S6: Nüzul bağlamı

S7: Kırpma riski — burada MUTLAKA belgeleme yapılır







ADIM 06 — ÇAPRAZ AYET ANALİZİ





Konuyla ilgili diğer âyetler

Kur'an içi tutarlılık kontrolü

İstisna/kural ilişkisi





ADIM 07 — SİSTEM HARİTASI (CAUSAL LOOP DIAGRAM)





Kilit değişkenler

Pekiştirici döngüler (R)

Dengeleyici döngüler (B)

Tipping Point (kırılma noktası) + geri dönülebilirlik seviyesi

Kırılganlık / Direnç / Uyum üçlüsü

Kaldıraç noktası





ADIM 08 — DÖRT SENARYO





1.Koruyucu senaryo

2.Bozuluş senaryo

3.Denge senaryo

4.İhya senaryo



Her senaryo için:



İlke ve dinamik

Sinyal / eşik

Ufuk (H1/H2/H3/H4)

Kalite puanı (O,T,F,A,S)

Karar kolu



Kontenjans notu zorunludur.







ADIM 09 — ZAMAN UFKU BANDI





H1 (0-3 yıl)

H2 (3-10 yıl)

H3 (10-30 yıl)

H4 (30+ yıl)





ADIM 10 — SAYISAL VE MORFOLOJİK LABORATUVAR (Opsiyonel)





Kayıt: Ebced, cıfr veya numeroloji KULLANILMAMIŞTIR (Sıfır İlke C).

Morfolojik gözlem: Kelime kökünün dilsel anlamı.







ADIM 10b — BELİRSİZLİK VE KARAR STRATEJİSİ





Belirsizlik türü (Risk / Uncertainty / Ambiguity)

Karar stratejisi (Robust / Shaping / Adaptive / Preserving)





ADIM 11 — İSTATİSTİKSEL VE EPİSTEMİK GÜVENLİK FRENİ (8 TEST)





1.Test 1: Ayet Sayım Sistemi

2.Test 2: Normalizasyon / İmla

3.Test 3: Texas Sharpshooter

4.Test 4: Permütasyon / Sağlam

5.Test 5: Bağlam ve Tefsir Uyumu (5a-5g)

5a: Sibak

5b: Siyak

5c: Süre bütünlüğü

5d: Nüzul

5e: Hitap kapsamı (N4)

5f: İstisna/kural

5g: Çapraz ayet

6.Test 6: Kesin Tarih Kontrolü

7.Test 7: Kaynak ve Base-Rate Kontrolü \[v5.2.0 SIKILAŞTIRILDI]

7a: Sınıf A/B kaynak

7b: Base-Rate — MUTLAKA somut veri kaynağı içermelidir

Zorunlu alanlar: Endeks adı, kurum adı, yayın yılı, sayısal referans, kaynak sınıfı

"Ampirik olarak sabit" veya "genel olarak bilinmektedir" TEK BAŞINA YETERSİZDİR.

7c: Destekliyor mu?

8.Test 8: Geri Çekilebilirlik





ADIM 12 — KARŞI OKUMA + RED TEAM + FALSIFİABİLİTE





Hat 1: Literalist / Şekilci itiraz + cevap

Hat 2: Seküler / Pozitivist itiraz + cevap





Falsifiabilite Protokolü \[v5.2.0 — YENİ STANDARD]:





Adım 12'de yazılacak falsifiabilite koşulu MUTLAKA şu üç unsuru içermelidir:





1.ZAMAN ARALIĞI: Kaç yıllık pencere içinde ölçülecek? (örn. "5 yıllık pencere")

2.ENDEKS / VERİ KAYNAĞI: Hangi ölçülebilir endeks? (örn. "Dünya Bankası Hukukun Üstünlüğü Endeksi", "Transparency International Yolsuzluk Algı Endeksi", "TÜİK", "UNDP", "Gini")

3.SAYISAL EŞİK: Hangi değer? (örn. "≥ 0.75", "≥ %75")



Format:

"Bu kararı düşürecek veri: \[ZAMAN ARALIĞI] içinde \[ENDEKS ADI] üzerinde ölçülen \[DEĞİŞKEN], \[SAYISAL EŞİK] değerini aşarsa veya altına düşerse bu karar düşer."





Örnek:

"Bu kararı düşürecek veri: 5 yıllık pencere içinde Dünya Bankası Hukukun Üstünlüğü Endeksi'nde ölçülen yolsuzluk denetimi skoru ≥ 0.75 olarak sabitlenirse, yüksek caydırıcılık (nekâl) kararı düşer."





Bu üç unsurdan herhangi biri eksikse falsifiabilite GEÇERSİZ sayılır ve rapor ŞARTLI duruma düşer.







ADIM 13 — MISRİ KATMANI + ENFÜSÎ-KARAR KÖPRÜSÜ





Mısri (iç âlem) tevili

Enfüsî-karar köprüsü: iç ahlak ile dış karar arasındaki bağ

Her karar koluna (K1, K2, K3) etkisi





ADIM 14 — ERKEN UYARI HARİTASI





Gösterge (EU-XX-XX kodu)

Sayısal eşik

Alarm seviyesi (İZLE / HAZIRLIK / MÜDAHALE)

If-Then kartı





\[v5.2.0 — BAYES ALANI — YENİ]:





Prior (başlangıç olasılığı):

Kaynak: \[veri kaynağı]

Değer: \[sayısal değer veya tahmini aralık]

Tarih: \[başlangıç tarihi]





Posterior (güncellenmiş olasılık):

Durum: Henüz hesaplanmadı — ilk veri bekleniyor

Güncelleme kuralı: P(Hipotez | Kanıt) = \[P(Kanıt | Hipotez) × P(Hipotez)] / P(Kanıt)





Kapsam notu: Bayes güncellemesi YALNIZCA bu alanda çalışır. Teolojik veya ahlaki çıkarımlara sayısal katsayı bulaştırılmaz (Bölüm 9 yasağı).







ADIM 15 — KARAR KOLU MATRİSİ (10 ALANLI KART)





1.Seçenek

2.Gerekçe

3.Karar stratejisi

4.Ufuk bandı

5.Sorumlu aktör

6.KPI (ölçülebilir)

7.Trade-off

8\.İkinci derece etki

9.Geri dönüş opsiyonu

10.Etik denetim notu



Ek alan: Adalet türü (Dağıtımsal / Cezalandırıcı / Prosedürel / Nesiller Arası)







ADIM 16 — ETİK VE ÖNYARGI DENETİMİ





Filtreler:



1.Doğrulama yanılması

2.Otorite yanılgısı

3.Güncellik yanılgısı

4.Grup düşüncesi

5.Korku yanılgısı

6\.Çıkar yanılgısı



Her filtre için: Risk durumu + Alınan önlem







QC KAPISI (Adım 16 Sonrası):





&#x20;Snapshot ve metin kilidi aktif mi?

&#x20;Siyak-Sibak (S1-S7) ve nüzul bağlamı işlendi mi?

&#x20;Test 5 alt testleri (5a-5g) ve 8 test gerekçeleri tam mı?

&#x20;Karşıt ilke testi ve İs-Ought köprüsü yazıldı mı?

&#x20;Falsifiabilite ölçülebilir şartla (zaman + endeks + eşik) bağlandı mı? \[v5.2.0]

&#x20;Bayes alanı (prior + posterior) dolduruldu mu? \[v5.2.0]

&#x20;3'lü Dil Matrisi tamam mı? (H6 raporlarında) \[v5.2.0]

&#x20;10 alanlı karar kolu kartı hazır mı?

&#x20;Zemahşerî lafzı tahlilde kullanıldı mı?

&#x20;Bağımsız Dış Okuyucu Protokolü (G3.1): Atandı mı?

&#x20;gem\_lint.py v5.2.2 taramasından geçti mi? \[v5.2.0]





ADIM 17 \& 17b — GÜVEN DÜZEYİ VE AKTÖR HARİTASI





Güven düzeyi: A / B / C

Bilgi düzeyi: SABİT / ARAŞTIRMA NOTU / TESPİT

Sayısal olasılık YOK (Bölüm 9)





Aktör haritası (A1-A7):



A1: Güç odakları

A2: Yargı / güvenlik

A3: Emekçiler / küçük mülk sahipleri

A4: Karşıt aktörler

A5: Sivil toplum / dengeleyiciler

A6: Düzenleyici kurullar

A7: Gelecek nesiller (sessiz aktör — zorunlu)





ADIM 18 — BİLGİ TABANI KARARI VE ZAYIFLIK LİSTESİ





Karar: SABİT / ARAŞTIRMA NOTU / TESPİT

Gerekçe

Zayıflık listesi (numaralı)







ADIM 18.1 — DİL GÜVENLİĞİ





Yasaklı kelimeler (rapor gövdesinde):

mükemmel, %100, kesinlikle, tartışmasız, sıfır zafiyet, sıfır metodolojik zafiyet, ispatlanmıştır, kanıtlanmıştır, onaylandı (tam uyum), tam uyum, herkesçe bilinmektedir, tartışmaya kapalı





İngilizce:

flawless, 100%, absolutely, indisputably, zero vulnerability, proven, universally known, beyond dispute, definitively proven





Koşullu yasaklı (uyarı): mutlak, absolute





İstisna: "mutlak mülkiyet", "mutlak sahip", "mutlak egemenlik" vb. naṣṣ bağlamları.





18.1-B MUAFİYET \[v5.2.0]:

Yasaklı kelimeler aşağıdaki bağlamlarda serbesttir:



1.Tırnak içi örnek gösterim olarak (örnek: "mükemmel" kelimesi yasaktır).

2.Linter kural listesinde (gem\_lint.py değişken tanımları).

3.Tarihî veya karşıt görüş alıntısı olarak (örnek: Red Team itirazı içinde).



Bu üç bağlam dışında her kullanım ihlaldir.







ADIM 19 — İZLEME DÖNGÜSÜ + RETRODICTION





İzleme KPI (ölçülebilir)





Retroadiction formatı:



1.Dönem (tarihsel olay)

2.O tarihte bu metodoloji ne söylerdi?

3.Gerçekleşti mi?

4.Karşı örnek

5.Sonuç (Doğrulandı / Kısmen doğrulandı / Çürütüldü)





ADIM 20 — AÇIK SORULAR VE VARSAYIM KAYDI





Açık soru (numaralı)

Varsayım (numaralı)







ÜÇÜNCÜ KISIM — RAPOR SONU ZORUNLU KAYITLAR





1.Yasal / Metodolojik Uyarı

2.Otorite Reddi (Sıfır İlke 1)

3.Determinizm Reddi (Sıfır İlke 2)

4.Kaynak Etiketleri (Sınıf A / B)

5.Dil Güvenliği Taraması (18.1)

6.Falsifiabilite Kontrolü (12)

7.Bağımsız Dış Denetim (G3.1)

8\.Öz-Denetim Notu



Onay Zinciri:



Analyst

Red Team (Karşı Okuyucu)

QC Sorumlusu

Karar Mercii





DÖRDÜNCÜ KISIM — PARADOKSAL DİL FİLTRESİ \[v5.2.0 YENİ]





v5.1.3'te tespit edilen metin-içi gerilim: kural metni, yasakladığı kelimeleri kuralı anlatırken kullanmak zorunda kalıyor.





ÇÖZÜM (18.1-B):



Talimat metninde: tırnak içi + "örnek" etiketi → serbest

Rapor gövdesinde: yasak

Linter kodunda: serbest



Bu kural gem\_lint.py v5.2.2'de otomatik uygulanmaktadır.







BEŞİNCİ KISIM — BAYES DİSİPLİNİ \[v5.2.0 YENİ]





KAPSAM SINIRI:





Bayes güncellemesi YALNIZCA şu alanlarda çalışır:



Adım 14: Erken uyarı göstergeleri (sayısal eşikler)

Adım 15: Karar kolu KPI'ları (ölçülebilir hedefler)

Adım 19: İzleme KPI'ları (ampirik veri)



Bayes güncellemesi şu alanlarda ASLA çalışmaz:



Adım 17: Güven düzeyi (A/B/C) — Bölüm 9 yasağı

Adım 18: Bilgi tabanı kararı (SABİT / ARAŞTIRMA NOTU)

Teolojik veya ahlaki çıkarımlar



Formül:

P(Hipotez | Kanıt) = \[P(Kanıt | Hipotez) × P(Hipotez)] / P(Kanıt)





Kullanım:



Prior: Adım 14/19'da verilen başlangıç değeri

Likelihood: Yeni ampirik veri

Posterior: Sonraki rapor revizyonunda güncellenir





ALTINCI KISIM — 3'LÜ DİL MATRİSİ KAPSAM KURALI \[v5.2.0 YENİ]





ZORUNLU:



1.Katman 3 raporlarda + H6 Zorlu Âyet kapsamındaki analizlerde

2\.Çift okuma sonucunda anlaşmazlık çıktığında



OPSİYONEL:



Katman 1-2 raporlarında



NEDEN SINIRLI: v5.1.2'de 26 adımın bürokrasiyi aşırı artırdığı tespit edilmişti. 3'lü matrisin kapsamı sınırlı tutularak bu hata tekrarlanmamalıdır.







YEDİNCİ KISIM — FALSIFİABİLİTE STANDARDI \[v5.2.0 YENİ]





ZORUNLU ÜÇ UNSUR:



1.Zaman aralığı (yıl/pencere)

2.Endeks / veri kaynağı (ölçülebilir)

3.Sayısal eşik (≥ veya ≤ değer)



Eksikse: Rapor ŞARTLI duruma düşer.





SOYUT KOŞUL YASAĞI:

"Aksine icmaî nass bulunursa" veya "pratikte imkânsız koşul" yazılamaz. Falsifiabilite MUTLAKA erişilebilir ve ölçülebilir olmalıdır.







SEKİZİNCİ KISIM — BASE-RATE STANDARDI \[v5.2.0 YENİ]





Test 7(b) alanı MUTLAKA şunları içermelidir:



1.Somut veri kaynağı (endeks adı, kurum adı, yayın yılı)

2.Sayısal referans (örn. "residivizm oranı %50-70")

3.Kaynak sınıfı (SINIF A veya SINIF B)



YETERSİZ İFADELER:



"Ampirik olarak sabit"

"Genel olarak bilinmektedir"

"Yaygın kabul görmektedir"





DOKUZUNCU KISIM — DIŞ DENETİM PROTOKOLÜ (G3.1)





Dış denetim üç yoldan herhangi biriyle karşılanabilir:



1.Bireysel dış okuyucu ataması (mevcut kural)

2.Peer-Review Havuzu: Git tabanlı pull-request sistemi (asenkron)

3\.Üniversite konsorsiyumu veya ilmi heyet onayı



Darboğaz durumunda (30 gün içinde dış okuyucu bulunamazsa):



Rapor "ÖN ONAYLI" statüsüyle yayınlanabilir

Başlangıçta "Bağımsız dış denetim beklenmektedir" uyarısı

Denetim tamamlandığında "ONAYLI" statüsüne güncellenir





ONUNCU KISIM — GEM\_LINT.PY v5.2.2 ENTEGRASYONU





Her rapor yayınlanmadan ÖNCE linter taramasından geçmelidir.





Komutlar:

python src/gem\_lint.py rapor.md

python src/gem\_lint.py rapor.md --katman 3

python src/gem\_lint.py rapor.md --katman 3 --h6





Sonuç eşikleri:



🟢 GEÇTİ → Yayınlanabilir (Red Team önerilir)

🟡 GEÇTİ (Şartlı) → Küçük düzeltme yapılmalı

🟡 ŞARTLI → Düzeltilmeden yayınlanmamalı

🔴 DÜŞTÜ → Rapor derlenemez, yeniden yazılmalı



Onay zincirine yeni satır:

Dil Denetimi: gem\_lint.py v5.2.2 otomatik taraması (GEÇTİ / ŞARTLI / DÜŞTÜ)







EKLER





EK A — YASAKLI KELİMELER TAM LİSTESİ





Türkçe (hard fail):



1.mükemmel

2.%100

3.kesinlikle

4.tartışmasız

5.sıfır zafiyet

6.sıfır metodolojik zafiyet

7.ispatlanmıştır

8.kanıtlanmıştır

9.onaylandı (tam uyum)

10.tam uyum

11.herkesçe bilinmektedir

12.tartışmaya kapalı



İngilizce (hard fail):



1.flawless

2.100%

3.absolutely

4.indisputably

5.zero vulnerability

6.proven

7.universally known

8.beyond dispute

9.definitively proven



Koşullu (uyarı):



1.mutlak / absolute





EK B — ZORUNLU BÖLÜMLER KONTROL LİSTESİ





Genel (tüm raporlar):



Yorumcu konumu

Zemahşerî (el-Keşşâf)

Falsifiabilite / Yanlışlanabilirlik

Tipping Point / Kırılma noktası

N4

S7

Zayıflık

Geliştirme önerisi

Öz-denetim

Dil güvenliği

Karar kolu

Aktör

Retrodiction / Retroadiction

Karşıt ilke

İs-Ought köprüsü

Hume giyotini

Künye

Güven düzeyi

Bilgi düzeyi



Katman 3 ek:



Zaman aralığı

Endeks / veri kaynağı

Sayısal eşik

Prior

Posterior

Bayes



H6 ek:



3'lü Dil Matrisi

İbn Fâris

İbn Manzûr





EK C — KAYNAK LİSTESİ





Klasik Tefsir Zemini (SINIF A):



Zemahşerî, el-Keşşâf

Taberî, Câmiu'l-Beyân

Cessâs, Ahkâmü'l-Kur'ân



Dil Zemini \[v5.2.0]:



İbn Fâris, Makâyîsü'l-Lüğa (SINIF A)

Râgıb el-İsfahânî, el-Müfredât (SINIF A)

İbn Manzûr, Lisânü'l-Arab (SINIF A)



Makasıd Zemini (SINIF A):



Şâtıbî, el-Muvâfakât

İbn Âşûr, Makasıdü'ş-Şerîa

İbnü'l-Kayyim, İ'lâmü'l-Muvakkıîn



Felsefi / İktisadi Zemin (SINIF B):



Beccaria, Dei Delitti e Delle Pene (1764)

Hernando De Soto, The Mystery of Capital (2000)





EK D — SÜRÜM GEÇMİŞİ





v5.1.3 → v5.2.0 Değişiklikleri:



1.Paradoksal dil filtresi çözümü (18.1-B)

2.Falsifiabilite standardı (zaman + endeks + eşik)

3.Bayes disiplini (yalnız ölçülebilir)

4.3'lü Dil Matrisi (sınırlı kapsam)

5.Dış denetim darboğaz çözümü (G3.1 genişletme)

6.Base-rate standardı (Test 7b sıkılaştırma)

7.Yorumcu konumu sıkılaştırması (H3)

8.gem\_lint.py v5.2.2 linter entegrasyonu

9.Geriye dönük işler (DV-001 + H6 kapanış)

10.Sürüm numarası ve onay zinciri güncellemesi





ONAY





Hazırlayan: GEM Talimat Geliştirme Masası

Denetim: Bağımsız Kalite ve Etik Kapısı

Linter: gem\_lint.py v5.2.2

Durum: ONAYLANDI (v5.2.0 — Yürürlükte)

