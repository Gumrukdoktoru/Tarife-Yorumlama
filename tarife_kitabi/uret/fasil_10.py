import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_09_13 import *  # noqa: F401,F403

d = {
 "tur": "fasil",
 "fasil": 10,
 "baslik": "Hububat",
 "bolum": "II",
 "oz": {
  "vurgu": "Fasıl 10 yalnızca tane halindeki hububatı kapsar; başak veya sap içinde olması fark etmez. Tane kavuzundan çıkarılmış veya başka şekilde işlenmişse Fasıl 11’e gider. Bu kuralın iki istisnası vardır: pirinç (kavuzu çıkarılmış, değirmenden geçirilmiş, parlatılmış, yarım kaynatılmış veya kırık) 10.06’da, saponini ayırmak için perikarpı alınmış kinoa 10.08’de kalır.",
  "maddeler": [
   "Taze hububat, sebze olarak kullanılmaya uygun olsa bile Fasıl 10’dadır; tek istisna tatlı mısırdır (Fasıl 7).",
   "Ekim amaçlı (tohumluk) hububat da Fasıl 10’da kalır; 12.09’a gitmez.",
   "Tane yapısını önemli ölçüde değiştiren işlemler (ön pişirme, şişirme) pirinci 19.04’e götürür.",
   "Darı ailesine dikkat: tane sorgum 10.07, cin ve kum darı 10.08, yem ve çayır darıları 12.14, tatlı darı 12.12, akdarı 14.04."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Tatlı mısır mı?", "Fasıl 7"],
   ["2", "Pirinç mi? (çeltik, kahverengi, beyaz, parlatılmış, perdahlanmış, yarı kaynatılmış, kırık, zenginleştirilmiş)", "<b>10.06</b> (ön pişirilmiş veya şişirilmiş <b>19.04</b>)"],
   ["3", "Kinoa mı? (saponini ayırmak için perikarpı alınmış, başka işlem görmemiş dahil)", "<b>10.08</b>"],
   ["4", "Diğer bir hububat tanesi kavuzundan çıkarılmış, yassılaştırılmış, kırılmış veya öğütülmüş mü?", "Fasıl 11 (<b>11.01</b> – <b>11.04</b>)"],
   ["5", "Filizlendirilmiş (malt) veya kahve yerine kullanılmak üzere kavrulmuş mu?", "Malt <b>11.07</b> · kavrulmuş arpa <b>21.01</b>"],
   ["6", "Yem veya çayır darısı, tatlı darı ya da akdarı mı?", "<b>12.14</b> / <b>12.12</b> / <b>14.04</b>"],
   ["7", "Mantar teşekkülüne açık çavdar (çavdar mahmuzu) mu?", "<b>12.11</b>"],
   ["8", "Tane halinde hububat mı? (başak veya sap içinde olsun olmasın)*", "Buğday-mahlut <b>10.01</b> · çavdar <b>10.02</b> · arpa <b>10.03</b> · yulaf <b>10.04</b> · mısır <b>10.05</b> · tane sorgum <b>10.07</b> · diğer <b>10.08</b>"]
  ],
  "dipnot": "* Ekim amaçlı tohumluk hububat da aynı pozisyonlarda kalır (Fasıl 12 Not 3). Olgunlaşmadan biçilmiş, kapçıklı taneler normal tanelerle birlikte sınıflandırılır."
 },
 "pozisyon_haritasi": [
  ["10.01", "Buğday ve mahlut", "Makarnalık (durum) ve adi buğday; mahlut = çavdar-buğday karışımı", "Durum buğdayı, kaplıca, tohumluk buğday"],
  ["10.02", "Çavdar", "Çavdar mahmuzu hariç (12.11)", "Çavdar tanesi"],
  ["10.03", "Arpa", "Kavuzlu bracteiferous ve tabii kavuzsuz arpa; malt hariç", "Yemlik arpa, maltlık arpa"],
  ["10.04", "Yulaf", "Kavuzlu veya tabii kavuzsuz; kavuzu çıkarılmışı 11.04", "Gri ve beyaz yulaf"],
  ["10.05", "Mısır", "Tatlı mısır hariç (Fasıl 7)", "Tohumluk mısır, dane mısır"],
  ["10.06", "Pirinç", "Kavuzlu, kahverengi, beyaz, kırık; ön pişirilmiş hariç", "Çeltik, kırık pirinç, yarı kaynatılmış pirinç"],
  ["10.07", "Koca darı (tane sorgum)", "İnsan tüketimine mahsus tane darı; yem darısı hariç", "Kafir, durra, kaoliang"],
  ["10.08", "Karabuğday, darı, kuş yemi; diğer hububat", "Kinoa istisnası; melez hububat", "Karabuğday, kuş yemi, triticale, fonio, kinoa"]
 ],
 "notlar": [
  ["Fasıl 10 Not 1(A)", "Bu fasıldaki ürünler ancak <b>tane halinde</b> iseler, başakları içinde veya saplarında olsun olmasın bu pozisyonlarda sınıflandırılır."],
  ["Fasıl 10 Not 1(B)", "Kavuzundan çıkarılmış veya başkaca işlenmiş hububat taneleri bu fasla dahil değildir. İstisnalar: kavuzu çıkarılmış, değirmenden geçirilmiş, parlatılmış, yarım kaynatılmış veya kırık pirinç <b>10.06</b>; saponini ayırmak için perikarpı tamamen veya kısmen çıkarılmış, fakat başka işlem görmemiş kinoa <b>10.08</b>."],
  ["Fasıl 10 Not 2", "10.05 pozisyonuna tatlı mısır dahil değildir (Fasıl 7)."],
  ["Genel Açıklamalar", "Olgunlaşmadan biçilen ve kapçıklı halde bulunan hububattan elde edilen taneler normal tanelerle birlikte sınıflandırılır. Taze hububat (Fasıl 7’deki tatlı mısır dışında) sebze olarak kullanılmaya uygun olsun olmasın Fasıl 10’dadır."],
  ["10.01 Açıklama Notu", "Kaplıca (harmandan sonra bile kapçıklı halde bulunan küçük kahverengi taneli buğday türü) 10.01’dedir. Mahlut: çavdarla buğdayın genellikle 2’ye 1 oranında karışımı."],
  ["10.02 Açıklama Notu", "Mantar teşekkülüne açık çavdar mahmuzu (ergot) bu pozisyona dahil değildir (12.11)."],
  ["10.03 Açıklama Notu", "Kavuzları taneye yapışık bracteiferous arpa kavuzlu halde 10.03’te; değirmende kabuğu çıkarılmışsa 11.04’te. Tabii haliyle kavuzsuz arpa, harman ve savurma dışında işlem görmemişse 10.03’tedir. Hariç: malt 11.07; kahve yerine kullanılan kavrulmuş arpa 21.01; malt filizleri ve diğer mayalama artıkları 23.03."],
  ["10.04 Açıklama Notu", "Kavuzlu yulaf ile harman ve savurma dışında işlem görmemiş tabii kavuzsuz yulaf; normal işleme ve dağıtım sırasında kavuz uçları dökülmüş yulaf da dahil."],
  ["10.06 Açıklama Notu", "Çeltik, kahverengi (kargo) pirinç, yarı veya tam değirmenden geçirilmiş pirinç; parlatılmış, perdahlanmış (talk ve glikoz ile kaplanmış), Camolino (ince yağ tabakasıyla kaplanmış), kırık, zenginleştirilmiş (yaklaşık %1 vitamin emdirilmiş taneler içeren) ve yarı kaynatılmış pirinç (tam pişirme 20–35 dakika). Ön pişirilmiş pirinç (kısmen ön pişirilmişte hazırlama 5–12 dakika) ve şişirilmiş pirinç 19.04."],
  ["10.07 Açıklama Notu", "Yalnız insan tüketimine mahsus hububat olarak kullanılabilen tane darılar (kafir, beyaz durra, kahverengi durra, kaoliang). Yem ve çayır darıları 12.14 (ekim tohumları 12.09), tatlı darılar 12.12, akdarı 14.04."],
  ["10.08 Açıklama Notu", "Karabuğday (Polygonaceae familyası; Gramineae değil), darı (cin ve kum darı; teff dahil), kuş yemi (parlak saman renginde, uzun ve iki ucu sivri tohumlar) ve diğer hububat (buğday-çavdar melezi triticale gibi melezler, fonio, kinoa)."],
  ["Fasıl 12 Not 3", "Hububat, ekilmeye mahsus olsa bile 12.09’da değil, Fasıl 10’da sınıflandırılır."]
 ],
 "sinir_komsulari": [
  ["Tatlı mısır", "Fasıl 7", "Fasıl 10 Not 2"],
  ["Kavuzu çıkarılmış yulaf, yassılaştırılmış arpa, yarma", "11.04", "Fasıl 10 Not 1(B): işlenmiş tane"],
  ["Kırık buğday, arpa, mısır, çavdar", "Fasıl 11", "Kırık tane istisnası yalnız pirince aittir"],
  ["Buğday unu; diğer hububat unları", "11.01 / 11.02", "Değirmencilik ürünü"],
  ["Malt (filizlendirilmiş arpa)", "11.07", "10.03 hariç tutması"],
  ["Kahve yerine kullanılan kavrulmuş arpa", "21.01", "10.03 hariç tutması"],
  ["Malt filizleri ve mayalama artıkları", "23.03", "10.03 hariç tutması"],
  ["Ön pişirilmiş pirinç; şişirilmiş pirinç; mısır gevreği", "19.04", "Tane yapısı önemli ölçüde değişmiş veya pişirilmiş"],
  ["Çavdar mahmuzu (ergot)", "12.11", "10.02 hariç tutması"],
  ["Yem darıları ve çayır darıları (halepense, sudanense)", "12.14", "10.07 hariç tutması"],
  ["Tatlı darı (saccharatum)", "12.12", "Şurup veya melas imalatında kullanılır"],
  ["Akdarı", "14.04", "10.07 hariç tutması"],
  ["Hububat sapları ve kapçıkları", "12.13", "Tane değil"],
  ["Fiğ, yonca (yem bitkisi)", "12.14", "Hububat değil, yem bitkisi"]
 ],
 "tuzaklar": [
  "<b>Kırık pirinç Fasıl 10’da kalır, diğer kırık taneler kalmaz.</b> Not 1(B) istisnası yalnız pirinç (ve perikarpı alınmış kinoa) içindir; kırık buğday, arpa, mısır veya çavdar Fasıl 11’e gider.",
  "<b>Tatlı mısır sebzedir.</b> Fasıl 7’dedir; buna karşılık sebze olarak tüketilmeye uygun diğer taze hububat Fasıl 10’da kalır.",
  "<b>Başak veya sap faslı değiştirmez.</b> Tane halindeki hububat başağı veya sapıyla sunulsa da Fasıl 10’dadır; tanesiz saplar ve kapçıklar ise 12.13’tedir.",
  "<b>Tohumluk hububat 12.09’a gitmez.</b> Fasıl 12 Not 3 hububatı 12.09’dan hariç tutar; tohumluk buğday 10.01’de, tohumluk mısır 10.05’te kalır.",
  "<b>Yarı kaynatılmış ≠ ön pişirilmiş.</b> Kavuzlu iken sıcak su veya buharla işlenip kurutulan pirinç (tam pişirme 20–35 dakika) 10.06; pişirilip suyu alınmış ön pişirilmiş pirinç 19.04.",
  "<b>Karabuğday buğday değildir.</b> Polygonaceae familyasındandır ve 10.08’de yer alır; mahlut ise buğdayla birlikte 10.01’dedir.",
  "<b>Her darı aynı yerde değildir.</b> Tane sorgum (kafir, durra, kaoliang) 10.07; cin ve kum darı 10.08; yem ve çayır darıları 12.14; tatlı darı 12.12; akdarı 14.04.",
  "<b>Arpanın kavuzu nasıl gitti?</b> Tabii kavuzsuz arpa ve kavuzlu bracteiferous arpa 10.03’te; değirmende kabuğu çıkarılan bracteiferous arpa 11.04’te.",
  "<b>Kuş yemi bir hububattır.</b> 10.08 pozisyon metninde sayılmıştır; “yem” kelimesi sizi 12.14’e veya Fasıl 23’e götürmesin.",
  "<b>Kaplıca 10.01’dedir.</b> Harmandan sonra da kapçıklı kalan bu buğday türü, kapçıklı olduğu için 12.13 veya 11.04 sayılmaz."
 ],
 "hafiza": {
  "kanca": "BU-ÇA-AR-YU-MI-Pİ-KO-KA",
  "aciklama": "<b>BU</b>ğday ve mahlut 10.01 · <b>ÇA</b>vdar 10.02 · <b>AR</b>pa 10.03 · <b>YU</b>laf 10.04 · <b>MI</b>sır 10.05 · <b>Pİ</b>rinç 10.06 · <b>KO</b>ca darı 10.07 · <b>KA</b>rabuğday, darı, kuş yemi ve diğerleri 10.08. Kural cümlesi: “Tane girer, işlenen çıkar; pirinçle kinoa kalır.”"
 },
 "sinav_odagi": [
  "Fasıl 10 çıkmış sorularda az sayıda doğrudan sorulmuştur; en belirgin konu Not 1(B)’deki pirinç istisnasıdır: “hangisi 10. fasılda sınıflandırılır?” sorusunda kırık buğday, arpa, mısır ve çavdar çeldirici, kırık pirinç doğru cevaptır.",
  "Fasıl 12 sorularında kuş yemi, mısır ve darı gibi Fasıl 10 hububatı çeldirici olarak kullanılmış; yem bitkisi olan fiğin (12.14) ayırt edilmesi istenmiştir.",
  "Fasıl–konu eşleştirmesi: “Hububat 10. fasılda yer alır” gibi ifadeler, farklı fasıllara ait doğru/yanlış önermeler arasında verilmiştir.",
  "Bölüm II fasıl başlıkları sorusunda “Hububat” başlığının bitkisel ürünler bölümünde yer aldığı, Fasıl 21 başlığının ise yer almadığı sınanmıştır.",
  "Bazı sorularda “10. Bölüm” ifadesi çeldirici olarak kullanılmıştır; Fasıl 10 (hububat) Bölüm II’dedir ve Bölüm X ile karıştırılmamalıdır."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdaki hububat tanelerinden hangisi Türk Gümrük Tarife Cetveli’nin 10. faslında sınıflandırılır?",
   "secenekler": ["Kırık buğday", "Kırık arpa", "Kırık pirinç", "Kırık mısır", "Kırık çavdar"],
   "cevap": "C",
   "aciklama": "Fasıl 10 Not 1(B)’ye göre kavuzundan çıkarılmış veya başkaca işlenmiş taneler bu fasla girmez; istisna, kavuzu çıkarılmış, değirmenden geçirilmiş, parlatılmış, yarım kaynatılmış veya kırık pirinçtir (10.06). Diğer kırık taneler Fasıl 11’dedir."
  },
  {
   "soru": "Aşağıdakilerden hangisi Tarife Cetvelinde 12. fasılda sınıflandırılır?",
   "secenekler": ["Kuş yemi", "Mısır", "Fiğ", "Darı"],
   "cevap": "C",
   "aciklama": "Fiğ, 12.14’te sayılan yem bitkilerindendir. Kuş yemi ve darı 10.08’de, mısır 10.05’te, yani Fasıl 10’dadır."
  }
 ],
 "ozet": [
  "Fasıl 10 = tane halindeki hububat; başak veya sap içinde olması fark etmez.",
  "Kavuzu çıkarılmış veya işlenmiş tane Fasıl 11’e gider; pirinç (10.06) ve kinoa (10.08) istisnadır.",
  "Tatlı mısır Fasıl 7’de; diğer taze hububat sebze olarak kullanılmaya uygun olsa da Fasıl 10’da.",
  "Pirinç: çeltik, kahverengi, beyaz, parlatılmış, yarı kaynatılmış, kırık 10.06; ön pişirilmiş ve şişirilmiş 19.04.",
  "Darı: tane sorgum 10.07, cin ve kum darı 10.08, yem ve çayır darısı 12.14, tatlı darı 12.12, akdarı 14.04.",
  "Tohumluk hububat da Fasıl 10’dadır; malt 11.07, kavrulmuş arpa 21.01, çavdar mahmuzu 12.11."
 ]
}

