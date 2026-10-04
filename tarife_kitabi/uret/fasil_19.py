import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_19_23 import S, kaydet  # noqa: E402

obj = {
    "tur": "fasil",
    "fasil": 19,
    "baslik": "Hububat, un, nişasta veya süt müstahzarları; pastacılık ürünleri",
    "bolum": "IV",
    "oz": {
        "vurgu": "Fasıl 19, esası hububat, un, nişasta, malt hülasası veya süt (04.01–04.04) olan gıda müstahzarlarını ve bütün ekmekçilik ürünlerini toplar. Üç ölçüt belirleyicidir: et, balık vb. oranı (%20), kakao oranı (19.01’de %40 / %5, 19.04’te %6) ve ürünün Fasıl 10–11’in ötesinde hazırlanıp hazırlanmadığı.",
        "maddeler": [
            "19.01 tamamlayıcı pozisyondur: malt hülasası ile başka yerde yer almayan un, kaba un, nişasta, malt hülasası veya süt esaslı müstahzarlar (bebek maması, hamur ve kek karışımı, pişirilmemiş pizza).",
            "Makarna pişmiş, doldurulmuş veya başka şekilde hazırlanmış olsa da, kuskus hazırlanmış olsun olmasın 19.02’dedir; doldurulmuş makarnada %20 kuralı işlemez.",
            "Tapyoka 19.03; kabartılmış veya kavrulmuş hububat, müsli, bulgur ve ön pişirilmiş dane hububat (mısır hariç) 19.04.",
            "Ekmek, bisküvi, kek, gofret, ön pişmiş veya pişmiş pizza ile hosti, boş ilaç kapsülü, mühür güllacı ve pirinç kâğıdı 19.05; kakao oranı önemsizdir."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Ağırlıkça %20’den fazla sosis, et, sakatat, kan, böcek, balık veya su omurgasızı içeriyor mu? (doldurulmuş makarna hariç)", "<b>Fasıl 16</b>"],
            ["2", "Hayvan beslenmesi için özel olarak hazırlanmış mı? (köpek bisküvisi)", "<b>23.09</b>"],
            ["3", "Makarna veya kuskus mu? (pişmiş, doldurulmuş, dondurulmuş, hazır öğün)", "<b>19.02</b>"],
            ["4", "Ön pişirilmiş veya pişirilmiş ekmekçilik ürünü mü? (ekmek, bisküvi, kek, gofret, pizza, hosti, pirinç kâğıdı)", "<b>19.05</b> (kakao oranı önemsiz)"],
            ["5", "Nişastadan flokon, dane, inci şeklinde tapyoka veya benzeri mi?", "<b>19.03</b>"],
            ["6", "Kabartılmış/kavrulmuş hububat, müsli, bulgur veya ön pişirilmiş dane hububat (mısır hariç) mı?", "<b>19.04</b> · kakao %6’yı aşar veya tamamen çikolata kaplıysa <b>18.06</b>"],
            ["7", "Esası un, kaba un, nişasta veya malt hülasası olan müstahzar mı?", "Kakao %40’tan az: <b>19.01</b> · %40 ve fazla: <b>18.06</b>*"],
            ["8", "Esası 04.01–04.04 maddeleri (süt ürünleri) olan müstahzar mı?", "Kakao %5’ten az: <b>19.01</b> · %5 ve fazla: <b>18.06</b>*"]
        ],
        "dipnot": "* Kakao oranları yağı tamamen alınmış baz üzerinden ağırlıkça hesaplanır; kakao miktarı normal olarak birleşik teobromin ve kafein miktarının 31 ile çarpılmasıyla bulunur. Şekerleme karakteri kazanmış ürünler 17.04’e gider."
    },
    "pozisyon_haritasi": [
        ["19.01", "Malt hülasası; un, nişasta, malt veya süt esaslı müstahzarlar (başka yerde yer almayan)", "Kakao: un esaslıda %40’tan az, süt esaslıda %5’ten az", "Bebek maması, kek ve hamur karışımı, pişmemiş pizza, süt esaslı dondurma tozu"],
        ["19.02", "Makarnalar; kuskus", "Fermente edilmemiş hamur; pişmiş, doldurulmuş, hazırlanmış olabilir", "Spagetti, şehriye, ravioli, lazanya, taze gnocchi, kuskus"],
        ["19.03", "Tapyoka ve nişastadan tapyoka benzerleri", "Flokon, dane, inci, kalbur içi şekli", "Manyok tapyokası, sagu, patates tapyokası"],
        ["19.04", "Kabartılmış/kavrulmuş hububat; müsli; bulgur; ön pişmiş dane hububat", "Fasıl 10–11’in ötesinde işlem; kakao en çok %6", "Mısır gevreği, patlamış pirinç, müsli, bulgur, ön pişirilmiş pirinç"],
        ["19.05", "Ekmek, pasta, kek, bisküvi; hosti, boş kapsül, mühür güllacı, pirinç kâğıdı", "Ekmekçilik ürünü; kakao oranı önemsiz", "Gevrek ekmek, gofret, kraker, pişmiş pizza, quiche, beze, krep"]
    ],
    "notlar": [
        ["Fasıl 19 Not 1", "Fasıl 19 dışı: (a) ağırlıkça %20’den fazla sosis, et, sakatat, kan, böcek, balık, kabuklu hayvan, yumuşakça veya diğer su omurgasızı ya da bunların karışımını içeren gıda müstahzarları → Fasıl 16 (<b>19.02’deki doldurulmuş mamuller hariç</b>); (b) hayvan beslenmesi için özel şekilde hazırlanmış un veya nişastadan bisküvi ve diğer ürünler → 23.09; (c) Fasıl 30’daki ilaçlar ve diğer ürünler."],
        ["Fasıl 19 Not 2", "19.01 anlamında “kabaca öğütülerek elde edilen küçük parçalar” Fasıl 11’deki hububat parçalarıdır. “Un ve kaba un”: (1) Fasıl 11’deki hububat unları ve kaba unları; (2) herhangi bir fasılda yer alan bitkisel menşeli un, ezme ve tozlar (ör. soya fasulyesi unu). <b>Hariç:</b> kurutulmuş sebze (07.12), patates (11.05) ve kuru baklagil (11.06) unları, kaba unları ve tozları."],
        ["Fasıl 19 Not 3", "19.04; yağı tamamen alınmış baz üzerinden ağırlıkça <b>%6’dan fazla</b> kakao içeren veya <b>tamamen çikolata ile kaplanmış</b> müstahzarları ve 18.06’daki kakao içeren diğer gıda müstahzarlarını kapsamaz → 18.06."],
        ["Fasıl 19 Not 4", "19.04 anlamında “başka şekilde hazırlanmış”: Fasıl 10 ve 11’in notlarında veya pozisyonlarında belirtilenlerden daha ileri bir işleme tabi tutulmuş hububat."],
        ["Genel Açıklamalar", "Kakao miktarı normal olarak birleşik teobromin ve kafein miktarının <b>31</b> faktörü ile çarpılmasıyla hesaplanır; “kakao” hamur ve katı haller dahil bütün halleri kapsar."],
        ["Genel Açıklamalar", "18.06’ya giden eşikler: un, kaba un, nişasta veya malt hülasası esaslıda <b>%40 ve fazlası</b>; 04.01–04.04 maddeleri esaslıda <b>%5 ve fazlası</b> kakao. Kahve içeren kahve yerine geçen kavrulmuş maddeler 09.01, kavrulmuş arpa gibi diğerleri 21.01; esası un, nişasta, malt hülasası veya süt olmayan krema, dondurma, tatlı tozları genellikle 21.06."],
        ["19.01 Açıklama Notu", "Malt hülasası külçe, toz veya kıvamlı sıvı olabilir; lesitin, vitamin, tuz katılmış olanlar da Fasıl 30 müstahzarı değilse burada kalır. Malt hülasalı şekerlemeler 17.04, bira ve malt esaslı içkiler (malton) Fasıl 22, malt enzimleri 35.07."],
        ["19.01 Açıklama Notu", "Esas karakteri un, nişasta vb. verir (ağırlık veya hacimce hâkim olup olmadığına bakılmaz). “Nişasta”: değişikliğe uğramamış, ön jelatinize veya çözülebilir nişasta; dekstri-maltoz gibi ileri ürünler hariç. Süt yağının bitkisel yağla değiştirildiği süt müstahzarları ve dondurma hazır karışımları 19.01; dondurmanın kendisi 21.05."],
        ["19.01 Açıklama Notu", "Hariç: kendi kendine kabaran ve ön jelatinize unlar, karışık hububat unları (11.01 / 11.02); karışık baklagil ve meyve unları (11.06); kısmen veya tamamen pişirilmiş fırıncılık mamulleri (19.05); soslar (21.03); çorbalar (21.04); tekstüre bitkisel protein (21.06); Fasıl 22 içecekleri. Esası patates unu olan knödel Fasıl 20’dedir."],
        ["19.02 Açıklama Notu", "Makarna pirinç, patates, mısır, buğday vb. unu ve irmiğinden <b>fermente edilmeden</b> yapılır; kuru, taze veya dondurulmuş olabilir. Herhangi bir oranda et, balık, peynir vb. ile doldurulmuş olabilir (kapalı: ravioli; uçları açık: cannelloni; tabakalı: lazanya). Kuskus irmiğin ısıl işlemiyle elde edilir. Makarna içeren çorbalar 21.04."],
        ["19.04 Açıklama Notu", "Bulgur: sert buğday tanelerinin pişirildikten sonra kurutulması, kabuğundan ayrılması, parçalanması ve elenmesiyle elde edilir; bütün tane de olabilir. Hamurdan yapılıp bitkisel yağda kızartılan çerezler 19.05; şekerleme karakterinde şekerli hububat 17.04; hazırlanmış yenilebilir mısır koçanı ve daneleri Fasıl 20."],
        ["19.05 Açıklama Notu", "Gevrek ekmek: su ağırlıkça <b>%10’u</b> geçmez. Tatlı bisküvi: un + şeker/tatlandırıcı + yağ ağırlıkça <b>en az %50</b>, su <b>%12</b> veya daha az, yağ <b>en fazla %35</b> (dolgu ve kaplama hesaba katılmaz). Waffle ve gofret: su <b>%10</b> veya daha az."],
        ["19.05 Açıklama Notu", "Pişirilmemiş pizza 19.01’de, ön pişirilmiş veya pişirilmiş pizza 19.05’te. Un katılmadan yapılan beze, krep, quiche ve esası patates unu veya mısır kaba unu olan yağda kızartılmış çerezler 19.05’tedir. Palmiye özünden yapılan “pirinç kâğıdı” ile karıştırılmamalıdır (14.04)."],
        ["Fasıl 16 Not 2", "%20 kuralı 19.02’deki doldurulmuş ürünlere ve 21.03, 21.04 müstahzarlarına uygulanmaz; karidesli veya etli mantı, dolgu oranı ne olursa olsun 19.02’de kalır."]
    ],
    "sinir_komsulari": [
        ["Kendi kendine kabaran un, ön jelatinize (şişen) un, karışık hububat unları", "11.01 / 11.02", "Başka şekilde hazırlanmamış değirmencilik ürünü"],
        ["Karışık baklagil unları, karışık meyve unları ve tozları", "11.06", "19.01 hariç tutması"],
        ["Ağırlıkça %20’den fazla et içeren etli pay veya doldurulmamış makarnalı hazır öğün", "Fasıl 16", "Fasıl 19 Not 1(a); istisna yalnız doldurulmuş makarna"],
        ["Köpek bisküvisi, hayvanlar için özel hazırlanmış un ürünleri", "23.09", "Fasıl 19 Not 1(b)"],
        ["Un esaslı %40 ve fazla, süt esaslı %5 ve fazla kakaolu müstahzar; çikolata kaplı mısır gevreği", "18.06", "Kakao eşikleri (Not 3, Genel Açıklamalar)"],
        ["Malt hülasalı şekerleme; şekerleme karakterinde şekerli hububat", "17.04", "Şeker mamulü karakteri"],
        ["Kahve içeren kahve yerine geçen kavrulmuş madde / kavrulmuş arpa", "09.01 / 21.01", "Genel Açıklamalar hariç tutması"],
        ["Bira, malton", "22.03 / 22.06", "Malt esaslı içkiler Fasıl 22"],
        ["Malt enzimleri", "35.07", "19.01 hariç tutması"],
        ["Süt esaslı dondurma (kakaolu olsun olmasın)", "21.05", "Dondurma tozu ise 19.01’de kalır"],
        ["Soslar; makarnalı çorba ve et suları", "21.03 / 21.04", "19.01 ve 19.02 hariç tutmaları"],
        ["Tekstüre bitkisel protein; esası un olmayan krema veya tatlı tozu", "21.06", "Başka yerde yer almayan gıda müstahzarı"],
        ["Esası patates unu olan knödel; hazırlanmış tatlı mısır", "Fasıl 20", "19.01 ve 19.04 hariç tutmaları"],
        ["Palmiye özünden “pirinç kâğıdı”", "14.04", "Un veya nişasta hamurundan olan 19.05"]
    ],
    "tuzaklar": [
        "<b>Doldurulmuş makarnada %20 sınırı yoktur.</b> Etli ravioli veya karidesli mantı, dolgu oranı ne olursa olsun 19.02’dedir; %20’den fazla et içeren doldurulmamış makarnalı hazır öğün ise Fasıl 16’ya gider.",
        "<b>Pizza pişmemişse 19.01, ön pişmiş veya pişmişse 19.05.</b> Üzerindeki peynir, domates veya ançüez faslı değiştirmez.",
        "<b>Kakao eşiği pozisyona göre değişir.</b> 19.01’de un esaslı %40, süt esaslı %5; 19.04’te %6 (veya tamamen çikolata kaplı); 19.05’te sınır yoktur.",
        "<b>Her un 19.01 anlamında “un” değildir.</b> Kurutulmuş sebze (07.12), patates (11.05) ve kuru baklagil (11.06) unları kapsam dışı; soya fasulyesi unu gibi diğer bitkisel unlar kapsam içi.",
        "<b>Kendi kendine kabaran un müstahzar sayılmaz.</b> Az miktarda kabartma tozu katılmış un 11.01 veya 11.02’de kalır; un, şeker, yağ ve yumurtalı hazır kek karışımı ise 19.01’dir.",
        "<b>Bulgur ve ön pişirilmiş pirinç Fasıl 10–11’de değil.</b> Pişirme Fasıl 10–11’in ötesinde bir işlemdir (Not 4) → 19.04. Fasıl 11 notundaki “kabaca öğütülerek elde edilen küçük parçalar (bulgur)” ifadesi pişirilmemiş hububat parçalarını anlatır; işlenmiş tane halindeki bulgur 19.04’tedir. Dane grubunda mısır hariçtir.",
        "<b>Dondurma ile dondurma karışımı ayrıdır.</b> Süt esaslı dondurma tozu 19.01’de; dondurmanın kendisi kakao oranına bakılmaksızın 21.05’te.",
        "<b>Köpek bisküvisi bisküvi değildir.</b> Hayvanlar için özel hazırlanmış un veya nişasta ürünleri 23.09’dadır.",
        "<b>Çerezde yöntem belirleyicidir.</b> Nemlendirilmiş taneler kabartılıp aroma püskürtülürse 19.04; hamurdan yapılıp yağda kızartılırsa 19.05.",
        "<b>Pirinç kâğıdı iki türlüdür.</b> Un veya nişasta hamurundan pişirilip kurutulan 19.05; palmiye özünün dilimlenmesiyle yapılan 14.04."
    ],
    "hafiza": {
        "kanca": "MA – MA – TA – GE – FI  /  20 – 40 – 5 – 6",
        "aciklama": "<b>MA</b>lt ve müstahzarlar 19.01 · <b>MA</b>karna-kuskus 19.02 · <b>TA</b>pyoka 19.03 · <b>GE</b>vrek (kabartılmış, kavrulmuş, müsli, bulgur) 19.04 · <b>FI</b>rın ürünleri 19.05. Sayılar: %20 et sınırı (doldurulmuş makarna hariç), un esaslıda %40, süt esaslıda %5, kahvaltılık gevrekte %6 kakao."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az sayıda yer almış; daha çok GYK ile birleştirilmiş set sorularında ve eşleştirme seçeneklerinde karşımıza çıkmıştır.",
        "Doldurulmuş makarna kuralı: karidesli mantı ve çorba tozundan oluşan setin, karides oranı %20’yi aşsa bile doldurulmuş makarna olarak 19.02’de ve GYK 1, 2(b), 3(b) ve 6 ile sınıflandırılması.",
        "GYK 3(b) set tanımı: pişirilmemiş spagetti, rendelenmiş peynir ve domates sosundan oluşan yemek setinin 19.02’de sınıflandırılması; aynı cins eşyanın çoklu ambalajı veya birbiriyle ilgisiz ürünlerin set sayılmaması.",
        "“Hangi eşleştirme yanlıştır” kalıbında kuskusun 19.02 ile doğru eşleştirme olarak kullanılması; komşu fasıllardaki ürünlerle (reçel, et suyu) birlikte sorulması.",
        "Fasıl 16 Not 2 istisnalarının (19.02’deki doldurulmuş ürünler, 21.03, 21.04) %20 kuralı ile birlikte sorulması."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarifenin Yorumuna İlişkin Genel Kurallardan (GYK) 3(b) anlamında “perakende satılacak hale getirilmiş takım halinde bulunan eşya” için aşağıdakilerden hangisi uygun bir örnektir?",
            "secenekler": [
                "Tek bir kutu içinde paketlenmiş, aynı malzemeden mamul, aynı renk ve tasarıma sahip 12 adet balık bıçağı",
                "Tek bir kutu içinde paketlenmiş, bir adet göz farı ve bir adet göz kalemi",
                "Tek bir kutu içinde paketlenmiş; bir poşet makarna ve üzerine dökmek için bir poşet rendelenmiş peynir ile bir poşet domates sosu (tüm ürünler sadece bir porsiyon makarna hazırlamaya yetecek gramajdadır)",
                "Tek bir kutu içinde paketlenmiş, bir kavanoz kahve (200 gr) ve bir adet seramik fincan",
                "Tek bir koli içinde paketlenmiş; bir paket makarna, bir şişe sıvı yağ, bir kavanoz salça, bir paket un ve bir paket patates cipsi"
            ],
            "cevap": "C",
            "aciklama": "GYK 3(b) Açıklama Notu, bir yemeği hazırlamak için birlikte kullanılacak pişirilmemiş spagetti, rendelenmiş peynir ve domates sosu setini örnek verir ve seti 19.02’de sınıflandırır. Aynı cins 12 bıçak farklı pozisyonlara girebilen en az iki parça şartını karşılamaz; hazır kahve ile fincan ise set oluşturmaz."
        },
        {
            "soru": "Tarife Cetveline göre ürün ve sınıflandırıldığı tarife pozisyonu ile ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?",
            "secenekler": ["Yumurta sarısı 04.08", "Buğday unu 11.01", "Kuskus 19.02", "Reçel 20.08", "Et suyu 21.04"],
            "cevap": "D",
            "aciklama": "Kuskus, hazırlanmış olsun olmasın 19.02 pozisyon metninde sayılmıştır. Yanlış olan reçeldir: pişirilerek hazırlanan reçel 20.07’dedir; 20.08 başka yerde yer almayan meyve hazırlıklarının pozisyonudur."
        }
    ],
    "ozet": [
        "%20’den fazla et, balık vb. içeren müstahzar Fasıl 16’dır; doldurulmuş makarna ise her oranda 19.02.",
        "Makarna ve kuskus pişmiş, dondurulmuş, doldurulmuş veya hazır öğün olsa da 19.02; makarnalı çorba 21.04.",
        "Kabartılmış/kavrulmuş hububat, müsli, bulgur, ön pişmiş pirinç 19.04; kakao %6’yı aşarsa veya tamamen çikolata kaplıysa 18.06.",
        "Ekmekçilik ürünleri (ekmek, bisküvi, kek, gofret, pişmiş pizza, hosti) 19.05; kakao oranı önemsiz.",
        "19.01 tamamlayıcı pozisyon: malt hülasası, un/nişasta/malt esaslı (kakao %40’tan az) ve süt esaslı (kakao %5’ten az) müstahzarlar, pişmemiş pizza, hamur karışımı.",
        "Hayvan için özel hazırlanmış bisküvi 23.09; ilaçlar Fasıl 30."
    ],
    "sorular": []
}

