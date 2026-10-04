#!/usr/bin/env python3
"""Hap bilgi sayfaları – Grup H5: Fasıl 50–63 (Bölüm XI, dokumaya elverişli maddeler).

Bölüm XI notlarının çekirdeği (Not 1 bölüm dışı, Not 2 karışım, Not 7–8 hazır eşya) Fasıl 50'de;
perakende (Not 4) ve dikiş ipliği (Not 5) Fasıl 52'de; sicim (Not 3) Fasıl 53/56'da; elastomerik iplik
(Not 13) Fasıl 60'ta; set kuralı (Not 14) ve kapanma yönü Fasıl 61/62'de verilmiştir.
"""
import json
import os
import re

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KITAP, "hap")

H = {}

# ------------------------------------------------------------------ 50
H[50] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; Bölüm XI notları dolaylı çıktı: “aynı bölüm” sorusunda pamuk "
            "ipliği, gömlek, toz bezi XI. Bölümde, düğme Fasıl 96’da; tekstil yüzlü valiz Not 1(l) gereği 42.02’de.",
    pozisyonlar=[
        ["50.02", "Ham ipek (bükülmemiş; zamkı alınmış, boyalı olabilir)"],
        ["50.03", "Döküntü: çekilemeyen koza, buret, ditme döküntüsü"],
        ["50.06", "Perakende ipek ipliği; ipek böceği guddesi (misina)"],
        ["50.07", "İpek veya ipek döküntüsünden dokunmuş mensucat"],
    ],
    hap=[
        "<b>Bölüm dışı (Not 1):</b> fırça kılı 05.02, at kılı 05.11, diş ipliği 33.06, kesiti 1 mm’yi aşan "
        "plastik monofil, 42.01–42.02 eşyası, ayakkabı, başlık, oyuncak, bebek bezi 96.19.",
        "<b>Karışım (Not 2):</b> ağırlıkça üstün gelen lif belirler; eşitlikte numara sırasında en sondaki "
        "pozisyon. Önce fasıl, sonra pozisyon; 54 ve 55 tek fasıl sayılır.",
        "<b>Hazır eşya (Not 7–8):</b> kare-dikdörtgen dışı kesilmiş, kenarı bastırılmış, düğümlü saçaklı, "
        "dikilerek birleştirilmiş veya örülerek şekillenmiş eşya; 50–55 ve 60’a, aksi yazılmadıkça 56–59’a da "
        "girmez.",
    ],
    karistirilan=[
        ["İpekten dokunmuş kadın bluzu", "62.06", "Hazır eşya; 50.07 kumaş değil (Bölüm XI Not 7–8)"],
        ["İpek kırpıntı, toz, taraz; ipek vatka", "56.01", "Döküntü 50.03’e değil, vatka-kırpıntı pozisyonuna"],
    ],
)

# ------------------------------------------------------------------ 51
H[51] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez: Not 1(b) ince hayvan kılı listesi, “hangi hayvandan elde edilemez” kalıbıyla; "
            "cevap katır (lama, yak, alpaka, Tibet keçisi listede).",
    pozisyonlar=[
        ["51.01", "Yün (karde-taranmamış): yalnız koyun-kuzu lifi"],
        ["51.02", "İnce veya kaba hayvan kılı (karde-taranmamış)"],
        ["51.09", "Perakende yün ve ince kıl ipliği"],
        ["51.10", "Kaba kıl ve at kılı ipliği (perakende dahil)"],
    ],
    hap=[
        "<b>İnce hayvan kılı (Not 1(b)):</b> alpaka, lama, vikuna, deve, yak; Ankara, Tibet, Kaşmir vb. keçi "
        "(adi keçi hariç); tavşan, yabani tavşan, kunduz, Güney Amerika kunduzu, misk faresi. Katır, at yok.",
        "<b>Yün = yalnız koyun-kuzu lifi.</b> Kaba kıl listede olmayan hayvanlarınkidir (adi keçi); fırça kılı "
        "05.02, at kılı (yele-kuyruk) 05.11 fasıl dışı; at kılı ipliği 51.10, kumaşı 51.13.",
        "<b>Perakende:</b> yün ve ince kıl ipliği 51.09; kaba kıl ve at kılı ipliği perakende olsa da 51.10. "
        "Yün ipliği hiçbir kalınlıkta sicim (56.07) sayılmaz.",
    ],
    karistirilan=[
        ["%40 sentetik, %35 taranmış yün, %25 ince kıl", "51.12", "Yün ve ince kıl toplanır (%60); 55.15 değil"],
        ["Ham at kılı (yele, kuyruk)", "05.11", "Bölüm XI dışı; at kılı ipliği 51.10"],
    ],
)

