from yardim_78_83 import soru, kaydet

E4 = "Eşya → 4’lü pozisyon"
OT = "Olumsuz teşhis"
FA = "Farklı/aynı pozisyon veya fasıl"
FN = "Fasıl notu · Tanım/Eşik"
GY = "Genel Yorum Kuralı"
EB = "Eşleştirme / Boşluk doldurma"
CC = "Çoktan-çoğa (I–IV)"
SN = "Senaryo"

obj = {
 "tur": "fasil",
 "fasil": 83,
 "baslik": "Adi metallerden çeşitli eşya",
 "bolum": "XV",
 "oz": {
  "vurgu": "Fasıl 83, Fasıl 82 gibi eşyanın yapıldığı adi metale bakmaz: kilit, donanım, kasa, büro eşyası, zil-süs-çerçeve, bükülebilir boru, toka-kopça, tıpa-kapak, levha ve kaplı kaynak elektrotları hangi adi metalden olursa olsun buradadır. Sorulacak soru, eşyanın bu on bir pozisyondan birinde adıyla sayılıp sayılmadığıdır; sayılmışsa 72–76 ve 78–81. Fasıllara gitmez (Bölüm XV Not 2).",
  "maddeler": [
   "83.01 kilitler ve anahtarlar; 83.02 mobilya, kapı, pencere, karoseri, bavul ve saraciye donanımı, sabit askılar, küçük tekerlekler, otomatik kapı kapayıcılar; 83.03 kasalar.",
   "83.04 masa üstü büro eşyası; 83.05 klasör mekanizması, ataş, kağıt raptiyesi, şerit halinde zımba teli; 83.06 elektriksiz zil ve çan, süs eşyası, çerçeve ve metal ayna.",
   "83.07 eğilip bükülebilir borular; 83.08 kopça, toka, bağ deliği kapsülü, boru şeklinde veya yarık saplı perçin, boncuk ve pul; 83.09 tıpa, kapak, kapsül, mühür; 83.10 esaslı bilgi taşıyan levhalar; 83.11 kaplanmış veya içi doldurulmuş kaynak elektrotları.",
   "Yay, zincir, kablo, vida, cıvata, somun ve çivi, Fasıl 83 eşyası için özel yapılmış olsa da parça sayılmaz; kendi pozisyonlarına gider (Fasıl 83 Not 1).",
   "Küçük tekerlek (83.02): çapı bandajı dahil 75 mm’yi geçmeyen ya da çapı 75 mm’yi geçse bile tekerlek veya bandaj genişliği 30 mm’den az olan tekerlek (Fasıl 83 Not 2)."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Vida, cıvata, somun, çivi, zincir, yay veya kablo mu?", "Kendi pozisyonu: <b>73.12</b>, <b>73.15</b>, <b>73.17</b>, <b>73.18</b>, <b>73.20</b> veya diğer metal fasılları (Fasıl 83 Not 1)"],
   ["2", "Anahtarla, şifreyle veya elektrikle çalışan kilit, kilitli kanca ya da anahtar mı?", "<b>83.01</b>"],
   ["3", "Mobilya, kapı, pencere, karoseri, bavul, saraciye donanımı; sabit askı; küçük tekerlek*; otomatik kapı kapayıcı mı?", "<b>83.02</b> (mobilya görünümlü portmanto Fasıl 94)"],
   ["4", "Zırhlı kasa, kasa dairesi kapısı veya bölmesi, emniyetli kutu mu?", "<b>83.03</b> (konut tipi çelik güvenlik kapısı 73.08)"],
   ["5", "Masa üstü büro eşyası mı (dosya kutusu, kalem kutusu, hokka)?", "<b>83.04</b> (büro mobilyası 94.03)"],
   ["6", "Klasör mekanizması, ataş, kağıt raptiyesi, şerit halinde zımba teli mi?", "<b>83.05</b> (pünez 73.17 / 74.15)"],
   ["7", "Elektriksiz zil, çan, gong; süs eşyası; çerçeve veya metal ayna mı?", "<b>83.06</b> (cam ayna 70.09; elektrikli zil 85.31)"],
   ["8", "Eğilip bükülebilir boru mu?", "<b>83.07</b> (makine veya taşıt aksamı haline gelmişse Bölüm XVI–XVII)"],
   ["9", "Kopça, toka, bağ deliği kapsülü, boru şeklinde veya yarık saplı perçin, boncuk, pul mu?", "<b>83.08</b> (çıtçıt 96.06; fermuar 96.07)"],
   ["10", "Tıpa, kapak, kapsül, mühür veya benzeri ambalaj teferruatı mı?", "<b>83.09</b>"],
   ["11", "Esaslı bilgileri taşıyan levha, tabela, harf, rakam mı?", "<b>83.10</b> (ışıklı ise 94.05)"],
   ["12", "Eritici veya temizleyici madde ile kaplanmış ya da içi doldurulmuş kaynak teli, çubuğu, elektrodu mu?", "<b>83.11</b>"]
  ],
  "dipnot": "* Küçük tekerlek: çapı (bandaj dahil) 75 mm’yi geçmeyen ya da çapı 75 mm’yi geçse bile tekerlek veya bandaj genişliği 30 mm’den az olan tekerlek; donanımı adi metalden olmalıdır (Fasıl 83 Not 2)."
 },
 "pozisyon_haritasi": [
  ["83.01", "Kilitler, asma kilitler; kilitli kancalar; anahtarlar", "Anahtarlı, şifreli, elektrikli; anahtar taslakları dahil", "Kapı kilidi, bavul asma kilidi, kartlı otel kilidi"],
  ["83.02", "Donanım ve tertibat; askılar; küçük tekerlekler; kapı kapayıcılar", "Genel amaçlı donanım, özel kullanım için olsa da", "Menteşe, kapı kolu, perde rayı, mobilya tekerleği"],
  ["83.03", "Kasalar, zırhlı kapı ve bölmeler, emniyetli kutular", "Delme ve kesmeye dayanıklı güvenlik", "Banka kasası, kasa dairesi kapısı"],
  ["83.04", "Masa üstü büro eşyası", "94.03 büro mobilyası hariç", "Dosya kutusu, kalem kutusu, kitap desteği"],
  ["83.05", "Klasör mekanizması, ataş, raptiye; şerit zımba teli", "Kağıt iliştirme ve işaretleme", "Halkalı mekanizma, ataş, zımba teli"],
  ["83.06", "Elektriksiz zil, çan; süs eşyası; çerçeve; metal ayna", "Süs niteliği ağır basan eşya", "Bisiklet zili, kupa, heykelcik, fotoğraf çerçevesi"],
  ["83.07", "Eğilip bükülebilir borular", "Bağlantı parçalı olsun olmasın", "Spiral metal hortum, termostatik körük"],
  ["83.08", "Kopça, toka, bağ deliği kapsülü; boru şeklinde perçin; boncuk, pul", "Giyim, ayakkabı, çanta ve diğer hazır eşya için", "Kemer tokası, kör perçin, metal pul"],
  ["83.09", "Tıpa, kapak, kapsül, mühür ve ambalaj teferruatı", "Ağız kapama ve mühürleme", "Dişli şişe kapağı, çekme halkalı kapak, kurşun mühür"],
  ["83.10", "İşaret levhaları, tabelalar, harfler, rakamlar", "Esaslı bilgiyi taşıyan; ışıklılar hariç", "Trafik levhası, otomobil plakası, makine isim levhası"],
  ["83.11", "Kaplanmış veya içi doldurulmuş kaynak elektrotları ve telleri", "Eritici veya temizleyici madde şart", "Kaplanmış ark kaynağı elektrodu, özlü kaynak teli"]
 ],
 "notlar": [
  ["Bölüm XV Not 2", "Genel kullanıma mahsus aksam: (a) 73.07, 73.12, 73.15, 73.17, 73.18 eşyası ve diğer adi metallerden benzerleri; (b) yaylar (saat zemberekleri hariç); (c) 83.01, 83.02, 83.08, 83.10 eşyası ile 83.06’daki çerçeve ve aynalar. Fasıl 83 Not 1 saklı kalmak kaydıyla, 82 veya 83. Fasıl eşyası 72–76 ve 78–81. Fasıllara verilmez."],
  ["Fasıl 83 Not 1", "Adi metal aksam, ait olduğu eşyanın pozisyonunda sınıflandırılır. Ancak 73.12, 73.15, 73.17, 73.18 veya 73.20’deki demir-çelik eşya ile diğer adi metallerden benzerleri (74–76 ve 78–81. Fasıllar) Fasıl 83 eşyasının aksam ve parçası sayılmaz."],
  ["Fasıl 83 Not 2", "83.02 anlamında küçük tekerlekler: çapı (bandaj dahil) <b>75 mm’yi geçmeyen</b> veya çapı 75 mm’yi geçse bile tekerlek ya da bandaj genişliği <b>30 mm’den az</b> olan tekerlekler."],
  ["Genel Açıklamalar", "73–76 ve 78–81. Fasıllarda yer metale göre belirlenirken bu fasıl, Fasıl 82 gibi, imal edildiği adi metal ne olursa olsun belli eşyayı kapsar. Yaylar (kilitler için özel olsa da), zincirler, kablolar, cıvata, somun, vida ve çiviler bu fasılda değildir."],
  ["83.01 Açıklama Notu", "Anahtarla, harf veya rakam şifresiyle ya da elektrikle (manyetik kart, klavye, radyo sinyali) çalışan kilitler; kilitli kancalar; kilit aksamı (dil, muhafaza, mekanizma); bitmiş veya bitmemiş anahtarlar (kaba döküm, dövme veya ıstampa ile şekil verilmiş anahtar taslakları dahil). Hariç: çantalar için basit kilit mandalları (83.02) ve anahtarsız basit kapamalar, kopçalar (83.08)."],
  ["83.02 Açıklama Notu", "Mobilya, kapı, pencere, karoseri vb. üzerinde kullanılan genel amaçlı donanım; otomobil kapı kolu veya menteşesi gibi özel kullanım için yapılmış olsa da burada. Esas aksam niteliğindeki parçalar (pencere çerçevesi, döner koltuk mekanizması) hariç. Küçük tekerleğin donanımı adi metalden olmalı, tekerlek herhangi bir maddeden olabilir (kıymetli metal hariç); şartlara uymayanlar başka fasıllara (ör. Fasıl 87) gider. Portmanto gibi mobilya görünümlü askılar Fasıl 94’tedir."],
  ["83.03 Açıklama Notu", "Kasalar ve zırhlı dolaplar; kasa dairesi kapıları ve bölmeleri; emniyetli çekmece ve kutular; benzer güvenlik şartlarını taşıyan para ve koleksiyon kutuları (aksi halde metaline göre veya oyuncak). Hariç: konut tipi çelik güvenlik kapıları (73.08); delme ve kesmeye ciddi direnç göstermeyen yangına dayanıklı konteynerler (94.03)."],
  ["83.04 ve 83.05 Açıklama Notları", "83.04: masa üstü dosya, fiş, tasnif kutuları, kağıtlıklar, kalem kutuları, hokkalar, evrak ağırlıkları, kitap destekleri; atık kağıt sepetleri metaline göre (ör. 73.26). 83.05: klasör ve cilt mekanizmaları, ataş, kağıt raptiyesi, köşebent, işaret maşası, şerit halinde zımba telleri; pünezler (73.17, 74.15) ile kitap kapama tertibatı (83.01, 83.08) hariç."],
  ["83.06 Açıklama Notu", "(A) Elektriksiz zil, çan, gong (bisiklet, kapı, masa, hayvan çanları dahil); elektrikli ziller 85.31, saat gongları 91.14, müzik aleti niteliğindeki çanlar 92.06 / 92.07, oyuncaklar 95.03. (B) Süs eşyası: süs vasfı galip eşya; süsü işlevini azaltmayan ev eşyası kendi pozisyonunda kalır (73.23, 74.18, 76.16). (C) Adi metal çerçeveler ve metal aynalar; metal çerçeveli cam aynalar 70.09’dadır. Barometre-termometre (Fasıl 90), saat kasaları (Fasıl 91), masa çakmakları (96.13) hariç."],
  ["83.07 Açıklama Notu", "Helezoni sarılmış şeritten veya ondüleli borulardan bükülebilir borular; örgü kılıflı olanlar, Bowden kablosu kılıfları, termostatik körükler ve bağlantı parçalı olanlar dahil. Hariç: dışı metalle takviye edilmiş kauçuk borular (40.09); makine veya taşıt aksamı haline getirilmiş borular (Bölüm XVI–XVII)."],
  ["83.08 Açıklama Notu", "Kopçalar, bağ deliği kapsülleri; boru şeklinde veya yarık saplı perçinler (kör perçinler dahil); çanta, kitap, kol saati kapamaları (kilitliler 83.01); tokalar; metal boncuk ve kesilmiş pullar. Hariç: tokalar dışındaki süsler (71.17), diğer perçinler (73–76. Fasıllar), çıtçıtlar (96.06), fermuarlar (96.07)."],
  ["83.09 Açıklama Notu", "Dişli tıpalar ve kapaklar, varil kapakları, boşaltıcı tıpalar, yırtılabilen kapsüller, kurşun veya kalay yapraktan kapsüller, şampanya mantarı telleri, kurşun veya kalay sactan mühürler, sandık köşelikleri, çekme halkalı alüminyum kolay açılır kapaklar. Esası porselen veya plastik olan mekanizmalı tıpalar hariç."],
  ["83.10 Açıklama Notu", "Esaslı bilgileri (harf, sayı, kelime, desen) taşıyan levhalar: yol ve cadde levhaları, tabelalar, reklam levhaları, adres levhaları, anahtar ve vestiyer etiketleri, makine isim levhaları, otomobil plakaları. Hariç: yalnız tesadüfi bilgi taşıyan levhalar (metaline göre), matbaa harfleri (84.42), daktilo harfleri (84.73), demiryolu işaret levhaları (86.08), ışıklı tabelalar (94.05); stensil levhalar metaline göre."],
  ["83.11 Açıklama Notu", "Lehim ve kaynak için eritici veya temizleyici madde (çinko klorür, boraks, reçine vb.) ile kaplanmış ya da içi doldurulmuş tel, çubuk, boru, levha ve elektrotlar ile metal püskürtmede kullanılan aglomere metal tozu tel ve çubuklar. Kaplamasız olanlar 72–76 ve 78–81. Fasıllarda; eritici dışında ağırlıkça <b>%2 veya daha fazla</b> kıymetli metal alaşımı içeren lehimler Fasıl 71’dedir."]
 ],
 "sinir_komsulari": [
  ["Kilit için özel çelik yay; çelik vida, cıvata, zincir", "73.20 / 73.18 / 73.15", "Fasıl 83 Not 1"],
  ["Konut tipi çelik güvenlik kapısı", "73.08", "83.03 hariç tutması"],
  ["Delme ve kesmeye dayanıksız, yangına dayanıklı konteyner", "94.03", "83.03 hariç tutması"],
  ["Raflı, mobilya görünümlü portmanto; büro mobilyası", "Fasıl 94", "83.02 ve 83.04 Açıklama Notları"],
  ["Çelikten atık kağıt sepeti", "73.26", "83.04 hariç tutması"],
  ["Pünez", "73.17 / 74.15", "83.05 hariç tutması"],
  ["Metal çerçeveli cam ayna", "70.09", "83.06 hariç tutması"],
  ["Elektrikli zil ve işaret cihazları", "85.31", "83.06 hariç tutması"],
  ["Süslü barometre ve termometre; saat kasası", "Fasıl 90 / Fasıl 91", "83.06 hariç tutması"],
  ["Çıtçıt; kayarak işleyen fermuar", "96.06 / 96.07", "83.08 hariç tutması"],
  ["Dışı metal takviyeli kauçuk boru", "40.09", "83.07 hariç tutması"],
  ["Işıklı isim tabelası", "94.05", "83.10 hariç tutması"],
  ["Matbaa harfleri ve rakamları", "84.42", "83.10 hariç tutması"],
  ["Kaplamasız çelik kaynak teli", "Fasıl 72", "83.11 Açıklama Notu"],
  ["Ağırlıkça %2 veya fazla kıymetli metal içeren hazır lehim", "Fasıl 71", "83.11 Açıklama Notu"]
 ],
 "tuzaklar": [
  "<b>Kilit mi, kapama mı?</b> Anahtarla, şifreyle veya elektrikle çalışan kapama 83.01; anahtarsız basit kilit mandalı 83.02; basit kopça ve çanta kapaması 83.08.",
  "<b>Yay ve vida Fasıl 83 parçası değildir.</b> Kilide özgü yay bile 73.20’de (veya diğer metal fasıllarında) kalır; vida, çivi ve zincir de öyle (Fasıl 83 Not 1).",
  "<b>Küçük tekerlekte iki ölçü vardır.</b> Çap 75 mm’yi geçmiyorsa küçük tekerlektir; geçiyorsa tekerlek veya bandaj genişliği 30 mm’den az olmalıdır. Pnömatik lastikte çap normal basınçta şişirilmiş halde ölçülür.",
  "<b>Bilgi taşımayan levha 83.10 değildir.</b> Esaslı bilgisi sonradan eklenecek levha ve etiketler metaline göre (73.25, 73.26, 76.16, 79.07) sınıflandırılır.",
  "<b>Ayna camdansa 70.09’dadır.</b> Metal ayna 83.06’da; metal çerçeveli cam ayna 70.09’da.",
  "<b>Her kasa 83.03 değildir.</b> Delmeye ve kesmeye ciddi direnç göstermeyen yangına dayanıklı konteyner 94.03’te; konut tipi çelik güvenlik kapısı 73.08’de.",
  "<b>Süslü ev eşyası süs eşyası sayılmaz.</b> Süsü işlevini azaltmayan tepsi ve kaseler kendi pozisyonunda (73.23, 74.18, 76.16); işlevini yitirecek kadar süslü olanlar 83.06’da.",
  "<b>Perçinin tipi pozisyonu belirler.</b> Boru şeklinde ve yarık saplı perçinler (kör perçin dahil) 83.08’de; diğer perçinler 73–76. Fasıllarda.",
  "<b>Taşıta takılsa da Fasıl 83’te kalır.</b> Otomobil kapı kolu 83.02’de, bisiklet zili 83.06’dadır; Bölüm XVII Not 2 bunları taşıt aksamı saymaz.",
  "<b>Ataş 83.05, pünez 73.17.</b> Kağıt raptiyesi, köşebent ve şerit halinde zımba teli 83.05’te; pünezler 83.05’ten hariçtir."
 ],
 "hafiza": {
  "kanca": "Kilit – kol – kasa – kalemlik – klasör – zil – hortum – toka – tıpa – tabela – elektrot (83.01 → 83.11)",
  "aciklama": "Bir binaya girin: <b>kilidi</b> açın (83.01), <b>kapı kolunu</b> çevirin (83.02), <b>kasanın</b> önünden geçin (83.03), masadaki <b>kalemliği</b> (83.04) ve <b>klasörü</b> (83.05) görün, <b>zili</b> çalın (83.06), bahçe <b>hortumunu</b> çekin (83.07), kemer <b>tokasını</b> takın (83.08), şişenin <b>tıpasını</b> açın (83.09), kapıdaki <b>tabelayı</b> okuyun (83.10) ve çıkışta kaynakçının <b>elektroduna</b> (83.11) bakın."
 },
 "sinav_odagi": [
  "Fasıl 73 ile karıştırma kalıbı: demir-çelikten olsa da şerit halinde zımba telinin 73. Fasılda değil 83.05’te yer alması (“hangisi 73. Fasılda yer almaz?”).",
  "Taşıt aksamı sanılan eşya: bisikletlerde kullanılan demir zillerin 87.14 veya 73.26 yerine 83.06’da sınıflandırılması.",
  "Anahtar taslaklarının sınıflandırılmasında GYK 2(a)’nın (bitmemiş eşya) kullanılması.",
  "Bölüm sorusu: adi metalden kapı kilidinin Bölüm XV’te, traş makinası, jeneratör ve valfin Bölüm XVI’da olması.",
  "83.07 (bükülebilir borular) gibi pozisyonların başka fasıllara ait eşya sorularında çeldirici olarak kullanılması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Tarife Cetveline göre bisikletlerde kullanılan demirden mamul ziller hangi tarife pozisyonundadır?",
   "secenekler": ["87.14", "73.26", "96.07", "83.06"],
   "cevap": "D",
   "aciklama": "83.06 elektriksiz zilleri imal edildiği adi metal ne olursa olsun kapsar; Açıklama Notu bisiklet zillerini açıkça sayar. Bölüm XVII Not 2(d), 83.06 eşyasını taşıt aksamından hariç tuttuğundan zil 87.14’e gitmez; Bölüm XV Not 2 de Fasıl 83 eşyasının Fasıl 73’e verilmesini engeller."
  },
  {
   "soru": "Aşağıdaki demir-çelikten mamul eşyalardan hangisi 73. Fasılda yer almaz?",
   "secenekler": ["Yay", "Filika demiri", "Somun", "Tığ", "Şerit halinde zımba teli"],
   "cevap": "E",
   "aciklama": "Bürolarda, döşemecilikte ve ambalajda kullanılan şerit halindeki zımba telleri 83.05’te adıyla sayılmıştır ve 73.17 metni bunları hariç tutar. Yay (73.20), filika demiri (73.16), somun (73.18) ve tığ (73.19) Fasıl 73’tedir."
  }
 ],
 "ozet": [
  "Fasıl 83 eşyası metali ne olursa olsun buradadır; Bölüm XV Not 2 bunları 72–76 ve 78–81. Fasıllardan çıkarır.",
  "01 kilit · 02 donanım-askı-küçük tekerlek · 03 kasa · 04 masa üstü büro · 05 klasör-ataş-zımba teli · 06 zil-süs-çerçeve-metal ayna.",
  "07 bükülebilir boru · 08 toka-kopça-boru perçin-pul · 09 tıpa-kapak-mühür · 10 bilgi taşıyan levha · 11 kaplı kaynak elektrodu.",
  "Yay, vida, zincir, çivi Fasıl 83 parçası sayılmaz (Not 1).",
  "Küçük tekerlek: çap 75 mm’ye kadar; daha büyükse genişlik 30 mm’den az (Not 2).",
  "Sınırlar: cam ayna 70.09, elektrikli zil 85.31, çıtçıt 96.06, fermuar 96.07, ışıklı tabela 94.05, pünez 73.17."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1
S.append(soru(
 "Tarife Cetveline göre, kaba dövme ile şekil verilmiş, dişleri henüz açılmamış çelik anahtar taslağı hangi pozisyonda sınıflandırılır?",
 ["73.26", "83.01", "72.28", "83.08", "73.18"], "B", E4,
 "83.01 Açıklama Notu, kilitlere mahsus bitirilmiş veya bitirilmemiş anahtarları, kaba döküm ile dövme veya ıstampa yoluyla şekil verilmiş anahtar taslakları dahil, açıkça bu pozisyona alır. Taslak anahtarın yaklaşık şeklini taşıdığından çelik çubuk (72.28) veya demir-çelik eşya (73.26) değildir; Bölüm XV Not 2 de Fasıl 83 eşyasını Fasıl 73’ten çıkarır.",
 "83.01 Açıklama Notu; Bölüm XV Not 2."))
# 2
S.append(soru(
 "Aşağıdakilerden hangisi 83.02 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Kapı menteşesi", "Adi metalden otomobil kapı kolu", "Duvara tespit edilen elbise askılığı", "Raflı, ayaklı ve mobilya görünümünde portmanto", "Bina kapıları için hidrolik otomatik kapı kapayıcı"], "D", OT,
 "83.02 Açıklama Notu, raflı elbise askıları (portmantolar) gibi mobilya görünümünü almış askıların Fasıl 94’te yer aldığını belirtir. Menteşeler, otomobil kapı kolları, sabit elbise askılıkları ve yaylı veya hidrolik otomatik kapı kapayıcılar 83.02’de sayılmıştır.",
 "83.02 Açıklama Notu (G) ve (H)."))
