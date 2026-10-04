#!/usr/bin/env python3
"""Fasıl 66 modülü üreteci."""
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
    "fasil": 66,
    "baslik": "Şemsiyeler, güneş şemsiyeleri, bastonlar, iskemle bastonlar, kamçılar, kırbaçlar ve bunların aksamı",
    "bolum": "XII",
    "oz": {
        "vurgu": "Fasıl 66’nın üç pozisyonu da <b>maddeden bağımsızdır</b>: her türlü şemsiye 66.01, her türlü baston, kamçı ve kırbaç 66.02, bunların aksamı 66.03. Sınav sorusu çoğu zaman eşyanın gerçekten şemsiye veya baston olup olmadığını (silahlı, ölçülü, ortopedik, oyuncak, spor sopası) ve aksamın 66.03’ten dışlanıp dışlanmadığını sorar.",
        "maddeler": [
            "66.01: tören, çadır, bahçe, kafe, pazar şemsiyeleri; dışı baston görünüşlü kın içindeki “baston şemsiye” ve iskemleli baston şemsiye dahil.",
            "66.02: iskemle bastonlar, sakat ve yaşlılar için bastonlar, izci ve çoban sopaları, kırbaçlar (uçları dahil) ve kamçılar; işçilik görmüş baston taslakları dahil.",
            "66.03: kulp, kabza, çerçeve, mil, sürgü, yay, uç, oturma tablası gibi aksam (kıymetli metalden olsa bile); tekstil aksam ve her maddeden kın, kılıf, püskül hariç (Not 2).",
            "Fasıl dışı: ölçü gösteren baston (90.17), tüfekli, kılıçlı, kurşunlu baston (Fasıl 93), oyuncak şemsiye ve spor sopaları (Fasıl 95), koltuk değneği (90.21).",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı yeri verir.",
        "satirlar": [
            ["1", "Oyuncak veya karnaval şemsiyesi; golf, hokey, kayak sopası ya da dağcılık buz baltası mı?", "Fasıl 95"],
            ["2", "Ölçü gösteren baston veya ölçü çubuğu mu?", "<b>90.17</b>"],
            ["3", "Tüfekli, kılıçlı, kurşunlu baston vb. mi?", "Fasıl 93"],
            ["4", "Koltuk değneği veya ortopedik baston mu?", "<b>90.21</b>"],
            ["5", "Şemsiye veya güneş şemsiyesi mi (baston şemsiye, bahçe, çadır şemsiyesi dahil)?", "<b>66.01</b>"],
            ["6", "Baston, iskemle baston, sopa, kamçı, kırbaç; işçilik görmüş taslak veya bitmemiş baston mu?", "<b>66.02</b>"],
            ["7", "66.01 / 66.02 eşyasının aksamı mı (kulp, çerçeve, mil, uç, yay, oturma tablası)?*", "<b>66.03</b>"],
            ["8", "Kabaca yontulmuş ağaç veya bambu; belirli boyda kesilmiş çelik boru mu?", "<b>14.01</b> / Fasıl 44 · Fasıl 72 / 73"],
        ],
        "dipnot": "* Dokumaya elverişli maddeden aksam ile her maddeden kın, kılıf, püskül ve kordon 66.03’e girmez: eşyaya takılıysa onunla birlikte, takılı değilse (birlikte sunulsa bile) ayrı sınıflandırılır (Not 2).",
    },
    "pozisyon_haritasi": [
        ["66.01", "Şemsiyeler ve güneş şemsiyeleri",
         "Madde önemsiz; baston şemsiye, bahçe ve çadır şemsiyesi dahil",
         "Katlanır şemsiye, tören şemsiyesi, kafe şemsiyesi"],
        ["66.02", "Bastonlar, iskemle bastonlar, kamçılar, kırbaçlar",
         "Her maddeden; işçilik görmüş taslak ve bitmemiş baston dahil",
         "Yaşlı bastonu, izci sopası, çoban sopası, binici kamçısı"],
        ["66.03", "66.01 ve 66.02 eşyasının aksam, süs ve teferruatı",
         "Madde önemsiz; tekstil aksam, kın, kılıf, püskül hariç",
         "Şemsiye çerçevesi, kulp, mil, sürgü, baston ucu"],
    ],
    "notlar": [
        ["Fasıl 66 Not 1",
         "Fasıl dışı: (a) ölçü gösteren baston ve benzerleri (90.17); (b) tüfekli bastonlar, kılıçlı bastonlar, kurşunlu bastonlar ve benzerleri (Fasıl 93); (c) Fasıl 95’teki eşya (oyuncak şemsiyeler, oyuncak güneş şemsiyeleri gibi)."],
        ["Fasıl 66 Not 2",
         "66.03’e dokumaya elverişli maddelerden aksam, süs veya aksesuar ile herhangi bir maddeden kın, kılıf, püskül, şemsiye kılıfı ve benzerleri dahil değildir. Bunlar 66.01 veya 66.02 eşyasıyla birlikte sunulsalar dahi, eşyaya takılmamışlarsa onun parçası sayılmaz ve ayrı sınıflandırılır."],
        ["66.01 Açıklama Notu",
         "Bileşenlerinin (aksesuar ve süsler dahil) maddesine bakılmaksızın her nevi şemsiye: tören, çadır, baston ve iskemleli baston şemsiyeler; kahve, pazar, bahçe şemsiyeleri. Yüz mensucat, plastik, kâğıt olabilir; dantel, işleme, saçakla süslenebilir. Kulplar kıymetli metal, fildişi, boynuz, kemik, kehribar, sedef vb. olabilir ve kıymetli taşlarla birleşebilir."],
        ["66.01 Açıklama Notu (tanımlar)",
         "<b>Baston şemsiye:</b> dışı baston görünüşlü sert bir kın içine yerleştirilmiş şemsiye. <b>Çadır şemsiyesi:</b> kenarları tenteli, kazıklarla veya tente uçlarındaki kum cepleriyle toprağa tespit edilebilen büyük şemsiye."],
        ["66.01 Açıklama Notu (hariç)",
         "Şemsiyeye geçirilmemiş kılıflar (kendi pozisyonları); şemsiye veya çadır şemsiye niteliği taşımayan plaj çadırları ve kabinleri (63.06); oyuncak veya karnaval şemsiyeleri (Fasıl 95)."],
        ["66.02 Açıklama Notu",
         "Her nevi maddeden bastonlar; tutamağı açılıp oturak oluşturan iskemle bastonlar, sakat ve yaşlılar için düzenlenmiş bastonlar, izci ve çoban sopaları; kırbaçlar (kırbaç uçları dahil) ve ucunda kısa deri halkası olan saptan oluşan kamçılar. Tornalanmış, eğilmiş veya başka suretle işçilik görmüş ağaç/bambu baston taslakları dahildir; sadece kabaca yontulmuş veya yuvarlatılmış olanlar 14.01 veya Fasıl 44’te, bitmemiş sap olarak tanımlanabilen taslaklar 66.03’tedir."],
        ["66.02 Açıklama Notu (hariç)",
         "Ölçü çubukları ve ölçü gösteren bastonlar (90.17); destekler ve koltuk değnekleri (90.21); tüfekli, kılıçlı, kurşunlu bastonlar (Fasıl 93); golf, hokey, kayak değnek ve sopaları, alpin dağcılık buz baltaları (Fasıl 95)."],
        ["66.03 Açıklama Notu",
         "Maddesi ne olursa olsun (kıymetli metal, kıymetli taş dahil) aksam, süs ve teferruat: kulplar ve kabzalar (bitmemiş taslaklar dahil), şemsiye çerçeveleri (mile takılmış olanlar dahil), yivler ve gergiler, şemsiye sapları, kamçı ve kırbaç sapları, sürgüler, tel uçları, halkalar, yaylar, yüksükler, dil tertibatı, baston sivri uçları, iskemle baston oturma tablaları. Hariç: bitmemiş bastonlar (66.02); yiv ve gergi için belirli boylarda kesilmiş demir-çelik boru ve profiller (Fasıl 72 veya 73)."],
        ["90.21 Açıklama Notu",
         "Koltuk değnekleri ve ortopedik bastonlar 90.21’dedir; özel olarak sakatlar için yapılmış olsa da mutat bastonlar 66.02’de kalır."],
    ],
    "sinir_komsulari": [
        ["Ölçü gösteren baston, ölçü çubuğu", "90.17", "Not 1(a)"],
        ["Kılıçlı, tüfekli, kurşunlu baston", "Fasıl 93", "Not 1(b)"],
        ["Oyuncak veya karnaval şemsiyesi", "Fasıl 95", "Not 1(c)"],
        ["Golf, hokey, kayak sopası; dağcılık buz baltası", "Fasıl 95", "66.02 hariç tutması"],
        ["Koltuk değneği, ortopedik baston", "90.21", "Sakatlar için mutat baston ise 66.02"],
        ["Şemsiye niteliği olmayan plaj çadırı veya kabini", "63.06", "66.01 hariç tutması"],
        ["Çadır şemsiyesi", "66.01", "63.06 hariç tutması; şemsiyedir"],
        ["Şemsiyeye takılmamış kılıf, kın, püskül", "Kendi pozisyonları", "Not 2; birlikte sunulsa bile ayrı"],
        ["Sadece kabaca yontulmuş baston ağacı veya bambusu", "14.01 / Fasıl 44", "66.02 Açıklama Notu"],
        ["Şemsiye teli için belirli boyda kesilmiş çelik boru", "Fasıl 72 / 73", "66.03 hariç tutması"],
        ["Deriden binici kamçısı, kırbaç", "66.02", "Fasıl 42 Not 2; saraciye değil"],
        ["Gümüş veya altın şemsiye kulpu", "66.03", "Fasıl 71 Not 3; madde önemsiz"],
        ["Ahşap baston, ahşap şemsiye sapı", "66.02 / 66.03", "Fasıl 44 hariç tutması"],
    ],
    "tuzaklar": [
        "<b>Madde önemsizdir.</b> Altın kulplu baston, fildişi saplı şemsiye, gümüş şemsiye kulpu Fasıl 71’e değil Fasıl 66’ya girer; şemsiye ve baston maddesine göre sınıflandırılmaz.",
        "<b>Baston şemsiye bir şemsiyedir.</b> Baston görünüşlü kın içindeki şemsiye ve iskemleli baston şemsiye 66.01’dedir, 66.02’de değil.",
        "<b>Silahlı veya ölçülü baston baston değildir.</b> Kılıçlı, tüfekli, kurşunlu bastonlar Fasıl 93’te, ölçü gösteren bastonlar 90.17’dedir.",
        "<b>Sakatlar için baston ≠ ortopedik baston.</b> Yaşlı ve sakatlar için düzenlenmiş mutat bastonlar 66.02’de; koltuk değnekleri ve ortopedik bastonlar 90.21’dedir.",
        "<b>Takılmamış kılıf ayrı sınıflandırılır.</b> Not 2 gereği şemsiyeyle birlikte sunulsa bile takılmamış kılıf, kın, püskül ayrıdır; not aksini söylediği için burada GYK 5(a) uygulanmaz.",
        "<b>Tekstil aksam 66.03’e girmez.</b> Dokumaya elverişli maddeden şemsiye parçaları ve süsleri kendi pozisyonlarında; metal çerçeve, mil, kulp 66.03’tedir.",
        "<b>Baston taslağında işçilik derecesi önemlidir.</b> Tornalanmış veya eğilmiş taslak 66.02; sadece kabaca yontulmuş veya yuvarlatılmış ağaç/bambu 14.01 veya Fasıl 44; bitmemiş kulp taslağı 66.03.",
        "<b>Bitmemiş baston aksam değildir.</b> 66.03’ün hariç tutması gereği 66.02’de kalır.",
        "<b>Kamçı saraciye değildir.</b> Deriden olsa bile binici kamçısı ve kırbaç 66.02’dedir; Fasıl 42 bunları hariç tutar.",
        "<b>Spor sopası baston değildir.</b> Golf, hokey, kayak sopaları ve buz baltası Fasıl 95’te; buna karşılık bastonlar ve kırbaçlar Fasıl 95’e girmez.",
    ],
    "hafiza": {
        "kanca": "YAĞMUR – YAŞLI – YEDEK: 01 şemsiye · 02 baston-kırbaç · 03 yedek parça",
        "aciklama": "<b>Yağmur</b> yağar, şemsiye açılır (66.01); <b>yaşlı</b> bastonuyla, binici kamçısıyla yürür (66.02); kırılan tel, kulp, uç <b>yedek</b> parçadır (66.03). Üç pozisyonda da madde sorulmaz; sorulan tek şey eşyanın kılıç, ölçü, ortopedi, oyuncak veya spor sopası olup olmadığıdır.",
    },
    "sinav_odagi": [
        "Silahlı bastonlar: kılıçlı bastonun Fasıl 93’te yer aldığı; seçeneklerde 66, 90 ve 95. fasılların çeldirici olarak kullanılması.",
        "“Hangisi farklı pozisyondadır?” kalıbında şemsiyenin (66.01) baston, iskemle baston, kamçı ve kırbaçtan (66.02) ayrılması.",
        "Pozisyon sırası soruları: şemsiye (66.01) ve bastonun (66.02) miğfer (65.06) ve perukla (67.04) karşılaştırılması.",
        "“Hangisi mamul olduğu maddeye göre sınıflandırılır?” kalıbında şemsiye ve bastonun maddeden bağımsız sınıflandırıldığı; tabak gibi eşyanın ise maddesine göre ayrıldığı.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Kılıçlı baston isimli eşya Türk Gümrük Tarife Cetvelinin hangi fasılında yer almaktadır?",
            "secenekler": ["66", "93", "95", "90"],
            "cevap": "B",
            "aciklama": "Fasıl 66 Not 1(b) gereği tüfekli, kılıçlı, kurşunlu bastonlar ve benzerleri Fasıl 66 dışındadır ve Fasıl 93’te yer alır. Ölçü gösteren bastonlar 90.17’de, oyuncak şemsiyeler Fasıl 95’tedir.",
        },
        {
            "soru": "Aşağıdakilerden hangisi Türk Gümrük Tarife Cetvelinde diğerlerinden farklı bir tarife pozisyonunda yer alır?",
            "secenekler": ["Baston", "Kamçı", "Şemsiye", "Kırbaç", "İskemle baston"],
            "cevap": "C",
            "aciklama": "Şemsiyeler 66.01’de; bastonlar, iskemle bastonlar, kamçılar ve kırbaçlar ise 66.02’de sınıflandırılır.",
        },
    ],
    "ozet": [
        "Fasıl 66’da üç pozisyon vardır ve üçünde de madde önemsizdir.",
        "Her türlü şemsiye (baston şemsiye, iskemleli baston şemsiye, bahçe, kafe, çadır şemsiyesi) 66.01.",
        "Baston, iskemle baston, izci ve çoban sopası, kamçı, kırbaç (ucu dahil) 66.02; işçilik görmüş taslak ve bitmemiş baston da burada.",
        "Aksam, süs ve teferruat 66.03; tekstil aksam ile her maddeden kın, kılıf, püskül hariç, takılmamışsa ayrı sınıflandırılır.",
        "Fasıl dışı: ölçü bastonu 90.17, silahlı baston Fasıl 93, oyuncak şemsiye ve spor sopaları Fasıl 95, koltuk değneği 90.21, plaj kabini 63.06.",
    ],
}

