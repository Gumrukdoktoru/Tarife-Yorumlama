#!/usr/bin/env python3
"""Hap bilgi sayfaları – Grup H6: Fasıl 64–83 (Bölüm XII–XV)."""
import json
import os
import re

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KITAP, "hap")

H = {}

# ------------------------------------------------------------------ 64
H[64] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 3 kez ana konu: ortopedik ayakkabının 90.21’e gitmesi (güreş, bisiklet, kar sörfü, "
            "koşu ayakkabısı 64’te), ayakkabının VIII. değil XII. Bölümde olması ve 64.06’da topuk rampası varken "
            "çivi, kopça, toka, bağın yer almaması. Ayakkabıyla ilgili ürünlerin 34.05, 44.17, 68.12, 96.05’te "
            "olduğu da seçeneklerde kullanıldı.",
    pozisyonlar=[
        ["64.01", "Su geçirmez, kauçuk/plastik; yüz dikişsiz, perçinsiz, vidasız"],
        ["64.02", "Diğer kauçuk/plastik taban ve yüzlü ayakkabılar"],
        ["64.03", "Yüzü deri; taban kauçuk, plastik, deri"],
        ["64.04", "Yüzü dokumaya elverişli madde; aynı tabanlar"],
        ["64.05", "Diğer: ağaç, mantar, ip, keçe taban"],
        ["64.06", "Aksam, iç taban, topuk rampası, getr, tozluk"],
    ],
    hap=[
        "<b>Belirleyici iki madde:</b> dış taban (topuk hariç yere temas eden en büyük yüzey) ve yüz (dış yüzeyin "
        "en büyük parçası); astar, süs, aksesuar ve takviyeler dikkate alınmaz (Not 4).",
        "<b>Not 1 – fasıl dışı:</b> tabansız kullan-at örtü (maddesine göre), dış tabanı tutturulmamış tekstil "
        "(XI. Bölüm), balyalı kullanılmış (63.09), amyant (68.12), ortopedik (90.21), oyuncak ve paten takılı "
        "bot (Fasıl 95).",
        "<b>Not 2 – 64.06 aksamı değil:</b> ayakkabı çivisi ve demiri, kopça, toka, bağ, bağ deliği kapsülü, "
        "ponpon, düğme (96.06), fermuar (96.07); topuk, iç taban ve topuk rampası ise 64.06.",
        "<b>Spor ayakkabısı 64’te kalır:</b> güreş, koşu, bisiklet, kayak, kar sörfü ayakkabısı 64; buz veya "
        "tekerlekli paten takılı olanlar 95.06; ortopedik ayakkabı 90.21.",
        "<b>Tanımlar (Not 3):</b> dış yüzü gözle görülür kauçuk/plastik kaplı mensucat “kauçuk/plastik” sayılır; "
        "“deri” yalnız 41.07 ve 41.12–41.14, terkip deri (41.15) deri sayılmaz.",
    ],
    karistirilan=[
        ["Ortopedik ayakkabı", "90.21", "Not 1(e); spor ayakkabıları ise 64’te"],
        ["Deri yüzlü ayakkabı (bölüm sorusu)", "64.03", "XII. Bölüm; kürk, kösele, çanta VIII. Bölüm"],
        ["Amyanttan ayakkabı", "68.12", "Not 1(d); ayakkabı boyası 34.05, ahşap kalıp 44.17"],
    ],
)

# ------------------------------------------------------------------ 65
H[65] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; seçeneklerde plastik madenci başlığı (65.06, sıralama sorusu) ve "
            "mantardan şapka siperliği (başlık aksamı, Fasıl 45 değil) çeldirici olarak yer aldı.",
    pozisyonlar=[
        ["65.01", "Keçe şapka taslakları, diskler, üstüvaneler (şekilsiz)"],
        ["65.05", "Örme veya mensucattan şapkalar; her maddeden saç filesi"],
        ["65.06", "Koruyucu başlıklar; kauçuk, plastik, deri, kürk, metal"],
        ["65.07", "İç şerit, astar, kasnak, siperlik, çene kayışı"],
    ],
    hap=[
        "<b>Madde ve amaç önemsiz:</b> şerit/örgü şapka 65.04, örme-keçe-mensucat 65.05; diğerleri ve tüm "
        "koruyucu başlıklar (spor kaskı, mikrofonlu veya kulaklıklı olanlar dahil) 65.06; 65.03 boştur.",
        "<b>Not 1 – fasıl dışı:</b> balyalı kullanılmış başlık 63.09, amyant başlık 68.12, oyuncak bebek ve "
        "karnaval şapkası Fasıl 95; ayrıca hayvan başlığı 42.01, peruk 67.04.",
    ],
    karistirilan=[
        ["Mantardan şapka siperliği", "65.07", "Başlık aksamı; Fasıl 45 başlıkları hariç tutar"],
        ["Bisiklet veya motosiklet kaskı", "65.06", "Koruyucu başlık; Fasıl 95 spor eşyası değil"],
    ],
)

