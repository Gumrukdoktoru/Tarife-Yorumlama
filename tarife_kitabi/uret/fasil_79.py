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
 "fasil": 79,
 "baslik": "Çinko ve çinkodan eşya",
 "bolum": "XV",
 "oz": {
  "vurgu": "Fasıl 79 basamak basamak ilerler: işlenmemiş çinko 79.01, hurda 79.02, toz ve pul 79.03, çubuk-profil-tel 79.04, yassı ürünler 79.05, geri kalan her şey 79.07. Eşyanın çinkodan sayılması için çinkonun ağırlıkça üstün metal olması gerekir (Bölüm XV Not 5 ve 7); çinko kaplama ise eşyanın faslını değiştirmez.",
  "maddeler": [
   "Toz ve pullar ayrı pozisyondadır (79.03); “ince toz” çinko buharının yoğunlaştırılmasıyla elde edilir, ağırlıkça en az %80’i 63 mikrometrelik elekten geçer.",
   "Çubuk, profil ve tel 79.04’te; sac, levha, şerit ve yaprak 79.05’te; boru ve bağlantı parçaları için ayrı pozisyon yoktur (79.06 boş), bunlar 79.07’dedir.",
   "Çinkodan çivi, vida, cıvata, kova, eviye, oluk, depluvayye, boş bitki etiketi ve kurban anotlar 79.07’dedir.",
   "Kül, kalıntı, galvanizleme çamuru ve “çinko kurumu” 26.20’de; cevher 26.08’de; pirinç (bakır üstün) Fasıl 74’te; galvanizli çelik eşya Fasıl 72–73’tedir.",
   "Kilit (83.01), bilgi taşıyan levha ve etiket (83.10), eritici kaplı kaynak çubuğu (83.11) çinkodan olsa da Fasıl 83’tedir."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Çinko cevheri veya zenginleştirilmiş cevher mi (çinko blend gibi)?", "<b>26.08</b>"],
   ["2", "Çinko imali veya galvanizlemeden kalan kül, çamur, tekne dibi artığı ya da “çinko kurumu” mu?", "<b>26.20</b>"],
   ["3", "Bölüm XV Not 1 veya Fasıl 82–83 tarafından ismen alınmış mı?", "Kilit <b>83.01</b> · kapı kolu <b>83.02</b> · bilgi taşıyan levha <b>83.10</b> · kaplı kaynak çubuğu <b>83.11</b> · boya Fasıl 32 · vana <b>84.81</b>"],
   ["4", "Ağırlıkça üstün metal çinko mu?*", "Hayır ise ilgili metalin faslı (pirinç Fasıl 74; galvanizli çelik Fasıl 72–73)"],
   ["5", "Kesinlikle kullanılmaz halde çinko döküntü veya hurda mı?", "<b>79.02</b>"],
   ["6", "İnce toz, toz veya pul mu?", "<b>79.03</b> (pellet ise 79.01; boya halinde Fasıl 32)"],
   ["7", "Blok, külçe, kalın dilim, pellet veya yeniden döküm için döküm çubuğu mu (hurdadan eritilmiş külçe dahil)?", "<b>79.01</b>"],
   ["8", "Çubuk, profil veya tel mi (kaplamasız kaynak çubuğu dahil)?", "<b>79.04</b>"],
   ["9", "Sac, levha, şerit veya yaprak mı?", "<b>79.05</b>"],
   ["10", "Hiçbiri değilse (boru, bağlantı parçası, kap, çivi, oluk, anot, depluvayye…)", "<b>79.07</b>"]
  ],
  "dipnot": "* Alaşımda çinko ağırlıkça diğer metallerin her birinden fazla olmalıdır (Bölüm XV Not 5); birden fazla adi metalden eşyada da ağırlıkça üstün metal esas alınır (Bölüm XV Not 7)."
 },
 "pozisyon_haritasi": [
  ["79.01", "İşlenmemiş çinko", "Spelter’den saf çinkoya; blok, külçe, kalın dilim, pellet; toz hariç", "Galvanizleme için çinko külçe, çinko pelleti"],
  ["79.02", "Çinko döküntü ve hurdaları", "Kullanılmaz metal; kül ve kalıntılar hariç", "Çinko levha kırpıntısı, eskimiş çinko oluk"],
  ["79.03", "Çinkodan ince tozlar, tozlar ve pullar", "İnce toz: buhar yoğunlaştırma, 63 mikrometre; toz: Not 8(b)", "Şerardizasyon tozu, çinko pulu"],
  ["79.04", "Çinko çubuk, profil ve teller", "Not 9(a)–(c); kaplamasız kaynak çubuğu dahil", "Püskürtme kaplama teli, çinko profil"],
  ["79.05", "Çinko sac, levha, yaprak ve şeritler", "Not 9(d) yassı ürün; depluvayye hariç", "Çatı çinko levhası, pil zarfı şeridi"],
  ["79.07", "Çinkodan diğer eşya", "Artık pozisyon; boru ve bağlantı parçaları dahil", "Oluk, kova, çivi, kurban anot, boş bitki etiketi"]
 ],
 "notlar": [
  ["Bölüm XV Not 1", "Bölüm dışı (özet): metalik toz veya pul esaslı müstahzar boyalar (32.07–32.10, 32.12, 32.13, 32.15); Fasıl 71 eşyası; Bölüm XVI (makine, mekanik cihaz, elektrikli alet); Bölüm XVII; Bölüm XVIII; Bölüm XIX; Fasıl 94, 95, 96 ve 97 eşyası."],
  ["Bölüm XV Not 2", "Genel kullanıma mahsus aksam: 73.07, 73.12, 73.15, 73.17, 73.18 eşyası ve diğer adi metallerden benzerleri; yaylar (saat zemberekleri hariç); 83.01, 83.02, 83.08, 83.10 eşyası ile 83.06’daki çerçeve ve aynalar. 82 veya 83. Fasıl eşyası 72–76 ve 78–81. Fasıllara verilmez."],
  ["Bölüm XV Not 5", "Adi metal alaşımı, ağırlıkça diğer metallerin <b>her birinden</b> üstün olan metalin alaşımıdır. Bölüm XV metalleri ile Bölüm dışı elemanlardan oluşan alaşım, adi metallerin toplam ağırlığı diğer elemanların toplamına <b>eşit veya fazlaysa</b> Bölüm XV alaşımıdır (aksi halde genellikle 38.24). Sinterlenmiş karışımlar, eritmeyle elde edilen heterojen karışımlar ve metallerarası bileşimler de alaşımdır."],
  ["Bölüm XV Not 7 ve Genel Açıklamalar (B)", "İki veya daha fazla adi metal içeren eşya, ağırlıkça diğer metallerin her birinden üstün olan metalden mamul sayılır; alaşımlar, Not 5’e göre alaşımı sayıldıkları metalden ibaret kabul edilir. Kısmen metal olmayan maddeden eşyada, GYK’ye göre esas niteliği adi metal vermelidir."],
  ["Bölüm XV Not 8", "Döküntü ve hurda: tamamen metal döküntüler ile kırılma, kesilme, eskime vb. nedenlerle kesinlikle kullanılmaz haldeki metal eşya. Toz: göz açıklığı <b>1 mm</b> olan elekten ağırlıkça <b>%90 veya daha fazlası</b> geçen ürün."],
  ["Bölüm XV Not 9", "Çubuk: enine kesiti her yerde aynı, rulo halinde olmayan içi dolu ürün; tel: aynı özellikte, rulo halinde. Profil: diğer tanımlara uymayan, kesiti her yerde aynı ürün. Levha, sac, şerit ve yaprak: kalınlığı genişliğinin onda birini geçmeyen yassı ürün; delinmiş, oluklanmış, parlatılmış veya kaplanmış olabilir. Boru: tek kapalı boşluklu, kesiti ve et kalınlığı her yerde aynı içi boş ürün."],
  ["Fasıl 79 Altpozisyon Notu 1(c)", "“Çinkodan ince tozlar” (79.03 metninde geçer): çinko buharının yoğunlaştırılmasıyla elde edilen, çinko tozlarından daha ince yuvarlak parçacıklar; ağırlıkça en az <b>%80</b>’i göz açıklığı <b>63 mikrometre</b> olan elekten geçer ve ağırlıkça en az <b>%85</b> metalik çinko içerir."],
  ["Genel Açıklamalar", "Çinko-alüminyum alaşımları (basınçlı döküm: karbüratör gövdesi, radyatör kafesi; katodik koruma anotları) ve çinko-bakır (metal düğme) alaşımları, çinko üstün olduğunda bu fasıldadır; pirinç gibi alaşımlarda başka metal üstündür. Fasıl 72 Genel Açıklamalarında sayılan yüzey işlemleri sınıflandırmayı etkilemez."],
  ["79.01 Açıklama Notu", "Spelter’den saf çinkoya her saflıkta işlenmemiş çinko: blok, levha, külçe, çubuk, kalın dilim veya pellet. İnce tozlar, tozlar ve pullar hariç (79.03)."],
  ["79.02 Açıklama Notu", "Çinko imalinden veya galvanizlemeden kalan küller ve artıklar (elektrolitik galvanizleme çamurları, sıcak daldırma teknesinin dibindeki metalik artıklar) 26.20’de; hurdadan eritilmiş külçeler 79.01’dedir."],
  ["79.03 Açıklama Notu", "Çinkodan ince tozlar, 26.20’deki “çinko kurumu”, “çinko oksit kurumu” veya “filtre artığı çinko kurumu” ile karıştırılmamalıdır. Boya olarak hazırlanmış toz ve pullar Fasıl 32’de, çinko pelletleri 79.01’dedir."],
  ["79.04 Açıklama Notu", "Çinko esaslı kaynak çubukları eritici madde ile kaplanmamışsa burada, kaplanmışsa 83.11’de; haddeleme veya yeniden döküm için döküm çubukları 79.01’dedir."],
  ["79.05 Açıklama Notu", "Çatı kaplaması, kuru pil zarfları, fotogravür ve litografya levhaları için kullanılır. Metal depluvayye (79.07) ve 84.42’deki hazırlanmış klişe levhaları bu pozisyona dahil değildir."],
  ["79.07 Açıklama Notu", "Mekanik veya termik tertibatsız depo ve kaplar; eczacılık tüpleri; çinko telden mensucat, kafeslik ve depluvayye; çivi, somun, cıvata, vida; kova, eviye, küvet, leğen (galvanizli demir-çelikten olanlar 73.23 / 73.24); bitki etiketleri (esaslı bilgi taşıyanlar 83.10); elektro kaplama ve kurban anotlar; oluk, mahya, çerçeve gibi inşaat eşyası; ince ve kalın borular ile bağlantı parçaları."]
 ],
 "sinir_komsulari": [
  ["Çinko blend (çinko cevheri), zenginleştirilmiş cevher", "26.08", "Cevherler Bölüm XV dışında"],
  ["Galvanizleme çamuru, sıcak daldırma teknesi dibi artığı, çinko külü", "26.20", "79.02 hariç tutması"],
  ["“Çinko kurumu”, “filtre artığı çinko kurumu”", "26.20", "79.03 Açıklama Notu"],
  ["Çinko tozu içeren hazır boya", "Fasıl 32", "Bölüm XV Not 1; 79.03 hariç tutması"],
  ["Pirinç (bakırın ağırlıkça üstün olduğu bakır-çinko alaşımı)", "Fasıl 74", "Bölüm XV Not 5"],
  ["Çinko kaplı (galvanizli) çelik sac, genişliği 600 mm veya fazla", "72.10", "Esas metal çelik; kaplama faslı değiştirmez"],
  ["Galvanizli demir-çelikten kova, eviye, küvet", "73.23 / 73.24", "79.07 Açıklama Notu"],
  ["Eritici madde ile kaplanmış çinko esaslı kaynak çubuğu", "83.11", "79.04 hariç tutması"],
  ["Esaslı bilgileri taşıyan çinko etiket veya cadde levhası", "83.10", "79.07 Açıklama Notu"],
  ["Hazırlanmış klişe (baskı) levhası", "84.42", "79.05 hariç tutması"],
  ["Çinkodan kapı kilidi; kapı kolu ve topuzu", "83.01 / 83.02", "Fasıl 83 eşyası (Bölüm XV Not 2)"],
  ["Çinkodan musluk ve vana", "84.81", "Bölüm XVI (Bölüm XV Not 1)"],
  ["Kullanılmış kuru pil, pil döküntü ve hurdası", "85.48", "Bölüm XV Genel Açıklamaları"]
 ],
 "tuzaklar": [
  "<b>Pirinç çinko değildir.</b> Pirinçte bakır ağırlıkça üstün olduğundan Fasıl 74’tedir; çinko-alüminyum basınçlı döküm alaşımı ise çinko üstünse Fasıl 79’dadır.",
  "<b>Üstünlük “her birinden” ölçülür.</b> %40 çinko, %35 alüminyum, %25 bakır içeren alaşım çinko alaşımıdır; çinkonun %50’yi geçmesi gerekmez.",
  "<b>“Çinko kurumu” 79.03 değildir.</b> Çinko buharının yoğunlaştırılmasıyla elde edilen ince toz 79.03’tür; “çinko kurumu”, “çinko oksit kurumu”, “filtre artığı çinko kurumu” 26.20’dedir.",
  "<b>Pellet tozla aynı yerde değildir.</b> Çinko pelleti işlenmemiş çinkodur (79.01); toz, ince toz ve pullar 79.03’tür.",
  "<b>Galvanizli eşya çinkodan eşya değildir.</b> Çinko kaplama bir yüzey işlemidir; galvanizli çelik kova 73.23’te, galvanizli çelik sac Fasıl 72’dedir.",
  "<b>Kaynak çubuğunda üç ihtimal.</b> Kaplamasız çinko kaynak çubuğu 79.04; eritici madde ile kaplanmış olan 83.11; yeniden döküm için döküm çubuğu 79.01.",
  "<b>Etiket bilgi taşıyorsa Fasıl 83’e gider.</b> Yalnız sonradan eklenecek bilgi için alan bulunan bitki etiketi 79.07; esaslı bilgileri taşıyan etiket ve levha 83.10.",
  "<b>Boru için ayrı pozisyon yok.</b> 79.06 boştur; çinko borular ve bağlantı parçaları 79.07’dedir. 79.04’teki içi boş profiller ise boru sayılmaz.",
  "<b>Depluvayye levha değildir.</b> Çinkodan metal depluvayye 79.05’te değil, 79.07’dedir."
 ],
 "hafiza": {
  "kanca": "İŞ – HU – TO – ÇU – YA – Dİ (01 – 02 – 03 – 04 – 05 – 07)",
  "aciklama": "<b>İŞ</b>lenmemiş 79.01 · <b>HU</b>rda 79.02 · <b>TO</b>z ve pul 79.03 · <b>ÇU</b>buk-profil-tel 79.04 · <b>YA</b>ssı ürün 79.05 · <b>Dİ</b>ğer her şey 79.07. Kurşundan farkı: çinkoda toz ve çubuk-tel kendi pozisyonlarına sahiptir; boş kalan yalnız 79.06’dır (boru), o da “diğer” sepetine düşer."
 },
 "sinav_odagi": [
  "Fasıl 79 çıkmış sorularda doğrudan neredeyse hiç sorulmamış; Bölüm XV’in ortak tanım ve kurallarının uygulandığı fasıllardan biri olarak dolaylı biçimde yer almıştır.",
  "Bölüm XV Not 9 tanımları: çubuk ile telin rulo halinde olup olmama ölçütüyle ayrılması (tanım sorusu kalıbı).",
  "Hangi adi metallerin kendine ait bir faslı olduğu: kurşun, çinko ve kalayın ayrı fasılları varken magnezyum, titanyum, krom gibi metallerin Fasıl 81’de toplanması.",
  "“Aynı bölümde yer alan eşya” kalıbı: adi metalden kapı kilidi gibi eşyanın Bölüm XV’te, makine ve elektrikli cihazların Bölüm XVI’da olması."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Türk Gümrük Tarife Cetveli’nin XV. Bölüm Notlarına göre “çubuk” ve “tel” arasındaki farklılık nedir?",
   "secenekler": ["Enine kesitleri", "Üretim yöntemleri", "İçlerinin dolu-boş olması", "Rulo halde olup olmaması", "Mamul oldukları madde"],
   "cevap": "D",
   "aciklama": "Bölüm XV Not 9(a) ve (c)’ye göre çubuk rulo halinde olmayan, tel ise rulo halinde olan içi dolu üründür; enine kesit şekilleri aynıdır. Çinkoda çubuk, profil ve tel birlikte 79.04’te yer alır."
  }
 ],
 "ozet": [
  "Sıra: cevher 26.08 → işlenmemiş 79.01 → hurda 79.02 → toz-pul 79.03 → çubuk-profil-tel 79.04 → yassı 79.05 → diğer 79.07.",
  "İnce toz: buhar yoğunlaştırma; ağırlıkça en az %80’i 63 mikrometrelik elekten geçer, en az %85 metalik çinko; “çinko kurumu” 26.20.",
  "Pellet 79.01; toz ve pul 79.03; boya halinde Fasıl 32.",
  "Boru ve bağlantı parçaları, çivi-vida, kova, oluk, anot, depluvayye ve boş etiket 79.07.",
  "Çinko kaplama faslı değiştirmez: galvanizli çelik Fasıl 72–73; pirinç Fasıl 74.",
  "Fasıl 83’e gidenler: kilit 83.01, kapı kolu 83.02, bilgi taşıyan levha 83.10, kaplı kaynak çubuğu 83.11."
 ],
 "sorular": []
}

