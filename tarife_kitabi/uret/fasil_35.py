#!/usr/bin/env python3
# Fasıl 35 modülü üreteci
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
Q(E4, "Tarife Cetveline göre, kuru madde üzerinden hesaplandığında ağırlık itibarıyla %85 peyniraltı suyu proteini içeren ve iki veya daha fazla peyniraltı suyu proteininden oluşan peyniraltı suyu protein konsantresi hangi pozisyonda sınıflandırılır?",
  ["04.04", "35.04", "35.02", "21.06", "35.01"], "35.02",
  "35.02 pozisyon metni, kuru madde üzerinden ağırlıkça %80’den fazla peyniraltı suyu proteini içeren iki veya daha fazla peyniraltı suyu proteini konsantrelerini albümin olarak kapsar. Oran %80 veya daha az olsaydı eşya 04.04’te kalırdı. 35.04 globülinler gibi diğer proteinlerin, 35.01 kazeinin yeridir.",
  "35.02 pozisyon metni ve Açıklama Notu (1).")

# 2
Q(E4, "Kazein ve tebeşir karışımına az miktarda boraks katılarak elde edilen, 25 kg’lık torbalarda dökme olarak sunulan toz halindeki kazein tutkalı hangi tarife pozisyonunda yer alır?",
  ["35.06", "35.01", "35.03", "35.05", "39.13"], "35.01",
  "Kazein tutkalları 35.01 pozisyon metninde ismen sayılır; kazein ile tebeşir karışımlarına boraks veya amonyum klorür katılmasıyla elde edilenler örnek olarak verilmiştir. Yalnızca net ağırlığı 1 kg’ı geçmeyen perakende ambalajlarda sunulsaydı 35.06’ya giderdi. 35.03 hayvansal menşeli diğer tutkalları kazein tutkalları hariç kapsar; sertleştirilmiş kazein 39.13’tedir.",
  "35.01 pozisyon metni ve Açıklama Notu; 35.03 pozisyon metni.")

# 3
Q(E4, "Bilardo ıstakasının ucuna takılmak üzere sertleştirilmemiş jelatinden disk şeklinde kesilmiş küçük plakalar Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
  ["35.03", "39.13", "49.11", "96.02", "95.04"], "96.02",
  "35.03 Açıklama Notuna göre yaprak halindeki jelatin ancak dikdörtgen (kare dahil) şekilde ise bu pozisyonda kalır; disk gibi başka şekillerde kesilmiş veya kalıplanmış sertleştirilmemiş jelatin 96.02’ye gider. 39.13 sertleştirilmiş jelatinin, 49.11 baskılı ürünlerin yeridir.",
  "35.03 Açıklama Notu; 96.02 Açıklama Notu (8).")

# 4
Q(E4, "Proteolitik bir enzim olan papaine dekstroz katılarak hazırlanan ve etleri yumuşatmak için kullanılan enzimatik müstahzar hangi pozisyonda yer alır?",
  ["21.06", "13.02", "35.07", "21.03", "30.04"], "35.07",
  "35.07 Açıklama Notu, tarifenin başka yerinde yer almayan müstahzar enzimler arasında dekstroz veya diğer gıda maddeleri katılmış proteolitik enzimlerden (papain gibi) oluşan et yumuşatıcı müstahzarları ismen sayar. Sadece suda kısmen eriyebilen kurutulmuş lateks halindeki papain ise 13.02’dedir; tuzak, gıda katkısı görünümü nedeniyle 21.06’yı seçmektir.",
  "35.07 Açıklama Notu (C)(i); papain paragrafı.")

# 5
Q(E4, "Hidroksipropil grupları içeren, eterleşme yoluyla tadil edilmiş nişasta Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
  ["11.08", "35.05", "39.13", "17.02", "38.09"], "35.05",
  "35.05, dekstrinleri ve önceden jelatinlenmiş, esterleşmiş veya eterleşmiş nişastalar gibi tadil edilmiş diğer nişastaları kapsar; Açıklama Notu hidroksietil, hidroksipropil veya karboksimetil grupları içeren eterleşmiş nişastaları örnek verir. Tadil edilmemiş nişasta 11.08’de, nişasta esaslı müstahzar apreler 38.09’dadır.",
  "35.05 pozisyon metni ve Açıklama Notu.")

# 6
Q(OT, "Aşağıdakilerden hangisi Tarife Cetvelinin 35. faslında <b>sınıflandırılmaz</b>?",
  ["Buzağıların dördüncü midesinden elde edilen peynir mayası (rennin)", "Tanen tayininde kullanılan kromlu deri tozu",
   "Mersin balığının hava keselerinden elde edilen katı ihtiyokol", "Bira mayası",
   "Kuru maddede dekstroz olarak ifade edilen indirgen şeker oranı %8 olan maltodekstrin"],
  "Bira mayası",
  "Fasıl 35 Not 1(a) mayaları fasıl dışında bırakır; mayalar 21.02’dedir. Peynir mayası (şirden mayası) bir enzim olarak 35.07’de, kromlu deri tozu 35.04’te, katı ihtiyokol 35.03’te, indirgen şeker oranı %10’u geçmeyen maltodekstrin dekstrin olarak 35.05’tedir. Tuzak, “peynir mayası” adını mayayla karıştırmaktır.",
  "Fasıl 35 Not 1(a) ve Not 2; 35.07 Açıklama Notu.")