# ------------------------------------------------------------------ 66
H[66] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez: “hangisi farklı pozisyonda” kalıbıyla şemsiyenin (66.01) baston, iskemle "
            "baston, kamçı ve kırbaçtan (66.02) ayrılması; ayrıca baston ve şemsiyenin maddesine göre "
            "sınıflandırılmadığı (tabak ise maddesine göre) soruldu.",
    pozisyonlar=[
        ["66.01", "Her tür şemsiye; baston şemsiye, bahçe şemsiyesi"],
        ["66.02", "Baston, iskemle baston, kamçı, kırbaç (her maddeden)"],
        ["66.03", "Aksam: kulp, çerçeve, mil; tekstil, kılıf hariç"],
    ],
    hap=[
        "<b>Madde önemsiz:</b> altın kulplu baston, fildişi saplı şemsiye, deri kamçı da Fasıl 66’dadır; baston "
        "görünüşlü kın içindeki baston şemsiye 66.01’dir.",
        "<b>Not 1 – fasıl dışı:</b> ölçü gösteren baston 90.17, kılıçlı, tüfekli, kurşunlu baston Fasıl 93, "
        "oyuncak şemsiye Fasıl 95.",
        "<b>Not 2:</b> tekstil aksam ile her maddeden kın, kılıf, püskül 66.03’e girmez; şemsiyeyle birlikte "
        "gelse de takılı değilse ayrı sınıflandırılır.",
    ],
    karistirilan=[
        ["Koltuk değneği, ortopedik baston", "90.21", "Yaşlı ve sakatlar için mutat baston ise 66.02"],
        ["Golf sopası, kayak değneği", "95.06", "Spor eşyası; baston değil"],
    ],
)

# ------------------------------------------------------------------ 67
H[67] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; ham tüy-saç (Fasıl 5) ile "
            "işlenmiş hali (67) ayrımı ve peruğun 67.04’te olduğu bilinmeli.",
    pozisyonlar=[
        ["67.01", "İşlenmiş kuş tüyü ve tüyden eşya, yelpaze"],
        ["67.02", "Yapma çiçek, yaprak, meyve (parçalar birleştirilmiş)"],
        ["67.03", "Hazırlanmış insan saçı; peruk için yün, kıl"],
        ["67.04", "Peruk, takma sakal, kaş, kirpik; saç eşyası"],
    ],
    hap=[
        "<b>Fasıl 5 / 67 sınırı:</b> yalnız temizlenmiş tüy 05.05, yalnız yıkanmış saç 05.01; ağartılmış, boyanmış, "
        "kıvrılmış tüy 67.01; kök-uç dizilmiş, ağartılmış, boyanmış saç 67.03.",
        "<b>Yapma çiçek (Not 3):</b> parçalar bağlama, yapıştırma, geçirme ile birleştirilmişse 67.02; camdan "
        "olanlar Fasıl 70; tek parça dökülmüş, oyulmuş seramik, taş, metal çiçek maddesine göre.",
        "<b>Not 1 – fasıl dışı:</b> saç filesi ve başlık Fasıl 65, ayakkabı 64, oyuncak ve karnaval eşyası 95, "
        "tüy süpürge ve pudra ponponu 96, insan saçından tasir torbası 59.11.",
    ],
    karistirilan=[
        ["Kaz tüyü dolgulu yastık, yorgan", "94.04", "Not 2(a): tüy yalnız dolgu maddesi"],
        ["İnsan saçından saç filesi", "65.05", "Not 1(d); peruk değil, başlık faslı"],
    ],
)

# ------------------------------------------------------------------ 68
H[68] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; seçeneklerde 3 kez yer aldı: dişçilik alçısının 68.09 değil 25.20 "
            "olduğu, 68.13 (balata) pozisyonunun otomobille, 68.12 (amyant ayakkabı) pozisyonunun ayakkabıyla "
            "ilgili olduğu.",
    pozisyonlar=[
        ["68.02", "İşlenmiş yontu ve inşaat taşı; mozaik küp"],
        ["68.04", "Çerçevesiz değirmen, bileği taşı, taşlama diski"],
        ["68.12", "İşlenmiş amyant ve amyanttan giysi, ayakkabı"],
        ["68.13", "Monte edilmemiş sürtünme malzemesi: balata, debriyaj diski"],
    ],
    hap=[
        "<b>Fasıl 25–68–69–70 sınırı:</b> ham, kabaca yontulmuş veya yalnız dikdörtgen kesilmiş taş 25; daha "
        "ileri işlenmiş taş ve mineral eşya 68; pişirilmiş toprak 69; cam 70.",
        "<b>Bağlayıcıya göre:</b> asfalt 68.07, talaş + mineral bağlayıcı pano 68.08, alçı 68.09, beton ve suni "
        "taş 68.10, lif takviyeli çimento 68.11; taş ve cüruf yünü 68.06.",
        "<b>Amyant ve balata:</b> amyant eşyası 68.12; takılmamış balata 68.13, metal tabakaya takılı balata "
        "taşıt aksamı; el veya pedalla çalışan çatkılı bileği 82.05.",
    ],
    karistirilan=[
        ["Dişçilikte kullanılan alçı", "25.20", "Madde olarak Fasıl 25; alçıdan eşya 68.09"],
        ["Cam yünü", "70.19", "Mineral yün (taş, cüruf yünü) ise 68.06"],
    ],
)

