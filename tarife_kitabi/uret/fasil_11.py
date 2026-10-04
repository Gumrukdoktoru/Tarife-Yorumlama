import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_09_13 import *  # noqa: F401,F403

d = {
 "tur": "fasil",
 "fasil": 11,
 "baslik": "Değirmencilik ürünleri; malt; nişasta; inulin; buğday gluteni",
 "bolum": "II",
 "oz": {
  "vurgu": "Fasıl 11; Fasıl 10 hububatının (ve tatlı mısırın) değirmencilik ürünlerini, malt, nişasta, inulin ve buğday glutenini, ayrıca patates, kuru baklagil, kök-yumru ve Fasıl 8 meyvelerinin unlarını kapsar. Hububat ürünlerinde karar zinciri sayısaldır: önce nişasta ve kül (Fasıl 11 mi, 23.02 mi?), sonra un eleği (11.01/11.02 mi?), sonra Not 3 eleği (11.03 mü, 11.04 mü?).",
  "maddeler": [
   "Kuru madde üzerinden nişasta %45’ten fazla ve kül tablodaki sınırı aşmıyorsa ürün Fasıl 11’dedir; aksi halde 23.02 (hububat embriyoları daima 11.04).",
   "Un: 315 mikrometre elekten en az %80 geçen ürün (mısır ve tane darıda 500 mikrometre elekten en az %90); buğday-mahlut 11.01, diğerleri 11.02.",
   "Daha ileri işlem faslı değiştirir: hazırlanmış unlar ve malt ekstraktı 19.01, mısır gevreği ve işlenmiş tane halindeki bulgur 19.04, dekstrin ve modifiye nişasta 35.05.",
   "Pirinç ve kinoa işlenmiş olsa da Fasıl 10’da kalır; diğer hububatın işlenmiş taneleri 11.04’tedir."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Fasıl 11 Not 1’de hariç tutulan bir ürün mü? (kahve yerine kavrulmuş malt, hazırlanmış un, mısır gevreği, hazırlanmış sebze, ilaç, kozmetik nişasta)", "<b>09.01</b>/<b>21.01</b> · <b>19.01</b> · <b>19.04</b> · Fasıl 20 · Fasıl 30 · Fasıl 33"],
   ["2", "Nişasta veya inulin mi?", "<b>11.08</b> (dekstrin ve modifiye nişasta <b>35.05</b>)"],
   ["3", "Buğday gluteni mi?", "<b>11.09</b>"],
   ["4", "Malt mı? (kavrulmuş veya öğütülmüş dahil)", "<b>11.07</b> (malt ekstraktı <b>19.01</b>)"],
   ["5", "Patatesten elde edilmiş un, kaba un, toz, flokon, granül veya pellet mi?", "<b>11.05</b> (basitçe kurutulmuş patates <b>07.12</b>)"],
   ["6", "Kuru baklagil, sagu, kök-yumru veya Fasıl 8 meyvesinin unu mu?", "<b>11.06</b>"],
   ["7", "Hububat değirmencilik ürünü nişasta ve kül şartını sağlamıyor mu?*", "<b>23.02</b> (hububat embriyoları daima <b>11.04</b>)"],
   ["8", "Not 2(B) eleğinden yeterli oranda geçiyor mu?", "Buğday-mahlut <b>11.01</b> · diğer hububat <b>11.02</b>"],
   ["9", "Not 3 eleğinden (mısırda 2 mm, diğerlerinde 1,25 mm) en az %95 geçiyor mu veya pellet mi?", "<b>11.03</b>"],
   ["10", "Kabuğu çıkarılmış, yassılaştırılmış, flokon, yuvarlatılmış, dilimlenmiş, iri parçalı tane veya embriyo mu?", "<b>11.04</b> (pirinç <b>10.06</b>, kinoa <b>10.08</b>)"]
  ],
  "dipnot": "* Not 2(A) tablosu (kuru ürün üzerinden, ağırlıkça): nişasta tüm hububatta %45’ten fazla; kül en çok buğday ve çavdar %2,5 · arpa %3 · yulaf %5 · mısır ve tane darı %2 · pirinç %1,6 · karabuğday %4. Un eleği: mısır ve tane darıda 500 mikrometre %90, diğerlerinde 315 mikrometre %80."
 },
 "pozisyon_haritasi": [
  ["11.01", "Buğday veya mahlut unu", "Not 2 şartları + 315 mikrometre elekten en az %80", "Ekmeklik buğday unu, gluten katkılı un"],
  ["11.02", "Diğer hububat unları", "Mısır ve tane darıda 500 mikrometre elekten en az %90", "Mısır unu, pirinç unu, çavdar unu"],
  ["11.03", "Kabaca öğütülmüş küçük parçalar, kaba un (irmik), pellet", "Not 3 eleği: mısır 2 mm, diğer 1,25 mm, en az %95", "Durum buğdayı irmiği, mısır kaba unu"],
  ["11.04", "Diğer şekilde işlenmiş taneler; hububat embriyoları", "Kabuğu çıkarılmış, yassı, flokon, yuvarlatılmış, yarma", "Yassılaştırılmış yulaf, yarma, buğday embriyosu"],
  ["11.05", "Patates unu, kaba unu, tozu, flokonu, granülü, pelleti", "Pişirilip püre yapılıp kurutulmuş patates", "Patates flokonu, patates granülü"],
  ["11.06", "Kuru baklagil, sagu, kök-yumru ve Fasıl 8 ürünlerinin unları", "Soya unu (12.08) ve keçiboynuzu unu (12.12) hariç", "Mercimek unu, kestane unu, muz unu"],
  ["11.07", "Malt (kavrulmuş olsun olmasın)", "Filizlendirilmiş tane; malt ekstraktı hariç", "Bira maltı, renk maltı, malt unu"],
  ["11.08", "Nişastalar; inulin", "Parmaklar arasında gıcırdar; modifiye nişasta hariç", "Mısır, buğday, patates, manyok nişastası"],
  ["11.09", "Buğday gluteni (kurutulmuş olsun olmasın)", "Nişastanın su ile ayrılmasıyla elde edilir", "Kuru gluten tozu, nemli gluten"]
 ],
 "notlar": [
  ["Bölüm II Notu", "“Pellet”: doğrudan sıkıştırılarak veya ağırlığının <b>%3</b>’ünü geçmeyen oranda bağlayıcı ilavesiyle küçük topaklar halinde bir araya getirilen ürünler (11.03 ve 11.05 pelletleri)."],
  ["Fasıl 11 Not 1", "Hariç: kahve yerine kullanılan kavrulmuş malt (09.01 veya 21.01); 19.01’deki hazırlanmış unlar, kabaca öğütülmüş küçük parçalar, kaba unlar ve nişastalar; 19.04’teki mısır gevreği ve diğer ürünler; 20.01, 20.04 veya 20.05’teki hazırlanmış veya konserve sebzeler; eczacılık ürünleri (Fasıl 30); parfümeri, kozmetik veya tuvalet ürünü karakterindeki nişastalar (Fasıl 33)."],
  ["Fasıl 11 Not 2(A)", "Tablodaki hububatın değirmencilik ürünleri, kuru ürün üzerinden ağırlıkça nişasta oranı (2) numaralı sütundakinden <b>fazla</b> ve kül miktarı (katılmış mineral maddeler hariç) (3) numaralı sütundakinden <b>fazla değilse</b> bu fasıldadır; aksi halde 23.02. Bütün, yuvarlatılmış, flokon veya öğütülmüş hububat embriyoları <b>daima 11.04</b>."],
  ["Fasıl 11 Not 2(A) tablosu", "Nişasta: tüm hububatta %45. Kül: buğday ve çavdar %2,5 · arpa %3 · yulaf %5 · mısır ve tane darı %2 · pirinç %1,6 · karabuğday %4."],
  ["Fasıl 11 Not 2(B)", "Not 2(A)’ya göre fasla giren ürünler, tablodaki elekten geçen miktar ağırlıkça belirtilen orandan az değilse 11.01 veya 11.02’de, aksi halde 11.03 veya 11.04’te yer alır. Elek: buğday, çavdar, arpa, yulaf, pirinç ve karabuğdayda 315 mikrometre elekten <b>%80</b>; mısır ve tane darıda 500 mikrometre elekten <b>%90</b>."],
  ["Fasıl 11 Not 3", "11.03’te “kabaca öğütülerek elde edilen küçük parçalar” ve “kaba un”: mısır ürünlerinde göz büyüklüğü <b>2 mm</b>, diğer hububat ürünlerinde <b>1,25 mm</b> olan elekten ağırlıkça en az <b>%95</b> geçen ürünler."],
  ["Genel Açıklamalar", "Fasıl; Fasıl 10 tahıllarının ve Fasıl 7’deki tatlı mısırın değirmencilik ürünlerini, nişasta veya gluten çıkarma ya da malt haline getirme gibi işlemlerle elde edilen ürünleri ve kuru baklagil, patates, meyve gibi diğer fasıl hammaddelerinden benzer işlemlerle elde edilen ürünleri kapsar. Hariç: hububat kapçıkları 12.13; tapyoka 19.03; işlenmiş tane halindeki bulgur 19.04; değirmencilik kalıntıları 23.02."],
  ["11.01 Açıklama Notu", "Çok az miktarda mineral fosfat, antioksidan, emülsifiye edici, vitamin veya kabartma tozu katılmış (kendi kendine kabaran) unlar, genel olarak <b>%10</b>’u geçmeyecek şekilde gluten katılmış buğday unları ve ön jelatinize unlar 11.01’de kalır. Kakaolu unlar: yağı tamamen alınmış baz üzerinden ağırlıkça <b>%40</b> veya daha fazla kakao 18.06, daha az 19.01."],
  ["11.04 Açıklama Notu", "Yassılaştırılmış veya flokon taneler; kavuzu çıkarılmış yulaf, karabuğday ve darı; yuvarlatılmış taneler; iri parçalar halinde ufalanmış taneler (yarma); hububat embriyoları. Hariç: pirinç 10.06; kinoa 10.08; tabii kavuzsuz yulaf 10.04; işlenmiş taneler halindeki bulgur 19.04; embriyo yağı çıkarımı artıkları 23.06."],
  ["11.05 Açıklama Notu", "Basitçe kurutulmuş, dehidrate edilmiş veya buharlaştırılmış patates 07.12’de; patates nişastası 11.08’de; patates nişastasından tapyoka ikameleri 19.03’te."],
  ["11.06 Açıklama Notu", "Bezelye, fasulye, mercimek unları; sagu ve manyok gibi kök-yumru unları; kestane, badem, hurma, muz, Hindistan cevizi, demirhindi unları ve meyve kabuğu unları. Hariç: yağı alınmamış soya unu 12.08; keçiboynuzu unu 12.12; pellet halindeki kök-yumru unları ve sagu özü 07.14; tapyoka 19.03."],
  ["11.07 Açıklama Notu", "Malt: filizlendirilmiş ve genellikle sıcak havalı fırınlarda kurutulmuş tane (çoğunlukla arpa); bütün, öğütülmüş, malt unu ve biraları renklendirmede kullanılan kavrulmuş malt dahil. Hariç: malt ekstraktı 19.01; kahve yerine kullanılan kavrulmuş malt 21.01."],
  ["11.08 Açıklama Notu", "Nişasta parmaklar arasında gıcırdar ve iyotla genellikle koyu mavi renk verir; inulin açık sarımsı kahverengi verir. Hariç: tapyoka 19.03; kozmetik nişastalar Fasıl 33; dekstrin ve diğer modifiye nişastalar 35.05; nişasta esaslı zamklar 35.05 veya 35.06; müstahzar haşıl ve apreler 38.09; amilopektin ve amiloz 39.13."],
  ["11.09 Açıklama Notu", "Gluten, buğday ununda bulunan nişasta vb. maddelerin su ile ayrılmasıyla elde edilir. Hariç: gluten katılmış buğday unu 11.01; buğday gluteninden elde edilen proteinler 35.04; tutkal veya apre olarak hazırlanmış gluten 35.06 veya 38.09."]
 ],
 "sinir_komsulari": [
  ["Kepek ve diğer değirmencilik kalıntıları (nişasta-kül şartını sağlamayan)", "23.02", "Fasıl 11 Not 2(A)"],
  ["Hububat kapçıkları", "12.13", "Değirmencilik ürünü değil"],
  ["Kavuzu çıkarılmış, parlatılmış veya kırık pirinç; perikarpı alınmış kinoa", "10.06 / 10.08", "Fasıl 10 Not 1(B) istisnası"],
  ["Hazırlanmış unlar; malt ekstraktı", "19.01", "Fasıl 11 Not 1; 11.07 hariç tutması"],
  ["Kakaolu un (yağsız bazda %40 ve üzeri kakao)", "18.06", "11.01 hariç tutması"],
  ["Tapyoka ve tapyoka ikameleri", "19.03", "Nişastadan hazırlanmış gıda"],
  ["Mısır gevreği, kabartılmış pirinç, işlenmiş tane halinde bulgur", "19.04", "Fasıl 11 Not 1; Genel Açıklamalar"],
  ["Kahve yerine kullanılan kavrulmuş malt", "09.01 / 21.01", "Fasıl 11 Not 1"],
  ["Basitçe kurutulmuş patates", "07.12", "11.05 hariç tutması"],
  ["Yağı alınmamış soya unu", "12.08", "Yağlı tohum unu; 11.06 hariç tutması"],
  ["Keçiboynuzu unu", "12.12", "11.06 hariç tutması"],
  ["Dekstrin ve diğer modifiye nişastalar", "35.05", "11.08 hariç tutması"],
  ["Buğday gluteninden elde edilen proteinler", "35.04", "11.09 hariç tutması"],
  ["Kozmetik ürünü karakterindeki nişasta", "Fasıl 33", "Fasıl 11 Not 1"],
  ["Hububat embriyosu yağının çıkarılmasından kalan artık", "23.06", "11.04 Açıklama Notu"]
 ],
 "tuzaklar": [
  "<b>Sıra şaşmaz: önce nişasta ve kül, sonra elek.</b> Nişasta %45’i aşmıyorsa veya kül tablodaki sınırı aşıyorsa ürün un görünse de 23.02’dedir; elek testine hiç geçilmez.",
  "<b>Embriyo, kalıntı testinden muaftır.</b> Bütün, yuvarlatılmış, flokon veya öğütülmüş hububat embriyoları nişasta ve kül sonucuna bakılmaksızın daima 11.04’tedir.",
  "<b>Mısırın eleği farklıdır.</b> Mısır ve tane darıda un için 500 mikrometre elekten %90, diğerlerinde 315 mikrometre elekten %80 aranır; Not 3’te de mısırda 2 mm, diğerlerinde 1,25 mm elek kullanılır.",
  "<b>Mahlut unu 11.01’dedir.</b> 11.02 “buğday unu veya mahlut unu hariç” diğer hububat unlarını kapsar.",
  "<b>İki “bulgur” vardır.</b> Not 3’teki “kabaca öğütülerek elde edilen küçük parçalar (bulgur)” 11.03’tedir; işlenmiş taneler halindeki bulgur ise 19.04’e gider.",
  "<b>Malt üç yere dağılır.</b> Malt ve biraları renklendiren kavrulmuş malt 11.07; malt ekstraktı 19.01; kahve yerine kullanılan kavrulmuş malt 09.01 veya 21.01.",
  "<b>Un ile nişasta karıştırılmaz.</b> Patates unu 11.05, patates nişastası 11.08; “sagu unu” da denilen sagu nişastası 11.08, sagu unu 11.06. Nişasta parmaklar arasında gıcırdar, un gıcırdamaz.",
  "<b>Modifiye nişasta Fasıl 11’de değildir.</b> Dekstrin ve diğer modifiye nişastalar 35.05’te, nişastadan hazırlanan tapyoka 19.03’tedir.",
  "<b>Her un 11.06 değildir.</b> Yağı alınmamış soya unu 12.08 (yağlı tohum unu), keçiboynuzu unu 12.12, pellet halindeki manyok unu 07.14.",
  "<b>Küçük katkılar unu değiştirmez.</b> Vitamin, mineral fosfat, kabartma tozu ve (genel olarak %10’a kadar) gluten katılmış un 11.01’de kalır; gıda müstahzarı karakteri kazanırsa 19.01’e gider."
 ],
 "hafiza": {
  "kanca": "BU-Dİ-İR-İŞ  /  PA-BA-MA-Nİ-GLU",
  "aciklama": "<b>BU</b>ğday ve mahlut unu 11.01 · <b>Dİ</b>ğer hububat unları 11.02 · <b>İR</b>mik, kırma ve pellet 11.03 · <b>İŞ</b>lenmiş tane ve embriyo 11.04 · <b>PA</b>tates 11.05 · <b>BA</b>klagil, sagu ve meyve unları 11.06 · <b>MA</b>lt 11.07 · <b>Nİ</b>şasta ve inulin 11.08 · <b>GLU</b>ten 11.09. Hububatta üç kapı vardır: nişasta-kül kapısı (23.02 mi?), un eleği (11.01/11.02 mi?), irmik eleği (11.03 mü, 11.04 mü?)."
 },
 "sinav_odagi": [
  "Fasıl 11 çıkmış sorularda az sayıda yer almıştır; doğrudan soru, fasılda sınıflandırma için kullanılan ölçütler üzerinedir: nişasta oranı, kül oranı, elekten geçme oranı ve hububatın cinsi kullanılır, şeker oranı kullanılmaz (“hangisi kullanılan bilgilerden değildir” kalıbı).",
  "Ürün–pozisyon eşleştirme sorularında buğday ununun 11.01’de olduğu doğru eşleştirme olarak verilmiş; yumurta sarısı, kuskus, reçel ve et suyu gibi farklı fasıl ürünleriyle birlikte sorulmuştur.",
  "Kırık hububat tanelerinin (buğday, arpa, mısır, çavdar) Fasıl 10’da kalmayıp değirmencilik ürünü olarak işlem gördüğü, kırık pirincin ise 10.06’da kaldığı bilgisi sınanmıştır.",
  "Bölüm II fasıl başlıkları sorusunda bitkisel ürünler bölümüne ait olmayan başlığın (Fasıl 21) seçilmesi istenmiştir; Fasıl 11 gibi işlenmiş bitkisel ürün fasıllarının Bölüm II’de, gıda müstahzarlarının Bölüm IV’te olduğu ayrımı önemlidir."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 11. fasılda sınıflandırma için kullanılan bilgilerden <b>değildir</b>?",
   "secenekler": ["Nişasta oranı", "Kül oranı", "Şeker oranı", "Elekten geçme oranı", "Hububatın cinsi"],
   "cevap": "C",
   "aciklama": "Fasıl 11 Not 2’deki tablo, hububatın cinsine göre nişasta oranı, kül oranı ve elekten geçme oranı ölçütlerini kullanır; Not 3 de bir elek ölçütüdür. Şeker oranı Fasıl 11 notlarında yer almaz."
  },
  {
   "soru": "Tarife Cetveline göre ürün ve sınıflandırıldığı tarife pozisyonu ile ilgili aşağıdaki eşleştirmelerden hangisi <b>yanlıştır</b>?",
   "secenekler": ["Yumurta sarısı – 04.08", "Buğday unu – 11.01", "Kuskus – 19.02", "Reçel – 20.08", "Et suyu – 21.04"],
   "cevap": "D",
   "aciklama": "Reçel, pişirilerek hazırlanan meyve müstahzarı olarak 20.07’dedir; 20.08 başka yerde belirtilmeyen meyve hazırlıklarını kapsar. Buğday unu 11.01, yumurta sarısı 04.08, kuskus 19.02, et suyu 21.04 doğru eşleştirmelerdir."
  }
 ],
 "ozet": [
  "Fasıl 11 = hububatın değirmencilik ürünleri + malt + nişasta ve inulin + buğday gluteni + patates, baklagil, kök-yumru ve meyve unları.",
  "Kapı 1: nişasta %45’i aşmıyor veya kül tablodaki sınırı aşıyorsa 23.02 (embriyo daima 11.04).",
  "Kapı 2: un eleği (315 mikrometre %80; mısır ve tane darıda 500 mikrometre %90) → buğday-mahlut 11.01, diğerleri 11.02.",
  "Kapı 3: Not 3 eleği (mısırda 2 mm, diğerlerinde 1,25 mm, en az %95) → 11.03; değilse işlenmiş tane 11.04.",
  "Daha ileri işlem faslı değiştirir: hazırlanmış un ve malt ekstraktı 19.01, mısır gevreği 19.04, modifiye nişasta 35.05.",
  "Pirinç ve kinoa işlenmiş olsa da Fasıl 10’da kalır; soya unu 12.08, keçiboynuzu unu 12.12."
 ]
}

