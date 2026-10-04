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
  "Tarife Cetveline göre, kahve yerine kullanılmak üzere kavrulmuş ve ufalanmış kestane hangi pozisyonda sınıflandırılır?",
  "21.01", ["08.02", "08.13", "20.08", "09.01"],
  "Fasıl 8 Genel Açıklamaları, genellikle kahve yerine kullanılan kavrulmuş meyve ve sert kabuklu meyveleri "
  "(örneğin kestane, badem ve incir; ufalanmış olsun olmasın) fasıl dışında bırakarak 21.01’e gönderir. "
  "Kestanenin taze veya kurutulmuş hali 08.02’de kalırdı; kavurma ve kahve ikamesi niteliği ürünü Fasıl 8’den çıkarır. "
  "09.01 yalnız içinde herhangi bir oranda kahve bulunan kahve yerine kullanılan maddeleri kapsar.",
  "Fasıl 8 Genel Açıklamalar; 09.01 pozisyon metni.")

# 2
q("GYK", GY, "A",
  "Genel Yorum Kuralı 1’in açıklama notunda, diğer yorum kurallarına başvurulmasına gerek kalmaksızın yalnızca pozisyon "
  "metni veya notlar uyarınca sınıflandırılabilen eşyaya örnek olarak aşağıdakilerden hangisi gösterilmiştir?",
  "Canlı atlar (01.01)",
  ["Kendinden motorlu saç ve sakal tıraş makineleri (85.10)",
   "Motorlu taşıtlarda kullanılan tufte halılar (57.03)",
   "Spagetti, rendelenmiş peynir ve domates sosundan oluşan takım (19.02)",
   "Dürbünle birlikte sunulan dürbün mahfazası (90.05)"],
  "GYK 1 açıklama notu (III)(a), birçok eşyanın yorum kurallarına gerek kalmadan pozisyon metinleri ve notlarla "
  "sınıflandırılabileceğini belirtir ve canlı atları (01.01) ile Fasıl 30 Not 4 uyarınca eczacılık müstahzarlarını (30.06) örnek verir. "
  "Tıraş makineleri ve tufte halılar GYK 3(a)’nın, spagetti takımı GYK 3(b)’nin, dürbün mahfazası ise GYK 5(a)’nın "
  "açıklama notlarındaki örneklerdir.",
  "GYK 1 Açıklama Notu (III)(a).")

# 3
q(64, E4, "E",
  "Tarife Cetveline göre, dış tabanı keçeden, yüzü tabii deriden yapılmış ve ev içinde giyilen terlik hangi pozisyonda sınıflandırılır?",
  "64.05", ["64.03", "64.04", "64.06", "64.02"],
  "64.01 ila 64.04 pozisyonları dış tabanı kauçuk, plastik, tabii veya terkip yoluyla elde edilen deri olan ayakkabılarla sınırlıdır. "
  "64.05 Açıklama Notu, dış tabanı ağaç, mantar, sicim, karton, kürk, mensucat, keçe vb. olan ayakkabıları, yüzü hangi maddeden "
  "olursa olsun bu pozisyonda sayar. Yüzün deri olması tuzaktır: 64.03 için dış tabanın da kauçuk, plastik veya deri olması gerekir.",
  "Fasıl 64 Not 4(b); 64.03 pozisyon metni; 64.05 Açıklama Notu.")

