"""Fasıl 75 – Nikel ve nikelden eşya modülünü üretir."""
from yardim_73_76 import (ESYA, OLUMSUZ, FARKLI, TANIM, GYK, ESLES, COKLU, SENARYO,
                          soru, kaydet)

obj = {
 "tur": "fasil",
 "fasil": 75,
 "baslik": "Nikel ve nikelden eşya",
 "bolum": "XV",
 "oz": {
  "vurgu": "Fasıl 75, nikelin ağırlıkça üstün olduğu metal ve eşyayı yalnızca sekiz pozisyonda toplar. Fasıl notu yoktur; sınıflandırmayı Bölüm XV notları (alaşım, karma eşya, çubuk-tel-levha-boru tanımları) ile Açıklama Notlarındaki üç ayrım belirler: ara ürün mü işlenmemiş nikel mi, katot mu kaplama anodu mu, kendi pozisyonu mu yoksa 75.08 mi?",
  "maddeler": [
   "Metalurji sırası: mat ve oksit sinterleri 75.01, işlenmemiş nikel 75.02, hurda 75.03, toz 75.04; nikelde ön alaşım pozisyonu yoktur.",
   "Yarı mamuller birleşiktir: çubuk-profil-tel 75.05; saç, levha, şerit ve yaprak kalınlık ayrımı olmadan 75.06; boru ve boru bağlantı parçası birlikte 75.07.",
   "Elektrokaplama anotları ve geri kalan bütün nikel eşya 75.08’dedir; 82 ve 83. fasıl eşyası ile Bölüm XV Not 1’deki eşya hariç.",
   "Alaşımlarda ağırlıkça üstün metal faslı belirler (bakır üstünse Fasıl 74); nikel kaplama ise yüzey işlemidir ve sınıflandırmayı değiştirmez."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Kıymetli metal (altın, gümüş, platin) oranı ağırlıkça %2 veya daha fazla mı?", "Fasıl <b>71</b>"],
   ["2", "Adi metaller arasında nikel ağırlıkça üstün mü? (kaplama hesaba katılmaz)", "Değilse üstün metalin faslı (bakır <b>74</b>, çelik <b>72</b> / <b>73</b>)"],
   ["3", "Cevher veya zenginleştirilmiş cevher mi?", "<b>26.04</b>"],
   ["4", "82 / 83. fasılda adıyla sayılan eşya mı? (kilit, menteşe, çerçeve, süs, esnek boru)", "Fasıl <b>82</b> / <b>83</b>"],
   ["5", "Mat, saf olmayan nikel oksit (sinter), saf olmayan ferro-nikel veya speiss mi?", "<b>75.01</b> (rafine ferro-nikel <b>72.02</b>)"],
   ["6", "İşlenmemiş nikel mi? (külçe, pellet, kancasız katot, rafine için döküm anot)", "<b>75.02</b>"],
   ["7", "Döküntü veya hurda mı?", "<b>75.03</b> (cüruf ve kül <b>26.20</b>)"],
   ["8", "Toz veya ince pul mu?", "<b>75.04</b>"],
   ["9", "Çubuk, profil (içi boş dahil) veya tel mi?", "<b>75.05</b>"],
   ["10", "Saç, levha, şerit veya yaprak mı?", "<b>75.06</b>"],
   ["11", "Boru veya boru bağlantı parçası mı?", "<b>75.07</b>"],
   ["12", "Hiçbiri değilse (kaplama anodu, tel mensucat, çivi, depo, para taslağı…)", "<b>75.08</b>"]
  ],
  "dipnot": ""
 },
 "pozisyon_haritasi": [
  ["75.01", "Nikel matları, oksit sinterleri, diğer ara ürünler", "Metalurji ara ürünü; saf olmayan ferro-nikel dahil", "Nikel matı, yeşil nikel oksit, speiss"],
  ["75.02", "İşlenmemiş nikel", "Külçe, pellet, katot; rafine için döküm anot", "Nikel katodu, pellet, briket"],
  ["75.03", "Nikel döküntü ve hurdaları", "Bölüm XV Not 8(a); cüruf-kül 26.20", "Nikel talaşı, kullanılmaz nikel eşya"],
  ["75.04", "Nikel tozu ve ince pulları", "Kullanım önemsiz; oksit sinteri hariç", "Batarya levhası için nikel tozu"],
  ["75.05", "Çubuklar, profiller, teller", "Bölüm XV Not 9(a)–(c); içi boş profil dahil", "Süper alaşım çubuk, nikel-krom tel"],
  ["75.06", "Saç, levha, şerit, yaprak", "Kalınlık ayrımı yok; genleştirilmiş metal hariç", "Nikel levha, nikel şerit"],
  ["75.07", "Borular ve boru bağlantı parçaları", "Boru ve rakor aynı pozisyonda", "Nikel alaşımı kimya borusu, dirsek"],
  ["75.08", "Nikelden diğer eşya", "Kaplama anotları + artık pozisyon", "Kancalı anot, para taslağı, tel mensucat"]
 ],
 "notlar": [
  ["Fasıl 75 (not durumu)", "Fasıl 75’te fasıl notu yoktur; sınıflandırma Bölüm XV notları, pozisyon metinleri ve Açıklama Notlarıyla yapılır. Fasıldaki tanımlar yalnız alt pozisyon düzeyindedir (alaşımsız nikel: ağırlıkça en az %99 nikel ve kobalt, kobalt en çok %1,5; nikel alaşımı: nikelin ağırlıkça üstün olduğu ve bu sınırları aşan metalik madde)."],
  ["Bölüm XV Not 3", "Nikel “adi metal”dir. Liste: demir ve çelik, bakır, nikel, alüminyum, kurşun, çinko, kalay, tungsten, molibden, tantal, magnezyum, kobalt, bizmut, kadmiyum, titan, zirkonyum, antimon, manganez, berilyum, krom, germanyum, vanadyum, galyum, hafniyum, indiyum, niyobyum, renyum vb. Altın, gümüş, platin adi metal değildir (Fasıl 71)."],
  ["Bölüm XV Genel Açıklamalar", "Bölüm, bakır, nikel veya kobalt matlarını kapsar; metal cevherleri (26.01–26.17) bölüm dışıdır. Alaşım ağırlığına göre <b>%2’den az</b> kıymetli metal içeren alaşımlar adi metal alaşımıdır (Fasıl 71 Not 5); %2 veya fazlası Fasıl 71’e gider."],
  ["Bölüm XV Not 5", "Adi metal alaşımı ağırlıkça üstün metalin alaşımıdır. Bölüm metalleri ile bölüm dışı elementlerden oluşan alaşım, adi metallerin toplam ağırlığı diğer elementlerin toplam ağırlığına eşit veya fazlaysa bu bölümdedir; aksi halde genellikle 38.24’e girer."],
  ["Bölüm XV Not 7", "Birden çok adi metalden eşya, pozisyon metninde aksine hüküm yoksa ağırlıkça üstün metalden sayılır; alaşım, sınıflandırıldığı metal gibi hesaba katılır. Sinterlenmemiş metal tozu karışımları da bu nota göre sınıflandırılır."],
  ["Bölüm XV Not 8 ve 9", "Not 8: hurda (kesinlikle kullanılmaz metal eşya dahil) ve toz (1 mm elekten ağırlıkça %90 veya fazlası geçen) tanımları. Not 9: çubuk (rulo değil), profil, tel (rulo halinde), levha-sac-şerit-yaprak ve boru tanımları; 74–76 ve 78–81. fasıllarda uygulanır."],
  ["Fasıl 72 Not 1(c)", "Ferro-alyaj tanımı: ağırlıkça %4 veya daha fazla demir ve belirtilen oranlarda diğer elementleri içeren, katkı maddesi olarak kullanılan, genellikle dövülemeyen alaşımlar. Rafine ferro-nikel bu nedenle 72.02’dedir."],
  ["Genel Açıklamalar", "Başlıca nikel alaşımları: demir-nikel, nikel-krom veya nikel-krom-demir (uçak türbinlerinde kullanılan “süper alaşımlar” dahil) ve nikel-bakır alaşımları. Kaplama gibi yüzey işlemleri sınıflandırmayı etkilemez."],
  ["75.01 Açıklama Notu", "Nikel matları; saf olmayan nikel oksitler (nikel oksit sinterleri, toz veya 50 mm’ye kadar kütleler); yüksek kükürt (%0,5 veya fazla) ve fosfor içeren, ön arıtma olmadan çelikte kullanılamayan saf olmayan ferro-nikel; nikel speissleri."],
  ["75.02 Açıklama Notu", "İşlenmemiş nikel: külçe, pik, pellet, tabla, küp, briket, katot ve diğer elektro-tortu şekilleri; elektrolitik arıtma için dökülen rafine edilmemiş anotlar. Küçük parçalara veya şeritlere kesilmiş katotlar da buradadır; kanca takılmamış ve kanca için hazırlanmamış olmalarıyla kaplama anotlarından ayrılır. Toz ve pullar 75.04’tedir."],
  ["75.07 Açıklama Notu", "73.04–73.07 notları gerekli değişikliklerle uygulanır. İçi boş profiller 75.05’te; boruları tutturan nikel cıvata ve somunlar 75.08’de; musluk-valflı teferruat 84.81’de; makine aksamı olmuş borular XVI. Bölümde."],
  ["75.08 Açıklama Notu", "(A) Elektrokaplama anotları: yıldız, halka, özel profil veya plaka, şerit, disk, top biçiminde; tanklara asılmak için kancayla donatılmış veya delme, vidalama, set ve yiv açma ile kanca için hazırlanmış. (B) Diğer: pencere çerçeveleri ve inşaat aksamı, her kapasitede depo ve kaplar, genleştirilmiş metal ve tel mensucat, çivi, cıvata, somun, saat yayı dışındaki yaylar, ev ve sıhhi tesisat eşyası, yükseltilmiş kenarlı nikel para taslakları."]
 ],
 "sinir_komsulari": [
  ["Nikel cevheri ve konsantresi", "26.04", "Cevherler Bölüm XV dışındadır"],
  ["Nikel cürufu, külü ve artıkları", "26.20", "75.03 hariç tutması"],
  ["Rafine ferro-nikel", "72.02", "Fasıl 72 Not 1(c): ferro-alyaj"],
  ["Nikel kaplanmış çelik vida, tel, levha", "Fasıl 72 / 73", "Kaplama yüzey işlemidir; çelik üstün"],
  ["Bakırı ağırlıkça üstün kupro-nikel ve nikel gümüşü", "Fasıl 74", "Bölüm XV Not 5"],
  ["Ağırlıkça %2 veya daha fazla kıymetli metal içeren nikel alaşımı", "Fasıl 71", "Fasıl 71 Not 5"],
  ["Metal paralar", "71.18", "Bölüm XV dışı; para taslağı ise 75.08"],
  ["Metalize iplik", "56.05", "75.05 hariç tutması"],
  ["İzole edilmiş nikel bara ve tel (emayeli dahil)", "85.44", "75.05 hariç tutması"],
  ["Musluk veya valfla donatılmış nikel teferruat", "84.81", "75.07 hariç tutması"],
  ["Makine aksamı haline gelmiş nikel boru", "XVI. Bölüm", "75.07 hariç tutması"],
  ["Nikelden eğilip bükülebilen boru", "83.07", "Adi metallerden esnek borular"],
  ["Nikel fotoğraf çerçevesi, süs eşyası", "83.06", "Bölüm XV Not 2 son paragraf"],
  ["Nikel kilit ve menteşe", "83.01 / 83.02", "Fasıl 83 eşyası 75. fasla verilmez"],
  ["Saat yayı", "91.14", "75.08’deki yay kapsamı dışı"]
 ],
 "tuzaklar": [
  "<b>Toz görünümlü oksit sinteri toz değildir.</b> Nikel oksit sinterleri 75.01’dedir; 75.04 Açıklama Notu bunları açıkça hariç tutar.",
  "<b>Ferro-nikelin iki adresi vardır.</b> Yüksek kükürt ve fosfor içeren saf olmayan ferro-nikel 75.01; doğrudan alaşımlamada kullanılan rafine ferro-nikel ferro-alyaj olarak 72.02.",
  "<b>Katot mu, anot mu?</b> Kancasız ve kanca için hazırlanmamış katot parçaları 75.02; kancalı ya da kanca için delinmiş, vidalanmış, yivlenmiş kaplama anotları 75.08; elektrolitik arıtma için dökülen anotlar yine 75.02.",
  "<b>Nikelde boru ile rakor aynı pozisyondadır.</b> 75.07 boruları ve bağlantı parçalarını birlikte kapsar; içi boş profil 75.05’e, boruyu tutturan cıvata-somun 75.08’e gider.",
  "<b>Nikelde levha-yaprak sınırı yoktur.</b> 75.06 saç, levha, şerit ve yaprağı birlikte kapsar; bakırdaki 0,15 mm ve alüminyumdaki 0,2 mm sınırları burada aranmaz.",
  "<b>Nikel kaplama eşyayı nikel yapmaz.</b> Kaplama yüzey işlemidir; ağırlıkça üstün metal çelikse eşya Fasıl 72 / 73’tedir.",
  "<b>Bakır çoksa Fasıl 74’tür.</b> Nikel-bakır alaşımlarında ağırlıkça üstün metal belirleyicidir; kupro-nikel ve nikel gümüşü bakır alaşımıdır.",
  "<b>Para taslağı para değildir.</b> Yükseltilmiş kenarlı nikel disk 75.08’de; metal paralar ise 71.18’de.",
  "<b>Nikelde ayrı mensucat, çivi, depo veya yay pozisyonu yoktur.</b> Hepsi 75.08’dedir; ancak çerçeve, menteşe, kilit gibi 83. fasıl eşyası kendi faslına gider."
 ],
 "hafiza": {
  "kanca": "MAT – HAM – HURDA – TOZ – ÇUBUK – LEVHA – BORU – DİĞER",
  "aciklama": "Nikel sekiz kelimelik bir fasıldır: <b>01</b> mat, <b>02</b> ham (işlenmemiş), <b>03</b> hurda, <b>04</b> toz, <b>05</b> çubuk-profil-tel, <b>06</b> levha-yaprak, <b>07</b> boru-rakor, <b>08</b> diğer. Bakırdaki on dokuz pozisyon burada sıkıştırılmıştır: ön alaşım yoktur, tel ayrı değildir, yaprak ayrı değildir, rakor ayrı değildir; kaplama anotları dahil geri kalan her şey 08’dedir."
 },
 "sinav_odagi": [
  "Bu fasıl çıkmış sorularda doğrudan sorulmamıştır; nikel, Bölüm XV’in yapısını ve genel notlarını ölçen sorularda yer almıştır.",
  "Fasıl yapısı: hangi adi metal için ayrı fasıl açıldığı sorulmuştur; nikel (75), bakır (74), alüminyum (76), kurşun (78), çinko (79) ve kalay (80) ayrı fasıllardayken magnezyum, titanyum ve krom Fasıl 81’de toplanmıştır.",
  "Bölüm XV Not 9 tanımları: “çubuk” ile “tel” arasındaki farkın rulo halinde olup olmamak olduğu 74–76 ve 78–81. fasıllar için ortak olarak sorulmuştur; nikelde ikisi de 75.05’tedir.",
  "“Aynı bölümde yer alan eşya” sorularında adi metalden eşyanın (ör. adi metal kapı kilidi) Bölüm XV’e, makine ve cihazların XVI. Bölüme ayrılması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdaki adi metallerden hangisi için Armonize Sistem Nomanklatüründe özel olarak açılmış bir fasıl bulunmaktadır?",
   "secenekler": ["Magnezyum", "Titanyum", "Krom", "Kalay"],
   "cevap": "D",
   "aciklama": "Bölüm XV’te bakır (74), nikel (75), alüminyum (76), kurşun (78), çinko (79) ve kalay (80) için ayrı fasıl açılmıştır. Magnezyum (81.04), titanyum (81.08) ve krom (81.12) “diğer adi metaller” faslı olan 81. fasılda toplanmıştır."
  }
 ],
 "ozet": [
  "Nikel ağırlıkça üstünse Fasıl 75; kıymetli metal %2 veya fazlaysa Fasıl 71, bakır üstünse Fasıl 74.",
  "Mat ve oksit sinteri 75.01 · işlenmemiş nikel 75.02 · hurda 75.03 · toz 75.04 (ön alaşım pozisyonu yok).",
  "Çubuk-profil-tel 75.05 · saç-levha-şerit-yaprak 75.06 (kalınlık sınırı yok) · boru ve rakor 75.07.",
  "Kancalı veya kanca için hazırlanmış kaplama anodu 75.08; kancasız katot parçası 75.02.",
  "Ferro-nikel: saf olmayan 75.01, rafine 72.02.",
  "Geri kalan her şey 75.08: depo, tel mensucat, çivi-cıvata, yay, ev-sıhhi eşya, para taslağı."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1
S.append(soru(ESYA,
 "Tarife Cetveline göre, nikel içeren sülfürlerin işlenmesiyle elde edilen, toz veya 50 mm’ye kadar kütleler halindeki, esas olarak alaşımlı çelik imalatında kullanılan saf olmayan nikel oksit sinterleri hangi pozisyonda sınıflandırılır?",
 ["26.04", "72.02", "75.02", "75.01", "75.04"], "D", "75.01",
 "Nikel oksit sinterleri gibi saf olmayan nikel oksitler, nikel matları, saf olmayan ferro-nikel ve nikel speissleri nikel metalurjisinin ara ürünleri olarak 75.01’dedir. 75.04 Açıklama Notu nikel oksit sinterlerini açıkça hariç tutar; toz halinde olmaları 75.04’e götürmez. Cevher 26.04’te, rafine ferro-nikel 72.02’de, işlenmemiş nikel 75.02’dedir.",
 "75.01 Açıklama Notu; 75.04 Açıklama Notu, hariç tutma."))

# 2
S.append(soru(TANIM,
 "Bölüm XV Not 3’e göre aşağıdakilerden hangisi “adi metal” <b>değildir</b>?",
 ["Kobalt", "Platin", "Germanyum", "Hafniyum", "Bizmut"], "B", "Platin",
 "Bölüm XV Not 3 adi metalleri sayar: demir ve çelik, bakır, nikel, alüminyum, kurşun, çinko, kalay, tungsten, molibden, tantal, magnezyum, kobalt, bizmut, kadmiyum, titan, zirkonyum, antimon, manganez, berilyum, krom, germanyum, vanadyum, galyum, hafniyum, indiyum, niyobyum, renyum vb. Platin bu listede yoktur; kıymetli metal olarak Fasıl 71’in konusudur. Kobalt, germanyum, hafniyum ve bizmut ayrı faslı olmasa da adi metaldir (Fasıl 81).",
 "Bölüm XV Not 3; Fasıl 71."))

# 3
S.append(soru(OLUMSUZ,
 "Aşağıdakilerden hangisi Tarife Cetvelinin 75. faslında <b>sınıflandırılmaz</b>?",
 ["Nikel pelleti", "Nikel tozu", "Nikel döküntü ve hurdası", "Nikel matı", "Zenginleştirilmiş nikel cevheri"], "E",
 "Zenginleştirilmiş nikel cevheri",
 "Bölüm XV Genel Açıklamalarına göre metal cevherleri (26.01 ila 26.17) bölüm dışıdır; nikel cevheri ve zenginleştirilmiş nikel cevheri 26.04’tedir. Bölüm XV ise nikel matlarını açıkça kapsar: mat 75.01’de, pellet 75.02’de, hurda 75.03’te, toz 75.04’tedir.",
 "Bölüm XV Genel Açıklamalar; 26.04 pozisyon metni; 75.01–75.04 Açıklama Notları."))

# 4
S.append(soru(FARKLI,
 "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
 ["Çelik sanayisinde doğrudan alaşımlama ürünü olarak kullanılan rafine edilmiş ferro-nikel", "Nikel matı",
  "Nikel oksit sinteri", "Yüksek oranda kükürt ve fosfor içeren saf olmayan ferro-nikel", "Nikel speissi"], "A",
 "Çelik sanayisinde doğrudan alaşımlama ürünü olarak kullanılan rafine edilmiş ferro-nikel",
 "Saf olmayan ferro-nikel yüksek kükürt (%0,5 veya daha fazla) ve fosfor içerdiğinden ön arıtma yapılmadan çelik sanayisinde kullanılamaz ve 75.01’de kalır. Rafine edilmiş ferro-nikel ise Fasıl 72 Not 1(c) uyarınca ferro-alyaj olarak 72.02’dedir. Nikel matı, nikel oksit sinteri ve speiss 75.01’dedir.",
 "75.01 Açıklama Notu; Fasıl 72 Not 1(c)."))

# 5
S.append(soru(ESYA,
 "Tarife Cetveline göre, elektrolitik rafinasyonla elde edilmiş, küçük dikdörtgen parçalar halinde kesilmiş, askı kancası takılmamış ve kanca için delik, yiv gibi bir hazırlık görmemiş rafine nikel katotları hangi pozisyonda sınıflandırılır?",
 ["75.01", "75.04", "75.02", "75.06", "75.08"], "C", "75.02",
 "75.02 Açıklama Notu, küçük dikdörtgen parçalar veya şeritler halinde kesilmiş ya da yalnızca düzeltilmiş katotları, kullanım amacı ve ebatları ne olursa olsun işlenmemiş nikel olarak bu pozisyona alır. Bunlar 75.08’deki elektrokaplama anotlarından askı kancası takılmamış veya kanca için hazırlanmamış olmalarıyla ayrılır. Levha görünümü eşyayı haddelenmiş ürünler pozisyonuna (75.06) götürmez.",
 "75.02 Açıklama Notu; 75.08 Açıklama Notu (A)."))

# 6
S.append(soru(ESLES,
 "Aşağıdaki ürünler ile tarife pozisyonlarının doğru eşleştirildiği seçenek hangisidir? I. Nikel matı  II. İşlenmemiş nikel pelleti  III. Nikel tozu  IV. Nikel döküntü ve hurdası — a) 75.01  b) 75.02  c) 75.03  d) 75.04",
 ["I-a, II-b, III-c, IV-d", "I-b, II-a, III-d, IV-c", "I-a, II-d, III-b, IV-c", "I-a, II-b, III-d, IV-c",
  "I-c, II-b, III-d, IV-a"], "D", "I-a, II-b, III-d, IV-c",
 "Nikel matları 75.01’de; pelletler işlenmemiş nikel olarak 75.02’de (75.08 Açıklama Notu da işlenmemiş pelletleri 75.02’ye bırakır); döküntü ve hurdalar 75.03’te; tozlar kullanım yeri ne olursa olsun 75.04’tedir. Tuzak, sırayı bakırla aynı sanmaktır: nikelde ön alaşım pozisyonu olmadığından hurda 75.03, toz 75.04’tür.",
 "75.01, 75.02, 75.03 ve 75.04 Açıklama Notları."))

# 7
S.append(soru(GYK,
 "Ağırlıkça %55 nikel ve %45 bakırdan oluşan alaşımdan haddelenmiş levhalar, Bölüm XV Not 5 uyarınca nikel alaşımı sayılarak 75.06 pozisyonunda sınıflandırılır. Bu sınıflandırmada esas alınan Genel Yorum Kuralı hangisidir?",
 ["GYK 1", "GYK 2(b)", "GYK 3(a)", "GYK 3(b)", "GYK 3(c)"], "A", "GYK 1",
 "Alaşımın hangi metalin alaşımı sayılacağını Bölüm XV Not 5 belirler: ağırlıkça üstün olan nikel. Sınıflandırma pozisyon metni ve bölüm notuna göre yapıldığından GYK 1 uygulanır; not meseleyi çözdüğü için 2(b) ve 3 numaralı kurallara başvurulmaz. Bakır oranının yüksekliği eşyayı Fasıl 74’e götürmez.",
 "GYK 1; Bölüm XV Not 5; 75.06 pozisyon metni."))

# 8
S.append(soru(OLUMSUZ,
 "Aşağıdakilerden hangisi 75.08 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Askı kancalarıyla donatılmış nikel elektrokaplama anodu", "Basitçe haddelenmiş, kanca için hazırlanmamış nikel plaka",
  "Nikelden cıvata ve somun", "Nikelden genleştirilmiş metal", "Nikelden sıhhi tesisat eşyası"], "B",
 "Basitçe haddelenmiş, kanca için hazırlanmamış nikel plaka",
 "75.08 Açıklama Notu, elektrokaplama anodu niteliği taşımayan basitçe haddelenmiş plakaları 75.06’ya bırakır. Kancalı anotlar (A grubu) ile nikel cıvata ve somunlar, genleştirilmiş metal ve ev-sıhhi tesisat eşyası (B grubu) 75.08’de sayılmıştır. Tuzak, kaplama işinde kullanılacak her nikel parçasını anot saymaktır.",
 "75.08 Açıklama Notu (A) ve (B)."))

