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
 "fasil": 82,
 "baslik": "Adi metallerden aletler, bıçakçı eşyası ve sofra takımları; adi metallerden bunların aksam ve parçaları",
 "bolum": "XV",
 "oz": {
  "vurgu": "Fasıl 82, yapıldığı adi metale bakmaksızın el aletlerini, değişebilir aletleri, makine bıçaklarını, bıçakçı eşyasını ve sofra takımlarını toplar. İki test belirleyicidir: İş gören kısım Fasıl 82 Not 1’deki maddelerden mi (adi metal, metal karbür, sermet, mesnetli kıymetli taş veya aşındırıcı)? Alet doğrudan elde mi kullanılıyor, yoksa motorlu, mesnetli veya makine niteliğinde mi (Fasıl 84–85)?",
  "maddeler": [
   "El aletleri 82.01–82.05; bunların perakende takımları 82.06; değişebilir aletler 82.07; makine bıçakları 82.08; monte edilmemiş sermet uçlar 82.09.",
   "Elle işleyen, 10 kg veya daha hafif mekanik mutfak cihazları 82.10; bıçaklar 82.11; ustura ve traş makinaları 82.12; makaslar 82.13; diğer bıçakçı eşyası ve manikür takımları 82.14; kaşık, çatal, kepçe 82.15.",
   "İş gören kısmı kauçuk, deri, keçe, mensucat veya seramik olan aletler maddesine göre sınıflandırılır; motorlu, pnömatik veya hidrolik el aletleri 84.67, tıbbi aletler 90.18, oyuncak aletler Fasıl 95’tedir.",
   "Parçalar ait oldukları aletle birlikte sınıflandırılır; ancak vida, çivi, zincir, yay gibi genel kullanım parçaları (Bölüm XV Not 2) ve 84.66’daki alet tutucular dışarıda kalır.",
   "Elektrikli traş ve saç kesme makinalarının başları, bıçakları ve kesici levhaları 85.10’dadır."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "İş gören kısım adi metal, metal karbür, sermet ya da mesnetli kıymetli taş veya aşındırıcı değil mi?*", "Maddesine göre (kauçuk Fasıl 40, deri 42, mensucat 59, seramik 69.09); bileği taşı 68.04"],
   ["2", "Elle kullanılan motorlu, pnömatik veya hidrolik alet ya da tezgaha, zemine monte edilecek mesnetli cihaz mı?", "<b>84.67</b> / Fasıl 84 (ör. 84.59, 84.62)"],
   ["3", "Tıp, cerrahi, dişçilik, veterinerlik aleti ya da ölçme-kontrol aleti mi?", "<b>90.18</b> / Fasıl 90"],
   ["4", "Elektrikli traş veya saç kesme makinası ya da bunların başı, bıçağı mı?", "<b>85.10</b>"],
   ["5", "Makineye veya el aletine takılan değişebilir alet mi (matkap ucu, pafta lokması, freze, tornavida ucu)?", "<b>82.07</b> (testere ağzı ise 82.02)"],
   ["6", "Makine veya mekanik cihaz bıçağı ya da kesici ağzı mı?", "<b>82.08</b>"],
   ["7", "Alete monte edilmemiş sermet veya sinterlenmiş karbür uç, levha, çubuk mu?", "<b>82.09</b>"],
   ["8", "Tarım, bahçe veya orman el aleti mi (kürek, kazma, balta, halkasız budama makası, tırpan)?", "<b>82.01</b>"],
   ["9", "Testere veya testere ağzı; eğe, pens, teneke makası, zımba; sıkıştırma anahtarı mı?", "<b>82.02</b> · <b>82.03</b> · <b>82.04</b>"],
   ["10", "Başka yerde yer almayan el aleti, kaynak lambası, mengene, örs veya portatif ocak mı?", "<b>82.05</b> (82.02–82.05 aletlerinden perakende takım <b>82.06</b>)"],
   ["11", "Elle işleyen, 10 kg veya daha hafif mekanik mutfak cihazı mı?", "<b>82.10</b>"],
   ["12", "Bıçakçı veya sofra eşyası mı?", "Bıçak <b>82.11</b> · ustura <b>82.12</b> · makas <b>82.13</b> · satır, kalemtraş, manikür <b>82.14</b> · kaşık, çatal, kepçe <b>82.15</b>"]
  ],
  "dipnot": "* Kaynak lambaları, portatif demirci ocakları, çatkılı bileğiler, manikür-pedikür takımları ve 82.09 eşyası bu ölçüte tabi değildir (Fasıl 82 Not 1)."
 },
 "pozisyon_haritasi": [
  ["82.01", "Tarım, bahçe, orman el aletleri", "Halkasız, tek elle budama makası dahil", "Bel, kazma, balta, tırpan, çit makası"],
  ["82.02", "El testereleri; her tür testere ağzı", "Makine testere ağızları dahil; motorlu testere hariç", "Demir testeresi, dairevi ve zincir testere ağzı"],
  ["82.03", "Eğe, törpü, pens, kerpeten, cımbız, teneke makası, kesici, zımba", "Elle kullanılan; makine tipi makas hariç", "Kerpeten, kulak markalama pensesi, delik zımbası"],
  ["82.04", "Elle sıkıştırma anahtarları; soketler", "Dinamometrik dahil; kılavuz anahtarı hariç", "Ayarlı anahtar, lokma takımı"],
  ["82.05", "Başka yerde yer almayan el aletleri; kaynak lambası, mengene, örs", "Torba pozisyon; mesnetsiz el matkabı dahil", "Çekiç, tornavida, rende, camcı elması"],
  ["82.06", "82.02–82.05 aletlerinden takımlar", "İki veya daha fazla alet; perakende satışa hazır", "Oto tamir alet çantası"],
  ["82.07", "Değişebilir aletler", "Makineye veya el aletine takılır", "Matkap ucu, pafta lokması, sondaj ucu, hadde"],
  ["82.08", "Makine ve mekanik cihaz bıçakları", "Monte edilmemiş; el aleti bıçakları hariç", "Kıyma makinası bıçağı, çim biçme bıçağı"],
  ["82.09", "Monte edilmemiş sermet levha, çubuk, uç", "Monte edilince 82.07; saf karbür 28.49", "Karbür torna ucu"],
  ["82.10", "Elle işleyen mekanik mutfak cihazları", "10 kg veya daha hafif; mekanizma şart", "Kahve değirmeni, el kıyma makinası"],
  ["82.11", "Kesici ağızlı bıçaklar", "Sabit, katlanır; ağız ve metal saplar dahil", "Mutfak bıçağı, çakı, budama çakısı"],
  ["82.12", "Usturalar, traş makinaları ve bıçakları", "Elektriksiz; elektrikliler 85.10", "Ustura, jilet, traş bıçağı"],
  ["82.13", "Makaslar ve ağızları", "Parmak geçecek halkalı", "Terzi, kuaför, manikür, puro makası"],
  ["82.14", "Diğer bıçakçı eşyası; manikür-pedikür", "Kağıt bıçağı, kalemtraş, satır, elle saç kesme", "Kalemtraş, et satırı, tırnak törpüsü"],
  ["82.15", "Kaşık, çatal, kepçe, spatula, balık ve yağ bıçağı, şeker maşası", "Bıçak + en az eşit sayıda 82.15 eşyası takımı dahil", "Çatal-kaşık takımı, kepçe, pasta maşası"]
 ],
 "notlar": [
  ["Bölüm XV Not 2", "Genel kullanıma mahsus aksam: 73.07, 73.12, 73.15, 73.17, 73.18 eşyası ve diğer adi metallerden benzerleri; yaylar (saat zemberekleri hariç); 83.01, 83.02, 83.08, 83.10 eşyası ile 83.06’daki çerçeve ve aynalar. Bu aksam Fasıl 82 eşyasının parçası sayılmaz. 82 veya 83. Fasıl eşyası 72–76 ve 78–81. Fasıllara verilmez."],
  ["Fasıl 82 Not 1", "82.09 eşyası, kaynak lambaları, portatif demirci ocakları, çatkılı bileğiler ve manikür-pedikür takımları hariç, fasıl yalnız bıçağı veya iş gören kısmı şunlardan olan eşyayı kapsar: (a) adi metal; (b) metal karbür veya sermet; (c) adi metal, metal karbür veya sermet mesnet üzerine tespit edilmiş kıymetli veya yarı kıymetli taş; (d) adi metal mesnet üzerine tespit edilmiş aşındırıcı (dişler ve kesici kısımlar aşındırıcı ilavesine rağmen kimlik ve işlevini korumalıdır)."],
  ["Fasıl 82 Not 2", "Fasıl eşyasının adi metal aksamı, ismen belirtilen aksam ile el aletlerine mahsus alet tutucular (84.66) hariç, esas eşyanın pozisyonunda yer alır. Bölüm XV Not 2 anlamında genel kullanım aksamı her durumda fasıl dışıdır. Elektrikli traş ve saç kesme makinalarının başları, tarakları, bıçakları ve kesici parçaları 85.10’dadır."],
  ["Fasıl 82 Not 3", "82.11’deki bir veya daha fazla bıçak ile 82.15’teki <b>en az eşit sayıda</b> eşyadan oluşan takımlar 82.15’te sınıflandırılır."],
  ["Genel Açıklamalar (el aleti – makine)", "Fasıl, doğrudan elde kullanılan aletleri (dişli, krank, vida mekanizmalı olsalar da) kapsar. Tezgaha, duvara monte edilmek üzere yapılan veya mesnet, çerçeve, kaide üzerine monte edilmiş cihazlar genellikle Fasıl 84’tedir: mesnetsiz el matkabı 82.05, mesnetli matkap 84.59; kıskaç tipi metal makası 82.03, kaideye monte giyotin makas 84.62. İstisnalar: mengene, çatkılı bileği, portatif ocak 82.05’te; püskürtme cihazları 84.24’te, pnömatik aletler 84.67’de."],
  ["Genel Açıklamalar (madde ve süs)", "İş gören kısmı adi metal, karbür veya sermetten olmayan aletler genellikle iş gören kısmın maddesine göre sınıflandırılır; ama sapı ağaç olsa da iş gören kısmı metal olan rende Fasıl 82’dedir. 82.08–82.15 eşyası kıymetli metalden basit süs taşıyabilir; kıymetli metalden sap veya ağız içeren ya da inci, kıymetli taş taşıyanlar Fasıl 71’dedir."],
  ["Genel Açıklamalar (hariç)", "Tıp, dişçilik, cerrahi ve veterinerlik aletleri 90.18’de; oyuncak niteliğindeki aletler Fasıl 95’te; bileği taşları ve aşındırıcı diskler 68.04’te; makine aksamı fırçalar 96.03’tedir."],
  ["82.01 Açıklama Notu", "Tek elle kullanılan budama makasları ve kümes hayvanı makasları parmak geçecek halkası olmadığından 82.13’teki makaslardan ayrılır. Hariç: hayvan kulağı markalama pensleri (82.03), budama çakıları (82.11), çim biçme makinaları (Fasıl 84), dağcı kazmaları (95.06)."],
  ["82.02 Açıklama Notu", "Her madde için el testereleri ve testere ağızları (şerit, dairevi, zincir, düz, dişsiz taş testeresi), dişleri açılmış taslaklar dahil. Hariç: aşındırıcı kaplı dişsiz diskler (68.04), taş kesme kablosu (73.12), zıvana zinciri (82.07), motorlu el testereleri (84.67), müzik testereleri (92.08)."],
  ["82.05 Açıklama Notu", "Başka yerde yer almayan el aletleri: matkap, pafta, kılavuz anahtarı; çekiç; rende, keski; tornavida; 73.23’e girmeyen ev aletleri (basit konserve açacağı, gazlı ütü); camcı elması (yalnız elmas 71.02); kaynak lambaları (gazlı kaynak makinası 84.68); mengene, örs, portatif ocak, çatkılı bileği. Elektrikli ütü 85.16’dadır."],
  ["82.06 Açıklama Notu", "82.02–82.05 aletlerinden iki veya daha fazlasından oluşan, perakende satış için hazırlanmış takımlar (oto tamir takımı, anahtar-tornavida setleri). Esas karakter korunmak şartıyla diğer pozisyonlardan daha az önemli aletler içerebilir."],
  ["82.07 – 82.09 Açıklama Notları", "82.07: makineye veya el aletine takılan değişebilir aletler; kaya delme ve sondaj aletleri, çekme haddeleri, tornavida uçları (radyoaktif olsalar da). Hariç: testere ağzı 82.02, rende bıçağı 82.05, makine bıçakları 82.08, alet tutucular 84.66. 82.08: makine bıçakları (kıyma makinası, çim biçme makinası, giyotin makas ağızları). 82.09: monte edilmemiş sermet uçlar; monte edilince 82.07."],
  ["82.10 Açıklama Notu", "Yiyecek-içecek hazırlama veya servisinde kullanılan, <b>10 kg veya daha hafif</b>, elle çalışan elektriksiz cihazlar; manivelalı kol, dişli, Arşimet vidası, pompa gibi bir mekanizma şarttır. Mesnetsiz basit manivela veya itici piston tek başına mekanik unsur sayılmaz. Ör.: kahve değirmeni, kıyma makinası, meyve sıkacağı, mekanik konserve açıcı."],
  ["82.11 – 82.15 Açıklama Notları", "82.11: sabit ve katlanır bıçaklar, çakılar (tirbuşon, tornavida, makaslı olsa da), ağızlar ve adi metal saplar; bağcı bıçağı 82.01’de. 82.12: elektriksiz traş makinaları ve bıçakları; bıçaksız plastik traş makinası 39.24. 82.13: parmak halkalı makaslar; nalbant toynak makası 82.05. 82.14: kağıt bıçağı, kalemtraş (kalem açma makinası 84.72), manikür takımları, elle saç kesme cihazı, satır. 82.15: kaşık, çatal, kepçe, kesici olmayan balık ve yağ bıçakları, maşalar."]
 ],
 "sinir_komsulari": [
  ["Elle kullanılan elektrik motorlu testere, pnömatik matkap", "84.67", "Genel Açıklamalar; 82.02 ve 82.05 Açıklama Notları"],
  ["Mesnet veya destek çerçevesi üzerine monte matkap", "84.59", "Genel Açıklamalar"],
  ["Kaideye monte, elle kullanılan giyotin tipi metal makası", "84.62", "Genel Açıklamalar"],
  ["Elektrikli traş makinası; başları ve bıçakları", "85.10", "Fasıl 82 Not 2"],
  ["Elektrikli ütü", "85.16", "82.05 Açıklama Notu"],
  ["Cerrahi makas, dişçi aleti", "90.18", "Genel Açıklamalar"],
  ["Kumpas, kalibre gibi ölçme aletleri", "Fasıl 90", "82.05 Açıklama Notu"],
  ["Bileği taşı, aşındırıcı kaplı dişsiz kesme diski", "68.04", "Genel Açıklamalar; 82.02 Açıklama Notu"],
  ["İş gören kısmı kauçuktan cam silme aleti", "Fasıl 40", "Fasıl 82 Not 1; Genel Açıklamalar"],
  ["Dağcı kazması", "95.06", "82.01 Açıklama Notu"],
  ["El aletlerine mahsus alet tutucu", "84.66", "Fasıl 82 Not 2"],
  ["Çelikten budama makası yayı; çelik alet vidası", "73.20 / 73.18", "Genel kullanım aksamı (Bölüm XV Not 2)"],
  ["Gümüş saplı sofra bıçağı", "Fasıl 71", "Genel Açıklamalar"],
  ["Tek başına sunulan, monte edilmemiş elmas", "71.02", "82.05 Açıklama Notu"],
  ["Seyahat tuvalet veya dikiş takımı (manikür takımı hariç)", "96.05", "96.05 Açıklama Notu"]
 ],
 "tuzaklar": [
  "<b>Parmak halkası makası ayırır.</b> Tek elle kullanılan, halkasız budama ve kümes hayvanı makasları 82.01’de; parmak geçecek halkalı makaslar 82.13’te; iki saplı nalbant toynak makası 82.05’te.",
  "<b>Mesnet ve motor fasıl değiştirir.</b> Mesnetsiz el matkabı 82.05, mesnetli matkap 84.59; elle kullanılan motorlu, pnömatik veya hidrolik aletler 84.67.",
  "<b>Elektrikli traş makinasının bıçağı Fasıl 82’de değildir.</b> Başlar, bıçaklar ve kesici levhalar 85.10’dadır (Not 2); elektriksiz traş makinası ve bıçakları 82.12.",
  "<b>Bıçak-çatal takımında sayıya bakılır.</b> Bıçak sayısı 82.15 eşyasının sayısını geçmiyorsa takım 82.15’tedir (Not 3); bıçaklar daha fazlaysa takım 82.11’de kalır.",
  "<b>Balık ve yağ bıçağı “bıçak” pozisyonunda değildir.</b> Kesici olmayan balık ve yağ bıçakları ile şeker maşaları 82.15’tedir.",
  "<b>Çakı 82.11, bağcı bıçağı 82.01.</b> Budama çakısı 82.11’de; bağcı bıçakları ve geniş yüzlü şeker kamışı bıçakları 82.01’dedir.",
  "<b>Monte edilmemiş uç 82.09, monte edilmiş uç 82.07.</b> Sermet veya sinterlenmiş karbür uç alete takılmadıkça 82.09’dadır; saf karbür tozu 28.49’dur.",
  "<b>Basit konserve açacağı 82.05, mekanik olanı 82.10.</b> 82.10 için mekanizma ve 10 kg sınırı birlikte aranır; basit manivela yeterli değildir.",
  "<b>Vida, yay, zincir alet parçası sayılmaz.</b> Budama makasına özgü yay bile genel kullanım aksamıdır ve kendi pozisyonuna gider (Bölüm XV Not 2; Fasıl 82 Not 2).",
  "<b>Manikür takımı 82.14, seyahat takımları 96.05.</b> Tuvalet, dikiş ve ayakkabı temizleme seyahat takımları 96.05’tedir; manikür takımı bundan açıkça hariçtir."
 ],
 "hafiza": {
  "kanca": "“Bahçeden sofraya”: 01 bahçe → 02 testere → 03 pens → 04 anahtar → 05 diğer → 06 çanta → 07 uç → 08 makine bıçağı → 09 sermet → 10 kıyma → 11 bıçak → 12 ustura → 13 makas → 14 manikür → 15 kaşık",
  "aciklama": "Bahçede (82.01) dalı testereyle (82.02) kes, pensle (82.03) tut, anahtarla (82.04) sık, kalan aletler (82.05) çantaya (82.06); makineye uç tak (82.07), bıçağını (82.08) ve sermet ucunu (82.09) değiştir. Mutfakta kıyma makinasını (82.10) çevir, bıçakla (82.11) doğra, usturayla (82.12) traş ol, makasla (82.13) kes, manikürünü (82.14) yap ve kaşık-çatalla (82.15) sofraya otur."
 },
 "sinav_odagi": [
  "82.06 takım tanımı: 82.02–82.05 aletlerinden oluşan takımlar içinde 82.01’deki bir aletin (ör. çit makası) bulunduğu seçeneği bulma kalıbı.",
  "Manikür takımının (82.14) seyahat tuvalet, dikiş ve ayakkabı temizleme takımlarından (96.05) farklı fasılda yer alması.",
  "GYK 3(b) takım sorularında Fasıl 82 eşyasının çeldirici olması: kalem açacağı içeren çizim takımının esas karakter nedeniyle 90.17’de sınıflandırılması.",
  "El aleti ile makine sınırı: dinamometrik sıkıştırma anahtarı gibi bir el aletinin bir makine ile birlikte sunulduğu senaryolar.",
  "Fasıl 71 ile sınır: “mücevherci eşyası” tabirinin çatal-bıçak gibi sofra takımlarını kapsamaması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Tarife mevzuatına göre aşağıdakilerden hangisi farklı fasılda yer alır?",
   "secenekler": ["Tuvalet takımı", "Dikiş takımı", "Ayakkabı temizleme takımı", "Manikür takımı"],
   "cevap": "D",
   "aciklama": "Manikür ve pedikür takımları 82.14’te (Fasıl 82) yer alır. Seyahat için hazırlanmış tuvalet, dikiş ve ayakkabı-elbise temizleme takımları ise 96.05’tedir; 96.05 Açıklama Notu manikür takımını açıkça hariç tutar."
  },
  {
   "soru": "Tarife Cetvelinde 82.02 ila 82.05 pozisyonlarındaki aletlerin iki veya daha fazlasından meydana gelen perakende satış için hazırlanmış takımlar 82.06 tarife pozisyonunda yer almaktadır. Buna göre aşağıdaki hangi takım 82.06 pozisyonunda sınıflandırılmaz?",
   "secenekler": ["El testeresi, pens, sıkıştırma anahtarı", "Çit makası, kaynak lambası, portatif demirci ocağı", "Eğe, tenekeci makası, camcı elması", "Kerpeten, boru kesici, örs", "Mengene, testere ağzı, törpü"],
   "cevap": "B",
   "aciklama": "B seçeneğindeki çit makası 82.01’dedir ve 82.06’nın tanımladığı 82.02–82.05 aletleri arasında değildir. Diğer seçeneklerdeki testere ve testere ağzı (82.02), pens, eğe, törpü, teneke makası, kerpeten, boru kesici (82.03), sıkıştırma anahtarı (82.04), camcı elması, örs ve mengene (82.05) bu pozisyonlardadır."
  }
 ],
 "ozet": [
  "İş gören kısım testi (Not 1): adi metal, karbür, sermet, mesnetli kıymetli taş veya aşındırıcı; değilse maddesine göre.",
  "Elde kullanılan alet Fasıl 82; mesnetli veya monte cihaz Fasıl 84; motorlu, pnömatik, hidrolik el aleti 84.67.",
  "01 bahçe · 02 testere · 03 eğe-pens-makas-zımba · 04 anahtar · 05 diğer el aletleri · 06 takım · 07 değişebilir alet · 08 makine bıçağı · 09 sermet uç.",
  "10 mekanik mutfak (10 kg veya daha hafif) · 11 bıçak · 12 ustura · 13 makas · 14 diğer bıçakçı ve manikür · 15 kaşık-çatal.",
  "Parçalar ana eşyayla; genel kullanım aksamı ve alet tutucular (84.66) dışarıda; elektrikli traş başları 85.10.",
  "Bıçak + en az eşit sayıda kaşık-çatal takımı 82.15 (Not 3)."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1
S.append(soru(
 "Tarife Cetveline göre, tek elle kullanılan, parmak geçecek halkası bulunmayan, bir kolu konkav diğeri kesici ağızlı konveks (“papağan gagası”) ve yaylı bahçe budama makası hangi pozisyonda sınıflandırılır?",
 ["82.13", "82.01", "82.03", "82.11", "82.14"], "B", E4,
 "82.01 Açıklama Notu, tek elle kullanılan budama makaslarını ve benzerlerini bu pozisyona alır ve bunları parmak geçecek halkaları olmadığı için 82.13’teki makaslardan ayırır. Budama çakısı 82.11’de, kesici pensler 82.03’tedir. Tuzak, “makas” kelimesini görüp 82.13’ü seçmektir.",
 "82.01 Açıklama Notu; 82.13 Açıklama Notu."))
# 2
S.append(soru(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 82. faslında <b>sınıflandırılmaz</b>?",
 ["İş gören kısmı kauçuktan olan, adi metal saplı cam silme aleti", "Kaynak lambası", "Portatif demirci ocağı", "El ile işleyen çatkılı bileği", "Manikür takımı"], "A", OT,
 "Fasıl 82 Not 1’e göre fasıl, iş gören kısmı adi metal, karbür, sermet gibi maddelerden olan eşyayı kapsar; iş gören kısmı kauçuk olan alet maddesine göre Fasıl 40’ta sınıflandırılır, metal sapı sonucu değiştirmez. Kaynak lambası, portatif demirci ocağı, çatkılı bileği ve manikür takımı Not 1’deki istisnalar olduğundan iş gören kısım şartına tabi değildir.",
 "Fasıl 82 Not 1; Fasıl 82 Genel Açıklamalar."))
# 3
S.append(soru(
 "Fasıl 82 Not 1’e göre aşağıdakilerden hangisi, iş gören kısmı notta sayılan maddelerden olmasa bile bu fasılda yer alır?",
 ["İş gören kısmı keçeden olan aletler", "İş gören kısmı seramikten olan değişebilir aletler", "Çatkısı olmayan bileği taşları", "Ağzı ve sapı tamamen plastikten olan mutfak spatulası", "Manikür ve pedikür takımları"], "E", FN,
 "Fasıl 82 Not 1, 82.09 eşyası, kaynak lambaları, portatif demirci ocakları, çatkılı bileğiler ile manikür ve pedikür takımlarını iş gören kısım şartının dışında tutar. Keçeden iş gören kısımlı aletler Fasıl 59’da, seramik değişebilir aletler 69.09’da, çatkısız bileği taşları 68.04’te, tamamen plastik spatula Fasıl 39’dadır.",
 "Fasıl 82 Not 1; Fasıl 82 Genel Açıklamalar."))
# 4
S.append(soru(
 "Aşağıdaki makaslardan hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
 ["Terzi makası", "Kuaför makası", "Tek elle kullanılan, parmak halkası olmayan kümes hayvanı makası", "Manikür makası", "Puro makası"], "C", FA,
 "Kümes hayvanı makasları tek elle kullanılan budayıcılar gibi 82.01’de sayılmıştır; parmak geçecek halkaları yoktur. Terzi, kuaför, manikür ve puro makasları parmak halkalı makaslar olarak 82.13’tedir.",
 "82.01 ve 82.13 Açıklama Notları."))
# 5
S.append(soru(
 "Tarife Cetveline göre, mesnedi veya destek çerçevesi bulunmayan, basit dişli mekanizmalı, elle çevrilerek kullanılan el matkabı hangi pozisyonda sınıflandırılır?",
 ["84.59", "82.07", "84.67", "82.05", "82.04"], "D", E4,
 "Fasıl 82 Genel Açıklamalarına göre basit dişli mekanizması olsa da mesnedi olmayan, elde kullanılan el matkabı 82.05’tedir; mesnet veya destek çerçevesine monte matkap ise 84.59’a gider. 84.67 motorlu, pnömatik veya hidrolik el aletleri, 82.07 matkap uçları gibi değişebilir aletler içindir.",
 "Fasıl 82 Genel Açıklamalar; 82.05 Açıklama Notu."))
# 6
S.append(soru(
 "Kendine özgü şekilde yapılmış, uzun süre kullanılmaya uygun deri kılıfı ile birlikte sunulan ve normal olarak bu kılıfla satılan bir av bıçağında, kılıfın bıçakla birlikte 82.11 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
 ["GYK 3(b)", "GYK 5(b)", "GYK 5(a)", "GYK 2(a)", "GYK 3(c)"], "C", GY,
 "GYK 5(a), belli bir eşyaya göre şekil verilmiş, uzun süre kullanılmaya uygun, eşyayla birlikte sunulan ve normal olarak onunla satılan mahfazaların eşya ile birlikte sınıflandırılmasını öngörür; bıçak kılıfı bu niteliktedir. 5(b) normal ambalaj malzemesi, 3(b) takımlar ve bileşik eşya içindir. Kılıf ayrı sunulsaydı kendi pozisyonunda yer alırdı.",
 "GYK 5(a) ve Açıklama Notu; 82.11 Açıklama Notu."))
# 7
S.append(soru(
 "Fasıl 82 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Elektrikli saç kesme makinalarının bıçakları 85.10 pozisyonunda yer alır.<br/>II. El aletlerine mahsus alet tutucular 82.07 pozisyonunda yer alır.<br/>III. Dağcılara mahsus kazmalar 82.01 pozisyonunda yer alır.<br/>IV. Cerrahide kullanılan makaslar 90.18 pozisyonunda yer alır.",
 ["I ve II", "II ve III", "I ve IV", "III ve IV", "I, III ve IV"], "C", CC,
 "Fasıl 82 Not 2, elektrikli traş ve saç kesme makinalarının bıçaklarını 85.10’a gönderir (I doğru). Aynı not el aletlerine mahsus alet tutucuları 84.66’ya bırakır (II yanlış). Dağcı kazmaları 82.01’den hariç tutulup 95.06’ya gönderilmiştir (III yanlış). Cerrahi makaslar Genel Açıklamalara göre 90.18’dedir (IV doğru).",
 "Fasıl 82 Not 2; 82.01 Açıklama Notu; Fasıl 82 Genel Açıklamalar."))
# 8
S.append(soru(
 "Aşağıdakilerden hangisi 82.05 pozisyonunda <b>yer almaz</b>?",
 ["Tornavida", "Çekiç", "Kılavuz anahtarı", "Saplı camcı elması", "Elektrikle çalışan ütü"], "E", OT,
 "82.05 Açıklama Notu ev işlerinde kullanılan gaz, parafin veya odun kömürü ile çalışan ütüleri kapsar, ancak elektrikle çalışan ütüleri 85.16’ya bırakır. Tornavida, çekiç, saplı camcı elması 82.05’te sayılır; kılavuz anahtarları da 82.04’ten hariç tutulup 82.05’e alınmıştır.",
 "82.05 Açıklama Notu; 82.04 Açıklama Notu."))
# 9
S.append(soru(
 "Perakende satış için kutulanmış; 6 sofra bıçağı, 6 çatal ve 6 kaşıktan oluşan takım Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
 ["82.11", "82.15", "82.14", "82.06", "73.23"], "B", FN,
 "Fasıl 82 Not 3’e göre 82.11’deki bir veya daha fazla bıçak ile 82.15’teki en az eşit sayıda eşyadan oluşan takımlar 82.15’tedir. Burada 6 bıçağa karşılık 12 adet 82.15 eşyası (çatal ve kaşık) bulunduğundan takım 82.15’tedir. 82.06 yalnız 82.02–82.05 aletlerinden takımlar içindir.",
 "Fasıl 82 Not 3; 82.15 Açıklama Notu."))
# 10
S.append(soru(
 "Tarife Cetveline göre tek elle kullanılan, parmak halkası olmayan budama makasları …… pozisyonunda; parmak geçecek halkalı makaslar …… pozisyonunda; nalbantlara mahsus iki saplı toynak kesme makasları ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
 ["82.13 – 82.01 – 82.05", "82.01 – 82.13 – 82.03", "82.01 – 82.01 – 82.13", "82.01 – 82.13 – 82.05", "82.03 – 82.13 – 82.05"], "D", EB,
 "Halkasız, tek elle kullanılan budama makasları 82.01’de; parmak geçecek halkalı makaslar 82.13’te yer alır. 82.13 Açıklama Notu nalbantlara mahsus iki saplı toynak kesme makaslarını hariç tutarak 82.05’e gönderir.",
 "82.01 ve 82.13 Açıklama Notları."))
# 11
S.append(soru(
 "Tarife Cetveline göre, kıyma makinasına takılan, monte edilmemiş delikli dairesel kesici ağız hangi pozisyonda sınıflandırılır?",
 ["82.10", "82.11", "82.08", "84.38", "82.07"], "C", E4,
 "82.08 makine ve mekanik cihazlara mahsus monte edilmemiş bıçak ve kesici ağızları kapsar; Açıklama Notu gıda sanayii veya mutfak cihazları için kıyma makinası bıçak ağızlarını açıkça sayar. Fasıl 82 Not 2’ye göre ismen belirtilen aksam kendi pozisyonundadır; makinanın pozisyonuna (82.10 veya 84.38) gitmez. 82.07 değişebilir aletler içindir.",
 "82.08 Açıklama Notu; Fasıl 82 Not 2."))
# 12
S.append(soru(
 "Plastik bir alet kutusu içinde perakende satışa sunulan; bir çekiç, bir pense, iki tornavida, bir ayarlı sıkıştırma anahtarı ve bir demir testeresinden oluşan takım hangi pozisyonda sınıflandırılır?",
 ["82.05", "82.03", "42.02", "82.04", "82.06"], "E", SN,
 "Takımdaki aletler 82.02 (testere), 82.03 (pense), 82.04 (anahtar) ve 82.05 (çekiç, tornavida) pozisyonlarındandır; 82.02–82.05 aletlerinden iki veya daha fazlasından oluşan ve perakende satış için hazırlanmış takımlar 82.06’dadır. Plastik kutu takımın esas niteliğini vermez; tek tek pozisyonlara ayırmak tuzaktır.",
 "82.06 pozisyon metni ve Açıklama Notu."))
# 13
S.append(soru(
 "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir fasılda yer alır?",
 ["Elektriksiz traş makinası", "Ustura", "Traş bıçağı şerit taslağı", "Elektriksiz traş makinası bıçağı", "Elektrikli traş makinasının kesici başı"], "E", FA,
 "Fasıl 82 Not 2, elektrikli traş makinalarının başlarını, bıçaklarını ve kesici parçalarını 85.10’a gönderir. Elektriksiz traş makinaları, usturalar, bunların bıçakları ve delikleri açılmış şerit taslakları 82.12’dedir. Tuzak, kesici parçayı metal olduğu için Fasıl 82’de aramaktır.",
 "Fasıl 82 Not 2; 82.12 Açıklama Notu."))
# 14
S.append(soru(
 "Aşağıdakilerden hangisi 82.11 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Katlanabilir cep çakısı", "Kesici olmayan balık bıçağı", "Kasap bıçağı", "Budama çakısı", "Birden fazla değiştirilebilir ağzı olan bıçak"], "B", OT,
 "82.11 Açıklama Notu balık bıçaklarını ve yağ bıçaklarını hariç tutarak 82.15’e gönderir; 82.15 kesici olmayan balık ve yağ bıçaklarını sofra eşyası olarak sayar. Cep çakısı, kasap bıçağı, budama çakısı ve değiştirilebilir ağızlı bıçaklar 82.11’dedir.",
 "82.11 ve 82.15 Açıklama Notları."))