# 4
q(24, OL, "B",
  "Aşağıdakilerden hangisi 24.03 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Tütün hülasası içeren, perakende ambalajlı böcek öldürücü müstahzar",
  ["Enfiye imali için sıkıştırılmış veya likörlenmiş tütün",
   "Tütün saplarından elde edilen selüloz tabakalar üzerine aglomere edilmiş yeniden tertip edilmiş tütün",
   "Tütün artıklarının su içinde kaynatılmasıyla hazırlanmış tütün hülasası",
   "Pipoda içilmek üzere hazırlanmış, tütün içermeyen bitkisel karışım"],
  "24.03 Açıklama Notu; enfiye imaline mahsus sıkıştırılmış veya likörlenmiş tütünü, mesnet üzerinde olsun olmasın yeniden tertip "
  "edilmiş tütünü, tütün hülasa ve esanslarını ve tütün içermeyen içilen karışımları (mamul tütün yerine geçen ürünler) bu pozisyonda sayar. "
  "Aynı not, 38.08 pozisyonunda yer alan böcek öldürücüleri pozisyon dışında bırakır. Tuzak, tütün hülasalarının esas olarak böcek "
  "ilacı imalinde kullanılmasıdır: hülasanın kendisi 24.03’te, ondan hazırlanmış böcek öldürücü ise 38.08’dedir.",
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
  "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
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
  "Tarife Cetveline göre; önceden küçük parçalara ayrılmamış veya kıyma haline getirilmemiş, başka madde katılmamış, tuzlanıp "
  "tütsülenerek tabii bir bağırsak kılıf içine alınmış, pişirilmemiş bütün domuz kol eti hangi pozisyonda sınıflandırılır?",
  "02.10", ["16.01", "16.02", "02.03", "05.04"],
  "02.10 Açıklama Notuna göre tuzlanmış, kurutulmuş veya tütsülenmiş etler (domuzun sırt, but, kol etleri gibi), önceden küçük "
  "parçalara ayrılmamış veya kıyma haline getirilmemiş ve diğer maddelerle kombine edilmemiş olmak şartıyla bağırsak, mesane, deri veya "
  "benzeri kılıflara alınmış olsalar da bu pozisyonda kalır. Kılıf ürünü kendiliğinden sosis yapmaz; 16.01 doğranmış veya kıyılmış et "
  "müstahzarlarını kapsar. Bağırsakların kendisi ise 05.04’te yer alır.",
  "02.10 Açıklama Notu; 16.01 Açıklama Notu.")

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
  "Aşağıdaki ürünlerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  "Kakao ile aromalandırılmış, sütten mamul meşrubat",
  ["Keçi sütünden elde edilmiş tereyağı",
   "Sulu hamurla kaplanıp önceden pişirilmiş, ancak peynir karakterini koruyan peynir",
   "Silindir şeklinde kalıplanmış kabuksuz yumurtalar (“uzun yumurtalar”)",
   "Petek parçaları içeren tabii bal"],
  "04.02 Açıklama Notu, kakao veya diğer maddelerle aromalandırılmış, sütten mamul meşrubatı pozisyon dışında bırakarak 22.02’ye "
  "gönderir. Keçi veya koyun sütünden tereyağı 04.05’te, peynir karakterini korumak şartıyla sulu hamurla kaplanmış ve önceden "
  "pişirilmiş peynirler 04.06’da, kalıplanmış “uzun yumurtalar” 04.08’de, petek parçaları içeren bal 04.09’da, yani hepsi Fasıl 4’te kalır.",
  "04.02, 04.05, 04.06, 04.08 ve 04.09 Açıklama Notları.")

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
  "27.15 Açıklama Notuna göre; katranlı makadam (katranla karıştırılmış taş kırıkları) ………, katran ile aglomere edilmiş dolomit ………, "
  "kullanılmadan önce tekrar eritilmek üzere bloklar halinde aglomere edilmiş asfalt sakızı ise ……… pozisyonunda sınıflandırılır. "
  "Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
  "25.17 – 25.18 – 27.15",
  ["27.15 – 25.18 – 68.07", "25.17 – 27.15 – 68.07", "27.14 – 25.18 – 27.15", "25.17 – 25.18 – 68.07"],
  "27.15 Açıklama Notu, katranlı makadamı 25.17’ye, katranla aglomere edilmiş dolomiti 25.18’e göndererek pozisyon dışında bırakır. "
  "Asfalt sakızı gibi bitümenli karışımların kullanılmadan önce yeniden eritilmek üzere blok vb. şekillerde aglomere edilmiş olanları "
  "27.15’te kalır; yalnızca kaldırım taşı, levha gibi son şeklini almış mamuller 68.07’ye gider. 27.14 ise tabii bitümen ve tabii asfalt içindir.",
  "27.14 ve 27.15 Açıklama Notları.")