# 3
S.append(soru(
 "Fasıl 83 Not 2’ye göre, adi metal donanımlı aşağıdaki tekerleklerden hangisi 83.02 anlamında “küçük tekerlek” sayılır? (Çaplar bandaj dahildir.)",
 ["Çapı 100 mm, tekerlek genişliği 25 mm olan tekerlek", "Çapı 100 mm, tekerlek genişliği 35 mm olan tekerlek", "Çapı 90 mm, bandaj genişliği 30 mm olan tekerlek", "Çapı 120 mm, tekerlek genişliği 40 mm olan tekerlek", "Çapı 80 mm, bandaj genişliği 32 mm olan tekerlek"], "A", FN,
 "Fasıl 83 Not 2’ye göre küçük tekerlek, çapı 75 mm’yi geçmeyen veya çapı 75 mm’yi geçse bile tekerlek ya da bandaj genişliği 30 mm’den az olan tekerlektir. 100 mm çaplı ve 25 mm genişlikli tekerlek ikinci şartı sağlar. 30 mm genişlik “30 mm’den az” değildir; tuzak budur. Diğerlerinde hem çap 75 mm’yi geçer hem genişlik 30 mm veya daha fazladır.",
 "Fasıl 83 Not 2; 83.02 Açıklama Notu."))