# 15
S.append(soru(
 "Fasıl 82 Not 2’ye göre aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Fasıl eşyasının adi metal aksamı, ismen belirtilenler ve el aletlerine mahsus 84.66’daki alet tutucular hariç, ait olduğu eşyanın pozisyonunda yer alır.", "Budama makasları için özel olarak üretilmiş yaylar budama makasının pozisyonunda sınıflandırılır.", "Elektrikli traş makinalarının bıçakları 82.12 pozisyonunda yer alır.", "El aletlerine mahsus alet tutucular 82.07 pozisyonunda yer alır.", "Testere kolu gibi açıkça tanınabilen parçalar her durumda 73.26 pozisyonunda yer alır."], "A", FN,
 "Fasıl 82 Not 2’ye göre aksam ana eşyanın pozisyonunda yer alır; ismen belirtilen aksam ve 84.66’daki alet tutucular istisnadır. Genel kullanım aksamı olan yaylar, budama makası için özel olsa da fasıl dışıdır; elektrikli traş makinası bıçakları 85.10’dadır. Testere kolu gibi parçalar Açıklama Notuna göre ait oldukları aletle birlikte sınıflandırılır.",
 "Fasıl 82 Not 2; Bölüm XV Not 2; Fasıl 82 Genel Açıklamalar."))