# 16
q(85, E4, "C",
  "Tarife Cetveline göre, bisiklet tekerleğinin jantı veya dış lastiği üzerinde çalışan bir sürtünme çarkı aracılığıyla elektrik üreten "
  "ve yalnızca aydınlatmada kullanılan bisiklet dinamosu hangi pozisyonda sınıflandırılır?",
  "85.12", ["85.01", "85.11", "87.14", "85.13"],
  "85.12 Açıklama Notu, bisiklet ve motorlu kara taşıtlarına mahsus elektrikli aydınlatma ve işaret cihazları arasında tekerleğin jantı "
  "veya lastiği üzerinde çalışan sürtünme çarkıyla elektrik üreten dinamoları sayar; 85.11 Açıklama Notu da bisikletlerde yalnızca "
  "aydınlatma için kullanılan dinamoları kendi kapsamı dışında bırakır. Fasıl 85 Not 2 gereği 85.12’de tarif edilen eşya 85.01 ila 85.04 "
  "pozisyonlarına giremez. Bölüm XVII Not 2 elektrikli cihazları taşıt aksamı kapsamından çıkardığından 87.14 de uygun değildir.",
  "Fasıl 85 Not 2; 85.11 ve 85.12 Açıklama Notları; Bölüm XVII Not 2(f).")

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
  "Tabii mantardan yapılmış olsa bile aşağıdakilerden hangisi 45.03 pozisyonunda <b>sınıflandırılmaz</b>?",
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
  "GYK 3(b) açıklama notuna göre bu kural yalnızca belirli eşya gruplarına uygulanır. Aşağıdakilerden hangisi bu gruplar arasında "
  "<b>sayılmamıştır</b>?",
  "Birleştirilmemiş veya demonte halde sunulan tamamlanmış eşya",
  ["Karışımlar",
   "Çeşitli maddelerden oluşan bileşik eşya",
   "Çeşitli eşyanın birleşmesinden meydana gelen bileşik eşya",
   "Perakende satılacak hale getirilmiş takım halinde bulunan eşya"],
  "GYK 3(b) açıklama notu (VI), kuralın yalnızca karışımlar, çeşitli maddelerden oluşan bileşik eşya, çeşitli eşyanın birleşmesinden "
  "meydana gelen bileşik eşya ve perakende satılacak hale getirilmiş takımlarla ilgili olduğunu ve ancak 3(a) yetersiz kaldığında "
  "uygulanacağını belirtir. Birleştirilmemiş veya demonte sunulan tamamlanmış eşya ise GYK 2(a)’nın ikinci kısmının konusudur ve monte "
  "edilmiş eşya ile aynı pozisyonda sınıflandırılır.",
  "GYK 3(b) Açıklama Notu (VI); GYK 2(a) Açıklama Notu (V).")

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
  "Çiğ balığın preslenmesiyle elde edilen balık suyu",
  ["Katı yağ ilave edilerek hazırlanmış hamsi ezmesi",
   "Şarap veya sirke içinde baharat katılarak hazırlanmış marine balık",
   "Pastörize edilmiş balık",
   "Hazırlanmış balık karaciğerleri"],
  "16.04 Açıklama Notu; marine balıkları, katı yağ ilavesiyle yapılan hamsi ve somon ezmelerini, hazırlanmış balık yumurtası ve "
  "karaciğerlerini, pastörize veya sterilize edilmiş balıkları bu pozisyonda sayar. Aynı not balık hülasa ve sularını 16.04 dışında "
  "bırakır; 16.03 Açıklama Notu da çiğ balığın preslenmesiyle elde edilen suları 16.03’te sınıflandırır. Ürünün balıktan elde edilmiş "
  "olması 16.04 için yeterli değildir.",
  "16.03 ve 16.04 Açıklama Notları.")

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
  "Süt pastörizatörü",
  ["Süt sağma makinesi",
   "Sütü homojen hale getirmeye mahsus makine",
   "Motorla döndürülen tereyağı yayığı",
   "Sert peynir imalinde kullanılan peynir presi"],
  "84.34 Açıklama Notu süt sağma makinelerini, sütü homojenleştiren makineleri, yayıkları ve peynir preslerini bu pozisyonda sayar. "
  "Aynı not, sütün işlenmesine mahsus olup esas itibarıyla ısı değişikliği gerektiren pastörizatör, sterilizatör gibi cihazları 84.19’a "
  "gönderir. Fasıl 84 Not 2 de 84.01–84.24’teki bir tanıma uyan makinelerin 84.25–84.80 grubunda sınıflandırılmamasını öngörür.",
  "Fasıl 84 Not 2; 84.34 Açıklama Notu.")

