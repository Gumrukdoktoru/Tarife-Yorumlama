#!/usr/bin/env python3
"""Hap bilgi sayfaları: Fasıl 86–92 (grup H8)."""
import json
import os
import re

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KITAP, "hap")

H = {}

# ---------------------------------------------------------------- 86 (C)
H[86] = {
    "tur": "hap", "fasil": 86, "kademe": "C",
    "sinavda": "Son 5 sınavda 1 kez, Fasıl 70 sorusu içinde: lokomotifin ısıtma tertibatlı ön camı Fasıl 70’e "
               "girmez (70 Not 1(e)), taşıt aksamıdır; ısıtmasız çerçevesiz ön cam Fasıl 70’te kalır.",
    "pozisyonlar": [
        ["86.01", "Elektrikli lokomotif: dış kaynak veya akümülatör"],
        ["86.07", "Aksam: boji, dingil, tekerlek, fren, tampon"],
        ["86.08", "Birleştirilmiş hat; mekanik-elektromekanik sinyal (karayolu dahil)"],
        ["86.09", "Bir veya daha fazla taşıma şekline özel konteyner"],
    ],
    "hap": [
        "<b>Bölüm XVII Not 4–5:</b> karayolu-ray için özel taşıt ve amfibi motorlu taşıt 87; kara taşıtı da "
        "olan uçak 88. Hava yastıklı: kılavuz hatlı 86, karada veya kara-suda 87, suda 89.",
        "<b>Fasıl 86 Not 1:</b> ahşap travers 44.06, beton travers 68.10, demir-çelik ray ve hat malzemesi "
        "73.02, elektrikli sinyalizasyon 85.30 fasıl dışı; traverslerle birleştirilmiş hat ise 86.08.",
        "<b>Lokomotif:</b> elektriği dışarıdan veya akümülatörden alan 86.01; dizel, buharlı ve tender 86.02; "
        "bakım-servis taşıtı kendinden hareketli olsun olmasın 86.04.",
    ],
    "karistirilan": [
        ["Lokomotifin ısıtma tertibatlı ön camı", "86.07", "70 Not 1(e): ısıtmalı taşıt camı Fasıl 70 dışı, aksamdır"],
        ["Elektrikli trafik sinyal cihazı", "85.30", "86 Not 1(c); mekanik veya elektromekanik olan 86.08"],
    ],
}

