import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_09_13 import *  # noqa: F401,F403

d = {
 "tur": "fasil",
 "fasil": 9,
 "baslik": "Kahve, çay, paraguay çayı ve baharat",
 "bolum": "II",
 "oz": {
  "vurgu": "Fasıl 9; kahve, Thea cinsi çay, paraguay çayı ve baharatları kapsar. Temel test: ürün karakteristik tadı nedeniyle çeşni olarak kullanılan bir baharat mı, yoksa esas olarak parfümeri veya eczacılıkta kullanılan bir bitki (12.11) ya da sebze (Fasıl 7) mi? Baharat karışımlarında ise karışımdaki ürünlerin pozisyon sayısı ve esas özelliğin korunup korunmadığı belirleyicidir.",
  "maddeler": [
   "Bütün, ezilmiş veya toz halinde olmak pozisyonu değiştirmez; kahvede kavurma ve kafeinin alınması da 09.01’i bozmaz.",
   "Hülasa, esans ve konsantreler (instant kahve, çay hülasası) Fasıl 9’da değil, 21.01’dedir.",
   "09.02 yalnızca Thea (Camellia) cinsi çaydır; “çay” adı taşıyan diğer ürünler 09.03, 09.09, 12.11 veya 21.06’ya gider.",
   "Karışımlar Fasıl 9 Not 1 ile çözülür: aynı pozisyon → o pozisyon, farklı pozisyon → 09.10, esas özellik kaybı → 21.03."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Esas olarak parfümeri veya eczacılıkta kullanılan bir bitki mi? (nane, adaçayı, fesleğen, biberiye, kebabe biberi, karanfil kabuğu ve yaprağı)", "<b>12.11</b>"],
   ["2", "Taze yeşillik veya taze biber mi? (maydanoz, dere otu, kişniş otu, tere, tarhun; ezilmemiş taze Capsicum veya Pimenta)", "Fasıl 7 (taze biber <b>07.09</b>)"],
   ["3", "Hardal tohumu veya şerbetçi otu mu?", "<b>12.07</b> / <b>12.10</b> (hardal unu <b>21.03</b>)"],
   ["4", "Kahve mi? (çiğ, kavrulmuş, kafeinsiz, kabuk ve kapçık, kahve içeren ikame)", "<b>09.01</b> · hülasa, instant kahve ve kahvesiz ikame <b>21.01</b>"],
   ["5", "Thea (Camellia) cinsi çay mı? (aromalandırılmış veya kafeini alınmış dahil)", "<b>09.02</b>"],
   ["6", "Paraguay çayı (maté) mı?", "<b>09.03</b>"],
   ["7", "Tek bir baharat türü mü? (bütün, ezilmiş veya toz)", "<b>09.04</b> – <b>09.10</b> arasındaki kendi pozisyonu"],
   ["8", "09.04–09.10 ürünlerinin karışımı mı?", "Aynı pozisyondakiler o pozisyonda · farklı pozisyondakiler <b>09.10</b>"],
   ["9", "Katılan başka maddeler esas özelliği değiştirmiş mi?", "Çeşni veya lezzet verici karışım <b>21.03</b>*"]
  ],
  "dipnot": "* Seyrelticiler (tahıl unu, dekstroz), renk vericiler (ksantofil), tat artırıcılar (sodyum glutamat) ve korunma için küçük miktarda tuz veya antioksidan esas özelliği değiştirmedikçe sınıflandırmayı etkilemez. İçecek aromalandırmaya mahsus bitki karışımlarında asli karakter 09.04–09.10 türlerinden gelmiyorsa 21.06."
 },
 "pozisyon_haritasi": [
  ["09.01", "Kahve; kahve kabuk ve kapçıkları; kahve içeren ikameler", "Kavrulmuş veya kafeinsiz olsun olmasın; hülasa hariç", "Çiğ kahve çekirdeği, kafeinsiz öğütülmüş kahve, kahveli hindiba karışımı"],
  ["09.02", "Çay (aromalandırılmış olsun olmasın)", "Yalnızca Thea (Camellia) cinsi", "Siyah, yeşil, Oolong çayı; bergamutlu çay"],
  ["09.03", "Paraguay çayı (maté)", "Holly familyası ağaçların kurutulmuş yaprakları", "Maté yaprağı"],
  ["09.04", "Piper cinsi biber; Capsicum ve Pimenta (kurutulmuş, ezilmiş, öğütülmüş)", "Kebabe biberi hariç; taze Capsicum 07.09", "Karabiber, beyaz biber, kurutulmuş acı biber, paprika, Jamaika biberi"],
  ["09.05", "Vanilya", "Vanilin ve vanilya şekeri hariç", "Bütün veya öğütülmüş vanilya"],
  ["09.06", "Tarçın ve tarçın ağacının çiçekleri", "İç kabuk; chips, çiçek ve meyve dahil", "Çubuk tarçın, toz tarçın"],
  ["09.07", "Karanfil (meyve, çiçek ve saplar)", "Kabuk ve yaprak hariç (12.11)", "Kurutulmuş karanfil tomurcuğu"],
  ["09.08", "Küçük Hindistan cevizi, kabuğu ve kakule", "Malageta biberi de buradadır", "Küçük Hindistan cevizi, kakule"],
  ["09.09", "Anason, Çin anasonu, rezene, kişniş, kimyon, karaman kimyonu tohumları; ardıç meyveleri", "Bitkisel çayda kullanılsa bile burada", "Kimyon, kişniş tohumu, yıldız anason"],
  ["09.10", "Zencefil, safran, zerdeçal, kekik, defne yaprağı, köri ve diğer baharat", "Farklı pozisyon karışımlarının yeri", "Toz zencefil, safran, köri, defne yaprağı, dere otu tohumu"]
 ],
 "notlar": [
  ["Fasıl 9 Not 1", "09.04–09.10 ürünlerinin birbirleriyle karışımları: (a) aynı pozisyona giren ürünlerin karışımı o pozisyonda; (b) farklı pozisyonlara giren ürünlerin karışımı <b>09.10</b>’da sınıflandırılır. Başka maddelerin katılması esas özelliği değiştirmedikçe sınıflandırmayı etkilemez; aksi halde karışım bu fasılda yer almaz ve lezzet veya çeşni verici yapıdakiler <b>21.03</b>’te sınıflandırılır."],
  ["Fasıl 9 Not 2", "Kebabe biberi (Piper cubeba) ve 12.11 pozisyonunda yer alan diğer ürünler bu fasla dahil değildir."],
  ["Genel Açıklamalar", "Baharat: uçucu yağlar ve aromatik maddelerce zengin, karakteristik tatları nedeniyle çeşni maddesi olarak kullanılan bitkisel ürünler (tohumlar dahil). Bütün, ezilmiş veya toz halinde olabilir."],
  ["Genel Açıklamalar", "Esas özelliği değiştirmeyen katkılar: ölçmeyi ve dağılmayı kolaylaştıran seyrelticiler (tahıl unu, dekstroz), renk vericiler (ksantofil), tadı artıran ürünler (sodyum glutamat), korunma için küçük miktarlarda tuz veya kimyasal antioksidan."],
  ["Genel Açıklamalar", "Doğrudan meşrubata tat vermek veya meşrubat hülasası hazırlamak için kullanılan bitki karışımları: asli karakteri tek bir 09.04–09.10 türü veriyorsa o pozisyon; bu türlerin iki veya daha fazlasının karışımı veriyorsa 09.10; ikisi de değilse 21.06."],
  ["Genel Açıklamalar", "Fasıl dışı: Fasıl 7 sebzeleri (maydanoz, frenk maydanozu, tarhun, tere, kişniş otu, dere otu); hardal tohumu 12.07, hardal unu 21.03; şerbetçi otu 12.10; baharat olarak kullanılabilse de daha çok parfümeri veya ilaç yapımında kullanılan bitkiler (biberiye, fesleğen, bütün nane türleri, sedef otu, adaçayı) 12.11; karışık çeşni vericiler ve karışık baharatlar 21.03."],
  ["09.01 Açıklama Notu", "Çiğ kahve (kabuklu veya çekirdek), kafeini alınmış kahve, kavrulmuş kahve (öğütülmüş olsun olmasın), kahvenin kabuk ve kapçıkları, herhangi bir oranda kahve içeren ikameler. Hariç: kahve mumu 15.21; kahve hülasası, esansı, konsantresi (instant kahve) ve kahve içermeyen kavrulmuş ikameler 21.01; kafein 29.39."],
  ["09.02 Açıklama Notu", "Yalnız Thea (Camellia) cinsi: yeşil (fermente edilmemiş), siyah (fermente) ve kısmen fermente (Oolong) çay; çay çiçeği, tomurcuğu, kalıntıları, tablet veya sıkıştırılmış çay; uçucu yağ veya aromatik bitki katılmış ve kafeini alınmış çaylar. Hariç: paraguay çayı 09.03; bitkisel çaylar 08.13, 09.09, 12.11 veya 21.06; ginseng çayı 21.06."],
  ["09.04 Açıklama Notu", "Piper cinsi (kebabe hariç) karabiber, beyaz biber, uzun biber, biber tozu ve döküntüleri; Capsicum (acı biber, paprika) ve Pimenta (Jamaika biberi) cinsinin kurutulmuş veya ezilmiş ya da öğütülmüş meyveleri. Ezilmemiş, öğütülmemiş taze meyveler 07.09."],
  ["09.05 Açıklama Notu", "Hariç: vanilya oleorezini 13.02; vanilya şekeri 17.01 veya 17.02; vanilin (vanilyanın hoş kokulu özü) 29.12."],
  ["09.06 Açıklama Notu", "Tarçın (bazı ağaçların genç dallarının iç kabukları), “chips” denilen tarçın döküntüleri, kurutulup elekten geçirilmiş ve uzunluğu normalde <b>1 cm</b>’yi geçmeyen tarçın ağacı çiçekleri ile tarçın meyvesi."],
  ["09.07 Açıklama Notu", "Karanfil ağacının bütün haldeki meyveleri, olgunlaşmadan toplanıp güneşte kurutulmuş çiçekleri ve çiçek sapları. Karanfil kabuk ve yaprakları 12.11."],
  ["09.08 Açıklama Notu", "Küçük Hindistan cevizi, küçük Hindistan cevizi kabuğu (dış kabukla çekirdek arasındaki zarımsı tabaka) ve kakuleler; büyük kakuleler 27–40 mm uzunluğundadır. Malageta biberi (cennet tanesi) de bu pozisyondadır."],
  ["09.09 Açıklama Notu", "Bu pozisyondaki tohum ve meyveler, özellikle anason, bitkisel çay veya bitkisel içecek imalinde kullanılsalar bile 09.09’da kalır."],
  ["09.10 Açıklama Notu", "Zencefil (geçici olarak salamurada korunan taze zencefil dahil; şekerli şurupta korunan 20.08), safran, zerdeçal, kekik (yabani kekik dahil), defne yaprağı, köri, dere otu ve çemen otu tohumu ile farklı pozisyonlara giren 09.04–09.10 ürünlerinin karışımları."]
 ],
 "sinir_komsulari": [
  ["Kahve hülasası, instant kahve; kahve içermeyen kavrulmuş ikame (kavrulmuş hindiba, kavrulmuş arpa)", "21.01", "09.01 hariç tutması; ikamede kahve yok"],
  ["Kafein", "29.39", "Kahvenin alkaloidi; 09.01 ve 09.02 hariç tutması"],
  ["Kahve mumu", "15.21", "09.01 hariç tutması"],
  ["Ginseng çayı (laktoz ve glikoz içeren hülasa karışımı)", "21.06", "Thea cinsi değil; 09.02 hariç tutması"],
  ["Adaçayı, ıhlamur, nane, papatya (bitkisel çay)", "12.11", "Fasıl 9 Not 2; esas olarak eczacılıkta kullanılan bitkiler"],
  ["Kebabe biberi; karanfil kabuğu ve yaprağı", "12.11", "Fasıl 9 Not 2; 09.07 hariç tutması"],
  ["Ezilmemiş, öğütülmemiş taze acı biber veya dolmalık biber", "07.09", "Yalnız kurutulmuş veya ezilmiş, öğütülmüş olan 09.04"],
  ["Taze maydanoz, dere otu, kişniş otu, tere, tarhun", "Fasıl 7", "Sebze; Fasıl 9 Genel Açıklamalar"],
  ["Salep", "07.14", "Nişasta ve inülince zengin kök yumru; baharat değil"],
  ["Hardal tohumu / hardal unu", "12.07 / 21.03", "Fasıl 9 Genel Açıklamalar"],
  ["Şerbetçi otu kozalakları", "12.10", "Fasıl 9 Genel Açıklamalar"],
  ["Vanilya oleorezini / vanilya şekeri / vanilin", "13.02 / 17.01–17.02 / 29.12", "09.05 hariç tutması"],
  ["Şekerli şurupta korunmuş zencefil", "20.08", "09.10 hariç tutması"],
  ["Esas özelliği değişmiş baharat karışımı (karışık çeşni verici)", "21.03", "Fasıl 9 Not 1"]
 ],
 "tuzaklar": [
  "<b>Kafeinsiz veya öğütülmüş kahve hâlâ 09.01’dir; hülasa değildir.</b> Kafeinin alınması ve öğütme 09.01’i bozmaz; kahve hülasası, esansı ve konsantresi (instant kahve) ise 21.01’e gider.",
  "<b>İkamede kahve varsa 09.01.</b> Herhangi bir oranda kahve içeren kahve yerine kullanılan madde 09.01’de; hiç kahve içermeyen kavrulmuş ikame (kavrulmuş hindiba, kavrulmuş arpa) 21.01’de.",
  "<b>Her “çay” 09.02 değildir.</b> 09.02 yalnız Thea (Camellia) cinsidir. Paraguay çayı 09.03; adaçayı, ıhlamur, nane 12.11; anason tohumu 09.09; ginseng çayı ve karışık bitki çayları 21.06.",
  "<b>Aroma katılması çayı çay olmaktan çıkarmaz.</b> Bergamut veya limon yağı, yasemin çiçeği, kurutulmuş portakal kabuğu ya da karanfil katılmış çaylar ve kafeini alınmış çaylar 09.02’de kalır.",
  "<b>Karışımda önce pozisyon sayısına bakın.</b> Aynı pozisyondaki ürünlerin karışımı o pozisyonda kalır (karabiber + paprika = 09.04); farklı pozisyondakiler 09.10’a gider (karabiber + küçük Hindistan cevizi). Esas özellik kaybolmuşsa çeşni karışımı 21.03.",
  "<b>Tohum ile yaprak ayrı fasıllardadır.</b> Kişniş tohumu 09.09, kişniş otu Fasıl 7; dere otu tohumu 09.10, dere otu Fasıl 7.",
  "<b>Kebabe biberi Piper cinsidir ama 09.04’te değildir.</b> Fasıl 9 Not 2 onu 12.11’e gönderir. Pimenta cinsi Jamaika biberi ise 09.04’te, Malageta biberi (cennet tanesi) 09.08’dedir.",
  "<b>Taze biber Fasıl 7’dir.</b> Ezilmemiş, öğütülmemiş taze Capsicum ve Pimenta 07.09; kurutulmuş veya ezilmiş, öğütülmüş olanlar 09.04.",
  "<b>Zencefilde koruma ortamı belirleyicidir.</b> Geçici olarak salamurada korunan taze zencefil 09.10’da kalır; şekerli şurupta korunan zencefil 20.08’e gider.",
  "<b>Aynı ağacın farklı parçaları farklı yerdedir.</b> Karanfilin meyvesi, çiçeği ve sapı 09.07; kabuğu ve yaprağı 12.11. Tarçın ağacının çiçeği ve meyvesi ise 09.06’da kalır."
 ],
 "hafiza": {
  "kanca": "KA-ÇA-MA  /  Bİ-VA-TA-KA-KÜ-TO-ZE",
  "aciklama": "<b>KA</b>hve 09.01 · <b>ÇA</b>y 09.02 · <b>MA</b>té 09.03 · <b>Bİ</b>ber 09.04 · <b>VA</b>nilya 09.05 · <b>TA</b>rçın 09.06 · <b>KA</b>ranfil 09.07 · <b>KÜ</b>çük Hindistan cevizi ve kakule 09.08 · <b>TO</b>humlar (anason, rezene, kişniş, kimyon) ve ardıç 09.09 · <b>ZE</b>ncefil, safran, zerdeçal, kekik, defne, köri 09.10. Son durak 09.10 aynı zamanda farklı pozisyonlardaki baharatların karışımlarının da adresidir."
 },
 "sinav_odagi": [
  "“Hangisi 9. fasılda sınıflandırılmaz?” kalıbında vanilya, tarçın ve defne yaprağı gibi baharatların arasına başka fasılda yer alan bir bitkisel ürün (salep, Fasıl 7) yerleştirilmiştir.",
  "Bitkisel çay malzemesinin yeri sorulmuş; adaçayının 12.11’de olduğu, 09.02 (çay), 09.10 (diğer baharat) ve 07.12 (kurutulmuş sebze) seçeneklerinin çeldirici olduğu görülmüştür.",
  "“Tümü 12.11’de olanlar” sorusunda vanilya–tarçın–karanfil, kişniş–kimyon–anason tohumu, zencefil–kekik gibi Fasıl 9 grupları ile paraguay çayı çeldirici olarak kullanılmıştır.",
  "Bölüm bilgisi: kahvenin Bölüm II’de (bitkisel ürünler) yer aldığı; sirke, kakao, şeker ve meşrubatla birlikte verilerek Bölüm IV’e aitmiş gibi gösterildiği sorular vardır.",
  "Çay hülasasının Fasıl 9’da değil Fasıl 21’de olduğu, “aynı fasıl” sorularında dondurma, ketçap ve canlı maya ile aynı grupta verilerek sınanmıştır.",
  "GYK 3(b) takım sorularında bir kavanoz kahve ile seramik fincanın birlikte paketlenmesinin takım oluşturmadığı bilgisi kullanılmıştır."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Aşağıdaki bitkisel ürünlerden hangisi Türk Gümrük Tarife Cetveli’nin 9. faslında <b>sınıflandırılmaz</b>?",
   "secenekler": ["Salep", "Vanilya", "Tarçın", "Defne yaprağı"],
   "cevap": "A",
   "aciklama": "Salep, 07.14 pozisyon metninde sayılan, nişasta ve inülince zengin kök yumrulardandır (Fasıl 7). Vanilya 09.05’te, tarçın 09.06’da, defne yaprağı 09.10’da yer alır."
  },
  {
   "soru": "Bitkisel çay yapımında kullanılacak adaçayı aşağıdaki tarife pozisyonlarının hangisinde sınıflandırılır?",
   "secenekler": ["09.02", "09.10", "12.11", "07.12"],
   "cevap": "C",
   "aciklama": "Adaçayı, Fasıl 12 Not 4’te 12.11 kapsamında sayılmıştır; tek türden oluşan bitkisel “çay” da 12.11’de kalır. 09.02 yalnızca Thea cinsi çayları kapsar ve Fasıl 9 Not 2, 12.11 ürünlerini fasıl dışında bırakır."
  }
 ],
 "ozet": [
  "Kahve 09.01 (çiğ, kavrulmuş, kafeinsiz, kabuk-kapçık, kahve içeren ikame); hülasa ve kahvesiz ikame 21.01.",
  "Çay 09.02 yalnızca Thea cinsi; maté 09.03; bitki çayları 09.09, 12.11 veya 21.06.",
  "Biber 09.04 · vanilya 09.05 · tarçın 09.06 · karanfil 09.07 · küçük Hindistan cevizi ve kakule 09.08 · tohumlar ve ardıç 09.09 · zencefil, safran, zerdeçal, kekik, defne, köri 09.10.",
  "Karışım: aynı pozisyon → o pozisyon; farklı pozisyon → 09.10; esas özellik kaybolursa 21.03.",
  "Esas olarak parfümeri veya eczacılıkta kullanılan bitkiler ve kebabe biberi 12.11; taze yeşillikler ve taze biber Fasıl 7.",
  "Vanilin 29.12, vanilya şekeri 17.01/17.02, kafein 29.39, kahve mumu 15.21."
 ]
}

