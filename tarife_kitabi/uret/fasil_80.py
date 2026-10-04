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
 "fasil": 80,
 "baslik": "Kalay ve kalaydan eşya",
 "bolum": "XV",
 "oz": {
  "vurgu": "Fasıl 80’in yalnız dört pozisyonu vardır: işlenmemiş kalay 80.01, hurda 80.02, çubuk-profil-tel 80.03 ve geri kalan her şey 80.07. Belirleyici iki soru şudur: Kalay ağırlıkça üstün metal mi (Bölüm XV Not 5 ve 7)? Eşya Bölüm XV Not 1 veya Fasıl 83 tarafından alınmış mı?",
  "maddeler": [
   "80.04, 80.05 ve 80.06 boştur: kalay levha, sac, şerit ve yapraklar, tozlar ve pullar, borular ve bağlantı parçaları 80.07’de toplanır.",
   "Kalay kırıntıları ve granülleri işlenmemiş kalaydır (80.01); toz ve pullar 80.01’den açıkça hariçtir (80.07).",
   "Kalayla kaplanmış çelik (teneke) kalay eşya değildir: yassı ürün 72.10 veya 72.12’de, kalaylı demir-çelik hurdası 72.04’tedir.",
   "Kalay-kurşun alaşımlarında ağırlıkça hangi metal üstünse o fasıl uygulanır: kalay üstünse Fasıl 80, kurşun üstünse Fasıl 78.",
   "Kasiterit 26.09’da, kalay cürufu ve külü 26.20’de; eritici kaplı lehim çubuğu 83.11’de; kalay yaprağından şişe kapsülü ve kalay sactan mühür 83.09’dadır."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Kalay cevheri (kasiterit) veya zenginleştirilmiş cevher mi?", "<b>26.09</b>"],
   ["2", "Kalay imalinden kalan cüruf, kül veya artık mı?", "<b>26.20</b>"],
   ["3", "Kalay ağırlıkça üstün metal mi?*", "Hayır ise ilgili metalin faslı (kalaylı çelik Fasıl 72–73; kurşun üstün lehim Fasıl 78)"],
   ["4", "Bölüm XV Not 1 veya Fasıl 82–83 tarafından ismen alınmış mı?", "Kapsül, mühür <b>83.09</b> · eritici kaplı lehim çubuğu <b>83.11</b> · süs eşyası <b>83.06</b> · oyuncak Fasıl 95 · boya Fasıl 32"],
   ["5", "Kesinlikle kullanılmaz halde kalay döküntü veya hurda mı?", "<b>80.02</b>"],
   ["6", "Blok, külçe, kütük, pik, döküm çubuğu, kırıntı veya granül mü (hurdadan eritilmiş külçe dahil)?", "<b>80.01</b>"],
   ["7", "Haddelenmiş veya kalıptan çekilmiş çubuk, profil ya da tel mi (kaplamasız kaynak çubuğu dahil)?", "<b>80.03</b>"],
   ["8", "Hiçbiri değilse (levha, yaprak, toz, pul, boru, tüp, kap, sofra eşyası, hacim ölçeği, anot…)", "<b>80.07</b>"]
  ],
  "dipnot": "* Alaşımda kalay ağırlıkça diğer metallerin her birinden fazla olmalıdır (Bölüm XV Not 5); birden fazla adi metalden eşyada da ağırlıkça üstün metal esas alınır (Bölüm XV Not 7)."
 },
 "pozisyon_haritasi": [
  ["80.01", "İşlenmemiş kalay", "Blok, külçe, kütük, pik, döküm çubuğu, kırıntı, granül; toz ve pul hariç", "Kalay külçesi, kalay granülü"],
  ["80.02", "Kalay döküntü ve hurdaları", "Kullanılmaz metal; cüruf ve kül hariç", "Kalay kırpıntısı, eskimiş kalay kap"],
  ["80.03", "Kalay çubuk, profil ve teller", "Not 9(a)–(c); kaplamasız kaynak çubuğu dahil; döküm çubuğu hariç", "Kalıptan çekilmiş kalay kaynak çubuğu, kalay tel"],
  ["80.07", "Kalaydan diğer eşya", "Artık pozisyon; levha, yaprak, toz, pul, boru ve bağlantı parçaları dahil", "Diş macunu tüpü, kalay kupa, hacim ölçeği, kalay yaprak"]
 ],
 "notlar": [
  ["Bölüm XV Not 1", "Bölüm dışı (özet): metalik toz veya pul esaslı müstahzar boyalar (32.07–32.10, 32.12, 32.13, 32.15); Fasıl 71 eşyası; Bölüm XVI (makine, mekanik cihaz, elektrikli alet); Bölüm XVII; Bölüm XVIII; Bölüm XIX; Fasıl 94, 95 (oyuncaklar, oyun ve spor malzemesi), 96 ve 97 eşyası."],
  ["Bölüm XV Not 2", "Genel kullanıma mahsus aksam: 73.07, 73.12, 73.15, 73.17, 73.18 eşyası ve diğer adi metallerden benzerleri; yaylar (saat zemberekleri hariç); 83.01, 83.02, 83.08, 83.10 eşyası ile 83.06’daki çerçeve ve aynalar. 82 veya 83. Fasıl eşyası 72–76 ve 78–81. Fasıllara verilmez."],
  ["Bölüm XV Not 3", "“Adi metaller”: demir ve çelik, bakır, nikel, alüminyum, kurşun, çinko, <b>kalay</b> ile tungsten, molibden, tantal, magnezyum, kobalt, bizmut, kadmiyum, titan, zirkonyum, antimon, manganez, berilyum, krom, germanyum, vanadyum, galyum, hafniyum, indiyum, niyobyum, renyum ve talyum. Listede olmayan metaller (ör. cıva) Bölüm XV’te değildir."],
  ["Bölüm XV Not 5", "Adi metal alaşımı, ağırlıkça diğer metallerin her birinden üstün olan metalin alaşımıdır. Bölüm XV metalleri ile Bölüm dışı elemanlardan oluşan alaşım, adi metallerin toplam ağırlığı diğer elemanların toplamına eşit veya fazlaysa Bölüm XV alaşımıdır."],
  ["Bölüm XV Not 7", "İki veya daha fazla adi metal içeren eşya, ağırlıkça diğer metallerin her birinden üstün olan metalden mamul sayılır. Bu hesapta demir ve çelik tek metal sayılır; bir alaşım, Not 5’e göre alaşımı sayıldığı metalden ibaret kabul edilir (ör. pirinç parça tamamen bakır sayılır)."],
  ["Bölüm XV Not 8", "Döküntü ve hurda: tamamen metal döküntüler ile kırılma, kesilme, eskime vb. nedenlerle kesinlikle kullanılmaz haldeki metal eşya. Toz: göz açıklığı <b>1 mm</b> olan elekten ağırlıkça <b>%90 veya daha fazlası</b> geçen ürün."],
  ["Bölüm XV Not 9", "Çubuk rulo halinde olmayan, tel rulo halinde olan içi dolu üründür; levha, sac, şerit ve yapraklarda kalınlık genişliğin onda birini geçmez; boru tek kapalı boşluklu, kesiti ve et kalınlığı her yerde aynı içi boş üründür. Kalayda bu tanımlardan yalnız çubuk-profil-tel kendi pozisyonuna (80.03) sahiptir."],
  ["Genel Açıklamalar", "Kalay ticari olarak kasiteritten (26.09) elde edilir; hurda tenekelerin klorla veya elektrolitik işlenmesiyle ya da kalay hurdasının yeniden eritilmesiyle de kazanılır. Başlıca alaşımlar: kalay-kurşun (kalay esaslı yumuşak lehimler, kap kacak, hacim ölçekleri), kalay-antimon (Britannia metali; sofra eşyası, yataklar), kalay-kurşun-antimon (antifriksiyon metaller), kalay-kadmiyum. Fasıl 72 Genel Açıklamalarında sayılan yüzey işlemleri sınıflandırmayı etkilemez."],
  ["80.01 Açıklama Notu", "Blok, külçe, kütük, pik, çubuk veya benzeri biçimlerde işlenmemiş kalay ile kalay kırıntıları, granülleri ve benzeri ürünler. Kalay tozları ve pulları hariç (80.07)."],
  ["80.02 Açıklama Notu", "72.04’ün hurda koşulları uygulanır. Kalay imalinden kalan cüruf, kül ve artıklar 26.20’de; hurdadan eritilmiş külçeler ve benzeri işlenmemiş döküm biçimleri 80.01’dedir."],
  ["80.03 Açıklama Notu", "Kalay esaslı kaynak çubukları (kesilmiş olsun olmasın) eritici madde ile kaplanmamışsa burada, kaplanmışsa 83.11’de; haddeleme, çekme veya yeniden döküm için döküm çubukları 80.01’dedir."],
  ["80.07 Açıklama Notu", "Fıçı, depo, tekne ve kaplar (mekanik veya termik tertibatsız); diş macunu, boya vb. için yumuşak tüpler; ev ve sofra eşyası (güğüm, kupa, kadeh, sifon başı, bira kadehi kapağı); hacim ölçekleri; elektro kaplama anotları; kalay tozları ve pulları; kalay levha, sac, şerit ve yapraklar (baskılı veya kağıt, karton, plastik mesnetli olsun olmasın); ince ve kalın borular ile bağlantı parçaları."]
 ],
 "sinir_komsulari": [
  ["Kasiterit (kalay cevheri), zenginleştirilmiş kalay cevheri", "26.09", "Cevherler Bölüm XV dışında"],
  ["Kalay cürufu, külü ve artıkları", "26.20", "80.02 hariç tutması"],
  ["Kalayla kaplanmış demir veya alaşımsız çelik yassı ürün, genişliği 600 mm veya fazla", "72.10", "Esas metal çelik; kalaylama yüzey işlemi"],
  ["Aynı ürün, genişliği 600 mm’den az", "72.12", "Esas metal çelik"],
  ["Kalaylı demir veya çelik döküntü ve hurdası", "72.04", "Demir-çelik hurdası pozisyonu"],
  ["Kurşunun ağırlıkça üstün olduğu kurşun-kalay lehim", "Fasıl 78", "Bölüm XV Not 5"],
  ["Bakırın ağırlıkça üstün olduğu bakır-kalay alaşımı", "Fasıl 74", "Bölüm XV Not 5"],
  ["Eritici madde ile kaplanmış kalay esaslı lehim çubuğu veya teli", "83.11", "80.03 hariç tutması"],
  ["Kalay yaprağından şarap ve şampanya şişesi kapsülü; kalay sactan mühür", "83.09", "83.09 Açıklama Notu; Bölüm XV Not 2"],
  ["Süs niteliği ağır basan kalay heykelcik ve biblo", "83.06", "Fasıl 83 eşyası"],
  ["Kalaydan oyuncak", "Fasıl 95", "Bölüm XV Not 1"],
  ["Kalay tozu içeren hazır boya", "Fasıl 32", "Bölüm XV Not 1"],
  ["Cıva", "28.05", "Bölüm XV Not 3 listesinde yok"]
 ],
 "tuzaklar": [
  "<b>Teneke kalay eşya değildir.</b> Kalayla kaplanmış çelik sac Fasıl 72’de (72.10 / 72.12), teneke hurdası 72.04’tedir; kalaylama bir yüzey işlemidir.",
  "<b>Levha ve yaprak 80.07’dedir.</b> 80.04 ve 80.05 boştur; kalay levha, sac, şerit ve yapraklar (baskılı veya mesnetli olsalar da) “diğer eşya” pozisyonundadır.",
  "<b>Toz da 80.07’dedir.</b> Kurşunda 78.04, çinkoda 79.03 olan toz, kalayda 80.07’ye düşer; 80.01 Açıklama Notu tozu ve pulları açıkça hariç tutar.",
  "<b>Granül işlenmemiş kalaydır.</b> Kalay kırıntıları ve granülleri 80.01’de; toz ve pullar 80.07’de.",
  "<b>Lehimde üstün metal belirleyicidir.</b> Kalay ağırlıkça üstünse Fasıl 80, kurşun üstünse Fasıl 78; eritici madde ile kaplanmışsa her ikisi de 83.11.",
  "<b>Kapsül kalaydan olsa da 83.09’dadır.</b> Şarap ve şampanya şişelerinin kurşun veya kalay yaprağından kapsülleri ve kalay sactan mühürler Fasıl 83’tedir.",
  "<b>Döküm çubuğu ile çubuk farklıdır.</b> Yeniden döküm için döküm çubuğu 80.01; haddelenmiş veya kalıptan çekilmiş çubuk 80.03.",
  "<b>Karma eşyada alaşım tek metal sayılır.</b> Kalay alaşımı gövde ve pirinç kapaktan oluşan kupada pirinç bakır, gövde kalay sayılır; ağırlıkça üstün olan belirleyicidir."
 ],
 "hafiza": {
  "kanca": "İŞ – HU – ÇU – Dİ (01 – 02 – 03 – 07): “dört kapı, son kapı geniş”",
  "aciklama": "<b>İŞ</b>lenmemiş 80.01 · <b>HU</b>rda 80.02 · <b>ÇU</b>buk-profil-tel 80.03 · <b>Dİ</b>ğer her şey 80.07. Aradaki üç boş numara (80.04, 80.05, 80.06) levha-yaprak, toz ve boruların eski yeridir; hepsi son ve en geniş kapıdan, 80.07’den girer."
 },
 "sinav_odagi": [
  "Fasıl 80’in pozisyonları çıkmış sorularda doğrudan sorulmamış; fasıl daha çok Bölüm XV’in yapısını sorgulayan sorularda yer almıştır.",
  "“Hangi adi metal için özel bir fasıl açılmıştır?” kalıbı: kalayın kendi faslı (80) olduğu, magnezyum, titanyum ve krom gibi metallerin Fasıl 81’de toplandığı.",
  "Bölüm XV Not 3’teki adi metal listesinin bilinmesi; adi metallerin kıymetli metal tanımlarıyla karıştırılması üzerine kurulan seçenekler.",
  "Bölüm XV Not 9 tanımları (çubuk-tel ayrımı) gibi bölüm geneli tanımların kalay ürünlerine de uygulanması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdaki adi metallerden hangisi için Armonize Sistem Nomanklatüründe özel olarak açılmış bir fasıl bulunmaktadır?",
   "secenekler": ["Magnezyum", "Titanyum", "Krom", "Kalay"],
   "cevap": "D",
   "aciklama": "Kalay ve kalaydan eşya için ayrı bir fasıl (Fasıl 80) açılmıştır. Magnezyum (81.04), titanyum (81.08) ve krom (81.12) ise “diğer adi metaller” olarak Fasıl 81’de birer pozisyonda yer alır."
  }
 ],
 "ozet": [
  "Dört pozisyon: 80.01 işlenmemiş · 80.02 hurda · 80.03 çubuk-profil-tel · 80.07 diğer her şey.",
  "Levha, yaprak, toz, pul, boru ve bağlantı parçaları 80.07’de; kırıntı ve granül 80.01’de.",
  "Kalay kaplı çelik Fasıl 72; teneke hurdası 72.04; kasiterit 26.09; cüruf ve kül 26.20.",
  "Alaşımda ağırlıkça üstün metal: kalay-kurşun lehimde kalay fazlaysa 80, kurşun fazlaysa 78.",
  "Kaplamasız kaynak çubuğu 80.03; eritici kaplı lehim çubuğu 83.11; döküm çubuğu 80.01.",
  "Kapsül ve mühür 83.09; süs eşyası 83.06; oyuncak Fasıl 95."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1
S.append(soru(
 "Tarife Cetveline göre, diş macunlarının ambalajlanmasında kullanılan kalaydan yumuşak tüp hangi pozisyonda sınıflandırılır?",
 ["80.03", "80.07", "83.09", "39.23", "76.12"], "B", E4,
 "80.07 Açıklama Notu, diş macunu, boya veya diğer ürünlerin ambalajlanmasında kullanılan kalaydan yumuşak tüpleri açıkça sayar. 80.03 çubuk, profil ve teller içindir; 83.09 tıpa, kapak ve kapsülleri kapsar. 39.23 plastik, 76.12 alüminyum ambalaj kaplarına aittir.",
 "80.07 Açıklama Notu."))
# 2
S.append(soru(
 "Aşağıdakilerden hangisi 80.07 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Kalay tozları ve pulları", "Kalayın ağırlıkça üstün olduğu kalay-kurşun alaşımından bira kadehi kapağı", "Kalaydan hacim ölçeği", "Kalay levha ve şeritler", "Kalay granülleri"], "E", OT,
 "80.01 Açıklama Notu kalay kırıntılarını, granüllerini ve benzeri ürünleri işlenmemiş kalayla birlikte sayar; granüller 80.01’dedir. Toz ve pullar ise 80.01’den açıkça hariç tutulup 80.07’ye gönderilmiştir. Bira kadehi kapağı, hacim ölçeği, levha ve şeritler 80.07 Açıklama Notunda sayılır.",
 "80.01 ve 80.07 Açıklama Notları."))
