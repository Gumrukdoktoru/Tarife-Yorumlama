#!/usr/bin/env python3
"""Hap bilgi sayfaları – grup H7: Fasıl 84 (A) ve Fasıl 85 (A)."""
import json
import os
import re

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KITAP, "hap")

F84 = {
    "tur": "hap",
    "fasil": 84,
    "kademe": "A",
    "sinavda": (
        "Son 5 sınavda 14 soruda konu, 8’inde seçenek; ağırlık eşya → 4’lü pozisyon: deniz taşıtı dizel motoru "
        "84.08, traktöre takılan kültivatör 84.32 (iki kez), boş çelik yangın söndürücü 84.24, poşette farklı "
        "maddeden contalar 84.84, buz pisti düzeltme makinası 84.79, demonte işleme merkeziyle gelen montaj aleti "
        "84.57. Ayrıca “hangisi yer almaz” (84.18’de eşanjör; ayakkabıyla ilgisiz 84.54), Not 9 cep tipi ölçüsü, ayrı parça pozisyonu "
        "olmayan makina (84.77) ve 84.68’in elektriklisi (85.15) soruldu."
    ),
    "pozisyonlar": [
        ["84.08", "Dizel motorlar; gemi motoru dahil"],
        ["84.18", "Buzdolabı, dondurucu, ısı pompası; eşanjör değil"],
        ["84.19", "Isı değişikliğiyle işleme, eşanjör; ev tipi hariç"],
        ["84.24", "Püskürtme cihazı; yangın söndürücü dolu-boş"],
        ["84.32", "Toprak işleme-ekim; traktöre takılan dahil"],
        ["84.54", "Konvertisör, döküm potası, külçe kalıbı, döküm makinası"],
        ["84.57", "Metal işleme merkezi, transfer tezgâhı (Not 4)"],
        ["84.68", "Gazla lehim-kaynak; elektriklisi 85.15"],
        ["84.70", "Hesap makinası, yazar kasa, POS; cep tipi"],
        ["84.77", "Kauçuk-plastik işleme; ayrı parça pozisyonu yok"],
        ["84.79", "Kendine özgü fonksiyonlu, başka yerde yok"],
        ["84.84", "Farklı maddeden conta takımı; mekanik salmastra"],
    ],
    "hap": [
        "<b>Bölüm XVI Not 1 (dışarıda):</b> kauçuk kolan-conta (40.10, 40.16), deri ve tekstil teknik eşya "
        "(42.05, 59.10, 59.11), masura-bobin, genel kullanım adi metal parça, Fasıl 82, 83, 90, 91, 95, "
        "Bölüm XVII, tripod 96.20.",
        "<b>Elektrikli olmak 85 demek değil:</b> 84’teki makina elektrikli de olsa 84’te; 85’e gidenler adıyla "
        "sayılır: süpürge 85.08, ev tipi elektromekanik 85.09, elektrikli kaynak 85.15, elektrikli şofben 85.16. Seramik "
        "makina Fasıl 69, laboratuvar camı 70.17.",
        "<b>Bölüm XVI Not 2 (parça):</b> kendi pozisyonu olan parça (pompa, valf, rulman, dişli, motor) daima "
        "orada; belirli makinaya özgü olan o makinanın pozisyonunda veya parça pozisyonunda; kalan elektriksiz "
        "84.87, elektrikli 85.48.",
        "<b>Ayrı parça pozisyonları:</b> pistonlu motor → 84.09, kaldırma-toprak (asansör dahil) → 84.31, tekstil "
        "(dokuma dahil) → 84.48, takım tezgâhı (torna dahil) → 84.66, büro → 84.73; plastik makinası (84.77) "
        "parçası kendi pozisyonunda.",
        "<b>Bölüm XVI Not 3–5:</b> kombine veya çok işlevli makina esas fonksiyonuna göre (Not 3); tek fonksiyonu "
        "birlikte gören ayrı elemanlar fonksiyonel birim, hidrolik sistem 84.12 gibi (Not 4); “makina” = "
        "84–85’teki her cihaz (Not 5).",
        "<b>Fasıl 84 Not 2–3:</b> hem 84.01–84.24 hem 84.25–84.80’e uyan makina ilk grupta; istisna: kuluçka "
        "84.36, tekstil ısıl işlem 84.51, çuval dikme 84.52, mürekkep püskürtmeli baskı 84.43; lazer-su jeti "
        "84.56 tezgâhlara üstün.",
        "<b>Rakamlar:</b> cep tipi ≤ 170 x 100 x 45 mm, hiçbir ölçü aşılamaz (Not 9); çelik bilyada çap sapması "
        "%1 veya 0,05 mm’yi (hangisi azsa) geçmezse 84.82, geçerse 73.26 (Not 7).",
        "<b>84.71 (Not 6):</b> program depolar, serbestçe programlanır, aritmetik hesap yapar, insan müdahalesiz "
        "mantıksal kararla akışı değiştirir; klavye ve mouse 84.71, yazıcı-faks 84.43, ağ cihazı 85.17, "
        "monitör 85.28.",
    ],
    "karistirilan": [
        ["Deniz taşıtı dizel motoru", "84.08", "Motor nerede kullanılırsa kullanılsın 84’te; Fasıl 89 değil"],
        ["Traktöre takılan kültivatör, pulluk", "84.32", "Traktörle gelse de 84.32; traktör ayrıca 87.01"],
        ["Isı değiştirici (eşanjör)", "84.19", "84.18 değil; 84.18 soğutucu, dondurucu, ısı pompası"],
        ["Elektrikli kaynak makinası", "85.15", "84.68 yalnız elektriksiz (gazla) olanlar"],
        ["Poşette plastik, kauçuk, çelik contalar", "84.84", "Farklı maddeden takım; tek kauçuk conta 40.16"],
        ["Kendinden hareketli buz pisti düzeltme makinası", "84.79",
         "Özgün fonksiyon; 84.29, 84.30 veya 87.05 değil"],
    ],
}