# ------------------------------------------------------------------ 52
H[52] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 kez, ikisi de kapsam sorusu: pamuk ipliği Fasıl 52’dedir (viskoz ve sentetik filament "
            "54, keten döküntüsü 53; Bölüm X değil XI) ve “pamuk 53. fasılda” ifadesi yanlıştır. “Aynı bölüm” sorusunda "
            "pamuk ipliği seçenekte geçti.",
    pozisyonlar=[
        ["52.01", "Pamuk (karde-penye edilmemiş); hidrofil dahil"],
        ["52.04", "Pamuk dikiş ipliği (perakende olsun olmasın)"],
        ["52.07", "Perakende pamuk ipliği (dikiş ipliği hariç)"],
        ["52.08", "Kumaş: ≥%85 pamuk, ≤200 g/m² (ağırı 52.09)"],
        ["52.10", "%85’ten az, sentetik-suni karışık, ≤200 g/m²"],
        ["52.12", "Diğer pamuklu kumaş (yün, keten vb. karışık)"],
    ],
    hap=[
        "<b>Linter ≠ pamuk:</b> 5 mm’den kısa linter 14.04; ham, ağartılmış, boyalı, hidrofil pamuk "
        "karde-penye edilmedikçe 52.01; vatka 56.01.",
        "<b>Perakende (Bölüm XI Not 4):</b> mesnete sarılı: ipek-sentetik 85 g, diğer 125 g; top-çile: 85 / 125 g, "
        "kalın iplik 500 g. Tek kat, bobin, çapraz çile perakende değil.",
        "<b>Dikiş ipliği (Not 5):</b> katlı, mesnetle ≤1.000 g, dikiş için aprelenmiş, “Z” bükümlü → 52.04, "
        "perakende olsun olmasın; 52.07 dikiş ipliği dışındaki perakende iplik.",
        "<b>%85 ve 200 g:</b> %85 iplikte (52.05/52.06) ve kumaşta pozisyon böler; 200 g/m² yalnız kumaşta. "
        "%85’ten az pamuklu kumaşta esas karışan lif yün-keten ise 52.12.",
        "<b>Önce fasıl (Not 2):</b> %40 pamuk + %30 suni + %30 sentetik devamsız → 54–55 toplamı üstün → 55.16. "
        "Eşitlikte numara sırasında son: pamuk-yün eşitse Fasıl 52.",
    ],
    karistirilan=[
        ["Viskoz (suni) filament ipliği", "54.03", "Suni lif (Fasıl 54 Not 1); pamuk ipliği 52.05–52.06"],
        ["Pamuktan havlu kumaşı (bukleli, top halinde)", "58.02", "Havlu cinsi bukleli mensucat Fasıl 52’de değil"],
        ["Emici dokusu pamuk bebek bezi", "96.19", "Bölüm XI Not 1(u): malzemeye bakılmaz"],
    ],
)

