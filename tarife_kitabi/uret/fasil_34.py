#!/usr/bin/env python3
# Fasıl 34 modülü üreteci
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
Q(E4, "Tarife Cetveline göre, kimyasal yolla elde edilmiş, mum karakterinde olan, damlama noktası 40 °C’nin üzerinde bulunan ve ambalajlamada kullanılan polietilen mum hangi tarife pozisyonunda sınıflandırılır?",
 ["27.12", "39.01", "34.04", "15.21", "38.23"], "34.04",
 "Kimyasal yolla elde edilen mumsu karakterdeki organik ürünler Fasıl 34 Not 5(a) uyarınca suni mumdur; polialkilen (polietilen) mumlar 34.04 Açıklama Notunda örnek olarak sayılır. Mum karakterinde olmayan polietilen 39.01’e gider; 27.12 mineral mumların, 15.21 karıştırılmamış bitkisel/hayvansal mumların, 38.23 sınai yağ asitleri ve yağ alkollerinin yeridir.",
 "Fasıl 34 Not 5(a); 34.04 Açıklama Notu.")

# 2
Q(E4, "Aktif bileşeni sentetik organik yüzey aktif maddeler olan, sıvı halde ve perakende satılacak şekilde pompalı şişeye konulmuş, cildi yıkamaya mahsus el yıkama müstahzarı Tarife Cetvelinde hangi pozisyonda yer alır?",
 ["34.02", "34.01", "33.05", "33.07", "38.24"], "34.01",
 "34.01, cilt yıkamaya mahsus, sıvı veya krem halinde ve perakende satılacak hale getirilmiş yüzey aktif organik ürün ve müstahzarları (sabun içersin içermesin) ismen kapsar. Aynı müstahzar perakende satışa hazırlanmamış olsaydı 34.02’de yer alırdı; tuzak budur. 33.05 saç müstahzarlarının, 33.07 banyo ve traş müstahzarlarının pozisyonudur.",
 "34.01 pozisyon metni ve Açıklama Notu (III).")

# 3
Q(E4, "Ağırlık itibarıyla %60 mineral yağ, ayrıca hayvansal yağ ve yüzey aktif madde içeren, metal kesme tezgâhlarında kullanılan yağlama müstahzarı hangi tarife pozisyonunda sınıflandırılır?",
 ["34.03", "27.10", "34.02", "38.24", "15.18"], "34.03",
 "34.03, kesici aletleri yağlamaya mahsus müstahzarları kapsar; ancak esas madde olarak ağırlıkça %70 veya daha fazla petrol yağı içerenler hariçtir. Mineral yağ oranı %60 olduğundan eşya 34.03’te kalır; oran %70 veya daha fazla olsaydı 27.10 gündeme gelirdi. Doğrudan kesmede kullanılamayan, kesme yağı imaline mahsus yüzey aktif esaslı müstahzarlar ise 34.02’dedir.",
 "34.03 pozisyon metni ve Açıklama Notu (C); Fasıl 34 Not 4.")

# 4
Q(E4, "Mutfak lavabolarını ve çinileri ovmak için kullanılan, çok ince öğütülmüş kum, sodyum karbonat ve sabundan oluşan toz halindeki temizleme müstahzarı hangi pozisyonda sınıflandırılır?",
 ["34.01", "34.02", "25.13", "38.24", "34.05"], "34.05",
 "Aşındırıcı toz içeren ürünler Fasıl 34 Not 2 uyarınca yalnızca çubuk, topak veya kalıplanmış parça ve şekillerde iseler 34.01’e girer; diğer şekillerde “temizleme tozları ve benzeri müstahzarlar” olarak 34.05’te yer alır. 34.02, yüzey aktif madde içeren aşındırıcı müstahzarları açıkça hariç tutar; karıştırılmamış aşındırıcı tozlar ise Fasıl 25 veya 28’dedir.",
 "Fasıl 34 Not 2; 34.05 Açıklama Notu (4); 34.02 Açıklama Notu hariç (d).")

# 5
Q(E4, "Tarife Cetveline göre, çocukların eğlenmesi için hazırlanmış, farklı renklerde çubuklar halinde perakende kutuda sunulan model patı (oyun hamuru) takımı hangi pozisyonda yer alır?",
 ["34.07", "34.04", "32.13", "95.03", "38.24"], "34.07",
 "34.07 pozisyon metni “çocukların eğlenmesi için hazırlanan patlar dahil” model patlarını ismen kapsar; Açıklama Notu takım halinde olanların da burada kaldığını belirtir. Eşyanın oyuncak gibi kullanılması onu 95.03’e taşımaz; 34.04 suni ve müstahzar mumların, 32.13 sanatkâr boyalarının yeridir.",
 "34.07 pozisyon metni ve Açıklama Notu (A).")

# 6
Q(OT, "Aşağıdakilerden hangisi 34.01 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Kalıp halindeki traş sabunu", "Sabun emdirilmiş kağıt mendil", "Çubuk halinde, pomza tozu katılmış aşındırıcı sabun",
  "Siklohekzanol içinde hazırlanmış sabun çözeltisi", "Alkol ve gliserol ile işlenmiş yarı şeffaf gliserinli sabun"],
 "Siklohekzanol içinde hazırlanmış sabun çözeltisi",
 "Bir organik çözücü (siklohekzanol gibi) içindeki sabun solüsyonları veya dispersiyonları 34.01’den hariç tutulmuş ve yüzey aktif müstahzar olarak 34.02’de sayılmıştır. Su içindeki sabun çözeltileri ise sıvı sabun olarak 34.01’de kalır. Blok traş sabunu, sabun emdirilmiş kağıt, kalıp halindeki aşındırıcı sabun ve gliserinli sabun 34.01’dedir.",
 "34.01 Açıklama Notu hariç (e); 34.02 Açıklama Notu (II)(A)(4).")

