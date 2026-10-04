#!/usr/bin/env python3
"""Fasıl 32 (Debagat ve boyacılık hülasaları; boyalar, vernikler, macunlar, mürekkepler) modülünü üretir."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KITAP, "data", "fasil_32.json")

T_ESYA = "Eşya → 4’lü pozisyon"
T_OLUMSUZ = "Olumsuz teşhis"
T_FARKLI = "Farklı/aynı pozisyon veya fasıl"
T_NOT = "Fasıl notu · Tanım/Eşik"
T_GYK = "Genel Yorum Kuralı"
T_ESL = "Eşleştirme / Boşluk doldurma"
T_COK = "Çoktan-çoğa (I–IV)"
T_SEN = "Senaryo"


def Q(tip, soru, dogru, yanlislar, harf, gerekce, dayanak):
    assert len(yanlislar) == 4, soru
    i = "ABCDE".index(harf)
    secenekler = list(yanlislar)
    secenekler.insert(i, dogru)
    return {"soru": soru, "secenekler": secenekler, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


sorular = [
    # 1
    Q(T_ESYA,
      "Esası akrilik polimer olan, su ile inceltilerek uygulanan iç cephe plastik boyası Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
      "32.09", ["32.08", "32.10", "32.14", "39.06"], "E",
      "Esası sentetik polimer olan ve sulu ortamda dağılan veya çözünen boyalar 32.09’dadır; açıklama notu poliakrilik esterleri bağlayıcı örneği olarak sayar. Aynı polimer susuz (çözücü) ortamda olsaydı 32.08 olurdu. Yüksek oranda dolgu içeren, mala ile uygulanan yüzey müstahzarları 32.14’e, boya niteliği kazanmamış akrilik polimerler 39.06’ya gider.",
      "32.09 pozisyon metni ve Açıklama Notu."),
    # 2
    Q(T_ESYA,
      "Film tabakası keten tohumu yağı ile tabii reçinelerin karışımından oluşan yağlı vernik hangi pozisyonda yer alır?",
      "32.10", ["32.08", "32.09", "15.18", "32.11"], "C",
      "32.10 açıklama notu, film tabakasını kurutucu bir sıvı yağın veya bu yağın tabii reçinelerle karışımının oluşturduğu yağlı vernikleri sayar. 32.08 ve 32.09 esası sentetik veya kimyasal olarak tadil edilmiş tabii polimer olan ürünler içindir. 15.18 kaynatılmış veya kimyasal olarak tadil edilmiş yağlar, 32.11 kurutucular içindir.",
      "32.10 Açıklama Notu (B)(1)."),
    # 3
    Q(T_ESYA,
      "Kitap kapaklarına sıcak baskı ile yazı basmakta kullanılan, plastik bir mesnet yaprak üzerine metal tespit edilerek elde edilmiş ince yapraklar (baskı folyosu) hangi pozisyonda sınıflandırılır?",
      "32.12", ["76.07", "39.20", "32.07", "32.15"], "A",
      "Fasıl 32 Not 6, ıstampacılığa mahsus varakları; metal tozları veya pigmentlerin bağlayıcıyla aglomere edildiği ya da metal veya pigmentlerin herhangi bir maddeden mesnet yaprak üzerine tespit edildiği, baskıcılıkta kullanılan ince yapraklar olarak tanımlar ve bunlar 32.12’dedir. Haddeleme veya dövme ile elde edilen metal folyolar ise metaline göre (ör. 76.07) sınıflandırılır.",
      "Fasıl 32 Not 6; 32.12 Açıklama Notu (B)."),
    # 4
    Q(T_ESYA,
      "Ressamların kullandığı türden, tüpler içinde perakende satılan yağlı boyalar hangi pozisyonda yer alır?",
      "32.13", ["32.10", "32.12", "32.08", "96.09"], "D",
      "32.13; ressamlar, öğrenciler veya tabelacılar tarafından kullanılan, tablet, tüp, kavanoz, şişe, çanak veya benzeri şekil ya da ambalajlardaki boyaları (sulu boya, guaj, yağlı boya) kapsar. “Yağlı” kelimesi 32.10’u çağrıştırır; perakende ev boyaları 32.12’de, pasteller ve boya kalemleri 96.09’dadır.",
      "32.13 pozisyon metni ve Açıklama Notu."),
    # 5
    Q(T_ESYA,
      "Koşnil böceklerinden asitli suda ekstraksiyon yoluyla elde edilen koşnil hülasası (dökme) hangi pozisyonda sınıflandırılır?",
      "32.03", ["32.04", "32.05", "05.11", "13.02"], "B",
      "32.03 hayvansal veya bitkisel menşeli boyayıcı maddeleri kapsar; açıklama notu koşnil hülasalarını hayvansal menşeli boyayıcı örneği olarak verir. Koşnil hülasası şap ile işlenip bir baz üzerine tespit edilirse koşnil kırmızısı lakı olarak 32.05’e geçer; tuzak budur. 32.04 sentetik organik boyalar içindir.",
      "32.03 Açıklama Notu (2); 32.05 Açıklama Notu."),
    # 6 — Olumsuz
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi Tarife Cetvelinin 32. faslında <b>sınıflandırılmaz</b>?",
      "Fildişi karası",
      ["Prusya mavisi", "Litopon", "Ultramarin mavisi", "Bizmut oksiklorürle kaplanmış mika"], "A",
      "Fildişi karası ve diğer hayvansal karalar 32.03 açıklama notunda hariç tutulmuş ve 38.02’ye gönderilmiştir. Prusya mavisi, litopon, ultramarin ve sentetik sedef pigmenti olarak bizmut oksiklorürle kaplanmış mika 32.06 açıklama notunda sayılan diğer boyayıcı maddelerdir.",
      "32.03 ve 32.06 Açıklama Notları."),
    # 7
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 32.15 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Mürekkep haznesi ve bilyalı ucuyla birlikte tükenmez kalem kartuşu",
      ["Tablet halinde, sulandırılarak kullanılan konsantre yazı mürekkebi",
       "Normal dolma kalemlere mahsus mürekkep dolu kartuş",
       "Tükenmez kalemler için şişede mürekkep",
       "Kobalt klorür esaslı görünmez mürekkep"], "E",
      "32.15 açıklama notu, mürekkep haznesi ve bilyalı ucuyla birlikte olan kartuşları 96.08’e gönderir; yalnızca normal dolma kalemler için mürekkep dolu kartuşlar 32.15’tedir. Konsantre veya katı (tablet) mürekkepler, tükenmez kalem mürekkepleri ve görünmez mürekkepler pozisyon kapsamındadır.",
      "32.15 pozisyon metni ve Açıklama Notu."),
    # 8
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 32.14 pozisyonunda <b>yer almaz</b>?",
      "Asfalt macunu",
      ["Camcı macunu",
       "Mum esaslı aşılama macunu",
       "Plastik esaslı araba kaportası dolgu macunu",
       "Stoma çevresindeki deride kullanılan sızdırmazlık macunu"], "C",
      "Asfalt macunları ve diğer bitümenli macunlar 27.15’tedir (Fasıl 32 Not 1(c); 32.14 Açıklama Notu). Camcı macunu, mum esaslı aşılama macunları, plastik esaslı kaporta dolguları ve stoma-fistula çevresinde kullanılan deri macunları 32.14 açıklama notunda ismen sayılır.",
      "Fasıl 32 Not 1(c); 32.14 Açıklama Notu."),
    # 9
    Q(T_OLUMSUZ,
      "Aşağıdakilerden hangisi 32.12 pozisyonunda <b>sınıflandırılmaz</b>?",
      "Dövme yoluyla elde edilmiş altın folyo",
      ["Küçük zarflarda perakende satılan kumaş boyası",
       "Mikroskobik müstahzarların boyanmasına mahsus küçük şişelerde laboratuvar boyası",
       "Boya imalinde kullanılan, white spirit içinde hamur halinde alüminyum pul dispersiyonu",
       "Tablet şeklinde perakende satış için hazırlanmış ev boyası"], "B",
      "32.12 açıklama notuna göre haddeleme veya dövme ile elde edilen metalik folyolar metaline göre sınıflandırılır (altın 71.08). Perakende kumaş ve laboratuvar boyaları, tablet şeklindeki ev boyaları ve boya imaline mahsus susuz ortamdaki metal pul dispersiyonları 32.12’nin kapsamındadır.",
      "32.12 Açıklama Notu (A), (B), (C)."),
    # 10 — Farklı / aynı
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
      "Fırçasıyla birlikte küçük şişede perakende tırnak cilası",
      ["Poliüretan esaslı, solventli parke verniği",
       "Gomalakanın alkoldeki çözeltisinden oluşan vernik",
       "Toz halinde kazeinli distemper (beyaz boya)",
       "Su ile inceltilen akrilik esaslı parke verniği"], "D",
      "32.08 açıklama notu, 33.04 açıklama notunda belirtilen şekillerde hazırlanmış tırnak parlatıcısı tipindeki vernikleri hariç tutar; tırnak cilası Fasıl 33’tedir. Poliüretan solventli vernik 32.08, su bazlı akrilik vernik 32.09, gomalaka verniği ve distemper 32.10’dadır.",
      "32.08 Açıklama Notu; 33.04 Açıklama Notu."),
    # 11
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir tarife pozisyonunda sınıflandırılır?",
      "Krom tuzları esaslı mineral debagat maddesi",
      ["Kebrako ağacından elde edilen debagat hülasası", "Akasya (mimoza) kabuğundan debagat hülasası", "Mazı palamudu taneni (gallotannik asit)", "Kestane odunundan elde edilen tanen"], "D",
      "Krom, alüminyum, demir veya zirkonyum tuzları esaslı inorganik debagat maddeleri 32.02’dedir. Kebrako ve mimoza hülasaları bitkisel menşeli debagat hülasaları, mazı palamudu ve kestane odunu tanenleri ise tanenler olarak 32.01’de yer alır.",
      "32.01 ve 32.02 Açıklama Notları."),
    # 12
    Q(T_FARKLI,
      "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı tarife pozisyonunda yer alır?",
      "Floresanlı aydınlatma maddesi olarak kullanılan stilben türevi – Reaktif boya",
      ["Sentetik indigo – Tabii indigo",
       "Koşnil hülasası – Koşnil kırmızısı lakı",
       "Rodamin B içeren organik lüminofor – Çinko sülfür esaslı inorganik lüminofor",
       "Karmen lakı – Karbon karası"], "B",
      "Floresanlı aydınlatma maddeleri olarak kullanılan sentetik organik ürünler ve reaktif boyalar 32.04’te birliktedir. Sentetik indigo 32.04, tabii indigo 32.03; koşnil hülasası 32.03, lakı 32.05; organik lüminofor 32.04, inorganik lüminofor 32.06; karmen lakı 32.05, karbon karası 28.03’tür.",
      "32.03, 32.04, 32.05 ve 32.06 Açıklama Notları."),
    # 13
    Q(T_FARKLI,
      "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
      "Ateşe dayanıklı harç",
      ["Mala ile uygulanan akrilik esaslı dış cephe sıvası",
       "Yalnız macun olarak formüle edilmiş silikon esaslı derz macunu",
       "Çinko oksiklorür esaslı macun",
       "Belgelerin mühürlenmesinde kullanılan mühür mumu"], "E",
      "32.14 açıklama notu ateşe dayanıklı çimento ve harçları 38.16’ya gönderir; pozisyon zaten “ateşe dayanıklı olmayan” sıvama müstahzarlarıyla sınırlıdır. Dış cephe sıvası, silikon esaslı macun, çinko oksiklorür macunu ve mühür mumu 32.14’te sayılmıştır.",
      "32.14 pozisyon metni ve Açıklama Notu."),
    # 14 — Not / eşik
    Q(T_NOT,
      "Fasıl 32 Not 4’e göre, 39.01–39.13 pozisyonlarındaki bir polimerin başka katkı içermeyen uçucu organik çözücüdeki çözeltisinde çözücünün ağırlığı çözelti ağırlığının %40’ı ise eşya nerede sınıflandırılır?",
      "Fasıl 39",
      ["32.08", "32.09", "Fasıl 38", "Fasıl 27"], "A",
      "Not 4 bu çözeltileri yalnız çözücü ağırlığı çözelti ağırlığının %50’sinden fazla olduğunda 32.08’e verir. 32.08 açıklama notu, çözücü oranı %50’yi geçmeyen çözeltilerin 39. Fasılda kaldığını açıkça belirtir. Kollodyonlar ise oran ne olursa olsun 39.12’dedir.",
      "Fasıl 32 Not 4; 32.08 Açıklama Notu (C)."),
    # 15
    Q(T_NOT,
      "Fasıl 32 Not 5’e göre “boyayıcı madde” tabiri ile ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
      "Yağlı boyalarda dolgu olarak kullanılan ürünleri, pigment olmaya uygun olsa da kapsamaz.",
      ["Yağlı boyalarda dolgu maddesi olarak kullanılan bütün ürünleri kapsar.",
       "Yalnızca sentetik organik kökenli ve boyama gücü standardize edilmiş ürünleri kapsar.",
       "Kimyasal olarak belirli bileşikleri hiçbir durumda kapsamaz; bunlar Fasıl 28–29’dadır.",
       "Yalnızca perakende satılacak şekilde ambalajlanmış ürünleri kapsar."], "C",
      "Not 5, yağlı boyalarda dolgu maddesi olarak kullanılan ürünleri (boyayıcı pigment olarak kullanılmaya uygun olsun olmasın) “boyayıcı madde” tabirinin dışında tutar; 32.06 açıklama notu kaolin, talk, baryum sülfat gibi örnekleri kendi pozisyonlarına gönderir. Kimyasal olarak belirli bileşikler ise 32.03 ve 32.04’te açıkça kapsama alınmıştır.",
      "Fasıl 32 Not 5; Not 1(a); 32.06 Açıklama Notu."),
    # 16
    Q(T_NOT,
      "Fasıl 32 Not 6’ya göre 32.12 pozisyonundaki “ıstampacılığa mahsus varaklar” hangisidir?",
      "Baskıda kullanılan, metal veya pigmentten ince yapraklar (aglomere veya mesnet üzerinde)",
      ["Haddeleme veya dövme yoluyla elde edilen, kıymetli metalden ince yapraklar",
       "Daktilo makinelerinde kullanılan, mürekkep emdirilmiş dokuma şeritler",
       "Seramik eşyaya uygulanan ve pişirme sırasında camlaşan sırlar",
       "Mürekkep emdirilmiş, kutu içindeki ıstampa yastıkları"], "E",
      "Not 6, ıstampacılığa mahsus varakları; metal tozları veya pigmentlerin tutkal, jelatin gibi bağlayıcılarla aglomere edilmesinden ya da metal veya pigmentlerin mesnet yaprak üzerine tespitinden oluşan, kitap kapağı veya şapka şeridi baskısında kullanılan ince yapraklar olarak tanımlar. Dövme metal folyolar metaline göre, mürekkepli şerit ve ıstampalar 96.12’de, sırlar 32.07’dedir.",
      "Fasıl 32 Not 6; 32.12 Açıklama Notu (B); 32.15 Açıklama Notu."),
    # 17
    Q(T_NOT,
      "Fasıl 32 Not 1(a) kimyaca belirli yapıda izole bileşikleri fasıl dışında bırakır. Aşağıdakilerden hangisi bu hükmün istisnaları arasında <b>değildir</b>?",
      "32.11’deki müstahzar kurutucu maddeler",
      ["32.04’teki sentetik organik boyayıcı maddeler",
       "32.06’daki lüminofor olarak kullanılan inorganik ürünler",
       "32.12’deki perakende satılacak şekilde ambalajlanmış boyalar",
       "32.07’deki eritilmiş kuvartzdan elde edilmiş toz cam"], "A",
      "Not 1(a)’nın istisnaları 32.03 ve 32.04 maddeleri, 32.06’daki inorganik lüminoforlar, 32.07’de öngörülen şekillerde eritilmiş kuvartz veya silisten cam ve 32.12’deki perakende boyalardır. 32.11 açıklama notu ise kimyasal olarak belirli izole bileşikleri kurutucular pozisyonundan açıkça hariç tutar (Fasıl 28 veya 29).",
      "Fasıl 32 Not 1(a); 32.11 Açıklama Notu."),
    # 18 — GYK
    Q(T_GYK,
      "Ayrı kaplarda epoksi reçine ve sertleştiriciden oluşan, kullanım anında karıştırılacak, birlikte sunulan ve yalnız vernik olarak kullanılacağı açıkça belli olan solventsiz vernik takımı nasıl sınıflandırılır?",
      "Bölüm VI Not 3 uyarınca vernik olarak 32.10’da (GYK 1 ve 6)",
      ["GYK 3(b) uyarınca esas karakteri veren reçineye göre Fasıl 39’da",
       "Reçine Fasıl 39’da, sertleştirici kendi pozisyonunda ayrı ayrı",
       "GYK 3(c) uyarınca numara sırasına göre en son pozisyonda",
       "GYK 2(a) uyarınca tamamlanmamış boya olarak 32.08’de"], "D",
      "Bölüm VI Not 3, birlikte karıştırılmak üzere tasarlanmış, birlikte sunulan ve birbirini tamamlayan bileşenlerden oluşan setleri elde edilecek ürünün pozisyonunda sınıflandırır. 32.10 açıklama notu, sertleştiricisi ayrı kapta paketlenen solventsiz sıvı vernikleri sayar; yalnız vernik olarak kullanımı belli değilse ürün Fasıl 39’a giderdi.",
      "Bölüm VI Not 3; 32.10 Açıklama Notu (B)(4)."),
    # 19
    Q(T_GYK,
      "Bölüm VI açıklama notlarına göre, ön karıştırma yapılmaksızın birbirini izleyen şekilde kullanılmak üzere tasarlanmış ve perakende satışa sunulmuş, Bölüm VI ürünlerinden oluşan takımlar nasıl sınıflandırılır?",
      "Bölüm VI Not 3 uygulanmaz; genellikle GYK 3(b) ile sınıflandırılır.",
      ["Bölüm VI Not 3 uyarınca karışımdan elde edilecek ürünün pozisyonunda",
       "Perakende olsa bile her durumda bileşenler ayrı ayrı sınıflandırılır",
       "GYK 3(c) uyarınca numara sırasına göre en son pozisyonda",
       "GYK 4 uyarınca en çok benzeyen eşyanın pozisyonunda"], "B",
      "Bölüm VI Not 3 yalnız birlikte karıştırılması amaçlanan bileşenlere uygulanır. Açıklama notu, birbirini izleyen şekilde kullanılan takımlardan perakende satışa sunulanların genellikle GYK 3(b) ile, perakende olmayanların ise ayrı ayrı sınıflandırılacağını belirtir.",
      "Bölüm VI Not 3 ve Açıklama Notu; GYK 3(b)."),
    # 20 — Boşluk / eşleştirme
    Q(T_ESL,
      "Esası sentetik polimer olan boya ve vernikler susuz bir ortamda eriyor veya dağılıyorsa ……… pozisyonunda; sulu ortamda dağılıyor veya çözünüyorsa ……… pozisyonunda sınıflandırılır. Boşluklara sırasıyla hangisi gelmelidir?",
      "32.08 – 32.09",
      ["32.09 – 32.08", "32.08 – 32.10", "32.10 – 32.09", "32.09 – 32.10"], "C",
      "32.08 susuz ortamda, 32.09 sulu ortamda eriyen veya dağılan sentetik ya da kimyasal olarak tadil edilmiş tabii polimer esaslı boya ve vernikleri kapsar. 32.10 kurutucu yağ, tabii reçine, kauçuk (sentetik hariç) veya bitümen esaslı diğer boya ve verniklerin yeridir. “Sulu ortam” su veya su ile suda çözünen bir solventin karışımıdır.",
      "32.08 ve 32.09 pozisyon metinleri ve Açıklama Notları."),
    # 21
    Q(T_ESL,
      "Aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>doğrudur</b>?",
      "Enzim esaslı suni sama – 32.02",
      ["Debagat hülasası imalinde kullanılan kuru palamut – 32.01",
       "Gallik asit – 32.01",
       "Esasen debagat maddesi olmayan deri apresi – 32.02",
       "Kazein tannat – 32.01"], "A",
      "Derilerin yumuşatılmasında kullanılan, esası seçilmiş enzimler olan suni samalar 32.02’dedir. Debagat hülasası yapımında kullanılan ham bitkisel maddeler 14.04’te, gallik asit 29.18’de, esasen debagat maddesi olmayan deri apreleri 38.09’da, kazein tannat ise 35.01’dedir (Not 1(b)).",
      "32.01 ve 32.02 Açıklama Notları; Fasıl 32 Not 1(b)."),
    # 22 — Çoktan-çoğa
    Q(T_COK,
      "Aşağıdakilerden hangileri 32.06 pozisyonunda sınıflandırılır? I. Kalsiyum ve baryum sülfatla karıştırılmış, pigment olarak kullanılan titanyum dioksit II. Karışmamış ve yüzey işlem görmemiş titanyum dioksit III. Çok küçük miktarda sentetik organik boyayıcı katılarak renkleri canlandırılmış boyayıcı topraklar IV. Yağlı boyalarda dolgu maddesi olarak kullanılan talk",
      "I ve III",
      ["I ve II", "II ve IV", "I, III ve IV", "III ve IV"], "E",
      "32.06 açıklama notu, diğer maddelerle karıştırılmış veya yüzey işlem görmüş titanyum dioksit pigmentlerini (I) ve renkleri sentetik organik boyayla canlandırılmış boyayıcı toprakları (III) kapsar. Karışmamış ve yüzey işlem görmemiş titanyum dioksit 28.23’te (II), dolgu maddesi olarak talk 25.26’dadır (IV; Not 5).",
      "32.06 Açıklama Notu; Fasıl 32 Not 5."),
    # 23
    Q(T_COK,
      "Aşağıdaki ifadelerden hangileri doğrudur? I. Tırnak cilası tipindeki vernikler 32.08’de yer alır. II. Statik elektrikle veya ısı etkisiyle uygulanan, esası plastik olan toz boyalar Fasıl 39’dadır. III. Fotokopi makinelerinde kullanılan, toner ve taşıyıcıdan oluşan devolope ediciler 37.07’dedir. IV. Toz, granül veya pul şeklinde olmayan kütle halindeki emaye cam 32.07’dedir.",
      "II ve III",
      ["I ve IV", "I, II ve III", "II, III ve IV", "III ve IV"], "C",
      "32.10 açıklama notu plastik esaslı toz boyaları Fasıl 39’a (II), 32.15 açıklama notu fotokopi devolope edicilerini 37.07’ye (III) gönderir. Tırnak cilası tipi vernikler 33.04’tedir (I yanlış); 32.07 açıklama notu toz, granül veya pul dışındaki emaye camı 70.01’e verir (IV yanlış).",
      "32.07, 32.08, 32.10 ve 32.15 Açıklama Notları."),
    # 24 — Senaryo
    Q(T_SEN,
      "Bir plastik fabrikası, kütle halindeki plastiklerin boyanmasında hammadde olarak kullanmak üzere; sentetik organik pigmentlerin plastik içinde konsantre dispersiyonu halindeki küçük parçacıklardan oluşan renk konsantresi ithal etmektedir. Eşya hangi pozisyonda sınıflandırılır?",
      "32.04",
      ["39.26", "32.06", "32.12", "38.24"], "B",
      "32.04 açıklama notu, sentetik organik boyayıcı maddelerin plastikler, kauçuk veya plastifiyerler içindeki konsantre dispersiyonlarını ismen sayar; Not 3 de esası boyayıcı olan ve başka maddeleri boyamada kullanılan müstahzarları 32.03–32.06’ya verir. Pigment inorganik olsaydı 32.06 olurdu; 32.12 ise boya imaline mahsus susuz ortamdaki sıvı veya hamur pigmentler içindir.",
      "Fasıl 32 Not 3; 32.04 Açıklama Notu (I)(C)."),
    # 25
    Q(T_SEN,
      "Bir mobilya atölyesi; white spirit içinde kobalt naftenatın konsantre çözeltisinden oluşan, boya ve verniklerdeki kurutucu yağın oksidasyonunu kolaylaştırarak kurumayı hızlandıran bir ürün satın almaktadır. Ürün kimyasal olarak belirli tek bir bileşik değildir. Eşya hangi pozisyonda sınıflandırılır?",
      "32.11",
      ["38.06", "32.08", "15.18", "38.14"], "D",
      "Müstahzar kurutucular (sikatifler) 32.11’dedir; açıklama notu white spirit içindeki kobalt naftenat çözeltisini örnek verir. Aynı not kaynatılmış yağları (15.18), kimyasal olarak belirli izole bileşikleri ve rezinatları (38.06) hariç tutar. Ürün boya veya vernik olmadığından 32.08’e, çözücü karışımı olmadığından 38.14’e girmez.",
      "32.11 pozisyon metni ve Açıklama Notu."),
]

modul = {
    "tur": "fasil",
    "fasil": 32,
    "baslik": "Debagatte veya boyacılıkta kullanılan hülasalar; tanenler ve türevleri; boyalar, pigmentler ve diğer boyayıcı maddeler; müstahzar boyalar ve vernikler; macunlar; mürekkepler",
    "bolum": "VI",
    "oz": {
        "vurgu": "Fasıl 32 iki soruyla çözülür: Eşya bir debagat veya boyayıcı madde mi (menşeine göre 32.01–32.06), yoksa bu maddelerden yapılmış hazır bir ürün mü (32.07–32.15)? Hazır boya ve verniklerde bağlayıcıya ve ortama bakılır: sentetik polimer + susuz ortam 32.08, sentetik polimer + sulu ortam 32.09, diğerleri 32.10.",
        "maddeler": [
            "Kimyasal olarak belirli izole bileşikler Fasıl 28–29’dadır; istisnalar 32.03–32.04 boyayıcıları, 32.06 inorganik lüminoforları, 32.07 camları ve 32.12 perakende boyalarıdır.",
            "Not 3: esası boyayıcı madde olan ve başka maddeleri boyamada veya boyayıcı müstahzar imalinde kullanılan müstahzarlar 32.03–32.06’dadır; boya imaline mahsus susuz ortamdaki pigmentler 32.12’dedir.",
            "Perakende ev boyaları 32.12; ressam, eğitim, afiş ve eğlence boyaları 32.13; makyaj boyaları 33.04, saç boyaları 33.05.",
            "Macunlar ve ateşe dayanıklı olmayan sıvalar 32.14; mürekkepler konsantre veya katı olsa bile 32.15.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Debagatte kullanılan bitkisel hülasa veya tanen mi? Sentetik veya mineral debagat maddesi, suni sama mı?", "<b>32.01</b> · <b>32.02</b>"],
            ["2", "Seramik, emaye, cam sanayiine mahsus müstahzar pigment, sır, cam haline gelebilen terkip ya da toz, granül, pul cam mı?", "<b>32.07</b>"],
            ["3", "Boyayıcı madde veya Not 3 müstahzarı mı?", "Bitkisel/hayvansal <b>32.03</b> · sentetik organik <b>32.04</b> · lak <b>32.05</b> · inorganik <b>32.06</b>"],
            ["4", "39.01–39.13 polimerinin uçucu organik çözücüdeki çözeltisi, çözücü %50’den fazla mı?", "<b>32.08</b> (≤ %50 ise Fasıl 39; kollodyon 39.12)"],
            ["5", "Boya veya vernik; esası sentetik/tadil edilmiş tabii polimer mi?", "Susuz ortam <b>32.08</b> · sulu ortam <b>32.09</b>"],
            ["6", "Diğer boya ve vernik mi? (yağlı, tabii reçine, kauçuk, bitümen esaslı; distemper; deri finisaj pigmenti)", "<b>32.10</b>"],
            ["7", "Müstahzar kurutucu (sikatif) mı?", "<b>32.11</b>"],
            ["8", "Boya imaline mahsus susuz ortamda sıvı/hamur pigment, ıstampacılık varağı veya perakende boyayıcı mı?", "<b>32.12</b>"],
            ["9", "Ressam, öğrenci, tabelacı boyası; renk değiştirici veya eğlence boyası mı? (tablet, tüp, kavanoz…)", "<b>32.13</b>"],
            ["10", "Macun, reçineli çimento, kalafat bileşiği, boyacı dolgusu, ateşe dayanıklı olmayan sıva mı?", "<b>32.14</b>"],
            ["11", "Baskı, yazı, çizim veya diğer mürekkep mi?", "<b>32.15</b>"],
        ],
        "dipnot": "* İki bileşenli boya, vernik ve macunlar birlikte kullanılacakları belli, birlikte sunulmuş ve birbirini tamamlayıcı ise ürünün pozisyonunda sınıflandırılır (Bölüm VI Not 3). Kullanımda sertleştirici gerekiyorsa sertleştiricinin bulunmaması bu sınıflandırmayı engellemez.",
    },
    "pozisyon_haritasi": [
        ["32.01", "Bitkisel debagat hülasaları; tanenler ve türevleri", "Bitkisel menşe; tannatlar", "Kebrako, mimoza hülasası, mazı palamudu taneni"],
        ["32.02", "Sentetik organik ve anorganik debagat maddeleri; ön debagat enzim müstahzarları", "Sentetik veya mineral; suni samalar", "Sentan, krom tuzu esaslı debagat maddesi"],
        ["32.03", "Bitkisel veya hayvansal menşeli boyayıcı maddeler", "Menşe; kimyasal yapı önemsiz", "Koşnil hülasası, tabii indigo, safran, klorofil"],
        ["32.04", "Sentetik organik boyayıcılar; floresanlı aydınlatıcılar; organik lüminoforlar", "Sentetik organik; kimyasal yapı önemsiz", "Azo boya, sentetik indigo, reaktif boya, optik beyazlatıcı"],
        ["32.05", "Boyayıcı laklar", "Boyayıcının bir baz üzerine tespiti", "Koşnil kırmızısı lakı, karmen lakı"],
        ["32.06", "Diğer (inorganik) boyayıcılar; inorganik lüminoforlar", "Mineral pigment müstahzarları", "Titandioksit pigmenti, ultramarin, litopon, Prusya mavisi"],
        ["32.07", "Seramik, emaye, cam sanayii müstahzarları; toz, granül, pul cam", "Uygulamadan sonra yüksek ısı", "Sır, cam haline gelebilen terkip, frit, cam tozu"],
        ["32.08", "Sentetik polimer esaslı, susuz ortamda boya ve vernikler; Not 4 çözeltileri", "Çözücü ortam; %50 eşiği", "Solventli poliüretan vernik, alkid esaslı solventli boya"],
        ["32.09", "Sentetik polimer esaslı, sulu ortamda boya ve vernikler", "Su veya su + suda çözünen solvent", "Su bazlı akrilik plastik boya"],
        ["32.10", "Diğer boya ve vernikler; distemperler; deri finisaj pigmentleri", "Yağlı, tabii reçine, kauçuk, bitümen esaslı", "Yağlı vernik, gomalaka verniği, distemper"],
        ["32.11", "Müstahzar kurutucular (sikatifler)", "Kurutucu yağın oksidasyonunu hızlandırma", "White spirit içinde kobalt naftenat"],
        ["32.12", "Boya imaline mahsus susuz pigmentler; ıstampacılık varakları; perakende boyalar", "Konsantre dispersiyon; perakende ambalaj", "Alüminyum pul pastası, baskı folyosu, zarfta kumaş boyası"],
        ["32.13", "Resim, eğitim, afiş, renk değiştirici ve eğlence boyaları", "Tablet, tüp, kavanoz, çanak; takım halinde", "Suluboya takımı, tüpte yağlı boya, guaj"],
        ["32.14", "Macunlar, reçineli çimentolar; boyacı dolguları; ateşe dayanıklı olmayan sıvalar", "Kalın tabaka; mala, spatula, tabanca", "Camcı macunu, silikon mastik, kaporta dolgusu"],
        ["32.15", "Baskı, yazı, çizim ve diğer mürekkepler", "Konsantre veya katı olsa bile", "Baskı mürekkebi, çini mürekkebi, dolma kalem kartuşu"],
    ],
    "notlar": [
        ["Fasıl 32 Not 1", "Fasıl dışı: (a) kimyaca belirli izole elementler ve bileşikler (32.03, 32.04 maddeleri, 32.06 inorganik lüminoforlar, 32.07’deki eritilmiş kuvartz veya silisten cam ve 32.12’deki perakende boyalar hariç); (b) tannatlar ve 29.36–29.39, 29.41 veya 35.01–35.04 ürünlerinin diğer tanen türevleri; (c) asfalt sakızı ve diğer bitümenli sakızlar (27.15)."],
        ["Fasıl 32 Not 2", "Stabilize diazonyum tuzları ile azoik boya üretiminde kullanılan bağlayıcılardan oluşan karışımlar 32.04’tedir (izole diazonyum tuzları Fasıl 29)."],
        ["Fasıl 32 Not 3", "Esası boyayıcı madde olan ve herhangi bir maddeyi boyamada veya boyayıcı müstahzar imalinde katkı olarak kullanılan müstahzarlar 32.03–32.06’dadır (32.06 için 25.30 ve Fasıl 28 pigmentleri, metal pul ve tozları dahil). Ancak boya imaline mahsus susuz ortamdaki sıvı veya hamur pigmentler (32.12) ile 32.07, 32.08, 32.09, 32.10, 32.12, 32.13, 32.15 müstahzarları bu pozisyonlara girmez."],
        ["Fasıl 32 Not 4", "39.01–39.13 ürünlerinin uçucu organik çözücüler içindeki çözeltileri (kollodyon hariç), çözücü ağırlığı çözelti ağırlığının <b>%50’sinden fazla</b> ise 32.08’dedir; değilse Fasıl 39. Terebentin gibi yüksek kaynama noktalı çözücüler de uçucu organik çözücü sayılır."],
        ["Fasıl 32 Not 5", "“Boyayıcı madde” tabiri yağlı boyalarda dolgu maddesi olarak kullanılan ürünleri (boyayıcı pigment olmaya uygun olsun olmasın) kapsamaz."],
        ["Fasıl 32 Not 6", "“Istampacılığa mahsus varaklar”: kitap kapağı, şapka şeridi gibi baskılarda kullanılan; (a) metal tozları (kıymetli dahil) veya pigmentlerin tutkal, jelatin vb. bağlayıcıyla aglomere edilmesinden ya da (b) metal veya pigmentlerin herhangi bir maddeden mesnet yaprak üzerine tespitinden oluşan ince yapraklar."],
        ["Bölüm VI Not 3", "Birlikte karıştırılması tasarlanan, birlikte sunulan ve birbirini tamamlayan bileşenlerden oluşan setler, elde edilecek ürünün pozisyonunda sınıflandırılır (ör. iki bileşenli boya, vernik, macun). Birbirini izleyen şekilde kullanılan takımlara uygulanmaz; bunlar perakende ise genellikle GYK 3(b), değilse ayrı ayrı."],
        ["32.04 Açıklama Notu", "Sentetik organik boyalar sulandırılmış, karışık veya plastik, kauçuk içindeki konsantre dispersiyon halinde de buradadır. Boya olmayan ara ürünler (anilin, resorsinol vb.) Fasıl 29’dadır; boyayıcı özelliği için kullanılmayan maddeler (pikrik asit, bilirubin vb.) hariçtir."],
        ["32.06 Açıklama Notu", "Karışmamış, yüzey işlem görmemiş titanyum dioksit 28.23; canlandırılmamış boyayıcı topraklar ve mikalı demir oksitler 25.30; kimyaca belirli inorganik boyayıcılar Fasıl 28; metal pul ve tozları Bölüm XIV veya XV; yağlı boya dolguları (kaolin, talk, baryum sülfat) kendi pozisyonlarında."],
        ["32.08 Açıklama Notu", "Hariç: yüksek oranda dolgulu, mala ile uygulanan yüzey müstahzarları (32.14), baskı mürekkepleri (32.15), tırnak cilası tipi vernikler (33.04), perakende düzeltme sıvıları (38.24), kollodyonlar (39.12); net ağırlığı 1 kg’ı geçmeyen perakende tutkallar 35.06."],
        ["32.10 Açıklama Notu", "Solventsiz sıvı vernikler (epoksi, poliüretan) ve kauçuk esaslı vernikler ancak yalnız vernik olarak kullanımları belli ise buradadır; değilse Fasıl 39 veya 40. Plastik esaslı, ısıyla uygulanan toz boyalar Fasıl 39; ayakkabı temizlemeye mahsus beyazlatıcılar distemper olarak buradadır."],
        ["32.12 Açıklama Notu", "Perakende boyalar film tabakası oluşturmayan “ev boyaları”dır (elbise, ayakkabı, mobilya) ve laboratuvar boyalarını da kapsar. Hariç: 32.13 boyaları, baskı mürekkepleri (32.15), makyaj boyaları (33.04), saç boyaları (33.05), boya kalemleri ve pasteller (96.09). Dövme veya haddeleme metal folyolar metaline göre (71.08, 74.10, 76.07)."],
        ["32.15 Açıklama Notu", "Fotokopi devolope edicileri 37.07; mürekkep haznesi ve bilyalı uçlu kartuşlar 96.08 (yalnız dolma kalem kartuşları 32.15); mürekkepli şerit ve ıstampalar 96.12."],
    ],
    "sinir_komsulari": [
        ["Debagat hülasası imalinde kullanılan ham kabuk, palamut vb.", "14.04", "32.01 Açıklama Notu"],
        ["Gallik asit", "29.18", "32.01 Açıklama Notu"],
        ["Esasen debagat maddesi olmayan deri apresi, mordan", "38.09", "32.02 Açıklama Notu"],
        ["Karbon karası; fildişi karası ve hayvansal karalar", "28.03 / 38.02", "32.03 Açıklama Notu"],
        ["Karışmamış, yüzey işlem görmemiş titanyum dioksit", "28.23", "32.06 Açıklama Notu"],
        ["Canlandırılmamış boyayıcı topraklar; mikalı tabii demir oksit", "25.30", "32.06 Açıklama Notu"],
        ["Yağlı boya dolguları: kaolin, talk, tabii baryum sülfat", "25.07 / 25.26 / 25.11", "Fasıl 32 Not 5"],
        ["Asfalt macunu; dişçi çimentosu; ateşe dayanıklı harç", "27.15 / 30.06 / 38.16", "32.14 Açıklama Notu"],
        ["Tırnak cilası, sahne makyajı boyası; saç boyası", "33.04 / 33.05", "32.08 ve 32.12 Açıklama Notları"],
        ["Ayakkabı cilası ve kremi (“ayakkabı boyası”)", "34.05", "34.05 pozisyon metni"],
        ["Fotokopi devolope edicisi; perakende düzeltme sıvısı", "37.07 / 38.24", "32.15 ve 32.08 Açıklama Notları"],
        ["Kollodyon; çözücüsü ≤ %50 polimer çözeltisi; plastik toz boya", "39.12 / Fasıl 39", "Not 4; 32.08 ve 32.10 Açıklama Notları"],
        ["Kütle halinde emaye cam; mikro küreler", "70.01 / 70.18", "32.07 Açıklama Notu"],
        ["Dövme altın folyo; alüminyum folyo", "71.08 / 76.07", "32.12 Açıklama Notu"],
        ["Pastel ve boya kalemi; bilyalı uçlu kartuş; daktilo şeridi", "96.09 / 96.08 / 96.12", "32.13 ve 32.15 Açıklama Notları"],
    ],
    "tuzaklar": [
        "<b>Sulu mu susuz mu?</b> Aynı akrilik polimer esaslı boya çözücü ortamda ise 32.08, su bazlı ise 32.09. Yağlı, tabii reçine, sentetik olmayan kauçuk veya bitümen esaslılar 32.10.",
        "<b>%50 çözücü eşiği.</b> 39.01–39.13 polimerlerinin uçucu organik çözücüdeki çözeltisi, çözücü ağırlığı %50’yi geçerse 32.08; geçmezse Fasıl 39. Kollodyon her oranda 39.12.",
        "<b>Perakende ev boyası ≠ ressam boyası.</b> Elbise, ayakkabı, mobilya için küçük zarf veya şişedeki boyayıcılar 32.12; tüp, tablet, çanaktaki resim, eğitim, afiş boyaları 32.13.",
        "<b>“Ayakkabı boyası” 34.05’tir.</b> 34.05 metni ayakkabı boya ve cilalarını ismen sayar; 32.05 (boyayıcı laklar) bu soruda çeldiricidir.",
        "<b>Kozmetik boyalar Fasıl 33’tedir.</b> Tırnak cilası tipi vernikler ve sahne makyajı boyaları 33.04, saç boyaları 33.05.",
        "<b>Sentetik organikte kimyasal yapı önemsiz, inorganikte önemli.</b> Sentetik organik boya kimyasal olarak belirli olsa da 32.04’tedir; karışmamış ve yüzey işlem görmemiş titanyum dioksit ise 28.23, pigment olarak hazırlanmışı 32.06.",
        "<b>Dolgu maddesi boyayıcı değildir.</b> Yağlı boyalarda dolgu olarak kullanılan kaolin, talk, baryum sülfat (Not 5) kendi pozisyonlarındadır.",
        "<b>Lak iki anlamlıdır.</b> Boyayıcı lak (bir baz üzerine tespit edilmiş boyayıcı) 32.05; vernik anlamındaki laklar 32.08–32.10; Japon (Çin) lakı 13.02.",
        "<b>Mürekkep katı olsa da mürekkeptir.</b> Toz, tablet veya çubuk halindeki konsantre mürekkep 32.15; ama bilyalı uçlu kartuş 96.08, daktilo şeridi 96.12, fotokopi devolope edicisi 37.07.",
        "<b>Macun ile boya farkı dolgu oranıdır.</b> Yüksek oranda dolgu içeren, mala veya spatula ile kalın uygulanan yüzey müstahzarları plastik esaslı olsa da 32.14’tedir.",
    ],
    "hafiza": {
        "kanca": "TABAK – RENK – FIRIN – KUTU – KURUT – RAF – MACUN – HOKKA",
        "aciklama": "<b>TABAK</b>hane 32.01–32.02 · <b>RENK</b> dolabı: doğal 03, sentetik 04, lak 05, mineral 06 · seramik <b>FIRIN</b>ı 32.07 · boya <b>KUTU</b>ları: solventli 08, su bazlı 09, diğer 10 · <b>KURUT</b>ucu şişe 32.11 · mağaza <b>RAF</b>ı: perakende boya 12, ressam tüpü 13 · <b>MACUN</b> tabancası 32.14 · mürekkep <b>HOKKA</b>sı 32.15. Bir deri-boya atölyesini kapıdan arka depoya bu sırayla gezin.",
    },
    "sinav_odagi": [
        "Fasıl 32 notlarının doğrudan sorulması: 39.01–39.13 ürünlerinin uçucu organik çözücüdeki çözeltilerinde %50 eşiği ve 32.08; 27.10, 34.03, 38.14 çeldirici.",
        "Benzer adlı ürünlerde doğru fasıl: “ayakkabı boyası”nın 34.05’te olduğu; 32.05, 35.01 ve 38.24 çeldirici olarak kullanılmıştır.",
        "“Boya” kelimesine rağmen saç boyasının Fasıl 33’te yer aldığı “farklı fasıl” soruları.",
        "Bölüm düzeyinde gruplama: yağlı boyanın şampuan ve haşere öldürücüyle aynı bölümde (Bölüm VI), klinkerin farklı bölümde olduğu.",
        "Set (GYK 3(b)) sorularında resim fırçası, suluboya ve resim defterinin perakende set oluşturabildiği; ilgisiz eşya birlikteliklerinin set sayılmadığı.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveli’nin 32. fasıl notlarına göre; 39.01 ila 39.13 pozisyonlarında belirtilen ürünlerin herhangi birinden oluşan çözeltiler (kollodyumlar hariç), uçucu organik çözücüler içinde, çözücünün ağırlığı çözeltinin ağırlığının %50’sinden fazla olduğu zaman hangi pozisyonda yer alır?",
            "secenekler": ["27.10", "32.08", "34.03", "38.14"],
            "cevap": "B",
            "aciklama": "Fasıl 32 Not 4 bu çözeltileri 32.08’e verir; çözücü oranı %50’yi geçmiyorsa çözelti Fasıl 39’da kalır, kollodyonlar ise her oranda 39.12’dedir.",
        },
        {
            "soru": "Türk Gümrük Tarife Cetveline göre ayakkabı boyası hangi tarife pozisyonunda sınıflandırılır?",
            "secenekler": ["32.05", "35.01", "34.05", "38.24"],
            "cevap": "C",
            "aciklama": "34.05 pozisyon metni ayakkabı, deri ve köselede kullanılan boya, cila ve benzeri müstahzarları ismen sayar. 32.05 boyayıcı laklar içindir; “boya” kelimesi eşyayı tek başına Fasıl 32’ye taşımaz.",
        },
    ],
    "ozet": [
        "Önce kimyasal yapı: izole belirli bileşik Fasıl 28–29’dadır (istisnalar 32.03, 32.04, 32.06 lüminofor, 32.07 cam, 32.12 perakende).",
        "Debagat: bitkisel hülasa ve tanen 32.01; sentetik, mineral, suni sama 32.02.",
        "Boyayıcı: doğal 32.03, sentetik organik 32.04, lak 32.05, inorganik 32.06.",
        "Boya ve vernik: sentetik polimer + susuz 32.08; + sulu 32.09; diğerleri 32.10. Çözücü %50’yi aşmazsa Fasıl 39.",
        "Perakende ev boyası 32.12; ressam, eğitim, afiş boyası 32.13.",
        "Macun 32.14; mürekkep 32.15; kozmetik boyalar Fasıl 33; ayakkabı cilası 34.05.",
    ],
    "sorular": sorular,
}

if __name__ == "__main__":
    harfler = Counter(q["cevap"] for q in sorular)
    assert len(sorular) == 25, len(sorular)
    assert all(harfler[h] == 5 for h in "ABCDE"), harfler
    with open(CIKTI, "w", encoding="utf-8") as f:
        json.dump(modul, f, ensure_ascii=False, indent=1)
    print("yazıldı:", CIKTI, dict(harfler))