S = obj["sorular"]

# 1
S.append(soru(
 "Tarife Cetveline göre, çinko buharının yoğunlaştırılmasıyla elde edilen, ağırlıkça %90’ı göz açıklığı 63 mikrometre olan elekten geçen ve ağırlıkça %95 metalik çinko içeren ince toz hangi pozisyonda sınıflandırılır?",
 ["79.01", "26.20", "79.03", "79.02", "79.04"], "C", E4,
 "Çinko buharının yoğunlaştırılmasıyla elde edilen, ağırlıkça en az %80’i 63 mikrometrelik elekten geçen ve en az %85 metalik çinko içeren ürün “çinkodan ince toz”dur ve 79.03’te yer alır. 79.01 Açıklama Notu tozları işlenmemiş çinkodan hariç tutar. 26.20 ise “çinko kurumu” gibi artıkları kapsar; tuzak, ince tozu kurumla karıştırmaktır.",
 "Fasıl 79 Altpozisyon Notu 1(c); 79.01 ve 79.03 Açıklama Notları."))
# 2
S.append(soru(
 "Aşağıdakilerden hangisi 79.07 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Çinkodan cıvata ve somun", "Eczacılık ürünlerinin ambalajında kullanılan çinko tüp", "Çinkodan yağmur oluğu", "Üzerinde cadde adı ve bina numarası kabartma olarak bulunan çinko levha", "Çinko telden kafeslik"], "D", OT,
 "Yol, cadde ve bina adı veya numarası gibi esaslı bilgileri taşıyan adi metal levhalar 83.10’dadır; Bölüm XV Not 2 son paragrafı uyarınca 83. Fasıl eşyası Fasıl 79’a verilmez. Cıvata ve somun, eczacılık tüpü, oluk ve çinko telden kafeslik 79.07 Açıklama Notunda sayılan eşyadır.",
 "79.07 Açıklama Notu; 83.10 Açıklama Notu; Bölüm XV Not 2."))
