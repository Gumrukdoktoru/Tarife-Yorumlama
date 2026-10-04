#!/usr/bin/env python3
"""Deneme sınavı 9 üreticisi → data/deneme_09.json"""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "deneme_09.json")

ESYA = "Eşya → 4’lü pozisyon"
OLUM = "Olumsuz teşhis"
FARK = "Farklı/aynı pozisyon veya fasıl"
NOT = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
ESL = "Eşleştirme / Boşluk doldurma"
COK = "Çoktan-çoğa (I–IV)"
SEN = "Senaryo"

S = []


def q(fasil, tip, soru, secenekler, cevap, gerekce, dayanak):
    S.append({"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
              "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil})


# 1
q(11, ESYA,
  "Tarife Cetveline göre, kurutulmuş kestanelerin öğütülmesiyle elde edilen, başka hiçbir madde katılmamış kestane "
  "unu hangi pozisyonda sınıflandırılır?",
  ["08.02", "11.02", "11.06", "11.05", "19.01"], "C",
  "11.06 pozisyonu, 07.13’teki kuru baklagillerin ve 07.14’teki sagu, kök ve yumruların unlarının yanında 8. Fasıla "
  "giren ürünlerin un, kaba un ve tozlarını da kapsar; açıklama notu bu ürünler arasında kestane, badem, hurma ve muzu "
  "sayar. 11.02 hububat unları, 11.05 ise patates unu içindir. Tuzak, kestanenin kendisi 08.02’de yer aldığı için "
  "ununu da Fasıl 8’de sanmaktır.",
  "11.06 pozisyon metni ve Açıklama Notu.")

# 2
q("GYK", GYK,
  "Bölüm XV’in başlığı “Adi metaller ve adi metallerden eşya” olduğu halde, tamamen çelikten yapılmış şemsiye "
  "iskeletlerinin bu bölümde değil 66.03 pozisyonunda sınıflandırılması Genel Yorum Kurallarına göre nasıl açıklanır?",
  ["GYK 3(a) uyarınca 66.03, eşyayı demir veya çelikten eşya pozisyonlarına göre daha özel şekilde tanımlar.",
   "GYK 1 uyarınca başlıklar yalnızca gösterici olup sınıflandırma pozisyon metinleri ve Bölüm XV Not 1’e göre yapılır.",
   "GYK 3(b) uyarınca iskelete esas niteliğini veren unsur, maddesi değil şemsiye olarak kullanılma işlevidir.",
   "GYK 3(c) uyarınca 66.03, geçerli olabilecek pozisyonlar arasında numara sırasına göre sonuncusudur.",
   "GYK 2(a) uyarınca iskelet, tamamlanmamış şemsiye sayılarak bitmiş şemsiyenin pozisyonunda sınıflandırılır."],
  "B",
  "GYK 1, bölüm, fasıl ve tali fasıl başlıklarının yalnızca gösterici nitelikte olduğunu ve sınıflandırmanın pozisyon "
  "metinlerine ve bölüm veya fasıl notlarına göre yapılacağını belirtir. Bölüm XV Not 1, 66.03 pozisyonundaki şemsiye "
  "iskeletlerini bu bölüm dışında bıraktığından eşya, maddesi çelik olsa da 66.03’te yer alır; not hükmü bulunduğundan "
  "GYK 3’e başvurulmaz. 3(c) uygulansaydı numara sırasında sonra gelen bir Fasıl 73 pozisyonu seçilirdi; iskelet ise "
  "66.03 metnindeki aksam olarak bitmiş şemsiyenin pozisyonuna gitmez.",
  "GYK 1 ve Açıklama Notu (II), (III); Bölüm XV Not 1(d).")

# 3
q(86, ESYA,
  "Tarife Cetveline göre, kendinden hareketli olmayan, röntgenle tedavi cihazları ile donatılmış ve yolcu trenlerine "
  "eklenerek kullanılan demiryolu hastane vagonu hangi pozisyonda sınıflandırılır?",
  ["86.05", "86.04", "86.06", "86.03", "86.09"], "A",
  "86.05 pozisyonu kendinden hareketli olmayan yolcu vagonlarının yanında bagaj furgonlarını, posta vagonlarını ve "
  "diğer özel amaçlı vagonları kapsar; açıklama notu ambulans, hastane ve röntgenle tedavi vagonlarını ismen sayar. "
  "86.04 yalnızca demiryolu veya tramvayların bakım ya da servisine ait taşıtlar (atölye vagonu, drezin vb.) içindir; "
  "86.06 yük taşımaya mahsus, 86.03 kendinden hareketli vagonları kapsar. Tuzak, özel donanımı nedeniyle 86.04’ü "
  "seçmektir.",
  "86.05 pozisyon metni ve Açıklama Notu (8).")

# 4
q(36, OLUM,
  "Aşağıdakilerden hangisi 36.05 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Sapı ağaçtan yapılmış, kutusundaki pürüzlü yüzeye sürtülerek yakılan kibrit",
   "Sapı mukavvadan yapılmış, katlanır kapaklı bir zarf içinde sunulan kibrit",
   "Sapı stearin emdirilmiş dokumaya elverişli maddeden yapılmış mum kibriti",
   "Sürtülerek ateş alan ve kibrit şeklinde olan, renkli alevle yanan Bengal kibriti",
   "Özel olarak hazırlanmış bir yüzeye sürtüldüğünde alev veren emniyet kibriti"],
  "D",
  "36.05 pozisyonu, pürüzlü bir yüzeye sürtüldüğünde alev veren ve sapı ağaç, mukavva ya da stearin veya parafin "
  "emdirilmiş dokumaya elverişli maddeden olan kibritleri kapsar. Bengal kibritleri ve benzeri bazı pirotekni ürünleri, "
  "sürtünmeyle ateş alıp kibrit şeklinde olsalar da pozisyon metnindeki istisna gereğince 36.04’te yer alır. Tuzak, "
  "şekil benzerliği nedeniyle Bengal kibritini de 36.05’te sanmaktır.",
  "36.05 pozisyon metni ve Açıklama Notu.")

# 5
q(2, ESYA,
  "Tarife Cetveline göre, avlanmış yaban domuzlarından elde edilen, insan tüketimine uygun, dondurulmuş but etleri "
  "hangi pozisyonda sınıflandırılır?",
  ["02.08", "02.10", "16.02", "02.05", "02.03"], "E",
  "02.03 açıklama notu, ister evcil ister yabani olsun domuzların (örneğin yabani erkek domuzların) taze, soğutulmuş "
  "veya dondurulmuş etlerini bu pozisyona dahil eder; canlı yaban domuzları da aynı şekilde 01.03’te yer alır. Av "
  "hayvanı olması eti “diğer etler” olarak 02.08’e götürmez; 02.10 ise tuzlanmış, salamura edilmiş, kurutulmuş veya "
  "tütsülenmiş etler içindir. Tuzak, “yabani/av eti” düşüncesiyle 02.08’i seçmektir.",
  "02.03 Açıklama Notu; 01.03 Açıklama Notu.")

# 6
q(85, FARK,
  "Ev işlerinde kullanılan aşağıdaki elektrikli cihazlardan hangisi Tarife Cetvelinde diğerlerinden farklı bir "
  "pozisyonda sınıflandırılır?",
  ["Kendinden elektrik motorlu kahve öğütücü",
   "Elektrikli su kaynatma kabı (kettle)",
   "Mutfak evyesine monte edilen, kendinden motorlu mutfak artığı öğütücü",
   "Elektrikli diş fırçası",
   "Kendinden elektrik motorlu meyve ve sebze presi"],
  "B",
  "85.09 açıklama notu; ev tipi gıda öğütücü ve karıştırıcıları (kahve öğütücüler dahil), meyve ve sebze preslerini, "
  "mutfak artıklarını öğüten cihazları ve elektrikli diş fırçalarını kendinden elektrik motorlu ev aletleri olarak "
  "sayar. Su kaynatma kapları (kettle) ise ısıtma işlevi gören ev tipi elektrotermik cihazlar olarak 85.16 "
  "açıklama notunda ismen yer alır. Tuzak, hepsinin mutfakta kullanılan elektrikli cihaz olmasından hareketle "
  "kettle’ı da 85.09’da sanmaktır.",
  "85.09 ve 85.16 pozisyon metinleri ve Açıklama Notları.")

# 7
q(19, ESYA,
  "Tarife Cetveline göre, un veya nişasta hamurundan yapılmış, ilaç doldurulup birbirine tutturularak kılıf "
  "oluşturacak şekilde çiftler halinde imal edilmiş, eczacılıkta kullanılan türden boş kapsüller hangi pozisyonda "
  "sınıflandırılır?",
  ["19.05", "96.02", "30.06", "35.03", "19.02"], "A",
  "19.05 açıklama notu; hosti, eczacılıkta kullanılan türden boş kapsüller, mühür güllacı ve pirinç kağıdı gibi un "
  "veya nişasta hamurundan pişirilerek yapılan ürünleri bu pozisyona dahil eder. 96.02’de sayılan eczacılık "
  "kapsülleri sertleştirilmemiş jelatinden yapılanlardır; 35.03 jelatinin kendisini kapsar. Tuzak, kullanım amacına "
  "bakarak eşyayı Fasıl 30’a yöneltmektir.",
  "19.05 Açıklama Notu; 96.02 Açıklama Notu.")

# 8
q(68, FARK,
  "Aşağıdaki lifli veya genleştirilmiş mineral ürünlerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda "
  "yer alır?",
  ["Granit veya bazaltın eritilip lif haline getirilmesiyle elde edilen kaya yünü",
   "Alümina ve silika karışımının eritilip üflenmesiyle elde edilen seramik lifler",
   "Isıl işlemle hacmi büyütülmüş (genleştirilmiş) perlit",
   "Eritilmiş cürufa az miktarda su katılarak elde edilen köpüklü cüruf",
   "Camın eritilip lif haline getirilmesiyle elde edilen cam yünü"],
  "E",
  "Kaya yünü, cüruf yünü ve “seramik lifler” olarak bilinen alümina-silikat lifleri ile genleştirilmiş perlit, "
  "vermikülit, kil ve köpüklü cüruf 68.06 pozisyonunda yer alır. Cam yünü ise görünüşü benzer olsa da açıklama notunda "
  "belirtildiği üzere 70.19 pozisyonunda (Fasıl 70) sınıflandırılır. Tuzak, “mineral yün” görünümünden hareketle cam "
  "yününü de 68.06’ya almaktır.",
  "68.06 Açıklama Notu; 70.19 pozisyon metni.")

# 9
q(27, OLUM,
  "Aşağıdakilerden hangisi 27.14 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Suyu ve gangı giderilerek toz haline getirilmiş tabii bitümen",
   "Bitümenli veya yağlı şist",
   "Ham petrolün işlenmesinden kalan petrol bitümeni",
   "Mineral yağ kaynağı olarak kullanılan katranlı kumlar",
   "Asfaltlı kireç taşı"],
  "C",
  "27.14 pozisyonu tabii bitümen ve tabii asfaltı, bitümenli veya yağlı şistleri, katranlı kumları, asfaltitleri ve "
  "asfaltlı kireç taşı gibi asfaltlı kayaları kapsar; bu maddeler su ve gangı giderilmiş veya toz haline getirilmiş "
  "olsalar da pozisyonda kalır. Petrolden elde edilen bitümen ise açıklama notunda bu pozisyon haricinde bırakılarak "
  "27.13’e yönlendirilmiştir. Tuzak, tabii ve petrol kökenli bitümeni aynı pozisyonda sanmaktır.",
  "27.14 Açıklama Notu; 27.13 pozisyon metni.")