S = {}
# ---- Eşya → 4’lü pozisyon
S["E1"] = Q(T_ES,
 "Tarife Cetveline göre, mekanik kabuk çıkarıcılarla kavuzu çıkarılmış ancak perikarp ile sarılı halde bulunan kahverengi pirinç hangi pozisyonda sınıflandırılır?",
 "10.06", ["11.04", "10.08", "11.02", "19.04"], "C",
 "Fasıl 10 Not 1(B) kavuzundan çıkarılmış taneleri fasıl dışında bırakır, ancak kavuzu çıkarılmış pirinci açıkça 10.06’da tutar; kahverengi (kargo) pirinç 10.06 Açıklama Notunda sayılmıştır. Diğer hububatta kavuzun çıkarılması 11.04’e götürür; pirinçte bu kural işlemez. 19.04 yalnız ön pişirilmiş veya şişirilmiş pirinç içindir.",
 "Fasıl 10 Not 1(B); 10.06 Açıklama Notu.")
S["E2"] = Q(T_ES,
 "Tarife Cetveline göre, saponini ayırmak amacıyla perikarpı kısmen çıkarılmış ancak başka bir işlemden geçirilmemiş kinoa hangi pozisyonda sınıflandırılır?",
 "10.08", ["11.04", "12.09", "10.07", "19.04"], "A",
 "Fasıl 10 Not 1(B), saponini ayırmak için perikarpı tamamen veya kısmen çıkarılmış fakat başka işlem görmemiş kinoayı 10.08’de tutar. 11.04 Açıklama Notu da bu kinoayı hariç tutarak 10.08’e gönderir. Tuzak, perikarpın çıkarılmasını “başka şekilde işlenmiş tane” sayıp 11.04’ü seçmektir.",
 "Fasıl 10 Not 1(B); 11.04 Açıklama Notu.")