# 16
S.append(soru(
 "Ağırlığı 2,5 kg olan, krank kollu ve Arşimet vidası mekanizmalı, elle çalışan, elektriksiz ev tipi et kıyma makinası Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
 ["84.38", "82.05", "85.09", "82.10", "82.08"], "D", E4,
 "82.10, yiyecek ve içeceklerin hazırlanmasında kullanılan, ağırlığı 10 kg veya daha az olan, elle işleyen mekanik aletleri kapsar; Arşimet vidası ve krank kolu mekanik unsurdur ve Açıklama Notu et kıyma cihazlarını açıkça sayar. Elektriksiz olduğundan 85.09’a, hafif ve elle çalıştığından 84.38’e girmez; 82.08 yalnız makinanın bıçağı içindir.",
 "82.10 pozisyon metni ve Açıklama Notu."))
# 17
S.append(soru(
 "Deri bir mahfaza içinde perakende satışa sunulan; elektrikli saç kesme makinası, tarak, bir çift makas, fırça ve havludan oluşan saç bakım takımı hangi pozisyonda ve hangi kurala göre sınıflandırılır?",
 ["82.13 – GYK 3(b)", "85.10 – GYK 3(b)", "42.02 – GYK 5(a)", "96.05 – GYK 1", "85.10 – GYK 3(c)"], "B", GY,
 "Takım, farklı pozisyonlardaki eşyadan oluşan ve perakende satılacak hale getirilmiş bir takımdır; GYK 3(b) Açıklama Notu bu örnekte takıma esas niteliği elektrikli saç kesme makinasının verdiğini ve takımın 85.10’da sınıflandırıldığını belirtir. Makas (82.13) ve mahfaza (42.02) esas niteliği vermez; 3(c) ancak esas nitelik belirlenemezse uygulanır.",
 "GYK 3(b) Açıklama Notu (X); Fasıl 82 Not 2."))
