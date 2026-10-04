#!/usr/bin/env python3
"""Hap bilgi fasıl sayfaları – Grup H2 (Fasıl 6–24).

Kaynak: data/fasil_NN.json (doğrulanmış modüller), kaynak/fasillar/FASILnn.txt,
kaynak/son5_analiz.json. Çıktı: hap/fasil_NN.json
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "hap")

H = {}

# ---------------------------------------------------------------- FASIL 6 (C)
H[6] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; bilgi Bölüm II kapsamı "
            "(Fasıl 6–14 bitkisel ürünler) ve 12.11 ile sınır sorularında arka plan olarak gerekir.",
    pozisyonlar=[
        ["06.01", "Çiçek soğanı, yumru, rizom; hindiba bitkisi-kökü"],
        ["06.02", "Diğer canlı bitkiler, fide, çelik, mantar miseli"],
        ["06.03", "Kesme çiçek ve tomurcuk; çiçekli buket, çelenk"],
        ["06.04", "Çiçeksiz süs yaprağı, dal, ot, yosun, liken"],
    ],
    hap=[
        "<b>Bölüm II notu (pellet):</b> doğrudan sıkıştırılarak veya ağırlığın en çok %3’ü kadar bağlayıcıyla "
        "topak haline getirilmiş ürün. Bölüm II = Fasıl 6–14 (bitkisel ürünler).",
        "<b>Not 1:</b> fasıl yalnız dikim veya süs amaçlı canlı bitkileri kapsar; patates, soğan, şalot, "
        "sarımsak dikimlik olsa da Fasıl 7’dedir.",
        "<b>Not 2:</b> buket, çelenk, çiçek sepetinde diğer maddeden aksesuar dikkate alınmaz; tek çiçek varsa "
        "06.03. Kolaj ve dekoratif plaket 97.01; buket veya süse uygun olmayan çiçek 12.11.",
    ],
    karistirilan=[
        ["Dikimlik soğan, sarımsak, şalot", "07.03", "Not 1: dikim amacı Fasıl 7’den çıkarmaz"],
        ["Parfümeri veya eczacılık için çiçek", "12.11", "Sunuluş şekliyle buket veya süse uygun değil"],
    ],
)

# ---------------------------------------------------------------- FASIL 7 (C)
H[7] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; bitki çayı yapımında kullanılacak ada çayı sorusunda 07.12 "
            "(kurutulmuş sebze) çeldirici seçenekti, doğrusu 12.11.",
    pozisyonlar=[
        ["07.09", "Diğer sebzeler: mantar, biber, zeytin, kabak, maydanoz"],
        ["07.12", "Kurutulmuş sebzeler; kuru baklagil hariç"],
        ["07.13", "Kabuksuz kuru baklagiller; tohumluk dahil"],
        ["07.14", "Manyok, salep, tatlı patates, yer elması (nişasta-inülinli)"],
    ],
    hap=[
        "<b>Not 2 – sebze sayılanlar:</b> mantar, domalan, zeytin, kebere, kabaklar, patlıcan, tatlı mısır, "
        "Capsicum ve Pimenta meyveleri, rezene, maydanoz, tarhun, tere, güvey otu.",
        "<b>Biber ve unlar:</b> taze Capsicum-Pimenta 07.09, dondurulmuşu 07.10; kurutulmuş, ezilmiş veya "
        "öğütülmüşü 09.04 (Not 4). Patates unu 11.05, kuru baklagil unu 11.06.",
        "<b>Ot mu, sebze mi?</b> Maydanoz, tere, tarhun 07.09; nane, fesleğen, biberiye, ada çayı 12.11. "
        "Salamurada geçici korunan, hemen yenmeyen sebze 07.11; başka şekilde hazırlanmışı Fasıl 20.",
    ],
    karistirilan=[
        ["Bitki çayı için kuru ada çayı", "12.11", "Kurutulmuş sebze (07.12) değil; Fasıl 12 Not 4"],
        ["Kurutulmuş, toz kırmızı biber", "09.04", "Fasıl 7 Not 4; taze biber 07.09"],
    ],
)

# ---------------------------------------------------------------- FASIL 8 (C)
H[8] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez doğrudan: “hangisi diğerlerinden farklı pozisyonda” kalıbında taze kaju "
            "cevizi (08.01), fındık, kestane, pekan ve kola cevizinden (08.02) ayrıldı.",
    pozisyonlar=[
        ["08.01", "Hindistan cevizi, Brezilya cevizi, kaju cevizi"],
        ["08.02", "Diğer sert kabuklular: fındık, badem, kestane, pekan, kola"],
        ["08.10", "Diğer taze meyveler: çilek, kivi, nar"],
        ["08.13", "Diğer kurutulmuş meyveler; kuruyemiş karışımları"],
    ],
    hap=[
        "<b>Adı sayılan meyveler:</b> 08.01–08.06’dakiler (kaju, fındık, muz, incir, turunçgil, üzüm) taze ve "
        "kuru halde kendi pozisyonunda; 08.07–08.10 yalnız taze; diğer kuru meyveler 08.13.",
        "<b>Notlar:</b> yenmeyen meyve fasıl dışı (Not 1); soğutulmuş = taze (Not 2); kükürtleme, sorbik asit, "
        "bitkisel yağ veya az glikoz şurubu kuru meyveyi fasıldan çıkarmaz (Not 3).",
        "<b>Fasıl dışı:</b> yer fıstığı 12.02 (kavrulmuşu 20.08); kopra 12.03; zeytin, domates, biber Fasıl 7; "
        "ardıç meyvesi 09.09; kakao 18.01.",
    ],
    karistirilan=[
        ["Kavrulmamış yer fıstığı", "12.02", "Sert kabuklu meyve değil, yağlı tohum; kavrulmuşu 20.08"],
        ["Kaktüs inciri (Frenk inciri)", "08.10", "08.04’teki incir yalnız Ficus carica"],
    ],
)

# ---------------------------------------------------------------- FASIL 9 (A)
H[9] = dict(
    kademe="A",
    sinavda="Son 5 sınavda 2 kez doğrudan, 4 kez seçenek olarak: kahvenin Bölüm II’de olduğu (IV. Bölüm "
            "sorusunda sirke, kakao, şeker, meşrubatla birlikte) soruldu. “Tümü 12.11” ve ada çayı sorularında "
            "vanilya-tarçın-karanfil, kişniş-kimyon-anason ile 09.02 ve 09.10 çeldirici oldu.",
    pozisyonlar=[
        ["09.01", "Kahve (kavrulmuş, kafeinsiz dahil); kahve içeren ikameler"],
        ["09.02", "Çay: yalnız Thea; aromalı çay dahil"],
        ["09.03", "Paraguay çayı (maté)"],
        ["09.04", "Piper biberi; kurutulmuş-öğütülmüş Capsicum ve Pimenta"],
        ["09.05", "Vanilya (vanilin ve vanilya şekeri hariç)"],
        ["09.06", "Tarçın ve tarçın ağacının çiçekleri"],
        ["09.07", "Karanfil: meyve, tane ve saplar"],
        ["09.08", "Küçük Hindistan cevizi, kabuğu; kakule"],
        ["09.09", "Anason, rezene, kişniş, kimyon tohumları; ardıç meyvesi"],
        ["09.10", "Zencefil, safran, zerdeçal, kekik, defne, köri; karışımlar"],
    ],
    hap=[
        "<b>Not 1 – karışımlar:</b> aynı pozisyondaki ürünlerin karışımı o pozisyonda; farklı pozisyondakiler "
        "09.10’da. Katılan madde esas özelliği değiştirirse fasıldan çıkar; çeşni karışımı 21.03.",
        "<b>Kahve:</b> çiğ, kavrulmuş, kafeinsiz, öğütülmüş kahve ve herhangi oranda kahve içeren ikame 09.01. "
        "Hülasa, instant kahve ve kahvesiz kavrulmuş ikame (hindiba, arpa) 21.01.",
        "<b>Her “çay” 09.02 değildir:</b> 09.02 yalnız Thea; aromalı ve kafeinsiz çay dahil. Maté 09.03; ada "
        "çayı, ıhlamur, nane 12.11; çay hülasası 21.01; karışık bitki çayı 21.06.",
        "<b>Not 2:</b> kebabe biberi ve 12.11’deki ürünler Fasıl 9 dışıdır. Baharat tadıyla çeşni verir; esas "
        "olarak parfümeri veya eczacılık bitkisi olan ürün 12.11’e gider.",
        "<b>Biber:</b> Piper ile kurutulmuş veya ezilmiş-öğütülmüş Capsicum ve Pimenta 09.04; taze biber 07.09. "
        "Jamaika biberi (Pimenta) 09.04, Malageta biberi 09.08.",
        "<b>Tohum ≠ ot:</b> kişniş, kimyon, anason, rezene tohumu 09.09; dere otu ve çemen tohumu 09.10; "
        "taze maydanoz, kişniş otu, dere otu Fasıl 7.",
        "<b>Bölüm ayrımı:</b> Fasıl 9 Bölüm II’dedir (bitkisel ürünler); şeker (17), kakao (18), meşrubat ve "
        "sirke (22) Bölüm IV’tedir.",
    ],
    karistirilan=[
        ["Bitki çayı için ada çayı", "12.11", "Thea değil; 09.02, 09.10, 07.12 çeldirici"],
        ["Tonka fasulyesi, ginseng kökü, nane", "12.11", "Baharat değil; parfümeri-eczacılık bitkisi"],
        ["Salep", "07.14", "Nişastalı kök yumru; baharat değil"],
        ["Instant kahve, çay hülasası", "21.01", "Hülasalar Fasıl 9’da değil"],
        ["Kebabe biberi (Piper cubeba)", "12.11", "Piper cinsi olsa da Fasıl 9 Not 2"],
    ],
)

# ---------------------------------------------------------------- FASIL 10 (C)
H[10] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; yalnız yanlış “eşya–fasıl” önermesini bulma sorusunda "
            "“Hububat 10. fasılda yer alır” doğru önerme olarak seçeneklerdeydi.",
    pozisyonlar=[
        ["10.01", "Buğday ve mahlut (durum buğdayı dahil)"],
        ["10.05", "Mısır; tatlı mısır hariç (Fasıl 7)"],
        ["10.06", "Pirinç: çeltik, kavuzsuz, parlatılmış, kırık"],
        ["10.08", "Karabuğday, darı, kuş yemi, kinoa, diğer hububat"],
    ],
    hap=[
        "<b>Not 1:</b> yalnız tane halindeki hububat (başakta veya sapta olabilir); kavuzu çıkarılmış veya "
        "işlenmiş tane Fasıl 11. İstisna: işlenmiş veya kırık pirinç 10.06, perikarpı alınmış kinoa 10.08.",
        "<b>Tohumluk ve taze hububat Fasıl 10’da kalır:</b> ekim amaçlı olsa da 12.09’a gitmez; tatlı mısır "
        "sebzedir (Not 2). Ön pişirilmiş veya şişirilmiş pirinç 19.04.",
        "<b>Darılar:</b> tane sorgum 10.07; darı ve kuş yemi 10.08; yem darıları 12.14; akdarı 14.04; "
        "hububat sapı ve kapçığı 12.13.",
    ],
    karistirilan=[
        ["Kavuzu çıkarılmış yulaf, yassılaştırılmış arpa", "11.04", "Not 1(B): işlenmiş tane Fasıl 10 dışı"],
        ["Taze tatlı mısır", "07.09", "Fasıl 10 Not 2; sebze sayılır"],
    ],
)

# ---------------------------------------------------------------- FASIL 11 (C)
H[11] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez doğrudan, 1 kez seçenek: Not 2 ölçütleri soruldu (nişasta, kül, elekten "
            "geçme oranı ve hububat cinsi kullanılır, şeker oranı kullanılmaz); eşleştirmede buğday unu 11.01 "
            "doğru verildi.",
    pozisyonlar=[
        ["11.01", "Buğday veya mahlut unu"],
        ["11.03", "Kaba un, irmik, kabaca öğütülmüş parçalar, pellet"],
        ["11.04", "Diğer işlenmiş taneler; hububat embriyoları"],
        ["11.08", "Nişastalar; inulin (modifiye nişasta 35.05)"],
    ],
    hap=[
        "<b>Not 2(A):</b> kuru maddede nişasta %45’ten fazla ve kül tablo sınırını (buğday-çavdar %2,5; arpa %3; "
        "yulaf %5; mısır %2; pirinç %1,6; karabuğday %4) aşmıyorsa Fasıl 11, aksi halde 23.02.",
        "<b>Not 2(B) – un eleği:</b> 315 mikrometre elekten en az %80 (mısır ve dane darıda 500 mikrometreden "
        "%90) geçen 11.01 / 11.02, geçmeyen 11.03 / 11.04. Embriyolar daima 11.04.",
        "<b>Not 3 – kaba un:</b> mısırda 2 mm, diğer hububatta 1,25 mm elekten en az %95 geçen ürün 11.03. "
        "Hazırlanmış unlar ve malt hülasası 19.01.",
    ],
    karistirilan=[
        ["Buğday kepeği", "23.02", "Nişasta-kül şartını sağlamayan değirmencilik kalıntısı"],
        ["Dekstrin, modifiye nişasta", "35.05", "11.08 yalnız doğal nişasta ve inulin"],
    ],
)

# ---------------------------------------------------------------- FASIL 12 (B)
H[12] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 kez doğrudan, 1 kez seçenek; odak 12.11: bitki çayı için ada çayı (09.02, 09.10, "
            "07.12 çeldirici) ve “tümü 12.11” sorusunda tonka fasulyesi–ginseng kökü–nane. “Aynı fasıl” "
            "sorusunda kopra, pamuk tohumu, şeker kamışı, ginseng kökü Fasıl 12 grubuydu.",
    pozisyonlar=[
        ["12.02", "Yer fıstığı (kavrulmamış); kavrulmuşu 20.08"],
        ["12.03", "Kopra (yağ için kurutulmuş Hindistan cevizi içi)"],
        ["12.07", "Diğer yağlı tohumlar: susam, haşhaş, pamuk, hardal"],
        ["12.09", "Ekime mahsus tohumlar (Not 3 listesi)"],
        ["12.11", "Parfümeri-eczacılık bitkileri: nane, adaçayı, ginseng, tonka"],
        ["12.12", "Keçiboynuzu, deniz otu, şeker pancarı-kamışı, kayısı çekirdeği"],
    ],
    hap=[
        "<b>Not 4 – 12.11 listesi:</b> fesleğen, zembil çiçeği, ginseng, çördük otu, meyan kökü, her türlü nane, "
        "biberiye, sedef otu, adaçayı, pelin. İlaç (Fasıl 30), kozmetik (Fasıl 33), 38.08 ürünleri hariç.",
        "<b>Daha özel pozisyon 12.11’i yener:</b> vanilya, tarçın, karanfil, kişniş, kimyon, anason, zencefil, "
        "kekik (Fasıl 9) ve paraguay çayı (09.03) eczacılıkta kullanılsa da Fasıl 9’da kalır.",
        "<b>Not 1:</b> 12.07 palm meyvesi-çekirdeği, pamuk, Hint yağı, susam, hardal, aspir, haşhaş tohumu ve "
        "shea fıstığını kapsar; 08.01–08.02 ürünleri ve zeytin hariç.",
        "<b>Not 3 – 12.09:</b> pancar, çim, süs çiçeği, sebze, orman ve meyve ağacı, fiğ (Vicia faba hariç), "
        "acı bakla tohumu. Ekimlik olsa da hububat, baklagil sebze, baharat, 12.01–12.07 ve 12.11 hariç.",
        "<b>Bitki çayı ve unlar:</b> tek türden bitki 12.11, değişik türlerin karışımı 21.06. Yağı alınmamış "
        "yağlı tohum unu 12.08, yağı alınmış küspe 23.04–23.06.",
    ],
    karistirilan=[
        ["Kişniş, kimyon, anason tohumu", "09.09", "Baharat; “tümü 12.11” sorusunda çeldirici"],
        ["Paraguay çayı (maté)", "09.03", "Ihlamur ve adaçayıyla verilse de 12.11 değil"],
        ["Kuş yemi, tane darı", "10.08", "Hububat; fiğ ise 12.14 yem bitkisi"],
    ],
)

# ---------------------------------------------------------------- FASIL 13 (C)
H[13] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; ham gliserin sorusunda 13.01 çeldirici seçenekti "
            "(doğrusu 15.20).",
    pozisyonlar=[
        ["13.01", "Lak; tabii sakız, reçine, sakız-reçine, yağ reçine"],
        ["13.02", "Bitkisel özsu, hülasa; pektin; agar-agar, kıvam vericiler"],
    ],
    hap=[
        "<b>Not 1 – 13.02’de:</b> meyan kökü, pire otu, şerbetçi otu, aloe ve afyon hülasaları. Hariç: kahve-"
        "çay-maté hülasası 21.01, malt hülasası 19.01, uçucu yağ ve rezinoit Fasıl 33.",
        "<b>Eşikler:</b> %10’dan fazla sakkarozlu veya şekerleme halindeki meyan kökü hülasası 17.04; en az %50 "
        "alkaloidli haşhaş samanı konsantresi 29.39.",
        "<b>“Sakız” sanılanlar:</b> tabii kauçuk, balata, güta-perka, çıkıl 40.01 (Not 1); amber 25.30; "
        "kolofan 38.06.",
    ],
    karistirilan=[
        ["Çıkıl, tabii kauçuk", "40.01", "“Sakız” adına rağmen Fasıl 13 Not 1 ile hariç"],
        ["Çay hülasası", "21.01", "Not 1: kahve, çay, maté hülasaları 21.01"],
    ],
)

# ---------------------------------------------------------------- FASIL 14 (C)
H[14] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı, seçeneklerde de yer almadı; bilgi Bölüm II kapsamı ve "
            "örgü-sepet eşyası (Fasıl 46) ile hammadde ayrımında gerekir.",
    pozisyonlar=[
        ["14.01", "Örgü maddeleri: bambu, Hint kamışı, rafya, söğüt"],
        ["14.04", "Başka yerde yer almayan bitkisel ürünler: linter, kapok"],
    ],
    hap=[
        "<b>Not 1:</b> esas olarak mensucatta kullanılan bitkisel maddeler ve lifler, nasıl hazırlanmış olursa "
        "olsun Fasıl 14 dışıdır (Bölüm XI).",
        "<b>Not 2–3:</b> yarılmış, cilalı, boyanmış, yanmaz bambu 14.01’de; yonga 44.04, odun yünü 44.05, "
        "hazır fırça başı 96.03 hariç.",
        "<b>Hammadde → eşya:</b> örgü 46.01, sepet 46.02. İşlenmemiş hububat sapı 12.13; temizlenmiş, "
        "beyazlatılmış veya boyanmış sap 14.01.",
    ],
    karistirilan=[
        ["Bambudan sepet", "46.02", "Hammadde değil, sepetçi eşyası"],
        ["Pamuk linteri", "14.04", "Pamuk (Fasıl 52) değil; çok kısa lifler"],
    ],
)

# ---------------------------------------------------------------- FASIL 15 (C)
H[15] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez doğrudan, 1 kez seçenek: ham gliserin ile gliserinli su ve lesivler 15.20 "
            "soruldu; sınai yağ alkolleri sorusunda 15.18 ve 15.20 çeldiriciydi (doğrusu 38.23).",
    pozisyonlar=[
        ["15.17", "Margarin; yenilen yağ karışımları ve müstahzarları"],
        ["15.18", "Kimyasal değiştirilmiş yağlar; yenilmeyen karışımlar"],
        ["15.20", "Ham gliserin; gliserinli sular ve lesivler"],
        ["15.21", "Bitkisel mumlar, balmumu, ispermeçet (karıştırılmamış)"],
    ],
    hap=[
        "<b>Bölüm III = yalnız Fasıl 15</b> (bölüm notu yok). Not 1 hariç: eritilmemiş domuz-kümes yağı 02.09, "
        "kakao yağı 18.04, %15’ten fazla 04.05 ürünü içeren yenilen müstahzar, yağ asitleri ve VI. Bölüm ürünleri.",
        "<b>Gliserin ve yağ alkolü:</b> ham gliserin (saflık %95’ten az) 15.20, %95 ve üzeri 29.05. Sınai yağ "
        "asitleri ve yağ alkolleri 38.23; sabun 34.01.",
        "<b>Zeytin ve karışımlar:</b> çözücüyle elde edilen zeytin yağı 15.10 (Not 2); yenilen karışım 15.17, "
        "yenilmeyen 15.18; yalnız denatüre edilmiş yağ kendi pozisyonunda kalır (Not 3).",
    ],
    karistirilan=[
        ["Sınai yağ alkolleri", "38.23", "Not 1: VI. Bölüm ürünü; 15.18 veya 15.20 değil"],
        ["Kakao yağı", "18.04", "Bitkisel yağ olsa da Fasıl 15 Not 1(b)"],
    ],
)

# ---------------------------------------------------------------- FASIL 16 (B)
H[16] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 kez doğrudan, 3 kez seçenek: “IV. Bölüm, 16. Fasıl, 5. pozisyon” numaralandırma "
            "sorusu (16.05). Karidesli mantı setinde karides müstahzarı, kurutulmuş tuzlu çekirgede 16.02 "
            "çeldirici oldu (doğruları 19.02 ve 04.10).",
    pozisyonlar=[
        ["16.01", "Sosisler ve benzerleri (et, sakatat, kan, böcek)"],
        ["16.02", "Diğer hazır et, sakatat, kan, böcek müstahzarları"],
        ["16.03", "Et, balık, su omurgasızı hülasa ve suları"],
        ["16.04", "Hazır-konserve balık; balık sosisi; havyar"],
        ["16.05", "Hazır-konserve kabuklu, yumuşakça, su omurgasızları"],
    ],
    hap=[
        "<b>Bölüm IV = Fasıl 16–24</b> (gıda sanayii, içki, tütün). Bölüm notu: pellet = doğrudan sıkıştırılmış "
        "veya en çok %3 bağlayıcılı topak. Kahve, çay, baharat (Fasıl 9) Bölüm II’dedir.",
        "<b>Not 2 – %20 kuralı:</b> ağırlıkça %20’den fazla sosis, et, sakatat, kan, böcek, balık, kabuklu veya "
        "yumuşakça içeren gıda müstahzarı Fasıl 16’dadır; pozisyonu ağırlıkça fazla olan bileşen belirler.",
        "<b>%20’nin istisnaları:</b> 19.02’deki doldurulmuş makarna (mantı, ravioli), 21.03 soslar, 21.04 "
        "çorbalar ve homojenize bileşik müstahzarlar; et oranı ne olursa olsun kendi yerinde kalır.",
        "<b>Not 1:</b> Fasıl 2–3’te, Fasıl 4 Not 6’da veya 05.04’te sayılan işlemleri görmüş ürün Fasıl 16’ya "
        "girmez: tuzlu-kurutulmuş böcek 04.10, kabuğunda haşlanmış karides 03.06.",
        "<b>Sosis ve et suyu:</b> 16.01 et, sakatat, kan veya böcek sosisi; balık sosisi 16.04. Çiğ etten "
        "pres suyu ve hülasa 16.03; çorba niteliğindeki et suyu 21.04.",
    ],
    karistirilan=[
        ["Karidesli mantı + çorba tozu seti", "19.02", "Doldurulmuş makarna; %20 kuralı uygulanmaz"],
        ["Kurutulmuş, tuzlanmış yenilebilir çekirge", "04.10", "Fasıl 4 Not 6 işlemi; 16.02 değil"],
        ["Kabuğunda buharda pişmiş karides", "03.06", "Fasıl 3 işlemi; 16.05 değil"],
    ],
)

# ---------------------------------------------------------------- FASIL 17 (B)
H[17] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 kez doğrudan, 1 kez seçenek: tabii balla karışık olsun olmasın diyabetik suni bal "
            "17.02 soruldu (04.09, 09.05, 19.05 çeldirici); ciklet ve şeker, Bölüm IV kapsamı sorularında geçti.",
    pozisyonlar=[
        ["17.01", "Katı kamış-pancar şekeri; kimyaca saf sakkaroz"],
        ["17.02", "Laktoz, glikoz, fruktoz; aromasız şurup; suni bal, karamel"],
        ["17.03", "Melaslar (şeker ekstraksiyonu-rafinajı yan ürünü)"],
        ["17.04", "Kakaosuz şeker mamulleri: ciklet, lokum, beyaz çikolata"],
    ],
    hap=[
        "<b>Not 1:</b> kakao içeren şeker mamulü 18.06; sakkaroz, laktoz, maltoz, glikoz ve fruktoz dışındaki "
        "kimyaca saf şekerler 29.40; ilaçlar Fasıl 30.",
        "<b>Bal:</b> yalnız katkısız tabii bal 04.09; suni bal, tabii balla karışık olsa da 17.02.",
        "<b>Beyaz çikolata 17.04:</b> kakao yağı kakao sayılmaz; çok az kakao bile şekerlemeyi 18.06’ya "
        "götürür.",
        "<b>Katı ↔ şurup:</b> aroma veya renk katılmış katı şeker 17.01’de kalır; aromalı veya renkli şeker "
        "şurubu 21.06. Sorbitollü (şekersiz) sakız ve şekerleme 21.06.",
    ],
    karistirilan=[
        ["Diyabetik suni bal (tabii balla karışık)", "17.02", "04.09 yalnız katkısız tabii bal"],
        ["Çikolata kaplı badem şekeri", "18.06", "Kakao oranı ne olursa olsun 18.06"],
        ["Reçel, marmelat", "20.07", "Şeker mamulü değil; şekerlenmiş meyve 20.06"],
    ],
)

# ---------------------------------------------------------------- FASIL 18 (C)
H[18] = dict(
    kademe="C",
    sinavda="Son 5 sınavda doğrudan sorulmadı; “IV. Bölüm kapsamında değildir” sorusunda kakao Bölüm IV "
            "eşyası olarak seçenekteydi (cevap kahve, Bölüm II).",
    pozisyonlar=[
        ["18.03", "Kakao hamuru (şekersiz; yağı alınmış olabilir)"],
        ["18.04", "Kakao yağı (Fasıl 15’e girmez)"],
        ["18.05", "Şekersiz kakao tozu"],
        ["18.06", "Çikolata ve kakaolu diğer gıda müstahzarları"],
    ],
    hap=[
        "<b>Not 2:</b> kakaolu şeker mamulleri ve diğer kakaolu gıdalar 18.06. Not 1 hariç: %20’den fazla "
        "etli-balıklı (Fasıl 16), 04.03, 19.01, 19.02, 19.04, 19.05, 21.05, 22.02, 22.08, 30.03, 30.04.",
        "<b>Fasıl 19 eşikleri (yağsız baz):</b> un-malt esaslıda %40’tan, süt esaslıda %5’ten az kakaolu "
        "müstahzar 19.01; kavrulmuş hububatta %6’dan fazla kakao veya tam çikolata kaplama 18.06.",
        "<b>Kakao sayılmayan kakao yağı:</b> beyaz çikolata 17.04. Kakaolu dondurma 21.05, çikolata kaplı "
        "bisküvi 19.05.",
    ],
    karistirilan=[
        ["Beyaz çikolata", "17.04", "Kakao yağı kakao sayılmaz"],
        ["Kakaolu dondurma", "21.05", "Not 1(b); kakao oranı önemsiz"],
    ],
)

# ---------------------------------------------------------------- FASIL 19 (B)
H[19] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 kez doğrudan, 2 kez seçenek: dondurulmuş şehriye Fasıl 19; karidesli mantı ve "
            "çorba tozu seti doldurulmuş makarna olarak 19.02 (GYK 1, 2(b), 3(b), 6). Eşleştirmede kuskus "
            "19.02 doğru verildi.",
    pozisyonlar=[
        ["19.01", "Malt hülasası; un, nişasta, süt esaslı müstahzarlar"],
        ["19.02", "Makarna (pişmiş, doldurulmuş, hazırlanmış olabilir); kuskus"],
        ["19.03", "Tapyoka ve nişastadan benzerleri"],
        ["19.04", "Gevrek, patlamış tane, müsli, bulgur, ön pişmiş pirinç"],
        ["19.05", "Ekmek, bisküvi, kek, gofret, pişmiş pizza, hosti"],
    ],
    hap=[
        "<b>Doldurulmuş makarna istisnası:</b> etli veya karidesli mantı, ravioli, dolgu oranı %20’yi aşsa da "
        "19.02’dedir (Fasıl 16 Not 2, Fasıl 19 Not 1(a)).",
        "<b>Kakao eşikleri (yağsız baz):</b> 19.01’de un-malt esaslıda %40’tan, süt esaslıda %5’ten az; 19.04’te "
        "en çok %6 ve tamamen çikolata kaplı olmayan; 19.05’te sınır yok.",
        "<b>Not 2 – 19.01’de “un”:</b> Fasıl 11 hububat unları ve her fasıldan bitkisel un; kurutulmuş sebze "
        "(07.12), patates (11.05) ve kuru baklagil (11.06) unları hariç.",
        "<b>Not 4:</b> 19.04’te “başka şekilde hazırlanmış” = Fasıl 10–11’deki işlemlerin ötesi; bulgur ve ön "
        "pişmiş pirinç 19.04. Hayvanlar için bisküvi 23.09 (Not 1(b)).",
        "<b>Pizza ve dondurma:</b> pişmemiş pizza 19.01, ön pişmiş veya pişmiş 19.05. Süt esaslı dondurma tozu "
        "19.01, dondurmanın kendisi 21.05.",
    ],
    karistirilan=[
        ["Ağırlıkça %20’den fazla etli makarna yemeği", "16.02", "İstisna yalnız doldurulmuş makarnaya"],
        ["Tamamen çikolata kaplı mısır gevreği", "18.06", "Fasıl 19 Not 3; 19.04 değil"],
        ["Köpek bisküvisi", "23.09", "Fasıl 19 Not 1(b); hayvan için hazırlanmış"],
    ],
)

# ---------------------------------------------------------------- FASIL 20 (C)
H[20] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 2 kez doğrudan, 1 kez seçenek: “hangi eşleştirme yanlış” kalıbında reçel 20.08 "
            "verildi (doğrusu 20.07); 20.08’in alt ayrım ölçütleri soruldu (ağırlık, şeker oranı, ilave alkol; "
            "Brix değeri 20.09 meyve sularının ölçütü).",
    pozisyonlar=[
        ["20.01", "Sirke veya asetik asitle hazırlanmış sebze-meyve (turşu)"],
        ["20.07", "Pişirilerek yapılmış reçel, jöle, marmelat, püre"],
        ["20.08", "Diğer meyve hazırlıkları: kavrulmuş fındık, fıstık ezmesi"],
        ["20.09", "Fermente edilmemiş meyve-sebze suları (alkol ≤ %0,5)"],
    ],
    hap=[
        "<b>Not 1 fasıl dışı:</b> Fasıl 7, 8, 11 işlemlerini görmüş ürünler, bitkisel yağlar, %20’den fazla "
        "etli-balıklı müstahzarlar (Fasıl 16), ekmekçilik ürünleri (19.05), homojenize bileşik müstahzarlar (21.04).",
        "<b>Eşikler:</b> kuru maddesi %7 ve üzeri domates suyu 20.02 (Not 4); 20.09’da alkol hacimce %0,5’i "
        "geçmez (Not 6), 20 °C’de ölçülür.",
        "<b>Not 2:</b> şekerleme (17.04) veya çikolata (18.06) haline getirilmiş meyve jölesi, ezmesi ve bademli "
        "şekerler 20.07–20.08 dışıdır. Şurupta meyve 20.08, şekerlenmiş meyve 20.06.",
    ],
    karistirilan=[
        ["Reçel", "20.07", "Pişirilerek hazırlanmış; 20.08 değil"],
        ["Domates ketçabı", "21.03", "Sos; domates salçası ise 20.02"],
    ],
)

# ---------------------------------------------------------------- FASIL 21 (B)
H[21] = dict(
    kademe="B",
    sinavda="Son 5 sınavda doğrudan sorulmadı, 5 kez seçenekte: “aynı fasıl” sorularında dondurma, ketçap, "
            "canlı maya, çay hülasası ve bira mayası, kavrulmuş hindiba Fasıl 21 grubuydu; mantı setinde çorba "
            "(21.04) çeldirici, et suyu 21.04 doğru eşleştirmeydi.",
    pozisyonlar=[
        ["21.01", "Kahve-çay hülasası, instant kahve; kavrulmuş hindiba"],
        ["21.02", "Mayalar (canlı, cansız); hazır kabartma tozları"],
        ["21.03", "Soslar, ketçap, mayonez; hardal unu, hazır hardal"],
        ["21.04", "Çorbalar, et suları; homojenize bileşik müstahzarlar"],
        ["21.05", "Dondurma ve yenilen buzlar (kakaolu olsa da)"],
        ["21.06", "Başka yerde yer almayan gıda müstahzarları"],
    ],
    hap=[
        "<b>Not 1 fasıl dışı:</b> 07.12 sebze karışımları; kahve içeren kavrulmuş ikame (09.01); aromalı çay "
        "(09.02); 09.04–09.10 baharatları; ilaç olarak hazırlanmış maya (Fasıl 30); hazır enzimler (35.07).",
        "<b>%20 kuralı sos ve çorbaya işlemez:</b> etli bolonez sosu 21.03’te, etli çorba 21.04’te kalır; "
        "diğer %20’den fazla etli-balıklı müstahzarlar Fasıl 16.",
        "<b>Not 3 – homojenize bileşik:</b> iki veya daha fazla temel bileşen (et, balık, sebze, meyve vb.); "
        "bebek, küçük çocuk veya diyet amaçlı, net en çok 250 gr’lık perakende kapta → 21.04.",
        "<b>Kahve ikamesi:</b> kahvesiz kavrulmuş ikame (hindiba, arpa) 21.01; kahve içeren ikame 09.01, "
        "ama onun hülasası 21.01 (Not 2).",
        "<b>Maya:</b> canlı veya cansız maya 21.02, otolize maya 21.06; mikroorganizma kültürü 30.02. "
        "İçilmez yemeklik şarap 21.03; sorbitollü sakız 21.06.",
    ],
    karistirilan=[
        ["Aromalı (bergamutlu) çay", "09.02", "Not 1(c); çay hülasası ise 21.01"],
        ["Hazır enzim, et yumuşatıcı", "35.07", "Not 1(g); maya değil"],
        ["Süt esaslı dondurma tozu", "19.01", "Dondurmanın kendisi 21.05"],
    ],
)

# ---------------------------------------------------------------- FASIL 22 (B)
H[22] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 1 kez doğrudan, 3 kez seçenek: “hangisi 22. fasılda değildir” kalıbında deniz suyu "
            "(25.01) sirke, kar, bal şarabı, alkolsüz bira arasından seçildi; sirke ve meşrubat Bölüm IV, "
            "sıralamada içki → sigara.",
    pozisyonlar=[
        ["22.01", "Sade sular, maden suyu, soda; buz ve kar"],
        ["22.02", "Tatlandırılmış-aromalı sular; alkolsüz içecekler, alkolsüz bira"],
        ["22.06", "Diğer fermente içkiler: elma şarabı, bal şarabı, sake"],
        ["22.07", "Tağyirsiz etil alkol ≥ %80; tağyirli alkol"],
        ["22.08", "Tağyirsiz etil alkol %80’den az; damıtık içkiler, likörler"],
        ["22.09", "Sirke ve asetik asitten sirke ikameleri"],
    ],
    hap=[
        "<b>Not 3 – alkolsüz içecek:</b> alkol derecesi hacimce %0,5’i geçmeyen içecek (22.02). Alkol derecesi "
        "20 °C’de ölçülür (Not 2; Fasıl 20 ve 21 için de geçerli).",
        "<b>Not 1 fasıl dışı:</b> deniz suyu 25.01; damıtılmış-iletken su 28.53; %10’dan fazla asetik asitli "
        "çözelti 29.15; içilmez yemeklik ürün genellikle 21.03 (sirke hariç); ilaç Fasıl 30; parfümeri Fasıl 33.",
        "<b>%80 eşiği:</b> tağyir edilmemiş etil alkol hacimce %80 ve üzeri 22.07, altı 22.08; tağyir edilmiş "
        "alkol her derecede 22.07.",
        "<b>Kar ve buz 22.01’dedir:</b> tabii kar dahil; kuru buz 28.11, yenilen buzlar 21.05. Şekerli veya "
        "aromalı maden suyu 22.02.",
        "<b>Şarap ayrımı:</b> taze üzüm şarabı ve %0,5’i aşan şıra 22.04; vermut 22.05; kuru üzüm, elma, bal "
        "şarabı 22.06. Fermente olmamış şıra 20.09.",
    ],
    karistirilan=[
        ["Deniz suyu", "25.01", "Not 1(b); 22.01 değil"],
        ["Alkolsüz bira (≤ %0,5)", "22.02", "Malttan olsa da 22.03 değil"],
        ["Seyreltilmemiş meyve suyu", "20.09", "Fermente değil; limonata ise 22.02"],
    ],
)

# ---------------------------------------------------------------- FASIL 23 (C)
H[23] = dict(
    kademe="C",
    sinavda="Son 5 sınavda 1 kez: “aynı bölüm” sorusunda şarap tortusu (23.07) ciklet ve tütünle birlikte "
            "Bölüm IV eşyası olarak geçti; başka seçenekte yer almadı.",
    pozisyonlar=[
        ["23.01", "İnsana elverişsiz et-balık unları, pelletleri; kıkırdak"],
        ["23.02", "Hububat kepeği ve değirmencilik kalıntıları"],
        ["23.07", "Şarap tortusu; ham tartar"],
        ["23.09", "Hayvan yemi müstahzarları: kedi-köpek maması, premiks"],
    ],
    hap=[
        "<b>Not 1:</b> ana maddenin esas özelliklerini kaybettirecek derecede işlenmiş, başka yerde yer almayan "
        "hayvan gıdası ürünleri 23.09’dadır.",
        "<b>Kalıntının kaynağı:</b> nişasta-şeker-bira-damıtma artıkları 23.03 (melas 17.03); küspe: soya 23.04, "
        "yer fıstığı 23.05, diğer bitkisel yağlar 23.06.",
        "<b>Kepek ve unlar:</b> Fasıl 11 Not 2(A) nişasta-kül şartını sağlamayan öğütme ürünü 23.02; insana "
        "uygun et unu 02.10, balık unu 03.09.",
    ],
    karistirilan=[
        ["Etli kedi-köpek maması, köpek bisküvisi", "23.09", "Hayvan için hazırlanmış; Fasıl 16 veya 19 değil"],
        ["Krem tartar", "29.18", "Ham tartar 23.07; krem tartar hariç"],
    ],
)

# ---------------------------------------------------------------- FASIL 24 (B)
H[24] = dict(
    kademe="B",
    sinavda="Son 5 sınavda 2 kez doğrudan, 2 kez seçenek: boşluk doldurmada e-sigara 85.43, kartuşu 24.04, "
            "sigara 24.02, sigara kağıdı 48.13; 30. fasıl sorusunda nikotinli bant (24.04) çeldirici; Bölüm IV "
            "ve sıralama (içki → sigara → çakmak) soruları.",
    pozisyonlar=[
        ["24.01", "Yaprak tütün ve tütün döküntüleri"],
        ["24.02", "Puro, sigarillo, sigara (tütünsüz olanlar dahil)"],
        ["24.03", "Diğer mamul tütün: pipo, nargile, çiğneme tütünü, enfiye"],
        ["24.04", "Yanmadan solunan ürünler; nikotinli bant, sakız, e-sıvı"],
    ],
    hap=[
        "<b>Öncelik kuralı:</b> hem 24.04’e hem bu faslın başka pozisyonuna girebilen ürün 24.04’te; ısıtılan "
        "tütün çubuğu 24.03 değil 24.04.",
        "<b>“Yanma olmadan solunan”:</b> ısı yoluyla veya diğer yollarla (kimyasal, ultrasonik) yanmadan "
        "soluma; e-sıvı, kartuş ve tek kullanımlık e-sigara 24.04.",
        "<b>Cihaz ↔ sarf:</b> yeniden doldurulabilir e-sigara cihazı 85.43, sıvı ve kartuşu 24.04; sigara "
        "kağıdı 48.13; pipo ve ağızlık 96.14; çakmak 96.13.",
        "<b>Fasıl notu:</b> tıbbi sigaralar Fasıl 30; ama sigarayı bırakmaya yardımcı nikotinli tablet, sakız "
        "ve bant Fasıl 30 değil 24.04’tür.",
        "<b>Nikotinin kendisi</b> (tabii veya sentetik) 29.39; tütün hülasası 24.03. Tütün-ikame karışımından "
        "sigara, oran ne olursa olsun 24.02.",
    ],
    karistirilan=[
        ["Sigarayı bırakma için nikotinli bant", "24.04", "Fasıl 30 Not 1 ile ilaç dışı"],
        ["Doldurulabilir e-sigara cihazı", "85.43", "Cihaz; kartuşu ve sıvısı 24.04"],
        ["Sigara kağıdı (defter, boru)", "48.13", "Tütün içermez; kağıt faslı"],
    ],
)


def main():
    os.makedirs(OUT, exist_ok=True)
    for n, d in sorted(H.items()):
        rec = {"tur": "hap", "fasil": n, "kademe": d["kademe"], "sinavda": d["sinavda"],
               "pozisyonlar": d["pozisyonlar"], "hap": d["hap"], "karistirilan": d["karistirilan"]}
        p = os.path.join(OUT, f"fasil_{n:02d}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
        print("yazıldı", p)


if __name__ == "__main__":
    main()
