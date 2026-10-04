#!/usr/bin/env python3
"""Fasıl 88 modülü üreteci."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yardim_86_89 import EP, OT, FA, TN, GY, ES, CC, SN, soru, yaz  # noqa: E402

obj = {
    "tur": "fasil",
    "fasil": 88,
    "baslik": "Hava taşıtları, uzay taşıtları ve bunların aksam ve parçaları",
    "bolum": "XVII",
    "oz": {
        "vurgu": "Fasıl 88 hava taşıtlarını üç soruyla ayırır: Havadan hafif mi veya motorsuz mu? (balon, hava gemisi, planör, delta kanat, uçurtma → 88.01). İçinde pilot olmadan uçmak üzere mi tasarlanmış? (insansız hava taşıtı → 88.06). Değilse motorlu uçak, helikopter ve uzay araçları 88.02’dedir. Paraşütler 88.04, fırlatma-iniş tertibatı ve yer eğitim cihazları 88.05, 88.01, 88.02 ve 88.06 taşıtlarının aksamı 88.07’dedir.",
        "maddeler": [
            "Balonlar ve hava gemileri havadan hafif hava taşıtlarıdır; motorla işleyen hava gemileri de 88.01’dedir. Planörde ise motor bulunması veya motor takılmak üzere dizayn edilmiş olması 88.02’ye götürür.",
            "İnsansız hava taşıtı (Not 1): 88.01’dekiler dışında, içinde bir pilot olmadan uçmak üzere tasarlanmış her hava aracı; yük taşıyabilir, kalıcı entegre dijital kamera veya başka ekipman taşıyabilir. Yalnız eğlence amaçlı uçan oyuncaklar 95.03’tedir.",
            "Uydular, uzay araçlarını fırlatıcı araçlar ve yörünge-altı araçlar 88.02’de; askeri fırlatma araçları ve balistik füzeler 93.06’da.",
            "Kara taşıtı olarak da kullanılmak üzere özel imal edilmiş hava taşıtları Fasıl 88’dedir (Bölüm XVII Not 4).",
            "Uçak motorları (84.07–84.12), elektrik teçhizatı (Fasıl 85), aletler (Fasıl 90), ön lambalar (94.05) ve koltuklar (94.01) uçağa mahsus olsa da 88.07’ye girmez.",
        ],
    },
    "karar_tablosu": {
        "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
        "satirlar": [
            ["1", "Oyuncak veya yalnız eğlence amaçlı uçan model mi? Teşhir modeli mi? Süs modeli mi?",
             "<b>95.03</b> · <b>90.23</b> · <b>44.20</b> / <b>83.06</b>"],
            ["2", "Askeri fırlatma aracı veya balistik füze mi?", "<b>93.06</b>"],
            ["3", "Havadan hafif mi? (serbest veya bağımlı balon, hava gemisi)", "<b>88.01</b> (motorlu hava gemisi dahil)"],
            ["4", "Havadan ağır ve motorsuz mu? (planör, delta kanatlı planör, uçurtma)", "<b>88.01</b>"],
            ["5", "İçinde pilot olmadan uçmak üzere mi tasarlanmış?", "<b>88.06</b>"],
            ["6", "Motorlu uçak, helikopter, motorlu planör, uydu, uzay aracı fırlatıcısı veya yörünge-altı araç mı?",
             "<b>88.02</b>"],
            ["7", "Paraşüt, sevk edilebilir paraşüt, yamaç paraşütü, rotoşüt veya bunların aksamı mı?", "<b>88.04</b>"],
            ["8", "Uçak fırlatma tertibatı, iniş-durdurma tertibatı veya yerde uçuş eğitimi cihazı mı?*",
             "<b>88.05</b>"],
            ["9", "88.01, 88.02 veya 88.06 taşıtının aksamı mı? (Bölüm XVII Not 2 eşyası değilse)", "<b>88.07</b>"],
        ],
        "dipnot": "* Motorlu taşıt şasisine monte simülatör 87.05, römorka monte simülatör 87.16; refleks test cihazları 90.19; roket fırlatma rampaları 84.79; planörleri havalandıran motorlu vinçler 84.25.",
    },
    "pozisyon_haritasi": [
        ["88.01", "Balonlar, hava gemileri, planörler, delta kanatlı planörler, motorsuz diğer hava taşıtları",
         "Havadan hafif veya motorsuz",
         "Meteoroloji balonu, bağımlı balon, hava gemisi, planör, delta kanat, uçurtma"],
        ["88.02", "Diğer hava taşıtları; uzay araçları, fırlatıcılar, yörünge-altı araçlar",
         "Motorlu; 88.06 hariç",
         "Uçak, deniz uçağı, helikopter, motorlu planör, uydu, fırlatıcı roket"],
        ["88.04", "Paraşütler, paragliderler, rotoşütler; aksamı",
         "Malzemesi önemsiz; aksam ve aksesuar dahil",
         "Paraşüt, kuyruk paraşütü, yamaç paraşütü, paraşüt çantası, koşum takımı"],
        ["88.05", "Fırlatma ve iniş tertibatı; yerde uçuş eğitim cihazları; aksamı",
         "Üç ayrı grup cihaz",
         "Uçak gemisi fırlatma rampası, iniş durdurma tertibatı, uçuş simülatörü"],
        ["88.06", "İnsansız hava taşıtları",
         "İçinde pilot olmadan uçmak üzere tasarım; oyuncak hariç",
         "Kameralı drone, yük taşıyan İHA, yolcu taşıyan İHA"],
        ["88.07", "88.01, 88.02 veya 88.06 taşıtlarının aksam ve parçaları",
         "Yalnız veya esas itibarıyla bu taşıtlara; Not 2 dışı",
         "Pervane, rotor, iniş takımı, kanat, gövde, yakıt tankı"],
    ],
    "notlar": [
        ["Fasıl 88 Not 1",
         "“İnsansız hava taşıtı”: 88.01 pozisyonunda yer alanlar dışında, içinde bir pilot olmadan uçmak üzere tasarlanmış herhangi bir hava aracı. Yük taşıyacak şekilde tasarlanabilir veya kalıcı olarak entegre edilmiş dijital kameralar ya da uçuş sırasında faydacı işlevler görmesini sağlayan diğer ekipmanlarla donatılabilir. Yalnızca eğlence amacıyla tasarlanmış uçan oyuncaklar bu tabire girmez (95.03)."],
        ["Bölüm XVII Not 2 ve Not 4",
         "Not 2 gereği motorlar (84.07–84.12), Fasıl 85 elektrik teçhizatı, Fasıl 90 aletleri, Fasıl 91 saatleri, 94.05 lambaları uçağa mahsus olsa da “aksam” sayılmaz. Not 4: aynı zamanda kara taşıtı olarak kullanılabilecek şekilde özel imal edilmiş hava taşıtları Fasıl 88’in uygun pozisyonunda sınıflandırılır."],
        ["Fasıl 88 Genel Açıklamalar",
         "Fasıl; balonları, hava gemilerini, planörleri (88.01), diğer uçakları (88.02 veya 88.06), uzay araçlarını ve fırlatıcılarını (88.02), paraşütleri (88.04), uçak fırlatma, durdurma ve yerde uçuş eğitimi cihazlarını (88.05) ve bunların aksamını kapsar. Motorlarla donatılmamış veya iç teçhizatı olmayan tamamlanmamış uçaklar, tamamlanmış özelliklerine sahipse eksiksiz uçak gibi sınıflandırılır."],
        ["88.01 Açıklama Notu (balonlar)",
         "Havadan hafif hava taşıtları: serbest veya bağımlı (kabloyla yere bağlı) balonlar ve motorla işleyen hava gemileri. Meteoroloji balonları: sinyal balonları (normal ağırlık 350–1500 gram, 4500 grama kadar olabilir), pilot balonları (50–100 gram, rüzgâr yön ve hızı), irtifa balonları (4–30 gram, bulut yüksekliği). Çocuk oyuncağı balonlar 95.03’tedir; aşağı kalite kauçuktan yapılmaları, şişirme emziklerinin daha kısa olması ve reklam veya dekoratif baskı taşımaları ile ayırt edilir."],
        ["88.01 Açıklama Notu (planör ve uçurtma)",
         "Planör: atmosfer akımını kullanarak havada kalan, havadan ağır hava aracı; motorla donatılmış veya motorla donatılmak için dizayn edilmiş planörler 88.02’dedir. Delta kanatlı planörler, borulu metal yapı üzerine gerilmiş kumaş kanat ve yatay kumanda çubuğundan oluşur. Meteorolojik cihaz taşıyan, iple yere bağlanan uçurtmalar 88.01’de; çocuk oyuncağı uçurtmalar 95.03’te. Süs modelleri 44.20 veya 83.06, teşhir modelleri 90.23."],
        ["88.02 Açıklama Notu",
         "Havadan ağır motorlu hava araçları: kara uçakları, deniz uçakları, hem suya hem karaya inen uçaklar, otojirolar ve helikopterler; kara taşıtı olarak kullanılmak üzere özel imal edilmiş hava taşıtları dahil. Uzay araçları (uydular), uzay aracı fırlatıcıları (yüküne fırlatış sonunda <b>7000 m/s’den fazla</b> son hız verir) ve bilimsel yörünge-altı araçlar da buradadır. Hariç: yükünü 7000 m/s’yi aşmayan hızla parabolik yörüngede hedefe çarptıran askeri fırlatma araçları ve balistik füzeler (93.06), insansız hava taşıtları (88.06), eğlence amaçlı modeller ve oyuncaklar (95.03), eğlence parkı modelleri (95.08)."],
        ["88.04 Açıklama Notu",
         "İnsan, askeri teçhizat, meteorolojik alet ve işaretler için paraşütler (ipek, lif, keten, pamuk, kâğıt vb.), jet uçaklarını yavaşlatan kuyruk paraşütleri, dağ yamacından atlamak için yamaç paraşütleri ve meteorolojide iniş roketlerini kontrol eden dönen kanat üniteli rotoşütler. Aksam: paraşüt çantası, koşum takımları, açılmayı sağlayan mekanik yaylı sistem."],
        ["88.05 Açıklama Notu",
         "Üç grup: (A) gemi bordasındaki metal rampa gibi uçağın ilk hareketini sağlayan fırlatma tertibatı; (B) hava limanı, hangar ve uçak gemilerinde iniş hızını azaltan, durma mesafesini kısaltan durdurma tertibatı; (C) yerde uçuş eğitimi cihazları (elektronik uçuş ve hava muharebe simülatörleri, “link trainer”). Hariç: planörleri havalandıran motorlu vinçler (84.25), roket fırlatma rampaları ve kuleleri (84.79), motorlu taşıt şasisine veya römorka monte simülatörler (87.05, 87.16), uçuş şartlarında insan reaksiyonlarını kaydeden refleks test cihazları (90.19), havacıların genel eğitimine mahsus modeller (90.23)."],
        ["88.06 Açıklama Notu",
         "İnsansız hava aracı uzaktan kumandalı olabileceği gibi operatör müdahalesi olmadan programlanmış uçuş yeteneğine de sahip olabilir; GNSS alıcıları, engellerden kaçınma ve nesne izleme sistemleri bulunabilir. Yük veya yolcu taşıma, hava fotoğrafçılığı, tarımsal çalışma, kurtarma, yangınla mücadele, gözetleme gibi işlevler için kullanılır. Yalnız eğlence amaçlı uçan oyuncaklar (95.03); düşük ağırlık, sınırlı yükseklik, menzil, süre ve hız, otonom uçamama, yük taşıyamama ve gelişmiş elektronik cihaz bulunmaması ile ayırt edilir."],
        ["88.07 Açıklama Notu",
         "Aksam iki şartı sağlar: yalnız ve özellikle 88.01, 88.02 veya 88.06 taşıtlarıyla kullanılmaya uygun olmak ve Bölüm XVII notlarıyla hariç tutulmamış olmak. Örnekler: balon sepetleri, hava gemisi çerçeveleri ve pervaneleri; uçak gövdeleri, kanatlar ve kanat kirişleri, kontrol yüzeyleri, motor yerleri ve kapakları, tekerlekler, iniş takımları (frenleri dahil), deniz uçağı yüzdürücüleri, pervaneler ve helikopter rotorları, kontrol manivelaları, yedek yakıt tankları dahil yakıt tankları."],
    ],
    "sinir_komsulari": [
        ["Çocuk oyuncağı balon ve uçurtma", "95.03", "88.01 hariç tutması"],
        ["Yalnız eğlence amaçlı uçan oyuncak drone", "95.03", "Fasıl 88 Not 1"],
        ["Teşhir amaçlı uçak modeli; genel havacılık eğitimi için büyük jiroskop modeli", "90.23", "88.01, 88.02, 88.05 hariç tutmaları"],
        ["Dekorasyon amaçlı uçak maketi", "44.20 / 83.06", "88.01 ve 88.02 hariç tutmaları"],
        ["Balistik füze; askeri fırlatma aracı", "93.06", "88.02 hariç tutması"],
        ["Roket fırlatma rampası ve kulesi", "84.79", "88.05 hariç tutması"],
        ["Planörleri havalandıran motorlu vinç", "84.25", "88.05 hariç tutması"],
        ["Uçak motoru (turbojet, pistonlu motor)", "84.07–84.12", "Bölüm XVII Not 2(e)"],
        ["Pilot refleks test cihazı (rotatif kol üzerindeki hücre)", "90.19", "88.05 hariç tutması"],
        ["Motorlu taşıt şasisine monte uçuş simülatörü", "87.05", "88.05 Açıklama Notu"],
        ["Uçak ön lambası", "94.05", "Bölüm XVII Not 2(k)"],
        ["Uçak koltuğu", "94.01", "Daha belirli pozisyon"],
        ["Uçak hız göstergesi; uçak saati", "90.29 / Fasıl 91", "Bölüm XVII Not 2(g), (h)"],
        ["Uçağa ait elektrikli işaret cihazı; elektrikli buzlanma önleyici", "85.31 / 85.43", "Bölüm XVII Not 2(f)"],
        ["Gemi pervanesi (karşılaştırma)", "84.87", "Fasıl 89’da aksam hükmü yok; uçak pervanesi ise 88.07"],
    ],
    "tuzaklar": [
        "<b>Motorlu hava gemisi yine 88.01’dir.</b> Balon ve hava gemisi havadan hafiftir ve 88.01 motorla işleyen hava gemilerini de kapsar. Planörde ise motor (veya motor takılacak tasarım) 88.02’ye götürür.",
        "<b>Drone oyuncak mı, İHA mı?</b> Kalıcı entegre kamera, yük taşıma tasarımı veya faydacı işlev → 88.06; yalnız eğlence amaçlı, hafif, sınırlı yükseklik ve menzilli, otonom uçamayan, gelişmiş elektroniği olmayan uçan oyuncak → 95.03.",
        "<b>Uçurtma ve balon ikiye ayrılır.</b> Meteorolojik cihaz taşıyan uçurtma ve meteoroloji balonları 88.01; çocuk oyuncağı uçurtma ve balonlar 95.03.",
        "<b>7000 m/s sınırı.</b> Yüküne 7000 m/s’den fazla son hız veren uzay fırlatıcıları 88.02; yükünü bu hızı aşmadan parabolik yörüngede hedefe çarptıran balistik füzeler 93.06. Bilimsel yörünge-altı araçlar 88.02’de kalır.",
        "<b>88.03 boştur; aksam 88.07’dedir.</b> Pervane, rotor, iniş takımı, kanat ve gövde 88.07’de; paraşüt aksamı ise 88.04, simülatör aksamı 88.05 içindedir.",
        "<b>Delta kanat ≠ yamaç paraşütü.</b> Borulu metal iskelet üzerine gerilmiş üçgen kanatlı, kumanda çubuklu delta kanatlı planör 88.01; katlanabilen kanat, kablolar ve kemerden oluşan yamaç paraşütü 88.04.",
        "<b>Simülatörün yeri kaidesine bağlıdır.</b> Yerde uçuş eğitimi cihazı 88.05; motorlu taşıt şasisine monte ise 87.05, römorka monte ise 87.16. Refleks test cihazları 90.19.",
        "<b>Roket rampası ≠ uçak fırlatma tertibatı.</b> Gemi bordasındaki uçak fırlatma rampası 88.05; roket fırlatma rampaları ve kuleleri 84.79; planör vinci 84.25.",
        "<b>Uçak motoru 88.07 değildir.</b> Motorlar 84.07–84.12; ön lambalar 94.05; koltuklar 94.01; hız göstergeleri 90.29. Uçak pervanesi ise 88.07’dedir (gemi pervanesi 84.87).",
    ],
    "hafiza": {
        "kanca": "1 HAFİF – 2 MOTORLU – 4 DÜŞÜŞ – 5 YER – 6 PİLOTSUZ – 7 YEDEK",
        "aciklama": "88.01 <b>HAFİF</b> ve motorsuz (balon, hava gemisi, planör, uçurtma) · 88.02 <b>MOTORLU</b> (uçak, helikopter, uydu) · 88.04 <b>DÜŞÜŞ</b> (paraşüt) · 88.05 <b>YER</b> cihazları (fırlatma, durdurma, simülatör) · 88.06 <b>PİLOTSUZ</b> (İHA) · 88.07 <b>YEDEK</b> parça. 88.03 numarası boştur. Görsel benzetme: havaalanında gökyüzüne bakın; en yukarıda süzülen balon ve planör, altında jet ve helikopter, iniş pistinde durdurma kablosu, hangarda simülatör, kenarda vızıldayan drone, depoda pervane ve iniş takımları."
    },
    "sinav_odagi": [
        "Bu fasıl çıkmış sorularda az yer almıştır; doğrudan sorulan konu insansız hava taşıtlarıdır (drone), diğer sorularda 88.02, 88.04 ve 88.07 seçeneklerde çeldirici olarak kullanılmıştır.",
        "Dijital kamera ile donatılmış uzaktan kumandalı drone’ların 88.06’da sınıflandırıldığı; 85.25 (kamera-verici), 88.04, 88.05 ve 88.07 çeldiricileri.",
        "Taşımayla ilgili ama Fasıl 88 dışı eşya: teleferiklerin 84.28’de, elektromanyetik frenlerin 85.05’te sınıflandırıldığı sorularda 88.04 çeldirici olarak verilmiştir.",
        "Nakil vasıtalarına ait motorların Bölüm XVII’de değil Fasıl 84’te kaldığı (deniz taşıtı dizel motoru 84.08 sorusunda 88.02 çeldiricisi).",
        "Pozisyon numaralarının ve taşıt türlerinin karıştırılması: römorkör sorusunda 88.04, nakil vasıtası sorularında 88.02 gibi seçeneklerin yanıltıcı olarak kullanılması.",
    ],
    "cikmis_ornekler": [
        {
            "soru": "Tarife Cetveli’nde dijital kamera ile donatılmış uzaktan kumandalı “drone veya quadcopter” olarak tanımlanan insansız hava taşıtları hangi tarife pozisyonunda sınıflandırılabilir?",
            "secenekler": ["85.25", "88.04", "88.05", "88.06", "88.07"],
            "cevap": "D",
            "aciklama": "Fasıl 88 Not 1’e göre içinde pilot olmadan uçmak üzere tasarlanmış ve kalıcı entegre dijital kamerayla donatılabilen hava araçları insansız hava taşıtıdır ve 88.06’da sınıflandırılır. Kamera taşıması onu 85.25’e götürmez; 88.07 aksam, 88.04 paraşüt, 88.05 yer cihazları içindir.",
        },
    ],
    "ozet": [
        "Havadan hafif (balon, motorlu hava gemisi dahil) ve motorsuz havadan ağır (planör, delta kanat, uçurtma) → 88.01.",
        "Motorlu uçak, helikopter, motorlu planör, uydu, fırlatıcı, yörünge-altı araç → 88.02; balistik füze 93.06.",
        "İçinde pilot olmadan uçmak üzere tasarlanmış → 88.06; yalnız eğlence amaçlı uçan oyuncak → 95.03.",
        "Paraşüt ve aksamı 88.04; fırlatma, durdurma ve uçuş eğitim cihazları 88.05; taşıt aksamı 88.07 (88.03 boş).",
        "Motor 84.07–84.12, ön lamba 94.05, koltuk 94.01, aletler Fasıl 90: uçağa mahsus olsa da 88.07 değil.",
        "Kara taşıtı olarak da kullanılan hava taşıtı Fasıl 88’de kalır (Bölüm XVII Not 4).",
    ],
}

S = []

# --- Eşya → 4’lü pozisyon (5) ---
S.append(soru(
    "Tarife Cetveline göre, rüzgârın yön ve hızını tayin için kullanılan, normal ağırlığı 50–100 gram arasında olan meteorolojik pilot balonu hangi pozisyonda sınıflandırılır?",
    "88.01", ["95.03", "88.02", "88.06", "88.07"], "B", EP,
    "88.01 Açıklama Notu meteorolojide kullanılan sinyal, pilot ve irtifa balonlarını açıkça kapsar; pilot balonları rüzgâr yön ve hızını tayin eder ve normal ağırlıkları 50–100 gramdır. Oyuncak balonlar 95.03’tedir ancak bunlar aşağı kalite kauçuk, kısa şişirme emziği ve baskılarıyla ayırt edilir. 88.02 motorlu, havadan ağır hava taşıtları içindir.",
    "88.01 Açıklama Notu (I)(2)."))
S.append(soru(
    "Jet motorlu uçakları iniş sırasında yavaşlatmak için kullanılan kuyruk paraşütü hangi pozisyonda yer alır?",
    "88.04", ["88.07", "88.05", "88.02", "88.06"], "D", EP,
    "88.04 Açıklama Notu, bazı paraşüt tiplerinin jet motorlu uçakları yavaşlatmak için kuyruk paraşütü olarak kullanıldığını belirtir; paraşütler hangi amaçla kullanılırsa kullanılsın 88.04’tedir. Uçak aksamı olarak 88.07 veya iniş durdurma tertibatı olarak 88.05 düşünülmesi tuzaktır.",
    "88.04 Açıklama Notu."))
S.append(soru(
    "Uçak gemilerinde iniş anındaki uçağın hızını azaltarak durma mesafesini kısaltmaya yarayan durdurma tertibatı hangi pozisyonda sınıflandırılır?",
    "88.05", ["88.07", "84.25", "88.04", "89.06"], "A", EP,
    "88.05 hava taşıtlarının iniş cihaz ve tertibatını kapsar; Açıklama Notunun (B) bendi hava limanı, hangar ve uçak gemilerinde iniş hızını azaltan ve durma mesafesini kısaltan teçhizatı sayar. Uçağın kendi aksamı değildir (88.07); uçak gemisi ise 89.06 savaş gemisidir, tertibat ayrıca sınıflandırılır.",
    "88.05 pozisyon metni ve Açıklama Notu (B)."))
S.append(soru(
    "Bir helikoptere ait ana rotor hangi pozisyonda sınıflandırılır?",
    "88.07", ["84.11", "88.02", "84.12", "84.87"], "E", EP,
    "88.07 Açıklama Notu uçak ve helikopter pervanelerini, pervane kanatlarını ve yükselme kontrol mekanizmalarını aksam olarak sayar; pozisyonun alt ayrımı da “pervaneler ve rotorlar”dır. Motorlar (84.11, 84.12) Bölüm XVII Not 2 ile dışarıda kalır; gemi pervaneleri 84.87’dedir, ancak hava taşıtı rotoru 88.07’de kalır.",
    "88.07 Açıklama Notu (II)(7); Bölüm XVII Not 2(e)."))
S.append(soru(
    "Yörüngeye yerleştirilmek üzere ithal edilen telekomünikasyon uydusu hangi pozisyonda yer alır?",
    "88.02", ["88.06", "85.25", "93.06", "88.01"], "C", EP,
    "88.02 atmosferin dışına yolculuk yapabilen uzay araçlarını (telekomünikasyon ve meteoroloji uyduları dahil) kapsar. Uydunun verici cihaz taşıması onu 85.25’e götürmez; bütün olarak uzay aracıdır. 93.06 askeri fırlatma araçları ve balistik füzeler, 88.06 pilotsuz hava taşıtları içindir.",
    "88.02 pozisyon metni ve Açıklama Notu (2)."))

# --- Olumsuz teşhis (4) ---
S.append(soru(
    "Aşağıdakilerden hangisi 88.01 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Motor takılmak üzere dizayn edilmiş planör",
    ["Bir kabloyla yere bağlanan bağımlı balon", "Motorla işleyen hava gemisi", "Delta kanatlı planör", "Meteorolojik cihaz taşıyan, iple yere bağlı uçurtma"],
    "A", OT,
    "88.01 Açıklama Notuna göre motorla donatılmış veya motorla donatılmak için dizayn edilmiş planörler 88.02’dedir. Bağımlı balonlar ve motorla işleyen hava gemileri havadan hafif taşıt olarak, delta kanatlı planörler ve meteorolojik uçurtmalar motorsuz taşıt olarak 88.01’dedir.",
    "88.01 Açıklama Notu (I), (II), (III)."))
S.append(soru(
    "Aşağıdakilerden hangisi uçağa mahsus olsa bile 88.07 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Uçağın turbojet motoru",
    ["Uçak kanadı ana kirişi", "Geri çekilebilir iniş takımı", "Deniz uçağının su üzerinde yüzen şamandırası", "Yedek yakıt tankı"],
    "D", OT,
    "Bölüm XVII Not 2(e) 84.01–84.79 makinelerini, Bölüm Genel Açıklamaları da her çeşit araç motorlarını (84.07–84.12) aksam tabirinin dışında bırakır. Kanat kirişleri, iniş takımları, deniz uçağı yüzdürücüleri ve yakıt tankları 88.07 Açıklama Notunda sayılmıştır.",
    "Bölüm XVII Not 2(e); 88.07 Açıklama Notu."))
S.append(soru(
    "Aşağıdakilerden hangisi Tarife Cetvelinin 88. faslında <b>yer almaz</b>?",
    "Pilot reaksiyonlarını kaydeden refleks test cihazı",
    ["Hava muharebe simülatörü", "Paraşüt çantası", "Dağ yamacından atlamak için yamaç paraşütü", "Meteorolojide kullanılan rotoşüt"],
    "E", OT,
    "88.05 Açıklama Notu, başlıca rolü insanın zor uçuş şartlarındaki reaksiyonlarını kaydetmek olan cihazları (rotatif kol üzerindeki hücreler gibi) psikoteknik refleks test cihazı sayarak 90.19’a gönderir. Hava muharebe simülatörü 88.05’te, paraşüt çantası, yamaç paraşütü ve rotoşüt 88.04’tedir.",
    "88.05 Açıklama Notu, hariç tutmalar; 88.04 Açıklama Notu."))
S.append(soru(
    "Aşağıdakilerden hangisi 88.02 pozisyonunda <b>sınıflandırılmaz</b>?",
    "Askeri balistik füze",
    ["Hem suya hem karaya inebilen uçak", "Helikopter", "Bilimsel amaçlı yörünge-altı fırlatıcı araç", "Uydu fırlatan uzay aracı fırlatıcısı"],
    "B", OT,
    "88.02 Açıklama Notu, yüklerine 7000 m/s’yi aşmayan sürat vererek parabolik yörünge sonunda hedefe çarptıran askeri fırlatma araçlarını ve balistik füzeleri hariç tutar (93.06). Amfibi uçaklar, helikopterler, bilimsel yörünge-altı araçlar ve uzay fırlatıcıları 88.02’de sayılmıştır.",
    "88.02 Açıklama Notu (1), (3), (4) ve hariç tutmalar."))

# --- Farklı/aynı pozisyon veya fasıl (4) ---
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda yer alır?",
    "Uçak iniş takımının freni",
    ["Paraşüt koşum takımı", "Paraşütün açılmasını sağlayan mekanik yaylı sistem", "Paraşüt çantası", "Kılavuz paraşüt"],
    "C", FA,
    "İniş takımları ve bunların frenleri hava taşıtı aksamı olarak 88.07’dedir. Paraşüt koşum takımı, mekanik yaylı açma sistemi, paraşüt çantası ve kılavuz paraşüt 88.04 Açıklama Notunda paraşütün aksam, parça ve teferruatı olarak sayılmıştır; paraşüt aksamı 88.07’ye değil 88.04’e gider.",
    "88.04 ve 88.07 Açıklama Notları."))
S.append(soru(
    "Aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
    "Çocuk oyuncağı uçurtma",
    ["Deniz uçağı", "Sinyal balonu", "Kalıcı entegre kameralı drone", "Uçuş simülatörü"],
    "E", FA,
    "88.01 Açıklama Notu çocuk oyuncağı olarak düzenlenen uçurtmaları hariç tutar; bunlar 95.03’te, yani Fasıl 95’tedir. Deniz uçağı 88.02, sinyal balonu 88.01, kameralı drone 88.06, uçuş simülatörü 88.05 ile Fasıl 88’dedir.",
    "88.01 Açıklama Notu (III); Fasıl 88 Not 1."))
S.append(soru(
    "Aşağıdaki eşya çiftlerinden hangisinde her iki eşya da aynı pozisyonda sınıflandırılır?",
    "Planör – Delta kanatlı planör",
    ["Helikopter – İçinde pilot olmadan uçmak üzere tasarlanmış helikopter", "Paraşüt – Uçak pervanesi", "Uçak fırlatma rampası – Roket fırlatma rampası", "Hava gemisi – Uçak"],
    "A", FA,
    "Planörler ve delta kanatlı planörler motorsuz hava taşıtları olarak 88.01’dedir. Helikopter 88.02, pilotsuz helikopter 88.06; paraşüt 88.04, pervane 88.07; uçak fırlatma rampası 88.05, roket rampası 84.79; hava gemisi 88.01, uçak 88.02’dir.",
    "88.01, 88.02, 88.04–88.07 Açıklama Notları."))
S.append(soru(
    "Uçaklarda kullanılan aşağıdaki eşyadan hangisi diğerlerinden farklı bir fasılda yer alır?",
    "Uçak koltuğu",
    ["Uçak tekerleği", "Uçak gövdesi bölümü", "Helikopter pervanesi", "Uçak kontrol kolu"],
    "D", FA,
    "Bölüm XVII Genel Açıklamaları nakil vasıtaları için koltukları daha belirli olarak yer aldıkları 94.01’e gönderir. Tekerlekler, gövde bölümleri, pervaneler ve kontrol manivelaları 88.07 Açıklama Notunda hava taşıtı aksamı olarak sayılmıştır.",
    "Bölüm XVII Genel Açıklamalar (III)(C); 88.07 Açıklama Notu."))

# --- Fasıl notu · Tanım/Eşik (4) ---
S.append(soru(
    "Fasıl 88 Not 1’e göre “insansız hava taşıtı” tabiri hakkında aşağıdakilerden hangisi <b>doğrudur</b>?",
    "88.01 dışında, içinde pilot olmadan uçmak üzere tasarlanmış her hava aracıdır.",
    ["Yalnız uzaktan kumandayla uçan ve kamera taşıyan hava araçlarını kapsar.",
     "88.01’deki balon ve planörlerin pilotsuz olanlarını da kapsar.",
     "Yalnızca eğlence amacıyla tasarlanmış uçan oyuncakları da kapsar.",
     "Yük taşıyacak şekilde tasarlanan hava araçları bu tanıma girmez."],
    "B", TN,
    "Not 1, 88.01’dekiler dışında içinde pilot olmadan uçmak üzere tasarlanmış her hava aracını insansız hava taşıtı sayar; bunlar yük taşıyacak şekilde tasarlanabilir veya kamera gibi ekipmanla donatılabilir. Kamera zorunlu değildir; programlı uçuş yeteneği de olabilir. Yalnız eğlence amaçlı uçan oyuncaklar tanım dışındadır (95.03).",
    "Fasıl 88 Not 1; 88.06 Açıklama Notu."))
S.append(soru(
    "88.06 Açıklama Notuna göre yalnız eğlence amaçlı uçan oyuncakları insansız hava taşıtlarından ayırt etmeye yarayan ölçütler arasında aşağıdakilerden hangisi <b>yer almaz</b>?",
    "Pervane veya rotor sayısı",
    ["Düşük ağırlık", "Sınırlı uçuş yüksekliği ve mesafesi", "Otonom olarak uçamama", "Yük veya kargo taşıyamama"],
    "C", TN,
    "88.06 Açıklama Notu uçan oyuncakları düşük ağırlık, sınırlı yükseklik, mesafe, süre ve hız, otonom uçamama, yük taşıyamama ve gelişmiş elektronik cihaz (konumlandırma, gece görüşü) bulunmaması ile ayırt eder. Pervane veya rotor sayısı bir ölçüt değildir; İHA’lar çeşitli şekil ve boyutta olabilir.",
    "88.06 Açıklama Notu; Fasıl 88 Not 1."))
S.append(soru(
    "88.02 Açıklama Notuna göre uzay aracını fırlatıcı araçları, askeri fırlatma araçlarından ve balistik füzelerden ayıran ölçüt hangisidir?",
    "Yüklerine 7000 m/s’den fazla son sürat vermeleri",
    ["Yüklerine 7000 m/s’den az son sürat vermeleri", "Yalnız sivil kurumlarca kullanılmaları", "Yüklerini paraşütle yeryüzüne geri döndürmeleri", "Atmosfer içinde kalan bir yörünge izlemeleri"],
    "E", TN,
    "88.02 Açıklama Notu uzay aracı fırlatıcılarının yüklerine fırlatış sonunda 7000 m/s’den fazla son hız verdiğini belirtir; yüklerini 7000 m/s’yi aşmayan hızla parabolik yörüngede hedefe çarptıran askeri araçlar ve balistik füzeler 93.06’dadır. Yükü paraşütle geri döndürmek bilimsel yörünge-altı araçların özelliğidir ve onlar da 88.02’dedir.",
    "88.02 Açıklama Notu (3), (4) ve hariç tutmalar."))
S.append(soru(
    "88.01 Açıklama Notuna göre meteorolojide kullanılan balonlar ile 95.03’teki çocuk oyuncağı balonlar arasındaki fark hangi seçenekte doğru verilmiştir?",
    "Oyuncak balonlar daha aşağı kalite kauçuktan, kısa şişirme emzikli ve baskılıdır.",
    ["Meteoroloji balonları plastik yapraktan, oyuncak balonlar kauçuktan yapılır.",
     "Ağırlığı 100 gramı geçen balonlar daima 95.03’te sınıflandırılır.",
     "Oyuncak balonların şişirme emzikleri meteoroloji balonlarınınkinden daha uzundur.",
     "Üzerinde baskı bulunan balonlar meteoroloji balonu sayılır."],
    "A", TN,
    "Açıklama Notu meteoroloji balonlarının genellikle çok ince, şişirmeye son derece elverişli kauçuktan yapıldığını; oyuncak balonların ise aşağı kalitede kauçuktan yapılmaları, şişirme emziklerinin daha kısa olması ve reklam veya dekoratif baskılar taşımalarıyla ayırt edildiğini belirtir. Sinyal balonları 4500 grama kadar çıkabildiğinden ağırlık ölçütü yanlıştır.",
    "88.01 Açıklama Notu (I)."))

# --- Genel Yorum Kuralı (2) ---
S.append(soru(
    "Motorları takılmamış ve iç teçhizatı yapılmamış, ancak tamamlanmış uçağın asli özelliklerine sahip yolcu uçağı hangi pozisyonda ve hangi Genel Yorum Kuralları uyarınca sınıflandırılır?",
    "88.02 – GYK 1, 2(a) ve 6",
    ["88.07 – GYK 1 ve 6", "88.02 – GYK 3(b) ve 6", "88.07 – GYK 2(a) ve 6", "88.06 – GYK 1, 2(a) ve 6"],
    "C", GY,
    "Fasıl 88 Genel Açıklamaları, motorlarla donatılmamış veya iç teçhizatı olmayan uçakların tamamlanmış özelliklerine sahip olmaları şartıyla eksiksiz uçaklar gibi sınıflandırılacağını belirtir; bu GYK 2(a)’nın uygulamasıdır, alt pozisyon GYK 6 ile belirlenir. Eksik uçak aksam (88.07) sayılmaz; pilotlu yolcu uçağı olduğundan 88.06 da değildir.",
    "GYK 1, 2(a) ve 6; Fasıl 88 Genel Açıklamalar."))
S.append(soru(
    "Kanatları, boru iskeleti ve kumanda çubuğu aynı ambalajda monte edilmemiş halde birlikte sunulan delta kanatlı planör hangi pozisyonda ve hangi Genel Yorum Kuralları uyarınca sınıflandırılır?",
    "88.01 – GYK 1 ve 2(a)",
    ["88.07 – GYK 1", "88.01 – GYK 3(b)", "88.04 – GYK 1 ve 2(a)", "88.07 – GYK 2(a)"],
    "E", GY,
    "GYK 2(a) monte edilmemiş veya sökülmüş halde sunulan eşyayı tamamlanmış eşya gibi sınıflandırır; delta kanatlı planör 88.01 pozisyon metninde açıkça sayılmıştır. Parçaların birlikte sunulması onları tek tek aksam (88.07) yapmaz. 88.04 yamaç paraşütlerini kapsar; delta kanat ise planördür.",
    "GYK 1 ve 2(a); 88.01 pozisyon metni ve Açıklama Notu (II)."))

# --- Eşleştirme / Boşluk doldurma (2) ---
S.append(soru(
    "Aşağıdaki eşya ile pozisyonların doğru eşleştirmesi hangi seçenekte verilmiştir?<br/>I. Meteorolojide iniş roketlerini kontrol eden rotoşüt<br/>II. Pilot kabini olarak teçhiz edilmiş, mesnet üzerinde dönen küçük kabinli “link trainer”<br/>III. Radyo verici cihazlarını yükseğe taşıyan sinyal balonu<br/>IV. Uçak gövde ve tekne bölümleri<br/>a) 88.07 · b) 88.01 · c) 88.04 · d) 88.05",
    "I-c, II-d, III-b, IV-a",
    ["I-d, II-c, III-b, IV-a", "I-c, II-d, III-a, IV-b", "I-c, II-a, III-b, IV-d", "I-b, II-d, III-c, IV-a"],
    "B", ES,
    "Rotoşütler 88.04’te, “link trainer” yerde uçuş eğitimi cihazı olarak 88.05’te, sinyal balonu meteoroloji balonu olarak 88.01’de, uçak gövde ve tekne bölümleri aksam olarak 88.07’dedir. Rotoşütü dönen kanadı nedeniyle 88.05 veya 88.07 sanmak tipik hatadır.",
    "88.01, 88.04, 88.05, 88.07 Açıklama Notları."))
S.append(soru(
    "Bölüm XVII Not 4’e göre aynı zamanda kara taşıtı olarak da kullanılabilecek şekilde özel olarak imal edilmiş hava taşıtları ..... pozisyonunda; Fasıl 88 Not 1’e göre ise yalnızca eğlence amacıyla tasarlanmış uçan oyuncaklar ..... pozisyonunda sınıflandırılır. Boşluklara sırasıyla gelmesi gerekenler hangisidir?",
    "88.02 – 95.03",
    ["87.03 – 95.03", "88.02 – 88.06", "87.03 – 88.06", "88.06 – 95.03"],
    "D", ES,
    "Bölüm XVII Not 4 bu taşıtları Fasıl 88’e gönderir ve 88.02 Açıklama Notu kara nakil vasıtası olarak kullanılabilmek için özel imal edilmiş hava taşıtlarını açıkça kapsar. Not 1 yalnız eğlence amaçlı uçan oyuncakları insansız hava taşıtı tabirinin dışında bırakıp 95.03’e yönlendirir.",
    "Bölüm XVII Not 4; Fasıl 88 Not 1; 88.02 Açıklama Notu (1)."))

# --- Çoktan-çoğa (2) ---
S.append(soru(
    "Aşağıdakilerden hangileri 88.05 pozisyonunda yer alır?<br/>I. Gemilerin bordasında kullanılan ve uçağın ilk hareketini sağlayan metal fırlatma rampası<br/>II. Planörlerin havalandırılmasında kullanılan motorlu vinç teçhizatı<br/>III. Pilotları eğitmeye mahsus hava muharebe simülatörü<br/>IV. Roket fırlatma kulesi",
    "I ve III",
    ["I, II ve III", "II ve IV", "I, III ve IV", "Yalnız III"],
    "A", CC,
    "88.05 uçak fırlatma tertibatını (gemi bordasındaki rampalar) ve yerde uçuş eğitimi cihazlarını (hava muharebe simülatörleri dahil) kapsar. Planörleri havalandıran motorlu vinçler 84.25’te, roket fırlatma rampaları ve kuleleri 84.79’dadır.",
    "88.05 Açıklama Notu (A) ve (C), hariç tutmalar."))
S.append(soru(
    "Aşağıdakilerden hangileri 88.04 pozisyonunda sınıflandırılır?<br/>I. Meteorolojik aletler için kullanılan paraşüt<br/>II. Yaylı kanca ve tokalarla donatılmış paraşüt koşum takımı<br/>III. Meteorolojide iniş roketlerini kontrol eden dönen kanat üniteli rotoşüt<br/>IV. Geri çekip alma teçhizatlı uçak iniş takımı",
    "I, II ve III",
    ["I ve II", "II ve IV", "I, III ve IV", "III ve IV"],
    "C", CC,
    "88.04 her amaçla kullanılan paraşütleri, rotoşütleri ve bunların aksam, parça ve teferruatını (koşum takımları dahil) kapsar. Uçak iniş takımı ise 88.07 Açıklama Notunda hava taşıtı aksamı olarak sayılmıştır.",
    "88.04 ve 88.07 Açıklama Notları."))

# --- Senaryo (2) ---
S.append(soru(
    "Bir tarım işletmesi; içinde pilot bulunmayan, uydu navigasyon alıcısı sayesinde operatör müdahalesi olmadan programlanmış rotada uçabilen, tarlalara ilaç püskürtmek için kalıcı olarak entegre edilmiş püskürtme ekipmanı ve 20 litrelik deposu bulunan çok rotorlu bir hava aracı ithal etmektedir. Eşya hangi pozisyonda sınıflandırılır?",
    "88.06",
    ["84.24", "88.02", "95.03", "88.07"],
    "D", SN,
    "Fasıl 88 Not 1’e göre içinde pilot olmadan uçmak üzere tasarlanmış ve faydacı işlev için kalıcı entegre ekipmanla donatılmış hava araçları insansız hava taşıtıdır; 88.06 Açıklama Notu tarımsal çalışmayı ve programlanmış uçuşu açıkça sayar. Püskürtme ekipmanı taşıması onu 84.24’e götürmez; pilotlu olmadığı için 88.02 değildir.",
    "Fasıl 88 Not 1; 88.06 Açıklama Notu."))
S.append(soru(
    "Atmosfer akımlarını kullanarak havada kalan, motoru bulunmayan, kumaş kanadı boru şeklindeki metal yapı üzerine gerilmiş, üçgen kanatları ve yatay kumanda çubuğu ile koşum takımına bağlı tek kişi tarafından yönetilen hava aracı hangi pozisyonda yer alır?",
    "88.01",
    ["88.04", "88.02", "95.06", "88.07"],
    "B", SN,
    "Tarif edilen araç delta kanatlı planördür; 88.01 Açıklama Notu bunları borulu metal yapı üzerine gerilmiş kumaş kanat ve yatay kumanda çubuğuyla tanımlar ve motorsuz hava taşıtı olarak 88.01’e verir. Katlanabilen kanat ve kablolardan oluşan yamaç paraşütü 88.04’tedir; motorlu olsaydı 88.02’ye giderdi.",
    "88.01 Açıklama Notu (II); 88.04 Açıklama Notu."))

obj["sorular"] = S
yaz(obj)
