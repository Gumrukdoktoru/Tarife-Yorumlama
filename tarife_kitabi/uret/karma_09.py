#!/usr/bin/env python3
"""Karma test 9 üreticisi → karma/karma_09.json"""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_09.json")

ESYA = "Eşya → 4’lü pozisyon"
POZ = "Pozisyon → eşya"
OLUM = "Olumsuz teşhis"
FARK = "Farklı/aynı pozisyon veya fasıl"
BUL = "Fasıl/Bölüm bulma"
NOT = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
SIRA = "Sıralama"
YAPI = "Tarife yapısı"

S = []


def q(fasil, tip, soru, secenekler, cevap, gerekce, dayanak):
    S.append({"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
              "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil})


# 1 — Tarife yapısı
q("Genel", YAPI,
  "Türk Gümrük Tarife Cetvelinin bölüm ve fasıl yapısına ilişkin aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
  ["Bir pozisyonun dört rakamlı numarasının ilk iki rakamı, pozisyonun yer aldığı faslı gösterir.",
   "Fasıl 77, Armonize Sistem Nomanklatüründe ileride kullanılmak üzere saklı tutulmuştur.",
   "Bölüm III ve Bölüm XIX, yalnızca birer fasıldan oluşur.",
   "Mobilyalar, oyuncaklar ve sanat eserleri aynı bölümde, Bölüm XX’de yer alır.",
   "Müzik aletleri; optik aletler ve saatlerle aynı bölümde, Bölüm XVIII’de yer alır."],
  "D",
  "İçindekiler listesine göre Bölüm XX (Muhtelif mamul eşya) Fasıl 94–96’dan oluşur; sanat eserleri, koleksiyon "
  "eşyası ve antikalar (Fasıl 97) ayrı bir bölüm olan Bölüm XXI’dedir. Diğer ifadeler doğrudur: Bölüm III yalnız "
  "Fasıl 15’i, Bölüm XIX yalnız Fasıl 93’ü kapsar.",
  "Tarife Cetveli İçindekiler (bölüm ve fasıl listesi).")

# 2 — Fasıl 1
q(1, ESYA,
  "Tarife Cetveline göre, bir çiftlikte tavuk ve hindilerle birlikte yetiştirilen canlı tavus kuşları hangi "
  "pozisyonda sınıflandırılır?",
  ["01.05", "01.06", "02.07", "95.08", "05.05"],
  "B",
  "01.05 yalnızca pozisyonda ismen sayılan evcil kanatlıları (Gallus domesticus türü tavuklar, ördekler, kazlar, "
  "hindiler, beç tavukları) kapsar; açıklama notu tavus kuşlarını 01.06’daki diğer kuşlar arasında sayar. Tuzak, "
  "kümeste yetiştirildiği için 01.05’i seçmektir.",
  "01.05 ve 01.06 pozisyon metinleri ve Açıklama Notları.")

# 3 — Fasıl 94
q(94, BUL,
  "Yere konularak kullanılmak üzere imal edilmiş, adi metalden çekmeceli dosya dolabı Tarife Cetvelinin hangi "
  "fasılında yer alır?",
  ["Fasıl 73", "Fasıl 83", "Fasıl 76", "Fasıl 84", "Fasıl 94"],
  "E",
  "83.04 adi metallerden dosya ve tasnif kutuları gibi büro eşyasını kapsar, ancak 94.03’teki büro mobilyalarını "
  "hariç tutar; yere konularak kullanılan dosya dolabı mobilya olarak Fasıl 94’tedir. Tuzak, “adi metalden büro "
  "eşyası” düşüncesiyle Fasıl 83’ü seçmektir.",
  "83.04 pozisyon metni ve Açıklama Notu; Fasıl 94 Not 2; 94.03 Açıklama Notu.")

# 4 — Fasıl 20
q(20, OLUM,
  "Tarife Cetvelinin 20. faslı sebzeler, meyveler, sert kabuklu meyveler ve bitkilerin diğer kısımlarından elde "
  "edilen müstahzarları kapsar. Aşağıdakilerden hangisi bu fasılda <b>sınıflandırılmaz</b>?",
  ["Sirke ile konserve edilmiş enginar içleri",
   "Teneke kutularda sunulan domates salçası",
   "Domates esaslı, hazırlanmış domates çorbası",
   "Dilimlenmiş halde konserve edilmiş domalan",
   "Şurup içinde konserve edilmiş kayısı yarımları"],
  "C",
  "20.02 açıklama notu domates püresi, salçası ve konsantresini bu pozisyona alırken domates çorbası ve benzeri "
  "müstahzarları 21.04’e gönderir; Fasıl 20 Genel Açıklamaları da 21.04’teki çorbaları fasıl dışında bırakır. "
  "Diğerleri sırasıyla 20.01, 20.02, 20.03 ve 20.08’dedir.",
  "Fasıl 20 Genel Açıklamalar; 20.01, 20.02, 20.03 ve 20.08 Açıklama Notları.")

# 5 — Fasıl 5
q(5, ESYA,
  "Tarife Cetveline göre, bir geyik türü tarafından salgılanan, koyu kahverengi ve kuvvetli kokulu, normal olarak "
  "şeklini aldığı torbalar içinde bulunan tabii misk hangi pozisyonda sınıflandırılır?",
  ["05.10", "05.07", "33.01", "05.11", "30.01"],
  "A",
  "05.10 pozisyon metni ak amber, kunduz hayası ve kedi miskiyle birlikte miski ismen sayar; açıklama notu bunun "
  "bir geyik tarafından salgılanıp torbalarda bulunduğunu, Fasıl 29’daki suni misklerle karıştırılmaması "
  "gerektiğini belirtir. 05.07 geyik boynuzları, 05.11 başka yerde yer almayan hayvansal ürünler içindir.",
  "05.10 pozisyon metni ve Açıklama Notu.")

# 6 — Fasıl 39
q(39, OLUM,
  "Aşağıdaki plastik eşyadan hangisi 39.24 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Plastikten yatak lazımlığı",
   "Plastikten tükürük kabı",
   "Bina duvarına daimi olarak tespit edilmek üzere hazırlanmamış plastik havlu askısı",
   "Plastikten bebek banyo küveti",
   "Plastikten ekmek kutusu"],
  "D",
  "39.22 açıklama notu, sabit hijyenik tesisatın yanında bebek banyo küvetleri, taşınabilir klozetler ve kamp "
  "tuvaletleri gibi benzer boyut ve kullanımdaki eşyayı da kapsar. Yatak lazımlığı gibi küçük taşınabilir hijyenik "
  "eşya, tükürük kabı, ekmeklik ve duvara daimi tespit edilmeyen havlu askısı 39.24’tedir.",
  "39.22 ve 39.24 Açıklama Notları.")

# 7 — GYK (kural 1)
q("GYK", GYK,
  "Fasıl 96 dolma kalemleri ve kurşun kalemleri kapsamasına rağmen, teknik çizim kalemlerinin bu fasılda değil "
  "90.17 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralının gereğidir?",
  ["GYK 1", "GYK 3(a)", "GYK 3(b)", "GYK 3(c)", "GYK 4"],
  "A",
  "Fasıl 96 Not 1(f), teknik çizim kalemlerini 90. Fasıldaki eşya olarak bu fasıl dışında bırakır; sınıflandırma "
  "not hükmü ve 90.17 pozisyon metniyle, yani GYK 1 ile yapılır. Not hükmü varken eşya iki pozisyona girmiş "
  "sayılmadığından GYK 3(a)’ya başvurulmaz.",
  "GYK 1; Fasıl 96 Not 1(f).")

# 8 — Fasıl 17
q(17, ESYA,
  "Tatlı sorgum bitkisinin gövdesinden sıkılan özsuyun koyulaştırılmasıyla hazırlanan, içine başka hiçbir madde "
  "katılmamış sorgum şurubu Tarife Cetvelinde hangi pozisyonda yer alır?",
  ["17.01", "17.03", "21.06", "12.12", "17.02"],
  "E",
  "17.02 açıklama notu, şeker pancarı ve kamışı dışındaki bitkilerden elde edilen sakkaroz şuruplarını bu "
  "pozisyona alır ve tatlı sorgumdan elde edilenleri ismen sayar. 17.01 yalnız kamış veya pancar şekerini ve katı "
  "haldeki kimyaca saf sakkarozu, 21.06 ise aromalı şurupları kapsar.",
  "17.01 ve 17.02 Açıklama Notları.")

# 9 — Fasıl 23
q(23, POZ,
  "Aşağıdakilerden hangisi 23.01 pozisyonunda sınıflandırılır?",
  ["İnsan tüketimine uygun, ısıl işlem görmüş karides unu",
   "Memeli deniz hayvanlarının işlenmesiyle elde edilen, insan gıdası olarak kullanılmaya elverişli olmayan kaba un",
   "Yağı alınmış kemiklerin öğütülmesiyle elde edilen kemik tozu",
   "Hayvan yemi yapımında kullanılan, toz haline getirilmiş istiridye kabukları",
   "İnsan tüketimine uygun olmayan cansız çekirgelerden elde edilen un"],
  "B",
  "23.01 açıklama notu, kemik, boynuz ve kabuk gibi uzuvlar hariç olmak üzere memeli deniz hayvanları dahil bütün "
  "hayvanların işlenmesiyle elde edilen ve insan gıdasına elverişli olmayan unları kapsar. Böcek unları 05.11’e, "
  "kemik tozu 05.06’ya, kabuk tozu 05.08’e, yenilebilir karides unu 03.09’a gider.",
  "23.01 Açıklama Notu; 03.09, 05.06 ve 05.08 Açıklama Notları.")

# 10 — Fasıl 65 (sıralama)
q(65, SIRA,
  "Aşağıdaki eşyanın Tarife Cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru dizilişi hangisidir?"
  "<br/>I. Kauçuktan banyo bonesi"
  "<br/>II. Şapka imaline mahsus, kalıplanarak şekil verilmemiş keçeden üstüvane"
  "<br/>III. Doğrudan örülüp keçeleştirilmiş fes"
  "<br/>IV. Başlıklara takılmaya hazır, deriden çene altı kayışı"
  "<br/>V. Rafya şeritlerinden örülmüş, kalıpta preslenerek şekil verilmiş şapka",
  ["II – III – V – I – IV",
   "V – II – III – IV – I",
   "II – V – III – I – IV",
   "II – V – I – III – IV",
   "V – II – I – III – IV"],
  "C",
  "Keçe üstüvane 65.01, şeritlerden örülüp şekil verilmiş şapka 65.04, örülüp keçeleştirilmiş fes 65.05, "
  "kauçuktan banyo bonesi 65.06, çene altı kayışı 65.07’dedir. Tuzak, keçeleştirilmiş fesi keçe taslağı sanıp "
  "65.01’e yakın düşünmek veya banyo bonesini 65.05’teki başlıklarla karıştırmaktır.",
  "65.01, 65.04, 65.05, 65.06 ve 65.07 Açıklama Notları.")

# 11 — Fasıl 22
q(22, OLUM,
  "Aşağıdakilerden hangisi 22.06 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Armut suyunun fermentasyonuyla elde edilen armut şarabı (perry)",
   "Bazı palmiyelerin özsularından elde edilen hurma (palmiye) şarabı",
   "Alkol derecesi hacimce %0,5’i geçen bira ve şarap karışımı",
   "İncir suyunun fermentasyonuyla elde edilen, alkol derecesi hacimce %0,5’i geçen incir şarabı",
   "Pirinç veya palmiye şarabından damıtma yoluyla elde edilen arak"],
  "E",
  "22.06, armut ve hurma şarabı, incir şarabı ile %0,5’i aşan bira-şarap karışımları gibi fermente içecekleri "
  "kapsar. Pirinç veya palmiye şarabından elde edilen arak ise damıtma yoluyla elde edilmiş alkollü içki olarak "
  "22.08’de ismen sayılır. Tuzak, hammaddesinin fermente bir içecek olmasıdır.",
  "22.06 ve 22.08 Açıklama Notları.")