# 3
S.append(soru(
 "Bölüm XV Not 3’e göre aşağıdakilerden hangisi “adi metal” <b>değildir</b>?",
 ["Kalay", "Bizmut", "Kadmiyum", "Cıva", "Antimon"], "D", FN,
 "Bölüm XV Not 3, tarifenin neresinde geçerse geçsin adi metallerin listesini verir; kalay, bizmut, kadmiyum ve antimon bu listededir. Cıva listede yoktur; Fasıl 28’de 28.05 pozisyon metninde ayrıca sayılmıştır. Tuzak, sıvı metal olan cıvayı da metal sayıp Bölüm XV’te aramaktır.",
 "Bölüm XV Not 3; 28.05 pozisyon metni."))
# 4
S.append(soru(
 "Aşağıdaki kalay ürünlerinden hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
 ["Kalay tel", "Kalay yaprak", "Kalay profil", "Haddelenmiş kalay çubuk", "Kaplamasız kalay esaslı kaynak çubuğu"], "B", FA,
 "Kalay yaprakları için ayrı pozisyon yoktur (80.04 ve 80.05 boş); bunlar 80.07 Açıklama Notunda sayılır. Tel, profil, haddelenmiş çubuk ve eritici madde ile kaplanmamış kalay esaslı kaynak çubukları 80.03’tedir. Tuzak, kurşun ve çinkodaki ayrı yassı ürün pozisyonunu kalayda da aramaktır.",
 "80.03 ve 80.07 Açıklama Notları; Bölüm XV Not 9."))