# ------------------------------------------------------------------ 53
H[53] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; çeldirici olarak çıktı: “pamuk 53. fasılda yer alır” yanlış "
            "ifadesi ve 52. fasıl sorusunda “keten döküntüleri” seçeneği (53.01).",
    pozisyonlar=[
        ["53.01", "Keten lifi, kıtık ve döküntüleri (iplik değil)"],
        ["53.02", "Kendir: yalnız Cannabis sativa L."],
        ["53.03", "Jüt, kenaf ve diğer iç kabuk lifleri"],
        ["53.05", "Koko, abaka, rami, sisal ve diğer bitkisel lifler"],
    ],
    hap=[
        "<b>Zincir:</b> lif 53.01–53.05 → iplik (keten 53.06, jüt 53.07, kendir-koko-kağıt 53.08) → kumaş "
        "(keten 53.09, jüt 53.10, diğer-kağıt 53.11). Fasıl notu yoktur.",
        "<b>Adına aldanma:</b> Manila kendiri (abaka) 53.05, Hint/Sunn kendiri 53.03; Yeni Zelanda keteni 53.05; "
        "rami çift çenekli olsa da 53.05.",
        "<b>Sicim eşiği (Not 3):</b> cilalı keten-kendir ≥1.429 desiteks, cilasız 20.000’i aşan; üç ve fazla "
        "katlı koko → 56.07. Kağıt ipliği (örülmemiş, metal takviyesiz) 53.08’de kalır.",
    ],
    karistirilan=[
        ["%40 pamuk, %35 keten, %25 jüt kumaş", "53.09", "Keten ve jüt aynı fasılda toplanır; 52.12 değil"],
        ["Pamuk lifi (çırçırlanmış)", "52.01", "Fasıl 52; Fasıl 53 pamuk dışı bitkisel liflerdir"],
    ],
)

# ------------------------------------------------------------------ 54
H[54] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; 52. fasıl sorusunda “viskoz ipeği” ve “sentetik-suni "
            "filamentler” Fasıl 54 eşyası olarak çeldiriciydi.",
    pozisyonlar=[
        ["54.02", "Sentetik filament ipliği (perakende değil)"],
        ["54.03", "Suni (viskoz, asetat) filament ipliği"],
        ["54.04", "Sentetik monofil (≥67 desiteks) ve şerit (≤5 mm)"],
        ["54.07", "Sentetik filament ipliğinden dokunmuş mensucat"],
    ],
    hap=[
        "<b>Sentetik / suni (Fasıl 54 Not 1):</b> sentetik monomer polimerizasyonuyla (naylon, poliester, "
        "akrilik); suni tabii polimerden (selüloz, kazein) – viskoz, asetat, kupro. Viskoz bitkisel lif değildir.",
        "<b>Ölçüler:</b> 67 desiteksten ince monofil iplik sayılır (54.02/54.03); kesiti 1 mm’yi aşan monofil, "
        "5 mm’den geniş şerit Fasıl 39. Filament 54, kesilmiş (devamsız) lif 55.",
        "<b>Sicim ve perakende:</b> sentetik-suni iplik 10.000 desiteksi aşarsa 56.07; perakende 54.06 "
        "(mesnetle 85 g), tek kat iplik perakende sayılmaz; dikiş ipliği 54.01.",
    ],
    karistirilan=[
        ["%35 filament, %25 devamsız sentetik, %40 yün kumaş", "54.07",
         "54 ve 55 tek fasıl: sentetik %60; 51.12 değil"],
        ["Çengel takılmış misina (olta)", "95.07", "Çengelsiz monofil 54.04; olta Fasıl 95"],
    ],
)

# ------------------------------------------------------------------ 55
H[55] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; yalnız 52. fasıl kapsam sorusunda sentetik-suni lif "
            "çeldiricileri arasında dolaylı yer aldı.",
    pozisyonlar=[
        ["55.03", "Sentetik devamsız lif (karde edilmemiş)"],
        ["55.09", "Sentetik devamsız lif ipliği (perakende değil)"],
        ["55.13", "Sentetik %85’ten az, pamuklu, ≤170 g/m²"],
        ["55.16", "Suni devamsız lif mensucatı (oran alt pozisyonda)"],
    ],
    hap=[
        "<b>Demet (Fasıl 55 Not 1):</b> 2 m’den uzun, metrede 5 turdan az bükümlü, filamenti 67 desiteksten "
        "ince, toplam 20.000 desiteksi aşan demet 55.01/55.02; 2 m’ye kadar 55.03/55.04.",
        "<b>Kumaş eşikleri:</b> sentetik devamsız ≥%85 → 55.12; daha azı ve esasen pamuklu ≤170 g/m² 55.13, "
        "ağırı 55.14; diğer karışım 55.15; suni devamsız 55.16 (pamukta eşik 200 g).",
        "<b>Kısa lif:</b> 5 mm’yi geçmeyen lif kırpıntısı (flok), toz, vatka 56.01; dokunmamış 56.03; sentetik "
        "paçavra Fasıl 63.",
    ],
    karistirilan=[
        ["%55 pamuk, %45 poliester, 180 g/m² kumaş", "52.10", "Pamuk üstün → Fasıl 52; ≤200 g/m² → 52.10"],
        ["Poliester filament ipliğinden kumaş", "54.07", "Filament Fasıl 54; Fasıl 55 yalnız devamsız lif"],
    ],
)

