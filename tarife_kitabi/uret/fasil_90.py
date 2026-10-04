#!/usr/bin/env python3
# Fasıl 90 modülü üreticisi
import json
import os

K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

oz = {
    "vurgu": "Fasıl 90’da önce Not 1’deki hariç tutmalara bakılır (dijital kamera 85.25, radar ve telsiz uzaktan kumanda 85.26, optik işlenmemiş ayna 70.09, tripod 96.20 vb.); sonra eşyanın ne yaptığı sorulur: görmek ve görüntülemek (optik), tedavi etmek (tıp), ölçmek-kontrol etmek veya otomatik ayarlamak. Ölçü aletlerinde pozisyonu ölçülen büyüklük belirler; adıyla yer almayan ölçü aleti 90.31’e, otomatik ayarlayan alet ise Not 7 şartlarıyla 90.32’ye gider.",
    "maddeler": [
        "Bölüm XVIII’in bölüm notu yoktur; Fasıl 90 bölümün ilk faslıdır ve hassas alet ve cihazları kapsar. Basit güneş gözlüğü, basit büyüteç, metre-cetvel ve fantazi higrometre gibi eşya hassas olmasa da bu fasıldadır.",
        "Optik elemanlar ayrı bir zincir izler: camdan olup optik tarzda işlenmemişse Fasıl 70; işlenmiş ve monte edilmemişse 90.01; bir alete monte edilmişse 90.02; kendi başına bir alet oluşturuyorsa (el büyüteci, kapı gözü) 90.13.",
        "Tıp grubu beş pozisyona bölünür: genel tıbbi alet 90.18; mekanoterapi, masaj ve terapik solunum 90.19; diğer solunum cihazı ve gaz maskesi 90.20; ortopedi, protez, işitme cihazı ve kalp pili 90.21; X-ışını ve iyonlaştırıcı ışınlı cihaz 90.22.",
        "Parçalar Not 2 ile üç basamakta sınıflandırılır: kendi pozisyonu olan parça orada (vakum pompası 84.14, optik eleman 90.01 / 90.02, fotoğraf makinası 90.06); belirli bir alete özgü parça o aletin pozisyonunda; birden çok pozisyona ortak parça 90.33’te.",
        "Not 3 ile Bölüm XVI Not 3 ve 4 bu fasılda da uygulanır: kombine aletler esas fonksiyonlarına göre, ayrı elemanlardan oluşup tek bir fonksiyonu birlikte gören sistemler (ör. telemetri sistemi) fonksiyonel birim olarak bütün halinde sınıflandırılır.",
    ],
}

karar_tablosu = {
    "aciklama": "Soruları yukarıdan aşağıya sırayla sorun; ilk “evet” cevabı pozisyonu verir.",
    "satirlar": [
        ["1", "Not 1 ile hariç mi? (kauçuk, deri, tekstil teknik eşya; elastik bandaj; seramik veya cam laboratuvar eşyası; işlenmemiş ayna; genel kullanım parçası; dijital kamera; radar, uzaktan kumanda; oyuncak; tripod)",
         "Fasıl 90 dışı: <b>40.16</b>, <b>42.05</b>, <b>59.11</b>, Bölüm XI, <b>69.09</b>, <b>70.09</b>, <b>70.17</b>, <b>85.25</b>, <b>85.26</b>, Fasıl 95, <b>96.20</b>"],
        ["2", "Ayrı gelen aksam, parça veya aksesuar mı?",
         "Kendi pozisyonu (Fasıl 84, 85, 90, 91) → ait olduğu aletin pozisyonu → <b>90.33</b> (Not 2)"],
        ["3", "Mercek, prizma, ayna, filtre gibi bir optik eleman mı?",
         "Camdan ve işlenmemiş: Fasıl 70 · monte edilmemiş <b>90.01</b> · alete monte <b>90.02</b>"],
        ["4", "Yalnız teşhir için yapılmış, başka işe elverişsiz alet veya model mi?",
         "<b>90.23</b>"],
        ["5", "X-ışınlı veya alfa, beta, gama ışınlı cihaz mı? (tıbbi olsun olmasın)",
         "<b>90.22</b> (radyasyonu yalnız ölçen veya bulan alet <b>90.30</b>; tıbbi sintigrafi <b>90.18</b>)"],
        ["6", "Tıbbi, cerrahi, dişçilik veya veteriner amaçlı mı?",
         "Ortopedi, protez, işitme cihazı, kalp pili <b>90.21</b> · mekanoterapi, masaj, terapik solunum <b>90.19</b> · diğer solunum, gaz maskesi <b>90.20</b> · diğerleri <b>90.18</b>*"],
        ["7", "Ölçtüğü değeri istenen değerle karşılaştırıp otomatik olarak düzeltiyor mu? (Not 7)",
         "<b>90.32</b>"],
        ["8", "Ölçtüğü büyüklük bir pozisyonda adıyla belirtilmiş mi?",
         "Seyrüsefer <b>90.14</b> · arazi-meteoroloji <b>90.15</b> · terazi <b>90.16</b> · elde uzunluk <b>90.17</b> · malzeme testi <b>90.24</b> · sıcaklık-atmosfer-nem <b>90.25</b> · akış-seviye-basınç <b>90.26</b> · analiz-ışık-ses <b>90.27</b> · sayaç <b>90.28</b> · devir-hız <b>90.29</b> · elektrik-radyasyon <b>90.30</b>"],
        ["9", "Gözlük, dürbün, fotoğraf-sinema cihazı, projektör veya mikroskop mu?",
         "<b>90.03</b>–<b>90.12</b>"],
        ["10", "Hiçbiri değilse",
         "Ölçme-kontrol aleti, profil projektörü <b>90.31</b> (Not 5) · lazer ve diğer optik alet <b>90.13</b>"],
    ],
    "dipnot": "* Tıpta kullanılsa da 90.18’e girmeyenler: gözlük 90.04, fotoğraf makinası 90.06, mikroskop 90.11 / 90.12 (oftalmolojik çift gözlü mikroskop hariç), termometre 90.25, laboratuvar tahlil aleti 90.27, tekerlekli sandalye 87.13, dişçilik aletiyle birleşmemiş dişçi koltuğu ve hastane mobilyası 94.02.",
}