S["E3"] = Q(T_ES,
 "Tarife Cetveline göre, harman edilmemiş, başakları içinde ve sapları ile birlikte demetler halinde sunulan olgun arpa hangi pozisyonda sınıflandırılır?",
 "10.03", ["12.13", "12.14", "11.04", "10.08"], "E",
 "Fasıl 10 Not 1(A)’ya göre bu fasıldaki ürünler tane halinde iseler başakları içinde veya saplarında olsun olmasın kendi pozisyonlarında sınıflandırılır; arpa 10.03’tedir. 12.13 yalnız hububat saplarını ve kapçıklarını, 12.14 yem bitkilerini kapsar. Tane işlenmediği için 11.04 de söz konusu değildir.",
 "Fasıl 10 Not 1(A); Fasıl 10 Genel Açıklamalar.")
S["E4"] = Q(T_ES,
 "Tarife Cetveline göre, harman işleminden sonra bile kapçıklı halde bulunan, küçük kahverengi taneli bir buğday türü olan kaplıca hangi pozisyonda yer alır?",
 "10.01", ["10.08", "11.04", "12.13", "10.03"], "B",
 "10.01 Açıklama Notu, harman işleminden sonra bile kapçıklı halde bulunan kaplıcayı açıkça bu pozisyonda sayar. Kapçıklı olması onu hububat kapçığı (12.13) veya işlenmiş tane (11.04) yapmaz; bir buğday türü olduğu için 10.08’deki “diğer hububat” da değildir.",
 "10.01 Açıklama Notu.")