S = {}
# ---- Eşya → 4’lü pozisyon
S["E1"] = Q(T_ES,
 "Tarife Cetveline göre, 07.13 pozisyonuna giren kurutulmuş bezelyelerin öğütülmesiyle elde edilen ve çorba yapımında kullanılan un hangi pozisyonda sınıflandırılır?",
 "11.06", ["11.02", "07.13", "11.05", "21.04"], "D",
 "11.06, 07.13 pozisyonuna giren kuru baklagillerin un, kaba un ve tozlarını kapsar; bezelye, fasulye ve mercimek unları bu pozisyondadır. 11.02 yalnızca Fasıl 10 hububatının unlarını, 11.05 patates ürünlerini kapsar. Sebze unu esaslı hazır çorbalar ise 21.04’tedir; unun çorba yapımında kullanılması onu çorba yapmaz.",
 "11.06 pozisyon metni ve Açıklama Notu.")
S["E2"] = Q(T_ES,
 "Tarife Cetveline göre patates nişastası hangi pozisyonda sınıflandırılır?",
 "11.08", ["11.05", "11.06", "35.05", "19.03"], "B",
 "11.08 nişastaları kapsar; patates nişastası 11.05 Açıklama Notunda açıkça 11.08’e gönderilmiştir. 11.05 ise patates unu, kaba unu, tozu, flokonu, granülü ve pelletlerini kapsar. Dekstrin ve modifiye nişastalar 35.05’te, patates nişastasından hazırlanan tapyoka ikameleri 19.03’tedir.",
 "11.05 ve 11.08 Açıklama Notları.")