# 5
S.append(soru(
 "Tarife Cetveline göre kalay granülleri hangi pozisyonda sınıflandırılır?",
 ["80.07", "80.03", "80.01", "80.02", "26.09"], "C", E4,
 "80.01 Açıklama Notu, işlenmemiş kalayın yanında kalay kırıntılarını, granüllerini ve benzeri ürünleri de bu pozisyona alır. Tozlar ve pullar ise 80.07’dedir; tuzak, granülü tozla karıştırmaktır. 80.02 hurdaları, 26.09 kalay cevherini kapsar.",
 "80.01 Açıklama Notu."))
# 6
S.append(soru(
 "Kalaydan yapılmış, gövdesi tamamlanmış ancak henüz kulpu takılmamış bir kupa 80.07 pozisyonunda sınıflandırılırken hangi Genel Yorum Kuralları uygulanır?",
 ["GYK 1 ve 5(a)", "GYK 1 ve 2(a)", "GYK 1 ve 2(b)", "GYK 1 ve 3(b)", "GYK 1 ve 4"], "B", GY,
 "GYK 2(a)’ya göre bir eşyaya yapılan atıf, gümrüğe sunulduğunda bitmiş eşyanın ayırt edici niteliğini taşıyan eksik veya bitmemiş halini de kapsar; kulpsuz kupa, kupanın esas niteliğine sahiptir. 2(b) madde karışımları, 3(b) bileşik eşya ve takımlar, 5(a) mahfazalar içindir; 4 ancak diğer kurallar yetersiz kaldığında uygulanır.",
 "GYK 1 ve 2(a); 80.07 Açıklama Notu."))