S["E5"] = Q(T_ES,
 "Tarife Cetveline göre, tamamen pişirilip daha sonra suyu alınmış, tüketilmeden önce yalnızca suda ıslatılıp kaynatılması gereken pirinç taneleri hangi pozisyonda sınıflandırılır?",
 "19.04", ["10.06", "11.04", "19.01", "11.02"], "D",
 "10.06 Açıklama Notuna göre tane yapısını önemli ölçüde değiştiren işlemlere tabi tutulmuş pirinçler bu pozisyon dışındadır; tamamen veya kısmen pişirilmiş ve sonra suyu alınmış ön pişirilmiş pirinç 19.04’te yer alır. Yarı kaynatılmış pirinç ise tane yapısı az değiştiğinden 10.06’da kalır; tuzak bu iki ürünü karıştırmaktır.",
 "10.06 Açıklama Notu.")
# ---- Olumsuz teşhis
S["O1"] = Q(T_OL,
 "Aşağıdakilerden hangisi 10.06 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Şişirilerek kabartılmış, tüketime hazır pirinç",
 ["Kavuz içinde bulunan pirinç (çeltik)", "İnce bir yağ tabakasıyla kaplanmış Camolino pirinci", "İşleme sırasında kırılan pirinç taneleri", "Yarı kaynatılmış pirinç"], "B",
 "Şişirme işlemiyle elde edilmiş ve tüketime hazır haldeki kabartılmış (puffed) pirinçler 19.04’te yer alır. Çeltik, Camolino pirinci, kırık pirinç ve yarı kaynatılmış pirinç 10.06 Açıklama Notunda açıkça sayılmıştır.",
 "10.06 Açıklama Notu; Fasıl 10 Not 1(B).")