# 18
S.append(soru(
 "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda yer alır?",
 ["Kalemtraş – et satırı", "Çakı – kağıt bıçağı", "Şeker maşası – cımbız", "Basit konserve açacağı – mekanik konserve açıcı", "Matkap ucu – el matkabı"], "A", FA,
 "Kalemtraşlar ile kasap veya mutfak satırları 82.14’te birlikte sayılmıştır. Çakı 82.11, kağıt bıçağı 82.14; şeker maşası 82.15, cımbız 82.03; basit konserve açacağı 82.05, mekanik olanı 82.10; matkap ucu 82.07, el matkabı 82.05’tedir.",
 "82.03, 82.05, 82.07, 82.10, 82.11, 82.14 ve 82.15 Açıklama Notları."))
# 19
S.append(soru(
 "Aşağıdaki eşya ile pozisyonları eşleştirildiğinde hangisi <b>doğru</b> olur?<br/>I. Kaya delmeye mahsus sondaj ucu<br/>II. Kıyma makinası bıçağı<br/>III. Alete monte edilmemiş, sinterlenmiş karbür uç<br/>IV. Elle kullanılan dinamometrik sıkıştırma anahtarı<br/>a) 82.04 b) 82.07 c) 82.08 d) 82.09",
 ["I-b, II-c, III-d, IV-a", "I-c, II-b, III-d, IV-a", "I-b, II-d, III-c, IV-a", "I-a, II-c, III-d, IV-b", "I-b, II-c, III-a, IV-d"], "A", EB,
 "Kaya delme ve sondaj aletleri değişebilir alet olarak 82.07’de; makine bıçakları 82.08’de; alete monte edilmemiş sermet (sinterlenmiş karbür) uçlar 82.09’da; dinamometrik anahtarlar dahil elle kullanılan sıkıştırma anahtarları 82.04’tedir.",
 "82.04, 82.07, 82.08 ve 82.09 pozisyon metinleri ve Açıklama Notları; Bölüm XV Not 4."))