pozisyon_haritasi = [
    ["90.01", "Optik lif, polarizan levha, monte edilmemiş optik eleman", "Cam ise optik tarzda işlenmiş olmalı", "Kontakt lens, gözlük camı, prizma"],
    ["90.02", "Alete monte edilmiş optik elemanlar", "Bir alete takılmak üzere çerçeveli", "Kamera objektifi, mikroskop oküleri"],
    ["90.03", "Gözlük çerçeveleri ve parçaları", "Adi metal vida, zincir, yay hariç", "Plastik çerçeve, sap, köprü"],
    ["90.04", "Gözlükler (düzeltici, koruyucu, diğer)", "Yalnız gözleri kaplar; siper, kask hariç", "Güneş, kayak, 3D gözlük"],
    ["90.05", "Dürbün, teleskop, astronomi aletleri", "Silah dürbünü, periskop 90.13 (Not 4)", "Tiyatro dürbünü, gece görüş dürbünü"],
    ["90.06", "Fotoğraf makinası; flaş cihazı ve ampulü", "Film esaslı; dijital kamera 85.25", "Anında baskı kabini, tek kullanımlık makina"],
    ["90.07", "Sinema kamerası ve projektörü", "Sesli olsun olmasın; optiksiz de", "Film projektörü (video projektörü hariç)"],
    ["90.08", "Sabit görüntü projektörü; fotoğraf büyültücü", "Sinematografik olmayan", "Slayt projektörü, episkop, mikrofilm okuyucu"],
    ["[90.09]", "Metinde içeriksiz (boş) pozisyon", "Fotokopi cihazları 84.43’te", "—"],
    ["90.10", "Fotoğraf laboratuvarı aletleri; negatoskop; perde", "Başka yerde yer almayan", "Banyo tankı, film kurutucu, projeksiyon perdesi"],
    ["90.11", "Bileşik optik mikroskoplar", "İki safhalı büyütme", "Stereo ve cerrahi mikroskop, trişinoskop"],
    ["90.12", "Optik olmayan mikroskoplar; difraksiyon cihazları", "Elektron veya proton demeti", "Elektron mikroskobu"],
    ["90.13", "Lazerler; başka yerde yer almayan optik aletler", "Lazer diyotu 85.41 hariç", "El büyüteci, kapı gözü, periskop"],
    ["90.14", "Pusulalar; seyrüsefer aletleri", "Radar, radyo seyrüsefer 85.26", "Sekstant, otomatik pilot, iskandil"],
    ["90.15", "Arazi ölçme, meteoroloji, jeofizik; telemetre", "Pusula hariç; GPS 85.26", "Teodolit, anemometre, sismograf"],
    ["90.16", "Hassas teraziler", "Hassasiyet 5 cg veya daha iyi", "Analitik terazi, kırat terazisi"],
    ["90.17", "Çizim, işaretleme, hesap aletleri; elde uzunluk ölçüsü", "Elde kullanılır; sabit ayaklı 90.31", "Pergel, iletki, sürgülü cetvel, kumpas"],
    ["90.18", "Tıp, cerrahi, dişçilik, veteriner aletleri", "Sintigrafi, elektro-medikal, göz testi dahil", "Şırınga, EKG, endoskop, dişçi ünitesi"],
    ["90.19", "Mekanoterapi, masaj, psikoteknik; terapik solunum", "Tıbbi gözetim; egzersiz aleti 95.06", "Masaj aleti, oksijen çadırı, nebülizör"],
    ["90.20", "Diğer solunum cihazları; gaz maskeleri", "Filtresiz, mekaniksiz maske hariç", "İtfaiyeci solunum cihazı, gaz maskesi"],
    ["90.21", "Ortopedi, kırık cihazı, protez, işitme cihazı", "Taşınan veya vücuda yerleştirilen", "Koltuk değneği, takma diş, kalp pili"],
    ["90.22", "X-ışınlı ve iyonlaştırıcı ışınlı cihazlar", "Tıbbi olsun olmasın; tüp, ekran dahil", "Röntgen cihazı, tomograf, endüstriyel X-ışını"],
    ["90.23", "Teşhir amaçlı alet, cihaz ve modeller", "Başka amaca elverişsiz", "Anatomi modeli, kabartma küre, hazır lam"],
    ["90.24", "Malzemelerin mekanik özelliklerini test makinaları", "Sertlik, çekme, aşınma testi", "Sertlik test cihazı, tekstil dinamometresi"],
    ["90.25", "Hidrometre, termometre, pirometre, barometre, higrometre", "Kaydedici olsun olmasın; kombineler dahil", "Klinik termometre, barograf, fantazi higrometre"],
    ["90.26", "Sıvı-gaz akış, seviye, basınç ölçerleri", "Anlık değişken; toplam miktar 90.28", "Debimetre, manometre, seviye göstergesi"],
    ["90.27", "Fiziksel-kimyasal analiz; ısı, ışık, ses ölçümü; mikrotom", "Cam laboratuvar eşyası 70.17", "Spektrometre, pH metre, pozometre"],
    ["90.28", "Gaz, sıvı, elektrik sayaçları", "Toplam miktar; kalibre sayaçları dahil", "Su sayacı, peşin ödemeli elektrik sayacı"],
    ["90.29", "Devir ve üretim sayaçları; hız göstergesi; stroboskop", "90.14 / 90.15’tekiler hariç", "Taksimetre, pedometre, takometre"],
    ["90.30", "Elektriksel ölçüm; iyonlaştırıcı radyasyon ölçümü", "Elektrik sayacı 90.28’de", "Osiloskop, multimetre, dozimetre"],
    ["90.31", "Başka yerde yer almayan ölçme-kontrol; profil projektörü", "Not 5: 90.13’e üstün", "Balans makinası, inşaatçı su terazisi, yük hücresi"],
    ["90.32", "Otomatik ayar ve kontrol aletleri", "Not 7: ölç, karşılaştır, düzelt", "Termostat, manostat, humidistat"],
    ["90.33", "Fasıl 90 eşyasının diğer parçaları", "Not 2(c) artık pozisyon", "Birden çok pozisyona ortak parça"],
]