# ------------------------------------------------------------------ 56
H[56] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; “terkip yoluyla elde edilen deri” sorusunda 56.03 (dokunmamış "
            "mensucat) çeldiriciydi, doğrusu 41.15.",
    pozisyonlar=[
        ["56.01", "Vatka; 5 mm’ye kadar lif, toz, taraz"],
        ["56.02", "Keçe (iğne işi, dikiş-trikotaj dahil)"],
        ["56.03", "Dokunmamış mensucat (emdirilmiş, kaplanmış olsa da)"],
        ["56.07", "Sicim, kordon, ip, halat (örülmüş dahil)"],
    ],
    hap=[
        "<b>Sicim-ip-halat (Bölüm XI Not 3):</b> ipek ve bitkisel liften 20.000, sentetik-suniden 10.000 "
        "desiteksi aşan iplik 56.07; sıkı örülmüş ve metal takviyeli ip her zaman 56.07. Yün ipliği asla sicim değil.",
        "<b>Fasıl 56 Not 1:</b> bebek bezi, hijyenik ped, tampon 96.19; parfüm-kozmetik, sabun, cila, yumuşatıcı "
        "emdirilmiş taşıyıcı vatka-keçe-dokunmamış Fasıl 33, 34.01, 34.05, 38.09.",
        "<b>Plastikli keçe/dokunmamış (Not 3):</b> kural olarak 56.02/56.03’te kalır; dokuma maddesi ≤%50 veya "
        "tamamen gömülü keçe, iki yüzü görünür kaplı dokunmamış Fasıl 39–40.",
    ],
    karistirilan=[
        ["Terkip yoluyla elde edilen deri levha", "41.15", "Deri lifli aglomere; dokunmamış 56.03 veya 59.03 değil"],
        ["Sicimden düğümlü hazır balık ağı", "56.08", "Örme file 60.02–60.06; spor filesi Fasıl 95"],
    ],
)

# ------------------------------------------------------------------ 57
H[57] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; Bölüm XI kapsamı ve 58–59 ile "
            "sınırları için bilinmeli.",
    pozisyonlar=[
        ["57.01", "Düğümlü veya sarmalı halılar (Gördes, Senna düğümü)"],
        ["57.02", "Dokunmuş halılar; kilim, sumak, karaman dahil"],
        ["57.03", "Tufte halılar (çim dahil)"],
    ],
    hap=[
        "<b>Fasıl 57 Not 1:</b> kullanımda dışa bakan yüzü tekstil olan yer kaplaması; yer kaplaması özelliği "
        "taşıyorsa duvara asılsa da burada. Hazır olsun olmasın Fasıl 57.",
        "<b>Dışarıda kalanlar:</b> halı altı bağımsız taban örtüsü maddesine göre (Not 2); linoleum ve kaplamalı "
        "tekstil mesnetli yer kaplaması 59.04; hasır paspas 46.01; plastik çim Fasıl 39.",
    ],
    karistirilan=[
        ["El dokuması duvar halısı (Goblen)", "58.05", "Pano niteliği; kilim ise 57.02"],
        ["Yere serilmeye elverişsiz tufte mensucat", "58.02", "Halı sertlik-kalınlığı yok; 57.03 değil"],
    ],
)

