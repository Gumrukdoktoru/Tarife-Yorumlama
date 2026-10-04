import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_19_23 import S, kaydet  # noqa: E402

obj = {
    "tur": "fasil",
    "fasil": 20,
    "baslik": "Sebzeler, meyveler, sert kabuklu meyveler ve bitkilerin diğer kısımlarından elde edilen müstahzarlar",
    "bolum": "IV",
    "oz": {
        "vurgu": "Fasıl 20, sebze, meyve, sert kabuklu meyve ve yenilen diğer bitki parçalarının Fasıl 7, 8 ve 11’de sayılan işlemlerin ötesinde hazırlanmış veya konserve edilmiş hallerini kapsar. Önce yöntem sorulur (sirke, şekerle konserve, pişirerek reçel, meyve suyu), sonra ürün (domates, mantar, diğer sebze, meyve).",
        "maddeler": [
            "Sirke veya asetik asitle hazırlanan sebze, meyve ve kuruyemiş (turşu) 20.01; sirke dışı yöntemle domates 20.02, mantar ve domalan 20.03.",
            "Diğer sebzeler: hazırlanmış ve dondurulmuşsa 20.04, dondurulmamışsa 20.05; şekerle konserve edilmiş (suyu alınmış, glase, kristalize) ürünler 20.06.",
            "Pişirilerek hazırlanan reçel, jöle, marmelat, püre ve pastlar 20.07; başka yerde yer almayan meyve ve kuruyemiş hazırlıkları (kavrulmuş fındık, fıstık ezmesi, şurupta meyve) 20.08.",
            "Fermente edilmemiş ve alkol katılmamış (alkol derecesi hacimce %0,5’i geçmeyen) meyve ve sebze suları 20.09."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Ağırlıkça %20’den fazla sosis, et, sakatat, kan, böcek, balık veya su omurgasızı içeriyor mu?", "<b>Fasıl 16</b>"],
            ["2", "Yalnız Fasıl 7, 8 veya 11’de belirtilen işlemleri mi görmüş? (soğutma, dondurma, kurutma, geçici konserve, öğütme)", "<b>Fasıl 7 / 8 / 11</b>"],
            ["3", "Ekmekçilik ürünü, 21.04 homojenize bileşik müstahzar, şekerleme veya çikolata mamulü mü?", "<b>19.05</b> / <b>21.04</b> / <b>17.04</b> / <b>18.06</b>"],
            ["4", "Meyve, kuruyemiş veya sebze suyu mu? (fermente değil, alkol %0,5’i geçmiyor)", "<b>20.09</b> · kuru maddesi %7+ domates suyu <b>20.02</b> · alkol %0,5’i aşarsa <b>Fasıl 22</b>"],
            ["5", "Sirke veya asetik asitle mi hazırlanmış?", "<b>20.01</b>"],
            ["6", "Şekerle konserve edilmiş mi? (suyu alınmış, glase, kristalize)", "<b>20.06</b> · şurup içindeyse meyve <b>20.08</b>, sebze <b>20.02 / 20.03 / 20.05</b>"],
            ["7", "Pişirilerek hazırlanmış reçel, jöle, marmelat, püre veya pastlar mı?", "<b>20.07</b>"],
            ["8", "Domates mi? Mantar veya domalan mı?", "<b>20.02</b> / <b>20.03</b>"],
            ["9", "Diğer sebze mi?", "Dondurulmuş <b>20.04</b> · dondurulmamış <b>20.05</b>"],
            ["10", "Meyve, sert kabuklu meyve veya yenilen diğer bitki parçası mı?", "<b>20.08</b>"]
        ],
        "dipnot": "Ambalaj türü (teneke kutu, kavanoz, fıçı, hava geçirmez kap) Fasıl 20 içindeki pozisyonu değiştirmez; belirleyici olan hazırlama yöntemidir."
    },
    "pozisyon_haritasi": [
        ["20.01", "Sirke veya asetik asitle hazırlanmış sebze, meyve, kuruyemiş", "Yöntem: sirke/asetik asit; tuz, baharat, şeker olabilir", "Hıyar ve kornişon turşusu, sirkeli zeytin, kapari"],
        ["20.02", "Domatesler (sirke dışı yöntemle)", "Bütün, parça, homojenize; kuru maddesi %7+ domates suyu", "Domates konservesi, salça, domates püresi"],
        ["20.03", "Mantarlar ve domalan (sirke dışı)", "Saplar dahil; bütün, dilim, homojenize", "Konserve mantar, domalan konservesi"],
        ["20.04", "Diğer sebzeler, dondurulmuş (sirke dışı)", "Hazırlanmış ve dondurulmuş; 20.06 hariç", "Dondurulmuş parmak patates, tereyağlı donmuş bezelye"],
        ["20.05", "Diğer sebzeler, dondurulmamış (sirke dışı)", "Hazırlanmış, dondurulmamış; 20.06 hariç", "Sofralık zeytin, sauerkraut, konserve tatlı mısır"],
        ["20.06", "Şekerle konserve edilmiş sebze, meyve, kabuk, bitki parçası", "Suyu alınmış, glase, kristalize; şurupta olanlar hariç", "Kristalize kiraz, şekerlenmiş portakal kabuğu"],
        ["20.07", "Reçel, jöle, marmelat, püre ve pastlar", "Pişirilerek elde edilmiş; tatlandırıcı olsun olmasın", "Çilek reçeli, portakal marmelatı, ayva pastı"],
        ["20.08", "Başka yerde yer almayan meyve, kuruyemiş, bitki parçası hazırlıkları", "Tamamlayıcı pozisyon; şeker veya alkol katılmış olabilir", "Kavrulmuş fındık, fıstık ezmesi, şurupta şeftali, marrons glacés"],
        ["20.09", "Meyve, kuruyemiş ve sebze suları (fermente edilmemiş)", "Alkol %0,5’i geçmez; konsantre veya toz olabilir", "Portakal suyu, üzüm şırası, Hindistan cevizi suyu, havuç suyu"]
    ],
    "notlar": [
        ["Fasıl 20 Not 1", "Fasıl 20 dışı: (a) Fasıl 7, 8 veya 11’de belirtilen usullerle hazırlanmış veya konserve edilmiş sebze, meyve ve sert kabuklu meyveler; (b) bitkisel katı ve sıvı yağlar (Fasıl 15); (c) ağırlıkça %20’den fazla sosis, et, sakatat, kan, böcek, balık, kabuklu hayvan, yumuşakça veya diğer su omurgasızı içeren gıda müstahzarları (Fasıl 16); (d) 19.05’teki ekmekçilik mamulleri; (e) 21.04’teki homojenize edilmiş bileşik gıda müstahzarları."],
        ["Fasıl 20 Not 2", "Şeker mamulleri (17.04) veya çikolata mamulleri (18.06) haline getirilmiş meyve jöleleri, meyve ezmeleri, bademli şekerler ve benzerleri 20.07 ve 20.08’e dahil değildir."],
        ["Fasıl 20 Not 3", "20.01, 20.04 ve 20.05; Not 1(a)’daki usullerden başka şekilde hazırlanmış veya konserve edilmiş olmak şartıyla yalnızca Fasıl 7 ürünlerini veya 11.05 ya da 11.06 ürünlerini (Fasıl 8 ürünlerinin unları, kaba unları ve tozları hariç) kapsar."],
        ["Fasıl 20 Not 4", "Kuru ağırlık muhteviyatı <b>%7 ve daha fazla</b> olan domates suları 20.02’de yer alır."],
        ["Fasıl 20 Not 5", "20.07 anlamında “pişirilerek elde edilmiş”: su içeriğinin azaltılması veya diğer yöntemlerle viskozitenin artırılması için ürünün atmosfer basıncında veya düşürülmüş basınç altında ısıl işleme tabi tutulması."],
        ["Fasıl 20 Not 6", "20.09 anlamında “fermente edilmemiş ve ilave alkol katılmamış sular”: alkol derecesi hacim itibariyle <b>%0,5’i geçmeyen</b> sular."],
        ["Fasıl 22 Not 2", "Fasıl 20, 21 ve 22’nin uygulanmasında hacim itibariyle alkol derecesi <b>20 °C</b> sıcaklıkta tespit edilir."],
        ["Genel Açıklamalar", "Fasıl 20’ye dahil: sirke veya asetik asitle hazırlananlar; şekerle konserve edilenler; pişirilerek elde edilen reçel, jöle, marmelat, püre ve pastlar; homojenize sebze ve meyveler; meyve ve sebze suları; başka işlemlerle hazırlananlar; osmotik dehidrasyonla konserve edilen meyveler. Hariç: meyve tartları gibi pastacılık ürünleri (19.05), 21.04 çorbaları, alkolü %0,5’i aşan sular (Fasıl 22)."],
        ["20.01 Açıklama Notu", "Tuz, baharat, hardal, şeker, yağ içerebilir; dökme, kavanoz, şişe veya hava geçirmez kapta olabilir. 21.03’teki sıvı, emülsiyon veya süspansiyon halinde, tek başına yenmeyen soslardan farklıdır."],
        ["20.02 Açıklama Notu", "Kap tipi dikkate alınmaz; domates püresi, salçası, konsantresi ve kuru maddesi %7+ domates suyu dahildir. Domates ketçabı ve diğer domates sosları 21.03, domates çorbası 21.04."],
        ["20.05 Açıklama Notu", "Soda çözeltisinde işlenerek veya salamurada uzun süre yatırılarak yenilir hale getirilmiş zeytin 20.05; salamurada yalnız geçici olarak konserve edilmiş zeytin 07.11. Sauerkraut ve kızartılarak cips yapılacak patates unu tabletleri 20.05; 19.05’teki baharatlı gevrek çerezler ve sebze suları (20.09) hariç."],
        ["20.06 Açıklama Notu", "Ne şekilde paketlenmiş olursa olsun şurup içinde konserve edilenler hariçtir (sebze 20.02, 20.03 veya 20.05; meyve, marrons glacés, zencefil 20.08). Az şeker katılmış veya dışı kendi şekeriyle kaplanmış kurutulmuş meyveler Fasıl 8’de kalır."],
        ["20.07 Açıklama Notu", "Reçel meyvenin yaklaşık kendi ağırlığı kadar şekerle kaynatılmasıyla, jöle meyve sularından (meyve parçası içermez), marmelat genellikle turunçgillerden yapılır. Sorbitol gibi suni tatlandırıcı kullanılabilir. Jelatin, şeker ve meyve esansından sofralık jöleler 21.06."],
        ["20.08 Açıklama Notu", "Kavrulmuş sert kabuklu meyveler, yer fıstığı ezmesi, suda, şurupta veya alkolde meyve, sterilize meyve pulpu, pişirilmiş meyve dahildir. Buharda veya suda kaynatılıp dondurulmuş meyve 08.11; su veya şurup katılarak doğrudan içilebilir hale getirilmiş ezilmiş meyve 22.02; bitki çayı karışımları 08.13, 09.09 veya 21.06."],
        ["20.09 Açıklama Notu", "Şeker, tatlandırıcı, koruyucu, standardize edici madde içerebilir; ancak doğal dengeyi kesin olarak bozan ilaveler ürünü pozisyon dışına çıkarır. Doğal orandan fazla su veya karbondioksit eklenmiş sular ve limonatalar 22.02; %0,5’i aşan kısmen fermente üzüm şırası 22.04; meyve suyu bulunmayan meyvelerin (kuşburnu, ardıç) suda ısıtılmasıyla elde edilen sıvılar genellikle 21.06."]
    ],
    "sinir_komsulari": [
        ["Salamurada geçici olarak konserve edilmiş, hemen yenmeye elverişsiz zeytin", "07.11", "Fasıl 7 işlemi (Not 1(a))"],
        ["Buharda veya suda kaynatılıp dondurulmuş meyve", "08.11", "20.08 hariç tutması"],
        ["Az şeker katılmış kurutulmuş incir veya erik", "Fasıl 8", "20.06 hariç tutması"],
        ["Bitkisel katı ve sıvı yağlar", "Fasıl 15", "Not 1(b)"],
        ["Ağırlıkça %20’den fazla et içeren sebzeli konserve yemek", "Fasıl 16", "Not 1(c)"],
        ["Meyve jölesi şekerlemesi; meyve ezmeli çikolatalı bonbon", "17.04 / 18.06", "Not 2"],
        ["Meyveli tart; esası patates unu olan kızartılmış gevrek çerez", "19.05", "Not 1(d); 20.05 hariç tutması"],
        ["Domates ketçabı ve diğer domates sosları", "21.03", "Tek başına yenmeyen sos"],
        ["Domates çorbası; 21.04 homojenize bileşik gıda müstahzarı", "21.04", "Not 1(e); 20.02 hariç tutması"],
        ["Jelatinli sofralık jöle; kuşburnu veya ardıç meyvesinden elde edilen sıvı", "21.06", "20.07 ve 20.09 hariç tutmaları"],
        ["Seyreltilmiş meyve suyu, limonata, içilmeye hazır ezilmiş meyve", "22.02", "Alkolsüz içecek karakteri"],
        ["Kısmen fermente olmuş üzüm şırası (alkol %0,5’in üzerinde)", "22.04", "20.09 hariç tutması"],
        ["Bitki ve bitki parçalarından bitki çayı karışımları", "08.13 / 09.09 / 21.06", "20.08 hariç tutması"]
    ],
    "tuzaklar": [
        "<b>Sirke yöntemi önce gelir.</b> Sirkeli zeytin, sirkeli domates veya sirkeli mantar 20.01’dedir; 20.02–20.05 başlıkları “sirke veya asetik asitten başka usullerle” hazırlananları kapsar.",
        "<b>Şurup içindeki meyve 20.06 değildir.</b> 20.06 suyu alınmış, glase veya kristalize ürünleri kapsar; şurupta konserve meyve (marrons glacés, zencefil dahil) 20.08’e, şurupta sebze 20.02 / 20.03 / 20.05’e gider.",
        "<b>Zeytinde üç yol vardır.</b> Salamurada geçici konserve ve hemen yenmeye elverişsiz zeytin 07.11; soda çözeltisinde işlenip veya uzun süre salamurada yatırılıp yenilir hale getirilen zeytin 20.05; sirkeli zeytin 20.01.",
        "<b>Dondurulmuş hazır sebze 20.04’tür.</b> Yağda tamamen veya kısmen pişirilip dondurulan parmak patates ve tereyağı veya sosla ambalajlanmış dondurulmuş bezelye 20.04’te; aynı ürünler dondurulmamışsa 20.05’te.",
        "<b>Domates suyunda %7 eşiği.</b> Kuru ağırlık muhteviyatı %7 ve fazlası olan domates suyu 20.02’de; daha az olan 20.09’da.",
        "<b>Meyve suyu ile içecek ayrımı.</b> Doğal oranı aşan su eklenmiş veya normalden fazla karbondioksitli meyve suyu ve limonata 22.02; alkolü hacimce %0,5’i aşan meyve suyu Fasıl 22.",
        "<b>Reçel 20.07, 20.08 değil.</b> Pişirilerek hazırlanmış reçel, jöle, marmelat, püre ve pastlar 20.07’de; şekerleme veya çikolata mamulü haline getirilmişse 17.04 veya 18.06.",
        "<b>Kavrulmuş fındık ve fıstık ezmesi Fasıl 8 veya 12’de değil.</b> Kavrulmuş veya yağda kavrulmuş sert kabuklu meyve ve yer fıstığı ile fıstık ezmesi 20.08’dedir.",
        "<b>Sos ile turşu ayrımı.</b> Sıvı, emülsiyon veya süspansiyon halinde, tek başına yenmeyip yemeğe eşlik eden müstahzar 21.03; sirkeyle hazırlanmış sebze 20.01.",
        "<b>Patates unu tableti 20.05, kızartılmış çerez 19.05.</b> Derin kızartmayla cips yapılacak patates unu tabletleri 20.05’te; tüketime hazır kızartılmış baharatlı gevrek çerezler 19.05’te."
    ],
    "hafiza": {
        "kanca": "SİRKE – DOMATES – MANTAR – DON – DİĞER – ŞEKER – REÇEL – MEYVE – SU",
        "aciklama": "<b>Sirke</b> 20.01 · <b>Domates</b> 20.02 · <b>Mantar</b> 20.03 · <b>Don</b>durulmuş diğer sebze 20.04 · <b>Diğer</b> sebze 20.05 · <b>Şeker</b>le konserve 20.06 · <b>Reçel</b> 20.07 · <b>Meyve</b> hazırlıkları 20.08 · <b>Su</b>lar 20.09. Sıra mantığı: önce sirke yöntemi, sonra tek tek sebzeler, sonra şeker ve reçel, en sonda meyve ve sular."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az sayıda ve çoğunlukla seçeneklerde, özellikle eşleştirme sorularında yer almıştır.",
        "Reçelin pozisyonu: “hangi eşleştirme yanlıştır” kalıbında reçelin 20.08 ile eşleştirilmesi; doğrusu pişirilerek hazırlanan ürünlerin pozisyonu 20.07’dir.",
        "Alkolsüz içecek sınırı: 22.02 için hacimce %0,5 alkol eşiğinin sorulması; aynı eşik 20.09 meyve suları için Fasıl 20 Not 6’da tekrarlanır.",
        "Alt ayrımlarda kullanılan ölçütlerin (şeker oranı, ilave alkol, Brix değeri) sorulduğu kalıplar; Brix tanımı yalnız meyve suları için alt pozisyon notunda yer alır.",
        "Fasıl 20’nin Bölüm IV’te, taze ve kurutulmuş sebze ve meyvelerin ise Bölüm II’de (Fasıl 7–8) yer aldığının bölüm kapsamı sorularında kullanılması."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre ürün ve sınıflandırıldığı tarife pozisyonu ile ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?",
            "secenekler": ["Yumurta sarısı 04.08", "Buğday unu 11.01", "Kuskus 19.02", "Reçel 20.08", "Et suyu 21.04"],
            "cevap": "D",
            "aciklama": "Reçel, pişirilerek hazırlanmış bir meyve müstahzarı olarak 20.07 pozisyon metninde açıkça sayılmıştır. 20.08 ise başka yerde belirtilmeyen veya yer almayan, başka surette hazırlanmış meyve ve sert kabuklu meyvelerin tamamlayıcı pozisyonudur."
        }
    ],
    "ozet": [
        "Hazırlık Fasıl 7, 8 veya 11 işlemlerini aşıyorsa Fasıl 20; aşmıyorsa o fasıllarda kalır.",
        "Sirke veya asetik asit → 20.01; yöntem ürün türünden önce gelir.",
        "Domates 20.02, mantar 20.03; diğer sebze dondurulmuşsa 20.04, değilse 20.05.",
        "Şekerle konserve (glase, kristalize) 20.06; şurupta meyve 20.08.",
        "Reçel, jöle, marmelat, püre ve pastlar 20.07; kavrulmuş kuruyemiş, fıstık ezmesi, şurupta meyve 20.08.",
        "Sular 20.09: fermente değil, alkol %0,5’i geçmez; seyreltilmiş içecek 22.02, kuru maddesi %7+ domates suyu 20.02."
    ],
    "sorular": []
}