notlar = [
    ["Bölüm XVIII", "Bölüm XVIII’in bölüm notu yoktur. Fasıl 90 bölümün ilk faslıdır; bölüm başlığına göre bölüm ayrıca saatçi eşyası ile müzik aletlerini (Fasıl 91 ve 92) kapsar."],
    ["Fasıl 90 Not 1 (a)–(f)", "Fasıl dışı: (a) sertleştirilmiş kauçuk hariç vulkanize kauçuktan (40.16), deriden (42.05) veya dokumaya elverişli maddelerden (59.11) teknik eşya; (b) etkisini yalnız elastikiyetinden alan tekstil kemer ve bandajlar (hamile korsesi, göğüs, karın, eklem ve adale bandajları) → Bölüm XI; (c) ateşe dayanıklı eşya (69.03), seramik laboratuvar eşyası (69.09); (d) optik tarzda işlenmemiş cam aynalar (70.09), optik eleman niteliği olmayan adi veya kıymetli metal aynalar (83.06, Fasıl 71); (e) 70.07, 70.08, 70.11, 70.14, 70.15 ve 70.17 eşyası; (f) adi metalden genel kullanıma mahsus parçalar (Bölüm XV) ve plastikten benzerleri (Fasıl 39). <b>İstisna:</b> özel olarak tıbbi, cerrahi, dişçilik veya veterinerlikte implant olarak kullanılmak üzere dizayn edilmiş eşya 90.21’dedir."],
    ["Fasıl 90 Not 1 (g)", "Ölçü tertibatlı tevzi pompaları (84.13); eşyayı tartarak sayan ve kontrol eden tartı aletleri ile ayrı gelen ağırlıklar (84.23); kaldırma-elleçleme makinaları (84.25–84.28); kâğıt-karton kesme makinaları (84.41); 84.66’daki iş parçası veya takım ayar tertibatı (optik bölücü gibi optik aletli olanlar dahil, merkez hizalama teleskobu gibi tamamen optik olanlar hariç); hesap makinaları (84.70); vanalar (84.81); 84.86 makinaları (hassaslaştırılmış yarı iletken üzerine devre taslağı çizen veya yansıtan cihazlar dahil)."],
    ["Fasıl 90 Not 1 (h)–(n)", "Taşıt ve bisiklet projektörleri (85.12); portatif elektrik lambaları (85.13); sinematografik ses kayıt ve okuma cihazları (85.19); ses kafaları (85.22); televizyon kameraları, diğer görüntü kaydedici kameralar ve <b>dijital kameralar (85.25)</b>; <b>radar ve telsiz uzaktan kumanda cihazları (85.26)</b>; optik lif bağlantı parçaları (85.36); sayısal kontrol cihazları (85.37); monoblok farlar (85.39); 85.44’teki optik lif kabloları; 94.05 projektörleri; Fasıl 95 eşyası; monopod, bipod, tripod (96.20); maddesine göre sınıflandırılan kapasite ölçüleri; bobin ve makaralar (ör. 39.23, Bölüm XV)."],
    ["Fasıl 90 Not 2", "Not 1 saklı kalmak üzere aksam ve parçalar: (a) kendisi Fasıl 84, 85, 90 veya 91’de bir pozisyona giren parça (84.87, 85.48, 90.33 hariç) her halükarda kendi pozisyonunda; (b) yalnız veya esas itibariyle belirli bir alete ya da aynı pozisyondaki (90.10, 90.13, 90.31 dahil) birden fazla alete elverişli parça o aletin pozisyonunda; (c) diğer bütün parçalar <b>90.33</b>’te."],
    ["Fasıl 90 Not 3", "Bölüm XVI Not 3 ve 4 bu fasılda da uygulanır: kombine ve çok işlevli aletler esas fonksiyonlarına göre; tek bir fonksiyonu birlikte gören ayrı elemanlar (ör. vericisi, alıcısı ve kayıt aletiyle telemetri sistemi) fonksiyonel birim olarak bütün halinde sınıflandırılır. Esas fonksiyon belirlenemezse GYK 3(c) uygulanır."],
    ["Fasıl 90 Not 4", "Silahlar için teleskopik nişan dürbünleri, denizaltı ve tank periskopları, bu fasıl veya Bölüm XVI makinalarına ait teleskoplar 90.05’e girmez → <b>90.13</b>. Silaha takılı veya silahla birlikte gelen nişan dürbünü ise silahla birlikte sınıflandırılır (90.13 Açıklama Notu)."],
    ["Fasıl 90 Not 5", "Hem 90.13 hem 90.31 pozisyonunda sınıflandırılabilen optik ölçü veya kontrol makina, cihaz ve aletleri <b>90.31</b>’de sınıflandırılır."],
    ["Fasıl 90 Not 6", "90.21 anlamında “ortopedik cihaz”: vücudun şekil bozukluklarını önleyen veya düzelten ya da bir hastalık, ameliyat veya yaralanmayı takiben vücudun belli kısımlarını destekleyen veya sabit tutan cihazlar. Ortopedik koşulları düzeltmek üzere tasarlanmış ayakkabı ve özel iç tabanlar da (1) ölçüye göre yapılmışsa veya (2) seri halde üretilmiş olup <b>çift halinde değil tek başına</b> sunulmuş ve <b>her iki ayağa eşit şekilde uyacak</b> biçimde tasarlanmışsa bu tabire girer."],
    ["Fasıl 90 Not 7", "90.32 yalnız şunlara uygulanır: (a) sıvı veya gazların akış, seviye, basınç veya diğer değişkenlerini ya da sıcaklığı otomatik kontrol eden alet ve cihazlar (çalışmaları elektrik olayına bağlı olsun olmasın); (b) elektriksel miktarların otomatik düzenleyicileri ile çalışması kontrol edilen faktöre göre değişen bir <b>elektrik olayına bağlı</b> olarak elektriksel olmayan miktarları otomatik kontrol eden alet ve cihazlar. Her ikisi de faktörün gerçek değerini sürekli veya periyodik ölçerek onu istenen değere getirir ve orada tutar."],
    ["Genel Açıklamalar (I)", "Fasıl esas itibariyle çok hassas alet ve cihazları kapsar. İstisnalar: toz ve güneş gözlüğü gibi basit koruyucu gözlükler (90.04), basit büyüteçler ve büyütücü olmayan periskoplar (90.13), basit metre ve cetveller (90.17), doğruluk derecesi ne olursa olsun fantazi higrometreler (90.25). Eşya her maddeden (kıymetli metal ve taşlar dahil) yapılabilir."],
    ["Genel Açıklamalar (II)", "GYK 2(a): optik aksamı takılmamış fotoğraf makinası veya mikroskop ve toplama tertibatı takılmamış elektrik sayacı, tamamlanmış eşyanın asli niteliğini taşıdığından tamamlanmış eşya gibi sınıflandırılır."],
    ["Genel Açıklamalar (III)", "Kendi pozisyonu olan parçalar: elektron mikroskobunun vakum pompası 84.14; transformatör, kondansatör, direnç, röle, lamba Fasıl 85; optik parçalar her durumda 90.01 / 90.02; saat makinaları Fasıl 91; mikroskop veya stroboskop için yapılmış olsa da fotoğraf makinası 90.06. Ayrıca bu fasılın aletleriyle donatılmış uzay aracı 88.02’dedir."],
    ["90.01 Açıklama Notu", "Camdan optik eleman ancak <b>optik tarzda işlenmişse</b> (yüzeyi istenen optik etki için cilalanmışsa) 90.01’e girer; cilalanmamış ve cilalamadan önce başka işlem gerektirenler Fasıl 70’tedir. Camdan başka maddeden olanlar işlenmiş olsun olmasın 90.01’dedir. Yalnız taşıma sırasında korunmak için geçici monte edilen eleman monte sayılmaz. Tek tek kılıflı liflerden optik lif kabloları 85.44’tür."],
    ["90.04 Açıklama Notu", "Yalnız gözleri kaplayan gözlükler: görme kusurunu düzelten, güneş, kayak, kaynakçı, sualtı gözlükleri ve kâğıt çerçeveli olsa da 3D film gözlükleri. Yüzün önemli bir kısmını koruyan siperler, motosikletçi kask ve vizyerleri, sualtı maskeleri hariçtir; kontakt lens 90.01, gözlük çerçeveli opera dürbünü 90.05, oyuncak gözlük 95.03, karnaval gözlüğü 95.05."],
    ["90.13 Açıklama Notu", "Lazer: dalga boyu 1 nanometre ile 1 milimetre arasında ışın üretir; kablolarla bağlı ayrı ünitelerden oluşan lazer sistemi birlikte sunulursa 90.13’tedir. Belirli bir işe uyarlanmış lazerli makinalar işlevine göre: madde işleme 84.56, lehim-kaynak 85.15, boru hizalama 90.15, tıbbi 90.18. Lazer diyotu 85.41, pompalama flaş lambası 85.39, lazer kristali, aynası ve merceği 90.01 / 90.02."],
    ["90.16 Açıklama Notu", "Hassasiyeti <b>5 santigram veya daha iyi</b> olan teraziler, birlikte gelen ağırlıklarıyla 90.16’dadır. Daha az hassas teraziler ve ayrı gelen ağırlıklar (kıymetli metalden olsa da) 84.23’tedir."],
    ["90.17 Açıklama Notu", "Elde kullanılan uzunluk ölçü aletlerinde elde taşınabilme özelliği şarttır; bir ayak, destek veya makinaya daimi bağlanmışsa 90.31. Mesaha zincir ve şeritleri 90.15; hesap makinaları 84.70; grafik tabletleri 84.71; fotogrametrik koordinatograflar 90.15."],
    ["90.18 Açıklama Notu", "Çekiç, testere, makas, pens gibi alelade aletler ancak sterilizasyon için kolay sökülebilme, imalattaki özen, yapıldıkları madde veya belirli bir müdahale için çanta-kutu içinde takım halinde sunulma gibi özelliklerle açıkça tıbbi oldukları anlaşılırsa 90.18’e girer."],
    ["90.19 Açıklama Notu", "Mekanoterapi aleti tıbbi gözetim altında eklem ve kas tedavisine yöneliktir; evde veya salonda kullanılan sıradan egzersiz aletleri 95.06’da, merdiven ve barfiks gibi tamamen sabit aletler kendi pozisyonlarında. Hiperbarik ve dekompresyon odaları 90.18’dedir."],
    ["90.20 Açıklama Notu", "Mekanik parçası ve değiştirilebilir filtresi olmayan koruyucu maskeler (aktif karbonlu olsa da tekstil toz maskesi, cerrah maskesi) 63.07; yalnız tel ağdan maske Bölüm XV; anestezi maskesi 90.18; tüpsüz kullanılan dalgıç maskesi ve şnorkel 95.06."],
    ["90.22 Açıklama Notu", "X-ışını çalışmaları için özelleştirilmiş muayene-tedavi masa ve koltukları ayrı gelse de 90.22’dedir; özelleştirilmemiş olanlar 94.02. Radyasyonu yalnız ölçen veya bulan aletler 90.30; kurşunlu kauçuk önlük ve eldiven 40.15, kurşunlu cam gözlük 90.04."],
    ["90.23 Açıklama Notu", "Yalnız teşhir için yapılmış ve başka işe elverişsiz olmalıdır: anatomi modelleri, kesit modeller, kabartma harita ve küreler (basılı olsun olmasın), hazır mikroskop lamları. Basılı tablo ve plan Fasıl 49; yerde uçuş eğitim cihazı 88.05; eğlence amaçlı model Fasıl 95; yüz yılı aşan antikalar 97.06."],
    ["90.26 / 90.28 Açıklama Notları", "Debimetre akış hızını ölçer (90.26); belirli bir sürede geçen toplam miktarı gösteren sayaç 90.28’dedir. Barometre atmosfer basıncını (90.25), manometre kapalı yerdeki sıvı veya gaz basıncını (90.26) ölçer."],
    ["90.27 Açıklama Notu", "Taksimatlı basit cam eşya niteliğindeki aletler (bütirometre, üreometre vb.) 70.17’dedir. Laboratuvarda kullanılsa da fırın, santrifüj, karıştırıcı, filtre gibi Bölüm XVI makinaları ve laboratuvar mobilyası kendi pozisyonlarındadır. Yalnız alarm veren elektronik duman dedektörü 85.31’dedir."],
]