S = []
# 1 D
S.append(soru(
    "Tarife Cetveline göre, kafe ve pazar yerlerinde kullanılan, masaya veya zemine takılarak sabitlenen büyük güneş şemsiyesi hangi pozisyonda sınıflandırılır?",
    "66.01", ["63.06", "66.03", "94.03", "95.06"], "D", EP,
    "66.01, bileşenlerinin maddesine bakılmaksızın her nevi şemsiye ve güneş şemsiyesini kapsar; kahve, pazar ve bahçe şemsiyeleri Açıklama Notunda açıkça sayılmıştır. Şemsiye niteliği taşımayan plaj çadırları 63.06’dadır. Büyük ve sabitlenebilir olması onu mobilya veya aksam yapmaz.",
    "66.01 pozisyon metni ve Açıklama Notu."))
# 2 B
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinin 66. faslında <b>sınıflandırılmaz</b>?",
    "Ölçü gösteren baston",
    ["Baston şemsiye", "Çobanların kullandığı sopa", "İzci sopası", "Deriden kırbaç ucu"], "B", OT,
    "Fasıl 66 Not 1(a) gereği ölçü gösteren bastonlar ve benzerleri 90.17’dedir. Baston şemsiyeler 66.01’de; çoban ve izci sopaları ile kırbaçlar (kırbaç uçları dahil) 66.02’de sınıflandırılır. Bastonun üzerindeki ölçü bölmeleri onu ölçü aleti yapar.",
    "Fasıl 66 Not 1(a); 66.01 ve 66.02 Açıklama Notları."))