# ------------------------------------------------------------------ 69
H[69] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; “maddesine göre sınıflandırılan eşya” sorusunda doğru cevap "
            "tabaktı (porselen 69.11, diğer seramik 69.12; şemsiye ve baston maddeden bağımsız).",
    pozisyonlar=[
        ["69.02", "Ateşe dayanıklı tuğla, karo, inşaat eşyası"],
        ["69.07", "Döşeme ve kaplama karosu, mozaik küp"],
        ["69.10", "Lavabo, küvet, klozet (sabit tesisata bağlı)"],
        ["69.11", "Porselen/çini sofra-mutfak eşyası; diğer seramikten 69.12"],
    ],
    hap=[
        "<b>Not 1:</b> yalnız şekil verildikten sonra pişirilmiş seramik; 800 °C’nin altında ısıtılan ürün "
        "pişirilmiş sayılmaz (Fasıl 68). Tamamen camlaşan eşya ve cam-seramik Fasıl 70.",
        "<b>Tür esastır, madde değil:</b> porselen ya da gre lavabo aynı 69.10; madde ayrımı yalnız sofra, "
        "mutfak, ev, tuvalet eşyasında: porselen/çini 69.11, taklit porselen dahil diğer seramik 69.12.",
        "<b>Not 2 – fasıl dışı:</b> seramik aşındırıcı 68.04, taklit mücevher 71.17, izolatör 85.46, takma diş "
        "90.21, saat, mobilya-lamba, oyuncak, düğme 96.06, pipo 96.14.",
    ],
    karistirilan=[
        ["Seramik elektrik izolatörü", "85.46", "Not 2(f); teknik seramik eşya 69.09 değil"],
        ["Seramik gövdeli masa lambası", "94.05", "Not 2(ij); süs eşyası 69.13 değil"],
    ],
)

# ------------------------------------------------------------------ 70
H[70] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 kez ana konu: ısıtma tertibatlı taşıt camının çerçevesiz olsa da 70 dışı kalması "
            "(Not 1(e); tertibatsız ön cam, ayna, far camı, cam tülü 70’te) ve taşıt far-stop camının 87 değil "
            "70.14 olduğu. Cam (70), dikiz aynası (70.09) ve cam bardak başka sorularda seçenekti.",
    pozisyonlar=[
        ["70.07", "Emniyet camı: yalnız temperli veya lamine"],
        ["70.09", "Cam aynalar; taşıt dikiz aynası dahil"],
        ["70.10", "Ticari taşıma-ambalaj şişe, kavanoz, damacana"],
        ["70.13", "Sofra, mutfak, tuvalet, büro, süs cam eşyası"],
        ["70.14", "Optik işlenmemiş sinyal camı; far, stop camı"],
        ["70.19", "Cam lifi, cam yünü, cam tülü"],
    ],
    hap=[
        "<b>Not 1(d)–(e):</b> 86–88. fasıl taşıtlarının çerçeveli camları ile ısıtma tertibatlı veya "
        "elektrikli/elektronik cihaz içeren camları (çerçevesiz olsa da) 70 dışıdır; tertibatsız çerçevesiz "
        "cam 70’te kalır.",
        "<b>Diğer dışlamalar (Not 1):</b> cam tozu-firit 32.07, taklit mücevher Fasıl 71, optik işlenmiş eleman "
        "ve termometre Fasıl 90, lamba ve parçaları 94.05, oyuncak 95, düğme, termos, parfüm spreyi 96.",
        "<b>Düz cam:</b> dökme-haddeleme 70.03, çekme-üfleme 70.04, float veya parlatılmış 70.05; bombeli, kenarı "
        "işlenmiş, delinmiş, emayeli 70.06. Kesme ve tavlama öncesi işlem işleme sayılmaz (Not 2).",
        "<b>Eşikler:</b> eritilmiş kuvars her yerde camdır (Not 5). Cam yünü (Not 4): silis ≥ %60; ya da daha az "
        "silisle alkali oksit %5’ten veya borik oksit %2’den fazla; değilse 68.06.",
        "<b>Kapta amaç:</b> ticari ambalaj 70.10, sofra-mutfak-süs 70.13, laboratuvar-eczane 70.17, teşhir "
        "kavanozu 70.20; boncuk, taklit inci, oyuncak bebek gözü, 1 mm’den küçük kürecik 70.18.",
    ],
    karistirilan=[
        ["Isıtmalı lokomotif ön camı (çerçevesiz)", "86.07", "Not 1(e): tertibat varsa çerçevesiz de 70 dışı"],
        ["Motorlu taşıt far ve stop camı", "70.14", "87 değil; optik işlenmemiş sinyal camı"],
        ["Abajur ve avize camı", "94.05", "Not 1(g): lamba parçası"],
    ],
)