sinir_komsulari = [
    ["Dijital fotoğraf makinası, video kamera", "85.25", "Not 1(h); 90.06 film esaslı makinaları kapsar"],
    ["Radar, GPS alıcısı, telsiz uzaktan kumanda cihazı", "85.26", "Not 1(h); 90.14 ve 90.15 hariç tutmaları"],
    ["Video projektörü", "85.28", "90.07 ve 90.08 hariç tutmaları"],
    ["Fotokopi cihazı; küçük ekranlı mikrofilm okuyucu-fotokopi cihazı", "84.43", "90.06 ve 90.08 hariç tutmaları"],
    ["Optik işlenmemiş ayna (tıraş aynası, dikiz aynası); işlenmemiş gözlük camı", "70.09 / 70.15", "Not 1(d) ve (e)"],
    ["Cam laboratuvar eşyası; bütirometre, piknometre", "70.17", "Not 1(e); 90.25 ve 90.27 Açıklama Notları"],
    ["Hassasiyeti 5 cg’dan az terazi; ayrı gelen ağırlıklar", "84.23", "Not 1(g); 90.16 Açıklama Notu"],
    ["Tripod, monopod, bipod", "96.20", "Not 1(l); alete özel yapılmış olsa da"],
    ["Tekerlekli sandalye; hastane yatağı, ameliyat masası", "87.13 / 94.02", "90.18 hariç tutmaları"],
    ["Elastik tekstil bandaj, hamile korsesi; varis çorabı", "Bölüm XI (62.12, 63.07, 61.15)", "Not 1(b); 90.21 hariç tutmaları"],
    ["Tekstil toz maskesi, tek kullanımlık cerrah maskesi", "63.07", "90.20: mekanik parçasız ve filtresiz"],
    ["Evde kullanılan egzersiz aleti; şnorkel", "95.06", "90.19 ve 90.20 hariç tutmaları"],
    ["Diş dolgu maddesi, diş alçısı; kemiği yeniden oluşturan yapıştırıcı", "30.06", "90.18 ve 90.21 hariç tutmaları"],
    ["Lazerle metal işleyen tezgah; lazer kaynak makinası", "84.56 / 85.15", "90.13: işe uyarlanmış lazerler"],
    ["Termostatik valf, basınç düşürücü valf; programlanabilir kontrol cihazı", "84.81 / 85.37", "90.32 hariç tutmaları"],
]

tuzaklar = [
    "<b>Kamera her zaman 90.06 değildir.</b> Film esaslı fotoğraf makinası 90.06’dadır; dijital kamera ve video kamera Not 1(h) gereği 85.25’e gider. Buna karşılık jeton veya kartla çalışan, pozu anında basan kabin tipi makina 84.76’ya değil 90.06’ya girer.",
    "<b>Aynı adlı alet, iki ayrı pozisyon.</b> Anemometre meteorolojik ise 90.15, maden-tünel tipi ise 90.26; su terazisi arazi ölçme için ise 90.15, inşaatçı tipi ise 90.31; ölçü şeridi mesaha için 90.15, genel kullanım için 90.17; altimetre yalnız yükseklik gösteriyorsa 90.14, barometreli ise 90.25.",
    "<b>Ölçmek ≠ otomatik ayarlamak.</b> Termometre 90.25, manometre 90.26; ölçtüğü değeri istenen değerle karşılaştırıp düzelten termostat veya manostat 90.32. Termostatla kontrol edilen valf ise 84.81’dedir.",
    "<b>Akış hızı ≠ toplam miktar.</b> Debimetre 90.26; su, gaz veya elektrik sayacı 90.28; voltmetre ve ampermetre 90.30; taksimetre ve takometre 90.29.",
    "<b>Optik eleman zinciri.</b> Camdan ve optik tarzda işlenmemiş: Fasıl 70; işlenmiş ve monte edilmemiş: 90.01; alete monte: 90.02; kendi başına alet (el büyüteci, kapı gözü, alete takılmayan işlenmiş muayene aynası): 90.13.",
    "<b>Not 4 ve Not 5 öncelikleri.</b> Silah nişan dürbünü ve tank periskobu 90.05’e değil 90.13’e; hem 90.13 hem 90.31’e uyan optik ölçü aleti 90.31’e gider.",
    "<b>Tıpta kullanılan her alet 90.18 değildir.</b> Klinik termometre 90.25, cerrahi mikroskop 90.11, tıbbi gözlük 90.04, kan-idrar tahlil aleti 90.27, X-ışını cihazı 90.22; dişçilik aletiyle birleşmemiş dişçi koltuğu 94.02.",
    "<b>Ortopedik ayakkabı Fasıl 64’te değildir.</b> Not 6 şartlarını taşıyan ortopedik ayakkabı ve özel iç taban 90.21’dedir; iç tabanı düz tabanlık için basitçe kabartılmış hazır ayakkabı ise Fasıl 64’te kalır.",
    "<b>Terazide birim santigramdır.</b> 5 cg veya daha iyi hassasiyet 90.16; daha az hassas teraziler ve ayrı gelen ağırlıklar 84.23.",
    "<b>Radyasyonla ilgili üç ayrı yer.</b> Tıbbi teşhis için görüntü üreten gama kamera 90.18; radyoaktif kaynakla kalınlık ölçen veya paket içeriğini izleyen alet 90.22; radyasyonu yalnız ölçen veya bulan alet 90.30.",
]

hafiza = {
    "kanca": "GÖR – YOL BUL – TART-ÇİZ – İYİLEŞTİR – GÖSTER – ÖLÇ – AYARLA – PARÇA",
    "aciklama": "<b>GÖR</b> 90.01–90.13 (optik eleman, gözlük, dürbün, foto-sinema, mikroskop, lazer) · <b>YOL BUL</b> 90.14–90.15 (seyrüsefer, arazi-meteoroloji) · <b>TART-ÇİZ</b> 90.16–90.17 · <b>İYİLEŞTİR</b> 90.18–90.22 (tıp, terapi, solunum, ortopedi, X-ışını) · <b>GÖSTER</b> 90.23 · <b>ÖLÇ</b> 90.24–90.31 · <b>AYARLA</b> 90.32 · <b>PARÇA</b> 90.33. Ölçü bloğunu bir fabrika turu gibi düşünün: numuneyi kırarsınız (24), havaya bakarsınız (25), boruyu izlersiniz (26), laboratuvara girersiniz (27), sayacı okursunuz (28), makinanın devrini sayarsınız (29), elektriği ölçersiniz (30), kalanı kontrol masasında ölçersiniz (31); termostat (32) hepsini ayarlar.",
}

sinav_odagi = [
    "“Aynı 4’lü pozisyonda yer almayan eşya” kalıbı: termometre ve barometrenin (90.25) mikrometre (90.17) ile karıştırılması; taksimetre-stroboskop-pedometre (90.29), spektrometre-pozometre-mikrotom (90.27), debimetre-manometre-kalorimetre (90.26), pantograf-iletki-sürgülü cetvel (90.17) gruplarının bilinmesi.",
    "Pozisyon numara sırası ve fasıl aidiyeti: gözlük çerçevesi (90.03) → mikroskop (90.11) → şırınga (90.18) sıralaması; kontakt lens, sinema kamerası, kalp pili ve takometrenin aynı fasılda (Fasıl 90) toplandığı.",
    "Not 1 hariç tutmaları ve Fasıl 85 sınırı: telsiz uzaktan kumanda cihazlarının 85.26’da, dijital fotoğraf makinasının 85.25’te sınıflandırılması; bu sorularda 90.14 ve 90.22’nin çeldirici olarak kullanılması.",
    "GYK uygulamaları: plastik mahfaza içindeki cetvel, hesap diski, pergel, kurşun kalem ve kalemtıraştan oluşan çizim takımının GYK 3(b) ile 90.17’de; fotoğraf makinası mahfazası gibi özel mahfazaların GYK 5(a) ile eşyayla birlikte sınıflandırılması.",
    "Fasıl 90 eşyasının diğer fasılların sorularında çeldirici olması: ortopedik ayakkabının Fasıl 64 dışında (90.21) kalması; dişçilikte kullanılan alçıların 30.06’da (90.21 değil), oyuncak bebeklere mahsus camdan gözlerin 70.18’de, araç dikiz aynasının 70.09’da, tek kullanımlık tıbbi maskenin 63.07’de yer alması.",
    "Alt pozisyon düzeyinde sorulmuş ama 4’lü düzeyde öğrenilebilen eşya: inşaatçı tipi su terazisinin 90.31’de, kabartma dünya haritasının 90.23’te sınıflandırılması.",
]

cikmis_ornekler = [
    {
        "soru": "Aşağıdaki seçeneklerin hangisinde aynı tarife pozisyonunda (4’lü) yer <b>almayan</b> eşya bulunmaktadır?",
        "secenekler": [
            "Spektrometre, pozometre, mikrotom",
            "Taksimetre, stroboskop, pedometre",
            "Termometre, barometre, mikrometre",
            "Debimetre, manometre, kalorimetre",
            "Pantograf, iletki, sürgülü cetvel",
        ],
        "cevap": "C",
        "aciklama": "Termometre ve barometre 90.25’te, mikrometre ise elde kullanılan uzunluk ölçü aleti olarak 90.17’dedir. Diğer gruplar sırasıyla 90.27, 90.29, 90.26 ve 90.17’de tek pozisyonda toplanır.",
    },
    {
        "soru": "Aşağıdakilerden hangisinde eşyalar Türk Gümrük Tarife Cetvelindeki tarife pozisyon numara sıralamasına uygun olarak dizilmiştir?",
        "secenekler": [
            "Gözlük çerçevesi – Şırınga – Mikroskop",
            "Şırınga – Gözlük çerçevesi – Mikroskop",
            "Gözlük çerçevesi – Mikroskop – Şırınga",
            "Mikroskop – Gözlük çerçevesi – Şırınga",
        ],
        "cevap": "C",
        "aciklama": "Gözlük çerçeveleri 90.03’te, bileşik optik mikroskoplar 90.11’de, şırıngalar 90.18’dedir; doğru sıra 90.03 → 90.11 → 90.18’dir.",
    },
]

