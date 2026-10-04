"""Fasıl 78–83 modülleri için ortak yardımcılar."""
import json
import os
from collections import Counter

KITAP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def soru(soru, secenekler, cevap, tip, gerekce, dayanak):
    assert len(secenekler) == 5, soru
    assert cevap in "ABCDE", soru
    return {"soru": soru, "secenekler": secenekler, "cevap": cevap, "tip": tip,
            "gerekce": gerekce, "dayanak": dayanak}


def kaydet(obj, nn):
    for q in obj["sorular"]:
        # I–IV listeleri düz metinde satır içi yazılır (yalnız <b>, <i> serbest)
        q["soru"] = q["soru"].replace("<br/>", " ")
    sayac = Counter(q["cevap"] for q in obj["sorular"])
    tipler = Counter(q["tip"] for q in obj["sorular"])
    print("cevaplar:", dict(sorted(sayac.items())))
    print("tipler:", dict(tipler))
    yol = os.path.join(KITAP, "data", f"fasil_{nn:02d}.json")
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print("yazıldı:", yol)