# 7
Q(OT, "Aşağıdakilerden hangisi Tarife Cetvelinin 34. faslında <b>yer almaz</b>?",
 ["Otomobil karoserlerine mahsus cila", "Su üstünde yüzebilen gece kandili", "Poli(oksietilen) (polietilen glikol) esaslı mum",
 "Bulaşık yıkamada kullanılan sıvı deterjan", "Sabun içeren saç şampuanı"],
 "Sabun içeren saç şampuanı",
 "Fasıl 34 Not 1(c), sabun veya diğer yüzey aktif organik maddeler içeren şampuanları, diş macunlarını, traş krem ve köpüklerini ve banyo müstahzarlarını fasıl dışında bırakır; şampuan 33.05’tedir. Karoser cilası 34.05’te, yüzen gece kandili 34.06’da, polietilen glikol mumu 34.04’te, bulaşık deterjanı 34.02’de yer alır.",
 "Fasıl 34 Not 1(c); 34.06 Açıklama Notu.")

# 8
Q(OT, "Aşağıdakilerden hangisi “ışık temini için kullanılan her türlü mumlar ve benzerleri” pozisyonunda (34.06) <b>sınıflandırılmaz</b>?",
 ["Boyanmış ve parfümlenmiş stearin mum", "Top şeklinde sarılmış ince mum", "Su üstünde yüzebilen gece kandili",
  "Süslenmiş parafin mum", "Astım hastalığına karşı kullanılan fitilli mum"],
 "Astım hastalığına karşı kullanılan fitilli mum",
 "34.06 Açıklama Notu, astım hastalıklarına karşı kullanılan fitilli mumları hariç tutar ve 30.04’e gönderir. Mumların boyanmış, parfümlenmiş veya süslenmiş olması 34.06’yı bozmaz; top veya halka şeklindeki ince mumlar ve yüzen gece kandilleri de açıkça kapsama dahildir.",
 "34.06 Açıklama Notu, hariç (a).")

# 9
Q(OT, "Fasıl 34 Not 5’e göre aşağıdakilerden hangisi 34.04 pozisyonundaki “suni mumlar ve müstahzar mumlar” kapsamında <b>değildir</b>?",
 ["Farklı bitkisel mumların birbirine karıştırılmasıyla elde edilen ürün", "Parafin mumu ile polietilenden oluşan kaplama mumu",
  "Rafine edilmiş ve boyanmış, karıştırılmamış arı mumu", "Mineral mum ile bitkisel mumun karışımı",
  "Kimyasal yolla elde edilen, mumsu vasfı olan organik ürün"],
 "Rafine edilmiş ve boyanmış, karıştırılmamış arı mumu",
 "Not 5(b) istisnası uyarınca karıştırılmamış hayvansal veya bitkisel mumlar, boyanmış veya rafine edilmiş olsalar bile 15.21’de kalır. Farklı mumların karışımları (bitkisel+bitkisel, mineral+bitkisel), mum esaslı müstahzarlar ve kimyasal yolla elde edilen mumsu ürünler 34.04’ün tanımına girer. Tuzak, “rafine/boyanmış” ifadesini işlem görmüş müstahzar sanmaktır.",
 "Fasıl 34 Not 5; 34.04 Açıklama Notu (B), (C).")

# 10
Q(FA, "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
 ["Süetten (güderi) yapılmış ayakkabılar için müstahzar sıvı boya", "Deri ayakkabılar için krem cila", "Mobilya cilası", "Cam cilası",
 "Gümüş eşya için metal cilası"],
 "Süetten (güderi) yapılmış ayakkabılar için müstahzar sıvı boya",
 "Ayakkabı, mobilya, cam ve metal cila ve kremleri 34.05’te yer alır. 34.05 Açıklama Notu ise tablet halindeki ayakkabı beyazlatıcılarını ve güderiden yapılmış ayakkabılar için müstahzar sıvı boyaları hariç tutarak 32.10’a gönderir. Tuzak, “ayakkabı boyası” kelimesini her durumda 34.05 sanmaktır.",
 "34.05 Açıklama Notu, hariç (b).")

# 11
Q(FA, "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
 ["Sabun içeren traş köpüğü", "Kalıp halindeki traş sabunu", "Sabun içeren banyo köpüğü",
  "Yüzey aktif madde içeren diş macunu", "Sabun içeren şampuan"],
 "Kalıp halindeki traş sabunu",
 "Traş köpüğü, banyo köpüğü, diş macunu ve şampuan, sabun veya yüzey aktif madde içerseler de Fasıl 34 Not 1(c) uyarınca Fasıl 33’tedir (33.05, 33.06, 33.07). Blok (kalıp) halindeki traş sabunu ise 34.01 Açıklama Notunda tuvalet sabunu olarak sayılır ve Fasıl 34’te kalır.",
 "Fasıl 34 Not 1(c); 34.01 Açıklama Notu (I)(1)(c).")

# 12
Q(FA, "Aşağıdaki eşya ikililerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
 ["Sabun emdirilmiş keçe – sabun emdirilmiş gözenekli kauçuk", "Su içinde sabun çözeltisi (sıvı sabun) – organik çözücü içinde sabun çözeltisi",
  "Karıştırılmamış arı mumu – arı mumu ile parafin mumu karışımı", "Cila emdirilmiş gözenekli plastik sünger – sabunlu aşındırıcı ovma macunu",
  "Kalıp halindeki aşındırıcı sabun – sabunlu aşındırıcı ovma tozu"],
 "Cila emdirilmiş gözenekli plastik sünger – sabunlu aşındırıcı ovma macunu",
 "34.05, cila ve temizleme müstahzarlarını gözenekli plastik veya gözenekli kauçuğa emdirilmiş halde de kapsar; ovma macunları da 34.05’tedir. Buna karşılık sabun emdirilmiş keçe 34.01’de, sabun emdirilmiş gözenekli kauçuk mesnet maddesine göre; sıvı sabun 34.01, organik çözücüdeki sabun 34.02; karıştırılmamış arı mumu 15.21, mum karışımı 34.04; kalıp aşındırıcı sabun 34.01, ovma tozu 34.05’tedir.",
 "34.05 pozisyon metni; 34.01 Açıklama Notu hariç (e), (f); Fasıl 34 Not 2 ve Not 5.")