# ---------------------------------------------------------------- 87 (A)
H[87] = {
    "tur": "hap", "fasil": 87, "kademe": "A",
    "sinavda": "Son 5 sınavda 4 kez konu, 7 kez seçenek: pedalsız, ayakla itilen iki tekerlekli araç 87.16 "
               "(GYK 1 ve 6), far-stop camı 87 dışı (70.14), 87.10’da binek otomobile ait ürün yok, 87.02 alt "
               "pozisyon açılımı. Çeldirici kalıbı: traktöre takılan kültivatör 84.32, elektrikli cam silici 85.12, "
               "üç tekerlekli bisiklet 95.03, buz pisti düzeltme makinesi 84.79.",
    "pozisyonlar": [
        ["87.01", "Traktör: esas işi çekmek veya itmek"],
        ["87.02", "Sürücü dahil 10 veya daha fazla kişi"],
        ["87.03", "İnsan taşıma: otomobil, ambulans, karavan, golf arabası"],
        ["87.04", "Eşya taşıma: kamyon, pick-up, damper"],
        ["87.05", "Taşıma dışı hizmet: itfaiye, kurtarıcı, beton mikseri"],
        ["87.06", "Motorlu şasi, sürücü mahalli yok"],
        ["87.08", "87.01–87.05 aksamı: fren, tampon, radyatör, kemer"],
        ["87.09", "Kaldırma tertibatsız kısa mesafe yük arabası"],
        ["87.10", "Tank, zırhlı savaş taşıtı ve aksamı"],
        ["87.11", "Motosiklet, mopet, yan sepet"],
        ["87.12", "Motorsuz bisiklet (çocuk bisikleti dahil)"],
        ["87.16", "Römork; el, ayak veya hayvanla yürüyen taşıt"],
    ],
    "hap": [
        "<b>Bölüm XVII Not 2 (aksam sayılmaz):</b> conta 84.84, genel kullanım parçası, Fasıl 82 aleti, 83.06, "
        "84.01–84.79 makinesi (radyatör hariç), 84.81, 84.82, Fasıl 85, 90, 91, 93, lamba 94.05, fırça 96.03.",
        "<b>Aksam şartı (XVII Not 3):</b> yalnız veya esas itibarıyla bu taşıtlara uygun olmalı, daha belirli yer "
        "olmamalı: lastik 40.11, çerçevesiz emniyet camı 70.07, dikiz aynası 70.09, koltuk 94.01 dışarıda.",
        "<b>Not 2 (traktör):</b> esas işi başka taşıt, cihaz veya yükü çekmek-itmek. Traktöre takılan alet monte "
        "gelse de kendi faslında: kültivatör, pulluk 84.32; çayır biçme 84.33.",
        "<b>87.03 / 87.04:</b> emniyet kemerli koltuk, arka yan cam, bölme panel yokluğu ve konfor donanımı 87.03; "
        "bank koltuk, penceresiz yan panel, daimi bölme ve çıplak yük alanı 87.04.",
        "<b>Şasi (Not 3):</b> motor ve sürücü mahalli varsa 87.02–87.04; motorlu ama sürücü mahallisiz 87.06; "
        "motorsuz şasi 87.08; karoser ve sürücü kabini 87.07.",
        "<b>Not 1 ve Not 4:</b> yalnız raylar üzerinde giden taşıt Fasıl 86. Çocuklar için her türlü bisiklet "
        "87.12; diğer tekerlekli çocuk araçları (üç tekerlekli çocuk bisikleti, pedallı araba) 95.03.",
        "<b>Ayakla itilen taşıt:</b> sele, pedal ve krank dişlisi olmayan iki tekerlekli araç bisiklet değildir; "
        "elle veya ayakla hareket ettirilen taşıt olarak 87.16’dadır (GYK 1 ve 6).",
        "<b>87.09:</b> fabrika, liman, havalimanında kısa mesafe yük arabası; kaldırma tertibatı yok, yüklü hızı "
        "genellikle 30–35 km/saati geçmez. Forklift ve kaldırma tertibatlı yük arabası 84.27.",
    ],
    "karistirilan": [
        ["Traktöre takılan kültivatör", "84.32", "87 Not 2: monte gelse de alet kendi faslında"],
        ["Elektrik motorlu cam silici; far", "85.12", "Bölüm XVII Not 2(f): Fasıl 85 eşyası aksam sayılmaz"],
        ["Taşıt far ve stop camı", "70.14", "İşaret camı; daha belirli yer, Fasıl 87 dışı"],
        ["Üç tekerlekli çocuk bisikleti", "95.03", "87 Not 4; iki tekerlekli çocuk bisikleti 87.12"],
        ["Buz pisti yüzey düzeltme makinesi", "84.79", "Kendinden hareketli olsa da 87.05 değil"],
        ["Taşıt motoru; krank mili", "84.07", "Not 2(e): motor Fasıl 84; krank mili 84.83"],
    ],
}

# ---------------------------------------------------------------- 88 (B)
H[88] = {
    "tur": "hap", "fasil": 88, "kademe": "B",
    "sinavda": "Son 5 sınavda 1 kez konu: dijital kameralı, uzaktan kumandalı drone 88.06 (85.25, 88.04, 88.05, "
               "88.07 çeldirici). Seçeneklerde 2 kez: deniz taşıtı dizel motoru (84.08) ve römorkör (89.04) "
               "sorularında 88.02 ve 88.04 çeldirici.",
    "pozisyonlar": [
        ["88.01", "Balon, hava gemisi, planör, delta kanat, uçurtma"],
        ["88.02", "Motorlu uçak, helikopter; uydu, uzay fırlatıcısı"],
        ["88.04", "Paraşüt, yamaç paraşütü, rotoşüt ve aksamı"],
        ["88.05", "Fırlatma-iniş tertibatı; yerde uçuş simülatörü"],
        ["88.06", "İnsansız hava taşıtı (drone)"],
        ["88.07", "88.01, 88.02, 88.06 aksamı: pervane, kanat, iniş takımı"],
    ],
    "hap": [
        "<b>Not 1 (insansız hava taşıtı):</b> 88.01 dışında, içinde pilot olmadan uçmak üzere tasarlanmış her "
        "hava aracı; yük veya kalıcı entegre kamera taşıyabilir → 88.06. Yalnız eğlence amaçlı uçan oyuncak 95.03.",
        "<b>Motor ölçütü:</b> balon ve hava gemisi motorlu olsa da 88.01; planör motorlu veya motor takılacak "
        "tasarımdaysa 88.02. Meteorolojik balon ve uçurtma 88.01, oyuncak olanlar 95.03.",
        "<b>7000 m/s:</b> yüküne 7000 m/s’den fazla son hız veren uzay fırlatıcısı 88.02; bu hızı aşmayan balistik "
        "füze ve askeri fırlatma aracı 93.06.",
        "<b>Aksam sayılmaz (Bölüm XVII Not 2):</b> uçak motoru 84.07–84.12, elektrik teçhizatı Fasıl 85, "
        "göstergeler Fasıl 90, saat Fasıl 91, ön lamba 94.05; koltuk 94.01. 88.03 numarası boştur.",
    ],
    "karistirilan": [
        ["Dijital kameralı drone", "88.06", "Kamera taşısa da 85.25 değil; oyuncak ise 95.03"],
        ["Roket fırlatma rampası", "84.79", "Uçak fırlatma tertibatı 88.05; planör vinci 84.25"],
    ],
}