S["E3"] = Q(T_ES,
 "Tarife Cetveline göre, biraları renklendirmede kullanılan kavrulmuş malt hangi pozisyonda sınıflandırılır?",
 "11.07", ["21.01", "19.01", "23.03", "09.01"], "E",
 "11.07 pozisyon metni maltı “kavrulmuş olsun olmasın” kapsar; Açıklama Notu biraları renklendirmede kullanılan kavrulmuş maltı örnek verir. Kahve yerine kullanılan kavrulmuş malt ise Fasıl 11 Not 1 uyarınca 09.01 veya 21.01’e, malt ekstraktı 19.01’e, malt filizleri 23.03’e gider. Kavrulmuş olmak tek başına faslı değiştirmez; kahve ikamesi olarak kullanılmak değiştirir.",
 "11.07 pozisyon metni ve Açıklama Notu; Fasıl 11 Not 1.")
S["E4"] = Q(T_ES,
 "Tarife Cetveline göre, buharla ısıtılıp sıcak silindirler arasında yassılaştırılarak flokon haline getirilmiş, pişirilmiş müstahzar niteliği taşımayan yulaf taneleri hangi pozisyonda sınıflandırılır?",
 "11.04", ["10.04", "11.03", "19.04", "11.02"], "A",
 "11.04 yassılaştırılmış veya flokon halindeki taneleri kapsar; bu işlemde tane genellikle buharla ısıtılır veya sıcak silindirler arasında yassılaştırılır. İşlenmiş tane olduğu için 10.04’te kalamaz (Fasıl 10 Not 1(B)). “Mısır gevreği” tipindeki tüketime hazır pişirilmiş kahvaltılıklar ise 19.04’tedir.",
 "11.04 pozisyon metni ve Açıklama Notu; Fasıl 10 Not 1(B).")