S = {}
# ---- Eşya → 4’lü pozisyon
S["E1"] = Q(T_ES,
 "Tarife Cetveline göre, kafeini alınmış, kavrulmuş ve öğütülmüş kahve hangi tarife pozisyonunda sınıflandırılır?",
 "09.01", ["21.01", "29.39", "09.02", "21.06"], "B",
 "09.01, kafeini alınmış olsun olmasın kavrulmuş kahveyi öğütülmüş halde de kapsar; kafeinin alınması ve öğütme pozisyonu değiştirmez. Kahve hülasası, esansı ve konsantreleri (instant kahve) 21.01’de, kahveden ayrılan kafein ise alkaloit olarak 29.39’dadır. Tuzak, “kafeinsiz” ifadesini işlenmiş ürün sanıp 21.01’e yönelmektir.",
 "09.01 pozisyon metni ve Açıklama Notu.")
S["E2"] = Q(T_ES,
 "Tarife Cetveline göre, bergamut yağı ilave edilerek aromalandırılmış, fermente edilmiş siyah çay hangi pozisyonda yer alır?",
 "09.02", ["09.03", "12.11", "21.01", "21.06"], "D",
 "09.02 pozisyon metni çayı “aromalandırılmış olsun olmasın” kapsar; limon veya bergamut yağı gibi uçucu yağlar ya da yasemin çiçeği, portakal kabuğu gibi bitkiler eklenerek tatlandırılan çaylar da buradadır. 09.03 paraguay çayına, 12.11 tıbbi ve aromatik bitkilere, 21.01 çay hülasalarına, 21.06 ginseng çayı gibi karışımlara aittir.",
 "09.02 pozisyon metni ve Açıklama Notu.")