# 9
S.append(soru(TANIM,
 "Tarife Cetveline göre nikel ile gümüşten oluşan bir alaşımın kıymetli metal alaşımı değil, adi metal (nikel) alaşımı sayılabilmesi için gümüş oranı ne olmalıdır?",
 ["Ağırlıkça %10’dan az", "Ağırlıkça %5’ten az", "Ağırlıkça %50’den az", "Ağırlıkça %2 veya daha fazla",
  "Ağırlıkça %2’den az"], "E", "Ağırlıkça %2’den az",
 "Fasıl 71 Not 5 ve Bölüm XV Genel Açıklamaları, alaşım ağırlığına göre %2’den az kıymetli metal (altın, gümüş, platin) içeren alaşımları adi metal alaşımı sayar; herhangi bir kıymetli metal %2 veya daha fazlaysa alaşım Fasıl 71’dedir. Adi metal alaşımı olduğu belirlendikten sonra hangi faslın geçerli olduğuna Bölüm XV Not 5’e göre ağırlıkça üstün adi metale bakılarak karar verilir.",
 "Fasıl 71 Not 5; Bölüm XV Genel Açıklamalar (A)."))

# 10
S.append(soru(SENARYO,
 "Bir firma, uçak motoru türbin kanatlarının imalinde kullanılmak üzere “süper alaşım” olarak bilinen; ağırlıkça %55 nikel, %20 krom, %12 kobalt ve kalanı molibden, titanyum ve alüminyumdan oluşan, sıcak haddelenmiş, rulo halinde olmayan, kesiti daire şeklinde içi dolu ürünler ithal etmektedir. Bu eşya hangi pozisyonda sınıflandırılır?",
 ["72.28", "75.02", "75.05", "75.06", "81.05"], "C", "75.05",
 "Bölüm XV Not 5 gereği alaşım, ağırlıkça üstün metal olan nikelin alaşımıdır; Fasıl 75 Genel Açıklamaları uçak türbinlerinde kullanılan süper alaşımları nikel alaşımları arasında sayar. Rulo halinde olmayan, kesiti boydan boya aynı içi dolu ürün Bölüm XV Not 9(a)’daki çubuk tanımına uyduğundan 75.05’tedir. 72.28 demir esaslı alaşımlı çelik çubuklar içindir; kobalt (81.05) ağırlıkça üstün değildir; ürün henüz türbin kanadı şekli almadığından makine aksamı da değildir.",
 "Bölüm XV Not 5 ve Not 9(a); Fasıl 75 Genel Açıklamalar."))