S["E5"] = Q(T_ES,
 "Tarife Cetveline göre, buğday ununun yapısındaki nişastanın su ile ayrılmasıyla elde edilen, kurutulmuş, krem renkli toz halindeki buğday gluteni hangi pozisyonda sınıflandırılır?",
 "11.09", ["35.04", "11.01", "35.06", "11.08"], "C",
 "11.09 buğday glutenini kurutulmuş olsun olmasın kapsar; gluten nemli (macun) veya kuru (krem renkli toz) olabilir. Buğday gluteninden elde edilmiş proteinler 35.04’te, tutkal olarak kullanılmak üzere hazırlanmış gluten 35.06’da, gluten ile zenginleştirilmiş buğday unu 11.01’dedir.",
 "11.09 pozisyon metni ve Açıklama Notu.")
# ---- Olumsuz teşhis
S["O1"] = Q(T_OL,
 "Aşağıdakilerden hangisi Tarife Cetvelinin 11. faslında <b>sınıflandırılmaz</b>?",
 "Dekstrin",
 ["Malt unu", "Hindiba köklerinden elde edilen inulin", "Muz unu", "Öğütülmüş hububat embriyosu"], "E",
 "Dekstrinler ve diğer modifiye nişastalar 11.08’den hariç tutulmuş ve 35.05’e gönderilmiştir. Malt unu 11.07’de, inulin 11.08’de, muz unu (Fasıl 8 ürünü) 11.06’da, öğütülmüş hububat embriyosu 11.04’tedir.",
 "11.08 Açıklama Notu; 11.04, 11.06, 11.07 Açıklama Notları.")
