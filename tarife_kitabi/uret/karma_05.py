#!/usr/bin/env python3
"""Karma test 5 üreticisi → KITAP/karma/karma_05.json"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def q(soru, secenekler, cevap, tip, gerekce, dayanak, fasil):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


S = []

# 1 – Genel · Tarife yapısı (C)
S.append(q(
    "Tarife Cetvelinde aşağıdaki bölümlerden hangisi yalnızca tek bir fasıldan oluşur?",
    ["Bölüm V", "Bölüm VII", "Bölüm III", "Bölüm XVIII", "Bölüm XII"],
    "C", "Tarife yapısı",
    "Bölüm III yalnız Fasıl 15’ten (katı ve sıvı yağlar) oluşur. Bölüm V 25–27, Bölüm VII 39–40, "
    "Bölüm XII 64–67, Bölüm XVIII 90–92. fasılları kapsar; tek fasıllı bölümlere başka örnekler XIV (Fasıl 71) ve XIX (Fasıl 93)’dur.",
    "Tarife Cetveli İçindekiler (bölüm–fasıl listesi).",
    "Genel"))

# 2 – Fasıl 1 · Olumsuz teşhis (E)
S.append(q(
    "Aşağıdaki canlı hayvanlardan hangisi Tarife Cetvelinin 1. faslında <b>sınıflandırılmaz</b>?",
    ["Canlı tavus kuşu", "Canlı kuğu", "Canlı yılan", "Canlı ayı", "Canlı deniz anası"],
    "E", "Olumsuz teşhis",
    "Fasıl 1 notu 03.01, 03.06, 03.07 ve 03.08’e giren su hayvanlarını hariç tutar; deniz anası 03.08’deki "
    "su omurgasızıdır. Tavus kuşu, kuğu, yılan ve ayı 01.06’da kalır; “canlı” olmak tek başına yetmez.",
    "Fasıl 1 Notu; 01.06 ve 03.08 Açıklama Notları.",
    1))

# 3 – Fasıl 70 · Fasıl/Bölüm bulma (B)
S.append(q(
    "Balık ağlarına takılmak üzere camdan yapılmış yüzdürücüler, Tarife Cetvelinin hangi bölümünde yer alır?",
    ["Bölüm XI", "Bölüm XIII", "Bölüm XX", "Bölüm XVII", "Bölüm VII"],
    "B", "Fasıl/Bölüm bulma",
    "Balık ağlarına mahsus camdan yüzdürücüler 70.20 (camdan diğer eşya) Açıklama Notunda sayılır; Fasıl 70 "
    "XIII. Bölümdedir. Olta ile balıkçılık eşyası (Fasıl 95, Bölüm XX) ve ağların kendisi (Bölüm XI) çeldiricidir.",
    "70.20 Açıklama Notu; Bölüm XIII (Fasıl 68–70).",
    70))

# 4 – Fasıl 4 · Eşya → 4’lü pozisyon (D)
S.append(q(
    "Konsantre edilerek toz haline getirilmiş ve ilave şeker içeren yayıkaltı, Tarife Cetvelinde hangi tarife "
    "pozisyonunda sınıflandırılır?",
    ["04.02", "04.01", "04.04", "04.03", "19.01"],
    "D", "Eşya → 4’lü pozisyon",
    "04.03 metni yayıkaltını konsantre edilmiş veya ilave şekerli halleriyle kapsar; ürün toz da olabilir. "
    "04.02 konsantre veya şekerli süt ve kremayı alır, ancak fermente veya asitliği artırılmış olanları 04.03’e bırakır.",
    "04.03 pozisyon metni ve Açıklama Notu; 04.02 Açıklama Notu.",
    4))

# 5 – Fasıl 82 · Eşya → 4’lü pozisyon (A)
S.append(q(
    "Berberlerin kullandığı, elle çalıştırılan ve elektrik motoru bulunmayan adi metalden saç kesme makinesi, "
    "Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?",
    ["82.14", "85.10", "82.13", "84.36", "82.12"],
    "A", "Eşya → 4’lü pozisyon",
    "82.14 Açıklama Notu elle çalışan, elektriksiz saç kesme cihazlarını bu pozisyonda sayar. Elektrik motorlu "
    "olanlar 85.10’a, sehpalı mekanik hayvan kırkma cihazları 84.36’ya gider; makas (82.13) ve tıraş makinası (82.12) çeldiricidir.",
    "82.14 pozisyon metni ve Açıklama Notu.",
    82))

# 6 – Fasıl 21 · Olumsuz teşhis (C)
S.append(q(
    "Aşağıda sayılan eşyadan hangisi Tarife Cetvelinin 21 inci faslında <b>sınıflandırılmamaktadır</b>?",
    ["Kahve yerine kullanılan kavrulmuş palamut (palamut kahvesi)", "Mantar sosu",
     "Karamelize edilmiş şekerden ibaret karamel", "Buzlu şekerleme", "Destilasyon mayası"],
    "C", "Olumsuz teşhis",
    "21.01 Açıklama Notu karamelize melas ve karamelize şekerden oluşan karameli hariç tutup 17.02’ye gönderir. "
    "Palamut kahvesi 21.01’de, mantar sosu 21.03’te, buzlu şekerleme 21.05’te, destilasyon mayası 21.02’de kalır.",
    "21.01 Açıklama Notu (hariçler); 21.02, 21.03 ve 21.05 Açıklama Notları.",
    21))

# 7 – Fasıl 48 · Eşya → 4’lü pozisyon (E)
S.append(q(
    "Yaprakları kağıttan, çerçevesi bambudan yapılmış, açılıp kapanan el yelpazesi Tarife Cetvelinde hangi "
    "tarife pozisyonunda sınıflandırılır?",
    ["46.02", "67.01", "63.07", "71.13", "48.23"],
    "E", "Eşya → 4’lü pozisyon",
    "48.23 Açıklama Notu, çerçevesi herhangi bir maddeden olan kağıttan açılıp kapanan el yelpazelerini sayar. "
    "Çerçevesi kıymetli metalden olanlar 71.13’e; yaprakları mensucattan olanlar 63.07’ye, tüylü süs yelpazeleri 67.01’e gider.",
    "48.23 Açıklama Notu; 63.07 ve 67.01 Açıklama Notları.",
    48))

# 8 – GYK (A)
S.append(q(
    "Yalnızca toplama tertibatı takılmamış, bunun dışında tamamlanmış bir elektrik sayacının asli karakterini "
    "taşıyan cihaz, hangi yorum kuralına göre hangi pozisyonda sınıflandırılır?",
    ["GYK 1 ve 2(a) – 90.28", "GYK 1 – 90.33 (aksam ve parça olarak)", "GYK 3(b) – 90.28",
     "GYK 3(a) – 90.30", "GYK 4 – 85.43"],
    "A", "Genel Yorum Kuralı",
    "GYK 2(a), asli karakteri taşıyan eksik eşyayı tamamlanmış eşya gibi sınıflandırır; Fasıl 90 Genel "
    "Açıklamaları toplama tertibatı takılmamış elektrik sayacını örnek verir. 90.33 yalnız parçalar içindir; "
    "90.30 elektrik sayaçlarını hariç tutar.",
    "GYK 2(a); Fasıl 90 Genel Açıklamalar (II); 90.28 ve 90.30 pozisyon metinleri.",
    "GYK"))

# 9 – Fasıl 61 · Farklı/aynı pozisyon (B)
S.append(q(
    "Aşağıdaki örme eşyadan hangisi Tarife Cetvelinde diğerlerinden farklı bir tarife pozisyonunda yer alır?",
    ["Örme jokey kıyafeti", "Yağmurluğun içine takılıp çıkarılabilen, ayrı sunulan örme astar",
     "Cerrahların giydiği örme önlük", "Örme papaz cüppesi", "Havacılar için elektrikle ısıtılan örme giysi"],
    "B", "Farklı/aynı pozisyon veya fasıl",
    "Yağmurluklara takılıp çıkarılabilen ve ayrı sunulan astarlar 61.17’de giysi aksesuarı olarak sayılır. "
    "Önlük, papaz cüppesi, havacılara mahsus ısıtmalı giysi ve jokey kıyafeti 61.14’teki diğer giyim eşyasıdır.",
    "61.14 ve 61.17 Açıklama Notları.",
    61))

# 10 – Fasıl 24 · Olumsuz teşhis (D)
S.append(q(
    "Tütün veya nikotinle ilgili aşağıdaki ürünlerden hangisi Tarife Cetvelinin 24. faslında <b>yer almaz</b>?",
    ["Tütün ile tütün yerine geçen madde karışımından yapılmış sigarillo",
     "Karbon ısı kaynağıyla ısıtılarak yanmadan solunan, tütün granülleri içeren ürün",
     "Tütün içermeyen, ağızda çözünerek nikotin veren pastil",
     "Tıbbi sigara",
     "Tıbbi özelliği olmayan, sigara içme alışkanlığını kırmaya yönelik formüle edilmiş özel sigara"],
    "D", "Olumsuz teşhis",
    "Fasıl 24 notu tıbbi sigaraları kapsam dışı bırakır (Fasıl 30). Alışkanlık kırıcı ancak tıbbi özelliği "
    "olmayan sigaralar ve karışım sigarillolar 24.02’de; yanmadan solunan tütünlü ürünler ve tütünsüz nikotinli "
    "ağız ürünleri 24.04’te kalır.",
    "Fasıl 24 Not 1; 24.02 ve 24.04 Açıklama Notları.",
    24))

# 11 – Fasıl 66 · Fasıl notu · Tanım/Eşik (E)
S.append(q(
    "Aşağıdaki eşyalardan hangisi ile ilgili Tarife Cetvelinin 66. Fasıl notlarında açıklama "
    "<b>bulunmamaktadır</b>?",
    ["Ölçü gösteren bastonlar", "Kılıçlı bastonlar", "Oyuncak güneş şemsiyeleri", "Şemsiye kılıfları",
     "Koltuk değnekleri"],
    "E", "Fasıl notu · Tanım/Eşik",
    "Fasıl 66 notları ölçü gösteren bastonları (90.17), kılıçlı bastonları (Fasıl 93), oyuncak şemsiyeleri "
    "(Fasıl 95) ve takılmamış kılıfları düzenler. Koltuk değnekleri ise notlarda değil, yalnız 66.02 Açıklama "
    "Notunda geçer ve 90.21’e gönderilir.",
    "Fasıl 66 Not 1 ve 2; 66.02 Açıklama Notu.",
    66))

# 12 – Genel · Tarife yapısı (B)
S.append(q(
    "Tarife Cetvelinin XVII. Bölümünde yer alan fasıllardan birinin 8. pozisyonu aşağıdakilerden hangisi olabilir?",
    ["84.08", "87.08", "90.08", "73.08", "70.08"],
    "B", "Tarife yapısı",
    "4’lü kodun ilk iki rakamı faslı, son iki rakamı fasıl içindeki sırayı gösterir. XVII. Bölüm (nakil vasıtaları) "
    "86–89. fasılları kapsar; Fasıl 84 XVI., 90 XVIII., 73 XV., 70 ise XIII. Bölümdedir.",
    "Tarife Cetveli İçindekiler; Bölüm XVII (Fasıl 86–89).",
    "Genel"))

# 13 – Fasıl 47 · Eşya → 4’lü pozisyon (A)
S.append(q(
    "Hububat saplarının (samanın) kimyasal işlemlerle liflerine ayrıştırılmasıyla elde edilen ve balyalanmış "
    "levhalar halinde sunulan kağıt hamuru, Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?",
    ["47.06", "47.03", "12.13", "47.05", "47.01"],
    "A", "Eşya → 4’lü pozisyon",
    "47.06 odun dışındaki lifli selülozik maddelerin hamurlarını kapsar; Fasıl 47 Genel Açıklamaları tahıl "
    "saplarını bu maddeler arasında sayar. 47.01–47.05 yalnız odun hamurlarıdır; işlenmemiş saman ise 12.13’tedir.",
    "Fasıl 47 Genel Açıklamalar; 47.06 pozisyon metni ve Açıklama Notu.",
    47))

# 14 – Fasıl 83 · Pozisyon → eşya (C)
S.append(q(
    "Tarife Cetveline göre aşağıdakilerden hangisi 83.09 pozisyonunda sınıflandırılır?",
    ["Esası porselen olan, yaylı manivelalı şişe tıpası",
     "Elektrikli süpürge hortumunda kullanılan, metal şeridin helezoni sarılmasıyla yapılmış eğilip bükülebilen boru",
     "Torbaları mühürlemeye mahsus, iki plastik şerit arasına sıkıştırılmış çelik telden bağlama tertibatı",
     "El çantalarına mahsus, kilitle donatılmış mesnetli kanca",
     "Üzerinde harf veya rakam bulunmayan, esas bilgileri sonradan eklenecek adi metal levha"],
    "C", "Pozisyon → eşya",
    "83.09 Açıklama Notu torba ve benzeri kapları mühürlemek için plastik veya kağıt şeritler arasına sıkıştırılan "
    "çelik telli bağlama tertibatını sayar. Esası porselen tıpalar hariçtir; boru 83.07, kilitli kanca 83.01’dedir; "
    "harfsiz levha 83.10’a da girmez.",
    "83.09 Açıklama Notu; 83.01, 83.07 ve 83.10 Açıklama Notları.",
    83))

# 15 – Fasıl 84 · Farklı/aynı pozisyon (D)
S.append(q(
    "Aşağıdaki tarım makinelerinden hangisi Tarife Cetvelinde diğerlerinden farklı bir tarife pozisyonunda yer alır?",
    ["Yumurtaları ağırlıklarına göre ayıran makine", "Patatesleri büyüklüklerine göre ayıran ve temizleyen makine",
     "Ot ve saman balyalama presi",
     "Tohumları hava akımıyla temizleyip ağırlık ve şekillerine göre ayıran selektör",
     "Üzüm toplama makinesi"],
    "D", "Farklı/aynı pozisyon veya fasıl",
    "Yumurta ve patates tasnif makineleri, balyalama presi ve üzüm toplama makinesi 84.33’tedir. 84.33, kuru "
    "baklagil, hububat ve tohumlara mahsus tasnif makinelerini hariç tutar; tohum selektörleri 84.37’de yer alır.",
    "84.33 ve 84.37 pozisyon metinleri ve Açıklama Notları.",
    84))

# 16 – Fasıl 87 · Olumsuz teşhis (A)
S.append(q(
    "Ayrı olarak sunulduğunda aşağıdakilerden hangisi 87.14 pozisyonunda <b>sınıflandırılmaz</b>?",
    ["Bisikletlere mahsus, adi metalden elektriksiz zil", "Motosiklet duruş ayağı", "Bisiklet gidonu",
     "Motosiklet susturucusu", "Engelli taşıtlarına mahsus manivela iticisi"],
    "A", "Olumsuz teşhis",
    "Bölüm XVII Not 2(d), 83.06’ya giren eşyayı taşıt aksamı saymaz; bisiklet zilleri 83.06 Açıklama Notunda "
    "açıkça sayılır. Duruş ayağı, gidon, susturucu ve manivela iticisi 87.14 Açıklama Notundaki aksam listesindedir.",
    "Bölüm XVII Not 2(d); 83.06 ve 87.14 Açıklama Notları.",
    87))

# 17 – Fasıl 52 · Eşya → 4’lü pozisyon (B)
S.append(q(
    "Ağırlıkça %88 pamuk ve %12 ipekten oluşan, m2 ağırlığı 260 g olan, farklı renkteki ipliklerden dokunmuş "
    "mensucat Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?",
    ["52.08", "52.09", "52.12", "52.11", "50.07"],
    "B", "Eşya → 4’lü pozisyon",
    "Bölüm XI Not 2 uyarınca ağırlıkça üstün gelen lif pamuk olduğundan Fasıl 52’ye girer. %85 veya daha fazla "
    "pamuk içerip m2 ağırlığı 200 g’ı geçtiği için 52.09’dadır; 52.12 “diğer”, 52.11 sentetik veya suni lif karışımları içindir.",
    "Bölüm XI Not 2(A); 52.09 pozisyon metni.",
    52))

# 18 – Fasıl 90 · Fasıl notu · Tanım/Eşik (E)
S.append(q(
    "Fasıl 90 Not 4 hükmü dikkate alındığında aşağıdakilerden hangisi 90.05 pozisyonunda değil, 90.13 "
    "pozisyonunda sınıflandırılır?",
    ["Kızılötesi görüntüyü görünür hale getiren tüplerle donatılmış gece çift gözlü dürbünü",
     "Aynalı astronomik teleskop", "Tiyatro dürbünü", "Jetonla çalışan, sehpalı seyir dürbünü",
     "Tankların bünyesinde kullanılan periskopik teleskop"],
    "E", "Fasıl notu · Tanım/Eşik",
    "Fasıl 90 Not 4; silahlara ait teleskopik dürbünleri, denizaltı veya tanklar için periskopik teleskopları ve "
    "bu fasıl ile Bölüm XVI makinalarına ait teleskopları 90.05’ten çıkarıp 90.13’e gönderir. Diğer seçenekler "
    "90.05 Açıklama Notunda sayılır.",
    "Fasıl 90 Not 4; 90.05 Açıklama Notu.",
    90))

# 19 – GYK (C)
S.append(q(
    "Genel Yorum Kuralları ve açıklama notlarıyla ilgili aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
    ["Bölüm ve fasıl başlıkları ile pozisyon metni çeliştiğinde sınıflandırmada başlıklar esas alınır.",
     "3(c) kuralına göre eşya, geçerli olabilecek pozisyonlardan numara sırasına göre ilkinde sınıflandırılır.",
     "3(b) anlamında bileşik eşya, birbirini tamamlayan ve ayrı satışa sunulmayan ayrılabilir parçalı eşyayı da kapsar.",
     "5(a) kuralı, bir bütün olarak esas niteliği mahfaza olan eşyaya da uygulanır.",
     "3(b) kuralı, imalatta kullanılmak üzere belirli miktarlarda ayrı ayrı paketlenip ortak ambalajda sunulan eşyaya da uygulanır."],
    "C", "Genel Yorum Kuralı",
    "Açıklama notu, birbirini tamamlayan ve ayrı satılmayan ayrılabilir parçalı eşyayı (kaideli kül tablası gibi) "
    "3(b) bileşik eşyası sayar. Başlıklar yasal değildir; 3(c) sonuncuyu seçer; 5(a) esas niteliği mahfaza olana, "
    "3(b) üretim için ayrı paketlenen eşyaya uygulanmaz.",
    "GYK 1, 3(b), 3(c), 5(a) ve Açıklama Notları.",
    "GYK"))

# 20 – Fasıl 54 · Senaryo (D)
S.append(q(
    "Bir firma; viskoz (rejenere selüloz) çözeltisinin dar yarıklardan geçirilmesiyle elde edilen, “suni saman” "
    "olarak bilinen yassı şeritleri, uzunlamasına katlanmış ve hafifçe bükülmüş halde bobinlere sarılı olarak ithal "
    "etmektedir. Şeritlerin açık genişliği 9 mm, katlı ve bükülü haldeki görünen genişliği 4 mm’dir. Şapka ve çanta "
    "örücülüğünde kullanılacak bu eşya Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?",
    ["54.04", "39.20", "46.01", "54.05", "54.03"],
    "D", "Senaryo",
    "Viskoz suni liftir; 54.05 görünen genişliği 5 mm’yi geçmeyen suni şeritleri (suni saman) kapsar ve katlı "
    "veya bükülü şeritte görünen genişlik esas alınır. 54.04 sentetik şeritler içindir; görünen genişlik 5 mm’yi "
    "aşsaydı Fasıl 39 gündeme gelirdi.",
    "Fasıl 54 Not 1(b); 54.05 pozisyon metni; 54.04 Açıklama Notu.",
    54))


def main():
    assert len(S) == 20
    out = {"tur": "karma", "no": 5, "sorular": S}
    path = os.path.join(ROOT, "karma", "karma_05.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for i, s in enumerate(S, 1):
        g = s["gerekce"]
        print(i, s["cevap"], s["fasil"], len(g), len(g.split()))
    print("yazıldı:", path)


if __name__ == "__main__":
    main()