# ------------------------------------------------------------------ 58
H[58] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; yangın hortumu sorusunda 58.11 (kapitoneli mensucat) "
            "çeldiriciydi, doğrusu 59.09.",
    pozisyonlar=[
        ["58.01", "Dokunmuş kadife, peluş, tırtıl mensucat"],
        ["58.04", "Tül, ağ mensucat; dantel (zeminsiz)"],
        ["58.06", "Kordela: eni ≤30 cm, iki kenarı kendinden"],
        ["58.11", "Kapitoneli parça mensucat (top halinde)"],
    ],
    hap=[
        "<b>Lif cinsi önemsiz:</b> 58.09 (metal iplikli giyim-döşeme kumaşı) hariç; kaplanmış mensucat, fitil, "
        "hortum, kolan Fasıl 59; örme 60; hazır eşya 61–63 (duvar halısı 58.05 hariç).",
        "<b>Ayrımlar:</b> dantel zeminsiz, işleme (58.10) mevcut zemin üzerine; havlu kumaşı 58.02, havlu 63.02; "
        "gaz mensucat leno dokuma, tıbbi gaz bezi 30.05.",
    ],
    karistirilan=[
        ["Sentetik liften yangın hortumu", "59.09", "Teknik eşya; 58.11 veya 63.06 değil"],
        ["Kilim, sumak, karaman", "57.02", "Duvar halısı tekniği olsa da 58.05 değil"],
    ],
)

# ------------------------------------------------------------------ 59
H[59] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 kez: sentetik liften yangın hortumu 59.09 (çeldiriciler 39.17, 58.11, 63.06). "
            "Seçeneklerde de geçti: terkip deri sorusunda 59.03, “gezici hayvan sergisi ile aynı fasıl” "
            "sorusunda tiyatro dekoru (59.07).",
    pozisyonlar=[
        ["59.03", "Plastikle emdirilmiş, kaplanmış, lamine mensucat"],
        ["59.06", "Kauçuklu mensucat (≤1.500 g/m² veya dokuma %50’den fazla)"],
        ["59.07", "Diğer kaplanmış mensucat; tiyatro dekoru bezleri"],
        ["59.09", "Tulumba ve benzeri hortumlar (teçhizatlı olsa da)"],
        ["59.10", "Taşıyıcı ve transmisyon kolanları"],
        ["59.11", "Teknik ürünler (Not 8): elek bezi, filtre, conta"],
    ],
    hap=[
        "<b>Plastikli mensucat (Not 2):</b> işlem çıplak gözle görülmüyorsa 50–55, 58, 60; 7 mm silindirde "
        "kırılmadan bükülemiyorsa veya plastiğe tamamen gömülü / iki yüzü kaplıysa Fasıl 39; diğerleri 59.03.",
        "<b>Kauçuklu mensucat (Not 5):</b> 1.500 g/m²’yi geçmeyen ya da geçip ağırlıkça %50’den fazla dokuma "
        "maddesi içeren 59.06; aksi halde Fasıl 40. Kauçuklu kolan 40.10.",
        "<b>Hortum ve kolan:</b> tekstil hortum astarlı, spiralli, rakorlu olsa da 59.09 (mensucat yalnız "
        "takviyeyse 40.09); kolan 3 mm’den inceyse 59.10 değil, uçları birleştirilmişse kalınlık aranmaz.",
        "<b>59.07:</b> başka maddelerle (katran, mum, yağ, mika tozu) kaplanmış mensucat ve boyanmış tiyatro "
        "dekoru, atölye fonu bezleri; sadece boyayla desenlenmiş kumaş girmez.",
        "<b>Hazır eşya kuralı:</b> kaplanmış mensucattan giysi 61.13 / 62.10, çadır 63.06’ya gider; hortum, "
        "kolan ve 59.11 teknik eşyası hazır halde de Fasıl 59’dadır.",
    ],
    karistirilan=[
        ["Mensucatla takviyeli vulkanize kauçuk hortum", "40.09", "Tekstil yalnız takviye; 59.09 değil"],
        ["Kauçuklu mensucattan transmisyon kayışı", "40.10", "Fasıl 59 Not 7(b); 59.10 değil"],
        ["Plastik kaplı dokunmuş kumaştan yağmurluk", "62.10", "Hazır eşya; 59.03 kumaş değil (Bölüm XI Not 8)"],
    ],
)