S["O2"] = Q(T_OL,
 "Aşağıdakilerden hangisi 11.06 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Yağı alınmamış soya unu",
 ["Mercimek unu", "Kestane unu", "Manyok kökü unu", "Badem unu"], "C",
 "11.06 Açıklama Notu yağı alınmamış soya ununu hariç tutar; bu ürün yağlı tohum unu olarak 12.08’dedir. Mercimek unu (kuru baklagil), manyok unu (07.14 kökleri), kestane ve badem unları (Fasıl 8 ürünleri) 11.06’dadır. Tuzak, soyayı kuru baklagil saymaktır.",
 "11.06 Açıklama Notu; Fasıl 12 Not 2.")
S["O3"] = Q(T_OL,
 "Aşağıdakilerden hangisi 11.08 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Nişastadan hazırlanmış tapyoka",
 ["Buğday nişastası", "Mısır nişastası", "Manyok nişastası", "İnulin"], "A",
 "Nişastadan hazırlanan tapyoka ve tapyoka ikameleri 11.08’den hariç tutulmuş ve 19.03’e gönderilmiştir. Buğday, mısır ve manyok nişastaları ile yer elması, dahlia ve hindiba köklerinden elde edilen inulin 11.08’dedir.",
 "11.08 pozisyon metni ve Açıklama Notu.")
S["O4"] = Q(T_OL,
 "Aşağıdakilerden hangisi 11.05 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Daha ileri işlem görmeden basitçe kurutulmuş patates dilimleri",
 ["Patates unu", "Patates flokonları", "Patates granülleri", "Patates pelletleri"], "D",
 "11.05 Açıklama Notu, daha ileri bir işleme tabi tutulmadan basitçe kurutulmuş, dehidrate edilmiş veya buharlaştırılmış patatesleri hariç tutar; bunlar 07.12’dedir. Patates unu, flokonu, granülü ve pelleti 11.05 pozisyon metninde sayılmıştır.",
 "11.05 pozisyon metni ve Açıklama Notu.")