S["O2"] = Q(T_OL,
 "Aşağıdakilerden hangisi Tarife Cetvelinin 10. faslında <b>yer almaz</b>?",
 "Tatlı mısır (Zea mays var. saccharata)",
 ["Karabuğday", "Kuş yemi", "Buğday ve çavdar melezi (triticale)", "Çatal otu (fonio)"], "E",
 "Fasıl 10 Not 2’ye göre tatlı mısır 10.05’e dahil değildir ve Fasıl 7’de sebze olarak sınıflandırılır. Karabuğday, kuş yemi, triticale ve fonio 10.08 pozisyonunda, yani Fasıl 10’dadır. Tuzak, “mısır” kelimesini görüp 10.05’i düşünmektir.",
 "Fasıl 10 Not 2; 10.08 pozisyon metni ve Açıklama Notu.")
S["O3"] = Q(T_OL,
 "Aşağıdakilerden hangisi 10.03 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Değirmende kabuğu çıkarılmış bracteiferous arpa taneleri",
 ["Kavuzu taneye yapışık halde bulunan bracteiferous arpa", "Yalnız harman ve savurma görmüş, tabii haliyle kavuzsuz arpa", "Hayvan yemi olarak kullanılacak arpa", "Malt imalinde kullanılacak, filizlendirilmemiş arpa"], "A",
 "10.03 Açıklama Notuna göre kavuzları taneye yapışık bracteiferous arpa kavuzlu halde 10.03’tedir; değirmen işleminden geçirilerek kabuğu çıkarılmışsa 11.04’e gider. Tabii kavuzsuz arpa yalnız harman ve savurma görmüşse 10.03’te kalır. Kullanım amacı (yem, malt yapımı) sınıflandırmayı değiştirmez; filizlendirilmiş arpa ise malt olarak 11.07’dedir.",
 "10.03 Açıklama Notu; Fasıl 10 Not 1(B).")
S["O4"] = Q(T_OL,
 "Aşağıdakilerden hangisi 10.07 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Otlatmada yararlanılan sudanense çayır darısı",
 ["Kafir (caffrorum) darısı", "Beyaz durra (cernuum)", "Kahverengi durra", "Kaoliang (nervosum)"], "D",
 "10.07 yalnız tane darı olarak bilinen ve insan tüketimine mahsus hububat olarak kullanılabilen darıları (kafir, beyaz durra, kahverengi durra, kaoliang) kapsar. Halepense gibi yem darıları ve sudanense gibi çayır darıları 12.14’te yer alır.",
 "10.07 Açıklama Notu.")
# ---- Farklı/aynı
S["F1"] = Q(T_FA,
 "Aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
 "Kaoliang", ["Karabuğday", "Kuş yemi", "Kinoa", "Triticale"], "C",
 "Kaoliang (nervosum) bir tane sorgum çeşidi olarak 10.07’de yer alır. Karabuğday, kuş yemi, kinoa ve triticale (buğday-çavdar melezi) 10.08’dedir. Tuzak, darı adı taşıyan veya hububat sayılan her ürünü aynı pozisyonda sanmaktır.",
 "10.07 ve 10.08 Açıklama Notları.")
S["F2"] = Q(T_FA,
 "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
 "Kavuzu çıkarılmış yulaf taneleri", ["Mahlut", "Çavdar", "Kavuzlu yulaf", "Tohumluk mısır"], "E",
 "Kavuzu çıkarılmış ancak perikarpı çıkarılmamış yulaf, işlenmiş tane olarak 11.04’te (Fasıl 11) yer alır. Mahlut 10.01’de, çavdar 10.02’de, kavuzlu yulaf 10.04’te, tohumluk mısır 10.05’tedir. Tabii haliyle kavuzsuz yulafın 10.04’te kaldığı da unutulmamalıdır.",
 "Fasıl 10 Not 1(B); 10.04 ve 11.04 Açıklama Notları.")
