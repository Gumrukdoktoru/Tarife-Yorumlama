#!/usr/bin/env python3
# Fasıl 37 modülü üreteci
import json, os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = "ABCDE"
SORULAR = []


def Q(tip, soru, secenekler, dogru, gerekce, dayanak):
    assert dogru in secenekler, (soru, dogru)
    assert len(secenekler) == 5
    SORULAR.append({"soru": soru, "secenekler": secenekler, "cevap": L[secenekler.index(dogru)],
                    "tip": tip, "gerekce": gerekce, "dayanak": dayanak})


E4 = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
FN = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"

# 1
Q(E4, "Tarife Cetveline göre, diş röntgeninde kullanılan, her iki yüzü hassas hale getirilmiş, henüz ışınlanmamış (boş), düz X-ışını filmi hangi pozisyonda sınıflandırılır?",
  ["37.02", "37.04", "37.01", "90.22", "37.05"], "37.01",
  "37.01, hassas hale getirilmiş boş fotoğraf levhalarını ve düz filmleri (kağıt, karton, mensucat hariç herhangi bir maddeden) kapsar; Açıklama Notu diş röntgeninde kullanılanlar dahil X-ışını levha ve düz filmlerini örnek verir. Rulo halinde olsaydı 37.02’ye, ışınlanmış ama develope edilmemiş olsaydı 37.04’e giderdi. 90.22 röntgen cihazlarının yeridir.",
  "37.01 pozisyon metni ve Açıklama Notu (A)(2).")

# 2
Q(E4, "Eni 35 mm olan, perfore edilmiş, rulo halinde, hassas hale getirilmiş ve henüz ışınlanmamış sinema filmi hangi pozisyonda yer alır?",
  ["37.06", "37.02", "37.01", "39.20", "37.04"], "37.02",
  "37.02, fotoğrafçılıkta kullanılan rulo halindeki hassas boş filmleri kapsar; Açıklama Notu standart genişliği 35, 16, 9,5 veya 8 mm olan sinematograf filmlerini ismen sayar. 37.06 yalnızca dolu ve develope edilmiş sinema filmlerini kapsar; hassas hale getirilmemiş plastik film Fasıl 39’dadır.",
  "37.02 pozisyon metni ve Açıklama Notu (A).")

# 3
Q(E4, "Mavi baskı (kopya) işlerinde kullanılmak üzere ferrisiyanür ile hassas hale getirilmiş, boş kağıt hangi pozisyonda sınıflandırılır?",
  ["37.03", "48.09", "37.01", "49.11", "37.07"], "37.03",
  "37.03, hassas hale getirilmiş boş fotoğrafçılık kağıdı, karton ve mensucatını düz veya rulo halde kapsar; Açıklama Notu mavi baskılarda kullanılan ferrisiyanür ve ferro-galat kağıtlarını örnek verir. 37.01 kağıt dışındaki maddelerden levha ve filmleri kapsar; hassas olmayan kaplı kağıtlar Fasıl 48’e gider.",
  "37.03 pozisyon metni ve Açıklama Notu (3).")

# 4
Q(E4, "Şeffaf mesnet üzerinde, dolu ve develope edilmiş mikrokopi (mikrofilm) Tarife Cetvelinde hangi pozisyonda yer alır?",
  ["37.06", "37.04", "49.11", "37.05", "85.23"], "37.05",
  "37.05, sinemacılıkta kullanılanlar hariç dolu ve develope edilmiş fotoğraf levha ve filmlerini kapsar; Açıklama Notu şeffaf mesnetli mikrokopileri (mikrofilmler) açıkça bu pozisyona alır. 37.04 develope edilmemiş olanların, 37.06 develope edilmiş sinema filmlerinin yeridir.",
  "37.05 pozisyon metni ve Açıklama Notu.")

# 5
Q(E4, "Fotoğraf yöntemiyle hazırlanmış, develope edilmiş ve ofset baskıda doğrudan kullanıma hazır baskı levhası hangi pozisyonda sınıflandırılır?",
  ["37.05", "37.01", "84.42", "37.04", "49.11"], "84.42",
  "37.05 Açıklama Notu, ofset baskı gibi baskı için develope edilmiş ve kullanıma hazır levhaları hariç tutarak 84.42’ye gönderir. Fotoğrafik yolla hazırlanmış olmaları onları Fasıl 37’de tutmaz; boş fotomekanik levhalar ise 37.01’dedir.",
  "37.05 Açıklama Notu, hariç (c).")

# 6
Q(OT, "Aşağıdakilerden hangisi Tarife Cetvelinin 37. faslında <b>sınıflandırılmaz</b>?",
  ["Dolu fakat develope edilmemiş fotoğraf kağıdı", "Develope edilmiş fotoğraf kağıdı (basılmış fotoğraf)", "Develope edilmiş 16 mm sinema filmi",
   "Perakende satış için hazırlanmış fiksör müstahzarı", "Hassas hale getirilmiş boş fotoğraf kağıdı"],
  "Develope edilmiş fotoğraf kağıdı (basılmış fotoğraf)",
  "Fasıl 37 Genel Açıklamalarına göre fotoğraf kağıtları, kartonları ve mensucatı yalnızca boş veya dolu fakat develope edilmemiş halde bu fasıldadır; develope edilmiş olanlar Fasıl 49’da veya Bölüm XI’de yer alır. Dolu-develope edilmemiş kağıt 37.04’te, develope sinema filmi 37.06’da, fiksör 37.07’de, boş hassas kağıt 37.03’tedir.",
  "Fasıl 37 Genel Açıklamalar (B); 37.04 Açıklama Notu.")