# 4
S.append(soru(
 "Aşağıdaki eşyadan hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
 ["Kapı menteşesi", "Kitaplık rafı mesnedi", "Bavul köşe koruyucusu", "Pencere ispanyoleti", "Anahtarla çalışan çekmece kilidi"], "E", FA,
 "Anahtarla çalışan kilitler, mobilya kilitleri dahil 83.01’dedir. Menteşe, raf mesnedi, bavul köşe koruyucusu ve pencere ispanyoleti, mobilya, kapı, pencere ve seyahat eşyası için donanım ve tertibat olarak 83.02’de yer alır.",
 "83.01 ve 83.02 Açıklama Notları."))
# 5
S.append(soru(
 "Tarife Cetveline göre, içecek kutularında kullanılan, kolayca açılabilmesi için üstünde çekme halkası ve inceltilmiş kulakçığı bulunan alüminyum kapak hangi pozisyonda sınıflandırılır?",
 ["76.12", "76.16", "83.09", "83.08", "83.02"], "C", E4,
 "83.09 Açıklama Notu, içecek ve gıda kutularında kullanılan, çekme halkalı ve inceltilmiş kulakçıklı alüminyum kapakları açıkça sayar. Fasıl 83 eşyası, Bölüm XV Not 2 uyarınca alüminyum faslına (76.12, 76.16) verilmez. 83.08 kopça ve tokalar, 83.02 donanım içindir.",
 "83.09 Açıklama Notu; Bölüm XV Not 2."))