# 3 A
S.append(soru(
    "Fasıl 66 Açıklama Notlarına göre “baston şemsiye” tabirinden ne anlaşılır?",
    "Dışı baston görünüşlü sert bir kın içine yerleştirilmiş şemsiye",
    ["Sapı normal şemsiyelerden daha uzun olan her türlü şemsiye",
     "Tutamak kısmı açılarak oturma yeri oluşturan baston",
     "Kenarları tenteli, kazıkla zemine tespit edilen şemsiye",
     "Bastona sonradan takılan ve ayrı sunulan şemsiye yüzü"], "A", TN,
    "66.01 Açıklama Notu baston şemsiyeyi, dışı baston görünüşlü sert bir kın içine yerleştirilmiş şemsiye olarak tanımlar; bu eşya 66.01’dedir. Tutamağı açılıp oturak oluşturan eşya iskemle bastondur (66.02), kenarları tenteli ve kazıkla tespit edilen ise çadır şemsiyesidir. Sap uzunluğu bir ölçüt değildir.",
    "66.01 Açıklama Notu; 66.02 Açıklama Notu (A)."))
# 4 E
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
    "Tüfekli baston",
    ["İskemle baston", "Fildişi kulplu baston", "Çoban sopası", "Kırbaç"], "E", FA,
    "Tüfekli, kılıçlı ve kurşunlu bastonlar Fasıl 66 Not 1(b) gereği Fasıl 93’tedir. İskemle bastonlar, kulpu fildişinden olan bastonlar, çoban sopaları ve kırbaçlar 66.02’de yer alır; kulpun maddesi sınıflandırmayı değiştirmez.",
    "Fasıl 66 Not 1(b); 66.02 Açıklama Notu."))
