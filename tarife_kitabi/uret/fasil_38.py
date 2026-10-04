#!/usr/bin/env python3
# Fasıl 38 modülü üreteci
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
Q(E4, "Tarife Cetveline göre, domuz yağı ve kullanılmış kızartma yağlarından transesterifikasyon yoluyla elde edilen, yakıt olarak kullanılan ve hiç petrol yağı içermeyen yağ asidi mono alkil esterleri (biyodizel) hangi pozisyonda sınıflandırılır?",
  ["27.10", "15.18", "38.26", "29.15", "38.23"], "38.26",
  "Fasıl 38 Not 7, hayvansal, bitkisel veya mikrobiyal yağlardan (kullanılmış olsun olmasın) elde edilen ve yakıt olarak kullanılan yağ asitlerinin mono alkil esterlerini biyodizel olarak tanımlar; bunlar 38.26’dadır. Ağırlıkça %70 veya daha fazla petrol yağı içeren karışımlar ile tamamen deoksijene edilmiş bitkisel yağ ürünleri 27.10’a gider.",
  "Fasıl 38 Not 7; 38.26 Açıklama Notu.")

# 2
Q(E4, "Yağı alınmış kemiklerin kapalı bir kap içinde kalsine edilmesiyle elde edilen, şeker sanayiinde renk giderici olarak kullanılan siyah, gözenekli kemik karası hangi pozisyonda yer alır?",
  ["38.02", "05.06", "38.01", "28.03", "38.25"], "38.02",
  "38.02 pozisyon metni hayvansal karaları (kullanılmış ve tesiri kalmamış olanlar dahil) kapsar; Açıklama Notu kemik karasını, kan karasını ve fildişi karasını örnek verir. İşlenmemiş kemikler Fasıl 5’te, suni grafit 38.01’de kalır; kemik karasının kullanılmış olması da onu atık pozisyonuna (38.25) götürmez.",
  "38.02 pozisyon metni ve Açıklama Notu (Hayvansal karalar).")

# 3
Q(E4, "Güvelere karşı kullanılmak üzere yuvarlak toplar halinde şekillendirilip perakende satış için kutulara konulmuş naftalen hangi tarife pozisyonunda sınıflandırılır?",
  ["29.02", "38.08", "27.07", "33.07", "38.24"], "38.08",
  "38.08 Açıklama Notuna göre karışım halinde olmayan ürünler de haşarat öldürücü olarak perakende satışa elverişli ambalajlarda veya perakende satılacağına şüphe bırakmayan şekillerde (toplar, tabletler vb.) ise bu pozisyondadır; naftalen bu bağlamda örnek olarak anılır. Dökme halde izole naftalen ise kimyasal olarak belirli bileşik olarak Fasıl 29’da kalır; Bölüm VI Not 2 de 38.08’e öncelik verir.",
  "38.08 Açıklama Notu (A) ve hariç (a)(4); Bölüm VI Not 2.")

# 4
Q(E4, "Glikol türevleri esaslı, araç radyatörlerinde soğutma suyunun donmasını önlemek için kullanılan müstahzar Tarife Cetvelinde hangi pozisyonda yer alır?",
  ["38.20", "38.19", "38.11", "29.05", "38.14"], "38.20",
  "38.20, donmayı önleyici müstahzarları ve donmayı çözücü müstahzar sıvıları (örneğin glikol türevleri esaslı karışımlar) kapsar; bazıları soğutucu veya ısı değiştirici olarak kullanılır. 38.19 hidrolik fren ve transmisyon sıvılarının, 38.11 mineral yağlar için katkıların yeridir; izole glikol ise Fasıl 29’dadır.",
  "38.20 Açıklama Notu.")

# 5
Q(E4, "Ham tall oilin damıtılmasıyla elde edilen, başlıca oleik ve linoleik asitten oluşan ve kuru madde üzerinden ağırlıkça %92 yağ asidi içeren tall oil yağ asitleri (TOFA) hangi pozisyonda sınıflandırılır?",
  ["38.23", "38.03", "38.06", "29.16", "38.07"], "38.23",
  "38.23 Açıklama Notu, ham tall oilin damıtılmasıyla elde edilen ve ağırlıkça %90 veya daha fazla yağ asidi içeren tall oil yağ asitlerini sınai monokarboksilik yağ asitleri arasında sayar; 38.03 Açıklama Notu da bunları hariç tutar. Ham veya rafine tall oil 38.03’te, tall oil reçine asitleri 38.06’da, sülfat zifti 38.07’dedir.",
  "38.23 Açıklama Notu (A)(3); 38.03 Açıklama Notu, hariç (e).")

# 6
Q(OT, "Aşağıdakilerden hangisi Tarife Cetvelinin 38. faslında <b>sınıflandırılmaz</b>?",
  ["Nükleer reaktörlerde moderatör olarak kullanılan suni grafit", "Su arıtmada kullanılan granül aktif kömür",
   "Tıbbi özelliğe sahip, ölçülü dozlarda tabletler halindeki aktif kömür", "Şeker sanayiinde kullanılan kemik karası",
   "Mineral yağ içinde kolloidal süspansiyon halinde grafit"],
  "Tıbbi özelliğe sahip, ölçülü dozlarda tabletler halindeki aktif kömür",
  "38.02 Açıklama Notu, ilaç özelliğine sahip aktif hale getirilmiş karbonları hariç tutarak 30.03 veya 30.04’e gönderir; ölçülü dozlardaki tablet 30.04’tedir. Nükleer suni grafit ve kolloidal grafit 38.01’de, su arıtma aktif kömürü ve kemik karası 38.02’dedir. Kolloidal grafitin yağ içinde olması onu yağlama müstahzarı (34.03) yapmaz.",
  "38.02 Açıklama Notu, hariç (c); 38.01 Açıklama Notu; Fasıl 38 Not 1(e).")

# 7
Q(OT, "Aşağıdakilerden hangisi 38.08 pozisyonunda <b>yer almaz</b>?",
  ["Öğütülmüş piretrum çiçekleri", "Zehirli madde içermeyen, yapışkanlı sinek kağıdı", "Zehirli maddeyle karıştırılmış buğday tanelerinden oluşan kemirgen yemi",
   "Tekne ve sarnıçların dezenfeksiyonunda kullanılan kükürtlü fitil", "Perakende ambalajda, dezenfekte edici özellikli kuaterner amonyum tuzu müstahzarı"],
  "Öğütülmüş piretrum çiçekleri",
  "38.08 Açıklama Notu, tanımlara uymayan ürünler arasında öğütülmüş piretrum çiçeklerini sayar ve 12.11’e gönderir (piretrum hülasası 13.02’dedir). Zehir içermeyenler dahil sinek kağıtları, zehirli yemler, kükürtlü fitiller ve perakende ambalajdaki katyonik dezenfektanlar 38.08’de açıkça sayılmıştır.",
  "38.08 pozisyon metni ve Açıklama Notu, hariç (a)(1).")