# ---------------------------------------------------------------- 89 (C)
H[89] = {
    "tur": "hap", "fasil": 89, "kademe": "C",
    "sinavda": "Son 5 sınavda 1 kez konu: römorkörler 89.04 (84.08, 87.01, 87.16, 88.04 çeldirici). Seçenekte: "
               "deniz taşıtı dizel motoru gemiye mahsus olsa da 84.08’dedir, 89.03 değil.",
    "pozisyonlar": [
        ["89.01", "Yolcu, feribot, yük gemisi, tanker, mavna"],
        ["89.03", "Yat, eğlence-spor teknesi, kürekli kayık, kano"],
        ["89.04", "Römorkör ve itici gemi"],
        ["89.05", "Fener, yangın, tarak gemisi; yüzer vinç, havuz"],
    ],
    "hap": [
        "<b>Gemi aksamı Fasıl 89’da yoktur</b> (tekne hariç): motor 84.08, pervane 84.87, dümen-sevk teçhizatı "
        "84.79, çapa 73.16, yelken 63.06, halat 56.07, ahşap kürek 44.21.",
        "<b>Not 1:</b> tamamlanmamış gemi veya tekne belirli gemi türünün temel özelliğine sahipse o pozisyonda, "
        "değilse 89.06. Sökülmek için getirilen gemi 89.08.",
        "<b>Ortam ölçütü:</b> amfibi motorlu taşıt Fasıl 87, deniz uçağı 88.02; suda işleyen hava yastıklı taşıt "
        "89; yüzer vasıtaya monte hareketli makine (yüzer vinç, tarama) 89.",
    ],
    "karistirilan": [
        ["Gemi pervanesi", "84.87", "Fasıl 89’da aksam hükmü yok; uçak pervanesi 88.07"],
        ["Yangın söndürme donanımlı römorkör", "89.04", "Yalnız yangın söndürme gemisi ise 89.05"],
    ],
}