# ------------------------------------------------------------------ 71
H[71] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 3 kez, hep aynı kalıp: “hangisi platin tabirine girmez?” – cevap berilyum veya "
            "kadmiyum (adi metal); osmiyum, iridyum, paladyum, rodyum platin sayılır (Not 4).",
    pozisyonlar=[
        ["71.02", "Elmaslar (monte edilmemiş, mıhlanmamış)"],
        ["71.04", "Sentetik veya terkip taşlar; kübik zirkonya dahil"],
        ["71.10", "Platin grubu metaller (işlenmemiş, yarı işlenmiş, pudra)"],
        ["71.13", "Mücevherci eşyası: yüzük, kolye, broş, tesbih"],
        ["71.14", "Kuyumcu eşyası: sofra, tuvalet, büro, dini eşya"],
        ["71.17", "Taklit mücevher: inci, taş, kıymetli metal içermeyen"],
    ],
    hap=[
        "<b>Not 4:</b> kıymetli metal = gümüş, altın, platin. “Platin” = platin, iridyum, osmiyum, paladyum, "
        "rodyum, rutenyum. Berilyum, kadmiyum, kobalt, tantal adi metaldir (Bölüm XV Not 3).",
        "<b>%2 kuralı (Not 5):</b> ≥ %2 platin → platin alaşımı; değilse ≥ %2 altın → altın; değilse ≥ %2 gümüş "
        "→ gümüş; üçü de %2’nin altındaysa adi metal alaşımı.",
        "<b>Kaplama (Not 7):</b> lehim, kaynak, sıcak haddeleme gibi mekanik usulle kıymetli metal kaplama 71’dir; "
        "elektroliz, buhar, püskürtme, daldırma ile kaplanan adi metal kendi faslında kalır.",
        "<b>Not 2–3:</b> kıymetli metal yalnız önemsiz süsse (monogram, kenar) eşya 71’e girmez; Fasıl 64–66 "
        "eşyası, gözlük (90), saat (91), diş dolgusu (30), silah (93) fasıl dışıdır.",
        "<b>Mücevherci / taklit (Not 9, 11):</b> 71.13 kişisel küçük süs ve üstte taşınan eşya (sigara tabakası, "
        "pudra kutusu); 71.17 yalnız kişisel küçük süs olabilir, düğme ve tarak hariç.",
    ],
    karistirilan=[
        ["Camdan taklit inci veya taş", "70.18", "Sentetik taş (kübik zirkonya) ise 71.04"],
        ["Altın kasalı kol saati", "91.01", "Not 3(l): saatler Fasıl 91"],
        ["Kehribar veya lületaşı biblo", "96.02", "Not 4(C): kıymetli taş sayılmaz"],
    ],
)

# ------------------------------------------------------------------ 72 (+ Bölüm XV notları)
H[72] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 2 kez: Bölüm XV Not 9’a göre çubuk ile tel arasındaki farkın rulo halinde olup "
            "olmama olduğu ve 72.08 yassı ürünlerinin genişlik, kalınlık, rulo, karbon ölçütleriyle alt "
            "pozisyon tablosundan ayrıştırılması.",
    pozisyonlar=[
        ["72.01", "Pik demir: %2’den fazla karbon, dövülemez"],
        ["72.08", "Alaşımsız yassı, ≥ 600 mm, sıcak haddeli, kaplamasız"],
        ["72.13", "Filmaşin: sıcak haddelenmiş, düzensiz kangal"],
        ["72.17", "Tel: soğuk elde edilmiş, kangal halinde"],
    ],
    hap=[
        "<b>Bölüm XV Not 9 (74–76, 78–81):</b> çubuk: rulo olmayan içi dolu ürün; tel: rulo halinde içi dolu "
        "ürün; levhada kalınlık ≤ genişliğin onda biri; profil: diğer sabit kesitli ürün.",
        "<b>Genel kullanıma mahsus aksam (Bölüm XV Not 2):</b> 73.07, 73.12, 73.15, 73.17, 73.18 eşyası, yaylar "
        "(saat zembereği hariç), 83.01, 83.02, 83.08, 83.10 ve 83.06 çerçeve-aynaları; makine-taşıt parçası "
        "sayılmaz.",
        "<b>Alaşım ve karma eşya (Not 5, 7):</b> ağırlıkça üstün metal belirler; demir-çelik tek metal, alaşım "
        "kendi metali sayılır (pirinç = bakır). <b>Paslanmaz çelik:</b> krom ≥ %10,5 ve karbon ≤ %1,2.",
    ],
    karistirilan=[
        ["Kaynaklı profil, palplanş", "73.01", "Fasıl 72 Not 1(n): profil değil, Fasıl 73"],
        ["Otomobil için çelik yay", "73.20", "Genel kullanıma mahsus aksam; 87.08 değil"],
    ],
)