S["F3"] = Q(T_FA,
 "Aşağıdaki ikililerden hangisinde yer alan ürünler aynı tarife pozisyonunda sınıflandırılır?",
 "Buğday – Mahlut",
 ["Buğday – Karabuğday", "Mısır – Tatlı mısır", "Arpa – Malt", "Çavdar – Çavdar mahmuzu"], "A",
 "10.01 pozisyonu buğday ve mahlutu (çavdarla buğdayın genellikle 2’ye 1 oranında karışımı) birlikte kapsar. Karabuğday 10.08’de, tatlı mısır Fasıl 7’de, malt 11.07’de, çavdar mahmuzu 12.11’dedir.",
 "10.01 pozisyon metni ve Açıklama Notu; Fasıl 10 Not 2; 10.02 ve 10.03 Açıklama Notları.")
S["F4"] = Q(T_FA,
 "Ekim amacıyla kullanılmak üzere ithal edilen aşağıdaki tohumlardan hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
 "Yonca tohumu", ["Buğday tohumu", "Arpa tohumu", "Mısır tohumu", "Darı (cin ve kum darı) tohumu"], "D",
 "Fasıl 12 Not 3’e göre hububat, ekilmeye mahsus olsa bile 12.09’da sınıflandırılmaz; tohumluk buğday 10.01, arpa 10.03, mısır 10.05, darı 10.08 ile Fasıl 10’da kalır. Yonca gibi yem bitkisi tohumları ise ekim amaçlı olduğunda 12.09’dadır.",
 "Fasıl 12 Not 3; 12.09 Açıklama Notu.")
# ---- Fasıl notu
S["N1"] = Q(T_NO,
 "Fasıl 10 notlarına göre aşağıdakilerden hangisi <b>doğrudur</b>?",
 "Fasıl 10’daki ürünler ancak tane halinde iseler, başakları içinde veya saplarında olsun olmasın bu fasılda yer alır.",
 ["Başakları veya sapları ile birlikte sunulan hububat 12.13’te sınıflandırılır.",
  "Kavuzundan çıkarılmış her türlü hububat tanesi Fasıl 10’da kalır.",
  "Kırık hububat taneleri, cinsine bakılmaksızın Fasıl 10’da sınıflandırılır.",
  "Sebze olarak kullanılmaya uygun taze hububat Fasıl 7’de sınıflandırılır."], "B",
 "Fasıl 10 Not 1(A) ürünlerin tane halinde olmasını şart koşar; başak veya sap içinde olması sonucu değiştirmez. Not 1(B) kavuzundan çıkarılmış veya işlenmiş taneleri fasıl dışında bırakır; kırık tane istisnası yalnız pirince aittir. Genel Açıklamalara göre taze hububat (tatlı mısır hariç) sebze olarak kullanılmaya uygun olsa da Fasıl 10’dadır.",
 "Fasıl 10 Not 1(A) ve 1(B); Fasıl 10 Genel Açıklamalar.")
S["N2"] = Q(T_NO,
 "10.01 Açıklama Notuna göre “mahlut” aşağıdakilerden hangisidir?",
 "Çavdarla buğdayın genellikle 2’ye 1 oranındaki karışımı",
 ["Buğday ile arpanın eşit oranlardaki karışımı", "Buğday ile çavdarın melezi olan triticale", "Makarnalık buğday ile adi buğdayın karışımı", "Harmandan sonra kapçıklı kalan buğday türü"], "C",
 "10.01 Açıklama Notunda mahlut, çavdarla buğdayın genellikle 2’ye 1 oranında karışımı olarak tanımlanır ve buğday ile birlikte 10.01’dedir. Buğday-çavdar melezi triticale ise bir karışım değil, melez tane hububattır ve 10.08’dedir. Harmandan sonra kapçıklı kalan tür kaplıcadır.",
 "10.01 pozisyon metni ve Açıklama Notu; 10.08 Açıklama Notu.")
S["N3"] = Q(T_NO,
 "10.06 Açıklama Notunda yarı kaynatılmış pirinç ile kısmen ön pişirilmiş pirinci ayırt etmek için verilen süreler hangi seçenekte doğru eşleştirilmiştir?",
 "Yarı kaynatılmış: tam pişirme 20–35 dakika; kısmen ön pişirilmiş: hazırlama 5–12 dakika",
 ["Yarı kaynatılmış: tam pişirme 5–12 dakika; kısmen ön pişirilmiş: hazırlama 20–35 dakika",
  "Yarı kaynatılmış: tam pişirme 10–15 dakika; kısmen ön pişirilmiş: hazırlama 1–3 dakika",
  "Yarı kaynatılmış: tam pişirme 35–50 dakika; kısmen ön pişirilmiş: hazırlama 20–35 dakika",
  "Yarı kaynatılmış: tam pişirme 20–35 dakika; kısmen ön pişirilmiş: hazırlama 15–20 dakika"], "E",
 "10.06 Açıklama Notuna göre yarı kaynatılmış pirincin değirmenden geçirme ve parlatma sonrasında tam pişirilmesi 20 ila 35 dakika sürer ve tane yapısı az değiştiği için 10.06’da kalır. Kısmen ön pişirilmiş pirincin hazırlanması 5 ila 12 dakika gerektirir; tamamen ön pişirilmiş pirinç yalnız ıslatma ve kaynatma ister. Ön pişirilmiş pirinçler 19.04’tedir.",
 "10.06 Açıklama Notu.")