S["E3"] = Q(T_ES,
 "Tarife Cetveline göre, Capsicum cinsine ait kurutulmuş ve öğütülmüş acı kırmızı biber hangi pozisyonda sınıflandırılır?",
 "09.04", ["07.09", "07.12", "09.10", "21.03"], "A",
 "09.04, Capsicum ve Pimenta cinsi biberlerin kurutulmuş veya ezilmiş ya da öğütülmüş meyvelerini kapsar. Ezilmemiş, öğütülmemiş taze meyveler 07.09’dadır; Fasıl 7 kurutulmuş veya öğütülmüş Capsicum’u açıkça 09.04’e gönderdiği için 07.12 de yanlıştır. Tek tür biber olduğundan 09.10 (karışım) ve 21.03 (çeşni karışımı) uygulanmaz.",
 "09.04 pozisyon metni ve Açıklama Notu; Fasıl 7 Genel Açıklamalar.")
S["E4"] = Q(T_ES,
 "Tarife Cetveline göre, cin gibi alkollü içkilere ve turşulara tat vermede kullanılan kurutulmuş ardıç meyveleri hangi pozisyonda yer alır?",
 "09.09", ["08.13", "09.10", "12.11", "22.08"], "E",
 "09.09 pozisyon metni ardıç meyvelerini anason, rezene, kişniş, kimyon ve karaman kimyonu tohumlarıyla birlikte sayar. Kurutulmuş meyve olması onu 08.13’e, baharat olması 09.10’a götürmez; daha özel olarak 09.09’da isimlendirilmiştir. Alkollü içkiye aroma vermede kullanılması da pozisyonu değiştirmez.",
 "09.09 pozisyon metni ve Açıklama Notu.")