# ------------------------------------------------------------------ 73
H[73] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 kez ana konu: “hangisi 73’te yer almaz?” – şerit halinde zımba teli 83.05; yay, "
            "filika demiri, somun, tığ 73’te. 73.26, 73.18 ve 73.21 başka sorularda çeldirici veya “fırın "
            "geçen pozisyon” olarak kullanıldı.",
    pozisyonlar=[
        ["73.16", "Çapalar, filika demirleri ve aksamı"],
        ["73.18", "Vida, cıvata, somun, perçin, pim, rondela"],
        ["73.19", "Elle kullanılan dikiş iğnesi, şiş, tığ, çengelli iğne"],
        ["73.20", "Yaylar, yay yaprakları; saat zembereği hariç"],
        ["73.21", "Elektriksiz soba, ocak, fırın, mangal (ev, kamp)"],
        ["73.26", "Diğer demir-çelik eşya (artık pozisyon)"],
    ],
    hap=[
        "<b>Boru ailesi:</b> dökme demir 73.03, dikişsiz 73.04, iç-dış kesiti daire ve dış çapı 406,4 mm’yi geçen "
        "dikişli 73.05, diğer dikişli 73.06, bağlantı parçası (flanş, dirsek, manşon) 73.07.",
        "<b>Kaplar:</b> 300 litreyi geçen depo 73.09, geçmeyen 73.10, sıkıştırılmış veya sıvılaştırılmış gaz kabı "
        "her hacimde 73.11; karıştırıcı, ısıtıcı, soğutucu tertibat varsa Fasıl 84/85.",
        "<b>Fasıl 83’e gidenler:</b> şerit halinde zımba teli ve ataş 83.05, kilit 83.01, kapı-mobilya donanımı "
        "83.02, zil ve süs eşyası 83.06; demir-çelikten olsalar da 73’e verilmez.",
        "<b>Tanımlar:</b> tel = çapı 16 mm’yi geçmeyen, sıcak veya soğuk şekil verilmiş ürün, rulo şartı yok "
        "(Not 2); dökme demir = çelik bileşimine uymayan döküm ürünü (Not 1).",
        "<b>Isıtma:</b> 73.21–73.22 ısıtmada elektrik kullanmayan cihazlar; elektrikli ve gazlı-elektrikli birleşik "
        "ocaklar 85.16. Kalibreli çelik bilya 84.82, diğer çelik bilyalar 73.26.",
    ],
    karistirilan=[
        ["Boş çelik yangın söndürme cihazı", "84.24", "Dolu-boş fark etmez; 73.26 veya 83.07 değil"],
        ["Plastik, kauçuk, çelik conta takımı (poşette)", "84.84", "Bileşimi değişik conta takımı; 73.18 değil"],
        ["Taşıma türüne göre donatılmış çelik konteyner", "86.09", "73.09 / 73.10 depo değil"],
    ],
)

# ------------------------------------------------------------------ 74
H[74] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez, Bölüm XV Not 9 üzerinden: çubuk (rulo halinde olmayan) ile tel (rulo halinde) "
            "arasındaki fark; bakırda bu ayrım 74.07 / 74.08’i belirler.",
    pozisyonlar=[
        ["74.03", "Rafine bakır ve bakır alaşımları (işlenmemiş)"],
        ["74.07", "Çubuk ve profiller (rulo halinde değil)"],
        ["74.08", "Teller (rulo halinde içi dolu)"],
        ["74.15", "Çivi, cıvata, somun; başı bakır çelik çivi"],
    ],
    hap=[
        "<b>Bakır ağırlıkça üstünse 74:</b> pirinç, bronz, nikel gümüşü, kupro-nikel bakır alaşımıdır. Rafine "
        "bakır: en az %99,85 bakır ya da tablo sınırları içinde en az %97,5 bakır (Not 1(a)).",
        "<b>Levha–yaprak sınırı 0,15 mm:</b> kalını 74.09, incesi 74.10 (kaplama dahil, mesnet hariç ölçülür); "
        "alüminyumda sınır 0,2 mm.",
        "<b>Birleşik pozisyonlar:</b> ev ve sağlık eşyası 74.18; depo, kap, zincir, yay, tel mensucat 74.19; "
        "izoleli bakır tel ve kablo 85.44.",
    ],
    karistirilan=[
        ["Başı bakır, gövdesi çelik çivi", "74.15", "Pozisyon metni ağırlık kuralından önce gelir; 73.17 değil"],
        ["Bakırdan eğilip bükülebilir boru", "83.07", "74.11 değil; Fasıl 83 eşyası metale bakmaz"],
    ],
)