# 20
S.append(soru(
 "Tarife Cetveline göre, kesici ağzı olmayan sofra tipi tereyağı bıçağı hangi pozisyonda sınıflandırılır?",
 ["82.11", "82.14", "82.05", "82.13", "82.15"], "E", E4,
 "82.15 pozisyon metni balık bıçaklarını ve yağ bıçaklarını kaşık, çatal ve kepçe ile birlikte sayar; Açıklama Notu kesici olmayan balık ve yağ bıçaklarını burada gösterir. 82.11 Açıklama Notu bunları açıkça hariç tutar. Tuzak, adındaki “bıçak” kelimesine bakarak 82.11’i seçmektir.",
 "82.15 pozisyon metni ve Açıklama Notu; 82.11 Açıklama Notu."))
# 21
S.append(soru(
 "Aşağıdaki kesici aletlerden hangisi 82. Fasılda <b>yer almaz</b>?",
 ["Terzi makası", "Kuaför makası", "Teneke makası", "Ameliyatlarda kullanılan cerrahi makas", "Çit makası"], "D", OT,
 "Fasıl 82 Genel Açıklamaları tıp, dişçilik, cerrahi ve veterinerlikte kullanılan alet, makas ve diğer bıçakçı eşyasını hariç tutarak 90.18’e gönderir. Terzi ve kuaför makasları 82.13’te, teneke makası 82.03’te, çit makası 82.01’de, yani Fasıl 82’dedir.",
 "Fasıl 82 Genel Açıklamalar (hariç tutmalar)."))