S["E5"] = Q(T_ES,
 "Tarife Cetveline göre, şekerli şurup içinde korunmaya alınmış zencefil hangi pozisyonda sınıflandırılır?",
 "20.08", ["09.10", "17.04", "21.03", "21.06"], "C",
 "09.10 Açıklama Notu zencefili (geçici olarak salamurada korunmaya alınmış taze zencefil dahil) kapsar, ancak şekerli şurup içinde korunmaya alınmış zencefili açıkça 20.08’e gönderir. Şeker içermesi onu şekerleme (17.04) yapmaz; tek bir ürün olduğundan çeşni karışımı (21.03) da değildir. Tuzak, salamura ile şurup arasındaki farkı gözden kaçırmaktır.",
 "09.10 Açıklama Notu.")
# ---- Olumsuz teşhis
S["O1"] = Q(T_OL,
 "Aşağıdakilerden hangisi Tarife Cetvelinin 09.02 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Paraguay çayı (maté)",
 ["Kısmen fermente edilmiş Oolong çayı", "Yasemin çiçeği katılarak aromalandırılmış yeşil çay", "Tablet halinde sıkıştırılmış toz çay", "Kafeini alınmış siyah çay"], "E",
 "09.02 yalnızca Thea (Camellia) cinsi bitkilerden elde edilen çayları kapsar; kısmen fermente (Oolong), aromalandırılmış, sıkıştırılmış ve kafeini alınmış çaylar bu pozisyondadır. Holly familyasına dahil ağaçların kurutulmuş yapraklarından oluşan paraguay çayı ayrı bir pozisyonda, 09.03’te yer alır.",
 "09.02 ve 09.03 Açıklama Notları.")