# 13
Q(FA, "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir tarife pozisyonunda yer alır?",
 ["Çamaşır yıkamada kullanılan toz deterjan", "Sütçülükte kullanılan, sodyum karbonat esaslı yağ giderici müstahzar",
  "Yüzey aktif madde içeren aşındırıcı temizleme macunu", "Sıhhi eşyayı temizlemeye mahsus asit esaslı temizleyici",
  "Pencere temizlemeye mahsus, yüzey aktif esaslı temizleme müstahzarı"],
 "Yüzey aktif madde içeren aşındırıcı temizleme macunu",
 "Deterjanlar, yüzey aktif esaslı temizleme müstahzarları ve esası yüzey aktif madde olmayan asit/alkali temizleyiciler ile sütçülükte kullanılan yağ gidericiler 34.02 kapsamındadır. Yüzey aktif madde içeren aşındırıcı müstahzarlar (temizleme patları ve tozları) ise 34.02’den hariç tutulup 34.05’te sınıflandırılır.",
 "34.02 Açıklama Notu (II)(B), (C) ve hariç (d); 34.05 Açıklama Notu.")

# 14
Q(FN, "Fasıl 34 Not 3’e göre bir ürünün “yüzey-aktif organik madde” sayılabilmesi için yapılan testle ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Ürün 20 °C’de %0,5’lik konsantrasyonda suyla karıştırılıp aynı sıcaklıkta 1 saat bekletilir.",
  "Ürün 40 °C’de %5’lik konsantrasyonda suyla karıştırılıp 24 saat bekletilir.",
  "Suyun yüzey gerilimini en az 72 dyn/cm’ye yükseltmesi gerekir.",
  "Ürünün suda tamamen çözünerek renksiz bir çözelti vermesi şarttır; emülsiyon kabul edilmez.",
  "Suyun yüzey gerilimini 4,5x10-2 N/m’nin üzerinde tutan ürünler yüzey aktif sayılır."],
 "Ürün 20 °C’de %0,5’lik konsantrasyonda suyla karıştırılıp aynı sıcaklıkta 1 saat bekletilir.",
 "Not 3’e göre ürün 20 °C’de %0,5 konsantrasyonda suyla karıştırılıp aynı sıcaklıkta 1 saat bırakıldığında (a) şeffaf/yarı şeffaf sıvı veya erimeyen madde ayrılmadan sabit emülsiyon vermeli ve (b) suyun yüzey gerilimini 4,5x10-2 N/m (45 dyn/cm) veya daha aza indirmelidir. Emülsiyon kabul edilir; eşik yüzey gerilimini düşürmeye ilişkindir, yükseltmeye değil.",
 "Fasıl 34 Not 3; 34.02 Açıklama Notu (I).")

# 15
Q(FN, "Fasıl 34 Not 2’ye göre “sabun” ve aşındırıcı içeren ürünlerle ilgili aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
 ["34.01 anlamında “sabun” tabirinden sadece suda eriyen sabunlar anlaşılır.",
  "34.01’deki sabunlar dezenfekte edici, dolgu maddesi veya ilaç gibi katkılar içerebilir.",
  "Aşındırıcı toz içeren ürünler çubuk veya kalıplanmış parça halindeyse 34.01’de yer alır.",
  "Aşındırıcı toz içeren ürünler hangi şekilde sunulursa sunulsun 34.01’de sınıflandırılır.",
  "Aşındırıcı toz içeren ürünler çubuk, topak veya kalıp şeklinde değilse 34.05’te yer alır."],
 "Aşındırıcı toz içeren ürünler hangi şekilde sunulursa sunulsun 34.01’de sınıflandırılır.",
 "Not 2, aşındırıcı tozları içeren ürünlerin yalnızca çubuk, topak veya kalıplanmış parça ya da şekillerde oldukları takdirde 34.01’de kalacağını; diğer şekillerde “temizleme tozları ve benzeri müstahzarlar” olarak 34.05’e gideceğini belirtir. Diğer ifadeler notun lafzına uygundur.",
 "Fasıl 34 Not 2.")

# 16
Q(FN, "34.04 Açıklama Notuna göre, kimyasal yolla elde edilen mumlar ile mum esaslı müstahzar mumların (A ve C paragrafları) sahip olması gereken özellikler hangi seçenekte doğru verilmiştir?",
 ["Damlama noktası 20 °C’nin üzerinde; viskozitesi damlama noktasında 100 Pa.s’yi geçmeyen",
  "Damlama noktası 40 °C’nin üzerinde; damlama noktasının 10 °C üzerindeki bir sıcaklıkta viskozitesi 10 Pa.s (10.000 cP)’yi geçmeyen",
  "Erime noktası 60 °C’nin üzerinde; suda çözünmeyen",
  "Damlama noktası 40 °C’nin altında; 20 °C’de saydam",
  "Damlama noktası 100 °C’nin üzerinde; elektriği iyi ileten"],
 "Damlama noktası 40 °C’nin üzerinde; damlama noktasının 10 °C üzerindeki bir sıcaklıkta viskozitesi 10 Pa.s (10.000 cP)’yi geçmeyen",
 "Açıklama Notu iki zorunlu ölçüt koyar: 40 °C’nin üzerinde damlama noktası ve rotasyonel viskometreyle ölçüldüğünde damlama noktasının 10 °C üzerindeki sıcaklıkta 10 Pa.s (10.000 cP)’yi geçmeyen viskozite. Bu mumlar ayrıca genellikle 20 °C’de saydam değildir (yarı saydam olabilir), ısı ve elektriği çok zayıf iletir; suda çözünür olanlar da (ör. polietilen glikol mumları) kapsamdadır.",
 "34.04 Açıklama Notu (1), (2); Fasıl 34 Not 5(a).")