# 10
q(12, SEN,
  "Bir firma; yalnızca kurutulmuş papatya (Matricaria chamomilla) çiçeklerinden oluşan, başka hiçbir bitki veya madde "
  "katılmamış, bitki çayı hazırlanmak üzere süzen poşetlere konulup karton kutularda perakende satışa sunulan bir ürün "
  "ithal etmektedir. Ürün, tedavi veya korunma amacıyla ölçülü dozlar halinde hazırlanmamıştır. Bu ürün hangi "
  "pozisyonda sınıflandırılır?",
  ["09.02", "21.06", "30.04", "12.11", "21.01"], "D",
  "12.11 açıklama notu, bu pozisyondaki bitki veya bitki parçalarının bitkisel “çay” yapımı için küçük paketlere "
  "konulabileceğini ve tek bir türden oluşan bu ürünlerin de pozisyonda kaldığını belirtir; papatya çiçekleri 12.11’in "
  "bitki listesinde yer alır. Değişik türlerin veya başka maddelerin karışımı olsaydı 21.06’ya, tedavi amacıyla ölçülü "
  "doz halinde perakende ambalajlansaydı 30.03 veya 30.04’e giderdi. Tuzak, ürünün “çay” diye anılmasından hareketle "
  "09.02’yi seçmektir.",
  "Fasıl 12 Not 4; 12.11 Açıklama Notu.")

# 11
q(81, ESYA,
  "Tarife Cetveline göre, titanyumun ağırlıkça üstün olduğu bir titanyum alaşımından yapılmış, genel kullanıma "
  "mahsus cıvata ve somunlar hangi pozisyonda sınıflandırılır?",
  ["81.08", "73.18", "83.08", "84.87", "81.13"], "A",
  "Bölüm XV Not 2(a)’ya göre 73.18 pozisyonundaki eşya ile diğer adi metallerden benzeri eşya “genel kullanıma mahsus "
  "aksam ve parça”dır; 73.18 yalnızca demir veya çelikten olanları kapsadığından titanyumdan cıvata ve somunlar "
  "titanyumdan eşya olarak 81.08’de yer alır. Bölüm XV Not 5 gereği alaşım, ağırlıkça üstün olan titanyumun alaşımı "
  "sayılır; 81.13 ise sermetler içindir. Tuzak, cıvatayı her durumda 73.18’de sanmaktır.",
  "Bölüm XV Not 2(a) ve Not 5; 81.08 pozisyon metni.")

# 12
q("GYK", GYK,
  "GYK 1 açıklama notunda, “pozisyon ve notlarda aksine bir hüküm bulunmadıkça” tabirine örnek olarak; notları, bazı "
  "pozisyonlarının yalnızca belirli eşyayı kapsadığını hükme bağlayarak 2(b) Kuralının uygulanmasıyla bu pozisyonlara "
  "girebilecek eşyanın kapsanmasını önleyen fasıl hangisidir?",
  ["Fasıl 30", "Fasıl 97", "Fasıl 31", "Fasıl 15", "Fasıl 9"], "C",
  "GYK 1 açıklama notunun (III)(b) bendi, 31. Fasılın notlarının bu fasıldaki bazı pozisyonların belli eşyayı "
  "kapsadığını hükme bağladığını ve böylece 2(b) Kuralının uygulanmasıyla bu pozisyonlara girebilecek eşyanın "
  "kapsanmasını önlediğini örnek verir. Fasıl 30 Not 4 ise (III)(a) bendinde kurallara gerek kalmadan yapılan "
  "sınıflandırma örneğidir; Fasıl 97 Not 5(b) GYK 3’ün, 15.03’teki “karıştırılmamış” ifadesi GYK 2(b)’nin açıklama "
  "notunda geçer.",
  "GYK 1 Açıklama Notu (III)(b).")

# 13
q(20, FARK,
  "Aşağıdaki sebze müstahzarlarından hangisi Tarife Cetvelinde diğerlerinden farklı bir pozisyonda sınıflandırılır?",
  ["Sirke ile hazırlanmış kültür mantarı",
   "Sirke ile hazırlanmış kapari",
   "Asetik asitli bir sıvı içinde hazırlanmış küçük soğanlar",
   "Sirke ile hazırlanmış kırmızı pancar dilimleri",
   "Tuzlu su içinde hava geçirmez kutularda sterilize edilmiş kültür mantarı"],
  "E",
  "Sirke veya asetik asitle hazırlanmış ya da konserve edilmiş sebzeler, mantarlar dahil, 20.01 pozisyonunda toplanır. "
  "Mantarlar ve domalan ise sirke veya asetik asitten başka usullerle (örneğin tuzlu suda sterilize edilerek) "
  "hazırlandığında 20.03 pozisyonunda yer alır. Tuzak, iki seçenekteki ürünün aynı mantar olmasından hareketle "
  "hazırlanma usulünü gözden kaçırmaktır.",
  "20.01 ve 20.03 pozisyon metinleri; 20.03 Açıklama Notu.")