Q = obj["sorular"]

# 1
Q.append(S("E4",
    "Tarife Cetveline göre, sirke ile hazırlanmış ve kavanoza konulmuş kornişon turşusu hangi pozisyonda sınıflandırılır?",
    ["07.11", "20.01", "20.05", "21.03", "22.09"], "B",
    "20.01 pozisyonu sirke veya asetik asitle hazırlanmış veya konserve edilmiş sebzeleri kapsar ve Açıklama Notu hıyar ve kornişonları başlıca ürünler arasında sayar. 07.11 yalnız geçici olarak konserve edilmiş ve hemen yenmeye elverişsiz sebzeler, 20.05 sirke dışı yöntemle hazırlanan diğer sebzeler, 21.03 tek başına yenmeyen soslar, 22.09 ise sirkenin kendisi içindir.",
    "20.01 Açıklama Notu; Fasıl 20 Not 3."))
# 2
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 20. Faslında <b>sınıflandırılmaz</b>?",
    ["Kuru kavrulmuş ve tuzlanmış yer fıstığı",
     "Soda çözeltisinde işlenerek yenilir hale getirilmiş zeytin",
     "Osmotik dehidrasyon yoluyla konserve edilmiş meyve",
     "Hamur kabuğu içinde fırında pişirilmiş elmalı tart",
     "Fermente edilmemiş Hindistan cevizi suyu"], "D",
    "Fasıl 20 Genel Açıklamaları, meyve tartları gibi pastacılıkta hazırlanan ürünleri fasıl dışında bırakır (19.05); Not 1(d) de 19.05’teki ekmekçilik mamullerini hariç tutar. Kavrulmuş yer fıstığı ve osmotik dehidrasyonla konserve meyve 20.08’de, soda çözeltisinde işlenmiş zeytin 20.05’te, Hindistan cevizi suyu 20.09’dadır.",
    "Fasıl 20 Not 1(d); Fasıl 20 Genel Açıklamalar; 20.05, 20.08, 20.09 Açıklama Notları."))
