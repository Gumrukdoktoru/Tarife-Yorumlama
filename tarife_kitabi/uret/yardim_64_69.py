"""Fasıl 64–69 üreteçleri için ortak yardımcılar."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARF = "ABCDE"


def soru(metin, dogru, celdiriciler, harf, tip, gerekce, dayanak):
    assert len(celdiriciler) == 4, metin
    assert dogru not in celdiriciler, metin
    i = HARF.index(harf)
    secenekler = list(celdiriciler)
    secenekler.insert(i, dogru)
    return {"soru": metin, "secenekler": secenekler, "cevap": harf, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def yaz(obj):
    c = Counter(q["cevap"] for q in obj["sorular"])
    assert all(c[h] == 5 for h in HARF), c
    assert len(obj["sorular"]) == 25
    yol = os.path.join(KITAP, "data", "fasil_%02d.json" % obj["fasil"])
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", yol, dict(sorted(c.items())), Counter(q["tip"] for q in obj["sorular"]))