# 14
q(90, OLUM,
  "Aşağıdakilerden hangisi 90.28 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Konutlarda kullanılan diyaframlı (kuru) doğal gaz sayacı",
   "Akaryakıt istasyonlarında kullanılan, ölçü tertibatlı akaryakıt dağıtım pompası",
   "Önceden para atılarak çalıştırılan elektrik sayacı",
   "Türbinli soğuk su sayacı",
   "Gaz sayaçlarının doğruluğunu kontrole mahsus ayar sayacı"],
  "B",
  "90.28 pozisyonu gaz, sıvı ve elektrik sayaçlarını, bunların kalibre (ayar) cihazları ve önceden para atılarak "
  "çalıştırılan sayaçlar gibi özel amaçlı sayaçlar dahil kapsar. Ölçü tertibatlı tevziat tulumbaları ise açıklama "
  "notunda bu pozisyon haricinde bırakılmış olup 84.13 pozisyon metnindeki “sıvılar için pompalar (ölçü tertibatı "
  "olsun olmasın)” kapsamında yer alır. Tuzak, pompanın verilen miktarı göstermesinden hareketle onu sayaç sanmaktır.",
  "90.28 Açıklama Notu; 84.13 pozisyon metni.")

# 15
q(48, NOT,
  "Fasıl 48 notları ve 48.16 Açıklama Notuna göre, karbon kağıdının 48.09 yerine 48.16 pozisyonunda "
  "sınıflandırılmasını belirleyen ölçüt aşağıdakilerden hangisidir?",
  ["Ebadı ne olursa olsun kutulara konularak perakende satılacak hale getirilmiş olması",
   "Metrekare ağırlığının 40 g’ı geçmemesi ve daktilo kopyalarında kullanılması",
   "Daktilo makinelerinde veya kalemle kopya çıkarmada kullanılmaya mahsus olması",
   "Genişliği 36 cm’yi geçmeyen rulo veya hiçbir kenarı 36 cm’yi geçmeyen tabaka halinde olması",
   "Katlanmamış halde bir kenarı 36 cm’yi, diğer kenarı 15 cm’yi geçen tabakalar halinde olması"],
  "D",
  "Fasıl 48 Not 8 uyarınca 48.03–48.09 pozisyonları yalnızca genişliği 36 cm’yi geçen rulolara veya katlanmamış halde "
  "bir kenarı 36 cm’yi, diğer kenarı 15 cm’yi geçen dikdörtgen tabakalara uygulanır. 48.16 açıklama notu da kopya "
  "kağıtlarının genişliği 36 cm’yi geçmeyen rulolar, hiçbir kenarı 36 cm’yi geçmeyen tabakalar veya dikdörtgenden "
  "başka şekilde kesilmiş halde bu pozisyona girdiğini belirtir. 48.16 metnindeki “kutulara konularak perakende "
  "satılacak hale getirilmiş olsun olmasın” ifadesi, perakende ambalajın belirleyici olmadığını gösterir.",
  "Fasıl 48 Not 8; 48.16 Açıklama Notu.")

# 16
q(5, ESL,
  "Tarife Cetveline göre; suni tohumlamada kullanılan sığır spermi ……, dişi hayvana nakledilmek üzere dondurulmuş "
  "hayvan embriyonu ……, kurutulmuş safra …… ve safra özü (hülasası) …… pozisyonunda sınıflandırılır. Boşluklara "
  "sırasıyla aşağıdakilerden hangisi gelmelidir?",
  ["05.11 – 05.11 – 05.10 – 30.01",
   "05.11 – 30.02 – 05.10 – 30.01",
   "05.10 – 05.11 – 05.10 – 05.10",
   "05.11 – 05.11 – 30.01 – 30.01",
   "30.02 – 05.11 – 05.11 – 30.01"],
  "A",
  "05.11 açıklama notu, hayvan spermlerini ve dişi hayvana transplante edilmek amacıyla dondurulmuş hayvan "
  "embriyonlarını bu pozisyona dahil eder. Safra, kurutulmuş olsun olmasın 05.10 pozisyon metninde ismen yer alır; "
  "safra özü ise 05.10 açıklama notunda bu pozisyon haricinde bırakılarak 30.01’e yönlendirilmiştir. Tuzak, sperm ve "
  "embriyonu biyolojik ürün sayıp 30.02’ye götürmek ya da safra ile özünü aynı pozisyonda sanmaktır.",
  "05.10 pozisyon metni ve Açıklama Notu; 05.11 Açıklama Notu.")

# 17
q(87, ESYA,
  "Tarife Cetveline göre, ayrı olarak sunulan; bir tarafında tekerleği, diğer tarafında motosiklet yanına takılmaya "
  "mahsus tertibatı bulunan ve yalnız başına kullanılmaya elverişli olmayan, yolcu taşımaya mahsus motosiklet yan "
  "sepeti hangi pozisyonda sınıflandırılır?",
  ["87.14", "87.16", "87.11", "87.12", "87.08"], "C",
  "87.11 pozisyon metni motosikletlerin yanında “sepetler”i de ismen sayar; açıklama notu motosiklet ve bisikletlere "
  "mahsus her türlü yan sepetin bu pozisyonda yer aldığını, 87.12 açıklama notu da ayrı gelen sepetlerin 87.11’e "
  "girdiğini belirtir. 87.16’daki römork tabiri yan sepetleri kapsamaz. Tuzak, ayrı sunulduğu için eşyayı aksam-parça "
  "sayıp 87.14’ü seçmektir.",
  "87.11 pozisyon metni ve Açıklama Notu; 87.16 Açıklama Notu.")

# 18
q(39, OLUM,
  "Aşağıdaki plastikten eşyadan hangisi Tarife Cetvelinin 39. Faslında <b>sınıflandırılmaz</b>?",
  ["Plastik tabakaların dikilmesiyle yapılmış yağmurluk",
   "Plastikten yapay tırnak",
   "Plastik levhaların yapıştırılmasıyla yapılmış kitap kılıfı",
   "Mobilya için plastikten bağlantı elemanı",
   "Plastikten kol saati zarfı"],
  "E",
  "Fasıl 39 Not 2, 91. Fasla giren eşyayı (saatler ve saat mahfazaları gibi) bu fasıl dışında bırakır; plastikten "
  "kol saati zarfları Fasıl 91’de yer alır. Plastik tabakaların dikilmesi veya yapıştırılmasıyla yapılan "
  "yağmurluk gibi giysiler, kitap kılıfları, mobilya bağlantı elemanları ve yapay tırnaklar ise 39.26 açıklama notunda "
  "ismen sayılır. Tuzak, giysinin Bölüm XI’e gideceğini düşünerek yağmurluğu fasıl dışı saymaktır.",
  "Fasıl 39 Not 2; 39.26 Açıklama Notu.")

# 19
q(13, FARK,
  "Haşhaş (Papaver somniferum) bitkisinden elde edilen aşağıdaki ürünlerden hangisi Tarife Cetvelinde diğerlerinden "
  "farklı bir fasılda sınıflandırılır?",
  ["Ekim amacı taşımayan, dökme halde haşhaş tohumu",
   "Kurutulmuş haşhaş kellesi (kapsülü)",
   "Yağı alınmamış haşhaş tohumu unu",
   "Olgunlaşmamış kapsüllerin kurutulmuş özsuyu olan afyon",
   "Ekilmek üzere ithal edilen haşhaş tohumu"],
  "D",
  "Haşhaş tohumu Fasıl 12 Not 1 gereği 12.07’de yer alır ve Not 3 uyarınca ekim amaçlı olsa bile 12.09’a girmez; "
  "yağı alınmamış tohum unu 12.08’de, haşhaş kellesi 12.11’de sınıflandırılır. Olgunlaşmamış haşhaş kapsüllerinin "
  "kurutulmuş özsuyu olan afyon ise bitkisel özsu ve hülasa olarak 13.02 pozisyonunda (Fasıl 13) yer alır. Tuzak, tüm "
  "ürünlerin aynı bitkiden gelmesi nedeniyle afyonu da Fasıl 12’de sanmaktır.",
  "Fasıl 12 Not 1 ve Not 3; 13.02 Açıklama Notu.")

# 20
q(57, SEN,
  "Bir firma; havlı yüzü tırtıl ipliklerinin atkı ipliği olarak kullanılmasıyla dokunmuş, kaba ve sert tabanlı, ağır "
  "ve dayanıklı yapısıyla açıkça yere serilmeye mahsus olduğu anlaşılan, tufte veya floke edilmemiş ve düğümlü olmayan "
  "halılar ithal etmektedir. Bu halılar hangi pozisyonda sınıflandırılır?",
  ["58.01", "57.02", "56.06", "57.03", "57.05"], "B",
  "57.02 açıklama notu, havlı yüzleri tırtıl ipliklerinin kullanılmasıyla meydana getirilen tırtıl halıları dokunmuş "
  "halılar arasında sayar. Bu halılar 58.01’deki tırtıl mensucata benzer tarzda imal edilse de dayanıklılıkları, "
  "malzemelerinin kabalığı ve taban dokumalarının sertliği ile yer kaplaması olarak ayırt edilir ve Fasıl 57 Not 1 "
  "kapsamında kalır. 56.06 tırtıl ipliğin kendisini, 57.03 yalnızca tufte edilmiş halıları kapsar; tuzak, “tırtıl” "
  "kelimesinden hareketle 58.01 veya 56.06’yı seçmektir.",
  "Fasıl 57 Not 1; 57.02 Açıklama Notu (3).")