Q = obj["sorular"]

# 1
Q.append(S("E4",
    "Tarife Cetveline göre, sert buğday tanelerinin pişirildikten sonra kurutulması, kabuğundan ayrılması, parçalanması ve elenmesi suretiyle elde edilen bulgur hangi pozisyonda sınıflandırılır?",
    ["10.01", "11.01", "19.04", "11.04", "19.01"], "C",
    "19.04 pozisyon metni ve Açıklama Notu bulguru açıkça sayar: sert buğday taneleri önce pişirilir, sonra kurutulur, kabuğundan ayrılır, parçalanır ve elenir; bütün tane halinde de olabilir. Pişirme, Fasıl 10 ve 11’de belirtilenlerin ötesinde bir işlem olduğundan (Not 4) ürün buğday (10.01) veya işlenmiş tane (11.04) olarak sınıflandırılmaz; 11.04 Açıklama Notu da işlenmiş tane halindeki bulguru 19.04’e gönderir.",
    "Fasıl 19 Not 4; 19.04 Açıklama Notu (Bulgur); 11.04 Açıklama Notu, hariç tutmalar."))
# 2
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 19.05 pozisyonunda <b>sınıflandırılmaz</b>?",
    ["Köpekler için özel olarak hazırlanmış, un esaslı bisküvi",
     "Eczacılıkta kullanılan, nişastadan yapılmış boş ilaç kapsülleri",
     "Yumurta akı ve şekerle, un katılmadan yapılmış beze",
     "Ön pişirmeye tabi tutulmuş, üzeri peynir ve domatesle kaplı pizza",
     "Şeker hastaları için hazırlanmış gluten ekmeği"], "A",
    "Hayvan beslenmesinde kullanılmak üzere özel olarak hazırlanmış un veya nişastadan bisküviler Fasıl 19 Not 1(b) gereği 23.09’dadır. Boş ilaç kapsülleri, un katılmadan yapılan beze, ön pişmiş pizza ve gluten ekmeği 19.05 Açıklama Notunda bu pozisyona dahil olarak sayılmıştır. Tuzak, “bisküvi” kelimesine bakıp 19.05’i seçmektir.",
    "Fasıl 19 Not 1(b); 19.05 Açıklama Notu; 23.09 Açıklama Notu."))