# 11
S.append(soru(FARKLI,
 "Aşağıdaki nikel eşyadan hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
 ["Nikelden boru rakoru", "Nikelden çivi", "Boruları tutturmada kullanılan nikel cıvata ve somun",
  "Saat yayı dışındaki nikel yay", "Nikel tellerden mensucat"], "A", "Nikelden boru rakoru",
 "Nikelden boru bağlantı parçaları (rakor, dirsek, manşon) borularla birlikte 75.07’dedir. Nikel çiviler, cıvata ve somunlar (boruları tutturmakta kullanılsalar bile), yaylar ve tel mensucat ise 75.08 Açıklama Notunda sayılan “nikelden diğer eşya”dır; 75.07 Açıklama Notu boruları tutturan cıvata ve somunları açıkça 75.08’e bırakır.",
 "75.07 ve 75.08 Açıklama Notları."))

# 12
S.append(soru(ESYA,
 "Tarife Cetveline göre, kimya sanayinde aşındırıcı ortamlarda kullanılmak üzere, nikelin ağırlıkça üstün olduğu nikel-bakır alaşımından üretilmiş dikişsiz, kesiti daire şeklindeki borular hangi pozisyonda sınıflandırılır?",
 ["73.04", "74.11", "75.05", "75.07", "75.08"], "D", "75.07",
 "Nikel ağırlıkça üstün olduğundan alaşım nikel alaşımıdır (Bölüm XV Not 5). Nikelden ince ve kalın borular ile boru bağlantı parçaları 75.07’de birlikte yer alır ve 73.04–73.07 Açıklama Notları gerekli değişikliklerle uygulanır. 75.05 çubuk, profil (içi boş profil dahil) ve telleri, 74.11 bakır boruları, 73.04 demir-çelik dikişsiz boruları kapsar.",
 "Bölüm XV Not 5; 75.07 pozisyon metni ve Açıklama Notu."))