F85 = {
    "tur": "hap",
    "fasil": 85,
    "kademe": "A",
    "sinavda": (
        "Son 5 sınavda 13 soruda konu, 7’sinde seçenek: “hangisi yer almaz” (85.28’de katot ışınlı tüp, 85.09’da "
        "fırın), not tanımları (85.24 modülü video dönüştürücü içermez; notlarda radar yok), sıralama (trafo – el "
        "feneri – baskılı devre – atık pil; MP3 çalar – cep radyosu), eşya → pozisyon (cam silici 85.12, e-sigara "
        "85.43 / kartuş 24.04), farklı pozisyon (izolatör 85.46) ve 84.68’in elektriklisi 85.15."
    ),
    "pozisyonlar": [
        ["85.04", "Trafo, statik konvertör: şarj cihazı, UPS"],
        ["85.09", "Motorlu ev cihazı; ≤ 20 kg (Not 4)"],
        ["85.12", "Taşıt aydınlatma-işaret, cam silici, korna"],
        ["85.15", "Elektrikli lehim-kaynak; 84.68’in elektriklisi"],
        ["85.16", "Elektrotermik ev cihazı, ısıtıcı, ev fırını"],
        ["85.24", "Düz panel modülü; Not 7, öncelikli"],
        ["85.28", "Monitör, projektör, TV alıcısı (tuner varsa)"],
        ["85.34", "Baskılı devre (Not 8); yarı iletken içermez"],
        ["85.40", "Katotlu tüp-valf: katot ışınlı tüp, magnetron"],
        ["85.43", "Artık: e-sigara, IR kumanda, yükselteç, dedektör"],
        ["85.46", "Her maddeden izolatör (cam, porselen)"],
        ["85.49", "E-atık, hurda pil-akü (Bölüm XVI Not 6)"],
    ],
    "hap": [
        "<b>Önce Fasıl 84:</b> 84’te tanımlı makina elektrikli de olsa 84’te (bulaşık, çamaşır, buzdolabı, "
        "klima, bilgisayar, faks). Not 1 dışı: elektrikle ısıtılan battaniye-giysi, 70.11 cam zarf, tıbbi vakum "
        "90.18, ısıtmalı mobilya.",
        "<b>Parça (Bölüm XVI Not 2):</b> kendi pozisyonu olan parça orada (kömür fırça 85.45, kondansatör 85.32, "
        "elektromıknatıs 85.05); cihaza özgü olan 85.03, 85.22, 85.29, 85.38’de; kalan elektrikli parça 85.48.",
        "<b>85.09 ve fırın:</b> motoru bünyesinde ev cihazı; yer cilalama, öğütücü-karıştırıcı, meyve presi "
        "ağırlıksız, diğerleri ≤ 20 kg. Fırın 85.09’da yok: 73.21 elektriksiz ev, 84.17 elektriksiz sanayi, 85.14 "
        "elektrikli sanayi, 85.16 ev.",
        "<b>85.24 (Not 7):</b> en az bir ekranlı, başka eşyaya monte edilmek üzere tasarlanmış modül; düz, "
        "kavisli, esnek olabilir; video sinyali dönüştüren bileşen (ölçekleyici, kod çözücü IC) içermez; diğer "
        "pozisyonlara önceliklidir.",
        "<b>Not 12 önceliği:</b> yarı iletken ve LED 85.41, entegre devre (monolitik, hibrit, çoklu çip, MCO) "
        "85.42 diğer pozisyonlara önceliklidir; istisna: akıllı kart ve flash bellek 85.23’te (Not 6).",
        "<b>Notlarda tanımlı:</b> akıllı telefon (5), flash bellek ve akıllı kart (6), düz panel modülü (7), "
        "baskılı devre (8), optik lif konnektörü (9), LED modül-ampul (11), yarı iletken, entegre devre (12); "
        "radar yok.",
        "<b>Eşikler:</b> anahtar-sigorta-fiş 1000 V’a kadar 85.36, üstü 85.35; iki veya daha fazla cihazlı pano "
        "85.37. Şarjsız pil 85.06, akü 85.07. Tabanlı LED ampul 85.39, tek LED 85.41.",
        "<b>Sıra iskeleti:</b> 85.04 trafo, 85.07 akü, 85.13 el feneri, 85.16 ısıtıcı, 85.17 telefon, 85.19 "
        "ses-MP3, 85.21 video-DVD, 85.27 radyo, 85.28 monitör-TV, 85.34 baskılı devre, 85.39 ampul, 85.49 e-atık.",
    ],
    "karistirilan": [
        ["Otomobil elektrik motorlu cam silicisi", "85.12", "87.08 değil; Fasıl 85 eşyası taşıt parçası sayılmaz"],
        ["Katot ışınlı TV görüntü tüpü", "85.40", "85.28 değil; monitör ve TV alıcısı 85.28"],
        ["Dizüstü bilgisayar LCD ekran modülü", "85.24", "Not 7 önceliği; 84.73 parça pozisyonuna gitmez"],
        ["E-sigara kartuşu; tek kullanımlık e-sigara", "24.04", "Şarjlı-doldurulabilir e-sigara 85.43; sigara 24.02"],
        ["Kameralı uzaktan kumandalı drone", "88.06", "85.25 değil; insansız hava taşıtı"],
        ["Kızılötesi TV kumandası", "85.43", "Telsiz kumanda 85.26; 85.37 değil (Not 10)"],
    ],
}


def kelime(s):
    s = re.sub(r"^<b>.*?</b>", "", s)  # kalın anahtar ifade sayılmaz
    return len([w for w in re.sub(r"<[^>]+>", "", s).split() if re.search(r"\w", w)])


def kontrol(d):
    n = d["fasil"]
    for p, a in d["pozisyonlar"]:
        if kelime(a) > 8:
            print(f"  uyarı {n}: pozisyon {p} {kelime(a)} kelime")
    for h in d["hap"]:
        if kelime(h) > 30:
            print(f"  uyarı {n}: hap {kelime(h)} kelime: {h[:50]}")
    for e, p, w in d["karistirilan"]:
        if kelime(e) > 8 or kelime(w) > 12:
            print(f"  uyarı {n}: karıştırılan {e!r} ({kelime(e)}/{kelime(w)} kelime)")


for d in (F84, F85):
    kontrol(d)
    path = os.path.join(OUT, f"fasil_{d['fasil']:02d}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print("yazıldı:", path)
