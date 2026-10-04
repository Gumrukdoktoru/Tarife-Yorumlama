#!/usr/bin/env python3
import json, os

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def Q(soru, secenekler, cevap, tip, gerekce, dayanak):
    assert len(secenekler) == 5 and cevap in "ABCDE"
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


d = {
    "tur": "fasil",
    "fasil": 92,
    "baslik": "Müzik aletleri; bunların aksam, parça ve aksesuarı",
    "bolum": "XVIII",
    "oz": {
        "vurgu": "Fasıl 92’de önce eşyanın gerçek bir müzik aleti olup olmadığına (oyuncak, Fasıl 85 cihazı, elektronik müzik modülü değil) bakılır; sonra sesin nasıl üretildiğine: klavyeli telli 92.01, diğer telli 92.02, nefesli 92.05, vurmalı 92.06, elektriksiz normal çalınamayan elektrikli-elektronik alet 92.07, bunların dışında kalan müzik kutusu, düdük ve benzerleri 92.08; parça, aksesuar, metronom ve diyapozon 92.09.",
        "maddeler": [
            "Elektrikli pikap veya amplifikatör takılı olsa da bu tertibat olmadan çalınabilen mutat alet kendi pozisyonunda kalır (ses kutulu gitar 92.02); elektrik olmadan normal çalınamayan alet 92.07’dedir (ses kutusu olmayan elektro gitar, elektronik org). Elektrikli otomatik piyano ise 92.01’de kalır.",
            "Alete takılmamış veya aynı kabine yerleştirilmemiş mikrofon, amplifikatör, hoparlör, kulaklık Fasıl 85 veya 90’da; elektronik müzik modülleri 85.43’te; oyuncak niteliğindeki aletler 95.03’te; tripodlar 96.20’de; temizleme fırçaları 96.03’tedir.",
            "Not 2: 92.02 ve 92.06 aletleriyle birlikte gelen, normal sayıdaki yay ve bagetler aletle aynı pozisyonda; 92.09’daki kart, disk ve rulolar ise aletle gelse bile ayrı eşyadır.",
            "92.03 ve 92.04 numaraları boştur; akordeonlar ve klavyeli borulu orglar nefesli aletler pozisyonu 92.05’tedir."
        ]
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Oyuncak niteliğinde mi? (malzeme, kaba işçilik, müzikal kusur)", "<b>95.03</b>"],
            ["2", "Koleksiyon eşyası veya 100 yılı aşkın antika mı?", "<b>97.05</b> / <b>97.06</b>"],
            ["3", "Alete takılmamış mikrofon, amplifikatör, hoparlör ya da elektronik müzik modülü mü?", "Fasıl 85 (<b>85.18</b>, <b>85.43</b>) / Fasıl 90"],
            ["4", "Ses elektrikle üretiliyor veya yükseltiliyor ve alet elektriksiz normal çalınamıyor mu?", "<b>92.07</b>*"],
            ["5", "Klavyeli telli alet mi? (piyano, otomatik piyano, klavsen, spinet)", "<b>92.01</b>"],
            ["6", "Diğer telli alet mi? (keman, kontrbas, gitar, mandolin, arp, czimbalo)", "<b>92.02</b>"],
            ["7", "Nefesli alet mi? (borulu org, armonyum, akordeon, armonika, flüt, trompet, gayda)", "<b>92.05</b>"],
            ["8", "Vurmalı alet mi? (davul, ksilofon, zil, kastanyet, selesta, karillon)", "<b>92.06</b>"],
            ["9", "Müzik kutusu, orkestriyon, laterna, fuar orgu, mekanik öten kuş, müzik testeresi, düdük, av çağrı aleti mi?", "<b>92.08</b>"],
            ["10", "Parça, aksesuar, tel, metronom, diyapozon, akort düdüğü, kart-disk-rulo mu?", "<b>92.09</b>"]
        ],
        "dipnot": "* Delikli rulolarla çalınan elektrikli otomatik piyano 92.07’ye değil 92.01’e girer."
    },
    "pozisyon_haritasi": [
        ["92.01", "Piyanolar, klavsenler, klavyeli telli aletler", "Klavye + tokmakla vurulan tel; otomatik piyano dahil", "Düz ve kuyruklu piyano, otomatik piyano, klavsen"],
        ["92.02", "Telli diğer müzik aletleri", "Yayla veya parmak, mızrapla çalınır", "Keman, viyolonsel, gitar, mandolin, arp"],
        ["92.03 / 92.04", "Boş pozisyon numaraları", "Kullanılmıyor; org ve akordeon 92.05’te", "—"],
        ["92.05", "Nefesli müzik aletleri", "Üfleme veya körük; fuar ve sokak orgu hariç", "Borulu org, akordeon, armonika, klarnet, trompet, gayda"],
        ["92.06", "Vurmalı müzik aletleri", "Çubuk, tokmak, elle vurma veya sallama", "Davul, darbuka, ksilofon, zil, kastanyet, selesta"],
        ["92.07", "Sesi elektrikle üretilen veya yükseltilen aletler", "Elektriksiz normal çalınamaz", "Elektronik org, ses kutusuz elektro gitar, elektronik akordeon"],
        ["92.08", "Müzik kutuları, orkestriyonlar, düdükler vb.", "Başka yerde yer almayan aletler; çağrı ve işaret aletleri", "Müzik kutusu, laterna, av çağrı düdüğü, işaret düdüğü"],
        ["92.09", "Aksam, parça, aksesuar; metronom, diyapozon", "Tel, klavye, mekanizma, kart-disk-rulo dahil", "Keman teli, piyano mekanizması, metronom, nota taşıyıcı"]
    ],
    "notlar": [
        ["Fasıl 92 Not 1", "Fasıl dışı: (a) Bölüm XV Not 2’deki genel kullanıma mahsus adi metal parçalar ve plastikten benzerleri (Fasıl 39); (b) fasıl eşyası ile kullanılan ama alete takılmamış veya aynı kabine yerleştirilmemiş Fasıl 85 veya 90’daki mikrofon, yükselteç, hoparlör, kulaklık, şalter, stroboskop vb.; (c) oyuncak niteliğindeki alet ve cihazlar (95.03); (d) müzik aleti temizleme fırçaları (96.03), monopod, bipod, tripod ve benzerleri (96.20); (e) koleksiyon eşyası, antikalar (97.05, 97.06)."],
        ["Fasıl 92 Not 2", "92.02 veya 92.06 aletlerinin çalınmasında kullanılan, aletle birlikte getirilen, aletle kullanılmaya yetecek <b>normal miktarda</b> olan ve onunla kullanılacağı açık olan yay, baget ve benzerleri aletle aynı pozisyonda sınıflandırılır. 92.09’daki kart, disk ve rulolar aletle beraber getirilse dahi aletin parçası sayılmaz; ayrı eşyadır."],
        ["Genel Açıklamalar (elektrik)", "Elektrikli pikap ve amplifikatör tertibatı olan piyano, gitar vb. mutat tipte aletler, bu tertibat olmadan da kullanılabiliyorsa kendi pozisyonlarında kalır. Aletle bütün oluşturmayan veya aynı gövdeye monte edilmemiş elektrikli tertibat 85.18’dedir. Elektrikli veya elektronik tertibat olmadan kullanılamayan aletler (92.01’deki otomatik piyanolar hariç) 92.07’dedir: elektronik gitarlar, piyanolar, orglar, akordeonlar, çan takımları gibi."],
        ["Genel Açıklamalar (hariç)", "Elektronik müzik modülleri 85.43’te. Maddesi, kaba işçiliği, müzikal kusurları veya diğer vasıfları bakımından oyuncak olduğu açıkça görülen aletler (ağız armonikası, keman, akordeon, trampet, müzik kutusu vb.) Fasıl 95’te. Koleksiyon eşyası 97.05’te, 100 yılı aşan antikalar 97.06’da."],
        ["92.01 / 92.02 Açıklama Notu", "92.01 klavyeli ve tokmakla vurulan telli piyanoları (düz, kuyruklu), delikli kağıt veya mukavva rulolarla çalınan mekanik, pnömatik veya elektrikli otomatik piyanoları, klavsen ve spinetleri kapsar; elektronik piyanolar 92.07’dedir. 92.02 yaylı (keman, viyola, viyolonsel, kontrbas) ve parmak/mızrapla çalınan (mandolin, gitar, banço, ukulele, zitar, balalayka, arp) aletleri, rüzgar arplerini ve tokmakla çalınan czimbaloları kapsar. Ses kutusu olmayan elektro gitar 92.07’dedir."],
        ["92.05 Açıklama Notu", "“Pirinç-üflemeli” terimi aletin malzemesini değil ses kalitesini ifade eder. Klavyeli borulu orglar, armonyumlar, akordeonlar ve bandonyonlar, ağız armonikaları, flüt, obua, klarnet, saksofon gibi ağaç-üflemeliler, okarinalar ve gaydalar buradadır. Orgla birlikte gelen konsol ve org zarfı 92.05’te, ayrı gelirse 92.09’dadır. Orkestriyonlar ve sokak orgları 92.08’de, elektronik org ve akordeonlar 92.07’dedir."],
        ["92.06 Açıklama Notu", "Davul, darbuka, tef, timpani, tamtam, zil, gong, üçgen, kastanyet, ksilofon, metallofon, klavyeli selesta, borulu çanlar, marakas, klave, fleksaton ve kamu binalarında müzik yayını için karillonlar buradadır. Elektronik vurmalı aletler 92.07’de; müzik aleti sayılmayan kapı veya masa zilleri ve gongları 83.06 veya 85.31’de; saatler için zil ve çanlar 91.14’tedir."],
        ["92.07 Açıklama Notu", "Aletin bünyesine girmiş veya aynı zarfa monte edilmiş elektrikli-elektronik cihazlar, taşıma kolaylığı için ayrı ambalajlanmış olsa bile aletle birlikte sınıflandırılır; aletle bütün oluşturmayan amplifikatör ve hoparlörler Fasıl 85’tedir. Piyanoya adapte edilebilen elektronik aletler piyanoyla gelsin gelmesin 92.07’dedir. Elektrikli otomatik piyanolar 92.01’dedir."],
        ["92.08 Açıklama Notu", "Müzik kutuları, orkestriyonlar, laternalar, mekanik öten kuşlar, müzik testereleri, çıngırak ve ağızla üflenen sirenler, av hayvanı çağrı düdükleri, ağızla üflenen işaret düdükleri ve çağrı kornaları buradadır. Müzik mekanizmalı saat, minyatür mobilya, vazo, seramik gibi faydalı veya hediyelik eşya ile elektronik müzik modüllü kol saati, kupa ve tebrik kartları müzik kutusu sayılmaz; mekanizmasız hallerinin pozisyonuna girer. Kapı, masa, bisiklet zilleri (83.06, 85.31), taşıt kornaları ve vapur düdükleri (maddesine göre veya Bölüm XVI–XVII), elektrikli ses işaret cihazları (85.12, 85.31) hariçtir."],
        ["92.09 Açıklama Notu", "Metronom, diyapozon (tıpta kulak muayenesinde kullanılanlar dahil) ve akort düdükleri hangi amaçla kullanılırsa kullanılsın buradadır. Müzik kutusu mekanizmaları, aletlere ait olduğu anlaşılan teller (katgüt, ipek, sentetik monofilament, metal), klavye, piyano mekanizması, org boruları, akordeon körükleri, ağızlıklar, davul derileri, aletin üzerine takılan nota taşıyıcılar ve kart, disk, rulolar buradadır. Akort aletleri 82.05, müzik kutusu yaylı motorları 84.12, saat makinaları 91.08–91.10, piyano tabureleri 94.01, yere konan nota sehpaları 94.03, piyano aydınlatma mesnetleri 94.05, kalıplanmış reçine 96.02, fırçalar 96.03’tedir; işlenmemiş tuş taslakları 96.01 veya Fasıl 39’dadır."]
    ],
    "sinir_komsulari": [
        ["Oyuncak piyano, oyuncak trampet, oyuncak ağız armonikası", "95.03", "Fasıl 92 Not 1(c); oyuncak niteliği"],
        ["Elektronik müzik modülü", "85.43", "Fasıl 92 Genel Açıklamalar"],
        ["Alete takılmamış amplifikatör, hoparlör, mikrofon", "85.18", "Fasıl 92 Not 1(b)"],
        ["Ayrı gelen müzik aleti mahfazası", "42.02", "Aletle gelirse GYK 5(a) ile aletin pozisyonunda"],
        ["Müzik aletini temizleme fırçası", "96.03", "Fasıl 92 Not 1(d)"],
        ["Müzik aleti için tripod, monopod", "96.20", "Fasıl 92 Not 1(d); alete takılan mesnet ise 92.09"],
        ["Piyano taburesi", "94.01", "92.09 hariç tutması"],
        ["Yere konularak kullanılan nota sehpası", "94.03", "92.09 hariç tutması; alete takılan nota taşıyıcı 92.09"],
        ["Piyano için aydınlatma mesneti", "94.05", "92.09 hariç tutması"],
        ["Akort anahtarı (akort aleti)", "82.05", "92.09 hariç tutması"],
        ["Müzik kutusu için diğer parçalarla donatılmamış yaylı motor", "84.12", "92.09 hariç tutması"],
        ["Kapı, masa, bisiklet zili; müzik aleti olmayan gong", "83.06 / 85.31", "92.06 ve 92.08 hariç tutmaları"],
        ["Elektrikli ses işaret cihazı, taşıt korna", "85.12 / 85.31", "92.08 hariç tutması"],
        ["Saat için zil, çan, gong", "91.14", "92.06 hariç tutması"],
        ["Müzik mekanizmalı hediyelik vazo, minyatür mobilya, saat", "Mekanizmasız halinin pozisyonu", "92.08 Açıklama Notu"],
        ["Metronom (zaman ölçse de)", "92.09", "Fasıl 91’de değil; 91.06 hariç tutması"]
    ],
    "tuzaklar": [
        "<b>Elektrik var diye 92.07 değildir.</b> Ses kutulu gitara pikap ve amplifikatör takılmış olsa da elektriksiz çalınabildiği için 92.02’dedir; ses kutusu olmayan elektro gitar 92.07’dedir.",
        "<b>Elektrikli otomatik piyano 92.01’dir.</b> 92.07’nin tek açık istisnası budur; elektronik piyano ise 92.07’dir.",
        "<b>Klavye pozisyonu belirlemez.</b> Selesta klavyelidir ama vurmalıdır (92.06); akordeon ve borulu org klavyelidir ama nefeslidir (92.05). 92.01 klavyeli <i>telli</i> aletler içindir.",
        "<b>Yay ve baget aletle gider, kart-disk-rulo gitmez.</b> Not 2 yalnızca 92.02 ve 92.06 aletlerinin normal sayıdaki yay ve bagetleri için geçerlidir; otomatik aletlerin kart, disk ve ruloları her durumda 92.09’dadır.",
        "<b>Amplifikatör aletin içinde mi?</b> Alete takılı veya aynı kabine yerleştirilmiş elektrikli cihaz aletle birlikte sınıflandırılır (ayrı ambalajlansa bile); aletle bütün oluşturmayan amplifikatör ve hoparlör Fasıl 85’e gider.",
        "<b>Müzik mekanizmalı hediyelik eşya müzik kutusu değildir.</b> Müzikli vazo, saat veya tebrik kartı mekanizmasız halinin pozisyonundadır.",
        "<b>Metronom ve diyapozon her amaçla 92.09.</b> Kulak muayenesinde kullanılan diyapozon da, sanayide kullanılan metronom da 92.09’dadır; metronom Fasıl 91’de değildir.",
        "<b>Org konsolu ve zarfı birlikte geldiği şeye göre değişir.</b> Orgla birlikte 92.05, ayrı gelirse 92.09.",
        "<b>Nota sehpası ikiye ayrılır.</b> Alete takılan nota taşıyıcı 92.09; yere konan nota sehpası mobilya olarak 94.03."
    ],
    "hafiza": {
        "kanca": "KLAVYE-TEL (01) · TEL (02) · [03–04 boş] · NEFES (05) · VURMA (06) · FİŞ (07) · DÜDÜK-KUTU (08) · PARÇA (09)",
        "aciklama": "Bir konser sahnesini önden arkaya düşünün: en önde piyano (01), yanında yaylılar ve gitarlar (02), iki boş sandalye (03–04), arkada üflemeliler (05), en arkada davullar (06). Sahnenin kenarında fişe takılı elektronik aletler (07), kapıda müzik kutusu satan ve düdük çalan satıcı (08), kulisteki dolapta teller, tuşlar ve metronom (09)."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda daha çok GYK sorularında ve seçeneklerde yer almıştır; doğrudan 4’lü pozisyon sorusu azdır.",
        "GYK 5(a): keman ve kemana uygun yapılmış mahfazanın birlikte, kemanın pozisyonunda sınıflandırılması; müzik aleti mahfazasının GYK 5 kapsamındaki tipik örnek olması.",
        "Fasıl 92 Not 2’nin ikinci cümlesi: piyano ile birlikte getirilen kart, disk ve rulo türü eşyanın aletin parçası sayılmayıp ayrıca 92.09’da sınıflandırılması.",
        "Bölüm bilgisi: gitarın kol saati ve güneş gözlüğüyle aynı bölümde (Bölüm XVIII), tabancanın ise Bölüm XIX’da yer alması."
    ],
    "cikmis_ornekler": [
        {
            "soru": "Birlikte gümrüğe sunulan keman ve bu kemana uygun olarak yapılmış mahfazası hangi yorum kuralına göre ve ne şekilde sınıflandırılır?",
            "secenekler": ["Birlikte kemanın pozisyonunda, GYK 2", "Birlikte kemanın pozisyonunda, GYK 5", "Keman ve mahfazası ayrı olarak kendi pozisyonlarında, GYK 3", "Keman ve mahfazası ayrı olarak kendi pozisyonlarında, GYK 6"],
            "cevap": "B",
            "aciklama": "GYK 5(a), belli bir eşyaya uygun yapılmış, uzun süre kullanılmaya elverişli ve eşyayla birlikte sunulan mahfazaları eşyayla birlikte sınıflandırır; açıklama notu müzik aleti mahfazalarını (92.02) örnek olarak sayar. Keman ve mahfazası 92.02’de yer alır."
        }
    ],
    "ozet": [
        "Önce eleme: oyuncak 95.03, elektronik müzik modülü 85.43, alete takılmamış amplifikatör ve hoparlör Fasıl 85, tripod 96.20.",
        "Elektriksiz normal çalınamıyorsa 92.07; elektrikli otomatik piyano istisna olarak 92.01.",
        "Telli: klavyeli 92.01, diğerleri 92.02. Nefesli 92.05 (org ve akordeon dahil). Vurmalı 92.06 (selesta ve karillon dahil).",
        "Müzik kutusu, laterna, fuar orgu, mekanik öten kuş, düdük ve av çağrı aleti 92.08; müzikli hediyelik eşya müzik kutusu değildir.",
        "Parça, tel, aksesuar, metronom, diyapozon, kart-disk-rulo 92.09; yay ve baget aletle gelirse aletle kalır (Not 2).",
        "Piyano taburesi 94.01, yere konan nota sehpası 94.03, akort aleti 82.05, temizleme fırçası 96.03."
    ],
    "sorular": [
        # 1 B
        Q("Tarife Cetveline göre, gövdesinde ses kutusu bulunmayan, sesi yalnızca manyetik pikap ve harici bir amplifikatör aracılığıyla duyulabilen altı telli elektro gitar hangi pozisyonda sınıflandırılır?",
          ["92.02", "92.07", "92.08", "85.18", "92.09"], "B", "Eşya → 4’lü pozisyon",
          "Elektrik veya elektronik unsurları olmadan normal çalınamayan aletler 92.07’dedir; 92.02 açıklama notu ses kutusu olmayan elektrogitarı açıkça 92.07’ye gönderir. Gitar olması 92.02’yi düşündürür; tuzak budur. Harici amplifikatör ayrı gelirse 85.18’e girer, ama gitarın kendisi 92.07’dedir.",
          "92.02 ve 92.07 Açıklama Notları; Fasıl 92 Genel Açıklamalar."),
        # 2 C
        Q("Tarife Cetveline göre, klavye vasıtasıyla çalıştırılan mekanik çekiçlerin özel çelik levhalara vurmasıyla ses elde edilen, dış görünüşü küçük bir piyanoyu andıran selesta hangi pozisyonda sınıflandırılır?",
          ["92.01", "92.05", "92.06", "92.07", "92.08"], "C", "Eşya → 4’lü pozisyon",
          "Selesta, 92.06 açıklama notunda vurularak çalınan aletler arasında sayılmıştır; ses çelik levhaya çekiçle vurularak elde edilir. Klavyeli olması ve piyanoya benzemesi 92.01’i düşündürür; ancak 92.01 telli klavyeli aletler içindir. Elektronik değildir (92.07); 92.08 diğer pozisyonlarda yer almayan aletler içindir.",
          "92.06 Açıklama Notu; 92.01 pozisyon metni."),
        # 3 E
        Q("Tarife Cetveline göre, körüklü, klavyeli ve herhangi bir elektrik tertibatı bulunmayan akordeon hangi pozisyonda sınıflandırılır?",
          ["92.01", "92.07", "92.08", "92.09", "92.05"], "E", "Eşya → 4’lü pozisyon",
          "Akordeonlar 92.05 pozisyon metninde nefesli müzik aletleri arasında açıkça sayılmıştır. Klavye 92.01’i düşündürür ama 92.01 telli aletler içindir. Yalnızca elektronik akordeonlar 92.07’ye gider; 92.08 fuar ve sokak orgları ile diğer pozisyonlarda yer almayan aletler içindir.",
          "92.05 pozisyon metni ve Açıklama Notu; Fasıl 92 Genel Açıklamalar."),
        # 4 A
        Q("Tarife Cetveline göre, ördek sesini taklit ederek av hayvanlarını çekmeye yarayan, ağızla üflenerek kullanılan ahşap av çağrı düdüğü hangi pozisyonda sınıflandırılır?",
          ["92.08", "92.05", "95.07", "92.09", "95.03"], "A", "Eşya → 4’lü pozisyon",
          "92.08 pozisyon metni av hayvanlarını ve kuşlarını çağırmaya mahsus her tür düdük ve aleti açıkça kapsar. Üflemeli olması 92.05’i düşündürür; ancak çağrı ve işaret aletleri 92.08’dedir. Fasıl 95 açıklama notları da öten tuzak nesnelerini 92.08’e gönderir; bu nedenle 95.07 çeldiricidir.",
          "92.08 pozisyon metni ve Açıklama Notu (B)(1); 95.07 Açıklama Notu."),
        # 5 D
        Q("Tarife Cetveline göre, naylon monofilamentten yapılmış, ucunda tutturma ilmeği bulunan ve üzerinde kullanım talimatı basılı küçük zarflar içinde perakende ambalajlanmış klasik gitar telleri hangi pozisyonda sınıflandırılır?",
          ["54.04", "92.02", "39.16", "92.09", "56.07"], "D", "Eşya → 4’lü pozisyon",
          "92.09 müzik aletlerinin tellerini kapsar; sentetik monofilament teller de buradadır. Teller nihai halleri, ilmekleri ve talimatlı ambalajları ile müzik teli olarak tanınır. Müzik aletine ait olduğu açıkça anlaşılmayan monofilamentler kendi pozisyonlarına (54.04, 39.16 gibi) gider; tellerin gitarla aynı pozisyonda (92.02) olduğunu sanmak da tuzaktır.",
          "92.09 Açıklama Notu (C)."),
        # 6 C
        Q("Aşağıdakilerden hangisi Tarife Cetvelinin 92. faslında <b>sınıflandırılmaz</b>?",
          ["Metronom", "Müzik kutusu", "Elektronik müzik modülü", "Akort düdüğü", "Laterna"], "C", "Olumsuz teşhis",
          "Fasıl 92 genel açıklamaları elektronik müzik modüllerini fasıl dışında bırakır ve 85.43’e gönderir. Metronom ve akort düdüğü 92.09’da, müzik kutusu ve laterna 92.08’de sınıflandırılır. Modülün müzik çalması onu müzik aleti yapmaz.",
          "Fasıl 92 Genel Açıklamalar; 92.08 ve 92.09 Açıklama Notları."),
        # 7 B
        Q("Ayrı olarak gelen aşağıdaki eşyadan hangisi 92.09 pozisyonunda <b>yer almaz</b>?",
          ["Kulak muayenesinde kullanılan diyapozon", "Yere konularak kullanılan nota sehpası", "Saksofona takılan nota taşıyıcı", "Otomatik müzik aletleri için delikli kâğıt rulo", "Yumuşak başlı davul bageti"], "B", "Olumsuz teşhis",
          "92.09 açıklama notu zemine yerleştirilen nota sehpalarını hariç tutar ve 94.03’e (mobilya) gönderir. Müzik aletinin üzerine takılan nota taşıyıcılar, tıpta kullanılan diyapozonlar, otomatik aletlerin ruloları ve ayrı gelen bagetler 92.09’dadır. Tuzak, iki nota tutucuyu aynı sanmaktır.",
          "92.09 Açıklama Notu ve hariç tutma (e)."),
        # 8 E
        Q("Aşağıdakilerden hangisi 92.06 pozisyonunda <b>sınıflandırılmaz</b>?",
          ["Zillerle donatılmış davul seti", "Ksilofon", "Üçgen", "Kastanyet", "Müzik aleti sayılmayan masa gongu"], "E", "Olumsuz teşhis",
          "92.06 açıklama notu müzik aletlerinden sayılmayan kapı veya masa zil ve gonglarını hariç tutar; bunlar 83.06 veya 85.31’dedir. Zillerle birleştirilmiş davul setleri, ksilofon, üçgen ve kastanyet vurmalı aletler olarak 92.06’da sayılmıştır.",
          "92.06 Açıklama Notu ve hariç tutma (a)."),
        # 9 D
        Q("Aşağıdakilerden hangisi 92.07 pozisyonunda <b>sınıflandırılmaz</b>?",
          ["Elektronik org", "Ses kutusu olmayan elektro gitar", "Elektronik akordeon", "Delikli kâğıt rulolarla çalınan elektrikli otomatik piyano", "Elektronik vurmalı çalgı"], "D", "Olumsuz teşhis",
          "92.07 açıklama notu elektrikle çalışan otomatik piyanoları açıkça hariç tutar ve 92.01’e gönderir. Elektronik org, ses kutusu olmayan elektro gitar, elektronik akordeon ve elektronik vurmalı aletler ise elektriksiz normal çalınamadıkları için 92.07’dedir.",
          "92.07 Açıklama Notu; 92.01 Açıklama Notu; Fasıl 92 Genel Açıklamalar."),
        # 10 D
        Q("Aşağıdaki müzik aletlerinden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
          ["Arp", "Ukulele", "Banço", "Klavsen", "Viyolonsel"], "D", "Farklı/aynı pozisyon veya fasıl",
          "Klavsen, klavyeli telli bir alet olarak 92.01’dedir. Arp, ukulele, banço (parmakla veya mızrapla çalınan) ve viyolonsel (yayla çalınan) 92.02’deki telli diğer müzik aletleridir. Yaylı ve mızraplı ayrımı yalnızca alt pozisyon düzeyindedir.",
          "92.01 ve 92.02 Açıklama Notları."),
        # 11 E
        Q("Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
          ["Armonyum", "Klavyeli borulu kilise orgu", "Ağız armonikası", "Okarina", "Mekanik sokak orgu"], "E", "Farklı/aynı pozisyon veya fasıl",
          "92.05 pozisyon metni fuar orglarını ve mekanik sokak orglarını açıkça hariç tutar; bunlar 92.08’dedir. Armonyum, klavyeli borulu org, ağız armonikası ve okarina 92.05’teki nefesli aletlerdir. “Org” kelimesinin hepsini 92.05’e götürdüğünü sanmak tuzaktır.",
          "92.05 pozisyon metni ve Açıklama Notu; 92.08 Açıklama Notu (A)."),
        # 12 A
        Q("Ayrı olarak gelen aşağıdaki eşyadan hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
          ["Flütü temizlemeye mahsus fırça", "Piyano teli", "Metronom", "Org körüğü", "Keman çene dayanağı (mantonyer)"], "A", "Farklı/aynı pozisyon veya fasıl",
          "Fasıl 92 Not 1(d) ve 92.09 hariç tutmaları müzik aletlerini temizlemeye mahsus fırçaları 96.03’e (Fasıl 96) gönderir. Piyano teli, metronom, org körüğü ve mantonyer 92.09’da sayılan aksam, parça ve aksesuardır. Fırçanın yalnızca flüt için yapılmış olması onu aksesuar yapmaz.",
          "Fasıl 92 Not 1(d); 92.09 Açıklama Notu."),
        # 13 B
        Q("Aşağıdaki gruplardan hangisinde yer alan eşyanın <b>tamamı</b> aynı pozisyonda sınıflandırılır?",
          ["Piyano – klavsen – selesta", "Keman – viyola – kontrbas – gitar", "Flüt – saksofon – mekanik sokak orgu", "Davul – kastanyet – kapı gongu", "Akordeon – elektronik akordeon – bandonyon"], "B", "Farklı/aynı pozisyon veya fasıl",
          "Keman, viyola, kontrbas ve gitar 92.02’deki telli diğer aletlerdir. Selesta 92.06’da; mekanik sokak orgu 92.08’de; kapı gongu 83.06 veya 85.31’de; elektronik akordeon 92.07’de olduğundan diğer gruplar karışıktır.",
          "92.02, 92.05, 92.06, 92.07, 92.08 Açıklama Notları."),
        # 14 A
        Q("Fasıl 92 Not 2’ye göre aşağıdakilerden hangisi <b>doğrudur</b>?",
          ["92.02 ve 92.06 aletleriyle birlikte getirilen ve normal miktarda olan yay ve bagetler ilgili aletle aynı pozisyonda sınıflandırılır.", "Bütün müzik aletleriyle birlikte gelen her tür aksesuar aletle aynı pozisyonda sınıflandırılır.", "92.09’daki kart, disk ve rulolar aletle birlikte getirildiğinde aletin parçası sayılır.", "Yay ve bagetler aletle birlikte gelse de her durumda 92.09’da sınıflandırılır.", "92.05 aletleriyle birlikte gelen yedek ağızlıklar aletle aynı pozisyonda sınıflandırılır."], "A", "Fasıl notu · Tanım/Eşik",
          "Not 2, yalnızca 92.02 ve 92.06 aletlerinin çalınmasında kullanılan, aletle birlikte getirilen, normal miktarda olan ve onunla kullanılacağı açık olan yay, baget ve benzerlerini aletle birlikte sınıflandırır. Aynı notun ikinci cümlesine göre kart, disk ve rulolar aletle gelse bile ayrı eşyadır. Not, bütün aksesuarları veya nefesli aletlerin ağızlıklarını kapsamaz.",
          "Fasıl 92 Not 2; Fasıl 92 Genel Açıklamalar."),
        # 15 C
        Q("Fasıl 92 Not 1’e göre, bu fasıldaki aletlerle kullanılan mikrofon, yükselteç ve hoparlörler hangi durumda Fasıl 92’de değil, Fasıl 85 veya 90’da sınıflandırılır?",
          ["Aletle aynı kutuda ambalajlanmış olduklarında", "Değerleri aletin değerini aştığında", "Alete takılmamış veya aletle aynı kabine yerleştirilmemiş olduklarında", "Aletten ayrı bir taşıtla getirildiklerinde", "Yalnızca 92.07 aletleriyle birlikte kullanıldıklarında"], "C", "Fasıl notu · Tanım/Eşik",
          "Not 1(b), fasıl eşyasıyla kullanılan fakat bunlara takılmamış veya aynı kabine yerleştirilmemiş mikrofon, yükselteç, hoparlör, kulaklık vb.ni fasıl dışında bırakır. Ölçüt ambalaj veya değer değil, aletle bütünleşmedir; 92.07 açıklama notuna göre bünyeye girmiş cihaz ayrı ambalajlansa bile aletle kalır.",
          "Fasıl 92 Not 1(b); 92.07 Açıklama Notu."),
        # 16 D
        Q("Fasıl 92 ve Fasıl 95 açıklama notlarına göre, bir müzik aletinin oyuncak niteliğinde sayılarak Fasıl 95’te sınıflandırılmasında dikkate alınan ölçütlerden biri <b>değildir</b>?",
          ["İmal olunduğu maddenin vasıfları", "Gördüğü kaba işçilik", "Müzikal kusurları", "Satış fiyatı", "Gerçek aletten küçük boyutu ve sınırlı kapasitesi"], "D", "Fasıl notu · Tanım/Eşik",
          "Fasıl 92 genel açıklamaları oyuncak niteliğini maddenin vasıfları, kaba işçilik, müzikal kusurlar ve diğer vasıflarla belirler; Fasıl 95 açıklama notu da oyuncak müzik aletlerinin gerçeklerinden büyüklükleri ve sınırlı kapasiteleriyle ayırt edildiğini belirtir. Satış fiyatı notlarda ölçüt olarak sayılmamıştır.",
          "Fasıl 92 Not 1(c) ve Genel Açıklamalar; 95.03 Açıklama Notu."),
        # 17 B
        Q("92.07 açıklama notuna göre, bu pozisyondaki aletleri elektrikli pikap ve amplifikatör takılabilen mutat piyano, akordeon ve gitarlardan ayıran ölçüt aşağıdakilerden hangisidir?",
          ["Elektrik şebekesine fişle bağlanabilmeleri", "Elektrik veya elektronik unsurları olmaksızın normal olarak çalınamamaları", "Hoparlörlerinin aletin içinde bulunması", "Klavyeli olmaları", "Birden fazla aletin sesini taklit edebilmeleri"], "B", "Fasıl notu · Tanım/Eşik",
          "92.07, sesi elektrikle üretilen veya yükseltilen ve elektrik-elektronik unsurları olmadan normal çalınamayan aletleri kapsar. Pikap ve amplifikatör takılabilen mutat aletler bu tertibat olmadan da çalınabildiği için kendi pozisyonlarında kalır. Fişle bağlanma, hoparlörün içeride olması veya klavye tek başına belirleyici değildir.",
          "92.07 Açıklama Notu; Fasıl 92 Genel Açıklamalar."),
        # 18 E
        Q("Tarife Cetveline göre, birlikte gümrüğe sunulan bir saksafon ile bu saksafonun şekline uygun olarak yapılmış, uzun süre kullanılmaya elverişli ve normal olarak saksafonla birlikte satılan sert çantası nasıl sınıflandırılır?",
          ["Birlikte, çantanın pozisyonunda; GYK 3(b)", "Ayrı ayrı, kendi pozisyonlarında; GYK 1", "Birlikte, saksafonun pozisyonunda; GYK 2(a)", "Birlikte, numara sırasına göre sonuncu pozisyonda; GYK 3(c)", "Birlikte, saksafonun pozisyonunda; GYK 5(a)"], "E", "Genel Yorum Kuralı",
          "GYK 5(a), belli bir eşyaya uygun yapılmış, uzun süre kullanılmaya elverişli ve eşyayla birlikte sunulan, normal olarak onunla satılan mahfazaları eşyayla birlikte sınıflandırır; açıklama notu müzik aleti mahfazalarını açıkça örnek verir. Saksafon ve çantası bir set (3(b)) veya demonte eşya (2(a)) değildir; ikisi birlikte 92.05’e girer.",
          "GYK 5(a) ve Açıklama Notu (II)(4)."),
        # 19 C
        Q("Taşıma kolaylığı için ayakları, pedal mekanizması ve kapağı sökülmüş, ancak bütün parçaları aynı sevkiyatta birlikte sunulan ve yalnızca vidalarla yeniden monte edilecek kuyruklu piyanonun sınıflandırılmasında hangi Genel Yorum Kuralları kullanılır?",
          ["GYK 1 ve 6", "GYK 1, 2(b) ve 6", "GYK 1, 2(a) ve 6", "GYK 1, 3(b) ve 6", "GYK 1, 5(a) ve 6"], "C", "Genel Yorum Kuralı",
          "GYK 2(a)’nın ikinci kısmına göre birleştirilmemiş veya demonte halde sunulan tamamlanmış eşya, monte edilmiş eşya ile aynı pozisyonda (92.01) sınıflandırılır; montajın yalnızca bağlantı elemanlarıyla yapılması bu kuralın koşuludur. Ayaklar ve pedallar ayrıca 92.09’da sınıflandırılmaz. Eşya bir set (3(b)) değildir; 2(b) madde karışımları içindir.",
          "GYK 2(a) Açıklama Notu (V)–(VII); 92.01 pozisyon metni."),
        # 20 A
        Q("Aşağıdaki müzik aletlerini sınıflandırıldıkları pozisyonlarla eşleştiriniz.<br/>I. Kastanyet<br/>II. Banço<br/>III. Bandonyon<br/>IV. Müzik testeresi<br/>a) 92.02 · b) 92.05 · c) 92.06 · d) 92.08",
          ["I-c, II-a, III-b, IV-d", "I-c, II-b, III-a, IV-d", "I-d, II-a, III-b, IV-c", "I-c, II-a, III-d, IV-b", "I-a, II-c, III-b, IV-d"], "A", "Eşleştirme / Boşluk doldurma",
          "Kastanyet vurmalı alettir (92.06); banço mızrapla çalınan telli alettir (92.02); bandonyon akordeon benzeri körüklü nefesli alettir (92.05); müzik testeresi 92.08 pozisyon metninde açıkça sayılmıştır. Bandonyonu telli, müzik testeresini vurmalı sanmak tipik hatadır.",
          "92.02, 92.05, 92.06 ve 92.08 Açıklama Notları."),
        # 21 D
        Q("Fasıl 92 Not 2’ye göre, 92.09 pozisyonundaki ……… bir müzik aletiyle beraber getirilmiş olsalar dahi bu müzik aletinin bir parçası olarak değil, ayrı eşya olarak işlem görür. Boşluğa aşağıdakilerden hangisi gelmelidir?",
          ["yay ve bagetler", "teller", "mızraplar", "kart, disk ve rulolar", "ağızlıklar"], "D", "Eşleştirme / Boşluk doldurma",
          "Not 2’nin ikinci cümlesi 92.09’daki kart, disk ve ruloların aletle birlikte gelse bile ayrı eşya olduğunu hükme bağlar; 92.08 açıklama notu da bunların her zaman 92.09’da sınıflandırıldığını tekrarlar. Yay ve bagetler (ve genel açıklamalara göre mızraplar) ise aletle birlikte gelince aletin pozisyonunda kalır.",
          "Fasıl 92 Not 2; Fasıl 92 Genel Açıklamalar; 92.08 Açıklama Notu."),
        # 22 E
        Q("Fasıl 92 ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Elektrikli pikap ve amplifikatörü bulunan bir gitar, bu tertibat olmadan da çalınabiliyorsa 92.02’de kalır.<br/>II. Elektronik orglar, borulu orglar gibi 92.05’te sınıflandırılır.<br/>III. Müzik aletleriyle kullanılan monopod, bipod ve tripodlar 96.20’de sınıflandırılır.<br/>IV. Koleksiyon eşyası niteliğindeki müzik aletleri 92.08’de sınıflandırılır.",
          ["I ve II", "II ve IV", "I, II ve III", "III ve IV", "I ve III"], "E", "Çoktan-çoğa (I–IV)",
          "I, genel açıklamalar ve 92.02 açıklama notuyla; III, Not 1(d) ile uyumludur. II yanlıştır: elektronik orglar 92.07’dedir. IV yanlıştır: koleksiyon eşyası ve antikalar Not 1(e) gereği 97.05 veya 97.06’dadır.",
          "Fasıl 92 Not 1(d), (e); 92.02, 92.05 ve 92.07 Açıklama Notları."),
        # 23 B
        Q("92.08 pozisyonu ile ilgili aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Müzik mekanizmasıyla birleştirilmiş hediyelik seramik eşya, bu pozisyon anlamında müzik kutusu sayılmaz.<br/>II. Elektronik müzik modülü içeren tebrik kartları bu pozisyonda sınıflandırılır.<br/>III. Ağızla üflenen işaret düdükleri ve çağrı kornaları bu pozisyondadır.<br/>IV. Mekanik öten kuşlar ve müzik testereleri bu pozisyondadır.",
          ["I ve II", "I, III ve IV", "II ve III", "II, III ve IV", "I ve IV"], "B", "Çoktan-çoğa (I–IV)",
          "I, III ve IV 92.08 açıklama notunda açıkça yer alır. II yanlıştır: elektronik müzik modüllü kol saati, kupa ve tebrik kartları bu pozisyonda değerlendirilmez; modülsüz hallerinin pozisyonunda sınıflandırılır.",
          "92.08 Açıklama Notu (A)(1), (4), (5) ve (B)(2)."),
        # 24 A
        Q("Bir müzik mağazası için ithal edilen eşya: ahşap ses kutusu bulunan; gövdesine monte edilmiş pikap ve aynı gövdeye yerleştirilmiş ön amplifikatör devresi olan; amplifikatöre bağlanmadan da akustik olarak normal şekilde çalınabilen altı telli gitar. Bu eşya Tarife Cetvelinde hangi pozisyonda sınıflandırılır?",
          ["92.02", "92.07", "85.18", "92.09", "92.08"], "A", "Senaryo",
          "Elektrikli pikap ve amplifikatör tertibatı bulunan mutat tipteki gitar, bu tertibat olmadan da kullanılabildiği için kendi pozisyonunda, 92.02’de kalır. Gövdeye yerleştirilmiş elektrik devresi aletle bütün oluşturduğundan ayrıca 85.18’e gitmez. 92.07 yalnızca elektriksiz normal çalınamayan aletler içindir; tuzak, “elektrik” görünce 92.07’yi seçmektir.",
          "Fasıl 92 Genel Açıklamalar; 92.02 ve 92.07 Açıklama Notları."),
        # 25 C
        Q("Bir belediye binasının kulesine yerleştirilmek üzere getirilen; akort edilmiş bir dizi çandan oluşan, çanlara mekanik tokmaklarla vurulan, herhangi bir elektronik ses üretme veya yükseltme tertibatı ve saat kadranı bulunmayan, kamuya müzik yayını için kullanılan karillon hangi pozisyonda sınıflandırılır?",
          ["92.07", "83.06", "92.06", "91.05", "92.08"], "C", "Senaryo",
          "92.06 açıklama notu müzik yayını için kamu binalarında kullanılan karillonları vurmalı aletler arasında sayar. Elektronik karillonlar 92.07’de, saat kadranlı mutat saatler Fasıl 91’de olurdu; eşyada bunlar yoktur. Müzik aleti olmayan zil ve gonglar 83.06’ya gider, karillon ise müzik aletidir.",
          "92.06 Açıklama Notu; 92.07 Açıklama Notu; 85.31 Açıklama Notu."),
    ]
}

out = os.path.join(KITAP, "data", "fasil_92.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("yazıldı:", out)