# 13
S.append(soru(COKLU,
 "Tarife Cetveline göre aşağıdaki ifadelerden hangileri doğrudur? I. Nikel oksit sinterleri toz halinde olduğunda 75.04’te sınıflandırılır.  II. Rafine edilmiş ferro-nikel 72.02’de ferro-alyaj olarak sınıflandırılır.  III. Nikel döküntü ve hurdalarının yeniden eritilmesiyle elde edilen külçeler 75.02’de sınıflandırılır.  IV. Nikel cürufu, külü ve artıkları 75.03’te sınıflandırılır.",
 ["I ve II", "II ve III", "I, II ve III", "III ve IV", "II, III ve IV"], "B", "II ve III",
 "Nikel oksit sinterleri toz halinde olsa bile 75.01’dedir; 75.04 bunları hariç tutar (I yanlış). Rafine ferro-nikel Fasıl 72 Not 1(c) uyarınca 72.02’dedir (II doğru). Hurdaların yeniden eritilmesiyle elde edilen külçeler işlenmemiş nikel olarak 75.02’dedir (III doğru). Cüruf, kül ve nikel artıkları 75.03’ten hariç tutulmuş olup 26.20’dedir (IV yanlış).",
 "75.01, 75.03 ve 75.04 Açıklama Notları; Fasıl 72 Not 1(c)."))