# 7
S.append(soru(
 "Fasıl 80 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Kalay levha, sac ve şeritler 80.07 pozisyonunda yer alır.<br/>II. Kalay tozları 80.01 pozisyonunda yer alır.<br/>III. Kalay döküntü ve hurdalarının yeniden eritilmesiyle elde edilen külçeler 80.01 pozisyonunda yer alır.<br/>IV. Eritici madde ile kaplanmış kalay esaslı kaynak çubukları 80.03 pozisyonunda yer alır.",
 ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "III ve IV"], "B", CC,
 "Levha, sac ve şeritler 80.07’de sayılmıştır (I doğru). Tozlar 80.01’den hariç tutulup 80.07’ye gönderilmiştir (II yanlış). Hurdadan eritilmiş külçeler 80.02’den hariç tutulup 80.01’e alınmıştır (III doğru). Eritici madde ile kaplanmış kaynak çubukları 80.03’ten hariçtir ve 83.11’dedir (IV yanlış).",
 "80.01, 80.02, 80.03 ve 80.07 Açıklama Notları."))
# 8
S.append(soru(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 80. faslında <b>sınıflandırılmaz</b>?",
 ["Kalaydan elektro kaplama anodu", "Kalaydan sifon başı", "Kalayla kaplanmış, genişliği 800 mm olan alaşımsız çelik sac", "Kalaydan ince boru", "Kalay döküntü ve hurdası"], "C", OT,
 "Kalayla kaplanmış demir veya alaşımsız çelik yassı ürünlerde esas metal çeliktir; genişliği 600 mm veya daha fazla olan kaplanmış ürünler 72.10’da adıyla yer alır. Kalaylama, Fasıl 72 Genel Açıklamalarında sayılan bir yüzey işlemidir. Anot, sifon başı ve boru 80.07’de, hurda 80.02’dedir.",
 "72.10 pozisyon metni; Fasıl 72 Genel Açıklamalar; 80.07 Açıklama Notu."))