# ------------------------------------------------------------------ 75
H[75] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; Bölüm XV ortak kuralları (alaşım, "
            "Not 9 tanımları) nikele de uygulanır.",
    pozisyonlar=[
        ["75.02", "İşlenmemiş nikel: külçe, katot, pellet"],
        ["75.05", "Çubuk, profil ve teller birlikte"],
        ["75.06", "Levha, şerit, yaprak (kalınlık sınırı yok)"],
        ["75.08", "Diğer eşya; kancalı elektrokaplama anotları"],
    ],
    hap=[
        "<b>Birleşik yapı:</b> çubuk-profil-tel 75.05, levha-yaprak 75.06 (0,15 mm sınırı yok), boru ve bağlantı "
        "parçası birlikte 75.07; çivi, depo, yay, tel mensucat 75.08.",
        "<b>Sınırlar:</b> rafine ferro-nikel ferro-alyaj (72.02); bakırı üstün kupro-nikel Fasıl 74; nikel "
        "kaplama faslı değiştirmez; kancalı kaplama anodu 75.08, kancasız katot 75.02.",
    ],
    karistirilan=[
        ["Nikel kaplı çelik vida", "73.18", "Kaplama yüzey işlemidir; esas metal çelik"],
    ],
)

# ------------------------------------------------------------------ 76
H[76] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; alüminyum su terazisinin 76 değil 90.31 olduğu soruda "
            "alüminyum yaprak (76.07) çeldiriciydi.",
    pozisyonlar=[
        ["76.04", "Çubuk ve profiller (içi boş profil dahil)"],
        ["76.06", "Levha, şerit (0,2 mm’yi geçen)"],
        ["76.07", "Yaprak (0,2 mm’yi geçmeyen; mesnet hariç)"],
        ["76.12", "Fıçı, kutu, tüp kaplar (≤ 300 litre)"],
    ],
    hap=[
        "<b>0,2 mm sınırı:</b> levha 76.06 / yaprak 76.07, mesnet hariç ölçülür; esas niteliğini kağıt veya "
        "kartonun verdiği folyo kaplı ürün 48.11.",
        "<b>Kaplar:</b> 300 litreyi geçen depo 76.11, geçmeyen fıçı, kutu ve diş macunu tüpü 76.12, gaz kabı "
        "76.13; ev eşyası 76.15; çivi, cıvata, zincir, tel mensucat 76.16.",
    ],
    karistirilan=[
        ["Alüminyumdan su terazisi", "90.31", "Ölçme aleti; Bölüm XV Not 1 gereği 76 dışı"],
        ["Alüminyum prefabrik yapı", "94.06", "76.10 inşaat aksamını alır, prefabrik yapıyı değil"],
    ],
)

# ------------------------------------------------------------------ 77 (saklı)
H[77] = dict(
    kademe="C",
    sinavda="Saklı fasıl.",
    pozisyonlar=[],
    hap=[
        "Armonize Sistemde ileride kullanılmak üzere saklı tutulmuştur; pozisyonu ve notu yoktur, adi metal "
        "fasılları 76’dan (alüminyum) 78’e (kurşun) atlar.",
    ],
    karistirilan=[],
)

# ------------------------------------------------------------------ 78
H[78] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; Bölüm XV ortak kuralları "
            "(alaşım, karma eşya, Not 9 tanımları) burada da geçerlidir.",
    pozisyonlar=[
        ["78.01", "İşlenmemiş kurşun; hurdadan eritilmiş külçe dahil"],
        ["78.04", "Levha, sac, yaprak, şerit; toz ve pul"],
        ["78.06", "Diğer: çubuk, tel, boru, bağlantı parçası"],
    ],
    hap=[
        "<b>Dört pozisyon:</b> işlenmemiş 78.01, hurda 78.02, yassı ürün ile toz-pul 78.04, geri kalan her şey "
        "78.06; 78.03 ve 78.05 boş olduğundan çubuk, tel, boru 78.06’dadır.",
        "<b>Fasıl dışı:</b> mühimmat saçması 93.06, kurşun mühür ve kapsül 83.09, eritici kaplı lehim çubuğu "
        "83.11, kurşun cürufu ve külü 26.20; kalayı üstün lehim Fasıl 80.",
    ],
    karistirilan=[
        ["Kurşun levhadan asit tankı", "78.06", "Levhadan yapılmış eşya levha sayılmaz; 78.04 değil"],
    ],
)

# ------------------------------------------------------------------ 79
H[79] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; çinko alaşımı ve kaplama ayrımı "
            "Bölüm XV Not 5 ve 7 ile çözülür.",
    pozisyonlar=[
        ["79.01", "İşlenmemiş çinko; pellet dahil, toz hariç"],
        ["79.03", "Toz, ince toz ve pullar"],
        ["79.04", "Çubuk, profil ve teller"],
        ["79.07", "Diğer: boru, çivi, oluk, kova, anot"],
    ],
    hap=[
        "<b>Çinko üstünse 79:</b> ağırlıkça diğer her metalden fazla olması yeter, %50 şart değil; pirinçte bakır "
        "üstün olduğundan Fasıl 74, galvanizli çelik eşya Fasıl 72/73.",
        "<b>Toz:</b> 1 mm elekten ağırlıkça %90 veya fazlası geçen ürün (Bölüm XV Not 8) 79.03’te; “çinko kurumu” "
        "ve galvaniz çamuru 26.20, boya halindeki toz Fasıl 32.",
    ],
    karistirilan=[
        ["Galvanizli çelik kova", "73.23", "Çinko kaplama faslı değiştirmez"],
    ],
)