# 6
S.append(soru(
 "Tüm parçaları birlikte, demonte halde gümrüğe sunulan, bina kapıları için yaylı otomatik kapı kapayıcının 83.02 pozisyonunda sınıflandırılmasında hangi Genel Yorum Kuralları uygulanır?",
 ["GYK 1 ve 3(b)", "GYK 1 ve 2(a)", "GYK 1 ve 2(b)", "GYK 1 ve 3(c)", "GYK 1 ve 5(a)"], "B", GY,
 "GYK 2(a)’nın ikinci kısmına göre birleştirilmemiş veya demonte halde sunulan eşya, monte edilmiş eşya ile aynı pozisyonda sınıflandırılır; otomatik kapı kapayıcılar 83.02 metninde adıyla yer alır. Parçalar arasında yay bulunması sonucu değiştirmez; yay, kapı kapayıcı şeklini aldığında 83.02’dedir. 3(b), 3(c) ve 5(a) burada gerekli değildir.",
 "GYK 1 ve 2(a); 83.02 Açıklama Notu (H)."))
# 7
S.append(soru(
 "Fasıl 83 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Manyetik kart veya radyo sinyali ile çalışan elektrikli bina kapı kilitleri 83.01 pozisyonunda yer alır.<br/>II. Pünezler 83.05 pozisyonunda yer alır.<br/>III. Dışı metal ile takviye edilmiş kauçuk borular 83.07 pozisyonunda yer alır.<br/>IV. Çelik veya pirinçten metal aynalar 83.06 pozisyonunda yer alır.",
 ["I ve II", "I ve IV", "II ve III", "I, III ve IV", "II ve IV"], "B", CC,
 "83.01 elektrikli kilitleri ve manyetik kart, klavye veya radyo sinyali ile çalışanları açıkça kapsar (I doğru). Pünezler 83.05’ten hariç tutulmuş, 73.17 veya 74.15’e gönderilmiştir (II yanlış). Metal takviyeli kauçuk borular 40.09’dadır (III yanlış). Metal aynalar 83.06’dadır (IV doğru).",
 "83.01, 83.05, 83.06 ve 83.07 Açıklama Notları."))