S["O2"] = Q(T_OL,
 "Aşağıdakilerden hangisi Tarife Cetvelinin 9. faslında <b>sınıflandırılmaz</b>?",
 "Karanfil ağacının yaprakları",
 ["Kahvenin kabuk ve kapçıkları", "Tarçın döküntüleri (chips)", "Karanfil çiçeklerinin sapları", "Küçük Hindistan cevizi kabuğu"], "D",
 "Karanfil kabuk ve yaprakları 09.07’den açıkça hariç tutulmuş ve 12.11’e gönderilmiştir. Kahve kabuk ve kapçıkları 09.01’de, tarçın döküntüleri (chips) 09.06’da, karanfil sapları 09.07’de, küçük Hindistan cevizi kabuğu 09.08’dedir. Tuzak, aynı bitkinin her parçasının aynı pozisyona gittiğini sanmaktır.",
 "09.07 Açıklama Notu; Fasıl 9 Not 2; 09.01, 09.06, 09.08 Açıklama Notları.")
S["O3"] = Q(T_OL,
 "Aşağıdakilerden hangisi 09.04 pozisyonunda <b>sınıflandırılmaz</b>?",
 "Kebabe biberi (Piper cubeba)",
 ["Beyaz biber", "Uzun biber (Piper longum) meyvesi", "Kurutulmuş Jamaika biberi", "Biber tozu ve döküntüleri"], "B",
 "Kebabe biberi Piper cinsine girmesine rağmen Fasıl 9 Not 2 ile fasıl dışında bırakılmış ve 12.11’e gönderilmiştir. Beyaz biber ve uzun biber Piper cinsi, Jamaika biberi Pimenta cinsi olarak 09.04’tedir; biber toz ve döküntüleri de bu pozisyonda sayılmıştır.",
 "Fasıl 9 Not 2; 09.04 Açıklama Notu.")
S["O4"] = Q(T_OL,
 "Aşağıdakilerden hangisi Tarife Cetvelinin 9. faslında <b>yer almaz</b>?",
 "Taze kişniş otu",
 ["Kişniş tohumu", "Dere otu tohumu", "Çemen otu tohumu", "Defne yaprağı"], "C",
 "Fasıl 9 Genel Açıklamaları maydanoz, tere, tarhun, kişniş otu, dere otu gibi Fasıl 7 sebzelerini fasıl dışında bırakır. Kişniş tohumu 09.09’da; dere otu tohumu, çemen otu tohumu ve defne yaprağı 09.10’dadır. Tuzak, aynı bitkinin tohumu ile yaprağını karıştırmaktır.",
 "Fasıl 9 Genel Açıklamalar; 09.09 ve 09.10 Açıklama Notları.")