# 7
Q(OT, "Aşağıdakilerden hangisi 35.04 pozisyonunda <b>yer almaz</b>?",
  ["Mısırdan elde edilen zein", "Yağı alınmış soya unundan ekstraksiyonla elde edilen, protein içeriği %92 olan protein izolatı",
   "Fibrinojen", "Boynuz ve tüylerden elde edilen keratin", "Et peptonu"],
  "Fibrinojen",
  "35.04 Açıklama Notu, fibrinojen, fibrin, kan ve serum globülinleri ile diğer kan fraksiyonlarını hariç tutarak 30.02’ye gönderir. Zein (prolamin), protein içeriği %90’dan az olmayan protein izolatları, keratinler ve peptonlar 35.04’te sayılmıştır.",
  "35.04 Açıklama Notu ve hariç tutmalar; Fasıl 35 Not 1(b).")

# 8
Q(OT, "Aşağıdakilerden hangisi 35.03 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Kare şeklinde kesilmiş, yüzeyi boyanmış jelatin yaprağı", "Kemik tutkalı", "Jelatin tannat",
   "Balık artıklarından elde edilen sıvı balık tutkalı", "Jelatin esaslı kopyalama (teksir) patı"],
  "Jelatin esaslı kopyalama (teksir) patı",
  "35.03 Açıklama Notu jelatin esaslı kopya patlarını (teksir jölelerini) hariç tutarak 38.24’e gönderir. Dikdörtgen veya kare yaprak halindeki jelatin yüzeyi işlenmiş veya boyanmış olsa da, jelatin türevleri (jelatin tannat), kemik tutkalı ve balık tutkalları 35.03’tedir.",
  "35.03 pozisyon metni ve Açıklama Notu, hariç tutmalar.")

# 9
Q(OT, "Aşağıdakilerden hangisi 35.07 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Pepsin", "Ananas bitkisinden elde edilen bromelain", "Şarabı berraklaştırmak için jelatin katılmış pektik enzim müstahzarı",
   "Ön dabaklamada kullanılan enzimli müstahzar", "Mensucatın haşılını çıkarmada kullanılan bakteriyel amilaz müstahzarı"],
  "Ön dabaklamada kullanılan enzimli müstahzar",
  "Fasıl 35 Not 1(c) ve 35.07 Açıklama Notu, ön dabaklamada kullanılan enzimli müstahzarları 32.02’ye gönderir. Pepsin, bromelain, içecek berraklaştırıcı pektik enzim müstahzarları ve haşıl çıkarmada kullanılan bakteriyel amilaz müstahzarları 35.07’de sayılmıştır.",
  "Fasıl 35 Not 1(c); 35.07 Açıklama Notu.")

# 10
Q(FA, "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda yer alır?",
  ["Yenilebilir jelatin", "Asit kazein", "Kimyasal işlemle sertleştirilmiş kazein", "Glukoz izomeraz", "Beyaz dekstrin"],
  "Kimyasal işlemle sertleştirilmiş kazein",
  "Fasıl 35 Not 1(e) sertleştirilmiş proteinleri fasıl dışında bırakır; 35.01 Açıklama Notu da sertleştirilmiş kazeini 39.13’e gönderir. Jelatin (35.03), asit kazein (35.01), glukoz izomeraz (35.07) ve dekstrin (35.05) Fasıl 35’tedir.",
  "Fasıl 35 Not 1(e); 35.01 Açıklama Notu, hariç tutmalar.")

# 11
Q(FA, "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir tarife pozisyonunda sınıflandırılır?",
  ["Yumurta albümini (ovalbümin)", "Süt albümini (laktalbümin)", "Kurutulmuş kan (“kan albümini” diye tarif edilse de)",
   "Demir albüminat", "Balık albümini"],
  "Kurutulmuş kan (“kan albümini” diye tarif edilse de)",
  "35.02 Açıklama Notu, bazen yanlışlıkla “kan albümini” diye tarif edilen kurutulmuş kanı hariç tutar ve 05.11’e gönderir. Yumurta, süt ve balık albüminleri ile albüminatlar (demir albüminat gibi) 35.02’dedir.",
  "35.02 Açıklama Notu, hariç tutmalar.")

# 12
Q(FA, "Aşağıdaki eşya ikililerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda yer alır?",
  ["Hazırlanmamış mısır nişastası – önceden jelatinlenmiş nişasta", "Kazein – sertleştirilmiş kazein",
   "Peptonlar – nükleik asitler", "Malt amilazı – malt hülasası",
   "Dökme halde dekstrin tutkalı – işlem görmemiş nişasta, boraks ve nişasta eterlerinden oluşan dökme tutkal"],
  "Dökme halde dekstrin tutkalı – işlem görmemiş nişasta, boraks ve nişasta eterlerinden oluşan dökme tutkal",
  "Esası nişasta, dekstrin veya tadil edilmiş nişasta olan tutkallar (dekstrin tutkalları, işlem görmemiş nişasta, boraks ve nişasta eterlerinden oluşan tutkallar) perakende ambalajda değilse 35.05’tedir. Diğer ikililer ayrılır: nişasta 11.08 / önjelatinleşmiş nişasta 35.05; kazein 35.01 / sertleştirilmiş kazein 39.13; peptonlar 35.04 / nükleik asitler 29.34; malt amilazı 35.07 / malt hülasası 19.01.",
  "35.05 Açıklama Notu; 35.04 ve 35.07 Açıklama Notları, hariç tutmalar.")

