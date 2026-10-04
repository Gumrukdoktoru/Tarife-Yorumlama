#!/usr/bin/env python3
# Fasıl 36 modülü üreteci
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
Q(E4, "Tarife Cetveline göre, potasyum nitrat, kükürt ve odun kömürünün iyice karıştırılmasıyla elde edilen ve av barutu olarak kullanılan, eşit büyüklükte yuvarlak taneler halindeki kara barut hangi pozisyonda sınıflandırılır?",
  ["36.02", "36.01", "36.03", "28.34", "93.06"], "36.01",
  "Kara barut (tüfek barutu), 36.01 Açıklama Notunda silah barutlarının ilk örneği olarak sayılır; av barutu ve madencilik barutu olarak kullanılır. 36.02 silah barutu dışındaki müstahzar patlayıcıları, 36.03 fitil ve kapsülleri kapsar; 28.34 izole anorganik nitratların, 93.06 mühimmatın yeridir.",
  "36.01 Açıklama Notu (A).")

# 2
Q(E4, "Madencilikte ve taş ocaklarında kullanılan, amonyum nitrat ve akaryakıttan oluşan patlayıcı karışım (ANFO) hangi tarife pozisyonunda yer alır?",
  ["36.02", "31.02", "28.34", "36.01", "27.10"], "36.02",
  "36.02 Açıklama Notu, esasını amonyum nitrat teşkil eden patlayıcı karışımlar arasında ammonal, amatol ve amonyum nitrat yakıtını (ANFO) ismen sayar. Silah barutundan daha şiddetli reaksiyon veren bu karışımlar 36.01’e girmez; bileşenlerinden biri gübre veya akaryakıt olsa da karışım patlayıcı olarak 36.02’dedir.",
  "36.02 Açıklama Notu (3).")

# 3
Q(E4, "Dokumaya elverişli maddeden yapılmış, katran emdirilmiş ince bir kılıfın içine boydan boya kara barut doldurulmuş, alevi ateşleyiciye iletmeye yarayan emniyet fitili (Bickford fitili) hangi pozisyonda sınıflandırılır?",
  ["36.04", "36.01", "56.07", "36.03", "93.06"], "36.03",
  "36.03 pozisyon metni fitilleri ismen sayar; Açıklama Notu emniyet fitillerini (yavaş fitiller veya Bickford fitilleri) dokumaya elverişli kılıf içine doldurulmuş kara barut olarak tarif eder. İçindeki kara barut eşyayı 36.01’e, kılıfı ise 56.07’ye götürmez.",
  "36.03 pozisyon metni ve Açıklama Notu (A).")

# 4
Q(E4, "Denizde tehlike anında ışık ve duman yoluyla işaret vermek için kullanılan tehlike işareti roketi Tarife Cetvelinde hangi pozisyonda yer alır?",
  ["36.03", "93.06", "36.02", "85.31", "36.04"], "36.04",
  "36.04, şenlik fişekleri yanında işaret fişekleri, sis işaretleri ve diğer pirotekni eşyasını kapsar; Açıklama Notu denizde kullanılan tehlike işareti roketlerini ses veya ışık sinyali veren teknik araçlar arasında sayar. Patlayıcı ateşleme aksesuarları 36.03’te, mühimmat 93.06’dadır.",
  "36.04 pozisyon metni ve Açıklama Notu (B)(a).")

# 5
Q(E4, "Seryum ile demirin alaşımından yapılmış, sigara çakmaklarına takılan, perakende satış için kartela üzerine dizilmiş küçük silindir şeklindeki çakmak taşları hangi pozisyonda sınıflandırılır?",
  ["96.13", "28.05", "36.06", "72.02", "36.05"], "36.06",
  "36.06 pozisyon metni ferro-seryum ve diğer piroforik alaşımları “her şekilde” kapsar; Açıklama Notu mekanik ateşleyiciler için küçük silindir veya çubuk şeklindeki çakmak taşlarının perakende ambalajda olsun olmasın burada olduğunu belirtir. Çakmak aksamı olmalarına rağmen 96.13’e girmezler.",
  "36.06 pozisyon metni ve Açıklama Notu (I).")

# 6
Q(OT, "Aşağıdakilerden hangisi Tarife Cetvelinin 36. faslında <b>sınıflandırılmaz</b>?",
  ["Nitrogliserol esaslı dinamit", "Kimyasal olarak belirli bir yapıda, izole halde trinitrotoluen", "Bengal kibriti",
   "Stearin emdirilmiş dokumaya elverişli saplı mum kibriti", "Pentrit (PETN) içeren infilak kapsülü"],
  "Kimyasal olarak belirli bir yapıda, izole halde trinitrotoluen",
  "Fasıl 36 Not 1, Not 2(a) ve (b) dışında kimyasal olarak belirli yapıda izole bileşikleri fasıl dışında bırakır; 36.02 Açıklama Notu trinitrotolueni 29.04 örneğiyle anar. Dinamit 36.02’de, Bengal kibriti pirotekni eşyası olarak 36.04’te, mum kibritleri 36.05’te, infilak kapsülü 36.03’tedir.",
  "Fasıl 36 Not 1; 36.02 Açıklama Notu, son paragraf.")