# 21
q(38, ESYA,
  "Tarife Cetveline göre, antibiyotik üretiminde mikroorganizmaların beslenip üremesi için hazırlanmış; et hülasası, "
  "pepton, agar-agar ve glukozdan oluşan, sterilize edilerek kapalı cam şişelere konulmuş müstahzar hangi pozisyonda "
  "sınıflandırılır?",
  ["13.02", "35.04", "30.02", "38.22", "38.21"], "E",
  "38.21 pozisyonu, mikroorganizmaların (virüsler dahil) ve bitki, insan veya hayvan hücrelerinin geliştirilmesine "
  "veya idamesine mahsus müstahzar kültür ortamlarını kapsar; açıklama notuna göre bunlar çoğunlukla et hülasası, "
  "pepton, agar-agar ve jelatin gibi maddelerden hazırlanır. Kültür ortamı olarak hazırlanmamış agar-agar (13.02) ve "
  "peptonlar (35.04) kendi pozisyonlarında kalır; 30.02 mikroorganizma kültürlerinin kendisini, 38.22 ise laboratuvar "
  "ve teşhis reaktiflerini kapsar.",
  "38.21 pozisyon metni ve Açıklama Notu.")

# 22
q(69, NOT,
  "Fasıl 69 notları ve Genel Açıklamalarına göre “seramik mamulleri” ile ilgili aşağıdakilerden hangisi doğrudur?",
  ["Şekil verildikten sonra pişirilmiş steatit gibi kayalardan elde edilen mamuller de seramik mamulü sayılır.",
   "Reçinelerin kürlenmesi amacıyla 600 °C’ye kadar ısıtılan ürünler pişirilmiş seramik olarak değerlendirilir.",
   "Fasıl 69 yalnızca kil esaslı ham maddelerin pişirilmesiyle elde edilen mamulleri kapsar.",
   "Metalle sinterlenmiş metal karbürlerden oluşan sermetler Fasıl 69’da seramik mamulü olarak yer alır.",
   "Seramikten yapılmış ve Fasıl 82’ye giren bıçak gibi eşya 69.14 pozisyonunda sınıflandırılır."],
  "A",
  "Fasıl 69 Not 1 bu faslın yalnızca şekil verildikten sonra pişirilmiş seramik mamullerini kapsadığını belirtir; genel "
  "açıklamalar da şekil verildikten sonra pişirilmiş steatit gibi kayaları seramik mamulleri arasında sayar. Aynı not "
  "uyarınca 800 °C’den az sıcaklığa kadar ısıtılan ürünler pişirilmiş sayılmaz ve ham maddeler kil yanında oksitler, "
  "karbürler, nitrürler veya grafit gibi maddeler de olabilir; Not 2 ise 81.13’teki sermetleri ve Fasıl 82’deki eşyayı "
  "bu fasıl dışında bırakır.",
  "Fasıl 69 Not 1 ve Not 2(d), (e); Fasıl 69 Genel Açıklamalar.")

# 23
q(1, COK,
  "Aşağıdaki canlı hayvanlardan hangileri 01.06 pozisyonunda sınıflandırılır?<br/>I. Istakoz<br/>II. Tek hörgüçlü "
  "deve<br/>III. Kurbağa<br/>IV. Bıldırcın",
  ["I ve II", "II ve III", "II, III ve IV", "I, III ve IV", "I, II ve IV"], "C",
  "01.06 açıklama notu develeri (tek hörgüçlü develer dahil) memeliler arasında, bıldırcını 01.05’te ismen geçmeyen "
  "kuşlar arasında, kurbağaları ise “diğerleri” grubunda sayar. Istakoz gibi kabuklu hayvanlar Fasıl 1 notu gereği bu "
  "fasıl dışında kalıp 03.06’da yer alır. Tuzak, bıldırcını kümes hayvanı sayıp 01.05’e götürmektir; 01.05 evcil "
  "tavuk, ördek, kaz, hindi ve beç tavuğu gibi türleri kapsar.",
  "Fasıl 1 Notu; 01.06 Açıklama Notu.")

# 24
q("GYK", GYK,
  "Başka hiçbir madde katılmamış, tarçın (09.06) ile karanfilin (09.07) karışımından oluşan bir baharat karışımı "
  "09.10 pozisyonunda sınıflandırılmaktadır. Genel Yorum Kurallarının açıklama notlarına göre bu "
  "sınıflandırma hangi kurala dayanır?",
  ["GYK 3(c) – 09.10, baharat pozisyonları arasında numara sırasına göre sonuncu olduğu için",
   "GYK 2(b) – bir maddeye yapılan atıf, o maddenin başka maddelerle karışımlarını da kapsadığı için",
   "GYK 3(b) – karışıma esas niteliğini veren baharat, ağırlık ve kıymet bakımından belirlendiği için",
   "GYK 1 – fasıl notunda belirtilen hazır karışımlar 1 numaralı kurala göre sınıflandırıldığı için",
   "GYK 4 – karışım, kendisine en çok benzeyen eşyanın bulunduğu pozisyonda yer aldığı için"],
  "D",
  "GYK 2(b) açıklama notu, bir Bölüm veya Fasıl Notunda ya da pozisyon metninde belirtilen hazır karışımların 1 "
  "numaralı Kuraldaki esaslara göre sınıflandırılacağını belirtir. Fasıl 9 Not 1(b), 09.04 ila 09.10 pozisyonlarından "
  "farklı pozisyonlara giren ürünlerin karışımlarını doğrudan 09.10’a verdiğinden sonuç GYK 1 ile bulunur. GYK 3(c) "
  "uygulansaydı yalnızca karışımın girebileceği pozisyonlar (09.06 ve 09.07) arasında seçim yapılır ve sonuç 09.07 "
  "olurdu; bu kural ancak 3(a) ve 3(b) yetersiz kaldığında uygulanır.",
  "GYK 1; GYK 2(b) Açıklama Notu (X); Fasıl 9 Not 1(b).")

# 25
q(83, FARK,
  "Adi metalden yapılmış aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir pozisyonda "
  "sınıflandırılır?",
  ["Ayakkabı bağcık delikleri için bağ deliği kapsülleri (kuşgözü)",
   "Valiz ve bavullar için tutma sapı",
   "Giyim eşyası için kopça",
   "Giysilerin süslenmesinde kullanılan, kesilmiş ince pullar",
   "Boru şeklinde perçin"],
  "B",
  "83.08 pozisyonu giyim eşyası, ayakkabı ve seyahat eşyası gibi eşya için adi metalden kancaları, tokaları, "
  "kopçaları ve bağ deliği kapsüllerini, boru şeklinde veya yarık saplı perçinleri ve boncuklar ile kesilmiş ince "
  "pulları kapsar. Valiz, sandık ve bavullar için saplar ve köşe koruyucuları gibi donanım ise 83.02 pozisyon metninde "
  "“bavul, sandık, mahfaza ve benzeri eşya için donanım” olarak yer alır. Tuzak, seyahat eşyasına takıldığı için sapı "
  "da 83.08’de sanmaktır.",
  "83.02 ve 83.08 pozisyon metinleri; 83.02 Açıklama Notu.")

# 26
q(80, OLUM,
  "Aşağıdakilerden hangisi 80.07 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Kalaydan sofra tabağı",
   "Kalaydan hacim ölçekleri",
   "Kalaydan boru bağlantı parçaları (rakor, dirsek)",
   "Kalay pulları",
   "Kangal halinde sunulan kalay tel"],
  "E",
  "80.03 pozisyonu kalaydan çubukları, profilleri ve telleri kapsadığından kalay tel 80.07’de değil 80.03’te yer alır. "
  "80.07 “kalaydan diğer eşya” olup açıklama notunda ev ve sofra eşyası, hacim ölçekleri, kalay tozları ve pulları ile "
  "kalaydan borular ve boru bağlantı parçaları ismen sayılır. Tuzak, 80.07’nin kalay levha ve boruları da kapsayan "
  "geniş bir pozisyon olmasından hareketle teli de buraya koymaktır.",
  "80.03 pozisyon metni; 80.07 Açıklama Notu.")