# 3
Q.append(S("TN",
    "Tarife Cetvelinin 20. Fasıl notlarına göre, domates suyunun 20.09 yerine 20.02 pozisyonunda sınıflandırılmasında esas alınan ölçüt aşağıdakilerden hangisidir?",
    ["Kuru ağırlık muhteviyatının %7 ve daha fazla olması",
     "Brix değerinin 20’yi geçmesi ve şeker katılmamış olması",
     "Alkol derecesinin hacimce %0,5’i geçmesi",
     "Net ağırlığı 250 gr’ı geçmeyen kaplarda sunulması",
     "Kuru ağırlık muhteviyatının %20’den fazla olması"], "A",
    "Fasıl 20 Not 4’e göre kuru ağırlık muhteviyatı %7 ve daha fazla olan domates suları 20.02’de yer alır; 20.09 Açıklama Notu da bunları hariç tutar. Brix değeri meyve sularının alt ayrımına, %0,5 alkol eşiği Fasıl 22 ile sınıra, 250 gr ise homojenize ürünlerin alt pozisyon tanımına ilişkindir.",
    "Fasıl 20 Not 4; 20.02 ve 20.09 Açıklama Notları."))
# 4
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
    ["Çilek reçeli",
     "Portakal marmelatı",
     "Pişirilerek koyulaştırılmış ayva pastı",
     "Sorbitolle tatlandırılmış kayısı reçeli",
     "Şurup içinde konserve edilmiş şeftali dilimleri"], "E",
    "Reçel, marmelat ve meyve pastları pişirilerek hazırlandıkları için 20.07’dedir; Açıklama Notuna göre şeker yerine sorbitol gibi tatlandırıcı kullanılması bunu değiştirmez. Şurup içinde konserve edilmiş meyve ise 20.08 Açıklama Notunda sayılır.",
    "Fasıl 20 Not 5; 20.07 ve 20.08 Açıklama Notları."))