# ---- Farklı/aynı
S["F1"] = Q(T_FA,
 "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
 "Vanilin",
 ["Bütün halde vanilya meyvesi", "Öğütülmüş tarçın", "Karanfil çiçekleri", "Kakule"], "A",
 "Vanilin (vanilyanın hoş kokulu özü) 09.05’ten hariç tutulmuş ve Fasıl 29’a (29.12) gönderilmiştir. Vanilya 09.05, tarçın 09.06, karanfil 09.07, kakule 09.08 ile Fasıl 9’dadır. Vanilya şekeri (17.01 veya 17.02) ve vanilya oleorezini (13.02) de fasıl dışıdır.",
 "09.05 Açıklama Notu.")
S["F2"] = Q(T_FA,
 "Aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
 "Dere otu tohumu",
 ["Anason tohumu", "Rezene tohumu", "Kimyon tohumu", "Karaman kimyonu tohumu"], "E",
 "Anason, rezene, kimyon ve karaman kimyonu tohumları 09.09 pozisyon metninde sayılmıştır. Dere otu tohumu ise 09.09’da sayılmadığından 09.10 Açıklama Notu uyarınca “diğer baharat” olarak 09.10’da yer alır (çemen otu tohumu da öyle). Tuzak, bütün “tohum” baharatlarının 09.09’da olduğunu sanmaktır.",
 "09.09 pozisyon metni; 09.10 Açıklama Notu.")
S["F3"] = Q(T_FA,
 "Bitkisel çay yapımında kullanılmak üzere ayrı ayrı paketlenmiş aşağıdaki ürünlerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
 "Anason tohumu",
 ["Adaçayı yaprağı", "Ihlamur çiçeği", "Nane yaprağı", "Papatya çiçeği"], "B",
 "09.09 Açıklama Notuna göre bu pozisyondaki tohumlar, özellikle anason, bitkisel çay veya içecek imalinde kullanılsalar bile 09.09’da kalır. Adaçayı, ıhlamur, nane ve papatya ise esas olarak eczacılıkta kullanılan bitkiler olarak 12.11’dedir; tek türden oluşan bitkisel “çay” paketleri de bu pozisyonda yer alır.",
 "09.09 Açıklama Notu; Fasıl 12 Not 4; 12.11 Açıklama Notu.")
S["F4"] = Q(T_FA,
 "Aşağıdaki ikililerden hangisinde yer alan ürünler aynı tarife pozisyonunda sınıflandırılır?",
 "Zencefil – Zerdeçal",
 ["Karabiber – Kakule", "Tarçın – Karanfil", "Kahve – Paraguay çayı", "Safran – Vanilya"], "D",
 "Zencefil ve zerdeçal (curcuma) 09.10 pozisyon metninde birlikte sayılmıştır. Karabiber 09.04 / kakule 09.08, tarçın 09.06 / karanfil 09.07, kahve 09.01 / paraguay çayı 09.03, safran 09.10 / vanilya 09.05 pozisyonlarındadır.",
 "09.01–09.10 pozisyon metinleri.")
# ---- Fasıl notu
S["N1"] = Q(T_NO,
 "Tarife Cetveline göre, öğütülmüş karabiber ile öğütülmüş küçük Hindistan cevizinden oluşan bir baharat karışımı hangi pozisyonda sınıflandırılır?",
 "09.10", ["09.04", "09.08", "21.03", "21.06"], "C",
 "Fasıl 9 Not 1(b)’ye göre farklı pozisyonlara giren 09.04–09.10 ürünlerinin karışımları 09.10’da sınıflandırılır; karabiber 09.04’e, küçük Hindistan cevizi 09.08’e girdiğinden karışım 09.10’dadır. Karışım baharat olma özelliğini koruduğu için Fasıl 21’e (21.03 çeşni karışımı, 21.06 diğer müstahzar) gitmez. Bileşenlerden birinin pozisyonu seçilmez.",
 "Fasıl 9 Not 1(b); 09.10 Açıklama Notu.")
S["N2"] = Q(T_NO,
 "Tarife Cetveline göre, öğütülmüş karabiber ile acısı az kırmızı toz biberin (paprika) karışımı hangi pozisyonda sınıflandırılır?",
 "09.04", ["09.10", "21.03", "07.12", "09.08"], "A",
 "Karabiber (Piper cinsi) ve paprika (Capsicum cinsi) aynı pozisyona, 09.04’e girer. Fasıl 9 Not 1(a)’ya göre aynı pozisyona giren ürünlerin karışımları o pozisyonda sınıflandırılır. 09.10 yalnızca farklı pozisyonlardaki ürünlerin karışımı için geçerlidir; sorunun tuzağı budur.",
 "Fasıl 9 Not 1(a); 09.04 Açıklama Notu.")
S["N3"] = Q(T_NO,
 "Fasıl 9 notlarına göre, 09.04–09.10 pozisyonlarındaki ürünlere başka maddeler katılması sonucu esas özelliğini kaybetmiş, lezzet veya çeşni verici yapıdaki karışımlar hangi pozisyonda sınıflandırılır?",
 "21.03", ["09.10", "21.06", "21.04", "19.01"], "E",
 "Fasıl 9 Not 1’e göre katılan maddeler esas özelliği değiştirmedikçe sınıflandırmayı etkilemez; aksi halde karışım fasıl dışına çıkar ve lezzet veya çeşni verici yapıdaki karışımlar 21.03’te sınıflandırılır. 09.10 yalnızca baharat olma özelliğini koruyan karışımlar içindir. 21.06 ise içecek aromalandırmaya mahsus bitki karışımlarında asli karakter baharatlardan gelmediğinde söz konusudur.",
 "Fasıl 9 Not 1; Fasıl 9 Genel Açıklamalar.")