# 27
q(47, ESYA,
  "Tarife Cetveline göre, pamuk linterlerinin işlenmesiyle elde edilen ve suni lif imalatında selüloz kaynağı olarak "
  "kullanılan, balyalanmış tabakalar halindeki linter pamuğu hamuru hangi pozisyonda sınıflandırılır?",
  ["47.06", "14.04", "47.02", "47.03", "52.01"], "A",
  "47.06 pozisyonu, kağıt veya kartondan geri kazanılmış liflerin hamurlarının yanında odun dışındaki diğer lifli "
  "selülozik maddelerden elde edilen hamurları da kapsar ve linter pamuğu hamuru bu pozisyonda ayrıca belirtilmiştir. "
  "Pamuk linterlerinin kendisi ise Fasıl 47 genel açıklamaları gereği bu fasıl dışında kalarak 14.04’te yer alır. "
  "47.02 ve 47.03 yalnızca odun hamurları içindir; tuzak, linter ile linterden elde edilen hamuru aynı yerde sanmaktır.",
  "47.06 pozisyon metni; Fasıl 47 Genel Açıklamalar.")

# 28
q(17, SEN,
  "Bir gıda firması; esası şeker olan, buna nispeten çok miktarda bitkisel yağ ile süt tozu ve öğütülmüş fındık "
  "katılmış, kakao içermeyen ve yapısı itibarıyla doğrudan şekerleme haline dönüştürülmeye uygun olmayan, kavanozlarda "
  "sunulan bir ezme ithal etmektedir. Bu ürün hangi pozisyonda sınıflandırılır?",
  ["17.04", "18.06", "21.06", "20.08", "19.01"], "C",
  "17.04 açıklama notu, esası şeker olup çok az yağ içeren ve doğrudan şekerlemeye dönüştürülmeye elverişli fondan, "
  "nugat ve badem ezmelerini bu pozisyona alırken; nispeten çok miktarda yağ katılmış, bazen süt veya fındık içeren ve "
  "doğrudan şeker mamulüne dönüştürülmeye uygun olmayan esası şeker olan ezmeleri pozisyon haricinde bırakarak 21.06’ya "
  "yönlendirir. Ürün kakao içermediğinden 18.06 da söz konusu değildir. Tuzak, esasının şeker olmasından hareketle "
  "17.04’ü seçmektir.",
  "17.04 Açıklama Notu.")

# 29
q(39, NOT,
  "Fasıl 39 Not 2’ye göre, motor yağlarının akışkanlığını düzenlemek amacıyla hazırlanmış, esası 39. Fasıldaki "
  "polimerler olan müstahzar katkılar hangi pozisyonda sınıflandırılır?",
  ["39.01", "38.11", "27.10", "34.03", "38.24"], "B",
  "Fasıl 39 Not 2, mineral yağlar (benzin dahil) veya bunlarla aynı amaçla kullanılan diğer sıvılar için müstahzar "
  "katkıları bu fasıl dışında bırakarak 38.11’e yönlendirir; 38.11 pozisyon metni vuruntuyu önleyici, oksidasyonu "
  "durdurucu, akışkanlığı düzenleyici ve aşınmayı önleyici katkıları ismen sayar. Esası bir polimer olsa da katkı "
  "müstahzarı ilk şekillerdeki polimer olarak Fasıl 39’da kalmaz; yağlama müstahzarları ise 27.10 veya 34.03’te yer "
  "alır.",
  "Fasıl 39 Not 2(h); 38.11 pozisyon metni.")

# 30
q(14, ESL,
  "Tarife Cetveline göre; boyacılıkta kullanılan kına fidanı yaprakları ……, mazı yumrularından su ile çıkarılan tanen "
  "……, çiğnenerek tüketilen taze tanbul (betel) yaprakları …… ve uzunlamasına yarılmış hint kamışları …… "
  "pozisyonunda sınıflandırılır. Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
  ["14.04 – 14.04 – 12.11 – 14.01",
   "12.11 – 32.01 – 14.04 – 46.01",
   "14.04 – 32.03 – 12.11 – 14.01",
   "14.04 – 32.01 – 14.04 – 14.01",
   "13.02 – 32.01 – 14.04 – 14.01"],
  "D",
  "14.04 açıklama notu, esas olarak boyacılıkta kullanılan bitkisel ham maddeler arasında kına fidanını, “diğer "
  "bitkisel ürünler” arasında ise taze tanbul yapraklarını ismen sayar. Su ile çıkarılmış mazı yumrusu taneni dahil "
  "bitkisel tanenler aynı notta bu pozisyon haricinde bırakılarak 32.01’e yönlendirilmiştir. Hint kamışları, "
  "uzunlamasına yarılmış olsalar da örgü maddesi olarak 14.01’de kalır; henüz birleştirilip örgü haline getirilmediklerinden 46.01’e girmez. Tuzak, mazı "
  "yumrusunun kendisinin 14.04’te olmasından hareketle tanenini de orada sanmaktır.",
  "14.01 ve 14.04 Açıklama Notları.")

# 31
q(49, FARK,
  "Aşağıdaki baskılı aktarma (transfer) ürünlerinden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda "
  "sınıflandırılır?",
  ["Litografya işlerinde kullanılan türden transfer kağıtları",
   "Seramik eşyanın süslenmesinde kullanılan, cam haline gelen terkiplerle basılı çıkartmalar",
   "Çocukların eğlenmesine mahsus olarak üretilen çıkartmalar",
   "Sıcak ütü baskısıyla mensucat yüzeyine aktarılan nakış ve işleme çıkartmaları",
   "Nakil vasıtalarına marka vurmak amacıyla kullanılan çıkartmalar"],
  "A",
  "49.08 pozisyonu her nevi çıkartmayı kapsar; açıklama notu cam haline gelen terkiplerle basılı çıkartmaları, "
  "çocukların eğlenmesine mahsus çıkartmaları, sıcak ütüyle mensucata aktarılan nakış çıkartmalarını ve taşıtlara "
  "marka vurmada kullanılan çıkartmaları bu pozisyonda sayar. Buna karşılık litografya işlerinde kullanılan türden "
  "transfer kağıtları, aynı açıklama notuna göre duruma göre 48.09 veya 48.16 pozisyonlarında (Fasıl 48) yer alır. "
  "Tuzak, “aktarma” işlevi ortak olduğu için bunları da çıkartma saymaktır.",
  "49.08 Açıklama Notu.")

# 32
q(26, OLUM,
  "Aşağıdaki ürünlerden hangisi metal cevherleri, cüruf ve küllerin yer aldığı 26. Fasıl kapsamı <b>dışında "
  "kalır</b>?",
  ["Titan oksidinden oluşan rutil cevheri",
   "Demir ve manganez tungstatı olan volframit",
   "Antimon sülfürden oluşan stibnit (antimonit)",
   "Demir veya çeliğin imalinden elde edilen granüle cüruf (cüruf kumu)",
   "Kalsine edilmiş tabii magnezyum karbonat (manyezit)"],
  "E",
  "Fasıl 26 Not 1, tabii magnezyum karbonatı (manyezit), kalsine edilmiş olsun olmasın bu fasıl dışında bırakarak "
  "25.19’a yönlendirir; genel açıklamalar da magnezyum elde edilmesinde kullanılan manyezit ve dolomit gibi mineralleri "
  "26.01–26.17 dışında sayar. Rutil 26.14, volframit 26.11 ve stibnit 26.17 pozisyonlarında metal cevheri olarak; "
  "granüle cüruf ise 26.18’de yer alır. Tuzak, magnezyum kaynağı olmasından hareketle manyeziti metal cevheri "
  "sanmaktır.",
  "Fasıl 26 Not 1(b); Fasıl 26 Genel Açıklamalar.")

# 33
q(85, ESYA,
  "Tarife Cetveline göre, telekomünikasyonda kullanılan ve her biri ayrı ayrı kaplanmış (kılıflanmış) optik liflerden "
  "oluşan fiber optik kablo hangi pozisyonda sınıflandırılır?",
  ["90.01", "85.44", "85.36", "85.17", "70.19"], "B",
  "85.44 pozisyon metni, tek tek kaplanmış liflerden oluşan fiber optik kabloları (bağlantı parçaları veya elektrik "
  "iletkenleri ile teçhiz edilmiş olsun olmasın) ismen kapsar. 90.01 ise optik lifleri, optik lif demetlerini ve "
  "lifleri ayrı ayrı kılıflanmamış, bir veya daha fazla demeti kapsayan tek bir kılıftan oluşan optik lif kablolarını "
  "içine alır. 85.36 optik lif konnektörleri içindir; tuzak, “optik” kelimesinden hareketle 90.01’i seçmektir.",
  "85.44 ve 90.01 pozisyon metinleri; 90.01 Açıklama Notu.")

