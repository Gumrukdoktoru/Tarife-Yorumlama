#!/usr/bin/env python3
"""Karma test 8 (20 soru) üretici."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karma", "karma_08.json")


def S(soru, secenekler, cevap, tip, gerekce, dayanak, fasil):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


sorular = [
    # 1 – Fasıl 84 · Fasıl/Bölüm bulma (C)
    S("Evlerde kullanılan türden, kendinden elektrik motorlu dikiş makinesi Tarife Cetvelinin hangi fasılında yer alır?",
      ["Fasıl 85", "Fasıl 82", "Fasıl 84", "Fasıl 94", "Fasıl 90"],
      "C", "Fasıl/Bölüm bulma",
      "Dikiş makineleri ev tipi ve elektrik motorlu olsalar da 84.52’de, yani Fasıl 84’te yer alır. "
      "Fasıl 85 Not 4 dikiş makinelerini 85.09’daki kendinden motorlu ev aletleri dışında bırakır; "
      "“elektrikli ev aleti” görüntüsü Fasıl 85 tuzağıdır.",
      "84.52 pozisyon metni; Fasıl 85 Not 4.", 84),

    # 2 – Fasıl 11 · Eşya → 4’lü pozisyon (A)
    S("Tarife Cetveline göre, hindiba (çikori) köklerinden elde edilen, kimyevi olarak nişastaya benzeyen ancak iyotla "
      "mavi yerine açık sarımsı-kahverengi renk veren inülin hangi pozisyonda sınıflandırılır?",
      ["11.08", "12.12", "17.02", "35.05", "13.02"],
      "A", "Eşya → 4’lü pozisyon",
      "11.08 pozisyon metni nişastaların yanında inülini de sayar; inülin hindiba, dahlia ve yer elması köklerinden elde edilir. "
      "Hidrolizle fruktoz verse de şeker (17.02) veya modifiye nişasta (35.05) değildir; kavrulmamış hindiba kökü ise 12.12’dedir.",
      "11.08 pozisyon metni ve Açıklama Notu; 12.12 Açıklama Notu.", 11),

    # 3 – Genel · Tarife yapısı (D)
    S("Tarife Cetvelinde XI. Bölümün ilk faslının 2’nci pozisyonunda sınıflandırılan eşya aşağıdakilerden hangisidir?",
      ["Çekilmeye elverişli ipek böceği kozaları", "İpek döküntüleri",
       "Karde edilmemiş veya taranmamış yapağı", "Bükülmemiş ham ipek",
       "Karde edilmemiş veya penyelenmemiş pamuk"],
      "D", "Tarife yapısı",
      "XI. Bölüm (dokumaya elverişli maddeler) Fasıl 50 ile başlar; pozisyon numarasının ilk iki hanesi faslı, son iki hanesi "
      "fasıl içindeki sırayı gösterir. Aranan pozisyon 50.02 (bükülmemiş ham ipek)’dir; kozalar 50.01, ipek döküntüleri 50.03, "
      "yapağı 51.01, pamuk 52.01’dedir.",
      "Tarife Cetvelinin bölüm–fasıl düzeni (Bölüm XI: Fasıl 50–63); 50.01–50.03 pozisyon metinleri.", "Genel"),

    # 4 – Fasıl 42 · Eşya → 4’lü pozisyon (B)
    S("Tarife Cetveline göre, deriden yapılmış ustura kayışı hangi pozisyonda sınıflandırılır?",
      ["42.03", "42.05", "82.12", "68.04", "42.01"],
      "B", "Eşya → 4’lü pozisyon",
      "42.05 Açıklama Notu, başka yerde yer almayan deriden eşya arasında ustura kayışlarını açıkça sayar. "
      "Usturanın kendisi 82.12’de, bileği taşları 68.04’tedir; kayış giyim aksesuarı (42.03) veya saraciye eşyası (42.01) değildir.",
      "42.05 Açıklama Notu.", 42),

    # 5 – Fasıl 95 · Olumsuz teşhis (E)
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 95. faslında <b>sınıflandırılmaz</b>?",
      ["Paten takılmış bot şeklindeki buz patenleri", "Uçurtma", "Satranç takımı",
       "Karnavallarda havaya atılan kâğıt konfeti",
       "Oyuncak bebeklere takılmak üzere ayrı olarak sunulan, takılmamış cam gözler"],
      "E", "Olumsuz teşhis",
      "Fasıl 95 Not 1(ij), yapma bebeklere veya diğer oyuncaklara mahsus takılmamış cam gözleri 70.18’e gönderir. "
      "Paten takılı botlar Not 1(g) istisnasıyla 95.06’da, uçurtma 95.03’te, satranç 95.04’te, konfeti 95.05’te kalır.",
      "Fasıl 95 Not 1(g) ve 1(ij); 95.03–95.06 Açıklama Notları.", 95),

    # 6 – Fasıl 22 · Eşya → 4’lü pozisyon (B)
    S("Tarife Cetveline göre, su, şeker ve süzücü maddeler ilave edilerek içecek olarak tüketime hazır hale getirilmiş "
      "demir hindi (tamarind) nektarı hangi pozisyonda sınıflandırılır?",
      ["20.09", "22.02", "21.06", "22.06", "20.08"],
      "B", "Eşya → 4’lü pozisyon",
      "22.02 Açıklama Notu, su, şeker ve süzücü maddelerle içilmeye hazır hale getirilen demir hindi nektarını alkolsüz "
      "içecekler arasında sayar. Ürün 20.09 anlamında meyve suyu değildir; fermente olmadığından 22.06’ya da girmez.",
      "22.02 Açıklama Notu (C).", 22),

    # 7 – Fasıl 49 · Olumsuz teşhis (D)
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 49. faslında <b>sınıflandırılmaz</b>?",
      ["Körlere mahsus kabarık harflerle basılmış kitap", "El ile yazılmış müzik notası",
       "Tamamlanmış ve onaylanmış, hamiline yazılı hisse senedi", "Posta damgalı ilk gün zarfı",
       "Seramik eşyanın süslenmesinde kullanılan, cam haline gelen terkiplerle basılmış çıkartma"],
      "D", "Olumsuz teşhis",
      "Fasıl 49 Not 1(d), posta damgalı zarfları ve ilk gün zarflarını 97.04’e gönderir. Kabarık harfli kitap 49.01’de, "
      "el yazması nota 49.04’te, hisse senedi 49.07’de, cam haline gelen terkiplerle basılmış çıkartma 49.08’de yer alır.",
      "Fasıl 49 Not 1(d); 49.01, 49.04, 49.07 ve 49.08 Açıklama Notları.", 49),

    # 8 – Fasıl 27 · Olumsuz teşhis (A)
    S("Aşağıdakilerden hangisi Tarife Cetvelinin 27. faslında <b>sınıflandırılmaz</b>?",
      ["Cilt bakımında kullanılmaya uygun, bu kullanım için perakende satış ambalajına konulmuş vazelin",
       "Havagazı ve kok fabrikalarının karnilerinde biriken karni kömürü",
       "Aglomere edilmiş linyit briketi",
       "Yeraltında gazlaştırma yoluyla elde edilen gaz",
       "Linyitten çıkarılan montan mumu"],
      "A", "Olumsuz teşhis",
      "27.12 Açıklama Notu, cilt bakımına uygun ve bu kullanım için perakende ambalajlanmış vazelini 33.04’e gönderir. "
      "Karni kömürü 27.04’te, aglomere linyit 27.02’de, yeraltı gazlaştırma gazı 27.05’te, montan (linyit) mumu 27.12’de kalır.",
      "27.12 Açıklama Notu; Fasıl 27 Genel Açıklamalar (b); 27.02, 27.04, 27.05 Açıklama Notları.", 27),

    # 9 – Fasıl 10 · Sıralama (E)
    S("Aşağıdaki eşyanın Tarife Cetvelindeki pozisyon numaralarına göre küçükten büyüğe doğru dizilişi hangisidir?"
      "<br/>I. Kırık pirinç<br/>II. Yassılaştırılmış yulaf<br/>III. Çavdar<br/>IV. Kinoa<br/>V. Tohumluk mısır",
      ["III – II – V – I – IV", "III – V – IV – I – II", "V – III – I – IV – II",
       "III – V – I – II – IV", "III – V – I – IV – II"],
      "E", "Sıralama",
      "Çavdar 10.02, tohumluk mısır 10.05, kırık pirinç 10.06, kinoa 10.08’dedir. Yassılaştırılmış yulaf işlenmiş tane "
      "olduğundan 10.04’te değil 11.04’te yer alır ve sıranın sonuna gider; tuzak budur.",
      "Fasıl 10 Not 1(B); 10.02, 10.05, 10.06, 10.08 ve 11.04 pozisyon metinleri.", 10),

    # 10 – Fasıl 35 · Eşya → 4’lü pozisyon (C)
    S("Tarife Cetveline göre, mersin balığının hava keselerinin mekanik işleme tabi tutulmasıyla elde edilen, yarı saydam "
      "ince tabakalar halindeki ve bira ile şarabın berraklaştırılmasında kullanılan katı ihtiyokol hangi pozisyonda sınıflandırılır?",
      ["05.11", "35.04", "35.03", "35.02", "35.06"],
      "C", "Eşya → 4’lü pozisyon",
      "35.03 pozisyon metni katı ihtiyokolu jelatin ve hayvansal menşeli tutkallarla birlikte sayar. Hava kesesinden elde "
      "edilse de işlenmemiş hayvansal ürün (05.11) değildir; albüminler 35.02’de, diğer proteinler 35.04’te yer alır.",
      "35.03 pozisyon metni ve Açıklama Notu.", 35),

    # 11 – Fasıl 44 · Farklı/aynı pozisyon veya fasıl (A)
    S("Aşağıdaki ahşap eşyadan hangisi diğerlerinden <b>farklı</b> bir tarife pozisyonunda yer alır?",
      ["Kibrit çöpü imalinde kullanılan ağaç şeritler", "Arı kovanı", "Tabut",
       "Ayakkabı tabanlarını tutturmada kullanılan ağaç çivi", "Elbise askısı"],
      "A", "Farklı/aynı pozisyon veya fasıl",
      "Arı kovanı, tabut, ağaç ayakkabı çivisi ve elbise askısı 44.21 (ahşap diğer eşya) kapsamındadır. Kibrit çöpü "
      "imalinde kullanılan ağaç şeritler ise 44.21 Açıklama Notu uyarınca şerit halindeki ağaç olarak 44.04’te yer alır.",
      "44.21 Açıklama Notu; 44.04 pozisyon metni.", 44),

    # 12 – GYK · Genel Yorum Kuralı (D)
    S("Fasıl 95’in başlığı oyuncakları ve spor malzemelerini anmasına karşın, iki tekerlekli çocuk bisikletinin bu fasılda "
      "değil 87.12 pozisyonunda sınıflandırılması hangi Genel Yorum Kuralının gereğidir?",
      ["GYK 3(a) – 87.12 eşyayı daha özel tanımladığı için",
       "GYK 3(c) – numara sırasına göre en son pozisyon olduğu için",
       "GYK 4 – en çok benzediği eşya yetişkin bisikleti olduğu için",
       "GYK 1 – Fasıl 95 Not 1(o) ve 87.12 pozisyon metni gereğince",
       "GYK 2(a) – bisikletin esas niteliğini taşıdığı için"],
      "D", "Genel Yorum Kuralı",
      "GYK 1’e göre fasıl başlıkları yalnızca gösterici niteliktedir; sınıflandırma pozisyon metinleri ve notlara göre yapılır. "
      "Fasıl 95 Not 1(o) çocuk bisikletlerini 87.12’ye gönderir; notla çözülen durumda GYK 3’e geçilmez, 3(c) zaten 95.03’ü gösterirdi.",
      "GYK 1; Fasıl 95 Not 1(o); 87.12 pozisyon metni.", "GYK"),

    # 13 – Fasıl 34 · Eşya → 4’lü pozisyon (B)
    S("Tarife Cetveline göre, süt işletmelerinde ve bira fabrikalarında yağ giderme amacıyla kullanılan, esası kostik soda "
      "gibi alkalin maddeler olan ve az miktarda yüzey aktif madde içeren temizleme müstahzarı hangi pozisyonda sınıflandırılır?",
      ["28.15", "34.02", "34.05", "38.24", "34.01"],
      "B", "Eşya → 4’lü pozisyon",
      "34.02 Açıklama Notu (C), esası sabun veya yüzey aktif madde olmayan, sütçülükte ve biracılıkta kullanılan alkalin "
      "esaslı yağ giderme müstahzarlarını bu pozisyona alır. Müstahzar olduğundan kostik soda (28.15) değildir; aşındırıcı "
      "içermediği için 34.05’e de girmez.",
      "34.02 Açıklama Notu (C)(ii).", 34),

    # 14 – Fasıl 2 · Fasıl notu · Tanım/Eşik (E)
    S("Fasıl 2 Genel Açıklamalarına göre bir et veya sakatatın Fasıl 2’de kalıp kalmayacağının belirlenmesinde aşağıdakilerden "
      "hangisi dikkate alınan ölçütlerden <b>değildir</b>?",
      ["İnsan tüketimine uygun olup olmadığı",
       "Herhangi bir şekilde pişirilmiş olup olmadığı",
       "Biber ve tuz gibi baharatlarla işlem görüp görmediği",
       "Sucuk, sosis veya benzeri ürün haline getirilip getirilmediği",
       "Papain gibi proteolitik enzimlerle yumuşatılıp yumuşatılmadığı"],
      "E", "Fasıl notu · Tanım/Eşik",
      "Genel Açıklamalara göre taze, soğutulmuş, dondurulmuş, tuzlanmış, kurutulmuş veya tütsülenmiş et, proteolitik "
      "enzimlerle yumuşatılsa da Fasıl 2’de kalır. İnsan tüketimine uygun olmayanlar 05.11’e, pişirilmiş veya baharatlı "
      "et 16.02’ye, sucuk-sosis 16.01’e gider.",
      "Fasıl 2 Notu; Fasıl 2 Genel Açıklamaları.", 2),

    # 15 – Fasıl 85 · Pozisyon → eşya (C)
    S("Aşağıdakilerden hangisi 85.05 pozisyonunda sınıflandırılır?",
      ["Göz doktorlarınca kullanılmak üzere tasarlanmış elektromıknatıs",
       "Bağlayıcısıyla birlikte toz halinde sunulan manyetik ferrit",
       "Ayrı olarak sunulan, oyuncak olarak kullanılan küçük daimi mıknatıs",
       "Manyetik kilitleri açmaya yarayan, iki plastik tabaka arasına lamine edilmiş manyetik kart",
       "Elektromanyetik tertibatla kumanda edilen havalı fren"],
      "C", "Pozisyon → eşya",
      "85.05 Açıklama Notuna göre daimi mıknatıslar, oyuncak olarak kullanılan küçük mıknatıslar dahil, kullanıldıkları yere "
      "bakılmaksızın bu pozisyondadır. Göz doktoru elektromıknatısı 90.18’e, bağlayıcılı ferrit tozu 38.24’e, manyetik kart "
      "85.23’e gider; elektromanyetik kumandalı havalı fren kapsam dışıdır.",
      "85.05 Açıklama Notu.", 85),

    # 16 – Fasıl 28 · Senaryo (A)
    S("Bir ürünün özellikleri şöyledir: sulu sodyum borat çözeltisinin hidrojen peroksit ile işlenmesiyle elde edilmiştir; "
      "beyaz kristal toz halindedir; yapısındaki oksijeni kolayca bırakır; deterjan ve ağartıcı imalatında hammadde olarak "
      "kullanılacaktır; başka madde katılmamış olup dökme torbalarda sunulmuştur. Bu ürün hangi pozisyonda sınıflandırılır?",
      ["28.40", "28.47", "28.10", "34.02", "25.28"],
      "A", "Senaryo",
      "Tarif edilen ürün sodyum peroksiborattır (perboraks); 28.40 pozisyonu boratlarla birlikte peroksiboratları da kapsar. "
      "Hidrojen peroksitle elde edilmesi onu 28.47’ye, bor içermesi 28.10’a götürmez; müstahzar olmadığından 34.02’ye, "
      "doğal borat olmadığından 25.28’e girmez.",
      "28.40 pozisyon metni ve Açıklama Notu (B).", 28),

    # 17 – Fasıl 41 · Farklı/aynı pozisyon veya fasıl (E)
    S("Aşağıdaki ikililerden hangisinde yer alan deriler Tarife Cetvelinde <b>farklı</b> pozisyonlarda sınıflandırılır?",
      ["Tüyleri alınmamış, kurutulmuş ham ren geyiği derisi – Tüyleri alınmamış, tuzlanmış ham ceylan derisi",
       "Bütün halde, tuzlanmış ham bufalo derisi – Krupon halinde, kireçlenmiş ham at derisi",
       "Kılları alınmış, kromla dabaklanmış yaş (wet-blue) kanguru derisi – Kromla dabaklanmış yaş (wet-blue) yılan derisi",
       "Kılları alınmış, parşömine edilmiş sığır derisi – Kılları alınmış, dabaklandıktan sonra boyanıp bitirilmiş sığır derisi",
       "Geri alınabilir ön dabaklamaya tabi tutulmuş, kılları alınmış keçi derisi – Dabaklanmış ve ara kurutulmuş (crust) keçi derisi"],
      "E", "Farklı/aynı pozisyon veya fasıl",
      "Not 2(A) gereği geri alınabilir ön dabaklama görmüş deri ham sayılır; keçi derisi 41.03’te kalır, dabaklanmış veya crust "
      "keçi derisi ise 41.06’dadır. Diğer ikililer sırasıyla 41.03, 41.01, 41.06 ve 41.07’de birlikte yer alır.",
      "Fasıl 41 Not 1(c) ve 2(A); 41.01–41.07 pozisyon metinleri.", 41),

    # 18 – Fasıl 90 · Olumsuz teşhis (D)
    S("Aşağıdakilerden hangisi 90.19 pozisyonunda <b>sınıflandırılmaz</b>?",
      ["Su ve hava karışımını basınçla kullanarak vücuda masaj yapan hidromasaj cihazı",
       "Pilotların reaksiyonlarını test etmek için değişen hızlarda dönüp aniden durdurulan koltuk",
       "Yatak yaralarını önlemek için vücut ağırlığının dayandığı yeri sürekli değiştiren yatak",
       "Hiperbarik ve dekompresyon odası",
       "Diş etlerine ilaç püskürtmeye mahsus, basınçlı gazla çalışan aerosol el spreyi"],
      "D", "Olumsuz teşhis",
      "90.19 Açıklama Notu hiperbarik ve dekompresyon odalarını kapsam dışında bırakıp 90.18’e gönderir. Hidromasaj cihazı "
      "ve yatak yarasını önleyen yatak masaj aleti, pilot test koltuğu psikotekni cihazı, diş eti spreyi aeroterapi aleti "
      "olarak 90.19’dadır.",
      "90.19 Açıklama Notu.", 90),

    # 19 – Fasıl 30 · Fasıl notu · Tanım/Eşik (B)
    S("Fasıl 30 Not 4’e göre kolostomi, ileostomi ve ürostomi torbalarının 30.06 pozisyonunda sınıflandırılabilmesi için "
      "aranan şart aşağıdakilerden hangisidir?",
      ["Steril ambalajda sunulmaları",
       "Ostomi kullanımına mahsus olduğu belirlenebilen şekil verilerek kesilmiş olmaları",
       "Kullanım talimatıyla birlikte perakende satış için ambalajlanmış olmaları",
       "İlaç emdirilmiş veya ilaçla kaplanmış olmaları",
       "Yalnızca plastik maddeden yapılmış olmaları"],
      "B", "Fasıl notu · Tanım/Eşik",
      "Not 4(l), ostomi kullanımına mahsus olduğu belirlenebilen, şekil verilerek kesilmiş torba ve cihazları, yapışkan "
      "parça ve kapaklarıyla birlikte 30.06’ya alır. Sterillik, perakende ambalaj veya malzeme şartı aranmaz; ilaç "
      "emdirme ölçütü 30.05’e ilişkindir.",
      "Fasıl 30 Not 4(l).", 30),

    # 20 – GYK · Genel Yorum Kuralı (C)
    S("Başları bakırdan, gövdeleri çelikten olan ve ağırlıkça çelik kısmı bakır kısmından fazla olan küçük çiviler hangi "
      "pozisyonda ve hangi Genel Yorum Kuralına göre sınıflandırılır?",
      ["73.17 – GYK 1 (Bölüm XV Not 7 uyarınca ağırlıkça üstün metal)",
       "74.15 – GYK 3(c)",
       "74.15 – GYK 1 (pozisyon metni)",
       "73.17 – GYK 3(b)",
       "74.15 – GYK 2(b)"],
      "C", "Genel Yorum Kuralı",
      "Bölüm XV Not 7 ağırlıkça üstün metali esas alır, ancak pozisyon metinlerinde aksine hüküm yoksa uygulanır. 74.15 "
      "başları bakır, gövdeleri demir-çelik çivileri açıkça sayar, 73.17 de bunları hariç tutar; sonuç GYK 1 ile bulunur.",
      "GYK 1; Bölüm XV Not 7 ve Genel Açıklamalar (B); 73.17 ve 74.15 pozisyon metinleri.", "GYK"),
]

d = {"tur": "karma", "no": 8, "sorular": sorular}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("yazıldı:", OUT, len(sorular))