# 5 C
S.append(soru(
    "Tarife Cetveline göre, şemsiyeler için mile monte edilmiş halde bir araya getirilmiş metal tel çerçeve (iskelet), yüzü takılmamış olarak sunulduğunda hangi pozisyonda sınıflandırılır?",
    "66.03", ["73.26", "66.01", "72.17", "83.02"], "C", EP,
    "66.03 Açıklama Notu, şemsiye saplarına takılmış olanlar dahil şemsiye çerçevelerini ve bunların yiv ve gergilerini açıkça sayar. Yüzü olmayan çerçeve henüz şemsiye niteliği kazanmadığından 66.01’e girmez. Metalden olması Fasıl 72, 73 veya 83’ü gündeme getirmez; yalnızca belirli boylarda kesilmiş boru ve profiller Fasıl 72 veya 73’tedir.",
    "66.03 Açıklama Notu."))
# 6 A
S.append(soru(
    "Perakende satış için aynı kutuda, şemsiyeye geçirilmemiş kumaş kılıfıyla birlikte sunulan katlanır şemsiyede kılıfın şemsiyeden ayrı sınıflandırılmasının dayanağı aşağıdakilerden hangisidir?",
    "GYK 1 ve Fasıl 66 Not 2",
    ["GYK 5(a) (mahfaza kuralı)", "GYK 3(b) (takım kuralı)", "GYK 2(a) (eksik eşya)", "GYK 3(c) (son pozisyon)"], "A", GY,
    "Fasıl 66 Not 2, kılıfların 66.01 eşyasıyla birlikte sunulsalar dahi şemsiyeye takılmamışlarsa onun parçası sayılmayacağını ve ayrı sınıflandırılacağını hükme bağlar. Notlar GYK 1 kapsamında uygulanır; GYK 2 ila 5 ancak pozisyon metinleri ve notlar aksini gerektirmediğinde devreye girer. Bu nedenle mahfazaları eşyayla birlikte sınıflandıran GYK 5(a) ve takım kuralı 3(b) burada uygulanmaz.",
    "GYK 1; Fasıl 66 Not 2; 66.01 Açıklama Notu, hariç tutmalar."))