# 7
Q(OT, "Aşağıdakilerden hangisi 37.07 pozisyonunda <b>yer almaz</b>?",
  ["Hidrokinon esaslı develope edici müstahzar", "Perakende ambalajda, magnezyum tozu esaslı flaş ışığı maddesi",
   "Develope banyosu için ölçülendirilmiş sodyum tiyosülfat tabletleri", "Yüzeyleri hassas hale getirmeye mahsus fotoğraf emülsiyonu",
   "Negatiflerin muhafazası ve parlaklık verilmesi için kullanılan vernik"],
  "Negatiflerin muhafazası ve parlaklık verilmesi için kullanılan vernik",
  "37.07 pozisyon metni vernikleri, tutkalları ve yapıştırıcıları hariç tutar; Açıklama Notu da fotoğrafik görüntünün elde edilmesinde doğrudan kullanılmayan yardımcı ürünleri (negatif koruma verniği, fotoğraf yapıştırma zamkı, rötuş boyası) kapsam dışı bırakır. Develope ediciler, ölçülü fiksör tabletleri, perakende flaş maddeleri ve emülsiyonlar 37.07’dedir.",
  "37.07 pozisyon metni ve Açıklama Notu, hariç (a).")

# 8
Q(OT, "Aşağıdakilerden hangisi 37.02 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Rulo halinde, hassas, boş 16 mm sinema filmi", "Rulo halinde anında develope olarak fotoğraf veren hassas boş film",
   "Mekanik usulle ses kaydı için hazırlanmış, kayıt yapılmamış film", "Fotoelektrik yöntemle ses kaydı için hassas hale getirilmiş film",
   "Kullanıma uygun ebatlarda kesilmemiş hassas boş fotoğraf filmi"],
  "Mekanik usulle ses kaydı için hazırlanmış, kayıt yapılmamış film",
  "37.02 Açıklama Notu, mekanik usulle ses kaydı için hazırlanmış kayıt yapılmamış filmleri hariç tutarak 85.23’e gönderir; bunlar ışığa duyarlı değildir. Fotoelektrik yöntemle ses kaydına mahsus hassas filmler, rulo anında filmler, sinema filmleri ve ebatlarına kesilmemiş filmler 37.02’dedir.",
  "37.02 Açıklama Notu, hariç (c).")

# 9
Q(OT, "Aşağıdakilerden hangisi 37.03 pozisyonu kapsamında <b>değildir</b>?",
  ["Fotoğraf pozitiflerinin elde edilmesine mahsus hassas boş kağıt", "Kamerada negatif elde etmek için kullanılan hassas kağıt “film”",
   "Elektrokardiyografide kullanılan hassas boş kağıt", "Ferro-galat ile hassaslaştırılmış mavi baskı kağıdı",
   "Baryum sülfat ile kaplanmış fakat hassas hale getirilmemiş kağıt"],
  "Baryum sülfat ile kaplanmış fakat hassas hale getirilmemiş kağıt",
  "37.03 Açıklama Notu, albümin, jelatin, baryum sülfat veya çinko oksitle hazırlanmış ancak hassas hale getirilmemiş kağıt, karton ve mensucatı hariç tutar (Fasıl 48 veya Bölüm XI). Pozitif kağıtları, negatif için kullanılan kağıt “film”ler, elektrokardiyografi kağıtları ve ferro-galat kağıtları hassas oldukları için 37.03’tedir.",
  "37.03 Açıklama Notu ve hariç (c).")

# 10
Q(FA, "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
  ["Dolu ve develope edilmiş diapozitif (slayt)", "Şeffaf mesnetli develope edilmiş mikrofilm", "Grafik sanatlarında kullanılan develope edilmiş raster film klişesi",
   "Develope edilmiş fotoğraf negatifi (cam levha)", "Sinema projeksiyon cihazında kullanılan develope edilmiş 35 mm film"],
  "Sinema projeksiyon cihazında kullanılan develope edilmiş 35 mm film",
  "Diapozitifler, mikrofilmler, film klişeleri ve develope edilmiş negatif levhalar 37.05’tedir. Hareketli resim projeksiyonunda kullanılan develope edilmiş sinema filmleri ise 37.05’ten hariç tutulup 37.06’da sınıflandırılır.",
  "37.05 Açıklama Notu ve hariç (a); 37.06 Açıklama Notu.")

# 11
Q(FA, "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda yer alır?",
  ["Fotoelektrik yöntemle kaydedilmiş ses izi taşıyan develope edilmiş sinema filmi", "Hassas hale getirilmiş boş düz X-ışını filmi",
   "Hassas hale getirilmiş boş fotoğraf kağıdı", "Yalnızca manyetik yöntemle kaydedilmiş ses izi taşıyan develope edilmiş film",
   "Fotoğrafçılıkta kullanılmak üzere karıştırılmış fiksör müstahzarı"],
  "Yalnızca manyetik yöntemle kaydedilmiş ses izi taşıyan develope edilmiş film",
  "37.06 Açıklama Notuna göre sadece ses izi taşıyan filmlerde ses izinin fotoelektrik yöntemle kaydedilmiş olması gerekir; ses izi yalnızca mekanik veya manyetik yolla elde edilmiş filmler 85.23’e (Fasıl 85) gider. Diğer seçenekler 37.06, 37.01, 37.03 ve 37.07’de, yani Fasıl 37’dedir.",
  "37.06 Açıklama Notu, son paragraf.")