# 3
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
    ["Mısır gevreği (corn flakes)",
     "Basınç altında ısıtılıp kabartılmış pirinç",
     "Kavrulmamış hububat flokonu, kuru meyve ve fındıktan oluşan müsli",
     "Bütün tane halindeki bulgur",
     "Hamurdan yapılıp bitkisel yağda kızartılmış peynir aromalı çerez"], "E",
    "Mısır gevreği, kabartılmış pirinç, müsli ve bulgur 19.04 metninde ve Açıklama Notunda sayılmıştır. 19.04 Açıklama Notu, nemlendirilmiş tanelerin kabartılmasıyla elde edilen çeşnili çerezleri kapsadığını, hamurdan yapılıp bitkisel yağda kızartılan benzeri ürünlerin ise hariç olduğunu (19.05) belirtir.",
    "19.04 Açıklama Notu; 19.05 Açıklama Notu."))
# 4
Q.append(S("TN",
    "Tarife Cetvelinin 19. Fasıl notlarına göre, 19.04 pozisyonundaki hububat ürünlerinin kakao içeriğine ilişkin aşağıdakilerden hangisi <b>doğrudur</b>?",
    ["Yağı tamamen alınmış baz üzerinden ağırlıkça %40’tan az kakao içerenler 19.04’te kalır.",
     "Yağı alınmış bazda %6’dan fazla kakaolu veya tamamen çikolata kaplı olanlar 18.06’ya gider.",
     "Kakao oranı ne olursa olsun 19.04’teki ürünler bu pozisyonda kalır.",
     "Yağı tamamen alınmış baz üzerinden ağırlıkça %5 ve daha fazla kakao içerenler 18.06’ya gider.",
     "Yalnızca çikolata ile kaplanmış ürünler 19.04 dışında kalır; kakao oranı hiçbir durumda dikkate alınmaz."], "B",
    "Fasıl 19 Not 3’e göre 19.04, yağı tamamen alınmış baz üzerinden ağırlıkça %6’dan fazla kakao içeren veya tamamen çikolata ile kaplanmış müstahzarları kapsamaz; bunlar 18.06’dadır. %40 ve %5 eşikleri 19.01’e aittir (un esaslı ve süt esaslı müstahzarlar); oranın önemsiz olduğu pozisyon ise 19.05’tir.",
    "Fasıl 19 Not 3; Fasıl 19 Genel Açıklamalar."))