# 34
q(28, GYK,
  "Diş hekimliğinde dolgu yapımında kullanılmak üzere, kullanım öncesinde birbiriyle karıştırılması tasarlanmış bir "
  "toz ve bir sıvıdan oluşan, nispi miktarları itibarıyla birbirini tamamlayan ve tek bir ambalajda birlikte sunulan "
  "takımın sınıflandırılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
  ["GYK 3(b) uyarınca, ağırlık ve hacim bakımından takıma esas niteliğini veren toz bileşenin pozisyonunda "
   "sınıflandırılır.",
   "Bileşenler ayrı ayrı kendi pozisyonlarında sınıflandırılır; Bölüm VI Not 3 yalnızca perakende satışa "
   "hazırlanmış takımlara uygulanır.",
   "Bölüm VI Not 3 ve GYK 1 uyarınca, karıştırılınca elde edilecek ürüne uygun olan 30.06 pozisyonunda "
   "sınıflandırılır.",
   "GYK 3(c) uyarınca, bileşenlerin girebileceği pozisyonlardan numara sırasına göre sonuncusunda bir bütün olarak "
   "sınıflandırılır.",
   "GYK 5(b) uyarınca, ortak ambalajı ile birlikte sıvı bileşenin girdiği pozisyonda bir bütün olarak "
   "sınıflandırılır."],
  "C",
  "Bölüm VI Not 3; tamamı veya bir kısmı bu bölümde yer alan ve VI. veya VII. Bölümdeki bir ürünü elde etmek için "
  "karıştırılması tasarlanan set halindeki eşyanın, birlikte kullanılmaya mahsus olduğu açıkça belli olma, birlikte "
  "sunulma ve birbirini tamamlama şartlarıyla bu ürüne uygun pozisyonda sınıflandırılacağını hükme bağlar; açıklama "
  "notu 30.06’daki dişçilikte kullanılan alçı ve dolguları örnek verir. Sınıflandırma not hükmüne, yani GYK 1’e "
  "dayanır. Bileşenler önceden karıştırılmadan birbirini izleyerek kullanılsaydı not uygulanmaz, perakende takımlarda "
  "genellikle GYK 3(b)’ye başvurulurdu.",
  "Bölüm VI Not 3 ve Genel Açıklamalar; GYK 1.")

# 35
q(54, NOT,
  "Sentetik filament iplikler ve bunlardan mensucatla ilgili olarak Bölüm XI notlarına göre aşağıdakilerden hangisi "
  "doğrudur?",
  ["“Emdirilmiş” tabiri, maddeye batırılarak işlem görmüş ürünleri kapsamaz.",
   "Dokumaya elverişli maddelerin kauçuk ipliklerle birleştirilmesiyle oluşan elastiki ürünler Fasıl 40’ta yer alır.",
   "Elastomerik iplik tanımı, gerildiğinde kopmayan tekstüre iplikleri de kapsar.",
   "Bu bölüm anlamında “poliamidler” tabirine aramidler de dahildir.",
   "Değişik pozisyonlardaki mensucattan giyim eşyası, perakende takım halindeyse her durumda GYK 3(b) ile tek "
   "pozisyonda sınıflandırılır."],
  "D",
  "Bölüm XI Not 12, bu bölüm anlamında “poliamidler” tabirine aramidlerin de dahil olduğunu belirtir; bu nedenle aramid "
  "filament iplikleri naylon ve diğer poliamidlerden iplikler gibi değerlendirilir. Not 11’e göre “emdirilmiş” tabiri "
  "“batırılmış”ı da kapsar; Not 10 kauçuk ipliklerle birleştirilmiş elastiki ürünleri bu bölümde tutar; Not 13 "
  "tekstüre iplikleri elastomerik iplik tanımı dışında bırakır; Not 14 ise değişik pozisyonlardaki mensucattan giyim "
  "eşyasının perakende takım halinde olsa bile kendi pozisyonlarında sınıflandırılacağını hükme bağlar.",
  "Bölüm XI Not 10, 11, 12, 13 ve 14.")

# 36
q(67, FARK,
  "Kuş tüylerinden yapılmış aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda "
  "sınıflandırılır?",
  ["Tamamen kuş tüylerinden yapılmış kadın şapkası",
   "Şapkalarda kullanılmak üzere kuş tüylerinden yapılmış süs",
   "Ağartılmış ve boyanmış tüylü kuş derisi",
   "Bir mensucat mesnet üzerine yapıştırıcıyla tespit edilmiş kalem tüyler",
   "Salkım şeklinde bir araya getirilmiş fantazi süs tüyleri"],
  "A",
  "Hazırlanmış tüylü kuş derileri, salkım veya demet halinde birleştirilmiş tüyler, mesnet üzerine tespit edilmiş "
  "tüyler ile şapka ve giysiler için tüy süsleri 67.01 açıklama notunda bu pozisyonun eşyası olarak sayılır. Kuş "
  "tüylerinden mamul başlıklar ise Fasıl 67 Not 1(d) ve 67.01 açıklama notu gereğince bu fasıl dışında kalıp Fasıl "
  "65’te yer alır. Tuzak, şapka süsü ile şapkanın kendisini aynı yerde sanmaktır.",
  "Fasıl 67 Not 1(d); 67.01 Açıklama Notu.")

# 37
q(84, COK,
  "Aşağıdakilerden hangileri 84.14 pozisyonunda sınıflandırılır?<br/>I. El veya ayakla çalıştırılan hava pompası"
  "<br/>II. Sıvıların aktarılmasına mahsus santrifüj pompa<br/>III. Bir aspiratörü olan, havalandırmaya mahsus "
  "davlumbaz<br/>IV. Gaz geçirmez biyolojik güvenlik kabini",
  ["I ve II", "II ve III", "I ve IV", "II, III ve IV", "I, III ve IV"], "E",
  "84.14 pozisyon metni hava veya vakum pompalarını, hava veya gaz kompresörlerini, fanları, bir aspiratörü olan "
  "havalandırma davlumbazlarını ve gaz geçirmez biyolojik güvenlik kabinlerini kapsar; el veya ayakla çalıştırılan "
  "hava pompaları da bu pozisyondadır. Sıvılar için pompalar (ölçü tertibatı olsun olmasın) ise 84.13’te yer alır. "
  "Tuzak, “pompa” ortak adından hareketle sıvı pompasını da 84.14’e almaktır.",
  "84.13 ve 84.14 pozisyon metinleri.")

# 38
q(56, ESYA,
  "Tarife Cetveline göre, ayakkabı parlatmakta kullanılan bir cila (krem) emdirilmiş ve dokumaya elverişli maddenin "
  "yalnızca taşıyıcı (mesnet) olarak işlev gördüğü keçe parçaları hangi pozisyonda sınıflandırılır?",
  ["56.02", "34.05", "59.07", "63.07", "56.03"], "B",
  "Fasıl 56 Not 1(a), dokumaya elverişli maddenin yalnızca mesnet olarak kullanıldığı hallerde 34.05’teki cila, krem "
  "ve benzeri müstahzarlarla emdirilmiş, sıvanmış veya kaplanmış vatka, keçe ve dokunmamış mensucatı bu fasıl dışında "
  "bırakır. Bu nedenle ürün keçe olarak 56.02’de değil, cila müstahzarı olarak 34.05’te yer alır. Tuzak, ürünün "
  "fiziksel olarak keçe olmasına bakarak 56.02’yi seçmektir.",
  "Fasıl 56 Not 1(a).")

# 39
q(46, OLUM,
  "Aşağıdakilerden hangisi Tarife Cetvelinin 46. Faslında <b>sınıflandırılmaz</b>?",
  ["Söğüt sürgünlerinden örülmüş balık sepeti",
   "Muz yapraklarından kesilmiş şeritlerle örülmüş tepsi",
   "Deri şeritlerinin örülmesiyle yapılmış meyve sepeti",
   "Kağıt şeritlerden örülmüş çamaşır sepeti",
   "Hint kamışından örülmüş kuş kafesi"],
  "C",
  "Fasıl 46 Not 1’e göre “örülmeye elverişli madde” tabiri söğüt, hint kamışı, bitkisel şeritler ve kağıt şeritleri "
  "kapsar; ancak deriden veya terkip yoluyla elde edilen deriden şeritleri kapsamaz. Bu nedenle deri şeritlerden "
  "örülmüş sepet Fasıl 46 dışında kalır (genellikle Fasıl 41 veya 42). Balık sepetleri, tepsiler ve kuş kafesleri ise "
  "46.02 açıklama notunda sepetçi eşyası olarak sayılır.",
  "Fasıl 46 Not 1; 46.02 Açıklama Notu; Fasıl 46 Genel Açıklamalar.")