# 8
S.append(soru(
 "Aşağıdakilerden hangisi 83.06 pozisyonunda <b>yer almaz</b>?",
 ["Elektriksiz kapı zili", "Hayvanlara takılan çan", "Adi metalden heykelcik", "Metal çerçeveli cam ayna", "Adi metalden fotoğraf çerçevesi"], "D", OT,
 "83.06 Açıklama Notu adi metalden çerçeveleri ve metal aynaları kapsar, ancak metal çerçeveli cam aynaları hariç tutarak 70.09’a gönderir. Elektriksiz kapı zilleri, hayvan çanları, heykelcikler ve fotoğraf çerçeveleri 83.06’da sayılmıştır.",
 "83.06 Açıklama Notu (A), (B) ve (C)."))
# 9
S.append(soru(
 "Eritici madde ile kaplanmış hazır lehim çubukları, eritici madde dışında ağırlıkça en az hangi oranda kıymetli metal alaşımı içerirse 83.11 yerine Fasıl 71’de sınıflandırılır?",
 ["%0,5", "%1", "%2", "%5", "%10"], "C", FN,
 "83.11 Açıklama Notu, eritici maddeler dışında ağırlıkça %2 veya daha fazla oranda kıymetli metal alaşımı içeren hazırlanmış lehim çubuk ve tellerini bu pozisyondan hariç tutarak Fasıl 71’e gönderir. Bölüm XV Genel Açıklamalarında da %2’den az kıymetli metal içeren alaşımlar adi metal alaşımı sayılır.",
 "83.11 Açıklama Notu; Bölüm XV Genel Açıklamalar (A)."))