# 5
Q.append(S("E4",
    "Tarife Cetveline göre, yağda kısmen pişirildikten sonra dondurulmuş parmak patates (French fries) hangi pozisyonda sınıflandırılır?",
    ["07.10", "20.05", "20.04", "19.05", "11.05"], "C",
    "20.04 Açıklama Notu, yağda tamamen veya kısmen pişirilip sonra dondurulmuş patatesleri bu pozisyonun örnekleri arasında sayar. Yağda pişirme Fasıl 7 işlemi olmadığından 07.10’a girmez; ürün dondurulmuş olduğu için 20.05’e de girmez.",
    "Fasıl 20 Not 1(a) ve Not 3; 20.04 Açıklama Notu."))
# 6
Q.append(S("SN",
    "Bir ürün, kabuğu soyulmuş ve çekirdekleri çıkarılmış şeftalilerin ezilip sterilize edilmesiyle elde edilmiştir. Ürüne bir miktar şeker şurubu eklenmiş, ancak eklenen miktar ürünü doğrudan içecek olarak tüketilebilir hale getirmeye yetmemektedir. Ürün teneke kutularda sunulmaktadır. Bu ürün hangi pozisyonda sınıflandırılır?",
    ["20.09", "22.02", "20.07", "08.11", "20.08"], "E",
    "20.08 Açıklama Notu, içecek olarak doğrudan tüketim için yeterli olmayacak oranda su veya şeker şurubu içeren, ezilmiş ve sterilize edilmiş bütün meyveleri bu pozisyona alır; yeterli su veya şurup eklenip içilmeye hazır hale getirilirse 22.02’ye gider. Ürün meyve suyu (20.09) değildir; viskoziteyi artırmak için pişirilmediğinden 20.07’ye de girmez.",
    "20.08 Açıklama Notu; Fasıl 20 Not 5."))