# 12
Q(FA, "Aşağıdaki eşya ikililerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
  ["Hassas, boş düz film – hassas, boş rulo film", "Develope edilmiş fotoğraf negatifi – develope edilmiş fotoğraf kağıdı",
   "Fotoğrafçılıkta kullanılan flaş ışığı maddesi – fotoğrafik flaş lambası", "Dolu fakat develope edilmemiş film – dolu fakat develope edilmemiş fotoğraf kağıdı",
   "Hassas hale getirilmiş boş plastik film – hassas hale getirilmemiş plastik film"],
  "Dolu fakat develope edilmemiş film – dolu fakat develope edilmemiş fotoğraf kağıdı",
  "37.04, 37.01, 37.02 ve 37.03’teki levha, film, kağıt, karton ve mensucatın dolu fakat develope edilmemiş olanlarını birlikte kapsar; bu aşamada malzeme ayrımı yapılmaz. Diğer ikililer ayrılır: düz 37.01 / rulo 37.02; negatif 37.05 / kağıt baskı Fasıl 49; flaş maddesi 37.07 / flaş lambası 90.06; hassas film Fasıl 37 / hassas olmayan film Fasıl 39.",
  "37.04 Açıklama Notu; 37.01, 37.05 ve 37.07 Açıklama Notları.")

# 13
Q(FA, "Aşağıdaki fotoğrafçılık ürünlerinden hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
  ["Perakende satış için hazırlanmış fiksör müstahzarı", "İki kimyasalın karıştırılmasıyla elde edilmiş, dökme halde develope edici",
   "Fotoğrafçılıkta kullanılmak üzere perakende satış için ambalajlanmış civalı klorür", "Ölçülendirilmiş miktarlarda sodyum sülfür ton verici",
   "Yüzeyleri hassas hale getirmeye mahsus emülsiyon"],
  "Fotoğrafçılıkta kullanılmak üzere perakende satış için ambalajlanmış civalı klorür",
  "37.07 Açıklama Notu, civalı klorürlerin fotoğrafçılıkta kullanılmaya mahsus ölçülü veya perakende halde olsalar bile 28.52’de sınıflandırılacağını belirtir; Bölüm VI Not 1(B) de 28.52 tanımına uyan ürünlere öncelik verir. Diğer seçenekler 37.07’dedir.",
  "37.07 Açıklama Notu (4); Bölüm VI Not 1(B).")

# 14
Q(FN, "Fasıl 37 Not 2’ye göre “fotoğrafçılığa ait” tabiri neyi ifade eder?",
  ["Yalnızca gümüş halojenür emülsiyonu kullanılan görüntü kaydını",
   "Işığa karşı hassas (ısıya duyarlı dahil) yüzeylerde ışık hareketi veya diğer ışın yayma şekilleriyle doğrudan veya dolaylı olarak görülebilen şekiller meydana getirme işlemini",
   "Elektronik sensörlerle görüntünün sayısal olarak kaydedilmesini",
   "Yalnızca görünür ışıkla yapılan ve ısıya duyarlı yüzeyleri kapsamayan işlemleri",
   "Manyetik ortama ses ve görüntü kaydedilmesini"],
  "Işığa karşı hassas (ısıya duyarlı dahil) yüzeylerde ışık hareketi veya diğer ışın yayma şekilleriyle doğrudan veya dolaylı olarak görülebilen şekiller meydana getirme işlemini",
  "Not 2, “fotoğrafçılığa ait” tabirini ışığa karşı hassas (ısıya duyarlı dahil) yüzeylerde ışık veya diğer ışın yayma şekilleriyle doğrudan ya da dolaylı olarak görülebilen şekiller oluşturma işlemi olarak tanımlar. Isıya duyarlı yüzeyler açıkça dahildir; emülsiyon türüyle sınırlı değildir.",
  "Fasıl 37 Not 2.")

# 15
Q(FN, "Fasıl 37 Genel Açıklamalarına göre fotoğrafçılık levha ve filmlerinin hassas olduğu ışınlar, elektromanyetik spektrumda yaklaşık kaç nanometreden daha uzun dalga boyuna sahip olmayan ışınlardır?",
  ["400 nanometre", "700 nanometre", "3.000 nanometre", "10.000 nanometre", "1.300 nanometre"], "1.300 nanometre",
  "Genel Açıklamalar, bu fasıldaki hassas malzemelerin elektromanyetik spektrumda yaklaşık 1.300 nanometreden daha uzun dalga boyuna sahip olmayan ışınlara (gama ışını, X-ışını, ultraviyole ve yakın kızılötesi) ve nükleer ya da parçacık ışınlarına duyarlı olduğunu belirtir. Kızılötesi lazere duyarlı levhalara ısıya duyarlı (termal) levhalar denir.",
  "Fasıl 37 Genel Açıklamalar.")