# 40
q(18, ESL,
  "Tarife Cetveline göre; katı veya sıvı kakao yağı ……, yağı tamamen alınmış kakao hamuru (kakao küspesi) ……, kakao "
  "içeren dondurma …… ve tüketime hazır kakaolu likör (crème de cacao) …… yer alır. Boşluklara sırasıyla "
  "aşağıdakilerden hangisi gelmelidir?",
  ["18.04 – 18.05 – 21.05 – Fasıl 22",
   "15.15 – 18.03 – 18.06 – Fasıl 22",
   "18.03 – 18.03 – 18.06 – 18.06",
   "18.04 – 18.03 – 21.05 – Fasıl 22",
   "18.04 – 18.03 – 18.06 – 18.06"],
  "D",
  "Kakao yağı katı veya sıvı halde 18.04’te yer alır; kakao hamuru ise 18.03 pozisyon metni gereği yağı alınmış olsun "
  "olmasın 18.03’tedir ve açıklama notu tamamen veya kısmen yağı alınmış hamuru (kakao küspesi) ismen sayar. Fasıl 18 "
  "Not 1 ve genel açıklamalara göre herhangi bir oranda kakao içeren dondurmalar 21.05’e, “crème de cacao” gibi "
  "tüketime hazır içecekler Fasıl 22’ye gider. Tuzak, kakao içeren her ürünü 18.06’da toplamaktır.",
  "Fasıl 18 Not 1; 18.03 Açıklama Notu; Fasıl 18 Genel Açıklamalar.")

# 41
q("GYK", GYK,
  "Kendinden elektrik motorlu bir epilasyon cihazının 85.10 pozisyonunda yer aldığı belirlendikten sonra, bu "
  "pozisyondaki tıraş makineleri, saç kesme ve hayvan kırkma makineleri ile epilasyon cihazlarına ait tek tireli alt "
  "pozisyonlardan hangisine gireceğinin tespiti hangi kurala göre yapılır?",
  ["GYK 1 – yalnızca pozisyon metni ile bölüm ve fasıl notlarına göre",
   "GYK 3(a) – eşyayı en özel şekilde niteleyen pozisyonun öncelik alması ilkesine göre",
   "GYK 3(c) – geçerli olabilecek alt pozisyonlardan numara sırasına göre sonuncusunun seçilmesiyle",
   "GYK 4 – eşyaya en çok benzeyen eşyanın yer aldığı alt pozisyonun seçilmesiyle",
   "GYK 6 – aynı seviyedeki alt pozisyonlar karşılaştırılarak alt pozisyon metinlerine göre"],
  "E",
  "GYK 6, eşyanın bir pozisyonun alt pozisyonlarındaki yerinin yalnızca aynı seviyedeki alt pozisyonların "
  "karşılaştırılmasıyla, alt pozisyon metinlerine ve ilgili alt pozisyon notlarına göre saptanacağını öngörür; 1 ila 5 "
  "numaralı kurallar bu düzeyde gerekli değişiklikler yapılarak uygulanır. 85.10 içinde epilasyon cihazları için ayrı "
  "bir tek tireli alt pozisyon bulunduğundan alt pozisyon tespiti bu kurala dayanır. GYK 1 ve 3(a) pozisyon "
  "düzeyindeki seçimi, GYK 4 ise hiçbir pozisyona yerleştirilemeyen eşyayı düzenler.",
  "GYK 6 ve Açıklama Notu (I), (II).")

# 42
q(35, FARK,
  "Hayvansal menşeli aşağıdaki protein ürünlerinden hangisi Tarife Cetvelinde diğerlerinden farklı bir pozisyonda "
  "sınıflandırılır?",
  ["Mersin balığının hava keselerinin mekanik işlenmesiyle elde edilen katı ihtiyokol",
   "Kemiklerin sıcak suyla işlenmesiyle elde edilen kemik tutkalı",
   "Bitkisel tanen tayininde kullanılan, kromla işlem görmüş deri tozu",
   "Bir jelatin türevi olan jelatin tannat",
   "Dikdörtgen şeklinde kesilmiş, yüzeyi boyanmış yaprak jelatin"],
  "C",
  "Jelatin (dikdörtgen yaprak halindekiler dahil, yüzeyi işlenmiş veya boyanmış olsun olmasın), jelatin tannat gibi "
  "türevleri, katı ihtiyokol ve kemik tutkalı gibi hayvansal menşeli diğer tutkallar 35.03 pozisyonunda yer alır. "
  "Tanen tayininde kullanılan deri tozu ise kromla işlem görmüş olsun olmasın 35.04 pozisyon metninde ismen "
  "sayılmıştır. Tuzak, deri kökenli olması nedeniyle deri tozunu deri tutkalıyla aynı pozisyonda sanmaktır.",
  "35.03 ve 35.04 pozisyon metinleri ve Açıklama Notları.")

# 43
q(40, SEN,
  "Bir firma; kampta ve plajda kullanılmak üzere tasarlanmış, sertleştirilmemiş vulkanize kauçuktan yapılmış, "
  "ventilinden pompayla hava doldurularak kullanılan ve içinde dolgu malzemesi bulunmayan şişme yatak (şilte) ithal "
  "etmektedir. Bu eşya hangi pozisyonda sınıflandırılır?",
  ["40.16", "94.04", "95.06", "63.06", "40.14"], "A",
  "40.16 açıklama notu; havalı yatakları, yastıkları, minderleri ve diğer şişirilebilir eşyayı (40.14 veya 63.06’daki "
  "eşya hariç) bu pozisyonda sayar. Fasıl 94 Not 1(a) da hava veya su ile şişirilen şilte, yastık ve minderleri Fasıl "
  "94 dışında bırakarak 39, 40 veya 63. Fasıllara yönlendirir; bu nedenle ürün 94.04’e gitmez. 63.06 dokumaya elverişli "
  "maddeden kamp eşyası içindir; tuzak, “yatak” adından hareketle 94.04’ü seçmektir.",
  "40.16 Açıklama Notu; Fasıl 94 Not 1(a).")

# 44
q(91, NOT,
  "Fasıl 91 Genel Açıklamalarına göre aşağıdaki ifadelerden hangisi doğrudur?",
  ["Saatin içine basit bir aydınlatma tertibatı konulması, saatin Fasıl 91 dışında sınıflandırılmasını gerektirir.",
   "Mobilya, lamba veya kalemlik gibi diğer eşya ile birleştirilmiş saatlerin yeri Genel Yorum Kurallarına göre "
   "belirlenir.",
   "Güneş saatleri ve kum saatleri, zaman ölçtükleri için 91.05 pozisyonunda “diğer saatler” olarak yer alır.",
   "Zaman kadranı bulunmayan müzik kutuları, saat mekanizmasıyla çalıştıklarından 91.07 pozisyonunda yer alır.",
   "Saat makinası bulunmayan oyuncak saatler, saat görünümünde olduklarından 91.05 pozisyonunda yer alır."],
  "B",
  "Fasıl 91 Genel Açıklamaları, mobilya, lamba, hokka takımı veya kalemlik gibi diğer eşya ile birleştirilmiş "
  "saatlerin yerinin Genel Yorum Kurallarına göre belirleneceğini, saatlerin içine konulan basit aydınlatma "
  "tertibatının ise bunların bu fasılda kalmasına engel olmadığını belirtir. Aynı açıklamalara göre güneş ve kum "
  "saatleri yapıldıkları maddeye göre, zaman kadransız müzik kutuları 92.08’de, saat makinası olmayan oyuncak saatler "
  "95.03 veya 95.05’te sınıflandırılır.",
  "Fasıl 91 Genel Açıklamalar.")