# 5
Q.append(S("E4",
    "Tarife Cetveline göre, kıyılmış et ve peynirle doldurulmuş dondurulmuş ravioli (dolgudaki etin ağırlığı ürünün %30’u) hangi pozisyonda sınıflandırılır?",
    ["16.02", "19.01", "21.04", "19.02", "16.01"], "D",
    "19.02 pozisyon metni et veya diğer maddelerle doldurulmuş makarnayı kapsar; Açıklama Notuna göre dolgu herhangi bir oranda olabilir. Fasıl 19 Not 1(a) ve Fasıl 16 Not 2, %20 kuralını 19.02’deki doldurulmuş ürünlere uygulamaz. Bu nedenle et oranı %20’yi aşsa da ürün 16.01 veya 16.02’ye gitmez.",
    "Fasıl 19 Not 1(a); Fasıl 16 Not 2; 19.02 Açıklama Notu."))
# 6
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 19.01 pozisyonunda <b>yer almaz</b>?",
    ["İçine az miktarda kabartma tozu katılmış kendi kendine kabaran buğday unu",
     "Lesitin ve vitamin katılmış, eczacılık müstahzarı niteliğinde olmayan toz malt hülasası",
     "Hububat unu, şeker, yağ ve yumurtadan oluşan hazır kek hamuru karışımı",
     "Süt yağının bitkisel yağla değiştirilmesiyle elde edilen süt müstahzarı",
     "Süt esaslı dondurma yapımında kullanılan hazır toz karışım"], "A",
    "19.01 Açıklama Notu, 11.01 veya 11.02’deki kendi kendine kabaran unları bu pozisyon dışında bırakır. Vitaminli malt hülasası (Fasıl 30 müstahzarı değilse), hazır hamur karışımları, süt bileşeninin başka maddeyle değiştirildiği süt müstahzarları ve dondurma hazır karışımları 19.01’de sayılmıştır.",
    "19.01 Açıklama Notu (kapsam ve hariç tutmalar); 21.02 Açıklama Notu."))