# ------------------------------------------------------------------ 80
H[80] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; kalayın kendi faslı olduğu "
            "(Fasıl 81’de değil) bilinmeli.",
    pozisyonlar=[
        ["80.01", "İşlenmemiş kalay; kırıntı ve granül dahil"],
        ["80.03", "Çubuk, profil ve teller"],
        ["80.07", "Diğer: levha, yaprak, toz, boru, tüp"],
    ],
    hap=[
        "<b>Dört pozisyon:</b> işlenmemiş 80.01, hurda 80.02, çubuk-profil-tel 80.03, geri kalan her şey (levha, "
        "yaprak, toz, pul, boru) 80.07; 80.04–80.06 boştur.",
        "<b>Teneke kalay değildir:</b> kalay kaplı çelik yassı ürün 72.10/72.12, teneke hurdası 72.04; kalay-kurşun "
        "lehimde ağırlıkça üstün metal faslı belirler (80 ya da 78).",
    ],
    karistirilan=[
        ["Kalay yaprağından şişe kapsülü", "83.09", "Fasıl 83 eşyası metale bakmaz"],
    ],
)

# ------------------------------------------------------------------ 81
H[81] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; ancak “platin tabirine girmeyen” sorularının doğru cevabı olan "
            "berilyum ve kadmiyum bu fasılda (81.12) yer alan adi metallerdir.",
    pozisyonlar=[
        ["81.04", "Magnezyum ve eşyası (hurda, toz dahil)"],
        ["81.08", "Titanyum ve eşyası"],
        ["81.12", "Berilyum, krom, kadmiyum, vanadyum vb. ve eşyası"],
        ["81.13", "Sermetler ve eşyası"],
    ],
    hap=[
        "<b>Her metale tek pozisyon:</b> tungsten 81.01, molibden 81.02, tantal 81.03, magnezyum 81.04, kobalt "
        "81.05, bizmut 81.06, titanyum 81.08, zirkonyum 81.09, antimon 81.10, manganez 81.11; 81.07 boş.",
        "<b>Fasıl dışı:</b> ferro-alyajlar (ferro-tungsten, ferro-titan) 72.02; listede olmayan metaller (cıva, "
        "sodyum) Fasıl 28; monte edilmemiş sermet uç 82.09.",
    ],
    karistirilan=[
        ["Toz halinde tungsten karbür", "28.49", "Karbür metal değil; sinterlenmiş uç 82.09"],
    ],
)

# ------------------------------------------------------------------ 82
H[82] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 kez ana konu: 82.06 takımı 82.02–82.05 aletlerinden oluşur; çit makası (82.01) "
            "içeren takım 82.06 sayılmadı. Kalemtıraş (82.14) sıralama, demonte makineyle gelen dinamometrik "
            "anahtar ise GYK sorusunda seçenekti.",
    pozisyonlar=[
        ["82.01", "Tarım-bahçe el aletleri; çit makası, budama makası"],
        ["82.04", "Elle sıkıştırma anahtarları (dinamometrik dahil), soketler"],
        ["82.05", "Diğer el aletleri; mengene, örs, kaynak lambası"],
        ["82.06", "82.02–82.05 aletlerinden perakende takımlar"],
        ["82.13", "Parmak halkalı makaslar ve ağızları"],
        ["82.15", "Kaşık, çatal, kepçe, şeker maşası, balık bıçağı"],
    ],
    hap=[
        "<b>Not 1 – iş gören kısım:</b> adi metal, metal karbür, sermet ya da adi metal mesnetli kıymetli taş "
        "veya aşındırıcı olmalı; değilse eşya maddesine göre sınıflandırılır.",
        "<b>82.06 takımı:</b> 82.02–82.05 aletlerinden iki veya fazlası, perakende satış için; esas karakter "
        "korunursa başka pozisyondan az önemli alet olabilir. Çit makası gibi 82.01 aleti bu pozisyonlarda değildir.",
        "<b>El aleti – makine:</b> doğrudan elde kullanılan alet 82; mesnetli veya tezgaha monte olan 84 "
        "(mesnetli matkap 84.59); motorlu, pnömatik, hidrolik el aleti 84.67; elektrikli traş başları 85.10.",
        "<b>Makas ayrımı:</b> parmak halkası olmayan tek elle budama ve çit makası 82.01; parmak halkalı makas "
        "82.13; teneke makası 82.03; nalbant toynak makası 82.05.",
        "<b>Takımlar:</b> bıçak + en az eşit sayıda kaşık-çatal 82.15 (Not 3); manikür-pedikür takımı 82.14; "
        "seyahat dikiş ve tuvalet takımı 96.05; elle işleyen mekanik mutfak aleti ≤ 10 kg 82.10.",
    ],
    karistirilan=[
        ["Dinamometrik anahtar (demonte makineyle gelen)", "82.04",
         "Tek başına 82.04; sınavda makineyle (84.57) beyan edildi"],
        ["Cerrahi makas, dişçi aleti", "90.18", "Tıbbi alet; Fasıl 82 değil"],
        ["Elektrik motorlu el matkabı veya testere", "84.67", "Motorlu el aleti; 82.05 / 82.02 değil"],
    ],
)