# 7 D
S.append(soru(
    "Aşağıdakilerden hangileri 66.03 pozisyonunda sınıflandırılır? I. Kıymetli metalden şemsiye kulpu II. Şemsiyeye takılmamış dokuma püskül III. İskemle bastonlara mahsus oturma tablası IV. Bitmemiş baston",
    "I ve III", ["I ve II", "II ve IV", "I, III ve IV", "II, III ve IV"], "D", CC,
    "66.03 aksamı maddesine bakılmaksızın kapsar; kıymetli metalden kulplar ve iskemle baston oturma tablaları bu pozisyondadır (I ve III). Dokumaya elverişli maddeden süsler ve her maddeden püsküller Not 2 gereği 66.03’e girmez (II). Bitmemiş bastonlar 66.03’ün hariç tutması gereği 66.02’dedir (IV).",
    "Fasıl 66 Not 2; 66.03 Açıklama Notu."))
# 8 B
S.append(soru(
    "Tarife Cetveline göre, tutamak kısmı açılarak oturma yeri oluşturan, yaşlılar için alüminyumdan yapılmış iskemle baston hangi pozisyonda sınıflandırılır?",
    "66.02", ["66.01", "90.21", "94.01", "76.16"], "B", EP,
    "66.02 Açıklama Notu, tutamak kısımları oturacak yer oluşturacak şekilde açılır kapanır yapılmış iskemle bastonları ve yaşlılar için düzenlenmiş bastonları kapsar; madde önemsizdir. Oturak oluşturması onu 94.01’e, yaşlılara yönelik olması 90.21’e götürmez; şemsiyesi olsaydı iskemleli baston şemsiye olarak 66.01’de olurdu.",
    "66.02 Açıklama Notu (A); 90.21 Açıklama Notu."))
# 9 E
S.append(soru(
    "Aşağıdakilerden hangisi 66.03 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Birlikte sunulan, şemsiyeye takılmamış kumaş kılıf",
    ["Şemsiyelere mahsus açıp kapama sürgüsü", "Baston ucuna takılan metal yüksük",
     "İskemle bastona mahsus oturma tablası", "Kamçı ve kırbaçlar için sap"], "E", OT,
    "Not 2 gereği her maddeden kılıflar 66.03’e girmez; şemsiyeyle birlikte sunulsa bile takılmamışsa ayrı sınıflandırılır. Açıp kapama sürgüleri, baston uçlarına takılan yüksükler, iskemle baston oturma tablaları ve kamçı sapları 66.03 Açıklama Notunda sayılan aksamdır.",
    "Fasıl 66 Not 2; 66.03 Açıklama Notu."))
# 10 C
S.append(soru(
    "Bir ithalatçı şu ürünü getirmiştir: dışarıdan bakıldığında baston görünümünde sert bir kın; kın açıldığında içinden metal çerçeveli, kumaş yüzlü bir şemsiye çıkmaktadır; kulp kısmı gümüş kaplamalı metaldendir. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
    "66.01", ["66.02", "66.03", "71.14", "93.07"], "C", SN,
    "Dışı baston görünüşlü sert bir kın içine yerleştirilmiş şemsiye “baston şemsiye”dir ve 66.01 Açıklama Notunda açıkça sayılmıştır. Baston görünümü onu 66.02’ye, gümüş kaplama kulp ise Fasıl 71’e götürmez; şemsiyeler bileşenlerinin maddesine bakılmaksızın sınıflandırılır. Kın içinde silah değil şemsiye bulunduğundan Fasıl 93 söz konusu değildir.",
    "66.01 Açıklama Notu; Fasıl 71 Not 3(ij)."))