# 22
S.append(soru(
 "82.10 pozisyonuna göre, yiyecek veya içecek hazırlamada kullanılan elle işleyen bir cihazın bu pozisyonda yer alabilmesi için aranan şartlar hangi seçenekte doğru verilmiştir?",
 ["Ağırlığı 10 kg veya daha az olmalı ve manivelalı kol, dişli, Arşimet vidası, pompa gibi bir mekanizma içermelidir.", "Ağırlığı 10 kg veya daha az olmalı ve elektrik motoru içermelidir.", "Ağırlığı 20 kg veya daha az olmalı; mekanizma şartı aranmaz.", "Ağırlığı ne olursa olsun, yalnızca basit bir manivela içermesi yeterlidir.", "Ağırlığı 5 kg veya daha az olmalı ve duvara tespit edilmiş olmalıdır."], "A", FN,
 "82.10 pozisyon metni ve Açıklama Notuna göre cihaz 10 kg veya daha hafif olmalı, genellikle elle çalışan elektriksiz bir cihaz olmalı ve manivelalı kol, dişli tertibat, Arşimet vidası, pompa gibi bir mekanizma içermelidir. Mesnet yoksa basit bir manivela veya itici piston tek başına mekanik unsur sayılmaz.",
 "82.10 pozisyon metni ve Açıklama Notu."))