# 7
Q(OT, "Aşağıdakilerden hangisi 36.03 pozisyonunda <b>yer almaz</b>?",
  ["PETN doldurulmuş infilak fitili", "Kartuşların alt kısmına yerleştirilen ağız otu kapsülü", "Plastik halkalar halinde oyuncak tabanca kapsülü",
   "Entegre devre zamanlayıcısı içeren elektronik infilak ettirici", "Sülfürik asit ve potasyum klorat içeren kimyasal ateşleyici"],
  "Plastik halkalar halinde oyuncak tabanca kapsülü",
  "36.03 Açıklama Notu, oyuncak tabanca kapsüllerini ve madenci lambalarında kullanılan parafinli amors şeritlerini hariç tutarak 36.04’e gönderir; bunlar pirotekni oyuncaklarıdır. İnfilak fitilleri, ağız otları, elektronik infilak ettiriciler ve kimyasal ateşleyiciler 36.03’te sayılmıştır.",
  "36.03 Açıklama Notu, hariç (a); 36.04 Açıklama Notu (A)(2).")

# 8
Q(OT, "Aşağıdakilerden hangisi 36.04 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Doluya karşı roket", "Noel fişeği", "Kimyasal ışıldama aracılığıyla ışık veren çubuk", "Demiryollarında kullanılan sis işaret fişeği",
   "Boru hatlarında sızıntı testi için duman üretici tertip"],
  "Kimyasal ışıldama aracılığıyla ışık veren çubuk",
  "36.04 Açıklama Notu, kimyasal ışıldama aracılığıyla ışık etkisi üreten eşyayı hariç tutup 38.24’e gönderir; bunlar yanma veya patlama ile değil kimyasal ışıldama ile çalışır. Doluya karşı roketler, Noel fişekleri, demiryolu sis işaretleri ve sızıntı testi duman üreticileri pirotekni eşyası olarak 36.04’tedir.",
  "36.04 Açıklama Notu, hariç (b).")

# 9
Q(OT, "Aşağıdakilerden hangisi 36.06 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Demir tozunun bir katalizörle oksidasyonu sonucu alevsiz ısı üreten tek kullanımlık el ısıtıcısı",
   "Yakıt olarak kullanılmak üzere tablet haline getirilmiş metaldehit", "Sabun ve selüloz türevleri katılmış katılaştırılmış alkol",
   "Reçine ve zift emdirilmiş, saplı reçineli meşale", "Gazyağı ve su ilave edilmiş üre-formaldehit reçinesinden ateş yakıcı"],
  "Demir tozunun bir katalizörle oksidasyonu sonucu alevsiz ısı üreten tek kullanımlık el ısıtıcısı",
  "36.06 Açıklama Notu, ışık ve alev üretmeksizin ekzotermik bir reaksiyonla ısı veren tek kullanımlık el ve ayak ısıtıcılarını hariç tutar ve 38.24’e gönderir. Tablet halindeki metaldehit, katılaştırılmış alkol, reçineli meşaleler ve ateş yakıcılar Fasıl 36 Not 2’deki ateş alıcı maddelerdendir.",
  "Fasıl 36 Not 2; 36.06 Açıklama Notu (II).")

# 10
Q(FA, "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
  ["Nitroselüloz esaslı dumansız barut", "Kara barut", "Pamuk barutu (nitroselüloz)", "Amonyum nitrat esaslı emülsiyon patlayıcı", "TNT ile PETN karışımı pentolit"],
  "Pamuk barutu (nitroselüloz)",
  "36.01 Açıklama Notu, pamuk barutu gibi nitroselülozu (selüloz nitratları) hariç tutarak 39.12’ye gönderir. Nitroselüloz esaslı dumansız barut ve kara barut 36.01’de, emülsiyon patlayıcı ve pentolit 36.02’de, yani Fasıl 36’dadır. Tuzak, adında “barut” geçen ürünü Fasıl 36 sanmaktır.",
  "36.01 Açıklama Notu, hariç (c).")

# 11
Q(FA, "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir tarife pozisyonunda yer alır?",
  ["Madenci lambalarında kullanılan parafinli amors şeridi", "İnfilak fitili", "Emniyet fitili", "Elektrikli ateşleyici", "Friksiyonlu ağız otu (ateşleme tüpü)"],
  "Madenci lambalarında kullanılan parafinli amors şeridi",
  "İnfilak fitilleri, emniyet fitilleri, elektrikli ateşleyiciler ve ağız otları 36.03’tedir. Madenci lambalarında kullanılan parafinli amors şeritleri veya ruloları ise 36.03 Açıklama Notunda hariç tutulup pirotekni eşyası olarak 36.04’e gönderilir.",
  "36.03 Açıklama Notu, hariç (a).")

