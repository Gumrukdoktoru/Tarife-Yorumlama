from yardim_44_47 import q, yaz, T_E, T_O, T_F, T_N, T_G, T_B, T_C, T_S

sorular = [
    # 1
    q("Tarife Cetveline göre, tomruğun kendi ekseni etrafında döndürülerek soyulmasıyla elde edilen, kontrplak imalatında kullanılacak, kalınlığı 4 mm olan ağaç yaprakları hangi pozisyonda sınıflandırılır?",
      "44.08", ["44.07", "44.12", "44.09", "44.04"], "C", T_E,
      "44.08, uzunlamasına biçilmiş, dilimlenmiş veya yaprak halinde açılmış, kalınlığı 6 mm’yi geçmeyen kaplama ve kontrplak yapraklarını kapsar. Kalınlık 6 mm’yi geçseydi 44.07’ye girerdi. Yaprakların yapıştırılmasıyla elde edilen kontrplağın kendisi 44.12’de, devamlı şekil verilmiş ağaç 44.09’da, örgü ve çip kutusu yapımına mahsus dar kasnak tahtaları 44.04’tedir.",
      "44.08 pozisyon metni ve Açıklama Notu; 44.07 Açıklama Notu (hariç tutmalar)."),
    # 2
    q("Bir kenarı boyunca lambalanmış, karşı kenarına yiv açılmış, henüz birbirine birleştirilmemiş meşe parke şeritleri Tarife Cetvelinde hangi pozisyonda yer alır?",
      "44.09", ["44.07", "44.18", "44.12", "44.21"], "A", T_E,
      "44.09 metni, devamlı şekil verilmiş (lambalanmış, yiv açılmış vb.) ağaçları ve birleştirilmemiş parke tahtaları için şeritleri açıkça kapsar. Yalnız planyalanmış, zımparalanmış veya uç uca eklenmiş şeritler 44.07’de kalır. Panel halinde birleştirilmiş parke 44.18’e, parke taklidi ince kaplamalı kontrplak paneller 44.12’ye gider.",
      "44.09 pozisyon metni ve Açıklama Notu; 44.18 ve 44.12 Açıklama Notları."),
    # 3
    q("Aşağıdakilerden hangisi Tarife Cetvelinin 44. faslında <b>sınıflandırılmaz</b>?",
      "Aktif hale getirilmiş odun kömürü",
      ["Hindistan cevizi kabuğunun karbonlaştırılmasıyla elde edilen kömür",
       "Bambu katlarından yapılmış kontrplak",
       "Kreozotla emprenye edilmiş ağaçtan elektrik direği",
       "Testere talaşının sıkıştırılmasıyla elde edilen odun pelletleri"], "E", T_O,
      "Fasıl 44 Not 1 aktif hale getirilmiş kömürü fasıl dışında bırakır; bunlar 38.02’dedir. Meyve kabuğu kömürü 44.02’de açıkça sayılmıştır, bambu kontrplak Not 6 gereği 44.12’dedir. Kreozotla emprenye koruyucu işlem olduğundan direği 44.03’ten çıkarmaz; aglomere talaş (pellet) 44.01’dedir.",
      "Fasıl 44 Not 1 ve Not 6; 44.01, 44.02, 44.03 Açıklama Notları."),
    # 4
    q("Fasıl 44 notlarına göre “yoğunlaştırılmış ahşap” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Kimyasal veya fiziksel işlemle yoğunluğu ve sertliği önemli derecede artmış masif veya yapıştırılmış levhalardan oluşan ağaçtır.",
      ["Yalnızca birbirine yapıştırılmış ince kaplama tabakalarından oluşan ağaçları ifade eder.",
       "Tabakaların birbirine yapıştırılması işlemi tek başına ağaca bu vasfı kazandırır.",
       "Reçine ile aglomere edilmiş ağaç yongalarından preslenmiş levhalardır.",
       "Yoğunluğu 0,8 gr/cm3’ü geçen her türlü lif levhayı ifade eder."], "B", T_N,
      "Not 2’ye göre yoğunlaştırılmış ahşap, kimyasal veya fiziksel işlem görmüş ve bu suretle yoğunluğu ve sertliği önemli derecede artmış, mekanik dayanıklılık veya kimyasal ya da elektrik etkilerine direnç kazanmış masif veya yapıştırılmış levhalardan oluşan ağaçtır. Tabakalı olanlarda yapıştırmadan daha ileri bir işlem gerekir; yani yalnız yapıştırma yetmez. Yongalı levha 44.10’un, yoğun lif levha 44.11’in konusudur.",
      "Fasıl 44 Not 2; 44.13 Açıklama Notu."),
    # 5
    q("Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
      "Ahşap ütü tahtası",
      ["Ahşap pencere çerçevesi", "Ahşap kapı eşiği",
       "Beton dökümünde kullanılan ahşap kalıp", "Ahşap padavra"], "D", T_F,
      "Pencere çerçevesi, kapı eşiği, beton inşaat kalıbı ve padavra bina ve inşaat için marangozluk ve doğrama mamulü olarak 44.18’dedir. Ütü tahtaları ise 44.21 Açıklama Notunda “ahşap diğer eşya” arasında sayılmıştır. Tuzak, beton kalıbını alet veya diğer eşya sanmaktır.",
      "44.18 ve 44.21 Açıklama Notları."),
    # 6
    q("Ahşaptan yapılmış, taşıyıcılarla ayrılmış iki yükleme yüzeyi bulunan, fork-lift ile taşınmaya uygun yük tablası (palet) hangi pozisyonda sınıflandırılır?",
      "44.15", ["44.21", "86.09", "44.18", "94.03"], "A", T_E,
      "44.15 metni ahşap paletleri, palet sandıklarını ve diğer yük tablalarını açıkça sayar; Açıklama Notu paleti fork-lift veya palet kaldırıcılarla taşımaya göre yapılmış yükleme tablası olarak tanımlar. 86.09 bir veya daha fazla taşıta göre özel yapılmış konteynerler içindir. 44.21 kalıntı pozisyondur ve özel pozisyonu bulunan eşyaya uygulanmaz.",
      "44.15 pozisyon metni ve Açıklama Notu (III)."),
    # 7
    q("Fasıl 44 Not 4’e göre 44.10, 44.11 veya 44.12 pozisyonlarındaki levhalarla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Başka pozisyonlardaki eşya vasfını kazanmadıkça eğilmiş, ondüle edilmiş veya perfore edilmiş olabilirler.",
      ["Kare veya dikdörtgen dışında bir şekilde kesildiklerinde 44.21 pozisyonuna geçerler.",
       "Perfore edilmeleri halinde bu pozisyonlarda kalamazlar.",
       "Yalnızca 44.09’daki şekillerde işlenmiş olanlar bu pozisyonlarda kalır; başka işlem görenler hariçtir.",
       "Yüzeyleri kağıt veya plastikle kaplandığında Fasıl 39 veya 48’e geçerler."], "C", T_N,
      "Not 4’e göre bu levhalar 44.09’daki şekillerde işlenmiş, eğilmiş, ondüle edilmiş, perfore edilmiş, kare veya dikdörtgenden başka şekilde kesilmiş ya da başka bir işleme tabi tutulmuş olabilir; yeter ki diğer pozisyonlardaki eşya vasfını kazanmasın. Açıklama Notları kağıt, plastik, mensucat veya metalle kaplanmış olanları da bu pozisyonlarda bırakır. Diğer seçenekler notun tersini söylemektedir.",
      "Fasıl 44 Not 4; 44.10, 44.11 ve 44.12 Açıklama Notları."),
    # 8
    q("Aşağıdakilerden hangisi 44.17 pozisyonunda <b>yer almaz</b>?",
      "Ahşap şapka kalıbı",
      ["Ahşap ayakkabı kalıbı", "Tornalanmış ahşap kazma sapı",
       "Tamamı ahşap bahçe tırmığı", "Ahşap fırça gövdesi"], "E", T_O,
      "44.17 ahşap aletleri, alet sapları, süpürge ve fırça gövde ve saplarını, bot ve ayakkabı kalıplarını kapsar. Açıklama Notu şapka kalıplarını açıkça hariç tutar ve 84.49’a gönderir. Tuzak, ayakkabı kalıbıyla şapka kalıbını aynı pozisyonda sanmaktır.",
      "44.17 pozisyon metni ve Açıklama Notu (hariç tutmalar)."),
    # 9
    q("Montaj için zıvana ve kırlangıç kuyruğu yerleri hazırlanmış, menteşe ve kilidiyle birlikte monte edilmemiş halde getirilen ahşap kapının, bitmiş kapı gibi 44.18 pozisyonunda sınıflandırılmasını sağlayan Genel Yorum Kuralı hangisidir?",
      "GYK 2(a)", ["GYK 3(a)", "GYK 3(b)", "GYK 5(b)", "GYK 4"], "D", T_G,
      "GYK 2(a), bir eşyaya yapılan atfın o eşyanın sökülerek veya monte edilmeden getirilmiş olanlarını da kapsadığını hükme bağlar. Fasıl 44 Genel Açıklamaları da tamamlanmamış veya demonte ahşap eşyayı, parçaları bir arada olmak şartıyla bitmiş eşya gibi sınıflandırır; 44.18 Açıklama Notu monte edilmemiş doğramanın tanınabilir olmasını ister. 3(a), 3(b) ve 4 burada gerekmez; 5(b) ambalajlarla ilgilidir.",
      "GYK 2(a); Fasıl 44 Genel Açıklamalar; 44.18 Açıklama Notu."),
    # 10
    q("Aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
      "Hücreli ahşap panel – 44.12",
      ["Ağaç unu – 44.05", "Ahşap kablo makarası – 44.15",
       "Ahşap fıçı tahtası – 44.16", "Ahşap küçük heykelcik – 44.20"], "B", T_B,
      "Hücreli ahşap levhalar 44.18 pozisyon metninde açıkça sayılmıştır; 44.12 Açıklama Notu da bunları hariç tutar. Ağaç unu 44.05’te, kablo makaraları 44.15’te, fıçı tahtaları 44.16’da, heykelcikler 44.20’dedir. Göbekli kontrplağa benzemesi hücreli paneli 44.12 sanmanın nedenidir.",
      "44.18 pozisyon metni; 44.12 Açıklama Notu (hariç tutmalar)."),
    # 11
    q("Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur? I. Koruma amacıyla kreozotla emprenye edilmiş yuvarlak tomruk 44.03’te kalır. II. Kalınlığı 8 mm olan, uzunlamasına biçilmiş çam tahtası 44.08’de yer alır. III. Yakacak olarak kullanılmaktan başka işe yaramayan eski ambalaj sandıkları 44.01’de yer alır. IV. Reçine ile kaplanarak çıra haline getirilmiş odun 44.01’de yer alır.",
      "I ve III", ["I ve II", "II ve IV", "I, III ve IV", "II, III ve IV"], "B", T_C,
      "Kreozotla emprenye gibi koruyucu işlemler ağacın sınıflandırmasını etkilemez (I doğru). 6 mm’yi geçen biçilmiş ağaç 44.07’dedir (II yanlış). Kullanılamayan eski ambalaj sandıkları odun artığı olarak 44.01’e girer (III doğru). Reçine ile çıra haline getirilmiş odun 44.01’den hariç tutulup 36.06’ya gönderilmiştir (IV yanlış).",
      "Fasıl 44 Genel Açıklamalar; 44.01, 44.07 ve 44.15 Açıklama Notları."),
    # 12
    q("Bir firma, kayından elde edilen çok ince kaplama levhalarını ısı ile sertleşen reçinelerle emprenye edip yüksek sıcaklık ve basınç altında sıkıştırmakta; yoğunluğu ve sertliği önemli ölçüde artmış, makine yatakları ve dişlileri imalinde kullanılacak bloklar üretmektedir. Bu bloklar hangi pozisyonda sınıflandırılır?",
      "44.13", ["44.12", "44.10", "39.21", "44.11"], "E", T_S,
      "Emprenyeleme ve yoğunluğu artırma işlemlerinin birlikte uygulandığı, yoğunluğu ve sertliği artmış ağaç 44.13 kapsamındadır; Açıklama Notu kullanım yerleri arasında yatak ve diğer makine kısımlarını sayar. 44.12 Açıklama Notu lamine edilmiş yoğunlaştırılmış ağaç levhaları açıkça hariç tutar. Reçine kullanılması eşyayı plastik levha (39.21) yapmaz; yonga ve lif levhalar ise ayrı pozisyonlardadır.",
      "Fasıl 44 Not 2; 44.13 ve 44.12 Açıklama Notları."),
    # 13
    q("Kenarları kabaca düzleştirilmiş, ray vidaları için delikleri açılmış, uzun süreli koruma için kreozotla emprenye edilmiş, planyalanmamış ağaçtan köprü traversi hangi pozisyonda yer alır?",
      "44.06", ["44.03", "44.07", "44.18", "86.08"], "A", T_E,
      "44.06 Açıklama Notu demiryolu traverslerinden daha geniş ve kalın olan köprü traverslerini de kapsar; delik açılması ve kreozotla emprenye bu pozisyonu bozmaz. Travers şeklinde kesilmiş ağaç 44.03 Açıklama Notunda hariç tutularak 44.06’ya gönderilmiştir. Biçilmiş ağaç (44.07) ve doğrama (44.18) seçenekleri traversin özel pozisyonu karşısında geçersizdir.",
      "44.06 pozisyon metni ve Açıklama Notu; 44.03 Açıklama Notu (hariç tutmalar)."),
    # 14
    q("Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Ahşap tüfek dipçiği",
      ["Ahşap yemek kaşığı", "Ahşap tabut", "Ahşap resim çerçevesi", "Ahşap şarap fıçısı"], "C", T_F,
      "Fasıl 44 Not 1 ateşli silahların aksam ve parçalarını fasıl dışında bırakır; ahşap tüfek dipçiği 93.05’tedir (44.21 Açıklama Notu da aynı hariç tutmayı yapar). Kaşık 44.19’da, tabut 44.21’de, resim çerçevesi 44.14’te, fıçı 44.16’dadır; hepsi Fasıl 44 içindedir.",
      "Fasıl 44 Not 1; 44.21 Açıklama Notu."),
    # 15
    q("44.10 pozisyonu Açıklama Notuna göre yonga levhalar genellikle levha ağırlığının en fazla yüzde kaçını aşmayan oranda organik bağlayıcı ilavesiyle aglomere edilir?",
      "%15", ["%3", "%5", "%10", "%25"], "D", T_N,
      "44.10 Açıklama Notuna göre yonga levhalar genellikle levha ağırlığının %15’ini aşmayan oranda organik bağlayıcı (çoğunlukla ısı ile sertleşen sentetik reçine) ilavesiyle aglomere edilir. %3 oranı odun pelleti ve briketi için bağlayıcı sınırıdır; karıştırılmamalıdır. Çimento veya alçı gibi mineral bağlayıcılı levhalar ise 68.08’e gider.",
      "44.10 Açıklama Notu; Fasıl 44 Alt pozisyon Notları (odun pelleti, briket)."),
    # 16
    q("Aşağıdakilerden hangisi 44.21 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Ahşaptan oyuncak tren",
      ["Ahşap tabut", "Ahşap arı kovanı",
       "Uçlarına yanıcı madde sürülmemiş ahşap kibrit çöpü", "Ahşap kürdan"], "E", T_O,
      "Oyuncaklar, oyun ve spor malzemeleri Fasıl 44 Not 1 ve 44.21 Açıklama Notu gereği Fasıl 95’tedir. Tabut, arı kovanı, kürdan ve uçlarına yanıcı madde sürülmemiş kibrit çöpleri 44.21 Açıklama Notunda açıkça sayılmıştır. Kibrit çöpünün ucuna yanıcı madde sürülmüş olsaydı Fasıl 44 dışında kalırdı.",
      "Fasıl 44 Not 1; 44.21 Açıklama Notu."),
    # 17
    q("“Kontrplak, kontrplak imaline mahsus üç veya daha fazla ahşap tabakanın damar yönleri birbirine ……… gelecek şekilde üst üste konularak basınç altında tutkalla yapıştırılmasıyla elde edilir; ortadaki kata ……… adı verilir.” Cümlesindeki boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
      "çapraz – göbek", ["paralel – göbek", "çapraz – kaplama", "paralel – flanş", "dik açıyla – kasnak"], "A", T_B,
      "44.12 Açıklama Notuna göre kontrplakta katların damar yönleri birbirine çapraz gelecek şekilde tertiplenir; bu, direnci artırır ve eğriliği azaltır. Her yaprağa “kat”, ortadaki kata “göbek” denir ve kat adedi genellikle tek rakamlıdır. Damarları paralel yapıştırılan levhalar glulam gibi 44.18 ürünlerinin özelliğidir; flanş I kirişlerin, kasnak ise 44.04 şeritlerinin terimidir.",
      "44.12 Açıklama Notu (1)."),
    # 18
    q("Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
      "Ahşap ekmek tahtası",
      ["Ahşap mücevher kutusu", "Ahşaptan hayvan figürü (biblo)",
       "Cepte taşınan ahşap enfiye kutusu", "Üzerine kakma yapılmış ahşap levha"], "D", T_F,
      "Ekmek tablaları ve kıyma tahtaları sofra ve mutfak eşyası olarak 44.19’dadır. Mücevher kutuları, enfiye kutusu gibi küçük kutular, heykelcik ve süs eşyası ile kakma ağaç 44.20’de yer alır. 44.20 Açıklama Notu mutfaklarda kullanılan sıradan baharat kutularını da 44.19’a gönderir.",
      "44.19 ve 44.20 Açıklama Notları."),
    # 19
    q("Yuvarlak bir ağaç gövdesinin yüzeyleri balta ile düzleştirilerek enine kesiti kabaca kare hale getirilmiştir; yüzeylerde kabuk kalıntıları görülmektedir ve malzeme kereste fabrikasına gönderilecektir. Bu ağaç malzeme hangi pozisyonda sınıflandırılır?",
      "44.03", ["44.07", "44.01", "44.04", "44.06"], "C", T_S,
      "44.03 metni kabaca kare şeklinde yontulmuş yuvarlak ağaçları kapsar; Açıklama Notuna göre bu malzeme işlenmemiş olması veya kabuk kalıntılarıyla tanınır ve kereste fabrikaları için bu şekilde hazırlanır. 44.07 Açıklama Notu kabaca kare şeklinde olanları hariç tutarak 44.03’e gönderir. 44.04 yalnız kazık, sırık, çember ve baston-sap çubukları içindir.",
      "44.03 pozisyon metni ve Açıklama Notu; 44.07 Açıklama Notu (hariç tutmalar)."),
    # 20
    q("Seramik sofra takımlarıyla birlikte sunulan, bu eşyanın ambalajında normal olarak kullanılan ve sürekli kullanıma elverişli olmadığı açıkça belli olan ahşap kafes sandık nasıl sınıflandırılır?",
      "İçindeki eşya ile birlikte, GYK 5(b) uyarınca",
      ["Ayrı olarak 44.15 pozisyonunda, GYK 1 uyarınca",
       "İçindeki eşya ile birlikte, GYK 5(a) uyarınca",
       "Ayrı olarak 44.15 pozisyonunda, GYK 5(b) uyarınca",
       "Esas niteliği veren eşyaya göre, GYK 3(b) uyarınca"], "B", T_G,
      "GYK 5(b)’ye göre içindeki eşya ile birlikte sunulan ve o eşyanın ambalajında normal olarak kullanılan ambalaj mahfazaları eşya ile birlikte sınıflandırılır; sürekli kullanıma elverişli olduğu açıkça belli olanlar bu hükmün dışındadır. 5(a) belli bir eşyaya göre şekil verilmiş, uzun süre kullanılabilir mahfazalar içindir. Sandık ayrı sunulsaydı 44.15’e girerdi.",
      "GYK 5(b); 44.15 Açıklama Notu."),
    # 21
    q("Fasıl 44 notlarına göre aşağıdakilerden hangisi <b>yanlıştır</b>?",
      "96.03 pozisyonuna giren eşyaların ahşap gövde ve sapları Fasıl 96’da sınıflandırılır.",
      ["Not 1 saklı kalmak kaydıyla, fasılda “ağaç”a yapılan atıf bambuları ve odunsu yapıdaki diğer maddeleri de kapsar.",
       "44.14 ila 44.21 pozisyonları lif levha veya yonga levhadan yapılmış eşyaya da uygulanır.",
       "İş gören kısmı Fasıl 82 Not 1’de sayılan bir maddeden yapılmış aletler 44.17’ye dahil değildir.",
       "İşlenmemiş haldeki bambular bu fasla dahil değildir."], "D", T_N,
      "Not 1, Fasıl 96 eşyasını hariç tutarken 96.03’e giren eşyaların (süpürge ve fırçalar) ahşap gövde ve saplarını bu hariç tutmanın dışında bırakır; bunlar 44.17’dedir. Diğer ifadeler sırasıyla Not 6, Not 3, Not 5 ve Not 1’in doğru özetleridir. Tuzak, bitmiş fırçanın 96.03’e gittiğini bilip gövdesini de oraya göndermektir.",
      "Fasıl 44 Not 1, 3, 5 ve 6; 44.17 pozisyon metni."),
    # 22
    q("Aşağıdakilerden hangileri 44.12 pozisyonunda yer alır? I. Orta tabakası yonga levha olan, iki yüzü ahşap kaplamalık yaprakla kaplanmış levha II. Parke döşemesini taklit eden ince ahşap kaplamalı kontrplak döşeme paneli III. Damarları paralel tabakaların tutkalla birleştirilmesiyle yapılmış lamine kiriş (glulam) IV. Lamine edilmiş ağaç bloklarının dilimlenmesiyle elde edilen ince kaplama yaprağı",
      "I ve II", ["I ve III", "II ve IV", "I, II ve III", "II, III ve IV"], "A", T_C,
      "Orta tabakası yonga levha gibi başka maddeden olan kaplamalı levhalar ve parke taklidi ince kaplamalı döşeme panelleri 44.12 Açıklama Notunda açıkça sayılmıştır (I, II). Glulam gibi masif lamine kiriş ve kemerler 44.18’e (III), lamine ağaçların dilimlenmesiyle elde edilen kaplama yaprakları 44.08’e gider (IV).",
      "44.12 Açıklama Notu; 44.10 Açıklama Notu (hariç tutmalar); 44.08 pozisyon metni."),
    # 23
    q("Aşağıdakilerden hangisi 44.01 pozisyonunda <b>yer almaz</b>?",
      "Kağıt hamuru üretiminde kullanılacak yuvarlak kağıtlık odun",
      ["Kütük halinde yakacak odun", "Testere talaşından sıkıştırılmış briket",
       "Yapım ve yıkım döküntülerinden ayrılan, kereste olarak kullanılmayan odun artıkları",
       "Selüloz hamuru üretiminde kullanılacak yongalar halindeki odun"], "E", T_O,
      "44.01 Açıklama Notu yuvarlak veya yarılmış haldeki kağıtlık odunu hariç tutar ve 44.03’e gönderir. Yakacak odun, aglomere talaş (briket), kereste olarak kullanılmayan yapım-yıkım odun artıkları ve selüloz hamuru için yongalar 44.01 kapsamındadır. Yonga ile kağıtlık tomruğun ayrımı sık sorulan bir tuzaktır.",
      "44.01 Açıklama Notu (B), (D) ve hariç tutmalar."),
    # 24
    q("Testere talaşı, rende talaşı ve diğer odun artıklarının öğütülmesiyle elde edilen, plastik sanayiinde dolgu maddesi olarak kullanılan, parçacıkları küçük ve düzgün toz hangi pozisyonda sınıflandırılır?",
      "44.05", ["44.01", "14.04", "44.10", "12.11"], "C", T_E,
      "Ağaç unu 44.05’tedir; Açıklama Notu onu 44.01’deki testere talaşından parçacıklarının daha küçük ve muntazam olmasıyla ayırır. Hindistan cevizi kabuğundan elde edilen benzeri un 14.04’e gider. 12.11 yalnız parfümeri, eczacılık veya böcek-mantar öldürme amaçlı toz ağaç içindir.",
      "44.05 Açıklama Notu; Fasıl 44 Not 1."),
    # 25
    q("Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda yer alır?",
      "Ahşap kablo makarası – Ahşap palet",
      ["Ahşap bina kapısı – Ahşap el merdiveni",
       "Ahşap resim çerçevesi – Çerçeveli cam ayna",
       "Kontrplak – Hücreli ahşap panel",
       "Ağaç yünü – Testere talaşı"], "B", T_F,
      "Kablo makaraları ve paletler 44.15 metninde birlikte sayılmıştır. Kapı 44.18’de, el merdiveni 44.21’de; resim çerçevesi 44.14’te, çerçeveli cam ayna 70.09’da; kontrplak 44.12’de, hücreli panel 44.18’de; ağaç yünü 44.05’te, testere talaşı 44.01’dedir.",
      "44.15 pozisyon metni; 44.14, 44.18 ve 44.21 Açıklama Notları."),
]