# ---------------------------------------------------------------- 90 (A)
H[90] = {
    "tur": "hap", "fasil": 90, "kademe": "A",
    "sinavda": "Son 5 sınavda 5 kez konu, 5 kez seçenek: “aynı 4’lü pozisyonda olmayan” taraması (termometre-"
               "barometre 90.25 ≠ mikrometre 90.17), su terazisi 90.31, kabartma dünya haritası 90.23, dişçi "
               "tornası fırçası 90.18, ortopedik ayakkabı 90.21. Seçeneklerde: kontakt lens, sinema kamerası, "
               "kalp pili, takometre aynı fasıl; dişçilikte kullanılan alçı 25.20.",
    "pozisyonlar": [
        ["90.01", "Monte edilmemiş işlenmiş optik eleman; kontakt lens"],
        ["90.04", "Gözlükler: düzeltici, güneş, koruyucu"],
        ["90.17", "Çizim-hesap aleti; elde uzunluk ölçüsü (mikrometre)"],
        ["90.18", "Tıp, dişçilik, veteriner aletleri; dişçi tornası fırçası"],
        ["90.21", "Ortopedi, protez, işitme cihazı, kalp pili"],
        ["90.23", "Yalnız teşhir modeli; kabartma harita ve küre"],
        ["90.25", "Termometre, barometre, higrometre, hidrometre"],
        ["90.26", "Akış, seviye, basınç: debimetre, manometre, kalorimetre"],
        ["90.27", "Analiz, ışık-ses ölçümü: spektrometre, pozometre, mikrotom"],
        ["90.29", "Devir-hız: taksimetre, pedometre, takometre, stroboskop"],
        ["90.31", "Başka yerde olmayan ölçü aleti; su terazisi"],
        ["90.32", "Otomatik ayar-kontrol: termostat, manostat"],
    ],
    "hap": [
        "<b>Not 1 hariçleri:</b> dijital kamera 85.25; radar, GPS, telsiz uzaktan kumanda 85.26; optik "
        "işlenmemiş ayna 70.09; cam laboratuvar eşyası 70.17; elastik bandaj Bölüm XI; tripod 96.20; oyuncak Fasıl 95.",
        "<b>Not 2 (parça):</b> kendisi Fasıl 84, 85, 90 veya 91’de pozisyonu olan parça orada; belirli alete "
        "özgü parça o aletin pozisyonunda; diğer bütün parçalar 90.33.",
        "<b>Optik eleman zinciri:</b> optik tarzda işlenmemiş cam Fasıl 70 → işlenmiş, monte edilmemiş 90.01 → "
        "alete monte 90.02 → kendi başına alet (büyüteç, kapı gözü) 90.13.",
        "<b>Not 4–5:</b> silah nişan dürbünü, tank ve denizaltı periskobu 90.05 değil 90.13; hem 90.13 hem "
        "90.31’e uyan optik ölçü-kontrol aleti 90.31.",
        "<b>Not 6 (ortopedik ayakkabı):</b> ölçüye göre yapılmış ya da seri üretilip çift değil tek sunulan ve iki "
        "ayağa eşit uyan ayakkabı veya iç taban 90.21; değilse Fasıl 64.",
        "<b>Not 7 (90.32):</b> ölçtüğü değeri istenen değerle karşılaştırıp otomatik düzelten ve orada tutan alet "
        "(termostat, manostat). Yalnız ölçen termometre 90.25, manometre 90.26.",
        "<b>Eşikler:</b> hassasiyeti 5 cg veya daha iyi terazi 90.16, daha az hassası 84.23; lazer 1 nm–1 mm "
        "dalga boyu; elde kullanılan uzunluk ölçüsü 90.17, ayağa sabitlenmişse 90.31.",
        "<b>Tıpta kullanılan her alet 90.18 değil:</b> klinik termometre 90.25, tahlil aleti 90.27, X-ışını cihazı "
        "90.22, gözlük 90.04, tekerlekli sandalye 87.13, hastane mobilyası 94.02.",
    ],
    "karistirilan": [
        ["Dijital fotoğraf makinası, video kamera", "85.25", "Not 1(h); film esaslı fotoğraf makinası 90.06"],
        ["Telsiz uzaktan kumanda; GPS alıcısı", "85.26", "Not 1(h); 90.14 veya 90.15 değil"],
        ["Dişçilikte kullanılan alçı", "25.20", "Alçı esaslı dişçilik müstahzarı 34.07; 90.21 değil"],
        ["Dişçi tornasına mahsus fırça", "90.18", "Tıbbi-dişçilik fırçası 96.03’e girmez"],
        ["Basılı kabartma (rölyef) dünya haritası", "90.23", "Basılı olsa da 49.05 değil; teşhir modeli"],
        ["Tek kullanımlık cerrah veya toz maskesi", "63.07", "Mekanik parçası, değiştirilebilir filtresi yok; 90.20 değil"],
    ],
}

# ---------------------------------------------------------------- 91 (C)
H[91] = {
    "tur": "hap", "fasil": 91, "kademe": "C",
    "sinavda": "Son 5 sınavda doğrudan sorulmadı; seçeneklerde 2 kez: “saat 91. fasılda” doğru ifade olarak ve "
               "kol saatinin güneş gözlüğü-gitarla aynı bölümde (XVIII) olduğu bilgisiyle.",
    "pozisyonlar": [
        ["91.01", "Zarfı tamamen kıymetli metal/kaplama kol-cep saati"],
        ["91.02", "Diğer kol-cep saatleri (kakmalı adi metal dahil)"],
        ["91.03", "Not 3 makinalı masa, duvar, çalar saat"],
        ["91.04", "Taşıt, uçak, gemi alet tablosu saati"],
    ],
    "hap": [
        "<b>Not 3 (saat makinası):</b> kalınlık ≤ 12 mm; genişlik, uzunluk veya çap ≤ 50 mm. Uyan makinalı masa-"
        "çalar saat 91.03; sarkaçlı, büyük veya senkron motorlu 91.05.",
        "<b>Not 1:</b> saat camı ve ağırlığı maddesine göre, saat zinciri 71.13 / 71.17, genel kullanım parçası "
        "ve rulman fasıl dışı; saat yayı ise 91.14’te.",
        "<b>Bölüm XVIII = Fasıl 90–92</b> (bölüm notu yok): güneş gözlüğü, kol saati ve gitar aynı bölümde; "
        "tabanca Bölüm XIX (Fasıl 93).",
    ],
    "karistirilan": [
        ["Metronom", "92.09", "Zaman ölçse de Fasıl 91 değil"],
        ["Pedometre, taksimetre", "90.29", "Sayaç niteliğinde; saat değil"],
    ],
}

