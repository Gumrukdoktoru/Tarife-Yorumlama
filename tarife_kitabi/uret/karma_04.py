#!/usr/bin/env python3
"""Karma test 4 üreticisi (20 soru, şık dağılımı 4×A–E)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_04.json")

E4 = "Eşya → 4’lü pozisyon"
POZ = "Pozisyon → eşya"
OLM = "Olumsuz teşhis"
FAR = "Farklı/aynı pozisyon veya fasıl"
FB = "Fasıl/Bölüm bulma"
NOT = "Fasıl notu · Tanım/Eşik"
GYK = "Genel Yorum Kuralı"
SIR = "Sıralama"
YAP = "Tarife yapısı"


def q(fasil, tip, soru, secenekler, cevap, gerekce, dayanak):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


S = [
    # 1 — Genel / Tarife yapısı — D
    q("Genel", YAP,
      "Tarife Cetvelinin bölüm–fasıl yapısına göre aşağıdaki fasıl ikililerinden hangisinde yer alan "
      "fasıllar <b>farklı</b> bölümlerde bulunur?",
      ["Fasıl 25 – Fasıl 27", "Fasıl 28 – Fasıl 38", "Fasıl 64 – Fasıl 67",
       "Fasıl 71 – Fasıl 72", "Fasıl 86 – Fasıl 89"],
      "D",
      "Fasıl 71 tek başına XIV. Bölümü oluşturur; adi metaller bölümü (XV) Fasıl 72 ile başlar. "
      "Diğer ikililer aynı bölümdedir: 25–27 V, 28–38 VI, 64–67 XII, 86–89 XVII. Tuzak: komşu fasılları "
      "aynı bölümde sanmak.",
      "Tarife Cetveli bölüm ve fasıl listesi (İçindekiler)."),

    # 2 — 85 / Fasıl bulma — B
    q(85, FB,
      "Tarife Cetveline göre, çektiği görüntüleri dahili bir yarı iletken mesnet üzerine kaydeden dijital "
      "fotoğraf makinesi hangi fasılda yer alır?",
      ["Fasıl 90", "Fasıl 85", "Fasıl 84", "Fasıl 37", "Fasıl 95"],
      "B",
      "85.25 metni dijital kameraları ismen sayar; 90.06 Açıklama Notu da dijital kameraları fotoğraf "
      "makinelerinden hariç tutup 85.25’e gönderir. Tuzak: “fotoğraf makinesi” adı nedeniyle Fasıl 90’ı "
      "seçmek; Fasıl 37 film ve levhaları kapsar.",
      "85.25 pozisyon metni; 90.06 Açıklama Notu."),

    # 3 — 94 / Eşya → 4’lü — E
    q(94, E4,
      "Tarife Cetveline göre, belirli bir kanepe modeline ait olduğu açıkça anlaşılan, gözenekli plastikle "
      "doldurulmuş ve kumaşla kaplanmış, kanepeden ayrı olarak sunulan oturma minderi hangi pozisyonda "
      "sınıflandırılır?",
      ["94.01", "63.04", "39.26", "94.03", "94.04"],
      "E",
      "94.01 Açıklama Notuna göre içi doldurulmuş veya gözenekli plastikten ayrı gelen minderler, döşenmiş "
      "koltuğun aksamı olduğu anlaşılsa bile 94.04’tedir; mobilyayla birleşik ya da birlikte sunulsaydı "
      "94.01’de kalırdı. İçi boş minder kılıfı 63.04’tür.",
      "94.01 ve 94.04 Açıklama Notları."),

    # 4 — 61 / Olumsuz — A
    q(61, OLM,
      "Örme veya kroşe olarak imal edilmiş aşağıdaki eşyadan hangisi Tarife Cetvelinin 61. faslında <b>yer almaz</b>?",
      ["Pantolon askısı",
       "Elektrikle ısıtılan yelek",
       "Metal iplikten örülmüş kadın şalı",
       "Boyu 80 cm olan bebek için tulum",
       "Yalnızca süs niteliğinde deri biyesi bulunan kazak"],
      "A",
      "Fasıl 61 Not 2(a) 62.12 eşyasını hariç tutar; pantolon askıları örülmüş olsalar da 62.12’dedir. "
      "Elektrikle ısıtılan örme giysi ve metal iplikten örme eşya (Not 10) fasılda kalır; bebek tulumu "
      "61.11’de, basit süslü kazak 61.10’dadır.",
      "Fasıl 61 Not 2(a), 6 ve 10; Fasıl 61 Genel Açıklamaları; 62.12 pozisyon metni."),

    # 5 — 87 / Farklı-aynı — C
    q(87, FAR,
      "Aşağıdaki seçeneklerin hangisinde, diğerleriyle aynı 4’lü pozisyonda yer <b>almayan</b> bir eşya "
      "bulunmaktadır?",
      ["Golf arabası – Kar üzerinde hareket etmek için özel imal edilmiş taşıt – Cenaze arabası",
       "Tank – Silahla donatılmamış zırhlı savaş taşıtı – Ayrı gelen tank paleti",
       "İtfaiye taşıtı – Beton karıştırıcı ile donatılmış kamyon – Devirme tertibatlı (damperli) kamyon",
       "Bebek arabası – Bebek arabası şasisi – Bebek arabası tekerleği",
       "Yarı römork – Karavan tipi kamp römorku – Elle itilen el arabası"],
      "C",
      "İtfaiye taşıtı ve beton karıştırıcılı kamyon özel amaçlı taşıt olarak 87.05’te, damperli kamyon "
      "ise eşya taşıyan taşıt olarak 87.04’tedir. Diğer gruplar sırasıyla 87.03, 87.10 (aksamı dahil), "
      "87.15 (aksamı dahil) ve 87.16’da toplanır.",
      "87.03, 87.04, 87.05, 87.10, 87.15 ve 87.16 pozisyon metinleri ve Açıklama Notları."),

    # 6 — 27 / Eşya → 4’lü — B
    q(27, E4,
      "Tarife Cetveline göre, bitümenli şistin kuru damıtılmasıyla elde edilen ve yalnızca suyu alınıp "
      "tortusundan ayrılmış ham şist yağı hangi pozisyonda sınıflandırılır?",
      ["27.14", "27.09", "27.10", "27.06", "27.07"],
      "B",
      "27.09, bitümenli minerallerin kuru damıtılmasından elde edilen ham yağları da kapsar; tortudan "
      "ayırma ve suyunu alma ürünü ham olmaktan çıkarmaz. Şistin kendisi 27.14’te, ham olmayan yağlar "
      "27.10’da, taşkömürü-linyit-turb katranları 27.06’dadır.",
      "27.09 pozisyon metni ve Açıklama Notu; 27.14 pozisyon metni."),

    # 7 — 46 / Sıralama — A
    q(46, SIR,
      "Aşağıdaki eşyanın (I–V) Tarife Cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru "
      "dizilişi hangisidir?<br/>"
      "I. Hint kamışından (rattan) örülmüş koltuk<br/>"
      "II. Söğüt dallarından örülmüş çamaşır sepeti<br/>"
      "III. Henüz örülmemiş, demetler halindeki sepetçi söğüdü dalları<br/>"
      "IV. Genişliği 60 cm olan rulolar halinde, ön yüzü örülmeye elverişli maddelerle kaplanmış "
      "kâğıttan duvar kaplaması<br/>"
      "V. Hasır şeritlerinin dikilerek birleştirilmesiyle yapılmış, astarlanmış yazlık şapka",
      ["III – II – IV – V – I", "II – III – IV – V – I", "III – II – V – IV – I",
       "III – IV – II – V – I", "II – III – V – I – IV"],
      "A",
      "Örülmemiş söğüt 14.01, söğüt sepeti 46.02, ön yüzü örgü maddesiyle kaplı kâğıt duvar kaplaması "
      "48.14, şerit birleştirme şapka 65.04, rattan koltuk 94.01’dedir. Fasıl 46 Not 2 duvar kaplamasını, "
      "şapkayı ve mobilyayı fasıl dışına çıkarır.",
      "Fasıl 46 Not 2; Fasıl 48 Not 9(a); 14.01, 46.02, 65.04 ve 94.01 pozisyon metinleri."),

    # 8 — 76 / Pozisyon → eşya — C
    q(76, POZ,
      "Alüminyumdan yapılmış aşağıdaki eşyadan hangisi 76.15 pozisyonunda sınıflandırılır?",
      ["Alüminyumdan çorba kepçesi",
       "Konserve ambalajında kullanılan alüminyum kutu",
       "Alüminyumdan banyo küveti",
       "Süs eşyası olarak kullanılan alüminyum heykelcik",
       "Ev tipi elektrikli alüminyum su ısıtıcısı"],
      "C",
      "76.15 sofra ve mutfak eşyasıyla birlikte sağlığı koruyucu eşyayı da kapsar; küvet bu gruptadır. "
      "Açıklama Notu kepçeleri (82.15), 76.12 kutularını, süs eşyasını (83.06) ve 85.16 gibi elektrikli ev "
      "cihazlarını hariç tutar.",
      "76.15 pozisyon metni ve Açıklama Notu; 73.24 Açıklama Notu."),

    # 9 — 33 / Olumsuz — E
    q(33, OLM,
      "Aşağıdakilerden hangisi Tarife Cetvelinin 33. faslında <b>sınıflandırılmaz</b>?",
      ["Makyaj temizleme losyonu emdirilmiş vatka ped",
       "Hayvan tırnaklarını tedaviye mahsus müstahzar",
       "Diş hekimlerince kullanılan, aşındırıcı madde içeren diş parlatma macunu",
       "Tırnak çevresindeki ölü derileri gidermeye mahsus müstahzar",
       "Sabun emdirilmiş, el ve yüz yıkamada kullanılan vatka ped"],
      "E",
      "Sabun veya deterjan emdirilmiş kâğıt, vatka, keçe ve dokunmamış mensucat 34.01’dedir. Kozmetik "
      "emdirilmiş vatka Not 4 gereği 33.07’de; tırnak tedavi müstahzarı 33.07’de, dişçi macunu 33.06’da, "
      "tırnak eti giderici 33.04’te kalır.",
      "Fasıl 33 Not 4 ve Genel Açıklamalar; 33.04 ve 33.06 Açıklama Notları; 34.01 pozisyon metni."),

    # 10 — GYK 5(a) — D
    q("GYK", GYK,
      "Görme kusurunu düzeltici bir gözlük; bu gözlüğe göre şekil verilmiş, uzun süre kullanılmaya "
      "elverişli ve normal olarak gözlükle birlikte satılan türden kılıfı içinde gümrüğe sunulmuştur. "
      "Kılıflı gözlük hangi pozisyonda ve hangi yorum kuralına göre sınıflandırılır?",
      ["Gözlük 90.04’te, kılıf 42.02’de ayrı ayrı – GYK 1",
       "90.04 – GYK 5(b)",
       "42.02 – GYK 3(b)",
       "90.04 – GYK 5(a)",
       "90.04 – GYK 3(b)"],
      "D",
      "GYK 5(a), belli bir eşyaya göre şekillendirilmiş, uzun süre kullanılmaya uygun ve eşyayla birlikte "
      "satılan mahfazayı o eşyayla birlikte sınıflandırır; kılıf gözlükle 90.04’e gider. 5(b) yalnız "
      "normal ambalaj içindir; mahfaza için özel kural varken 3(b)’ye başvurulmaz.",
      "GYK 5(a) ve Açıklama Notu; 90.04 pozisyon metni."),

    # 11 — 93 / Olumsuz — D
    q(93, OLM,
      "Aşağıdakilerden hangisi Tarife Cetvelinin 93. faslında <b>sınıflandırılmaz</b>?",
      ["Tüfeğe takılan süngü ve kını",
       "Üzerine takılı teleskopik dürbünüyle birlikte sunulan av tüfeği",
       "Harp gemisine takılmak üzere tasarlanmış, ayrı olarak gelen top",
       "Askerî personele mahsus çelik miğfer",
       "Basınçlı havayla çalışan tüfek"],
      "D",
      "Fasıl 93 Genel Açıklamaları çelik miğferleri ve diğer askerî başlıkları fasıl dışında bırakarak "
      "Fasıl 65’e gönderir. Silaha takılı dürbün silahla sınıflandırılır; taşıta takılacak ayrı gelen "
      "silahlar 93.01’de, süngü ve kını 93.07’de, havalı tüfek 93.04’tedir.",
      "Fasıl 93 Not 1(d) ve Genel Açıklamalar; 93.01 Açıklama Notu."),

    # 12 — 59 / Eşya → 4’lü — A
    q(59, E4,
      "Tarife Cetveline göre, ayakkabı cilalama makinelerinde kullanılmak üzere dokumaya elverişli maddeden "
      "yapılmış parlatma diski hangi pozisyonda sınıflandırılır?",
      ["59.11", "59.10", "63.07", "68.04", "96.03"],
      "A",
      "59.11 Açıklama Notu, ayakkabı cila makinelerine ve diğer makinelere mahsus dokumaya elverişli disk, "
      "manşon ve tamponları teknik eşya sayar; Bölüm XVI Not 1(e) de bunları makine parçası olmaktan "
      "çıkarır. 59.10 kolanları, 68.04 aşındırıcı taşları kapsar.",
      "Fasıl 59 Not 8(b); 59.11 Açıklama Notu; Bölüm XVI Not 1(e)."),

    # 13 — 41 / Eşya → 4’lü — C
    q(41, E4,
      "Tarife Cetveline göre, kılları alınmış; dabaklama ve ara kurutmadan sonra boyanıp perdahlanarak "
      "ileri derecede hazırlanmış deve derisi hangi pozisyonda sınıflandırılır?",
      ["41.06", "41.07", "41.13", "41.03", "43.02"],
      "C",
      "41.13 Açıklama Notu, 41.07 ve 41.12’de belirtilmeyen hayvanların (deve dahil) dabaklama veya ara "
      "kurutmadan sonra ileri derecede hazırlanmış derilerini kapsar. Yalnız dabaklanmış veya crust olsaydı "
      "41.06’da, ham olsaydı 41.03’te kalırdı; 41.07 yalnız sığır ve at derileri içindir.",
      "41.06 ve 41.13 pozisyon metinleri; 41.13 Açıklama Notu."),

    # 14 — 68 / Farklı fasıl — C
    q(68, FAR,
      "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
      ["Cüruf yününden ısı yalıtım şiltesi",
       "Turbdan yapılmış bitki yetiştirme saksısı",
       "Mermerden yapılmış satranç tahtası ve taşları",
       "Mermerden kesilip cilalanmış pencere denizliği",
       "Bıçak bilemeye mahsus, el ile kullanılan tabii taştan bileği taşı"],
      "C",
      "Fasıl 68 Not 1(l), Fasıl 95 eşyasını (oyun ve spor levazımatı) hariç tutar; satranç takımı yapıldığı "
      "madde ne olursa olsun 95.04’tedir. Cüruf yünü 68.06, turbdan eşya 68.15, işlenmiş mermer 68.02, "
      "bileği taşı 68.04 ile Fasıl 68’dedir.",
      "Fasıl 68 Not 1(l); 95.04 Açıklama Notu; 68.02, 68.04, 68.06 ve 68.15 pozisyon metinleri."),

    # 15 — 48 / Fasıl notu — E
    q(48, NOT,
      "Tarife Cetvelinin 48. Fasıl Not 3’üne göre, aşağıdaki işlemlerden hangisini görmüş kâğıt 48.01 ila "
      "48.05 pozisyonlarında sınıflandırılmaya devam edebilir?",
      ["Bir yüzünün kaolinle sıvanması (kuşe edilmesi)",
       "Kendinden yapışkanlı hale getirilmesi",
       "Parafinle emdirilmesi",
       "Bir yüzünün plastikle kaplanması",
       "Kütle halinde boyanması veya mermer taklidi yapılması"],
      "E",
      "Not 3, perdahlama, cilalama, taklit filigran, yüzey apresi ile kütle halinde boyanmış veya mermer "
      "taklidi yapılmış kâğıdı 48.01–48.05’te bırakır. Kaolinle sıvama 48.10’a; yapışkanlı hale getirme, "
      "parafin emdirme ve plastik kaplama 48.11’e götürür.",
      "Fasıl 48 Not 3; 48.10 ve 48.11 pozisyon metinleri."),

    # 16 — GYK 3(b) — B
    q("GYK", GYK,
      "Perakende satış için hazırlanmış bir hediye kutusunda bir şişe parfüm (33.03), bir kalıp tuvalet "
      "sabunu (34.01) ve bir tüp vücut losyonu (33.04) birlikte sunulmaktadır. Takımın değerinin büyük "
      "kısmını parfüm oluşturmaktadır. Bu eşya hangi pozisyonda ve hangi yorum kuralına göre "
      "sınıflandırılır?",
      ["Her biri kendi pozisyonunda ayrı ayrı – GYK 1",
       "33.03 – GYK 3(b)",
       "34.01 – GYK 3(c)",
       "33.04 – GYK 3(a)",
       "33.03 – GYK 5(b)"],
      "B",
      "Farklı pozisyonlara giren, kişisel bakım için bir araya getirilip son kullanıcıya doğrudan satılacak "
      "biçimde kutulanan ürünler perakende takımdır; pozisyonlar eşit derecede özel sayılır ve esas niteliği "
      "veren parfüme göre 33.03’te sınıflandırılır. 3(c) ancak esas nitelik saptanamazsa uygulanır.",
      "GYK 3(a) ikinci cümlesi; GYK 3(b) ve Açıklama Notu (X)."),

    # 17 — 84 / Eşya → 4’lü — A
    q(84, E4,
      "Tarife Cetveline göre, bahçelerde duvar dipleri ve çalılık kenarlarındaki çimleri kesmeye mahsus, "
      "içten yanmalı kendinden motorlu, kesici tertibatı naylon tellerden oluşan ve elde taşınarak "
      "kullanılan portatif cihaz hangi pozisyonda sınıflandırılır?",
      ["84.67", "84.33", "84.32", "82.01", "84.79"],
      "A",
      "84.33 Açıklama Notu binmeli çim biçme makinelerini kapsar, ancak duvar dibi ve çalılıklarda "
      "kullanılan naylon telli, kendinden motorlu portatif çim kesme cihazlarını hariç tutarak elle "
      "kullanılan kendinden motorlu alet olarak 84.67’ye gönderir. 82.01 motorsuz el aletleri içindir.",
      "84.33 Açıklama Notu; 84.67 pozisyon metni."),

    # 18 — 38 / Olumsuz — E
    q(38, OLM,
      "Aşağıdakilerden hangisi Tarife Cetvelinin 38. faslında <b>sınıflandırılmaz</b>?",
      ["Alüminyum oksit mesnet üzerine nikel bileşiği tespit edilmiş takviyeli katalizör",
       "Benzinli motorlar için vuruntuyu önleyici müstahzar",
       "Donmayı çözücü müstahzar sıvı",
       "Kauçuk için vulkanizasyonu çabuklaştırıcı müstahzar",
       "Kıymetli metalin geri kazanılmasında kullanılan türden, etkisi kalmamış katalizör"],
      "E",
      "Fasıl 38 Not 1(f) ve 38.15 Açıklama Notu, kıymetli metallerin geri kazanılmasında kullanılan etkisi "
      "kalmamış katalizörleri 71.12’ye gönderir. Mesnetli nikel katalizör 38.15, vuruntu önleyici 38.11, "
      "donma çözücü 38.20, vulkanizasyon çabuklaştırıcı 38.12’dedir.",
      "Fasıl 38 Not 1(f); 38.15 Açıklama Notu."),

    # 19 — 71 / Fasıl notu — D
    q(71, NOT,
      "Tarife Cetvelinin 71. Fasıl notlarına göre, kıymetli metal, inci veya kıymetli taş içermeyen "
      "aşağıdaki eşyadan hangisi 71.17 pozisyonu anlamında “taklit mücevher” tabirine <b>girmez</b>?",
      ["Adi metalden kol düğmesi",
       "Adi metalden kravat iğnesi",
       "Cam boncuklarla süslenmiş adi metal küpe",
       "Adi metalden elbise düğmesi",
       "Adi metalden dini madalyon"],
      "D",
      "Not 11 taklit mücevheri Not 9(a)’daki kişisel süs eşyası olarak tanımlar, ancak 96.06’daki "
      "düğmeleri ve 96.15’teki tarak-tokaları hariç tutar. Elbise düğmesi Not 9(a)’da sayılsa da "
      "96.06’dadır; kol düğmesi, kravat iğnesi, küpe ve madalyon 71.17’dedir.",
      "Fasıl 71 Not 9(a) ve Not 11; 96.06 pozisyon metni."),

    # 20 — GYK 1 (Bölüm XVII Not 5) — B
    q("GYK", GYK,
      "Hava yastıklı taşıtların Bölüm XVII’de “en çok benzedikleri taşıtlar ile birlikte” "
      "sınıflandırılması Genel Yorum Kuralları bakımından hangi kurala dayanır?",
      ["GYK 4 – eşya, en çok benzediği eşyanın pozisyonunda sınıflandırıldığı için",
       "GYK 1 – sınıflandırma bir bölüm notu hükmüne göre yapıldığı için",
       "GYK 3(a) – ilgili fasıl eşyayı daha özel tanımladığı için",
       "GYK 3(c) – geçerli pozisyonlardan numara sırasına göre sonuncusu esas alındığı için",
       "GYK 2(a) – hava yastıklı taşıt tamamlanmamış taşıt sayıldığı için"],
      "B",
      "Not metnindeki “en çok benzedikleri” ifadesi GYK 4’ü çağrıştırsa da sınıflandırma Bölüm XVII Not 5 "
      "hükmüyle yapıldığından GYK 1’e dayanır. GYK 4 yalnız 1–3 numaralı kurallarla sınıflandırılamayan "
      "eşyaya uygulanır; hava treni böylece Fasıl 86’ya, suda işleyenler Fasıl 89’a girer.",
      "GYK 1 ve GYK 4 Açıklama Notları; Bölüm XVII Not 5."),
]

assert len(S) == 20
doc = {"tur": "karma", "no": 4, "sorular": S}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT)