# ------------------------------------------------------------------ 60
H[60] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; yalnız “kullanılmış giyim eşyası hangi fasılda” sorusunda "
            "Fasıl 60 yanlış seçenekti (doğrusu 63).",
    pozisyonlar=[
        ["60.01", "Tüylü örme (kadife, peluş, taklit havlu)"],
        ["60.02", "Eni ≤30 cm, elastomer/kauçuk iplik ≥%5"],
        ["60.04", "Eni 30 cm’yi aşan, elastomer ≥%5"],
        ["60.06", "Diğer örme veya kroşe mensucat (artık)"],
    ],
    hap=[
        "<b>Yalnız parça mensucat:</b> örme kumaş top veya basitçe kare-dikdörtgen kesilmiş halde 60’ta; kenarı "
        "bastırılmış, şekilli örülmüş eşya hazır eşyadır → 61–63 (Bölüm XI Not 7–8).",
        "<b>Fasıl 60 Not 1–3:</b> tığ işi dantel 58.04, örme etiket 58.07, kaplanmış örme Fasıl 59 (tüylü ise "
        "60.01’de kalır); dikiş-trikotaj eşyası “örme” sayılır.",
        "<b>Elastomerik iplik (Bölüm XI Not 13):</b> üç katına gerilince kopmayan, iki katına gerilip bırakılınca "
        "5 dakikada en çok 1,5 katına dönen sentetik filament; tekstüre iplik hariç.",
    ],
    karistirilan=[
        ["Kullanıma hazır örme seyahat battaniyesi", "63.01", "Hazır eşya; 60.05 parça mensucat değil"],
        ["Dokunmuş kadife, peluş", "58.01", "Dokuma; örme tüylü mensucat 60.01"],
    ],
)

# ------------------------------------------------------------------ 61
H[61] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez: Not 9 metni verilip cinsiyeti belirlenemeyen örme giysi soruldu → kadın-kız "
            "pozisyonu (GYK 3–4 ifadeleri çeldirici). Kullanılmış giyim sorusunda Fasıl 61 yanlış seçenekti.",
    pozisyonlar=[
        ["61.09", "Tişört, fanila, atlet (cinsiyetsiz)"],
        ["61.11", "Bebek giyimi: boy ≤86 cm; öncelikli"],
        ["61.13", "59.03/59.06/59.07 örme mensucattan giysi"],
        ["61.17", "Örme şal, kravat, mendil, diğer aksesuar"],
    ],
    hap=[
        "<b>Kapanma yönü (Not 9):</b> önü soldan sağa kapanan erkek, sağdan sola kadın giysisidir; kesimden "
        "belliyse bakılmaz. Cinsiyeti belirlenemeyen giysi kadın-kız pozisyonuna girer (62’de de aynı).",
        "<b>Öncelik ve dışarıda kalanlar:</b> bebek 61.11 her pozisyondan, 61.13 diğerlerinden önce gelir; örme "
        "sütyen-korse 62.12, kullanılmış balya 63.09, ortopedik korse 90.21.",
        "<b>Set ≠ takım (Bölüm XI Not 14):</b> farklı pozisyondaki giysiler perakende sette de ayrı ayrı "
        "sınıflandırılır; takım elbise, takım, pijama gibi metinde geçenler hariç.",
    ],
    karistirilan=[
        ["Köpek elbisesi (tekstil)", "42.01", "Hayvan eşyası Bölüm VIII; Fasıl 61–62 değil"],
        ["Örme eldiven", "61.16", "Dokunmuş 62.16, kauçuk 40.15; 61.15 çorap değil"],
    ],
)

