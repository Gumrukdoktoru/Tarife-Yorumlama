# -*- coding: utf-8 -*-
"""Karma test 7 üreticisi → karma/karma_07.json"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_07.json")

ESYA = "Eşya → 4’lü pozisyon"
POZESYA = "Pozisyon → eşya"
OLUMSUZ = "Olumsuz teşhis"
FARKLI = "Farklı/aynı pozisyon veya fasıl"
BULMA = "Fasıl/Bölüm bulma"
TANIM = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
COKTAN = "Çoktan-çoğa / Eşleştirme"
YAPI = "Tarife yapısı"

S = []


def Q(soru, secenekler, cevap, dogru, tip, gerekce, dayanak, fasil):
    assert len(secenekler) == 5, soru
    assert secenekler["ABCDE".index(cevap)] == dogru, (soru, cevap, dogru)
    S.append({"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
              "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil})


# 1 ─ Genel: tarife yapısı (pozisyon numaralandırması)
Q("Tarife Cetvelinde dört rakamlı pozisyon numaralarının düzeniyle ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
  ["Pozisyon numarasının ilk iki rakamı, pozisyonun yer aldığı bölümün numarasını gösterir.",
   "Her faslın ilk pozisyonu, fasıl numarasını izleyen “.00” rakamlarıyla gösterilir.",
   "Bir fasıldaki pozisyonlar her zaman kesintisiz sıra izler; örneğin 95. Fasıl 95.01 ile başlar.",
   "Bazı pozisyon numaraları kullanılmamaktadır; örneğin 95. Faslın ilk pozisyonu 95.03’tür.",
   "Pozisyon numarasının son iki rakamı, eşyanın tireli alt pozisyon düzeyini gösterir."],
  "D", "Bazı pozisyon numaraları kullanılmamaktadır; örneğin 95. Faslın ilk pozisyonu 95.03’tür.", YAPI,
  "İlk iki rakam faslı, son iki rakam fasıl içindeki sırayı gösterir; ancak numaralar boş kalabilir: 95. Fasılda "
  "[95.01] ve [95.02] kullanılmaz, fasıl 95.03 ile başlar (benzer şekilde [42.04], [88.03]). “.00” ile başlayan "
  "pozisyon yoktur; tireler alt pozisyonları gösterir.",
  "Fasıl 95, 42 ve 88 pozisyon listeleri.", "Genel")

# 2 ─ Fasıl 66: bölüm bulma
Q("Tarife Cetveline göre, dağcıların alpin dağcılığında kullandığı buz baltası hangi bölümde yer alır?",
  ["Bölüm XII", "Bölüm XX", "Bölüm XV", "Bölüm XIX", "Bölüm XVI"],
  "B", "Bölüm XX", BULMA,
  "66.02 Açıklama Notu, alpin dağcılığında kullanılan buz baltalarını bastonlardan ayırarak 95. Fasla gönderir; "
  "95.06 da bunları sayar. Fasıl 95, XX. Bölümdedir. Bastonlar XII. Bölümde (Fasıl 66), adi metal aletler XV. "
  "Bölümde (Fasıl 82) yer alır.",
  "66.02 Açıklama Notu; 95.06 Açıklama Notu.", 66)

# 3 ─ Fasıl 12: eşya → pozisyon
Q("Tarife Cetveline göre, yemeklik yağ üretiminde hammadde olarak kullanılacak kurutulmuş üzüm çekirdekleri hangi "
  "tarife pozisyonunda yer alır?",
  ["08.06", "12.07", "12.12", "12.09", "23.06"],
  "B", "12.07", ESYA,
  "12.07 Açıklama Notu, yağ ekstraksiyonunda kullanılan tohumlar arasında üzüm çekirdeklerini açıkça sayar. Üzüm "
  "08.06’da, kayısı veya şeftali gibi meyve çekirdekleri 12.12’de, yağı alındıktan sonra kalan küspeler ise 23.04–23.06’dadır.",
  "Fasıl 12 Genel Açıklamalar; 12.07 Açıklama Notu.", 12)

# 4 ─ Fasıl 8: olumsuz teşhis
Q("Tarife Cetveline göre aşağıdakilerden hangisi 8. fasılda <b>yer almaz</b>?",
  ["Salamurada geçici olarak konserve edilmiş karpuz kabuğu",
   "Sıcaklığı +10 °C’ye düşürülerek bu derecede tutulan kavun",
   "Toz haline getirilmiş kurutulmuş limon kabuğu",
   "Dondurulmadan önce kaynar suda haşlanmış, dondurulmuş dut",
   "Potasyum sorbat ilavesiyle dayanıklılığı artırılmış kuru erik"],
  "C", "Toz haline getirilmiş kurutulmuş limon kabuğu", OLUMSUZ,
  "08.14 Açıklama Notuna göre toz haline getirilmiş kabuklar 11.06’dadır. Salamuradaki karpuz kabuğu 08.14’te, "
  "+10 °C’de tutulan kavun soğutulmuş sayılarak 08.07’de, haşlanıp dondurulan dut 08.11’de, sorbatla korunan kuru "
  "erik Not 3 gereği 08.13’tedir.",
  "Fasıl 8 Not 2, Not 3; Genel Açıklamalar; 08.14 Açıklama Notu.", 8)

# 5 ─ Fasıl 20: eşya → pozisyon
Q("Tarife Cetveline göre, sirke veya asetik asit kullanılmadan hazırlanıp teneke kutularda hemen tüketime hazır "
  "halde konserve edilmiş, dolma yapımına mahsus bağ (asma) yaprakları hangi tarife pozisyonunda sınıflandırılır?",
  ["20.05", "07.11", "20.01", "12.12", "20.08"],
  "E", "20.08", ESYA,
  "20.08 Açıklama Notu, başka şekilde hazırlanmış veya korunmuş yenilebilir bitki parçaları arasında bağ yapraklarını "
  "açıkça sayar. 20.05’teki “sebzeler” Not 3 ile 7. Fasıl ürünleriyle sınırlıdır; 07.11 geçici koruma, 20.01 sirkeli "
  "hazırlama içindir.",
  "Fasıl 20 Not 3; 20.05 ve 20.08 Açıklama Notları.", 20)

# 6 ─ Fasıl 19: eşya → pozisyon
Q("Tarife Cetveline göre, nemlendirilmiş mısır danelerinin ısıtılarak kabartılmasından sonra üzerine bitkisel yağ, "
  "peynir, tuz ve monosodyum glutamat karışımından oluşan aroma verici madde püskürtülerek elde edilen çeşnili "
  "gevrek çerez hangi tarife pozisyonunda sınıflandırılır?",
  ["19.04", "19.05", "20.05", "10.05", "21.06"],
  "A", "19.04", ESYA,
  "19.04 Açıklama Notu, hububat danelerinin kabartılıp üzerine aroma püskürtülmesiyle elde edilen çeşnili gevrekleri "
  "bu pozisyona alır. Hamurdan yapılıp bitkisel yağda kızartılan benzerleri 19.05’te, işlenmemiş mısır ise 10.05’tedir.",
  "19.04 Açıklama Notu.", 19)

# 7 ─ Fasıl 17: olumsuz teşhis
Q("Aşağıdaki ürünlerden hangisi Tarife Cetvelinin 17. faslında <b>sınıflandırılmaz</b>?",
  ["Tatlı sorgumdan elde edilen, aroma veya renk verici katılmamış sakkaroz şurubu",
   "Renklendirilmiş şeker kamışı melası",
   "Bisküvi yapımında boyayıcı olarak kullanılan renklendirici karamel",
   "Kimyaca saf maltoz",
   "Şeker katılarak tatlandırılmış kakao tozu"],
  "E", "Şeker katılarak tatlandırılmış kakao tozu", OLUMSUZ,
  "Fasıl 17 Genel Açıklamalarına göre tatlandırılmış kakao tozları 18.06’dadır. Sorgum şurubu ve renklendirici "
  "karamel 17.02’de, renklendirilmiş melas 17.03’tedir; kimyaca saf maltoz Not 1’deki istisna nedeniyle 29.40’a "
  "gitmez, 17.02’de kalır.",
  "Fasıl 17 Not 1; Genel Açıklamalar; 17.02 ve 17.03 Açıklama Notları.", 17)

# 8 ─ Fasıl 30: olumsuz teşhis
Q("Aşağıdakilerden hangisi Tarife Cetvelinin 30. faslında <b>sınıflandırılmaz</b>?",
  ["Gliserinde muhafaza edilen, tedavide kullanılmak üzere hazırlanmış kırmızı kemik iliği",
   "Steril laminarya fitilleri",
   "Çürük önleyici florür içeren diş macunu",
   "Cerrahi yaraları kapatmada kullanılan steril doku yapıştırıcısı",
   "Ostomi kullanımına mahsus olduğu belirlenebilen, şekil verilerek kesilmiş kolostomi torbası"],
  "C", "Çürük önleyici florür içeren diş macunu", OLUMSUZ,
  "Fasıl 30 Not 1’e göre 33.03–33.07 müstahzarları tedavi edici veya koruyucu özellik taşısa da bu fasla girmez; "
  "diş macunu 33.06’dadır. Kemik iliği 30.01’de; laminarya fitili, doku yapıştırıcısı ve ostomi torbası Not 4 "
  "gereği 30.06’dadır.",
  "Fasıl 30 Not 1, Not 4; 30.01 ve 33.06 Açıklama Notları.", 30)

# 9 ─ Fasıl 42: fasıl notu / tanım
Q("Tarife Cetvelinin 42. Fasıl notları ve 42.02 Açıklama Notu dikkate alındığında aşağıdakilerden hangisi 42.02 "
  "pozisyonunda sınıflandırılır?",
  ["Hasır örgüden yapılmış el çantası",
   "Uzun süre kullanılmak üzere yapılmamış, baskılı plastik yapraktan saplı çanta",
   "Hazır ağdan yapılmış alışveriş filesi",
   "Ahşap iskeletli, dış yüzü tamamen kâğıtla kaplanmış mücevher kutusu",
   "Kaplanmamış masif ahşaptan yapılmış mücevher kutusu"],
  "D", "Ahşap iskeletli, dış yüzü tamamen kâğıtla kaplanmış mücevher kutusu", TANIM,
  "Pozisyonun ikinci kısmındaki mücevher kutuları, iskeleti ahşap olsa da sayılan maddelerle veya kâğıtla kaplıysa "
  "42.02’dedir. Not 3(A) gereği örme çanta 46.02’de, dayanıksız plastik çanta 39.23’te; Not 2 gereği ağdan eşya "
  "56.08’de; kaplanmamış ahşap kutu 44.20’dedir.",
  "Fasıl 42 Not 2, Not 3(A); 42.02 Açıklama Notu.", 42)

# 10 ─ Fasıl 64: olumsuz teşhis
Q("Aşağıdakilerden hangisi Tarife Cetvelinin 64. faslında yer alan eşyalardan <b>değildir</b>?",
  ["Çok küçük çocuklar için bele kadar uzanan, bacakları saran tek parça tozluk (tayt)",
   "Boks ayakkabısı",
   "Ayakkabı yüzü ile astarı arasına konulan burun takviye parçası",
   "Ağaçtan yapılmış ayakkabı topuğu",
   "Çadır bezinden yapılmış kısa konçlu tozluk"],
  "A", "Çok küçük çocuklar için bele kadar uzanan, bacakları saran tek parça tozluk (tayt)", OLUMSUZ,
  "64.06 Açıklama Notu, çok küçük çocuklara mahsus, bele kadar uzanan tek parça tozlukları (taytları) 61 veya 62. "
  "Fasla gönderir. Boks ayakkabısı spor ayakkabısı olarak 64’te; takviye parçası, ahşap topuk ve kısa konçlu tozluk "
  "64.06’dadır.",
  "Fasıl 64 Genel Açıklamalar; 64.06 Açıklama Notu.", 64)

# 11 ─ Fasıl 88: farklı fasıl
Q("Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda sınıflandırılır?",
  ["Hava gemisine ait, ayrı olarak sunulan pervane",
   "Bir balona ait, ayrı olarak sunulan sepet",
   "Uçak kanadının altında yakıt yerleştirmek için yapılmış çıkıntılı bölme",
   "Eğlence parkı gezintileri için özel olarak tasarlanmış uçak modeli",
   "Bulut yüksekliğini anlamak için kullanılan irtifa balonu"],
  "D", "Eğlence parkı gezintileri için özel olarak tasarlanmış uçak modeli", FARKLI,
  "88.02 Açıklama Notu, eğlence parkı gezintileri ve panayırlar için özel olarak tasarlanmış modelleri 95.08’e "
  "gönderir. Hava gemisi pervanesi, balon sepeti ve kanat altı yakıt bölmesi 88.07’de, irtifa balonu 88.01’de, "
  "yani 88. Fasıldadır.",
  "88.01, 88.02 ve 88.07 Açıklama Notları.", 88)

# 12 ─ Fasıl 95: farklı fasıl
Q("Oyuncak bebeklerle ilgili aşağıdaki eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
  ["Oyuncak bebeklere mahsus takma saç",
   "Oyuncak bebek figürü ile birleştirilmiş müzik kutusu",
   "Kukla tiyatrosu gösterilerinde kullanılmaya mahsus yapma bebek",
   "Salonları süslemek için kullanılan maskot bebek",
   "Yapma bebeklere mahsus ev ve mobilya"],
  "B", "Oyuncak bebek figürü ile birleştirilmiş müzik kutusu", FARKLI,
  "95.03 Açıklama Notu, oyuncak bebek figürü ile birleştirilmiş müzik kutularını 92.08’e gönderir. Takma saç bebek "
  "aksesuarı olarak; kukla ve maskot bebekler ile bebek evleri ve mobilyaları 95.03’te, yani 95. Fasıldadır.",
  "95.03 Açıklama Notu.", 95)

# 13 ─ Fasıl 90: eşya → pozisyon
Q("Tarife Cetveline göre, maden ocaklarında ve tünellerde hava cereyanının hızını ölçmede kullanılan, esas itibarıyla "
  "özel tipte bir vantilatör ile bir kadrandan oluşan anemometre hangi tarife pozisyonunda sınıflandırılır?",
  ["90.15", "90.25", "90.26", "90.27", "90.31"],
  "C", "90.26", ESYA,
  "90.15 Açıklama Notu rüzgâr hızını ölçen meteorolojik anemometreleri kapsar; madenlerde, tünellerde ve bacalarda "
  "hava akımının hızını ölçen vantilatörlü anemometreleri ise 90.26’ya gönderir. Termometre ve higrometreler 90.25’te, "
  "analiz cihazları 90.27’dedir.",
  "90.15 ve 90.26 Açıklama Notları.", 90)

# 14 ─ Fasıl 84: pozisyon → eşya
Q("Tarife Cetveline göre aşağıdakilerden hangisinde sayılanların tümü 84.36 pozisyonunda sınıflandırılır?",
  ["Bal presi – bal mumunu petek şekline sokmaya mahsus makine – yem karıştırıcısı",
   "Bal presi – balı petekten ayırmaya mahsus santrifüjlü cihaz – civciv büyütme cihazı",
   "Arı kovanı – yumurtaları muayeneye mahsus mekanik tertibatlı cihaz – kuluçka makinesi",
   "Ot kurutmaya mahsus cihaz – yem karıştırıcısı – çit teşkil eden çalıları kesen makine",
   "Civcivleri sayıp kutulara yerleştiren makine – civciv büyütme cihazı – bal presi"],
  "A", "Bal presi – bal mumunu petek şekline sokmaya mahsus makine – yem karıştırıcısı", POZESYA,
  "84.36 Açıklama Notu, arıcılıkta bal preslerini ve petek makinelerini, hayvan yemi hazırlamada yem karıştırıcılarını "
  "sayar. Bal santrifüjü 84.21’de, ot kurutucusu 84.19’da, civciv sayıp kutulayan makine 84.22’de; arı kovanı ise "
  "maddesine göre (genellikle 44.21) sınıflandırılır.",
  "84.36 Açıklama Notu.", 84)

# 15 ─ GYK 1 (fasıl notu)
Q("Yağ çıkarılmasında kullanılacak taze zeytinler, yağlı meyve olmalarına rağmen 12.07 pozisyonunda değil 7. Fasılda "
  "sınıflandırılır. Bu sonuç hangi Genel Yorum Kuralının gereğidir?",
  ["GYK 2(b)", "GYK 3(a)", "GYK 3(c)", "GYK 4", "GYK 1"],
  "E", "GYK 1", GYK,
  "Fasıl 12 Not 1, 12.07 pozisyonunun zeytinlere uygulanmayacağını açıkça hükme bağlar. Sınıflandırma pozisyon "
  "metinleri ve fasıl notlarına göre yapıldığından dayanak GYK 1’dir; not yeterli olduğundan 2–4 numaralı kurallara "
  "başvurulmaz.",
  "GYK 1; Fasıl 12 Not 1.", "GYK")

# 16 ─ Fasıl 91: çoktan-çoğa
Q("Tarife Cetveline göre aşağıdakilerden hangileri 91.05 pozisyonunda sınıflandırılır?"
  "<br/>I. Rasathanelerde kullanılan astronomi saati"
  "<br/>II. Güverte saati"
  "<br/>III. Mutat saat kadranlı stadyum saati"
  "<br/>IV. Gemilerin kontrol panellerine monte edilmek üzere özel olarak imal edilmiş saat",
  ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "III ve IV"],
  "B", "I ve III", COKTAN,
  "91.05 Açıklama Notu rasathane ve astronomi saatlerini sayar; 91.06 Açıklama Notu da mutat kadranlı stadyum "
  "saatlerini 91.05’e gönderir. Güverte saatleri 91.01 veya 91.02’de, taşıt ve gemi kontrol panellerine mahsus "
  "saatler 91.04’tedir.",
  "91.02, 91.04, 91.05 ve 91.06 Açıklama Notları.", 91)

# 17 ─ Fasıl 83: fasıl notu / eşik
Q("Fasıl 83 Not 2 ve 83.02 Açıklama Notuna göre adi metal donanımlı küçük tekerlekler (castors) ile ilgili "
  "aşağıdakilerden hangisi <b>yanlıştır</b>?",
  ["Çapı (takılabilecek bandaj dahil) 75 mm’yi geçmeyen tekerlekler, genişliklerine bakılmaksızın küçük tekerlek sayılır.",
   "Çapı 75 mm’yi geçen bir tekerleğin küçük tekerlek sayılması için tekerlek veya bandaj genişliğinin 30 mm’den az olması gerekir.",
   "Pnömatik lastikli küçük tekerleklerin çapı, normal basınçta şişirilmiş lastiğiyle birlikte ölçülür.",
   "Donanımın adi metalden olması şarttır; tekerleğin kendisi kıymetli metal dışında herhangi bir maddeden olabilir.",
   "Not 2’deki ölçü şartlarını karşılamayan tekerlekler, donanımları adi metalden olduğu sürece yine 83.02’de sınıflandırılır."],
  "E", "Not 2’deki ölçü şartlarını karşılamayan tekerlekler, donanımları adi metalden olduğu sürece yine 83.02’de sınıflandırılır.",
  TANIM,
  "83.02 Açıklama Notuna göre pozisyon metnindeki veya Not 2’deki koşullara uymayan küçük tekerlekler bu pozisyon "
  "dışında kalır (örneğin Fasıl 87). Diğer ifadeler 75 mm/30 mm ölçütünü, pnömatik lastik ölçümünü ve madde kuralını "
  "doğru yansıtır.",
  "Fasıl 83 Not 2; 83.02 Açıklama Notu.", 83)

# 18 ─ Fasıl 31: fasıl notu / eşik
Q("Fasıl 31 Not 3’e göre; 31.05’te belirtilen tablet vb. şekillerde veya brüt ağırlığı 10 kg’ı geçmeyen ambalajlarda "
  "olmaksızın dökme halde sunulan, kuru anhidrit ürün üzerinden ağırlıkça %0,1 flor içeren kalsiyum "
  "hidrojenortofosfat ile tek süperfosfatın karışımından oluşan gübre için aşağıdakilerden hangisi <b>doğrudur</b>?",
  ["Flor oranı %0,2’nin altında kaldığından karışım 28.35’te sınıflandırılır.",
   "Fosfordan başka gübreleyici unsur içermese de karışım olduğu için 31.05’te sınıflandırılır.",
   "Bu tür karışımlarda flor miktar limiti dikkate alınmadığından 31.03’te sınıflandırılır.",
   "Kimyasal olarak belirli bir bileşik içerdiğinden Fasıl 31 Not 1 gereği 38.24’te sınıflandırılır.",
   "Ancak kalsiyum hidrojenortofosfatın flor oranı %0,2 veya daha fazla olursa 31.03’te, aksi halde 31.04’te sınıflandırılır."],
  "C", "Bu tür karışımlarda flor miktar limiti dikkate alınmadığından 31.03’te sınıflandırılır.", TANIM,
  "Not 3(a), kalsiyum hidrojenortofosfatı tek başına ancak %0,2 veya daha fazla flor içerirse 31.03’e alır; Not 3(b) "
  "ise (a) fıkrasındaki ürünlerin birbirleriyle karışımlarında flor miktar limitinin dikkate alınmayacağını belirtir. "
  "Karışım 31.03’tedir.",
  "Fasıl 31 Not 3(a)(iv), 3(b).", 31)

# 19 ─ GYK 6
Q("08.02 pozisyonunda yer aldığı belirlenen kabuksuz kestanenin, önce aynı seviyedeki tek tireli alt pozisyonlar "
  "karşılaştırılarak “Kestane” alt pozisyonunun, ardından bunun altındaki iki tireli “Kabuksuz” alt pozisyonunun "
  "seçilmesi hangi Genel Yorum Kuralının gereğidir?",
  ["GYK 6", "GYK 1", "GYK 3(a)", "GYK 3(c)", "GYK 4"],
  "A", "GYK 6", GYK,
  "GYK 6, alt pozisyonlarda sınıflandırmanın yalnızca aynı seviyedeki (tek tireli veya iki tireli) alt pozisyonlar "
  "karşılaştırılarak yapılacağını öngörür. Dört rakamlı pozisyon GYK 1 ile bulunduktan sonra alt pozisyon seçimi "
  "GYK 6’ya dayanır.",
  "GYK 6 ve Açıklama Notu.", "GYK")

# 20 ─ GYK 2(a): eksik ve demonte makine
Q("Metal işlemeye mahsus bir torna tezgâhının, yalnızca alet tutucusu bulunmayan ancak tamamlanmış tezgâhın asli "
  "niteliklerine sahip olan bütün parçaları aynı sevkiyatta demonte halde gümrüğe sunulmuştur. Bu eşya hangi yorum "
  "kurallarına göre hangi pozisyonda sınıflandırılır?",
  ["84.66 – GYK 1 ve 6", "84.58 – GYK 1, 3(b) ve 6", "84.59 – GYK 1, 2(a) ve 6",
   "84.58 – GYK 1, 2(a) ve 6", "84.66 – GYK 1, 2(b) ve 6"],
  "D", "84.58 – GYK 1, 2(a) ve 6", GYK,
  "GYK 2(a), asli niteliği taşıyan eksik eşyayı ve bunun demonte halini tamamlanmış eşya gibi sınıflandırır; Bölüm "
  "XVI Genel Açıklamaları da alet tutacağı noksan makineyi tam makineyle aynı pozisyona koyar. Parçalar 84.66’ya "
  "gitmez; torna tezgâhları 84.58’dedir.",
  "GYK 1, 2(a), 6; Bölüm XVI Genel Açıklamalar (IV), (V).", "GYK")


if __name__ == "__main__":
    from collections import Counter
    assert len(S) == 20, len(S)
    c = Counter(q["cevap"] for q in S)
    assert all(c[L] == 4 for L in "ABCDE"), c
    for i, q in enumerate(S, 1):
        n = len(q["gerekce"].split())
        if n > 45 or len(q["gerekce"]) > 420:
            print(f"UYARI soru {i}: gerekçe {n} kelime / {len(q['gerekce'])} karakter")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"tur": "karma", "no": 7, "sorular": S}, f, ensure_ascii=False, indent=1)
    print("yazıldı:", OUT, dict(c), "".join(q["cevap"] for q in S))
