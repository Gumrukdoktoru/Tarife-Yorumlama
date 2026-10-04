#!/usr/bin/env python3
"""Karma test 2 üreticisi → KITAP/karma/karma_02.json"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_02.json")


def q(fasil, tip, soru, secenekler, cevap, gerekce, dayanak):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


S = []

# 1 — Genel · Tarife yapısı (B)
S.append(q("Genel", "Tarife yapısı",
    "Tarife Cetvelinde, Armonize Sistem Nomanklatüründe ileride kullanılmak üzere saklı tutulan "
    "(içeriği boş bırakılmış) fasıl aşağıdakilerden hangisidir?",
    ["Fasıl 66", "Fasıl 77", "Fasıl 81", "Fasıl 98", "Fasıl 99"],
    "B",
    "Fasıl 77, XV. Bölümde alüminyum (76) ile kurşun (78) arasında ileride kullanılmak üzere saklı tutulur. "
    "Fasıl 98 de saklıdır, ancak akit tarafların özel amaçları içindir; Fasıl 99 özel amaçlı pozisyonlara ayrılmıştır.",
    "Tarife Cetveli İçindekiler (Bölüm XV ve Bölüm XXI fasıl listesi)."))

# 2 — Fasıl 51 · Fasıl/Bölüm bulma (D)
S.append(q(51, "Fasıl/Bölüm bulma",
    "Tarife Cetveline göre karde edilmiş Ankara tavşanı kılı tarifenin hangi bölümünde yer alır?",
    ["Bölüm I", "Bölüm VIII", "Bölüm X", "Bölüm XI", "Bölüm XII"],
    "D",
    "Ankara tavşanı kılı Fasıl 51 Not 1(b) uyarınca “ince hayvan kılı”dır; karde edilmiş hali 51.05’te, yani "
    "XI. Bölümdedir. Tavşan kürkü çağrışımıyla VIII. Bölüm, hayvansal ürün çağrışımıyla I. Bölüm tuzaktır.",
    "Fasıl 51 Not 1(b); 51.05 pozisyon metni."))

# 3 — Fasıl 74 · Fasıl/Bölüm bulma (A)
S.append(q(74, "Fasıl/Bölüm bulma",
    "Ağırlıkça %62 bakır ve %38 çinko içeren pirinçten mamul, diş açılmamış perçin çivileri Tarife Cetvelinin "
    "hangi faslında yer alır?",
    ["Fasıl 74", "Fasıl 73", "Fasıl 79", "Fasıl 83", "Fasıl 76"],
    "A",
    "Bakırın ağırlıkça diğer her elementten fazla olduğu pirinç bakır alaşımıdır; bakırdan perçin çivileri "
    "74.15’te sayılır. Çinko içeriği Fasıl 79’a, “genel kullanıma mahsus eşya” algısı Fasıl 73 veya 83’e götürmez.",
    "Bölüm XV Not 5; Fasıl 74 Not 1(b); 74.15 pozisyon metni."))

# 4 — Fasıl 9 · Olumsuz teşhis (E)
S.append(q(9, "Olumsuz teşhis",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 9. faslında <b>yer almaz</b>?",
    ["Kavrulmamış yeşil kahve çekirdekleri",
     "Kurutulmuş ve ufalanmış Paraguay çayı (maté) yaprakları",
     "Kakule tohumları",
     "Zerdeçal",
     "Laktoz ve glikoz içeren ginseng hülasası karışımı (ginseng çayı)"],
    "E",
    "Thea cinsinden elde edilmeyen ginseng çayı 09.02 Açıklama Notuyla 21.06’ya gönderilir. Yeşil kahve 09.01, "
    "maté 09.03, kakule 09.08, zerdeçal 09.10’dadır; adındaki “çay” sözcüğü tuzaktır.",
    "09.02 Açıklama Notu (hariç tutulanlar); 09.01, 09.03, 09.08, 09.10 pozisyon metinleri."))

# 5 — Fasıl 3 · Olumsuz teşhis (C)
S.append(q(3, "Olumsuz teşhis",
    "Aşağıdaki ürünlerin hangisi Tarife Cetvelinin 3. faslında <b>sınıflandırılmaz</b>?",
    ["Canlı yılan balığı",
     "Kabuğu içinde suda haşlanıp dondurulmuş kerevit",
     "Dondurulmuş fok eti",
     "Soğutulmuş kalamar",
     "Tuzlanarak kurutulmuş köpek balığı yüzgeci"],
    "C",
    "Fok 01.06’daki deniz memelilerindendir; Fasıl 3 Not 1 bu memelilerin etlerini fasıl dışında bırakır (02.08). "
    "Yılan balığı 03.01, kabuğunda haşlanmış kerevit 03.06, kalamar 03.07, kurutulmuş yüzgeç 03.05’tedir.",
    "Fasıl 3 Not 1(b); 02.08 pozisyon metni; Fasıl 3 Genel Açıklamalar."))

# 6 — Fasıl 7 · Farklı/aynı pozisyon veya fasıl (E)
S.append(q(7, "Farklı/aynı pozisyon veya fasıl",
    "Tarife Cetveline göre aşağıdaki taze kök ve yumrulardan hangisi diğerlerinden farklı bir fasılda "
    "sınıflandırılır?",
    ["Kırmızı pancar", "Yer elması", "Teke sakalı (salsifis)", "Turp", "Şeker pancarı"],
    "E",
    "Gıda sanayiinde hammadde olan şeker pancarı Fasıl 7 Genel Açıklamalarında fasıl dışı sayılır (12.12). "
    "Kırmızı pancar, teke sakalı ve turp 07.06’da, yer elması 07.14’te; hepsi Fasıl 7’dedir.",
    "Fasıl 7 Genel Açıklamalar (hariç tutulanlar); 07.06 ve 07.14 pozisyon metinleri."))

# 7 — Fasıl 92 · Pozisyon → eşya (A)
S.append(q(92, "Pozisyon → eşya",
    "Tarife Cetveline göre aşağıdakilerden hangisi 92.08 pozisyonunda sınıflandırılır?",
    ["Spor hakemlerinin kullandığı, ağızla üflenen metal düdük",
     "Müzik aletlerini akort etmeye mahsus akort düdüğü",
     "Bisikletler için mekanik zil",
     "Elektrikle çalışan kapı zili",
     "Ağız armonikası"],
    "A",
    "92.08, ağızla üflenen düdükleri ve diğer ağızla işaret verme aletlerini kapsar. Akort düdüğü 92.09’da, "
    "ağız armonikası 92.05’te; bisiklet ve kapı zilleri 83.06 veya 85.31’de yer alır.",
    "92.08 Açıklama Notu (B) ve hariç tutulanlar; 92.09 Açıklama Notu (A)."))

# 8 — Fasıl 44 · Eşya → 4’lü pozisyon (B)
S.append(q(44, "Eşya → 4’lü pozisyon",
    "Tarife Cetveline göre kabaca yontulmuş, fakat torna edilmemiş, bükülmemiş veya başka surette işlenmemiş, "
    "şemsiye sapı imaline elverişli kalınlık ve uzunluktaki ahşap çubuklar hangi pozisyonda sınıflandırılır?",
    ["44.03", "44.04", "44.17", "44.21", "66.03"],
    "B",
    "Baston, şemsiye ve alet sapı imaline elverişli, yalnızca kabaca yontulmuş çubuklar 44.04 metninde sayılır. "
    "Torna edilmiş veya bükülmüş saplar ait oldukları pozisyonlara (şemsiye kulpu 66.03, alet sapı 44.17) gider.",
    "44.04 pozisyon metni ve Açıklama Notu (4); 66.03 Açıklama Notu."))

# 9 — Fasıl 16 · Olumsuz teşhis (D)
S.append(q(16, "Olumsuz teşhis",
    "Aşağıdakilerden hangisi Tarife Cetvelinin 16. faslında <b>sınıflandırılmaz</b>?",
    ["Tavuk etinden yapılmış, kılıf içinde tütsülenmiş sosis",
     "Konserve edilmiş, pişmiş sığır dili",
     "Domates soslu uskumru konservesi",
     "Ağırlıkça %25 tavuk eti içeren konsantre tavuk çorbası",
     "Pişirilerek konserve edilmiş ahtapot"],
    "D",
    "Fasıl 16 Not 2’deki %20 eşiği 21.04’teki çorba ve et sularına uygulanmaz; %25 tavuk eti içerse de çorba "
    "21.04’tedir. Sosis 16.01, sakatat konservesi 16.02, uskumru 16.04, pişmiş ahtapot 16.05’tedir.",
    "Fasıl 16 Not 2; Fasıl 16 Genel Açıklamalar; 16.02 Açıklama Notu (hariç tutulanlar)."))

# 10 — Fasıl 33 · Farklı/aynı pozisyon veya fasıl (C)
S.append(q(33, "Farklı/aynı pozisyon veya fasıl",
    "Tarife Cetveline göre aşağıdaki müstahzarlardan hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
    ["Saç biryantini",
     "Saç ağartıcısı",
     "Vücut tüylerini ağartmaya mahsus krem",
     "Saç düzleştirici (defrize) müstahzar",
     "Saç pomatı"],
    "C",
    "Biryantin, saç ağartıcısı, defrize müstahzarı ve pomat saç müstahzarı olarak 33.05’tedir. Saça değil "
    "vücut tüylerine uygulanan müstahzarlar 33.05 dışında, 33.07’de yer alır; ortak “ağartıcı” adı tuzaktır.",
    "33.05 Açıklama Notu; 33.07 pozisyon metni."))

# 11 — Fasıl 87 · Eşya → 4’lü pozisyon (D)
S.append(q(87, "Eşya → 4’lü pozisyon",
    "Tarife Cetveline göre seyyar dondurma satıcılarının kullandığı, elle itilerek yürütülen, izole edilmiş ve "
    "soğutma tertibatı bulunmayan küçük araba hangi pozisyonda sınıflandırılır?",
    ["84.18", "87.09", "87.15", "87.16", "94.03"],
    "D",
    "Hareket ettirici tertibatı olmayan, elle itilen izoleli satıcı arabaları 87.16 Açıklama Notunda açıkça "
    "sayılır. Soğutma tertibatı yoktur (84.18 değil); 87.09 kendinden hareketli yük arabalarını, 87.15 bebek "
    "arabalarını kapsar.",
    "87.16 Açıklama Notu (B)(6)."))

# 12 — Fasıl 93 · Farklı/aynı pozisyon veya fasıl (B)
S.append(q(93, "Farklı/aynı pozisyon veya fasıl",
    "Aşağıdakilerden hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda sınıflandırılır?",
    ["Sadece işaret fişeği atmak üzere imal edilmiş tabanca",
     "Ayrı olarak gelen işaret fişekleri",
     "Revolver",
     "Av tüfeği için saçmalı fişek",
     "Ayrı olarak gelen av tüfeği namlusu"],
    "B",
    "Fasıl 93 Not 1(a) gereği işaret fişekleri Fasıl 36’dadır (36.04). İşaret fişeği atan tabanca 93.03’te, "
    "revolver 93.02’de, fişek 93.06’da, namlu 93.05’te kalır; tabanca ile fişeğin ayrışması tuzaktır.",
    "Fasıl 93 Not 1(a); 93.03 pozisyon metni; 93.06 Açıklama Notu (hariç tutulanlar)."))

# 13 — Fasıl 62 · Eşya → 4’lü pozisyon (A)
S.append(q(62, "Eşya → 4’lü pozisyon",
    "Tarife Cetveline göre erkekler için dokunmuş poliester kumaştan dikilmiş, içine pille çalışan elektrikli "
    "ısıtma telleri yerleştirilmiş, kapüşonlu ve kalçayı örten anorak hangi pozisyonda sınıflandırılır?",
    ["62.01", "62.11", "85.16", "61.01", "63.01"],
    "A",
    "Fasıl 62 Genel Açıklamalarına göre elektrikle ısıtılan giyim eşyası bu fasılda kalır; Fasıl 85 Not 1 de "
    "bunu dışarıda bırakır. Erkek anorağı 62.01’dedir; 85.16 ısıtıcı, 61.01 örme giysi, 63.01 battaniye çeldiricidir.",
    "Fasıl 62 Genel Açıklamalar; Fasıl 85 Not 1(a); 62.01 pozisyon metni."))

# 14 — Genel · Tarife yapısı (C)
S.append(q("Genel", "Tarife yapısı",
    "Tarife Cetveline göre aşağıdaki fasıllardan hangisi, yer aldığı bölümün ilk faslı <b>değildir</b>?",
    ["Fasıl 41", "Fasıl 64", "Fasıl 73", "Fasıl 86", "Fasıl 90"],
    "C",
    "XV. Bölüm Fasıl 72 (demir ve çelik) ile başlar; Fasıl 73 bu bölümün ikinci faslıdır. Fasıl 41 VIII., "
    "64 XII., 86 XVII. ve 90 XVIII. Bölümün ilk faslıdır; bölüm notları bu fasılların önünde yer alır.",
    "Tarife Cetveli İçindekiler (Bölüm VIII, XII, XV, XVII ve XVIII fasıl listeleri)."))

# 15 — Fasıl 38 · Eşya → 4’lü pozisyon (E)
S.append(q(38, "Eşya → 4’lü pozisyon",
    "Tarife Cetveline göre fırın ve kok fırınlarının iç tuğla örgüsünün tamirinde kullanılan, ısıya dayanıklı "
    "hidrolik çimento ile ateşe dayanıklı çakıl karışımından oluşan ateşe dayanıklı beton hangi pozisyonda "
    "sınıflandırılır?",
    ["25.23", "68.10", "69.02", "38.24", "38.16"],
    "E",
    "Ateşe dayanıklı çimento, harç ve betonlar 38.16 Açıklama Notunda açıkça sayılır. 25.23 hidrolik çimentoyu, "
    "68.10 çimento veya betondan eşyayı, 69.02 ateşe dayanıklı seramik tuğlaları kapsar; 38.24 artık pozisyondur.",
    "38.16 pozisyon metni ve Açıklama Notu."))

# 16 — Fasıl 85 · Olumsuz teşhis (B)
S.append(q(85, "Olumsuz teşhis",
    "Tarife Cetveline göre aşağıdakilerden hangisi 85.18 pozisyonunda <b>sınıflandırılmaz</b>?",
    ["Otomatik bilgi işlem makinesine bağlanmak üzere tasarlanmış, ayrı sunulan hoparlör",
     "Ses karıştırmaya ve dengelemeye mahsus cihaz",
     "Telefonculukta ses tekrarlayıcı (repetör) olarak kullanılan ses frekans amplifikatörü",
     "Bir mikrofon ve hoparlörlerden oluşan, konferans katılımcılarına mahsus set",
     "Kablosuz mikrofon ve kablosuz alıcıdan oluşan mikrofon seti"],
    "B",
    "85.18 Açıklama Notuna göre ses karıştırma ve dengeleme cihazları bağımsız fonksiyonlu cihaz olarak "
    "85.43’tedir. Bilgisayar hoparlörü, repetör amplifikatörü, konferans seti ve kablosuz mikrofon seti notta "
    "85.18 kapsamında sayılır.",
    "85.18 Açıklama Notu (A), (B), (C), (D)."))

# 17 — Fasıl 59 · Fasıl notu · Tanım/Eşik (D)
S.append(q(59, "Fasıl notu · Tanım/Eşik",
    "Fasıl 59 Not 1’e göre, metinde aksi belirtilmedikçe bu fasıldaki “dokumaya elverişli mensucat” tabirine "
    "aşağıdakilerden hangisi <b>girmez</b>?",
    ["50 ila 55. fasıllardaki dokunmuş mensucat",
     "58.06 pozisyonundaki dar dokunmuş mensucat",
     "60.02 ila 60.06 pozisyonlarındaki örme mensucat",
     "56.03 pozisyonundaki dokunmamış mensucat",
     "58.08 pozisyonundaki parça halindeki kordonlar ve süs eşyası"],
    "D",
    "Not 1 tanımı 50–55. fasıllar, 58.03, 58.06 ve 58.08 ile 60.02–60.06 mensucatıyla sınırlıdır. Dokunmamış "
    "mensucat (56.03) sayılmamıştır; tekstil ürünü olması tanıma girdiği anlamına gelmez.",
    "Fasıl 59 Not 1."))

# 18 — GYK (A)
S.append(q("GYK", "Genel Yorum Kuralı",
    "Bir kutu içinde perakende satışa sunulan; tırnak makası, tırnak törpüsü, tırnak temizleyici ve kıl çekme "
    "cımbızından oluşan manikür takımının sınıflandırılmasıyla ilgili aşağıdakilerden hangisi doğrudur?",
    ["Manikür takımları 82.14 metninde ismen sayıldığından GYK 1 uyarınca 82.14’te sınıflandırılır.",
     "GYK 3(b) uyarınca takıma esas niteliğini veren tırnak makasının pozisyonunda (82.13) sınıflandırılır.",
     "Perakende takım sayılmadığından her alet kendi pozisyonunda ayrı ayrı sınıflandırılır.",
     "GYK 3(c) uyarınca geçerli pozisyonların numara sırasına göre sonuncusunda sınıflandırılır.",
     "GYK 4 uyarınca kendisine en çok benzeyen eşyanın pozisyonunda sınıflandırılır."],
    "A",
    "82.14 metni “manikür veya pedikür takımları”nı ismen kapsar; açıklama notu bu takımların makas ve cımbız "
    "içerebileceğini belirtir. Eşya pozisyon metniyle (GYK 1) sınıflandırılır; GYK 3(b)’ye geçilmez.",
    "GYK 1; 82.14 pozisyon metni ve Açıklama Notu."))

# 19 — Fasıl 84 · Fasıl notu · Tanım/Eşik (C)
S.append(q(84, "Fasıl notu · Tanım/Eşik",
    "Fasıl 84 Not 7’ye göre itibari çapı 4 mm olan, en büyük ve en küçük çapları aşağıda verilen kalibrelenmiş "
    "çelik bilyalardan hangisi 84.82 pozisyonunda sınıflandırılır?",
    ["En büyük çap 4,05 mm – en küçük çap 3,99 mm",
     "En büyük çap 4,02 mm – en küçük çap 3,95 mm",
     "En büyük çap 4,03 mm – en küçük çap 3,97 mm",
     "En büyük çap 4,06 mm – en küçük çap 4,00 mm",
     "En büyük çap 4,00 mm – en küçük çap 3,94 mm"],
    "C",
    "Not 7’de tolerans itibari çapın %1’i veya 0,05 mm’dir; hangisi azsa o esas alınır. 4 mm’de %1 = 0,04 mm "
    "olduğundan çaplar 3,96–4,04 mm arasında kalmalıdır. 0,05 mm’yi esas almak tuzaktır; uymayan bilyalar 73.26’ya gider.",
    "Fasıl 84 Not 7; Bölüm XVI Genel Açıklamalar (aksam ve parçalar)."))

# 20 — GYK (E)
S.append(q("GYK", "Genel Yorum Kuralı",
    "Aşağıdaki sınıflandırma örneklerinden hangisinde dayanılan Genel Yorum Kuralları <b>yanlış</b> gösterilmiştir?",
    ["Canlı atlar – 01.01 – GYK 1 ve 6",
     "Tüm parçaları aynı kolide, monte edilmemiş halde sunulan motorsuz bisiklet – 87.12 – GYK 1, 2(a) ve 6",
     "Hava taşıtı için şekillendirilmiş, çerçevesiz lamine emniyet camı – 70.07 – GYK 1, 3(a) ve 6",
     "Dürbünle birlikte sunulan, o dürbüne uygun yapılmış mahfaza – 90.05 – GYK 1, 5(a) ve 6",
     "Tek başına sunulan, belirli bir gitara uygun sert gitar kutusu – 92.02 – GYK 1, 5(a) ve 6"],
    "E",
    "GYK 5(a) yalnız ait olduğu eşya ile birlikte sunulan mahfazalara uygulanır; tek başına gelen gitar kutusu "
    "kendi pozisyonunda sınıflandırılır. Diğer dört örnek GYK açıklama notlarındaki örneklerle uyumludur.",
    "GYK 5(a) Açıklama Notu (I)(3), (II); GYK 1 Açıklama Notu (III); GYK 3(a) Açıklama Notu (IV)."))


assert len(S) == 20
from collections import Counter
print(Counter(x["cevap"] for x in S))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"tur": "karma", "no": 2, "sorular": S}, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT)
