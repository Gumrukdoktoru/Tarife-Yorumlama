#!/usr/bin/env python3
"""GYK azaltma: karma_05 s19 ve karma_06 s13, s16 GYK sorularını başka tipte yeni sorularla değiştirir.

Plan: KITAP/kaynak/gyk_azaltma_plani.json → 5: [[19, 85, "Olumsuz teşhis"]],
6: [[13, 39, "Pozisyon → eşya"], [16, 85, "Eşya → 4’lü pozisyon"]].
Cevap harfi korunur (4 × A…E dengesi bozulmaz); diğer sorulara dokunulmaz.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def q(soru, secenekler, cevap, tip, gerekce, dayanak, fasil):
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


DEGISIM = {
    5: {
        # 19 – Fasıl 85 · Olumsuz teşhis (C)
        19: q(
            "Tarife Cetveline göre aşağıdaki makine ve cihazlardan hangisi 85.15 pozisyonunda "
            "<b>sınıflandırılmaz</b>?",
            ["Plastik filmleri ultrasonik dalgalarla birbirine kaynaştıran makine",
             "Termoplastikleri elektrikle ısıtılmış havayla birleştiren sıcak gaz kaynak cihazı",
             "Parçaları birbirine sürterek oluşan ısıyla birleştiren sürtünmeli kaynak makinesi",
             "Kaynak yapmak üzere özel olarak düzenlenmiş sanayi robotu",
             "Metalleri elektrik arkıyla eritip sıkıştırılmış havayla püskürten cihaz"],
            "C", "Olumsuz teşhis",
            "85.15 Açıklama Notu sürtünmeli (friction) kaynak makinalarını pozisyon dışında bırakıp 84.68’e "
            "gönderir; ısı elektrikle değil sürtünmeyle elde edilir. Ultrasonik ve sıcak gaz kaynak cihazları, "
            "kaynak robotları ve elektrik arklı metal püskürtme cihazları 85.15’te açıkça sayılır.",
            "85.15 Açıklama Notu (I), (II) ve hariç tutulanlar; 84.68.",
            85),
    },
    6: {
        # 13 – Fasıl 39 · Pozisyon → eşya (C)
        13: q(
            "Tarife Cetveline göre aşağıdakilerden hangisi 39.12 pozisyonunda sınıflandırılır?",
            ["Karboksimetilselüloz doldurulmuş, buz kabı olarak kullanılan plastik kap",
             "Kâfurla plastikleştirilmiş selüloz nitrattan (selüloit) çubuklar",
             "Kalınlaştırıcı olarak kullanılan, toz halindeki karboksimetilselüloz",
             "Rejenere selülozdan elde edilmiş, dokumaya elverişli suni lifler",
             "Selüloz asetattan yapılmış ince şeffaf film"],
            "C", "Pozisyon → eşya",
            "39.12 selüloz ve kimyasal türevlerini yalnız ilk şekillerde kapsar; toz halindeki karboksimetilselüloz "
            "bir selüloz eteridir. Selüloit çubuk ve selüloz asetat film 39.16/39.20–39.21’e, rejenere selüloz "
            "lifleri Fasıl 54–55’e, CMC dolu plastik buz kabı 39.26’ya gider.",
            "Fasıl 39 Not 6; 39.12 ve 39.26 Açıklama Notları.",
            39),
        # 16 – Fasıl 85 · Eşya → 4’lü pozisyon (A)
        16: q(
            "Tarife Cetveline göre; farklı elektronik cihazları beslemek üzere tasarlanmış, bir regülatörle "
            "kombine haldeki redresörlerden oluşan kesintisiz güç kaynağı ünitesi hangi tarife pozisyonunda "
            "sınıflandırılır?",
            ["85.04", "85.07", "90.32", "85.02", "85.43"],
            "A", "Eşya → 4’lü pozisyon",
            "85.04 Açıklama Notu stabilize güç kaynaklarını, örneğin elektronik cihazlar için kesintisiz güç "
            "kaynağı ünitelerini statik konvertör sayar. Otomatik voltaj regülatörleri 90.32’de, elektrojen "
            "grupları 85.02’de, akümülatörler 85.07’dedir; “güç kaynağı” adı jeneratöre götürmez.",
            "85.04 Açıklama Notu (II) Statik konvertörler; 90.32 ve 85.02 pozisyon metinleri.",
            85),
    },
}


def main():
    for no, degisim in DEGISIM.items():
        yol = os.path.join(ROOT, "karma", f"karma_{no:02d}.json")
        with open(yol, encoding="utf-8") as f:
            d = json.load(f)
        for sira, yeni in degisim.items():
            eski = d["sorular"][sira - 1]
            assert eski["cevap"] == yeni["cevap"], (no, sira, eski["cevap"], yeni["cevap"])
            assert eski["fasil"] == "GYK" or eski["soru"] == yeni["soru"], (no, sira, eski["fasil"])
            d["sorular"][sira - 1] = yeni
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("yazıldı:", yol, sorted(degisim))


if __name__ == "__main__":
    main()