# 7
Q.append(S("FA",
    "Aşağıdaki eşyadan hangisi diğerlerinden farklı bir fasılda yer alır?",
    ["Hosti",
     "Mühür güllacı",
     "Un ve nişasta hamurundan pişirilip kurutularak yapılan pirinç kâğıdı",
     "Bazı palmiyelerin öz kısmının dilimlenmesiyle yapılan “pirinç kâğıdı”",
     "Eczacılıkta kullanılan çeşitte boş kapsüller"], "D",
    "Hosti, mühür güllacı, boş ilaç kapsülleri ve un veya nişasta hamurundan yapılan pirinç kâğıdı 19.05 pozisyon metninde sayılmıştır. 19.05 Açıklama Notu, palmiyelerin öz kısmını dilimleyerek yapılan ve aynı adla anılan maddenin bunlarla karıştırılmaması gerektiğini belirtip 14.04’e (Fasıl 14) gönderir.",
    "19.05 Açıklama Notu (pirinç kâğıdı)."))
# 8
Q.append(S("TN",
    "Tarife Cetvelinin 19.05 pozisyonu Açıklama Notuna göre “tatlı bisküvi” tanımı ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
    ["Un, şeker ve yağ ağırlıkça en az %40’ını oluşturur; su miktarı %10’u geçemez.",
     "Un, şeker/tatlandırıcı ve yağ en az %50; su en çok %12, yağ en çok %35 olur.",
     "Su miktarı %12’yi, yağ miktarı %20’yi geçemez; dolgu ve kaplama hesaba katılır.",
     "Un ve şeker ağırlıkça en az %50’sini oluşturur; yağ oranı için bir sınır yoktur.",
     "Su miktarı ağırlıkça %10’u geçmeyen, ince ve gevrek ekmekçilik ürünüdür."], "B",
    "Açıklama Notuna göre tatlı bisküviler un, şeker veya diğer tatlandırıcılar ve yağdan (bu maddeler ağırlıkça en az %50) yapılır; su %12 veya daha az, yağ en fazla %35 olmalıdır ve dolgu ile kaplama bu hesaba katılmaz. Su sınırı %10 olan ürünler gevrek ekmek ile waffle ve gofretlerdir (A ve E’deki tuzak).",
    "19.05 Açıklama Notu (Bisküviler, Gevrek ekmek, Waffle ve gofretler)."))