# 13
Q(FA, "Perakende satış için ambalajlanmamış (dökme) olarak sunulan aşağıdaki tutkallardan hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
  ["Kemik tutkalı", "Deri tutkalı", "Sinir (veter) tutkalı", "Kısmi fermentasyonla çözünür hale getirilmiş glutenden elde edilen gluten tutkalı (“Viyana tutkalı”)",
   "Balık artıklarından elde edilen balık tutkalı"],
  "Kısmi fermentasyonla çözünür hale getirilmiş glutenden elde edilen gluten tutkalı (“Viyana tutkalı”)",
  "Kemik, deri, sinir ve balık tutkalları hayvansal menşeli tutkallar olarak 35.03’tedir. Gluten tutkalları ise bitkisel kaynaklıdır ve 35.06 Açıklama Notunda “tarifenin başka yerinde belirtilmeyen müstahzar tutkallar” örneği olarak sayılır. Dökme sunum, perakende kuralını (35.06) devre dışı bırakır; ayrım kaynağa göre yapılır.",
  "35.03 Açıklama Notu; 35.06 Açıklama Notu (B)(i).")

# 14
Q(FN, "Fasıl 35 Not 2’ye göre “dekstrin” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
  ["Dekstroz olarak ifade edilen indirgen şeker miktarı kuru madde üzerinden %10 veya daha az olan nişasta parçalanma ürünleridir.",
   "İndirgen şeker miktarı kuru madde üzerinden %20’yi geçmeyen nişasta parçalanma ürünleridir.",
   "İndirgen şeker oranı %10’dan fazla olan nişasta parçalanma ürünleri de dekstrin olarak 35.05’te kalır.",
   "Dekstrin tanımında ölçüt nişastanın protein oranıdır.",
   "İndirgen şeker oranı %10’dan fazla olanlar 11.08 pozisyonunda yer alır."],
  "Dekstroz olarak ifade edilen indirgen şeker miktarı kuru madde üzerinden %10 veya daha az olan nişasta parçalanma ürünleridir.",
  "Not 2’ye göre dekstrin, nişastanın parçalanmasıyla elde edilen ve dekstroz olarak ifade edilen indirgen şeker miktarı kuru madde üzerinden %10 veya daha az olan üründür. %10’u aşanlar 17.02’de yer alır; 11.08 tadil edilmemiş nişastanın pozisyonudur. Maltodekstrin de bu eşiğe göre ayrılır.",
  "Fasıl 35 Not 2; 35.05 Açıklama Notu.")

# 15
Q(FN, "Fasıl 35 Not 1(b) ile ilgili aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
  ["Bütün kan fraksiyonları, tedavi amacıyla hazırlanmamış olsalar da Fasıl 35’te yer alır.",
   "Tedavi veya korunmada kullanılmak üzere hazırlanmamış kan albümini Fasıl 35’te kalır; diğer kan fraksiyonları fasıl dışıdır.",
   "Tedavi amacıyla hazırlanmış kan albümini 35.02’de sınıflandırılır.",
   "Fibrinojen ve serum globülinleri 35.04’te yer alır.",
   "Kan albümini her durumda Fasıl 30’dadır."],
  "Tedavi veya korunmada kullanılmak üzere hazırlanmamış kan albümini Fasıl 35’te kalır; diğer kan fraksiyonları fasıl dışıdır.",
  "Not 1(b), kan fraksiyonlarını Fasıl 35 dışında bırakır ama tedavi veya korunmada kullanılmak üzere hazırlanmamış kan albüminini bu istisnadan ayırır; bu ürün 35.02’dedir. Tedavi veya korunma için hazırlanan kan albümini Fasıl 30’a, fibrinojen ve kan/serum globülinleri 30.02’ye gider.",
  "Fasıl 35 Not 1(b); 35.02 ve 35.04 Açıklama Notları.")

# 16
Q(FN, "35.02 Açıklama Notuna göre, peyniraltı suyu protein konsantrelerinde peyniraltı suyu protein muhtevası nasıl hesaplanır?",
  ["Nitrojen miktarı 6,25 çevirme faktörüyle çarpılarak", "Nitrojen miktarı 6,38 çevirme faktörüyle çarpılarak",
   "Laktoz miktarı 6,38 çevirme faktörüyle çarpılarak", "Kuru madde miktarı 0,80 katsayısıyla çarpılarak",
   "Nitrojen miktarı 5,70 çevirme faktörüyle çarpılarak"],
  "Nitrojen miktarı 6,38 çevirme faktörüyle çarpılarak",
  "35.02 Açıklama Notu, peyniraltı suyu protein muhtevasının nitrojen miktarının 6,38’lik çevirme faktörüyle çarpılarak hesaplanacağını belirtir. Bu hesapla kuru maddede %80’den fazla peyniraltı suyu proteini çıkan konsantreler 35.02’de, %80 veya daha az olanlar 04.04’tedir.",
  "35.02 Açıklama Notu (1); 35.02 pozisyon metni.")

# 17
Q(FN, "35.04 Açıklama Notuna göre bir bitkisel maddeden ekstraksiyonla elde edilen “protein izolatları”nın protein içeriği için öngörülen ölçüt hangisidir?",
  ["%50’den az olmamalıdır", "%70’ten az olmamalıdır", "%80’den fazla olmalıdır", "%85’ten az olmamalıdır", "%90’dan az olmamalıdır"],
  "%90’dan az olmamalıdır",
  "35.04 Açıklama Notu, yağı alınmış soya unu gibi bitkisel maddelerden ekstraksiyonla elde edilen protein izolatlarının protein içeriklerinin %90’dan daha az olmadığını belirtir. Yağı alınmış soya unundan bazı maddelerin giderilmesiyle elde edilen konsantreler ise 21.06’dadır. %80 eşiği peyniraltı suyu protein konsantrelerine (35.02) aittir.",
  "35.04 Açıklama Notu (B); hariç (a).")