# 7
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 20.09 pozisyonunda <b>yer almaz</b>?",
    ["Fermente olmamış, konsantre edilmiş üzüm şırası",
     "Doğal oranın üzerinde su eklenerek seyreltilmiş elma suyu içeceği",
     "Suda tamamen çözünen toz halindeki portakal suyu",
     "Tuz ve baharat eklenmiş havuç suyu",
     "Kuru eriğin suyla saatlerce ısıtılmasıyla elde edilen kuru erik suyu"], "B",
    "20.09 Açıklama Notuna göre normal meyve suyuna doğal suyu oluşturacak miktardan fazla su eklenmesiyle elde edilen seyreltilmiş ürünler 22.02’deki içeceklerin karakterini taşır. Fermente olmamış üzüm şırası (konsantre olabilir), tamamen çözünen toz meyve suyu, tuz ve baharatlı sebze suyu ve kuru erik suyu 20.09’da sayılmıştır.",
    "20.09 Açıklama Notu."))
# 8
Q.append(S("TN",
    "Tarife Cetvelinin 20. Fasıl notlarına göre, 20.09 pozisyonu anlamında “fermente edilmemiş ve ilave alkol katılmamış sular” tabirinden hangisi anlaşılır?",
    ["Alkol derecesi hacim itibariyle %0,5’i geçmeyen sular",
     "Alkol derecesi hacim itibariyle %1,2’yi geçmeyen sular",
     "Hiç alkol içermeyen, alkol derecesi sıfır olan sular",
     "Alkol derecesi ağırlık itibariyle %0,5’i geçmeyen sular",
     "Alkol derecesi hacim itibariyle %0,2’yi geçmeyen sular"], "A",
    "Fasıl 20 Not 6, bu tabirden alkol derecesi hacim itibariyle %0,5’i geçmeyen suları anlar; alkol derecesi Fasıl 22 Not 2 uyarınca 20 °C’de tespit edilir. Ölçüt ağırlık değil hacimdir (D); sıfır alkol şartı aranmaz (C).",
    "Fasıl 20 Not 6; Fasıl 22 Not 2."))
# 9
Q.append(S("FA",
    "Aşağıdaki seçeneklerin hangisinde sayılan eşyanın <b>tamamı</b> 20.08 pozisyonunda yer alır?",
    ["Yer fıstığı ezmesi – çilek reçeli – tuzlu kavrulmuş badem",
     "Şurupta ananas – kristalize kiraz – kavrulmuş fındık",
     "Konserve palmiye içi – sirkeli kapari – şurupta zencefil kökü",
     "Kavrulmuş yer fıstığı – şurupta kayısı – sterilize meyve pulpu",
     "Şurupta şeftali – meyve jölesi – yer fıstığı ezmesi"], "D",
    "Kavrulmuş yer fıstığı, şurupta konserve meyve ve sterilize edilmiş meyve pulpu 20.08 Açıklama Notunda sayılmıştır. Diğer gruplarda reçel ve meyve jölesi 20.07’ye, kristalize kiraz 20.06’ya, sirkeli kapari 20.01’e gider.",
    "20.08 Açıklama Notu; 20.01, 20.06, 20.07 pozisyon metinleri."))
