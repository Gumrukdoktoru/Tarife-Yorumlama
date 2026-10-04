#!/usr/bin/env python3
# Fasıl 41 modülü üreticisi
import json, os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

E4 = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
FN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
ES = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"

d = {
 "tur": "fasil",
 "fasil": 41,
 "baslik": "Ham postlar, deriler (kürkler hariç) ve köseleler",
 "bolum": "VIII",
 "oz": {
  "vurgu": "Fasıl 41 deriyi iki eksende sınıflandırır: hayvan (sığır-at / koyun-kuzu / diğer) ve işlem derecesi (ham → dabaklanmış veya crust → ileri hazırlanmış). Bu üç sütun-üç satırlık tabloya özel deriler (41.14: güderi, rugan, metalize) ile terkip deri ve döküntüler (41.15) eklenir. Tüylü deriler Not 1(c) istisnasına girmiyorsa Fasıl 43’e gider.",
  "maddeler": [
   "Ham (41.01–41.03): yaş, tuzlanmış, kurutulmuş, kireçlenmiş, pikle edilmiş; geri alınabilir ön dabaklama görmüş olabilir; dabaklanmamış ve parşömine edilmemiş.",
   "Dabaklanmış veya crust (41.04–41.06): geri alınamaz dabaklama; crust, kurutulmadan önce yeniden dabaklanmış, renklendirilmiş veya yağla doldurulmuş deridir (Not 2).",
   "İleri hazırlanmış (41.07, 41.12, 41.13): boyama, sırça, baskı, perdah gibi bitirme işlemleri; parşömine edilmiş deri (vellum) dahil.",
   "41.14 güderi, rugan, ruganla kaplanmış ve metalize deriyi; 41.15 yalnız deri esaslı terkip deriyi ve eşya imaline uygun olmayan deri döküntülerini kapsar.",
   "Bölüm VIII’in bölüm notu yoktur; 41.08–41.11 pozisyonları boştur."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Ham post veya derinin kırpıntısı mı? Telek ve tüyleri alınmamış kuş derisi mi?", "<b>05.11</b> · <b>05.05</b> / <b>67.01</b>"],
   ["2", "Yenilebilir hayvan derisi mi?", "Pişmemiş Fasıl 2 (balık derisi Fasıl 3) · pişmiş <b>16.02</b>"],
   ["3", "Tüylü veya yünlü mü ve Not 1(c) istisnasına girmiyor mu ya da kılıyla birlikte dabaklanmış-aprelenmiş mi?", "Fasıl <b>43</b> (<b>43.01</b> / <b>43.02</b>)"],
   ["4", "Özel biçimde kesilmiş parça (çanta, ayakkabı aksamı) mı?*", "Fasıl <b>42</b> / <b>64</b>"],
   ["5", "Esası deri veya deri lifi olan terkip deri ya da eşya imaline uygun olmayan deri kırpıntısı, talaşı, tozu, unu mu?", "<b>41.15</b>"],
   ["6", "Güderi, rugan, ruganla kaplanmış veya metalize deri mi?", "<b>41.14</b>"],
   ["7", "Ham mı? (yaş, tuzlu, kurutulmuş, kireçlenmiş, pikle; geri alınabilir ön dabaklama)", "Sığır-at <b>41.01</b> · koyun-kuzu <b>41.02</b> · diğer <b>41.03</b>"],
   ["8", "Dabaklanmış veya crust, ileri işlem görmemiş mi?", "<b>41.04</b> · <b>41.05</b> · <b>41.06</b>"],
   ["9", "Dabaklama veya crust sonrası ileri hazırlanmış ya da parşömine edilmiş mi?", "<b>41.07</b> · <b>41.12</b> · <b>41.13</b>"]
  ],
  "dipnot": "* Bütün ya da parça halindeki deriler (sırt, omuz, karın, şerit) Fasıl 41’de kalır. Plastik kaplaması 0,15 mm’den az olmayan ve toplam kalınlığın yarısını aşan deriler Fasıl 39’dadır."
 },
 "pozisyon_haritasi": [
  ["41.01", "Sığır ve at ham deri ve postları", "Dabaklanmamış; kılı alınmış olsun olmasın", "Tuzlu sığır derisi, pikle bufalo derisi"],
  ["41.02", "Koyun ve kuzu ham derileri", "Not 1(c) kuzuları hariç", "Pikle kuzu derisi, yünlü ham koyun derisi"],
  ["41.03", "Diğer ham post ve deriler", "Keçi, domuz, sürüngen, tüysüz kuş, balık", "Ham keçi, yılan, devekuşu derisi"],
  ["41.04", "Sığır, at: dabaklanmış veya crust", "Kılı alınmış; ileri işlem yok", "Wet-blue sığır derisi"],
  ["41.05", "Koyun, kuzu: dabaklanmış veya crust", "Yünü alınmış; koyun-keçi melezi dahil", "Wet-blue koyun derisi, skiver"],
  ["41.06", "Diğer hayvanlar: dabaklanmış veya crust", "Keçi, domuz, sürüngen, kanguru vb.", "Crust keçi derisi, dabaklanmış yılan derisi"],
  ["41.07", "Sığır, at: ileri hazırlanmış deri", "Parşömine dahil; 41.14 hariç", "Taban köselesi, box-calf, vellum"],
  ["41.12", "Koyun, kuzu: ileri hazırlanmış deri", "Parşömine dahil; 41.14 hariç", "Boyanıp bitirilmiş koyun derisi"],
  ["41.13", "Diğer hayvanlar: ileri hazırlanmış deri", "Keçi, domuz, sürüngen vb.; 41.14 hariç", "Bitirilmiş timsah ve keçi derisi"],
  ["41.14", "Güderi; rugan; metalize deri", "Özel bitirme işlemleri", "Koyun güderisi, rugan deri"],
  ["41.15", "Terkip deri; deri kırpıntı, talaş, toz, un", "Esası deri veya deri lifi", "Deri lifinden levha, deri tozu"]
 ],
 "notlar": [
  ["Bölüm VIII", "Bölüm VIII’in (Fasıl 41–43) bölüm notu yoktur; sınıflandırma fasıl notları ve Açıklama Notlarıyla yapılır. Fasıl 41 ham ve işlenmiş deri, Fasıl 42 deri eşya, saraciye, seyahat eşyası ve bağırsaktan eşya, Fasıl 43 kürk ve taklit kürktür."],
  ["Fasıl 41 Not 1", "Hariç: (a) ham post veya derilerin kırpıntı ve benzeri döküntüleri (05.11); (b) kuşların tüylü derileri ve tüylü diğer kısımları (05.05 veya 67.01); (c) tüylü hayvanların tüyleri ve yünleri alınmamış ham, dabaklanmış veya aprelenmiş derileri (Fasıl 43). Ancak şu hayvanların tüylü <b>ham</b> derileri Fasıl 41’dedir: sığır (bufalo dahil), at türü, koyun ve kuzu (Astragan, Karakul, Persaniye, breitschwanz ve benzerleri ile Hint, Çin, Moğol, Tibet kuzuları hariç), keçi ve oğlak (Yemen, Moğolistan, Tibet keçi ve oğlakları hariç), domuz (pekari dahil), dağ keçisi, ceylan, deve (tek hörgüçlü dahil), geyik, şimal geyiği, ren geyiği, karaca ve köpek."],
  ["Fasıl 41 Not 2", "(A) 41.04–41.06, geri alınabilir dabaklama (ön dabaklama dahil) görmüş deri ve postları kapsamaz; bunlar 41.01–41.03’tedir. (B) “Ara kurutmalı (crust)”: kurutulmadan önce yeniden dabaklanmış, renklendirilmiş veya yağla doldurulmuş (fat-liquored) deri ve postlar."],
  ["Fasıl 41 Not 3", "Tarifenin neresinde geçerse geçsin “terkip yoluyla elde edilen deri ve kösele” tabiri yalnız 41.15’e giren maddeleri ifade eder."],
  ["Genel Açıklamalar", "Ham deri hazırlık işlemleri (yıkama, kıl alma, et temizleme, kireç giderme) deriyi ham olmaktan çıkarmaz. Dabaklama (bitkisel, mineral, kimyasal) geri alınamaz bir reaksiyondur ve ürünü “deri” yapar. Parşömine deriler dabaklanmadan, kireçli hamurla sıvanıp tıraşlanarak ve jelatinle sepilenerek hazırlanır; yeni doğmuş buzağı derisinden olanlara “vellum” denir. Yarma (parçalanmış) deriler bütün derinin pozisyonunu izler."],
  ["Genel Açıklamalar", "Bütün haldeki (baş ve ayak derisi alınmış olabilir) veya parça halindeki (yan, omuz, kıç, karın) deriler ile şerit ve tabakalar Fasıl 41’dedir; özel biçimlerde kesilmiş parçalar eşya sayılır (özellikle Fasıl 42, 64)."],
  ["41.01–41.03 Açıklama Notları", "Yenilebilir, pişmemiş hayvan derileri 02.06 veya 02.10’da, pişmiş olanlar 16.02’de; yenilebilir balık derileri Fasıl 3’te. 41.03: 41.01 ve 41.02 dışındaki ham deriler; telek ve tüyleri alınmış kuş derileri, balık ve sürüngen derileri, kılları alınmış keçi ve oğlak derileri (Yemen, Moğol, Tibet keçileri dahil) ve Not 1(c)’de sayılan hayvanların tüylü ham derileri."],
  ["41.04–41.06 Açıklama Notları", "Hariç: güderi (41.14); dabaklanmış veya crust deri kırpıntıları (41.15); kılı veya yünü ile birlikte dabaklanmış ya da crust deriler (Fasıl 43). Koyun-keçi melezlerinin derileri 41.05’te; domuz, sürüngen, ceylan, kanguru, geyik, fil, deve, köpek, balık ve deniz memelisi derileri 41.06’da."],
  ["41.07 / 41.12 / 41.13 Açıklama Notları", "Sığır derisinden taban köselesi (silindir veya çekiçle sertleştirilmiş), makine kayışı derisi (öküz sırtından) ve box-calf 41.07’de. Formaldehit veya sıvı yağla dabaklanmış yarma koyun derisinden “doeskin” 41.13’e değil 41.12 veya 41.14’e girer. Yünü veya kılıyla aprelenmiş deriler Fasıl 43’tedir."],
  ["41.14 Açıklama Notu", "Güderi: balık yağı veya diğer hayvansal yağlarla dabaklanmış, yumuşak, sarı, yıkanabilir deri; formaldehitle kısmen, ardından yağla dabaklanan kombine güderi dahil. Formaldehit ve şapla dabaklanmış diğer yıkanabilir deriler ile başka usulle dabaklanıp yalnız yağla doldurulmuş deriler hariç. Rugan: vernik, lak veya ince plastikle kaplı, ayna parlaklığında, kaplaması <b>0,15 mm’yi geçmeyen</b> deri. Ruganla kaplanmış: plastik 0,15 mm’yi geçer fakat toplam kalınlığın <b>yarısından azdır</b>. Metalize: metal tozu veya yaprakla kaplı deri."],
  ["41.14 / 41.15 sınırları", "Plastik kaplaması 0,15 mm’den az olmayan ve toplam deri kalınlığının yarısını aşan deriler Fasıl 39’dadır. Terkip yoluyla elde edilen derinin rugan veya metalize olanları 41.14’e değil 41.15’e girer."],
  ["41.15 Açıklama Notu", "Terkip deri: deri kırpıntılarının bağlayıcıyla veya bağlayıcısız güçlü basınçla birleştirilmesi ya da deri döküntülerinin lif haline getirilip hamurlaştırılarak haddelenmesiyle elde edilen levha, yaprak, şeritler (rulo olsun olmasın). Kare veya dikdörtgen dışı kesilmiş olanlar başka fasıllarda (özellikle Fasıl 42). Plastik (39), kauçuk (40), kağıt (48) veya sıvanmış mensucat (59) esaslı taklit deriler hariç."],
  ["41.15 Açıklama Notu", "Döküntüler: eşya imaline uygun olmayan deri kırpıntıları, kullanılamaz durumdaki ekşimiş deri eşya, deri tozu ve talaşı, deri unu. Eşya imaline elverişli kırpıntılar ve deri eşya hurdaları (eski makine kayışları gibi) deri olarak 41.07 veya 41.12–41.14’te; ham deri kırpıntıları 05.11’de; eski ayakkabılar 63.09’da."]
 ],
 "sinir_komsulari": [
  ["Ham post ve deri kırpıntıları", "05.11", "Fasıl 41 Not 1(a)"],
  ["Telek ve tüyleri alınmamış kuş derisi", "05.05 / 67.01", "Fasıl 41 Not 1(b)"],
  ["Astragan, Karakul, Persaniye kuzusunun yünlü ham derisi", "43.01", "Not 1(c) istisnasının dışında"],
  ["Yemen, Moğol, Tibet keçisinin kıllı ham derisi", "43.01", "Not 1(c) istisnasının dışında"],
  ["Kılı ile birlikte dabaklanmış sığır veya buzağı derisi", "43.02", "41.04 ve 41.07 hariç tutmaları"],
  ["Pişmemiş yenilebilir domuz derisi; pişmiş deri", "02.06 / 02.10 / 16.02", "41.01–41.03 hariç tutmaları"],
  ["Plastik esaslı suni deri; plastik kaplaması kalınlığın yarısını aşan deri", "Fasıl 39", "41.15 ve 41.14 Açıklama Notları"],
  ["Kauçuk esaslı taklit deri", "Fasıl 40", "41.15 Açıklama Notu"],
  ["Sıvanmış dokumaya elverişli mensucattan taklit deri", "Fasıl 59", "41.15 Açıklama Notu"],
  ["Çanta veya ayakkabı için özel biçimde kesilmiş deri parçaları", "Fasıl 42 / 64", "Fasıl 41 Genel Açıklamalar"],
  ["Eski ayakkabılar", "63.09", "41.15 hariç tutması"],
  ["Kılları alınmış ham Tibet keçisi derisi", "41.03", "Kıl alınınca Fasıl 41’e döner"],
  ["Eşya imaline elverişli deri kırpıntısı, eski makine kayışı", "41.07 / 41.12–41.14", "41.15’e değil deri pozisyonuna"],
  ["Formaldehit ve şapla dabaklanmış yıkanabilir deri", "41.07 / 41.12 / 41.13", "41.14 güderi tanımı dışında"]
 ],
 "tuzaklar": [
  "<b>Tüylü deri her zaman kürk değildir.</b> Sığır, at, koyun, keçi, domuz, geyik, ren geyiği, ceylan, deve ve köpeğin tüylü ham derileri Fasıl 41’dedir; Astragan-Karakul-Persaniye ile Hint, Çin, Moğol, Tibet kuzuları ve Yemen, Moğol, Tibet keçileri Fasıl 43’e gider.",
  "<b>İstisna yalnız HAM deri içindir.</b> Kılı ile birlikte dabaklanmış veya aprelenmiş deri, sığır derisi bile olsa Fasıl 43’tedir (43.02).",
  "<b>Kılı alınan egzotik keçi Fasıl 41’e döner.</b> Tibet keçisinin kılları alınmış ham derisi 41.03’te, kılsız dabaklanmış hali 41.06’dadır.",
  "<b>Ön dabaklama dabaklama değildir.</b> Geri alınabilir hafif dabaklama görmüş deri ham deri pozisyonunda kalır (Not 2(A)).",
  "<b>Parşömine deri dabaklanmamıştır ama ham da değildir.</b> Vellum dahil parşömine deriler 41.07, 41.12 veya 41.13’tedir.",
  "<b>Güderi hayvana bakmaz.</b> Yağla dabaklanmış koyun veya geyik güderisi 41.14’tedir; formaldehit ve şapla dabaklanmış yıkanabilir deri ise güderi sayılmaz.",
  "<b>0,15 mm ve “yarı” kuralı.</b> Rugan kaplaması 0,15 mm’ye kadar; ruganla kaplanmış deride kaplama 0,15 mm’yi geçer ama kalınlığın yarısından azdır. Plastik kalınlığın yarısını aşarsa Fasıl 39.",
  "<b>“Suni deri” her zaman 41.15 değildir.</b> 41.15 yalnız esası deri veya deri lifi olanlar içindir (Not 3); plastik, kauçuk, kağıt veya sıvanmış mensucat esaslı taklitler Fasıl 39, 40, 48, 59’dadır.",
  "<b>Kırpıntının yeri kullanılabilirliğe bağlıdır.</b> Ham deri kırpıntısı 05.11; eşya imaline uygun olmayan dabaklı deri kırpıntısı 41.15; eşya imaline elverişli kırpıntı deri pozisyonunda kalır.",
  "<b>Koyun-keçi melezi koyun sayılır.</b> Dabaklanmış melez derisi 41.05’te, bitirilmişi 41.12’dedir; keçi ise 41.06 / 41.13."
 ],
 "hafiza": {
  "kanca": "3 HAYVAN, 3 AŞAMA + 2 ÖZEL: HAM 01-02-03 → DABAK 04-05-06 → BİTMİŞ 07-12-13 · 14 GÜDERİ-RUGAN · 15 TERKİP",
  "aciklama": "Her aşamada hayvan sırası aynıdır: önce sığır-at, sonra koyun-kuzu, sonra diğerleri. Ham deri 41.01 / 02 / 03, dabaklanmış-crust 41.04 / 05 / 06, bitirilmiş deri 41.07 / 12 / 13 (41.08–41.11 boş). En sonda iki özel kapı: parlak ve yumuşak deriler 41.14, hamur ve kırpıntı 41.15."
 },
 "sinav_odagi": [
  "Fasıl 41 Not 1(c) istisnaları: “hangi hayvanın tüyleri ve yünleri alınmamış ham derisi 43. Fasılda sınıflandırılır” sorusunda Tibet keçisinin, Fasıl 41’de kalan at, deve ve ren geyiğinden ayrılması istenmiştir.",
  "Terkip yoluyla elde edilen derinin yeri: 41.15’in plastik levha (39.21), dokunmamış mensucat (56.03) ve sıvanmış mensucat (59.03) seçenekleriyle karıştırılması; Not 3 tanımı.",
  "Bölüm VIII’in kapsamı: kürkler, köseleler, çantalar ve evcil hayvan elbiseleri bölümde yer alırken ayakkabıların (Fasıl 64) yer almadığı; “deriler ve köseleler”in bölüm eşleştirme sorularında çeldirici olarak kullanılması.",
  "Doğrudan Fasıl 41 pozisyonu soran soru azdır; fasıl daha çok bölüm kapsamı sorularında ve seçeneklerde yer almıştır. Tüylü deri ile kürk ayrımı ve terkip deri tanımı en çok sorulan iki konudur."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdaki hayvanlardan hangisinin tüyleri ve yünleri alınmamış ham derileri 43. Fasılda sınıflandırılır?",
   "secenekler": ["Tibet keçisi", "İngiliz atı", "Hecin devesi", "Ren geyiği"],
   "cevap": "A",
   "aciklama": "Fasıl 41 Not 1(c), Yemen, Moğol ve Tibet keçi ve oğlaklarını Fasıl 41’de kalan hayvanlar istisnasından hariç tutar; bu nedenle tüylü ham Tibet keçisi derisi Fasıl 43’tedir. At, deve (tek hörgüçlü dahil) ve ren geyiğinin tüylü ham derileri Fasıl 41’dedir."
  },
  {
   "soru": "Tarife cetvelindeki “terkip yoluyla elde edilen deri” tabirine uyan levha ve yapraklar hangi tarife pozisyonunda sınıflandırılır?",
   "secenekler": ["39.21", "41.15", "56.03", "59.03"],
   "cevap": "B",
   "aciklama": "Fasıl 41 Not 3 uyarınca bu tabir tarifenin her yerinde yalnız 41.15’e giren, esası deri veya deri lifi olan ürünleri ifade eder. Plastik, dokunmamış mensucat veya sıvanmış mensucat esaslı taklitler 39.21, 56.03 veya 59.03 gibi pozisyonlara gider."
  }
 ],
 "ozet": [
  "Hayvan ve aşama: ham 41.01 / 41.02 / 41.03 → dabaklanmış-crust 41.04 / 41.05 / 41.06 → bitirilmiş 41.07 / 41.12 / 41.13.",
  "Tüylü ham deri kural olarak Fasıl 43; sığır, at, koyun, keçi, domuz, geyik, ceylan, deve, köpek istisnadır (egzotik kuzu ve keçiler hariç). Kılıyla dabaklanan her deri Fasıl 43.",
  "Ön dabaklama deriyi ham bırakır; crust = kurutmadan önce yeniden dabaklama, renklendirme veya yağla doldurma.",
  "Parşömine deri (vellum) bitirilmiş deri pozisyonlarındadır.",
  "41.14: güderi, rugan (kaplama ≤ 0,15 mm), ruganla kaplanmış, metalize deri; 41.15: yalnız deri esaslı terkip deri ve kullanılamaz deri döküntüleri.",
  "Ham deri kırpıntısı 05.11 · tüylü kuş derisi 05.05 / 67.01 · yenilebilir deri Fasıl 2 · şekilli kesilmiş deri Fasıl 42 / 64."
 ],
 "sorular": [
  {
   "soru": "Tarife Cetveline göre, yünü alınmış, zayıf sülfürik asit ve tuzla pikle edilerek geçici olarak muhafaza altına alınmış, dabaklanmamış kuzu derisi hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.05", "41.01", "41.03", "41.02", "41.12"],
   "cevap": "D", "tip": E4,
   "gerekce": "Pikle etme, ham deriyi geçici olarak muhafaza eden bir işlemdir; dabaklanmamış koyun ve kuzu derileri yünü alınmış olsun olmasın 41.02’dedir. 41.05 dabaklanmış veya crust, 41.12 ileri hazırlanmış koyun derileri içindir; 41.01 sığır-at, 41.03 diğer hayvanların ham derilerini kapsar.",
   "dayanak": "41.02 pozisyon metni ve Açıklama Notu; 41.01 Açıklama Notu (pikle etme)."
  },
  {
   "soru": "Tarife Cetvelinin 41. Fasıl notlarına göre, 41.04 ila 41.06 pozisyonları anlamında “ara kurutmalı (crust)” terimi hangisini ifade eder?",
   "secenekler": [
    "Dabaklanmadan önce güneşte veya fırında kurutulmuş ham deri ve postları",
    "Kurutulmadan önce yeniden dabaklanmış, renklendirilmiş veya yağla doldurulmuş deri ve postları",
    "Geri alınabilir ön dabaklamaya tabi tutulup ardından kurutulmuş deri ve postları",
    "Dabaklamadan sonra boyanmış, sırça yapılmış ve cilalanmış deri ve köseleleri",
    "Balık yağıyla dabaklanmış ve sünger taşıyla yumuşatılmış deri ve postları"
   ],
   "cevap": "B", "tip": FN,
   "gerekce": "Not 2(B), crust deriyi kurutulmadan önce yeniden dabaklanmış, renklendirilmiş veya yağla doldurulmuş deri ve postlar olarak tanımlar. Geri alınabilir ön dabaklama görmüş deriler Not 2(A) gereği ham deri pozisyonlarındadır (C). Sırça ve cila gibi bitirme işlemleri deriyi 41.07, 41.12 veya 41.13’e (D), yağla dabaklama güderi olarak 41.14’e (E) götürür.",
   "dayanak": "Fasıl 41 Not 2 (A) ve (B); Fasıl 41 Genel Açıklamalar."
  },
  {
   "soru": "Aşağıdakilerden hangisi Tarife Cetvelinin 41. Faslında <b>sınıflandırılmaz</b>?",
   "secenekler": [
    "Kılları alınmamış, tuzlanmış ham at derisi",
    "Kılları alınmamış, kurutulmuş ham geyik derisi",
    "Kılları alınmamış, kireçlenmiş ham domuz derisi",
    "Telek ve tüyleri alınmış ham kuş derisi",
    "Yünü alınmamış, tuzlanmış ham Karakul kuzusu derisi"
   ],
   "cevap": "E", "tip": OT,
   "gerekce": "Fasıl 41 Not 1(c), Astragan, Karakul, Persaniye ve benzeri kuzular ile Hint, Çin, Moğol ve Tibet kuzularının yünü alınmamış derilerini Fasıl 43’e bırakır. At, geyik ve domuzun tüylü ham derileri notun istisnası olarak Fasıl 41’de kalır (41.01, 41.03); telek ve tüyleri alınmış kuş derisi de 41.03’tedir.",
   "dayanak": "Fasıl 41 Not 1(c); 41.02 ve 41.03 Açıklama Notları."
  },
  {
   "soru": "Tarife Cetveline göre, kılları alınmış, kromla dabaklanmış ve yaş halde (wet-blue) bulunan, daha ileri işlem görmemiş sığır derisi hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.04", "41.01", "41.07", "41.14", "43.02"],
   "cevap": "A", "tip": E4,
   "gerekce": "41.04, sığır (bufalo dahil) ve atların kılı alınmış, dabaklanmış veya crust, fakat daha ileri işlem görmemiş derilerini kapsar; yaş haldeki (wet-blue) deriler de buradadır. Kromla dabaklama geri alınamaz olduğundan ham deri pozisyonu 41.01 söz konusu değildir; ileri hazırlık görmediği için 41.07’ye, kılları alındığı için 43.02’ye gitmez.",
   "dayanak": "41.04 pozisyon metni ve Açıklama Notu; Fasıl 41 Genel Açıklamalar (II)."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdaki derilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
   "secenekler": [
    "Kılları alınmış, dabaklanmış kanguru derisi",
    "Kılları alınmış, dabaklanmış domuz derisi",
    "Yünü alınmış, dabaklanmış koyun-keçi melezi derisi",
    "Dabaklanmış yılan derisi",
    "Kılları alınmış, dabaklanmış keçi derisi"
   ],
   "cevap": "C", "tip": FA,
   "gerekce": "41.05 Açıklama Notu koyun-keçi melezlerinin derilerini koyun ve kuzu derileriyle birlikte 41.05’e alır. Kanguru, domuz, yılan (sürüngen) ve keçi derileri dabaklanmış veya crust halde 41.06’dadır. Tuzak, melezi keçi sayıp 41.06’ya göndermektir.",
   "dayanak": "41.05 ve 41.06 Açıklama Notları."
  },
  {
   "soru": "Kromla dabaklanmış bir sığır derisinin yüzeyi, ayna gibi parlak görünüm veren ve kalınlığı 0,15 mm’yi geçmeyen ince bir poliüretan tabakayla kaplanmıştır. Bu deri 41.07’de değil 41.14’te (rugan) sınıflandırılır. Bu sonucun dayanağı hangisidir?",
   "secenekler": [
    "GYK 3(a): eşyayı en özel şekilde tanımlayan pozisyon önceliklidir",
    "GYK 3(b): eşyaya esas niteliğini veren madde belirleyicidir",
    "GYK 3(c): numara sırasına göre en son pozisyon seçilir",
    "GYK 4: eşyanın en çok benzediği eşyanın pozisyonu uygulanır",
    "GYK 1: 41.07 pozisyon metni 41.14’teki deri ve köseleleri açıkça hariç tutar"
   ],
   "cevap": "E", "tip": GY,
   "gerekce": "GYK 1’e göre sınıflandırma öncelikle pozisyon metinleri ve notlara göre yapılır. 41.07 metni “41.14 pozisyonunda yer alan deri ve köseleler hariç” ifadesini taşıdığından ilk bakışta iki pozisyona girme durumu oluşmaz ve GYK 3’e geçilmez. Kaplaması 0,15 mm’yi geçmeyen ayna parlaklığındaki deri 41.14 Açıklama Notuna göre rugandır.",
   "dayanak": "GYK 1; 41.07 pozisyon metni; 41.14 Açıklama Notu."
  },
  {
   "soru": "Tarife Cetvelinin 41. Fasıl notlarına göre, aşağıdaki hayvanlardan hangisinin tüyleri alınmamış ham derisi 41. Fasılda sınıflandırılır?",
   "secenekler": ["Ren geyiği", "Astragan kuzusu", "Yemen keçisi", "Moğol kuzusu", "Tibet oğlağı"],
   "cevap": "A", "tip": FN,
   "gerekce": "Not 1(c) uyarınca tüylü hayvanların tüylü ham derileri kural olarak Fasıl 43’tedir; ancak sığır, at, koyun-kuzu, keçi-oğlak, domuz, dağ keçisi, ceylan, deve, geyik, ren geyiği, karaca ve köpeğin tüylü ham derileri Fasıl 41’de kalır. Astragan ve Moğol kuzuları ile Yemen ve Tibet keçi-oğlakları bu istisnanın dışında tutulduğundan Fasıl 43’e gider.",
   "dayanak": "Fasıl 41 Not 1(c)."
  },
  {
   "soru": "Tarife Cetveline göre, dabaklandıktan sonra boyanmış, yağla beslenmiş, yumuşatılmış ve baskıyla desen verilmiş timsah derisi hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.06", "41.03", "41.14", "41.13", "42.05"],
   "cevap": "D", "tip": E4,
   "gerekce": "41.13, 41.07 ve 41.12 dışındaki hayvanların (sürüngenler dahil) dabaklama veya crust sonrası ileri derecede hazırlanmış derilerini kapsar. Yalnız dabaklanmış veya crust halde olsaydı 41.06’da, ham olsaydı 41.03’te olurdu. Güderi, rugan veya metalize olmadığından 41.14; eşya olmadığından 42.05 söz konusu değildir.",
   "dayanak": "41.13 pozisyon metni ve Açıklama Notu; Fasıl 41 Genel Açıklamalar (III)."
  },
  {
   "soru": "Aşağıdakilerden hangisi 41.15 pozisyonunda <b>sınıflandırılmaz</b>?",
   "secenekler": [
    "Deri kırpıntılarının tutkalla birleştirilmesiyle elde edilen levha",
    "Plastik esaslı, deri görünümlü taklit deri levha",
    "Deri liflerinin hamur haline getirilip haddeden geçirilmesiyle elde edilen levha",
    "Derinin zımparalanmasından arta kalan deri tozu",
    "Deri eşya imaline uygun olmayan dabaklanmış deri kırpıntıları"
   ],
   "cevap": "B", "tip": OT,
   "gerekce": "41.15 yalnız esası deri veya deri lifi olan terkip deriyi kapsar; plastik esaslı taklit deriler Fasıl 39’da (kauçuk esaslılar Fasıl 40’ta, kağıt esaslılar Fasıl 48’de, sıvanmış mensucat Fasıl 59’da) yer alır. Diğer seçenekler terkip deri veya deri döküntüsü olarak 41.15’tedir.",
   "dayanak": "Fasıl 41 Not 3; 41.15 Açıklama Notu."
  },
  {
   "soru": "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda sınıflandırılır?",
   "secenekler": [
    "Eşya imaline uygun olmayan dabaklanmış deri kırpıntıları",
    "Deri talaşı ve tozu",
    "Ham post ve derilerin kırpıntıları",
    "Deri unu",
    "Kullanılamayacak durumda ekşimiş deri eşya"
   ],
   "cevap": "C", "tip": FA,
   "gerekce": "Fasıl 41 Not 1(a), ham post ve derilerin kırpıntı ve benzeri döküntülerini 05.11’e (Fasıl 5) gönderir. Dabaklanmış deri kırpıntıları, deri talaşı-tozu, deri unu ve kullanılamaz deri eşya 41.15’tedir.",
   "dayanak": "Fasıl 41 Not 1(a); 41.15 Açıklama Notu."
  },
  {
   "soru": "41.14 Açıklama Notuna göre boşlukları doğru tamamlayan seçenek hangisidir? “Ruganla kaplanmış deri ve köseleler; kalınlığı ..... geçen, fakat tüm deri kalınlığının ..... daha az kalınlıkta plastikle kaplanmış, ayna gibi parlak derilerdir.”",
   "secenekler": ["0,5 mm’yi – üçte birinden", "0,15 mm’yi – yarısından", "0,15 mm’yi – üçte birinden", "1 mm’yi – yarısından", "0,25 mm’yi – dörtte birinden"],
   "cevap": "B", "tip": ES,
   "gerekce": "41.14 Açıklama Notuna göre rugan derilerde kaplama 0,15 mm’yi geçmez; ruganla kaplanmış derilerde plastik tabaka 0,15 mm’yi geçer ama toplam deri kalınlığının yarısından azdır. Kaplaması 0,15 mm’den az olmayan ve toplam kalınlığın yarısını aşan plastik kaplı deriler Fasıl 39’dadır.",
   "dayanak": "41.14 Açıklama Notu (II)."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur? I. Tüyleri alınmamış ham sığır derileri Fasıl 41’de yer alır. II. Tüyleri alınmamış ham Moğol keçisi derisi Fasıl 41’de yer alır. III. Tüyleri alınmamış ham köpek derisi Fasıl 41’de yer alır. IV. Kılı ile birlikte dabaklanmış sığır derisi Fasıl 43’te yer alır.",
   "secenekler": ["I ve II", "II ve IV", "I, II ve III", "II, III ve IV", "I, III ve IV"],
   "cevap": "E", "tip": CC,
   "gerekce": "Not 1(c) gereği sığır (I) ve köpeğin (III) tüylü ham derileri Fasıl 41’de kalır. Moğol keçisi istisnanın dışında tutulduğundan tüylü ham derisi Fasıl 43’tedir (II yanlış). Not 1(c)’deki istisna yalnız ham deriler içindir; kılıyla dabaklanmış deriler Fasıl 43’e gider (IV doğru; 41.04 hariç tutması).",
   "dayanak": "Fasıl 41 Not 1(c); 41.04 Açıklama Notu, hariç tutma (c)."
  },
  {
   "soru": "Tarife Cetvelinin 41. Fasıl notlarına göre, tarifenin neresinde geçerse geçsin “terkip yoluyla elde edilen deri ve kösele” tabiri hangisini ifade eder?",
   "secenekler": [
    "Yalnız 41.15 pozisyonuna giren maddeleri",
    "Plastik veya kauçuk esaslı tüm taklit derileri",
    "Deri görünümü verilmiş sıvanmış dokumaya elverişli mensucatı",
    "41.14 pozisyonundaki rugan ve metalize derileri",
    "Deri kırpıntısı içeren her türlü levha ve yaprağı"
   ],
   "cevap": "A", "tip": FN,
   "gerekce": "Fasıl 41 Not 3, “terkip yoluyla elde edilen deri ve kösele” tabirinin tarifenin her yerinde yalnız 41.15’e giren maddeleri, yani esası deri veya deri lifi olan levha, yaprak ve şeritleri ifade ettiğini belirtir. Plastik, kauçuk veya sıvanmış mensucat esaslı taklitler bu tabire girmez.",
   "dayanak": "Fasıl 41 Not 3; 41.15 Açıklama Notu."
  },
  {
   "soru": "Aşağıdakilerden hangisi 41.03 pozisyonunda <b>yer almaz</b>?",
   "secenekler": [
    "Tuzlanmış, yenilmeyen ham balık derisi",
    "Kılları alınmış ham Tibet keçisi derisi",
    "Kurutulmuş ham sürüngen derisi",
    "Telek ve tüyleri alınmamış kuş derisi",
    "Kılları alınmamış ham köpek derisi"
   ],
   "cevap": "D", "tip": OT,
   "gerekce": "Telek ve tüyleri alınmamış kuş derileri ve parçaları Not 1(b) gereği 05.05 veya 67.01’dedir. 41.03; balık ve sürüngen derilerini, kılları alınmış keçi derilerini (Tibet keçisi dahil) ve tüylü köpek derisini kapsar. Tibet keçisi derisi ancak kılları alınmamışsa Fasıl 43’e gider.",
   "dayanak": "Fasıl 41 Not 1(b) ve (c); 41.03 Açıklama Notu."
  },
  {
   "soru": "Tarife Cetveline göre, dabaklandıktan sonra ince altın renkli metal yaprakla kaplanmış keçi derisi hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.13", "41.06", "41.14", "41.15", "39.21"],
   "cevap": "C", "tip": E4,
   "gerekce": "41.14, metal tozları veya metal yapraklarla (altın, gümüş, bronz, alüminyum gibi) kaplanmış metalize deri ve köseleleri kapsar; bu nedenle ileri hazırlanmış keçi derisi pozisyonu 41.13 yerine 41.14 uygulanır. Terkip yoluyla elde edilen derinin metalize olanı ise 41.15’tedir.",
   "dayanak": "41.14 pozisyon metni ve Açıklama Notu (II)(3); 41.13 pozisyon metni."
  },
  {
   "soru": "Kılları alınmamış, tuzlanmış ham at derisinin pozisyonu ve sınıflandırma kuralı hangi seçenekte doğru verilmiştir?",
   "secenekler": ["41.01 – GYK 1 ve 6", "43.01 – GYK 1 ve 6", "41.01 – GYK 3(a) ve 6", "43.01 – GYK 3(c) ve 6", "41.03 – GYK 4 ve 6"],
   "cevap": "A", "tip": GY,
   "gerekce": "Fasıl 41 başlığı “kürkler hariç” dese de başlıklar yalnız gösterici niteliktedir (GYK 1). Not 1(c) at türü hayvanların tüylü ham derilerini açıkça Fasıl 41’de bırakır ve 41.01 metni “kılları alınmış olsun olmasın” ifadesini taşır. Sınıflandırma pozisyon metni ve notla yapıldığından GYK 3 veya 4’e gerek yoktur.",
   "dayanak": "GYK 1; Fasıl 41 Not 1(c); 41.01 pozisyon metni."
  },
  {
   "soru": "Aşağıdaki hayvan derilerinden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
   "secenekler": [
    "Kireçlenmiş ham keçi derisi",
    "Pikle edilmiş ham koyun derisi",
    "Pişmemiş, yenilebilir domuz derisi",
    "Kurutulmuş ham at derisi",
    "Kurutulmuş ham yılan derisi"
   ],
   "cevap": "C", "tip": FA,
   "gerekce": "41.01–41.03 Açıklama Notları yenilebilir, pişmemiş hayvan derilerini Fasıl 2’ye (02.06 veya 02.10), pişmiş olanlarını 16.02’ye gönderir. Kireçlenmiş keçi, pikle koyun, kurutulmuş at ve yılan derileri dabaklamaya hazır ham deriler olarak Fasıl 41’dedir (41.01, 41.02, 41.03).",
   "dayanak": "41.01, 41.02, 41.03 Açıklama Notları ve hariç tutmalar."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur? I. Deri kırpıntılarının bağlayıcıyla birleştirilmesiyle elde edilen levhalar 41.15’tedir. II. Deri liflerinin hamur haline getirilip haddeden geçirilmesiyle elde edilen levhalar 41.15’tedir. III. Kare veya dikdörtgen dışında özel biçimde kesilmiş terkip deri parçaları 41.15’tedir. IV. Deri eşya imaline elverişli deri kırpıntıları 41.15’tedir.",
   "secenekler": ["I, II ve III", "II ve IV", "I ve III", "II, III ve IV", "I ve II"],
   "cevap": "E", "tip": CC,
   "gerekce": "41.15 Açıklama Notu, deri kırpıntılarının bağlayıcıyla veya basınçla birleştirilmesiyle ya da lif haline getirilip hamurlaştırılarak haddelenmesiyle elde edilen levhaları kapsar (I, II). Kare veya dikdörtgen dışında kesilmiş terkip deriler başka fasıllarda, özellikle Fasıl 42’dedir (III yanlış). Deri eşya imaline elverişli kırpıntılar deri olarak 41.07 veya 41.12–41.14’te sınıflandırılır (IV yanlış).",
   "dayanak": "41.15 Açıklama Notu (I) ve (II)."
  },
  {
   "soru": "Aşağıdakilerden hangisi 41.14 pozisyonunda <b>yer almaz</b>?",
   "secenekler": [
    "Balık yağıyla dabaklanmış koyun güderisi",
    "Formaldehit ve şapla dabaklanmış yıkanabilir deri",
    "Formaldehitle kısmen, ardından yağla dabaklanmış kombine güderi",
    "Gümüş yaprakla kaplanmış metalize deri",
    "Lakla kaplanmış, ayna gibi parlak rugan deri"
   ],
   "cevap": "B", "tip": OT,
   "gerekce": "41.14 Açıklama Notu, formaldehit ve şapla dabaklanmış diğer yıkanabilir derileri ve başka usulle dabaklanıp yalnız yağla doldurulmuş derileri bu pozisyonun dışında tutar; bunlar hayvan türüne göre 41.07, 41.12 veya 41.13’e gider. Yağla dabaklanmış güderi, kombine güderi, rugan ve metalize deri 41.14’tedir.",
   "dayanak": "41.14 Açıklama Notu (I) ve (II)."
  },
  {
   "soru": "Tarife Cetveline göre, telek ve tüyleri alınmış, tuzlanarak muhafaza edilmiş ve dabaklanmamış devekuşu derisi hangi pozisyonda sınıflandırılır?",
   "secenekler": ["05.05", "41.06", "67.01", "41.03", "43.01"],
   "cevap": "D", "tip": E4,
   "gerekce": "41.03 Açıklama Notu, telek ve tüyleri alınmış kuş derilerini diğer ham deriler arasında sayar. Telek ve tüyleri alınmamış olsaydı Not 1(b) gereği 05.05 veya 67.01’de olurdu; dabaklanmadığından 41.06’ya, kürk olmadığından 43.01’e gitmez.",
   "dayanak": "41.03 Açıklama Notu; Fasıl 41 Not 1(b)."
  },
  {
   "soru": "Aşağıdaki derilerin pozisyonlarla eşleştirilmesi hangi seçenekte doğru verilmiştir? I. Kılları alınmış, kromla dabaklanmış, yaş haldeki (wet-blue) at derisi; II. Yünü alınmış, dabaklanıp ara kurutulmuş (crust) koyun derisi; III. Dabaklandıktan sonra boyanmış ve baskıyla desen verilmiş domuz derisi; IV. Dabaklandıktan sonra yağla beslenmiş, boyanmış ve perdahlanmış sığır derisi — a) 41.04 b) 41.05 c) 41.13 d) 41.07",
   "secenekler": [
    "I-a, II-c, III-b, IV-d",
    "I-d, II-b, III-c, IV-a",
    "I-a, II-b, III-d, IV-c",
    "I-b, II-a, III-c, IV-d",
    "I-a, II-b, III-c, IV-d"
   ],
   "cevap": "E", "tip": ES,
   "gerekce": "Dabaklanmış veya crust at derisi 41.04’te, koyun derisi 41.05’tedir. Dabaklama sonrası ileri hazırlanmış domuz derisi 41.13’te, sığır derisi 41.07’dedir. Hayvan sırası her aşamada aynıdır: sığır-at, koyun-kuzu, diğerleri.",
   "dayanak": "41.04, 41.05, 41.07, 41.13 pozisyon metinleri; Fasıl 41 Not 2(B)."
  },
  {
   "soru": "Bir işletme; sırçası giderilmiş koyun derilerinin yaş yarmalarını kısmen yağdan arındırmış, balık yağıyla tekrarlanan işlemlerle dabaklamış ve sünger taşıyla yumuşatmıştır. Elde edilen sarı renkli, yumuşak ve yıkanabilir deriler temizlik bezi ve eldiven imalinde kullanılacaktır. Bu ürün Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.14", "41.12", "41.05", "41.15", "43.02"],
   "cevap": "A", "tip": SN,
   "gerekce": "Balık yağı veya diğer hayvansal yağlarla dabaklanan, yumuşaklığı, sarı rengi ve yıkanabilirliği ile tanınan bu deriler güderidir ve 41.14’te sınıflandırılır. Koyun derisi olması onu 41.05 veya 41.12’ye götürmez; bu pozisyonlar güderiyi açıkça hariç tutar. Yünü bulunmadığından Fasıl 43 söz konusu değildir.",
   "dayanak": "41.14 Açıklama Notu (I); 41.05 ve 41.12 hariç tutmaları."
  },
  {
   "soru": "Tarife Cetveline göre aşağıdaki bitirilmiş derilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
   "secenekler": [
    "Kılları alınmış, dabaklama sonrası boyanıp perdahlanmış sığır yarma derisi",
    "Bitkisel dabaklı, silindirle sertleştirilmiş sığır taban köselesi",
    "Yağla dabaklanmış geyik güderisi",
    "Makine kayışı imaline mahsus, yağlanıp aprelenmiş öküz derisi",
    "Kromla dabaklanmış, renkli ve cilalı dana derisi (box-calf)"
   ],
   "cevap": "C", "tip": FA,
   "gerekce": "Yağla dabaklanmış güderi, hangi hayvandan elde edilirse edilsin 41.14’tedir. Bitirilmiş yarma deri, taban köselesi, makine kayışı derisi ve box-calf, sığır derilerinin dabaklama sonrası ileri hazırlanmış halleri olarak 41.07’dedir.",
   "dayanak": "41.07 ve 41.14 Açıklama Notları."
  },
  {
   "soru": "Yeni doğmuş buzağı derisi; dabaklanmadan, kılları alınıp yağ ve etleri giderilmiş, çerçeveye gerilmiş, sönmüş kireç içeren hamurla sıvanmış, istenen kalınlığa kadar tıraşlanmış, sünger taşıyla ovulmuş ve jelatinle sepilenmiştir. Kaliteli kitap ciltlemesinde kullanılacak bu ürün Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.01", "41.04", "41.14", "41.07", "41.15"],
   "cevap": "D", "tip": SN,
   "gerekce": "Parşömine deriler dabaklanmaz, kendi muhafazasını sağlayan işlemlerle hazırlanır; yeni doğmuş buzağı derisinden yapılan kaliteli çeşide vellum denir. 41.07 pozisyon metni “parşömine edilmiş deri dahil” ifadesini taşırken ham deri pozisyonu 41.01 parşömine edilmemiş olmayı şart koşar. Tuzak, “dabaklanmamış” ifadesini ham deri sanmaktır.",
   "dayanak": "41.01 ve 41.07 pozisyon metinleri; Fasıl 41 Genel Açıklamalar (III)."
  },
  {
   "soru": "Tarife Cetvelinin 41. Fasıl notlarına göre, bölme işlemini kolaylaştırmak için geri alınabilir hafif bir ön dabaklamaya tabi tutulmuş, kılları alınmış sığır derisi hangi pozisyonda sınıflandırılır?",
   "secenekler": ["41.04", "41.01", "41.07", "41.06", "43.02"],
   "cevap": "B", "tip": FN,
   "gerekce": "Not 2(A) gereği 41.04–41.06 geri alınabilir dabaklama (ön dabaklama dahil) görmüş deri ve postları kapsamaz; bunlar ham deri pozisyonlarında (sığır için 41.01) kalır. Genel Açıklamalara göre bu deriler bitirilmeden önce ileri dabaklama gerektirir ve dabaklanmış deri sayılmaz.",
   "dayanak": "Fasıl 41 Not 2(A); 41.01 Açıklama Notu; Fasıl 41 Genel Açıklamalar (I)."
  }
 ]
}

out = os.path.join(KITAP, "data", "fasil_41.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("yazıldı:", out)
