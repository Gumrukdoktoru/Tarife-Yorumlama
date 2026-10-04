#!/usr/bin/env python3
"""Hap bilgi sayfaları: Fasıl 39–49 (grup H4).

Kaynak: data/fasil_NN.json modülleri, kaynak/fasillar/FASILnn.txt, kaynak/son5_analiz.json.
Çıktı: hap/fasil_39.json … hap/fasil_49.json
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "hap")

H = {}

# ---------------------------------------------------------------- 39 (A)
H[39] = dict(
    kademe="A",
    sinavda="Son 5 sınavda 4 soruda konu, 6 soruda seçenek: “hangisi 39. fasılda / 39.26’da yer "
            "almaz” (plastik okul çantası 42.02; biberon 39.24) ve “farklı fasıl” (silikon 39.10 ≠ kauçuklar "
            "Fasıl 40; sertleştirilmiş protein 39.13 ≠ jelatin, enzim Fasıl 35). 39.15, 39.17, 39.21, 39.26 başka "
            "fasıl sorularında sık çeldiricidir.",
    pozisyonlar=[
        ["39.10", "Silikonlar; silikon elastomeri de burada"],
        ["39.13", "Tabii polimerler; sertleştirilmiş protein, aljinik asit"],
        ["39.15", "Plastik döküntü, kalıntı ve hurdalar"],
        ["39.16", "Kesiti 1 mm’yi geçen monofil, çubuk, profil"],
        ["39.17", "Boru, hortum, bağlantı elemanı; sucuk kılıfı"],
        ["39.20", "Gözeneksiz, takviyesiz levha, film, folye"],
        ["39.21", "Gözenekli veya takviyeli-lamine levha, film"],
        ["39.22", "Küvet, lavabo, klozet, rezervuar: hijyenik eşya"],
        ["39.23", "Ambalaj: şişe, kutu, torba, tıpa, kapak"],
        ["39.24", "Sofra, mutfak, ev, tuvalet eşyası; biberon"],
        ["39.25", "Not 11 inşaat malzemesi; 300 litreyi geçen tank"],
        ["39.26", "Diğer: büro malzemesi, süs, emzik, yağmurluk"],
    ],
    hap=[
        "<b>Önce Not 2:</b> plastikten olmak yetmez. Çanta-valiz 42.02, ayakkabı-şapka-şemsiye Bölüm XII, "
        "mobilya-lamba 94, oyuncak 95, düğme-tarak-kalem 96, makine XVI, taşıt aksamı XVII, saat 91.",
        "<b>Plastik (Not 1):</b> 39.01–39.14 maddeleri; dış etkiyle şekil alır, şeklini korur. Tanım tarifenin "
        "her yerinde geçerli; vulkanize lif dahil, Bölüm XI dokumaya elverişli maddeleri hariç.",
        "<b>İlk şekiller (Not 6):</b> sıvı, hamur, dispersiyon, çözelti; düzensiz blok, biçimsiz parça, toz, "
        "granül, pul. Düzenli geometrik blok ilk şekil değil, levhadır (39.20 / 39.21).",
        "<b>Kopolimer (Not 4):</b> tek monomer ünitesi ağırlıkça %95’e ulaşmayan polimer. Ağırlıkça üstün "
        "komonomerin pozisyonu; eşitlikte numara sırasına göre en sondaki pozisyon.",
        "<b>Kauçuk değil:</b> silikon elastomeri 39.10 ve poliizobütilen 39.02 sentetik kauçuk tanımına uymaz; "
        "tabii, sentetik, rejenere kauçuk ve çıkıl Fasıl 40’tadır.",
        "<b>Not 2(e) ve yakınları:</b> çözücüsü ağırlıkça %50’yi geçen uçucu organik çözücülü çözelti 32.08 "
        "(kollodiyon hariç); polimer mumları 34.04; net 1 kg’ı geçmeyen perakende yapıştırıcı 35.06.",
        "<b>Ölçü eşikleri:</b> kesiti 1 mm’yi geçmeyen sentetik monofil 54.04; dikdörtgen kesitte boy enin 1,5 "
        "katını aşarsa profil (Not 8); kağıt dışı mesnetli duvar kaplaması eni ≥ 45 cm (Not 9).",
        "<b>Hurda ve askılar:</b> ilk şekle dönmüş tek termoplastik hurdası 39.01–39.14, diğer hurda 39.15. "
        "Duvara daimi tespitli havlu askısı-sabunluk 39.25, serbest duranı 39.24.",
    ],
    karistirilan=[
        ["Plastik okul çantası, valiz, el çantası", "42.02", "Fasıl 39 Not 2: 42.02 eşyası Fasıl 39’da yer almaz"],
        ["Plastik biberon", "39.24", "Ev-tuvalet eşyası; emzik (bebek kuklası) ve süs eşyası 39.26"],
        ["Sertleştirilmiş protein", "39.13", "Tadil edilmiş tabii polimer; jelatin 35.03, enzim 35.07"],
        ["Sentetik liften yangın hortumu", "59.09", "Dokumaya elverişli maddeden hortum; 39.17 değil"],
        ["Terkip yoluyla elde edilen deri levha", "41.15", "Fasıl 41 Not 3; plastik levha 39.21 değil"],
        ["Plastik, kauçuk, çelik conta takımı poşette", "84.84", "Farklı maddeden conta takımı; 39.26 / 40.16 değil"],
    ],
)

# ---------------------------------------------------------------- 40 (B)
H[40] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 soruda konu, 3 soruda seçenek: “hangisi farklı fasılda” kalıbında tabii, bütadien, "
            "rejenere kauçuk ve çıkıl (Fasıl 40) ≠ silikon (39.10). 40.16, cam silici (85.12) ve conta takımı "
            "(84.84) sorularında çeldirici; silgi (40.16) sıralama sorusunda geçti.",
    pozisyonlar=[
        ["40.01", "Tabii kauçuk, balata, güta-perka, çıkıl"],
        ["40.02", "Sentetik kauçuk (Not 4 testi); taklit kauçuk"],
        ["40.11", "Kauçuktan yeni dış lastikler"],
        ["40.15", "Giyim eşyası; cerrahi dahil her tür eldiven"],
        ["40.16", "Diğer: conta, silgi, paspas, şişirilebilir eşya"],
        ["40.17", "Sert kauçuk (ebonit) her şekliyle, döküntüsü dahil"],
    ],
    hap=[
        "<b>Kauçuk (Not 1):</b> tabii kauçuk, balata, güta-perka, guayül, çıkıl ve benzeri tabii sakızlar, "
        "sentetik kauçuk, yağlardan taklit kauçuk ve rejenereleri; vulkanize veya sert olsun olmasın.",
        "<b>Sentetik kauçuk testi (Not 4):</b> 18–29 °C’de kopmadan 3 kat uzar, 2 kat uzatılınca 5 dakikada "
        "1,5 kata döner. Geçemeyen elastomer Fasıl 39’dadır; tiyoplastlar testsiz kauçuktur.",
        "<b>Not 2 hariçleri:</b> Bölüm XI, ayakkabı 64, başlık 65, sert kauçuktan makine aksamı XVI, Fasıl 90, "
        "92, 94, 96 ve Fasıl 95 (spor eldiveni ile 40.11–40.13 eşyası hariç).",
        "<b>Eşikler:</b> kesiti 5 mm’yi geçen vulkanize iplik 40.08, geçmeyen 40.07 (Not 7). Sert kauçuk: "
        "100 birim kauçuğa 15 birimden fazla birleşik kükürt → 40.17.",
        "<b>Lastikler:</b> yeni dış lastik 40.11; sırt geçirilmiş-kullanılmış lastik, dolgu lastiği, sırt ve "
        "kolan 40.12; iç lastik 40.13. Kesinlikle kullanılamaz lastik döküntüsü 40.04.",
    ],
    karistirilan=[
        ["Silikon elastomeri", "39.10", "Not 4 testine uymaz; kauçuklardan farklı fasıl"],
        ["Elektrik motorlu cam silici", "85.12", "Pozisyon metninde adıyla geçer; 40.16 ve 87.08 değil"],
        ["Kauçuk, plastik, çelik contalar poşette", "84.84", "Farklı maddeden conta takımı; 40.16 değil"],
    ],
)

# ---------------------------------------------------------------- 41 (C)
H[41] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 soruda konu, 1 soruda seçenek: “terkip yoluyla elde edilen deri” levhaları 41.15 "
            "(39.21, 56.03, 59.03 çeldirici); Bölüm VIII kapsamı (kürk, kösele, çanta var; ayakkabı yok).",
    pozisyonlar=[
        ["41.01", "Sığır, at ham derisi; tüylü olabilir"],
        ["41.07", "Sığır, at: bitirilmiş deri, kösele, parşömine"],
        ["41.14", "Güderi, rugan, ruganla kaplanmış, metalize deri"],
        ["41.15", "Terkip deri; kullanılamaz deri kırpıntısı, tozu"],
    ],
    hap=[
        "<b>Terkip deri (Not 3):</b> tarifenin her yerinde yalnız 41.15 maddeleri: esası deri veya deri lifi "
        "olan levha, yaprak, şerit. Plastik, kauçuk, kağıt, sıvanmış mensucat esaslı taklitler 39, 40, 48, 59.",
        "<b>Tüylü ham deri (Not 1(c)):</b> sığır, at, koyun-kuzu, keçi, domuz, geyik, ceylan, deve, köpek "
        "Fasıl 41’de; Astragan-Karakul, Hint-Çin-Moğol-Tibet kuzusu, Yemen-Moğol-Tibet keçisi 43.01.",
        "<b>Bölüm VIII = Fasıl 41–43:</b> deri-kösele, deri eşya-saraciye-çanta, kürk; bölüm notu yoktur. "
        "Ayakkabı Fasıl 64 ile Bölüm XII’dedir.",
    ],
    karistirilan=[
        ["Kılıyla dabaklanmış sığır derisi", "43.02", "Not 1(c) istisnası yalnız ham deri içindir"],
        ["Ham deri kırpıntısı", "05.11", "Not 1(a); dabaklı deri döküntüsü ise 41.15"],
    ],
)

# ---------------------------------------------------------------- 42 (A)
H[42] = dict(
    kademe="A",
    sinavda="Son 5 sınavda 4 soruda konu, 3 soruda seçenek; odak hep 42.02: “hangisi 42.02’de yer almaz” "
            "(ahşap mücevher kutusu 44.20, metal sigara kutusu) ve “farklı fasıl” (ahşap bavul 42.02 ≠ Fasıl 44; "
            "plastik okul çantası 42.02 ≠ Fasıl 39). Bölüm VIII kapsamında çantalar soruldu.",
    pozisyonlar=[
        ["42.01", "Saraciye, koşum; her hayvan, her madde"],
        ["42.02", "İlk kısım (bavul, valiz, okul çantası): her madde"],
        ["42.02", "İkinci kısım (el çantası, cüzdan, kutular): sınırlı madde"],
        ["42.03", "Deriden giysi, eldiven, kemer, askı, bilek kayışı"],
        ["42.05", "Deriden diğer: makine kayışı, kitap kabı, etiket"],
        ["42.06", "Bağırsak, kursak, mesane, tendondan eşya; katgüt"],
        ["44.20", "Ahşap mücevher kutusu — 42.02 değil"],
        ["39.23", "Kısa ömürlü plastik saplı çanta — 42.02 değil"],
    ],
    hap=[
        "<b>42.02 ilk kısım her maddeden:</b> sandık, bavul, valiz, makyaj valizi, evrak-okul çantası, gözlük, "
        "dürbün, fotoğraf makinesi, müzik aleti, silah mahfazası; ahşap, metal, plastik olabilir.",
        "<b>42.02 ikinci kısım sınırlı madde:</b> el-sırt-spor çantası, cüzdan, para kesesi, sigara-mücevher "
        "kutusu yalnız deri, terkip deri, plastik yaprak, tekstil, vulkanize lif, karton ya da bunlarla veya kağıtla kaplı.",
        "<b>Not 3(A):</b> uzun süre kullanılmayacak plastik yapraktan saplı çanta 39.23; örülmeye elverişli "
        "maddeden (hasır, sepet örgüsü) çanta 46.02.",
        "<b>42.01 her hayvan, her madde:</b> eyer, koşum, yular, köpek elbisesi, kedi-köpek tasması, at "
        "battaniyesi. Ayrı gelen üzengi, gem Bölüm XV; kamçı 66.02.",
        "<b>42.03 (Not 4):</b> deriden giysi ve aksesuar: eldiven (spor ve koruma dahil), önlük, askı, bel "
        "kemeri, palaska, bilek kayışı. Saat kayışı 91.13.",
        "<b>Not 2 hariçleri:</b> steril katgüt 30.06, kürk astarlı giysi 43.03 / 43.04 (eldiven hariç), "
        "ayakkabı 64, başlık 65, taklit mücevher 71.17, müzik aleti teli 92.09, oyuncak 95, düğme 96.06.",
        "<b>Kıymetli metal süs (Not 3(B)):</b> esas karakter vermiyorsa eşya 42.02 / 42.03’te kalır (altın "
        "tokalı deri kemer 42.03); esas karakter verirse Fasıl 71.",
    ],
    karistirilan=[
        ["Ahşap bavul, valiz", "42.02", "İlk kısım her maddeden; Fasıl 44 değil"],
        ["Kalıplanmış plastik okul çantası", "42.02", "Fasıl 39 Not 2: 42.02 eşyası Fasıl 39’a girmez"],
        ["Hasır veya sepet örgüsü el çantası", "46.02", "Not 3(A): örülmeye elverişli maddeden eşya"],
        ["Deri saat kayışı", "91.13", "Not 4; deri bilek kayışı ise 42.03"],
        ["İçi hakiki kürk kaplı deri ceket", "43.03", "Not 2(b); deri-kürk eldiven ise 42.03’te kalır"],
    ],
)

# ---------------------------------------------------------------- 43 (C)
H[43] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; 2 soruda seçenekte geçti: Bölüm VIII kapsamı (kürk bölümde, "
            "ayakkabı değil) ve pozisyon sıralamasında taklit kürk (43.04).",
    pozisyonlar=[
        ["43.01", "Ham kürk; Fasıl 41 hayvanları hariç"],
        ["43.02", "Dabaklanmış kürk; başka madde katmadan birleştirilmiş"],
        ["43.03", "Kürkten giysi, aksesuar, eşya; kürk astarlı giysi"],
        ["43.04", "Taklit kürk (lif yapıştırılmış, dikilmiş) ve eşyası"],
    ],
    hap=[
        "<b>Kürk (Not 1):</b> 43.01 ham kürkleri hariç, tüyü veya yünü alınmamış dabaklanmış ya da aprelenmiş "
        "deri; hayvan türü önemsiz (kılıyla dabaklanmış buzağı derisi de kürk).",
        "<b>Kürklü giysi (Not 4):</b> içi kürk-taklit kürk kaplı veya dışında basit süsü aşan kürklü giysi "
        "43.03 / 43.04; yaka, kol, cep, etek kenarı kürkü basit süstür.",
        "<b>Taklit kürk (Not 5):</b> yün, kıl, lifin mesnede yapıştırılması veya dikilmesi; dokuma veya örme "
        "tüylü kumaş 58.01 / 60.01. Kürk şapka 65, kürk bot 64, oyuncak 95.",
    ],
    karistirilan=[
        ["Deri ve kürkten eldiven", "42.03", "Not 2(c); tamamen kürkten eldiven 43.03"],
        ["Kürk kaplı bavul, valiz", "42.02", "42.02 ilk kısmı her maddeden; 43.03 değil"],
    ],
)

# ---------------------------------------------------------------- 44 (A)
H[44] = dict(
    kademe="A",
    sinavda="Son 5 sınavda 3 soruda konu, 2 soruda seçenek: “farklı pozisyon / fasıl” kalıbı (kontrplak 44.12 ≠ "
            "kapı, padavra, merdiven, panjur 44.18; ahşap bavul 42.02 ≠ odun kömürü, yonga levha, kontrplak) ve "
            "ahşap mücevher kutusu (44.20, 42.02 değil). Sıralamada odun kömürü 44.02 → travers 44.06 → tabut "
            "44.21; ayakkabı kalıbı 44.17 seçenekte.",
    pozisyonlar=[
        ["44.01", "Yakacak odun, yonga, talaş, pelet, briket"],
        ["44.02", "Odun kömürü; meyve kabuğu kömürü dahil"],
        ["44.06", "Ahşap demiryolu, tramvay traversleri"],
        ["44.07", "Biçilmiş ağaç, kalınlığı 6 mm’yi geçen"],
        ["44.10", "Yonga levha, OSB, waferboard"],
        ["44.11", "Lif levha (MDF, sert levha)"],
        ["44.12", "Kontrplak, ahşap kaplamalı levha, lamine ağaç"],
        ["44.15", "Sandık, kasa, kablo makarası, palet"],
        ["44.17", "Alet, alet ve fırça sapı; ayakkabı kalıbı"],
        ["44.18", "Doğrama: kapı, pencere, merdiven, padavra, parke panosu"],
        ["44.20", "Kakma; mücevher, çatal-bıçak kutusu; heykelcik, süs"],
        ["44.21", "Diğer: elbise askısı, tabut, el merdiveni, kürdan"],
    ],
    hap=[
        "<b>Not 1 hariçleri:</b> ahşap olsa da 42.02 eşyası (bavul), sepetçi eşyası 46, ayakkabı 64, "
        "şemsiye-baston 66, taklit mücevher 71.17, makine-taşıt aksamı XVI-XVII, saat-müzik aleti XVIII, "
        "mobilya 94, oyuncak 95.",
        "<b>Not 1 – toz ağaç ve kömür:</b> parfümeri-eczacılık amaçlı toz ağaç 12.11, boyacılık-dabaklama "
        "amaçlı 14.04, aktif kömür 38.02, ateşli silah aksamı 93.05, sanat eseri 97.",
        "<b>Bambu (Not 6):</b> “ağaç” atfı bambu ve odunsu maddeleri kapsar: bambu kontrplak, levha, kömür "
        "Fasıl 44; işlenmemiş bambu 14.01, bambu sepet 46.02, bambu mobilya 94.",
        "<b>6 mm sınırı:</b> uzunlamasına biçilmiş, dilimlenmiş ağaç 6 mm’yi geçerse 44.07, geçmezse 44.08 "
        "(kaplama yaprağı). Rendeleme, zımparalama, uç uca ekleme yeri değiştirmez; devamlı profil 44.09.",
        "<b>Levhalar:</b> yonga levha-OSB 44.10, lif levha 44.11, kontrplak 44.12, yoğunlaştırılmış ağaç 44.13. "
        "Not 4: kesilip şekillendirilse de başka eşya vasfı kazanmadıkça yerinde kalır.",
        "<b>Not 3:</b> 44.14–44.21 eşyası masif ağaçtan olduğu gibi yonga levha, lif levha, lamine veya "
        "yoğunlaştırılmış ağaçtan da olabilir.",
        "<b>44.18 doğrama:</b> kapı, pencere, kepenk, merdiven, beton kalıbı, padavra, birleştirilmiş parke "
        "panosu, hücreli levha, glulam. El merdiveni ve basamak 44.21.",
        "<b>Alet ve kutu:</b> ahşap alet, fırça gövde-sapı, ayakkabı kalıbı 44.17 (iş gören kısmı Fasıl 82 "
        "Not 1 maddesinden alet hariç, Not 5); mücevher kutusu, biblo 44.20.",
    ],
    karistirilan=[
        ["Ahşap bavul, valiz", "42.02", "Not 1: 42.02 eşyası; ilk kısmı her maddeden"],
        ["Ahşap mücevher kutusu", "44.20", "42.02 ikinci kısmı ahşap kutuyu kapsamaz"],
        ["Kontrplak", "44.12", "Kapı, padavra, merdiven, panjur (kepenk) ise 44.18"],
        ["Demonte ahşap masa, dolap", "94.03", "Mobilya Fasıl 94 (Not 1); demonte eşya GYK 2(a)"],
        ["Aktif kömür", "38.02", "Not 1; odun kömürü ise 44.02"],
        ["Bitmiş süpürge, fırça", "96.03", "Fırçanın ahşap gövde ve sapı 44.17’de kalır"],
    ],
)

# ---------------------------------------------------------------- 45 (C)
H[45] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 soruda konu: “mantardan eşyadan hangisi 45. fasılda” — şişe tıpası 45.03; "
            "ayakkabı topuğu (64), şapka siperliği (65), dart tablası (95) Not 1 gereği dışarıda.",
    pozisyonlar=[
        ["45.01", "Ham tabii mantar, döküntü, granül, toz"],
        ["45.02", "Kabuğu alınmış; dikdörtgen blok, levha, şerit"],
        ["45.03", "Tabii mantardan eşya: tıpa, conta, ağ yüzdürücüsü"],
        ["45.04", "Aglomere mantar ve ondan eşya"],
    ],
    hap=[
        "<b>Not 1:</b> mantardan olsa da ayakkabı ve aksamı (topuk, tabanlık) Fasıl 64, başlık ve aksamı "
        "(siperlik) Fasıl 65, oyuncak-oyun-spor eşyası (dart tablası, olta mantarı) Fasıl 95.",
        "<b>Mantar = mantar meşesi kabuğu:</b> keskin kenarlı tıpa taslağı ve dikdörtgen levha 45.02; yuvarlak "
        "kenarlı taslak ve tıpa 45.03; aglomere mantardan tıpa, karo 45.04.",
    ],
    karistirilan=[
        ["Tıpa diskli metal şişe kapsülü", "83.09", "45.03 hariç tutması; mantar yalnız disk"],
        ["Mantar conta da içeren conta takımı", "84.84", "Farklı maddeden takım contalar; 45.03 değil"],
    ],
)

# ---------------------------------------------------------------- 46 (C)
H[46] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez, tarife yapısı sorusunda: sepetçi-hasırcı eşyası (46.02) Bölüm IX’dadır, "
            "Bölüm X değil (Bölüm IX = Fasıl 44–46).",
    pozisyonlar=[
        ["46.01", "Örgüler; levha halinde hasır, paspas, paravan"],
        ["46.02", "Sepetçi eşyası (sepet, örgü çanta); lufadan eşya"],
    ],
    hap=[
        "<b>Örülmeye elverişli madde (Not 1):</b> hasır, söğüt, bambu, hint kamışı, saz, ağaç ve bitkisel "
        "şeritler, eğrilmemiş tabii lif, plastik monofil-şerit, kağıt şerit. Deri, keçe, insan saçı, at kılı, iplik değil.",
        "<b>Not 2 hariçleri:</b> duvar kaplaması 48.14, sicim-halat 56.07 (örülmüş olsa da), ayakkabı 64, "
        "başlık 65, sepetçi eşyasından taşıt gövdesi 87, mobilya-lamba 94.",
        "<b>Ham ve ince madde:</b> işlenmemiş bambu, rattan, söğüt 14.01; kesiti 1 mm’yi geçmeyen monofil ve "
        "görünür eni 5 mm’yi aşmayan plastik şerit dokuma maddesidir (Fasıl 54).",
    ],
    karistirilan=[
        ["Rattan koltuk, hasır sandalye", "94.01", "Not 2: mobilya her maddeden Fasıl 94"],
        ["Bambu kontrplak", "44.12", "Fasıl 44 Not 6: “ağaç” bambuyu da kapsar"],
    ],
)

# ---------------------------------------------------------------- 47 (C)
H[47] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez, sıralama kalıbında: geri kazanılmış kağıt lifi hamuru 47.06 → önceki günden "
            "satılmamış gazete 47.07 → gazete kağıdı 48.01 → günün gazetesi 49.02.",
    pozisyonlar=[
        ["47.01", "Mekanik odun hamuru"],
        ["47.02", "Çözünür kimyasal odun hamuru (Not 1)"],
        ["47.06", "Geri kazanılmış kağıt lifi, linter, bambu hamuru"],
        ["47.07", "Kağıt-karton döküntü, hurda; eski gazete"],
    ],
    hap=[
        "<b>Hamur yöntemi:</b> mekanik 47.01, çözünür kimyasal 47.02, soda-sülfat 47.03, sülfit 47.04, mekanik + "
        "kimyasal 47.05; odun dışı lif ve geri kazanılmış kağıt hamuru 47.06.",
        "<b>Not 1:</b> 20 °C’de %18 sodyum hidroksitte bir saat sonra çözünmeyen kısım soda-sülfatta ≥ %92, "
        "sülfitte ≥ %88; sülfitte kül ≤ %0,15 → 47.02.",
        "<b>47.07 hurda:</b> kağıt-karton kırpıntısı, eski gazete-dergi, matbaa ıskartası; paketlemede "
        "kullanılabilmesi yeri değiştirmez. Kağıt yünü 48.23, gümüşlü fotoğraf kağıdı hurdası 71.12.",
    ],
    karistirilan=[
        ["Pamuk linteri", "14.04", "Hammaddedir; linterden elde edilen hamur 47.06"],
        ["PE veya PP liflerinden sentetik kağıt hamuru", "39.20", "Selülozik değil; Fasıl 47 dışında"],
    ],
)

# ---------------------------------------------------------------- 48 (A)
H[48] = dict(
    kademe="A",
    sinavda="Son 5 sınavda 4 soruda konu, 2 soruda seçenek: sigara kağıdı 48.13 (e-sigara 85.43, kartuş 24.04, "
            "sigara 24.02 ile boşluk doldurma), gazete kağıdı 48.01 sıralaması, fotokopi kağıdının bölümü "
            "(Bölüm X), not defteri + parfüm (set değil, ayrı ayrı). Not defteri 48.20 sıralama seçeneklerinde geçti.",
    pozisyonlar=[
        ["48.01", "Gazete kağıdı (Not 4), rulo veya tabaka"],
        ["48.02", "Yazı-baskı, fotokopi kağıdı; her ebatta"],
        ["48.03", "Tuvalet, havlu kağıdı; eni 36 cm’yi geçen rulo"],
        ["48.04", "Kraft kağıt ve karton (Not 6)"],
        ["48.11", "Plastik, mum, yapışkanla kaplı-emdirilmiş kağıt"],
        ["48.13", "Sigara kağıdı; her ebatta, defter, boru"],
        ["48.14", "Duvar kağıdı; rulo eni 45–160 cm"],
        ["48.18", "Tuvalet kağıdı, mendil, peçete, havlu; küçük rulo"],
        ["48.19", "Kutu, koli, torba, kese kağıdı"],
        ["48.20", "Defter, ajanda, klasör, form, albüm"],
        ["48.21", "Kağıt etiketler, baskılı olsun olmasın"],
        ["48.23", "Diğer: kağıt tabak-bardak, kesilmiş kağıt"],
    ],
    hap=[
        "<b>Bölüm X = Fasıl 47–49:</b> hamur (47) → kağıt ve kağıt eşya (48) → basılı ürün (49); fotokopi "
        "kağıdı 48.02 ile Bölüm X’dadır.",
        "<b>Gazete kağıdı (Not 4):</b> lifin en az %50’si mekanik veya kimyasal-mekanik odun lifi, 40–65 g/m2; "
        "rulo eni 28 cm’yi geçer (tabakada bir kenar 28, diğeri 15 cm’yi).",
        "<b>36 cm kuralı (Not 8):</b> 48.03–48.09 yalnız eni 36 cm’yi geçen rulo veya bir kenarı 36, diğeri "
        "15 cm’yi geçen tabaka; 48.02, 48.10, 48.11 her ebatta.",
        "<b>Not 6–7:</b> kraft = lifin en az %80’i sülfat-soda kimyasal lifi. 48.01–48.11’den birden fazlasına "
        "uyan kağıt, metin aksini demedikçe numara sırasına göre en sondakine.",
        "<b>Plastikli kağıt:</b> plastik tabaka toplam kalınlığın yarısından fazlaysa Fasıl 39, değilse 48.11; "
        "duvar kaplaması her durumda 48.14 (Not 9: eni 45–160 cm rulo).",
        "<b>Not 2 hariçleri:</b> parfümlü-kozmetikli kağıt 33, sabunlu 34.01, fotoğraf kağıdı 37.01–37.04, "
        "reaktifli kağıt 38.22, zımpara 68.05, oyuncak 95, bebek bezi-ped-tampon 96.19, 42.02 eşyası.",
        "<b>Baskı (Not 12):</b> motif veya resim eşyanın esas unsuruysa Fasıl 49; duvar kağıdı 48.14 ve etiket "
        "48.21 yine Fasıl 48. Baskısı tali ajanda-form 48.20.",
        "<b>Ebat pozisyon değiştirir:</b> tuvalet kağıdı eni 36 cm’yi geçen rulo 48.03, küçük rulo 48.18; karbon "
        "kağıdı geniş rulo 48.09, küçük ebat 48.16. Sigara kağıdı her ebatta 48.13.",
    ],
    karistirilan=[
        ["Kağıttan bebek bezi, hijyenik ped", "96.19", "Not 2(q): Fasıl 96 eşyası; 48.18 değil"],
        ["Not defteri + parfüm birlikte", "48.20", "Set değil (GYK 3(b)); parfüm ayrıca 33.03"],
        ["Elektronik sigara", "85.43", "Sigara kağıdı 48.13, sigara 24.02, kartuş 24.04"],
        ["Takvim", "49.10", "Baskı esas; ajanda, takvimli hatıra defteri 48.20"],
        ["Günün gazetesi", "49.02", "Gazete kağıdı 48.01; satılmamış eski gazete 47.07"],
        ["Turnusol kağıdı, teşhis şeridi", "38.22", "Not 2(f): reaktif emdirilmiş kağıt"],
    ],
)

# ---------------------------------------------------------------- 49 (B)
H[49] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 soruda konu: basılı rölyef dünya haritası 90.23 (Not 1; 49.05 değil) ve gazete "
            "zinciri sıralaması (47.06 → 47.07 → 48.01 → 49.02).",
    pozisyonlar=[
        ["49.01", "Kitap, broşür; ciltli gazete takımı (Not 3)"],
        ["49.02", "Gazete, periyodik yayın; reklam içerse de"],
        ["49.03", "Çocuk resimli kitabı, boyama albümü (Not 6)"],
        ["49.05", "Basılı harita, atlas, küre; rölyef değil"],
        ["49.10", "Matbu takvimler, blok takvim dahil"],
        ["49.11", "Diğer: katalog, afiş, bilet, resim, sticker"],
    ],
    hap=[
        "<b>Ölçüt:</b> baskı eşyanın esas karakterini ve kullanımını belirliyorsa Fasıl 49; tali ise malzemenin "
        "faslı (kağıtta 48). 39.18, 39.19, 48.14, 48.21 baskılı olsa da dışarıda.",
        "<b>Not 1 hariçleri:</b> rölyef harita, plan, küre 90.23 (baskılı olsun olmasın); saydam negatif-pozitif "
        "Fasıl 37; oyun kağıdı 95; orijinal gravür 97.02; 97.04 pulları; antika 97.",
        "<b>Gazete ve kitap:</b> gazete 49.02; başka surette birleştirilmiş veya tek kapakta birden fazla sayı "
        "49.01 (Not 3); esasen reklam yayını, ticari katalog 49.11 (Not 5).",
        "<b>Baskılı (Not 2):</b> teksir, bilgisayar çıktısı, kabartma, fotoğraf, fotokopi, termokopi, daktilo "
        "dahil. Elle çizilmiş plan, el yazısı metin 49.06; nota 49.04.",
        "<b>Pul ve değerli kağıt:</b> tedavüldeki kullanılmamış pul, damgalı kağıt, banknot, çek defteri, hisse "
        "senedi 49.07; tedavülde olmayan koleksiyon pulu 97.04.",
    ],
    karistirilan=[
        ["Basılı rölyef dünya haritası", "90.23", "Not 1(b): baskılı olsa da 49.05 değil"],
        ["Satılmamış eski gazete", "47.07", "Kağıt döküntüsü sayılır; günün gazetesi 49.02"],
        ["Ajanda, takvimli hatıra defteri", "48.20", "Baskı tali; takvim ise 49.10"],
    ],
)

# ---------------------------------------------------------------- yaz ve kendi kendini denetle
LIM = {"A": ((8, 12), (6, 8), (4, 6)), "B": ((4, 6), (4, 5), (2, 3)), "C": ((2, 4), (2, 3), (1, 2))}
TAG = re.compile(r"</?(b|i)>|<br/>")


def wc(s):
    return len(TAG.sub("", s).split())


def kontrol(n, d):
    uy = []
    (p0, p1), (h0, h1), (k0, k1) = LIM[d["kademe"]]
    if not p0 <= len(d["pozisyonlar"]) <= p1:
        uy.append(f"pozisyonlar {len(d['pozisyonlar'])} ({p0}–{p1})")
    if not h0 <= len(d["hap"]) <= h1:
        uy.append(f"hap {len(d['hap'])} ({h0}–{h1})")
    if not k0 <= len(d["karistirilan"]) <= k1:
        uy.append(f"karistirilan {len(d['karistirilan'])} ({k0}–{k1})")
    for p, a in d["pozisyonlar"]:
        if not re.fullmatch(r"\d\d\.\d\d", p):
            uy.append(f"poz kodu {p}")
        if wc(a) > 8:
            uy.append(f"poz {p} {wc(a)} kelime: {a}")
    for b in d["hap"]:
        if wc(b) > 30:
            uy.append(f"hap {wc(b)} kelime: {b[:50]}")
    for g, p, r in d["karistirilan"]:
        if wc(g) > 8:
            uy.append(f"kar. eşya {wc(g)} kelime: {g}")
        if wc(r) > 12:
            uy.append(f"kar. neden {wc(r)} kelime: {r}")
        if not re.fullmatch(r"\d\d\.\d\d", p):
            uy.append(f"kar. kodu {p}")
    s = d["sinavda"]
    if len(re.findall(r"[^\d][.!?](\s|$)", s)) > 2:
        uy.append("sinavda cümle sayısı fazla")
    return uy


def main():
    os.makedirs(OUT, exist_ok=True)
    for n, d in sorted(H.items()):
        out = {"tur": "hap", "fasil": n, "kademe": d["kademe"], "sinavda": d["sinavda"],
               "pozisyonlar": d["pozisyonlar"], "hap": d["hap"], "karistirilan": d["karistirilan"]}
        for u in kontrol(n, d):
            print(f"  ! fasıl {n}: {u}")
        p = os.path.join(OUT, f"fasil_{n:02d}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        print("yazıldı", p)


if __name__ == "__main__":
    main()