# 10
Q.append(S("GYK",
    "Genel Yorum Kurallarının açıklama notlarına göre; 16.02 pozisyonundaki çöreğin içinde sığır etinden oluşan sandviç ile 20.04 pozisyonundaki patates cipslerinin (french fries) birlikte ambalajlanmasıyla oluşan perakende takım nasıl sınıflandırılır?",
    ["GYK 3(c) uyarınca 20.04 pozisyonunda",
     "Her ürün ayrı ayrı kendi pozisyonunda",
     "GYK 3(b) uyarınca 16.02 pozisyonunda",
     "GYK 3(b) uyarınca 20.04 pozisyonunda",
     "GYK 2(a) uyarınca 19.05 pozisyonunda"], "C",
    "GYK 3(b) Açıklama Notu bu takımı perakende satılacak hale getirilmiş takım örneği olarak verir ve 16.02’de sınıflandırır: ürünler farklı pozisyonlara girer, bir öğün için birlikte paketlenmiştir ve asli niteliği sandviç verir. Patates cipsi 20.04 ürünü olsa da takımın esas niteliğini belirlemez; 3(c) ancak 3(b) yetersiz kalırsa uygulanır.",
    "GYK 3(b) Açıklama Notu (X)."))
# 11
Q.append(S("E4",
    "Tarife Cetveline göre, kavrulmuş yer fıstığının öğütülmesiyle elde edilen ve tuz katılmış yer fıstığı ezmesi hangi pozisyonda sınıflandırılır?",
    ["20.08", "12.02", "20.07", "15.08", "21.06"], "A",
    "20.08 Açıklama Notu “yer fıstığı ezmesi”ni (tuz veya yağ katılmış olsun olmasın) kavrulmuş yer fıstığının öğütülmesiyle yapılan bir macun olarak açıkça sayar. 12.02 kavrulmamış yer fıstığını, 15.08 yer fıstığı yağını kapsar; 20.07’deki pastlar pişirilerek koyulaştırılmış meyve ürünleridir.",
    "20.08 Açıklama Notu."))
# 12
Q.append(S("CC",
    "Tarife Cetveline göre zeytinle ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Sirke veya asetik asitle hazırlanmış zeytin 20.01 pozisyonunda yer alır. II. Salamurada yalnızca geçici olarak konserve edilmiş, bu haliyle hemen yenmeye elverişli olmayan zeytin 20.05 pozisyonunda yer alır. III. Soda çözeltisinde özel işleme tabi tutularak yenilir hale getirilmiş zeytin 20.05 pozisyonunda yer alır. IV. 20.05’teki zeytinler konuldukları kabın tipine göre farklı pozisyonlarda sınıflandırılır.",
    ["I ve II", "II ve IV", "I, II ve III", "I ve III", "III ve IV"], "D",
    "Sirkeli zeytin 20.01’de (I doğru), soda çözeltisinde veya uzun süre salamurada işlenerek yenilir hale getirilen zeytin 20.05’tedir (III doğru). Salamurada yalnız geçici olarak konserve edilmiş zeytin 07.11’dedir (II yanlış). 20.05 Açıklama Notuna göre ürünler kap tipine bakılmaksızın bu pozisyonda yer alır (IV yanlış).",
    "20.01 ve 20.05 Açıklama Notları; Fasıl 20 Not 1(a)."))
# 13
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
    ["Tereyağlı sosla ambalajlanmış dondurulmuş bezelye",
     "Az miktarda şeker katılmış kurutulmuş incir",
     "Suyu alınmış ve şekerle parlatılmış (glase) kestane",
     "Şeker şurubundaki demir hindi meyvesi",
     "Konserve edilmiş tatlı mısır daneleri"], "B",
    "20.06 Açıklama Notuna göre kurutulmuş meyveler (incir, erik gibi) az miktarda şeker katılmış olsalar bile Fasıl 8’de sınıflandırılır. Tereyağlı dondurulmuş bezelye 20.04, glase kestane 20.06, şurupta demir hindi 20.08, konserve tatlı mısır 20.05 ile Fasıl 20’dedir.",
    "20.04, 20.05, 20.06, 20.08 Açıklama Notları."))
# 14
Q.append(S("TN",
    "Tarife Cetvelinin 20. Fasıl notlarına göre, 20.07 pozisyonu anlamında “pişirilerek elde edilmiş” tabiri için aşağıdakilerden hangisi <b>doğrudur</b>?",
    ["Ürünün yalnızca atmosfer basıncında kaynatılmasıyla elde edilmesi anlaşılır.",
     "Ürünün en az kendi ağırlığı kadar şekerle birlikte kaynatılması anlaşılır.",
     "Ürünün sterilize edilerek mikroorganizmalardan arındırılması anlaşılır.",
     "Ürünün su içeriğinin dondurularak kurutma ile azaltılması anlaşılır.",
     "Viskoziteyi artırmak için normal veya düşük basınçta ısıl işlem anlaşılır."], "E",
    "Fasıl 20 Not 5’e göre bu tabir, su içeriğinin azaltılması veya diğer yöntemlerle viskozitenin artırılması için ürünün atmosfer basıncında veya düşürülmüş basınç altında ısıl işleme tabi tutulmasıdır; yalnız atmosfer basıncı şartı yoktur (A). Şekerle eşit ağırlıkta kaynatma reçelin tarifidir, notun tanımı değildir (B).",
    "Fasıl 20 Not 5; 20.07 Açıklama Notu."))