# 14
S.append(soru(TANIM,
 "Bölüm XV Not 5’e göre nikel ile bu bölüme girmeyen elementlerden oluşan bir alaşım hangi şartla Bölüm XV’te adi metal alaşımı olarak sınıflandırılır?",
 ["Nikelin, bölüm dışı elementlerin her birinden ağırlıkça fazla olması",
  "Bölüm dışı elementlerin toplamının ağırlıkça %2’yi geçmemesi", "Alaşımın dövülebilir ve haddelenebilir olması",
  "Bölüm dışı elementlerin toplamının ağırlıkça %10’u geçmemesi",
  "Bölüm XV’e giren adi metallerin toplam ağırlığının diğer elementlerin toplam ağırlığına eşit veya daha fazla olması"],
 "E", "Bölüm XV’e giren adi metallerin toplam ağırlığının diğer elementlerin toplam ağırlığına eşit veya daha fazla olması",
 "Bölüm XV Not 5’e göre bölüm metalleri ile bölüm dışı elementlerden oluşan alaşımlar, adi metallerin toplam ağırlığı diğer elementlerin toplam ağırlığına eşit veya fazlaysa bu bölümün adi metal alaşımı sayılır; aksi halde Genel Açıklamalara göre genellikle 38.24’e girer. Nikelin her bir elementten fazla olması yetmez; ölçüt toplamlar arasındadır. %2 eşiği kıymetli metal alaşımlarına aittir.",
 "Bölüm XV Not 5; Bölüm XV Genel Açıklamalar (A)."))