# 12 — Fasıl 85
q(85, FARK,
  "Aşağıdaki seçeneklerin hangisinde aynı 4’lü pozisyonda yer almayan eşya bulunmaktadır?",
  ["Elektrikli perma yapma cihazı – Kendinden elektrik motorlu saç kesme makinesi",
   "Elektrikli saç kurutucu – Elektrikli el kurutma cihazı",
   "Kendinden elektrik motorlu tıraş makinesi – Kendinden elektrik motorlu epilasyon cihazı",
   "Ev tipi elektrikli krep yapıcı – Ev tipi elektrikli gofret (waffle) ütüsü",
   "Ev tipi elektrikli yoğurt yapma cihazı – Ev tipi elektrikli patlamış mısır cihazı"],
  "A",
  "85.16, saç kurutucu ve perma cihazı gibi berber işlerine mahsus elektrotermik cihazları, el kurutma cihazlarını "
  "ve krep, gofret, yoğurt, patlamış mısır cihazı gibi ev tipi elektrotermik cihazları kapsar. Kendinden motorlu "
  "saç kesme makinesi ise tıraş ve epilasyon cihazlarıyla birlikte 85.10’dadır.",
  "85.10 ve 85.16 pozisyon metinleri ve Açıklama Notları.")

# 13 — Fasıl 30
q(30, ESYA,
  "Tarife Cetveline göre, tedavide kullanılmak üzere hazırlanmış, gliserin içinde muhafaza edilen, dozlandırılmamış "
  "ve perakende satış için ambalajlanmamış (dökme) kırmızı kemik iliği hangi pozisyonda sınıflandırılır?",
  ["05.10", "30.02", "30.04", "30.01", "02.06"],
  "D",
  "30.01 açıklama notu, tedavide veya korunmada kullanılmak üzere hazırlanmış insan veya hayvan menşeli diğer "
  "maddeler arasında gliserinde muhafaza edilen kırmızı kemik iliğini sayar; ölçülü dozlarda veya perakende "
  "ambalajda olsaydı 30.04’e girerdi. Tuzak, gliserolde geçici korunan guddeler nedeniyle 05.10’u seçmektir.",
  "30.01 ve 05.10 Açıklama Notları.")

