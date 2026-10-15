from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent.parent
DOCS_TR = ROOT / "docs" / "tr"

LAFZI_BLOCKS = {
    "12-rapor-hucurat-49910-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (Hucurât Sûresi 49:9–10 — Resm-i Osmânî):**
  > وَإِن طَآئِفَتَانِ مِنَ ٱلْمُؤْمِنِينَ ٱقْتَتَلُوا۟ فَأَصْلِحُوا۟ بَيْنَهُمَا ۖ فَإِنۢ بَغَتْ إِحْدَىٰهُمَا عَلَى ٱلْأُخْرَىٰ فَقَـٰتِلُوا۟ ٱلَّتِى تَبْغِى حَتَّىٰ تَفِىٓءَ إِلَىٰٓ أَمْرِ ٱللَّهِ ۚ فَإِن فَآءَتْ فَأَصْلِحُوا۟ بَيْنَهُمَا بِٱلْعَدْلِ وَأَقْسِطُوٓا۟ ۖ إِنَّ ٱللَّهَ يُحِبُّ ٱلْمُقْسِطِينَ ﴿٩﴾ إِنَّمَا ٱلْمُؤْمِنُونَ إِخْوَةٌ فَأَصْلِحُوا۟ بَيْنَ أَخَوَيْكُمْ ۚ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُرْحَمُونَ ﴿١٠﴾

- **Sahih Türkçe Meal:**
  > *"Eğer müminlerden iki topluluk birbirleriyle vuruşacak olurlarsa aralarını derhal düzeltin (ıslah edin). Şayet biri ötekine saldırıp haddi aşarsa (bağy ederse), Allah’ın buyruğuna (hak ve hukuka) dönünceye kadar o mütecaviz tarafla mücadele edin. Eğer dönerse, artık aralarını adaletle düzeltin ve tam bir hakkaniyetle (kıst ile) hareket edin; şüphesiz Allah adil davrananları (muksitleri) sever. (9) Müminler ancak kardeştirler; öyleyse iki kardeşinizin arasını düzeltin ve Allah’a karşı sorumluluk bilinciyle (takvâ ile) hareket edin ki merhamete erişesiniz. (10)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `وَإِن طَآئِفَتَانِ مِنَ ٱلْمُؤْمِنِينَ` (Ve in tâifetâni mine'l-mü'minîn): Eğer müminlerden iki zümre / topluluk (tesniye kalıbıyla gelse de lafzı cem‘ manası taşıdığı için devamındaki fiil çoğul gelmiştir).
  - `ٱقْتَتَلُوا۟` (iktetelû): Birbirleriyle çarpışırlarsa, fiilî çatışmaya girerlerse (*ifti‘âl* bâbından işteşlik/müşâreket bildirir; çatışmanın iki taraf arasında vuku bulduğunu gösterir).
  - `فَأَصْلِحُوا۟ بَيْنَهُمَا` (fe-aslihû beynehümâ): Derhal aralarını ıslah edin; öğüt, arabuluculuk ve sulh çağrısıyla çatışmayı durdurun.
  - `فَإِنۢ بَغَتْ إِحْدَىٰهُمَا عَلَى ٱلْأُخْرَىٰ` (fe-in bağat ihdâhümâ ‘ale'l-uhrâ): Şayet ikisinden biri diğerine karşı haddi aşar, sulhu reddedip zulüm ve tecavüze (bağy) kalkışırsa.
  - `فَقَـٰتِلُوا۟ ٱلَّتِى تَبْغِى` (fe-kâtilü'lletî tebğî): O haddi aşan / mütecaviz grupla (zulmü durdurmak üzere kolektif meşru güçle) mücadele edin.
  - `حَتَّىٰ تَفِىٓءَ إِلَىٰٓ أَمْرِ ٱللَّهِ` (hattâ tefîe ilâ emrillâh): Allah’ın hükmüne, hakemliğine ve hukuk düzenine rücû edip dönünceye kadar (mücadelenin hedefi imha değil, hukuka döndürmektir).
  - `فَإِن فَآءَتْ فَأَصْلِحُوا۟ بَيْنَهُمَا بِٱلْعَدْلِ` (fe-in fâet fe-aslihû beynehümâ bi'l-‘adl): Eğer hukuka dönerse, artık aralarını rövanşizmle değil tam bir adaletle ıslah edin.
  - `وَأَقْسِطُوٓا۟ ۖ إِنَّ ٱللَّهَ يُحِبُّ ٱلْمُقْسِطِينَ` (ve aksitû innallâhe yuhibbü'l-muksitîn): Hakkaniyeti (kıstı) ayakta tutun; Allah hakkaniyetle hükmedenleri sever.
  - `إِنَّمَا ٱلْمُؤْمِنُونَ إِخْوَةٌ` (İnneme'l-mü'minûne ihvetün): Müminler ancak ve yalnızca kardeştirler (*innemâ* hasr edatıyla çatışma halinde dahi iman kardeşliği hukukunun düşmediği tescil edilmiştir).
  - `فَأَصْلِحُوا۟ بَيْنَ أَخَوَيْكُمْ` (fe-aslihû beyne ehaveyküm): Öyleyse iki kardeşinizin arasını düzeltin (9. âyetteki 'iki grup', 10. âyette 'iki öz kardeş' mertebesine indirilerek şefkat ve uzlaşı zemini güçlendirilmiştir).

- **Klasik Tefsir Lafzî Tahlili (Kurtubî & Fahreddîn er-Râzî):**
  - `[NAKİL]`: Kurtubî (*el-Câmi‘ li-Ahkâmi'l-Kur'ân*, C. 16, s. 315–322), âyette birbirleriyle savaşan ve biri diğerine *bağy* (zulüm/isyan) eden zümrelerin hâlâ *"el-mü'minîn"* ve *"ihvetün"* (müminler ve kardeşler) olarak isimlendirilmesinin, büyük günah işleyen kimsenin imandan çıkmadığının (Ehl-i Sünnet kaidesinin) en açık nassı olduğunu; ayrıca *"bi'l-adl"* kaydının çatışma sonrası galiplerin mağluplara keyfî şartlar dayatmasını kesin olarak haram kıldığını belirtir.[^1]
  - `[YORUM]`: Lafzî dizilim 3 aşamalı bir barış inşası protokolü kurar: (1) Önleyici diplomasi ve sulh (`fe-aslihû`), (2) Sulhu reddeden mütecavizi hukuka döndürmeye matuf orantılı caydırıcılık (`hattâ tefîe`), (3) Çatışma sonrası rövanşizmden arınmış adil yeniden inşa (`bi'l-adl ve aksitû`).

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "13-rapor-isra-1736-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (İsrâ Sûresi 17:36 — Resm-i Osmânî):**
  > وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِۦ عِلْمٌ ۚ إِنَّ ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ كُلُّ أُو۟لَـٰٓئِكَ كَانَ عَنْهُ مَسْـُٔولًا ﴿٣٦﴾

- **Sahih Türkçe Meal:**
  > *"Hakkında kesin bilgin olmayan şeyin peşine düşme (ardına takılıp hüküm verme)! Çünkü kulak, göz ve kalp (fuâd); bunların hepsi ondan (yaptığı tahkik ve eylemden) sorumludur / sorguya çekilecektir. (36)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `وَلَا تَقْفُ` (Ve lâ takfu): Ardına düşme, izini sürme, peşine takılıp konuşma ve hüküm verme! (`kafâ - yakfû - kafven` kökünden nehy-i hâzır; illet harfi vav cezm alameti olarak düşmüştür).
  - `مَا لَيْسَ لَكَ بِهِۦ عِلْمٌ` (mâ leyse leke bihî ‘ilm): Senin için kendisi hakkında doğrulanmış, yakînî veya delilli bir bilgi (`‘ilm`) bulunmayan şey (nekre olarak gelen `‘ilm`, nefy siyâkında umum ifade ederek her türlü temelsiz zan, dedikodu, yalan şahitlik ve tahkiksiz iddiayı kapsar).
  - `إِنَّ ٱلسَّمْعَ` (inne's-sem‘a): Şüphesiz kulak / işitme yetisi (işitsel ve naklî bilginin giriş kapısı; tekil mastar kalıbıyla cins isim olarak bütün işitme süreçlerini kuşatır).
  - `وَٱلْبَصَرَ` (ve'l-basara): Ve göz / görme yetisi (gözleme, deneye ve görsel şahitliğe dayalı ampirik bilginin giriş kapısı).
  - `وَٱلْفُؤَادَ` (ve'l-füâde): Ve kalp / zihnî-ahlaki muhakeme merkezi (`füâd`, `fekd/tefevvüd` kökünden tutuşup parlayan idrak, akıl ve vicdan süzgecidir; duyulardan gelen ham veriyi analiz edip hükme bağlayan merkezdir).
  - `كُلُّ أُو۟لَـٰٓئِكَ` (küllü ülâike): İşte bütün bu yetilerin her biri (`ülâike` işaret zamiri normalde akıl sahipleri için kullanılırken burada kulak, göz ve kalbin şuurlu birer şahit gibi muhatap alınacağını göstermek üzere istiâre/teşhis sanatıyla kullanılmıştır).
  - `كَانَ عَنْهُ مَسْـُٔولًا` (kâne ‘anhü mes'ûlâ): Ondan (sahibinin bu yetileri nasıl kullandığından veya bu yetilerin bizzat kendisinden) kesin olarak hesap sorulacaktır.

- **Klasik Tefsir Lafzî Tahlili (Fahreddîn er-Râzî & İbn Âşûr):**
  - `[NAKİL]`: Fahreddîn er-Râzî (*Mefâtîhu'l-Gayb*, C. 20, s. 209–212), âyetteki `lâ takfu` nehyinin hem itikadî konularda taklit ve zannı, hem fıkhî/kazâî konularda delilsiz şahitliği ve iftirayı, hem de toplumsal hayatta teyitsiz haber yaymayı kapsadığını; `sem‘`, `basar` ve `füâd` sıralamasının ise insan bilgisinin *duyu verisi -> gözlem -> rasyonel/vicdani muhakeme* hiyerarşisini kusursuz biçimde ortaya koyduğunu vurgular.[^1]
  - `[YORUM]`: Âyet-i kerîme, modern epistemolojinin "gerekçelendirilmiş doğru inanç" (*justified true belief*) şartını ahlaki ve hukuki hesap verebilirlikle (`mes'ûlâ`) birleştirerek; teyitsiz paylaşımı, sahte haberi ve algoritmik dezenformasyonu doğrudan kulak, göz ve kalp emanetine ihanet olarak tanımlar.

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "14-rapor-hasr-597-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (Haşr Sûresi 59:7 — Resm-i Osmânî):**
  > مَّآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْ أَهْلِ ٱلْقُرَىٰ فَلِلَّهِ وَلِلرَّسُولِ وَلِذِى ٱلْقُرْبَىٰ وَٱلْيَتَـٰمَىٰ وَٱلْمَسَـٰكِينِ وَٱبْنِ ٱلسَّبِيلِ كَىْ لَا يَكُونَ دُولَةًۢ بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ ۚ وَمَآ ءَاتَىٰكُمُ ٱلرَّسُولُ فَخُذُوهُ وَمَا نَهَىٰكُمْ عَنْهُ فَٱنتَهُوا۟ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ ﴿٧﴾

- **Sahih Türkçe Meal:**
  > *"Allah’ın, (fethedilen) beldelerin halkından Resûlüne fey olarak (savaşsız kamu gelirleriyle) verdiği mallar; Allah’a, Resûlüne, yakınlara, yetimlere, yoksullara ve yolda kalmışlara aittir. Bu, o malların içinizden yalnızca zenginler arasında elden ele dolaşan bir servet tekeli (dûleten) haline gelmemesi içindir. Peygamber size ne verdiyse onu alın, sizi neden menettiyse ondan da sakının. Allah’a karşı gelmekten sakının; şüphesiz Allah’ın cezası pek çetindir. (7)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `مَّآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ` (Mâ efâallâhu ‘alâ rasûlihî): Allah’ın Resûlüne fey olarak döndürüp nasip ettiği kamu kaynakları (`fey’`, gölgenin dönmesi gibi servetin asıl gayesi olan kamu yararına rücû etmesidir).
  - `مِنْ أَهْلِ ٱلْقُرَىٰ` (min ehli'l-kurâ): Beldelerin / şehirlerin ahalisinden (savaşsız anlaşmalarla ve kamu hukuku yoluyla hazineye intikal eden gelirler).
  - `فَلِلَّهِ وَلِلرَّسُولِ` (fe-lillâhi ve li'r-rasûli): Allah’a ve Resûlüne aittir (yani kamu otoritesinin genel maslahat ve adalet harcamalarına tahsis edilir).
  - `وَلِذِى ٱلْقُرْبَىٰ وَٱلْيَتَـٰمَىٰ` (ve li-zi'l-kurbâ ve'l-yetâmâ): Yakınlara ve cemiyet içinde hâmisiz kalan yetimlere.
  - `وَٱلْمَسَـٰكِينِ وَٱبْنِ ٱلسَّبِيلِ` (ve'l-mesâkîni vebni's-sebîl): Geçim darlığı çeken yoksullara ve memleketinden uzakta çaresiz kalmış yolculara/muhacirlere.
  - `كَىْ لَا يَكُونَ دُولَةًۢ` (key lâ yekûne dûleten): Ta ki o servet sadece belirli bir zümrenin tekelinde dönüp duran bir meta (`dûle`) olmasın! (`key` ta‘lîl/illet edatıdır; İslam iktisat hukukunun en temel *hikmet-i teşrî‘* ve *illet* cümlesidir).
  - `بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ` (beyne'l-ağniyâi minküm): İçinizden yalnızca zenginler / sermaye sahipleri arasında (kapalı devre dolaşan bir rant çarkı olmasın).
  - `وَمَآ ءَاتَىٰكُمُ ٱلرَّسُولُ فَخُذُوهُ وَمَا نَهَىٰكُمْ عَنْهُ فَٱنتَهُوا۟` (ve mâ âtâkümü'r-rasûlü fe-huzûhü ve mâ nehâküm ‘anhü fentehû): Resûl size neyi verdiyse (ve neyi emrettiyse) onu alın; sizi neden nehyettiyse ondan derhal vazgeçin (hem mali taksimde hem de küllî teşrî‘de Sünnetin bağlayıcılık delili).

- **Klasik Tefsir Lafzî Tahlili (İbn Âşûr & Cessâs):**
  - `[NAKİL]`: İbn Âşûr (*et-Tahrîr ve't-Tenvîr*, C. 28, s. 84–91), `key lâ yekûne dûleten beyne'l-ağniyâi minküm` cümlesinin İslam maliye ve iktisat hukukunda **külli bir makâsıd kaidesi (aslün ‘azîm)** olduğunu; Şâri‘in servetin dar bir oligarşi elinde toplanmasını (temerküz/tekelleşme) açıkça gayrimeşru ilan ettiğini ve kamu maliyesinin serveti tabana yaymakla yükümlü olduğunu belirtir.[^1]
  - `[YORUM]`: Âyetin lafzî mimarisi mülkiyet hakkını ortadan kaldırmaz; fakat kamu kaynaklarının ve iktisadi büyümenin sadece en üst gelir dilimi arasında kapalı devre dönmesini (`dûle`) toplumsal çöküş sebebi sayarak kırılgan kesimler lehine yapısal yeniden bölüşümü emreder.

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "15-rapor-rum-3022-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (Rûm Sûresi 30:22 — Resm-i Osmânî):**
  > وَمِنْ ءَايَـٰتِهِۦ خَلْقُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَـٰفُ أَلْسِنَتِكُمْ وَأَلْوَٰنِكُمْ ۚ إِنَّ فِى ذَٰلِكَ لَـَٔايَـٰتٍ لِّلْعَـٰلِمِينَ ﴿٢٢﴾

- **Sahih Türkçe Meal:**
  > *"Göklerin ve yerin yaratılması ile dillerinizin ve renklerinizin farklılığı da O’nun (kudret ve hikmetinin) âyetlerindendir (delillerindendir). Şüphesiz bunda bilenler (âlimler / derin kavrayış sahipleri) için nice ibretler ve işaretler vardır. (22)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `وَمِنْ ءَايَـٰتِهِۦ` (Ve min âyâtihî): O’nun (Allah’ın varlığının, birliğinin ve sonsuz hikmetinin) kevnî âyetlerinden / mucizevi delillerindendir.
  - `خَلْقُ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضِ` (halku's-semâvâti ve'l-ard): Göklerin ve yerin yoktan ve kusursuz bir ölçüyle yaratılması.
  - `وَٱخْتِلَـٰفُ أَلْسِنَتِكُمْ` (vahtilâfü elsinetiküm): Ve dillerinizin, lehçelerinizin, ses tonlarınızın ve ifade biçimlerinizin çeşitliliği (`elsine`, `lisân` kelimesinin çoğuludur; hem fonetik ses farklılığını hem de dünya dillerinin çoğulculuğunu kapsar).
  - `وَأَلْوَٰنِكُمْ` (ve elvâniküm): Ve ten renklerinizin, ırkî/fizyolojik simalarınızın ve fıtrî mizaçlarınızın çeşitliliği (`elvân`, `levn` kelimesinin çoğuludur).
  - `إِنَّ فِى ذَٰلِكَ لَـَٔايَـٰتٍ` (inne fî zâlike le-âyâtin): Şüphesiz bütün bunlarda kesin ve çoğul deliller / dersler vardır.
  - `لِّلْعَـٰلِمِينَ` (li'l-‘âlimîn): Âlimler / ilim ve basiret sahipleri için (Hafs kıraatinde lam’ın kesresiyle `li'l-‘âlimîn` [bilenler, bilginler]; diğer mütevatir kıraatte fethasıyla `li'l-‘âlemîn` [bütün âlemler] okunarak hem bilimsel derinliğe hem evrensel insanlığa işaret edilmiştir).

- **Klasik Tefsir Lafzî Tahlili (Taberî, Râzî & İbn Âşûr):**
  - `[NAKİL]`: Fahreddîn er-Râzî (*Mefâtîhu'l-Gayb*, C. 25, s. 96–98) ve İbn Âşûr (*et-Tahrîr ve't-Tenvîr*, C. 21, s. 68–71), dillerin ve renklerin farklılığının (`ihtilâf`) göklerin ve yerin yaratılışıyla (`halku's-semâvâti ve'l-ard`) aynı cümlede eşdeğer bir "ilahi âyet" olarak zikredilmesine dikkat çekerler: Nasıl ki gökleri ve yeri tahrip etmek ilahi sanata saldırıysa, insanlığın dil ve renk çeşitliliğini zorla tek tipleştirmeye çalışmak veya bir rengi/dili diğerine üstün görmek de Allah’ın kevnî âyetleriyle savaşmaktır.[^1]
  - `[YORUM]`: Lafzî düzlemde `ihtilâf` (çeşitlilik) bir arıza, ceza veya çatışma sebebi değil; bizzat Yaratıcı’nın murat ettiği kozmik bir güzellik ve ontolojik eşitlik delilidir.

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "16-rapor-enam-6151152-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (En'âm Sûresi 6:151–152 — Resm-i Osmânî):**
  > قُلْ تَعَالَوْا۟ أَتْلُ مَا حَرَّمَ رَبُّكُمْ عَلَيْكُمْ ۖ أَلَّا تُشْرِكُوا۟ بِهِۦ شَيْـًٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَـٰنًا ۖ وَلَا تَقْتُلُوٓا۟ أَوْلَـٰدَكُم مِّنْ إِمْلَـٰقٍ ۖ نَّحْنُ نَرْزُقُكُمْ وَإِيَّاهُمْ ۖ وَلَا تَقْرَبُوا۟ ٱلْفَوَٰحِشَ مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ ۖ وَلَا تَقْتُلُوا۟ ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ إِلَّا بِٱلْحَقِّ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَعْقِلُونَ ﴿١٥١﴾ وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ ۖ وَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ بِٱلْقِسْطِ ۖ لَا نُكَلِّفُ نَفْسًا إِلَّا وُسْعَهَا ۖ وَإِذَا قُلْتُمْ فَٱعْدِلُوا۟ وَلَوْ كَانَ ذَا قُرْبَىٰ ۖ وَبِعَهْدِ ٱللَّهِ أَوْفُوا۟ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَذَكَّرُونَ ﴿١٥٢﴾

- **Sahih Türkçe Meal:**
  > *"De ki: Gelin, Rabbinizin size neleri haram kıldığını (ve neleri emrettiğini) okuyayım: O’na hiçbir şeyi ortak koşmayın, anne-babaya iyilikle (ihsanla) muamele edin, yoksulluk korkusuyla çocuklarınızı öldürmeyin —sizi de onları da rızıklandıran Biziz—; kötülüklerin (fevâhişin) açığına da gizlisine de yaklaşmayın ve Allah’ın dokunulmaz (haram) kıldığı cana haklı bir (hukuki) sebep olmadıkça kıymayın! İşte aklınızı kullanasınız diye Allah size bunları vasiyet etti. (151) Rüşdüne (olgunluk çağına) erişinceye kadar yetimin malına, en güzel (onun menfaatine en uygun) şeklin dışında yaklaşmayın; ölçüyü ve tartıyı adaletle (kıst ile) tam yapın —Biz hiçbir kimseye gücünün yettiğinden fazlasını yüklemeyiz—; konuştuğunuz (veya şahitlik/hakemlik yaptığınız) zaman yakınınız dahi olsa adaleti gözetin ve Allah’a verdiğiniz ahdi tam yerine getirin! İşte düşünüp öğüt alasınız diye Allah size bunları vasiyet etti. (152)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `قُلْ تَعَالَوْا۟ أَتْلُ` (Kul te‘âlev etlü): De ki: Gelin (yüksek bir hakikat ve ahlak ufkuna yükselin), size okuyup beyan edeyim (`te‘âlev`, aslen yüksek bir yere çağırmak olup cehalet ve zulüm çukurundan evrensel hukuk zirvesine daveti ifade eder).
  - `وَلَا تَقْتُلُوٓا۟ أَوْلَـٰدَكُم مِّنْ إِمْلَـٰقٍ` (ve lâ taktülû evlâdeküm min imlâk): Yoksulluk / açlık (`imlâk`) yüzünden çocuklarınızın canına kıymayın.
  - `وَلَا تَقْرَبُوا۟ ٱلْفَوَٰحِشَ مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ` (ve lâ takrabü'l-fevâhişe mâ zahera minhâ ve mâ batan): Çirkinliklerin / ahlaksızlıkların alenî olanına da gizli olanına da yaklaşmayın (`lâ takrabû`, fiilin kendisini değil ona götüren öncülleri de yasaklayan sedd-i zerâi‘ kalıbıdır).
  - `وَلَا تَقْتُلُوا۟ ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ إِلَّا بِٱلْحَقِّ` (ve lâ taktülü'n-nefse'lletî harramallâhu illâ bi'l-hakk): Allah’ın dokunulmaz kıldığı insan canına hukuki/meşru bir gerekçe (`bi'l-hakk`) dışında dokunmayın.
  - `وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ` (ve lâ takrabû mâle'l-yetîmi illâ bi'lletî hiye ahsen): Yetimin malına, onun malını koruyup nemalandıracak en güzel yol dışında yaklaşmayın.
  - `وَأَوْفُوا۟ ٱلْكَيْلَ وَٱلْمِيزَانَ بِٱلْقِسْطِ` (ve evfü'l-keyle ve'l-mîzâne bi'l-kıst): Ölçüyü ve tartıyı tam ve adil (`kıst`) olarak yerine getirin (iktisadi ve ticari standartlarda sıfır hile ilkesi).
  - `وَإِذَا قُلْتُمْ فَٱعْدِلُوا۟ وَلَوْ كَانَ ذَا قُرْبَىٰ` (ve izâ kultüm fa‘dilû ve lev kâne zâ kurbâ): Söz söylediğinizde, şahitlik ettiğinizde veya hüküm verdiğinizde —lehine veya aleyhine konuştuğunuz kişi öz akrabanız (`zâ kurbâ`) dahi olsa— tam adaletle konuşun!

- **Klasik Tefsir Lafzî Tahlili (İbn Mes‘ûd Rivayeti, Taberî & Kurtubî):**
  - `[NAKİL]`: Abdullah b. Mes‘ûd (r.a.) bu âyetler hakkında *"Kim üzerinde Hz. Muhammed’in (s.a.v.) mührü bulunan ilahi vasiyetnameyi okumak isterse En'âm 151–153. âyetleri okusun"* buyurmuş; Kurtubî (*el-Câmi‘*, C. 7, s. 132–140) ve İbn Âşûr bu âyetlerin bütün semavî şeriatlarda neshedilmeyen **Evrensel Ahlak ve İnsan Hakları Anayasası (el-Muhkemât)** olduğunu belirtmiştir.[^1]
  - `[YORUM]`: Âyet, yaşam hakkı (`nefs`), kırılgan çocuk ve yetim hakları (`evlâd/yetîm`), piyasa dürüstlüğü (`keyl/mîzân`) ve yargıda akraba kayırmacılığı yasağını (`ve lev kâne zâ kurbâ`) tek bir bağlayıcı "İlahi Vasiyet" (`vassâküm bihî`) altında birleştirir.

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "17-rapor-hadid-5725-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (Hadîd Sûresi 57:25 — Resm-i Osmânî):**
  > لَقَدْ أَرْسَلْنَا رُسُلَنَا بِٱلْبَيِّنَـٰتِ وَأَنزَلْنَا مَعَهُمُ ٱلْكِتَـٰبَ وَٱلْمِيزَانَ لِيَقُومَ ٱلنَّاسُ بِٱلْقِسْطِ ۖ وَأَنزَلْنَا ٱلْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَـٰفِعُ لِلنَّاسِ وَلِيَعْلَمَ ٱللَّهُ مَن يَنصُرُهُۥ وَرُسُلَهُۥ بِٱلْغَيْبِ ۚ إِنَّ ٱللَّهَ قَوِىٌّ عَزِيزٌ ﴿٢٥﴾

- **Sahih Türkçe Meal:**
  > *"Andolsun Biz peygamberlerimizi açık delillerle (beyyinelerle) gönderdik ve insanların adaleti (kıstı) bizzat ayakta tutmaları için onlarla birlikte Kitab’ı ve Mîzân’ı (adalet ölçüsünü) indirdik. Ve kendisinde çetin bir güç (caydırıcı kudret) ve insanlar için çeşitli faydalar bulunan demiri de indirdik (var ettik); ta ki Allah, görmediği halde (gaybda) kendisine ve peygamberlerine kimin yardım edeceğini ortaya çıkarsın. Şüphesiz Allah mutlak güç sahibidir, daima üstündür. (25)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `لَقَدْ أَرْسَلْنَا رُسُلَنَا بِٱلْبَيِّنَـٰتِ` (Lekad erselnâ rusülenâ bi'l-beyyinât): Yemin olsun ki elçilerimizi apaçık deliller, burhanlar ve mucizelerle gönderdik.
  - `وَأَنزَلْنَا مَعَهُمُ ٱلْكِتَـٰبَ` (ve enzelnâ me‘ahümü'l-kitâbe): Ve onlarla birlikte ilahi vahyi ve yazılı hukuk normlarını (`el-Kitâb`) indirdik.
  - `وَٱلْمِيزَانَ` (ve'l-mîzân): Ve adalet terazisini, rasyonel ve hukuki denge ölçütünü (`el-Mîzân`).
  - `لِيَقُومَ ٱلنَّاسُ بِٱلْقِسْطِ` (li-yekûme'n-nâsü bi'l-kıst): Ta ki insanlar toplumsal, iktisadi ve hukuki hayatta hakkaniyeti (`el-kıst`) bizzat kendileri ayakta tutsunlar (`lâm-ı ta‘lîl` ile bütün peygamberlerin ve kitapların gönderiliş gayesi tek bir cümlede özetlenmiştir: **Adaletin ikamesi**).
  - `وَأَنزَلْنَا ٱلْحَدِيدَ` (ve enzelne'l-hadîd): Ve demiri indirdik / yarattık (hem kozmolojik olarak süpernova nükleosenteziyle yeryüzüne indirilişine hem de nimet olarak insanlığın emrine verilişine işaret eder).
  - `فِيهِ بَأْسٌ شَدِيدٌ` (fîhi be'sün şedîd): Onda çetin bir sertlik, savunma ve caydırıcılık gücü (`be'sün şedîd`) vardır (hukuku koruyan meşru kamu gücü ve savunma kapasitesi).
  - `وَمَنَـٰفِعُ لِلنَّاسِ` (ve menâfi‘u li'n-nâs): Ve insanlar için sayısız sivil, endüstriyel ve medeni faydalar (`menâfi‘`) vardır.

- **Klasik Tefsir Lafzî Tahlili (Mâtürîdî, Râzî & İbn Teymiyye):**
  - `[NAKİL]`: Ebû Mansûr el-Mâtürîdî (*Te'vîlâtü Ehli's-Sünne*, C. 9, s. 524–526) ve Fahreddîn er-Râzî (*Mefâtîhu'l-Gayb*, C. 29, s. 242–245), âyetin medeniyetin üç kurucu sütununu bir araya getirdiğini vurgularlar: **Kitap** (vahyî ve ahlaki norm), **Mîzân** (akli ve hukuki adalet ölçüsü) ve **Hadîd / Demir** (bu adaleti dış ve iç saldırılara karşı koruyan caydırıcı icra gücü ve sivil teknoloji).[^1]
  - `[YORUM]`: Hukuktan (`Kitap` ve `Mîzân`) kopuk bir demir (`Hadîd`) zorbalık ve yıkım üretir; demirden (caydırıcı güç ve teknolojiden) yoksun bir hukuk ise mütecavizler karşısında aciz kalır. Medeniyet ancak `Kitap + Mîzân + Hadîd` dengesiyle ayakta durur.

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "18-rapor-nahl-1690-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (Nahl Sûresi 16:90 — Resm-i Osmânî):**
  > إِنَّ ٱللَّهَ يَأْمُرُ بِٱلْعَدْلِ وَٱلْإِحْسَـٰنِ وَإِيتَآئِ ذِى ٱلْقُرْبَىٰ وَيَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ وَٱلْبَغْىِ ۚ يَعِظُكُمْ لَعَلَّكُمْ تَذَكَّرُونَ ﴿٩٠﴾

- **Sahih Türkçe Meal:**
  > *"Şüphesiz Allah; adaleti, ihsanı (iyiliği, güzelliği ve erdemli fazileti) ve yakınlara (haklarını/ihtiyaçlarını) vermeyi emreder; fahşâdan (hayâsızlıktan), münkerden (aklın ve dinin çirkin gördüğü kötülüklerden) ve bağyden (haddi aşmaktan, zulüm ve zorbalıktan) ise nehyeder (yasaklar). Düşünüp öğüt alasınız diye size böyle vaaz eder. (90)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `إِنَّ ٱللَّهَ يَأْمُرُ` (İnnallâhe ye'muru): Şüphesiz Allah kesin ve sürekli bir hükümle emreder (muzâri fiil teceddüd ve süreklilik ifade eder).
  - `بِٱلْعَدْلِ` (bi'l-‘adl): Adaleti (ifrat ve tefritten uzak tam dengeyi, herkese hakkını eksiksiz vermeyi ve hukuk önünde mutlak eşitliği).
  - `وَٱلْإِحْسَـٰنِ` (ve'l-ihsân): Ve ihsanı (farz olan adaletin ötesine geçerek karşılık beklemeden iyilik yapmayı, kusuru affetmeyi ve her işi en yüksek kalite/estetik ve samimiyetle icra etmeyi).
  - `وَإِيتَآئِ ذِى ٱلْقُرْبَىٰ` (ve îtâi zi'l-kurbâ): Ve yakınlara / akrabaya ve sosyal çevredeki muhtaçlara haklarını ve desteklerini vermeyi (aile ve sosyal dayanışma ağının korunması).
  - `وَيَنْهَىٰ عَنِ ٱلْفَحْشَآءِ` (ve yenhâ ‘ani'l-fahşâi): Ve fahşâyı yasaklar (nefsin şehvet ve açgözlülük güdüsüyle işlediği sınır aşan her türlü çirkinlik ve ahlaksızlık).
  - `وَٱلْمُنكَرِ` (ve'l-münker): Ve münkeri yasaklar (selim aklın, fıtratın ve şer‘î hukukun tanımayıp reddettiği her türlü kamusal kötülük).
  - `وَٱلْبَغْىِ` (ve'l-bağy): Ve bağyi yasaklar (insanlara karşı kibirlenme, yetki aşımı, tahakküm, zulüm ve meşru düzene karşı zorbalık).
  - `يَعِظُكُمْ لَعَلَّكُمْ تَذَكَّرُونَ` (ye‘izuküm le‘alleküm tezekkerûn): Düşünüp fıtrî hakikati hatırlayasınız diye size öğüt verir.

- **Klasik Tefsir Lafzî Tahlili (İbn Mes‘ûd, Taberî & İbn Âşûr):**
  - `[NAKİL]`: Abdullah b. Mes‘ûd (r.a.) *"Kur’ân’da hayır ve şerri bu âyetten daha kapsamlı toplayan (câmi‘) başka bir âyet yoktur"* demiş; İbn Âşûr (*et-Tahrîr ve't-Tenvîr*, C. 14, s. 256–262) Ömer b. Abdülazîz’in bu âyeti cuma hutbelerinin sonuna yerleştirmesiyle İslam medeniyetinin her hafta bu **6 maddelik anayasal sözleşmeyi** (3 emir: *Adl, İhsan, Îtâi zi'l-kurbâ*; 3 yasak: *Fahşâ, Münker, Bağy*) yenilediğini kaydetmiştir.[^1]
  - `[YORUM]`: Salt hukuk (`Adl`) toplumu ayakta tutar ama soğuk bürokrasiye dönüşebilir; `İhsan` ve `Sosyal Dayanışma` hukuku merhametle ısıtır. Karşısındaki 3 yasak ise bireysel yozlaşmayı (`Fahşâ`), kamusal suçu (`Münker`) ve siyasal/kurumsal zorbalığı (`Bağy`) aynı anda engeller.

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "19-rapor-hucurat-4913-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (Hucurât Sûresi 49:13 — Resm-i Osmânî):**
  > يَـٰٓأَيُّهَا ٱلنَّاسُ إِنَّا خَلَقْنَـٰكُم مِّن ذَكَرٍ وَأُنثَىٰ وَجَعَلْنَـٰكُمْ شُعُوبًا وَقَبَآئِلَ لِتَعَارَفُوٓا۟ ۚ إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ ۚ إِنَّ ٱللَّهَ عَلِيمٌ خَبِيرٌ ﴿١٣﴾

- **Sahih Türkçe Meal:**
  > *"Ey insanlar! Şüphesiz Biz sizi bir erkekle bir dişiden yarattık ve birbirinizle tanışıp bilişesiniz (teârüf edesiniz) diye sizi milletlere (şuûb) ve kabilelere ayırdık. Şüphesiz Allah katında en üstününüz (en değerli olanınız), O’na karşı sorumluluk bilinci en yüksek olanınızdır (en muttakî olanınızdır). Şüphesiz Allah her şeyi hakkıyla bilendir, her şeyden haberdar olandır. (13)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `يَـٰٓأَيُّهَا ٱلنَّاسُ` (Yâ eyyühe'n-nâs): Ey insanlar! (Sûrenin önceki âyetlerinde `Yâ eyyühellezîne âmenû` hitabı kullanılırken, bu âyette hitap doğrudan bütün insanlık ailesine genişletilmiştir).
  - `إِنَّا خَلَقْنَـٰكُم مِّن ذَكَرٍ وَأُنثَىٰ` (innâ halaknâküm min zekerin ve ünsâ): Şüphesiz Biz sizi tek bir erkek (Hz. Âdem) ve tek bir dişiden (Hz. Havvâ) —veya her birinizi anne ve baba birliğinden— yarattık (bütün insanların ontolojik ve biyolojik eşitliği).
  - `وَجَعَلْنَـٰكُمْ شُعُوبًا وَقَبَآئِلَ` (ve ce‘alnâküm şu‘ûben ve kabâile): Ve sizi büyük milletlere/halklara (`şu‘ûb`) ve boylara/kabilelere (`kabâil`) ayırdık.
  - `لِتَعَارَفُوٓا۟` (li-te‘ârafû): Birbirinizle tanışasınız, yardımlaşasınız ve karşılıklı kültür/bilgi alışverişinde bulunasınız diye! (`tefâ‘ul` bâbından işteş fiil; üstünlük taslamak `li-tefâharû` veya çatışmak `li-tenâkerû` için değil, karşılıklı tanışma `teârüf` içindir).
  - `إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ` (inne ekrameküm ‘indallâhi etkâküm): Şüphesiz Allah katında en kerîm, en şerefli ve en üstün olanınız, takvâca (ahlaki sorumluluk ve adalet bilincince) en ileri olanınızdır.
  - `إِنَّ ٱللَّهَ عَلِيمٌ خَبِيرٌ` (innallâhe ‘alîmün habîr): Şüphesiz Allah (niyetleri ve amelleri) hakkıyla bilendir, (kalplerin iç yüzünden) haberdar olandır.

- **Klasik Tefsir Lafzî Tahlili (Taberî, Zemahşerî & İbn Âşûr):**
  - `[NAKİL]`: İbn Âşûr (*et-Tahrîr ve't-Tenvîr*, C. 26, s. 258–264), `li-te‘ârafû` kelimesindeki `lâm-ı ta‘lîl`in sosyolojik çeşitliliğin tek meşru gayesini **"karşılıklı tanışma ve medeni işbirliği"** olarak belirlediğini; `inne ekrameküm ‘indallâhi etkâküm` cümlesinin ise cahiliyenin soy, kan, ırk ve kabile üstünlüğü (`neseb/asabiyet`) iddiasını kökünden yıkarak değer ölçütünü iradî ve ahlaki liyakate (`takvâ`) bağladığını vurgular.[^1]
  - `[YORUM]`: Lafzî yapı üç aşamalı bir insanlık beyannamesidir: (1) Yaratılışta mutlak eşitlik (`min zekerin ve ünsâ`), (2) Sosyolojik çeşitlilikte çatışma değil tanışma etiği (`li-te‘ârafû`), (3) Üstünlükte ırk/soy değil yalnızca ahlaki sorumluluk ve adalet (`etkâküm`).

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",

    "20-rapor-maide-532-v6.1.1.md": """### ADIM 01 — LAFZÎ TAHLİL, SİYÂK-SİBÂK VE TARİHSEL BAĞLAM

- **Arapça Metin (Mâide Sûresi 5:32 — Resm-i Osmânî):**
  > مِنْ أَجْلِ ذَٰلِكَ كَتَبْنَا عَلَىٰ بَنِىٓ إِسْرَٰٓءِيلَ أَنَّهُۥ مَن قَتَلَ نَفْسًۢا بِغَيْرِ نَفْسٍ أَوْ فَسَادٍ فِى ٱلْأَرْضِ فَكَأَنَّمَا قَتَلَ ٱلنَّاسَ جَمِيعًا وَمَنْ أَحْيَاهَا فَكَأَنَّمَآ أَحْيَا ٱلنَّاسَ جَمِيعًا ۚ وَلَقَدْ جَآءَتْهُمْ رُسُلُنَا بِٱلْبَيِّنَـٰتِ ثُمَّ إِنَّ كَثِيرًا مِّنْهُم بَعْدَ ذَٰلِكَ فِى ٱلْأَرْضِ لَمُسْرِفُونَ ﴿٣٢﴾

- **Sahih Türkçe Meal:**
  > *"İşte bu yüzdendir ki (Kâbil’in Hâbil’i haksız yere öldürmesi sebebiyle) İsrâiloğullarına şöyle yazdık (hüküm olarak farz kıldık): Kim, bir cana karşılık (kısas) olmaksızın veya yeryüzünde bir fesat (terör/eşkıyalık) çıkarmaya karşılık olmaksızın bir insanı öldürürse, sanki bütün insanları öldürmüş gibidir! Kim de bir insanın hayatını kurtarırsa (ihyâ ederse), sanki bütün insanların hayatını kurtarmış gibidir! Andolsun ki elçilerimiz onlara apaçık delillerle (beyyinelerle) gelmiştir; fakat bundan sonra da onlardan birçoğu yeryüzünde (kan dökerek) haddi aşmaktadırlar. (32)"*

- **Kelime-Kelime Lafzî Çözümleme (Kelime Mealleri):**
  - `مِنْ أَجْلِ ذَٰلِكَ` (Min ecli zâlike): İşte bu cinayet (Âdem’in iki oğlunun kıssasındaki ilk haksız kan dökme suçu) sebebiyledir ki.
  - `كَتَبْنَا عَلَىٰ بَنِىٓ إِسْرَٰٓءِيلَ` (ketebnâ ‘alâ benî isrâîle): İsrâiloğulları üzerine (ve tüm semavî şeriatlarda geçerli evrensel bir hüküm olarak) yazdık / farz kıldık.
  - `أَنَّهُۥ مَن قَتَلَ نَفْسًۢا` (ennehû men katele nefsen): Kim bir canı (`nefsen` nekre olarak gelerek din, ırk, statü farkı gözetmeksizin her masum insan canını kapsar) öldürürse.
  - `بِغَيْرِ نَفْسٍ أَوْ فَسَادٍ فِى ٱلْأَرْضِ` (bi-ğayri nefsin ev fesâdin fi'l-ard): Bir cana karşılık (mahkeme kararıyla infaz edilen adil kısas) veya yeryüzünde silahlı terör/eşkıyalık (`fesâd fi'l-ard`) suçu dışında haksız yere.
  - `فَكَأَنَّمَا قَتَلَ ٱلنَّاسَ جَمِيعًا` (fe-keennemâ katele'n-nâse cemî‘â): Sanki bütün insanlığı topyekûn öldürmüş gibidir! (`keennemâ` teşbih-i belîğ ve tazim edatı; `cemî‘â` tekit haliyle tek bir masumun yaşam hakkını tüm insanlığın yaşam hakkına eşitler).
  - `وَمَنْ أَحْيَاهَا` (ve men ahyâhâ): Ve kim de o canı yaşatırsa / ölümden kurtarırsa (affederek, boğulmaktan/yangından/açlıktan kurtararak, tıbbi tedavi veya insani yardımla hayata döndürerek).
  - `فَكَأَنَّمَآ أَحْيَا ٱلنَّاسَ جَمِيعًا` (fe-keennemâ ahye'n-nâse cemî‘â): Sanki bütün insanlığı diriltmiş / yaşatmış gibidir!
  - `فِى ٱلْأَرْضِ لَمُسْرِفُونَ` (fi'l-ardı le-müsrifûn): Yeryüzünde (kan dökme ve hak çiğneme konusunda) haddi aşan müsriflerdir.

- **Klasik Tefsir Lafzî Tahlili (Taberî, Râzî & Kurtubî):**
  - `[NAKİL]`: Fahreddîn er-Râzî (*Mefâtîhu'l-Gayb*, C. 11, s. 210–213) ve Kurtubî (*el-Câmi‘*, C. 6, s. 146–149), `fe-keennemâ katele'n-nâse cemî‘â` ifadesinin lafzî ve hukuki sırrını şöyle açıklarlar: Tek bir masum insanı haksız yere öldüren kimse, "insan hayatının dokunulmazlığı" (*hurmetü'd-dem*) ilkesini yıkmıştır; bu ilke yıkıldığında ise hiçbir insanın can güvenliği kalmaz. Tersine bir canı kurtaran (`ahyâhâ`) ise bütün insanlığın yaşam onurunu ihya etmiştir.[^1]
  - `[YORUM]`: Âyet, insan hayatını aritmetik çoğunluk hesabına kurban eden faydacı (*utilitarian*) anlayışı reddederek `1 Masum Can = Bütün İnsanlık` ontolojik denklemini kurar.

- **Siyâk-Sibâk ve Tarihsel Bağlam:**""",
}


def main():
    for fname, new_header in LAFZI_BLOCKS.items():
        p = DOCS_TR / fname
        txt = p.read_text(encoding="utf-8")
        target = "### ADIM 01 — SİYÂK-SİBÂK VE TARİHSEL BAĞLAM"
        if target in txt:
            txt = txt.replace(target, new_header, 1)
            p.write_text(txt, encoding="utf-8")
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
            print(f"Enriched ADIM 01 in {fname} (SHA256: {h[:12]})")
        else:
            print(f"Target not found or already enriched in {fname}")


if __name__ == "__main__":
    main()