# 9
Q.append(S("GYK",
    "Karton kutu içinde perakende satışa sunulan; pişirilmemiş bir paket spagetti, küçük bir poşet rendelenmiş peynir ve küçük bir teneke domates sosundan oluşan ve spagetti yemeği hazırlamak için birlikte kullanılması amaçlanan takım için hangi kural–pozisyon ikilisi doğrudur?",
    ["GYK 3(c) – 21.03", "GYK 3(a) – 04.06", "GYK 2(a) – 19.02", "GYK 3(b) – 21.03", "GYK 3(b) – 19.02"], "E",
    "Ürünler farklı pozisyonlara (19.02, 04.06, 21.03) girer, belirli bir yemeği hazırlamak için bir araya getirilmiştir ve yeniden paketlenmeden son kullanıcıya satılabilir; bu nedenle perakende takımdır. GYK 3(b) Açıklama Notu bu örneği vererek takımı asli niteliği veren spagetti üzerinden 19.02’de sınıflandırır. 3(c) ile numara sırasına göre son pozisyonu (21.03) seçmek tuzaktır; 3(c) ancak 3(b) yetersiz kalırsa uygulanır.",
    "GYK 3(b) Açıklama Notu (X)."))
# 10
Q.append(S("ES",
    "Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
    ["Kuskus – 19.02", "Tapyoka – 19.03", "Ön pişirilmiş pizza – 19.01", "Malt hülasası – 19.01", "Waffle – 19.05"], "C",
    "19.01 Açıklama Notu yalnız pişirilmemiş pizzayı bu pozisyona alır; ön pişirmeye tabi tutulmuş veya pişirilmiş pizza 19.05’tedir. Kuskus 19.02, tapyoka 19.03, malt hülasası 19.01 ve waffle 19.05 pozisyon metinlerinde veya Açıklama Notlarında doğru yerdedir.",
    "19.01 ve 19.05 Açıklama Notları (pizza)."))
# 11
Q.append(S("CC",
    "Tarife Cetveline göre 19.01 pozisyonu anlamında aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. “Un” tabiri, soya fasulyesi unu gibi herhangi bir fasılda yer alan bitkisel menşeli gıda unlarını da kapsar. II. “Un” tabiri, 11.05 pozisyonundaki patates ununu da kapsar. III. “Nişasta” tabiri, ön jelatinize edilmiş veya çözülebilir nişastaları kapsar. IV. “Nişasta” tabiri, dekstri-maltoz gibi daha ileri nişasta ürünlerini de kapsar.",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "I, II ve III"], "B",
    "Fasıl 19 Not 2 ve 19.01 Açıklama Notuna göre “un”, Fasıl 11 hububat unlarıyla birlikte herhangi bir fasıldaki bitkisel menşeli gıda unlarını (ör. soya unu) kapsar; ancak kurutulmuş sebze (07.12), patates (11.05) ve kuru baklagil (11.06) unları hariçtir (II yanlış). “Nişasta” değişikliğe uğramamış, ön jelatinize veya çözülebilir nişastaları kapsar, dekstri-maltoz gibi ileri ürünleri kapsamaz (IV yanlış).",
    "Fasıl 19 Not 2; 19.01 Açıklama Notu."))
# 12
Q.append(S("SN",
    "Kahvaltıda sütle tüketilmek üzere hazırlanan bir ürün; kavrulmamış yulaf flokonları, kavrulmuş buğday flokonları, kuru üzüm, fındık ve bal içermektedir. Ürün kakao içermemekte, çikolata ile kaplı değildir ve perakende kutularda sunulmaktadır. Bu ürün hangi pozisyonda sınıflandırılır?",
    ["11.04", "19.01", "20.08", "17.04", "19.04"], "E",
    "19.04 Açıklama Notu, kavrulmamış hububat flokonlarından veya bunların kavrulmuş flokonlar ya da kabartılmış hububatla karışımlarından elde edilen, kurutulmuş meyve, fındık, şeker, bal vb. içerebilen “müsli” türü hazır gıdaları bu pozisyona alır. Yalnız flokon haline getirilmiş yulaf 11.04’te kalırdı; fındık ve kuru meyve ilavesi ürünü 20.08’e götürmez.",
    "19.04 Açıklama Notu (müsli); Fasıl 19 Not 4."))
# 13
Q.append(S("E4",
    "Tarife Cetveline göre, manyok nişastasından elde edilen inci tanesi şeklindeki tapyoka hangi pozisyonda sınıflandırılır?",
    ["19.03", "11.08", "07.14", "19.01", "11.06"], "A",
    "19.03, manyok (tapyoka), sagu, patates ve benzeri nişastalardan flokon, dane, inci veya kalbur içi kalıntısı şeklinde elde edilen yenilebilir ürünleri kapsar. Nişastanın kendisi 11.08, manyok kökü 07.14, manyok unu 11.06’dadır; 19.01 Açıklama Notu tapyokayı açıkça hariç tutup 19.03’e gönderir.",
    "19.03 Açıklama Notu; 19.01 Açıklama Notu, hariç tutmalar."))
# 14
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 19. Faslında <b>yer almaz</b>?",
    ["Önceden kısmen pişirilip suyu alınmış, dane yapısı değişmiş pirinç",
     "Mayasız ekmek (matzos)",
     "Esası hububat unu ve malt hülasası olan, yağı tamamen alınmış bazda %15 kakaolu ve sütle karıştırılarak içilen toz",
     "Esası un, nişasta, malt hülasası veya süt ürünleri olmayan, sofralık krema yapımına mahsus toz",
     "Peynir, yumurta ve krema dolgulu quiche"], "D",
    "Fasıl 19 Genel Açıklamaları, esası un, kaba un, nişasta, malt hülasası veya 04.01–04.04 maddeleri olmayan krema, dondurma, tatlı vb. tozlarını fasıl dışında bırakır (genellikle 21.06). Ön pişmiş pirinç 19.04’te, matzos ve quiche 19.05’te; kakao oranı %40’ın altında kalan un esaslı içecek tozu ise 19.01’dedir.",
    "Fasıl 19 Genel Açıklamalar; 19.01, 19.04, 19.05 Açıklama Notları."))