# 15
S.append(soru(OLUMSUZ,
 "Aşağıdakilerden hangisi 75.05 pozisyonunda <b>yer almaz</b>?",
 ["Alaşımsız nikelden çubuk", "Nikel alaşımından rulo halinde tel",
  "İnşaatta kullanılmak üzere hazırlanmış (delinmiş, kesilmiş) nikel profil", "Nikelden içi boş profil",
  "Nikel alaşımından profil"], "C", "İnşaatta kullanılmak üzere hazırlanmış (delinmiş, kesilmiş) nikel profil",
 "75.05, Bölüm XV Not 9(a)–(c)’de tanımlanan nikel çubuk, profil ve telleri kapsar; 75.07 Açıklama Notu içi boş profilleri de 75.05’e bırakır. İnşaatta kullanılmak üzere hazırlanmış çubuk ve profiller 75.05’ten hariç tutulmuş olup 75.08’dedir; nikelde 73.08’in ayrı bir karşılığı yoktur. İzole edilmiş baralar ve teller ise 85.44’e gider.",
 "75.05 Açıklama Notu, hariç tutmalar; 75.07 ve 75.08 Açıklama Notları."))

# 16
S.append(soru(FARKLI,
 "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde aynı pozisyonda sınıflandırılır?",
 ["Nikel tel – nikel tellerden mensucat", "Nikel boru – nikel boru dirseği",
  "Nikel levha – nikelden genleştirilmiş metal", "Nikel hurdası – hurdadan dökülmüş nikel külçe",
  "Nikel oksit sinteri – nikel tozu"], "B", "Nikel boru – nikel boru dirseği",
 "75.07 nikelden ince ve kalın borular ile boru bağlantı parçalarını tek pozisyonda toplar (bakırda 74.11 / 74.12, demir-çelikte 73.04–73.06 / 73.07 ayrıdır). Diğer çiftlerde: tel 75.05 – mensucat 75.08; levha 75.06 – genleştirilmiş metal 75.08; hurda 75.03 – yeniden eritilmiş külçe 75.02; oksit sinteri 75.01 – toz 75.04.",
 "75.07 pozisyon metni; 75.01–75.06 ve 75.08 Açıklama Notları."))