# 17
Q(FN, "34.07 Açıklama Notuna göre dişçilikte kullanılan alçı esaslı müstahzarlarla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Yalnızca perakende satış için ambalajlanmış olanlar 34.07’de yer alır; dökme olanlar 25.20’dedir.",
  "Genellikle ağırlıkça %2’den fazla katkı maddesi içerirler ve sunum ile biçimlerine bakılmaksızın 34.07’de sınıflandırılırlar.",
  "Sadece az miktarda hızlandırıcı veya geciktirici içeren alçılar da 34.07’de yer alır.",
  "Dişçilik çimentoları ve diş dolguları da bu müstahzarlarla birlikte 34.07’dedir.",
  "Bu müstahzarlar ancak at nalı veya plaka şeklinde sunulduklarında 34.07’de kalır."],
 "Genellikle ağırlıkça %2’den fazla katkı maddesi içerirler ve sunum ile biçimlerine bakılmaksızın 34.07’de sınıflandırılırlar.",
 "Alçı esaslı dişçilik müstahzarları genellikle ağırlıkça %2’den fazla katkı (titanyum dioksit, renklendirici, kizelgur, dekstrin vb.) içerir ve sunum ile biçimlerine bakılmaksızın 34.07’dedir. Sadece az miktarda hızlandırıcı veya geciktirici içeren alçılar 25.20’de, dişçilik çimentoları ve dolgular 30.06’dadır. Şekil şartı (plaka, at nalı, çubuk) alçı müstahzarları için değil, “dişçi mumu” için aranır.",
 "34.07 Açıklama Notu (B) ve (C).")

# 18
Q(GYK, "Parafin mumu ile stearik asitten oluşan ve fitilli mum yapımında hammadde olarak kullanılan mum karışımı 34.04 pozisyonunda sınıflandırılır. Bu sınıflandırma hangi Genel Yorum Kuralına dayanır?",
 ["GYK 2(b)", "GYK 3(b)", "GYK 1", "GYK 3(c)", "GYK 4"], "GYK 1",
 "Mumların karışımları ve mum esaslı müstahzarlar Fasıl 34 Not 5(b) ve (c) ile 34.04’ün tanımına açıkça alınmıştır. GYK 2(b) Açıklama Notuna göre bir Bölüm veya Fasıl Notunda belirtilen hazır karışımlar 1 No.lu Kurala göre sınıflandırılır; bu nedenle 2(b), 3(b) veya 3(c)’ye başvurmaya gerek kalmaz.",
 "GYK 1; GYK 2(b) Açıklama Notu (X); Fasıl 34 Not 5(b), (c).")

# 19
Q(GYK, "Perakende satış için normal plastik şişesine doldurulmuş sıvı sabun gümrüğe sunulmuştur. Şişenin ayrıca sınıflandırılmayıp sabunla birlikte 34.01 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
 ["GYK 2(a)", "GYK 3(b)", "GYK 4", "GYK 5(a)", "GYK 5(b)"], "GYK 5(b)",
 "GYK 5(b), içindeki eşyayla birlikte sunulan ve o eşyanın ambalajında normal olarak kullanılan ambalaj maddelerinin eşyayla birlikte sınıflandırılmasını öngörür; tekrar kullanıma elverişli olduğu açıkça belli olanlar hariçtir. GYK 5(a) ise belli bir eşyaya göre şekillendirilmiş, uzun süre kullanılmaya uygun mahfazalara (ör. fotoğraf makinesi kabı) ilişkindir.",
 "GYK 5(b); GYK 5(a) Açıklama Notu (I).")

# 20
Q(ES, "34.03 pozisyon metnine göre aşağıdaki cümlede boş bırakılan yerlere sırasıyla hangisi gelmelidir? “34.03 pozisyonu, esas madde olarak içinde ağırlık itibarıyla ..... veya daha fazla petrol yağı veya bitümenli minerallerden elde edilen yağ içeren müstahzarları kapsamaz; bu yağların tanımı için ..... Fasıl Notuna bakılır.”",
 ["%50 – 27. Fasılın 2 No.lu", "%70 – 38. Fasılın 1 No.lu", "%85 – 27. Fasılın 1 No.lu", "%70 – 27. Fasılın 2 No.lu", "%60 – 34. Fasılın 3 No.lu"],
 "%70 – 27. Fasılın 2 No.lu",
 "34.03 pozisyon metni, esas madde olarak ağırlıkça %70 veya daha fazla petrol yağı ya da bitümenli minerallerden elde edilen yağ içeren müstahzarları hariç tutar. Fasıl 34 Not 4 ise 34.03’teki “petrol yağları ve bitümenli minerallerden elde edilen yağlar” tabirinin 27. Fasılın 2 No.lu Notunda tarif edilen ürünler olduğunu belirtir.",
 "34.03 pozisyon metni; Fasıl 34 Not 4.")

# 21
Q(ES, "34.04 pozisyonundan hariç tutulan aşağıdaki ürünler ile sınıflandırıldıkları pozisyonlar eşleştirildiğinde hangi seçenek doğru olur? I. Mumsu karaktere haiz lanolin alkoller; II. Mumsu karaktere haiz hidrojenlenmiş sıvı yağlar; III. Mumsu karaktere haiz sınai yağ alkolleri; IV. Takım halinde, perakende ambalajlı dişçi mumu. — a. 38.23 · b. 15.05 · c. 34.07 · d. 15.16",
 ["I-b, II-d, III-a, IV-c", "I-d, II-b, III-a, IV-c", "I-b, II-a, III-d, IV-c", "I-a, II-d, III-b, IV-c", "I-b, II-d, III-c, IV-a"],
 "I-b, II-d, III-a, IV-c",
 "34.04 Açıklama Notu hariç tutmalarına göre lanolin alkoller 15.05’te, hidrojenlenmiş sıvı yağlar 15.16’da, sınai yağ alkolleri 38.23’te, takım halinde veya perakende ambalajlı dişçi mumları 34.07’dedir. Bu ürünlerin mumsu görünmesi onları 34.04’e sokmaz.",
 "Fasıl 34 Not 5 istisna (a); 34.04 Açıklama Notu hariç (a), (b), (d), (e).")

# 22
Q(CC, "34.01 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Bu pozisyon anlamında “sabun” tabirinden sadece suda eriyen sabunlar anlaşılır. II. Kalsiyum sabunu gibi suda çözünmeyen metalik sabunlar 34.01’de yer alır. III. Sabun veya deterjan emdirilmiş keçe ve dokunmamış mensucat 34.01’de yer alır. IV. Perakende satışa hazırlanmamış, cildi yıkamaya mahsus sıvı yüzey aktif müstahzarlar 34.01’de yer alır.",
 ["I ve II", "II ve IV", "I, III ve IV", "I ve III", "III ve IV"], "I ve III",
 "I, Not 2’nin lafzıdır; III, pozisyon metninde ismen sayılmıştır. Suda çözünmeyen ve yalnızca kimyasal anlamda sabun olan kalsiyum ve diğer metalik sabunlar 34.01 dışındadır (II yanlış). Cilt yıkama müstahzarları ancak perakende satışa hazırlanmışsa 34.01’de, aksi halde 34.02’dedir (IV yanlış).",
 "Fasıl 34 Not 2; 34.01 pozisyon metni ve Açıklama Notu (III), hariç (b).")