# 8
Q(OT, "Aşağıdakilerden hangisi 38.24 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Seramik fırınlarının ısısını kontrol etmeye yarayan Seger konileri", "Perakende satış için küçük şişelere konulmuş düzeltme sıvısı",
   "Her biri 3 g ağırlığında, optik eleman olmayan potasyum bromür kültür kristalleri", "Oksalik asit esteri ile hidrojen peroksit reaksiyonuyla ışık veren aydınlatma çubuğu",
   "Her biri 1 g ağırlığında, optik eleman olmayan sodyum klorür kültür kristalleri"],
  "Her biri 1 g ağırlığında, optik eleman olmayan sodyum klorür kültür kristalleri",
  "Fasıl 38 Not 3(a), alkali veya toprak alkali metal halojenürlerinden her birinin ağırlığı 2,5 g’dan az olmayan kültür kristallerini 38.24’e alır. Açıklama Notuna göre 2,5 g’dan hafif olanlar hale göre Fasıl 28’de veya sodyum klorür kristalleri ise 25.01’de yer alır. Seger konileri, perakende düzeltme sıvıları ve kimyasal ışık çubukları 38.24’tedir.",
  "Fasıl 38 Not 3(a), (d), (e); 38.24 Açıklama Notu.")

# 9
Q(OT, "Aşağıdakilerden hangisi 38.25 pozisyonu kapsamında <b>değildir</b>?",
  ["Esas olarak petrol yağları içeren atıklar", "Kullanılmış eldiven ve şırınga gibi kontamine klinik atıklar", "Arıtma tesisinden elde edilen, stabilize edilmemiş kanalizasyon çamuru",
   "Temizleme işlemlerinden kalan, birincil ürün olarak kullanılamayan atık organik çözücüler",
   "Evlerden ve ofislerden toplanan karışık şehir atıkları"],
  "Esas olarak petrol yağları içeren atıklar",
  "Fasıl 38 Not 6, “diğer atıklar” tabirinin esas olarak petrol yağları veya bitümenli minerallerden elde edilen yağları içeren atıkları kapsamadığını belirtir; bunlar 27.10’dadır. Klinik atıklar, atık organik çözücüler, stabilize edilmemiş kanalizasyon çamuru ve karışık şehir atıkları 38.25’tedir.",
  "Fasıl 38 Not 4, 5 ve 6.")

# 10
Q(FA, "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
  ["Odun katranı", "Odun kreozotu", "Mineral kreozot (kreozot yağı)", "Yaklaşık %80 metanol ve %15 aseton içeren odun naftası", "Tall oilin damıtılmasından kalan sülfat zifti"],
  "Mineral kreozot (kreozot yağı)",
  "Odun katranı, odun kreozotu, odun naftası ve sülfat zifti (bitkisel zift) 38.07’dedir. 38.07 Açıklama Notu odun kreozotunun 27.07’deki kreozot yağları veya mineral kreozotla karıştırılmaması gerektiğini vurgular; mineral kreozot 27.07’dedir.",
  "38.07 Açıklama Notu (A), (B), (C).")

# 11
Q(FA, "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  ["Ham tall oil", "Çam iğnesi (yaprağı) esansı", "Kolofan", "Terebentin esansı", "Odun hamuru imalinden arta kalan lignin sülfonatlar"],
  "Çam iğnesi (yaprağı) esansı",
  "Tall oil (38.03), lignin sülfonatlar (38.04), terebentin esansı (38.05) ve kolofan (38.06) Fasıl 38’dedir. 38.05 Açıklama Notu ise bir uçucu yağ olan çam iğnesi (yaprağı) esansını hariç tutarak 33.01’e gönderir.",
  "38.05 Açıklama Notu, hariç (b).")

# 12
Q(FA, "Aşağıdaki eşya ikililerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
  ["Yangın söndürme cihazına bulunduğu şekilde yerleştirilecek dolgu kartuşu – doldurulmuş yangın söndürme cihazı",
   "Bor ile dope edilmiş, disk şeklinde silikon – selektif difüzyon işlemi görmüş yarı iletken",
   "Agar-agar – agar-agar esaslı müstahzar kültür ortamı",
   "Suda çözünmeyen petrol sülfonatları – kalsiyum naftenat",
   "Laboratuvar reaktifi haline getirilmiş sodalı kireç – anestezi sistemlerinde kullanılan sodalı kireç"],
  "Suda çözünmeyen petrol sülfonatları – kalsiyum naftenat",
  "Suda çözünmeyen petrol sülfonatları ve naftenik asit tuzları (kalsiyum naftenat gibi) 38.24 Açıklama Notunda birlikte sayılır. Diğer ikililer ayrılır: dolgu 38.13 / cihaz 84.24; dope disk 38.18 / işlenmiş yarı iletken 85.41; agar-agar 13.02 / kültür ortamı 38.21; reaktif sodalı kireç 38.22 / sodalı kireç 38.24.",
  "38.24 Açıklama Notu; 38.13, 38.18 ve 38.21 Açıklama Notları.")

# 13
Q(FA, "Aşağıdaki ürünlerin hepsi ağırlıkça %75 petrol yağı içermektedir. Hangisi diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  ["Transmisyon kayışlarının kaymasını önleyici müstahzar", "Esas bileşeni dietil eter olan, benzinli motorlar için ilk ateşleme sıvısı",
   "Hidrolik fren sıvısı", "Makine parçalarının yağını temizlemeye mahsus organik karma çözücü",
   "Benzin içinde çözünmüş ksilen ve klorlu çözücülerden oluşan boya inceltici"],
  "Hidrolik fren sıvısı",
  "38.19 yalnızca petrol yağı içermeyen veya ağırlıkça %70’ten az içeren hidrolik sıvıları kapsar; %75 petrol yağlı fren sıvısı 27.10’a (Fasıl 27) gider. Buna karşılık 38.24 Açıklama Notu kayış kaymazlık müstahzarlarını ve ilk ateşleme sıvılarını %70 veya fazla petrol yağı içerseler de kapsar; 38.14 de organik çözücü ve incelticileri petrol yağı oranından bağımsız olarak kapsar; bu nedenle diğer dört ürün Fasıl 38’de kalır.",
  "38.19 pozisyon metni ve Açıklama Notu; 38.14 Açıklama Notu; 38.24 Açıklama Notu.")

