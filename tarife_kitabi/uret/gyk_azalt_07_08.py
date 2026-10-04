#!/usr/bin/env python3
"""GYK azaltma: karma_07 s15, s20 ve karma_08 s20 GYK sorularını başka tipte yeni sorularla değiştirir.

Plan: KITAP/kaynak/gyk_azaltma_plani.json → 7: [[15, 85, "Olumsuz teşhis"], [20, 84, "Eşya → 4’lü pozisyon"]],
8: [[20, 96, "Farklı/aynı pozisyon veya fasıl"]].
Cevap harfi korunur (4 × A…E dengesi bozulmaz); diğer sorulara dokunulmaz.
Kaynak: kaynak/fasillar/FASIL84.txt, FASIL85.txt, FASIL96.txt.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def q(soru, secenekler, cevap, tip, gerekce, dayanak, fasil):
    assert len(secenekler) == 5, soru
    assert len(gerekce) <= 420 and len(gerekce.split()) <= 45, (len(gerekce), len(gerekce.split()), soru)
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak, "fasil": fasil}


DEGISIM = {
    7: {
        # 15 – Fasıl 85 · Olumsuz teşhis (E)
        15: q(
            "Aşağıdakilerden hangisi 85.14 tarife pozisyonunda <b>sınıflandırılmaz</b>?",
            ["Bisküvi imalatında kullanılan, kızılötesi ve yüksek frekanslı ısıtmayı birlikte kullanan elektrikli fırın",
             "Krank millerinin ve dişli çarkların yüzeyini endüksiyon yoluyla sertleştiren makine",
             "Atıkların yakılarak yok edilmesinde kullanılan elektrikli ocak",
             "Ağacı yüksek frekanslı güçle dielektrik kaybı yoluyla ısıtarak kurutan makine",
             "Yalnızca yarı iletken disk (wafer) imalatında kullanılan türden elektrikli difüzyon fırını"],
            "E", "Olumsuz teşhis",
            "85.14 Açıklama Notu yarı iletken disk veya düz panel ekran imalatına mahsus elektrikli fırınları hariç "
            "tutar; bunlar Fasıl 84 Not 11(D) gereği 84.86’dadır. Bisküvi fırını, atık yakma ocağı, endüksiyonla "
            "sertleştirme ve dielektrik kayıpla ağaç kurutma makineleri 85.14’te sayılır; kurutma işlevi 84.19’a "
            "götürmez.",
            "85.14 Açıklama Notu (I), (II) ve hariç tutulanlar; Fasıl 84 Not 11(D); 84.86 Açıklama Notu.",
            85),
        # 20 – Fasıl 84 · Eşya → 4’lü pozisyon (D)
        20: q(
            "Tarife Cetveline göre, plastik şişe kapağı üretiminde kullanılan bir enjeksiyon makinesine takılmak "
            "üzere tasarlanmış, ayrı olarak sunulan çok gözlü çelik enjeksiyon kalıbı hangi tarife pozisyonunda "
            "sınıflandırılır?",
            ["84.77", "82.07", "84.54", "84.80", "84.87"],
            "D", "Eşya → 4’lü pozisyon",
            "84.80 pozisyon metni kauçuk ve plastik maddeler için kalıpları açıkça sayar; 84.77 Açıklama Notu da "
            "makinenin aksam-parçaları arasından 84.80’deki kalıpları hariç tutar. Stampaj kalıpları 82.07’de, "
            "külçe kalıpları 84.54’te yer alır; tuzak, kalıbı makine parçası sayıp 84.77’ye götürmektir.",
            "84.80 pozisyon metni ve Açıklama Notu; 84.77 Açıklama Notu (aksam ve parçalar).",
            84),
    },
    8: {
        # 20 – Fasıl 96 · Farklı/aynı pozisyon veya fasıl (C)
        20: q(
            "Tarife Cetveline göre aşağıdaki eşyadan hangisi, elle kullanılan numaratör ile aynı tarife "
            "pozisyonunda sınıflandırılır?",
            ["Koyun kulağını ve diğer hayvanları markalamaya mahsus pens",
             "Masaya sabitlenmeye mahsus kaidesi bulunan tarih damgası",
             "Oyuncak niteliğinde olmayan; kumpas, harf, cımbız ve ıstampa içeren kutulu el baskı takımı",
             "Ayrı olarak sunulan, mürekkep emdirilmiş kutulu ıstampa",
             "Çekiçle vurularak kullanılan, metal eşyaya işaret basmaya mahsus zımba"],
            "C", "Farklı/aynı pozisyon veya fasıl",
            "96.11 Açıklama Notu, elle kullanılan numaratörlerle birlikte kutu içinde kumpas, değiştirilebilir "
            "karakter, cımbız ve ıstampadan oluşan küçük el baskı takımlarını da (oyuncaklar hariç) kapsar. "
            "Markalama pensi 82.03’te, işaretleme zımbası 82.05’te, kaideli damga 84.72’de, ayrı ıstampa "
            "96.12’dedir.",
            "96.11 ve 96.12 pozisyon metinleri ve Açıklama Notları; 84.72 Açıklama Notu.",
            96),
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
            # yalnız GYK sorusu değiştirilir; betik ikinci kez çalışırsa aynı soruyu yeniden yazar
            assert eski["fasil"] == "GYK" or eski["soru"] == yeni["soru"], (no, sira, eski["fasil"])
            d["sorular"][sira - 1] = yeni
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("yazıldı:", yol, sorted(degisim))


if __name__ == "__main__":
    main()