S["N4"] = Q(T_NO,
 "09.06 Açıklama Notuna göre tarçın ağacı çiçekleri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 "Kurutulup elekten geçirilmiş, uzunluğu normalde 1 cm’yi geçmeyen sopa şeklindeki çiçeklerdir; 09.06’da yer alır.",
 ["Kurutulup elekten geçirilmiş, uzunluğu normalde 3 cm’yi geçmeyen çiçeklerdir; 09.06’da yer alır.",
  "Tarçın ağacının kurutulmuş çiçekleri karanfil ile birlikte 09.07’de yer alır.",
  "Kurutulmuş tarçın ağacı çiçekleri süs amaçlı sayıldığından 06.03’te yer alır.",
  "Tarçın ağacının çiçekleri 12.11’de, yalnızca iç kabukları 09.06’da yer alır."], "B",
 "09.06 Açıklama Notuna göre tarçın ağacı çiçeği; kurutulmuş ve elekten geçirilmiş, uzunluğu normalde 1 cm’yi geçmeyen sopa şeklindeki çiçeklerdir ve dövüldükten sonra tarçınla karıştırılır. Tarçın meyvesi ve tarçın döküntüleri (chips) de 09.06’dadır. 12.11’e giden karanfil kabuk ve yaprağıyla karıştırılmamalıdır.",
 "09.06 pozisyon metni ve Açıklama Notu.")
# ---- GYK
S["G1"] = Q(T_GY,
 "Fasıl 9 Not 1(b) uyarınca, farklı pozisyonlara giren baharatlardan oluşan bir karışımın 09.10’da sınıflandırılması hangi Genel Yorum Kuralına dayanır?",
 "GYK 1 – karışım fasıl notunda belirtildiği için not hükmüne göre",
 ["GYK 3(a) – eşyayı en özel şekilde tanımlayan pozisyona göre",
  "GYK 3(b) – karışıma esas niteliğini veren baharata göre",
  "GYK 3(c) – geçerli pozisyonların numara sırasına göre sonuncusuna göre",
  "GYK 4 – eşyaya en çok benzeyen eşyanın pozisyonuna göre"], "A",
 "GYK 2(b) Açıklama Notuna göre bir bölüm veya fasıl notunda ya da pozisyon metninde belirtilen hazır karışımlar 1 No.lu Kuralda yer alan esaslara göre sınıflandırılır. Fasıl 9 Not 1(b) bu karışımı doğrudan 09.10’a bağladığından GYK 3’e geçilmez. 09.10’un numara olarak son pozisyon olması tesadüftür; 3(c) tuzaktır.",
 "GYK 1; GYK 2(b) Açıklama Notu (X); Fasıl 9 Not 1(b).")
S["G2"] = Q(T_GY,
 "Perakende satış için, süslü gümüş bir kupanın içine konulmuş siyah çay birlikte gümrüğe sunulmuştur. Bu eşyanın sınıflandırılmasıyla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
 "Kupa GYK 5 kapsamında değerlendirilmez; çay ve kupa kendi pozisyonlarında ayrı ayrı sınıflandırılır.",
 ["Kupa GYK 5(a) uyarınca çay ile birlikte 09.02’de sınıflandırılır.",
  "Kupa GYK 5(b) uyarınca normal ambalaj sayılır ve çay ile birlikte 09.02’de sınıflandırılır.",
  "Eşya GYK 3(b) uyarınca takım sayılır ve kupanın pozisyonunda sınıflandırılır.",
  "Eşya GYK 3(c) uyarınca numara sırasına göre sonuncu pozisyonda sınıflandırılır."], "C",
 "GYK 5(a) Açıklama Notu, çay konulan gümüş kupaları bu kuralın kapsamı dışında sayar. Kupa açıkça sürekli kullanıma elverişli olduğundan GYK 5(b)’deki ambalaj hükmü de uygulanmaz. GYK 3(b) Açıklama Notundaki hazır kahve ile seramik fincan örneğinde olduğu gibi takım da oluşmaz; çay 09.02’de, kupa kendi pozisyonunda sınıflandırılır.",
 "GYK 5(a) Açıklama Notu (III); GYK 5(b); GYK 3(b) Açıklama Notu (X).")
# ---- Eşleştirme / Boşluk
S["B1"] = Q(T_EB,
 "Fasıl 9’a göre; Thea cinsi bitkilerden elde edilen çaylar ……, Holly familyasına dahil ağaçların kurutulmuş yapraklarından oluşan paraguay çayı ……, kahve hülasası ise …… pozisyonunda yer alır. Boşluklara sırasıyla gelmesi gerekenler hangi seçenekte doğru verilmiştir?",
 "09.02 – 09.03 – 21.01",
 ["09.03 – 09.02 – 21.01", "09.02 – 12.11 – 09.01", "09.02 – 09.03 – 09.01", "21.01 – 09.03 – 09.01"], "D",
 "Thea (Camellia) cinsi çaylar 09.02’de, paraguay çayı (maté) 09.03’te yer alır. Kahve hülasası, esansı ve konsantreleri (instant kahve) 09.01’den hariç tutulmuş ve 21.01’e gönderilmiştir. 09.01 yalnızca çiğ, kavrulmuş veya kafeini alınmış kahveyi ve kahve içeren ikameleri kapsar.",
 "09.01, 09.02, 09.03 Açıklama Notları.")