# 12
Q(FA, "Aşağıdaki eşya ikililerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda sınıflandırılır?",
  ["Toz halinde metaldehit – tablet halinde yakıt metaldehit", "Mum kibriti – Bengal kibriti",
   "Fotoğrafçılıkta kullanılan flaş ışığı maddesi – uçaklarda kullanılan foto-flaş fişeği",
   "Ferro-seryum çakmak taşı – 250 cm3’lük kaba konulmuş çakmak doldurma gazı", "Briket halinde aglomere edilmiş testere talaşı – parafin emdirilmiş kağıttan ateş yakıcı"],
  "Ferro-seryum çakmak taşı – 250 cm3’lük kaba konulmuş çakmak doldurma gazı",
  "Piroforik alaşımlar ve 300 cm3’ü aşmayan kaplardaki çakmak yakıtları 36.06’dadır. Diğer ikililer ayrılır: toz metaldehit 29.12 / tablet yakıt 36.06; mum kibriti 36.05 / Bengal kibriti 36.04; fotoğraf flaş maddesi 37.07 / foto-flaş fişeği 36.04; talaş briketi 44.01 / ateş yakıcı 36.06.",
  "Fasıl 36 Not 2; 36.04, 36.05 ve 36.06 Açıklama Notları.")

# 13
Q(FA, "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir tarife pozisyonunda sınıflandırılır?",
  ["Oyuncak tabancalar için şerit halinde kapsül", "Sihirli mum", "Perçinleme aletlerinde kullanılan, patlayıcı içeren boş fişek",
   "Bengal maytabı", "Noel fişeği"],
  "Perçinleme aletlerinde kullanılan, patlayıcı içeren boş fişek",
  "Oyuncak tabanca kapsülleri, sihirli mumlar, Bengal maytapları ve Noel fişekleri pirotekni eşyası olarak 36.04’tedir. Perçinleme aletleri veya motor çalıştırma için kullanılan, patlayıcı içeren boş fişekler ise 36.04’ten hariç tutulup 93.06’ya gönderilir.",
  "36.04 Açıklama Notu (A) ve hariç (c).")

# 14
Q(FN, "Fasıl 36 Not 2’ye göre çakmaklarda veya ateşlemeye yarayan benzeri aletlerde kullanılan türden sıvı veya sıvılaştırılmış akaryakıtların “ateş alıcı madde” sayılarak 36.06’da yer alması için konuldukları kapların hacmi en fazla ne olmalıdır?",
  ["100 cm3", "250 cm3", "500 cm3", "300 cm3", "1.000 cm3"], "300 cm3",
  "Not 2(b), çakmaklarda veya benzeri ateşleme aletlerinde kullanılan türden olup 300 cm3 veya daha az hacimdeki kaplara konulmuş sıvı veya sıvılaştırılmış akaryakıtları ateş alıcı madde sayar. Bu sınırı aşan kaplardaki yakıtlar 36.06’ya girmez; çakmak aksamı olan doldurulabilir kartuşlar ise 96.13’tedir.",
  "Fasıl 36 Not 2(b); 36.06 Açıklama Notu (II)(A).")

# 15
Q(FN, "Fasıl 36 Not 1 ve Not 2 ile ilgili aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
  ["Kimyasal olarak belirli yapıdaki izole bileşikler kural olarak Fasıl 36’ya dahil değildir.",
   "Yakıt olarak kullanılmak üzere tablet şeklinde hazırlanmış hekzametilentetramin, kimyasal olarak belirli olsa da 36.06’da yer alabilir.",
   "36.06’daki “ateş alıcı maddeler” tabiri yalnızca Not 2’de sayılan ürünleri kapsar.",
   "Reçineli meşaleler ve ateş yakıcı maddeler ateş alıcı maddeler arasında sayılmıştır.",
   "Alkol esaslı yakıtlar ancak sıvı halde iseler ateş alıcı madde sayılır."],
  "Alkol esaslı yakıtlar ancak sıvı halde iseler ateş alıcı madde sayılır.",
  "Not 2(a), alkol esaslı yakıtları ve benzeri müstahzar yakıtları katı veya hamur (yarı katı) halde iken ateş alıcı madde sayar; “katılaştırılmış alkol” buna örnektir. Not 1 kimyasal olarak belirli izole bileşikleri dışarıda bırakır ama Not 2(a) ve (b)’deki ürünleri istisna tutar; Not 2’deki liste sınırlayıcıdır (“yalnızca”).",
  "Fasıl 36 Not 1 ve Not 2.")

# 16
Q(FN, "Fasıl 36 Genel Açıklamalarına göre bu fasıldaki barut ve müstahzar patlayıcı maddeleri tanımlayan özellik hangisidir?",
  ["Yanmaları için gerekli oksijeni havadan alan ve yavaş yanan karışımlar olmaları",
   "Yanmaları için gerekli oksijeni içeren ve yanışlarında birden büyük hacimde, yüksek ısıda gaz oluşturan karışımlar olmaları",
   "Kimyasal olarak belirli yapıda, izole halde bileşikler olmaları",
   "Yalnızca askeri amaçla kullanılan ve mühimmata yerleştirilmiş maddeler olmaları",
   "Sürtünmeyle kıvılcım veren metal alaşımları olmaları"],
  "Yanmaları için gerekli oksijeni içeren ve yanışlarında birden büyük hacimde, yüksek ısıda gaz oluşturan karışımlar olmaları",
  "Genel Açıklamalar barut ve müstahzar patlayıcıları, yanmaları için gerekli oksijeni içeren ve yanışları anında birden büyük hacimde ve yüksek ısıda gaz oluşturan karışımlar olarak tanımlar. İzole bileşikler Fasıl 28–29’a, mühimmat Fasıl 93’e gider; sürtünmeyle kıvılcım veren alaşımlar ise piroforik alaşımlardır (36.06).",
  "Fasıl 36 Genel Açıklamalar.")