# 14 — GYK (kural 5(b))
q("GYK", GYK,
  "Bira doldurulmuş; boşaltıldıktan sonra iade edilip yeniden doldurulmak üzere kullanılan, sürekli kullanıma "
  "elverişli olduğu açıkça belli 50 litrelik paslanmaz çelik fıçılar gümrüğe sunulmuştur. Bu eşyanın "
  "sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
  ["Fıçılar GYK 5(b) uyarınca ambalaj sayılarak bira ile birlikte 22.03 pozisyonunda sınıflandırılır.",
   "GYK 5(b) uygulanmaz; fıçılar 73.10, bira 22.03 pozisyonunda ayrı ayrı sınıflandırılır.",
   "Fıçılar GYK 5(a) uyarınca belli bir eşyaya göre yapılmış mahfaza sayılarak bira ile birlikte 22.03 "
   "pozisyonunda sınıflandırılır.",
   "GYK 3(b) uyarınca esas niteliği veren çelik fıçının pozisyonunda, 73.10’da birlikte sınıflandırılır.",
   "Fıçılar sıkıştırılmış gaz kabı sayılarak 73.11, bira 22.03 pozisyonunda sınıflandırılır."],
  "B",
  "GYK 5(b) ambalajı içindeki eşyayla birlikte sınıflandırır; ancak sürekli kullanıma elverişli olduğu açıkça belli "
  "ambalajlara uygulanmaz. Bu nedenle çelik fıçı, hacmi 300 litreyi geçmeyen çelik kaplar arasında 73.10’da, bira "
  "22.03’te ayrı sınıflandırılır; ortada bir takım bulunmadığından 3(b) de uygulanmaz.",
  "GYK 5(b) ve Açıklama Notu (IV); 73.10 pozisyon metni.")