# 23
Q(CC, "34.04 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Esas itibarıyla hidrokarbonlardan oluşan Fischer-Tropsch mumları 34.04’te yer alır. II. Mum karakterinde olmayan polietilenler 34.04’te değil 39. Fasılda (ör. 39.01) yer alır. III. Boyanmış suni mumlar 34.04 kapsamı dışındadır. IV. Sıvı bir ortamda karıştırılmış, dağıtılmış veya eritilmiş mumlar 34.04’te yer almaz.",
 ["I ve III", "II ve IV", "I, II ve IV", "II, III ve IV", "Yalnız IV"], "II ve IV",
 "Sentetik olarak veya başka şekilde üretilen 27.12’deki mumlar (Fischer-Tropsch mumları gibi) 34.04 dışındadır (I yanlış). Açıklama Notu “yukarıdaki mumlar boyanmış olsalar da burada sınıflandırılır” der (III yanlış). Mum karakterinde olmayan polietilenler 39.01 gibi pozisyonlara, sıvı ortamda dağıtılmış mumlar 34.05, 38.09 vb.’ne gider (II ve IV doğru).",
 "Fasıl 34 Not 5 istisna (c), (d); 34.04 Açıklama Notu (A) ve hariç (ij).")

# 24
Q(SN, "Bir ithalatçının beyan ettiği ürünün özellikleri şunlardır: aktif bileşeni sentetik organik yüzey aktif maddelerdir ve az miktarda sabun da içerir; aşındırıcı madde içermez; dikdörtgen kalıp halinde, alelade bir tuvalet sabunu biçimindedir; el ve vücut yıkamada kullanılır. Bu ürün hangi tarife pozisyonunda sınıflandırılır?",
 ["34.02", "33.07", "34.05", "33.04", "34.01"], "34.01",
 "34.01, çubuk, kalıplanmış parça ve şekillerde olup sabun olarak kullanılan yüzey aktif organik ürün ve müstahzarları (sabun içersin içermesin) kapsar; aktif unsurun sentetik olması ve sabunun herhangi bir oranda bulunması fark etmez. Aynı müstahzar toz veya pat halinde sunulsaydı 34.02’ye giderdi; burada belirleyici olan kalıp şeklidir. 33.07 banyo ve traş müstahzarlarının, 34.05 aşındırıcılı ovma ürünlerinin yeridir.",
 "34.01 pozisyon metni ve Açıklama Notu (II).")

# 25
Q(SN, "Lanolin esaslı olan, white spirit içinde çözünmüş bulunan (white spirit oranı ağırlıkça %75) ve metal yüzeylerde paslanmayı önlemek için kullanılan bir müstahzar Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
 ["27.10", "15.05", "34.03", "38.24", "32.08"], "34.03",
 "34.03 Açıklama Notu, lanolin esaslı ve white spirit’te çözünmüş paslanmayı önleyici müstahzarları, white spirit oranı ağırlıkça %70 veya daha fazla olsa bile bu pozisyona dahil eder; çünkü esas madde lanolindir. Tuzak, %70 eşiğini görünce doğrudan 27.10’u işaretlemektir. 15.05 karıştırılmamış lanolin ve yün yağının, 38.24 ise 38.24’teki paslanmayı önleyicilerin yeridir.",
 "34.03 Açıklama Notu, dahil olanlar (2).")