# 17
Q(FN, "36.02 Açıklama Notuna göre aşağıdaki kimyasal olarak belirli, izole patlayıcı maddelerden hangisinin sınıflandırıldığı pozisyon <b>yanlış</b> verilmiştir?",
  ["Anorganik nitratlar – 28.34", "Civa fulminat – 28.52", "Trinitrotoluen – 29.04", "Trinitrofenol – 29.08", "Kurşun azür esaslı başlatıcı karışım – 28.52"],
  "Kurşun azür esaslı başlatıcı karışım – 28.52",
  "36.02 Açıklama Notu, kimyasal olarak belirli izole maddeleri patlayıcı olsalar bile dışarıda bırakır ve anorganik nitratları 28.34, civa fulminatı 28.52, trinitrotolueni 29.04, trinitrofenolü 29.08 örnekleriyle anar. Kurşun azür esaslı karışımlar ise bir bileşik değil, primer ve başlatıcı bileşik olarak 36.02’de sayılan müstahzar patlayıcılardır.",
  "36.02 Açıklama Notu (5) ve son paragraf.")

# 18
Q(GYK, "Yakıt olarak kullanılmak üzere tablet şeklinde hazırlanmış metaldehit, kimyasal olarak belirli bir bileşik olmasına rağmen 29.12’de değil 36.06’da sınıflandırılır. Bu sınıflandırma hangi Genel Yorum Kuralına dayanır?",
  ["GYK 2(b)", "GYK 3(a)", "GYK 3(c)", "GYK 4", "GYK 1"], "GYK 1",
  "Sonuç doğrudan Fasıl 36 Not 1’in istisnasından ve Not 2(a)’dan (metaldehit, yakıt olarak tablet, çubuk vb. şekillerde) doğar; pozisyon metni ve notlarla yapılan sınıflandırma GYK 1’dir. Toz veya kristal halindeki metaldehit ise not kapsamı dışında kalır ve 29.12’dedir; GYK 3’e başvurmaya gerek yoktur.",
  "GYK 1; Fasıl 36 Not 1 ve Not 2(a); 36.06 Açıklama Notu (II)(B)(1).")

# 19
Q(GYK, "Perakende satış için şenlik fişeklerinin konulduğu, bu tür eşyanın ambalajında normal olarak kullanılan basit karton kutu, içindeki fişeklerle birlikte 36.04 pozisyonunda sınıflandırılır. Bu durum hangi Genel Yorum Kuralına dayanır?",
  ["GYK 2(a)", "GYK 5(b)", "GYK 3(b)", "GYK 5(a)", "GYK 6"], "GYK 5(b)",
  "GYK 5(b), içindeki eşyayla birlikte sunulan ve o eşyanın ambalajında normal olarak kullanılan ambalaj maddelerinin eşyayla birlikte sınıflandırılmasını öngörür. GYK 5(a), belli bir eşyaya göre şekillendirilmiş ve uzun süre kullanılmaya uygun mahfazalar içindir; basit karton kutu bu niteliği taşımaz.",
  "GYK 5(b); GYK 5(a) Açıklama Notu (I).")

# 20
Q(ES, "Aşağıdaki cümlede boş bırakılan yerlere sırasıyla hangisi gelmelidir? “Metaldehit ve hekzametilentetramin, yakıt olarak kullanılmak üzere tablet, çubuk veya benzeri şekillerde hazırlanmışlarsa ..... pozisyonunda; toz veya kristal gibi diğer şekillerde ise sırasıyla ..... pozisyonlarında yer alır.”",
  ["36.06 – 29.12 ve 29.33", "36.04 – 29.12 ve 29.33", "36.06 – 29.33 ve 29.12", "36.02 – 28.52 ve 29.04", "36.06 – 38.24 ve 29.33"],
  "36.06 – 29.12 ve 29.33",
  "36.06 Açıklama Notu, yakıt olarak tablet, çubuk vb. şekillerde hazırlanmış metaldehit ve hekzametilentetramini ateş alıcı madde olarak 36.06’ya alır; diğer şekillerde (toz veya kristal) olanların sırasıyla 29.12 ve 29.33’te kaldığını belirtir. Sıranın ters verildiği seçenek tuzaktır.",
  "Fasıl 36 Not 2(a); 36.06 Açıklama Notu (II)(B)(1).")