ozet = [
    "Önce Not 1: dijital kamera 85.25, radar ve uzaktan kumanda 85.26, işlenmemiş ayna 70.09, cam laboratuvar eşyası 70.17, tripod 96.20, elastik bandaj Bölüm XI.",
    "Optik eleman: işlenmemiş cam Fasıl 70 → monte edilmemiş 90.01 → alete monte 90.02 → tek başına alet 90.13.",
    "Tıp: genel 90.18; terapi-masaj 90.19; diğer solunum ve gaz maskesi 90.20; ortopedi-protez-işitme-kalp pili 90.21; X-ışını 90.22.",
    "Ölçü aletinde ölçülen büyüklük pozisyonu belirler (90.14–90.30); adıyla yer almayan ölçü aleti 90.31, otomatik ayarlayan alet 90.32.",
    "Notlardaki öncelikler: Not 4 (silah dürbünü, periskop → 90.13), Not 5 (90.13 / 90.31 → 90.31), Not 7 (90.32’nin sınırları).",
    "Parça: kendi pozisyonu → ait olduğu aletin pozisyonu → 90.33.",
    "Eşik ve tanımlar: terazide 5 cg (90.16); ortopedik ayakkabıda ölçüye göre ya da tek başına ve iki ayağa uygun (Not 6); lazerde 1 nanometre–1 milimetre dalga boyu.",
]

E = "Eşya → 4’lü pozisyon"
O = "Olumsuz teşhis"
F = "Farklı/aynı pozisyon veya fasıl"
T = "Fasıl notu · Tanım/Eşik"
G = "Genel Yorum Kuralı"
M = "Eşleştirme / Boşluk doldurma"
C = "Çoktan-çoğa (I–IV)"
S = "Senaryo"