# 9
S.append(soru(
 "Ağırlıkça %48 kalay, %45 kurşun ve %7 antimon içeren, külçe halindeki antifriksiyon alaşımı Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
 ["78.01", "80.01", "81.10", "80.07", "38.24"], "B", FN,
 "Bölüm XV Not 5’e göre alaşım, ağırlıkça diğer metallerin her birinden üstün olan metalin alaşımıdır. Kalay (%48) kurşundan (%45) ve antimondan ayrı ayrı fazladır; %50’yi geçmesi gerekmez. Külçe halindeki işlenmemiş kalay alaşımı 80.01’dedir. Kurşun üstün olsaydı 78.01 söz konusu olurdu; 38.24 adi metal oranı yetersiz alaşımlar içindir.",
 "Bölüm XV Not 5 ve Not 6; 80.01 Açıklama Notu; Fasıl 80 Genel Açıklamalar."))
# 10
S.append(soru(
 "Tarife Cetveline göre kalay granülleri …… pozisyonunda, kalay tozları …… pozisyonunda, eritici madde ile kaplanmamış kalay esaslı kaynak çubukları ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
 ["80.07 – 80.07 – 83.11", "80.01 – 80.05 – 80.03", "80.01 – 80.07 – 80.03", "80.03 – 80.07 – 80.01", "80.01 – 80.01 – 83.11"], "C", EB,
 "Kalay granülleri işlenmemiş kalayla birlikte 80.01’de; tozlar 80.01’den hariç tutularak 80.07’de; kaplamasız kalay esaslı kaynak çubukları 80.03’te yer alır. 80.05 boş bir pozisyondur; 83.11 yalnız eritici madde ile kaplanmış veya içi doldurulmuş çubuklar içindir.",
 "80.01, 80.03 ve 80.07 Açıklama Notları."))