# 3
S.append(soru(
 "Fasıl 79 alt pozisyon notunda tanımlanan ve 79.03 pozisyon metninde geçen “çinkodan ince tozlar” için aşağıdakilerden hangisi <b>doğrudur</b>?",
 ["Çinko buharının yoğunlaştırılmasıyla elde edilir; ağırlıkça en az %80’i göz açıklığı 63 mikrometre olan elekten geçer ve en az %85 metalik çinko içerir.",
  "Göz açıklığı 1 mm olan elekten ağırlıkça %90 veya daha fazlası geçen ürünlerdir.",
  "Çinko cevherinin öğütülmesiyle elde edilir ve ağırlıkça en az %97,5 çinko içerir.",
  "Ağırlıkça en az %80’i göz açıklığı 1 mm olan elekten geçer ve en az %85 çinko oksit içerir.",
  "Çinko imalinden kalan ve “çinko kurumu” olarak bilinen tozlardır."], "A", FN,
 "Fasıl 79 Altpozisyon Notu 1(c), ince tozları çinko buharının yoğunlaştırılmasıyla elde edilen, ağırlıkça en az %80’i 63 mikrometrelik elekten geçen ve en az %85 metalik çinko içeren ürün olarak tanımlar. 1 mm / %90 ölçütü Bölüm XV Not 8(b)’deki genel “toz” tanımıdır; %97,5 alaşımsız çinko eşiğidir. “Çinko kurumu” 26.20’dedir.",
 "Fasıl 79 Altpozisyon Notu 1(c); Bölüm XV Not 8(b); 79.03 Açıklama Notu."))