S["N4"] = Q(T_NO,
 "Fasıl 10 Not 1(B) uyarınca, kavuzundan çıkarılmış veya başkaca işlenmiş olmasına rağmen Fasıl 10’da kalan ürünler hangi seçenekte birlikte verilmiştir?",
 "Pirinç ve kinoa", ["Pirinç ve yulaf", "Kinoa ve karabuğday", "Arpa ve yulaf", "Mısır ve pirinç"], "A",
 "Not 1(B) kavuzundan çıkarılmış veya işlenmiş taneleri fasıl dışında bırakır ve iki istisna sayar: kavuzu çıkarılmış, değirmenden geçirilmiş, parlatılmış, yarım kaynatılmış veya kırık pirinç (10.06) ile saponini ayırmak için perikarpı çıkarılmış, başka işlem görmemiş kinoa (10.08). Kavuzu çıkarılmış yulaf, karabuğday ve darı 11.04’e gider.",
 "Fasıl 10 Not 1(B); 11.04 Açıklama Notu.")
# ---- GYK
S["G1"] = Q(T_GY,
 "Kavuzu çıkarılmış, değirmenden geçirilmiş ve parlatılmış pirincin 10.06 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
 "GYK 1 – pozisyon metni ve Fasıl 10 Not 1(B) hükmüne göre",
 ["GYK 2(a) – işlenmiş eşya tamamlanmış eşya gibi sınıflandırıldığı için",
  "GYK 3(a) – 10.06, 11.04’e göre daha özel olduğu için",
  "GYK 3(c) – numara sırasına göre sonuncu pozisyon olduğu için",
  "GYK 4 – eşyaya en çok benzeyen eşya çeltik olduğu için"], "D",
 "Sınıflandırma doğrudan 10.06 pozisyon metni ve Fasıl 10 Not 1(B) hükmüyle yapılır; not, kavuzu çıkarılmış, değirmenden geçirilmiş ve parlatılmış pirinci açıkça 10.06’ya bağlar. Not hükmü varken GYK 3’e veya GYK 4’e geçilmez. GYK 2(a) ise Açıklama Notuna göre I–VI. Bölümlerdeki eşyaya normal olarak uygulanmaz.",
 "GYK 1; Fasıl 10 Not 1(B); GYK 2(a) Açıklama Notu (III).")
S["G2"] = Q(T_GY,
 "Buğday, bu eşyanın taşınmasında normal olarak kullanılan ve tekrar kullanıma elverişli olduğu açıkça belli olmayan jüt çuvallar içinde gümrüğe sunulmuştur. Çuvalların sınıflandırılmasıyla ilgili hangisi <b>doğrudur</b>?",
 "GYK 5(b) uyarınca buğday ile birlikte 10.01’de sınıflandırılır.",
 ["GYK 5(a) uyarınca buğday ile birlikte 10.01’de sınıflandırılır.",
  "GYK 1 uyarınca kendi pozisyonunda ayrı olarak sınıflandırılır.",
  "GYK 3(b) uyarınca buğday ile birlikte takım oluşturur.",
  "GYK 2(a) uyarınca bitirilmemiş eşya olarak sınıflandırılır."], "B",
 "GYK 5(b)’ye göre içindeki eşya ile birlikte sunulan ve bu eşyanın ambalajında normal olarak kullanılan ambalaj maddeleri eşya ile beraber sınıflandırılır; sürekli kullanıma elverişli olduğu açıkça belli olanlar hariçtir. GYK 5(a) ise belli bir eşyaya göre şekil verilmiş, uzun süre kullanılmaya uygun kutu ve mahfazalar içindir. Çuval ile buğday takım oluşturmaz.",
 "GYK 5(a) ve 5(b); GYK 5 Açıklama Notları.")
# ---- Eşleştirme / Boşluk
S["B1"] = Q(T_EB,
 "Fasıl 10 notlarına ve açıklama notlarına göre; tatlı mısır …… Fasılda, akdarı …… pozisyonunda, halepense gibi yem darıları ise …… pozisyonunda yer alır. Boşluklara sırasıyla gelmesi gerekenler hangi seçenekte doğru verilmiştir?",
 "7 – 14.04 – 12.14",
 ["7 – 12.12 – 12.14", "11 – 14.04 – 23.08", "10 – 12.14 – 14.04", "7 – 14.04 – 10.07"], "C",
 "Fasıl 10 Not 2 tatlı mısırı Fasıl 7’ye gönderir. 10.07 Açıklama Notuna göre akdarı 14.04’te, yem darıları ve çayır darıları 12.14’te, tatlı darılar 12.12’de yer alır. 10.07 yalnız insan tüketimine mahsus tane darıları kapsar.",
 "Fasıl 10 Not 2; 10.07 Açıklama Notu.")