# ------------------------------------------------------------------ 62
H[62] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 kez: kenarı 50 cm kare fular → 62.13 mendil (Not 8; seçenekler 62.13–62.17). "
            "Kullanılmış giyim (63.09) ve “aynı bölüm” (gömlek) sorularında seçenekteydi.",
    pozisyonlar=[
        ["62.09", "Bebek giyimi (boy ≤86 cm); her pozisyondan önce"],
        ["62.10", "Keçe, dokunmamış, 59.03/59.06/59.07 mensucattan giysi"],
        ["62.12", "Sütyen, korse, jartiyer (örülmüş olsun olmasın)"],
        ["62.13", "Mendil: kare/karemsi, hiçbir kenarı 60 cm’yi aşmaz"],
        ["62.14", "Şal, eşarp, kaşkol, duvak; kenarı 60 cm’yi aşan"],
        ["62.16", "Eldiven (dokunmuş; örme ise 61.16)"],
    ],
    hap=[
        "<b>Fular-mendil (Not 8):</b> kare veya karemsi, hiçbir kenarı 60 cm’yi aşmayan fular 62.13’te mendildir; "
        "bir kenarı 60 cm’yi geçen veya kare olmayan şal-eşarp 62.14. Saçak ölçüye dahil.",
        "<b>Kapsam (Not 1):</b> örülmemiş her mensucattan (dokunmuş, keçe, dokunmamış, dantel; vatka hariç) hazır "
        "giysi. Örme olan Fasıl 61’e gider; tek istisna 62.12 sütyen-korse grubu.",
        "<b>Öncelik:</b> bebek 62.09 → özel mensucattan giysi 62.10 → diğerleri. Keçeden bebek giysisi 62.09; "
        "kapitoneli (58.11) mont 62.01/62.02; kâğıt giysi 48.18.",
        "<b>Örme / örülmemiş farkı:</b> fanila-atlet örme 61.09 (cinsiyetsiz), dokunmuş 62.07/62.08; çorap örme "
        "61.15, örülmemiş 62.17; ayrı yelek 62.11 (örme 61.10); mendil-şal-kravat örme 61.17.",
        "<b>Kapanma ve set:</b> soldan sağa erkek, sağdan sola kadın; belirlenemezse kadın (Not 9). Farklı "
        "pozisyondaki giysiler perakende sette de ayrı sınıflandırılır (Bölüm XI Not 14).",
    ],
    karistirilan=[
        ["Kenarı 50 cm kare ipek fular", "62.13", "Hiçbir kenarı 60 cm’yi aşmıyor → mendil; 62.14 değil"],
        ["Örme sütyen", "62.12", "Örülmüş olsun olmasın 62.12; Fasıl 61 değil"],
        ["Ortopedik korse, fıtık bağı", "90.21", "Fasıl 62 Not 2(b); 62.12 değil"],
    ],
)

# ------------------------------------------------------------------ 63
H[63] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 kez: kullanılmış giyim eşyası Fasıl 63 (63.09; çeldirici 60–62) ve “63.07’de "
            "sınıflandırılamaz” kalıbında bebek bezi (96.19); maske, toz-yer bezi, cankurtaran yeleği 63.07’dir. "
            "Kamp çadırı (63.06) “aynı fasıl” sorusunda çeldiriciydi.",
    pozisyonlar=[
        ["63.01", "Battaniye ve diz (seyahat) battaniyesi"],
        ["63.02", "Yatak çarşafı, masa örtüsü, havlu, mutfak bezi"],
        ["63.05", "Ambalaj torba ve çuvalları (dökme yük torbası dahil)"],
        ["63.06", "Çadır, tente, dış stor, yelken, kamp eşyası"],
        ["63.07", "Diğer hazır eşya: yer-toz bezi, maske, cankurtaran yeleği"],
        ["63.09", "Kullanılmış giyim: kullanım izi + dökme/balya"],
    ],
    hap=[
        "<b>63.09 (Not 3):</b> fazla kullanım izi ve dökme ya da balya-çuval ambalaj birlikte aranır; liste "
        "kapalı: giysi-aksesuar, battaniye, ev tekstili, ayakkabı, başlık. Halı, kilim, 94.04 eşyası hariç.",
        "<b>I. tali fasıl (Not 1–2):</b> 63.01–63.07 her mensucattan (örme, keçe, dokunmamış dahil) hazır "
        "eşyadır; 56–62. fasıl eşyası ve 63.09 eşyası buraya girmez.",
        "<b>Fasıl 94’e kaçanlar:</b> yorgan, kapitone örtü, uyku torbası, içi doldurulmuş yastık-minder 94.04; "
        "abajur 94.05. Battaniye 63.01, minder kılıfı 63.04.",
        "<b>Bezler:</b> havlu, tabak kurulama ve cam bezi 63.02; kaba yer, toz, bulaşık bezi 63.07; deterjan "
        "veya cila emdirilmişse 34.01 / 34.05.",
        "<b>63.08 takımı:</b> en az bir parça dokunmuş mensucat + iplik, perakende; halı, kilim, işleme yapımı "
        "için. Kullanıma hazır masa örtüsü veya giysi yapım takımı girmez.",
    ],
    karistirilan=[
        ["Tek kullanımlık bebek bezi", "96.19", "Bölüm XI Not 1(u); 63.07 değil"],
        ["Tekstil yüzlü tekerlekli valiz, sırt çantası", "42.02", "Bölüm XI Not 1(l); 63.05–63.07 değil"],
        ["Çocuk oyun çadırı", "95.03", "Oyuncak; kamp çadırı 63.06"],
    ],
)

