#!/usr/bin/env python3
"""Deneme sınavı 8 üreticisi -> data/deneme_08.json"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "deneme_08.json")

E4 = "Eşya → 4’lü pozisyon"
OL = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
NT = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SE = "Senaryo"

Q = []


def q(fasil, tip, harf, soru, dogru, yanlis, gerekce, dayanak):
    assert len(yanlis) == 4, soru
    idx = "ABCDE".index(harf)
    secenekler = list(yanlis)
    secenekler.insert(idx, dogru)
    Q.append({
        "soru": soru,
        "secenekler": secenekler,
        "cevap": harf,
        "tip": tip,
        "gerekce": gerekce,
        "dayanak": dayanak,
        "fasil": fasil,
    })


# 1
q(8, E4, "C",
  "Tarife Cetveline göre, dondurularak kurutulmuş (liyofilize), şeker katılmamış ve başka bir işlem görmemiş çilek dilimleri "
  "hangi pozisyonda sınıflandırılır?",
  "08.13", ["08.11", "08.10", "20.08", "08.12"],
  "Fasıl 8 Genel Açıklamaları, bu fasıldaki meyvelerin kurutulmuş (suyu alınmış, buharlaştırılmış veya dondurularak kurutulmuş "
  "olanlar dahil) halde de bulunabileceğini belirtir. 08.13 pozisyonu 08.01 ila 08.06 dışındaki kurutulmuş meyveleri kapsar; açıklama "
  "notu bunların taze hallerinin 08.07 ila 08.10’da yer aldığını belirtir ve taze çilek 08.10’dadır. Dondurma aşaması ürünü 08.11’e "
  "götürmez, çünkü eşya dondurulmuş değil kurutulmuş haldedir; 08.12 ise geçici olarak korunmaya alınmış ve hemen yenmeye elverişli "
  "olmayan meyveler içindir.",
  "Fasıl 8 Genel Açıklamalar; 08.13 pozisyon metni ve Açıklama Notu.")

# 2
q("GYK", GY, "A",
  "GYK 2(b)’ye göre bir maddeye yapılan atıf, kural olarak bu maddenin başka maddelerle karışımlarını da kapsar. Buna rağmen "
  "konsantre edilmemiş, ancak ilave şeker içeren inek sütü 04.01’de değil 04.02’de sınıflandırılır. Bunun dayanağı aşağıdakilerden hangisidir?",
  "04.01 metnindeki “ilave şeker veya diğer tatlandırıcı maddeleri içermeyenler” kaydı aksine bir hüküm olduğundan GYK 2(b) "
  "uygulanmaz; ürün GYK 1 uyarınca 04.02’de yer alır.",
  ["Ürün ilk bakışta iki pozisyona girdiğinden GYK 3(a) uyarınca daha özel tanım olan 04.02 öncelik alır.",
   "Ürüne esas niteliğini ilave şeker verdiğinden GYK 3(b) uyarınca 04.02’de sınıflandırılır.",
   "Esas nitelik belirlenemediğinden GYK 3(c) uyarınca numara sırasına göre sonra gelen 04.02 seçilir.",
   "GYK 2(b) yalnız belirli bir maddeden mamul eşyaya uygulanır; maddelerin karışımlarını kapsamaz."],
  "GYK 2(b) açıklama notu (X), kuralın pozisyonlarda, bölüm veya fasıl notlarında aksine bir hüküm bulunmadığı hallerde "
  "uygulanacağını belirtir ve “domuz yağı karıştırılmamış” kaydını taşıyan 15.03’ü örnek verir. 04.01 metnindeki “ilave şeker veya "
  "diğer tatlandırıcı maddeleri içermeyenler” kaydı da böyle bir hükümdür; 04.02 ise ilave şeker içeren süt ve kremayı açıkça kapsar. "
  "Bu nedenle 3. kurala geçilmeden sınıflandırma doğrudan pozisyon metinlerine, yani GYK 1’e dayanır.",
  "GYK 1; GYK 2(b) Açıklama Notu (X); 04.01 ve 04.02 pozisyon metinleri.")

# 3
q(64, E4, "E",
  "Tarife Cetveline göre, ayrı bir dış tabanı bulunmayan; ayağın altını, yanlarını ve üstünü tek parça halinde saran tabii deriden "
  "yapılmış makosen tipi ayakkabı hangi pozisyonda sınıflandırılır?",
  "64.03", ["64.05", "64.06", "64.04", "42.05"],
  "Fasıl 64 Genel Açıklamaları (C), taban takılmamış yekpare ayakkabılarda ayrı bir tabana gerek olmadığını ve bunların alt "
  "yüzeylerini oluşturan maddeye göre sınıflandırılacağını belirtir; (D) bendi de makosen tipi ayakkabılarda yüzün, ayağın üstünü ve "
  "yanlarını kaplayan kısım olarak kabul edileceğini açıklar. Yere temas eden alt yüzey de yüz de tabii deri olduğundan ayakkabı, dış "
  "tabanı tabii köseleden ve yüzü deriden olan ayakkabıları kapsayan 64.03’te yer alır. Ayrı tabanın bulunmaması eşyayı 64.05’e veya "
  "aksam olarak 64.06’ya götürmez.",
  "Fasıl 64 Genel Açıklamalar (C) ve (D); 64.03 pozisyon metni.")

# 4
q(24, OL, "B",
  "Tütünden elde edilmiş bir madde içerse bile aşağıdakilerden hangisi 24.03 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Tütün hülasası içeren, perakende ambalajlı böcek öldürücü müstahzar",
  ["Enfiye imali için sıkıştırılmış veya likörlenmiş tütün",
   "Yüksek derecede fermente edilmiş ve likörlenmiş çiğneme tütünü",
   "Tütün artıklarının su içinde kaynatılmasıyla hazırlanmış tütün hülasası",
   "Pipoda içilmek üzere hazırlanmış, tütün içermeyen bitkisel karışım"],
  "24.03 Açıklama Notu; enfiye imaline mahsus sıkıştırılmış veya likörlenmiş tütünü, çiğneme tütününü, tütün hülasa ve esanslarını "
  "ve tütün içermeyen içilen karışımları (mamul tütün yerine geçen ürünler) bu pozisyonda sayar. Aynı not, 38.08 pozisyonunda yer alan "
  "böcek öldürücüleri pozisyon dışında bırakır. Tuzak, tütün hülasalarının esas olarak böcek ilacı imalinde kullanılmasıdır: hülasanın "
  "kendisi 24.03’te, ondan hazırlanmış böcek öldürücü ise 38.08’dedir.",
  "24.03 Açıklama Notu.")

# 5
q(43, FA, "D",
  "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  "Örme yoluyla elde edilmiş uzun tüylü taklit kürk mensucatı",
  ["Deri üzerine yün yapıştırılarak elde edilmiş taklit kürk",
   "Mensucat üzerine kıllar dikilerek elde edilmiş taklit kürk",
   "Dabaklanmış, birleştirilmemiş ve özel bir kullanım için kesilmemiş tilki derisi",
   "Kürkçülüğe elverişli ham vizon kuyrukları"],
  "Fasıl 43 Not 5’e göre “taklit kürk”, deri, mensucat veya diğer maddeler üzerine yapıştırılmış ya da dikilmiş yün, kıl veya diğer "
  "liflerden oluşan ürünlerdir ve 43.04’te yer alır. Aynı not dokuma veya örme suretiyle elde edilen taklit kürkleri tabirin dışında "
  "bırakır; bunlar genellikle 58.01 veya 60.01 pozisyonlarında, yani Bölüm XI’de sınıflandırılır. Dabaklanmış tilki derisi 43.02’de, "
  "kürkçülüğe elverişli ham kuyruklar 43.01’de olup Fasıl 43’te kalır.",
  "Fasıl 43 Not 5; 43.01 ve 43.02 Açıklama Notları.")

# 6
q(30, E4, "B",
  "Tarife Cetveline göre, yoğurt ve kefir yapımında kullanılan, canlı laktik fermentlerden oluşan mikroorganizma kültürü hangi pozisyonda sınıflandırılır?",
  "30.02", ["21.02", "35.07", "04.03", "30.04"],
  "30.02 Açıklama Notu, mayalar hariç mikroorganizma kültürlerini bu pozisyonda sayar ve örnek olarak süt türevlerinin (kefir, yoğurt, "
  "laktik asit) yapımında kullanılan laktik fermentleri gösterir. Aynı not, mikrobik menşeli olsalar dahi enzimleri 35.07’ye, canlı olmayan "
  "tek hücreli mikroorganizmaları 21.02’ye gönderir. Ürün bir yoğurt veya ilaç olmadığından 04.03 ve 30.04 de uygun değildir.",
  "30.02 pozisyon metni ve Açıklama Notu.")

# 7
q(66, FA, "A",
  "Bastonlar ve kamçılarla ilgili aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
  "İzci sopası – Kırbaç ucu",
  ["Koltuk değneği – Yaşlılar için düzenlenmiş baston",
   "Kayak değneği – İskemle baston",
   "Kamçı sapı – Binici kamçısı",
   "Şemsiye çerçevesi – Şemsiyeye takılmamış kumaş şemsiye kılıfı"],
  "66.02 Açıklama Notu; alelade bastonların yanında izci ve çoban sopalarını, iskemle bastonları ve kırbaç uçları dahil kırbaç ve "
  "kamçıları bu pozisyonda sayar. Koltuk değnekleri 90.21’e, kayak değnekleri Fasıl 95’e gider; kamçı ve kırbaç sapları ile şemsiye "
  "çerçeveleri ise aksam olarak 66.03’tedir. Şemsiyeye takılmamış kılıflar Fasıl 66 Not 2 gereği ayrıca sınıflandırılır.",
  "Fasıl 66 Not 2; 66.02 ve 66.03 Açıklama Notları.")

# 8
q(2, E4, "B",
  "Tarife Cetveline göre; yüksek oranda yağ içermekle birlikte yağ tabakaları arasında yağsız et katmanları bulunan, tuzlanmış ve "
  "tütsülenmiş lifli domuz eti hangi pozisyonda sınıflandırılır?",
  "02.10", ["02.09", "15.01", "16.02", "02.03"],
  "02.09 Açıklama Notu, bu pozisyondaki domuz yağını yağsız et kısımlarını içermeyen yağlarla sınırlar ve lifli domuz eti ile yüksek "
  "oranda domuz yağı karıştırılmış benzer etleri duruma göre 02.03 veya 02.10’a gönderir. 02.10 Açıklama Notu da pozisyon metnindeki "
  "usullerle hazırlanmış lifli domuz etini bu pozisyonda sayar; ürün tuzlanıp tütsülendiğinden 02.03 değil 02.10 uygundur. Eritilmiş "
  "domuz yağı 15.01’e, pişirilmiş veya baharatla hazırlanmış et ise 16.02’ye gider.",
  "02.09 ve 02.10 Açıklama Notları.")

# 9
q(76, OL, "E",
  "Aşağıdakilerden hangisi 76.15 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Alüminyum gövdeli vakumlu termos şişesi",
  ["Alüminyumdan bulaşık ovma süngeri",
   "Alüminyumdan temizlik eldiveni",
   "Isıtıcı elemanı bulunmayan alüminyum pişirme tenceresi",
   "Alüminyumdan elektriksiz, ev tipi pişirme ve ısıtma cihazı"],
  "76.15 pozisyon metni ve Açıklama Notu; alüminyumdan sofra, mutfak ve ev eşyasını, süngerleri, temizlik ve parlatma işlerinde "
  "kullanılan eşya ile eldivenleri ve 74.18’de tarif edilenlere benzer alüminyum pişirme ve ısıtma cihazlarını kapsar. Aynı not "
  "96.17 pozisyonundaki vakumlu kapları ve termos şişelerini pozisyon dışında bırakır. Malzemenin alüminyum olması termos şişesini "
  "Fasıl 76’ya getirmez.",
  "76.15 pozisyon metni ve Açıklama Notu.")

# 10
q(25, NT, "C",
  "Fasıl 25 notlarına göre, bu fasıldaki mineral maddelere tozlanmayı önleyici unsurların katılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
  "Katılabilir; ancak bu unsurlar maddeyi genel kullanımdan ziyade özel bir kullanıma uygun hale getirmemelidir.",
  ["Hiçbir durumda katılamaz; katılan unsur ürünü Fasıl 28’e götürür.",
   "Yalnız ağırlıkça %3’ü geçmemek şartıyla katılabilir.",
   "Yalnız 25.17 pozisyonundaki taş kırıklarına katılabilir.",
   "Katılabilir; bu durumda ürün karışım sayılarak 38.24’te sınıflandırılır."],
  "Fasıl 25 notu, bu fasıldaki maddelere tozlanmayı önleyici unsurlar katılabileceğini, ancak katılan unsurların maddeyi genel "
  "kullanımdan ziyade özel kullanıma uygun hale getirmemesi gerektiğini belirtir. Not herhangi bir yüzde eşiği öngörmez; %3 sınırı "
  "Bölüm IV ve Fasıl 23’teki “pellet” tanımında geçen bağlayıcı oranıdır. Bu şart sağlandığında katkı sınıflandırmayı değiştirmez.",
  "Fasıl 25 Not 1; Fasıl 25 Genel Açıklamalar.")

# 11
q("GYK", GY, "A",
  "96.06 pozisyon metninde düğmelerle birlikte açıkça “düğme taslakları”na da yer verilmiştir. Düğme taslaklarının bu pozisyonda "
  "sınıflandırılmasının dayanağı aşağıdakilerden hangisidir?",
  "GYK 1 – taslaklar pozisyon metninde açıkça belirtildiğinden",
  ["GYK 2(a) – son şeklini almamış eşya bitmiş eşyanın esas niteliğini taşıdığından",
   "GYK 2(b) – bir maddeye yapılan atıf o maddenin karışımlarını da kapsadığından",
   "GYK 3(a) – eşyayı en özel şekilde niteleyen pozisyon öncelik aldığından",
   "GYK 4 – eşyaya en çok benzeyen eşya düğme olduğundan"],
  "GYK 2(a) açıklama notu (II), kuralın şartlarının son şeklini almamış eşyaya “özel bir pozisyonda belirtilmedikçe” uygulanacağını "
  "ifade eder. 96.06 pozisyon metni düğme taslaklarını açıkça saydığından sınıflandırma, GYK 2(a)’ya başvurmaksızın doğrudan pozisyon "
  "metnine, yani GYK 1’e dayanır. 2(a) seçeneği taslakların genel olarak bitmiş eşya gibi sınıflandırılması mantığına dayandığı için "
  "çekicidir; ancak burada sonucu pozisyon metni belirler.",
  "GYK 1; GYK 2(a) Açıklama Notu (II); 96.06 pozisyon metni.")

# 12
q(88, E4, "D",
  "Tarife Cetveline göre, masa üstü süs eşyası olarak kullanılan, uçma kabiliyeti olmayan ve ahşaptan oyularak yapılmış yolcu uçağı "
  "modeli hangi pozisyonda sınıflandırılır?",
  "44.20", ["88.02", "90.23", "95.03", "88.07"],
  "88.01 ve 88.02 Açıklama Notları; doğru ölçülerde yapılsın yapılmasın dekorasyon için kullanılan modelleri (örneğin 44.20 veya "
  "83.06), yalnız gösteri amaçlı modelleri (90.23) ve eğlence amaçlı model ve oyuncakları (95.03) hava taşıtı pozisyonlarının dışında "
  "bırakır. Ahşaptan süs amaçlı model, ahşap küçük heykelcik ve diğer süs eşyasını kapsayan 44.20’de yer alır. Model yalnızca gösteri "
  "(demonstrasyon) amacına yönelik olsaydı 90.23 söz konusu olurdu.",
  "88.01 ve 88.02 Açıklama Notları; 44.20 pozisyon metni.")

# 13
q(4, FA, "A",
  "Süt ve arı ürünleriyle ilgili aşağıdaki eşya çiftlerinden hangisinde her iki ürün de Tarife Cetvelinde <b>aynı</b> pozisyonda yer alır?",
  "Peyniraltı suyu tereyağı – Rekombine tereyağı",
  ["Yayıkaltı – Sürülerek yenilen süt ürünü",
   "Lor – Krema",
   "Vitaminlerle zenginleştirilmiş, konsantre edilmemiş süt – Konsantre edilmiş süt",
   "Petekli tabii bal – Arı mumu"],
  "Fasıl 4 Not 3(a), 04.05 anlamında “tereyağı” tabirini yalnızca sütten elde edilen ve belirli süt yağı, yağsız kuru madde ve su "
  "oranlarını taşıyan tabii tereyağı, peyniraltı suyu tereyağı ve rekombine tereyağı olarak tanımlar; bu nedenle iki ürün de 04.05’tedir. "
  "Yayıkaltı 04.03’te, sürülerek yenilen süt ürünleri 04.05’te; lor 04.06’da, krema 04.01 veya 04.02’de; konsantre edilmemiş süt "
  "04.01’de, konsantre süt 04.02’de; tabii bal 04.09’da, arı mumu ise 15.21’de yer alır.",
  "Fasıl 4 Not 3(a); 04.01 ila 04.06 ve 04.09 pozisyon metinleri; 15.21 pozisyon metni.")

# 14
q(53, OL, "E",
  "Aşağıdakilerden hangisi 53.01 pozisyonunda <b>yer almaz</b>?",
  "Hint keteni (Abroma augusta) lifleri",
  ["Kostik soda çözeltisinde kaynatılıp asit çözeltisinde işlenerek lifleri ayrılmış kotonize keten",
   "Suda ıslatılmış keten",
   "Keten kıtığı",
   "Keten iplik döküntülerinin ve mensucat artıklarının sökülmesiyle elde edilen lifler"],
  "53.01 Açıklama Notu ham, suda ıslatılmış, kabukları çıkarılmış, kotonize edilmiş ve taranmış keteni, keten kıtığını ve iplik "
  "döküntüleri ile ditme suretiyle elde edilen döküntüler dahil keten döküntülerini kapsar. Aynı not, bazen “keten” olarak anılan "
  "Hint ketenini (Abroma augusta) 53.03’e, Yeni Zelanda ketenini ise 53.05’e gönderir. İsim benzerliği tuzaktır; belirleyici olan bitki türüdür.",
  "53.01 Açıklama Notu.")

# 15
q(27, ES, "C",
  "27.15 Açıklama Notuna göre; bir çözücü içinde genellikle %60 veya daha fazla bitümen içeren ve yolların kaplanmasında kullanılan "
  "cut-back’ler ………, katran ile aglomere edilmiş dolomit ………, bitümenli vernik ve boyalar ise ……… pozisyonunda sınıflandırılır. "
  "Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
  "27.15 – 25.18 – 32.10",
  ["27.13 – 25.18 – 27.15", "27.15 – 27.15 – 32.10", "27.14 – 68.07 – 32.10", "27.15 – 25.18 – 27.15"],
  "27.15 Açıklama Notu, cut-back’leri, bitümen emülsiyonlarını ve asfalt sakızı gibi bitümenli karışımları bu pozisyonda sayar. Aynı "
  "not katran ile aglomere edilmiş dolomiti 25.18’e, bitümenli vernik ve boyaları ise 32.10’a göndererek pozisyon dışında bırakır; "
  "vernik ve boyalar ince ve sert film oluşturmaları, havada kuruyabilmeleri gibi özellikleriyle bu karışımlardan ayrılır. 27.13 petrol "
  "bitümenini, 27.14 tabii bitümen ve asfaltı kapsar; son şeklini almış mamuller 68.07’dedir.",
  "27.15 Açıklama Notu.")

# 16
q(85, E4, "C",
  "Tarife Cetveline göre, yol kavşaklarına yerleştirilen; bir taşıtın geçişi anında yol üzerindeki bir kontak aracılığıyla otomatik "
  "olarak çalışan elektrikli trafik ışıkları hangi pozisyonda sınıflandırılır?",
  "85.30", ["86.08", "85.31", "94.05", "85.12"],
  "85.30 pozisyonu karayolları, demiryolları, limanlar ve havaalanlarında kullanılan elektrikli işaret, emniyet ve trafik kontrol "
  "cihazlarını kapsar; Açıklama Notu elle veya otomatik çalışan (zaman ayarlı, fotoelektrik selülle ya da yol üzerindeki bir kontakla "
  "çalışan) trafik ışıklarını açıkça sayar. 86.08 mekanik (elektromekanik dahil) işaret cihazları içindir; 85.31 ise 85.30’dakiler "
  "hariç ses veya görüntülü işaret cihazlarını kapsar. Motorlu taşıtlara mahsus işaret cihazları 85.12’de, statik ışıklı yön panoları "
  "ise 94.05 gibi pozisyonlarda yer alır.",
  "85.30 pozisyon metni ve Açıklama Notu; 85.31 Açıklama Notu.")

# 17
q(10, FA, "D",
  "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> olarak Tarife Cetvelinin 10. faslında sınıflandırılır?",
  "Buğday ile çavdarın melezi olan triticale taneleri",
  ["Mantar teşekkülüne açık çavdar mahmuzu (ergot)",
   "Kahve yerine kullanılan kavrulmuş arpa",
   "Malt imalinde fırınlama sırasında ayrılan malt filizleri",
   "Şurup ve melas imalinde kullanılan tatlı darı (saccharatum)"],
  "10.08 Açıklama Notu, “diğer hububat” grubunda buğday ve çavdar melezi olan triticale gibi melez tane hububatı sayar; ürün Fasıl 10’dadır. "
  "Çavdar mahmuzu 12.11’e, kahve yerine kullanılan kavrulmuş arpa 21.01’e, malt filizleri 23.03’e, tatlı darılar ise 12.12’ye gider. "
  "Hepsi hububatla ilgili görünse de hububat tanesi niteliği taşımayan veya işlenmiş ürünlerdir.",
  "10.02, 10.03, 10.07 ve 10.08 Açıklama Notları.")

# 18
q(45, OL, "B",
  "Aşağıdaki tabii mantar eşyadan hangisi 45.03 pozisyonu kapsamı <b>dışında</b> kalır?",
  "Fişek tapası",
  ["Can kurtaran simidi", "Balıkçı ağı yüzdürücüsü", "Banyo paspası", "Bıçak sapı"],
  "45.03 Açıklama Notu, tabii mantardan can kurtaran simitlerini, balıkçı ağı yüzdürücülerini, banyo paspaslarını, masa altlıklarını "
  "ve bıçak sapı gibi sap tutacaklarını bu pozisyonda sayar. Aynı not fişek tapa mantarını pozisyon dışında bırakarak 93.06’ya gönderir. "
  "Balık oltalarına mahsus mantarlar gibi spor eşyası da Fasıl 95’e gider; ağ yüzdürücüleri ise 45.03’te kalır.",
  "45.03 Açıklama Notu.")

# 19
q(32, NT, "E",
  "Fasıl 32 notlarına göre, stabilize diazonyum tuzları ile azoik boyaların üretiminde kullanılan bağlayıcılardan oluşan karışımlar "
  "hangi pozisyonda sınıflandırılır?",
  "32.04", ["29.27", "32.06", "32.12", "38.24"],
  "Fasıl 32 Not 2, stabilize diazonyum tuzları ve azoik boyaların üretiminde kullanılan bağlayıcılardan oluşan karışımların 32.04’te "
  "yer aldığını hükme bağlar. Ürün karışım halinde olduğundan kimyaca belirli izole bileşikleri kapsayan Fasıl 29’a girmez; 38.24 gibi "
  "genel bir pozisyon da not hükmü karşısında uygulanmaz. 32.06 diğer boyayıcı maddeleri, 32.12 ise susuz ortamda dağılan pigmentleri "
  "ve perakende boyaları kapsar.",
  "Fasıl 32 Not 2.")

# 20
q(9, E4, "B",
  "Tarife Cetveline göre, geçici olarak salamurada korunmaya alınmış, bu haliyle hemen tüketilmeye elverişli olmayan taze zencefil "
  "hangi pozisyonda sınıflandırılır?",
  "09.10", ["07.11", "20.08", "12.11", "07.09"],
  "09.10 Açıklama Notu, geçici olarak salamurada korunmaya alınmış ve bu haliyle hemen tüketilmeye elverişli olmayan taze zencefili "
  "açıkça bu pozisyonda sayar; yalnızca şekerli şurup içinde korunmaya alınmış zencefil 20.08’e gider. Geçici korunmuş sebzeleri kapsayan "
  "07.11 tuzaktır: zencefil Fasıl 9’da baharat olarak özel şekilde tanımlanmıştır. 12.11 ise esas olarak parfümeri ve eczacılıkta "
  "kullanılan bitkiler içindir.",
  "09.10 Açıklama Notu.")

# 21
q(40, FA, "E",
  "Aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir bölümde sınıflandırılır?",
  "Adi metalden bir kaide, bir kulp ve vakum manivelası ile kauçuk disklerden oluşan vakumlu kap tutacağı",
  ["Gemi veya doklarda kullanılan, sertleştirilmemiş vulkanize kauçuktan çarpmayı önleyici tampon",
   "Kenarları şevlenmiş, iç lastik onarımına mahsus kauçuk yama",
   "Sertleştirilmemiş vulkanize kauçuktan lavabo pompası",
   "Mobilyalar için sertleştirilmemiş vulkanize kauçuktan ayak"],
  "40.16 Açıklama Notu; gemi ve doklarda kullanılan çarpmayı önleyici tamponları, iç lastik onarımına mahsus kenarları şevlenmiş "
  "yamaları, lavabo pompalarını ve mobilyalar için kauçuk ayakları bu pozisyonda, dolayısıyla Bölüm VII’de sayar. Aynı not, adi metalden "
  "kaide, kulp ve vakum manivelası ile kauçuk disklerden ibaret vakumlu kap tutacaklarını pozisyon dışında bırakarak Bölüm XV’e gönderir. "
  "Kauçuk disk içermesi bu eşyayı Fasıl 40’ta tutmaz.",
  "40.16 Açıklama Notu.")

# 22
q("GYK", GY, "D",
  "Bir firma aynı sevkiyatta; motor yağı doldurulmuş ve bu ürünün ambalajında normal olarak kullanılan türden, tekrar kullanılmaya "
  "elverişli olmayan plastik bidonlar ile ayrıca satılmak üzere getirilen aynı tip boş plastik bidonlar ithal etmektedir. GYK 5(b) "
  "çerçevesinde aşağıdakilerden hangisi doğrudur?",
  "Dolu bidonlar motor yağı ile birlikte yağın pozisyonunda; boş bidonlar ise ayrı olarak plastikten ambalaj eşyası pozisyonunda "
  "sınıflandırılır.",
  ["Dolu ve boş bütün bidonlar aynı sevkiyatta sunulduklarından motor yağı ile birlikte yağın pozisyonunda sınıflandırılır.",
   "Bidonlar dolu olsun boş olsun ayrı olarak plastikten ambalaj eşyası pozisyonunda, motor yağı ise kendi pozisyonunda sınıflandırılır.",
   "Dolu bidonlar GYK 5(a) uyarınca mahfaza sayılarak yağ ile birlikte, boş bidonlar ise GYK 2(a) uyarınca eksik eşya olarak yağın "
   "pozisyonunda sınıflandırılır.",
   "Plastik bidonlar sürekli kullanıma elverişli sayıldığından GYK 5(b) uygulanmaz; bütün bidonlar ayrı olarak sınıflandırılır."],
  "GYK 5(b), içindeki eşya ile birlikte sunulan ve o eşyanın ambalajında normal olarak kullanılan türden ambalaj madde ve "
  "mahfazalarının bu eşya ile birlikte sınıflandırılacağını öngörür; tekrar kullanıma elverişli olduğu açıkça belli olanlar bu hükmün "
  "dışındadır. Kural yalnız içindeki eşya ile birlikte sunulan ambalajlara uygulandığından boş bidonlar, aynı sevkiyatta gelseler de "
  "kendi pozisyonlarında (plastikten ambalaj eşyası olarak 39.23’te) sınıflandırılır. GYK 5(a) ise belli bir eşyaya göre şekil "
  "verilmiş, uzun süre kullanılmaya elverişli mahfazalarla ilgilidir.",
  "GYK 5(b) ve Açıklama Notu (IV); 39.23 pozisyon metni.")

# 23
q(51, E4, "A",
  "Tarife Cetveline göre, kullanılmış yatak ve yastıkların içinin boşaltılması sırasında elde edilen; karde edilmemiş, taranmamış ve "
  "ditme işlemi görmemiş yün döküntüleri hangi pozisyonda sınıflandırılır?",
  "51.03", ["51.04", "63.10", "51.01", "51.05"],
  "51.03 Açıklama Notu, yün ve hayvan kılı döküntüleri arasında kullanılmış yatak, yastık vb. eşyanın içindeki yün ve kılların "
  "boşaltılması sırasında oluşan döküntüleri açıkça sayar. Ditme suretiyle elde edilen döküntüler 51.04’e, karde edilmiş veya taranmış "
  "döküntüler 51.05’e, yalnızca gübre olarak kullanılmaya uygun olanlar Fasıl 31’e gider. 51.01 ise döküntü niteliği taşımayan karde "
  "edilmemiş ve taranmamış yünü kapsar.",
  "51.03 Açıklama Notu.")

# 24
q(16, OL, "C",
  "Aşağıdakilerden hangisi 16.04 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Yemeklere pişirilirken veya servis sırasında çeşni vermek için kullanılan sıvı balık sosu",
  ["Şarap veya sirke içinde baharat katılarak hazırlanmış marine ringa balığı",
   "Mersin balığı yumurtasından hazırlanmış, ezilerek homojen macun haline getirilmiş havyar",
   "Hava geçirmez kutuda sterilize edilmiş ton balığı",
   "Katı yağ ilavesiyle hazırlanmış somon balığı ezmesi"],
  "16.04 Açıklama Notu; şarap veya sirke içinde baharatla hazırlanmış marine balıkları, katı yağ ilavesiyle yapılan balık ezmelerini, "
  "ezilerek macun haline getirilmiş olanlar dahil havyarı ve hava geçirmez kaplardaki balık konservelerini bu pozisyonda sayar. Aynı "
  "not soslar ve diğer ilgili müstahzarları, karışık çeşni ve baharatları 21.03’e göndererek pozisyon dışında bırakır; 21.03 Açıklama "
  "Notu da balık sosunu çeşni sıvıları arasında açıkça anar. Balıktan elde edilmiş olması sosu 16.04’e getirmez.",
  "16.04 ve 21.03 Açıklama Notları.")

# 25
q(50, NT, "B",
  "Bölüm XI Not 1, insan saçını ve insan saçından eşyayı bu bölümün dışında bırakır. Bu notta yer alan istisna uyarınca, yağ "
  "preslerinde veya benzeri teknik işlerde kullanılan insan saçından mamul filtre veya tasir torbaları hangi pozisyonda sınıflandırılır?",
  "59.11", ["05.01", "67.04", "67.03", "63.05"],
  "Bölüm XI Not 1(b), insan saçını ve insan saçından eşyayı (05.01, 67.03 veya 67.04) bölüm dışında bırakırken, genellikle yağ "
  "preslerinde veya benzeri teknik işlerde kullanılan insan saçından filtre veya tasir torbaları ile kaba dokumaları ayrıca belirterek "
  "59.11’e gönderir. Böylece bu teknik eşya, insan saçından yapılmış olmasına rağmen Bölüm XI’de kalır. Torba biçimi, ürünü ambalaj "
  "çuvalı olarak 63.05’e de götürmez.",
  "Bölüm XI Not 1(b).")

# 26
q(84, FA, "E",
  "Sütçülükte kullanılan aşağıdaki makine ve cihazlardan hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
  "Sütü kaymağından ayıran santrifüjlü seperatör (kremöz)",
  ["Süt sağma makinesi",
   "Sütü homojen hale getirmeye mahsus makine",
   "Motorla döndürülen tereyağı yayığı",
   "Sert peynir imalinde kullanılan peynir presi"],
  "84.34 Açıklama Notu süt sağma makinelerini, sütü homojenleştiren makineleri, yayıkları ve peynir preslerini bu pozisyonda sayar. "
  "Aynı not, sütü kaymağından ayıran seperatörleri (kremözler) ile filtre-presleri ve diğer filtre veya arıtma makinelerini 84.21’e "
  "gönderir. Sütçülükte kullanılması kremözü 84.34’e getirmez; santrifüjle ayırma işlemi 84.21’in konusudur.",
  "84.34 Açıklama Notu; 84.21 pozisyon metni.")

# 27
q(42, ES, "A",
  "42.05 Açıklama Notuna göre; deriden yapılmış, içi doldurulmamış minder yüzü ………, deriyle kaplanmış içi doldurulmuş minder ………, "
  "deriden yapılmış yapma çiçek ise ……… pozisyonunda sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
  "42.05 – 94.04 – 67.02",
  ["42.05 – 42.05 – 67.02", "94.04 – 94.04 – 42.05", "42.02 – 94.04 – 42.05", "63.04 – 94.04 – 67.02"],
  "42.05 Açıklama Notu, deriden içi doldurulmamış minder yüzlerini bu pozisyonda sayarken içi dolu minderlerin 94.04’te "
  "sınıflandırıldığını belirtir. Aynı not yapma çiçek, yaprak ve meyveleri ile bunların aksamını pozisyon dışında bırakarak 67.02’ye "
  "gönderir. Deri maddesi tek başına 42.05’i belirlemez; doldurma işlemi ve eşyanın niteliği sonucu değiştirir.",
  "42.05 Açıklama Notu.")

# 28
q(78, E4, "D",
  "Tarife Cetveline göre, elektrolitik arıtmada kullanılmak üzere saf olmayan kurşundan dökülmüş anotlar hangi pozisyonda sınıflandırılır?",
  "78.01", ["78.06", "78.04", "85.45", "78.02"],
  "78.01 Açıklama Notu, saf olmayan kurşun külçesinden elektrolizle saflaştırılmış kurşuna kadar işlenmemiş kurşunu kapsar ve "
  "elektrolitik arıtma için döküm anotlarını da bu pozisyonda sayar. “Anot” adı eşyayı kurşundan diğer eşya (78.06) yapmaz; bu "
  "anotlar henüz arıtılacak işlenmemiş metaldir. 78.02 döküntü ve hurdaları, 85.45 ise kömür elektrotları kapsar.",
  "78.01 Açıklama Notu.")

# 29
q(65, OL, "C",
  "Tarife Cetveline göre aşağıdaki başlıklardan hangisi 65.05 pozisyonu kapsamı <b>dışında</b> kalır?",
  "Ait olduğu kolsuz cekete takılıp çıkarılabilen ve cekete birlikte sunulan kapüşon",
  ["Örülerek elde edilip keçeleştirilmiş fes",
   "Yağ emdirilmiş mensucattan geniş kenarlı gemici başlığı",
   "Mensucattan yapılmış aşçı başlığı",
   "Tülden yapılmış saç filesi"],
  "65.05 Açıklama Notu; fesleri, yağ emdirilmiş mensucattan gemici başlıklarını, aşçı ve hemşire başlıkları gibi mensucattan "
  "başlıkları, kapüşonları ve her türlü maddeden saç filelerini bu pozisyonda sayar. Ancak ait oldukları kolsuz ceket, pelerin vb. ile "
  "birlikte sunulan takılıp çıkarılabilir türden başlıklar pozisyon dışında bırakılır ve mamul bulundukları maddenin rejimine tabi "
  "tutulur. Tuzak, kapüşonların genel olarak 65.05’te sayılmasıdır.",
  "65.05 Açıklama Notu.")

# 30
q(31, NT, "B",
  "Fasıl 31 notlarına göre; 31.05’te belirtilen şekil veya ambalajlarda olmamak kaydıyla, amonyum klorürün tebeşir, alçı taşı veya "
  "bitki besin maddesi olmayan diğer anorganik maddelerle karıştırılmasından oluşan gübreler hangi pozisyonda sınıflandırılır?",
  "31.02", ["28.27", "31.05", "38.24", "31.04"],
  "Fasıl 31 Not 2(c), amonyum klorürün veya azotlu gübre tanımına giren ürünlerin tebeşir, alçı taşı ya da bitki besin maddesi "
  "olmayan diğer anorganik maddelerle karışımlarından oluşan gübreleri 31.02 kapsamında sayar. Saf amonyum klorür kimyaca belirli "
  "izole bileşik olarak Fasıl 31 dışında kalır (28.27); ancak bu karışım not hükmü gereği azotlu gübredir. Ürün tablet vb. şekillerde "
  "veya brüt ağırlığı 10 kg’ı geçmeyen ambalajlarda olsaydı 31.05 söz konusu olurdu.",
  "Fasıl 31 Not 1(b) ve Not 2(c); 31.05 pozisyon metni.")

# 31
q(7, FA, "E",
  "Sebze esaslı aşağıdaki ürünlerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  "Kurutulmuş sebzelerden yapılmış hazır çorba",
  ["Hava sızdırmaz teneke kutulara konulmuş soğan tozu",
   "Dondurulmadan önce buharda pişirilmiş ve tuz ilave edilerek dondurulmuş ıspanak",
   "Kabuğu çıkarılmış ve ikiye ayrılmış kuru bakla",
   "Dikim amacıyla ithal edilen sarımsak dişleri"],
  "Fasıl 7 Genel Açıklamaları, hava sızdırmaz kaplara konulmuş sebzelerin (teneke kutudaki soğan tozu gibi) ve ekim veya dikim "
  "amacına yönelik sebzelerin bu fasılda kaldığını belirtir; dondurulmadan önce buharda pişirilmiş ve tuz ilave edilmiş sebzeler "
  "07.10’da, kabuksuz kuru baklagiller 07.13’te yer alır. 07.12 Açıklama Notu ise kuru sebzelerden yapılmış hazır çorbaları fasıl "
  "dışında bırakarak 21.04’e gönderir. Esasının kuru sebze olması hazır çorbayı Fasıl 7’de tutmaz.",
  "Fasıl 7 Genel Açıklamalar; 07.10 ve 07.12 Açıklama Notları.")

# 32
q(33, E4, "D",
  "Tarife Cetveline göre, arı sütü içeren, ilaç niteliği taşımayan ve perakende kavanozlarda satılan cilt besleyici krem hangi "
  "pozisyonda sınıflandırılır?",
  "33.04", ["04.10", "30.04", "33.07", "21.06"],
  "33.04 Açıklama Notu; güzellik kremlerini, temizleme kremlerini ve arı sütü içerenler dahil cilt besleyicileri, ilaç niteliği "
  "taşımamak kaydıyla bu pozisyonda sayar. İçeriğindeki arı sütü ürünü gıda niteliğindeki hayvansal ürünlerin pozisyonuna götürmez; "
  "eşya bir cilt bakım müstahzarıdır. Bazı cilt rahatsızlıklarını tedavi eden kremler 30.03 veya 30.04’e giderdi; 33.07 ise tıraş, "
  "deodorant, banyo müstahzarları ile başka yerde yer almayan müstahzarlar içindir.",
  "33.04 pozisyon metni ve Açıklama Notu.")

# 33
q(39, CC, "C",
  "Aşağıdaki plastikten eşyadan hangileri 39.24 pozisyonunda sınıflandırılır?"
  "<br/>I. Plastikten sıcak su şişesi"
  "<br/>II. Duvara daimi olarak tespit edilmek üzere hazırlanmamış plastik diş fırçası tutacağı"
  "<br/>III. Plastikten kibrit kutusu kabı"
  "<br/>IV. Plastikten klozet kapağı ve oturağı",
  "I, II ve III",
  ["I ve II", "II ve IV", "I, III ve IV", "Yalnız III"],
  "39.24 Açıklama Notu; sıcak su şişelerini ve kibrit kutusu kaplarını diğer ev eşyası olarak, duvarlara daimi olarak tespit "
  "edilmemiş sabun kaplarını, havlu ve diş fırçası tutacaklarını da tuvalet eşyası olarak bu pozisyonda sayar. Alafranga tuvaletler, "
  "kapaklar ve oturaklar ise 39.22 pozisyon metninde hijyenik eşya olarak ayrıca belirtilmiştir. Duvara daimi tespit edilmek üzere "
  "hazırlanmış tutacaklar Fasıl 39 Not 11 gereği 39.25’e gideceğinden tespit şekli belirleyicidir.",
  "39.22 pozisyon metni; 39.24 Açıklama Notu; Fasıl 39 Not 11.")

# 34
q(44, SE, "A",
  "Bir firma; fıçı tahtalarından oluşan, ancak alt ve üst kapakları zıvana ile değil çivi ile tutturulmuş, kuru boya ve kimyasal "
  "madde taşımada kullanılan silindir biçimli ahşap kaplar ithal etmektedir. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
  "44.15", ["44.16", "44.21", "44.20", "44.07"],
  "44.16 pozisyonu, gövdeleri kapakların takılması için uçlarına zıvana açılmış fıçı tahtalarından oluşan ve çemberlerle korunan "
  "fıçıcılık mamulleriyle sınırlıdır. Açıklama Notu, alt ve üst kapakları çivi ile tutturulmuş fıçı tahtalarından oluşan mahfazaları "
  "44.16 dışında bırakarak 44.15’e gönderir; 44.15 Açıklama Notu da kuru boya, kimyasal maddeler vb. taşımada kullanılan silindir "
  "sandıkları sayar. Fıçı tahtasından yapılmış olması tuzaktır.",
  "44.15 ve 44.16 Açıklama Notları.")

# 35
q("GYK", GY, "B",
  "Bir firma, ahşap prefabrik bir evin tamamlanması için gereken bütün zorunlu unsurları aynı sevkiyatta, monte edilmemiş halde ithal "
  "etmektedir. Duvarlar kısmen monte edilmiş, kirişler ve direkler kalıp şeklinde kesilmiştir; eşik ve izolasyon malzemesi ise inşaat "
  "sahasında kesilmek üzere belirsiz uzunluklarda sunulmuştur. Sevkiyatta montaj için uygun miktarda çivi, tutkal ve boya da "
  "bulunmaktadır. Bu eşyanın sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
  "Eşyanın tamamı monte edilmemiş prefabrik yapı olarak 94.06’da sınıflandırılır; sahada kesilecek unsurların bulunması bu sonucu "
  "değiştirmez.",
  ["Sahada kesilecek unsurlar daha ileri işçilik gerektirdiğinden GYK 2(a) uygulanmaz; her unsur kendi pozisyonunda sınıflandırılır.",
   "Yapı unsurları 94.06’da, çivi, tutkal ve boya ise kendi pozisyonlarında ayrı ayrı sınıflandırılır.",
   "Unsurlar ahşaptan olduğundan GYK 3(b) uyarınca esas niteliği veren ahşabın pozisyonunda, 44.18’de sınıflandırılır.",
   "Yapı henüz monte edilmediğinden ayrı olarak getirilen bina parçaları gibi işlem görür ve 44.18’de sınıflandırılır."],
  "94.06 Açıklama Notu, prefabrik yapıların tamamlanmış ancak monte edilmemiş halde de sunulabileceğini ve bu durumda zorunlu "
  "unsurların kısmen monte edilmiş, kalıp şeklinde kesilmiş ya da bazı hallerde inşaat sahasında kesilmek üzere belirsiz uzunluklarda "
  "olabileceğini belirtir; bu, GYK 2(a)’nın demonte eşyaya ilişkin kısmının pozisyona özgü uygulamasıdır. Aynı not, yapının "
  "tamamlanması veya montajı için gerekli çivi, tutkal, sıva, boya gibi malzemelerin uygun miktarlarda olmak şartıyla yapıyla birlikte "
  "sınıflandırılacağını hükme bağlar. Ayrı olarak getirilen bina parçaları ise kendi pozisyonlarında yer alır; bu sevkiyatta bütün "
  "zorunlu unsurlar birlikte sunulmuştur.",
  "GYK 2(a); 94.06 Açıklama Notu.")

# 36
q(75, OL, "D",
  "Aşağıdakilerden hangisi 75.01 pozisyonunda <b>yer almaz</b>?",
  "Nikel üretiminden kalan cüruf, kül ve artıklar",
  ["Nikel matları", "Nikel oksit sinterleri", "Saf olmayan ferro-nikel", "Nikel speissleri"],
  "75.01 Açıklama Notu nikel matlarını ve nikel metalürjisinin diğer ara ürünlerini, yani saf olmayan nikel oksitleri (nikel oksit "
  "sinterleri dahil), çelik sanayiinde ön arıtma olmaksızın kullanılamayan saf olmayan ferro-nikeli ve arseniyür karışımı olan nikel "
  "speisslerini kapsar. Nikelin cüruf, kül ve artıkları ise 75.03 Açıklama Notu uyarınca 26.20’de sınıflandırılır. Rafine edilmiş "
  "ferro-nikelin ferro-alyaj olarak 72.02’ye gittiği de unutulmamalıdır.",
  "75.01 ve 75.03 Açıklama Notları.")

# 37
q(97, NT, "A",
  "Fasıl 97 Not 2’ye göre 97.01 pozisyonu aşağıdakilerden hangisine <b>uygulanmaz</b>?",
  "Sanatçı tarafından tasarlanmış olsa da ticari nitelikte seri halde üretilmiş mozaik reprodüksiyonları",
  ["Küçük seramik parçaların elle yan yana getirilmesiyle yapılmış, ticari karakter taşımayan mozaik pano",
   "Mürekkepli kalemle tamamen elle yapılmış çizim",
   "Ünlü bir tablonun tamamen elle yapılmış kopyası",
   "Guaş boya ile kağıt üzerine elle yapılmış minyatür"],
  "Fasıl 97 Not 2, 97.01 pozisyonunun, sanatçılar tarafından tasarlanmış veya yaratılmış olsalar bile ticari nitelikteki geleneksel "
  "zanaatkârlığın seri üretim reprodüksiyonları, kalıpları veya eserleri olan mozaiklere uygulanmayacağını belirtir. Elle yapılan ve "
  "ticari karakter taşımayan mozaikler, guaş veya mürekkepli kalemle tamamen elle yapılmış resimler ve orijinal resimlerin tamamen elle "
  "yapılmış kopyaları ise sanatsal değeri ne olursa olsun 97.01’de kalır.",
  "Fasıl 97 Not 2; 97.01 Açıklama Notu.")

# 38
q(85, FA, "E",
  "Elektrik tesisatında kullanılan aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
  "Elektrik bağlantılarını sağlamaya mahsus terminallerle donatılmış T şeklinde rakor",
  ["Montaj amacıyla döküm sırasında içine küçük metal vida yuvaları gömülmüş, plastikten sigorta kaidesi",
   "Lamba duyunun izole edici iç kısmı",
   "İç yüzeyi elektriğe karşı izole edici özel bir vernikle kaplanmış, adi metalden tesisat borusu",
   "İç yüzeyi kağıtla izole edilmiş adi metalden tesisat borusu dirseği"],
  "85.47 pozisyonu; montaj amacıyla döküm sırasında gömülmüş küçük metal parçalar içerse de tamamen izole edici maddeden yapılmış "
  "izole edici bağlantı parçalarını (sigorta kaideleri, lamba duylarının izole edici iç kısımları gibi) ve iç yüzeyleri elektriğe karşı "
  "izole edilmiş adi metal borular ile bunların bağlantı parçalarını kapsar. Açıklama Notu, elektrik bağlantılarını sağlamaya mahsus "
  "terminallerle donatılmış manşon ve T rakorları 85.47 dışında bırakarak 85.35 veya 85.36’ya gönderir.",
  "85.47 pozisyon metni ve Açıklama Notu.")

# 39
q(23, ES, "C",
  "Tarife Cetveline göre; şeker kamışının özsuyu çıkarıldıktan sonra kalan lifli kısım (bagas) ………, şeker kamışı bagası pulpu ………, "
  "şekerin ekstraksiyonundan veya rafine edilmesinden arta kalan melas ise ……… pozisyonunda sınıflandırılır. Boşluklara sırasıyla "
  "aşağıdakilerden hangisi gelmelidir?",
  "23.03 – 47.06 – 17.03",
  ["23.08 – 47.06 – 23.03", "23.03 – 23.08 – 23.09", "14.04 – 47.06 – 17.03", "23.03 – 23.08 – 17.03"],
  "23.03 pozisyon metni şeker kamışı bagasını ve şeker sanayiinin diğer artıklarını açıkça sayar; Açıklama Notu da kâğıt imalinde ve "
  "hayvan gıdası hazırlanmasında kullanılan bagası bu pozisyonda gösterir. Aynı not, şeker kamışı bagası pulpunu 47.06’ya, şekerin "
  "ekstraksiyonundan veya rafinesinden arta kalan melası 17.03’e göndererek pozisyon dışında bırakır. Bagasın lifli yapısı 14.04 veya "
  "23.08 gibi pozisyonları akla getirse de pozisyon metni belirleyicidir.",
  "23.03 pozisyon metni ve Açıklama Notu.")

# 40
q(79, E4, "D",
  "Tarife Cetveline göre, baskı yapılacak resim ve yazının yüzeyine işlenmesiyle baskıya hazır hale getirilmiş çinko klişe levhası "
  "hangi pozisyonda sınıflandırılır?",
  "84.42", ["79.05", "79.07", "49.11", "83.10"],
  "79.05 Açıklama Notu, çinko sac ve levhaların fotogravür, litografya ve diğer baskı levhaları olarak kullanıldığını belirtmekle "
  "birlikte, 84.42 pozisyonunda yer alan hazırlanmış klişe levhalarını bu pozisyon dışında bırakır. Baskı yüzeyi işlenmiş levha artık "
  "yarı mamul çinko levha değildir. 79.07 çinkodan diğer eşyayı, 83.10 ise bilgi taşıyan işaret levhaları ve etiketleri kapsar.",
  "79.05 Açıklama Notu.")

# 41
q(3, CC, "B",
  "03.02 pozisyonuna ilişkin aşağıdaki ifadelerden hangileri doğrudur?"
  "<br/>I. Nakledilmeleri sırasında geçici olarak muhafaza edilmek üzere tuz veya buzla paketlenmiş taze balıklar 03.02’de kalır."
  "<br/>II. Şekerle hafifçe işlem görmüş veya birkaç defne yaprağıyla paketlenmiş taze balıklar 03.02’de yer alır."
  "<br/>III. Gövdenin geri kalanından ayrılmış taze yüzme keseleri ve balık dilleri 03.02’de sınıflandırılır."
  "<br/>IV. Kılçıkları ayıklanmış taze balık filetoları 03.02’de sınıflandırılır.",
  "I, II ve III",
  ["I ve II", "II ve IV", "I, III ve IV", "Yalnız II"],
  "03.02 Açıklama Notu; nakil sırasında geçici muhafaza için tuz veya buzla paketlenmiş ya da tuzlu su püskürtülmüş balıkları, "
  "şekerle hafifçe işlem görmüş veya birkaç defne yaprağıyla paketlenmiş balıkları ve gövdeden ayrılmış yenilebilir balık sakatatını "
  "(deriler, kuyruklar, yüzme keseleri, başlar, mideler, yüzgeçler, diller vb.) bu pozisyonda sayar. Pozisyon metni ise 03.04’teki balık "
  "filetolarını ve diğer balık etlerini açıkça hariç tuttuğundan IV yanlıştır.",
  "03.02 pozisyon metni ve Açıklama Notu.")

# 42
q(96, GY, "C",
  "Bir havayolu şirketi, uçuş sırasında veya bagajı bulunamayan yolculara dağıtılmak üzere; dokuma bir çanta içinde diş fırçası, tarak, "
  "kozmetik ürünler, selüloz mendil, tişört ve pijamadan oluşan setler ithal etmektedir. Bu setlerin sınıflandırılmasıyla ilgili "
  "aşağıdakilerden hangisi doğrudur?",
  "96.05 dışında kalır; seti oluşturan parçaların her biri kendi uygun pozisyonunda sınıflandırılır.",
  ["Seyahat tuvalet takımı olarak GYK 1 uyarınca 96.05’te sınıflandırılır.",
   "Takıma esas niteliğini çanta verdiğinden GYK 3(b) uyarınca 42.02’de sınıflandırılır.",
   "Takıma esas niteliğini giysiler verdiğinden GYK 3(b) uyarınca giyim eşyasının pozisyonunda sınıflandırılır.",
   "Esas nitelik saptanamadığından GYK 3(c) uyarınca numara sırasına göre en son pozisyonda sınıflandırılır."],
  "96.05 pozisyonu tuvalet, dikiş veya ayakkabı temizleme amaçlı seyahat takımlarını pozisyon metniyle, yani GYK 1 uyarınca kapsar. "
  "Ancak 96.05 Açıklama Notu, havayollarınca yolculara dağıtılan ve bu tür eşyanın yanında kozmetik ürünleri, selüloz mendilleri ve "
  "pijama, tişört gibi tekstil ürünlerini içeren setleri açıkça pozisyon dışında bırakır ve seti oluşturan parçaların kendi uygun "
  "pozisyonlarında sınıflandırılacağını belirtir. Bu hüküm karşısında GYK 3(b) veya 3(c) ile tek bir pozisyon aranmaz.",
  "96.05 Açıklama Notu; GYK 1.")

# 43
q(34, OL, "A",
  "Aşağıdakilerden hangisi 34.03 pozisyonunda <b>sınıflandırılmaz</b>? (Ürünlerin hiçbiri esas madde olarak ağırlıkça %70 veya "
  "daha fazla petrol yağı içermemektedir.)",
  "Kesme yağı müstahzarlarının imalinde kullanılan, esası petrol sülfonatları olan ve doğrudan kesme işlerinde kullanılmaya elverişli "
  "olmayan müstahzar",
  ["Tel çekme haddelerinde demir çubukların kolayca kaymasını sağlayan, don yağı ve sülfürik asidin sulu emülsiyonundan oluşan müstahzar",
   "Başlıca bileşimini yağlama yağlarının oluşturduğu, çözücü ve pas giderici de içeren cıvata ve somun gevşetme müstahzarı",
   "Vazelin ve kalsiyum sabunlarından ibaret, bağlantı contalarının montajında kullanılan sertleşmeyi önleyici pat",
   "Makinelerin hareketli kısımları arasındaki sürtünmeyi azaltmaya mahsus, hayvansal ve mineral yağ karışımından oluşan yağlama müstahzarı"],
  "34.03 Açıklama Notu; makinelerin hareketli kısımlarına mahsus yağlama müstahzarlarını, tel çekme haddelerine mahsus müstahzarları "
  "(don yağı ve sülfürik asidin sulu emülsiyonları gibi), cıvata ve somun gevşetme müstahzarlarını ve vazelin ile kalsiyum "
  "sabunlarından ibaret sertleşmeyi önleyici patları bu pozisyonda sayar. Aynı not, kesme işlerine mahsus yağlama müstahzarlarının "
  "imalinde kullanılan fakat doğrudan kesme işlerinde kullanılmaya elverişli olmayan, esası petrol sülfonatları veya diğer yüzey aktif "
  "ürünler olan müstahzarları 34.02’ye gönderir. Belirleyici olan, ürünün kendisinin yağlayıcı olarak kullanılabilir olmasıdır.",
  "34.03 Açıklama Notu.")

# 44
q(15, NT, "E",
  "15.15 Açıklama Notuna göre “mikrobiyal katı ve sıvı yağlar” ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Tek hücreli yağlar olarak da bilinir; mayalar dahil mantarlar, bakteriler ve mikroalgler gibi yağlı mikroorganizmalardan lipidlerin "
  "çıkarılmasıyla elde edilir.",
  ["Fasıl 15 kapsamı dışında olup gıda müstahzarı olarak 21.06’da sınıflandırılır.",
   "Yalnız hidrojene edildikleri takdirde Fasıl 15’te yer alır.",
   "Hayvansal kökenli sayıldıklarından 15.06’da sınıflandırılır.",
   "Yalnız mikroalglerden elde edilenler Fasıl 15’te yer alır; maya kökenli olanlar 21.02’dedir."],
  "15.15 Açıklama Notu, mikrobiyal katı ve sıvı yağları tek hücreli yağlar (SCO) olarak da tanımlar ve bunların mantarlar (mayalar "
  "dahil), bakteriler ve mikroalgler gibi yağlı mikroorganizmalardan lipidlerin çıkarılmasıyla elde edildiğini belirtir. Basit ve "
  "kimyasal olarak değiştirilmemiş mikrobiyal yağlar 15.15’te yer alır; fasıl başlığı da mikrobiyal yağları açıkça anar. Maya kaynaklı "
  "olmaları, ürünü mayaları kapsayan 21.02’ye götürmez.",
  "15.15 Açıklama Notu; Fasıl 15 Genel Açıklamalar.")

# 45
q(89, SE, "D",
  "Bir armatör; ticari balıkçılık için ağlarla donatılmış, avlanan balıkların muhafazasına mahsus bölümleri bulunan, turizm "
  "mevsiminde ise gezi amacıyla da kullanılan bir balıkçı gemisi ithal etmektedir. Tarife Cetveline göre bu gemi hangi pozisyonda "
  "sınıflandırılır?",
  "89.02", ["89.01", "89.03", "89.06", "89.05"],
  "89.02 Açıklama Notu, deniz veya kara sularında ticari balıkçılık yapmak için düzenlenmiş her türlü balıkçı gemisini kapsar ve turizm "
  "mevsiminde gezi amaçlı da kullanılabilen balıkçı gemilerinin bu pozisyonda sınıflandırıldığını açıkça belirtir. Gezinti gemileri "
  "89.01’de, balıkçı sandalları ile spor olarak kullanılan balıkçı araçları ise 89.03’te yer alır. Geminin dönemsel olarak gezi amaçlı "
  "kullanılması sınıflandırmayı değiştirmez.",
  "89.02 Açıklama Notu.")

# 46
q(40, NT, "B",
  "Fasıl 40 Not 3’e göre 40.01 ila 40.03 ve 40.05 pozisyonlarındaki “ilk şekiller” tabirine aşağıdakilerden hangisi <b>dahil değildir</b>?",
  "Dikdörtgen (kare dahil) şeklinde basitçe kesilmiş levha ve yapraklar",
  ["Prevulkanize edilmiş olsun olmasın lateks ve diğer dispersiyonlar",
   "Düzensiz şekillerdeki bloklar ve biçimsiz parçalar",
   "Balyalar",
   "Tozlar, granüller ve kırıntılar"],
  "Fasıl 40 Not 3, “ilk şekiller” tabirini sınırlı olarak tanımlar: sıvı veya hamurlar (prevulkanize olsun olmasın lateks, diğer "
  "dispersiyonlar ve çözeltiler dahil) ile düzensiz şekillerdeki bloklar, biçimsiz parçalar, balyalar, tozlar, granüller, kırıntılar ve "
  "benzeri düzensiz biçimler. Dikdörtgen kesilmiş levha ve yapraklar ilk şekil sayılmaz; bunlar Not 9’da ayrıca tanımlanan “levhalar, "
  "yapraklar ve şeritler” kapsamındadır. Aynı pozisyonlar her iki şekli de kapsadığından ayrım tanım düzeyinde önem taşır.",
  "Fasıl 40 Not 3 ve Not 9.")

# 47
q("GYK", GY, "C",
  "Bir hava kompresörü, yalnızca bu kompresörün basıncını göstermek üzere yapılmış ve üzerine takılacak şekilde hazırlanmış bir "
  "manometre ile birlikte aynı sevkiyatta gümrüğe sunulmuştur. Manometre ayrı sunulsaydı 90.26 pozisyonunda yer alacaktı. Bölüm XVI "
  "Genel Açıklamaları ve Genel Yorum Kuralları çerçevesinde aşağıdakilerden hangisi doğrudur?",
  "Manometre, ait olduğu kompresörle birlikte kompresörün pozisyonunda sınıflandırılır.",
  ["Manometre ayrı olarak 90.26’da, kompresör ise kendi pozisyonunda sınıflandırılır.",
   "Ölçü aleti daha özel tanımlandığından GYK 3(a) uyarınca bütün eşya 90.26’da sınıflandırılır.",
   "Manometrenin kompresörle birlikte sınıflandırılabilmesi için çeşitli makinelerde kullanılabilecek türden olması gerekir.",
   "Manometre GYK 5(a) uyarınca kompresörün mahfazası gibi işlem görerek onunla birlikte sınıflandırılır."],
  "Bölüm XVI Genel Açıklamaları (III), ait oldukları makine ile birlikte sunulan manometre, termometre gibi yardımcı alet ve "
  "cihazların, o makineye mahsus ölçü, ayar veya kontrol cihazlarından olmaları halinde makinenin pozisyonunda sınıflandırılacağını "
  "belirtir ve GYK 2(a) ile 3(b)’ye atıf yapar. Çeşitli makinelerde kullanılmaya mahsus türden yardımcı aletler ise kendi "
  "pozisyonlarında yer alır. Kompresöre mahsus manometre bu nedenle 90.26’ya ayrılmaz; GYK 5(a) ise mahfaza ve kutularla ilgilidir.",
  "Bölüm XVI Genel Açıklamalar (III); GYK 2(a) ve 3(b).")

# 48
q(84, CC, "A",
  "Fasıl 84 Not 1’e göre aşağıdakilerden hangileri, makine veya cihaz niteliğinde olsalar bile Fasıl 84 <b>dışında</b> sınıflandırılır?"
  "<br/>I. Seramikten yapılmış pompa"
  "<br/>II. Laboratuvarlarda kullanılan camdan damıtma cihazı"
  "<br/>III. Ev tipi bulaşık yıkama makinesi"
  "<br/>IV. El ile kullanılan, motorsuz mekanik yer süpürgesi",
  "I, II ve IV",
  ["I ve II", "II ve III", "III ve IV", "I, III ve IV"],
  "Fasıl 84 Not 1; seramikten mamul makine, cihaz ve aletleri (pompalar gibi) Fasıl 69’a, laboratuvarlar için cam eşyayı 70.17’ye, "
  "el ile kullanılan motorsuz mekanik yer süpürgelerini ise 96.03’e bırakarak fasıl dışında tutar. Bulaşık yıkama makineleri ise ev "
  "tipi olsalar dahi 84.22’de kalır; Fasıl 85 Not 4 de bunları 85.09 kapsamı dışında bırakır.",
  "Fasıl 84 Not 1; Fasıl 85 Not 4.")

# 49
q(52, SE, "D",
  "Ağırlıkça %100 pamuktan, ağartılmış, çok katlı bükülü (rötor), 2.500 desiteks bir iplik; çapraz sarılmamış çileler halinde ve her "
  "bir çile 400 g ağırlığında sunulmaktadır. İplik dikiş ipliği niteliğinde değildir. Tarife Cetveline göre bu iplik hangi pozisyonda "
  "sınıflandırılır?",
  "52.07", ["52.04", "52.05", "52.06", "56.07"],
  "Bölüm XI Not 4(A)(b), top veya çile halindeki ipliklerde 2.000 desiteksten az “diğer” iplikler için 125 g, diğer iplikler için 500 g "
  "sınırını öngörür; 2.500 desiteks pamuk ipliği 500 g sınırına tabidir ve 400 g’lık çileler bu şartı sağlar. İplik ağartılmış olduğundan "
  "çile halindeki ağartılmamış çok katlı ipliklere ilişkin istisnaya, çapraz sarılmamış olduğundan da çapraz sarılmış çile istisnasına "
  "girmez; bu nedenle perakende satış için hazırlanmış sayılır ve 52.07’de yer alır. 125 g sınırının uygulanması tuzaktır; 20.000 "
  "desiteksi aşmadığından 56.07’deki sicim tanımına da girmez.",
  "Bölüm XI Not 3(A) ve Not 4; 52.07 pozisyon metni.")

# 50
q(85, SE, "E",
  "Bir otel işletmesi; odalardaki çağırma düğmelerine basıldığında resepsiyondaki büyük bir tablo üzerinde ilgili oda numarasının "
  "ışıklı olarak belirmesini sağlayan elektrikli oda çağrı göstergeleri (oda endikatörleri) ithal etmektedir. Cihazların telefon veya "
  "veri iletimi işlevi yoktur. Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
  "85.31", ["85.37", "85.17", "85.30", "94.05"],
  "85.31 pozisyonu kulağa veya göze hitap eden elektrikli işaret cihazlarını kapsar; Açıklama Notu, işaret tabloları arasında üzerinde "
  "oda numaraları bulunan ve bir odada çağırma düğmesine basılınca ilgili numarayı ışıkla veya flapla gösteren oda endikatörlerini "
  "açıkça sayar. “Tablo” ifadesi elektrik kontrol ve dağıtım tablolarını kapsayan 85.37’yi çağrıştırsa da cihaz elektriği kontrol "
  "etmez, yalnız uyarı verir. Telefon işlevi olmadığından 85.17, trafik kontrolü amaçlı olmadığından 85.30 uygun değildir; statik "
  "ışıklı panolar ise 94.05 gibi pozisyonlara gider.",
  "85.31 pozisyon metni ve Açıklama Notu.")


assert len(Q) == 50, len(Q)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"tur": "deneme", "no": 8, "sorular": Q}, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT)