S["B2"] = Q(T_EB,
 "Aşağıdaki ürünleri sınıflandırıldıkları pozisyonlarla eşleştiriniz. I. Safran  II. Küçük Hindistan cevizi  III. Çin anasonu (yıldız anason)  IV. Jamaika biberi — a. 09.04  b. 09.08  c. 09.09  d. 09.10",
 "I-d, II-b, III-c, IV-a",
 ["I-c, II-b, III-d, IV-a", "I-d, II-a, III-c, IV-b", "I-b, II-d, III-c, IV-a", "I-d, II-b, III-a, IV-c"], "E",
 "Safran 09.10’da, küçük Hindistan cevizi 09.08’de, Çin anasonu (anasonun yıldız şeklindeki türü) 09.09’da, Pimenta cinsi Jamaika biberi ise 09.04’te yer alır. Jamaika biberi, Capsicum ile birlikte 09.04 pozisyon metninde sayılmıştır; “diğer baharat” olarak 09.10’a gitmez.",
 "09.04, 09.08, 09.09, 09.10 pozisyon metinleri ve Açıklama Notları.")
# ---- Çoktan-çoğa
S["C1"] = Q(T_CC,
 "Aşağıdakilerden hangileri 09.01 pozisyonunda sınıflandırılır? I. Kahvenin kabuk ve kapçıkları  II. Ağırlıkça %10 kahve içeren kahve yerine kullanılan madde  III. Kahve mumu  IV. Hiç kahve içermeyen kavrulmuş kahve ikamesi",
 "I ve II", ["I ve III", "II ve IV", "I, II ve IV", "I, III ve IV"], "A",
 "09.01, kahvenin kabuk ve kapçıklarını ve içinde herhangi bir oranda kahve bulunan kahve yerine kullanılan maddeleri kapsar (I, II). Kahve mumu 15.21’de (III), kahve içermeyen kavrulmuş kahve yerine kullanılan maddeler 21.01’de (IV) yer alır. Ölçüt, ikamenin içinde kahve bulunup bulunmamasıdır; oran önemli değildir.",
 "09.01 pozisyon metni ve Açıklama Notu.")
S["C2"] = Q(T_CC,
 "Fasıl 9 Genel Açıklamalarına göre, doğrudan meşrubata tat vermek veya meşrubat hülasası hazırlamak için kullanılan bitki karışımlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Asli karakteri 09.04–09.10 pozisyonlarından birindeki tek bir tür veriyorsa duruma göre o pozisyonda yer alır.  II. Asli karakteri 09.04–09.10 pozisyonlarındaki iki veya daha fazla türün karışımı veriyorsa 09.10’da yer alır.  III. Asli karakteri bu türler veya karışımları vermiyorsa 21.06’da yer alır.  IV. Karışımda Fasıl 7 veya Fasıl 12 bitkisi bulunuyorsa her durumda 12.11’de yer alır.",
 "I, II ve III", ["I ve II", "I ve IV", "II, III ve IV", "I, III ve IV"], "C",
 "Genel Açıklamalar, Fasıl 7, 9, 11, 12 gibi çeşitli fasıllara giren bitki parçalarından oluşan içecek aromalandırma karışımlarını asli karaktere göre ayırır: tek bir 09.04–09.10 türü veriyorsa o pozisyon (I), bu türlerin karışımı veriyorsa 09.10 (II), hiçbiri vermiyorsa 21.06 (III). Fasıl 7 veya 12 bitkisi bulunması karışımı kendiliğinden 12.11’e götürmez (IV yanlış).",
 "Fasıl 9 Genel Açıklamalar.")
# ---- Senaryo
S["S1"] = Q(T_SE,
 "Karanfil ağacının olgunlaşmadan toplanıp güneşte kurutulmuş çiçek tomurcukları, sapları ile birlikte öğütülmüş; aromasını korumak amacıyla içine küçük miktarda antioksidan katılmış ve 1 kg’lık torbalarda sunulmuştur. Eşya hangi pozisyonda sınıflandırılır?",
 "09.07", ["09.10", "12.11", "21.03", "33.01"], "D",
 "Karanfil (çiçekler) ve sapları 09.07’de yer alır; öğütülmüş olması pozisyonu değiştirmez. Fasıl 9 Genel Açıklamalarına göre ürünün korunması ve aroma gücünün sürmesi için küçük miktarlarda katılan tuz veya kimyasal antioksidanlar esas özelliği değiştirmediğinden sınıflandırmayı etkilemez; bu nedenle 21.03’e gitmez. 12.11 yalnız karanfil kabuk ve yaprakları içindir; 33.01 uçucu yağların pozisyonudur.",
 "09.07 Açıklama Notu; Fasıl 9 Not 1; Fasıl 9 Genel Açıklamalar.")
S["S2"] = Q(T_SE,
 "Kahve yerine içecek hazırlamakta kullanılan, ağırlıkça %70 kavrulmuş hindiba kökü ve %30 kavrulmuş kahveden oluşan öğütülmüş bir karışım perakende ambalajda ithal edilmektedir. Eşya hangi pozisyonda sınıflandırılır?",
 "09.01", ["21.01", "12.12", "21.06", "09.10"], "B",
 "09.01 pozisyon metni, içinde herhangi bir oranda kahve bulunan kahve yerine kullanılan maddeleri kapsar; %30 kahve içeren karışım bu tanıma girer. Kahve içermeyen kavrulmuş hindiba ve diğer kavrulmuş kahve ikameleri 21.01’dedir. Kavrulmamış hindiba kökü ise 12.12’de yer alır; burada kök kavrulmuştur ve karışım kahve içerir.",
 "09.01 pozisyon metni ve Açıklama Notu; 12.12 Açıklama Notu.")

SIRA = ["E1", "O1", "F1", "N1", "E2", "C1", "O2", "F2", "B1", "E3", "G1", "S1", "N2",
        "O3", "E4", "F3", "N3", "C2", "B2", "O4", "F4", "E5", "G2", "N4", "S2"]
d["sorular"] = sirala(S, SIRA)
yaz(9, d)