# 21
Q(ES, "Fasıl 36’dan hariç tutulan aşağıdaki ürünler ile yer aldıkları pozisyonlar eşleştirildiğinde hangi seçenek doğru olur? I. Fotoğrafçılıkta kullanılan flaş ışığı maddeleri; II. Kimyasal ışıldama aracılığıyla ışık etkisi üreten eşya; III. Mermi ve fişek kovanları (ağız otu ile mücehhez olsun olmasın); IV. Pamuk barutu gibi nitroselüloz. — a. 93.06 · b. 39.12 · c. 37.07 · d. 38.24",
  ["I-d, II-c, III-a, IV-b", "I-c, II-d, III-b, IV-a", "I-c, II-a, III-d, IV-b", "I-c, II-d, III-a, IV-b", "I-a, II-d, III-c, IV-b"],
  "I-c, II-d, III-a, IV-b",
  "36.04 Açıklama Notu fotoğraf flaş maddelerini 37.07’ye, kimyasal ışıldama eşyasını 38.24’e; 36.03 Açıklama Notu mermi ve fişek kovanlarını 93.06’ya; 36.01 Açıklama Notu nitroselülozu (pamuk barutu) 39.12’ye gönderir.",
  "36.01, 36.03 ve 36.04 Açıklama Notları, hariç tutmalar.")

# 22
Q(CC, "36.02 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Nitrogliserol esaslı karışımlardan oluşan dinamitler 36.02’de yer alır. II. Kimyasal olarak belirli yapıdaki civa fulminat patlayıcı olduğu için 36.02’de yer alır. III. Mineral yağlarda emülsifiye edilmiş alkali nitrat çözeltisinden oluşan “emülsiyon” patlayıcılar 36.02’dedir. IV. Kurşun azür ve tetrazen esaslı primer ve başlatıcı karışımlar 36.02’dedir.",
  ["I ve II", "II ve III", "I, II ve IV", "III ve IV", "I, III ve IV"], "I, III ve IV",
  "Dinamitler, emülsiyon patlayıcılar ve kurşun azür/tetrazen esaslı primer bileşikler 36.02 Açıklama Notunda sayılmıştır (I, III, IV doğru). Civa fulminat kimyasal olarak belirli izole bir bileşik olduğundan 28.52’dedir (II yanlış).",
  "36.02 Açıklama Notu (1), (3), (5) ve son paragraf; Fasıl 36 Not 1.")

# 23
Q(CC, "36.06 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Sigara çakmaklarının aksamını teşkil eden yeniden doldurulabilir kartuşlar, dolu iseler 36.06’da yer alır. II. Ferro-seryum ve diğer piroforik alaşımlar perakende satış için ambalajlanmış olsun olmasın 36.06’dadır. III. Briket halinde aglomere edilmiş testere talaşı ateş yakıcı madde olarak 36.06’dadır. IV. Mineral yağ veya parafin mumu emdirilmiş kağıttan oluşan ateş yakıcılar 36.06’dadır.",
  ["I ve II", "II ve IV", "I, II ve III", "III ve IV", "II, III ve IV"], "II ve IV",
  "Piroforik alaşımlar her şekilde ve perakende ambalajlı olsun olmasın 36.06’dadır (II doğru); mineral yağ veya parafin emdirilmiş kağıt ateş yakıcılar Açıklama Notunda örnek verilmiştir (IV doğru). Çakmak aksamı olan doldurulabilir kartuşlar dolu veya boş 96.13’te (I yanlış), talaş briketleri 44.01’de (III yanlış) yer alır.",
  "36.06 Açıklama Notu (I) ve (II).")

# 24
Q(SN, "Karboksimetilselüloz bağlayıcı ve yanmayı desteklemek için çok az sodyum nitrat katılmış odun kömürü tozundan çubuk haline getirilmiş, giysiler içinde taşınan hemen hemen hava geçirmez bir kutuda yavaş yanarak ısı veren katı yakıt hangi tarife pozisyonunda sınıflandırılır?",
  ["44.02", "38.24", "36.04", "36.06", "36.01"], "36.06",
  "36.06 Açıklama Notu, katı veya yarı katı yakıtlara örnek olarak, karboksimetilselüloz bağlayıcılı ve az miktarda sodyum nitrat katılmış çubuk haline getirilmiş odun kömürü tozunu, giysiler içinde taşınan kutuda yavaş yanan ısı kaynağı olarak açıkça sayar. Alevsiz ekzotermik reaksiyonla çalışan demir tozlu el ısıtıcıları ise 38.24’tedir; tuzak budur.",
  "Fasıl 36 Not 2(a); 36.06 Açıklama Notu (II)(C).")

# 25
Q(SN, "Metal bir tüp içinde elektrikli fünye kafası, yaklaşık 300 mg kurşun azür esaslı bir ilk ateşleyici ve daha güçlü bir patlayıcı olarak PETN bulunan, son derece hassas gecikme sağlayan entegre devre zamanlayıcısıyla donatılmış ve madenlerde dinamiti ateşlemek için kullanılan eşya hangi pozisyonda sınıflandırılır?",
  ["36.03", "85.43", "36.02", "93.06", "85.36"], "36.03",
  "36.03 pozisyon metni elektrikli infilak ettiricileri ismen sayar; Açıklama Notu entegre devre zamanlayıcısı içeren elektronik infilak ettiricileri de bu gruba dahil eder. Elektronik devre içermesi eşyayı Fasıl 85’e, patlayıcı içermesi de 36.02’ye götürmez; 93.06 mühimmatın yeridir.",
  "36.03 pozisyon metni ve Açıklama Notu (F).")

