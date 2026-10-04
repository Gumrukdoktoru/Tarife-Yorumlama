#!/usr/bin/env python3
"""Fasıl 86 modülü üreteci (Bölüm XVII'nin ilk faslı)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_86_89 import EP, OT, FA, TN, GY, ES, CC, SN, soru, yaz  # noqa: E402

obj = {
    "tur": "fasil",
    "fasil": 86,
    "baslik": "Demiryolu ve benzeri hatlara ait taşıtlar ve malzemeler ve bunların aksam ve parçaları; her türlü mekanik (elektromekanik olanlar dahil) trafik sinyalizasyon cihazları",
    "bolum": "XVII",
    "oz": {
        "vurgu": "Fasıl 86 raylı ve kılavuz hatlı taşıtları güç kaynağına ve işlevine göre ayırır: lokomotifler ve kendinden hareketli vagonlar 86.01–86.03, bakım-servis taşıtları 86.04, kendinden hareketli olmayan vagonlar 86.05–86.06; aksam 86.07, sabit hat malzemesi ve mekanik sinyalizasyon 86.08, konteynerler 86.09. Bölüm XVII Not 2’de sayılan eşya, nakil vasıtasına mahsus olsa bile bu bölüme girmez.",
        "maddeler": [
            "“Demiryolu” ve “tramvay” terimleri çelik raylı hatlarla birlikte manyetik yükselme veya beton kılavuz hat kullanan sistemleri de kapsar; kılavuz hat üzerinde işleyen hava yastıklı taşıtlar (hava treni) Fasıl 86’dadır.",
            "Lokomotifte ölçüt güç kaynağıdır: elektriği dışarıdan veya akümülatörden alan 86.01; dizel (elektrikli, hidrolik, mekanik), buharlı ve diğerleri ile tenderler 86.02. İki tip güçle çalışan lokomotif esas güç tipine göre sınıflandırılır.",
            "Mekanik veya elektromekanik sinyal, emniyet ve trafik kontrol cihazları yalnız demiryolu için değil karayolu, iç su yolu, park yeri, liman ve havalimanı için de 86.08’dedir; elektrikli olanlar 85.30’a gider.",
            "Traversler ve ray malzemesi Fasıl 86 dışıdır (44.06, 68.10, 73.02); traverslerle birleştirilmiş hatlar ise 86.08’de yer alır.",
            "Hem karayolunda hem rayda kullanılmak üzere özel imal edilen taşıtlar Fasıl 87’dedir (Bölüm XVII Not 4).",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Oyuncak tren, teşhir modeli, eğlence parkı veya panayır aracı mı?",
             "<b>95.03</b> · <b>90.23</b> · <b>95.08</b>"],
            ["2", "Hem karayolunda hem raylar üzerinde kullanılmak üzere özel imal edilmiş mi?",
             "Fasıl 87 (traktör <b>87.01</b>, kara-demiryolu kamyonu <b>87.04</b>)"],
            ["3", "Bölüm XVII Not 2 eşyası mı? (conta, genel kullanım aksamı, motor, rulman, elektrik teçhizatı, Fasıl 90–91 aleti, lamba, fırça)",
             "Kendi fasılları (<b>84.84</b>, Bölüm XV, Fasıl 84, 85, 90, 91, <b>94.05</b>, <b>96.03</b>)"],
            ["4", "Elektriği dışarıdan veya akümülatörden alan lokomotif mi?", "<b>86.01</b>"],
            ["5", "Diğer lokomotif (dizel, buharlı, gaz türbinli) veya lokomotif tenderi mi?", "<b>86.02</b>"],
            ["6", "Hat bakım veya servis taşıtı mı? (atölye, vinçli, balast, deneme vagonu, drezin)",
             "<b>86.04</b> (kendinden hareketli olsun olmasın)"],
            ["7", "Kendinden hareketli yolcu veya yük vagonu mu? (otomotris, elektrikli tren vagonu, tramvay arabası)",
             "<b>86.03</b>"],
            ["8", "Kendinden hareketli olmayan yolcu, bagaj, posta veya özel amaçlı vagon mu?", "<b>86.05</b>"],
            ["9", "Kendinden hareketli olmayan yük vagonu mu? (sarnıçlı, frigorifik, kendinden boşaltmalı, maden, kereste)",
             "<b>86.06</b>"],
            ["10", "Demiryolu taşıtına mahsus aksam ve parça mı? (boji, dingil, tekerlek, fren, tampon, cer kancası, monte edilmemiş karoser)",
             "<b>86.07</b>"],
            ["11", "Birleştirilmiş hat, döner platform, durdurma tamponu veya mekanik sinyal-trafik kumanda cihazı mı?*",
             "<b>86.08</b> (elektrikli ise <b>85.30</b>)"],
            ["12", "Bir veya daha fazla taşıma şekline göre özel yapılmış ve donatılmış konteyner mi?", "<b>86.09</b>"],
        ],
        "dipnot": "* Elektro-pnömatik sistemlerde işaret kolları ve bunları hareket ettiren pnömatik tertibat 86.08’de, elektrikli kontrol ve kumanda tabloları Fasıl 85’te kalır. Mekanik unsuru olmayan levhalar (azami hız, yön, meyil) maddesine göre (44.21, 83.10) sınıflandırılır.",
    },
    "pozisyon_haritasi": [
        ["86.01", "Elektrikli lokomotifler",
         "Elektriği dışarıdan (havai hat, üçüncü ray) veya akümülatörden alır",
         "Pantograflı elektrikli lokomotif, akülü lokomotif"],
        ["86.02", "Diğer lokomotifler; tenderler",
         "86.01 dışı her güç kaynağı",
         "Dizel-elektrikli, dizel-hidrolik, buharlı, ateşsiz lokomotif; tender"],
        ["86.03", "Kendinden hareketli demiryolu ve tramvay vagonları",
         "Yolcu veya yük taşıyabilir; uçlarda kumanda kabini; 86.04 hariç",
         "Otomotris, elektrikli motorlu vagon, tramvay arabası"],
        ["86.04", "Bakım ve servis taşıtları",
         "Kendinden hareketli olsun olmasın",
         "Atölye vagonu, vinçli vagon, balast sıkıştırıcı, deneme vagonu, drezin"],
        ["86.05", "Kendinden hareketli olmayan yolcu, bagaj, posta ve özel amaçlı vagonlar",
         "Yolcu trenine eklenen vagon tipleri; 86.04 hariç",
         "Yataklı, lokanta, posta, hastane, hapishane vagonu"],
        ["86.06", "Kendinden hareketli olmayan yük vagonları",
         "Eşya nakli; yaysız küçük maden-şantiye vagonları dahil",
         "Sarnıçlı, frigorifik, kendinden boşaltmalı, kereste, maden vagonu"],
        ["86.07", "Demiryolu taşıtlarının aksam ve parçaları",
         "Yalnız veya esas itibarıyla Fasıl 86 taşıtına; Not 2 dışı",
         "Boji, dingil, tekerlek, fren, müsademe tamponu, cer kancası, karoser"],
        ["86.08", "Sabit hat malzemesi; mekanik sinyal ve trafik kontrol cihazları",
         "Mekanik veya elektromekanik; karayolu, liman, havalimanı dahil",
         "Birleştirilmiş hat, döner platform, durdurma tamponu, semafor, makas tertibatı"],
        ["86.09", "Konteynerler",
         "Bir veya daha fazla taşıma şekline göre özel yapılmış ve donatılmış",
         "Uluslararası yük konteyneri, izoleli konteyner, sıvı konteyneri"],
    ],
    "notlar": [
        ["Bölüm XVII Not 1",
         "Bölüm XVII; 95.03 veya 95.08 pozisyonlarına giren eşyayı ve 95.06’daki küçük ve büyük yarış kızakları ile benzerlerini kapsamaz."],
        ["Bölüm XVII Not 2 (a)–(d)",
         "“Aksam ve parça” ile “aksam, parça ve aksesuar” tabirleri, nakil vasıtalarına mahsus oldukları anlaşılsa bile şunlara uygulanmaz: (a) her maddeden contalar, rondelalar ve benzerleri (maddesine göre veya 84.84) ve sertleştirilmemiş vulkanize kauçuktan diğer eşya (40.16); (b) XV. Bölüm Not 2’de tanımlanan adi metallerden genel kullanıma mahsus aksam (Bölüm XV) ve plastikten benzerleri (Fasıl 39); (c) Fasıl 82 aletleri; (d) 83.06 eşyası."],
        ["Bölüm XVII Not 2 (e)–(l)",
         "(e) 84.01–84.79 makina ve cihazları ile aksamı (<b>bu bölüm eşyasına ait radyatörler hariç</b>), 84.81 ve 84.82 eşyası, motor ve makinaların bünyesine giren 84.83 eşyası; (f) Fasıl 85 elektrik makina, teçhizat ve aksesuarı; (g) Fasıl 90 eşyası; (h) Fasıl 91 eşyası; (ij) silahlar (Fasıl 93); (k) 94.05 lambaları, aydınlatma cihazları ve aksamı; (l) nakil vasıtalarında aksam olarak kullanılan fırçalar (96.03)."],
        ["Bölüm XVII Not 3",
         "Fasıl 86–88’deki “aksam ve parça” veya “aksesuar” atfı, sadece veya esas itibarıyla bu fasıllardaki taşıtlarda kullanılmaya uygun olmayan eşyayı kapsamaz. Bu fasılların iki veya daha fazla pozisyonuna girebilecek aksam, <b>asıl kullanımına</b> tekabül eden pozisyonda sınıflandırılır."],
        ["Bölüm XVII Not 4",
         "Hem karayolunda hem raylar üzerinde kullanılmak üzere özel imal edilmiş taşıtlar ve hem denizde hem karada kullanılan motorlu taşıtlar <b>Fasıl 87</b>’de; aynı zamanda kara taşıtı olarak kullanılabilecek şekilde özel imal edilmiş hava taşıtları <b>Fasıl 88</b>’de sınıflandırılır."],
        ["Bölüm XVII Not 5",
         "Hava yastıklı taşıtlar en çok benzedikleri taşıtlarla sınıflandırılır: kılavuz hat üzerinde işleyenler (hava treni) Fasıl 86; karada veya hem karada hem suda işleyenler Fasıl 87; suda işleyenler (sahile ve iskeleye çıkabilsin veya buz üzerinde işleyebilsin, işlemesin) Fasıl 89. Aksamı, taşıtın sınıflandırıldığı pozisyona gider. Hava treni hatlarının sabit malzemesi ve sinyal-kumanda cihazları demiryolundaki karşılıkları gibi sınıflandırılır."],
        ["Bölüm XVII Genel Açıklamalar (I)–(II)",
         "Bölüm dışı: hareket eden bazı makinalar, 90.23’teki teşhir modelleri, oyuncaklar (pedallı araba, oyuncak bot ve uçak 95.03), kızaklar (95.06), fuar ve panayır araçları (95.08). Yüzer vasıtalara monte edilmiş tüm hareketli makinalar (yüzen vinç, tarama makinası) Fasıl 89’dadır."],
        ["Bölüm XVII Genel Açıklamalar (III)",
         "Aksam, parça ve aksesuar üç koşulun <b>hepsini</b> sağlarsa Fasıl 86–88 pozisyonlarına girer: (a) Not 2 ile hariç tutulmamış olmak; (b) özellikle veya esas itibarıyla bu fasıllardaki taşıtlarda kullanılmaya elverişli olmak; (c) Tarifenin başka yerinde daha belirli olarak yer almamış olmak. Birden fazla taşıt türüne uyan fren, tekerlek, dingil gibi aksam esas olarak kullanıldığı taşıtın pozisyonuna gider. Fasıl 89’da gemi teknesi dışında aksam hükmü yoktur."],
        ["Bölüm XVII Genel Açıklamalar (III)(C)",
         "Başka yerde daha belirli olarak yer aldığından bölüm dışında kalan aksam: vulkanize kauçuk profiller (40.08), transmisyon kolanları (40.10), dış ve iç lastikler (40.11–40.13), alet çantaları (42.02), çekme halatları (56.09), halılar (Fasıl 57), çerçevesiz emniyet camları (70.07), dikiz aynaları (70.09 veya Fasıl 90), çerçevesiz camlar (70.14), hız göstergesi esnek şaftları (84.83), koltuklar (94.01)."],
        ["Fasıl 86 Not 1",
         "Fasıl dışı: (a) demiryolu veya tramvay hatları için ahşap veya beton traversler ve hava treni kılavuz hatlarının beton kısımları (44.06 veya 68.10); (b) 73.02’deki demir veya çelikten demiryolu-tramvay hattı malzemesi; (c) 85.30’daki elektrikli sinyalizasyon, emniyet, trafik kontrol veya kumanda cihazları."],
        ["Fasıl 86 Not 2",
         "86.07’ye dahildir: (a) dingiller, tekerlekler, tekerlek takımları, metal bandajlar, tekerlek gövde ve göbekleri; (b) şasiler, bojiler ve bissel-bojiler; (c) dingil kutuları, her türlü fren tertibatı; (d) müsademe tamponları, cer kancaları, diğer koşum takımları ve geçiş körükleri; (e) vagonlara ait karoseri eşyası."],
        ["Fasıl 86 Not 3",
         "Not 1 saklı kalmak üzere 86.08’e dahildir: (a) birleştirilmiş hatlar, döner platformlar ve döner köprüler, yük gabarileri ve durdurma tamponları; (b) demiryolu, tramvay, karayolu, iç su yolu, park yeri, liman tesisi ve havalimanları için semaforlar, mekanik işaret diskleri ve levhaları, demiryolu geçidi kumanda cihazları, makas tertibatı, uzaktan manevra cihazları ve diğer mekanik (elektromekanik dahil) sinyal, emniyet, trafik kontrol ve kumanda cihazları — <b>elektrikli aydınlatma tertibatı bulunsun bulunmasın</b>."],
        ["Fasıl 86 Genel Açıklamalar",
         "“Demiryolu” ve “tramvay” çelik raylı hatlar yanında manyetik yükselme veya beton hat kullanan kılavuz sistemleri de kapsar. Asli özelliğe sahip tamamlanmamış taşıtlar tamamlanmış gibi sınıflandırılır: güç tertibatı veya ölçü aletleri takılmamış lokomotif, koltukları monte edilmemiş yolcu vagonu, süspansiyon ve tekerlekleriyle tamamlanmış vagon alt gövdesi. Şasiye monte edilmemiş karoserler ise 86.07’dedir. Hariç: teşhir modelleri (90.23), demiryolu taşıtına monte ağır topçu silahları (93.01), oyuncak trenler (95.03), eğlence parkı ve panayır eşyası (95.08)."],
        ["86.02–86.03 Açıklama Notları",
         "Dizel lokomotiflerin üç türü (dizel-elektrikli, dizel-hidrolik, dizel-mekanik) ve her tip buhar lokomotifi 86.02’dedir; hem yol hem ray üzerinde giden traktörler 87.01. Kendinden hareketli vagonlar güç ünitesine ek olarak yolcu veya yük taşımak için düzenlenebilir; başlıca özellikleri iki ucunda veya ortada yüksek bir yerde kumanda kabini bulunmasıdır. Motoruna dokunulmadan yalnız tekerlekleri değiştirilip direksiyonu bloke edilerek otoraya çevrilebilen motorlu kara taşıtları 87.02’dedir."],
        ["86.04 ve 86.06 Açıklama Notları",
         "86.04 hat kenarı yapılarında, onarım ve bakımda kullanılmak üzere düzenlenmiş taşıtları kapsar; basit tekerlekli platformlara veya uygun olmayan gövdelere monte edilmiş makineler Fasıl 84’tedir (84.25, 84.26, 84.28, 84.29, 84.30). Yol gösterici raylarla teçhizatlı özel vagonlarla taşınmak üzere tasarlanmış römorklar 86.06 dışıdır (87.16)."],
        ["86.07 Açıklama Notu",
         "Aksam iki şartı sağlamalıdır: (i) yalnız ve esas itibarıyla Fasıl 86 taşıtlarına ait olduğu açıkça anlaşılmalı; (ii) Bölüm XVII notlarıyla hariç tutulmamış olmalı. Isıtma veya fren tertibatı için bağlantı başlıklı borular ve bojiye monte edilen hidrolik şok tertibatı da buradadır. Demiryolu aksamı olduğu anlaşılacak derecede işçilik görmemiş adi metal profil, sac, levha ve borular Bölüm XV’tedir."],
        ["86.08 Açıklama Notu",
         "Mekanik işaret cihazında işaret kolları iki veya daha fazla hareket yapar ve her hareket ayrı bir talimat anlamına gelir. Mekanik unsuru olmayan levhalar maddesine göre (44.21, 83.10); geçit engelleri maddesine göre (73.08, 44.21), ancak engelin açık-kapalı olduğunu gösteren mekanik işaretler 86.08’de; havai hat pilonları ve portikler 68.10, 73.08 vb.; işaret lambaları 85.30 veya 94.05; lokomotif çaprazları ile vagon devirici ve iticiler 84.28; makas dillerini kumanda mekanizmasına bağlayan çubuklar 73.02."],
        ["86.09 Açıklama Notu",
         "Konteynerler eşyanın bir nevi ambalajıdır; kara, deniz veya hava taşımasında genellikle ikinci bir ambalaja gerek olmadan adresten adrese taşımaya uygun, metal veya ahşap olabilen, kanca, halka, tekerlek, destek gibi teçhizatlı birimlerdir. Sıvı veya gaz konteyneri taşıt tipine uygun ve bir destekle irtibatlıysa 86.09’da, değilse maddesine göre sınıflandırılır. Hariç: bu nitelikte olmayan sandık ve kutular (maddesine göre), kara-demiryolu römorkları (87.16), modüler yapı üniteleri (94.06)."],
    ],
    "sinir_komsulari": [
        ["Ahşap travers", "44.06", "Fasıl 86 Not 1(a)"],
        ["Beton travers; hava treni kılavuz hattının beton kısmı", "68.10", "Fasıl 86 Not 1(a)"],
        ["Demir-çelik ray, travers, makas dili; birleştirilmemiş hat malzemesi", "73.02", "Fasıl 86 Not 1(b); birleştirilmiş hat ise 86.08"],
        ["Elektrikli sinyalizasyon, emniyet ve trafik kontrol cihazı", "85.30", "Fasıl 86 Not 1(c); mekanik olan 86.08"],
        ["İşaret lambası; tren ön lambası", "85.30 / 94.05", "86.08 hariç tutması; Bölüm XVII Not 2(k)"],
        ["Mekanik unsuru olmayan hız sınırı veya yön levhası", "44.21 / 83.10", "Maddesine göre sınıflandırılır"],
        ["Demiryolu geçidi engeli (bariyer kolu)", "73.08 / 44.21", "Maddesine göre; açık-kapalı gösteren mekanik işaret 86.08"],
        ["Hem karayolu hem demiryolunda kullanılan traktör", "87.01", "Bölüm XVII Not 4(a); 86.02 hariç tutması"],
        ["Kara-demiryolu kamyonu", "87.04", "Karayolunda ve rayda seyahat için özel düzenlenmiş"],
        ["Tekerlek değiştirilerek otoraya çevrilebilen motorlu kara taşıtı", "87.02", "86.03 hariç tutması"],
        ["Raylı vagonla taşınan kara-demiryolu römorku", "87.16", "86.06 ve 86.09 hariç tutması"],
        ["Basit tekerlekli platforma monte vinç, kaldırma makinesi", "84.25 / 84.26 / 84.28", "86.04 hariç tutması"],
        ["Demiryolu taşıtına monte ağır topçu silahı", "93.01", "Fasıl 86 Genel Açıklamalar"],
        ["Oyuncak tren; teşhir modeli", "95.03 / 90.23", "Bölüm XVII Not 1; Genel Açıklamalar"],
        ["Lokomotif tekerleği rulmanı; lokomotif dizel motoru", "84.82 / 84.08", "Bölüm XVII Not 2(e)"],
    ],
    "tuzaklar": [
        "<b>Elektrikli ≠ mekanik sinyal.</b> Mekanik veya elektromekanik sinyal, emniyet ve trafik kontrol cihazları 86.08’de; elektrikli olanlar 85.30’da. Elektro-pnömatik sistemde işaret kolu ve pnömatik tertibat 86.08’de, elektrikli kumanda tablosu Fasıl 85’te kalır.",
        "<b>86.08 yalnız demiryolu değildir.</b> Karayolu, iç su yolu, park yeri, liman ve havalimanları için mekanik trafik kumanda cihazları da buradadır; üzerinde elektrikli aydınlatma bulunması sonucu değiştirmez.",
        "<b>Travers ve ray 86.08 değildir.</b> Ahşap travers 44.06, beton travers 68.10, demir-çelik hat malzemesi 73.02. Traverslerle birleştirilmiş hat (kruvazman, makas, kavisli hat) ise 86.08.",
        "<b>Müsademe tamponu ≠ durdurma tamponu.</b> Vagonun üzerindeki müsademe tamponu aksamdır (86.07); hat sonuna konulan hidrolik veya yaylı durdurma tamponu sabit malzemedir (86.08).",
        "<b>Lokomotifte güç kaynağına bakılır.</b> Akümülatörlü lokomotif de 86.01’dir; tekerlekleri elektrik motoru döndürse bile dizel-elektrikli lokomotif 86.02’dedir.",
        "<b>Bakım taşıtı 86.04’e öncelik alır.</b> 86.03 ve 86.05 metinleri 86.04’e girenleri açıkça hariç tutar; bakım taşıtı kendinden hareketli olsun olmasın 86.04’tedir. Basit tekerlekli platforma monte makine ise Fasıl 84’tedir.",
        "<b>Monte edilmemiş karoser aksamdır.</b> Şasisine monte edilmemiş vagon, tramvay veya tender karoseri 86.07’de; buna karşılık koltuksuz yolcu vagonu veya güç tertibatı takılmamış lokomotif GYK 2(a) ile tamamlanmış taşıt gibi sınıflandırılır.",
        "<b>Rayda da giden kara taşıtı Fasıl 87’dir.</b> Hem rayda hem karayolunda kullanılmak üzere özel imal edilen traktör 87.01’de, kara-demiryolu kamyonu 87.04’te.",
        "<b>Konteyner metalden olsa da 86.09’dadır.</b> Bir veya daha fazla taşıma şekline göre özel yapılmış ve donatılmış konteyner ambalaj niteliğindedir; modüler yapı üniteleri 94.06, kara-demiryolu römorkları 87.16.",
        "<b>Not 2 listesi trene mahsus eşyayı da dışarıda bırakır.</b> Rulman 84.82, motor Fasıl 84, pantograf ve akım kollektörü Fasıl 85, hız göstergesi 90.29, panel saati Fasıl 91, ön lamba 94.05, fırça 96.03.",
    ],
    "hafiza": {
        "kanca": "EL – Dİ – KEN – BAK  /  YOL – YÜK  /  PAR – SAB – KON",
        "aciklama": "<b>EL</b>ektrikli lokomotif 86.01 · <b>Dİ</b>ğer lokomotif ve tender 86.02 · <b>KEN</b>dinden hareketli vagon 86.03 · <b>BAK</b>ım-servis 86.04 · <b>YOL</b>cu ve özel vagon 86.05 · <b>YÜK</b> vagonu 86.06 · <b>PAR</b>ça 86.07 · <b>SAB</b>it hat ve sinyal 86.08 · <b>KON</b>teyner 86.09. Görsel benzetme: istasyonda yürüyün; önce elektrikli ve dizel lokomotif, sonra kendi motoruyla giden banliyö treni ve hattı onaran sarı bakım vagonu; arkada yolcu ve yük vagonları, depoda yedek boji ve tekerlekler, hat başında makas kolu ve semafor, en sonda vince takılmış bir konteyner."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda daha çok seçeneklerde/çeldirici olarak yer almıştır; doğrudan sorulan konu konteynerlerdir.",
        "Uluslararası eşya taşımacılığına uygun demir konteynerlerin, 73. Fasıldaki demir-çelik eşya pozisyonları ve 87.09 çeldiricilerine karşın 86.09’da sınıflandırıldığı.",
        "Bölüm XVII Not 2 mantığı: nakil vasıtasına mahsus olsa bile elektromanyetik fren (85.05), bisiklet zili (83.06), contalar (84.84), motorlar (Fasıl 84) gibi eşyanın bölüm dışında kaldığı; bu sorularda Fasıl 86–88 pozisyonları çeldirici olarak verilmiştir.",
        "Taşımayla ilgili olup Bölüm XVII’ye girmeyen eşya: teleferiklerin 84.28’de sınıflandırıldığı; 87.09 ve 88.04 seçenekleri çeldirici olmuştur.",
        "Nakil vasıtası camları: çerçevesiz emniyet camı Fasıl 70’te kalırken ısıtma tertibatlı ön camın Fasıl 70 dışına çıktığı lokomotif ön camı örneğiyle sorulmuştur.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Uluslararası eşya taşımacılığına uygun olarak yapılmış demir konteynerler hangi tarife pozisyonundadır?",
            "secenekler": ["73.09", "73.26", "86.09", "87.09"],
            "cevap": "C",
            "aciklama": "86.09, bir veya daha fazla taşıma şekline göre özel olarak yapılmış ve donatılmış konteynerleri kapsar; bunlar metal veya ahşap olabilen, eşyanın bir nevi ambalajı sayılan birimlerdir. 87.09 ise fabrika, liman ve havalimanlarında kısa mesafe yük arabalarıdır.",
        },
        {
            "soru": "Elektromanyetik frenler hangi tarife pozisyonunda sınıflandırılır?",
            "secenekler": ["84.12", "84.81", "85.05", "87.09", "88.04"],
            "cevap": "C",
            "aciklama": "Bölüm XVII Not 2(f) elektrik makina ve teçhizatını bölüm dışında bırakır; Bölüm XVII Genel Açıklamaları elektromanyetik kıskaç ve frenlerin 85.05’te yer aldığını belirtir. Nakil vasıtasına mahsus olması 87.09 veya 88.04’e götürmez.",
        },
    ],
    "ozet": [
        "Lokomotif: elektriği dışarıdan veya aküden alan 86.01, diğerleri ve tenderler 86.02; kendinden hareketli vagon 86.03.",
        "Bakım-servis taşıtı her durumda 86.04; kendinden hareketli olmayan yolcu ve özel vagon 86.05, yük vagonu 86.06.",
        "Aksam 86.07’dedir; ama Bölüm XVII Not 2 eşyası (rulman, motor, elektrik teçhizatı, Fasıl 90 aleti, lamba) kendi yerine gider.",
        "Birleştirilmiş hat ve mekanik/elektromekanik sinyalizasyon 86.08; elektrikli sinyalizasyon 85.30; traversler ve ray 44.06, 68.10, 73.02.",
        "Konteyner 86.09; kara-demiryolu römorku 87.16, modüler yapı 94.06.",
        "Hem rayda hem karayolunda kullanılan taşıt Fasıl 87; kılavuz hatlı hava yastıklı taşıt Fasıl 86.",
    ],
}

S = []

# --- Eşya → 4’lü pozisyon (5) ---
S.append(soru(
    "Tarife Cetveline göre, enerjisini araç üzerinde taşınan elektrik akümülatörlerinden alan demiryolu lokomotifi hangi pozisyonda sınıflandırılır?",
    "86.01", ["86.02", "86.03", "86.04", "87.09"], "A", EP,
    "86.01 elektrik enerjisini dışarıdan alan veya elektrik akümülatörlü olan bütün elektrikli lokomotifleri kapsar. 86.02 elektrik dışındaki güç kaynaklarıyla çalışan lokomotifler, 86.03 yolcu veya yük taşıyabilen kendinden hareketli vagonlar içindir. 87.09 raysız kısa mesafe yük arabalarıdır; “akümülatörlü” ifadesi bu çeldiriciye çekebilir.",
    "86.01 pozisyon metni ve Açıklama Notu."))
S.append(soru(
    "Dizel motorun bir elektrik jeneratörünü çalıştırdığı ve elde edilen elektrik gücüyle tekerleklerin döndürüldüğü demiryolu lokomotifi hangi pozisyonda yer alır?",
    "86.02", ["86.01", "86.03", "85.02", "84.08"], "C", EP,
    "Dizel-elektrikli lokomotifler 86.02 Açıklama Notunda dizel lokomotif türleri arasında sayılmıştır; tekerlekleri elektrik motorunun döndürmesi onu 86.01’e taşımaz, çünkü elektrik dışarıdan veya akümülatörden alınmaz. Komple lokomotif söz konusu olduğundan jeneratör grubu (85.02) veya dizel motor (84.08) pozisyonları uygulanmaz.",
    "86.02 Açıklama Notu (1)(a); 86.01 Açıklama Notu."))
S.append(soru(
    "Hat boyunca türeyen yabani otları yok etmeye mahsus püskürtme tertibatıyla donatılmış, kendinden hareketli olmayan demiryolu vagonu hangi pozisyonda sınıflandırılır?",
    "86.04", ["86.05", "86.06", "84.24", "86.03"], "E", EP,
    "86.04, demiryollarının bakım veya servisine ait taşıtları kendinden hareketli olsun olmasın kapsar ve Açıklama Notu yabani ot öldürmeye mahsus püskürtmeli vagonları açıkça sayar. 86.05 ve 86.03 metinleri 86.04’e girenleri hariç tutar. Püskürtme cihazı (84.24) çeldiricidir; burada sınıflandırılan, cihazla donatılmış demiryolu vagonudur.",
    "86.04 pozisyon metni ve Açıklama Notu."))
S.append(soru(
    "Dizel motorla donatılmış, iki ucunda kumanda kabini bulunan ve yolcu taşımak için düzenlenmiş kendinden hareketli demiryolu aracı (otomotris) hangi pozisyonda yer alır?",
    "86.03", ["86.02", "86.05", "87.02", "86.01"], "B", EP,
    "Kendinden hareketli demiryolu vagonları güç ünitesine ek olarak yolcu veya yük taşımak için düzenlenebilir; başlıca özellikleri her iki uçta veya ortada yüksek bir yerde kumanda kabini bulunmasıdır ve otomotrisler bu pozisyonda sayılmıştır. 86.05 kendinden hareketli olmayan vagonlar, 86.02 lokomotifler içindir. 87.02 yalnız tekerlek değiştirilerek otoraya çevrilebilen motorlu kara taşıtlarını alır.",
    "86.03 Açıklama Notu (B)."))
S.append(soru(
    "Canlı balık ve kümes hayvanlarının taşınması için özel olarak donatılmış, kendinden hareketli olmayan demiryolu vagonu hangi pozisyonda sınıflandırılır?",
    "86.06", ["86.05", "86.09", "86.04", "87.16"], "D", EP,
    "86.06 kendinden hareketli olmayan, yük taşımaya mahsus vagonları kapsar; canlı balık ve kümes hayvanı taşımaya özel donatılmış vagonlar Açıklama Notunda açıkça sayılmıştır. 86.05 yolcu, posta ve özel amaçlı vagonlar; 86.09 konteynerler; 87.16 raysız römorklar içindir.",
    "86.06 Açıklama Notu (9)."))

# --- Olumsuz teşhis (4) ---
S.append(soru(
    "Aşağıdakilerden hangisi, demiryolu taşıtında kullanılsa bile 86.07 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Vagon tekerlek takımına ait bilyalı rulman",
    ["Boji ve bissel-boji", "Müsademe tamponu", "Şasisine monte edilmemiş yolcu vagonu karoseri", "Lokomotif dingil kutusu"],
    "E", OT,
    "Bölüm XVII Not 2(e) gereği 84.82’deki rulmanlar, nakil vasıtasına mahsus olsa bile “aksam” sayılmaz ve 84.82’de kalır. Bojiler, müsademe tamponları ve dingil kutuları Fasıl 86 Not 2’de, monte edilmemiş karoserler Genel Açıklamalarda 86.07 aksamı olarak sayılmıştır. Tuzak, dingil kutusu ile rulmanı aynı sanmaktır.",
    "Bölüm XVII Not 2(e); Fasıl 86 Not 2; Fasıl 86 Genel Açıklamalar."))
S.append(soru(
    "Aşağıdakilerden hangisi 86.08 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Demiryolu hattı için betondan travers",
    ["Traverslerle birleştirilmiş makas ve kruvazman", "Lokomotifleri bir hattan diğerine geçiren döner platform", "Hat sonuna konulan hidrolik durdurma tamponu", "Liman tesisi için mekanik trafik kumanda cihazı"],
    "A", OT,
    "Fasıl 86 Not 1(a) uyarınca ahşap veya betondan traversler Fasıl 86 dışındadır; beton traversler 68.10’dadır. Birleştirilmiş hatlar, döner platformlar ve durdurma tamponları Not 3(a)’da, limanlar için mekanik trafik kumanda cihazları Not 3(b)’de 86.08 kapsamında sayılmıştır.",
    "Fasıl 86 Not 1(a) ve Not 3."))
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinin 86. faslında <b>yer almaz</b>?",
    "Demiryolu taşıtı üzerine monte edilmiş ağır topçu silahı",
    ["Lokomotif tenderi", "Mekanik olarak çalışmayan, ayakla hareket ettirilen ray muayene bisikleti", "Kılavuz hat üzerinde işletilmek üzere imal edilmiş hava yastıklı taşıt", "Gezici posta vagonu"],
    "C", OT,
    "Fasıl 86 Genel Açıklamaları demiryolu vasıtaları üzerine monte edilmiş ağır topçu silahlarını hariç tutar (93.01). Tender 86.02’de, ray muayene bisikleti 86.04’te, posta vagonu 86.05’tedir; kılavuz hatlı hava yastıklı taşıt Bölüm XVII Not 5 uyarınca Fasıl 86’dadır.",
    "Fasıl 86 Genel Açıklamalar; Bölüm XVII Not 5."))
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinin XVII. Bölümünde <b>yer almaz</b>?",
    "Fuar ve panayır eğlencelerine mahsus dizayn edilmiş çarpışan araba",
    ["Bir veya daha fazla taşıma şekline göre özel donatılmış konteyner", "Park yerleri için mekanik trafik kontrol cihazı", "Paraşüt", "Hava taşıtlarını fırlatma tertibatı"],
    "D", OT,
    "Bölüm XVII Not 1, 95.08’e giren eşyayı kapsam dışında bırakır; fuar ve panayır eğlencelerine mahsus çarpışan arabalar Bölüm Genel Açıklamalarında 95.08’e gönderilmiştir. Konteyner (86.09), mekanik trafik kontrol cihazı (86.08), paraşüt (88.04) ve uçak fırlatma tertibatı (88.05) bölüm içindedir.",
    "Bölüm XVII Not 1; Bölüm XVII Genel Açıklamalar (I)."))

# --- Farklı/aynı pozisyon veya fasıl (4) ---
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
    "Lokanta vagonu",
    ["Atölye vagonu", "Vinçli vagon", "Balast sıkıştırma makinesiyle donatılmış vagon", "Rayları kontrol eden deneme vagonu"],
    "B", FA,
    "Lokanta vagonu, kendinden hareketli olmayan yolcu vagonları arasında 86.05’te sayılmıştır. Atölye, vinçli, balast sıkıştırıcılı ve deneme vagonları demiryolunun bakım veya servisine ait taşıtlar olarak 86.04’tedir. Hepsi “vagon” kelimesiyle anıldığı için aynı pozisyon sanılabilir.",
    "86.04 ve 86.05 pozisyon metinleri ve Açıklama Notları."))
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda yer alır?",
    "Elektrikli trafik sinyalizasyon ve kumanda cihazı",
    ["Demiryolu için semafor", "Demiryolu geçidi için mekanik kumanda cihazı", "Makas tertibatı", "Havalimanı için mekanik işaret diski"],
    "D", FA,
    "Fasıl 86 Not 1(c) uyarınca elektrikli sinyalizasyon, emniyet, trafik kontrol ve kumanda cihazları 85.30’da, yani Fasıl 85’tedir. Semaforlar, geçit kumanda cihazları, makas tertibatı ve havalimanları için mekanik işaret diskleri Not 3(b) gereği 86.08’dedir.",
    "Fasıl 86 Not 1(c) ve Not 3(b)."))
S.append(soru(
    "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda sınıflandırılır?",
    "Dizel-hidrolik lokomotif – Lokomotif tenderi",
    ["Akümülatörlü lokomotif – Dizel-elektrikli lokomotif", "Sarnıçlı vagon – Sıvı taşımaya mahsus konteyner", "Boji – Birleştirilmiş hat", "Posta vagonu – Kereste taşıma vagonu"],
    "A", FA,
    "86.02 diğer lokomotifleri ve lokomotif tenderlerini birlikte kapsar; dizel-hidrolik lokomotif ve tender aynı pozisyondadır. Akümülatörlü lokomotif 86.01, dizel-elektrikli 86.02; sarnıçlı vagon 86.06, konteyner 86.09; boji 86.07, birleştirilmiş hat 86.08; posta vagonu 86.05, kereste vagonu 86.06’dır.",
    "86.01, 86.02, 86.05–86.09 Açıklama Notları."))
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
    "Hem rayda hem karayolunda gidebilen kara-demiryolu kamyonu",
    ["Otomotris", "Drezin", "Kılavuz hat üzerinde işleyen hava yastıklı taşıt (hava treni)", "Elektrikli tramvay arabası"],
    "E", FA,
    "Bölüm XVII Not 4(a) uyarınca hem karayolunda hem raylar üzerinde kullanılmak üzere özel imal edilen taşıtlar Fasıl 87’dedir; kara-demiryolu kamyonu 87.04 Açıklama Notunda sayılmıştır. Otomotris ve tramvay arabası 86.03, drezin 86.04, hava treni Bölüm XVII Not 5 gereği Fasıl 86’dadır.",
    "Bölüm XVII Not 4 ve Not 5; 87.04 Açıklama Notu (4)."))

# --- Fasıl notu · Tanım/Eşik (4) ---
S.append(soru(
    "Fasıl 86 Not 2’de 86.07 pozisyonuna dahil olduğu belirtilen eşya arasında aşağıdakilerden hangisi <b>yoktur</b>?",
    "Döner platformlar ve döner köprüler",
    ["Dingil kutuları ve her türlü fren tertibatı", "Şasiler, bojiler ve bissel-bojiler", "Müsademe tamponları ve geçiş körükleri", "Vagonlara ait karoseri eşyası"],
    "C", TN,
    "Döner platformlar ve döner köprüler sabit hat malzemesi olarak Fasıl 86 Not 3(a)’da 86.08’e dahil edilmiştir. Dingil kutuları, fren tertibatı, şasiler, bojiler, müsademe tamponları, geçiş körükleri ve vagon karoseri eşyası Not 2’de 86.07 kapsamında sayılır.",
    "Fasıl 86 Not 2 ve Not 3(a)."))
S.append(soru(
    "Fasıl 86 Not 3’e göre 86.08 pozisyonunun kapsamıyla ilgili aşağıdakilerden hangisi <b>doğrudur</b>?",
    "Mekanik sinyal ve trafik kontrol cihazları, elektrikli aydınlatma tertibatı bulunsa da bu pozisyondadır.",
    ["Yalnız demiryolu ve tramvaylar için olan cihazları kapsar; karayolu ve liman için olanlar Fasıl 84’tedir.",
     "Elektrikli sinyalizasyon ve trafik kontrol cihazları da bu pozisyonda yer alır.",
     "Demir veya çelikten raylar ve traversler bu pozisyonda sınıflandırılır.",
     "Elektrikli aydınlatma tertibatı bulunan mekanik sinyal cihazları 94.05’te yer alır."],
    "B", TN,
    "Not 3(b), demiryolu, tramvay, karayolu, iç su yolu, park yeri, liman ve havalimanları için mekanik (elektromekanik dahil) sinyal ve trafik kontrol cihazlarını elektrikli aydınlatma tertibatı bulunsun bulunmasın 86.08’e dahil eder. Elektrikli olanlar Not 1(c) ile 85.30’a, demir-çelik ray ve traversler Not 1(b) ile 73.02’ye gider.",
    "Fasıl 86 Not 1 ve Not 3(b)."))
S.append(soru(
    "Bölüm XVII Not 3’e göre aşağıdakilerden hangisi <b>doğrudur</b>?",
    "İki veya daha fazla pozisyona girebilecek aksam, asıl kullanımına tekabül eden pozisyonda sınıflandırılır.",
    ["İki veya daha fazla pozisyona girebilecek aksam, numara sırasına göre en son pozisyonda sınıflandırılır.",
     "Sadece veya esas itibarıyla bu fasıllardaki taşıtlarda kullanılmaya uygun olmayan aksam da Fasıl 86–88 aksam pozisyonlarına girer.",
     "Not 3, Fasıl 89’daki gemi aksamına da uygulanır ve bu aksam 89.06’da sınıflandırılır.",
     "Birden fazla taşıt türüne uyan aksam, kıymeti en yüksek taşıtın aksam pozisyonunda sınıflandırılır."],
    "A", TN,
    "Not 3’e göre Fasıl 86–88’deki aksam atfı, sadece veya esas itibarıyla bu taşıtlarda kullanılmaya uygun olmayan eşyayı kapsamaz; birden fazla pozisyona girebilecek aksam asıl kullanımına göre sınıflandırılır. Numara sırası (GYK 3(c) mantığı) ve kıymet ölçütü notta yoktur; not yalnız Fasıl 86–88’den söz eder.",
    "Bölüm XVII Not 3; Bölüm XVII Genel Açıklamalar (III)(B)."))
S.append(soru(
    "Fasıl 86 Genel Açıklamalarına göre “demiryolu” ve “tramvay” terimleri hakkında aşağıdakilerden hangisi <b>doğrudur</b>?",
    "Manyetik yükselme veya beton hat kullanan kılavuz sistemlerini de kapsar.",
    ["Yalnız çelik raylı hatları kapsar; manyetik yükselmeli sistemler Fasıl 84’tedir.",
     "Beton kılavuz hatlar üzerinde işleyen taşıtlar Fasıl 87’de sınıflandırılır.",
     "Dar ebatlı ve tek raylı demiryolları bu terimlerin dışında kalır.",
     "Tramvay terimi yalnız elektrikle işleyen şehir içi hatları kapsar."],
    "D", TN,
    "Fasıl 86 Genel Açıklamaları bu terimlerin yalnız çelik raylı geleneksel demiryolu ve tramvayları değil, manyetik yükselmeyi veya beton hat kullanımını sağlayan kılavuz sistemlerini de kapsadığını belirtir. Fasıl dar ebatlı ve tek raylı demiryollarını da açıkça içine alır.",
    "Fasıl 86 Genel Açıklamalar."))

# --- Genel Yorum Kuralı (2) ---
S.append(soru(
    "Koltukları henüz monte edilmemiş, kendinden hareketli olmayan demiryolu yolcu vagonu hangi pozisyonda ve hangi Genel Yorum Kuralları uyarınca sınıflandırılır?",
    "86.05 – GYK 1 ve 2(a)",
    ["86.07 – GYK 1", "86.05 – GYK 3(b)", "86.03 – GYK 1 ve 2(a)", "86.06 – GYK 1 ve 2(a)"],
    "E", GY,
    "Fasıl 86 Genel Açıklamaları, koltukları monte edilmemiş yolcu vagonlarını tamamlanmış taşıtın asli özelliklerine sahip eksik eşya örneği olarak verir; GYK 2(a) ile tamamlanmış yolcu vagonu gibi 86.05’te sınıflandırılır. Aksam pozisyonu (86.07) yalnız monte edilmemiş karoserler içindir; 86.03 kendinden hareketli vagonları kapsar. Ortada birden fazla pozisyona giren karışım olmadığından GYK 3(b) uygulanmaz.",
    "GYK 1 ve 2(a); Fasıl 86 Genel Açıklamalar."))
S.append(soru(
    "Şasisi üzerine monte edilmemiş halde ayrı olarak ithal edilen tramvay arabası karoseri hangi pozisyonda ve hangi kural uyarınca sınıflandırılır?",
    "86.07 – GYK 1",
    ["86.03 – GYK 1 ve 2(a)", "86.05 – GYK 2(a)", "87.07 – GYK 1", "86.03 – GYK 3(b)"],
    "B", GY,
    "Fasıl 86 Genel Açıklamaları, motorlu vagonların, tramvay arabalarının, vagonların ve tenderlerin şasileri üzerine monte edilmemiş karoserlerini açıkça demiryolu taşıtı aksamı (86.07) sayar; sınıflandırma pozisyon metni ve notlarla, yani GYK 1 ile yapılır. Karoser tek başına taşıtın asli özelliğini taşımadığından GYK 2(a) ile 86.03’e götürmek tuzaktır; 87.07 motorlu kara taşıtı karoserleri içindir.",
    "GYK 1; Fasıl 86 Genel Açıklamalar; Fasıl 86 Not 2(e)."))

# --- Eşleştirme / Boşluk doldurma (2) ---
S.append(soru(
    "Aşağıdaki eşya ile pozisyonların doğru eşleştirmesi hangi seçenekte verilmiştir?<br/>I. Lokomotif tenderi<br/>II. Drezin<br/>III. Kendinden hareketli olmayan frigorifik vagon<br/>IV. Hat sonuna konulan hidrolik durdurma tamponu<br/>a) 86.08 · b) 86.02 · c) 86.06 · d) 86.04",
    "I-b, II-d, III-c, IV-a",
    ["I-b, II-c, III-d, IV-a", "I-d, II-b, III-c, IV-a", "I-b, II-d, III-a, IV-c", "I-c, II-d, III-b, IV-a"],
    "C", ES,
    "Tender 86.02’de, drezin bakım-servis taşıtı olarak 86.04’te, frigorifik vagon yük vagonu olarak 86.06’da, hat sonundaki durdurma tamponu sabit hat malzemesi olarak 86.08’dedir. Vagona takılan müsademe tamponu ise 86.07 aksamıdır; iki tampon türünü karıştırmak tipik hatadır.",
    "86.02, 86.04, 86.06 Açıklama Notları; Fasıl 86 Not 3(a)."))
S.append(soru(
    "Bölüm XVII Not 4’e göre, hem karayolunda hem de raylar üzerinde kullanılabilecek şekilde özel olarak imal edilmiş taşıtlar ..... Fasılda; aynı zamanda kara taşıtı olarak da kullanılabilecek şekilde özel olarak imal edilmiş hava taşıtları ise ..... Fasılda sınıflandırılır. Boşluklara sırasıyla gelmesi gerekenler hangisidir?",
    "87 – 88",
    ["86 – 88", "86 – 87", "87 – 87", "86 – 89"],
    "A", ES,
    "Not 4 hem karayolu hem ray taşıtlarını Fasıl 87’ye, kara taşıtı olarak da kullanılabilen hava taşıtlarını Fasıl 88’e gönderir. Rayda da gidebilmesi taşıtı Fasıl 86’ya götürmez; Fasıl 86 yalnız raylar üzerinde hareket edenleri alır (Fasıl 87 Not 1).",
    "Bölüm XVII Not 4; Fasıl 87 Not 1."))

# --- Çoktan-çoğa (2) ---
S.append(soru(
    "Bölüm XVII Not 2’ye göre aşağıdakilerden hangileri, nakil vasıtalarına mahsus oldukları anlaşılsa bile “aksam ve parça” sayılmaz?<br/>I. Sertleştirilmemiş vulkanize kauçuktan çamurluk kapağı<br/>II. Vagon bojisi<br/>III. Bisiklet zili<br/>IV. Lokomotif dingil kutusu",
    "I ve III",
    ["I ve II", "II ve IV", "I, III ve IV", "Yalnız III"],
    "D", CC,
    "Not 2(a) sertleştirilmemiş vulkanize kauçuktan eşyayı (40.16), Not 2(d) 83.06 eşyasını (bisiklet zili) aksam tabirinin dışında bırakır. Boji ve dingil kutusu Fasıl 86 Not 2’de 86.07 aksamı olarak sayılmıştır.",
    "Bölüm XVII Not 2(a) ve (d); Bölüm XVII Genel Açıklamalar (III)(A); Fasıl 86 Not 2."))
S.append(soru(
    "Bölüm XVII notlarına göre aşağıdaki ifadelerden hangileri <b>doğrudur</b>?<br/>I. Kılavuz bir hat üzerinde işletilmek üzere imal olunan hava yastıklı taşıtlar Fasıl 86’ya girer.<br/>II. Hem karada hem de suda işletilmek üzere imal olunan hava yastıklı taşıtlar Fasıl 89’a girer.<br/>III. Hem denizde hem de karada kullanılan motorlu taşıtlar Fasıl 87’de sınıflandırılır.<br/>IV. Hava yastıklı taşıtların aksam ve parçaları, taşıtın sınıflandırıldığı pozisyonda yer alır.",
    "I, III ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "Yalnız I"],
    "B", CC,
    "Not 5’e göre kılavuz hatlı hava yastıklı taşıtlar Fasıl 86’da, karada veya hem karada hem suda işleyenler Fasıl 87’de, yalnız suda işleyenler Fasıl 89’dadır; aksamları da taşıtın pozisyonuna gider. Hem denizde hem karada kullanılan motorlu taşıtlar Not 4 gereği Fasıl 87’dedir. II yanlıştır; çift ortamlı hava yastıklı taşıt Fasıl 87’dedir.",
    "Bölüm XVII Not 4 ve Not 5."))

# --- Senaryo (2) ---
S.append(soru(
    "Bir lojistik firması; metal gövdeli, kapıları ve köşelerinde kaldırma halkaları bulunan, ikinci bir ambalaja gerek kalmadan eşyanın karayolu, deniz yolu ve demiryolu ile adresten adrese taşınmasına göre özel olarak düzenlenmiş ve donatılmış yük taşıma birimleri ithal etmektedir. Eşya hangi pozisyonda sınıflandırılır?",
    "86.09",
    ["73.09", "87.16", "86.06", "94.06"],
    "E", SN,
    "Bir veya daha fazla taşıma şekline göre özel olarak yapılmış ve donatılmış, kanca, halka gibi teçhizatı olan ve ikinci ambalaja gerek kalmadan taşımaya uygun konteynerler 86.09’dadır; metalden olmaları sonucu değiştirmez. Römork (87.16) ve yük vagonu (86.06) taşıttır; modüler yapı üniteleri ise 86.09 Açıklama Notunda 94.06’ya gönderilmiştir.",
    "86.09 pozisyon metni ve Açıklama Notu."))
S.append(soru(
    "Bir liman işletmesi; kontrol noktasından manivela ve çubuklarla mekanik olarak çalıştırılan, kolları iki veya daha fazla hareket yaparak deniz taşıtlarına ayrı talimatlar (“geç”, “dur”) veren ve gece görülebilmesi için elektrikli aydınlatma tertibatıyla donatılmış bir işaret cihazı ithal etmektedir. Cihaz hangi pozisyonda yer alır?",
    "86.08",
    ["85.30", "94.05", "89.07", "85.31"],
    "C", SN,
    "Fasıl 86 Not 3(b), limanlar ve iç su yolları için mekanik sinyal ve trafik kontrol cihazlarını elektrikli aydınlatma tertibatı bulunsun bulunmasın 86.08’e dahil eder; işaret kollarının birden fazla hareketle ayrı talimat vermesi mekanik işaret cihazının tanımıdır. 85.30 yalnız elektrikli sinyalizasyon cihazları içindir; 94.05 lambalar, 89.07 yüzen işaret kuleleridir.",
    "Fasıl 86 Not 1(c) ve Not 3(b); 86.08 Açıklama Notu (B)."))

obj["sorular"] = S
yaz(obj)