# ---- Farklı/aynı
S["F1"] = Q(T_FA,
 "Aşağıdaki unlardan hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
 "Mahlut unu", ["Çavdar unu", "Mısır unu", "Pirinç unu", "Arpa unu"], "B",
 "11.01 buğday unu veya mahlut ununu kapsar; 11.02 ise “buğday unu veya mahlut unu hariç” diğer hububat unlarını kapsar. Çavdar, mısır, pirinç ve arpa unları 11.02’de, mahlut unu 11.01’dedir. Tuzak, mahlutun içindeki çavdar nedeniyle 11.02’yi seçmektir.",
 "11.01 ve 11.02 pozisyon metinleri.")
S["F2"] = Q(T_FA,
 "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
 "Malt ekstraktı", ["Malt", "Buğday gluteni", "Pirinç nişastası", "Patates pelleti"], "E",
 "Malt ekstraktı ve esasını malt ekstraktı oluşturan gıda müstahzarları 11.07’den hariç tutulmuş ve 19.01’e gönderilmiştir. Malt 11.07’de, buğday gluteni 11.09’da, pirinç nişastası 11.08’de, patates pelleti 11.05’te, yani Fasıl 11’dedir.",
 "11.07 Açıklama Notu.")
S["F3"] = Q(T_FA,
 "Aşağıdaki ikililerden hangisinde yer alan ürünler aynı tarife pozisyonunda sınıflandırılır?",
 "Hububat embriyosu – Yassılaştırılmış arpa",
 ["Buğday unu – Mısır unu", "Durum buğdayı irmiği – Yarma", "Patates unu – Patates nişastası", "Malt – Malt ekstraktı"], "A",
 "Hububat embriyoları ve yassılaştırılmış taneler 11.04’tedir. Buğday unu 11.01 / mısır unu 11.02; irmik (kaba un) 11.03 / yarma (iri parçalar halinde ufalanmış tane) 11.04; patates unu 11.05 / patates nişastası 11.08; malt 11.07 / malt ekstraktı 19.01.",
 "11.01–11.08 pozisyon metinleri; 11.04 ve 11.07 Açıklama Notları.")
S["F4"] = Q(T_FA,
 "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
 "Yuvarlatılmış arpa",
 ["Buğday irmiği", "Mısır kaba unu", "Hububat pelletleri", "Buğdayın kabaca öğütülmesinden elde edilen küçük parçalar"], "D",
 "Yuvarlatılmış taneler (genellikle arpa; perikarpı pratikte tamamen çıkarılmış ve uçları yuvarlatılmış) 11.04’tedir. Hububat kaba unları (irmik), kabaca öğütülmüş küçük parçalar ve hububat pelletleri 11.03 pozisyon metninde sayılmıştır.",
 "11.03 ve 11.04 pozisyon metinleri ve Açıklama Notları.")
# ---- Fasıl notu
S["N1"] = Q(T_NO,
 "Fasıl 11 Not 2(A)’ya göre, tablodaki hububat cinslerinin değirmencilik ürünlerinin bu fasılda yer alabilmesi için kuru ürün üzerinden ağırlık itibariyle nişasta oranı hangi değerden fazla olmalıdır?",
 "%45", ["%25", "%35", "%55", "%80"], "C",
 "Not 2(A) tablosunun (2) numaralı sütununda nişasta oranı bütün hububat cinsleri için %45 olarak verilmiştir; nişasta bu değerden fazla ve kül oranı (3) numaralı sütundaki değerden fazla değilse ürün Fasıl 11’de, aksi halde 23.02’dedir. %80, 315 mikrometre elekten geçme oranıdır; tuzak budur.",
 "Fasıl 11 Not 2(A) ve tablo.")
S["N2"] = Q(T_NO,
 "Fasıl 11 Not 2(A) tablosuna göre aşağıdaki hububat cinsi – azami kül oranı eşleştirmelerinden hangisi <b>doğrudur</b>?",
 "Pirinç – %1,6", ["Yulaf – %2", "Mısır – %3", "Buğday – %4", "Arpa – %5"], "B",
 "Tabloya göre kül oranı sınırları şöyledir: buğday ve çavdar %2,5; arpa %3; yulaf %5; mısır ve tane darı %2; pirinç %1,6; karabuğday %4. Bu sınırı aşan değirmencilik ürünleri 23.02’ye gider. Diğer seçeneklerde cinslerin değerleri birbirine karıştırılmıştır.",
 "Fasıl 11 Not 2(A) tablosu.")
S["N3"] = Q(T_NO,
 "Fasıl 11 Not 2(B)’ye göre mısır ve tane darıdan elde edilen değirmencilik ürünlerinin 11.02’de un olarak sınıflandırılabilmesi için hangi elek ölçütünü sağlaması gerekir?",
 "Göz büyüklüğü 500 mikrometre olan elekten ağırlıkça en az %90 geçmesi",
 ["Göz büyüklüğü 315 mikrometre olan elekten ağırlıkça en az %80 geçmesi",
  "Göz büyüklüğü 2 mm olan elekten ağırlıkça en az %95 geçmesi",
  "Göz büyüklüğü 1,25 mm olan elekten ağırlıkça en az %95 geçmesi",
  "Göz büyüklüğü 500 mikrometre olan elekten ağırlıkça en az %80 geçmesi"], "A",
 "Not 2(B) tablosunda mısır ve tane darı için yalnız (5) numaralı sütun doldurulmuştur: 500 mikrometre elekten en az %90. Diğer hububat için 315 mikrometre elekten en az %80 aranır. 2 mm ve 1,25 mm elekler ise Not 3’te 11.03’teki kaba un ve küçük parçalar için kullanılır.",
 "Fasıl 11 Not 2(B) ve tablo; Fasıl 11 Not 3.")