# 11 C
S.append(soru(
    "Fasıl 66 Not 2 ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
    "Her maddeden kın ve kılıflar, şemsiyeyle birlikte sunulsa da takılmamışsa ayrı sınıflandırılır.",
    ["Şemsiyeyle birlikte sunulan kılıflar her durumda şemsiyeyle birlikte 66.01’de sınıflandırılır.",
     "Dokumaya elverişli maddeden aksam ve süsler 66.03’te sınıflandırılır.",
     "Kılıflar yalnızca deriden olduklarında 66.03’te sınıflandırılır.",
     "Kıymetli metalden yapılmış püsküller 66.03’te sınıflandırılır."], "C", TN,
    "Not 2, dokumaya elverişli maddeden aksam, süs ve aksesuarı ile herhangi bir maddeden kın, kılıf, püskül ve benzerlerini 66.03’ün dışında bırakır; bunlar eşyaya takılmamışsa birlikte sunulsalar dahi ayrı sınıflandırılır. Püskül ve kılıf için madde ayrımı yapılmaz; kıymetli metal istisnası yalnız kulp, çerçeve gibi aksam için geçerlidir.",
    "Fasıl 66 Not 2; 66.03 Açıklama Notu."))
# 12 E
S.append(soru(
    "Aşağıdaki eşyadan hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
    "Baston şemsiye",
    ["İskemle baston", "İzci sopası", "Binici kamçısı", "Tornalanmış ağaçtan baston taslağı"], "E", FA,
    "Baston şemsiye, dışı baston görünüşlü kın içindeki bir şemsiyedir ve 66.01’dedir. İskemle bastonlar, izci sopaları, kamçılar ve tornalanmış ağaçtan baston taslakları 66.02’de sınıflandırılır. Adındaki “baston” kelimesi tuzaktır.",
    "66.01 ve 66.02 Açıklama Notları."))
# 13 A
S.append(soru(
    "Aşağıdaki eşya – yer eşleştirmelerinden hangisi <b>yanlıştır</b>?",
    "Koltuk değneği – 66.02",
    ["Ölçü gösteren baston – 90.17", "Kurşunlu baston – Fasıl 93", "Oyuncak şemsiye – Fasıl 95",
     "Şemsiye niteliği taşımayan plaj kabini – 63.06"], "A", ES,
    "Destekler ve koltuk değnekleri 66.02 Açıklama Notunun hariç tutmalarında sayılmış olup 90.21’dedir. Ölçü gösteren baston 90.17, kurşunlu baston Fasıl 93, oyuncak şemsiye Fasıl 95 ve plaj kabini 63.06 ile doğru eşleştirilmiştir. Sakatlar için yapılmış mutat bastonların 66.02’de kalması koltuk değneğiyle karıştırılmamalıdır.",
    "Fasıl 66 Not 1; 66.01 ve 66.02 Açıklama Notları, hariç tutmalar."))
# 14 D
S.append(soru(
    "Tarife Cetveline göre, ucunda kısa deri halka bulunan bir saptan oluşan, deriyle kaplanmış binici kamçısı hangi pozisyonda sınıflandırılır?",
    "66.02", ["42.01", "66.03", "95.06", "42.05"], "D", EP,
    "66.02 kamçıları ve kırbaçları her nevi maddeden kapsar; kamçı Açıklama Notunda ucunda kısa deri halkaları olan sap olarak tarif edilmiştir. Fasıl 42 kamçı ve binici kırbaçlarını açıkça hariç tutar; bu nedenle saraciye (42.01) veya deriden diğer eşya (42.05) değildir. Tam bir kamçı olduğundan 66.03’e de girmez.",
    "66.02 Açıklama Notu (B); Fasıl 42 Not 2."))
# 15 B
S.append(soru(
    "Aşağıdakilerden hangisi 66.02 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Yalnızca kabaca yontulmuş, baston imaline elverişli bambu",
    ["Tornalanmış ve eğilmiş ağaçtan baston taslağı", "Sakat kişiler için düzenlenmiş mutat baston",
     "Gümüş kulplu baston", "Deri kaplı saplı kırbaç"], "B", OT,
    "66.02 Açıklama Notuna göre baston imaline elverişli ağaç veya bambuların sadece kabaca yontulmuş veya yuvarlak hale getirilmiş olanları bu pozisyon dışındadır (14.01 veya Fasıl 44). Tornalanmış, eğilmiş taslaklar, sakatlar için mutat bastonlar, kulpu kıymetli metalden bastonlar ve kırbaçlar 66.02’dedir.",
    "66.02 Açıklama Notu (A) ve (B); 90.21 Açıklama Notu."))