# 27
q(42, ES, "A",
  "Fasıl 42 Not 2’ye göre; deriden yapılmış bilezik ……… pozisyonunda, deriyle kaplanmış düğme ……… pozisyonunda, deriden yapılmış "
  "oyuncak bebek ise ……… faslında sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
  "71.17 – 96.06 – 95",
  ["42.03 – 96.06 – 42", "71.13 – 42.05 – 95", "42.03 – 42.05 – 95", "71.17 – 42.05 – 42"],
  "Fasıl 42 Not 2; kol düğmelerini, bilezikleri ve diğer taklit mücevherleri (71.17), 96.06 pozisyonundaki düğmeleri, çıtçıtları ve "
  "düğme taslaklarını, oyuncaklar ile oyun ve spor levazımatı gibi 95. Fasıl eşyasını deriden yapılmış olsalar dahi bu fasıl dışında "
  "bırakır. Deri eşya için akla gelen 42.03 (giyim eşyası ve aksesuarları) ve 42.05 (deriden diğer eşya) bu nedenle uygulanmaz.",
  "Fasıl 42 Not 2.")

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
  "Kurutulmuş ve kabuğu çıkarılmış halde sunulan aşağıdaki baklagil tohumlarından hangisi Tarife Cetvelinde diğerlerinden "
  "<b>farklı</b> bir fasılda sınıflandırılır?",
  "Acı bakla tohumu",
  ["Guar tohumu", "At baklası", "Adzuki fasulyesi", "Nohut"],
  "07.13 Açıklama Notu, insan gıdası veya hayvan yemi olarak kullanılan cinsten kurutulmuş ve kabukları çıkarılmış baklagilleri sayar "
  "ve bezelye, nohut, Adzuki ve diğer fasulyeler, mercimek, bakla, at baklası ile guar tohumunu örnek verir. Aynı not, bakla ve at "
  "baklası dışındaki fiğ tohumlarını, burçağı ve acı bakla tohumlarını 12.09’a, soya fasulyesini 12.01’e gönderir. Guar tohumunun "
  "07.13’te açıkça sayılması tuzaktır.",
  "07.13 Açıklama Notu.")

# 32
q(33, E4, "D",
  "Tarife Cetveline göre, diş hekimlerince kullanılan, aşındırıcı madde içeren ve dişlerin yüzeyini temizleyip parlatmaya mahsus "
  "diş macunu hangi pozisyonda sınıflandırılır?",
  "33.06", ["30.06", "34.05", "34.07", "33.07"],
  "33.06 Açıklama Notu, aşındırıcı özellikteki maddeleri içersin içermesin ve diş hekimleri tarafından kullanılsın kullanılmasın bütün "
  "diş macunlarını ve dişleri temizleme veya parlatmaya mahsus müstahzarları bu pozisyonda sayar. Kullanıcının diş hekimi olması ürünü "
  "30.06’daki diş dolgu maddelerine veya 34.07’deki dişçilik müstahzarlarına dönüştürmez. Aşındırıcı içermesi de onu 34.05’teki "
  "temizleme patlarına götürmez.",
  "33.06 Açıklama Notu.")