# 15
Q.append(S("FA",
    "Aşağıdaki seçeneklerin hangisinde sayılan eşyanın <b>tamamı</b> aynı tarife pozisyonunda yer alır?",
    ["Spagetti – kuskus – tapyoka",
     "Mısır gevreği – bulgur – pişirilmemiş pizza",
     "Krep – zencefilli ekmek – pretzel",
     "Malt hülasası – hazır kek karışımı – köpek bisküvisi",
     "Lazanya – ravioli – makarnalı çorba"], "C",
    "Krep, zencefilli ekmek ve pretzel 19.05 Açıklama Notunda ekmekçilik ürünü olarak sayılmıştır. Diğer gruplarda birer “yabancı” vardır: tapyoka 19.03, pişirilmemiş pizza 19.01, köpek bisküvisi 23.09, makarnalı çorba 21.04.",
    "19.05 Açıklama Notu; Fasıl 19 Not 1(b); 19.02 Açıklama Notu, hariç tutmalar."))
# 16
Q.append(S("TN",
    "Tarife Cetvelinin 19. Fasıl Genel Açıklamalarına göre, esası 04.01 ila 04.04 pozisyonlarındaki maddeler olan bir gıda müstahzarı, yağı tamamen alınmış baz üzerinden ağırlıkça en az yüzde kaç kakao içerdiğinde 18.06 pozisyonuna girer?",
    ["%40", "%6", "%20", "%31", "%5"], "E",
    "Genel Açıklamalara göre 04.01–04.04 maddelerinden yapılan gıda müstahzarları, yağı tamamen alınmış bazda ağırlıkça %5 ve daha fazla kakao içerirse 18.06’dadır; 19.01 metni de bu ürünleri “%5’ten az” kakao ile sınırlar. %40 un esaslı müstahzarların, %6 ise 19.04’ün eşiğidir; 31 kakao hesabında teobromin ve kafein toplamının çarpıldığı faktördür.",
    "Fasıl 19 Genel Açıklamalar; 19.01 pozisyon metni."))
# 17
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
    ["Taze (kurutulmamış), patates ve buğday unundan yapılmış gnocchi",
     "İçine kıyma konularak yapılmış, ağırlıkça %30 et içeren etli pay",
     "Pişirilmiş ton balığı ve peynirle doldurulmuş, uçları açık cannelloni",
     "Sebzeler ve sosla birlikte komple bir öğün halinde hazırlanmış kuskus",
     "Ispanak ve beşamelle hazırlanmış dondurulmuş lazanya"], "B",
    "Gnocchi, cannelloni, lazanya ve hazırlanmış kuskus 19.02’dedir; doldurulmuş makarnada dolgu oranı önemsizdir. Etli pay ise bir ekmekçilik ürünüdür ve %20 istisnası yalnız 19.02’deki doldurulmuş ürünler için geçerli olduğundan, ağırlıkça %20’den fazla et içeren pay 19.05 Açıklama Notu uyarınca Fasıl 16’ya gider.",
    "Fasıl 19 Not 1(a); 19.02 ve 19.05 Açıklama Notları."))
# 18
Q.append(S("GYK",
    "Dolgusunda ağırlıkça %40 et bulunan etli ravioli 16.02 yerine 19.02 pozisyonunda sınıflandırılmaktadır. Bu sınıflandırmanın dayandığı Genel Yorum Kuralı aşağıdakilerden hangisidir?",
    ["GYK 1: pozisyon metni ve fasıl notlarının açık hükmü",
     "GYK 3(b): mamule asli niteliği veren maddenin hamur olması",
     "GYK 3(c): geçerli pozisyonlardan numara sırasına göre sonuncusu",
     "GYK 4: eşyaya en çok benzeyen eşyanın bulunduğu pozisyon",
     "GYK 2(b): karışımların bileşenlerine göre sınıflandırılması"], "A",
    "19.02 metni “et veya diğer maddelerle doldurulmuş” makarnayı açıkça sayar; Fasıl 19 Not 1(a) ve Fasıl 16 Not 2 de %20 kuralını doldurulmuş ürünlere uygulamaz. Sonuç doğrudan pozisyon metni ve notlardan çıktığı için GYK 1 uygulanır; 3(b) veya 3(c) gibi kurallara ancak 1. kural yetmediğinde başvurulur.",
    "GYK 1; Fasıl 19 Not 1(a); Fasıl 16 Not 2."))
# 19
Q.append(S("E4",
    "Tarife Cetveline göre, çavdar unu hamurundan yapılıp ekşi hamurla mayalanmış, ince dikdörtgen şekilli ve su içeriği ağırlıkça %10’u geçmeyen gevrek ekmek (knäckebrot) hangi pozisyonda sınıflandırılır?",
    ["19.04", "11.02", "19.05", "19.01", "11.04"], "C",
    "19.05 Açıklama Notu gevrek ekmeği (knäckebrot) açıkça sayar: çavdar, yulaf, arpa veya buğday unu ya da kaba unundan hamur, mayalı veya ekşi hamurlu, su miktarı ağırlıkça %10’u geçmez. Fırında pişmiş bir ekmekçilik ürünü olduğundan kabartılmış hububat (19.04), un (11.02) veya hamur karışımı (19.01) olarak sınıflandırılmaz.",
    "19.05 Açıklama Notu (Gevrek ekmek)."))
# 20
Q.append(S("TN",
    "Tarife Cetvelinin 19. Fasıl notlarına göre, 19.04 pozisyonu anlamında “başka şekilde hazırlanmış” tabirinden ne anlaşılır?",
    ["Yalnızca şekerle kaplanmış veya tatlandırılmış hububat",
     "Kabuğu çıkarılmış, yassılatılmış veya flokon haline getirilmiş hububat",
     "Ağırlıkça %6’dan fazla kakao içeren hububat müstahzarları",
     "10. ve 11. Fasıllarda belirtilenlerden daha ileri işleme tabi tutulmuş hububat",
     "Un, kaba un veya kabaca öğütülerek elde edilen küçük parçalar halindeki hububat"], "D",
    "Fasıl 19 Not 4’e göre bu tabir, 10. ve 11. Fasıl notlarında veya pozisyonlarında belirtilenlerden daha ileri işleme tabi tutulmuş hububatı ifade eder. Kabuğu çıkarma, yassılatma, flokon yapma Fasıl 11 işlemleridir; %6’yı aşan kakaolu ürünler Not 3 gereği 18.06’dadır; un ve kaba un ise 19.04 metninden açıkça hariçtir.",
    "Fasıl 19 Not 3 ve Not 4; 19.04 pozisyon metni."))
