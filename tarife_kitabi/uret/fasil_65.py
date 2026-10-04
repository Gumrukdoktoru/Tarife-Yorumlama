#!/usr/bin/env python3
"""Fasıl 65 modülü üreteci."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_64_69 import soru, yaz  # noqa: E402

EP = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
TN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"

obj = {
    "tur": "fasil",
    "fasil": 65,
    "baslik": "Başlıklar ve aksamı",
    "bolum": "XII",
    "oz": {
        "vurgu": "Fasıl 65, kullanım amacı ve maddesi ne olursa olsun şapka taslaklarını, şapkaları, diğer başlıkları ve saç filelerini kapsar. Pozisyonu <b>yapım tekniği</b> (keçe, şerit/örgü, örme veya parça mensucat) ile <b>bitmişlik derecesi</b> (şekil, kenar, astar, donatım) belirler; bunlara uymayan her başlık, özellikle koruyucu miğferler, 65.06’dadır.",
        "maddeler": [
            "Taslaklar: keçeden olanlar 65.01, şerit birleştirme veya örgüyle yapılanlar 65.02; kalıplanarak şekil verilmemiş, kenar yapılmamış (65.02’de ayrıca astarlanmamış, donatılmamış) olmalıdır.",
            "Şapkalar: şeritten/örgüden olanlar 65.04; örme veya parça halindeki dantel, keçe, mensucattan olanlar ile her maddeden saç fileleri 65.05.",
            "65.06: koruyucu başlıklar (mikrofonlu veya kulaklıklı olsa bile) ile kauçuk, plastik, deri, kürk, kuş tüyü, yapma çiçek ve metal başlıklar.",
            "65.07: iç şerit, astar, kılıf, kasnak, çatı, siperlik ve çene altı kayışı. 65.03 pozisyonu boştur.",
            "Fasıl dışı: kullanılmış balyalı başlık (63.09), amyant (68.12), oyuncak ve karnaval şapkası (Fasıl 95), hayvan başlığı (42.01), peruk (67.04), şal ve eşarp (61.17 / 62.14).",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Balyalı kullanılmış başlık, amyanttan başlık, oyuncak veya karnaval şapkası, hayvan başlığı, peruk, şal/eşarp mı?",
             "<b>63.09</b> · <b>68.12</b> · Fasıl 95 · <b>42.01</b> · <b>67.04</b> · <b>61.17</b> / <b>62.14</b>"],
            ["2", "Başlığa takılmaya hazır iç şerit, astar, kılıf, kasnak, çatı, siperlik veya çene altı kayışı mı?", "<b>65.07</b>"],
            ["3", "Keçeden, kalıplanarak şekil verilmemiş ve kenar yapılmamış taslak, disk veya üstüvane mi?", "<b>65.01</b>"],
            ["4", "Şerit birleştirme veya örgüyle yapılmış; şekil, kenar, astar, donatım yapılmamış taslak mı?", "<b>65.02</b>"],
            ["5", "Şerit birleştirme veya örgüyle yapılmış şapka/başlık mı (şekil verilmiş, kenar yapılmış ya da astarlı/donatılmış)?", "<b>65.04</b>"],
            ["6", "Örme veya parça halindeki dantel, keçe, mensucattan şapka ya da herhangi bir maddeden saç filesi mi?*", "<b>65.05</b>"],
            ["7", "Hiçbiri değilse (koruyucu miğfer; kauçuk, plastik, deri, kürk, tüy, yapma çiçek, metal başlık)", "<b>65.06</b>"],
        ],
        "dipnot": "* Kuş tüyünden veya yapma çiçekten şapkalar 65.05’in dışındadır (65.06); buna karşılık üzeri dokumaya elverişli mensucatla kaplanmış mantar veya ağaç özünden miğfer 65.05’te sayılmıştır. Süs olarak takılan tüy ve yapma çiçek pozisyonu değiştirmez.",
    },
    "pozisyon_haritasi": [
        ["65.01", "Keçe şapka taslakları, diskler, üstüvaneler",
         "Kalıplanarak şekil verilmemiş, kenar yapılmamış; boyuna yarılmış dahil",
         "Tüy keçe konik taslak, keçe disk"],
        ["65.02", "Şerit birleştirme veya örgü şapka taslakları",
         "Şekil, kenar, astar, donatım yok; başa uygun oval yok",
         "Hasır, rafya, palmiye lifi örgü taslak"],
        ["65.03", "Boş pozisyon", "Metinde içeriksiz olarak yer alır", "—"],
        ["65.04", "Şeritten birleştirilmiş veya örülmüş şapkalar",
         "65.02 taslağının şekil verilmiş, kenar yapılmış ya da astarlı/donatılmış hali",
         "Kurdeleli hasır şapka, şeritten kadın şapkası"],
        ["65.05", "Örme veya parça mensucat, dantel, keçe şapkalar; saç fileleri",
         "Şerit halinde olmayan dokumaya elverişli madde; saç filesi her maddeden",
         "Örme bere, fes, kasket, aşçı başlığı, keçe şapka, kapüşon"],
        ["65.06", "Diğer başlıklar",
         "Koruyucu başlıklar; kauçuk, plastik, deri, kürk, tüy, yapma çiçek, metal",
         "Motosiklet kaskı, baret, askerî miğfer, banyo bonesi, kürk şapka"],
        ["65.07", "İç şerit, astar, kılıf, kasnak, siperlik, çene altı kayışı",
         "Başlığa takılmaya hazır bağlantı parçaları",
         "Kesilmiş deri iç şerit, kep siperliği, çene kayışı"],
    ],
    "notlar": [
        ["Fasıl 65 Not 1",
         "Fasıl dışı: (a) 63.09’daki kullanılmış başlıklar; (b) amyanttan (asbestten) başlıklar (68.12); (c) Fasıl 95’teki oyuncak bebek şapkaları, diğer oyuncak şapkalar veya karnaval eşyası."],
        ["Fasıl 65 Not 2",
         "65.02’ye dikilerek hazırlanan şapka taslakları dahil değildir; yalnızca şeritlerin helezoni şekilde basitçe dikilmesiyle elde edilenler 65.02’de kalır."],
        ["Genel Açıklamalar",
         "Fasıl; kullanım amacına (günlük giyim, tiyatro, kılık değiştirme, korunma vb.) ve maddesine bakılmaksızın şapka taslaklarını, şapkaları, başlıkları, her türlü saç filesini ve bazı başlık bağlantılarını kapsar. Süs ve teferruat Fasıl 71 maddelerinden de olabilir."],
        ["Genel Açıklamalar (hariç)",
         "Hayvan başlıkları (42.01); şal, eşarp, kaşkol, peçe (61.17 veya 62.14); balyalı kullanılmış başlıklar (63.09); peruklar (67.04); amyant başlıklar (68.12); oyuncak ve karnaval şapkaları (Fasıl 95); başlığa birleştirilmemiş toka, kopça, nişan, süs tüyü, yapma çiçek (kendi pozisyonları)."],
        ["65.01 Açıklama Notu",
         "Konik keçe taslaklar; tepesi yuvarlatılmış veya kenarı uzatılmış ama şekil verilmemiş olanlar dahil (düz zemine dik konulunca kenar yayılmaz, konik kalır). Keçe diskler yaklaşık <b>60 cm</b> çapında; üstüvanelerin çevresi <b>100 cm</b>, yüksekliği <b>40–50 cm</b>. Düzleme, perdahlama, boyama, apreleme sınıflandırmayı etkilemez."],
        ["65.02 Açıklama Notu",
         "Hububat sapı, saz, rafya, palmiye lifi, sisal, kâğıt, ağaç veya plastik şeritlerden doğrudan örülen ya da genellikle <b>5 cm’den dar</b> şeritlerin helezoni birleştirilmesiyle yapılan taslaklar. Olduğu gibi plaj veya kır şapkası olarak kullanılabilseler de şekil verilmemiş, astarlanmamış, donatılmamışsa burada kalırlar. 65.04’teki şapkalardan, başa uygun oval şekil almamış olmalarıyla ayrılırlar. Ağartma, boyama gibi işlemler etkilemez; kurdele veya astarla donatılanlar 65.04’tedir."],
        ["65.04 Açıklama Notu",
         "Şekil verme: taslak jelatin, çiriş, zamk vb. ile sertleştirilip kalıpta preslenerek ütülenir; ağız baş çevresinin oval şeklini alır. Şeritlerin doğrudan birleştirilmesiyle yapılan şapkalar ile şekil verilmiş/kenar yapılmış ya da astarlanmış/donatılmış 65.02 taslakları buradadır; yapma çiçek, tüy, iğne gibi süslerle donatılabilir."],
        ["65.05 Açıklama Notu",
         "Doğrudan örülmüş (keçeleştirilmiş olsun olmasın) veya parça halindeki dantel, keçe, mensucattan (yağlanmış, kauçuklanmış vb. olabilir) şapkalar; 65.01 taslak, disk ve üstüvanelerinden yapılan keçe şapkalar; dikilerek elde edilen taslaklar. Bere, bone, fes, kasket, meslek ve din adamı başlıkları, aşçı, rahibe, hemşire başlıkları, mensucat kaplı mantar veya ağaç özü miğfer, yağlı mensucattan gemici başlığı, kapüşon, silindir şapka; her maddeden saç fileleri. Hariç: tüy veya yapma çiçekten şapkalar (65.06); giysiyle birlikte sunulan çıkarılabilir kapüşonlar."],
        ["65.06 Açıklama Notu",
         "Önceki pozisyonlarda veya Fasıl 63, 68, 95’te yer almayan bütün başlıklar: koruyucu dolgulu, mikrofonlu veya kulaklıklı olsun olmasın koruyucu başlıklar (spor, asker, itfaiyeci, motosikletçi, kömür ve inşaat işçisi miğferleri); kauçuk/plastik başlıklar (banyo bonesi, kapüşon); deri veya terkip deri, kürk veya taklit kürk, kuş tüyü veya yapma çiçek ve metal başlıklar."],
        ["65.07 Açıklama Notu",
         "Yalnız başlık bağlantıları: uzunluğuna kesilmiş veya birleştirmeye hazırlanmış iç şeritler, astarlar, kılıflar, şapka kasnakları, açılır kapanır şapka çatıları, siperlikler, takılmaya hazır çene altı kayışları. Gözleri korumaya mahsus siperlik ancak bir başlık kısmıyla birlikteyse buradadır, aksi halde maddesine göre. Tepe içine tespit edilen etiketler hariç."],
        ["Fasıl 95 Not 1(g)",
         "Fasıl 65’teki spor başlıkları Fasıl 95’e girmez; spor kaskları Fasıl 65’te kalır."],
    ],
    "sinir_komsulari": [
        ["Balya halinde, fazla kullanıldığı belli eski şapkalar", "63.09", "Not 1(a)"],
        ["Amyanttan başlık", "68.12", "Not 1(b)"],
        ["Oyuncak bebek şapkası, karnaval şapkası", "Fasıl 95", "Not 1(c)"],
        ["Atlar için başlık", "42.01", "Hayvan başlıkları saraciye eşyasıdır"],
        ["Şal, eşarp, kaşkol, peçe", "61.17 / 62.14", "Giyim aksesuarı; başlık değil"],
        ["Peruk ve benzerleri", "67.04", "Genel Açıklamalar hariç tutması"],
        ["Başlığa takılmamış toka, nişan, süs tüyü, yapma çiçek", "Kendi pozisyonları", "Birleştirilmemiş süs ve teferruat"],
        ["Başlıkla birleşmemiş göz siperliği", "Maddesine göre", "65.07 Açıklama Notu"],
        ["Pilotlar için kulaklıklı, mikrofonlu başlık", "65.06", "85.18 hariç tutması; koruyucu başlık"],
        ["Askerî çelik miğfer", "65.06", "Fasıl 93 dışı"],
        ["Dalgıç elbisesine takılan dalgıç başlığı", "90.20", "Teneffüs cihazları pozisyonunda sayılmıştır"],
        ["Bisiklet veya binicilik kaskı", "65.06", "Fasıl 95 Not 1(g)"],
        ["Örme veya kroşe bebek bonesi", "65.05", "Fasıl 61 hariç tutması; giyim eşyası değil"],
        ["İnsan saçından saç filesi", "65.05", "Fasıl 5 ve Fasıl 67 hariç tutmaları"],
        ["Kuş tüyünden veya yapma çiçekten şapka", "65.06", "65.05 ve Fasıl 67 hariç tutmaları"],
    ],
    "tuzaklar": [
        "<b>Plaj şapkası gibi kullanılabilen taslak hâlâ taslaktır.</b> Örgü taslak şekil verilmemiş, kenar yapılmamış, astarlanmamış ve donatılmamışsa 65.02’de kalır; kurdele veya astar takılınca 65.04’e geçer.",
        "<b>Ağartma, boyama taslağı şapka yapmaz.</b> Bu işlemler ile taslağın orijinal şekline sokulması 65.01 ve 65.02’deki sınıflandırmayı etkilemez.",
        "<b>Dikilmiş taslak 65.02’de değildir.</b> Not 2’ye göre yalnızca şeritlerin helezoni basitçe dikilmesiyle elde edilenler kalır; parça mensucattan dikilen taslaklar 65.05’tedir.",
        "<b>Yapma çiçekle süslü ≠ yapma çiçekten yapılmış.</b> Süslü hasır veya keçe şapka 65.04 / 65.05’te kalır; tamamı tüyden veya yapma çiçekten şapka 65.06’dadır.",
        "<b>Mantar miğferin yeri kaplamaya bağlıdır.</b> Üzeri dokumaya elverişli mensucatla kaplı mantar veya ağaç özü miğfer 65.05’te sayılmıştır; koruyucu miğferler 65.06’dadır.",
        "<b>Kulaklık ve mikrofon başlığı değiştirmez.</b> Koruyucu başlıklar mikrofonlu veya kulaklıklı olsa da 65.06’dadır; kulaklıklı pilot başlıkları 85.18’e girmez.",
        "<b>Spor kaskı Fasıl 95’te değildir.</b> Fasıl 95 Not 1(g) spor başlıklarını Fasıl 65’e bırakır; oyuncak ve karnaval şapkaları ise Fasıl 95’tedir.",
        "<b>Saç filesi her maddeden 65.05’tir.</b> İnsan saçından yapılmış olsa bile 67.04’e değil 65.05’e gider.",
        "<b>65.07 yalnız hazır bağlantı parçaları içindir.</b> İç şerit uzunluğuna kesilmiş, çene kayışı takılmaya hazır olmalıdır; tepeye konan etiketler ve başlık kısmı olmayan göz siperlikleri hariçtir.",
    ],
    "hafiza": {
        "kanca": "01 → 05, 02 → 04: Taslak büyür, şapka olur; 06 sığınak, 07 iç donanım",
        "aciklama": "Keçe taslak <b>65.01</b> şekil alınca <b>65.05</b>’e (keçe/kumaş şapka) gider; şerit taslak <b>65.02</b> şekil, kenar, astar veya kurdele alınca <b>65.04</b>’e (şerit şapka) gider. Hiçbir kalıba uymayan kask, plastik bone, kürk veya tüy şapka “diğer” <b>65.06</b>’ya sığınır; şapkanın iç şeridi, astarı, siperliği ve çene kayışı <b>65.07</b>’dedir. 65.03 boştur.",
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda daha çok seçeneklerde/çeldirici olarak yer almıştır; doğrudan Fasıl 65’i soran soru azdır.",
        "Pozisyon sırası soruları: miğferin (65.06) şemsiye (66.01), baston (66.02) ve perukla (67.04) karşılaştırılıp hangisinin daha sonraki pozisyonda olduğunun sorulması.",
        "Eşyaları pozisyon numarasına göre küçükten büyüğe sıralama sorularında plastik madenci başlığının (65.06) seçeneklerde kullanılması.",
        "Madde fasıllarıyla karşılaştırma: mantardan şapka siperliği gibi başlık aksamının Fasıl 45’te değil Fasıl 65’te kalması; başlıkların 39, 40, 42, 43, 45, 46 ve 48. fasıllardan hariç tutulması.",
        "Bölüm XII kapsamı: başlıkların ayakkabı, şemsiye, baston ve perukla aynı bölümde, ardışık fasıllarda yer alması.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Aşağıdakilerden hangisi Türk Gümrük Tarife Cetveli’nde diğerlerinden daha sonraki bir pozisyonda sınıflandırılır?",
            "secenekler": ["Şemsiye", "Baston", "Peruk", "Miğfer"],
            "cevap": "C",
            "aciklama": "Miğfer koruyucu başlık olarak 65.06’da, şemsiye 66.01’de, baston 66.02’de, peruk ise 67.04’te sınıflandırılır; en sonraki pozisyon peruktur.",
        },
    ],
    "ozet": [
        "Kullanım amacı ve madde ne olursa olsun başlık Fasıl 65’tedir; istisnalar 63.09, 68.12, Fasıl 95, 42.01, 67.04, 61.17 / 62.14.",
        "Keçe taslak, disk, üstüvane 65.01; şerit/örgü taslak 65.02 (şekilsiz, kenarsız, astarsız, donatımsız).",
        "Şerit/örgü şapka 65.04; örme veya parça mensucat, keçe, dantel şapka ve her maddeden saç filesi 65.05.",
        "Koruyucu başlıklar ile kauçuk, plastik, deri, kürk, tüy, yapma çiçek ve metal başlıklar 65.06.",
        "İç şerit, astar, kılıf, kasnak, siperlik, çene altı kayışı 65.07; 65.03 boştur.",
        "Süs pozisyonu değiştirmez: yapma çiçekle süslü şapka kendi pozisyonunda, yapma çiçekten şapka 65.06’da.",
    ],
}

S = []
# 1 C
S.append(soru(
    "Tarife Cetveline göre, doğrudan örülerek elde edilmiş ve ardından keçeleştirilmiş yünden bere hangi pozisyonda sınıflandırılır?",
    "65.05", ["65.01", "65.04", "65.06", "61.17"], "C", EP,
    "65.05, doğrudan örme suretiyle elde edilen (keçeleştirilmiş olsun olmasın) şapka ve başlıkları kapsar; bereler ve boneler Açıklama Notunda açıkça sayılmıştır. 65.01 keçe taslaklar, 65.04 şeritten yapılan şapkalar içindir. Örme olması onu giyim aksesuarı olarak 61.17’ye götürmez; başlıklar Fasıl 65’tedir.",
    "65.05 Açıklama Notu (2)."))
# 2 A
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinin 65. faslında <b>sınıflandırılmaz</b>?",
    "Atlar için başlık",
    ["İnsan saçından yapılmış saç filesi", "Tiyatro oyununda kullanılan şapka", "Motosikletçi kaskı", "Fes"], "A", OT,
    "Hayvanlar için başlıklar Fasıl 65 Genel Açıklamaları gereği fasıl dışıdır ve 42.01’de sınıflandırılır. Saç fileleri her maddeden (insan saçı dahil) 65.05’te, fesler 65.05’te, motosikletçi kaskları 65.06’dadır. Fasıl, başlıkları kullanım amacına (tiyatro, kılık değiştirme dahil) bakılmaksızın kapsar.",
    "Fasıl 65 Genel Açıklamalar; 65.05 ve 65.06 Açıklama Notları."))
# 3 E
S.append(soru(
    "Fasıl 65 Not 2’ye göre dikilerek hazırlanan şapka taslakları ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
    "65.02’ye girmez; yalnız şeritlerin helezoni basitçe dikilmesiyle elde edilenler 65.02’de kalır.",
    ["Dikiş yöntemine bakılmaksızın tamamı 65.02’de sınıflandırılır; astarlananlar 65.04’e geçer.",
     "Yalnızca keçeden olanlar 65.02’de sınıflandırılır; diğer maddelerden olanlar 65.04’e gider.",
     "Dikiş yöntemine bakılmaksızın tamamı keçe taslak sayılarak 65.01’de sınıflandırılır.",
     "5 cm’den geniş şeritlerden dikilenler 65.02’de, daha dar şeritlerden dikilenler 65.04’te yer alır."], "E", TN,
    "Not 2, dikilerek hazırlanan şapka taslaklarını 65.02’nin dışında bırakır; istisna, şeritlerin helezoni bir şekilde basitçe dikilmesiyle elde edilen taslaklardır. Parça mensucattan dikilen taslaklar 65.05’te yer alır. 65.01 yalnız keçe taslaklar içindir; 5 cm ölçüsü şerit genişliğinin genel tarifidir, bir istisna ölçütü değildir.",
    "Fasıl 65 Not 2; 65.02 ve 65.05 Açıklama Notları."))
# 4 B
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
    "Kalıpta şekil verilmiş, kenarı yapılmış keçe şapka",
    ["Şapka imaline mahsus keçe disk", "Şapka imaline mahsus keçe üstüvane", "Boyuna yarılmış keçe üstüvane", "Şekil verilmemiş, kenarsız keçe şapka taslağı"], "B", FA,
    "Keçe diskler, üstüvaneler (boyuna yarılmış olanlar dahil) ve şekil verilmemiş keçe taslaklar 65.01’dedir. Bu taslaklardan kalıplanarak şekil verilip kenar yapılan keçe şapkalar ise 65.05’te sınıflandırılır. Keçeden olmak tek başına 65.01 için yeterli değildir; belirleyici olan şekil ve kenar işlemidir.",
    "65.01 pozisyon metni ve Açıklama Notu; 65.05 Açıklama Notu."))
# 5 D
S.append(soru(
    "Tarife Cetveline göre, inşaat işçileri için plastikten yapılmış, iç kısmında koruyucu dolgu bulunan baret hangi pozisyonda sınıflandırılır?",
    "65.06", ["39.26", "65.07", "65.05", "95.06"], "D", EP,
    "65.06 Açıklama Notu, koruyucu dolgu malzemesiyle teçhiz edilmiş olsun olmasın inşaat işçilerinin miğferlerini açıkça sayar. Fasıl 39 Bölüm XII eşyasını kapsamaz; 65.07 yalnız bağlantı parçaları, 65.05 mensucat başlıklar içindir. Koruyucu başlık spor eşyası değildir.",
    "65.06 Açıklama Notu; Fasıl 39 Not 2 (Bölüm XII hariç tutması)."))
# 6 B
S.append(soru(
    "Kalıplanarak şekil verilmiş ve kenarı yapılmış, ancak henüz astarı takılmamış ve kurdelesi geçirilmemiş keçe şapka 65.05 pozisyonunda sınıflandırılır. Bu sınıflandırmaya esas olan Genel Yorum Kuralı aşağıdakilerden hangisidir?",
    "GYK 1", ["GYK 2(a)", "GYK 2(b)", "GYK 3(b)", "GYK 4"], "B", GY,
    "65.05 pozisyon metni şapkaları “astarlanmış veya donatılmış olsun olmasın” kapsar; astarsız ve kurdelesiz şapka doğrudan pozisyon metniyle sınıflandırılır, bu GYK 1’dir. Eşya eksik görünse de pozisyon metni astar ve donatımı şart koşmadığından GYK 2(a)’ya başvurmaya gerek yoktur. 2(b), 3(b) ve 4 madde karışımı, esas nitelik ve benzerlik içindir.",
    "GYK 1; 65.05 pozisyon metni ve Açıklama Notu."))
# 7 E
S.append(soru(
    "Aşağıdakilerden hangileri 65.05 pozisyonunda sınıflandırılır? I. Örme bere II. İnsan saçından saç filesi III. Plastikten banyo bonesi IV. Mensucattan rahibe başlığı",
    "I, II ve IV", ["I ve III", "II ve III", "I, III ve IV", "II, III ve IV"], "E", CC,
    "Örme bereler, her maddeden saç fileleri (insan saçı dahil) ve mensucattan rahibe başlıkları 65.05 Açıklama Notunda sayılmıştır. Kauçuk veya plastikten başlıklar, örneğin banyo boneleri, 65.06’dadır. Bu nedenle III’ü içeren seçenekler yanlıştır.",
    "65.05 Açıklama Notu (2), (6) ve saç fileleri; 65.06 Açıklama Notu."))
# 8 A
S.append(soru(
    "Tarife Cetveline göre, rafya şeritlerinden doğrudan örülmüş; kalıplanarak şekil verilmemiş, kenarı yapılmamış, astarlanmamış ve donatılmamış şapka taslağı hangi pozisyonda sınıflandırılır?",
    "65.02", ["65.01", "65.04", "46.02", "65.05"], "A", EP,
    "65.02, her nevi maddeden şeritleri birleştirmek veya örmek suretiyle yapılan, şekil verilmemiş, kenar yapılmamış, astarlanmamış ve donatılmamış taslakları kapsar; rafya Açıklama Notunda sayılan maddelerdendir. Şekil, kenar, astar veya donatım olsaydı 65.04’e geçerdi. Örülmüş olması onu Fasıl 46’ya götürmez; 65.01 keçe taslaklar içindir.",
    "65.02 pozisyon metni ve Açıklama Notu; Fasıl 46 Not 2."))
# 9 C
S.append(soru(
    "Aşağıdakilerden hangisi 65.06 pozisyonunda <b>yer almaz</b>?",
    "Üzeri dokuma mensucatla kaplanmış mantardan miğfer",
    ["Kürkten yapılmış kışlık şapka", "Plastikten yapılmış banyo bonesi", "Kuş tüylerinden yapılmış kadın şapkası", "Metalden yapılmış tören başlığı"], "C", OT,
    "65.05 Açıklama Notu, mantar veya ağaç özünden imal edilip üzeri dokumaya elverişli mensucatla kaplanmış miğferleri açıkça 65.05’te sayar. Kürk, plastik, kuş tüyü ve metalden başlıklar ise 65.06 Açıklama Notunda yer alır. Tuzak, “miğfer” kelimesini görünce otomatik olarak 65.06’yı seçmektir.",
    "65.05 Açıklama Notu (7); 65.06 Açıklama Notu."))
# 10 D
S.append(soru(
    "Bir firma motosiklet sürücüleri için tasarlanmış şu ürünü ithal etmektedir: plastik dış kabuk, içte darbe emici koruyucu dolgu, kabuğa entegre mikrofon ve kulaklıklar. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
    "65.06", ["85.18", "39.26", "95.06", "65.07"], "D", SN,
    "65.06 Açıklama Notu, koruyucu dolgu malzemesiyle teçhiz edilmiş ve bazı hallerde mikrofonlu veya kulaklıklı olsun olmasın koruyucu başlıkları, bu arada motosikletçi miğferlerini kapsar. Mikrofon ve kulaklık başlığı 85.18’e götürmez; plastik olması Fasıl 39’u, korunma amacı Fasıl 95’i gündeme getirmez. 65.07 yalnız başlık bağlantı parçaları içindir.",
    "65.06 Açıklama Notu; 85.18 Açıklama Notu, hariç tutmalar."))
# 11 A
S.append(soru(
    "65.01 Açıklama Notuna göre şapka imalinde kullanılan keçe disklerin çapı ile keçe üstüvanelerin çevresi yaklaşık olarak hangisidir?",
    "Disk çapı 60 cm; üstüvane çevresi 100 cm",
    ["Disk çapı 100 cm; üstüvane çevresi 60 cm", "Disk çapı 40 cm; üstüvane çevresi 50 cm",
     "Disk çapı 50 cm; üstüvane çevresi 120 cm", "Disk çapı 60 cm; üstüvane çevresi 40 cm"], "A", TN,
    "Açıklama Notuna göre keçe diskler geniş yapılı koniler gerilerek yaklaşık 60 cm çapında disklere dönüştürülür. Üstüvanelerin çevresi 100 cm, yükseklikleri 40 ila 50 cm’dir. Sayıların yer değiştirildiği veya yükseklik değerinin çevre gibi verildiği seçenekler çeldiricidir.",
    "65.01 Açıklama Notu (B)."))
# 12 D
S.append(soru(
    "Aşağıdaki başlıklardan hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
    "Karnaval şapkası",
    ["Askerî çelik miğfer", "Bisikletçi kaskı", "İtfaiyeci miğferi", "Kulaklıklı pilot başlığı"], "D", FA,
    "Karnaval eşyası ve oyuncak şapkalar Fasıl 65 Not 1(c) gereği Fasıl 95’tedir. Askerî miğferler (Fasıl 93 dışı), spor kaskları (Fasıl 95 Not 1(g)), itfaiyeci miğferleri ve kulaklıklı pilot başlıkları koruyucu başlık olarak 65.06’dadır. Spor ve askerî amaç bu başlıkları Fasıl 95 veya 93’e götürmez.",
    "Fasıl 65 Not 1(c); 65.06 Açıklama Notu; Fasıl 95 Not 1(g)."))
# 13 E
S.append(soru(
    "Aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
    "Kürkten şapka – 65.06",
    ["Peruk – 65.05", "Balya halinde kullanılmış şapka – 65.06", "Atlar için başlık – 65.07", "Yünden örme eşarp – 65.05"], "E", ES,
    "Kürkten veya taklit kürkten şapkalar 65.06 Açıklama Notunda sayılmıştır. Peruklar 67.04’te, balyalı kullanılmış başlıklar 63.09’da, hayvan başlıkları 42.01’de, örme eşarplar 61.17’dedir. Başa giyilen her eşya Fasıl 65 eşyası değildir.",
    "65.06 Açıklama Notu; Fasıl 65 Not 1 ve Genel Açıklamalar, hariç tutmalar."))
# 14 C
S.append(soru(
    "Tarife Cetveline göre, tavşan tüyünden keçeleştirilmiş, konik biçimli, kalıplanarak şekil verilmemiş ve kenar yapılmamış şapka taslağı hangi pozisyonda sınıflandırılır?",
    "65.01", ["65.02", "56.02", "65.05", "65.06"], "C", EP,
    "65.01, kalıplanarak şekil verilmemiş veya kenar yapılmamış keçeden şapka taslaklarını kapsar; tavşan tüyü Açıklama Notunda en çok kullanılan maddeler arasında sayılmıştır. 65.02 şerit veya örgü taslaklar içindir. Keçe olması onu 56.02’ye götürmez; şekil verilip kenar yapılsaydı 65.05’e geçerdi.",
    "65.01 pozisyon metni ve Açıklama Notu."))
# 15 B
S.append(soru(
    "Aşağıdakilerden hangisi 65.05 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Yapma çiçeklerden yapılmış şapka",
    ["Aşçı başlığı", "Hemşire başlığı", "Silindir şapka", "Yağ emdirilmiş mensucattan geniş kenarlı gemici başlığı"], "B", OT,
    "65.05 Açıklama Notu, kuş tüylerinden veya yapma çiçeklerden şapkaları açıkça bu pozisyonun dışında bırakır; bunlar 65.06’dadır. Aşçı ve hemşire başlıkları, silindir şapkalar ve yağlı mensucattan gemici başlıkları 65.05’te sayılmıştır. Yapma çiçekle yalnızca süslenmiş şapka ise kendi pozisyonunda kalır.",
    "65.05 Açıklama Notu (1), (6), (8), (10); 65.06 Açıklama Notu."))
# 16 A
S.append(soru(
    "Aşağıdaki şapka taslaklarından hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
    "Kurdele geçirilerek donatılmış, şekil verilmemiş hasır şapka taslağı",
    ["Rafya şeritlerinden örülmüş, donatılmamış şapka taslağı",
     "Plastik şeritlerden örülmüş, astarsız ve donatılmamış şapka taslağı",
     "Ağartılmış ve boyanmış, şekil verilmemiş hasır şapka taslağı",
     "Kâğıt şeritlerin helezoni dikilmesiyle elde edilmiş, donatılmamış taslak"], "A", FA,
    "65.02 Açıklama Notuna göre şekil verilmemiş ve kenar yapılmamış taslakların kurdele, astar veya başka suretle donatılmış olanları 65.04’e geçer. Rafya ve plastik şeritlerden örülen, yalnızca ağartılıp boyanan veya şeritlerin helezoni basitçe dikilmesiyle elde edilen donatılmamış taslaklar 65.02’de kalır. Ağartma ve boyama sınıflandırmayı etkilemez.",
    "Fasıl 65 Not 2; 65.02 ve 65.04 Açıklama Notları."))
# 17 E
S.append(soru(
    "65.02 pozisyonundaki şapka taslaklarını 65.04 pozisyonundaki şekil verilmiş şapkalardan ayıran özellik Açıklama Notunda nasıl tarif edilmiştir?",
    "Henüz insan kafasına uygun oval bir şekil almamış olmaları",
    ["Yalnızca hasır veya rafya şeritlerinden yapılmış olmaları", "Kenar genişliklerinin 5 cm’yi geçmemesi ve astarsız olmaları",
     "Plaj veya kır şapkası olarak olduğu gibi kullanılamamaları", "Ağartılmamış, boyanmamış ve apre görmemiş olmaları"], "E", TN,
    "65.02 Açıklama Notu, bu taslakların 65.04’teki şekil verilmiş şapkalardan henüz insan kafasına uygun oval şekil almamış olmalarıyla ayırt edildiğini belirtir. Taslaklar plaj veya kır şapkası olarak olduğu gibi kullanılabilir; ağartma ve boyama sınıflandırmayı etkilemez. 5 cm ölçüsü şeritlerin genişliğiyle ilgilidir, kenarla değil.",
    "65.02 Açıklama Notu; 65.04 Açıklama Notu."))
# 18 B
S.append(soru(
    "Bir motosikletçi kaskının dış kabuğu, koruyucu iç dolgusu ve çene altı kayışı aynı ambalajda, birbirine takılmamış halde birlikte sunulmuştur. Bunların bütün halinde 65.06 pozisyonunda kask olarak sınıflandırılmasını sağlayan Genel Yorum Kuralı hangisidir?",
    "GYK 2(a)", ["GYK 2(b)", "GYK 3(b)", "GYK 3(c)", "GYK 5(b)"], "B", GY,
    "GYK 2(a), bir eşyaya yapılan atfın o eşyanın sökülmüş veya monte edilmemiş halde getirilenlerini de kapsadığını belirtir. Kaskın bütün parçaları birlikte sunulduğundan tamamlanmış kask gibi 65.06’da sınıflandırılır. 2(b) madde karışımları, 3(b) ve 3(c) birden fazla pozisyona girebilen eşya, 5(b) ambalaj malzemesi içindir.",
    "GYK 2(a); 65.06 Açıklama Notu."))
# 19 C
S.append(soru(
    "Tarife Cetveline göre, şapkaların iç tarafına takılmak üzere uzunluğuna kesilmiş ve birleştirmeye hazırlanmış deri iç şerit hangi pozisyonda sınıflandırılır?",
    "65.07", ["42.05", "65.06", "41.07", "65.04"], "C", EP,
    "65.07, başlıklara mahsus iç şeritleri kapsar; bunlar genellikle deriden olup uzunluğu boyunca kesilmiş veya başlıklar için birleştirilmeye hazırlanmışsa bu pozisyonda sınıflandırılır. Deriden olması onu 41.07 veya 42.05’e götürmez; 65.06 ve 65.04 bitmiş başlıklar içindir.",
    "65.07 Açıklama Notu (1)."))
# 20 D
S.append(soru(
    "Fasıl 65 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Fasıl, başlıkları kullanım amaçlarına (tiyatro, kılık değiştirme, korunma vb.) bakılmaksızın kapsar. II. Başlıklardaki süs ve teferruat 71. Fasılda yer alan maddelerden olabilir. III. Amyanttan başlıklar 65.06 pozisyonunda sınıflandırılır. IV. 65.02’deki taslaklar ağartma veya boyama işlemi görünce 65.04’e geçer.",
    "I ve II", ["I ve III", "II ve IV", "I, II ve III", "III ve IV"], "D", CC,
    "Genel Açıklamalar fasılın başlıkları kullanım amacına bakılmaksızın kapsadığını ve süslerin Fasıl 71 maddelerinden olabileceğini belirtir (I ve II doğru). Amyanttan başlıklar Not 1(b) gereği 68.12’dedir (III yanlış). Ağartma ve boyama 65.02’deki sınıflandırmayı etkilemez (IV yanlış).",
    "Fasıl 65 Not 1(b); Genel Açıklamalar; 65.02 Açıklama Notu."))
# 21 E
S.append(soru(
    "Aşağıdakilerden hangisi 65.07 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Şapka tepesinin iç kısmına tespit edilecek etiket",
    ["Kartondan şapka kasnağı", "Açılır kapanır şapkalar için yaylı tel çatı",
     "Şapkaya takılmaya hazır çene altı kayışı", "Mensucattan şapka astarı"], "E", OT,
    "65.07 Açıklama Notu, şapka tepelerinin iç kısmına tespit edilen etiketlerin bu pozisyona dahil olmadığını açıkça belirtir. Kartondan kasnaklar, açılır kapanır şapka çatıları, takılmaya hazır çene altı kayışları ve astarlar 65.07’de sayılmıştır.",
    "65.07 Açıklama Notu (2), (4), (5), (7)."))
# 22 A
S.append(soru(
    "Başa giyilen veya takılan aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
    "Yünden örme eşarp",
    ["Yünden örme bebek bonesi", "Keçe fes", "Kürk şapka", "İnsan saçından saç filesi"], "A", FA,
    "Şallar, eşarplar ve kaşkollar Fasıl 65 Genel Açıklamaları gereği fasıl dışıdır; örme olanlar 61.17’dedir. Örme bebek bonesi ve keçe fes 65.05’te, kürk şapka 65.06’da, insan saçından saç filesi 65.05’te yer alır. Başa örtülmesi eşarbı başlık yapmaz.",
    "Fasıl 65 Genel Açıklamalar, hariç tutmalar; 65.05 ve 65.06 Açıklama Notları."))
# 23 D
S.append(soru(
    "Bir şapkanın özellikleri şöyledir: hasır şeritlerden doğrudan örülmüş; jelatinle sertleştirilip kalıpta preslenerek baş çevresine uygun oval şekil verilmiş; kenarı biçimlendirilmiş; astarı yok; kenarına yapma çiçekler dikilerek süslenmiş. Tarife Cetveline göre bu şapka hangi pozisyonda sınıflandırılır?",
    "65.04", ["65.02", "65.06", "46.02", "67.02"], "D", SN,
    "Şerit veya örgüden yapılmış taslağa şekil verilip kenar yapıldığında eşya 65.04’e girer; astarsız olması bunu değiştirmez. 65.04 Açıklama Notu, yapma çiçek, yapraklı dal veya tüy gibi aksesuarla süslenmeyi bu pozisyonda sayar. Tamamı yapma çiçekten olsaydı 65.06’ya giderdi; şekil verildiği için 65.02’de kalamaz, Fasıl 46 ve 67.02 ise başlıkları kapsamaz.",
    "65.04 Açıklama Notu; 65.05 Açıklama Notu (1); Fasıl 67 hariç tutmaları."))
# 24 B
S.append(soru(
    "Tarife Cetveline göre şeritlerden örülmüş şapka taslakları, kalıplanarak şekil verilmemiş, kenarı yapılmamış, astarlanmamış ve donatılmamış ise ..... pozisyonunda; aynı taslak yalnızca kurdele ile donatılmış ise ..... pozisyonunda sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
    "65.02 – 65.04", ["65.01 – 65.05", "65.02 – 65.05", "65.04 – 65.02", "65.02 – 65.07"], "B", ES,
    "Şekil, kenar, astar ve donatım işlemi görmemiş örgü taslaklar 65.02’dedir. 65.02 Açıklama Notu, kurdele, astar veya başka suretle donatılmış taslakları açıkça 65.04’e gönderir. 65.01 keçe taslaklar, 65.05 mensucat ve keçe şapkalar, 65.07 bağlantı parçaları içindir.",
    "65.02 ve 65.04 pozisyon metinleri ve Açıklama Notları."))
# 25 C
S.append(soru(
    "65.06 Açıklama Notuna göre koruyucu başlıklarla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
    "Koruyucu dolgulu, mikrofonlu veya kulaklıklı olsalar bile 65.06’da kalırlar.",
    ["Kulaklıklı veya mikrofonlu olanlar cihaz sayılarak 85.18’de sınıflandırılır.",
     "Spor faaliyetlerinde kullanılanlar spor levazımatı olarak 95.06’dadır.",
     "Askerî miğferler silah aksesuarı sayılarak 93. Fasılda sınıflandırılır.",
     "Yalnızca metalden olanlar 65.06’da; plastikten olanlar Fasıl 39’dadır."], "C", TN,
    "65.06 Açıklama Notu, koruyucu dolgu malzemesiyle teçhiz edilmiş veya bazı hallerde mikrofonlu ya da kulaklıklı olsun olmasın spor, asker, itfaiyeci, motosikletçi, madenci ve inşaat işçisi miğferlerini kapsar. Kulaklıklı başlıklar 85.18’in, spor başlıkları Fasıl 95’in, çelik miğferler Fasıl 93’ün hariç tutmalarında Fasıl 65’e yönlendirilmiştir. Madde sınırlaması yoktur.",
    "65.06 Açıklama Notu; Fasıl 95 Not 1(g); Fasıl 93 Genel Açıklamalar."))

obj["sorular"] = S
yaz(obj)