# 16
Q(FN, "Fasıl 37 Genel Açıklamalarına göre fotoğraf kağıtları, kartonları ve mensucatı ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
  ["Develope edilmiş olsalar da Fasıl 37’de kalırlar.",
   "Boş veya dolu olsunlar, develope edilmemiş iseler Fasıl 37’de; develope edilmiş iseler Fasıl 49’da veya Bölüm XI’de yer alırlar.",
   "Yalnızca boş olanlar Fasıl 37’dedir; dolu olanlar Fasıl 49’a gider.",
   "Kağıttan yapılmış negatif “film”ler 37.01’de yer alır.",
   "Develope edilmiş kağıtlar 37.05’te yer alır."],
  "Boş veya dolu olsunlar, develope edilmemiş iseler Fasıl 37’de; develope edilmiş iseler Fasıl 49’da veya Bölüm XI’de yer alırlar.",
  "Genel Açıklamalar (B), fotoğraf kağıdı, karton ve mensucatın yalnızca boş veya dolu fakat develope edilmemiş halde Fasıl 37’de kaldığını; develope edilenlerin Fasıl 49 veya Bölüm XI’e gittiğini belirtir. Levha ve filmler ise develope edilmiş halde de 37.05 veya 37.06’da kalır; kağıt “film”ler 37.03’tedir.",
  "Fasıl 37 Genel Açıklamalar (B); 37.03 Açıklama Notu.")

# 17
Q(FN, "37.07 Açıklama Notunda fotoğrafçılıkta kullanılan ürünler için konulan şartlarla ilgili aşağıdakilerden hangisi <b>yanlıştır</b>?",
  ["Karışım halinde olmayan maddeler, ölçülendirilmiş miktarlarda hazırlanmışlarsa 37.07’de yer alır.",
   "Karışım halinde olmayan maddeler, perakende satılacak şekilde ambalajlanmış ve fotoğrafçılıkta kullanıma hazır olduğuna dair ibare taşıyorsa 37.07’de yer alır.",
   "Fotoğrafçılıkta kullanılmak amacıyla iki veya daha fazla ürünün karıştırılmasıyla elde edilen müstahzarlar dökme halde de 37.07’de yer alır.",
   "Karışım halinde olmayan maddeler dökme halde sunulsalar da fotoğrafçılıkta kullanılacaklarsa 37.07’de yer alır.",
   "Şartları taşımayan karışmamış maddeler niteliklerine göre (ör. Fasıl 28 veya 29) sınıflandırılır."],
  "Karışım halinde olmayan maddeler dökme halde sunulsalar da fotoğrafçılıkta kullanılacaklarsa 37.07’de yer alır.",
  "Karışmamış ürünler yalnızca ölçülendirilmiş miktarlarda veya kullanıma hazır ibaresiyle perakende ambalajda iseler 37.07’dedir; aksi halde kimyasal ürün olarak Fasıl 28 veya 29’da, metal tozu olarak Bölüm XV’te vb. sınıflandırılır. Karışımlar için ise sunum şekli önemsizdir.",
  "37.07 pozisyon metni ve Açıklama Notu (A), (B).")

# 18
Q(GYK, "Kamera içine doğrudan takılabilecek bir kutu içinde; hassas hale getirilmiş negatif levha, özel işlem görmüş pozitif kağıt ve develope ediciden oluşan, düz halde, anında develope olarak fotoğraf veren film 37.01 pozisyonunda sınıflandırılır. Bu sınıflandırma hangi Genel Yorum Kuralına dayanır?",
  ["GYK 1", "GYK 3(b)", "GYK 2(a)", "GYK 3(c)", "GYK 5(a)"], "GYK 1",
  "37.01 pozisyon metni “anında develope olarak fotoğraf veren boş, düz, hassas hale getirilmiş filmler”i ismen kapsar; Açıklama Notu da bu filmi negatif levha, pozitif kağıt ve develope ediciden oluşan bir ürün olarak tanımlar. Farklı bileşenlerden oluşması onu takım (GYK 3(b)) yapmaz; pozisyon metniyle sınıflandırma GYK 1’dir.",
  "GYK 1; 37.01 pozisyon metni ve Açıklama Notu (B).")

# 19
Q(GYK, "Hassas hale getirilmiş boş rulo fotoğraf filmi, ışığın etkisinden korunması için normal olarak kullanılan ışık geçirmez kağıt mahfaza içinde sunulmuştur. Kağıt mahfazanın ayrıca sınıflandırılmayıp filmle birlikte 37.02’de sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
  ["GYK 2(b)", "GYK 3(b)", "GYK 4", "GYK 5(b)", "GYK 6"], "GYK 5(b)",
  "GYK 5(b), içindeki eşyayla birlikte sunulan ve o eşyanın ambalajında normal olarak kullanılan ambalaj maddelerinin eşyayla birlikte sınıflandırılmasını öngörür; 37.02 Açıklama Notu da rulo filmlerin kağıt mahfaza veya uygun ambalajla ışıktan korunduğunu belirtir. Mahfaza sürekli kullanıma elverişli bir kap olmadığından istisna uygulanmaz.",
  "GYK 5(b); 37.02 Açıklama Notu (A).")