# 33
q(39, CC, "C",
  "Fasıl 39 Not 11’e göre aşağıdakilerden hangileri 39.25 pozisyonunda sınıflandırılır?"
  "<br/>I. Kapasitesi 250 litre olan plastik su deposu"
  "<br/>II. Plastikten pencere panjuru"
  "<br/>III. Duvara tespit edilmek üzere hazırlanmış plastik havlu rayı"
  "<br/>IV. Atölyelerde montaj ve tesisat işleri için kullanılan plastikten büyük raflar",
  "II, III ve IV",
  ["I ve II", "II ve III", "I, III ve IV", "Yalnız IV"],
  "Fasıl 39 Not 11, 39.25 pozisyonunu sınırlı bir listeyle tanımlar: kapasitesi 300 litreden fazla sarnıç, tank ve depolar; kepenk, "
  "panjur ve benzerleri; montaj ve tesisat işleri için büyük raflar; kapı, pencere, merdiven, duvar vb. yerlere tespit edilmek üzere "
  "hazırlanmış havlu rayı, tutaç, kanca gibi bağlantı ve montaj parçaları bu listededir. 250 litrelik depo 300 litre eşiğini aşmadığından "
  "39.25’e giremez. Eşik değerin gözden kaçırılması tuzaktır.",
  "Fasıl 39 Not 11.")

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
  "GYK 6 açıklama notunda, alt pozisyonların yorumunda ilgili bölüm veya fasıl notunun uygulanmadığı “aksine bir hüküm” durumuna "
  "örnek olarak aşağıdakilerden hangisi gösterilmiştir?",
  "Fasıl 71 Not 4(b)’deki “platin” teriminin, ilgili alt pozisyon notundaki “platin” teriminden farklı olması",
  ["Hem 97.06’ya hem 97.01–97.05’e girebilen eşyanın Fasıl 97 Not 5(b) uyarınca 97.01–97.05’te sınıflandırılması",
   "Fasıl 31 notlarının, GYK 2(b) yoluyla bazı pozisyonlara girebilecek eşyayı bu pozisyonların dışında tutması",
   "Fasıl 30 Not 4 uyarınca bazı eczacılık eşyasının 30.06’da sınıflandırılması",
   "Hem 25.17’ye hem Fasıl 25’in başka bir pozisyonuna girebilen ürünün 25.17’de sınıflandırılması"],
  "GYK 6, alt pozisyon sınıflandırmasında metinde aksi belirtilmedikçe bölüm ve fasıl notlarının da uygulanacağını söyler. Açıklama notu "
  "“aksine bir hüküm” halini, bölüm veya fasıl notlarının alt pozisyon metinleri ya da alt pozisyon notlarıyla çeliştiği durum olarak "
  "açıklar ve Fasıl 71 Not 4(b)’deki “platin” ile alt pozisyon notundaki “platin” teriminin farklılığını örnek verir; bu durumda alt "
  "pozisyon notu uygulanır. Fasıl 97 Not 5(b) örneği GYK 3’ün, Fasıl 31 ve Fasıl 30 örnekleri GYK 1’in açıklama notlarında yer alır.",
  "GYK 6 Açıklama Notu (II).")

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
  "Aşağıdakilerden hangisi 34.07 pozisyonunda <b>sınıflandırılmaz</b>?",
  "Diş doldurmaya mahsus dişçi çimentosu",
  ["At nalı şeklinde dişçi mumu",
   "Perakende satılacak şekilde takım halinde ambalajlanmış dişçi mumu",
   "Kalsine edilmiş alçı esaslı dişçilik müstahzarı",
   "Heykel modellerinin yapımında kullanılan model patı"],
  "34.07 pozisyon metni model patlarını; takım halinde, perakende ambalajlı veya plaka, at nalı, çubuk gibi şekillerdeki “dişçi mumu” "
  "denilen müstahzarları ve kalsine edilmiş alçı ya da kalsiyum sülfat esaslı diğer dişçilik müstahzarlarını kapsar. Dişçi çimentoları "
  "ve diş doldurmaya mahsus diğer maddeler ise Fasıl 30 Not 4 uyarınca 30.06’da sınıflandırılır. Her ikisinin de dişçilikte kullanılması tuzaktır.",
  "34.07 pozisyon metni; Fasıl 30 Not 4.")

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
  "Fasıl 40 Not 6’ya göre, 40.04 pozisyonu anlamında “döküntü, kırpıntı ve artıklar” tabirinden ne anlaşılır?",
  "Kesilme, eskime veya diğer sebeplerle kesinlikle kullanıma elverişli olmayan kauçuk eşya ile kauçuğun işlenmesinden veya eşyanın "
  "imalatından arta kalan döküntü, kırpıntı ve artıklar",
  ["Yalnız kauçuk eşyanın imalatından arta kalan kırpıntılar; kullanılmış kauçuk eşya bu tabire girmez",
   "Kullanıma elverişli olup olmadığına bakılmaksızın her türlü kullanılmış kauçuk eşya",
   "Yeniden sırt geçirilmeye elverişli olanlar dahil bütün kullanılmış dış lastikler",
   "Sertleştirilmiş kauçuk döküntüleri dahil, her şekildeki kauçuk artıkları"],
  "Fasıl 40 Not 6, “döküntü, kırpıntı ve artıklar” tabirini, kesilme, eskime veya diğer sebeplerle kesinlikle kullanıma elverişli "
  "olmayan kauçuk eşya ile kauçuğun işlenmesinden veya eşyanın imalatından arta kalan döküntü, kırpıntı ve artıklar olarak tanımlar. "
  "Kullanılmış dış lastikler 40.12 pozisyon metninde ayrıca sayılır; sertleştirilmiş kauçuğun döküntü ve artıkları ise 40.17 pozisyon "
  "metni gereği 40.17’de yer alır.",
  "Fasıl 40 Not 6; 40.12 ve 40.17 pozisyon metinleri.")