# 15 — Fasıl 49
q(49, ESYA,
  "Tarife Cetveline göre, bir ülkenin turistik faaliyetlerini ve demiryolu hatlarını uygun resim ve çizgilerle "
  "gösteren, basılı şematik harita hangi pozisyonda sınıflandırılır?",
  ["49.05", "49.06", "49.11", "90.23", "49.01"],
  "C",
  "49.05 her türlü basılı haritayı kapsasa da açıklama notu, bir ülkenin turistik veya endüstriyel faaliyetlerini ya "
  "da demiryolu hatlarını resim ve çizgilerle gösteren şematik haritaları bu pozisyon dışında bırakarak 49.11’e "
  "gönderir. 49.06 elle çizilmiş planlar, 90.23 kabartma haritalar içindir.",
  "49.05 Açıklama Notu, istisna (d); 49.11.")

# 16 — Fasıl 35
q(35, FARK,
  "Eczacılık, gıda ve tutkal sanayiinde kullanılan aşağıdaki protein esaslı maddelerden hangisi Tarife Cetvelinde "
  "diğerlerinden farklı bir pozisyonda sınıflandırılır?",
  ["Buğday veya çavdardan çıkartılan gliadin",
   "Temel soya proteini olan glisinin",
   "Bira mayasından izole edilmiş nükleoproteidler",
   "Demir peptonat",
   "Kazein tannat"],
  "E",
  "Gliadin gibi tahıl proteinleri, glisinin, nükleoproteidler ve peptonların türevi olan demir peptonat 35.04’tedir. "
  "Kazein tannat ise 35.01 açıklama notunda klorinatlı ve iyotlu kazeinle birlikte kazein türevi olarak sayılır. "
  "Tuzak, “tannat” ifadesi nedeniyle onu da diğer protein türevleriyle aynı pozisyonda sanmaktır.",
  "35.01 ve 35.04 Açıklama Notları.")