# 4
S.append(soru(
 "Aşağıdaki çinko ürünlerinden hangisi diğerlerinden <b>farklı</b> bir pozisyonda yer alır?",
 ["Çinko profil", "Çinko tel", "Çinko çubuk", "Kaplamasız çinko esaslı kaynak çubuğu", "Çinkodan ince boru"], "E", FA,
 "Çinkoda boru için ayrı pozisyon yoktur (79.06 boş); Bölüm XV Not 9(e) tanımına uyan çinko borular 79.07’dedir. Çubuk, profil ve teller ile eritici madde ile kaplanmamış çinko esaslı kaynak çubukları 79.04’te yer alır.",
 "79.04 ve 79.07 Açıklama Notları; Bölüm XV Not 9."))
# 5
S.append(soru(
 "Tarife Cetveline göre, asetilen şalümosu ile püskürtme suretiyle çinko kaplama yapılmasında kullanılan, rulo halinde, üzeri herhangi bir maddeyle kaplanmamış çinko tel hangi pozisyonda sınıflandırılır?",
 ["79.04", "79.03", "79.07", "83.11", "72.17"], "A", E4,
 "79.04 Açıklama Notu çinko tellerin özellikle şalümo ile püskürtülerek çinko kaplamada ilk madde olarak kullanıldığını belirtir; rulo halindeki içi dolu ürün Bölüm XV Not 9(c) anlamında teldir. 83.11 yalnız eritici veya temizleyici madde ile kaplanmış ya da içi doldurulmuş teller içindir. 72.17 demir-çelik tellere aittir.",
 "79.04 Açıklama Notu; Bölüm XV Not 9(c); 83.11 Açıklama Notu."))
