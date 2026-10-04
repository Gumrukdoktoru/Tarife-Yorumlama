#!/usr/bin/env python3
"""Karma test 6 üretici (20 soru)."""
import json
import os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KITAP, "karma", "karma_06.json")


def S(soru, secenekler, cevap, tip, gerekce, dayanak, fasil):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


sorular = [
    # 1 — Genel · Tarife yapısı (C)
    S("Tarife Cetvelinin yapısında yer alan bölüm notları ile ilgili aşağıdakilerden hangisi doğrudur?",
      ["Bölüm notları, bölüm başlıkları gibi yalnızca gösterici niteliktedir.",
       "Bölüm notları yalnızca bölümün ilk faslındaki pozisyonlara uygulanır.",
       "Bölüm notları, pozisyon metinleri ve fasıl notlarıyla birlikte sınıflandırmanın yasal dayanağını oluşturur.",
       "Bölüm notları, alt pozisyonlar arasındaki seçimde dikkate alınmaz.",
       "Tarife Cetvelindeki her bölümün başında en az bir bölüm notu bulunur."],
      "C", "Tarife yapısı",
      "GYK 1’e göre yalnız başlıklar göstericidir; sınıflandırma pozisyon metinleri ile bölüm ve fasıl notlarına göre yapılır. "
      "Bölüm notları ilk fasılda yer alsa da tüm bölüme uygulanır, GYK 6 gereği alt pozisyonlarda da geçerlidir; Bölüm V’in notu yoktur.",
      "GYK 1 ve 6; Tarife Cetveli bölüm yapısı (Bölüm V).", "Genel"),

    # 2 — Fasıl 52 · Fasıl/Bölüm bulma (A)
    S("Ağırlık itibarıyla %40 pamuk, %35 yün, %15 poliester devamsız lif ve %10 naylon filamentten oluşan, "
      "top halindeki düz dokunmuş mensucat Tarife Cetvelinin hangi faslında sınıflandırılır?",
      ["Fasıl 52", "Fasıl 51", "Fasıl 53", "Fasıl 54", "Fasıl 55"],
      "A", "Fasıl/Bölüm bulma",
      "Karışım, ağırlıkça her birine üstün gelen maddeden yapılmış sayılır. 54 ve 55. fasıllar tek fasıl kabul edilse de "
      "sentetikler toplamı %25’tir; pamuk (%40) yünden (%35) fazladır. Üstünlük için %50’yi aşmak gerekmez.",
      "Bölüm XI Not 2(A) ve 2(B)(b)–(c).", 52),

    # 3 — Fasıl 25 · Olumsuz teşhis (E)
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 25. faslında <b>yer almaz</b>?",
      ["Toz haline getirilmiş tabii tebeşir", "Kabaca yontulmuş kayağantaşı blokları", "Ham zımpara taşı",
       "Pişmiş kiremit kırıkları", "Terzilerin kumaş işaretlemede kullandığı tebeşir"],
      "E", "Olumsuz teşhis",
      "Fasıl 25 Not 2 yazı, resim ve terzi tebeşirlerini 96.09’a gönderir; tabii tebeşir ise 25.09’da kalır. "
      "Zımpara taşı 25.13’te, kabaca yontulmuş kayağantaşı 25.14’te, kiremit kırıkları Not 4 gereği 25.30’dadır.",
      "Fasıl 25 Not 2 ve Not 4; 25.09, 25.13, 25.14 pozisyon metinleri.", 25),

    # 4 — Fasıl 16 · Eşya → 4’lü pozisyon (B)
    S("Tarife Cetveline göre, fırında pişirildikten sonra dilimlenip dondurulmuş, başka hiçbir madde katılmamış "
      "kemiksiz kuzu budu hangi tarife pozisyonunda sınıflandırılır?",
      ["02.04", "16.02", "02.10", "16.01", "21.06"],
      "B", "Eşya → 4’lü pozisyon",
      "Fasıl 2 yalnız pişirilmemiş eti kapsar; haşlanmış, ızgara yapılmış veya fırınlanmış et Fasıl 2 dışındadır ve 16.02’de yer alır. "
      "Dondurulmuş olması 02.04’e götürmez; sosis niteliği olmadığından 16.01 de uygulanmaz.",
      "Fasıl 2 Genel Açıklamalar; 16.02 Açıklama Notu.", 16),

    # 5 — Fasıl 5 · Olumsuz teşhis (D)
    S("Aşağıdaki hayvansal ürünlerden hangisi Tarife Cetvelinin 5. faslında <b>yer almaz</b>?",
      ["Kurutulmuş ve tütsülenmiş domuz mideleri", "Sığır kuyruğundan elde edilmiş işlenmemiş kıllar",
       "Sosis yapımında kullanılacak sıvı haldeki sığır kanı", "Yenilebilir, kurutulmuş köpekbalığı yüzgeçleri",
       "Mercan tozu ve döküntüleri"],
      "D", "Olumsuz teşhis",
      "Yenilebilir balık yüzgeçleri yenilen balık sakatatı olarak Fasıl 3’tedir. Not 1(a) yenilebilir ürünleri dışlar, ancak "
      "mideleri ve sıvı kanı yenilebilir olsa da fasılda bırakır (05.04, 05.11); sığır kuyruk kılı Not 4 gereği at kılıdır, mercan tozu 05.08’dedir.",
      "Fasıl 5 Not 1(a) ve Not 4; Fasıl 5 Genel Açıklamalar; 05.08 pozisyon metni.", 5),

    # 6 — Fasıl 33 · Eşya → 4’lü pozisyon (D)
    S("Tarife Cetveline göre; sabun veya yüzey aktif madde içermeyen, esas olarak cildi temizlemek üzere tertiplenmiş, "
      "sivilceyi tedavi edici aktif maddeleri yeterli derecede yüksek miktarda içermeyen ve perakende şişelerde satılan "
      "sivilce karşıtı temizleme losyonu hangi tarife pozisyonunda sınıflandırılır?",
      ["30.04", "34.01", "33.07", "33.04", "34.02"],
      "D", "Eşya → 4’lü pozisyon",
      "33.04 Açıklama Notu, esasen cildi temizleyen ve tedavi edici aktif madde içeriği yeterince yüksek olmayan sivilce "
      "müstahzarlarını bu pozisyona alır; ilaç (30.04) sayılmaz. Sabun veya yüzey aktif madde içermediğinden 34.01’e de girmez.",
      "33.04 Açıklama Notu; Fasıl 30 Not 1(e).", 33),

    # 7 — Fasıl 48 · Olumsuz teşhis (A)
    S("Aşağıdaki kâğıttan veya selüloz vatkadan eşyadan hangisi Tarife Cetvelinin 48. faslında <b>sınıflandırılmaz</b>?",
      ["Ayakkabı parlatmaya mahsus cila emdirilmiş kâğıt mendil", "Kâğıttan kalıplanmış tek kullanımlık tabak",
       "Oluklu kartondan koli", "Selüloz vatkadan kuru kâğıt mendil", "Kâğıttan dosya ve klasör"],
      "A", "Olumsuz teşhis",
      "Fasıl 48 Not 2(d), cila, krem veya benzeri müstahzar emdirilmiş kâğıt ve selüloz vatkayı 34.05’e gönderir. "
      "Kâğıt tabak 48.23’te, oluklu karton koli 48.19’da, kuru kâğıt mendil 48.18’de, kâğıt klasör 48.20’dedir.",
      "Fasıl 48 Not 2(d); 48.18, 48.19, 48.20, 48.23 pozisyon metinleri.", 48),

    # 8 — Fasıl 15 · Eşya → 4’lü pozisyon (C)
    S("Tarife Cetveline göre, bazı yağlı tohumların işlenmesiyle elde edilen, kristalli veya taneli kalıplar halinde bulunan, "
      "dışı beyaz ve içi yeşilimsi sarı renkte olan ve ticarette “Borneo don yağı” olarak bilinen, başka bir işlem görmemiş "
      "bitkisel ürün hangi tarife pozisyonunda sınıflandırılır?",
      ["15.02", "15.21", "15.15", "15.16", "15.03"],
      "C", "Eşya → 4’lü pozisyon",
      "15.15 Açıklama Notu, Borneo ve Çin bitkisel don yağlarını diğer bitkisel sabit yağlar arasında sayar. Adı “don yağı” olsa da "
      "hayvansal olmadığından 15.02’ye, gerçekte yağ olduğundan bitkisel mumlara (15.21) girmez; hidrojenize edilmediği için 15.16 da uygulanmaz.",
      "15.15 Açıklama Notu.", 15),

    # 9 — Fasıl 43 · Farklı/aynı pozisyon veya fasıl (E)
    S("Aşağıdaki kürkle ilgili eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir fasılda yer alır?",
      ["Kürkten yapılmış oyun çantası", "Dekorasyonda kullanılan merdaneler için kürkten parlatma derisi",
       "Kürkten, yere serilmek üzere hazırlanmış örtü", "İçi kürkle astarlanmış dokuma kumaştan kaban",
       "Dış yüzü kürkle kaplanmış dürbün mahfazası"],
      "E", "Farklı/aynı pozisyon veya fasıl",
      "42.02’nin ilk kısmındaki dürbün mahfazası gibi eşya her maddeden olabilir ve 43.03 dışında bırakılmıştır; Fasıl 42’dedir. "
      "Oyun çantası, parlatma derisi ve yer örtüsü kürkten eşya, içi kürk astarlı kaban Not 4 gereği 43.03’tedir.",
      "Fasıl 43 Not 4; 43.03 Açıklama Notu; 42.02 Açıklama Notu.", 43),

    # 10 — Fasıl 70 · Eşya → 4’lü pozisyon (B)
    S("Tarife Cetveline göre, televizyon alıcılarına ait katot ışınlı tüplerin imalinde kullanılan, henüz hiçbir "
      "donanımı takılmamış camdan koniler hangi tarife pozisyonunda sınıflandırılır?",
      ["85.40", "70.11", "70.20", "85.29", "70.02"],
      "B", "Eşya → 4’lü pozisyon",
      "70.11, lamba ve katot ışınlı tüpler için donanımsız açık cam zarfları ve bunların camdan parçalarını (televizyon tüplerinin "
      "konileri gibi) kapsar. Ağzı kapatılmış veya donatılmış tüpler 85.40’a girer; yalnız kesilmiş cam borular 70.02’dedir.",
      "70.11 pozisyon metni ve Açıklama Notu.", 70),

    # 11 — Fasıl 45 · Olumsuz teşhis (A)
    S("Tabii veya aglomere mantar içeren aşağıdaki eşyadan hangisi Tarife Cetvelinin 45. faslında <b>yer almaz</b>?",
      ["Mantar tıpanın yalnızca yardımcı bir kısım olarak işlev gördüğü, metal gövdeli ölçü tıpası",
       "Parafinlenmiş ve ateşle markalanmış tabii mantar şarap tıpası",
       "Filtre imalinde kullanılan aglomere mantardan silindirler",
       "Sigara uçlarında kullanılan, kâğıtla sağlamlaştırılmış rulo halinde ince tabii mantar şeridi",
       "Kaynar suyla muamele edildikten sonra presle düzleştirilmiş tabii mantar"],
      "A", "Olumsuz teşhis",
      "45.03 Açıklama Notu, mantar tıpanın yalnız yardımcı kısım olduğu ölçü ve süzme tıpalarını esas karakteri veren maddeye göre "
      "sınıflandırır. Parafinli tıpa 45.03’te, ince şerit 45.02’de, aglomere silindir 45.04’te, preslenmiş mantar 45.01’dedir.",
      "45.03 Açıklama Notu (1); 45.01, 45.02, 45.04 Açıklama Notları.", 45),

    # 12 — Fasıl 87 · Fasıl notu · Tanım/Eşik (E)
    S("Tarife Cetvelinin 87. Faslındaki notlar ve pozisyon metinlerine göre aşağıdaki ifadelerden hangisi doğrudur?",
      ["Sürücü dahil dokuz kişi taşımaya mahsus motorlu taşıtlar 87.02 pozisyonunda yer alır.",
       "Yalnız raylar üzerinde hareket etmek üzere imal edilmiş tramvay taşıtları 87. Fasılda yer alır.",
       "Traktöre uygun olarak tasarlanıp traktöre monte edilmiş halde sunulan çalışma aletleri traktörle birlikte 87.01’de yer alır.",
       "Motorla ve sürücü mahalliyle teçhiz edilmiş şasiler 87.06 pozisyonunda yer alır.",
       "Sürücü dahil on veya daha fazla kişi taşımaya mahsus motorlu taşıtlar 87.02 pozisyonunda yer alır."],
      "E", "Fasıl notu · Tanım/Eşik",
      "87.02 metni sürücü dahil on veya daha fazla kişilik taşıtları kapsar; dokuz kişilik taşıt 87.03’tedir. "
      "Not 1 raylı tramvayları dışlar, Not 2 traktörle gelen aletleri asıl fasıllarına gönderir, Not 3 sürücü mahalli olan şasileri 87.02–87.04’e verir.",
      "Fasıl 87 Not 1, 2, 3; 87.02 pozisyon metni.", 87),

    # 13 — GYK (C)
    S("Burun kısmı henüz kapatılmamış olmakla birlikte bitmiş çorabın esas karakterini taşıyan, sentetik iplikten örülmüş "
      "uzun konçlu kadın çorapları Tarife Cetvelinde hangi pozisyonda ve hangi Genel Yorum Kuralına göre sınıflandırılır?",
      ["61.15 – GYK 3(b)", "60.06 – GYK 1", "61.15 – GYK 1 ve 2(a)", "61.17 – GYK 4", "63.07 – GYK 3(c)"],
      "C", "Genel Yorum Kuralı",
      "GYK 2(a), bitmiş eşyanın esas karakterini taşıyan bitirilmemiş eşyayı bitmiş eşyanın pozisyonuna alır; 61.15 Açıklama Notu "
      "da imali bitirilmemiş çorapları bu pozisyona dahil eder. Örme mensucat (60.06) veya diğer hazır eşya (63.07) sayılmaz.",
      "GYK 1 ve 2(a); Fasıl 61 Genel Açıklamalar; 61.15 Açıklama Notu.", "GYK"),

    # 14 — Fasıl 60 · Olumsuz teşhis (B)
    S("Parça halinde (top veya rulo) sunulan aşağıdaki eşyadan hangisi Tarife Cetvelinin 60. faslında <b>sınıflandırılmaz</b>?",
      ["Eni 150 cm, ağırlıkça %6 elastomerik iplik içeren, tüysüz atkılı örme mensucat",
       "Zemini örme mensucat olup üzerine motifler işlenmiş işlemeli mensucat",
       "Eni 25 cm, elastomerik iplik içermeyen pamuklu örme şerit",
       "Galloon örgü makinesinde yapılmış, eni 90 cm, elastomersiz çözgülü örme mensucat",
       "Eni 200 cm, elastomerik iplik içermeyen pamuklu atkılı örme mensucat"],
      "B", "Olumsuz teşhis",
      "60.02–60.06 Açıklama Notları işlemeli mensucatı (58.10) bu pozisyonların dışında bırakır. Elastomerli geniş mensucat 60.04’te, "
      "30 cm’yi geçmeyen elastomersiz şerit 60.03’te, galloon ürünü 60.05’te, elastomersiz geniş atkılı örme 60.06’dadır.",
      "60.02–60.06 Açıklama Notları.", 60),

    # 15 — Fasıl 90 · Farklı/aynı pozisyon veya fasıl (D)
    S("Aşağıdaki ölçü aletlerinden hangisi diğerlerinden farklı bir tarife pozisyonunda yer alır?",
      ["Akümülatör asidinin özgül ağırlığını ölçen yüzer tip asidimetre",
       "Sütün yoğunluğunu ölçen laktodensimetre",
       "Kil gibi katı bir maddenin büzülmesi esasına dayanan pirometre",
       "Kerestenin nem içeriğini belirlemeye mahsus nem ölçer",
       "Sıcaklığı göstermenin yanında alarm devresini çalıştıran kontakt termometre"],
      "D", "Farklı/aynı pozisyon veya fasıl",
      "90.25 hidrometreleri (asidimetre, laktodensimetre), pirometreleri ve kontakt termometreleri kapsar; katı maddelerin nem "
      "içeriğini belirleyen cihazları ise açıkça dışlar, bunlar 90.27’dedir. 90.25’teki higrometreler hava ve gazların nemini ölçer.",
      "90.25 Açıklama Notu (A), (B), (D).", 90),

    # 16 — GYK (A)
    S("Rafine edilmiş prina yağı ile saf zeytinyağının karışımından oluşan, kimyasal olarak değiştirilmemiş yemeklik sıvı yağ "
      "hangi pozisyonda ve hangi Genel Yorum Kuralına göre sınıflandırılır?",
      ["15.10 – GYK 1", "15.09 – GYK 3(b)", "15.10 – GYK 3(c)", "15.09 – GYK 2(b)", "15.15 – GYK 4"],
      "A", "Genel Yorum Kuralı",
      "15.10 metni, prina yağının 15.09’daki zeytinyağlarıyla karışımlarını ismen kapsar; GYK 2(b) Açıklama Notuna göre pozisyon "
      "metninde belirtilen karışımlar 1 No.lu Kurala göre sınıflandırılır. Esas nitelik (3(b)) veya numara sırası (3(c)) araştırılmaz.",
      "GYK 1; GYK 2(b) Açıklama Notu (X); 15.10 pozisyon metni ve Açıklama Notu.", "GYK"),

    # 17 — Fasıl 92 · Fasıl notu · Tanım/Eşik (E)
    S("Fasıl 92 notları ve açıklamalarına göre, ayrı olarak sunulan aşağıdaki eşyadan hangisi bir müzik aletiyle kullanılsa bile "
      "92. Fasılda <b>yer almaz</b>?",
      ["Sınai amaçlarla kullanılan, elektrik kontaklı metronom", "Trompete takılan tipte nota taşıyıcı",
       "Müzik kutuları için mekanizma", "Akordeon körüğü", "Trampeti çalma konumunda tutmaya mahsus tripod sehpa"],
      "E", "Fasıl notu · Tanım/Eşik",
      "Fasıl 92 Not 1(d), müzik aletleri için monopod, bipod, tripod ve benzerlerini 96.20’ye gönderir; alete takılan nota taşıyıcılar "
      "92.09’dadır. Metronomlar sınai amaçlı olsalar da, müzik kutusu mekanizmaları ve akordeon körükleri de 92.09’da kalır.",
      "Fasıl 92 Not 1(d); 92.09 Açıklama Notu.", 92),

    # 18 — Fasıl 84 · Senaryo (C)
    S("Bir kafe zinciri; içine konulan kahve çekirdeklerini öğütüp sıcak suyla demleyerek bardağa dolduran, su ısıtma ve süt karıştırma "
      "tertibatı bulunan bir makine ithal etmektedir. Makine, yuvasına metal para veya jeton atılmadıkça ya da manyetik kart okutulmadıkça "
      "içecek vermemekte olup esas fonksiyonu içeceğin otomatik satışıdır. Tarife Cetveline göre bu makine hangi tarife pozisyonunda sınıflandırılır?",
      ["84.19", "85.16", "84.76", "84.38", "84.79"],
      "C", "Senaryo",
      "84.76, para, jeton veya kartla mal veren otomatik satış makinelerini kapsar; esas fonksiyon satış olduğu sürece ısıtma veya "
      "hazırlama tertibatı bulunması sonucu değiştirmez. Ödeme tertibatı olmayan sıcak veya soğuk içecek makineleri 84.19’dadır.",
      "84.76 Açıklama Notu.", 84),

    # 19 — GYK (B)
    S("Maden ocaklarında kullanılan bir makine, kömürü kesip parçaladıktan sonra aynı zamanda taşıyıcı banda yüklemektedir. "
      "Kesme işlevi bakımından 84.30, yükleme işlevi bakımından 84.28 pozisyonuna girebilen makinenin esas fonksiyonu belirlenememektedir. "
      "Bu makine hangi pozisyonda ve hangi kurala göre sınıflandırılır?",
      ["84.28 – GYK 3(a)", "84.30 – GYK 3(c)", "84.28 – GYK 3(c)", "84.30 – GYK 3(b)", "84.79 – GYK 4"],
      "B", "Genel Yorum Kuralı",
      "Bölüm XVI Not 3’e göre çok işlevli makineler esas fonksiyonlarına göre sınıflandırılır; esas fonksiyon belirlenemezse GYK 3(c) "
      "uygulanır ve geçerli pozisyonlardan numara sırasına göre sonuncusu olan 84.30 seçilir.",
      "Bölüm XVI Not 3 ve Genel Açıklamalar (VI); 84.30 Açıklama Notu; GYK 3(c).", "GYK"),

    # 20 — Fasıl 97 · Çoktan-çoğa / Eşleştirme (D)
    S("Aşağıdakilerden hangileri Tarife Cetvelinin 97. faslında sınıflandırılır?<br/>"
      "I. Sanatçının özel bir kâğıda çizip transfer tekniğiyle taşa geçirdiği çizimden, mekanik veya fotomekanik usul kullanılmadan basılmış litografya<br/>"
      "II. Elle boyanarak dekore edilmiş fabrikasyon seramik tabak<br/>"
      "III. Koleksiyon için hazırlanmış, içleri boşaltılmış kuş yumurtaları<br/>"
      "IV. Posta pulu taşımayan resimli ilk gün kartı",
      ["I ve II", "II ve IV", "I, III ve IV", "I ve III", "II, III ve IV"],
      "D", "Çoktan-çoğa / Eşleştirme",
      "Transfer tekniğiyle elde edilen orijinal litografya 97.02’de, içi boşaltılmış yumurta koleksiyonu 97.05’tedir. "
      "Elle dekore edilmiş fabrikasyon ürünler kendi pozisyonlarında, pul taşımayan ilk gün kartları 48.17 veya Fasıl 49’dadır.",
      "Fasıl 97 Not 3; 97.01, 97.02, 97.04, 97.05 Açıklama Notları.", 97),
]

assert len(sorular) == 20
obj = {"tur": "karma", "no": 6, "sorular": sorular}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT)