# 11
S.append(soru(
 "Tarife Cetveline göre, üzerine baskı yapılmış ve kağıt mesnetle desteklenmiş kalay yaprak hangi pozisyonda sınıflandırılır?",
 ["80.03", "48.11", "76.07", "80.07", "80.01"], "D", E4,
 "80.07 Açıklama Notu, Bölüm XV Not 9(d)’de tanımlanan kalay levha, sac ve şeritler ile kalay yapraklarını, baskılı olsun olmasın, kağıt, karton, plastik veya benzeri maddelerle desteklenmiş olsun olmasın bu pozisyona alır. Kağıt mesnet ürünü 48.11’e götürmez; 76.07 alüminyum yapraklar içindir.",
 "80.07 Açıklama Notu; Bölüm XV Not 9(d)."))
# 12
S.append(soru(
 "Bir restoran ekipmanı tedarikçisi, ağırlıkça %92 kalay, %6 antimon ve %2 bakır içeren alaşımdan (Britannia metali) dökülerek ve preslenerek yapılmış, süssüz, günlük kullanıma mahsus çay demlikleri ithal etmektedir. Demliklerde herhangi bir ısıtma tertibatı yoktur. Ürün hangi pozisyonda sınıflandırılır?",
 ["73.23", "74.18", "80.07", "83.06", "85.16"], "C", SN,
 "Kalay ağırlıkça üstün olduğundan alaşım kalay alaşımıdır (Bölüm XV Not 5); Fasıl 80 Genel Açıklamaları Britannia metalini kalay-antimon alaşımları arasında sayar. Kalaydan ev ve sofra eşyası 80.07’dedir. Süssüz ve iş görme amaçlı olduğundan 83.06’daki süs eşyası sayılmaz; 73.23 ve 74.18 demir-çelik ve bakır eşya içindir.",
 "Bölüm XV Not 5; Fasıl 80 Genel Açıklamalar; 80.07 Açıklama Notu; 83.06 Açıklama Notu (B)."))
# 13
S.append(soru(
 "Aşağıdaki alaşım ürünlerinden hangisi diğerlerinden <b>farklı</b> bir fasılda yer alır?",
 ["Ağırlıkça %40 kalay ve %60 kurşun içeren lehim külçesi", "Ağırlıkça %60 kalay ve %40 kurşun içeren lehim külçesi", "Kalayın ağırlıkça üstün olduğu kalay-antimon alaşımından sofra takımı", "Kalayın ağırlıkça üstün olduğu kalay-kadmiyum antifriksiyon alaşımı külçe", "Kalay döküntü ve hurdası"], "A", FA,
 "Bölüm XV Not 5’e göre alaşım, ağırlıkça üstün metalin alaşımıdır: %60 kurşun içeren lehim kurşun alaşımıdır ve Fasıl 78’dedir (78.01). Kalayın üstün olduğu lehim külçesi ve antifriksiyon alaşımı 80.01’de, sofra takımı 80.07’de, hurda 80.02’de, yani Fasıl 80’dedir.",
 "Bölüm XV Not 5; Fasıl 78 ve Fasıl 80 Genel Açıklamalar."))
# 14
S.append(soru(
 "Aşağıdakilerden hangisi 80.02 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Kalay döküntü ve hurdalarının yeniden eritilmesiyle elde edilen külçe", "Kalay eşya imalatında ortaya çıkan kalay kırpıntıları", "Eskime nedeniyle kesinlikle kullanılmaz hale gelmiş kalay kaplar", "Kırılarak kullanılmaz hale gelmiş kalay borular", "Kalay çubukların tornalanmasından kalan talaşlar"], "A", OT,
 "80.02 Açıklama Notu, külçeleri ve kalay döküntü ve hurdalarının yeniden eritilmesiyle elde edilen benzeri işlenmemiş döküm formlarını hurda pozisyonundan hariç tutar; bunlar 80.01’dedir. Kırpıntılar, talaşlar ve kesinlikle kullanılmaz haldeki kalay eşya Bölüm XV Not 8(a) anlamında döküntü ve hurdadır.",
 "80.02 Açıklama Notu; Bölüm XV Not 8(a)."))
# 15
S.append(soru(
 "Ağırlıkça %70’i kalayın üstün olduğu kalay-kurşun alaşımından gövde, %30’u pirinçten kapaktan oluşan, süssüz bir bira kupası Bölüm XV Not 7 dikkate alındığında hangi pozisyonda sınıflandırılır?",
 ["74.18", "83.06", "80.07", "70.13", "80.03"], "C", FN,
 "Bölüm XV Not 7’ye göre karma eşya ağırlıkça üstün metalden sayılır ve bir alaşım, alaşımı sayıldığı metalden ibaret kabul edilir: gövde kalay (%70), pirinç kapak bakır (%30) sayılır. Kalay üstün olduğundan kupa 80.07’dedir; Açıklama Notu kupaları ve bira kadehi kapaklarını sayar. 74.18 bakır ev eşyası, 83.06 süs eşyası içindir.",
 "Bölüm XV Not 7; Bölüm XV Genel Açıklamalar (B); 80.07 Açıklama Notu."))