# 6
S.append(soru(
 "Tüm parçaları birlikte, demonte halde gümrüğe sunulan, çinkodan imal edilmiş bir banyo küvetinin 79.07 pozisyonunda sınıflandırılmasında hangi Genel Yorum Kuralları uygulanır?",
 ["GYK 1 ve 2(a)", "GYK 1 ve 2(b)", "GYK 1 ve 3(a)", "GYK 1 ve 3(c)", "GYK 1 ve 5(b)"], "A", GY,
 "GYK 2(a)’nın ikinci kısmına göre birleştirilmemiş veya demonte halde sunulan eşya, monte edilmiş eşya ile aynı pozisyonda sınıflandırılır; çinkodan banyo küvetleri 79.07 Açıklama Notunda sayılmıştır. 2(b) madde karışımları ve bileşik eşya, 3(a) ve 3(c) birden fazla pozisyona girebilen eşya, 5(b) ambalaj için uygulanır.",
 "GYK 1 ve 2(a); 79.07 Açıklama Notu."))
# 7
S.append(soru(
 "Fasıl 79 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Çinko pelletleri 79.03 pozisyonunda yer alır.<br/>II. Çinkodan ince ve kalın borular 79.07 pozisyonunda yer alır.<br/>III. Çinkodan metal depluvayye 79.07 pozisyonunda yer alır.<br/>IV. Elektrolitik galvanizleme sonucunda meydana gelen çamurlar 79.02 pozisyonunda yer alır.",
 ["I ve II", "II ve III", "I ve IV", "II, III ve IV", "III ve IV"], "B", CC,
 "Çinko pelletleri 79.03’ten açıkça hariç tutulmuş olup 79.01’dedir (I yanlış). Borular ve bağlantı parçaları 79.07’dedir (II doğru). Metal depluvayye 79.05’ten hariç tutulup 79.07’de sayılmıştır (III doğru). Galvanizleme çamurları 79.02’den hariç tutulmuş, 26.20’ye gönderilmiştir (IV yanlış).",
 "79.02, 79.03, 79.05 ve 79.07 Açıklama Notları."))
# 8
S.append(soru(
 "Aşağıdakilerden hangisi Tarife Cetvelinin 79. faslında <b>yer almaz</b>?",
 ["Çinko pelleti", "Galvanizli demir-çelikten kova", "Çinkodan eviye", "Kaplamasız çinko esaslı kaynak çubuğu", "Çinkodan ince pullar"], "B", OT,
 "79.07 Açıklama Notu, ev işlerinde kullanılan kova, eviye gibi eşyanın çoğunun galvanizli demir veya çelikten yapıldığını ve bu nedenle 73.23 ve 73.24’e girdiğini belirtir; çinko kaplama esas metali değiştirmez. Çinko pelleti 79.01, çinkodan eviye 79.07, kaplamasız kaynak çubuğu 79.04, ince pullar 79.03’tedir.",
 "79.07 Açıklama Notu; Bölüm XV Not 7; Fasıl 72 Genel Açıklamalar (yüzey işlemleri)."))
# 9
S.append(soru(
 "Ağırlıkça %40 çinko, %35 alüminyum ve %25 bakır içeren işlenmemiş bir alaşım Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
 ["76.01", "74.03", "79.01", "79.07", "81.04"], "C", FN,
 "Bölüm XV Not 5’e göre alaşım, ağırlıkça diğer metallerin her birinden üstün olan metalin alaşımıdır. Çinko (%40) toplamda %50’yi geçmese de alüminyumdan (%35) ve bakırdan (%25) ayrı ayrı fazladır; işlenmemiş çinko alaşımı 79.01’dedir. Tuzak, üstünlüğü diğer metallerin toplamıyla karşılaştırmaktır.",
 "Bölüm XV Not 5 ve Not 6; 79.01 Açıklama Notu."))