# 18
Q(GYK, "Ambalajı üzerinde yalnızca tutkal olarak satılacağı belirtilmiş, net ağırlığı 250 g olan perakende kutuda dekstrin, 35.05 yerine 35.06 pozisyonunda sınıflandırılır. Bu sınıflandırma hangi Genel Yorum Kuralına dayanır?",
  ["GYK 1", "GYK 2(b)", "GYK 3(a)", "GYK 3(c)", "GYK 5(b)"], "GYK 1",
  "Sonuç, pozisyon metni (35.06: tutkal olarak perakende satılmak üzere net ağırlığı 1 kg’ı geçmeyen ambalajlara konulmuş ürünler) ile Bölüm VI Not 2’den doğar; Bölüm VI Not 2’nin açıklamasında tutkal olarak perakende satış için hazırlanmış dekstrinin 35.05’te değil 35.06’da sınıflandırılacağı örneği yer alır. Pozisyon ve not hükmüyle yapılan sınıflandırma GYK 1’dir; GYK 3’e başvurulmaz.",
  "GYK 1; Bölüm VI Not 2 ve Genel Açıklaması; 35.06 pozisyon metni.")

# 19
Q(GYK, "Genel Yorum Kurallarının Açıklama Notlarına göre, I ila VI. Bölümlere giren eşya (örneğin Fasıl 35’teki tutkallar ve enzimler) bakımından normal olarak uygulanmayan kural hangisidir?",
  ["GYK 1", "GYK 2(b)", "GYK 3(b)", "GYK 2(a)", "GYK 5(b)"], "GYK 2(a)",
  "GYK 2(a) Açıklama Notları (III) ve (IX), kuralın tamamlanmamış/bitirilmemiş eşya ile birleştirilmemiş veya demonte eşyaya ilişkin kısımlarının I ila VI. Bölüm eşyasına normal olarak uygulanmayacağını belirtir. Karışımlarla ilgili GYK 2(b), takımlarla ilgili 3(b) ve ambalajla ilgili 5(b) bu bölümlerde de kullanılabilir.",
  "GYK 2(a) Açıklama Notu (III), (IX).")

# 20
Q(ES, "Aşağıdaki cümlede boş bırakılan yerlere sırasıyla hangisi gelmelidir? “35.06 pozisyonu, tutkal ve yapıştırıcı olarak perakende satılmak üzere net ağırlığı ..... geçmeyen ambalajlara konulmuş ürünleri kapsar; buna karşılık sertleştirilmiş proteinler Fasıl 35 Not 1 uyarınca ..... pozisyonunda yer alır.”",
  ["1 kg’ı – 39.13", "5 kg’ı – 39.13", "1 kg’ı – 35.04", "500 g’ı – 39.06", "2 kg’ı – 96.02"],
  "1 kg’ı – 39.13",
  "35.06 pozisyon metni perakende eşik olarak net 1 kg’ı belirler; aynı eşik 35.01, 35.03 ve 35.05 Açıklama Notlarındaki hariç tutmalarda da tekrarlanır. Fasıl 35 Not 1(e) sertleştirilmiş proteinleri 39.13’e gönderir; 35.04 ise başka yerde yer almayan proteinlerin pozisyonudur.",
  "35.06 pozisyon metni; Fasıl 35 Not 1(e).")

# 21
Q(ES, "Fasıl 35 Not 1 uyarınca fasıl dışında kalan aşağıdaki ürünler ile yer aldıkları pozisyon veya fasıllar eşleştirildiğinde hangi seçenek doğru olur? I. Mayalar; II. Ön dabaklamada kullanılan enzimli müstahzarlar; III. Sertleştirilmiş proteinler; IV. Baskı sanayiinde kullanılan jelatin ürünler. — a. 39.13 · b. Fasıl 49 · c. 21.02 · d. 32.02",
  ["I-c, II-a, III-d, IV-b", "I-d, II-c, III-a, IV-b", "I-c, II-d, III-b, IV-a", "I-b, II-d, III-a, IV-c", "I-c, II-d, III-a, IV-b"],
  "I-c, II-d, III-a, IV-b",
  "Not 1’e göre mayalar 21.02’de, ön dabaklamada kullanılan enzimli müstahzarlar 32.02’de, sertleştirilmiş proteinler 39.13’te, baskı sanayiinde kullanılan jelatin ürünler Fasıl 49’da yer alır. Notun diğer bentleri kan fraksiyonlarını ve ilaçları (Fasıl 30) ile ıslatıcı veya yıkayıcı enzimli müstahzarları (Fasıl 34) dışarıda bırakır.",
  "Fasıl 35 Not 1(a), (c), (e), (f).")

# 22
Q(CC, "35.05 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Önceden jelatinlenmiş (şişmiş) nişasta 35.05’te yer alır. II. Hazırlanmamış nişasta 35.05’te yer alır. III. Patlayıcı yapımında kullanılan nişasta nitratları 35.05’te yer alır. IV. Formaldehit ile işlem görmüş, cerrahi eldivenlerde kullanılan nişasta tozları 35.05’te yer alır.",
  ["I ve II", "I, III ve IV", "II ve III", "I, II ve IV", "III ve IV"], "I, III ve IV",
  "Önjelatinleşmiş nişasta, esterleşmiş nişastalar arasında sayılan nişasta nitratları ve formaldehit veya epiklorhidrin ile işlem görmüş nişasta (cerrahi eldiven tozları) tadil edilmiş nişasta olarak 35.05’tedir. Hazırlanmamış nişasta ise 35.05 Açıklama Notunda hariç tutulup 11.08’e gönderilir (II yanlış).",
  "35.05 Açıklama Notu ve hariç (a).")