obj = {
    "tur": "fasil",
    "fasil": 44,
    "baslik": "Ağaç ve ahşap eşya; odun kömürü",
    "bolum": "IX",
    "oz": {
        "vurgu": "Fasıl 44 ağacı işlenme derecesine göre basamak basamak sıralar: ham ağaç ve yakacak (44.01–44.06), biçilmiş veya şekil verilmiş ağaç (44.07–44.09), levhalar (44.10–44.13) ve mamul ahşap eşya (44.14–44.21). Eşya ahşap olsa bile Not 1’de sayılan bir fasla (mobilya 94, oyuncak 95, sepetçi eşyası 46, şemsiye-baston 66, alet 82, müzik aleti 92 vb.) aitse burada sınıflandırılmaz.",
        "maddeler": [
            "“Ağaç”a yapılan her atıf bambuyu ve odunsu yapıdaki diğer maddeleri de kapsar (Not 6); ancak işlenmemiş bambu 14.01’e, bambu sepet Fasıl 46’ya, bambu mobilya Fasıl 94’e gider.",
            "44.14–44.21’deki eşya masif ağaçtan olduğu kadar yonga levha, lif levha, lamine (kaplama) veya yoğunlaştırılmış ağaçtan da yapılabilir (Not 3).",
            "Kurutma, boyama, vernikleme, kreozotla emprenye gibi koruyucu işlemler ağacın pozisyonunu değiştirmez; 44.10–44.12 levhaları başka eşya vasfı kazanmadıkça kesilip şekillendirilse de yerinde kalır (Not 4).",
            "Tamamlanmamış veya demonte ahşap eşya, parçaları bir arada ise bitmiş eşya gibi sınıflandırılır; birlikte satılan cam, mermer, metal aksesuarlar da onunla birlikte sınıflandırılır."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Not 1’deki bir fasla ait eşya mı? (mobilya, prefabrik yapı, oyuncak, müzik aleti, saat kutusu, şemsiye-baston, sepetçi eşyası, ayakkabı, makine aksamı, 42.02 mahfazası, silah aksamı)", "Fasıl 94 / 95 / 92 / 91 / 66 / 46 / 64 / XVI–XVII / <b>42.02</b> / <b>93.05</b>"],
            ["2", "Parfümeri, eczacılık, böcek-mantar öldürme ya da boyacılık-debagat amaçlı dilim veya toz ağaç mı? Aktif kömür mü?", "<b>12.11</b> / <b>14.04</b> / <b>38.02</b>"],
            ["3", "Yakacak odun, yonga, talaş, odun artığı (pellet, briket dahil) mı?", "<b>44.01</b>"],
            ["4", "Odun kömürü mü? (meyve kabuğu kömürü dahil)", "<b>44.02</b>"],
            ["5", "Yuvarlak, kabuğu soyulmuş veya kabaca kare yontulmuş gövde mi?", "<b>44.03</b> (sivri kazık, sırık, çember, kaba sap çubuğu <b>44.04</b>; travers <b>44.06</b>)"],
            ["6", "Ağaç yünü veya ağaç unu mu?", "<b>44.05</b>"],
            ["7", "Uzunlamasına biçilmiş, dilimlenmiş veya yaprak halinde açılmış mı?", "Kalınlık 6 mm’yi geçerse <b>44.07</b>, geçmezse <b>44.08</b>; kenar veya yüzüne devamlı şekil verilmişse <b>44.09</b>"],
            ["8", "Levha mı?", "Yonga levha, OSB <b>44.10</b> · lif levha, MDF <b>44.11</b> · kontrplak, kaplamalı levha <b>44.12</b> · yoğunlaştırılmış <b>44.13</b>"],
            ["9", "Mamul ahşap eşya mı?", "Çerçeve <b>44.14</b> · ambalaj, palet <b>44.15</b> · fıçı <b>44.16</b> · alet, sap, ayakkabı kalıbı <b>44.17</b> · doğrama <b>44.18</b> · mutfak-sofra <b>44.19</b> · kakma, küçük kutu, süs <b>44.20</b> · diğer <b>44.21</b>"]
        ],
        "dipnot": ""
    },
    "pozisyon_haritasi": [
        ["44.01", "Yakacak odun; yonga; talaş ve odun artıkları", "Aglomere olsun olmasın; kereste olarak kullanılmayan artık", "Odun pelleti, briket, selüloz yongası, talaş"],
        ["44.02", "Odun kömürü", "Havasız karbonlaştırma; meyve kabuğu kömürü dahil", "Mangal kömürü, hindistan cevizi kabuğu kömürü"],
        ["44.03", "Yuvarlak ağaçlar", "Kabuğu soyulmuş veya kabaca kare yontulmuş olabilir", "Tomruk, elektrik direği, kağıtlık odun"],
        ["44.04", "Çember, sırık, sivri kazık, kaba çubuk, kasnak tahtası", "Kabaca yontulmuş, torna edilmemiş", "Çit kazığı, baston taslağı, kibrit kutusu şeridi"],
        ["44.05", "Ağaç yünü; ağaç unu", "Uzun kıvrık şerit / ince düzgün toz", "Ambalaj ağaç yünü, plastik dolgu unu"],
        ["44.06", "Demiryolu veya tramvay traversleri", "Planyalanmamış, dikdörtgen kesitli", "Kreozotlu travers, köprü traversi"],
        ["44.07", "Biçilmiş ağaç, kalınlığı 6 mm’yi geçen", "Rendelenmiş, zımparalanmış, uç uca eklenmiş olabilir", "Kalas, kiriş, tahta, lata"],
        ["44.08", "Kaplama ve kontrplak yaprakları (≤ 6 mm)", "Soyma, dilimleme ile elde", "Kaplamalık yaprak, kontrplak katı"],
        ["44.09", "Devamlı şekil verilmiş ağaç", "Lamba, yiv, şev, korniş, profil", "Birleştirilmemiş parke şeridi, süpürgelik, pervaz"],
        ["44.10", "Yonga levha, OSB, waferboard", "Yongalar gözle seçilebilir; organik bağlayıcı", "Yonga levha, OSB"],
        ["44.11", "Lif levha", "Liflerine ayrılmış lignoselülozik madde", "MDF, sert levha, yumuşak yalıtım levhası"],
        ["44.12", "Kontrplak, kaplamalı levha, benzeri lamine ağaç", "Çapraz damarlı katlar; parke taklidi panel dahil", "Kontrplak, kontrtabla, LVL"],
        ["44.13", "Yoğunlaştırılmış ağaç", "Yoğunluk ve sertlik artırılmış", "Metalize ağaç, sıkıştırılmış kayın blok"],
        ["44.14", "Resim, fotoğraf, ayna çerçeveleri", "Çerçeveli cam ayna hariç", "Ahşap resim çerçevesi"],
        ["44.15", "Sandık, kasa, kablo makarası, palet", "Ambalaj ve yük taşıma", "Meyve kasası, palet, kablo makarası"],
        ["44.16", "Fıçıcı eşyası ve fıçı tahtaları", "Zıvanalı tahtalardan çemberli gövde", "Şarap fıçısı, fıçı tahtası"],
        ["44.17", "Alet, alet gövde ve sapı; ayakkabı kalıbı", "İş gören kısmı Fasıl 82 maddesinden değil", "Tokmak, kazma sapı, fırça gövdesi"],
        ["44.18", "Bina ve inşaat doğraması", "Kapı, pencere, beton kalıbı, parke paneli, glulam", "Ahşap kapı, panjur, padavra"],
        ["44.19", "Mutfak ve sofra eşyası", "Masa ve mutfak takımı niteliği", "Kesme tahtası, tahta kaşık"],
        ["44.20", "Kakma ağaç; küçük kutular; süs eşyası", "Özenli işçilik; Fasıl 94 dışı küçük döşeme", "Mücevher kutusu, biblo"],
        ["44.21", "Diğer ahşap eşya", "Kalıntı pozisyon; ahşap aksam ve parçalar", "Elbise askısı, tabut, kürdan, kibrit çöpü"]
    ],
    "notlar": [
        ["Bölüm IX", "Bölüm IX’un bölüm notu yoktur. Bölüm; Fasıl 44 (ağaç ve ahşap eşya, odun kömürü), Fasıl 45 (mantar) ve Fasıl 46 (hasır ve sepetçi eşyası) fasıllarından oluşur."],
        ["Fasıl 44 Not 1", "Fasıl dışı: parfümeri, eczacılık, böcek veya mantar öldürme vb. amaçlı dilim, rendelenmiş, kırılmış, öğütülmüş veya toz ağaç (12.11); işlenmemiş bambu ve örgüye mahsus odunsu maddeler (yarılmış, biçilmiş veya kesilmiş olsun olmasın) (14.01); boyacılık veya debagat amaçlı dilim veya toz ağaç (14.04); aktif kömür (38.02); 42.02 eşyası; Fasıl 46 eşyası; Fasıl 64 ayakkabı ve aksamı; Fasıl 66 eşyası (şemsiye, baston ve aksamı); 68.08 eşyası; 71.17 taklit mücevherat; Bölüm XVI–XVII eşyası (makine aksamı, mahfazalar, kabinler, araba yapımına mahsus eşya); Bölüm XVIII eşyası (saat kutuları, müzik aletleri ve aksamı); ateşli silah aksamı (93.05); Fasıl 94 (mobilya, lamba, prefabrik yapı); Fasıl 95 (oyuncak, oyun, spor malzemesi); Fasıl 96 (pipo, düğme, kurşun kalem, monopod, bipod, tripod) – <b>96.03 eşyasının ahşap gövde ve sapları hariç</b>; Fasıl 97 (sanat eserleri)."],
        ["Fasıl 44 Not 2", "“Yoğunlaştırılmış ahşap”: kimyasal veya fiziksel işlem görmüş (tabakalıysa yapıştırmadan daha ileri bir işlem görmüş), böylece yoğunluğu ve sertliği önemli derecede artmış ve mekanik dayanıklılık ya da kimyasal veya elektrik etkilerine karşı daha fazla direnç kazanmış masif veya yapıştırılmış levhalardan oluşan ağaç."],
        ["Fasıl 44 Not 3", "44.14 ila 44.21, ahşap eşyaya uygulandığı gibi yonga levha veya benzeri levha, lif levha, lamine (kaplama) ağaç veya yoğunlaştırılmış ağaçtan aynı eşyaya da uygulanır."],
        ["Fasıl 44 Not 4", "44.10, 44.11 ve 44.12 ürünleri; 44.09’daki şekillerde işlenmiş, eğilmiş, ondüle edilmiş, perfore edilmiş, kare veya dikdörtgen dışı kesilmiş ya da başka işlem görmüş olabilir; yeter ki başka pozisyonların eşya vasfını kazanmasın."],
        ["Fasıl 44 Not 5", "Kesici kısmı, iş gören kenarı, yüzü veya diğer iş gören kısmı Fasıl 82 Not 1’deki maddelerden olan aletler 44.17’ye dahil değildir."],
        ["Fasıl 44 Not 6", "Not 1 saklı kalmak ve metin başka türlü gerektirmemek kaydıyla, fasıl pozisyonlarında “ağaç”a yapılan atıf bambuları ve odunsu yapıdaki diğer maddeleri de kapsar."],
        ["Genel Açıklamalar", "Dört grup: işlenmemiş ağaç, yakacak, kömür, yün-un, travers (44.01–44.06); biçilmiş, dilimlenmiş, parmak eklemeli ve şekil verilmiş ağaç (44.07–44.09); yonga, lif, lamine ve yoğunlaştırılmış levhalar (44.10–44.13); ahşap eşya (44.14–44.21)."],
        ["Genel Açıklamalar", "Kurutma, yüzeysel kömürleştirme, astarlama, boyama, vernikleme, kreozot vb. ile emprenye gibi koruyucu işlemler sınıflandırmayı etkilemez. Tamamlanmamış veya demonte ahşap eşya, parçaları bir arada ise bitmiş eşya gibi sınıflandırılır."],
        ["Genel Açıklamalar", "Ağaç ve plastik tabakalı yapı panelleri esas karakteri veren dış yüzeye göre: yonga levha dış tabaka + plastik yalıtım tabakası 44.10; dış yüzleri plastik, içteki ağacı yalnız destek olan panel çoğu kez Fasıl 39."],
        ["44.07 / 44.08 Açıklama Notları", "Uzunlamasına biçilmiş, dilimlenmiş veya soyulmuş ağaç: kalınlık <b>6 mm’yi geçerse 44.07</b>, geçmezse 44.08. Planyalama, zımparalama, parmak birleştirme pozisyonu değiştirmez; kabaca kare olanlar 44.03’tedir."],
        ["44.09 Açıklama Notu", "“Kenar” uçları da kapsar. Devamlı şekil: lamba-yiv, set, şev, (V) oluk, korniş, kalıplanmış çubuk ve pervaz, yuvarlatılmış çubuk. Parke şeritleri yalnız planyalanmış veya parmak eklenmişse 44.07’de kalır; panel halinde birleştirilmiş parke 44.18’dedir."],
        ["44.10 Açıklama Notu", "Yonga levha genellikle levha ağırlığının <b>%15’ini aşmayan</b> organik bağlayıcıyla aglomere edilir; OSB yongaları genişliğinin en az iki katı uzunluktadır. Kaplama levhasıyla kaplanmış yonga levha 44.12’ye, çimento veya alçı gibi mineral bağlayıcılı levhalar 68.08’e gider."],
        ["44.11 Açıklama Notu", "Kuru süreçle üretilen orta yoğunluklu lif levhanın (MDF) yoğunluğu genellikle 0,45–1 gr/cm3; ıslak süreçte sert levha 0,8 gr/cm3’ü geçer, yumuşak (yalıtım) levha 0,35 gr/cm3 veya daha azdır. Tabakalı yapısı yarıldığında görülen karton (presspan, saman kartonu) Fasıl 48’dedir."],
        ["44.12 Açıklama Notu", "Kontrplak: üç veya daha fazla katın damarları birbirine çapraz gelecek şekilde tutkallanmasıyla elde edilir; ortadaki kata “göbek” denir. Glulam gibi masif lamine kiriş ve kemerler 44.18’de, hücreli paneller 44.18’de, lamine yoğunlaştırılmış levhalar 44.13’tedir."],
        ["44.15 Açıklama Notu", "Monte edilmemiş sandık parçaları tam bir kabın esas özelliğini verecek şekilde bir arada olmalıdır. Kablo makaraları genellikle 1 m’yi aşan çaptadır. Yeniden kullanılabilecek kullanılmış kasa 44.15’te; yalnız yakacak olabilecek olanlar 44.01’dedir."],
        ["44.18 Açıklama Notu", "Marangozluk mamulleri: kapı, pencere, kepenk, merdiven, çerçeveler; doğrama: kiriş, mertek, payanda; beton kalıpları, hücreli paneller, birleştirilmiş parke panelleri, glulam. Padavra: bir ucu 5 mm’den kalın, diğer ucu 5 mm’den ince, uzunluğuna biçilmiş ağaç. Duvara tutturulan dolaplar 94.03, prefabrik yapılar 94.06."],
        ["44.20 / 44.21 Açıklama Notları", "44.20: kakma ağaç, mücevher ve çatal-bıçak kutuları, enfiye ve benzeri küçük kutular, heykelcik ve süs eşyası, Fasıl 94’e girmeyen küçük döşeme eşyası. 44.21: makara ve bobinler, kafes ve kovanlar, el merdivenleri, elbise askıları, kürdan, kibrit çöpü, tabut ve önceki pozisyonlardaki eşyanın ahşap parçaları (44.16 hariç)."]
    ],
    "sinir_komsulari": [
        ["Parfümeri veya eczacılık amaçlı dilimlenmiş ya da toz ağaç", "12.11", "Fasıl 44 Not 1"],
        ["Yarılmış, parlatılmış işlenmemiş bambu kamışı", "14.01", "Örgüye mahsus bitkisel madde; Not 1"],
        ["Boyacılık veya debagat amaçlı toz ağaç; hindistan cevizi kabuğu unu", "14.04", "Not 1; 44.05 hariç tutması"],
        ["Reçine ile çıra haline getirilmiş odun", "36.06", "44.01 hariç tutması"],
        ["Aktif kömür", "38.02", "Not 1; 44.02 hariç tutması"],
        ["Ahşap bavul veya valiz", "42.02", "42.02’nin ilk kısmı her maddeden olabilir; Not 1"],
        ["Bambu veya söğütten örülmüş sepet", "46.02", "Sepetçi eşyası; Not 1"],
        ["Ahşap baston, şemsiye sapı", "66.02 / 66.03", "Fasıl 66 eşyası; Not 1"],
        ["Ağaç yünü veya talaşın çimentoyla aglomere edildiği levha", "68.08", "Mineral bağlayıcı; 44.10 hariç tutması"],
        ["Çerçeveli cam ayna", "70.09", "44.14 hariç tutması"],
        ["Ahşap şapka kalıbı; ahşap döküm modeli", "84.49 / 84.80", "44.17 ve 44.21 hariç tutmaları"],
        ["Ahşap tüfek dipçiği", "93.05", "Ateşli silah aksamı; Not 1"],
        ["Ahşap mobilya, demonte ahşap masa; prefabrik ahşap ev", "94.03 / 94.06", "Not 1; 44.18 hariç tutması"],
        ["Ahşap oyuncak, oyun ve spor malzemesi", "Fasıl 95", "Not 1"],
        ["Bitmiş fırça veya süpürge; kömür kalem", "96.03 / 96.09", "Fırçanın ahşap gövde ve sapı ise 44.17’de kalır"]
    ],
    "tuzaklar": [
        "<b>Ahşap mücevher kutusu 42.02 değildir.</b> 42.02’nin ikinci kısmındaki mücevher kutuları yalnız sayılan maddelerden (deri, plastik yaprak, mensucat, vulkanize lif, karton) veya bunlarla kaplanmış olmalıdır; ahşap mücevher kutusu 44.20’dedir. Bavul ve valiz ise ilk kısımda olduğundan ahşaptan da olsa 42.02’ye gider.",
        "<b>6 mm sınırı.</b> Biçilmiş veya dilimlenmiş ağaç 6 mm’yi geçerse 44.07, geçmezse 44.08. Kasnak tahtası gibi dar örgü şeritleri ise 44.04’tedir.",
        "<b>Rendeleme 44.09 yapmaz.</b> Planyalama, zımparalama, parmak birleştirme 44.07–44.08’de bırakır; bir kenar veya yüz boyunca devamlı şekil (lamba, yiv, şev, korniş) 44.09’a taşır; uçlarına zıvana veya kırlangıç kuyruğu açılmış ya da panel halinde birleştirilmiş ağaç 44.18’e gider.",
        "<b>Parke üç yere ayrılır.</b> Birleştirilmemiş lambalı şerit 44.09; birleştirilmiş (çok katlı) parke paneli 44.18; parke görünümlü ince kaplamalı kontrplak veya lamine panel 44.12.",
        "<b>Her lamine ürün 44.12 değildir.</b> Glulam kiriş ve kemerler 44.18; lamine yoğunlaştırılmış levha 44.13; lamine bloktan dilimlenmiş kaplama yaprağı 44.08; hücreli panel 44.18.",
        "<b>Bambu üç yöne çekilir.</b> İşlenmemiş bambu 14.01, bambu sepet 46.02, bambu mobilya 94; ama bambu kontrplak, bambu odun kömürü, bambu yonga ve levhalar Not 6 gereği Fasıl 44’tedir.",
        "<b>Aletlerde iş gören kısım belirler.</b> Tamamen ahşap tokmak, tırmık, kürek 44.17; iş gören kısmı Fasıl 82 Not 1 maddesinden olan alet Fasıl 82. Fırça gövde ve sapı 44.17, bitmiş fırça 96.03.",
        "<b>Kullanılmış sandık ikiye ayrılır.</b> Yeniden kullanılabiliyorsa 44.15; yalnız yakacak olarak işe yarıyorsa 44.01.",
        "<b>El merdiveni bina merdiveni değildir.</b> İnşaat doğraması olarak merdiven 44.18; el merdivenleri ve basamaklar 44.21.",
        "<b>Her kömür 44.02 değildir.</b> Aktif kömür 38.02, kokulu tablet kömür 33.07, ilaç olarak hazırlanmış kömür Fasıl 30, çizim kömürü 96.09."
    ],
    "hafiza": {
        "kanca": "ORMAN – TESTERE – PRES – ATÖLYE",
        "aciklama": "<b>ORMAN</b> 44.01–44.06: yakacak, kömür, tomruk, kazık, yün-un, travers · <b>TESTERE</b> 44.07–44.09: biçilmiş (6 mm’yi geçen), yaprak (≤ 6 mm), profil · <b>PRES</b> 44.10–44.13: yonga, lif, kontrplak, yoğunlaştırılmış · <b>ATÖLYE</b> 44.14–44.21: çerçeve, sandık, fıçı, alet, doğrama, mutfak, süs, diğer. Atölyeden çıkan eşya mobilya, oyuncak veya sepet ise kapıdan çıkar: 94, 95, 46."
    },
    "sinav_odagi": [
        "“Hangisi farklı fasılda/pozisyonda yer alır?” kalıbı: odun kömürü, yonga levha, kontrplak, ahşap merdiven gibi Fasıl 44 eşyası arasına 42.02’deki ahşap bavul konmuş; ahşap kapı, padavra, panjur (44.18) arasında kontrplağın (44.12) farklı olduğu sorulmuştur.",
        "Demonte ahşap masa veya dolap: mobilya olduğu için Fasıl 94; GYK 2(a) (demonte eşya) ve masa-sandalye takımlarında GYK 3 ile birlikte sorulmuştur.",
        "Mahfaza soruları: ahşap mücevher kutusunun 42.02’de değil 44.20’de yer aldığı, 42.02 seçenekleri arasında çeldirici olarak kullanılmıştır.",
        "Tarife sıralaması (dizilim) soruları: odun kömürü (44.02) → ahşap travers (44.06) → laminat parke → ahşap tabut (44.21) sırası doğru dizilim olarak verilmiştir.",
        "Tropikal ağaç kavramı: tropikal ağaç adları Açıklama Notlarının ekindeki listede pilot isimleriyle verilmiştir (limba, balsa, tik gibi); okaliptüs bu listede yer almaz.",
        "“Hangi pozisyonda ayakkabıyla ilgili bir ürün sınıflandırılmaz?” kalıbında 44.17 (ahşap bot ve ayakkabı kalıpları) ayakkabıyla ilgili pozisyonlardan biri olarak çeldirici yapılmıştır."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Aşağıdakilerden hangisi Türk Gümrük Tarife Cetveli’nin farklı faslında yer alır?",
            "secenekler": ["Odun kömürü", "Yonga levha", "Ahşap merdiven", "Kontrplak", "Ahşap bavul"],
            "cevap": "E",
            "aciklama": "Fasıl 44 Not 1, 42.02 eşyasını fasıl dışında bırakır; 42.02’nin ilk kısmındaki bavul ve valizler her maddeden olabileceğinden ahşap bavul Fasıl 42’dedir. Odun kömürü (44.02), yonga levha (44.10), kontrplak (44.12) ve ahşap merdiven Fasıl 44’tedir."
        },
        {
            "soru": "Demonte olarak gelen ahşap masa hangi fasılda sınıflandırılır?",
            "secenekler": ["42", "44", "47", "94"],
            "cevap": "D",
            "aciklama": "Fasıl 44 Not 1 mobilyayı Fasıl 94’e bırakır; demonte gelmesi GYK 2(a) gereği sınıflandırmayı değiştirmez. Ahşaptan yapılmış olması masayı Fasıl 44’e sokmaz."
        }
    ],
    "ozet": [
        "Önce Not 1: mobilya, oyuncak, sepet, şemsiye, alet, müzik aleti, 42.02 mahfazası ahşaptan da olsa Fasıl 44 dışıdır.",
        "Ham ağaç 44.01–44.06: yakacak ve artık 44.01, kömür 44.02, tomruk 44.03, kazık ve sırık 44.04, yün-un 44.05, travers 44.06.",
        "Biçilmiş ağaçta ölçüt 6 mm: üstü 44.07, altı 44.08; devamlı şekil 44.09.",
        "Levhalar: yonga 44.10, lif 44.11, kontrplak ve kaplamalı 44.12, yoğunlaştırılmış 44.13; işlenmeleri eşya vasfı vermedikçe yerlerinde kalır.",
        "Eşya 44.14–44.21; levhalardan yapılmış eşya da buradadır (Not 3). 44.21 kalıntı pozisyondur.",
        "Koruyucu işlemler ve demonte sunum sınıflandırmayı değiştirmez."
    ],
    "sorular": sorular,
}

yaz(44, obj)