# 10
S.append(soru(
 "Tarife Cetveline göre çinko tozları …… pozisyonunda, çinko pelletleri …… pozisyonunda, “filtre artığı çinko kurumu” ise …… pozisyonunda sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
 ["79.01 – 79.03 – 79.02", "79.03 – 79.03 – 26.20", "79.03 – 79.01 – 26.20", "79.03 – 79.01 – 79.02", "79.01 – 79.01 – 26.08"], "C", EB,
 "Çinko tozları ve pulları 79.03’tedir; 79.03 Açıklama Notu çinko pelletlerini hariç tutarak 79.01’e gönderir. Aynı not, “çinko kurumu”, “çinko oksit kurumu” ve “filtre artığı çinko kurumu” gibi ürünlerin 26.20’de yer aldığını belirtir. 26.08 cevherleri, 79.02 hurdaları kapsar.",
 "79.03 Açıklama Notu; 79.01 Açıklama Notu."))
# 11
S.append(soru(
 "Tarife Cetveline göre, kuru pillerin zarflarının imalinde kullanılan, Bölüm XV Not 9(d) tanımına uyan rulo halinde çinko şerit hangi pozisyonda sınıflandırılır?",
 ["79.04", "79.05", "79.07", "85.06", "72.12"], "B", E4,
 "Bölüm XV Not 9(d) tanımına uyan saclar, levhalar, şeritler ve yapraklar 79.05’tedir; Açıklama Notu çinko sac ve levhaların kuru pil zarflarının imalinde kullanıldığını belirtir. Kullanım amacı şeridi pil pozisyonuna (85.06) taşımaz; 79.04 çubuk ve tel, 72.12 demir-çelik yassı ürün pozisyonudur.",
 "79.05 Açıklama Notu; Bölüm XV Not 9(d)."))
# 12
S.append(soru(
 "Çatı kaplamasında kullanılmak üzere ithal edilen ürün; ağırlıkça %99 çinko içeren, haddelenmiş, rulo halinde, kalınlığı 0,7 mm, genişliği 1000 mm olan, yüzeyi delinmiş ve oluklanmış, ancak başka bir pozisyondaki eşyanın niteliğini kazanmamış yassı bir üründür. Ürün hangi pozisyonda sınıflandırılır?",
 ["79.05", "79.04", "79.07", "72.10", "79.01"], "A", SN,
 "Kalınlığı genişliğinin onda birini geçmeyen yassı ürün Bölüm XV Not 9(d) anlamında levha, sac veya şerittir; not, delinmiş, oluklanmış, parlatılmış veya kaplanmış olanların da başka bir eşya niteliği kazanmadıkça bu pozisyonlarda kalacağını belirtir. Bu nedenle ürün 79.05’tedir. 72.10 çelik yassı ürünler, 79.07 ise şekil verilmiş inşaat eşyası içindir.",
 "Bölüm XV Not 9(d); 79.05 Açıklama Notu."))
# 13
S.append(soru(
 "Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir fasılda yer alır?",
 ["Çinkodan asma kilit", "Çinkodan vida", "Çinkodan kova", "Çinkodan elektro kaplama anodu", "Kiremitleri tutturmaya mahsus çinko çengel"], "A", FA,
 "Adi metalden kilitler ve asma kilitler, yapıldığı metal ne olursa olsun 83.01’dedir; Bölüm XV Not 2 son paragrafı Fasıl 83 eşyasının Fasıl 79’a verilmesini engeller. Vida, kova, elektro kaplama anodu ve kiremit çengeli 79.07 Açıklama Notunda sayılan çinko eşyadır.",
 "83.01 Açıklama Notu; Bölüm XV Not 2; 79.07 Açıklama Notu."))
# 14
S.append(soru(
 "Aşağıdakilerden hangisi 79.03 pozisyonunda <b>sınıflandırılmaz</b>?",
 ["Çinko buharının yoğunlaştırılmasıyla elde edilen ince toz", "Bölüm XV Not 8(b) tanımına uyan çinko tozu", "Çinkodan ince pullar", "Şerardizasyon yöntemiyle kaplamada kullanılan çinko tozu", "Çinko pelletleri"], "E", OT,
 "79.03 Açıklama Notu çinko pelletlerini açıkça hariç tutar; pelletler işlenmemiş çinko olarak 79.01’dedir. Buhar yoğunlaştırma ile elde edilen ince toz, Not 8(b)’ye uyan toz, ince pullar ve şerardizasyonda kullanılan toz 79.03’tedir.",
 "79.03 Açıklama Notu; 79.01 Açıklama Notu."))