# 23
S.append(soru(
 "Aşağıdaki testere ve testere ürünlerinden hangisi diğerlerinden <b>farklı</b> bir fasılda yer alır?",
 ["Demir testeresi", "Zincir halinde testere ağzı", "Dairevi testere ağzı", "Elle kullanılan, elektrik motorlu taşınabilir daire testere", "Katlanabilir bahçıvan testeresi"], "D", FA,
 "82.02 Açıklama Notu motorlu el testerelerini hariç tutarak 84.67’ye gönderir; elle kullanılan motorlu aletler Fasıl 84’tedir. Demir testeresi, katlanabilir bahçıvan testeresi ile zincir ve dairevi testere ağızları 82.02’de, yani Fasıl 82’dedir.",
 "82.02 Açıklama Notu; Fasıl 82 Genel Açıklamalar."))
# 24
S.append(soru(
 "Tarife Cetveline göre aşağıdakilerden hangileri 82.05 pozisyonunda sınıflandırılır?<br/>I. Saplı camcı elması<br/>II. Parafinle çalışan ütü<br/>III. Elle kullanılan pnömatik perçin tabancası<br/>IV. Tezgah mengenesi",
 ["I ve II", "I, II ve IV", "II ve III", "I, III ve IV", "Yalnız IV"], "B", CC,
 "82.05 Açıklama Notu saplı camcı elmaslarını, gaz veya parafin ile çalışan ütüleri ve tezgah mengenelerini kapsar (I, II ve IV). Elle kullanılan pnömatik, hidrolik veya motorlu aletler ise 82.05’ten hariç tutulup 84.67’ye gönderilmiştir (III).",
 "82.05 Açıklama Notu."))
# 25
S.append(soru(
 "Bir firma, adi metal gövdeli ve plastik kaplamalı; iki katlanır bıçak ağzı, bir tirbuşon, bir tornavida ve küçük bir makas içeren cep çakıları ithal etmektedir. Ürün hangi pozisyonda sınıflandırılır?",
 ["82.05", "82.06", "82.11", "82.13", "82.14"], "C", SN,
 "82.11 Açıklama Notu, cepte taşınan bıçak ve çakıların birden fazla ağızlı olabileceğini ve tirbuşon, bız, tornavida, makas, konserve açacağı gibi aletlerle donatılabileceğini açıkça belirtir. Ürün tek bir eşyadır; 82.06 takımları, 82.13 makasları, 82.05 diğer el aletlerini kapsar.",
 "82.11 Açıklama Notu."))

kaydet(obj, 82)