# 14
Q(FN, "Fasıl 38 Not 2’ye göre “sertifikalı referans maddeler” ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
  ["Sertifika şartı aranmaz; tahlilde kullanılan her madde sertifikalı referans maddedir.",
   "Sertifikalı referans maddeler, Fasıl 28 ve 29 ürünleri hariç, Tarife Cetvelindeki diğer tüm pozisyonlara göre 38.22’de öncelikle sınıflandırılır.",
   "Sertifikalı referans maddeler, kimyasal olarak belirli olsalar dahi her durumda 38.22’de sınıflandırılır.",
   "Sertifikalı referans maddeler 38.24’te sınıflandırılır.",
   "Sertifikanın yalnızca üretici adını göstermesi yeterlidir."],
  "Sertifikalı referans maddeler, Fasıl 28 ve 29 ürünleri hariç, Tarife Cetvelindeki diğer tüm pozisyonlara göre 38.22’de öncelikle sınıflandırılır.",
  "Not 2’ye göre sertifikalı referans maddeler, onaylanmış özelliklerin değerlerini, bu değerlerin belirlenme yöntemlerini ve her değerin kesinlik derecesini gösteren bir sertifikanın eşlik ettiği, tahlil, ölçme veya referans amaçlarına uygun maddelerdir. Bunlarda 38.22, Fasıl 28 ve 29’daki ürünler hariç diğer tüm pozisyonlara göre öncelik alır.",
  "Fasıl 38 Not 2; 38.22 Açıklama Notu.")

# 15
Q(FN, "Fasıl 38 Not 3’e göre magnezyum oksidin veya alkali ya da toprak alkali metallerin halojenürlerinden meydana gelen kültür kristallerinin (optik elemanlar hariç) 38.24’te yer alabilmesi için her birinin ağırlığı en az ne olmalıdır?",
  ["1 gram", "2 gram", "5 gram", "2,5 gram", "10 gram"], "2,5 gram",
  "Not 3(a), her birinin ağırlığı 2,5 gramdan az olmayan kültür kristallerini 38.24’e alır. Daha hafif olanlar hale göre Fasıl 28’de, sodyum klorür kristalleri 25.01’de, potasyum klorür kristalleri 31.04’te kalır; optik eleman haline getirilmiş kristaller ise 90.01’dedir.",
  "Fasıl 38 Not 3(a); 38.24 Açıklama Notu.")

# 16
Q(FN, "Fasıl 38 Not 7 ve 38.26 Açıklama Notuna göre biyodizel ile ilgili aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
  ["Biyodizel, yakıt olarak kullanılan yağ asitlerinin mono alkil esterleridir.",
   "Kullanılmış kızartma yağlarından elde edilen ürün de biyodizel tanımına girer.",
   "Ağırlıkça %70’ten az petrol yağı içeren biyodizel karışımları 38.26’da kalır.",
   "Ağırlıkça %70 veya daha fazla petrol yağı içeren biyodizel karışımları 38.26’da yer alır.",
   "Tamamen deoksijene edilmiş, yalnızca alifatik hidrokarbon zincirlerinden oluşan bitkisel yağ ürünleri 38.26’da yer almaz."],
  "Ağırlıkça %70 veya daha fazla petrol yağı içeren biyodizel karışımları 38.26’da yer alır.",
  "38.26 Açıklama Notu, ağırlıkça %70 veya daha fazla petrol yağı içeren karışımları ve tamamen deoksijene edilmiş bitkisel yağ ürünlerini hariç tutarak 27.10’a gönderir. Not 7’ye göre biyodizel, hayvansal, bitkisel veya mikrobiyal yağlardan (kullanılmış olsun olmasın) elde edilen yağ asidi mono alkil esterleridir.",
  "Fasıl 38 Not 7; 38.26 Açıklama Notu, hariç tutmalar.")

# 17
Q(FN, "Fasıl 38 Not 1(a), kimyasal olarak belirli yapıdaki izole element ve bileşikleri fasıl dışında bırakır. Aşağıdakilerden hangisi bu kuralın istisnası olarak Fasıl 38’de yer alabilen ürünlerden <b>değildir</b>?",
  ["Suni grafit", "38.08’de belirtilen şekillerde perakende satışa hazırlanmış haşarat öldürücüler",
   "Yangın söndürme bombalarına konulmuş söndürücü maddeler", "Sertifikalı referans maddeler",
   "Plastifiyan olarak kullanılan, kimyasal olarak belirli dioktil fitalat"],
  "Plastifiyan olarak kullanılan, kimyasal olarak belirli dioktil fitalat",
  "Not 1(a)’nın istisnaları suni grafit (38.01), 38.08 şekillerindeki ürünler, 38.13’teki söndürücü maddeler, sertifikalı referans maddeler ve Not 3(a) ile 3(c)’deki ürünlerdir. Dioktil fitalat bu listede yoktur; 38.12 Açıklama Notu da kimyasal olarak belirli dioktil fitalatı Fasıl 29’a gönderir.",
  "Fasıl 38 Not 1(a); 38.12 Açıklama Notu, hariç (b).")

# 18
Q(GYK, "Yangın söndürme cihazlarına bulunduğu şekilde yerleştirilmek üzere kaplara konulmuş, bromoklorodiflorometan ile bromotriflorometan karışımından oluşan söndürücü dolgu, hem 38.13 hem de 38.27 tanımına uymaktadır. Bu eşya 38.13’te sınıflandırılır. Bu sonuca hangi kurala göre ulaşılır?",
  ["GYK 3(a)", "GYK 3(b)", "GYK 3(c)", "GYK 4", "GYK 1"], "GYK 1",
  "Bölüm VI Not 4’e göre bir eşya ismen veya işlevi itibarıyla Bölüm VI’daki bir pozisyona ve ayrıca 38.27’ye uyuyorsa, ismi veya işlevine uygun pozisyonda sınıflandırılır. Sonuç bir bölüm notundan doğduğu için GYK 1 uygulanır; “numara sırasına göre sonuncusu” olan GYK 3(c) ile 38.27’yi seçmek tuzaktır.",
  "Bölüm VI Not 4; GYK 1; 38.13 Açıklama Notu (B).")