# 15
S.append(soru(
 "Bölüm XV Not 5’e göre, Bölüm XV adi metalleri ile bu Bölüm dışında kalan elemanlardan oluşan bir alaşımın Bölüm XV’te adi metal alaşımı olarak sınıflandırılabilmesi için hangi şart aranır?",
 ["Alaşımda tek bir adi metalin ağırlıkça %50’den fazla olması", "Adi metallerin toplam ağırlığının diğer elemanların toplam ağırlığının iki katını geçmesi", "Alaşımın sinterleme yoluyla elde edilmiş olması", "Adi metallerin toplam ağırlığının diğer elemanların toplam ağırlığına eşit veya daha fazla olması", "Bölüm dışı elemanların ağırlıkça %10’u geçmemesi"], "D", FN,
 "Bölüm XV Not 5’e göre bu tür alaşımlar, bünyesindeki adi metallerin toplam ağırlığı diğer elemanların toplam ağırlığına eşit veya daha fazla olduğunda Bölüm XV alaşımı sayılır; aksi halde Bölüm Genel Açıklamalarına göre genellikle 38.24’e gider. Diğer seçeneklerde notta yer almayan oranlar veya yöntem şartları vardır.",
 "Bölüm XV Not 5; Bölüm XV Genel Açıklamalar (A)."))
# 16
S.append(soru(
 "Tarife Cetveline göre, galvanizleme işlemi sırasında sıcak daldırma teknesinin dibinde biriken metalik artık hangi pozisyonda sınıflandırılır?",
 ["79.02", "79.01", "26.08", "26.20", "79.03"], "D", E4,
 "79.02 Açıklama Notu, çinko imalinden veya galvanizleme işleminden meydana gelen külleri ve diğer artıkları (elektrolitik galvanizleme çamurları, sıcak daldırma teknelerinin dibindeki metalik artıklar) hurda pozisyonundan çıkararak 26.20’ye gönderir. 26.08 cevherleri kapsar; 79.01 işlenmemiş çinko, 79.03 toz ve pullar içindir.",
 "79.02 Açıklama Notu."))
# 17
S.append(soru(
 "Ahşap saplı, çinkodan bir kova (eşyaya esas niteliğini çinko gövde vermektedir) 79.07 pozisyonunda sınıflandırılırken hangi Genel Yorum Kuralları uygulanır?",
 ["Yalnız GYK 1", "GYK 1 ve 2(a)", "GYK 1 ve 3(c)", "GYK 1 ve 4", "GYK 1, 2(b) ve 3(b)"], "E", GY,
 "GYK 2(b)’ye göre belirli bir maddeden eşyaya yapılan atıf, kısmen o maddeden yapılmış eşyayı da kapsar ve birden fazla maddeden oluşan eşya Kural 3’e göre sınıflandırılır. Kova ilk bakışta hem ahşap hem çinko eşya olabileceğinden esas niteliği veren çinko gövde dikkate alınır (3(b)). Bölüm XV Genel Açıklamaları da kısmen metal olmayan eşyada esas niteliğin GYK’ye göre adi metalden gelmesini arar.",
 "GYK 2(b) ve 3(b); Bölüm XV Genel Açıklamalar (B); 79.07 Açıklama Notu."))
# 18
S.append(soru(
 "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da Tarife Cetvelinde <b>aynı</b> pozisyonda yer alır?",
 ["Çinko tozu – çinko pelleti", "Çinko hurdası – hurdadan eritilmiş çinko külçe", "Çinko sac – çinkodan metal depluvayye", "Çinko külçe – çinko pelleti", "Çinko tel – eritici madde ile kaplanmış çinko kaynak teli"], "D", FA,
 "Külçe ve pellet işlenmemiş çinko olarak birlikte 79.01’dedir. Toz 79.03, pellet 79.01; hurda 79.02, hurdadan eritilmiş külçe 79.01; sac 79.05, depluvayye 79.07; kaplamasız tel 79.04, eritici kaplı kaynak teli 83.11’dedir.",
 "79.01, 79.02, 79.03, 79.04, 79.05 ve 79.07 Açıklama Notları."))
# 19
S.append(soru(
 "Aşağıdaki eşya ile pozisyonları eşleştirildiğinde hangisi <b>doğru</b> olur?<br/>I. Kaplamasız çinko esaslı kaynak çubuğu<br/>II. Eritici madde ile kaplanmış çinko esaslı kaynak çubuğu<br/>III. Haddeleme veya yeniden döküm için çinko döküm çubuğu<br/>IV. Esaslı bilgileri taşıyan çinko etiket<br/>a) 79.01 b) 79.04 c) 83.10 d) 83.11",
 ["I-a, II-d, III-b, IV-c", "I-b, II-c, III-a, IV-d", "I-b, II-d, III-c, IV-a", "I-b, II-d, III-a, IV-c", "I-d, II-b, III-a, IV-c"], "D", EB,
 "Kaplamasız çinko kaynak çubuğu 79.04’te, eritici madde ile kaplanmış olanı 83.11’de, yeniden döküme mahsus döküm çubuğu 79.01’dedir. Esaslı bilgileri taşıyan etiketler 83.10’da; yalnız sonradan eklenecek bilgi için alanı bulunan etiketler ise 79.07’de kalır.",
 "79.04 ve 79.07 Açıklama Notları; 83.10 ve 83.11 Açıklama Notları."))
# 20
S.append(soru(
 "Tarife Cetveline göre, boruları ve gemi sarnıçlarını korozyona karşı korumak için kullanılan çinko alaşımından katodik koruma (kurban) anodu hangi pozisyonda sınıflandırılır?",
 ["79.01", "79.04", "79.05", "85.45", "79.07"], "E", E4,
 "79.07 Açıklama Notu, boruları, gemi sarnıçlarını vb. korozyona karşı korumak için kullanılan katodik koruma anotlarını (kurban anotlar) ve elektro kaplama anotlarını açıkça sayar. Ürün işlenmemiş çinko (79.01) veya çubuk-levha gibi yarı mamul değil, belirli bir işlevi olan eşyadır. 85.45 karbon elektrotlarını kapsar.",
 "79.07 Açıklama Notu; Fasıl 79 Genel Açıklamalar."))