# 16
S.append(soru(
 "Tarife Cetveline göre, kalay imalinden meydana gelen cüruf ve kül hangi pozisyonda sınıflandırılır?",
 ["26.20", "80.02", "26.09", "80.01", "80.07"], "A", E4,
 "80.02 Açıklama Notu, kalay imalinden meydana gelen cüruf, kül ve artıkları hurda pozisyonundan çıkararak 26.20’ye gönderir. 26.09 kalay cevherini (kasiterit), 80.02 kalay döküntü ve hurdalarını, 80.01 işlenmemiş kalayı kapsar.",
 "80.02 Açıklama Notu."))
# 17
S.append(soru(
 "Kalay sactan mamul, ambalaj sandıklarını mühürlemeye mahsus garanti mühürlerinin Fasıl 80 yerine 83.09 pozisyonunda sınıflandırılmasının dayanağı hangisidir?",
 ["GYK 2(a)", "GYK 2(b)", "GYK 3(b)", "GYK 3(c)", "GYK 1 (83.09 pozisyon metni ve Bölüm XV Not 2 ile)"], "E", GY,
 "GYK 1’e göre sınıflandırma pozisyon metinleri ile Bölüm ve Fasıl notlarına göre yapılır. 83.09 mühür kurşunlarını ve benzeri ambalaj teferruatını adıyla kapsar; Açıklama Notu bunların genellikle kurşun veya kalay sactan yapıldığını belirtir. Bölüm XV Not 2 son paragrafı Fasıl 83 eşyasının Fasıl 80’e verilmesini engellediğinden 2 veya 3 numaralı kurallara gerek kalmaz.",
 "GYK 1; 83.09 Açıklama Notu; Bölüm XV Not 2."))
# 18
S.append(soru(
 "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda yer alır?",
 ["Kalay granülü – kalay tozu", "Kalay tel – kalay yaprak", "Kalay hurdası – kalay cürufu", "Kalay döküm çubuğu – haddelenmiş kalay çubuk", "Kalay tozu – kalaydan ince boru"], "E", FA,
 "Kalay tozları ve kalaydan borular, ayrı pozisyonları bulunmadığından birlikte 80.07’dedir. Granül 80.01, toz 80.07; tel 80.03, yaprak 80.07; hurda 80.02, cüruf 26.20; döküm çubuğu 80.01, haddelenmiş çubuk 80.03’tedir.",
 "80.01, 80.02, 80.03 ve 80.07 Açıklama Notları."))
# 19
S.append(soru(
 "Aşağıdaki eşya ile pozisyonları eşleştirildiğinde hangisi <b>doğru</b> olur?<br/>I. Kasiterit<br/>II. Kalaylı demir veya çelik döküntü ve hurdası<br/>III. Kalay döküntü ve hurdası<br/>IV. Kalay imalinden kalan cüruf<br/>a) 26.09 b) 26.20 c) 72.04 d) 80.02",
 ["I-a, II-d, III-c, IV-b", "I-b, II-c, III-d, IV-a", "I-a, II-b, III-d, IV-c", "I-a, II-c, III-d, IV-b", "I-c, II-a, III-d, IV-b"], "D", EB,
 "Kalay cevheri kasiterit 26.09’da; kalaylı demir veya çelik hurdası esas metal demir-çelik olduğundan 72.04’te; kalay hurdası 80.02’de; kalay imalinden kalan cüruf ise 80.02 hariç tutması uyarınca 26.20’dedir.",
 "Fasıl 80 Genel Açıklamalar; 80.02 Açıklama Notu; 72.04 pozisyon metni."))
# 20
S.append(soru(
 "Tarife Cetveline göre, ağırlıkça %99 kalay içeren, kalıptan çekilerek elde edilmiş, belirli boylarda kesilmiş ve üzeri eritici bir madde ile kaplanmamış kaynak çubuğu hangi pozisyonda sınıflandırılır?",
 ["80.01", "80.07", "83.11", "78.06", "80.03"], "E", E4,
 "80.03 Açıklama Notu, genellikle kalıptan çekme ile elde edilen kalay esaslı kaynak çubuklarını, uzunluğuna kesilmiş olsun olmasın, üzerleri eritici madde ile kaplanmamış olmak şartıyla bu pozisyona alır. Kaplanmış olsaydı 83.11, yeniden döküme mahsus döküm çubuğu olsaydı 80.01 söz konusu olurdu.",
 "80.03 Açıklama Notu; 83.11 Açıklama Notu."))