# ------------------------------------------------------------------ 83
H[83] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 kez ana konu: demir-çelikten olsa da şerit halinde zımba telinin 73 değil 83.05 "
            "olduğu. Ayrıca adi metal kapı kilidinin (83.01) XV. Bölümde, valf ve jeneratörün XVI. Bölümde "
            "olduğu ve 83.07’nin çeldirici olarak kullanıldığı sorular var.",
    pozisyonlar=[
        ["83.01", "Kilit, asma kilit, anahtar (taslak dahil)"],
        ["83.02", "Mobilya, kapı, karoseri donanımı; küçük tekerlekler"],
        ["83.05", "Klasör mekanizması, ataş, şerit halinde zımba teli"],
        ["83.06", "Elektriksiz zil, çan; süs eşyası; çerçeve, metal ayna"],
        ["83.09", "Tıpa, kapak, kapsül, mühür"],
        ["83.11", "Eritici kaplı veya dolgulu kaynak elektrodu, teli"],
    ],
    hap=[
        "<b>Metal önemsiz:</b> Fasıl 83 eşyası hangi adi metalden olursa olsun burada; Bölüm XV Not 2 gereği "
        "72–76 ve 78–81. fasıllara verilmez (çelik zımba teli 83.05, kalay kapsül 83.09).",
        "<b>Not 1:</b> yay, zincir, kablo, vida, cıvata, somun, çivi Fasıl 83 eşyasına özel olsa da onun parçası "
        "sayılmaz; kendi pozisyonlarında kalır (kilit yayı 73.20).",
        "<b>Not 2 – küçük tekerlek (83.02):</b> çapı bandaj dahil 75 mm’yi geçmeyen ya da daha büyük olup "
        "tekerlek veya bandaj genişliği 30 mm’den az olan tekerlek.",
        "<b>Kilit – kapama:</b> anahtarlı, şifreli, elektrikli kapama 83.01; anahtarsız çanta mandalı 83.02; "
        "kopça, toka, boru şeklinde veya yarık saplı perçin 83.08; çıtçıt 96.06, fermuar 96.07.",
        "<b>Sınırlar:</b> elektrikli zil 85.31, pünez 73.17, ışıklı tabela 94.05, matbaa harfi 84.42; taşıta "
        "takılsa da kapı kolu 83.02, bisiklet zili 83.06.",
    ],
    karistirilan=[
        ["Demirden bisiklet zili", "83.06", "Taşıt aksamı 87.14 veya 73.26 değil"],
        ["Metal çerçeveli cam ayna", "70.09", "Metal ayna 83.06; cam ayna 70.09"],
        ["Delmeye dayanıksız, yangına dayanıklı kutu", "94.03", "Güvenlik şartı yok; 83.03 kasa değil"],
    ],
)

# ------------------------------------------------------------------ yazım + kontrol
LIM = {"A": ((8, 12), (6, 8), (4, 6)), "B": ((4, 6), (4, 5), (2, 3)), "C": ((2, 4), (2, 3), (1, 2))}


def wc(s):
    return len(re.sub(r"</?[bi]>|<br/>", " ", s).split())


def kontrol(n, d):
    msg = []
    if n == 77:
        return msg
    (pa, pb), (ha, hb), (ka, kb) = LIM[d["kademe"]]
    if not pa <= len(d["pozisyonlar"]) <= pb:
        msg.append(f"pozisyon sayısı {len(d['pozisyonlar'])}")
    if not ha <= len(d["hap"]) <= hb:
        msg.append(f"hap sayısı {len(d['hap'])}")
    if not ka <= len(d["karistirilan"]) <= kb:
        msg.append(f"karıştırılan sayısı {len(d['karistirilan'])}")
    for p, a in d["pozisyonlar"]:
        if wc(a) > 8:
            msg.append(f"poz {p} {wc(a)} kelime")
    for h in d["hap"]:
        if wc(h) > 30:
            msg.append(f"hap {wc(h)} kelime: {h[:40]}")
    for e, p, g in d["karistirilan"]:
        if wc(e) > 8 or wc(g) > 12:
            msg.append(f"karış {e[:30]} {wc(e)}/{wc(g)}")
    return msg


def main():
    os.makedirs(OUT, exist_ok=True)
    for n, d in sorted(H.items()):
        rec = {"tur": "hap", "fasil": n, "kademe": d["kademe"], "sinavda": d["sinavda"],
               "pozisyonlar": d["pozisyonlar"], "hap": d["hap"], "karistirilan": d["karistirilan"]}
        p = os.path.join(OUT, f"fasil_{n:02d}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
        m = kontrol(n, d)
        print(p, "uyarı: " + "; ".join(m) if m else "")


if __name__ == "__main__":
    main()