# 23
Q(CC, "35.07 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Mayalar enzim içerdikleri için 35.07’de yer alır. II. Kokarboksilaz gibi koenzimler 35.07’de yer alır. III. Peynir mayası, standardizasyon için katılan tuzları ve gliserol gibi koruyucuları içerse de 35.07’de kalır. IV. Sadece suda kısmen eriyebilen kurutulmuş lateks halindeki papain 13.02’de yer alır.",
  ["I ve II", "II ve III", "I, III ve IV", "Yalnız III", "III ve IV"], "III ve IV",
  "Peynir mayası tuz ve koruyucu madde içerebilir ve 35.07’de kalır (III doğru); kurutulmuş lateks halindeki papain 13.02’dedir (IV doğru). Mayalar 21.02’de (I yanlış), kokarboksilaz ve kozimaz gibi koenzimler Fasıl 29’dadır (II yanlış).",
  "35.07 Açıklama Notu ve hariç tutmalar; Fasıl 35 Not 1(a).")

# 24
Q(SN, "Bir gıda üreticisinin ithal ettiği ürün yağı alınmış soya unundan ekstraksiyon yoluyla elde edilmiştir; çeşitli soya proteinlerinin karışımından oluşur, protein içeriği ağırlıkça %92’dir ve toz halindedir. Bu ürün hangi tarife pozisyonunda sınıflandırılır?",
  ["35.04", "21.06", "12.08", "23.04", "35.02"], "35.04",
  "35.04 Açıklama Notu, bir bitkisel maddeden (yağı alınmış soya unu gibi) ekstraksiyonla elde edilen ve protein içeriği %90’dan az olmayan protein izolatlarını “diğer proteinli maddeler” arasında sayar. Yağı alınmış soya unundan bazı maddelerin giderilmesiyle elde edilen konsantreler ise 21.06’dadır; soya unu 12.08’e, küspe 23.04’e aittir. 35.02 albüminleri kapsar.",
  "35.04 Açıklama Notu (B) ve hariç (a).")

# 25
Q(SN, "Esası 39.01 ila 39.13 pozisyonlarındaki polimerler olan, ayrıca Fasıl 39 ürünlerine katılmasına izin verilmeyen mumlar ve reçine esterleri içeren, özel olarak yapıştırıcı olarak formüle edilmiş ve 20 kg’lık varillerde sunulan bir müstahzar hangi tarife pozisyonunda sınıflandırılır?",
  ["35.06", "32.08", "38.24", "39.05", "32.14"], "35.06",
  "35.06 Açıklama Notu (B), 39.01–39.13 polimerlerinden oluşan ve Fasıl 39’daki ürünlere katılmasına izin verilenler dışında ek maddeler (mumlar, reçine esterleri, modifiye edilmemiş doğal şellak gibi) içeren, yapıştırıcı olarak özel formüle edilmiş müstahzarları kapsar; perakende şartı aranmaz. Polimerlerin yalnızca çözelti veya dispersiyonları Fasıl 39 veya 32.08’de, macunlar 32.14’te kalır.",
  "35.06 Açıklama Notu (B)(iv) ve hariç tutmalar.")