# 21
S.append(soru(
 "Aşağıdaki kalay içeren ürünlerden hangisi 80. Fasılda <b>yer almaz</b>?",
 ["Kalay tel", "Kalayın ağırlıkça üstün olduğu kalay-antimon alaşımından sofra eşyası", "Kalay külçe", "Kalay yaprağından mamul şampanya şişesi kapsülü", "Kalaydan, mekanik veya termik tertibatı olmayan kimyasal madde deposu"], "D", OT,
 "83.09 Açıklama Notu, bazı şampanya ve şarap şişelerinde kullanılan kurşun veya kalay yapraklarından mamul kapsülleri açıkça sayar; Bölüm XV Not 2 son paragrafı uyarınca bu eşya Fasıl 80’e verilmez. Tel 80.03’te, sofra eşyası ve depo 80.07’de, külçe 80.01’dedir.",
 "83.09 Açıklama Notu; Bölüm XV Not 2; 80.01, 80.03 ve 80.07 Açıklama Notları."))
# 22
S.append(soru(
 "Bölüm XV Not 8(a)’ya göre “döküntü ve hurda” tabiri aşağıdakilerden hangisini ifade eder?",
 ["Tamamen metal döküntü ve hurdalar ile kırılma, kesilme, eskime veya diğer nedenlerle kesinlikle kullanılmaz halde olan metal eşya", "Metal imalinden kalan cüruf, kül ve artıklar", "Döküntü ve hurdaların yeniden eritilmesiyle elde edilen külçeler", "Onarıldıktan sonra yeniden kullanılabilecek ikinci el metal eşya", "Göz açıklığı 1 mm olan elekten ağırlıkça %90’ı geçen metal parçacıklar"], "A", FN,
 "Bölüm XV Not 8(a), döküntü ve hurdayı tamamen metal döküntü ve hurdalar ile kesinlikle kullanılmaz haldeki metal eşya olarak tanımlar. Cüruf ve kül 26.20’de, hurdadan eritilmiş külçe 80.01’dedir; onarılabilir eşya hurda değildir. Son seçenek Not 8(b)’deki toz tanımına yakındır.",
 "Bölüm XV Not 8; 80.02 Açıklama Notu."))
# 23
S.append(soru(
 "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir bölümde yer alır?",
 ["Kalaydan heykelcik", "Kalay yaprak", "Eritici madde ile kaplanmış kalay esaslı lehim teli", "Kalaydan oyuncak asker", "Kalaydan bira kupası"], "D", FA,
 "Oyuncaklar Bölüm XV Not 1 uyarınca Bölüm dışıdır ve Fasıl 95’te, yani Bölüm XX’dedir. Heykelcik (83.06) ve eritici kaplı lehim teli (83.11) Fasıl 80 dışına çıksa da Bölüm XV içinde kalır; yaprak ve kupa 80.07’dedir. Tuzak, “fasıl dışı” ile “bölüm dışı”yı karıştırmaktır.",
 "Bölüm XV Not 1 ve Not 2; 83.06 ve 83.11 Açıklama Notları."))
# 24
S.append(soru(
 "Aşağıdaki eşyadan hangileri Fasıl 80 <b>dışında</b> sınıflandırılır?<br/>I. Kalay sactan garanti mühürü<br/>II. Kalaydan güğüm<br/>III. Kurşunun ağırlıkça üstün olduğu kurşun-kalay lehim külçesi<br/>IV. Kalayla kaplanmış, genişliği 600 mm’den fazla alaşımsız çelik sac",
 ["I, III ve IV", "I ve III", "II ve IV", "Yalnız I", "I, II ve III"], "A", CC,
 "Kalay sactan mühür 83.09’da (I), kurşunun üstün olduğu lehim külçesi Bölüm XV Not 5 uyarınca 78.01’de (III), kalayla kaplanmış çelik sac 72.10’da (IV) yer alır. Kalaydan güğüm ev eşyası olarak 80.07’dedir (II).",
 "83.09 ve 80.07 Açıklama Notları; Bölüm XV Not 5; 72.10 pozisyon metni."))
# 25
S.append(soru(
 "Bir elektronik montaj firması; kalayın ağırlıkça üstün olduğu kalay-kurşun alaşımından kalıptan çekilerek elde edilmiş, belirli boylarda kesilmiş ve üzeri lehimleme için reçine esaslı eritici madde ile kaplanmış çubuklar ithal etmektedir. Ürün hangi pozisyonda sınıflandırılır?",
 ["80.03", "80.07", "80.01", "78.06", "83.11"], "E", SN,
 "83.11, lehim ve kaynak işlerinde kullanılmak üzere temizleyici veya eritici maddelerle üzerleri kaplanmış ya da içleri doldurulmuş adi metal çubuk ve telleri kapsar; Açıklama Notu reçineyi bu maddeler arasında sayar. 80.03 Açıklama Notu kaplanmış kaynak çubuklarını açıkça 83.11’e gönderir. Kaplama olmasaydı ürün kalay alaşımı olarak 80.03’te kalırdı.",
 "83.11 Açıklama Notu; 80.03 Açıklama Notu; Bölüm XV Not 2."))

kaydet(obj, 80)