# ---------------------------------------------------------------- 92 (C)
H[92] = {
    "tur": "hap", "fasil": 92, "kademe": "C",
    "sinavda": "Son 5 sınavda 1 kez konu: piyano ile birlikte getirilen hafıza kartı 92.09 (Not 2; 85.23 ve 92.01 "
               "çeldirici). Seçenekte: gitar, kol saati ve güneş gözlüğüyle aynı bölümde (XVIII).",
    "pozisyonlar": [
        ["92.01", "Piyano, klavsen; klavyeli telli (otomatik piyano dahil)"],
        ["92.02", "Diğer telli: keman, gitar, mandolin, arp"],
        ["92.07", "Elektriksiz normal çalınamayan elektrikli-elektronik alet"],
        ["92.09", "Aksam, tel, metronom, diyapozon, kart-disk-rulo"],
    ],
    "hap": [
        "<b>Not 2:</b> 92.02 ve 92.06 aletleriyle gelen normal sayıdaki yay ve baget aletle sınıflandırılır; "
        "92.09’daki kart, disk ve rulolar aletle gelse de ayrı eşyadır.",
        "<b>Elektrik ölçütü:</b> elektriksiz normal çalınamayan alet 92.07 (ses kutusuz elektro gitar, elektronik "
        "org); pikaplı ses kutulu gitar 92.02; elektrikli otomatik piyano 92.01.",
        "<b>Fasıl dışı:</b> alete takılmamış mikrofon, amplifikatör, hoparlör Fasıl 85; oyuncak çalgı "
        "95.03; temizleme fırçası 96.03; tripod 96.20; elektronik müzik modülü 85.43.",
    ],
    "karistirilan": [
        ["Piyanoyla gelen hafıza kartı", "92.09", "Not 2: aletle gelse de ayrı eşya; 92.01 değil"],
        ["Akordeon, borulu org", "92.05", "Klavyeli ama nefesli; 92.01 değil"],
    ],
}

# ---------------------------------------------------------------- kontrol ve yazım
LIM = {"A": ((8, 12), (6, 8), (4, 6)), "B": ((4, 6), (4, 5), (2, 3)), "C": ((2, 4), (2, 3), (1, 2))}


def wc(s):
    return len(re.sub(r"<[^>]+>", "", s).split())


def kontrol(d):
    k = d["kademe"]
    (p0, p1), (h0, h1), (k0, k1) = LIM[k]
    n = d["fasil"]
    assert p0 <= len(d["pozisyonlar"]) <= p1, (n, "pozisyonlar", len(d["pozisyonlar"]))
    assert h0 <= len(d["hap"]) <= h1, (n, "hap", len(d["hap"]))
    assert k0 <= len(d["karistirilan"]) <= k1, (n, "karistirilan", len(d["karistirilan"]))
    for c, t in d["pozisyonlar"]:
        assert re.fullmatch(r"\d\d\.\d\d", c), (n, c)
        assert wc(t) <= 8, (n, "poz", wc(t), t)
    for b in d["hap"]:
        assert wc(b) <= 30, (n, "hap", wc(b), b[:60])
    for e, c, w in d["karistirilan"]:
        assert wc(e) <= 8, (n, "kar eşya", wc(e), e)
        assert wc(w) <= 12, (n, "kar neden", wc(w), w)


os.makedirs(OUT, exist_ok=True)
for n, d in H.items():
    kontrol(d)
    with open(os.path.join(OUT, f"fasil_{n:02d}.json"), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print("yazıldı", n)