# 19
Q(GYK, "GYK 5(b) ve Açıklama Notuna göre, aşağıdaki Fasıl 38 eşyasının hangisinde içinde bulunduğu kap eşyayla birlikte <b>sınıflandırılmaz</b>?",
  ["Perakende satış için karton kutuya konulmuş haşarat öldürücü tabletler", "Laboratuvar reaktifinin konulduğu küçük cam şişe",
   "Antifriz müstahzarının satıldığı tek kullanımlık plastik bidon", "Düzeltme sıvısının satıldığı fırçalı kapaklı küçük şişe",
   "Sıkıştırılmış gaz karışımının konulduğu, tekrar kullanıma elverişli çelik tüp"],
  "Sıkıştırılmış gaz karışımının konulduğu, tekrar kullanıma elverişli çelik tüp",
  "GYK 5(b), eşyayla birlikte sunulan ve normal olarak o eşyanın ambalajında kullanılan ambalaj maddelerini eşyayla birlikte sınıflandırır; ancak tekrar kullanıma elverişli olduğu açıkça belli olan ambalajlara uygulanmaz. Açıklama Notu, sıkıştırılmış veya likit gazlar için demir ve çelikten bazı kapları bu istisnaya örnek verir.",
  "GYK 5(b) ve Açıklama Notu (IV).")

# 20
Q(ES, "Aşağıdaki cümlede boş bırakılan yerlere sırasıyla hangisi gelmelidir? “Hidrolik fren sıvıları, petrol yağı veya bitümenli minerallerden elde edilen yağ oranı ağırlıkça ..... ise 38.19’da yer alır; organik karma çözücüler ve incelticiler ise petrol yağı oranından ..... 38.14’te yer alır.”",
  ["%70 veya daha fazla – bağımsız olarak", "%50’den az – bağımsız olarak", "%70’ten az – %70’ten az olmak şartıyla",
   "%70’ten az – bağımsız olarak", "%85’ten az – %70’ten az olmak şartıyla"],
  "%70’ten az – bağımsız olarak",
  "38.19 pozisyon metni, petrol yağı içermeyen veya ağırlıkça %70’ten az içeren müstahzar hidrolik sıvıları kapsar; %70 veya fazlası 27.10’dadır. 38.14 Açıklama Notu ise organik çözücü ve incelticileri “ağırlık itibarıyla %70 veya daha fazla petrol yağı içersin içermesin” kapsar.",
  "38.19 pozisyon metni; 38.14 Açıklama Notu.")

# 21
Q(ES, "Çam ve iğne yapraklı ağaçlardan elde edilen aşağıdaki ürünler ile pozisyonları eşleştirildiğinde hangi seçenek doğru olur? I. Odun hamuru imalinden arta kalan lignin sülfonatlar; II. Terebentin esansı; III. Kolofan; IV. Bira fıçılarının kaplanmasında kullanılan biracı zifti. — a. 38.06 · b. 38.04 · c. 38.07 · d. 38.05",
  ["I-d, II-b, III-a, IV-c", "I-b, II-a, III-d, IV-c", "I-b, II-d, III-c, IV-a", "I-c, II-d, III-a, IV-b", "I-b, II-d, III-a, IV-c"],
  "I-b, II-d, III-a, IV-c",
  "Lignin sülfonatlar dahil odun hamuru lesivleri 38.04’te, terebentin esansı 38.05’te, kolofan 38.06’da, esası kolofan veya bitkisel zift olan biracı ziftleri 38.07’dedir. Bu grup tall oil (38.03) ile birlikte fasıldaki “çam ağacı ürünleri” dizisini oluşturur.",
  "38.04, 38.05, 38.06 ve 38.07 pozisyon metinleri.")

# 22
Q(CC, "38.23 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Ticari stearik asit (stearin) 38.23’te yer alır. II. Kuru madde üzerinden %87 saflıkta oleik asit 38.23’te yer alır. III. Ham yağların rafinasyonu sırasında elde edilen rafinaj mahsulü asit yağları 38.23’tedir. IV. Kuru madde üzerinden %95 saflıkta, kimyasal olarak belirli yağ alkolleri 38.23’tedir.",
  ["I ve II", "I ve III", "II ve IV", "I, II ve III", "I, III ve IV"], "I ve III",
  "Ticari stearik asit ve rafinaj mahsulü asit yağları 38.23’te sayılmıştır (I, III doğru). Açıklama Notu %85 veya daha fazla saflıktaki oleik asidi 29.16’ya (II yanlış), %90 veya daha fazla saflıktaki kimyasal olarak belirli yağ alkollerini genellikle 29.05’e gönderir (IV yanlış).",
  "38.23 Açıklama Notu ve hariç tutmalar.")

# 23
Q(CC, "Fasıl 38 Not 4, 5 ve 6 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Şehir atıklarından ayrılarak ayrı toplanmış plastik atıklar şehir atığı olarak 38.25’te yer alır. II. Gübre olarak kullanılmaya uygun stabilize edilmiş kanalizasyon çamuru 38.25’tedir. III. Kullanılmış eldiven ve şırınga gibi kontamine klinik atıklar 38.25’tedir. IV. Esas olarak petrol yağı içermeyen fren ve antifriz sıvısı atıkları 38.25’tedir.",
  ["I ve II", "II ve III", "III ve IV", "I, III ve IV", "Yalnız III"], "III ve IV",
  "Not 6, klinik atıkları ve metal temizleme, hidrolik, fren ve antifriz sıvılarının atıklarını “diğer atıklar” arasında sayar (III, IV doğru). Not 4’e göre atıklardan ayrılan tek madde ve eşyalar kendi pozisyonlarına gider (I yanlış); Not 5’e göre gübre olarak kullanılmaya uygun stabilize çamur Fasıl 31’dedir (II yanlış).",
  "Fasıl 38 Not 4, 5 ve 6.")

# 24
Q(SN, "Milyonda bir oranında bor ile dope edilmiş, disk (wafer) şeklinde kesilmiş, parlatılmış ve yeknesak epitaksiyel tabakayla kaplanmış, ancak selektif difüzyon gibi daha ileri bir işlem görmemiş, elektronikte kullanılacak silikon hangi tarife pozisyonunda sınıflandırılır?",
  ["85.41", "38.18", "28.04", "38.24", "85.42"], "38.18",
  "38.18, elektronikte kullanılmak üzere disk, pul veya benzeri şekillerde dope edilmiş kimyasal elementleri kapsar; Açıklama Notu parlatılmış veya epitaksiyel tabakayla kaplanmış olanları da dahil eder. Çekilmiş işlenmemiş halde veya silindir/çubuk halinde olsaydı Fasıl 28’de kalırdı; selektif difüzyon gibi ileri işlem görseydi yarı iletken olarak 85.41’e giderdi.",
  "38.18 pozisyon metni ve Açıklama Notu.")