modul = {
    "tur": "fasil",
    "fasil": 36,
    "baslik": "Barut ve patlayıcı maddeler; pirotekni mamulleri; kibritler; piroforik alaşımlar; ateş alıcı maddeler",
    "bolum": "VI",
    "oz": {
        "vurgu": "Fasıl 36, yanmaları için gerekli oksijeni kendisi içeren barut ve patlayıcı karışımları, bunları ateşleyen aksesuarları ve ışık, ses, duman, alev veya kıvılcım üreten eşyayı (pirotekni, kibrit, piroforik alaşım, ateş alıcı maddeler) toplar. Sınavdaki temel test: eşya bir karışım/eşya mı (Fasıl 36), yoksa kimyasal olarak belirli izole bileşik (Fasıl 28–29) veya mühimmat (Fasıl 93) mı?",
        "maddeler": [
            "İtici etki için silah barutu 36.01; daha şiddetli patlayan müstahzar patlayıcı 36.02; ateşleme aksesuarları 36.03.",
            "Işık, ses, duman veren her türlü pirotekni (oyuncak kapsülü, Bengal kibriti dahil) 36.04; sürtünmeyle alev veren kibrit 36.05.",
            "36.06: ferro-seryum ve diğer piroforik alaşımlar her şekilde; “ateş alıcı maddeler” yalnızca Not 2’de sayılanlardır.",
            "Çakmak yakıtında sınır 300 cm3; çakmak aksamı olan doldurulabilir kartuş 96.13.",
            "İzole kimyasal patlayıcılar (TNT, civa fulminat) Fasıl 28–29’da, nitroselüloz 39.12’de, mermi ve fişek kovanları 93.06’dadır."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Kimyasal olarak belirli izole bir bileşik mi? (Not 2(a)/(b) yakıtları hariç)", "<b>Fasıl 28 / 29</b> (ör. TNT <b>29.04</b>, civa fulminat <b>28.52</b>)"],
            ["2", "Mühimmat, mermi/fişek kovanı veya patlayıcılı boş fişek mi?", "<b>93.06</b>"],
            ["3", "Silah barutu mu? (kara barut, dumansız barut, roket barutu)", "<b>36.01</b> (nitroselülozun kendisi <b>39.12</b>)"],
            ["4", "Silah barutu dışında müstahzar patlayıcı mı? (dinamit, TNT karışımı, ANFO, primer karışım)", "<b>36.02</b>"],
            ["5", "Fitil, infilak fitili, ağız otu, infilak kapsülü, ateşleyici veya elektrikli infilak ettirici mi?", "<b>36.03</b>"],
            ["6", "Işık, ses, duman veya alev veren pirotekni eşyası mı? (şenlik/işaret fişeği, oyuncak kapsülü, Bengal kibriti)", "<b>36.04</b>"],
            ["7", "Pürüzlü yüzeye sürtülünce alev veren kibrit mi?", "<b>36.05</b>"],
            ["8", "Piroforik alaşım ya da Not 2’deki ateş alıcı madde mi? (tablet yakıt, katı alkol, ≤ 300 cm3 çakmak yakıtı, meşale, ateş yakıcı)", "<b>36.06</b>"]
        ],
        "dipnot": "* Fotoğraf flaş maddeleri 37.07’ye, kimyasal ışıldama eşyası ve demir tozlu el ısıtıcıları 38.24’e, çakmak aksamı olan kartuşlar 96.13’e gider."
    },
    "pozisyon_haritasi": [
        ["36.01", "Silah barutu", "İtici etki; kara ve dumansız barut", "Av barutu, roket barutu"],
        ["36.02", "Müstahzar patlayıcılar", "Silah barutundan şiddetli; karışım", "Dinamit, ANFO, pentolit"],
        ["36.03", "Fitiller, kapsüller, ateşleyiciler", "Ateşleme aksesuarı", "Bickford fitili, elektronik detonatör"],
        ["36.04", "Şenlik ve işaret fişekleri; pirotekni", "Işık, ses, duman etkisi", "Havai fişek, imdat roketi, oyuncak kapsülü"],
        ["36.05", "Kibritler", "Sürtünmeyle alev; pirotekni hariç", "Tahta kibrit, mum kibriti"],
        ["36.06", "Piroforik alaşımlar; ateş alıcı maddelerden eşya", "Not 2 listesi; 300 cm3", "Çakmak taşı, katı alkol, çakmak gazı"]
    ],
    "notlar": [
        ["Fasıl 36 Not 1", "Not 2(a) veya (b)’de yazılı olanlar hariç, kimyasal olarak belirli bir yapıda bulunan izole bileşikler bu fasla dahil değildir."],
        ["Fasıl 36 Not 2", "36.06’daki “ateş alıcı maddeler” <b>yalnızca</b> şunlardır: (a) yakıt olarak tablet, çubuk vb. şekillerde hazırlanmış metaldehit, hekzametilentetramin ve benzerleri; katı veya hamur halindeki alkol esaslı ve benzeri müstahzar yakıtlar; (b) çakmaklarda veya benzeri ateşleme aletlerinde kullanılan türden, <b>300 cm3 veya daha az</b> hacimli kaplara konulmuş sıvı veya sıvılaştırılmış akaryakıtlar; (c) reçineli meşaleler, ateş yakıcı maddeler ve benzerleri."],
        ["Genel Açıklamalar", "Barut ve müstahzar patlayıcılar: yanmaları için gerekli oksijeni içeren, yanışlarında birden büyük hacimde ve yüksek ısıda gaz oluşturan karışımlar. Fünye, infilak kapsülü ve fitiller ile ışık, ses, duman, alev veya kıvılcım veren eşya da buradadır. Hariç: izole kimyasal bileşikler (Fasıl 28–29), Fasıl 93 mühimmatı."],
        ["36.01 Açıklama Notu", "Kara barut: potasyum veya sodyum nitrat, kükürt ve odun kömürü karışımı. Dumansız barutlar nitroselüloz esaslıdır. Hariç: izole bileşikler, 36.02 patlayıcıları, pamuk barutu gibi nitroselüloz (39.12)."],
        ["36.02 Açıklama Notu", "Silah barutundan daha şiddetli reaksiyon veren karışımlar: dinamitler, TNT/heksojen/PETN esaslı karışımlar (heksolit, pentolit), amonyum nitrat esaslılar (ammonal, amatol, ANFO, bulamaç ve emülsiyon patlayıcılar), klorat/perklorat esaslılar, kurşun azür esaslı primer bileşikler. İzole maddeler hariç: anorganik nitratlar 28.34, civa fulminat 28.52, trinitrotoluen 29.04, trinitrofenol 29.08."],
        ["36.03 Açıklama Notu", "Emniyet fitilleri, infilak fitilleri (PETN), ağız otları (patlayıcı karışım genellikle 10–200 mg), infilak kapsülleri, elektrikli ve kimyasal ateşleyiciler, entegre devre zamanlayıcılı elektronik infilak ettiriciler dahil. Hariç: parafinli amors şeritleri ve oyuncak tabanca kapsülleri (36.04), patlayıcı içermeyen parçalar (niteliğine göre), mermi ve fişek kovanları (93.06)."],
        ["36.04 Açıklama Notu", "Eğlence amaçlı fişekler, pirotekni oyuncakları, işaret ve tehlike roketleri, sis işaretleri, doluya karşı roketler, zirai duman üreticiler, cankurtaran halat roketleri. Hariç: fotoğraf flaş maddeleri (37.07), kimyasal ışıldama eşyası (38.24), perçin aletleri ve motor çalıştırma için boş fişekler (93.06)."],
        ["36.05 Açıklama Notu", "Pürüzlü yüzeye sürtülünce alev veren kibritler (ağaç, mukavva veya mum emdirilmiş tekstil saplı). Bengal kibritleri ve benzeri pirotekni ürünler 36.04’tedir."],
        ["36.06 Açıklama Notu", "Piroforik alaşımlar dökme veya çakmak taşı şeklinde, perakende olsun olmasın buradadır. Çakmak aksamı olan doldurulabilir kartuşlar (dolu veya boş) 96.13’te; toz/kristal metaldehit 29.12, hekzamin 29.33’te; demir tozlu alevsiz el ve ayak ısıtıcıları 38.24’te; talaş briketleri 44.01’de."]
    ],
    "sinir_komsulari": [
        ["İzole anorganik nitratlar; civa fulminat", "28.34 / 28.52", "Fasıl 36 Not 1"],
        ["İzole trinitrotoluen; trinitrofenol", "29.04 / 29.08", "Kimyasal olarak belirli bileşik"],
        ["Toz veya kristal metaldehit; hekzametilentetramin", "29.12 / 29.33", "Yakıt şeklinde değil"],
        ["Fotoğrafçılıkta kullanılan flaş ışığı maddeleri", "37.07", "36.04 hariç tutması"],
        ["Kimyasal ışıldama çubuğu; demir tozlu tek kullanımlık el ısıtıcı", "38.24", "Yanma/patlama yok"],
        ["Nitroselüloz (pamuk barutu)", "39.12", "36.01 hariç tutması"],
        ["Briket halinde testere talaşı", "44.01", "Ateş yakıcı sayılmaz"],
        ["Mermi ve fişek kovanları; perçin aleti ve motor çalıştırma boş fişekleri", "93.06", "Mühimmat"],
        ["Çakmak aksamı olan doldurulabilir kartuş ve gaz haznesi", "96.13", "36.06 hariç tutması"],
        ["Patlayıcı içermeyen kapsül, tüp, elektrikli ateşleme cihazı", "Niteliğine göre", "36.03 hariç tutması"],
        ["Bengal kibriti", "36.04", "Kibrit şeklinde olsa da pirotekni"],
        ["Oyuncak tabanca kapsülü; parafinli amors şeridi", "36.04", "36.03 dışı, pirotekni oyuncağı"]
    ],
    "tuzaklar": [
        "<b>İzole kimyasal patlayıcı Fasıl 36’da değildir.</b> TNT 29.04, trinitrofenol 29.08, civa fulminat 28.52; Fasıl 36 karışımları kapsar.",
        "<b>Adında “barut” geçmesi yetmez.</b> Pamuk barutu (nitroselüloz) 39.12’de; nitroselüloz esaslı dumansız barut ise 36.01’dedir.",
        "<b>Barut iter, patlayıcı parçalar.</b> İtici etki yapan silah ve roket barutları 36.01; daha şiddetli müstahzar patlayıcılar 36.02.",
        "<b>Oyuncak kapsülü ateşleme aksesuarı değildir.</b> Oyuncak tabanca kapsülü ve parafinli amors 36.04; gerçek ağız otu 36.03.",
        "<b>Bengal kibriti kibrit değildir.</b> Sürtünmeyle tutuşsa da pirotekni eşyasıdır → 36.04.",
        "<b>300 cm3 ve çakmak aksamı ayrımı.</b> Çakmak doldurma yakıtı 300 cm3 veya altındaki kapta 36.06; çakmağın parçası olan doldurulabilir kartuş veya hazne 96.13.",
        "<b>Metaldehitte şekil belirleyicidir.</b> Yakıt tableti 36.06; toz veya kristal 29.12.",
        "<b>Isı veren her ürün ateş alıcı değildir.</b> Demir tozunun oksidasyonuyla alevsiz ısı veren el ısıtıcısı 38.24; odun kömürü tozlu yavaş yanan çubuk 36.06.",
        "<b>Işık veren her ürün pirotekni değildir.</b> Fotoğraf flaş maddesi 37.07, kimyasal ışık çubuğu 38.24.",
        "<b>Çakmak taşı çakmak parçası olarak 96.13’e gitmez.</b> Ferro-seryum her şekilde 36.06’dadır."
    ],
    "hafiza": {
        "kanca": "BA – PA – Fİ – Şİ – Kİ – ÇA",
        "aciklama": "<b>BA</b>rut 36.01 · <b>PA</b>tlayıcı 36.02 · <b>Fİ</b>til ve kapsül 36.03 · <b>Şİ</b>şenlik (şenlik fişeği) 36.04 · <b>Kİ</b>brit 36.05 · <b>ÇA</b>kmak taşı ve ateş alıcı 36.06. Görsel benzetme: bir taş ocağında barutu kovana koyar, dinamiti hazırlar, fitili çeker; akşam şenlikte fişek atılır, kibrit çakılır ve çakmak taşıyla ocak yakılır."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda çok az yer almıştır; doğrudan bağlantılı tek konu çakmak yakıtı ve çakmak aksamı ayrımıdır.",
        "Çakmakta kullanılan, LPG ile doldurulmuş plastik gaz haznesinin çakmak aksamı olarak 96.13’te sınıflandırıldığı; 27.11 (gaz) ve 39.26 (plastik eşya) seçeneklerinin çeldirici olarak kullanıldığı.",
        "Soru kalıbı “hangi tarife pozisyonundadır”: yakıtın kendisi (300 cm3’ü aşmayan kapta 36.06) ile çakmağın parçası olan doldurulabilir hazne (96.13) arasındaki farkın bilinmesi.",
        "Tarife sıralaması sorularında (içki – sigara – sigara tabakası – çakmak) çakmağın Fasıl 96’da yer aldığı bilgisi kullanılmıştır; çakmak taşı ve çakmak doldurma yakıtının ise Fasıl 36’da kaldığına dikkat edilmelidir."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Çakmaklarda kullanılan içi sıvılaştırılmış petrol gazı (LPG) ile doldurulmuş plastikten mamul gaz haznesi hangi tarife pozisyonundadır?",
            "secenekler": ["27.07", "27.11", "39.26", "96.13"],
            "cevap": "D",
            "aciklama": "36.06 Açıklama Notu, sigara çakmaklarının aksamını teşkil eden yeniden doldurulabilir kartuşları ve diğer kapları (dolu veya boş) hariç tutarak 96.13’e gönderir. 36.06’ya yalnızca çakmak doldurmaya mahsus, 300 cm3’ü aşmayan kaplardaki yakıtlar girer."
        }
    ],
    "ozet": [
        "Fasıl 36 karışımları kapsar; izole kimyasal patlayıcı Fasıl 28–29, nitroselüloz 39.12, mühimmat Fasıl 93.",
        "36.01 silah barutu (itici), 36.02 müstahzar patlayıcı (dinamit, ANFO, primer karışım), 36.03 fitil-kapsül-ateşleyici.",
        "36.04 tüm pirotekni: şenlik ve işaret fişekleri, oyuncak kapsülleri, Bengal kibriti.",
        "36.05 kibrit; 36.06 ferro-seryum her şekilde ve Not 2’deki ateş alıcı maddeler.",
        "Çakmak yakıtı 300 cm3 veya daha az kapta 36.06; çakmak aksamı olan kartuş 96.13.",
        "Metaldehit tablet 36.06 / toz 29.12; demir tozlu el ısıtıcı ve kimyasal ışık çubuğu 38.24; fotoğraf flaşı 37.07."
    ],
    "sorular": SORULAR
}

if __name__ == "__main__":
    print(Counter(q["cevap"] for q in SORULAR), len(SORULAR))
    print("".join(q["cevap"] for q in SORULAR))
    out = os.path.join(KITAP, "data", "fasil_36.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(modul, f, ensure_ascii=False, indent=1)
    print("yazıldı:", out)