S["N4"] = Q(T_NO,
 "Fasıl 11 Not 2(A) ile ilgili aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
 "Şartları karşılamayan ürünler 23.02’de sınıflandırılır; ancak hububat embriyoları daima 11.04’tedir.",
 ["Şartları karşılamayan ürünler 11.04’te, hububat embriyoları ise 23.02’de sınıflandırılır.",
  "Nişasta oranı kuru madde üzerinden değil, ürünün kendi ağırlığı üzerinden hesaplanır.",
  "Kül miktarına ürüne sonradan katılmış mineral maddeler de dahil edilir.",
  "Nişasta oranı tablodakinden az olan ürünler elek ölçütünü sağlıyorsa 11.01 veya 11.02’de kalır."], "E",
 "Not 2(A)’ya göre nişasta ve kül oranları kuru ürün üzerinden hesaplanır, kül miktarından katılmış mineral maddelere ait kısım çıkarılır. Şartları sağlamayan ürünler 23.02’ye gider ve elek testine geçilmez. Bütün, yuvarlatılmış, flokon veya öğütülmüş hububat embriyoları ise bu sonuçtan bağımsız olarak daima 11.04’tedir.",
 "Fasıl 11 Not 2(A).")
# ---- GYK
S["G1"] = Q(T_GY,
 "Genel Yorum Kuralı 2(a)’ya ilişkin Açıklama Notuna göre aşağıdakilerden hangisi <b>doğrudur</b>?",
 "GYK 2(a), I–VI. Bölümlere ait pozisyonlardaki eşyaya normal olarak uygulanmaz.",
 ["GYK 2(a), yalnızca I–VI. Bölümlerdeki eşyaya uygulanır.",
  "GYK 2(a), değirmencilik ürünlerinin karışımlarını sınıflandırmak için kullanılır.",
  "GYK 2(a), bir fasıl notunda belirtilen karışımlara GYK 1’den önce uygulanır.",
  "GYK 2(a) uyarınca öğütülmemiş hububat, un gibi sınıflandırılır."], "D",
 "GYK 2(a) Açıklama Notu, hem bitirilmemiş eşya hem de birleştirilmemiş veya demonte eşya bakımından kuralın I ila VI. Bölümlere ait pozisyonlardaki eşyaya normal olarak uygulanmadığını belirtir; Fasıl 11 Bölüm II’dedir. Karışımlar 2(a) ile değil 2(b) ve 3 ile ilgilidir; notta belirtilen hazır karışımlar ise GYK 1’e göre sınıflandırılır.",
 "GYK 2(a) Açıklama Notu (III) ve (IX); GYK 2(b) Açıklama Notu (X).")
S["G2"] = Q(T_GY,
 "Bir değirmencilik ürününün 11.01’de mi yoksa 23.02’de mi sınıflandırılacağı Fasıl 11 Not 2(A)’daki nişasta ve kül ölçütlerine göre belirlenmektedir. Bu belirleme hangi Genel Yorum Kuralı çerçevesinde yapılır?",
 "GYK 1 – pozisyon metinleri ve fasıl notlarına göre",
 ["GYK 3(a) – eşyayı en özel tanımlayan pozisyona göre",
  "GYK 3(b) – eşyaya esas niteliğini veren maddeye göre",
  "GYK 3(c) – numara sırasına göre son pozisyona göre",
  "GYK 4 – eşyaya en çok benzeyen eşyaya göre"], "B",
 "GYK 1’e göre sınıflandırma pozisyon metinlerine ve bölüm veya fasıl notlarına göre yapılır; Fasıl 11 Not 2(A) ölçütleri doğrudan bir not hükmüdür. Notla çözülen durumda GYK 3’e veya GYK 4’e başvurulmaz. 23.02’nin numara olarak sonra gelmesi 3(c) için bir gerekçe değildir.",
 "GYK 1; Fasıl 11 Not 2(A).")
# ---- Eşleştirme / Boşluk
S["B1"] = Q(T_EB,
 "Fasıl 11 Not 3’e göre 11.03 anlamında “kabaca öğütülerek elde edilen küçük parçalar” ve “kaba un”; mısır ürünlerinde göz büyüklüğü …… olan, diğer hububat ürünlerinde ise …… olan elekten ağırlık itibariyle en az …… geçen ürünlerdir. Boşluklara sırasıyla gelmesi gerekenler hangisidir?",
 "2 mm – 1,25 mm – %95",
 ["1,25 mm – 2 mm – %95", "500 mikrometre – 315 mikrometre – %90", "2 mm – 1,25 mm – %80", "315 mikrometre – 500 mikrometre – %80"], "C",
 "Not 3’e göre mısırda 2 mm, diğer hububatta 1,25 mm göz büyüklüğündeki elekten ağırlıkça en az %95 geçen ürünler 11.03’teki küçük parçalar ve kaba unlardır. 315 ve 500 mikrometre elekler ile %80 ve %90 oranları ise Not 2(B)’de unu belirlemek için kullanılır; iki not karıştırılmamalıdır.",
 "Fasıl 11 Not 3; Fasıl 11 Not 2(B).")