# 15
Q.append(S("ES",
    "Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
    ["Domates ketçabı – 20.02",
     "Jelatin, şeker ve meyve esansından sofralık jöle – 20.07",
     "Konserve domalan – 20.03",
     "Kristalize portakal kabuğu – 20.08",
     "Kuru maddesi %5 olan domates suyu – 20.02"], "C",
    "20.03 mantarlar ile birlikte domalanları da kapsar (sirke dışı yöntemle hazırlananlar). Domates ketçabı 21.03’te, jelatinli sofralık jöle 21.06’da, kristalize meyve kabuğu 20.06’da, kuru maddesi %7’nin altındaki domates suyu 20.09’dadır.",
    "20.02, 20.03, 20.06, 20.07 Açıklama Notları; Fasıl 20 Not 4."))
# 16
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 20.06 pozisyonunda <b>sınıflandırılmaz</b>?",
    ["Şekerle konserve edilmiş, suyu alınmış kiraz",
     "Şurup içinde konserve edilmiş kestane (marrons glacés)",
     "Sakkaroz şurubuna daldırılıp parlak tabakayla kaplanmış armut",
     "Kristalize edilmiş menekşe çiçekleri",
     "Şekerle konserve edilmiş ağaç kavunu kabuğu"], "B",
    "20.06 Açıklama Notu, ne şekilde paketlenmiş olursa olsun şurup içinde konserve edilen meyveleri (marrons glacés, zencefil gibi) hariç tutar ve 20.08’e gönderir. Suyu alınmış, glase (parlak) ve kristalize ürünler ile meyve kabukları ve çiçekler 20.06’dadır.",
    "20.06 ve 20.08 Açıklama Notları."))
# 17
Q.append(S("E4",
    "Tarife Cetveline göre, havuç ve bezelyeden oluşan, sterilize edilmiş, dondurulmamış ve hava geçirmez kutularda sunulan sebze karışımı (sirke kullanılmamış) hangi pozisyonda sınıflandırılır?",
    ["07.12", "20.04", "21.04", "07.10", "20.05"], "E",
    "Konserve edilmiş, dondurulmamış ve sirke kullanılmamış sebzeler (karışımlar ve salatalar dahil) kap tipine bakılmaksızın 20.05’tedir. Dondurulmuş olsaydı 20.04’e girerdi; 21.04 Açıklama Notu da çorba yapımında kullanılsalar bile konserve sebze karışımlarını hariç tutar.",
    "Fasıl 20 Not 3; 20.05 Açıklama Notu; 21.04 Açıklama Notu, hariç tutmalar."))
# 18
Q.append(S("FA",
    "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
    ["Domates salçası",
     "Domates püresi",
     "Kuru ağırlık muhteviyatı %8 olan domates suyu",
     "Domates, şeker, sirke, tuz ve baharattan yapılmış ketçap",
     "Teneke kutuda, kendi suyunda parça halinde domates konservesi"], "D",
    "Domates ketçabı ve diğer domates sosları 20.02 Açıklama Notunda hariç tutulmuş ve 21.03’e gönderilmiştir. Salça, püre, kuru maddesi %7 ve üzeri domates suyu ve parça domates konservesi 20.02’dedir.",
    "Fasıl 20 Not 4; 20.02 Açıklama Notu; 21.03 Açıklama Notu."))
# 19
Q.append(S("GYK",
    "Tarifenin Yorumuna İlişkin Genel Kurallar açısından aşağıdakilerden hangisi <b>doğrudur</b>?",
    ["Kuru maddesi %7 ve üzeri domates suyu, Fasıl 20 Not 4 ile GYK 1 uyarınca 20.02’dedir.",
     "Domates suyu hem 20.02 hem 20.09’a girebildiğinden GYK 3(c) uyarınca 20.09’da sınıflandırılır.",
     "Domates suyu sıvı olduğundan GYK 4 uyarınca en çok benzediği 22.02’deki içeceklerle sınıflandırılır.",
     "Kuru maddesi %7’yi aşan domates suyu GYK 3(b) uyarınca asli niteliğine göre 20.09’da sınıflandırılır.",
     "GYK 2(a) eksik veya bitirilmemiş eşya kuralı, Fasıl 20 ürünlerine normal olarak uygulanır."], "A",
    "GYK 1’e göre sınıflandırma öncelikle pozisyon metinleri ve fasıl notlarıyla yapılır; Fasıl 20 Not 4 bu domates sularını açıkça 20.02’ye verdiğinden 3. veya 4. kurallara gerek yoktur. GYK 2(a) Açıklama Notu, kuralın bu kısmının I–VI. Bölümlere giren eşyaya normal olarak uygulanmadığını belirtir (E).",
    "GYK 1; GYK 2(a) Açıklama Notu (III); Fasıl 20 Not 4."))
# 20
Q.append(S("TN",
    "Tarife Cetvelinin 20. Fasıl notlarına göre; Not 1(a)’daki usullerden başka şekilde hazırlanmış veya konserve edilmiş olmak şartıyla 20.01, 20.04 ve 20.05 pozisyonları hangi ürünleri kapsar?",
    ["Fasıl 7, 8 ve 12’deki ürünleri",
     "Fasıl 7’deki ürünler ile 11.01 ve 11.02’deki unları",
     "Fasıl 7 ürünleri ile 11.05 veya 11.06 ürünlerini (Fasıl 8 unları hariç)",
     "Yalnızca Fasıl 8’deki meyve ve sert kabuklu meyveleri",
     "Fasıl 7’deki ürünler ile Fasıl 8 ürünlerinin un, kaba un ve tozlarını"], "C",
    "Fasıl 20 Not 3’e göre bu pozisyonlar, duruma göre, yalnız Fasıl 7 ürünlerini veya 11.05 ya da 11.06 pozisyonlarındaki ürünleri kapsar; 8. Fasıl ürünlerinin unları, kaba unları ve tozları bu kapsamdan açıkça hariç tutulmuştur (E’deki tuzak). Meyveler bu pozisyonlarda değil 20.06–20.08’de değerlendirilir.",
    "Fasıl 20 Not 3."))
