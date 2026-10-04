#!/usr/bin/env python3
"""GYK payını azaltma: karma_01 (s17, s20) ve karma_02 (s18) sorularını yeni fasıl sorularıyla değiştirir.

Plan: KITAP/kaynak/gyk_azaltma_plani.json. Değiştirilen sorunun cevap harfi korunur (4'er harf dengesi);
diğer sorulara dokunulmaz.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def q(fasil, tip, soru, secenekler, cevap, gerekce, dayanak):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


YENI = {
    1: {
        # s17 — Fasıl 33 · Fasıl notu · Tanım/Eşik (A)
        17: q(33, "Fasıl notu · Tanım/Eşik",
              "Tarife Cetvelinin 33.01 pozisyonu Açıklama Notuna göre, uçucu yağların, rezinoitlerin ve "
              "ekstraksiyonla elde edilen yağ reçinelerinin bu pozisyonda kalma şartlarıyla ilgili aşağıdaki "
              "ifadelerden hangisi <b>yanlıştır</b>?",
              ["Çıkarılmaları sırasında kullanılan çözücüden (etil alkol gibi) az bir miktar kalmışsa "
               "pozisyon dışında kalırlar.",
               "Temel maddelerinin bir kısmı giderilerek veya eklenerek standardize edilenler, bileşimleri "
               "tabii hâlin normal sınırları içindeyse pozisyonda kalır.",
               "Fraksiyonlarına ayrılarak bileşimi orijinal üründen önemli derecede farklı hâle getirilenler "
               "pozisyon dışında kalır.",
               "Terpenlerinin alınmasıyla kokuları değişikliğe uğratılmış uçucu yağlar pozisyonda kalır.",
               "Uçucu yağlardan izole edilen, kimyaca belirli yapıdaki bileşikler pozisyon dışında kalır."],
              "A",
              "33.01 Açıklama Notu, çıkarmada kullanılan çözücünün az miktarda kalmasının ürünü pozisyon dışına "
              "çıkarmadığını açıkça belirtir. Normal sınırlarda standardize edilenler ve terpeni alınanlar "
              "33.01’de kalır; önemli derecede tadil edilenler 33.02’ye, izole kimyasal bileşikler Fasıl 29’a gider.",
              "33.01 pozisyon metni ve Açıklama Notu."),
        # s20 — Fasıl 48 · Fasıl/Bölüm bulma (D)
        20: q(48, "Fasıl/Bölüm bulma",
              "Kapı ve pencere camlarına yapıştırılmaya hazır ebatta kesilmiş; camı taklit etmek üzere "
              "renklendirilmiş ve üzerine süs mahiyetinde desenler basılmış, ince, sert ve çok parlak yarı "
              "saydam kâğıttan “cam kâğıdı” Tarife Cetvelinin hangi faslında yer almaktadır?",
              ["Fasıl 70", "Fasıl 49", "Fasıl 39", "Fasıl 48", "Fasıl 59"],
              "D",
              "48.14 metni duvar kâğıtlarıyla birlikte cam kâğıtlarını sayar; Fasıl 48 Not 12 gereği desen basılı "
              "olmaları onları Fasıl 49’a götürmez. Benzeyen çıkartmalar 49.08’e, yalnız plastikten kaplamalar "
              "Fasıl 39’a, kâğıt mesnetli dokuma kaplamalar 59.05’e girer; “cam” adı Fasıl 70 tuzağıdır.",
              "48.14 pozisyon metni ve Açıklama Notu (B); Fasıl 48 Not 12."),
    },
    2: {
        # s18 — Fasıl 90 · Eşya → 4’lü pozisyon (A)
        18: q(90, "Eşya → 4’lü pozisyon",
              "Tarife Cetveline göre, hekimlerin hastanın kan basıncını ölçmekte kullandığı, göstergesi madeni "
              "manometre tipinde olan tansiyon aleti (sfigmomanometre) hangi tarife pozisyonunda sınıflandırılır?",
              ["90.18", "90.26", "90.25", "90.31", "90.19"],
              "A",
              "90.18 Açıklama Notu, özel teşhis aletleri arasında kan basıncını ölçen sfigmomanometre, tansiyometre "
              "ve osilometreleri sayar; manometreli göstergesi eşyayı 90.26’ya götürmez. Tıpta kullanılan "
              "termometrelerin 90.25’e gitmesi tansiyon aletine uygulanmaz.",
              "90.18 Açıklama Notu (B)(3); 90.26 pozisyon metni."),
    },
}


def main():
    for no, degisim in YENI.items():
        yol = os.path.join(ROOT, "karma", f"karma_{no:02d}.json")
        with open(yol, encoding="utf-8") as f:
            d = json.load(f)
        for sira, yeni in degisim.items():
            eski = d["sorular"][sira - 1]
            assert eski["cevap"] == yeni["cevap"], (no, sira, eski["cevap"], yeni["cevap"])
            d["sorular"][sira - 1] = yeni
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("yazıldı:", yol, sorted(degisim))


if __name__ == "__main__":
    main()