S["B2"] = Q(T_EB,
 "Aşağıdaki ürünleri sınıflandırıldıkları pozisyonlarla eşleştiriniz. I. Malt ekstraktı  II. Mısır gevreği (corn flakes)  III. Dekstrin  IV. Hububat kapçıkları — a. 12.13  b. 19.01  c. 19.04  d. 35.05",
 "I-b, II-c, III-d, IV-a",
 ["I-c, II-b, III-d, IV-a", "I-b, II-c, III-a, IV-d", "I-d, II-c, III-b, IV-a", "I-b, II-a, III-d, IV-c"], "D",
 "Malt ekstraktı 19.01’de (11.07 hariç tutması), mısır gevreği 19.04’te (Fasıl 11 Not 1), dekstrin 35.05’te (11.08 hariç tutması), hububat kapçıkları 12.13’tedir (Fasıl 11 Genel Açıklamalar). Dördü de Fasıl 11 ürünlerine benzeyen ama fasıl dışında kalan eşyadır.",
 "Fasıl 11 Not 1; Fasıl 11 Genel Açıklamalar; 11.07 ve 11.08 Açıklama Notları.")
# ---- Çoktan-çoğa
S["C1"] = Q(T_CC,
 "11.01 Açıklama Notuna göre aşağıdakilerden hangileri 11.01 pozisyonunda kalır? I. Çok az miktarda vitamin ve mineral fosfat katılmış buğday unu  II. Hazırlanmış kabartma tozu katılmış, kendi kendine kabaran buğday unu  III. Nişastası ön jelatinize edilmiş (kabartılmış) buğday unu  IV. Yağı tamamen alınmış baz üzerinden ağırlıkça %40 kakao içeren buğday unu",
 "I, II ve III", ["I ve II", "I, II ve IV", "II, III ve IV", "I, III ve IV"], "B",
 "11.01 Açıklama Notuna göre çok az miktarda mineral fosfat, antioksidan, emülsifiye edici, vitamin veya hazırlanmış kabartma tozu katılmış unlar ve ön jelatinize edilmiş unlar 11.01’de kalır (I, II, III). Yağı tamamen alınmış baz üzerinden ağırlıkça %40 veya daha fazla kakao içeren unlar 18.06’dadır (IV).",
 "11.01 Açıklama Notu.")
S["C2"] = Q(T_CC,
 "Aşağıdakilerden hangileri Tarife Cetvelinin 11. faslı dışında kalır? I. Kahve yerine kullanılan kavrulmuş malt  II. Parfümeri veya kozmetik ürünü karakterine sahip nişasta  III. Öğütülmüş hububat embriyosu  IV. Tapyoka",
 "I, II ve IV", ["I ve II", "II ve III", "I ve IV", "I, II ve III"], "E",
 "Fasıl 11 Not 1 kahve yerine kullanılan kavrulmuş maltı (09.01 veya 21.01) ve kozmetik karakterli nişastaları (Fasıl 33) fasıl dışında bırakır; tapyoka da Genel Açıklamalara göre 19.03’tedir (I, II, IV). Öğütülmüş hububat embriyoları ise Not 2(A) uyarınca daima 11.04’tedir (III).",
 "Fasıl 11 Not 1 ve Not 2(A); Fasıl 11 Genel Açıklamalar.")
# ---- Senaryo
S["S1"] = Q(T_SE,
 "Bir buğday değirmencilik ürününün analiz sonuçları şöyledir: kuru madde üzerinden ağırlıkça nişasta %70, kül %1,8; göz büyüklüğü 315 mikrometre olan elekten ağırlıkça %85’i geçmektedir. Ürüne başka madde katılmamıştır. Eşya hangi pozisyonda sınıflandırılır?",
 "11.01", ["11.03", "11.04", "23.02", "11.02"], "C",
 "Buğday için tablo sınırları nişastada %45’ten fazla, külde en çok %2,5’tir; %70 nişasta ve %1,8 kül ile ürün Fasıl 11’e girer (23.02 değil). 315 mikrometre elekten geçen oran %85 olup %80’in altında olmadığından ürün un sayılır; buğday unu olduğu için 11.02 değil 11.01’dedir.",
 "Fasıl 11 Not 2(A) ve 2(B); 11.01 pozisyon metni.")
S["S2"] = Q(T_SE,
 "Bir mısır değirmencilik ürününün analiz sonuçları şöyledir: kuru madde üzerinden ağırlıkça nişasta %60, kül %1,5; göz büyüklüğü 500 mikrometre olan elekten ağırlıkça %40’ı, 2 mm olan elekten ise %97’si geçmektedir. Eşya hangi pozisyonda sınıflandırılır?",
 "11.03", ["11.02", "11.04", "23.02", "11.01"], "A",
 "Mısırda nişasta %45’ten fazla ve kül %2’yi aşmadığından ürün Fasıl 11’dedir. 500 mikrometre elekten geçen %40, aranan %90’ın altında olduğundan un (11.02) değildir. Not 3’e göre mısır ürünlerinde 2 mm elekten en az %95 geçen ürünler 11.03’teki küçük parçalar ve kaba unlardır; %97 bu şartı sağlar.",
 "Fasıl 11 Not 2(A), 2(B) ve Not 3.")

SIRA = ["E1", "N1", "O1", "F1", "E2", "B1", "G1", "O2", "C1", "F2", "N2", "E3", "S1",
        "O3", "F3", "B2", "N3", "O4", "E4", "C2", "G2", "E5", "N4", "F4", "S2"]
d["sorular"] = sirala(S, SIRA)
yaz(11, d)