# 10
S.append(soru(
 "Tarife Cetveline göre esaslı bilgileri taşıyan adi metal levhalar …… pozisyonunda; sabit ışık kaynağına sahip ışıklı isim tabelaları …… pozisyonunda; matbaa harfleri ve rakamları ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
 ["83.10 – 83.10 – 84.42", "94.05 – 83.10 – 84.73", "83.10 – 94.05 – 83.10", "83.06 – 94.05 – 84.42", "83.10 – 94.05 – 84.42"], "E", EB,
 "83.10, esaslı bilgileri taşıyan adi metal levhaları kapsar; aynı pozisyon metni 94.05’teki ışıklı tabelaları hariç tutar. 83.10 Açıklama Notu matbaa harflerini ve rakamlarını 84.42’ye, daktilo harflerini 84.73’e gönderir.",
 "83.10 pozisyon metni ve Açıklama Notu."))
# 11
S.append(soru(
 "Tarife Cetveline göre, mobilya ayağına takılan, çapı 50 mm olan, plastik tekerlekli ve adi metal donanımlı küçük tekerlek hangi pozisyonda sınıflandırılır?",
 ["87.16", "94.03", "39.26", "83.02", "73.26"], "D", E4,
 "Çapı 75 mm’yi geçmeyen tekerlek Fasıl 83 Not 2 anlamında küçük tekerlektir; 83.02 Açıklama Notuna göre donanımı adi metalden olmalı, tekerlek ise kıymetli metal dışında herhangi bir maddeden olabilir. Bölüm XV Not 2 bu eşyayı genel kullanım aksamı saydığından mobilya parçası (94.03) olarak da sınıflandırılmaz.",
 "Fasıl 83 Not 2; 83.02 Açıklama Notu; Bölüm XV Not 2."))
# 12
S.append(soru(
 "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir fasılda yer alır?",
 ["Konut tipi çelik güvenlik kapısı", "Banka kasası", "Kasa dairesi zırhlı kapısı", "Şifreli kilitli, taşınabilir emniyetli para kutusu", "Kasa dairesi zırhlı bölmesi"], "A", FA,
 "83.03 Açıklama Notu, tüm konut tipleri için çelik güvenlik kapılarını hariç tutarak 73.08’e gönderir. Kasalar, kasa dairesi zırhlı kapı ve bölmeleri ile güvenlik şartlarını taşıyan emniyetli para kutuları 83.03’te, yani Fasıl 83’tedir.",
 "83.03 Açıklama Notu."))