# 16 B
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
    "Bitmemiş baston",
    ["Şemsiye teli için gergi", "Bitmemiş şemsiye kulpu taslağı", "Baston için sivri uçlu demir", "Şemsiye mili (sapı)"], "B", FA,
    "66.03 Açıklama Notu bitmemiş bastonları hariç tutar ve 66.02 Açıklama Notuna gönderir; bunlar 66.02’dedir. Gergiler, bitmemiş eşya olarak tanımlanabilen kulp taslakları, baston sivri uçları ve şemsiye milleri 66.03’te sayılan aksamdır.",
    "66.03 Açıklama Notu, hariç tutmalar; 66.02 Açıklama Notu."))
# 17 A
S.append(soru(
    "66.01 Açıklama Notuna göre “çadır şemsiyeleri” nasıl tanımlanmıştır?",
    "Kenarları tenteli, kazık veya kum cepleriyle toprağa tespit edilen büyük şemsiyeler",
    ["Şemsiye niteliği taşımayan, kumsalda kurulan plaj çadırları ve kabinleri",
     "Dışı baston görünüşlü sert bir kın içinde taşınan şemsiyeler",
     "Yalnızca yüzü çadır bezinden yapılmış, elde taşınan şemsiyeler",
     "Kamp çadırlarının üzerine geçirilen, kenarları tenteli yağmurluklar"], "A", TN,
    "Açıklama Notu çadır şemsiyelerini kenarları tenteli, alelade çadırlar gibi kazıklarla veya tente uçlarındaki kum cepleri aracılığıyla toprağa tespit edilebilen büyük şemsiyeler olarak tanımlar; bunlar 66.01’dedir. Şemsiye niteliği taşımayan plaj kabinleri 63.06’dadır; baston görünüşlü kın tarifi baston şemsiyeye aittir.",
    "66.01 Açıklama Notu; 63.06 Açıklama Notu, hariç tutmalar."))
# 18 E
S.append(soru(
    "Mili, metal çerçevesi ve kumaş yüzü takılmış, yalnızca kulpu (tutamağı) henüz takılmamış halde sunulan bir şemsiyenin aksam olarak 66.03’te değil şemsiye olarak 66.01’de sınıflandırılmasını sağlayan Genel Yorum Kuralı hangisidir?",
    "GYK 2(a)", ["GYK 2(b)", "GYK 3(a)", "GYK 4", "GYK 5(a)"], "E", GY,
    "GYK 2(a)’ya göre bir eşyaya yapılan atıf, gümrüğe sunulduğunda tamamlanmış eşyanın ayırt edici niteliğini taşıması şartıyla aksamı tamamlanmamış halini de kapsar. Mili, çerçevesi ve yüzü olan şemsiye bu niteliği taşır; eksik kulp onu aksam yapmaz. 2(b) madde karışımları, 3(a) en özel tanım, 4 benzerlik, 5(a) mahfazalar içindir.",
    "GYK 2(a); 66.01 ve 66.03 Açıklama Notları."))
# 19 C
S.append(soru(
    "Tarife Cetveline göre, gümüşten yapılmış ve kıymetli taşlarla süslenmiş, ayrı olarak sunulan şemsiye kulpu hangi pozisyonda sınıflandırılır?",
    "66.03", ["71.13", "71.14", "66.01", "71.16"], "C", EP,
    "66.03 Açıklama Notu, aksam, süs ve teferruatın kıymetli metal veya kıymetli taş da dahil maddesi ne olursa olsun bu pozisyonda sınıflandırılacağını belirtir; kulplar ilk sırada sayılmıştır. Fasıl 71 Not 3 de Fasıl 66 eşyasını kapsam dışında bırakır. Tek başına kulp şemsiye olmadığından 66.01’e girmez.",
    "66.03 Açıklama Notu; Fasıl 71 Not 3(ij)."))
# 20 D
S.append(soru(
    "Fasıl 66 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Şemsiyeler, bileşenlerinin yapıldığı maddeler dikkate alınmaksızın 66.01’de sınıflandırılır. II. Şemsiye yüzleri kâğıttan olabilir. III. Golf sopaları 66.02’de sınıflandırılır. IV. Kırbaç uçları 66.02’de sınıflandırılır.",
    "I, II ve IV", ["I ve III", "II ve III", "I, III ve IV", "III ve IV"], "D", CC,
    "66.01 Açıklama Notu şemsiyeleri bileşenlerinin maddesine bakılmaksızın kapsar ve yüzlerin mensucat, plastik veya kâğıttan olabileceğini belirtir (I ve II doğru). 66.02 kırbaçları kırbaç uçları dahil kapsar (IV doğru). Golf sopaları Fasıl 95 eşyası olarak 66.02’nin hariç tutmalarındadır (III yanlış).",
    "66.01 ve 66.02 Açıklama Notları."))