# 17
S.append(soru(ESYA,
 "Tarife Cetveline göre, yükseltilmiş kenarlı nikel disk biçimindeki, henüz basılmamış madeni para taslakları hangi pozisyonda sınıflandırılır?",
 ["71.18", "75.02", "75.06", "83.08", "75.08"], "E", "75.08",
 "75.08 Açıklama Notu (B), yükseltilmiş kenarlı nikel disk biçimindeki metal para taslaklarını nikelden diğer eşya olarak sayar. 71.18 metal paraları kapsar ve Bölüm XV Genel Açıklamaları metal paraları bölüm dışında tutar; ancak basılmamış taslak para değildir. Disk biçimi eşyayı levha (75.06) veya işlenmemiş nikel (75.02) yapmaz.",
 "75.08 Açıklama Notu (B); Bölüm XV Genel Açıklamalar, hariç tutmalar."))

# 18
S.append(soru(ESLES,
 "Tarife Cetveline göre bakırdan saç-levha ile ince yaprak arasındaki kalınlık sınırı ...(1)... mm, alüminyumda ...(2)... mm’dir; nikelden saç, levha, şerit ve yapraklar ise kalınlık ayrımı yapılmaksızın ...(3)... pozisyonunda yer alır. Boşluklara sırasıyla gelmesi gerekenler hangisidir?",
 ["0,15 – 0,2 – 75.06", "0,2 – 0,15 – 75.06", "0,15 – 0,2 – 75.05", "0,15 – 0,15 – 75.06", "0,2 – 0,2 – 75.08"], "A",
 "0,15 – 0,2 – 75.06",
 "Bakırda 74.09 / 74.10 sınırı 0,15 mm, alüminyumda 76.06 / 76.07 sınırı 0,2 mm’dir. Nikelde ise 75.06 pozisyon metni saç, levha, şerit ve yaprakları kalınlık sınırı koymadan birlikte kapsar. 75.05 çubuk-profil-tel, 75.08 diğer eşya içindir.",
 "75.06 pozisyon metni; 74.09, 74.10, 76.06 ve 76.07 pozisyon metinleri."))

# 19
S.append(soru(FARKLI,
 "Aşağıdaki nikel eşyadan hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
 ["Nikel tellerden mensucat", "Nikelden cıvata", "Nikelden sıhhi tesisat eşyası", "Nikelden fotoğraf çerçevesi",
  "Nikelden, mekanik tertibatı olmayan depo"], "D", "Nikelden fotoğraf çerçevesi",
 "75.08; 82 veya 83. fasıllarda yer alan eşya ile Bölüm XV Not 1 kapsamındakiler dışındaki bütün nikel eşyayı kapsar. Fotoğraf ve resim çerçeveleri adi metalden olmaları yeterli olduğundan 83.06’dadır ve Bölüm XV Not 2 son paragrafı gereği 75. fasla verilmez. Tel mensucat, cıvata, sıhhi eşya ve depolar 75.08’de sayılmıştır.",
 "75.08 Açıklama Notu (B); 83.06 pozisyon metni; Bölüm XV Not 2."))

# 20
S.append(soru(GYK,
 "Tüm parçaları birlikte sunulan, monte edilmemiş haldeki, mekanik veya termik tertibatı bulunmayan nikel alaşımından 500 litrelik kimyasal depolama tankı hangi pozisyonda ve hangi kurallarla sınıflandırılır?",
 ["75.06 – GYK 1 ve 2(a)", "73.09 – GYK 1 ve 2(a)", "75.08 – GYK 1 ve 2(a)", "75.08 – GYK 3(b)", "75.06 – GYK 3(c)"], "C",
 "75.08 – GYK 1 ve 2(a)",
 "GYK 2(a) gereği sökülmüş veya monte edilmemiş halde, bütün parçalarıyla sunulan eşya tamamlanmış eşya gibi sınıflandırılır. 75.08 Açıklama Notu, ısı ve mekanik ekipman takılmamış her kapasitedeki nikel depoları kapsar; nikelde 73.09 / 73.10 gibi hacme göre ayrı pozisyon yoktur. 73.09 demir veya çelik depolar içindir; parçaların levha görünümü eşyayı 75.06’ya götürmez.",
 "GYK 1 ve 2(a); 75.08 Açıklama Notu (B)."))

