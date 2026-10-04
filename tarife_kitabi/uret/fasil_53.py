import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_53_58 import S, SX, yaz  # noqa: E402

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
 "fasil": 53,
 "baslik": "Dokumaya elverişli diğer bitkisel lifler; kağıt ipliği ve kağıt ipliğinden dokunmuş mensucat",
 "bolum": "XI",
 "oz": {
  "vurgu": "Fasıl 53, pamuk dışındaki dokumaya elverişli bitkisel lifleri ve kağıt ipliğini ham lif → iplik → dokunmuş mensucat sırasıyla izler. İki soru sorulur: Lif hangi bitki grubundan (keten, kendir, jüt ve diğer iç kabuk lifleri, diğer bitkisel lifler)? Eşya hangi aşamada (lif-döküntü, iplik, mensucat)? Fasıl notu yoktur; Bölüm XI notları (karışım ve sicim eşikleri) belirleyicidir.",
  "maddeler": [
   "Lif pozisyonları: keten 53.01, kendir (yalnız Cannabis sativa L.) 53.02, jüt ve diğer iç kabuk lifleri 53.03, koko-abaka-rami-sisal ve diğerleri 53.05; kıtık ve döküntüler dahil, iplik haline getirilmemiş olmak şartıyla.",
   "İplik pozisyonları: keten 53.06, jüt ve iç kabuk lifleri 53.07, kendir-koko-diğer bitkisel lifler ve kağıt ipliği 53.08. Sicim, ip, halat eşiğini aşan iplik 56.07’ye gider (Bölüm XI Not 3).",
   "Dokunmuş mensucat: keten 53.09, jüt ve iç kabuk lifleri 53.10, diğer bitkisel lifler ve kağıt ipliği 53.11.",
   "Ağartma, boyama, kotonizasyon lif pozisyonunu değiştirmez; pamuk Fasıl 52’de, linter ve işlenmemiş bazı bitkisel maddeler Fasıl 14’te kalır."
  ]
 },
 "karar_tablosu": {
  "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
  "satirlar": [
   ["1", "Pamuk, linter veya dokumaya hazırlık işlemi görmemiş Fasıl 14 maddesi mi?", "Pamuk <b>Fasıl 52</b> · linter, süpürge sapı vb. <b>Fasıl 14</b>"],
   ["2", "İki veya daha fazla lifin karışımı mı?", "Bölüm XI Not 2: önce fasıl (keten + jüt tek madde), sonra fasıl içinde en ağır lif; eşitlikte numara sırasına göre son pozisyon"],
   ["3", "Hazır eşya mı? (Bölüm XI Not 7)", "<b>56–63. fasıllar</b> (Bölüm XI Not 8)"],
   ["4", "Sicim, ip, halat tanımına giren iplik mi? (cilalı keten-kendir ≥ 1.429 dtex; cilasız keten-kendir veya diğer bitkisel lif &gt; 20.000 dtex; üç ve fazla katlı koko; metal takviyeli)", "<b>56.07</b>"],
   ["5", "Metal tel/şeritle birleştirilmiş veya metalle kaplanmış (metalize) iplik mi?", "<b>56.05</b>"],
   ["6", "İplik haline getirilmemiş lif, kıtık, döküntü mü?", "Keten <b>53.01</b> · kendir <b>53.02</b> · jüt ve iç kabuk lifleri <b>53.03</b> · koko, abaka, rami, sisal vb. <b>53.05</b>"],
   ["7", "İplik mi? (kağıt ipliği dahil)", "Keten <b>53.06</b> · jüt ve iç kabuk lifleri <b>53.07</b> · kendir, koko, diğerleri, kağıt ipliği <b>53.08</b>"],
   ["8", "Dokunmuş mensucat mı?", "Keten <b>53.09</b> · jüt ve iç kabuk lifleri <b>53.10</b> · diğer bitkisel lifler ve kağıt ipliği <b>53.11</b>"]
  ],
  "dipnot": "* Kağıt şeritlerinin örülmesiyle elde edilen mensucat 46.01’de, uzunlamasına katlanmış kağıt şeritler Fasıl 48’de, paçavralar ile ip ve halat hurdaları Fasıl 63’te yer alır."
 },
 "pozisyon_haritasi": [
  ["53.01", "Keten (iplik değil); kıtık ve döküntüleri", "Ham, ıslatılmış, kırılmış, taranmış; fitil dahil", "Taranmış keten şeridi, keten kıtığı"],
  ["53.02", "Kendir; kıtık ve döküntüleri", "Yalnız Cannabis sativa L.", "Kabuğu çıkarılmış kendir lifi"],
  ["53.03", "Jüt ve diğer iç kabuk lifleri", "Çift çenekli bitki gövdesi; keten, kendir, rami hariç", "Jüt, kenaf, ısırgan otu lifi"],
  ["53.04", "Kullanılmayan pozisyon numarası", "Metinde [53.04] olarak gösterilir", "—"],
  ["53.05", "Koko, abaka, rami ve d.y.b. bitkisel lifler", "Tek çenekli bitki lifleri + rami; daha kaba", "Sisal, koko lifi, Manila kendiri, rami"],
  ["53.06", "Keten iplikleri", "Perakende olsun olmasın", "Tek kat keten ipliği"],
  ["53.07", "Jüt ve iç kabuk lifi iplikleri", "53.03 liflerinden", "Jüt ipliği"],
  ["53.08", "Diğer bitkisel lif iplikleri; kağıt ipliği", "Kendir, koko, kapok, istle; kağıt", "Kendir ipliği, iki katlı koko ipliği"],
  ["53.09", "Ketenden dokunmuş mensucat", "%85 ayrımı alt pozisyonda", "Keten çarşaflık, keten yelken bezi"],
  ["53.10", "Jüt ve iç kabuk lifi mensucatı", "Çuval, ambalaj bezi", "Çuval imaline mahsus jüt bez"],
  ["53.11", "Diğer bitkisel lif ve kağıt ipliği mensucatı", "53.08 ipliklerinden dokunmuş", "Koko mensucat, kağıt ipliği mensucatı"]
 ],
 "notlar": [
  ["Fasıl 53", "Fasıl notu yoktur. Sınıflandırma pozisyon metinleri, Bölüm XI notları ve Açıklama Notlarıyla yapılır."],
  ["Bölüm XI Not 1(c)", "14. fasıldaki linter pamuğu ve diğer bitkisel maddeler Bölüm XI’e dahil değildir."],
  ["Bölüm XI Not 2(A)", "İki veya daha fazla dokumaya elverişli maddeden karışım eşya, ağırlıkça üstün gelen madde esas alınarak sınıflandırılır. Hiçbiri üstün gelmezse, her biri geçerli olabilecek pozisyonların numara sırasına göre sonuncusunda sınıflandırılır."],
  ["Bölüm XI Not 2(B)(b) ve (d)", "Önce uygun fasıl, sonra fasıl içindeki pozisyon seçilir; o fasılda sınıflandırılmayan madde dikkate alınmaz. Bir fasıl farklı dokumaya elverişli maddelere atıf yapıyorsa bunlar tek madde sayılır. Açıklama Notu örneği: %35 keten + %25 jüt + %40 pamuk → keten ve jüt toplamıyla Fasıl 53, keten jütten ağır → 53.09."],
  ["Bölüm XI Not 3(A)", "Sicim, ip ve halat sayılan iplikler (Fasıl 53 açısından): keten veya kendirden cilalanmış/parlatılmış 1.429 desiteks veya daha fazla, cilalanmamış 20.000 desiteksten fazla; üç veya daha fazla katlı koko iplikleri; diğer bitkisel liflerden 20.000 desiteksten fazla; metal iplikle takviye edilmiş olanlar → 56.07."],
  ["Bölüm XI Not 3(B)(a)", "Kağıt iplikleri (metal iplikle takviye edilenler hariç) bu eşiklere tabi değildir; sicim, kordon, ip veya halat şeklinde olsa da 53.08’de kalır. Örülmüş veya metal takviyeli kağıt ipi 56.07’dedir."],
  ["Bölüm XI Not 7–8", "Hazır eşya (kare veya dikdörtgen dışında kesilmiş, kenarı bastırılmış, dikilerek birleştirilmiş vb.) 50–55. fasıllara girmez; 56–63. fasıllarda yer alır."],
  ["53.01 Açıklama Notu", "Ham (keten samanı), suda ıslatılmış, kırılmış, kabuğu çıkarılmış, kotonize, taranmış keten; şerit ve hafif bükümlü fitil hâlinde olsa da iplik sayılmaz. Kırılmış odunsu parçalar 44.01; Hint keteni (Abroma augusta) 53.03; Yeni Zelanda keteni (Phormium tenax) 53.05."],
  ["53.02 Açıklama Notu", "Yalnız Cannabis sativa L. Gambo/Ambari, Rosella, Hint (Sunn) kendiri ve Çin jütü 53.03; Manila kendiri (abaka), Haiti, Mauritius ve Yeni Zelanda kendiri 53.05; Tampiko kendiri (istle) 14.04 veya 53.05. Kendir ipliği 53.08; kendir paçavra ve halat hurdaları Fasıl 63."],
  ["53.03 Açıklama Notu", "Çift çenekli bitkilerin gövdelerinden lifler (keten, kendir ve rami hariç): jüt, kenaf, abutilon, katırtırnağı, urena, ısırgan otu vb. Bu lifler 53.05 liflerinden daha yumuşak ve incedir. Süpürge sapları 14.04; tıbbi amaçlı perakende kıtık 30.05."],
  ["53.05 Açıklama Notu", "Tek çenekli bitkilerden lifler (koko, abaka, sisal, halfa, aloe, ananas, yukka vb.) ile rami. Fasıl 14 lifleri (kapok, istle) ve turba lifleri ancak dokumaya elverişli madde olarak kullanılacağını gösteren işlem (ezme, karde, tarama) görmüşse buraya girer; aksi halde Fasıl 14 veya 27.03. İşlem görmemiş halfa yaprakları Fasıl 14."],
  ["53.06 / 53.08 Açıklama Notu", "Perakende satışa hazırlanmış olsun olmasın iplikler bu pozisyonlarda kalır; herhangi bir oranda metal iplikle birleştirilmiş metalize iplikler 56.05’tedir."],
  ["53.08 / 53.11 Açıklama Notu", "Uzunlamasına katlanmış kağıt şeritler Fasıl 48; metalle kaplanmış kağıt ipliği 56.05; kağıt şeritlerinin örülmesiyle elde edilen mensucat 46.01."]
 ],
 "sinir_komsulari": [
  ["Pamuk lifi, pamuk ipliği, pamuk mensucat", "Fasıl 52", "Pamuk Fasıl 53’ün konusu değildir"],
  ["Linter pamuğu", "Fasıl 14", "Bölüm XI Not 1(c)"],
  ["Süpürge sapları; işlenmemiş istle, kapok, halfa yaprağı", "14.04 / Fasıl 14", "Dokumaya hazırlık işlemi görmemiş"],
  ["Su kamışı (Typha) tohum tüyleri (dolgu)", "14.04", "53.05 Açıklama Notu hariç tutması"],
  ["Keten saplarından kalan kırılmış odunsu parçalar", "44.01", "53.01 Açıklama Notu"],
  ["İşlem görmemiş turba lifleri", "27.03", "Dokuma amacını gösteren işlem yok"],
  ["Tıbbi amaçlı perakende kıtık; perakende bandaj", "30.05", "Fasıl 30 eşyası (Bölüm XI Not 1(e))"],
  ["Odun selülozundan viskoz lifi", "Fasıl 54 / 55", "Suni liftir (Fasıl 54 Not 1(b)), bitkisel lif değil"],
  ["Sicim eşiğini aşan keten, kendir, jüt ipliği; üç katlı koko ipliği", "56.07", "Bölüm XI Not 3"],
  ["Metalize keten veya kağıt ipliği", "56.05", "Metalle birleştirilmiş/kaplanmış iplik"],
  ["Kağıt şeritlerinden örülmüş mensucat", "46.01", "53.11 Açıklama Notu"],
  ["Uzunlamasına katlanmış kağıt şerit", "Fasıl 48", "İplik değildir"],
  ["Kendir paçavraları, ip ve halat hurdaları", "Fasıl 63", "53.02 ve 53.03 hariç tutmaları"]
 ],
 "tuzaklar": [
  "<b>Her “kendir” 53.02 değildir.</b> 53.02 yalnız Cannabis sativa L.’yi kapsar; Manila kendiri (abaka) 53.05’te, Hint/Sunn ve Gambo kendiri 53.03’tedir.",
  "<b>Her “keten” 53.01 değildir.</b> Hint keteni (Abroma augusta) 53.03’te, Yeni Zelanda keteni (Phormium tenax) 53.05’tedir.",
  "<b>Rami çift çeneklidir ama 53.05’tedir.</b> 53.03 çift çenekli gövde liflerini kapsar, ancak keten, kendir ve rami açıkça hariçtir.",
  "<b>Hafif bükümlü fitil iplik değildir.</b> Taranmış keten fitili hafif bükümlü olsa da 53.01’de kalır; 53.06’daki tek katlı iplikle karıştırılmamalıdır.",
  "<b>Kendir lifi 53.02, kendir ipliği 53.08.</b> Kendirin ayrı iplik pozisyonu yoktur; keten (53.06) ve jüt (53.07) dışındaki bitkisel lif iplikleri 53.08’de toplanır, mensucatı 53.11’dedir.",
  "<b>Kalınlık ipliği sicime çevirir.</b> Cilalı keten veya kendir ipliği 1.429 desiteks ve üzeri, cilasız 20.000 desiteksi aşarsa 56.07; koko ipliğinde ölçüt kat sayısıdır: üç ve fazlası 56.07.",
  "<b>Kağıt ipliği sicim eşiğine takılmaz.</b> Sicim görünümündeki kağıt ipliği de 53.08’dir; yalnız örülmüş veya metal takviyeli olanlar 56.07’ye gider.",
  "<b>Fasıl 14 lifleri işlemle 53.05’e geçer.</b> Kapok, istle, halfa ancak ezme, karde veya tarama gibi dokumaya hazırlık işlemi görmüşse 53.05’e girer.",
  "<b>Karışımda önce fasıl seçilir.</b> Keten ve jüt Fasıl 53 içinde tek madde sayılır; toplamları pamuktan fazlaysa eşya Fasıl 53’e girer, sonra fasıl içinde ağır olan lif pozisyonu belirler."
 ],
 "hafiza": {
  "kanca": "KE–KEN–JÜT–DİĞER: lif 01-02-03-05 · iplik 06-07-08 · kumaş 09-10-11",
  "aciklama": "Lifte dört kutu vardır: <b>ke</b>ten 53.01, <b>ken</b>dir 53.02, <b>jüt</b> 53.03, <b>diğer</b>leri 53.05 (53.04 boş). İplik ve kumaşta kendir “diğerleri” kutusuna düşer: keten 06/09, jüt 07/10, kendir-koko-kağıt 08/11. Kendir, lifte kendi pozisyonu olup iplikte “diğer”e karışan tek liftir."
 },
 "sinav_odagi": [
  "Bu fasıl çıkmış sorularda daha çok seçeneklerde ve çeldirici olarak yer almıştır; doğrudan Fasıl 53 pozisyonu soran soru azdır.",
  "“Hangisi yanlıştır” kalıbında fasıl–eşya eşleştirmesi: pamuğun 53. fasılda değil 52. fasılda yer aldığı.",
  "Fasıl 52 sorularında keten döküntülerinin (Fasıl 53) ve viskoz ipeğinin (Fasıl 54) çeldirici olarak kullanılması; lif cinsine göre fasıl ayrımı.",
  "Dokumaya elverişli maddelerin Bölüm XI’de (50–63. fasıllar) toplandığı ve 50–55. fasılların madde esasına göre ayrıldığı.",
  "Karışık dokumaya elverişli mensucatın Bölüm XI Not 2 ile, dolayısıyla GYK 1’e göre sınıflandırıldığı."
 ],
 "cikmis_ornekler": [
  {
   "soru": "Tarife Cetveli’ne göre aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
   "secenekler": ["Hububat 10. fasılda yer alır.", "Gübre 31. fasılda yer alır.", "Pamuk 53. fasılda yer alır.", "Cam 70. fasılda yer alır.", "Saat 91. fasılda yer alır."],
   "cevap": "C",
   "aciklama": "Pamuk Fasıl 52’nin konusudur. Fasıl 53 pamuk dışındaki dokumaya elverişli bitkisel lifleri (keten, kendir, jüt, sisal vb.) ve kağıt ipliğini kapsar."
  },
  {
   "soru": "Tarife Cetveli’nin 52. faslında yer alan bir eşya için aşağıdakilerden hangisi söylenebilir?",
   "secenekler": ["Eşya TGTC 10. Bölüm kapsamındadır.", "Viskoz ipeği bu fasılda yer alır.", "Sentetik ve suni filamentleri içerir.", "Keten döküntüleri bu fasıl kapsamındadır.", "Pamuk ipliği bu fasılda yer alır."],
   "cevap": "E",
   "aciklama": "Pamuk ipliği Fasıl 52’dedir. Keten döküntüleri 53.01’de, viskoz ipeği ve sentetik-suni filamentler Fasıl 54’te yer alır; tekstil eşyası Bölüm XI’dedir."
  }
 ],
 "ozet": [
  "Fasıl 53 = pamuk dışı bitkisel lifler + kağıt ipliği; sıra lif → iplik → dokunmuş mensucat.",
  "Lif: keten 53.01, kendir (yalnız Cannabis sativa) 53.02, jüt ve iç kabuk lifleri 53.03, koko-abaka-rami-sisal 53.05.",
  "İplik: keten 53.06, jüt 53.07, kendir-koko-diğerleri-kağıt 53.08. Mensucat: keten 53.09, jüt 53.10, diğerleri-kağıt 53.11.",
  "Kalın iplik sicimdir (Bölüm XI Not 3) → 56.07; kağıt ipliği bu eşiğe tabi değildir.",
  "Karışımda önce fasıl (keten + jüt tek madde), sonra fasıl içinde en ağır lif; eşitlikte numara sırasına göre son pozisyon.",
  "Fasıl 14 lifleri yalnız dokumaya hazırlık işlemi görürse 53.05’e girer."
 ],
 "sorular": [
  # --- Eşya → 4'lü pozisyon (5)
  S("Tarife Cetveline göre, kabukları çıkarılmış ve taranarak şerit haline getirilmiş, ancak henüz bükülerek iplik haline getirilmemiş Cannabis sativa L. lifleri hangi pozisyonda sınıflandırılır?",
    "53.02", ["53.01", "53.03", "53.05", "53.08"], "B", E4,
    "53.02 yalnızca Cannabis sativa L. kendirini kapsar; ham, suda ıslatılmış, kabuğu çıkarılmış ve iplik imali için taranmış (şerit veya fitil halinde) lifler buradadır. Bükülerek iplik haline getirilmiş kendir 53.08’e gider. 53.01 keten, 53.03 jüt ve diğer iç kabuk lifleri, 53.05 tek çenekli bitki lifleri içindir.",
    "53.02 Açıklama Notu."),
  S("Tarife Cetveline göre, Hindistan cevizinin lifli dış zarfından elde edilmiş ve iplik imali için taranmış lifler hangi pozisyonda yer alır?",
    "53.05", ["53.03", "53.08", "14.04", "53.11"], "D", E4,
    "Hindistan cevizi (koko) lifleri 53.05’te sayılan lifler arasındadır; ham olması veya iplik imali için taranmış olması sonucu değiştirmez. 53.03 çift çenekli bitki gövdelerinden elde edilen iç kabuk lifleri, 53.08 koko ipliği, 53.11 dokunmuş mensucat içindir. Fasıl 14 ise dokumaya hazırlık işlemi görmemiş bazı bitkisel lifleri (kapok gibi) kapsar.",
    "53.05 Açıklama Notu."),
  S("Tarife Cetveline göre, jüt liflerinden bükülerek elde edilmiş, sicim, kordon, ip veya halat tanımına girmeyen iki katlı iplik hangi pozisyondadır?",
    "53.07", ["53.03", "53.08", "56.07", "53.10"], "A", E4,
    "53.07, 53.03 pozisyonundaki jüt ve diğer bitki iç kabuğu liflerinden elde edilen tek veya çok katlı iplikleri kapsar. Jüt lifi 53.03’te, jüt mensucat 53.10’dadır; 53.08 kendir, koko ve diğer bitkisel lif iplikleri içindir. İplik sicim tanımına girmediğinden 56.07 söz konusu değildir.",
    "53.07 Açıklama Notu; Bölüm XI Not 3."),
  S("Tarife Cetveline göre, nemlendirilmiş kağıt şeritlerinin uzunlamasına bükülmesiyle elde edilmiş, perakende satış için makaraya sarılmış tek katlı kağıt ipliği hangi pozisyondadır?",
    "53.08", ["53.11", "56.07", "46.01", "56.05"], "E", E4,
    "Kağıt iplikleri, perakende satış için hazırlanmış olsun olmasın 53.08’de yer alır. Bu ipliklerden dokunmuş mensucat 53.11’de, kağıt şeritlerinin örülmesiyle elde edilen mensucat 46.01’de, metalle kaplanmış kağıt ipliği 56.05’te, örülmüş veya metal takviyeli kağıt ipi 56.07’dedir.",
    "53.08 Açıklama Notu (B); 53.11 Açıklama Notu."),
  S("Tarife Cetveline göre, ağırlık itibariyle %80 keten ve %20 pamuk içeren, ağartılmış, parça halinde (hazır eşya niteliğinde olmayan) dokunmuş mensucat hangi pozisyondadır?",
    "53.09", ["53.06", "53.10", "53.11", "52.12"], "C", E4,
    "Keten ağırlıkça üstün geldiğinden eşya ketenden dokunmuş mensucat olarak 53.09’dadır; %85 eşiği yalnızca alt pozisyon ayrımıdır, pozisyonu değiştirmez. 53.06 keten ipliği, 53.10 jüt mensucat, 53.11 diğer bitkisel lif mensucatıdır. Pamuk üstün olmadığı için 52.12 söz konusu olmaz.",
    "Bölüm XI Not 2(A); 53.09 pozisyon metni ve Açıklama Notu."),
  # --- Olumsuz teşhis (4)
  S("Aşağıdakilerden hangisi 53.01 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Keten saplarının kabuk çıkarma işleminden kalan kırılmış odunsu parçalar",
    ["Suda ıslatılarak pektik maddelerinden arındırılmış keten",
     "Taranmış ve hafif bükümlü keten fitili",
     "Ağartılmış keten kıtığı",
     "Keten mensucat artıklarının ditilmesiyle elde edilen döküntü lifler"], "A", OT,
    "Kabuk çıkarma işlemlerinden kalan kırılmış odunsu parçalar 53.01’in hariç tuttuğu eşyadır ve 44.01’de yer alır. Suda ıslatılmış keten, hafif bükümlü olsa da iplik sayılmayan taranmış fitil, ağartılmış kıtık ve ditme suretiyle elde edilen döküntüler 53.01’dedir.",
    "53.01 Açıklama Notu."),
  S("Aşağıdaki liflerden hangisi 53.03 pozisyonunda <b>yer almaz</b>?",
    "Yeni Zelanda keteni (Phormium tenax) lifleri",
    ["Kırmızı jüt (Tossa) lifleri", "Hibiskus kendiri (kenaf) lifleri", "Isırgan otu lifleri",
     "Hint keteni (Abroma augusta) lifleri"], "C", OT,
    "Yeni Zelanda keteni (Phormium tenax) 53.05’te sayılan liflerdendir. Jüt, kenaf (Hibiscus cannabinus), ısırgan otu ve adında keten geçse de Abroma augusta (Hint keteni) çift çenekli bitkilerin iç kabuk lifleri olarak 53.03’tedir. Tuzak, isimdeki “keten” veya “kendir” kelimesine göre karar vermektir.",
    "53.03 ve 53.05 Açıklama Notları; 53.01 Açıklama Notu hariç tutmaları."),
  S("Aşağıdakilerden hangisi Tarife Cetvelinin 53. faslında <b>sınıflandırılmaz</b>?",
    "Süpürge yapımında kullanılan, işlenmemiş süpürge sapları",
    ["Ezilip taranarak iplik imaline hazırlanmış kapok lifleri",
     "Kağıt ipliğinden dokunmuş mensucat",
     "Cilalanmamış, 5.000 desiteks kendir ipliği",
     "Soyulup alkalide kaynatılmış rami lifleri"], "E", OT,
    "Süpürge sapları 53.03’ün hariç tuttuğu eşya olup 14.04’te yer alır. Fasıl 14 lifleri (kapok gibi) ancak dokumaya elverişli madde olarak kullanılacağını gösteren ezme, karde, tarama gibi işlemlerle 53.05’e girer; kağıt ipliği mensucatı 53.11’de, sicim eşiğinin altındaki kendir ipliği 53.08’de, rami lifleri 53.05’tedir.",
    "53.03 Açıklama Notu (hariç tutmalar); 53.05 Açıklama Notu."),
  S("Aşağıdaki ipliklerden hangisi 53.08 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Üç katlı Hindistan cevizi (koko) ipliği",
    ["İki katlı Hindistan cevizi (koko) ipliği",
     "Cilalanmamış, 5.000 desiteks kendir ipliği",
     "Örülmemiş ve metalle takviye edilmemiş, sicim görünümünde kağıt ipliği",
     "Dokumaya hazırlanmış kapok liflerinden bükülmüş iplik"], "B", OT,
    "Bölüm XI Not 3(A)(d) uyarınca üç veya daha fazla katlı koko iplikleri “sicim, ip ve halat” sayılır ve 56.07’ye gider; bir veya iki katlı koko ipliği 53.08’de kalır. Cilasız ve 20.000 desiteksi aşmayan kendir ipliği, örülmemiş ve metal takviyesiz kağıt ipliği (Not 3(B)(a)) ve Fasıl 14 liflerinden (kapok) bükülen iplik 53.08’dedir.",
    "Bölüm XI Not 3; 53.08 Açıklama Notu."),
  # --- Farklı/aynı (4)
  S("Aşağıdaki liflerden hangisi diğerlerinden <b>farklı</b> bir pozisyonda sınıflandırılır?",
    "Kenaf (Hibiscus cannabinus) lifleri",
    ["Sisal lifleri", "Abaka (Manila kendiri) lifleri", "Rami lifleri", "Taranmış halfa lifleri"], "D", FA,
    "Kenaf, çift çenekli bitki gövdesinden elde edilen iç kabuk lifi olarak 53.03’tedir. Sisal, abaka, rami ve dokumaya elverişli madde olarak kullanılacağını gösteren tarama işlemi görmüş halfa 53.05’te yer alır. Rami çift çenekli olduğu halde 53.03’ten açıkça hariç tutulmuştur.",
    "53.03 ve 53.05 Açıklama Notları."),
  S("Aşağıdaki eşya çiftlerinden hangisinin her ikisi de <b>aynı</b> tarife pozisyonunda sınıflandırılır?",
    "Kendir ipliği – İki katlı koko ipliği (ikisi de sicim değil)",
    ["Keten ipliği – Jüt liflerinden bükülmüş iki katlı iplik", "Kabuğu çıkarılmış kendir lifi – Kendir ipliği", "Jüt ipliğinden dokunmuş mensucat – Keten mensucat",
     "Kağıt ipliği – Kağıt şeritlerinin örülmesiyle elde edilen mensucat"], "E", FA,
    "Kendir ipliği ile bir veya iki katlı koko ipliği 53.08’de birlikte yer alır. Keten ipliği 53.06, jüt ipliği 53.07; kendir lifi 53.02, kendir ipliği 53.08; jüt mensucat 53.10, keten mensucat 53.09; kağıt ipliği 53.08, kağıt şeritlerinden örülmüş mensucat 46.01’dedir.",
    "53.06, 53.07, 53.08, 53.11 Açıklama Notları; Bölüm XI Not 3."),
  S("Aşağıdakilerden hangisi diğerlerinden <b>farklı</b> bir fasılda sınıflandırılır?",
    "Odun selülozundan elde edilen viskoz devamsız lifler",
    ["Kostik sodada kaynatılarak kotonize edilmiş keten lifleri", "Jüt liflerinden bükülmüş tek katlı iplik", "Nemli kağıt şeritlerinin bükülmesiyle elde edilen iplik",
     "Hindistan cevizi liflerinden dokunmuş mensucat"], "A", FA,
    "Viskoz, tabii organik polimerin (selüloz) kimyasal işlenmesiyle üretilen suni liftir (Fasıl 54 Not 1(b)); devamsız hali Fasıl 55’tedir. Bitkisel kökenli olması onu Fasıl 53 yapmaz. Kotonize keten 53.01, jüt ipliği 53.07, kağıt ipliği 53.08, koko mensucat 53.11 ile Fasıl 53’tedir.",
    "Fasıl 54 Not 1(b); 53.01, 53.07, 53.08, 53.11 Açıklama Notları."),
  S("Aşağıdaki kendir ve diğer bitkisel lif ürünlerinden hangisi, diğer dördünden <b>farklı</b> olarak 53. fasıl dışında sınıflandırılır?",
    "Kendir paçavraları ve kullanılmış halat hurdaları",
    ["Kostik soda ile kotonize edilmiş keten lifleri", "Ağartılmış ve boyanmış jüt kıtığı", "Soyulup alkalide kaynatılmış rami lifleri",
     "Kendir liflerinin tarama sırasında çıkan döküntüleri"], "D", FA,
    "Kendir paçavra ve kırpıntıları ile ip ve halat hurdaları 53.02’nin hariç tuttuğu eşya olup Fasıl 63’te yer alır. Kotonize keten 53.01, ağartılmış jüt kıtığı 53.03 (ağartma yerini değiştirmez), rami 53.05, kendir tarama döküntüleri 53.02 ile Fasıl 53’tedir.",
    "53.02 Açıklama Notu (hariç tutmalar); 53.01, 53.03, 53.05 Açıklama Notları."),
  # --- Fasıl notu · Tanım/Eşik (4)
  S("Bölüm XI notlarına göre keten veya kendirden <b>cilalanmış veya parlatılmış</b> bir ipliğin “sicim, ip ve halat” sayılması için ölçüsü nasıl olmalıdır?",
    "1.429 desiteks veya daha fazla",
    ["20.000 desiteksten fazla", "10.000 desiteksten fazla", "5.000 desiteksten fazla",
     "133 desiteks veya daha az"], "B", FN,
    "Bölüm XI Not 3(A)(c)(i) uyarınca cilalanmış veya parlatılmış keten veya kendir ipliği 1.429 desiteks veya daha fazla ise sicim, ip ve halat sayılır (56.07). Cilasız olanlarda sınır 20.000 desiteksi aşmaktır; 10.000 desiteks suni ve sentetik lifler, 133 desiteks ise ipeğin perakende istisnası içindir.",
    "Bölüm XI Not 3(A)(c)."),
  S("Bölüm XI notlarına göre aşağıdaki ipliklerden hangisi “sicim, ip ve halat” <b>sayılmaz</b>?",
    "Metal takviyesiz, 30.000 desiteks kağıt ipliği",
    ["Cilalanmamış ve parlatılmamış, 25.000 desiteks keten ipliği", "Üç katlı, örülmemiş Hindistan cevizi (koko) ipliği",
     "Metal iplikle takviye edilmiş, 3.000 desiteks jüt ipliği", "Cilalanmamış, 22.000 desiteks tek katlı jüt ipliği"], "C", FN,
    "Not 3(B)(a) kağıt ipliklerini (metal takviyeli olanlar hariç) sicim tanımının dışında tutar; bu iplik ne kadar kalın olursa olsun 53.08’de kalır. Cilasız 20.000 desiteksi aşan keten ipliği, üç katlı koko ipliği, metal takviyeli iplik ve 20.000 desiteksi aşan diğer bitkisel lif (jüt) ipliği sicim sayılır ve 56.07’ye gider.",
    "Bölüm XI Not 3(A) ve 3(B)(a)."),
  S("53.03 ve 53.05 pozisyonlarının ayrımına ilişkin aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
    "53.03 çift çenekli gövde liflerini kapsar; rami çift çenekli olsa da 53.05’tedir.",
    ["53.05’teki tek çenekli bitki lifleri, 53.03’teki iç kabuk liflerinden genellikle daha yumuşak ve incedir.",
     "Keten ve kendir, iç kabuk lifi oldukları için 53.03’te sınıflandırılır.",
     "Fasıl 14’teki kapok, hiçbir işlem görmeden 53.05’te sınıflandırılır.",
     "Jüt liflerinin ağartılmış veya boyanmış olanları 53.03 dışında kalır."], "D", FN,
    "53.03 keten, kendir ve rami hariç çift çenekli bitki gövdelerinin liflerini kapsar; rami urticaceae familyasından olup 53.05’te sayılmıştır. 53.03 lifleri 53.05 liflerinden daha yumuşak ve incedir (ilk ifade tersidir). Keten 53.01, kendir 53.02’dedir; kapok ancak dokumaya hazırlık işlemiyle 53.05’e girer; ağartma ve boyama yer değiştirmez.",
    "53.03 ve 53.05 Açıklama Notları."),
  S("Bölüm XI Not 2(B) hükümleriyle ilgili aşağıdaki ifadelerden hangisi <b>yanlıştır</b>?",
    "Keten ve jüt farklı pozisyonlarda yer aldığından karışımda fasıl seçilirken ayrı ayrı tartılır.",
    ["Uygun pozisyonun seçimi önce uygun faslın, sonra o fasıldaki pozisyonun seçimiyle yapılır.",
     "Fasıl içinde pozisyon seçilirken o fasılda sınıflandırılmayan maddeler dikkate alınmaz.",
     "54. ve 55. fasılların her ikisi bir başka fasılla ilgili olduğunda tek fasıl kabul edilir.",
     "Metalize iplik tek bir dokumaya elverişli madde sayılır; ağırlığı unsurlarının toplam ağırlığıdır."], "A", FN,
    "Not 2(B)(d) uyarınca bir fasıl farklı dokumaya elverişli maddelere atıf yapıyorsa bunlar tek madde sayılır; Fasıl 53’teki keten ve jüt fasıl seçiminde toplanır. Diğer dört ifade Not 2(B)(b), (c) ve (a)’nın doğru özetidir.",
    "Bölüm XI Not 2(B)(a)–(d); Bölüm XI Genel Açıklamalar (I)(A)."),
  # --- GYK (2)
  S("Ağırlık itibariyle %50 keten ve %50 pamuk ipliklerinden dokunmuş, parça halindeki mensucatın 4’lü pozisyonu ve sınıflandırmanın dayandığı kural hangi seçenekte doğru verilmiştir?",
    "53.09 – GYK 1 (Bölüm XI Not 2(A) uyarınca)",
    ["52.12 – GYK 3(b)", "52.12 – GYK 3(c)", "53.09 – GYK 3(b)", "53.11 – GYK 1 (Bölüm XI Not 2(A) uyarınca)"], "C", GY,
    "Hiçbir madde ağırlıkça üstün gelmediğinden Bölüm XI Not 2(A) ikinci paragrafı uygulanır: eşya, her biri geçerli olabilecek pozisyonların numara sırasına göre sonuncusunda, yani keten mensucat olarak 53.09’da sınıflandırılır. Sonuç bir Bölüm notundan çıktığı için dayanak GYK 1’dir; GYK 3(c) benzer mantık taşısa da uygulanmaz. 53.11 keten dışı bitkisel lif mensucatı içindir.",
    "Bölüm XI Not 2(A); GYK 1."),
  S("Bir keten mensucat ile bir jüt mensucatın bütün yüzeyleriyle üst üste konulup dikilmesiyle elde edilen, 58.11 pozisyonundaki kapitoneli ürün niteliğinde olmayan parça halindeki ürün için aşağıdakilerden hangisi <b>doğrudur</b>?",
    "Ürün, Tarifenin Yorumuna ilişkin 3 numaralı Kurala göre sınıflandırılır.",
    ["Ağırlıkça üstün gelen lif esas alınarak Bölüm XI Not 2 uyarınca sınıflandırılır.",
     "GYK 2(a) uyarınca bitirilmemiş hazır eşya olarak sınıflandırılır.",
     "Bölüm XI Not 7 anlamında hazır eşya sayılarak Fasıl 63’te yer alır.",
     "Her tabaka ayrı ayrı kendi pozisyonunda sınıflandırılır."], "E", GY,
    "Bölüm XI Genel Açıklamalarına göre iki veya daha fazla mensucatın tabakalar halinde dikilme, yapıştırma vb. ile tertip edilmesinden oluşan ürünler (58.11 hariç) GYK 3’e göre sınıflandırılır; Not 2’deki ağırlık kuralı yalnız tek bir kumaşın içindeki liflerin karşılaştırılmasında kullanılır. Not 7(f), bütün yüzeyleriyle üst üste konularak birleştirilen mensucatı hazır eşya saymaz.",
    "Bölüm XI Genel Açıklamalar (I)(A); Bölüm XI Not 7(f); GYK 3."),
  # --- Eşleştirme / Boşluk doldurma (2)
  S("Aşağıdaki lif/iplik – pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
    "Rami lifi – 53.05",
    ["Kendir ipliği – 53.06", "Abaka (Manila kendiri) lifi – 53.02", "Jüt ipliği – 53.08",
     "Kenaf lifi – 53.05"], "B", ES,
    "Rami 53.05’te sayılan liflerdendir. Kendir ipliği 53.08’de (53.06 yalnız keten ipliği), abaka adında kendir geçse de 53.05’te, jüt ipliği 53.07’de, kenaf ise iç kabuk lifi olarak 53.03’tedir.",
    "53.02, 53.03, 53.05, 53.07, 53.08 Açıklama Notları."),
  S("“Kendir lifleri ..... pozisyonunda, kendir iplikleri ..... pozisyonunda, kendir ipliğinden dokunmuş mensucat ise ..... pozisyonunda sınıflandırılır.” Boşluklara sırasıyla gelmesi gerekenler hangi seçenekte verilmiştir?",
    "53.02 – 53.08 – 53.11",
    ["53.02 – 53.06 – 53.09", "53.02 – 53.07 – 53.10", "53.03 – 53.08 – 53.11", "53.01 – 53.08 – 53.10"], "C", ES,
    "Kendir lifi 53.02’de, kendir ipliği 53.08’de (53.02 Açıklama Notu hariç tutması), 53.08 ipliklerinden dokunmuş mensucat ise 53.11’de yer alır. 53.06/53.09 keten, 53.07/53.10 jüt ipliği ve mensucatıdır; 53.03 jüt ve iç kabuk lifleri içindir.",
    "53.02, 53.08, 53.11 Açıklama Notları."),
  # --- Çoktan-çoğa (2)
  SX("Tarife Cetveline göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>? I. Ağartılmış veya boyanmış jüt lifleri 53.03’te kalır. II. Hafif bükümlü taranmış keten fitili keten ipliği olarak 53.06’da sınıflandırılır. III. Örülmemiş ve metal takviyesiz kağıt ipliği, sicim şeklinde olsa da 53.08’de kalır. IV. Dokumaya elverişli madde olarak kullanılacağını gösteren işlem görmemiş turba lifleri 27.03’te yer alır.",
     ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"], "D", CC,
     "I doğrudur: ağartma veya boyama 53.03’teki yeri değiştirmez. II yanlıştır: hafif bükümlü fitil 53.01’de kalır ve 53.06’daki tek katlı iplikle karıştırılmamalıdır. III doğrudur: Not 3(B)(a) kağıt ipliğini sicim tanımı dışında tutar. IV doğrudur: işlem görmemiş turba lifleri 27.03’tedir.",
     "53.01, 53.03, 53.05, 53.08 Açıklama Notları; Bölüm XI Not 3(B)(a)."),
  SX("Aşağıdakilerden hangileri 53.05 pozisyonunda yer alır? I. Sisal lifleri II. Hiçbir işlem görmemiş halfa yaprakları III. Taranmış Tampiko kendiri (istle) lifleri IV. Su kamışı (Typha) tohumlarının etrafındaki dolgu tüyleri",
     ["I ve II", "I ve III", "II ve IV", "I, II ve III", "I, III ve IV"], "B", CC,
     "Sisal (I) 53.05’te sayılmıştır. İstle (III) genellikle 14.04’te yer alır, ancak tarama gibi dokumaya elverişli madde olarak kullanılacağını gösteren işlem görmüşse 53.05’e girer. İşlem görmemiş halfa yaprakları (II) Fasıl 14’te, su kamışı tohum tüyleri (IV) 14.04’te kalır.",
     "53.05 Açıklama Notu."),
  # --- Senaryo (2)
  S("Bir firma, ağırlık itibariyle %30 keten, %32 jüt ve %38 pamuktan oluşan, parça halinde, çuval imalinde kullanılacak dokunmuş mensucat ithal etmektedir. Bu mensucat hangi pozisyonda sınıflandırılır?",
    "53.10", ["52.12", "53.09", "53.11", "53.07"], "A", SN,
    "Not 2(B)(d) uyarınca Fasıl 53’teki keten ve jüt tek madde sayılır (%62) ve pamuktan (%38) üstün geldiği için önce Fasıl 53 seçilir. Fasıl içinde pamuk dikkate alınmaz (Not 2(B)(b)); jüt (%32) ketenden (%30) ağır olduğundan jüt mensucat pozisyonu 53.10 uygulanır. Tek tek bakıldığında en ağır lif pamuk olsa da 52.12’ye gidilmez; 53.09 seçmek fasıl içi karşılaştırmayı atlamaktır.",
    "Bölüm XI Not 2(A), 2(B)(b) ve (d); Bölüm XI Genel Açıklamalar (I)(A)."),
  S("Bir ithalatçı, ticarette Manila kendiri olarak bilinen, Musa textilis Nee türü muz bitkisinin yaprak saplarından kazınarak ayrılmış, deniz suyuna dayanıklı, iplik imali için şerit haline getirilmiş ve henüz bükülmemiş lifler getirmiştir. Lifler hangi pozisyonda sınıflandırılır?",
    "53.05", ["53.02", "53.03", "53.08", "14.04"], "E", SN,
    "Abaka (Manila kendiri) 53.05 pozisyon metninde açıkça sayılmıştır; şerit veya fitil haline getirilmiş olması yerini değiştirmez. Adında “kendir” geçmesi 53.02’yi gerektirmez, çünkü 53.02 yalnız Cannabis sativa L. içindir. 53.03 çift çenekli iç kabuk lifleri, 53.08 iplikler içindir.",
    "53.05 pozisyon metni ve Açıklama Notu; 53.02 Açıklama Notu.")
 ]
}

yaz(d, 53)