# 21 E
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinin 66. faslında <b>yer almaz</b>?",
    "Şemsiye niteliği taşımayan plaj çadırı (plaj kabini)",
    ["Resmî törenlerde kullanılan tören şemsiyesi", "Kenarları dantelle süslenmiş güneş şemsiyesi", "Yüzü kâğıttan yapılmış güneş şemsiyesi",
     "Tutamağı oturak olan iskemleli baston şemsiye"], "E", OT,
    "66.01 Açıklama Notu, şemsiye veya çadır şemsiye mahiyetini haiz olmayan plaj çadırlarını ve plaj kabinlerini hariç tutar; bunlar 63.06’dadır. Tören şemsiyeleri, dantel süslü veya kâğıt yüzlü güneş şemsiyeleri ve iskemleli baston şemsiyeler 66.01’de açıkça sayılmıştır.",
    "66.01 Açıklama Notu, hariç tutmalar."))
# 22 C
S.append(soru(
    "Spor veya oyunla ilgili görünen aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
    "Çoban sopası",
    ["Golf sopası", "Hokey sopası", "Alpin dağcılığında kullanılan buz baltası", "Oyuncak şemsiye"], "C", FA,
    "Çoban sopaları 66.02 Açıklama Notunda bastonlarla birlikte sayılmıştır ve Fasıl 66’dadır. Golf ve hokey sopaları ile buz baltaları 66.02’nin hariç tutmalarında, oyuncak şemsiyeler Fasıl 66 Not 1(c)’de Fasıl 95’e gönderilmiştir.",
    "66.02 Açıklama Notu; Fasıl 66 Not 1(c)."))
# 23 B
S.append(soru(
    "Bir firma şu ürünü ithal etmektedir: ahşap gövdeli, alt ucunda metal sivri uç bulunan, üst kısmında tutamak olan bir yürüyüş bastonu; gövdesi boyunca santimetre bölmeleri işlenmiş olup arazide derinlik ve yükseklik ölçmek için de kullanılmaktadır. Tarife Cetveline göre bu ürün hangi pozisyonda sınıflandırılır?",
    "90.17", ["66.02", "66.03", "44.21", "95.06"], "B", SN,
    "Fasıl 66 Not 1(a) ve 66.02 Açıklama Notu, ölçü gösteren bastonları ve benzerlerini Fasıl 66 dışında bırakarak 90.17’ye gönderir. Görünüşü yürüyüş bastonu olsa da ölçü bölmeleri eşyayı ölçü aleti yapar. Ahşaptan olması 44.21’i, arazide kullanılması Fasıl 95’i gündeme getirmez.",
    "Fasıl 66 Not 1(a); 66.02 Açıklama Notu, hariç tutmalar."))
# 24 D
S.append(soru(
    "Tarife Cetveline göre şemsiye çerçeveleri ..... pozisyonunda; yivler ve gergiler için basit şekilde belirli boylarda kesilmiş demir veya çelikten borular ve profiller ise ..... sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
    "66.03 – Fasıl 72 veya 73’te",
    ["66.01 – Fasıl 72 veya 73’te", "66.03 – Fasıl 76 veya 83’te", "66.02 – Fasıl 82 veya 83’te", "66.03 – 66.01’de"], "D", ES,
    "66.03 Açıklama Notu şemsiye çerçevelerini (mile takılmış olanlar dahil) aksam olarak sayar. Aynı not, yiv ve gergiler için yalnızca belirli boylarda kesilmiş demir ve çelik boru ve profilleri hariç tutarak Fasıl 72 veya 73’e gönderir. Bu basit işlem görmüş malzeme henüz şemsiye aksamı niteliği kazanmamıştır.",
    "66.03 Açıklama Notu, hariç tutmalar."))
# 25 A
S.append(soru(
    "66.02 Açıklama Notuna göre “iskemle bastonlar” nasıl tarif edilmiştir?",
    "Tutamağı açılıp kapanarak oturacak yer oluşturan bastonlar",
    ["Bir iskemleye ayak olarak takılmak üzere yapılmış baston biçimli parçalar",
     "Bir şemsiye ile birleştirilmiş ve oturma yeri bulunan bastonlar",
     "Koltuk değneği olarak kullanılan, koltuk altı destekli bastonlar",
     "Ucunda kısa deri halkaları bulunan, binicilikte kullanılan saplar"], "A", TN,
    "66.02 Açıklama Notu iskemle bastonları, tutamak kısımları oturacak bir yer teşkil edecek şekilde açılır kapanır tarzda yapılmış bastonlar olarak tanımlar. Şemsiyeyle birleşmiş olanlar iskemleli baston şemsiye olarak 66.01’de, koltuk değnekleri 90.21’dedir. Ucunda kısa deri halka bulunan sap ise kamçının tarifidir.",
    "66.02 Açıklama Notu (A) ve (B); 66.01 Açıklama Notu."))

obj["sorular"] = S
yaz(obj)