# 45
q(84, OLUM,
  "Aşağıdakilerden hangisi 84.51 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Kuru temizleme makinesi",
   "Elbise ve çamaşırları ütülemeye mahsus buhar presi",
   "Mensucatı top halinde sarmaya ve katlamaya mahsus makine",
   "Çamaşırhane tipi, yıkama ve kurutma tertibatı bir arada olan çamaşır yıkama makinesi",
   "Mensucatı ağartmaya ve boyamaya mahsus makine"],
  "D",
  "84.51 pozisyonu dokumaya elverişli ipliklerin, mensucatın ve mamullerinin temizlenmesi, kurutulması, ütülenmesi, "
  "ağartılması, boyanması ve apre işlemleri ile mensucatı sarma, katlama ve kesme makinelerini kapsar; kuru temizleme "
  "makineleri ve buhar presleri de buradadır. Ancak pozisyon metni 84.50’dekileri hariç tutar; ev veya çamaşırhane "
  "tipi yıkama makineleri, yıkama ve kurutma tertibatı bir arada olsa bile 84.50’de yer alır. Tuzak, çamaşırhanede "
  "kullanılmasından hareketle makineyi sanayi tipi sayıp 84.51’e almaktır.",
  "84.50 ve 84.51 pozisyon metinleri; 84.51 Açıklama Notu.")

# 46
q(82, ESYA,
  "Tarife Cetveline göre, tıraş makinesi bıçağı imali amacıyla delikleri açılmış ve hafif bir bastırmayla birbirinden "
  "ayrılacak bıçaklar şeklinde zımbalanmış, şerit halindeki çelik taslaklar hangi pozisyonda sınıflandırılır?",
  ["82.08", "85.10", "73.26", "82.11", "82.12"], "E",
  "82.12 pozisyon metni usturaları, tıraş makinelerini ve tıraş bıçaklarını “şerit halindeki taslaklar dahil” olarak "
  "kapsar; açıklama notu, tıraş bıçağı imali için delikleri açılmış veya bıçaklar şeklinde zımbalanmış çelik şerit "
  "taslakların bu pozisyonda yer aldığını belirtir. Elektrikli tıraş makinelerinin kesici ağızları 85.10’a, makine "
  "bıçakları 82.08’e gider. Tuzak, eşyayı henüz bitmemiş bir çelik ürün sayıp demir-çelik eşyası olarak "
  "sınıflandırmaktır.",
  "82.12 pozisyon metni ve Açıklama Notu.")

# 47
q(37, COK,
  "Aşağıdakilerden hangileri 37.05 pozisyonunda sınıflandırılır?<br/>I. Çekilmiş ve develope edilmiş röntgen "
  "(X-ışını) filmi<br/>II. Grafik sanatlarında kullanılan, fotoğraf yöntemiyle elde edilmiş develope film klişeleri<br/>III. Ses izi "
  "bulunan, develope edilmiş sinema filmi<br/>IV. Ofset baskıda doğrudan kullanıma hazır, develope edilmiş fotoğrafik baskı levhası",
  ["I ve II", "I, II ve III", "II ve IV", "I, III ve IV", "II, III ve IV"], "A",
  "37.05 pozisyonu, 37.01 ve 37.02’deki fotoğrafik levha ve filmlerin dolu ve develope edilmiş olanlarını kapsar; "
  "röntgen filmleri 37.01 kapsamındaki filmlerden olduğundan develope edildiğinde 37.05’e girer ve açıklama notu "
  "grafik sanatlarında kullanılan, fotoğraf yöntemiyle elde edilmiş film klişelerini ismen sayar. Hareketli resim projeksiyonunda kullanılan develope edilmiş sinema "
  "filmleri 37.06’ya, ofset baskı için develope edilmiş kullanıma hazır levhalar ise 84.42’ye gider.",
  "37.01 ve 37.05 Açıklama Notları.")

# 48
q(55, NOT,
  "Akrilik devamsız lif ipliklerinden oluşan iki paralel iplik tabakası, iplikler dik açı oluşturacak şekilde üst üste "
  "konulmuş ve kesişme noktalarında bir yapıştırıcıyla birbirine bağlanmıştır. Bölüm XI notlarına göre bu ürünle "
  "ilgili aşağıdakilerden hangisi doğrudur?",
  ["İplikler dokuma yoluyla birleşmediğinden dokunmamış mensucat olarak 56.03 pozisyonunda sınıflandırılır.",
   "Bölüm XI Not 9 uyarınca dokunmuş mensucat sayılır ve Fasıl 55’in dokunmuş mensucat pozisyonlarında yer alır.",
   "Tabakalar yapıştırıcıyla birbirine tutturulduğundan keçe olarak 56.02 pozisyonunda sınıflandırılır.",
   "İplik tabakalarından oluştuğu için Fasıl 55’in iplik pozisyonlarında, iplik olarak sınıflandırılır.",
   "Dokuma tezgahında üretilmediğinden örme veya kroşe mensucat olarak Fasıl 60’ta sınıflandırılır."],
  "B",
  "Bölüm XI Not 9’a göre 50 ila 55. fasıllardaki dokunmuş mensucata, dokumaya elverişli paralel ipliklerin dar veya "
  "dik açı oluşturacak şekilde üst üste konulmasıyla meydana gelen ve ipliklerin kesişme noktalarında bir birleştirici "
  "veya sıcak yapıştırma ile birleştirildiği tabakalı mensucat da dahildir. Bu nedenle akrilik devamsız lif "
  "ipliklerinden oluşan ürün Fasıl 55’in dokunmuş mensucat pozisyonlarında yer alır. Tuzak, “dokuma yapılmadığı” "
  "gerekçesiyle ürünü Fasıl 56 veya 60’a götürmektir.",
  "Bölüm XI Not 9.")

# 49
q("GYK", GYK,
  "GYK 3(a) ve açıklama notuna göre, iki pozisyondan hangisinin eşyayı daha özel şekilde nitelediğinin "
  "belirlenmesine ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
  ["Numara sırasına göre sonra gelen pozisyon, önce gelen pozisyona göre her zaman daha özel sayılır.",
   "Eşyanın kullanım amacını belirten pozisyon, maddesini belirten pozisyondan her zaman daha özel sayılır.",
   "Perakende takımın yalnız bir kalemine atıfta bulunan pozisyon, o kalemi daha kesin tanımlıyorsa daha özeldir.",
   "Kesin kural konulamaz; genel olarak ismen yapılan tanım sınıf tanımına, daha açık tarif eksik tarife öncelik alır.",
   "Bölüm veya fasıl başlığında eşyanın adının geçtiği pozisyon diğerlerinden daha özel sayılır."],
  "D",
  "GYK 3(a) açıklama notunun (IV) bendi, bir pozisyonun eşyayı diğerinden daha özel niteleyip nitelemediğinin "
  "tespitinde kesin kurallar konulamayacağını, ancak genel olarak ismen yapılmış tanımın sınıf şeklinde yapılan "
  "tanımdan ve eşyayı daha açık tarif eden tanımın daha eksik tanımdan öncelik alacağını belirtir. (V) bendine göre "
  "takımın yalnız bir kalemine atıf yapan pozisyonlar, biri daha kesin tanım verse de eşit derecede özel sayılır; "
  "numara sırası 3(c)’nin, başlıklar ise GYK 1 gereği yalnızca gösterici niteliktedir.",
  "GYK 3(a) Açıklama Notu (IV) ve (V); GYK 1.")

# 50
q(84, NOT,
  "Cam levhaları ultrasonik yöntemle delen ve kesen bir takım tezgahı, aynı zamanda 84.64 pozisyonundaki camı soğuk "
  "olarak işlemeye mahsus makineler tanımına da uymaktadır. Fasıl 84 notlarına göre bu tezgah hangi pozisyonda "
  "sınıflandırılır?",
  ["84.64", "84.79", "84.56", "84.65", "84.59"], "C",
  "Fasıl 84 Not 3’e göre 84.56 pozisyonundaki tanıma ve aynı zamanda 84.57–84.61, 84.64 veya 84.65 pozisyonlarındaki "
  "tanımlara da uyan, herhangi bir maddenin işlenmesine mahsus takım tezgahları 84.56’da sınıflandırılır. Ultrasonik "
  "yöntemle çalışan makineler 84.56 pozisyon metninde ismen sayıldığından, camı soğuk olarak işleme tanımına da uysa "
  "tezgah 84.56’da yer alır. 84.79 ancak başka bir pozisyonda belirtilmeyen makineler içindir; tuzak, işlenen maddeye "
  "bakarak 84.64’ü seçmektir.",
  "Fasıl 84 Not 3; 84.56 pozisyon metni.")


def main():
    assert len(S) == 50, len(S)
    c = Counter(x["cevap"] for x in S)
    assert all(c[L] == 10 for L in "ABCDE"), c
    print(Counter(x["tip"] for x in S))
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"tur": "deneme", "no": 9, "sorular": S}, f, ensure_ascii=False, indent=1)
    print("yazıldı:", OUT)


if __name__ == "__main__":
    main()