sorular = [
    {  # 1 C
        "soru": "Tarife Cetveline göre, yüzeyleri istenen optik etkiyi verecek şekilde düzleştirilip cilalanmış, ancak herhangi bir çerçeveye monte edilmemiş camdan gözlük camı hangi pozisyonda sınıflandırılır?",
        "secenekler": ["70.15", "90.02", "90.01", "90.04", "90.03"],
        "cevap": "C", "tip": E,
        "gerekce": "90.01, optik tarzda işlenmiş (yüzeyi cilalanmış) fakat monte edilmemiş camdan optik elemanları kapsar; gözlük camları da bunlar arasındadır. Optik tarzda işlenmemiş gözlük camı 70.15’e gider (A tuzağı). 90.02 alete monte edilmiş optik elemanları, 90.03 gözlük çerçevelerini, 90.04 ise kullanıma hazır gözlükleri kapsar.",
        "dayanak": "Fasıl 90 Not 1(e); 90.01 ve 90.04 Açıklama Notları.",
    },
    {  # 2 A
        "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 90.18 pozisyonunda <b>sınıflandırılmaz</b>?",
        "secenekler": [
            "Hastanın ateşini ölçmeye mahsus klinik termometre",
            "Elektrikli ısıtma ve oksijen düzenleme tertibatlı bebek kuvözü",
            "Dişçilik aletleriyle donatılmış dişçi koltuğu",
            "Pıhtılaşmayı önleyici madde içeren, iğneli steril plastik kan torbası",
            "Elektrik akımı uygulayarak kalbi defibrile eden cihaz",
        ],
        "cevap": "A", "tip": O,
        "gerekce": "Tıpta ve veterinerlikte kullanılan termometreler 90.18’in hariç tutmaları arasında sayılmış olup 90.25’te sınıflandırılır. Kuvöz ve defibrilatör elektrikli tıbbi alet olarak, dişçilik donanımı içeren dişçi koltuğu ve suni maddeden steril kan torbası ise açıklama notunda adıyla 90.18’dedir. Dişçilik aletiyle birleştirilmemiş dişçi koltuğu ise 94.02’ye gider.",
        "dayanak": "90.18 Açıklama Notu, hariç tutmalar (p) ve (r); (I)(L), (II) ve (V) bölümleri.",
    },
    {  # 3 D
        "soru": "Tarife Cetveline göre hassas teraziler ile ilgili aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
        "secenekler": [
            "Hassasiyeti 5 miligram veya daha iyi olan teraziler 90.16 pozisyonunda yer alır.",
            "Kıymetli metallerden yapılmış ağırlıklar ayrı gelseler de 90.16 pozisyonunda kalır.",
            "Hassasiyeti 5 santigramdan az olan teraziler, laboratuvarda analiz amacıyla kullanılıyorsa 90.16’ya girer.",
            "Hassasiyeti 5 santigram veya daha iyi olan teraziler birlikte gelen ağırlıklarıyla 90.16’da yer alır.",
            "Kırat birimiyle taksimatlandırılmış kıymetli taş terazileri, hassasiyetlerine bakılmaksızın her durumda 84.23’te yer alır.",
        ],
        "cevap": "D", "tip": T,
        "gerekce": "90.16, hassasiyeti 5 santigram veya daha iyi olan her tip teraziyi birlikte gelen ağırlıklarıyla kapsar. Ayrı gelen ağırlıklar kıymetli metalden olsalar bile 84.23’e gider; hassasiyeti 5 santigramdan az teraziler de 84.23’tedir. Kıymetli taş terazileri 90.16 Açıklama Notunda adıyla sayılmıştır. Birim tuzağı: eşik miligram değil santigramdır.",
        "dayanak": "90.16 pozisyon metni ve Açıklama Notu; Fasıl 90 Not 1(g).",
    },
    {  # 4 B
        "soru": "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
        "secenekler": ["Taksimetre", "Planimetre", "Pedometre", "Stroboskop", "Elde tutulan sayaç"],
        "cevap": "B", "tip": F,
        "gerekce": "Taksimetre, pedometre, stroboskop ve elde tutulan sayaçlar 90.29 Açıklama Notunda adıyla sayılmıştır. Aynı not planimetreleri kapsam dışında bırakır; düz bir alanın yüzölçümünü ölçen planimetreler 90.31’de sınıflandırılır. Tuzak, planimetreyi sayaç benzeri bir ölçü aleti sanarak 90.29’a koymaktır.",
        "dayanak": "90.29 Açıklama Notu (A); 90.31 Açıklama Notu (I)(A)(5).",
    },
    {  # 5 E
        "soru": "Tarife Cetveline göre, konut kapılarına takılan ve kapının dışını görmeye yarayan optik sistemli kapı gözü (kapı merceği) hangi pozisyonda sınıflandırılır?",
        "secenekler": ["90.02", "90.05", "83.02", "90.01", "90.13"],
        "cevap": "E", "tip": E,
        "gerekce": "Kapı mercekleri 90.13 Açıklama Notunda adıyla sayılmıştır; 90.05 Açıklama Notu da kapı gözlerini 90.13’e yönlendirir. Kendi başına bir alet oluşturduğundan alete monte edilen optik eleman (90.02) veya monte edilmemiş optik eleman (90.01) sayılmaz. Kapı donanımı çağrışımı (83.02) yanıltıcıdır.",
        "dayanak": "90.13 Açıklama Notu (3); 90.05 Açıklama Notu, hariç tutma (d).",
    },
    {  # 6 B
        "soru": "Bir çift gözlü dürbün, kendisine göre şekil verilmiş, uzun süre kullanılmaya uygun deri mahfazası içinde ve normal olarak onunla birlikte satılan şekilde ithal edilmiştir. Mahfazanın sınıflandırılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
        "secenekler": [
            "GYK 3(b) uyarınca esas niteliği mahfaza verdiğinden 42.02’de",
            "GYK 5(a) uyarınca dürbünle birlikte 90.05’te",
            "GYK 5(b) uyarınca ambalaj olarak dürbünle birlikte 90.05’te",
            "GYK 1 uyarınca deri eşya olarak ayrıca 42.02’de",
            "GYK 2(a) uyarınca dürbünün aksamı sayılarak 90.33’te",
        ],
        "cevap": "B", "tip": G,
        "gerekce": "GYK 5(a), belirli bir eşyaya göre şekil verilmiş, uzun süre kullanılmaya uygun ve eşya ile birlikte sunulup normal olarak onunla satılan mahfazaları eşya ile birlikte sınıflandırır; kuralın açıklama notunda dürbün ve teleskop mahfazaları (90.05) örnek olarak sayılmıştır. GYK 5(b) yalnız normal ambalaj maddeleri içindir; mahfaza tek başına gelseydi kendi pozisyonunda sınıflandırılırdı.",
        "dayanak": "GYK 5(a) ve Açıklama Notu (II)(3).",
    },
    {  # 7 D
        "soru": "Fasıl 90 Not 2 ve Genel Açıklamalara göre aksam, parça ve aksesuar ile ilgili aşağıdaki ifadelerden hangileri doğrudur?<br/>I. Elektron mikroskobunda kullanılan, ayrı gelen vakum pompası 84.14’te sınıflandırılır.<br/>II. Mikroskopla kullanılmak üzere özel olarak imal edilmiş, ayrı gelen fotoğraf makinası mikroskop aksamı olarak 90.11’de sınıflandırılır.<br/>III. 90.01 veya 90.02’deki optik parçalar, yerleştirilecekleri alet ne olursa olsun bu pozisyonlarda kalır.<br/>IV. Fasıl 90’ın değişik pozisyonlarındaki çeşitli alet kategorileriyle kullanılmaya elverişli aksam ve aksesuar 90.33’te sınıflandırılır.",
        "secenekler": ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
        "cevap": "D", "tip": C,
        "gerekce": "Not 2(a) gereği kendi başına Fasıl 84, 85, 90 veya 91’de bir pozisyona giren parça o pozisyonda kalır: vakum pompası 84.14’te, optik parçalar 90.01 veya 90.02’de (I ve III doğru). Başka bir aletle kullanılmaya mahsus olsa bile fotoğraf makinası 90.06’da yer aldığından II yanlıştır. Birden fazla pozisyondaki aletlerle kullanılabilen parçalar Not 2(c) gereği 90.33’e gider (IV doğru).",
        "dayanak": "Fasıl 90 Not 2; Genel Açıklamalar (III); 90.06 Açıklama Notu.",
    },
    {  # 8 A
        "soru": "Bir firma; karbondioksit lazer kaynağı, iş parçasını taşıyan hareketli tabla, parçayı tespit ve ayarlama tertibatı ile işlem sırasında gözlem ve kontrol tertibatı bulunan, metal levhaları lazer ışınıyla kesen bir makina ithal etmiştir. Tarife Cetveline göre bu makina hangi pozisyonda sınıflandırılır?",
        "secenekler": ["84.56", "90.13", "85.15", "90.31", "84.62"],
        "cevap": "A", "tip": S,
        "gerekce": "90.13 yalnız lazerin kendisini (lazer başlığı ve birlikte sunulan yardımcı ünitelerle lazer sistemi) kapsar. İş tablası, tespit ve kontrol tertibatı gibi yardımcı donanımla belirli bir işi yapacak şekilde uyarlanmış lazerler 90.13 dışında kalır; lazerle madde işleyen takım tezgahları 84.56’dadır. Lazerli lehim ve kaynak makinaları 85.15’e gider; kesme işlevi ölçme aleti (90.31) niteliği de vermez.",
        "dayanak": "90.13 Açıklama Notu (1)(i) ve (ii).",
    },
    {  # 9 B
        "soru": "Tarife Cetveline göre, içten yanmalı bir motor, dinamo, ateşleme jeneratörü ve ölçü aletlerinden oluşan, benzinin oktan derecesini tayine mahsus laboratuvar cihazı hangi pozisyonda sınıflandırılır?",
        "secenekler": ["90.27", "90.31", "84.07", "90.24", "90.26"],
        "cevap": "B", "tip": E,
        "gerekce": "Yakıtların muayenesinde, özellikle benzinin oktan ve dizel yakıtının setan derecesinin tayininde kullanılan motorlu laboratuvar cihazları 90.31 Açıklama Notunda adıyla sayılmıştır. Cihaz bir motor içerse de motor olarak (84.07) sınıflandırılmaz. Fiziksel-kimyasal analiz (90.27), malzemenin mekanik özelliklerinin testi (90.24) ve akışkanların akış-basınç ölçümü (90.26) çeldiricidir.",
        "dayanak": "90.31 Açıklama Notu (I)(A)(3).",
    },
    {  # 10 E
        "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 90. Fasılda <b>sınıflandırılmaz</b>?",
        "secenekler": [
            "Jetonla çalışan, pozu anında basan kabin tipi fotoğraf makinası",
            "Optik parçaları takılmamış olarak gelen sinema kamerası",
            "Görüntü yoğunlaştırıcı tüplü gece görüş dürbünü",
            "Önceden film yüklenmiş tek kullanımlık fotoğraf makinası",
            "Görüntüyü elektronik olarak kaydeden dijital fotoğraf makinası",
        ],
        "cevap": "E", "tip": O,
        "gerekce": "Fasıl 90 Not 1(h) ve 90.06 Açıklama Notu dijital kameraları 85.25’e gönderir. Kabin tipi anında baskı yapan makinalar 84.76’da değil 90.06’da, tek kullanımlık makinalar 90.06’da, optik parçası olmayan sinema cihazları 90.07’de, ışık yükselteçli gece dürbünleri 90.05’tedir. Tuzak, “fotoğraf makinası” adını tek başına 90.06 için yeterli saymaktır.",
        "dayanak": "Fasıl 90 Not 1(h); 90.05, 90.06 ve 90.07 Açıklama Notları.",
    },
    {  # 11 C
        "soru": "Fasıl 90 Not 6’ya göre ortopedik koşulları düzeltmek üzere tasarlanmış ayakkabı ve özel iç tabanlar, ölçüye göre yapılmamış ve seri halde üretilmişlerse hangi şartla “ortopedik cihaz” sayılır?",
        "secenekler": [
            "Çift halinde sunulmaları ve hekim reçetesine dayanılarak satılmaları şartıyla",
            "Dış tabanlarının kauçuk veya plastikten, sayalarının deriden yapılmış olması şartıyla",
            "Tek başlarına sunulmaları ve her iki ayağa eşit şekilde uyacak biçimde tasarlanmaları şartıyla",
            "İç tabanlarının düz tabanlığı hafifletmek amacıyla basitçe kabartılarak komple üretilmiş olması şartıyla",
            "Perakende satış için iki ayak birlikte, kutusunda takım halinde sunulmaları şartıyla",
        ],
        "cevap": "C", "tip": T,
        "gerekce": "Not 6, ortopedik ayakkabı ve özel iç tabanları ya ölçüye göre yapılmışsa ya da seri halde üretilmiş olup çift halinde değil tek başına sunulan ve her iki ayağa eşit şekilde uyacak biçimde tasarlanmışsa ortopedik cihaz sayar. İç tabanı düz tabanlık için basitçe kabartılmış hazır ayakkabılar ortopedik sayılmaz ve Fasıl 64’te kalır (D tuzağı). Yapıldığı madde ölçüt değildir; çift halinde sunulma ise şartın tersidir.",
        "dayanak": "Fasıl 90 Not 6; 90.21 Açıklama Notu (I) ve hariç tutma (d).",
    },
    {  # 12 A
        "soru": "Tarife Cetveline göre aşağıdaki eşya – pozisyon eşleştirmelerinden hangisi <b>yanlıştır</b>?",
        "secenekler": [
            "Fotoğrafçılıkta poz süresini ölçen pozometre – 90.06",
            "Radyografileri incelemeye mahsus negatoskop – 90.10",
            "Opak cisimlerin görüntüsünü perdeye aksettiren episkop – 90.08",
            "Domuz etini incelemeye mahsus trişinoskop – 90.11",
            "Kat radyatörlerine takılan küçük tip kalorimetre – 90.26",
        ],
        "cevap": "A", "tip": M,
        "gerekce": "Pozometreler kameralara takılmak üzere hazırlanmış olsalar bile 90.27’de sınıflandırılır; 90.06 Açıklama Notu bunları açıkça hariç tutar. Negatoskop 90.10’da, episkop sabit görüntü projektörü olarak 90.08’de, trişinoskop özel amaçlı mikroskop olarak 90.11’de, ısıtma bedelini bölüştürmeye yarayan radyatör kalorimetresi 90.26’dadır.",
        "dayanak": "90.06 Açıklama Notu, hariç tutmalar; 90.08, 90.10, 90.11, 90.26 ve 90.27 Açıklama Notları.",
    },
    {  # 13 D
        "soru": "Tarife Cetveline göre aşağıdaki alet ve cihazlardan hangisi diğerlerinden farklı bir pozisyonda sınıflandırılır?",
        "secenekler": ["Refraktometre", "Polarimetre", "Mikrotom", "Manometre", "Viskozimetre"],
        "cevap": "D", "tip": F,
        "gerekce": "Refraktometre ve polarimetre (fiziksel-kimyasal analiz), viskozimetre (akışkanlık ölçümü) ve mikrotom 90.27’de yer alır. Kapalı bir yerdeki sıvı veya gaz basıncını ölçen manometre ise 90.26’dadır. Tuzak, “-metre” ile biten her ölçü aletini aynı pozisyona koymaktır.",
        "dayanak": "90.26 ve 90.27 pozisyon metinleri ve Açıklama Notları.",
    },
    {  # 14 E
        "soru": "Tarife Cetveline göre, pusulanın okumalarına göre geminin dümenini kumanda eden otomatik pilot (gyro pilot) hangi pozisyonda sınıflandırılır?",
        "secenekler": ["90.32", "85.26", "90.15", "84.79", "90.14"],
        "cevap": "E", "tip": E,
        "gerekce": "Pusula okumalarına göre geminin dümenini kontrol eden otomatik pilotlar, 90.14 Açıklama Notunda deniz seyrüseferine ait aletler arasında adıyla sayılmıştır; uçak otomatik pilotları da aynı pozisyondadır. Otomatik kontrol yapması onu 90.32’ye götürmez. Radar ve radyo ile seyrüsefer cihazları 85.26’da, arazi ölçme ve meteoroloji aletleri 90.15’tedir.",
        "dayanak": "90.14 Açıklama Notu (II)(B)(1) ve (C)(7); Fasıl 90 Not 1(h).",
    },
    {  # 15 B
        "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 90.04 pozisyonunda <b>sınıflandırılmaz</b>?",
        "secenekler": [
            "Kâğıt çerçeveli, plastik polarizan camlı üç boyutlu film gözlüğü",
            "Kaynakçılara mahsus, yüzün önemli bir kısmını koruyan siper",
            "Röntgen teknisyenlerinin kullandığı kurşunlu camdan koruyucu gözlük",
            "Kış sporlarında kullanılan güneş gözlüğü",
            "Görme kusurunu düzeltmeye mahsus tek gözlük (monokl)",
        ],
        "cevap": "B", "tip": O,
        "gerekce": "90.04 yalnız gözleri kaplayacak şekilde yapılmış gözlükleri kapsar; yüzün önemli bir kısmını maskeleyen veya koruyan kaynakçı siperleri, motosikletçi kask ve vizyerleri ile sualtı maskeleri bu pozisyon dışındadır. Üç boyutlu film gözlükleri (çerçevesi kâğıttan olsa da), kış sporu güneş gözlükleri ve görme düzeltici tek gözlükler 90.04’te sayılmıştır; kurşunlu camdan teknisyen gözlükleri de 90.22 Açıklama Notunda 90.04’e yönlendirilmiştir.",
        "dayanak": "90.04 Açıklama Notu; 90.22 Açıklama Notu, aksam-parça bölümü.",
    },
    {  # 16 E
        "soru": "Fasıl 90 Not 7’ye göre 90.32 pozisyonunun kapsamı ile ilgili aşağıdaki ifadelerden hangisi <b>doğrudur</b>?",
        "secenekler": [
            "Elektriksel olmayan miktarları otomatik kontrol eden aletler, çalışmaları kontrol edilen faktöre göre değişen bir elektrik olayına bağlı olmasa da 90.32’ye girer.",
            "Termostat yoluyla kontrol edilen valfler, sıcaklığı otomatik kontrol ettiklerinden 90.32’de yer alır.",
            "Programlanabilir kontrol cihazları, otomatik kontrol yaptıklarından 90.32’de yer alır.",
            "Ölçtüğü değeri istenen değerle karşılaştırmayan, yalnız gösteren basınç ölçerler de 90.32’de yer alır.",
            "Sıvı veya gazların akış, seviye ve basıncını ya da sıcaklığı otomatik kontrol eden aletler, elektrik olayına bağlı olmasalar da 90.32’ye girebilir.",
        ],
        "cevap": "E", "tip": T,
        "gerekce": "Not 7(a), sıvı-gaz değişkenlerini ve sıcaklığı otomatik kontrol eden aletleri çalışmalarının bir elektrik olayına bağlı olup olmamasına bakmaksızın 90.32’ye alır; elektriksel olmayan diğer miktarlar için ise Not 7(b) elektrik olayına bağlılığı şart koşar (A yanlış). Termostatla kontrol edilen valfler 84.81’de, programlanabilir kontrol cihazları 85.37’de, yalnız ölçen aletler 90.25, 90.26 veya 90.30’dadır.",
        "dayanak": "Fasıl 90 Not 7(a) ve (b); 90.32 Açıklama Notu, hariç tutmalar.",
    },
    {  # 17 C
        "soru": "Tarife Cetveline göre aşağıdakilerden hangisi diğerlerinden farklı bir fasılda sınıflandırılır?",
        "secenekler": ["Kontakt lens", "Kalp pili", "Video projektörü", "Sinema projektörü", "Takometre"],
        "cevap": "C", "tip": F,
        "gerekce": "Video projektörleri 90.07 Açıklama Notunda hariç tutulmuş olup 85.28’de, yani Fasıl 85’te sınıflandırılır. Kontakt lens 90.01’de, kalp pili 90.21’de, sinema projektörü 90.07’de, takometre 90.29’da olmak üzere diğerleri Fasıl 90’dadır. Tuzak, sinema projektörü ile video projektörünü aynı yere koymaktır.",
        "dayanak": "90.07 Açıklama Notu, hariç tutmalar; 90.01, 90.21 ve 90.29 pozisyon metinleri.",
    },
    {  # 18 D
        "soru": "Objektif, oküler ve aynası takılmamış olarak gelen; iskeleti, tüpleri ve ayar tertibatı tamam olan bileşik optik mikroskop hangi Genel Yorum Kuralı ile hangi pozisyonda sınıflandırılır?",
        "secenekler": ["GYK 3(a) – 90.02", "GYK 2(b) – 90.11", "GYK 4 – 90.13", "GYK 2(a) – 90.11", "GYK 1 – 90.33"],
        "cevap": "D", "tip": G,
        "gerekce": "Fasıl 90 Genel Açıklamaları (II), GYK 2(a)’ya atıfla, optik aksamı takılmamış mikroskop veya fotoğraf makinasını tamamlanmış eşyanın asli niteliğini taşıdığı için tamamlanmış eşya gibi sınıflandırır; 90.11 Açıklama Notu da optik unsurları bulunsun bulunmasın mikroskopları kapsar. GYK 2(b) madde karışım ve bileşimleriyle ilgilidir; eksik mikroskop parça (90.33) veya optik eleman (90.02) sayılmaz.",
        "dayanak": "GYK 2(a); Fasıl 90 Genel Açıklamalar (II); 90.11 Açıklama Notu.",
    },
    {  # 19 A
        "soru": "Fasıl 90 Not 1’e göre aşağıdaki ifadelerden hangileri doğrudur?<br/>I. Motorlu taşıtlarda kullanılan türden projektörler 85.12 pozisyonunda sınıflandırılır.<br/>II. Monopod, bipod, tripod ve benzeri eşya, belirli bir alet için özel olarak yapılmış olsa bile 96.20’de yer alır.<br/>III. Hacim ölçmeye mahsus ölçü kapları, ölçü aleti oldukları için Fasıl 90’da sınıflandırılır.<br/>IV. Sayısal kontrol cihazları otomatik kontrol cihazı olarak 90.32 pozisyonunda yer alır.",
        "secenekler": ["I ve II", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"],
        "cevap": "A", "tip": C,
        "gerekce": "Not 1(h) taşıt ve bisiklet projektörlerini 85.12’ye, Not 1(l) monopod, bipod ve tripodları 96.20’ye gönderir; 90.15 ve 90.16 Açıklama Notları bunların alete özel yapılmış olsalar bile hariç olduğunu belirtir. Not 1(m) kapasite ölçü aletlerini mamul oldukları maddeye göre sınıflandırır (III yanlış); Not 1(h) sayısal kontrol cihazlarını 85.37’ye gönderir (IV yanlış).",
        "dayanak": "Fasıl 90 Not 1(h), (l) ve (m); 90.15 ve 90.16 Açıklama Notları.",
    },
    {  # 20 C
        "soru": "Hastanın yatağına sabitlenen şeffaf plastik bir çadırdan oluşan; çadır içine oksijen veya oksijen-karbondioksit karışımı besleyen ve gerektiğinde ilaçların mikro-sprey halinde teneffüs edilmesini de sağlayan cihaz Tarife Cetveline göre hangi pozisyonda sınıflandırılır?",
        "secenekler": ["90.18", "90.20", "90.19", "63.06", "84.24"],
        "cevap": "C", "tip": S,
        "gerekce": "Oksijen tedavisi ve aerosol tedavisi cihazları (oksijen çadırları dahil) 90.19’dadır; çadırları ve onları sabitleyen tertibat da bu pozisyonun aksamı olarak sayılmıştır. 90.20 havacı, dalgıç, itfaiyeci gibi kullanıcılara ait diğer solunum cihazları ve gaz maskeleri içindir. Hiperbarik odalar 90.18’e gider; çadır görünümü (63.06) ve püskürtme işlevi (84.24) yanıltıcıdır.",
        "dayanak": "90.19 Açıklama Notu (V)(B), (VI) ve aksam-parça bölümü; 90.20 Açıklama Notu.",
    },
    {  # 21 D
        "soru": "Tarife Cetveline göre, hastaya verilen radyoaktif izleyicinin vücuttaki dağılımını sintilasyon sayacıyla tarayarak organın görüntüsünü çıkaran tıbbi teşhis cihazı (gama kamera) hangi pozisyonda sınıflandırılır?",
        "secenekler": ["90.22", "90.30", "85.25", "90.18", "90.06"],
        "cevap": "D", "tip": E,
        "gerekce": "Sintigrafik tıbbi aletler (gama kamera, sintilasyon tarayıcı) 90.18’in pozisyon metninde ve açıklama notunda yer alır; 90.30 Açıklama Notu da tıbbi teşhis amaçlı sintilasyon sayaçlı cihazları kapsam dışında bırakır. Radyoaktif kaynakla çalışan radyografi ve ölçüm cihazları 90.22’dedir; “kamera” adı ise eşyayı 85.25 veya 90.06’ya götürmez.",
        "dayanak": "90.18 pozisyon metni ve Açıklama Notu (IV); 90.30 Açıklama Notu, hariç tutma (a).",
    },
    {  # 22 E
        "soru": "Tarife Cetveline göre aşağıdakilerden hangisi 90.20 pozisyonunda <b>sınıflandırılmaz</b>?",
        "secenekler": [
            "İtfaiyecilerin kullandığı, portatif basınçlı hava tüpüyle beslenen solunum cihazı",
            "Dalgıç elbiselerine takılmaya mahsus dalgıç başlığı",
            "Solunum cihazıyla birleştirilmiş radyasyon geçirmez koruyucu elbise",
            "Değiştirilebilir filtre kartuşlu, göz siperli gaz maskesi",
            "Değiştirilebilir filtresi olmayan, aktif karbonlu dokuma tabakalı toz maskesi",
        ],
        "cevap": "E", "tip": O,
        "gerekce": "90.20 pozisyon metni, mekanik parçası ve değiştirilebilen filtresi olmayan koruyucu maskeleri kapsam dışında bırakır; dokumaya elverişli maddeden bu tür toz ve koku maskeleri aktif karbonla işlem görmüş olsa da 63.07’dedir. Basınçlı hava tüplü solunum cihazları, dalgıç başlıkları, solunum cihazıyla birleşik koruyucu elbiseler ve filtreli gaz maskeleri 90.20’dedir.",
        "dayanak": "90.20 pozisyon metni ve Açıklama Notu, hariç tutma (a).",
    },
    {  # 23 B
        "soru": "Fasıl 90 Not 1(f) hükmüne göre aşağıdakilerden hangisi 90.21 pozisyonunda sınıflandırılır?",
        "secenekler": [
            "Cerrahi alet ve cihazlarda kullanılan, adi metalden genel kullanıma mahsus yaylar ve benzeri parçalar",
            "Tıpta implant olarak kullanılmak üzere özel olarak dizayn edilmiş adi metal vidalar",
            "Gözlük çerçevelerinde kullanılan, adi metalden vidalar",
            "Plastikten, genel kullanıma mahsus bağlantı parçaları",
            "Tespite yarayan tertibatı olmayan, adi metalden gözlük zincirleri",
        ],
        "cevap": "B", "tip": T,
        "gerekce": "Not 1(f), Bölüm XV Not 2’deki adi metalden genel kullanıma mahsus parçaları ve plastikten benzerlerini Fasıl 90 dışında bırakır; ancak özel olarak tıbbi, cerrahi, dişçilik veya veterinerlik bilimlerinde implant olarak kullanılmak üzere dizayn edilmiş eşyayı 90.21’e alır. Gözlük çerçevelerindeki adi metal vidalar, tespit tertibatı olmayan zincirler ve yaylar 90.03 Açıklama Notu gereği kendi pozisyonlarındadır.",
        "dayanak": "Fasıl 90 Not 1(f); 90.03 ve 90.21 Açıklama Notları.",
    },
    {  # 24 A
        "soru": "Fasıl 90 Not 5’e göre: “Hem …… hem de …… pozisyonunda sınıflandırılabilen optik ölçü veya kontrol makina, cihaz ve aletleri …… pozisyonunda sınıflandırılır.” Boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
        "secenekler": ["90.13 – 90.31 – 90.31", "90.13 – 90.31 – 90.13", "90.02 – 90.31 – 90.31", "90.13 – 90.27 – 90.27", "90.05 – 90.13 – 90.13"],
        "cevap": "A", "tip": M,
        "gerekce": "Not 5, hem 90.13 hem 90.31’e girebilecek optik ölçü veya kontrol aletlerini 90.31’e verir; 90.13 Açıklama Notu da optik ölçü, muayene ve kontrol aletlerinin 90.13’e dahil olmadığını belirtir. Bu nedenle optik komparatör, hiza teleskobu ve fosimetre gibi aletler 90.31’dedir. E şıkkındaki 90.05–90.13 ilişkisi ise Not 4’e (silah dürbünü, periskop) aittir.",
        "dayanak": "Fasıl 90 Not 4 ve 5; 90.13 ve 90.31 Açıklama Notları.",
    },
    {  # 25 C
        "soru": "Tarife Cetveline göre aşağıdaki seçeneklerin hangisinde yer alan eşyanın tamamı aynı 4’lü pozisyonda sınıflandırılır?",
        "secenekler": [
            "Mikrometre, kumpas, şerit metre, inşaatçı su terazisi",
            "Yalnız yükseklik gösteren altimetre, sekstant, pusula, barometre",
            "Teodolit, sismograf, meteorolojik anemometre, telemetre",
            "Debimetre, manometre, gaz sayacı, seviye göstergesi",
            "Elektron mikroskobu, stereoskopik mikroskop, cerrahi mikroskop, trişinoskop",
        ],
        "cevap": "C", "tip": F,
        "gerekce": "Teodolit (arazi ölçme), sismograf (jeofizik), meteorolojik anemometre ve telemetre 90.15’tedir. A’da inşaatçı su terazisi 90.31’e, B’de barometre 90.25’e, D’de gaz sayacı 90.28’e, E’de elektron mikroskobu 90.12’ye gider; her seçeneğin diğer eşyası sırasıyla 90.17, 90.14, 90.26 ve 90.11’dedir.",
        "dayanak": "90.15 pozisyon metni ve Açıklama Notu; 90.12, 90.25, 90.28 ve 90.31 Açıklama Notları.",
    },
]

d = {
    "tur": "fasil",
    "fasil": 90,
    "baslik": "Optik alet ve cihazlar, fotoğraf, sinema, ölçü, kontrol, ayar alet ve cihazları, tıbbi veya cerrahi alet ve cihazlar; bunların aksam, parça ve aksesuarı",
    "bolum": "XVIII",
    "oz": oz,
    "karar_tablosu": karar_tablosu,
    "pozisyon_haritasi": pozisyon_haritasi,
    "notlar": notlar,
    "sinir_komsulari": sinir_komsulari,
    "tuzaklar": tuzaklar,
    "hafiza": hafiza,
    "sinav_odagi": sinav_odagi,
    "cikmis_ornekler": cikmis_ornekler,
    "ozet": ozet,
    "sorular": sorular,
}

out = os.path.join(K, "data", "fasil_90.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("yazıldı:", out)
