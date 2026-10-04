#!/usr/bin/env python3
"""Karma test 3 üretici: KITAP/karma/karma_03.json"""
import json
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_03.json")


def S(soru, secenekler, cevap, tip, gerekce, dayanak, fasil):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


sorular = [
    # 1 — Genel / Tarife yapısı (C)
    S("Tarife Cetvelinin bölüm–fasıl yapısına göre aşağıdaki fasıl – bölüm eşleştirmelerinden hangisi "
      "<b>yanlıştır</b>?",
      ["Fasıl 49 – Bölüm X",
       "Fasıl 67 – Bölüm XII",
       "Fasıl 43 – Bölüm IX",
       "Fasıl 70 – Bölüm XIII",
       "Fasıl 92 – Bölüm XVIII"],
      "C", "Tarife yapısı",
      "Fasıl 43 (kürkler) VIII. Bölümün (41–43) son faslıdır; IX. Bölüm Fasıl 44 ile başlar. Fasıl 49 X. "
      "(47–49), Fasıl 67 XII. (64–67), Fasıl 70 XIII. (68–70) ve Fasıl 92 XVIII. (90–92) bölümlerin son "
      "fasıllarıdır; tuzak, bölüm sınırındaki fasıllardır.",
      "Tarife Cetveli İçindekiler (bölüm–fasıl dizilişi).", "Genel"),

    # 2 — Fasıl 3 / Eşya → 4’lü pozisyon (A)
    S("Tarife Cetveline göre, balığın gövdesinden ayrılmış, insanların yemesine elverişli, tuzlanarak "
      "kurutulmuş balık yüzme keseleri hangi pozisyonda sınıflandırılır?",
      ["03.05", "05.11", "03.02", "05.04", "16.04"],
      "A", "Eşya → 4’lü pozisyon",
      "03.05 Açıklama Notu, gövdeden ayrılmış yenilebilir balık sakatatını (yüzme keseleri dahil) kurutulmuş, "
      "tuzlanmış veya tütsülenmiş halde bu pozisyona alır. Taze olsalardı 03.02’de kalırdı; yenilemeyenler "
      "05.11’e gider, 05.04 ise balıklarınki hariç mideleri kapsar.",
      "03.05 Açıklama Notu; 05.04 pozisyon metni.", 3),

    # 3 — Fasıl 62 / Fasıl-Bölüm bulma (B)
    S("Pamuklu dokunmuş mensucattan dikilmiş, karnaval ve maskeli balolarda giyilmek üzere hazırlanmış "
      "palyaço kostümü Tarife Cetvelinin hangi faslında yer almaktadır?",
      ["Fasıl 61", "Fasıl 62", "Fasıl 63", "Fasıl 95", "Fasıl 96"],
      "B", "Fasıl/Bölüm bulma",
      "Fasıl 95 Not 1(e), dokumaya elverişli maddelerden 61 veya 62. fasıldaki karnaval giyim eşyasını "
      "Fasıl 95 dışında bırakır. Kostüm dokunmuş (örülmemiş) mensucattan olduğundan Fasıl 62’dedir; tuzak, "
      "eğlence eşyası diye 95.05’i seçmektir.",
      "Fasıl 95 Not 1(e); Fasıl 62 Not 1.", 62),

    # 4 — Fasıl 96 / Eşya → 4’lü pozisyon (A)
    S("Tarife Cetveline göre, terzilerin dikilen giysiyi vücuda uydurmak için kullandığı, maşe kartondan "
      "kalıplanıp dokumaya elverişli maddeyle kaplanmış ve yalnızca gövde kısmından oluşan terzi mankeni "
      "hangi pozisyonda sınıflandırılır?",
      ["96.18", "90.23", "95.03", "48.23", "63.07"],
      "A", "Eşya → 4’lü pozisyon",
      "96.18 Açıklama Notu, maşe karton, alçı veya plastikten kalıplanıp çoğu kez dokumaya elverişli maddeyle "
      "kaplanan terzi mankenlerini açıkça sayar. Yalnız gösteri amaçlı modeller 90.23’e, yapma bebekler "
      "Fasıl 95’e gider; maddeye göre sınıflandırma yapılmaz.",
      "96.18 Açıklama Notu.", 96),

    # 5 — Fasıl 9 / Farklı-aynı pozisyon (D)
    S("Aşağıdaki seçeneklerin hangisinde aynı 4’lü pozisyonda yer <b>almayan</b> bir eşya bulunmaktadır?",
      ["Küçük Hindistan cevizi – küçük Hindistan cevizi kabuğu – kakule",
       "Rezene tohumu – Çin anasonu – ardıç meyvesi",
       "Zerdeçal – safran – kekik",
       "Bütün halde vanilya – öğütülmüş vanilya – vanilya şekeri",
       "Karanfil sapları – karanfil ağacının meyveleri – kurutulmuş karanfil çiçekleri"],
      "D", "Farklı/aynı pozisyon veya fasıl",
      "09.05 Açıklama Notu vanilya şekerini bu pozisyon dışında bırakır (17.01 veya 17.02); vanilya ezilmiş "
      "olsun olmasın 09.05’tedir. Diğer üçlüler sırasıyla 09.08, 09.09, 09.10 ve 09.07’de bir aradadır.",
      "09.05, 09.07, 09.08, 09.09 ve 09.10 Açıklama Notları.", 9),

    # 6 — Fasıl 73 / Olumsuz teşhis (E)
    S("Aşağıdaki demir veya çelikten mamul eşyalardan hangisi Tarife Cetvelinin 73. faslında "
      "<b>yer almaz</b>?",
      ["Ağaca tırmanmaya yarayan demirler",
       "Hayvanlar için burun halkası",
       "Hasta yataklarına mahsus sürgü",
       "Dökme demirden gemi babası",
       "Arazi ölçmede kullanılan mesaha zinciri"],
      "E", "Olumsuz teşhis",
      "73.15 Açıklama Notu arazi ölçme zincirlerini zincir pozisyonu dışında bırakır; mesaha zincirleri "
      "90.15’tedir. Tırmanma demirleri ve burun halkaları 73.26’da, hasta sürgüleri 73.24’te, dökme gemi "
      "babaları 73.25’te sayılmıştır.",
      "73.15, 73.24, 73.25 ve 73.26 Açıklama Notları; 90.15 Açıklama Notu.", 73),

    # 7 — GYK (B)
    S("Kakao yağının, başlığında katı ve sıvı yağlara yer verilen Fasıl 15 yerine 18.04 pozisyonunda "
      "sınıflandırılması aşağıdakilerden hangisinin gereğidir?",
      ["GYK 2(b) – kakao yağı karışım halinde bir yağ sayıldığından",
       "GYK 1 – başlıklar gösterici olup Fasıl 15 notu onu dışarıda bıraktığından",
       "GYK 3(a) – 18.04 eşyayı daha özel bir şekilde tanımladığından",
       "GYK 3(b) – eşyaya esas niteliğini kakao maddesi verdiğinden",
       "GYK 4 – kakao yağı en çok kakao ürünlerine benzediğinden"],
      "B", "Genel Yorum Kuralı",
      "GYK 1’e göre bölüm ve fasıl başlıkları yalnızca gösterici niteliktedir; sınıflandırma pozisyon "
      "metinleri ve notlarla yapılır. Fasıl 15 Not 1(b) kakao yağını 18.04’e gönderdiğinden GYK 3 veya 4’e "
      "başvurulmaz.",
      "GYK 1; Fasıl 15 Not 1(b); 18.04 pozisyon metni.", "GYK"),

    # 8 — Fasıl 21 / Eşya → 4’lü pozisyon (C)
    S("Tarife Cetveline göre, sodyum bikarbonat ile tartarik asit karışımına nişasta katılarak hazırlanan ve "
      "pasta ile bisküvi hamurlarının kabartılmasında kullanılan kabartma tozu hangi pozisyonda "
      "sınıflandırılır?",
      ["28.36", "21.06", "21.02", "38.24", "11.08"],
      "C", "Eşya → 4’lü pozisyon",
      "21.02 pozisyon metni ve Açıklama Notu, sodyum bikarbonat, tartarik asit veya fosfat gibi kimyasalların "
      "(nişasta katılmış olsun olmasın) karışımından oluşan hazırlanmış kabartma tozlarını kapsar. Karışım "
      "olduğundan 28.36’ya, özel pozisyonu bulunduğundan 21.06 veya 38.24’e girmez.",
      "21.02 pozisyon metni ve Açıklama Notu.", 21),

    # 9 — Fasıl 34 / Olumsuz teşhis (E)
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 34. faslında <b>yer almaz</b>?",
      ["Metallerin parlatılmasında kullanılan, elmas tozu içeren müstahzar",
       "Tel çekmede kullanılmak üzere hazırlanmış, suda çözünen sınai sabun",
       "Sütçülükte ekipmanın yağdan arındırılmasında kullanılan, sodyum karbonat esaslı temizleyici",
       "Takma diş kalıbı almak için kullanılan, at nalı şeklindeki dişçi mumu",
       "Tekne ve sarnıçların dezenfeksiyonunda kullanılan, kükürtle işlem görmüş fitiller"],
      "E", "Olumsuz teşhis",
      "34.06 Açıklama Notu, kükürtle muamele edilmiş şerit, fitil ve mumları ışık mumu saymaz; bunlar 38.08’dedir. "
      "Elmas tozlu parlatıcılar 34.05’te, tel çekme sabunları 34.01’de, sütçülükteki yağ gidericiler 34.02’de, "
      "at nalı biçimli dişçi mumları 34.07’dedir.",
      "34.06 ve 38.08 Açıklama Notları; 34.01, 34.02, 34.05 ve 34.07 Açıklama Notları.", 34),

    # 10 — Fasıl 63 / Farklı-aynı pozisyon (D)
    S("Aşağıdaki hazır eşyadan hangisi diğerlerinden <b>farklı</b> bir tarife pozisyonunda yer alır? "
      "(Eşyanın tamamı dokunmuş mensucattan yapılmıştır.)",
      ["Çözgü uçları düğümlenmiş, dikdörtgen kesilmiş peynir sarmaya mahsus bez",
       "Pastayı süslemek için krema sıkmaya mahsus torba",
       "Elektrikçilerin kullandığı, giysi kemeri niteliği taşımayan iş kemeri",
       "Düğün törenlerinde kullanılmaya mahsus duvar örtüsü",
       "Kahve filtresi"],
      "D", "Farklı/aynı pozisyon veya fasıl",
      "63.04 Açıklama Notu, düğün veya cenaze gibi törenlerde kullanılan duvar örtülerini mefruşat eşyası "
      "sayar. Peynir bezi, krema sıkma torbası, meslek kemerleri ve kahve filtreleri 63.07 Açıklama Notunda "
      "diğer hazır eşya olarak sayılmıştır.",
      "63.04 ve 63.07 Açıklama Notları.", 63),

    # 11 — Fasıl 85 / Sıralama (A)
    S("Aşağıda verilen eşyanın (I–V) Tarife Cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru "
      "dizilişi hangisidir?<br/>I. Elektrikli saç kurutma makinesi<br/>II. Kendinden elektrik motorlu tıraş "
      "makinesi<br/>III. Elektrik arkıyla çalışan kaynak makinesi<br/>IV. Elektrikli kapı zili<br/>"
      "V. Kurşun asitli akümülatör",
      ["V – II – III – I – IV",
       "II – V – III – I – IV",
       "V – II – I – III – IV",
       "V – III – II – I – IV",
       "V – II – III – IV – I"],
      "A", "Sıralama",
      "Akümülatör 85.07, tıraş makinesi 85.10, ark kaynak makinesi 85.15, saç kurutma makinesi 85.16, "
      "elektrikli zil 85.31’dedir. Tuzak, berber cihazlarını (85.10 ve 85.16) ardışık sanıp kaynak "
      "makinesinin araya girdiğini gözden kaçırmaktır.",
      "85.07, 85.10, 85.15, 85.16 ve 85.31 pozisyon metinleri.", 85),

    # 12 — GYK (E)
    S("Perakende satış için, bu tür eşyanın ambalajında normal olarak kullanılan ve tekrar kullanılmaya "
      "elverişli olduğu açıkça belli olmayan cam kavanozlar içinde sunulan reçelin, kavanozlarıyla birlikte "
      "sınıflandırılması hangi seçenekte doğru verilmiştir?",
      ["Reçel 20.07’de, kavanoz 70.10’da ayrı ayrı – GYK 1",
       "20.07 – GYK 5(a)",
       "70.10 – GYK 3(c)",
       "20.07 – GYK 3(b)",
       "20.07 – GYK 5(b)"],
      "E", "Genel Yorum Kuralı",
      "GYK 5(b) uyarınca eşyanın ambalajında normal olarak kullanılan ve tekrar kullanıma elverişli olduğu "
      "açıkça belli olmayan kavanoz, reçelle birlikte 20.07’de sınıflandırılır. 5(a) belli eşyaya göre "
      "şekillendirilmiş uzun ömürlü mahfazalara, 3(b) takımlara ilişkindir.",
      "GYK 5(b) Açıklama Notu (IV); 20.07 pozisyon metni.", "GYK"),

    # 13 — Fasıl 64 / Eşya → 4’lü pozisyon (D)
    S("Tarife Cetveline göre, dış tabanı kauçuktan olan ve yüzünün tamamı tüyleri üzerinde bulunan kürkten "
      "yapılmış kışlık bot hangi pozisyonda sınıflandırılır?",
      ["64.02", "64.03", "64.04", "64.05", "43.03"],
      "D", "Eşya → 4’lü pozisyon",
      "64.05 Açıklama Notu, dış tabanı kauçuk veya plastik olup yüzü kauçuk, plastik, deri veya dokumaya "
      "elverişli madde dışındaki maddeden yapılan ayakkabıları kapsar. Kürk, Fasıl 64 anlamında deri "
      "(41.07, 41.12–41.14) değildir; ayakkabılar Fasıl 43 dışındadır.",
      "Fasıl 64 Not 3(b) ve 4(a); 64.05 Açıklama Notu; Fasıl 43 Not 2.", 64),

    # 14 — Fasıl 39 / Fasıl notu · Tanım-Eşik (B)
    S("Fasıl 39 Not 11’e göre aşağıdaki plastik eşyadan hangisi 39.25 pozisyonunda <b>yer almaz</b>?",
      ["Dükkân ve atölyelerde montaj ve tesisat işleri için kullanılan büyük raflar",
       "Kapasitesi 250 litre olan su deposu",
       "Yağmur olukları ve bunların donanımları",
       "Venedik kepenkleri ve benzeri panjurlar",
       "Güvercinlik ve küçük kubbe gibi süs mahiyetindeki mimari motifler"],
      "B", "Fasıl notu · Tanım/Eşik",
      "Not 11(a), sarnıç, tank ve benzeri kapları ancak kapasiteleri 300 litreyi geçtiğinde 39.25’e alır; "
      "250 litrelik depo bu pozisyona giremez. Büyük raflar (g), oluklar (c), kepenk ve panjurlar (f) ile "
      "mimari süs motifleri (h) notta açıkça sayılmıştır.",
      "Fasıl 39 Not 11.", 39),

    # 15 — Fasıl 15 / Olumsuz teşhis (C)
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 15. faslında <b>sınıflandırılmaz</b>?",
      ["Atlardan elde edilen katı yağ",
       "İyice haşlanmış yumurtadan çıkarılan yumurta sarısı sıvı yağı",
       "Piridin bazları içeren, bazen “kemik yağı” denilen Dippel yağı",
       "Yapağı yağının buhar damıtma ve preslemeyle ayrılan sıvı kısmı (yapağı yağı oleini)",
       "İpek böceği krizalitlerinden çıkarılan sıvı yağ"],
      "C", "Olumsuz teşhis",
      "15.06 Açıklama Notu, esas itibarıyla piridin bazları içeren ve bazen kemik yağı denilen Dippel yağını "
      "38.24’e gönderir. At yağı, yumurta sarısı yağı ve krizalit yağı 15.06’da, yapağı yağı oleini "
      "15.05’tedir; tuzak, “kemik yağı” adıdır.",
      "15.05 ve 15.06 Açıklama Notları.", 15),

    # 16 — Fasıl 53 / Pozisyon → eşya (E)
    S("Aşağıdakilerin hangisinde sayılan liflerin tümü 53.03 pozisyonunda sınıflandırılır?",
      ["Beyaz jüt – rami – Çin jütü (abutilon)",
       "Queensland kendiri (Sida) – Mauritius kendiri – Rozella kendiri",
       "Urena lobata lifleri – henequen – kırmızı jüt (Tossa)",
       "Kenaf – yukka lifleri – Thespesia lifleri",
       "Isırgan otu lifleri – katırtırnağı lifleri – Sunn kendiri (Crotalaria juncea)"],
      "E", "Pozisyon → eşya",
      "53.03 Açıklama Notu ısırgan otu, katırtırnağı ve Crotalaria juncea (Sunn) liflerini çift çenekli bitki "
      "gövdesi lifleri olarak sayar. Rami çift çenekli olsa da 53.05’te; Mauritius kendiri, henequen ve yukka "
      "da 53.05’te yer alır.",
      "53.03 ve 53.05 Açıklama Notları.", 53),

    # 17 — GYK (A)
    S("Tüm parçaları aynı kolide birlikte sunulan, montajı yalnızca cıvata ve somunlarla yapılacak demonte "
      "haldeki tek tekerlekli el arabası hangi pozisyonda ve hangi Genel Yorum Kuralları uyarınca "
      "sınıflandırılır?",
      ["87.16 – GYK 1 ve 2(a)",
       "87.16 – GYK 1 ve 3(b)",
       "87.16 – GYK 2(b)",
       "Her parça kendi pozisyonunda – GYK 1",
       "73.26 – GYK 3(c)"],
      "A", "Genel Yorum Kuralı",
      "El arabaları 87.16 Açıklama Notunda elle hareket ettirilen taşıtlar arasında sayılır. GYK 2(a), "
      "parçaları yalnızca bağlantı elemanlarıyla birleştirilecek demonte eşyayı monte edilmiş eşyayla aynı "
      "pozisyona alır; takım veya karışım olmadığından 3(b) ve 2(b) uygulanmaz.",
      "GYK 1; GYK 2(a) Açıklama Notu (VII); 87.16 Açıklama Notu.", "GYK"),

    # 18 — Fasıl 84 / Olumsuz teşhis (C)
    S("Aşağıdakilerden hangisi 84.38 pozisyonunda <b>sınıflandırılmaz</b>?",
      ["Ekmek hamurunu mekanik olarak eşit parçalara bölen hamur bölme makinesi",
       "Badem gibi sert maddelerin üzerini şekerle kaplayan döner draje tavası",
       "Makarna ve pasta hamurlarını yufka halinde açmaya mahsus makine",
       "Çikolata hamurunun bileşenlerini birbirine iyice nüfuz ettiren “conche” makinesi",
       "Şeker kamışını yüksek hızda dönen bıçaklarla lif haline getiren makine"],
      "C", "Olumsuz teşhis",
      "84.38 Açıklama Notu, makarna ve pasta hamurlarını yufka halinde açmaya mahsus makineleri bu pozisyon "
      "dışında bırakır (84.20). Hamur bölme makineleri, draje tavaları, conche makineleri ve şeker kamışını "
      "lif haline getiren makineler notta 84.38 kapsamında sayılmıştır.",
      "84.38 Açıklama Notu; 84.20 pozisyon metni.", 84),

    # 19 — Fasıl 29 / Çoktan-çoğa-Eşleştirme (D)
    S("Tarife Cetveline göre; kimyaca belirli yapıdaki salisilik asit ……, karabuğdayda bulunan bir glikozit "
      "olan rutin (rutosit) ……, Ephedra bitkisinde bulunan bir alkaloit olan efedrin ise …… pozisyonunda "
      "sınıflandırılır. Boşlukları sırasıyla tamamlayan seçenek hangisidir?",
      ["29.18 – 29.36 – 29.39",
       "29.07 – 29.38 – 29.39",
       "29.18 – 29.38 – 29.37",
       "29.18 – 29.38 – 29.39",
       "29.16 – 29.36 – 29.39"],
      "D", "Çoktan-çoğa / Eşleştirme",
      "Salisilik asit ek oksijen fonksiyonlu karboksilik asit olarak 29.18’de; rutin, “vitamin P” denilse de "
      "29.36 Açıklama Notu gereği glikozit olarak 29.38’de; efedrin alkaloit olarak 29.39’dadır. Fenol "
      "yapısı 29.07’yi, vitamin adı 29.36’yı çağrıştırır.",
      "29.18, 29.38 ve 29.39 Açıklama Notları; 29.36 Açıklama Notu (hariç tutulanlar).", 29),

    # 20 — Fasıl 86 / Senaryo (B)
    S("Bir demiryolu işletmesi şu özelliklere sahip bir taşıt ithal etmektedir:<br/>"
      "• Raylar üzerinde hareket eden, kendinden hareketli olmayan bir vagondur.<br/>"
      "• Üzerine sabit olarak beton karıştırıcısı (betonyer) monte edilmiştir.<br/>"
      "• Elektrikli trenlere ait havai hatları taşıyan pilonların temellerine dökülecek betonu hazırlamakta "
      "kullanılır.<br/>"
      "• Yük veya yolcu taşımak için düzenlenmemiştir.<br/>"
      "Bu taşıt Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
      ["86.06", "86.04", "84.74", "86.05", "87.05"],
      "B", "Senaryo",
      "86.04 Açıklama Notu, demiryolu bakım ve servis taşıtları arasında havai hat pilonlarının temel betonunu "
      "hazırlayan betonyerli vagonları açıkça sayar; kendinden hareketli olup olmaması önemsizdir. Yük vagonu "
      "(86.06) veya makine (84.74) sayılmaz; 87.05 karayolu taşıtlarıdır.",
      "86.04 Açıklama Notu.", 86),
]

# Öz denetim
assert len(sorular) == 20
cnt = Counter(q["cevap"] for q in sorular)
assert all(cnt[L] == 4 for L in "ABCDE"), cnt
for i, q in enumerate(sorular, 1):
    g = q["gerekce"]
    assert len(g) <= 420, (i, len(g))
    assert len(re.sub(r"<[^>]+>", " ", g).split()) <= 45, (i, len(g.split()))
    assert len(q["secenekler"]) == 5

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"tur": "karma", "no": 3, "sorular": sorular}, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT, dict(cnt))