modul = {
  "tur": "fasil",
  "fasil": 34,
  "baslik": "Sabunlar, yüzey-aktif organik maddeler, yıkama müstahzarları, yağlama müstahzarları, suni mumlar, müstahzar mumlar, temizleme veya bakım müstahzarları, ışık temini için kullanılan her türlü mumlar ve benzerleri, model yapmaya mahsus her türlü patlar, \"dişçi mumları\" ve alçı esaslı dişçilik müstahzarları",
  "bolum": "VI",
  "oz": {
    "vurgu": "Fasıl 34, katı ve sıvı yağların, mumların sınai işlemden geçirilmesiyle elde edilen müstahzarlarla bazı yapay ürünleri (yüzey aktif maddeler, suni mumlar) toplar. Sınavda iki test öne çıkar: Eşya Fasıl 33’ün kozmetik/tuvalet müstahzarı mı, yoksa Fasıl 34’ün yıkama-temizleme-bakım ürünü mü? Ve sunum şekli (kalıp mı, toz mu; perakende mi, dökme mi) pozisyonu nasıl değiştiriyor?",
    "maddeler": [
      "Kimyaca belirli izole bileşikler ve karışım/müstahzar halinde olmayan tabii ürünler fasıl dışıdır (Fasıl 28–29, Fasıl 15, Fasıl 27).",
      "Sabun içerse bile şampuan, diş macunu, traş krem/köpüğü ve banyo müstahzarları Fasıl 33’tedir (Not 1(c)).",
      "Sabun = suda eriyen sabun; kalıp halindeki sabun ve sabun gibi kullanılan yüzey aktif ürünler, perakende cilt yıkama sıvıları ve sabun/deterjan emdirilmiş kağıt-vatka-keçe-dokunmamış mensucat 34.01’dedir.",
      "Yağlama müstahzarlarında ölçüt %70 petrol yağıdır; mumlarda ölçüt “karışım veya kimyasal yolla elde edilmiş mum”dur (tek tabii mum 15.21, mineral mum 27.12).",
      "Dişçi mumu şekle bağlıdır; alçı esaslı dişçilik müstahzarı her sunumda 34.07’dedir."
    ]
  },
  "karar_tablosu": {
    "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
    "satirlar": [
      ["1", "Kimyaca belirli izole bir bileşik mi?", "Fasıl 34 dışı → <b>Fasıl 28 / 29</b>"],
      ["2", "Şampuan, diş temizleyici, traş krem/köpüğü veya banyo müstahzarı mı? (sabun içerse de)", "<b>33.05</b> / <b>33.06</b> / <b>33.07</b>"],
      ["3", "Suda eriyen sabun; kalıp/çubuk halinde sabun gibi kullanılan yüzey aktif ürün; perakende cilt yıkama sıvısı/kremi; sabun/deterjan emdirilmiş kağıt, vatka, keçe, dokunmamış mensucat mı?", "<b>34.01</b>"],
      ["4", "Ayakkabı, mobilya, döşeme, karoser, cam veya metal cilası/kremi ya da aşındırıcılı ovma tozu/macunu mu?", "<b>34.05</b> (süet ayakkabı sıvı boyası <b>32.10</b>)"],
      ["5", "Yüzey aktif madde (Not 3 testi), deterjan, yardımcı yıkama veya temizleme/yağ giderme müstahzarı mı?", "<b>34.02</b>"],
      ["6", "Yağlama, kesme, cıvata gevşetme, pas önleme, kalıp ayırma veya tekstil/deri yağlama müstahzarı mı?", "Esas olarak ≥ %70 petrol yağı → <b>27.10</b> · aksi halde <b>34.03</b>"],
      ["7", "Mum karakterli; kimyasal yolla elde edilmiş, mum karışımı veya mum esaslı müstahzar mı?", "<b>34.04</b> (tek tabii mum <b>15.21</b> · mineral mum <b>27.12</b>)"],
      ["8", "Işık temini için fitilli mum, ince mum veya gece kandili mi?", "<b>34.06</b>"],
      ["9", "Model patı, belirli şekilde/takımda dişçi mumu veya alçı esaslı dişçilik müstahzarı mı?", "<b>34.07</b>"]
    ],
    "dipnot": "* Aşındırıcı içeren ürün kalıp, çubuk veya topak halindeyse 3. satırda (34.01) durur; toz veya macun ise 4. satıra (34.05) iner."
  },
  "pozisyon_haritasi": [
    ["34.01", "Sabunlar; sabun gibi kullanılan yüzey aktif ürünler; emdirilmiş kağıt vb.", "Suda eriyen sabun; kalıp şekli; cilt yıkamada perakende sıvı/krem", "Tuvalet sabunu, sıvı el sabunu, sabunlu kağıt mendil"],
    ["34.02", "Yüzey aktif maddeler; yıkama ve temizleme müstahzarları", "Not 3 testi; sabun dışı yüzey aktifler; deterjanlar", "Çamaşır/bulaşık deterjanı, cam temizleyici"],
    ["34.03", "Yağlama ve yağlanma müstahzarları", "Esas olarak %70’ten az petrol yağı", "Kesme yağı, pas önleyici, kalıp ayırıcı"],
    ["34.04", "Suni mumlar ve müstahzar mumlar", "Kimyasal yolla elde veya karışık mum", "Polietilen mum, polietilen glikol mumu, mühür mumu"],
    ["34.05", "Cilalar, kremler, ovma pat ve tozları", "Bakım/parlatma; aşındırıcılı temizleyici", "Ayakkabı boyası, mobilya cilası, ovma tozu"],
    ["34.06", "Işık temini için mumlar", "Fitilli; boyalı/süslü olabilir", "Stearin mum, yüzen gece kandili"],
    ["34.07", "Model patları; dişçi mumu; alçı esaslı dişçilik müstahzarı", "Dişçi mumunda şekil şartı", "Oyun hamuru, at nalı dişçi mumu"]
  ],
  "notlar": [
    ["Fasıl 34 Not 1", "Fasıl dışı: (a) döküm kalıbı müstahzarı olarak kullanılan yenilebilir hayvansal, bitkisel veya mikrobiyal yağ karışımları (15.17); (b) kimyaca belirli izole bileşikler; (c) sabun veya diğer yüzey aktif organik maddeler içeren şampuanlar, diş macunları, traş krem ve köpükleri, banyo müstahzarları (33.05, 33.06, 33.07)."],
    ["Fasıl 34 Not 2", "34.01’de “sabun” yalnızca <b>suda eriyen</b> sabundur. Sabunlar dezenfekte edici, aşındırıcı toz, dolgu maddesi veya ilaç içerebilir. Aşındırıcı tozlu ürün yalnızca <b>çubuk, topak, kalıplanmış parça veya şekil</b> halindeyse 34.01’de; diğer şekillerde temizleme tozu olarak 34.05’tedir."],
    ["Fasıl 34 Not 3", "“Yüzey-aktif organik madde”: <b>20 °C’de %0,5</b> konsantrasyonda suyla karıştırılıp aynı sıcaklıkta <b>1 saat</b> bırakıldığında (a) şeffaf/yarı şeffaf sıvı veya erimeyen madde ayrılmadan sabit emülsiyon veren ve (b) suyun yüzey gerilimini <b>4,5x10-2 N/m (45 dyn/cm) veya daha aza</b> indiren ürün."],
    ["Fasıl 34 Not 4", "34.03’teki “petrol yağları ve bitümenli minerallerden elde edilen yağlar”: 27. Fasılın 2 No.lu Notunda tarif edilen ürünler."],
    ["Fasıl 34 Not 5", "“Suni ve müstahzar mumlar” yalnızca: (a) kimyasal yolla elde edilen mumsu organik ürünler (suda çözünür olsun olmasın); (b) farklı mumların karışımları; (c) mum veya parafin esaslı, katı yağ, reçine, mineral madde vb. içeren mumsu ürünler. <b>Hariç:</b> 15.16, 34.02, 38.23 ürünleri (mumsu olsa da); karıştırılmamış hayvansal/bitkisel mumlar (15.21, boyanmış/rafine olsa da); mineral mumlar (27.12, birbirine karışmış veya boyanmış olsa da); sıvı ortamda karıştırılmış/dağıtılmış/eritilmiş mumlar (34.05, 38.09 vb.)."],
    ["Genel Açıklamalar", "Fasıl, katı yağ, sıvı yağ veya mumların sınai işlemiyle elde edilen müstahzarları ve yüzey aktif maddeler, suni mumlar gibi yapay ürünleri kapsar. Kimyaca belirli izole bileşikler ve karışım/müstahzar halinde olmayan tabii ürünler fasıl dışıdır."],
    ["34.01 Açıklama Notu", "Sabun: en az <b>sekiz karbon</b> atomlu yağ asitlerinin alkali tuzu. Sert sabun sodyum, yumuşak sabun potasyum hidroksit/karbonatla yapılır. Sıvı sabun: sabunun sudaki çözeltisi (genellikle <b>%5’i geçmeyen</b> alkol veya gliserol katılabilir). Perakende olmayan cilt yıkama müstahzarı 34.02’dedir. Hariç: sabun hammaddeleri (15.22), suda çözünmeyen metalik sabunlar, basitçe kokulandırılmış kağıt vb. (Fasıl 33), organik çözücüdeki sabun çözeltileri (34.02), sabun emdirilmiş gözenekli plastik/kauçuk, dokuma ve metal yastıkçıklar (mesnet maddesine göre)."],
    ["34.02 Açıklama Notu", "Yüzey aktif maddeler anyonlu, katyonlu, iyonlu olmayan veya amfolitik olabilir. 1 saat sonunda katı parçacıklar çıplak gözle görülüyor veya fazlar ayrışıyorsa emülsiyon stabil sayılmaz. Esası yüzey aktif olmayan asit/alkali temizleyiciler ve sütçülük-biracılık yağ gidericileri de buradadır. Hariç: aşındırıcılı temizleme pat ve tozları (34.05); suda çözünmeyen naftenatlar ve petrol sülfonatları (38.24)."],
    ["34.03 Açıklama Notu", "Esas olarak ≥ %70 petrol yağı içerenler 27.10’dadır. Buna rağmen 34.03’te kalanlar: mineral yağda molibden disülfit süspansiyonları (temel unsur molibden disülfit), lanolin esaslı ve white spirit’te çözünmüş pas önleyiciler (white spirit ≥ %70 olsa bile). Hariç: suni degralar (15.22), tıbbi jel kayganlaştırıcılar (30.06), kolloidal grafit (38.01), transmisyon kayışı kaymayı önleyicileri (38.24)."],
    ["34.04 Açıklama Notu", "Kimyasal yolla elde edilen ve mum esaslı müstahzar mumlarda: damlama noktası <b>40 °C’nin üzerinde</b> ve damlama noktasının 10 °C üzerinde viskozite <b>10 Pa.s (10.000 cP)’yi geçmez</b>. Boyanmış olsalar da buradadır. Mineral mum karışımları 27.12’de kalır."],
    ["34.07 Açıklama Notu", "Dişçi mumu ve dişçilik baskı bileşikleri yalnızca takım halinde, perakende ambalajda veya plaka, at nalı, çubuk vb. şekillerde 34.07’dedir; dökme ise bileşimine göre (34.04, 38.24 vb.). Alçı esaslı dişçilik müstahzarları genellikle <b>%2’den fazla</b> katkı içerir, sunumuna bakılmaksızın 34.07’dedir; az hızlandırıcılı alçılar 25.20’de, dişçi çimentoları 30.06’dadır."]
  ],
  "sinir_komsulari": [
    ["Sabun içeren şampuan, diş macunu, traş kremi/köpüğü, banyo köpüğü", "33.05 / 33.06 / 33.07", "Fasıl 34 Not 1(c)"],
    ["Basitçe kokulandırılmış kağıt, vatka, keçe", "Fasıl 33", "Sabun/deterjan emdirilmemiş; yalnız koku"],
    ["Ekmekçilikte kalıp gevşetici yenilebilir yağ karışımı", "15.17", "Fasıl 34 Not 1(a)"],
    ["Sabun hammaddesi; suni degra", "15.22", "34.01 ve 34.03 hariç tutmaları"],
    ["Karıştırılmamış arı mumu, bitkisel mum (rafine/boyanmış)", "15.21", "Not 5 istisna (b)"],
    ["Parafin mumu, mineral mum karışımları, Fischer-Tropsch mumu", "27.12", "Not 5 istisna (c)"],
    ["Esas olarak ≥ %70 petrol yağı içeren yağlama yağı", "27.10", "34.03 pozisyon metni"],
    ["Tıbbi muayene ve cerrahi için jel kayganlaştırıcı", "30.06", "34.03 hariç tutması"],
    ["Kolloidal grafit, grafit patı", "38.01", "34.03 hariç tutması"],
    ["Sınai yağ alkolleri ve sınai monokarboksilik yağ asitleri", "38.23", "Not 5 istisna (a)"],
    ["Suda çözünmeyen naftenatlar, petrol sülfonatları; kayış kaymayı önleyici", "38.24", "34.02 ve 34.03 hariç tutmaları"],
    ["Tablet ayakkabı beyazlatıcısı; süet ayakkabı sıvı boyası", "32.10", "34.05 hariç tutması"],
    ["Astım mumu / mumlu kibrit / kükürtlü fitil ve mum", "30.04 / 36.05 / 38.08", "34.06 hariç tutmaları"],
    ["Dişçilik için kalsine alçı (az hızlandırıcılı) / dişçi çimentosu", "25.20 / 30.06", "34.07 Açıklama Notu"],
    ["Önemli miktarda fenol/krezol içeren sıvı dezenfektan", "38.08", "Dezenfektan sabun (katı) 34.01’dedir"]
  ],
  "tuzaklar": [
    "<b>Sabun içeren şampuan sabun değildir.</b> Şampuan, diş macunu, traş kremi/köpüğü ve banyo müstahzarları yüzey aktif madde içerse de Fasıl 33’tedir; yalnız blok traş sabunu 34.01’de kalır.",
    "<b>Aşındırıcılı sabunda şekil belirleyicidir.</b> Kalıp, çubuk veya topak ise 34.01; toz veya macun ise 34.05. Yüzey aktifli aşındırıcı müstahzarlar 34.02’ye de girmez.",
    "<b>Cilt yıkama sıvısı: perakende 34.01, dökme 34.02.</b> Sentetik yüzey aktif esaslı sıvı/krem cilt temizleyici ancak perakende satışa hazırlanmışsa 34.01’dedir.",
    "<b>Sabunlu sünger ≠ cilalı sünger.</b> 34.01 yalnız kağıt, vatka, keçe ve dokunmamış mensucatı kapsar; sabun emdirilmiş gözenekli plastik/kauçuk mesnet maddesine göre ayrılır. 34.05 ise gözenekli plastik ve kauçuğu da kapsar.",
    "<b>%70 eşiğinin istisnaları var.</b> Mineral yağda molibden disülfit süspansiyonu ve white spirit’te lanolin esaslı pas önleyici, oran %70’i aşsa da 34.03’te kalır.",
    "<b>Tek mum 15.21, karışık mum 34.04, mineral mum 27.12.</b> Mineral mumların kendi aralarındaki karışımı yine 27.12’dir; boyanmış suni mum ise 34.04’ten çıkmaz.",
    "<b>Sıvıda dağıtılmış mum artık mum değildir.</b> Çözünmüş veya emülsiyon halindeki mumlar 34.05, 38.09 vb.’ne gider.",
    "<b>Dişçi mumu şekil ister, dişçilik alçısı istemez.</b> Dökme dişçi mumu bileşimine göre (34.04, 38.24); alçı esaslı dişçilik müstahzarı her sunumda 34.07; az hızlandırıcılı alçı 25.20.",
    "<b>Dezenfektan sabun katıdır.</b> Az miktarda fenol, krezol vb. içeren katı sabun 34.01; önemli miktarda içeren sıvı dezenfektan 38.08.",
    "<b>Mum aydınlatma cihazı aksamı değildir.</b> Lambayla birlikte bile mum 34.06’dadır; astım mumu ise 30.04’e gider."
  ],
  "hafiza": {
    "kanca": "SA – YÜ – YA – MU – Cİ – IŞ – MO",
    "aciklama": "<b>SA</b>bun 34.01 · <b>YÜ</b>zey aktif ve deterjan 34.02 · <b>YA</b>ğlama 34.03 · <b>MU</b>m (suni/müstahzar) 34.04 · <b>Cİ</b>la ve ovma tozu 34.05 · <b>IŞ</b>ık mumu 34.06 · <b>MO</b>del patı ve dişçi 34.07. Görsel benzetme: ellerinizi sabunla yıkayın, bulaşığı deterjanla yıkayın, makineyi yağlayın, mumları karıştırın, ayakkabıyı cilalayın, mumu yakın ve çocuğunuzla oyun hamurundan model yapın."
  },
  "sinav_odagi": [
    "Fasıl 34 çıkmış sorularda sınırlı sayıda doğrudan sorulmuş; çoğunlukla Fasıl 33, 27 ve 94 sorularında seçenek ve çeldirici olarak yer almıştır.",
    "Ayakkabı boyasının 34.05’te yer aldığı; 34.05’in “ayakkabı ile ilgili ürün içeren pozisyon” olarak tanınması (pozisyon sorgulama kalıbı).",
    "Sabun–kozmetik ayrımı: el sabununun Fasıl 34’te, diş macunu, saç boyası ve kontak lens solüsyonunun Fasıl 33’te olduğu “farklı fasıl” soruları; kontak lens solüsyonu sorusunda 34.01 ve 34.02 çeldirici olarak kullanılmıştır.",
    "Mumun 94.05’teki aydınlatma cihazlarının aksamı sayılmadığı; ham vazelinin 27.12’de olduğu ve 34.01’in çeldirici olduğu sorular.",
    "Dişçilik alçısı: özel kalsine edilmiş alçının 25.20’de kaldığı; alçı esaslı dişçilik müstahzarlarının 34.07’ye, dişçi çimentolarının 30.06’ya gittiği ayrım."
  ],
  "cikmis_ornekler": [
    {
      "soru": "Türk Gümrük Tarife Cetveline göre ayakkabı boyası hangi tarife pozisyonunda sınıflandırılır?",
      "secenekler": ["32.05", "35.01", "34.05", "38.24"],
      "cevap": "C",
      "aciklama": "34.05 pozisyon metni ayakkabı boya ve cilalarını ismen kapsar. Yalnızca tablet halindeki ayakkabı beyazlatıcıları ve güderi ayakkabılar için müstahzar sıvı boyalar 32.10’a gider."
    },
    {
      "soru": "Tarife mevzuatına göre aşağıdakilerden hangisi 94.05 pozisyonundaki bir aydınlatma cihazının aksamı olarak bu pozisyonda <b>sınıflandırılmaz</b>?",
      "secenekler": ["Abajur ayağı", "Reflektör", "Mum", "Lamba camı"],
      "cevap": "C",
      "aciklama": "Mumlar aydınlatma cihazı aksamı sayılmaz; boyalı, parfümlü veya süslü olsalar da ışık temini için kullanılan mumlar olarak 34.06’da sınıflandırılır."
    }
  ],
  "ozet": [
    "Kimyaca belirli bileşik Fasıl 28–29’a; sabunlu şampuan, diş macunu, traş ve banyo ürünü Fasıl 33’e gider.",
    "34.01: suda eriyen sabun, kalıp halinde sabun gibi kullanılan yüzey aktif ürün, perakende cilt yıkama sıvısı, sabunlu kağıt-vatka-keçe-dokunmamış mensucat.",
    "34.02: Not 3 testini geçen yüzey aktifler, deterjanlar, yardımcı yıkama ve temizleme müstahzarları.",
    "34.03: yağlama ve yağlanma müstahzarları; esas olarak ≥ %70 petrol yağı ise 27.10.",
    "34.04: kimyasal yolla elde veya karışık mumlar (damlama noktası 40 °C’nin üzerinde); tek tabii mum 15.21, mineral mum 27.12.",
    "34.05 cila ve ovma tozu, 34.06 ışık mumu, 34.07 model patı, şekilli dişçi mumu ve alçı esaslı dişçilik müstahzarı."
  ],
  "sorular": SORULAR
}

if __name__ == "__main__":
  print(Counter(q["cevap"] for q in SORULAR), len(SORULAR))
  print("".join(q["cevap"] for q in SORULAR))
  out = os.path.join(KITAP, "data", "fasil_34.json")
  with open(out, "w", encoding="utf-8") as f:
    json.dump(modul, f, ensure_ascii=False, indent=1)
  print("yazıldı:", out)