# 20
Q(ES, "Aşağıdaki cümlede boş bırakılan yerlere sırasıyla hangisi gelmelidir? “Fasıl 37 Not 1’e göre döküntü ve ıskartalar bu fasla dahil değildir; kıymetli metallerin tekrar kazanılmasında kullanılan türden, kıymetli metal içeren fotoğraf filmi döküntüleri ..... pozisyonunda, plastikten olan döküntü ve hurdalar ise ..... pozisyonunda sınıflandırılır.”",
  ["71.12 – 39.15", "37.04 – 39.15", "71.12 – 47.07", "28.43 – 39.15", "81.12 – 39.20"],
  "71.12 – 39.15",
  "Fasıl 37 Not 1 döküntü ve ıskartaları fasıl dışında bırakır; Genel Açıklamalar, kıymetli metal kazanılmasında kullanılan türden kıymetli metal içeren film döküntülerini 71.12’ye, diğerlerini malzemesine göre (plastikten olanları 39.15’e, kağıttan olanları 47.07’ye) gönderir.",
  "Fasıl 37 Not 1; Fasıl 37 Genel Açıklamalar, son paragraf.")

# 21
Q(ES, "Fotoğrafçılıkta kullanılan film ve levhaların durumları ile pozisyonları eşleştirildiğinde hangi seçenek doğru olur? I. Hassas hale getirilmiş, boş, düz film; II. Dolu fakat develope edilmemiş film; III. Dolu ve develope edilmiş film (sinema filmi hariç); IV. Dolu ve develope edilmiş sinema filmi. — a. 37.05 · b. 37.01 · c. 37.06 · d. 37.04",
  ["I-b, II-d, III-a, IV-c", "I-d, II-b, III-a, IV-c", "I-b, II-a, III-d, IV-c", "I-b, II-d, III-c, IV-a", "I-a, II-d, III-b, IV-c"],
  "I-b, II-d, III-a, IV-c",
  "Boş düz film ve levhalar 37.01’de, dolu fakat develope edilmemiş olanlar 37.04’te, dolu ve develope edilmiş levha ve filmler (sinema hariç) 37.05’te, develope edilmiş sinema filmleri 37.06’dadır. Fasıl, eşyanın işlem aşamasını (boş → dolu → develope) pozisyon sırasına yansıtır.",
  "37.01, 37.04, 37.05 ve 37.06 pozisyon metinleri.")

# 22
Q(CC, "Aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Fotoğrafçılıkta kullanılmak üzere perakende satış için ambalajlanmış gümüş nitrat 37.07’de yer alır. II. Fotoğrafçılıkta kullanılmak amacıyla iki ürünün karıştırılmasıyla elde edilen müstahzarlar dökme halde de 37.07’dedir. III. Fotoğrafların yapıştırılmasında kullanılan zamklar 37.07’dedir. IV. Elektrostatik dokümanların reprodüksiyonu için kullanılan develope ediciler 37.07’dedir.",
  ["I ve II", "II ve IV", "I, II ve IV", "II, III ve IV", "III ve IV"], "II ve IV",
  "Karışım halindeki fotoğraf müstahzarları sunum şekline bakılmaksızın 37.07’dedir (II doğru); Açıklama Notu elektrostatik reprodüksiyon develope edicilerini de kapsama alır (IV doğru). Gümüş nitrat perakende ambalajlı olsa bile Bölüm VI Not 1(B) uyarınca 28.43’tedir (I yanlış); fotoğraf yapıştırma zamkları doğrudan görüntü elde etmede kullanılmadığından hariçtir (III yanlış).",
  "37.07 Açıklama Notu; Bölüm VI Not 1(B) ve Genel Açıklaması.")

# 23
Q(CC, "Fasıl 37 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Bu fasıldaki levha ve filmler boş ya da dolu (develope edilmiş olsun olmasın) olabilir. II. Develope edilmiş fotoğraf kağıtları 37.05’te yer alır. III. Bazı levhalar emülsiyonla kaplı olmayıp tamamen veya esas itibarıyla ışığa duyarlı plastiklerden ibarettir. IV. Hassas hale getirilmemiş plastik düz filmler 37.01’de yer alır.",
  ["I ve III", "II ve IV", "I, II ve III", "Yalnız I", "I, III ve IV"], "I ve III",
  "Genel Açıklamalar levha ve filmlerin boş veya dolu (develope edilmiş olsun olmasın) olabileceğini ve bazı levhaların ışığa duyarlı plastiklerden ibaret olduğunu belirtir (I ve III doğru). Develope edilmiş kağıtlar Fasıl 49 veya Bölüm XI’dedir (II yanlış); hassas hale getirilmemiş levha ve düz filmler mamul oldukları maddeye göre sınıflandırılır (IV yanlış).",
  "Fasıl 37 Genel Açıklamalar; 37.01 Açıklama Notu, hariç (a).")

# 24
Q(SN, "Hidrokinon ile sodyum sülfitin karıştırılmasıyla hazırlanmış, fotoğrafik görüntüleri görünür hale getirmekte kullanılan ve 200 litrelik varillerde dökme olarak sunulan sıvı develope edici hangi tarife pozisyonunda sınıflandırılır?",
  ["29.07", "38.24", "37.07", "28.32", "37.04"], "37.07",
  "37.07 Açıklama Notuna göre fotoğrafçılıkta kullanılmak amacıyla iki veya daha fazla ürünün karıştırılmasından elde edilen müstahzarlar, küçük miktarlarda veya dökme halde olsun, perakende olsun olmasın bu pozisyondadır. Dökme sunum yalnızca karışmamış tek maddeler için belirleyicidir; bileşenlerden birinin kimyasal pozisyonu (29.07 veya 28.32) seçilmez.",
  "37.07 Açıklama Notu (B).")