# 25
Q(SN, "Laboratuvarda veya evde kandaki glukoz düzeyini ölçmek için kullanılan; reaktif emdirilmiş plastik şeritlerden oluşan, vücut dışında (in vitro) kullanılan ve hastaya uygulanmayan, perakende kutuda sunulan teşhis kiti hangi pozisyonda sınıflandırılır?",
  ["30.06", "30.04", "90.27", "38.22", "38.21"], "38.22",
  "38.22, bir mesnet üzerindeki ve kit şeklinde olsun olmasın laboratuvarda veya teşhiste kullanılan müstahzar reaktifleri kapsar; Açıklama Notu kandaki glukoz testi kitlerini örnek verir. Hastaya tatbik edilmek üzere tasarlanmış (in vivo) teşhis reaktifleri ise 30.06’dadır; 38.21 kültür ortamlarının yeridir.",
  "38.22 pozisyon metni ve Açıklama Notu.")

modul = {
    "tur": "fasil",
    "fasil": 38,
    "baslik": "Muhtelif kimyasal ürünler",
    "bolum": "VI",
    "oz": {
        "vurgu": "Fasıl 38, Bölüm VI’nın son ve en geniş fasıldır: kimyasal olarak belirli olmayan kimyasal ürünler, sanayi müstahzarları, karışımlar, atıklar ve yakıt nitelikli bazı ürünler burada toplanır. Temel test iki adımlıdır: Eşya kimyasal olarak belirli izole bir bileşik mi (o zaman Fasıl 28–29, beş istisna hariç)? Değilse, ismen veya işleviyle özel bir pozisyona (38.01–38.23, 38.25–38.27) uyuyor mu; uymuyorsa 38.24.",
        "maddeler": [
            "İzole bileşik istisnaları: suni grafit (38.01), perakende veya müstahzar halindeki 38.08 ürünleri, yangın söndürme dolguları (38.13), sertifikalı referans maddeler (38.22), Not 3(a)/(c) ürünleri (38.24).",
            "Gıda hazırlamada kullanılan besleyici karışımlar (21.06), ilaçlar (30.03/30.04), 24.04 ürünleri, metal içeren cüruf ve kül (26.20) ve kullanılmış katalizörler (26.20/71.12) fasıl dışıdır.",
            "Petrol yağı %70 eşiği üç farklı sonuç verir: fren sıvısı (38.19) ve biyodizel (38.26) için %70’ten az şart; çözücüler (38.14) ve bazı 38.24 ürünleri için oran önemsiz.",
            "Çam ağacı ürünleri 38.03–38.07 sırasıyla: tall oil, lesiv, terebentin, kolofan, odun katranı ve ziftler.",
            "38.25 atıkları, 38.26 biyodizeli, 38.27 halojenli metan/etan/propan türevi karışımlarını kapsar; 38.27 isim veya işlevle yer alan pozisyonlardan sonra gelir (Bölüm VI Not 4)."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Kimyasal olarak belirli izole element veya bileşik mi? (Not 1(a) istisnaları hariç)", "<b>Fasıl 28 / 29</b>"],
            ["2", "Gıda hazırlamada kullanılan besleyici karışım, ilaç, 24.04 ürünü, metal içeren cüruf/kül veya kullanılmış katalizör mü?", "<b>21.06</b> · <b>30.03/30.04</b> · <b>24.04</b> · <b>26.20</b> · <b>71.12</b>"],
            ["3", "Sertifikalı referans madde mi?", "<b>38.22</b> (Fasıl 28–29 dışında her pozisyona öncelikli)"],
            ["4", "Haşere, kemirgen, mantar, yabancı ot, dezenfektan ürünü; perakende veya müstahzar halinde mi?", "<b>38.08</b>"],
            ["5", "Atık mı? (şehir atığı, kanalizasyon çamuru, klinik atık, atık çözücü, kimya sanayii atığı)", "<b>38.25</b> (petrol yağı esaslı <b>27.10</b> · eczacılık atığı <b>30.06</b>)"],
            ["6", "Karbon veya çam ağacı kökenli mi? (grafit, aktif karbon, tall oil, lesiv, terebentin, kolofan, odun katranı)", "<b>38.01</b>–<b>38.07</b>"],
            ["7", "Belirli bir sanayi işlevi mi? (apre, dekapaj/lehim, yağ katkısı, kauçuk katkısı, söndürücü, çözücü, katalizör, ateşe dayanıklı harç, alkilbenzen, dope wafer, fren sıvısı, antifriz)", "<b>38.09</b>–<b>38.20</b>"],
            ["8", "Kültür ortamı, laboratuvar/teşhis reaktifi veya sınai yağ asidi/yağ alkolü mü?", "<b>38.21</b> / <b>38.22</b> / <b>38.23</b>"],
            ["9", "Biyodizel (petrol yağı %70’ten az) mi?", "<b>38.26</b> (%70 veya fazlası <b>27.10</b>)"],
            ["10", "Başka yerde yer almayan kimyasal ürün veya müstahzar mı?", "<b>38.24</b>; halojenli metan/etan/propan karışımı ise <b>38.27</b>*"]
        ],
        "dipnot": "* 38.27, eşya ismen veya işleviyle Bölüm VI’daki başka bir pozisyona uyuyorsa uygulanmaz (Bölüm VI Not 4)."
    },
    "pozisyon_haritasi": [
        ["38.01", "Suni grafit; kolloidal grafit; karbon patları", "Tabii grafit 25.04", "Elektrot patı, nükleer grafit"],
        ["38.02", "Aktif karbon; aktif mineraller; hayvansal karalar", "Yüzey yapısı işlemle değiştirilmiş", "Aktif kömür, kemik karası"],
        ["38.03", "Tall oil", "Kağıt hamuru yan ürünü; rafine olabilir", "Ham tall oil"],
        ["38.04", "Odun hamuru lesivleri", "Lignin sülfonatlar dahil", "Sülfit lesivi"],
        ["38.05", "Terebentin ve terpenik yağlar", "Ham dipenten, çam yağı", "Terebentin esansı"],
        ["38.06", "Kolofan, reçine asitleri ve türevleri", "Rezinatlar, ester sakızları", "Kolofan, kolofan yağı"],
        ["38.07", "Odun katranı, kreozot, nafta; bitkisel zift", "Odun kaynaklı; mineral değil", "Biracı zifti, kalafat zifti"],
        ["38.08", "Haşarat, mantar, ot öldürücüler; dezenfektanlar", "Perakende veya müstahzar", "Böcek spreyi, sinek kağıdı"],
        ["38.09", "Mensucat, kağıt, deri apre ve finisajı", "Başka yerde yer almayan", "Yumuşatıcı, mordan, haşıl"],
        ["38.10", "Metal dekapaj; lehim ve kaynak yardımcıları", "Metal + yardımcı madde", "Lehim pastası, flux"],
        ["38.11", "Mineral yağ ve yakıt katkıları", "Vuruntu önleyici, antioksidan", "Benzin katkısı"],
        ["38.12", "Kauçuk/plastik katkıları", "Hızlandırıcı, plastifiyan, stabilizatör", "Vulkanizasyon hızlandırıcı"],
        ["38.13", "Yangın söndürme dolguları ve bombaları", "Cihaz 84.24’te", "Söndürücü kartuş"],
        ["38.14", "Organik karma çözücü ve incelticiler", "Petrol yağı oranı önemsiz", "Tiner, boya sökücü"],
        ["38.15", "Reaksiyon başlatıcı ve katalizörler", "Takviye edilmiş katalizör", "Ziegler katalizörü"],
        ["38.16", "Ateşe dayanıklı çimento, harç, beton", "38.01 patları hariç", "Fırın astar harcı"],
        ["38.17", "Karışık alkil benzen ve alkil naftalenler", "27.07, 29.02 hariç", "Deterjan hammaddesi"],
        ["38.18", "Dope edilmiş element ve bileşikler", "Disk/wafer; ileri işlem 85.41", "Dope silikon wafer"],
        ["38.19", "Hidrolik fren ve transmisyon sıvıları", "Petrol yağı %70’ten az", "Glikol esaslı fren hidroliği"],
        ["38.20", "Donmayı önleyici ve çözücü sıvılar", "Glikol esaslı karışımlar", "Antifriz"],
        ["38.21", "Müstahzar kültür ortamları", "Hazırlanmış besiyeri", "Agar esaslı besiyeri"],
        ["38.22", "Laboratuvar/teşhis reaktifleri; referans maddeler", "In vitro; kit olabilir", "Gebelik testi, kan grubu reaktifi"],
        ["38.23", "Sınai yağ asitleri ve yağ alkolleri", "Saflık eşikleri altında", "Stearin, TOFA, setil alkol"],
        ["38.24", "Maça bağlayıcıları; b.y.y. kimyasal ürünler", "Artık pozisyon", "Beton katkısı, düzeltme sıvısı"],
        ["38.25", "Kimya sanayii artıkları; atıklar", "Not 4–6 tanımları", "Şehir atığı, klinik atık"],
        ["38.26", "Biyodizel ve karışımları", "Petrol yağı %70’ten az", "Yağ asidi metil esteri"],
        ["38.27", "Halojenli metan, etan, propan karışımları", "Başka yerde yer almayan", "Soğutucu gaz karışımı"]
    ],
    "notlar": [
        ["Bölüm VI Not 2", "Ölçülü dozlarda veya perakende satış için hazırlanmış olması nedeniyle 38.08’e giren ürünler, tarifenin başka pozisyonuna girmez."],
        ["Bölüm VI Not 4", "Bir eşya ismen veya işleviyle Bölüm VI’daki bir pozisyona ve ayrıca 38.27’ye uyuyorsa, ismi veya işlevine uygun pozisyonda sınıflandırılır; 38.27’de sınıflandırılmaz."],
        ["Fasıl 38 Not 1(a)", "Kimyasal olarak belirli izole element ve bileşikler fasıl dışıdır. <b>İstisnalar:</b> suni grafit (38.01); 38.08 şekillerindeki haşarat öldürücü, dezenfektan vb.; yangın söndürme cihazları için veya bombalara konulmuş söndürücüler (38.13); sertifikalı referans maddeler; Not 3(a) ve 3(c) ürünleri."],
        ["Fasıl 38 Not 1(b)–(f)", "Fasıl dışı: (b) insan gıdası hazırlamada kullanılan, kimyasal maddelerle gıda veya besleyici maddelerin karışımları (genellikle 21.06); (c) 24.04 ürünleri; (d) Fasıl 26 Not 3(a)/(b) şartlarına uyan metal veya arsenik içeren cüruf, kül ve artıklar (26.20); (e) ilaçlar (30.03, 30.04); (f) adi metal çıkarmada kullanılmış katalizörler (26.20), kıymetli metal kazanımı için kullanılmış katalizörler (71.12), metal veya alaşımlardan katalizörler (Bölüm XIV veya XV)."],
        ["Fasıl 38 Not 2", "“Sertifikalı referans maddeler”: onaylanmış özelliklerin değerlerini, yöntemleri ve her değerin kesinlik derecesini gösteren bir sertifikanın eşlik ettiği, tahlil, ölçme veya referans amaçlı maddeler. Bunlarda 38.22, <b>Fasıl 28 ve 29 hariç</b> diğer tüm pozisyonlara göre öncelik alır."],
        ["Fasıl 38 Not 3", "38.24 ayrıca şunları kapsar: (a) magnezyum oksit veya alkali/toprak alkali metal halojenürlerinden, her biri <b>2,5 g’dan az olmayan</b> kültür kristalleri (optik elemanlar hariç); (b) füzel yağı, Dippel yağı; (c) perakende mürekkep lekesi çıkarıcılar; (d) perakende stensil düzelticiler, düzeltme sıvıları ve şeritleri (96.12 hariç); (e) seramik fırınlarına mahsus eriyen ısı göstergeleri (Seger konileri)."],
        ["Fasıl 38 Not 4", "“Şehir atıkları”: evler, oteller, lokantalar, hastaneler, dükkânlar, ofislerden toplanan atıklar, yol ve kaldırım süprüntüleri, inşaat ve yıkım atıkları. Kapsamaz: atıklardan ayrılmış tek madde ve eşyalar (kendi pozisyonlarında), sanayi atıkları, eczacılık atıkları (Fasıl 30 Not 4(k)), klinik atıklar."],
        ["Fasıl 38 Not 5", "“Kanalizasyon çamuru”: şehir atıklarını arıtma tesislerinden elde edilen çamur; ön arıtma, kalbur döküntüleri ve stabilize edilmemiş çamur dahil. Gübre olarak kullanılmaya uygun stabilize çamur hariç (Fasıl 31)."],
        ["Fasıl 38 Not 6", "38.25’teki “diğer atıklar”: (a) klinik atıklar; (b) atık organik çözücüler; (c) metal temizleme, hidrolik, fren ve antifriz sıvılarının atıkları; (d) kimya sanayii atıkları. Esas olarak petrol yağı içeren atıklar hariç (27.10)."],
        ["Fasıl 38 Not 7", "“Biyodizel”: hayvansal, bitkisel veya mikrobiyal yağlardan (kullanılmış olsun olmasın) elde edilen, yakıt olarak kullanılan yağ asitlerinin mono alkil esterleri."],
        ["Genel Açıklamalar", "Not 1(b) bakımından besleyici maddenin karışımda önemsiz oranda bulunması onu fasıl dışına çıkarmaya yetmez; fasıl dışı kalan karışımlar insan gıdası hazırlamada kullanılan ve besleyici nitelikleriyle değerlendirilenlerdir."],
        ["38.01 Açıklama Notu", "Nükleer suni grafit: bor milyonda bir veya daha az, kül milyonda 20’yi geçmez. Hariç: tabii grafit (25.04), karni kömürü (27.04), işlenmiş suni grafit eşya (elektrik dışı 68.15, elektrik işleri 85.45), gümüş tozlu yarı mamuller (71.06)."],
        ["38.08 Açıklama Notu", "Ürünler perakende satışa elverişli ambalajda/şekilde veya müstahzar halinde olmalıdır; karışmamış ürünler dökme ise Fasıl 28–29’dadır. Hariç: öğütülmüş piretrum (12.11), piretrum hülasası (13.02), mineral kreozot (27.07), dezenfektan sabun (34.01), oda deodorantı (33.07), ilaçlar (30.03/30.04)."],
        ["38.14 Açıklama Notu", "Organik karma çözücü ve incelticiler, ağırlıkça %70 veya daha fazla petrol yağı içersin içermesin 38.14’tedir. Hariç: izole çözücüler (Fasıl 29), çözücü nafta (27.07), white spirit (27.10), terebentin (38.05), perakende tırnak cilası çıkarıcılar (33.04)."],
        ["38.19 ve 38.26 Açıklama Notları", "Hidrolik fren ve transmisyon sıvıları ile biyodizel ve karışımları, petrol yağı içermiyor veya ağırlıkça <b>%70’ten az</b> içeriyorsa 38.19 / 38.26’da; %70 veya fazlası 27.10’dadır. Tamamen deoksijene edilmiş bitkisel yağ ürünleri de 27.10’dadır."],
        ["38.22 Açıklama Notu", "Teşhis reaktifleri laboratuvarda (in vitro) kullanılır; hastaya tatbik edilen (in vivo) reaktifler 30.06’dadır. Kitler, ayrı sunulsa başka pozisyona girecek bileşenler içerse de buradadır."],
        ["38.23 Açıklama Notu", "Tall oil yağ asitleri en az %90 yağ asidi içerir. Hariç: %85 veya fazla saflıkta oleik asit (29.16), %90 veya fazla saflıkta diğer yağ asitleri (29.15, 29.16, 29.18), %90 veya fazla saflıkta yağ alkolleri (29.05)."],
        ["38.24 Açıklama Notu", "Dökümhane maça bağlayıcıları (dekstrin esaslılar 35.05), naftenatlar, metal karbür karışımları, beton katkıları, ateşe dayanıklı olmayan harçlar, sorbitol şurupları (D-glusitol kuru maddenin %60–80’i), petrol sülfonatları, kimyasal ışık çubukları, kayış kaymazlık müstahzarları ve ilk ateşleme sıvıları (≥ %70 petrol yağı olsa da). Civa bileşikleri 28.52’de, gıda geliştiricileri 21.06’da."]
    ],
    "sinir_komsulari": [
        ["Tabii grafit; işlenmiş suni grafit eşya", "25.04 / 68.15 / 85.45", "38.01 hariç tutmaları"],
        ["Tabii aktif mineral (Fuller toprağı); aktif alümin", "Fasıl 25 / 28.18", "38.02 hariç tutmaları"],
        ["Tıbbi aktif kömür; buzdolabı koku giderici (perakende)", "30.03–30.04 / 33.07", "38.02 hariç tutmaları"],
        ["Öğütülmüş piretrum çiçeği; piretrum hülasası", "12.11 / 13.02", "38.08 hariç tutmaları"],
        ["Dezenfektan sabun; oda deodorantı", "34.01 / 33.07", "Daha özel pozisyon"],
        ["Mineral kreozot (kreozot yağı)", "27.07", "Odun kreozotu 38.07’de"],
        ["Çam iğnesi esansı", "33.01", "Uçucu yağ; 38.05 değil"],
        ["Doldurulmuş veya boş yangın söndürme cihazı", "84.24", "Dolgusu 38.13’te"],
        ["Perakende tırnak cilası çıkarıcı; white spirit", "33.04 / 27.10", "38.14 hariç tutmaları"],
        ["Selektif difüzyon görmüş yarı iletken", "85.41", "Dope wafer 38.18’de"],
        ["≥ %70 petrol yağlı fren sıvısı ve biyodizel karışımı", "27.10", "38.19 ve 38.26 eşiği"],
        ["Agar-agar, pepton, jelatin (kültür ortamı olarak hazırlanmamış)", "13.02 / 35.04 / 35.03", "38.21 hariç tutmaları"],
        ["Hastaya tatbik edilen teşhis reaktifi", "30.06", "38.22 in vitro reaktifleri kapsar"],
        ["%85+ saf oleik asit; %90+ saf yağ alkolü", "29.16 / 29.05", "38.23 saflık eşikleri"],
        ["Miadı dolmuş ilaçlar (eczacılık atığı)", "30.06", "Fasıl 30 Not 4(k); şehir atığı değil"]
    ],
    "tuzaklar": [
        "<b>Fasıl 38 izole bileşiklerin çöplüğü değildir.</b> Kimyasal olarak belirli bileşik Fasıl 28–29’a gider; yalnızca Not 1(a)’daki beş istisna Fasıl 38’de kalır.",
        "<b>38.08 sunum şartı ister.</b> Dökme naftalen Fasıl 29; güve topu şeklinde perakende naftalen 38.08. Müstahzarlar ise her sunumda 38.08’dedir.",
        "<b>%70 kuralı üç farklı sonuç verir.</b> Fren sıvısı ve biyodizel %70’ten az petrol yağı şartıyla 38.19 / 38.26; çözücüler 38.14’te oran fark etmez; kayış kaymazlık müstahzarı ve ilk ateşleme sıvısı %70’i aşsa da 38.24.",
        "<b>Tall oil ailesi beş pozisyona dağılır.</b> Tall oil 38.03, siyah lesiv ve köpük 38.04, tall oil reçine asitleri 38.06, sülfat zifti 38.07, TOFA (en az %90 yağ asidi) 38.23; sabunlaştırılmış tall oil 34.01.",
        "<b>Odun kreozotu ≠ mineral kreozot.</b> Odun kreozotu 38.07; kreozot yağı (mineral) 27.07.",
        "<b>Grafitin yeri işlenme derecesine bağlıdır.</b> Tabii 25.04; suni ve kolloidal 38.01; kesilip işlenmiş eşya 68.15 veya 85.45.",
        "<b>Söndürücü dolgu ≠ söndürme cihazı.</b> Dolgu ve bombalar 38.13; doldurulmuş olsun olmasın cihaz 84.24.",
        "<b>In vitro 38.22, in vivo 30.06.</b> Sertifikalı referans madde ise Fasıl 28–29 dışındaki her pozisyona karşı 38.22’ye öncelik verir.",
        "<b>Kültür kristalinde 2,5 g sınırı.</b> 2,5 g ve üstü 38.24; daha hafif ise Fasıl 28, 25.01 veya 31.04; optik eleman 90.01.",
        "<b>38.27 en son bakılır.</b> İsmen veya işleviyle Bölüm VI’da başka pozisyona uyan halojenli karışım o pozisyonda kalır (Bölüm VI Not 4)."
    ],
    "hafiza": {
        "kanca": "KÖMÜR – ÇAM – BÖCEK – FABRİKA – LAB – YAĞ – TORBA – ÇÖP – BİYO – HALO",
        "aciklama": "<b>KÖMÜR</b> 38.01–38.02 (grafit, aktif karbon) · <b>ÇAM</b> 38.03–38.07 (tall oil, lesiv, terebentin, kolofan, katran) · <b>BÖCEK</b> 38.08 · <b>FABRİKA</b> 38.09–38.20 (apre, lehim, katkılar, söndürücü, çözücü, katalizör, ateş harcı, alkilbenzen, wafer, fren sıvısı, antifriz) · <b>LAB</b> 38.21–38.22 · <b>YAĞ</b> 38.23 · <b>TORBA</b> 38.24 (başka yerde yer almayan) · <b>ÇÖP</b> 38.25 · <b>BİYO</b>dizel 38.26 · <b>HALO</b>jenli karışım 38.27. Görsel benzetme: kömür ocağından çam ormanına geçin, böcek ilaçlayın, fabrikaya ve laboratuvara uğrayın, yağ deposunun yanındaki büyük torbaya kalanları atın; çöpü ayırın, aracı biyodizelle doldurun ve klima gazını en son kontrol edin."
    },
    "sinav_odagi": [
        "Sınai yağ alkollerinin 38.23’te yer aldığı; 15.18, 15.20, 29.34 ve 38.24’ün çeldirici olarak kullanıldığı pozisyon sorusu.",
        "Haşarat öldürücülerin (38.08) kimya sanayii ürünü olarak Bölüm VI’da, klinkerin ise Bölüm V’te yer aldığı “farklı bölümde sınıflandırılan eşya” sorusu.",
        "Miadı dolmuş hazır ilaçların atık pozisyonu 38.25’te değil, eczacılık ürünü olarak 30.06’da sınıflandırıldığı.",
        "Pozisyon sırası sorularında biyodizelin (38.26) ve ateşe dayanıklı çimentonun (38.16) yerinin bilinmesi.",
        "Yangın söndürme cihazının 84.24’te sınıflandırıldığı; söndürücü dolguların ise 38.13’te kaldığı ayrım.",
        "38.24’ün diğer fasılların sorularında (jelatin kapsül, ayakkabı boyası, kontak lens solüsyonu) sık kullanılan çeldirici olması; 38.14’ün polimer çözeltileri sorusunda 32.08’in yanında çeldirici olarak yer alması."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre sınai yağ alkolleri aşağıdaki tarife pozisyonlarından hangisinde yer alır?",
            "secenekler": ["15.18", "15.20", "29.34", "38.23", "38.24"],
            "cevap": "D",
            "aciklama": "38.23 pozisyon metni sınai yağ alkollerini ismen sayar; mumsu yapıdaki sınai yağ alkolleri de buradadır. Yalnızca %90 veya daha fazla saflıktaki kimyasal olarak belirli yağ alkolleri Fasıl 29’a (genellikle 29.05) gider."
        },
        {
            "soru": "Kullanım süresi bitmiş hazır ilaçların sınıflandırıldığı tarife pozisyonu nedir?",
            "secenekler": ["30.04", "30.06", "38.25", "39.15"],
            "cevap": "B",
            "aciklama": "Raf ömrü bittiği için amacına uygun kullanılamayan eczacılık ürünleri Fasıl 30 Not 4(k) uyarınca 30.06’dadır. Fasıl 38 Not 4 de eczacılık atıklarını şehir atığı tanımından çıkarır; bu nedenle 38.25 uygulanmaz."
        }
    ],
    "ozet": [
        "Önce izole bileşik testi: kimyasal olarak belirli ise Fasıl 28–29 (beş istisna: suni grafit, 38.08 ürünleri, söndürücüler, sertifikalı referans maddeler, Not 3(a)/(c)).",
        "Sıra: kömür 38.01–38.02 → çam ürünleri 38.03–38.07 → biyositler 38.08 → sanayi müstahzarları 38.09–38.20 → lab 38.21–38.22 → yağ asidi/alkolü 38.23.",
        "38.24 başka yerde yer almayan kimyasallar ve Not 3 ürünleri; 38.25 atıklar (petrol yağı esaslı atık 27.10).",
        "%70 petrol yağı: 38.19 ve 38.26 için “az olmalı”, 38.14 için önemsiz.",
        "38.22: in vitro reaktifler, kitler ve sertifikalı referans maddeler; in vivo reaktifler 30.06.",
        "38.27 halojenli metan/etan/propan karışımları için son durak; isim veya işlevle başka pozisyona uyan eşya orada kalır."
    ],
    "sorular": SORULAR
}

if __name__ == "__main__":
    print(Counter(q["cevap"] for q in SORULAR), len(SORULAR))
    print("".join(q["cevap"] for q in SORULAR))
    out = os.path.join(KITAP, "data", "fasil_38.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(modul, f, ensure_ascii=False, indent=1)
    print("yazıldı:", out)