modul = {
    "tur": "fasil",
    "fasil": 35,
    "baslik": "Albüminoid maddeler; değişikliğe uğramış nişasta esaslı ürünler; tutkallar; enzimler",
    "bolum": "VI",
    "oz": {
        "vurgu": "Fasıl 35, proteinler (kazein, albümin, jelatin, pepton ve diğer proteinler), tadil edilmiş nişastalar, tutkallar ve enzimlerden oluşur. Sınavdaki temel test, eşyanın Not 1’deki hariç tutmalara (maya, kan fraksiyonu, sertleştirilmiş protein) takılıp takılmadığı ve tutkalların kaynağına mı yoksa perakende sunumuna mı (net 1 kg) göre ayrıldığıdır.",
        "maddeler": [
            "Proteinler sırayla ayrılır: kazein 35.01, albümin 35.02, jelatin ve hayvansal tutkal 35.03, pepton ve başka yerde yer almayan proteinler 35.04.",
            "Dekstrin ölçütü: kuru maddede dekstroz olarak indirgen şeker %10 veya daha az; fazlası 17.02.",
            "Kazein, hayvansal ve nişasta esaslı tutkallar kendi pozisyonlarındadır; net 1 kg’ı geçmeyen perakende tutkal ambalajı hepsini 35.06’ya çeker (Bölüm VI Not 2).",
            "Enzimler ve başka yerde yer almayan müstahzar enzimler 35.07’dedir; maya, koenzim, ilaç ve yıkama enzimi fasıl dışıdır.",
            "Sertleştirilmiş proteinler (kazein, jelatin) 39.13’e; kalıplanmış veya dikdörtgen dışı kesilmiş sertleştirilmemiş jelatin 96.02’ye gider."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Not 1 hariç tutması mı? (maya, kan fraksiyonu/ilaç, ön dabaklama müstahzarı, yıkama enzimi, sertleştirilmiş protein, baskı jelatini)", "<b>21.02</b> · <b>Fasıl 30</b> · <b>32.02</b> · <b>Fasıl 34</b> · <b>39.13</b> · <b>Fasıl 49</b>"],
            ["2", "Tutkal/yapıştırıcı olarak perakende satış için net 1 kg’ı geçmeyen ambalajda mı?", "<b>35.06</b> (Bölüm VI Not 2)"],
            ["3", "Kazein, kazeinat, kazein türevi veya kazein tutkalı mı?", "<b>35.01</b> (kıymetli metal kazeinatı <b>28.43</b>)"],
            ["4", "Albümin, albüminat veya kuru maddede %80’den fazla peyniraltı suyu proteini içeren konsantre mi?", "<b>35.02</b> (%80 veya altı <b>04.04</b>)"],
            ["5", "Jelatin (dikdörtgen/kare yaprak dahil), jelatin türevi, katı ihtiyokol veya hayvansal tutkal mı?", "<b>35.03</b> (başka şekilde kesilmiş/kalıplanmış <b>96.02</b>)"],
            ["6", "Pepton, başka yerde yer almayan protein (zein, keratin, izolat) veya deri tozu mu?", "<b>35.04</b>"],
            ["7", "Dekstrin, tadil edilmiş nişasta veya nişasta/dekstrin esaslı tutkal mı?", "<b>35.05</b> (işlenmemiş <b>11.08</b> · şeker %10’dan fazla <b>17.02</b>)"],
            ["8", "Enzim, enzim konsantresi veya başka yerde yer almayan müstahzar enzim mi?", "<b>35.07</b>"],
            ["9", "Başka yerde yer almayan müstahzar tutkal veya yapıştırıcı mı? (gluten, silikat, polimer, kauçuk esaslı)", "<b>35.06</b>"]
        ],
        "dipnot": "* 2. satır kazein, hayvansal ve nişasta esaslı tutkallara da uygulanır: bunlar perakende 1 kg’lık ambalajda ise 35.01, 35.03 veya 35.05 yerine 35.06’ya gider."
    },
    "pozisyon_haritasi": [
        ["35.01", "Kazeinler, kazeinatlar, kazein tutkalları", "Süt proteini; suda çözünmez", "Asit kazein, sodyum kazeinat"],
        ["35.02", "Albüminler ve albüminatlar", "%80’den fazla peyniraltı suyu proteini", "Yumurta akı tozu, peyniraltı suyu protein konsantresi"],
        ["35.03", "Jelatin, ihtiyokol, hayvansal tutkallar", "Dikdörtgen/kare yaprak; kazein tutkalı hariç", "Yaprak jelatin, kemik tutkalı"],
        ["35.04", "Peptonlar; diğer proteinler; deri tozu", "Başka yerde yer almayan protein", "Zein, soya protein izolatı"],
        ["35.05", "Dekstrinler, tadil edilmiş nişastalar, nişasta tutkalları", "İndirgen şeker %10 veya daha az", "Maltodekstrin, eterleşmiş nişasta"],
        ["35.06", "Müstahzar tutkallar; perakende tutkallar", "Net 1 kg’ı geçmeyen perakende ambalaj", "Tüp yapıştırıcı, Viyana tutkalı"],
        ["35.07", "Enzimler; müstahzar enzimler", "Canlı hücre kaynaklı katalizör", "Peynir mayası, pepsin, amilaz"]
    ],
    "notlar": [
        ["Bölüm VI Not 1(B)", "28.43, 28.46 veya 28.52 tanımına uyan ürünler Bölüm VI’nın başka pozisyonuna girmez; örneğin gümüş kazeinat 35.01’de değil 28.43’tedir."],
        ["Bölüm VI Not 2", "Ölçülü dozlarda veya perakende satış için hazırlanmış olması nedeniyle 35.06’ya giren ürünler başka pozisyona girmez; tutkal olarak perakende satış için hazırlanmış dekstrin 35.05’te değil 35.06’dadır."],
        ["Fasıl 35 Not 1", "Fasıl dışı: (a) mayalar (21.02); (b) kan fraksiyonları (tedavi veya korunmada kullanılmak üzere hazırlanmamış kan albümini <b>hariç</b>), Fasıl 30’daki ilaçlar ve diğer ürünler; (c) ön dabaklamada kullanılan enzimli müstahzarlar (32.02); (d) Fasıl 34’teki ıslatıcı veya yıkayıcı enzimli müstahzarlar; (e) sertleştirilmiş proteinler (39.13); (f) baskı sanayiinde kullanılan jelatin ürünler (Fasıl 49)."],
        ["Fasıl 35 Not 2", "“Dekstrin”: nişastanın parçalanmasıyla elde edilen ve dekstroz olarak ifade edilen indirgen şeker miktarı kuru madde üzerinden <b>%10 veya daha az</b> olan ürün. %10’dan fazla olanlar 17.02’dedir."],
        ["35.01 Açıklama Notu", "Kazein suda çözünmez, alkalilerde çözünür. Kazein tutkalları kalsiyum kazeinattan veya kazein-tebeşir karışımına az miktar boraks/amonyum klorür katılarak yapılır. Hariç: “bitkisel kazein” (35.04), net 1 kg’ı geçmeyen perakende kazein tutkalı (35.06), sertleştirilmiş kazein (39.13)."],
        ["35.02 Açıklama Notu", "Peyniraltı suyu proteini içeriği nitrojen × <b>6,38</b> ile hesaplanır; kuru maddede %80’den fazla ise 35.02, %80 veya daha az ise 04.04. Hariç: kurutulmuş kan (05.11), tedavi veya korunma için hazırlanmış kan albümini (Fasıl 30)."],
        ["35.03 Açıklama Notu", "Yaprak jelatin <b>dikdörtgen (kare dahil)</b> ise yüzeyi işlenmiş/boyanmış olsa da burada; başka şekilde kesilmiş veya kalıplanmış/oyulmuş sertleştirilmemiş jelatin 96.02’de. Hariç: kazein tutkalı (35.01), perakende tutkal (35.06), jelatin esaslı kopya patı (38.24), sertleştirilmiş jelatin (39.13)."],
        ["35.04 Açıklama Notu", "Protein izolatlarının protein içeriği <b>%90’dan az değildir</b>. Tanen tayininde kullanılan deri tozu burada; değersiz kromlu deri tozu/unu 41.15’te. Hariç: gıda katkısı protein hidrolizatları ve soya konsantreleri (21.06), nükleik asitler (29.34), fibrinojen ve kan globülinleri (30.02), enzimler (35.07)."],
        ["35.05 Açıklama Notu", "Isı, kimyasal madde veya enzimle dönüştürülmüş, oksitlenmiş, esterleşmiş, eterleşmiş, çapraz bağlı nişastalar ve nişasta/dekstrin esaslı tutkallar. Hariç: hazırlanmamış nişasta (11.08), indirgen şekeri %10’u geçen ürünler (17.02), perakende tutkal (35.06), nişasta esaslı müstahzar haşıl ve apreler (38.09)."],
        ["35.06 Açıklama Notu", "Perakende kısmı: net <b>1 kg’ı geçmeyen</b> ambalaj; birlikte paketlenmiş küçük fırça tutkalla sınıflandırılır; başka kullanımları da olan ürünler (dekstrin, metil selüloz) ambalajda yalnız tutkal olarak satışa işaret varsa buradadır. Diğer kısım: gluten tutkalları, silikat esaslı, polimer veya kauçuk esaslı müstahzar yapıştırıcılar. Hariç: ökse (13.02), karışmamış silikat (28.39), polimer çözeltileri (Fasıl 39, 32.08), kauçuk çözeltileri (Fasıl 40), macunlar (32.14), maça bağlayıcıları (38.24)."],
        ["35.07 Açıklama Notu", "Enzim: canlı hücrelerin ürettiği, kendi yapısı değişmeden reaksiyonları başlatıp düzenleyen organik madde. Saf enzimler, enzimatik konsantreler ve müstahzar enzimler (et yumuşatıcı, içecek berraklaştırıcı, haşıl çıkarıcı) buradadır. Malt hülasası 19.01’de, kurutulmuş lateks papain 13.02’de. Hariç: mayalar (21.02), koenzimler (Fasıl 29), 30.01–30.02 ürünleri, ilaçlar."]
    ],
    "sinir_komsulari": [
        ["Peyniraltı suyu protein konsantresi (kuru maddede %80 veya daha az)", "04.04", "35.02 eşiğinin altında"],
        ["Kurutulmuş kan", "05.11", "“Kan albümini” diye tarif edilse de 35.02 dışı"],
        ["Hazırlanmamış nişasta", "11.08", "Tadil edilmemiş"],
        ["Kurutulmuş lateks halinde papain; ökse", "13.02", "Bitkisel öz ve hülasa"],
        ["Glikoz şurubu gibi indirgen şekeri %10’u aşan nişasta ürünleri", "17.02", "Fasıl 35 Not 2"],
        ["Malt hülasası", "19.01", "Malt enzimleri yalnız amilaz olarak 35.07’de"],
        ["Bira mayası, ekmek mayası", "21.02", "Fasıl 35 Not 1(a)"],
        ["Gıda katkısı protein hidrolizatı; soya protein konsantresi", "21.06", "35.04 hariç tutması"],
        ["Fibrinojen, kan globülini, tedavi amaçlı kan albümini, mikroorganizma kültürü", "30.02 / Fasıl 30", "Fasıl 35 Not 1(b)"],
        ["Ön dabaklama enzim müstahzarı / enzimli deterjan", "32.02 / Fasıl 34", "Fasıl 35 Not 1(c), (d)"],
        ["Jelatin esaslı kopya patı; dökümhane maça bağlayıcısı", "38.24", "35.03 ve 35.06 hariç tutmaları"],
        ["Nişasta veya dekstrin esaslı mensucat, kağıt apreleri", "38.09", "35.05 hariç tutması"],
        ["Sertleştirilmiş kazein, sertleştirilmiş jelatin", "39.13", "Fasıl 35 Not 1(e)"],
        ["Jelatin kapsül, disk şeklinde jelatin, kalıplanmış jelatin eşya", "96.02", "35.03 Açıklama Notu"],
        ["Baskılı jelatin kartpostal", "Fasıl 49", "Fasıl 35 Not 1(f)"]
    ],
    "tuzaklar": [
        "<b>Peynir mayası maya değildir.</b> Rennin bir enzimdir → 35.07; bira ve ekmek mayası ise 21.02.",
        "<b>“Kan albümini” etiketi her zaman albümin demek değildir.</b> Kurutulmuş kan 05.11’de; tedavi amaçlı hazırlanmamış gerçek kan albümini 35.02’de; tedavi amaçlı olan Fasıl 30’da.",
        "<b>%80 ve %90 eşiklerini karıştırmayın.</b> Peyniraltı suyu proteini konsantresi %80’den fazla ise 35.02; bitkisel protein izolatı en az %90 protein içerir ve 35.04’tedir.",
        "<b>Dekstrin %10 şeker sınırıyla tanımlanır.</b> Maltodekstrin bu sınırı aşarsa 17.02’ye geçer.",
        "<b>Tutkalda önce perakende testine bakın.</b> Kazein, hayvansal ve nişasta tutkalları dökme ise kendi pozisyonlarında, net 1 kg’ı geçmeyen perakende ambalajda ise 35.06’dadır.",
        "<b>Jelatinin şekli pozisyon değiştirir.</b> Dikdörtgen/kare yaprak 35.03; disk, kapsül veya kalıplanmış eşya 96.02; sertleştirilmiş jelatin 39.13; baskılı jelatin Fasıl 49.",
        "<b>Sertleştirilmiş protein plastiktir.</b> Sertleştirilmiş kazein ve diğer sertleştirilmiş proteinler 39.13’tedir.",
        "<b>Kıymetli metal tuzu öncelik alır.</b> Gümüş kazeinat 35.01’de değil 28.43’te (Bölüm VI Not 1).",
        "<b>Yapıştırıcı gibi kullanılan her ürün 35.06 değildir.</b> Karışmamış silikat 28.39, ökse 13.02, polimer çözeltisi Fasıl 39 veya 32.08, kauçuk çözeltisi Fasıl 40."
    ],
    "hafiza": {
        "kanca": "KA – AL – JE – PE – DEK – TUT – EN",
        "aciklama": "<b>KA</b>zein 35.01 · <b>AL</b>bümin 35.02 · <b>JE</b>latin 35.03 · <b>PE</b>pton ve diğer proteinler 35.04 · <b>DEK</b>strin ve tadil nişasta 35.05 · <b>TUT</b>kal (müstahzar/perakende) 35.06 · <b>EN</b>zim 35.07. Görsel benzetme: bir mutfak tezgâhında sırayla süt (kazein), yumurta akı (albümin), kemik suyu jölesi (jelatin), sindirilmiş et (pepton) ve nişasta durur; tezgâhın ucunda bir tüp yapıştırıcı ve bir şişe enzim vardır."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az sayıda yer almıştır; daha çok “hangi pozisyonda” ve “aynı fasılda yer almaz” kalıplarında seçenek olarak kullanılmıştır.",
        "Jelatin kapsüllerin 35.03’te değil, sertleştirilmemiş jelatinden mamul eşya olarak 96.02’de yer aldığı (35.03 çeldirici).",
        "Jelatin, enzim ve sertleştirilmiş protein üçlüsünde sertleştirilmiş proteinin 39.13’e gitmesi; Fasıl 35 Not 1(e) bilgisinin “aynı fasılda sınıflandırılmaz” sorusunda kullanılması.",
        "Tedavi veya korunma amacıyla hazırlanmamış kan albümininin Fasıl 30’da sınıflandırılmadığı (Fasıl 35 Not 1(b) istisnası).",
        "Ayakkabı boyası sorusunda 35.01’in çeldirici olarak yer alması: kazein tutkalının boyacılıkla ilişkisinin karıştırılması."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveline göre jelatin kapsüller hangi tarife pozisyonundadır?",
            "secenekler": ["96.02", "35.03", "05.11", "38.24"],
            "cevap": "A",
            "aciklama": "Eczacılık ürünleri için sertleştirilmemiş jelatinden kapsüller, kalıplanmış jelatin eşya olarak 96.02’de yer alır. 35.03 yalnızca dikdörtgen veya kare yaprak halindeki jelatini kapsar."
        },
        {
            "soru": "Aşağıda belirtilen ürünlerden hangisi, Eczacılık ürünlerinin yer aldığı 30. fasılda <b>sınıflandırılmaz</b>?",
            "secenekler": ["Kızamık aşısı", "Alçılı sargı bezi", "Tedavi edici veya koruyucu olarak hazırlanmamış kan albümini", "Serum"],
            "cevap": "C",
            "aciklama": "Fasıl 35 Not 1(b), kan fraksiyonlarını Fasıl 35 dışında bırakırken tedavi veya korunmada kullanılmak üzere hazırlanmamış kan albüminini istisna tutar; bu ürün 35.02’de sınıflandırılır."
        }
    ],
    "ozet": [
        "Not 1 dışı: maya 21.02, kan fraksiyonu ve ilaç Fasıl 30, ön dabaklama 32.02, yıkama enzimi Fasıl 34, sertleştirilmiş protein 39.13, baskı jelatini Fasıl 49.",
        "Proteinler: kazein 35.01 · albümin 35.02 (%80’den fazla peyniraltı suyu proteini) · jelatin 35.03 · pepton ve diğerleri 35.04 (izolat en az %90).",
        "Dekstrin = indirgen şeker %10 veya daha az; fazlası 17.02; tadil nişastalar ve nişasta tutkalları 35.05.",
        "Net 1 kg’ı geçmeyen perakende tutkal ambalajı her tutkalı 35.06’ya çeker; dökme müstahzar yapıştırıcılar da 35.06.",
        "Enzimler ve müstahzar enzimler 35.07; maya, koenzim ve malt hülasası dışarıda.",
        "Jelatin dikdörtgen yaprak ise 35.03, başka şekil veya kalıplanmış eşya ise 96.02."
    ],
    "sorular": SORULAR
}

if __name__ == "__main__":
    print(Counter(q["cevap"] for q in SORULAR), len(SORULAR))
    print("".join(q["cevap"] for q in SORULAR))
    out = os.path.join(KITAP, "data", "fasil_35.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(modul, f, ensure_ascii=False, indent=1)
    print("yazıldı:", out)