# 25
Q(SN, "Fotoğrafçılıkta tespit (fiksaj) banyosu hazırlamak için satın alınan, başka hiçbir maddeyle karıştırılmamış sodyum tiyosülfat; ölçülendirilmemiş ve perakende ambalajlanmamış halde, 25 kg’lık torbalarda dökme olarak sunulmuştur. Bu ürün hangi tarife pozisyonunda sınıflandırılır?",
  ["37.07", "38.24", "37.04", "29.30", "28.32"], "28.32",
  "37.07 Açıklama Notuna göre karışım halinde olmayan maddeler ancak ölçülendirilmiş miktarlarda veya kullanıma hazır ibareli perakende ambalajda iseler 37.07’dedir; diğer şekilleri kendi niteliklerine göre sınıflandırılır. Sodyum tiyosülfat bir tiyosülfat olarak 28.32’de yer alır; fotoğrafçılıkta kullanılacak olması tek başına 37.07’yi uygulatmaz.",
  "37.07 Açıklama Notu (A); 28.32 pozisyon metni.")

modul = {
    "tur": "fasil",
    "fasil": 37,
    "baslik": "Fotoğrafçılıkta veya sinemacılıkta kullanılan eşya",
    "bolum": "VI",
    "oz": {
        "vurgu": "Fasıl 37, ışığa veya diğer ışınlara duyarlı (ısıya duyarlı dahil) levha, film, kağıt, karton ve mensucatı ve fotoğrafçılık kimyasallarını kapsar. Pozisyonu iki soru belirler: malzeme nedir (levha/film mi, kağıt mı; düz mü, rulo mu) ve işlem aşaması nedir (boş, dolu fakat develope edilmemiş, develope edilmiş)?",
        "maddeler": [
            "Boş hassas malzeme: düz levha ve film 37.01, rulo film 37.02, kağıt-karton-mensucat 37.03.",
            "Dolu fakat develope edilmemiş her türlü hassas malzeme 37.04’tedir.",
            "Develope edilmiş levha ve film 37.05 (slayt, mikrofilm), develope sinema filmi 37.06; develope edilmiş kağıt ise Fasıl 49 veya Bölüm XI.",
            "Fotoğraf kimyasalları 37.07: karışımlar her sunumda, karışmamış maddeler yalnız ölçülü veya perakende kullanıma hazır halde.",
            "Döküntü ve ıskartalar fasıl dışıdır (kıymetli metal içerenler 71.12)."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Döküntü veya ıskarta mı?", "Kıymetli metal içeren <b>71.12</b> · plastik <b>39.15</b> · kağıt <b>47.07</b>"],
            ["2", "Işığa duyarlı (hassas) hale getirilmemiş levha, film veya kağıt mı?", "Malzemesine göre (<b>Fasıl 39</b>, <b>Fasıl 48</b>, <b>Bölüm XI</b>)"],
            ["3", "Kimyasal ürün mü? (emülsiyon, develope edici, fiksör, flaş maddesi)", "<b>37.07</b>* (gümüş nitrat <b>28.43</b> · civalı klorür <b>28.52</b>)"],
            ["4", "Develope edilmiş kağıt, karton veya mensucat mı?", "<b>Fasıl 49</b> / <b>Bölüm XI</b>"],
            ["5", "Develope edilmiş, kullanıma hazır baskı (ofset) levhası mı?", "<b>84.42</b>"],
            ["6", "Develope edilmiş sinema filmi mi? (ses izi fotoelektrik)", "<b>37.06</b> (yalnız manyetik/mekanik ses izi <b>85.23</b>)"],
            ["7", "Develope edilmiş diğer levha veya film mi? (slayt, mikrofilm, film klişe)", "<b>37.05</b>"],
            ["8", "Dolu fakat develope edilmemiş mi? (malzeme fark etmez)", "<b>37.04</b>"],
            ["9", "Boş ve hassas: kağıt/karton/mensucat mı, düz levha/film mi, rulo film mi?", "<b>37.03</b> / <b>37.01</b> / <b>37.02</b>"]
        ],
        "dipnot": "* Karışmamış tek bir madde yalnızca ölçülendirilmiş miktarlarda veya kullanıma hazır ibareli perakende ambalajda 37.07’dedir; aksi halde Fasıl 28, 29 veya Bölüm XV’e gider. Vernik, tutkal ve rötuş malzemeleri 37.07 dışıdır."
    },
    "pozisyon_haritasi": [
        ["37.01", "Boş hassas levha ve düz filmler", "Düz; kağıt dışı malzeme; anında film (düz)", "Boş X-ışını filmi, fotomekanik levha"],
        ["37.02", "Boş hassas rulo filmler", "Rulo; anında film (rulo)", "35 mm boş sinema filmi, rulo film"],
        ["37.03", "Boş hassas kağıt, karton, mensucat", "Kağıt esaslı; düz veya rulo", "Fotoğraf baskı kağıdı, mavi baskı kağıdı"],
        ["37.04", "Dolu, develope edilmemiş malzeme", "Işınlanmış, banyo görmemiş", "Çekilmiş ama banyo edilmemiş film"],
        ["37.05", "Dolu, develope levha ve filmler", "Sinema filmi hariç", "Slayt, mikrofilm, negatif"],
        ["37.06", "Develope edilmiş sinema filmleri", "Görüntü ve/veya fotoelektrik ses izi", "35 mm gösterim kopyası"],
        ["37.07", "Fotoğraf kimyasalları ve flaş maddeleri", "Karışım her halde; tek madde dozlu/perakende", "Develope edici, fiksör, emülsiyon"]
    ],
    "notlar": [
        ["Bölüm VI Not 1(B)", "28.43, 28.46 veya 28.52 tanımına uyan ürünler Bölüm VI’nın başka pozisyonuna girmez: fotoğrafçılık için perakende ambalajlanmış gümüş nitrat 37.07’de değil 28.43’tedir."],
        ["Bölüm VI Not 2", "Ölçülü dozlarda veya perakende satış için hazırlanmış olması nedeniyle 37.07’ye giren ürünler başka pozisyona girmez."],
        ["Fasıl 37 Not 1", "Döküntü ve ıskartalar bu fasla dahil değildir."],
        ["Fasıl 37 Not 2", "“Fotoğrafçılığa ait”: ışığa karşı hassas (<b>ısıya duyarlı dahil</b>) yüzeylerde ışık hareketi veya diğer ışın yayma şekilleriyle doğrudan veya dolaylı olarak görülebilen şekiller meydana getirme işlemi."],
        ["Genel Açıklamalar", "Hassas malzemeler yaklaşık <b>1.300 nm</b>’den uzun olmayan dalga boyundaki ışınlara (gama, X, ultraviyole, yakın kızılötesi) ve nükleer/parçacık ışınlarına duyarlıdır. Levha ve filmler boş veya dolu (develope edilmiş olsun olmasın) olabilir; kağıt, karton ve mensucat ise yalnız <b>develope edilmemiş</b> halde bu fasıldadır (develope edilmişler Fasıl 49 / Bölüm XI). Kıymetli metal içeren film döküntüleri 71.12’de; diğer döküntüler malzemesine göre (plastik 39.15, kağıt 47.07)."],
        ["37.01 Açıklama Notu", "Düz levha ve filmler (disk film dahil) cam, plastik, metal veya taştan olabilir; X-ışını ve fotomekanik levhalar dahil; bazı levhalar ışığa duyarlı plastikten ibarettir. Hariç: hassas hale getirilmemiş levha ve filmler (malzemesine göre), rulo filmler (37.02). Rulo anında film 37.02’dedir."],
        ["37.02 Açıklama Notu", "35, 16, 9,5 veya 8 mm sinema filmleri, rulo kamera filmleri, ebatına kesilmemiş filmler ve fotoelektrik ses kaydı için hassas filmler dahil. Hariç: düz filmler (37.01), hassas olmayan plastik film (Fasıl 39), mekanik ses kaydı için boş filmler (85.23)."],
        ["37.03 Açıklama Notu", "Pozitif kağıtları, negatif için kağıt “levha/film”ler, mavi baskı (ferrisiyanür, ferro-galat) kağıtları. Hariç: anında filmler (37.01/37.02), dolu-develope edilmemiş kağıt (37.04), hassas olmayan kaplı kağıt (Fasıl 48 / Bölüm XI), develope edilmiş kağıt (Fasıl 49 / Bölüm XI)."],
        ["37.05 Açıklama Notu", "Develope edilmiş negatif ve pozitif (diapozitif) levha ve filmler, şeffaf mesnetli mikrofilmler, grafik sanatlarında kullanılan film klişeleri. Hariç: develope sinema filmleri (37.06), develope kağıtlar (Fasıl 49 / Bölüm XI), kullanıma hazır develope baskı levhaları (84.42)."],
        ["37.06 Açıklama Notu", "Develope edilmiş sinema filmleri, görüntü ve/veya ses izli. Yalnız ses izi taşıyanlarda iz <b>fotoelektrik</b> olmalı; birden çok izde en az biri fotoelektrik olmalıdır. Ses izi yalnız mekanik veya manyetik yolla kaydedilmiş filmler 85.23’tedir."],
        ["37.07 Açıklama Notu", "Emülsiyonlar, develope ediciler (elektrostatik reprodüksiyon için olanlar dahil), fiksörler, koyulaştırıcı/indirgeyiciler, tonerler, temizleyiciler ve magnezyum/alüminyum esaslı flaş maddeleri. Karışmamış maddeler yalnız ölçülendirilmiş veya kullanıma hazır perakende halde; karışımlar her halde. Hariç: zamk, vernik, rötuş boya ve kalemleri; flaş lambaları (90.06); 28.43–28.46 ve 28.52 ürünleri (civalı klorür 28.52)."]
    ],
    "sinir_komsulari": [
        ["Kıymetli metal içeren film döküntüsü", "71.12", "Fasıl 37 Not 1"],
        ["Plastik veya kağıt film döküntüleri", "39.15 / 47.07", "Malzemesine göre"],
        ["Hassas hale getirilmemiş plastik film ve levha", "Fasıl 39", "Işığa duyarlı değil"],
        ["Albümin, jelatin veya baryum sülfat kaplı, hassas olmayan kağıt", "Fasıl 48 / Bölüm XI", "37.03 hariç tutması"],
        ["Develope edilmiş fotoğraf kağıdı (basılı fotoğraf)", "Fasıl 49 / Bölüm XI", "Kağıt yalnız develope edilmemiş halde Fasıl 37’de"],
        ["Develope edilmiş, kullanıma hazır ofset baskı levhası", "84.42", "37.05 hariç tutması"],
        ["Yalnız manyetik ses izli film; mekanik ses kaydı için boş film", "85.23", "Fotoelektrik değil"],
        ["Fotoğrafik flaş lambası", "90.06", "37.07 hariç tutması"],
        ["Uçaklarda kullanılan foto-flaş fişeği", "36.04", "Pirotekni eşyası"],
        ["Gümüş nitrat (perakende olsa da)", "28.43", "Bölüm VI Not 1(B)"],
        ["Civalı klorür (fotoğraf amaçlı perakende olsa da)", "28.52", "37.07 Açıklama Notu"],
        ["Dökme, karışmamış sodyum tiyosülfat", "28.32", "Ölçülü veya perakende değil"],
        ["Fotoğraf yapıştırma zamkı, negatif verniği, rötuş kalemi", "Kendi pozisyonları", "Görüntü elde etmede doğrudan kullanılmaz"]
    ],
    "tuzaklar": [
        "<b>Kağıt film değildir.</b> Hassas boş kağıt, karton ve mensucat 37.03’te; kağıttan negatif “film”ler bile 37.03’tedir.",
        "<b>Düz mü, rulo mu?</b> Boş levha ve düz film 37.01, rulo film 37.02; anında develope filmler de şekline göre bu iki pozisyona ayrılır.",
        "<b>Dolu fakat develope edilmemiş her şey 37.04.</b> Bu aşamada film-kağıt ayrımı yapılmaz.",
        "<b>Develope edilmiş kağıt Fasıl 37’den çıkar.</b> Basılı fotoğraf Fasıl 49 veya Bölüm XI; develope edilmiş film ise 37.05 veya 37.06’da kalır.",
        "<b>Sinema filmi ayrı tutulur.</b> Develope sinema filmi 37.06; slayt, mikrofilm ve film klişe 37.05.",
        "<b>Ses izi fotoelektrik olmalıdır.</b> Yalnız manyetik veya mekanik ses izli film 85.23’e gider.",
        "<b>Tek kimyasal ile karışım farklı işlem görür.</b> Karışım dökme halde de 37.07; karışmamış madde yalnız ölçülü veya perakende kullanıma hazır halde 37.07, aksi halde Fasıl 28–29.",
        "<b>Kıymetli metal ve civa bileşikleri öncelik alır.</b> Gümüş nitrat 28.43, civalı klorür 28.52; perakende fotoğraf ambalajı sonucu değiştirmez.",
        "<b>Develope ofset levhası makine aksamıdır.</b> Kullanıma hazır baskı levhası 84.42; boş fotomekanik levha 37.01.",
        "<b>Flaşın üç yeri vardır.</b> Flaş tozu 37.07, flaş lambası 90.06, uçak foto-flaş fişeği 36.04."
    ],
    "hafiza": {
        "kanca": "LE – RU – KA – DO – DE – Sİ – Kİ",
        "aciklama": "<b>LE</b>vha ve düz film 37.01 · <b>RU</b>lo film 37.02 · <b>KA</b>ğıt 37.03 · <b>DO</b>lu ama banyo edilmemiş 37.04 · <b>DE</b>velope (sinema hariç) 37.05 · <b>Sİ</b>nema filmi 37.06 · <b>Kİ</b>myasallar 37.07. Görsel benzetme: fotoğrafçı dükkândan boş levha, rulo ve kağıt alır, çekim yapar (dolu), karanlık odada banyo eder (develope), filmi sinemada gösterir; raftaki şişelerde kimyasallar durur."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda doğrudan sorulmamıştır; fotoğrafçılık ve sinemacılıkla ilgili eşya sorularda başka fasıllar üzerinden yer almıştır.",
        "Fotoğraf makinesi mahfazasının makineyle birlikte sınıflandırılması (GYK 5(a)) ve 42.02’deki mahfazalar sorulmuştur; kamera ve kabı Fasıl 37 eşyası değildir.",
        "“Aynı fasılda yer almayan eşya” sorularında sinema kamerası gibi cihazların Fasıl 90’da yer aldığı bilgisi kullanılmıştır; Fasıl 37 yalnızca hassas malzemeleri, filmleri ve kimyasalları kapsar.",
        "Örnek soru bulunmadığından bu fasılda pozisyon sırası (boş → dolu → develope), kağıt-film ayrımı ve 37.07’nin sunum şartları esas alınmalıdır."
    ],
    "cikmis_ornekler": [],
    "ozet": [
        "Fasıl 37 = ışığa (ısı dahil) duyarlı malzemeler ve fotoğraf kimyasalları; kamera ve cihazlar Fasıl 90, döküntüler 71.12 veya malzemesine göre.",
        "Boş: düz levha/film 37.01, rulo film 37.02, kağıt-karton-mensucat 37.03.",
        "Dolu fakat develope edilmemiş her şey 37.04.",
        "Develope: levha ve film 37.05, sinema filmi 37.06 (ses izi fotoelektrik); develope kağıt Fasıl 49 / Bölüm XI.",
        "37.07: karışımlar her halde, tek maddeler yalnız ölçülü veya perakende kullanıma hazır; gümüş nitrat 28.43, civalı klorür 28.52.",
        "Ofset levha 84.42, flaş lambası 90.06, manyetik ses izli film 85.23."
    ],
    "sorular": SORULAR
}

if __name__ == "__main__":
    print(Counter(q["cevap"] for q in SORULAR), len(SORULAR))
    print("".join(q["cevap"] for q in SORULAR))
    out = os.path.join(KITAP, "data", "fasil_37.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(modul, f, ensure_ascii=False, indent=1)
    print("yazıldı:", out)
