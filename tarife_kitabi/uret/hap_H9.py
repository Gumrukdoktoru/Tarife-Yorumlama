#!/usr/bin/env python3
"""Hap bilgi sayfaları: Fasıl 93–97 (grup H9)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "hap")

HAP = {}

# ------------------------------------------------------------------ FASIL 93
HAP[93] = {
    "tur": "hap",
    "fasil": 93,
    "kademe": "B",
    "sinavda": "Son 5 sınavda 2 kez doğrudan: ok ve yayın 93. Fasılda sınıflandırılmadığı (av tüfeği, mızrak, "
               "süngü, kılıç kını içeride) ve av tüfeği ile şekline uygun mahfazasının GYK 5(a) ile tüfeğin "
               "pozisyonunda kaldığı. Tabanca “aynı bölüm” sorusunda (Bölüm XIX), 93.05 de seçenekte yer aldı.",
    "pozisyonlar": [
        ["93.01", "Harp silahları: top, havan, makinalı tüfek-tabanca"],
        ["93.02", "Revolver, tabanca; elde tutulur, patlayıcıyla mermi atar"],
        ["93.03", "Av-spor tüfeği, kuru sıkı, işaret tabancası, zıpkın tüfeği"],
        ["93.05", "93.01–93.04 parçası: namlu, şarjör, dipçik, susturucu"],
        ["93.06", "Mühimmat: fişek, saçma, bomba, mayın, torpil, parçaları"],
        ["93.07", "Kılıç, süngü, mızrak, hançer ve kınları"],
    ],
    "hap": [
        "<b>Fasıl dışı (Not 1):</b> Fasıl 36 eşyası (kapsül, fünye, işaret fişeği), zırhlı savaş aracı 87.10, "
        "ayrı gelen dürbün (Fasıl 90), ok, yay, eskrim kılıcı, oyuncak silah (Fasıl 95), koleksiyon ve antika "
        "(97.05 / 97.06).",
        "<b>Silahlı taşıt yine taşıttır:</b> tank 87.10, harp gemisi 89.06, askeri uçak Fasıl 88, zırhlı tren "
        "Fasıl 86; bunlar için ayrı gelen top ve makinalı tüfek 93.01.",
        "<b>Her tabanca 93.02 değildir:</b> makinalı tabanca 93.01; kuru sıkı, yalnız işaret fişeği atan ve "
        "sürgülü hayvan öldürme tabancası 93.03; havalı, gazlı, yaylı tabanca ile cop, muşta, sapan 93.04.",
        "<b>Mahfaza ve dürbün:</b> tüfekle birlikte gelen, şekline uygun mahfaza tüfeğin pozisyonunda (GYK 5(a)); "
        "ayrı gelen kılıf 42.02. Dürbün silaha takılı veya silahla gelirse silahla, ayrıysa 90.13.",
        "<b>Kesici silah 93.07:</b> kılıç, pala, süngü, mızrak, hançer ve kınları seremoni, dekorasyon veya "
        "tiyatro için yapılmış olsa da buradadır; kılıçlı baston da 93.07 (Fasıl 66 değil).",
    ],
    "karistirilan": [
        ["Okçuluk oku ve yayı; eskrim kılıcı", "95.06", "Not 1(e); av tüfeği, mızrak, süngü, kın Fasıl 93"],
        ["İşaret fişeği; kapsül, fünye", "36.04 / 36.03", "Patlayıcı ürün; fişeği atan tabanca 93.03"],
        ["Oyuncak sapan, oyuncak tabanca", "95.03", "Kuşlara atış için yapılan sapan 93.04"],
    ],
}

# ------------------------------------------------------------------ FASIL 94
HAP[94] = {
    "tur": "hap",
    "fasil": 94,
    "kademe": "B",
    "sinavda": "Son 5 sınavda 3 kez doğrudan: demonte masa ve 2 sandalyeden oluşan perakende setin GYK 1, 2(a), "
               "3(c) ve 6 ile 94.03’te; elektrikli çelengin 94.05’te (95.04, 85.39 çeldirici); dişçi koltuğunun "
               "Bölüm XX’de olduğu. Ameliyat masası ve avize “aynı bölüm” sorusunda seçenekti.",
    "pozisyonlar": [
        ["94.01", "Oturma mobilyası; yatağa dönüşen çekyat dahil"],
        ["94.02", "Tıbbi, dişçi, veteriner mobilyası; döner-yükselir-yatar berber koltuğu"],
        ["94.03", "Diğer mobilya: masa, dolap, karyola, beşik, okul sırası"],
        ["94.04", "Somya; yaylı, doldurulmuş, gözenekli yatak, yorgan, uyku tulumu"],
        ["94.05", "Lamba, avize, projektör, elektrikli çelenk; sabit ışıklı tabela"],
        ["94.06", "Prefabrik yapılar; çelik modüler yapı birimleri"],
    ],
    "hap": [
        "<b>Mobilya testi (Not 2):</b> eşya zemine konularak kullanılmalıdır. Asılsa veya duvara tutturulsa da "
        "mobilya sayılanlar: dolap, raflı ve ünite mobilya, yatak, oturma mobilyası. Duvar askılığı mobilya değildir.",
        "<b>Demonte ve takım (GYK 2(a), 3(c)):</b> bütün parçalarıyla gelen demonte mobilya monte edilmiş gibi; "
        "masa ve sandalyelerden oluşan perakende sette özsel nitelik belirlenemezse numara sırasına göre son "
        "pozisyon 94.03.",
        "<b>Parça sayılmaz (Not 3):</b> diğer parçalarla birleşmemiş cam, ayna, mermer levha kendi faslında; "
        "ayrı gelen yaylı veya doldurulmuş koltuk minderi 94.04. Hava-su ile şişirilen yatak Fasıl 39, 40, 63.",
        "<b>94.05 her madde, her ışık kaynağı:</b> mum, gaz, petrol, elektrikli lamba ve avize. Ampul ve LED "
        "kaynağı 85.39, taşıt-bisiklet lambası 85.12, pilli el feneri 85.13, mum 34.06.",
        "<b>Fasıl dışı (Not 1):</b> yere konan boy aynası 70.09, kasa 83.03, buzdolabı 84.18, dikiş makinesi "
        "mobilyası 84.52, bilardo masası 95.04, oyuncak mobilya 95.03, tripod 96.20, saat Fasıl 91.",
    ],
    "karistirilan": [
        ["Dişçilik cihazlarıyla birleşik dişçi koltuğu", "90.18", "Not 1; cihazsız dişçi koltuğu 94.02"],
        ["Elektrikli çelenk (Noel ağacı ışıkları)", "94.05", "Fasıl 95 Not 1(u); 95.04 / 95.05 değil"],
        ["Radyoloji masası", "90.22", "94.02 hariç tutar; ameliyat masası 94.02"],
    ],
}

# ------------------------------------------------------------------ FASIL 95
HAP[95] = {
    "tur": "hap",
    "fasil": 95,
    "kademe": "A",
    "sinavda": "Son 5 sınavda 3 kez doğrudan: üç tekerlekli bisikletin 95.03’te olduğu (87.12 çeldirici), “gezici "
               "hayvan sergisi ile aynı fasıl” kalıbında üç tekerlekli bisiklet (heykel, zooloji koleksiyonu, "
               "tiyatro dekoru, kamp çadırı çeldirici) ve ok-yayın 95.06’ya gittiği. Elektrikli çelenk (95.04 "
               "çeldirici) ve mantar dart tablası seçeneklerde yer aldı.",
    "pozisyonlar": [
        ["95.03", "Tekerlekli oyuncak: üç tekerlekli bisiklet, skuter, pedallı araba"],
        ["95.03", "Oyuncak bebek ve arabası, eğlencelik model, bulmaca"],
        ["95.04", "Video oyun konsolu; ödeme aracıyla çalışan eğlence makinesi"],
        ["95.04", "Bilardo, kumarhane masası, oyun kağıdı, satranç, dart, bowling"],
        ["95.05", "Bayram, karnaval, Noel eşyası; sihirbazlık, şaka eşyası"],
        ["95.06", "Artık spor eşyası: jimnastik, kayak, golf, raket, top"],
        ["95.06", "Paten takılı bot, kızak, yüzme havuzu, okçuluk ok-yayı"],
        ["95.07", "Olta takımı, kepçe, kelebek ağı, yapma av kuşu"],
        ["95.08", "Gezici sirk-hayvan sergisi-tiyatro; lunapark, su parkı, panayır"],
    ],
    "hap": [
        "<b>Not 1 – fasıl dışı (1):</b> mum 34.06, havai fişek 36.04, spor çantası 42.02, tekstil spor ve "
        "karnaval giyimi Fasıl 61, 62, spor ayakkabısı Fasıl 64, spor başlığı Fasıl 65, bayrak-yelken Fasıl 63.",
        "<b>Not 1 – fasıl dışı (2):</b> çocuk bisikleti 87.12, insansız hava taşıtı 88.06, kano-kayık Fasıl 89, "
        "spor gözlüğü 90.04, düdük 92.08, silah Fasıl 93, elektrikli çelenk 94.05, tripod 96.20; çadır ve eldiven "
        "maddesine göre.",
        "<b>Bisiklet ayrımı:</b> üç tekerlekli çocuk bisikleti 95.03 (pozisyon metninde adıyla); diğer çocuk "
        "bisikletleri 87.12. Gerçek bebek arabası 87.15, oyuncak bebek arabası 95.03.",
        "<b>Spor taşıtı ve paten:</b> Bölüm XVII spor taşıtları fasıl dışı, ama kızak ve yarış kızağı 95.06. "
        "Buz veya tekerlekli paten takılı bot 95.06; patensiz spor ayakkabısı Fasıl 64.",
        "<b>Aksam (Not 3):</b> yalnız veya esas itibarıyla fasıl eşyasıyla kullanılan aksam eşyanın "
        "pozisyonunda; ama elektrik motoru 85.01, transformatör 85.04, uzaktan kumanda 85.26 / 85.43 ve genel "
        "kullanım parçaları fasıl dışı.",
        "<b>Not 4 ve Not 5:</b> başka eşyayla birleşik oyuncak, perakende satış için hazırlanmış ve oyuncağın "
        "mümeyyiz vasfını taşıyorsa 95.03. Yalnız hayvanlar için tasarlanmış oyuncak 95.03’e girmez.",
        "<b>95.08 tanımı (Not 6):</b> eğlence parkı gezinti eşyası kişiyi sabit veya sınırlı parkurda taşır; "
        "konut ve oyun alanlarında yaygın kurulan ekipman hariç (çocuk bahçesi salıncağı 95.06).",
        "<b>Pozisyon sınırları:</b> oyun kağıdı 95.04, bulmaca 95.03, sihirbazlık kağıdı 95.05. Noel motifli "
        "tabak, örtü gibi fayda eşyası maddesine göre (Not 1(z)); hakiki Noel ağacı Fasıl 6.",
    ],
    "karistirilan": [
        ["Elektrikli çelenk (Noel ışıkları)", "94.05", "Not 1(u); 95.04 veya 95.05 değil"],
        ["Mantardan dart tablası", "95.04", "Fasıl 45 Not 1: Fasıl 95 eşyası mantar faslına girmez"],
        ["Orijinal heykel; zooloji koleksiyonu; tiyatro dekoru", "97.03 / 97.05 / 59.07",
         "Gezici hayvan sergisi ise 95.08"],
        ["Kamp çadırı; kamera tripodu", "63.06 / 96.20", "Not 1(y), (v); çocuk oyun çadırı 95.03"],
        ["İnsansız hava taşıtı (drone)", "88.06", "Not 1(p); yalnız eğlence için uçan oyuncak 95.03"],
        ["Yüzücü ve kayak gözlüğü", "90.04", "Not 1(r); oyuncak gözlük 95.03"],
    ],
}

# ------------------------------------------------------------------ FASIL 96
HAP[96] = {
    "tur": "hap",
    "fasil": 96,
    "kademe": "A",
    "sinavda": "Son 5 sınavda 3 kez doğrudan, “sınıflandırılamaz / yanlış gösterilmiştir” kalıbında: bebek bezinin "
               "96.19’da olduğu (63.07 değil), dişçilik tornası fırçasının 90.18’e gittiği (96.03 değil), seyahat "
               "dikiş takımının GYK 1 ile 96.05’te olduğu (3(b) değil). Seçeneklerde: ayakkabı temizleme takımı "
               "96.05, diş fırçasının maddesine göre sınıflanmaması, resim fırçası, çakmak.",
    "pozisyonlar": [
        ["96.01", "İşlenmiş fildişi, kemik, boynuz, mercan, sedef ve eşyası"],
        ["96.02", "Korozo, kehribar, lületaşı; mum-reçine kalıp eşyası; jelatin kapsül"],
        ["96.03", "Süpürge, fırça, paspas, boya rulosu; makine fırçası dahil"],
        ["96.05", "Tuvalet, dikiş, ayakkabı-elbise temizleme seyahat takımları"],
        ["96.06", "Düğme, çıtçıt, düğme taslağı; kol düğmesi hariç"],
        ["96.08", "Tükenmez-keçeli-dolma kalem, dolma kurşun kalem, yedek uç"],
        ["96.09", "Kurşun kalem, boya kalemi, pastel, tebeşir"],
        ["96.13", "Çakmak, ateşleyici; dolu veya boş gaz haznesi dahil"],
        ["96.14", "Pipo, nargile, ağızlık; elektronik sigara hariç"],
        ["96.15", "Tarak, toka, firkete, bigudi; elektrikli olanlar hariç"],
        ["96.19", "Bebek bezi, hijyenik ped, tampon; madde önemsiz"],
        ["96.20", "Monopod, bipod, tripod, selfie çubuğu"],
    ],
    "hap": [
        "<b>Not 1 – fasıl dışı:</b> makyaj kalemi Fasıl 33, taklit mücevher 71.17, gözlük çerçevesi 90.03, teknik "
        "çizim kalemi 90.17, tıbbi-dişçilik fırçası 90.18; Fasıl 66, 91–95 ve 97 eşyası.",
        "<b>Maddeye değil adına göre:</b> 96.03–96.20 eşyayı adıyla sayar; diş fırçası, tarak, kalem, çakmak "
        "maddesine bakılmaksızın Fasıl 96. Bebek bezi “hangi maddeden olursa olsun” 96.19; tripod da her maddeden.",
        "<b>96.01–96.02 kalıntıdır:</b> fildişi, kemik, sedef, kehribar, lületaşı eşyası başka yerde adıyla "
        "geçiyorsa oraya gider: düğme 96.06, tarak 96.15, pipo 96.14, piyano tuşu 92.09, dipçik levhası 93.05.",
        "<b>Kıymetli madde (Not 4):</b> kalem, çakmak, pipo, termos kıymetli metal veya taş içerse de Fasıl 96; "
        "96.01–96.06 ve 96.15 eşyası ise yalnız önemsiz süs ölçüsünde, fazlası Fasıl 71.",
        "<b>96.03 fırça:</b> makine, cihaz ve taşıt fırçası, badana rulosu, paspas dahil. Dişçilik-cerrahi fırçası "
        "90.18, oyuncak fırça 95.03, pudra ponponu 96.16, motorlu süpürge 84.79.",
        "<b>96.05 seyahat takımı:</b> farklı pozisyon eşyasından tuvalet, dikiş, ayakkabı-elbise temizleme takımı; "
        "pozisyon metniyle GYK 1 ile sınıflanır. Manikür takımı 82.14’tedir.",
        "<b>Kalem ayrımı:</b> mürekkep sistemli kalem, yedek ucu ve dolma kurşun kalem 96.08; kılıflı kurşun "
        "kalem, pastel, tebeşir 96.09; mürekkep kartuşu 32.15; makyaj kalemi Fasıl 33.",
        "<b>Aksam ve özel madde:</b> çakmağın dolu-boş gaz haznesi 96.13 (39.26, 27.11 değil); sertleştirilmemiş "
        "jelatin kapsül 96.02, kare-dikdörtgen jelatin levha 35.03; elektronik sigara 85.43.",
    ],
    "karistirilan": [
        ["Dişçilik tornasında kullanılan fırça", "90.18", "Not 1(f); saç, elbise, resim fırçası ve rulo 96.03"],
        ["Tek kullanımlık bebek bezi", "96.19", "Madde önemsiz; 63.07, 48.18, 56.01 değil"],
        ["Manikür takımı", "82.14", "96.05 hariç tutar; seyahat dikiş takımı 96.05"],
        ["Elektronik sigara, nargile şeklinde de", "85.43", "96.14 dışı; nargile ve pipo 96.14"],
        ["Çakmak taşı; doldurma kabındaki gaz", "36.06", "Çakmağın kendi gaz haznesi ise 96.13"],
        ["Kaş, göz, dudak kalemi", "33.04", "Not 1(a); kurşun ve boya kalemi 96.09"],
    ],
}

# ------------------------------------------------------------------ FASIL 97
HAP[97] = {
    "tur": "hap",
    "fasil": 97,
    "kademe": "B",
    "sinavda": "Son 5 sınavda 1 kez doğrudan: eskiliği 100 yılı aşan orijinal heykelin Not 5(B) gereği GYK 1 ile "
               "97.03’te kaldığı (97.06 ve GYK 3 çeldirici). Orijinal heykel ve zooloji koleksiyonu “gezici hayvan "
               "sergisi ile aynı fasıl”, antika biblo “maddesine göre sınıflanan eşya” sorularında çeldirici oldu.",
    "pozisyonlar": [
        ["97.01", "Tamamen elle yapılmış resim, elle kopya, kolaj, mozaik"],
        ["97.02", "Elle hazırlanmış levhadan doğrudan orijinal gravür, litografya"],
        ["97.03", "Orijinal heykel, madde önemsiz; seri üretim hariç"],
        ["97.04", "Kullanılmış pul, pullu ilk gün zarfı; 49.07 hariç"],
        ["97.05", "Zoolojik, botanik, arkeolojik, tarihi, nümizmatik koleksiyon eşyası"],
        ["97.06", "Eskiliği 100 yılı aşan diğer antikalar (artık)"],
    ],
    "hap": [
        "<b>Yaş, sanat eserini antikaya çevirmez (Not 5(B)):</b> 97.06, 97.01–97.05 eşyasına uygulanmaz; "
        "100 yaşını aşan orijinal heykel GYK 1 ile 97.03’te, tablo 97.01’de kalır.",
        "<b>Not 5(A):</b> Not 1–4 saklı kalmak şartıyla bu fasıldaki eşya başka fasılda sınıflandırılmaz; antika "
        "biblo, mobilya, halı, saat maddesine veya işlevine göre değil 97.06’da.",
        "<b>Seri üretim sanat eseri değildir (Not 2, 4):</b> sanatçı tasarlasa da ticari seri üretim mozaik ve "
        "heykel fasıl dışı; heykelcik ve elle dekore fabrikasyon vazo maddesine göre (44.20, 68.02, 69.13, 83.06).",
        "<b>Fasıl dışı (Not 1):</b> itibari değeri tanınan kullanılmamış pul 49.07; tiyatro dekoru ve atölye fonu "
        "tuvali 59.07; inci ve kıymetli taş yaşına bakılmaksızın 71.01–71.03.",
        "<b>Baskı ve çerçeve (Not 3, 6):</b> mekanik veya fotomekanik usulle yapılan baskı 97.02 dışı; çerçeve "
        "mahiyet ve kıymetçe esere uygunsa eserle, değilse ayrı sınıflandırılır.",
    ],
    "karistirilan": [
        ["Gezici hayvan sergisi; üç tekerlekli bisiklet", "95.08 / 95.03",
         "Fasıl 95; orijinal heykel, zooloji koleksiyonu Fasıl 97"],
        ["Elle çizilmiş mimari plan; mobilya deseni", "49.06", "Resim sayılmaz; 97.01 dışı"],
        ["Hediye kutusunda yasal tedavüldeki madeni para", "71.18", "Koleksiyon eşyası değil; 97.05 dışı"],
    ],
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for n, d in HAP.items():
        p = os.path.join(OUT, f"fasil_{n:02d}.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("yazıldı", p)


if __name__ == "__main__":
    main()