# 21
S.append(soru(OLUMSUZ,
 "Aşağıdakilerden hangisi 75.02 pozisyonunda <b>yer almaz</b>?",
 ["Nikel külçesi", "Nikel tozu", "Elektrolitik arıtma için dökülmüş, iki çengelli rafine edilmemiş nikel anodu",
  "Nikel briketi", "Nikel küpü (işlenmemiş ilk şekil)"], "B", "Nikel tozu",
 "75.02 işlenmemiş nikeli (külçe, pik, pellet, tabla, küp, briket, katot vb.) ve elektrolitik arıtma için dökülmüş rafine edilmemiş nikel anotlarını kapsar. Nikel tozu ve ince pulları 75.02 Açıklama Notunda hariç tutulmuş olup 75.04’tedir. Elektrolitik arıtma anotlarını 75.08’deki elektrokaplama anotlarıyla karıştırmamak gerekir.",
 "75.02 Açıklama Notu ve hariç tutma; 75.04 pozisyon metni."))

# 22
S.append(soru(COKLU,
 "Aşağıdakilerden hangileri 75.08 pozisyonunda sınıflandırılır? I. Nikelden pencere çerçevesi  II. Nikelden genleştirilmiş metal  III. Nikel oksit sinteri  IV. Saat yayı dışındaki nikel yaylar",
 ["I ve II", "II ve IV", "I, III ve IV", "II, III ve IV", "I, II ve IV"], "E", "I, II ve IV",
 "75.08 Açıklama Notu (B), pencere çerçeveleri ve hazır inşaat aksamını, genleştirilmiş metal ile tel mensucatı ve 91.14’teki saat yayları dışındaki yayları sayar. Nikel oksit sinteri ise nikel metalurjisinin ara ürünü olarak 75.01’dedir.",
 "75.08 Açıklama Notu (B); 75.01 Açıklama Notu."))

# 23
S.append(soru(ESYA,
 "Tarife Cetveline göre, nikel tellerden dokunmuş, kenarları kaynaklanmış, rulo halindeki filtre mensucatı hangi pozisyonda sınıflandırılır?",
 ["75.08", "75.05", "75.06", "73.14", "58.09"], "A", "75.08",
 "75.08 Açıklama Notu (B) nikel telden mensucat, örgü ve kafeslikleri nikelden diğer eşya olarak sayar; nikelde 73.14’ün ayrı bir karşılığı yoktur. Tel hali 75.05’te kalır ama tellerden dokunmuş ürün artık tel değildir. 73.14 demir veya çelik tel mensucatı, 58.09 ise giyim ve döşemecilikte kullanılan türden metal iplikli dokumaları kapsar.",
 "75.08 Açıklama Notu (B)."))

# 24
S.append(soru(SENARYO,
 "Bir firma, alaşımsız çelikten imal edilmiş, yüzeyi elektroliz yoluyla ince bir nikel tabakasıyla kaplanmış, başı yarık, sivri uçlu ahşap vidaları ithal etmektedir. Vidaların ağırlığının %98’i çelik, %2’si nikel kaplamadır. Bu eşya hangi pozisyonda sınıflandırılır?",
 ["73.17", "74.15", "75.08", "73.18", "83.02"], "D", "73.18",
 "Bölüm XV Not 7’ye göre eşya ağırlıkça üstün metal olan çelikten mamul sayılır; Fasıl 72 Genel Açıklamalarına göre nikel kaplama gibi yüzey işlemleri de pozisyonu değiştirmez. Başı yarık, sivri uçlu ahşap vidası 73.18’dedir; başı yarık olmasaydı vidalı çivi olarak 73.17’ye giderdi. Vidalar nikelden olsaydı 75.08 söz konusu olurdu.",
 "Bölüm XV Not 7; Fasıl 72 Genel Açıklamalar (kaplama); 73.18 Açıklama Notu."))

# 25
S.append(soru(TANIM,
 "75.08 Açıklama Notuna göre rafine nikelden bir ürünün “elektrokaplama anodu” olarak 75.08’de sınıflandırılması için aranan ayırt edici özellik hangisidir?",
 ["Ağırlıkça en az %99 nikel içermesi", "Elektroliz yoluyla elde edilmiş olması",
  "Elektrokaplama tanklarına asılmak için kancalarla donatılmış ya da delme, vidalama veya set ve yiv açma ile kanca için hazırlanmış olması",
  "Başlama levhasına takılı iki nikel çengel ile birlikte sunulması", "Genişliğinin 30,5 cm’yi aşması"], "C",
 "Elektrokaplama tanklarına asılmak için kancalarla donatılmış ya da delme, vidalama veya set ve yiv açma ile kanca için hazırlanmış olması",
 "75.08 Açıklama Notu (A), elektrokaplama anotlarını tanklara asılmak üzere kancalarla donatılmış veya kanca için hazırlanmış ürünler olarak tanımlar. Kancasız, kanca için hazırlanmamış katot parçaları ve pelletler 75.02’de, basitçe haddelenmiş plakalar 75.06’da kalır. Başlama levhasındaki iki çengel katotların (75.02) özelliğidir; elektrokaplama anotlarının genişliği ise nadiren 30,5 cm’yi aşar.",
 "75.08 Açıklama Notu (A); 75.02 Açıklama Notu."))

kaydet(obj, 75)