# 47
q("GYK", GY, "C",
  "Bir çelik raf sisteminin bütün parçaları aynı sevkiyatta birlikte gümrüğe sunulmuştur. Ancak parçaların birleştirilebilmesi için önce "
  "ölçüsüne göre kesilmeleri ve bağlantı deliklerinin açılması gerekmektedir; montaj daha sonra cıvata ve kaynakla yapılacaktır. GYK 2(a) "
  "açıklama notuna göre aşağıdakilerden hangisi doğrudur?",
  "Parçalar nihai şekli için daha ileri işçilik gerektirdiğinden eşya, bu kural anlamında birleştirilmemiş (demonte) eşya sayılmaz.",
  ["Montajda kaynak kullanılacağından eşya, bu kural anlamında demonte eşya sayılmaz.",
   "Montaj yönteminin karmaşıklığı nedeniyle eşya, bu kural anlamında demonte eşya sayılmaz.",
   "Bütün parçalar birlikte sunulduğundan eşya, monte edilmiş raf gibi sınıflandırılır.",
   "Montajdan arta kalan parça bulunmadığından eşya, monte edilmiş raf gibi sınıflandırılır."],
  "GYK 2(a) açıklama notu (VII), “birleştirilmemiş veya demonte eşya” tabirini parçaları yalnızca bağlantı elemanlarıyla ya da perçin "
  "veya kaynakla birleştirme işlemini gerektiren eşya olarak tanımlar ve montaj yönteminin karmaşıklığının dikkate alınmayacağını "
  "belirtir. Bununla birlikte, nihai şeklin verilmesi için parçaların daha ileri bir işçilik görmemesi gerekir. Kesme ve delme işlemi "
  "gereken parçalar bu şartı karşılamaz; kaynak kullanılması veya montajın karmaşıklığı ise tek başına engel değildir.",
  "GYK 2(a) Açıklama Notu (VII).")

# 48
q(84, CC, "A",
  "Fasıl 84 Not 1’e göre aşağıdakilerden hangileri, makine veya cihaz niteliğinde olsalar bile Fasıl 84 <b>dışında</b> sınıflandırılır?"
  "<br/>I. Seramikten yapılmış pompa"
  "<br/>II. Kara taşıtlarına mahsus motor soğutma radyatörü"
  "<br/>III. Ev tipi bulaşık yıkama makinesi"
  "<br/>IV. Vakumlu elektrik süpürgesi",
  "I, II ve IV",
  ["I ve II", "II ve III", "III ve IV", "I, III ve IV"],
  "Fasıl 84 Not 1; seramikten mamul makine, cihaz ve aletleri (pompalar gibi) Fasıl 69’a, XVII. Bölümde yer alan araçlar için "
  "radyatörleri Bölüm XVII’ye, 85.08 pozisyonundaki vakumlu elektrik süpürgelerini ise Fasıl 85’e bırakarak fasıl dışında tutar. "
  "Bulaşık yıkama makineleri ise ev tipi olsalar dahi 84.22’de kalır; Fasıl 85 Not 4 de bunları 85.09 kapsamı dışında bırakır.",
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
  "Bir firma; araçların ön camına takılan, uydulardan aldığı küresel konum belirleme sistemi (GPS) sinyalleriyle aracın konumunu "
  "belirleyip sürücüye güzergâh gösteren, telefon veya yayın alma işlevi bulunmayan ekranlı navigasyon cihazları ithal etmektedir. "
  "Tarife Cetveline göre bu eşya hangi pozisyonda sınıflandırılır?",
  "85.26", ["85.17", "85.28", "84.71", "85.27"],
  "85.26 Açıklama Notu, telsiz seyrüsefer yardımcı cihazları arasında küresel konum belirleme sistemlerinin (GPS) alıcılarını açıkça "
  "sayar. Cihazın telefon işlevi bulunmadığından 85.17, televizyon yayını alıcısı olmadığından 85.28, radyo yayını alıcısı olmadığından "
  "85.27 uygun değildir. Fasıl 84 Not 6(E) uyarınca bilgi işleme dışında kendine has bir fonksiyonu olan makineler fonksiyonlarına uyan "
  "pozisyonda sınıflandırıldığından ekran ve hesaplama yeteneği ürünü 84.71’e götürmez.",
  "85.26 Açıklama Notu; Fasıl 84 Not 6(E).")


assert len(Q) == 50, len(Q)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"tur": "deneme", "no": 8, "sorular": Q}, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT)