# 17 — Fasıl 44
q(44, OLUM,
  "Aşağıdakilerden hangisi 44.04 pozisyonunda <b>sınıflandırılmaz</b>?",
  ["Boylamasına yarılmış ve fıçıya takıldığında uçları birbirine geçecek şekilde iki başından kertik açılmış "
   "çember odunu",
   "Fıçı çemberi yapımında kullanılan, demetler halindeki yarılmış söğüt çubukları",
   "Uçları sivriltilmiş fakat uzunlamasına biçilmemiş çit kazıkları",
   "Baston imaline elverişli, kabaca yontulmuş fakat torna edilmemiş ağaç çubuklar",
   "Elek ve kibrit kutusu yapımında kullanılan, eğilip bükülebilen ince kasnak tahtaları"],
  "A",
  "44.04 açıklama notu ağaç çemberleri, uçları sivriltilmiş kazıkları, kabaca yontulmuş baston çubuklarını ve "
  "kasnak tahtalarını kapsar; ancak fıçıya takılmak üzere iki başından kertik açılmış çember odununu fıçıcı "
  "eşyası olarak 44.16’ya gönderir. Tuzak, hepsinin yarılmış veya yontulmuş ağaç olmasıdır.",
  "44.04 Açıklama Notu; 44.16 pozisyon metni.")

# 18 — Fasıl 96 (Not 3)
q(96, NOT,
  "Fasıl 96 Not 3’e göre, 96.03 pozisyonu anlamında “hazırlanmış süpürge ve fırça başları” tabirinden "
  "aşağıdakilerden hangisi anlaşılır?",
  ["Bir sapa veya gövdeye monte edilerek kullanıma hazır hale getirilmiş süpürge ve fırçalar",
   "Bir ayırıma gerek duyulmaksızın kullanılmaya hazır olan ya da yalnızca baş kısmını keserek şekil verme gibi "
   "önemsiz bir işçilik gerektiren, monte edilmemiş başlar",
   "Yalnızca temizlenmiş, ağartılmış veya boyanmış, demetler halindeki domuz ve porsuk kılları",
   "Kök uçları hizalanıp boylarına göre ayrıldıktan sonra kullanılabilecek, gevşekçe sarılmış kıl yığınları",
   "Yalnızca bitkisel liflerden oluşan ve fırça imalinde kullanılmadan önce demetlere ayrılması gereken lif "
   "kütleleri"],
  "B",
  "Not 3, hayvan kılı, bitkisel lif veya diğer maddelerden; ayırıma gerek olmadan kullanılmaya hazır ya da yalnızca "
  "baş kısmının kesilerek şekillendirilmesi gibi önemsiz işçilik gerektiren monte edilmemiş başları tanımlar. "
  "Yalnızca temizlenmiş, ağartılmış veya demetlenmiş kıllar 05.02’de kalır; monte edilmiş fırçalar bitmiş eşyadır.",
  "Fasıl 96 Not 3; 05.02 Açıklama Notu.")