S["B2"] = Q(T_EB,
 "Aşağıdaki ürünleri sınıflandırıldıkları pozisyonlarla eşleştiriniz. I. Çeltik  II. Kaoliang  III. Karabuğday  IV. Mahlut — a. 10.01  b. 10.06  c. 10.07  d. 10.08",
 "I-b, II-c, III-d, IV-a",
 ["I-b, II-d, III-c, IV-a", "I-a, II-c, III-d, IV-b", "I-b, II-c, III-a, IV-d", "I-c, II-b, III-d, IV-a"], "A",
 "Kavuz içindeki pirinç (çeltik) 10.06’da, tane sorgum çeşidi kaoliang 10.07’de, Polygonaceae familyasından karabuğday 10.08’de, çavdar-buğday karışımı mahlut 10.01’de yer alır. Karabuğdayın adındaki “buğday” onu 10.01’e götürmez.",
 "10.01, 10.06, 10.07, 10.08 pozisyon metinleri ve Açıklama Notları.")
# ---- Çoktan-çoğa
S["C1"] = Q(T_CC,
 "Aşağıdakilerden hangileri 10.06 pozisyonunda sınıflandırılır? I. İnce bir yağ tabakasıyla kaplanmış Camolino pirinci  II. Talk ve glikoz karışımıyla kaplanmış perdahlanmış pirinç  III. Kısmen ön pişirilmiş, 5–12 dakikada hazırlanan pirinç  IV. İşleme sırasında kırılan pirinç",
 "I, II ve IV", ["I ve II", "II ve III", "I, II ve III", "II, III ve IV"], "E",
 "Camolino pirinci, perdahlanmış pirinç ve kırık pirinç 10.06 Açıklama Notunda açıkça sayılmıştır (I, II, IV). Kısmen ön pişirilmiş pirinç tane yapısını önemli ölçüde değiştiren işlem gördüğünden 19.04’tedir (III).",
 "10.06 Açıklama Notu.")
S["C2"] = Q(T_CC,
 "Yulaf ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kavuzlu yulaf 10.04’te yer alır.  II. Tabii haliyle kavuzsuz yulaf, harman ve savurma dışında işlem görmemişse 10.04’te yer alır.  III. Normal işleme ve taşıma sırasında kavuz uçları dökülmüş yulaf 10.04’te yer alır.  IV. Kavuzu çıkarılmış, perikarpı çıkarılmamış yulaf 10.04’te yer alır.",
 "I, II ve III", ["I ve II", "I ve IV", "II ve III", "I, II ve IV"], "D",
 "10.04 kavuzlu yulafı, harman ve savurma dışında işlem görmemiş tabii kavuzsuz yulafı ve dağıtım sırasında kavuz uçları dökülmüş yulafı kapsar (I, II, III). Kavuzu çıkarılmış ancak perikarpı çıkarılmamış yulaf işlenmiş tane olarak 11.04’tedir (IV).",
 "10.04 ve 11.04 Açıklama Notları; Fasıl 10 Not 1(B).")
# ---- Senaryo
S["S1"] = Q(T_SE,
 "Olgunlaşmadan önce biçilmiş, kapçıklı halde bulunan ve sebze gibi tüketilmeye uygun taze yeşil buğday taneleri ithal edilmektedir. Ürün tatlı mısır değildir ve tane halinde olup başka bir işlem görmemiştir. Eşya hangi pozisyonda sınıflandırılır?",
 "10.01", ["07.09", "12.14", "11.04", "10.08"], "B",
 "Fasıl 10 Genel Açıklamalarına göre olgunlaşmadan biçilen ve kapçıklı halde bulunan hububattan elde edilen taneler normal tanelerle birlikte sınıflandırılır; taze hububat da (tatlı mısır hariç) sebze olarak kullanılmaya uygun olsun olmasın Fasıl 10’dadır. Ürün buğday olduğu için 10.01’de yer alır. Fasıl 7 yalnız tatlı mısır için söz konusudur.",
 "Fasıl 10 Genel Açıklamalar; Fasıl 10 Not 2.")
S["S2"] = Q(T_SE,
 "Kafes kuşlarını beslemek için kullanılan; parlak saman renginde, uzun ve iki ucu sivri tohumlardan oluşan, başka hiçbir madde katılmamış ve hazırlanmamış ürün dökme halde ithal edilmektedir. Eşya hangi pozisyonda sınıflandırılır?",
 "10.08", ["23.09", "12.09", "10.07", "12.14"], "C",
 "10.08 Açıklama Notu kuş yemini parlak saman renginde, uzun ve iki ucu sivri tohumlar olarak tanımlar ve pozisyon metni onu açıkça sayar. Hayvan beslemede kullanılması onu hazırlanmış hayvan yemlerine (23.09) veya yem bitkilerine (12.14) götürmez; ekim amacı olmadığı için 12.09 da söz konusu değildir.",
 "10.08 pozisyon metni ve Açıklama Notu.")

SIRA = ["E1", "N1", "O1", "F1", "E2", "B1", "O2", "G1", "F2", "N2", "E3", "O3", "S1",
        "F3", "C1", "E4", "N3", "B2", "O4", "G2", "E5", "C2", "N4", "F4", "S2"]
d["sorular"] = sirala(S, SIRA)
yaz(10, d)