# 21
Q.append(S("CC",
    "Tarife Cetveline göre aşağıdakilerden hangileri 19. Fasıl <b>dışında</b> sınıflandırılır? I. İçinde herhangi bir oranda kahve bulunan, kahve yerine kullanılan kavrulmuş maddeler II. Kavrulmuş arpa gibi kahve yerine kullanılan diğer kavrulmuş maddeler III. Malt hülasası içeren şekerleme mamulleri IV. Lesitin katılmış, eczacılık müstahzarı niteliğinde olmayan malt hülasası",
    ["I ve II", "I ve III", "II, III ve IV", "III ve IV", "I, II ve III"], "E",
    "Genel Açıklamalara göre kahve içeren kahve yerine geçen kavrulmuş maddeler 09.01’de (I), kavrulmuş arpa gibi diğerleri 21.01’de (II) yer alır. Malt hülasalı şekerlemeler 19.01 Açıklama Notu gereği 17.04’tedir (III). Lesitin, vitamin veya tuz katılmış malt hülasası ise Fasıl 30 müstahzarı olmadıkça 19.01’de kalır (IV fasıl içidir).",
    "Fasıl 19 Genel Açıklamalar; 19.01 Açıklama Notu (Malt hülasası)."))
# 22
Q.append(S("SN",
    "Bir firma; pirinç unu, muhtelif nişastalar, tatlı meşe palamudu ve şekerden oluşan, vanilya ile aromalandırılmış ve yağı tamamen alınmış baz üzerinden ağırlıkça %10 kakao içeren bir gıda müstahzarı (rakau) ithal etmektedir. Ürün süt veya su ile karıştırılarak tüketilmektedir. Bu ürün hangi pozisyonda sınıflandırılır?",
    ["18.06", "21.06", "19.01", "11.02", "19.04"], "C",
    "19.01 Açıklama Notu rakauyu (pirinç unu, nişastalar, tatlı meşe palamudu, şeker ve kakaodan oluşan, vanilyalı gıda müstahzarı) örnek olarak sayar. Esası un ve nişasta olduğundan kakao eşiği %40’tır; %10 kakao ürünü 18.06’ya götürmez. Başka yerde yer almayan müstahzarlar için 21.06’ya ancak 19.01 uymadığında gidilir.",
    "19.01 Açıklama Notu; Fasıl 19 Genel Açıklamalar."))
# 23
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 19.04 pozisyonunda <b>sınıflandırılmaz</b>?",
    ["Tamamen çikolata ile kaplanmış mısır gevreği",
     "Kabartılmış buğday (puffed wheat)",
     "Ön pişirme yapılmış, asli karakteri değişmeyecek kadar az sebze ve baharat katılmış pirinç",
     "Kepeğin kavrulmasıyla elde edilen kahvaltılık gıda müstahzarı",
     "Bütün tane halindeki bulgur"], "A",
    "Fasıl 19 Not 3, tamamen çikolata ile kaplanmış müstahzarları kakao oranına bakılmaksızın 19.04 dışında bırakır (18.06). Kabartılmış buğday, kavrulmuş kepek ürünleri, az miktarda sebze ve baharatlı ön pişmiş pirinç ve bütün tane bulgur 19.04 Açıklama Notunda sayılmıştır.",
    "Fasıl 19 Not 3; 19.04 Açıklama Notu."))
# 24
Q.append(S("ES",
    "Tarife Cetveline göre; pişirilmemiş pizza (I) pozisyonunda, ön pişirmeye tabi tutulmuş pizza (II) pozisyonunda, makarna içeren çorba (III) pozisyonunda, köpek bisküvisi ise (IV) pozisyonunda sınıflandırılır. Boşlukları sırasıyla dolduran seçenek hangisidir?",
    ["19.05 / 19.01 / 19.02 / 23.09",
     "19.01 / 19.05 / 21.04 / 23.09",
     "19.01 / 19.05 / 19.02 / 19.05",
     "19.05 / 19.05 / 21.04 / 23.09",
     "19.01 / 19.01 / 21.03 / 23.09"], "B",
    "Pişirilmemiş pizza 19.01’de, ön pişmiş veya pişmiş pizza 19.05’te yer alır. Makarna içeren çorbalar 19.02 Açıklama Notu gereği 21.04’e gider; hayvanlar için özel hazırlanmış köpek bisküvisi Fasıl 19 Not 1(b) uyarınca 23.09’dadır.",
    "19.01, 19.02, 19.05 Açıklama Notları; Fasıl 19 Not 1(b)."))
# 25
Q.append(S("E4",
    "Tarife Cetveline göre, waffle hamurunun özel bir makineden püskürtülmesiyle elde edilen ve su içeriği ağırlıkça %10’u geçmeyen dondurma külahı (kornet) hangi pozisyonda sınıflandırılır?",
    ["21.05", "19.01", "17.04", "19.05", "19.04"], "D",
    "19.05 Açıklama Notu, waffle hamurunun özel bir makineden püskürtülmesiyle elde edilen ürünleri (ör. dondurma kornetleri) waffle ve gofretler arasında sayar; bitmiş üründe su ağırlıkça %10 veya daha azdır. Külah dondurma ile birlikte kullanılsa da dondurma (21.05) değildir; şekerleme (17.04) de sayılmaz.",
    "19.05 Açıklama Notu (Waffle ve gofretler)."))

kaydet(obj, 19)