# ------------------------------------------------------------------ kontrol + yazım
SINIR = {"A": ((8, 12), (6, 8), (4, 6)), "B": ((4, 6), (4, 5), (2, 3)), "C": ((2, 4), (2, 3), (1, 2))}
TAG = re.compile(r"</?(b|i)>|<br/>")
POZ = re.compile(r"^\d\d\.\d\d$")


def kelime(s):
    return len(TAG.sub("", s).split())


def kontrol(n, d):
    hata = []
    (pmin, pmax), (hmin, hmax), (kmin, kmax) = SINIR[d["kademe"]]
    if not pmin <= len(d["pozisyonlar"]) <= pmax:
        hata.append(f"pozisyonlar {len(d['pozisyonlar'])}")
    if not hmin <= len(d["hap"]) <= hmax:
        hata.append(f"hap {len(d['hap'])}")
    if not kmin <= len(d["karistirilan"]) <= kmax:
        hata.append(f"karistirilan {len(d['karistirilan'])}")
    for p, a in d["pozisyonlar"]:
        if not POZ.match(p) or not p.startswith(f"{n:02d}."):
            hata.append(f"pozisyon kodu {p}")
        if kelime(a) > 8:
            hata.append(f"pozisyon {p} {kelime(a)} kelime")
    for h in d["hap"]:
        if kelime(h) > 30:
            hata.append(f"hap {kelime(h)} kelime: {h[:40]}")
    for e, p, g in d["karistirilan"]:
        if not POZ.match(p):
            hata.append(f"karistirilan kodu {p}")
        if kelime(e) > 8:
            hata.append(f"karistirilan eşya {kelime(e)} kelime: {e}")
        if kelime(g) > 12:
            hata.append(f"karistirilan neden {kelime(g)} kelime: {g}")
    return hata


def main():
    os.makedirs(OUT, exist_ok=True)
    tum = []
    for n, d in sorted(H.items()):
        h = kontrol(n, d)
        if h:
            tum.append(f"Fasıl {n}: " + "; ".join(h))
        kayit = {"tur": "hap", "fasil": n, "kademe": d["kademe"], "sinavda": d["sinavda"],
                 "pozisyonlar": d["pozisyonlar"], "hap": d["hap"], "karistirilan": d["karistirilan"]}
        with open(os.path.join(OUT, f"fasil_{n:02d}.json"), "w", encoding="utf-8") as f:
            json.dump(kayit, f, ensure_ascii=False, indent=1)
    if tum:
        print("UYARI:\n  " + "\n  ".join(tum))
    print(f"{len(H)} dosya yazıldı: {', '.join(f'fasil_{n:02d}.json' for n in sorted(H))}")


if __name__ == "__main__":
    main()