# 13
S.append(soru(
 "Bir otel zinciri; odalarda kullanılmak üzere, anahtar yerine manyetik kart ile açılan, elektronik kart okuyuculu ve adi metal gövdeli kapı kilitleri ithal etmektedir. Ürün hangi pozisyonda sınıflandırılır?",
 ["85.43", "85.31", "83.01", "83.02", "84.71"], "C", SN,
 "83.01 pozisyon metni adi metallerden anahtarlı, şifreli veya elektrikli kilitleri kapsar; Açıklama Notu manyetik kartın eklenmesiyle, klavyeden şifre girilmesiyle veya radyo sinyaliyle çalışan elektrikli kilitleri açıkça sayar. Elektronik okuyucu bulunması kilidi Fasıl 85’e götürmez; 83.02 kilitsiz donanım içindir.",
 "83.01 pozisyon metni ve Açıklama Notu."))
# 14
S.append(soru(
 "Aşağıdakilerden hangisi 83.08 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Kemer tokası", "Kayarak işleyen fermuar", "Ayakkabı bağ deliği kapsülü", "Boru şeklinde perçin", "Giysi süslemeye mahsus kesilmiş metal pul"], "B", OT,
 "83.08 Açıklama Notu kayarak işleyen fermuarları ve bunların aksamını hariç tutarak 96.07’ye gönderir; çıtçıtlar da 96.06’dadır. Kemer tokaları, bağ deliği kapsülleri, boru şeklindeki perçinler ve kesilmiş metal pullar 83.08’de sayılmıştır.",
 "83.08 Açıklama Notu."))
# 15
S.append(soru(
 "Fasıl 83 Not 1’e göre aşağıdakilerden hangisi, Fasıl 83 eşyasının aksamı olarak ait olduğu eşyanın pozisyonunda sınıflandırılır?",
 ["Kapı kilidine özgü çelik yay", "Asma kilit için çelik zincir", "Kilit için adi metal kilit dili ve silindirik muhafaza", "Menteşeyi tutturmaya mahsus çelik vida", "Kasaya mahsus çelik cıvata"], "C", FN,
 "Fasıl 83 Not 1’e göre adi metal aksam ait olduğu eşyanın pozisyonunda yer alır; 83.01 Açıklama Notu kilit dillerini ve silindirik muhafazaları kilit aksamı olarak sayar. Ancak 73.15 (zincir), 73.18 (vida, cıvata) ve 73.20 (yay) eşyası, Fasıl 83 eşyası için özel olsa da aksam sayılmaz.",
 "Fasıl 83 Not 1; 83.01 Açıklama Notu; Fasıl 83 Genel Açıklamalar."))
# 16
S.append(soru(
 "Bölüm XV Not 2’ye göre aşağıdaki pozisyonlardan hangisinin eşyası “genel kullanıma mahsus aksam ve parça” tanımına <b>girmez</b>?",
 ["83.01", "83.02", "83.08", "83.10", "83.09"], "E", FN,
 "Bölüm XV Not 2(c), 83.01, 83.02, 83.08 ve 83.10 eşyası ile 83.06’daki çerçeve ve aynaları genel kullanıma mahsus aksam sayar. 83.09’daki tıpa, kapak ve mühürler bu listede yer almaz. Tanımın önemi, örneğin taşıt veya mobilya aksamı sorularında bu eşyanın kendi pozisyonunda kalmasıdır.",
 "Bölüm XV Not 2."))
# 17
S.append(soru(
 "Adi metalden bir otomobil kapı kolunun 87.08 (motorlu taşıt aksamı) yerine 83.02 pozisyonunda sınıflandırılmasının dayanağı hangisidir?",
 ["GYK 2(a)", "GYK 3(b)", "GYK 3(c)", "GYK 1 (83.02 pozisyon metni ile Bölüm XV ve Bölüm XVII notları)", "GYK 4"], "D", GY,
 "GYK 1’e göre sınıflandırma pozisyon metinleri ve Bölüm notlarına göre yapılır. Bölüm XV Not 2, 83.02 eşyasını genel kullanım aksamı sayar; Bölüm XVII Not 2(b) de genel kullanım aksamını taşıt aksamı kapsamından çıkarır. 83.02 Açıklama Notu otomobil kapı kollarını özel kullanım için yapılmış olsalar da burada sayar; 3(b) veya 3(c)’ye gerek kalmaz.",
 "GYK 1; Bölüm XV Not 2; Bölüm XVII Not 2(b); 83.02 Açıklama Notu."))
# 18
S.append(soru(
 "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda yer alır?",
 ["Kapı tokmağı – elektriksiz kapı zili", "Kemer tokası – çıtçıt", "Trafik levhası – metal stensil levha", "Kaplanmış kaynak elektrodu – kaplamasız çelik kaynak teli", "Dişli şişe kapağı – kurşun mühür"], "E", FA,
 "Dişli kapaklar ve kurşun veya kalay sactan mühürler 83.09’da birlikte sayılmıştır. Kapı tokmağı 83.02, zil 83.06; toka 83.08, çıtçıt 96.06; trafik levhası 83.10, stensil levha metaline göre; kaplanmış elektrot 83.11, kaplamasız tel Fasıl 72’dedir.",
 "83.02, 83.06, 83.08, 83.09, 83.10 ve 83.11 Açıklama Notları."))