# 21
Q.append(S("OT",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 20.05 pozisyonunda <b>yer almaz</b>?",
    ["Tuzlanmış lahananın kısmen fermantasyonuyla hazırlanan sauerkraut",
     "Kızartılarak cips yapılmak üzere patates unundan yapılmış ince tabletler",
     "Domates sosu içinde konserve edilmiş fasulye",
     "Önceden pişirilmiş, dondurulmuş havuç ve bezelye karışımı",
     "Teneke kutuya konulmuş kuşkonmaz konservesi"], "D",
    "20.04 Açıklama Notu, önceden pişirilmiş veya pişirilmemiş dondurulmuş tatlı mısır, havuç, bezelye vb. ürünleri 20.04’e alır; 20.05 başlığı “dondurulmamış” sebzelerle sınırlıdır. Sauerkraut, patates unu tabletleri, domates soslu fasulye ve kuşkonmaz konservesi 20.05’tedir.",
    "20.04 ve 20.05 Açıklama Notları; Fasıl 20 Not 3."))
# 22
Q.append(S("CC",
    "Tarife Cetveline göre aşağıdakilerden hangileri 20. Fasıl <b>dışında</b> kalır? I. Ağırlıkça %25 kıyma içeren sebzeli konserve yemek II. Şekerleme haline getirilmiş meyve jölesi III. Fermente edilmemiş Hindistan cevizi suyu IV. Tuz katılmış yer fıstığı ezmesi",
    ["I ve II", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"], "A",
    "Ağırlıkça %20’den fazla et içeren gıda müstahzarı Not 1(c) gereği Fasıl 16’ya (I), şeker mamulü haline getirilmiş meyve jölesi Not 2 gereği 17.04’e gider (II). Hindistan cevizi suyu 20.09 metninde, yer fıstığı ezmesi 20.08 Açıklama Notunda sayıldığından fasıl içindedir.",
    "Fasıl 20 Not 1(c) ve Not 2; 20.08 ve 20.09 Açıklama Notları."))
# 23
Q.append(S("ES",
    "Tarife Cetveline göre; kristalize kiraz (I), şurup içinde konserve kiraz (II), kiraz reçeli (III), fermente edilmemiş ve alkol katılmamış kiraz suyu ise (IV) pozisyonunda sınıflandırılır. Boşlukları sırasıyla dolduran seçenek hangisidir?",
    ["20.08 / 20.06 / 20.07 / 20.09",
     "20.06 / 20.06 / 20.07 / 22.02",
     "20.06 / 20.08 / 20.08 / 20.09",
     "20.07 / 20.08 / 20.07 / 20.09",
     "20.06 / 20.08 / 20.07 / 20.09"], "E",
    "Kristalize meyve şekerle konserve edildiğinden 20.06’da; şurup içindeki meyve 20.06’dan hariç tutulup 20.08’e gönderilir. Reçel pişirilerek hazırlandığı için 20.07’de, fermente edilmemiş ve alkol katılmamış meyve suyu 20.09’dadır.",
    "20.06, 20.07, 20.08, 20.09 Açıklama Notları."))
# 24
Q.append(S("SN",
    "Bir ürün; fermente olmamış konsantre limon suyuna, toplam asit miktarını doğal meyve suyundakinden önemli ölçüde yüksek kılacak oranda sitrik asit ve meyve uçucu yağı eklenerek hazırlanmıştır. Ürün, su ile seyreltilerek içecek hazırlanmasında kullanılmaktadır. Bu ürün hangi pozisyonda sınıflandırılır?",
    ["20.09", "21.06", "22.02", "33.02", "20.08"], "B",
    "20.09 Açıklama Notuna göre eklenen madde (sitrik asit, uçucu yağ vb.) doğal meyve suyundaki dengeyi kesin olarak bozuyorsa ürün orijinal karakterini kaybeder ve pozisyon dışında kalır. 21.06 Açıklama Notu, bu şekilde sitrik asit ve uçucu meyve yağı katılmış konsantre meyve suyunu içecek imalinde kullanılan müstahzarlar arasında sayar. Ürün içilmeye hazır olmadığından 22.02’ye, esası koku verici madde olmadığından 33.02’ye girmez.",
    "20.09 Açıklama Notu; 21.06 Açıklama Notu."))
# 25
Q.append(S("E4",
    "Tarife Cetveline göre, fermente edilmemiş ve alkol katılmamış, kristal halde sunulan ve ince fırıncılık ürünlerinde kullanılan, piyasada “üzüm şekeri” veya “üzüm balı” olarak bilinen üzüm şırası hangi pozisyonda sınıflandırılır?",
    ["17.02", "22.04", "20.09", "04.09", "17.04"], "C",
    "20.09 Açıklama Notu, fermente olmamak şartıyla her türlü kullanım için olan üzüm şırasını kapsar ve konsantre veya kristal halde sunulabileceğini, kristal formun “üzüm şekeri” veya “üzüm balı” olarak bilindiğini belirtir. Adındaki “şeker” ve “bal” kelimeleri 17.02 veya 04.09’a götürmez; alkol derecesi %0,5’i aşan şıra ise 22.04’tedir.",
    "20.09 Açıklama Notu; 22.04 Açıklama Notu (Üzüm şırası)."))

kaydet(obj, 20)
