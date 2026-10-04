"""Fasıl 19–23 modülleri için ortak yardımcı: soru listesi kurma, kontrol ve kaydetme."""
import json
import os
import re
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIPLER = {
    "E4": "Eşya → 4’lü pozisyon",
    "OT": "Olumsuz teşhis",
    "FA": "Farklı/aynı pozisyon veya fasıl",
    "TN": "Fasıl notu · Tanım/Eşik",
    "GYK": "Genel Yorum Kuralı",
    "ES": "Eşleştirme / Boşluk doldurma",
    "CC": "Çoktan-çoğa (I–IV)",
    "SN": "Senaryo",
}
BEKLENEN = {"E4": 5, "OT": 4, "FA": 4, "TN": 4, "GYK": 2, "ES": 2, "CC": 2, "SN": 2}


def S(tip, soru, secenekler, cevap, gerekce, dayanak):
    assert tip in TIPLER, tip
    assert len(secenekler) == 5, soru
    assert cevap in "ABCDE"
    return {
        "soru": soru,
        "secenekler": secenekler,
        "cevap": cevap,
        "tip": TIPLER[tip],
        "gerekce": gerekce,
        "dayanak": dayanak,
        "_k": tip,
    }


def kaydet(obj, nn):
    qs = obj["sorular"]
    assert len(qs) == 25, len(qs)
    harf = Counter(q["cevap"] for q in qs)
    assert all(harf[L] == 5 for L in "ABCDE"), harf
    tip = Counter(q["_k"] for q in qs)
    for k, v in BEKLENEN.items():
        if tip[k] != v:
            print(f"  uyarı: tip {k} sayısı {tip[k]} (beklenen {v})")
    # doğru şıkkın sistematik olarak en uzun olmaması
    def _tek_en_uzun(q):
        L = [len(o) for o in q["secenekler"]]
        c = L["ABCDE".index(q["cevap"])]
        return c == max(L) and L.count(c) == 1
    en_uzun = sum(1 for q in qs if _tek_en_uzun(q))
    print(f"  doğru şık en uzun olan soru sayısı: {en_uzun}/25")
    print("  cevap sırası:", "".join(q["cevap"] for q in qs))
    for q in qs:
        del q["_k"]
    yol = os.path.join(KITAP, "data", f"fasil_{nn:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", yol)