# 19
S.append(soru(
 "Aşağıdaki eşya ile pozisyonları eşleştirildiğinde hangisi <b>doğru</b> olur?<br/>I. Şampanya şişesi mantarını tutan özel tel tertibat<br/>II. Kör uçlu çivili (çekme) perçin<br/>III. Halkalı klasör mekanizması<br/>IV. Masa üstü kalem kutusu<br/>a) 83.04 b) 83.05 c) 83.08 d) 83.09",
 ["I-d, II-c, III-b, IV-a", "I-c, II-d, III-b, IV-a", "I-d, II-b, III-c, IV-a", "I-d, II-c, III-a, IV-b", "I-b, II-c, III-d, IV-a"], "A", EB,
 "Şampanya mantarını emniyete alan tel tertibat 83.09’da; kör uçlu çivili perçinler boru şeklinde perçinlerle birlikte 83.08’de; klasör ve cilt mekanizmaları 83.05’te; kalem kutusu gibi masa üstü büro eşyası 83.04’tedir.",
 "83.04, 83.05, 83.08 ve 83.09 Açıklama Notları."))
# 20
S.append(soru(
 "Tarife Cetveline göre, elektrikli ark kaynağı için üzeri eritici bir madde ile kaplanmış çelik elektrot hangi pozisyonda sınıflandırılır?",
 ["72.17", "85.15", "85.45", "72.29", "83.11"], "E", E4,
 "83.11, lehim ve kaynak işlerinde kullanılmak üzere temizleyici veya eritici maddelerle kaplanmış ya da içi doldurulmuş adi metal tel, çubuk ve elektrotları kapsar. Kaplamasız çelik teller 72.17 veya 72.29’da kalır; 85.15 kaynak makinaları, 85.45 karbon elektrotlar içindir.",
 "83.11 pozisyon metni ve Açıklama Notu."))
# 21
S.append(soru(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 83. faslında <b>sınıflandırılmaz</b>?",
 ["Çelik pünez", "Ataş (kağıt klipsi)", "Şerit halinde zımba teli", "Halkalı klasör mekanizması", "Kağıt köşebendi"], "A", OT,
 "83.05 Açıklama Notu pünezleri açıkça hariç tutar; çelik pünezler 73.17’de, bakır başlı olanlar 74.15’tedir. Ataş, şerit halindeki zımba telleri, klasör mekanizmaları ve kağıt köşebentleri 83.05’te sayılmıştır.",
 "83.05 Açıklama Notu; 73.17 pozisyon metni."))
# 22
S.append(soru(
 "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir bölümde yer alır?",
 ["Kapı kilidi", "Kapı menteşesi", "Elektrikli kapı zili", "Kapı numarası levhası", "Elektriksiz kapı zili"], "C", FA,
 "83.06 Açıklama Notu elektrikli zilleri hariç tutarak 85.31’e gönderir; Fasıl 85 Bölüm XVI’dadır. Kapı kilidi (83.01), menteşe (83.02), numara levhası (83.10) ve elektriksiz kapı zili (83.06) Bölüm XV’tedir.",
 "83.06 Açıklama Notu; Bölüm XV Not 1."))
# 23
S.append(soru(
 "Aşağıdaki eşyadan hangileri Fasıl 83 <b>dışında</b> sınıflandırılır?<br/>I. Çelikten atık kağıt sepeti<br/>II. Masa üstü evrak ağırlığı<br/>III. Delme ve kesmeye karşı ciddi direnç göstermeyen, yangına dayanıklı konteyner<br/>IV. Otomobil plakası",
 ["I ve II", "II ve IV", "Yalnız III", "I ve III", "I, III ve IV"], "D", CC,
 "83.04 Açıklama Notu atık kağıt sepetlerini hariç tutar; çelikten olanlar 73.26’dadır (I). 83.03 Açıklama Notu delme ve kesmeye ciddi direnç göstermeyen yangına dayanıklı konteynerleri 94.03’e gönderir (III). Evrak ağırlığı 83.04’te, otomobil plakası 83.10’da kalır.",
 "83.03, 83.04 ve 83.10 Açıklama Notları."))
# 24
S.append(soru(
 "Pirinçten dökülmüş, kabartma motifli bir at figürü ithal edilmektedir. Figürün kaidesinde küçük bir küllük çukuru bulunmakla birlikte, ürün esas olarak salon vitrini veya şömine üzerinde süs olarak kullanılmak üzere tasarlanmıştır. Ürün hangi pozisyonda sınıflandırılır?",
 ["74.19", "83.06", "74.18", "71.17", "83.04"], "B", SN,
 "83.06 Açıklama Notu, esas olarak dekorasyon amacıyla yapılmış adi metal figürleri ve üzerinde tali derecede sigara tablası koymaya yarayan bir kap bulunan süs eşyasını bu pozisyonda sayar; süs vasfı galip olduğundan küllük çukuru sonucu değiştirmez. Fasıl 83 eşyası bakır faslına (74.18, 74.19) verilmez; 71.17 taklit mücevherci eşyası, 83.04 masa üstü büro eşyası içindir.",
 "83.06 Açıklama Notu (B); Bölüm XV Not 2."))
# 25
S.append(soru(
 "Tarife Cetveline göre, bankalarda kullanılan, zırhlı alaşımlı çelik cidarlı, çift kapılı ve şifreli kilitli kasa hangi pozisyonda sınıflandırılır?",
 ["83.03", "94.03", "73.26", "83.01", "73.08"], "A", E4,
 "83.03, mücevherat ve kıymetli evrakı yangına ve hırsıza karşı korumaya mahsus, zırhlı duvarlı ve emniyetli kilitli kasaları kapsar; Açıklama Notu bunların bankalarda, bürolarda kullanıldığını belirtir. Kilit taşıması onu 83.01’e götürmez; 94.03 delmeye dayanıksız konteynerler, 73.08 konut tipi çelik güvenlik kapıları içindir.",
 "83.03 Açıklama Notu."))

kaydet(obj, 83)