# 19 — GYK (kural 6)
q("GYK", GYK,
  "Tropikal bir ağaçtan oyularak yapılmış küçük bir süs heykelciğinin 44.20 pozisyonunda yer aldığı belirlenmiştir. "
  "Bu pozisyonun “ahşap küçük heykelcikler ve diğer süs eşyası” tek tireli alt pozisyonu altındaki “tropikal "
  "ağaçlardan olanlar” ve “diğerleri” iki tireli alt pozisyonlarından hangisine gireceğinin belirlenmesiyle ilgili "
  "aşağıdakilerden hangisi doğrudur?",
  ["GYK 3(a) uyarınca eşyayı en özel niteleyen alt pozisyon, farklı seviyedeki alt pozisyonlar da birbiriyle "
   "karşılaştırılarak seçilir.",
   "GYK 1 uyarınca yalnız dört rakamlı pozisyon metni dikkate alınır; alt pozisyonlar arasında kurala dayalı seçim "
   "yapılmaz.",
   "GYK 3(c) uyarınca geçerli olabilecek alt pozisyonlardan numara sırasına göre sonuncusu, yani “diğerleri” seçilir.",
   "GYK 6 uyarınca yalnız aynı seviyedeki iki tireli alt pozisyonlar, ait oldukları tek tireli alt pozisyonun "
   "kapsamı içinde karşılaştırılır.",
   "GYK 4 uyarınca eşyaya en çok benzeyen süs eşyasının yer aldığı alt pozisyon esas alınır."],
  "D",
  "GYK 6’ya göre alt pozisyonlarda sınıflandırma yalnız aynı seviyedeki alt pozisyonlar karşılaştırılarak yapılır: "
  "önce eşyayı en özel niteleyen tek tireli alt pozisyon seçilir, iki tireli alt pozisyonlara ancak bundan sonra "
  "bakılır ve bunların kapsamı tek tireli alt pozisyonu aşamaz.",
  "GYK 6 ve Açıklama Notu; 44.20 pozisyon metni.")

# 20 — Fasıl 56
q(56, NOT,
  "56.02 ve 56.03 pozisyonlarının Açıklama Notlarına göre iğneleme yöntemiyle elde edilen mensucatla ilgili "
  "aşağıdakilerden hangisi doğrudur?",
  ["İğneleme yöntemiyle elde edilen her türlü mensucat, lif türüne bakılmaksızın keçe olarak 56.02’de yer alır.",
   "Keçeleşme özelliği olmayan jüt gibi bitkisel liflerden iğneleme yöntemiyle keçe elde edilemez.",
   "Filament esaslı tülbentlerin iğnelenmesiyle elde edilen kumaşlar dokunmamış mensucat olarak 56.03’te yer alır.",
   "Devamsız liflerden, iğnelemenin başka bir tutturma yöntemine yalnızca tamamlayıcı olduğu kumaşlar keçe olarak "
   "56.02’de yer alır.",
   "Dikiş-trikotaj usulü, dokunmamış mensucatta liflerin mekanik olarak tutturulmasında kullanılan yöntemlerden "
   "biridir."],
  "C",
  "56.02 açıklama notu, filament esaslı iğnelenmiş kumaşları ve iğnelemenin başka bir tutturmaya tamamlayıcı olduğu "
  "devamsız lif kumaşlarını dokunmamış mensucat (56.03) sayar. İğne işi tekniği jüt gibi keçeleşmeyen liflerden de "
  "keçe elde edilmesini sağlar; dikiş-trikotaj usulü dokunmamış mensucatın mekanik tutturma yöntemi değildir.",
  "56.02 ve 56.03 Açıklama Notları; Fasıl 56 Not 2.")


if __name__ == "__main__":
    assert len(S) == 20, len(S)
    cnt = Counter(x["cevap"] for x in S)
    assert all(cnt[L] == 4 for L in "ABCDE"), cnt
    for i, x in enumerate(S, 1):
        assert len(x["secenekler"]) == 5, i
        assert len(x["gerekce"]) <= 420, (i, len(x["gerekce"]))
        assert len(x["gerekce"].split()) <= 45, (i, len(x["gerekce"].split()))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"tur": "karma", "no": 9, "sorular": S}, f, ensure_ascii=False, indent=1)
    print("yazıldı:", OUT, dict(sorted(cnt.items())), "".join(x["cevap"] for x in S))