# 21
S.append(soru(
 "Aşağıdakilerden hangisi 79.05 pozisyonunda <b>yer almaz</b>?",
 ["Çatı kaplamasında kullanılan çinko sac", "Kuru pil zarflarının imalinde kullanılan çinko levha", "Çinkodan metal depluvayye", "Çinko yaprak", "Çinko şerit"], "C", OT,
 "79.05 Açıklama Notu metal depluvayyeyi açıkça hariç tutar; çinkodan depluvayye 79.07’dedir. Çatı sacı, pil zarfı levhası, yaprak ve şerit Bölüm XV Not 9(d) anlamında yassı ürün olarak 79.05’te kalır.",
 "79.05 ve 79.07 Açıklama Notları; Bölüm XV Not 9(d)."))
# 22
S.append(soru(
 "Bölüm XV Not 9(e)’ye göre bir ürünün “ince veya kalın boru” sayılabilmesi için aşağıdakilerden hangisi gereklidir?",
 ["Rulo halinde olmaması ve et kalınlığının dış çapın onda birini geçmemesi", "Bütün uzunluğu boyunca yalnız bir kapalı boşluğu olması; enine kesiti ve et kalınlığının her yerde aynı olması", "Birden fazla kapalı boşluğu olabilmesi, ancak enine kesitinin daire olması", "Yalnız dikişsiz olarak üretilmiş olması", "Flanş, bilezik veya halka ile donatılmamış olması"], "B", FN,
 "Bölüm XV Not 9(e)’ye göre ince ve kalın borular, bütün uzunlukları boyunca sadece bir kapalı boşluğu olan, enine kesitleri ve et kalınlıkları her yerde aynı içi boş ürünlerdir; rulo halinde olabilirler. Not, boruların flanş, bilezik veya halka ile donatılmış olabileceğini de açıkça belirtir. Çinkoda bu tanıma uyan borular 79.07’dedir.",
 "Bölüm XV Not 9(e); 79.07 Açıklama Notu."))
# 23
S.append(soru(
 "Aşağıdaki metal ürünlerinden hangisi Tarife Cetvelinde diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
 ["Ağırlıkça %96 çinko ve %4 alüminyum içeren basınçlı döküm alaşımı külçe", "Ağırlıkça %60 bakır ve %40 çinkodan oluşan pirinç çubuk", "Çinkonun ağırlıkça üstün olduğu çinko-bakır alaşımından levha", "Çinkodan kurban anot", "Çinko döküntü ve hurdası"], "B", FA,
 "Pirinçte bakır ağırlıkça üstün olduğundan Bölüm XV Not 5 uyarınca bakır alaşımıdır ve Fasıl 74’tedir; Fasıl 79 Genel Açıklamaları da pirinçte başka metalin üstün olduğunu belirtir. Çinko-alüminyum külçe 79.01, çinko üstün levha 79.05, kurban anot 79.07, hurda 79.02’dedir.",
 "Bölüm XV Not 5; Fasıl 79 Genel Açıklamalar."))
# 24
S.append(soru(
 "Tarife Cetveline göre aşağıdakilerden hangileri Fasıl 79’da sınıflandırılır?<br/>I. Çinkodan çivi<br/>II. Bakırın ağırlıkça üstün olduğu pirinçten vida<br/>III. Çinko kaplı (galvanizli) çelik sac<br/>IV. Yalnız sonradan yazılacak bilgi için alanı bulunan, çinkodan bitki etiketi",
 ["I ve II", "II ve III", "I, II ve IV", "III ve IV", "I ve IV"], "E", CC,
 "Çinkodan çiviler ve esaslı bilgi taşımayan bitki etiketleri 79.07 Açıklama Notunda sayılmıştır (I ve IV). Pirinç bakır alaşımı olduğundan vida Fasıl 74’e gider (II); galvanizli çelik sacta esas metal çelik olduğundan ürün Fasıl 72’dedir (III).",
 "79.07 Açıklama Notu; Bölüm XV Not 5 ve Not 7."))
# 25
S.append(soru(
 "Bir firma, çinkonun ağırlıkça üstün olduğu bir çinko alaşımından basınçlı döküm yöntemiyle üretilmiş, bina iç kapılarına takılacak kapı kolları ve topuzları ithal etmektedir. Ürünlerde kilit mekanizması bulunmamaktadır. Ürünler hangi pozisyonda sınıflandırılır?",
 ["79.07", "83.01", "83.02", "73.26", "79.04"], "C", SN,
 "Kapılar için kollar ve topuzlar, imal edildiği adi metal ne olursa olsun 83.02’deki donanım ve tertibat arasında sayılmıştır. Bölüm XV Not 2 son paragrafı uyarınca 83. Fasıl eşyası, çinkodan olsa bile Fasıl 79’a verilmez. Kilit mekanizması olmadığından 83.01 söz konusu değildir; 73.26 demir-çelik eşya içindir.",
 "83.02 Açıklama Notu; Bölüm XV Not 2."))

kaydet(obj, 79)
